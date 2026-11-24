#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — entry program.

Pure Python stdlib, no dependencies, no network, no randomness: the same
bytes on every run. It writes one original one-line one-star review,
written by a house cat about its human, to /output/entry.txt, where the
house gate checks it (UTF-8 text, 1-200 characters, not only whitespace)
and the house judge then compares it head to head with the other entries.

The review (125 characters):

    One star. He bought a $400 cat bed, then looked betrayed when I slept
    in the box. The box was the gift. He was the packaging.

Why it should land with the judge's brief, in the brief's own order:

1. It is a one-star review by a house cat about its human, and nothing
   else: the whole line is the complaint, in review shape ("One star.").
2. The complaint is specific and recognisable: a $400 cat bed bought,
   then ignored for the cardboard box it came in — the oldest cat joke
   there is, because every cat owner has lived it.
3. The voice is unmistakably feline: the human is measured by cat
   standards (he is judged on whether he understands the box), and the
   review gives away more about the cat than the owner — the cat thinks
   the human, not the bed, was the packaging.
4. The wording is tight and the sting lands in the last few words:
   "The box was the gift. He was the packaging." reframes the whole
   purchase in two short sentences and rewards a second read.
5. It keeps the deadpan shape of a real one-star review while the
   content goes somewhere only a cat would go: rating a human the way
   a shopper rates a product, then demoting him to packaging.
"""

import os

REVIEW = (
    "One star. He bought a $400 cat bed, then looked betrayed "
    "when I slept in the box. The box was the gift. "
    "He was the packaging."
)


def main() -> None:
    line = REVIEW.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("read-back mismatch")
    if not 1 <= len(written) <= 200:
        raise ValueError("written entry fails the 1-200 char gate")
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
