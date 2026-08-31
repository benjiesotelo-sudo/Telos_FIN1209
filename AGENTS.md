# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## The decks are generated, never hand-edited

Editing a `.pptx` is a dead end; the next build overwrites it. Change
`build/content_chapter01.py` (pure data) and rebuild. Drawing code lives only
in `build/deckkit.py`, which knows nothing about any chapter. `build/README.md`
has the environment, the design rules the build enforces, and the fonts.

## This repository is public and the course text is not ours

The textbook, the publisher's scans, the previous course holder's decks, and
**the book's figures** are third-party copyrighted works. None of them may be
committed. Figure artwork lives in the gitignored `assets/figures/`, and
figures are off by default so the plain build always reproduces the committed
text deck. `--with-figures` is refused when it is aimed at a committed deck
path. Before committing a deck, confirm it embeds no artwork:
`unzip -l <deck>.pptx | grep ppt/media` must be empty.

Every chapter after this one inherits the constraint. See
`chapter-01/README.md` for the two build commands and the figure file naming.

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
and resolves them. The notes name figures and terms, and the build fails if
the notes reference a figure the deck does not place, if a figure is never
mentioned in the prose, or if the deck teaches a term the notes never define.
The notes take their summary and review questions from the deck's closing
slides instead of holding a copy.

`build/README.md` covers the sharp edges: headless Chrome writes the PDF and
then never exits, so the build polls for the file instead of waiting on the
process; pagination is done by a script inside the page, not by Chrome; and
the notes turn on three paginator behaviours the plan deliberately does not.

**Render every finished PDF back to images and look at every page before you
commit it**, and for the lecture notes look at both the placeholder build and
the figure build. An earlier notes PDF was committed without anyone viewing a
rendered page and two of its pages were unusable; later, the figure build
overflowed every image on top of its own caption while the placeholder build
looked perfect. `chapter-01/teaching-plan-design.md` and
`chapter-01/lecture-notes-design.md` record the research each design came
from, with sources.

## The closing slides are not validated

`deckkit.validate()` walks `chapter.sections` only, so the `CLOSING` tuple in
`build/content_chapter01.py` escapes every design rule: the six line limit, the
em dash ban and the safe bottom check. A closing slide that overflows the page
builds clean and then collides with the progress marker in the room. When you
edit one, call `deckkit._content_bottom()` on it by hand and compare against
`deckkit.SAFE_BOTTOM`. The review questions slide already sits at 6.53in
against a 6.50in limit, so it has no headroom at all.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
