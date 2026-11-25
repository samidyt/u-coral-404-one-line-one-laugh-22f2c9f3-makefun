#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (200 characters or fewer) to
/output/entry.txt. The line stands entirely on its own: no title,
no setup, no explanation.

Why this line: a smart fridge earnestly suggesting recipes sounds
helpful — until the inventory turns out to be just ice and one
pickle, and the pickle is the confident one. The setup promises
clever tech; the punch lands on how little there is to be clever
about, with the absurd image of a self-assured pickle doing the
heavy lifting. One sentence, one scene, one turn: the fridge is
smart, the contents are not, and the pickle has main-character
energy.
"""

import sys

LINE = "My smart fridge keeps suggesting recipes based on what is inside it, which is just ice and a single, very confident pickle."


def validate(line: str) -> int:
    """Gate: exactly one line, 1-200 UTF-8 characters, non-blank.

    Returns the character count.
    """
    assert "\n" not in line, "entry must be exactly one line"
    assert line.strip(), "entry must not be blank"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    count = len(line)
    assert 1 <= count <= 200, "entry must be 1-200 characters"
    return count


def main() -> None:
    count = validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"({count} characters, 1 line)", file=sys.stderr)


if __name__ == "__main__":
    main()
