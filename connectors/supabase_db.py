#!/usr/bin/env python3
"""Supabase/Postgres connector -> masked daily DB snapshot in raw/.

Connects READ-ONLY to the wih-app Supabase Postgres (DATABASE_URL), inventories
public tables with row counts, and shows a few recent rows from CRM-relevant
tables. Writes raw/supabase-snapshot-DATE.md (masked). Self-skips (exit 0) if
DATABASE_URL is absent. Never writes to the database (connection is read_only).
"""
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
MAX_TABLES_DETAIL = 25     # show recent rows for up to this many tables
RECENT_ROWS = 5
MAX_COLS = 6
CELL_CHARS = 40
CRM_HINTS = ("contact", "lead", "property", "properties", "deal", "opportunit",
             "message", "conversation", "task", "tenant", "owner", "seller",
             "buyer", "campaign", "appointment", "note", "user")

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text


def load_db_url():
    import os
    for src in (REPO / ".env", Path(r"C:\Users\joshu\wih-app\.env")):
        if src.exists():
            for line in src.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = line.strip()
                if line.startswith("DATABASE_URL=") and "=" in line:
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("DATABASE_URL")


def with_ssl(url: str) -> str:
    if "sslmode=" in url:
        return url
    return url + ("&" if "?" in url else "?") + "sslmode=require"


def cell(v) -> str:
    s = "" if v is None else str(v)
    s = s.replace("|", "\\|").replace("\n", " ")
    return s[:CELL_CHARS]


def main() -> int:
    url = load_db_url()
    if not url:
        print("supabase connector: DATABASE_URL not set -- skipping (no error).")
        return 0
    try:
        import psycopg
    except Exception:
        print("supabase connector: psycopg not installed -- skipping.")
        return 0
    try:
        conn = psycopg.connect(with_ssl(url), connect_timeout=30)
    except Exception as e:
        print(f"supabase connector: connect failed ({type(e).__name__}: {e}); skipping.")
        return 0

    d = datetime.now().strftime("%Y-%m-%d")
    try:
        conn.read_only = True  # enforce: no writes possible on this connection
        with conn.cursor() as cur:
            cur.execute(
                "SELECT table_name FROM information_schema.tables "
                "WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name"
            )
            tables = [r[0] for r in cur.fetchall()]

            counts = {}
            for t in tables:
                try:
                    cur.execute(f'SELECT count(*) FROM "{t}"')
                    counts[t] = cur.fetchone()[0]
                except Exception:
                    counts[t] = "?"

            # columns per table
            cur.execute(
                "SELECT table_name, column_name FROM information_schema.columns "
                "WHERE table_schema='public' ORDER BY table_name, ordinal_position"
            )
            cols = {}
            for tn, cn in cur.fetchall():
                cols.setdefault(tn, []).append(cn)

            out = [
                "---",
                f"name: source-supabase-snapshot-{d}",
                "type: source",
                "tags: [supabase, wih-app, database, crm, snapshot]",
                f"sources: [supabase-snapshot-{d}.md]",
                f"updated: {d}",
                "---",
                f"# Supabase (wih-app DB) Snapshot -- {d}",
                "",
                f"**Summary**: Read-only snapshot of the [[wih-app]] Supabase Postgres -- "
                f"{len(tables)} public tables.",
                "",
                f"**Sources**: supabase-snapshot-{d}.md (Postgres, read-only)",
                "",
                f"**Last updated**: {d}",
                "",
                "---",
                "",
                "## Tables (row counts)",
                "| Table | Rows |",
                "|---|---|",
            ]
            for t in tables:
                out.append(f"| {t} | {counts.get(t)} |")

            # pick CRM-relevant tables (or biggest) for recent-row detail
            def is_crm(t):
                return any(h in t.lower() for h in CRM_HINTS)
            detail = [t for t in tables if is_crm(t)][:MAX_TABLES_DETAIL]

            out += ["", "## Recent rows (CRM-relevant tables)"]
            for t in detail:
                tcols = cols.get(t, [])
                order = next((c for c in ("updated_at", "created_at", "inserted_at", "id")
                              if c in tcols), None)
                shown = tcols[:MAX_COLS]
                try:
                    q = f'SELECT {", ".join(chr(34)+c+chr(34) for c in shown)} FROM "{t}"'
                    if order:
                        q += f' ORDER BY "{order}" DESC'
                    q += f" LIMIT {RECENT_ROWS}"
                    cur.execute(q)
                    rows = cur.fetchall()
                except Exception as e:
                    out.append(f"\n### {t}\n_(could not read: {type(e).__name__})_")
                    continue
                out.append(f"\n### {t}  ({counts.get(t)} rows)")
                if not rows:
                    out.append("_empty_")
                    continue
                out.append("| " + " | ".join(shown) + " |")
                out.append("| " + " | ".join("---" for _ in shown) + " |")
                for r in rows:
                    out.append("| " + " | ".join(cell(v) for v in r) + " |")

            out += ["", "## Related pages", "- [[wih-app]]", "- [[supabase]]", "- [[ghl]]", ""]
            body = mask_text("\n".join(out))
    finally:
        conn.close()

    target = RAW / f"supabase-snapshot-{d}.md"
    RAW.mkdir(parents=True, exist_ok=True)
    target.write_text(body + "\n", encoding="utf-8")
    print(f"supabase connector: wrote raw/{target.name} ({len(tables)} tables).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
