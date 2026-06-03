#!/usr/bin/env python3
"""Mercury connector -> masked daily snapshot (READ-ONLY insight side).

Pulls accounts (balances) and recent transactions, summarizes the Profit First
view + recent activity, masks (account/routing numbers, tokens), writes
raw/mercury-snapshot-DATE.md. Self-skips (exit 0) if MERCURY_API_TOKEN absent.

IMPORTANT: this connector only issues GET requests. Any money-moving / invoicing
action is intentionally NOT here -- those will live in a separate, approval-gated
tool so nothing can move funds autonomously.
"""
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
BASE = "https://api.mercury.com/api/v1"
TXNS_PER_ACCT = 15

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text


def load_token():
    import os
    for src in (REPO / ".env", Path(r"C:\Users\joshu\wih-app\.env")):
        if src.exists():
            for line in src.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.startswith("MERCURY_API_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("MERCURY_API_TOKEN")


def api(path, token):
    req = urllib.request.Request(BASE + path, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "BusinessBrain-Connector/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def money(v):
    try:
        return f"${float(v):,.2f}"
    except (TypeError, ValueError):
        return str(v)


def main() -> int:
    token = load_token()
    if not token:
        print("mercury connector: MERCURY_API_TOKEN not set -- skipping (no error).")
        return 0
    try:
        accts = api("/accounts", token).get("accounts", [])
    except urllib.error.HTTPError as e:
        print(f"mercury connector: HTTP {e.code} ({e.reason}); skipping.")
        return 0
    except Exception as e:
        print(f"mercury connector: error ({type(e).__name__}: {e}); skipping.")
        return 0

    d = datetime.now().strftime("%Y-%m-%d")
    total = 0.0
    for a in accts:
        try:
            total += float(a.get("currentBalance", a.get("availableBalance", 0)) or 0)
        except (TypeError, ValueError):
            pass

    out = [
        "---",
        f"name: source-mercury-snapshot-{d}",
        "type: source",
        "tags: [mercury, banking, finance, profit-first, snapshot]",
        f"sources: [mercury-snapshot-{d}.md]",
        f"updated: {d}",
        "---",
        f"# Mercury Snapshot -- {d}",
        "",
        f"**Summary**: Read-only Mercury snapshot -- {len(accts)} accounts, "
        f"total balance {money(total)}.",
        "",
        f"**Sources**: mercury-snapshot-{d}.md (Mercury API, read-only)",
        "",
        f"**Last updated**: {d}",
        "",
        "---",
        "",
        "## Accounts (Profit First view)",
        "| Account | Type | Available | Current |",
        "|---|---|---|---|",
    ]
    for a in accts:
        out.append(f"| {a.get('name','')} | {a.get('type','')} | "
                   f"{money(a.get('availableBalance'))} | {money(a.get('currentBalance'))} |")

    out += ["", "## Recent transactions"]
    for a in accts:
        aid = a.get("id")
        if not aid:
            continue
        try:
            txns = api(f"/account/{aid}/transactions?limit={TXNS_PER_ACCT}&offset=0", token).get("transactions", [])
        except Exception:
            continue
        out.append(f"\n### {a.get('name','')}")
        if not txns:
            out.append("_no recent transactions_")
            continue
        out.append("| Date | Amount | Counterparty | Kind | Status |")
        out.append("|---|---|---|---|---|")
        for t in txns:
            date = (t.get("createdAt") or t.get("postedAt") or "")[:10]
            cp = (t.get("counterpartyName") or "").replace("|", "\\|")
            out.append(f"| {date} | {money(t.get('amount'))} | {cp} | "
                       f"{t.get('kind','')} | {t.get('status','')} |")

    out += ["", "## Related pages", "- [[mercury]]", "- [[profit-first]]", "- [[wih]]", "- [[baselane-to-mercury-migration]]", ""]
    target = RAW / f"mercury-snapshot-{d}.md"
    RAW.mkdir(parents=True, exist_ok=True)
    target.write_text(mask_text("\n".join(out)) + "\n", encoding="utf-8")
    print(f"mercury connector: wrote raw/{target.name} ({len(accts)} accounts).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
