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

  * Terminal illustrations/screenshots: the macOS PATH error is a real,
    verified-today shell error (SCREENSHOT); the Windows one has no
    machine to run on (ILLUSTRATION). The walkthrough's own terminal
    pictures are real captures of commands genuinely run today in a
    throwaway local folder (SCREENSHOT), rendered the same way.
  * Doc-card illustrations: a plain mockup of a GitHub or browser screen
    for a step no local command can show (sign-up, invites, the pull
    request pages), built from GitHub's and OpenAI's own current
    documentation, fetched today and cited in that slide's notes. Always
    labelled ILLUSTRATION, never presented as a live capture.
  * A Git/GitHub flow diagram and two Stock Desk pictures (one a real
    screenshot composite, one a made-up example), as before.

These render through render_shot(), render_shot_text() and
render_prompt_step() below, written for this deck rather than added to
deckkit.py, since deckkit "knows nothing about any chapter" and this is not
one.

Every command this deck shows was fetched or genuinely run today; see
build/content_special_lecture.py's module docstring and each slide's
speaker notes for the exact source or the exact command run. Never taken
from memory and never staged as something it is not.
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
# against the screenshot. Composited side by side at build time so the
# result is wide enough to fill the slide.
CHART_CROP = (300, 395, 1018, 700)          # candlestick chart + legend
PANEL_CROP = (1030, 230, 1366, 600)         # "Last signal fired" + scoreboard


# --------------------------------------------------------------------------
# The illustrations this deck draws for itself
# --------------------------------------------------------------------------

MONO_FONT_PATH = "/System/Library/Fonts/Menlo.ttc"


def make_terminal_png(path: Path, lines: tuple[str, ...], *, width=1760,
                      font_size=34, line_h=54, diff_mode=False) -> None:
    """One terminal window, large monospace text (readable from the back
    of a classroom).

    Used for both kinds of terminal picture this deck places: the two
    PATH-error illustrations (just the error, 2 lines, a bigger font) and
    the walkthrough's real command transcripts (more lines, this smaller
    default size so a ten-line transcript still fits one picture). Colour
    carries meaning the same way a real terminal's does: red for an error,
    cyan for a typed prompt line, green for an added diff line or a
    successful result, exactly like `git diff` and a shell's own output.
    """
    bar_h = 54
    pad_top = 28
    pad_bottom = 24
    height = bar_h + pad_top + len(lines) * line_h + pad_bottom

    img = Image.new("RGB", (width, height), (28, 28, 30))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, bar_h], fill=(44, 44, 46))
    for cx, dot_color in ((30, (255, 95, 86)), (64, (255, 189, 46)),
                          (98, (39, 201, 63))):
        r = bar_h * 0.18
        draw.ellipse([cx - r, bar_h / 2 - r, cx + r, bar_h / 2 + r],
                     fill=dot_color)

    font = ImageFont.truetype(MONO_FONT_PATH, font_size, index=0)
    y = bar_h + pad_top
    for line in lines:
        color = (225, 225, 225)
        if ("not found" in line or "not recognized" in line
                or line.startswith("codex :")):
            color = (255, 110, 100)
        elif line.startswith("$") or line.startswith("~ %") or line.startswith("PS>"):
            color = (110, 210, 255)
        elif diff_mode and line.startswith("+") and not line.startswith("+++"):
            color = (120, 220, 130)
        elif diff_mode and line.startswith("-") and not line.startswith("---"):
            color = (235, 120, 110)
        elif line.startswith("codex") or line.startswith("exec") or line == "user":
            color = (180, 180, 255)
        draw.text((32, y), line, font=font, fill=color)
        y += line_h

    GENERATED.mkdir(parents=True, exist_ok=True)
    img.save(path)


def make_doc_card_png(path: Path, *, site: str, lines: tuple[str, ...],
                      width=1760, font_size=34, line_h=54) -> None:
    """A plain browser-style mockup for a step no local command can show:
    a light address bar naming the site, then the documented steps as
    body text. Deliberately unlike make_terminal_png's dark terminal, so
    the room can tell at a glance that this is a mockup of a web page,
    not a captured command result, exactly as its ILLUSTRATION label
    says."""
    bar_h = 54
    pad_top = 30
    pad_bottom = 26
    height = bar_h + pad_top + len(lines) * line_h + pad_bottom

    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, bar_h], fill=(237, 237, 239))
    for cx, dot_color in ((30, (255, 95, 86)), (64, (255, 189, 46)),
                          (98, (39, 201, 63))):
        r = bar_h * 0.18
        draw.ellipse([cx - r, bar_h / 2 - r, cx + r, bar_h / 2 + r],
                     fill=dot_color)
    addr_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    draw.rounded_rectangle([140, bar_h * 0.2, width - 24, bar_h * 0.8],
                          radius=8, fill=(255, 255, 255),
                          outline=(210, 210, 212))
    draw.text((156, bar_h / 2), site, font=addr_font, fill=(80, 80, 80),
              anchor="lm")

    body_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial.ttf", font_size)
    y = bar_h + pad_top
    for line in lines:
        draw.text((32, y), line, font=body_font, fill=(26, 26, 26))
        y += line_h

    GENERATED.mkdir(parents=True, exist_ok=True)
    img.save(path)


def make_example_position_png(path: Path, *, width=1200, height=560) -> None:
    """A made-up Stock Desk position card: the same dark-UI look as the
    real tool, invented numbers, clearly not a screenshot (no real buy
    this small ever looked exactly like this; see the EXAMPLE banner
    drawn onto the card itself, not only the slide's own label)."""
    bg = (10, 10, 12)
    card = (18, 20, 26)
    ink = (235, 235, 235)
    muted = (150, 155, 165)
    green = (60, 200, 120)
    gold = (230, 170, 40)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    pad = 36
    draw.rounded_rectangle([pad, pad, width - pad, height - pad], radius=16,
                          fill=card, outline=(40, 44, 54), width=2)

    title_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
    label_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    value_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)
    banner_font = ImageFont.truetype(
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)

    x = pad + 36
    y = pad + 30
    draw.text((x, y), "Your MSFT position", font=title_font, fill=ink)
    draw.text((width - pad - 36, y), "EXAMPLE, NOT REAL", font=banner_font,
              fill=gold, anchor="ra")
    y += 56
    draw.text((x, y), "HOLD", font=title_font, fill=green)
    y += 56
    draw.text((x, y), "Advice only: stop and target below; a sell signal",
              font=label_font, fill=muted)
    y += 32
    draw.text((x, y), "never forces an exit. You decide.", font=label_font,
              fill=muted)
    y += 56

    rows = [
        ("Bought", "2026-11-18, 5 sh at $480.00"),
        ("Now", "+3.40% since bought"),
        ("Target", "$512.60"),
        ("Stop", "$462.40"),
    ]
    for label, value in rows:
        draw.text((x, y), label, font=label_font, fill=muted)
        draw.text((width - pad - 36, y), value, font=value_font, fill=ink,
                  anchor="ra")
        y += 48

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


# A walkthrough step: what to type/click (top, large text, same size as a
# Content slide's body), then its real or documented result (the picture),
# then what to do if it did not work (smaller, italic), then a one-line
# credit. The picture's height is whatever is left after the text above
# and below it, clamped so a very short or very long prompt never makes it
# absurdly tall or thin.
STEP_TEXT_TOP = 1.95
STEP_CREDIT_Y = 6.58
STEP_FALLBACK_BOTTOM = 6.46
STEP_IMAGE_MIN_H = 1.1
STEP_IMAGE_MAX_H = 2.75


def render_prompt_step(prs, *, title, label, do_lines, do_accent, image_path,
                       fallback, credit, marker, notes=()):
    slide = deckkit._blank(prs)
    deckkit._content_frame(slide, title, marker)

    inner_in = deckkit.CONTENT_W.inches
    top = STEP_TEXT_TOP
    lines_h = sum(deckkit._text_height(line, inner_in, 18, spacing=1.15)
                 + 0.12 for line in do_lines)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                             deckkit.CONTENT_W, Inches(lines_h + 0.2))
    for i, line in enumerate(do_lines):
        deckkit._para(frame, line, size=18, color=deckkit.INK,
                      first=(i == 0), space_after=8, line_spacing=1.15)
    top += lines_h + 0.12

    accent_h = deckkit._text_height(do_accent, inner_in - 0.32, 18, "bold") + 0.14
    deckkit._rect(slide, deckkit.MARGIN, Inches(top), Inches(0.09),
                  Inches(accent_h), deckkit.GOLD)
    frame = deckkit._textbox(slide, deckkit.MARGIN + Inches(0.32),
                             Inches(top + 0.03),
                             deckkit.CONTENT_W - Inches(0.32), Inches(accent_h))
    deckkit._para(frame, do_accent, size=18, color=deckkit.INK, bold=True,
                  first=True, line_spacing=1.12)
    top += accent_h + 0.2

    fallback_h = deckkit._text_height(fallback, inner_in, 15, spacing=1.12)
    fallback_top = STEP_FALLBACK_BOTTOM - fallback_h
    image_top = top
    image_h = max(STEP_IMAGE_MIN_H,
                 min(STEP_IMAGE_MAX_H, fallback_top - 0.18 - image_top))

    band_w = inner_in
    px_w, px_h = deckkit._png_size(image_path)
    pad = 0.13
    scale = min((band_w - 2 * pad) / px_w, (image_h - 2 * pad) / px_h)
    w, h = px_w * scale, px_h * scale
    x = deckkit.MARGIN.inches + (band_w - w) / 2.0
    y = image_top + (image_h - h) / 2.0

    deckkit._rect(slide, Inches(x - pad), Inches(y - pad),
                  Inches(w + 2 * pad), Inches(h + 2 * pad), deckkit.WHITE,
                  line=deckkit.BORDER)
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(fallback_top),
                             deckkit.CONTENT_W, Inches(fallback_h + 0.1))
    deckkit._para(frame, "If it did not work: " + fallback, size=15,
                  color=deckkit.INK, italic=True, first=True,
                  line_spacing=1.12)

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(STEP_CREDIT_Y),
                             deckkit.CONTENT_W, Inches(0.3))
    deckkit._para(frame, f"{label} - {credit}", size=11, color=deckkit.MUTED,
                  first=True)

    deckkit._notes(slide, notes)


# --------------------------------------------------------------------------
# Assembling the deck
# --------------------------------------------------------------------------

def _build_stock_desk_shots() -> dict[int, Path]:
    out = {}
    GENERATED.mkdir(parents=True, exist_ok=True)
    for i, shot in enumerate(content.STOCK_DESK_SHOTS):
        kind = shot["composite"]
        if kind == "chart_panel":
            src = STOCK_DESK_EVIDENCE / shot["source_file"]
            dst = GENERATED / "stock-desk-chart-panel.png"
            make_chart_panel_composite(src, dst)
        elif kind == "example_position":
            dst = GENERATED / "stock-desk-example-position.png"
            make_example_position_png(dst)
        else:
            raise ValueError(kind)
        out[i] = dst
    return out


def _build_walkthrough_images() -> list[Path]:
    paths = []
    GENERATED.mkdir(parents=True, exist_ok=True)
    for i, step in enumerate(content.WALKTHROUGH):
        dst = GENERATED / f"walkthrough-{i:02d}.png"
        if step["kind"] == "terminal":
            make_terminal_png(dst, step["term_lines"],
                              diff_mode=step.get("diff_mode", False))
        elif step["kind"] == "doc":
            make_doc_card_png(dst, site=step["doc_site"], lines=step["doc_lines"])
        else:
            raise ValueError(step["kind"])
        paths.append(dst)
    return paths


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING

    mac_error_png = GENERATED / "codex-path-error-mac.png"
    make_terminal_png(mac_error_png, content.MAC_ERROR_SHOT["term_lines"],
                      font_size=46, line_h=78)
    win_error_png = GENERATED / "codex-path-error-win.png"
    make_terminal_png(win_error_png, content.WIN_ERROR_SHOT["term_lines"],
                      font_size=46, line_h=78)
    git_github_png = GENERATED / "git-github-flow.png"
    make_git_github_flow_png(git_github_png)
    shot_paths = _build_stock_desk_shots()
    walkthrough_images = _build_walkthrough_images()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    prs_slides.append(("content", content.AI_CLI_INTRO))
    prs_slides.append(("content", content.MAC_INSTALL))
    prs_slides.append(("shot_text", content.MAC_ERROR_SHOT | {"path": mac_error_png}))
    prs_slides.append(("content", content.WIN_INSTALL))
    prs_slides.append(("shot_text", content.WIN_ERROR_SHOT | {"path": win_error_png}))
    prs_slides.append(("content", content.SIGNIN))
    prs_slides.append(("content", content.TRANSITION))
    prs_slides.append(("shot", content.GIT_GITHUB_SHOT | {"path": git_github_png}))
    prs_slides.append(("content", content.WALKTHROUGH_INTRO))
    for step, image_path in zip(content.WALKTHROUGH, walkthrough_images):
        prs_slides.append(("step", {**step, "path": image_path}))
    prs_slides.append(("content", content.COLLAB_RULES))
    prs_slides.append(("content", content.STOCK_DESK_INTRO))
    for i, shot in enumerate(content.STOCK_DESK_SHOTS):
        prs_slides.append(("shot", {
            **shot, "path": shot_paths[i],
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
        elif kind == "step":
            label = "SCREENSHOT" if slide["kind"] == "terminal" else "ILLUSTRATION"
            render_prompt_step(
                prs,
                title=slide["title"],
                label=label,
                do_lines=slide["do_lines"],
                do_accent=slide["do_accent"],
                image_path=slide["path"],
                fallback=slide["fallback"],
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
