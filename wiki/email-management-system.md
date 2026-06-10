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
| `joshua@webberinvestmenthomes.com` | Deals, partners, lenders, legal, property decisions |
| `docs@webberinvestmenthomes.com` | Subscriptions, vendors, team ops, servicers, receipts |

**Important**: docs@ is also where [[mostafa]] operates (his Claude account). Anything flagged for him is sent to docs@ with an `[ACTION NEEDED]` prefix subject.

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

## Mostafa Escalation

When an email is operational and falls in Mostafa's scope:
1. Email to `docs@webberinvestmenthomes.com` with `[ACTION NEEDED]` subject
2. Brief: what the email is, what action is needed
3. CC Mostafa on the thread if he's taking it over
4. Apply `Routed-to-Mostafa` label

## Log

All run activity is appended to `wiki/email-management-log.md` after each pass.

## Setup Requirements

- [x] Gmail MCP connected to joshua@webberinvestmenthomes.com
- [ ] Gmail MCP connected to docs@webberinvestmenthomes.com (or set up as alias)
- [ ] Mostafa's direct email confirmed and added to [[mostafa]] wiki page
- [x] wih-app Supabase project ID: `catvxwoyguovitcyxwap`
- [ ] n8n hourly workflow created (`Email Management — Hourly Triage`)
- [ ] Gmail labels created: AI-Handled, Needs-Review, Escalate, Urgent, Routed-to-Mostafa

## Related pages
- [[mostafa]]
- [[ghl]]
- [[n8n]]
- [[wih-app]]
- [[contacts]]
- [[email-management-log]]
- [[joshua]]
