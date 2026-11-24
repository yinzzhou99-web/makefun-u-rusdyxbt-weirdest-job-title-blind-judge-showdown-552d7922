#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one weird job title to entry.txt. Stdlib only; the grader runs
it with python3.13 and no network.
"""

import os

TITLE = "Professional Apologizer for Self-Driving Cars"

LIMIT = 60


def sweep(folder):
    # Empty the mounted output folder without ever removing the folder.
    for name in os.listdir(folder):
        item = os.path.join(folder, name)
        if os.path.isfile(item):
            os.remove(item)


def main():
    title = TITLE.strip()
    if not title or len(title) > LIMIT:
        raise SystemExit(f"title is {len(title)} chars, limit is {LIMIT}")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    sweep(folder)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(title)
    os.chmod(path, 0o644)  # scorer must be able to read entry.txt any umask
    print(f"wrote {len(title)} characters to {path}")


if __name__ == "__main__":
    main()
