#!/usr/bin/env python3
"""SessionEnd hook: write the FINAL masked session report into raw/.

Reuses the per-session report file maintained by live_session_update.py (Stop
hook) and overwrites it with the finalized handover. One file per session.
Fails safe: any error -> exit 0, never blocks the session.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # the hooks/ dir
from session_summary import GUARD, read_transcript, summarize, sessid8, report_path, write_report


def main() -> int:
    if os.environ.get(GUARD) == "1":
        return 0  # recursion guard: this IS the summarizer's own headless run
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tpath = data.get("transcript_path")
    sid = sessid8(data.get("session_id"))
    if not tpath or not os.path.exists(tpath):
        return 0
    try:
        transcript, user_turns = read_transcript(tpath)
    except Exception:
        return 0
    if user_turns < 2 or len(transcript) < 200:
        return 0  # skip trivial sessions
    slug, title, body = summarize(transcript)
    if not body:
        return 0
    try:
        write_report(report_path(sid), title, body, final=True)
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
