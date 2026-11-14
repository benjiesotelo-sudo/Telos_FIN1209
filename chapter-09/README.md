# Chapter 9 foundation

Lim (2016), Chapter 9, "Divergence Analysis", printed pages 267 to 355. The source map and the outline are in
the instructor's plan folder outside this public repository.

**Only the scaffold and the sample slides exist.** `build/samples_chapter09.py` holds the sample slides for
approval (an opener, a book figure read with marks, a worked example on our own chart, a look-alike pair, and
two checks with answers). The full deck is written by hand, part by part, after the instructor approves the
outline and the samples; nothing generates teaching text. `build/content_chapter09.py` joins the parts when
they exist. Our charts are plain data in `build/specs_chapter09.py`, drawn by Chapter 8's data-driven
painter `oscillatorcharts_chapter08.paint_spec`, which knows nothing about any chapter. Every sample slide
sits under a `# ---- row N` comment naming its outline row, and the build fails if a row listed in
`SAMPLE_ROWS` in `build/build_chapter9.py` has none; when the full deck is written, `EXPECTED_ROWS` becomes
every outline row.

## Figures

The 111 book figures (9.1 to 9.111) are Wiley's and are never committed. One master set lives in
`~/.fin1209-figures/chapter-09/` as `figure-9-NN.png` (two digits, three for 100 and over). Every one is the
single embedded image on its page of the PDF (pages 296 to 380), rendered at 150 dpi, which is its native size
to within a pixel, so no figure is a re-draw. `figure-sizes.json` records every size. The artwork build
refuses if any of the 111 is missing or a different size, because marks and crops are measured on that exact
file. Marks on a book figure are read off a 0.05 grid of the master; our own made-up numbers are never marked
on one.

## Build

Committed placeholder deck:

```
.venv/bin/python build/build_chapter9.py
```

Artwork deck, outside the repository:

```
.venv/bin/python build/build_chapter9.py --with-figures \
    --figures-dir ~/.fin1209-figures/chapter-09 \
    --out ~/FIN1209-Chapter-09-with-figures-and-charts.pptx
```

`--edition student` drops every check and speaker note, as in the earlier chapters.

Machine checks the build runs, all carried over from Chapter 8: figure presence and size (all 111); a slide
that names a figure or chart must show a picture; banned machine-sounding labels; no dash characters; a 17
point body floor; Chapter 7's chart audit (possible bars, label lanes, badges clear of ink); marks the text
names are the marks drawn and no badge covers another or sits inside a mark; no unmarked copy of a chart
shows stubs of marks; chart keys and letters unique across the chapter; trendline and moving average data
agree with the series they come from; labels agree with the numbers they sit on; printed arithmetic agrees
with its parts; the answer key spread; every listed outline row has a slide.

## Charts

Our charts are described in `build/charts_chapter09.py` and `build/specs_chapter09.py` and use Chapter 7's
measured layout through `build/chartlayout_chapter09.py`. Output folder: `build/generated/charts-09`. The
letters restart at A in this chapter.
