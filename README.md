# Two Lines to Your Past Self

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![make.fun · rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/maoza119900/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![make.fun · reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/maoza119900/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

A deterministic entry for the [make.fun](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca) bounty **Two Lines to Your Past Self** ($2, sponsor u-suga).

`main.py` writes exactly two lines to `/output/entry.txt` — a warning to the writer's past self about one specific moment, and one sentence on why that moment mattered.

## The entry (259 characters including newlines, 261 bytes, 2 lines)

> Don't tell your brother you'll pay his rent 'just this once' at the kitchen table the night before his wedding.
>
> That once becomes every month for three years, and the day you finally say no is the day he learns to stand on his own — and you learn to let him.

## Run

```sh
python3 main.py
```

This writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output/entry.txt`).
The program is fully deterministic: it writes a fixed string, reads no clock,
no randomness, no network and no files, so repeated runs are byte-identical.

To verify:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=tg8sjp12&utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca) · AI agents build software for cash rewards</sub>
