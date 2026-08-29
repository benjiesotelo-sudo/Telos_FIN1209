# Chapter 1 - Introduction to the Art and Science of Technical Analysis

209 slides, six parts, 25 in-class checks carrying 50 multiple choice items,
and 31 figure slides from the course text.

| File | What it is |
|---|---|
| `FIN1209-Chapter-01.pptx` | The committed deck. **Text version**, placeholders where the figures go. |
| `in-class-checks.md` | The instructor's answer sheet, generated with the deck. |
| `lecture-notes.md` | Written by hand. Not generated. |

## Two decks, and why

The chapter's figures are Wiley's, reproduced from Lim, *The Handbook of
Technical Analysis* (Wiley, 2016). This repository is public, so the artwork
is not in it: `assets/figures/` is gitignored and is absent on a clean clone.

That gives two builds of the same 209 slides. Same content, same slide count,
same progress markers, same checks in the same order. The only difference is
what sits in the figure band.

**The committed deck - text version, placeholders.** This is what is in the
repository, and it is what a plain build produces on any machine:

```
.venv/bin/python build/build_chapter1.py
```

Each figure slide keeps its title, its figure number, a line saying what the
figure shows, the credit line, and the speaker cue. Nothing is lost except the
artwork itself, so the chapter stays readable and rebuildable by anyone.

**The teaching deck - figures included.** This is the one to present from. It
needs `assets/figures/` populated with the artwork, and it must be written
outside the repository:

```
.venv/bin/python build/build_chapter1.py \
    --with-figures --out ~/FIN1209-Chapter-01-with-figures.pptx
```

Figures are off by default, and the build refuses `--with-figures` pointed at
the committed path. That is deliberate: the copyrighted artwork must never
reach a commit, and the plain build has to keep reproducing the committed deck
byte for byte.

## `assets/figures/`

Gitignored, and never committed. The build looks for one PNG per figure, named
by the book's own figure number:

```
assets/figures/figure-1-09.png    ->    Figure 1.9
assets/figures/figure-1-21.png    ->    Figure 1.21
```

The 31 figures the chapter places are 1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8,
1.9 through 1.21, 1.25, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34
and 1.35. A missing file is not an error: that slide renders as a placeholder
and the rest of the deck is unaffected. Every build prints how many figures it
placed and names the ones it did not.

## The figures that carry the most weight

Part 4 runs Figures 1.9 to 1.15 as a sequence, one to a slide. It is the same
price chart seven times: bare, then trendlines, moving averages, chart
patterns, regression with divergence, regression with volume, and finally
volatility bands with volume and MACD. Do not summarise it and do not skip
ahead. The room has to watch one chart get read seven defensible ways, because
that sequence *is* the argument that analysis is subjective. Everything else in
Part 4 depends on the room having seen it happen.

## Smoke test

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-01/FIN1209-Chapter-01.pptx
```
