#!/usr/bin/env python3
"""Google Sheets connector -> masked daily snapshot of KPI/finance dashboards.

Discovers spreadsheets via Drive (KPI/finance keywords, else most-recent), reads a
capped slice of each sheet's values, and writes raw/google-sheets-snapshot-DATE.md
(masked). Self-skips (exit 0) if ADC/scopes are absent. Read-only.
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
DRIVE = "https://www.googleapis.com/drive/v3"
SHEETS = "https://sheets.googleapis.com/v4/spreadsheets"
MAX_SHEETS_FILES = 15
MAX_ROWS = 50
MAX_COLS = 12
CELL_CHARS = 40
KEYWORDS = ("kpi", "finance", "tracker", "dashboard", "bid", "quote", "goal",
            "ad spend", "team", "calculator", "profit", "p&l", "budget")

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _google_auth import get_token


def api(url, token):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "BusinessBrain-Connector/1.0",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def cell(v):
    return str(v).replace("|", "\\|").replace("\n", " ")[:CELL_CHARS]


def discover(token):
    res = api(f"{DRIVE}/files?" + urllib.parse.urlencode({
        "q": "mimeType='application/vnd.google-apps.spreadsheet' and trashed=false",
        "fields": "files(id,name,modifiedTime)",
        "orderBy": "modifiedTime desc",
        "pageSize": 100,
    }), token)
    files = res.get("files", [])
    keyed = [f for f in files if any(k in f["name"].lower() for k in KEYWORDS)]
    chosen = keyed or files
    return chosen[:MAX_SHEETS_FILES]


def main() -> int:
    token = get_token()
    if not token:
        print("sheets connector: ADC not available -- skipping (run gcloud auth application-default login).")
        return 0
    try:
        files = discover(token)
    except Exception as e:
        print(f"sheets connector: discovery error ({type(e).__name__}: {e}); skipping.")
        return 0
    if not files:
        print("sheets connector: no spreadsheets found -- skipping.")
        return 0

    d = datetime.now().strftime("%Y-%m-%d")
    out = [
        "---",
        f"name: source-google-sheets-snapshot-{d}",
        "type: source",
        "tags: [google-sheets, kpi, finance, snapshot]",
        f"sources: [google-sheets-snapshot-{d}.md]",
        f"updated: {d}",
        "---",
        f"# Google Sheets Snapshot -- {d}",
        "",
        f"**Summary**: Read-only snapshot of {len(files)} KPI/finance spreadsheet(s).",
        "",
        f"**Sources**: google-sheets-snapshot-{d}.md (Google Sheets API, read-only)",
        "",
        f"**Last updated**: {d}",
        "",
        "---",
    ]
    for f in files:
        sid, name = f["id"], f["name"]
        out.append(f"\n## {name}")
        try:
            meta = api(f"{SHEETS}/{sid}?" + urllib.parse.urlencode(
                {"fields": "sheets.properties(title)"}), token)
            titles = [s["properties"]["title"] for s in meta.get("sheets", [])]
        except Exception as e:
            out.append(f"_(could not open: {type(e).__name__})_")
            continue
        for title in titles[:8]:
            rng = f"'{title}'!A1:{chr(64 + MAX_COLS)}{MAX_ROWS}"
            try:
                vals = api(f"{SHEETS}/{sid}/values/" + urllib.parse.quote(rng), token).get("values", [])
            except Exception:
                continue
            if not vals:
                continue
            out.append(f"\n### {title}")
            width = min(MAX_COLS, max(len(r) for r in vals))
            header = vals[0] + [""] * (width - len(vals[0]))
            out.append("| " + " | ".join(cell(c) for c in header[:width]) + " |")
            out.append("| " + " | ".join("---" for _ in range(width)) + " |")
            for row in vals[1:MAX_ROWS]:
                row = list(row) + [""] * (width - len(row))
                out.append("| " + " | ".join(cell(c) for c in row[:width]) + " |")

    out += ["", "## Related pages", "- [[google-sheets]]", "- [[kpi-tracking]]", "- [[wih-app]]", ""]
    target = RAW / f"google-sheets-snapshot-{d}.md"
    RAW.mkdir(parents=True, exist_ok=True)
    target.write_text(mask_text("\n".join(out)) + "\n", encoding="utf-8")
    print(f"sheets connector: wrote raw/{target.name} ({len(files)} spreadsheets).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
