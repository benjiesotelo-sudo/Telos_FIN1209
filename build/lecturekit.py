#!/usr/bin/env python3
"""Renderer for the FIN1209 student lecture notes. Knows nothing about any chapter.

Three renderers now live in this repository and they draw three different
documents from the same chapter data:

    deckkit.py    the lecture deck, for the screen
    notekit.py    the teaching plan, for the instructor holding it in class
    lecturekit.py the lecture notes, for a student reading alone afterwards

The lecture notes are the student-facing record of what was discussed: readable
prose, the figures, every term defined once, a summary and the book's review
questions. They carry no timing, no cut tiers, no speaker cues and no slide
numbers. The research behind every one of those decisions, with sources, is
chapter-01/lecture-notes-design.md.

Chapter content is plain data in a module of its own, the same way
content_chapter01.py is plain data for the deck.

Two things are shared with notekit rather than copied: the FEU palette and the
in-page paginator. Everything else here is specific to a single column reading
document.

**Page geometry differs from the teaching plan on purpose.** The plan is a two
column sheet with a 34mm cue rail, because an instructor scans a rail. A
student reads a line, so this is one 160mm column at 10.6pt, which is about 86
characters, inside Butterick's 45 to 90 band.
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
MARGIN_X_MM = 25.0
MARGIN_TOP_MM = 16.0
MARGIN_BOTTOM_MM = 13.0
FOOTER_MM = 10.0

MAIN_MM = PAGE_W_MM - 2 * MARGIN_X_MM                       # 160mm
BODY_H_MM = PAGE_H_MM - MARGIN_TOP_MM - MARGIN_BOTTOM_MM - FOOTER_MM

# 160mm at 10.6pt Arial is about 86 characters: inside Butterick's 45 to 90
# band, and as many words to the line as the measure will carry.
BODY_PT = 10.6

CREDIT = "Lim, The Handbook of Technical Analysis (Wiley, 2016)"


# --------------------------------------------------------------------------
# Blocks
#
# Every block is atomic: the paginator moves it to the next sheet rather than
# splitting it. Prose is the one exception and splits only between its own
# paragraphs, so a figure never lands away from the caption that names it.
# --------------------------------------------------------------------------


@dataclass
class Block:
    pass


@dataclass
class Head(Block):
    """A numbered subsection heading, glued to whatever follows it."""

    number: str = ""      # "1.2"
    text: str = ""


@dataclass
class Para(Block):
    """Body prose. A blank line separates paragraphs."""

    text: str = ""


@dataclass
class Define(Block):
    """A term, defined at the point of first use.

    MIT 14.03 numbers these and Harvard boxes them; both put the definition in
    the flow of the argument rather than in a glossary at the back. The plain
    language gloss and the concrete example belong in the paragraphs around
    this block. What sits inside it is the wording a student should be able to
    reproduce.
    """

    term: str = ""
    text: str = ""


@dataclass
class Panel:
    """One image inside a figure block."""

    number: str = ""      # the book's own figure number, "1.11"
    label: str = ""       # short label under the panel, plates only


@dataclass
class Fig(Block):
    """A figure, or a plate of figures making one argument.

    ``height_mm`` is the height of the artwork band and is the same whether the
    artwork is present or a placeholder stands in its place, so the placeholder
    build and the teaching build paginate identically.
    """

    panels: tuple[Panel, ...] = ()
    caption: str = ""
    cols: int = 1
    height_mm: float = 56.0

    @property
    def numbers(self) -> tuple[str, ...]:
        return tuple(p.number for p in self.panels)

    @property
    def label(self) -> str:
        n = self.numbers
        if len(n) == 1:
            return f"Figure {n[0]}"
        return f"Figures {n[0]} to {n[-1]}"


@dataclass
class Points(Block):
    """A list, used only where the content is genuinely a list."""

    title: str = ""
    items: tuple[str, ...] = ()
    numbered: bool = False


@dataclass
class Quote(Block):
    """One of the quotable definitions students are expected to reproduce."""

    text: str = ""
    source: str = ""


@dataclass
class SelfCheck(Block):
    """The Berkeley CS 70 "Concept check" move: a question in the middle of the
    argument, unassessed, answered by the paragraphs around it."""

    text: str = ""


@dataclass
class Section:
    """One of the deck's six parts. Always starts on a fresh page."""

    number: int = 0
    title: str = ""
    standfirst: str = ""
    blocks: tuple[Block, ...] = ()


@dataclass
class LectureNotes:
    code: str = ""
    course: str = ""
    chapter: str = ""
    title: str = ""
    presenter: str = ""
    term: str = ""
    source_note: str = ""
    orientation: str = ""
    objectives: tuple[str, ...] = ()
    sections: tuple[Section, ...] = ()
    summary: tuple[str, ...] = ()
    review_questions: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()

    def terms(self) -> list[tuple[str, str]]:
        """Every defined term against the subsection it is defined in."""
        found: list[tuple[str, str]] = []
        for s in self.sections:
            where = str(s.number)
            for b in s.blocks:
                if isinstance(b, Head) and b.number:
                    where = b.number
                elif isinstance(b, Define):
                    found.append((b.term, where))
        return found

    def figure_numbers(self) -> list[str]:
        out: list[str] = []
        for s in self.sections:
            for b in s.blocks:
                if isinstance(b, Fig):
                    out.extend(b.numbers)
        return out

    def prose(self) -> str:
        """Everything a figure reference could legitimately be made from.

        Captions are excluded on purpose. A figure whose only mention is its
        own caption has not been referenced by anything.
        """
        parts: list[str] = [self.orientation, *self.objectives,
                            *self.summary, *self.review_questions]
        for s in self.sections:
            parts.append(s.standfirst)
            for b in s.blocks:
                if isinstance(b, (Para, SelfCheck)):
                    parts.append(b.text)
                elif isinstance(b, Points):
                    parts.append(b.title)
                    parts.extend(b.items)
                elif isinstance(b, Define):
                    parts.append(b.text)
                elif isinstance(b, Quote):
                    parts.append(b.text)
        return "\n".join(parts)


# --------------------------------------------------------------------------
# Inline markup. Content is data, so it cannot call the renderer.
#
#   **bold**     the term at first use, and the point of a paragraph
#   `mono`       data, prices, letters
# --------------------------------------------------------------------------


def _inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def _paras(text: str, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return "".join(
        f"<p{c}>{_inline(chunk.strip())}</p>"
        for chunk in text.split("\n\n") if chunk.strip()
    )


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------


def _blk(inner: str, cls: str = "", glue: bool = False,
         split: bool = False) -> str:
    attrs = ' data-glue="1"' if glue else ""
    attrs += ' data-split="1"' if split else ""
    return f'<div class="blk {cls}"{attrs}><div class="main">{inner}</div></div>'


def render_block(b: Block, figures: "FigureFacts") -> str:
    if isinstance(b, Head):
        num = f'<span class="hnum">{html.escape(b.number)}</span>' if b.number else ""
        return _blk(f"<h3>{num}{_inline(b.text)}</h3>", cls="h", glue=True)

    if isinstance(b, Para):
        return _blk(_paras(b.text, "pp"), cls="prose", split=True)

    if isinstance(b, Define):
        return _blk(
            f'<div class="define"><p><span class="dterm">'
            f'{_inline(b.term)}.</span> {_inline(b.text)}</p></div>',
            cls="d",
        )

    if isinstance(b, Points):
        tag = "ol" if b.numbered else "ul"
        title = f'<p class="ltitle">{_inline(b.title)}</p>' if b.title else ""
        items = "".join(f"<li>{_inline(i)}</li>" for i in b.items)
        return _blk(f"{title}<{tag}>{items}</{tag}>", cls="l")

    if isinstance(b, Quote):
        return _blk(
            f'<blockquote class="qq"><p>{_inline(b.text)}</p>'
            f'<p class="qsrc">{_inline(b.source)}</p></blockquote>',
            cls="q",
        )

    if isinstance(b, SelfCheck):
        return _blk(
            f'<div class="scheck"><span class="slabel">Check yourself</span>'
            f'{_paras(b.text)}</div>',
            cls="s",
        )

    if isinstance(b, Fig):
        return _figure_html(b, figures)

    raise TypeError(f"unhandled block {type(b).__name__}")


def _figure_html(f: Fig, figures: "FigureFacts") -> str:
    cells = []
    for p in f.panels:
        art = figures.art(p.number)
        label = (f'<span class="plabel">Figure {html.escape(p.number)}. '
                 f'{_inline(p.label)}</span>') if len(f.panels) > 1 else ""
        cells.append(f'<div class="panel">{art}{label}</div>')

    grid = (f'<div class="figgrid" '
            f'style="grid-template-columns:repeat({f.cols},1fr);'
            f'height:{f.height_mm}mm">{"".join(cells)}</div>')

    # data-float: the paginator lets a figure that will not fit wait for the
    # next sheet rather than leaving the rest of this one blank.
    return (
        f'<div class="blk fig" data-float="1"><div class="main">{grid}'
        f'<p class="figcap"><span class="fignum">{html.escape(f.label)}</span>'
        f'{_inline(f.caption)}'
        f'<span class="figcredit">Reproduced from {html.escape(CREDIT)}</span>'
        f'</p></div></div>'
    )


# --------------------------------------------------------------------------
# Figure facts: what the deck says each figure shows, and where the artwork is
# --------------------------------------------------------------------------


@dataclass
class FigureFacts:
    """Figure descriptions taken from the deck, plus an optional artwork folder.

    The description is never retyped in the lecture content module. It comes
    from content_chapterNN.py, which is the same place the deck's own figure
    placeholder takes it from, so the two can never disagree.
    """

    shows: dict = field(default_factory=dict)      # number -> one line
    files: dict = field(default_factory=dict)      # number -> filename
    directory: Path | None = None

    def path(self, number: str) -> Path | None:
        if self.directory is None:
            return None
        p = self.directory / self.files.get(number, "")
        return p if p.is_file() else None

    def art(self, number: str) -> str:
        p = self.path(number)
        if p is not None:
            # A background image, not an <img>. Inside a flex column whose
            # height comes from the grid row, an <img> with max-height:100%
            # has no definite height to resolve against, so it renders at its
            # natural size and spills over the caption and the paragraph
            # underneath. A background sized to contain cannot overflow.
            return (f'<div class="art" role="img" '
                    f'aria-label="Figure {html.escape(number)}" '
                    f'style="background-image:url({p.resolve().as_uri()})">'
                    f'</div>')
        # No figure number here: the caption below a single figure names it,
        # and a panel inside a plate carries its own label. Printing it in the
        # placeholder as well said "Figure 1.9" twice on the same figure.
        return (f'<div class="art placeholder">'
                f'<span class="phtext">{_inline(self.shows.get(number, ""))}</span>'
                f'<span class="phfoot">Artwork not reproduced in the public '
                f'build</span></div>')

    def placed(self) -> int:
        return sum(1 for n in self.files if self.path(n) is not None)


# --------------------------------------------------------------------------
# The document
# --------------------------------------------------------------------------


def _masthead(n: LectureNotes) -> str:
    return f"""
<div class="blk cover">
  <span class="cov-code">{html.escape(n.code)}  {html.escape(n.course)}</span>
  <h1 class="cov-title">{html.escape(n.chapter)}. {html.escape(n.title)}</h1>
  <p class="cov-sub">Lecture notes  |  {html.escape(n.term)}</p>
  <p class="cov-by">{html.escape(n.presenter)}</p>
</div>"""


def _sheet_head(title: str, kicker: str = "") -> str:
    kick = f'<span class="sheet-kick">{html.escape(kicker)}</span>' if kicker else ""
    return (f'<div class="blk shead">{kick}'
            f'<h2 class="sheet-title">{html.escape(title)}</h2></div>')


def _section_head(s: Section) -> str:
    # data-glue: the opener moves with whatever follows it, so a section can
    # never be announced at the very bottom of a sheet and then start on the
    # next one.
    return f"""
<div class="blk sechead" data-glue="1">
  <span class="sec-kick">Section {s.number}</span>
  <h2 class="sec-title">{html.escape(s.title)}</h2>
  <p class="sec-stand">{_inline(s.standfirst)}</p>
</div>"""


def _back_head(text: str) -> str:
    """A back matter heading. No number: the back matter is not a section."""
    return f"<h3>{html.escape(text)}</h3>"


def _key_terms(n: LectureNotes) -> str:
    rows = "".join(
        f'<li><span class="kt">{_inline(t)}</span>'
        f'<span class="kw">{html.escape(where)}</span></li>'
        for t, where in n.terms()
    )
    return (f'{_back_head("Key terms")}'
            f'<p class="pp">Every term this chapter defines, against the '
            f'subsection that defines it.</p>'
            f'<ul class="terms">{rows}</ul>')


def _css() -> str:
    return f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: #ffffff; }}
body {{
  font-family: {BODY_FONT};
  font-size: {BODY_PT}pt;
  line-height: 1.40;
  color: {INK};
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
code {{ font-family: {MONO_FONT}; font-size: 9.6pt; }}

/* ---- sheets ---------------------------------------------------------- */
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
  padding-top: 1.8mm;
  font-size: 8pt; color: {MUTED};
}}
.page-foot .ff-right {{ font-family: {MONO_FONT}; font-size: 8.4pt; color: {INK}; }}

.blk {{ margin-bottom: 2.3mm; }}
.main {{ width: 100%; }}
.main p {{ margin: 0 0 1.9mm 0; }}
.main p:last-child {{ margin-bottom: 0; }}
.main strong {{ font-weight: 700; }}
.main code {{
  background: rgba(0,122,51,0.07); padding: 0 0.6mm; border-radius: 0.6mm;
}}
p.pp {{ text-align: justify; }}

/* ---- masthead -------------------------------------------------------- */
.cover {{ padding: 0 0 3.0mm 0; border-bottom: 2.4pt solid {GREEN}; margin-bottom: 3.4mm; }}
.cov-code {{
  font-family: {MONO_FONT}; font-size: 9.4pt; color: {GREEN};
  letter-spacing: 0.06em;
}}
.cov-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 24pt;
  color: {GREEN_DEEP}; margin: 1.8mm 0 1.4mm 0; line-height: 1.12;
}}
.cov-sub {{ font-size: 10.5pt; margin: 0 0 1.2mm 0; color: {INK}; }}
.cov-by {{ margin: 0; font-size: 9pt; color: {MUTED}; }}

/* ---- section openers ------------------------------------------------- */
.sechead {{ margin-bottom: 3.6mm; border-bottom: 2.2pt solid {GREEN}; padding-bottom: 1.8mm; }}
.sec-kick {{
  display: block; font-family: {MONO_FONT}; font-size: 9pt; color: {GREEN};
  letter-spacing: 0.10em; margin-bottom: 1.4mm;
}}
.sec-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 20pt;
  color: {GREEN_DEEP}; margin: 0 0 1.8mm 0; line-height: 1.12;
}}
.sec-stand {{ margin: 0; font-size: 10.5pt; color: #3c3c3c; }}

.shead {{ margin-bottom: 4.0mm; border-bottom: 1.8pt solid {GOLD}; padding-bottom: 1.6mm; }}
.sheet-kick {{
  display: block; font-family: {MONO_FONT}; font-size: 8.6pt;
  color: {GREEN}; letter-spacing: 0.09em; margin-bottom: 1.2mm;
}}
.sheet-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 18pt;
  color: {GREEN_DEEP}; margin: 0; line-height: 1.15;
}}

/* ---- subsection headings --------------------------------------------- */
h3 {{
  font-family: {DISPLAY_FONT};
  font-size: 13.5pt; font-weight: 400; color: {GREEN_DEEP};
  margin: 0; line-height: 1.2;
}}
h3 .hnum {{
  font-family: {MONO_FONT}; font-size: 11pt; color: {GREEN};
  margin-right: 2.6mm;
}}
.blk.h {{ margin-top: 3.0mm; margin-bottom: 2.0mm; }}
.rq h3, .kx h3, .src h3 {{ margin-top: 2.2mm; margin-bottom: 1.5mm; }}
.rq h3:first-child, .kx h3:first-child, .src h3:first-child {{ margin-top: 0; }}

/* ---- definitions ------------------------------------------------------ */
/* One compact run-in rather than a labelled card. Forty nine of these sit in
   the chapter, so four millimetres saved on each is four pages saved. */
.define {{
  background: rgba(0,122,51,0.05); border-left: 2.4pt solid {GREEN};
  padding: 1.5mm 2.6mm 1.6mm 2.6mm; border-radius: 0 1mm 1mm 0;
}}
.define p {{ margin: 0 !important; font-size: 10.2pt; }}
.dterm {{ font-weight: 700; color: {GREEN_DEEP}; }}

/* ---- figures ---------------------------------------------------------- */
.blk.fig {{ margin-top: 2.8mm; margin-bottom: 3.2mm; }}
.figgrid {{
  display: grid; gap: 2.6mm; grid-auto-rows: 1fr; overflow: hidden;
}}
.panel {{
  display: flex; flex-direction: column;
  min-height: 0; min-width: 0; overflow: hidden;
}}
.art {{
  flex: 1 1 0; min-height: 0; min-width: 0;
  display: flex; align-items: center; justify-content: center;
  background-color: #ffffff; border: 0.5pt solid {BORDER};
  border-radius: 0.8mm; padding: 1.4mm; overflow: hidden;
  background-repeat: no-repeat; background-position: center center;
  background-size: contain; background-origin: content-box;
}}
.art.placeholder {{
  flex-direction: column; text-align: center; justify-content: center;
  border: 0.8pt dashed {GREEN}; background: rgba(0,122,51,0.035);
  padding: 2.4mm 3mm;
}}
.phtext {{ font-size: 8.6pt; color: #3c3c3c; line-height: 1.32; }}
.phfoot {{
  font-size: 7.2pt; color: {MUTED}; margin-top: 1.6mm;
  letter-spacing: 0.05em; text-transform: uppercase;
}}
.plabel {{
  display: block; font-size: 7.8pt; color: {MUTED}; margin-top: 1.0mm;
  line-height: 1.25;
}}
.figcap {{
  font-size: 8.8pt; color: #3c3c3c; line-height: 1.34;
  margin: 1.6mm 0 0 0 !important;
}}
.fignum {{
  font-family: {MONO_FONT}; font-size: 8.8pt; font-weight: 700;
  color: {GREEN_DEEP}; margin-right: 2.2mm; white-space: nowrap;
}}
.figcredit {{
  display: block; font-size: 7.4pt; color: {MUTED}; margin-top: 0.7mm;
}}

/* ---- quotations ------------------------------------------------------- */
.qq {{
  margin: 0; padding: 0 0 0 4mm; border-left: 2.4pt solid {GOLD};
}}
.qq p {{ font-size: 10.2pt; }}
.qsrc {{ font-size: 8.8pt; color: {MUTED}; margin-top: 1.2mm !important; }}

/* ---- self check ------------------------------------------------------- */
.scheck {{
  background: rgba(242,169,0,0.16); border-radius: 1mm;
  padding: 1.8mm 2.8mm 1.9mm 2.8mm;
}}
.slabel {{
  display: block; font-size: 7.4pt; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: {INK}; margin-bottom: 1.2mm;
}}
.scheck p {{ font-size: 9.9pt; }}

/* ---- lists ------------------------------------------------------------ */
.ltitle {{ font-weight: 700; margin: 0 0 1.4mm 0 !important; }}
.main ul, .main ol {{ margin: 0; padding-left: 6mm; }}
.main li {{ margin-bottom: 1.0mm; }}
.main li:last-child {{ margin-bottom: 0; }}
.main ul {{ list-style: none; padding-left: 4.6mm; }}
.main ul li {{ position: relative; }}
.main ul li::before {{
  content: ""; position: absolute; left: -3.6mm; top: 1.9mm;
  width: 1.5mm; height: 1.5mm; background: {GOLD};
}}
.main ol li::marker {{ color: {GREEN}; font-weight: 700; }}

/* ---- key terms index --------------------------------------------------- */
ul.terms {{
  list-style: none; padding: 0; margin: 0;
  column-count: 2; column-gap: 8mm;
}}
ul.terms li::before {{ content: none; display: none; }}
ul.terms li {{
  display: flex; justify-content: space-between; gap: 3mm;
  break-inside: avoid; margin-bottom: 0.45mm;
  border-bottom: 0.4pt solid {BORDER}; padding-bottom: 0.5mm;
  font-size: 8.9pt; line-height: 1.32;
}}
.kw {{ font-family: {MONO_FONT}; font-size: 8.2pt; color: {GREEN}; }}
"""


def render(notes: LectureNotes, figures: FigureFacts) -> str:
    """Return the complete HTML document."""
    sections: list[str] = []

    front = [
        _masthead(notes),
        _sheet_head("What this chapter is about", "Start here"),
        _blk(_paras(notes.orientation, "pp"), cls="prose", split=True),
        render_block(
            Points(title="After studying this chapter you should be able to:",
                   items=notes.objectives, numbered=True),
            figures,
        ),
        _blk(f'<p class="figcredit">{_inline(notes.source_note)}</p>',
             cls="note"),
    ]
    sections.append(
        f'<section data-footer="{html.escape(notes.chapter)} lecture notes">'
        f'{"".join(front)}</section>'
    )

    for s in notes.sections:
        body = "".join(render_block(b, figures) for b in s.blocks)
        foot = f"{s.number}. {s.title}"
        # data-flow: a section may carry on down the current sheet rather
        # than always opening a fresh one. See the paginator in notekit.
        sections.append(
            f'<section data-flow="1" data-footer="{html.escape(foot)}">'
            f"{_section_head(s)}{body}</section>"
        )

    # The back matter is built as four atomic blocks rather than as headings
    # followed by content. A heading that glues only to the paragraph after it
    # will happily leave its list on the next sheet, which is how the key terms
    # index ended up alone on a page of its own.
    rq = "".join(f"<li>{_inline(q)}</li>" for q in notes.review_questions)
    src = "".join(f"<li>{_inline(x)}</li>" for x in notes.sources)
    back = [
        _sheet_head("Summary", "Chapter 1 in five sentences"),
        render_block(Points(items=notes.summary, numbered=True), figures),
        _blk(f'{_back_head("Review questions")}'
             f'<p class="pp">These are the chapter\'s own review questions. '
             f'Every one is answered somewhere in the six sections above, and '
             f'they are the shape the quiz takes.</p><ol>{rq}</ol>', cls="rq"),
        _blk(_key_terms(notes), cls="kx"),
        _blk(f'{_back_head("Sources")}<ul>{src}</ul>', cls="src"),
    ]
    sections.append(
        f'<section data-flow="1" data-footer="Summary and review">'
        f'{"".join(back)}</section>'
    )

    title = f"{notes.code} {notes.chapter} - Lecture notes"
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

MIN_MEASURE = 45
MAX_MEASURE = 90


def validate(document: str, notes: LectureNotes, deck_figures: dict,
             deck_terms: list[str]) -> list[str]:
    """Refuse to write notes that break the design.

    The three checks that matter are the drift checks. The notes are a second
    document about the same chapter, so the deck is the authority on which
    figures and which terms exist, and the build fails rather than shipping a
    set of notes that has quietly diverged from what was taught.
    """
    problems: list[str] = []

    # 1. Figures the deck does not have.
    numbers = notes.figure_numbers()
    for n in numbers:
        if n not in deck_figures:
            problems.append(
                f"figure {n} is not in the deck. The deck is the authority on "
                "scope; either the number is wrong or the deck no longer "
                "places it."
            )
    dupes = {n for n in numbers if numbers.count(n) > 1}
    for n in sorted(dupes):
        problems.append(f"figure {n} appears in more than one figure block")

    # 2. Figures nothing points at.
    prose = notes.prose()
    for n in sorted(set(numbers)):
        if not re.search(rf"Figure {re.escape(n)}\b", prose):
            problems.append(
                f"figure {n} is never referenced from the prose. A figure no "
                "paragraph mentions is decoration; say what to look at in it."
            )

    # 3. Terms, against the deck, in both directions.
    defined = [t for t, _ in notes.terms()]
    seen = set()
    for t in defined:
        if t in seen:
            problems.append(f"term defined more than once: {t!r}")
        seen.add(t)
    for t in deck_terms:
        if t not in seen:
            problems.append(
                f"the deck teaches {t!r} and the notes never define it"
            )
    for t in sorted(seen - set(deck_terms)):
        problems.append(
            f"the notes define {t!r} and the deck does not teach it"
        )

    # 4. House style.
    for ch, name in BANNED.items():
        if ch in document:
            where = document.find(ch)
            problems.append(
                f"{name} at character {where}: "
                f"{document[max(0, where - 60):where + 60]!r}"
            )

    # 5. Measure.
    chars = MAIN_MM / (BODY_PT * 0.5 * 25.4 / 72)
    if not (MIN_MEASURE <= chars <= MAX_MEASURE):
        problems.append(
            f"main column is about {chars:.0f} characters, outside the "
            f"{MIN_MEASURE} to {MAX_MEASURE} band"
        )

    return problems
