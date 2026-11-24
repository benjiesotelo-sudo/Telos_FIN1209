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

Three kinds of picture this deck places, neither a Lim Figure nor an
invented Chart:

  * A dual terminal-mockup illustration (the macOS PATH/command-not-found
    error and the Windows "not recognized" error, each with its exact fix),
    generated at build time by this script with Pillow, since no real
    recording of either error exists. Labelled ILLUSTRATION.
  * A Git/GitHub flow diagram (your computer, push, GitHub, pull, a
    teammate's computer), also generated at build time. Labelled
    ILLUSTRATION.
  * Two real screenshots of Stock Desk, my own live tool, cropped to the
    chart, the signal panel and the position card at large size and copied
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

# Crop box (left, top, right, bottom) in source pixels, dropping the
# watchlist sidebar so the chart, the signal panel and the position card
# read at large size on a projector. Picked by eye against each screenshot.
CROPS = {
    "deployed-final-ipad.png": (300, 95, 1366, 880),
    "deployed-position-card.png": (300, 85, 1366, 870),
}


# --------------------------------------------------------------------------
# The illustrations this deck draws for itself
# --------------------------------------------------------------------------

MONO_FONT_PATH = "/System/Library/Fonts/Menlo.ttc"


def _terminal_panel_height(lines: tuple[str, ...], *, line_h=38) -> int:
    bar_h = 44
    pad_top = 28
    pad_bottom = 22
    return bar_h + pad_top + len(lines) * line_h + pad_bottom


def _draw_terminal_panel(img, draw, x0, y0, width, lines, title, *,
                         line_h=38, font_size=23) -> None:
    """One terminal window, its title bar and monospace lines, at (x0, y0)."""
    bar_h = 44
    pad_top = 28
    height = _terminal_panel_height(lines, line_h=line_h)

    draw.rectangle([x0, y0, x0 + width, y0 + bar_h], fill=(44, 44, 46))
    for cx, dot_color in ((x0 + 24, (255, 95, 86)), (x0 + 54, (255, 189, 46)),
                          (x0 + 84, (39, 201, 63))):
        draw.ellipse([cx - 8, y0 + bar_h / 2 - 8, cx + 8, y0 + bar_h / 2 + 8],
                     fill=dot_color)
    draw.rectangle([x0, y0 + bar_h, x0 + width, y0 + height],
                   fill=(28, 28, 30))

    label_font = ImageFont.truetype(MONO_FONT_PATH, 20, index=0)
    draw.text((x0 + width - 10, y0 - 30), title, font=label_font,
              fill=(90, 90, 90), anchor="ra")

    font = ImageFont.truetype(MONO_FONT_PATH, font_size, index=0)
    y = y0 + bar_h + pad_top
    for line in lines:
        color = (235, 235, 235)
        if "not found" in line or "not recognized" in line:
            color = (255, 110, 100)
        elif line.startswith("~ %") or line.startswith("PS>") or line.startswith("›"):
            color = (110, 210, 255)
        elif line.startswith("Codex CLI") or "Fix:" in line or "New window" in line:
            color = (140, 230, 140)
        draw.text((x0 + 28, y), line, font=font, fill=color)
        y += line_h


def make_dual_terminal_png(path: Path, *, left_title, left_lines, right_title,
                            right_lines, panel_width=980, gap=60) -> None:
    """Two terminal-window illustrations side by side: macOS and Windows.

    Not a real recording; render_shot() labels every slide that uses this
    ILLUSTRATION, never SCREENSHOT, so it is never mistaken for one.
    """
    left_h = _terminal_panel_height(left_lines)
    right_h = _terminal_panel_height(right_lines)
    top_pad = 40
    height = top_pad + max(left_h, right_h) + 20
    width = panel_width * 2 + gap

    img = Image.new("RGB", (width, height), (250, 248, 242))
    draw = ImageDraw.Draw(img)
    _draw_terminal_panel(img, draw, 0, top_pad, panel_width, left_lines,
                         left_title)
    _draw_terminal_panel(img, draw, panel_width + gap, top_pad, panel_width,
                         right_lines, right_title)

    GENERATED.mkdir(parents=True, exist_ok=True)
    img.save(path)


def make_git_github_flow_png(path: Path, *, width=1700, height=560) -> None:
    """Your computer, push, GitHub, pull, a teammate's computer.

    One simple picture for the "What are Git and GitHub?" slide: three
    boxes and two labelled arrows, each box naming what Git or GitHub does
    there.
    """
    bg = (250, 248, 242)
    ink = (26, 26, 26)
    green = (0, 122, 51)
    gold = (242, 169, 0)
    muted = (110, 110, 110)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
    body_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial.ttf", 24)
    label_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)

    box_w, box_h = 430, 230
    y = (height - box_h) // 2
    xs = [40, (width - box_w) // 2, width - box_w - 40]
    boxes = [
        ("Your computer", "Git keeps the history\nof every change you\nmake here.", green),
        ("GitHub", "Stores that history\nonline, so your group\ncan share it.", gold),
        ("Teammate's computer", "Pulls the shared\nhistory down to\nwork on it too.", green),
    ]
    centers = []
    for x, (title, body, accent) in zip(xs, boxes):
        draw.rounded_rectangle([x, y, x + box_w, y + box_h], radius=18,
                               fill=(255, 255, 255), outline=(215, 224, 217),
                               width=2)
        draw.rectangle([x, y, x + box_w, y + 6], fill=accent)
        draw.text((x + 24, y + 26), title, font=title_font, fill=ink)
        draw.multiline_text((x + 24, y + 80), body, font=body_font,
                            fill=muted, spacing=10)
        centers.append((x + box_w // 2, y + box_h // 2))

    arrow_y = y + box_h // 2
    for (cx0, _), (cx1, _), label in zip(centers, centers[1:], ("push", "pull")):
        x_start = cx0 + box_w // 2
        x_end = cx1 - box_w // 2
        draw.line([(x_start, arrow_y), (x_end, arrow_y)], fill=ink, width=4)
        draw.polygon([(x_end, arrow_y), (x_end - 18, arrow_y - 11),
                     (x_end - 18, arrow_y + 11)], fill=ink)
        mid = (x_start + x_end) // 2
        draw.text((mid, arrow_y - 44), label, font=label_font, fill=ink,
                  anchor="ma")

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
    GENERATED.mkdir(parents=True, exist_ok=True)
    for shot in content.STOCK_DESK_SHOTS:
        name = shot["source_file"]
        src = STOCK_DESK_EVIDENCE / name
        dst = GENERATED / name
        box = CROPS.get(name)
        if box:
            Image.open(src).crop(box).save(dst)
        else:
            shutil.copyfile(src, dst)
        out[name] = dst
    return out


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING

    error_png = GENERATED / "codex-path-error.png"
    make_dual_terminal_png(
        error_png,
        left_title=content.ERROR_SHOT["mac_title"],
        left_lines=content.ERROR_SHOT["mac_lines"],
        right_title=content.ERROR_SHOT["win_title"],
        right_lines=content.ERROR_SHOT["win_lines"],
    )
    git_github_png = GENERATED / "git-github-flow.png"
    make_git_github_flow_png(git_github_png)
    shot_paths = _copy_stock_desk_shots()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    for c in content.CONTENT:
        prs_slides.append(("content", c))
    prs_slides.append(("shot", content.ERROR_SHOT | {"path": error_png}))
    for c in content.MORE_CONTENT:
        prs_slides.append(("content", c))
    prs_slides.append(("shot", content.GIT_GITHUB_SHOT | {"path": git_github_png}))
    for c in content.MORE_CONTENT_2:
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
