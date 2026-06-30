---
name: bookingkoala
type: entity
tags: [crm, cleaning, scheduling, booking, platform]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt]
updated: 2026-05-29
---

# BookingKoala

**Summary**: Full-stack service business platform for LBK Cleaners — booking, scheduling, cleaner management, payments, notifications, and hiring in one system.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt

**Last updated**: 2026-05-29

---

Used exclusively for [[lbk-cleaners]] operations. 370-article help center available as reference (source: BookingKoala_Help_Center_Full_Reference.md.txt).

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
- [[lbk-cleaners-launch]]
- [[zapier]]
- [[stripe]]
- [[source-bookingkoala-help-center]]
