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

Pictures this deck places, neither a Lim Figure nor an invented Chart:

  * Two terminal-mockup illustrations, one per operating system (the macOS
    PATH/command-not-found error, the Windows "not recognized" error),
    generated at build time with Pillow, since no real recording of either
    error exists. Each image is just the error, large; the fix itself is
    large actual slide text underneath, not image text or a small caption,
    so it reads from the back of a room. Labelled ILLUSTRATION.
  * A Git/GitHub flow diagram (your computer, push, GitHub, pull, a
    teammate's computer), also generated at build time. Labelled
    ILLUSTRATION.
  * Two real Stock Desk pictures, my own live tool: the candlestick chart
    and the signal panel, cropped from the same screenshot and composited
    side by side so the result is wide enough to fill the slide; and the
    position card alone, cropped and enlarged. Copied in from the
    firstmate home's data/stock-desk-build/evidence/. Labelled SCREENSHOT.

These render through render_shot() and render_shot_text() below, written
for this deck rather than added to deckkit.py, since deckkit "knows nothing
about any chapter" and this is not one.

Every Codex CLI command this deck quotes was fetched today from OpenAI's own
docs; see build/content_special_lecture.py's module docstring and each
slide's speaker notes for the exact URL and date. Never taken from memory.
"""

from __future__ import annotations

import argparse
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

# Crop boxes (left, top, right, bottom) in source pixels, picked by eye
# against each screenshot. The chart and panel crops are composited side by
# side at build time so the result is wide enough to fill the slide; the
# position-card crop is used alone, enlarged.
CHART_CROP = (300, 395, 1018, 700)          # candlestick chart + legend
PANEL_CROP = (1030, 230, 1366, 600)         # "Last signal fired" + scoreboard
POSITION_CARD_CROP = (1030, 85, 1366, 330)  # "Your NVDA position" card alone


# --------------------------------------------------------------------------
# The illustrations this deck draws for itself
# --------------------------------------------------------------------------

MONO_FONT_PATH = "/System/Library/Fonts/Menlo.ttc"


def make_error_term_png(path: Path, lines: tuple[str, ...], *, width=1760,
                        font_size=46, line_h=78) -> None:
    """One terminal window, just the error itself, at full slide width and
    large monospace text (readable from the back of a classroom).

    Not a real recording; render_shot_text() labels every slide that uses
    this ILLUSTRATION, never SCREENSHOT, so it is never mistaken for one.
    The fix itself is large actual slide text, not drawn into this image;
    see render_shot_text().
    """
    bar_h = 64
    pad_top = 34
    pad_bottom = 30
    height = bar_h + pad_top + len(lines) * line_h + pad_bottom

    img = Image.new("RGB", (width, height), (28, 28, 30))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, bar_h], fill=(44, 44, 46))
    for cx, dot_color in ((34, (255, 95, 86)), (74, (255, 189, 46)),
                          (114, (39, 201, 63))):
        draw.ellipse([cx - 11, bar_h / 2 - 11, cx + 11, bar_h / 2 + 11],
                     fill=dot_color)

    font = ImageFont.truetype(MONO_FONT_PATH, font_size, index=0)
    y = bar_h + pad_top
    for line in lines:
        color = (235, 235, 235)
        if "not found" in line or "not recognized" in line:
            color = (255, 110, 100)
        elif line.startswith("~ %") or line.startswith("PS>"):
            color = (110, 210, 255)
        draw.text((36, y), line, font=font, fill=color)
        y += line_h

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


def make_chart_panel_composite(src: Path, dst: Path, *, gap=36) -> None:
    """The candlestick chart and the signal panel, side by side.

    Cropped from the same screenshot (CHART_CROP, PANEL_CROP above) and
    scaled to a common height, so the combined picture is wide (its own
    content, not stretched) and fills the slide width instead of the
    portrait-shaped full screenshot's wide side margins.
    """
    im = Image.open(src)
    chart = im.crop(CHART_CROP)
    panel = im.crop(PANEL_CROP)

    target_h = max(chart.height, panel.height)
    chart = chart.resize((round(chart.width * target_h / chart.height), target_h))
    panel = panel.resize((round(panel.width * target_h / panel.height), target_h))

    width = chart.width + gap + panel.width
    composite = Image.new("RGB", (width, target_h), (10, 10, 12))
    composite.paste(chart, (0, 0))
    composite.paste(panel, (chart.width + gap, 0))

    GENERATED.mkdir(parents=True, exist_ok=True)
    composite.save(dst)


def make_position_card_crop(src: Path, dst: Path) -> None:
    """The position card alone, cropped out of the full screenshot."""
    GENERATED.mkdir(parents=True, exist_ok=True)
    Image.open(src).crop(POSITION_CARD_CROP).save(dst)


# --------------------------------------------------------------------------
# A picture slide that is neither a Lim Figure nor an invented Chart
# --------------------------------------------------------------------------

FIGURE_TOP = deckkit.FIGURE_TOP
FIGURE_H = deckkit.FIGURE_H
FIGURE_CAPTION_Y = deckkit.FIGURE_CAPTION_Y


def render_shot(prs, *, title, label, image_path, credit, marker, notes=(),
                band_top=None, band_h=None, caption_y=None):
    """A screenshot or an illustration, one to a slide, with its own credit
    line under it. Same picture band as render_figure/render_chart by
    default so the deck does not jump between them, but neither Lim's
    citation nor an invented-data notice: this picture is ours and it is
    real or is plainly labelled a mockup, never presented as either of the
    other two. band_top/band_h/caption_y override the band for a picture
    that needs more room than a textbook figure ever does."""
    top = FIGURE_TOP if band_top is None else band_top
    height = FIGURE_H if band_h is None else band_h
    cap_y = FIGURE_CAPTION_Y if caption_y is None else caption_y

    slide = deckkit._blank(prs)
    deckkit._content_frame(slide, title, marker)

    band_w = deckkit.CONTENT_W.inches
    px_w, px_h = deckkit._png_size(image_path)
    pad = 0.13
    scale = min((band_w - 2 * pad) / px_w, (height - 2 * pad) / px_h)
    w, h = px_w * scale, px_h * scale
    x = deckkit.MARGIN.inches + (band_w - w) / 2.0
    y = top + (height - h) / 2.0

    deckkit._rect(slide, Inches(x - pad), Inches(y - pad),
                  Inches(w + 2 * pad), Inches(h + 2 * pad), deckkit.WHITE,
                  line=deckkit.BORDER)
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    # One caption line, same as render_figure/render_chart: a second line
    # above it would intrude on a height-bound image's own plate, which
    # fills the band to its exact bottom edge for a landscape picture like
    # this one.
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(cap_y),
                             deckkit.CONTENT_W, Inches(0.7))
    deckkit._para(frame, f"{label} - {credit}", size=12, color=deckkit.MUTED,
                  first=True, line_spacing=1.15)

    deckkit._notes(slide, notes)


# The band for the two error-illustration slides: short (the image is only
# the error itself, 2 lines), so most of the slide is free for the large
# fix text below it. Safe bottom matches deckkit.SAFE_BOTTOM (6.50); the
# small credit line and the progress marker still need room after it.
ERROR_IMAGE_TOP = 1.95
ERROR_IMAGE_H = 1.35
ERROR_TEXT_TOP = 3.45
ERROR_CAPTION_Y = 6.55


def render_shot_text(prs, *, title, label, image_path, lines, accent,
                     credit, marker, rare=None, notes=()):
    """An illustration slide with a large actual-text body under the
    picture, not a small caption: the picture is just the error, the fix is
    real slide text at the same size every other content slide uses, per
    the readability review (small caption text does not read from the back
    of a room). ``rare`` is an optional extra line, still large, for a
    rarer wording of the same error (only the Mac slide has one)."""
    slide = deckkit._blank(prs)
    deckkit._content_frame(slide, title, marker)

    band_w = deckkit.CONTENT_W.inches
    px_w, px_h = deckkit._png_size(image_path)
    pad = 0.13
    scale = min((band_w - 2 * pad) / px_w, (ERROR_IMAGE_H - 2 * pad) / px_h)
    w, h = px_w * scale, px_h * scale
    x = deckkit.MARGIN.inches + (band_w - w) / 2.0
    y = ERROR_IMAGE_TOP + (ERROR_IMAGE_H - h) / 2.0

    deckkit._rect(slide, Inches(x - pad), Inches(y - pad),
                  Inches(w + 2 * pad), Inches(h + 2 * pad), deckkit.WHITE,
                  line=deckkit.BORDER)
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    top = ERROR_TEXT_TOP
    inner_in = deckkit.CONTENT_W.inches
    line_h_total = sum(deckkit._text_height(line, inner_in, 18, spacing=1.15)
                       + 0.14 for line in lines)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                             deckkit.CONTENT_W, Inches(line_h_total + 0.2))
    for i, line in enumerate(lines):
        deckkit._para(frame, line, size=18, color=deckkit.INK,
                      first=(i == 0), space_after=10, line_spacing=1.15)
    top += line_h_total + 0.18

    accent_h = deckkit._text_height(accent, inner_in - 0.32, 18, "bold") + 0.14
    deckkit._rect(slide, deckkit.MARGIN, Inches(top), Inches(0.09),
                  Inches(accent_h), deckkit.GOLD)
    frame = deckkit._textbox(slide, deckkit.MARGIN + Inches(0.32),
                             Inches(top + 0.03),
                             deckkit.CONTENT_W - Inches(0.32), Inches(accent_h))
    deckkit._para(frame, accent, size=18, color=deckkit.INK, bold=True,
                  first=True, line_spacing=1.12)
    top += accent_h + 0.18

    if rare:
        rare_h = deckkit._text_height(rare, inner_in, 16, spacing=1.12)
        frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                                 deckkit.CONTENT_W, Inches(rare_h + 0.1))
        deckkit._para(frame, rare, size=16, color=deckkit.INK, italic=True,
                      first=True, line_spacing=1.12)

    frame = deckkit._textbox(slide, deckkit.MARGIN,
                             Inches(ERROR_CAPTION_Y), deckkit.CONTENT_W,
                             Inches(0.3))
    deckkit._para(frame, f"{label} - {credit}", size=11, color=deckkit.MUTED,
                  first=True)

    deckkit._notes(slide, notes)


# --------------------------------------------------------------------------
# Assembling the deck
# --------------------------------------------------------------------------

def _build_stock_desk_shots() -> dict[str, Path]:
    out = {}
    GENERATED.mkdir(parents=True, exist_ok=True)
    for shot in content.STOCK_DESK_SHOTS:
        name = shot["source_file"]
        src = STOCK_DESK_EVIDENCE / name
        kind = shot["composite"]
        if kind == "chart_panel":
            dst = GENERATED / "stock-desk-chart-panel.png"
            make_chart_panel_composite(src, dst)
        elif kind == "position_card":
            dst = GENERATED / "stock-desk-position-card.png"
            make_position_card_crop(src, dst)
        else:
            raise ValueError(kind)
        out[name] = dst
    return out


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING

    mac_error_png = GENERATED / "codex-path-error-mac.png"
    make_error_term_png(mac_error_png, content.MAC_ERROR_SHOT["term_lines"])
    win_error_png = GENERATED / "codex-path-error-win.png"
    make_error_term_png(win_error_png, content.WIN_ERROR_SHOT["term_lines"])
    git_github_png = GENERATED / "git-github-flow.png"
    make_git_github_flow_png(git_github_png)
    shot_paths = _build_stock_desk_shots()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    for c in content.CONTENT:
        prs_slides.append(("content", c))
    prs_slides.append(("shot_text", content.MAC_ERROR_SHOT | {"path": mac_error_png}))
    prs_slides.append(("shot_text", content.WIN_ERROR_SHOT | {"path": win_error_png}))
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
                band_top=slide.get("band_top"),
                band_h=slide.get("band_h"),
                caption_y=slide.get("caption_y"),
            )
        elif kind == "shot_text":
            render_shot_text(
                prs,
                title=slide["title"],
                label=slide["label"],
                image_path=slide["path"],
                lines=slide["lines"],
                accent=slide["accent"],
                credit=slide["credit"],
                marker=marker,
                rare=slide.get("rare"),
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
