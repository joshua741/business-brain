---
name: lbk-cleaners-launch
type: project
tags: [cleaning, lubbock, launch, bookingkoala]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt]
updated: 2026-05-29
---

# LBK Cleaners Launch

**Summary**: LBK Cleaners go-to-market execution. Website live, BookingKoala CRM configured. Next: booking page live, then cleaner hiring via the hiring module.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt

**Last updated**: 2026-05-29

---

Launch sequence for [[lbk-cleaners]]. Operated under [[mostafa]]'s oversight. [[bookingkoala]] is the full operational platform.

## Current State
- Website: live
- BookingKoala CRM: configured

## Launch Sequence

### Phase 1: Booking Page (Current)
1. Choose booking form type — Form 1 (flat rate by bedrooms/bathrooms) or Form 2 (itemized packages)
2. Configure smart scheduling
3. Set up notification templates (customer and cleaner SMS/email)
4. Connect payment processor (Stripe Connect for cleaner payouts)
5. Test booking flow end-to-end
6. Publish booking page

### Phase 2: Cleaner Hiring
1. Activate the **Hiring Module** in BookingKoala (Growing/Premium plan required)
2. Set up hiring pipeline — application form, vetting questions, offer flow
3. Add approved cleaners as Providers with: schedule, pay rate, form settings
4. Set up provider mobile app for cleaners (clock in/out, job notes, signatures)
5. Use the Import Tool for bulk cleaner onboarding if needed

### Phase 3: Automation
1. Connect BookingKoala to [[zapier]] — set up triggers:
   - New booking → GHL pipeline entry
   - Booking completed → follow-up sequence
   - New provider → onboarding sequence
2. Connect [[bookingkoala]] to [[ghl]] for customer and provider comms routing through [[mostafa]]
3. Activate checklists for cleaner quality control

## Related pages
- [[lbk-cleaners]]
- [[bookingkoala]]
- [[mostafa]]
- [[zapier]]
- [[ghl]]
- [[source-bookingkoala-help-center]]
