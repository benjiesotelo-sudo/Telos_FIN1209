#!/usr/bin/env python3
"""Build the FIN1209 Chapter 7 foundation teaching deck."""

from __future__ import annotations

import argparse
import json
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
CANONICAL_FIGURES_DIR = Path.home() / ".fin1209-figures" / "chapter-07"
if CANONICAL_FIGURES_DIR.is_dir():
    FIGURES_DIR = CANONICAL_FIGURES_DIR
FIGURE_SIZE_MANIFEST = REPO / "chapter-07" / "figure-sizes.json"
CHARTS_DIR = REPO / "build" / "generated" / "charts-07"


def _inside_repo(path: Path) -> bool:
    resolved = path.expanduser().resolve()
    return resolved == REPO or REPO in resolved.parents


def _artwork_problems(figures_dir: Path) -> list[str]:
    """Return every reason an artwork build must be refused.

    Figure slides are repeated in the chapter, so report each missing file
    once while still checking the complete set of declared figure slides.
    The size manifest protects marks and crops from being applied to a
    different extraction of the same textbook figure.
    """
    statuses = deckkit.figure_status(CHAPTER, figures_dir)
    missing = sorted({filename for _number, filename, have in statuses
                      if not have})
    problems = []
    if missing:
        problems.append("missing figure files: " + ", ".join(missing))

    if not FIGURE_SIZE_MANIFEST.is_file():
        problems.append("figure size manifest is missing: "
                        f"{FIGURE_SIZE_MANIFEST}")
        return problems

    try:
        manifest = json.loads(FIGURE_SIZE_MANIFEST.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        problems.append(f"cannot read figure size manifest: {exc}")
        return problems
    expected = manifest.get("figures") if isinstance(manifest, dict) else None
    if not isinstance(expected, dict):
        problems.append("figure size manifest must contain a 'figures' object")
        return problems

    try:
        from PIL import Image
    except ImportError as exc:  # pragma: no cover - build environment guard
        problems.append(f"Pillow is required to check figure sizes: {exc}")
        return problems

    declared = sorted({filename for _number, filename, _have in statuses})
    for filename in declared:
        size = expected.get(filename)
        if (not isinstance(size, list) or len(size) != 2
                or not all(isinstance(value, int) for value in size)):
            problems.append(f"figure size manifest has no valid size for {filename}")
            continue
        path = figures_dir / filename
        if not path.is_file():
            continue
        try:
            with Image.open(path) as image:
                actual = list(image.size)
        except OSError as exc:
            problems.append(f"cannot read {filename}: {exc}")
            continue
        if actual != size:
            problems.append(f"figure size mismatch for {filename}: expected "
                            f"{size[0]}x{size[1]}, found {actual[0]}x{actual[1]}")
    return problems


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
    if args.with_figures and _inside_repo(args.out):
        parser.error("artwork builds must be written outside the repository")
    if args.with_figures:
        artwork_problems = _artwork_problems(args.figures_dir)
        if artwork_problems:
            print("Artwork build refused:", file=sys.stderr)
            for problem in artwork_problems:
                print(f"  {problem}", file=sys.stderr)
            return 1

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
