---
name: bookingkoala
type: entity
tags: [crm, cleaning, scheduling, booking, platform, payments, client-profiles]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt, lbk-cleaners-bookingkoala-setup-guide.md, lbk-cleaners-builder-q3-answers.md]
updated: 2026-06-09
---

# BookingKoala

**Summary**: Full-stack service business platform for LBK Cleaners — booking, scheduling, cleaner management, payments, notifications, and hiring in one system.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt

**Last updated**: 2026-06-09

---

Used exclusively for [[lbk-cleaners]] operations. 370-article help center available as reference (source: BookingKoala_Help_Center_Full_Reference.md.txt).

Admin panel: `lbkcleaners.bookingkoala.com/admin`
Booking URL: `lbkcleaners.bookingkoala.com/booknow`

## LBK Cleaners Account Settings

| Field | Value |
|---|---|
| Business Name | LBK Cleaners |
| Support Email | info@lbkcleaners.com |
| Phone | (806) 429-4569 |
| Time Zone | CST6CDT |
| Date Format | MM/DD/YYYY |
| Time Format | 12-hour (e.g., 5:30 PM) |
| Tax Rate | 0% residential (TX exempt) / 8.25% if commercial |
| Service Area | Lubbock + Wolfforth, TX |
| Payment Processor | Square (Production keys required — see below) |

## Payment Processor — Square Setup

Square is the configured processor. **Current status: "Invalid key or no location exists" error — needs Production keys.**

### Fix Steps
1. Log into Square Developer Dashboard → copy **Production** Application ID (`sq0idp-...`) and Access Token (`EAAA...`)
2. Go to `Settings > General > Store Options > Admin > Connect Payment Gateways`
3. Toggle Square to **Enabled**
4. Paste Application ID and Access Token → click **Save**
5. Click **Get Locations** — pulls physical merchant locations from Square account
6. Select the Lubbock/Wolfforth location from dropdown → click **Save**
7. Verify in `Settings > Industries > [Industry] > Form 1 > Locations` — each location should be set to "No, Use Default" (or mapped to the specific Square location)

> Warning: Paste keys only in the BookingKoala admin panel — not in chat, Slack, or any unsecured log.

## Client Profile — What Gets Created

When a customer books for the first time, BookingKoala automatically creates a **customer profile** containing:

| Field | Source |
|---|---|
| Full name | Booking form Step 1 |
| Email address | Booking form Step 1 |
| Phone number | Booking form Step 1 |
| Service address | Booking form Step 2 |
| Beds / baths / sqft | Booking form Step 2 |
| Service type | Booking form Step 3 |
| Booking frequency | Booking form Step 3 |
| Payment method on file | Square (tokenized card) |
| Booking history | Auto-updated each job |
| Job notes / checklist results | Added by cleaner via provider app |
| Booking total + receipts | Auto-logged per charge |

Profiles are accessible at `Customers` in the BookingKoala admin panel. Each profile shows full booking history, payment records, and any notes left by the team.

## On-Site Bid Confirmation Workflow

For jobs where the final price needs to be confirmed after a property walkthrough (common for initial commercial bids or large residential add-ons):

1. **Customer gets online estimate** on [[lbk-cleaners-website]] (Steps 1–2) or via Lena SMS quote
2. **Team visits the property** to assess actual scope
3. **If the quote is accurate** → send the customer their booking link (Lena sends via GHL) to complete Step 3 payment
4. **If the scope changed** → admin updates the booking in BookingKoala (`Bookings > Edit`) with the confirmed price → customer receives updated quote and payment link
5. **Customer pays via Square** → booking is confirmed → confirmation SMS fires from GHL
6. **BookingKoala profile is created/updated** with all job details

### On-Site — Provider App Actions
The cleaner uses the **BookingKoala provider mobile app** at the property to:
- View job details and confirmed scope
- Update job notes (access codes, special instructions, parking)
- Complete job checklists (quality verification)
- Capture customer signature on completion
- Clock in/out (GPS-verified location)
- Trigger job completion → fires review request sequence

### Price Adjustment After Arrival
If additional scope is discovered after the job starts:
1. Cleaner notes it in the provider app
2. Admin creates an additional charge in `Bookings > [Booking] > Charges` → Square processes it
3. Customer receives updated receipt automatically

## Core Capabilities

**Booking forms** — 5 form types for different pricing structures. For cleaning: Form 1 (flat rate by bedrooms/bathrooms) or Form 2 (itemized packages). Must be selected and configured before going live.

**Smart scheduling** — automated engine that assigns cleaners based on availability and location. Critical to configure before launch.

**Notifications** — email and SMS templates for customers and cleaners: booking confirmations, reminders, completions, cancellations, payment receipts. All fully customizable.

**Provider (Cleaner) management** — full cleaner profiles with schedules, pay rates, industry settings. Cleaners get a mobile app to clock in/out, add job notes, and capture customer signatures.

**Hiring module** — 23 dedicated articles. A built-in pipeline for recruiting, vetting, and onboarding cleaners. Available on Growing and Premium plans. This is the next major milestone after the booking page goes live in [[lbk-cleaners-launch]].

**Checklists** — job checklists for cleaners to complete during service. Customers can review post-job.

**Marketing** — coupons, referral sharing (Growing+), campaign broadcasts (Premium), gift cards (Growing+).

**Reporting** — revenue and activity reports. Can sync to QuickBooks.

## Integrations

| Integration | Use Case |
|---|---|
| **Zapier** | 16 triggers (new booking, cancellation, charge, new customer, new provider, payout). Connects [[bookingkoala]] events to [[ghl]] pipeline — critical for WIH automation stack |
| **Stripe Connect** | Provider payouts — cleaners connect their bank accounts for direct deposit |
| **Square / PayPal / Authorize.net** | Alternative payment processors |
| **Google Calendar** | Sync all bookings; providers get their own calendar view |
| **Google Sheets** | Sync booking events for tracking and reporting |
| **QuickBooks** | Sync charges and refunds for accounting |
| **MailChimp** | Email lists: abandoned cart, one-time users, recurring users |
| **Google Analytics / Ads** | Website tracking and conversion measurement |

## Key Setup Sequence (for LBK Cleaners)
1. Store Options (Settings > General > Store Options)
2. Choose and configure booking form type
3. Set up smart scheduling
4. Configure notification templates
5. Create cleaner profiles and set up provider app
6. Activate payment processor (Stripe Connect for cleaner payouts)
7. Go live with booking page
8. Activate hiring module for ongoing cleaner recruitment
9. Connect Zapier → [[ghl]] for automation

## Support
- Email: support@bookingkoala.com
- Phone: +1 (800) 671-9655
- Demo: calendly.com/bookingkoala

## Related pages
- [[lbk-cleaners]]
- [[lbk-cleaners-website]]
- [[lbk-cleaners-launch]]
- [[zapier]]
- [[stripe]]
- [[ghl]]
- [[source-bookingkoala-help-center]]
