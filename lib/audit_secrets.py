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
