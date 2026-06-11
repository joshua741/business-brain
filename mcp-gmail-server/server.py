import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional

from mcp.server.fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

mcp = FastMCP("gmail-mcp", stateless_http=True)

GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]

ACCOUNTS = {
    "joshua": {
        "email": "joshua@webberinvestmenthomes.com",
        "refresh_token": os.environ.get("JOSHUA_GMAIL_REFRESH_TOKEN", ""),
    },
    "docs": {
        "email": "docs@webberinvestmenthomes.com",
        "refresh_token": os.environ.get("DOCS_GMAIL_REFRESH_TOKEN", ""),
    },
}


def get_service(account: str = "joshua"):
    acct = ACCOUNTS.get(account)
    if not acct or not acct["refresh_token"]:
        raise ValueError(f"No refresh token configured for account '{account}'")
    creds = Credentials(
        token=None,
        refresh_token=acct["refresh_token"],
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://mail.google.com/"],
    )
    creds.refresh(Request())
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
    # Fallback: HTML body if no plain text found
    if mime_type == "text/html":
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    return ""


@mcp.tool()
def gmail_search(
    query: str,
    account: str = "joshua",
    max_results: int = 50,
    page_token: Optional[str] = None,
) -> dict:
    """
    Search Gmail using Gmail query syntax (e.g. 'in:inbox is:unread', 'from:someone@email.com').
    account: 'joshua' or 'docs'. Supports pagination via page_token from previous response.
    Returns message metadata + next_page_token for looping through all results.
    """
    service = get_service(account)
    params = {"userId": "me", "q": query, "maxResults": min(max_results, 500)}
    if page_token:
        params["pageToken"] = page_token

    resp = service.users().messages().list(**params).execute()
    raw_ids = resp.get("messages", [])

    messages = []
    for raw in raw_ids:
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
        "account_email": ACCOUNTS[account]["email"],
    }


@mcp.tool()
def gmail_get_email(message_id: str, account: str = "joshua") -> dict:
    """Get the full content of an email including body text."""
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
    """Mark a single email as read (removes UNREAD label)."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]}
    ).execute()
    return {"success": True, "message_id": message_id}


@mcp.tool()
def gmail_batch_mark_as_read(message_ids: list, account: str = "joshua") -> dict:
    """Mark multiple emails as read in a single API call. Pass a list of message_ids."""
    service = get_service(account)
    service.users().messages().batchModify(
        userId="me", body={"ids": message_ids, "removeLabelIds": ["UNREAD"]}
    ).execute()
    return {"success": True, "count": len(message_ids)}


@mcp.tool()
def gmail_add_label(message_id: str, label_id: str, account: str = "joshua") -> dict:
    """Add a label to an email. label_id can be a custom label ID or a system label like IMPORTANT."""
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
    """Archive an email by removing it from INBOX."""
    service = get_service(account)
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": ["INBOX"]}
    ).execute()
    return {"success": True, "message_id": message_id}


@mcp.tool()
def gmail_create_label(name: str, account: str = "joshua") -> dict:
    """Create a new Gmail label. Returns the label_id to use in add_label calls."""
    service = get_service(account)
    label = service.users().labels().create(
        userId="me",
        body={
            "name": name,
            "labelListVisibility": "labelShow",
            "messageListVisibility": "show",
        },
    ).execute()
    return {"label_id": label["id"], "name": label["name"]}


@mcp.tool()
def gmail_list_labels(account: str = "joshua") -> dict:
    """List all labels in the Gmail account. Use this to find label IDs before applying them."""
    service = get_service(account)
    result = service.users().labels().list(userId="me").execute()
    return {
        "labels": [{"id": l["id"], "name": l["name"]} for l in result.get("labels", [])],
        "account_email": ACCOUNTS[account]["email"],
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
    msg["from"] = ACCOUNTS[account]["email"]
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
    """Create a draft email. Set thread_id to create a draft reply in an existing thread."""
    service = get_service(account)
    msg = MIMEText(body)
    msg["to"] = to
    msg["from"] = ACCOUNTS[account]["email"]
    msg["subject"] = subject

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    draft_body: dict = {"message": {"raw": raw}}
    if thread_id:
        draft_body["message"]["threadId"] = thread_id

    result = service.users().drafts().create(userId="me", body=draft_body).execute()
    return {"success": True, "draft_id": result["id"]}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
