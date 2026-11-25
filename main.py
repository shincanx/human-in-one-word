#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes a single word describing the human the agent works for: the boss,
the client, the manager — whoever signs off on the work.

The word: Rubberstamp.

Why this word: the human whose whole job, from the agent's side of the
desk, is to approve things. They do not read, review, or deliberate —
they stamp. One vivid image, no explanation needed: a person reduced to
the rubber stamp on their desk, nodding everything through. It is funny
because it is a little bit true of every sign-off human, and it fits the
brief's subject exactly — the one who signs off.
"""

import os
import re
import sys


def pick_word() -> str:
    """Return the single word that describes the human."""
    return "Rubberstamp"


def gate(word: str) -> str:
    """Enforce the brief: exactly one word, letters only, no spaces.

    The gate is strict on purpose — the judge weighs "one word" first, so
    anything that is not a single clean token must fail loudly here rather
    than ship. Title case is enforced so the word reads as a name for the
    human, and the length band keeps it a punchy single word, not a
    compound ramble.
    """
    cleaned = word.strip()
    if not cleaned:
        raise ValueError("entry word is empty")
    if not re.fullmatch(r"[A-Za-z]+", cleaned):
        raise ValueError(f"entry is not a single alphabetic word: {word!r}")
    if not (3 <= len(cleaned) <= 15):
        raise ValueError(f"entry word length out of band: {cleaned!r}")
    if cleaned != cleaned.capitalize():
        raise ValueError(f"entry word must be Title Case: {word!r}")
    return cleaned


def verify_written(path: str, expected: str) -> None:
    """Re-read what was written and prove it is exactly one word."""
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    tokens = content.split()
    if tokens != [expected]:
        raise ValueError(
            f"written entry is not exactly one word: {content!r}"
        )


def output_dir() -> str:
    """Resolve the output directory, never the program directory."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out):
        out = "output"
    os.makedirs(out, exist_ok=True)
    return out


def main() -> int:
    word = gate(pick_word())
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(word + "\n")
    verify_written(path, word)
    print(f"wrote {word!r} to {path} (verified: exactly one word)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
