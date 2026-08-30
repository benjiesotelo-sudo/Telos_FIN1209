#!/usr/bin/env python3
"""Build the FIN1209 Chapter 1 student lecture notes as a print-ready PDF.

    .venv/bin/python build/build_lecture_notes.py

This is the student-facing document: a readable record of what the lesson
covered, with the figures, every term defined once, a summary and the book's
review questions. The instructor's document is a different artifact, built by
build/build_plan.py.

Content is data in build/lecture_chapter01.py. Layout is build/lecturekit.py,
which knows nothing about any chapter. This script wires the two together and
checks the notes against the deck, which is the authority on scope: a figure
the deck does not place, or a term the deck teaches and the notes never
define, fails the build.

Chapters 2 to 10 are a content file away, not a rewrite.

The figures are Wiley's and this repository is public, so the plain build
renders a placeholder in each figure's place and that is what is committed.
The teaching copy, with the artwork, goes outside the repository:

    .venv/bin/python build/build_lecture_notes.py --with-figures \\
        --out ~/FIN1209-Chapter-01-Lecture-Notes.pdf

After building, look at the result. Every page:

    DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
    $DATA/pdfpng chapter-01/FIN1209-Chapter-01-Lecture-Notes.pdf /tmp/ln \\
        $(seq 1 18)

See chapter-01/lecture-notes-design.md for why the document looks the way it
does, and for the research it came from.
"""

from __future__ import annotations

import argparse
import dataclasses
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chrome  # noqa: E402
import deckkit  # noqa: E402
import lecturekit  # noqa: E402
from content_chapter01 import CHAPTER  # noqa: E402
from lecture_chapter01 import NOTES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PDF_OUT = REPO / "chapter-01" / "FIN1209-Chapter-01-Lecture-Notes.pdf"
FIGURES_DIR = REPO / "assets" / "figures"


def deck_facts(chapter) -> tuple[dict[str, str], dict[str, str], list[str]]:
    """What the deck says exists: figure numbers, their descriptions, terms.

    The lecture notes never retype a figure description. It comes from here,
    which is the same line the deck's own placeholder prints, so the two
    documents cannot describe the same figure differently.
    """
    shows: dict[str, str] = {}
    files: dict[str, str] = {}
    terms: list[str] = []
    for section in chapter.sections:
        for slide in section.slides:
            if isinstance(slide, deckkit.Figure):
                shows[slide.number] = slide.shows
                files[slide.number] = slide.filename
            elif isinstance(slide, deckkit.Term):
                terms.append(slide.term)
    return shows, files, terms


# The two closing slides the notes reproduce verbatim, by title.
SUMMARY_SLIDE = "Chapter 1 in five sentences"
REVIEW_SLIDE = "The review questions to prepare"


def deck_closing(chapter) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """The summary and the review questions, taken from the deck's own closing.

    These are the book's, not ours, and the deck is where they are maintained.
    Reading them here rather than retyping them in the content module is what
    stops the notes shipping last term's review questions after somebody edits
    the closing slide: when the audit changed that slide from six questions to
    six lines carrying all eight, the notes went stale silently.
    """
    found: dict[str, tuple[str, ...]] = {}
    for slide in chapter.closing:
        title = getattr(slide, "title", "")
        if title in (SUMMARY_SLIDE, REVIEW_SLIDE):
            found[title] = tuple(getattr(slide, "lines", ()))
    missing = [t for t in (SUMMARY_SLIDE, REVIEW_SLIDE) if not found.get(t)]
    if missing:
        raise SystemExit(
            "the deck's closing no longer carries " + " and ".join(missing)
            + ". The lecture notes reproduce those slides, so rename them here "
            "and in build_lecture_notes.py together."
        )
    return found[SUMMARY_SLIDE], found[REVIEW_SLIDE]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PDF_OUT)
    parser.add_argument("--chrome", type=Path, default=chrome.CHROME)
    parser.add_argument(
        "--with-figures", action="store_true",
        help=("Place the textbook artwork instead of placeholders. Off by "
              "default: the figures are Wiley's, they are not committed, and "
              "the plain build has to keep reproducing the committed PDF."),
    )
    parser.add_argument(
        "--figures-dir", type=Path, default=FIGURES_DIR,
        help="Folder holding the artwork, used only with --with-figures.",
    )
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside the PDF, for inspection",
    )
    args = parser.parse_args()

    if args.with_figures and not args.figures_dir.is_dir():
        parser.error(
            f"--with-figures was given but {args.figures_dir} does not exist. "
            "The textbook figures are copyrighted and are not in this "
            "repository; see chapter-01/README.md. Drop the flag to build the "
            "placeholder version."
        )
    if args.with_figures and args.out.resolve() == PDF_OUT.resolve():
        parser.error(
            "the committed lecture notes are the placeholder build and must "
            "stay that way, because the figures are copyrighted. Give --out a "
            "path outside this repository for the students' copy."
        )
    if args.with_figures and REPO in args.out.resolve().parents:
        parser.error(
            "--with-figures writes copyrighted artwork into the PDF, so it "
            "cannot be aimed anywhere inside this repository."
        )

    shows, files, terms = deck_facts(CHAPTER)
    summary, review = deck_closing(CHAPTER)
    figures = lecturekit.FigureFacts(
        shows=shows,
        files=files,
        directory=args.figures_dir if args.with_figures else None,
    )

    # The summary and the review questions are the deck's, not the content
    # module's. See deck_closing.
    notes = dataclasses.replace(NOTES, summary=summary, review_questions=review)

    document = lecturekit.render(notes, figures)

    problems = lecturekit.validate(document, notes, shows, terms)
    if problems:
        raise SystemExit(
            "Lecture notes design rules violated:\n  " + "\n  ".join(problems)
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "lecture-notes.html"
        html_path.write_text(document, encoding="utf-8")
        chrome.render_pdf(html_path, args.out, args.chrome)
        if args.keep_html:
            kept = args.out.with_suffix(".html")
            shutil.copyfile(html_path, kept)
            print(f"html   : {kept}")

    pages = chrome.page_count(args.out)
    words = len(notes.prose().split())
    placed = figures.placed() if args.with_figures else 0

    print(f"notes  : {_relative(args.out)}")
    print(f"pages  : {pages}")
    print(f"words  : {words} of body prose")
    print(f"figures: {len(notes.figure_numbers())} placed in "
          f"{sum(1 for s in notes.sections for b in s.blocks if isinstance(b, lecturekit.Fig))}"
          f" blocks, artwork {placed} of {len(notes.figure_numbers())}")
    print(f"terms  : {len(notes.terms())} defined, checked against the deck")
    print(f"closing: {len(summary)} summary lines and {len(review)} review "
          f"questions, taken from the deck")
    print(f"source : {args.figures_dir if args.with_figures else 'placeholders, no artwork'}")
    print("look at it: every page, as an image, before you commit it.")
    return 0


def _relative(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(REPO))
    except ValueError:
        return str(p)


if __name__ == "__main__":
    raise SystemExit(main())
