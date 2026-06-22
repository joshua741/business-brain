---
name: content-ai
type: project
tags: [ai, social-media, automation, r2oc]
status: active
sources: [CLAUDE.md seed, paste-may-16-2026-8-48am.md, transcript-2026-05-28-morning-meeting-josh-mostafa.md, clip-2026-06-03-the-new-way-of-making-content-in-the-age-of-ai.md, transcript-2026-06-12-morning-meeting-josh-mostafa.md]
updated: 2026-06-22
---

# Content AI

**Summary**: Automated social media content pipeline for Rent 2 Own Cribs via Google Sheets and daily automation, with a Google Apps Script approval/posting workflow.

**Sources**: CLAUDE.md seed; paste-may-16-2026-8-48am.md

**Last updated**: 2026-06-22

---

Automates daily social media posts for [[r2oc]]. Driven by [[google-sheets]] as the content source with daily automation triggers. Builds brand awareness for the rent-to-own portfolio without manual effort.

## Apps Script engine
A Google Apps Script (snapshot May 16, 2026) powers the in-sheet workflow via a "Content Studio" custom menu: approve/deny/post/request-revision on a Daily Queue, knowledge-base and audience-question management, scheduling, full-automation run, and a weekly summary email — all changes written to an Audit Log (source: paste-may-16-2026-8-48am.md). Expected tabs: Daily Queue, Knowledge Base, Audience Questions, Brand Intelligence, Pre-Schedule Builder, References, Source URLs, Daily/Monthly Content Identity, Dashboard, Approved Library, Audit Log. See [[source-content-ai-script]].

## Photo-branding skill (Canva MCP)
A reusable Claude "skill" now brands property photos with the [[r2oc]] logo via the Canva MCP integration: canvas 940×626, logo 410×248 placed bottom-right. It enforces a fixed photo order — front → living → kitchen → master bed → master bath → secondary → additional → back exterior — and pulls brand assets from a reusable "Brand Themes" folder. First used to produce listing images + a description for [[4513-48th-st]], posted to Facebook Marketplace.

## NotebookLM integration (Jun 2026)
As of June 12, 2026, Mostafa is using **NotebookLM** to generate AI-written property listing copy — feeding property details in and pulling out professional descriptions. First live test: video + photos for a living room listing, scheduled and posted on time. Quality described as "so professional, so perfect" with phone number and property website link included. (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

**CapCut** identified as a next tool for creating short-form video clips (reels/shorts) from existing property footage — not yet in use but flagged for consideration.

## Content volume (Jun 12, 2026)
**16 days of content queued** at 2 posts/day as of June 12, 2026. (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

## Facebook strategy — cross-posting SOP
Key distinction established June 12, 2026 (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md):
- **Cross-post, do NOT share.** Sharing a post underperforms algorithmically vs. creating the same content independently on each destination. Cross-posting behaves as an independent post on each group/page and reaches far more people.
- **Post as the R2OC Facebook PAGE to the Facebook GROUP.** Switch to acting as the page before posting — this builds brand credibility and correct attribution.
- **Always change the Marketplace listing title.** A $9,200 listing without a descriptive title looks like a scam — one listing triggered an actual scam report because the title was never changed. Title must include context (e.g., "Rent to Own – $9,200 Down").
- **Two highest-traffic drivers:** text blasts + bandit signs. Facebook alone does not replicate the traffic spike from these two channels.

## Strategic frame — proof-based content
From Alex Hormozi ([[source-new-way-content-ai]]): proof-based content wins — *"do epic shit and document it."* The [[business-brain]] transcript pipeline is reused to extract "interesting moments" into the content backlog at zero extra capture cost — a "self-licking ice cream cone" that turns work already being done into content. Ties into the [[information-moat]] thesis.

## Related pages
- [[r2oc]]
- [[google-sheets]]
- [[ghl]]
- [[ai-automation-strategy]]
- [[source-content-ai-script]]
- [[business-brain]]
- [[information-moat]]
- [[4513-48th-st]]
- [[source-transcript-2026-06-12]]
