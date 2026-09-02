# Chapter 1 - Introduction to the Art and Science of Technical Analysis

227 slides, six parts, 25 in-class checks carrying 50 multiple choice items,
49 terms, 35 figures from the course text, and 9 charts drawn for this course.
It ships in two editions: the teaching edition at 227 slides, and the student
edition at 177, which is the same deck without the checks, the reveals and the
speaker notes.

Four documents come out of the same chapter data, and they are for four
different people:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-01.pptx` | The room | The committed deck, teaching edition. Placeholders where the book's figures go; our own nine charts are really in it. | `build/content_chapter01.py` |
| `FIN1209-Chapter-01-Student-Edition.pptx` | The students | 177 slides. The same deck with the checks, the reveals and the speaker cues removed. | `build/content_chapter01.py` |
| `FIN1209-Chapter-01-Teaching-Plan.pdf` | The instructor | 26 pages. Timing, cut tiers, what to say, which check comes next. | `build/plan_chapter01.py` |
| `FIN1209-Chapter-01-Lecture-Notes.pdf` | The students | 29 pages. What the lesson covered, in prose, with the figures and the charts. | `build/lecture_chapter01.py` |
| `in-class-checks.md` | The instructor | The answer sheet. | `build/content_chapter01.py` |
| `check-answerability-audit.md` | The instructor | Whether every check item can be answered from the slides alone. | Written by hand |
| `teaching-plan-design.md` | Whoever edits the plan | Why the plan looks the way it does. | Written by hand |
| `lecture-notes-design.md` | Whoever writes the next chapter | The research behind the lecture notes, with sources. | Written by hand |

**Nothing in this folder is hand-edited except the two design files, the check
audit and this one.** The two decks, the answer sheet and the two PDFs are all
build output, and the next build overwrites them.

## Two editions of the deck, one content file

The instructor presents from the teaching edition and hands out the student
edition. Neither is a copy of the other and neither is hand-edited: both are
rendered from `build/content_chapter01.py`, which holds everything.

```
.venv/bin/python build/build_chapter1.py                     # teaching, 227 slides
.venv/bin/python build/build_chapter1.py --edition student   # student, 177 slides
```

The student edition drops all 25 checks and all 25 reveals, which is the 50
slide difference, and carries no speaker notes. The checks are for reading the
room live, and a student who has already seen the questions and the answers
tells the instructor nothing. The speaker cues are written to the instructor
about the room, so they are not a handout either.

Everything else is the same deck: the same terms, the same 35 figures, the
same nine charts, the same six parts, the same identity. The progress markers are regenerated for
whichever slides the edition holds rather than carried across, and the one
generated line that named the checks, the accent on the roadmap slide, is
reworded rather than replaced with new teaching content. `build/README.md`
has the mechanics.

Only the teaching build writes `in-class-checks.md`. The answer sheet is the
instructor's, and the student build cannot touch it.

## A teaching plan is not lecture notes

The distinction is the reason there are two PDFs, and it is worth keeping
straight in every chapter. Chapter 2 keeps the distinction and shortens the
instructor's half to three pages; see `chapter-02/README.md` for why.

The **teaching plan** is a run card. It is held in the hand while the deck is
on the screen. It carries minute counts, five run plans, a cut tier for every
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
| A slide, a term, a check, a figure, a chart slide | `build/content_chapter01.py` | both deck editions and both PDF builds |
| What is drawn on one of our charts | `build/charts_chapter01.py` | both deck editions and both PDF builds |
| How a chart is drawn at all | `build/chartkit.py` | everything |
| Anything in the teaching plan | `build/plan_chapter01.py` | `build/build_plan.py` |
| Anything in the lecture notes | `build/lecture_chapter01.py` | `build/build_lecture_notes.py` |
| How a slide is drawn | `build/deckkit.py` | the deck build |
| How a teaching plan page is laid out | `build/notekit.py` | both PDF builds |
| How a lecture notes page is laid out | `build/lecturekit.py` | `build/build_lecture_notes.py` |

**Rebuild both PDFs whenever you rebuild the deck.** The deck is the authority
on scope and both PDFs are checked against it. The plan resolves every slide
reference against the deck. The notes resolve every figure number and every
term against it, and the build fails if the notes name a figure the deck does
not place, or if the deck teaches a term the notes never define. The notes also
take their summary and their review questions straight from the deck's closing
slides rather than keeping a copy, so those cannot go stale either.

## The lecture notes

```
.venv/bin/python build/build_lecture_notes.py
```

29 A4 pages: a masthead and the chapter's learning objectives, then the deck's
six parts as six numbered sections in the same order, then a summary, the
book's review questions, a key terms index and the sources.

`lecture-notes-design.md` records the research the design came from, with real
URLs, and the length arithmetic. The short version: the page count is what
carrying all 35 figures and all 49 definitions costs, and the prose runs at
about 35 words per minute of teaching. Nine of those pages carry one of our
own charts, and unlike the book's figures those are in the committed build.

## The teaching plan

```
.venv/bin/python build/build_plan.py
```

26 A4 pages: a one-page run card, the standing instructions, what the
department examines, the five run plans with a mark-the-deck table, one page
per part keyed to the deck's own slide numbers, and the review crib. The five
plans are Full at 210 minutes, Discussion at 180, Long at 163, Standard at 111
and Short at 81, all of them content time with the openers' five minutes on top; `check-answerability-audit.md` records which slide answers
each of the 50 check items.

The plan never contains a typed slide number. It names slides by key
(`{s:fig:1.11}`, `{s:chart:C}`, `{s:check:13}`, `{s:term:Price}`) and the build
resolves those
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
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/ln $(seq 1 29)
$DATA/pdfpng ~/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/lnfig $(seq 1 29)
$DATA/pdfpng chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf /tmp/plan $(seq 1 26)
```

## Two builds of everything, and why

The chapter's **figures** are Wiley's, reproduced from Lim, *The Handbook of
Technical Analysis* (Wiley, 2016). This repository is public, so the artwork
is not in it: `assets/figures/` is gitignored and is absent on a clean clone.

The chapter's nine **charts** are the opposite case and are not affected by any
of this. They are ours, they are drawn at build time from
`build/charts_chapter01.py`, and they are in every build including the
committed ones. Nothing about them needs `--with-figures` and nothing about
them can be missing from a clean clone.

That gives two builds of each deck edition and two of the lecture notes. Same
content, same page and slide counts, same order. The only difference is what
sits in the figure band.

**The committed versions are the placeholder builds.** This is what is in the
repository and what a plain build produces on any machine:

```
.venv/bin/python build/build_chapter1.py
.venv/bin/python build/build_chapter1.py --edition student
.venv/bin/python build/build_lecture_notes.py
```

Every figure keeps its number, a line saying what it shows, and the credit
line, so the chapter stays readable and rebuildable by anyone.

**The versions with the artwork placed** must be written outside the
repository. There are three of them, one per document that carries figures:

```
.venv/bin/python build/build_chapter1.py \
    --with-figures --out ~/FIN1209-Chapter-01-with-figures.pptx
.venv/bin/python build/build_chapter1.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-01-Student-Edition.pptx
.venv/bin/python build/build_lecture_notes.py \
    --with-figures --out ~/FIN1209-Chapter-01-Lecture-Notes.pdf
```

The first is what the instructor presents from. The last two are what go to
students through Canvas.

Figures are off by default, and both builds refuse `--with-figures` pointed
anywhere inside the repository, whichever edition is being built. That is
deliberate: the copyrighted artwork must never reach a commit, and the plain
builds have to keep reproducing the committed files.

Before committing either deck, confirm it embeds no artwork that is not ours:
`unzip -l <deck>.pptx | grep ppt/media` must list exactly nine images and
nothing else, and their hashes must match `build/generated/charts/`:

```
unzip -o -d /tmp/media chapter-01/FIN1209-Chapter-01.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts/*.png | awk '{print $1}' | sort)
```

For the notes PDF the same check is `pdfimages -list <pdf>`: nine images, all
2274 by 768, and no others.

## `assets/figures/`

Gitignored, and never committed. Both builds look for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-1-09.png    ->    Figure 1.9
assets/figures/figure-1-21.png    ->    Figure 1.21
```

The 35 figures the chapter places are 1.1 through 1.35, complete, with no
gaps. A missing file is not an error: that figure renders as a placeholder
and the rest of the document is unaffected.

## `build/generated/charts/`

Gitignored too, and for the opposite reason: it is build output, not somebody
else's property. Every build of the deck and of the lecture notes redraws all
nine PNGs from `build/charts_chapter01.py` before it starts, so the folder is
never stale and never needed in a commit.

The nine are lettered, not numbered, and they carry their own credit line
rather than Wiley's. Both live in one place, `deckkit.chart_credit`, so a
student can always tell which pictures are the book's and which are ours, and
so the wording can be changed in one edit.

## The figures that carry the most weight

Part 4 runs Figures 1.9 to 1.15 as a sequence, one to a slide. It is the same
price chart seven times: bare, then trendlines, moving averages, chart
patterns, regression with divergence, regression with volume, and finally
volatility bands with volume and MACD. Do not summarize it and do not skip
ahead. The room has to watch one chart get read seven defensible ways, because
that sequence *is* the argument that analysis is subjective. Everything else in
Part 4 depends on the room having seen it happen.

In the lecture notes the same seven figures are one plate on a single page,
walked through in order by the paragraph underneath it, which is how a
textbook handles a sequence a reader is meant to compare at a glance.

Part 4 then closes on the book's own self test, Figures 1.22, 1.23 and 1.24.
It is an activity, not a set of slides: a blank USDCAD chart, four minutes of
silence while the room draws its own trendlines, a comparison with the person
beside them, then the book's lines, then a second pass for chart patterns.
**Do not narrate over it and do not skip Figure 1.22**, because without the
blank chart there is nothing to compare against. It is also Homework 1
rehearsed on paper, and the bridge into the charting platform half of the
week.

## Smoke test

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-01/FIN1209-Chapter-01.pptx
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-01/FIN1209-Chapter-01-Student-Edition.pptx
```
