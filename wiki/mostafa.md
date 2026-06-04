---
name: mostafa
type: person
tags: [team, operations, communications]
sources: [CLAUDE.md seed, transcript-2026-05-26-morning-meeting-josh-mostafa.md, transcript-2026-05-29-morning-meeting-josh-mostafa.md]
updated: 2026-06-04
---

# Mostafa (Elkhamisy)

**Summary**: Operations lead. ALL outbound communications go through Mostafa — non-negotiable. Primary human-in-the-loop for AI automations across WIH and LBK Cleaners. Future state: his execution-layer tasks progressively transfer to AI agents/skills as automation matures.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Mostafa is the execution layer for [[wih]] and [[lbk-cleaners]]. Every outbound message — texts, emails, GHL sequences — routes through him. Joshua does not send outbound comms directly. **SOP reaffirmed (May 2026): all outbound comms route through Mostafa.**

He is also the human-in-the-loop for all AI automations. When [[vince-ai]] or other agents need a human decision or review, Mostafa handles it.

For [[lbk-cleaners]], he oversees the [[bookingkoala]] platform — managing bookings, cleaner coordination, and customer communications through [[ghl]] via [[zapier]] integration.

## Delegation SOP — what routes to Mostafa vs. Claude (June 2026)

**Routes to Mostafa:**
- All outbound communications — texts, emails, GHL sequences, anything leaving the business. Non-negotiable.
- Actions requiring portal credentials I don't have (servicer logins, utility accounts, lender portals)
- Payment authorizations and financial actions (paying bills, initiating wires, making calls to servicers)
- Phone calls to vendors, servicers, tenants, or any third party
- Physical or on-site operational tasks

**Claude handles directly:**
- Research, analysis, email monitoring and summarizing
- Wiki, CLAUDE.md, Notion updates
- Database operations (Supabase, app builds, automations)
- Drafting messages, tasks, scripts — then routes execution to Mostafa
- Any task solvable via available tool/API access

**Future state:**
Mostafa's current role is interim infrastructure. As AI automation matures, each category of his execution tasks gets replaced by an AI agent or skill (e.g., Vince AI for capital raising already does this). The long-term model is a fully AI-run operations layer. Mostafa's role evolves from execution toward oversight and exception-handling. This aligns with the [[wih]] "AI-run company" thesis.

## Role and tooling (May 2026)

Mostafa's role is best described as transaction coordinator + appointment setter + IT tech + "master of automations." He is now onboarded onto VS Code + Claude Code + the superpowers plugin and is building automations/skills hands-on (GitHub handle `m_khamisy`; Claude account on docs@webberinvestmenthomes.com). (source: transcript-2026-05-26-morning-meeting-josh-mostafa.md, transcript-2026-05-29-morning-meeting-josh-mostafa.md)

He is named on lender authorization forms as Joshua's authorized assistant (e.g. the [[yvonne-scott-subject-to]] deal).

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
