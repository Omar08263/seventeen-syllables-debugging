"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
at most 200 characters) to /output/entry.txt.

Deterministic: the same bytes on every run.
Standard library only, no network, no randomness.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "code that worked at noon won't run.\n"
    "Nothing changed. I did.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    # Read-back check: fail loudly on any difference.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        assert f.read() == HAIKU, "read-back mismatch"


if __name__ == "__main__":
    main()
