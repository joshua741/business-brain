"""Simulate a month of deposits through a Mercury auto-transfer ruleset.

Used to prove the Mercury rules reproduce exactly what Sequence does today
(Phase 2 / Task 13): feed a month's deposits + the rule map, compare the
resulting balances to the real Baselane statement.

Rule semantics (matching Mercury):
  - "percent": moves a percentage of the INCOMING funds to that source
    (not the running balance) — so 15% + 5% of a $1,000 deposit = $150 + $50,
    leaving $800, regardless of rule order.
  - "fixed": moves a fixed amount, capped at the available balance.
"""


def apply_rules(deposits, rules):
    balances = {}
    deposited = {}
    for d in deposits:
        balances[d["account"]] = balances.get(d["account"], 0) + d["amount"]
        deposited[d["account"]] = deposited.get(d["account"], 0) + d["amount"]

    for r in rules:
        src = r["source"]
        available = balances.get(src, 0)
        if available <= 0:
            continue
        if r["type"] == "percent":
            moved = deposited.get(src, 0) * (r["amount"] / 100)
        else:  # fixed
            moved = r["amount"]
        moved = min(moved, available)
        balances[src] = available - moved
        balances[r["dest"]] = balances.get(r["dest"], 0) + moved

    return balances
