#!/usr/bin/env python3
"""Renderer for the FIN1209 take-home activity. Knows nothing about any chapter.

Four renderers now live in this repository and they draw four documents from
the same course:

    deckkit.py     the lecture deck, for the screen
    notekit.py     the teaching plan, for the instructor holding it in class
    lecturekit.py  the lecture notes, for a student reading alone afterwards
    activitykit.py the take-home activity, for a student at a keyboard

The activity is the only one of the four a student **works through** rather
than reads, and every decision here follows from that. A step is a numbered
instruction with the screen it produces printed underneath it, so a reader who
has never opened a spreadsheet can compare their screen against the page. The
answer spaces are ruled lines, because the sheet is printed and written on.

Two things are shared with notekit rather than copied: the FEU palette and the
in-page paginator. Page geometry is this document's own. The margins are
narrower than the lecture notes' because a 1440 pixel screenshot printed at
170mm is about 215 dots to the inch, and at the lecture notes' 160mm measure
the Google Sheets menu bar stops being readable.

One renderer draws both documents. The worksheet and the answer key are the
same content module rendered twice, with `key=True` turning on the blocks the
students' copy does not carry. Nothing is forked, so an answer cannot drift
from the question it answers.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from pathlib import Path

from notekit import (BODY_FONT, BORDER, DISPLAY_FONT, GOLD, GREEN, GREEN_DEEP,
                     INK, MONO_FONT, MUTED, PAPER, paginator_js)


# --------------------------------------------------------------------------
# Page geometry
# --------------------------------------------------------------------------

PAGE_W_MM = 210.0
PAGE_H_MM = 297.0
MARGIN_X_MM = 20.0
MARGIN_TOP_MM = 14.0
MARGIN_BOTTOM_MM = 12.0
FOOTER_MM = 9.0

MAIN_MM = PAGE_W_MM - 2 * MARGIN_X_MM                       # 170mm
BODY_H_MM = PAGE_H_MM - MARGIN_TOP_MM - MARGIN_BOTTOM_MM - FOOTER_MM

BODY_PT = 10.2

# A captured frame is 1440 by 900. Printed 170mm wide that is 215dpi, which
# is where the Sheets menu bar stops being legible on paper. Anything cropped
# tighter than this prints larger, never smaller.
SHOT_W = 1440
SHOT_H = 900


# --------------------------------------------------------------------------
# Blocks
#
# Every block is atomic: the paginator moves it to the next sheet rather than
# splitting it. Para is the one exception and splits between its paragraphs.
# --------------------------------------------------------------------------


@dataclass
class Block:
    pass


@dataclass
class Head(Block):
    text: str
    number: str = ""
    kicker: str = ""


@dataclass
class Para(Block):
    text: str


@dataclass
class Points(Block):
    items: tuple[str, ...]
    title: str = ""
    numbered: bool = False


@dataclass
class Callout(Block):
    """A boxed aside. `tone` picks the colour of the rule down its left."""
    label: str
    text: str
    tone: str = "green"          # green, gold


@dataclass
class Shot:
    """One committed screenshot, with the crop and the highlight it is placed with.

    `crop` is (left, top, right, bottom) in pixels of the captured 1440 by 900
    frame. `box` is (left, top, width, height) in the same pixel space and is
    drawn as a rectangle so a reader can find a small control. Both are
    applied at build time from the unaltered capture, so the repository holds
    what the screen actually showed and the page holds the part of it the step
    is about.
    """
    name: str
    crop: tuple[int, int, int, int] | None = None
    box: tuple[int, int, int, int] | None = None
    caption: str = ""
    # How much of the measure the picture takes. A crop of a tall, narrow
    # panel printed across the full 170mm is 200mm deep and eats a page, so
    # those are placed smaller. Anything wide stays at 100.
    width_pct: int = 100


@dataclass
class Step(Block):
    """One numbered instruction and the screen it produces.

    `number` is filled in by the build, never typed here, so inserting a step
    cannot leave the sheet counting 4, 5, 5, 6.
    """
    title: str
    text: str = ""
    type_this: str = ""
    then: str = ""
    shot: Shot | None = None
    number: int = 0


@dataclass
class TypeBox(Block):
    """A formula to be typed, outside a numbered step."""
    text: str
    label: str = "Type exactly this"
    intro: str = ""


@dataclass
class Question(Block):
    """One identification question with a ruled space for the answer.

    `cell` names the cell of the student's own sheet that holds the answer, so
    marking is mechanical. `answer` is printed only in the key.
    """
    text: str
    cell: str
    answer: str = ""


@dataclass
class QuestionSet(Block):
    title: str
    intro: str
    questions: tuple[Question, ...]
    key_note: str = ""


@dataclass
class Lines(Block):
    """Ruled writing space, for the answers a formula cannot produce."""
    count: int
    title: str = ""
    intro: str = ""


@dataclass
class Table(Block):
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    widths: tuple[int, ...] = ()
    title: str = ""
    note: str = ""
    # Columns rendered in the mono face. A formula set in the body face is a
    # formula a student will mistype.
    mono_cols: tuple[int, ...] = ()


@dataclass
class Figure(Block):
    """A chart this course drew, from a real file, with its own credit line."""
    path: Path | None
    caption: str
    credit: str
    height_mm: float = 92.0


@dataclass
class KeyOnly(Block):
    """A block that exists only in the instructor's copy."""
    inner: Block


@dataclass
class Section:
    title: str
    blocks: tuple[Block, ...]
    kicker: str = ""
    footer: str = ""
    flow: bool = False


@dataclass
class Activity:
    code: str
    course: str
    chapter: str
    title: str
    subtitle: str
    presenter: str
    points: int
    duration: str
    replaces: str
    source_note: str
    sections: tuple[Section, ...] = ()
    key_sections: tuple[Section, ...] = ()

    def steps(self) -> tuple[Step, ...]:
        out: list[Step] = []
        for s in self.sections:
            for b in s.blocks:
                if isinstance(b, Step):
                    out.append(b)
        return tuple(out)

    def questions(self) -> tuple[Question, ...]:
        out: list[Question] = []
        for s in self.sections + self.key_sections:
            for b in s.blocks:
                if isinstance(b, QuestionSet):
                    out.extend(b.questions)
        return tuple(out)


# --------------------------------------------------------------------------
# Inline markup: **bold**, `code`, and nothing else
# --------------------------------------------------------------------------


def _inline(text: str) -> str:
    out = html.escape(text)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def _paras(text: str, cls: str = "") -> str:
    klass = f' class="{cls}"' if cls else ""
    return "".join(f"<p{klass}>{_inline(p)}</p>"
                   for p in text.split("\n\n") if p.strip())


def _blk(inner: str, cls: str = "", glue: bool = False,
         split: bool = False, float_: bool = False) -> str:
    attrs = ' data-glue="1"' if glue else ""
    attrs += ' data-split="1"' if split else ""
    attrs += ' data-float="1"' if float_ else ""
    return f'<div class="blk {cls}"{attrs}><div class="main">{inner}</div></div>'


# --------------------------------------------------------------------------
# Where the prepared screenshots are
# --------------------------------------------------------------------------


@dataclass
class Shots:
    """The screenshot folder, and the prepared copies the build wrote.

    `prepared` maps a Shot's identity to the file the page should reference.
    `sizes` maps it to that file's pixel size. build_activity.py fills both in;
    nothing here knows how the cropping is done.

    **The size is not decoration.** The paginator measures a block before the
    page is printed, and an `<img>` with no declared height measures zero until
    it loads. That put five steps on one sheet and clipped two of them off the
    bottom, silently. Every picture therefore goes down as a box with a height
    in millimetres, computed from the file's own aspect, which is the same
    thing lecturekit does with the book's figures and for the same reason.
    """
    directory: Path
    prepared: dict = field(default_factory=dict)
    sizes: dict = field(default_factory=dict)

    def height_mm(self, shot: Shot) -> float:
        w, h = self.sizes.get(id(shot), (SHOT_W, SHOT_H))
        return MAIN_MM * (shot.width_pct / 100.0) * (h / w)

    def uri(self, shot: Shot) -> str:
        p = self.prepared.get(id(shot))
        if p is None:
            p = self.directory / f"{shot.name}.png"
        return p.resolve().as_uri()

    def exists(self, shot: Shot) -> bool:
        return (self.directory / f"{shot.name}.png").is_file()


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------


def render_block(b: Block, shots: Shots, key: bool) -> str:
    if isinstance(b, KeyOnly):
        return render_block(b.inner, shots, key) if key else ""

    if isinstance(b, Head):
        num = f'<span class="hnum">{html.escape(b.number)}</span>' if b.number else ""
        kick = (f'<p class="hkick">{_inline(b.kicker)}</p>'
                if b.kicker else "")
        return _blk(f"<h3>{num}{_inline(b.text)}</h3>{kick}", cls="h", glue=True)

    if isinstance(b, Para):
        return _blk(_paras(b.text, "pp"), cls="prose", split=True)

    if isinstance(b, Points):
        tag = "ol" if b.numbered else "ul"
        title = f'<p class="ltitle">{_inline(b.title)}</p>' if b.title else ""
        items = "".join(f"<li>{_inline(i)}</li>" for i in b.items)
        return _blk(f"{title}<{tag}>{items}</{tag}>", cls="l")

    if isinstance(b, Callout):
        return _blk(
            f'<div class="call call-{b.tone}">'
            f'<span class="calllabel">{_inline(b.label)}</span>'
            f'{_paras(b.text)}</div>', cls="c")

    if isinstance(b, Step):
        return _step_html(b, shots)

    if isinstance(b, TypeBox):
        intro = f'<p class="pp">{_inline(b.intro)}</p>' if b.intro else ""
        return _blk(
            f'{intro}<div class="typebox">'
            f'<span class="typelabel">{_inline(b.label)}</span>'
            f'<code class="typed">{html.escape(b.text)}</code></div>',
            cls="tb")

    if isinstance(b, QuestionSet):
        return _questions_html(b, key)

    if isinstance(b, Lines):
        rules = "".join('<div class="rule"></div>' for _ in range(b.count))
        title = f'<p class="ltitle">{_inline(b.title)}</p>' if b.title else ""
        intro = f'<p class="pp">{_inline(b.intro)}</p>' if b.intro else ""
        return _blk(f"{title}{intro}{rules}", cls="w")

    if isinstance(b, Table):
        return _table_html(b)

    if isinstance(b, Figure):
        return _figure_html(b)

    raise TypeError(f"unhandled block {type(b).__name__}")


def _step_html(s: Step, shots: Shots) -> str:
    parts = [f'<p class="steptitle">'
             f'<span class="stepnum">{s.number}</span>'
             f'{_inline(s.title)}</p>']
    if s.text:
        parts.append(_paras(s.text, "pp"))
    if s.type_this:
        parts.append(f'<div class="typebox"><span class="typelabel">Type '
                     f'exactly this</span><code class="typed">'
                     f'{html.escape(s.type_this)}</code></div>')
    if s.then:
        parts.append(_paras(s.then, "pp"))
    if s.shot is not None:
        parts.append(_shot_html(s.shot, shots))
    return _blk("".join(parts), cls="step")


def _shot_html(shot: Shot, shots: Shots) -> str:
    cap = (f'<p class="shotcap">{_inline(shot.caption)}</p>'
           if shot.caption else "")
    return (f'<figure class="shot" style="width:{shot.width_pct}%">'
            f'<div class="shotart" role="img" aria-label="screenshot" '
            f'style="height:{shots.height_mm(shot):.2f}mm;'
            f'background-image:url({shots.uri(shot)})"></div>'
            f"{cap}</figure>")


def _questions_html(q: QuestionSet, key: bool) -> str:
    rows = []
    for i, item in enumerate(q.questions, start=1):
        if key:
            value = f'<span class="ans">{_inline(item.answer)}</span>'
        else:
            value = '<span class="blank"></span>'
        rows.append(
            f'<li><span class="qrow">'
            f'<span class="qtext">{_inline(item.text)}</span>'
            f'<span class="qcell">{html.escape(item.cell)}</span>'
            f'{value}</span></li>')
    note = (f'<p class="keynote">{_inline(q.key_note)}</p>'
            if key and q.key_note else "")
    return _blk(
        f'<p class="ltitle">{_inline(q.title)}</p>'
        f'<p class="pp">{_inline(q.intro)}</p>'
        f'<ol class="qs">{"".join(rows)}</ol>{note}', cls="q")


def _table_html(t: Table) -> str:
    cols = ("".join(f'<col style="width:{w}%">' for w in t.widths)
            if t.widths else "")
    head = "".join(f"<th>{_inline(h)}</th>" for h in t.headers)
    body = "".join(
        "<tr>" + "".join(
            (f'<td class="mono">{html.escape(c)}</td>' if i in t.mono_cols
             else f"<td>{_inline(c)}</td>")
            for i, c in enumerate(row)) + "</tr>"
        for row in t.rows)
    title = f'<p class="ltitle">{_inline(t.title)}</p>' if t.title else ""
    note = f'<p class="tnote">{_inline(t.note)}</p>' if t.note else ""
    return _blk(f'{title}<table><colgroup>{cols}</colgroup>'
                f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
                f"{note}", cls="t")


def _figure_html(f: Figure) -> str:
    # A background image, not an <img>: the same reason lecturekit gives. A
    # box with a definite height cannot spill over the caption beneath it.
    return (f'<div class="blk fig" data-float="1"><div class="main">'
            f'<div class="art" role="img" style="height:{f.height_mm}mm;'
            f'background-image:url({f.path.resolve().as_uri()})"></div>'
            f'<p class="figcap">{_inline(f.caption)}'
            f'<span class="figcredit">{html.escape(f.credit)}</span>'
            f"</p></div></div>")


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------


def _masthead(a: Activity, key: bool) -> str:
    band = ("Answer key and marking guide  |  instructor's copy"
            if key else f"{a.points} points  |  {a.duration}")
    what = "Answer key" if key else "Student worksheet"
    return (
        f'<div class="blk cover"><div class="main">'
        f'<p class="cov-code">{html.escape(a.code)}  {html.escape(a.course)}'
        f'  |  {html.escape(a.chapter)}</p>'
        f'<h1 class="cov-title">{_inline(a.title)}</h1>'
        f'<p class="cov-sub">{_inline(a.subtitle)}</p>'
        f'<p class="cov-band"><span class="cov-what">{html.escape(what)}'
        f'</span><span class="cov-pts">{html.escape(band)}</span></p>'
        f'<p class="cov-by">{_inline(a.presenter)}</p>'
        f"</div></div>")


def _namebar() -> str:
    return (
        '<div class="blk namebar"><div class="main"><table><colgroup>'
        '<col style="width:46%"><col style="width:27%"><col style="width:27%">'
        '</colgroup><tbody><tr>'
        '<td>Name<span class="nb"></span></td>'
        '<td>Section<span class="nb"></span></td>'
        '<td>Date<span class="nb"></span></td>'
        "</tr></tbody></table></div></div>")


def _section_head(s: Section) -> str:
    kick = f'<p class="skick">{_inline(s.kicker)}</p>' if s.kicker else ""
    return (f'<div class="blk sh" data-glue="1"><div class="main">'
            f'<h2>{_inline(s.title)}</h2>{kick}</div></div>')


# --------------------------------------------------------------------------
# CSS
# --------------------------------------------------------------------------


def _css() -> str:
    return f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: #ffffff; }}
body {{
  font-family: {BODY_FONT};
  font-size: {BODY_PT}pt;
  line-height: 1.38;
  color: {INK};
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
code {{ font-family: {MONO_FONT}; font-size: 9.2pt; }}

#source {{ position: absolute; left: -20000mm; top: 0; width: {MAIN_MM}mm; }}
.page {{
  position: relative;
  width: {PAGE_W_MM}mm;
  height: {PAGE_H_MM}mm;
  padding: {MARGIN_TOP_MM}mm {MARGIN_X_MM}mm {MARGIN_BOTTOM_MM}mm {MARGIN_X_MM}mm;
  background: {PAPER};
  overflow: hidden;
  page-break-after: always;
  break-after: page;
}}
.page:last-child {{ page-break-after: auto; break-after: auto; }}
.page-body {{ height: {BODY_H_MM}mm; overflow: hidden; }}
.page-foot {{
  height: {FOOTER_MM}mm;
  display: flex; align-items: flex-end; justify-content: space-between;
  border-top: 0.5pt solid {BORDER};
  padding-top: 1.6mm;
  font-size: 7.8pt; color: {MUTED};
}}
.page-foot .ff-right {{ font-family: {MONO_FONT}; font-size: 8.2pt; color: {INK}; }}

.blk {{ margin-bottom: 2.4mm; }}
.main {{ width: 100%; }}
.main p {{ margin: 0 0 1.8mm 0; }}
.main p:last-child {{ margin-bottom: 0; }}
.main strong {{ font-weight: 700; }}
.main code {{
  background: rgba(0,122,51,0.08); padding: 0 0.6mm; border-radius: 0.6mm;
}}
p.pp {{ text-align: left; }}

/* ---- masthead -------------------------------------------------------- */
.cover {{ padding: 0 0 2.6mm 0; border-bottom: 2.4pt solid {GREEN}; margin-bottom: 3.0mm; }}
.cov-code {{
  font-family: {MONO_FONT}; font-size: 9pt; color: {GREEN};
  letter-spacing: 0.05em; margin: 0 0 1.4mm 0;
}}
.cov-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 23pt;
  color: {GREEN_DEEP}; margin: 0 0 1.4mm 0; line-height: 1.12;
}}
.cov-sub {{ font-size: 10.6pt; margin: 0 0 2.0mm 0; color: {INK}; }}
.cov-band {{
  display: flex; justify-content: space-between; align-items: baseline;
  border-top: 0.5pt solid {BORDER}; border-bottom: 0.5pt solid {BORDER};
  padding: 1.4mm 0; margin: 0 0 1.6mm 0;
}}
.cov-what {{ font-weight: 700; color: {GREEN_DEEP}; }}
.cov-pts {{ font-family: {MONO_FONT}; font-size: 9.2pt; color: {INK}; }}
.cov-by {{ margin: 0; font-size: 8.8pt; color: {MUTED}; }}

.namebar table {{ width: 100%; border-collapse: collapse; }}
.namebar td {{
  padding: 0 3mm 0 0; font-size: 9pt; color: {MUTED};
  vertical-align: bottom;
}}
.namebar .nb {{
  display: block; border-bottom: 0.6pt solid {INK};
  height: 7mm; margin-top: 0.6mm;
}}

/* ---- section and heads ----------------------------------------------- */
.sh {{ margin-top: 1.5mm; margin-bottom: 2.6mm; }}
.sh h2 {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 16.5pt;
  color: {GREEN_DEEP}; margin: 0 0 1.0mm 0; line-height: 1.15;
  border-bottom: 1.6pt solid {GOLD}; padding-bottom: 1.4mm;
}}
.skick {{ margin: 0; font-size: 9.4pt; color: {MUTED}; }}
.h h3 {{
  font-size: 11.2pt; font-weight: 700; color: {GREEN_DEEP};
  margin: 1.0mm 0 0.8mm 0;
}}
.h .hnum {{ font-family: {MONO_FONT}; color: {GREEN}; margin-right: 2mm; }}
.hkick {{ margin: 0; font-size: 9.2pt; color: {MUTED}; }}

/* ---- lists ----------------------------------------------------------- */
.l ul, .l ol {{ margin: 0.4mm 0 0 5mm; padding: 0; }}
.l li {{ margin-bottom: 1.1mm; }}
.ltitle {{ font-weight: 700; color: {GREEN_DEEP}; margin: 0 0 1.2mm 0; }}

/* ---- steps ----------------------------------------------------------- */
.step {{
  border-left: 2.2pt solid {GREEN}; padding: 0 0 1.6mm 4mm;
  margin-bottom: 3.4mm;
}}
.steptitle {{
  font-weight: 700; color: {GREEN_DEEP}; font-size: 10.8pt;
  margin: 0 0 1.4mm 0;
}}
.stepnum {{
  display: inline-block; min-width: 6.4mm; height: 6.4mm; line-height: 6.4mm;
  text-align: center; background: {GREEN}; color: #ffffff;
  border-radius: 3.2mm; font-family: {MONO_FONT}; font-size: 9pt;
  margin-right: 2.6mm; vertical-align: 0.4mm;
}}
.typebox {{
  border: 0.6pt solid {BORDER}; background: #ffffff;
  padding: 1.8mm 2.4mm; margin: 1.6mm 0;
}}
.typelabel {{
  display: block; font-size: 7.6pt; letter-spacing: 0.07em;
  text-transform: uppercase; color: {GREEN}; margin-bottom: 1.0mm;
}}
code.typed {{
  display: block; font-size: 8.6pt; line-height: 1.45; color: {INK};
  word-break: break-all; white-space: pre-wrap; background: none; padding: 0;
}}
figure.shot {{ margin: 1.8mm 0 0 0; }}
figure.shot .shotart {{
  width: 100%;
  background-repeat: no-repeat;
  background-position: top left;
  background-size: 100% 100%;
  background-color: #ffffff;
  border: 0.6pt solid {BORDER};
}}
.shotcap {{
  margin: 1.0mm 0 0 0; font-size: 8.4pt; color: {MUTED}; line-height: 1.3;
}}

/* ---- callouts -------------------------------------------------------- */
.call {{ border-left: 2.2pt solid {GREEN}; padding: 0.6mm 0 0.6mm 3.4mm; }}
.call-gold {{ border-left-color: {GOLD}; }}
.calllabel {{
  display: block; font-size: 7.6pt; letter-spacing: 0.07em;
  text-transform: uppercase; color: {GREEN}; margin-bottom: 0.8mm;
}}
.call-gold .calllabel {{ color: #8a6100; }}

/* ---- questions ------------------------------------------------------- */
.qs {{ margin: 0.6mm 0 0 8mm; padding: 0; }}
.qs li {{ margin-bottom: 1.9mm; }}
.qs li > .qrow {{ display: flex; align-items: baseline; gap: 2mm; }}
.qtext {{ flex: 1 1 auto; }}
.qcell {{
  font-family: {MONO_FONT}; font-size: 8.2pt; color: {GREEN};
  flex: 0 0 auto;
}}
.blank {{
  flex: 0 0 42mm; border-bottom: 0.6pt solid {INK}; height: 3.6mm;
}}
.ans {{ flex: 0 0 42mm; }}
.ans {{
  font-family: {MONO_FONT}; font-size: 9.4pt; font-weight: 700;
  color: {GREEN_DEEP};
  border-bottom: 0.6pt solid {BORDER};
}}
.keynote {{ margin-top: 1.6mm; font-size: 9.2pt; color: {MUTED}; }}

/* ---- ruled writing space --------------------------------------------- */
.rule {{ border-bottom: 0.5pt solid #b9c4bc; height: 7.4mm; }}

/* ---- tables ---------------------------------------------------------- */
.t table {{
  width: 100%; border-collapse: collapse; font-size: 9.2pt;
  background: #ffffff;
}}
.t th {{
  text-align: left; font-size: 8.2pt; letter-spacing: 0.05em;
  text-transform: uppercase; color: #ffffff; background: {GREEN};
  padding: 1.4mm 2mm; font-weight: 700;
}}
.t td {{
  padding: 1.4mm 2mm; border-bottom: 0.5pt solid {BORDER};
  vertical-align: top;
}}
.t tr:last-child td {{ border-bottom: none; }}
.t td.mono {{
  font-family: {MONO_FONT}; font-size: 8.4pt; word-break: break-all;
}}
.tnote {{ margin-top: 1.2mm; font-size: 8.6pt; color: {MUTED}; }}

/* ---- figures --------------------------------------------------------- */
.fig .art {{
  width: 100%; background-repeat: no-repeat; background-position: center;
  background-size: contain; background-color: #ffffff;
  border: 0.6pt solid {BORDER};
}}
.figcap {{
  margin: 1.2mm 0 0 0; font-size: 8.6pt; color: {INK}; line-height: 1.32;
}}
.figcredit {{ display: block; font-size: 7.8pt; color: {MUTED}; margin-top: 0.8mm; }}
"""


# --------------------------------------------------------------------------
# The document
# --------------------------------------------------------------------------


def render(activity: Activity, shots: Shots, key: bool = False) -> str:
    sections: list[str] = []

    front = [_masthead(activity, key)]
    if not key:
        front.append(_namebar())
    sections.append(
        f'<section data-flow="1" data-footer="{html.escape(activity.code)} '
        f'{html.escape(activity.chapter)} activity">{"".join(front)}</section>')

    chosen = activity.sections + (activity.key_sections if key else ())
    for s in chosen:
        body = "".join(render_block(b, shots, key) for b in s.blocks)
        foot = s.footer or s.title
        flow = ' data-flow="1"' if s.flow else ""
        sections.append(
            f'<section{flow} data-footer="{html.escape(foot)}">'
            f'{_section_head(s)}{body}</section>')

    what = "answer key" if key else "worksheet"
    title = f"{activity.code} {activity.chapter} activity - {what}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{_css()}</style>
</head>
<body>
<div id="source">{''.join(sections)}</div>
<div id="pages"></div>
<script>{paginator_js(BODY_H_MM)}</script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# The rules the build enforces
# --------------------------------------------------------------------------

BANNED = {"—": "em dash", "–": "en dash"}


def validate(activity: Activity, shots: Shots) -> list[str]:
    """Refuse to write an activity that cannot be followed.

    The checks that matter are not typographic. They are the ones that catch
    a worksheet a student cannot complete: a step whose screenshot is missing,
    a question with no answer in the key, and a rubric that does not add up to
    the mark the sheet claims to be worth.
    """
    problems: list[str] = []

    for s in activity.sections + activity.key_sections:
        for b in s.blocks:
            inner = b.inner if isinstance(b, KeyOnly) else b
            if isinstance(inner, Step) and inner.shot is not None:
                if not shots.exists(inner.shot):
                    problems.append(
                        f"step \"{inner.title}\" names screenshot "
                        f"{inner.shot.name}.png, which is not in "
                        f"{shots.directory}")

    for q in activity.questions():
        if not q.answer:
            problems.append(
                f"question \"{q.text}\" has no answer, so the key would ship "
                "with a blank in it")

    # Every dash the deck bans, banned here too, for the same reason: the
    # course prints in one voice.
    text = " ".join(_all_text(activity))
    for ch, name in BANNED.items():
        if ch in text:
            problems.append(f"an {name} is in the copy; use a comma or a full "
                            "stop")
    return problems


def _all_text(activity: Activity) -> list[str]:
    out: list[str] = []
    for s in activity.sections + activity.key_sections:
        out.extend([s.title, s.kicker])
        for b in s.blocks:
            b = b.inner if isinstance(b, KeyOnly) else b
            for fname in ("text", "title", "intro", "then", "caption",
                          "label", "note", "kicker", "key_note"):
                v = getattr(b, fname, None)
                if isinstance(v, str):
                    out.append(v)
            for fname in ("items", "questions", "headers"):
                v = getattr(b, fname, None)
                if isinstance(v, tuple):
                    for item in v:
                        if isinstance(item, str):
                            out.append(item)
                        elif isinstance(item, Question):
                            out.extend([item.text, item.answer])
            rows = getattr(b, "rows", None)
            if isinstance(rows, tuple):
                for row in rows:
                    out.extend(str(c) for c in row)
    return out
