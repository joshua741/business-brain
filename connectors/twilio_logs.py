#!/usr/bin/env python3
"""Twilio connector -> masked daily SMS log snapshot in raw/.

Pulls recent Twilio messages via the REST API, summarizes direction/number/status
and recent threads, masks (phone numbers + tokens), writes raw/twilio-sms-log-DATE.md.
Reads creds from env or vault/.wih-app .env. Self-skips (exit 0) if creds absent.
Read-only: only GET. Auth uses API Key + Secret over the account SID.

Creds: TWILIO_ACCOUNT_SID + TWILIO_API_KEY + TWILIO_API_SECRET
       (optional context: TWILIO_OUTREACH_NUMBER, TWILIO_SELLER_NUMBER)
"""
import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
PAGE_SIZE = 200
MAX_RECENT = 25
BODY_CHARS = 120

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text


def load_creds() -> dict:
    import os
    creds = dict(os.environ)
    for envfile in (REPO / ".env", Path(r"C:\Users\joshu\wih-app\.env")):
        if envfile.exists():
            for line in envfile.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    creds.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    return creds


def api_get(url: str, auth: str) -> dict:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Basic {auth}",
        "Accept": "application/json",
        "User-Agent": "BusinessBrain-Connector/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_report(messages, numbers):
    d = datetime.now().strftime("%Y-%m-%d")
    inbound = sum(1 for m in messages if (m.get("direction") or "").startswith("inbound"))
    outbound = len(messages) - inbound
    # activity per counterparty number (the non-Twilio side)
    own = set(filter(None, numbers))
    by_party = {}
    for m in messages:
        party = m.get("from") if (m.get("direction") or "").startswith("inbound") else m.get("to")
        by_party[party] = by_party.get(party, 0) + 1

    out = [
        "---",
        f"name: source-twilio-sms-log-{d}",
        "type: source",
        "tags: [twilio, sms, crm, snapshot]",
        f"sources: [twilio-sms-log-{d}.md]",
        f"updated: {d}",
        "---",
        f"# Twilio SMS Log -- {d}",
        "",
        f"**Summary**: Recent Twilio SMS activity -- {len(messages)} messages "
        f"({inbound} inbound, {outbound} outbound) across {len(by_party)} counterparties.",
        "",
        f"**Sources**: twilio-sms-log-{d}.md (Twilio REST API, read-only)",
        "",
        f"**Last updated**: {d}",
        "",
        "---",
        "",
        f"Business numbers: {', '.join(own) if own else 'n/a'}.",
        "",
        "## Top counterparties (by message count)",
        "| Number | Messages |",
        "|---|---|",
    ]
    for num, cnt in sorted(by_party.items(), key=lambda kv: kv[1], reverse=True)[:15]:
        out.append(f"| {num} | {cnt} |")

    out += ["", "## Recent messages", "| Date | Dir | From | To | Status | Body |", "|---|---|---|---|---|---|"]
    for m in messages[:MAX_RECENT]:
        body = (m.get("body") or "").replace("|", "\\|").replace("\n", " ")[:BODY_CHARS]
        date = (m.get("date_created") or "")[:16]
        direc = "in" if (m.get("direction") or "").startswith("inbound") else "out"
        out.append(f"| {date} | {direc} | {m.get('from','')} | {m.get('to','')} | "
                   f"{m.get('status','')} | {body} |")

    out += ["", "## Related pages", "- [[twilio]]", "- [[ghl]]", "- [[vince-ai]]", "- [[wih-app]]", ""]
    return mask_text("\n".join(out))


def main() -> int:
    c = load_creds()
    sid = c.get("TWILIO_ACCOUNT_SID")
    key = c.get("TWILIO_API_KEY")
    sec = c.get("TWILIO_API_SECRET")
    if not (sid and key and sec):
        print("twilio connector: TWILIO_ACCOUNT_SID/API_KEY/API_SECRET not set -- skipping (no error).")
        return 0
    auth = base64.b64encode(f"{key}:{sec}".encode()).decode()
    url = (f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json?"
           + urllib.parse.urlencode({"PageSize": PAGE_SIZE}))
    try:
        data = api_get(url, auth)
    except urllib.error.HTTPError as e:
        print(f"twilio connector: HTTP {e.code} ({e.reason}); skipping. Check API key/secret.")
        return 0
    except Exception as e:
        print(f"twilio connector: error ({type(e).__name__}: {e}); skipping.")
        return 0

    messages = data.get("messages", [])
    numbers = [c.get("TWILIO_OUTREACH_NUMBER"), c.get("TWILIO_SELLER_NUMBER")]
    d = datetime.now().strftime("%Y-%m-%d")
    target = RAW / f"twilio-sms-log-{d}.md"
    RAW.mkdir(parents=True, exist_ok=True)
    target.write_text(build_report(messages, numbers) + "\n", encoding="utf-8")
    print(f"twilio connector: wrote raw/{target.name} ({len(messages)} messages).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
