---
name: doorloop
type: entity
tags: [property-management, crm]
status: active
sources: [CLAUDE.md seed, memo-2026-05-31T12-03-10-session.md, transcript-2026-05-27-morning-meeting-josh-mostafa.md, transcript-2026-06-02-meeting.md]
updated: 2026-06-03
---

# DoorLoop

**Summary**: Property management platform for WIH — leases, charges, maintenance, and tenant communications.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Primary platform for managing the [[wih]] rental portfolio. Handles leases, rent charges, maintenance requests, and tenant comms across all Lubbock properties. Operated by [[mostafa]]. Generates per-property cash-basis P&L statements — see [[source-webber-2025-pl]] (e.g. [[4019-37th-st]] net $14,649.74, [[7005-winston-ave]] net $12,559 for 2025).

> **Integration status:** DoorLoop is **not wired for live data** in Joshua's Claude environment (no API/MCP connection). Claude can read exported DoorLoop notes/statements dropped into `raw/` but cannot pull live tenant/lease/maintenance records. Live access would be a real project — DoorLoop has an API, connectable via [[ghl]]/[[zapier]] or [[wih-ai-service]] (source: memo-2026-05-31T12-03-10-session.md).

## Cost & replacement plan
DoorLoop costs **~$265/mo billed PER LEASE/tenant** — so it scales (gets more expensive) as the portfolio grows. Joshua's plan is to **replace it with a custom in-house property-management dashboard + tenant portal** (the [[wih-app]] "Us" build), potentially saving ~$500/mo.

## Integrations & automations
- **Zapier "AI Employee":** connected via a Zapier API key that syncs tenant payment data into a [[google-sheets|Google Sheet]] ("tenant payment checklist") on a Mon/Wed/Fri 8am schedule.
- **SMS late-tenant skill:** live for 14 of 15 leases. The message triggers one day before the grace period expires; AI drafts it and Joshua approves via the DoorLoop mobile push notification. New tenants require the SMS checkboxes ticked in the lease — this can't be set via API.

**SOP:** tenant payment follow-ups go through DoorLoop.

One property — [[4438-puffer-st]] — is **NOT** on DoorLoop; it's serviced by [[one-point-lending]].

## Related pages
- [[wih]]
- [[mostafa]]
- [[source-webber-2025-pl]]
- [[wih-app]]
- [[one-point-lending]]
- [[google-sheets]]
