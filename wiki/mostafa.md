---
name: mostafa
type: person
tags: [team, operations, communications]
sources: [CLAUDE.md seed, transcript-2026-05-26-morning-meeting-josh-mostafa.md, transcript-2026-05-29-morning-meeting-josh-mostafa.md, transcript-2026-06-04-morning-meeting-josh-mostafa.md, transcript-2026-06-12-morning-meeting-josh-mostafa.md]
updated: 2026-06-22
---

# Mostafa (Elkhamisy)

**Summary**: Operations lead. ALL outbound communications go through Mostafa — non-negotiable. Primary human-in-the-loop for AI automations across WIH and LBK Cleaners.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Mostafa is the execution layer for [[wih]] and [[lbk-cleaners]]. Every outbound message — texts, emails, GHL sequences — routes through him. Joshua does not send outbound comms directly. **SOP reaffirmed (May 2026): all outbound comms route through Mostafa.**

He is also the human-in-the-loop for all AI automations. When [[vince-ai]] or other agents need a human decision or review, Mostafa handles it.

For [[lbk-cleaners]], he oversees the [[bookingkoala]] platform — managing bookings, cleaner coordination, and customer communications through [[ghl]] via [[zapier]] integration.

## Role and tooling (May 2026)

Mostafa's role is best described as transaction coordinator + appointment setter + IT tech + "master of automations." He is now onboarded onto VS Code + Claude Code + the superpowers plugin and is building automations/skills hands-on (GitHub handle `m_khamisy`; Claude account on docs@webberinvestmenthomes.com). (source: transcript-2026-05-26-morning-meeting-josh-mostafa.md, transcript-2026-05-29-morning-meeting-josh-mostafa.md)

He is named on lender authorization forms as Joshua's authorized assistant (e.g. the [[yvonne-scott-subject-to]] deal).

## Content AI work (Jun 2026)
Mostafa is actively building out the [[content-ai]] pipeline. As of June 12, he used **NotebookLM** to generate AI-written property listing copy and tested scheduled Facebook posting — post went live on time. He also clarified the Facebook cross-posting SOP (create independently on each destination rather than sharing). (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

## wih-app onboarding via VS Code Live Share (Jun 12, 2026)
Joshua onboarded Mostafa onto the [[wih-app]] codebase using **VS Code Live Share** on June 12, 2026. Mostafa joined the session, viewed the Pipeline/Stages view, and received a handover document. Going forward, Joshua keeps his desktop running so Mostafa can continue working on the app independently in later sessions. (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

## AI operating principles for Mostafa (Jun 12, 2026)
Joshua coached Mostafa on how to work more efficiently with AI:
- When AI goes in circles, tell it to find a more efficient path and save that as internal memory.
- AI should self-improve: save better solutions as internal memory so the same mistake isn't repeated.
- Give AI compressed, precise instructions rather than broad requests — reduces unnecessary back-and-forth.
- AI should act as the field expert and pick the most efficient implementation, not present multiple options.
(source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

## AI skills centralization (Jun 17, 2026)
As of June 17, a plan was finalized to centralize AI skills for both Joshua and Mostafa in a **private GitHub repo** with a **cron-based sync agent** running every 6 hours or daily. Agent auto-finds new/updated skills in local directories and pushes to the shared repo. Mostafa gets repo access once set up. Zero manual involvement after one-time setup. (source: transcript-2026-06-17-morning-meeting-josh-angel.md)

## GitHub collaboration — Business Brain (Jun 2026)
Mostafa was **added as a collaborator on the Business Brain GitHub repository** on June 4, 2026. His Claude Code instance (opened in the Business Brain directory) reads the same CLAUDE.md automatically — giving him full business context from the start of every session. His Claude operates from the same wiki but with a different lens: execute and handle operations, escalate decisions to Joshua's Claude. No separate repo or sync drift. (source: transcript-2026-06-04-morning-meeting-josh-mostafa.md)

Works remotely from Egypt, often overnight relative to Central time. Task management is migrating from [[ghl]] into [[notion]] (a dedicated Team Space).

## Related pages
- [[wih]]
- [[lbk-cleaners]]
- [[ghl]]
- [[vince-ai]]
- [[bookingkoala]]
- [[joshua]]
- [[mkenzy]]
- [[kenneth]]
- [[notion]]
- [[yvonne-scott-subject-to]]
- [[wih-app]]
- [[content-ai]]
- [[source-transcript-2026-06-12]]
- [[source-transcript-2026-06-17]]
