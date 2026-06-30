---
name: source-n8n-acquisition-lookup
type: source
tags: [n8n, automation, cad, property-data]
sources: [n8n-property-acquisition-lookup-v2.md, n8n-property-acquisition-lookup-v3.md]
updated: 2026-05-29
---

# Source: n8n Property Acquisition Lookup (v2 & v3)

**Summary**: An [[n8n]] workflow that pulls deed/ownership data for the 13 portfolio properties from Lubbock and Potter-Randall CAD and writes to Google Sheets. v3 uses the real JSON API; v2 scraped HTML.

**Sources**: n8n-property-acquisition-lookup-v2.md; n8n-property-acquisition-lookup-v3.md

**Last updated**: 2026-05-29

---

Manual-trigger workflow: define 13 properties → batch one-at-a-time → route Lubbock vs Potter-Randall → query CAD → parse property/owner/deed → fetch detail page → extract deed date/seller/buyer/instrument → write to Google Sheets ("Property Acquisition Dates," ID 1WrXKYCVea_pDET_QDA2T7c-EewsHHKQevRzpEjwHF6Y). v3 uses the Lubbock CAD JSON API and a 2-second rate-limit wait; Potter-Randall still manual. Flags `buyer_is_joshua_entity` (WEBBER/W&M/WWH/TENGIC) and `mkenzie_eligible` (post-2025) (source: n8n-property-acquisition-lookup-v2.md, n8n-property-acquisition-lookup-v3.md).

The 13-property list and the Lubbock-vs-Amarillo location finding are summarized on the [[n8n]] page. New entity identifier surfaced: **TENGIC**.

## Property list (entity / deal type / CAD)
4019 37th, 7005 Winston, 3904 Ave R, 3423 E Baylor, 1312 65th Dr, 4618 45th, 2102 68th, 1926 27th, 4205 E 61st, 4302 E 61st (Lubbock CAD); 4626 S Lipscomb, 4438 Parker St, 2802 S Channing (Potter-Randall / Amarillo).

## Related pages
- [[n8n]]
- [[wih]]
- [[google-sheets]]
- [[mkenzy]]
