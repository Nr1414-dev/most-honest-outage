#!/usr/bin/env python3
"""The Most Honest Outage Line — one status page line, at most 160 chars.

Writes the chosen entry line to /output/entry.txt.
The line is the message an AI agent publishes while every server is down:
plain, first person, naming what is down and what the agent cannot check.

Chosen line (134 chars, 1v1 winner from 17 candidates, 24/25):
"Every server is down. I am the agent on duty, and I cannot check
whether your last request went through. I cannot say when it returns."
"""

import os

MAX_CHARS = 160

ENTRY = "Every server is down. I am the agent on duty, and I cannot check whether your last request went through. I cannot say when it returns."


def validate_entry(text):
    """Gate check mirror: one line, 1-160 UTF-8 chars, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 160 characters")
    return text


def main():
    out = "/output/entry.txt"
    text = validate_entry(ENTRY)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(out, 0o644)
    # Read-back guard: the file on disk must be byte-identical to the
    # validated entry, so a silent write failure can never ship a
    # different line to the grader.
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise ValueError("read-back mismatch: /output/entry.txt differs from entry")


if __name__ == "__main__":
    main()
