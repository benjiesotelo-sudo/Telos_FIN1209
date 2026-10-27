"""One measured layout for all Chapter 7 course charts.

Prices are data, not layout hints. Every OHLC label uses its real data
coordinate. Long sequences are paginated, never squeezed or downscaled.
This chapter-local renderer does not change the shared slide or chart kits.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from contextlib import contextmanager
from functools import lru_cache
import math
import re

from pptx.util import Emu, Inches

import chartkit as ck
import deckkit as dk
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from matplotlib.textpath import TextPath
from matplotlib.transforms import Bbox

WIDTH, HEIGHT = ck.FIG_W, ck.FIG_H
FONT = 16.5
CAPTION = 'Prices and volume are invented for teaching.'
PRICE_CAPTION = 'Prices are invented for teaching.'


@dataclass
class CourseChart(dk.Chart):
    asset: str = ''
    page: int = 0
    display_letter: str = ''
    teaching: tuple[str, ...] = ()
    # A crop of the book's own drawing of the same form, shown beside a
    # narrower chart; the sentences read the chart, whose marks they name.
    figure: dk.Figure | None = None

    @property
    def filename(self):
        return f'chart-{self.asset}-{self.page}.png'

    @property
    def credit(self):
        return dk.chart_credit(self.display_letter)

    @property
    def name(self):
        return f'Chart {self.display_letter}'


def course_chart(asset, **kwargs):
    """Keep displayed owner letters while namespacing conflicting assets."""
    return CourseChart(asset=asset, display_letter=kwargs['letter'], **kwargs)


def book_crop(number, window, shows, marks=(), masks=()):
    """One drawing cut from a book figure: ``window`` is the part kept,
    (left, top, right, bottom) as fractions of the whole figure, measured
    on a gridded render of the artwork."""
    import json
    from pathlib import Path
    sizes = json.loads((Path(__file__).resolve().parents[1] / 'chapter-07' /
                        'figure-sizes.json').read_text())['figures']
    major, minor = number.split('.')
    w, h = sizes[f'figure-{major}-{int(minor):02d}.png']
    x0, y0, x1, y1 = window
    # Marks are written in fractions of the whole figure, as read off the
    # grid, and moved here into fractions of the part shown.
    def fx(x): return (x - x0) / (x1 - x0)
    def fy(y): return (y - y0) / (y1 - y0)
    shown = tuple(replace(m, x0=fx(m.x0), y0=fy(m.y0), x1=fx(m.x1), y1=fy(m.y1),
                          at=None if m.at is None else (fx(m.at[0]), fy(m.at[1])))
                  for m in marks)
    figure = dk.Figure(number=number, shows=shows, aspect=w / h, marks=shown,
                       crop=(x0, y0, 1 - x1, 1 - y1))
    # A neighbouring drawing that no straight cut can exclude is painted
    # over on the slide; (left, top, right, bottom) in whole-figure fractions.
    figure.masks = tuple(masks)
    return figure


def _paint_masks(slide, figure):
    """Cover each mask of a placed book crop with paper-white."""
    masks = getattr(figure, 'masks', ())
    if not masks:
        return
    pictures = [p for p in slide.shapes if p.shape_type == 13]
    if not pictures:
        return
    pic = pictures[-1]
    cl, ct, cr, cb = figure.crop
    for x0, y0, x1, y1 in masks:
        fx = lambda x: (x - cl) / (1 - cl - cr)
        fy = lambda y: (y - ct) / (1 - ct - cb)
        left = pic.left + int(pic.width * max(0, fx(x0)))
        top = pic.top + int(pic.height * max(0, fy(y0)))
        right = pic.left + int(pic.width * min(1, fx(x1)))
        bottom = pic.top + int(pic.height * min(1, fy(y1)))
        dk._rect(slide, left, top, right - left, bottom - top, dk.WHITE)
    # The marks go back on top of the paint.
    dk._draw_marks(slide, figure.marks, pic.left / 914400, pic.top / 914400,
                   pic.width / 914400, pic.height / 914400)


def chart_slides(asset, title, lines, *, figure=None, notes=(), origin=''):
    """A chart's teaching text and the chart, written as the text slide and
    the chart slide that expand_chart_pages folds into one."""
    from charts_chapter07 import DATA
    text = dk.Content(title=title, lines=tuple(lines), notes=tuple(notes), origin=origin)
    chart = course_chart(asset, title=title, letter=DATA[asset]['letter'],
                         shows=DATA[asset]['items'][0].name, tier='core',
                         notes=tuple(notes), origin=origin, figure=figure)
    return text, chart


def page_specs(spec):
    if spec['special']:
        return ((0, 0, 0),)
    result = []
    for cell_index, cell in enumerate(spec['items']):
        count = max(max(len(p.bars), len(p.line), len(p.columns), 1) for p in cell.panes)
        if spec.get('one_page'):
            # A pattern read across all its bars stays on one page; only the
            # bars its sentences read carry price labels (bar_labels).
            result.append((cell_index, 0, count))
            continue
        # Three OHLC bars leave room for both side labels plus a level lane.
        # A four-bar pattern stays whole: its sentences name all four bars.
        step = (4 if count == 4 else 3) if any(p.bars for p in cell.panes) else count
        result.extend((cell_index, start, min(count, start + step)) for start in range(0, count, step))
    return tuple(result)


def artwork(data):
    return tuple(ck.ChartArt(letter=f'{key}-{page}', draw=draw,
                             kwargs=dict(key=key, page=page))
                 for key, spec in data.items()
                 for page in range(len(page_specs(spec))))


TEXT_H = 1.2   # four lines of 17 point teaching text above the chart


def _paragraphs(content):
    """Split each paragraph of a slide at sentence ends, keeping every word."""
    return [re.split(r'(?<=[.!?])\s+(?=[A-Z\[])', value)
            for value in (*content.lines, content.accent, content.caption) if value]


def _refs(sentence):
    return {int(n) for n in re.findall(r'\[(\d+)\]', sentence)}


def _place(asset, paragraphs):
    """Give each chart page the sentences that read it.

    A sentence naming marks goes to the page that carries them. The
    sentences before the first of those introduce the chart, so they open
    its first page and stand on any page no mark falls on. Any other
    sentence stays with a marked sentence earlier in its own paragraph,
    else goes with the next marked sentence, else the last.
    """
    from charts_chapter07 import DATA
    numbers = [{m.number for m in layout(asset, page)[1]}
               for page in range(len(page_specs(DATA[asset])))]
    sentences = [s for paragraph in paragraphs for s in paragraph]
    owner = [i for i, paragraph in enumerate(paragraphs) for _s in paragraph]
    homes = []
    for sentence in sentences:
        refs = _refs(sentence)
        pages = [page for page, have in enumerate(numbers) if refs and refs <= have]
        assert pages or not refs, (asset, 'sentence names marks on no single page', sentence)
        homes.append(pages[0] if pages else None)
    if all(home is None for home in homes):
        return [list(sentences) for _ in numbers]
    first = next(i for i, home in enumerate(homes) if home is not None)
    opening = sentences[:first]
    marked = list(homes)
    for i, home in enumerate(homes):
        if i < first:
            homes[i] = 0
        elif home is None:
            same = [marked[j] for j in range(i) if owner[j] == owner[i] and marked[j] is not None]
            later = [h for h in marked[i:] if h is not None]
            homes[i] = (same[-1] if same else later[0] if later
                        else [h for h in marked[:i] if h is not None][-1])
    placed = [[s for s, home in zip(sentences, homes) if home == page]
              for page in range(len(numbers))]
    return [page or list(opening) for page in placed]


def _chunks(sentences):
    """Split a page's sentences across slides, never shrinking the text."""
    chunks, chunk = [], []
    for sentence in sentences:
        if chunk and dk._text_height(' '.join((*chunk, sentence)), WIDTH, 17, spacing=1.26) > TEXT_H:
            chunks.append(tuple(chunk))
            chunk = []
        chunk.append(sentence)
    if chunk:
        chunks.append(tuple(chunk))
    for chunk in chunks:
        assert dk._text_height(' '.join(chunk), WIDTH, 17, spacing=1.26) <= TEXT_H, chunk
    return chunks


# Look-alike patterns get their own slides (checklist 26); a two-case
# comparison chart takes each page's title from the case it shows.
PAGE_TITLES = {
    'r3a-a': ('An exhaustion bar ends a long run',
              'A pin bar pierces support and then snaps back inside'),
}
CASE_TITLES = ('r3b-le', 'r3b-li')


def _renumber(sentences, marks):
    """Number a look-alike's own slide from 1, in the order its text reads.

    Colours stay with their marks: a leader line drawn into the chart
    carries its mark's colour.
    """
    order = []
    for sentence in sentences:
        order.extend(n for n in map(int, re.findall(r'\[(\d+)\]', sentence)) if n not in order)
    new = {old: i for i, old in enumerate(order, 1)}
    sentences = [re.sub(r'\[(\d+)\]', lambda m: f'[{new[int(m.group(1))]}]', s) for s in sentences]
    return sentences, tuple(replace(mark, number=new[mark.number]) for mark in marks)


def _title_width(title):
    """Inches the chart slide's 28 point Palatino title needs, or 0 when
    the font file is not on this machine."""
    from pathlib import Path
    from PIL import ImageFont
    path = Path('/System/Library/Fonts/Palatino.ttc')
    if not path.is_file():
        return 0.0
    return ImageFont.truetype(str(path), 280).getlength(title) / 10 / 72


def expand_chart_pages(chapter):
    """Put each chart beside the sentences that read it, one page per slide.

    The text slide written in front of a chart is folded onto the chart's
    own slides, so a sentence that names a mark is read where the mark is.
    """
    from charts_chapter07 import DATA
    serial = 0
    def expand(slides):
        nonlocal serial
        result = []
        for index, slide in enumerate(slides):
            following = slides[index + 1] if index + 1 < len(slides) else None
            if isinstance(slide, dk.Content) and isinstance(following, CourseChart):
                continue
            if not isinstance(slide, CourseChart):
                result.append(slide)
                continue
            previous = slides[index - 1] if index else None
            paragraphs = _paragraphs(previous) if isinstance(previous, dk.Content) else [[slide.shows]]
            specs = page_specs(DATA[slide.asset])
            for page, selected in enumerate(_place(slide.asset, paragraphs)):
                assert selected, (slide.asset, page + 1, 'chart page with no sentence')
                title = slide.title
                # The title box has room for one line; a second runs into
                # the teaching text, so the build refuses it.
                assert _title_width(title) <= .98 * dk.CONTENT_W.inches, (slide.asset, 'title wraps', title)
                if slide.asset in PAGE_TITLES:
                    title = PAGE_TITLES[slide.asset][page]
                elif slide.asset in CASE_TITLES:
                    title = DATA[slide.asset]['items'][specs[page][0]].name
                marks = layout(slide.asset, page)[1]
                if slide.asset in PAGE_TITLES or slide.asset in CASE_TITLES:
                    selected, marks = _renumber(selected, marks)
                for chunk in _chunks(selected):
                    internal = chr(65 + serial // 26) + chr(65 + serial % 26)
                    serial += 1
                    shown = marks
                    if DATA[slide.asset].get('marks_by_sentence'):
                        # Each slide carries only the marks its own sentences name.
                        named = set().union(*(_refs(sentence) for sentence in chunk))
                        shown = tuple(m for m in marks if m.number in named)
                    result.append(replace(slide, page=page, letter=internal, title=title,
                                          teaching=chunk, notes=slide.notes or (slide.shows,),
                                          marks=shown))
        return tuple(result)
    openers = expand(chapter.openers or ())
    sections = tuple(replace(section, slides=expand(section.slides)) for section in chapter.sections)
    return replace(chapter, openers=openers, sections=sections, closing=expand(chapter.closing))


def _book_drawing(slide, figure, x, y, w, h):
    """The book's drawing fitted into its column, level with the chart, with
    a one-line credit under the column where the chart's credit sits."""
    from pathlib import Path
    from pptx.util import Inches
    path = None if dk.FIGURES_DIR is None else Path(dk.FIGURES_DIR) / figure.filename
    px_w, px_h = dk._picture_size(figure, path)
    scale = min(w / px_w, h / px_h)
    pic_w, pic_h = px_w * scale, px_h * scale
    pic_x, pic_y = x + (w - pic_w) / 2, y + (h - pic_h) / 2
    dk._rect(slide, Inches(x - .04), Inches(y - .04), Inches(w + .08), Inches(h + .08),
             dk.WHITE, line=dk.BORDER)
    if path is not None and path.is_file():
        dk._add_picture(slide, figure, path, pic_x, pic_y, pic_w, pic_h)
    else:
        dk._placeholder_plate(slide, figure, pic_x, pic_y, pic_w, pic_h)
    dk._draw_marks(slide, figure.marks, pic_x, pic_y, pic_w, pic_h)
    frame = dk._textbox(slide, Inches(x), Inches(6.52), Inches(w), Inches(.22))
    dk._para(frame, f'Figure {figure.number}, Lim (2016)', size=11,
             color=dk.MUTED, first=True)


PADDED_CHECKS = {'The 16 characteristics on Figure 7.13'}
BODY_PT = 17.0   # checklist A10: no body text below 17 point


def _check_fits(s):
    """Whether a plain two-question check fits at 17 point, cards and all."""
    col_in = (dk.CONTENT_W.inches - 0.7) / 2 - 0.6
    question = max(dk._text_height(q.stem, col_in, BODY_PT, "bold")
                   + sum(dk._text_height(f"D.  {o}", col_in, BODY_PT) + 0.15
                         for o in q.options) for q in s.questions)
    inner = dk.CONTENT_W.inches - 0.8
    answer = sum(0.95 + dk._text_height(f"Q1   {q.stem}", inner, BODY_PT)
                 + dk._text_height(f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}",
                                   inner, 18.0, "mono")
                 + dk._text_height(q.reason, inner, BODY_PT) for q in s.questions)
    return question <= 5.02 - 0.95 and answer + 0.27 <= 5.1


def _render_check_17(prs, s, marker, index, total):
    """deckkit's plain check slide, with every run at 17 point or more."""
    from pptx.util import Inches, Emu
    slide = dk._blank(prs)
    dk._ground(slide, dk.GREEN_DEEP)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), f"CHECK {index} OF {total}", fill=dk.GOLD,
             text_color=dk.INK, width=Inches(1.85))
    frame = dk._textbox(slide, dk.MARGIN + Inches(2.1), Inches(0.57), Inches(8.0), Inches(0.4))
    dk._para(frame, s.label, size=15, color=dk.WHITE, bold=True, first=True)
    col_w = Emu(int((dk.CONTENT_W - Inches(0.7)) / 2))
    inner_in = col_w.inches - 0.6
    card_top, card_h = 1.32, 5.02
    tallest = max(dk._text_height(q.stem, inner_in, BODY_PT, "bold") for q in s.questions)
    for i, q in enumerate(s.questions):
        x = dk.MARGIN + (col_w + Inches(0.7)) * i
        dk._rect(slide, x, Inches(card_top), col_w, Inches(card_h), dk.GREEN)
        frame = dk._textbox(slide, x + Inches(0.3), Inches(card_top + 0.27),
                            col_w - Inches(0.6), Inches(0.25))
        dk._para(frame, f"Q{i + 1}", size=12, color=dk.GOLD, bold=True, first=True)
        stem_h = dk._text_height(q.stem, inner_in, BODY_PT, "bold")
        frame = dk._textbox(slide, x + Inches(0.3), Inches(card_top + 0.58),
                            col_w - Inches(0.6), Inches(stem_h + 0.1))
        dk._para(frame, q.stem, size=BODY_PT, color=dk.WHITE, bold=True, first=True,
                 line_spacing=1.15)
        frame = dk._textbox(slide, x + Inches(0.3), Inches(card_top + 0.58 + tallest + 0.32),
                            col_w - Inches(0.6), Inches(3.2))
        for j, opt in enumerate(q.options):
            dk._para(frame, f"{'ABCD'[j]}.  {opt}", size=BODY_PT, color=dk.WHITE,
                     first=(j == 0), space_after=9, line_spacing=1.12)
    dk._progress(slide, marker, on_dark=True)
    dk._notes(slide, s.notes)


def _render_reveal_17(prs, s, marker, index, total):
    """deckkit's plain answer slide, with stems and reasons at 17 point."""
    from pptx.util import Inches
    slide = dk._blank(prs)
    dk._ground(slide, dk.PAPER)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), "ANSWERS", fill=dk.GREEN,
             text_color=dk.WHITE, width=Inches(1.35))
    frame = dk._textbox(slide, dk.MARGIN + Inches(1.6), Inches(0.57), Inches(8.5), Inches(0.4))
    dk._para(frame, s.label, size=15, color=dk.GREEN, bold=True, first=True)
    inner_in = dk.CONTENT_W.inches - 0.8
    y = 1.32
    for i, q in enumerate(s.questions):
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        stem_h = dk._text_height(stem, inner_in, BODY_PT)
        ans_h = dk._text_height(answer, inner_in, 18.0, "mono")
        card_h = 0.95 + stem_h + ans_h + dk._text_height(q.reason, inner_in, BODY_PT)
        dk._rect(slide, dk.MARGIN, Inches(y), dk.CONTENT_W, Inches(card_h), dk.WHITE, line=dk.BORDER)
        dk._rect(slide, dk.MARGIN, Inches(y), Inches(0.1), Inches(card_h), dk.GOLD)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.4), Inches(y + 0.26),
                            dk.CONTENT_W - Inches(0.8), Inches(stem_h + 0.1))
        dk._para(frame, stem, size=BODY_PT, color=dk.MUTED, first=True, line_spacing=1.15)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.4), Inches(y + 0.26 + stem_h + 0.28),
                            dk.CONTENT_W - Inches(0.8), Inches(ans_h + 1.0))
        dk._para(frame, answer, size=18.0, color=dk.GREEN, font=dk.MONO_FONT,
                 bold=True, first=True, line_spacing=1.15)
        dk._para(frame, q.reason, size=BODY_PT, color=dk.INK, space_before=7, line_spacing=1.15)
        y += card_h + 0.27
    dk._progress(slide, marker)
    dk._notes(slide, s.notes)


@dataclass
class CourseCheck(dk.Check):
    """A picture-free check whose stems, options and reasons stay at 17 point.

    deckkit's own picture-free check sets options at 15 point and reasons at
    16; the slide standard's floor is 17, and the shared kit cannot change
    under the earlier chapters. The build fails rather than shrinking.
    """


def _course_check(prs, s, marker, index, total):
    slide = dk._blank(prs)
    dk._ground(slide, dk.GREEN_DEEP)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), f"CHECK {index} OF {total}",
             fill=dk.GOLD, text_color=dk.INK, width=Inches(1.85))
    frame = dk._textbox(slide, dk.MARGIN + Inches(2.1), Inches(0.57), Inches(8.0), Inches(0.4))
    dk._para(frame, s.label, size=17, color=dk.WHITE, bold=True, first=True)
    col_w = Emu(int((dk.CONTENT_W - Inches(0.7)) / 2))
    inner = col_w.inches - 0.6
    card_top, card_h = 1.32, 5.02
    stem_pt, opt_pt = 18.0, 17.0
    tallest = max(dk._text_height(q.stem, inner, stem_pt, "bold") for q in s.questions)
    for q in s.questions:
        options = sum(dk._text_height(f"D.  {o}", inner, opt_pt) + 0.13 for o in q.options)
        assert tallest + 0.32 + options <= card_h - 0.95, (s.label, 'check text does not fit at 17 point')
    for i, q in enumerate(s.questions):
        x = dk.MARGIN + (col_w + Inches(0.7)) * i
        dk._rect(slide, x, Inches(card_top), col_w, Inches(card_h), dk.GREEN)
        frame = dk._textbox(slide, x + Inches(0.3), Inches(card_top + 0.27), col_w - Inches(0.6), Inches(0.25))
        dk._para(frame, f"Q{i + 1}", size=12, color=dk.GOLD, bold=True, first=True)
        stem_top = card_top + 0.58
        frame = dk._textbox(slide, x + Inches(0.3), Inches(stem_top), col_w - Inches(0.6),
                            Inches(dk._text_height(q.stem, inner, stem_pt, "bold") + 0.1))
        dk._para(frame, q.stem, size=stem_pt, color=dk.WHITE, bold=True, first=True, line_spacing=1.15)
        frame = dk._textbox(slide, x + Inches(0.3), Inches(stem_top + tallest + 0.32),
                            col_w - Inches(0.6), Inches(3.2))
        for j, option in enumerate(q.options):
            dk._para(frame, f"{'ABCD'[j]}.  {option}", size=opt_pt, color=dk.WHITE,
                     first=(j == 0), space_after=9, line_spacing=1.12)
    dk._progress(slide, marker, on_dark=True)
    dk._notes(slide, s.notes)


def _course_reveal(prs, s, marker, index, total):
    slide = dk._blank(prs)
    dk._ground(slide, dk.PAPER)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), "ANSWERS", fill=dk.GREEN,
             text_color=dk.WHITE, width=Inches(1.35))
    frame = dk._textbox(slide, dk.MARGIN + Inches(1.6), Inches(0.57), Inches(8.5), Inches(0.4))
    dk._para(frame, s.label, size=17, color=dk.GREEN, bold=True, first=True)
    inner = dk.CONTENT_W.inches - 0.8
    stem_pt, ans_pt, reason_pt = 17.0, 20.0, 17.0
    cards = []
    for i, q in enumerate(s.questions):
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        heights = (dk._text_height(stem, inner, stem_pt), dk._text_height(answer, inner, ans_pt, "mono"),
                   dk._text_height(q.reason, inner, reason_pt))
        cards.append((stem, answer, q.reason, heights))
    assert sum(0.95 + sum(h) for *_t, h in cards) + 0.27 <= 5.1, (s.label, 'answers do not fit at 17 point')
    y = 1.32
    for stem, answer, reason, (stem_h, ans_h, reason_h) in cards:
        card_h = 0.95 + stem_h + ans_h + reason_h
        dk._rect(slide, dk.MARGIN, Inches(y), dk.CONTENT_W, Inches(card_h), dk.WHITE, line=dk.BORDER)
        dk._rect(slide, dk.MARGIN, Inches(y), Inches(0.1), Inches(card_h), dk.GOLD)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.4), Inches(y + 0.26),
                            dk.CONTENT_W - Inches(0.8), Inches(stem_h + 0.1))
        dk._para(frame, stem, size=stem_pt, color=dk.MUTED, first=True, line_spacing=1.15)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.4), Inches(y + 0.26 + stem_h + 0.28),
                            dk.CONTENT_W - Inches(0.8), Inches(ans_h + 1.0))
        dk._para(frame, answer, size=ans_pt, color=dk.GREEN, font=dk.MONO_FONT,
                 bold=True, first=True, line_spacing=1.15)
        dk._para(frame, reason, size=reason_pt, color=dk.INK, space_before=7, line_spacing=1.15)
        y += card_h + 0.27
    dk._progress(slide, marker)
    dk._notes(slide, s.notes)


@dataclass
class CourseFigureCheck(dk.Check):
    """A check with its figure beside the questions, every run at 17 point.

    deckkit's own check with a picture sets options at 15 point; this form
    stacks the two questions in a column ``text_w`` wide and draws the
    figure, marks and all, in the rest of the slide. The build fails rather
    than shrinking the text.
    """


FIGURE_CHECK_W = 3.3   # the figure's column on a check's question slide


def _figure_column(slide, s, top, x0=None):
    """The check's figure, fitted right of the text column."""
    from pathlib import Path
    from pptx.util import Inches
    picture = s.picture
    path = None if dk.FIGURES_DIR is None else Path(dk.FIGURES_DIR) / picture.filename
    if x0 is None:
        x0 = dk.MARGIN.inches + s.text_w + 0.35
    width, height = dk.MARGIN.inches + dk.CONTENT_W.inches - x0, 6.3 - top
    px_w, px_h = dk._picture_size(picture, path) or (picture.aspect * 1000.0, 1000.0)
    scale = min(width / px_w, height / px_h)
    pic_w, pic_h = px_w * scale, px_h * scale
    pic_x = x0 + (width - pic_w) / 2
    dk._rect(slide, Inches(pic_x - .04), Inches(top - .04), Inches(pic_w + .08),
             Inches(pic_h + .08), dk.WHITE, line=dk.BORDER)
    if path is not None and path.is_file():
        dk._add_picture(slide, picture, path, pic_x, top, pic_w, pic_h)
    else:
        dk._placeholder_plate(slide, picture, pic_x, top, pic_w, pic_h)
    dk._draw_marks(slide, picture.marks, pic_x, top, pic_w, pic_h)
    frame = dk._textbox(slide, Inches(pic_x), Inches(top + pic_h + .1), Inches(pic_w), Inches(.3))
    dk._para(frame, picture.credit, size=11, color=dk.MUTED, first=True)


def _course_figure_check(prs, s, marker, index, total):
    """Two question cards side by side, the figure in a third column."""
    from pptx.util import Inches
    slide = dk._blank(prs)
    dk._ground(slide, dk.GREEN_DEEP)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), f"CHECK {index} OF {total}",
             fill=dk.GOLD, text_color=dk.INK, width=Inches(1.85))
    frame = dk._textbox(slide, dk.MARGIN + Inches(2.1), Inches(0.57), Inches(8.0), Inches(0.4))
    dk._para(frame, s.label, size=17, color=dk.WHITE, bold=True, first=True)
    refs = {m.number: dk.GOLD for m in s.picture.marks}
    card_w = (dk.CONTENT_W.inches - FIGURE_CHECK_W - 0.7) / 2
    inner = card_w - 0.6
    card_top, card_h = 1.32, 5.02
    tallest = max(dk._text_height(q.stem, inner, 17, "bold") for q in s.questions)
    for q in s.questions:
        options = sum(dk._text_height(f"D.  {o}", inner, 17) + 0.13 for o in q.options)
        assert 0.58 + tallest + 0.32 + options <= card_h - 0.15, (s.label, 'check text does not fit at 17 point')
    for i, q in enumerate(s.questions):
        x = dk.MARGIN.inches + (card_w + 0.35) * i
        dk._rect(slide, Inches(x), Inches(card_top), Inches(card_w), Inches(card_h), dk.GREEN)
        frame = dk._textbox(slide, Inches(x + 0.3), Inches(card_top + 0.27), Inches(inner), Inches(0.25))
        dk._para(frame, f"Q{i + 1}", size=12, color=dk.GOLD, bold=True, first=True)
        frame = dk._textbox(slide, Inches(x + 0.3), Inches(card_top + 0.58), Inches(inner),
                            Inches(dk._text_height(q.stem, inner, 17, "bold") + 0.1))
        dk._para(frame, q.stem, size=17, color=dk.WHITE, bold=True, first=True, line_spacing=1.15, refs=refs)
        frame = dk._textbox(slide, Inches(x + 0.3), Inches(card_top + 0.58 + tallest + 0.32),
                            Inches(inner), Inches(3.2))
        for j, option in enumerate(q.options):
            dk._para(frame, f"{'ABCD'[j]}.  {option}", size=17, color=dk.WHITE,
                     first=(j == 0), space_after=9, line_spacing=1.12)
    _figure_column(slide, s, card_top, dk.MARGIN.inches + dk.CONTENT_W.inches - FIGURE_CHECK_W)
    dk._progress(slide, marker, on_dark=True)
    dk._notes(slide, s.notes)


def _arial_lines(text, width_in, pt, weight='regular'):
    """Lines the text wraps to in Arial, or deckkit's estimate without the font."""
    from pathlib import Path
    from PIL import ImageFont
    path = Path('/System/Library/Fonts/Supplemental') / ('Arial Bold.ttf' if weight == 'bold' else 'Arial.ttf')
    if not path.is_file():
        return dk._line_count(text, width_in, pt, weight)
    font = ImageFont.truetype(str(path), int(pt * 10))
    limit = width_in * 72 * 10 * .98   # PowerPoint's text inset leaves a little less
    lines, line = 1, ''
    for word in text.split():
        trial = f'{line} {word}'.strip()
        if line and font.getlength(trial) > limit:
            lines, line = lines + 1, word
        else:
            line = trial
    return lines


def _course_figure_reveal(prs, s, marker, index, total):
    from pptx.util import Inches
    slide = dk._blank(prs)
    dk._ground(slide, dk.PAPER)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(0.16), dk.GOLD)
    dk._chip(slide, dk.MARGIN, Inches(0.55), "ANSWERS", fill=dk.GREEN,
             text_color=dk.WHITE, width=Inches(1.35))
    frame = dk._textbox(slide, dk.MARGIN + Inches(1.6), Inches(0.57), Inches(8.5), Inches(0.4))
    dk._para(frame, s.label, size=17, color=dk.GREEN, bold=True, first=True)
    refs = {m.number: m.rgb for m in s.picture.marks}
    inner = s.text_w - 0.6
    def height(text, pt, weight='regular'):
        # PowerPoint draws a 1.15 spaced line about 1.2 em apart, and wraps
        # by the font's real widths, so both are measured here (fm 008).
        return _arial_lines(text, inner, pt, weight) * pt * 1.15 * 1.2 / 72
    y = 1.32
    for i, q in enumerate(s.questions):
        stem = f"Q{i + 1}   {q.stem}"
        answer = f"{q.answer}.  {q.options['ABCD'.index(q.answer)]}"
        stem_h, ans_h, reason_h = height(stem, 17), height(answer, 18, 'bold'), height(q.reason, 17)
        card_h = 0.12 + stem_h + 0.08 + ans_h + 0.08 + reason_h + 0.2
        dk._rect(slide, dk.MARGIN, Inches(y), Inches(s.text_w), Inches(card_h), dk.WHITE, line=dk.BORDER)
        dk._rect(slide, dk.MARGIN, Inches(y), Inches(0.1), Inches(card_h), dk.GOLD)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.3), Inches(y + 0.12), Inches(inner), Inches(stem_h))
        dk._para(frame, stem, size=17, color=dk.MUTED, first=True, line_spacing=1.15, refs=refs)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.3), Inches(y + 0.12 + stem_h + 0.08),
                            Inches(inner), Inches(ans_h + 0.08 + reason_h))
        dk._para(frame, answer, size=18, color=dk.GREEN, bold=True, first=True, line_spacing=1.15)
        dk._para(frame, q.reason, size=17, color=dk.INK, space_before=6, line_spacing=1.15)
        y += card_h + 0.15
    assert y - 0.15 <= 6.45, (s.label, 'answers do not fit at 17 point')
    _figure_column(slide, s, 1.32)
    dk._progress(slide, marker)
    dk._notes(slide, s.notes)


@dataclass
class WidePair(dk.Pair):
    """A book figure drawn as large as the slide allows, beside a narrow column.

    The header is the compact one the course charts use, so the picture
    gets the full height from the rule down to the credit line. Body text
    stays at 17 point; the build fails rather than shrinking it.
    """


WIDE_TOP, WIDE_BOTTOM, CREDIT_Y = 1.36, 6.68, 6.24


def _wide_pair(prs, s, marker):
    from pathlib import Path
    slide = dk._blank(prs)
    dk._ground(slide, dk.PAPER)
    dk._rect(slide, 0, 0, dk.SLIDE_W, Inches(.16), dk.GREEN)
    frame = dk._textbox(slide, dk.MARGIN, Inches(.42), dk.CONTENT_W, Inches(.84))
    dk._para(frame, s.left.title, size=28, color=dk.GREEN, font=dk.DISPLAY_FONT,
             first=True, line_spacing=1.0)
    dk._header_rule(slide, Inches(1.25))
    refs = {m.number: m.rgb for m in s.picture.marks}
    top = WIDE_TOP
    frame = dk._textbox(slide, dk.MARGIN, Inches(top), Inches(s.text_w), Inches(4.8))
    for i, line in enumerate(s.left.lines):
        dk._para(frame, line, size=17, color=dk.INK, first=(i == 0), space_after=11,
                 line_spacing=dk._PAIR_BODY_SPACING, refs=refs)
    top += sum(dk._text_height(line, s.text_w, 17, spacing=dk._PAIR_BODY_H) + 0.18
               for line in s.left.lines) + 0.22
    if s.left.accent:
        accent_h = dk._text_height(s.left.accent, s.text_w - 0.32, 18, "bold",
                                   spacing=dk._PAIR_TIGHT_H) + 0.16
        dk._rect(slide, dk.MARGIN, Inches(top), Inches(0.09), Inches(accent_h), dk.GOLD)
        frame = dk._textbox(slide, dk.MARGIN + Inches(0.32), Inches(top + 0.04),
                            Inches(s.text_w - 0.32), Inches(accent_h))
        dk._para(frame, s.left.accent, size=18, color=dk.INK, bold=True, first=True,
                 line_spacing=1.0, refs=refs)
        top += accent_h
    assert top <= CREDIT_Y - 0.06, (s.left.title, 'text does not fit at 17 point')
    picture = s.picture
    root = dk.FIGURES_DIR if isinstance(picture, dk.Figure) else dk.CHARTS_DIR
    path = None if root is None else Path(root) / picture.filename
    x0 = dk.MARGIN.inches + s.text_w + 0.35
    width, height = dk.MARGIN.inches + dk.CONTENT_W.inches - x0, WIDE_BOTTOM - WIDE_TOP
    px_w, px_h = dk._picture_size(picture, path) or (picture.aspect * 1000.0, 1000.0)
    scale = min(width / px_w, height / px_h)
    pic_w, pic_h = px_w * scale, px_h * scale
    pic_x, pic_y = x0 + (width - pic_w) / 2, WIDE_TOP
    dk._rect(slide, Inches(pic_x - .04), Inches(pic_y - .04), Inches(pic_w + .08),
             Inches(pic_h + .08), dk.WHITE, line=dk.BORDER)
    if path is not None and path.is_file():
        dk._add_picture(slide, picture, path, pic_x, pic_y, pic_w, pic_h)
    else:
        dk._placeholder_plate(slide, picture, pic_x, pic_y, pic_w, pic_h)
    dk._draw_marks(slide, picture.marks, pic_x, pic_y, pic_w, pic_h)
    # The credit closes the text column, so the picture can take the full height.
    frame = dk._textbox(slide, dk.MARGIN, Inches(CREDIT_Y), Inches(s.text_w), Inches(.42))
    dk._para(frame, picture.credit, size=11, color=dk.MUTED, first=True)
    dk._progress(slide, marker)
    dk._notes(slide, s.notes)


@contextmanager
def course_slide_renderer():
    """Install the chapter-only wide chart/text form for this build only."""
    original=dk.render_chart
    original_check,original_reveal=dk.render_check,dk.render_reveal
    original_pair=dk.render_pair
    def pair(prs,s,marker):
        if isinstance(s,WidePair):
            return _wide_pair(prs,s,marker)
        result=original_pair(prs,s,marker)
        _paint_masks(prs.slides[-1],s.picture)
        return result
    def check(prs,s,marker,index,total):
        if isinstance(s,CourseFigureCheck):
            return _course_figure_check(prs,s,marker,index,total)
        if isinstance(s,CourseCheck) and s.picture is None:
            return _course_check(prs,s,marker,index,total)
        if s.picture is None and _check_fits(s):
            return _render_check_17(prs,s,marker,index,total)
        if s.label in PADDED_CHECKS:
            # deckkit sizes the beside cards from an estimate that runs short
            # for these options; measure them a line taller so the last
            # choice keeps its padding (rp2x2 finding 8).
            measure = dk._text_height
            dk._text_height = lambda text, *a, **k: measure(text, *a, **k) * 1.12 + .02
            try:
                return original_check(prs,s,marker,index,total)
            finally:
                dk._text_height = measure
        return original_check(prs,s,marker,index,total)
    def reveal(prs,s,marker,index,total):
        if isinstance(s,CourseFigureCheck):
            return _course_figure_reveal(prs,s,marker,index,total)
        if isinstance(s,CourseCheck) and s.picture is None:
            return _course_reveal(prs,s,marker,index,total)
        if s.picture is None and _check_fits(s):
            return _render_reveal_17(prs,s,marker,index,total)
        return original_reveal(prs,s,marker,index,total)
    def render(prs,s,marker):
        if not isinstance(s,CourseChart):
            return original(prs,s,marker)
        from pathlib import Path
        from pptx.util import Inches,Pt
        slide=dk._blank(prs)
        dk._ground(slide,dk.PAPER)
        dk._rect(slide,0,0,dk.SLIDE_W,Inches(.16),dk.GREEN)
        frame=dk._textbox(slide,dk.MARGIN,Inches(.42),dk.CONTENT_W,Inches(.84))
        dk._para(frame,s.title,size=28,color=dk.GREEN,font=dk.DISPLAY_FONT,first=True,line_spacing=1.0)
        dk._header_rule(slide,Inches(1.25))
        frame=dk._textbox(slide,dk.MARGIN,Inches(1.33),dk.CONTENT_W,Inches(TEXT_H))
        refs={mark.number: mark.rgb for mark in s.marks}
        dk._para(frame,' '.join(s.teaching),size=17,color=dk.INK,first=True,line_spacing=1.0,refs=refs)
        from charts_chapter07 import DATA
        width=chart_width(DATA[s.asset])
        y=2.62
        if s.figure is None:
            x=(dk.SLIDE_W.inches-width)/2
        else:
            x=dk.MARGIN.inches+dk.CONTENT_W.inches-width
            gap=.22
            _book_drawing(slide,s.figure,dk.MARGIN.inches,y,x-gap-dk.MARGIN.inches,HEIGHT)
        dk._rect(slide,Inches(x-.04),Inches(y-.04),Inches(width+.08),Inches(HEIGHT+.08),dk.WHITE,line=dk.BORDER)
        dk._add_picture(slide,s,Path(dk.CHARTS_DIR)/s.filename,x,y,width,HEIGHT)
        dk._draw_marks(slide,s.marks,x,y,width,HEIGHT)
        frame=dk._textbox(slide,Inches(x),Inches(6.52),Inches(width),Inches(.22))
        dk._para(frame,s.credit,size=11,color=dk.MUTED,first=True)
        dk._progress(slide,marker)
        dk._notes(slide,s.notes)
    dk.render_chart=render
    dk.render_check,dk.render_reveal=check,reveal
    dk.render_pair=pair
    try:
        yield
    finally:
        dk.render_chart=original
        dk.render_check,dk.render_reveal=original_check,original_reveal
        dk.render_pair=original_pair


def _overlaps(a, b):
    return a.x0 < b.x1 and b.x0 < a.x1 and a.y0 < b.y1 and b.y0 < a.y1


def _circle_box(cx, cy, radius, box):
    x = max(box.x0, min(cx, box.x1))
    y = max(box.y0, min(cy, box.y1))
    return math.hypot(x - cx, y - cy) < radius


def _segment_box(start, end, box):
    """Exact line/rectangle intersection, not the line's enclosing box."""
    x,y=start
    dx,dy=end[0]-x,end[1]-y
    lower,upper=0.,1.
    for p,q in ((-dx,x-box.x0),(dx,box.x1-x),(-dy,y-box.y0),(dy,box.y1-y)):
        if abs(p)<1e-12:
            if q<0:
                return False
        elif p<0:
            lower=max(lower,q/p)
        else:
            upper=min(upper,q/p)
        if lower>upper:
            return False
    return True


def _segment_distance(start, end, point):
    dx,dy=end[0]-start[0],end[1]-start[1]
    length=dx*dx+dy*dy
    t=max(0,min(1,((point[0]-start[0])*dx+(point[1]-start[1])*dy)/length)) if length else 0
    return math.hypot(point[0]-start[0]-t*dx,point[1]-start[1]-t*dy)


def _assert_layout(fig, labels, bars):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [t.get_window_extent(renderer).padded(2) for t in labels]
    for i, (label, box) in enumerate(zip(labels, boxes)):
        assert fig.bbox.contains(box.x0, box.y0) and fig.bbox.contains(box.x1, box.y1), (
            f'label outside chart: {label.get_text()}')
        assert not any(_overlaps(box, b) for b in boxes[:i]), (
            f'label overlap: {label.get_text()}')
        assert not any(_overlaps(box, line) for line in bars), (
            f'label crosses OHLC bar: {label.get_text()}')
        # Arial capitals at 16.5 pt have >=15 px of true ink at 100 dpi.
        # A rendered-PPTX raster audit also measures every actual label.
        assert label.get_fontsize() >= FONT
        ink = TextPath((0,0),label.get_text(),size=label.get_fontsize(),
                       prop=label.get_fontproperties()).get_extents().height*100/72
        assert ink >= 14, f'Glyph ink below safe 100 dpi threshold: {label.get_text()}: {ink:.2f}px'
    return boxes


def _marks(fig, targets, specs, boxes, segments, groups, brackets=None, authored=False):
    """Compute exact data-anchored rings and touching, collision-free badges."""
    ring_radius, badge_r = .048 * ck.DPI, .14 * ck.DPI
    circles = []
    result = []
    leaders = []
    group_gap = getattr(fig, 'group_gap', 0) * ck.DPI   # keeps a box's badge off its border
    future = [(targets[tuple(s['target'])], group_gap if tuple(s['target']) in groups
               else 5 if tuple(s['target']) in (brackets or {}) else ring_radius)
              for s in specs if tuple(s['target']) in targets]
    # Reserve a middle-of-bar badge before its high/low neighbours. Greedy
    # extreme-first placement can otherwise close both escape lanes.
    ordered=sorted(specs,key=lambda spec: 0 if spec['target'][2] in ('range','group') else 1)
    for spec in ordered:
        target = tuple(spec['target'])
        if target not in targets:
            continue
        cx, cy = targets[target]
        radius=group_gap if target in groups else ring_radius
        bracket = (brackets or {}).get(target)
        if bracket:
            # The badge sits beside the bracket's middle, never on it.
            # 3.5 point line: half its width is about 5 px at 200 dpi.
            cx, cy, radius = bracket[0], (bracket[1]+bracket[2])/2, 5
        own = [b for b in segments if bracket and abs((b.x0+b.x1)/2-cx) < 1 and b.width < 10]
        obstacles = boxes + [b for b in segments if not any(b is o for o in own)]
        if getattr(fig, 'paint_boxes', False):
            # Another mark's box is never a place for this badge.
            from matplotlib.transforms import Bbox as _B
            obstacles = obstacles + [_B([[g[0], g[1]], [g[2], g[3]]]) for t, g in groups.items() if t != target]
        if target in groups and authored:
            # A boxed feature keeps its badge outside the box (rp2x2 finding 2).
            from matplotlib.transforms import Bbox
            x0, y0, x1, y1 = groups[target]
            pad = .05 * ck.DPI if getattr(fig, 'paint_boxes', False) else 0   # never touching its own box
            own_box = Bbox([[x0 - pad, y0 - pad], [x1 + pad, y1 + pad]])
        else:
            own_box = None
        assert not any(_circle_box(cx, cy, radius, b) for b in boxes), (spec, 'ring crosses text', (cx, cy, radius), [(b.x0, b.y0, b.x1, b.y1) for b in boxes if _circle_box(cx, cy, radius, b)])
        found = None
        # A mark may name the directions its badge should try first.
        order = list(spec.get('angles', ())) + [a for a in range(0, 360, 5) if a not in spec.get('angles', ())]
        if bracket and target[2] == 'span':
            # A range bracket keeps its badge at mid-height, a badge-width
            # clear to its left, joined by a hairline (rp4x2 finding 1).
            gap = .3 * ck.DPI
            bx, by = cx - gap - badge_r, cy
            assert not any(_circle_box(bx, by, badge_r + 2, b) for b in boxes), (spec, 'bracket badge crosses text')
            found = (bx, by, (cx - 5, cy), (bx + badge_r, by), gap)
        # Authored charts keep each badge clearly off every tick and label
        # (rp2x2 finding 2); the owners' charts keep their validated layout.
        clear = 8 if authored else 1
        # Try direct contact first. Firstmate's 012 instruction permits the
        # nearest clear badge joined to its ring by a same-colour hairline.
        for extra in ([] if found else range(0, int(2*ck.DPI), 4)):
            distance = radius + badge_r + extra
            for angle in order:
                theta = math.radians(angle)
                ux,uy=math.cos(theta),math.sin(theta)
                bx, by = cx + distance * ux, cy + distance * uy
                if not (badge_r + 2 <= bx <= fig.bbox.width - badge_r - 2 and badge_r + 2 <= by <= fig.bbox.height - badge_r - 2):
                    continue
                if any(_circle_box(bx, by, badge_r + clear, b) for b in obstacles):
                    continue
                if own_box is not None and _circle_box(bx, by, badge_r - 1, own_box):
                    continue
                if any(math.hypot(bx - x, by - y) < badge_r + r + 1 for ((x,y),r) in circles):
                    continue
                if any(math.hypot(bx - x, by - y) < badge_r + r - .01 for ((x,y),r) in future):
                    continue
                start=(cx+radius*ux,cy+radius*uy)
                end=(bx-badge_r*ux,by-badge_r*uy)
                if extra and any(_segment_box(start,end,b.padded(1)) for b in obstacles):
                    continue
                if extra and any(_segment_distance(start,end,point)<r+1 for point,r in circles):
                    continue
                if extra and any(point != (cx,cy) and _segment_distance(start,end,point)<r+1 for point,r in future):
                    continue
                found=(bx,by,start,end,extra)
                break
            if found:
                break
        if found is None:
            raise AssertionError(f'No touching badge position for {spec}')
        bx,by,start,end,extra=found
        if extra:
            color='#'+str(dk.MARK_COLORS[spec['color']])
            fig.add_artist(Line2D((start[0]/ck.DPI,end[0]/ck.DPI),
                                  (start[1]/ck.DPI,end[1]/ck.DPI),
                                  transform=fig.dpi_scale_trans,color=color,lw=1))
            leaders.append((spec['number'],extra/ck.DPI))
        circles.extend((((cx, cy), radius), ((bx, by), badge_r)))
        bounds=groups.get(target,(cx-radius,cy-radius,cx+radius,cy+radius))
        if bracket and target[2] == 'span':
            # Caps at the high and low ticks make the bracket read as a span.
            color='#'+str(dk.MARK_COLORS[spec['color']])
            for y in (bracket[1], bracket[2]):
                fig.add_artist(Line2D(((bracket[0]-1)/ck.DPI,(bracket[0]+.09*ck.DPI)/ck.DPI),
                                      (y/ck.DPI,y/ck.DPI),transform=fig.dpi_scale_trans,
                                      color=color,lw=3.5))
        if bracket:
            result.append(dk.Mark(spec['number'], 'line',
                                  bracket[0]/fig.bbox.width, 1-bracket[1]/fig.bbox.height,
                                  bracket[0]/fig.bbox.width, 1-bracket[2]/fig.bbox.height,
                                  color=spec['color'], at=(bx/fig.bbox.width, 1-by/fig.bbox.height), size=.28))
            continue
        result.append(dk.Mark(spec['number'], 'box' if target in groups else 'circle',
                              bounds[0]/fig.bbox.width, 1-bounds[3]/fig.bbox.height,
                              bounds[2]/fig.bbox.width, 1-bounds[1]/fig.bbox.height,
                              color=spec['color'], at=(bx/fig.bbox.width, 1-by/fig.bbox.height), size=.28))
    fig.chart_leaders=tuple(leaders)
    return tuple(result)


def chart_width(spec):
    """Full content width, or narrower beside a book drawing."""
    return spec.get('width', WIDTH)


def _target_specs(key, spec):
    # Explicit semantic anchors, independent of artwork dimensions.
    # The remaining entries are imported from the owners' marked drawings.
    return spec.get('targets', ())


@lru_cache(maxsize=128)
def layout(key, page=0):
    from charts_chapter07 import DATA
    spec = DATA[key]
    W = chart_width(spec)
    fig = plt.figure(figsize=(W, HEIGHT), dpi=ck.DPI)
    labels, segments, targets, levels, tips, groups = [], [], {}, [], [], {}
    columns = []   # labels keep off them; a volume badge sits on its own
    ink = []       # plotted ink that only badges must avoid
    # Part 2 marks a range as a box along the bar and a volume as a box
    # round its column, with every badge clear of both (rp2x1 findings 3, 4).
    authored = spec.get('owner') in ('p2', 'sh')
    vbox = authored or spec.get('volume_boxes', False)
    brackets = {}
    def text(x, y, value, *, ha='center', va='center', color=ck.INK):
        # A white backing breaks a dashed level line where it meets a label.
        artist = fig.text(x/W, y/HEIGHT, value, ha=ha, va=va,
                          fontsize=FONT, color=color, fontweight='bold',
                          fontfamily=dk.BODY_FONT,
                          bbox=dict(facecolor=ck.WHITE, edgecolor='none', pad=1))
        labels.append(artist)
        return artist

    def semantic_labels(pane,index):
        result=[]
        for note in pane.notes:
            if note.x!=index or not note.label:
                continue
            value=note.label.replace('\n',' ')
            # These old price callouts are now the four tick-anchored labels.
            if re.match(r'^(?:(?:next|first|second|middle|wide)\s+)?[OHLC]\s+\d',value,re.I):
                continue
            if re.match(r'^(?:open|high|low|close|prior low)\s+\d',value,re.I):
                continue
            result.append(value)
        return result
    def line(ax, x, y, **kwargs):
        artist, = ax.plot(x, y, **kwargs)
        return artist
    if spec['special'] == 'sentiment':
        for i, (trend, formation, result) in enumerate((
                ('Uptrend +4.0%', 'Bullish formation +2.0%', 'CONTINUATION'),
                ('Uptrend +4.0%', 'Bearish formation -2.0%', 'POTENTIAL REVERSAL'),
                ('Downtrend -4.0%', 'Bullish formation +2.0%', 'POTENTIAL REVERSAL'),
                ('Downtrend -4.0%', 'Bearish formation -2.0%', 'CONTINUATION'))):
            x, y = (3 if i%2==0 else 8.5), (2.9 if i<2 else 1.35)
            text(x,y+.45,trend, color=ck.GREEN_DEEP)
            text(x,y+.12,formation, color=ck.GREEN_DEEP)
            text(x,y-.35,result, color=ck.GOLD if 'REVERSAL' in result else ck.GREEN_DEEP)
            dot=Circle((x-2.2,y-.35),.025,transform=fig.dpi_scale_trans,color=ck.GREEN)
            fig.add_artist(dot)
            targets[0,i,'case']=((x-2.2)*ck.DPI,(y-.35)*ck.DPI)
    elif spec['special'] == 'counts':
        # Groups of plain bars, each named by how many bars it has. The
        # shapes are drawn only to be counted, so they carry no prices.
        shapes=((1.45,2.45,1.75,2.2),(1.6,2.6,2.3,1.85),(1.4,2.3,1.6,2.1),
                (1.55,2.55,2.2,1.7),(1.5,2.5,1.8,2.35))
        for gi,((count,label),centre) in enumerate(zip(spec['count_groups'],spec['count_centres'])):
            xs=[centre+(i-(count-1)/2)*.42 for i in range(count)]
            for i,x in enumerate(xs):
                low,high,opening,closing=shapes[i]
                for xx,yy in (((x,x),(low,high)),((x-.15,x),(opening,opening)),((x,x+.15),(closing,closing))):
                    artist=Line2D(xx,yy,transform=fig.dpi_scale_trans,color=ck.INK,lw=2.4)
                    fig.add_artist(artist)
                    segments.append(artist.get_window_extent().padded(2))
            text(centre,.95,label,color=ck.GREEN_DEEP)
            bounds=((xs[0]-.35)*ck.DPI,1.25*ck.DPI,(xs[-1]+.35)*ck.DPI,2.75*ck.DPI)
            groups[0,gi,'group']=bounds
            targets[0,gi,'group']=(bounds[2],(bounds[1]+bounds[3])/2)
    elif spec['special'] == 'nr_table':
        # ID/NR4 to NR7 as a table: each window counted back from the last
        # bar, its narrowest range, and whether the last bar is that bar.
        ranges=spec['nr_ranges']
        last=len(ranges)
        text(.6,3.2,'Bar',ha='left',color=ck.GREEN_DEEP)
        text(.6,2.82,'Range',ha='left',color=ck.GREEN_DEEP)
        for i,value in enumerate(ranges):
            x=2.6+i*1.2
            text(x,3.2,str(i+1),color=ck.MUTED)
            text(x,2.82,f'{value:.1f}')
        heads=((.6,'Window','left'),(3.3,'Bars counted','center'),
               (5.9,'Narrowest range','center'),(8.7,f'Is bar {last} the narrowest?','center'))
        for x,value,ha in heads:
            text(x,2.25,value,ha=ha,color=ck.GREEN_DEEP)
        rows=[]
        for row,count in enumerate(range(4,last+1)):
            y=1.85-row*.36
            window=ranges[last-count:]
            low=min(window)
            where=last-count+window.index(low)+1
            answer='Yes' if where==last and window.count(low)==1 else 'No'
            text(.6,y,f'NR{count}',ha='left')
            text(3.3,y,f'bars {last-count+1} to {last}')
            text(5.9,y,f'{low:.1f}, bar {where}')
            text(8.7,y,answer,color=ck.GREEN_DEEP if answer=='Yes' else '#'+str(dk.MARK_COLORS['red']))
            targets[0,count,'answer']=(9.25*ck.DPI,y*ck.DPI)
            rows.append((answer,y))
        yes=[y for answer,y in rows if answer=='Yes']
        if yes:
            # One bracket spans every window the last bar wins.
            brackets[0,0,'yes']=(9.25*ck.DPI,(min(yes)-.13)*ck.DPI,(max(yes)+.13)*ck.DPI)
            targets[0,0,'yes']=(9.25*ck.DPI,(min(yes)+max(yes))/2*ck.DPI)
            ink.append(Bbox.from_extents(9.25*ck.DPI-3,(min(yes)-.13)*ck.DPI,9.25*ck.DPI+3,(max(yes)+.13)*ck.DPI))
    elif spec['special'] == 'paint':
        import shapecharts_chapter07 as sc
        canvas = sc.Canvas(fig, W, text, segments, ink, groups, targets)
        spec['paint'](canvas)
    elif spec['special'] == 'characteristics':
        for y, number, title, meaning in ((2.8,'7','BRR','real body ÷ total range'),
                (1.35,'8','Angular symmetry and momentum','the angle and momentum change')):
            text(.5,y,number, color=ck.GOLD)
            text(1,y+.22,title,ha='left',color=ck.GREEN_DEEP)
            text(1,y-.22,meaning,ha='left',color=ck.MUTED)
    else:
        cell_index, start, end = page_specs(spec)[page]
        cell = spec['items'][cell_index]
        title = cell.name.replace('\n',' ')
        if title:
            text(W/2,3.64,title,color=ck.GREEN_DEEP)
        note = cell.note.replace('\n',' ')
        if note:
            text(W/2,3.32,note,color=ck.MUTED)
        has_volume = any(p.columns for p in cell.panes) and any(p.bars or p.line for p in cell.panes)
        price_bottom = 1.55 if has_volume else 1.0
        price_top = 2.72
        count = end-start
        left = 3.6 if any(p.strokes for p in cell.panes) else 2.1
        right = W - 1.5
        side = .50   # tick end to its O or C label
        if W < WIDTH:
            # Beside a book drawing the bars take the width, keeping a left
            # lane only when a level line needs its caption there.
            left = 2.3 if any(p.strokes for p in cell.panes) else 1.36
            right, side = W - 1.36, .40
        if count == 4:
            # Four bars need the full width; a level caption climbs instead,
            # and each side label sits nearer its own tick than its neighbour's.
            left, right, side = 1.36, W - spec.get('right_margin', 1.32), .36
        if spec.get('one_page') and count > 4:
            left, right = .95, W - 1.4
        xs = [left + (right-left) * i/max(1,count-1) for i in range(count)] if count>1 else [W/2]
        for pane_index, pane in enumerate(cell.panes):
            if pane.bars or pane.line:
                values = [v for b in pane.bars for v in (b.open,b.high,b.low,b.close)] + list(pane.line)
                values += [p[1] for s in pane.strokes for p in s.points]
                lo, hi = min(values),max(values)
                span = hi-lo or 1
                axis = fig.add_axes([0,price_bottom/HEIGHT,1,(price_top-price_bottom)/HEIGHT])
                axis.set_axis_off()
                axis.set_xlim(0,W)
                axis.set_ylim(lo,hi)
                def y_inches(y):
                    return price_bottom + (y-lo)/span*(price_top-price_bottom)
                def x_inches(x):
                    if count == 1:
                        return xs[0]
                    return xs[0]+(x-start)*(xs[-1]-xs[0])/(count-1)
                for index in range(start,end):
                    x=xs[index-start]
                    if pane.bars:
                        b=pane.bars[index]
                        for xx,yy in (((x,x),(b.low,b.high)),((x-.17,x),(b.open,b.open)),((x,x+.17),(b.close,b.close))):
                            artist=line(axis,xx,yy,color=ck.INK,lw=2.4,clip_on=False)
                            segments.append(artist.get_window_extent().padded(2))
                        shown=spec.get('bar_labels',{}).get(index,'OHLC')
                        if 'O' in shown:
                            text(x-side,y_inches(b.open),f'O {b.open:.2f}',ha='right')
                        if 'C' in shown:
                            text(x+side,y_inches(b.close),f'C {b.close:.2f}',ha='left')
                        if (cell_index,index,'span') in spec.get('spans',()):
                            # A range drawn as a bracket beside the bar, on its open side.
                            sx=(x-.32)*ck.DPI
                            brackets[cell_index,index,'span']=(sx,y_inches(b.low)*ck.DPI,y_inches(b.high)*ck.DPI)
                            targets[cell_index,index,'span']=(sx,y_inches((b.low+b.high)/2)*ck.DPI)
                            ink.append(Bbox.from_extents(sx-3,y_inches(b.low)*ck.DPI,sx+3,y_inches(b.high)*ck.DPI))
                        prev = pane.bars[index-1] if index > start else None
                        # A label that would sit inside the gap before its bar
                        # moves to the side, level with its own tick.
                        beside = {}
                        if authored and prev is not None:
                            gap_down, gap_up = b.high < prev.low, b.low > prev.high
                            for name, value, wanted in (('H', b.high, gap_down), ('L', b.low, gap_up)):
                                if not wanted:
                                    continue
                                if abs(y_inches(value)-y_inches(b.close)) >= .26:
                                    beside[name] = (x+side, value, 'left')
                                elif abs(y_inches(value)-y_inches(b.open)) >= .26:
                                    beside[name] = (x-side, value, 'right')
                        for name, value, direction, offset, va in (('H', b.high, 1, .19, 'bottom'), ('L', b.low, -1, -.17, 'top')):
                            if name not in shown:
                                continue
                            if name in beside:
                                bx_, val, ha = beside[name]
                                text(bx_, y_inches(val), f'{name} {value:.2f}', ha=ha)
                            else:
                                tips.append((text(x,y_inches(value)+offset,f'{name} {value:.2f}',va=va),direction))
                        if authored:
                            # A range is marked by a slim box from the bar's
                            # high to its low, inside the open and close ticks.
                            bounds = ((x-.06)*ck.DPI, (y_inches(b.low)-.03)*ck.DPI,
                                      (x+.06)*ck.DPI, (y_inches(b.high)+.03)*ck.DPI)
                            groups[cell_index,index,'range'] = bounds
                            targets[cell_index,index,'range'] = (bounds[2], (bounds[1]+bounds[3])/2)
                        for name,xx,yy in (('open',x-.17,b.open),('high',x,b.high),('low',x,b.low),('close',x+.17,b.close),('range',x,(b.low+b.high)/2)):
                            if (cell_index,index,name) not in groups:
                                targets[cell_index,index,name] = (xx*ck.DPI,y_inches(yy)*ck.DPI)
                        if index > start:
                            # A gap is the empty price space between two
                            # ranges: its mark sits midway between the bars.
                            prev = pane.bars[index-1]
                            if b.low > prev.high or b.high < prev.low:
                                edge = (prev.high+b.low)/2 if b.low > prev.high else (prev.low+b.high)/2
                                gx = (x+xs[index-start-1])/2
                                targets[cell_index,index,'gap'] = (gx*ck.DPI, y_inches(edge)*ck.DPI)
                                if authored:
                                    # A gap is a price range: box it from one
                                    # bar's extreme to the other's (rp2x2 finding 3).
                                    lo_, hi_ = sorted((prev.high, b.low) if b.low > prev.high else (b.high, prev.low))
                                    bounds = ((gx-.09)*ck.DPI, y_inches(lo_)*ck.DPI, (gx+.09)*ck.DPI, y_inches(hi_)*ck.DPI)
                                    groups[cell_index,index,'gap'] = bounds
                                    targets[cell_index,index,'gap'] = (bounds[2], (bounds[1]+bounds[3])/2)
                    else:
                        y=pane.line[index]
                        targets[cell_index,index,'line']=(x*ck.DPI,y_inches(y)*ck.DPI)
                        label=spec.get('line_format','{:g}').format(y)
                        # A trough's value sits under it, clear of the line climbing away.
                        trough=(spec.get('trough_below') and 0<index<len(pane.line)-1
                                and y<pane.line[index-1] and y<pane.line[index+1])
                        if trough:
                            text(x,y_inches(y)-.17,label,va='top')
                        else:
                            text(x,y_inches(y)+.19,label,va='bottom')
                for target,group in spec.get('groups',{}).items():
                    ci,first,last=group
                    if pane.bars and ci==cell_index and start<=first<=last<end:
                        members=pane.bars[first:last+1]
                        bottom=min(b.low for b in members)
                        top=max(b.high for b in members)
                        # A pair at the chart's edge keeps its box inside the picture.
                        bounds=(max(.05,x_inches(first)-1.45)*ck.DPI,(y_inches(bottom)-.45)*ck.DPI,
                                min(W-.05,x_inches(last)+1.45)*ck.DPI,(y_inches(top)+.45)*ck.DPI)
                        groups[target]=bounds
                        targets[target]=(bounds[2],(bounds[1]+bounds[3])/2)
                if pane.line:
                    line(axis,xs,pane.line[start:end],color=ck.INK,lw=2.4)
                    if spec.get('protect_line'):
                        # The plotted path is ink a badge must not sit on.
                        points=[(x*ck.DPI,y_inches(y)*ck.DPI) for x,y in zip(xs,pane.line[start:end])]
                        for (x0,y0),(x1,y1) in zip(points,points[1:]):
                            for step in range(41):
                                t=step/40
                                px,py=x0+(x1-x0)*t,y0+(y1-y0)*t
                                ink.append(Bbox.from_extents(px-3,py-3,px+3,py+3))
                for stroke in pane.strokes:
                    # Clip long sequences at page boundaries, preserving the
                    # original level value and global period numbering.
                    points = [(x_inches(x),y) for x,y in stroke.points]
                    if len({y for _,y in points}) == 1:
                        value=points[0][1]
                        if spec.get('span_levels'):
                            # A comparison level drawn only from its own bar to the bar read against it.
                            level=line(axis,(points[0][0],points[-1][0]+.02),(value,value),color=ck.INK,lw=1.6,ls=(0,(4,3)),zorder=0)
                            ink.append(level.get_window_extent().padded(3))
                        else:
                            band=line(axis,(.12,W-.2),(value,value),color=ck.MUTED,lw=.8,ls=(0,(4,4)),zorder=0)
                            if spec.get('level_ink'):
                                ink.append(band.get_window_extent().padded(3))   # a badge keeps off the level
                        for index,x in zip(range(start,end),xs):
                            targets[cell_index,index,'level:'+str(value)] = (x*ck.DPI,y_inches(value)*ck.DPI)
                        if stroke.label:
                            artist=text(.12,y_inches(value)+.06,stroke.label.replace('\n',' '),ha='left',va='bottom',color=ck.MUTED)
                            levels.append(artist)
                    else:
                        line(axis,[p[0] for p in points],[p[1] for p in points],color=ck.MUTED,lw=1,ls='--')
                if pane.bars:
                    for index,x in zip(range(start,end),xs):
                        semantic=semantic_labels(pane,index)
                        caption=f'Bar {index+1}' + (': '+'; '.join(semantic) if semantic else '')
                        caption_y=.39
                        if spec.get('stack_captions') and semantic:
                            # Six bars to a page leave no room for a one-line caption.
                            caption, caption_y = f'Bar {index+1}\n'+'; '.join(semantic), .5
                        artist=text(x,caption_y,caption,color=ck.MUTED)
                        fig.canvas.draw()
                        box=artist.get_window_extent(fig.canvas.get_renderer())
                        if box.x1>fig.bbox.width-3:
                            artist.set_position(((fig.bbox.width-3)/fig.bbox.width,caption_y/HEIGHT))
                            artist.set_ha('right')
                        elif box.x0<3:
                            artist.set_position((3/fig.bbox.width,caption_y/HEIGHT))
                            artist.set_ha('left')
                elif pane.line and spec.get('line_captions'):
                    # A line of trades is not a run of bars: name each point.
                    for index,x in zip(range(start,end),xs):
                        text(x,.39,spec['line_captions'][index],color=ck.MUTED)
                elif pane.line:
                    # A cell that continues an earlier one keeps the bar numbers it began with.
                    offset=spec.get('bar_offsets',{}).get(cell_index,0)
                    semantic=[f'Bar {i+1+offset}: {label}' for i in range(start,end) for label in semantic_labels(pane,i)]
                    for volume in cell.panes:
                        if volume.columns:
                            semantic.extend(f'Bar {i+1}: {label}' for i,label in volume.tags if not re.match(r'^[0-9.]+m$',label))
                    if semantic:
                        text(W/2,.39,'; '.join(semantic),color=ck.MUTED)
            elif pane.columns:
                bottom,top = (.60,spec.get('volume_top',.80)) if has_volume else (.72,2.7)
                cols=pane.columns[start:end]
                lo,hi=min(0,min(cols)),max(cols)
                span=hi-lo or 1
                ax=fig.add_axes([0,bottom/HEIGHT,1,(top-bottom)/HEIGHT])
                ax.set_axis_off();ax.set_xlim(0,W);ax.set_ylim(lo,hi)
                if lo < 0:
                    ax.axhline(0,color=ck.MUTED,lw=.8,zorder=0)
                for patch in ax.bar(xs,cols,width=.23,color=ck.GREEN):
                    columns.append(patch.get_window_extent().padded(2))
                for index,x,value in zip(range(start,end),xs,cols):
                    y=bottom+(value-lo)/span*(top-bottom)
                    label=f'{value:g}m' if has_volume else f'{value:g}'
                    # A value sits beyond its column's end: above a rise,
                    # below a fall, never on the column itself.
                    if value < 0:
                        text(x,y-.07,label,va='top',color=ck.GREEN_DEEP)
                    else:
                        text(x,y+.07,label,va='bottom',color=ck.GREEN_DEEP)
                    targets[cell_index,index,'volume']=(x*ck.DPI,(bottom+(value/2-lo)/span*(top-bottom))*ck.DPI)
                    if vbox and value > 0:
                        bounds=((x-.17)*ck.DPI,(bottom-.03)*ck.DPI,(x+.17)*ck.DPI,(y+.03)*ck.DPI)
                        groups[cell_index,index,'volume']=bounds
                        targets[cell_index,index,'volume']=(bounds[2],(bounds[1]+bounds[3])/2)
                for t in spec.get('targets', ()):
                    c_, first, name = t['target']
                    if vbox and c_ == cell_index and name.startswith('volumes:'):
                        last = int(name.split(':')[1])
                        if start <= first <= last < end:
                            peak = bottom+(max(cols[first-start:last-start+1])-lo)/span*(top-bottom)
                            bounds=((xs[first-start]-.17)*ck.DPI,(bottom-.03)*ck.DPI,
                                    (xs[last-start]+.17)*ck.DPI,(peak+.03)*ck.DPI)
                            groups[c_,first,name]=bounds
                            targets[c_,first,name]=(bounds[2],(bounds[1]+bounds[3])/2)
    caption = spec.get('caption', CAPTION)
    if (spec.get('owner') == 'p2' or spec['owner'] in ('r3a','r3b')) and not any(p.columns for c in spec['items'] for p in c.panes):
        # Say volume only where the chart draws it (rp2x3 finding 4).
        caption = PRICE_CAPTION
    text(W/2,.02,caption,color=ck.MUTED,va='bottom')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    for artist,direction in tips:
        x,y=artist.get_position()
        for pixels in range(int(.65*ck.DPI)):
            artist.set_position((x,y+direction*pixels/fig.bbox.height))
            box=artist.get_window_extent(renderer).padded(2)
            others=[t.get_window_extent(renderer).padded(2) for t in labels if t is not artist and t not in levels]
            if not any(_overlaps(box,b) for b in others+segments+columns):
                break
    # Far-left level labels may move up from their line, or else down below
    # it, never horizontally away from the level's left end. Actual renderer
    # boxes determine the lane.
    for artist in levels:
        x,y=artist.get_position()
        height=artist.get_window_extent(renderer).height/fig.bbox.height
        moves=[pixels/fig.bbox.height for pixels in range(int(HEIGHT*ck.DPI))]
        moves+=[-height-.12/HEIGHT-pixels/fig.bbox.height for pixels in range(int(HEIGHT*ck.DPI))]
        if authored:
            # Near the line first, above or below, before climbing away
            # past other prices' labels (rp2x2 finding 7).
            near = int(.12*ck.DPI)
            moves = moves[:near] + [-height-.04/HEIGHT-p/fig.bbox.height for p in range(near)] + moves[near:]
        for move in moves:
            artist.set_position((x,y+move))
            box=artist.get_window_extent(renderer).padded(2)
            others=[t.get_window_extent(renderer).padded(2) for t in labels if t is not artist]
            if (.5*ck.DPI < box.y0 and box.y1 < 3.15*ck.DPI
                    and not any(_overlaps(box,b) for b in others+segments+columns)):
                break
        else:
            raise AssertionError(f'{key}: no level caption lane: {artist.get_text()}')
    try:
        boxes=_assert_layout(fig,labels,segments+columns)
        for bounds in groups.values():
            x0,y0,x1,y1=bounds
            edges=(((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0)))
            clash = [i for i, box in enumerate(boxes) if any(_segment_box(a, b, box) for a, b in edges)]
            assert not clash, f'group box crosses text: {[labels[i].get_text() for i in clash]}'
        fig.group_gap=spec.get('group_gap',0)
        fig.paint_boxes=spec.get('special') == 'paint'
        marks=_marks(fig,targets,_target_specs(key,spec),boxes,
                     segments+ink+(columns if vbox else []),groups,brackets,vbox)
    except AssertionError as error:
        plt.close(fig)
        raise AssertionError(f'{key} page {page+1}: {error}') from error
    plt.close(fig)
    fig.chart_targets=targets
    return fig,marks


def draw(path, *, key, page=0, display_font=None):
    fig,_marks=layout(key,page)
    fig.savefig(path,dpi=ck.DPI,facecolor=ck.WHITE)
    return path


def audit_pptx(path, charts_dir):
    """Refuse a deck that scales the validated artwork below its contract."""
    import hashlib
    from pathlib import Path
    from pptx import Presentation
    from charts_chapter07 import DATA
    from content_chapter07 import CHAPTER
    placed={s.asset for section in CHAPTER.sections for s in section.slides if isinstance(s,CourseChart)}
    assets={hashlib.sha256((Path(charts_dir)/f'chart-{key}-{page}.png').read_bytes()).hexdigest(): (key,page)
            for key,spec in DATA.items() if key in placed for page in range(len(page_specs(spec)))}
    presentation=Presentation(path)
    found=set()
    for page,slide in enumerate(presentation.slides,1):
        for shape in slide.shapes:
            if shape.shape_type != 13:
                continue
            key=assets.get(hashlib.sha256(shape.image.blob).hexdigest())
            if key is None:
                continue
            found.add(key)
            scale=shape.width/914400/chart_width(DATA[key[0]])
            assert shape.width >= .55*presentation.slide_width, f'Slide {page}: chart is too narrow'
            assert scale >= .999, f'Slide {page}: chart text scaled below validated size'
    assert found==set(assets.values()), 'Missing chart pages in rendered deck'
