---
name: wih-app
type: project
tags: [web-app, railway, supabase]
status: active
sources: [CLAUDE.md seed, memo-2026-05-29T14-03-38-session.md]
updated: 2026-06-03
---

# WIH App

**Summary**: Main WIH web application. Deployed on Railway with Supabase backend.

**Sources**: CLAUDE.md seed

**Last updated**: 2026-05-28

---

The primary web application for [[wih]]. Deployed on [[railway]] with [[supabase]] as the PostgreSQL backend. AI capabilities provided by [[wih-ai-service]].

## Deployment facts (source: memo-2026-05-29T14-03-38-session.md)
- **Railway project:** `terrific-blessing` = wih-app
- **Live URL:** https://web-production-bcdba.up.railway.app
- **Stack:** React/Vite frontend (`client/`) + Node backend (`src/server.ts`) + Postgres
- **Local code:** `C:\Users\joshu\wih-app`
- **GitHub:** `github.com/joshua741/wih-app` — pushes to `origin` auto-deploy to Railway
- Note: wih-app-specific working context lives in the `C--Users-joshu-wih-app` project memory, not this wiki.

## Related pages
- [[wih]]
- [[railway]]
- [[supabase]]
- [[wih-ai-service]]
