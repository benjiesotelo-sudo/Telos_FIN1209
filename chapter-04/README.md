# Chapter 4 - Market Phase Analysis

46 slides, nine parts, 8 in-class checks carrying 16 multiple choice items,
6 terms, and 19 of the book's 32 figures. No charts of our own.

**This chapter is a trial of a much leaner deck.** Chapters 1 to 3 run to
about 200 slides each. The instructor asked for the fewest slides from which
the chapter can still be learned and taught properly, with no length set in
advance, and this is the answer for Lim's Chapter 4.

One document ships, and it is for one person:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-04.pptx` | The instructor | The committed deck, teaching edition. A placeholder where each of the book's figures goes. | `build/content_chapter04.py` |

**There is no student edition, no lecture notes, no run card, no answer sheet
and no check audit for this chapter**, on purpose: the trial is of the deck.
The answers are on the check slides themselves, so an answer sheet would
repeat them. If the lean shape is kept, those documents are the next step,
and `TEMPLATE.md` says what they would need.

## What changed in shape, and what did not

| Chapters 1 to 3 | Chapter 4 |
|---|---|
| Six parts, the template's own convention | Nine parts, the book's sections 4.1 to 4.9. Section 4.10 is the book's summary and feeds the closing slides. |
| A divider slide and a recap slide for every part | Neither. The first slide of a part carries the book's section number in its title, and the last check of a part is its recap. |
| A check is a question slide and a reveal slide | A check is one slide. Each answer is a gold strip on its own question card, hidden until its click. |
| A figure is a slide of its own, after the slide that needs it | A figure sits beside the idea it shows, on the same slide |
| Every figure in the chapter is placed | One figure for each point. Where several make the same point, one is used: 19 of 32. |
| Two objectives slides and a roadmap slide, generated | One of each, written in the content module |

What did not change: one idea per slide, six body lines at the most, every
term taught plain words first and the book's own definition last, nothing
taught that the book does not teach, every check answerable from slides that
come before it, no slide that refers back to a check, the answer key spread
across A to D, and no em dash anywhere. The build still refuses a deck that
breaks any of the rules it can check.

## Which sections are taught in full, and which are kept light

Most of Chapter 4 previews tools that later chapters of the book teach. A
light section says what the book's section says about market phase and
leaves the tool to its own chapter.

| Section | Treatment | Slides | Why |
|---|---|---|---|
| 4.1 Dow theory of market phase | **Full** | 13 | The chapter's own material: the phases, who is on each side, and when a consolidation is over |
| 4.2 Chart pattern interpretation | **Full** | 12 | The chapter's own material: consolidation patterns, and intrinsic and extrinsic bias |
| 4.3 Volume and open interest | Light | 3 | Chapter 6 teaches both |
| 4.4 Moving averages | Light | 2 | Chapter 11 |
| 4.5 Divergence and momentum | Light | 1 | Chapter 9 |
| 4.6 Sentiment | Light | 2 | Chapter 23 |
| 4.7 Sakata's interpretation | **Full** | 4 | The chapter's own material, and the Eastern half of one learning objective |
| 4.8 Elliott's interpretation | Light | 1 | Chapter 18 |
| 4.9 Cycle analysis | Light | 2 | Chapter 20 |

The other six slides are the title, the objectives, the roadmap and three
closing slides.

## How long the chapter takes

**85 minutes at the calibrated rate**, against 219 for Chapter 3. That is
information, not a target: nothing was cut to reach it.

The rate is the one written down in `chapter-03/README.md`: a content slide
1, a term 1.25, a figure 0.75, a check with its reveal 2.5, each opening and
closing slide 1, all scaled by 1.150 into minutes. The two new slide types
are costed as the sum of what they merge, because putting two things on one
slide saves a click and not the talking:

- a check that reveals on its own slide is still 2.5;
- a picture beside a teaching slide is 1 + 0.75, and beside a term 1.25 + 0.75;
- there are no dividers and no recaps, so that weight is zero.

| Part | Slides | Minutes |
|---|---|---|
| Title, objectives, roadmap | 3 | 3.5 |
| 4.1 Dow | 13 | 22.4 |
| 4.2 Chart patterns | 12 | 22.4 |
| 4.3 Volume | 3 | 6.0 |
| 4.4 Moving averages | 2 | 4.9 |
| 4.5 Divergence | 1 | 2.0 |
| 4.6 Sentiment | 2 | 4.9 |
| 4.7 Sakata | 4 | 8.3 |
| 4.8 Elliott | 1 | 2.0 |
| 4.9 Cycles | 2 | 4.9 |
| Closing | 3 | 3.5 |

The weights sum to 73.75 and 73.75 times 1.150 is 84.8. If every slide were
costed as one slide of an existing type, with nothing added for the picture
beside it, the same deck would come to 68 minutes; the honest figure is the
higher one. The rate was calibrated on a full length deck, so how well it
holds for a deck this dense is one of the things the trial will show.

## Building it

```
.venv/bin/python build/build_chapter4.py
```

That writes the committed deck, a placeholder where every figure goes. It is
deterministic: a second run leaves `git status` clean.

The deck the instructor reads has the book's artwork in it and must be
written outside the repository. The PDF is the copy for an iPad, where the
click to reveal does not run; a PDF shows every slide in its final state, so
each check appears with both answers showing.

```
.venv/bin/python build/build_chapter4.py \
    --with-figures --out ~/FIN1209-Chapter-04-with-figures-and-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-04-with-figures-and-charts.pptx
```

Before committing the deck, confirm it embeds no artwork. This chapter draws
no charts, so the list must be empty:

```
unzip -l chapter-04/FIN1209-Chapter-04.pptx | grep -c ppt/media    # 0
```

The deck with the artwork in it holds 19 images, one for each figure placed.

Then look at it. Convert the figure build and view every page, because that
is the build the instructor reads:

```
pdftoppm -r 80 -png ~/FIN1209-Chapter-04-with-figures-and-charts.pdf /tmp/ch4/p
```

## The two new slide types

Both are in `build/deckkit.py`, added beside the renderers the earlier
chapters use and without changing any of them. All six earlier decks, both
editions of Chapters 1 to 3, rebuild byte for byte with them in place.

**`InlineCheck`** is a `Check` that renders as one slide. Each question card
ends in a gold strip carrying the answer letter and the one line reason. The
strips are hidden until clicked, one click each, so the room still answers
before it sees anything. It is a `Check` in every other way: two questions,
the answer key rules, and a student edition would drop it.

**`Pair`** puts an ordinary `Content` or `Term` on the left and an ordinary
`Figure` or `Chart` on the right. The two parts keep their own types, so a
book figure keeps the Wiley credit line and a placeholder in the committed
build, exactly as it does on a slide of its own. `text_w` sets the width of
the text column; widen it for a long definition beside a simple diagram. The
build measures the text column the same way the renderer draws it and
refuses a pair whose text would run past the safe bottom.

Three options on `Chapter` shape the frame around the parts: `openers`
replaces the generated objectives and roadmap slides, `title_notes` replaces
the generated title cues, and `dividers=False` drops the divider slides. A
`Section` with no `recap` renders no recap slide. Left alone, all four give
the frame the earlier chapters have.

`build_chapter4.py` also checks the closing slides against the page on every
build. `deckkit` does not, for any chapter; `AGENTS.md` records that trap.

## `assets/figures/`

Gitignored, and never committed. The build looks for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-4-01.png    ->    Figure 4.1
assets/figures/figure-4-32.png    ->    Figure 4.32
```

The 19 figures the deck places are 4.1 to 4.6, 4.8, 4.11, 4.12, 4.15 to
4.17, 4.21, 4.22, 4.25 to 4.28 and 4.31.

The book PDF embeds all 32 as one image each on PDF pages 126 to 149, so
`pdfimages -png -f 125 -l 150` on the course text yields 32 files. **They
are not all in figure order.** The three images on PDF page 147 come out as
4.28, 4.29, 4.27, so the 27th, 28th and 29th files have to be renamed by
what they show: the Elliott wave structure is 4.28, the weekly gold chart is
4.29, and Dow's three phase market drawn with Sakata's pieces is 4.27. Every
other page is in order.

## Why no charts of our own

A chart earns its place only where the book asserts something that none of
its own figures shows. Chapter 4 has 32 figures in 26 pages, most of them
schematics drawn to make exactly the point the text makes, and every term
the deck teaches already has one beside it. `build/charts_chapter04.py`
holds the empty list and the reasoning.

## Where the book is silent or contradicts itself

Every one of these is named on a slide, and no check rests on any of them.

**Consolidation is never defined in one place.** Review question 1 asks for
the definition. The term slide joins the book's sentence in 4.1, that there
are only two basic phases, with its sentence in 4.2, on how a market
consolidates, and the speaker cue says that is what was done.

**Broadening formations are filed two ways.** The book's list of patterns
that are bullish with respect to an uptrend includes broadening formations.
Its next paragraph says broadening, diamond and island formations are
regarded as reversal formations whose bias disagrees with the trend, and its
own Figure 4.5 files them under distribution in an uptrend. The slide says
so and teaches the paragraph.

**The abc correction is given to both consolidations.** The book says the
accumulation phase includes the abc correction "in most cases" and, in the
next sentence, that distribution is "usually" the abc correction. The slide
says both.

**Names the chapter uses and never teaches.** The shapes of the chart
patterns; open interest; whipsaws; divergence, MACD and RSI; the thirteen
sentiment indicators; Elliott's rules; how a cycle is found; price based
volume; and the inertial characteristics its own learning objectives
promise, a word the text never uses. One closing slide collects them with
the chapter each belongs to and says that only what each tool says about
market phase is examinable from this chapter.
