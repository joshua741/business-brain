# Skill Permissions — Always Pre-Authorize Tools

**Type**: HOW to work (behavioral rule)
**Durability**: Permanent — applies to every skill, every session
**Created**: 2026-06-11

---

## Rule

**After every skill is tested and functional (minimum: setup phase complete), immediately add every tool it uses to `allowedTools` in `.claude/settings.local.json`.**

No skill ships without its tools pre-authorized. Full stop.

## Why

Skills are built to run autonomously — triggered by n8n, cron, or another agent with no human at the keyboard. If a tool isn't in `allowedTools`, Claude Code pauses and waits for a human to approve. In an automated run, that pause means the skill silently dies. The entire point of the skill is defeated.

Discovered during email management skill run #2 (2026-06-11): every tool call that hadn't been pre-authorized fired an approval prompt, requiring Joshua to manually respond "Tool loaded" or approve each one before the run could continue. In a live automated session, those prompts would have killed the run.

## When to Apply

- A new skill is created → before the first test run, add all known tools to `allowedTools`
- A skill is tested and passes initial setup → confirm all tools are in `allowedTools`, commit
- A skill adds a new tool during development → add it to `allowedTools` in the same commit
- End of any skill-building session → run a quick audit: does every tool in the skill have a matching entry in `allowedTools`?

## How to Identify the Tools

Read the skill file and list every MCP tool called across all phases. Add all of them. When in doubt, add more than needed — extra entries in `allowedTools` cause no harm.

## Where to Update

`.claude/settings.local.json` in the repo — under `permissions.allow`. Commit and push alongside the skill file.

## Scope

Every skill. Every tool. No exceptions. This is not optional for skills intended to run autonomously.
