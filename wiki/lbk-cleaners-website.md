---
name: lbk-cleaners-website
type: entity
tags: [website, lovable, booking, payments, square, ghl, lbk-cleaners]
status: active
sources: [lbk-cleaners-bookingkoala-setup-guide.md, lbk-cleaners-builder-q3-answers.md]
updated: 2026-06-09
---

# LBK Cleaners Website

**Summary**: Single-page booking funnel for [[lbk-cleaners]] built on Lovable. Handles the full customer flow from landing → instant quote → payment. Square processes payments; GHL manages the pipeline; [[bookingkoala]] handles operations after booking.

**Sources**: lbk-cleaners-bookingkoala-setup-guide.md, lbk-cleaners-builder-q3-answers.md

**Last updated**: 2026-06-09

---

## Site Details

| Field | Value |
|---|---|
| Platform | Lovable (AI site builder) |
| URL | lbkcleaners.com |
| Phone | (844) 717-CLEAN |
| Support Email | lena@lbkcleaners.com |
| Brand Colors | Dark Green `#0F3A20`, Gold `#D4AF37` |
| Design Style | Modern, minimal, premium — clean white space |
| Navigation | Logo left + "Call Us: (844) 717-CLEAN" right only |

---

## Page Structure (Booking Funnel)

```
Landing / Home  →  Step 1: Contact  →  Step 2: Instant Quote  →  Step 3: Payment  →  Thank You
```

1. **Landing** — CTA to start booking; headline, trust signals, what's included
2. **Step 1: Contact Gate** — name, phone, email; contact created in GHL at Stage 1
3. **Step 2: Instant Quote** — address lookup → auto-fill beds/baths/sqft → pricing calculator → GHL moved to Stage 2
4. **Step 3: Payment** — service type, add-ons, frequency, date/time, Square Web Payments SDK
5. **Thank You** — confirms service type, date, arrival window, contact number; GHL moved to Stage 3

---

## Pricing Engine

### Base Price
- **$125** — 1 bedroom, 1 bathroom, under 1,000 sqft (absolute floor; no booking accepted below this)

### Bedroom Add-Ons
| Extra Bedroom | Price |
|---|---|
| 2nd bedroom | +$19 |
| 3rd bedroom+ | +$10 each |

### Bathroom Add-Ons
| Extra Bathroom | Price |
|---|---|
| Each additional bath beyond 1st | +$30 |

### Service Type Multipliers
| Service | Multiplier |
|---|---|
| Standard Clean | 1.0× |
| Deep Clean | 1.7× |
| Move-In / Move-Out | 1.7× |

Inside oven and baseboards are **included** in Deep Clean and Move-In/Out — UI should hide those add-ons for those service types.

### Frequency Discounts (applied to total including add-ons)
| Frequency | Discount |
|---|---|
| One-Time | 0% |
| Monthly | 10% |
| Bi-Weekly | 15% |
| Weekly | 20% |

**First-time discount (20%) and frequency discount do NOT stack** — the system applies whichever is greater.

### Add-On Pricing
| Add-On | Price | Availability |
|---|---|---|
| Inside Oven | $35 | Standard only (included in Deep/Move) |
| Inside Fridge (food inside) | $25 | All |
| Inside Fridge (empty) | $40 | All |
| Inside Cabinets (partial) | $25 | All |
| Inside Cabinets (full empty) | $50 | All |
| Interior Windows | $5 per window | All |
| Full Wall Wipe-Down | $0.10/sqft | All |
| Shedding Pets Surcharge | $35 flat | All |
| Disinfectant Treatment | $50 flat | All |
| Laundry (per load) | $20 | Standard + Deep only |

### Payment Rules
- Square processing fee (3.25%) is **absorbed** — not shown as a line item
- **No sales tax** on residential cleaning in Texas (TX Comptroller Publication 94-111; confirm with CPA before launch)
- Tips: 10% / 15% / 20% / Custom — calculated on subtotal before fees

---

## Booking Constraints

| Rule | Value |
|---|---|
| Minimum lead time | 48 hours (no same-day or next-day) |
| Max booking window | 60 days out |
| Daily capacity | 2–3 jobs max (GHL calendar enforces) |
| Working hours (Mon–Fri) | 8:00 AM – 5:00 PM CST |
| Working hours (Sat) | 9:00 AM – 2:00 PM CST |
| Sunday | Closed |

---

## Property Lookup (Step 2)

- **API**: RentCast (preferred) or ATTOM Data — $50/month max, ~$0.10/lookup
- **Trigger**: Manual "Look up my home" button — not auto-triggered on address entry
- **Fallback**: Manual entry with message "We couldn't find your home details — please enter them below"
- Pre-populates: bedrooms, bathrooms, sqft
- Budget cap: $50/month (~500 lookups/month)

---

## Square Payment Connection

Square handles all payments on the Lovable site. **Current status: connection needs to be completed.**

### Setup Steps (Joshua must execute)
1. Log into [Square Developer Dashboard](https://developer.squareup.com/apps)
2. Create or open the LBK Cleaners application
3. Copy **Production** Application ID (`sq0idp-...`) and Access Token (`EAAA...`)
4. Add to Lovable project environment variables: `SQUARE_APP_ID` and `SQUARE_ACCESS_TOKEN`
5. The Square Web Payments SDK is embedded in Step 3 of the booking form
6. Enable **Payment Links API** in Square (needed for Lena to send per-contact payment links)
7. Test with Square Sandbox first — sandbox Application ID prefix `sandbox-`, token `EAAAlB...`
8. Switch to Production before launch

### Square → GHL Webhook
Lovable has a serverless endpoint that:
1. Receives Square payment confirmation webhook
2. Validates the webhook signature
3. Calls GHL API → moves contact to Stage 3 (Booked & Paid)
4. GHL triggers confirmation SMS sequence via Lena

---

## GHL Pipeline Stages

| Stage | Name | Trigger |
|---|---|---|
| 1 | New Lead | Contact form submitted (Step 1) |
| 2 | Quote Viewed | Quote displayed to customer (Step 2) |
| 3 | Booked & Paid | Square payment confirmed (webhook) |
| 4 | Service Scheduled | Appointment confirmed in GHL calendar |
| 5 | Service Completed | Joshua manually marks complete in GHL |
| 6 | Review Requested | 2-hour delay after Stage 5 |
| 7 | Recurring Active | Frequency ≠ One-Time AND first service complete |
| 8 | Lapsed | 45+ days no booking |

### Abandoned Quote Recovery
- **Message 1**: 30 minutes after Stage 2 if no payment
- **Message 2**: 24 hours after Stage 2 — includes `WELCOME20` promo code (7-day expiry, 20% off)
- No third touch

---

## Returning Customer Flow

When a returning customer enters their phone number and it matches a GHL contact, the following pre-populate:
- Full name, email, service address
- Last service type, last frequency
- Beds, baths, sqft
- Parking and access instructions (stored in `contact.parking_instructions`)

All fields remain editable. New data is saved back to GHL on booking.

---

## Bid Confirmation Workflow (On-Site)

For commercial bids or situations where the quote needs field confirmation:

1. **Customer gets estimate** via the Lovable booking form (Steps 1–2, no payment yet) — or Lena sends a quote summary via SMS
2. **Team visits the property** and assesses actual scope
3. **Confirm or adjust** the bid:
   - If pricing matches the quote → customer proceeds to Step 3 payment (booking link sent by Lena)
   - If scope differs → update the booking total in [[bookingkoala]] admin or GHL, send a revised payment link via Lena
4. **Customer pays** → webhook fires → contact moves to Stage 3 → confirmation SMS fires
5. **Booking lands in [[bookingkoala]]** → client profile created/updated with full job details

For on-site price confirmation at the property, the cleaner uses the **BookingKoala provider mobile app** to view job details, update notes, and confirm the final scope before completing the service.

---

## Voice AI — Lena

- **Number**: (844) 717-CLEAN
- **Email**: lena@lbkcleaners.com
- **Owner SMS alerts**: (806) 781-8495
- Lena always sends booking/payment links — never collects card numbers verbally
- Opening hours differ from booking hours: Mon–Fri 8am–7pm, Sat 9am–4pm
- After hours: fully functional for Q&A and booking links, cannot transfer to live person
- Transfer threshold: 2nd request triggers immediate transfer to Joshua

---

## Post-Service

- **Receipt**: Square auto-email receipt + GHL confirmation SMS
- **Review request**: 2 hours after service marked complete
  - 4–5 stars → redirected to Google Business Profile / Facebook to post
  - 1–3 stars → private feedback form → Joshua follows up within 24 hours
- **Re-clean policy**: within 24 hours of service, covers only unsatisfied areas (never cash refunds)

---

## Related pages
- [[lbk-cleaners]]
- [[lbk-cleaners-launch]]
- [[bookingkoala]]
- [[ghl]]
- [[stripe]]
- [[lbk-commercial-strategy]]
- [[source-lbk-bid-calculators]]
