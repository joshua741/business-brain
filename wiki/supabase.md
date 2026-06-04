---
name: supabase
type: entity
tags: [database, backend]
status: active
sources: [CLAUDE.md seed, transcript-2026-06-02-meeting.md]
updated: 2026-06-04
---

# Supabase

**Summary**: PostgreSQL database backend for wih-app and related services.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Provides the database layer for [[wih-app]]. Deployed alongside [[railway]] for the WIH web application.

It is now the destination for the ~16,375-contact CRM migration off [[ghl]] (GHL is reduced to a data source, no longer the system of record). Supabase backs the [[wih-app]] "Us" build, where it serves as storage/backup while [[railway]] handles hosting. Connection is via the session pooler / direct connection string plus the DB password.

## Live state (as of 2026-06-04, source: [[source-supabase-snapshot-2026-06-04]])
14 public tables. Key counts:
- `directory_contacts`: **14,206** (GHL migration ~87% complete)
- `contacts`: 2 (Joshua Webber, Aaron Burch)
- `conversations`: 1 active (Vince ↔ Joshua test thread, last message Jun 4 01:42 UTC)
- `messages`: 9 (the Vince SMS system is live and writing to DB)
- `pipeline_stages`: 14 configured
- All lead/deal tables (agent_profiles, buyer_profiles, deals, call_logs): empty — not yet populated

## Related pages
- [[wih-app]]
- [[railway]]
- [[ghl]]
