---
name: zapier
type: entity
tags: [automation, integration]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md]
updated: 2026-05-29
---

# Zapier

**Summary**: Integration layer connecting platforms across the WIH and LBK Cleaners stack. The bridge between BookingKoala and GHL.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md

**Last updated**: 2026-05-29

---

Handles integrations between platforms that don't have native connections. Works alongside [[n8n]] for workflow automation.

For [[lbk-cleaners]], Zapier is the critical bridge between [[bookingkoala]] and [[ghl]]. BookingKoala exposes 16 native Zapier triggers:

- New Booking / Booking Updated / Booking Cancelled / Booking Completed / Booking Charged
- New Customer / Customer Updated
- New Provider / Update Provider / Delete Provider / Provider Payout
- New Quote / New Rating / Card Hold / Booking Deleted / Booking Charge Declined

Key automation to build: **New Booking → GHL pipeline entry** so every LBK Cleaners booking automatically flows into the GHL hub where [[mostafa]] can manage it. This makes [[ghl]] the single source of truth across all business lines, including the cleaning business.

## Related pages
- [[n8n]]
- [[ghl]]
- [[bookingkoala]]
- [[lbk-cleaners-launch]]
- [[mostafa]]
