# meeting-tasks — Design Spec

**Date:** 2026-06-03
**Status:** Approved design, pre-implementation
**Owner:** Claude (maintained), Joshua (curates)

---

## Problem

There is no task list in the system. Action items live as ~105 scattered, unchecked
checkboxes inside dated meeting transcripts (Morning Meetings, tenant/investor calls)
that the `notion-meetings` connector pulls into `raw/`. The same action item recurs
across consecutive meetings (e.g. "follow up with Veronica about late payment" appeared
in both 2026-06-02 meetings). Checking boxes inside a dated transcript snapshot tracks
nothing going forward, and there is no signal for which items are actually done.

When asked to "check off tasks," there was nothing to check — that is the gap this closes.

## Goal

One living, deduped task list that is the single source of truth for "what needs doing,"
auto-built from meeting transcripts, surfaced where Joshua and Mostafa already work
(Notion), and where completion is recorded by humans — never fabricated by the AI.

## Non-Goals (YAGNI)

- Not a project-management app, no subtasks/dependencies/Gantt.
- Not auto-completing tasks based on inference.
- Not sending any outbound messages (that stays with Mostafa via GHL).
- Not replacing the `ingest-transcripts` skill (that routes *context* into master prompts;
  this routes *action items* into a task list — different output, same input).

---

## Architecture

A new skill `meeting-tasks` plus a supporting extractor, run as a step after the daily
transcript ingest. Follows the existing `connectors/` + skill conventions.

### Components

1. **Extractor — `connectors/meeting_tasks.py`** (stdlib only, mirrors `notion_meetings.py`)
   - Parses the already-masked `raw/*.md` transcripts for checkbox lines (`- [ ]` /
     `- [x]`) and items under an "Action items" heading. Chosen over re-walking Notion
     blocks: decoupled from the API, works offline, and the text is already masked.
   - Emits a list of candidate tasks: `{text, owner, source_file, meeting_date}`.

2. **Merge engine — same module**
   - Loads the source of truth `tasks/tasks.json`.
   - Dedups candidates against existing open tasks by normalized text similarity
     (lowercased, punctuation-stripped, owner-aware). A match updates `last_seen` +
     appends the source meeting; a non-match creates a new task.
   - Carries forward: one task, many sightings — never duplicate rows per meeting.

3. **Notion sync — same module**
   - Creates (once) a Notion **Tasks** database under an existing integration-shared page.
   - Pushes new/updated open tasks as DB rows.
   - Reads back the `Status` (or a Done checkbox) of existing rows and marks the matching
     `tasks.json` entries `done` — this is the only path to completion.

4. **Renderer — same module**
   - Writes `wiki/tasks.md` (Obsidian-visible, grouped by owner then status) from
     `tasks.json` so the list is readable in the vault without opening Notion.

5. **Skill — `~/.claude/skills/meeting-tasks/SKILL.md`**
   - Orchestrates: run extractor → merge → Notion sync → render → report.
   - Invokable manually ("update my tasks") and wired into the daily pipeline after ingest.

### Data model — `tasks/tasks.json`

```json
{
  "tasks": [
    {
      "id": "t-0001",
      "text": "Follow up with Veronica about late payment and payment plan",
      "owner": "Mostafa",
      "status": "open",            // open | done | stale-review
      "first_seen": "2026-06-02",
      "last_seen": "2026-06-02",
      "sources": ["transcript-2026-06-02-morning-meeting.md"],
      "notion_page_id": "..."      // set after first push, used for read-back
    }
  ]
}
```

### Notion Tasks DB schema

| Property | Type | Notes |
|---|---|---|
| Task | title | the action item text |
| Owner | select | Joshua / Mostafa / M'kenzy / Kenneth / Other |
| Status | select | Open / Done (human-set; read back by the skill) |
| First seen | date | |
| Last seen | date | |
| Source | rich_text | source transcript filename(s) |

DB is created under a page already shared with the integration (e.g. "Systems & Processes").
DB creation under an existing shared page is supported by the Notion API; teamspace/member
creation is not (per prior finding) — so we attach, not create a teamspace.

---

## Data flow

```
daily ingest (notion-meetings)  →  new transcripts in raw/
        │
        ▼
meeting_tasks.py: extract action items  →  dedup/merge into tasks/tasks.json
        │
        ├─►  render wiki/tasks.md  (Obsidian view)
        │
        └─►  push open tasks to Notion Tasks DB
                    │
                    ▼
        read back Status from Notion  →  mark done in tasks.json
```

## Completion rule (the rule that was missing)

- Tasks are created `open`. The AI **never** sets `done`.
- `done` is set only by reading a human-set Status=Done back from the Notion DB.
- If an open task has not been seen in N days (default 14) and shows no completion signal,
  the skill sets it to `stale-review` and lists it for Joshua/Mostafa to confirm — it is
  surfaced, never silently closed or checked.

## Error handling

- Missing `NOTION_API_KEY` → run file-only (extract, merge, render); skip Notion sync;
  print a clear notice. Mirrors `notion_meetings.py` self-skip behavior.
- Notion API 429/5xx → exponential backoff retry (reuse the `with_retries` pattern).
- Dedup is conservative: when uncertain whether two items match, create a new task rather
  than wrongly merging (a duplicate is cheaper to dismiss than a lost task).
- All extracted text passes through `lib/mask_sensitive.mask_text` before any write,
  consistent with the rest of `raw/`/`wiki/`.

## Testing (live-validate, per Joshua's "ship it, test it" rule)

1. Unit: dedup engine merges the two 2026-06-02 "Veronica late payment" items into one task.
2. Unit: extractor pulls the 06-02 action items and assigns owners correctly.
3. Live: run against current `raw/`, confirm `tasks.json` + `wiki/tasks.md` populate,
   confirm the Notion Tasks DB is created and rows appear.
4. Live loop: manually set one row to Done in Notion, re-run, confirm `tasks.json` flips
   that task to `done` and `tasks.md` reflects it.

## Open question deferred to implementation

- Exact parent page for the Notion DB ("Systems & Processes" vs a new "Operations" page) —
  decided at build time from what is shared with the integration.

## Related

- `connectors/notion_meetings.py` — source of the transcripts; pattern to mirror.
- `ingest-transcripts` skill — sibling consumer of the same transcripts (context, not tasks).
- Pending "Mostafa daily scheduler" Task DB — this design realizes it.
