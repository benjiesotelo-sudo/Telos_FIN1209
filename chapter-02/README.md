# Chapter 2 - Introduction to Dow Theory

175 slides, six parts, 21 in-class checks carrying 42 multiple choice items,
27 terms, 26 figures from the course text, and 8 charts drawn for this
course. It ships in two editions: the teaching edition at 175 slides, and the
student edition at 133, which is the same deck without the checks, the
reveals and the speaker notes.

Four documents come out of the same chapter data, and they are for three
different people:

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-02.pptx` | The room | The committed deck, teaching edition. Placeholders where the book's figures go; our own eight charts are really in it. | `build/content_chapter02.py` |
| `FIN1209-Chapter-02-Student-Edition.pptx` | The students | 133 slides. The same deck with the checks, the reveals and the speaker cues removed. | `build/content_chapter02.py` |
| `FIN1209-Chapter-02-Run-Card.pdf` | The instructor | 3 pages. Minutes per part, what to cut first, and what must never be cut. | `build/plan_chapter02.py` |
| `FIN1209-Chapter-02-Lecture-Notes.pdf` | The students | 22 pages. What the lesson covered, in prose, with the figures and the charts. | `build/lecture_chapter02.py` |
| `in-class-checks.md` | The instructor | The answer sheet. | `build/content_chapter02.py` |
| `check-answerability-audit.md` | The instructor | Whether every check item can be answered from the slides alone. | Written by hand |

**Nothing in this folder is hand-edited except the check audit and this
file.** The two decks, the answer sheet and the two PDFs are all build
output, and the next build overwrites them.

## A run card, and not a teaching plan

This is the one place Chapter 2 deliberately does not follow Chapter 1.

Chapter 1 ships a 26 page teaching plan with five run plans, a cut tier for
every block, and one page per part. The instructor taught from it on
2026-09-02 and said plainly that he did not really use it. The problem it was
built to solve was real and it did not solve it: **he had 180 minutes and
reached the end of Part 4 of 6.**

So Chapter 2 ships three pages instead, and they do three things.

- **Page 1 is the clock.** Minutes per part in two columns, full and cut,
  each with the wall clock time to be starting that part at.
- **Page 2 is what to cut, first and second**, named slide by slide, with the
  minutes each cut buys.
- **Page 3 is the emergency cut and the floor**: seven things that carry a
  check, a past paper item or Homework 1 and are never on the table.

`chapter-01/teaching-plan-design.md` still records the research behind the
page layout, which this card inherits unchanged. What changed is the length
and the job, not the typography.

## How long the chapter actually takes

**The minutes on the run card are calibrated, not estimated**, and this is
the arithmetic behind them.

Chapter 1's front matter plus its first four parts is 155 slides. That is
what 180 minutes bought in the room on 2026-09-02. Costing each slide type at
what it plausibly takes, a term slide more than a figure, a check more than
either, and then scaling the whole model so that Chapter 1's first 155 slides
come to exactly 180 minutes, gives a rate that can be applied to any deck
built to this design.

Chapter 2's own mix of 27 terms, 26 figures, 8 charts, 21 checks and the rest
comes to **202 minutes at that rate.** Which is to say:

- **Chapter 2 is one session, but only with the run card's first two cuts.**
  Taking both before the session starts brings it to 179 minutes.
- Left uncut it needs about 3 hours 25 minutes, which is a session and a
  half.
- If it slips anyway, the natural break is **the end of Part 5**. Part 6 is
  the only part nothing later in the chapter depends on.

The deck was not compressed to reach a number. One idea per slide, plain
words before the formal definition, and a check every few terms are the
instructor's rules and they are not negotiable; what the run card does is
name, in advance, exactly which twenty three minutes come out.

## Two editions of the deck, one content file

```
.venv/bin/python build/build_chapter2.py                     # teaching, 175 slides
.venv/bin/python build/build_chapter2.py --edition student   # student, 133 slides
```

The student edition drops all 21 checks and all 21 reveals, which is the 42
slide difference, and carries no speaker notes. Everything else is the same
deck. Only the teaching build writes `in-class-checks.md`.

## The lecture notes and the run card

```
.venv/bin/python build/build_lecture_notes2.py    # students, 22 pages
.venv/bin/python build/build_plan2.py            # instructor, 3 pages
```

**Rebuild both whenever you rebuild the deck.** The deck is the authority on
scope and both PDFs are checked against it. The run card resolves every slide
reference against the deck, so a content change moves the card with it and a
broken reference fails the build rather than printing a wrong number in front
of a class. The notes resolve every figure number, every chart letter and
every term, and take their summary and review questions straight from the
deck's closing slides.

## Then look at the PDFs

Every page, as an image. Both builds of the lecture notes, not just one: the
figure build is not the placeholder build with pictures in it.

```
DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
$DATA/pdfpng chapter-02/FIN1209-Chapter-02-Lecture-Notes.pdf /tmp/ln $(seq 1 22)
$DATA/pdfpng ~/FIN1209-Chapter-02-Lecture-Notes-with-charts.pdf /tmp/lnfig $(seq 1 22)
$DATA/pdfpng chapter-02/FIN1209-Chapter-02-Run-Card.pdf /tmp/card 1 2 3
```

## Two builds of everything, and why

The chapter's 26 **figures** are Wiley's, reproduced from Lim, *The Handbook
of Technical Analysis* (Wiley, 2016). This repository is public, so the
artwork is not in it: `assets/figures/` is gitignored and absent on a clean
clone.

The chapter's eight **charts** are the opposite case. They are ours, drawn at
build time from `build/charts_chapter02.py`, and they are in every build
including the committed ones. Nothing about them needs `--with-figures`.

**The committed versions are the placeholder builds.** Every figure keeps its
number, a line saying what it shows, and the credit line, so the chapter
stays readable and rebuildable by anyone.

**The versions with the artwork placed** must be written outside the
repository:

```
.venv/bin/python build/build_chapter2.py \
    --with-figures --out ~/FIN1209-Chapter-02-with-figures-and-charts.pptx
.venv/bin/python build/build_chapter2.py --edition student \
    --with-figures --out ~/FIN1209-Chapter-02-Student-Edition-with-charts.pptx
.venv/bin/python build/build_lecture_notes2.py \
    --with-figures --out ~/FIN1209-Chapter-02-Lecture-Notes-with-charts.pdf
```

The first is what the instructor presents from. The last two are what go to
students through Canvas. Both builds refuse `--with-figures` pointed anywhere
inside the repository.

Before committing either deck, confirm it embeds no artwork that is not ours:
`unzip -l <deck>.pptx | grep ppt/media` must list exactly eight images, and
their hashes must match this chapter's own chart folder:

```
unzip -o -d /tmp/media chapter-02/FIN1209-Chapter-02.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts-02/*.png | awk '{print $1}' | sort)
```

For the notes PDF the same check is `pdfimages -list <pdf>`: eight images,
all 2274 by 768, and no others.

## `assets/figures/`

Gitignored, and never committed. Both builds look for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-2-04.png    ->    Figure 2.4
assets/figures/figure-2-26.png    ->    Figure 2.26
```

The 26 figures the chapter places are 2.1 through 2.26, complete, with no
gaps. A missing file is not an error: that figure renders as a placeholder
and the rest of the document is unaffected.

## `build/generated/charts-02/`

Gitignored too, and for the opposite reason: it is build output, not somebody
else's property. Every build of the deck and of the lecture notes redraws all
eight PNGs from `build/charts_chapter02.py` before it starts.

**One folder per chapter.** The letters restart at A in every chapter, so a
shared folder would have Chapter 2's Chart A overwrite Chapter 1's and break
the hash check above for both. Chapter 1's folder is `charts`; every chapter
after it is numbered.

## Where the book is silent, and what this chapter does about it

Three places, and all three are named on the slides and in the notes rather
than filled in from outside the book.

**Review question 8 asks about Elliott, and the chapter never mentions him.**
The book's own eighth review question asks for the main differences between
Dow's and Ralph N. Elliott's determination of a trend. Chapter 2 gives Dow's
half and nothing else; the book takes Elliott up in Chapter 4 and again in
Chapter 18. A closing slide names the gap, gives the Dow half, and tells
students not to finish the question from outside the book. **No check is set
on it**, which is the same treatment Chapter 1 gave supply side and demand
side.

**Figure 2.1 asks a question the book does not answer.** The caption is "Is
the Market Discounting Unknown Information?" and the text asks whether the
decline before September 11 was discounting or coincidence and then moves on.
The slide asks it and leaves it open, and no check rests on it.

**Support and resistance are used and never defined.** Part 5 quotes the
book's own sentence, that unless a prior support or resistance level is
breached the trend is assumed intact. The slide says plainly that the chapter
does not define either word, offers the working reading the chapter's own
figures show, and points at where the book defines them properly.

## The figures that carry the most weight

Part 3 runs Figures 2.8 and 2.9, then 2.10 and 2.11, as two pairs. Each pair
is the same price on two different scales, and the pairs exist to show that
the same prices produce a different date for the same change of trend. **Do
not show one half of a pair.** If the clock is against you, drop the second
pair whole; that is the run card's first cut.

Part 5 closes on Figures 2.18 and 2.19, the three top reversals and the three
bottom reversals. The three differ in exactly one respect, what the second
peak did relative to the first, and saying that out loud before naming them
is worth more than naming them twice.

## Smoke test

```
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-02/FIN1209-Chapter-02.pptx
soffice --headless --convert-to pdf --outdir /tmp/smoke chapter-02/FIN1209-Chapter-02-Student-Edition.pptx
```
