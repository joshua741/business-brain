---
name: r2oc
type: entity
tags: [marketing-brand, rent-to-own, content, social-media]
status: active
sources: [CLAUDE.md seed]
updated: 2026-05-28
---

# Rent 2 Own Cribs (R2OC)

**Summary**: Marketing brand for rent-to-own properties and content. Social media automated via Content AI.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

External-facing brand for [[wih]]'s rent-to-own properties and educational content. Content pipeline is being automated via [[content-ai]] using Google Sheets + daily automation.

Website: https://rent2owncribs.com — property listings live here. Application flow: prequalify → apply at rent2owncribs.com ($49.90 fee).

## Facebook Marketplace listing title formula

`🏡 Rent2Own [BEDS]/[BATHS] [DOWN_ROUNDED]k⬇️`

- Beds/baths: actual unit count (e.g. 4/2)
- Down: option fee rounded DOWN to the nearest thousand (e.g. $9,500 → 9k, $12,000 → 12k)
- Example: `🏡 Rent2Own 4/2 9k⬇️`
- Posted on Joshua's personal Facebook page (not a business page)
- Images use R2OC-watermarked photos (via the Claude/Canva listing skill); to avoid Facebook duplicate-listing blocks, vary the title, description, and images per post

## Outreach workflow

When a new RTO property is available:
1. Check if listing is live at rent2owncribs.com/property/[slug]
2. Text blast to current RTO tenant list (via wih-app / Twilio) — include front-of-house photo
3. Facebook Marketplace post (Joshua's personal page) — title formula above, R2OC listing link, unique images
4. Responses handled via RTO script system (see [[sales-scripts]])
5. Interested contacts enter wih-app as `rto_buyer` at "New Inquiry" stage in the `rent_to_own` pipeline

## Related pages
- [[wih]]
- [[content-ai]]
- [[rent-to-own]]
- [[google-sheets]]
