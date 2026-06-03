# lbk_cleaners_question_booklet.md

*(Converted from local file `lbk_cleaners_question_booklet.md.pdf` by the local-files connector on 2026-06-03.)*

---

LBK Cleaners — Complete Architecture
Question Booklet
Everything I need answered before building. Organized by system area.
SECTION A: Website & Booking Flow (Lovable)
A1. Scheduling & Calendar Logic
1. What calendar system are we using for appointment slots — GHL calendar with pre-set availability windows, or open date picker?
2. What are the available booking hours? (e.g., Mon-Fri 8am-5pm, Sat 9am-2pm, Sun closed?)
3. How far out can a customer book — 2 weeks, 30 days, 60 days? 4. Is there a minimum lead time for booking? (e.g., must book at least 48 hours in
advance?) 5. Can customers book same-day or next-day, or is there a buffer?
A2. Capacity & Staffing
1. How many cleaning teams/cleaners are currently active? 2. How many jobs can be handled per day right now? 3. Should the calendar block off slots once capacity is reached for that day, or is it
unlimited and you manage overflow manually? 4. If multiple teams exist, does the system need to assign specific cleaners to jobs, or is
that handled separately?
A3. Recurring Booking Logic
1. When a customer selects Weekly/Bi-Weekly/Monthly, does the system auto-book ALL future appointments on the same day/time going forward?
2. Or does it book only the first appointment and auto-generate the next one after each service is completed?
3. If auto-booking forward, how many weeks out does it pre-schedule? (4 weeks? 8 weeks? Indefinitely?)
4. Can recurring customers skip a week without canceling their entire recurring plan?

A4. Pricing Engine Details
1. The base standard clean is $125. Is that for a 1-bed/1-bath under 1,000 sqft? What's the exact baseline spec?
2. Bedroom add-on: +$19 for the first extra bedroom, then +$10 for each additional — is that correct, or is it flat $19 per extra bedroom?
3. Bathroom add-on: +$30 per extra bathroom — starting from which count? (Is 1 bathroom included in base, so the charge starts at bathroom #2?)
4. Deep Cleaning multiplier: you said ~1.7x. Is it exactly 1.7x, or a different number? 5. Move-In/Out multiplier: same as deep cleaning (1.7x), or different? 6. The frequency discounts (Weekly 20%, Bi-Weekly 15%, Monthly 10%) — are these
applied to the total including add-ons, or just the base service price? 7. The 20% first-time discount — does it stack with the frequency discount? (e.g., new
customer + weekly = 20% first-time + 20% weekly = 40%? Or is it one or the other?)
A5. Add-Ons — Scope Clarification
1. "Inside Cabinets (partial)" vs. "Full Inside Cabinets (empty)" — partial means just accessible/reachable cabinets without emptying, and full means client empties everything first and we clean all surfaces inside?
2. "Full Inside Refrigerator" vs. "Empty Inside Refrigerator" — what's the distinction? Is "Full" = we clean it with food still in it, and "Empty" = client empties it first and we deep clean?
3. "Walls" — is this spot-cleaning scuffs/marks, or full wall wipe-down of all walls in the home? Or is it priced differently for each?
4. "Shedding Pets" — is this a flat surcharge regardless of number of pets, or does it scale (1 pet vs. 3 pets)?
5. "Disinfectant Treatment" — is this whole-home or per-room? Does it apply to all surfaces or specific high-touch areas?
6. Are add-ons available for ALL service types (Standard, Deep, Move-In/Out), or are some already included in Deep/Move-In/Out?
A6. Address & Property Lookup
1. Which property data API do you prefer — Zillow (via Bridge API), ATTOM Data, or should I research the best free/affordable option for this use case?
2. If the API has a cost per lookup, is there a budget ceiling? (Some charge $0.10-$0.50 per lookup)

3. Should the lookup happen as soon as they enter the address (auto-trigger), or when they click a "Look up my home" button?
4. If the lookup fails (new construction, rural property, etc.), does the form just show empty fields for manual entry with no error message, or should it say something like "We couldn't find your home details — please enter them manually"?
A7. Payment Page Details
1. Square processing fee (3.25%) — is this passed to the customer as a visible line item, or absorbed into the price?
2. Tax rate — what's the applicable sales tax rate for cleaning services in Lubbock? (Texas doesn't tax most cleaning services — can you confirm LBK Cleaners charges tax or not?)
3. Tip preset options: 10%, 15%, 20%, Custom. Are these percentages of the subtotal before or after fees/tax?
4. After payment is confirmed, what does the customer see? A confirmation page with appointment details, a "thank you" screen, or a redirect somewhere?
5. Do they receive an email receipt from Square automatically, or do we send a custom confirmation email from GHL?
A8. Returning Customer Experience
1. When a returning customer enters their phone number, what exactly pre-populates? Just name/email/address, or also their last service type, frequency, beds/baths/sqft, parking, and access instructions?
2. Can a returning customer change their service type or add-ons for the new booking, or does it default to "rebook same service"?
3. If a returning customer has moved to a new address, does the system detect that, or do they just manually update it?
A9. Website — Current State & Branding
1. What's the current state of lbkcleaners.com — is it a live Lovable site with a basic landing page, or does it need to be built from scratch?
2. Do you have brand assets locked in (logo, color palette, fonts)? 3. Is there a specific design style you want — modern/minimal, warm/friendly,
bold/corporate? 4. Are there any pages beyond the booking flow that need to exist? (About Us, Services
breakdown, FAQ, Contact, Blog?)

5. Should the site have a header navigation, or is it a single-page funnel focused purely on booking?
SECTION B: GHL Pipeline & Automations
B1. Pipeline Stage Transitions
1. Stage 1 (New Lead) → Stage 2 (Quote Viewed): This happens automatically when the form submits and the quote is displayed. Is there any manual gate here, or is it purely automated?
2. Stage 2 → Stage 3 (Booked & Paid): Triggered by Square payment webhook. Confirmed — no manual step?
3. Stage 4 (Service Scheduled) → Stage 5 (Service Completed): You said manual toggle for now. Is this done inside GHL (marking appointment complete), or through a separate action?
4. Stage 5 → Stage 6 (Review Requested): Does this fire immediately when you mark service complete, or is there a delay?
5. Stage 6 → Stage 7 (Recurring Active): What triggers this? Is it when the customer has a frequency other than "One-Time" and their first service is complete?
6. Stage 7 → Stage 8 (Lapsed): 45+ days with no booking and no active subscription. Is this a GHL workflow that checks daily, or a manual review?
B2. Abandoned Quote Recovery
1. The 30-minute follow-up fires for contacts in Stage 1 who haven't moved to Stage 2. But based on your updated flow, Stage 1 is "New Lead" (form submitted) and Stage 2 is "Quote Viewed" (they saw the price). So the abandoned quote recovery should fire for people in Stage 2 who haven't moved to Stage 3 (Booked & Paid) — correct? Because by Stage 2, they already have the quote but haven't paid.
2. If someone gets the 20% first-time discount follow-up (after 24 hours), and THEN books — does the discount auto-apply at checkout, or do they need a code at that point?
B3. Follow-Up Sequences — Timing & Logic
1. For the abandoned quote recovery: after the 30-min text and the 24-hour text, is there a third touch? Or does it stop at 2 messages?
2. For the 20% first-time discount: this goes out after 24 hours of no conversion. Is there a follow-up after that, or is it one shot?

3. If a lapsed client re-books, do they re-enter the pipeline at Stage 3 (Booked & Paid), or do they go back to Stage 1?
4. For recurring clients (Stage 7), the monthly check-in asks "anything special for next visit?" — if they reply with notes, where do those notes get stored? Contact notes? A custom field?
B4. Cancellation & Reschedule Policy
1. 24-hour cancellation policy — if someone cancels within 24 hours of their appointment, is there a fee charged? If so, how much (flat fee or percentage)?
2. If they cancel within 24 hours, does the system enforce the fee automatically, or just flag it for you?
3. How many times can a customer reschedule before it becomes a concern? Is there a limit?
4. When someone reschedules, do they pick a new date via text (AI asks "what date works?"), get sent back to the booking page, or does it create a task for you?
SECTION C: Voice AI (Lena)
C1. Call Handling Details
1. When Lena answers, what's her greeting? (e.g., "Thank you for calling LBK Cleaners, this is Lena, how can I help you?")
2. If a caller asks about pricing, does Lena quote exact numbers over the phone, or does she direct them to the website for an instant quote?
3. Can Lena book appointments directly over the phone (collecting all info verbally and creating the booking in GHL), or does she always send a booking link?
4. If Lena sends a booking link via SMS during the call, does she stay on the line while they fill it out, or does she say "I've sent you a link, you can complete it at your convenience"?
5. For returning clients calling in — Lena greets them by name and offers to rebook. Can she process payment over the phone (read card number), or does she always send a payment link?
C2. Escalation & Edge Cases
1. "Persistent request for live person" — how many times does the caller need to ask before Lena transfers? (Once? Twice? Three times?)

2. If Joshua doesn't answer the transfer, Lena takes a message. Does she ask specific questions (name, reason for call, callback number), or just let them speak freely?
3. What if someone calls about a complaint or quality issue? Does Lena handle it (apologize, offer re-clean within 24 hours per policy), or immediately escalate?
4. What if someone calls asking about employment/hiring? Lena sends the application link — is there anything else she should say (pay range, requirements, hours)?
C3. After-Hours Behavior
1. After-hours greeting — does it change? (e.g., "Thanks for calling LBK Cleaners. Our office is currently closed, but I can still help you...")
2. After-hours: can Lena still send booking links and answer questions, or does she only take messages?
3. The callback task created after-hours — who does it get assigned to in GHL? Just you, or a team?
SECTION D: Integrations & Technical
D1. GHL ↔ Lovable Connection
1. Is the Lovable site already deployed and connected to the GHL location, or does the connection still need to be established?
2. The Lovable backend functions — are these already set up in the Lovable project, or do they need to be created from scratch?
3. For the webhook from Square → GHL: is there already a webhook endpoint configured in GHL, or does this need to be built?
D2. Square Setup
1. Is the Square account already created and connected to GHL, or just connected to GHL but not fully configured?
2. Is Square in sandbox/test mode or live production mode right now? 3. Do you have the Square API credentials (Application ID, Access Token) available, or do I
need to retrieve them from the Square dashboard? 4. For the per-contact payment links (returning customers): does the Square account have
the Checkout API / Payment Links API enabled?
D3. Property Lookup API

1. Do you have an existing account with any property data provider (Zillow, ATTOM, Realtor.com, etc.)?
2. Budget for property lookups — is there a monthly cap you'd want to set? (e.g., 500 lookups/month at $0.10 each = $50/month)
3. If the cost is too high, would you accept a simpler approach where the customer just enters beds/baths/sqft manually (no auto-lookup)?
D4. GHL Conversation AI
1. Is GHL Conversation AI already enabled on this location, or does it need to be activated? 2. Does the current GHL plan include Conversation AI, or is it an add-on that needs to be
purchased? 3. For training the AI — do you want it to handle ONLY FAQ-style questions and direct to
booking, or should it be able to actually modify appointments (reschedule, cancel) through the conversation?
SECTION E: Business Operations & Policies
E1. Service Delivery
1. What's the average job duration for each service type? (Standard: ~2 hrs? Deep: ~4 hrs? Move-In/Out: ~5 hrs?)
2. Is there a minimum booking amount? (e.g., can someone book a 1-bed/1-bath standard clean for $125, or is there a floor?)
3. Do cleaners bring their own supplies, or does the customer need to provide anything? 4. Is there a key lockbox system for recurring clients, or do they need to be home every
time?
E2. Refund & Satisfaction Policy
1. "Satisfaction re-clean offered within 24 hours" — does the customer need to report the issue within 24 hours of service completion to qualify?
2. If they request a re-clean, is it the full home or just the areas they're unsatisfied with? 3. Is there ever a scenario where a cash refund is given, or is it always a re-clean?
E3. Communication Preferences

1. All SMS comes from "Lena" — does email also come from Lena, or from "LBK Cleaners" / "Joshua" / a generic brand name?
2. Is there a specific email address for outbound emails? (e.g., hello@lbkcleaners.com, lena@lbkcleaners.com?)
3. For the owner notification texts (voicemail transcriptions, callback tasks) — those go to (806) 781-8495. Is that also where urgent escalations go, or is there a separate number?
E4. Competitive Positioning
1. The 20% first-time discount — is there an expiration on it? (e.g., "Book within 7 days to get 20% off your first clean"?)
2. Are there any other promotions planned? (Referral program, seasonal specials, bundle deals?)
3. Do you want a referral program built into the system? (e.g., "Refer a friend, get $25 off your next clean"?)
NSEeCeTdItOoNUFn:dFeurtsutarendB)uild Context (Not Building Now, But
F1. Cleaner App / Internal Tools
1. The Connecteam integration — is this already set up and active, or is it planned? 2. When the custom Lovable-built cleaner app is eventually built, should it integrate with
GHL for job assignments, or will that stay in Connecteam? 3. GPS clock-in/clock-out — is this for payroll purposes, quality verification, or both?
F2. Scaling Considerations
1. At what point do you plan to hire cleaners? (After X bookings per week? A specific revenue target?)
2. When staff is hired, does the calendar need to support assigning specific cleaners to specific jobs based on location/availability?
3. Will there be a team lead or manager role, or will you manage all cleaners directly?
SECTION G: Testing & Launch

G1. Testing Plan
1. Do you want to run a full test cycle with a fake customer before going live (test booking, test payment in Square sandbox, test SMS sequences)?
2. Is there a target launch date for the full system? 3. Do you want a soft launch (invite-only, limited bookings) or hard launch (open to
public, marketing push)?
G2. Post-Launch
1. Who monitors the system daily once it's live — you, or should there be automated alerts for issues (failed payments, missed appointments, etc.)?
2. How quickly do you want to respond to new leads? (Is there an SLA — e.g., all new leads contacted within 5 minutes via automation?)
3. Do you want a daily/weekly report on bookings, revenue, conversion rates, etc.? If so, where — email, Notion, or GHL dashboard?
That's everything I can think of — 109 questions across all systems. Answer what you can now, flag anything that's "decide later," and let me know if any of these spark new ideas you want to add.


