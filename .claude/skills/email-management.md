# Email Management Skill

**Trigger**: `/email-management` or invoked by the hourly n8n automation

**Purpose**: Triage, contextualize, and respond to all unread emails across both inboxes using business context from wih-app, wiki, and GHL. Maintain communication with all active business contacts while protecting Joshua's time.

---

## Accounts in Scope

| Account | Role | Gmail MCP |
|---|---|---|
| `joshua@webberinvestmenthomes.com` | Personal deals, partners, lenders, legal, urgent | Primary (connected) |
| `docs@webberinvestmenthomes.com` | Subscriptions, vendors, team, servicers, invoices | Secondary (connect as alias or separate account) |

**Note on docs@**: If docs@ is not yet connected as a second MCP account, process only `joshua@` and flag this gap in the run log. The intent is for docs@ to handle all team/business operational correspondence.

---

## Execution Protocol

Run these phases in order on every invocation.

### Phase 1 — Load Context

Before touching any email:

1. Read `wiki/index.md` to orient on active projects and people
2. Read `wiki/email-management-system.md` for routing rules and any overrides
3. Read `wiki/contacts.md` for the known contact registry and recent interactions
4. Note today's date and day of week — only run M–F

### Phase 2 — Inbox Scan

Search for unread emails in both inboxes:

```
Query: in:inbox is:unread
Accounts: joshua@webberinvestmenthomes.com, docs@webberinvestmenthomes.com
```

For each unread email, capture:
- Sender email and name
- Subject line
- Thread ID (for reply continuity)
- Date/time received
- Full body text
- Whether it's part of an existing thread

Process oldest first. Do not skip any unread email.

### Phase 3 — Contact Resolution

For each sender, run this lookup chain in order. Stop at first match.

**Step 1 — wih-app Supabase** (primary):
```sql
SELECT id, name, email, phone, contact_type, pipeline, notes, metadata
FROM public.contacts
WHERE email ILIKE '[sender_email]'
LIMIT 1;
```
Also check adjacent tables if contact not found directly:
- `public.property_inquiries` (by phone or name match)
- `public.homepage_inquiries` (by name match)
- `public.pml_inquiries` (by email)
- `public.user_submissions` (by email)

**Step 2 — Wiki** (if not in wih-app):
Search `wiki/` for a page matching the sender's name or company. Check `wiki/index.md` people section. If found, read the full wiki page for context.

**Step 3 — GHL LeadConnector** (last resort, only if steps 1-2 yield nothing):
Use `leadconnector` tool to look up by email or name. Extract any available relationship context. Do NOT use GHL for any action — lookup only.

**Step 4 — No match**:
If the sender appears in zero sources, score them at 0 context points. Flag for Joshua review with a brief summary of the email content.

### Phase 4 — Confidence Score

Score each email 0–100. Start at 0, add points:

| Factor | Points |
|---|---|
| Sender found in wih-app contacts | +30 |
| Sender has a wiki page with documented relationship | +20 |
| Email topic maps to an active project or property in wiki | +15 |
| Prior thread history exists in this Gmail thread | +15 |
| Requested action matches a known SOP or pattern | +10 |
| Email intent is unambiguous — one clear ask | +10 |
| **Maximum** | **100** |

**Deductions** (apply if present):
- Legal language, demand letters, or formal notices: −20 (always escalate to Joshua)
- Request involves money movement or wire instructions: −30 (never auto-reply)
- Sender is unknown + email contains urgency language: −15

### Phase 5 — Routing Decision

| Score | Action |
|---|---|
| **≥95** | Auto-reply via Gmail, mark read, apply label `AI-Handled` |
| **75–94** | Draft reply via Gmail, push notification to Joshua: "Draft ready: [Sender] — [Subject]. Approve or edit in Gmail." |
| **50–74** | No draft. Push notification to Joshua with a 3-sentence summary: who sent it, what they want, why it needs his call. Apply label `Needs-Review` |
| **<50** | Immediate push notification. Apply label `Escalate`. If Mostafa-relevant, also notify Mostafa per Phase 7. |
| **Legal / money movement** | Never auto-reply. Immediate push notification to Joshua regardless of score. Apply label `Urgent`. |

### Phase 6 — Inbox Routing Rules

**Route to `joshua@` response queue:**
- Deals, acquisitions, creative finance negotiations
- Private money lenders and transactional lenders
- Title companies (Hub City Title, etc.)
- Legal or government correspondence
- Key partners: Austin Hughes, any active deal counterpart
- Property servicers when a decision is required
- Anything from a known person with an active deal in the wiki

**Route to `docs@` response queue** (reply FROM docs@, or flag for docs@ if not yet connected):
- Subscription billing: GHL, Railway, Supabase, Zapier, Twilio, n8n, ElevenLabs, BookingKoala
- Mortgage servicer statements: Rocket Mortgage, Lakeview, One-Point Lending
- Vendor invoices and receipts
- Team tool accounts — anything where Mostafa or M'kenzy is the operator
- LBK Cleaners vendor or supplier correspondence
- Insurance policies and renewals

### Phase 7 — Draft Reply Guidelines

When writing a reply (auto or draft):

**Tone**: Direct, professional but not corporate. Short paragraphs. Clear next step in last sentence.

**Signature — joshua@**:
```
Joshua Webber
```

**Signature — docs@**:
```
Webber Investment Homes Team
```

**Never mention**: Webber Investment Homes, Webber Wealth Holdings, or W&M Series LLC in external vendor/third-party replies.

**Auto-reply rules**:
- Acknowledge what they asked in one sentence
- Answer or confirm in 1–3 sentences
- State the next step or expected timeline
- No filler, no "I hope this email finds you well"
- If you're confirming a task, note that Mostafa will follow up if action is needed

**Example auto-reply structure**:
> Got it — [brief confirmation of their request]. [Answer or next step]. [Timeline or Mostafa follow-up note if applicable].

### Phase 8 — Mostafa Escalation Protocol

Escalate to Mostafa when:
- Email is operational: property maintenance, vendor scheduling, tenant follow-up
- Email is LBK Cleaners operational (not strategic)
- Email in docs@ inbox involves team tooling that needs hands-on action
- Score is <75 and the topic is within Mostafa's ops scope

**How to notify Mostafa**:
1. Send email TO: `docs@webberinvestmenthomes.com` (his working account)
2. Subject: `[ACTION NEEDED] [original subject]`
3. Body: Forward the original email with a 2-sentence brief at the top: what it is, what action is needed
4. CC the original sender if Mostafa is taking over the thread
5. Apply label `Routed-to-Mostafa` on the original email

**When to CC Mostafa on a reply**:
If auto-replying on behalf of Joshua but execution falls to Mostafa, CC `docs@webberinvestmenthomes.com` in the reply so Mostafa has full thread context.

### Phase 9 — Labels to Apply

Create these Gmail labels if they don't exist:
- `AI-Handled` — auto-replied, no further action needed
- `Needs-Review` — draft created, waiting on Joshua approval
- `Escalate` — urgent, requires Joshua's direct attention
- `Urgent` — legal, money, or critical decision
- `Routed-to-Mostafa` — passed to Mostafa for action

### Phase 10 — Post-Run Log

After processing all emails, append to `wiki/email-management-log.md`:

```
## [YYYY-MM-DD HH:MM CT]
- Emails processed: [N]
- Auto-replied: [N] — [list subjects]
- Drafts created: [N] — [list subjects + senders]
- Escalated to Joshua: [N] — [list subjects + reason]
- Routed to Mostafa: [N] — [list subjects]
- New contacts added to wiki: [N]
- Notes: [anything notable this run]
```

Also update `wiki/contacts.md` if any new senders were identified and had enough context to document.

---

## Scheduling

This skill runs automatically via n8n:
- **Schedule**: Every hour, Monday–Friday, 6:00 AM – 7:00 PM CT
- **n8n workflow**: `Email Management — Hourly Triage`
- **Manual trigger**: `/email-management` in any Claude Code session

To start the loop manually in a session: `/loop 1h /email-management`

---

## What This Skill Does NOT Do

- Does not delete emails — archive only, never delete
- Does not move money or approve financial transactions
- Does not respond to legal demands — always escalates
- Does not reply on behalf of Joshua to unknown senders below 50 confidence
- Does not use GHL for any action — contact lookup only
- Does not send outbound cold emails — reactive/response only
