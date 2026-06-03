---
name: baselane-to-mercury-migration
type: project
tags: [finance, banking, mercury, baselane, automation, ai]
status: active
sources: [memo-2026-06-03-mercury-migration-and-vision.md]
updated: 2026-06-03
---

# Baselane → Mercury Migration

**Summary**: Move banking and money-routing off [[baselane]] (Thread Bank) + [[sequence]] onto [[mercury]], with [[doorloop]] as the rent rail, so AI can own the money layer via Mercury's API/MCP. Funds do not move until fully vetted.

**Sources**: session 2026-06-03

**Last updated**: 2026-06-03

---

Full design and phased plan: `docs/superpowers/specs/2026-06-03-baselane-to-mercury-migration-design.md`.

**Why:** [[baselane]] has no usable API, so AI can never control the money layer. [[sequence]] ($90.92/mo) is a serviceable but separate routing bandaid that **actively pushes external payments** (e.g. the Dillon Ford seller-finance payment). [[mercury]] replaces it in two layers: (1) native auto-transfer rules for the internal Profit First splits, and (2) the AI layer driving Mercury's **payment API** for outbound payments — centralized through a single **disbursement hub** account that holds the recipients and the write key. The full Banking API + MCP is the whole point: AI becomes the money-mover, with dry-run gating, recipient allowlist, Mostafa-gated outbound, and a kill switch.

**Confirmed scope:** rent already flows through [[doorloop]] (so the no-tenant-portal gap is already solved); end state switches banking fully to Mercury but keeps Baselane as a read-only bookkeeping layer; no funds move until vetted.

**Phases:** 0 Inventory → 1 Build Mercury shell → 2 Vet (sandbox + one live property) → 3 Cutover (Dillon Ford seller-finance first, never miss a payment) → 4 Decommission Sequence + stand up the AI money-ops layer.

**Committed future phase (much later):** an in-house management app that replaces [[doorloop]] entirely — tenant portals, in-house seller-finance note servicing, in-house rent-to-own payment servicing — to kill per-user + servicing + setup fees. Rolls up to [[company-roadmap]].

## Related pages
- [[mercury]]
- [[baselane]]
- [[sequence]]
- [[doorloop]]
- [[profit-first]]
- [[wih-app]]
- [[company-roadmap]]
- [[ai-operating-system]]
