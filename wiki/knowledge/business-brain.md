---
name: business-brain
type: concept
tags: [system, knowledge-base, ai, meta]
sources: [CLAUDE.md seed]
updated: 2026-06-03
---

# Business Brain

**Summary**: Joshua's persistent, compounding second brain — a Claude-maintained wiki that is the single source of truth for the business, finances, projects, and personal context. Notion master prompts and CLAUDE.md are compressed views derived from it.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

The Business Brain is the `wiki/` knowledge base inside the `joshua741/business-brain` GitHub repo, synced as a local Obsidian vault. Joshua sources and curates; Claude writes, links, and maintains every page. Raw documents land in `raw/` and are ingested into linked `wiki/` pages; an automated daily agent (`daily-wiki-maintenance.ps1`) pulls Google Drive briefings, ingests by reconciliation, lints, and commits. Working sessions are auto-captured as memos and reconciled in [[source-session-captures]].

It is the implementation of the [[ai-operating-system]] pattern ([[nate-herk]]) — strong on **Context** and **Capabilities**, with live **Connections** ([[ghl]], [[baselane]], [[doorloop]], [[google-sheets]]) the main gap. New ingestion surfaces include the `/watch` [[watch-video-capability]] (video → transcript → wiki). The brain underpins the broader [[ai-automation-strategy]].

**The information moat:** the wiki is Joshua's [[information-moat]]. Per Boris Cherny / the Bitter Lesson, the durable advantage is the quality of context fed to the model — not prompt-tuning. Accumulating high-quality, business-specific context compounds in a way competitors can't easily copy, and it directly powers the [[claude-code-workflow]] build stack.

**Proof-content engine:** the brain also doubles as a content engine — transcripts → "interesting moments" → [[content-ai]] backlog — so the act of running the business generates marketing material at zero extra capture cost.

Live ingest now spans **Notion, [[ghl]], Google Drive, Google Calendar, and [[doorloop]]** into the Obsidian graph.

## Related pages
- [[ai-operating-system]]
- [[ai-automation-strategy]]
- [[nate-herk]]
- [[watch-video-capability]]
- [[information-moat]]
- [[claude-code-workflow]]
- [[content-ai]]
