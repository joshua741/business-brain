---
name: wih-app
type: project
tags: [web-app, railway, supabase, crm, central]
status: active
sources: [CLAUDE.md seed, memo-2026-05-29T14-03-38-session.md, transcript-2026-05-29-morning-meeting-josh-mostafa.md, transcript-2026-06-02-meeting.md, clip-2026-06-03-how-to-build-a-business-intelligence-dashboard-with-claude-a.md]
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

## "Us" — the consolidated in-house app
Joshua now also calls the consolidated in-house app **"Us"** — the one-stop replacement for [[doorloop]], [[ghl]], and the contacts directory, i.e. "everything in the house." Internal [[railway]] project codename is **"Terrific Blessing."** Architecture: [[supabase]] = storage/backup, [[railway]] = hosting.

Major build threads underway:
- **Contacts migration** — moving all ~16,000 [[ghl]] contacts into [[supabase]] as a deduplicated Contacts directory. Data quality is poor: ~89% untagged and only 39 contacts have emails, so cleanup/dedup is part of the work.
- **Wholesale KPI command-center dashboard** — a three-phase build that mirrors the No Fluff Operator GHL→Supabase→Railway/Vercel pattern (see [[source-bi-dashboard-claude]], [[no-fluff-model]], and [[claude-code-workflow]]). Surfaces [[kpi-tracking]] and [[disposition]] metrics.
- **AI lead-reply** via [[twilio]].
- **Google Maps street view** in-app.
- **Notes tab.**

**Long-term goal:** replace [[doorloop]] (~$265/mo, billed per-lease) with a custom property-management dashboard + tenant portal inside this app.

## Feature context to fold in
Running backlog of app-relevant ideas pulled from ingested sources. The daily ingest appends here whenever a new source touches CRM features, AI agents, dashboards, or the three verticals. Review periodically and pull the best into the wih-app dev project.
- **AI / voice agent layer** -- voice agents via ElevenLabs + Twilio for [[vince-ai]]-style flows; could power in-app call/SMS ([[source-voice-agents-elevenlabs]], [[elevenlabs]]).
- **AIOS / agent-operating-system patterns** -- orchestration patterns for an all-in-one AI workspace ([[source-aios-nate-herk]]).
- **Rich contact profiles** -- every lead/contact (sellers, buyers, agents, referrals) should have a full context profile inside the app: referral source, deal structure notes, AI follow-up history, status, timeline. Not just a name + phone. GHL is the backup until the app is functional; app becomes primary.
- **AI follow-up from within the app** -- AI handles automated outreach/follow-up with leads (sellers, buyers, PML) directly from the app. Conversations logged in the app, not just GHL. Unified thread: SMS and email in the same conversation view, filterable by type.
- **Referral tracking** -- when a deal has a referral source, the app tracks: referral contact, agreed amount, notification triggers (when contacted, when under contract, when closed). Referral amount is deal-dependent; system stores it per deal. Samuel Bergen is the first referral source ($1k/$500 split structure, deal-dependent).
- **Calendar page** -- app-native calendar showing closings, follow-up dates, AI handoffs, tasks. Toggle between individual team calendars (Joshua, Mostafa, M'kenzy, Angel, AI) with overlap/filter view. MVP: build without Google backend first, wire Google Calendar later.
- **Email + SMS unified thread** -- all contact correspondence (email + SMS) in one scrollable thread per contact. Click an email in the thread → dropdown shows full email chain → respond from there. Filter view to see only SMS or only email. AI email address for outbound; toggle between email/SMS when composing.
- **Document signing** -- send agreements from within the app. In-house if possible (minimize subscriptions). Signed by counterparty, stored on contact profile. Eventual replacement for any external e-sign subscription.
- **Cash flow gap detection** -- monitor upcoming payment obligations against incoming funds. When a payment is scheduled to pull (e.g., Evergreen on the 1st) and funds are in transit / arriving after the pull date, flag it proactively so funds can be temporarily covered from reserves and restored when the payment lands. Core use case: avoid NSF events caused by timing gaps, not actual shortfalls.
- **RTO outreach KPI dashboard** -- track texts sent, response rate, qualification rate, booking rate (M'kenzy calls booked), no-show rate. Filterable by time period. Lives inside the app; powers performance review for the RTO outreach AI.
- **Google Calendar integration** -- auto-create 30-min events on Joshua's calendar when a lead books a pre-qual call with M'kenzy; add M'kenzy + lead as guests automatically.
- **M'kenzy automated briefing** -- countdown reminders to M'kenzy at 15/10/5/2 min before each pre-qual call; 5-min message includes full property + lead brief (see sales-scripts.md M'kenzy briefing protocol).
- **Incoming (queued for next ingest):** a "build a business intelligence dashboard with Claude" clip and two wholesale-blueprint clips -- relevant to CRM dashboards and the wholesale vertical. Fold their takeaways here once ingested.

## Related pages
- [[wih]]
- [[railway]]
- [[supabase]]
- [[wih-ai-service]]
- [[vince-ai]]
- [[business-brain]]
- [[ai-automation-strategy]]
- [[claude-code-workflow]]
- [[no-fluff-model]]
- [[disposition]]
- [[kpi-tracking]]
