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

The Business Brain is the `wiki/` knowledge base in `C:\Users\joshu\Documents\Business_Brain`. Joshua sources and curates; Claude writes, links, and maintains every page. Raw documents land in `raw/` and are ingested into linked `wiki/` pages; an automated daily agent (`daily-wiki-maintenance.ps1`) pulls Google Drive briefings, ingests by reconciliation, lints, and commits. Working sessions are auto-captured as memos and reconciled in [[source-session-captures]].

It is the implementation of the [[ai-operating-system]] pattern ([[nate-herk]]) — strong on **Context** and **Capabilities**, with live **Connections** ([[ghl]], [[baselane]], [[doorloop]], [[google-sheets]]) the main gap. New ingestion surfaces include the `/watch` [[watch-video-capability]] (video → transcript → wiki). The brain underpins the broader [[ai-automation-strategy]].

## Related pages
- [[ai-operating-system]]
- [[ai-automation-strategy]]
- [[nate-herk]]
- [[watch-video-capability]]
