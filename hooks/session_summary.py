#!/usr/bin/env python3
"""Shared summarization helpers for the conversation-capture hooks.

Used by both capture_conversation.py (SessionEnd, final report) and
live_session_update.py (Stop, throttled in-progress updates). One evolving
report file per session, keyed by session id, masked on write.
"""
import glob
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent  # hooks/ -> repo root; works in any clone
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


def sessid8(session_id) -> str:
    return (re.sub(r"[^a-zA-Z0-9]", "", session_id or "") or "session")[:8]


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return (text or "session")[:48]


def read_transcript(path: str):
    parts, users = [], 0
    with open(path, "r", encoding="utf-8-sig", errors="ignore") as fh:
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


def summarize(transcript: str):
    """Return (slug, title_line, masked_body) or (None, None, None) on failure."""
    env = dict(os.environ)
    env[GUARD] = "1"
    try:
        # Prompt via stdin, NOT argv: large multi-line args get mangled by claude.cmd.
        proc = subprocess.run(
            [CLAUDE, "--print"],
            input=PROMPT + transcript,
            capture_output=True, text=True, env=env, timeout=120,
        )
    except Exception:
        return None, None, None
    out = (proc.stdout or "").strip()
    if not out:
        return None, None, None
    title = "session"
    first, _, rest = out.partition("\n")
    if first.upper().startswith("TITLE:"):
        title = first.split(":", 1)[1].strip()
        out = rest.strip()
    return slugify(title), title, mask_text(out)


def report_path(sid: str) -> Path:
    """Stable per-session report path; reuse an existing one if present."""
    hits = glob.glob(str(RAW / f"conversation-*-{sid}.md"))
    if hits:
        return Path(hits[0])
    return RAW / f"conversation-{datetime.now().strftime('%Y-%m-%d')}-{sid}.md"


def write_report(path: Path, title: str, body: str, final: bool):
    stem = path.name[:-3]
    tags = "[conversation, claude-session]" if final else "[conversation, claude-session, live]"
    marker = "" if final else (
        "> **Live session report** — updates as the conversation continues; "
        "finalized at session end.\n\n"
    )
    frontmatter = (
        "---\n"
        f"name: source-{stem}\n"
        "type: source\n"
        f"tags: {tags}\n"
        f"sources: [{path.name}]\n"
        f"updated: {datetime.now().strftime('%Y-%m-%d')}\n"
        "---\n"
    )
    RAW.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter + "\n" + marker + body + "\n", encoding="utf-8")
