# Notion Meeting-Notes Ingest — Design

**Date:** 2026-06-03
**Status:** Approved design, pending implementation
**Author:** Claude (brainstormed with Joshua)

---

## Goal

Automatically pull the Notion AI meeting notes from Joshua's ~2-hour morning team meetings (with Mostafa) into the Business Brain: write them to `raw/` and ingest them into `wiki/` once per day, with no manual steps after setup.

## Decisions (locked)

| Question | Decision |
|---|---|
| Where do transcripts originate? | Notion AI Meeting Notes (each becomes a Notion page) |
| Where are they stored today? | Scattered → consolidate into one dedicated **"Team Meetings" database** |
| Freshness requirement | **Once-a-day pull** is sufficient |
| Run time | **4:00 PM** daily (after meeting, before 5 PM email batch) |
| Who creates the Notion DB? | Claude creates it **via the Notion API** once the token exists |
| Auth method | **Notion internal integration token** (not MCP/OAuth — OAuth dies in headless Task Scheduler runs) |

## The one manual prerequisite (Joshua only)

Claude cannot log into Notion. Joshua must, once:

1. Go to `notion.so/my-integrations` → create an internal integration (e.g. "Business Brain") → copy the **Internal Integration Secret** (starts with `ntn_` / `secret_`).
2. Pick a parent page in Notion where the new "Team Meetings" database should live, and **share that page with the integration** (Connections → add the integration). Provide its page URL/ID to Claude.

Everything after that is automated.

---

## Architecture

A **second, independent** scheduled run — separate from the existing 6:57 AM `daily-wiki-maintenance.ps1`, which fires *before* the meeting and therefore can't see the notes.

```
4:00 PM Windows Task
   └─ notion-meetings-pull.ps1
        1. git pull
        2. python connectors/notion_meetings.py   ── pulls new notes → raw/*.md (masked)
        3. claude --print  <ingest agent prompt>   ── raw → wiki (same agent as daily run)
        4. python lib/audit_secrets.py             ── secret audit (warning)
        5. gh repo private check                    ── hard privacy gate
        6. git add/commit/push  (only if changes)
```

### Component 1 — `connectors/notion_meetings.py`

A new connector, modeled on `local_files.py`. Responsibilities:

- **Config:** read `NOTION_API_KEY` and `NOTION_MEETINGS_DB_ID` from a gitignored `.env` at repo root (small inline parser — no new dependency).
- **DB bootstrap (one-time):** if `NOTION_MEETINGS_DB_ID` is empty, create the "Team Meetings" database under the shared parent page via `POST /v1/databases`, then print the new DB id for Joshua to paste into `.env`. Properties: `Name` (title), `Date` (date), `Attendees` (multi-select), `Ingested` (checkbox — written back after ingest to prevent re-pulls).
- **Query:** `POST /v1/databases/{id}/query` filtered to pages where `Ingested` is unchecked (fallback: `created_time` on-or-after a stored cursor). This handles the "only new notes" requirement robustly even if a run is missed.
- **Fetch content:** walk each page's blocks via `GET /v1/blocks/{id}/children` (paginated, recursing into children) and flatten to Markdown — paragraphs, headings, bullets, to-dos, toggles, callouts. This captures the full transcript + AI summary that Notion AI Meeting Notes produces.
- **Mask:** run the flattened text through `lib/mask_sensitive.mask_text` (same gate every other source passes).
- **Write:** save to `raw/transcript-YYYY-MM-DD-team-meeting.md` (uses the page's Date; disambiguates with a `-2`, `-3` suffix if multiple notes share a date). Follows the existing source-routing naming convention. Never overwrites `raw/` content silently — idempotent via a `connectors/.notion-meetings-manifest.json` keyed by `page_id + last_edited_time`, so an edited note re-ingests but an unchanged one is skipped.
- **Write-back:** mark the Notion page `Ingested = true` after a successful raw write.
- **Flags:** `--report-only` (dry run, no writes, no manifest persist, no Notion write-back) mirroring `local_files.py`.

### Component 2 — `notion-meetings-pull.ps1`

A trimmed sibling of `daily-wiki-maintenance.ps1`, ASCII-only (per the PowerShell-encoding lesson), reusing its exact patterns: `$env:BB_CAPTURE_RUNNING=1` to suppress session-capture hooks, the same `claude.cmd` ingest-agent prompt (reconciliation-based, autonomous, no questions), the `audit_secrets.py` + `gh repo view --json isPrivate` privacy gate before any push, and append-to-log. Logs to `daily-maintenance.log` with a distinct `=== Notion meeting pull ===` banner.

### Component 3 — Windows Scheduled Task

`schtasks` daily trigger at 16:00 running `powershell.exe -ExecutionPolicy Bypass -File notion-meetings-pull.ps1`. Registered via a `.bat`/command mirroring the existing `setup-task.bat` pattern.

### Component 4 — Connector registry update

Flip the `notion` entry in `connectors/connectors.json` from `needs-credentials` to `active`, point `extractor` at `connectors/notion_meetings.py`, and note the 4 PM cadence. `discover_gaps.py` will then reflect it in `STATUS.md`.

---

## Data flow

```
Notion "Team Meetings" DB  ──API──>  notion_meetings.py  ──mask──>  raw/transcript-YYYY-MM-DD-team-meeting.md
                                                                          │
                                          ingest agent (claude --print) ──┘──>  wiki/ (source page + entity/person/project updates + index + log)
                                                                                      │
                                                              privacy gate + git push ┘
```

## Error handling

- **No token / no DB id:** connector prints a clear instruction and exits 0 (non-fatal) so the rest of the chain is a no-op rather than a crash.
- **No new notes today:** connector prints `no new meeting notes` and exits 0; ingest still runs harmlessly (reconciliation finds nothing new).
- **Notion API 429 / 5xx:** retry with backoff a few times, then log and exit 0 — never block the pipeline; the unchecked `Ingested` flag means it retries tomorrow.
- **Privacy gate:** identical hard stop to the daily script — if the GitHub repo is ever not private, abort before commit/push.
- **Secret safety:** `.env` is added to `.gitignore`; the token never enters `raw/`, `wiki/`, or git.

## Testing / validation (live, per Joshua's "test it before trusting it")

1. Run `python connectors/notion_meetings.py --report-only` after token+DB setup → confirm it sees the DB and would pull the right pages.
2. Drop one real (or sample) meeting note in the DB, run the connector for real → confirm a masked `raw/transcript-*.md` appears and the Notion page flips to `Ingested`.
3. Run `notion-meetings-pull.ps1` manually once → confirm wiki source page + links created, privacy gate passes, commit/push happens.
4. Confirm the 4 PM scheduled task is registered (`schtasks /query`).

## Out of scope (YAGNI)

- Real-time / push ingestion (webhooks, n8n) — explicitly rejected; once-a-day is enough.
- Pulling other Notion content (master prompts, Vince memory) — separate connector, later.
- Notifying Mostafa — not requested here.

## Related
- Existing: `daily-wiki-maintenance.ps1`, `connectors/local_files.py`, `lib/mask_sensitive.py`, `lib/audit_secrets.py`
- Memory: `notion-api-teamspace-member-limits`, `mostafa-daily-scheduler`, `windows-powershell-encoding`, `claude-cli-stdin-prompts`
