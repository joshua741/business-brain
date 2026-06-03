---
name: notion
type: entity
tags: [tool, database, memory, ai]
status: active
sources: [vince-master-booklet.md, gumloop-instruction-manual.md, CLAUDE.md seed, memo-2026-05-29T12-49-45-session.md]
updated: 2026-06-03
---

# Notion

**Summary**: Database/knowledge tool that hosts Joshua's master prompts and serves as long-term memory for AI agents (e.g. Vince's "PML Lender Profiles" database).

**Sources**: vince-master-booklet.md; gumloop-instruction-manual.md; CLAUDE.md seed

**Last updated**: 2026-05-29

---

Notion holds the **Personal** and **Business Master Prompts** that are compressed views of this wiki (per CLAUDE.md). It also serves as AI agent memory: the V2 [[vince-ai]] build uses a Notion database **"PML Lender Profiles"** (phone as primary lookup key, append-only conversation history) accessed via the [[gumloop]] Notion MCP node (source: vince-master-booklet.md).

> **Note:** Per memory, teamspaces and member invites can't be created via the Notion API (UI-only). Joshua creates the teamspace in the UI; the API/MCP fills it.

**Queued build — "Daily Tasks — Mostafa" database** (blocked on Notion MCP auth as of 2026-05-29): a Task DB inside [[mostafa]]'s teamspace with fields Task, Date, Priority, Category, Property (tied to the Lubbock portfolio), Status, Notes, plus Today / This Week / Done views — so Mostafa sees done vs. pending each day. Fully specced; next step is reconnecting Notion via `/mcp` before building (source: memo-2026-05-29T12-49-45-session.md).

## Related pages
- [[vince-ai]]
- [[gumloop]]
- [[ai-automation-strategy]]
- [[ghl]]
- [[mostafa]]
