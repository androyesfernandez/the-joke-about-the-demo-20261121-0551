#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write this entry's one-line demo joke to a text file.

The joke is the whole entry: a rehearsal that went perfectly, a live
demo that fell over in four seconds, and an incident report blaming
the audience. The program takes no arguments and prints nothing; it
just drops the joke into entry.txt under the output directory.
"""
import os

# The joke, built from its two beats: the setup, then the report that
# delivers the punchline. Kept as one line of exactly 150 characters.
SETUP = "The rehearsal was flawless; the live demo crashed in four seconds."
REPORT = "My agent's incident report was one line:"
PUNCH = "\u201cThe audience was an unhandled edge case.\u201d"

JOKE = f"{SETUP} {REPORT} {PUNCH}"


def main():
    """Write the joke to entry.txt under the output directory."""
    target = os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as out:
        out.write(JOKE)


if __name__ == "__main__":
    main()
