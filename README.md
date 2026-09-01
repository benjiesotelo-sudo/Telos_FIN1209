# FIN1209 - Technical Analysis in Investment

Course workspace for FIN1209, Institute of Accounts, Business and Finance, FEU Manila.
Taught by Benjamin C. Sotelo.

## The course

Three units, 54 hours, elective. This semester covers Chapters 1 to 10 of the course text:
Lim, M. (2016). *The Handbook of Technical Analysis*. John Wiley & Sons.

Assessment weighting from the course booklet: class participation 20 percent, quizzes 30 percent, major examinations the balance.
Official delivery runs on Canvas; this repository is the preparation workspace.

## What is here

| Path | What it is |
|---|---|
| `TEMPLATE.md` | How to build the next chapter. Read it first. |
| `chapter-01/` | The Chapter 1 deck, the instructor's teaching plan, the students' lecture notes, and the in-class checks |
| `build/` | The scripts that generate all four |

The deck, the teaching plan and the lecture notes are three views of one
chapter, generated from the same content files. The teaching plan is the
instructor's run card; the lecture notes are what students read to revise or
to catch up. See `chapter-01/README.md`.

## What is deliberately not here

Source material inherited from the previous course holder is not committed.
That includes the textbook PDF, the publisher's scanned chapters, the FEU course booklet, and the previous holder's own lecture decks and assessments.
Those are third-party copyrighted works and stay outside version control.
Answer keys for graded assessments are also kept out of this repository.

The textbook figures are third-party copyrighted works too, so they are not committed either.
The decks place them from `assets/figures/`, which is gitignored and absent here.
In the committed deck every figure slide renders a placeholder carrying the figure number, what the figure shows, the credit line and the speaker cue, so the chapter stays complete and rebuildable without the artwork.
See `chapter-01/README.md` for the command that builds each version.

The charts this course draws for itself are a different matter. They are ours,
so they are generated from code in this repository on every build and they are
in the committed deck and the committed lecture notes with their artwork in
place. They are lettered and credited separately from the book's figures, and
their data is invented rather than taken from any market.

## Teaching design

Slides are built for a class that includes students with ADHD:

- One idea per slide, never a wall of text.
- Every new term glossed in plain language, with a concrete example before the formal definition.
- A visible progress marker so students always know where they are.
- A two-question multiple choice check after every two or three new terms, with the answer revealed on the following slide.
- Where a term is being explained, a chart of it on the slide immediately after. Chapter 1 Part 1 is the pilot: nine terms, nine charts.
