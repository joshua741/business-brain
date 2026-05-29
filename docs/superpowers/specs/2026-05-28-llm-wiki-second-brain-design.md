# LLM Wiki Second Brain — Design Spec

**Date:** 2026-05-28
**Status:** Approved
**Scope:** Full second brain for Joshua — business, personal, finance, health, and life

---

## 1. Purpose

A persistent, compounding knowledge base that lives in Obsidian and is maintained entirely by Claude. Joshua sources and curates; Claude writes, links, and maintains everything. The wiki is the source of truth. Notion master prompts and CLAUDE.md are compressed views derived from it.

---

## 2. Folder Structure

```
C:\Users\joshu\.claude\Business_Brain\
├── raw/                          # immutable source documents — never modified by Claude
│   └── assets/                   # images downloaded from web-clipped articles
├── wiki/                         # LLM-maintained knowledge base
│   ├── index.md                  # master table of contents, grouped by type
│   └── log.md                    # append-only ingest/query/lint history
├── docs/
│   └── superpowers/
│       └── specs/                # design specs (this file)
└── CLAUDE.md                     # wiki schema + rules (governs all wiki behavior)
```

**Rules:**
- Claude never modifies anything in `raw/`
- `wiki/` is Claude's sole writing surface
- `Business Brain/` subfolder (separate Obsidian vault) is untouched

---

## 3. File Conventions

### Naming
All wiki files use lowercase-kebab-case: `vince-ai.md`, `1312-65th-dr.md`, `profit-first.md`

### Frontmatter (required on every wiki page)
```yaml
---
name: vince-ai
type: project          # entity | project | concept | person | source
tags: [ai, ghl, twilio, capital-raising]
status: active         # active | paused | complete | archived
sources: [transcript-2026-05-10.md]
updated: 2026-05-28
---
```

### Page Types

| Type | What it covers | Examples |
|---|---|---|
| `entity` | Things that exist — companies, properties, tools, accounts | `wih.md`, `1312-65th-dr.md`, `ghl.md`, `mercury.md` |
| `project` | Active initiatives with a goal and status | `vince-ai.md`, `lbk-cleaners-launch.md`, `content-ai.md` |
| `concept` | Ideas and frameworks | `profit-first.md`, `rent-to-own.md`, `subject-to.md` |
| `person` | Team, vendors, partners, mentors | `mostafa.md`, `austin-hughes.md`, `alex-hormozi.md` |
| `source` | One page per ingested raw file | `transcript-2026-05-10.md` |

### Wikilinks
Always use clean short-form links: `[[vince-ai]]`, `[[mostafa]]`, `[[profit-first]]`. Never use path prefixes.

### Page Template
```markdown
# Page Title

**Summary**: One to two sentences.

**Sources**: [list of raw source files]

**Last updated**: YYYY-MM-DD

---

Main content. Link related concepts with [[wikilinks]] throughout.

## Related pages
- [[related-page-1]]
- [[related-page-2]]
```

---

## 4. Three-Brain Architecture

Joshua maintains three knowledge layers:

```
Notion Personal Prompt  ←→  raw/  ←→  wiki/  ←→  CLAUDE.md
Notion Business Prompt  ←→  raw/        ↑
Transcripts/Clips/Docs  ──→  raw/  ──→  wiki/
```

| Layer | Purpose | Update cadence |
|---|---|---|
| `raw/` | Immutable sources | n8n daily pull + manual drops |
| `wiki/` | Expanded, detailed knowledge base | Ingest agent after new raw files |
| Notion Personal Prompt | Compressed identity context | When wiki delta is meaningful |
| Notion Business Prompt | Compressed business state | When wiki delta is meaningful |
| `CLAUDE.md` | Working session context | After Notion updates |

**Flow:** Everything feeds `raw/`. `raw/` feeds the wiki. The wiki synthesizes back up to Notion and CLAUDE.md when the delta warrants it.

---

## 5. Automated Daily Cycle

One Claude Code scheduled agent runs daily. Two-phase execution:

### Phase 1 — n8n Notion Pull (3:00 AM)
- n8n polls Notion API for Personal and Business master prompt pages
- Checks `last_edited_time` against last known timestamp
- If unchanged → does nothing (zero tokens)
- If changed → exports as markdown to `raw/notion-personal-YYYY-MM-DD.md` or `raw/notion-business-YYYY-MM-DD.md`

### Phase 2 — Claude Agent (4:00 AM)
1. **Ingest check** — scans `raw/` for files newer than last ingest timestamp
   - If nothing new → exits (zero tokens spent)
   - If new files → ingests each: creates/updates wiki pages, updates `index.md`, appends to `log.md`
2. **Lint** — runs on the wiki silently
   - Auto-fixes: orphan links, missing cross-references, stale `status` fields
   - Flags contradictions it cannot auto-resolve in `log.md` (one line only)
   - Never surfaces findings unless critical
3. **CLAUDE.md delta check** — compares wiki state against current CLAUDE.md
   - If significant delta → proposes a CLAUDE.md update in the next active session

**Token optimization:** On quiet days (nothing changed, nothing new in `raw/`), the cycle costs near zero. Tokens only flow when content actually changed.

---

## 6. Ingest Workflow (Manual Trigger)

When Joshua drops a file into `raw/` and says "ingest this":

1. Claude reads the source in full
2. Discusses key takeaways with Joshua before writing anything
3. Creates a `source` page in `wiki/` summarizing the document
4. Creates or updates entity, project, concept, and person pages touched by the source
5. Links everything with wikilinks
6. Updates `wiki/index.md` with any new pages
7. Appends an entry to `wiki/log.md`

A single source may touch 10–15 wiki pages. That is normal.

---

## 7. Query Workflow

When Joshua asks a question:

1. Claude reads `wiki/index.md` to identify relevant pages
2. Reads those pages and synthesizes an answer with citations
3. Cites specific wiki pages in the response
4. If the answer is valuable, offers to save it as a new wiki page

Good answers are filed back into the wiki so they compound over time.

---

## 8. Lint Workflow (Automated Daily)

Runs silently as part of the daily agent cycle:

- Finds contradictions between pages
- Finds orphan pages (no inbound links from other pages)
- Identifies concepts mentioned but lacking their own page
- Flags claims newer sources may have superseded
- Auto-fixes what it can (broken links, missing cross-references, stale status)
- Appends a one-line summary to `wiki/log.md`
- Never requires Joshua's attention unless a contradiction cannot be auto-resolved

---

## 9. Index & Log Structure

### wiki/index.md
Groups entries by type. Each entry is one line under 150 characters.

```markdown
# Wiki Index

## Entities
- [WIH](wih.md) — Webber Investment Homes, primary real estate operating brand
- [1312 65th Dr](1312-65th-dr.md) — multi-unit property, Unit F active

## Projects
- [Vince AI](vince-ai.md) — PML/TL qualification chatbot, GHL + Twilio + Claude

## Concepts
- [Profit First](profit-first.md) — cash management framework, Mercury accounts

## People
- [Mostafa](mostafa.md) — operations lead, all outbound comms route through him

## Sources
- [transcript-2026-05-10.md](transcript-2026-05-10.md) — coaching call, Vince AI architecture
```

### wiki/log.md
Append-only. Each entry starts with `## [YYYY-MM-DD] operation | title` for grep-ability.

```markdown
## [2026-05-28] seed | Initial wiki seeded from CLAUDE.md context
## [2026-05-28] ingest | transcript-2026-05-10.md — updated vince-ai, mostafa, ghl
## [2026-05-28] lint | 2 orphans fixed, 0 contradictions found
```

---

## 10. Day-One Seed

On initial setup, the wiki is pre-seeded from existing CLAUDE.md context — no raw files needed. This creates starting pages for all known entities, projects, people, and concepts documented in Joshua's master prompts. Raw source ingests then expand and update these pages over time.

---

## 11. Source Routing Convention

| Source type | Raw filename format | Triggers |
|---|---|---|
| Notion Personal export | `notion-personal-YYYY-MM-DD.md` | Person + concept pages |
| Notion Business export | `notion-business-YYYY-MM-DD.md` | Entity + project + person pages |
| Meeting transcript | `transcript-YYYY-MM-DD-topic.md` | All page types |
| Voice memo | `memo-YYYY-MM-DD-topic.md` | All page types |
| Web clip | `clip-YYYY-MM-DD-title.md` | Concept + source pages |
| Document/PDF | `doc-YYYY-MM-DD-title.md` | All page types |
