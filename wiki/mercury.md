---
name: mercury
type: entity
tags: [banking, profit-first, finance]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Mercury

**Summary**: Business bank accounts running the Profit First cash management model across all entities.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Mercury holds all business bank accounts for [[wih]] and related entities. Accounts are allocated by percentage following the [[profit-first]] model — profit, owner pay, taxes, and operating expenses each have dedicated accounts. Financial dashboard tracked via [[google-sheets]].

> **Becoming the primary money layer:** Under [[baselane-to-mercury-migration]], Mercury is set to replace both [[baselane]] (banking — unlimited free sub-accounts) and [[sequence]] (routing — native percentage auto-transfer rules, up to 20 accounts). The decisive advantage is Mercury's **full Banking API + MCP server**, which lets the AI layer query balances, pull transactions, and trigger payments programmatically — the thing Baselane structurally can't do. Constraints to mind: auto-transfer rules only work between same-partner-bank accounts; Treasury auto-transfers are capped at 2/mo, ≥7 days apart.

## Related pages
- [[profit-first]]
- [[wih]]
- [[google-sheets]]
- [[baselane]]
- [[sequence]]
- [[baselane-to-mercury-migration]]
- [[doorloop]]
- [[company-roadmap]]
