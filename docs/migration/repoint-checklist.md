# Repoint Checklist — Migration Inventory

> Phase 0 / Task 3 artifact. Three buckets: who pays IN, who we PUSH to (→ Mercury hub), who PULLS from a card (→ Mercury debit card).
> Built from `account-tree.md`, the Baselane statements, and `wiki/source-baselane-statements.md`.
> **Last built:** 2026-06-03

---

## Bucket A — Payers IN (repoint deposit destination to Mercury)

| Source | What | Lands today in | Cutover action |
|---|---|---|---|
| HAOL HCV (Housing Authority of Lubbock, Section 8) | ~$970/mo (1312) + any other Sec 8 units | Property-bank accounts | Give housing authority the new Mercury account/routing # |
| DoorLoop tenant deposits | Tenant-paid rent | (via DoorLoop → bank) | Repoint DoorLoop deposit account → Mercury per property |
| Stripe | ~$4,350/mo payment processing (3423 E Baylor merchant) | WWH Main | Update Stripe payout account → Mercury |
| Ally Bank P2P (Joshua personal) | ~$3,500/mo | WWH Main | Repoint to Mercury main |
| W&M series transfers (1926, 2102, 3423, 4019) | Rent collections funneled to main | WWH Main | Recreate as internal Mercury transfers |
| TRUE ASSET PROPE ACH | $500 (Mar 2026) | WWH Main | Confirm what this is; repoint |

## Bucket B — Push-payees (→ Mercury disbursement HUB + recipient allowlist)

These are money WE actively send out. Each becomes a hub recipient; AI pushes via the payment API, dry-run-gated.

**Debt (CRITICAL — must not miss a payment):**
| Payee | Amount/mo | Property | Memo string |
|---|---|---|---|
| Dillon Ford | $2,310.94 | 1312 65th Dr | "1312 65th Dr — Dillon Ford seller finance" |
| Mr. Cooper (NSM DBA) | $1,537.60 | 2802 S Channing St | "2802 S Channing — Mr Cooper mtg #7609254" |
| M&T Mortgage | $997.42 | 3904 Ave R | "3904 Ave R — M&T mtg #0093797744" |

**Vendors / draws / one-off (set up as needed):**
| Payee | What | Notes |
|---|---|---|
| Shelby McDonald | Contractor labor draws | Per-project; ~$18k/house phased |
| 33 Carpentry & Construction | Contractor | Per-project |
| Hub City Title | Closing wires (e.g. $32,709.28 Mar 2026) | Per-deal, large wires |
| Integrity Homes LLC | Assignment fees ($1,000) | Per-deal |
| Smart Texan Logical Layouts | Contractor/service ($4,860.84) | Per-deal |
| Lubbock Central Appraisal | Property taxes ($3,688.12; $1,625.06) | Periodic |
| De Leon Law PLLC | Legal ($977.50) | Periodic |
| Texas Secretary of State | Entity filings ($300) | Periodic |

## Bucket C — Pull-merchants (→ Mercury debit CARD on file; NOT the hub)

These charge a card; they don't need a hub recipient. Just put the Mercury card on file for each.

| Merchant | ~Monthly | | Merchant | ~Monthly |
|---|---|---|---|---|
| GoHighLevel (base) | $25 | | OpenAI/ChatGPT | $5–$21 |
| GoHighLevel Agency Sub | $103.40 | | xAI (Grok) | $55 |
| Zapier | $31.97 | | PropStream/BatchLeads | $41.57 |
| **Sequence.io** | $90.92 | | Skool/Whop/7-Fig coaching | $51–$197 |
| Twilio | $10–$27 | | Anthropic Claude Team | $133.25 |
| Lovable | $31.98 | | Wispr | $30 |
| DoorLoop | $143–$239 | | Notion | $51.17 |
| iSpeedToLead | $1,798 | | Hostinger | $26.10 |
| GoDaddy | $24–$99 | | Railway | $20 |
| Baselane | $25 | | Google One / Amazon / Apple | misc |

> **Note:** Sequence.io ($90.92/mo) is in this list only until Task 19 cancels it. DoorLoop and Baselane stay (DoorLoop = rent rail; Baselane = read-only books).

## Full portfolio debt/servicing reconciliation (2026-06-03 ingest)

The daily ingest surfaced debt + servicing relationships beyond the Baselane/Sequence statements. Confidence varies — items marked ⚠️ need verification (amount or current servicer) before cutover.

### Notes WE PAY → these become Mercury hub outbound (push) items
| Property | Paid to | Amount/mo | Currently via | Confidence |
|---|---|---|---|---|
| 1312 65th Dr | Dillon Ford (seller finance) | $2,310.94 | Baselane/Sequence | Confirmed |
| 2802 S Channing | underlying mortgage, **Rocket Mortgage** (formerly Mr. Cooper #7609254 — loan was sold, same debt) | $1,537.60 | Baselane | Confirmed |
| 3904 Ave R | M&T Mortgage | $997.42 | Baselane/Sequence | Confirmed |
| 7005 Winston Ave | (mortgagee TBD) ⚠️ | ~interest-only, amt TBD | TBD — confirm how paid | Low |
| 3423 E Baylor | (mortgagee TBD) ⚠️ | TBD ($7,110.81 principal in 2025) | TBD | Low |
| 4626 S Lipscomb / 4618 45th / 5427 35th | (mortgagees TBD) ⚠️ | TBD | TBD — confirm how paid | Low |
| 2102 68th St | Kiavi Funding (hard money) | $181,600 note; $38,200 rehab holdback | TBD | Confirm if still active |

> **Dig result (2026-06-03, conclusive within available statements):** a full grep of every Baselane statement for mortgage/servicer terms returns **only the three confirmed payments** (1312 Dillon Ford, 2802 Rocket/Mr.Cooper, 3904 M&T). 7005 Winston, 3423 E Baylor, 4626 Lipscomb, 4618 45th, 5427 35th show **no mortgage-servicer activity in Baselane at all** — their debt (if any is currently being paid) is paid from **outside Baselane**. So the Baselane→Mercury *money-routing* scope is exactly these 3 outbound payments + the internal Profit First splits. Anything paid elsewhere is either out of this migration's scope or needs its source account identified to fold in.

### Notes WE RECEIVE → inflows; repoint the deposit, NOT a hub recipient
| Property | Buyer pays | Serviced by (OUTSIDE Baselane/Sequence) | Migration action |
|---|---|---|---|
| 4438 Puffer St | seller-finance buyer | **One-Point Lending** (also: only property NOT on DoorLoop) | Repoint remittance deposit → Mercury |
| 526 53rd St | Sharonda Fanell Lee ($911/mo P&I) | **Escrow Services, Inc.** (wrap; pays underlying Happy State Bank) | Repoint remittance deposit → Mercury |
| 4019 37th St | Joseph (~$1,813/mo escrowed) | **Secured Sequence** escrow (≠ getsequence.io) | Repoint remittance deposit → Mercury |
| 4513 48th St | Joseph ($1,813/mo escrowed) | **Secured Sequence** escrow | Repoint remittance deposit → Mercury |
| 2802 S Channing | seller-finance buyer ($2,103.83/mo, incl. escrow shortage we're covering) | collected to our account (wrap over the Rocket underlying) | Repoint deposit → Mercury |

> **2802 is a wrap (both columns):** buyer pays us $2,103.83 → we pay the $1,537.60 underlying to Rocket. Net positive spread; the escrow shortage is the gap we're temporarily absorbing.

> **Key distinction:** third-party servicers (One-Point, Escrow Services, Secured Sequence) collect from the buyer and remit to us. For the migration they're just **payers-in** (Bucket A) — give them the new Mercury deposit account. They do NOT need to be hub recipients and their internal servicing does not migrate.

## Open items for Joshua (verification)
1. **2802 S Channing** — Mr. Cooper ($1,537.60) vs Rocket Mortgage ($2,103.83): which is the current servicer + amount?
2. **How are the "we pay" mortgages currently paid** for 7005 Winston, 3423 E Baylor, 4626 Lipscomb, 4618 45th, 5427 35th — autopay/ACH pull, manual, or a Sequence rule that didn't fire in captured months? Each needs a payee + amount before cutover.
3. **Is the Kiavi note on 2102 still active**, and is there a monthly payment to route?
4. **ACH details** (account + routing) for every "we pay" recipient — needed to set up Mercury hub recipients (Task 9).
