---
name: mercury
type: entity
tags: [banking, profit-first, finance, invoicing]
status: active
sources: [CLAUDE.md seed]
updated: 2026-06-03
---

# Mercury

**Summary**: Business bank accounts running the Profit First cash management model across all entities.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-04

---

Mercury holds all business bank accounts for [[wih]] and related entities. Accounts are allocated by percentage following the [[profit-first]] model — profit, owner pay, taxes, and operating expenses each have dedicated accounts. Financial dashboard tracked via [[google-sheets]].

> **Becoming the primary money layer:** Under [[baselane-to-mercury-migration]], Mercury is set to replace both [[baselane]] (banking — unlimited free sub-accounts) and [[sequence]] (routing — native percentage auto-transfer rules, up to 20 accounts). The decisive advantage is Mercury's **full Banking API + MCP server**, which lets the AI layer query balances, pull transactions, and trigger payments programmatically — the thing Baselane structurally can't do. Constraints to mind: auto-transfer rules only work between same-partner-bank accounts; Treasury auto-transfers are capped at 2/mo, ≥7 days apart.

## Current balance snapshot (2026-06-04)
Mercury is in early migration state — only 2 accounts exist today:
- **Checking ••3039:** $263.55 (+ $1,172.98 pending from Tre'sye Rodriguez)
- **Savings ••2610:** $0.00

Recent transactions: -$32.67 Mercury subscription fee (Jun 3), -$296.22 to SEQUENCE (May 28), -$837.48 to LAFAYETTE LIFE (May 8). Lafayette Life is a new payee — not previously in migration docs; likely life insurance premium, possibly [[infinite-banking]] related. Tre'sye Rodriguez incoming payment context unknown — could be rent, RTO, or reimbursement. (Source: [[source-mercury-snapshot-2026-06-04]])

The low balance reflects that the Profit First account buildout under [[baselane-to-mercury-migration]] hasn't yet moved primary cash flows over.

## Invoicing (capability identified 2026-06-03)
Mercury can **create and send invoices natively** — a capability we hadn't logged before. WIH invoices frequently, so this is a real opportunity: consolidate invoicing into Mercury rather than a separate tool, and (via the Banking API) automate invoice creation/tracking from [[wih-app]] — fits the "own the software / one-stop app" direction. Action: evaluate Mercury invoicing vs. the current method and consider wiring it into the in-house app's billing.

## Related pages
- [[profit-first]]
- [[wih]]
- [[google-sheets]]
- [[baselane]]
- [[sequence]]
- [[baselane-to-mercury-migration]]
- [[doorloop]]
- [[company-roadmap]]
