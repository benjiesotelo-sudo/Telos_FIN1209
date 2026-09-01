# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Start at TEMPLATE.md if you are building a chapter

`TEMPLATE.md` at the repository root is what whoever writes Chapter 2 reads
first: which files to copy and which to write fresh, the content module's
structure, the non-negotiable teaching design rules, the copyright split, the
three build commands, and the verification steps. This file carries only the
sharp edges; that one carries the method.

## Teach only what the textbook teaches

The instructor's standing rule, and it outranks everything else here. Where
Lim's chapter defines a term, use the book's definition. Where the book is
silent, ambiguous, or contradicts itself, say so plainly on the slide and in
the notes rather than importing a definition or narrating events the book does
not. The worked example is `Supply side and demand side` in
`build/content_chapter01.py`: the book never defines the pair, so the deck
teaches the gap, marks the outside readings non-examinable, and sets no
question on either.

## The deck ships in two editions from one content file

`build/build_chapter1.py` takes `--edition teaching` (the default, 227 slides,
everything) or `--edition student` (177 slides, every check and reveal dropped
and no speaker notes). One content module feeds both; nothing is forked and
nothing is deleted from `build/content_chapter01.py`. The switch lives in
`deckkit.build()` and knows nothing about any chapter, so a later chapter
inherits it by copying the build script.

The one rule this puts on content: **never write a slide that refers back to a
check.** "As the last question showed" is true in one edition and false in the
other, and no build check catches it. `build/README.md` has the mechanics and
`chapter-01/README.md` the two commands.

## The decks are generated, never hand-edited

Editing a `.pptx` is a dead end; the next build overwrites it. Change
`build/content_chapter01.py` (pure data) and rebuild. Drawing code lives only
in `build/deckkit.py`, which knows nothing about any chapter. `build/README.md`
has the environment, the design rules the build enforces, and the fonts.

## Our own charts are committed. The book's figures never are.

Part 1 carries nine charts this course drew, one on a companion slide after
each of its term slides. They are the opposite case to the textbook figures in
every respect, and the two must not be conflated:

| | Book figure | Our chart |
|---|---|---|
| Type | `deckkit.Figure` | `deckkit.Chart`, not a subclass |
| Named | `1.11`, the book's scheme | `Chart C`, our namespace |
| Credit | Wiley, hard coded on `Figure.credit` | `deckkit.chart_credit()`, one place |
| In the repo | Never. `assets/figures/` is gitignored | Always, drawn at build time |
| Committed build | Placeholder | The real artwork |

`build/chartkit.py` draws them and knows nothing about any chapter;
`build/charts_chapter01.py` is the data. Every build of the deck and of the
lecture notes redraws all nine first, so a fresh clone gets the real slide.
The data is invented from fixed seeds, because we hold no market data licence,
and every chart says so in its credit line.

The one trap: the committed decks now embed nine PNGs, so the artwork check
before a commit is no longer "empty". `build/README.md` has the two commands
that confirm the nine images in a deck are exactly the nine we drew, and
`chapter-01/README.md` the same for the notes PDF.

Charts are also the only block a run plan can cut whole, so **never write a
slide that refers back to a chart**, the same rule and the same reason as for
a check.

## This repository is public and the course text is not ours

The textbook, the publisher's scans, the previous course holder's decks, and
**the book's figures** are third-party copyrighted works. None of them may be
committed. Figure artwork lives in the gitignored `assets/figures/`, and
figures are off by default so the plain build always reproduces the committed
text decks. `--with-figures` is refused anywhere inside the repository, for
either edition. Before committing a deck, confirm it embeds no artwork that is
not ours: `unzip -l <deck>.pptx | grep ppt/media` must list exactly the nine
charts and nothing else. See the section above for the hash check that proves
which nine they are.

Every chapter after this one inherits the constraint. See
`chapter-01/README.md` for the build commands and the figure file naming.

## Two print documents, for two different readers

Do not merge them, and do not let content leak between them.

| Document | Reader | Built by | Content |
|---|---|---|---|
| `chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf` | The instructor | `build/build_plan.py` | `build/plan_chapter01.py` |
| `chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf` | The students | `build/build_lecture_notes.py` | `build/lecture_chapter01.py` |

The **teaching plan** is a run card: timing, run plans, cut tiers, speaker
cues, check answers, slide numbers. The **lecture notes** are the student
facing record of the content: prose, the figures, every term defined once, the
review questions. A slide number or a minute count in the lecture notes means
it is in the wrong document.

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
