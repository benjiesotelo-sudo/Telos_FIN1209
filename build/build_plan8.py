#!/usr/bin/env python3
"""Build the FIN1209 Chapter 6 run card as a print-ready PDF.

    .venv/bin/python build/build_plan6.py

This is the instructor's document. The student-facing lecture notes are a
separate artifact, built by build/build_lecture_notes6.py.

Content is data in build/plan_chapter06.py. Layout is build/notekit.py, which
knows nothing about any chapter. This script wires the two together, resolves
every slide reference against the deck's own content so the card cannot drift
away from the deck, writes HTML with real print CSS, and renders it with
headless Chrome.

It is build_plan4.py pointed at Chapter 6. Chapter 4 changed two things from
build_plan3.py, both because it is the lean deck, and Chapter 6 is the same
lean deck.

**The deck is numbered the way the lean deck is built.** Chapter 6 has its
own opening slides, no dividers and no recaps, and nearly every slide is a
Pair: an idea on the left and a picture on the right. A Pair is one slide
with two names, so `{s:slide:Its title}` and `{s:fig:6.24}` resolve to the
same number, and `{s:part:3}` is the first slide of the part, which carries
the book's section number in its title.

**The minutes on the card are checked, not trusted.** build_chapter6.py
costs the deck at the project's calibrated rate. This script costs it the
same way, costs every cut the card names slide by slide, and refuses a card
whose typed minutes disagree with the deck.

One thing differs from build_plan4.py, in check_minutes(). A row of the
clock passes when it is its costed minutes rounded up or down, not only to
the nearest. Chapter 6 has eight rows, and rounding each to the nearest
minute leaves the column a minute short of the chapter's costed total, so
the card could not print a whole-chapter figure that is both the sum of
its rows and the true total. Every total, the whole chapter and each cut,
is still held to the nearest minute.

The card prints no check answers. They are in the instructor's answer sheet,
which build_chapter6.py writes outside this repository.

Chrome, and not LibreOffice: see build/chrome.py.

After building, look at the result. Every page:

    pdftoppm -r 80 -png chapter-06/FIN1209-Chapter-06-Run-Card.pdf /tmp/card

chapter-01/teaching-plan-design.md records the research behind the page
layout, which this card inherits unchanged.
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
import plan_chapter08 as plan  # noqa: E402
from content_chapter08 import CHAPTER_A as CHAPTER, CHAPTER_B  # noqa: E402
import plan_chapter08b  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PDF_OUT = REPO / "chapter-08" / "FIN1209-Chapter-08-Part-A-Run-Card.pdf"


# --------------------------------------------------------------------------
# The deck, walked for slide numbers
# --------------------------------------------------------------------------


def index_deck(chapter) -> tuple[dict[str, int], dict[str, tuple[int, object]],
                                notekit.DeckFacts, list[str]]:
    """Number every slide exactly the way deckkit.build numbers them.

    Returns the key to slide-number map, each key's row of the clock and the
    slide it names, the counts the card quotes, and any ambiguous keys.

    This deliberately mirrors the traversal in deckkit.build rather than
    opening the .pptx: the card is built from the same source the deck is,
    so a content change moves both together.

    No answer letters are collected. This card does not print them.
    """
    slides: dict[str, int] = {}
    where: dict[str, tuple[int, object]] = {}
    part_checks: dict[int, list[int]] = {}
    collisions: list[str] = []
    n = 0
    row = 0                                  # 0 is the opening row of the clock

    def put(key: str, slide=None) -> None:
        if key in slides:
            collisions.append(key)
            return
        slides[key] = n
        where[key] = (row, slide)

    def name(slide) -> None:
        """Every key the slide answers to. A Pair answers to both halves."""
        if isinstance(slide, deckkit.Pair):
            name(slide.left)
            name(slide.picture)
        elif isinstance(slide, deckkit.Figure):
            put(f"fig:{slide.number}", current)
        elif isinstance(slide, deckkit.Chart):
            put(f"chart:{slide.letter}", current)
        elif isinstance(slide, deckkit.Term):
            put(f"term:{slide.term}", current)
        elif isinstance(slide, deckkit.Content):
            put(f"slide:{slide.title}", current)

    n += 1
    put("open:title")
    if chapter.openers is None:
        raise SystemExit("build_plan6.py numbers a deck that brings its own "
                         "opening slides. Use build_plan3.py for the others.")
    for current in chapter.openers:
        n += 1
        name(current)

    check_index = 0
    figures = 0
    charts = 0
    for row, section in enumerate(chapter.sections, start=1):
        if chapter.dividers:
            n += 1
            put(f"part:{section.number}")
        first = True
        for current in section.slides:
            if isinstance(current, deckkit.Check):
                check_index += 1
                n += 1
                put(f"check:{check_index}", current)
                n += 1
                put(f"reveal:{check_index}")
                part_checks.setdefault(section.number, []).append(check_index)
                continue
            n += 1
            if first and not chapter.dividers:
                # No divider: the part starts on its first teaching slide.
                put(f"part:{section.number}")
            first = False
            picture = (current.picture if isinstance(current, deckkit.Pair)
                       else current)
            figures += isinstance(picture, deckkit.Figure)
            charts += isinstance(picture, deckkit.Chart)
            name(current)
        put(f"end:{section.number}")         # the last slide of the part
        if section.recap is not None:
            n += 1
            put(f"recap:{section.number}")

    row = len(chapter.sections) + 1
    for current in chapter.closing:
        n += 1
        name(current)

    facts = notekit.DeckFacts(
        total_slides=n,
        total_checks=check_index,
        total_figures=figures,
        total_charts=charts,
        part_checks=part_checks,
        total_parts=len(chapter.sections),
    )
    return slides, where, facts, collisions


# --------------------------------------------------------------------------
# The minutes, costed from the deck and held against the card
# --------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--part", choices=("A", "B"), default="A", help="A: the first class card, B: the second class card")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--chrome", type=Path, default=chrome.CHROME)
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside the PDF, for inspection",
    )
    args = parser.parse_args()

    chapter = CHAPTER if args.part == "A" else CHAPTER_B
    if args.out is None:
        args.out = PDF_OUT if args.part == "A" else PDF_OUT.with_name("FIN1209-Chapter-08-Part-B-Run-Card.pdf")
    slides, where, facts, collisions = index_deck(chapter)
    if collisions:
        print("warning: ambiguous slide keys, first occurrence wins: "
              + ", ".join(sorted(set(collisions))), file=sys.stderr)

    if args.part == "A":
        p1 = slides["end:1"] - slides["part:1"] + 1
        p2 = slides["end:2"] - slides["part:2"] + 1
        stats = dict(total=facts.total_slides, opening=slides["part:1"] - 1, part1=p1, part2=p2, checks=facts.total_checks)
        assert stats["opening"] + p1 + p2 == facts.total_slides, stats
        the_plan = plan.make(stats)
    else:
        parts = {n: slides[f"end:{n}"] - slides[f"part:{n}"] + 1 for n in range(3, 9)}
        stats = dict(total=facts.total_slides, opening=slides["part:3"] - 1, parts=parts, checks=facts.total_checks)
        assert stats["opening"] + sum(parts.values()) == facts.total_slides, stats
        the_plan = plan_chapter08b.make(stats)

    # No answers are handed to the resolver, so an {a:N} placeholder in the
    # card fails the build as an unresolved key instead of printing a letter.
    res = notekit.Resolver(slides, {})
    document = notekit.render(the_plan, res, facts)

    problems = notekit.validate(document, res)
    if problems:
        raise SystemExit(
            "Run card design rules violated:\n  " + "\n  ".join(problems)
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "plan.html"
        html_path.write_text(document, encoding="utf-8")
        chrome.render_pdf(html_path, args.out, args.chrome)
        if args.keep_html:
            kept = args.out.with_suffix(".html")
            shutil.copyfile(html_path, kept)
            print(f"html   : {kept}")

    pages = chrome.page_count(args.out)
    print(f"card   : {_relative(args.out)}")
    print(f"pages  : {pages}")
    print(f"deck   : {facts.total_slides} slides, {facts.total_checks} checks, "
          f"{facts.total_figures} figures, {facts.total_charts} charts")
    print(f"keys   : {len(slides)} slide references resolvable")
    print("look at it: every page, as an image, before you commit it.")
    return 0


def _relative(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(REPO))
    except ValueError:
        return str(p)


if __name__ == "__main__":
    raise SystemExit(main())
