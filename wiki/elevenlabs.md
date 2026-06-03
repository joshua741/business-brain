---
name: elevenlabs
type: entity
tags: [ai, voice, tts, automation, tool]
status: active
sources: [clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md]
updated: 2026-06-03
---

# ElevenLabs

**Summary**: AI voice / text-to-speech platform and voice-agent builder. Candidate voice layer for [[vince-ai]] — pairs with [[twilio]] for phone and [[claude-api|Claude Code]] for code-first configuration.

**Sources**: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md

**Last updated**: 2026-06-03

---

ElevenLabs provides realistic TTS voices (library voices plus custom voice clones) and a full **conversational voice-agent** product. An agent is defined by four parts — Persona, Voice, Knowledge, Tools — and can be deployed three ways: dashboard test, embedded website widget (two lines of HTML), or a phone number via [[twilio]] integration / SIP trunking (source: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md). See [[source-voice-agents-elevenlabs]] for the full build walkthrough.

Agents and tools can be configured entirely through [[claude-api|Claude Code]] ("code beats clicks") — configs versioned in git, pushed with `elevenlabs agents push`. Cost runs ~$0.08–$0.12/min. Security note: widgets are open to any domain by default — lock the hostname allowlist.

**Relevance to WIH**: the most likely path to a **voice version of [[vince-ai]]** — reusing Vince's persona, qualification knowledge, and booking tools to answer inbound lender calls or a web widget.

## Related pages
- [[source-voice-agents-elevenlabs]]
- [[vince-ai]]
- [[twilio]]
- [[ai-automation-strategy]]
