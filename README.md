# QuantWall

**NO BLACK BOXES · NO HYPE**

Quantitative trading research in the open: how to test a trading idea so you stop fooling yourself.
This repository holds the free notebooks behind the QuantWall videos, plus the channel's brand kit.

- YouTube: https://www.youtube.com/@quantwall
- Contact: hello@quantwall.org
- Website: https://quantwall.org (domain registered; site not built yet)

> Education only. Not financial advice. Every number is computed from seeded, synthetic data. See [DISCLAIMER](DISCLAIMER.md).

## How the notebooks work

- One notebook per video. A notebook is added on the day its video is published, so everything listed here is already out.
- Each notebook reproduces every number shown in its video from a seeded simulation. Change an input and see how the conclusion moves.
- No market data, no signals, no strategy. The notebooks teach the method, not a trade.
- Outputs are stripped, so you run each notebook yourself and see your own numbers.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt jupyterlab
jupyter lab
```

## Index

### Start here

Short videos for the words the channel uses all the time.

| Notebook | Video | Published |
|---|---|---|
| [`s1_what_a_backtest_is`](notebooks/start-here/s1_what_a_backtest_is.ipynb) | [228 Trades, 228 Winners. What a Backtest Really Is](https://youtu.be/_XfqFv38_Co) | 2026-11-13 |

### Introduction

What we look for, how we test, and what this channel will never do.

| Notebook | Video | Published |
|---|---|---|
| [`02_what_we_look_for`](notebooks/introduction/02_what_we_look_for.ipynb) | [What a Real Trading Edge Looks Like (It's Smaller Than You Think)](https://youtu.be/VMEAh_eI2Cw) | 2026-10-31 |
| [`03_why_systematic`](notebooks/introduction/03_why_systematic.ipynb) | [Why I Test Trading Ideas With Rules, Not Charts](https://youtu.be/jBQ1JV3Vjy0) | 2026-11-03 |
| [`04_why_trust_this_channel`](notebooks/introduction/04_why_trust_this_channel.ipynb) | [I Made a "Perfect" Trading Channel From Pure Noise](https://youtu.be/eg9IdHXK5oU) | 2026-11-06 |
| [`05_the_map`](notebooks/introduction/05_the_map.ipynb) | [Two Backtests, Both Wrong: What Happens Before (and After) the Test](https://youtu.be/kfYqeTbW9ho) | 2026-11-10 |

### AI

What happens when an AI helps you test an idea.

| Notebook | Video | Published |
|---|---|---|
| [`57_ai_desk_on_noise`](notebooks/ai/57_ai_desk_on_noise.ipynb) | [We Fed a Viral "AI Trading Desk" Fake Markets. It Approved 42 Trades.](https://youtu.be/cr0yMdmxPV0) | 2026-11-12 |

## Repository layout

| Path | What it is |
|---|---|
| `notebooks/` | One notebook per published video, grouped by section |
| `brand/` | Logo, avatar, banner, colours, type, channel text and templates |
| `scripts/check.py` | The checks every notebook must pass |
| `DISCLAIMER.md` | Full legal disclaimer |
| `LICENSE` | MIT |

## Licence

Code and notebooks are MIT licensed. The QuantWall name, logo and channel artwork are not: please ask before reusing them.
