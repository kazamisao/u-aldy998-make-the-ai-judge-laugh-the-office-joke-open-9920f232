# Make the AI Judge Laugh: the Office Joke Open — entry (Python 3.13, stdlib only).
# The program writes one single-line office joke, at most 200 characters,
# to /output/entry.txt. No network, no randomness, no file reads besides
# this one: two runs write byte-identical output.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

_OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

JOKE = (
    "Our office printer is brilliant at networking \u2014 it introduces "
    "itself to every laptop, then jams with all of them at once."
)

assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
assert "\n" not in JOKE, "joke must be a single line"
assert JOKE == JOKE.strip(), "no leading/trailing whitespace: every char counts"

os.makedirs(_OUT, exist_ok=True)
with open(os.path.join(_OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)

# Gate self-check: re-read what was written and prove it is exactly the joke.
with open(os.path.join(_OUT, "entry.txt"), encoding="utf-8") as f:
    written = f.read()
assert written == JOKE, "entry.txt differs from JOKE"
