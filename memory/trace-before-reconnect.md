# Trace Before Reconnect — Always Go Back Through History

**Type**: HOW to work (behavioral rule)
**Durability**: Permanent — applies to every broken connection, every tool, every session
**Created**: 2026-06-11

---

## Rule

**Before attempting to reconnect, reconfigure, or debug any broken connection or tool, first trace how it was originally set up by going back through the git history.**

Never assume the connection method based on general knowledge. Always verify against what actually happened in this specific environment.

## When to Apply

- A tool or MCP server that used to work is now failing or returning errors
- A connection needs to be re-authorized or re-established
- Something worked in a previous session and isn't working now
- Investigating why an operation returns 403, 404, "not found," or "token expired"
- Any time before proposing a reconnection path to Joshua

## How to Do It

1. Run `git log --oneline --all` to see the full commit history
2. Search for commits referencing the tool or connection by name (e.g., "Gmail", "Nylas", "Twilio", "Notion")
3. Run `git show <commit-hash>` on relevant commits to see exactly what was changed
4. Check the connectors/ directory and connectors/STATUS.md for whether a local connector exists
5. Check `.claude/settings.local.json` for pre-authorized tools
6. If nothing exists in the repo — the connection was made at the environment level (Claude Code web UI), not in code

## Why This Matters

Discovered 2026-06-11 while debugging the Nylas Gmail MCP write operations (403 token expired). The instinct was to reconfigure via a known Nylas OAuth flow — but tracing the history revealed the connection was never in the repo at all. It was set up at the Claude Code remote environment level. That one finding changed the entire reconnection path: no code fix possible, Joshua needs to re-authorize through the environment settings UI.

Going off assumptions wastes time on the wrong fix. The git history is always the source of truth for how things were set up.

## What the History Can Tell You

- Was a connector script written for this tool? (`connectors/`)
- Was it configured via environment variables? (`.env.example`, vault setup commits)
- Was it set up at the Claude Code environment level? (if nothing is in the repo)
- Was the MCP server added to allowedTools, and when?
- What scopes or credentials were used originally?
