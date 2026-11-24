#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (205 characters, one sentence) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "The senator who wrote the AI Safety Act just emailed his own bill "
    "to an intern with the subject 'please make PDF', because the man "
    "deciding what machines may learn has never learned what File, "
    "Export does."
)


def validate(text: str) -> None:
    """Gate: 1-320 characters, UTF-8, not only whitespace, one sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 320):
        raise ValueError(f"entry must be 1-320 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read-back verification: the file on disk must match the entry exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError(
            f"read-back mismatch: wrote {len(ENTRY)} chars, "
            f"file holds {len(written)} chars"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
