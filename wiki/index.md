# Wiki Index

> Master table of contents. Updated by Claude after every ingest.
> Each entry: [Title](filename.md) — one-line description. Max 150 chars per line.

## Entities — Companies
- [WIH](wih.md) — Webber Investment Homes, primary real estate operating brand
- [Webber Wealth Holdings](webber-wealth-holdings.md) — holding entity, not used externally
- [W&M Series LLC](wm-series-llc.md) — series entity for specific properties
- [LBK Cleaners](lbk-cleaners.md) — cleaning business in Lubbock, TX; commercial-only, funds Joshua's personal income
- [Rent 2 Own Cribs](r2oc.md) — marketing brand for rent-to-own properties and content; rebrand planned
- [Hub City Title](hub-city-title.md) — title company used on closings

## Entities — Properties
- [1312 65th Dr](1312-65th-dr.md) — six-unit owned by Joshua; tenants Stephanie (A), Angel Garcia (D), Aaron (E)
- [4019 37th St](4019-37th-st.md) — seller-finance to Joseph; 7500 Winston tenants Ronald & Samantha in eviction
- [2802 S Channing St](2802-s-channing-st.md) — Amarillo TX FHA wrap; payer Tracy (Morales note); Rocket Mortgage
- [3423 E Baylor St](3423-e-baylor-st.md) — Lubbock, TX; Stripe merchant account tied here; tenant Veronica
- [4626 S Lipscomb St](4626-s-lipscomb-st.md) — Lubbock, TX rental property
- [4618 45th St](4618-45th-st.md) — Lubbock, TX rental property
- [1926 27th St](1926-27th-st.md) — Lubbock, TX rental property
- [2102 68th St](2102-68th-st.md) — Lubbock, TX; $35k KRC Services wholesale assignment
- [5427 35th St](5427-35th-st.md) — Lubbock, TX rental property
- [3904 Ave R](3904-ave-r.md) — Lubbock, TX rental property
- [3602 31st St](3602-31st-st.md) — Lubbock, TX rental property
- [4302 E 61st St](4302-e-61st-st.md) — creative-finance close ~Mar 2026; seller-finance transfer to tenants in progress
- [526 53rd St](526-53rd-st.md) — Lubbock, TX seller-finance property
- [7005 Winston Ave](7005-winston-ave.md) — Units E & F; water heater + flooring work; tenant Ronald
- [4513 48th St](4513-48th-st.md) — active RTO; tenant Joseph $1,813 escrowed; TMGLC/Michael Bullis; Curtis William funding
- [4438 Puffer St](4438-puffer-st.md) — seller-finance note serviced by One-Point Lending; only property NOT on DoorLoop
- [2106 68th St](2106-68th-st.md) — Lubbock rental; tenant Ashley
- [7000 Patterson Ave](7000-patterson-ave.md) — tenants catching up to enable biweekly payments
- [915 Tulane St](915-tulane-st.md) — distressed (Erica Jimenez); Joshua declined; archived
- [1314-1316 65th Dr](1314-1316-65th-dr.md) — 9-unit; acquisition paused (declined for now); squatter situation

## Entities — Tools & Platforms
- [GoHighLevel](ghl.md) — comms/pipeline hub; 16k contacts migrating to Supabase, GHL becomes data source
- [BookingKoala](bookingkoala.md) — CRM for LBK Cleaners
- [DoorLoop](doorloop.md) — property management platform ($265/mo per-lease); slated for in-house replacement
- [Baselane](baselane.md) — financial tracking; statement-pull automation; Section 8 payments land here
- [Mercury](mercury.md) — business bank accounts, Profit First; becoming the primary money layer (API + MCP)
- [Sequence](sequence.md) — getsequence.io money-routing layer; Claude MCP reads balances; ≠ Secured Sequence
- [Secured Sequence](secured-sequence.md) — RTO/seller-finance escrow-account provider (≠ Sequence)
- [One-Point Lending](one-point-lending.md) — third-party note servicer (4438 Puffer St)
- [Giggle Finance](giggle-finance.md) — working-capital / bridge funding for fast-repay closings
- [Lakeview](lakeview.md) — FL mortgage servicer on the Yvonne/Scott subject-to deal
- [Rocket Mortgage](rocket-mortgage.md) — servicer on 2802 S Channing (FHA)
- [Stripe](stripe.md) — payment processing, merchant account at 3423 E Baylor
- [Twilio](twilio.md) — SMS/voice for AI agents
- [Claude API](claude-api.md) — AI backbone for Vince and other automations
- [Zapier](zapier.md) — integration layer ("AI Employee" key for DoorLoop sync)
- [Railway](railway.md) — deployment platform for AI services (wih-app "Terrific Blessing")
- [Supabase](supabase.md) — database for wih-app; destination for 16k-contact CRM migration
- [Google Sheets](google-sheets.md) — KPI tracking, financial dashboards, content automation
- [n8n](n8n.md) — workflow automation
- [ElevenLabs](elevenlabs.md) — AI voice / TTS + voice-agent builder; candidate voice layer for Vince AI
- [Manus](manus.md) — prior AI agent tool; dropped May 2026 for Claude Code + superpowers (archived)
- [/watch Video Capability](watch-video-capability.md) — Claude Code video-analysis plugin; video → transcript → wiki

## Projects
- [Vince AI](vince-ai.md) — PML/TL + acquisitions chatbot on a GHL workflow; needs dedicated number + publishing
- [Content AI](content-ai.md) — automated R2OC social; Canva-MCP photo branding; proof-content engine
- [LBK Cleaners Launch](lbk-cleaners-launch.md) — booking page, then cleaner hiring
- [LBK Commercial Strategy](lbk-commercial-strategy.md) — commercial-only cleaning direction; funds Joshua's income
- [wih-app](wih-app.md) — central CRM / "Us" app, Railway + Supabase; KPI dashboard, DoorLoop replacement
- [wih-ai-service](wih-ai-service.md) — AI service layer for WIH automations
- [9-Unit Acquisition](9-unit-acquisition.md) — 1314/1316 65th Dr; PAUSED (declined for now)
- [Yvonne/Scott Subject-To](yvonne-scott-subject-to.md) — active subject-to acquisition; Lakeview loan; auth forms signed
- [Baselane → Mercury Migration](baselane-to-mercury-migration.md) — move banking + routing to Mercury so AI owns the money layer

## Concepts
- [Profit First](profit-first.md) — cash management framework, Mercury accounts by percentage
- [Rent-to-Own](rent-to-own.md) — primary exit strategy, seller finance structures
- [Subject-To](subject-to.md) — creative financing: taking title subject to existing mortgage
- [Seller Finance](seller-finance.md) — owner-carry note structures
- [Creative Financing](creative-financing.md) — umbrella: rent-to-own, subject-to, seller finance
- [PML/TL](pml-tl.md) — Private Money Lenders and Transactional Lenders, capital raising
- [Infinite Banking](infinite-banking.md) — cash-value life insurance as a capital strategy
- [Loan Servicing](loan-servicing.md) — note servicing; in-house servicing ambition
- [Draw Reimbursements](draw-reimbursements.md) — owner-draw / reimbursement tracking
- [Wholesale](wholesale.md) — top-of-funnel deal sourcing; 2026 AI-automation playbook
- [No Fluff Model](no-fluff-model.md) — Matt Beard's 3-phase wholesale system (Lead Gen → 3 Cs → Disposition)
- [Agent Outreach](agent-outreach.md) — direct-to-agent acquisition channel + scripts
- [MLS Two-Call Closing](mls-two-call-closing.md) — Alex Martinez on-market discovery + close framework
- [Disposition](disposition.md) — AI buyer-side 5-day dispo process; A/B/C buyer tiers
- [Sales Scripts](sales-scripts.md) — NEPQ seller scripts + 2026 agent-outreach/MLS scripts
- [AI Automation Strategy](ai-automation-strategy.md) — GHL hub, Matt Beard framework, three verticals
- [AI Operating System](ai-operating-system.md) — Four Cs / Three Ms / Bike Method (Nate Herk)
- [Claude Code Workflow](claude-code-workflow.md) — Plan Mode, minimal CLAUDE.md, verification loops, skills (Boris Cherny)
- [Information Moat](information-moat.md) — quality of context > prompt-tuning; the wiki as durable asset
- [Business Brain](business-brain.md) — the Claude-maintained wiki itself; source of truth + proof-content engine
- [Property Management](property-management.md) — self-managed portfolio ops, Mostafa as lead
- [Cleaning Business Models](cleaning-business-models.md) — analysis of cleaning-company models for LBK
- [Legal Document Templates](legal-document-templates.md) — reusable legal/contract templates
- [KPI Tracking](kpi-tracking.md) — daily KPI dashboard; $500 needle-mover bet
- [Company Roadmap](company-roadmap.md) — the billion-dollar ladder; AI-run, in-house software

## People
- [Joshua](joshua.md) — systems architect and decision-maker
- [Mostafa Elkhamisy](mostafa.md) — operations lead; Claude Code builder; all outbound comms route through him
- [M'kenzy](mkenzy.md) — team; manual fieldwork; owns a cleaning company; PM-partner candidate
- [Kenneth](kenneth.md) — team / partner
- [Antonio](antonio.md) — trained by Josh on cash-flow underwriting (acquisitions/deal-analysis; role TBD)
- [Aaron McCloskey](aaron-mccloskey.md) — tenant
- [Austin Hughes](austin-hughes.md) — Thunder Sun Homes; 9-unit deal (paused)
- [Don Pittman](don-pittman.md) — CPA; entity consolidation (verify approach)
- [Curtis William](curtis-william.md) — private/transactional lender ($15k → 4513 48th St)
- [Michael Bullis](michael-bullis.md) — seller-side counterparty on 4513 48th St (TMGLC)
- [Shane Leary](shane-leary.md) — HVAC/plumbing vendor
- [Jacob Swim](jacob-swim.md) — Allstate insurance agent (4019 37th St)
- [John Garcia](john-garcia.md) — flooring/handyman contractor
- [Dondi Cook](dondi-cook.md) — real estate photographer
- [Alex Hormozi](alex-hormozi.md) — role model; proof-based content framework
- [Dan Martell](dan-martell.md) — role model
- [David Goggins](david-goggins.md) — role model, discipline
- [Pace Morby](pace-morby.md) — role model, creative financing
- [Ed Mylett](ed-mylett.md) — role model
- [Grant Cardone](grant-cardone.md) — role model
- [Matt Beard](matt-beard.md) — "No Fluff" AI-augmented wholesale framework (primary reference)
- [Alex Martinez](alex-martinez.md) — RealEstateSkills.com; MLS two-call closing reference
- [Hieu](hieu.md) — direct-to-agent off-market wholesaler ($1.3M on GHL)
- [Jerry Norton](jerry-norton.md) — wholesale educator (Flipping Mastery)
- [Boris Cherny](boris-cherny.md) — creator of Claude Code; workflow reference
- [Nate Herk](nate-herk.md) — AI automation creator; AI Operating System framework

## Sources — Daily connector snapshots (2026-06-04)
- [GHL Snapshot 2026-06-04](source-ghl-snapshot-2026-06-04.md) — 500 opps, 12 pipelines, 16,375 contacts; Ashley Paz hot in Send Deposit Agreement
- [Mercury Snapshot 2026-06-04](source-mercury-snapshot-2026-06-04.md) — $263.55 checking, Lafayette Life $837.48 flagged, Tre'sye Rodriguez $1,172.98 incoming
- [Supabase Snapshot 2026-06-04](source-supabase-snapshot-2026-06-04.md) — 14,206 directory contacts (87% migrated), 1 live SMS conversation
- [Twilio SMS Log 2026-06-04](source-twilio-sms-log-2026-06-04.md) — **Vince AI confirmed live** on +18XXXXX2532; acquisition outreach active Jun 3–4

## Sources — Reference data
- [Davis — Available Properties](davis-available-properties.md) — ~28 tracked acquisition leads with MAO/ARV/cashflow

## Sources — Key documents & clips
- [BookingKoala Help Center](source-bookingkoala-help-center.md) — 370-article complete reference for LBK Cleaners
- [AIOS video (Nate Herk)](source-aios-nate-herk.md) — "Claude Opus 4.8 as my AI Operating System" — Four Cs framework
- [Voice Agents w/ ElevenLabs](source-voice-agents-elevenlabs.md) — code-first voice agent build; voice layer for Vince
- [Vince Master Booklet](source-vince-master-booklet.md) — full spec/knowledge base for the Vince AI bot
- [Session Captures (May 29–Jun 3)](source-session-captures.md) — reconciliation page for 57 session-capture memos
- [Pre-Foreclosure Underwriting (Josh→Antonio)](source-underwriting-antonio.md) — cash-flow underwriting SOP: ARV pricing, interest bands, PITI, 20% net margin
- [LBK Cleaners swivel logo](source-lbk-swivel-logo.md) — 2-sec silent brand asset (logo on green)

## Sources — Wholesale frameworks (2026)
- [No Fluff Blueprint (Matt Beard)](source-wholesale-blueprint-next-market.md) — canonical 3-phase model + KPIs
- [Ultimate Agent Outreach Script (Matt Beard)](source-ultimate-agent-outreach-script.md) — acquisition opener + objection bank
- [Hieu $1.3M Process](source-hieu-1-3m-process.md) — direct-to-agent texting + discovery scripts on GHL
- [Selling Wholesale Easier (No Fluff)](source-selling-wholesale-easier.md) — AI 5-day disposition + A/B/C buyer tiers
- [Start Wholesale 2026 (Alex Martinez)](source-start-wholesale-2026.md) — on-market MLS, reverse-engineering offer math
- [Agent Script / Free Script (Alex Martinez)](source-agent-script-freescript.md) — 15-part discovery call script
- [$1.2M Script (Alex Martinez)](source-this-exact-wholesale-script-1-2m.md) — MLS two-call discovery + close + objection multipliers
- [Wholesaling Follow-Up Strategy](source-wholesaling-follow-up-strategy.md) — triple-dial cadence

## Sources — AI build & content clips
- [Claude Code Creator's Workflow (Boris Cherny)](source-claude-code-creator-starts-project.md) — 6 principles, Plan Mode first
- [New Way of Making Content (Hormozi)](source-new-way-content-ai.md) — proof-based content; self-licking ice cream cone
- [BI Dashboard with Claude](source-bi-dashboard-claude.md) — GHL→Supabase→Vercel KPI dashboard build

## Sources — Daily meeting transcripts (May 20 – Jun 2, 2026)
- [2026-05-21 Morning Meeting](source-transcript-2026-05-21-morning-meeting-josh-mostafa.md) — Telegram SOP, Vince≠Gumloop, flat late fee
- [2026-05-22 Morning Meeting](source-transcript-2026-05-22-morning-meeting-josh-mostafa.md) — 4513 photos, insurance, Linda deal
- [2026-05-26 Morning Meeting](source-transcript-2026-05-26-morning-meeting-josh-mostafa.md) — Claude Code adopted, 9-unit numbers, Giggle Finance
- [2026-05-27 Morning Meeting](source-transcript-2026-05-27-morning-meeting-josh-mostafa.md) — 9-unit declined, skills-first, LBK + girlfriend
- [2026-05-28 Morning Meeting](source-transcript-2026-05-28-morning-meeting-josh-mostafa.md) — 2802 Amarillo/FHA, watermark skill
- [2026-05-29 Morning Meeting](source-transcript-2026-05-29-morning-meeting-josh-mostafa.md) — wih-app "Terrific Blessing", Baselane automation
- [2026-05-30 Yvonne Phone Call](source-transcript-2026-05-30-phone-call-with-yvonne-and-josh.md) — subject-to playbook, forms signed
- [2026-05-30 Yvonne/Scott Video Call](source-transcript-2026-05-30-video-call-with-yvonne-scott-and-josh.md) — subject-to Q&A; 31-entities flag
- [2026-06-01 Morning Meeting](source-transcript-2026-06-01-morning-meeting-josh-mostafa.md) — eviction decision, squatters (truncated)
- [2026-06-02 Morning Meeting](source-transcript-2026-06-02-morning-meeting-josh-mostafa.md) — GHL→Supabase, Don Pittman, Curtis William
- [2026-06-02 Tactical Session](source-transcript-2026-06-02-meeting.md) — contacts migration, DoorLoop SMS, "Us" app, Sequence MCP
- Low-signal stubs: [05-20 Angel](source-transcript-2026-05-20-morning-meeting-angel.md), [05-22 Michael](source-transcript-2026-05-22-meeting-with-michael-and-josh.md), [05-22 Role-Play w/ Jon](source-transcript-2026-05-22-weekly-role-play-w-jon.md)

## Sources — Documents (legal, financial, property)
- [2802 Trust Addendum](source-2802-trust-addendum.md) · [4302 E 61st Creative Terms](source-4302-e-61st-creative-terms.md) · [4513 48th Amendment](source-4513-48th-st-amendment.md)
- [4513 48th St Lease/46th](source-lease-agreement-46th.md) · [Assignment of Contract](source-assignment-of-contract.md) · [Seller Finance 526 53rd](source-seller-finance-526-53rd.md)
- [RTO Disclosures](source-rto-disclosures.md) · [Gonzalez Inspection Notice](source-gonzalez-inspection-notice.md) · [HUD 222408](source-hud-222408.md)
- [Property Insurance](source-property-insurance.md) · [EIN Registry](source-ein-registry.md) · [Webber 2025 P&L](source-webber-2025-pl.md)
- [Baselane Statements](source-baselane-statements.md) · [Baselane Statement Analyzer Skill](source-baselane-statement-analyzer-skill.md)
- [53 Alabama Properties](source-53-al-properties.md) · [n8n Acquisition Lookup](source-n8n-acquisition-lookup.md) · [Gumloop Manual](source-gumloop-manual.md)
- [LBK Bid Calculators](source-lbk-bid-calculators.md) · [LBK Commercial Targets](source-lbk-commercial-targets.md) · [Cleaning Model Analysis](source-cleaning-model-analysis.md) · [Content AI Script](source-content-ai-script.md)
