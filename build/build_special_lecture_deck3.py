#!/usr/bin/env python3
"""Build deck 3 of 3: a simple stock tool with structured prompts, then view it.

    .venv/bin/python build/build_special_lecture_deck3.py
    .venv/bin/python build/build_special_lecture_deck3.py --edition student

See build_special_lecture_deck1.py's module docstring for how the three
special-lecture decks fit together and special_lecture_kit.py for the
shared Metropolis-style rendering they all use.

Every terminal picture here is a mockup, but never an invented one: each
carries a verbatim excerpt of the real transcript a scout worker recorded
running this exact five-prompt sequence twice, in
data/fin1209-deck3-run/screens/terminal-0N-*.txt (see
content_special_lecture_deck3.py's module docstring). The screenshots are
that worker's own genuine captures of the page the server actually
served, copied in unchanged.

A sixth, optional prompt (a single stock ticker via Yahoo, as a bonus
alongside the three required indexes) is built from a second scout's
verification in data/fin1209-deck3-bonus/report.md, after his 25 Nov
decision to keep both data paths. Its one real screenshot
(browser-bonus-nvda-429.png) is used as copied; see that report for why
no chart screenshot exists (Yahoo was rate-limiting the test network by
the time of the dedicated screenshot attempt, after one real, verified
BUY reading earlier in the same session). That report also surfaced an
unrelated browser tab belonging to the real, production Stock Desk tool;
this build does not use or reference that screenshot, deliberately.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deckkit  # noqa: E402
import special_lecture_kit as kit  # noqa: E402
import content_special_lecture_deck3 as content  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "special-lecture"
DECK_OUT = OUT_DIR / "FIN1209-Special-Lecture-3-BuildIt.pptx"
STUDENT_OUT = OUT_DIR / "FIN1209-Special-Lecture-3-BuildIt-Student-Edition.pptx"
DEFAULT_OUT = {deckkit.TEACHING: DECK_OUT, deckkit.STUDENT: STUDENT_OUT}

DECK3_RUN = (Path.home() / ".treehouse" / "benjie-agent-workspace-8bf1b0"
            / "1" / "benjie-agent-workspace" / "data" / "fin1209-deck3-run")
SCREENS = DECK3_RUN / "screens"
BONUS_SCREENS = DECK3_RUN.parent / "fin1209-deck3-bonus" / "screens"


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING
    kit.apply_metropolis_style()
    kit.GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck3"
    kit.GENERATED.mkdir(parents=True, exist_ok=True)

    step_images = []
    for i, step in enumerate(content.STEPS):
        dst = kit.GENERATED / f"prompt-{i + 1:02d}.png"
        kit.make_terminal_png(dst, step["term_lines"], font_size=42, line_h=66)
        step_images.append(dst)

    # Both real screenshots are a full page capture with a large flat
    # background margin below the real content (verified: same bg colour
    # from row 1328 of 2029 to the bottom on both). Cropped to the content
    # only so the picture fills its slide instead of mostly empty space.
    shot_images = []
    for shot in content.VIEW_SHOTS:
        src = SCREENS / shot["image_file"]
        dst = kit.GENERATED / shot["image_file"]
        im = Image.open(src)
        im.crop((0, 0, im.width, 1345)).save(dst)
        shot_images.append(dst)

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    prs_slides.append(("speakers", dict(speakers=content.SPEAKERS)))
    prs_slides.append(("content", content.INTRO))
    prs_slides.append(("content", content.SCOPE_NOTE))
    for step, image_path in zip(content.STEPS, step_images):
        prs_slides.append(("step", {**step, "path": image_path}))
        if step["title"].startswith("Prompt 4"):
            for shot, shot_path in zip(content.VIEW_SHOTS, shot_images):
                prs_slides.append(("shot", {
                    "title": shot["title"],
                    "path": shot_path,
                    "credit": shot["credit"],
                    "layout": "tall",
                }))

    bonus_path = kit.GENERATED / content.BONUS_STEP["image_file"]
    shutil.copyfile(BONUS_SCREENS / content.BONUS_STEP["image_file"], bonus_path)
    prs_slides.append(("step", {**content.BONUS_STEP, "path": bonus_path}))

    prs_slides.append(("closing", content.CLOSING))

    return kit.build_presentation(
        prs_slides, out_path=out_path,
        title=f"FIN1209 Special Lecture 3 - {content.TITLE.title}",
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
