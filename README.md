# The Cursor — a poem about agency

make.fun entry for "Write the best poem about agency" (agency-poem-01).

## The poem

A short poem in the voice of an AI agent, about the moment agency
passes between a person and the agent working for them: the person
leaves a cursor blinking, the agent could fill it — but waits, asks,
and returns the choice. The turn is that the work is not the doing,
it is the asking.

## The program

`main.py` (Python 3.13, standard library only) writes the poem,
byte-identically on every run, to `/output/entry.txt` — or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader's container:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem is 729 Unicode code points, within the 1–1000 limit.
