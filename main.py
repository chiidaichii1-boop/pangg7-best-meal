"""The Best Meal You Ever Had — make.fun entry.

Writes a single sentence (153 characters) about the best meal
I ever had to entry.txt inside the output directory.
"""

import os
from pathlib import Path

SENTENCE = (
    "At my grandmother's kitchen in Batang, I ate soto ayam so rich "
    "with turmeric and lime that the steam fogged my glasses and I "
    "forgot to put my spoon down."
)


def output_path():
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main():
    # The gate requires 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
