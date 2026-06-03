#!/usr/bin/env python3
"""Notion meetings connector: discover Notion AI meeting/call notes via the
search API and pull them into raw/ as masked .md.

Read-only against Notion (never mutates pages). Stdlib only (urllib). Reads
NOTION_API_KEY from a gitignored .env at the repo root. A page counts as a
meeting transcript when its title starts with an ISO datetime or contains a
meeting keyword (see is_meeting_title). Idempotent via a page-id manifest
keyed on last_edited_time, so edited notes re-ingest and unchanged ones skip.
"""
import argparse
import json
import re
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
# Meeting detection + filename + manifest
# --------------------------------------------------------------------------- #
# A page is a meeting transcript if its title starts with an ISO datetime
# (Notion AI recordings named only by timestamp) or contains a meeting keyword.
ISO_TITLE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:")
DATE_IN_TITLE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
ISO_STAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}T[\d:.+\-]+")
MEETING_KEYWORDS = ("meeting", "call", "role play", "standup", "stand-up",
                    "1:1", "interview", "sync", "huddle")
# Container/non-transcript pages to never treat as a meeting note, by exact title.
EXCLUDE_TITLES = {"meeting transcripts"}


def page_title(page: dict) -> str:
    for v in page.get("properties", {}).values():
        if v.get("type") == "title":
            return "".join(x.get("plain_text", "") for x in v.get("title", []))
    return ""


def is_meeting_title(title: str) -> bool:
    t = (title or "").strip()
    if not t or t.lower() in EXCLUDE_TITLES:
        return False
    if ISO_TITLE_RE.match(t):
        return True
    return any(k in t.lower() for k in MEETING_KEYWORDS)


def slug_from_title(title: str) -> str:
    t = ISO_STAMP_RE.sub("", title or "")          # drop embedded timestamp
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t.strip().lower()).strip("-")
    return (t or "meeting")[:60]


def target_name(date_str: str, slug: str, existing: set) -> str:
    base = f"transcript-{date_str}-{slug}"
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


def find_meeting_pages(token: str) -> list:
    """Search every page shared with the integration, return only meeting/call
    transcript pages (by title heuristic). Paginated."""
    results, cursor = [], None
    while True:
        body = {"filter": {"value": "page", "property": "object"}, "page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        page = _request("POST", f"{API}/search", token, body)
        for o in page.get("results", []):
            if o.get("object") == "page" and is_meeting_title(page_title(o)):
                results.append(o)
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


def page_date(page: dict) -> str:
    """Prefer a date embedded in the title, then a Date property, then created_time."""
    m = DATE_IN_TITLE_RE.search(page_title(page))
    if m:
        return m.group(1)
    d = page.get("properties", {}).get("Date", {}).get("date")
    if d and d.get("start"):
        return d["start"][:10]
    return page.get("created_time", "")[:10] or datetime.now().strftime("%Y-%m-%d")


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def run(token: str, report_only: bool) -> tuple:
    manifest = load_manifest()
    existing = {p.name for p in RAW.glob("*.md")}
    pulled, skipped, failed = [], [], []
    pages = find_meeting_pages(token)
    for page in pages:
        pid = page["id"]
        last_edited = page.get("last_edited_time", "")
        if not needs_ingest(pid, last_edited, manifest):
            skipped.append((page_title(page), "unchanged"))
            continue
        try:
            blocks = fetch_block_tree(token, pid)
            md = blocks_to_markdown(blocks)
            if not md.strip():
                failed.append((page_title(page), "empty note"))
                continue
            title = page_title(page)
            date_str = page_date(page)
            name = target_name(date_str, slug_from_title(title), existing)
            body = mask_text(md)
            header = (
                f"# {title or 'Meeting ' + date_str}\n\n"
                f"*(Pulled from Notion by the notion-meetings connector on "
                f"{datetime.now().strftime('%Y-%m-%d')}.)*\n\n---\n\n"
            )
            if not report_only:
                (RAW / name).write_text(header + body + "\n", encoding="utf-8")
                manifest[pid] = {"last_edited_time": last_edited, "target": name}
            existing.add(name)
            pulled.append((title, name))
        except Exception as e:
            failed.append((page_title(page), str(e)))
    if not report_only:
        MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return pulled, skipped, failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report-only", action="store_true",
                    help="show what would be pulled without writing files")
    args = ap.parse_args()

    cfg = parse_env(ENV_FILE)
    token = cfg.get("NOTION_API_KEY", "").strip()
    if not token:
        print("notion-meetings: NOTION_API_KEY not set in .env -- skipping (no-op).")
        return

    RAW.mkdir(parents=True, exist_ok=True)
    pulled, skipped, failed = run(token, args.report_only)
    mode = " (report-only)" if args.report_only else ""
    print(f"notion-meetings{mode}: pulled {len(pulled)}, skipped {len(skipped)}, failed {len(failed)}")
    for title, name in pulled:
        print(f"  + raw/{name}   <- {title}")
    for title, why in skipped:
        print(f"  = {title} ({why})")
    for title, why in failed:
        print(f"  ! {title} ({why})")


if __name__ == "__main__":
    main()
