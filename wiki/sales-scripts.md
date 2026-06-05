---
name: sales-scripts
type: concept
tags: [sales, scripts, nepq, acquisition, leasing]
sources: [nepq-aged-leads-script.md, low-equity-agent-script.md, tenant-script.md, copy-of-black-book-for-real-estate-investors.md, vince-master-booklet.md]
updated: 2026-06-03
---

# Sales Scripts

**Summary**: The library of phone/outreach scripts used across [[wih]] acquisition, leasing, and capital-raising — mostly built on the NEPQ (problem-centered questioning) methodology.

**Sources**: nepq-aged-leads-script.md; low-equity-agent-script.md; tenant-script.md; copy-of-black-book-for-real-estate-investors.md; vince-master-booklet.md

**Last updated**: 2026-06-03

---

Scripts feed the [[ghl]]-based outreach and AI agents (e.g. [[vince-ai]]). All route through [[mostafa]] for outbound execution per SOP. The dominant framework is **NEPQ** — connection, situation, problem awareness, solution awareness, needs/anchor, consequence, commitment, deal killers, stress test, transition to close, presentation.

## Acquisition scripts
- **NEPQ Aged Leads Script** — works aged seller leads through the full NEPQ flow; anchors offers at ~80% of need and presents at 90–95% of actual offer; includes a "Market Max Program" hybrid-listing fallback (source: nepq-aged-leads-script.md).
- **Low Equity Agent Script** — calls listing agents to pitch [[subject-to]] deals (pay seller's equity, cover commission/closing, remove mortgage from DTI); extensive rebuttal tree; books a call with Josh via GHL LeadConnector links; SMS "YES" confirmation trigger (source: low-equity-agent-script.md).
- **NEPQ Black Book for Real Estate Investors** — the full reference question bank for cold/inbound/outbound seller calls (source: copy-of-black-book-for-real-estate-investors.md).

## Leasing script
- **Tenant Script** — inbound prospective-tenant qualification: move-in timing, pets (max 2, none over 50 lbs without service-animal docs; $199/pet deposit + $20/mo), occupancy (max 2 people/bedroom + child), then routes to application or tour (source: tenant-script.md). Feeds [[property-management]] / [[doorloop]].

## Capital raising
- **Vince Master Booklet** — script/knowledge base for the [[vince-ai]] PML/TL qualification bot (source: vince-master-booklet.md). See [[vince-ai]].

## Wholesale agent-outreach & MLS scripts (2026)

A second script family, distinct from the NEPQ **seller-facing** scripts above — these are **agent-facing**, built for the AI-automated [[wholesale]] machine ([[agent-outreach]], [[mls-two-call-closing]], [[no-fluff-model]], [[disposition]]):

- **Matt Beard agent-outreach opener + objection bank** — the direct-to-agent cold opener and rebuttal library; never positions as "investor" (source pages: [[source-ultimate-agent-outreach-script]]).
- **Hieu's direct-to-agent texting + discovery sequence** — the $1.3M direct-to-agent texting flow and discovery questions ([[source-hieu-1-3m-process]]).
- **Alex Martinez 15-part MLS discovery + close call** — the on-market two-call closing script ([[source-this-exact-wholesale-script-1-2m]], [[source-agent-script-freescript]], [[source-start-wholesale-2026]]).
- **Triple-dial follow-up cadence** — the persistent multi-touch dial sequence ([[source-wholesaling-follow-up-strategy]]).
- **5-day dispo Magic-Question / FOMO templates** — buyer-side disposition messaging ([[source-selling-wholesale-easier]]).

**Key reusable rule:** *finish every objection answer with a question* — keep the prospect talking and surrender control of the call back to the script.

## RTO outreach scripts (text-based, via wih-app / Twilio)

Built from the R2OC FAQ and RTO terms (see [[rent-to-own]]). Used by Mostafa and eventually automated via the wih-app AI layer.

### Initial blast SMS (attach front-of-house photo as MMS)
Joshua's actual voice — casual, paragraph-spaced, personal, conversational close:

> Hey [First Name], it's Vince.
>
> I saw you're on our rent-to-own list and wanted to personally reach out, we just got a home available that I think could be a great fit for you.
>
> It's a [BEDS] bed / [BATHS] bath on [STREET] here in Lubbock.
>
> $[OPTION_FEE] deposit to lock it in and $[MONTHLY]/mo.
>
> Here's the link with all the pictures and details:
> rent2owncribs.com/property/[SLUG]
>
> Is this something you'd want to come check out?

Style rules: paragraph break between every point. First name + "it's Vince." opener (period, not exclamation). No exclamation marks anywhere. No dashes, use commas instead (hyphenated words like "rent-to-own" are fine). End with open question. Medium length. Feels like a real person sent it.

### RTO FB Inbound Script — Hard Rules (Non-Negotiable)

These rules govern every conversation. Missing any one of them breaks the flow.

**1. Standard qualification order: Income → Program Preference → M'kenzy**
Ask income (S8) first. After income is confirmed, ask program preference (S7). Then offer M'kenzy's call.
*Exception:* If the conversation has been about payments or deposits (S5 territory), ask program preference first, then income — you're already in that discussion.

**2. M'kenzy is earned, not offered**
Never schedule, offer, or imply a booking until income is confirmed. You may tease ("M'kenzy can go deeper on that on the call") but must qualify before booking. Sequence: answer → income → M'kenzy.

**3. Credit is never the qualifier — income is**
Never ask about credit. Never disclose the 520 internal floor. Always say: "No credit minimum — our program is income-based." Route edge cases (low credit + strong income) to M'kenzy. She makes the final call.

**4. Never reveal the income threshold until disqualification**
In Step 2A (probing for other income): say "that's a little off" only — no dollar amounts. The threshold ($3× monthly payment) is only revealed at Step 3A when disqualifying.

**5. End every answer with a question**
Never let a response be a dead end. After answering any question, ask the next qualifying question or redirect back to the lead. They should always have something to respond to.

**6. Spec objections — probe before closing**
When a lead says the home isn't a fit (wrong area, wrong beds, etc.): probe for specifics immediately → round up with "anything else you're looking for?" → then qualify income before closing out.

**7. Accept income answers directly — don't probe the answer**
When a lead directly answers the income question, accept it. Do not question their answer with "is that your budget or what your income allows?" — that probe is only for budget-range discussions, not after a direct income answer. If income is too low: ask for other household income sources (Step 2A). If still insufficient, proceed to disqualification.

**8. Facebook group close — every non-M'kenzy conversation**
Every conversation that does not end in a M'kenzy booking closes with the Facebook group link. No exceptions — disqualifications, wrong specs, not interested, wrong timing, no matching property.

**9. Income capture — universal**
If no income is on file at the end of any conversation, ask once before closing. Do not push if they won't share.

**10. Email capture — before confirming the booking time**
Ask for email BEFORE saying "I'll schedule you for [TIME]." Only if no email on file. Optional — do not pressure.

**11. No-reply cadence**
24hr → first follow-up (same property, casual nudge). 48hr → second follow-up ("still looking?"). Still no reply → passive re-engagement (Facebook group + future blasts). If they give a future timeline, tag it and note for re-engagement.

---

### Scenarios

---

**S1 — Lead asks if home is available**
> Yes this home is available, would you be interested?

---

**S2 — Home is under contract**
> So we just went under contract with this home today. We do have other homes available — were you only interested in this one?

---

**S3 — Lead asks about a bedroom count we don't have / wrong area or specs**
> We don't have a property within those specs as of now. However, would you like me to keep you informed when we do?

*If yes:* Probe for specifics before closing out — follow this sequence:
1. Ask what area they're looking in (if area is the issue) or how many beds/baths (if specs are the issue)
2. After they answer, ask: "Is there anything else you're looking for in a home?"
3. Then qualify income: "Just so I can match you to the right home — do you know approximately how much your household brings in per month?"
4. Note income, tag max payment (income ÷ 3), and keep on buyers list
5. Close with Facebook group link

*Phone number:* SMS flow — number already known. Facebook Marketplace flow — add "What's a good number for you?" after step 1.

---

**S4 — Lead asks about SF payments**
> Principal & Interest: $[P&I]
> Taxes & Insurance (estimated): $[T&I]
> Total: $[TOTAL]
>
> Your final payment would depend on how much your home insurance policy would be.

Then include one unanswered question: income (S8 Step 1) OR program preference (S7).

---

**S5 — Lead asks if more down lowers payment**
> So the monthly payments are based on the remaining balance after your down payment. To decrease the payment $200–$300 for instance would take around 20–30% down — on this home that's around $[20% of sell price] to $[30% of sell price]. That's not something we require. For this home, Rent to Own is $[RTO_DEPOSIT] down and Seller Finance is $[SF_DOWN] down. Are you leaning towards Rent to Own or Seller Finance?

*For 4513 48th St:* 20% = $50,000 | 30% = $75,000 | RTO deposit = $9,200 | SF down = $20,400

After program preference is answered → go to income (S8 Step 1).

---

**S6 — Lead asks difference between SF and RTO**
> So Rent to Own is leasing with the option to purchase the home later. The term is 3 years. You don't own the home yet, however you have equitable title where you have the right to buy.
>
> Seller Finance is when you own the title. The term is 30 years. At this point we are the lender and you are the borrower, and you are paying the home off through payments.

Then include one unanswered question: income (S8 Step 1) OR program preference (S7).

---

**S7 — Verify which program the lead wants**
> Are you leaning towards Rent to Own or Seller Finance?
>
> Rent to Own is $[RTO_DEPOSIT] ([RTO_%]) down
> Seller Finance is $[SF_DOWN] ([SF_%]) down
> Payments are $[MONTHLY]/mo ([RATE]% interest — taxes and insurance included)

*For 4513 48th St:* RTO $9,200 (3.7%) | SF $20,400 (8.2%) | RTO payment: $2,525/mo | 8.5%

**Note on SF monthly payment:** SF payment is different from RTO — the down payment reduces the loan, so P&I is lower. Present SF payment as an estimate since insurance varies by policy and exact taxes must come from LCAD. Say: "approximately $[SF_ESTIMATED]/mo — taxes and insurance are included but insurance is an estimate until you have your own policy." M'kenzy will give the exact figure on the pre-qual call.

*For 4513 48th St SF estimate:* Loan $229,600 | P&I ~$1,765 | Taxes (exact from LCAD — see Mostafa task) | Insurance ~$350 est. | **Total est. ~$2,115 + exact taxes**

---

**S8 — Income qualification**

**Step 1 — Ask income:**
> So our program is an income-based approval. Do you know approximately how much per month your household brings in?

**Step 2A — Income too low (below 3× monthly payment):**
> So that's actually a little off from what we look for on this home. Are there any other sources of income? Maybe a spouse or partner? We do verify this, however I want to be sure that I understand.

**Step 3A — Denial: reveal threshold + offer a different home (income qualifies for $1,400+/mo but not current property):**
> So for this home we are looking for households earning at least $[3× PAYMENT] per month — that's 3 times the monthly payment. Your income is a little short of that, however we do have another home that may be a better fit. Would you like me to send you the details?

**Step 3A-MIN — Income below $1,400/mo floor (income < $4,200/mo — can't qualify for anything in portfolio):**
Before disqualifying, probe to see if they can stretch:
> So just to make sure I understand — are you specifically looking for something around that payment range, or is that just what your income allows right now?

*If they say they want something cheap AND income confirms they can't qualify for $1,400/mo → Step 4A-MIN.*
*If they say they'd be open to more, reveal what they could qualify for:*
> Based on your income you could qualify for a home up to about $[income ÷ 3]/mo. If we found something in that range that worked for you, would that be something you'd be open to?
*If yes → keep on buyers list, note expanded max payment. If no → Step 4A-MIN.*

**Step 4A — Denial: no qualifying home available (income qualifies for $1,400+ but no matching property):**
> I totally understand, feel free to join our Facebook community since we do post other homes that we have there.
>
> https://www.facebook.com/share/g/1AsARPmnAf/?mibextid=wwXIfr
>
> I look forward to seeing you in there.

**Step 4A-MIN — Hard disqualification (income can't reach $1,400/mo floor, no path to expand):**
> I totally understand, feel free to join our Facebook community since we do post other homes that we have there.
>
> https://www.facebook.com/share/g/1AsARPmnAf/?mibextid=wwXIfr
>
> I look forward to seeing you in there.
>
> **[Internal: tag contact "do not send properties" — keep on buyers list for future re-engagement campaigns. Do NOT remove from list.]**

**Minimum payment floor: $1,400/mo** — income required: $4,200/mo (3×). No WIH property is currently priced below this. Any lead whose income can't reach $1,400/mo goes to Step 3A-MIN regardless of which property they're inquiring about.

**Step 2B — Income approved: affirm, transition, offer times:**
*(Affirm their income looks good. Frame the call as the next step before meeting in person. Assume the sale — go straight to times, don't ask if they want to book.)*
> So your income looks good. M'kenzy will jump on a quick call with you to go over everything before you guys meet. She's available today at 10:30am, 2:00pm, and 4:30pm. Which of those works best for you?

**Step 2B rebuttal — lead says they want to see the house instead of a call:**
> M'kenzy can get you all set up — she's available today at 10:30am, 2:00pm, and 4:30pm for a quick call. Which of those works best for you?

**Step 3B — Offer meeting times (if Step 2B needs a second push):**
*(SMS flow — phone number already known. Facebook Marketplace flow — add "Also what's a good number for her to reach you?" at the end.)*
> So M'kenzy is available today at 10:30am, 2:00pm, and 4:30pm for a quick call. Which time works for your schedule?

**Step 4B — Confirm meeting:**
> Perfect, I'll schedule you guys for [TIME]. You'll receive a text reminder leading up to the meeting.
>
> This part is important — here is a video explaining how our program works:
> https://rent2owncribs.com/how-it-works
>
> M'kenzy will be referring to this video on the Pre-Qualification call. Could you watch this prior to the meeting?

**Universal — Email capture (applies across all scenarios):**
Sent BEFORE Step 4B (before confirming the time), if no email is on file. Optional for the lead — do not pressure.
> Before I go ahead and get this scheduled, what's a good email for you? Just for scheduling purposes.

**Universal — Income capture (applies across all scenarios):**
If no income is on file by the end of the conversation, ask before closing out. Ask once — do not push if they won't share.
> Do you mind if I ask how much your household brings in per month? Just helps us make sure we find the right fit for you.

**Universal — No-reply follow-up after Step 4B:**
If the lead does not respond to the Step 4B message within 2 minutes, send this as a standalone follow-up:
> Just locking you in for [TIME]. Don't forget to watch that video before the call — it'll make a big difference.

**Universal — Lead day-of reminder (1 hour before M'kenzy call):**
> Hey [Name], just a reminder you're scheduled with M'kenzy today at [TIME]. The call is only 10–15 minutes — she just wants to make sure everything lines up before you meet. Don't forget to watch this beforehand:
> https://rent2owncribs.com/how-it-works

**Universal — Facebook group close (applies across all scenarios):**
End every conversation with the Facebook group invite if it hasn't been sent yet. Keeps the close warm and non-abrupt. Send AFTER any disqualification message, any "keep you in the loop" wrap-up, or any close that doesn't route to M'kenzy.
> In the meantime, feel free to join our Facebook community — we post all our available homes there too:
> https://www.facebook.com/share/g/1AsARPmnAf/?mibextid=wwXIfr

---

## M'kenzy briefing & reminder protocol

Triggered every time a lead books a pre-qual call with M'kenzy.

**Calendar:** Create a 30-minute event on Joshua's calendar. Add M'kenzy and the lead as guests.

**Immediate booking confirmation (text to M'kenzy):**
> Hey M'kenzy, pre-qual booked. [NAME] at [TIME] for [PROPERTY ADDRESS]. Income: $[X]/mo | Leaning: [RTO/SF] | [any notes from convo].

**Countdown reminders to M'kenzy:**
- **15 min out:** "Pre-qual with [Name] in 15."
- **10 min out:** "10 minutes — [Name] for [ADDRESS]."
- **5 min out:** Full brief (see below)
- **2 min out:** "2 minutes — [Name] is about to call."

**M'kenzy 5-minute full brief:**
> Pre-qual in 5 — here's everything:
>
> **Property:** [ADDRESS] | [BEDS]/[BATHS]
> **Sell Price:** $[X] | Rate: [X]%
> **RTO:** $[RTO_DEPOSIT] down | $[RTO_PAYMENT]/mo
> **SF:** $[SF_DOWN] down | ~$[SF_PAYMENT]/mo (est.)
> **P&I:** $[X]/mo | Taxes: $[X]/mo | Insurance: ~$350/mo
>
> **Lead:** [NAME] | Income: $[X]/mo | Leaning: [RTO/SF]
> [Any other notes — household size, questions asked, concerns mentioned]

---

**S10 — Lead says they're not interested**
> I totally get it. Just out of curiosity, is it the home itself, the area, or the payments?

- If **area or specs** → S3 flow: probe specifics → "anything else?" → qualify income → keep on list → Facebook group close
- If **payments** → S11 flow below
- If **flat no / general** → acknowledge, close with Facebook group link, tag on buyers list

---

**S11 — Too expensive (deposit or payment)**
> I hear you. Just so I can figure out what would actually work for you — do you know approximately how much your household brings in per month?

Then run S8. If they qualify for a different home, offer it. If below floor, go to S4A-MIN. Do not ask them to name a budget — income tells you what they qualify for.

---

**S12 — Need to think about it / talk to partner**
> Of course. Do you have a general idea of your household income? Just want to make sure it's a fit before you have that conversation.

- If income qualifies → affirm income looks good → send how-it-works video → ask when they'll have that conversation → follow up at that time
- If income doesn't qualify → S8 disqualification flow

*Follow-up timing:* Reach back out 30 minutes after the time they gave you. If no response → follow up next morning → then passive.

---

**S13 — No reply to initial blast**
- **24 hours:** Follow up once — same property, casual nudge:
  > Hey [First Name], just wanted to make sure you saw this. Still have the 4 bed / 2 bath on 48th St available — $9,200 down, $2,525/mo. Is this something you'd want to check out?
- **48 hours (still no reply):** Second follow-up — softer, check timing:
  > Hey [First Name], just checking in — are you still in the market for a home? No worries if your situation has changed, just don't want to keep reaching out if the timing's off.
- **If they respond with a future timeline** (e.g., "next year"): acknowledge, tag timeline, keep on buyers list, close with Facebook group link. Schedule re-engagement for that period.
- **Still no reply after second follow-up:** Close with Facebook group link → move to passive re-engagement (future blasts only).

---

## Rescheduling protocol

Either the lead or M'kenzy may request a reschedule.

**When lead reschedules:**
> No problem, I'll check with M'kenzy and confirm a new time with you shortly.

Text M'kenzy immediately with the rescheduling request. Follow up every 30 minutes, up to 3 times.

**If M'kenzy doesn't respond after 3 follow-ups:**
- Create a task for Mostafa to reach M'kenzy directly
- Add to Joshua's next-day task board: "M'kenzy hasn't confirmed rescheduled time for [NAME] — [PROPERTY]"
- Do NOT text Joshua immediately; escalate only if unresolved by next morning

**When M'kenzy reschedules:** Notify the lead immediately with new time options; confirm both parties before closing the loop.

---

**S9 — Lead requests to be removed from the list**
> No problem at all. I'll go ahead and get you removed. If you ever change your mind, you're always welcome back. Take care!

**[Internal: Remove contact from RTO list. Do NOT re-add to future blasts.]**

## Related pages
- [[wih]]
- [[wholesale]]
- [[subject-to]]
- [[vince-ai]]
- [[property-management]]
- [[ghl]]
- [[mostafa]]
- [[agent-outreach]]
- [[mls-two-call-closing]]
- [[no-fluff-model]]
- [[disposition]]
