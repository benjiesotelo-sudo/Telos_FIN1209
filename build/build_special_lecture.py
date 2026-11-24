#!/usr/bin/env python3
"""Build the FIN1209 special lecture deck: AI CLI tools, Git and GitHub.

    .venv/bin/python build/build_special_lecture.py
    .venv/bin/python build/build_special_lecture.py --edition student

This is a one-off special lecture, not a textbook chapter, so it does not
use deckkit.Chapter/Section/build() (parts, dividers, checks, an answer
sheet, a run card): none of that exists here because nothing here claims to
teach Lim's book. It reuses deckkit's visual identity (TitleSlide, Content,
Closing, the FEU palette and fonts) because this lecture is taught from the
same projector as every other FIN1209 deck, and it reuses the two-edition
switch: the teaching edition carries speaker cues, the student edition does
not.

Two kinds of picture this deck places, neither a Lim Figure nor an invented
Chart:

  * One terminal-mockup illustration (the PATH/command-not-found error and
    its fix), generated at build time by this script with Pillow, since no
    real recording of that error exists. Labelled ILLUSTRATION on the slide.
  * Two real screenshots of Stock Desk, the captain's own live tool, copied
    in from the firstmate home's data/stock-desk-build/evidence/. Labelled
    SCREENSHOT.

Both render through render_shot() below, written for this deck rather than
added to deckkit.py, since deckkit "knows nothing about any chapter" and this
is not one.

Every Codex CLI command this deck quotes was fetched today from OpenAI's own
docs; see build/content_special_lecture.py's module docstring and each
slide's speaker notes for the exact URL and date. Never taken from memory.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pptx.util import Inches

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deckkit  # noqa: E402
import content_special_lecture as content  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "special-lecture"
DECK_OUT = OUT_DIR / "FIN1209-Special-Lecture-AI-Tools.pptx"
STUDENT_OUT = OUT_DIR / "FIN1209-Special-Lecture-AI-Tools-Student-Edition.pptx"
DEFAULT_OUT = {deckkit.TEACHING: DECK_OUT, deckkit.STUDENT: STUDENT_OUT}

# Build-time output for the two kinds of picture. Gitignored like every
# other build/generated/ folder; what is committed is the .pptx that embeds
# these bytes, not the folder itself.
GENERATED = REPO / "build" / "generated" / "special-lecture"

# Where the real Stock Desk screenshots live: the firstmate home's evidence
# folder, outside this repository. Not committed as loose files; only their
# bytes, embedded in the deck, are committed.
STOCK_DESK_EVIDENCE = (Path.home() / ".treehouse" / "benjie-agent-workspace-8bf1b0"
                       / "1" / "benjie-agent-workspace" / "data"
                       / "stock-desk-build" / "evidence")


# --------------------------------------------------------------------------
# The one terminal-mockup illustration this deck draws for itself
# --------------------------------------------------------------------------

def make_terminal_png(path: Path, lines: tuple[str, ...], *, width=1500) -> None:
    """A plain terminal-window illustration: title bar, monospace lines.

    Not a real recording; render_shot() labels every slide that uses this
    ILLUSTRATION, never SCREENSHOT, so it is never mistaken for one.
    """
    bar_h = 54
    line_h = 42
    pad_top = 36
    pad_bottom = 30
    height = bar_h + pad_top + len(lines) * line_h + pad_bottom

    bg = (28, 28, 30)
    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, bar_h], fill=(44, 44, 46))
    for cx, dot_color in ((28, (255, 95, 86)), (64, (255, 189, 46)),
                          (100, (39, 201, 63))):
        draw.ellipse([cx - 9, bar_h / 2 - 9, cx + 9, bar_h / 2 + 9],
                     fill=dot_color)

    font = ImageFont.truetype(
        "/System/Library/Fonts/Menlo.ttc", 27, index=0)
    y = bar_h + pad_top
    for line in lines:
        color = (235, 235, 235)
        if line.startswith("zsh:"):
            color = (255, 110, 100)
        elif line.startswith("~ %") or line.startswith("›"):
            color = (110, 210, 255)
        elif line.startswith("Codex CLI"):
            color = (140, 230, 140)
        draw.text((36, y), line, font=font, fill=color)
        y += line_h

    GENERATED.mkdir(parents=True, exist_ok=True)
    img.save(path)


# --------------------------------------------------------------------------
# A picture slide that is neither a Lim Figure nor an invented Chart
# --------------------------------------------------------------------------

FIGURE_TOP = deckkit.FIGURE_TOP
FIGURE_H = deckkit.FIGURE_H
FIGURE_CAPTION_Y = deckkit.FIGURE_CAPTION_Y


def render_shot(prs, *, title, label, image_path, credit, marker, notes=()):
    """A screenshot or an illustration, one to a slide, with its own credit
    line under it. Same picture band as render_figure/render_chart so the
    deck does not jump between them, but neither Lim's citation nor an
    invented-data notice: this picture is ours and it is real or is plainly
    labelled a mockup, never presented as either of the other two."""
    slide = deckkit._blank(prs)
    deckkit._content_frame(slide, title, marker)

    band_w = deckkit.CONTENT_W.inches
    px_w, px_h = deckkit._png_size(image_path)
    pad = 0.13
    scale = min((band_w - 2 * pad) / px_w, (FIGURE_H - 2 * pad) / px_h)
    w, h = px_w * scale, px_h * scale
    x = deckkit.MARGIN.inches + (band_w - w) / 2.0
    y = FIGURE_TOP + (FIGURE_H - h) / 2.0

    deckkit._rect(slide, Inches(x - pad), Inches(y - pad),
                  Inches(w + 2 * pad), Inches(h + 2 * pad), deckkit.WHITE,
                  line=deckkit.BORDER)
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    # One caption line, same as render_figure/render_chart: a second line
    # above it would intrude on a height-bound image's own plate, which
    # fills the band to its exact bottom edge for a landscape picture like
    # this one.
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(FIGURE_CAPTION_Y),
                             deckkit.CONTENT_W, Inches(0.7))
    deckkit._para(frame, f"{label} - {credit}", size=12, color=deckkit.MUTED,
                  first=True, line_spacing=1.15)

    deckkit._notes(slide, notes)


# --------------------------------------------------------------------------
# Assembling the deck
# --------------------------------------------------------------------------

def _copy_stock_desk_shots() -> dict[str, Path]:
    out = {}
    for shot in content.STOCK_DESK_SHOTS:
        src = STOCK_DESK_EVIDENCE / shot["source_file"]
        dst = GENERATED / shot["source_file"]
        GENERATED.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        out[shot["source_file"]] = dst
    return out


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING

    error_png = GENERATED / "codex-path-error.png"
    make_terminal_png(error_png, content.ERROR_SHOT["lines"])
    shot_paths = _copy_stock_desk_shots()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    for c in content.CONTENT:
        prs_slides.append(("content", c))
    prs_slides.append(("shot", content.ERROR_SHOT | {"path": error_png}))
    for c in content.MORE_CONTENT:
        prs_slides.append(("content", c))
    for shot in content.STOCK_DESK_SHOTS:
        prs_slides.append(("shot", {
            **shot, "path": shot_paths[shot["source_file"]],
        }))
    prs_slides.append(("closing", content.CLOSING))

    total = len(prs_slides) - 1  # the title slide carries no marker

    from pptx import Presentation
    prs = Presentation()
    prs.slide_width = deckkit.SLIDE_W
    prs.slide_height = deckkit.SLIDE_H

    core = prs.core_properties
    core.title = f"FIN1209 Special Lecture - {content.TITLE.title}"
    core.author = "Benjamin C. Sotelo"
    core.last_modified_by = "Benjamin C. Sotelo"
    core.subject = content.TITLE.course
    core.revision = 1
    core.created = deckkit.EPOCH
    core.modified = deckkit.EPOCH

    position = 0
    for kind, slide in prs_slides:
        if kind == "title":
            deckkit.render_title(prs, slide)
            continue
        position += 1
        marker = f"Slide {position} of {total}"
        if kind == "content":
            deckkit.render_content(prs, slide, marker)
        elif kind == "shot":
            render_shot(
                prs,
                title=slide["title"],
                label=slide["label"],
                image_path=slide["path"],
                credit=slide["credit"],
                marker=marker,
                notes=slide.get("notes", ()),
            )
        elif kind == "closing":
            deckkit.render_closing(prs, slide)
        else:
            raise TypeError(kind)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_path))
    deckkit._repack_deterministically(out_path)
    return len(prs.slides._sldIdLst)


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
