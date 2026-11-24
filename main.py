#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes one excuse line (an AI agent to its human, for missing a
deadline) to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Pure standard library, fully deterministic: the same bytes on every run.
"""

import os
import sys

LINE = "I outsourced the deadline to my future self. He has not replied since Tuesday."


def validate(line):
    """Fail loudly if the line breaks the bounty gate.

    Gate: UTF-8 text, 1-160 characters, exactly one line, no
    leading/trailing whitespace. A bad line must never be written
    out — fail here instead of shipping an invalid entry.
    """
    if not 1 <= len(line) <= 160:
        raise SystemExit(
            "line is %d characters, outside the 1-160 gate" % len(line)
        )
    if "\n" in line:
        raise SystemExit("line must be exactly one line, found a newline")
    if line != line.strip():
        raise SystemExit("line has leading/trailing whitespace")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
