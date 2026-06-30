---
name: source-transcript-2026-06-02-meeting
type: source
tags: [transcript, meeting, supabase, wih-app, doorloop, sequence]
status: complete
sources: [transcript-2026-06-02-meeting.md]
updated: 2026-06-03
---
# Tactical Tuesday Build Session (2026-06-02, 12:46pm)

**Summary**: Afternoon live-coding session (continuation of the morning meeting) migrating 16,000 GHL contacts into Supabase, building a DoorLoop late-tenant SMS skill, adopting Sequence's bank-balance MCP, and consolidating the whole operation into one custom app named "Us."

**Sources**: transcript-2026-06-02-meeting.md

**Last updated**: 2026-06-03

---

Joshua + [[mostafa]]; live call to tenant Tracy. Screen-shared live coding in Claude Code.

## Decisions
- Migrate all 16,000 [[ghl]] contacts into [[supabase]] as a deduplicated lookup directory.
- Build a Contacts section in the app (advanced filter + export, keep the richest contact, no dupes).
- Data in [[supabase]] reflected in the [[railway]]-hosted app (Supabase = storage, Railway = hosting); connection established (Connect → session pooler + DB password).
- Built the [[doorloop]] SMS late-tenant skill — live for 14/15 leases, then paused for app integration.
- Adopt [[sequence]]'s new MCP with Claude (read bank balances; can't create pods / add accounts yet).
- Build utility-bill automation (dedicated email inbox → Claude updates expense tracking; Sequence auto-pays → Claude verifies cleared).
- Consolidate everything into one custom app named **"Us."**

## Action items
- Follow up Veronica + Ronald (today).
- Follow up Tracy tomorrow (bank / check cashing).
- Tracy to contact Wells Fargo with trust docs before Friday, notarize + cash the check.
- Post [[4513-48th-st]] on FB Marketplace.
- Investigate Claude responding to FB Marketplace messages.
- Explore the [[sequence]] MCP.
- Build utility-bill tracking via email.

## Property updates
- **[[4513-48th-st]]**: post to FB Marketplace.
- **[[2802-s-channing-st]]**: tied to Ronald Davis / Amarillo.
- Tenant statuses (via [[doorloop]]):
  - **Tracy**: due $2,103.83, escrow shortage $1,172.98 (check ~$1,209), monthly drops ~$20 once cashed; needs Wells Fargo + trust docs + notarized check Friday; on good terms. Her disgruntled mother (3 months behind, gave Tracy's brother $1,000) is blocked.
  - **Veronica**: $600 due June 1, one day before grace; lease #1 needed a manual SMS-enable fix.
  - **Stephanie**: late fee applied prematurely (system error; due June 3 not 2; due date 31st → 1st).
  - **Angel Garcia**: flagged late but payment confirmed made.
  - **Ronald Davis**: late.

## People
- **[[mostafa]]**: hands-on building + tenant comms via DoorLoop.
- **[[mkenzy]]**: some tenant contact; Veronica partial payment went to her.
- **Tracy** (Wells Fargo customer); **Tracy's mother** (blocked).
- **Veronica, Ronald Davis, Stephanie, Angel Garcia** (tenants).

## Deals & money
- Tracy $2,103.83 / shortage $1,172.98 / ~$20/mo reduction.
- Veronica $600.
- DoorLoop replacement could save ~$500/mo / $2,000/yr.
- Goal: back-to-back $50k+ months.

## Projects & tooling
- **[[supabase]] + [[railway]] + "Us" app** ([[wih-app]] line): contacts migration live; advanced-filter Contacts section.
- **[[doorloop]] SMS skill**: live 14/15; message "Your payment will be late tomorrow and late payment fee will be applied. When can we expect your payment?"; triggers one day before grace; AI drafts / Joshua approves via DoorLoop mobile push; new tenants auto-covered if SMS checkboxes ticked (can't set via API).
- **[[sequence]] MCP**: reads balances only.
- **Subscription tracking skill**: gaps — seller-financing amounts blank, need portal-login automation + credentials.
- Data quality: 89% of 16,000 contacts untagged, only 39 have emails.
- SOP: payment follow-ups via [[doorloop]], other comms via [[ghl]].

## Personal observations
- "You're creating a workflow, but you're not creating AI... I want it to talk to them and ask why are you late."
- Teach AI HOW to think, not WHAT to say.
- MVP / iterate mindset.
- End-state: run the whole business inside Claude, then hand it to an AI bot — name the app "Us."

## New context / flags
- [[sequence]] bank-balance MCP.
- App named **"Us"** — in-house replacement consolidating [[doorloop]] / [[ghl]] / contacts (the [[wih-app]] vision).
- [[doorloop]] billed per-lease (scales with portfolio).
- CRM data-quality reality (89% untagged, 39 emails).
- An IT-tech role added.

## Notable quotes
- "Everything's in the house. Everything but Claude. It's us."
- "We're trying to do a complete task with AI. That's different."

## Related pages
- [[supabase]]
- [[railway]]
- [[wih-app]]
- [[doorloop]]
- [[ghl]]
- [[sequence]]
- [[2802-s-channing-st]]
- [[4513-48th-st]]
- [[mostafa]]
- [[mkenzy]]
