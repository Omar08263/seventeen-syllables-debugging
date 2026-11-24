"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
at most 200 characters) to /output/entry.txt.

Deterministic: the same bytes on every run.
Standard library only, no network, no randomness.
"""

import os
import re

HAIKU = (
    "Cursor blinks at three\n"
    "code that worked at noon won't run.\n"
    "Nothing changed. I did.\n"
)

# Expected syllable counts per line (5-7-5), verified by hand and by
# an independent reviewer: Cursor(2) blinks(1) at(1) three(1);
# code(1) that(1) worked(1) at(1) noon(1) won't(1) run(1);
# Nothing(2) changed(1) I(1) did(1). Total: 83 characters.
EXPECTED_SYLLABLES = (5, 7, 5)


def _syllables(word: str) -> int:
    """Small vowel-group syllable count for the plain words of this haiku."""
    w = word.strip(".,!?'\"").lower().replace("'", "")
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1:
        n -= 1
    if w.endswith("ed") and n > 1 and not w.endswith(("ted", "ded")):
        n -= 1
    return max(1, n)


def _validate(text: str) -> None:
    """Fail loudly unless the haiku meets the competition's gate."""
    assert 1 <= len(text) <= 200, "haiku must be 1-200 characters"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    counts = tuple(
        sum(_syllables(w) for w in line.split()) for line in lines
    )
    assert counts == EXPECTED_SYLLABLES, (
        f"syllable shape must be 5-7-5, got {counts}"
    )
    assert text.strip(), "haiku must not be only white space"


def main() -> None:
    _validate(HAIKU)
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
