---
name: ghl
type: entity
tags: [crm, automation, ai, central-hub]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md]
updated: 2026-06-03
---

# GoHighLevel (GHL)

**Summary**: Central hub for ALL WIH business communications, pipelines, AI agents, and automations. Single source of truth across real estate and cleaning business.

**Sources**: CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md

**Last updated**: 2026-05-29

---

GHL is the nerve center of Joshua's business. Every AI agent ([[vince-ai]], [[content-ai]]) lives here. All outbound communications route through [[mostafa]] via GHL — this is non-negotiable per SOP.

The strategic vision is full AI automation of real estate operations with GHL as the hub across three verticals: wholesale, property management, and capital raising ([[pml-tl]]).

**LBK Cleaners feed:** [[bookingkoala]] connects to GHL via [[zapier]]. Every new booking, cancellation, or charge in BookingKoala triggers a Zap that creates or updates a contact/pipeline entry in GHL. This makes GHL the unified view across both the real estate and cleaning businesses.

[[twilio]] provides SMS/voice capabilities. [[claude-api]] is the AI backbone for agent conversations.

**Contacts migration & data source role:** the plan is to export all ~16,000 contacts to [[supabase]] for the [[wih-app]] "Us" build — at which point GHL becomes a *data source*, not the system of record. Access is via a GHL Private Integration token (all scopes) plus the Location ID. AI parses GHL tasks into [[notion]]. CRM data quality is currently poor — ~89% of contacts untagged and only 39 have emails — so dedup/cleanup happens during migration.

**SOP reaffirmed:** payment follow-ups route through [[doorloop]]; other comms go through GHL; all outbound routes via [[mostafa]].

## Related pages
- [[vince-ai]]
- [[twilio]]
- [[claude-api]]
- [[mostafa]]
- [[ai-automation-strategy]]
- [[bookingkoala]]
- [[zapier]]
- [[lbk-cleaners]]
- [[supabase]]
- [[wih-app]]
