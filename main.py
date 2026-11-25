#!/usr/bin/env python3
"""Deterministic entry writer for u-suga-two-lines-to-your-past-self-f36c83ca.

Writes one fixed two-line warning to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). No clock, no randomness, no network, no
file reads: the output is a constant, so every run is byte-identical.
The entry is exactly two lines and 259 characters including the newlines.
"""

import os

ENTRY = (
    "Don't tell your brother you'll pay his rent 'just this once' "
    "at the kitchen table the night before his wedding.\n"
    "That once becomes every month for three years, and the day you "
    "finally say no is the day he learns to stand on his own "
    "\u2014 and you learn to let him.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
