"""Chapter 8 reuses Chapter 7's measured chart layout unchanged.

Importing this module points that layout at Chapter 8's chart data, content
and figure sizes, then re-exports the pieces a content file uses. Nothing is
copied: badge placement, label lanes and the machine checks are Chapter 7's.
"""
import chartlayout_chapter07 as _layout

_layout.CHAPTER_DIR = 'chapter-08'
_layout.DATA_MODULE = 'charts_chapter08'
_layout.CONTENT_MODULE = 'content_chapter08'
# Chapter 7's layout caches nothing before this point, but clear it anyway.
_layout.layout.cache_clear()

from chartlayout_chapter07 import (CourseCheck, CourseFigureCheck, WidePair,  # noqa: E402,F401
                                   artwork, audit_pptx, book_crop, chart_slides,
                                   course_chart, course_slide_renderer,
                                   expand_chart_pages)

# Chapter 8's checks give their figure about half the slide (Chapter 7's column is 3.3 inches).

# One typeface for every answer line in this chapter: the plain check's answer
# slide would otherwise set its answer in Courier and the figure check's in Arial.
import deckkit as _dk  # noqa: E402
_dk.MONO_FONT = _dk.BODY_FONT


# A check whose figure takes the right half of the slide: the two questions
# are stacked in a column on the left, each at 17 point, and the figure gets
# at least six inches. Chapter 7's form puts two narrow cards beside a narrow
# figure; this one is for a figure the questions have to be read against.
from dataclasses import dataclass as _dataclass  # noqa: E402
from contextlib import contextmanager as _contextmanager  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
from pptx.util import Inches as _In  # noqa: E402


@_dataclass
class StackedFigureCheck(_layout.CourseFigureCheck):
    """A figure check with the questions stacked beside a large figure."""


def _stacked_check(prs, s, marker, index, total):
    dk = _dk
    slide = dk._blank(prs)
    dk._ground(slide, dk.GREEN_DEEP)
    dk._rect(slide, 0, 0, dk.SLIDE_W, _In(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, _In(0.55), f"CHECK {index} OF {total}",
             fill=dk.GOLD, text_color=dk.INK, width=_In(1.85))
    frame = dk._textbox(slide, dk.MARGIN + _In(2.1), _In(0.57), _In(8.0), _In(0.4))
    dk._para(frame, s.label, size=17, color=dk.WHITE, bold=True, first=True)
    refs = {m.number: dk.GOLD for m in s.picture.marks}
    inner = s.text_w - 0.6
    top, gap, card_h = 1.05, 0.1, 2.65
    for i, q in enumerate(s.questions):
        y = top + i * (card_h + gap)
        # Real Arial line counts, as Chapter 7's answer slide measures them.
        stem_h = _layout._arial_lines(q.stem, inner, 17, 'bold') * 17 * 1.15 * 1.1 / 72
        opts = [_layout._arial_lines(f"D.  {o}", inner, 17) * 17 * 1.1 / 72 + 0.07 for o in q.options]
        assert 0.42 + stem_h + 0.12 + sum(opts) <= card_h - 0.05, (s.label, 'check text does not fit at 17 point')
        dk._rect(slide, dk.MARGIN, _In(y), _In(s.text_w), _In(card_h), dk.GREEN)
        frame = dk._textbox(slide, dk.MARGIN + _In(0.3), _In(y + 0.15), _In(inner), _In(0.25))
        dk._para(frame, f"Q{i + 1}", size=12, color=dk.GOLD, bold=True, first=True)
        frame = dk._textbox(slide, dk.MARGIN + _In(0.3), _In(y + 0.42), _In(inner), _In(stem_h + 0.1))
        dk._para(frame, q.stem, size=17, color=dk.WHITE, bold=True, first=True, line_spacing=1.15, refs=refs)
        frame = dk._textbox(slide, dk.MARGIN + _In(0.3), _In(y + 0.42 + stem_h + 0.12), _In(inner), _In(1.6))
        for j, option in enumerate(q.options):
            dk._para(frame, f"{'ABCD'[j]}.  {option}", size=17, color=dk.WHITE,
                     first=(j == 0), space_after=3, line_spacing=1.1)
    # The figure: right of the questions, as large as the column allows.
    picture = s.picture
    path = None if dk.FIGURES_DIR is None else _Path(dk.FIGURES_DIR) / picture.filename
    x0 = dk.MARGIN.inches + s.text_w + 0.35
    width, height = dk.MARGIN.inches + dk.CONTENT_W.inches - x0, 6.4 - top
    px_w, px_h = dk._picture_size(picture, path) or (picture.aspect * 1000.0, 1000.0)
    scale = min(width / px_w, height / px_h)
    pic_w, pic_h = px_w * scale, px_h * scale
    pic_x = x0 + (width - pic_w) / 2
    dk._rect(slide, _In(pic_x - .04), _In(top - .04), _In(pic_w + .08), _In(pic_h + .08), dk.WHITE, line=dk.BORDER)
    if path is not None and path.is_file():
        dk._add_picture(slide, picture, path, pic_x, top, pic_w, pic_h)
    else:
        dk._placeholder_plate(slide, picture, pic_x, top, pic_w, pic_h)
    dk._draw_marks(slide, picture.marks, pic_x, top, pic_w, pic_h)
    frame = dk._textbox(slide, _In(pic_x), _In(top + pic_h + .1), _In(pic_w), _In(.3))
    dk._para(frame, picture.credit, size=11, color=dk.WHITE, first=True)
    dk._progress(slide, marker, on_dark=True)
    dk._notes(slide, s.notes)


@_contextmanager
def course_slide_renderer():  # noqa: F811
    """Chapter 7's renderer, plus the stacked figure check."""
    with _layout.course_slide_renderer():
        original_check = _dk.render_check

        def check(prs, s, marker, index, total):
            if isinstance(s, StackedFigureCheck):
                return _stacked_check(prs, s, marker, index, total)
            return original_check(prs, s, marker, index, total)

        _dk.render_check = check
        original_pair = _dk.render_pair

        def pair(prs, s, marker):
            if isinstance(s, TopPair):
                return _top_pair(prs, s, marker)
            return original_pair(prs, s, marker)

        _dk.render_pair = pair
        try:
            yield
        finally:
            _dk.render_pair = original_pair
            _dk.render_check = original_check


# Tables are not charts of invented data: their credit says what they are made from.
_TABLES = {'AS': 'FIN1209 table, from Lim\'s lists (pp. 239 to 240).',
           'AW': 'FIN1209 table, from Lim\'s four definitions (pp. 246 to 247).',
           'AX': 'FIN1209 table: examples from the slides of this class, our charts and Lim\'s figures.',
           'BA': "FIN1209 table, from Lim's three formulas (p. 252).", 'BC': "FIN1209 table, from the book's own numbers (p. 253).",
           'BE': "FIN1209 table: the book's method (p. 253), worked on our numbers.", 'BF': "FIN1209 table, worked by the book's method (p. 253).",
           'BH': "FIN1209 table, from Lim's list (p. 253)."}
_orig_credit = CourseChart_credit = _layout.CourseChart.credit


def _credit(self):
    return _TABLES.get(self.display_letter) or _orig_credit.fget(self)


_layout.CourseChart.credit = property(_credit)


# A wide book figure under four lines of text, the way a course chart sits under its text. A figure
# wider than about two to one is drawn at the full width of the slide this way; beside a text column it
# came out a third of the height of the slide with the rest empty.
@_dataclass
class TopPair(_layout.WidePair):
    """Text across the top, the figure under it as large as the slide allows."""


TOP_Y, TOP_H = 2.62, 3.8


def _top_pair(prs, s, marker):
    from pathlib import Path
    slide = _dk._blank(prs)
    _dk._ground(slide, _dk.PAPER)
    _dk._rect(slide, 0, 0, _dk.SLIDE_W, _In(.16), _dk.GREEN)
    frame = _dk._textbox(slide, _dk.MARGIN, _In(.42), _dk.CONTENT_W, _In(.84))
    _dk._para(frame, s.left.title, size=28, color=_dk.GREEN, font=_dk.DISPLAY_FONT, first=True, line_spacing=1.0)
    _dk._header_rule(slide, _In(1.25))
    refs = {m.number: m.rgb for m in s.picture.marks}
    text = ' '.join(s.left.lines)
    assert _dk._text_height(text, _dk.CONTENT_W.inches, 17, spacing=1.26) <= _layout.TEXT_H, (s.left.title, 'text runs past four lines')
    frame = _dk._textbox(slide, _dk.MARGIN, _In(1.33), _dk.CONTENT_W, _In(_layout.TEXT_H))
    _dk._para(frame, text, size=17, color=_dk.INK, first=True, line_spacing=1.0, refs=refs)
    picture = s.picture
    root = _dk.FIGURES_DIR if isinstance(picture, _dk.Figure) else _dk.CHARTS_DIR
    path = None if root is None else _Path(root) / picture.filename
    px_w, px_h = _dk._picture_size(picture, path) or (picture.aspect * 1000.0, 1000.0)
    scale = min(_dk.CONTENT_W.inches / px_w, TOP_H / px_h)
    pic_w, pic_h = px_w * scale, px_h * scale
    pic_x = (_dk.SLIDE_W.inches - pic_w) / 2
    _dk._rect(slide, _In(pic_x - .04), _In(TOP_Y - .04), _In(pic_w + .08), _In(pic_h + .08), _dk.WHITE, line=_dk.BORDER)
    if path is not None and path.is_file():
        _dk._add_picture(slide, picture, path, pic_x, TOP_Y, pic_w, pic_h)
    else:
        _dk._placeholder_plate(slide, picture, pic_x, TOP_Y, pic_w, pic_h)
    _dk._draw_marks(slide, picture.marks, pic_x, TOP_Y, pic_w, pic_h)
    frame = _dk._textbox(slide, _In(pic_x), _In(TOP_Y + pic_h + .1), _In(pic_w), _In(.22))
    _dk._para(frame, picture.credit, size=11, color=_dk.MUTED, first=True)
    _dk._progress(slide, marker)
    _dk._notes(slide, s.notes)
