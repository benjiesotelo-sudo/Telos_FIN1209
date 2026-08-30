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

## The teaching notes are generated too

`chapter-01/FIN1209-Chapter-01-Notes.pdf` is built by `build/build_notes.py`
from `build/notes_chapter01.py` (content) and `build/notekit.py` (layout). The
old hand-written `chapter-01/lecture-notes.md` is retired.

The notes never store a slide number. They name slides by key and the build
resolves them against `build/content_chapter01.py`, so **rebuild the notes
whenever you rebuild the deck**. `build/README.md` covers the two sharp edges:
headless Chrome writes the PDF and then never exits, so the build polls for the
file instead of waiting on the process; and pagination is done by a script
inside the page, not by Chrome.

**Render the finished PDF back to images and look at every page before you
commit it.** The previous notes PDF was committed without anyone viewing a
rendered page, and two of its pages were unusable. `chapter-01/notes-design.md`
records the research the design came from.

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
