---
name: watch-video-capability
type: entity
tags: [tool, ai, video, claude-code, ingestion]
status: active
sources: [memo-2026-06-02T14-17-12-session.md, memo-2026-06-02T15-40-19-session.md, memo-2026-06-02T17-12-07-session.md, memo-2026-06-02T17-12-52-session.md, memo-2026-06-02T18-00-46-session.md, memo-2026-06-02T18-13-39-session.md]
updated: 2026-06-03
---

# /watch Video-Analysis Capability

**Summary**: Claude Code video-analysis plugin (`watch@claude-video` v0.1.3, from `bradautomates/claude-video`) that downloads, transcribes, and analyzes a video (URL or local file) and answers questions about it. Set up on Joshua's Windows machine over the 2026-06-02 sessions; gives the [[business-brain]] a path to ingest recorded meetings, training, and competitor content. Complements the `video-report` skill (video → structured report → wiki).

**Sources**: session-capture memos 2026-06-02

**Last updated**: 2026-06-03

---

A tooling capability, not a business entity — captured here because it adds a real ingestion surface to the [[business-brain]] tech stack: video → transcript → wiki.

**Install state (as of 2026-06-03):** installed and working. Deps confirmed on PATH — Python 3.12.10, ffmpeg/ffprobe 8.1.1, yt-dlp 2026.03.17. Optional Groq `whisper-large-v3` key configured at `~/.config/watch/.env` (ACL locked to the `joshu` user) for videos lacking native captions.

**Windows gotchas (durable):**
- `/plugin marketplace add` failed with an EBUSY rename lock — fix was to clone the repo into `~/.claude/plugins/marketplaces/claude-video` and hand-register it in `known_marketplaces.json` + `installed_plugins.json`.
- **Open blocker:** stable `yt-dlp 2026.03.17` throws HTTP 403 on YouTube (SABR/EJS challenge). Fix recipe (nightly yt-dlp + EJS/Deno + `--cookies-from-browser chrome`) is Unix-style (WSL/git-bash), not yet ported to native PowerShell.

Full troubleshooting history lives in the `watch-plugin-setup` memory note.

## Related pages
- [[ai-automation-strategy]]
- [[ai-operating-system]]
