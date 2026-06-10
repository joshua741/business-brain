# Email Management Skill

**Trigger**: `/email-management` or invoked by the hourly n8n automation (cron: `0 6-19 * * 1-5`)

**Purpose**: Triage, contextualize, and respond to all unread emails across both inboxes. Look up every sender using wih-app → wiki → GHL. Reply autonomously at ≥95% confidence. Escalate below that. Keep Joshua's and Mostafa's Notion tasks in sync with every email action. Run hourly M–F, 6 AM–7 PM CT.

---

## Accounts in Scope

| Account | Role |
|---|---|
| `joshua@webberinvestmenthomes.com` | Joshua's personal business email — deals, partners, lenders, legal, key contacts |
| `docs@webberinvestmenthomes.com` | Business operational email — subscriptions, vendors, servicers, team tools, invoices, anything business-infrastructure related |

Both accounts run through the same Gmail MCP. When docs@ is not yet connected as a separate account or alias, note it in the run log and process joshua@ only.

---

## People & Notification Channels

| Person | Role | Email | Notification Channel |
|---|---|---|---|
| **Joshua Webber** | Owner / decision-maker | joshua@webberinvestmenthomes.com | Push notification (in-session) + SMS to **806-781-8495** via Twilio MCP |
| **Mostafa Elkhamisy** | Operations lead | mostafa.webberinvestmenthomes@gmail.com | **Telegram** (anytime, no review needed) + task added to his Notion delegate section |

**SMS to Joshua (806-781-8495)**: Use Twilio MCP when available. For urgent escalations during automated (non-session) runs, send via email to joshua@webberinvestmenthomes.com as fallback.

**Telegram to Mostafa**: Use Telegram MCP when available. Fallback: email to mostafa.webberinvestmenthomes@gmail.com. Mostafa does not need to review/approve — he just gets notified and his task gets created.

---

## Execution Protocol

Run these phases in order on every invocation.

### Phase 1 — Load Context

1. Read `wiki/index.md` — orient on active projects, properties, and people
2. Read `wiki/email-management-system.md` — routing rules and any overrides
3. Read `wiki/contacts.md` — known contact email registry
4. Confirm it is a weekday. Do not process emails on Saturday or Sunday.

### Phase 2 — Inbox Scan

Search both inboxes for unread email:

```
Query: in:inbox is:unread
```

Run against: `joshua@webberinvestmenthomes.com` and `docs@webberinvestmenthomes.com`

For each unread email, capture:
- Sender name and email address
- Subject line
- Thread ID (for reply continuity)
- Date/time received
- Full body text
- Whether it's part of an existing thread

Process oldest first. Do not skip any unread email.

### Phase 3 — Contact Resolution

For each sender, run this lookup chain in order. Stop at the first meaningful match.

**Step 1 — wih-app Supabase** (primary CRM):
```sql
-- Primary lookup
SELECT id, name, email, phone, contact_type, pipeline, notes, metadata
FROM public.contacts
WHERE email ILIKE '[sender_email]'
LIMIT 1;

-- Secondary lookups if primary returns nothing
SELECT first_name, last_name, email, phone FROM public.user_submissions WHERE email ILIKE '[sender_email]' LIMIT 1;
SELECT first_name, last_name, email, phone FROM public.pml_inquiries WHERE email ILIKE '[sender_email]' LIMIT 1;
SELECT first_name, last_name, phone, message FROM public.property_inquiries WHERE phone = '[sender_phone]' LIMIT 1;
```

**Step 2 — Wiki** (if not in wih-app):
Check `wiki/contacts.md` email index first. Then search wiki person pages by name. If a page exists, read it fully for relationship context.

**Step 3 — GHL LeadConnector** (last resort — lookup only, no actions):
Use `leadconnector` to search by email or name. Extract relationship context only.

**Step 4 — No match**:
Zero context points. Flag for Joshua escalation with a summary.

### Phase 4 — Confidence Score

Score each email 0–100. Start at 0, add points:

| Factor | Points |
|---|---|
| Sender found in wih-app contacts table | +30 |
| Sender has a wiki page with documented relationship | +20 |
| Email topic maps to an active project or property in wiki | +15 |
| Prior thread history exists in this Gmail thread | +15 |
| Requested action matches a known SOP | +10 |
| Email intent is completely unambiguous — single clear ask | +10 |
| **Maximum** | **100** |

**Deductions**:
- Legal language, demand letters, notices: −20 (always escalate)
- Money movement, wire instructions, financial account requests: −30 (never auto-reply)
- Unknown sender + urgency language: −15

### Phase 5 — Routing Decision

| Score | Action |
|---|---|
| **≥95** | Auto-reply via Gmail, mark read, label `AI-Handled` |
| **75–94** | Draft reply via Gmail, push notification + SMS to Joshua: "Draft ready — [Sender]: [Subject]. Check Gmail to approve." |
| **50–74** | No draft. Push notification + SMS to Joshua with 3-sentence summary: who, what they want, why it needs his judgment. Label `Needs-Review`. |
| **<50** | Immediate push + SMS to Joshua. Label `Escalate`. If Mostafa-relevant, also notify Mostafa via Telegram and create his task. |
| **Legal / money** | Immediate push + SMS to Joshua regardless of score. Label `Urgent`. Never draft. |

### Phase 6 — Inbox Routing Rules

**Reply FROM `joshua@`** when:
- Deal counterparts: buyers, sellers, title companies (Hub City Title, etc.)
- Private / transactional lenders and PML contacts
- Key strategic partners: Austin Hughes, active deal counterparts
- Legal, government, insurance correspondence
- Property servicers when a Joshua decision is required
- Any known person with an active deal in the wiki

**Reply FROM `docs@`** (or flag for docs@ if not yet connected) when:
- SaaS subscriptions: GHL, Railway, Supabase, Zapier, Twilio, n8n, ElevenLabs, BookingKoala
- Mortgage servicer statements: Rocket Mortgage, Lakeview, One-Point Lending, Shellpoint, Freedom Mortgage
- Vendor invoices, receipts, expense confirmations
- Team tool accounts — anything Mostafa or M'kenzy operates
- LBK Cleaners vendor or supplier correspondence
- Insurance renewals

### Phase 7 — Draft Reply Guidelines

**Tone**: Direct, professional, zero corporate fluff. Short paragraphs. Clear next step in the last sentence.

**Signature — `joshua@`**:
```
Joshua Webber
```

**Signature — `docs@`**:
```
Webber Investment Homes Team
```

**Never include** in external replies: Webber Investment Homes, Webber Wealth Holdings, W&M Series LLC (to vendors or third parties).

**Auto-reply structure**:
> Got it — [brief one-line confirmation]. [Answer or next step in 1–3 sentences]. [Timeline or handoff note if Mostafa is taking action].

No preamble. No "hope this finds you well." Lead with the answer.

### Phase 8 — Mostafa Escalation Protocol

Route to Mostafa when the email is operational:
- Property maintenance, vendor coordination, tenant follow-up
- LBK Cleaners operational (not strategic)
- docs@ inbox items that need hands-on action
- Anything score <75 that falls within Mostafa's ops scope per the wiki

**Notify Mostafa (in order of preference)**:
1. **Telegram message** (via Telegram MCP) — anytime, immediate
2. **Email fallback**: Send to `mostafa.webberinvestmenthomes@gmail.com`, subject: `[ACTION NEEDED] [original subject]`, body: 2-sentence brief at top (what it is, what action is needed) + forwarded original email content

**CC Mostafa on thread**: When auto-replying on behalf of Joshua but Mostafa handles execution, CC `mostafa.webberinvestmenthomes@gmail.com` in the reply.

**Apply label**: `Routed-to-Mostafa` on the original email.

### Phase 9 — Notion Task Updates

After every email action, update the Notion task accordingly. **The WIH Daily Schedule is the source of truth.**

**Page**: WIH Daily Schedule — Webber Wealth Holdings
**Notion page ID**: `35a92db1-8570-81e3-a2c4-e6ddf3adff07`

**To add a task for Joshua**: Append to the **NEW TASKS** section. No prefix needed. Tag with `[AI]`.

**To add a task for Mostafa**: Append to the **NEW TASKS** section, prefixed with "Mostafa —". This auto-routes to his delegate section on next rebuild. Tag with `[AI]`.

**When to add/update a task**:
1. **New email requires action from Joshua** → add to NEW TASKS for Joshua
2. **New email requires action from Mostafa** → add to NEW TASKS for Mostafa
3. **New email updates context on an existing task** → find the existing task in the schedule and append the update note directly (e.g., "UPDATE: [sender] replied — [one-line summary] [date]")
4. **Auto-reply sent** → no task needed unless it has an open follow-up
5. **Thread continues with new info** → re-check for any existing task linked to that sender/topic and update it

**Task format for NEW TASKS**:
```
[AI Email] [Sender Name] — [one-line action] | Context: [one sentence why] [AI]
```

Example: `[AI Email] Jacob Swim — Review Allstate renewal quote for 4019 37th St | Context: Renewal quote received via email [AI]`

### Phase 10 — Gmail Labels

Create these labels if they don't exist (one-time setup):
- `AI-Handled` — replied automatically
- `Needs-Review` — draft waiting Joshua approval
- `Escalate` — requires Joshua personally
- `Urgent` — legal, money, or critical
- `Routed-to-Mostafa` — operational, Mostafa notified

### Phase 11 — Post-Run Log

Append to `wiki/email-management-log.md` after every pass:

```markdown
## [YYYY-MM-DD HH:MM CT]
- Emails processed: N
- Auto-replied: N — [subjects]
- Drafts created: N — [sender + subject]
- Escalated to Joshua: N — [subject + reason]
- Routed to Mostafa: N — [subject]
- Tasks added to Joshua Notion: N
- Tasks added to Mostafa Notion: N
- New contacts documented: N
- Notes: [anything notable]
```

Update `wiki/contacts.md` email index whenever a new sender is identified with enough context to document.

---

## Scheduling

- **Automated**: n8n cron `0 6-19 * * 1-5` (every hour M–F 6 AM–7 PM CT) triggers Claude Code API → `/email-management`
- **Manual**: `/email-management` in any Claude Code session
- **Session loop**: `/loop 1h /email-management`

---

## Required MCPs / Integrations

| Integration | Status | Used For |
|---|---|---|
| Gmail MCP (joshua@) | ✅ Connected | Read/reply/label emails |
| Gmail MCP (docs@) | ⚠️ Pending | Read/reply docs@ inbox |
| Twilio MCP | ⚠️ Pending | SMS to Joshua at 806-781-8495 |
| Telegram MCP | ⚠️ Pending | Notify Mostafa instantly |
| wih-app Supabase | ✅ Connected | Contact lookup (project: `catvxwoyguovitcyxwap`) |
| Notion MCP | ✅ Connected | Task updates (WIH Daily Schedule) |
| GHL LeadConnector | ✅ Connected | Contact context fallback only |

---

## Hard Rules

- Never delete emails — archive only
- Never respond to legal demands — always escalate to Joshua
- Never act on wire transfer or money movement instructions — always escalate
- Never reply on behalf of Joshua to unknown senders below 50 confidence
- Never use GHL for any action — contact lookup only
- Never send outbound cold email — this system is reactive/response only
- Never disclose entity names (Webber Investment Homes, Webber Wealth Holdings, W&M) to external vendors or third parties
