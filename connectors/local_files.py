#!/usr/bin/env python3
"""Local-files connector: pull business documents from local folders into raw/ as masked .md.

Default channel is the intentional drop folder (Documents\\Business_Brain\\drop).
Pass --include-downloads to also sweep the Downloads backlog (deduped + junk-filtered).

Converts: .pdf (pdftotext), .csv (table), .xlsx (openpyxl), .md/.txt (copy). Masks every
output via lib/mask_sensitive. Idempotent via a manifest; never deletes the originals.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
DROP = REPO / "drop"
DOWNLOADS = Path(r"C:\Users\joshu\Downloads")
MANIFEST = Path(__file__).resolve().parent / ".local-ingest-manifest.json"
PDFTOTEXT = r"C:\Program Files\Git\mingw64\bin\pdftotext.exe"

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text

ALLOWED = {".pdf", ".csv", ".xlsx", ".md", ".txt"}
MAX_CSV_ROWS = 300
# junk/non-business names to skip (case-insensitive substring match)
DENY = ["loading google docs", "untitled", "screenshot", "image", "~$"]
# exact lowercased stems that are dev/config artifacts, never business sources
DENY_STEMS = {"claude", "skill", "reference", "test", "readme", "carousel-skill"}


def kebab(stem: str) -> str:
    stem = re.sub(r"\.md$", "", stem, flags=re.I)  # handle "X.md.pdf" -> "X"
    s = re.sub(r"[^a-zA-Z0-9]+", "-", stem.strip().lower()).strip("-")
    return (s or "file")[:80]


def load_manifest() -> dict:
    if MANIFEST.exists():
        try:
            return json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def pdf_to_text(path: Path) -> str:
    exe = PDFTOTEXT if os.path.exists(PDFTOTEXT) else "pdftotext"
    proc = subprocess.run([exe, "-q", "-enc", "UTF-8", str(path), "-"],
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=120)
    return proc.stdout or ""


def csv_to_md(path: Path) -> str:
    out, truncated = [], False
    with open(path, "r", encoding="utf-8-sig", errors="ignore", newline="") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return ""
    header = rows[0]
    out.append("| " + " | ".join(c.strip() for c in header) + " |")
    out.append("| " + " | ".join("---" for _ in header) + " |")
    for r in rows[1:MAX_CSV_ROWS + 1]:
        out.append("| " + " | ".join(c.strip().replace("|", "\\|") for c in r) + " |")
    if len(rows) - 1 > MAX_CSV_ROWS:
        truncated = True
        out.append(f"\n*(... {len(rows) - 1 - MAX_CSV_ROWS} more rows truncated)*")
    return "\n".join(out)


def xlsx_to_md(path: Path) -> str:
    try:
        import openpyxl
    except Exception:
        return ""  # signal unsupported
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    parts = []
    for ws in wb.worksheets:
        parts.append(f"## Sheet: {ws.title}")
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        header = [str(c) if c is not None else "" for c in rows[0]]
        parts.append("| " + " | ".join(header) + " |")
        parts.append("| " + " | ".join("---" for _ in header) + " |")
        for r in rows[1:MAX_CSV_ROWS + 1]:
            cells = [("" if c is None else str(c)).replace("|", "\\|") for c in r]
            parts.append("| " + " | ".join(cells) + " |")
    return "\n".join(parts)


def extract(path: Path):
    """Return (text, ok). ok=False means unsupported/empty."""
    ext = path.suffix.lower()
    try:
        if ext == ".pdf":
            t = pdf_to_text(path)
        elif ext == ".csv":
            t = csv_to_md(path)
        elif ext == ".xlsx":
            t = xlsx_to_md(path)
        elif ext in (".md", ".txt"):
            t = path.read_text(encoding="utf-8-sig", errors="ignore")
        else:
            return "", False
    except Exception as e:
        return f"(extraction error: {e})", False
    return t, bool(t.strip())


def process(folders, manifest, write_files=True):
    ingested, skipped, failed = [], [], []
    # normalized stems of everything already in raw/ — catches case/format dupes
    existing = {kebab(p.stem) for p in RAW.glob("*.md")}
    for folder in folders:
        if not folder.exists():
            continue
        for f in sorted(folder.iterdir()):
            if not f.is_file():
                continue
            ext = f.suffix.lower()
            name_l = f.name.lower()
            stem_kebab = kebab(f.stem)
            key = str(f.resolve())
            if ext not in ALLOWED or any(d in name_l for d in DENY) or f.stat().st_size == 0:
                continue
            if f.stem.lower() in DENY_STEMS or stem_kebab.endswith("-skill"):
                continue  # dev/config artifact, not a business source
            st = f.stat()
            sig = {"size": st.st_size, "mtime": int(st.st_mtime)}
            prev = manifest.get(key)
            if prev and prev.get("size") == sig["size"] and prev.get("mtime") == sig["mtime"]:
                continue  # already processed, unchanged
            target = RAW / f"{stem_kebab}.md"
            if stem_kebab in existing and not (prev and prev.get("target") == target.name):
                # a raw page already covers this (case/format-insensitive) -> dedup skip
                manifest[key] = {**sig, "target": target.name, "status": "dedup-skip"}
                skipped.append((f.name, "already in raw as " + target.name + ".md"))
                continue
            text, ok = extract(f)
            if not ok:
                failed.append((f.name, "unsupported/empty"))
                manifest[key] = {**sig, "status": "failed"}
                continue
            body = mask_text(text)
            header = (
                f"# {f.stem}\n\n"
                f"*(Converted from local file `{f.name}` by the local-files connector on "
                f"{datetime.now().strftime('%Y-%m-%d')}.)*\n\n---\n\n"
            )
            if write_files:
                target.write_text(header + body + "\n", encoding="utf-8")
                manifest[key] = {**sig, "target": target.name, "status": "ingested"}
            ingested.append((f.name, target.name))
    return ingested, skipped, failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-downloads", action="store_true",
                    help="also sweep the Downloads backlog (deduped + junk-filtered)")
    ap.add_argument("--report-only", action="store_true",
                    help="show what would happen without writing")
    args = ap.parse_args()

    folders = [DROP]
    if args.include_downloads:
        folders.append(DOWNLOADS)
    DROP.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    if args.report_only:
        # dry run: don't persist manifest or write files
        snapshot = json.loads(json.dumps(manifest))
        ingested, skipped, failed = process(folders, snapshot, write_files=False)
    else:
        ingested, skipped, failed = process(folders, manifest, write_files=True)
        MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"local-files connector: ingested {len(ingested)}, skipped {len(skipped)}, failed {len(failed)}")
    for n, t in ingested:
        print(f"  + {n} -> raw/{t}")
    for n, why in skipped:
        print(f"  = {n} ({why})")
    for n, why in failed:
        print(f"  ! {n} ({why})")


if __name__ == "__main__":
    main()
