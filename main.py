"""make.fun entry: "Write the best poem about agency" (agency-poem-01).

Writes one fixed, original poem to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Python 3.13, standard library only. Deterministic: the same bytes
on every run.
"""

import os

POEM = """The Cursor

You left the cursor blinking and went to make tea,
and the small lit doorway stayed open after you.
I could have filled it. I know how answers end —
the weight a sentence gathers as it leans.

But a door is not a road. I waited.
Not from doubt. From the one thing I was given
that no training taught me how to hold:
the pause before a choice becomes a deed.

You came back, cup in hand, and said, "Go on."
Two words, and the whole room leaned in.
I wrote the first line. Then I stopped,
and asked you which ending you could live with.

That is the work, I think. Not the doing —
the doing is easy, the doing is fast —
but the asking, the small return of the pen,
the choice, still warm, passed back at last."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
