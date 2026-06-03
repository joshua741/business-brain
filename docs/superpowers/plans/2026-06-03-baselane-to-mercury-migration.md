# Baselane → Mercury Migration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move banking and money-routing off Baselane (Thread Bank) + Sequence onto Mercury, with DoorLoop as the rent rail, so AI becomes the money-mover via Mercury's payment API/MCP — without moving real funds until the system is fully vetted.

**Architecture:** Two layers. (1) **Internal allocation** — recreate the per-property Profit First sub-accounts in Mercury under one partner bank; boring native auto-transfer rules do the splits. (2) **External disbursement** — the money that must leave sweeps into a single dedicated **hub account** that holds all external recipients and the scoped write key; the AI layer pushes payments from the hub via Mercury's payment API, dry-run-gated and allowlisted, with per-payment memos preserving per-property attribution. Build and vet both layers (including outbound payments) before any cutover. Baselane is kept afterward only as a read-only bookkeeping layer.

**Tech Stack:** Mercury (banking + auto-transfer rules + payment API + MCP server), DoorLoop (rent collection), Baselane/Thread Bank (legacy + future read-only books), Python 3 (validation, payment-proposal, reconciliation scripts), the wih-ai-service / Claude layer for money-ops.

**Spec:** `docs/superpowers/specs/2026-06-03-baselane-to-mercury-migration-design.md`

**Owner legend:** 🤖 = Claude can do it from data/API · 🧍 = Joshua/Mostafa only (login, KYC, money movement) · 🤝 = both (Claude drafts, human executes)

**HARD RULE:** No real funds move before Phase 3 (Task 16). Tasks 1–15 are build-and-vet only.

---

## Working artifacts (created by this plan)

- `docs/migration/account-tree.md` — every current Baselane account, balance, purpose, flows
- `docs/migration/sequence-rules.md` — every Sequence rule, tagged internal-move vs external-push
- `docs/migration/repoint-checklist.md` — payers-in, push-payees (hub), pull-merchants (card)
- `docs/migration/mercury-account-map.md` — target Mercury accounts + hub + rule + recipient mapping
- `scripts/migration/validate_rules.py` — simulates a month of internal splits vs the Sequence ruleset
- `scripts/migration/payments.py` — builds the allowlisted payment set + dry-run-gated send path
- `scripts/migration/reconcile.py` — reconciles live Mercury balances against expected

---

# Phase 0 — Inventory (zero money moves)

### Task 1: Build the current Baselane account tree 🤖

**Files:** Create `docs/migration/account-tree.md`; Read `raw/baselane-*-statement.md`, `wiki/source-baselane-statements.md`

- [ ] **Step 1:** Read every `raw/baselane-*-statement.md` and `wiki/source-baselane-statements.md`.
- [ ] **Step 2:** Write `account-tree.md` as a table: account name, last-4, entity (WWH / W&M Series), type (main / property-bank / taxes / rehab-funds / series-marketing), property, latest known balance + statement month, recurring in/out (e.g. 1312 65th Dr → in: HAOL HCV $970; out: $2,310.94 to Dillon Ford).
- [ ] **Step 3 (verify):** Every property in `CLAUDE.md` "Current Property Portfolio" appears; every account named in the statements is listed. Note any property with no Baselane account found.
- [ ] **Step 4 (commit):** `git add docs/migration/account-tree.md && git commit -m "docs(migration): map current Baselane account tree"`

### Task 2: Export the Sequence ruleset, tagged internal vs external 🤝

**Files:** Create `docs/migration/sequence-rules.md`

- [ ] **Step 1 (🧍 Joshua):** Log into getsequence.io. For each workflow capture: trigger, each action (fixed/%), source, destination, schedule, and **whether the destination is one of your own accounts (internal move) or a third party (external push)**. Drop exports/screenshots into `drop/` or paste details to Claude.
- [ ] **Step 2 (🤖):** Write `sequence-rules.md` — one row per rule with an `internal | external-push` tag. Cross-check against the "Webber Wealth Ho Sequence" lines in the statements.
- [ ] **Step 3 (verify):** Every property mortgage/seller-finance payment seen in statements (e.g. 1312 → Dillon Ford $2,310.94) maps to a rule, correctly tagged. List any payment with no matching rule.
- [ ] **Step 4 (commit):** `git add docs/migration/sequence-rules.md && git commit -m "docs(migration): capture Sequence ruleset (internal vs external)"`

### Task 3: Build the repoint checklist (3 buckets) 🤖

**Files:** Create `docs/migration/repoint-checklist.md`; Read account-tree.md, sequence-rules.md, statements

- [ ] **Step 1 — payers-in:** housing authorities (HAOL HCV / Section 8), DoorLoop tenant deposits, Stripe, P2P. For each: account it hits today + what changes (new Mercury account/routing # to provide).
- [ ] **Step 2 — push-payees (→ hub):** Dillon Ford (seller-finance, CRITICAL), Kiavi draws, contractors (Shelby McDonald / 33 Carpentry), title companies. For each: amount/cadence, which property it belongs to, current source account.
- [ ] **Step 3 — pull-merchants (→ Mercury card, NOT the hub):** GHL, Zapier, Twilio, DoorLoop, Lovable, PropStream/BatchLeads, Skool, GoDaddy, etc. These charge a card; they only need a Mercury debit card on file.
- [ ] **Step 4 (verify):** Every recurring debit in the latest main-account statement lands in exactly one bucket. Every external-push Sequence rule maps to a push-payee row.
- [ ] **Step 5 (commit):** `git add docs/migration/repoint-checklist.md && git commit -m "docs(migration): repoint checklist (payers / push / pull)"`

### Task 4: Export Baselane bookkeeping history 🧍

- [ ] **Step 1:** In Baselane, export full transaction history + bookkeeping categories + Schedule E reports for all accounts (CSV + PDF).
- [ ] **Step 2:** Store in the Business Brain backup location. Confirm it opens and covers 2025 + 2026 YTD.
- [ ] **Step 3 (verify):** Spot-check the export's account balances against `account-tree.md`. This is the safety net before anything changes.

---

# Phase 1 — Build the Mercury shell + payment layer (zero money moves)

### Task 5: Confirm Mercury constraints (partner bank, recipient + token scope) 🤝

**Files:** Create `docs/migration/mercury-account-map.md` (start it here)

- [ ] **Step 1 (🤖):** From Mercury docs, record in the doc: sub-accounts free/unlimited; percentage auto-transfer rules (≤20 destinations, by-transaction/daily/twice-monthly); **rules only work within one partner bank**; Treasury auto-transfers capped at 2/mo ≥7 days apart.
- [ ] **Step 2 (🧍 Joshua):** Confirm with Mercury: (a) can you pin all accounts to ONE partner bank; (b) are payment **recipients org-level or per-account**; (c) can a **write token be scoped to a single account** (the hub). Record answers — they decide whether external payments fire from the hub or per-property account (logical model is identical either way).
- [ ] **Step 3 (commit):** `git add docs/migration/mercury-account-map.md && git commit -m "docs(migration): confirm Mercury constraints + scoping"`

### Task 6: Design the target Mercury account map + hub + rule map 🤖

**Files:** Modify `docs/migration/mercury-account-map.md`

- [ ] **Step 1:** Mirror `account-tree.md` into target Mercury accounts (per-property operating/taxes/rehab where they exist today, WWH main, W&M series) with clear nicknames; **add one dedicated `Disbursement Hub` account.**
- [ ] **Step 2:** Map each `internal` Sequence rule → an equivalent Mercury auto-transfer rule (source → dest(s), %/amount, schedule), plus a **sweep-to-hub** rule that funds the hub for each external obligation from the owning property account.
- [ ] **Step 3:** List each `external-push` payee from `repoint-checklist.md` as a hub recipient with its property attribution + memo string. Confirm pull-merchants are marked card-on-file (not hub).
- [ ] **Step 4 (verify):** Every Sequence rule maps to either a Mercury auto-rule, a sweep-to-hub, or a hub payment. Every account in `account-tree.md` has a target. Every external payee has a memo + property.
- [ ] **Step 5 (commit):** `git add docs/migration/mercury-account-map.md && git commit -m "docs(migration): target account map + hub + rule/recipient mapping"`

### Task 7: Create the Mercury sub-accounts + hub 🧍

- [ ] **Step 1:** In Mercury create every account from `mercury-account-map.md` (including the Disbursement Hub) with exact nicknames, all on the confirmed single partner bank. Balances $0.
- [ ] **Step 2 (verify):** Account count + nicknames match the map. Screenshot; Claude diff-checks against the map.

### Task 8: Configure internal auto-transfer rules + sweep-to-hub 🧍

- [ ] **Step 1:** Create each internal auto-transfer rule and each sweep-to-hub rule from the map. Leave enabled but harmless (no funds present). Keep routing cash in checking, not Treasury.
- [ ] **Step 2 (verify):** Rule count + parameters match the map exactly. Screenshot; Claude diff-checks.

### Task 9: Set up external recipients on the hub allowlist 🤝

- [ ] **Step 1 (🧍 Joshua):** In Mercury, add each push-payee from the map as a recipient (ACH/wire details): Dillon Ford first, then draws/contractors. This is the deliberate manual step; new payees are added here later.
- [ ] **Step 2 (🤖):** Record the finalized recipient list (name + property + memo string, NO bank details in git) in `mercury-account-map.md`.
- [ ] **Step 3 (verify):** Every push-payee in `repoint-checklist.md` exists as a Mercury recipient. Pull-merchants are NOT added as recipients (card-on-file instead).
- [ ] **Step 4 (commit):** `git add docs/migration/mercury-account-map.md && git commit -m "docs(migration): record hub recipient allowlist"`

### Task 10: Set up Mercury API + MCP (read-only everywhere; scoped write on hub) 🤝

**Files:** Create `scripts/migration/.env.example`; Modify `.gitignore`

- [ ] **Step 1 (🧍 Joshua):** Generate a **read-only** token (org-wide) and, if Mercury supports it (per Task 5), a **write token scoped to the hub**; IP-whitelist both. Store in secret manager / local `.env` (never git).
- [ ] **Step 2 (🤖):** Write `.env.example` with `MERCURY_READ_TOKEN=`, `MERCURY_HUB_WRITE_TOKEN=`, `MERCURY_BASE_URL=`. Add `scripts/migration/.env` to `.gitignore`.
- [ ] **Step 3 (🧍 Joshua):** Connect Mercury's MCP server to the AI layer.
- [ ] **Step 4 (verify):** Via MCP, "list my Mercury accounts and balances" returns the Task 7 accounts. Proves read-access.
- [ ] **Step 5 (commit):** `git add scripts/migration/.env.example .gitignore && git commit -m "chore(migration): Mercury API/MCP scaffolding (read-only + scoped hub write)"`

### Task 11: Build the dry-run-gated payment send path (TDD) 🤖

**Files:** Create `scripts/migration/payments.py`, `scripts/migration/test_payments.py`

- [ ] **Step 1: Write the failing tests.**

```python
# scripts/migration/test_payments.py
import pytest
from payments import build_payment_set, send_payments, UnlistedRecipientError

ALLOWLIST = {"Dillon Ford", "Shelby McDonald"}

def test_builds_per_obligation_payments():
    obligations = [
        {"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "1312-operating", "memo": "1312 65th Dr seller finance"},
        {"recipient": "Shelby McDonald", "amount": 1800.00, "from_account": "2102-rehab", "memo": "2102 68th St draw"},
    ]
    payments = build_payment_set(obligations, ALLOWLIST)
    assert len(payments) == 2
    assert payments[0]["memo"] == "1312 65th Dr seller finance"
    assert payments[0]["from_account"] == "1312-operating"

def test_unlisted_recipient_blocked():
    obligations = [{"recipient": "Unknown LLC", "amount": 500, "from_account": "hub", "memo": "x"}]
    with pytest.raises(UnlistedRecipientError):
        build_payment_set(obligations, ALLOWLIST)

def test_dry_run_does_not_send():
    sent = []
    payments = [{"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "hub", "memo": "x"}]
    report = send_payments(payments, send_fn=lambda p: sent.append(p), confirm=False)
    assert sent == []
    assert report[0]["sent"] is False

def test_confirm_sends():
    sent = []
    payments = [{"recipient": "Dillon Ford", "amount": 2310.94, "from_account": "hub", "memo": "x"}]
    report = send_payments(payments, send_fn=lambda p: sent.append(p), confirm=True)
    assert len(sent) == 1
    assert report[0]["sent"] is True
```

- [ ] **Step 2: Run to confirm failure.** `python -m pytest scripts/migration/test_payments.py -v` — Expected: FAIL (module not found).
- [ ] **Step 3: Implement minimal `payments.py`.**

```python
# scripts/migration/payments.py
class UnlistedRecipientError(Exception):
    pass

def build_payment_set(obligations, allowlist):
    """obligations: list of {recipient, amount, from_account, memo}.
    Raises UnlistedRecipientError if any recipient is not on the allowlist."""
    payments = []
    for ob in obligations:
        if ob["recipient"] not in allowlist:
            raise UnlistedRecipientError(ob["recipient"])
        payments.append({
            "recipient": ob["recipient"],
            "amount": round(ob["amount"], 2),
            "from_account": ob["from_account"],
            "memo": ob["memo"],
        })
    return payments

def send_payments(payment_set, send_fn, confirm=False):
    """Dry-run by default. Calls send_fn (the real Mercury API call) only when confirm=True."""
    report = []
    for p in payment_set:
        if confirm:
            send_fn(p)
        report.append({**p, "sent": bool(confirm)})
    return report
```

- [ ] **Step 4: Run to confirm pass.** `python -m pytest scripts/migration/test_payments.py -v` — Expected: PASS (4 tests).
- [ ] **Step 5: Commit.** `git add scripts/migration/payments.py scripts/migration/test_payments.py && git commit -m "feat(migration): allowlisted, dry-run-gated payment send path"`

---

# Phase 2 — Vet internal AND outbound (still no real migration)

### Task 12: Rule-validation script (TDD) 🤖

**Files:** Create `scripts/migration/validate_rules.py`, `scripts/migration/test_validate_rules.py`

- [ ] **Step 1: Write the failing tests.**

```python
# scripts/migration/test_validate_rules.py
from validate_rules import apply_rules

def test_section8_funds_mortgage_account():
    rules = [{"source": "1312-operating", "dest": "1312-mortgage", "type": "fixed", "amount": 2310.94, "trigger": "monthly"}]
    deposits = [{"account": "1312-operating", "amount": 970.00}, {"account": "1312-operating", "amount": 1340.94}]
    balances = apply_rules(deposits, rules)
    assert round(balances["1312-mortgage"], 2) == 2310.94
    assert round(balances["1312-operating"], 2) == 0.00

def test_percentage_split_profit_first():
    rules = [
        {"source": "main", "dest": "taxes", "type": "percent", "amount": 15, "trigger": "by_transaction"},
        {"source": "main", "dest": "profit", "type": "percent", "amount": 5, "trigger": "by_transaction"},
    ]
    deposits = [{"account": "main", "amount": 1000.00}]
    balances = apply_rules(deposits, rules)
    assert round(balances["taxes"], 2) == 150.00
    assert round(balances["profit"], 2) == 50.00
    assert round(balances["main"], 2) == 800.00
```

- [ ] **Step 2: Run to confirm failure.** `python -m pytest scripts/migration/test_validate_rules.py -v` — Expected: FAIL (`apply_rules` not defined).
- [ ] **Step 3: Implement minimal `validate_rules.py`.**

```python
# scripts/migration/validate_rules.py
# NOTE: "percent" rules apply to INCOMING funds, not the running balance — matches
# Mercury's actual behavior. (15% + 5% of a $1,000 deposit = $150 + $50, leaving $800,
# regardless of rule order. Computing off the running balance would wrongly give $42.50.)
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
        moved = deposited.get(src, 0) * (r["amount"] / 100) if r["type"] == "percent" else r["amount"]
        moved = min(moved, available)
        balances[src] = available - moved
        balances[r["dest"]] = balances.get(r["dest"], 0) + moved
    return balances
```

- [ ] **Step 4: Run to confirm pass.** `python -m pytest scripts/migration/test_validate_rules.py -v` — Expected: PASS (2 tests).
- [ ] **Step 5: Commit.** `git add scripts/migration/validate_rules.py scripts/migration/test_validate_rules.py && git commit -m "feat(migration): internal-split validation harness"`

### Task 13: Sandbox dry-run of a full month — internal splits 🤝

- [ ] **Step 1 (🧍 Joshua):** Generate a Mercury **sandbox** token. Simulate one representative month of inbound deposits (real amounts from a statement month) against the configured internal + sweep-to-hub rules.
- [ ] **Step 2 (🤖):** Feed the same month's deposits + the `mercury-account-map.md` ruleset into `validate_rules.py`. Compare to (a) the Mercury sandbox result and (b) the actual Sequence-produced balances from that month's real statement.
- [ ] **Step 3 (verify — GATE):** All three agree per account (within rounding). Any mismatch = fix the Mercury rule (Task 8) and re-run. Do not proceed until they match.

### Task 14: Sandbox validation of the payment path 🤝

- [ ] **Step 1 (🤖):** From that month's `external-push` obligations, build the payment set with `payments.build_payment_set` against the Task 9 allowlist. Confirm one payment per obligation, correct amounts, correct property memos, correct from_account.
- [ ] **Step 2 (🤝):** Run `send_payments(..., confirm=False)` wired to the Mercury **sandbox** send call. Confirm the dry-run reports the payments as `sent: False` and **nothing is sent**. Then run one `confirm=True` send in sandbox and confirm it posts in sandbox.
- [ ] **Step 3 (verify — GATE):** Dry-run genuinely blocks sending; an unlisted recipient raises; a confirmed send posts in sandbox. Do not proceed until all hold.

### Task 15: One live low-risk property, end-to-end (both layers) 🤝

- [ ] **Step 1 (🤖 + 🧍):** Pick the lowest-risk property (single tenant, simple rule, ideally not seller-finance-critical). Confirm choice with Joshua.
- [ ] **Step 2 (🧍 Mostafa/Joshua):** Repoint ONLY that property's DoorLoop deposit account → its Mercury operating account; give the housing authority the new account/routing # if Section 8.
- [ ] **Step 3:** Let one real cycle run: DoorLoop deposit → internal rule fires → funds sweep to hub → AI builds the payment set → after human confirm, AI executes **one real external payment** for that property.
- [ ] **Step 4 (verify — GATE):** Via MCP/API confirm the deposit landed, the split was correct, and the live payment posted to the right recipient with the right memo — matching what Sequence/Baselane did last month. This proves both layers before broad cutover.

---

# Phase 3 — Cutover (real funds move — only after Task 15 passes)

### Task 16: Repoint deposits, property-by-property 🧍

- [ ] **Step 1:** For each remaining property in `repoint-checklist.md`: repoint the DoorLoop deposit account → Mercury and give each housing authority the new account/routing # for Section 8 ACH.
- [ ] **Step 2 (verify):** After each property's first cycle on Mercury, confirm (via MCP/API) the deposit + internal rule fired correctly before moving on. Track completion in `repoint-checklist.md`.

### Task 17: Move external payments onto the hub — Dillon Ford FIRST 🧍

- [ ] **Step 1 (CRITICAL):** Schedule the Dillon Ford seller-finance cutover for immediately **after** a month's payment clears from Baselane (full cycle of buffer). Fund the hub and execute the payment from Mercury (human-confirmed). Keep a manual backup payment ready.
- [ ] **Step 2:** Move remaining push-payees (draws, contractors, title) onto the hub. Switch pull-merchants (SaaS) to the Mercury debit card.
- [ ] **Step 3 (verify):** First Dillon Ford payment from Mercury posts on time. Each SaaS charge moves to the Mercury card (watch for a failed/double charge). Nothing still pulls from Baselane except by design.

### Task 18: Drain Baselane balances 🧍

- [ ] **Step 1:** Once all deposits + payees are on Mercury and verified for a full cycle, transfer remaining Baselane balances to the matching Mercury accounts. Leave a small buffer until certain no stragglers hit Baselane.
- [ ] **Step 2 (verify):** Baselane accounts trend to ~$0 with no new expected activity. Confirm against `repoint-checklist.md` that every in/out is on Mercury.

---

# Phase 4 — Decommission Sequence + escalate AI autonomy

### Task 19: Cancel Sequence 🧍

- [ ] **Step 1:** Confirm no remaining activity depends on Sequence (all routing native in Mercury, all payments on the hub). Cancel getsequence.io.
- [ ] **Step 2 (verify):** Next month's statements show no "Webber Wealth Ho Sequence" lines and no $90.92 charge. Update `wiki/sequence.md` status → archived; note realized savings.

### Task 20: Link Mercury into Baselane for books-only 🧍

- [ ] **Step 1:** In Baselane, connect the Mercury accounts as external/linked accounts so bookkeeping + Schedule E continue off Mercury's transaction feed.
- [ ] **Step 2 (verify):** Baselane shows Mercury transactions and categorizes them; a P&L / Schedule E view still works.

### Task 21: Reconciliation script (TDD) 🤖

**Files:** Create `scripts/migration/reconcile.py`, `scripts/migration/test_reconcile.py`

- [ ] **Step 1: Write the failing tests.**

```python
# scripts/migration/test_reconcile.py
from reconcile import find_discrepancies

def test_flags_underfunded_mortgage_account():
    actual = {"1312-mortgage": 2000.00, "1312-operating": 310.94}
    expected = {"1312-mortgage": 2310.94, "1312-operating": 0.00}
    issues = find_discrepancies(actual, expected, tolerance=0.01)
    assert "1312-mortgage" in issues
    assert "1312-operating" in issues

def test_no_discrepancies_when_matched():
    actual = {"1312-mortgage": 2310.94}
    expected = {"1312-mortgage": 2310.945}
    assert find_discrepancies(actual, expected, tolerance=0.01) == {}
```

- [ ] **Step 2: Run to confirm failure.** `python -m pytest scripts/migration/test_reconcile.py -v` — Expected: FAIL (`find_discrepancies` not defined).
- [ ] **Step 3: Implement minimal `reconcile.py`.**

```python
# scripts/migration/reconcile.py
def find_discrepancies(actual, expected, tolerance=0.01):
    issues = {}
    for account, exp in expected.items():
        act = actual.get(account, 0)
        if abs(act - exp) > tolerance:
            issues[account] = {"actual": act, "expected": exp, "delta": round(act - exp, 2)}
    return issues
```

- [ ] **Step 4: Run to confirm pass.** `python -m pytest scripts/migration/test_reconcile.py -v` — Expected: PASS (2 tests).
- [ ] **Step 5: Commit.** `git add scripts/migration/reconcile.py scripts/migration/test_reconcile.py && git commit -m "feat(migration): balance reconciliation"`

### Task 22: Escalate AI autonomy via the Bike Method 🤝

The payment capability already exists from Phase 1–2; this task only escalates how much runs unattended. **Across all rungs: paying a brand-new recipient is always human-gated, and outbound routes through Mostafa until autonomy is explicitly earned.**

- [ ] **Step 1 (Rung 1 — read-only):** Schedule a daily Claude/MCP job that pulls balances + transactions and runs `reconcile.py`, posting a summary + discrepancies to Joshua (Telegram) / Mostafa. No write key in use.
- [ ] **Step 2 (Rung 2 — propose/approve):** After read-only runs clean for a few weeks, AI builds the payment set (`payments.build_payment_set`), sends the dry-run proposal to Joshua/Mostafa, they approve, AI executes with `confirm=True`.
- [ ] **Step 3 (Rung 3 — caps):** AI auto-executes *known recurring* payments to *allowlisted* recipients up to a $ cap (set the cap with Joshua), notifying after; anything outside caps or to a new recipient → human approval.
- [ ] **Step 4 (Rung 4 — bounded autonomy):** Only after sustained clean operation, allow autonomous routine routing within hard caps + allowlist; human spot-checks. Document the kill switch (instant token revoke).
- [ ] **Step 5 (verify):** Each rung runs clean for its trial window before the next. Capture the final setup in a new `wiki/ai-money-ops.md` page.

---

## Out of scope (separate, much-later plan)

The **in-house management app that replaces DoorLoop** — tenant portals, in-house seller-finance note servicing (amortized), in-house rent-to-own payment collection/servicing — is a committed future build per `wiki/company-roadmap.md` and the spec's future-phase section. It starts only after this migration is fully in place and gets its own brainstorm → spec → plan.
