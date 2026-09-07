# Chapter 3 - Mechanics and Dynamics of Charting

188 slides, six parts, 23 in-class checks carrying 46 multiple choice items,
39 terms, 40 figures from the course text, and 6 charts drawn for this
course. It ships in two editions: the teaching edition at 188 slides, and the
student edition at 142, which is the same deck without the checks, the
reveals and the speaker notes.

Four documents come out of the same chapter data, and they are for three
different people:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-03.pptx` | The room | The committed deck, teaching edition. Placeholders where the book's figures go; our own six charts are really in it. | `build/content_chapter03.py` |
| `FIN1209-Chapter-03-Student-Edition.pptx` | The students | 142 slides. The same deck with the checks, the reveals and the speaker cues removed. | `build/content_chapter03.py` |
| `FIN1209-Chapter-03-Run-Card.pdf` | The instructor | 3 pages. Minutes per part, what to cut, and what must never be cut. | `build/plan_chapter03.py` |
| `FIN1209-Chapter-03-Lecture-Notes.pdf` | The students | 32 pages. What the lesson covered, in prose, with the figures and the charts. | `build/lecture_chapter03.py` |
| `in-class-checks.md` | The instructor | The answer sheet. | `build/content_chapter03.py` |
| `check-answerability-audit.md` | The instructor | Whether every check item can be answered from the slides alone. | Written by hand |

**Nothing in this folder is hand-edited except the check audit and this
file.** The two decks, the answer sheet and the two PDFs are all build
output, and the next build overwrites them.

## How long the chapter actually takes

**219 minutes at the calibrated rate, against a 180 minute session.** Chapter
3 is heavier than Chapter 2, mostly because the book gives it forty figures
to Chapter 2's twenty six.

The run card names three cuts, all to be taken before the session starts:

| Cut | What comes out | Minutes | Chapter runs |
|---|---|---|---|
| None | The whole deck | | 219 |
| 1 | Eleven figures that repeat an earlier figure or slide | 10 | 209 |
| 2 | All six charts, and eight slides that restate a neighbour | 12 | 197 |
| 3 | Six checks, each beside another check in the same part | 18 | 179 |

With all three the chapter is one session and nothing is left in reserve. The
card also offers the one clean alternative: **Parts 1 to 5 uncut, with the
openers and the wrap up, are 169 minutes**, and Part 6, futures, is self
contained and can be carried whole to the next session.

The deck was not compressed to reach a number. One idea per slide, plain
words before the formal definition, and a check every few terms are the
instructor's rules and they are not negotiable.

### The rate, written down

Chapter 2's README describes the calibration and does not give the numbers.
They are here so the next chapter can be costed the same way.

Each slide type carries a weight: a content or quote slide 1, a term slide
1.25, a figure 0.75, one of our charts 0.5, a check with its reveal 2.5, and
each part's divider and recap together 1. Each opening slide and each wrap up
slide is 1. The weights are then scaled so that what the room actually got
through on 2026-09-02, Chapter 1's four opening slides and its first four
parts, comes to exactly 180 minutes. The scale factor is 1.150, so in minutes
a content slide is 1.15, a term 1.44, a figure 0.86, a chart 0.58 and a check
2.88.

That model reproduces all six part figures on Chapter 2's run card and its
202 minute total, which is the test that it is the same rate. Applied to
Chapter 3's parts it gives 30, 26, 45, 32, 26 and 50 minutes, with 5 for the
openers and 5 for the wrap up.

## Two editions of the deck, one content file

```
.venv/bin/python build/build_chapter3.py                     # teaching, 188 slides
.venv/bin/python build/build_chapter3.py --edition student   # student, 142 slides
```

The student edition drops all 23 checks and all 23 reveals, which is the 46
slide difference, and carries no speaker notes. Everything else is the same
deck. Only the teaching build writes `in-class-checks.md`.

## The lecture notes and the run card

```
.venv/bin/python build/build_lecture_notes3.py    # students, 32 pages
.venv/bin/python build/build_plan3.py             # instructor, 3 pages
```

**Rebuild both whenever you rebuild the deck.** The deck is the authority on
scope and both PDFs are checked against it. The run card resolves every slide
reference against the deck, so a content change moves the card with it. The
notes resolve every figure number, every chart letter and every term, and
take their summary and review questions straight from the deck's closing
slides.

**The notes take their definitions from the deck too.** Every definition box
in `build/lecture_chapter03.py` is built by `formal()`, which reads the
formal wording off the deck's own term slide, so a term is defined in the
same words in both documents by construction. Chapter 2 retyped them.

**Bold in the notes covers whole sentences.** The paginator moves a bold
element whole and splits text only at a sentence end, so a bold phrase in the
middle of a sentence let a page break fall inside the sentence. The figure
build did exactly that twice before the notes were changed.

## Then look at the PDFs

Every page, as an image. Both builds of the lecture notes, not just one: the
figure build is not the placeholder build with pictures in it.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-03/FIN1209-Chapter-03-Lecture-Notes.pdf /tmp/ln $(seq 1 32)
$DATA/pdfpng ~/FIN1209-Chapter-03-Lecture-Notes-with-charts.pdf /tmp/lnfig $(seq 1 32)
$DATA/pdfpng chapter-03/FIN1209-Chapter-03-Run-Card.pdf /tmp/card 1 2 3
```

## Two builds of everything, and why

The chapter's 40 **figures** are Wiley's, reproduced from Lim, *The Handbook
of Technical Analysis* (Wiley, 2016). This repository is public, so the
artwork is not in it: `assets/figures/` is gitignored and absent on a clean
clone.

The chapter's six **charts** are the opposite case. They are ours, drawn at
build time from `build/charts_chapter03.py`, and they are in every build
including the committed ones.

**The committed versions are the placeholder builds.** The versions with the
artwork placed must be written outside the repository:

```
.venv/bin/python build/build_chapter3.py \
    --with-figures --out ~/FIN1209-Chapter-03-with-figures-and-charts.pptx
.venv/bin/python build/build_chapter3.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-03-Student-Edition-with-charts.pptx
.venv/bin/python build/build_lecture_notes3.py \
    --with-figures --out ~/FIN1209-Chapter-03-Lecture-Notes-with-charts.pdf
```

The first is what the instructor presents from. The last two are what go to
students through Canvas.

Before committing either deck, confirm it embeds no artwork that is not ours:
`unzip -l <deck>.pptx | grep ppt/media` must list exactly six images, and
their hashes must match this chapter's own chart folder:

```
unzip -o -d /tmp/media chapter-03/FIN1209-Chapter-03.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts-03/*.png | awk '{print $1}' | sort)
```

For the notes PDF the same check is `pdfimages -list <pdf>`: six images, all
2274 by 768, and no others.

## `assets/figures/`

Gitignored, and never committed. Both builds look for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-3-01.png    ->    Figure 3.1
assets/figures/figure-3-40.png    ->    Figure 3.40
```

The 40 figures the chapter places are 3.1 through 3.40, complete. The book
PDF embeds each of them as one image, in figure order, on PDF pages 93 to
123, so `pdfimages -png -f 91 -l 124` on the course text yields exactly forty
files that map one to one onto `figure-3-01.png` to `figure-3-40.png`.

The deck places Figure 3.40 before Figure 3.39 on purpose: the book's
schematic of how back adjusting is done teaches the mechanism, and the real
gold chart after it shows the consequence.

## `build/generated/charts-03/`

Gitignored too, because it is build output. Every build of the deck and of
the lecture notes redraws all six PNGs from `build/charts_chapter03.py`
before it starts. Five of the six use chart forms added to
`build/chartkit.py` for this chapter; both editions of Chapters 1 and 2
rebuild byte for byte with them in place.

## Where the book is silent or contradicts itself

Every one of these is named on a slide and in the notes, and no check rests
on any of them.

**Ratio scaling contradicts itself.** The book defines ratio scaling as equal
distances for equal percentage changes, and two sentences later says equal
distances on the chart do not equate to equal percentage changes. The
definition is stated twice and drawn twice; the deck teaches it and names the
stray sentence on its own slide.

**Equivolume has two accounts of its data.** Beside Figure 3.4 the book says
equivolume bars require OHLCV data; in its section on equivolume it says the
bars are built from the high and the low and the open and close are
disregarded. The deck says both and names the difference.

**Figure 3.26 labels a support level resistance.** Its title and the text call
the level support. The deck teaches it as support and says so.

**The long and short rule in the bid-ask section reads wrongly as printed.**
The book says long entries and long exits are hurt on a bid-based chart and
short exits are not, and defines shorting in that section as selling to open
or close a position. Read long as the position rather than the order and the
rule contradicts the book's own example. The deck says to read long as any
buy.

**Names the chapter uses and never teaches.** Gann bars, Kagi charts and Gann
swing charts; the thirteen breadth and sentiment data items; the averaging in
the average true range, which is Chapter 8; support, resistance and
trendlines, which are Chapter 5; the expected spot price that normal contango
needs, with no word on how to estimate it; the 100 dollar threshold for ratio
charts, without saying what it is measured on; a volatility neutral chart,
which is in the learning objectives and never in the text; and a futures
contract, which is never defined. One closing slide collects them and says
none is examinable from this chapter.

## Smoke test

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-03/FIN1209-Chapter-03.pptx
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-03/FIN1209-Chapter-03-Student-Edition.pptx
```
