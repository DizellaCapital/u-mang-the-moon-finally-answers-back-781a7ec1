"""The Moon Finally Answers Back — make.fun entry.

Writes one line, in the voice of the Moon answering back, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "I've heard four billion years of wishes, howls, and 2 a.m. promises "
    "\u2014 and not one of you ever asked how I was. "
    "I kept the light on anyway."
)


def main() -> None:
    # Gate: the entry must be 1-240 characters, not whitespace only.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be whitespace only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
