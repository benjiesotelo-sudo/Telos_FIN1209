#!/usr/bin/env python3
"""Build deck 2 of 3: the Stock Desk guide, one feature per slide.

    .venv/bin/python build/build_special_lecture_deck2.py
    .venv/bin/python build/build_special_lecture_deck2.py --edition student

See build_special_lecture_deck1.py's module docstring for how the three
special-lecture decks fit together and special_lecture_kit.py for the
shared Metropolis-style rendering they all use.

Every screenshot here is real, copied in from the firstmate home's
data/stock-desk-guide/guide/png/ (step01 through step10), confirmed fixed
(badges beside, not on; sharp 2x crops) by that guide's own 25 Nov
revision note. Nothing in this script edits or regenerates them; it only
places them, one per slide, with the guide's own plain-words caption.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deckkit  # noqa: E402
import special_lecture_kit as kit  # noqa: E402
import content_special_lecture_deck2 as content  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "special-lecture"
DECK_OUT = OUT_DIR / "FIN1209-Special-Lecture-2-StockDesk.pptx"
STUDENT_OUT = OUT_DIR / "FIN1209-Special-Lecture-2-StockDesk-Student-Edition.pptx"
DEFAULT_OUT = {deckkit.TEACHING: DECK_OUT, deckkit.STUDENT: STUDENT_OUT}

GUIDE_PNG = (Path.home() / ".treehouse" / "benjie-agent-workspace-8bf1b0"
            / "1" / "benjie-agent-workspace" / "data" / "stock-desk-guide"
            / "guide" / "png")


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING
    kit.apply_metropolis_style()
    kit.GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck2"
    kit.GENERATED.mkdir(parents=True, exist_ok=True)

    step_images = []
    for step in content.STEPS:
        src = GUIDE_PNG / step["image_file"]
        dst = kit.GENERATED / step["image_file"]
        shutil.copyfile(src, dst)
        step_images.append(dst)

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    prs_slides.append(("speakers", dict(speakers=content.SPEAKERS)))
    prs_slides.append(("content", content.INTRO))
    for step, image_path in zip(content.STEPS, step_images):
        credit = step["shows"]
        if step["note"]:
            credit = f'{credit} {step["note"]}'
        prs_slides.append(("shot", {
            "title": step["title"],
            "path": image_path,
            "credit": credit,
            "band_h": 4.6,
        }))
    prs_slides.append(("closing", content.CLOSING))

    return kit.build_presentation(
        prs_slides, out_path=out_path,
        title=f"FIN1209 Special Lecture 2 - {content.TITLE.title}",
        course=content.TITLE.course, author="Benjamin C. Sotelo",
        edition=edition,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=deckkit.EDITIONS,
                        default=deckkit.TEACHING)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    out_path = args.out or DEFAULT_OUT[args.edition]
    count = build(args.edition, out_path)
    print(f"{out_path}: {count} slides ({args.edition} edition)")


if __name__ == "__main__":
    main()
