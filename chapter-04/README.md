# Chapter 4 - Market Phase Analysis

79 slides, nine parts, 11 in-class checks carrying 22 multiple choice items,
6 terms, all 32 of the book's figures, and 18 charts of our own. It ships in
two editions: the teaching edition at 79 slides, and the student edition at
57, which is the same deck without the checks, the reveals and the speaker
notes.

**This chapter is the leaner deck.** Chapters 1 to 3 run to about 200
slides each. The instructor asked for the fewest slides from which the
chapter can still be learned and taught properly, with no length set in
advance. The instructor read the result, said "I like these slides", and
asked for the rest of the chapter in the same style, so the companions below
were built to it.

**This is the second build, and the first one was wrong in three ways.** It
came to 46 slides. The instructor opened it and sent it back:

1. Five slides in a row were text with no picture, and neither he nor a
   student could follow them.
2. Each check showed its answer on the question slide, which cannot be
   presented in a room.
3. It taught less than the book does. It placed 19 of the 32 figures and
   dropped what the book says about the other 13.

So the lean rule is now narrower than it was. **It cuts a slide that teaches
nothing new, and never what the book says.**

Four documents ship from the same chapter data, for three different people,
and two more are written outside the repository:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-04.pptx` | The room | The committed deck, teaching edition. Our own charts, and a placeholder where each of the book's figures goes. | `build/content_chapter04.py` |
| `FIN1209-Chapter-04-Student-Edition.pptx` | The students | 57 slides. The same deck with the checks, the reveals and the speaker cues removed. | `build/content_chapter04.py` |
| `FIN1209-Chapter-04-Run-Card.pdf` | The instructor | 3 pages. Minutes per part, when each part should start and the latest it can, what to cut if it runs slow, and what must never be cut. No answers. | `build/plan_chapter04.py` |
| `FIN1209-Chapter-04-Lecture-Notes.pdf` | The students | 33 pages. What the lesson covered, in prose, with every figure and every chart the deck places. | `build/lecture_chapter04.py` |
| `~/FIN1209-Chapter-04-In-Class-Checks (answer sheet).md` | The instructor | The answer sheet. **Not in this repository.** | `build/content_chapter04.py` |
| `~/FIN1209-Chapter-04-Check-Audit.md` | The instructor | Whether every check item can be answered from the slides before it. **Not in this repository.** | Written by hand |

**Nothing in this folder is hand-edited except this file.** The two decks
and the two PDFs are build output, and the next build overwrites them.

**The answer material stays out of this public repository.** Chapters 2 and
3 commit their answer sheets and audits beside the deck. Chapter 4 does not:
`build_chapter4.py` writes the answer sheet to the instructor's home
directory, refuses a `--checks-out` path inside the repository, and only the
teaching build writes it. The audit is written by hand beside it, and the
run card prints no answers and points there. Its result can be stated
without its answers: **22 items, 22 pass**, every one answered by the text
of a slide that comes before its check, none by a picture, a caption alone
or a speaker cue.

## What is lean about it, and what is not

| Chapters 1 to 3 | Chapter 4 |
|---|---|
| Six parts, the template's own convention | Nine parts, the book's sections 4.1 to 4.9. Section 4.10 is the book's summary and feeds the closing slides. |
| A divider slide and a recap slide for every part | Neither. The first slide of a part carries the book's section number in its title. |
| A picture is a slide of its own, after the slide that needs it | A picture sits beside the idea it shows, on the same slide |
| Two objectives slides and a roadmap slide, generated | One of each, written in the content module |

What did not change: one idea per slide, six body lines at the most, every
term taught plain words first and the book's own definition last, nothing
taught that the book does not teach, **a check is a question slide and then
a reveal slide**, every check answerable from slides that come before it, no
slide that refers back to a check or a chart, the answer key spread across A
to D, and no em dash anywhere. The build still refuses a deck that breaks
any of the rules it can check.

## Every idea has a picture

Of the 51 teaching slides, 50 carry a picture. The one that does not is the
list of thirteen sentiment indicators, which the book names and explains
none of. The other 28 slides are the 11 checks, at two slides each, and the
six slides of the frame.

- **A book figure where the book has one.** All 32 are placed, each beside
  what the book says about it. Figure 4.14 is on a slide of its own because
  the book gives it half a sentence.
- **One of our own charts otherwise.** 18 of them, lettered A to R. See the
  table below.

A check may rest on what a slide's text says and never on what only its
picture shows, because the committed build prints a placeholder where a book
figure goes. All 22 items were checked against that.

## What each section teaches

Every section is taught as fully as the book teaches it. Nothing is kept
light by choice any more.

| Section | Slides | Figures | Our charts | What the first build left out |
|---|---|---|---|---|
| 4.1 Dow theory of market phase | 20 | 4.1 to 4.4 | A to J | A picture for every slide; the downtrend as a slide of its own; the signs of a distribution as a slide of its own; volume as the first evidence; a third check |
| 4.2 Chart patterns | 22 | 4.5 to 4.14 | K to P | The shapes behind the book's three lists; the book's own example of one triangle in three places; Figures 4.7, 4.9, 4.10, 4.13 and 4.14 and what the book says about each; the lists of patterns with respect to trend sentiment; a third check |
| 4.3 Volume and open interest | 7 | 4.15 to 4.19 | | Figures 4.18 and 4.19, the two real charts; a check of its own |
| 4.4 Moving averages | 2 | 4.20, 4.21 | | Figure 4.20, the single average and its whipsaws |
| 4.5 Divergence and momentum | 5 | 4.22 to 4.24 | | Figures 4.23 and 4.24: bullish divergence, and the confluence with a pattern and a cycle |
| 4.6 Sentiment | 5 | 4.25 | Q | Why sentiment reads best at extremes; the book's list of thirteen indicators |
| 4.7 Sakata | 5 | 4.26, 4.27 | R | A picture beside the five names |
| 4.8 Elliott | 2 | 4.28, 4.29 | | Figure 4.29, the wave count on the gold chart |
| 4.9 Cycle analysis | 5 | 4.30 to 4.32 | | Figures 4.30 and 4.32: the plain guideline, and the price channel |

The other six slides are the title, the objectives, the roadmap and three
closing slides.

**What is still short, and why.** Sections 4.3 to 4.6, 4.8 and 4.9 use a
tool that a later chapter of the book teaches, and the book's own Chapter 4
does not explain it. The deck stops where the book stops and says so on the
slide:

| Used and not explained by the book here | Where the slide says so | Taught in |
|---|---|---|
| Open interest | 4.3, caption | Chapter 6 |
| Price-based volume | 4.3, caption | not said |
| Whipsaws, and moving averages themselves | 4.4, caption | Chapter 11 |
| Divergence, MACD and RSI | 4.5, caption | Chapter 9 |
| The thirteen sentiment indicators | 4.6, a slide of its own | Chapter 23 |
| Elliott's rules, and Fibonacci projection | 4.8, caption | Chapter 18 |
| How a cycle period is found | 4.9, caption | Chapter 20 |
| Diamond formations | 4.2, on Chart O | Chapter 13 names them only |

## The eighteen charts

A chart is drawn where the book makes a point in words that none of its own
figures shows. Section 4.1 has three pages on who buys and who sells in each
phase with no figure at all, and section 4.2 lists seventeen patterns by
name. `build/charts_chapter04.py` holds the data and the reasoning.

| Chart | Beside | What it shows |
|---|---|---|
| A | Markets move in phases | One line through accumulation, trend, distribution and trend |
| B | Known only afterwards | One consolidation, two outcomes |
| C | Accumulation | The selling climax, and the informed gathering shares |
| D | The uptrend | Who joins, in the order they join |
| E | The downtrend | The same feedback running downward |
| F | Distribution | The blow-off, and the informed selling |
| G | Tops and bottoms | The book's three comparisons on one cycle |
| H | Signs of an accumulation | Prior bottom, no lower troughs, volume subsiding then surging |
| I | Signs of a distribution | The mirror of H |
| J | Minimum measuring objective | The three completion levels, in pesos |
| K | Patterns show the phase | Which kind of pattern sits in which phase |
| L | Consolidation pattern | A confined range, beside a V bottom |
| M | Intrinsically bullish | The book's eight, sketched |
| N | Intrinsically bearish | The book's seven, sketched |
| O | Intrinsically neutral | Four of the five the book names, sketched |
| P | Extrinsic bias | One ascending triangle in three locations |
| Q | Sentiment at extremes | Where the indicators are most accurate |
| R | The five methods | Sakata's five names on one line |

**Charts M, N and O are the one place the deck reaches past Chapter 4.** The
chapter names seventeen patterns and shows seven of them on real charts, in
Figures 4.6 to 4.14, which are all placed, but it describes no shape in
words. The book does that in its
Chapter 13. A list of seventeen names teaches nothing without a picture, so
each is sketched from Chapter 13's own one line description and from nothing
outside the book, every gallery says so in its footnote, and no check asks
for a shape. Diamond formations have no sketch: the book says only that they
need four trendlines.

The data on every chart is invented from a fixed seed, and each says so.

## How long the chapter takes

**136 minutes at the calibrated rate, against a 180 minute session.** It
fits, with 44 minutes in hand, and it is the first chapter whose run card
names no cut to take before starting. That is information, not a target:
nothing was cut to reach it. `build_chapter4.py` prints the sum on every
build, and `build_plan4.py` refuses a run card whose minutes disagree with
it.

The rate is the one written down in `chapter-03/README.md`: a content slide
1, a term 1.25, a figure 0.75, a chart 0.5, a check with its reveal 2.5,
each opening and closing slide 1, all scaled by 1.150 into minutes. A slide
with a picture beside it is costed as the sum of its two parts, because
putting them on one slide saves a click and not the talking. There are no
dividers and no recaps, so that weight is zero.

| Part | Slides | Minutes |
|---|---|---|
| Title, objectives, roadmap | 3 | 3.4 |
| 4.1 Dow | 20 | 34.5 |
| 4.2 Chart patterns | 22 | 38.8 |
| 4.3 Volume | 7 | 12.9 |
| 4.4 Moving averages | 2 | 4.0 |
| 4.5 Divergence | 5 | 8.9 |
| 4.6 Sentiment | 5 | 7.8 |
| 4.7 Sakata | 5 | 8.9 |
| 4.8 Elliott | 2 | 4.0 |
| 4.9 Cycles | 5 | 8.9 |
| Closing | 3 | 3.4 |

The weights sum to 118.0 and 118.0 times 1.150 is 135.7. The rate was
calibrated on a full length deck with a picture on a slide of its own, so
how well it holds for this shape is one of the things the room will show,
and the run card says so on its first page.

**The run card's cuts, for a session that runs slow.** A cut here is a whole
slide, idea and picture together, because there is no chart standing alone
to drop. No check rests on a cut slide and no later slide refers back to
one.

| Cut | What comes out | Minutes | Chapter runs |
|---|---|---|---|
| None | The whole deck | | 136 |
| 1 | Five second examples: Figures 4.14, 4.18, 4.23, 4.29 and 4.32 with their slides | 9 | 127 |
| 2 | Checks 2 and 6, each in a part that has three | 6 | 121 |
| Last resort | Stop at the end of 4.6 and carry 4.7 to 4.9 with the closing slides | 25 | |

The card's table gives each part a Latest start, the last clock time it can
begin and still end by 3:00 uncut, which is the start time plus the 44
minutes in hand.

## Building it

From the repository root, in this order, every time the content module
changes:

```
.venv/bin/python build/build_chapter4.py                     # teaching, 79 slides, and the answer sheet in ~
.venv/bin/python build/build_chapter4.py --edition student   # student, 57 slides
.venv/bin/python build/build_plan4.py                        # instructor, 3 pages
.venv/bin/python build/build_lecture_notes4.py               # students, 33 pages
```

The two deck builds draw the eighteen charts and are deterministic: a second
run leaves `git status` clean. The two PDF builds are not byte reproducible,
because Chrome stamps its own identifiers; compare them by `pdftotext`
before committing a rebuild. The teaching build writes the answer sheet to
`~/FIN1209-Chapter-04-In-Class-Checks (answer sheet).md`, never inside the
repository; `--checks-out` moves it elsewhere outside.

**Rebuild both PDFs whenever you rebuild the deck.** The run card resolves
every slide reference against the deck and costs every minute it prints. The
notes resolve every figure number, every chart letter and every term, fail
if the deck places a picture the notes do not, and take their summary and
review questions from the deck's closing slides. Every definition in the
notes is read off the deck's own term slide by `formal()`.

The versions with the book's artwork must be written outside the
repository. The teaching deck's PDF is the copy for an iPad; the student
edition and the notes are what go to students through Canvas:

```
.venv/bin/python build/build_chapter4.py \
    --with-figures --out ~/FIN1209-Chapter-04-with-figures-and-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-04-with-figures-and-charts.pptx
.venv/bin/python build/build_chapter4.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-04-Student-Edition-with-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-04-Student-Edition-with-charts.pptx
.venv/bin/python build/build_lecture_notes4.py \
    --with-figures --out ~/FIN1209-Chapter-04-Lecture-Notes-with-charts.pdf
cp chapter-04/FIN1209-Chapter-04-Run-Card.pdf ~/FIN1209-Chapter-04-Run-Card.pdf
```

Before committing either deck, confirm it embeds no artwork that is not
ours. Each must hold exactly eighteen images, and their hashes must match
this chapter's own chart folder. The student edition must also carry no
notes part:

```
unzip -l chapter-04/FIN1209-Chapter-04.pptx | grep -c ppt/media                    # 18
unzip -l chapter-04/FIN1209-Chapter-04-Student-Edition.pptx | grep -c ppt/media    # 18
unzip -l chapter-04/FIN1209-Chapter-04-Student-Edition.pptx | grep -c notesSlide   # 0
unzip -o -d /tmp/media chapter-04/FIN1209-Chapter-04.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts-04/*.png | awk '{print $1}' | sort)
```

For the notes PDF the same check is `pdfimages -list <pdf>`: eighteen
images, fifteen of them 1124 by 768 and three 1044 by 692, and no others.
The run card holds no images. The decks with the book's artwork in them
hold 50: the eighteen charts and one for each of the 32 figures.

Then look at every page, as an image: both builds of the notes, the run
card, and the student edition with the artwork, because the figure build is
not the placeholder build with pictures in it.

```
pdftoppm -r 80 -png chapter-04/FIN1209-Chapter-04-Run-Card.pdf /tmp/card
pdftoppm -r 80 -png chapter-04/FIN1209-Chapter-04-Lecture-Notes.pdf /tmp/ln
pdftoppm -r 80 -png ~/FIN1209-Chapter-04-Lecture-Notes-with-charts.pdf /tmp/lnfig
pdftoppm -r 60 -png ~/FIN1209-Chapter-04-Student-Edition-with-charts.pdf /tmp/stu
```

## The lecture notes

Nine sections, the book's 4.1 to 4.9 in order, so a student can move
between the slides, the book and the notes. Every one of the 32 figures and
18 charts is placed and named in a sentence saying what to look at. The
charts are drawn for the slide's picture column, which is close to square,
so on the page their height sets their width; they are set at 76mm, or 82mm
for the two pattern galleries, because shorter than that their labels cannot
be read in print. Section 9.3 collects what the chapter uses without
teaching and the three places the book says two things.

## What was added to the kits

All of it was added beside what the earlier chapters use and without
changing any of that. All six earlier decks, both editions of Chapters 1 to
3, rebuild byte for byte, and their six PDFs rebuild identical by text.

**`Pair`**, in `build/deckkit.py`, puts an ordinary `Content` or `Term` on
the left and an ordinary `Figure` or `Chart` on the right. The two parts
keep their own types, so a book figure keeps the Wiley credit line and a
placeholder in the committed build, exactly as it does on a slide of its
own. `text_w` sets the width of the text column. The build measures the text
column the same way the renderer draws it and refuses a pair whose text
would run past the safe bottom.

**Hold every `Pair` to 17pt or larger.** The renderer steps the type down
to 15pt to make a long column fit, and a slide at 15pt is hard to read from
the back of a room. Every pair in this chapter is at 17pt or above. The
check is by hand: `_pair_fit()` returns the size, and the fix is to shorten
a line by a few words until it wraps one line fewer.

Three options on `Chapter` shape the frame around the parts: `openers`
replaces the generated objectives and roadmap slides, `title_notes` replaces
the generated title cues, and `dividers=False` drops the divider slides. A
`Section` with no `recap` renders no recap slide. Left alone, all four give
the frame the earlier chapters have.

**Two chart forms**, in `build/chartkit.py`. `annotated` is one price line
with spans, boxes, levels, pattern sides, measures and short labels marked
on it, and an optional volume panel. `gallery` is a grid of small named
shapes with no axes. Both take the size to draw at, and `pair_size()` works
that size out from deckkit's own geometry, so a chart fills its picture
column exactly and a 10 point label in the artwork is a 10 point label on
the slide.

The first build added a third thing, a check that revealed its answers on
the question slide. It has been removed from `deckkit.py`, because the
instructor could not present it and nothing else used it.

`build_chapter4.py` also checks the closing slides against the page on every
build. `deckkit` does not, for any chapter; `AGENTS.md` records that trap.

The companions added two things to the print kits, each beside what was
there and defaulting to it. `notekit.DeckFacts` takes the part count the
run card's cover prints, which was hard coded to six, and `lecturekit`
counts the sections in the sentence above the review questions instead of
saying six. Every earlier chapter's run card, plan and notes rebuild
identical by text, and all six earlier decks byte for byte.

## `assets/figures/`

Gitignored, and never committed. The build looks for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-4-01.png    ->    Figure 4.1
assets/figures/figure-4-32.png    ->    Figure 4.32
```

The book PDF embeds all 32 as one image each on PDF pages 126 to 149, so
`pdfimages -png -f 125 -l 150` on the course text yields 32 files. **They
are not all in figure order.** The three images on PDF page 147 come out as
4.28, 4.29, 4.27, so the 27th, 28th and 29th files have to be renamed by
what they show: the Elliott wave structure is 4.28, the weekly gold chart is
4.29, and Dow's three phase market drawn with Sakata's pieces is 4.27. Every
other page is in order.

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

**Two names for one sentiment index, or two indexes.** Figure 4.25 lists a
Bullish Percent Index and the book's list of thirteen indicators has a
Bullish Sentiment Index. The book does not say whether they are the same,
and the slide says that.

**Figure 4.29's top is called an inverted head and shoulders.** The book
describes the new consolidation around the top of wave 5 that way. The
speaker cue says to read it as the book states it.

**The inertial characteristics** its own learning objectives promise are
never mentioned in the text. The last closing slide says so.
