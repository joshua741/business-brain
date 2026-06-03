---
name: doorloop
type: entity
tags: [property-management, crm]
status: active
sources: [CLAUDE.md seed, memo-2026-05-31T12-03-10-session.md]
updated: 2026-06-03
---

# DoorLoop

**Summary**: Property management platform for WIH — leases, charges, maintenance, and tenant communications.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Primary platform for managing the [[wih]] rental portfolio. Handles leases, rent charges, maintenance requests, and tenant comms across all Lubbock properties. Operated by [[mostafa]]. Generates per-property cash-basis P&L statements — see [[source-webber-2025-pl]] (e.g. [[4019-37th-st]] net $14,649.74, [[7005-winston-ave]] net $12,559 for 2025).

> **Integration status:** DoorLoop is **not wired for live data** in Joshua's Claude environment (no API/MCP connection). Claude can read exported DoorLoop notes/statements dropped into `raw/` but cannot pull live tenant/lease/maintenance records. Live access would be a real project — DoorLoop has an API, connectable via [[ghl]]/[[zapier]] or [[wih-ai-service]] (source: memo-2026-05-31T12-03-10-session.md).

## Related pages
- [[wih]]
- [[mostafa]]
- [[source-webber-2025-pl]]
