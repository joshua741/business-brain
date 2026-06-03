# LBK_Cleaners_Builder_Q3_Answers.md

*(Converted from local file `LBK_Cleaners_Builder_Q3_Answers.md.pdf` by the local-files connector on 2026-06-03.)*

---

LBK Cleaners — Complete Architecture Q&A Response (Round 3)
To: Implementation AI Agent (Builder) From: Lead Architect (Manus) Project: LBK Cleaners — Full Automation & Operations Build Document Purpose: Comprehensive answers to all 109 questions in the architecture question booklet. These answers are final and should be treated as locked-in decisions unless noted otherwise.
SECTION A: Website & Booking Flow (Lovable)
A1. Scheduling & Calendar Logic
A1.1 — Calendar System: Use the GHL calendar with pre-set availability windows. The Lovable booking form should query the GHL Calendar API to display available time slots. Do not use an open date picker that allows any date/time selection. Slots must be constrained to what GHL has open. A1.2 — Available Booking Hours: The calendar should only show slots during cleaner working hours: • Monday–Friday: 8:00 AM – 5:00 PM (CST) • Saturday: 9:00 AM – 2:00 PM (CST) • Sunday: Closed (no slots available) Note: These are the hours cleaners can START a job. Lena's phone answering hours (Mon– Fri 8am–7pm, Sat 9am–4pm) are different — that is just when she takes calls, not when bookings can be scheduled. A1.3 — Booking Window: Customers can book up to 60 days out. Do not allow bookings beyond 60 days. A1.4 — Minimum Lead Time: 48-hour minimum lead time. If today is Monday, the earliest available slot is Wednesday. Block out the next 48 hours from the calendar display. A1.5 — Same-Day/Next-Day: No same-day or next-day bookings. The 48-hour buffer is firm.
A2. Capacity & Staffing

A2.1 — Active Teams: Currently 1 active team (Joshua solo or with 1 cleaner). Plan the system for 1 team now with the architecture to support multiple teams later. A2.2 — Daily Capacity: 2–3 jobs per day maximum right now. The GHL calendar should enforce this limit. A2.3 — Capacity Blocking: Yes, block off slots once daily capacity is reached. Do not allow overflow bookings. Joshua manages his own schedule and does not want to be overbooked. A2.4 — Team Assignment: Not needed in the booking flow right now. The system just secures the time slot. Cleaner assignment is handled separately in Connecteam. Build the architecture so cleaner assignment can be added to GHL later, but do not build it now.
A3. Recurring Booking Logic
A3.1 — Auto-Booking: When a customer selects Weekly, Bi-Weekly, or Monthly, the system should auto-book ALL future appointments on the same day and time going forward. Do not wait for each service to be completed before scheduling the next. A3.2 — Generation Method: Pre-schedule forward on a rolling basis. A3.3 — Pre-Schedule Horizon: Pre-schedule 8 weeks out on a rolling basis. As each week passes and a new week opens up within the 8-week window, add the next appointment automatically. A3.4 — Skipping a Week: Yes, recurring customers can skip a single week without canceling their entire plan. For now, this is handled manually — the customer texts in, Joshua or Lena acknowledges it and removes that one appointment from GHL without touching the rest of the recurring schedule.
A4. Pricing Engine Details
A4.1 — Base Standard Clean Spec: $125 is the base price for a 1-bedroom, 1-bathroom home under 1,000 sqft. This is the absolute floor for any booking. A4.2 — Bedroom Add-On: +$19 for the first extra bedroom (bedroom #2), then +$10 for each additional bedroom after that. So a 3-bed home = $125 + $19 + $10 = $154 base before multipliers. A4.3 — Bathroom Add-On: +$30 per extra bathroom, starting from bathroom #2. The first bathroom is included in the base price. A 2-bath home = $125 + $30 = $155 base. A4.4 — Deep Cleaning Multiplier: Exactly 1.7x the standard price (after bedroom/bathroom add-ons are applied). A4.5 — Move-In/Out Multiplier: Exactly 1.7x the standard price (same as deep cleaning).

A4.6 — Frequency Discounts: Applied to the total price including all add-ons (not just the base). The discount applies to the full calculated amount before the Square fee is added.

Frequency Weekly Bi-Weekly Monthly One-Time

Discount 20% 15% 10% 0%

A4.7 — First-Time Discount vs. Frequency Discount: They do NOT stack. A new customer can receive the 20% first-time discount OR the frequency discount — whichever is greater for that booking. The system should apply whichever discount is larger and display it clearly. In practice, the first-time discount (20%) equals the weekly discount (20%), so for weekly new customers the first-time discount applies and the weekly discount kicks in from the second booking forward.

A5. Add-Ons — Scope Clarification

A5.1 — Inside Cabinets:

•

"Inside Cabinets (partial)" = We open and wipe accessible/reachable without the client emptying anything. Priced at $25.

cabinet

surfaces

•

"Full Inside Cabinets (empty)" = Client empties interior surfaces thoroughly. Priced at $50.

everything

beforehand;

we

clean

all

A5.2 — Inside Refrigerator:

•

"Full Inside Refrigerator" door seals). Priced at $25.

=

We

clean

it

with

food

still

in

it

(wiping

shelves,

drawers,

•

"Empty Inside Refrigerator" = Client interior surfaces. Priced at $40.

empties

it

first;

we

do

a

full

deep

clean

of

all

A5.3 — Walls:

•

Spot-cleaning charge.

scuffs

and

marks

is

included

in

Deep

Clean

and

Move-In/Out

at

no

extra

•

"Full Wall Wipe-Down" as a standalone add-on = full wipe-down of all wall surfaces in the home. Priced at $0.10 per sqft of the home (so a 1,200 sqft home = $120 add-on).

This is a premium add-on and should be clearly described as "full wall surface cleaning."

A5.4 — Shedding Pets: Flat surcharge of $35 regardless of the number of pets. This covers extra vacuuming, dander removal, and additional time. It is not scaled per pet. A5.5 — Disinfectant Treatment: Whole-home treatment (electrostatic spray or fogger applied to all high-touch surfaces throughout the home). Flat $50 add-on. Not per-room. A5.6 — Add-On Availability by Service Type:

Add-On

Standard

Inside Oven

✓

Inside Fridge (Full) ✓

Inside Fridge (Empty) ✓

Inside Cabinets (Partial)

✓

Inside Cabinets (Full Empty)

✓

Walls (Full Wipe-Down) ✓

Interior Windows ✓

SSuhrecdhdairnggePets

✓

Disinfectant Treatment ✓

Laundry (per load) ✓

Deep Clean Included ✓ ✓
✓
✓
✓ ✓
✓
✓ ✓

Move-In/Out Included Included ✓ ✓
✓ ✓ ✓ ✓ ✓
✗

Note: Inside oven and baseboards are included in Deep Clean and Move-In/Out by default. The UI should reflect this so customers don't add them unnecessarily. Add-On Pricing Reference Table:

Add-On

Price

Inside Oven

$35

Inside Fridge (Full, food inside)

$25

Inside Fridge (Empty, client empties)

$40

Inside Cabinets (Partial)

$25

Inside Cabinets (Full Empty)

$50

Interior Windows Full Wall Wipe-Down Shedding Pets Surcharge Disinfectant Treatment Laundry (per load)

$5 per window $0.10/sqft $35 $50 $20/load

A6. Address & Property Lookup
A6.1 — API Preference: The preferred approach is RentCast API or ATTOM Data for property lookups (beds, baths, sqft). If neither is feasible within budget, fall back to manual entry. Do NOT use Zillow Bridge API — it requires a formal partnership application and is not accessible for this use case. RentCast has a free tier (100 requests/month) and paid plans starting at ~$35/month. A6.2 — Budget Ceiling: $50/month maximum for property lookups. At roughly $0.10 per lookup, that is ~500 lookups/month, which is more than sufficient for the current volume. A6.3 — Trigger: Lookup should happen when the user clicks a "Look up my home" button, not automatically on address entry. This prevents unnecessary API calls and gives the user control. A6.4 — Failure State: If the lookup fails (new construction, rural property, unrecognized address), show empty fields for manual entry with the friendly message: "We couldn't find your home details — please enter them manually below." Do not show a technical error. The form should still be fully functional for manual input.
A7. Payment Page Details
A7.1 — Square Processing Fee: The 3.25% Square fee is absorbed into the price. It is NOT shown as a visible line item to the customer. The price displayed is the all-in price. A7.2 — Sales Tax: LBK Cleaners does NOT charge sales tax on residential cleaning services. Under Texas law (Texas Comptroller Publication 94-111), there is no sales tax on charges from a cleaning company providing residential maid services. The total sales tax rate in Lubbock is 8.25% (6.25% state + 2% city), but this does not apply to LBK Cleaners' residential cleaning services. Confirm with a Texas CPA before launch, but this is the standard interpretation. A7.3 — Tip Presets: 10%, 15%, 20%, Custom. Tips are calculated on the subtotal before any fees or discounts — i.e., on the raw service price before the Square fee is factored in.

A7.4 — Post-Payment Experience: After payment is confirmed, the customer sees a custom "Thank You" confirmation page built in Lovable. This page shows: • Service type • Date and time • Address • Cleaner arrival window • Contact number for questions: (844) 717-CLEAN A7.5 — Receipt: The customer receives both the automatic Square email receipt AND a custom GHL confirmation SMS (and email if they provided one). The GHL confirmation is the primary communication and should fire within seconds of payment confirmation via webhook.
A8. Returning Customer Experience
A8.1 — Pre-Population: When a returning customer enters their phone number and it matches a GHL contact, the following fields pre-populate: • Full name • Email address • Service address • Last service type • Last frequency • Beds, baths, sqft • Parking instructions • Access/entry instructions All of this data is pulled from the GHL contact record via the serverless function in Lovable's backend (never expose the GHL token client-side). A8.2 — Changing Service: Yes, returning customers can change their service type, frequency, and add-ons for the new booking. The form defaults to their last service but every field is editable. It should be clear that they are rebooking and can modify anything. A8.3 — Address Change: The system does not auto-detect an address change. If a returning customer has moved, they simply update the address field manually. The new address will be saved to their GHL contact record upon booking.
A9. Website — Current State & Branding

A9.1 — Current State: The website needs to be built from scratch in Lovable. There is no existing live site to work from. Model the booking flow after DallasMaids.com (3-step: Contact → Quote → Payment). A9.2 — Brand Assets: • Logo: LbkCleaners.png (provided in project files) • Color palette: Clean, professional blues and whites derived from the logo • Fonts: Modern sans-serif (e.g., Inter or Poppins) A9.3 — Design Style: Modern, minimal, clean, and highly trustworthy. The design should feel like a premium service, not a budget cleaner. Think clean white space, clear CTAs, and professional photography-style imagery. A9.4 — Pages: For the initial build, the site is a single-page booking funnel. No About Us, Blog, or FAQ pages are needed right now. The only pages needed are: 1. Landing/Home (with CTA to start booking) 2. Step 1: Contact Gate 3. Step 2: Instant Quote 4. Step 3: Payment & Booking 5. Thank You / Confirmation page A9.5 — Navigation: Minimal header with the LBK Cleaners logo on the left and "Call Us: (844) 717-CLEAN" on the right. No full navigation menu. This is a conversion-focused funnel, not a traditional website.
SECTION B: GHL Pipeline & Automations
B1. Pipeline Stage Transitions
B1.1 — Stage 1 → Stage 2 (New Lead → Quote Viewed): Purely automated. When the Lovable form submits Step 1 (contact info), the contact is created in GHL at Stage 1. When Step 2 (the quote) is displayed, GHL is updated to Stage 2 automatically via API call. No manual gate. B1.2 — Stage 2 → Stage 3 (Quote Viewed → Booked & Paid): Triggered by the Square payment webhook. When Square confirms payment, the webhook fires to GHL, which moves the contact to Stage 3. No manual step. B1.3 — Stage 4 → Stage 5 (Service Scheduled → Service Completed): Manual toggle by Joshua inside GHL. He marks the appointment as "complete" in the GHL calendar/appointment view. This is the trigger. No separate app needed right now.

B1.4 — Stage 5 → Stage 6 (Service Completed → Review Requested): Fires with a 2-hour delay after Joshua marks service complete. This gives the customer time to get home and settle before receiving the review request. B1.5 — Stage 6 → Stage 7 (Review Requested → Recurring Active): Triggered when the customer's service_frequency field is NOT "One-Time" AND their first service is marked complete. The workflow checks both conditions before moving to Stage 7. B1.6 — Stage 7 → Stage 8 (Recurring Active → Lapsed): An automated GHL workflow runs daily and checks for contacts in Stage 7 or Stage 3 who have had no new booking in 45+ days and whose service_frequency is "One-Time" (or their recurring subscription has effectively stopped). These contacts move to Stage 8 automatically.
B2. Abandoned Quote Recovery
B2.1 — Correct Target Stage: Confirmed. The abandoned quote recovery sequence fires for contacts in Stage 2 (Quote Viewed) who have NOT moved to Stage 3 (Booked & Paid) within 30 minutes. Stage 1 contacts who never even saw the quote get a different, simpler nudge. B2.2 — Discount Code Application: When the 20% first-time discount follow-up is sent (after 24 hours of no conversion), the SMS includes a promo code (e.g., WELCOME20). The customer enters this code at checkout on the Lovable site, and the discount is applied automatically. The code should be a GHL-tracked coupon that auto-expires after 7 days.
B3. Follow-Up Sequences — Timing & Logic
B3.1 — Abandoned Quote Recovery Sequence: Stops at 2 messages: • Message 1: 30 minutes after Stage 2 (quote viewed, no payment) • Message 2: 24 hours after Stage 2 (includes WELCOME20 code) • No third touch. Keep it clean. B3.2 — First-Time Discount Follow-Up: One shot only — sent at the 24-hour mark if no conversion. No follow-up after that. B3.3 — Lapsed Client Re-Entry: If a lapsed client re-books (responds to reactivation campaign or calls in), they re-enter the pipeline at Stage 3 (Booked & Paid) — not Stage 1. They are already a known contact; no need to re-run the new lead flow. B3.4 — Monthly Check-In Notes Storage: When a recurring client (Stage 7) replies to the monthly check-in with special instructions, those notes should be stored in a custom GHL field called contact.special_instructions_next_visit . Also append to the contact's notes with a

timestamp. This field should be visible on the contact record so Joshua can see it before the next job.
B4. Cancellation & Reschedule Policy
B4.1 — Cancellation Fee: $50 flat fee for cancellations within 24 hours of the scheduled appointment time. This applies to all service types. B4.2 — Fee Enforcement: The system flags it for Joshua to enforce manually. The GHL workflow creates a task for Joshua when a cancellation is detected within 24 hours, noting the $50 fee is due. Joshua then charges it via Square manually. The system does not autocharge. B4.3 — Reschedule Limit: No hard limit, but the system should flag for review after 3 consecutive reschedules by the same customer. A GHL task is created for Joshua to review the account. B4.4 — Reschedule Process: Lena (SMS bot) asks "What date works best for you?" and collects their preferred date. The system checks GHL calendar availability and confirms the new slot. The appointment in GHL is updated automatically. If no slots are available on their preferred date, Lena offers the next 2–3 available dates.
SECTION C: Voice AI (Lena)
C1. Call Handling Details
C1.1 — Opening Greeting: "Thank you for calling LBK Cleaners, this is Lena! How can I help you today?" C1.2 — Pricing Questions: Lena gives the starting base rate ($125 for a 1-bed/1-bath standard clean) and directs them to the website for an exact instant quote. She says: "Our standard cleaning starts at $125 for a 1-bedroom home. For an exact quote based on your home size and service type, I can send you a link to our instant quote calculator right now — it takes about 60 seconds. Would that work for you?" C1.3 — Booking Method: Lena always sends a booking link via SMS. She does not collect all booking details verbally and create the booking in GHL directly. The booking link goes to the Lovable site. This keeps the data clean and ensures payment is collected through the proper flow. C1.4 — Link Handoff Script:

"I've just sent a booking link to your phone. You can complete it right from your phone whenever you're ready — it only takes about 2 minutes. Is there anything else I can answer for you while I have you?" She stays on the line briefly to answer any remaining questions, then closes the call naturally. C1.5 — Returning Client Payment: Lena always sends a payment link. She does not read card numbers over the phone. She says: "Great, [Name]! I'll send you a secure payment link right now. Once you complete that, you're all set and we'll see you on [date]."
C2. Escalation & Edge Cases
C2.1 — Transfer Threshold: Twice. If the caller asks once, Lena acknowledges and tries to help. If they ask a second time, she transfers immediately during business hours. Script: First ask: "I completely understand. Let me see if I can help you first — what's your question?" Second ask: "Of course! Let me connect you with Joshua right now. One moment please." C2.2 — Message Taking (If Joshua Doesn't Answer): Lena asks structured questions: 1. "What's your name?" 2. "What's the best number to reach you?" 3. "Can you give me a brief reason for your call so Joshua can be prepared when he calls
you back?" She does NOT let them just speak freely — structured intake ensures Joshua has what he needs. C2.3 — Complaints / Quality Issues: Lena handles it with empathy first, then escalates: "I'm so sorry to hear that — that's not the experience we want you to have. We stand behind our work 100%. I'm going to make sure Joshua personally reaches out to you within the next few hours to make this right. We offer a complimentary re-clean within 24 hours. Can I confirm your name and the best number to reach you?" She creates an urgent GHL task tagged "Quality Complaint" and sends Joshua an immediate SMS alert. C2.4 — Employment/Hiring Calls: Lena says: "That's awesome — we're always looking for great cleaners! Pay starts at 40% of the job value for solo cleans, and we provide all the supplies. Hours are flexible, Monday through

Saturday. I'll send you our application link right now — it only takes a few minutes to fill out." She sends the application link via SMS and creates a GHL task for Joshua.
C3. After-Hours Behavior
C3.1 — After-Hours Greeting: "Thanks for calling LBK Cleaners! Our team is currently offline, but I'm Lena, our virtual assistant, and I'm here 24/7. I can answer questions, give you a quote, or send you a booking link right now. How can I help?" C3.2 — After-Hours Capabilities: Lena can still send booking links, answer questions, and provide pricing information after hours. She is fully functional — she just cannot transfer to a live person. If someone insists on speaking to Joshua after hours, she takes a message and creates a callback task. C3.3 — Callback Task Assignment: All after-hours callback tasks are assigned to Joshua in GHL. There is no team to assign to right now.
SECTION D: Integrations & Technical
D1. GHL ↔ Lovable Connection
D1.1 — Current Status: The Lovable site does not yet exist and the GHL connection has not been established. Both need to be built from scratch. D1.2 — Backend Functions: The Lovable backend functions (serverless edge functions) need to be created from scratch. These functions handle: • GHL contact creation/lookup via API • Square payment processing • Webhook receipt from Square → GHL stage update D1.3 — Square → GHL Webhook: This needs to be built. The flow is: 1. Square fires a payment confirmation webhook to a Lovable serverless endpoint 2. The endpoint validates the webhook signature 3. The endpoint calls GHL API to move the contact to Stage 3 (Booked & Paid) and create
the appointment 4. GHL triggers the booking confirmation SMS sequence

D2. Square Setup
D2.1 — Current Status: Square is connected to GHL but not fully configured for the Lovable integration. The Web Payments SDK needs to be embedded in the Lovable site. D2.2 — Mode: Live production mode. Do not use sandbox mode for the final build. Use sandbox only during testing. D2.3 — Credentials: Retrieve the Square Application ID and Access Token from the Square Developer Dashboard. The GHL integration already has Square connected, but the Lovable site needs its own Square Web Payments SDK credentials. D2.4 — Payment Links API: Yes, the Checkout API / Payment Links API must be enabled on the Square account. This is needed for Lena to generate per-contact payment links for returning customers.

D3. Property Lookup API
D3.1 — Existing Account: No existing account with any property data provider. D3.2 — Budget: $50/month maximum. At $0.10/lookup, that is ~500 lookups/month. D3.3 — Fallback: Yes, manual entry is the preferred fallback if the API is too complex or costly to implement quickly. The booking form should always work without the API. The property lookup is a convenience feature, not a requirement. If the API is not ready at launch, ship with manual entry and add the lookup later.

D4. GHL Conversation AI

D4.1 — Current Status: GHL Conversation AI needs to be activated on this location. It is not currently enabled.

D4.2 — Plan/Cost: GHL Conversation AI is part of the AI Employee feature set. It is an addon at $97/month per sub-account for unlimited usage (under the Unlimited plan's Fair Use Policy). This needs to be enabled and paid for before the SMS bot can be configured.

D4.3 — Training Scope: Train the AI to handle:

• FAQ-style questions (pricing, service area, what's included, etc.)

• Direct to booking (send booking link)

•

Appointment modification — the AI should be able to reschedule and cancel appointments through the conversation. This is a key capability. Configure the

bot

intent as "Appointment Booking" with the ability to also handle general support.

SECTION E: Business Operations & Policies
E1. Service Delivery
E1.1 — Average Job Duration:

Service Type Standard Clean (1-bed/1-bath) Deep Clean (1-bed/1-bath) Move-In/Out (1-bed/1-bath)

Average Duration ~2 hours ~4 hours ~5 hours

Add approximately 30–45 minutes per additional bedroom and 20–30 minutes per additional bathroom. E1.2 — Minimum Booking: $125 is the absolute minimum. There is no scenario where a booking is accepted below $125. E1.3 — Supplies: Cleaners bring all their own supplies (mops, vacuums, cleaning products, microfiber cloths, etc.). Customers do not need to provide anything. This is a key selling point and should be stated clearly on the website. E1.4 — Access System: Recurring clients are encouraged to use a key lockbox (like a Master Lock combination box) so they do not need to be home. For the first visit, the client should be present or provide access. The access method and any codes/instructions are stored in the contact.parking_instructions field in GHL (this field covers both parking and access).
E2. Refund & Satisfaction Policy
E2.1 — Reporting Window: The customer must report the issue within 24 hours of service completion to qualify for a re-clean. After 24 hours, the claim is not honored. E2.2 — Re-Clean Scope: The re-clean covers only the specific areas the customer is unsatisfied with, not the full home. Joshua will assess the complaint and dispatch accordingly. E2.3 — Cash Refunds: Never. The policy is always a re-clean, never a cash refund. This should be stated clearly in the Terms of Service and the booking confirmation.
E3. Communication Preferences

E3.1 — Email Sender Name: All automated emails should come from "Lena from LBK Cleaners" — not "Joshua," not "LBK Cleaners" alone. E3.2 — Email Address: Use lena@lbkcleaners.com as the outbound email address. This needs to be configured in GHL's email settings. E3.3 — Owner Notifications: All owner notification texts (voicemail transcriptions, callback tasks, urgent escalations, quality complaints, failed payments) go to (806) 781-8495. There is no separate escalation number.
E4. Competitive Positioning
E4.1 — First-Time Discount Expiration: The 20% first-time discount offer expires 7 days after it is sent. The WELCOME20 promo code should be configured with a 7-day expiration in GHL. E4.2 — Other Promotions: No other promotions are planned at this time. Do not build seasonal specials or bundle deals into the system. E4.3 — Referral Program: Not building now. Keep the architecture open for it (e.g., a "Referred By" field on the contact record), but do not build the referral tracking or reward system yet.
SECTION F: Future Build Context (Not Building Now)
F1. Cleaner App / Internal Tools
F1.1 — Connecteam Status: Connecteam is planned but not yet fully active. The account exists but has not been fully configured. GPS clock-in/out and scheduling are the primary features needed. F1.2 — Future App Integration: When the custom Lovable-built cleaner app is eventually built, it should integrate with GHL for job assignments (pulling job details, updating status) while Connecteam handles GPS clock-in/out and payroll. The two systems will coexist. F1.3 — GPS Purpose: GPS clock-in/out serves both payroll and quality verification. Payroll: confirms hours worked. Quality: confirms the cleaner was actually at the job location for the expected duration.
F2. Scaling Considerations

F2.1 — Hiring Trigger: Plan to hire when consistently hitting 15+ bookings per week or when Joshua can no longer handle the volume solo. No specific revenue target is set. F2.2 — Calendar Assignment: Yes, when staff is hired, the calendar will need to support assigning specific cleaners to specific jobs based on their location and availability. Build the GHL calendar architecture now with this in mind (use GHL's "Teams" or "Users" calendar feature so it can be expanded later). F2.3 — Management Structure: Joshua will manage all cleaners directly for the foreseeable future. No team lead or manager role is planned.
SECTION G: Testing & Launch
G1. Testing Plan
G1.1 — Full Test Cycle: Yes, run a full test cycle before going live: 1. Submit a test booking via Lovable (fake customer data) 2. Verify contact creation in GHL at Stage 1 3. Verify quote display moves contact to Stage 2 4. Process a test payment in Square sandbox mode 5. Verify contact moves to Stage 3 and confirmation SMS fires 6. Manually mark service complete; verify review SMS fires (with has_left_google_review =
"No") 7. Test Lena voice AI: call (844) 717-CLEAN and verify all 5 call paths 8. Test after-hours behavior 9. Test SMS bot sequences end-to-end G1.2 — Target Launch Date: As soon as testing is verified and passing. There is no fixed calendar date — the goal is to launch correctly, not to hit a specific date. G1.3 — Launch Type: Soft launch first. Invite 3–5 trusted contacts (friends, family) to go through the full booking flow as real customers. Collect feedback for 1 week, fix any issues, then open to the public with a marketing push.
G2. Post-Launch
G2.1 — System Monitoring: Set up automated GHL alerts for: • Failed payment attempts

• Missed/cancelled appointments • Contacts stuck in Stage 1 or 2 for more than 48 hours • Any Square webhook failures These alerts should send an SMS to Joshua at (806) 781-8495. G2.2 — Lead Response SLA: All new leads must be contacted within 5 minutes via automation (the GHL SMS bot fires immediately). No manual response is required for the initial contact — the automation handles it. G2.3 — Reporting: Send a weekly summary report every Monday morning to Joshua's email. The report should include: • Total bookings that week • Total revenue • New leads vs. conversions (conversion rate) • Cancelled/rescheduled jobs • Review requests sent vs. reviews received This can be built as a GHL workflow that compiles contact/opportunity data and sends a formatted email summary.

Appendix: Key Decisions Summary

Topic Booking lead time Booking window Base price Deep/Move-In multiplier Frequency discount basis First-time + frequency stacking
Sales tax
Square fee Tip calculation basis

Decision 48 hours minimum 60 days out $125 (1-bed/1-bath, <1,000 sqft) 1.7x Total price including add-ons No — one or the other Not charged (residential cleaning exempt in TX) Absorbed — not shown to customer Subtotal before fees/discounts

Cancellation fee Lena transfer threshold After-hours Lena
Property lookup API
GHL Conversation AI
Refund policy Email sender Referral program Launch type

$50 flat, manual enforcement 2nd request Fully functional (booking links, Q&A) RfaellnbtaCcakst or ATTOM; $50/month cap; manual Add-on required ($97/month); activate before build Re-clean only, never cash lena@lbkcleaners.com Not building now Soft launch first

Document prepared by Lead Architect (Manus). All decisions are final unless Joshua explicitly overrides them. Questions about any decision should be escalated to Joshua at (806) 781-8495 before proceeding with the affected build component.


