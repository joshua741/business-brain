#!/usr/bin/env python3
"""Notion meetings connector: pull Notion AI meeting notes from the dedicated
"Team Meetings" database into raw/ as masked .md, then mark them ingested.

Stdlib only (urllib). Reads NOTION_API_KEY + NOTION_MEETINGS_DB_ID from a
gitignored .env at the repo root. Idempotent via a page-id manifest plus the
Notion "Ingested" checkbox write-back.
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
ENV_FILE = REPO / ".env"
MANIFEST = Path(__file__).resolve().parent / ".notion-meetings-manifest.json"
NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
def parse_env(path: Path) -> dict:
    """Minimal .env parser: KEY=VALUE lines, ignores blanks/#comments, strips quotes."""
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key:
            out[key] = val
    return out


# --------------------------------------------------------------------------- #
# Block -> Markdown
# --------------------------------------------------------------------------- #
def rich_text_to_str(rich_text) -> str:
    return "".join(rt.get("plain_text", "") for rt in (rich_text or []))


def blocks_to_markdown(blocks, depth: int = 0) -> str:
    """Flatten a list of Notion blocks (with optional pre-fetched 'children') to Markdown.
    Children are expected to already be attached under each block's 'children' key."""
    lines = []
    for b in blocks or []:
        btype = b.get("type", "")
        data = b.get(btype, {}) if isinstance(b.get(btype), dict) else {}
        text = rich_text_to_str(data.get("rich_text"))
        if btype == "heading_1":
            lines.append(f"# {text}")
        elif btype == "heading_2":
            lines.append(f"## {text}")
        elif btype == "heading_3":
            lines.append(f"### {text}")
        elif btype in ("bulleted_list_item", "toggle"):
            lines.append(f"- {text}")
        elif btype == "numbered_list_item":
            lines.append(f"1. {text}")
        elif btype == "to_do":
            box = "x" if data.get("checked") else " "
            lines.append(f"- [{box}] {text}")
        elif btype == "quote":
            lines.append(f"> {text}")
        elif btype == "callout":
            lines.append(f"> {text}")
        elif btype == "code":
            lines.append(f"```\n{text}\n```")
        elif btype == "divider":
            lines.append("---")
        elif text:
            lines.append(text)  # paragraph and anything else with text
        if b.get("children"):
            child_md = blocks_to_markdown(b["children"], depth + 1)
            if child_md:
                lines.append(child_md)
    return "\n\n".join(l for l in lines if l != "")


# --------------------------------------------------------------------------- #
# Filename + manifest
# --------------------------------------------------------------------------- #
def target_name(date_str: str, existing: set) -> str:
    base = f"transcript-{date_str}-team-meeting"
    name = f"{base}.md"
    n = 2
    while name in existing:
        name = f"{base}-{n}.md"
        n += 1
    return name


def needs_ingest(page_id: str, last_edited: str, manifest: dict) -> bool:
    prev = manifest.get(page_id)
    if not prev:
        return True
    return prev.get("last_edited_time") != last_edited


def load_manifest() -> dict:
    if MANIFEST.exists():
        try:
            return json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


# --------------------------------------------------------------------------- #
# Notion API client (with retry/backoff)
# --------------------------------------------------------------------------- #
class TransientAPIError(Exception):
    pass


def with_retries(fn, sleeper=time.sleep, attempts=4, base_delay=2.0):
    """Call fn(); on TransientAPIError retry with exponential backoff. Re-raise after attempts."""
    last = None
    for i in range(attempts):
        try:
            return fn()
        except TransientAPIError as e:
            last = e
            if i < attempts - 1:
                sleeper(base_delay * (2 ** i))
    raise last


def _request(method: str, url: str, token: str, body: dict = None) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Notion-Version", NOTION_VERSION)
    req.add_header("Content-Type", "application/json")

    def do():
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                raise TransientAPIError(f"{e.code} {url}")
            raise RuntimeError(f"Notion API {e.code}: {e.read().decode('utf-8', 'replace')}")
        except urllib.error.URLError as e:
            raise TransientAPIError(f"network: {e}")

    return with_retries(do)


def query_uningested(token: str, db_id: str) -> list:
    """Return pages where the Ingested checkbox is false, paginated."""
    results, cursor = [], None
    while True:
        body = {"filter": {"property": "Ingested", "checkbox": {"equals": False}},
                "page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        page = _request("POST", f"{API}/databases/{db_id}/query", token, body)
        results.extend(page.get("results", []))
        if not page.get("has_more"):
            break
        cursor = page.get("next_cursor")
    return results


def fetch_block_tree(token: str, block_id: str) -> list:
    """Fetch a block's children recursively, attaching nested children under 'children'."""
    blocks, cursor = [], None
    while True:
        url = f"{API}/blocks/{block_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        page = _request("GET", url, token)
        for b in page.get("results", []):
            if b.get("has_children"):
                b["children"] = fetch_block_tree(token, b["id"])
            blocks.append(b)
        if not page.get("has_more"):
            break
        cursor = page.get("next_cursor")
    return blocks


def mark_ingested(token: str, page_id: str) -> None:
    _request("PATCH", f"{API}/pages/{page_id}", token,
             {"properties": {"Ingested": {"checkbox": True}}})


def create_meetings_db(token: str, parent_page_id: str) -> str:
    body = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": "Team Meetings"}}],
        "properties": {
            "Name": {"title": {}},
            "Date": {"date": {}},
            "Attendees": {"multi_select": {}},
            "Ingested": {"checkbox": {}},
        },
    }
    return _request("POST", f"{API}/databases", token, body)["id"]


def page_date(page: dict) -> str:
    """Prefer the Date property; fall back to created_time. Returns YYYY-MM-DD."""
    props = page.get("properties", {})
    d = props.get("Date", {}).get("date")
    if d and d.get("start"):
        return d["start"][:10]
    return page.get("created_time", "")[:10] or datetime.now().strftime("%Y-%m-%d")


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def run(token: str, db_id: str, report_only: bool) -> tuple:
    manifest = load_manifest()
    existing = {p.name for p in RAW.glob("*.md")}
    pulled, skipped, failed = [], [], []
    pages = query_uningested(token, db_id)
    for page in pages:
        pid = page["id"]
        last_edited = page.get("last_edited_time", "")
        if not needs_ingest(pid, last_edited, manifest):
            skipped.append((pid, "unchanged"))
            continue
        try:
            blocks = fetch_block_tree(token, pid)
            md = blocks_to_markdown(blocks)
            if not md.strip():
                failed.append((pid, "empty note"))
                continue
            date_str = page_date(page)
            name = target_name(date_str, existing)
            body = mask_text(md)
            header = (
                f"# Team Meeting {date_str}\n\n"
                f"*(Pulled from Notion 'Team Meetings' database by the notion-meetings "
                f"connector on {datetime.now().strftime('%Y-%m-%d')}.)*\n\n---\n\n"
            )
            if not report_only:
                (RAW / name).write_text(header + body + "\n", encoding="utf-8")
                mark_ingested(token, pid)
                manifest[pid] = {"last_edited_time": last_edited, "target": name}
            existing.add(name)
            pulled.append((pid, name))
        except Exception as e:
            failed.append((pid, str(e)))
    if not report_only:
        MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return pulled, skipped, failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report-only", action="store_true",
                    help="show what would happen without writing or marking ingested")
    ap.add_argument("--create-db", action="store_true",
                    help="create the 'Team Meetings' database under NOTION_PARENT_PAGE_ID and exit")
    args = ap.parse_args()

    cfg = parse_env(ENV_FILE)
    token = cfg.get("NOTION_API_KEY", "").strip()
    if not token:
        print("notion-meetings: NOTION_API_KEY not set in .env -- skipping (no-op).")
        return

    if args.create_db:
        parent = cfg.get("NOTION_PARENT_PAGE_ID", "").strip()
        if not parent:
            print("notion-meetings: NOTION_PARENT_PAGE_ID not set in .env -- cannot create DB.")
            return
        db_id = create_meetings_db(token, parent)
        print("notion-meetings: created 'Team Meetings' DB. Add this to .env:\n"
              f"NOTION_MEETINGS_DB_ID={db_id}")
        return

    db_id = cfg.get("NOTION_MEETINGS_DB_ID", "").strip()
    if not db_id:
        print("notion-meetings: NOTION_MEETINGS_DB_ID not set in .env -- skipping (no-op). "
              "Run with --create-db once NOTION_PARENT_PAGE_ID is set.")
        return

    RAW.mkdir(parents=True, exist_ok=True)
    pulled, skipped, failed = run(token, db_id, args.report_only)
    mode = " (report-only)" if args.report_only else ""
    print(f"notion-meetings{mode}: pulled {len(pulled)}, skipped {len(skipped)}, failed {len(failed)}")
    for pid, name in pulled:
        print(f"  + {pid} -> raw/{name}")
    for pid, why in skipped:
        print(f"  = {pid} ({why})")
    for pid, why in failed:
        print(f"  ! {pid} ({why})")


if __name__ == "__main__":
    main()
