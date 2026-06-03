# Business Brain — Self-Feeding Auto-Ingest System

**Date:** 2026-06-03
**Status:** Design — pending approval
**Owner:** Joshua Webber

## Goal

Make the Business Brain self-feeding. Every source connected to the business — and every Claude conversation — automatically deposits a detailed summary report into `raw/`, which the existing daily loop ingests into the wiki and proposes back into the master prompts (`CLAUDE.md` + Notion). New connections must be picked up automatically or loudly flagged — never silently missed, never added by hand after the fact.

## Decisions (locked 2026-06-03)

1. **Hub model:** Hybrid + registry. n8n pulls the data connectors (it already holds most credentials); Notion and conversations arrive via Claude/hooks; a single registry + gap-detector governs coverage.
2. **Conversation capture:** Auto Claude Code **Stop hook** — writes a session summary report at session end, no manual step.
3. **Cadence:** Mixed — connectors pull daily (diff-based), conversations land in real time at session end, the 6:57 AM loop ingests everything.
4. **Sensitive data:** Mask identifiers (account/routing/card/SSN → last-4 or masked), keep all balances, amounts, dates, and names.

## Current state (what already exists)

- GitHub repo `joshua741/business-brain` holds the vault.
- **`sync.ps1`** (Task `BusinessBrainSync`, 5:30 AM): `git pull` + propagate `CLAUDE.md` to session location.
- **`daily-wiki-maintenance.ps1`** (Task `Business Brain Daily Wiki Maintenance`, 6:57 AM): pull → Claude headless ingest of `raw/` files newer than `.last-ingest` → lint → commit → push.
- Wiki ingest pattern (source page + entity/concept enrichment + index/log) is established and working.

### Two known defects in the current loop

- **It only ingests files *newer than* `.last-ingest`.** Pre-existing backlog files are skipped forever. (This is why 117 files sat un-ingested until the manual sweep on 2026-06-02.)
- **The headless agent asks for approval instead of writing.** The 2026-06-02 run analyzed the backlog then ended with "approve writes" — a cron job can't answer. The prompt must force autonomous execution.

## Architecture

```
                          ┌─────────────── INPUT STREAMS ───────────────┐
  Business connectors ──▶ n8n extractors ─┐
  (GHL, Stripe, Mercury,                  │
   DoorLoop, BookingKoala,                ├─▶ masking filter ─▶ raw/*.md ─▶ git push
   Google Sheets, Notion,                 │
   Supabase, Twilio, Gumloop, Telegram)   │
                                          │
  Claude Code sessions ──▶ Stop hook ─────┘   (real-time, session end)
                          ┌──────────── GOVERNANCE ────────────┐
  connectors.yaml (registry)  +  discovery/gap detector ──▶ raw/_gaps-DATE.md + log.md

                          ┌──────────── OUTPUT ────────────┐
  raw/*.md ─▶ 6:57 AM ingest loop ─▶ wiki/*.md + index.md + log.md
                                   └─▶ proposes CLAUDE.md / Notion master-prompt updates
```

## Components (isolated units)

Each unit has one purpose, a defined interface, and can be tested alone.

### 1. Connector extractors (one per source)
- **What:** Pull from a single source, write `raw/<source>-snapshot-YYYY-MM-DD.md` as a structured summary report (not a raw dump).
- **Where:** n8n workflows (leverages existing credentials). `n8n` and `Gumloop` may self-report their run outputs.
- **Interface:** input = stored credential; output = one dated `.md` report, masked, pushed to repo.
- **Independent:** a failure in one extractor never blocks others.

### 2. Connector registry — `connectors.yaml` (repo root)
- **What:** Declarative source of truth. One entry per source:
  `name, type (api|mcp|file|hook), extractor (workflow id / hook), schedule, last_pull, sensitivity, status (active|manual|gap)`.
- **Purpose:** Defines expected coverage. Everything else reconciles against this.

### 3. Discovery + gap detector (runs inside the 6:57 AM job)
- **What:** Enumerate *live* connections — `claude mcp list`, n8n credentials (n8n API), Google/Notion OAuth grants — and diff against the registry.
- **Output:** For each connected source with no extractor → flag in `log.md` and write `raw/_gaps-YYYY-MM-DD.md`. Auto-pull any MCP-connected source that lacks a manual extractor.
- **This is the "don't make me add it manually" guarantee:** it can't author an extractor for an unknown API, but a new connection is auto-pulled (if MCP) or surfaced the next morning (if not) — never silent.

### 4. Conversation capture hook
- **What:** Claude Code **Stop hook** → runs a `claude --print` summarizer over the session transcript → writes `raw/conversation-YYYY-MM-DD-HHMM-topic.md`.
- **Report contents:** what was done, decisions made, current state, next steps, any new business facts, contradictions surfaced.
- **Scope:** Claude Code sessions on this machine. Claude.ai/desktop chats are out of scope for the hook (see Gaps).

### 5. Masking filter (shared)
- **What:** Applied to every report before write. Masks bank account/routing numbers, card numbers (keep last 4), full SSNs/EINs-of-individuals; **keeps** balances, amounts, dates, names, addresses.
- **Where:** a shared step both extractors and the hook call.

### 6. Ingest loop (hardened `daily-wiki-maintenance.ps1`)
- **Fixes:** (a) ingest by reconciliation, not date filter — ingest any `raw/` file with no corresponding source page, regardless of age; (b) rewrite the prompt to execute all writes autonomously and never ask; (c) add a verification step (every raw file must end with a source page, else re-run / flag).

### 7. Master-prompt sync
- **What:** After ingest, the agent updates the wiki, then proposes a `CLAUDE.md` diff in the next interactive session (per existing "never update silently" rule) and flags the Notion Business/Personal master-prompt update. On approval, `sync.ps1` propagates `CLAUDE.md`.

## Per-connector extraction map

| Source | Contributes | Path | Cadence | Notes |
|---|---|---|---|---|
| GHL | pipelines, contacts, conversations, opportunities | API (v1/v2) via n8n | daily | central comms hub |
| DoorLoop | leases, tenants, maintenance, P&L | API/export | daily | |
| Baselane | statements, balances | email-forward / file parse | on arrival | **no robust API — manual/parse** |
| Mercury | balances, transactions | API | daily | |
| Stripe | payments, payouts, disputes | API | daily | |
| BookingKoala | bookings, customers, payouts | API / Sheets sync | daily | |
| Google Sheets | KPI + finance trackers | Sheets API | daily | reads dashboards directly |
| Notion | master prompts, Vince memory, DBs | Notion API | daily | also output target |
| Supabase | wih-app data | SQL/API | daily | |
| Twilio | SMS/voice logs | API | daily | |
| Gumloop / n8n | Vince V2 + workflow runs | API / self-write | per run | |
| Telegram | personal channel | Bot API | daily | personal context |
| Claude sessions | decisions, work, next steps | Stop hook | real-time | |

## Data flow & cadence

1. **Overnight (4:00–5:00 AM):** connector extractors run, mask, write dated reports, push to repo. Diff-based — a report is emitted only if the source changed since last snapshot.
2. **5:30 AM:** `sync.ps1` pulls.
3. **Session end (real-time):** Stop hook writes the conversation report.
4. **6:57 AM:** ingest loop runs discovery/gap detection, ingests all new raw, lints, proposes master-prompt updates, commits, pushes.

## Error handling / failure modes

- **Extractor failure:** registry `last_pull` not advanced; surfaced in `raw/_gaps-DATE.md`. No silent skip.
- **Ingest non-interactivity:** prompt forces autonomous writes; post-run verification asserts `count(raw new) == count(source pages new)`, else re-run once then flag.
- **Token cost:** reports are summaries, not dumps; diff-based emission; conversation summaries capped in length.
- **Dedup/conflict:** reports namespaced by `source + date`; wiki ingest merges into entity pages using the existing pattern; overlapping sources (e.g., Baselane vs Mercury) cross-linked, not duplicated.

## Privacy & security posture (confirmed 2026-06-03)

Balancing privacy with "don't stop progress." Repo `joshua741/business-brain` is **confirmed PRIVATE** — the foundational control. Layered on top:

- **Repo stays private, permanently.** A lint check asserts visibility is still private on each run; flags loudly if it ever flips.
- **Secrets never enter the vault.** API keys, tokens, and credentials live only in the n8n credential store / environment variables — never in `raw/`, `wiki/`, or any report. Extractors and the Stop hook are forbidden from writing credentials.
- **Masking is mandatory and audited.** The shared masking filter masks account/routing/card/SSN; a lint step scans `raw/` + `wiki/` for leaked identifier patterns each run and flags hits. Masking trades a small amount of completeness for a large reduction in blast radius if the repo ever leaked.
- **Trust boundary:** data flows only to (a) the private GitHub repo and (b) the Anthropic API for summarization/ingestion. No third party beyond those.
- **Efficiency is preserved** via diff-based emission, summaries (not dumps), reuse of the existing 6:57 AM loop and n8n, and phased rollout — privacy controls add checks, not roadblocks.

## Open gaps / risks (kept in sight)

1. **Zero MCP today.** Nothing is connected to Claude directly; hybrid model chosen so this isn't blocking. Revisit Claude-as-hub later if MCP coverage grows.
2. **Baselane has no real API.** Likely stays email-forward/file-drop; registry marks it `manual`.
3. **Claude.ai/desktop chats uncaptured.** Local hook covers Claude Code only. Web chats need a Claude.ai export/connector path — registry flags this as an open gap until solved.
4. **Irreducible one-touch step for brand-new APIs.** The system can't self-author an extractor for an unknown service; it flags the gap and the human adds one registry entry + one n8n credential. Goal is to make that the *only* manual step, ever.
5. **Repo secrecy.** RESOLVED — repo confirmed PRIVATE (2026-06-03). Ongoing control: lint asserts visibility stays private.
6. **Masking completeness.** Masking is regex-based and best-effort; the lint audit of `raw/` + `wiki/` for leaked identifiers is the backstop.

## Phased rollout

- **Phase 1 (immediate value, no external deps):** harden the ingest loop (reconciliation-based, autonomous, verified) + conversation Stop hook + masking filter.
- **Phase 2:** registry + discovery/gap detector + first 3 connectors via n8n (recommend Google Sheets, Stripe, Notion — all have clean APIs).
- **Phase 3:** remaining connectors + master-prompt auto-proposal + Notion two-way sync.

## Out of scope (YAGNI)

- Real-time webhook ingestion for every source (cadence decision was mixed/daily).
- Aggressive redaction of dollar figures (rejected — precision needed).
- A custom dashboard UI (Obsidian + wiki is the view).
