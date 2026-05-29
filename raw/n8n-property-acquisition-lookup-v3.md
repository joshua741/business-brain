# n8n Property Acquisition Lookup v3 (Corrected API)

**Summary**: Updated n8n workflow using the real Lubbock CAD JSON API endpoint (vs HTML scraping in v2) — searches 13 portfolio properties, extracts deed dates, buyer/seller info, and instrument numbers, writes to Google Sheets.

**Sources**: Google Drive — n8n_Property_Acquisition_Lookup_v3.json (1uJsw4E6_p_lnyel6RDuU2RMdsl7kn00e)

**Last updated**: 2026-05-29

---

## Workflow Overview

**Name:** Property Acquisition Date Lookup v3 (Corrected API)
**Trigger:** Manual
**Key improvement over v2:** Uses real Lubbock CAD JSON API (not HTML scraping) — more reliable and structured

---

## Node Flow

1. **Run Manually** → trigger
2. **Define All Properties** (Code node) → same 13 properties as v2
3. **SplitInBatches** (batch=1, does not reset)
4. **Is Lubbock?** (IF node, case sensitive)
5a. **Search Lubbock CAD API** (HTTP GET — JSON API endpoint with URL parameters: f=[search_term], ty=2026, pvty=2026, pt=RP;PP;MH;NR, take=20, skip=0)
5b. **Potter-Randall Placeholder** (Code node — outputs "Manual lookup needed" for all fields)
6a. **Parse Search Results** (Code node) → extracts from API response: PropertyQuickRefID, PartyQuickRefID, OwnerName, SitusAddress, MarketValue
7. **Fetch Property Detail** (HTTP GET lubbokcad.org/Property-Detail/[PropertyQuickRefID]/PartyQuickRefID/[PartyQuickRefID])
8. **Extract Deed Info** (Code node) → searches "SALES HISTORY" section for: deed_date, seller, buyer, instrument_number. Checks buyer against Joshua entities: WEBBER, W&M, WWH, TENGIC
9. **Write Lubbock to Sheets** → appends to Google Sheets
10. **Wait After Lubbock** (2 seconds) → rate limiting
11. Loop back to step 3

Potter-Randall branch:
5b → **Write Potter-Randall to Sheets** → **Wait After Potter-Randall** (2 seconds) → loop

---

## Output Fields (Lubbock)

- address, entity, cad_source: "lubbock"
- property_id, party_id, owner_name
- deed_date, seller, buyer, instrument_number
- market_value, lookup_timestamp
- buyer_is_joshua_entity: YES/NO (checks for WEBBER, W&M, WWH, TENGIC)

---

## Joshua Entity Identifiers

The workflow checks if buyer or seller contains any of:
- WEBBER
- W&M
- WWH
- TENGIC

---

## Notes

- v3 is the preferred version — uses actual JSON API
- Potter-Randall (prad.org) still requires manual lookup as of v3 build
- Google Sheets target: `1WrXKYCVea_pDET_QDA2T7c-EewsHHKQevRzpEjwHF6Y` / sheet "Property Acquisition Dates"
- Must connect Google Sheets credential on both Write nodes before running

---

## Related pages
- [[n8n-property-acquisition-lookup-v2]]
- [[n8n]]
- [[wih]]
- [[google-sheets]]
- [[property-management]]
