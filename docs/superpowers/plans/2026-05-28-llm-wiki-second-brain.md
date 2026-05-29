# LLM Wiki Second Brain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Joshua's complete second brain as a flat Obsidian wiki maintained by Claude, pre-seeded from CLAUDE.md context, with a daily automated cycle that pulls Notion exports, ingests new sources, and runs silent lint.

**Architecture:** Flat `wiki/` folder with typed YAML frontmatter. Everything in one folder, clean wikilinks, type filtering via frontmatter. Daily n8n job pulls Notion exports to `raw/` when changed; daily Claude agent ingests new files, runs lint, and proposes CLAUDE.md updates when the delta warrants it.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian (browse only), n8n (Notion pull), Claude Code schedule skill (daily agent), Notion API

---

## Phase 1: Wiki Foundation

### Task 1: Update CLAUDE.md wiki schema

**Files:**
- Modify: `C:\Users\joshu\CLAUDE.md` (lines 188–283 — the entire `# LLM Wiki` section)

- [ ] **Step 1: Replace the LLM Wiki section in CLAUDE.md**

Replace everything from `# LLM Wiki` to the end of the file with:

```markdown
# LLM Wiki — Business Brain

A persistent, compounding second brain maintained entirely by Claude.
Joshua sources and curates. Claude writes, links, and maintains everything.

## Purpose

This wiki is Joshua's complete second brain — business, personal, finance, health, and life.
The wiki is the source of truth. Notion master prompts and CLAUDE.md are compressed views derived from it.

## Folder Structure

```
raw/                          # immutable source documents — never modify these
raw/assets/                   # images downloaded from web-clipped articles
wiki/                         # LLM-maintained knowledge base
wiki/index.md                 # master table of contents, grouped by type
wiki/log.md                   # append-only ingest/query/lint history
wiki/.last-ingest             # timestamp of last successful ingest (ISO 8601)
```

## File Conventions

All wiki files use lowercase-kebab-case: `vince-ai.md`, `profit-first.md`, `1312-65th-dr.md`

Every wiki page requires this YAML frontmatter:

```yaml
---
name: vince-ai
type: project          # entity | project | concept | person | source
tags: [ai, ghl, twilio, capital-raising]
status: active         # active | paused | complete | archived (omit for concept/person)
sources: [transcript-2026-05-10.md]
updated: 2026-05-28
---
```

## Page Types

| Type | What it covers | Examples |
|---|---|---|
| `entity` | Companies, properties, tools, accounts | `wih.md`, `1312-65th-dr.md`, `ghl.md` |
| `project` | Active initiatives with a goal and status | `vince-ai.md`, `lbk-cleaners-launch.md` |
| `concept` | Ideas and frameworks | `profit-first.md`, `rent-to-own.md` |
| `person` | Team, vendors, partners, mentors | `mostafa.md`, `austin-hughes.md` |
| `source` | One page per ingested raw file | `transcript-2026-05-10.md` |

Wikilinks: always clean short-form — `[[vince-ai]]`, `[[mostafa]]`. Never use path prefixes.

## Page Template

```markdown
# Page Title

**Summary**: One to two sentences.

**Sources**: [list of raw source files, or "CLAUDE.md seed" for pre-seeded pages]

**Last updated**: YYYY-MM-DD

---

Main content. Link related concepts with [[wikilinks]] throughout.

## Related pages
- [[related-page-1]]
- [[related-page-2]]
```

## Ingest Workflow

When Joshua drops a file into `raw/` and says "ingest this":

1. Read the full source document
2. Discuss key takeaways with Joshua before writing anything
3. Create a `source` page in `wiki/` summarizing the document
4. Create or update entity, project, concept, and person pages touched by the source
5. Link everything with wikilinks
6. Update `wiki/index.md` with any new pages
7. Append an entry to `wiki/log.md`
8. Update `wiki/.last-ingest` with today's ISO 8601 date

A single source may touch 10–15 wiki pages. That is normal.

## Query Workflow

When Joshua asks a question:

1. Read `wiki/index.md` to identify relevant pages
2. Read those pages and synthesize an answer with citations
3. Cite specific wiki pages in the response
4. If the answer is valuable, offer to save it as a new wiki page

## Lint Workflow (Automated Daily — Silent)

Runs as part of the daily scheduled agent. Never requires Joshua's attention.

- Find contradictions between pages — flag in `log.md` if cannot auto-resolve
- Find orphan pages (no inbound links) — auto-fix by adding links from related pages
- Identify concepts mentioned but lacking their own page — create stub pages
- Flag claims newer sources may have superseded — note in `log.md`
- Update stale `status` fields where evidence exists
- Append one-line summary to `wiki/log.md`

## Citation Rules

- Every factual claim should reference its source file
- Use the format `(source: filename.md)` after the claim
- If two sources disagree, note the contradiction explicitly
- Pre-seeded pages from CLAUDE.md use `(source: CLAUDE.md seed)`

## Three-Brain Architecture

```
Notion Personal Prompt  ←→  raw/  ←→  wiki/  ←→  CLAUDE.md
Notion Business Prompt  ←→  raw/        ↑
Transcripts/Clips/Docs  ──→  raw/  ──→  wiki/
```

The wiki is the source of truth. Notion and CLAUDE.md are compressed views.
After significant wiki changes, Claude proposes a CLAUDE.md update in the active session.

## Source Routing Convention

| Source type | Raw filename format |
|---|---|
| Notion Personal export | `notion-personal-YYYY-MM-DD.md` |
| Notion Business export | `notion-business-YYYY-MM-DD.md` |
| Meeting transcript | `transcript-YYYY-MM-DD-topic.md` |
| Voice memo | `memo-YYYY-MM-DD-topic.md` |
| Web clip | `clip-YYYY-MM-DD-title.md` |
| Document/PDF | `doc-YYYY-MM-DD-title.md` |

## Rules

- Never modify anything in `raw/`
- Always update `wiki/index.md` and `wiki/log.md` after any changes
- Keep page names lowercase with hyphens
- Write in clear, plain language
- When uncertain about how to categorize something, ask Joshua
```

- [ ] **Step 2: Verify the file saved correctly**

Open `C:\Users\joshu\CLAUDE.md` and confirm the `# LLM Wiki` section now reads "Business Brain" (not "Japan") and contains the frontmatter format, page types table, and three-brain architecture section.

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu" add CLAUDE.md
git -C "C:\Users\joshu" commit -m "feat: replace LLM Wiki schema with Business Brain schema"
```

---

### Task 2: Create wiki/index.md

**Files:**
- Create: `C:\Users\joshu\.claude\Business_Brain\wiki\index.md`

- [ ] **Step 1: Write index.md**

```markdown
# Wiki Index

> Master table of contents. Updated by Claude after every ingest.
> Each entry: [Title](filename.md) — one-line description. Max 150 chars per line.

## Entities — Companies
- [WIH](wih.md) — Webber Investment Homes, primary real estate operating brand
- [Webber Wealth Holdings](webber-wealth-holdings.md) — holding entity, not used externally
- [W&M Series LLC](wm-series-llc.md) — series entity for specific properties
- [LBK Cleaners](lbk-cleaners.md) — cleaning business being built in Lubbock, TX
- [Rent 2 Own Cribs](r2oc.md) — marketing brand for rent-to-own properties and content

## Entities — Properties
- [1312 65th Dr](1312-65th-dr.md) — multi-unit, Unit F active, Unit D tenant Angel Garcia
- [4019 37th St](4019-37th-st.md) — Lubbock, TX rental property
- [2802 S Channing St](2802-s-channing-st.md) — Lubbock, TX rental property
- [3423 E Baylor St](3423-e-baylor-st.md) — Lubbock, TX, Stripe merchant account tied here
- [4626 S Lipscomb St](4626-s-lipscomb-st.md) — Lubbock, TX rental property
- [4618 45th St](4618-45th-st.md) — Lubbock, TX rental property
- [1926 27th St](1926-27th-st.md) — Lubbock, TX rental property
- [2102 68th St](2102-68th-st.md) — Lubbock, TX rental property
- [5427 35th St](5427-35th-st.md) — Lubbock, TX rental property
- [3904 Ave R](3904-ave-r.md) — Lubbock, TX rental property
- [1314-1316 65th Dr](1314-1316-65th-dr.md) — prospective 9-unit, Thunder Sun Homes / Austin Hughes

## Entities — Tools & Platforms
- [GoHighLevel](ghl.md) — central hub for all business comms, pipelines, AI agents
- [BookingKoala](bookingkoala.md) — CRM for LBK Cleaners
- [DoorLoop](doorloop.md) — property management platform
- [Baselane](baselane.md) — financial tracking for properties
- [Mercury](mercury.md) — business bank accounts, Profit First model
- [Stripe](stripe.md) — payment processing, merchant account at 3423 E Baylor
- [Twilio](twilio.md) — SMS/voice for AI agents
- [Claude API](claude-api.md) — AI backbone for Vince and other automations
- [Zapier](zapier.md) — integration layer between platforms
- [Railway](railway.md) — deployment platform for AI services
- [Supabase](supabase.md) — database for wih-app
- [Google Sheets](google-sheets.md) — KPI tracking, financial dashboards, content automation
- [n8n](n8n.md) — workflow automation

## Projects
- [Vince AI](vince-ai.md) — PML/TL qualification chatbot, GHL + Twilio + Claude, needs number and publishing
- [Content AI](content-ai.md) — automated social media for R2OC, Google Sheets + daily automation
- [LBK Cleaners Launch](lbk-cleaners-launch.md) — booking page next, then cleaner hiring
- [wih-app](wih-app.md) — main WIH web app, Railway + Supabase
- [wih-ai-service](wih-ai-service.md) — AI service layer for WIH automations
- [9-Unit Acquisition](9-unit-acquisition.md) — prospective 9-unit at 1314/1316 65th Dr

## Concepts
- [Profit First](profit-first.md) — cash management framework, Mercury accounts by percentage
- [Rent-to-Own](rent-to-own.md) — primary exit strategy, seller finance structures
- [Subject-To](subject-to.md) — creative financing: taking title subject to existing mortgage
- [Creative Financing](creative-financing.md) — umbrella: rent-to-own, subject-to, seller finance
- [PML/TL](pml-tl.md) — Private Money Lenders and Transactional Lenders, capital raising
- [Wholesale](wholesale.md) — top-of-funnel deal sourcing, AI-automated outreach pipeline
- [AI Automation Strategy](ai-automation-strategy.md) — GHL as hub, Matt Beard framework, three verticals

## People
- [Mostafa Elkhamisy](mostafa.md) — operations lead, all outbound comms route through him
- [M'kenzy](mkenzy.md) — team member
- [Kenneth](kenneth.md) — team member
- [Austin Hughes](austin-hughes.md) — Thunder Sun Homes, prospective 9-unit deal partner
- [Joshua](joshua.md) — systems architect and decision-maker
- [Alex Hormozi](alex-hormozi.md) — role model, business frameworks
- [Dan Martell](dan-martell.md) — role model
- [David Goggins](david-goggins.md) — role model, discipline
- [Pace Morby](pace-morby.md) — role model, creative financing
- [Ed Mylett](ed-mylett.md) — role model
- [Grant Cardone](grant-cardone.md) — role model
- [Matt Beard](matt-beard.md) — AI-augmented wholesale framework reference

## Sources
<!-- Populated as raw files are ingested -->
```

- [ ] **Step 2: Verify structure**

Open `wiki/index.md` in Obsidian. Confirm all five section headers are present (Entities — Companies, Properties, Tools, Projects, Concepts, People, Sources) and the file is under 200 lines.

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/index.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: create wiki index.md with full seed structure"
```

---

### Task 3: Create wiki/log.md and .last-ingest

**Files:**
- Create: `C:\Users\joshu\.claude\Business_Brain\wiki\log.md`
- Create: `C:\Users\joshu\.claude\Business_Brain\wiki\.last-ingest`

- [ ] **Step 1: Write log.md**

```markdown
# Wiki Log

Append-only. Format: `## [YYYY-MM-DD] operation | title`
Operations: seed | ingest | lint | query | update

---

## [2026-05-28] seed | Initial wiki seeded from CLAUDE.md context — 30 pages created across entities, projects, concepts, and people
```

- [ ] **Step 2: Write .last-ingest**

```
2026-05-28
```

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/log.md wiki/.last-ingest
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: create wiki log and last-ingest timestamp"
```

---

### Task 4: Seed entity pages — companies

**Files:**
- Create: `wiki/wih.md`, `wiki/webber-wealth-holdings.md`, `wiki/wm-series-llc.md`, `wiki/lbk-cleaners.md`, `wiki/r2oc.md`

- [ ] **Step 1: Write wih.md (full example — use as template for all entity pages)**

```markdown
---
name: wih
type: entity
tags: [real-estate, brand, lubbock]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Webber Investment Homes (WIH)

**Summary**: Primary real estate operating brand. Not shared externally with vendors or third parties.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

WIH is the public-facing brand for Joshua's real estate operations in Lubbock, TX. Vendor communications, tenant comms, and third-party relationships use WIH — never the holding entity name ([[webber-wealth-holdings]]).

Operations are run by [[mostafa]] as the human-in-the-loop for all AI automations and outbound comms. Joshua acts as systems architect and decision-maker only.

Current portfolio: 10 active properties plus one prospective 9-unit acquisition ([[1314-1316-65th-dr]]). Exit strategy is primarily [[rent-to-own]] and [[creative-financing]].

Tech hub: [[ghl]] is the central platform for all WIH communications, pipelines, and AI agents.

## Related pages
- [[webber-wealth-holdings]]
- [[mostafa]]
- [[ghl]]
- [[rent-to-own]]
- [[profit-first]]
```

- [ ] **Step 2: Write webber-wealth-holdings.md**

```markdown
---
name: webber-wealth-holdings
type: entity
tags: [holding-entity, legal]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Webber Wealth Holdings LLC

**Summary**: Holding entity. Not used in external communications with vendors or third parties.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

The legal holding structure above [[wih]]. Not referenced externally — all external-facing communications use WIH or property-specific identifiers.

## Related pages
- [[wih]]
- [[wm-series-llc]]
- [[joshua]]
```

- [ ] **Step 3: Write wm-series-llc.md**

```markdown
---
name: wm-series-llc
type: entity
tags: [legal, series-llc]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# W&M Series LLC

**Summary**: Series entity used for specific properties in the portfolio.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Series LLC structure used to hold specific properties separately within the portfolio. Part of the legal structure under [[webber-wealth-holdings]].

## Related pages
- [[webber-wealth-holdings]]
- [[wih]]
```

- [ ] **Step 4: Write lbk-cleaners.md**

```markdown
---
name: lbk-cleaners
type: entity
tags: [cleaning, lubbock, business]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# LBK Cleaners

**Summary**: Cleaning business being built from scratch in Lubbock, TX. Website live, BookingKoala CRM configured.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Separate business entity from the real estate portfolio. Website is live. CRM is [[bookingkoala]] — booking, scheduling, and customer management are configured. Next step: booking page live, then cleaner hiring.

Active launch work tracked in [[lbk-cleaners-launch]].

## Related pages
- [[lbk-cleaners-launch]]
- [[bookingkoala]]
- [[mostafa]]
```

- [ ] **Step 5: Write r2oc.md**

```markdown
---
name: r2oc
type: entity
tags: [marketing-brand, rent-to-own, content, social-media]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Rent 2 Own Cribs (R2OC)

**Summary**: Marketing brand for rent-to-own properties and content. Social media automated via Content AI.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

External-facing brand for [[wih]]'s rent-to-own properties and educational content. Content pipeline is being automated via [[content-ai]] using Google Sheets + daily automation.

## Related pages
- [[wih]]
- [[content-ai]]
- [[rent-to-own]]
- [[google-sheets]]
```

- [ ] **Step 6: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/wih.md wiki/webber-wealth-holdings.md wiki/wm-series-llc.md wiki/lbk-cleaners.md wiki/r2oc.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed entity pages — companies"
```

---

### Task 5: Seed entity pages — properties

**Files:**
- Create: one `.md` file per property (11 files listed below)

- [ ] **Step 1: Write 1312-65th-dr.md (full example)**

```markdown
---
name: 1312-65th-dr
type: entity
tags: [property, lubbock, multi-unit]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# 1312 65th Dr

**Summary**: Multi-unit property in Lubbock, TX. Unit F active, Unit D tenant Angel Garcia.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Multi-unit property. Currently Unit F active and Unit D occupied by tenant Angel Garcia. Part of the [[wih]] portfolio managed through [[doorloop]].

Adjacent prospective acquisition: [[1314-1316-65th-dr]] (9-unit, Thunder Sun Homes).

## Related pages
- [[wih]]
- [[doorloop]]
- [[mostafa]]
- [[1314-1316-65th-dr]]
```

- [ ] **Step 2: Write remaining property pages**

Create each file using the same frontmatter and template structure. Key differentiators per property:

| File | Address | Notes |
|---|---|---|
| `4019-37th-st.md` | 4019 37th St, Lubbock TX | Standard rental property |
| `2802-s-channing-st.md` | 2802 S Channing St, Lubbock TX | Standard rental property |
| `3423-e-baylor-st.md` | 3423 E Baylor St, Lubbock TX | Stripe merchant account tied here |
| `4626-s-lipscomb-st.md` | 4626 S Lipscomb St, Lubbock TX | Standard rental property |
| `4618-45th-st.md` | 4618 45th St, Lubbock TX | Standard rental property |
| `1926-27th-st.md` | 1926 27th St, Lubbock TX | Standard rental property |
| `2102-68th-st.md` | 2102 68th St, Lubbock TX | Standard rental property |
| `5427-35th-st.md` | 5427 35th St, Lubbock TX | Standard rental property |
| `3904-ave-r.md` | 3904 Ave R, Lubbock TX | Standard rental property |
| `1314-1316-65th-dr.md` | 1314/1316 65th Dr, Lubbock TX | Prospective 9-unit, Thunder Sun Homes / [[austin-hughes]] |

For `3423-e-baylor-st.md`, add: "Stripe merchant account for WIH payment processing is tied to this address. See [[stripe]]."

For `1314-1316-65th-dr.md`, set `status: paused` and add: "Prospective 9-unit acquisition being explored with [[austin-hughes]] (Thunder Sun Homes). Deal tracked in [[9-unit-acquisition]]."

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/1312-65th-dr.md wiki/4019-37th-st.md wiki/2802-s-channing-st.md wiki/3423-e-baylor-st.md wiki/4626-s-lipscomb-st.md wiki/4618-45th-st.md wiki/1926-27th-st.md wiki/2102-68th-st.md wiki/5427-35th-st.md wiki/3904-ave-r.md wiki/1314-1316-65th-dr.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed entity pages — properties"
```

---

### Task 6: Seed entity pages — tools

**Files:**
- Create: 13 tool entity pages

- [ ] **Step 1: Write ghl.md (full example)**

```markdown
---
name: ghl
type: entity
tags: [crm, automation, ai, central-hub]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# GoHighLevel (GHL)

**Summary**: Central hub for ALL WIH business communications, pipelines, AI agents, and automations. Single source of truth.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

GHL is the nerve center of Joshua's business. Every AI agent ([[vince-ai]], [[content-ai]]) lives here. All outbound communications route through [[mostafa]] via GHL — this is non-negotiable per SOP.

The strategic vision is full AI automation of real estate operations with GHL as the hub across three verticals: wholesale, property management, and capital raising ([[pml-tl]]).

[[twilio]] provides SMS/voice capabilities. [[claude-api]] is the AI backbone for agent conversations.

## Related pages
- [[vince-ai]]
- [[twilio]]
- [[claude-api]]
- [[mostafa]]
- [[ai-automation-strategy]]
```

- [ ] **Step 2: Write remaining tool pages**

Create each file with correct frontmatter and summary. Key content per tool:

| File | Name | Key content |
|---|---|---|
| `bookingkoala.md` | BookingKoala | CRM for [[lbk-cleaners]] — booking, scheduling, customer management |
| `doorloop.md` | DoorLoop | Property management platform — leases, charges, maintenance, tenant comms for [[wih]] portfolio |
| `baselane.md` | Baselane | Financial tracking for properties |
| `mercury.md` | Mercury | Business bank accounts running [[profit-first]] model across all entities |
| `stripe.md` | Stripe | Payment processing. Merchant account tied to [[3423-e-baylor-st]] |
| `twilio.md` | Twilio | SMS/voice for AI agents. Powers [[vince-ai]] via [[ghl]] |
| `claude-api.md` | Claude API | AI backbone for [[vince-ai]] and all automation agents. Made by Anthropic |
| `zapier.md` | Zapier | Integration layer between platforms |
| `railway.md` | Railway | Deployment platform for AI services. Hosts [[wih-app]] and [[wih-ai-service]] |
| `supabase.md` | Supabase | Database backend for [[wih-app]] |
| `google-sheets.md` | Google Sheets | KPI tracking, financial dashboards, [[content-ai]] automation |
| `n8n.md` | n8n | Workflow automation. Handles daily Notion pull to `raw/` for wiki ingest |

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/bookingkoala.md wiki/doorloop.md wiki/baselane.md wiki/mercury.md wiki/stripe.md wiki/twilio.md wiki/claude-api.md wiki/zapier.md wiki/railway.md wiki/supabase.md wiki/google-sheets.md wiki/n8n.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed entity pages — tools"
```

---

### Task 7: Seed project pages

**Files:**
- Create: `vince-ai.md`, `content-ai.md`, `lbk-cleaners-launch.md`, `wih-app.md`, `wih-ai-service.md`, `9-unit-acquisition.md`

- [ ] **Step 1: Write vince-ai.md (full example)**

```markdown
---
name: vince-ai
type: project
tags: [ai, ghl, twilio, capital-raising, pml, tl]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Vince AI

**Summary**: PML/TL qualification chatbot via GHL + Twilio + Claude API. Architecture complete, needs dedicated number and publishing.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

AI chatbot for qualifying Private Money Lenders and Transactional Lenders. Lives in [[ghl]], uses [[twilio]] for SMS/voice, and [[claude-api]] as the conversation engine.

Current state: architecture complete. Blockers: dedicated Twilio number not yet assigned, not yet published to GHL pipeline.

Strategic purpose: automate top-of-funnel capital raising ([[pml-tl]]) so Joshua doesn't need to manually qualify every lender inquiry.

## Related pages
- [[ghl]]
- [[twilio]]
- [[claude-api]]
- [[pml-tl]]
- [[mostafa]]
```

- [ ] **Step 2: Write remaining project pages**

| File | Status | Key content |
|---|---|---|
| `content-ai.md` | active | Automated social media for [[r2oc]] via [[google-sheets]] + daily automation |
| `lbk-cleaners-launch.md` | active | Website live, [[bookingkoala]] configured. Next: booking page, then cleaner hiring |
| `wih-app.md` | active | Main WIH web app. Deployed on [[railway]], [[supabase]] backend |
| `wih-ai-service.md` | active | AI service layer for WIH automations. Deployed on [[railway]] |
| `9-unit-acquisition.md` | active | Exploring 9-unit at [[1314-1316-65th-dr]] with [[austin-hughes]]. Thunder Sun Homes |

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/vince-ai.md wiki/content-ai.md wiki/lbk-cleaners-launch.md wiki/wih-app.md wiki/wih-ai-service.md wiki/9-unit-acquisition.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed project pages"
```

---

### Task 8: Seed person pages

**Files:**
- Create: `mostafa.md`, `mkenzy.md`, `kenneth.md`, `austin-hughes.md`, `joshua.md`, `alex-hormozi.md`, `dan-martell.md`, `david-goggins.md`, `pace-morby.md`, `ed-mylett.md`, `grant-cardone.md`, `matt-beard.md`

- [ ] **Step 1: Write mostafa.md (full example)**

```markdown
---
name: mostafa
type: person
tags: [team, operations, communications]
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Mostafa Elkhamisy

**Summary**: Operations lead. ALL outbound communications go through Mostafa — non-negotiable. Primary human-in-the-loop for AI automations.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Mostafa is the execution layer for [[wih]]. Every outbound message — texts, emails, GHL sequences — routes through him. Joshua does not send outbound comms directly.

He is also the human-in-the-loop for all AI automations. When [[vince-ai]] or other agents need a human decision or review, Mostafa handles it.

## Related pages
- [[wih]]
- [[ghl]]
- [[vince-ai]]
- [[joshua]]
```

- [ ] **Step 2: Write remaining person pages**

| File | Role | Key content |
|---|---|---|
| `mkenzy.md` | Team member | Route applicable tasks to M'kenzy |
| `kenneth.md` | Team member | Route applicable tasks to Kenneth |
| `austin-hughes.md` | Partner | Thunder Sun Homes. Prospective 9-unit deal at [[1314-1316-65th-dr]] |
| `joshua.md` | Owner | Systems architect and decision-maker. Not in the weeds of execution. Wakes 4:48 AM. Mobile-first, Lubbock TX. Planning Austin relocation September 2026 |
| `alex-hormozi.md` | Mentor/Model | Role model. Business frameworks and scaling |
| `dan-martell.md` | Mentor/Model | Role model |
| `david-goggins.md` | Mentor/Model | Role model. Discipline and mental toughness |
| `pace-morby.md` | Mentor/Model | Role model. Creative financing strategies — [[subject-to]], [[rent-to-own]] |
| `ed-mylett.md` | Mentor/Model | Role model |
| `grant-cardone.md` | Mentor/Model | Role model |
| `matt-beard.md` | Reference | AI-augmented wholesale framework. Primary external reference for [[ai-automation-strategy]] |

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/mostafa.md wiki/mkenzy.md wiki/kenneth.md wiki/austin-hughes.md wiki/joshua.md wiki/alex-hormozi.md wiki/dan-martell.md wiki/david-goggins.md wiki/pace-morby.md wiki/ed-mylett.md wiki/grant-cardone.md wiki/matt-beard.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed person pages"
```

---

### Task 9: Seed concept pages

**Files:**
- Create: `profit-first.md`, `rent-to-own.md`, `subject-to.md`, `creative-financing.md`, `pml-tl.md`, `wholesale.md`, `ai-automation-strategy.md`

- [ ] **Step 1: Write profit-first.md (full example)**

```markdown
---
name: profit-first
type: concept
tags: [finance, cash-management, mercury, profit-first]
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Profit First

**Summary**: Cash management framework where income is allocated by percentage across purpose-specific bank accounts before expenses are paid.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Joshua runs Profit First across all entities via [[mercury]] bank accounts. Income hits a primary account, then gets distributed by percentage to accounts designated for: profit, owner pay, taxes, and operating expenses.

This forces profitability by design — you can only spend what's in the operating account.

KPIs tracked daily via [[google-sheets]] dashboard.

## Related pages
- [[mercury]]
- [[wih]]
- [[lbk-cleaners]]
- [[google-sheets]]
```

- [ ] **Step 2: Write remaining concept pages**

| File | Key content |
|---|---|
| `rent-to-own.md` | Primary exit strategy for [[wih]] properties. Tenant pays rent + option consideration, builds toward purchase. [[r2oc]] is the marketing brand |
| `subject-to.md` | Creative financing: take title to a property subject to the existing mortgage. Seller stays on the loan; buyer makes payments. Reference: [[pace-morby]] |
| `creative-financing.md` | Umbrella term covering [[rent-to-own]], [[subject-to]], seller finance. Primary model for [[wih]] acquisitions and exits |
| `pml-tl.md` | Private Money Lenders (PML) and Transactional Lenders (TL). Capital raising vertical. Qualified via [[vince-ai]] |
| `wholesale.md` | Top-of-funnel deal sourcing. Find distressed properties, assign contracts. Building toward AI-automated outreach pipeline via [[ghl]] |
| `ai-automation-strategy.md` | [[ghl]] as the single hub for all AI agents. Three verticals: wholesale, property management, capital raising. External reference: [[matt-beard]] framework |

- [ ] **Step 3: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/profit-first.md wiki/rent-to-own.md wiki/subject-to.md wiki/creative-financing.md wiki/pml-tl.md wiki/wholesale.md wiki/ai-automation-strategy.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: seed concept pages"
```

---

### Task 10: Verify wikilinks and update log

**Files:**
- Modify: `wiki/log.md`

- [ ] **Step 1: Verify all wikilinks resolve**

Open Obsidian. In the graph view, confirm:
- No orphan nodes (every page has at least one connection)
- All `[[wikilinks]]` in every page point to files that exist in `wiki/`

If any broken links appear (shown as unresolved in Obsidian graph), create stub pages for them:
```markdown
---
name: stub-name
type: concept
tags: []
sources: []
updated: 2026-05-28
---

# Stub Title

**Summary**: Stub — to be expanded on next relevant ingest.

**Last updated**: 2026-05-28
```

- [ ] **Step 2: Count pages and update log**

```bash
ls "C:\Users\joshu\.claude\Business_Brain\wiki" | Where-Object { $_.Name -ne "index.md" -and $_.Name -ne "log.md" -and $_.Name -ne ".last-ingest" } | Measure-Object
```

Append to `wiki/log.md`:
```markdown
## [2026-05-28] seed | Wikilink verification complete — [N] pages seeded, all links resolve
```

- [ ] **Step 3: Final commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/log.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: verify wikilinks and finalize Phase 1 seed"
```

---

## Phase 2: Automation Layer

> Phase 1 must be complete before starting Phase 2.

### Task 11: Set up n8n Notion pull workflow

**Files:**
- Create: `docs/n8n-notion-pull-workflow.json` (export of the n8n workflow for version control)

**Prerequisites — gather these before starting:**
1. Notion API key (Settings → Integrations → Internal integration)
2. Page ID of Personal Master Prompt in Notion (from the page URL: `notion.so/Page-Title-<PAGE_ID>`)
3. Page ID of Business Master Prompt in Notion
4. Confirm whether n8n is running locally or cloud-hosted

- [ ] **Step 1: Create a new n8n workflow named "Notion → Business Brain raw/"**

In n8n, add the following nodes in sequence:

**Node 1 — Schedule Trigger**
- Type: Schedule Trigger
- Run at: 3:00 AM daily

**Node 2 — Read last-known timestamps (HTTP Request or File node)**
- If n8n is LOCAL: use "Read/Write Files from Disk" node
  - Path: `C:\Users\joshu\.claude\Business_Brain\wiki\.last-ingest`
  - Operation: Read
- If n8n is CLOUD: use "Read Binary File" node pointing to a Google Drive file `business-brain-last-ingest.txt`

**Node 3 — Notion: Get Personal Master Prompt page**
- Type: Notion node
- Operation: Get a Page
- Page ID: `<PERSONAL_MASTER_PROMPT_PAGE_ID>`
- This returns `last_edited_time`

**Node 4 — IF: Personal page changed?**
- Condition: `{{ $node["Node 3"].json.last_edited_time }}` > stored timestamp
- True branch → proceed to export
- False branch → skip

**Node 5 — Notion: Get page content (Personal)**
- Type: HTTP Request
- Method: POST
- URL: `https://api.notion.com/v1/blocks/PAGE_ID/children`
- Headers: `Authorization: Bearer NOTION_API_KEY`, `Notion-Version: 2022-06-28`

**Node 6 — Code: Convert blocks to markdown**
- Type: Code node (JavaScript)
```javascript
const blocks = $input.all()[0].json.results;
const lines = [];
const today = new Date().toISOString().split('T')[0];

for (const block of blocks) {
  const type = block.type;
  const content = block[type];
  if (!content || !content.rich_text) continue;
  const text = content.rich_text.map(t => t.plain_text).join('');
  if (type === 'heading_1') lines.push(`# ${text}`);
  else if (type === 'heading_2') lines.push(`## ${text}`);
  else if (type === 'heading_3') lines.push(`### ${text}`);
  else if (type === 'bulleted_list_item') lines.push(`- ${text}`);
  else if (type === 'paragraph') lines.push(text);
  lines.push('');
}

return [{ json: { content: lines.join('\n'), filename: `notion-personal-${today}.md` } }];
```

**Node 7 — Write file to raw/**
- If LOCAL: "Read/Write Files from Disk" node
  - Path: `C:\Users\joshu\.claude\Business_Brain\raw\{{ $json.filename }}`
  - Content: `{{ $json.content }}`
- If CLOUD: Write to Google Drive, then sync to local via Obsidian Sync or Git

**Repeat Nodes 3–7 for Business Master Prompt** (using Business page ID, filename `notion-business-YYYY-MM-DD.md`)

**Node 8 — Update .last-ingest timestamp**
- Write today's ISO date to `wiki/.last-ingest`

- [ ] **Step 2: Test the workflow manually**

In n8n, click "Execute Workflow" once. Confirm:
- `raw/notion-personal-2026-05-28.md` is created with readable markdown
- `raw/notion-business-2026-05-28.md` is created with readable markdown
- File content is not empty and matches what's in Notion

- [ ] **Step 3: Export workflow JSON for version control**

In n8n: ⋮ menu → Download → save as `docs/n8n-notion-pull-workflow.json`

- [ ] **Step 4: Commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add docs/n8n-notion-pull-workflow.json
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: add n8n Notion pull workflow"
```

---

### Task 12: Set up Claude scheduled daily agent

**Files:**
- The schedule is managed by Claude Code's CronCreate system — no file to create

- [ ] **Step 1: Invoke the schedule skill**

In Claude Code, run:
```
/schedule
```

When prompted, configure:
- **Name**: `business-brain-daily`
- **Schedule**: `0 4 * * *` (4:00 AM daily)
- **Prompt**:

```
You are the Business Brain daily maintenance agent.

Working directory: C:\Users\joshu\.claude\Business_Brain

Run these three checks in order:

## 1. Ingest Check
Read wiki/.last-ingest to get the last ingest date.
List all files in raw/ that are newer than that date (by filename date suffix YYYY-MM-DD).
If any new files exist:
- For each new file, run the full ingest workflow from CLAUDE.md (read → create/update wiki pages → update index.md → append log.md)
- Update wiki/.last-ingest to today's date after all ingests complete

If no new files, skip to step 2.

## 2. Silent Lint
Run the lint workflow from CLAUDE.md silently:
- Fix orphan pages by adding links from related pages
- Create stubs for mentioned concepts lacking pages
- Update stale status fields where evidence exists
- If contradictions exist that cannot be auto-resolved, append one line to wiki/log.md: [YYYY-MM-DD] lint | contradiction found: [brief description]
- Append one-line lint summary to wiki/log.md regardless

## 3. CLAUDE.md Delta Check
Compare the current state of key wiki pages (wih.md, joshua.md, active project pages) against C:\Users\joshu\CLAUDE.md.
If there is meaningful new information in the wiki that is not reflected in CLAUDE.md, note it in wiki/log.md:
[YYYY-MM-DD] update | CLAUDE.md delta detected: [one sentence summary] — will propose update in next active session

Do not surface anything to the user unless a contradiction cannot be auto-resolved.
```

- [ ] **Step 2: Verify the schedule was created**

Run `/schedule` again and confirm `business-brain-daily` appears in the list with a 4:00 AM cron.

- [ ] **Step 3: Trigger a manual test run**

Ask Claude Code to run the agent prompt manually once and confirm:
- It checks raw/ for new files
- It runs lint (and appends to log.md)
- It checks the CLAUDE.md delta
- `wiki/log.md` has a new entry after the run

- [ ] **Step 4: Append final log entry**

```markdown
## [2026-05-28] seed | Automation layer complete — n8n Notion pull + Claude daily agent scheduled
```

- [ ] **Step 5: Final commit**

```bash
git -C "C:\Users\joshu\.claude\Business_Brain" add wiki/log.md
git -C "C:\Users\joshu\.claude\Business_Brain" commit -m "feat: complete Phase 2 automation layer"
```

---

## Verification Checklist

After both phases are complete:

- [ ] `wiki/` contains ~30+ pages with correct YAML frontmatter
- [ ] Every page has at least one outbound `[[wikilink]]`
- [ ] Obsidian graph view shows no orphan nodes
- [ ] `wiki/index.md` lists all pages under correct type headers
- [ ] `wiki/log.md` has entries for seed, lint, and automation setup
- [ ] `C:\Users\joshu\CLAUDE.md` LLM Wiki section reads "Business Brain" not "Japan"
- [ ] n8n workflow runs without errors when triggered manually
- [ ] Claude scheduled agent `business-brain-daily` appears in `/schedule` list
- [ ] `wiki/.last-ingest` contains today's date
