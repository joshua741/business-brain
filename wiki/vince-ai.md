---
name: vince-ai
type: project
tags: [ai, ghl, twilio, capital-raising, pml, tl]
status: active
sources: [CLAUDE.md seed, vince-master-booklet.md, gumloop-instruction-manual.md]
updated: 2026-05-29
---

# Vince AI

**Summary**: SMS AI agent that qualifies Private Money Lenders and Transactional Lenders end-to-end and books qualified leads on Joshua's calendar. Two builds: a live GHL-native version and an in-progress Gumloop/Twilio/Claude/Notion version.

**Sources**: CLAUDE.md seed; vince-master-booklet.md; gumloop-instruction-manual.md

**Last updated**: 2026-05-29

---

AI SMS agent for qualifying [[pml-tl]] lenders for [[wih]]. Collects name/email/lending type/fund access/capital, answers limited questions, and books intro calls — never marks anyone Qualified without an explicit "VINCE" note from Joshua (source: vince-master-booklet.md).

## Two implementations
- **V1 — GHL-native SMS agent:** live, built inside a [[ghl]] AI Agent workflow (source: vince-master-booklet.md).
- **V2 — Gumloop architecture:** under construction — [[twilio]] (number + inbound webhook), [[gumloop]] automation engine, Claude Sonnet ([[claude-api]]) as the model, [[notion]] "PML Lender Profiles" DB as long-term memory, GHL as CRM only (source: vince-master-booklet.md). See [[gumloop-instruction-manual]].

## Personality & output rules
No exclamation marks, no hype, short human texts; business hours only (9AM–6PM CT M–F), max 4 SMS/contact/day. Every response = Part A (SMS reply) + Part B (structured system updates: contact fields, GHL stage, tags, notes, conversation log, appointment, internal notification, follow-up sequence) (source: vince-master-booklet.md).

## Qualification flow
9 steps: name → email → lending type → fund access → capital → source → questions → booking → confirmation. Capital uses a **three-layer clarification** (per-deal vs total liquid) before any disqualification. Minimums: **TL $5,000, PML $10,000**. Pure connectors confirmed twice then tagged Connector/Disqualified; under-minimum leads enrolled in 180-day re-engagement (source: vince-master-booklet.md). See [[sales-scripts]].

## Integration detail
- GHL pipeline "PML Lenders," phone as dedup key; v2 API for opportunities, v1 for contacts/tags/notes (source: vince-master-booklet.md).
- 10 follow-up/handler flows to build (inbound handler, PML/TL no-response sequences, no-show, rescheduling, re-engagement, etc.) (source: vince-master-booklet.md).

Blockers: V2 Twilio number + Gumloop flows not yet finished; GHL workflows must be paused before V2 go-live.

## Potential voice layer
Vince is SMS-only today. A natural next surface is **voice** — an [[elevenlabs]] agent reusing Vince's persona, qualification knowledge, and booking tools, deployed as an inbound phone line via [[twilio]] (or a web widget). The full build pattern (Claude Code configures the agent and tools, code-first, iteratively debugged) is documented in [[source-voice-agents-elevenlabs]].

## Related pages
- [[ghl]]
- [[twilio]]
- [[claude-api]]
- [[gumloop]]
- [[notion]]
- [[pml-tl]]
- [[sales-scripts]]
- [[mostafa]]
- [[ai-automation-strategy]]
- [[elevenlabs]]
- [[source-voice-agents-elevenlabs]]
