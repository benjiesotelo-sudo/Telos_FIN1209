#!/usr/bin/env python3
"""Build the FIN1209 Chapter 4 lecture deck.

Deterministic and re-runnable: it regenerates the deck from scratch on every
run, so the committed artefact is always exactly what this script produces
from build/content_chapter04.py.

    .venv/bin/python build/build_chapter4.py

Chapter 4 is a trial of a leaner deck, and it ships one document: the
teaching edition. There is no student edition, no answer sheet, no run card
and no lecture notes for it. The --edition switch is still here because it
lives in deckkit and costs nothing to keep, but the student build is not
part of this chapter and is not committed.

This script is build_chapter3.py with three things changed. It does not
write an answer sheet, because the trial is of the deck alone. It checks the
closing slides against the page, which deckkit.validate() does not do. And
it prints what the deck costs in minutes at the project's calibrated rate,
so the number in chapter-04/README.md is one this script produced.

The textbook figures are not ours and stay out of the repository. See
chapter-04/README.md for the two commands and build/README.md for the
environment.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chartkit  # noqa: E402
import deckkit  # noqa: E402
from charts_chapter04 import CHARTS  # noqa: E402
from content_chapter04 import CHAPTER  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DECK_OUT = REPO / "chapter-04" / "FIN1209-Chapter-04.pptx"
STUDENT_OUT = REPO / "chapter-04" / "FIN1209-Chapter-04-Student-Edition.pptx"

# The committed file each edition writes when --out is not given.
DEFAULT_OUT = {deckkit.TEACHING: DECK_OUT, deckkit.STUDENT: STUDENT_OUT}

# The textbook figures are Wiley's. They are not in this repository, the folder
# is gitignored, and figures are OFF by default on purpose: the plain build has
# to keep reproducing the committed deck exactly, on this machine and on a
# clean clone alike. Pass --with-figures for the instructor's teaching deck.
# Either way the slide count, the progress markers and the checks are identical.
# See chapter-04/README.md for the two commands.
FIGURES_DIR = REPO / "assets" / "figures"

# The charts this course draws for itself are the opposite case to the
# figures: they are ours, so they are generated here from committed code on
# every build and placed in both editions unconditionally. The folder is
# gitignored because it is output, not because anything in it is anyone
# else's. See build/chartkit.py.
#
# One folder per chapter, because the letters restart at A in every chapter
# and a shared folder would have Chapter 4's Chart A overwrite another chapter's.
# That would also break the check in both READMEs that the images inside a
# committed deck are exactly the ones its own chapter drew. Chapter 1's
# folder is plain "charts"; every chapter after it is numbered.
CHARTS_DIR = REPO / "build" / "generated" / "charts-04"


def check_frame(parser) -> None:
    """Hold the closing slides to the rules deckkit holds a section slide to.

    deckkit.validate() walks the sections and the chapter's own opening
    slides and never the closing tuple, so a closing slide that runs off the
    page, or carries a dash, builds clean. AGENTS.md says to check those by
    hand; this is that check, run on every build.
    """
    problems = []
    for i, slide in enumerate(CHAPTER.closing, start=1):
        where = f"closing slide {i}"
        texts = [slide.title, slide.accent, *slide.lines, *slide.notes,
                 getattr(slide, "caption", "")]
        if any("\u2014" in t or "\u2013" in t for t in texts):
            problems.append(f"{where}: dash character not allowed")
        if len(slide.lines) > deckkit.MAX_BODY_LINES:
            problems.append(f"{where}: {len(slide.lines)} body lines")
        if isinstance(slide, deckkit.Content):
            bottom = deckkit._content_bottom(slide)
            if bottom > deckkit.SAFE_BOTTOM:
                problems.append(
                    f"{where}: content runs to {bottom:.2f}in, past the "
                    f"{deckkit.SAFE_BOTTOM}in safe bottom")
    if problems:
        parser.error("closing slides break the design rules:\n  "
                     + "\n  ".join(problems))


# The per slide weights written down in chapter-03/README.md, and the factor
# that turns them into minutes. Both are calibrated on what a room actually
# got through, so they are copied here and not adjusted.
WEIGHTS = {deckkit.Content: 1.0, deckkit.Term: 1.25, deckkit.Quote: 1.0,
           deckkit.Figure: 0.75, deckkit.Chart: 0.5, deckkit.Check: 2.5}
FRAME_WEIGHT = 1.0
MINUTES_PER_WEIGHT = 1.150


def _weight(slide) -> float:
    """A Pair is costed as the sum of its two parts: putting a picture
    beside its idea saves a click and not the talking."""
    if isinstance(slide, deckkit.Pair):
        return _weight(slide.left) + _weight(slide.picture)
    for kind, weight in WEIGHTS.items():
        if isinstance(slide, kind):
            return weight
    raise TypeError(f"no weight for {type(slide).__name__}")


def cost() -> list[tuple[str, int, float]]:
    """(part, slides, minutes) for the opening, every section and the
    closing, at the calibrated rate."""
    rows = [("Title, objectives, roadmap", 1 + len(CHAPTER.openers or ()),
             (1 + len(CHAPTER.openers or ())) * FRAME_WEIGHT)]
    for section in CHAPTER.sections:
        slides = sum(2 if isinstance(s, deckkit.Check) else 1
                     for s in section.slides)
        rows.append((section.short, slides,
                     sum(_weight(s) for s in section.slides)))
    rows.append(("Closing", len(CHAPTER.closing),
                 len(CHAPTER.closing) * FRAME_WEIGHT))
    return [(name, slides, weight * MINUTES_PER_WEIGHT)
            for name, slides, weight in rows]


def _relative(path: Path) -> str:
    """Repository relative when it is inside the repository, absolute when the
    instructor's own deck is written outside it."""
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--display-font",
        default=deckkit.DISPLAY_FONT,
        help=("Typeface for titles and section dividers. Defaults to the FEU "
              "identity face; use a serif such as Palatino if it is not installed."),
    )
    parser.add_argument(
        "--edition",
        choices=deckkit.EDITIONS,
        default=deckkit.TEACHING,
        help=("teaching (default) is the full deck with the checks, the "
              "reveals and the speaker cues. student drops all of those and "
              "is the file that can be handed out."),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=("Where to write the deck. Defaults to the committed file for "
              "the chosen edition."),
    )
    parser.add_argument(
        "--with-figures",
        action="store_true",
        help=("Place the textbook artwork instead of placeholders. Off by "
              "default: the figures are Wiley's, they are not committed, and "
              "the plain build must keep reproducing the committed deck."),
    )
    parser.add_argument(
        "--figures-dir",
        type=Path,
        default=FIGURES_DIR,
        help="Folder holding the artwork, used only with --with-figures.",
    )
    args = parser.parse_args()
    if args.out is None:
        args.out = DEFAULT_OUT[args.edition]

    figures_dir = args.figures_dir if args.with_figures else None
    if figures_dir is not None and not figures_dir.is_dir():
        parser.error(
            f"--with-figures was given but {figures_dir} does not exist. "
            "The textbook figures are copyrighted and are not in this "
            "repository; see chapter-04/README.md. Drop the flag to build "
            "the placeholder deck."
        )
    # Both committed decks are placeholder builds, so the guard is the whole
    # repository and not just one filename: neither edition may take the
    # artwork inside it.
    if args.with_figures and (args.out.resolve() == REPO
                              or REPO in args.out.resolve().parents):
        parser.error(
            "the committed decks are the placeholder builds and must stay "
            "that way, because the figures are copyrighted. Give --out a "
            "path outside this repository for a deck with the artwork."
        )

    check_frame(parser)

    # Drawn before the deck, and every time, so a clone that has never built
    # anything still gets the real artwork on the first run.
    chartkit.generate(CHARTS, CHARTS_DIR, display_font=args.display_font)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    slides, checks = deckkit.build(CHAPTER, args.out,
                                   display_font=args.display_font,
                                   figures_dir=figures_dir,
                                   charts_dir=CHARTS_DIR,
                                   edition=args.edition)
    total_checks = sum(1 for _ in deckkit.iter_checks(CHAPTER))

    status = deckkit.figure_status(CHAPTER, figures_dir)
    placed = [n for n, _f, have in status if have]
    missing = [n for n, _f, have in status if not have]

    print(f"deck   : {_relative(args.out)}")
    print(f"edition : {args.edition}")
    print(f"slides : {slides}")
    if checks:
        print(f"checkpoints : {checks} ({checks * 2} multiple choice items)")
    else:
        print(f"checkpoints : 0, and no speaker notes. "
              f"{total_checks} checks omitted.")
    print(f"figures : {len(placed)} placed, {len(missing)} as placeholders "
          f"(of {len(status)} figure slides)")
    if missing:
        print("        : " + ", ".join(missing))
    charts = deckkit.chart_status(CHAPTER, CHARTS_DIR)
    print(f"charts : {sum(1 for *_r, have in charts if have)} of "
          f"{len(charts)} drawn and placed "
          f"({', '.join(letter for letter, _f, _h in charts)})")
    print(f"figure source : {figures_dir or 'none, placeholder build'}")
    print(f"chart source : {_relative(CHARTS_DIR)}, generated by this build"
          if charts else "chart source : none, this chapter draws no charts")
    print(f"display font : {args.display_font}")
    rows = cost()
    print(f"minutes : {sum(m for _n, _s, m in rows):.1f} at the calibrated "
          f"rate, over {sum(n for _p, n, _m in rows)} slides")
    for name, count, minutes in rows:
        print(f"        : {name:<28} {count:>3} slides {minutes:>6.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
