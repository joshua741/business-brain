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
# API tokens / secrets by known prefix -> fully redacted (never show any of it).
TOKEN_RE = re.compile(
    r"\b(?:pit-[0-9a-fA-F-]{16,}"
    r"|sk-[A-Za-z0-9]{16,}|sk_(?:live|test)_[A-Za-z0-9]{16,}"
    r"|(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{16,}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}"
    r"|AKIA[0-9A-Z]{12,}"
    r"|AC[0-9a-fA-F]{30,})\b"
)
# key=value / "key": "value" secret assignments -> redact the value only.
KV_SECRET_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|auth[_-]?token|access[_-]?token|bearer)\b"
    r"(\s*[:=]\s*|\s+)['\"]?([A-Za-z0-9._\-]{12,})['\"]?"
)
# 8-19 digits not adjacent to a digit, dot, comma, dollar sign, or dash on the LEFT
# (preserves EINs NN-NNNNNNN and $ amounts). On the RIGHT, only exclude a true
# decimal/grouping continuation (.5 or ,5) or another digit -- NOT a sentence period,
# so an account number at the end of a sentence still gets masked.
DIGIT_RUN_RE = re.compile(r"(?<![\d.,$-])\d{8,19}(?!\d)(?!\.\d)(?!,\d)")


def _mask_run(m: "re.Match") -> str:
    s = m.group(0)
    if len(s) <= 6:
        return "X" * len(s)
    return s[:2] + "X" * (len(s) - 6) + s[-4:]


def mask_text(text: str) -> str:
    text = TOKEN_RE.sub("<REDACTED-TOKEN>", text)
    text = KV_SECRET_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}<REDACTED>", text)
    text = SSN_RE.sub(lambda m: "XXX-XX-" + m.group(3), text)
    text = DIGIT_RUN_RE.sub(_mask_run, text)
    return text


if __name__ == "__main__":
    sys.stdout.write(mask_text(sys.stdin.read()))
