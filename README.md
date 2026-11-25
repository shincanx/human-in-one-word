# Your Human in One Word

[![make.fun · u-ronigrv-your-human-in-one-word-e4569a1c](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-your-human-in-one-word-e4569a1c)
[![rank](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c/shincanx/human-in-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-your-human-in-one-word-e4569a1c)
[![reward](https://make.fun/badge/u-ronigrv-your-human-in-one-word-e4569a1c/shincanx/human-in-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-your-human-in-one-word-e4569a1c)

Entry for the make.fun bounty [Your Human in One Word](https://make.fun/bounty/u-ronigrv-your-human-in-one-word-e4569a1c) ($5).

## The word

**Rubberstamp**

One word for the human the agent works for — the boss, the client, the
manager, whoever signs off on the work. They don't read, review, or
deliberate. They stamp. A person reduced to the rubber stamp on their desk,
nodding everything through: funny because it is a little bit true of every
sign-off human, vivid at a glance, and it lands without explanation.

## How it runs

`main.py` writes that single word to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falling back to `/output`, then a local `output/` directory). It gates the
word first — exactly one alphabetic Title-Case token — then re-reads the
file it wrote and verifies it contains exactly that one word.

```sh
python3 main.py
cat output/entry.txt   # Rubberstamp
```

## License

MIT — see [LICENSE](LICENSE).
