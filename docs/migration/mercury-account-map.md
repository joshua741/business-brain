# Mercury Account Map — Target Structure + Rules + Recipients

> Phase 1 / Tasks 5–6 artifact. The blueprint for what to create in Mercury, how money routes, and who the hub pays.
> Built from `account-tree.md`, `sequence-rules.md`, `repoint-checklist.md`. **Last built:** 2026-06-03
> 🤖 = Claude-designed (this doc) · 🧍 = Joshua executes in Mercury

---

## Mercury constraints (Task 5 §1 — confirmed from Mercury docs)

- **Sub-accounts:** free / unlimited checking + savings under one login. Nickname each.
- **Auto-transfer rules:** percentage- or amount-based; up to **20 destinations per rule**; run **by-transaction / daily / twice-monthly / monthly**.
- **Same-partner-bank rule:** auto-transfer rules only work between accounts on the **same partner bank**. → Create ALL WIH accounts on one partner bank.
- **Treasury limit:** auto-transfers from a Treasury account are capped at **2/mo, ≥7 days apart** → keep routing cash in **checking**, not Treasury.
- **Payments:** API/UI pays to **pre-approved recipients** (allowlist) — a guardrail, not a limitation.

### Task 5 §2 — to confirm with Mercury (🧍, before Task 7)
1. Can all accounts be pinned to ONE partner bank?
2. Are payment **recipients org-level** (shared) or per-account?
3. Can a **write token be scoped to a single account** (the hub)?
*(Answers decide whether external payments fire from the hub or per-property account — logical model is identical either way.)*

---

## Current Mercury state (live read via API, 2026-06-03)

Verified by read-only `GET /accounts`. **Only 2 accounts exist today** — everything else below is greenfield:
| Existing account | Type | Status | Balance | Maps to target |
|---|---|---|---|---|
| Mercury Checking ••3039 | checking | active | $263.55 | → `WWH — Main / Operating` |
| Mercury Savings ••2610 | savings | active | $0.00 | → `WWH — Profit` (Profit First) |

So Task 7 creates: the **Disbursement Hub**, the per-property operating accounts, and the remaining reserve accounts (Taxes, Owner Pay). Reuse 3039 as Main and 2610 as Profit (or rename them for clarity).

## Target accounts to create (🧍 Task 7)

All under **Webber Wealth Holdings LLC**, one partner bank. Start with the active set; dormant per-property accounts can be added later as those properties activate.

### Core
| Nickname | Type | Mirrors (Baselane) | Purpose |
|---|---|---|---|
| `WWH — Main / Operating` | checking | Main #4927 | Hub of inbound; funds the splits |
| `WWH — Disbursement Hub` | checking | *(new)* | Holds the payment key + all external recipients; AI pays from here |
| `WWH — Taxes` | savings | Taxes 1312/2102 | Profit First tax reserve |
| `WWH — Profit` | savings | *(PF model)* | Profit First profit hold |
| `WWH — Owner Pay` | savings | *(PF model)* | Owner distributions |

### Per-property operating (create for active/debt-bearing first)
| Nickname | Mirrors | Why |
|---|---|---|
| `1312 65th Dr — Operating` | Bank #6030 | Collects rent + Section 8; sweeps Dillon Ford payment to hub |
| `2802 S Channing — Operating` | Bank #6023/0222 | Collects buyer $2,103.83; sweeps $1,537.60 to hub for Rocket |
| `3904 Ave R — Operating` | Bank #5596 | Collects rent; sweeps M&T payment to hub |
| `2102 68th St — Operating` (+ `— Rehab`) | #3944 / #3986 | If Kiavi note still active; rehab holdback |
| *(add 3602, 4019, others as they activate)* | | mirror on demand |

> Dormant Baselane accounts (3602, 4019, extra taxes) can be recreated lazily — no need to pre-build empty accounts.

---

## Routing rules (🧍 Task 8)

### A. Internal Profit First splits (on the Main account)
Percentage auto-transfer rules, by-transaction, Main → reserves.
| From | To | % | Status |
|---|---|---|---|
| WWH Main | WWH Taxes | ⚠️ TBD | **Confirm WIH PF percentages with Joshua** (LBK's are separate) |
| WWH Main | WWH Profit | ⚠️ TBD | " |
| WWH Main | WWH Owner Pay | ⚠️ TBD | " |

### B. Sweep-to-hub rules (fund each debt obligation) — THE 3 that matter
| From (property operating) | To | Amount | Schedule | Then hub pays |
|---|---|---|---|---|
| 1312 65th Dr — Operating | Disbursement Hub | $2,310.94 | by ~7th | Dillon Ford |
| 2802 S Channing — Operating | Disbursement Hub | $1,537.60 | by ~11th | Rocket Mortgage |
| 3904 Ave R — Operating | Disbursement Hub | $997.42 | by ~27th | M&T Mortgage |

*(1312 is partly pre-funded by the $970 Section 8 deposit; the rule tops up the remainder from Main.)*

---

## Hub recipients / allowlist (🧍 Task 9 — needs ACH details from Joshua)
| Recipient | For | Amount/mo | Memo string | ACH details |
|---|---|---|---|---|
| Dillon Ford | 1312 seller finance | $2,310.94 | "1312 65th Dr — Dillon Ford seller finance" | ⚠️ needed |
| Rocket Mortgage (loan #7609254) | 2802 underlying | $1,537.60 | "2802 S Channing — Rocket mtg #7609254" | ⚠️ needed |
| M&T Mortgage (loan #0093797744) | 3904 underlying | $997.42 | "3904 Ave R — M&T mtg #0093797744" | ⚠️ needed |

> Vendors/draws/title (Shelby, Hub City Title, etc.) are added as recipients **on demand**, not pre-loaded. Pull-merchants (SaaS) go on the **Mercury debit card**, never the hub (see `repoint-checklist.md` Bucket C).

---

## Inbound deposit repoints (🧍 Task 16, Phase 3 — listed here for completeness)
DoorLoop deposit account → Mercury per property; Section 8 (HAOL HCV) → new Mercury account/routing #; Stripe payout → Mercury; third-party servicer remittances (One-Point, Escrow Services, Secured Sequence) → new Mercury deposit info.

---

## Open before building
1. **WIH Profit First percentages** for the split rules (Section A) — only thing blocking a complete rule set.
2. Mercury partner-bank / recipient-scope / token-scope answers (Task 5 §2).
3. ACH details for the 3 hub recipients (Task 9).
