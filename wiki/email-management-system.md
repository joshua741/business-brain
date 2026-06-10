---
name: email-management-system
type: project
tags: [email, automation, ai, communication, gmail]
status: active
sources: [CLAUDE.md seed]
updated: 2026-06-10
---

# Email Management System

**Summary**: AI-managed email triage and response system covering both joshua@ and docs@ inboxes, running hourly M–F with context-driven confidence scoring, auto-reply, and escalation routing.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-06-10

---

## What This Is

An autonomous email management layer that reads all incoming emails, looks up every sender across [[wih-app]] (Supabase), the wiki, and GHL, scores confidence in the AI's ability to respond correctly, and either replies automatically, creates a draft for Joshua's approval, or escalates.

Runs every hour Monday–Friday 6 AM – 7 PM CT via [[n8n]]. Invoked manually via `/email-management`.

## Accounts

| Account | Purpose |
|---|---|
| `joshua@webberinvestmenthomes.com` | Joshua's personal business email — deals, partners, lenders, legal, key contacts |
| `docs@webberinvestmenthomes.com` | Business operational email — subscriptions, vendors, servicers, team tools, invoices, all business-infrastructure correspondence |

**docs@ intent**: This is the business-wide operational inbox. Subscriptions (GHL, Railway, Supabase, etc.), mortgage servicer statements, vendor invoices, team tool accounts, LBK Cleaners supplier comms — all of it lives here. docs@ is also Mostafa's working account for Claude Code.

## Contact Lookup Hierarchy

1. **wih-app Supabase** (`public.contacts` table, project `catvxwoyguovitcyxwap`) — primary
2. **Wiki** — person pages, entity pages, and source transcripts
3. **GHL LeadConnector** — last resort, lookup only, no actions

If no match is found anywhere: 0 context points, automatic escalation to Joshua.

## Confidence Score Thresholds

| Score | Action |
|---|---|
| ≥95 | Auto-reply sent, label `AI-Handled` |
| 75–94 | Draft created, push notification to Joshua |
| 50–74 | No draft, push notification with 3-sentence summary |
| <50 | Immediate escalation push notification |
| Legal / money | Always escalate regardless of score |

## Gmail Labels Used

- `AI-Handled` — processed and replied
- `Needs-Review` — draft waiting for Joshua
- `Escalate` — Joshua must respond personally
- `Urgent` — legal, money movement, or high-stakes decision
- `Routed-to-Mostafa` — operational, passed to Mostafa

## Routing Rules

**joshua@ handles**:
- Deal counterparts (buyers, sellers, title, attorneys)
- Private/transactional lenders
- Key strategic partners
- Property servicers with decision requests
- Legal and government

**docs@ handles**:
- SaaS subscriptions and billing (GHL, Railway, Supabase, Zapier, etc.)
- Mortgage servicer statements
- Vendor invoices
- Team tool accounts
- LBK Cleaners vendor/supplier comms
- Insurance renewals

## Auto-Reply Guidelines

- Direct, professional, no corporate fluff
- Acknowledge → answer → next step
- Never mention entity names (Webber Investment Homes, Webber Wealth Holdings, W&M) to third parties
- Signature for joshua@: `Joshua Webber`
- Signature for docs@: `Webber Investment Homes Team`

## Notification Channels

| Person | Primary | Fallback |
|---|---|---|
| **Joshua** | Push notification (in-session) + SMS to 806-781-8495 via Twilio MCP | Email to joshua@webberinvestmenthomes.com |
| **Mostafa** | Telegram (anytime — no review needed) | Email to mostafa.webberinvestmenthomes@gmail.com |

## Mostafa Escalation

When an email is operational and falls in Mostafa's scope:
1. **Telegram message** via Telegram MCP (or email to `mostafa.webberinvestmenthomes@gmail.com` as fallback), subject: `[ACTION NEEDED] [original subject]`
2. Brief at top: what the email is, what action is needed in 2 sentences
3. CC `mostafa.webberinvestmenthomes@gmail.com` on thread if he's taking it over
4. Apply `Routed-to-Mostafa` label
5. Add task to NEW TASKS section of WIH Daily Schedule with "Mostafa —" prefix

## Notion Task Integration

**WIH Daily Schedule** (ID: `35a92db1-8570-81e3-a2c4-e6ddf3adff07`) is the single task source of truth.
- **Joshua tasks**: Add to NEW TASKS section (routes to his schedule on next rebuild)
- **Mostafa tasks**: Add to NEW TASKS section with "Mostafa —" prefix (auto-routes to Section 2 delegate list)
- **Existing task updates**: Find the task by keyword and append: `UPDATE: [sender] replied — [one-line summary] [date]`
- Tag all AI-generated tasks with `[AI]`

## Log

All run activity is appended to `wiki/email-management-log.md` after each pass.

## Setup Requirements

- [x] Gmail MCP connected to joshua@webberinvestmenthomes.com
- [ ] Gmail MCP connected to docs@webberinvestmenthomes.com (or set up as alias)
- [x] Mostafa's email confirmed: `mostafa.webberinvestmenthomes@gmail.com`
- [x] Joshua's SMS number confirmed: `806-781-8495`
- [x] wih-app Supabase project ID: `catvxwoyguovitcyxwap`
- [x] Notion WIH Daily Schedule page ID: `35a92db1-8570-81e3-a2c4-e6ddf3adff07`
- [ ] **Telegram MCP** — add to session config with Mostafa's bot token + chat ID (recommended over n8n for notifications)
- [ ] **Twilio MCP** — add to session config for direct SMS to Joshua at 806-781-8495
- [ ] n8n cron workflow — `0 6-19 * * 1-5` — triggers hourly email run (scheduling only, not notification routing)
- [ ] Gmail labels created: AI-Handled, Needs-Review, Escalate, Urgent, Routed-to-Mostafa

## Related pages
- [[mostafa]]
- [[ghl]]
- [[n8n]]
- [[wih-app]]
- [[contacts]]
- [[email-management-log]]
- [[joshua]]
