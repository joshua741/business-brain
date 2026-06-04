---
name: ghl
type: entity
tags: [crm, automation, ai, central-hub]
status: active
sources: [CLAUDE.md seed, BookingKoala_Help_Center_Full_Reference.md]
updated: 2026-06-04
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

**Contacts migration & data source role:** migrating all ~16,375 contacts to [[supabase]] for the [[wih-app]] "Us" build — GHL becomes a *data source*, not the system of record. As of 2026-06-04: 14,206 contacts synced (~87%). Access is via a GHL Private Integration token (all scopes) plus the Location ID. AI parses GHL tasks into [[notion]]. CRM data quality is currently poor — ~89% of contacts untagged and only 39 have emails.

## Pipeline snapshot (2026-06-04, source: [[source-ghl-snapshot-2026-06-04]])
500 opportunities across 12 pipelines (pull capped at 500). Top pipelines:
- **Pipeline 6 (RTO Prospects):** 386 opps — 167 Reset, 62 FB Group Welcome, 56 New Inbound Call Prospect
- **Pipeline 2 (Follow Up Manager):** 40 opps — 20 New Lead, 15 Disqualified
- **Pipeline 1 (Seller Leads):** 26 opps — 6 Qualified, 3 Follow Up Engaged, 3 Offer Made
- **Transaction Board (Pipeline 3):** 4 closed deals, $76,000 total value logged
- **PML Lenders:** 2 in Info Collected

Hot lead: **Ashley Paz** moved to "Send Deposit Agreement" (RTO Prospects) on Jun 3.

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
