# Baselane Account Tree — Migration Inventory

> Phase 0 / Task 1 artifact. Built from all 23 `raw/baselane-*-statement.md` files + `wiki/source-baselane-statements.md`.
> Purpose: map every current Baselane (Thread Bank) account so it can be mirrored in Mercury.
> **Last built:** 2026-06-03

All accounts are at **Thread Bank** (Rogersville, TN). Most per-property and reserve accounts run to $0 each cycle — money lands, Sequence routes it, the account clears. Balances below are the latest observed, not steady-state.

## Accounts (12 found)

| # | Account | Last 4 | Entity | Type | Property | Latest balance | Month | Recurring IN | Recurring OUT |
|---|---|---|---|---|---|---|---|---|
| 1 | WWH Main | 4927 | WWH LLC | main | Operating hub | $18.98 | May 2026 | Ally P2P ~$3,500; Stripe ~$4,350; series transfers $6.7k–$22k | All SaaS; wires; taxes; assignments |
| 2 | Bank — 1312 65th Dr | 6030 | WWH LLC | property-bank | 1312 65th Dr | $0.00 | Feb 2026 | HAOL HCV (Sec 8) $970/mo | **Dillon Ford seller-finance $2,310.94/mo** |
| 3 | Bank — 2802 S Channing | 6023→0222 | WWH LLC | property-bank | 2802 S Channing St | $0.00 | Feb 2026 | Sequence-funded from main | **Mr. Cooper mortgage $1,537.60/mo** (loan #7609254) |
| 4 | Bank — 3904 Ave R | 5596 | WWH LLC | property-bank | 3904 Ave R | $0.00 | Feb 2026 | Sequence-funded from main | **M&T mortgage $997.42/mo** (loan #0093797744) |
| 5 | Bank — 2102 68th St | 3944 | WWH LLC | property-bank | 2102 68th St | $0.00 | Feb 2026 | — (rehab flows via series/main) | — |
| 6 | Bank — 3602 31st St | 6040 | WWH LLC | property-bank | 3602 31st St | $0.00 | Feb 2026 | — (no activity Jan–Feb) | — |
| 7 | Bank — 4019 37th St | 5997 | WWH LLC | property-bank | 4019 37th St | $0.00 | Jan 2026 | — (no activity Jan) | — |
| 8 | Taxes — 1312 65th Dr | 3348 | WWH LLC | taxes | 1312 65th Dr | $0.00 | Jan 2026 | — (dormant) | — |
| 9 | Taxes — 2102 68th St | 3946 | WWH LLC | taxes | 2102 68th St | $0.00 | Jan 2026 | — (dormant) | — |
| 10 | Additional Rehab Funds — 2102 68th St | 3986 | WWH LLC | rehab-funds | 2102 68th St | $0.00 | May 2026 | Kiavi holdback draws (periodic) | — |
| 11 | W&M Series — 1926 27th St (Marketing) | 8983 | W&M Series LLC | series-marketing | 1926 27th St | $453.19 | Dec 2025 | Rent collections | Transfer to main |
| 12 | W&M Series — 2102 68th St (Marketing) | 1480 | W&M Series LLC | series-marketing | 2102 68th St | $455.77 | Dec 2025 | Rent collections | Transfer to main |

## External debt payments (CRITICAL — these are the must-not-miss outbound items)

These are the third-party push payments the Mercury **disbursement hub** must take over. Each maps to a property account today:

| Payee | Amount/mo | Property | Type | Loan # | Source account today |
|---|---|---|---|---|---|
| **Dillon Ford** | $2,310.94 | 1312 65th Dr | Seller-finance deed of trust | — | Bank — 1312 (6030) |
| **Mr. Cooper (NSM DBA)** | $1,537.60 | 2802 S Channing St | Mortgage (likely sub-to) | 7609254 | Bank — 2802 (6023/0222) |
| **M&T Mortgage** | $997.42 | 3904 Ave R | Mortgage (likely sub-to) | 0093797744 | Bank — 3904 (5596) |

## Gaps to confirm with Joshua

These portfolio properties have **no dedicated Baselane property-bank account** found in the 23 statements — confirm how each collects rent and pays any debt before cutover:
- **3423 E Baylor St** (Stripe merchant account is tied here — may collect via Stripe; appears as a W&M series inbound transfer source)
- **4626 S Lipscomb St**
- **4618 45th St**
- **5427 35th St**
- **1926 27th St** (has a W&M *series-marketing* account #8983, but no separate property-bank account)
- **4302 E 61st St** (creative-finance close ~Mar 2026 — newer than most statements)

Also confirm:
- Are there **W&M series accounts** for 3423 E Baylor and 4019 37th St? Both appear as inbound transfer *sources* to the main account but no statement was provided for them.
- Do **2102 / 3602 / 4019** property accounts have debt payments that simply weren't active in the months captured?

## Notes
- "Sequence-funded from main" means the property account is fed by a Sequence transfer immediately before its debt payment clears, then returns to ~$0.
- The seller-finance/mortgage payments above are the **internal vs external** distinction that drives the hub design: rent in → internal split → fund the obligation → **push externally to the lender**.
