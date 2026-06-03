# LBK_Cleaners_BookingKoala_Setup_Guide.md

*(Converted from local file `LBK_Cleaners_BookingKoala_Setup_Guide.md.pdf` by the local-files connector on 2026-06-03.)*

---

The GPS Guide: BookingKoala Setup for
LBK Cleaners
This comprehensive, step-by-step guide is designed specifically for Claude Code to execute the complete setup, auditing, and optimization of the BookingKoala CRM account for LBK Cleaners, a residential cleaning company based in Lubbock and Wolfforth, Texas. As an autonomous agent, Claude Code will be logged into the BookingKoala admin panel at lbkcleaners.bookingkoala.com/admin and must follow this guide sequentially. This document acts as a precise global positioning system (GPS), detailing exactly what to do, in what order, and what to verify at each decision point.

Executive Context and Core Rules
Before initiating any configuration, Claude Code must understand the fundamental parameters of LBK Cleaners and the operational rules of this setup.

Business Profile

LBK Cleaners is a premium, locally-owned residential cleaning service serving Lubbock and Wolfforth, Texas. The business focuses on transparent pricing, eco-friendly practices, and seamless online booking.

• Primary Phone: (806) 429-GLOW / (806) 429-4569

• Support Email: info@lbkcleaners.com (or as configured in the admin panel)

• Website: lbkcleaners.com

• Brand Colors: Dark Green ( #0F3A20 ) and Gold ( #D4AF37 )

•

Service Model Reference: Atlanta Green Maids (booking.atlantagreenmaids.com/booknow)

Core Rules of Engagement
1. The Hierarchy Rule: If a pricing input or setting is already customized in BookingKoala, it remains the absolute source of truth. Do not override existing customizations in BookingKoala with pricing from the public website or Facebook unless the setting is completely blank or explicitly marked as a temporary placeholder. If a contradiction is found, note it down in the final report for Joshua Webber, but preserve the BookingKoala customization.
2. The "Do No Harm" Rule: Auditing means verifying and completing, not destroying. Never delete existing active customer data, provider profiles, or active booking records.

3. The Notification Keep-Alive Rule: Claude Code must log progress and flag any blocking manual inputs (such as credit card numbers, private API keys, or physical phone verification codes) immediately to Joshua Webber.

Phase 1: Audit (Verify Existing Setup)
This phase requires Claude Code to systematically check every corner of the BookingKoala admin panel to establish a baseline of what has been configured and what remains blank.
Step 1.1: Audit Company Profile & General Store Options
Claude Code must navigate to Settings > General > Store Options > General and expand the Store Info section [2]. 1. Verify Business Name: Ensure the field is set to LBKCleaners . Note if the subdomain
matches lbkcleaners . 2. Verify Contact Email: Confirm the email is set to info@lbkcleaners.com (or Joshua's
primary account email). This is the address that replaces the {{.SupportEmail}} shortcode in templates [2]. 3. Verify Time Zone: Ensure the timezone is set specifically to CST6CDT (Central Standard Time/Central Daylight Time) to handle automatic daylight saving adjustments in Lubbock [2]. 4. Verify Date & Time Format: Set the Time Format to 12-hour time (e.g., 5:30 PM) and the Date Format to MM/DD/YYYY [2]. 5. Verify Phone Number: Ensure the contact phone number is entered as (806)429-4569 . The Phone Number Format must be set to (999) 999-9999 [2]. 6. Verify Accepted Forms of Payment: Ensure Credit/Debit Card is checked. If cash/check is allowed for specific commercial or family bookings, leave it enabled for admin use, but restrict the frontend to Credit/Debit Card only if Joshua wants to enforce card-on-file bookings [2]. 7. Verify Form Types Offered: Ensure Booking Forms is enabled. If Joshua wants to collect leads, Lead Forms should also be enabled [2].

Parameter Business Name Support Email Time Zone

Required Setting LBK Cleaners info@lbkcleaners.com CST6CDT

Current Status (To Be Audited) ﻿ ﻿ ﻿

Phone Number Phone Format Card-on-File

(806) 429-4569

﻿

(999) 999-9999

﻿

Required for Frontend

﻿

Step 1.2: Audit Industry and Form Selection
Navigate to Settings > Industries. 1. Identify Active Industry: Verify that a residential cleaning industry (typically named
"Home Cleaning" or "Residential Cleaning") is active. 2. Verify Form Type: Click on the industry and navigate to Settings > Form Settings [1].
Verify that Form 1 (Variables-based pricing using Bedrooms/Bathrooms/SqFt) is the default and active form [1]. 3. Disable Unused Forms: If Form 2, 3, or 4 are active but unused, click Options > Disable next to them to prevent customer confusion [1].
Step 1.3: Audit Pricing Matrix (Form 1 Pricing Parameters)
Navigate to Settings > Industries > [Industry Name] > Form 1 > Pricing Parameter [2]. 1. Check Variable Categories: Verify that three distinct categories exist: Bedrooms,
Bathrooms, and Sq Ft [2]. 2. Verify Bedroom Variables: Click Manage Variables and check the bedroom counts
(typically 1 to 6 bedrooms) [2]. Note the flat-rate base pricing assigned to each bedroom count. 3. Verify Bathroom Variables: Check the bathroom counts (including half-baths, e.g., 1, 1.5, 2, 2.5, up to 5+ baths) [2]. Note the incremental pricing assigned to each bathroom variable. 4. Verify Sq Ft Variables: Check the square footage tiers (e.g., 1-999 sqft, 1000-1499 sqft, 1500-1999 sqft, etc.). Note if they add incremental costs or are set to $0.00 (relying entirely on bedrooms/bathrooms for pricing while using Sq Ft for scheduling/timing) [2]. 5. Audit the Hierarchy Rule: Create a table of the existing pricing in BookingKoala. Compare it against the pricing on lbkcleaners.com. If there are discrepancies, do not change the BookingKoala values. Highlight them in your audit log.
Step 1.4: Audit Service Categories
Navigate to Settings > Industries > [Industry Name] > Form 1 > Service Categories [1].

1. Verify Core Services: Ensure the three primary service types are configured:

• Standard Cleaning (Base service)

•

Deep Cleaning intensive)

(Typically priced

at

a

multiplier

or

higher

base

rate,

e.g.,

1.7x

• Move-In / Move-Out Cleaning (Detailed empty-home clean)

2. Verify Category Descriptions: Ensure each category has a customer-facing description explaining what is included (e.g., Standard includes dusting, mopping, vacuuming, kitchen/bath surfaces).

Step 1.5: Audit Add-On Services (Extras)
Navigate to Settings > Industries > [Industry Name] > Form 1 > Extras [1]. 1. Check Existing Extras: Identify which add-ons are currently active. Expected add-ons
for LBK Cleaners include: • Inside Oven • Inside Refrigerator • Inside Cabinets (Empty) • Interior Windows • Deep Baseboard Detail • Wet Wiping Blinds • Load of Laundry (Wash & Fold) 2. Record Pricing & Timing: Note the price and estimated duration (in minutes) for each extra. This is crucial for smart scheduling calculations [2].

Step 1.6: Audit Service Area & Zip Codes

Navigate to Settings > Industries > [Industry Name] > Form 1 > Locations [1].

1. Identify Active Locations: Check the configured service areas. The primary locations must cover Lubbock, TX and Wolfforth, TX [1].

2. Extract Zip Codes: Document all zip codes currently assigned to these locations. The core Lubbock and Wolfforth zip codes that should be present include:

•

Lubbock: 79401, 79403, 79416, 79423, 79424

79404,

79407,

79410,

79411,

79412,

79413,

79414,

79415,

• Wolfforth: 79382

3. Verify Travel Fees: Note if any location has a travel or service fee enabled [1].

Step 1.7: Audit Payment Integration Status (Square)
Navigate to Settings > General > Store Options > Admin and scroll to Connect Payment Gateways [3]. 1. Check Square Connection Status: Identify if Square is marked as "Enabled" or
"Disabled" [3]. 2. Document the Error State: The context notes an "Invalid key or no location exists"
error. Claude Code must inspect the Application ID and Secret Key/Access Token fields [1]. 3. Verify Environment: Check if the keys entered are Sandbox keys (prefixed with sandbox- ) instead of Production keys (prefixed with sq0idp- or similar).
Step 1.8: Audit Frequency Discounts
Navigate to Settings > Industries > [Industry Name] > Form 1 > Frequencies [2]. 1. Verify Configured Frequencies: Ensure the following frequencies are set up:
• One-Time (No discount) • Weekly • Bi-Weekly (Every 2 weeks) • Monthly (Every 4 weeks) 2. Note Existing Discounts: Record whether discounts are flat rates or percentages, and whether they apply to the first booking or only subsequent bookings [2].
Step 1.9: Audit Team & Staff Profiles
Navigate to the Providers section from the main dashboard [1]. 1. List Active Providers: Document any test or real provider accounts. 2. Check Provider Settings: Verify if providers are assigned to specific locations,
frequencies, or service categories [1] [2].
Phase 2: Complete Setup (Configuration Blueprint)
This phase outlines the exact steps Claude Code must take to resolve errors, complete unconfigured settings, and optimize the BookingKoala platform for live operations.
Step 2.1: Resolve Square Payment Integration Error

The "Invalid key or no location exists" error occurs when BookingKoala cannot validate the Square credentials against a live Production merchant location [1].
Plain Text
[Square Developer Dashboard] ---> Copy Production App ID & Access Token | v
[BookingKoala Admin] -------------> Paste Keys & Click "Get Locations" | v
[Select Location] ----------------> Link Default Location & Save
1. Access Developer Portal: Instruct Joshua to provide the Production credentials from the Square Developer Dashboard [1].
2. Verify Credentials Type: Ensure the credentials are Production, not Sandbox. Production Access Tokens begin with EAAA... and Application IDs begin with sq0idp-... .
3. Input Credentials: Go to Settings > General > Store Options > Admin > Connect Payment Gateways [3]. Toggle the payment processor to Enabled [1]. Click the Square tab, paste the Application ID and Secret Key (Access Token), and click Save [1].
4. Retrieve Square Locations: Click the blue Get Locations button [1]. This pulls the physical business locations configured in the Square merchant account.
5. Map Locations: Select the primary Lubbock/Wolfforth location from the dropdown and link it to the BookingKoala default location [1]. Click Save [1].
6. Verify Location Mapping: Navigate to Settings > Industries > [Industry Name] > Form 1 > Locations [1]. Click Options > Edit next to the Lubbock/Wolfforth location [1]. Proceed to the second page ("Setup Square account") and verify it is set to No, Use Default (or map it to the specific Square location if custom accounts are needed) [1].
Step 2.2: Configure Lubbock & Wolfforth Service Area
Ensure the physical boundaries of the service area are correctly mapped to prevent out-ofrange bookings. 1. Edit Location: Go to Settings > Industries > [Industry Name] > Form 1 > Locations
[1]. Click Options > Edit next to the primary service area [1]. 2. Define Zip Codes: In the Primary zip/postal codes box, paste the following comma-
separated list exactly (ensuring no spaces) [1]:
79382,79401,79403,79404,79407,79410,79411,79412,79413,79414,79415,79416,79423,79424

3. Configure Travel Fees: If travel fees are required for Wolfforth (which is slightly outside Lubbock), create a separate location named Wolfforth and assign zip code 79382 to it [1]. Set a flat Service Fee of $15.00 for this location [1]. For the main Lubbock location, set the Service Fee to $0.00 [1].
4. Set Sales Tax: In Texas, residential cleaning services are subject to state and local sales tax (8.25% total in Lubbock). Ensure Do you wish to exempt sales tax is set to No [1]. Navigate to Settings > General > Taxes and set the tax rate for the Lubbock/Wolfforth locations to 8.25%.

Step 2.3: Configure Frequency Discounts

Set up the recurring booking options to incentivize ongoing service. If these are not yet customized, use the following standard industry discounts as the baseline:

1. Weekly Service: Set a 20% discount [2].

2. Bi-Weekly Service (Every 2 weeks): Set a 15% discount (Most Popular) [2].

3. Monthly Service (Every 4 weeks): Set a 10% discount [2].

4. Configuration Steps:

• Go to Settings > Industries > [Industry Name] > Form 1 > Frequencies [2].

• Click Options > Edit (or Add New if missing) [2].

• Set Set occurrence time to Recurring and select the appropriate interval [2].

• In the Discount field, enter the percentage (e.g., 20 for Weekly) and select % [2].

•

Check Exclude first appointment and use original one-time job length to ensure the initial deep/detailed clean is charged at the full one-time rate and allocated

proper time [2].

•

Enable Charge one-time price if canceled after 1st appointment to protect margins against customers who book recurring services just to get a discount

on

a

single clean [2].

Step 2.4: Set Up Add-On Services (Extras)
Configure the pricing and time additions for the available add-ons. If blank, apply the following standard pricing and timing parameters:

Add-On Service

NCuasmtoemer-Facing Price ($)

Inside Oven

Inside Oven

$35.00

Inside Refrigerator Inside Fridge

$30.00

T(MimineuAtedsd)ition 30 mins 30 mins

Inside Cabinets

I(nEsmidpetyC)abinets

$25.00

20 mins

Interior Windows

Interior Windows (Per Window)

$5.00

10 mins

Deep Baseboard Detail Detail Baseboards $40.00

45 mins

Wet Wiping Blinds

Detail Blinds (Per Blind)

$10.00

15 mins

Load of Laundry

LFoauldn)dry (Wash, Dry, $25.00

45 mins

1. Configuration Path: Go to Settings > Industries > [Industry Name] > Form 1 > Extras [1].
2. Add Extra: Click Add New. Enter the name, price, and time (converted to hours/minutes/seconds) [2]. Ensure it is set to display on Customer frontend, backend & admin [2].
SMtoedpe2l).5: Configure Booking Form Style (The Atlanta Green Maids
LBK Cleaners wants their booking form to match the clean, step-by-step layout of Atlanta Green Maids.
Plain Text
[Step 1: Home Details] ---> Bedrooms, Bathrooms, Sq Ft, Service Category | v
[Step 2: Extras & Add-ons] -> Interactive Icons (Oven, Fridge, etc.) | v
[Step 3: Frequency] --------> One-time, Weekly, Bi-weekly, Monthly | v
[Step 4: Schedule & Info] --> Date/Time Selection, Customer Details, Payment
1. Access Website Builder: Navigate to Settings > Design Forms & Website > Website Builder & Themes and click Customize Theme [3].
2. Select Book Now Page: In the top center page menu of the builder, select the Book Now page [1].

3. Configure Step-by-Step Flow:

• Hover over the booking form element and click the Edit button [3].

•

Set the form layout scrolling page.

style

to

Multi-Step

or

Step-by-Step

rather

than

a

single

long

•

Step 1 (Select Service & Home Details): Display the Service Categories (Standard, Deep, Move-Out) and the Form 1 Pricing Parameters (Bedrooms, Bathrooms, Sq Ft

dropdowns/sliders) [1] [2].

•

Step 2 (Select icons [1].

Add-ons):

Display

the Extras

with

clear,

high-quality,

transparent

•

Step 3 (Select Frequency): Display the frequency options (One-Time, Weekly, Weekly, Monthly) with their corresponding discount badges highlighted [2].

Bi-

•

Step 4 (Schedule & Payment): Display the secure Square payment input fields [2] [3].

interactive

smart

calendar

and

the

4. Branding and Theme Alignment:

• Go to the Design menu at the top of the builder [3].

• Select Colors and enable custom colors [3].

•

Set the Primary Brand Dark Green: #0F3A20 .

Color

(Buttons,

active

states,

highlights)

to

LBK

Cleaners

• Set the Secondary/Accent Color (Badges, discount text, ratings) to Gold: #D4AF37 .

• Set the Font Family to a clean, modern sans-serif (such as Montserrat or Inter) [3].

• Click Save & Publish in the top right corner to push these design changes live [3].

Step 2.6: Configure Calendar, Availability, & Smart Scheduling
To prevent overbooking and optimize travel routes, smart scheduling must be configured. 1. Navigate to Smart Scheduling: Go to Settings > General > Store Options >
Scheduling. 2. Select Scheduling Type: Choose Smart Scheduling (which assigns jobs based on
provider locations, availability, and job duration) [1]. 3. Set Arrival Windows: Residential cleaning should use arrival windows rather than
exact times to account for traffic and varying job lengths. Set up the following standard arrival windows: • Morning: 8:00 AM - 10:00 AM • Mid-Day: 11:00 AM - 1:00 PM • Afternoon: 2:00 PM - 4:00 PM

4. Configure Buffer Time: Set a default 30-minute buffer between jobs to allow providers to travel between Lubbock neighborhoods and Wolfforth.
5. Set Cut-off Times: Prevent same-day booking surprises by setting a 16-hour booking cut-off. Customers cannot book a service online less than 16 hours before the requested start time.
Step 2.7: Configure Cancellation & Rescheduling Policies
To protect LBK Cleaners' schedule and provider earnings, establish clear automated policies. 1. Navigate to Customer Store Options: Go to Settings > General > Store Options >
Customer. 2. Expand Cancellation Settings: Locate the cancellation window settings. 3. Set 24-Hour Policy: Configure the system to charge a flat $50.00 fee if a customer
cancels or reschedules a booking less than 24 hours before their scheduled arrival time. 4. Customize Frontend Notice: Add a mandatory checkbox or clear text on the booking
form summary page stating: "I understand that LBK Cleaners enforces a 24-hour cancellation and rescheduling policy. Cancellations made within 24 hours of the service window are subject to a $50 fee."
Step 2.8: Configure Automated Notifications (Email & SMS)
LBK Cleaners requires a robust, branded sequence of confirmation, reminder, and review notifications.
Branded Email Master Template
Navigate to Settings > Notifications > Master Templates [3]. 1. Create a custom master template. 2. Set the header background color to Dark Green ( #0F3A20 ). 3. Place the LBK Cleaners logo (transparent PNG, max 225x50 pixels) in the header [2]. 4. Set the footer text to include the support phone (806)429-4569 and email
info@lbkcleaners.com [2]. 5. Apply this master template to all customer-facing emails [3].
Email 1: Booking Confirmation (Sent Immediately)
Navigate to Settings > Notifications > Emails > Customer [3].

1. Locate New Booking Confirmation and click Edit.
2. Subject Line: Your home is scheduled to sparkle! ������ Booking Confirmation #{{.BookingID}}
3. Body Copy: Warmly thank them for choosing LBK Cleaners. Display the booking summary using shortcodes: • Service Type: {{.ServiceCategory}} • Date & Arrival Window: {{.BookingDate}} at {{.ArrivalWindow}} • Home Details: {{.Bedrooms}} Bed / {{.Bathrooms}} Bath • Address: {{.CustomerAddress}} • Estimated Total: {{.BookingTotal}}
4. Include a prominent button linking to the Customer Portal where they can manage their booking.
SMS 1: Booking Confirmation (Sent Immediately)
Navigate to Settings > Notifications > SMS > Customer [3]. 1. Locate New Booking SMS and click Edit. 2. Text Content:
Hi {{.CustomerFirstName}}, your cleaning with LBK Cleaners is confirmed for {{.BookingDate}} ({{.ArrivalWindow}}). Manage your booking here: {{.CustomerPortalURL}}. Questions? Call us at 806-4294569!
Email 2: 24-Hour Reminder (Sent 24 Hours Prior)
Navigate to Settings > Notifications > Emails > Customer [3]. 1. Locate 24-Hour Booking Reminder and click Edit.
2. Subject Line: Reminder: LBK Cleaners is coming tomorrow! ������
3. Body Copy: Remind them of the upcoming service. Include a checklist of "How to Prepare" (e.g., leave a key, secure pets, pick up clutter). Remind them of the 24-hour cancellation policy to prevent last-minute lockouts.
SMS 2: 24-Hour Reminder (Sent 24 Hours Prior)
Navigate to Settings > Notifications > SMS > Customer [3]. 1. Locate 24-Hour Reminder SMS and click Edit. 2. Text Content:
Friendly reminder from LBK Cleaners! We are scheduled to clean your home tomorrow, {{.BookingDate}}, arriving between {{.ArrivalWindow}}. Please reply to this number or call 806-429-4569

if you have entry instructions.

Email 3: Post-Service Review Request (Sent 2 Hours After Completion)

Navigate to Settings > Notifications > Emails > Customer [3].

1. Locate Job Completed / Feedback Request and click Edit.

2. Subject Line: How did we do? Rate your clean! ✨

3. Body Copy: Express how much their feedback matters to a local Lubbock business. Provide direct 1-to-5 star rating links (which utilize BookingKoala's built-in feedback system).

4. Conditional Routing: Configure the feedback system so that:

•

4 or 5 Star Ratings: Automatically redirect the customer to a page thanking them and displaying direct links to LBK Cleaners' Google Business Profile and Facebook

page to publish their review.

•

1, 2, or 3 Star Ratings: Redirect the customer to a directly to Joshua Webber so he can contact them

private feedback form that goes within 24 hours to resolve the

issue under the 100% Satisfaction Guarantee.

Step 2.9: Set Up Gift Card System
Navigate to Settings > General > Store Options > Admin [3]. 1. Set Minimum Amount: Set the Minimum Gift Card Amount to $50.00 [3]. 2. Allow Dynamic Editing: Set Are you able to edit a gift card to have a total less than
its minimum requirement to No to ensure all gift cards sold online maintain a viable minimum balance [3]. 3. Configure Customer Settings: Go to the Customer tab under Store Options. Under General, locate Can customers purchase gift cards and set to Yes [3]. Set Can customers edit/reload gift cards to Yes to encourage repeat gifting [3]. 4. Populate Gallery: Navigate to Marketing > Gift Cards > Gift Card Gallery [3]. Upload custom-branded, high-quality images with dark green and gold elements for occasions like "Housewarming," "Happy Holidays," "Mother's Day," and "Just Because."

Step 2.10: Set Up Referral Program

Navigate to Settings > General > Store Options > Admin [3].

1. Define Incentives: Under the Referral section, set the default sharing incentives:

•

Referee Reward booking [3].

(The

Friend):

Enter

$20.00

in

credits

to

incentivize

their

first

•

Referrer Reward (The Advocate): Enter $20.00 in customer once the friend's clean is completed [3].

credits

to

reward

the

existing

2. Enable Sharing: Go to Settings > General > Store Options > Customer and ensure Referral Program is set to Enabled. This automatically generates a unique referral link inside every customer's dashboard [2].

SIntteepg2ra.1ti1o:nConfigure Zapier Webhooks for GoHighLevel (GHL)
Because BookingKoala does not have an open API, Claude Code must configure webhook triggers to push data to Joshua's GoHighLevel (GHL) CRM for advanced marketing automation [2].

Plain Text

[BookingKoala Event] ---> Trigger Webhook (Zapier/Make) ---> Push to GoHighLeve

1. Enable Zapier App: Navigate to Settings > General > Apps & Integrations [2]. Scroll to the Zapier box, click the blue button, and toggle the status to Enabled [2].

2. Generate API Key: Click Generate API Key and copy the unique string [2].

3. Configure Webhook Triggers: Claude Code must document the exact webhook triggers that need to be mapped in Zapier or Make to push to GoHighLevel:

•

Trigger: New Customer source-bookingkoala ).

->

Maps

to

GHL

"Create

Contact"

(Tags:

lbk-customer

,

lead-

•

Trigger: New Booking -> Maps Pipeline" (Stage: Scheduled ).

to

GHL

"Create

Opportunity"

in

the

"Booking

•

Trigger: Booking Cancelled -> Maps to GHL "Update Cancelled , triggers GHL win-back email sequence).

Opportunity"

(Stage:

•

Trigger: Booking Completed -> Maps to GHL "Update Opportunity" (Stage: Completed , triggers GHL review request and 30-day nurture sequence).

•

Trigger:
Payment

Booking Charge Declined -> Maps to GHL "Update Opportunity" (Stage: Declined , triggers GHL automated SMS alert to customer to update card).

Phase 3: Optimization & Final Checks
Before declaring the setup complete, Claude Code must run a rigorous quality assurance (QA) protocol.

Step 3.1: End-to-End Booking Flow Test

Claude Code must simulate a live customer booking on the frontend to verify pricing, math, and layout.

1. Navigate to Frontend: Go to the live booking URL (e.g., lbkcleaners.bookingkoala.com/booknow ).

2. Test Scenario 1: Standard Clean

•

Select: [2].

3

Bedrooms,

2

Bathrooms,

1800

Sq

Ft,

Standard

Cleaning,

One-Time

[1]

• Select Add-ons: Inside Oven, Inside Fridge [1].

• Verify: Does the pricing summary calculate correctly?

\text{Total Price} = \text{Base (3 Bed/2 Bath)} + \text{Sq Ft Surcharge} + $35 (\text{Oven}) + $30 (\text{Fridge})

$$

3. Test Scenario 2: Recurring Discount

• Select: 2 Bedrooms, 1 Bathroom, 1200 Sq Ft, Standard Cleaning, Bi-Weekly [1] [2].

•

Verify: Is the 15% discount applied only to subsequent cleanings, or correctly showing the full one-time price (if configured as such)? [2]

is

the

first

clean

1. Test Scenario 3: Tax Calculation

•

Verify: Is the Lubbock local sales bottom of the summary? [1]

tax

of

8.25%

being

added

to

the

final

total

at

the

Step 3.2: Notification Fire Check
Navigate to Bookings > Unassigned Bookings or Bookings > Active Bookings to view the test bookings generated during Phase 3.1. 1. Verify Logged Emails: Click on a test booking, scroll to the Logs/History or
Notifications Log section, and verify that the "New Booking Confirmation" email was queued and successfully sent to the test email address. 2. Verify SMS Log: Ensure the SMS notification log shows the corresponding Twilio text message payload.

Step 3.3: Mobile Responsiveness Audit
1. Open the booking form on a simulated mobile viewport (375px width, e.g., iPhone SE/12 Pro).

2. Verify that the bedroom/bathroom selection buttons do not overflow the screen. 3. Ensure the interactive calendar dates are easily tappable with a thumb (minimum touch
target size of 44x44px). 4. Verify that the "Book Now" sticky CTA or bottom summary button remains visible and
functional on mobile.

Master Checklist for Claude Code Execution
Claude Code must complete this checklist sequentially. Fill in the status column as each step is executed.
Plain Text

[Phase 1: Audit] ---------------------> [Phase 2: Complete Setup] -------------

- Audit Company Profile

- Resolve Square Error

- Verify Form 1 Default

- Configure Service Area

- Record Pricing & Add-ons

- Setup Frequency Discounts

- Check Square Gateway

- Build Branded Notifications

Step #

Action Item BSeocotkioinngiKnoala EOxuptecoctmede

Status

1

PAurodfiitleC&ompany SGeetnteinrgasl >>Store S12e-thtrotCimSTe6,C(8D0T6,) [ ]

Timezone

Options > General 429-4569

2

VdeerfaifuylFto&rmact1ivise

Settings > IHnodmusetrCielesa>ning > Settings

oFdotishramebrl1feodirsmdsefault;

[]

3

Epxritcraincgt amnadtraixudit

Settings > [I1nIn>dduPusrstictrriienys]g>> Form

Table of existing pBreidce/Bsath/SqFt

[]

4

Audit Service ECxattreagsories &

Settings >

Verified

Industries > [1In>dSuesrtvriyc]e>/EFxotrrmas

Standard, Deep, oMnosve-Out & Add-

[]

5

Audit Service Area Zip Codes

ISnedttuisntgrsie>s > [Industry] > Form 1 > Locations

Verified Lubbock & Wolfforth zip codes

[]

6

PAauydmiteSnqtuGaareteway

GSeetnteinrgasl >>Store Options > Admin

oIdfe"nIntivfiaeliddcKaeuys"e error

[]

7

Resolve Square IPnatyemgreantiton

Settings > GOepntieornasl >>SAtdomrein

Square slcouoccnacnteeioscsntfesudlmlya,pped [ ]

8

Configure LhuAbrbeaock/Wolffort

Settings > Industries > 1[In>dLuosctaryti]o>nFsorm

Assigned 14 zip scaoldeesst;asxet 8.25%

[]

9

Configure Frequency Discounts

Settings > Industries > [1In>dFurestqruy]e>ncFioersm

Weekly (20%), BiWeekly (15%), Monthly (10%)

[]

10

Build Add-on Pricing & Timing

ISnedttuisntgrsie>s > [Industry] > Form 1 > Extras

All 7 core extras configured with price/time

[]

11

CStoenpfiBgouorekiMnuglti- FSoetrtminsg&s >WDeebssiigten Sfotremp-sbtyy-lsetdepin [ ]

Form

> Website Builder Green/Gold

12

SSecht eUdpuSlimngart

Settings > GOScephnteieodrnauslli>>nSgtore

Arrival windows, bcuutf-foerf,fasentd 16-hr [ ]

13

Set Up CPoanliccyellation

Settings > General > Store COupsttioonmse>r

24-hr policy with afeuetoamctaivteed $50 [ ]

14

Build Email Master Template

Settings > Notifications > Master Templates

Header/Footer branded with GLoregeona/nGdold

[]

15

CCoonnffiigrmuraetion SNeotttiifnicgasti>ons > cImonmfiermdiaatteion [ ]

Emails/SMS Emails/SMS cteumstpolmatiezesd

16

Configure 24Hour Reminders

Settings > Notifications > Emails/SMS

24-hr reminder templates customized

[]

17

CReoqnufiegsutrse Review

NSeotttiifnicgasti>ons > Emails

rPaotsint-gsewrivtihcesmart [ ] Google routing

18

Configure Gift Cards & Referrals

Settings > GOepntieornasl >>SAtdomrein

Minimum $50 GC sreefte; r$r2a0l /a$c2ti0ve

[]

19

Enable GHL Zapier Integration

Settings > General > Apps & Integrations

gAePnIeKreayted; GHL webhook triggers documented

[]

20

EExnedcBuoteoEknindg-tToe-st bFrooonktienngdform

Vdeisrcifoieudntpsr,itcainxegs,, [ ] and logs

Handover and Manual Flags for Joshua Webber
Some configurations require private credentials, manual verification, or business decisions that Claude Code cannot execute autonomously. Claude Code must flag these items specifically for Joshua Webber in the final execution report: 1. Square Production Credentials: Joshua must log into his Square Developer
Dashboard, create an application, and provide the Production Application ID and Access Token [1]. Warning: Do not paste these keys into public chat channels or unsecure logs. 2. Twilio SMS Verification: BookingKoala uses Twilio for SMS notifications [3]. Joshua must provide the Twilio Account SID, Auth Token, and Twilio phone number, or complete the integrated BookingKoala phone verification process. 3. Domain Mapping (DNS Settings): To map booking.lbkcleaners.com to BookingKoala, Joshua must add a CNAME record in his domain registrar (e.g., GoDaddy, Namecheap) pointing to lbkcleaners.bookingkoala.com . 4. GHL Zapier API Key Mapping: Joshua must copy the generated BookingKoala API key and paste it into his Zapier or Make account to connect the webhooks to his

GoHighLevel account [2].
References
1. BookingKoala Help Center: How to Connect Your Square Account 2. BookingKoala Help Center: Setting Up the Store Info Section 3. BookingKoala Help Center: Setting Up Your Store Options Admin Tab 4. BookingKoala Help Center: How to Set Up Form 1 5. BookingKoala Help Center: Setting Up Frequencies for Every Form 6. BookingKoala Help Center: Setting Up Locations for Every Form 7. BookingKoala Help Center: Gift Cards Setup 8. BookingKoala Help Center: Zapier Integration Guide 9. BookingKoala Help Center: Customizing the Look of Your Forms


