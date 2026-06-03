---
name: supabase
type: entity
tags: [database, backend]
status: active
sources: [CLAUDE.md seed, transcript-2026-06-02-meeting.md]
updated: 2026-06-03
---

# Supabase

**Summary**: PostgreSQL database backend for wih-app and related services.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Provides the database layer for [[wih-app]]. Deployed alongside [[railway]] for the WIH web application.

It is now the destination for the ~16,000-contact CRM migration off [[ghl]] (GHL is reduced to a data source, no longer the system of record). Supabase backs the [[wih-app]] "Us" build, where it serves as storage/backup while [[railway]] handles hosting. Connection is via the session pooler / direct connection string plus the DB password.

## Related pages
- [[wih-app]]
- [[railway]]
- [[ghl]]
