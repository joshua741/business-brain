---
name: claude-code-workflow
type: concept
tags: [claude-code, workflow, ai-operating-system, build]
sources: [clip-2026-06-03-how-claude-code-s-creator-starts-every-project.md, clip-2026-06-03-how-to-build-a-business-intelligence-dashboard-with-claude-a.md]
updated: 2026-06-03
---

# Claude Code Workflow

**Summary**: How Joshua builds software with Claude Code, synthesized from [[boris-cherny]] (creator of Claude Code) and the No Fluff Operator BI-dashboard build.

**Sources**: clip-2026-06-03-how-claude-code-s-creator-starts-every-project.md, clip-2026-06-03-how-to-build-a-business-intelligence-dashboard-with-claude-a.md

**Last updated**: 2026-06-03

---

The working method behind Joshua's software builds, drawn from [[boris-cherny]] (creator of Claude Code) and a worked BI-dashboard build.

## Six principles
1. **Plan Mode first** (~80% of sessions). "Move slow to move fast." Have Claude interview you before building.
2. **Minimal CLAUDE.md** — keep it short; update only on mistakes; prune when bloated.
3. **Verification loops** — give Claude a way to see its own output → 2–3x quality. "Before any work, say how you'd verify it."
4. **Multiply yourself** — parallel partitioned sessions / git worktrees / agent-teams.
5. **Inner loops → Skills** — turn repeated tasks into slash commands / Skills.
6. **Build for the future / "never bet against the model"** — invest in the [[information-moat]], not prompt-tuning.

## Build pattern (BI dashboard)
Scaffold key features → Plan Mode → [[ghl]] → [[supabase]] → [[railway]]/Vercel → secrets in `.env.local` → verify locally and let Claude fix its own errors → cron auto-sync → GitHub auto-deploy.

This directly informs how [[wih-app]], [[wih-ai-service]], and the [[ai-operating-system]] get built.

## Related pages
- [[boris-cherny]]
- [[information-moat]]
- [[ai-operating-system]]
- [[wih-app]]
- [[supabase]]
- [[railway]]
- [[ghl]]
- [[source-claude-code-creator-starts-project]]
- [[source-bi-dashboard-claude]]
