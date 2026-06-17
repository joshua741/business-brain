---
name: mostafa-business-brain
type: dashboard
owner: mostafa
scope: operations / execution layer (WIH + LBK Cleaners)
updated: 2026-06-17
sync: pushed daily ~8:47 AM to joshua741/business-brain (master)
---

# Mostafa's Business Brain — Operations Heartbeat

**Purpose**: Joshua's real-time view into the execution side of the business. This is the operations/coordination layer — property management, payments, tenant health, automations, and the AI/tooling buildout. Joshua's side (strategy, deals, capital, big-picture finance) lives in the wiki and his master prompts; this doc is the complementary operations feed.

**Honesty note**: Hard rollup numbers (total monthly rent roll, collection %, NOI) live in **DoorLoop**, **Baselane**, and the **Property Payment Checklist** Google Sheet — items marked _⟶ pull live_ should be sourced from there rather than trusted from memory. Everything else is current as of the date above.

---

## 1. Owner & Scope

- **Me**: Mostafa Elkhamisy — Operations Lead / transaction coordinator + appointment setter + "master of automations." Human-in-the-loop for all AI automations. **ALL outbound comms route through me** (non-negotiable SOP).
- **Working context**: Remote from Egypt, often overnight vs. Central time. On VS Code + Claude Code + superpowers. Added as a Business Brain collaborator June 4, 2026; operate from the shared wiki with an execute-and-escalate lens.
- **My lane**: execute operations, draft all outbound comms for review, run/maintain the automations and skills, keep the wiki's execution-layer current. Decisions on SOPs, strategy, financials, and deal terms escalate to Joshua's Claude.

## 2. Current Projects & Status

| Project | Status | Notes |
|---|---|---|
| **Property management ops** | 🟢 Active | ~12-property Lubbock portfolio; rent collection, leases, maintenance, vendor coordination |
| **4513 48th St rent-to-own push** | 🟠 Top priority | Closed ~June 5 ($250K seller-finance @8.5%). Marketing via Facebook Marketplace + manual group posts; text-blast for inbound, M'kenzy runs showings |
| **DoorLoop → Sheet payment sync** | 🟢 Live | MWF automated sync of payment statuses to the Property Payment Checklist sheet |
| **Subscriptions & Utilities tracking** | 🟢 Live | 36-subscription roster + utilities tracker with status automation and repayment tracking |
| **GHL ↔ Notion task sync** | 🟢 Live | Two-way sync of my GHL tasks into the Mostafa Task Tracker (Notion) |
| **Task prioritization / time-blocking** | 🟢 Live | "Organize my tasks" workflow ranks + time-blocks the Notion tracker |
| **Vince daily rebuild** | 🟢 Live | "Organize My Tasks" Notion button → n8n → Claude rebuilds Joshua's daily schedule |
| **Skills sharing with Joshua** | 🟢 Live | joshua741/skills-shared; my new skills auto-push daily 7:33 AM |
| **Notion + GitHub connectors to Claude Code** | 🟡 In progress | CLI/MCP only — keep Zapier solely for the DoorLoop integration (must not disconnect) |

## 3. Revenue & Financial Metrics

**Known concrete data points (early–mid June 2026):**
- **Alyssa lease termination (4302 E 61st)**: $3,007.37 collected via Square → **$2,948.73 net** to acct ending 5847. M'kenzy commission 14.2% = **$418.72** (paid via Sequence).
- **4513 48th St** acquisition: $250K @ 8.5%, taxes $215.83/mo, insurance ~$350/mo.
- **1312 65th Dr Unit E (Aaron)**: $832/mo → renewing **$850/mo** (12 mo from Aug 1, 2026).

**Rollups _⟶ pull live_:**
- Total monthly rent roll across portfolio — _⟶ DoorLoop rent roll_
- Collection rate / delinquency this month — _⟶ DoorLoop + Payment Checklist_
- Reserve balances by property — _⟶ Baselane_
- Subscription + utility monthly outflow — _⟶ Payment Checklist (subscriptions + utilities tabs)_

## 4. Active Clients / Tenants & Health

| Tenant / Property | Health | Detail |
|---|---|---|
| Veronica — 3423 E Baylor | 🟡 Watch | Payment "processing"; verify source in DoorLoop; 10-day grace, follow up post-June 10 |
| Tracy — 2802 S Channing | 🟡 Watch | 10-day grace confirmed; $210.38 late fee from June 10 if unpaid |
| Aaron — 1312 65th Dr Unit E | 🟢 Renewing | New lease drafted $850/mo; signature deadline July 20 via Crystal Sherwood |
| 4019 37th St (Evergreen note) | 🔴 Issue | NSF returned; Evergreen now wire-only ($15/wire) for 6+ payments; moving to auto-draft to Josh Fox |
| 4626 S Lipscomb | 🔴 Issue | (a) mortgage AutoPay may have stopped; (b) Xcel Energy past-due weekly since Feb — collection threat |
| 7500 Winston Ave (Freedom Mortgage) | 🟡 Watch | Repeated "account status change" emails — requires login to check (note: Winston trust + Josh personal Baselane accts are CLOSED) |

_Full tenant roster & current statuses ⟶ pull live from DoorLoop + Payment Checklist._

## 5. Team Status & Capacity

- **Mostafa (me)** — operations + automations; capacity stretched across payments, property issues, marketing push, and AI buildout. Overnight-CT working hours.
- **M'kenzy** — deals/showings; negotiated Alyssa termination; running 4513 showings; wants a 30–45 min AI + rent-to-own briefing (next week, 3pm, not Tuesday). Surfaced new lead.
- **Kenneth** — team member; route tasks where applicable.
- **Joshua** — systems architect / decision-maker only; not in execution.

## 6. Key Performance Indicators

_Targets/automation in place; live values ⟶ pull from sources._
- Rent collected vs. due (month) — _⟶ DoorLoop / Payment Checklist_
- # tenants in grace / delinquent — currently ≥2 in grace (Veronica, Tracy) + 2 property-level issues (4019, 4626)
- Days-to-respond on outbound — all outbound through me
- 4513 marketing: inbound inquiries → showings → applications — _⟶ GHL/text-blast_
- Automations healthy: DoorLoop sync (MWF), skills sync (7:33 AM), task syncs — 🟢

## 7. Strategic Initiatives (my execution role)

- **AI-run operations**: build/maintain skills so routine ops self-run; reduce manual touch. Feeds Joshua's "own the software / AI-run company" thesis.
- **Rent-to-own marketing engine**: systematize the 4513 playbook (marketplace + text-blast + AI responder + showing handoff) into a repeatable process.
- **Tooling migration**: task management GHL → Notion Team Space; connectors via CLI/MCP not Zapier (except DoorLoop).
- **wih-app feedback loop**: surface operational pain points that should become wih-app features.

## 8. Challenges & Learnings

- **Mortgage servicing fragility**: NSF + servicer changes (Evergreen wire-only, Freedom Mortgage status emails) — moving toward direct auto-draft to lenders to bypass servicing friction.
- **Utility delinquency blind spot**: 4626 Lipscomb Xcel past-due ran Feb→present unnoticed — the utilities tracker exists to catch exactly this; tighten the alerting.
- **Credentials hygiene**: skill files had hardcoded API tokens (caught by GitHub push protection) — now excluded + secret-scan guard on sync. Don't commit live tokens.
- **Systems > goals**: "You don't rise to the level of your goals, you fall to the level of your systems." — the operating ethos here.

## 9. Upcoming Milestones

- **July 20, 2026** — Aaron lease-renewal signature deadline (1312 Unit E) via Crystal Sherwood.
- **Aug 1, 2026** — Aaron new lease term begins at $850/mo.
- **Next week** — M'kenzy AI/rent-to-own briefing (3pm, not Tue); Shelby McDonald confirmed start for 4302 E 61st rehab.
- **Ongoing** — 4513 48th St rent-to-own buyer acquisition; new 5-property lead from the E 61st investors (M'kenzy pursuing).

## 10. How This Doc Is Maintained

- **Source of record**: the Business Brain wiki (`wiki/`) + morning-meeting transcripts (`raw/`) + my operational memory.
- **Update cadence**: refreshed daily ~8:47 AM (CronCreate prompt) and committed/pushed; the durable 2-hourly "Business Brain Sync" task guarantees it reaches GitHub.
- **Commitment**: keep this current as the business changes — new payments, tenant status changes, project moves, milestones.
