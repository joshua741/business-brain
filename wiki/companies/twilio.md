---
name: twilio
type: entity
tags: [sms, voice, ai-agents]
status: active
sources: [CLAUDE.md seed]
updated: 2026-06-04
---

# Twilio

**Summary**: SMS and voice infrastructure for AI agents, primarily powering Vince AI via GHL.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Provides SMS and voice capabilities to [[ghl]]-based AI agents. Primary use case is [[vince-ai]] for PML/TL qualification and acquisition outreach.

## Production numbers (confirmed 2026-06-04)
- **+18XXXXX2532** — Vince AI (live as of Jun 3, 2026; source: [[source-twilio-sms-log-2026-06-04]])
- **+18XXXXX0719** — general outreach / seller inquiry line (active Jun 3)

Vince went live on Jun 3 with acquisition outreach conversations — asking agents/contacts about off-market or stalled listings. The dedicated-number blocker is resolved.

On the **voice** side, Twilio integration (or SIP trunking) is how an [[elevenlabs]] voice agent is connected to a phone number for inbound/outbound calls — the "phone" deployment surface for a voice version of Vince (source: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md). See [[source-voice-agents-elevenlabs]].

## Related pages
- [[ghl]]
- [[vince-ai]]
- [[claude-api]]
- [[elevenlabs]]
- [[source-voice-agents-elevenlabs]]
