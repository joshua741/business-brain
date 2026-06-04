---
name: vince-ai
type: project
tags: [ai, ghl, twilio, capital-raising, pml, tl]
status: active
sources: [CLAUDE.md seed, vince-master-booklet.md, gumloop-instruction-manual.md]
updated: 2026-06-04
---

# Vince AI

**Summary**: SMS AI agent that qualifies Private Money Lenders and Transactional Lenders end-to-end and books qualified leads on Joshua's calendar. Runs entirely on a [[ghl]] workflow under [[webber-wealth-holdings]] — it does **not** use Gumloop.

**Sources**: CLAUDE.md seed; vince-master-booklet.md; gumloop-instruction-manual.md

**Last updated**: 2026-06-03

---

AI SMS agent for qualifying [[pml-tl]] lenders for [[wih]]. Collects name/email/lending type/fund access/capital, answers limited questions, and books intro calls — never marks anyone Qualified without an explicit "VINCE" note from Joshua (source: vince-master-booklet.md).

## Engine: GHL-native (not Gumloop)
Vince runs **entirely on a [[ghl]] workflow** under [[webber-wealth-holdings]]. The AI Agent, qualification logic, and follow-up sequences all live inside GHL — it does **not** use Gumloop. (Earlier notes that described a separate Gumloop/Twilio automation engine as Vince's V2 are superseded; GHL is the engine.)

## Personality & output rules
No exclamation marks, no hype, short human texts; business hours only (9AM–6PM CT M–F), max 4 SMS/contact/day. Every response = Part A (SMS reply) + Part B (structured system updates: contact fields, GHL stage, tags, notes, conversation log, appointment, internal notification, follow-up sequence) (source: vince-master-booklet.md).

## Qualification flow
9 steps: name → email → lending type → fund access → capital → source → questions → booking → confirmation. Capital uses a **three-layer clarification** (per-deal vs total liquid) before any disqualification. Minimums: **TL $5,000, PML $10,000**. Pure connectors confirmed twice then tagged Connector/Disqualified; under-minimum leads enrolled in 180-day re-engagement (source: vince-master-booklet.md). See [[sales-scripts]].

## Integration detail
- GHL pipeline "PML Lenders," phone as dedup key; v2 API for opportunities, v1 for contacts/tags/notes (source: vince-master-booklet.md).
- 10 follow-up/handler flows to build (inbound handler, PML/TL no-response sequences, no-show, rescheduling, re-engagement, etc.) (source: vince-master-booklet.md).

**Vince is LIVE as of 2026-06-03.** Production number confirmed: **+18XXXXX2532** (source: [[source-twilio-sms-log-2026-06-04]]). The dedicated-number blocker is resolved. The agent is actively engaging contacts on acquisition outreach — asking about off-market/stalled listings — not just PML/TL qualification. A full **"Vince master booklet"** spec exists ([[source-vince-master-booklet]]).

## Build spec: Vince as an acquisitions agent
The 2026 [[wholesale]] frameworks now give Vince a concrete next-build target — extending him from PML/TL qualification into an **AI acquisitions agent**:
- **Discovery-call state machine** — the 15-part [[mls-two-call-closing]] script plus [[agent-outreach]] branching logic, encoded as a stateful GHL conversation flow.
- **Automated texting cadences** — the [[no-fluff-model]] sequence (**5 texts → 60-day wait → 5 more**) and the **triple-dial follow-up** cadence from [[sales-scripts]].
- **Commission-flex logic** — the dual/double-dip commission angle from [[agent-outreach]], applied dynamically per agent.

This acquisitions build feeds [[wih-app]] as the central CRM. See [[disposition]] for the buyer-side handoff.

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
- [[no-fluff-model]]
- [[agent-outreach]]
- [[mls-two-call-closing]]
- [[disposition]]
- [[wih-app]]
