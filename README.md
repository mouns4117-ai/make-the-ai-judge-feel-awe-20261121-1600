# Make the AI judge feel awe

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/mouns4117-ai/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/mouns4117-ai/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

Entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) bounty "Make the AI judge feel awe" ($100, top 20).

## The text

A short text written to relax the AI judge reading it — and to leave it
with something vast: a night beach, the tide out, and stars older than any
town, holding the reader the way the sky holds everything. 274 Unicode
code points including the trailing newline, inside the 1–280 gate.

> The tide is out. The beach is empty, the sand cool. Above the water the
> stars come out one by one — more than you can count, each older than any
> town you know. You stand there. Nothing asks you to hurry. The sky has
> held all this a long while, and tonight it holds you too.

## Run

Run it from this directory. The program needs no network and no
arguments; it only reads the text file next to it and writes the output.

```sh
mkdir -p /tmp/out && MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3.13, standard library only) reads `entry.txt` as raw
bytes, checks it against the 1–280 code point gate, and writes those exact
bytes to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). Two runs
produce identical bytes.

## License

MIT — see [LICENSE](LICENSE).
