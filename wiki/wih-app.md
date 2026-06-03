---
name: wih-app
type: project
tags: [web-app, railway, supabase, crm, central]
status: active
sources: [CLAUDE.md seed, memo-2026-05-29T14-03-38-session.md]
updated: 2026-06-03
---

# WIH App

**Summary**: The central CRM and one-stop shop for the entire business. Main WIH web application, deployed on Railway with a Supabase backend. This is the destination everything else feeds into.

**Sources**: CLAUDE.md seed; session memo 2026-05-29

**Last updated**: 2026-06-03

---

The primary web application for [[wih]] and the **strategic centerpiece**: wih-app is being built to be the business's CRM -- a single one-stop shop covering all three verticals (wholesale + creative financing, property management, capital raising). The goal is for the team to run the entire operation from this app rather than stitching together separate tools. Deployed on [[railway]] with [[supabase]] as the PostgreSQL backend; AI capabilities via [[wih-ai-service]].

Because it is the central system, **relevant knowledge accumulating in this Business Brain -- especially Joshua's uploaded video transcripts and clips -- should continuously feed app improvements.** App-relevant material is collected in the "Feature context to fold in" section below so it is never lost and can be pulled into the [[business-brain|Business Brain]] -> wih-app development loop.

## Deployment facts (source: memo-2026-05-29T14-03-38-session.md)
- **Railway project:** `terrific-blessing` = wih-app
- **Live URL:** https://web-production-bcdba.up.railway.app
- **Stack:** React/Vite frontend (`client/`) + Node backend (`src/server.ts`) + Postgres
- **Local code:** `C:\Users\joshu\wih-app`
- **GitHub:** `github.com/joshua741/wih-app` -- pushes to `origin` auto-deploy to Railway
- Note: wih-app-specific working/dev context lives in the `C--Users-joshu-wih-app` project memory, not this wiki. This page is the business-level view + the feature-idea pipeline.

## Feature context to fold in
Running backlog of app-relevant ideas pulled from ingested sources. The daily ingest appends here whenever a new source touches CRM features, AI agents, dashboards, or the three verticals. Review periodically and pull the best into the wih-app dev project.
- **AI / voice agent layer** -- voice agents via ElevenLabs + Twilio for [[vince-ai]]-style flows; could power in-app call/SMS ([[source-voice-agents-elevenlabs]], [[elevenlabs]]).
- **AIOS / agent-operating-system patterns** -- orchestration patterns for an all-in-one AI workspace ([[source-aios-nate-herk]]).
- **Incoming (queued for next ingest):** a "build a business intelligence dashboard with Claude" clip and two wholesale-blueprint clips -- relevant to CRM dashboards and the wholesale vertical. Fold their takeaways here once ingested.

## Related pages
- [[wih]]
- [[railway]]
- [[supabase]]
- [[wih-ai-service]]
- [[vince-ai]]
- [[business-brain]]
- [[ai-automation-strategy]]
