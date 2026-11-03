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

### Introduction

What we look for, how we test, and what this channel will never do.

| Notebook | Video | Published |
|---|---|---|
| [`02_what_we_look_for`](notebooks/introduction/02_what_we_look_for.ipynb) | [What a Real Trading Edge Looks Like (It's Smaller Than You Think)](https://youtu.be/VMEAh_eI2Cw) | 2026-10-31 |
| [`03_why_systematic`](notebooks/introduction/03_why_systematic.ipynb) | [Why I Test Trading Ideas With Rules, Not Charts](https://youtu.be/jBQ1JV3Vjy0) | 2026-11-03 |

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
