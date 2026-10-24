#!/usr/bin/env python3
"""Build the FIN1209 Chapter 7 foundation teaching deck."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chartkit
import deckkit
from charts_chapter07 import CHARTS
from content_chapter07 import CHAPTER

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "chapter-07" / "FIN1209-Chapter-07.pptx"
STUDENT_OUT = REPO / "chapter-07" / "FIN1209-Chapter-07-Student-Edition.pptx"
FIGURES_DIR = REPO / "assets" / "figures"
CHARTS_DIR = REPO / "build" / "generated" / "charts-07"


def _inside_repo(path: Path) -> bool:
    resolved = path.expanduser().resolve()
    return resolved == REPO or REPO in resolved.parents


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=deckkit.EDITIONS,
                        default=deckkit.TEACHING)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--with-figures", action="store_true")
    parser.add_argument("--figures-dir", type=Path, default=FIGURES_DIR)
    args = parser.parse_args()
    if args.out is None:
        args.out = STUDENT_OUT if args.edition == deckkit.STUDENT else DEFAULT_OUT
    if args.with_figures and not args.figures_dir.is_dir():
        parser.error(f"figure directory does not exist: {args.figures_dir}")
    if args.with_figures and _inside_repo(args.out):
        parser.error("artwork builds must be written outside the repository")

    chartkit.generate(CHARTS, CHARTS_DIR)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    slides, checks = deckkit.build(
        CHAPTER,
        args.out,
        figures_dir=args.figures_dir if args.with_figures else None,
        charts_dir=CHARTS_DIR,
        edition=args.edition,
    )
    figures = deckkit.figure_status(CHAPTER,
                                    args.figures_dir if args.with_figures else None)
    placed = sum(1 for _n, _f, have in figures if have)
    print(f"deck    : {args.out}")
    print(f"edition : {args.edition}")
    print(f"slides  : {slides}")
    print(f"checks  : {checks}")
    print(f"figures : {placed} of {len(figures)} placed")
    print(f"charts  : {len(CHARTS)} generated in {CHARTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
