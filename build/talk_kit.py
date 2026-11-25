"""A plain, conference-talk-style rendering kit: one idea per slide, a
soft plain background, one large line, at most a small label above or a
short line below. No boxes, cards, progress lines, footers, page numbers
or presenter tags; that detail lives only in speaker notes.

Modelled on a real Anthropic talk slide (data/fin1209-special-lecture/
photos/style-reference-talk-slide.png): a small serif label ("Follow
along:"), one large clean sans line, nothing else, lots of empty space.
Reuses deckkit's low-level primitives only (_blank, _rect, _textbox,
_para, _text_height, _notes, _repack_deterministically); none of its FEU
chrome or special_lecture_kit's Metropolis chrome.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Emu, Inches, Pt

import deckkit

BG = RGBColor(0xEA, 0xF1, 0xF8)       # one plain soft background colour
INK = RGBColor(0x24, 0x2B, 0x33)
MUTED = RGBColor(0x5B, 0x66, 0x72)
ACCENT = RGBColor(0xC2, 0x55, 0x2E)   # one deliberate accent, warm terracotta

SANS = "Helvetica Neue"
SERIF = "Georgia"
MONO = "Menlo"

SLIDE_W, SLIDE_H = deckkit.SLIDE_W, deckkit.SLIDE_H
MARGIN = Inches(1.0)
CONTENT_W = Emu(SLIDE_W - 2 * MARGIN)


def _blank(prs):
    slide = deckkit._blank(prs)
    deckkit._rect(slide, 0, 0, SLIDE_W, SLIDE_H, BG)
    return slide


LABEL_SIZE = 20
LABEL_H = 0.5
GAP = 0.45


def render_line(prs, *, label=None, line, sub=None, mono=False, size=None,
                notes=()) -> None:
    """One idea: an optional small serif label, one large line (sans or
    monospace for a command, which may be given as a tuple of strings
    for a deliberate, caller-chosen line break), an optional short line
    under it. The whole block is centred vertically on the slide, never
    pinned to the top third. Font size is fixed, never auto-shrunk: a
    command that needs breaking should be passed pre-broken (a tuple),
    at a size large enough to fill the slide width."""
    slide = _blank(prs)
    line_font = MONO if mono else SANS
    size = size or (44 if mono else 40)
    hard_lines = line if isinstance(line, tuple) else (line,)
    line_h_each = deckkit._text_height(hard_lines[0], CONTENT_W.inches, size,
                                       spacing=1.15)
    block_h = sum(deckkit._text_height(hl, CONTENT_W.inches, size,
                                       spacing=1.15) + 0.08
                 for hl in hard_lines) - 0.08

    total_h = block_h
    if label:
        total_h += LABEL_H + GAP
    if sub:
        total_h += GAP + 0.4

    y = (SLIDE_H.inches - total_h) / 2.0

    if label:
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(LABEL_H))
        deckkit._para(frame, label, size=LABEL_SIZE, color=MUTED, italic=True,
                      font=SERIF, align=deckkit.PP_ALIGN.CENTER, first=True)
        y += LABEL_H + GAP

    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                             Inches(block_h + 0.2))
    for i, hl in enumerate(hard_lines):
        deckkit._para(frame, hl, size=size, color=INK, font=line_font,
                      bold=not mono, align=deckkit.PP_ALIGN.CENTER,
                      first=(i == 0), space_after=6, line_spacing=1.15)
    y += block_h

    if sub:
        y += GAP
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(0.4))
        deckkit._para(frame, sub, size=18, color=MUTED, font=SANS,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_prose(prs, *, label=None, text, size=28, notes=()) -> None:
    """A prompt or other long sentence, wrapped automatically, at a
    fixed size never smaller than any other prompt in the deck. The
    caller is responsible for splitting text too long for one slide at
    this size into two calls (not this function shrinking it)."""
    slide = _blank(prs)
    text_h = deckkit._text_height(text, CONTENT_W.inches, size, spacing=1.25)
    total_h = text_h
    if label:
        total_h += LABEL_H + GAP
    y = (SLIDE_H.inches - total_h) / 2.0

    if label:
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(LABEL_H))
        deckkit._para(frame, label, size=LABEL_SIZE, color=MUTED, italic=True,
                      font=SERIF, align=deckkit.PP_ALIGN.CENTER, first=True)
        y += LABEL_H + GAP

    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                             Inches(text_h + 0.3))
    deckkit._para(frame, text, size=size, color=INK, font=SANS, bold=True,
                  align=deckkit.PP_ALIGN.CENTER, first=True, line_spacing=1.25)

    deckkit._notes(slide, notes)


def fits(text: str, size: int, *, max_h: float = 5.6) -> bool:
    """Whether ``text`` rendered at ``size`` fits comfortably on one
    slide, used to decide whether a prompt needs splitting rather than
    shrinking."""
    return deckkit._text_height(text, CONTENT_W.inches, size, spacing=1.25) <= max_h


def split_at_sentence(text: str) -> tuple[str, str]:
    """Split ``text`` into two roughly even halves at a sentence
    boundary (after a period followed by a space), for a prompt too
    long for one slide at the deck's common font size."""
    midpoint = len(text) // 2
    best_i = None
    for i, ch in enumerate(text):
        if ch == "." and i + 1 < len(text) and text[i + 1] == " ":
            if best_i is None or abs(i - midpoint) < abs(best_i - midpoint):
                best_i = i
    if best_i is None:
        return text, ""
    return text[:best_i + 1].strip(), text[best_i + 1:].strip()


def render_title(prs, *, course, title, subtitle=None, notes=()) -> None:
    slide = _blank(prs)
    title_h = deckkit._text_height(title, CONTENT_W.inches, 48, spacing=1.1)
    total_h = 0.5 + GAP + title_h
    if subtitle:
        total_h += GAP + 0.4
    y = (SLIDE_H.inches - total_h) / 2.0

    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W, Inches(0.5))
    deckkit._para(frame, course, size=18, color=MUTED, font=SERIF,
                  italic=True, align=deckkit.PP_ALIGN.CENTER, first=True)
    y += 0.5 + GAP

    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                             Inches(title_h + 0.2))
    deckkit._para(frame, title, size=48, color=INK, font=SANS, bold=True,
                  align=deckkit.PP_ALIGN.CENTER, first=True, line_spacing=1.1)
    y += title_h

    if subtitle:
        y += GAP
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(0.4))
        deckkit._para(frame, subtitle, size=20, color=MUTED, font=SANS,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_speakers(prs, *, speakers, notes=()) -> None:
    """speakers: a tuple of (name, photo_path) pairs. Every photo is the
    same equal portrait rectangle (4:5, the captain's own ready-made
    800x1000 head-and-shoulders crops, placed exactly as given: no
    further cropping, resizing out of shape, or stretching), same size,
    same top edge, side by side, with its name centred under it; nothing
    else, no role labels, no tags."""
    slide = _blank(prs)
    n = len(speakers)
    col_w = CONTENT_W.inches / n
    photo_w = min(2.6, col_w - 0.8)
    photo_h = photo_w * 1.25  # the captain's own crops are 800x1000, 4:5
    top = (SLIDE_H.inches - (photo_h + 0.75)) / 2.0

    for i, (name, photo_path) in enumerate(speakers):
        cx = MARGIN.inches + col_w * (i + 0.5)
        x = cx - photo_w / 2
        if photo_path:
            slide.shapes.add_picture(str(photo_path), Inches(x), Inches(top),
                                     Inches(photo_w), Inches(photo_h))
        else:
            deckkit._rect(slide, Inches(x), Inches(top), Inches(photo_w),
                         Inches(photo_h), RGBColor(0xD8, 0xE0, 0xE8))
        frame = deckkit._textbox(slide, Inches(cx - col_w / 2 + 0.2),
                                 Inches(top + photo_h + 0.25),
                                 Inches(col_w - 0.4), Inches(0.5))
        deckkit._para(frame, name, size=22, color=INK, font=SANS, bold=True,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def make_flow_png(path, labels: tuple[str, ...], *, width=2400) -> None:
    """A plain "how it works" picture: short labels only, large, joined
    by simple arrows, no boxes or cards. Wraps onto a second row (first
    ceil(n/2), then the rest) when more than 3 labels, with an elbowed
    arrow dropping through the gap between rows."""
    from PIL import ImageDraw, ImageFont

    n = len(labels)
    row1_n = -(-n // 2) if n > 3 else n
    row2_n = n - row1_n
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
    ink = (0x24, 0x2B, 0x33)
    accent = (0xC2, 0x55, 0x2E)
    bg = (0xEA, 0xF1, 0xF8)

    row_h = 220
    height = row_h * (2 if row2_n else 1) + (160 if row2_n else 0) + 100
    img = __import__("PIL.Image", fromlist=["Image"]).new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)

    def row_labels(items, y):
        widths = [draw.textlength(t, font=font) for t in items]
        gap = 140
        total_w = sum(widths) + gap * (len(items) - 1)
        x = (width - total_w) / 2
        centers = []
        for t, w in zip(items, widths):
            draw.text((x, y), t, font=font, fill=ink, anchor="lm")
            centers.append((x, x + w))
            x += w + gap
        for (_, x_end), (x_start, _) in zip(centers, centers[1:]):
            mid_y = y
            ax0, ax1 = x_end + 24, x_start - 24
            draw.line([(ax0, mid_y), (ax1, mid_y)], fill=accent, width=6)
            draw.polygon([(ax1, mid_y), (ax1 - 20, mid_y - 14),
                         (ax1 - 20, mid_y + 14)], fill=accent)
        return centers

    # Real clearance below/above a label's own glyph box (its descender),
    # not a small fixed offset, so the connector never touches a letter.
    bbox = draw.textbbox((0, 0), "Ag", font=font)
    half_text_h = (bbox[3] - bbox[1]) / 2.0
    clearance = half_text_h + 36

    y1 = 50 + row_h // 2
    c1 = row_labels(labels[:row1_n], y1)
    if row2_n:
        y2 = y1 + row_h + 160
        c2 = row_labels(labels[row1_n:], y2)
        x_last = (c1[-1][0] + c1[-1][1]) / 2
        x_first = (c2[0][0] + c2[0][1]) / 2
        mid_y = (y1 + y2) / 2
        draw.line([(x_last, y1 + clearance), (x_last, mid_y)],
                 fill=accent, width=6)
        draw.line([(x_last, mid_y), (x_first, mid_y)], fill=accent, width=6)
        draw.line([(x_first, mid_y), (x_first, y2 - clearance)],
                 fill=accent, width=6)
        draw.polygon([(x_first, y2 - clearance),
                     (x_first - 16, y2 - clearance - 24),
                     (x_first + 16, y2 - clearance - 24)], fill=accent)

    img.save(path)


def render_picture(prs, *, label=None, image_path, caption=None,
                   notes=()) -> None:
    """One picture, as large as the slide allows, with an optional small
    label above and a short caption below. No border, no card, no
    frame. Uses almost the full slide, not just the text column, since a
    diagram benefits from every inch a line of text does not need."""
    slide = _blank(prs)
    pic_margin = Inches(0.35)
    pic_w = Emu(SLIDE_W - 2 * pic_margin)
    top = 1.3
    bottom = 7.15
    if label:
        frame = deckkit._textbox(slide, MARGIN, Inches(0.85), CONTENT_W,
                                 Inches(0.45))
        deckkit._para(frame, label, size=18, color=MUTED, italic=True,
                      font=SERIF, align=deckkit.PP_ALIGN.CENTER, first=True)
        top = 1.35
    if caption:
        bottom = 6.7

    px_w, px_h = deckkit._png_size(image_path)
    avail_w, avail_h = pic_w.inches, bottom - top
    scale = min(avail_w / px_w, avail_h / px_h)
    w, h = px_w * scale, px_h * scale
    x = pic_margin.inches + (avail_w - w) / 2.0
    y = top + (avail_h - h) / 2.0
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    if caption:
        frame = deckkit._textbox(slide, MARGIN, Inches(6.8), CONTENT_W,
                                 Inches(0.5))
        deckkit._para(frame, caption, size=16, color=MUTED, font=SANS,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_closing(prs, *, line, notes=()) -> None:
    slide = _blank(prs)
    line_h = deckkit._text_height(line, CONTENT_W.inches, 44, spacing=1.15)
    y = (SLIDE_H.inches - line_h) / 2.0
    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                             Inches(line_h + 0.2))
    deckkit._para(frame, line, size=44, color=INK, font=SANS, bold=True,
                  align=deckkit.PP_ALIGN.CENTER, first=True, line_spacing=1.15)
    deckkit._notes(slide, notes)


def build_presentation(slides: list[tuple[str, dict]], *, out_path: Path,
                       title: str, course: str, author: str) -> int:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    core = prs.core_properties
    core.title = title
    core.author = author
    core.last_modified_by = author
    core.subject = course
    core.revision = 1
    core.created = deckkit.EPOCH
    core.modified = deckkit.EPOCH

    for kind, data in slides:
        if kind == "title":
            render_title(prs, **data)
        elif kind == "line":
            render_line(prs, **data)
        elif kind == "prose":
            render_prose(prs, **data)
        elif kind == "speakers":
            render_speakers(prs, **data)
        elif kind == "picture":
            render_picture(prs, **data)
        elif kind == "closing":
            render_closing(prs, **data)
        else:
            raise TypeError(kind)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_path))
    deckkit._repack_deterministically(out_path)
    return len(prs.slides._sldIdLst)
