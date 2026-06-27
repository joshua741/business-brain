---
name: source-voice-agents-elevenlabs
type: source
tags: [ai, voice, elevenlabs, twilio, claude-code, video, automation]
status: complete
sources: [clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md]
updated: 2026-06-03
---

# Source: Building Realistic Voice Agents Has Never Been Easier (Nate Herk)

**Summary**: [[nate-herk]] video (32:23, YouTube `-cdexJWN8YA`) showing how to build and ship a production voice agent end-to-end using natural-language [[claude-api|Claude Code]] prompts plus [[elevenlabs]] — built, debugged, and deployed a website sales agent that books calls on Cal.com in ~45 minutes. Directly applicable to giving [[vince-ai]] a voice/phone layer.

**Sources**: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md

**Last updated**: 2026-06-03

---

## What it covers
Nate Herk uses Claude Code (in VS Code) to build an [[elevenlabs]] voice agent by describing the goal in plain language. Claude reads the ElevenLabs + Cal.com docs, provisions the agent, wires two tools (`check_availability`, `book_call`), embeds the widget on a site, and iteratively debugs it — fixing a real timezone bug (the agent built the availability query window in UTC instead of Central) and prompt issues — until it successfully books a meeting and fires a confirmation email (source: clip-2026-06-03-building-realistic-voice-agents-has-never-been-easier.md).

## Core frameworks
- **Voice agent loop ("a loop, not magic")**: visitor speaks → agent listens via mic → LLM thinks, calls tools, decides reply → voice answers → loop repeats (source: clip).
- **Four pieces inside every agent**: **Persona** (system prompt — who it is, how it talks, what it refuses), **Voice** (ElevenLabs library voice or a custom clone), **Knowledge** (docs/URLs/DB that ground answers and stop hallucination), **Tools** (webhooks/functions called mid-conversation — DB queries, web search, bookings) (source: clip). Mirrors the Four Cs / [[ai-operating-system]] thinking.
- **"Code beats clicks"**: build/manage agents through versioned code (`elevenlabs agents push/pull`, `agent_configs/*.json` in git) rather than clicking in a dashboard — gives history, diffs, review, one-command deploy (source: clip).
- **Three deployment surfaces — "same agent, different door"**: **Test** (in dashboard), **Embed** (2 lines of HTML widget on any site), **Phone** ([[twilio]] integration or SIP trunking — inbound calls hit the same agent) (source: clip).

## Operating cautions (apply to any live voice agent)
- **Cost**: ~$0.08–$0.12/min, bundling voice + ASR + default LLM; bring-your-own-LLM costs extra (source: clip).
- **Security**: default is open — *any* domain with the agent ID can embed the widget. Lock the hostname allowlist in the agent's Security tab, or a stolen HTML snippet becomes a free voice line on your credits (source: clip).
- **Guardrails**: feed real docs (KB grounding), set a max per-call duration cap, rate-limit public pages, and accept that premium voice + smart LLM = more latency (source: clip).

## Why this matters for Joshua
[[vince-ai]] is currently an SMS-only PML/TL qualifier on [[twilio]] + [[claude-api]]. This source is the blueprint for adding a **voice/phone layer**: the same persona, knowledge, and tools that drive Vince's SMS qualification could power an ElevenLabs voice agent that picks up inbound calls (Twilio) or talks to lenders on a web widget — booking qualified intro calls automatically. The "code beats clicks" + iterative-debug workflow is the same Claude Code pattern Joshua already runs the [[business-brain]] on. See [[ai-automation-strategy]].

## Related pages
- [[elevenlabs]]
- [[vince-ai]]
- [[twilio]]
- [[nate-herk]]
- [[ai-automation-strategy]]
- [[ai-operating-system]]
