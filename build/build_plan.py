#!/usr/bin/env python3
"""Build the FIN1209 Chapter 1 teaching plan as a print-ready PDF.

    .venv/bin/python build/build_plan.py

This is the instructor's document. The student-facing lecture notes are a
separate artifact, built by build/build_lecture_notes.py.

Content is data in build/plan_chapter01.py. Layout is build/notekit.py, which
knows nothing about any chapter. This script wires the two together, resolves
every slide reference against the deck's own content so the plan cannot drift
away from the deck, writes HTML with real print CSS, and renders it with
headless Chrome.

Chapters 2 to 10 are a content file away, not a rewrite.

Chrome, and not LibreOffice: see build/chrome.py.

After building, look at the result. Every page:

    DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
    $DATA/pdfpng chapter-01/FIN1209-Chapter-01-Teaching-Plan.pdf /tmp/plan \
        $(seq 1 23)

See chapter-01/teaching-plan-design.md for why the document looks the way it
does.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chrome  # noqa: E402
import deckkit  # noqa: E402
import notekit  # noqa: E402
from content_chapter01 import CHAPTER  # noqa: E402
from plan_chapter01 import PLAN  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PDF_OUT = REPO / "chapter-01" / "FIN1209-Chapter-01-Teaching-Plan.pdf"



# --------------------------------------------------------------------------
# The deck, walked for slide numbers
# --------------------------------------------------------------------------


def index_deck(chapter) -> tuple[dict[str, int], dict[int, str],
                                notekit.DeckFacts, list[str]]:
    """Number every slide exactly the way deckkit.build numbers them.

    Returns the key to slide-number map, the check answer letters, the counts
    the plan quotes, and any ambiguous keys.

    This deliberately mirrors the traversal in deckkit.build rather than
    opening the .pptx: the plan is built from the same source the deck is,
    so a content change moves both together.
    """
    slides: dict[str, int] = {}
    answers: dict[int, str] = {}
    part_checks: dict[int, list[int]] = {}
    collisions: list[str] = []
    n = 0

    def put(key: str) -> None:
        nonlocal n
        if key in slides:
            collisions.append(key)
            return
        slides[key] = n

    n += 1                                   # 1, title
    put("open:title")
    for i in range(0, len(chapter.objectives), 4):
        n += 1                               # 2 and 3, learning objectives
        put(f"open:objectives{i // 4 + 1}")
    n += 1                                   # 4, roadmap
    put("open:roadmap")

    check_index = 0
    figures = 0
    charts = 0
    for section in chapter.sections:
        n += 1
        put(f"part:{section.number}")
        quote_index = 0
        for slide in section.slides:
            if isinstance(slide, deckkit.Check):
                check_index += 1
                n += 1
                put(f"check:{check_index}")
                n += 1
                put(f"reveal:{check_index}")
                answers[check_index] = "".join(
                    q.answer for q in slide.questions
                )
                part_checks.setdefault(section.number, []).append(check_index)
                continue
            n += 1
            if isinstance(slide, deckkit.Figure):
                figures += 1
                put(f"fig:{slide.number}")
            elif isinstance(slide, deckkit.Chart):
                # Our own charts have their own namespace in the deck, so
                # they get their own key space here too. {s:chart:C} is the
                # slide carrying Chart C, and it can never collide with a
                # book figure number.
                charts += 1
                put(f"chart:{slide.letter}")
            elif isinstance(slide, deckkit.Term):
                put(f"term:{slide.term}")
            elif isinstance(slide, deckkit.Quote):
                # Quotes repeat their source, so they are named by their
                # position within the part: quote:2:4 is the fourth quote
                # slide in Part 2.
                quote_index += 1
                put(f"quote:{section.number}:{quote_index}")
            elif isinstance(slide, deckkit.Content):
                put(f"slide:{slide.title}")
        n += 1
        put(f"recap:{section.number}")

    for slide in chapter.closing:
        n += 1
        title = getattr(slide, "title", "")
        if title:
            put(f"slide:{title}")

    facts = notekit.DeckFacts(
        total_slides=n,
        total_checks=check_index,
        total_figures=figures,
        total_charts=charts,
        part_checks=part_checks,
    )
    return slides, answers, facts, collisions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PDF_OUT)
    parser.add_argument("--chrome", type=Path, default=chrome.CHROME)
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside the PDF, for inspection",
    )
    args = parser.parse_args()

    slides, answers, facts, collisions = index_deck(CHAPTER)
    if collisions:
        print("warning: ambiguous slide keys, first occurrence wins: "
              + ", ".join(sorted(set(collisions))), file=sys.stderr)

    res = notekit.Resolver(slides, answers)
    document = notekit.render(PLAN, res, facts)

    problems = notekit.validate(document, res)
    if problems:
        raise SystemExit(
            "Teaching plan design rules violated:\n  " + "\n  ".join(problems)
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "plan.html"
        html_path.write_text(document, encoding="utf-8")
        chrome.render_pdf(html_path, args.out, args.chrome)
        if args.keep_html:
            kept = args.out.with_suffix(".html")
            shutil.copyfile(html_path, kept)
            print(f"html   : {kept.relative_to(REPO)}")

    pages = chrome.page_count(args.out)
    print(f"plan   : {args.out.relative_to(REPO)}")
    print(f"pages  : {pages}")
    print(f"deck   : {facts.total_slides} slides, {facts.total_checks} checks, "
          f"{facts.total_figures} figures, {facts.total_charts} charts")
    print(f"keys   : {len(slides)} slide references resolvable")
    print("look at it: every page, as an image, before you commit it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
