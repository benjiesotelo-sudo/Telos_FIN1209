#!/usr/bin/env python3
"""Build the FIN1209 Chapter 4 run card as a print-ready PDF.

    .venv/bin/python build/build_plan4.py

This is the instructor's document. The student-facing lecture notes are a
separate artifact, built by build/build_lecture_notes4.py.

Content is data in build/plan_chapter04.py. Layout is build/notekit.py, which
knows nothing about any chapter. This script wires the two together, resolves
every slide reference against the deck's own content so the card cannot drift
away from the deck, writes HTML with real print CSS, and renders it with
headless Chrome.

It is build_plan3.py with two things changed, both because Chapter 4 is the
lean deck.

**The deck is numbered the way the lean deck is built.** Chapter 4 has its
own opening slides, no dividers and no recaps, and nearly every slide is a
Pair: an idea on the left and a picture on the right. A Pair is one slide
with two names, so `{s:slide:Its title}` and `{s:fig:4.18}` resolve to the
same number, and `{s:part:3}` is the first slide of the part, which carries
the book's section number in its title.

**The minutes on the card are checked, not trusted.** build_chapter4.py
costs the deck at the project's calibrated rate. This script costs it the
same way, costs every cut the card names slide by slide, and refuses a card
whose typed minutes disagree with the deck.

The card prints no check answers. They are in the instructor's answer sheet,
which build_chapter4.py writes outside this repository.

Chrome, and not LibreOffice: see build/chrome.py.

After building, look at the result. Every page:

    pdftoppm -r 80 -png chapter-04/FIN1209-Chapter-04-Run-Card.pdf /tmp/card

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
import plan_chapter04 as plan  # noqa: E402
from build_chapter4 import MINUTES_PER_WEIGHT, cost, slide_weight  # noqa: E402
from content_chapter04 import CHAPTER  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PDF_OUT = REPO / "chapter-04" / "FIN1209-Chapter-04-Run-Card.pdf"


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
        raise SystemExit("build_plan4.py numbers a deck that brings its own "
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


def check_minutes(where: dict[str, tuple[int, object]]) -> list[str]:
    """Every minute the card types, against the deck at the calibrated rate.

    A minute figure on the card is a rounded one, so a row passes when it is
    the costed figure to the nearest minute, and a total passes when it is
    both the costed total to the nearest minute and the sum of its own rows.
    """
    problems: list[str] = []
    costed = cost()                          # (name, slides, minutes) per row

    def near(typed: int, real: float) -> bool:
        return abs(typed - real) <= 0.5 + 1e-9

    if len(plan.CLOCK) != len(costed):
        return [f"the clock has {len(plan.CLOCK)} rows and the deck has "
                f"{len(costed)} parts with its opening and closing"]

    # What each cut takes out of each row of the clock.
    out = [0.0] * len(costed)
    bought: dict[str, float] = {}
    for label, keys, _typed in plan.LADDER:
        bought[label] = 0.0
        for key in keys:
            if key not in where or where[key][1] is None:
                problems.append(f"cut {label} names {key!r}, which is not a "
                                "slide the deck can cost")
                continue
            row, slide = where[key]
            minutes = slide_weight(slide) * MINUTES_PER_WEIGHT
            out[row] += minutes
            bought[label] += minutes

    for (label, slides, full, cut), (name, real_slides, real), gone in zip(
            plan.CLOCK, costed, out):
        if slides != real_slides:
            problems.append(f"{label}: the card says {slides} slides and the "
                            f"deck has {real_slides}")
        if not near(full, real):
            problems.append(f"{label}: the card says {full} minutes and the "
                            f"deck costs {real:.2f}")
        if not near(cut, real - gone):
            problems.append(f"{label}: the card says {cut} minutes cut and "
                            f"the deck costs {real - gone:.2f}")

    total = sum(m for _n, _s, m in costed)
    if not near(plan.FULL, total):
        problems.append(f"the card's total of {plan.FULL} minutes is not the "
                        f"deck's {total:.2f}")
    if not near(plan.CUT, total - sum(out)):
        problems.append(f"the card's cut total of {plan.CUT} minutes is not "
                        f"the deck's {total - sum(out):.2f}")

    runs = total
    typed_runs = plan.FULL
    for label, _keys, typed in plan.LADDER:
        if not near(typed, bought[label]):
            problems.append(f"cut {label}: the card says it buys {typed} "
                            f"minutes and the deck costs {bought[label]:.2f}")
        runs -= bought[label]
        typed_runs -= typed
        if not near(typed_runs, runs):
            problems.append(f"after cut {label} the card says the chapter "
                            f"runs {typed_runs} and the deck costs {runs:.2f}")

    late = sum(slide_weight(where[key][1]) * MINUTES_PER_WEIGHT
               for key in plan.LADDER[0][1]
               if key in where and where[key][0] >= plan.CUT_1_LATE_ROW)
    if not near(plan.CUT_1_LATE, late):
        problems.append(f"the card says cut 1 taken late buys "
                        f"{plan.CUT_1_LATE} minutes and the deck costs "
                        f"{late:.2f}")

    carried = sum(m for i, (_n, _s, m) in enumerate(costed)
                  if i in plan.CARRY_ROWS)
    if not near(plan.CARRY, carried):
        problems.append(f"the card says the carry is {plan.CARRY} minutes "
                        f"and the deck costs {carried:.2f}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PDF_OUT)
    parser.add_argument("--chrome", type=Path, default=chrome.CHROME)
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside the PDF, for inspection",
    )
    args = parser.parse_args()

    slides, where, facts, collisions = index_deck(CHAPTER)
    if collisions:
        print("warning: ambiguous slide keys, first occurrence wins: "
              + ", ".join(sorted(set(collisions))), file=sys.stderr)

    problems = check_minutes(where)
    if problems:
        raise SystemExit(
            "The run card's minutes do not match the deck:\n  "
            + "\n  ".join(problems)
        )

    # No answers are handed to the resolver, so an {a:N} placeholder in the
    # card fails the build as an unresolved key instead of printing a letter.
    res = notekit.Resolver(slides, {})
    document = notekit.render(plan.PLAN, res, facts)

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
    print(f"minutes: {plan.FULL} full, {plan.CUT} with "
          f"{' and '.join('cut ' + label for label, _k, _t in plan.LADDER)}, "
          f"checked against the deck")
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
