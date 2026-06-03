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

## Open items pulled from Task 1 gaps
- Confirm rent-collection + any debt for: 3423 E Baylor, 4626 S Lipscomb, 4618 45th, 5427 35th, 1926 27th, 4302 E 61st (no dedicated property-bank account found).
- Confirm whether 2102 / 3602 / 4019 have debt payments not active in the captured months.
- Identify any debt payees beyond the three above before cutover (Task 2 Sequence export will surface them).
