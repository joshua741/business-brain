# Phase 1 Execution Guide — Mercury Account & Rule Setup

> Your hands-on checklist for setting up Mercury. Follow top-to-bottom. Reference `docs/migration/mercury-account-map.md` for the target structure.
> **Prerequisite:** You have the Mercury production token in `Business_Brain/.env` and read-only access is verified.

---

## Before You Start

Confirm you have:
- [ ] The **3 Mercury structural answers** (partner bank pinning, recipient scope, token scoping) from email or notes
- [ ] **WIH Profit First percentages** (taxes / profit / owner pay / opex) — these finalize the rule spec
- [ ] ACH details (account + routing #s) for the 3 hub recipients (Dillon Ford, Rocket #7609254, M&T #0093797744)

If any are missing, hold off. The percentages especially are load-bearing — they're not guesses.

---

## Phase 1a — Verify Partner Bank Pinning

Before creating accounts, confirm Mercury's structure with the answers above.

1. **Log into Mercury** (mercury.com)
2. **Check Settings → API & Integrations** — this is where the read-only token lives
3. **Ask yourself:** can you create accounts on a *single* partner bank, or are they spread across partner banks?
   - If spread: this changes the rule strategy (some routing won't work via native auto-transfer)
   - Confirm the answer to Question 1 before proceeding

---

## Phase 1b — Create the Account Structure

Reference: `mercury-account-map.md` "Target accounts to create" section.

**Existing accounts (rename or reuse):**
- [ ] `Mercury Checking ••3039` → rename to `WWH — Main / Operating` (or leave as-is, maps to Main)
- [ ] `Mercury Savings ••2610` → rename to `WWH — Profit` (or leave, maps to Profit reserve)

**Create new accounts (all checking, all on the confirmed partner bank):**
- [ ] `WWH — Disbursement Hub` — this holds the payment key + all external recipients
- [ ] `WWH — Taxes` (savings)
- [ ] `WWH — Owner Pay` (savings)
- [ ] **Per-property operating (create at least the 3 debt-bearing ones first):**
  - [ ] `1312 65th Dr — Operating`
  - [ ] `2802 S Channing — Operating`
  - [ ] `3904 Ave R — Operating`
  - *(defer others until properties activate)*

**Naming convention:** Keep the names exactly as above so the rule spec matches.

---

## Phase 1c — Set Up Internal Auto-Transfer Rules

These split incoming rent/deposits across the Profit First accounts. **Mercury requires one rule per destination or a multi-destination rule on the source.**

### Rule 1: Main account → Taxes
| Field | Value |
|---|---|
| From | `WWH — Main / Operating` |
| To | `WWH — Taxes` |
| Type | Percentage |
| Amount | **[INSERT WIH TAX %]** |
| Trigger | By transaction (when money lands) |

### Rule 2: Main account → Profit
| Field | Value |
|---|---|
| From | `WWH — Main / Operating` |
| To | `WWH — Profit` |
| Type | Percentage |
| Amount | **[INSERT WIH PROFIT %]** |
| Trigger | By transaction |

### Rule 3: Main account → Owner Pay
| Field | Value |
|---|---|
| From | `WWH — Main / Operating` |
| To | `WWH — Owner Pay` |
| Type | Percentage |
| Amount | **[INSERT WIH OWNER PAY %]** |
| Trigger | By transaction |

### Rules 4–6: Property sweeps to hub (the debt-funding layer)
For each property with a debt obligation, a sweep-to-hub rule funds the hub, which then pays the external lender.

#### Rule 4: 1312 → Hub
| Field | Value |
|---|---|
| From | `1312 65th Dr — Operating` |
| To | `WWH — Disbursement Hub` |
| Type | Fixed |
| Amount | $2,310.94 |
| Trigger | By transaction (or ~7th of month) |

#### Rule 5: 2802 → Hub
| Field | Value |
|---|---|
| From | `2802 S Channing — Operating` |
| To | `WWH — Disbursement Hub` |
| Type | Fixed |
| Amount | $1,537.60 |
| Trigger | By transaction (or ~11th of month) |

#### Rule 6: 3904 → Hub
| Field | Value |
|---|---|
| From | `3904 Ave R — Operating` |
| To | `WWH — Disbursement Hub` |
| Type | Fixed |
| Amount | $997.42 |
| Trigger | By transaction (or ~27th of month) |

**Note:** The trigger timing is a best-guess from Sequence history. You can adjust based on when rent actually arrives; Mercury will trigger by-transaction if deposits hit, or on a fixed schedule if you prefer.

---

## Phase 1d — Set Up Hub Recipients (Allowlist)

The disbursement hub pays out to the 3 debt obligations. Add each as a pre-approved recipient so the payment API won't reject them.

**Recipient 1: Dillon Ford**
| Field | Value |
|---|---|
| Name | Dillon Ford |
| Type | ACH Transfer |
| Account Number | **[INSERT from ACH details]** |
| Routing Number | **[INSERT from ACH details]** |

**Recipient 2: Rocket Mortgage (loan #7609254)**
| Field | Value |
|---|---|
| Name | Rocket Mortgage #7609254 |
| Type | ACH Transfer |
| Account Number | **[INSERT from ACH details]** |
| Routing Number | **[INSERT from ACH details]** |

**Recipient 3: M&T Mortgage (loan #0093797744)**
| Field | Value |
|---|---|
| Name | M&T Mortgage #0093797744 |
| Type | ACH Transfer |
| Account Number | **[INSERT from ACH details]** |
| Routing Number | **[INSERT from ACH details]** |

---

## Phase 1e — Verify & Test Rules in Mercury UI

Before Phase 2, confirm everything is wired:

1. **Simulate a deposit** to the main account (even $1) and verify the % splits fire correctly to taxes/profit/owner-pay.
2. **Simulate a deposit** to 1312-operating and verify the sweep to the hub fires for $2,310.94.
3. **Check the hub balance** — it should have accumulated $2,310.94 (if you only tested 1312).
4. **Do NOT send real payments yet** — that's Phase 2 vetting.

---

## Phase 1f — Generate API Tokens

Once the account structure and rules are locked:

1. **Generate a NEW read-only token** for the standing monitoring connection (or update `.env` to use the existing one).
2. **DO NOT generate a write/payment token yet.** The payment token comes later in Phase 2, with IP allowlisting, once we've proven the rules work in sandbox.

---

## Phase 1 Complete

At this point:
- ✅ All accounts created and renamed
- ✅ All rules configured (6 total: 3 PF splits + 3 sweeps)
- ✅ All 3 hub recipients added to the allowlist
- ✅ Verified rules fire correctly in Mercury UI

**Next: Phase 2 vetting** — sandbox dry-run + one live property test. The reconciliation script (`scripts/migration/reconcile.py`) is your gate.

---

## Placeholders (fill in from external context)

- **[INSERT WIH TAX %]** — e.g., 15 (percentage)
- **[INSERT WIH PROFIT %]** — e.g., 5 (percentage)
- **[INSERT WIH OWNER PAY %]** — e.g., 20 (percentage)
- **[INSERT ACH details]** — account + routing numbers for Dillon Ford, Rocket, M&T
