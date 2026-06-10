---
name: contacts
type: concept
tags: [contacts, email, crm, context]
sources: [CLAUDE.md seed, wiki pages]
updated: 2026-06-10
---

# Contacts Registry

**Summary**: Supplemental contact registry for the email management system. Tracks email addresses, confidence context, and communication history for people who email Joshua. This supplements wih-app Supabase — entries here are for people who have wiki pages or specific email context not yet in the app.

**Sources**: CLAUDE.md seed, wiki person pages

**Last updated**: 2026-06-10

---

## How This Works

When the email management system processes an email:
1. It checks `public.contacts` in wih-app Supabase first (by email)
2. If not found there, it checks this page and the wiki person pages
3. If still not found, it checks GHL as a last resort

This page is updated by the email management system when:
- A new sender is identified who has enough context to document
- A wiki person page is linked to an email address

---

## Known Contacts — Internal Team

| Name | Email | Notification | Role | Context Source |
|---|---|---|---|---|
| Mostafa Elkhamisy | mostafa.webberinvestmenthomes@gmail.com | Telegram (primary) | Operations Lead | [[mostafa]] |
| M'kenzy | — | — | Team member | [[mkenzy]] |
| Kenneth | — | — | Team member | [[kenneth]] |
| Joshua Webber | joshua@webberinvestmenthomes.com | Push + SMS 806-781-8495 | Owner / decision-maker | [[joshua]] |

---

## Known Contacts — Partners & Vendors

| Name | Email | Relationship | Wiki Page |
|---|---|---|---|
| Austin Hughes | — | Thunder Sun Homes, 9-unit deal | [[austin-hughes]] |
| Aaron McCloskey | — | Contact | [[aaron-mccloskey]] |
| Josh Fox | — | Contact | [[josh-fox]] |
| Jacob Swim | — | Contact | [[jacob-swim]] |
| Hub City Title | — | Title company | [[hub-city-title]] |
| One-Point Lending | — | Note servicer (4438 Puffer St) | [[one-point-lending]] |

> Email addresses above are unknown — add as encountered.

---

## Known Contacts — Servicers & Lenders (docs@ inbox)

| Name | Email | Account | Context |
|---|---|---|---|
| Rocket Mortgage | — | 2802 S Channing mortgage | [[rocket-mortgage]] |
| Lakeview | — | Yvonne/Scott subject-to | [[lakeview]] |
| GoHighLevel | — | Subscription | [[ghl]] |
| Railway | — | Subscription | [[railway]] |
| Supabase | — | Subscription | [[supabase]] |
| Twilio | — | Subscription | [[twilio]] |

> Email addresses above are unknown — auto-populated by email management system on first encounter.

---

## Confidence Context Notes

**High-confidence auto-reply patterns** (score 95+ expected):
- Subscription renewal/billing confirmations → acknowledge receipt, no action
- Mortgage statement delivery notifications → acknowledge, file
- Booking confirmation from BookingKoala (docs@ feed) → acknowledge
- Routine "check-in" from known partners already in wiki

**Always-escalate patterns** (regardless of score):
- Any email from an attorney or with "legal notice," "demand," "default," "foreclosure"
- Wire transfer instructions or requests for financial account details
- Government/IRS/tax authority correspondence
- Any unknown sender asking for personal information

---

## Email-to-Wiki Index

| Email Address | Contact Name | Wiki Page |
|---|---|---|
| mostafa.webberinvestmenthomes@gmail.com | Mostafa Elkhamisy | [[mostafa]] |
| docs@webberinvestmenthomes.com | Mostafa Elkhamisy (working account) | [[mostafa]] |
| joshua@webberinvestmenthomes.com | Joshua Webber | [[joshua]] |

> This index grows automatically as the email management system processes emails and identifies senders.

## Related pages
- [[email-management-system]]
- [[mostafa]]
- [[wih-app]]
- [[ghl]]
