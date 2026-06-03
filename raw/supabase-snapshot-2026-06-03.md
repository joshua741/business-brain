---
name: source-supabase-snapshot-2026-06-03
type: source
tags: [supabase, wih-app, database, crm, snapshot]
sources: [supabase-snapshot-2026-06-03.md]
updated: 2026-06-03
---
# Supabase (wih-app DB) Snapshot -- 2026-06-03

**Summary**: Read-only snapshot of the [[wih-app]] Supabase Postgres -- 14 public tables.

**Sources**: supabase-snapshot-2026-06-03.md (Postgres, read-only)

**Last updated**: 2026-06-03

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
| messages | 8 |
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
| 00XX7013-5647-4989-9e68-a22db678f932 | +18XXXXX8495 |  |  |  |  |
| 55acc3fd-4377-4018-9543-a4b50bf23ef0 | +18XXXXX3637 | Aaron Burch | amb7767@gmail.com | 1106 W 24th St | Odessa |

### conversations  (1 rows)
| id | contact_id | twilio_number | last_message_at | ai_summary | status |
| --- | --- | --- | --- | --- | --- |
| 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | +18XXXXX0719 | 2026-06-03 07:28:26.295865+00:00 |  | active |

### deals  (0 rows)
_empty_

### directory_contacts  (14206 rows)
| id | ghl_contact_id | first_name | last_name | full_name | phone |
| --- | --- | --- | --- | --- | --- |
| fd7a50b6-d626-4ee1-99f4-8e47793b3e9a | VUtmLcIIyN7LWBstnrQ9 | Susan | Kalisiak | Susan Kalisiak | +18XXXXX2349 |
| d2448a9c-67b0-465c-97bc-7fcf5a0a811b | oRHonlsfzisvqyuzSrfx | Chuck | Hardy | Chuck Hardy | +18XXXXX7756 |
| d893c50c-260c-4124-967a-444f66f13f5c | G33G6xLpfHQrYp7LP9mY | Bryan | Reese | Bryan Reese |  |
| c6a505d2-d7ed-458b-b84c-a1bed01707ba | FtXwYObBKdwIlYMQEn9p | Mary | O'bar | Mary O'bar | +15XXXXX9564 |
| c6a4604a-13dd-469c-932e-54cd3735e607 | icVyFiuWS0TrI10GiGQT | Sara | Azali | Sara Azali | +13XXXXX7236 |

### messages  (8 rows)
| id | conversation_id | contact_id | twilio_sid | direction | body |
| --- | --- | --- | --- | --- | --- |
| 161fe6ee-2792-4eeb-9eb4-73017644d9c3 | 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | SMf7376999de21befaeed84f80XXX3134c | outbound | Oh got it! So you're not an agent, you'r |
| ccdcbf48-34d2-40a9-8f31-9057fc6c6134 | 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | SM31c968f232faede26871dff8cb25ace0 | inbound | I’m thinking about selling my house |
| 81XX6122-d045-46ea-9ab3-743385564d4c | 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | SMab553ed71778eef9e2a94XX3133e89c3 | outbound | Yep, you got it! I'm Vince — I work with |
| 86f8202b-219d-429c-afdc-184499aa13eb | 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | SM28f9f7dc1a32238a59c26XXXXX8540a1 | inbound | OK, is this the right number for the buy |
| 1c78973b-9bbe-4bb0-a770-dc02840a9037 | 8caf2042-d28c-489e-ab4e-eaa07ef09e22 | 00XX7013-5647-4989-9e68-a22db678f932 | SM9d79477be9b313acb667fbf402ad5fb4 | outbound | Ha sorry for the confusion! I'm a buyer, |

### note_folders  (0 rows)
_empty_

## Related pages
- [[wih-app]]
- [[supabase]]
- [[ghl]]

