---
name: date-verification
type: concept
tags: [process, ai, memory, dates, calendar]
sources: [memory/date-verification.md]
updated: 2026-06-11
---

# Date Verification — Always Check Google Calendar

**Summary**: Permanent behavioral rule — before acting on any date or day of the week, always verify against Google Calendar. Never rely on the system context date alone.

**Sources**: memory/date-verification.md

**Last updated**: 2026-06-11

---

## The Rule

Before stating, assuming, or acting on any date or day of the week, call the Google Calendar MCP to confirm.

**Tool**: `list_events`
**Parameters**: `startTime: YYYY-MM-DDT00:00:00`, `endTime: YYYY-MM-DDT23:59:59`

The timezone and event `start.dateTime` fields in the response are the source of truth for both the date and the day of the week.

## Why This Exists

On 2026-06-11, the system `currentDate` context correctly showed June 11 but Claude stated it was Wednesday. It was **Thursday**. A wrong day-of-week causes the email management skill to skip processing (it checks weekday/weekend), and any scheduling logic silently fails.

The `currentDate` system reminder provides the date but not the day of week. Calendar confirmation is the only reliable source.

## When to Apply

Any task involving:
- Day-of-week checks (e.g. "is today a weekday?")
- Email triage (skill checks M–F before processing)
- Scheduling, cron validation, or calendar logic
- Any decision that changes based on the day

## Steps

1. Call `list_events` with today's date range
2. Read `timeZone` and `start.dateTime` from any returned event
3. Derive the actual day of week from the confirmed date
4. Proceed only after confirming

## Scope

Every skill, every task, every session — no exceptions.

## Related pages
- [[email-management-system]]
- [[claude-code-workflow]]
