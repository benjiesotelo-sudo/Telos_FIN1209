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
# Metropolis: a LaTeX-Beamer-Metropolis-style look, recreated in pptx/PIL,
# no FEU green or gold and no LaTeX installed (the captain's own words, 25
# Nov: "like Latex theme like simple and organized... Metropolis"). A slim
# dark frame-title bar, a thin accent progress line under it, a plain light
# body, small page numbers, one accent colour (Metropolis's own orange).
# --------------------------------------------------------------------------

from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN

METRO_BG = RGBColor(0xFA, 0xFA, 0xFA)
METRO_DARK = RGBColor(0x23, 0x37, 0x3B)      # Metropolis's own dark teal-grey
METRO_INK = RGBColor(0x3C, 0x3C, 0x3C)
METRO_MUTED = RGBColor(0x8A, 0x8A, 0x8A)
METRO_BORDER = RGBColor(0xDD, 0xDD, 0xDD)
METRO_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
METRO_ACCENT_DEFAULT = RGBColor(0xEB, 0x81, 0x1B)  # Metropolis's own orange

METRO_ACCENT = METRO_ACCENT_DEFAULT
METRO_SANS = "Helvetica Neue"
METRO_SANS_BOLD = "Helvetica Neue"

BAR_H = 0.95
PROGRESS_H = Pt(3)
FOOTER_Y = deckkit.SLIDE_H.inches - 0.42


def apply_metropolis_style(*, accent=None) -> None:
    """Set the one chosen accent colour (Metropolis's orange by default)
    and also override deckkit's own colour globals, in case any deckkit
    primitive still reads them directly. Call this once, before rendering
    any slide."""
    global METRO_ACCENT
    METRO_ACCENT = accent or METRO_ACCENT_DEFAULT
    deckkit.GREEN = METRO_DARK
    deckkit.GREEN_DEEP = METRO_DARK
    deckkit.GOLD = METRO_ACCENT
    deckkit.PAPER = METRO_BG
    deckkit.BORDER = METRO_BORDER
    deckkit.INK = METRO_INK
    deckkit.MUTED = METRO_MUTED
    deckkit.DISPLAY_FONT = METRO_SANS
    deckkit.BODY_FONT = METRO_SANS


# Kept for any call site that has not been updated yet; now just an alias.
def apply_neutral_palette(*, accent=None) -> None:
    apply_metropolis_style(accent=accent)


def _metro_blank(prs):
    slide = deckkit._blank(prs)
    deckkit._rect(slide, 0, 0, deckkit.SLIDE_W, deckkit.SLIDE_H, METRO_BG)
    return slide


def metro_frame(slide, title: str, *, position: int | None = None,
                total: int | None = None) -> float:
    """The Metropolis frame title: a slim dark bar with the title in it,
    a thin progress line under it. Returns the y (inches) content may
    start at.

    The line is a true Beamer-Metropolis progress indicator, not a static
    decoration: its accent-coloured portion runs from the left edge to
    ``position / total`` of the slide's width, the rest left in a muted
    track colour, so a glance at the line says how far into the deck this
    slide sits. Pass neither (a divider or any slide outside the normal
    position/total count) to draw a plain full-width accent line instead."""
    deckkit._rect(slide, 0, 0, deckkit.SLIDE_W, Inches(BAR_H), METRO_DARK)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(0.18),
                             deckkit.CONTENT_W, Inches(BAR_H - 0.2),
                             anchor=deckkit.MSO_ANCHOR.MIDDLE)
    deckkit._para(frame, title, size=26, color=METRO_WHITE,
                  font=METRO_SANS, first=True, line_spacing=1.05)
    if position is not None and total:
        deckkit._rect(slide, 0, Inches(BAR_H), deckkit.SLIDE_W, PROGRESS_H,
                      METRO_BORDER)
        filled_w = int(deckkit.SLIDE_W * (position / total))
        deckkit._rect(slide, 0, Inches(BAR_H), filled_w, PROGRESS_H,
                      METRO_ACCENT)
    else:
        deckkit._rect(slide, 0, Inches(BAR_H), deckkit.SLIDE_W, PROGRESS_H,
                      METRO_ACCENT)
    return BAR_H + 0.25


def metro_footer(slide, position: int, total: int) -> None:
    """A small page number in the corner, Metropolis-style: just the
    number, not a "Slide N of M" sentence."""
    frame = deckkit._textbox(slide, deckkit.SLIDE_W - Inches(1.2),
                             Inches(FOOTER_Y), Inches(1.0), Inches(0.3))
    deckkit._para(frame, str(position), size=11, color=METRO_MUTED,
                  font=METRO_SANS, align=PP_ALIGN.RIGHT, first=True)


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
        fill = ((METRO_ACCENT[0], METRO_ACCENT[1], METRO_ACCENT[2])
               if i == len(buttons) - 1 else (222, 222, 225))
        text_color = (255, 255, 255) if i == len(buttons) - 1 else (30, 30, 30)
        draw.rounded_rectangle([bx, y, bx + btn_w, y + btn_h], radius=8,
                              fill=fill)
        draw.text((bx + btn_w / 2, y + btn_h / 2), label, font=button_font,
                  fill=text_color, anchor="mm")
        bx += btn_w + gap

    _generated_dir()
    img.save(path)


def make_step_list_png(path: Path, *, heading: str, steps: tuple[str, ...],
                       note: str | None = None, width=2000, height=620) -> None:
    """A plain numbered-step illustration, for a real-world step this
    build can neither screenshot live (blocked by a bot check) nor cite
    a documentation screenshot for (none exists): a clean card with a
    small "Illustration" tag baked into the picture itself, a plain-text
    heading (a site name, never a logo or any recreated branding), and
    a numbered list, each step set at roughly the same size as this
    deck's own body text, filling the card rather than leaving it mostly
    empty. No visual element here recreates another site's own design;
    only the plain words are its own."""
    bg = (248, 248, 249)
    ink = (26, 26, 26)
    muted = (110, 110, 110)
    accent = (METRO_ACCENT[0], METRO_ACCENT[1], METRO_ACCENT[2])

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    pad = 40
    draw.rounded_rectangle([pad, pad, width - pad, height - pad], radius=18,
                           fill=(255, 255, 255), outline=(222, 224, 228),
                           width=2)

    heading_font = ImageFont.truetype(ARIAL_BOLD, 36)
    tag_font = ImageFont.truetype(ARIAL_BOLD, 24)
    num_font = ImageFont.truetype(ARIAL_BOLD, 38)
    step_font = ImageFont.truetype(ARIAL, 46)
    note_font = ImageFont.truetype(ARIAL, 30)

    inner_x = pad + 50
    y = pad + 36
    draw.text((inner_x, y), heading, font=heading_font, fill=muted)
    tag = "ILLUSTRATION"
    tag_w = draw.textlength(tag, font=tag_font)
    draw.text((width - pad - 40 - tag_w, y + 6), tag, font=tag_font,
              fill=accent)
    y += 58
    draw.line([(inner_x, y), (width - pad - 40, y)], fill=(222, 224, 228),
             width=2)
    y += 40

    for i, step in enumerate(steps, start=1):
        r = 28
        cy = y + r
        draw.ellipse([inner_x, y, inner_x + 2 * r, y + 2 * r],
                    outline=accent, width=3, fill=(255, 255, 255))
        draw.text((inner_x + r, cy), str(i), font=num_font, fill=accent,
                  anchor="mm")
        draw.text((inner_x + 2 * r + 28, cy), step, font=step_font,
                  fill=ink, anchor="lm")
        y += 2 * r + 22

    if note:
        y += 10
        draw.line([(inner_x, y), (width - pad - 36, y)], fill=(222, 224, 228),
                 width=2)
        y += 30
        tmp = Image.new("RGB", (10, 10))
        tmp_draw = ImageDraw.Draw(tmp)
        words, lines, cur = note.split(), [], ""
        max_w = width - pad - 36 - inner_x
        for w in words:
            trial = f"{cur} {w}".strip()
            if tmp_draw.textlength(trial, font=note_font) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        for line in lines:
            draw.text((inner_x, y), line, font=note_font, fill=muted)
            y += 34

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
    there. One accent colour only (the deck's own), on the GitHub box;
    the other two use a neutral dark grey, matching the "one deliberate
    colour" rule.
    """
    bg = (248, 248, 249)
    ink = (26, 26, 26)
    accent = (METRO_ACCENT[0], METRO_ACCENT[1], METRO_ACCENT[2])
    neutral_bar = (60, 70, 74)
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
        ("Your computer", "Git keeps the history\nof every change you\nmake here.", neutral_bar),
        ("GitHub", "Stores that history\nonline, so your group\ncan share it.", accent),
        ("Teammate's computer", "Pulls the shared\nhistory down to\nwork on it too.", neutral_bar),
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


def make_data_flow_png(path: Path, nodes: list[tuple[str, str]], *,
                       accent_index: int | None = None,
                       width=2300) -> None:
    """A plain "how it works" picture: boxes in a row, one arrow between
    each pair, no code names. ``nodes`` is (title, body) pairs, left to
    right; ``accent_index`` picks the one box (if any) drawn in the deck's
    own accent colour, the rest in the neutral dark bar used elsewhere in
    this kit, matching the "one deliberate colour" rule.

    More than 3 nodes wrap onto a second row (the first ceil(n/2), then
    the rest), connected by an elbowed arrow that drops down and back
    left, since text this large does not read in one row across the full
    width. Each card's height still hugs its own text (worst case two
    title lines, up to three body lines) rather than a fixed box with
    empty space under the words, and the canvas as a whole is shaped so
    the picture lands height-bound on its slide, filling the full
    content area top to bottom instead of a thin band across the middle."""
    bg = (248, 248, 249)
    ink = (26, 26, 26)
    muted = (110, 110, 110)
    accent = (METRO_ACCENT[0], METRO_ACCENT[1], METRO_ACCENT[2])
    neutral_bar = (60, 70, 74)

    n = len(nodes)
    row1_n = -(-n // 2) if n > 3 else n  # ceil(n/2) once wrapped
    row2_n = n - row1_n
    margin = 40
    gap = 54
    cols = max(row1_n, row2_n)
    box_w = (width - 2 * margin - (cols - 1) * gap) // cols

    title_font = ImageFont.truetype(ARIAL_BOLD, 69)
    body_font = ImageFont.truetype(ARIAL, 51)
    title_line_h, body_line_h, pad = 87, 66, 48
    box_h = pad * 2 + 2 * title_line_h + 27 + 3 * body_line_h

    row_gap = 150 if row2_n else 0
    height = margin * 2 + box_h * (2 if row2_n else 1) + row_gap

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)

    def wrap(text, font, max_w):
        words = text.split()
        lines, cur = [], ""
        for w in words:
            trial = f"{cur} {w}".strip()
            if draw.textlength(trial, font=font) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def draw_card(i, title, body, x, y):
        bar = accent if i == accent_index else neutral_bar
        draw.rounded_rectangle([x, y, x + box_w, y + box_h], radius=18,
                               fill=(255, 255, 255), outline=(220, 222, 226),
                               width=2)
        draw.rectangle([x, y, x + box_w, y + 14], fill=bar)
        ty = y + pad + 10
        for line in wrap(title, title_font, box_w - 2 * pad):
            draw.text((x + pad, ty), line, font=title_font, fill=ink)
            ty += title_line_h
        ty += 27
        for line in wrap(body, body_font, box_w - 2 * pad):
            draw.text((x + pad, ty), line, font=body_font, fill=muted)
            ty += body_line_h

    centers = []
    for i in range(row1_n):
        x = margin + i * (box_w + gap)
        y = margin
        draw_card(i, nodes[i][0], nodes[i][1], x, y)
        centers.append((x, x + box_w, y + box_h // 2))
    for j in range(row2_n):
        i = row1_n + j
        x = margin + j * (box_w + gap)
        y = margin + box_h + row_gap
        draw_card(i, nodes[i][0], nodes[i][1], x, y)
        centers.append((x, x + box_w, y + box_h // 2))

    for k in range(row1_n - 1):
        _, x_end_prev, ay = centers[k]
        x_start_next, _, _ = centers[k + 1]
        draw.line([(x_end_prev, ay), (x_start_next, ay)], fill=ink, width=5)
        draw.polygon([(x_start_next, ay), (x_start_next - 18, ay - 12),
                     (x_start_next - 18, ay + 12)], fill=ink)
    for k in range(row1_n, n - 1):
        _, x_end_prev, ay = centers[k]
        x_start_next, _, _ = centers[k + 1]
        draw.line([(x_end_prev, ay), (x_start_next, ay)], fill=ink, width=5)
        draw.polygon([(x_start_next, ay), (x_start_next - 18, ay - 12),
                     (x_start_next - 18, ay + 12)], fill=ink)
    if row2_n:
        # The elbow from the end of row 1 down to the start of row 2,
        # routed entirely through the empty gap band between the two
        # rows (never across a card): down from row 1's last card, left
        # to row 2's first card's own column, then down into its top.
        row1_bottom = margin + box_h
        row2_top = margin + box_h + row_gap
        gap_mid = (row1_bottom + row2_top) // 2
        x_last_row1 = margin + (row1_n - 1) * (box_w + gap) + box_w // 2
        x_first_row2 = margin + box_w // 2
        draw.line([(x_last_row1, row1_bottom), (x_last_row1, gap_mid)],
                 fill=ink, width=5)
        draw.line([(x_last_row1, gap_mid), (x_first_row2, gap_mid)],
                 fill=ink, width=5)
        draw.line([(x_first_row2, gap_mid), (x_first_row2, row2_top)],
                 fill=ink, width=5)
        draw.polygon([(x_first_row2, row2_top),
                     (x_first_row2 - 12, row2_top - 18),
                     (x_first_row2 + 12, row2_top - 18)], fill=ink)

    _generated_dir()
    img.save(path)


def _bpmn_task(draw, cx, cy, w, h, title, *, value=None, multi_instance=False,
              subprocess=False, fonts=None, value_above=False):
    """One BPMN task box centered at (cx, cy): a rounded rectangle, an
    optional sequential multi-instance marker (three small horizontal
    bars sitting on the bottom border, his standing rule for a
    once-per-item step), an optional "+" sub-process marker on the same
    border, and an optional dotted-border value annotation connected by a
    line. Returns (x, y, w, h) of the box in case a caller needs its
    exact edges."""
    title_font, body_font = fonts
    x, y = cx - w / 2, cy - h / 2
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                          fill=(255, 255, 255), outline=(40, 44, 54), width=3)
    words = title.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=title_font) <= w - 28:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    # Scaled to the title font itself, not a fixed pixel value: a bigger
    # font (as the BPMN diagrams now use) needs more room between wrapped
    # lines, or they print on top of each other.
    line_h = int(title_font.size * 1.25)
    text_zone_h = h - (34 if (multi_instance or subprocess) else 8)
    ty = y + 10 + max(0, (text_zone_h - len(lines) * line_h) / 2)
    for line in lines:
        draw.text((cx, ty), line, font=title_font, fill=(26, 26, 26),
                  anchor="ma")
        ty += line_h

    if multi_instance:
        bar_w, bar_gap = 20, 5
        bx = cx - (bar_w * 1.5 + bar_gap)
        by = y + h - 10
        for _ in range(3):
            draw.line([(bx, by), (bx + bar_w, by)], fill=(26, 26, 26), width=3)
            by -= 6
    if subprocess:
        sz = 20
        bcx, bcy = cx, y + h - 2
        draw.rectangle([bcx - sz / 2, bcy - sz / 2, bcx + sz / 2, bcy + sz / 2],
                       outline=(26, 26, 26), width=2, fill=(255, 255, 255))
        draw.line([(bcx - sz / 2 + 4, bcy), (bcx + sz / 2 - 4, bcy)],
                  fill=(26, 26, 26), width=2)
        draw.line([(bcx, bcy - sz / 2 + 4), (bcx, bcy + sz / 2 - 4)],
                  fill=(26, 26, 26), width=2)

    if value:
        ann_w, ann_h = w + 20, 90
        ax = cx - ann_w / 2
        ay = (y - ann_h - 26) if value_above else (y + h + 26)
        for seg in range(0, int(ann_w), 14):
            draw.line([(ax + seg, ay), (min(ax + seg + 8, ax + ann_w), ay)],
                      fill=(140, 140, 140), width=2)
            draw.line([(ax + seg, ay + ann_h), (min(ax + seg + 8, ax + ann_w), ay + ann_h)],
                      fill=(140, 140, 140), width=2)
        for seg in range(0, int(ann_h), 14):
            draw.line([(ax, ay + seg), (ax, min(ay + seg + 8, ay + ann_h))],
                      fill=(140, 140, 140), width=2)
            draw.line([(ax + ann_w, ay + seg), (ax + ann_w, min(ay + seg + 8, ay + ann_h))],
                      fill=(140, 140, 140), width=2)
        link_y = (ay + ann_h) if value_above else ay
        box_y = y if value_above else (y + h)
        draw.line([(cx, link_y), (cx, box_y)], fill=(140, 140, 140), width=2)
        vlines = []
        cur = ""
        for word in value.split():
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=body_font) <= ann_w - 20:
                cur = trial
            else:
                if cur:
                    vlines.append(cur)
                cur = word
        if cur:
            vlines.append(cur)
        vy = ay + ann_h / 2 - (len(vlines) * 24) / 2
        for vline in vlines:
            draw.text((cx, vy), vline, font=body_font, fill=(90, 90, 90),
                      anchor="ma")
            vy += 24
    return (x, y, w, h)


def _bpmn_elbow(draw, p0, p1, *, label=None, font=None, via="auto"):
    """A sequence-flow arrow from p0 to p1, elbowed (one bend) unless the
    two points already share an axis. ``via`` picks which leg comes first
    when a bend is needed: "h" (horizontal then vertical) or "v" (the
    reverse); "auto" picks horizontal-first."""
    x0, y0 = p0
    x1, y1 = p1
    if x0 == x1 or y0 == y1:
        segs = [(p0, p1)]
    elif via == "v":
        segs = [(p0, (x0, y1)), ((x0, y1), p1)]
    else:
        segs = [(p0, (x1, y0)), ((x1, y0), p1)]
    for a, b in segs:
        draw.line([a, b], fill=(26, 26, 26), width=3)
    ex, ey = p1
    px, py = segs[-1][0]
    if ex == px:
        dirv = 1 if ey > py else -1
        tip = [(ex, ey), (ex - 7, ey - 11 * dirv), (ex + 7, ey - 11 * dirv)]
    else:
        dirh = 1 if ex > px else -1
        tip = [(ex, ey), (ex - 11 * dirh, ey - 7), (ex - 11 * dirh, ey + 7)]
    draw.polygon(tip, fill=(26, 26, 26))
    if label:
        a, b = segs[0]
        lx, ly = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        if a[0] == b[0]:
            # A vertical segment: the label sits beside the line, not on
            # top of it.
            draw.text((lx + 26, ly), label, font=font, fill=(90, 90, 90),
                      anchor="lm")
        else:
            draw.text((lx, ly - 18), label, font=font, fill=(90, 90, 90),
                      anchor="mm")


def _bpmn_link_event(draw, cx, cy, label, *, outgoing, font):
    """A BPMN link intermediate event: a small circle holding a filled
    arrow, labelled. Used here as an off-page connector between the two
    display rows of one long pool, standard practice for a BPMN diagram
    too wide for one line, rather than one long routed arrow across the
    whole canvas."""
    r = 28
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(26, 26, 26),
                width=3, fill=(255, 255, 255))
    d = 1 if outgoing else -1
    draw.polygon([(cx - 10 * d, cy - 10), (cx - 10 * d, cy + 10),
                 (cx + 12 * d, cy)], fill=(26, 26, 26))
    draw.text((cx, cy + r + 10), label, font=font, fill=(26, 26, 26),
              anchor="ma")


def _bpmn_lanes(img, draw, lane_x0, lane_x1, top, mid, bot, labels, lane_font,
                ink):
    draw.rectangle([lane_x0, top, lane_x1, bot], outline=(190, 190, 195),
                  width=2)
    draw.line([(lane_x0, mid), (lane_x1, mid)], fill=(190, 190, 195), width=2)
    for band_top, band_bot, label in ((top, mid, labels[0]),
                                      (mid, bot, labels[1])):
        band = Image.new("RGBA", (band_bot - band_top, 60), (0, 0, 0, 0))
        bd = ImageDraw.Draw(band)
        bd.text((band.width / 2, 30), label, font=lane_font, fill=ink,
               anchor="mm")
        band = band.rotate(90, expand=True)
        img.paste(band, (lane_x0 - 64, band_top), band)


def make_bpmn_signal_png_part1(path: Path, *, width=2500, height=1000) -> None:
    """Part 1 of 2 (see make_bpmn_signal_png_part2): the Stock Desk lane
    computing a signal and the You lane reading it, up to a BPMN link
    event "A", continued on the next slide. Large type throughout, since
    one slide now holds only six shapes instead of eleven.

    Checked against the real code (engine/signals.ts): the gate is three
    checks (trend, RSI-or-MACD, the 5-bar trigger), not four. Volume is
    reported on the chart and strengthens the reading's wording but never
    gates the signal; drawn as a label inside the checks task, not a
    fourth check box, flagged in the deck's own notes as a difference
    from the first draft."""
    bg = (234, 241, 248)  # matches talk_kit's own slide background exactly,
                          # so no visible panel edge shows against the slide
    ink = (26, 26, 26)
    title_font = ImageFont.truetype(ARIAL_BOLD, 44)
    body_font = ImageFont.truetype(ARIAL, 23)
    lane_font = ImageFont.truetype(ARIAL_BOLD, 34)
    small_font = ImageFont.truetype(ARIAL, 28)
    fonts = (title_font, body_font)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    lane_x0, lane_x1 = 190, width - 40
    task_w, task_h = 380, 230

    top, mid, bot = 50, 500, 870
    _bpmn_lanes(img, draw, lane_x0, lane_x1, top, mid, bot,
               ("STOCK DESK", "YOU"), lane_font, ink)
    sd_y = top + 210
    you_y = mid + 155

    ev_start = (310, sd_y)
    draw.ellipse([ev_start[0] - 38, ev_start[1] - 38, ev_start[0] + 38,
                 ev_start[1] + 38], outline=ink, width=4, fill=(255, 255, 255))
    draw.text((ev_start[0], ev_start[1] + 54), "New price", font=small_font,
              fill=ink, anchor="ma")

    c_ind = (740, sd_y)
    _bpmn_task(draw, *c_ind, task_w, task_h, "Compute indicators",
              multi_instance=True, fonts=fonts)

    c_chk = (1220, sd_y)
    _bpmn_task(draw, *c_chk, task_w, task_h, "Three checks",
              multi_instance=True, fonts=fonts)

    gw_cx, gw_cy = 1700, sd_y
    gw_size = 120
    draw.polygon([(gw_cx, gw_cy - gw_size / 2), (gw_cx + gw_size / 2, gw_cy),
                 (gw_cx, gw_cy + gw_size / 2), (gw_cx - gw_size / 2, gw_cy)],
                outline=ink, width=4, fill=(255, 255, 255))
    draw.line([(gw_cx - 17, gw_cy - 17), (gw_cx + 17, gw_cy + 17)], fill=ink, width=4)
    draw.line([(gw_cx - 17, gw_cy + 17), (gw_cx + 17, gw_cy - 17)], fill=ink, width=4)
    draw.text((gw_cx, gw_cy - gw_size / 2 - 16), "All pass?",
              font=small_font, fill=ink, anchor="mb")

    c_sig = (2180, sd_y)
    _bpmn_task(draw, *c_sig, task_w, task_h, "Show signal", fonts=fonts)

    ev_hold = (gw_cx, mid - 65)
    draw.ellipse([ev_hold[0] - 36, ev_hold[1] - 36, ev_hold[0] + 36,
                 ev_hold[1] + 36], outline=ink, width=6, fill=(255, 255, 255))
    draw.text((ev_hold[0], ev_hold[1] + 52), "HOLD",
              font=small_font, fill=ink, anchor="ma")

    c_decide = (2180, you_y)
    _bpmn_task(draw, *c_decide, task_w, task_h, "You decide", fonts=fonts)

    _bpmn_elbow(draw, (ev_start[0] + 38, ev_start[1]),
               (c_ind[0] - task_w / 2, c_ind[1]))
    _bpmn_elbow(draw, (c_ind[0] + task_w / 2, c_ind[1]),
               (c_chk[0] - task_w / 2, c_chk[1]))
    _bpmn_elbow(draw, (c_chk[0] + task_w / 2, c_chk[1]),
               (gw_cx - gw_size / 2, gw_cy))
    _bpmn_elbow(draw, (gw_cx + gw_size / 2, gw_cy),
               (c_sig[0] - task_w / 2, c_sig[1]), label="yes", font=small_font)
    _bpmn_elbow(draw, (gw_cx, gw_cy + gw_size / 2), ev_hold, label="no",
               font=small_font)
    _bpmn_elbow(draw, (c_sig[0], c_sig[1] + task_h / 2 + 140),
               (c_decide[0], c_decide[1] - task_h / 2))

    link_a_out = (lane_x1 - 70, you_y)
    _bpmn_link_event(draw, *link_a_out, "A", outgoing=True, font=small_font)
    _bpmn_elbow(draw, (c_decide[0] + task_w / 2, c_decide[1]),
               (link_a_out[0] - 34, link_a_out[1]))

    _generated_dir()
    img.save(path)


def make_bpmn_signal_png_part2(path: Path, *, width=2500, height=1000) -> None:
    """Part 2 of 2 (see make_bpmn_signal_png_part1): from the "A" link
    event, logging a buy, the advice-only stop and target, selling or
    holding, and the scoreboard's own sub-process, 5 trading days later.
    His standing rules: a "+" marks a sub-process, horizontal bars on a
    task's bottom border mark a once-per-item (sequential multi-instance)
    step. Labels are 2-3 words only, no dotted value annotations; what
    each step is worth lives in speaker notes instead."""
    bg = (234, 241, 248)  # matches talk_kit's own slide background exactly
    ink = (26, 26, 26)
    title_font = ImageFont.truetype(ARIAL_BOLD, 44)
    body_font = ImageFont.truetype(ARIAL, 23)
    lane_font = ImageFont.truetype(ARIAL_BOLD, 34)
    small_font = ImageFont.truetype(ARIAL, 28)
    fonts = (title_font, body_font)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    lane_x0, lane_x1 = 190, width - 40
    task_w, task_h = 380, 230

    top, mid, bot = 50, 500, 870
    _bpmn_lanes(img, draw, lane_x0, lane_x1, top, mid, bot,
               ("STOCK DESK", "YOU"), lane_font, ink)
    sd_y = top + 210
    you_y = mid + 155

    link_a_in = (310, you_y)
    _bpmn_link_event(draw, *link_a_in, "A", outgoing=False, font=small_font)

    c_buy = (740, you_y)
    _bpmn_task(draw, *c_buy, task_w, task_h, "Log a buy", fonts=fonts)
    _bpmn_elbow(draw, (link_a_in[0] + 38, link_a_in[1]),
               (c_buy[0] - task_w / 2, c_buy[1]))

    c_advice = (740, sd_y)
    _bpmn_task(draw, *c_advice, task_w, task_h, "Stop and target",
              fonts=fonts)
    _bpmn_elbow(draw, (c_buy[0], c_buy[1] - task_h / 2),
               (c_advice[0], c_advice[1] + task_h / 2))

    c_sellhold = (1220, you_y)
    _bpmn_task(draw, *c_sellhold, task_w, task_h, "Sell or hold", fonts=fonts)
    _bpmn_elbow(draw, (c_buy[0] + task_w / 2, c_buy[1]),
               (c_sellhold[0] - task_w / 2, c_sellhold[1]))

    c_logsell = (1700, you_y)
    _bpmn_task(draw, *c_logsell, task_w, task_h, "Log a sell", fonts=fonts)
    _bpmn_elbow(draw, (c_sellhold[0] + task_w / 2, c_sellhold[1]),
               (c_logsell[0] - task_w / 2, c_logsell[1]), label="sell",
               font=small_font)

    c_score = (1700, sd_y)
    _bpmn_task(draw, *c_score, task_w, task_h, "Scoreboard",
              subprocess=True, fonts=fonts)
    _bpmn_elbow(draw, (c_logsell[0] - 70, c_logsell[1] - task_h / 2),
               (c_score[0] - 70, c_score[1] + task_h / 2))

    ev_end = (2180, sd_y)
    draw.ellipse([ev_end[0] - 38, ev_end[1] - 38, ev_end[0] + 38, ev_end[1] + 38],
                outline=ink, width=6, fill=(255, 255, 255))
    _bpmn_elbow(draw, (c_score[0] + task_w / 2, c_score[1]),
               (ev_end[0] - 38, ev_end[1]))

    _generated_dir()
    img.save(path)


def _bpmn_parallel_gateway(draw, cx, cy, size, ink, bg):
    """A BPMN parallel gateway: a diamond with a bold plus sign, for a
    fork (several branches all happen at once) or the matching join."""
    draw.polygon([(cx, cy - size / 2), (cx + size / 2, cy),
                 (cx, cy + size / 2), (cx - size / 2, cy)],
                outline=ink, width=4, fill=bg)
    arm = size * 0.28
    draw.line([(cx - arm, cy), (cx + arm, cy)], fill=ink, width=5)
    draw.line([(cx, cy - arm), (cx, cy + arm)], fill=ink, width=5)


def make_bpmn_vision_png_part1(path: Path, *, width=3300, height=1400) -> None:
    """The vision (1 of 2): live prices, a chosen bar size, a parallel
    split into six rule checks, a parallel join, an agreement score, and
    a drawn projection, handed off to "You" on the next slide (link A).
    A second link, B, re-enters here from the feedback loop on part 2,
    into the same parallel split: this is the vision, not the current
    build, and is drawn and labelled plainly as such.

    The six rule checks stack in a single column, each at its own
    unique height, entered and exited through two vertical spines (one
    on each side of the column). Every connector either travels at a
    box's own unique height or at the shared gateway height, in the
    empty gap, so no connector is ever drawn across another box."""
    bg = (234, 241, 248)
    ink = (26, 26, 26)
    title_font = ImageFont.truetype(ARIAL_BOLD, 34)
    body_font = ImageFont.truetype(ARIAL, 21)
    lane_font = ImageFont.truetype(ARIAL_BOLD, 30)
    small_font = ImageFont.truetype(ARIAL, 26)
    fonts = (title_font, body_font)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    lane_x0, lane_x1 = 190, width - 40
    top, bot = 50, height - 70
    draw.rectangle([lane_x0, top, lane_x1, bot], outline=(190, 190, 195), width=2)
    band = Image.new("RGBA", (bot - top, 60), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    bd.text((band.width / 2, 30), "THE TOOL", font=lane_font, fill=ink, anchor="mm")
    band = band.rotate(90, expand=True)
    img.paste(band, (lane_x0 - 64, top), band)

    row_y = (top + bot) // 2
    task_w, task_h = 280, 150
    gw_size = 110

    ev_start = (280, row_y)
    draw.ellipse([ev_start[0] - 34, ev_start[1] - 34, ev_start[0] + 34,
                 ev_start[1] + 34], outline=ink, width=4, fill=bg)
    draw.text((ev_start[0], ev_start[1] + 48), "Live prices", font=small_font,
              fill=ink, anchor="ma")

    c_bar = (650, row_y)
    _bpmn_task(draw, *c_bar, task_w, task_h, "Choose bar size", fonts=fonts)
    _bpmn_elbow(draw, (ev_start[0] + 34, ev_start[1]),
               (c_bar[0] - task_w / 2, c_bar[1]))

    gw_fork = (1010, row_y)
    _bpmn_parallel_gateway(draw, *gw_fork, gw_size, ink, bg)
    draw.text((gw_fork[0], gw_fork[1] - gw_size / 2 - 14), "Rules vote",
              font=small_font, fill=ink, anchor="mb")
    _bpmn_elbow(draw, (c_bar[0] + task_w / 2, c_bar[1]),
               (gw_fork[0] - gw_size / 2, gw_fork[1]))

    box_w, box_h = 440, 150
    box_x = 1700
    rules = ["Trend", "Momentum", "Breakout", "Volume", "Trendlines",
            "Support, resistance"]
    step = 190
    offsets = [(i - (len(rules) - 1) / 2) * step for i in range(len(rules))]
    box_ys = [row_y + o for o in offsets]

    for label, by in zip(rules, box_ys):
        _bpmn_task(draw, box_x, by, box_w, box_h, label, fonts=fonts)
        # Vertical first, at the gateway's own x, then horizontal at the
        # box's own unique height: this box is the only thing at that
        # height, so the line crosses nothing else.
        _bpmn_elbow(draw, (gw_fork[0] + gw_size / 2, gw_fork[1]),
                   (box_x - box_w / 2, by), via="v")

    gw_join = (box_x + 650, row_y)
    _bpmn_parallel_gateway(draw, *gw_join, gw_size, ink, bg)
    for by in box_ys:
        # Horizontal first, at the box's own unique height, then
        # vertical at the join's x: same guarantee, mirrored.
        _bpmn_elbow(draw, (box_x + box_w / 2, by),
                   (gw_join[0] - gw_size / 2, gw_join[1]))

    c_agree = (gw_join[0] + 320, row_y)
    _bpmn_task(draw, *c_agree, task_w, task_h, "Agreement score", fonts=fonts)
    _bpmn_elbow(draw, (gw_join[0] + gw_size / 2, gw_join[1]),
               (c_agree[0] - task_w / 2, c_agree[1]))

    c_draw = (c_agree[0] + 420, row_y)
    _bpmn_task(draw, *c_draw, task_w, task_h, "Draw what's next", fonts=fonts)
    _bpmn_elbow(draw, (c_agree[0] + task_w / 2, c_agree[1]),
               (c_draw[0] - task_w / 2, c_draw[1]))

    link_a_out = (c_draw[0] + 260, row_y)
    _bpmn_link_event(draw, *link_a_out, "A", outgoing=True, font=small_font)
    _bpmn_elbow(draw, (c_draw[0] + task_w / 2, c_draw[1]),
               (link_a_out[0] - 34, link_a_out[1]))

    link_b_in = (lane_x0 + 70, bot - 70)
    _bpmn_link_event(draw, *link_b_in, "B", outgoing=False, font=small_font)
    draw.text((link_b_in[0], link_b_in[1] + 86), "feedback loop",
             font=small_font, fill=(90, 90, 90), anchor="ma")
    _bpmn_elbow(draw, (link_b_in[0] + 34, link_b_in[1]),
               (gw_fork[0], gw_fork[1] + gw_size / 2), via="v")

    _generated_dir()
    img.save(path)


def make_bpmn_vision_png_part2(path: Path, *, width=2600, height=1000) -> None:
    """The vision (2 of 2): the You lane picks up from link A (Draw
    what's next, on part 1), reads the call, decides Buy, Sell, or Wait,
    and logs it; the tool checks the outcome later and learns which
    rules work, feeding back (link B) into part 1's parallel split."""
    bg = (234, 241, 248)
    ink = (26, 26, 26)
    title_font = ImageFont.truetype(ARIAL_BOLD, 40)
    body_font = ImageFont.truetype(ARIAL, 23)
    lane_font = ImageFont.truetype(ARIAL_BOLD, 32)
    small_font = ImageFont.truetype(ARIAL, 28)
    fonts = (title_font, body_font)

    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    lane_x0, lane_x1 = 190, width - 40
    task_w, task_h = 360, 220

    top, mid, bot = 50, 500, 870
    _bpmn_lanes(img, draw, lane_x0, lane_x1, top, mid, bot,
               ("THE TOOL", "YOU"), lane_font, ink)
    sd_y = top + 210
    you_y = mid + 155

    link_a_in = (300, you_y)
    _bpmn_link_event(draw, *link_a_in, "A", outgoing=False, font=small_font)

    c_read = (720, you_y)
    _bpmn_task(draw, *c_read, task_w, task_h, "Read the call", fonts=fonts)
    _bpmn_elbow(draw, (link_a_in[0] + 38, link_a_in[1]),
               (c_read[0] - task_w / 2, c_read[1]))

    gw_cx, gw_cy = 1260, you_y
    gw_size = 120
    draw.polygon([(gw_cx, gw_cy - gw_size / 2), (gw_cx + gw_size / 2, gw_cy),
                 (gw_cx, gw_cy + gw_size / 2), (gw_cx - gw_size / 2, gw_cy)],
                outline=ink, width=4, fill=bg)
    draw.line([(gw_cx - 17, gw_cy - 17), (gw_cx + 17, gw_cy + 17)], fill=ink, width=4)
    draw.line([(gw_cx - 17, gw_cy + 17), (gw_cx + 17, gw_cy - 17)], fill=ink, width=4)
    draw.text((gw_cx, gw_cy - gw_size / 2 - 16), "Buy, Sell, Wait",
              font=small_font, fill=ink, anchor="mb")
    _bpmn_elbow(draw, (c_read[0] + task_w / 2, c_read[1]),
               (gw_cx - gw_size / 2, gw_cy))

    c_log = (1740, you_y)
    _bpmn_task(draw, *c_log, task_w, task_h, "Log it", fonts=fonts)
    _bpmn_elbow(draw, (gw_cx + gw_size / 2, gw_cy),
               (c_log[0] - task_w / 2, c_log[1]))

    c_outcome = (2180, sd_y)
    _bpmn_task(draw, *c_outcome, task_w, task_h, "Outcome checked", fonts=fonts)
    _bpmn_elbow(draw, (c_log[0] + 60, c_log[1] - task_h / 2),
               (c_outcome[0] + 60, c_outcome[1] + task_h / 2))

    link_b_out = (lane_x1 - 70, sd_y)
    _bpmn_link_event(draw, *link_b_out, "B", outgoing=True, font=small_font)
    draw.text((link_b_out[0], link_b_out[1] + 90), "Learn which\nrules work",
             font=small_font, fill=ink, anchor="ma", align="center")
    _bpmn_elbow(draw, (c_outcome[0] + task_w / 2, c_outcome[1]),
               (link_b_out[0] - 34, link_b_out[1]))

    _generated_dir()
    img.save(path)


# --------------------------------------------------------------------------
# Slide renderers not in deckkit, since deckkit knows nothing about any
# chapter and none of these three decks is one
# --------------------------------------------------------------------------

FIGURE_TOP = 1.45
FIGURE_H = 4.6
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


SHOT_BOTTOM = 6.65  # leaves room for the presenter line/footer below


def render_shot(prs, *, title, image_path, credit, position, total, notes=(),
                band_top=None, band_h=None, caption_y=None, presenter=None,
                layout=None, **_ignored):
    """A screenshot or an illustration, one to a slide. A wide picture
    fills the content width with its caption under it; a tall or square
    one fills the available height instead, with the caption beside it,
    so a portrait crop never shrinks to a third of the slide the way a
    width-first fit would leave it. ``layout`` forces "wide" or "tall";
    left alone, the image's own aspect ratio decides (>=1.3 counts as
    wide)."""
    top = FIGURE_TOP if band_top is None else band_top
    px_w, px_h = deckkit._png_size(image_path)
    wide = (px_w / px_h >= 1.3) if layout is None else (layout == "wide")

    slide = _metro_blank(prs)
    metro_frame(slide, title, position=position, total=total)
    pad = 0.13

    if wide:
        height = FIGURE_H if band_h is None else band_h
        cap_y = FIGURE_CAPTION_Y if caption_y is None else caption_y
        band_w = deckkit.CONTENT_W.inches
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
    else:
        avail_h = SHOT_BOTTOM - top
        img_col_w = deckkit.CONTENT_W.inches * 0.46
        scale = min((img_col_w - 2 * pad) / px_w, (avail_h - 2 * pad) / px_h)
        w, h = px_w * scale, px_h * scale
        x = deckkit.MARGIN.inches + (img_col_w - w) / 2.0
        y = top + (avail_h - h) / 2.0

        deckkit._rect(slide, Inches(x - pad), Inches(y - pad),
                      Inches(w + 2 * pad), Inches(h + 2 * pad), deckkit.WHITE,
                      line=deckkit.BORDER)
        slide.shapes.add_picture(str(image_path), Inches(x), Inches(y),
                                 Inches(w), Inches(h))

        cap_x = deckkit.MARGIN.inches + img_col_w + 0.4
        cap_w = deckkit.CONTENT_W.inches - img_col_w - 0.4
        frame = deckkit._textbox(slide, Inches(cap_x), Inches(top),
                                 Inches(cap_w), Inches(avail_h),
                                 anchor=deckkit.MSO_ANCHOR.MIDDLE)
        deckkit._para(frame, credit, size=17, color=deckkit.INK,
                      first=True, line_spacing=1.3)

    draw_presenter(slide, presenter)
    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


ERROR_IMAGE_TOP = 1.45
ERROR_IMAGE_H = 1.35
ERROR_TEXT_TOP = 2.95


def render_shot_text(prs, *, title, image_path, lines, accent, position, total,
                     rare=None, presenter=None, notes=(), **_ignored):
    """An illustration slide with a large actual-text body under the
    picture, not a small caption: the picture is just the error, the fix is
    real slide text at the same size every other content slide uses.
    ``rare`` is an optional extra line, still large, for a rarer wording of
    the same error."""
    slide = _metro_blank(prs)
    metro_frame(slide, title, position=position, total=total)

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
    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


STEP_TEXT_TOP = 1.45
STEP_CREDIT_Y = 6.60
STEP_FALLBACK_BOTTOM = 6.50
STEP_IMAGE_MIN_H = 1.1
STEP_IMAGE_MAX_H = 3.1


def render_prompt_step(prs, *, title, do_lines, do_accent, image_path,
                       fallback, position, total,
                       fallback_label="If it did not work: ",
                       source_credit=None, presenter=None, notes=(),
                       **_ignored):
    """What to type/click (top), its real or documented result (the
    picture), then what to do if it did not work (smaller, italic). No
    provenance footer; an optional short source_credit (e.g. "Source:
    GitHub Docs") takes its place only where a real third-party image
    needs one. The picture's height is whatever is left after the text
    above and below it, clamped so a very short or very long prompt never
    makes it absurdly tall or thin."""
    slide = _metro_blank(prs)
    metro_frame(slide, title, position=position, total=total)

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
    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


def render_speakers(prs, *, speakers, position, total, notes=()):
    """"Your speakers": one placeholder avatar, a name and a one-line role
    per speaker, side by side. speakers is a tuple of (name, role) pairs.
    Neutral grey placeholder avatars until real photos arrive."""
    slide = _metro_blank(prs)
    metro_frame(slide, "Your speakers", position=position, total=total)

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

    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


def render_content_m(prs, s, *, position, total):
    """A Metropolis-style content slide: the dark frame title, the accent
    progress rule, then plain body text (lines, one gold-barred accent, a
    muted caption) exactly like a Content slide's body always has, just
    without deckkit's own FEU chrome around it."""
    slide = _metro_blank(prs)
    top = metro_frame(slide, s.title, position=position, total=total)

    inner_in = deckkit.CONTENT_W.inches
    if s.lines:
        frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                                 deckkit.CONTENT_W, Inches(3.4))
        for i, line in enumerate(s.lines):
            deckkit._para(frame, line, size=21, color=METRO_INK,
                          first=(i == 0), space_after=13, line_spacing=1.18)
        top += sum(deckkit._text_height(line, inner_in, 21, spacing=1.18) + 0.20
                  for line in s.lines) + 0.34

    if s.accent:
        accent_h = deckkit._text_height(s.accent, inner_in - 0.32, 22, "bold") + 0.16
        deckkit._rect(slide, deckkit.MARGIN, Inches(top), Inches(0.09),
                     Inches(accent_h), METRO_ACCENT)
        frame = deckkit._textbox(slide, deckkit.MARGIN + Inches(0.32),
                                 Inches(top + 0.04),
                                 deckkit.CONTENT_W - Inches(0.32), Inches(accent_h))
        deckkit._para(frame, s.accent, size=22, color=METRO_INK, bold=True,
                      first=True, line_spacing=1.15)
        top += accent_h + 0.26

    if s.caption:
        frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                                 deckkit.CONTENT_W, Inches(0.8))
        deckkit._para(frame, s.caption, size=15, color=METRO_MUTED,
                      italic=True, first=True, line_spacing=1.15)

    if s.origin:
        draw_presenter(slide, s.origin.replace("Presenter: ", "")
                      if s.origin.startswith("Presenter: ") else
                      ("both" if s.origin == "Both presenters" else s.origin))
    metro_footer(slide, position, total)
    deckkit._notes(slide, s.notes)


def render_prompt_text_m(prs, *, title, goal, prompt_text, position, total,
                         notes=()) -> None:
    """A prompt shown whole, never truncated: a short goal line, then the
    exact words to type in a bordered box, sized down a step (19pt, plain
    weight, not bold) so the longest of these prompts still fits one
    slide without clipping. Plain weight on purpose: a long paragraph set
    bold is harder to read, the same reason this kit never bolds a long
    wrapped line elsewhere."""
    slide = _metro_blank(prs)
    top = metro_frame(slide, title, position=position, total=total)
    inner_in = deckkit.CONTENT_W.inches

    if goal:
        frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(top),
                                 deckkit.CONTENT_W, Inches(0.8))
        deckkit._para(frame, goal, size=17, color=METRO_MUTED, italic=True,
                      first=True, line_spacing=1.15)
        top += deckkit._text_height(goal, inner_in, 17, spacing=1.15) + 0.3

    pad = 0.28
    safe_bottom = deckkit.SAFE_BOTTOM - 0.1
    # The longest of these prompts can still overflow a fixed font size;
    # step the size down rather than let the box run into the footer. A
    # small fudge margin on top of the estimate, since _text_height's own
    # wrap estimate can run a touch short of the actual render.
    for size in (19, 17, 15):
        text_h = deckkit._text_height(prompt_text, inner_in - 2 * pad, size,
                                      spacing=1.3) + 0.15
        box_h = text_h + 2 * pad
        if top + box_h <= safe_bottom or size == 15:
            break
    deckkit._rect(slide, deckkit.MARGIN, Inches(top), deckkit.CONTENT_W,
                 Inches(box_h), METRO_WHITE, line=METRO_BORDER)
    frame = deckkit._textbox(slide, deckkit.MARGIN + Inches(pad),
                             Inches(top + pad),
                             deckkit.CONTENT_W - Inches(2 * pad),
                             Inches(text_h))
    deckkit._para(frame, prompt_text, size=size, color=METRO_INK, first=True,
                  line_spacing=1.3)

    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


def render_section_m(prs, *, number: int, title: str, position: int,
                     total: int, notes=()) -> None:
    """A numbered Metropolis section divider: a plain break between the
    deck's parts (e.g. "1 Install Codex"), no frame-title bar, since
    there is no frame title yet at a section break, the same way Beamer's
    own \\section command draws one. Still carries the page number in the
    corner, so numbering stays continuous with the rest of the deck."""
    slide = _metro_blank(prs)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(2.7),
                             deckkit.CONTENT_W, Inches(1.1))
    deckkit._para(frame, str(number), size=54, color=METRO_ACCENT, bold=True,
                  font=METRO_SANS, first=True)
    deckkit._rect(slide, deckkit.MARGIN, Inches(3.75), Inches(1.6), Pt(3),
                  METRO_ACCENT)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(4.05),
                             deckkit.CONTENT_W, Inches(1.1))
    deckkit._para(frame, title, size=36, color=METRO_DARK, font=METRO_SANS,
                  first=True, line_spacing=1.05)

    metro_footer(slide, position, total)
    deckkit._notes(slide, notes)


def render_title_m(prs, s):
    """A plain Metropolis title slide: no colour block, just the title,
    subtitle and presenter on the light background, with a thin accent
    rule under the title."""
    slide = _metro_blank(prs)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(1.5),
                             deckkit.CONTENT_W, Inches(0.5))
    deckkit._para(frame, s.course, size=15, color=METRO_ACCENT, bold=True,
                  font=METRO_SANS, first=True)

    deckkit._rect(slide, deckkit.MARGIN, Inches(2.15), Inches(1.6), Pt(3),
                  METRO_ACCENT)

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(2.55),
                             deckkit.CONTENT_W, Inches(2.4))
    deckkit._para(frame, s.chapter, size=18, color=METRO_MUTED,
                  font=METRO_SANS, first=True)
    deckkit._para(frame, s.title, size=42, color=METRO_DARK,
                  font=METRO_SANS, space_before=10, line_spacing=1.05)

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(5.25),
                             deckkit.CONTENT_W, Inches(1.0))
    deckkit._para(frame, s.subtitle, size=17, color=METRO_INK,
                  font=METRO_SANS, first=True)
    deckkit._para(frame, s.presenter, size=14, color=METRO_MUTED,
                  font=METRO_SANS, space_before=8)

    deckkit._notes(slide, s.notes)


def render_closing_m(prs, s):
    """A plain Metropolis closing slide, the same bookend style as the
    title slide."""
    slide = _metro_blank(prs)
    deckkit._rect(slide, deckkit.MARGIN, Inches(1.65), Inches(1.6), Pt(3),
                  METRO_ACCENT)
    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(2.0),
                             deckkit.CONTENT_W, Inches(1.1))
    deckkit._para(frame, s.title, size=36, color=METRO_DARK,
                  font=METRO_SANS, first=True, line_spacing=1.05)

    frame = deckkit._textbox(slide, deckkit.MARGIN, Inches(3.2),
                             deckkit.CONTENT_W, Inches(2.4))
    for i, line in enumerate(s.lines):
        deckkit._para(frame, line, size=19, color=METRO_INK,
                      font=METRO_SANS, first=(i == 0), space_after=12,
                      line_spacing=1.15)

    if s.accent:
        frame = deckkit._textbox(slide, deckkit.MARGIN,
                                 deckkit.SLIDE_H - Inches(1.3),
                                 deckkit.CONTENT_W, Inches(0.7))
        deckkit._para(frame, s.accent, size=16, color=METRO_ACCENT, bold=True,
                      font=METRO_SANS, first=True)

    deckkit._notes(slide, s.notes)


# --------------------------------------------------------------------------
# Assembling a deck: the common presentation shell every deckN build script
# shares (core properties, the slide-kind dispatch loop, save and repack).
# --------------------------------------------------------------------------

def build_presentation(prs_slides: list[tuple[str, object]], *, out_path: Path,
                       title: str, course: str, author: str,
                       edition: str) -> int:
    """``prs_slides`` is a list of (kind, data) pairs in reading order;
    kind is one of title/section/content/prompt_text/shot/shot_text/step/
    speakers/closing. The title slide (kind == "title") always counts as position
    1, so the on-slide marker matches a slide's actual position in the
    deck."""
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
            render_title_m(prs, slide)
            position += 1
            continue
        pos = position
        position += 1
        if kind == "section":
            render_section_m(prs, number=slide["number"], title=slide["title"],
                            position=pos, total=total,
                            notes=slide.get("notes", ()))
        elif kind == "content":
            render_content_m(prs, slide, position=pos, total=total)
        elif kind == "prompt_text":
            render_prompt_text_m(prs, title=slide["title"], goal=slide.get("goal", ""),
                                prompt_text=slide["prompt_text"],
                                position=pos, total=total,
                                notes=slide.get("notes", ()))
        elif kind == "shot":
            render_shot(prs, title=slide["title"], image_path=slide["path"],
                       credit=slide["credit"], position=pos, total=total,
                       notes=slide.get("notes", ()),
                       band_top=slide.get("band_top"),
                       band_h=slide.get("band_h"),
                       caption_y=slide.get("caption_y"),
                       presenter=slide.get("presenter"),
                       layout=slide.get("layout"))
        elif kind == "shot_text":
            render_shot_text(prs, title=slide["title"],
                            image_path=slide["path"], lines=slide["lines"],
                            accent=slide["accent"], position=pos, total=total,
                            rare=slide.get("rare"), notes=slide.get("notes", ()),
                            presenter=slide.get("presenter"))
        elif kind == "step":
            render_prompt_step(
                prs, title=slide["title"], do_lines=slide["do_lines"],
                do_accent=slide["do_accent"], image_path=slide["path"],
                fallback=slide["fallback"],
                fallback_label=slide.get("fallback_label",
                                        "If it did not work: "),
                source_credit=slide.get("source_credit"),
                position=pos, total=total,
                presenter=slide.get("presenter"), notes=slide.get("notes", ()))
        elif kind == "speakers":
            render_speakers(prs, speakers=slide["speakers"], position=pos,
                           total=total, notes=slide.get("notes", ()))
        elif kind == "closing":
            render_closing_m(prs, slide)
        else:
            raise TypeError(kind)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out_path))
    deckkit._repack_deterministically(out_path)
    return len(prs.slides._sldIdLst)
