#!/usr/bin/env python3
"""Google Drive 'Business Brain Briefings' connector -> raw/ (masked).

Finds the 'Business Brain Briefings' Drive folder, downloads new/changed files
(Google Docs exported as text; plain text/markdown via media), converts to masked
.md in raw/. Idempotent via a small manifest keyed by file id + modifiedTime.
Self-skips (exit 0) if ADC/scopes or the folder are absent. Read-only.
"""
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
MANIFEST = Path(__file__).resolve().parent / ".gdrive-manifest.json"
FOLDER_NAME = "Business Brain Briefings"
DRIVE = "https://www.googleapis.com/drive/v3"

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _google_auth import get_token


def kebab(stem: str) -> str:
    stem = re.sub(r"\.(md|txt|docx?|pdf)$", "", stem, flags=re.I)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", stem.strip().lower()).strip("-")
    return (s or "briefing")[:80]


def api(url, token, raw=False):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "User-Agent": "BusinessBrain-Connector/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if raw else json.loads(data.decode("utf-8"))


def main() -> int:
    token = get_token()
    if not token:
        print("gdrive connector: ADC not available -- skipping (run gcloud auth application-default login).")
        return 0
    try:
        q = (f"name='{FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' "
             f"and trashed=false")
        res = api(f"{DRIVE}/files?" + urllib.parse.urlencode(
            {"q": q, "fields": "files(id,name)"}), token)
        folders = res.get("files", [])
        if not folders:
            print(f"gdrive connector: folder '{FOLDER_NAME}' not found -- skipping.")
            return 0
        fid = folders[0]["id"]
        res = api(f"{DRIVE}/files?" + urllib.parse.urlencode({
            "q": f"'{fid}' in parents and trashed=false",
            "fields": "files(id,name,mimeType,modifiedTime)",
            "orderBy": "modifiedTime desc",
            "pageSize": 100,
        }), token)
        files = res.get("files", [])
    except Exception as e:
        print(f"gdrive connector: list error ({type(e).__name__}: {e}); skipping.")
        return 0

    manifest = {}
    if MANIFEST.exists():
        try:
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}
    existing = {kebab(p.stem) for p in RAW.glob("*.md")}

    ingested = 0
    for f in files:
        fid_, name, mime, mtime = f["id"], f["name"], f.get("mimeType", ""), f.get("modifiedTime", "")
        if manifest.get(fid_, {}).get("modifiedTime") == mtime:
            continue  # unchanged since last pull
        try:
            if mime == "application/vnd.google-apps.document":
                text = api(f"{DRIVE}/files/{fid_}/export?" + urllib.parse.urlencode(
                    {"mimeType": "text/plain"}), token, raw=True).decode("utf-8", "replace")
            elif mime in ("text/plain", "text/markdown") or name.lower().endswith((".md", ".txt")):
                text = api(f"{DRIVE}/files/{fid_}?alt=media", token, raw=True).decode("utf-8", "replace")
            else:
                # binaries (pdf/sheets/etc.) handled by other connectors; skip here
                manifest[fid_] = {"modifiedTime": mtime, "status": "skipped-binary"}
                continue
        except Exception as e:
            manifest[fid_] = {"modifiedTime": mtime, "status": f"error:{type(e).__name__}"}
            continue
        if not text.strip():
            manifest[fid_] = {"modifiedTime": mtime, "status": "empty"}
            continue
        stem = kebab(name)
        if stem in existing and manifest.get(fid_, {}).get("target") != f"{stem}.md":
            manifest[fid_] = {"modifiedTime": mtime, "status": "dedup-skip"}
            continue
        header = (f"# {name}\n\n*(From Google Drive 'Business Brain Briefings' on "
                  f"{datetime.now().strftime('%Y-%m-%d')}.)*\n\n---\n\n")
        (RAW / f"{stem}.md").write_text(mask_text(header + text) + "\n", encoding="utf-8")
        manifest[fid_] = {"modifiedTime": mtime, "status": "ingested", "target": f"{stem}.md"}
        ingested += 1

    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"gdrive connector: {ingested} briefing file(s) ingested from '{FOLDER_NAME}'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
