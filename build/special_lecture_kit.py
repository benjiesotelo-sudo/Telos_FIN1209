"""Shared rendering kit for the FIN1209 special lecture decks (1, 2 and 3).

Like deckkit, this knows nothing about any one deck's content; each deck has
its own content_special_lecture_deckN.py (data) and build_special_lecture_
deckN.py (assembly), both importing from here. It reuses deckkit's drawing
primitives (_blank, _rect, _textbox, _para, _content_frame, _text_height,
_png_size, _repack_deterministically) and its Content/TitleSlide/Closing
slide types, but not deckkit.Chapter/Section/build() (parts, dividers,
checks, an answer sheet, a run card): none of that exists here because
nothing in any of these three decks claims to teach Lim's book.

Visual identity: neutral, not FEU's green/gold (the captain's own words,
25 Nov: "it shouldn't be an FEU theme"). apply_neutral_palette() overrides
deckkit's colour globals in place before any slide renders; every deck
build script calls it first. Safe because each `python build_special_
lecture_deckN.py` run is its own process, never sharing state with an
actual Lim-chapter build.

Pictures these decks place, neither a Lim Figure nor an invented Chart:

  * Terminal illustrations/screenshots (make_terminal_png): a real,
    verified command result (SCREENSHOT) or, for a step no local command
    can show, a plain terminal mockup carrying its own gold ILLUSTRATION
    watermark baked into the image (not only the caption).
  * Doc-card illustrations (make_doc_card_png): a plain browser-style
    mockup for a web page this build cannot sign in to or capture live.
  * A macOS system-dialog mockup (make_mac_dialog_png): for the one
    picture that is neither a terminal nor a web page.
  * A Git/GitHub flow diagram, a Stock Desk chart+panel composite from a
    real screenshot, and a made-up example position card.

No "SCREENSHOT -"/"ILLUSTRATION -" provenance footer renders on any slide;
that labelling lives in each slide's speaker notes and in the delivery
report instead, per the student-facing-polish review. A short
``source_credit`` (e.g. "Source: GitHub Docs") is the only footer text
these renderers ever draw, and only where a real third-party image needs
one.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches

import deckkit

REPO = Path(__file__).resolve().parent.parent
MONO_FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Where a deck's build script writes the pictures it generates. Each deck
# script sets this before calling any make_*_png function here (own
# subfolder per deck, so one deck's files never collide with another's).
# Gitignored like every other build/generated/ folder; what is committed is
# the .pptx that embeds these bytes, not the folder itself.
GENERATED: Path | None = None


def _generated_dir() -> Path:
    if GENERATED is None:
        raise RuntimeError("set special_lecture_kit.GENERATED before building")
    GENERATED.mkdir(parents=True, exist_ok=True)
    return GENERATED


# --------------------------------------------------------------------------
# The neutral palette: no FEU green or gold anywhere in these three decks
# --------------------------------------------------------------------------

def apply_neutral_palette(*, accent=None) -> None:
    """Override deckkit's colour globals in place: a clean neutral style
    (white/soft-grey background, dark text, one accent colour) instead of
    FEU's green and gold, since none of these three decks is FEU-branded.
    Call this once, before rendering any slide. ``accent`` lets a deck pick
    its own single accent colour; a calm blue by default."""
    from pptx.dml.color import RGBColor
    deckkit.GREEN = RGBColor(0x26, 0x29, 0x2E)       # dark slate: covers, title text
    deckkit.GREEN_DEEP = RGBColor(0x17, 0x19, 0x1D)  # darker slate: cover accents
    deckkit.GOLD = accent or RGBColor(0x2F, 0x6F, 0xED)  # one chosen accent: blue
    deckkit.PAPER = RGBColor(0xF8, 0xF8, 0xF9)       # soft grey, not warm paper
    deckkit.BORDER = RGBColor(0xDD, 0xDD, 0xE0)      # neutral grey, not FEU's sage
    # INK, MUTED, WHITE were already neutral; left as deckkit has them.


# --------------------------------------------------------------------------
# Illustrations these decks draw for themselves
# --------------------------------------------------------------------------

def make_terminal_png(path: Path, lines: tuple[str, ...], *, width=1760,
                      font_size=42, line_h=66, diff_mode=False,
                      watermark=None) -> None:
    """One terminal window, large monospace text (readable from the back
    of a classroom).

    Used for both a real command transcript (SCREENSHOT) and a mockup of
    one Codex could not actually run here (ILLUSTRATION, watermarked).
    Keep any transcript to about five lines so the picture renders at full
    slide width at a consistent size instead of shrinking to fit a taller
    box. Colour carries meaning the same way a real terminal's does: red
    for an error, cyan for a typed prompt line, green for an added diff
    line or a successful result, exactly like `git diff` and a shell's own
    output.

    ``watermark``, when given, prints a small gold label in the title bar
    (e.g. "ILLUSTRATION"): for a command this build could not actually run
    (it would need a real GitHub account or repository), so the picture
    itself, not only the slide's caption, says plainly that it is not a
    captured result.
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
    if watermark:
        wm_font = ImageFont.truetype(ARIAL_BOLD, 22)
        draw.text((width - 24, bar_h / 2), watermark, font=wm_font,
                  fill=(230, 170, 40), anchor="rm")

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

    _generated_dir()
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
    inner_w = width - 64
    body_font = ImageFont.truetype(ARIAL, font_size)
    tmp = Image.new("RGB", (10, 10))
    tmp_draw = ImageDraw.Draw(tmp)
    wrapped: list[str] = []
    for raw_line in lines:
        cur = ""
        for word in raw_line.split():
            trial = f"{cur} {word}".strip()
            if tmp_draw.textlength(trial, font=body_font) <= inner_w:
                cur = trial
            else:
                if cur:
                    wrapped.append(cur)
                cur = word
        wrapped.append(cur)
    height = bar_h + pad_top + len(wrapped) * line_h + pad_bottom

    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, bar_h], fill=(237, 237, 239))
    for cx, dot_color in ((30, (255, 95, 86)), (64, (255, 189, 46)),
                          (98, (39, 201, 63))):
        r = bar_h * 0.18
        draw.ellipse([cx - r, bar_h / 2 - r, cx + r, bar_h / 2 + r],
                     fill=dot_color)
    addr_font = ImageFont.truetype(ARIAL, 26)
    draw.rounded_rectangle([140, bar_h * 0.2, width - 24, bar_h * 0.8],
                          radius=8, fill=(255, 255, 255),
                          outline=(210, 210, 212))
    draw.text((156, bar_h / 2), site, font=addr_font, fill=(80, 80, 80),
              anchor="lm")

    y = bar_h + pad_top
    for line in wrapped:
        draw.text((32, y), line, font=body_font, fill=(26, 26, 26))
        y += line_h

    _generated_dir()
    img.save(path)


def make_mac_dialog_png(path: Path, *, title: str, message: str,
                        buttons: tuple[str, ...], width=1100) -> None:
    """A macOS system alert mockup: title, message, button row.

    For a dialog no local command can show live (e.g. the fresh-Mac
    Command Line Tools prompt): a native alert, not a web page, so it uses
    neither make_terminal_png's dark terminal nor make_doc_card_png's
    browser chrome.
    """
    title_font = ImageFont.truetype(ARIAL_BOLD, 30)
    body_font = ImageFont.truetype(ARIAL, 26)
    button_font = ImageFont.truetype(ARIAL, 24)

    pad = 40
    inner_w = width - 2 * pad
    tmp = Image.new("RGB", (10, 10))
    tmp_draw = ImageDraw.Draw(tmp)
    lines = []
    for word in message.split():
        trial = (lines[-1] + " " + word) if lines else word
        if tmp_draw.textlength(trial, font=body_font) <= inner_w:
            if lines:
                lines[-1] = trial
            else:
                lines.append(trial)
        else:
            lines.append(word)
    line_h = 36
    btn_h = 56
    height = pad + 44 + 16 + len(lines) * line_h + 30 + btn_h + pad

    img = Image.new("RGB", (width, height), (236, 236, 238))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=14,
                          fill=(246, 246, 248), outline=(205, 205, 208))

    y = pad
    draw.text((width / 2, y), title, font=title_font, fill=(20, 20, 20),
              anchor="ma")
    y += 44 + 16
    for line in lines:
        draw.text((width / 2, y), line, font=body_font, fill=(60, 60, 60),
                  anchor="ma")
        y += line_h
    y += 30

    btn_w = 170
    gap = 16
    total_w = len(buttons) * btn_w + (len(buttons) - 1) * gap
    bx = (width - total_w) / 2
    for i, label in enumerate(buttons):
        fill = (0, 110, 240) if i == len(buttons) - 1 else (222, 222, 225)
        text_color = (255, 255, 255) if i == len(buttons) - 1 else (30, 30, 30)
        draw.rounded_rectangle([bx, y, bx + btn_w, y + btn_h], radius=8,
                              fill=fill)
        draw.text((bx + btn_w / 2, y + btn_h / 2), label, font=button_font,
                  fill=text_color, anchor="mm")
        bx += btn_w + gap

    _generated_dir()
    img.save(path)


def make_example_position_png(path: Path, *, ticker="MSFT",
                              width=1200, height=560) -> None:
    """A made-up Stock Desk position card: the same dark-UI look as the
    real tool, invented numbers, clearly not a screenshot (the EXAMPLE
    banner is drawn onto the card itself, not only the slide's own
    label)."""
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

    title_font = ImageFont.truetype(ARIAL_BOLD, 34)
    label_font = ImageFont.truetype(ARIAL, 26)
    value_font = ImageFont.truetype(ARIAL_BOLD, 30)
    banner_font = ImageFont.truetype(ARIAL_BOLD, 24)

    x = pad + 36
    y = pad + 30
    draw.text((x, y), f"Your {ticker} position", font=title_font, fill=ink)
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

    _generated_dir()
    img.save(path)


def make_git_github_flow_png(path: Path, *, width=1700, height=560) -> None:
    """Your computer, push, GitHub, pull, a teammate's computer.

    One simple picture for a "What are Git and GitHub?" slide: three
    boxes and two labelled arrows, each box naming what Git or GitHub does
    there.
    """
    bg = (248, 248, 249)
    ink = (26, 26, 26)
    accent1 = (47, 111, 237)
    accent2 = (60, 200, 120)
    muted = (110, 110, 110)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(ARIAL_BOLD, 34)
    body_font = ImageFont.truetype(ARIAL, 24)
    label_font = ImageFont.truetype(ARIAL_BOLD, 26)

    box_w, box_h = 430, 230
    y = (height - box_h) // 2
    xs = [40, (width - box_w) // 2, width - box_w - 40]
    boxes = [
        ("Your computer", "Git keeps the history\nof every change you\nmake here.", accent2),
        ("GitHub", "Stores that history\nonline, so your group\ncan share it.", accent1),
        ("Teammate's computer", "Pulls the shared\nhistory down to\nwork on it too.", accent2),
    ]
    centers = []
    for x, (title, body, accent) in zip(xs, boxes):
        draw.rounded_rectangle([x, y, x + box_w, y + box_h], radius=18,
                               fill=(255, 255, 255), outline=(220, 222, 226),
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

    _generated_dir()
    img.save(path)


def make_chart_panel_composite(src: Path, dst: Path, *, chart_crop, panel_crop,
                               gap=36) -> None:
    """Two crops of the same screenshot, scaled to a common height and
    placed side by side, so the combined picture is wide (its own content,
    not stretched) and fills the slide width instead of a portrait-shaped
    full screenshot's wide side margins."""
    im = Image.open(src)
    left = im.crop(chart_crop)
    right = im.crop(panel_crop)

    target_h = max(left.height, right.height)
    left = left.resize((round(left.width * target_h / left.height), target_h))
    right = right.resize((round(right.width * target_h / right.height), target_h))

    width = left.width + gap + right.width
    composite = Image.new("RGB", (width, target_h), (10, 10, 12))
    composite.paste(left, (0, 0))
    composite.paste(right, (left.width + gap, 0))

    _generated_dir()
    composite.save(dst)


# --------------------------------------------------------------------------
# Slide renderers not in deckkit, since deckkit knows nothing about any
# chapter and none of these three decks is one
# --------------------------------------------------------------------------

FIGURE_TOP = deckkit.FIGURE_TOP
FIGURE_H = deckkit.FIGURE_H
FIGURE_CAPTION_Y = deckkit.FIGURE_CAPTION_Y


def draw_presenter(slide, presenter: str | None) -> None:
    """Who presents this slide (deck 1 only, two co-lecturers splitting
    the Mac and Windows runs): a small line level with the progress
    marker, same spot and size as deckkit's own origin line, so it reads
    as part of the deck's identity rather than an afterthought. "both"
    prints as "Both presenters"."""
    if not presenter:
        return
    text = "Both presenters" if presenter == "both" else f"Presents: {presenter}"
    frame = deckkit._textbox(slide, deckkit.MARGIN + Inches(deckkit.ORIGIN_X),
                             deckkit.SLIDE_H - Inches(0.72),
                             deckkit.CONTENT_W - Inches(deckkit.ORIGIN_X),
                             Inches(0.5))
    deckkit._para(frame, text, size=deckkit.ORIGIN_PT, color=deckkit.MUTED,
                  italic=True, align=deckkit.PP_ALIGN.RIGHT, first=True)


def render_shot(prs, *, title, image_path, credit, marker, notes=(),
                band_top=None, band_h=None, caption_y=None, presenter=None,
                **_ignored):
    """A screenshot or an illustration, one to a slide, with its own
    caption line under it (substantive content, not a provenance footer:
    see the module docstring)."""
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

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(cap_y),
                             deckkit.CONTENT_W, Inches(0.7))
    deckkit._para(frame, credit, size=12, color=deckkit.MUTED,
                  first=True, line_spacing=1.15)

    draw_presenter(slide, presenter)
    deckkit._notes(slide, notes)


ERROR_IMAGE_TOP = 1.95
ERROR_IMAGE_H = 1.35
ERROR_TEXT_TOP = 3.45


def render_shot_text(prs, *, title, image_path, lines, accent, marker,
                     rare=None, presenter=None, notes=(), **_ignored):
    """An illustration slide with a large actual-text body under the
    picture, not a small caption: the picture is just the error, the fix is
    real slide text at the same size every other content slide uses.
    ``rare`` is an optional extra line, still large, for a rarer wording of
    the same error."""
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

    draw_presenter(slide, presenter)
    deckkit._notes(slide, notes)


STEP_TEXT_TOP = 1.95
STEP_CREDIT_Y = 6.60
STEP_FALLBACK_BOTTOM = 6.50
STEP_IMAGE_MIN_H = 1.1
STEP_IMAGE_MAX_H = 3.1


def render_prompt_step(prs, *, title, do_lines, do_accent, image_path,
                       fallback, marker, fallback_label="If it did not work: ",
                       source_credit=None, presenter=None, notes=(),
                       **_ignored):
    """What to type/click (top), its real or documented result (the
    picture), then what to do if it did not work (smaller, italic). No
    provenance footer; an optional short source_credit (e.g. "Source:
    GitHub Docs") takes its place only where a real third-party image
    needs one. The picture's height is whatever is left after the text
    above and below it, clamped so a very short or very long prompt never
    makes it absurdly tall or thin."""
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

    fallback_text = fallback_label + fallback
    fallback_h = deckkit._text_height(fallback_text, inner_in, 15, spacing=1.12)
    fallback_bottom = STEP_CREDIT_Y - 0.08 if source_credit else STEP_FALLBACK_BOTTOM
    fallback_top = fallback_bottom - fallback_h
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
    deckkit._para(frame, fallback_text, size=15,
                  color=deckkit.INK, italic=True, first=True,
                  line_spacing=1.12)

    if source_credit:
        frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(STEP_CREDIT_Y),
                                 deckkit.CONTENT_W, Inches(0.3))
        deckkit._para(frame, source_credit, size=11, color=deckkit.MUTED,
                      first=True)

    draw_presenter(slide, presenter)
    deckkit._notes(slide, notes)


def render_speakers(prs, *, speakers, marker, notes=()):
    """"Your speakers": one placeholder avatar, a name and a one-line role
    per speaker, side by side. speakers is a tuple of (name, role) pairs.
    Neutral grey placeholder avatars until real photos arrive."""
    slide = deckkit._blank(prs)
    deckkit._content_frame(slide, "Your speakers", marker)

    n = len(speakers)
    col_w = deckkit.CONTENT_W.inches / n
    avatar_d = 1.7
    top = 2.3
    for i, (name, role) in enumerate(speakers):
        cx = deckkit.MARGIN.inches + col_w * (i + 0.5)
        deckkit._rect(slide, Inches(cx - avatar_d / 2), Inches(top),
                     Inches(avatar_d), Inches(avatar_d), deckkit.BORDER,
                     kind=deckkit.MSO_SHAPE.OVAL)
        frame = deckkit._textbox(slide, Inches(cx - col_w / 2 + 0.2),
                                 Inches(top + avatar_d + 0.25),
                                 Inches(col_w - 0.4), Inches(0.5))
        deckkit._para(frame, name, size=22, color=deckkit.INK, bold=True,
                      align=deckkit.PP_ALIGN.CENTER, first=True)
        frame = deckkit._textbox(slide, Inches(cx - col_w / 2 + 0.2),
                                 Inches(top + avatar_d + 0.75),
                                 Inches(col_w - 0.4), Inches(0.4))
        deckkit._para(frame, role, size=15, color=deckkit.MUTED,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


# --------------------------------------------------------------------------
# Assembling a deck: the common presentation shell every deckN build script
# shares (core properties, the slide-kind dispatch loop, save and repack).
# --------------------------------------------------------------------------

def build_presentation(prs_slides: list[tuple[str, object]], *, out_path: Path,
                       title: str, course: str, author: str,
                       edition: str) -> int:
    """``prs_slides`` is a list of (kind, data) pairs in reading order;
    kind is one of title/content/shot/shot_text/step/speakers/closing. The
    title slide (kind == "title") always counts as position 1, so the
    on-slide marker matches a slide's actual position in the deck."""
    prs = Presentation()
    prs.slide_width = deckkit.SLIDE_W
    prs.slide_height = deckkit.SLIDE_H

    core = prs.core_properties
    core.title = title
    core.author = author
    core.last_modified_by = author
    core.subject = course
    core.revision = 1
    core.created = deckkit.EPOCH
    core.modified = deckkit.EPOCH

    total = len(prs_slides)
    position = 1
    for kind, slide in prs_slides:
        if kind == "title":
            deckkit.render_title(prs, slide)
            position += 1
            continue
        marker = f"Slide {position} of {total}"
        position += 1
        if kind == "content":
            deckkit.render_content(prs, slide, marker)
            if slide.origin:
                deckkit._origin(prs, slide)
        elif kind == "shot":
            render_shot(prs, title=slide["title"], image_path=slide["path"],
                       credit=slide["credit"], marker=marker,
                       notes=slide.get("notes", ()),
                       band_top=slide.get("band_top"),
                       band_h=slide.get("band_h"),
                       caption_y=slide.get("caption_y"),
                       presenter=slide.get("presenter"))
        elif kind == "shot_text":
            render_shot_text(prs, title=slide["title"],
                            image_path=slide["path"], lines=slide["lines"],
                            accent=slide["accent"], marker=marker,
                            rare=slide.get("rare"), notes=slide.get("notes", ()),
                            presenter=slide.get("presenter"))
        elif kind == "step":
            render_prompt_step(
                prs, title=slide["title"], do_lines=slide["do_lines"],
                do_accent=slide["do_accent"], image_path=slide["path"],
                fallback=slide["fallback"],
                fallback_label=slide.get("fallback_label",
                                        "If it did not work: "),
                source_credit=slide.get("source_credit"), marker=marker,
                presenter=slide.get("presenter"), notes=slide.get("notes", ()))
        elif kind == "speakers":
            render_speakers(prs, speakers=slide["speakers"], marker=marker,
                           notes=slide.get("notes", ()))
        elif kind == "closing":
            deckkit.render_closing(prs, slide)
            if slide.origin:
                deckkit._origin(prs, slide)
        else:
            raise TypeError(kind)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_path))
    deckkit._repack_deterministically(out_path)
    return len(prs.slides._sldIdLst)
