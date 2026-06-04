---
name: source-supabase-snapshot-2026-06-04
type: source
tags: [supabase, wih-app, database, crm, snapshot]
sources: [supabase-snapshot-2026-06-04.md]
updated: 2026-06-04
---
# Supabase (wih-app DB) Snapshot -- 2026-06-04

**Summary**: Read-only snapshot of the [[wih-app]] Supabase Postgres -- 14 public tables.

**Sources**: supabase-snapshot-2026-06-04.md (Postgres, read-only)

**Last updated**: 2026-06-04

---

## Tables (row counts)
| Table | Rows |
|---|---|
| agent_profiles | 0 |
| buyer_profiles | 0 |
| call_logs | 0 |
| contact_notes | 0 |
| contact_properties | 0 |
| contact_tags | 0 |
| contacts | 2 |
| conversations | 1 |
| deals | 0 |
| directory_contacts | 14206 |
| messages | 9 |
| note_folders | 0 |
| pipeline_stages | 14 |
| tags | 0 |

## Recent rows (CRM-relevant tables)

### buyer_profiles  (0 rows)
_empty_

### contact_notes  (0 rows)
_empty_

### contact_properties  (0 rows)
_empty_

### contact_tags  (0 rows)
_empty_

### contacts  (2 rows)
| id | phone | name | email | address | city |
| --- | --- | --- | --- | --- | --- |
| 795c2b0b-2b0b-4689-a9e8-444553a77924 | +18XXXXX8495 | Joshua Webber |  |  | LUBBOCK |
| 55acc3fd-4377-4018-9543-a4b50bf23ef0 | +18XXXXX3637 | Aaron Burch | amb7767@gmail.com | 1106 W 24th St | Odessa |

### conversations  (1 rows)
| id | contact_id | twilio_number | last_message_at | ai_summary | status |
| --- | --- | --- | --- | --- | --- |
| cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | +18XXXXX2532 | 2026-06-04 01:42:41.551624+00:00 |  | active |

### deals  (0 rows)
_empty_

### directory_contacts  (14206 rows)
| id | ghl_contact_id | first_name | last_name | full_name | phone |
| --- | --- | --- | --- | --- | --- |
| b130fbb2-0ff8-4e83-8d25-ab4bbaab4b72 | 8iarWwy7uWEI4ELwKGnw | Joshua | Webber | Joshua Webber | +18XXXXX8495 |
| d893c50c-260c-4124-967a-444f66f13f5c | G33G6xLpfHQrYp7LP9mY | Bryan | Reese | Bryan Reese |  |
| fd7a50b6-d626-4ee1-99f4-8e47793b3e9a | VUtmLcIIyN7LWBstnrQ9 | Susan | Kalisiak | Susan Kalisiak | +18XXXXX2349 |
| d2448a9c-67b0-465c-97bc-7fcf5a0a811b | oRHonlsfzisvqyuzSrfx | Chuck | Hardy | Chuck Hardy | +18XXXXX7756 |
| c6a505d2-d7ed-458b-b84c-a1bed01707ba | FtXwYObBKdwIlYMQEn9p | Mary | O'bar | Mary O'bar | +15XXXXX9564 |

### messages  (9 rows)
| id | conversation_id | contact_id | twilio_sid | direction | body |
| --- | --- | --- | --- | --- | --- |
| 87a005ee-97e3-498e-be73-f7708abe0bb7 | cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | SMa8d81d10226ba043fb0b98XX4936a0f2 | outbound | Of course, no worries! If anything chang |
| 2b0512be-2d68-4872-9cf6-aa87ffa14b3a | cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | SM45XX6076c490615cb18e1df3c5bd503d | inbound | We are ok, thanks for reaching out |
| 780b4740-3267-4c80-ba38-affbdb50f931 | cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | SM5ae93d746706b93XX9648b6272d68c43 | outbound | Haha so which is it — are they getting o |
| 1e846b02-baac-43d8-a321-1ebc4a904ac9 | cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | SM27d6084421fdb782f624eab177b64e33 | inbound | Ok |
| a16d1fc2-d35f-43f6-952a-24f83a419fca | cef19796-e68e-4724-b669-fc9386e448ef | 795c2b0b-2b0b-4689-a9e8-444553a77924 | SM38b371f16d023ca881166bb0adb11b28 | outbound | Got it. Are they moving or have they bee |

### note_folders  (0 rows)
_empty_

## Related pages
- [[wih-app]]
- [[supabase]]
- [[ghl]]

