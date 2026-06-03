# LBK_Cleaners_Final_10_Questions

*(Converted from local file `LBK_Cleaners_Final_10_Questions.pdf` by the local-files connector on 2026-06-03.)*

---

LBK Cleaners — Final Architecture Q&A Response
To: Implementation AI Agent (Builder) From: Lead Architect (Manus) Project: LBK Cleaners — Full Automation & Operations Build Document Purpose: Comprehensive answers to the final 10 edge-case and operational questions to complete the system architecture.
1. Timezone Handling
Decision: The system should assume all times are Central Daylight Time (CDT) / Central Standard Time (CST), which is the local time in Lubbock, Texas. Implementation: Do not attempt to detect the user’s local timezone and convert it. If someone is booking from California for a move-in clean in Lubbock, they need to see the available slots in Lubbock local time. The booking UI should explicitly state “All times are Central Time (CT)” next to the time picker to prevent confusion.
2. Multi-Property Bookings
Decision: One address per booking. Implementation: The system architecture is built around a 1:1 relationship between a booking event, a property address, and a specific time slot. If a customer owns a rental and a primary home, they must complete two separate checkout flows. This ensures accurate pricing (since sqft/beds/baths differ) and prevents scheduling conflicts.
3. Booking Modification After Payment
Decision: Manual modification via Joshua/Lena. Implementation: If a customer pays and then wants to add an add-on (e.g., inside the oven), they do not need to cancel and rebook. They can text the business number. Lena (the AI) or Joshua will acknowledge the request, update the appointment notes in GHL, and Joshua will manually send a Square payment link for the difference (e.g., $35 for the oven). Do not build a complex self-serve modification portal for post-payment add-ons right now.

4. No-Show / Lockout Policy
Decision: $50 Lockout Fee, manually enforced. Implementation: If the cleaner arrives and cannot access the property within 15 minutes of the arrival window, they notify Joshua. Joshua attempts to call the customer. If unreachable, the cleaner leaves. Joshua manually charges a $50 lockout fee via Square (using the card on file) to cover the cleaner’s time and gas. The system does not auto-handle this; it requires human judgment.
5. Service Area Validation (Zip Codes)
Decision: The booking form should validate against a hardcoded list of approved zip codes. Implementation: If a user enters a zip code not on this list, the form should display: “We’re sorry, we don’t currently service that area. Please call us at (844) 717CLEAN to see if we can make an exception.”
Approved Zip Code List:
Lubbock: 79401, 79402, 79403, 79404, 79405, 79406, 79407, 79408, 79409, 79410, 79411, 79412, 79413, 79414, 79415, 79416, 79423, 79424, 79430, 79452, 79453, 79457, 79464, 79490, 79493, 79499 Wolfforth: 79382 Idalou: 79329 Slaton: 79364
6. Photo Storage (Before/After Photos)
Decision: Google Drive integrated with GHL. Implementation: For the future build, cleaners will upload photos via Connecteam or a custom app. Those photos should be routed via Zapier/Make to a specific Google Drive folder organized by [Customer Name] - [Date] . A link to that specific Google Drive folder should be automatically pasted into a custom field in the GHL contact record (e.g., contact.photo_folder_link ). Do not store raw image files directly inside GHL custom fields, as it clutters the CRM and consumes storage limits quickly.

7. Duplicate Contact Handling
Decision: Deduplicate by Phone Number primarily. Implementation: In GHL Settings > Business Profile > Contact Deduplication Preferences, turn “Allow Duplicate Contact” OFF. Set the primary search preference to Phone and the secondary to Email.
If a customer books with a new email but the same phone number, GHL will update the existing contact record with the new email. If a customer books with a new phone number but the same email, GHL will update the existing contact record with the new phone number. This prevents pipeline clutter and keeps conversation history unified.
8. Gift Certificates / Gift Bookings
Decision: Not supported in the automated flow right now. Implementation: Do not build a “Buy as a Gift” toggle on the website. If someone wants to buy a cleaning for someone else, they must call or text. Joshua will manually generate a Square Digital Gift Card link and send it to them. The recipient can then book online and use the Square gift card code at checkout.
9. Seasonal Demand
Decision: Flat pricing year-round. Implementation: While the cleaning industry sees spikes in Spring (March/April) and Holidays (Nov/Dec), LBK Cleaners will maintain consistent pricing year-round to build trust. Do not build surge pricing or dynamic pricing algorithms. The GHL calendar capacity limits (2-3 jobs/day) will naturally cap the schedule during busy seasons.
10. Insurance & Bonding
Decision: Yes, display trust signals prominently. Implementation: LBK Cleaners must carry General Liability Insurance and a Janitorial Surety Bond (standard for Texas cleaning businesses). The Lovable website should prominently feature a badge or text in the footer and near the checkout button stating: “Fully Insured & Bonded for Your Peace of Mind.” This is a critical conversion trust signal for residential services.
End of Document


