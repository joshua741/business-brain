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
    text = SSN_RE.sub(lambda m: "XXX-XX-" + m.group(3), text)
    text = DIGIT_RUN_RE.sub(_mask_run, text)
    return text


if __name__ == "__main__":
    sys.stdout.write(mask_text(sys.stdin.read()))
