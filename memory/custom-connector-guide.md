# Custom Connectors — Canonical Reference

**Type**: HOW to work (behavioral rule + resource pointer)
**Durability**: Permanent — reference this before building any custom connector
**Created**: 2026-06-11

---

## Rule

**When building a custom connector (remote MCP), always refer to this guide first:**

https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp

Do not proceed from general knowledge about OAuth or MCP. Use the official guide as the source of truth for steps, redirect URIs, required fields, and configuration format.

## Why This Exists

The built-in connectors in claude.ai (e.g. Gmail) have platform-level restrictions — write and delete tools may be locked or require approval. Custom connectors using your own OAuth credentials bypass those restrictions and give full control over scopes.

Discovered 2026-06-11 while trying to unlock Gmail write/delete operations for the email management skill. The built-in Gmail connector has "locked" icons on write/delete permissions — not fixable through the UI. The solution is a custom OAuth app (Google Cloud project with client ID + client secret) registered as a custom connector.

## When to Use a Custom Connector

- A built-in connector has write/delete operations locked or approval-gated
- You need full scope control over an OAuth integration
- You need two instances of the same service (e.g. two Gmail accounts — one per custom connector)
- A service isn't available as a built-in connector

## General Flow (always verify against the guide above)

1. Open the canonical guide URL above before starting
2. In claude.ai Connectors panel → add custom connector → note the redirect URI it provides
3. Create OAuth app in the service's developer console (e.g. Google Cloud Console)
4. Register the redirect URI from claude.ai in the OAuth app
5. Copy the client ID and client secret
6. Enter both into the claude.ai custom connector dialog
7. Complete the OAuth authorization flow — select the correct account and grant all needed scopes

## Applied To

- Gmail (`joshua@webberinvestmenthomes.com`) — custom connector needed for full write/delete/archive access
- Gmail (`docs@webberinvestmenthomes.com`) — second connector needed (same custom OAuth app, different account)
