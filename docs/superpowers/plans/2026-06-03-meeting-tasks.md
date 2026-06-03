# meeting-tasks Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Auto-build one deduped, living task list from meeting transcripts, render it for Obsidian, mirror it to a Notion Tasks DB, and record completion only from human-set Notion status.

**Architecture:** A stdlib-only extractor `connectors/meeting_tasks.py` parses masked transcripts in `raw/`, dedup-merges action items into `tasks/tasks.json` (source of truth), renders `wiki/tasks.md`, and one-way pushes open tasks to a Notion Tasks DB while reading back human-set Done status. A thin skill `~/.claude/skills/meeting-tasks/SKILL.md` orchestrates and is wired into the daily pipeline after ingest. Mirrors the existing `notion_meetings.py` connector conventions (DRY: reuses its `parse_env`, `_request`, `with_retries`, `TransientAPIError`).

**Tech Stack:** Python 3 stdlib (urllib, json, re, pathlib), pytest, Notion API v1 (`2022-06-28`), `lib/mask_sensitive.mask_text`.

---

## File Structure

- Create: `connectors/meeting_tasks.py` — extractor, dedup/merge, renderer, Notion sync, `run`/`main`.
- Create: `tests/test_meeting_tasks.py` — unit tests (pure functions; no network).
- Create: `~/.claude/skills/meeting-tasks/SKILL.md` — orchestration skill.
- Create (at runtime): `tasks/tasks.json`, `wiki/tasks.md`, `tasks/.notion-tasks-db.json`.
- Modify: `connectors/connectors.json` — register the connector.
- Modify: `daily-wiki-maintenance.ps1` — add the step after the ingest connectors.

Reused as-is (do not modify): `connectors/notion_meetings.py`, `lib/mask_sensitive.py`.

---

### Task 1: Module scaffold + reused helpers

**Files:**
- Create: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_meeting_tasks.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "connectors"))
import meeting_tasks as mt


def test_module_constants_and_reuse():
    # reuses notion_meetings.parse_env (DRY)
    assert callable(mt.parse_env)
    assert mt.NOTION_VERSION == "2022-06-28"
    assert str(mt.TASKS_JSON).endswith("tasks.json")
    assert str(mt.TASKS_MD).endswith("tasks.md")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_module_constants_and_reuse -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'meeting_tasks'`

- [ ] **Step 3: Write minimal implementation**

```python
# connectors/meeting_tasks.py
#!/usr/bin/env python3
"""meeting-tasks connector: extract action items from masked transcripts in raw/,
dedup-merge into tasks/tasks.json (source of truth), render wiki/tasks.md, and
one-way sync to a Notion Tasks DB (completion is read back from human-set status,
never written by this script). Stdlib only. Mirrors notion_meetings.py."""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
TASKS_DIR = REPO / "tasks"
TASKS_JSON = TASKS_DIR / "tasks.json"
TASKS_MD = REPO / "wiki" / "tasks.md"
DB_STATE = TASKS_DIR / ".notion-tasks-db.json"
ENV_FILE = REPO / ".env"
NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"
STALE_DAYS = 14

sys.path.insert(0, str(REPO / "connectors"))
sys.path.insert(0, str(REPO / "lib"))
from notion_meetings import parse_env, _request, with_retries, TransientAPIError  # noqa: E402
from mask_sensitive import mask_text  # noqa: E402

KNOWN_OWNERS = ["Joshua", "Josh", "Mostafa", "Mustafa", "M'kenzy", "Kenneth", "Tracy", "Team"]
OWNER_CANON = {"Josh": "Joshua", "Mustafa": "Mostafa"}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_module_constants_and_reuse -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): module scaffold reusing notion_meetings helpers"
```

---

### Task 2: Owner extraction

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_owner_of():
    assert mt.owner_of("Joshua to call Don Pittman at 3pm") == "Joshua"
    assert mt.owner_of("Mustafa to email watermarked images") == "Mostafa"  # canonicalized
    assert mt.owner_of("Team to explore Sequence integration") == "Team"
    assert mt.owner_of("Add difference to Joseph De La O's account") == "Unassigned"
    assert mt.owner_of("") == "Unassigned"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_owner_of -v`
Expected: FAIL with `AttributeError: module 'meeting_tasks' has no attribute 'owner_of'`

- [ ] **Step 3: Write minimal implementation**

```python
def owner_of(text: str) -> str:
    """Owner is the name at the start of an action item phrased 'X to <verb> ...'."""
    t = (text or "").strip()
    m = re.match(r"^([A-Z][A-Za-z'']+)\s+to\s+", t)
    if m:
        name = m.group(1)
        if name in KNOWN_OWNERS:
            return OWNER_CANON.get(name, name)
    return "Unassigned"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_owner_of -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): owner extraction with name canonicalization"
```

---

### Task 3: Action-item extraction from transcript markdown

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_extract_action_items():
    md = (
        "# Morning Meeting\n\n"
        "## Summary\n\nWe met and discussed things.\n\n"
        "## Action items\n\n"
        "- [ ] Joshua to call Don Pittman at 3pm\n"
        "- [x] Mustafa to post 4513 48th Street property on Facebook Marketplace\n"
        "- [ ] Follow up with Veronica about late payment\n\n"
        "## Notes\n\n- not an action item\n"
    )
    items = mt.extract_action_items(md, "transcript-2026-06-02-morning-meeting.md", "2026-06-02")
    texts = [i["text"] for i in items]
    assert "Joshua to call Don Pittman at 3pm" in texts
    assert "Mustafa to post 4513 48th Street property on Facebook Marketplace" in texts
    assert "Follow up with Veronica about late payment" in texts
    assert "not an action item" not in texts  # bullet outside Action items + not a checkbox
    j = next(i for i in items if i["text"].startswith("Joshua"))
    assert j["owner"] == "Joshua"
    assert j["source_file"] == "transcript-2026-06-02-morning-meeting.md"
    assert j["meeting_date"] == "2026-06-02"
    assert j["seed_checked"] is False
    m = next(i for i in items if i["text"].startswith("Mustafa"))
    assert m["seed_checked"] is True  # transcript already had [x]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_extract_action_items -v`
Expected: FAIL with `AttributeError: ... has no attribute 'extract_action_items'`

- [ ] **Step 3: Write minimal implementation**

```python
CHECKBOX_RE = re.compile(r"^\s*-\s*\[( |x|X)\]\s+(.*\S)\s*$")
ACTION_HEADING_RE = re.compile(r"^#{1,6}\s*action items?\b", re.IGNORECASE)
PLAIN_BULLET_RE = re.compile(r"^\s*-\s+(?!\[)(.*\S)\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s+")


def extract_action_items(md_text: str, source_file: str, meeting_date: str) -> list:
    """Pull action items from a transcript: every checkbox line anywhere, plus plain
    bullets that sit under an 'Action items' heading. Returns dicts (text/owner/
    source_file/meeting_date/seed_checked)."""
    items, in_action = [], False
    for line in (md_text or "").splitlines():
        if HEADING_RE.match(line):
            in_action = bool(ACTION_HEADING_RE.match(line))
        cb = CHECKBOX_RE.match(line)
        if cb:
            text = cb.group(2).strip()
            items.append(_mk_item(text, source_file, meeting_date,
                                  cb.group(1).lower() == "x"))
            continue
        if in_action:
            pb = PLAIN_BULLET_RE.match(line)
            if pb:
                items.append(_mk_item(pb.group(1).strip(), source_file,
                                      meeting_date, False))
    return items


def _mk_item(text: str, source_file: str, meeting_date: str, checked: bool) -> dict:
    return {"text": text, "owner": owner_of(text), "source_file": source_file,
            "meeting_date": meeting_date, "seed_checked": checked}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_extract_action_items -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): extract action items from transcript markdown"
```

---

### Task 4: Normalization + match key for dedup

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_match_key():
    a = mt.match_key("Mostafa", "Follow up with Veronica about late payment and payment plan")
    b = mt.match_key("Mostafa", "Follow up with Veronica about late payment.")
    c = mt.match_key("Mostafa", "Follow up with Ronald about late payment")
    assert a == b      # trailing words/punctuation differences collapse to same key
    assert a != c      # different person -> different task
```

> Match key = owner + normalized first 6 significant words. Conservative: close
> variants of the same action collapse; genuinely different items stay separate.

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_match_key -v`
Expected: FAIL with `AttributeError: ... has no attribute 'match_key'`

- [ ] **Step 3: Write minimal implementation**

```python
_WORD_RE = re.compile(r"[a-z0-9]+")


def normalize(text: str) -> str:
    return " ".join(_WORD_RE.findall((text or "").lower()))


def match_key(owner: str, text: str) -> str:
    words = normalize(text).split()
    return f"{owner}::" + " ".join(words[:6])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_match_key -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): normalization and dedup match key"
```

---

### Task 5: Merge engine (dedup, carry-forward, id assignment)

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_merge_dedups_and_carries_forward():
    existing = []
    cands = [
        mt._mk_item("Follow up with Veronica about late payment and payment plan",
                    "transcript-2026-06-02-morning-meeting.md", "2026-06-02", False),
        mt._mk_item("Follow up with Veronica about late payment.",
                    "transcript-2026-06-02-call.md", "2026-06-02", False),
        mt._mk_item("Joshua to call Don Pittman at 3pm",
                    "transcript-2026-06-02-morning-meeting.md", "2026-06-02", False),
    ]
    merged = mt.merge(existing, cands, today="2026-06-02")
    # two Veronica variants collapse into one task -> 2 tasks total
    assert len(merged) == 2
    veronica = next(t for t in merged if "veronica" in t["text"].lower())
    assert len(veronica["sources"]) == 2
    assert veronica["status"] == "open"
    assert veronica["first_seen"] == "2026-06-02"
    assert veronica["id"] == "t-0001"
    # re-merging the same candidates later only updates last_seen, no new tasks
    again = mt.merge(merged, cands, today="2026-06-09")
    assert len(again) == 2
    assert next(t for t in again if "veronica" in t["text"].lower())["last_seen"] == "2026-06-09"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_merge_dedups_and_carries_forward -v`
Expected: FAIL with `AttributeError: ... has no attribute 'merge'`

- [ ] **Step 3: Write minimal implementation**

```python
def _next_id(tasks: list) -> str:
    n = 0
    for t in tasks:
        try:
            n = max(n, int(str(t.get("id", "t-0")).split("-")[1]))
        except (IndexError, ValueError):
            pass
    return f"t-{n + 1:04d}"


def merge(existing: list, candidates: list, today: str) -> list:
    tasks = [dict(t) for t in existing]
    index = {match_key(t["owner"], t["text"]): t for t in tasks}
    for c in candidates:
        key = match_key(c["owner"], c["text"])
        hit = index.get(key)
        if hit:
            hit["last_seen"] = today
            if c["source_file"] not in hit["sources"]:
                hit["sources"].append(c["source_file"])
        else:
            task = {
                "id": _next_id(tasks),
                "text": c["text"],
                "owner": c["owner"],
                "status": "open",
                "first_seen": c["meeting_date"] or today,
                "last_seen": today,
                "sources": [c["source_file"]],
                "notion_page_id": None,
            }
            tasks.append(task)
            index[key] = task
    return tasks
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_merge_dedups_and_carries_forward -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): dedup/carry-forward merge engine with stable ids"
```

---

### Task 6: Stale-review marking

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_mark_stale():
    tasks = [
        {"id": "t-1", "text": "old open", "owner": "Joshua", "status": "open",
         "first_seen": "2026-05-01", "last_seen": "2026-05-01", "sources": [], "notion_page_id": None},
        {"id": "t-2", "text": "recent open", "owner": "Joshua", "status": "open",
         "first_seen": "2026-06-01", "last_seen": "2026-06-01", "sources": [], "notion_page_id": None},
        {"id": "t-3", "text": "done stays done", "owner": "Joshua", "status": "done",
         "first_seen": "2026-05-01", "last_seen": "2026-05-01", "sources": [], "notion_page_id": None},
    ]
    out = mt.mark_stale(tasks, today="2026-06-03")
    assert {t["id"]: t["status"] for t in out} == {
        "t-1": "stale-review", "t-2": "open", "t-3": "done"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_mark_stale -v`
Expected: FAIL with `AttributeError: ... has no attribute 'mark_stale'`

- [ ] **Step 3: Write minimal implementation**

```python
def _days_between(d1: str, d2: str) -> int:
    fmt = "%Y-%m-%d"
    return (datetime.strptime(d1, fmt) - datetime.strptime(d2, fmt)).days


def mark_stale(tasks: list, today: str) -> list:
    for t in tasks:
        if t.get("status") == "open":
            try:
                if _days_between(today, t.get("last_seen", today)) >= STALE_DAYS:
                    t["status"] = "stale-review"
            except ValueError:
                pass
    return tasks
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_mark_stale -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): flag long-unseen open tasks as stale-review"
```

---

### Task 7: Markdown renderer

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_render_markdown():
    tasks = [
        {"id": "t-1", "text": "Call Don Pittman", "owner": "Joshua", "status": "open",
         "first_seen": "2026-06-02", "last_seen": "2026-06-02",
         "sources": ["transcript-2026-06-02-morning-meeting.md"], "notion_page_id": None},
        {"id": "t-2", "text": "Post 4513 to FB", "owner": "Mostafa", "status": "done",
         "first_seen": "2026-06-02", "last_seen": "2026-06-02", "sources": [], "notion_page_id": None},
    ]
    md = mt.render_markdown(tasks, today="2026-06-03")
    assert md.startswith("# Tasks")
    assert "## Joshua" in md and "## Mostafa" in md
    assert "- [ ] Call Don Pittman" in md          # open -> unchecked
    assert "- [x] Post 4513 to FB" in md           # done -> checked
    assert "_Generated 2026-06-03" in md
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_render_markdown -v`
Expected: FAIL with `AttributeError: ... has no attribute 'render_markdown'`

- [ ] **Step 3: Write minimal implementation**

```python
def render_markdown(tasks: list, today: str) -> str:
    by_owner = {}
    for t in tasks:
        by_owner.setdefault(t.get("owner", "Unassigned"), []).append(t)
    order = {"open": 0, "stale-review": 1, "done": 2}
    lines = ["# Tasks", "",
             "_Auto-built from meeting transcripts. Check items off in the Notion Tasks DB; "
             "this file mirrors that. Do not hand-edit._", ""]
    for owner in sorted(by_owner):
        lines.append(f"## {owner}")
        lines.append("")
        for t in sorted(by_owner[owner], key=lambda x: (order.get(x["status"], 3), x["id"])):
            box = "x" if t["status"] == "done" else " "
            tag = "  _(stale — confirm?)_" if t["status"] == "stale-review" else ""
            lines.append(f"- [{box}] {t['text']}{tag}")
        lines.append("")
    lines.append(f"_Generated {today}. Source of truth: tasks/tasks.json._")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_render_markdown -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): render tasks.md grouped by owner and status"
```

---

### Task 8: Load/save source of truth

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_load_save_roundtrip(tmp_path, monkeypatch):
    f = tmp_path / "tasks.json"
    monkeypatch.setattr(mt, "TASKS_JSON", f)
    assert mt.load_tasks() == []          # missing file -> empty
    data = [{"id": "t-1", "text": "x", "owner": "Joshua", "status": "open",
             "first_seen": "2026-06-02", "last_seen": "2026-06-02",
             "sources": [], "notion_page_id": None}]
    mt.save_tasks(data)
    assert mt.load_tasks() == data
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_load_save_roundtrip -v`
Expected: FAIL with `AttributeError: ... has no attribute 'load_tasks'`

- [ ] **Step 3: Write minimal implementation**

```python
def load_tasks() -> list:
    if TASKS_JSON.exists():
        try:
            return json.loads(TASKS_JSON.read_text(encoding="utf-8")).get("tasks", [])
        except (ValueError, OSError):
            return []
    return []


def save_tasks(tasks: list) -> None:
    TASKS_JSON.parent.mkdir(parents=True, exist_ok=True)
    TASKS_JSON.write_text(json.dumps({"tasks": tasks}, indent=2), encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_load_save_roundtrip -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): load/save tasks.json source of truth"
```

---

### Task 9: Notion sync — ensure DB, push rows, read back completion

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

These functions wrap network calls through the injected `req` callable so they are
unit-testable with a fake (no real HTTP). `req(method, url, body)` mirrors
`notion_meetings._request` minus the token (bound by the caller).

- [ ] **Step 1: Write the failing test**

```python
def test_apply_notion_status_marks_done():
    tasks = [
        {"id": "t-1", "text": "a", "owner": "Joshua", "status": "open",
         "first_seen": "2026-06-02", "last_seen": "2026-06-02", "sources": [],
         "notion_page_id": "pg-1"},
        {"id": "t-2", "text": "b", "owner": "Joshua", "status": "open",
         "first_seen": "2026-06-02", "last_seen": "2026-06-02", "sources": [],
         "notion_page_id": "pg-2"},
    ]
    # Notion says pg-1 is Done, pg-2 still Open
    remote_status = {"pg-1": "Done", "pg-2": "Open"}
    out = mt.apply_notion_status(tasks, remote_status)
    assert {t["id"]: t["status"] for t in out} == {"t-1": "done", "t-2": "open"}


def test_db_payload_shape():
    body = mt.new_db_payload("parent-page-id")
    assert body["parent"]["page_id"] == "parent-page-id"
    props = body["properties"]
    assert props["Task"]["title"] == {}
    assert "Open" in [o["name"] for o in props["Status"]["select"]["options"]]
    assert "Done" in [o["name"] for o in props["Status"]["select"]["options"]]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_apply_notion_status_marks_done tests/test_meeting_tasks.py::test_db_payload_shape -v`
Expected: FAIL with `AttributeError: ... has no attribute 'apply_notion_status'`

- [ ] **Step 3: Write minimal implementation**

```python
def new_db_payload(parent_page_id: str) -> dict:
    return {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": "Tasks"}}],
        "properties": {
            "Task": {"title": {}},
            "Owner": {"select": {}},
            "Status": {"select": {"options": [
                {"name": "Open"}, {"name": "Done"}, {"name": "Stale-review"}]}},
            "First seen": {"date": {}},
            "Last seen": {"date": {}},
            "Source": {"rich_text": {}},
        },
    }


def _row_payload(db_id: str, task: dict) -> dict:
    return {
        "parent": {"database_id": db_id},
        "properties": {
            "Task": {"title": [{"text": {"content": task["text"][:1900]}}]},
            "Owner": {"select": {"name": task.get("owner", "Unassigned")}},
            "Status": {"select": {"name": {"open": "Open", "done": "Done",
                       "stale-review": "Stale-review"}.get(task["status"], "Open")}},
            "First seen": {"date": {"start": task["first_seen"]}},
            "Last seen": {"date": {"start": task["last_seen"]}},
            "Source": {"rich_text": [{"text": {"content": ", ".join(task["sources"])[:1900]}}]},
        },
    }


def ensure_db(req, parent_page_id: str) -> str:
    """Return the Tasks DB id, creating it once and caching the id in DB_STATE."""
    if DB_STATE.exists():
        try:
            return json.loads(DB_STATE.read_text(encoding="utf-8"))["database_id"]
        except (ValueError, KeyError, OSError):
            pass
    res = req("POST", f"{API}/databases", new_db_payload(parent_page_id))
    DB_STATE.parent.mkdir(parents=True, exist_ok=True)
    DB_STATE.write_text(json.dumps({"database_id": res["id"]}, indent=2), encoding="utf-8")
    return res["id"]


def push_rows(req, db_id: str, tasks: list) -> None:
    """Create a Notion row for any task lacking a notion_page_id; update existing rows'
    Last seen + Source. Never writes Status=Done (humans own completion)."""
    for t in tasks:
        if not t.get("notion_page_id"):
            res = req("POST", f"{API}/pages", _row_payload(db_id, t))
            t["notion_page_id"] = res["id"]
        else:
            req("PATCH", f"{API}/pages/{t['notion_page_id']}",
                {"properties": _row_payload(db_id, t)["properties"]})


def fetch_remote_status(req, db_id: str) -> dict:
    """Return {page_id: status_name} for every row in the Tasks DB."""
    out, cursor = {}, None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        page = req("POST", f"{API}/databases/{db_id}/query", body)
        for row in page.get("results", []):
            sel = row.get("properties", {}).get("Status", {}).get("select")
            out[row["id"]] = sel["name"] if sel else "Open"
        if not page.get("has_more"):
            break
        cursor = page.get("next_cursor")
    return out


def apply_notion_status(tasks: list, remote_status: dict) -> list:
    """Completion flows only inward: a row humans marked Done becomes done locally."""
    for t in tasks:
        pid = t.get("notion_page_id")
        if pid and remote_status.get(pid) == "Done":
            t["status"] = "done"
    return tasks
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_meeting_tasks.py::test_apply_notion_status_marks_done tests/test_meeting_tasks.py::test_db_payload_shape -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): Notion Tasks DB ensure/push/read-back (inward completion)"
```

---

### Task 10: Orchestration `run()` + `main()` with self-skip

**Files:**
- Modify: `connectors/meeting_tasks.py`
- Test: `tests/test_meeting_tasks.py`

- [ ] **Step 1: Write the failing test**

```python
def test_run_file_only(tmp_path, monkeypatch):
    raw = tmp_path / "raw"; raw.mkdir()
    (raw / "transcript-2026-06-02-morning-meeting.md").write_text(
        "## Action items\n\n- [ ] Joshua to call Don Pittman at 3pm\n", encoding="utf-8")
    monkeypatch.setattr(mt, "RAW", raw)
    monkeypatch.setattr(mt, "TASKS_JSON", tmp_path / "tasks.json")
    monkeypatch.setattr(mt, "TASKS_MD", tmp_path / "tasks.md")
    # token=None -> file-only path, no network
    pulled = mt.run(token=None, parent_page_id=None, today="2026-06-02")
    tasks = mt.load_tasks()
    assert len(tasks) == 1 and tasks[0]["owner"] == "Joshua"
    assert (tmp_path / "tasks.md").read_text(encoding="utf-8").startswith("# Tasks")
    assert pulled == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_meeting_tasks.py::test_run_file_only -v`
Expected: FAIL with `AttributeError: ... has no attribute 'run'`

- [ ] **Step 3: Write minimal implementation**

```python
def _date_from_name(name: str) -> str:
    m = re.search(r"(\d{4}-\d{2}-\d{2})", name)
    return m.group(1) if m else ""


def _gather_candidates() -> list:
    cands = []
    for f in sorted(RAW.glob("transcript-*.md")):
        md = f.read_text(encoding="utf-8", errors="ignore")
        cands.extend(extract_action_items(md, f.name, _date_from_name(f.name)))
    return cands


def run(token, parent_page_id, today: str) -> int:
    tasks = load_tasks()
    candidates = _gather_candidates()
    # mask candidate text consistently with the rest of raw/wiki
    for c in candidates:
        c["text"] = mask_text(c["text"])
    new_count_before = len(tasks)
    tasks = merge(tasks, candidates, today)
    tasks = mark_stale(tasks, today)

    if token and parent_page_id:
        def req(method, url, body=None):
            return _request(method, url, token, body)
        db_id = ensure_db(req, parent_page_id)
        push_rows(req, db_id, tasks)
        tasks = apply_notion_status(tasks, fetch_remote_status(req, db_id))

    save_tasks(tasks)
    TASKS_MD.parent.mkdir(parents=True, exist_ok=True)
    TASKS_MD.write_text(render_markdown(tasks, today), encoding="utf-8")
    return len(tasks) - new_count_before


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report-only", action="store_true",
                    help="extract + merge in memory and print counts; write nothing")
    args = ap.parse_args()
    cfg = parse_env(ENV_FILE)
    token = cfg.get("NOTION_API_KEY", "").strip() or None
    parent = cfg.get("NOTION_TASKS_PARENT_PAGE_ID", "").strip() or None
    today = datetime.now().strftime("%Y-%m-%d")
    if args.report_only:
        cands = _gather_candidates()
        merged = merge(load_tasks(), cands, today)
        print(f"meeting-tasks (report-only): {len(cands)} action items across transcripts, "
              f"{len(merged)} unique tasks after merge.")
        return
    if not token:
        print("meeting-tasks: NOTION_API_KEY not set -- running file-only (no Notion sync).")
    elif not parent:
        print("meeting-tasks: NOTION_TASKS_PARENT_PAGE_ID not set -- file-only "
              "(set it to a page shared with the integration to enable the Tasks DB).")
    added = run(token, parent if token else None, today)
    print(f"meeting-tasks: {len(load_tasks())} tasks total ({added} new). "
          f"Rendered {TASKS_MD.name}.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the full test file**

Run: `python -m pytest tests/test_meeting_tasks.py -v`
Expected: PASS (all tests)

- [ ] **Step 5: Commit**

```bash
git add connectors/meeting_tasks.py tests/test_meeting_tasks.py
git commit -m "feat(meeting-tasks): run/main orchestration with file-only self-skip"
```

---

### Task 11: Register connector + wire into daily pipeline

**Files:**
- Modify: `connectors/connectors.json`
- Modify: `daily-wiki-maintenance.ps1:48` (after the ingest connectors block, before the gap detector at line 56)

- [ ] **Step 1: Add the registry entry**

In `connectors/connectors.json`, add this object to the `connectors` array (after the `ghl` entry):

```json
{
  "name": "meeting-tasks",
  "type": "skill",
  "status": "active",
  "source": "raw/transcript-*.md action items",
  "extractor": "connectors/meeting_tasks.py",
  "cadence": "daily",
  "credential_needed": "NOTION_API_KEY + NOTION_TASKS_PARENT_PAGE_ID (optional; file-only without them)",
  "notes": "Dedup-merges meeting action items into tasks/tasks.json, renders wiki/tasks.md, mirrors to a Notion Tasks DB. Completion read back from human-set Status; never AI-set."
}
```

- [ ] **Step 2: Add the pipeline step**

In `daily-wiki-maintenance.ps1`, after the last ingest connector line (the `google_sheets.py` / `mercury.py` block) and before the `# 2c. Connector discovery` comment, insert:

```powershell
# 2b-tasks. Build the rolling task list from meeting transcripts
& python "$repoPath\connectors\meeting_tasks.py" 2>&1 | ForEach-Object { Log $_ }
```

- [ ] **Step 3: Verify the script still parses**

Run: `powershell -NoProfile -Command "$null = [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path .\daily-wiki-maintenance.ps1), [ref]$null, [ref]$null); 'parse-ok'"`
Expected: `parse-ok`

- [ ] **Step 4: Verify the connector runs in report-only mode against real transcripts**

Run: `python connectors/meeting_tasks.py --report-only`
Expected: a line like `meeting-tasks (report-only): NN action items across transcripts, MM unique tasks after merge.` with MM < NN (dedup happened).

- [ ] **Step 5: Commit**

```bash
git add connectors/connectors.json daily-wiki-maintenance.ps1
git commit -m "feat(meeting-tasks): register connector and wire into daily pipeline"
```

---

### Task 12: Author the orchestration skill

**Files:**
- Create: `C:/Users/joshu/.claude/skills/meeting-tasks/SKILL.md`

- [ ] **Step 1: Write the skill file**

```markdown
---
name: meeting-tasks
description: Use when Joshua wants to build or refresh his task list from meeting transcripts, check what's outstanding, or reconcile completed tasks. Extracts and dedups action items from raw/ transcripts into one living list, renders wiki/tasks.md, and mirrors to the Notion Tasks DB. Runs automatically in the daily pipeline; invoke manually on request ("update my tasks", "what's on my list").
---

# Meeting Tasks

Maintains the single source of truth for outstanding action items: `tasks/tasks.json`,
rendered to `wiki/tasks.md`, mirrored to the Notion **Tasks** database.

## When to run
- Automatically: the daily pipeline calls `connectors/meeting_tasks.py` after transcript ingest.
- Manually: when Joshua says "update my tasks", "what's on my list", or after a new meeting lands.

## How to run
From the Business_Brain repo root:

- Preview without writing: `python connectors/meeting_tasks.py --report-only`
- Full run: `python connectors/meeting_tasks.py`

The script self-skips Notion when `NOTION_API_KEY` / `NOTION_TASKS_PARENT_PAGE_ID` are
absent and still updates the local files.

## Reporting back to Joshua
After a run, summarize: how many new tasks, what's open per owner (lead with Joshua's own
items), and anything now flagged `stale-review` for him to confirm. Lead with the answer,
no preamble.

## The one rule that matters
Never mark a task done yourself. Completion is set by Joshua/Mostafa in the Notion Tasks DB
and read back by the script. If something looks done, surface it as `stale-review` — do not
check it off.

## Related
- `connectors/notion_meetings.py` — pulls the transcripts this consumes.
- `ingest-transcripts` skill — sibling: routes meeting *context* into master prompts.
- Spec: `docs/superpowers/specs/2026-06-03-meeting-tasks-design.md`
```

- [ ] **Step 2: Validate the skill loads**

Run: `python -c "import pathlib,sys; p=pathlib.Path.home()/'.claude/skills/meeting-tasks/SKILL.md'; t=p.read_text(encoding='utf-8'); sys.exit(0 if t.startswith('---') and 'name: meeting-tasks' in t else 1)"`
Expected: exit 0 (no output)

- [ ] **Step 3: Commit (skill lives outside the repo; commit only repo files)**

The skill file is under `~/.claude/skills/` and is not part of the Business_Brain git repo.
No commit needed here; note its path in the run report. (If a skills repo exists, commit there.)

---

### Task 13: Live end-to-end validation (Joshua's "ship it, test it" gate)

**Files:** none (runtime validation)

- [ ] **Step 1: Confirm `NOTION_TASKS_PARENT_PAGE_ID` is set**

Pick a page already shared with the integration (e.g. "Systems & Processes"), put its id in
`.env` as `NOTION_TASKS_PARENT_PAGE_ID=...`. If unset, the run is file-only — still valid,
but the live loop in Steps 3-4 needs Notion.

Run: `python -c "import sys; sys.path.insert(0,'connectors'); from notion_meetings import parse_env; from pathlib import Path; c=parse_env(Path('.env')); print('parent set' if c.get('NOTION_TASKS_PARENT_PAGE_ID') else 'parent MISSING')"`
Expected: `parent set`

- [ ] **Step 2: Full run, confirm artifacts**

Run: `python connectors/meeting_tasks.py`
Expected: prints total + new counts. Then confirm files exist and look right:
- `tasks/tasks.json` has tasks with owners and `notion_page_id` populated.
- `wiki/tasks.md` lists tasks grouped by owner, Joshua's items present.
- The Notion "Tasks" database exists with rows.

- [ ] **Step 3: Live completion loop**

In Notion, set one task's Status to **Done**. Re-run:
Run: `python connectors/meeting_tasks.py`
Expected: that task's `status` in `tasks/tasks.json` is now `"done"` and it shows `- [x]` in `wiki/tasks.md`.

- [ ] **Step 4: Idempotency**

Run `python connectors/meeting_tasks.py` once more with no new transcripts.
Expected: `(0 new)` — no duplicate tasks created.

- [ ] **Step 5: Commit the generated source of truth**

```bash
git add tasks/tasks.json wiki/tasks.md
git commit -m "chore(meeting-tasks): initial generated task list + rolling render"
```

---

## Self-Review

**Spec coverage:** extractor (T3), dedup/carry-forward (T4-T5), source of truth (T8), renderer (T7), Notion DB create/push/read-back (T9), completion-inward rule (T9 `apply_notion_status` + skill rule T12), stale-review (T6), error/self-skip (T10), daily wiring + registry (T11), live tests incl. the 06-02 Veronica dedup (T5) and completion loop (T13). All spec sections map to a task.

**Placeholder scan:** no TBD/TODO; every code step is complete; the one spec "open question" (parent page) is resolved concretely in T13 Step 1 (use "Systems & Processes").

**Type consistency:** task dict shape (`id, text, owner, status, first_seen, last_seen, sources, notion_page_id`) is identical across T5, T6, T7, T8, T9, T10. Status vocab (`open` / `done` / `stale-review`) consistent; Notion select names (`Open` / `Done` / `Stale-review`) mapped in one place (`_row_payload`). `req(method, url, body)` signature consistent across T9 and bound once in T10.
