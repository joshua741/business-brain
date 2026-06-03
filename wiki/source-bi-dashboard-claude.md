---
name: source-bi-dashboard-claude
type: source
tags: [clip, wih-app, kpi-tracking, ghl, supabase, claude-code]
status: complete
sources: [clip-2026-06-03-how-to-build-a-business-intelligence-dashboard-with-claude-a.md]
updated: 2026-06-03
---

# How To Build a Business Intelligence Dashboard With Claude AI

**Summary**: A real-estate wholesale operator ("No Fluff Operator") live-builds a three-phase KPI dashboard with Claude Code on a GHL → Supabase → Vercel stack — a near-exact mirror of the wih-app architecture and use case.

**Sources**: clip-2026-06-03-how-to-build-a-business-intelligence-dashboard-with-claude-a.md

**Last updated**: 2026-06-03

---

A no-code live build of a real-estate KPI dashboard via Claude Code, by an operator building a "Deal Generator" off [[ghl]].

## Core method / framework (in order)
1. **Goal** — one app as source of truth feeding an AI agent that tells you priority one each day.
2. **Scaffolding** — define key features first; AI organizes folders.
3. **Plan Mode first** (or you run out of context).
4. **Three-phase KPI model** w/ red/green thresholds:
   - **Phase 1 Lead Gen** — ≥95% deliverability, ≥8% response, ≤12% fail, ≤3% opt-out, ~500 texts/day
   - **Phase 2 Conversion / Call-Comp-Close** — no deal in "Second Call" >48 hrs; 1 contract per 20 off-market leads
   - **Phase 3 Disposition** — time-to-blast <36 hrs; ≥70% of dispo deals close; buyers list New/Vetted/A-tier
5. **MCP** = "Bluetooth for all applications."
6. **Integration** — GHL Private Integration token (all scopes) + Location ID; Supabase project + paste AI-provided SQL schema; Anthropic API key (console.anthropic.com); secrets in `.env.local`.
7. **Verify locally** — `npm run dev` → localhost; let Claude fix its own runtime errors; iterate CSS via a screenshot in a "design inspiration" folder.
8. **Automate** — cron sync every 6 hrs; auto-calc Phase 1 KPIs; trend graphs.
9. **Deploy** — GitHub → auto-deploy to Vercel on push.

## Tools
Claude Code, Google Antigravity, VS Code, GoHighLevel (Private Integrations + Location ID), Supabase, Vercel, GitHub, Anthropic API, Next.js, cron, MCP.

## Numbers & benchmarks
- Phase 1: ≥95% deliverability, ≥8% response, ≤12% fail, ≤3% opt-out, ~500 texts/day
- Phase 2: 48-hr Second Call SLA; 1 contract per 20 off-market leads
- Phase 3: time-to-blast <36 hrs; ≥70% dispo close
- Build time: "within an hour and a half... something actually usable"

## Actionable for Joshua
- Near-exact mirror of [[wih-app]]'s stack (GHL → Supabase → Railway/Vercel) and use case — build the three-phase KPI dashboard as the wih-app command center across his verticals.
- Reuse the wholesale KPI thresholds (95/8/12/3; 48-hr Second Call SLA; 1-in-20 contract; 36-hr TTB; 70% dispo close) — feeds [[kpi-tracking]].
- GHL Private Integration token (all scopes) + Location ID = exact recipe for his GHL connector.
- Add a Claude-generated "AI briefing / what to focus on today" layer to his morning briefings.
- Bake in cron auto-sync + self-healing build loop.
- The creator is also "moving Deal Generator off GoHighLevel" — same direction as Joshua's "own the software / replace SaaS" thesis.

## Maps to
[[wih-app]], [[ai-operating-system]], [[ai-automation-strategy]], [[ghl]], [[supabase]], [[railway]], [[claude-api]], [[business-brain]], [[kpi-tracking]], [[no-fluff-model]], [[disposition]]

## Key verbatim lines
- "Build an app that will tell you exactly what's happening in your business."
- "it all starts with a concept with key features... that's scaffolding."
- "Bluetooth for all applications... that's what MCP is."
- "if you just start building stuff, you're going to run out of context."
- "no one will ever be able to build what I'm building because everything... is specific to having very deep knowledge."
- "Within an hour and a half, we can make something actually usable."

## Related pages
- [[wih-app]]
- [[kpi-tracking]]
- [[no-fluff-model]]
- [[ghl]]
- [[supabase]]
