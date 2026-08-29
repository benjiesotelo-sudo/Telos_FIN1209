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

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
