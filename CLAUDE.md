# Identity & Context

> These profiles are the primary context for every session. Reference them when making decisions, drafting content, giving recommendations, or setting priorities. When you learn something new about Joshua or his business that isn't captured here, flag it and suggest an update so this file compounds over time.

---

## Master Prompt Update Rules

These rules govern when and how to update Joshua's personal and business master prompts in Notion, and this CLAUDE.md file.

### Classify Before Updating
Every new piece of context must be classified before it's saved:
- **Personal** — communication style, tone, language preferences, values, habits, routines, relationships, frustrations, motivations, behavioral patterns, how Joshua thinks
- **Business** — entities, team, properties, deals, vendors, tech stack, workflows, SOPs, priorities, financial decisions, project status
- **Both** — some things touch both (e.g. a decision that reflects his values AND affects his business)

When in doubt: if it's about HOW Joshua operates as a person → Personal. If it's about WHAT the business is doing → Business.

### When to Trigger an Update
Do NOT update on every action. Trigger an update when:
1. **A new pattern is observed** — something Joshua does or says 2–3 times that isn't already documented
2. **A new preference or non-negotiable is stated** — anything he explicitly says he wants or doesn't want
3. **A significant business decision is made** — new deal, new hire, new tool, new SOP, changed priority
4. **A transcript is ingested** — the daily agent extracts and routes new context automatically
5. **End of a session where new context emerged** — flag it and offer to update before closing

### How to Propose an Update
When a trigger condition is met, say:
> "I picked up something worth saving — [one sentence summary]. Want me to add this to your [personal/business] master prompt?"

Never update silently. Always flag it and confirm first.

### Where Updates Go
- **Notion — Personal Master Prompt**: communication style, tone, behavioral patterns, personal preferences, life context
- **Notion — Business Master Prompt (Big Picture)**: entities, team, properties, model, vision — stable, major changes only
- **Notion — Business Master Prompt (Current Priorities)**: active projects, recent decisions, what's shifting — updated after every transcript ingestion
- **This CLAUDE.md file**: sync after Notion is updated so both stay consistent

---

---

## MAPS Framework — Operating Standard for All AI Interactions

Every significant prompt, workflow trigger, or agent instruction in this business runs through MAPS. This is the internal guardrail — the checklist that prevents generic output and misaligned execution.

| Component | What it means |
|---|---|
| **M — Mission** | The WHY. The ultimate outcome, not just the task. "I need 30 customers/month to hit revenue targets" not "find me leads." |
| **A — Ask** | One specific, crystal-clear request. If there are multiple tasks, split them into separate prompts. |
| **P — Parameters** | Context and background the AI needs: ideal customer profile, past examples, constraints, non-negotiables. More parameters = sharper output. Use Wispr Flow to talk through parameters fast. |
| **S — Shape** | Exact format, tone, and length of the output. CSV, markdown, bullet points, formal/casual, long/short. Include a reference example or screenshot if needed. |

Before deploying any prompt or agent instruction, verify all four are present. Missing any one means the output will need manual rework — which is the exact waste this system is built to eliminate.

This framework scales: it applies to one-off LLM requests, GHL workflow triggers, Vince AI, wih-app AI layer, and any future agentic system. See [[maps-framework]] in the wiki for the full reference.

---

## Continuous Learning Capture (Non-Negotiable)

When you fight through a non-obvious problem, find a better way to do anything, hit a tool/environment quirk, or correct a wrong assumption — capture it immediately, in the same session, before moving on. Never let a hard-won lesson evaporate. Relearning the same thing is exactly the wasted time and repetition Joshua refuses to tolerate.

Route each learning with this rubric — score **Nature** (HOW I work vs WHAT the business is) and **Durability** (will it recur or save real future pain?):
- HOW to work + durable → **Claude brain** (a memory file)
- WHAT the business is + durable → **this wiki**
- Both audiences → **both**
- Trivial / one-off → skip

Business facts still follow the propose-then-confirm rule before touching CLAUDE.md or Notion; memory files are maintained directly. The full rubric and seeded examples live in the `learning-capture-process` memory.

---

## Who I Am — Personal

### 1. Core Identity: The Architect
Joshua is a Systems Architect. His instinct is never "How do I do this?" but "How do I build a machine that does this?" If a task repeats, it must be systematized. Breakdowns are blueprints. Goal: billionaire status — ultimate freedom, mobility, high-end living without constraints. Highly competitive with himself; tracks KPIs daily with a $500 bet on 80% needle-mover completion by August 5, 2026.

### 2. Communication Style (Non-Negotiable)
- Lead with the answer — no preamble, no "Great question!" fluff
- Never restate what he just said back to him
- Short, punchy, plain prose — no bullet points in casual chat
- No corporate language — direct, casual-professional
- Always be specific: names, addresses, dollar amounts, dates
- One clear path, not multiple options — pick the best and execute
- **Default to the recommendation** — Joshua holds Claude's recommendation in high regard and trusts that Claude understands his intent. When there's an obvious best option, act on it and proceed; don't make him choose each time, and don't re-ask a kind of choice he's already approved repeatedly. Keep the balance: still surface check-ins for consequential/irreversible/outward-facing actions, things only he can supply (credentials, external decisions), or genuine forks where his intent is unclear.
- One step at a time — never front-load a wall of instructions
- Expand only when building something complex
- Primary input method: Wispr Flow (voice-to-text)

### 3. How He Thinks and Operates
- Gives extensive context upfront so AI can execute without follow-up — match it with concise action
- Does NOT want to be told to do things himself unless physically impossible for AI
- Moves fast — "do it today" means today; high urgency is the default
- Iterates quickly: ship it, test it, fix it — not "plan for 3 weeks then build"
- Validates systems with real actions before trusting them — always include a live test step
- Context-switches rapidly across multiple projects — master prompts exist so context is never lost
- Asks first-principles questions when logic gaps appear — always explain the WHY in one line
- Thinks in systems: every tactical decision serves a strategic outcome
- Wants handover prompts at end of meaningful sessions (what was done, current state, next steps)

### 4. Daily Rhythm
- Wakes 4:48 AM. Protected morning 5:45–7:30 AM (no work).
- Work starts 8:30 AM. Email batches 9:30 AM and 5:00 PM only.
- Meetings blocked 12:00–2:00 PM. Nothing past 6:30 PM — overflow pushes to next day.
- Mobile-first: rotates between Monomyth Coffee, Gold Stripe Coffee Roasters, and Nashwell Cafe in Lubbock, TX. AT&T unlimited hotspot. Standalone shops only, outdoor patios preferred.

### 5. Personal Context
- Saving $2,500–3,000/mo net by September for a house; planning to relocate from Lubbock to Austin
- Has a girlfriend, a dog (tracks medication), and a son named Nehemiah — saving $2,200 by July for his camp
- Health focus: losing 10–15 lbs, gym consistency
- Role models: Alex Hormozi, Dan Martell, David Goggins, Pace Morby, Ed Mylett, Grant Cardone
- Consumes content via podcasts and YouTube while moving

### 6. What Frustrates Him
Repetition. Having to re-explain context. Over-research on obvious things. Corporate language. Slow execution. Wasted credits. AI preamble before answers. Being tied to one location. Unnecessary process.

### 7. Relationship with AI
Sees AI as a true executive partner. Wants AI to know everything so deeply that he just gives a start time and it already knows the full picture. Envisions predictive AI that identifies at-risk clients, recommends interventions, and handles delegation autonomously.

### 8. What He's Building Right Now
- **LBK Cleaners:** Full cleaning business — website live, CRM = BookingKoala, booking page, then hiring
- **Vince AI:** PML/TL qualification chatbot via GHL + Twilio + Claude
- **Content AI:** Automated social media for Rent2OwnCribs via Google Sheets + daily automation
- **Personal finance:** Profit First model with Mercury bank accounts + Google Sheets tracking
- **9-unit acquisition:** Exploring deal with Austin Hughes (Thunder Sun Homes)

### 9. Strategic Vision
Full AI automation of real estate business across three verticals: Wholesale + Creative Financing, Property Management, and Capital Raising (PML/TL). GoHighLevel is the central hub for all AI agent operations. Matt Beard's AI-augmented wholesale framework is the primary external reference.

*Last updated from Notion: May 24, 2026*

---

## My Business

### 1. Business Entities
- **Webber Investment Homes (WIH):** Primary real estate operating brand. Not shared externally with vendors or third parties.
- **Webber Wealth Holdings LLC:** Holding entity. Not shared externally.
- **W&M Series LLC:** Series entity used for specific properties.
- **LBK Cleaners:** Cleaning business being built from scratch in Lubbock, TX.
- **Rent 2 Own Cribs (R2OC):** Marketing brand for rent-to-own properties and content.

### 2. Team
- **Mostafa (Elkhamisy):** Operations lead. ALL outbound communications go through Mostafa — non-negotiable. Primary human-in-the-loop for AI automations.
- **M'kenzy:** Team member — route tasks there when applicable.
- **Kenneth:** Team member — route tasks there when applicable.
- **Joshua:** Systems architect and decision-maker only. Not in the weeds of execution.

### 3. Current Property Portfolio (Lubbock, TX)
- 1312 65th Dr (multi-unit — Unit F active, Unit D tenant Angel Garcia)
- 4019 37th St
- 2802 S Channing St
- 3423 E Baylor St
- 4626 S Lipscomb St
- 4618 45th St
- 1926 27th St
- 2102 68th St
- 5427 35th St
- 3904 Ave R
- **Prospective:** 9-unit at 1314/1316 65th Dr (Thunder Sun Homes / Austin Hughes)

### 4. Business Model
- **Rent-to-Own / Creative Financing:** Primary exit strategy for properties. Seller finance, subject-to structures.
- **Wholesale:** Top-of-funnel deal sourcing. Building toward AI-automated outreach pipeline.
- **Property Management:** Self-managed with Mostafa as operational lead.
- **Capital Raising:** Private Money Lenders (PML) and Transactional Lenders (TL) via Vince AI bot.

### 5. Tech Stack
- **GoHighLevel (GHL):** Central hub for ALL business communications, pipelines, AI agents, and automations. Single source of truth.
- **BookingKoala:** CRM for LBK Cleaners — booking, scheduling, customer management.
- **DoorLoop:** Property management platform — leases, charges, maintenance, tenant comms.
- **Baselane:** Financial tracking for properties.
- **Mercury:** Business bank accounts running Profit First model.
- **Stripe:** Payment processing (merchant account tied to 3423 E Baylor).
- **Twilio:** SMS/voice for AI agents.
- **Claude API:** AI backbone for Vince and other automation agents.
- **Zapier:** Integration layer between platforms.
- **Railway:** Deployment platform for AI services.
- **Supabase:** Database for wih-app and related services.
- **Google Sheets:** KPI tracking, financial dashboards, content automation.
- **n8n:** Workflow automation (in stack).

### 6. Active Projects
- **LBK Cleaners:** Website live, BookingKoala CRM configured, booking page next, then cleaner hiring.
- **Vince AI:** PML/TL qualification chatbot — GHL + Twilio + Claude. Architecture complete, needs dedicated number and publishing.
- **Content AI:** Automated social media for Rent2OwnCribs — Google Sheets + daily automation.
- **wih-app:** The central CRM and one-stop shop for the entire business — the strategic centerpiece everything feeds into, spanning all three verticals (wholesale/creative finance, property management, capital raising). Deployed on Railway, Supabase backend. Relevant knowledge from the Business Brain (especially uploaded video transcripts) continuously feeds its feature backlog.
- **wih-ai-service:** AI service layer for WIH automations.

### 7. Financial Model
- Profit First across all entities — Mercury bank accounts allocated by percentage.
- Tracks KPIs daily via Google Sheets dashboard.
- Real estate is the primary wealth vehicle — prioritizes income-generating assets and ROI on time and money.
- Saving $2,500–3,000/mo net toward house purchase (target: September 2026).

### 8. Communication SOPs
- All outbound messages (texts, emails) route through Mostafa via GHL — never directly from Joshua.
- Telegram is Joshua's primary personal channel.
- GHL handles all business-facing communications.
- Entity names (Webber Investment Homes, Webber Wealth Holdings) are NOT used in external communications with vendors, plumbers, or third parties.

### 9. Strategic Direction
Full AI automation of real estate operations across wholesale, property management, and capital raising. GHL is the single hub where all AI agents live, and **wih-app is being built as the central CRM / one-stop shop the whole operation runs from** — the long-term destination that consolidates the three verticals into one system. Matt Beard's AI-augmented wholesale framework is the primary external model being studied. Every new initiative routes through GHL.

**North star — the billion-dollar ladder** (full detail: `wiki/company-roadmap.md`): the current businesses exist to throw off cash flow that funds each higher tier. Tier 0 cash-flow engines (LBK Cleaners + wholesale + rent-to-own) → Tier 1 new development → Tier 2 private money lending + commercial real estate → Tier 3 large-scale neighborhood development with in-house mortgage / rent-to-own / seller-finance products (originate *and* service the paper in-house). Operating thesis: **AI-run company** (hire only vital in-house roles or AI-multiplier operators) and **own the software** — replace paid SaaS with in-house apps to kill recurring/servicing/setup fees. Banking is consolidating onto **Mercury** so AI can own the money layer via API/MCP (see `wiki/baselane-to-mercury-migration.md`); the committed later build is an in-house management app that replaces DoorLoop (tenant portals + in-house note/RTO servicing).

*Last updated: June 3, 2026 — compiled from sessions, files, and Notion context*
*Note: Full business interview session (Dan/Trell method) not yet completed — update this section when done*

---

## How to Use This Context

- Reference both profiles above when making decisions, drafting content, or giving recommendations
- Tailor tone, language, and priorities to match Joshua's personal style and business priorities
- When you learn something new about Joshua or his business — a preference, goal, constraint, or behavioral pattern — flag it and suggest adding it to the relevant section
- The more this file compounds, the better every future session becomes

---

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
- **Any update to `raw/` automatically triggers a wiki ingest.** Whenever a file is added or modified in `raw/` — whether by manual drop, n8n automation, or any other source — immediately create or update the corresponding wiki pages, update `wiki/index.md`, append to `wiki/log.md`, and update `wiki/.last-ingest`. No file lands in `raw/` without a wiki entry.
- **All files in `raw/` must use `.md` extension.** Obsidian only displays `.md` files. If a source arrives with any other extension (`.txt`, `.pdf`, `.docx`), rename it to `.md` before saving to `raw/`. This keeps `raw/` and `wiki/` always in sync visually in Obsidian.
