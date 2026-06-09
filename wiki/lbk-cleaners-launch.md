---
name: lbk-cleaners-launch
type: project
tags: [cleaning, lubbock, launch, bookingkoala]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md.txt, lbk-cleaners-finance-strategy.md, lbk-cleaners-goal-tracker.md, lbk-cleaners-finance-tracker.md, lbk-cleaners-bid-calculator-1.md, quote-calculator.md, quote-calculator-improved.md, lubbock-market-research-template.md]
updated: 2026-05-29
---

# LBK Cleaners Launch

**Summary**: LBK Cleaners go-to-market execution. Website live, BookingKoala CRM configured. Goal: ramp to $11,000+/mo gross to fund Nehemiah's camp ($2,200 by Jul 2026) then a house ($2,750/mo net by Sep 2026).

**Sources**: CLAUDE.md seed; BookingKoala reference; finance strategy/trackers; bid & quote calculators; Lubbock market research

**Last updated**: 2026-05-29

---

Launch sequence for [[lbk-cleaners]]. Operated under [[mostafa]]'s oversight. [[bookingkoala]] is the full operational platform.

## Current State
- Website (Lovable): live at lbkcleaners.com
- BookingKoala CRM: configured — see [[bookingkoala]] for full setup detail
- Square: connected to GHL; needs Production keys added to both [[lbk-cleaners-website]] (Lovable env vars) and BookingKoala (admin panel) to go live
- Booking page: not yet published — blocked on Square payment connection

## Financial plan ([[profit-first]])
- Targets: **$11,000+/mo gross, $2,750+/mo net, 25%+ margin**, avg job $175, ~20 jobs/week, 15+ recurring clients (source: lbk-cleaners-finance-strategy.md, lbk-cleaners-goal-tracker.md).
- Per-job economics (standard $175 clean): cleaner pay $70, supplies $12, gas $8 → **$85 gross profit (48%)**; break-even ~8–9 jobs/month (source: lbk-cleaners-finance-strategy.md).
- Profit First allocation (Phase 1 <$250k/yr): OpEx 52%, Tax 15%, Owner Pay 20%, Profit 5%, Goal sinking funds 8%; allocate on the 10th & 25th. Goal waterfall funds the Camp Fund first, then House Fund (source: lbk-cleaners-finance-strategy.md). Banking via [[mercury]].
- **Distributions: Joshua Webber 60% / Oralia Rivera 40%**, paid only after expenses + tax reserves (source: lbk-cleaners-finance-tracker.md). KPI benchmarks: cancellation <5%, utilization >75%, rebooking >60%, satisfaction >4.5/5 (source: lbk-cleaners-finance-tracker.md).
- Goal tracker (as of 5/21/2026): Camp Fund $0 / $2,200 (status Behind); House Fund ramp-up (source: lbk-cleaners-goal-tracker.md).

## Bidding tools
- **Bid Calculator / Quote Calculator (Improved)** — Lubbock-rate-loaded commercial bid tools: true hourly labor cost (~$17.70 all-in at $14 base + 14.95% liabilities), production rates by facility type, monthly price by margin (target 45% commercial); plus a Quick Eyeball Bid (source: lbk-cleaners-bid-calculator-1.md, quote-calculator-improved.md, quote-calculator.md). See [[source-lbk-bid-calculators]].
- **Lubbock market research / Airbnb data** template used for market context (Lubbock median janitor wage $12.95/hr) (source: lubbock-market-research-template.md).

## Launch Sequence

### Phase 1: Booking Page (Current — Square is the blocker)
1. **Connect Square to BookingKoala** — get Production Application ID + Access Token from Square Developer Dashboard; paste into `Settings > General > Store Options > Admin > Connect Payment Gateways`; click Get Locations; map to Lubbock/Wolfforth location (see [[bookingkoala]])
2. **Connect Square to Lovable site** — add `SQUARE_APP_ID` and `SQUARE_ACCESS_TOKEN` to Lovable project env vars; enable Payment Links API in Square (for Lena payment link sends)
3. Configure smart scheduling — arrival windows, 30-min buffer, 16-hr cut-off
4. Set up notification templates (customer and cleaner SMS/email)
5. Test booking flow end-to-end (Square sandbox → then production)
6. Publish booking page
7. Soft launch — 3–5 trusted contacts first; 1 week feedback; then public

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
- [[lbk-cleaners-website]]
- [[bookingkoala]]
- [[mostafa]]
- [[zapier]]
- [[ghl]]
- [[profit-first]]
- [[mercury]]
- [[lbk-commercial-strategy]]
- [[source-bookingkoala-help-center]]
- [[source-lbk-bid-calculators]]
