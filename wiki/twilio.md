---
name: twilio
type: entity
tags: [sms, voice, ai-agents]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Twilio

**Summary**: SMS and voice infrastructure for AI agents, primarily powering Vince AI via GHL.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Provides SMS and voice capabilities to [[ghl]]-based AI agents. Primary use case is [[vince-ai]] for PML/TL qualification. Needs a dedicated number assigned for Vince to go live.

On the **voice** side, Twilio integration (or SIP trunking) is how an [[elevenlabs]] voice agent is connected to a phone number for inbound/outbound calls — the "phone" deployment surface for a voice version of Vince (source: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md). See [[source-voice-agents-elevenlabs]].

## Related pages
- [[ghl]]
- [[vince-ai]]
- [[claude-api]]
- [[elevenlabs]]
- [[source-voice-agents-elevenlabs]]
