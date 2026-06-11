---
name: skill-permissions-rule
type: concept
tags: [process, ai, skills, permissions, automation]
sources: [memory/skill-permissions-rule.md]
updated: 2026-06-11
---

# Skill Permissions — Always Pre-Authorize Tools

**Summary**: Every skill must have all its required tools added to `allowedTools` in `.claude/settings.local.json` once it passes initial setup. Without this, autonomous runs die silently when permission prompts fire with no human present.

**Sources**: memory/skill-permissions-rule.md

**Last updated**: 2026-06-11

---

## The Rule

After every skill is tested and functional (minimum: setup phase complete), immediately add every tool it uses to `allowedTools` in `.claude/settings.local.json`. No skill ships without its tools pre-authorized.

## Why This Matters

Skills run autonomously — triggered by n8n or cron with no human present. When a tool isn't pre-authorized, Claude Code pauses and waits for a human to approve. In an automated run, that pause = the skill dies silently mid-execution.

Discovered during email management skill run #2 (2026-06-11): approval prompts fired on every non-pre-authorized tool, requiring manual "Tool loaded" responses. In a live automated session with no human, those would have killed the run entirely.

## The Process

1. When building a skill — identify all MCP tools used across every phase of the skill
2. Add all of them to `permissions.allow` in `.claude/settings.local.json`
3. Commit the settings update alongside the skill file
4. After testing confirms the skill works — verify the allowedTools list is complete
5. If a new tool is added to a skill during development — update `allowedTools` in the same commit

## Applies To

Every skill. Every tool. No exceptions. Existing skills need to be audited and backfilled if their tools aren't already pre-authorized.

## Related pages
- [[email-management-system]]
- [[claude-code-workflow]]
- [[skill-permissions-rule]]
