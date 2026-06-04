---
name: rent-to-own
type: concept
tags: [creative-financing, exit-strategy, r2oc]
sources: [CLAUDE.md seed, faq-rent-to-own.md, rent-to-own-and-seller-finance-faq.md, tenant-financing-disclosure.md, u-r2o-move-in-disclosure.md, doc-2026-06-04-r2oc-program-knowledge-base.md]
updated: 2026-06-04
---

# Rent-to-Own

**Summary**: Primary exit strategy for WIH properties. Tenant-buyer pays an option fee (deposit) that locks the price and is credited at purchase; monthly rent is NOT credited. Marketed through [[r2oc]].

**Sources**: CLAUDE.md seed; faq-rent-to-own.md; rent-to-own-and-seller-finance-faq.md; tenant-financing-disclosure.md; u-r2o-move-in-disclosure.md

**Last updated**: 2026-05-29

---

The dominant exit strategy in the [[wih]] portfolio. A lease that grants the tenant-buyer an **option to buy** at a locked-in price; the buyer holds **equitable interest** while title stays with the seller. Part of the broader [[creative-financing]] toolkit alongside [[subject-to]] and [[seller-finance]]. [[r2oc]] is the marketing brand.

## Program terms (R2OC)
- Initial deposit formula-based (see Underwriting SOP below) — credited toward purchase price; non-refundable.
- 3-year terms; purchase price locked at signing; monthly payments mirror a future mortgage (incl. taxes/insurance escrow) but are **not** applied to price (source: faq-rent-to-own.md).
- **Qualification: credit ~520+ (internal floor, not disclosed externally)**, income 3× monthly payment, basic background check, As-Is acceptance required. No foreclosure (5 yr), no bankruptcy (2 yr), no evictions/judgments. Credit floor is flexible — exceptions made when income is significantly strong (e.g., 500 credit score + $30K/mo income would likely qualify). Never disclose the 520 threshold to applicants. (source: faq-rent-to-own.md, confirmed Joshua June 2026)
- All properties sold/rented **strictly AS-IS** — all repairs (plumbing, HVAC, roof, appliances, cosmetic) are tenant/buyer's responsibility from move-in. The repair reserve in the deposit is WIH's protection, not a fund the buyer draws from.
- Tenant-buyer responsible for repairs/upkeep like an owner; cosmetic changes OK, structural needs written approval; renters insurance required (source: rent-to-own-and-seller-finance-faq.md).
- Conversion to [[seller-finance]] available after month 12 with 80%+ on-time payments — via **Secondary Deposit** (see below).
- Disclosures: tenant financing disclosure and R2O move-in disclosure govern the arrangement (source: tenant-financing-disclosure.md, u-r2o-move-in-disclosure.md). See [[source-rto-disclosures]].

## Secondary Deposit — RTO to Seller Finance Conversion
Paid when an RTO tenant converts to ownership. Separate from and paid after the initial deposit. (source: doc-2026-06-04-r2oc-program-knowledge-base.md)

**Formula:**
- Base Fee = Monthly Payment × 0.85
- Secondary Deposit = Base Fee + (Risk % × Home Price) + $1,000 closing costs

**Eligibility & Risk % by period:**
| Period | Late Payments | Risk % | Notes |
|---|---|---|---|
| 0–12 months | any | — | Not eligible |
| 13–24 months | 0 | 1.5% | |
| 13–24 months | 1–2 | 2.0% | |
| 13–24 months | 3–4 | 2.5% | |
| 13–24 months | 5+ | — | Not eligible |
| 25–36 months | 0–3 | 0% | **$0 deposit — best case** |
| 25–36 months | 4 | 1.5% | |
| 25–36 months | 5–7 | 2.5% | |
| 25–36 months | 8+ | — | Not eligible |
| 36+ months | — | — | Reevaluated; restarts at 13–24 tier |

Must maintain 80%+ on-time payment percentage at all times.

**Stacked total vs. going direct SF** (example: $140K home, $1,400/mo, 2 lates, converts month 18):
- Initial RTO Deposit: $5,770 + Secondary Deposit: $4,990 = **$10,760 total**
- Direct SF on Day 1: $13,540 — **saves $2,780 via RTO path**
- Best case (25–36 months, ≤3 lates): Secondary = $0, total cost = initial deposit only

## After move-in lifecycle
- Months 0–12: Build payment history. Lates count against future conversion eligibility.
- Months 13–24: First conversion window opens.
- Months 25–36: Best window — possibly $0 Secondary Deposit.
- After 36 months: Property reevaluated; eligibility tiers restart.

Application flow: prequalify → apply ($49.90 fee) at rent2owncribs.com (source: faq-rent-to-own.md).

## Underwriting / cash-flow SOP
How deals are priced and cash-flowed (from Josh's training of [[antonio]], see [[source-underwriting-antonio]]):
- **Sell price** = 110% of ARV, rounded DOWN to the nearest $10,000 (e.g., $251,900 → $250,000). Manual adjustment allowed to improve marketing attractiveness.
- **Interest rate by ARV band, not credit**: $120–150k → 9.5%; $151–210k → 9.0%; $211k+ → 8.5%. Start low, raise slowly as the portfolio grows.
- **Monthly payment = PITI** (P&I at sell price, 30yr; + taxes + insurance). Round DOWN to nearest $5 (ones digit 0–4 → 0; ones digit 5–9 → 5). Manual adjustment allowed.
  - **Taxes**: Pull the exact annual tax bill from [Lubbock Central Appraisal District](https://lubbockcad.org) — search by address, get dollars and cents, divide by 12. Never estimate. An n8n workflow exists to automate this lookup (future automation).
  - **Insurance**: Use Joshua's estimate until actual policy is in hand (currently ~$350/mo).
- **Income qualifier**: 3× monthly payment.
- **RTO deposit formula** (from calculator, June 2026):
  - Approx Mortgage = Monthly Payment × 0.85
  - Deposit = (3 × Approx Mortgage) + $1,500 + (Sell Price × 0.005)
  - Round DOWN: below $10k → nearest $100; above $10k → nearest $1,000. Manual adjustment allowed.
- **Seller finance down payment formula**:
  - Approx Mortgage = Monthly Payment × 0.85
  - Down = (6 × Approx Mortgage) + $3,500 + $1,500 + (Sell Price × 0.01)
  - Same rounding rules as RTO deposit. Manual adjustment allowed.
- **PM fee 2.5%** of selling rent; **target net margin = 20%** of selling rent (selling rent − PM fee − actual mortgage PITI) (source: clip-2026-06-03-pre-foreclosure-underwriting-with-antonio-and-josh-2026-05-0.md).

## Related pages
- [[wih]]
- [[r2oc]]
- [[creative-financing]]
- [[seller-finance]]
- [[subject-to]]
- [[pace-morby]]
- [[source-rto-disclosures]]
