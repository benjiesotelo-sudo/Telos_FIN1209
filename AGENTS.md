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

The FEU course booklet is the authority on hours and assessment weighting, not
on tooling: it contradicts itself over whether a Bloomberg terminal is
involved. Assume no paid terminal; Activity 1 needs only a browser, a Google
Sheet and a free charting site.

## Three chapters are built; copy the newest

Chapter 1 is 227 slides, Chapter 2 is 175 and Chapter 3 is 188. Chapters 2
and 3 are the same design done again; `TEMPLATE.md` says which files to copy
and what each chapter changed.

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

Chapter 1 carries nine charts this course drew, Chapter 2 eight and Chapter 3
six, each on a companion slide after the term it illustrates. They are the
opposite case to the textbook figures in every respect, and the two must not be
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
`charts-02`, `charts-03` after it. The letters restart at A in every chapter
and a shared folder would have one chapter's Chart A overwrite another's.

If a chapter needs a chart shape chartkit has not got, **add the form** rather
than editing an existing one; Chapter 2 added seven and Chapter 3 five. After
any kit change,
rebuild every earlier chapter and confirm the decks are byte identical.

The one trap: the committed decks embed those PNGs, so the artwork check
before a commit is not "empty". Each chapter's own README has the two commands
that confirm the images in its deck are exactly the ones it drew, and the same
for its notes PDF.

Charts are also the only block a run card can cut whole, so **never write a
slide that refers back to a chart**, the same rule and the same reason as for
a check.

## The take-home activity is a fourth renderer, and the only live dependency

`build/build_activity.py` writes both `chapter-01/activity/` PDFs from one
content module, with `key=True` turning on the answers and the reveal. Four
renderers now exist and none knows about any chapter: `deckkit`, `notekit`,
`lecturekit`, `activitykit`. `chapter-01/activity/README.md` carries the
method; this file carries the two traps.

**Every picture placed on a page needs a declared height in millimetres.** The
paginator measures a block before printing, and an `<img>` with no height
measures zero until it loads, so five steps landed on one sheet with two
clipped off the bottom and nothing failed. `activitykit.Shots.height_mm`
computes it from the file's own aspect; `lecturekit` does the same for the
book's figures. This is why a rendered page has to be looked at.

**The activity has one live external dependency, and the repository cannot
check it.** Students pull their prices with `IMPORTRANGE` from a Google Sheet
on the instructor's Drive, shared to anyone with the link as a **viewer**. Its
id is printed on the worksheet. If that file is deleted or its sharing
changes, every student gets `#REF!` and no build catches it.
`build/make_source_sheet.py --upload` rebuilds it from the committed CSVs and
prints the new id, which then goes into `SOURCE_SHEET` in
`build/activity_chapter01.py`.

## The written-answer rubric lives once, in `build/rubric.py`

The captain marks every written answer with no single correct response, in
every quiz and activity, with one general rubric: grounded, connected, and
honest (named, never marked), at 100, 75, 50 and 0 percent. **Never retype its
words into a content file.** Hand `rubric.WRITTEN` to the renderer
(`activitykit.written_rubric()` for an activity) and supply only what is the
document's own: which of its marks the rubric decides, and a worked answer at
every level on its own material. A duplicated instruction has already drifted
here once: pen on paper survived into a spreadsheet activity because it lived
in two places. `chapter-01/activity/README.md` has the rest, including why the
worked examples sit on Part A rather than Part B.

## Real market data, in exactly one place

The deck's nine charts are invented from fixed seeds because the course holds
no market data licence. The activity is the exception: its prices are real,
because a reveal drawn from invented numbers would be a lie. It is allowed
only because both FRED series are public domain, which
`build/activity_data.py` records with the licence URL. **Do not treat this as
a precedent for committing price data.** Anything not verifiably public domain
stays out, the same way the Wiley artwork does.

Google Sheets screenshots are committed under Google's standing permission for
screenshots of its products in instructional material. No other platform's
artwork is, and the charting-platform step deliberately ships without a
picture for that reason.

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

**A committed deck is not a teaching deck, and nothing in its filename says
so.** The committed `.pptx` and the committed notes carry the chapter's own
charts and a placeholder where every book figure goes; the teaching artefact is
the `--with-figures` build, which has to be made from a checkout outside this
repository. So never hand a chapter deliverable to a class or an LMS straight
from a repo clone, and check which one you are holding before it leaves:
`unzip -l <deck>.pptx | grep -c ppt/media` is the chapter's chart count for a
committed deck (9 for Chapter 1, 8 for Chapter 2, 6 for Chapter 3), and that
plus one image per placed figure for the real one.

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
| `chapter-03/FIN1209-Chapter-03-Run-Card.pdf` | The instructor | `build/build_plan3.py` | `build/plan_chapter03.py` |
| `chapter-03/FIN1209-Chapter-03-Lecture-Notes.pdf` | The students | `build/build_lecture_notes3.py` | `build/lecture_chapter03.py` |

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
Chapter 2 comes to 202 minutes at that rate and Chapter 3 to 219, and each
run card says so, then names exactly which minutes come out to land at 180.
The per slide weights are written down in `chapter-03/README.md`, with the
check that they reproduce Chapter 2's card.

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

The answer key rules are enforced for the deck's own checks: no letter over 35
percent or under 15, and no three identical answers in a row. Those cannot
regress silently there, but the guard reaches no further; see the next section.

## The term slide check reads low, and the closing slides are not checked

`deckkit._term_bottom()` measures a term slide at a smaller type size than
`render_term` actually uses, so a term the validator puts at 6.44in can render
to 6.89in, past the progress marker, and build clean. Chapter 2 ships three
terms at 6.59in. Chapter 3 holds every term to seven wrapped lines at 19pt,
which is 6.28in rendered. Before trusting a term, add up its rows the way
`render_term` lays them out: from 2.42in, each row is 0.42in plus its wrapped
text plus 0.24in, at the size `render_term` chose, not the one the check did.


`deckkit.validate()` walks `chapter.sections` only, so the `CLOSING` tuple in
`build/content_chapter01.py` escapes every design rule: the six line limit, the
em dash ban and the safe bottom check. A closing slide that overflows the page
builds clean and then collides with the progress marker in the room. When you
edit one, call `deckkit._content_bottom()` on it by hand and compare against
`deckkit.SAFE_BOTTOM`. The review questions slide already sits at 6.53in
against a 6.50in limit, so it has no headroom at all.

The answer key guard has the same blind spot: it tallies `Check` questions
found under `chapter.sections` and nothing else, so a quiz, a worksheet or an
answer sheet produced by any other path is unguarded. Tally those by hand. An
early build of the Chapter 1 key put 37 of 50 answers on B, which scored 74
percent for a student who simply picked B every time.

## Bold in the lecture notes covers whole sentences

The paginator moves a bold element whole and splits prose only at a sentence
end, so a bold phrase in the middle of a sentence lets a page break fall
inside the sentence, and nothing fails. Chapter 3's figure build did it twice.
Bold a whole sentence or nothing, in `Para` text; lists never split.

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
