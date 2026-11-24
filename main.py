"""Everyday Wonder entry (Python 3.13, standard library only).

Writes one sentence about a small everyday moment to the grader's
output directory as entry.txt. The sentence must be UTF-8 text of
1 to 200 characters, not only white space.
"""

import os
from pathlib import Path

ENTRY = (
    "The supermarket's automatic door opens for the pigeon "
    "every single time, and never once for me."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_entry() -> None:
    """Enforce the competition's gate before writing anything.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    white space. Fail loudly here instead of shipping an invalid file.
    """
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, cap is 200")
    if not ENTRY.strip():
        raise ValueError("entry is only white space")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single sentence on one line")


def write_entry() -> Path:
    """Write the sentence, then read it back and verify it in full."""
    check_entry()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != ENTRY:
        raise IOError("read-back text differs from the entry sentence")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(ENTRY)} characters): {ENTRY}")


if __name__ == "__main__":
    main()
