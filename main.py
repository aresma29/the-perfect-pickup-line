#!/usr/bin/env python3
"""Print the pickup line from entry.txt (resolved relative to this file).

The grader runs `python3 -P -s main.py` from an arbitrary working
directory on a read-only filesystem, so entry.txt is located via
__file__, never via the current directory.
"""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
