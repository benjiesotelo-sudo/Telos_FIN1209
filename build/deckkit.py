"""deckkit - the FEU lecture deck toolkit for FIN1209.

This module knows how to draw slides. It knows nothing about any particular
chapter. Chapter content lives in its own module (see content_chapter01.py)
as plain data, so adding Chapter 2 is a new content file rather than a rewrite.

Design rules encoded here, from the course teaching brief:

  * One idea per slide, six lines of body text at the very most.
  * Every content slide carries a progress marker: "Part 3 of 6 - Classifications".
  * Green carries structure, gold marks the single thing to notice.
  * Check slides look nothing like teaching slides, so the room knows
    instantly that a question is coming.
  * Two or three speaker cue lines in the notes of every content slide.
  * A figure is a slide of its own: title, image, credit line. It renders the
    same with or without the artwork, so the deck built from the public
    repository keeps its slide count and its progress markers.
"""

from __future__ import annotations

import os
import re
import zipfile
from dataclasses import dataclass, field, replace
from datetime import datetime
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# --------------------------------------------------------------------------
# FEU institutional identity
# --------------------------------------------------------------------------

GREEN = RGBColor(0x00, 0x7A, 0x33)  # institution, primary, structure
GREEN_DEEP = RGBColor(0x00, 0x4F, 0x21)  # check slides, section dividers
GOLD = RGBColor(0xF2, 0xA9, 0x00)  # emphasis, achievement, the one thing to notice
INK = RGBColor(0x1A, 0x1A, 0x1A)  # body text
PAPER = RGBColor(0xFA, 0xF8, 0xF2)  # warm page ground
MUTED = RGBColor(0x81, 0x81, 0x81)  # captions, progress markers
BORDER = RGBColor(0xD7, 0xE0, 0xD9)  # soft rules and hairlines
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Display face for titles and section dividers. The FEU identity face is
# Marcellus SC, shared with AMS0011. It is not installed on the build machine
# or on the lecture room PCs, and PowerPoint substitutes a sans for it, which
# loses the display serif entirely. So the deck ships on the named serif
# fallback, Palatino. Once Marcellus SC is installed on the presenting
# machine, rebuild with:
#     .venv/bin/python build/build_chapter1.py --display-font "Marcellus SC"
DISPLAY_FONT = "Palatino"
BODY_FONT = "Arial"  # system sans, present on every teaching machine
MONO_FONT = "Courier New"  # answer keys and data

# Fixed timestamp so a rebuild of unchanged content is byte identical.
EPOCH = datetime(2020, 1, 1, 0, 0, 0)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

MARGIN = Inches(0.85)
CONTENT_W = Emu(SLIDE_W - 2 * MARGIN)

# Where render_figure looks for artwork. The textbook figures are Wiley's and
# are not in this repository, so the folder is gitignored and is usually
# absent. When a figure file is missing the slide still renders, carrying the
# figure number, the credit line and the speaker cue, and the deck keeps its
# slide count and its progress markers. See chapter-01/README.md.
FIGURES_DIR: Path | None = None

# Where render_chart looks for the charts this course draws for itself.
# Unlike the textbook figures these are ours, so they are generated from code
# in this repository by build/chartkit.py rather than being absent from it,
# and the committed deck carries the real artwork rather than a placeholder.
CHARTS_DIR: Path | None = None

# An authored chart is not one of the book's figures and must never be taken
# for one, so it carries its own namespace and its own credit line. This is
# the one place either is written: the exact wording has not been settled, so
# changing it must stay a one line edit.
CHART_NAMESPACE = "Chart"
CHART_CREDIT = ("FIN1209 teaching chart, drawn for this course. "
                "Illustrative data, not a real instrument.")


def chart_credit(letter: str) -> str:
    return f"{CHART_NAMESPACE} {letter} - {CHART_CREDIT}"


# --------------------------------------------------------------------------
# Editions
# --------------------------------------------------------------------------
# One chapter module, two decks. The content file is written once and holds
# everything; the edition decides what reaches the .pptx.
#
#   TEACHING  everything the chapter declares: the checks, their reveals and
#             the speaker cues. This is what the instructor presents from.
#   STUDENT   the same deck with every Check dropped, which removes both the
#             question slide and the reveal slide, and with the speaker cues
#             left out. The cues are written to the instructor, not to a
#             reader, and the checks stop working the moment a student has
#             already seen the questions and the answers.
#
# Nothing else differs: same terms, same figures, same sections, same
# identity. The progress markers are regenerated from the slides the edition
# actually renders, never carried over from the other edition.
TEACHING = "teaching"
STUDENT = "student"
EDITIONS = (TEACHING, STUDENT)

# Set by build(). Read by _notes, which is the single place speaker cues are
# written, so one flag suppresses them everywhere.
INCLUDE_NOTES = True


# --------------------------------------------------------------------------
# Content model - what a chapter module hands to the builder
# --------------------------------------------------------------------------


@dataclass
class Slide:
    """Base for every slide the chapter content declares."""

    notes: tuple[str, ...] = field(default_factory=tuple)
    # Where the slide's content comes from, and whose its numbers are: one
    # short line printed bottom right, level with the progress marker. Added
    # for Chapter 5. Empty draws nothing, which is every earlier chapter.
    # Not called source: a Quote already has one, its attribution.
    origin: str = ""


@dataclass
class TitleSlide(Slide):
    course: str = ""
    chapter: str = ""
    title: str = ""
    subtitle: str = ""
    presenter: str = ""


@dataclass
class SectionOpen(Slide):
    number: int = 0
    total: int = 0
    title: str = ""
    covers: tuple[str, ...] = ()
    minutes: str = ""


@dataclass
class Content(Slide):
    """A teaching slide. Six body lines maximum, three preferred."""

    title: str = ""
    lines: tuple[str, ...] = ()
    accent: str = ""  # the one gold line, the thing to notice
    caption: str = ""  # small muted line under the accent


@dataclass
class Term(Slide):
    """A new term, taught plain words first and formal definition last."""

    term: str = ""
    plain: str = ""
    example: str = ""
    formal: str = ""


@dataclass
class Quote(Slide):
    """A short attributed quotation of a famous definition."""

    text: str = ""
    source: str = ""
    takeaway: str = ""


# The colours a numbered mark is drawn in, in order: mark 1 takes the first,
# mark 2 the second, and so on, unless a Mark names its own. The deck's own
# gold and green, plus three more chosen to stay apart from them and from
# each other on a white scan and on the paper ground, because the same colour
# also prints the mark's number in the slide text.
MARK_COLORS = {
    "gold": RGBColor(0xE0, 0x9B, 0x00),
    "red": RGBColor(0xC6, 0x28, 0x28),
    "blue": RGBColor(0x1F, 0x5F, 0xAD),
    "green": GREEN,
    "purple": RGBColor(0x7B, 0x3F, 0xA0),
}
MARK_KINDS = ("line", "box", "circle", "arrow")


@dataclass(frozen=True)
class Mark:
    """A numbered mark drawn over a Figure or a Chart, pointing at one part.

    The book's figures cannot be edited, so the mark is drawn as pptx shapes
    on top of the picture, and the text beside it names the same part by the
    same number in the same colour.

    ``x0, y0, x1, y1`` are fractions of the picture itself, 0 to 1 from its
    top left corner, not of the slide, so a mark stays on its part wherever
    the picture lands. For a ``line`` they are its two ends; for an ``arrow``
    its tail and then its head; for a ``box`` or a ``circle`` two opposite
    corners of the box it fills. The number sits in a small disc at the start
    of a line or an arrow and on the top left corner of a box or a circle;
    ``at`` moves it to any other point, in the same fractions.

    ``color`` is a MARK_COLORS key; left empty, mark n takes the n-th.

    In the slide's text, ``[n]`` prints as a bold ``(n)`` in mark n's colour.
    Only on a Pair whose picture carries mark n, so a bracketed number
    anywhere else in a deck is left as it is.

        deckkit.Figure(number="6.6", aspect=1.42, shows="...", marks=(
            deckkit.Mark(1, "line", 0.10, 0.62, 0.48, 0.62),
            deckkit.Mark(2, "box", 0.55, 0.70, 0.80, 0.95),
        ))
    """

    number: int
    kind: str
    x0: float
    y0: float
    x1: float
    y1: float
    color: str = ""
    at: tuple[float, float] | None = None
    size: float = 0.34

    @property
    def rgb(self) -> RGBColor:
        if self.color:
            return MARK_COLORS[self.color]
        palette = list(MARK_COLORS.values())
        return palette[(self.number - 1) % len(palette)]


@dataclass
class Figure(Slide):
    """A textbook figure, one to a slide.

    ``number`` is the book's own figure number, "1.11". ``shows`` is one line
    saying what is on the image; it is what the placeholder prints when the
    artwork is absent, so it has to stand on its own as a description.
    """

    title: str = ""
    number: str = ""
    shows: str = ""
    # Numbered marks drawn over the picture; see Mark. A figure that carries
    # marks declares ``aspect``, its artwork's width over its height, so the
    # placeholder takes the artwork's exact box and the marks land in the
    # same place with or without the artwork. The artwork build fails if the
    # file's own aspect disagrees, since every mark would then be off.
    marks: tuple[Mark, ...] = ()
    aspect: float = 0.0
    # The part of the artwork to show, when a slide talks about one panel:
    # (left, top, right, bottom), the fraction cut off each side. The shown
    # part is fitted to the box as the whole would be, so a crop draws it
    # larger, and marks are placed in fractions of the shown part.
    crop: tuple[float, float, float, float] = ()

    @property
    def filename(self) -> str:
        major, minor = self.number.split(".")
        return f"figure-{major}-{int(minor):02d}.png"

    @property
    def credit(self) -> str:
        return (f"Figure {self.number} - Lim, The Handbook of Technical "
                "Analysis (Wiley, 2016)")


@dataclass
class Chart(Slide):
    """A chart this course drew itself, one to a slide.

    Deliberately not a Figure. A Figure is Wiley's, is numbered in the book's
    own scheme, is copyrighted and is absent from this repository; a Chart is
    ours, is lettered A, B, C, is generated at build time from
    build/chartkit.py, and is committed. Keeping them as two types is what
    stops one being quietly credited as the other.

    A chart slide is a companion: it sits immediately after the term slide it
    illustrates and carries no teaching text of its own, because the term
    slide already fills its own page.

    ``letter`` is the chart's name in our namespace. ``shows`` is one line
    saying what is on it, which is what the lecture notes reuse and what the
    placeholder prints if the artwork has not been generated.
    """

    title: str = ""
    letter: str = ""
    shows: str = ""
    # Which run plans keep it. The chart slides are the only slides that can
    # be dropped as a block, so the teaching plan needs to know.
    tier: str = "reinforcement"
    # As on Figure. A chart is drawn on every build, so its aspect comes
    # from the file and need not be declared.
    marks: tuple[Mark, ...] = ()
    aspect: float = 0.0
    crop: tuple[float, float, float, float] = ()

    @property
    def name(self) -> str:
        return f"{CHART_NAMESPACE} {self.letter}"

    @property
    def filename(self) -> str:
        return f"chart-{self.letter.lower()}.png"

    @property
    def credit(self) -> str:
        return chart_credit(self.letter)


@dataclass
class Question:
    stem: str
    options: tuple[str, str, str, str]
    answer: str  # "A" / "B" / "C" / "D"
    reason: str


@dataclass
class Check(Slide):
    """Two multiple choice questions. Rendered as a question slide plus a
    reveal slide, so it always costs two slides in the deck."""

    label: str = ""
    questions: tuple[Question, ...] = ()
    # The Figure or Chart the questions ask about, marks and all, drawn
    # beside them on the question slide and again on the reveal. The two
    # questions then stack in a column ``text_w`` inches wide instead of
    # standing side by side. It must be a picture the chapter already places
    # on a teaching slide, so the student edition, which drops every check,
    # loses no picture.
    picture: Slide | None = None
    text_w: float = 6.6
    # "beside" puts the picture to the right of the stacked questions.
    # "top" draws it as a strip across the top and keeps the two questions
    # side by side under it, at the sizes a check without a picture uses,
    # for a wide, shallow picture such as a crop of one volume panel.
    layout: str = "beside"


CHECK_LAYOUTS = ("beside", "top")


@dataclass
class Pair(Slide):
    """One idea and the picture that shows it, side by side on one slide.

    ``left`` is an ordinary Content or Term and ``picture`` an ordinary
    Figure or Chart, so the two keep their own types, their own credit lines
    and their own rules about what may be committed. The left slide's title
    is the slide's title and the picture's own title is not drawn. The
    speaker cues are the Pair's; any on its two parts are ignored.

    ``text_w`` is the width of the text column in inches. Widen it for a
    long definition beside a simple diagram.
    """

    left: Slide | None = None
    picture: Slide | None = None
    text_w: float = 5.0
    picture_extra: float = 0.0


@dataclass
class Recap(Slide):
    """The you-now-know close of a section."""

    title: str = "You now know"
    items: tuple[str, ...] = ()


@dataclass
class Closing(Slide):
    title: str = ""
    lines: tuple[str, ...] = ()
    accent: str = ""


@dataclass
class Section:
    number: int
    title: str
    short: str  # the word used in the progress marker
    minutes: str
    covers: tuple[str, ...]
    slides: tuple[Slide, ...]
    # None renders no recap slide, for a part whose last check is its recap.
    recap: Recap | None = None


@dataclass
class Chapter:
    course: str
    code: str
    chapter: str
    title: str
    subtitle: str
    presenter: str
    objectives: tuple[str, ...]
    roadmap: tuple[str, ...]
    sections: tuple[Section, ...]
    closing: tuple[Slide, ...]
    # The three below shape the frame build() generates around the parts.
    # Left at their defaults they give the frame Chapters 1 to 3 were built
    # with: generated objectives and roadmap slides, and a divider slide
    # opening every part.
    #
    # ``openers`` replaces the generated objectives and roadmap slides with
    # the chapter's own Content slides. ``title_notes`` replaces the generated
    # cues on the title slide. ``dividers`` set to False drops the divider
    # slide in front of every part.
    openers: tuple[Slide, ...] | None = None
    title_notes: tuple[str, ...] = ()
    dividers: bool = True


# --------------------------------------------------------------------------
# Drawing primitives
# --------------------------------------------------------------------------


def _blank(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _rect(slide, x, y, w, h, fill, line=None, kind=MSO_SHAPE.RECTANGLE):
    shape = slide.shapes.add_shape(kind, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(1)
    # An autoshape carries a theme style reference that renders a drop shadow.
    # Strip it: the identity has no shadows, gradients or effects anywhere.
    style = shape._element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}style")
    if style is not None:
        shape._element.remove(style)
    shape.shadow.inherit = False
    return shape


# Rough text metrics, good enough to lay out a slide without a font engine.
# Average glyph advance as a fraction of the point size.
_ADVANCE = {"regular": 0.50, "bold": 0.53, "mono": 0.60}


def _line_count(text: str, width_in: float, size_pt: float,
                weight: str = "regular") -> int:
    """How many wrapped lines this text needs in a box of the given width."""
    if not text:
        return 0
    per_line = max(1.0, width_in * 72.0 / (size_pt * _ADVANCE[weight]))
    words, lines, current = text.split(), 1, 0
    for word in words:
        need = len(word) + (1 if current else 0)
        if current + need > per_line and current:
            lines += 1
            current = len(word)
        else:
            current += need
    return lines


def _text_height(text: str, width_in: float, size_pt: float,
                 weight: str = "regular", spacing: float = 1.15) -> float:
    """Height in inches of the wrapped text."""
    return _line_count(text, width_in, size_pt, weight) * size_pt * spacing / 72.0


def _ground(slide, color):
    """Paint the whole slide, since a blank layout is transparent."""
    _rect(slide, 0, 0, SLIDE_W, SLIDE_H, color)


def _textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(x, y, w, h)
    frame = box.text_frame
    frame.word_wrap = True
    frame.vertical_anchor = anchor
    frame.margin_left = 0
    frame.margin_right = 0
    frame.margin_top = 0
    frame.margin_bottom = 0
    return frame


def _para(frame, text, *, size, color, font=BODY_FONT, bold=False,
          italic=False, align=PP_ALIGN.LEFT, space_before=0, space_after=0,
          first=False, line_spacing=1.0, hanging=None, refs=None):
    para = frame.paragraphs[0] if first else frame.add_paragraph()
    para.alignment = align
    if hanging is not None:
        # Wrapped lines align under the text, not under the bullet mark.
        pPr = para._pPr if para._pPr is not None else para._p.get_or_add_pPr()
        pPr.set("marL", str(int(hanging)))
        pPr.set("indent", str(int(-hanging)))
    para.space_before = Pt(space_before)
    para.space_after = Pt(space_after)
    para.line_spacing = line_spacing
    # ``refs`` maps a mark number to its colour: each ``[n]`` in the text
    # becomes a bold ``(n)`` in that colour, the same width as what it
    # replaces, so the text measures exactly as written.
    pieces = [(text, color, bold)]
    if refs:
        pieces = []
        for i, piece in enumerate(_REF.split(text)):
            if i % 2 and int(piece) in refs:
                pieces.append((f"({piece})", refs[int(piece)], True))
            elif piece:
                pieces.append((f"[{piece}]" if i % 2 else piece, color, bold))
    for piece, piece_color, piece_bold in pieces:
        run = para.add_run()
        run.text = piece
        run.font.size = Pt(size)
        run.font.bold = piece_bold
        run.font.italic = italic
        run.font.name = font
        run.font.color.rgb = piece_color
    return para


_REF = re.compile(r"\[(\d)\]")


def _notes(slide, cues):
    """Speaker cues, so the instructor always knows the next sentence.

    The student edition carries none of them: they are addressed to the
    instructor and say things about the room that a handout should not.
    """
    if not cues or not INCLUDE_NOTES:
        return
    frame = slide.notes_slide.notes_text_frame
    frame.text = ""
    for i, cue in enumerate(cues):
        para = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        run = para.add_run()
        run.text = "- " + cue
        run.font.size = Pt(14)


def _progress(slide, marker, *, on_dark=False):
    """The small position marker every content slide carries."""
    frame = _textbox(slide, MARGIN, SLIDE_H - Inches(0.72), CONTENT_W, Inches(0.34))
    _para(
        frame,
        marker,
        size=12,
        color=WHITE if on_dark else MUTED,
        first=True,
    )


# The origin line starts clear of the longest progress marker and may wrap
# to a second line, which still ends above the foot of the slide.
ORIGIN_X = 4.7
ORIGIN_PT = 11.0
ORIGIN_MAX_LINES = 2


def _origin(prs, declared):
    """Print a slide's origin line on the slide just rendered.

    Called by build() after the renderer, so no renderer an earlier chapter
    uses was touched to make room for it. A Check carries none: its two
    slides are a question and its answer.
    """
    text = declared.origin
    if not text:
        return
    slide = prs.slides[len(prs.slides._sldIdLst) - 1]
    frame = _textbox(slide, MARGIN + Inches(ORIGIN_X), SLIDE_H - Inches(0.72),
                     CONTENT_W - Inches(ORIGIN_X), Inches(0.5))
    _para(frame, text, size=ORIGIN_PT, color=MUTED, italic=True,
          align=PP_ALIGN.RIGHT, first=True)


def _header_rule(slide, y):
    _rect(slide, MARGIN, y, CONTENT_W, Pt(1.25), BORDER)


def _gold_rule(slide, y, width=Inches(1.6)):
    _rect(slide, MARGIN, y, width, Pt(4), GOLD)


def _chip(slide, x, y, text, *, fill, text_color, width=Inches(1.9)):
    shape = _rect(slide, x, y, width, Inches(0.36), fill)
    frame = shape.text_frame
    frame.word_wrap = False
    frame.margin_left = 0
    frame.margin_right = 0
    frame.margin_top = 0
    frame.margin_bottom = 0
    frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    _para(frame, text, size=12, color=text_color, bold=True,
          align=PP_ALIGN.CENTER, first=True)
    return shape


# --------------------------------------------------------------------------
# Slide renderers
# --------------------------------------------------------------------------


def render_title(prs, s: TitleSlide):
    slide = _blank(prs)
    _ground(slide, GREEN)
    _rect(slide, 0, SLIDE_H - Inches(0.55), SLIDE_W, Inches(0.55), GREEN_DEEP)

    frame = _textbox(slide, MARGIN, Inches(1.55), CONTENT_W, Inches(0.5))
    _para(frame, s.course, size=15, color=GOLD, bold=True, first=True)

    _gold_rule(slide, Inches(2.25))

    frame = _textbox(slide, MARGIN, Inches(2.65), CONTENT_W, Inches(2.4))
    _para(frame, s.chapter, size=20, color=WHITE, font=DISPLAY_FONT, first=True)
    _para(frame, s.title, size=44, color=WHITE, font=DISPLAY_FONT,
          space_before=10, line_spacing=1.05)

    frame = _textbox(slide, MARGIN, Inches(5.35), CONTENT_W, Inches(1.0))
    _para(frame, s.subtitle, size=16, color=WHITE, first=True)
    _para(frame, s.presenter, size=14, color=GOLD, space_before=8)

    _notes(slide, s.notes)


def render_section_open(prs, s: SectionOpen):
    slide = _blank(prs)
    _ground(slide, GREEN)
    _rect(slide, 0, 0, Inches(0.28), SLIDE_H, GOLD)

    frame = _textbox(slide, MARGIN, Inches(1.15), CONTENT_W, Inches(0.4))
    _para(frame, f"Part {s.number} of {s.total}", size=15, color=GOLD,
          bold=True, first=True)

    frame = _textbox(slide, MARGIN, Inches(1.75), CONTENT_W, Inches(1.2))
    _para(frame, s.title, size=40, color=WHITE, font=DISPLAY_FONT,
          first=True, line_spacing=1.05)

    _rect(slide, MARGIN, Inches(3.2), Inches(1.6), Pt(3), GOLD)

    frame = _textbox(slide, MARGIN, Inches(3.7), CONTENT_W, Inches(2.2))
    for i, line in enumerate(s.covers):
        _para(frame, line, size=19, color=WHITE, first=(i == 0),
              space_after=10, line_spacing=1.15)

    frame = _textbox(slide, MARGIN, SLIDE_H - Inches(0.9), CONTENT_W, Inches(0.4))
    _para(frame, s.minutes, size=12, color=GOLD, first=True)

    _notes(slide, s.notes)


def _content_frame(slide, title, marker):
    """Shared chrome for every paper-ground teaching slide."""
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GREEN)

    frame = _textbox(slide, MARGIN, Inches(0.72), CONTENT_W, Inches(1.0))
    _para(frame, title, size=30, color=GREEN, font=DISPLAY_FONT, first=True,
          line_spacing=1.05)
    _header_rule(slide, Inches(1.72))
    _progress(slide, marker)


def render_content(prs, s: Content, marker):
    slide = _blank(prs)
    _content_frame(slide, s.title, marker)

    inner_in = CONTENT_W.inches
    top = 2.15
    if s.lines:
        frame = _textbox(slide, MARGIN, Inches(top), CONTENT_W, Inches(3.4))
        for i, line in enumerate(s.lines):
            _para(frame, line, size=21, color=INK, first=(i == 0),
                  space_after=13, line_spacing=1.18)
        top += sum(_text_height(line, inner_in, 21, spacing=1.18) + 0.20
                   for line in s.lines) + 0.34

    if s.accent:
        accent_h = _text_height(s.accent, inner_in - 0.32, 22, "bold") + 0.16
        _rect(slide, MARGIN, Inches(top), Inches(0.09), Inches(accent_h), GOLD)
        frame = _textbox(slide, MARGIN + Inches(0.32), Inches(top + 0.04),
                         CONTENT_W - Inches(0.32), Inches(accent_h))
        _para(frame, s.accent, size=22, color=INK, bold=True, first=True,
              line_spacing=1.15)
        top += accent_h + 0.26

    if s.caption:
        frame = _textbox(slide, MARGIN, Inches(top), CONTENT_W, Inches(0.8))
        _para(frame, s.caption, size=15, color=MUTED, italic=True, first=True,
              line_spacing=1.15)

    _notes(slide, s.notes)


def render_term(prs, s: Term, marker):
    """Plain words, then one concrete example, then the formal definition.
    Never the formal definition first."""
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GREEN)

    _chip(slide, MARGIN, Inches(0.62), "NEW TERM", fill=GOLD,
          text_color=INK, width=Inches(1.35))

    frame = _textbox(slide, MARGIN, Inches(1.15), CONTENT_W, Inches(0.9))
    _para(frame, s.term, size=32, color=GREEN, font=DISPLAY_FONT, first=True,
          line_spacing=1.05)
    _header_rule(slide, Inches(2.05))

    rows = (
        # Plain words first, one concrete example second, formal definition
        # last. Never the formal definition first.
        ("In plain words", s.plain, True),
        ("For example", s.example, False),
        ("The formal definition", s.formal, False),
    )
    inner_in = CONTENT_W.inches - 0.3
    body_pt = 19.0
    while body_pt > 14.0:
        total = sum(0.42 + _text_height(text, inner_in, body_pt,
                                        "bold" if emph else "regular")
                    for _, text, emph in rows if text)
        if total <= 4.1:
            break
        body_pt -= 1.0

    y = 2.42
    for label, text, emphasise in rows:
        if not text:
            continue
        text_h = _text_height(text, inner_in, body_pt,
                              "bold" if emphasise else "regular")
        _rect(slide, MARGIN, Inches(y + 0.05), Inches(0.07),
              Inches(text_h + 0.28), GOLD if emphasise else BORDER)
        frame = _textbox(slide, MARGIN + Inches(0.3), Inches(y),
                         CONTENT_W - Inches(0.3), Inches(text_h + 0.4))
        _para(frame, label.upper(), size=11, color=MUTED, bold=True, first=True,
              space_after=4)
        _para(frame, text, size=body_pt, color=INK, bold=emphasise,
              line_spacing=1.15)
        y += 0.42 + text_h + 0.24

    _progress(slide, marker)
    _notes(slide, s.notes)


def render_quote(prs, s: Quote, marker):
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GREEN)
    quoted = '"' + s.text + '"'
    inner_in = CONTENT_W.inches - 0.42
    quote_h = _text_height(quoted, inner_in, 25, spacing=1.2)
    source_h = _text_height(s.source, inner_in, 14) + 0.2
    _rect(slide, MARGIN, Inches(1.45), Inches(0.12),
          Inches(quote_h + source_h + 0.2), GOLD)

    frame = _textbox(slide, MARGIN, Inches(0.72), CONTENT_W, Inches(0.5))
    _para(frame, "A definition worth writing down", size=13, color=MUTED,
          bold=True, first=True)

    frame = _textbox(slide, MARGIN + Inches(0.42), Inches(1.5),
                     CONTENT_W - Inches(0.42), Inches(quote_h + source_h + 0.2))
    _para(frame, quoted, size=25, color=INK, font=DISPLAY_FONT,
          first=True, line_spacing=1.2)
    _para(frame, s.source, size=14, color=MUTED, space_before=14)

    frame = _textbox(slide, MARGIN, Inches(1.5 + quote_h + source_h + 0.55),
                     CONTENT_W, Inches(1.4))
    _para(frame, "What it tells us", size=11, color=MUTED, bold=True, first=True,
          space_after=6)
    _para(frame, s.takeaway, size=21, color=GREEN, bold=True, line_spacing=1.15)

    _progress(slide, marker)
    _notes(slide, s.notes)


def _png_size(path) -> tuple[int, int]:
    """Pixel dimensions from a PNG header, without an image library."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a PNG")
    return (int.from_bytes(head[16:20], "big"),
            int.from_bytes(head[20:24], "big"))


def _picture_size(picture, path) -> tuple[float, float] | None:
    """The pixel size the picture is fitted by, or None for a full plate.

    The artwork's own size when the file is there. Without it, a picture
    that carries marks and declares its aspect is fitted as if it were
    there, so the placeholder and the marks keep the artwork's exact box.
    """
    if path is not None and path.is_file():
        px_w, px_h = _png_size(path)
        if picture.aspect and abs(px_w / px_h / picture.aspect - 1) > 0.02:
            raise ValueError(
                f"{path.name} is {px_w}x{px_h}, aspect {px_w / px_h:.3f}, "
                f"but its slide declares {picture.aspect}; its marks would "
                "land in the wrong place")
    elif picture.aspect and (picture.marks or picture.crop):
        px_w, px_h = picture.aspect * 1000.0, 1000.0
    else:
        return None
    left, top, right, bottom = picture.crop or (0.0, 0.0, 0.0, 0.0)
    return float(px_w) * (1 - left - right), float(px_h) * (1 - top - bottom)


def _add_picture(slide, picture, path, x, y, w, h):
    """Place the artwork in the box given, cut to its crop if it has one."""
    shape = slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                     Inches(w), Inches(h))
    if picture.crop:
        (shape.crop_left, shape.crop_top, shape.crop_right,
         shape.crop_bottom) = picture.crop
    return shape


def _placeholder_plate(slide, picture, x, y, w, h):
    """The placeholder drawn into a picture's own box, for a marked figure."""
    is_figure = isinstance(picture, Figure)
    _rect(slide, Inches(x), Inches(y), Inches(w), Inches(h), WHITE,
          line=BORDER)
    _rect(slide, Inches(x), Inches(y), Inches(w), Pt(4), GOLD)
    frame = _textbox(slide, Inches(x + 0.3), Inches(y + 0.3),
                     Inches(w - 0.6), Inches(h - 0.5))
    # The box is the artwork's, and a crop can make it shallow, so the
    # description steps down until it fits inside the plate.
    shows_pt = next((pt for pt in (15.0, 13.0, 11.0, 9.0)
                     if 0.4 + _text_height(picture.shows, w - 0.6, pt,
                                           spacing=1.4) <= h - 0.4), 8.0)
    _para(frame,
          f"FIGURE {picture.number}" if is_figure else picture.name.upper(),
          size=11, color=MUTED, bold=True, first=True, space_after=4)
    _para(frame, picture.shows, size=shows_pt, color=INK, font=DISPLAY_FONT,
          line_spacing=1.15)


def _draw_marks(slide, marks, x, y, w, h):
    """Draw each Mark over the picture whose box is given, in inches.

    Plain pptx shapes, outlined and unfilled, so PowerPoint, Keynote and
    LibreOffice draw them alike and the picture shows through. Each number
    sits in a disc of its mark's colour, drawn last so no line crosses it.
    """
    def at(fx, fy):
        return Inches(x + fx * w), Inches(y + fy * h)

    discs = []
    for m in marks:
        color = m.rgb
        if m.kind in ("line", "arrow"):
            shape = slide.shapes.add_connector(
                MSO_CONNECTOR.STRAIGHT, *at(m.x0, m.y0), *at(m.x1, m.y1))
            if m.kind == "arrow":
                ln = shape.line._get_or_add_ln()
                ln.append(ln.makeelement(qn("a:tailEnd"), {
                    "type": "triangle", "w": "med", "len": "med"}))
            label = m.at or (m.x0, m.y0)
        else:
            left, top = min(m.x0, m.x1), min(m.y0, m.y1)
            shape = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE if m.kind == "box" else MSO_SHAPE.OVAL,
                *at(left, top), Inches(abs(m.x1 - m.x0) * w),
                Inches(abs(m.y1 - m.y0) * h))
            shape.fill.background()
            label = m.at or (left, top)
        shape.line.color.rgb = color
        shape.line.width = Pt(3.5)
        style = shape._element.find(qn("p:style"))
        if style is not None:
            shape._element.remove(style)
        discs.append((m.number, color, label))

    for number, color, (fx, fy) in discs:
        d = next((m.size for m in marks if m.number == number), 0.34)
        cx, cy = at(fx, fy)
        disc = _rect(slide, cx - Inches(d / 2), cy - Inches(d / 2),
                     Inches(d), Inches(d), color, line=WHITE,
                     kind=MSO_SHAPE.OVAL)
        frame = disc.text_frame
        frame.word_wrap = False
        frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        for side in ("left", "right", "top", "bottom"):
            setattr(frame, f"margin_{side}", 0)
        _para(frame, str(number), size=13, color=WHITE, bold=True,
              align=PP_ALIGN.CENTER, first=True)


# The band a figure is drawn into, between the header rule and the credit line.
FIGURE_TOP = 1.98
FIGURE_H = 4.10
FIGURE_CAPTION_Y = 6.20


def render_figure(prs, s: Figure, marker):
    """A textbook figure, one to a slide, with a credit line under it.

    Renders identically whether or not the artwork is present. When the file
    is missing the image band carries a placeholder plate naming the figure
    and saying what it shows, so the deck built from the public repository is
    complete and the instructor can see exactly what is meant to be there.
    """
    slide = _blank(prs)
    _content_frame(slide, s.title, marker)

    band_w = CONTENT_W.inches
    path = None if FIGURES_DIR is None else Path(FIGURES_DIR) / s.filename
    size = _picture_size(s, path)

    if size is not None:
        px_w, px_h = size
        pad = 0.13
        scale = min((band_w - 2 * pad) / px_w, (FIGURE_H - 2 * pad) / px_h)
        w, h = px_w * scale, px_h * scale
        x = MARGIN.inches + (band_w - w) / 2.0
        y = FIGURE_TOP + (FIGURE_H - h) / 2.0
        # A white plate under the artwork: the figures are scans on white and
        # the page ground is warm paper, so an unframed image looks like a
        # patch. The plate makes the edge deliberate.
        _rect(slide, Inches(x - pad), Inches(y - pad),
              Inches(w + 2 * pad), Inches(h + 2 * pad), WHITE, line=BORDER)
        if path is not None and path.is_file():
            _add_picture(slide, s, path, x, y, w, h)
        else:
            _placeholder_plate(slide, s, x, y, w, h)
        _draw_marks(slide, s.marks, x, y, w, h)
    else:
        plate_w = min(8.2, band_w)
        x = MARGIN.inches + (band_w - plate_w) / 2.0
        _rect(slide, Inches(x), Inches(FIGURE_TOP), Inches(plate_w),
              Inches(FIGURE_H), WHITE, line=BORDER)
        _rect(slide, Inches(x), Inches(FIGURE_TOP), Inches(plate_w),
              Pt(4), GOLD)

        frame = _textbox(slide, Inches(x + 0.6), Inches(FIGURE_TOP + 0.7),
                         Inches(plate_w - 1.2), Inches(FIGURE_H - 1.2))
        _para(frame, f"FIGURE {s.number}", size=15, color=MUTED, bold=True,
              first=True, space_after=14)
        _para(frame, s.shows, size=22, color=INK, font=DISPLAY_FONT,
              line_spacing=1.2, space_after=18)
        _para(frame,
              "The artwork is copyrighted and is not in the public "
              "repository. Build with assets/figures/ present to place it here.",
              size=14, color=MUTED, italic=True, line_spacing=1.15)

    frame = _textbox(slide, MARGIN, Inches(FIGURE_CAPTION_Y), CONTENT_W,
                     Inches(0.34))
    _para(frame, s.credit, size=13, color=MUTED, first=True)

    _notes(slide, s.notes)


def render_chart(prs, s: Chart, marker):
    """One of our own charts, one to a slide, with our own credit under it.

    The geometry is the figure band's, so a chart and a figure sit in exactly
    the same place on the page and the deck does not jump between them. What
    differs is the credit line, which names it as ours, and the fact that the
    artwork is normally there: the build generates it.
    """
    slide = _blank(prs)
    _content_frame(slide, s.title, marker)

    band_w = CONTENT_W.inches
    path = None if CHARTS_DIR is None else Path(CHARTS_DIR) / s.filename
    size = _picture_size(s, path)

    if size is not None:
        px_w, px_h = size
        pad = 0.13
        scale = min((band_w - 2 * pad) / px_w, (FIGURE_H - 2 * pad) / px_h)
        w, h = px_w * scale, px_h * scale
        x = MARGIN.inches + (band_w - w) / 2.0
        y = FIGURE_TOP + (FIGURE_H - h) / 2.0
        _rect(slide, Inches(x - pad), Inches(y - pad),
              Inches(w + 2 * pad), Inches(h + 2 * pad), WHITE, line=BORDER)
        if path is not None and path.is_file():
            _add_picture(slide, s, path, x, y, w, h)
        else:
            _placeholder_plate(slide, s, x, y, w, h)
        _draw_marks(slide, s.marks, x, y, w, h)
    else:
        # Only reachable if a caller skipped the generation step. The slide
        # still renders so the deck keeps its count and its markers.
        plate_w = min(8.2, band_w)
        x = MARGIN.inches + (band_w - plate_w) / 2.0
        _rect(slide, Inches(x), Inches(FIGURE_TOP), Inches(plate_w),
              Inches(FIGURE_H), WHITE, line=BORDER)
        _rect(slide, Inches(x), Inches(FIGURE_TOP), Inches(plate_w),
              Pt(4), GOLD)
        frame = _textbox(slide, Inches(x + 0.6), Inches(FIGURE_TOP + 0.7),
                         Inches(plate_w - 1.2), Inches(FIGURE_H - 1.2))
        _para(frame, s.name.upper(), size=15, color=MUTED, bold=True,
              first=True, space_after=14)
        _para(frame, s.shows, size=22, color=INK, font=DISPLAY_FONT,
              line_spacing=1.2, space_after=18)
        _para(frame,
              "This chart is generated by build/chartkit.py and was not "
              "drawn for this build. Rerun the build to place it.",
              size=14, color=MUTED, italic=True, line_spacing=1.15)

    frame = _textbox(slide, MARGIN, Inches(FIGURE_CAPTION_Y), CONTENT_W,
                     Inches(0.34))
    _para(frame, s.credit, size=13, color=MUTED, first=True)

    _notes(slide, s.notes)


def render_check(prs, s: Check, marker, index, total):
    """Question slide. Deliberately unlike any teaching slide: deep green
    ground, gold CHECK chip, two questions side by side."""
    if s.picture is not None and s.layout == "top":
        return _render_check_top(prs, s, marker, index, total)
    if s.picture is not None:
        return _render_check_beside(prs, s, marker, index, total)
    slide = _blank(prs)
    _ground(slide, GREEN_DEEP)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)

    _chip(slide, MARGIN, Inches(0.55), f"CHECK {index} OF {total}", fill=GOLD,
          text_color=INK, width=Inches(1.85))

    frame = _textbox(slide, MARGIN + Inches(2.1), Inches(0.57), Inches(8.0),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=WHITE, bold=True, first=True)

    col_w = Emu(int((CONTENT_W - Inches(0.7)) / 2))
    inner_in = col_w.inches - 0.6
    card_top, card_h = 1.32, 5.02
    budget = card_h - 0.95  # padding, the Q label, and the gap under the stem

    # Both columns share one pair of font sizes, chosen for the worse of the
    # two questions, so a long department-style stem never overlaps its options.
    stem_pt, opt_pt = 17.0, 15.0
    for stem_try, opt_try in ((17.0, 15.0), (16.0, 14.0), (15.0, 13.5),
                              (14.0, 13.0), (13.0, 12.0), (12.0, 11.0)):
        worst = max(
            _text_height(q.stem, inner_in, stem_try, "bold")
            + sum(_text_height(f"D.  {o}", inner_in, opt_try) + 0.13
                  for o in q.options)
            for q in s.questions
        )
        stem_pt, opt_pt = stem_try, opt_try
        if worst <= budget:
            break

    tallest_stem = max(_text_height(q.stem, inner_in, stem_pt, "bold")
                       for q in s.questions)

    for i, q in enumerate(s.questions):
        x = MARGIN + (col_w + Inches(0.7)) * i
        _rect(slide, x, Inches(card_top), col_w, Inches(card_h), GREEN)

        frame = _textbox(slide, x + Inches(0.3), Inches(card_top + 0.27),
                         col_w - Inches(0.6), Inches(0.25))
        _para(frame, f"Q{i + 1}", size=12, color=GOLD, bold=True, first=True)

        stem_top = card_top + 0.58
        stem_h = _text_height(q.stem, inner_in, stem_pt, "bold")
        frame = _textbox(slide, x + Inches(0.3), Inches(stem_top),
                         col_w - Inches(0.6), Inches(stem_h + 0.1))
        _para(frame, q.stem, size=stem_pt, color=WHITE, bold=True, first=True,
              line_spacing=1.15)

        # Options start on a shared baseline so the two columns read as a pair
        # even when one stem is much longer than the other.
        frame = _textbox(slide, x + Inches(0.3),
                         Inches(stem_top + tallest_stem + 0.32),
                         col_w - Inches(0.6), Inches(3.2))
        for j, opt in enumerate(q.options):
            _para(frame, f"{'ABCD'[j]}.  {opt}", size=opt_pt, color=WHITE,
                  first=(j == 0), space_after=9, line_spacing=1.12)

    _progress(slide, marker, on_dark=True)
    _notes(slide, s.notes or (
        "Read Q1 aloud, then Q2. Give them sixty seconds and no discussion.",
        "Ask for a show of hands on each option before you advance.",
        "This is for reading the room, not for marks. Say so if anyone tenses up.",
    ))


def render_reveal(prs, s: Check, marker, index, total):
    """Answer slide. Paper ground so the room feels the release, with the
    answers in the monospace face and one line of reason each."""
    if s.picture is not None and s.layout == "top":
        return _render_reveal_top(prs, s, marker, index, total)
    if s.picture is not None:
        return _render_reveal_beside(prs, s, marker, index, total)
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)

    _chip(slide, MARGIN, Inches(0.55), "ANSWERS", fill=GREEN,
          text_color=WHITE, width=Inches(1.35))

    frame = _textbox(slide, MARGIN + Inches(1.6), Inches(0.57), Inches(8.5),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=GREEN, bold=True, first=True)

    inner_in = CONTENT_W.inches - 0.8
    available = 5.1  # from y = 1.32 down to the progress marker

    # Shrink together until both cards fit. The answer stays in the monospace
    # face and stays the largest thing on the slide.
    stem_pt, ans_pt, reason_pt = 16.0, 20.0, 16.0
    for stem_try, ans_try, reason_try in ((16.0, 20.0, 16.0), (15.0, 18.0, 15.0),
                                          (14.0, 17.0, 14.0), (13.0, 15.0, 13.0)):
        heights = [
            0.95
            + _text_height(f"Q1   {q.stem}", inner_in, stem_try)
            + _text_height(f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}",
                           inner_in, ans_try, "mono")
            + _text_height(q.reason, inner_in, reason_try)
            for q in s.questions
        ]
        stem_pt, ans_pt, reason_pt = stem_try, ans_try, reason_try
        if sum(heights) + 0.27 <= available:
            break

    y = 1.32
    for i, q in enumerate(s.questions):
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        stem_h = _text_height(stem, inner_in, stem_pt)
        ans_h = _text_height(answer, inner_in, ans_pt, "mono")
        card_h = 0.95 + stem_h + ans_h + _text_height(q.reason, inner_in, reason_pt)

        _rect(slide, MARGIN, Inches(y), CONTENT_W, Inches(card_h), WHITE,
              line=BORDER)
        _rect(slide, MARGIN, Inches(y), Inches(0.1), Inches(card_h), GOLD)

        frame = _textbox(slide, MARGIN + Inches(0.4), Inches(y + 0.26),
                         CONTENT_W - Inches(0.8), Inches(stem_h + 0.1))
        _para(frame, stem, size=stem_pt, color=MUTED, first=True,
              line_spacing=1.15)

        frame = _textbox(slide, MARGIN + Inches(0.4),
                         Inches(y + 0.26 + stem_h + 0.28),
                         CONTENT_W - Inches(0.8), Inches(ans_h + 1.0))
        _para(frame, answer, size=ans_pt, color=GREEN, font=MONO_FONT,
              bold=True, first=True, line_spacing=1.15)
        _para(frame, q.reason, size=reason_pt, color=INK, space_before=7,
              line_spacing=1.15)

        y += card_h + 0.27

    _progress(slide, marker)
    _notes(slide, s.notes or (
        "Reveal one at a time. Say the reason out loud, not just the letter.",
        "If more than a third of the room missed one, step back and reteach it.",
    ))


# --------------------------------------------------------------------------
# A picture beside the idea it shows. Added for Chapter 4 as a renderer of
# its own, so no renderer an earlier chapter uses was touched to make room
# for it.
# --------------------------------------------------------------------------

# How far apart a Pair holds its text column and its picture column.
PAIR_GAP = 0.35
# A narrow column wraps into many more lines than a full width slide does, so
# a Pair cannot lean on the loose line height the wide slides get away with.
# _text_height counts a line as its point size times the spacing it is given,
# and a rendered line of Arial is about 1.2 times its point size before any
# line spacing is applied. These are the spacings render_pair sets and the
# heights _pair_fit therefore measures with.
_PAIR_NATURAL = 1.2
_PAIR_BODY_SPACING = 1.05
_PAIR_BODY_H = _PAIR_BODY_SPACING * _PAIR_NATURAL
_PAIR_TIGHT_H = 1.0 * _PAIR_NATURAL
# The picture column's band ends here and its credit line sits under it.
PAIR_BAND_BOTTOM = 6.08
PAIR_CREDIT_Y = 6.18
# Where the picture column starts beside a term, whose heading sits lower
# than a teaching slide's. chartkit reads this to draw a chart that fills
# the column exactly.
PAIR_TERM_TOP = 2.36


def _pair_fit(s: Pair) -> tuple[float, float]:
    """The body size render_pair will use, and where its text column ends.

    One function for the renderer and for the validator, on purpose: the
    term slide check measures at a different size from the one the renderer
    picks, and reads low because of it.
    """
    left, width = s.left, s.text_w
    if isinstance(left, Term):
        rows = ((left.plain, "bold"), (left.example, "regular"),
                (left.formal, "regular"))
        for pt in (18.0, 17.0, 16.0, 15.0, 14.0):
            bottom = 2.42 + sum(
                0.30 + _text_height(text, width - 0.3, pt, weight,
                                    spacing=_PAIR_TIGHT_H) + 0.20
                for text, weight in rows if text)
            if bottom <= SAFE_BOTTOM or pt == 14.0:
                return pt, bottom
    for pt in (20.0, 19.0, 18.0, 17.0, 16.0, 15.0):
        bottom = 2.15
        if left.lines:
            bottom += sum(_text_height(line, width, pt,
                                       spacing=_PAIR_BODY_H) + 0.18
                          for line in left.lines) + 0.22
        if left.accent:
            bottom += (_text_height(left.accent, width - 0.32, pt + 1, "bold",
                                    spacing=_PAIR_TIGHT_H) + 0.16 + 0.22)
        if left.caption:
            bottom += _text_height(left.caption, width, 13,
                                   spacing=_PAIR_TIGHT_H)
        if bottom <= SAFE_BOTTOM or pt == 15.0:
            return pt, bottom
    return 15.0, SAFE_BOTTOM


def _pair_picture(slide, picture, x, top, w, h):
    """Draw a Figure or a Chart into the box given, or its placeholder.

    The artwork is fitted to the box and sits at its top, level with the
    text beside it, with its credit line directly under it. The placeholder
    fills the box and carries its credit at the foot, so a build without the
    artwork gives the text column exactly the same room.
    """
    is_figure = isinstance(picture, Figure)
    root = FIGURES_DIR if is_figure else CHARTS_DIR
    path = None if root is None else Path(root) / picture.filename
    size = _picture_size(picture, path)

    if size is not None:
        px_w, px_h = size
        pad = 0.13
        scale = min((w - 2 * pad) / px_w, (h - 2 * pad) / px_h)
        pic_w, pic_h = px_w * scale, px_h * scale
        pic_x = x + (w - pic_w) / 2.0
        pic_y = top + pad
        _rect(slide, Inches(pic_x - pad), Inches(pic_y - pad),
              Inches(pic_w + 2 * pad), Inches(pic_h + 2 * pad), WHITE,
              line=BORDER)
        if path is not None and path.is_file():
            _add_picture(slide, picture, path, pic_x, pic_y, pic_w, pic_h)
        else:
            _placeholder_plate(slide, picture, pic_x, pic_y, pic_w, pic_h)
        _draw_marks(slide, picture.marks, pic_x, pic_y, pic_w, pic_h)
        # The credit sits just under the artwork rather than at the foot of
        # the band, so a shallow picture and its credit read as one thing.
        credit_y = pic_y + pic_h + pad + 0.10
    else:
        credit_y = PAIR_CREDIT_Y
        _rect(slide, Inches(x), Inches(top), Inches(w), Inches(h), WHITE,
              line=BORDER)
        _rect(slide, Inches(x), Inches(top), Inches(w), Pt(4), GOLD)
        frame = _textbox(slide, Inches(x + 0.45), Inches(top + 0.5),
                         Inches(w - 0.9), Inches(h - 0.8))
        _para(frame,
              f"FIGURE {picture.number}" if is_figure else picture.name.upper(),
              size=14, color=MUTED, bold=True, first=True, space_after=12)
        _para(frame, picture.shows, size=18, color=INK, font=DISPLAY_FONT,
              line_spacing=1.2, space_after=14)
        _para(frame,
              ("The artwork is copyrighted and is not in the public "
               "repository. Build with assets/figures/ present to place it "
               "here.") if is_figure else
              ("This chart is generated by build/chartkit.py and was not "
               "drawn for this build. Rerun the build to place it."),
              size=12, color=MUTED, italic=True, line_spacing=1.15)

    # The credit keeps to one line: a second would run past the safe bottom
    # under a placeholder, so a narrow column steps the type down instead.
    credit_pt = next((pt for pt in (12.0, 11.0, 10.0, 9.0)
                      if _line_count(picture.credit, w, pt) == 1), 9.0)
    frame = _textbox(slide, Inches(x), Inches(credit_y), Inches(w),
                     Inches(0.3))
    _para(frame, picture.credit, size=credit_pt, color=MUTED, first=True)


def render_pair(prs, s: Pair, marker):
    """Text on the left, the picture that shows it on the right.

    The left column is drawn the way its own slide type is drawn, a teaching
    slide or a new term, only narrower. The picture keeps the credit line
    its type carries everywhere else in the deck.
    """
    slide = _blank(prs)
    left = s.left
    text_w = Inches(s.text_w)
    body_pt, _bottom = _pair_fit(s)
    # Each [n] in the text is printed in mark n's colour; see Mark.
    refs = {m.number: m.rgb for m in s.picture.marks} or None

    if isinstance(left, Term):
        _ground(slide, PAPER)
        _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GREEN)
        _chip(slide, MARGIN, Inches(0.62), "NEW TERM", fill=GOLD,
              text_color=INK, width=Inches(1.35))
        frame = _textbox(slide, MARGIN, Inches(1.15), CONTENT_W, Inches(0.9))
        _para(frame, left.term, size=32, color=GREEN, font=DISPLAY_FONT,
              first=True, line_spacing=1.05)
        _header_rule(slide, Inches(2.05))
        _progress(slide, marker)

        rows = (
            # The same teaching order as render_term: plain words first.
            ("In plain words", left.plain, True),
            ("For example", left.example, False),
            ("The formal definition", left.formal, False),
        )
        inner = s.text_w - 0.3
        y = 2.42
        for label, text, emphasise in rows:
            if not text:
                continue
            text_h = _text_height(text, inner, body_pt,
                                  "bold" if emphasise else "regular",
                                  spacing=_PAIR_TIGHT_H)
            _rect(slide, MARGIN, Inches(y + 0.05), Inches(0.07),
                  Inches(text_h + 0.22), GOLD if emphasise else BORDER)
            frame = _textbox(slide, MARGIN + Inches(0.3), Inches(y),
                             text_w - Inches(0.3), Inches(text_h + 0.34))
            _para(frame, label.upper(), size=10.5, color=MUTED, bold=True,
                  first=True, space_after=3)
            _para(frame, text, size=body_pt, color=INK, bold=emphasise,
                  line_spacing=1.0, refs=refs)
            y += 0.30 + text_h + 0.20
        band_top = PAIR_TERM_TOP
    else:
        _content_frame(slide, left.title, marker)
        top = 2.15
        if left.lines:
            frame = _textbox(slide, MARGIN, Inches(top), text_w, Inches(3.4))
            for i, line in enumerate(left.lines):
                _para(frame, line, size=body_pt, color=INK, first=(i == 0),
                      space_after=11, line_spacing=_PAIR_BODY_SPACING,
                      refs=refs)
            top += sum(_text_height(line, s.text_w, body_pt,
                                    spacing=_PAIR_BODY_H)
                       + 0.18 for line in left.lines) + 0.22
        if left.accent:
            accent_h = _text_height(left.accent, s.text_w - 0.32,
                                    body_pt + 1, "bold",
                                    spacing=_PAIR_TIGHT_H) + 0.16
            _rect(slide, MARGIN, Inches(top), Inches(0.09), Inches(accent_h),
                  GOLD)
            frame = _textbox(slide, MARGIN + Inches(0.32), Inches(top + 0.04),
                             text_w - Inches(0.32), Inches(accent_h))
            _para(frame, left.accent, size=body_pt + 1, color=INK, bold=True,
                  first=True, line_spacing=1.0, refs=refs)
            top += accent_h + 0.22
        if left.caption:
            frame = _textbox(slide, MARGIN, Inches(top), text_w, Inches(0.8))
            _para(frame, left.caption, size=13, color=MUTED, italic=True,
                  first=True, line_spacing=1.0, refs=refs)
        band_top = FIGURE_TOP

    x = MARGIN.inches + s.text_w + PAIR_GAP
    _pair_picture(slide, s.picture, x, band_top,
                  CONTENT_W.inches - s.text_w - PAIR_GAP + s.picture_extra,
                  PAIR_BAND_BOTTOM - band_top)

    _notes(slide, s.notes)


def render_recap(prs, s: Recap, marker):
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GREEN)
    _rect(slide, SLIDE_W - Inches(0.28), 0, Inches(0.28), SLIDE_H, GOLD)

    frame = _textbox(slide, MARGIN, Inches(0.72), CONTENT_W - Inches(0.5),
                     Inches(0.9))
    _para(frame, s.title, size=32, color=GREEN, font=DISPLAY_FONT, first=True)
    _header_rule(slide, Inches(1.72))

    col_w = Emu(int((CONTENT_W - Inches(1.1)) / 2))
    inner_in = col_w.inches
    available = 4.15  # from y = 2.15 down to the progress marker

    # Recap lists vary in length between sections, so size the type to the
    # list and split the two columns by height rather than by item count.
    size, gap = 18.0, 0.17
    columns = ((), ())
    for try_size in (18.0, 17.0, 16.0, 15.0, 14.0, 13.0):
        heights = [_text_height("- " + item, inner_in, try_size) + gap
                   for item in s.items]
        target = sum(heights) / 2.0
        split, running = len(s.items), 0.0
        for i, h in enumerate(heights):
            if running + h / 2 > target:
                split = i
                break
            running += h
        left, right = heights[:split], heights[split:]
        size = try_size
        columns = (s.items[:split], s.items[split:])
        if max(sum(left), sum(right)) <= available:
            break

    for c, items in enumerate(columns):
        if not items:
            continue
        x = MARGIN + (col_w + Inches(0.6)) * c
        frame = _textbox(slide, x, Inches(2.15), col_w, Inches(available))
        for i, item in enumerate(items):
            _para(frame, "\u25aa  " + item, size=size, color=INK,
                  first=(i == 0), space_after=int(gap * 72), line_spacing=1.12,
                  hanging=Inches(0.26))

    _progress(slide, marker)
    _notes(slide, s.notes)


# --------------------------------------------------------------------------
# A check and its reveal with the picture they ask about beside them. Their
# own renderers, so a check without a picture renders exactly as before.
# --------------------------------------------------------------------------

# The type sizes a check beside a picture steps through, largest first, and
# never below twelve point.
_BESIDE_SIZES = ((17.0, 17.0),)
BESIDE_TOP = 1.32
BESIDE_BOTTOM = 6.30


def _beside_picture(slide, s: Check, reveal=False):
    x = MARGIN.inches + s.text_w + PAIR_GAP
    picture = s.picture
    # LibreOffice can paint a repeated cropped image blank when the answer
    # slide reuses the exact same source rectangle as the question slide.
    # A small crop change preserves the teaching crop and keeps the marks
    # aligned while giving the answer its own image paint operation.
    if reveal and isinstance(picture, Figure) and picture.crop:
        left, top, right, bottom = picture.crop
        picture = replace(picture, crop=(left - 0.01, top,
                                         right - 0.01, bottom))
    _pair_picture(slide, picture, x, BESIDE_TOP,
                  CONTENT_W.inches - s.text_w - PAIR_GAP,
                  PAIR_BAND_BOTTOM - BESIDE_TOP)


def _render_check_beside(prs, s: Check, marker, index, total):
    """The question slide with the two questions stacked on the left and the
    picture on the right, at the largest size at which both fit."""
    slide = _blank(prs)
    _ground(slide, GREEN_DEEP)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)
    _chip(slide, MARGIN, Inches(0.55), f"CHECK {index} OF {total}", fill=GOLD,
          text_color=INK, width=Inches(1.85))
    frame = _textbox(slide, MARGIN + Inches(2.1), Inches(0.57), Inches(8.0),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=WHITE, bold=True, first=True)

    inner_in = s.text_w - 0.5
    gap = 0.10

    def card_heights(stem_pt, opt_pt):
        return [0.28 + _text_height(q.stem, inner_in, stem_pt, "bold") + 0.08
                + sum(_text_height(f"D.  {o}", inner_in, opt_pt) + 0.04
                      for o in q.options) + 0.08
                for q in s.questions]

    for stem_pt, opt_pt in _BESIDE_SIZES:
        heights = card_heights(stem_pt, opt_pt)
        if sum(heights) + gap * (len(heights) - 1) <= BESIDE_BOTTOM - BESIDE_TOP:
            break

    y = BESIDE_TOP
    for i, (q, card_h) in enumerate(zip(s.questions, heights)):
        _rect(slide, MARGIN, Inches(y), Inches(s.text_w), Inches(card_h), GREEN)
        frame = _textbox(slide, MARGIN + Inches(0.25), Inches(y + 0.10),
                         Inches(inner_in), Inches(0.25))
        _para(frame, f"Q{i + 1}", size=12, color=GOLD, bold=True, first=True)
        stem_h = _text_height(q.stem, inner_in, stem_pt, "bold")
        frame = _textbox(slide, MARGIN + Inches(0.25), Inches(y + 0.32),
                         Inches(inner_in), Inches(stem_h + 0.1))
        _para(frame, q.stem, size=stem_pt, color=WHITE, bold=True, first=True,
              line_spacing=1.15)
        frame = _textbox(slide, MARGIN + Inches(0.25),
                         Inches(y + 0.32 + stem_h + 0.08), Inches(inner_in),
                         Inches(card_h - stem_h - 0.48))
        for j, opt in enumerate(q.options):
            _para(frame, f"{'ABCD'[j]}.  {opt}", size=opt_pt, color=WHITE,
                  first=(j == 0), space_after=2, line_spacing=1.05)
        y += card_h + gap

    _beside_picture(slide, s)
    _progress(slide, marker, on_dark=True)
    _notes(slide, s.notes or (
        "Read Q1 aloud, then Q2. Give them sixty seconds and no discussion.",
        "Ask for a show of hands on each option before you advance.",
        "This is for reading the room, not for marks. Say so if anyone tenses up.",
    ))


def _render_reveal_beside(prs, s: Check, marker, index, total):
    """The reveal with its cards in the left column and the same picture on
    the right, so the answer can be pointed at on it."""
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)
    _chip(slide, MARGIN, Inches(0.55), "ANSWERS", fill=GREEN,
          text_color=WHITE, width=Inches(1.35))
    frame = _textbox(slide, MARGIN + Inches(1.6), Inches(0.57), Inches(8.5),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=GREEN, bold=True, first=True)

    inner_in = s.text_w - 0.6
    refs = {m.number: m.rgb for m in s.picture.marks} or None

    def card_heights(stem_pt, ans_pt, reason_pt):
        return [0.80 + _text_height(f"Q1   {q.stem}", inner_in, stem_pt)
                + _text_height(f"{q.answer}.  "
                               f"{q.options['ABCD'.index(q.answer)]}",
                               inner_in, ans_pt, "mono")
                + _text_height(q.reason, inner_in, reason_pt)
                for q in s.questions]

    for stem_pt, ans_pt, reason_pt in ((17.0, 20.0, 17.0), (17.0, 18.0, 17.0)):
        heights = card_heights(stem_pt, ans_pt, reason_pt)
        if sum(heights) + 0.2 <= BESIDE_BOTTOM - BESIDE_TOP:
            break

    y = BESIDE_TOP
    for i, (q, card_h) in enumerate(zip(s.questions, heights)):
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        stem_h = _text_height(stem, inner_in, stem_pt)
        ans_h = _text_height(answer, inner_in, ans_pt, "mono")
        _rect(slide, MARGIN, Inches(y), Inches(s.text_w), Inches(card_h),
              WHITE, line=BORDER)
        _rect(slide, MARGIN, Inches(y), Inches(0.1), Inches(card_h), GOLD)
        frame = _textbox(slide, MARGIN + Inches(0.35), Inches(y + 0.2),
                         Inches(inner_in), Inches(stem_h + 0.1))
        _para(frame, stem, size=stem_pt, color=MUTED, first=True,
              line_spacing=1.15)
        frame = _textbox(slide, MARGIN + Inches(0.35),
                         Inches(y + 0.2 + stem_h + 0.2), Inches(inner_in),
                         Inches(card_h - stem_h - 0.4))
        _para(frame, answer, size=ans_pt, color=GREEN, font=MONO_FONT,
              bold=True, first=True, line_spacing=1.15)
        _para(frame, q.reason, size=reason_pt, color=INK, space_before=5,
              line_spacing=1.15, refs=refs)
        y += card_h + 0.2

    _beside_picture(slide, s, reveal=True)
    _progress(slide, marker)
    _notes(slide, s.notes or (
        "Reveal one at a time. Say the reason out loud, not just the letter.",
        "If more than a third of the room missed one, step back and reteach it.",
    ))


def render_closing(prs, s: Closing):
    slide = _blank(prs)
    _ground(slide, GREEN)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.22), GOLD)

    frame = _textbox(slide, MARGIN, Inches(1.5), CONTENT_W, Inches(1.1))
    _para(frame, s.title, size=38, color=WHITE, font=DISPLAY_FONT, first=True,
          line_spacing=1.05)
    _rect(slide, MARGIN, Inches(2.9), Inches(1.6), Pt(3), GOLD)

    frame = _textbox(slide, MARGIN, Inches(3.4), CONTENT_W, Inches(2.4))
    for i, line in enumerate(s.lines):
        _para(frame, line, size=20, color=WHITE, first=(i == 0), space_after=12,
              line_spacing=1.15)

    if s.accent:
        frame = _textbox(slide, MARGIN, SLIDE_H - Inches(1.5), CONTENT_W,
                         Inches(0.7))
        _para(frame, s.accent, size=18, color=GOLD, bold=True, first=True)

    _notes(slide, s.notes)



# --------------------------------------------------------------------------
# A check and its reveal under a strip picture, the questions side by side.
# --------------------------------------------------------------------------

# The question sizes a check under a strip steps through, largest first: the
# check's own sizes first, never below the deck's seventeen point stem.
_TOP_SIZES = ((17.0, 15.0), (17.0, 14.0))
_TOP_REVEAL_SIZES = ((16.0, 20.0, 16.0), (15.0, 18.0, 15.0),
                     (14.0, 17.0, 14.0))
TOP_PICTURE_TOP = 1.08
# The least height the strip keeps for the picture and its credit line.
TOP_PICTURE_MIN = 1.9
TOP_GAP = 0.12
# Where the cards under a strip end: lower than a beside check's, still
# clear of the progress marker, so the strip gets the room.
TOP_BOTTOM = 6.55


def _top_picture(slide, s: Check, bottom):
    """The picture across the top, fitted between the chip and ``bottom``,
    with its credit line under it."""
    _pair_picture(slide, s.picture, MARGIN.inches, TOP_PICTURE_TOP,
                  CONTENT_W.inches, bottom - TOP_PICTURE_TOP - 0.28)


def _render_check_top(prs, s: Check, marker, index, total):
    """The question slide with the picture as a strip across the top and the
    two questions side by side below it."""
    slide = _blank(prs)
    _ground(slide, GREEN_DEEP)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)
    _chip(slide, MARGIN, Inches(0.55), f"CHECK {index} OF {total}", fill=GOLD,
          text_color=INK, width=Inches(1.85))
    frame = _textbox(slide, MARGIN + Inches(2.1), Inches(0.57), Inches(8.0),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=WHITE, bold=True, first=True)

    col_w = Emu(int((CONTENT_W - Inches(0.7)) / 2))
    inner_in = col_w.inches - 0.6
    floor = TOP_BOTTOM - TOP_PICTURE_TOP - TOP_PICTURE_MIN - TOP_GAP

    for stem_pt, opt_pt in _TOP_SIZES:
        # Measured as rendered: a line of Arial is about 1.2 times its size,
        # times the 1.12 line spacing the options are set at.
        tallest_stem = max(_text_height(q.stem, inner_in, stem_pt, "bold",
                                        spacing=1.15 * 1.2)
                           for q in s.questions)
        card_h = max(0.52 + tallest_stem + 0.18
                     + sum(_text_height(f"D.  {o}", inner_in, opt_pt,
                                        spacing=1.12 * 1.2) + 6 / 72
                           for o in q.options) + 0.2
                     for q in s.questions)
        if card_h <= floor:
            break

    card_top = TOP_BOTTOM - card_h
    _top_picture(slide, s, card_top - TOP_GAP)

    for i, q in enumerate(s.questions):
        x = MARGIN + (col_w + Inches(0.7)) * i
        _rect(slide, x, Inches(card_top), col_w, Inches(card_h), GREEN)
        frame = _textbox(slide, x + Inches(0.3), Inches(card_top + 0.22),
                         col_w - Inches(0.6), Inches(0.25))
        _para(frame, f"Q{i + 1}", size=12, color=GOLD, bold=True, first=True)
        stem_top = card_top + 0.52
        stem_h = _text_height(q.stem, inner_in, stem_pt, "bold",
                              spacing=1.15 * 1.2)
        frame = _textbox(slide, x + Inches(0.3), Inches(stem_top),
                         col_w - Inches(0.6), Inches(stem_h + 0.1))
        _para(frame, q.stem, size=stem_pt, color=WHITE, bold=True, first=True,
              line_spacing=1.15)
        frame = _textbox(slide, x + Inches(0.3),
                         Inches(stem_top + tallest_stem + 0.18),
                         col_w - Inches(0.6), Inches(3.2))
        for j, opt in enumerate(q.options):
            _para(frame, f"{'ABCD'[j]}.  {opt}", size=opt_pt, color=WHITE,
                  first=(j == 0), space_after=6, line_spacing=1.12)

    _progress(slide, marker, on_dark=True)
    _notes(slide, s.notes or (
        "Read Q1 aloud, then Q2. Give them sixty seconds and no discussion.",
        "Ask for a show of hands on each option before you advance.",
        "This is for reading the room, not for marks. Say so if anyone tenses up.",
    ))


def _render_reveal_top(prs, s: Check, marker, index, total):
    """The reveal under the same strip, its two cards side by side."""
    slide = _blank(prs)
    _ground(slide, PAPER)
    _rect(slide, 0, 0, SLIDE_W, Inches(0.16), GOLD)
    _chip(slide, MARGIN, Inches(0.55), "ANSWERS", fill=GREEN,
          text_color=WHITE, width=Inches(1.35))
    frame = _textbox(slide, MARGIN + Inches(1.6), Inches(0.57), Inches(8.5),
                     Inches(0.4))
    _para(frame, s.label, size=15, color=GREEN, bold=True, first=True)

    col_w = Emu(int((CONTENT_W - Inches(0.5)) / 2))
    inner_in = col_w.inches - 0.6
    refs = {m.number: m.rgb for m in s.picture.marks} or None
    floor = TOP_BOTTOM - TOP_PICTURE_TOP - TOP_PICTURE_MIN - TOP_GAP

    for stem_pt, ans_pt, reason_pt in _TOP_REVEAL_SIZES:
        card_h = max(0.62 + _text_height(f"Q1   {q.stem}", inner_in, stem_pt)
                     + _text_height(f"{q.answer}.  "
                                    f"{q.options['ABCD'.index(q.answer)]}",
                                    inner_in, ans_pt, "mono")
                     + _text_height(q.reason, inner_in, reason_pt)
                     for q in s.questions)
        if card_h <= floor:
            break

    card_top = TOP_BOTTOM - card_h
    _top_picture(slide, s, card_top - TOP_GAP)

    for i, q in enumerate(s.questions):
        x = MARGIN + (col_w + Inches(0.5)) * i
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        stem_h = _text_height(stem, inner_in, stem_pt)
        _rect(slide, x, Inches(card_top), col_w, Inches(card_h), WHITE,
              line=BORDER)
        _rect(slide, x, Inches(card_top), Inches(0.1), Inches(card_h), GOLD)
        frame = _textbox(slide, x + Inches(0.35), Inches(card_top + 0.2),
                         Inches(inner_in), Inches(stem_h + 0.1))
        _para(frame, stem, size=stem_pt, color=MUTED, first=True,
              line_spacing=1.15)
        frame = _textbox(slide, x + Inches(0.35),
                         Inches(card_top + 0.2 + stem_h + 0.18),
                         Inches(inner_in), Inches(card_h - stem_h - 0.4))
        _para(frame, answer, size=ans_pt, color=GREEN, font=MONO_FONT,
              bold=True, first=True, line_spacing=1.15)
        _para(frame, q.reason, size=reason_pt, color=INK, space_before=5,
              line_spacing=1.15, refs=refs)

    _progress(slide, marker)
    _notes(slide, s.notes or (
        "Reveal one at a time. Say the reason out loud, not just the letter.",
        "If more than a third of the room missed one, step back and reteach it.",
    ))

# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

MAX_BODY_LINES = 6

# The cut tiers the teaching plan triages every slide into. deckkit does not
# use them to draw anything; it only refuses a chart that claims one that
# does not exist, so the plan's ladder and the deck cannot disagree.
TIERS = ("core", "reinforcement", "enrichment")

# Nothing may be drawn below this line: the progress marker sits at 6.78in.
SAFE_BOTTOM = 6.50


def _content_bottom(s: Content) -> float:
    """Where render_content will finish drawing, in inches."""
    inner = CONTENT_W.inches
    y = 2.15
    if s.lines:
        y += sum(_text_height(line, inner, 21, spacing=1.18) + 0.20
                 for line in s.lines) + 0.34
    if s.accent:
        y += _text_height(s.accent, inner - 0.32, 22, "bold") + 0.16 + 0.26
    if s.caption:
        y += _text_height(s.caption, inner, 15)
    return y


def _term_bottom(s: Term) -> float:
    """Where render_term will finish drawing, in inches, at the smallest
    body size it is allowed to fall back to."""
    inner = CONTENT_W.inches - 0.3
    rows = ((s.plain, True), (s.example, False), (s.formal, False))
    for pt in (19.0, 18.0, 17.0, 16.0, 15.0, 14.0):
        total = sum(0.42 + _text_height(text, inner, pt,
                                        "bold" if emph else "regular") + 0.24
                    for text, emph in rows if text)
        if total <= 4.1 or pt == 14.0:
            return 2.42 + total
    return 2.42


def _quote_bottom(s: Quote) -> float:
    inner = CONTENT_W.inches - 0.42
    quote_h = _text_height('"' + s.text + '"', inner, 25, spacing=1.2)
    source_h = _text_height(s.source, inner, 14) + 0.2
    top = 1.5 + quote_h + source_h + 0.55
    return top + 0.3 + _text_height(s.takeaway, CONTENT_W.inches, 21, "bold")


def _chart_letter(letter: str) -> bool:
    """A chart is lettered A to Z, and a chapter that draws a twenty seventh
    goes on to AA, AB, the way a spreadsheet's columns do."""
    return (1 <= len(letter) <= 2 and letter.isascii() and letter.isalpha()
            and letter.isupper())


def _validate(chapter: Chapter) -> list[str]:
    """Enforce the teaching brief's hard rules at build time, so a future
    chapter cannot quietly regress them."""
    problems: list[str] = []
    placed = {picture.filename for picture in _pictures(chapter)}

    def check_text(where: str, text: str):
        if "—" in text or "–" in text:
            problems.append(f"{where}: dash character not allowed, use a plain dash")

    def walk(where, slide):
        for value in vars(slide).values():
            if isinstance(value, str):
                check_text(where, value)
            elif isinstance(value, (tuple, list)):
                for item in value:
                    if isinstance(item, str):
                        check_text(where, item)

    def check_origin(where, slide):
        text = slide.origin
        width = CONTENT_W.inches - ORIGIN_X - 0.2
        if text and _line_count(text, width, ORIGIN_PT) > ORIGIN_MAX_LINES:
            problems.append(f"{where}: the origin line runs past "
                            f"{ORIGIN_MAX_LINES} lines")

    def check_frame_slide(where, slide):
        """A chapter's own opening slide: the rules a section slide obeys."""
        if not isinstance(slide, Content):
            problems.append(f"{where}: an opening slide must be a Content slide")
            return
        walk(where, slide)
        if len(slide.lines) > MAX_BODY_LINES:
            problems.append(
                f"{where}: {len(slide.lines)} body lines, limit is {MAX_BODY_LINES}"
            )
        bottom = _content_bottom(slide)
        if bottom > SAFE_BOTTOM:
            problems.append(
                f"{where}: content runs to {bottom:.2f}in, past the "
                f"{SAFE_BOTTOM}in safe bottom. Split the slide or shorten it."
            )
        if not 2 <= len(slide.notes) <= 3:
            problems.append(f"{where}: keep speaker cues to two or three lines")

    def check_marks(where, picture):
        numbers = [m.number for m in picture.marks]
        if len(set(numbers)) != len(numbers):
            problems.append(f"{where}: two marks share a number")
        for m in picture.marks:
            if m.kind not in MARK_KINDS:
                problems.append(f"{where}: mark {m.number} is a {m.kind!r}, "
                                f"not one of {MARK_KINDS}")
            if m.color and m.color not in MARK_COLORS:
                problems.append(f"{where}: mark {m.number} colour "
                                f"{m.color!r} is not in MARK_COLORS")
            if not 1 <= m.number <= 9:
                problems.append(f"{where}: mark numbers run 1 to 9")
            points = (m.x0, m.y0, m.x1, m.y1) + tuple(m.at or ())
            if not all(0.0 <= f <= 1.0 for f in points):
                problems.append(f"{where}: mark {m.number} reaches outside "
                                "its picture; fractions run 0 to 1")
        if picture.crop and (len(picture.crop) != 4
                             or not all(0.0 <= f < 0.9 for f in picture.crop)
                             or picture.crop[0] + picture.crop[2] >= 0.9
                             or picture.crop[1] + picture.crop[3] >= 0.9):
            problems.append(f"{where}: a crop is four fractions, left, top, "
                            "right, bottom, leaving at least a tenth shown")
        if picture.crop and isinstance(picture, Figure) and not picture.aspect:
            problems.append(f"{where}: a cropped figure declares its aspect")
        if picture.marks and isinstance(picture, Figure) and not picture.aspect:
            problems.append(
                f"{where}: figure {picture.number} carries marks, so it "
                "declares its aspect, or the placeholder build puts them "
                "somewhere else")

    def check_pair(where, slide):
        left, picture = slide.left, slide.picture
        if not isinstance(left, (Content, Term)):
            problems.append(f"{where}: a pair's left side is a Content or a Term")
            return
        if not isinstance(picture, (Figure, Chart)):
            problems.append(f"{where}: a pair's picture is a Figure or a Chart")
            return
        walk(where, left)
        walk(where, picture)
        check_marks(where, picture)
        if isinstance(left, Content) and len(left.lines) > MAX_BODY_LINES:
            problems.append(
                f"{where}: {len(left.lines)} body lines, limit is {MAX_BODY_LINES}"
            )
        if not picture.shows:
            problems.append(
                f"{where}: the picture needs a 'shows' line, which is what "
                "the placeholder prints without the artwork"
            )
        if isinstance(picture, Figure) and (not picture.number
                                            or "." not in picture.number):
            problems.append(f"{where}: a figure needs a book figure number")
        if isinstance(picture, Chart) and not _chart_letter(picture.letter):
            problems.append(
                f"{where}: a chart is lettered in its own namespace, one "
                f"capital letter, or two after Z, not {picture.letter!r}"
            )
        if not 3.5 <= slide.text_w <= 8.0:
            problems.append(
                f"{where}: text_w is {slide.text_w}in; keep the text column "
                "between 3.5in and 8.0in so both columns stay readable"
            )
            return
        size, bottom = _pair_fit(slide)
        if bottom > SAFE_BOTTOM:
            problems.append(
                f"{where}: the text column runs to {bottom:.2f}in at "
                f"{size:.0f}pt, its smallest size, past the {SAFE_BOTTOM}in "
                "safe bottom. Shorten it, widen text_w, or split the slide."
            )

    for i, slide in enumerate(chapter.openers or ()):
        check_frame_slide(f"opening slide {i + 1}", slide)
        check_origin(f"opening slide {i + 1}", slide)
    for cue in chapter.title_notes:
        check_text("title slide cues", cue)

    for section in chapter.sections:
        for i, slide in enumerate(section.slides):
            where = f"section {section.number} slide {i + 1}"
            walk(where, slide)
            check_origin(where, slide)
            if isinstance(slide, Pair):
                check_pair(where, slide)
            if isinstance(slide, Content) and len(slide.lines) > MAX_BODY_LINES:
                problems.append(
                    f"{where}: {len(slide.lines)} body lines, limit is {MAX_BODY_LINES}"
                )
            if isinstance(slide, (Figure, Chart)):
                check_marks(where, slide)
            if isinstance(slide, Figure):
                if not slide.number or "." not in slide.number:
                    problems.append(f"{where}: a figure needs a book figure number")
                if not slide.shows:
                    problems.append(
                        f"{where}: figure {slide.number} needs a 'shows' line, "
                        "which is what the placeholder prints without the artwork"
                    )
            if isinstance(slide, Chart):
                if not _chart_letter(slide.letter):
                    problems.append(
                        f"{where}: a chart is lettered in its own namespace, "
                        f"one capital letter, or two after Z, not "
                        f"{slide.letter!r}. Book "
                        "figure numbers belong to Figure."
                    )
                if not slide.shows:
                    problems.append(
                        f"{where}: chart {slide.letter} needs a 'shows' line, "
                        "which is what the lecture notes reuse"
                    )
                if slide.tier not in TIERS:
                    problems.append(
                        f"{where}: chart {slide.letter} has tier "
                        f"{slide.tier!r}; the teaching plan can only cut a "
                        "slide it can name, so use one of "
                        + ", ".join(TIERS)
                    )
            if isinstance(slide, Check):
                if len(slide.questions) != 2:
                    problems.append(f"{where}: a check must hold exactly 2 questions")
                for q in slide.questions:
                    walk(where, q)
                    if len(q.options) != 4:
                        problems.append(f"{where}: every question needs 4 options")
                    if q.answer not in "ABCD":
                        problems.append(f"{where}: answer must be A, B, C or D")
                if slide.picture is not None:
                    if not isinstance(slide.picture, (Figure, Chart)):
                        problems.append(f"{where}: a check's picture is a "
                                        "Figure or a Chart")
                    elif slide.picture.filename not in placed:
                        problems.append(
                            f"{where}: a check's picture must be one a "
                            "teaching slide places, or the student edition "
                            "loses it")
                    else:
                        check_marks(where, slide.picture)
                    if slide.layout not in CHECK_LAYOUTS:
                        problems.append(f"{where}: a check's layout is one "
                                        f"of {CHECK_LAYOUTS}")
                    if not 4.5 <= slide.text_w <= 8.0:
                        problems.append(f"{where}: a check's text_w runs "
                                        "4.5in to 8.0in")
            bottom = None
            if isinstance(slide, Content):
                bottom = _content_bottom(slide)
            elif isinstance(slide, Term):
                bottom = _term_bottom(slide)
            elif isinstance(slide, Quote):
                bottom = _quote_bottom(slide)
            if bottom is not None and bottom > SAFE_BOTTOM:
                problems.append(
                    f"{where}: content runs to {bottom:.2f}in, past the "
                    f"{SAFE_BOTTOM}in safe bottom. Split the slide or shorten it."
                )
            if not isinstance(slide, Check) and not slide.notes:
                problems.append(f"{where}: content slides need speaker cues")
            if slide.notes and len(slide.notes) > 3:
                problems.append(f"{where}: keep speaker cues to two or three lines")
        if section.recap is not None:
            walk(f"section {section.number} recap", section.recap)

    letters_used = [slide.letter for slide in _pictures(chapter)
                    if isinstance(slide, Chart)]
    for letter in sorted({x for x in letters_used if letters_used.count(x) > 1}):
        problems.append(
            f"chart {letter} is used on more than one slide; the letters are "
            "the chart's name and the lecture notes resolve them"
        )

    # Answer positions must be spread across A/B/C/D. A skewed key lets a
    # student score well by always picking one letter, which destroys the
    # only thing the checks are for: reading the room.
    letters = [q.answer
               for section in chapter.sections
               for slide in section.slides if isinstance(slide, Check)
               for q in slide.questions]
    if letters:
        for L in "ABCD":
            share = letters.count(L) / len(letters)
            if share > 0.35:
                problems.append(
                    f"answer key: {L} holds {share:.0%} of {len(letters)} items, "
                    "limit is 35%. Reorder options to spread the key."
                )
            elif share < 0.15:
                problems.append(
                    f"answer key: {L} holds only {share:.0%} of {len(letters)} "
                    "items, floor is 15%. Reorder options to spread the key."
                )
        runs = [i for i in range(len(letters) - 2)
                if letters[i] == letters[i + 1] == letters[i + 2]]
        if runs:
            problems.append(
                f"answer key: {len(runs)} run(s) of three identical answers in a "
                "row, starting at item(s) "
                + ", ".join(str(i + 1) for i in runs) + "."
            )
    return problems


def build(chapter: Chapter, out_path, *, display_font: str | None = None,
          figures_dir=None, charts_dir=None, edition: str = TEACHING):
    """Render the chapter to a .pptx. Deterministic: same input, same deck.

    ``figures_dir`` is where render_figure looks for the textbook artwork. Pass
    None, or a path that does not exist, and every figure slide renders as a
    placeholder instead. The slide count and the progress markers are the same
    either way.

    ``charts_dir`` is where render_chart looks for the charts this course
    draws itself. Those are ours and are generated from code in this
    repository, so the caller draws them first and passes the folder here;
    unlike the figures they are expected to be present in every build.

    ``edition`` is TEACHING or STUDENT. The student edition drops every check
    slide and its reveal, and carries no speaker cues. See the Editions block
    at the top of this file.

    Returns ``(slide_count, checks_rendered)``. ``checks_rendered`` is 0 for
    the student edition, which is the number the caller should report.
    """
    global DISPLAY_FONT, FIGURES_DIR, CHARTS_DIR, INCLUDE_NOTES
    if edition not in EDITIONS:
        raise ValueError(f"unknown edition {edition!r}, expected one of "
                         + ", ".join(EDITIONS))
    if display_font:
        DISPLAY_FONT = display_font
    FIGURES_DIR = Path(figures_dir) if figures_dir else None
    CHARTS_DIR = Path(charts_dir) if charts_dir else None
    INCLUDE_NOTES = edition == TEACHING
    with_checks = edition == TEACHING

    problems = _validate(chapter)
    if problems:
        raise SystemExit(
            "Teaching design rules violated:\n  " + "\n  ".join(problems)
        )

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # Fixed document properties keep the build byte-for-byte reproducible, so
    # rebuilding an unchanged chapter produces no diff.
    core = prs.core_properties
    core.title = f"{chapter.code} {chapter.chapter} - {chapter.title}"
    core.author = chapter.presenter
    core.last_modified_by = chapter.presenter
    core.subject = chapter.course
    core.revision = 1
    core.created = EPOCH
    core.modified = EPOCH

    total_sections = len(chapter.sections)
    checks: list[tuple[int, Check]] = []
    for section in chapter.sections:
        for slide in section.slides:
            if isinstance(slide, Check):
                checks.append((section.number, slide))
    total_checks = len(checks)

    render_title(prs, TitleSlide(
        course=f"{chapter.code}  {chapter.course}",
        chapter=chapter.chapter,
        title=chapter.title,
        subtitle=chapter.subtitle,
        presenter=chapter.presenter,
        notes=chapter.title_notes or (
            "Greet the room, then say what today buys them: after this session "
            "they can read a chart argument and say what it does and does not claim.",
            "Point at the roadmap slide next and promise a clean stopping point "
            "every twenty five minutes.",
        ),
    ))

    # A chapter that brings its own opening slides gets exactly those. The
    # generated frame below is what every chapter without them has always had.
    for slide in chapter.openers or ():
        render_content(prs, slide, marker=f"{chapter.chapter} - Opening")
        _origin(prs, slide)

    if chapter.openers is None:
        # The booklet lists seven objectives, which is more than one slide should
        # carry, so they are split rather than crammed.
        objective_chunks = [chapter.objectives[i:i + 4]
                            for i in range(0, len(chapter.objectives), 4)]
        for n, chunk in enumerate(objective_chunks):
            render_content(prs, Content(
                title="What you will be able to do" if n == 0 else "What you will be able to do, continued",
                lines=chunk,
                notes=(
                    "Read these out once, slowly. These are the exact learning "
                    "objectives in the course booklet for this week.",
                    "Tell them every one of these is examinable.",
                ),
            ), marker=f"{chapter.chapter} - Learning objectives")

        render_content(prs, Content(
            title="How today is laid out",
            lines=chapter.roadmap,
            # The only line in the generated frame that names the checks. The
            # student edition has none, so it says what is left that is true.
            accent=("Six parts, a check every few terms, and a clean stop at "
                    "every boundary." if with_checks else
                    "Six parts, and a clean stop at every boundary."),
            notes=(
                "Say the shape of the session out loud: six parts, roughly twenty "
                "five minutes each.",
                "Tell them the checks are for reading the room, not for marks.",
            ),
        ), marker=f"{chapter.chapter} - Roadmap")

    check_index = 0
    for section in chapter.sections:
        if chapter.dividers:
            render_section_open(prs, SectionOpen(
                number=section.number,
                total=total_sections,
                title=section.title,
                covers=section.covers,
                minutes=section.minutes,
                notes=(
                    f"Say we are starting Part {section.number} of {total_sections}.",
                    "Read the three covers lines, then move. Do not linger here.",
                ),
            ))

        # The marker denominator has always counted the body of the section,
        # never the checks, so it is computed here from the slides this
        # edition renders rather than being carried across from the other one.
        position = 0
        body = [s for s in section.slides if not isinstance(s, Check)]
        for slide in section.slides:
            if isinstance(slide, Check):
                if not with_checks:
                    continue
                check_index += 1
                marker = (f"Part {section.number} of {total_sections} - "
                          f"{section.short}  |  Check {check_index}")
                render_check(prs, slide, marker, check_index, total_checks)
                render_reveal(prs, slide, marker, check_index, total_checks)
                continue
            position += 1
            marker = (f"Part {section.number} of {total_sections} - "
                      f"{section.short}  |  {position} of {len(body)}")
            if isinstance(slide, Term):
                render_term(prs, slide, marker)
            elif isinstance(slide, Quote):
                render_quote(prs, slide, marker)
            elif isinstance(slide, Content):
                render_content(prs, slide, marker)
            elif isinstance(slide, Figure):
                render_figure(prs, slide, marker)
            elif isinstance(slide, Chart):
                render_chart(prs, slide, marker)
            elif isinstance(slide, Pair):
                render_pair(prs, slide, marker)
            else:
                raise TypeError(f"unhandled slide type {type(slide).__name__}")
            _origin(prs, slide)

        if section.recap is not None:
            render_recap(prs, section.recap,
                         marker=(f"Part {section.number} of {total_sections} - "
                                 f"{section.short}  |  recap"))

    for slide in chapter.closing:
        if isinstance(slide, Closing):
            render_closing(prs, slide)
        elif isinstance(slide, Content):
            render_content(prs, slide, marker=f"{chapter.chapter} - Wrap up")
        elif isinstance(slide, Pair):
            render_pair(prs, slide, marker=f"{chapter.chapter} - Wrap up")
        else:
            raise TypeError(f"unhandled closing slide {type(slide).__name__}")
        _origin(prs, slide)

    prs.save(str(out_path))
    _repack_deterministically(out_path)
    return len(prs.slides._sldIdLst), (total_checks if with_checks else 0)


def _pictures(chapter: Chapter):
    """Every Figure and Chart the chapter places, in reading order, whether
    it has a slide of its own or sits in a Pair."""
    slides = [s for section in chapter.sections for s in section.slides]
    for slide in [*slides, *chapter.closing]:
        if isinstance(slide, Pair):
            slide = slide.picture
        if isinstance(slide, (Figure, Chart)):
            yield slide


def figure_status(chapter: Chapter, figures_dir=None):
    """Every figure the chapter declares, and whether its artwork is present."""
    root = Path(figures_dir) if figures_dir else None
    out = []
    for slide in _pictures(chapter):
        if isinstance(slide, Figure):
            have = root is not None and (root / slide.filename).is_file()
            out.append((slide.number, slide.filename, have))
    return out


def chart_status(chapter: Chapter, charts_dir=None):
    """Every chart the chapter declares, and whether its artwork is present."""
    root = Path(charts_dir) if charts_dir else None
    out = []
    for slide in _pictures(chapter):
        if isinstance(slide, Chart):
            have = root is not None and (root / slide.filename).is_file()
            out.append((slide.letter, slide.filename, have))
    return out


def _repack_deterministically(path) -> None:
    """Rewrite the .pptx zip with a stable entry order and a fixed timestamp.

    python-pptx does not guarantee a stable order for the package parts, so
    two builds of identical content can differ byte for byte. That produces
    noisy diffs on a generated file that is committed. Repacking fixes it.
    """
    path = str(path)
    with zipfile.ZipFile(path) as src:
        entries = {name: src.read(name) for name in src.namelist()}

    # [Content_Types].xml conventionally comes first; the rest sort by name.
    first = "[Content_Types].xml"
    names = ([first] if first in entries else []) + sorted(
        n for n in entries if n != first)

    tmp = path + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for name in names:
            info = zipfile.ZipInfo(name, date_time=EPOCH.timetuple()[:6])
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            dst.writestr(info, entries[name])
    os.replace(tmp, path)


def iter_checks(chapter: Chapter):
    """Every check in reading order, for the instructor's answer sheet."""
    index = 0
    for section in chapter.sections:
        for slide in section.slides:
            if isinstance(slide, Check):
                index += 1
                yield index, section, slide
