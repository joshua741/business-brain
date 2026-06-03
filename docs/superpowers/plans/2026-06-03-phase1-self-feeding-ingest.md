# Phase 1: Self-Feeding Ingest — Hardened Loop, Conversation Capture, Masking

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Business Brain capture every Claude Code session into `raw/` automatically, ingest `raw/` by reconciliation (no more skipped backlog), and enforce a privacy baseline (masking + secret audit + repo-private check) — without manual steps.

**Architecture:** Two reusable Python libs (`mask_sensitive`, `audit_secrets`), one Python SessionEnd hook (`capture_conversation`) registered in user-level `settings.json`, and a hardened `daily-wiki-maintenance.ps1`. All data stays in the confirmed-private GitHub repo; the hook and the daily loop both apply masking and the audit backstops it.

**Tech Stack:** Python 3 (regex libs + hook), PowerShell (scheduled-task scripts), Claude Code headless (`claude --print`), `gh` CLI, git. Repo: `C:\Users\joshu\.claude\Business_Brain`.

---

## File structure

- Create `lib/mask_sensitive.py` — mask SSNs and bare account/card/loan digit-runs; preserve amounts, dates, EINs. CLI (stdin→stdout) + importable `mask_text()`.
- Create `lib/audit_secrets.py` — scan `raw/` + `wiki/` for unmasked identifiers; importable `scan(root)` + CLI.
- Create `hooks/capture_conversation.py` — SessionEnd hook: summarize the transcript via `claude --print`, mask, write `raw/conversation-*.md`.
- Create `tests/test_mask_sensitive.py`, `tests/test_audit_secrets.py` — plain `assert` tests run with `python`.
- Modify `daily-wiki-maintenance.ps1` — reconciliation-based + autonomous prompt + verification + privacy lint + private-gated push.
- Modify `C:\Users\joshu\.claude\settings.json` — register the SessionEnd hook.

All commits happen in the `Business_Brain` repo.

---

### Task 1: Masking module

**Files:**
- Create: `lib/mask_sensitive.py`
- Test: `tests/test_mask_sensitive.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_mask_sensitive.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "lib"))
from mask_sensitive import mask_text

def run():
    # SSN masked to last 4
    assert mask_text("SSN 123-45-6789 on file") == "SSN XXX-XX-6789 on file"
    # bare account/loan digit-run (>=8) masked: keep first 2 + last 4
    assert mask_text("Account 200012346030 active") == "Account 20XXXXXX6030 active"
    # card number masked
    assert mask_text("Card 4111111111111111") == "Card 41XXXXXXXXXX1111"
    # dollar amounts preserved
    assert mask_text("Mortgage $2,310.94/mo") == "Mortgage $2,310.94/mo"
    # entity EIN preserved (NN-NNNNNNN)
    assert mask_text("EIN 39-2122418") == "EIN 39-2122418"
    # ISO dates preserved
    assert mask_text("closed 2026-06-03") == "closed 2026-06-03"
    # already-masked values left alone (contain X, not pure digits)
    assert mask_text("acct 20XXXXXX6030") == "acct 20XXXXXX6030"
    print("test_mask_sensitive PASS")

if __name__ == "__main__":
    run()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python tests/test_mask_sensitive.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'mask_sensitive'`

- [ ] **Step 3: Write minimal implementation**

```python
# lib/mask_sensitive.py
#!/usr/bin/env python3
"""Mask sensitive identifiers while preserving financial figures.

Masks: SSNs (XXX-XX-####) and bare 8-19 digit runs (account/card/loan) to
first-2 + X's + last-4. Preserves: dollar amounts, ISO dates, entity EINs
(NN-NNNNNNN), names, addresses, and already-masked values containing X.
Usage: `python mask_sensitive.py < in > out`  or  `from mask_sensitive import mask_text`.
"""
import re
import sys

SSN_RE = re.compile(r"\b(\d{3})-(\d{2})-(\d{4})\b")
# 8-19 digits not adjacent to a digit, dot, comma, dollar sign, or dash.
# The dash exclusion preserves EINs (NN-NNNNNNN); the $/comma/dot exclusion preserves amounts.
DIGIT_RUN_RE = re.compile(r"(?<![\d.,$-])\d{8,19}(?![\d.,-])")


def _mask_run(m: "re.Match") -> str:
    s = m.group(0)
    if len(s) <= 6:
        return "X" * len(s)
    return s[:2] + "X" * (len(s) - 6) + s[-4:]


def mask_text(text: str) -> str:
    text = SSN_RE.sub(lambda m: "XXX-XX-" + m.group(3), text)
    text = DIGIT_RUN_RE.sub(_mask_run, text)
    return text


if __name__ == "__main__":
    sys.stdout.write(mask_text(sys.stdin.read()))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python tests/test_mask_sensitive.py`
Expected: `test_mask_sensitive PASS`

- [ ] **Step 5: Commit**

```bash
git add lib/mask_sensitive.py tests/test_mask_sensitive.py
git commit -m "feat: add sensitive-data masking module + tests"
```

---

### Task 2: Secret-audit lint

**Files:**
- Create: `lib/audit_secrets.py`
- Test: `tests/test_audit_secrets.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_audit_secrets.py
import sys, pathlib, tempfile, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "lib"))
from audit_secrets import scan

def run():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "raw").mkdir()
        (root / "wiki").mkdir()
        # planted unmasked secrets
        (root / "raw" / "a.md").write_text("SSN 123-45-6789 and acct 4000015856987", encoding="utf-8")
        # clean / already-masked content
        (root / "wiki" / "b.md").write_text("amount $2,310.94 EIN 39-2122418 acct 20XXXXXX6030", encoding="utf-8")
        hits = scan(root)
        joined = " ".join(hits)
        assert any("a.md" in h for h in hits), hits
        assert "123-45-6789" in joined, hits
        assert "4000015856987" in joined, hits
        # clean file must not be flagged
        assert not any("b.md" in h for h in hits), hits
    print("test_audit_secrets PASS")

if __name__ == "__main__":
    run()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python tests/test_audit_secrets.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'audit_secrets'`

- [ ] **Step 3: Write minimal implementation**

```python
# lib/audit_secrets.py
#!/usr/bin/env python3
"""Scan raw/ and wiki/ for UNMASKED sensitive identifiers.

`scan(root)` returns a list of human-readable hit strings. CLI prints hits and
exits 1 when any are found (the daily loop treats this as a non-fatal warning
and logs it; the repo-private check is the hard gate). Already-masked values
contain 'X' and are pure-digit regexes, so they are not matched.
"""
import re
import sys
import pathlib

SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
# 10-19 digit bare runs (higher floor than the masker to limit false positives in audit)
DIGIT_RUN_RE = re.compile(r"(?<![\d.,$-])\d{10,19}(?![\d.,-])")
CHECKS = [(SSN_RE, "SSN"), (DIGIT_RUN_RE, "long-digit-run")]


def scan(root, dirs=("raw", "wiki")):
    root = pathlib.Path(root)
    hits = []
    for d in dirs:
        base = root / d
        if not base.exists():
            continue
        for f in base.rglob("*.md"):
            text = f.read_text(encoding="utf-8", errors="ignore")
            for rx, label in CHECKS:
                for m in rx.finditer(text):
                    hits.append(f"{f.relative_to(root)}: {label} '{m.group(0)}'")
    return hits


if __name__ == "__main__":
    root = pathlib.Path(__file__).resolve().parent.parent
    found = scan(root)
    if found:
        print("POTENTIAL UNMASKED SECRETS:")
        for h in found:
            print(" -", h)
        sys.exit(1)
    print("audit clean")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python tests/test_audit_secrets.py`
Expected: `test_audit_secrets PASS`

- [ ] **Step 5: Run the audit against the live vault (informational)**

Run: `python lib/audit_secrets.py`
Expected: either `audit clean`, or a list of hits (e.g., mortgage loan numbers already in the wiki). Hits here are expected and non-fatal — they become the warning the loop logs. Do not fix wiki content in this task.

- [ ] **Step 6: Commit**

```bash
git add lib/audit_secrets.py tests/test_audit_secrets.py
git commit -m "feat: add secret-audit lint + tests"
```

---

### Task 3: Conversation-capture SessionEnd hook

**Files:**
- Create: `hooks/capture_conversation.py`

This hook receives SessionEnd JSON on stdin (`{transcript_path, session_id, cwd, reason, ...}`), summarizes the transcript with `claude --print`, masks the result, and writes a dated report into `raw/`. It must NEVER block or error out a session — any failure exits 0. A recursion guard prevents the summarizer's own headless run from triggering the hook again.

- [ ] **Step 1: Write the hook**

```python
# hooks/capture_conversation.py
#!/usr/bin/env python3
"""SessionEnd hook: summarize a Claude Code session into raw/ as a masked report.

Registered as a user-level SessionEnd hook. Reads hook JSON from stdin, reads the
transcript JSONL, asks `claude --print` for a structured summary, masks it, and
writes raw/conversation-YYYY-MM-DD-HHMM-<slug>.md. Fails safe: any error -> exit 0.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(r"C:\Users\joshu\.claude\Business_Brain")
RAW = REPO / "raw"
CLAUDE = r"C:\Users\joshu\AppData\Roaming\npm\claude.cmd"
GUARD = "BB_CAPTURE_RUNNING"
MAX_TRANSCRIPT_CHARS = 100_000

sys.path.insert(0, str(REPO / "lib"))
from mask_sensitive import mask_text

PROMPT = (
    "Summarize this Claude Code session as a detailed business handover report for "
    "Joshua Webber's Business Brain. Output Markdown with these sections: "
    "## Topic (one line), ## What was done, ## Decisions made, ## Current state, "
    "## Next steps, ## New business facts (anything about entities, properties, "
    "deals, people, tools, finances worth saving to the wiki), ## Open questions. "
    "Be specific with names, amounts, and dates. First line of output must be: "
    "TITLE: <3-6 word kebab-friendly topic>. Transcript follows:\n\n"
)


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return (text or "session")[:48]


def read_transcript(path: str) -> str:
    parts, users = [], 0
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = obj.get("message", obj)
            role = msg.get("role")
            content = msg.get("content", "")
            if isinstance(content, list):
                content = " ".join(
                    c.get("text", "") for c in content if isinstance(c, dict)
                )
            if not content:
                continue
            if role == "user":
                users += 1
            parts.append(f"{role}: {content}")
    return "\n".join(parts)[-MAX_TRANSCRIPT_CHARS:], users


def main() -> int:
    if os.environ.get(GUARD) == "1":
        return 0  # recursion guard: this IS the summarizer's own run
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tpath = data.get("transcript_path")
    if not tpath or not os.path.exists(tpath):
        return 0
    try:
        transcript, user_turns = read_transcript(tpath)
    except Exception:
        return 0
    if user_turns < 2 or len(transcript) < 200:
        return 0  # skip trivial sessions

    env = dict(os.environ)
    env[GUARD] = "1"
    try:
        proc = subprocess.run(
            [CLAUDE, "--print", PROMPT + transcript],
            capture_output=True, text=True, env=env, timeout=120,
        )
    except Exception:
        return 0
    out = (proc.stdout or "").strip()
    if not out:
        return 0

    title = "session"
    first, _, rest = out.partition("\n")
    if first.upper().startswith("TITLE:"):
        title = first.split(":", 1)[1]
        out = rest.strip()
    slug = slugify(title)

    now = datetime.now()
    stamp = now.strftime("%Y-%m-%d-%H%M")
    fname = f"conversation-{stamp}-{slug}.md"
    body = mask_text(out)
    frontmatter = (
        "---\n"
        f"name: source-conversation-{stamp}-{slug}\n"
        "type: source\n"
        "tags: [conversation, claude-session]\n"
        f"sources: [{fname}]\n"
        f"updated: {now.strftime('%Y-%m-%d')}\n"
        "---\n"
    )
    try:
        RAW.mkdir(parents=True, exist_ok=True)
        (RAW / fname).write_text(frontmatter + "\n" + body + "\n", encoding="utf-8")
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Create a fake transcript fixture and smoke-test the hook**

Run (PowerShell):
```powershell
$tmp = "$env:TEMP\bb-transcript.jsonl"
@'
{"message":{"role":"user","content":"We closed 9999 Test St for $120,000, EIN 39-1234567, SSN 555-12-3456."}}
{"message":{"role":"assistant","content":"Got it. Logging the close and the entity details."}}
{"message":{"role":"user","content":"Next step is to wire $5,000 earnest money tomorrow."}}
'@ | Out-File -Encoding utf8 $tmp
'{"transcript_path":"' + ($tmp -replace '\\','\\\\') + '","session_id":"smoke","reason":"clear"}' | python C:\Users\joshu\.claude\Business_Brain\hooks\capture_conversation.py
Get-ChildItem C:\Users\joshu\.claude\Business_Brain\raw\conversation-*.md | Sort-Object LastWriteTime | Select-Object -Last 1
```
Expected: a new `raw/conversation-*.md` exists. Open it and confirm: it has a Topic/sections, the SSN appears as `XXX-XX-3456`, `$120,000` and `EIN 39-1234567` are intact.

- [ ] **Step 3: Verify masking landed (no raw SSN)**

Run (PowerShell):
```powershell
$f = Get-ChildItem C:\Users\joshu\.claude\Business_Brain\raw\conversation-*.md | Sort-Object LastWriteTime | Select-Object -Last 1
if (Select-String -Path $f.FullName -Pattern '555-12-3456' -Quiet) { "FAIL: raw SSN present" } else { "PASS: SSN masked" }
```
Expected: `PASS: SSN masked`

- [ ] **Step 4: Delete the smoke-test artifact (don't pollute the vault)**

Run (PowerShell):
```powershell
Get-ChildItem C:\Users\joshu\.claude\Business_Brain\raw\conversation-*-we-closed-* | Remove-Item -Force -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\bb-transcript.jsonl" -Force -ErrorAction SilentlyContinue
```
Expected: no error.

- [ ] **Step 5: Commit**

```bash
git add hooks/capture_conversation.py
git commit -m "feat: add SessionEnd conversation-capture hook with masking"
```

---

### Task 4: Register the SessionEnd hook (user-level)

**Files:**
- Modify: `C:\Users\joshu\.claude\settings.json`

Register globally so EVERY Claude Code session (any project) is captured. Merge — do not clobber existing settings.

- [ ] **Step 1: Inspect current settings**

Run: `python -c "import json;print(json.dumps(json.load(open(r'C:/Users/joshu/.claude/settings.json')),indent=2))"`
Expected: prints current JSON (note whether a `hooks` key already exists).
If the file does not exist, treat current config as `{}`.

- [ ] **Step 2: Merge the SessionEnd hook in (idempotent)**

Run:
```bash
python - <<'PY'
import json, pathlib
p = pathlib.Path(r"C:/Users/joshu/.claude/settings.json")
cfg = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
hooks = cfg.setdefault("hooks", {})
se = hooks.setdefault("SessionEnd", [])
cmd = r"python C:\Users\joshu\.claude\Business_Brain\hooks\capture_conversation.py"
already = any(
    h.get("command") == cmd
    for grp in se for h in grp.get("hooks", [])
)
if not already:
    se.append({"hooks": [{"type": "command", "command": cmd}]})
p.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
print("registered" if not already else "already present")
PY
```
Expected: `registered` (or `already present` on re-run).

- [ ] **Step 3: Validate the JSON is well-formed**

Run: `python -c "import json;json.load(open(r'C:/Users/joshu/.claude/settings.json'));print('valid json')"`
Expected: `valid json`

- [ ] **Step 4: Live verification — capture a real session**

Open a new Claude Code session in any project, exchange 2–3 messages, then end it (`/exit`). Then run:
```powershell
Get-ChildItem C:\Users\joshu\.claude\Business_Brain\raw\conversation-*.md | Sort-Object LastWriteTime | Select-Object -Last 1
```
Expected: a fresh `conversation-*.md` from that session. (Note: `settings.json` is not in the Business_Brain repo, so there is nothing to commit for this task — the change lives in `~/.claude`.)

---

### Task 5: Harden the daily maintenance loop

**Files:**
- Modify: `daily-wiki-maintenance.ps1`

Fix the two defects (date-filter skip; agent asks instead of writing) and add the privacy gate.

- [ ] **Step 1: Replace the embedded prompt (`$prompt = @"..."@` block)**

Replace the entire here-string assigned to `$prompt` with:

```powershell
$prompt = @"
You are the daily maintenance agent for Joshua Webber's Business Brain wiki in the current directory. Execute ALL steps autonomously and perform ALL file writes yourself. NEVER ask for approval, confirmation, or input — this runs headless and no human will answer. Do not stop until every step is complete.

1. INGEST BY RECONCILIATION (not by date). For every file in raw/ (recursively, *.md), determine whether a wiki/source-*.md page already lists that exact filename in its `sources:` frontmatter. For each raw file with NO such source page, ingest it now:
   - Create wiki/source-<kebab-title>.md with frontmatter (name, type: source, tags, sources: [<exact raw filename>], updated: $date) and a detailed summary with specific figures, dates, parties, and (source: <filename>) citations and [[wikilinks]].
   - Create or update the entity/project/concept/person pages it touches; add [[wikilinks]] throughout.
   - Add the source under "## Sources" in wiki/index.md.
2. LINT: orphan pages (add an inbound link from the most relevant page); missing [[wikilinks]] (create stub pages with valid frontmatter); contradictions (flag in wiki/log.md, do not auto-resolve); stale status fields (update where evidence supports).
3. VERIFY: confirm every raw/*.md is now referenced by some wiki page. If any remain unreferenced, ingest them, then state the final counts.
4. Append to wiki/log.md: ## [$date] ingest+lint | <one-line summary including how many source pages were created and lint fixes>.
5. Write $date to wiki/.last-ingest.

Do not run any git commands. Exit when done.
"@
```

- [ ] **Step 2: Add the privacy gate after the Claude run, before the git commit block**

Immediately after the line `& $claude --print $prompt --dangerously-skip-permissions 2>&1 | ForEach-Object { Log $_ }`, insert:

```powershell
# --- Privacy gate ---
Log "Secret audit (non-fatal warning)"
& python "$repoPath\lib\audit_secrets.py" 2>&1 | ForEach-Object { Log $_ }

Log "Repo visibility check"
$isPrivate = (& $gh repo view joshua741/business-brain --json isPrivate -q .isPrivate 2>&1 | Out-String).Trim()
Log "isPrivate=$isPrivate"
if ($isPrivate -ne 'true') {
    Log "ABORT: repo is NOT private — refusing to commit/push sensitive data."
    Log "=== Daily maintenance halted on privacy gate ==="
    exit 1
}
```

- [ ] **Step 3: Add the `$gh` path variable near the other path vars (top of file)**

After the line `$git      = "C:\Program Files\Git\cmd\git.exe"`, insert:

```powershell
$gh       = "C:\Program Files\GitHub CLI\gh.exe"
```

(If `gh` lives elsewhere, set the correct path — find it with `(Get-Command gh).Source`.)

- [ ] **Step 4: Syntax-check the script parses**

Run (PowerShell):
```powershell
$null = [System.Management.Automation.PSParser]::Tokenize((Get-Content C:\Users\joshu\.claude\Business_Brain\daily-wiki-maintenance.ps1 -Raw), [ref]$null); "parses OK"
```
Expected: `parses OK`

- [ ] **Step 5: Confirm `gh` path resolves**

Run (PowerShell): `Test-Path "C:\Program Files\GitHub CLI\gh.exe"`
Expected: `True` (if `False`, fix `$gh` to the real path from `(Get-Command gh).Source`).

- [ ] **Step 6: Commit**

```bash
git add daily-wiki-maintenance.ps1
git commit -m "feat: reconciliation-based autonomous ingest + privacy gate in daily loop"
```

---

### Task 6: End-to-end dry run

**Files:** none (verification only)

- [ ] **Step 1: Reconciliation check — every raw file is covered**

Run (bash):
```bash
cd /c/Users/joshu/.claude/Business_Brain
missing=0
for raw in raw/*.md; do
  base=$(basename "$raw")
  grep -rqF "$base" wiki/*.md || { echo "UNCOVERED: $base"; missing=$((missing+1)); }
done
[ "$missing" -eq 0 ] && echo "All raw files covered"
```
Expected: `All raw files covered` (backlog already swept on 2026-06-02; new conversation reports from Task 4 should also be covered after the next loop run).

- [ ] **Step 2: Run the unit tests together**

Run (bash):
```bash
cd /c/Users/joshu/.claude/Business_Brain
python tests/test_mask_sensitive.py && python tests/test_audit_secrets.py
```
Expected: both print `PASS`.

- [ ] **Step 3: Manually trigger the scheduled task and read the log**

Run (PowerShell):
```powershell
Start-ScheduledTask -TaskName 'Business Brain Daily Wiki Maintenance'
Start-Sleep -Seconds 90
Get-Content C:\Users\joshu\.claude\Business_Brain\daily-maintenance.log -Tail 20
```
Expected: log shows the ingest ran, `isPrivate=true`, an `ingest+lint` line appended, and a commit/push (or "No changes"). Confirm it did NOT end on an "approve writes" prompt.

- [ ] **Step 4: Confirm `.last-ingest` advanced and log got an entry**

Run (PowerShell):
```powershell
Get-Content C:\Users\joshu\.claude\Business_Brain\wiki\.last-ingest
Get-Content C:\Users\joshu\.claude\Business_Brain\wiki\log.md -Tail 3
```
Expected: `.last-ingest` shows today; `log.md` has a fresh `ingest+lint` entry.

---

## Notes for the implementer

- **Fail-safe is sacred for the hook:** `capture_conversation.py` must never raise out to the session. Every external call is wrapped; on any doubt, `return 0`.
- **The repo-private check is the hard gate; the secret audit is a warning.** Don't make the audit abort the loop — Joshua's directive is "don't stop progress." Surface, log, move on; only repo-public halts the push.
- **Masking is best-effort.** The audit is the backstop; expect it to flag pre-existing mortgage loan numbers in the wiki — that's a future cleanup, not a Phase-1 blocker.
- **Out of scope for Phase 1:** the connector extractors, `connectors.yaml` registry, discovery/gap detector, and Notion two-way sync. Those are Phase 2–3 (separate plans).
