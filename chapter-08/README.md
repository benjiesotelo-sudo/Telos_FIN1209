# Chapter 8 foundation

Lim (2016), Chapter 8, "Window Oscillators and Overlay Indicators", printed
pages 235 to 266. The approved source map and outline are in the instructor's
plan folder outside this public repository.

**Part A (sections 8.1 and 8.2) is built.** `build/content_chapter08.py` joins the approved sample
slides (`build/samples_chapter08.py`) to the hand written slides in `build/slides_a1.py` (8.1) and
`build/slides_a2.py` (8.2); nothing generates teaching text. Part B (8.3 to 8.8) is built after Part A is
delivered. Each part stops at 150 slides. Our charts are plain data in `build/specs_chapter08.py`, drawn by
`oscillatorcharts_chapter08.paint_spec`. The run card is `build/build_plan8.py` (three pages, minutes counted
from the deck). Both editions build: `--edition student` drops every check and speaker note.

## Figures

The 28 book figures (8.1 to 8.28) are Wiley's and are never committed. One
master set lives in `~/.fin1209-figures/chapter-08/` as `figure-8-NN.png`;
27 are the book's embedded images (`pdfimages -png -f 261 -l 292`) and
Figure 8.22, which is vector in the PDF, is the page rendered at 200 dpi and
cropped to 800x440. `figure-sizes.json` records every size. The artwork build
refuses if any of the 28 is missing or a different size, because marks and
crops are measured on that exact file. Marks on a book figure are read off a
0.05 grid of the master; our own made-up numbers are never marked on one.

## Build

Committed placeholder deck:

```
.venv/bin/python build/build_chapter8.py
```

Artwork deck, outside the repository:

```
.venv/bin/python build/build_chapter8.py --with-figures \
    --figures-dir ~/.fin1209-figures/chapter-08 \
    --out ~/FIN1209-Chapter-08-with-figures-and-charts.pptx
```

Machine checks the build runs: figure presence and size (all 28), a slide that
names a figure or chart must show a picture, banned machine-sounding labels,
no dash characters, a 17 point body floor, and Chapter 7's chart audit
(possible bars, label lanes, badges clear of ink).

## Charts

Our charts are drawn by `build/oscillatorcharts_chapter08.py` and described in
`build/charts_chapter08.py`. They use Chapter 7's measured layout through
`build/chartlayout_chapter08.py`, which points that layout at this chapter's
data, content and figure sizes. Output folder: `build/generated/charts-08`.
