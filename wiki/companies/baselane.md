---
name: baselane
type: entity
tags: [finance, property-management]
status: active
sources: [CLAUDE.md seed, transcript-2026-05-29-morning-meeting-josh-mostafa.md]
updated: 2026-06-03
---

# Baselane

**Summary**: Financial tracking platform for WIH properties.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-03

---

Used for financial tracking across the [[wih]] property portfolio. Banking is provided through **Thread Bank** (Rogersville, TN). Works alongside [[mercury]] for overall cash management and runs the [[profit-first]] sub-account structure. Money-routing on top of Baselane is handled by [[sequence]].

> **Migration:** Baselane has no usable API, so AI can't control the money layer. Banking + routing are slated to move to [[mercury]] under [[baselane-to-mercury-migration]]; Baselane is to be kept afterward only as a read-only bookkeeping layer.

WWH operates a main account (ending 4927) plus dedicated per-property, taxes, and rehab-funds accounts. Statements are summarized in [[source-baselane-statements]]; a custom [[source-baselane-statement-analyzer-skill]] automates parsing them. **Section 8 government payments land directly in Baselane.**

## Statement-pull automation
A scheduled automation now pulls Baselane statements across all accounts. Because Baselane has no public API, it uses **Playwright browser automation running on [[railway]]** (credentials in env vars). Output feeds Google Drive + Google Sheets + `raw/` for wiki ingest. Goal: a daily balance view plus recurring/subscription expense pattern recognition. This is groundwork for the [[baselane-to-mercury-migration]].

## Related pages
- [[wih]]
- [[mercury]]
- [[sequence]]
- [[baselane-to-mercury-migration]]
- [[profit-first]]
- [[webber-wealth-holdings]]
- [[source-baselane-statements]]
- [[source-baselane-statement-analyzer-skill]]
- [[railway]]
