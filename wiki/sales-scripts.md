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
> So the monthly payments are based on the remaining balance after your down payment. To decrease the payment $200–$300 for instance would take 20–30% down. Complete your decision if you want to do this.

Then include one unanswered question: income (S8 Step 1) OR program preference (S7).

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

*For 4513 48th St:* RTO $9,200 (3.7%) | SF $20,400 (8.2%) | $2,525/mo | 8.5%

---

**S8 — Income qualification**

**Step 1 — Ask income:**
> So our program is an income-based approval. Do you know approximately how much per month your household brings in?

**Step 2A — Income too low (below 3× monthly payment):**
> So for this home we are looking to see that your household income is at least 3 times the monthly payment. That would mean earning at least $[3× PAYMENT] per month for this home. Are there any other sources of income? Or maybe a spouse or partner? We do verify this, however I want to be sure that I understand.

**Step 3A — Denial: offer a different home:**
> So for this home your income is not as high as we'd need it, however we have another that may be a better fit based on your income. Would you like me to send you over the details for this one?

**Step 4A — Denial: no qualifying home available:**
> I totally understand, feel free to join our Facebook community since we do post other homes that we have there.
>
> https://www.facebook.com/share/g/1AsARPmnAf/?mibextid=wwXIfr
>
> I look forward to seeing you in there.

**Step 2B — Income approved: offer pre-qual call:**
> So the next step is a Pre-Qualification call with our property manager M'kenzy. She will ask some questions as well as answer yours. Would you like to book this call?

**Step 3B — Offer meeting times:**
> So M'kenzy is available today at 10:30am, 2:00pm, and 4:30pm. Which time works for your schedule? Also what's a good number for her to reach you?

**Step 4B — Confirm meeting:**
> Perfect, I'll schedule you guys for [TIME]. You'll receive a text reminder leading up to the meeting.
>
> This part is important — here is a video explaining how our program works:
> https://rent2owncribs.com/how-it-works
>
> M'kenzy will be referring to this video on the Pre-Qualification call. Could you watch this prior to the meeting?

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
