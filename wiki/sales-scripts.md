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

> Hey [First Name], it's Josh!
>
> I saw you're on our rent-to-own list and wanted to personally reach out — we just got a home available that I think could be a great fit for you.
>
> It's a [BEDS] bed / [BATHS] bath on [STREET] here in Lubbock.
>
> $[OPTION_FEE] deposit to lock it in and $[MONTHLY]/mo.
>
> Here's the link with all the pictures and details:
> rent2owncribs.com/property/[SLUG]
>
> Is this something you'd want to come check out?

Style rules: paragraph break between every point. First name + "it's Josh" opener. End with open question — never "Reply YES/NO" or robotic command phrases. Medium length. Feels like a real person sent it.

### Response A — Interested (YES)
Qualification sequence (3 messages):
1. "That's great! Quick questions to see if you're a good fit — what's your current living situation? Renting, with family, or something else?"
2. "And roughly what's your monthly income before taxes? We need about $[2.5x monthly payment]/mo for this one."
3. "Last one — do you know your approximate credit score? We work with 520+."

→ **Qualifies**: "You sound like a great fit. Apply at rent2owncribs.com — $49.90 app fee. We'll get back to you within 24–48 hours. Ready to apply?"
→ **Doesn't qualify**: "You're a little short on [credit/income] right now, but that's fixable. Want to talk through what it would take in the next 60–90 days?"

### Response B — Not interested (NO)
1. "No problem! Can I ask — is it the price, location, or just not the right time?"
2. If timing/price: "Totally understand. Do you know anyone looking? We pay $500 referral fee if someone you send closes."
3. If fully out: "Got it. We list new properties regularly — want to stay on the list for future ones?"

### FAQ knowledge base (for question responses)
| Question | Answer |
|---|---|
| What's the down payment? | "$2,000 — credited toward your purchase price at closing. Locks in your price today." |
| Do I need perfect credit? | "Nope. 520+ minimum. Income and stability matter more than score." |
| Does rent go toward buying? | "Monthly payment mirrors a future mortgage but isn't directly credited. Your option fee is what's credited at purchase." |
| What if I can't buy at the end? | "1-year terms with annual renewals. After 12 months of on-time payments you can convert to seller financing — we carry the note, no bank." |
| Can I make changes? | "Cosmetic changes are fine. Structural changes need written approval. You're treated like an owner from day one." |
| How do I apply? | "Go to rent2owncribs.com, find [ADDRESS], and apply there. $49.90 fee. We'll review within 24–48 hours." |
| Is it still available? | "Yes, still available — moving fast. Get your application in this week." |

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
