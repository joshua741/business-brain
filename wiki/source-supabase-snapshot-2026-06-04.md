---
name: source-supabase-snapshot-2026-06-04
type: source
tags: [supabase, wih-app, database, crm, snapshot]
sources: [supabase-snapshot-2026-06-04.md]
updated: 2026-06-04
---

# Supabase (wih-app DB) Snapshot — 2026-06-04

**Summary**: Read-only snapshot of the [[wih-app]] Supabase Postgres — 14 public tables, 14,206 directory contacts, live SMS conversation active.

**Sources**: supabase-snapshot-2026-06-04.md (Postgres, read-only)

**Last updated**: 2026-06-04

---

## Table row counts (2026-06-04)
| Table | Rows | Notes |
|---|---|---|
| directory_contacts | 14,206 | GHL contacts migrated so far (~87% of 16,375) |
| contacts | 2 | Joshua Webber + Aaron Burch |
| conversations | 1 | Active SMS conversation |
| messages | 9 | Outbound + inbound SMS |
| pipeline_stages | 14 | Configured |
| agent_profiles | 0 | Not yet populated |
| buyer_profiles | 0 | Not yet populated |
| deals | 0 | Not yet populated |
| call_logs | 0 | Not yet populated |

## Active conversation
A live conversation exists: contact Joshua Webber (+18XXXXX8495) via Twilio number +18XXXXX2532, last message 2026-06-04 01:42 UTC. 9 messages in/out — this is the Vince AI test/live thread visible in both Supabase and the Twilio log.

## Migration progress
**14,206 of ~16,375 GHL contacts** have been synced to `directory_contacts` — approximately 87% complete. Each row includes `ghl_contact_id` for reconciliation.

## Related pages
- [[wih-app]]
- [[supabase]]
- [[ghl]]
- [[twilio]]
- [[vince-ai]]
