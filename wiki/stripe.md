---
name: stripe
type: entity
tags: [payments, merchant-account, provider-payouts]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md]
updated: 2026-05-29
---

# Stripe

**Summary**: Payment processing for WIH and LBK Cleaners. Merchant account at 3423 E Baylor St. Stripe Connect handles cleaner payouts via BookingKoala.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md

**Last updated**: 2026-05-29

---

Two distinct roles:

**WIH payments:** Merchant account for real estate transactions, tied to [[3423-e-baylor-st]].

**LBK Cleaners payouts:** [[bookingkoala]] uses Stripe Connect to pay cleaners directly. Each cleaner connects their own bank account via Stripe Connect, and BookingKoala deposits their pay automatically. Setup requires creating a Stripe Connect platform application in the Stripe dashboard before enabling provider payments in BookingKoala. This is a Phase 1 setup item for [[lbk-cleaners-launch]].

## Related pages
- [[wih]]
- [[3423-e-baylor-st]]
- [[bookingkoala]]
- [[lbk-cleaners]]
- [[lbk-cleaners-launch]]
