# Gmail MCP Server — Setup Guide

No browser OAuth flows. One service account impersonates both Gmail accounts forever.

---

## Step 1 — Google Cloud: Create Service Account

1. Go to console.cloud.google.com → your **gmail-mcp** project
2. **APIs & Services → Library** → search "Gmail API" → Enable it
3. **IAM & Admin → Service Accounts** → Create Service Account
   - Name: `gmail-mcp`
   - Click Create and Continue → skip role assignment → Done
4. Click the service account → **Keys** tab → **Add Key → Create new key → JSON**
5. Download the JSON key file — keep it safe, never commit it

---

## Step 2 — Google Workspace Admin: Enable Domain-Wide Delegation

1. Go to **admin.google.com** (you must be the Workspace admin)
2. **Security → Access and data control → API controls**
3. Click **Manage Domain-Wide Delegation**
4. Click **Add new**
   - **Client ID**: copy the `client_id` field from the JSON key file
   - **OAuth Scopes**: `https://mail.google.com/`
5. Click Authorize

This lets the service account impersonate any email on webberinvestmenthomes.com.

---

## Step 3 — Railway: Deploy and Set Environment Variables

1. Go to railway.app → New Project → Deploy from GitHub
2. Select `joshua741/business-brain` repo
3. Set **Root Directory** to `mcp-gmail-server`
4. Add these environment variables:
   - `GOOGLE_SERVICE_ACCOUNT_JSON` = paste the entire contents of the JSON key file
   - `MCP_API_KEY` = generate a strong random string (e.g. 32+ chars) — this secures the endpoint

5. Deploy. Once live, copy the Railway public URL (e.g. `https://gmail-mcp-production.up.railway.app`)

---

## Step 4 — Claude.ai: Add Custom Connector

1. Go to claude.ai → Customize → Connectors
2. (Team plan) Organization Settings → Connectors → Add → Custom → Web
3. MCP Server URL: `https://your-railway-url.railway.app/mcp`
4. Advanced Settings → set the API key header if needed (or pass via URL)
5. Add connector

---

## Environment Variables Reference

| Variable | Description |
|---|---|
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Full contents of the service account JSON key file |
| `MCP_API_KEY` | Random secret that secures the MCP endpoint |
| `PORT` | Set automatically by Railway |

---

## Why Service Account (not OAuth)

- OAuth refresh tokens in Testing mode expire after 7 days → weekly breakage
- Service accounts have no expiry — rotate only if the key is compromised
- One service account covers all emails on the domain (joshua@, docs@, any future address)
- No browser login flow needed for setup or renewal
