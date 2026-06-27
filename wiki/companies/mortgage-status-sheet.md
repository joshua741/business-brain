---
name: mortgage-status-sheet
type: entity
tags: [tool, google-sheets, finance, automation]
sources: [transcript-2026-06-23-morning-meeting-josh-mostafa.md, transcript-2026-06-24-morning-meeting-josh-mostafa.md, transcript-2026-06-25-morning-meeting-josh-mostafa.md]
updated: 2026-06-26
---

# Mortgage Status Sheet

**Summary**: The Google Sheet (within the Property Payment Checklist) tracking each property's mortgage status, balances, and payment math. Target of the Mercury balance-sync and the second-position/servicing build-out.

**Sources**: transcripts 2026-06-23 / -24 / -25

**Last updated**: 2026-06-26

---

- **Mercury balance sync**: an automation reads [[mercury]] bank + reserve balances Mon/Wed/Fri, writes them here, and Telegram-alerts when bank+reserve < the property's payment.
- **Second-position + servicing build-out (Jun 24)**: added columns for **total payment = first position + second position + servicing**, plus **second-position servicing (yes/no)** and **servicing amount**. The alert threshold compares balances against this **total**, closing a gap where only first position was tracked.
- Refinances change payments (e.g., [[3423-e-baylor-st]] dropped ~$500) — the sheet and [[sequence]] must be updated together when a property refis.
- Planned **array** across mortgage/loan/utilities tabs (column-A address mirrors) and a plain-language **status bar**.

## Related pages
- [[sequence]]
- [[mercury]]
- [[selling-notes]]
- [[mostafa]]
