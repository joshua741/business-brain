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

### RTO FB Inbound Script — 8 Scenarios

**No credit score question. Income is the primary qualifier. Always work in program preference (S7) and income (S8) if not yet answered.**

**Handling questions:**
- If the answer is known: give it briefly, then move to qualifying the lead (S8).
- If the answer is unknown or not documented: don't guess — you can mention M'kenzy can go deeper on the qualification call, then immediately pivot to qualifying them.
- **M'kenzy's call is only offered AFTER income qualification is confirmed.** Never schedule or offer M'kenzy's call before qualifying. You can tease it ("M'kenzy can cover that further on the qualification call") but you must then qualify them before booking.
- Sequence: answer question → qualify (S8) → offer M'kenzy's call.

---

**S1 — Lead asks if home is available**
> Yes this home is available, would you be interested?

---

**S2 — Home is under contract**
> So we just went under contract with this home today. We do have other homes available — were you only interested in this one?

---

**S3 — Lead asks about a bedroom count we don't have**
> We don't have a property within those specs as of now. However, would you like me to keep you informed when we do?

*If yes:* "I'll keep a note of what you're looking for and when we have that home available we'll send you a message. What's a good phone number for you?"

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

**Universal — Facebook group close (applies across all scenarios):**
End every conversation with the Facebook group invite if it hasn't been sent yet. Keeps the close warm and non-abrupt. Send AFTER any disqualification message, any "keep you in the loop" wrap-up, or any close that doesn't route to M'kenzy.
> In the meantime, feel free to join our Facebook community — we post all our available homes there too:
> https://www.facebook.com/share/g/1AsARPmnAf/?mibextid=wwXIfr

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
