---
name: content-ai
type: project
tags: [ai, social-media, automation, r2oc]
status: active
sources: [CLAUDE.md seed, paste-may-16-2026-8-48am.md, transcript-2026-05-28-morning-meeting-josh-mostafa.md, clip-2026-06-03-the-new-way-of-making-content-in-the-age-of-ai.md]
updated: 2026-06-03
---

# Content AI

**Summary**: Automated social media content pipeline for Rent 2 Own Cribs via Google Sheets and daily automation, with a Google Apps Script approval/posting workflow.

**Sources**: CLAUDE.md seed; paste-may-16-2026-8-48am.md

**Last updated**: 2026-06-03

---

Automates daily social media posts for [[r2oc]]. Driven by [[google-sheets]] as the content source with daily automation triggers. Builds brand awareness for the rent-to-own portfolio without manual effort.

## Apps Script engine
A Google Apps Script (snapshot May 16, 2026) powers the in-sheet workflow via a "Content Studio" custom menu: approve/deny/post/request-revision on a Daily Queue, knowledge-base and audience-question management, scheduling, full-automation run, and a weekly summary email — all changes written to an Audit Log (source: paste-may-16-2026-8-48am.md). Expected tabs: Daily Queue, Knowledge Base, Audience Questions, Brand Intelligence, Pre-Schedule Builder, References, Source URLs, Daily/Monthly Content Identity, Dashboard, Approved Library, Audit Log. See [[source-content-ai-script]].

## Photo-branding skill (Canva MCP)
A reusable Claude "skill" now brands property photos with the [[r2oc]] logo via the Canva MCP integration: canvas 940×626, logo 410×248 placed bottom-right. It enforces a fixed photo order — front → living → kitchen → master bed → master bath → secondary → additional → back exterior — and pulls brand assets from a reusable "Brand Themes" folder. First used to produce listing images + a description for [[4513-48th-st]], posted to Facebook Marketplace.

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
