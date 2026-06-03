---
name: ai-automation-strategy
type: concept
tags: [ai, strategy, ghl, automation]
sources: [CLAUDE.md seed]
updated: 2026-06-03
---

# AI Automation Strategy

**Summary**: Full AI automation of WIH real estate operations across three verticals using GoHighLevel as the central hub.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

The strategic direction for [[wih]]: automate all three business verticals — [[wholesale]] (deal sourcing), property management, and capital raising ([[pml-tl]]) — with AI agents living inside [[ghl]]. Every new AI initiative routes through GHL. Primary external reference: [[matt-beard]]'s AI-augmented wholesale framework. Active implementations: [[vince-ai]] (capital raising) and [[content-ai]] (brand). Joshua envisions predictive AI that identifies at-risk clients, recommends interventions, and handles delegation autonomously.

The [[ai-operating-system]] framework ([[nate-herk]]) gives this structure: the Business Brain already scores high on **Context** and **Capabilities**, with **Connections** (live data into [[ghl]], [[baselane]], [[doorloop]], [[google-sheets]]) the biggest gap and **Cadence** (autonomous scheduled runs) the next push. The Bike Method (phased trust) maps to the rule that all outbound routes through [[mostafa]]; the "keys vs instructions" lesson is a direct caution for scoping [[vince-ai]]'s Twilio send capability.

**Voice as a new surface**: a code-first [[elevenlabs]] + [[twilio]] voice agent (built and debugged through Claude Code) is now a realistic capability layer — most directly as a voice version of [[vince-ai]] that answers inbound lender calls. Full pattern in [[source-voice-agents-elevenlabs]].

## Build stack (June 2026 shift)
The build stack has moved to **Claude Code + the superpowers plugin**, REPLACING [[manus]] (dropped late May 2026 as too expensive and less token-efficient). The guiding build philosophy is the [[claude-code-workflow]] paired with the [[information-moat]] thesis — durable advantage comes from the quality of context fed to the model, not prompt-tuning.

**Skills-first strategy**: accumulate Claude Skills daily, keeping a max of ~3 in progress at once, and **never download external/third-party skills** (security + relevance — only build skills tailored to the business). Layer an AI agent on top later: *"skills are the recipe, AI agents are the chef."*

**Wholesale automation direction**: the wholesale pipeline now anchors on the [[no-fluff-model]] / [[agent-outreach]] approach feeding [[vince-ai]].

## Related pages
- [[ghl]]
- [[vince-ai]]
- [[content-ai]]
- [[wholesale]]
- [[pml-tl]]
- [[matt-beard]]
- [[elevenlabs]]
- [[source-voice-agents-elevenlabs]]
- [[claude-code-workflow]]
- [[information-moat]]
- [[manus]]
- [[no-fluff-model]]
