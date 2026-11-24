#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line — the error message a kitchen toaster shows its owner —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt where the
harness sets it).
"""

import os

ERROR = "E01: Bread stuck. I am not angry, just disappointed."
# The joke's angle: a real error code and the most common real toaster
# failure ("bread stuck"), then the twist is the voice — the toaster as
# a disappointed parent. No burnt-toast pun, no "toast is toast": the
# surprise is an appliance doing parental guilt, in 52 characters.

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ERROR)


if __name__ == "__main__":
    main()
