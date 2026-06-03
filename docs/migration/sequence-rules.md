# Sequence Ruleset — Reconstructed from Statements

> Phase 0 / Task 2 artifact. **Reconstructed from the actual "Webber Wealth Ho Sequence" transactions in the Baselane statements** (Jan/Feb property accounts + May main account), NOT from a live getsequence.io config export. Sequence has no API, but every move it makes is logged in the bank statements — so the *effective* ruleset is fully recoverable.
> **Last built:** 2026-06-03 · **Confidence:** High for the three debt-funding cycles; see "What only the live config adds" for the residual.

---

## How Sequence operates (the pattern)

Each property's debt obligation has its own Baselane account. Sequence (1) **accumulates** funds into that account — partly from the property's own Section 8 deposit, partly topped up from the WWH **main** account — until it equals the exact payment, then (2) **pushes the payment out** to the lender, returning the account to ~$0. It also runs small internal **reserve sweeps**.

## Effective rules — external debt payments (the must-replicate ones)

| Rule | Property | Payee (external) | Amount | Pay day | Funding |
|---|---|---|---|---|---|
| SF-1312 | 1312 65th Dr | **Dillon Ford** (seller finance) | $2,310.94/mo | ~8th | $970 Section 8 (HAOL HCV) + ~$1,340.94 top-up from main |
| MTG-2802 | 2802 S Channing | **Mr. Cooper** (NSM DBA, #7609254) | $1,537.60/mo | ~12th | Full amount swept from main |
| MTG-3904 | 3904 Ave R | **M&T Mortgage** (#0093797744) | $997.42/mo | ~28th | Full amount swept from main |

**Evidence (transaction trail):**
- **1312 — Jan:** Jan 05 +$370.94, Jan 07 +$970.00 → balance $2,310.94; **Jan 08 −$2,310.94 (pays Dillon Ford)**; Jan 09 +$50, Jan 29 +$345 (reserve). **Feb:** Feb 02 +$970 HAOL HCV, Feb 06 +$1,209.68 → $2,310.94; **Feb 08 −$2,310.94**; Feb 09 +$882 (next cycle).
- **2802 — Jan:** Jan 12 +$1,537.60 → pays Mr. Cooper.
- **3904 — Jan:** Jan 28 +$997.42 → pays M&T.
- **Main (May):** outbound Sequence transfers of $200, $96.55, $2.31, $200, $79.80, $116.20, $200 — incremental top-ups feeding the above + reserves (confirms no additional payees).

## Internal reserve rules (lower priority to replicate)

- Small sweeps into property accounts beyond the debt amount (e.g. 1312's $50 + $345 in Jan) — reserve/escrow building. These map to plain Mercury internal auto-transfer rules; exact %/amounts to confirm.

## What only the live getsequence.io config adds

The statement reconstruction gives the *effective* behavior. A live config export (or a quick login confirm) would only add:
1. **Recipient ACH details** — the bank account/routing numbers Sequence uses to pay Dillon Ford, Mr. Cooper, M&T. **These are needed to set up the Mercury hub recipients (Task 9)** and are the one genuinely Joshua-supplied item (sensitive; not in statements).
2. **Any configured-but-dormant rule** that didn't fire in the captured months (e.g. a property whose tenant was vacant).
3. The exact **fixed-vs-percentage** logic and trigger timing, vs. my inference from amounts/dates.

## Scope correction (2026-06-03 portfolio reconciliation)

The three debt payees above are the complete set **routed through Baselane/Sequence in the captured months** — but the wider portfolio carries more debt and uses other servicers. Do **not** read this as the full migration scope. See `repoint-checklist.md` → "Full portfolio debt/servicing reconciliation" for the complete picture. In short:

- **More notes we PAY** (not seen as Sequence lines in the captured months — confirm how each is paid today): 7005 Winston Ave, 3423 E Baylor, 4626 Lipscomb, 4618 45th, 5427 35th, plus Kiavi hard money on 2102 68th St.
- **Notes we RECEIVE, serviced OUTSIDE Baselane/Sequence** (these are inflows — repoint the deposit, not the hub): One-Point Lending (4438 Puffer), Escrow Services Inc (526 53rd wrap), Secured Sequence escrow (4019, 4513).
- **Verify:** 2802 S Channing — statements show $1,537.60 to Mr. Cooper (#7609254); wiki says Rocket Mortgage services it at $2,103.83. Confirm current servicer + amount before cutover.
