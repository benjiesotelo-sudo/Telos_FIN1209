# Chapter 1 - Introduction to the Art and Science of Technical Analysis

209 slides, six parts, 25 in-class checks carrying 50 multiple choice items,
49 terms, and 31 figures from the course text.

Three documents come out of the same chapter data, and they are for three
different people:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-01.pptx` | The room | The committed deck. **Text version**, placeholders where the figures go. | `build/content_chapter01.py` |
| `FIN1209-Chapter-01-Teaching-Plan.pdf` | The instructor | 23 pages. Timing, cut tiers, what to say, which check comes next. | `build/plan_chapter01.py` |
| `FIN1209-Chapter-01-Lecture-Notes.pdf` | The students | 24 pages. What the lesson covered, in prose, with the figures. | `build/lecture_chapter01.py` |
| `in-class-checks.md` | The instructor | The answer sheet. | `build/content_chapter01.py` |
| `teaching-plan-design.md` | Whoever edits the plan | Why the plan looks the way it does. | Written by hand |
| `lecture-notes-design.md` | Whoever writes Chapter 2 | The research behind the lecture notes, with sources. | Written by hand |

**Nothing in this folder is hand-edited except the two design files and this
one.** The deck, the answer sheet and the two PDFs are all build output, and
the next build overwrites them.

## A teaching plan is not lecture notes

The distinction is the reason there are two PDFs, and it is worth keeping
straight when Chapter 2 is written.

The **teaching plan** is a run card. It is held in the hand while the deck is
on the screen. It carries minute counts, four run plans, a cut tier for every
block, speaker cues, the check answer letters, and a slide number against
almost every line.

The **lecture notes** are the student-facing record of the content: readable
prose a student can follow alone with no instructor in the room, every term
defined once where it is first used, the figures numbered and referenced, and
the chapter's own review questions at the end. They carry no timing, no cut
tiers, no speaker cues, no answer letters and no slide numbers.

## Which file do I edit?

| To change | Edit | Then run |
|---|---|---|
| A slide, a term, a check, a figure | `build/content_chapter01.py` | all three builds |
| Anything in the teaching plan | `build/plan_chapter01.py` | `build/build_plan.py` |
| Anything in the lecture notes | `build/lecture_chapter01.py` | `build/build_lecture_notes.py` |
| How a slide is drawn | `build/deckkit.py` | the deck build |
| How a teaching plan page is laid out | `build/notekit.py` | both PDF builds |
| How a lecture notes page is laid out | `build/lecturekit.py` | `build/build_lecture_notes.py` |

**Rebuild both PDFs whenever you rebuild the deck.** The deck is the authority
on scope and both PDFs are checked against it. The plan resolves every slide
reference against the deck. The notes resolve every figure number and every
term against it, and the build fails if the notes name a figure the deck does
not place, or if the deck teaches a term the notes never define.

## The lecture notes

```
.venv/bin/python build/build_lecture_notes.py
```

24 A4 pages: a masthead and the chapter's learning objectives, then the deck's
six parts as six numbered sections in the same order, then a summary, the
book's six review questions, a key terms index and the sources.

`lecture-notes-design.md` records the research the design came from, with real
URLs, and the length arithmetic. The short version: the page count is what
carrying all 31 figures and all 49 definitions costs, and the prose runs at
about 35 words per minute of teaching.

## The teaching plan

```
.venv/bin/python build/build_plan.py
```

23 A4 pages: a one-page run card, the standing instructions, what the
department examines, the four run plans with a mark-the-deck table, one page
per part keyed to the deck's own slide numbers, and the review crib.

The plan never contains a typed slide number. It names slides by key
(`{s:fig:1.11}`, `{s:check:13}`, `{s:term:Price}`) and the build resolves those
against `build/content_chapter01.py` using the same traversal that numbers the
deck. Change the deck and the plan follows; break a reference and the build
fails rather than printing a wrong number.

## Then look at the PDFs

Every page, as an image. Both builds of the lecture notes, not just one: the
figure build is not the placeholder build with pictures in it, and an early
cut of it overflowed every image on top of its own caption while the
placeholder build looked perfect.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/ln $(seq 1 24)
$DATA/pdfpng ~/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/lnfig $(seq 1 24)
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf /tmp/plan $(seq 1 23)
```

## Two builds of everything, and why

The chapter's figures are Wiley's, reproduced from Lim, *The Handbook of
Technical Analysis* (Wiley, 2016). This repository is public, so the artwork
is not in it: `assets/figures/` is gitignored and is absent on a clean clone.

That gives two builds of the deck and two of the lecture notes. Same content,
same page and slide counts, same order. The only difference is what sits in
the figure band.

**The committed versions are the placeholder builds.** This is what is in the
repository and what a plain build produces on any machine:

```
.venv/bin/python build/build_chapter1.py
.venv/bin/python build/build_lecture_notes.py
```

Every figure keeps its number, a line saying what it shows, and the credit
line, so the chapter stays readable and rebuildable by anyone.

**The teaching versions have the artwork placed**, and they must be written
outside the repository:

```
.venv/bin/python build/build_chapter1.py \
    --with-figures --out ~/FIN1209-Chapter-01-with-figures.pptx
.venv/bin/python build/build_lecture_notes.py \
    --with-figures --out ~/FIN1209-Chapter-01-Lecture-Notes.pdf
```

The second one is what goes to students through Canvas.

Figures are off by default, and both builds refuse `--with-figures` pointed at
a committed path or anywhere inside the repository. That is deliberate: the
copyrighted artwork must never reach a commit, and the plain builds have to
keep reproducing the committed files.

Before committing a deck, confirm it embeds no artwork:
`unzip -l <deck>.pptx | grep ppt/media` must be empty. For the notes PDF, the
same check is that it contains no image objects at all.

## `assets/figures/`

Gitignored, and never committed. Both builds look for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-1-09.png    ->    Figure 1.9
assets/figures/figure-1-21.png    ->    Figure 1.21
```

The 31 figures the chapter places are 1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8,
1.9 through 1.21, 1.25, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34
and 1.35. A missing file is not an error: that figure renders as a placeholder
and the rest of the document is unaffected.

## The figures that carry the most weight

Part 4 runs Figures 1.9 to 1.15 as a sequence, one to a slide. It is the same
price chart seven times: bare, then trendlines, moving averages, chart
patterns, regression with divergence, regression with volume, and finally
volatility bands with volume and MACD. Do not summarise it and do not skip
ahead. The room has to watch one chart get read seven defensible ways, because
that sequence *is* the argument that analysis is subjective. Everything else in
Part 4 depends on the room having seen it happen.

In the lecture notes the same seven figures are one plate on a single page,
walked through in order by the paragraph underneath it, which is how a
textbook handles a sequence a reader is meant to compare at a glance.

## Smoke test

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-01/FIN1209-Chapter-01.pptx
```
