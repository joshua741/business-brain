---
name: gumloop
type: entity
tags: [automation, ai, no-code, tool]
status: active
sources: [gumloop-instruction-manual.md, vince-master-booklet.md]
updated: 2026-05-29
---

# Gumloop

**Summary**: No-code AI automation platform chosen as the engine for the V2 build of [[vince-ai]]. Splits builds into Agents (the brain) and Workflows (the nervous system).

**Sources**: gumloop-instruction-manual.md; vince-master-booklet.md

**Last updated**: 2026-05-29

---

A no-code AI automation platform sitting between simple automation tools and full developer systems. Core architecture: **Agents** (persistent, instruction-driven AI that makes decisions) and **Workflows** (event-triggered step sequences that move data and call agents). Build order is always Agent-first, tested standalone, before wiring into a Workflow (source: gumloop-instruction-manual.md).

## Use in the stack
Powers the V2 [[vince-ai]] architecture: Twilio webhook → parse → [[notion]] MCP lookup → Ask AI (Vince agent on Claude Sonnet) → Twilio outbound (Python custom node) → Notion update → [[ghl]] update → conditional notifications/follow-ups (source: vince-master-booklet.md, gumloop-instruction-manual.md).

## Key rules
- Credentials stored as environment variables (e.g. `TWILIO_ACCOUNT_SID`), never hardcoded.
- "Allow Self-Updates" OFF for production agents.
- Every outbound-messaging workflow needs a business-hours gate (9AM–6PM CT).
- Notion MCP requires the integration added as a Connection on the target database; field names must match exactly (source: gumloop-instruction-manual.md). See [[source-gumloop-manual]].

## Related pages
- [[vince-ai]]
- [[twilio]]
- [[notion]]
- [[claude-api]]
- [[ghl]]
- [[n8n]]
- [[source-gumloop-manual]]
