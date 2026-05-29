# n8n Property Acquisition Lookup v2

**Summary**: n8n workflow that searches Lubbock CAD and Potter-Randall CAD for all 13 portfolio properties, extracts deed dates and ownership info via HTML scraping, and writes results to Google Sheets.

**Sources**: Google Drive — n8n_Property_Acquisition_Lookup_v2.json (1yw3XsweOeX3Y3yfMNGaxZ6H53bL_hMKc)

**Last updated**: 2026-05-29

---

## Workflow Overview

**Name:** Property Acquisition Date Lookup (Lubbock & Potter-Randall CAD)
**Trigger:** Manual
**Output:** Google Sheets — Property Acquisition Dates sheet

---

## Properties Covered (13 total)

| Address | City | Entity | Deal Type | CAD |
|---|---|---|---|---|
| 4019 37th St | Lubbock TX | W&M Series LLC | DSCR/Rent to Own | Lubbock |
| 7005 Winston Ave | Lubbock TX | Webber Wealth Holdings LLC | Subto/Rent to Own | Lubbock |
| 3904 Ave R | Lubbock TX | Trust/WWH | Subto/Rent to Own | Lubbock |
| 3423 E Baylor | Lubbock TX | W&M Series LLC | HML-Bridge/Rent to Own | Lubbock |
| 1312 65th Dr | Lubbock TX | Trust | Seller Finance | Lubbock |
| 4618 45th St | Lubbock TX | Webber Wealth Holdings LLC | Subto/Rent to Own | Lubbock |
| 2102 68th St | Lubbock TX | W&M Series LLC | HML-Bridge/Rent to Own | Lubbock |
| 1926 27th St | Lubbock TX | W&M Series LLC | HML-Bridge/Rent to Own | Lubbock |
| 4205 E 61st St | Lubbock TX | W&M Series LLC | Coming Soon | Lubbock |
| 4302 E 61st St | Lubbock TX | W&M Series LLC | Coming Soon | Lubbock |
| 4626 S Lipscomb | Amarillo TX | Webber Wealth Holdings LLC | Subto/Seller Finance | Potter-Randall |
| 4438 Parker St | Amarillo TX | Webber Wealth Holdings LLC | Subto/Seller Finance | Potter-Randall |
| 2802 S Channing | Amarillo TX | Webber Wealth Holdings LLC | Subto/Seller Finance | Potter-Randall |

---

## Node Flow

1. **Run Manually** → trigger
2. **Define All Properties** (Code node) → outputs array of 13 property objects
3. **Process One at a Time** (SplitInBatches, batch=1)
4. **Is Lubbock?** (IF node) → routes Lubbock vs Potter-Randall
5a. **Search Lubbock CAD** (HTTP GET to lubbokcad.org) → HTML text response
5b. **Search Potter-Randall CAD** (HTTP GET to prad.org) → HTML text response
6. **Parse CAD Results** (Code node) → extracts PropertyQuickRefID, owner name, market value
7. **Fetch Property Detail Page** (HTTP GET to lubbokcad.org/Property-Detail/)
8. **Extract Ownership Details** (Code node) → extracts deed date, sale price, deed type
9. **Write to Google Sheets** → appends to "Property Acquisition Dates" sheet (ID: 1WrXKYCVea_pDET_QDA2T7c-EewsHHKQevRzpEjwHF6Y)
10. Loop back to step 3 for next property

---

## Output Fields

- address, city, entity, deal_type, cad_source
- property_id_cad, owner_on_record
- deed_date, sale_price, deed_type
- market_value, detail_url
- lookup_timestamp
- needs_manual_review (YES if deed date not found)
- pre_2025 (YES/NO/UNKNOWN based on deed date)
- mkenzie_eligible (CHECK — only post-2025 acquisitions)

---

## Notes

- v2 uses HTML scraping (lubbokcad.org search URL)
- v3 uses the real JSON API endpoint (more reliable)
- Potter-Randall properties require manual lookup via prad.org
- Google Sheets target: `1WrXKYCVea_pDET_QDA2T7c-EewsHHKQevRzpEjwHF6Y` / sheet "Property Acquisition Dates"

---

## Related pages
- [[n8n]]
- [[wih]]
- [[1312-65th-dr]]
- [[property-management]]
- [[google-sheets]]
