---
name: mostafa-business-brain
type: dashboard
owner: mostafa
scope: operations / execution layer (WIH + LBK Cleaners)
updated: 2026-06-26
sync: pushed daily ~8:47 AM to joshua741/business-brain (master)
freshness: ingested morning-meeting transcripts through 2026-06-26 (Jun 18/23/24/25/26)
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
| **Property management ops** | 🟢 Active | ~14-property Lubbock portfolio; rent collection, leases, maintenance, vendor coordination |
| **Baselane → Mercury migration** | 🟢 Done (Jun 23–24) | All property banking moved to Mercury; per-property virtual cards; Mercury API connected to Claude; auto-pay set on all mortgages |
| **Disposition push: 4513 48th St + 4302 E 61st** | 🟠 Top priority | 4513 **closed/funded ~Jun 22**; 4302 vacant + remarketed RTO ($1,450/mo, $145k, $35,922.50 down) — app sent to Glenda. Utilities turned on both. Text-blast + Facebook; M'kenzy runs showings |
| **Jacoby Maydwell 8-unit wholesale** | 🟡 In progress | Wholesale his townhomes to a cash/1031 buyer ($1.5–1.55M) via broker Rex Andrews; WIH spread $40k–$128k. On pause pending portfolio data |
| **Mortgage-status-sheet automations** | 🟢 / 🟡 | Mercury balance-sync (MWF + Telegram alert) live; adding 2nd-position + servicing total columns; AI reserve→bank transfers to replace Sequence rules |
| **DoorLoop → Sheet payment sync** | 🟢 Live | MWF automated sync of payment statuses to the Property Payment Checklist sheet |
| **Docs-mailbox AI automation** | 🟡 Building (this weekend) | AI to read docs@ mailbox for mortgage/utility statements + receipts (feeds utilities + reimbursement automations) |
| **Subscriptions & Utilities tracking** | 🟢 Live | 36-subscription roster + utilities tracker with status automation and repayment tracking |
| **GHL ↔ Notion task sync** | 🟢 Live | Two-way sync of my GHL tasks into the Mostafa Task Tracker (Notion) |
| **Task prioritization / time-blocking** | 🟢 Live | "Organize my tasks" workflow ranks + time-blocks the Notion tracker |
| **Vince daily rebuild** | 🟢 Live | "Organize My Tasks" Notion button → n8n → Claude rebuilds Joshua's daily schedule |
| **Skills sharing with Joshua** | 🟢 Live | joshua741/skills-shared; my new skills auto-push daily 7:33 AM |
| **Notion + GitHub connectors to Claude Code** | 🟡 In progress | CLI/MCP only — keep Zapier solely for the DoorLoop integration (must not disconnect) |

## 3. Revenue & Financial Metrics

**Known concrete data points (June 2026):**
- **4513 48th St** closed/funded ~Jun 22 ($250K @ 8.5%). Closing reconciliation: HUD cash-to-seller $71,334.27; Jacoby's cut $25,309.97; $17,250 back to lender Curtis (First Act, $15k + 15%); ~$28,774.30 net back to WIH.
- **4019 37th St (buyer Joseph DeLaO)**: payment rising **$1,674.08 → $1,826.87/mo (+$152.79)** once homeowner insurance escrows (P&I $1,203.35 + taxes $281.15 + ins $342.37); effective Aug 1. 1st position $1,367.07 + 2nd position $176.67 = $1,543.74.
- **4302 E 61st remarketing**: RTO $1,450/mo, purchase $145,000, seller-finance down $35,922.50.
- **Jacoby 8-unit portfolio**: owes ~$1.308M, appraised ~$1.736M, cash-flow negative ~$35k/yr; wholesale target $1.5–1.55M.
- **1312 65th Dr**: electric bill spiked ~$1,107 (≈2× May); Unit E (Aaron) renewing $850/mo Aug 1.
- **Alyssa/Jalissa termination (4302)**: $3,007.37 → $2,948.73 net; M'kenzy commission $418.72.

**Rollups _⟶ pull live_:**
- Total monthly rent roll across portfolio — _⟶ DoorLoop rent roll_
- Collection rate / delinquency this month — _⟶ DoorLoop + Payment Checklist_
- Reserve balances by property — _⟶ Baselane_
- Subscription + utility monthly outflow — _⟶ Payment Checklist (subscriptions + utilities tabs)_

## 4. Active Clients / Tenants & Health

| Tenant / Property | Health | Detail |
|---|---|---|
| Veronica — 3423 E Baylor | 🔴 Evicted | Evicted/foreclosed **June 25**; WIH regained access (need new master key). Property refinanced (~$500 lower payment) |
| Ronald & Samantha — 7500 Winston | 🔴 Eviction | Did not pay (25th); proceeding to eviction; no further contact per Josh |
| Joseph DeLaO — 4019 37th St | 🟢 Paying | Payment rising to $1,826.87 (+$152.79) Aug 1; insurance double-escrow resolved (see §8) |
| Tracy — 2802 S Channing | 🟢 Amended | Payment amount amended; DoorLoop merchant account approved |
| Aaron — 1312 65th Dr Unit E | 🟢 Renewing | New lease $850/mo; signature deadline July 20 via Crystal Sherwood |
| Elsa Galindo — 1926 27th St | 🟢 Converting | Switching to seller finance; lease being refied with Kiavi ($5k deposit) |
| 4205 E 61st St (mortgage) | 🟡 Watch | Mortgage was overdue (payment processing); Kenneth/Shellpoint pulling — recheck Mon |
| 4626 S Lipscomb | 🟡 Watch | One-time mortgage payment made (~$3.9k); Xcel Energy past-due still needs resolving (login reset) |

_Full tenant roster & current statuses ⟶ pull live from DoorLoop + Payment Checklist._

## 5. Team Status & Capacity

- **Mostafa (me)** — operations + automations; capacity stretched across payments, property issues, marketing push, and AI buildout. Overnight-CT working hours.
- **M'kenzy** — deals/showings/Airbnb. Runs Airbnbs (e.g., owner "Don," ~$11k/mo) via Airbnb auto-split. Exploring an Airbnb **partnership** with WIH (partner % in lieu of mgmt fee; AI to handle guest messages). Running 4513/4302 showings.
- **Kenneth** — partner; mortgages/lenders/refis (Kiavi, Shellpoint, Fay, Southern Loan Servicing); loan-broker access. Route lender tasks here.
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
- **4626 Lipscomb title (confirmed)**: held by the **4626 S Lipscomb St Irrevocable Trust**, beneficiary **Webber Wealth Holdings LLC** (subject-to acquisition w/ seller lease-back to John Arthur Castillo). The trust has **no EIN of its own by design** — so it correctly does NOT appear in the EIN registry. Not a data gap.
- **Skills-sync auth**: shared-skills push hit `403` on 2026-06-24 (the embedded PAT was rotated). Fixed by switching the `.skills-shared` clone to Git Credential Manager + adding a retry for pending-but-unpushed commits. `mercury-balance-sync` is now shared.
- **Credentials hygiene**: skill files had hardcoded API tokens (caught by GitHub push protection) — now excluded + secret-scan guard on sync. Don't commit live tokens.
- **Double-escrow insurance (4019, Jun 25)**: two homeowner policies (Portega/Black Opal + Allstate) were both escrowed via Fay Servicing → paying twice. Caught it, cancelled Portega, kept Allstate, requested refund. Lesson: when a new policy is placed, verify the old one is cancelled before the servicer escrows both.
- **Servicing setup gap (4302, Jun 26)**: lender Blake Hoffman went unpaid because Southern Loan Servicing never created the 4302 account (only 4205) despite a March submission. Lesson: confirm the servicer actually opened each account, don't assume a portal submission took.
- **Electric blind spot (1312)**: a back unit's AC switched back on doubled the bill (~$1,107). Action: per-unit thermostats; consider efficiency audit.
- **Systems > goals**: "You don't rise to the level of your goals, you fall to the level of your systems." — the operating ethos here.

## 9. Upcoming Milestones

- **Mon (next biz day)** — call Jessica @ Southern Loan Servicing to open the 4302 account (Blake Hoffman payment); recheck 4205 mortgage pull; revisit Kenneth for 3423 E Baylor PITI + portal credentials.
- **This weekend** — build the docs-mailbox AI automation (mortgage/utility statements + receipts).
- **July 20, 2026** — Aaron lease-renewal signature deadline (1312 Unit E) via Crystal Sherwood; **Aug 1** new term at $850/mo + Joseph DeLaO payment rises to $1,826.87.
- **Ongoing** — disposition of 4513 + 4302 (text-blast/Facebook); Jacoby 8-unit wholesale via Rex Andrews; Didi Haase portfolio proposal; selling-notes/partials as the next tier.

## 10. How This Doc Is Maintained

- **Source of record**: the Business Brain wiki (`wiki/`) + morning-meeting transcripts (`raw/`) + my operational memory.
- **Update cadence**: refreshed daily ~8:47 AM (CronCreate prompt) and committed/pushed; the durable 2-hourly "Business Brain Sync" task guarantees it reaches GitHub.
- **Commitment**: keep this current as the business changes — new payments, tenant status changes, project moves, milestones.
