#!/usr/bin/env python3
"""One-star review of a human, written by the house cat who employs him.

Entry for make.fun's "Make the AI Judge Laugh: Cat Reviews Its Human"
bounty. The program writes a single line of text to /output/entry.txt,
which a judge model compares head to head against other entries.
"""

import os

ENTRY = (
    "One star. My bowl is refilled only when empty, the bedroom door shuts "
    "in my face nightly, and he spends all day sitting on my warm laptop. "
    "He calls himself my owner. I pay rent in mice, unthanked."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
