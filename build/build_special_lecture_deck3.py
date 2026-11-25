#!/usr/bin/env python3
"""Build deck 3 of 3: a simple stock tool with structured prompts, then view it.

    .venv/bin/python build/build_special_lecture_deck3.py
    .venv/bin/python build/build_special_lecture_deck3.py --edition student

See build_special_lecture_deck1.py's module docstring for how the three
special-lecture decks fit together and special_lecture_kit.py for the
shared Metropolis-style rendering they all use.

Every prompt is two slides, per his 25 Nov fix (a student cannot type a
truncated prompt): the exact words to type, in full, then the real
result. The same full text is also written, verbatim, to
data/fin1209-special-lecture/deck3-prompts.txt, a handout he can share,
so nobody has to copy a prompt by hand off a slide.

Every terminal picture here is a mockup, but never an invented one: each
carries a verbatim excerpt of the real transcript a scout worker recorded
running this exact five-prompt sequence twice, in
data/fin1209-deck3-run/screens/terminal-0N-*.txt (see
content_special_lecture_deck3.py's module docstring). The screenshots are
that worker's own genuine captures of the page the server actually
served, cropped tighter here (the page's own redundant header dropped) so
each fills its slide instead of rendering small.

A sixth, optional prompt (a single stock ticker, as a bonus alongside the
three required indexes) is built from a second scout's verification in
data/fin1209-deck3-bonus/report.md, after his 25 Nov decision to keep
both data paths. Its one real screenshot is used as copied, only cropped
to drop blank space below the real content; see that report for why no
chart screenshot exists. That report also surfaced an unrelated browser
tab belonging to a real, separate production tool; this build does not
use or reference that screenshot, deliberately.
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

PROMPTS_HANDOUT = (Path.home() / ".treehouse" / "benjie-agent-workspace-8bf1b0"
                  / "1" / "benjie-agent-workspace" / "data"
                  / "fin1209-special-lecture" / "deck3-prompts.txt")

# Both "view it" screenshots and the bonus screenshot carry the page's own
# header (repeating what the slide title already says) and, for the
# bonus one, blank space below the real content. Crop boxes found by hand
# against each picture's own real content box.
VIEW_CROPS = {
    "browser-04-sp500-hold.png": (60, 155, 1140, 1335),
    "browser-04-nasdaq-sell.png": (60, 155, 1140, 1335),
}
BONUS_CROP = (10, 25, 490, 580)

# A large picture gets most of the slide body. These three crops are all
# near-square (aspect well under 1.3), which render_shot's own auto-pick
# would otherwise call "tall" (fills height, caption beside, in a ~46%-
# width column); forced to "wide" instead so the enlarged band actually
# takes effect, height still the real constraint, but centered across the
# slide with its caption below, not squeezed to a side column.
BIG_SHOT = dict(layout="wide", band_top=1.2, band_h=5.3, caption_y=6.55)


def _write_prompts_handout():
    lines = []
    for p in content.PROMPTS:
        lines.append(f"{p['title']}")
        lines.append("")
        lines.append(p["prompt_text"])
        lines.append("")
        lines.append("-" * 72)
        lines.append("")
    lines.append(content.BONUS["title"])
    lines.append("")
    lines.append(content.BONUS["prompt_text"])
    lines.append("")
    PROMPTS_HANDOUT.parent.mkdir(parents=True, exist_ok=True)
    PROMPTS_HANDOUT.write_text("\n".join(lines))


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING
    kit.apply_metropolis_style()
    kit.GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck3"
    kit.GENERATED.mkdir(parents=True, exist_ok=True)

    _write_prompts_handout()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    prs_slides.append(("speakers", dict(speakers=content.SPEAKERS)))
    prs_slides.append(("content", content.INTRO))
    prs_slides.append(("content", content.SCOPE_NOTE))

    def add_prompt(p, *, image_src=None):
        prs_slides.append(("prompt_text", {
            "title": p["title"], "goal": p["goal"],
            "prompt_text": p["prompt_text"],
        }))
        if image_src is None:
            img_path = kit.GENERATED / f"prompt-{p['number']:02d}.png"
            kit.make_terminal_png(img_path, p["term_lines"], font_size=42,
                                  line_h=66)
        else:
            img_path = image_src
        prs_slides.append(("shot", {
            "title": p["title"],
            "path": img_path,
            "credit": "If it did not work: " + p["fallback"],
            "notes": p.get("notes", ()),
        }))

    for p in content.PROMPTS:
        add_prompt(p)
        if p["number"] == 4:
            for shot in content.VIEW_SHOTS:
                src = SCREENS / shot["image_file"]
                dst = kit.GENERATED / shot["image_file"]
                crop = VIEW_CROPS.get(shot["image_file"])
                Image.open(src).crop(crop).save(dst) if crop else shutil.copyfile(src, dst)
                prs_slides.append(("shot", {
                    "title": shot["title"], "path": dst,
                    "credit": shot["credit"], "notes": shot.get("notes", ()),
                    **BIG_SHOT,
                }))

    bonus_dst = kit.GENERATED / content.BONUS["image_file"]
    Image.open(BONUS_SCREENS / content.BONUS["image_file"]).crop(BONUS_CROP).save(bonus_dst)
    add_prompt(content.BONUS, image_src=bonus_dst)
    # The bonus result slide just added used the default (smaller) shot
    # box; replace it with the enlarged one, same as the view-it shots.
    prs_slides[-1] = ("shot", {
        **prs_slides[-1][1], **BIG_SHOT,
    })

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
