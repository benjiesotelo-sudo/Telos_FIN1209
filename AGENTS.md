# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Start at TEMPLATE.md if you are building a chapter

`TEMPLATE.md` at the repository root is what whoever writes the next chapter
reads first: which files to copy and which to write fresh, the content
module's structure, the non-negotiable teaching design rules, the copyright
split, the build commands, and the verification steps. This file carries only
the sharp edges; that one carries the method.

## Teach only what the textbook teaches

The instructor's standing rule, and it outranks everything else here. Where
Lim's chapter defines a term, use the book's definition. Where the book is
silent, ambiguous, or contradicts itself, say so plainly on the slide and in
the notes rather than importing a definition or narrating events the book does
not. The worked example is `Supply side and demand side` in
`build/content_chapter01.py`: the book never defines the pair, so the deck
teaches the gap, marks the outside readings non-examinable, and sets no
question on either.

## Two chapters are built, and the newer one is the shape to copy

Chapter 1 is 227 slides and Chapter 2 is 175. Chapter 2 is the same design
done a second time and it is the fresher worked example; `TEMPLATE.md` says
which files to copy from it and what changed since Chapter 1.

## The deck ships in two editions from one content file

`build/build_chapterN.py` takes `--edition teaching` (the default, everything)
or `--edition student` (every check and reveal dropped and no speaker notes).
One content module feeds both; nothing is forked and nothing is deleted from
`build/content_chapterNN.py`. The switch lives in `deckkit.build()` and knows
nothing about any chapter, so a later chapter inherits it by copying the build
script.

The one rule this puts on content: **never write a slide that refers back to a
check.** "As the last question showed" is true in one edition and false in the
other, and no build check catches it. `build/README.md` has the mechanics and
`chapter-01/README.md` the two commands.

## The decks are generated, never hand-edited

Editing a `.pptx` is a dead end; the next build overwrites it. Change
`build/content_chapterNN.py` (pure data) and rebuild. Drawing code lives only
in `build/deckkit.py`, which knows nothing about any chapter. `build/README.md`
has the environment, the design rules the build enforces, and the fonts.

## Our own charts are committed. The book's figures never are.

Chapter 1 carries nine charts this course drew and Chapter 2 carries eight,
each on a companion slide after the term it illustrates. They are the opposite
case to the textbook figures in every respect, and the two must not be
conflated:

| | Book figure | Our chart |
|---|---|---|
| Type | `deckkit.Figure` | `deckkit.Chart`, not a subclass |
| Named | `1.11`, the book's scheme | `Chart C`, our namespace |
| Credit | Wiley, hard coded on `Figure.credit` | `deckkit.chart_credit()`, one place |
| In the repo | Never. `assets/figures/` is gitignored | Always, drawn at build time |
| Committed build | Placeholder | The real artwork |

`build/chartkit.py` draws them and knows nothing about any chapter;
`build/charts_chapterNN.py` is the data. Every build of the deck and of the
lecture notes redraws them first, so a fresh clone gets the real slide. The
data is invented from fixed seeds, because we hold no market data licence, and
every chart says so in its credit line.

**One output folder per chapter**, `build/generated/charts` for Chapter 1 and
`charts-02` for Chapter 2. The letters restart at A in every chapter and a
shared folder would have one chapter's Chart A overwrite another's.

If a chapter needs a chart shape chartkit has not got, **add the form** rather
than editing an existing one; Chapter 2 added seven. After any kit change,
rebuild every earlier chapter and confirm the decks are byte identical.

The one trap: the committed decks embed those PNGs, so the artwork check
before a commit is not "empty". Each chapter's own README has the two commands
that confirm the images in its deck are exactly the ones it drew, and the same
for its notes PDF.

Charts are also the only block a run card can cut whole, so **never write a
slide that refers back to a chart**, the same rule and the same reason as for
a check.

## This repository is public and the course text is not ours

The textbook, the publisher's scans, the previous course holder's decks, and
**the book's figures** are third-party copyrighted works. None of them may be
committed. Figure artwork lives in the gitignored `assets/figures/`, and
figures are off by default so the plain build always reproduces the committed
text decks. `--with-figures` is refused anywhere inside the repository, for
either edition. Before committing a deck, confirm it embeds no artwork that is
not ours: `unzip -l <deck>.pptx | grep ppt/media` must list exactly that
chapter's own charts and nothing else. See the section above for the hash
check that proves which ones they are.

Every chapter inherits the constraint. See the chapter's own `README.md` for
the build commands and the figure file naming.

## Two print documents, for two different readers

Do not merge them, and do not let content leak between them.

| Document | Reader | Built by | Content |
|---|---|---|---|
| `chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf` | The instructor | `build/build_plan.py` | `build/plan_chapter01.py` |
| `chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf` | The students | `build/build_lecture_notes.py` | `build/lecture_chapter01.py` |
| `chapter-02/FIN1209-Chapter-02-Run-Card.pdf` | The instructor | `build/build_plan2.py` | `build/plan_chapter02.py` |
| `chapter-02/FIN1209-Chapter-02-Lecture-Notes.pdf` | The students | `build/build_lecture_notes2.py` | `build/lecture_chapter02.py` |

The **instructor's document** carries timing, cuts, speaker cues, check
answers and slide numbers. The **lecture notes** are the student facing record
of the content: prose, the figures, every term defined once, the review
questions. A slide number or a minute count in the lecture notes means it is
in the wrong document.

**The instructor's document is three pages from Chapter 2 onwards, not
twenty six.** The captain taught from Chapter 1's 26 page teaching plan on
2026-09-02 and said plainly that he did not really use it, and the problem it
was built to solve happened anyway: 180 minutes, and he reached the end of
Part 4 of 6. Do not build another one. `build/plan_chapter02.py` is the shape
and `TEMPLATE.md` has the three things a run card does.

**Cost the minutes rather than guessing them, and print the honest total.**
The rate is calibrated on what happened in the room: Chapter 1's openers plus
its first four parts is 155 slides, and 155 slides is what 180 minutes bought.
Chapter 2 comes to 202 minutes at that rate and its run card says so, then
names exactly which twenty three minutes come out to land it at 180.
`chapter-02/README.md` has the arithmetic.

Layout lives in `build/notekit.py` and `build/lecturekit.py`, which know
nothing about any chapter; lecturekit takes the FEU palette and the paginator
from notekit rather than copying either. `build/chrome.py` renders both.

Both PDFs are checked against the deck, which is the authority on scope, so
**rebuild both whenever you rebuild the deck**. The plan names slides by key
and resolves them. The notes name figures, charts and terms, and the build
fails if the notes reference a figure or a chart the deck does not place, if
either is never mentioned in the prose, or if the deck teaches a term the
notes never define.
The notes take their summary and review questions from the deck's closing
slides instead of holding a copy.

`build/README.md` covers the sharp edges: headless Chrome writes the PDF and
then never exits, so the build polls for the file instead of waiting on the
process; pagination is done by a script inside the page, not by Chrome; and
the notes turn on three paginator behaviors the plan deliberately does not.

**Render every finished PDF back to images and look at every page before you
commit it**, and for the lecture notes look at both the placeholder build and
the figure build. An earlier notes PDF was committed without anyone viewing a
rendered page and two of its pages were unusable; later, the figure build
overflowed every image on top of its own caption while the placeholder build
looked perfect. `chapter-01/teaching-plan-design.md` and
`chapter-01/lecture-notes-design.md` record the research each design came
from, with sources.

## A cut has to be executable while standing up

This is what Chapter 1's teaching plan got wrong twice, and what the Chapter 2
run card is built to get right.

**A cut nobody can act on is not a cut.** Chapter 1 spread five run plans
across sixteen part pages, and an audit still found the plan carrying a 180
minute column while every cut marker said "cut at Long", so a part page told
the instructor to run 31 minutes of material in a 25 minute box. Chapter 2
names every cut slide by slide instead, resolved against the deck, so the card
cannot print a wrong number.

**Nothing on the floor may be cuttable, and nothing cuttable may carry a
check.** Before you write a run card, confirm it: no check item may rest on a
chart or on any figure the first cut drops.
`chapter-02/check-answerability-audit.md` is that confirmation for Chapter 2
and it is why the card can drop all eight charts as one block.

## A check must be answerable from the slides alone

The student edition carries no speaker notes, so a fact that lives only in a
cue is a fact the student never meets, and nothing in the room guarantees the
instructor said it anyway. The same goes for the lecture notes and the book.
**When you add or move a check item, the slide that supplies its answer has to
come before the check**, and no build check enforces either half of that.

`chapter-01/check-answerability-audit.md` is the item by item record and the
two failures it found: a check that sat in front of the slide it examined, and
a term the question named that only the speaker note ever said out loud. Both
failure modes are invisible to `deckkit.validate()`.
`chapter-02/check-answerability-audit.md` is the same audit run before the
chapter shipped rather than after, which is the order to work in. Its 42 items
all pass. Write one for every chapter.

The answer key rules are enforced: no letter over 35 percent or under 15, and
no three identical answers in a row. Those cannot regress silently.

## The closing slides are not validated

`deckkit.validate()` walks `chapter.sections` only, so the `CLOSING` tuple in
`build/content_chapter01.py` escapes every design rule: the six line limit, the
em dash ban and the safe bottom check. A closing slide that overflows the page
builds clean and then collides with the progress marker in the room. When you
edit one, call `deckkit._content_bottom()` on it by hand and compare against
`deckkit.SAFE_BOTTOM`. The review questions slide already sits at 6.53in
against a 6.50in limit, so it has no headroom at all.

## The two PDFs are not byte-reproducible; the decks are

A deck rebuild with no content change leaves `git status` clean. A rebuild of
either PDF does not: headless Chrome stamps its own identifiers into the file,
so the bytes move while the content does not. Before committing a PDF churn,
compare the text (`pdftotext old.pdf - | diff - <(pdftotext new.pdf -)`) and
revert the file if only the bytes changed.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
