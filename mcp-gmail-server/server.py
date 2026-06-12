import os
import json
import base64
import hashlib
from urllib.parse import urlencode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional

import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse
from starlette.routing import Route, Mount
from google.oauth2 import service_account
from googleapiclient.discovery import build

mcp = FastMCP("gmail-mcp", stateless_http=True)

ACCOUNTS = {
    "joshua": "joshua@webberinvestmenthomes.com",
    "docs": "docs@webberinvestmenthomes.com",
}

_CLIENT_ID = os.environ.get("OAUTH_CLIENT_ID", "wih-gmail-mcp-client")
_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET", "wih-gmail-mcp-secret-2026")
_TOKEN = hashlib.sha256(f"{_CLIENT_ID}:{_CLIENT_SECRET}:wih-static".encode()).hexdigest()
_AUTH_CODE = hashlib.sha256(f"{_CLIENT_ID}:{_CLIENT_SECRET}:code".encode()).hexdigest()[:32]
_REST_KEY = os.environ.get("REST_API_KEY", "wih-rest-n8n-2026")


def get_service(account: str = "joshua"):
    email = ACCOUNTS.get(account)
    if not email:
        raise ValueError(f"Unknown account '{account}'. Use 'joshua' or 'docs'.")
    sa_info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
    creds = service_account.Credentials.from_service_account_info(
        sa_info,
        scopes=["https://mail.google.com/"],
        subject=email,
    )
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _extract_body(payload: dict) -> str:
    mime_type = payload.get("mimeType", "")
    if mime_type == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    for part in payload.get("parts", []):
        result = _extract_body(part)
        if result:
            return result
    if mime_type == "text/html":
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    return ""


# ---------------------------------------------------------------------------
# MCP tools
# ---------------------------------------------------------------------------

@mcp.tool()
def gmail_search(
    query: str,
    account: str = "joshua",
    max_results: int = 50,
    page_token: Optional[str] = None,
) -> dict:
    """
    Search Gmail using Gmail query syntax (e.g. 'in:inbox is:unread').
    account: 'joshua' or 'docs'. Paginate via next_page_token from previous response.
    """
    service = get_service(account)
    params: dict = {"userId": "me", "q": query, "maxResults": min(max_results, 500)}
    if page_token:
        params["pageToken"] = page_token

    resp = service.users().messages().list(**params).execute()

    messages = []
    for raw in resp.get("messages", []):
        msg = service.users().messages().get(
            userId="me",
            id=raw["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "To", "Date"],
        ).execute()
        hdrs = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
        label_ids = msg.get("labelIds", [])
        messages.append({
            "message_id": raw["id"],
            "thread_id": msg.get("threadId"),
            "subject": hdrs.get("Subject", "(no subject)"),
            "from": hdrs.get("From", ""),
            "to": hdrs.get("To", ""),
            "date": hdrs.get("Date", ""),
            "snippet": msg.get("snippet", ""),
            "labels": label_ids,
            "is_unread": "UNREAD" in label_ids,
        })

    return {
        "messages": messages,
        "next_page_token": resp.get("nextPageToken"),
        "total_estimate": resp.get("resultSizeEstimate", 0),
        "account_email": ACCOUNTS[account],
    }


@mcp.tool()
def gmail_get_email(message_id: str, account: str = "joshua") -> dict:
    """Get full email content including body text."""
    service = get_service(account)
    msg = service.users().messages().get(userId="me", id=message_id, format="full").execute()
    hdrs = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
    return {
        "message_id": message_id,
        "thread_id": msg.get("threadId"),
        "subject": hdrs.get("Subject", ""),
        "from": hdrs.get("From", ""),
        "to": hdrs.get("To", ""),
        "date": hdrs.get("Date", ""),
        "body": _extract_body(msg.get("payload", {})),
        "snippet": msg.get("snippet", ""),
        "labels": msg.get("labelIds", []),
        "is_unread": "UNREAD" in msg.get("labelIds", []),
    }


@mcp.tool()
def gmail_mark_as_read(message_id: str, account: str = "joshua") -> dict:
    """Mark a single email as read."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]}
    ).execute()
    return {"success": True, "message_id": message_id}


@mcp.tool()
def gmail_batch_mark_as_read(message_ids: list, account: str = "joshua") -> dict:
    """Mark multiple emails as read in one API call."""
    service = get_service(account)
    service.users().messages().batchModify(
        userId="me", body={"ids": message_ids, "removeLabelIds": ["UNREAD"]}
    ).execute()
    return {"success": True, "count": len(message_ids)}


@mcp.tool()
def gmail_add_label(message_id: str, label_id: str, account: str = "joshua") -> dict:
    """Add a label to an email. Use gmail_list_labels to find label IDs."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"addLabelIds": [label_id]}
    ).execute()
    return {"success": True, "message_id": message_id, "label_id": label_id}


@mcp.tool()
def gmail_remove_label(message_id: str, label_id: str, account: str = "joshua") -> dict:
    """Remove a label from an email."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": [label_id]}
    ).execute()
    return {"success": True, "message_id": message_id, "label_id": label_id}


@mcp.tool()
def gmail_archive(message_id: str, account: str = "joshua") -> dict:
    """Archive an email (removes from INBOX)."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": ["INBOX"]}
    ).execute()
    return {"success": True, "message_id": message_id}


@mcp.tool()
def gmail_create_label(name: str, account: str = "joshua") -> dict:
    """Create a new Gmail label. Returns label_id for use in add_label calls."""
    service = get_service(account)
    label = service.users().labels().create(
        userId="me",
        body={"name": name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
    ).execute()
    return {"label_id": label["id"], "name": label["name"]}


@mcp.tool()
def gmail_list_labels(account: str = "joshua") -> dict:
    """List all labels in the account with their IDs."""
    service = get_service(account)
    result = service.users().labels().list(userId="me").execute()
    return {
        "labels": [{"id": l["id"], "name": l["name"]} for l in result.get("labels", [])],
        "account_email": ACCOUNTS[account],
    }


@mcp.tool()
def gmail_send(
    to: str,
    subject: str,
    body: str,
    account: str = "joshua",
    thread_id: Optional[str] = None,
    html: bool = False,
) -> dict:
    """Send an email. Set thread_id to reply in an existing thread."""
    service = get_service(account)
    msg = MIMEMultipart()
    msg["to"] = to
    msg["from"] = ACCOUNTS[account]
    msg["subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    send_body: dict = {"raw": raw}
    if thread_id:
        send_body["threadId"] = thread_id
    result = service.users().messages().send(userId="me", body=send_body).execute()
    return {"success": True, "message_id": result["id"]}


@mcp.tool()
def gmail_create_draft(
    to: str,
    subject: str,
    body: str,
    account: str = "joshua",
    thread_id: Optional[str] = None,
) -> dict:
    """Create a draft email. Set thread_id to draft a reply in an existing thread."""
    service = get_service(account)
    msg = MIMEText(body)
    msg["to"] = to
    msg["from"] = ACCOUNTS[account]
    msg["subject"] = subject
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    draft_body: dict = {"message": {"raw": raw}}
    if thread_id:
        draft_body["message"]["threadId"] = thread_id
    result = service.users().drafts().create(userId="me", body=draft_body).execute()
    return {"success": True, "draft_id": result["id"]}


# ---------------------------------------------------------------------------
# REST endpoints (for n8n — authenticated via X-Api-Key header)
# ---------------------------------------------------------------------------

def _check_rest_key(request: Request) -> bool:
    return request.headers.get("x-api-key", "") == _REST_KEY


async def rest_search(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        q = request.query_params.get("q", "in:inbox is:unread")
        account = request.query_params.get("account", "joshua")
        max_results = int(request.query_params.get("max", "50"))
        page_token = request.query_params.get("page_token")
        return JSONResponse(gmail_search(q, account, max_results, page_token))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_get_email(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        message_id = request.path_params["message_id"]
        account = request.query_params.get("account", "joshua")
        return JSONResponse(gmail_get_email(message_id, account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_mark_read(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await request.json()
        message_id = body["message_id"]
        account = body.get("account", "joshua")
        return JSONResponse(gmail_mark_as_read(message_id, account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_batch_mark_read(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await request.json()
        message_ids = body["message_ids"]
        account = body.get("account", "joshua")
        return JSONResponse(gmail_batch_mark_as_read(message_ids, account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_archive(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await request.json()
        message_id = body["message_id"]
        account = body.get("account", "joshua")
        return JSONResponse(gmail_archive(message_id, account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


def _resolve_label_id(service, label_name: str) -> str:
    """Find a label ID by name, creating the label if it doesn't exist."""
    result = service.users().labels().list(userId="me").execute()
    for lbl in result.get("labels", []):
        if lbl["name"].lower() == label_name.lower():
            return lbl["id"]
    new_lbl = service.users().labels().create(
        userId="me",
        body={"name": label_name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
    ).execute()
    return new_lbl["id"]


async def rest_label(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await request.json()
        message_id = body["message_id"]
        action = body.get("action", "add")
        account = body.get("account", "joshua")
        label_id = body.get("label_id")
        label_name = body.get("label_name")
        if not label_id and label_name:
            service = get_service(account)
            label_id = _resolve_label_id(service, label_name)
        if not label_id:
            return JSONResponse({"error": "label_id or label_name required"}, status_code=400)
        if action == "remove":
            return JSONResponse(gmail_remove_label(message_id, label_id, account))
        return JSONResponse(gmail_add_label(message_id, label_id, account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_list_labels(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        account = request.query_params.get("account", "joshua")
        return JSONResponse(gmail_list_labels(account))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_send(request: Request) -> JSONResponse:
    if not _check_rest_key(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await request.json()
        return JSONResponse(gmail_send(
            to=body["to"],
            subject=body["subject"],
            body=body["body"],
            account=body.get("account", "joshua"),
            thread_id=body.get("thread_id"),
            html=body.get("html", False),
        ))
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def rest_health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


# ---------------------------------------------------------------------------
# OAuth middleware (MCP paths only — /api/* use X-Api-Key instead)
# ---------------------------------------------------------------------------

class OAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # REST API paths — handled by their own key check inside each handler
        if path.startswith("/api/"):
            return await call_next(request)

        # Health check — always open
        if path == "/health":
            return await call_next(request)

        # OAuth discovery
        if path == "/.well-known/oauth-authorization-server":
            base = str(request.base_url).rstrip("/")
            return JSONResponse({
                "issuer": base,
                "authorization_endpoint": f"{base}/authorize",
                "token_endpoint": f"{base}/oauth/token",
                "response_types_supported": ["code"],
                "grant_types_supported": ["authorization_code", "client_credentials"],
                "token_endpoint_auth_methods_supported": [
                    "client_secret_post",
                    "client_secret_basic",
                    "none",
                ],
                "code_challenge_methods_supported": ["S256"],
            })

        # Authorization endpoint — auto-approves and redirects back with a code
        if path == "/authorize":
            redirect_uri = request.query_params.get("redirect_uri", "")
            state = request.query_params.get("state", "")
            if not redirect_uri:
                return JSONResponse({"error": "missing_redirect_uri"}, status_code=400)
            sep = "&" if "?" in redirect_uri else "?"
            params = urlencode({"code": _AUTH_CODE, "state": state})
            return RedirectResponse(url=f"{redirect_uri}{sep}{params}", status_code=302)

        # Token endpoint — exchanges auth code or client credentials for a Bearer token
        if path == "/oauth/token":
            form = await request.form()
            grant_type = form.get("grant_type", "")

            if grant_type == "authorization_code":
                code = form.get("code", "")
                if code == _AUTH_CODE:
                    return JSONResponse({
                        "access_token": _TOKEN,
                        "token_type": "bearer",
                        "expires_in": 31_536_000,
                    })
                return JSONResponse({"error": "invalid_grant"}, status_code=401)

            client_id = form.get("client_id", "")
            client_secret = form.get("client_secret", "")
            auth_hdr = request.headers.get("authorization", "")
            if auth_hdr.startswith("Basic "):
                try:
                    decoded = base64.b64decode(auth_hdr[6:]).decode()
                    if ":" in decoded:
                        client_id, client_secret = decoded.split(":", 1)
                except Exception:
                    pass

            if client_id == _CLIENT_ID and client_secret == _CLIENT_SECRET:
                return JSONResponse({
                    "access_token": _TOKEN,
                    "token_type": "bearer",
                    "expires_in": 31_536_000,
                })
            return JSONResponse({"error": "invalid_client"}, status_code=401)

        # All MCP calls must carry the Bearer token
        auth = request.headers.get("authorization", "")
        if not (auth.startswith("Bearer ") and auth[7:] == _TOKEN):
            return JSONResponse(
                {"error": "unauthorized"},
                status_code=401,
                headers={"WWW-Authenticate": "Bearer"},
            )

        return await call_next(request)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    rest_routes = [
        Route("/api/search", rest_search, methods=["GET"]),
        Route("/api/email/{message_id}", rest_get_email, methods=["GET"]),
        Route("/api/mark-read", rest_mark_read, methods=["POST"]),
        Route("/api/batch-mark-read", rest_batch_mark_read, methods=["POST"]),
        Route("/api/archive", rest_archive, methods=["POST"]),
        Route("/api/label", rest_label, methods=["POST"]),
        Route("/api/labels", rest_list_labels, methods=["GET"]),
        Route("/api/send", rest_send, methods=["POST"]),
        Route("/health", rest_health, methods=["GET"]),
    ]

    mcp_app = mcp.streamable_http_app()

    app = Starlette(routes=rest_routes + list(mcp_app.routes))
    app.add_middleware(OAuthMiddleware)

    uvicorn.run(app, host="0.0.0.0", port=port)
