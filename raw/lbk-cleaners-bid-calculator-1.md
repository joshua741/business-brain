# LBK Cleaners Bid Calculator

**Summary**: Commercial cleaning bid calculator for LBK Cleaners with Lubbock, TX market rates pre-loaded — calculates true hourly labor cost, estimates cleaning time by facility type, outputs monthly pricing at multiple margin levels, and includes apartment complex add-ons and a bid history log.

**Sources**: Google Drive — LBK_Cleaners_Bid_Calculator (1) (1CHcla9LY2xdBQaXrL1_dA-NeOV1f9qC8)

**Last updated**: 2026-05-29

---

## Section A — Client & Job Information (Sample)

| Field | Value |
|---|---|
| Client / Company Name | Sunset Ridge Apartments |
| Job Name / Reference | Sunset Ridge Common Areas |
| Facility Type | Apartment Complex (Common Areas) |
| Service Frequency (per week) | 5 |
| Total Cleanable Sq Ft | 8,000 |
| Number of Floors | 2 |
| Day or Night Service | Night |

---

## Section B — True Hourly Labor Cost (Lubbock, TX)

| Item | Value |
|---|---|
| Average Market Wage (Lubbock) | $14.00 |
| Lubbock median janitor wage (BLS 2024) | $12.95/hr |
| Competitive Boost % | 10.00% |
| Base Hourly Pay | $15.40 |
| SUTA – State Unemployment (TX) | 2.70% |
| FUTA – Federal Unemployment | 0.60% |
| Social Security Match (FICA) | 6.20% |
| Medicare Match (FICA) | 1.45% |
| Workers Comp Insurance (TX est.) | 2.50% |
| General Liability Insurance | 1.50% |
| Total Payroll Liabilities Rate | 14.95% |
| **TRUE HOURLY LABOR COST** | **$17.70** |

---

## Section C — Cleaning Time Estimation

| Metric | Value |
|---|---|
| Production Rate (Sq Ft / Hr) | 3,000 |
| Core Cleaning Time (Hrs / Clean) | 2.67 |

### Fixture & Area Detail

| Area / Fixture | Quantity | Mins / Unit | Hours |
|---|---|---|---|
| Toilets | 5 | 3.00 | 0.25 |
| Sinks | 5 | 3.00 | 0.25 |
| Urinals | 2 | 2.00 | 0.07 |
| Desks / Stations | 20 | 0.75 | 0.25 |
| Break Room(s) | 2 | 10.00 | 0.33 |
| Lobby / Entrance | 1 | 10.00 | 0.17 |
| Conference Rooms | 2 | 8.00 | 0.27 |
| Glass / Windows | 8 | 1.00 | 0.13 |
| Total Fixture / Area Time (Hrs) | — | — | 1.72 |

**Total Cleaning Time / Clean: 4.38 hrs**

---

## Production Rate Reference (Sq Ft / Hr)

| Facility Type | Low | High |
|---|---|---|
| Office Space | 3,000 | 4,000 |
| Common Areas | 4,000 | 5,000 |
| Dealership | 3,500 | 4,500 |
| Educational | 2,500 | 3,500 |
| Medical (General) | 2,000 | 2,800 |
| Medical (Dense) | 1,500 | 1,800 |
| Apartment Common Area | 3,500 | 4,500 |
| Apartment Unit Turn | 800 | 1,200 |
| Retail | 3,000 | 4,000 |
| Warehouse | 5,000 | 7,000 |
| Restaurant | 1,500 | 2,500 |
| Gym / Fitness | 2,000 | 3,000 |

---

## Section D — Pricing & Margin Analysis

| Metric | Value |
|---|---|
| Weekly Cleaning Frequency | 5 |
| Weekly Labor Hours | 21.92 |
| Monthly Labor Hours (× 4.33) | 94.90 |
| Total Monthly Labor Cost | $1,679.93 |
| Monthly Supply Cost | $150.00 |
| Sales Tax Rate | 0.00% |
| Target Gross Margin % | 45.00% |
| Suggested Margin (by weekly hrs) | 45.00% |
| **Monthly Price (at Target Margin)** | **$3,327.15** |
| Monthly Gross Profit | $1,497.22 |
| Actual Gross Margin % | 45.00% |
| Price per Sq Ft / Month | $0.416 |
| Effective Hourly Rate Charged | $35.06 |

---

## Section E — Margin Comparison Table

| Gross Margin % | Monthly Price | Gross Profit | Price/SqFt | Recommended? |
|---|---|---|---|---|
| 70% | $6,099.78 | $4,269.84 | $0.762 | — |
| 65% | $5,228.38 | $3,398.45 | $0.654 | — |
| 60% | $4,574.83 | $2,744.90 | $0.572 | — |
| 55% | $4,066.52 | $2,236.59 | $0.508 | — |
| 50% | $3,659.87 | $1,829.93 | $0.457 | — |
| **45%** | **$3,327.15** | **$1,497.22** | **$0.416** | **MATCHES TARGET** |
| 40% | $3,049.89 | $1,219.96 | $0.381 | — |
| 35% | $2,815.28 | $985.35 | $0.352 | — |
| 30% | $2,614.19 | $784.26 | $0.327 | — |
| 25% | $2,439.91 | $609.98 | $0.305 | — |
| 20% | $2,287.42 | $457.48 | $0.286 | — |

---

## Section F — Apartment Complex Add-Ons

| Field | Value |
|---|---|
| Number of Units in Complex | 0 |
| Common Area Sq Ft | 0 |
| Laundry Rooms | 0 |
| Unit Turn Cleans per Month (est.) | 0 |
| Price per Unit Turn | $0.00 |
| Common Area Monthly Price (from D) | $3,327.15 |
| Unit Turn Monthly Revenue | $0.00 |
| **Total Apartment Complex Monthly Bid** | **$3,327.15** |

---

## Lubbock Market Context

| Metric | Range |
|---|---|
| Lubbock median janitor wage | $12.95/hr (25% below national avg of $17.27/hr) |
| Office cleaning (per sqft/visit) | $0.05–$0.25 |
| Medical facilities premium over office | 30–40% |
| Apartment common area (per sqft/visit) | $0.05–$0.15 |
| Apartment unit turns | $45–$120 per unit |
| Typical commercial charge rate | $25–$45/hr |

---

## Formula Reference

| Formula | Description |
|---|---|
| True Hourly Cost | Base Pay × (1 + Total Liabilities %) |
| Cleaning Time | (Total SqFt ÷ Production Rate) + Fixture Time |
| Monthly Labor Cost | Cleaning Time × Frequency × 4.33 × True Hourly Cost |
| Monthly Price | (Labor + Supplies) ÷ (1 − Target Margin %) |
| Gross Profit | Monthly Price − Labor − Supplies |

---

## Suggested Margin by Weekly Hours

| Weekly Hours | Target Margin |
|---|---|
| 0–3 hrs/week | 60% |
| 3–7 hrs/week | 55% |
| 7–14 hrs/week | 50% |
| 14–33 hrs/week | 45% |
| 33–66 hrs/week | 40% |
| 66+ hrs/week | 35% |

---

## Bid History Log

| Date | Client Name | Facility Type | Sq Ft | Frequency | Monthly Price | Gross Margin % | Status |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

---

## Related pages
- [[lbk-cleaners-launch]]
- [[quote-calculator-improved]]
- [[lbk-cleaners-finance-strategy]]
- [[lbk-cleaners-kpi-dashboard]]
