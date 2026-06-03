# Notion Meeting-Notes Ingest — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Auto-pull Notion AI meeting notes from Joshua's morning team meetings into `raw/` and ingest them into `wiki/` once daily at 4 PM, with zero manual steps after one-time token setup.

**Architecture:** A new Python connector (`notion_meetings.py`) queries a dedicated "Team Meetings" Notion database via the REST API, flattens each new note's blocks to masked Markdown in `raw/`, and checks the note off in Notion. A new PowerShell script (`notion-meetings-pull.ps1`) chains pull → wiki ingest (reusing the existing daily agent) → privacy gate → git push, fired by a 4 PM Windows scheduled task. Mirrors the existing `local_files.py` + `daily-wiki-maintenance.ps1` patterns.

**Tech Stack:** Python 3.12 (stdlib `urllib` only — no new deps), Notion API v2022-06-28, PowerShell 5.1 (ASCII-only), Windows Task Scheduler, existing `lib/mask_sensitive.py` + `lib/audit_secrets.py`.

---

## Prerequisite Gate (Joshua — one time, before Task 5 live steps)

Claude cannot log into Notion. Before the connector can run for real, Joshua must:

1. Create an internal integration at `notion.so/my-integrations` → copy the **Internal Integration Secret**.
2. Open the Notion page that should *contain* the new database → `•••` → **Connections** → add the integration.
3. Provide Claude the **token** and the **parent page URL** (the 32-char id is in the URL).

Tasks 1–4 (pure code + tests) need none of this and can be built immediately. Task 5's *live* steps and Tasks 6–9 validation need it.

## File Structure

- Create: `connectors/notion_meetings.py` — the connector (env load, API client, block flattener, filename/manifest, `main()`).
- Create: `tests/test_notion_meetings.py` — unit tests for the pure functions.
- Create: `notion-meetings-pull.ps1` — the 4 PM orchestration script.
- Create: `setup-notion-task.bat` — registers/refreshes the scheduled task.
- Modify: `connectors/connectors.json` — flip `notion` entry to active.
- Modify: `.gitignore` — ignore the new manifest.

---

### Task 1: `.env` loader + connector skeleton

**Files:**
- Create: `connectors/notion_meetings.py`
- Test: `tests/test_notion_meetings.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_notion_meetings.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "connectors"))
import notion_meetings as nm


def test_parse_env_reads_keys_and_ignores_comments(tmp_path):
    env = tmp_path / ".env"
    env.write_text(
        "# a comment\n"
        "NOTION_API_KEY=ntn_abc123\n"
        "\n"
        'NOTION_MEETINGS_DB_ID="db-id-456"\n'
        "EXPORT_NOTE=export ignored=here\n",
        encoding="utf-8",
    )
    cfg = nm.parse_env(env)
    assert cfg["NOTION_API_KEY"] == "ntn_abc123"
    assert cfg["NOTION_MEETINGS_DB_ID"] == "db-id-456"  # surrounding quotes stripped


def test_parse_env_missing_file_returns_empty(tmp_path):
    assert nm.parse_env(tmp_path / "nope.env") == {}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: FAIL — `ModuleNotFoundError` / `AttributeError: module 'notion_meetings' has no attribute 'parse_env'`

- [ ] **Step 3: Write minimal implementation**

```python
#!/usr/bin/env python3
"""Notion meetings connector: pull Notion AI meeting notes from the dedicated
"Team Meetings" database into raw/ as masked .md, then mark them ingested.

Stdlib only (urllib). Reads NOTION_API_KEY + NOTION_MEETINGS_DB_ID from a
gitignored .env at the repo root. Idempotent via a page-id manifest.
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add connectors/notion_meetings.py tests/test_notion_meetings.py
git commit -m "feat(notion): connector skeleton + .env parser with tests"
```

---

### Task 2: Block → Markdown flattener

**Files:**
- Modify: `connectors/notion_meetings.py`
- Test: `tests/test_notion_meetings.py`

- [ ] **Step 1: Write the failing test**

```python
def test_rich_text_joins_plain_text():
    rt = [{"plain_text": "Hello "}, {"plain_text": "world"}]
    assert nm.rich_text_to_str(rt) == "Hello world"


def test_blocks_to_markdown_covers_common_types():
    blocks = [
        {"type": "heading_1", "heading_1": {"rich_text": [{"plain_text": "Summary"}]}},
        {"type": "paragraph", "paragraph": {"rich_text": [{"plain_text": "We met."}]}},
        {"type": "bulleted_list_item",
         "bulleted_list_item": {"rich_text": [{"plain_text": "point a"}]}},
        {"type": "to_do",
         "to_do": {"rich_text": [{"plain_text": "ship it"}], "checked": True}},
        {"type": "divider", "divider": {}},
    ]
    md = nm.blocks_to_markdown(blocks)
    assert "# Summary" in md
    assert "We met." in md
    assert "- point a" in md
    assert "- [x] ship it" in md
    assert "---" in md


def test_blocks_to_markdown_recurses_into_children():
    blocks = [{
        "type": "toggle",
        "toggle": {"rich_text": [{"plain_text": "Transcript"}]},
        "children": [
            {"type": "paragraph",
             "paragraph": {"rich_text": [{"plain_text": "Mostafa: hi"}]}},
        ],
    }]
    md = nm.blocks_to_markdown(blocks)
    assert "Transcript" in md
    assert "Mostafa: hi" in md
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: FAIL — `AttributeError: ... has no attribute 'rich_text_to_str'`

- [ ] **Step 3: Write minimal implementation**

Append to `connectors/notion_meetings.py`:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: PASS (5 passed)

- [ ] **Step 5: Commit**

```bash
git add connectors/notion_meetings.py tests/test_notion_meetings.py
git commit -m "feat(notion): block-to-markdown flattener with tests"
```

---

### Task 3: Filename builder + manifest dedup

**Files:**
- Modify: `connectors/notion_meetings.py`
- Test: `tests/test_notion_meetings.py`

- [ ] **Step 1: Write the failing test**

```python
def test_target_name_basic():
    assert nm.target_name("2026-06-03", set()) == "transcript-2026-06-03-team-meeting.md"


def test_target_name_disambiguates_on_collision():
    existing = {"transcript-2026-06-03-team-meeting.md"}
    assert nm.target_name("2026-06-03", existing) == "transcript-2026-06-03-team-meeting-2.md"


def test_needs_ingest_new_and_edited():
    manifest = {"page1": {"last_edited_time": "2026-06-03T10:00:00.000Z"}}
    # unchanged -> skip
    assert nm.needs_ingest("page1", "2026-06-03T10:00:00.000Z", manifest) is False
    # edited -> re-ingest
    assert nm.needs_ingest("page1", "2026-06-03T11:00:00.000Z", manifest) is True
    # brand new -> ingest
    assert nm.needs_ingest("page2", "2026-06-03T09:00:00.000Z", manifest) is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: FAIL — `AttributeError: ... has no attribute 'target_name'`

- [ ] **Step 3: Write minimal implementation**

Append to `connectors/notion_meetings.py`:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: PASS (8 passed)

- [ ] **Step 5: Commit**

```bash
git add connectors/notion_meetings.py tests/test_notion_meetings.py
git commit -m "feat(notion): filename + manifest dedup helpers with tests"
```

---

### Task 4: Notion API client with retry/backoff

**Files:**
- Modify: `connectors/notion_meetings.py`
- Test: `tests/test_notion_meetings.py`

The HTTP calls are thin wrappers around one `_request` function. The unit-testable piece is the retry loop, which takes an injected caller and sleeper so no real network/sleep is needed.

- [ ] **Step 1: Write the failing test**

```python
def test_with_retries_succeeds_after_transient_errors():
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise nm.TransientAPIError("429")
        return "ok"

    slept = []
    result = nm.with_retries(flaky, sleeper=slept.append, attempts=5)
    assert result == "ok"
    assert calls["n"] == 3
    assert len(slept) == 2  # slept before each of the 2 retries


def test_with_retries_gives_up_and_raises():
    def always_fail():
        raise nm.TransientAPIError("500")

    slept = []
    try:
        nm.with_retries(always_fail, sleeper=slept.append, attempts=3)
        assert False, "should have raised"
    except nm.TransientAPIError:
        pass
    assert len(slept) == 2  # 3 attempts -> slept between, not after the last
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: FAIL — `AttributeError: ... has no attribute 'with_retries'`

- [ ] **Step 3: Write minimal implementation**

Append to `connectors/notion_meetings.py`:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: PASS (10 passed)

- [ ] **Step 5: Commit**

```bash
git add connectors/notion_meetings.py tests/test_notion_meetings.py
git commit -m "feat(notion): API client (query/blocks/patch/create) + retry with tests"
```

---

### Task 5: Wire `main()` — bootstrap, pull, mask, write, mark

**Files:**
- Modify: `connectors/notion_meetings.py`
- Modify: `.gitignore`

- [ ] **Step 1: Add the manifest to `.gitignore`**

Add this line under the existing `connectors/.local-ingest-manifest.json` line:

```
connectors/.notion-meetings-manifest.json
```

- [ ] **Step 2: Append `main()` to `connectors/notion_meetings.py`**

```python
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
        print(f"notion-meetings: created 'Team Meetings' DB. Add this to .env:\n"
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
```

- [ ] **Step 3: Verify the full unit suite still passes**

Run: `python -m pytest tests/test_notion_meetings.py -q`
Expected: PASS (10 passed) — `main()`/`run()` are network paths, covered by live validation in Task 9.

- [ ] **Step 4: Verify the no-credential path is a clean no-op**

Run (with no `.env` present or token blank): `python connectors/notion_meetings.py --report-only`
Expected: prints `notion-meetings: NOTION_API_KEY not set in .env -- skipping (no-op).` and exits 0.

- [ ] **Step 5: Commit**

```bash
git add connectors/notion_meetings.py .gitignore
git commit -m "feat(notion): wire main() bootstrap/pull/mask/write + ignore manifest"
```

---

### Task 6: Orchestration script `notion-meetings-pull.ps1`

**Files:**
- Create: `notion-meetings-pull.ps1`

ASCII-only (per the `windows-powershell-encoding` lesson — no em-dashes, smart quotes, or non-ASCII). Reuses the exact ingest-agent prompt and privacy gate from `daily-wiki-maintenance.ps1`.

- [ ] **Step 1: Create the file**

```powershell
# Business Brain -- Notion Meeting Notes Pull + Ingest
# Runs at 4:00 PM via Windows Task Scheduler
# Sequence: git pull > pull Notion meeting notes > ingest > privacy gate > commit > push

$repoPath = "C:\Users\joshu\Documents\Business_Brain"
$logFile  = "$repoPath\daily-maintenance.log"
$claude   = "C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
$git      = "C:\Program Files\Git\cmd\git.exe"
$gh       = "C:\Program Files\GitHub CLI\gh.exe"
$date     = Get-Date -Format "yyyy-MM-dd"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$ts] $msg" | Out-File -Append -Encoding utf8 $logFile
}

Set-Location $repoPath
$env:BB_CAPTURE_RUNNING = "1"
Log "=== Notion meeting pull started ==="

Log "git pull"
& $git pull origin master 2>&1 | ForEach-Object { Log $_ }

Log "Notion meetings connector"
& python "$repoPath\connectors\notion_meetings.py" 2>&1 | ForEach-Object { Log $_ }

Log "Running wiki ingest agent"
$maintPrompt = @"
You are the daily maintenance agent for Joshua Webber's Business Brain wiki stored in the current directory ($repoPath).

CRITICAL: You are running fully autonomous with NO human present. Nobody can answer questions or approve anything. Do NOT ask questions. Do NOT produce a report and wait for approval. Directly CREATE and EDIT the files yourself with your file tools. Make your best judgment on any uncertainty and proceed. Your ONLY chat output should be a one-line summary at the very end.

Skip any source file that is empty (0 bytes) or contains no meaningful content -- do not create a page for it.

Do the following in order:

1. Read wiki/.last-ingest for reference only (do NOT use it as a filter).
2. INGEST BY RECONCILIATION (not by date). For every file in raw/ (recursively, *.md), determine whether a wiki/source-*.md page already lists that exact filename in its sources: frontmatter. For each raw file with NO such source page, ingest it now:
   - Create a source page in wiki/ named source-[kebab-title].md (frontmatter: name, type: source, tags, sources: [<exact raw filename>], updated: $date) with a detailed summary including specific figures, dates, parties, (source: <filename>) citations, and [[wikilinks]]
   - Create or update entity, project, concept, and person pages it touches
   - Add wikilinks throughout
   - Add the source to wiki/index.md under Sources
   - APP ROUTING: if the source is relevant to the wih-app CRM (CRM features, AI agents, dashboards, automations, or any of the three verticals: wholesale/creative finance, property management, capital raising), also append a one-line idea with a [[wikilink]] to the "Feature context to fold in" section of wiki/wih-app.md.
3. Run wiki lint:
   - Orphan pages: find pages with no inbound wikilinks, add a link from the most relevant page
   - Missing pages: find [[wikilinks]] with no corresponding file, create stub pages with correct frontmatter
   - Contradictions: flag in wiki/log.md, do not auto-resolve
   - Stale status: update status fields where evidence supports it
4. Append to wiki/log.md: ## [$date] notion-pull | [one-line summary of what was ingested]
5. Write $date to wiki/.last-ingest

Do not run any git commands. Exit when done.
"@
& $claude --print $maintPrompt --dangerously-skip-permissions 2>&1 | ForEach-Object { Log $_ }

Log "Secret audit (non-fatal warning)"
& python "$repoPath\lib\audit_secrets.py" 2>&1 | ForEach-Object { Log $_ }

Log "Repo visibility check"
$isPrivate = (& $gh repo view joshua741/business-brain --json isPrivate -q .isPrivate 2>&1 | Out-String).Trim()
Log "isPrivate=$isPrivate"
if ($isPrivate -ne 'true') {
    Log "ABORT: repo is NOT private -- refusing to commit/push sensitive data."
    Log "=== Notion meeting pull halted on privacy gate ==="
    exit 1
}

$changes = & $git status --porcelain 2>&1
if ($changes) {
    Log "Changes detected -- committing"
    & $git add -A 2>&1 | ForEach-Object { Log $_ }
    & $git commit -m "chore: notion meeting pull $date" 2>&1 | ForEach-Object { Log $_ }
    & $git push origin master 2>&1 | ForEach-Object { Log $_ }
    Log "Pushed to GitHub"
} else {
    Log "No changes -- nothing to commit"
}

Log "=== Notion meeting pull complete ==="
```

- [ ] **Step 2: Lint for non-ASCII (must output nothing)**

Run: `powershell -Command "Select-String -Path notion-meetings-pull.ps1 -Pattern '[^\x00-\x7F]'"`
Expected: no output (no non-ASCII characters).

- [ ] **Step 3: Syntax-check the script parses**

Run: `powershell -NoProfile -Command "$null = [System.Management.Automation.PSParser]::Tokenize((Get-Content -Raw notion-meetings-pull.ps1), [ref]$null); 'OK'"`
Expected: prints `OK`

- [ ] **Step 4: Commit**

```bash
git add notion-meetings-pull.ps1
git commit -m "feat(notion): 4 PM pull+ingest orchestration script"
```

---

### Task 7: Scheduled task registration

**Files:**
- Create: `setup-notion-task.bat`

- [ ] **Step 1: Create the file** (mirrors `setup-task.bat`, trigger at 16:00)

```bat
@echo off
:: Remove old task if it exists
powershell.exe -ExecutionPolicy Bypass -Command "Unregister-ScheduledTask -TaskName 'Business Brain Notion Meeting Pull' -Confirm:$false -ErrorAction SilentlyContinue"

:: Create new task -- daily at 4:00 PM
powershell.exe -ExecutionPolicy Bypass -Command "$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -ExecutionPolicy Bypass -File \"C:\Users\joshu\Documents\Business_Brain\notion-meetings-pull.ps1\"'; $trigger = New-ScheduledTaskTrigger -Daily -At '16:00'; $settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1) -RunOnlyIfNetworkAvailable; $principal = New-ScheduledTaskPrincipal -UserId 'joshu' -LogonType Interactive -RunLevel Highest; Register-ScheduledTask -TaskName 'Business Brain Notion Meeting Pull' -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force"
echo Done. Notion meeting pull task registered for 4:00 PM daily.
```

- [ ] **Step 2: Register the task**

Run: `cmd /c setup-notion-task.bat`
Expected: prints `Done. Notion meeting pull task registered for 4:00 PM daily.`

- [ ] **Step 3: Confirm it exists**

Run: `schtasks /query /tn "Business Brain Notion Meeting Pull" /fo LIST`
Expected: lists the task with `Schedule: Daily` at `4:00:00 PM`.

- [ ] **Step 4: Commit**

```bash
git add setup-notion-task.bat
git commit -m "feat(notion): scheduled task registration (4 PM daily)"
```

---

### Task 8: Connector registry update

**Files:**
- Modify: `connectors/connectors.json`

- [ ] **Step 1: Update the `notion` entry**

Replace the existing `notion` object's fields with:

```json
    {
      "name": "notion",
      "type": "api",
      "status": "active",
      "source": "Notion: Team Meetings database (AI meeting notes)",
      "extractor": "connectors/notion_meetings.py",
      "cadence": "daily-4pm",
      "credential_needed": "NOTION_API_KEY + NOTION_MEETINGS_DB_ID in .env",
      "notes": "Pulls morning team meeting notes -> raw/ -> wiki via notion-meetings-pull.ps1. Master-prompt sync still TODO under a separate path."
    },
```

- [ ] **Step 2: Validate JSON parses**

Run: `python -c "import json; json.load(open('connectors/connectors.json')); print('OK')"`
Expected: prints `OK`

- [ ] **Step 3: Refresh STATUS.md**

Run: `python connectors/discover_gaps.py`
Expected: regenerates `connectors/STATUS.md`; `notion` row reflects ACTIVE (or shows the .env creds detected).

- [ ] **Step 4: Commit**

```bash
git add connectors/connectors.json connectors/STATUS.md
git commit -m "chore(notion): mark connector active in registry"
```

---

### Task 9: Live end-to-end validation (requires Joshua's token — Prerequisite Gate)

No code. Run once Joshua supplies the token + parent page id.

- [ ] **Step 1: Create `.env` with credentials**

Create `C:\Users\joshu\Documents\Business_Brain\.env` (gitignored) containing:

```
NOTION_API_KEY=<token from Joshua>
NOTION_PARENT_PAGE_ID=<32-char id from the shared page URL>
NOTION_MEETINGS_DB_ID=
```

- [ ] **Step 2: Create the Team Meetings database**

Run: `python connectors/notion_meetings.py --create-db`
Expected: prints `NOTION_MEETINGS_DB_ID=<new-id>`. Paste that id into `.env`.

- [ ] **Step 3: Dry-run the connector**

Add one real or sample meeting note as a row in the new DB (leave `Ingested` unchecked), then run:
`python connectors/notion_meetings.py --report-only`
Expected: `pulled 1, skipped 0, failed 0` with the target filename — and NO file written, NO checkbox flipped.

- [ ] **Step 4: Real connector run**

Run: `python connectors/notion_meetings.py`
Expected: `raw/transcript-YYYY-MM-DD-team-meeting.md` exists, is masked, and the Notion row's `Ingested` box is now checked. Re-running prints `skipped 1 (unchanged)`.

- [ ] **Step 5: Full pipeline dry run**

Run: `powershell -ExecutionPolicy Bypass -File notion-meetings-pull.ps1`
Then check `daily-maintenance.log` for the `=== Notion meeting pull complete ===` banner, confirm a `wiki/source-*.md` page was created for the note, and confirm the privacy gate logged `isPrivate=true` before the commit/push.

- [ ] **Step 6: Confirm the scheduled task is armed**

Run: `schtasks /query /tn "Business Brain Notion Meeting Pull" /fo LIST`
Expected: Daily at 4:00 PM, Ready.

---

## Self-Review Notes

- **Spec coverage:** dedicated DB (Task 4 `create_meetings_db` + Task 9 Step 2), connector (Tasks 1-5), once-a-day 4 PM run (Tasks 6-7), masking (Task 5 uses `mask_text`), idempotency (Task 3 manifest + Notion `Ingested` write-back in Task 5), privacy gate (Task 6), registry flip (Task 8), live validation (Task 9). All spec sections map to a task.
- **No placeholders:** every code step shows complete code; only Task 9 (inherently live/manual) uses `<token>` placeholders Joshua fills.
- **Type consistency:** `parse_env`, `blocks_to_markdown`, `rich_text_to_str`, `target_name`, `needs_ingest`, `load_manifest`, `with_retries`, `TransientAPIError`, `_request`, `query_uningested`, `fetch_block_tree`, `mark_ingested`, `create_meetings_db`, `page_date`, `run`, `main` — names consistent across tasks; `run()` in Task 5 calls only helpers defined in Tasks 1-4.
