#!/usr/bin/env python3
"""Shared Google ADC token helper for the Google connectors.

Uses Application Default Credentials (set via `gcloud auth application-default
login`). Returns a bearer access token or None if ADC/scopes aren't available
(so callers can self-skip). Read-only scopes by default.
"""
SCOPES_RO = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
]


def get_token(scopes=None):
    scopes = scopes or SCOPES_RO
    try:
        import google.auth
        from google.auth.transport.requests import Request
        creds, _ = google.auth.default(scopes=scopes)
        creds.refresh(Request())
        return creds.token
    except Exception:
        return None
