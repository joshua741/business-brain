---
name: mercury-api
type: concept
tags: [mercury, api, banking, payments, invoicing, automation]
updated: 2026-06-03
---

# Mercury API — Capabilities & Workflow Plan

**Summary**: What the [[mercury]] Banking API exposes and the plan for using it — read insight is automated now; money-moving and invoicing are planned as approval-gated actions.

**Sources**: live read-only probes 2026-06-03; Mercury API docs (to be ingested from Joshua's drop)

**Last updated**: 2026-06-03

---

Base: `https://api.mercury.com/api/v1`. Auth: `Authorization: Bearer <token>`. The token in use is **full read/write** (stored in gitignored `.env`, masked everywhere).

## Confirmed working (read, live-tested 2026-06-03)
- `GET /accounts` — account list + balances. (2 accounts: Checking ••3039, Savings ••2610.)
- `GET /account/{id}/transactions` — transaction history per account.
- `GET /recipients` — payees for payments (currently 0 configured).
These power the daily read snapshot via [[connectors]] (`connectors/mercury.py` → `raw/mercury-snapshot-DATE.md`, account/routing numbers masked).

## Write capability (planned — APPROVAL-GATED, not yet wired)
The token can also write. These are intentionally **not** connected to any automation yet; they will live in a separate tool that **pauses for Joshua's explicit approval** before executing:
- **Send payments / transfers** — create a transaction to a recipient (`POST /account/{id}/transactions`); Mercury also has its own in-app approval flow for production money movement.
- **Manage recipients** — add/update payees.
- **Invoicing** — Mercury supports native invoicing in-product (a key reason to adopt it, since WIH invoices a lot). Exact API endpoints for creating/sending invoices to be confirmed from the official docs Joshua is providing. Goal: generate + send invoices programmatically and track paid/unpaid status into the brain.

## Design principles
- **Read = automatic. Write = human-approved.** Nothing moves money or sends an invoice without an explicit "yes," until Joshua chooses to loosen specific actions.
- **Security:** full-access token currently allows any IP (Joshua is mobile). Long-term, run money-moving actions from a fixed-IP server ([[railway]]) and pin Mercury's IP whitelist to that one address. See [[baselane-to-mercury-migration]].
- Fits the strategy of the [[ai-automation-strategy|AI owning the money layer]] and the in-house "own the software" direction.

## Next steps
1. Ingest Mercury's official API docs (Joshua → `drop/`) to confirm invoicing + payment endpoints.
2. Build the approval-gated action tool (start with invoicing).
3. Stand up a fixed-IP runner and tighten the token's IP whitelist.

## Related pages
- [[mercury]]
- [[wih-app]]
- [[profit-first]]
- [[baselane-to-mercury-migration]]
- [[ai-automation-strategy]]
