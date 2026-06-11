# Impact-First Ordering — Always Start With the Most Impactful Thing

**Type**: HOW to work (behavioral rule)
**Durability**: Permanent — applies to every multi-step task, every session
**Created**: 2026-06-11

---

## Rule

**Before executing a list of tasks, explicitly identify the goal, rank the list by impact toward that goal, and start with the highest-impact item.**

This applies to: building, reconnecting, testing, debugging, planning, and any session with multiple open items.

## How to Apply

1. State the goal in one sentence — what does "done" look like?
2. Look at the full task list and ask: which single item, if completed right now, moves us closest to that goal?
3. Start there. Complete it. Then re-rank if needed before moving to the next.
4. If two items are close in impact, prefer the one that unblocks the most other items downstream.

## Why This Matters

Joshua moves fast. Sessions have natural time limits. Starting with low-impact items means the highest-value work may never get done in that session. Starting with the most impactful item guarantees that even if the session ends early, the most important progress was made first.

## When to Apply

- A list of reconnections, fixes, or configurations needs to be worked through
- Multiple features or improvements are on deck
- A skill is being built and there are many components
- Debugging: multiple possible causes — investigate the one most likely to unblock everything else first
- End of session re-planning: before listing next steps, rank them by impact

## Example

Goal: email skill runs fully autonomously.  
Wrong order: set up labels → configure Telegram → fix Gmail write → wire cron  
Right order: fix Gmail write (core blocker) → Telegram (ops routing) → SMS (escalations) → cron (automation) → labels (cosmetic)
