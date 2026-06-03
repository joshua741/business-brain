#!/usr/bin/env python3
"""Stop hook: throttled in-progress session report into raw/.

Fires after each assistant turn but only does real work every
BB_LIVE_THROTTLE_MIN minutes (default 10) of active conversation, so the raw
context builds while the chat is still going without per-turn token cost.
Writes the same per-session file that SessionEnd later finalizes.
Fails safe: any error -> exit 0.
"""
import glob
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # the hooks/ dir
from session_summary import GUARD, read_transcript, summarize, sessid8, report_path, write_report

STATE_DIR = Path(__file__).resolve().parent / ".live-state"
THROTTLE_SECONDS = int(os.environ.get("BB_LIVE_THROTTLE_MIN", "10")) * 60


def main() -> int:
    if os.environ.get(GUARD) == "1":
        return 0  # recursion guard
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
        return 0

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_file = STATE_DIR / f"{sid}.json"
    now = time.time()
    last = {}
    if state_file.exists():
        try:
            last = json.loads(state_file.read_text())
        except Exception:
            last = {}
    # Throttle: skip unless enough time has passed AND there are new user turns.
    if now - last.get("ts", 0) < THROTTLE_SECONDS and user_turns <= last.get("users", 0):
        return 0

    slug, title, body = summarize(transcript)
    if not body:
        return 0
    try:
        write_report(report_path(sid), title, body, final=False)
        state_file.write_text(json.dumps({"ts": now, "users": user_turns}))
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
