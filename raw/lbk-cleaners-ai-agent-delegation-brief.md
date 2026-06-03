# LBK_Cleaners_AI_Agent_Delegation_Brief

*(Converted from local file `LBK_Cleaners_AI_Agent_Delegation_Brief.pdf` by the local-files connector on 2026-06-03.)*

---

LBK Cleaners — AI Agent Delegation Brief & Build Instructions
To: Implementation AI Agent From: Lead Architect (Manus) Project: LBK Cleaners Automation & Operations Build Objective: Execute the final build, integration, and testing of the LBK Cleaners GHL CRM, Voice AI, SMS Bot, and Lovable website connection based on the locked-in architectural blueprint.
1. Project Overview & Research Context
LBK Cleaners is a residential cleaning service operating in Lubbock, TX (Service areas: Lubbock, Wolfforth, Idalou, Slaton). The business model is built on full upfront payment, a three-tier service structure (Move In/Out, Standard, Deep Cleaning), and a highly automated customer journey.
Key Research Findings Informing the Build:
1. Competitive Landscape: No local competitor in Lubbock currently offers a selfserve instant quote calculator, automated booking, or AI-powered follow-up. This is the primary competitive advantage.
2. Reference Model: The booking flow is modeled after DallasMaids.com — a clean 3step flow (Contact → Quote → Payment) with returning customer phone recognition.
3. Pricing Strategy: The pricing matrix is already live on lbkcleaners.com. Base
standard clean is 125, withadd − onsf orbedrooms(+19/10)andbathrooms(+30).
Deep cleaning applies a ~1.7x multiplier. 4. Discount Structure: Industry standard recurring discounts have been adopted:
Weekly (20%), Bi-Weekly (15%), Monthly (10%). 5. Payment Architecture: Square is the sole payment processor. All jobs require full
upfront payment (including a 3.25% Square fee + tax). No partial deposits.

2. Current State: What Is Already Built
The following components have already been successfully built and deployed into the GHL account (Location ID: rJ9T0C5AHlIdftWdXgoE ):
1. Location Settings Updated: Address set to Lubbock, TX; Timezone set to America/Chicago (CST).
2. Custom Fields Created: contact.how_did_you_hear_about_us (Single Options: Google Search, Google Maps, AI, Angi, BBB, Cleaning for a Reason, Social Media, Referral, Yard Sign, Other) contact.service_frequency (Single Options: Weekly, Bi-Weekly, Monthly, One-Time) contact.has_left_google_review (Single Options: Yes, No) contact.supply_check_submitted_today (Single Options: Yes, No) contact.parking_instructions (Text) contact.last_service_date (Date) contact.total_jobs_completed (Numerical)
3. Custom Fields Updated: contact.cleaning_type updated to: Move In/Out Cleaning, Standard Cleaning, Deep Cleaning.
4. Phone Number: (844) 717-CLEAN is active and assigned to the GHL account. 5. Payment Processor: Square is connected and active.
3. Execution Plan: What You Need to Build
You are tasked with building the remaining infrastructure. Execute the following in order:

Phase 1: GHL Pipeline Construction
The previous attempt to build the pipeline failed due to token scope limitations. You must build the “LBK Cleaners — Client Journey” pipeline with the following 9 stages:
1. New Lead 2. Quote Viewed 3. Booking Initiated 4. Booked & Paid 5. Service Scheduled 6. Service Completed 7. Review Requested 8. Recurring Active 9. Lapsed
Phase 2: Lovable ↔ GHL Integration
Connect the Lovable website to GHL using the private integration token.
Webhook/API Trigger: When Step 1 of the Lovable form is submitted, create a contact in GHL and place them in Stage 1 (New Lead). Quote Sync: When the quote is generated, update the contact’s custom fields (Bedrooms, Bathrooms, Sq Ft, Cleaning Type). Payment Sync: When Square processes the upfront payment, move the contact to Stage 4 (Booked & Paid).
Phase 3: Voice AI (Lena) Configuration
Configure the GHL Voice AI agent (Name: Lena, Female voice, warm/professional tone).
Business Hours: Mon–Fri 8am–7pm, Sat 9am–4pm. Transfer Rule: Lena handles all quotes, bookings, and questions. She ONLY transfers to the owner (806-781-8495) during business hours if the caller persistently requests a live person.

After-Hours Rule: No transfers. Lena takes a message, GHL transcribes it, saves it to contact notes, texts the transcription to the owner, and creates a callback task.
Phase 4: SMS Bot & Automations
Build the following 5 SMS workflows (All messages sent from “Lena”): 1. Abandoned Quote: Fires 30 mins after Stage 1 if not moved to Stage 4. Follow-up at 24 hours. Max 2 touches. 2. Booking Confirmation: Fires instantly on Stage 4 entry. Reminder at 24 hours before, and “On our way” at 2 hours before. 3. Review Request: Fires 2 hours after Stage 6 (Service Completed). Condition: Only fire if contact.has_left_google_review == “No”. 4. Recurring Check-in: Fires monthly for contacts in Stage 8. 5. Lapsed Reactivation: Fires twice a month for contacts in Stage 9. No discounts offered. Holiday-aware.
Phase 5: Google My Business (GMB) Completion
The GMB profile needs to be completed and connected to GHL. Action: Connect the LBK Cleaners GMB profile to GHL Reputation Management. Content to Push: Add business description, full services list (Move In/Out, Standard, Deep), and hours.
4. Required Connectors & Credentials
You will need the following to execute the build: GHL Private Integration Token: pit-7b7eba41-46b5-4a59-b6ad-55be4cde581f GHL Location ID: rJ9T0C5AHlIdftWdXgoE Lovable Private Integration Token: pit-e026c588-b8e3-4285-a2e0-
4de1b830e518
Owner Phone Number (for transfers/alerts): (806) 781-8495

Note: Ensure the GHL token has the Opportunities/Pipelines scope enabled before attempting Phase 1.
5. Testing & Verification Protocol
After building, you must execute the following tests to verify the architecture:
1. Form Submission Test: Submit a test lead via Lovable. Verify contact creation in GHL and placement in Stage 1.
2. Payment Webhook Test: Simulate a Square payment. Verify contact moves to Stage 4 and the Confirmation SMS fires.
3. Voice AI Test: Simulate an inbound call during business hours. Request a live person and verify the transfer routes to (806) 781-8495.
4. After-Hours Voicemail Test: Simulate an after-hours call. Leave a voicemail and verify the transcription SMS is sent to the owner and a task is created.
5. Review Logic Test: Move a test contact to Stage 6 with has_left_google_review set to “Yes”. Verify the review SMS does not fire.
Proceed with the build immediately upon receipt of this brief. Report back with testing results upon completion.


