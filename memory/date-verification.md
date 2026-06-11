# Date Verification — Always Check Google Calendar

**Type**: HOW to work (behavioral rule)
**Durability**: Permanent — applies to every session, every task
**Created**: 2026-06-11

---

## Rule

**Before stating, assuming, or acting on any date or day of the week, always verify against Google Calendar.**

Use `list_events` for today's date window (start: `YYYY-MM-DDT00:00:00`, end: `YYYY-MM-DDT23:59:59`). The timezone on returned events is the source of truth for both date and day of week.

Do not rely on the `currentDate` system reminder alone — it provides the date but not the day of week, and can be misread.

## Why

On 2026-06-11, the system context said "today is June 11" but I stated it was Wednesday. It was Thursday. A wrong day-of-week causes the email skill to skip processing (it checks for weekdays) and any scheduling logic to fail silently.

## How to Apply

1. When any task involves a date-sensitive decision (email triage, scheduling, day-of-week checks, cron logic, "is today a weekday?"):
   - Call `list_events` with today's date range
   - Read the `timeZone` and event `start.dateTime` in the response
   - Derive the actual day of week from the confirmed date
2. Proceed only after confirming

## Scope

Every skill, every task, every session — no exceptions.
