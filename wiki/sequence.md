---
name: sequence
type: entity
tags: [finance, automation, money-routing]
status: active
sources: [source-baselane-statements.md, memo-2026-06-03-mercury-migration-and-vision.md, transcript-2026-06-02-meeting.md]
updated: 2026-06-03
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

**Retirement plan in motion (Jun 23–24, 2026):** Sequence currently auto-moves reserve→bank only when funds exist, on the 14th, capped at ~100 actions/mo (overages billed). The plan: have **AI make the reserve→bank top-up 2 days before each payment's due date** (reading [[mortgage-status-sheet]]), transferring only the shortfall, then **delete the Sequence rules**. AI is authorized for transfers (not payments) on its own. (source: [[source-transcript-2026-06-23-morning-meeting-josh-mostafa]])

## Related pages
- [[baselane]]
- [[mercury]]
- [[baselane-to-mercury-migration]]
- [[source-baselane-statements]]
- [[profit-first]]
- [[secured-sequence]]
