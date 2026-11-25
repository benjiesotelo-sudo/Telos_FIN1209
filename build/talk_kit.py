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


def render_line(prs, *, label=None, line, sub=None, mono=False,
                notes=()) -> None:
    """One idea: an optional small serif label, one large line (sans or
    monospace for a command), an optional short line under it. Centred
    in the upper-middle of the slide, generous empty space around it."""
    slide = _blank(prs)
    safe_bottom = 6.9
    y0 = 2.7 if not label else 2.0
    y = y0

    if label:
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(0.5))
        deckkit._para(frame, label, size=18, color=MUTED, italic=True,
                      font=SERIF, align=deckkit.PP_ALIGN.CENTER, first=True)
        y += 0.65

    line_font = MONO if mono else SANS
    # A long command or prompt can run well past a fixed font size; step
    # the size down until it fits the slide rather than clip at the
    # bottom edge. A fixed safety margin on top of the text-height
    # estimate, since a long line with few break points (a URL) can
    # measure a touch short of its real wrapped height.
    max_size = 30 if mono else 40
    for size in range(max_size, 15, -2):
        line_h = deckkit._text_height(line, CONTENT_W.inches, size,
                                      spacing=1.2) + 0.35
        if y + line_h + 0.2 <= safe_bottom or size <= 17:
            break
    frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                             Inches(line_h + 0.2))
    deckkit._para(frame, line, size=size, color=INK, font=line_font,
                  bold=not mono, align=deckkit.PP_ALIGN.CENTER, first=True,
                  line_spacing=1.2)
    y += line_h + 0.4

    if sub:
        frame = deckkit._textbox(slide, MARGIN, Inches(y), CONTENT_W,
                                 Inches(0.6))
        deckkit._para(frame, sub, size=18, color=MUTED, font=SANS,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_title(prs, *, course, title, subtitle=None, notes=()) -> None:
    slide = _blank(prs)
    frame = deckkit._textbox(slide, MARGIN, Inches(1.9), CONTENT_W,
                             Inches(0.5))
    deckkit._para(frame, course, size=18, color=MUTED, font=SERIF,
                  italic=True, align=deckkit.PP_ALIGN.CENTER, first=True)

    title_h = deckkit._text_height(title, CONTENT_W.inches, 48, spacing=1.1)
    frame = deckkit._textbox(slide, MARGIN, Inches(2.6), CONTENT_W,
                             Inches(title_h + 0.2))
    deckkit._para(frame, title, size=48, color=INK, font=SANS, bold=True,
                  align=deckkit.PP_ALIGN.CENTER, first=True, line_spacing=1.1)

    if subtitle:
        frame = deckkit._textbox(slide, MARGIN, Inches(2.6 + title_h + 0.5),
                                 CONTENT_W, Inches(0.6))
        deckkit._para(frame, subtitle, size=20, color=MUTED, font=SANS,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_speakers(prs, *, speakers, notes=()) -> None:
    """speakers: a tuple of (name, photo_path) pairs. Photo, name under
    it; nothing else, no role labels, no tags."""
    slide = _blank(prs)
    n = len(speakers)
    col_w = CONTENT_W.inches / n
    photo_h = 3.0
    top = 1.9
    for i, (name, photo_path) in enumerate(speakers):
        cx = MARGIN.inches + col_w * (i + 0.5)
        px_w, px_h = Image.open(photo_path).size if photo_path else (1, 1)
        photo_w = photo_h * px_w / px_h
        photo_w = min(photo_w, col_w - 0.6)
        photo_h_eff = photo_w * px_h / px_w
        x = cx - photo_w / 2
        if photo_path:
            slide.shapes.add_picture(str(photo_path), Inches(x), Inches(top),
                                     Inches(photo_w), Inches(photo_h_eff))
        frame = deckkit._textbox(slide, Inches(cx - col_w / 2 + 0.2),
                                 Inches(top + photo_h_eff + 0.3),
                                 Inches(col_w - 0.4), Inches(0.5))
        deckkit._para(frame, name, size=24, color=INK, font=SANS, bold=True,
                      align=deckkit.PP_ALIGN.CENTER, first=True)

    deckkit._notes(slide, notes)


def render_picture(prs, *, label=None, image_path, caption=None,
                   notes=()) -> None:
    """One picture, large, centred, with an optional small label above
    and a short caption below. No border, no card, no frame."""
    slide = _blank(prs)
    top = 1.5
    bottom = 6.8
    if label:
        frame = deckkit._textbox(slide, MARGIN, Inches(1.0), CONTENT_W,
                                 Inches(0.45))
        deckkit._para(frame, label, size=18, color=MUTED, italic=True,
                      font=SERIF, align=deckkit.PP_ALIGN.CENTER, first=True)
        top = 1.55
    if caption:
        bottom = 6.5

    px_w, px_h = deckkit._png_size(image_path)
    avail_w, avail_h = CONTENT_W.inches, bottom - top
    scale = min(avail_w / px_w, avail_h / px_h)
    w, h = px_w * scale, px_h * scale
    x = MARGIN.inches + (avail_w - w) / 2.0
    y = top + (avail_h - h) / 2.0
    slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                             Inches(w), Inches(h))

    if caption:
        frame = deckkit._textbox(slide, MARGIN, Inches(6.6), CONTENT_W,
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
