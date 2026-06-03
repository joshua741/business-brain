---
name: source-claude-code-creator-starts-project
type: source
tags: [clip, claude-code, ai-operating-system, workflow, boris-cherny]
status: complete
sources: [clip-2026-06-03-how-claude-code-s-creator-starts-every-project.md]
updated: 2026-06-03
---

# How Claude Code's Creator Starts EVERY Project

**Summary**: Austin Marchese reverse-engineers Boris Cherny's (creator of Claude Code, Anthropic) workflow into 6 principles — Plan Mode first, minimal CLAUDE.md, verification loops, parallel sessions, Skills, and betting on the general model.

**Sources**: clip-2026-06-03-how-claude-code-s-creator-starts-every-project.md

**Last updated**: 2026-06-03

---

A distillation of [[boris-cherny]]'s [[claude-code-workflow]] into 6 principles.

## Core method / framework
1. **Plan Mode** — start ~80% of sessions in Plan Mode (Shift+Tab twice). "Move slow to move fast." Have Claude interview you before building.
2. **Minimal CLAUDE.md** — keep it short (~couple thousand tokens); update only when a mistake occurs. If it bloats, delete and rebuild minimally.
3. **Verification loops** — give Claude a tool to see its output + a description of it; feedback loops 2–3x quality.
4. **Multiply yourself** — parallel partitioned Claude sessions / git worktrees. "Two context windows that don't know about each other tend to have better results."
5. **Inner loops → Claude Skills** — document repeated daily tasks as slash commands/Skills ("prompt = dribble the ball; Skill = the exact play").
6. **Build for the future** — "The Bitter Lesson" (Rich Sutton): the more general model always beats the specific one; "never bet against the model"; invest in your Information Moat (quality of data/context).

## Tools
Claude Code, CLAUDE.md, Plan Mode, Claude Skills, slash commands, git worktrees, Rich Sutton's "The Bitter Lesson."

## Actionable for Joshua
- Adopt Plan-Mode-first for all [[wih-app]] / [[wih-ai-service]] builds.
- Periodically prune his large CLAUDE.md ("remove anything no longer needed, contradictory, duplicate, bloat").
- Add "before any work, mention how you could verify it"; build verification into [[content-ai]] and automations.
- "Information Moat" reframes the [[business-brain]] wiki as the durable asset — see [[information-moat]].
- Parallel sessions map to agent-teams for wih-app.

## Maps to
[[claude-api]], [[ai-operating-system]], [[ai-automation-strategy]], [[business-brain]], [[wih-app]], [[boris-cherny]], [[information-moat]], [[claude-code-workflow]]

## Key verbatim lines
- "Probably 80% of my sessions I start in plan mode."
- "Move slow to move fast."
- "Do the minimal possible thing in order to get the model on track."
- "If Claude has that feedback loop, it will 2-3x the quality."
- "Two context windows that don't know about each other tend to have better results."
- "never bet against the model."
- "AI will never be as bad as it is today."

## Related pages
- [[boris-cherny]]
- [[claude-code-workflow]]
- [[information-moat]]
- [[ai-operating-system]]
- [[business-brain]]
