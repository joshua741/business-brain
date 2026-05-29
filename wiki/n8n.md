---
name: n8n
type: entity
tags: [automation, workflow]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# n8n

**Summary**: Workflow automation platform. Handles the daily Notion export pull to raw/ for wiki ingest.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

Used for workflow automation across the stack. Key role in the second brain system: runs a daily scheduled job at 3 AM to check Notion master prompts for changes and export to `raw/` when updated. Works alongside [[zapier]] for integrations.

## Related pages
- [[zapier]]
- [[ghl]]
