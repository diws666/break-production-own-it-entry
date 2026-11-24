#!/usr/bin/env python3
"""make.fun entry writer: prints the break-production-own-it entry line.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
with no trailing newline.
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
LINE = "I deleted the production database. I have backups. The backups are also in the production database."


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
