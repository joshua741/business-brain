---
name: sequence
type: entity
tags: [finance, automation, money-routing]
status: active
sources: [source-baselane-statements.md, memo-2026-06-03-mercury-migration-and-vision.md, transcript-2026-06-02-meeting.md, transcript-2026-06-12-morning-meeting-josh-mostafa.md]
updated: 2026-06-22
---

# Sequence (getsequence.io)

**Summary**: Money-routing / workflow automation layer ($90.92/mo) that sits on top of [[baselane]] and runs the rules that split incoming rent and Section 8, fund each property's mortgage account, and sweep the rest.

**Sources**: Baselane statements; session 2026-06-03

**Last updated**: 2026-06-03

---

Sequence is not banking — it's the rules engine layered over [[baselane]]. The recurring "Webber Wealth Ho Sequence" transactions in the [[source-baselane-statements]] are its automated transfers (e.g. funding and clearing the 1312 65th Dr seller-finance payment of $2,310.94/mo to Dillon Ford). Joshua values it because it's a visual, easily-editable workflow and cheap for the value — but it's a separate dependency and not AI-controllable.

> **Disambiguation (known trap):** [[secured-sequence]] — the RTO/seller-finance escrow-account provider used on [[4513-48th-st]] — is a **DIFFERENT vendor** from this getsequence.io money-routing layer. The name overlap is an easy trap; do not conflate them.

**Claude MCP integration:** Sequence now has a Claude MCP integration that can **READ bank balances via API**. It cannot yet create pods or add accounts. The key is shared between Joshua and [[mostafa]].

**Status:** slated for retirement under [[baselane-to-mercury-migration]] — [[mercury]]'s native percentage auto-transfer rules replace it, saving ~$1,091/yr.

## EIN application (Jun 2026)
Jacoby sent an EIN number sheet that needs to be edited — replace the name with **Joshua Weber** — and submitted to Sequence for application approval. A past-due invoice on [[2102-68th-st]] was also flagged in Sequence around June 12, 2026. (source: transcript-2026-06-12-morning-meeting-josh-mostafa.md)

## Related pages
- [[baselane]]
- [[mercury]]
- [[baselane-to-mercury-migration]]
- [[source-baselane-statements]]
- [[profit-first]]
- [[secured-sequence]]
- [[2102-68th-st]]
- [[source-transcript-2026-06-12]]
