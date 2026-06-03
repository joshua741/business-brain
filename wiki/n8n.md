---
name: n8n
type: entity
tags: [automation, workflow]
status: active
sources: [CLAUDE.md seed, n8n-property-acquisition-lookup-v2.md, n8n-property-acquisition-lookup-v3.md]
updated: 2026-05-29
---

# n8n

**Summary**: Workflow automation platform. Handles the daily Notion export pull to raw/ for wiki ingest, and a property-acquisition-date lookup workflow against county CAD records.

**Sources**: CLAUDE.md seed; n8n-property-acquisition-lookup-v2.md; n8n-property-acquisition-lookup-v3.md

**Last updated**: 2026-05-29

---

Used for workflow automation across the stack. Key role in the second brain system: runs a daily scheduled job at 3 AM to check Notion master prompts for changes and export to `raw/` when updated. Works alongside [[zapier]] for integrations.

## Property Acquisition Date Lookup
A manual-trigger workflow that looks up deed/ownership data for all 13 portfolio properties across **Lubbock CAD** and **Potter-Randall CAD**, then writes to [[google-sheets]] (sheet "Property Acquisition Dates").
- **v2** scrapes the Lubbock CAD HTML search; **v3** uses the real Lubbock CAD JSON API (preferred, more reliable). Potter-Randall (prad.org) still requires manual lookup (source: n8n-property-acquisition-lookup-v2.md, n8n-property-acquisition-lookup-v3.md).
- Flags `buyer_is_joshua_entity` by matching WEBBER / W&M / WWH / TENGIC, and `mkenzie_eligible` for post-2025 acquisitions (source: n8n-property-acquisition-lookup-v2.md, n8n-property-acquisition-lookup-v3.md). See [[source-n8n-acquisition-lookup]].

> **Portfolio note (lint):** The workflow's property list includes properties not in the CLAUDE.md seed — **7005 Winston Ave, 4205 E 61st St, 4302 E 61st St, 4438 Parker St** — and locates **4626 S Lipscomb, 4438 Parker, and 2802 S Channing in Amarillo TX** (Potter-Randall CAD), not Lubbock (source: n8n-property-acquisition-lookup-v2.md).

## Related pages
- [[zapier]]
- [[ghl]]
- [[google-sheets]]
- [[mkenzy]]
- [[source-n8n-acquisition-lookup]]
