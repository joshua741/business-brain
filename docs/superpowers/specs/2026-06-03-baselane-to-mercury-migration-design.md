# Baselane → Mercury Migration — Design Spec

**Date:** 2026-06-03
**Owner:** Joshua Webber
**Status:** Approved (architecture + phasing), pending spec review
**Related:** `company-roadmap.md`, `mercury.md`, `baselane.md`, `doorloop.md`, `profit-first.md`

---

## Problem

Baselane is doing two jobs: (1) it's the **bank** (Thread Bank accounts holding a Profit First per-property sub-account structure — WWH main account ending 4927, plus per-property "bank," "taxes," and "rehab funds" accounts, plus W&M series marketing accounts), and (2) it's a **landlord platform** (rent collection, tenant portal, bookkeeping).

[[Sequence]] (getsequence.io, $90.92/mo) is the **money-routing layer** sitting on top of Baselane. It runs the rules — when rent/Section 8 lands, it splits the money, funds each property's mortgage account, and sweeps the rest. The "Webber Wealth Ho Sequence" lines across the statements are these automated transfers (e.g. 1312 65th Dr → $2,310.94/mo seller-finance payment to Dillon Ford).

**Core problem:** Baselane has no usable API, so AI can never own the money layer. Sequence is a serviceable bandaid (visual, editable, cheap) but it's a separate dependency and still not AI-controllable. The strategic goal is AI control of the money layer — Baselane structurally cannot deliver it.

## Decision

Migrate banking + money-routing to **Mercury**, with **DoorLoop** as the rent-collection rail. Mercury replaces *both* Baselane-the-bank and Sequence:

- **Banking:** unlimited free checking/savings sub-accounts → recreate the per-property structure.
- **Routing (replaces Sequence):** native percentage-based auto-transfer rules, up to 20 accounts per rule, run by-transaction / daily / twice-monthly. Profit First is an advertised use case.
- **AI control (the whole point):** full Banking API + official MCP server — query balances, pull transactions, trigger ACH/wires programmatically and in natural language.

**Rejected alternatives:** (a) stay on Baselane + Sequence — fails the core goal, no API; (b) Relay Financial — has Profit First auto-rules but weaker API / no AI-MCP story, and banking already exists at Mercury.

## Confirmed constraints (from Joshua, 2026-06-03)

- **Rent already flows through DoorLoop**, which deposits to the bank. So the one functional gap (Mercury has no tenant rent portal) is already solved — DoorLoop just repoints its deposit account.
- **Rent-to-own payments also flow through DoorLoop today** (confirmed 2026-06-03). **Decision: DoorLoop stays the collection rail for all tenant + RTO payments through this migration** — change only the deposit destination, not the collection method. Rationale: a banking migration should change one variable at a time. Bringing RTO payment collection in-house is the separate, later DoorLoop-replacement phase, not this one.
- **End state:** switch banking fully to Mercury, but **keep Baselane as a read-only bookkeeping layer** (link Mercury as an external account for Schedule E / P&L). Sequence is retired.
- **No funds move until fully vetted.** Build and validate everything first; the actual fund cutover is a late, gated step.

## Target architecture

```
DoorLoop ──rent──►  Mercury per-property sub-accounts ──native % rules──►  taxes / profit / operating
(tenant portal,     (collection + internal allocation)                          │ amounts owed externally
 PM system)                                                                     ▼
                                                          ┌──────────────────────────────────┐
                                                          │   DISBURSEMENT HUB (one account)   │
                                                          │   holds the payment connection +   │
                                                          │   all external recipients          │
                                                          └──────────────────────────────────┘
                                                                            │ Mercury payment API
                                                          AI layer ─────────┤ (dry-run → allowlist →
                                                          (Claude/MCP)       │  Mostafa-gated → send)
                                                                            ▼
                                                          Dillon Ford (seller-finance), vendors, draws

Baselane = read-only bookkeeping (Mercury linked as external account)
Sequence = deleted (saves $90.92/mo ≈ $1,091/yr)
```

Two layers: (1) **internal allocation** via boring, always-on Mercury auto-transfer rules (the Profit First splits — no AI), and (2) **external disbursement** via a single hub account that AI drives through Mercury's payment API. Per-property attribution is preserved with payment memos so the books stay clean.

## Money-movement layer (the real Sequence replacement)

Confirmed with Joshua (2026-06-03): **Sequence actively pushes external payments** today — any account connected to it can send to third parties (e.g. the Dillon Ford seller-finance payment). The only manual friction is setting up a *new* account/recipient. So replacing Sequence is not just "recreate the internal rules" — it requires a programmatic outbound-payment capability. That capability is the AI layer driving Mercury's payment API, and it is **core to the migration, built and vetted before cutover** — not a later autonomy add-on.

**Hub-and-spoke, optimized per Joshua's guidance — centralize outbound through one dedicated account:**
- Internal Profit First splits run between same-partner-bank sub-accounts via native auto-transfer rules.
- The portion that must leave sweeps into a **single disbursement hub account**. All external recipients are set up once on this hub.
- AI initiates external payments from the hub via the Mercury payment API. Memos carry per-property attribution so Baselane's books/Schedule E stay accurate.

**Guardrails (designed up front — the "scope the key, not the rule" lesson from `ai-operating-system.md`):**
- **Recipient allowlist** — Mercury only pays pre-approved recipients (a feature, not a limitation). Adding a payee is the one deliberate manual step.
- **Scoped, IP-whitelisted write token** held only for the hub account; read-only everywhere else.
- **Mandatory dry-run** before any live send — compute and show the payment set, require confirmation, then execute (per `masking-and-dryrun-gotchas` discipline: the dry-run must actually gate the write).
- **Outbound stays Mostafa-gated** per the standing SOP until autonomy is explicitly earned.
- **Documented kill switch** — how to revoke the write token instantly.

## Migration phases — funds do not move until Phase 3, gated on Phase 2 passing

**Phase 0 — Inventory (zero money moves).**
- Export every Sequence workflow: trigger, %/fixed amount, source, destination.
- Map the full Baselane account tree: every account, balance, purpose, what hits it.
- Build the repoint checklist: who pays *in* (housing authorities/HAOL HCV, DoorLoop deposits, Stripe) and who gets paid *out* (Dillon Ford seller-finance, Kiavi draws, vendors, recurring SaaS).
- Export all Baselane bookkeeping history before anything changes.

**Phase 1 — Build the Mercury shell + payment layer (zero money moves).**
- Recreate the per-property sub-account structure in Mercury, **all under one partner bank** (auto-transfer rules only work between same-partner-bank accounts), plus the **single disbursement hub** account.
- Rebuild every Sequence *internal* rule as a Mercury auto-transfer rule. Keep operating cash in checking, not Treasury (Treasury auto-transfers are capped at 2/mo, ≥7 days apart).
- Set up the **external recipients** (Dillon Ford, vendors, draws) on the hub account's allowlist.
- Set up API tokens (read-only everywhere first; a scoped, IP-whitelisted read/write token bound to the hub for payments) and connect the MCP server to the AI layer.
- Build the **dry-run-gated payment send path** so AI can propose external payments without sending.

**Phase 2 — Vet, internal AND outbound (still no real migration).**
- Run a full month's flows through Mercury's **sandbox**; confirm the internal rules produce the *exact* same splits Sequence does today.
- Validate the **payment path in sandbox**: the dry-run produces the correct recipient + amount set, and the gate genuinely blocks a send until confirmed.
- Then a **live end-to-end test on a single low-risk property**: DoorLoop deposit → internal rule fires → funds reach the hub → AI executes one real external payment for that property and it posts correctly. This proves both layers before trusting them broadly (Joshua's standard live-test gate).

**Phase 3 — Cutover (the actual switch, only after Phase 2 passes).**
- Repoint DoorLoop deposits and Section 8 ACH to Mercury, property by property.
- Move external payments onto the hub — **Dillon Ford first**; never miss a seller-finance payment. Cut over immediately after a month's payment clears, with a manual backup payment ready.
- Drain Baselane balances to Mercury.

**Phase 4 — Decommission + escalate AI autonomy.**
- Cancel Sequence.
- Link Mercury into Baselane as an external account for books only.
- The payment capability already exists from Phase 1–2; Phase 4 escalates *how much* runs unattended via the Bike Method (read-only monitoring → AI-proposes/human-approves → AI-initiated within hard caps → bounded autonomy), keeping outbound Mostafa-gated and the kill switch documented (`ai-operating-system.md`).

## Future phase (committed, much later) — In-house management app, replacing DoorLoop

Noted here because Joshua explicitly wants it on the record as part of the ultimate plan. **Only after the Mercury/banking integrations above are fully in place.**

DoorLoop charges per user, and the business bleeds money on third-party **servicing fees and setup costs**. The plan is to bring it all in-house as an owned application (separate management surface, tied into [[wih-app]]):

- **Tenant portals** — login per tenant; balances, payments, autopay, lease/maintenance.
- **In-house seller-finance note servicing** — amortized payment schedules serviced internally (no external servicer).
- **In-house rent-to-own payment collection + servicing** — RTO and rent collection handled together since they're operationally near-identical.
- **One consolidated focal point** for management, integrated with the same banking/AI backbone built above.

This is both a **margin lever** (kill per-user + servicing + setup fees) and a **control lever** (own the rails, let AI run them). It rolls up to the in-house-software thesis and the vertically-integrated mortgage/RTO/seller-finance vision in `company-roadmap.md`.

## Risks / gotchas

- **Payment-key exposure** — a write token *can* send money regardless of instructions. Bind it to the hub account only, IP-whitelist it, require dry-run + confirmation, and keep the kill switch documented. Outbound stays Mostafa-gated until autonomy is earned.
- **Per-property attribution** — centralizing outbound through one hub must not blur which property each payment belongs to; enforce payment memos so Baselane's Schedule E stays correct.
- **Same-partner-bank constraint** on auto-transfer rules — open all sub-accounts under one partner bank.
- **Treasury auto-transfer limits** (2/mo, ≥7 days apart) — keep routing cash in checking.
- **Seller-finance continuity** — Dillon Ford and any other amortized payees must not miss a payment during cutover.
- **DoorLoop deposit re-verification** — micro-deposit / account-link lead time when repointing.
- **Don't lose Baselane history** — full export in Phase 0.

## Cost impact

- Sequence: **$90.92/mo eliminated** (~$1,091/yr).
- Mercury: no monthly fee. Baselane Core: free (kept for books).
- Net: lower cost, one fewer dependency, and AI finally owns the money layer.
