# Chapter 6 - Volume and Open Interest

191 slides, six parts, 19 in-class checks carrying 38 multiple choice items,
26 terms, all 44 of the book's figures, and 53 charts of our own. It ships
in two editions: the teaching edition at 191 slides, and the student
edition at 153, which is the same deck without the checks, the reveals and
the speaker notes.

**This chapter is built to the lean form the instructor approved in Chapter
4**, and to every rule his reviews of Chapter 5 added, from the first build:
the content decides the length, each question is followed by its own answer
slide, every idea that needs a picture has one beside it, and nothing the
book says is cut. `TEMPLATE.md` has the rules and `chapter-05/README.md` the
reviews they came from.

Four documents ship from the same chapter data, and two more are written
outside the repository:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-06.pptx` | The room | The committed deck, teaching edition. Our own charts, and a placeholder where each of the book's figures goes. | `build/content_chapter06.py` |
| `FIN1209-Chapter-06-Student-Edition.pptx` | The students | 153 slides. The same deck with the checks, the reveals and the speaker cues removed. | `build/content_chapter06.py` |
| `FIN1209-Chapter-06-Run-Card.pdf` | The instructor | 3 pages. Minutes per part, the two ways through the chapter, what to cut and what must never be cut. No answers. | `build/plan_chapter06.py` |
| `FIN1209-Chapter-06-Lecture-Notes.pdf` | The students | 51 pages. What the lesson covered, in prose, with every figure and every chart the deck places. | `build/lecture_chapter06.py` |
| `~/FIN1209-Chapter-06-In-Class-Checks (answer sheet).md` | The instructor | The answer sheet. **Not in this repository.** | `build/content_chapter06.py` |
| `~/FIN1209-Chapter-06-Check-Audit.md` | The instructor | Whether every check item can be answered from the slides before it. **Not in this repository.** | Written by hand |

**Nothing in this folder is hand-edited except this file.** The two decks
and the two PDFs are build output, and the next build overwrites them.

**A committed deck is not a teaching deck.** The files here carry a
placeholder where each of the 44 figures goes. The deck to teach from is the
build with the artwork, made outside the repository; see **Building it**.

**The answer material stays out of this public repository**, as for Chapter
4. `build_chapter6.py` writes the answer sheet to the home directory and
refuses a `--checks-out` path inside the repository; only the teaching build
writes it. The audit is written by hand beside it. Its result can be stated
without its answers: **38 items, 38 pass**, every one answered by the text
of a slide that comes before its check, none by a picture, a caption alone
or a speaker cue, and none by a slide the run card's Cut 1 drops.

## The shape

| Chapters 1 to 3 | Chapter 6 |
|---|---|
| Six parts, the template's own convention | Six parts. The book has two sections: 6.1 is thirty pages and twenty sub-headings, so it is Parts 1 to 5, split at its own sub-headings and in its order; 6.2 is Part 6. Section 6.3 is the book's summary and feeds the closing slides. |
| A divider slide and a recap slide for every part | Neither. The first slide of a part carries the book's section number in its title. |
| A picture is a slide of its own, after the slide that needs it | A picture sits beside the idea it shows, on the same slide |
| Two objectives slides and a roadmap slide, generated | One of each, written in the content module |

| Part | Book pages | Slides | Checks | Figures | Our charts | Terms |
|---|---|---|---|---|---|---|
| 1 Confirmation and divergence | 173 to 180 | 31 | 3 | 6.1 to 6.8 | A to I | Volume; bullish and bearish volume; volume divergence and confirmation; bullish and bearish divergence and confirmation; price-based and non-price-based volume oscillators |
| 2 Timing, the VWMA, climaxes | 180 to 186 | 31 | 3 | 6.9 to 6.17 | J to Q | Low volume breakout signal; low volume reversal; VWMA; upper and lower overextended volume levels; low volume top and bottom |
| 3 Barriers and filtering | 187 to 190 | 27 | 3 | 6.18 to 6.23 | R to V, RA to RC, SA, VA | Smoothed volume filter; two- or three-sigma volume filter; volume filtered inflection points |
| 4 Open interest and breadth | 190 to 197 | 34 | 4 | 6.24 to 6.29 | W to AG | Loss aversion bias; open interest; tick volume; the TRIN; volume by price and by time |
| 5 Bar range and cycles | 197 to 202 | 28 | 3 | 6.30 to 6.38 | AH to AL | Rest, reversal and continuation bars; intraday volume cycle |
| 6 Volume oscillators | 203 to 208 | 30 | 3 | 6.39 to 6.44 | AM to AR, FA to FD | OBV; ADL; Chaikin Money Flow and Oscillator; NYSE Up/Down Volume; Herrick Payoff Index; COT report |

The other ten slides are the title, the objectives, the roadmap and seven
closing slides.

## Every idea has a picture

Of the 143 teaching slides, 97 carry a picture: all 44 of the book's figures
and 53 charts of our own. Forty six carry none, and no two are next to each
other. Four of them are where the book gives no figure: the book's two lists of volume oscillators, its eight oscillators and
eight methods of reading them, the volume distortions, which the book gives
in two sentences, and the Herrick Payoff Index, for which it gives no
formula and no figure.

A chart of ours is drawn where the book makes a point in words, where its
figure is a sketch, or where a real chart is too dense to read the point
off. Every chart carries its explanation on it in the slide's own words:
numbered points, labelled lines, measured bars and the arithmetic written
beside the columns it adds up. They are lettered in the order the deck
shows them. `build/charts_chapter06.py` holds the data and the reasoning.

| Charts | What they show |
|---|---|
| A, B | How the book's figures draw volume; one day's five trades added up to its volume |
| C to I | The two principles; the four cases of bullish and bearish volume; divergence and confirmation; what each warns of; standard divergence against volume divergence; Figure 6.6's periods on one invented uptrend; price-based and non-price-based on one chart |
| J to Q | Why minimum volume times a breakout, with the stops drawn; a low volume reversal; the VWMA and its two readings; the four kinds of top and bottom; a higher and a lower overextension level; a volume extreme read only afterwards; one record by day and by month |
| R to V | The five volume actions at a support, each with the book's outcome; the four filters; a 20-bar smoothed volume filter; a three-sigma filter; a channel drawn only through heavily traded turns |
| W to AG | A trend on flat volume; loss aversion; bull and bear market volume; turnover; open interest day by day; price, volume and open interest as arrows; open interest and reversal speed; tick volume against volume; the TRIN worked; volume by price; the book's four steps, numbered |
| AH to AL | The four named bars; the two reversal bars; the rest bar in two trends and the continuation bar; price leading volume; the intraday volume cycle |
| AM to AR | The OBV worked day by day; its start date and its weakness; the ADL worked on three closes; its multiplying factor from low to high; the CMF worked; open interest testing a historical level |

**Computed, and said to be.** Charts I and AN compute the OBV of their own
bars, L and M a 10-bar VWMA, T a 20-bar average of volume, U that average
plus three standard deviations of the same 20 bars, and AF and AG their
volume by price from their own days. Each says so in its small print, and
where the book's own calculation is elsewhere (the VWMA, the averages:
Chapter 11) it says that too. Every peso and every share count is ours.

A check may rest on what a slide's text says and never on what only its
picture shows, because the committed build prints a placeholder where a book
figure goes. All 38 items were checked against that.

## A word from an earlier chapter

Every term the earlier decks mark was checked against this deck, and every
word they taught by use. A term slide here is a term's first teaching in
the course. Where an earlier chapter taught a word, the slide is an ordinary
one and names that chapter on the slide, not only in the cue.

| Word, and where it was taught | How Chapter 6 uses it | On the slide |
|---|---|---|
| Volume must confirm the trend, Ch. 2 term | The same | *Chapter 2's tenet: volume confirms the trend* |
| Volume, used since Ch. 1, never defined | Defined here | Term, with the recall in its plain row |
| Open interest, Ch. 3 and 4, "taught in Chapter 6" | Defined here | Term; its cue names both chapters |
| Tick volume, a Ch. 1 caption; Ch. 3's tick chart | Defined here | Term; the plain row names both |
| Divergence, standard, Ch. 4 and 5 | A different test: volume declining, whatever price does | *Not the divergence Chapters 4 and 5 drew*, with Chart G |
| Selling climax, blow-off or buying climax, Ch. 4 | The same, with their extreme volume added | *Tops and bottoms: volume at the extremes*, caption |
| Volume spread action and the squat bar, Ch. 5 | The same four cases, named; two read more strongly | *Volume and bar range: Chapter 5's four cases*, and the captions on the next two slides |
| Price-based volume, Ch. 4's Figure 4.19 | This chapter's volume by price, not its price-based oscillators | *Volume by price marks a support: silver*, caption |
| Equivolume, constant volume, point and figure, Renko, three line break charts, Ch. 3 terms | The same | The two slides that use them |
| Barrier, inflection point, angular symmetry, cycle period, backtest, bidirectional entry, Ch. 5 | The same | Each slide's text or caption names Chapter 5 |
| Breakout, Ch. 2 and 4 (a range) and Ch. 5 (any level) | Both uses, each named | *Volume as a timing indicator* (a range), *Volume leading price* (a trendline) |
| Stop orders, go long, liquidate, go short, cover, OHLC, Ch. 1 | The same | The slides and origin lines that use them |
| Moving average, met in Ch. 4 and 5 | Of volume, and the VWMA and EMA | Named as Chapter 11's, with our computation said |
| Overbought, oversold, MACD, Bollinger Bands, cycle-tuned stochastic | Still not taught | Said on each slide; the last closing slide collects them |

## How long the chapter takes

**238 minutes at the calibrated rate, against a 180 minute session.** That
is information, not a target: nothing was cut to reach a length. The rate
is the one written down in `chapter-03/README.md`: a content slide 1, a term
1.25, a figure 0.75, a chart 0.5, a check with its reveal 2.5, each opening
and closing slide 1, all scaled by 1.150 into minutes. A slide with a
picture beside it is costed as the sum of its two parts. `build_chapter6.py`
prints this table on every build.

| Part | Slides | Minutes |
|---|---|---|
| Title, objectives, roadmap | 3 | 3.4 |
| 1 Confirmation | 31 | 42.8 |
| 2 Timing | 31 | 42.0 |
| 3 Filtering | 27 | 30.2 |
| 4 Open interest | 34 | 45.1 |
| 5 Bar range | 28 | 35.9 |
| 6 Oscillators | 30 | 35.1 |
| Closing | 7 | 3.4 |

**The run card gives two ways through it**, and `build_plan6.py` refuses a
card whose minutes disagree with the deck:

| Plan | What it does | Runs |
|---|---|---|
| One session | Cut 1, twenty slides that repeat on one more chart a point already made (39 minutes), and Cut 2, seven checks each in a part that keeps another (20 minutes), taken before starting | 179 |
| Two sessions | Parts 1 to 4 uncut, then stop at the end of Part 4 and carry Parts 5 and 6 with the closing slides | 164 and 74 |

`build_plan6.py` differs from `build_plan4.py` in one thing: a row of the
clock may be rounded up or down, not only to the nearest minute, so that the
column adds up to the chapter's costed total. Every total is still held to
the nearest minute. Its docstring says why.

## Where the book is silent or contradicts itself

Every one of these is named on a slide, and no check rests on any of them.

- **Bullish divergence "can only occur in a downtrend"** (p.177), yet Figure
  6.6 finds it in two dips inside an uptrend. The slide reads downtrend as
  price falling, for any stretch, and says that reading is ours.
- **Figure 6.4's ATR.** The figure lists it as a supporting series; no
  sentence of the text mentions it.
- **Figure 6.6** is captioned daily and labelled weekly.
- **The VWMA.** Above it, price is "potentially bullish"; a paragraph later
  a stock above it is "overvalued", where institutions look to sell. Figure
  6.11 is captioned VWMA on a daily chart and is a 10-minute VWAP chart.
- **Figures 6.22 and 6.23** are captioned silver; the text calls 6.23 "the
  same daily chart of USDJPY", then "the Silver market".
- **The tick read with the TRIN** is never said to be anything; it is not
  shown to be tick volume. The text calls a bullish TRIN overbought and
  Figure 6.25 calls its bullish TRIN oversold. Figures 6.25 and 6.26 are
  captioned daily and are intraday.
- **The NYSE Up/Down Volume** is "the ratio of advancing volume over
  declining volume"; Figure 6.44 labels its line cumulative, and the line
  runs below zero, which a ratio cannot.
- **The Chaikin oscillator** is taken from a running total of the CMF, as
  the book says; it gives no lengths for its two EMAs, and Figure 6.43
  prints 3 and 10.
- **The sixth learning objective**, reading volume across successive
  contract months, is not taught in this chapter's text; Chapter 3 did. The
  objectives slide says so.
- **Named and never explained:** the Demand Index, detrended volume, ROC
  volume, the PVO, program trading, net position in the COT report, and
  liquidity. Advances, declines, up volume and down volume are read by
  their names, and the slide says that reading is ours.

## Building it

From the repository root, in this order, every time the content module
changes:

```
.venv/bin/python build/build_chapter6.py                     # teaching, 191 slides, and the answer sheet in ~
.venv/bin/python build/build_chapter6.py --edition student   # student, 153 slides
.venv/bin/python build/build_plan6.py                        # instructor, 3 pages
.venv/bin/python build/build_lecture_notes6.py               # students, 51 pages
```

The two deck builds draw the 53 charts and are deterministic: a second run
leaves `git status` clean. The two PDF builds are not byte reproducible,
because Chrome stamps its own identifiers; compare them by `pdftotext`
before committing a rebuild.

The versions with the book's artwork must be written outside the
repository. The teaching deck's PDF is the copy for an iPad; the student
edition and the notes are what go to students:

```
.venv/bin/python build/build_chapter6.py \
    --with-figures --out ~/FIN1209-Chapter-06-with-figures-and-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-06-with-figures-and-charts.pptx
.venv/bin/python build/build_chapter6.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-06-Student-Edition-with-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-06-Student-Edition-with-charts.pptx
.venv/bin/python build/build_lecture_notes6.py \
    --with-figures --out ~/FIN1209-Chapter-06-Lecture-Notes-with-charts.pdf
cp chapter-06/FIN1209-Chapter-06-Run-Card.pdf ~/FIN1209-Chapter-06-Run-Card.pdf
```

The book's chapter for the students' folder is PDF pages 199 to 234 of the
course text, printed pages 173 to 208, from the chapter's first page to its
review questions; the last page also carries the chapter's four references:

```
pdfseparate -f 199 -l 234 <course text>.pdf /tmp/ch6/p-%03d.pdf
pdfunite /tmp/ch6/p-*.pdf ~/"FIN1209 Chapter 6 - Lim, Handbook of Technical Analysis.pdf"
```

Before committing either deck, confirm it embeds no artwork that is not
ours. Each must hold exactly 53 images, and their hashes must match this
chapter's own chart folder. The student edition must also carry no notes
part:

```
unzip -l chapter-06/FIN1209-Chapter-06.pptx | grep -c ppt/media                    # 53
unzip -l chapter-06/FIN1209-Chapter-06-Student-Edition.pptx | grep -c ppt/media    # 53
unzip -l chapter-06/FIN1209-Chapter-06-Student-Edition.pptx | grep -c notesSlide   # 0
unzip -o -d /tmp/media chapter-06/FIN1209-Chapter-06.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts-06/*.png | awk '{print $1}' | sort)
```

For the notes PDF the same check is `pdfimages -list <pdf>`: 44 images, 24
of them 1084 by 768 and 20 of them 884 by 692, and no others. The run card
holds no images. The decks with the book's artwork in them hold 97: the 53
charts and one for each of the 44 figures.

Then look at every page, as an image: both builds of the notes, the run
card, and both deck editions with the artwork.

## What was added to the kits

Two chart forms, in `build/chartkit.py`, beside what the earlier chapters
use and without changing any of it. All ten earlier decks, both editions of
Chapters 1 to 5, rebuild byte for byte.

**`panels`** stacks any number of `Pane`s on one time axis: price bars, a
line or volume columns in each, with gold and grey columns picked out,
numbers printed over columns, traces, strokes, notes, brackets and boxes,
and volume by price drawn sideways from the left edge. `Guide`s run a dashed
upright through every pane. It is the price-over-volume picture the whole
chapter is made of.

**`cells`** is a grid of small cases, each a stack of panes with no axes,
for a list of named cases that are each price and volume doing one thing:
the four kinds of bullish and bearish volume, the five volume actions at a
barrier, the four named bars.

## `assets/figures/`

Gitignored, and never committed. The build looks for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-6-01.png    ->    Figure 6.1
assets/figures/figure-6-44.png    ->    Figure 6.44
```

The book PDF embeds all 44 as one image each on PDF pages 200 to 233, so
`pdfimages -png -f 199 -l 234` on the course text yields 44 files, and here
they come out in figure order: the n-th file is Figure 6.n. Each was looked
at against its caption. No figure has its labels set as page text.
