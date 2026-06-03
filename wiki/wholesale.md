---
name: wholesale
type: concept
tags: [deal-sourcing, acquisition, ai-automation]
sources: [CLAUDE.md seed, davis-available-properties.md, 53-al-properties.md, hud-222408.md, wih-assignment-of-contract.md, wwh-assignment-of-contract.md, n8n-property-acquisition-lookup-v3.md]
updated: 2026-05-29
---

# Wholesale

**Summary**: Top-of-funnel deal sourcing strategy. Find distressed properties, assign contracts. Building toward AI-automated outreach.

**Sources**: CLAUDE.md seed; davis-available-properties.md; 53-al-properties.md; hud-222408.md; assignment-of-contract templates; n8n-property-acquisition-lookup-v3.md

**Last updated**: 2026-05-29

---

The deal sourcing engine for [[wih]]. Identify distressed property owners, get the property under contract, and either assign the contract to another buyer (pure wholesale) or take it down with [[creative-financing]]. Currently building toward an AI-automated outreach pipeline via [[ghl]] and [[n8n]] (property acquisition lookup workflow). Reference framework: [[matt-beard]]. Outreach uses the [[sales-scripts]] library.

## Deal pipelines
- **Davis — Available Properties:** ~28 Lubbock-area (plus out-of-market) leads tracked with ARV, asking price, true MAO, assignment amount, RTO cashflow, HML/DSCR monthly. Includes won deals [[1926-27th-st]] and [[2102-68th-st]] ("Our Offer Accepted") and active [[5427-35th-st]] (source: davis-available-properties.md). See [[davis-available-properties]].
- **53 Alabama Properties:** 53 off-market distressed deals in Bessemer/Fairfield/Birmingham AL, $12k–$35k listing, mostly "Not Sent," 3 pushed to Investor Lift (source: 53-al-properties.md). See [[source-53-al-properties]].

## Assignment mechanics
- WIH/WWH assignment-of-contract templates assign a property under contract to an end buyer for a fee (source: wih-assignment-of-contract.md, wwh-assignment-of-contract.md). See [[source-assignment-of-contract]].
- Example wholesale assignment fee: $5,000 to Webber on the 2022 Slaton TX deal (HUD file 222408) (source: hud-222408.md). See [[source-hud-222408]]. Recent: $35,000 KRC Services assignment on [[2102-68th-st]].

## Related pages
- [[ghl]]
- [[n8n]]
- [[ai-automation-strategy]]
- [[matt-beard]]
- [[creative-financing]]
- [[sales-scripts]]
- [[davis-available-properties]]
- [[wih]]
