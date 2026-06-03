#!/usr/bin/env python3
"""GHL (GoHighLevel) connector -> masked daily snapshot in raw/.

Pulls pipelines, opportunities (aggregated into a funnel), and a contacts summary
via GHL API v2, then writes raw/ghl-snapshot-YYYY-MM-DD.md (masked). Reads creds
from env or a gitignored vault .env. Self-skips (exit 0) if creds are absent so the
daily pipeline never breaks. Read-only: only GET requests.

Required creds (in Documents\\Business_Brain\\.env or environment):
  GHL_API_TOKEN   = a GHL Private Integration Token (Settings -> Private Integrations)
  GHL_LOCATION_ID = the sub-account / location id
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
BASE = "https://services.leadconnectorhq.com"
VERSION = "2021-07-28"
MAX_OPP_PAGES = 5      # 100 opportunities per page
MAX_RECENT = 20

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text


def load_creds() -> dict:
    """Merge env + vault .env + wih-app/.env (later sources do not override earlier)."""
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


def api_get(path: str, token: str, params: dict) -> dict:
    url = f"{BASE}{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Version": VERSION,
        "Accept": "application/json",
        # GHL sits behind Cloudflare, which blocks the default Python-urllib UA (error 1010).
        "User-Agent": "BusinessBrain-Connector/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_pipelines(token, loc):
    data = api_get("/opportunities/pipelines", token, {"locationId": loc})
    return data.get("pipelines", [])


def fetch_opportunities(token, loc):
    opps, page = [], 0
    params = {"location_id": loc, "limit": 100}
    while page < MAX_OPP_PAGES:
        data = api_get("/opportunities/search", token, params)
        batch = data.get("opportunities", [])
        opps.extend(batch)
        meta = data.get("meta", {})
        after, after_id = meta.get("startAfter"), meta.get("startAfterId")
        if not batch or not after_id:
            break
        params["startAfter"], params["startAfterId"] = after, after_id
        page += 1
    return opps, (page + 1 >= MAX_OPP_PAGES)


def contacts_total(token, loc):
    data = api_get("/contacts/", token, {"locationId": loc, "limit": 1})
    return data.get("meta", {}).get("total")


def build_report(pipelines, opps, capped, c_total):
    stage_names = {}
    for p in pipelines:
        for s in p.get("stages", []):
            stage_names[s.get("id")] = (p.get("name"), s.get("name"))

    # funnel: count + $ per pipeline/stage
    funnel = {}
    for o in opps:
        sid = o.get("pipelineStageId")
        pname, sname = stage_names.get(sid, (o.get("pipelineId", "?"), "?"))
        key = (pname, sname)
        agg = funnel.setdefault(key, {"count": 0, "value": 0.0})
        agg["count"] += 1
        try:
            agg["value"] += float(o.get("monetaryValue") or 0)
        except (TypeError, ValueError):
            pass

    d = datetime.now().strftime("%Y-%m-%d")
    out = [
        "---",
        f"name: source-ghl-snapshot-{d}",
        "type: source",
        "tags: [ghl, crm, snapshot, pipeline]",
        f"sources: [ghl-snapshot-{d}.md]",
        f"updated: {d}",
        "---",
        f"# GHL Snapshot -- {d}",
        "",
        f"**Summary**: Daily GoHighLevel snapshot -- {len(opps)} opportunities across "
        f"{len(pipelines)} pipelines"
        + (f"; {c_total} total contacts" if c_total is not None else "") + ".",
        "",
        f"**Sources**: ghl-snapshot-{d}.md (GHL API v2, read-only)",
        "",
        f"**Last updated**: {d}",
        "",
        "---",
        "",
        "## Pipeline funnel (count / $ value by stage)",
    ]
    if funnel:
        out.append("| Pipeline | Stage | Opportunities | Value |")
        out.append("|---|---|---|---|")
        for (pname, sname), agg in sorted(funnel.items()):
            out.append(f"| {pname} | {sname} | {agg['count']} | ${agg['value']:,.0f} |")
    else:
        out.append("_No opportunities found._")
    if capped:
        out.append(f"\n*(opportunity pull capped at {MAX_OPP_PAGES * 100}; totals may understate.)*")

    out += ["", "## Recent opportunities"]
    recent = sorted(opps, key=lambda o: o.get("updatedAt") or "", reverse=True)[:MAX_RECENT]
    if recent:
        out.append("| Name | Stage | Status | Value | Updated |")
        out.append("|---|---|---|---|---|")
        for o in recent:
            sid = o.get("pipelineStageId")
            _, sname = stage_names.get(sid, ("?", "?"))
            name = (o.get("name") or "").replace("|", "\\|")
            val = o.get("monetaryValue") or 0
            upd = (o.get("updatedAt") or "")[:10]
            out.append(f"| {name} | {sname} | {o.get('status','')} | ${val} | {upd} |")
    else:
        out.append("_None._")

    out += ["", "## Related pages", "- [[ghl]]", "- [[wih-app]]", "- [[wholesale]]", "- [[vince-ai]]", ""]
    return mask_text("\n".join(out))


def main() -> int:
    creds = load_creds()
    token = creds.get("GHL_API_TOKEN") or creds.get("GHL_API_KEY")
    loc = creds.get("GHL_LOCATION_ID")
    if not token or not loc:
        print("ghl connector: GHL_API_TOKEN / GHL_LOCATION_ID not set -- skipping (no error).")
        return 0
    try:
        pipelines = fetch_pipelines(token, loc)
        opps, capped = fetch_opportunities(token, loc)
        c_total = contacts_total(token, loc)
    except urllib.error.HTTPError as e:
        print(f"ghl connector: HTTP {e.code} from GHL ({e.reason}); skipping. "
              f"Check token scopes/location id.")
        return 0
    except Exception as e:
        print(f"ghl connector: error ({type(e).__name__}: {e}); skipping.")
        return 0

    d = datetime.now().strftime("%Y-%m-%d")
    target = RAW / f"ghl-snapshot-{d}.md"
    RAW.mkdir(parents=True, exist_ok=True)
    target.write_text(build_report(pipelines, opps, capped, c_total) + "\n", encoding="utf-8")
    print(f"ghl connector: wrote raw/{target.name} "
          f"({len(opps)} opps, {len(pipelines)} pipelines).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
