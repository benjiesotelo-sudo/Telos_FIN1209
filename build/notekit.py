#!/usr/bin/env python3
"""Renderer for the FIN1209 teaching plan. Knows nothing about any chapter.

The counterpart of deckkit.py: deckkit draws slides, notekit lays out the
printed teaching plan the instructor holds while those slides are on the
screen. The students' lecture notes are a different document with a different
renderer, build/lecturekit.py, which takes the palette and the paginator here
and nothing else. Chapter content is plain data in a module of its own,
exactly as content_chapter01.py is plain data for the deck.

Output is HTML carrying real print CSS, rendered to PDF by headless Chrome in
build_plan.py. The design rationale, with sources, is
chapter-01/teaching-plan-design.md.

Two things in here are worth knowing before changing anything.

**Pagination is done in the page, not by Chrome.** A small script in the
document measures each block and distributes blocks into fixed A4 sheets. Chrome
cannot put a part name and a page number in a running footer on its own, and its
own pagination will happily split a table or strand a heading at the foot of a
sheet. Doing it in the document buys a real running footer, blocks that are
never split, and headings that are always followed by their content.

``paginator_js`` is shared with lecturekit, so it carries three behaviors the
teaching plan deliberately does not use: floated blocks, sections that flow on
rather than opening a fresh sheet, and paragraphs that split between sentences.
All three are opt-in through attributes the plan never sets.

**Slide numbers are resolved against the deck, never typed.** Content refers to
slides by stable key. build_plan.py walks the deck's own chapter data with the
same traversal deckkit.build uses to number slides, and hands the resolved map
in here. A key that does not resolve fails the build, so the plan cannot drift
away from the deck.
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass, field


# --------------------------------------------------------------------------
# The FEU identity, shared with the deck. deckkit.py holds the same values as
# RGBColor triples; these are the CSS spellings of the same palette.
# --------------------------------------------------------------------------

GREEN = "#007A33"        # institution, primary, structure
GREEN_DEEP = "#004F21"   # part numbers, the darkest structural marks
GOLD = "#F2A900"         # the one thing to notice on a page
INK = "#1a1a1a"          # body text
PAPER = "#faf8f2"        # warm page ground
MUTED = "#818181"        # captions, rail text, footers
BORDER = "#d7e0d9"       # soft rules and hairlines

# Marcellus SC is the FEU identity face and is not installed on the build
# machine or the lecture room PCs, so the named serif fallback is what actually
# renders. Same policy and same reason as the deck; see build/README.md.
DISPLAY_FONT = '"Marcellus SC", Palatino, "Palatino Linotype", Georgia, serif'
BODY_FONT = 'Arial, "Helvetica Neue", Helvetica, sans-serif'
MONO_FONT = '"Courier New", Menlo, monospace'

# A4, and the measure computed from it. 210mm less two 18mm margins leaves
# 174mm; a 34mm cue rail and a 6mm gutter leave a 134mm main column, which is
# about 76 characters of 10pt Arial. Butterick wants 45 to 90.
PAGE_W_MM = 210.0
PAGE_H_MM = 297.0
MARGIN_X_MM = 18.0
MARGIN_TOP_MM = 15.0
MARGIN_BOTTOM_MM = 16.0
RAIL_MM = 34.0
GUTTER_MM = 6.0
FOOTER_MM = 11.0

# A flowed section opener needs at least this much of a sheet left, otherwise
# it starts the next one. See the paginator. Section openers are also glued to
# their first block, so this is the coarse guard and not the only one; 66mm
# sits in the middle of a plateau where the lecture notes hold 24 pages at 95
# percent fill, rather than on the edge of one.
SECTION_MIN_MM = 66.0

CONTENT_W_MM = PAGE_W_MM - 2 * MARGIN_X_MM
MAIN_MM = CONTENT_W_MM - RAIL_MM - GUTTER_MM
BODY_H_MM = PAGE_H_MM - MARGIN_TOP_MM - MARGIN_BOTTOM_MM - FOOTER_MM
RAIL_MM_PLUS_GUTTER = RAIL_MM + GUTTER_MM


# --------------------------------------------------------------------------
# Blocks. Every one of these is atomic: the paginator will move it to the next
# sheet rather than split it. Prose is the one exception, and it splits only
# between its own paragraphs.
# --------------------------------------------------------------------------


@dataclass
class Block:
    """Base. ``cue`` is the rail text, and is where slide numbers live."""

    cue: str = ""


@dataclass
class Heading(Block):
    """A heading inside a part or a front-matter sheet.

    Always glued to the block after it, so a heading can never be the last
    thing on a sheet.
    """

    text: str = ""
    sub: str = ""


@dataclass
class Prose(Block):
    """Ordinary teaching notes. Blank line separates paragraphs."""

    text: str = ""


@dataclass
class Flag(Block):
    """A marked point: the kind of thing the Eberly Center calls a marker for
    an important, challenging or counterintuitive point.

    ``kind`` is one of:

    ``trap``      a place students reliably get it wrong. Gold field.
    ``rule``      a standing instruction that holds in every run plan.
    ``evidence``  what the department has actually examined.
    ``fold``      the sentence to say when the slide is cut.
    """

    kind: str = "trap"
    title: str = ""
    text: str = ""


@dataclass
class Board(Block):
    """Something that gets written on the board and left up."""

    title: str = ""
    lines: tuple[str, ...] = ()
    text: str = ""


@dataclass
class CheckCard(Block):
    """A check, at the point in the part where it happens.

    The answer letters and the slide number are resolved from the deck, so this
    carries no data that can drift.
    """

    index: int = 0
    label: str = ""
    text: str = ""


@dataclass
class Table(Block):
    """A table, sized to its content.

    Degani's line-length section is the reason for ``compact``: a wide gap
    between a label and its number invites perceptual misalignment, so tables
    that are mostly short values are set to their content width and left
    aligned rather than stretched across the measure.
    """

    title: str = ""
    headers: tuple[str, ...] = ()
    rows: tuple[tuple[str, ...], ...] = ()
    align: tuple[str, ...] = ()
    compact: bool = True
    note: str = ""
    full: bool = False  # span the rail as well as the main column


@dataclass
class Bullets(Block):
    title: str = ""
    items: tuple[str, ...] = ()
    numbered: bool = False


@dataclass
class Ladder(Block):
    """The triage for one part: Core, the chosen plan, then the cut tiers.

    Sits directly under the masthead because the never-cut material has to be
    the first thing found, which is Degani and Wiener's guideline (10).

    ``plan`` is the row for whichever run plan the instructor is actually
    running, and it names what comes off in this part. The other four rows are
    a classification; this one is an instruction. A plan that exists only in
    the summary table is a plan the instructor cannot see while teaching, and
    the part pages are the pages held in the hand.
    """

    core: str = ""
    plan: str = ""
    reinforcement: str = ""
    enrichment: str = ""
    fold: str = ""


@dataclass
class Spacer(Block):
    height_mm: float = 4.0


# --------------------------------------------------------------------------
# Sheets and parts
# --------------------------------------------------------------------------


@dataclass
class Sheet:
    """Front or back matter. Starts on a fresh page."""

    title: str = ""
    kicker: str = ""
    footer: str = ""
    blocks: tuple[Block, ...] = ()


@dataclass
class FigureRef:
    """A picture in this part, and the shortest plan that still shows it.

    ``kind`` decides which namespace ``number`` is in and how it is named on
    the page. ``fig`` is one of the book's, "1.11". ``chart`` is one this
    course drew, "C", printed as "Chart C". They are listed on separate rows
    of the masthead because they are not the same kind of thing and a run
    plan cuts them for different reasons.
    """

    number: str = ""       # the book's own figure number, or a chart letter
    keep: str = ""         # shortest plan that still shows it, or a note
    kind: str = "fig"      # fig or chart

    @property
    def key(self) -> str:
        return f"{self.kind}:{self.number}"

    @property
    def label(self) -> str:
        return self.number if self.kind == "fig" else f"Chart {self.number}"


@dataclass
class Part:
    """One of the deck's six parts. Always starts on a fresh page."""

    number: int = 0
    title: str = ""
    short: str = ""        # the word used in the deck's progress marker
    minutes: tuple[int, int, int, int] = (0, 0, 0, 0)  # full, long, std, short
    terms: str = ""
    open_line: str = ""
    close_line: str = ""
    figures: tuple[FigureRef, ...] = ()
    ladder: Ladder = field(default_factory=Ladder)
    blocks: tuple[Block, ...] = ()


@dataclass
class Notes:
    course: str = ""
    code: str = ""
    chapter: str = ""
    title: str = ""
    presenter: str = ""
    # What the cover calls this document. Chapter 1 ships a 26 page teaching
    # plan; Chapter 2 ships a three page run card from the same renderer, and
    # the cover has to be able to say which. The default is what the cover
    # used to have hard coded, so Chapter 1 is unaffected.
    doc_kind: str = "teaching plan"
    plans: tuple[str, ...] = ()   # names of the run plans, longest first
    # Which plan this term's session runs, and the hint printed beside it on
    # every part page. The chapter names it, because a plan chosen once at the
    # top of the document is a plan the instructor cannot see in the room.
    plan_row: tuple[str, str] = ("Plan", "")
    front: tuple[Sheet, ...] = ()
    parts: tuple[Part, ...] = ()
    back: tuple[Sheet, ...] = ()


# --------------------------------------------------------------------------
# Inline markup
#
# Content is data, so it cannot call the renderer. Three inline forms are
# understood, and they are resolved before escaping so a resolved value is
# always plain digits or letters:
#
#   {s:fig:1.11}     the deck slide number carrying Figure 1.11
#   {s:check:13}     the slide number of check 13's question slide
#   {s:term:Price}   the slide number of the term slide for Price
#   {s:slide:...}    the slide number of the content slide with that title
#   {s:part:3}       the slide number of Part 3's divider
#   {s:recap:3}      the slide number of Part 3's recap
#   {a:13}           check 13's two answer letters, "BD"
#
#   **bold**         one clause per paragraph, the point of the paragraph
#   `mono`           answer letters, slide numbers, data
# --------------------------------------------------------------------------

_PLACEHOLDER = re.compile(r"\{(s|a):([^}]*)\}")


class Resolver:
    """Maps content's stable slide keys onto the deck's real slide numbers."""

    def __init__(self, slides: dict[str, int], answers: dict[int, str]):
        self._slides = slides
        self._answers = answers
        self.unresolved: list[str] = []

    def slide(self, key: str) -> int | None:
        n = self._slides.get(key)
        if n is None:
            self.unresolved.append(key)
        return n

    def answer(self, index: int) -> str:
        a = self._answers.get(index)
        if a is None:
            self.unresolved.append(f"check:{index}")
            return "??"
        return a

    def substitute(self, text: str) -> str:
        def repl(m: re.Match) -> str:
            kind, arg = m.group(1), m.group(2)
            if kind == "a":
                return self.answer(int(arg))
            n = self.slide(arg)
            return "?" if n is None else str(n)
        return _PLACEHOLDER.sub(repl, text)


def _inline(text: str, res: Resolver) -> str:
    """Resolve placeholders, escape, then apply the two markup forms."""
    text = res.substitute(text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r'<code>\1</code>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def _paras(text: str, res: Resolver) -> str:
    out = []
    for chunk in [c.strip() for c in text.split("\n\n")]:
        if chunk:
            out.append(f"<p>{_inline(chunk, res)}</p>")
    return "".join(out)


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------


def _rail(cue: str, res: Resolver) -> str:
    if not cue:
        return '<div class="rail"></div>'
    return f'<div class="rail">{_inline(cue, res)}</div>'


def _row(cue: str, main: str, res: Resolver, cls: str = "", glue: bool = False,
         atomic: bool = True) -> str:
    attrs = ' data-glue="1"' if glue else ""
    attrs += "" if atomic else ' data-split="1"'
    return (f'<div class="blk {cls}"{attrs}>{_rail(cue, res)}'
            f'<div class="main">{main}</div></div>')


def render_block(b: Block, res: Resolver) -> str:
    if isinstance(b, Heading):
        sub = f'<span class="hsub">{_inline(b.sub, res)}</span>' if b.sub else ""
        return _row(b.cue, f'<h3>{_inline(b.text, res)}{sub}</h3>', res,
                    cls="h", glue=True)

    if isinstance(b, Prose):
        # The only splittable block, and it splits only between paragraphs.
        inner = "".join(
            f'<p class="pp">{_inline(c.strip(), res)}</p>'
            for c in b.text.split("\n\n") if c.strip()
        )
        return _row(b.cue, inner, res, cls="prose", atomic=False)

    if isinstance(b, Flag):
        label = {"trap": "Trap", "rule": "Rule", "evidence": "Examined",
                 "fold": "Fold"}[b.kind]
        title = f'<span class="ftitle">{_inline(b.title, res)}</span>' if b.title else ""
        return _row(
            b.cue,
            f'<div class="flag flag-{b.kind}">'
            f'<span class="flabel">{label}</span>'
            f'<div class="fbody">{title}{_paras(b.text, res)}</div></div>',
            res, cls="f")

    if isinstance(b, Board):
        lines = html.escape("\n".join(b.lines), quote=False)
        after = _paras(b.text, res) if b.text else ""
        title = _inline(b.title, res) if b.title else "Board work"
        return _row(
            b.cue,
            f'<div class="board"><span class="blabel">{title}</span>'
            f'<pre>{lines}</pre></div>{after}',
            res, cls="b")

    if isinstance(b, CheckCard):
        body = (f'<div class="cbody">{_paras(b.text, res)}</div>'
                if b.text.strip() else "")
        return _row(
            b.cue,
            f'<div class="check">'
            f'<div class="chead">'
            f'<span class="cnum">Check {b.index}</span>'
            f'<span class="clabel">{_inline(b.label, res)}</span>'
            f'<span class="cans">{res.answer(b.index)}</span>'
            f'</div>{body}</div>',
            res, cls="c")

    if isinstance(b, Table):
        return _row(b.cue, _table_html(b, res), res,
                    cls="t full" if b.full else "t")

    if isinstance(b, Bullets):
        tag = "ol" if b.numbered else "ul"
        title = f'<p class="btitle">{_inline(b.title, res)}</p>' if b.title else ""
        items = "".join(f"<li>{_inline(i, res)}</li>" for i in b.items)
        return _row(b.cue, f"{title}<{tag}>{items}</{tag}>", res, cls="l")

    if isinstance(b, Ladder):
        return _ladder_html(b, res)

    if isinstance(b, Spacer):
        return f'<div class="blk sp" style="height:{b.height_mm}mm"></div>'

    raise TypeError(f"unhandled block {type(b).__name__}")


def _table_html(t: Table, res: Resolver) -> str:
    align = t.align or tuple("l" for _ in t.headers)
    head = "".join(
        f'<th class="a{align[i]}">{_inline(h, res)}</th>'
        for i, h in enumerate(t.headers)
    )
    body = []
    for r in t.rows:
        cells = "".join(
            f'<td class="a{align[i] if i < len(align) else "l"}">'
            f'{_inline(c, res)}</td>'
            for i, c in enumerate(r)
        )
        body.append(f"<tr>{cells}</tr>")
    title = f'<p class="ttitle">{_inline(t.title, res)}</p>' if t.title else ""
    note = f'<p class="tnote">{_inline(t.note, res)}</p>' if t.note else ""
    cls = "tbl compact" if t.compact else "tbl"
    return (f'{title}<table class="{cls}"><thead><tr>{head}</tr></thead>'
            f"<tbody>{''.join(body)}</tbody></table>{note}")


# The name and the hint on the plan row come from Notes.plan_row, so the
# ladder does not have to know which plan this term's session runs.
_TIERS = (
    ("core", "Core", "Never cut"),
    ("plan", "", ""),
    ("reinf", "Reinforcement", "Cut when short"),
    ("enrich", "Enrichment", "Cut first"),
    ("fold", "Fold", "Say it, do not show it"),
)


def _ladder_html(l: Ladder, res: Resolver, plan_row=("Plan", "")) -> str:
    values = {"core": l.core, "plan": l.plan, "reinf": l.reinforcement,
              "enrich": l.enrichment, "fold": l.fold}
    rows = []
    for key, name, hint in _TIERS:
        if key == "plan":
            name, hint = plan_row
        text = values[key]
        if not text:
            text = "None."
        rows.append(
            f'<tr class="lad-{key}">'
            f'<th><span class="tier tier-{key}">{name}</span>'
            f'<span class="tierhint">{hint}</span></th>'
            f'<td>{_inline(text, res)}</td></tr>'
        )
    return (f'<div class="blk lad full" data-glue="0">'
            f'<table class="ladder"><tbody>{"".join(rows)}</tbody></table>'
            f'</div>')


# --------------------------------------------------------------------------
# Mastheads
# --------------------------------------------------------------------------


def _masthead(p: Part, res: Resolver, plans: tuple[str, ...],
              deck: "DeckFacts") -> str:
    first = res.slide(f"part:{p.number}")
    last = res.slide(f"recap:{p.number}")
    span = f"Slides {first} to {last}"
    n_slides = (last - first + 1) if (first and last) else 0

    cells = "".join(
        f'<div class="tcell">'
        f'<span class="tplan">{html.escape(name)}</span>'
        f'<span class="tmin">{p.minutes[i]}</span>'
        f'<span class="tunit">min</span></div>'
        for i, name in enumerate(plans)
    )

    checks = deck.checks_in_part(p.number)
    if checks:
        chips = "".join(
            f'<span class="cchip"><b>{i}</b>'
            f'<span class="cchip-a">{res.answer(i)}</span>'
            f'<span class="cchip-s">s{res.slide(f"check:{i}")}</span></span>'
            for i in checks
        )
    else:
        chips = '<span class="none">none in this part</span>'

    def _chips(refs) -> str:
        if not refs:
            return '<span class="none">none in this part</span>'
        return "".join(
            f'<span class="fchip"><b>{html.escape(f.label)}</b>'
            f'<span class="fchip-s">s{res.slide(f.key)}</span>'
            f'<span class="fchip-k">{html.escape(f.keep)}</span></span>'
            for f in refs
        )

    figs = _chips([f for f in p.figures if f.kind == "fig"])
    ours = [f for f in p.figures if f.kind == "chart"]
    # The charts row is printed only where there are charts, so the five parts
    # that have none do not gain an empty row saying so.
    charts_row = (
        f'<div class="mrow"><span class="mkey">Charts</span>'
        f'<span class="mval">{_chips(ours)}</span></div>' if ours else "")

    return f"""
<div class="blk mast full">
  <div class="mast-top">
    <span class="mast-kick">Part {p.number} of 6</span>
    <span class="mast-span">{span}</span>
  </div>
  <h2 class="mast-title">{html.escape(p.title)}</h2>
  <p class="mast-marker">Progress marker on screen reads
     <code>Part {p.number} of 6 - {html.escape(p.short)}</code>,
     {n_slides} slides including the divider and the recap.</p>
  <div class="timing">{cells}</div>
  <div class="mast-rows">
    <div class="mrow"><span class="mkey">Checks</span>
      <span class="mval">{chips}</span></div>
    <div class="mrow"><span class="mkey">Figures</span>
      <span class="mval">{figs}</span></div>
    {charts_row}
    <div class="mrow"><span class="mkey">Open</span>
      <span class="mval mtext">{_inline(p.open_line, res)}</span></div>
    <div class="mrow"><span class="mkey">Close</span>
      <span class="mval mtext">{_inline(p.close_line, res)}</span></div>
    <div class="mrow"><span class="mkey">Terms</span>
      <span class="mval mtext dim">{_inline(p.terms, res)}</span></div>
  </div>
</div>"""


def _sheet_head(s: Sheet, res: Resolver) -> str:
    # Kickers carry slide references too, so they go through the resolver like
    # everything else. They did not, once, and a raw {s:slide:...} placeholder
    # printed on the page. That is what looking at every page is for.
    kick = (f'<span class="sheet-kick">{_inline(s.kicker, res)}</span>'
            if s.kicker else "")
    return (f'<div class="blk shead full">{kick}'
            f'<h2 class="sheet-title">{_inline(s.title, res)}</h2></div>')


def _cover(n: Notes, deck: "DeckFacts") -> str:
    return f"""
<div class="blk cover full">
  <span class="cov-code">{html.escape(n.code)}  {html.escape(n.course)}</span>
  <h1 class="cov-title">{html.escape(n.chapter)} {html.escape(n.doc_kind)}</h1>
  <p class="cov-sub">{html.escape(n.title)}</p>
  <div class="cov-facts">
    <span><b>{deck.total_slides}</b> slides</span>
    <span><b>{deck.total_checks}</b> checks, {deck.total_checks * 2} items</span>
    <span><b>{deck.total_figures}</b> figures</span>
    <span><b>{deck.total_charts}</b> charts</span>
    <span><b>6</b> parts</span>
  </div>
  <p class="cov-by">{html.escape(n.presenter)}</p>
</div>"""


# --------------------------------------------------------------------------
# Deck facts, computed from the deck's own content by build_plan.py
# --------------------------------------------------------------------------


@dataclass
class DeckFacts:
    total_slides: int = 0
    total_checks: int = 0
    total_figures: int = 0
    total_charts: int = 0     # the charts this course drew for itself
    part_checks: dict = field(default_factory=dict)   # part number -> [indices]

    def checks_in_part(self, number: int) -> list[int]:
        return self.part_checks.get(number, [])


# --------------------------------------------------------------------------
# The document
# --------------------------------------------------------------------------


def _css() -> str:
    return f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: #ffffff; }}
body {{
  font-family: {BODY_FONT};
  font-size: 10pt;
  line-height: 1.40;
  color: {INK};
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
code {{ font-family: {MONO_FONT}; font-size: 9.2pt; }}

/* ---- sheets ---------------------------------------------------------- */
#source {{ position: absolute; left: -20000mm; top: 0; width: {CONTENT_W_MM}mm; }}
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
  font-size: 7.6pt; color: {MUTED};
}}
.page-foot .ff-left {{ letter-spacing: 0.04em; }}
.page-foot .ff-right {{ font-family: {MONO_FONT}; font-size: 8pt; color: {INK}; }}

/* ---- the rail and the main column ------------------------------------ */
.blk {{ display: flex; align-items: flex-start; margin-bottom: 2.6mm; }}
.blk.full {{ display: block; }}
/* full means span the rail as well, so the inner column has to give up its
   fixed width too. Without this a full block only moved its cue above the
   content and left the content itself at the main column's 120mm. */
.blk.full .main {{ width: 100%; }}
.rail {{
  flex: 0 0 {RAIL_MM}mm; width: {RAIL_MM}mm;
  margin-right: {GUTTER_MM}mm;
  font-family: {MONO_FONT};
  font-size: 8.2pt; line-height: 1.30;
  color: {GREEN}; text-transform: none;
  padding-top: 0.5mm;
}}
.rail code {{ font-size: 8.2pt; }}
.main {{ flex: 1 1 auto; min-width: 0; width: {MAIN_MM}mm; }}
.main p {{ margin: 0 0 2.0mm 0; }}
.main p:last-child {{ margin-bottom: 0; }}
.main strong {{ font-weight: 700; }}
.main code {{
  background: rgba(0,122,51,0.07); padding: 0 0.6mm; border-radius: 0.6mm;
}}

/* ---- headings -------------------------------------------------------- */
h3 {{
  font-family: {DISPLAY_FONT};
  font-size: 13pt; font-weight: 400; color: {GREEN_DEEP};
  margin: 0; padding-bottom: 1.1mm;
  border-bottom: 1pt solid {BORDER};
  line-height: 1.2;
}}
h3 .hsub {{
  display: block; font-family: {BODY_FONT}; font-size: 8.4pt;
  color: {MUTED}; margin-top: 0.8mm; line-height: 1.3;
}}
.blk.h {{ margin-top: 2.0mm; margin-bottom: 2.6mm; }}

/* ---- cover ----------------------------------------------------------- */
.cover {{ padding: 0 0 3mm 0; border-bottom: 2.2pt solid {GREEN}; }}
.cov-code {{
  font-family: {MONO_FONT}; font-size: 9pt; color: {GREEN};
  letter-spacing: 0.06em;
}}
.cov-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 23pt;
  color: {GREEN_DEEP}; margin: 1.4mm 0 1.0mm 0; line-height: 1.1;
}}
.cov-sub {{ font-size: 10.5pt; margin: 0 0 2.8mm 0; color: {INK}; }}
.cov-facts {{ display: flex; gap: 7mm; font-size: 9.5pt; color: {MUTED}; }}
.cov-facts b {{
  font-family: {MONO_FONT}; font-size: 11pt; color: {GREEN_DEEP};
  margin-right: 0.8mm;
}}
.cov-by {{ margin: 2.4mm 0 0 0; font-size: 8.6pt; color: {MUTED}; }}

/* ---- sheet heads ----------------------------------------------------- */
.shead {{ margin-bottom: 3.2mm; border-bottom: 1.6pt solid {GOLD}; padding-bottom: 1.4mm; }}
.sheet-kick {{
  display: block; font-family: {MONO_FONT}; font-size: 8.2pt;
  color: {GREEN}; letter-spacing: 0.08em; margin-bottom: 1.0mm;
}}
.sheet-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 17.5pt;
  color: {GREEN_DEEP}; margin: 0; line-height: 1.15;
}}

/* ---- part masthead: the two second band ------------------------------ */
.mast {{ margin-bottom: 4mm; }}
.mast-top {{
  display: flex; justify-content: space-between; align-items: baseline;
  border-bottom: 2.2pt solid {GREEN}; padding-bottom: 1.2mm;
}}
.mast-kick {{
  font-family: {MONO_FONT}; font-size: 9pt; color: {GREEN};
  letter-spacing: 0.08em;
}}
.mast-span {{ font-family: {MONO_FONT}; font-size: 10.5pt; color: {GREEN_DEEP}; font-weight: 700; }}
.mast-title {{
  font-family: {DISPLAY_FONT}; font-weight: 400; font-size: 22pt;
  color: {GREEN_DEEP}; margin: 2.2mm 0 1.0mm 0; line-height: 1.1;
}}
.mast-marker {{ margin: 0 0 3.0mm 0; font-size: 8.6pt; color: {MUTED}; }}
.mast-marker code {{ font-size: 8.2pt; color: {INK}; }}

.timing {{ display: flex; gap: 1.6mm; margin-bottom: 3.0mm; }}
.tcell {{
  flex: 1 1 0; border: 0.8pt solid {BORDER}; background: #ffffff;
  padding: 1.6mm 2mm 1.8mm 2mm; text-align: center;
}}
.tplan {{
  display: block; font-size: 7.4pt; letter-spacing: 0.10em;
  text-transform: uppercase; color: {MUTED}; margin-bottom: 0.6mm;
}}
.tmin {{
  font-family: {MONO_FONT}; font-size: 18pt; font-weight: 700;
  color: {GREEN_DEEP}; line-height: 1;
}}
.tunit {{ font-size: 7.4pt; color: {MUTED}; margin-left: 0.8mm; }}

.mast-rows {{ border-top: 0.5pt solid {BORDER}; }}
.mrow {{
  display: flex; align-items: baseline; gap: {GUTTER_MM}mm;
  border-bottom: 0.5pt solid {BORDER}; padding: 1.4mm 0;
}}
.mkey {{
  flex: 0 0 {RAIL_MM}mm; font-size: 7.6pt; letter-spacing: 0.10em;
  text-transform: uppercase; color: {MUTED};
}}
.mval {{ flex: 1 1 auto; min-width: 0; }}
.mval.mtext {{ font-size: 9.4pt; }}
.mval.dim {{ color: #4a4a4a; font-size: 8.8pt; }}
.none {{ color: {MUTED}; font-size: 8.8pt; }}

.cchip, .fchip {{
  display: inline-block; margin: 0 2.4mm 0 0; white-space: nowrap;
  font-family: {MONO_FONT}; font-size: 8.6pt;
}}
.cchip b {{
  background: {GREEN}; color: #ffffff; padding: 0.3mm 1.1mm;
  border-radius: 0.7mm; font-weight: 700;
}}
.cchip-a {{
  background: {GOLD}; color: {INK}; padding: 0.3mm 1.1mm;
  border-radius: 0.7mm; font-weight: 700; margin-left: 0.5mm;
}}
.cchip-s, .fchip-s {{ color: {MUTED}; margin-left: 0.8mm; }}
.fchip b {{ color: {GREEN_DEEP}; font-weight: 700; }}
.fchip-k {{ color: {MUTED}; margin-left: 0.8mm; font-family: {BODY_FONT}; font-size: 7.8pt; }}

/* ---- ladder ---------------------------------------------------------- */
.lad {{ margin-bottom: 4mm; }}
table.ladder {{ width: 100%; border-collapse: collapse; }}
table.ladder th {{
  width: {RAIL_MM_PLUS_GUTTER}mm; text-align: left; vertical-align: top;
  padding: 1.6mm {GUTTER_MM}mm 1.6mm 0; border-top: 0.5pt solid {BORDER};
}}
table.ladder td {{
  vertical-align: top; padding: 1.6mm 0; border-top: 0.5pt solid {BORDER};
  font-size: 9.2pt;
}}
table.ladder tr:last-child th, table.ladder tr:last-child td {{
  border-bottom: 0.5pt solid {BORDER};
}}
.tier {{
  display: inline-block; font-size: 8pt; font-weight: 700;
  letter-spacing: 0.06em; text-transform: uppercase;
  padding: 0.6mm 1.6mm; border-radius: 0.8mm;
}}
.tier-core {{ background: {GREEN}; color: #ffffff; }}
/* The plan row is the one instruction among four classifications, so it is
   the one chip that is neither green structure nor a gold marker. */
.tier-plan {{ background: {GREEN_DEEP}; color: #ffffff; }}
.tier-reinf {{ background: {GOLD}; color: {INK}; }}
.tier-enrich {{ background: #ffffff; color: {MUTED}; border: 0.8pt solid {BORDER}; }}
.tier-fold {{ background: #ffffff; color: {GREEN_DEEP}; border: 0.8pt solid {GREEN}; }}
.tierhint {{ display: block; font-size: 7.4pt; color: {MUTED}; margin-top: 0.8mm; }}

/* ---- flags ----------------------------------------------------------- */
.flag {{ display: flex; align-items: stretch; }}
.flabel {{
  flex: 0 0 auto; align-self: flex-start;
  font-size: 7.4pt; font-weight: 700; letter-spacing: 0.10em;
  text-transform: uppercase; padding: 0.9mm 1.8mm; margin-right: 2.4mm;
  border-radius: 0.8mm; white-space: nowrap;
}}
.fbody {{ flex: 1 1 auto; min-width: 0; }}
.ftitle {{ display: block; font-weight: 700; margin-bottom: 1.4mm; }}
/* Degani rule 15: black over yellow. The one field color under body text. */
.flag-trap {{ background: {GOLD}; padding: 2.2mm 2.6mm; border-radius: 1mm; }}
.flag-trap .flabel {{ background: {INK}; color: {GOLD}; }}
.flag-rule {{
  background: #ffffff; border: 0.8pt solid {GREEN}; border-left-width: 2.4pt;
  padding: 2.2mm 2.6mm; border-radius: 1mm;
}}
.flag-rule .flabel {{ background: {GREEN}; color: #ffffff; }}
.flag-evidence {{
  background: transparent; border-left: 2.4pt solid {GREEN_DEEP};
  padding: 0.6mm 0 0.6mm 2.6mm;
}}
.flag-evidence .flabel {{ background: {GREEN_DEEP}; color: #ffffff; }}
.flag-fold {{
  background: #ffffff; border: 0.8pt dashed {GREEN}; padding: 2.2mm 2.6mm;
  border-radius: 1mm;
}}
.flag-fold .flabel {{ background: #ffffff; color: {GREEN_DEEP}; border: 0.8pt solid {GREEN}; }}

/* ---- board ----------------------------------------------------------- */
.board {{
  background: #ffffff; border: 0.8pt solid {BORDER}; border-radius: 1mm;
  padding: 2.0mm 2.6mm 2.4mm 2.6mm; margin-bottom: 2.0mm;
}}
.blabel {{
  display: block; font-size: 7.4pt; font-weight: 700; letter-spacing: 0.10em;
  text-transform: uppercase; color: {GREEN}; margin-bottom: 1.4mm;
}}
.board pre {{
  font-family: {MONO_FONT}; font-size: 9.4pt; line-height: 1.42;
  margin: 0; white-space: pre; color: {INK};
}}

/* ---- checks ---------------------------------------------------------- */
.check {{ border: 0.8pt solid {GREEN}; border-radius: 1mm; overflow: hidden; }}
.chead {{
  display: flex; align-items: center; gap: 2.4mm;
  background: {GREEN}; padding: 1.4mm 2.4mm;
}}
.cnum {{
  font-family: {MONO_FONT}; font-size: 9.4pt; font-weight: 700; color: #ffffff;
  letter-spacing: 0.04em;
}}
.clabel {{ flex: 1 1 auto; font-size: 9pt; color: #ffffff; }}
.cans {{
  font-family: {MONO_FONT}; font-size: 11pt; font-weight: 700;
  background: {GOLD}; color: {INK}; padding: 0.5mm 2.0mm; border-radius: 0.8mm;
  letter-spacing: 0.10em;
}}
.cbody {{ padding: 2.0mm 2.4mm; font-size: 9.4pt; }}
.cbody p:last-child {{ margin-bottom: 0; }}

/* ---- tables ---------------------------------------------------------- */
.ttitle {{
  font-size: 8pt; letter-spacing: 0.08em; text-transform: uppercase;
  color: {MUTED}; margin: 0 0 1.4mm 0;
}}
table.tbl {{ border-collapse: collapse; font-size: 9.2pt; }}
/* Degani 3.7: keep the label next to its value, do not stretch the gap. */
table.tbl.compact {{ width: auto; }}
table.tbl:not(.compact) {{ width: 100%; }}
table.tbl th {{
  text-align: left; font-size: 7.8pt; letter-spacing: 0.07em;
  text-transform: uppercase; color: {MUTED}; font-weight: 700;
  border-bottom: 1pt solid {GREEN}; padding: 0 4mm 1.1mm 0; white-space: nowrap;
}}
table.tbl td {{
  padding: 1.0mm 4mm 1.0mm 0; border-bottom: 0.5pt solid {BORDER};
  vertical-align: top;
}}
table.tbl th:last-child, table.tbl td:last-child {{ padding-right: 0; }}
table.tbl .ar {{ text-align: right; }}
table.tbl .ac {{ text-align: center; }}
table.tbl .an {{ text-align: right; font-family: {MONO_FONT}; white-space: nowrap; }}
table.tbl tr.rule-row td {{ border-top: 1pt solid {GREEN}; font-weight: 700; }}
.tnote {{ font-size: 8.4pt; color: {MUTED}; margin: 1.4mm 0 0 0; }}

/* ---- lists ----------------------------------------------------------- */
.btitle {{ font-weight: 700; margin: 0 0 1.2mm 0; }}
.main ul, .main ol {{ margin: 0; padding-left: 5mm; }}
.main li {{ margin-bottom: 1.2mm; }}
.main li:last-child {{ margin-bottom: 0; }}
.main ul {{ list-style: none; padding-left: 4mm; }}
.main ul li {{ position: relative; }}
.main ul li::before {{
  content: ""; position: absolute; left: -3.4mm; top: 1.7mm;
  width: 1.4mm; height: 1.4mm; background: {GOLD};
}}
"""


def paginator_js(body_h_mm: float) -> str:
    """The in-page paginator, parameterized by the sheet's body height.

    Shared with build/lecturekit.py, which lays out the student lecture notes
    on the same machinery with a different page geometry. Keep it here: there
    is one paginator in this repository and both documents use it.
    """
    return f"""
(function () {{
  var MM = 1 / 25.4;
  var src = document.getElementById('source');
  var out = document.getElementById('pages');
  var probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;width:100mm;height:100mm;left:-30000mm;';
  document.body.appendChild(probe);
  var PX_PER_MM = probe.getBoundingClientRect().height / 100;
  document.body.removeChild(probe);
  var BODY_H = {body_h_mm} * PX_PER_MM;

  var page = null, body = null, footer = null;

  // How much of a sheet a flowed section opener needs before it is worth
  // starting there rather than on the next sheet.

  function newPage(footerText) {{
    page = document.createElement('div');
    page.className = 'page';
    body = document.createElement('div');
    body.className = 'page-body';
    footer = document.createElement('div');
    footer.className = 'page-foot';
    footer.innerHTML = '<span class="ff-left"></span><span class="ff-right"></span>';
    page.appendChild(body);
    page.appendChild(footer);
    out.appendChild(page);
    footer.querySelector('.ff-left').textContent = footerText;
    return page;
  }}

  function overflows() {{ return body.scrollHeight > Math.ceil(BODY_H); }}

  // How much of the current sheet the blocks on it actually occupy.
  function used() {{
    var last = body.lastElementChild;
    if (!last) return 0;
    return last.getBoundingClientRect().bottom
           - body.getBoundingClientRect().top;
  }}

  // Break a paragraph into sentence sized pieces without disturbing the
  // markup inside it: text nodes are cut after a sentence ending, elements
  // move whole.
  function explode(p) {{
    var out = [];
    var kids = Array.prototype.slice.call(p.childNodes);
    for (var i = 0; i < kids.length; i++) {{
      var n = kids[i];
      p.removeChild(n);
      if (n.nodeType === 3) {{
        var parts = n.nodeValue.split(/(?<=[.?!]\s)/);
        for (var j = 0; j < parts.length; j++) {{
          if (parts[j]) out.push(document.createTextNode(parts[j]));
        }}
      }} else {{
        out.push(n);
      }}
    }}
    return out;
  }}

  // Try to place a node. Returns true when it landed on the current page.
  function place(node) {{
    body.appendChild(node);
    if (!overflows()) return true;
    body.removeChild(node);
    return false;
  }}

  var sections = src.querySelectorAll('section');
  var overflowed = [];

  for (var si = 0; si < sections.length; si++) {{
    var sec = sections[si];
    var foot = sec.getAttribute('data-footer') || '';
    var deferred = [];
    var sinceDefer = 0;

    // A block marked data-float="1" that will not fit at the foot of a sheet
    // waits instead of forcing a page break, and the blocks after it fill the
    // space it could not use. It is then laid down at the top of the next
    // sheet. Without this a tall figure leaves the rest of its page empty,
    // which cost the lecture notes six pages of white paper. Only the lecture
    // notes mark blocks this way; the teaching plan floats nothing.
    function drain(fresh) {{
      if (fresh) newPage(foot);
      while (deferred.length) {{
        var d = deferred[0];
        if (place(d)) {{ deferred.shift(); continue; }}
        if (!body.firstChild) {{
          body.appendChild(d); overflowed.push(d); deferred.shift(); continue;
        }}
        newPage(foot);
      }}
      sinceDefer = 0;
    }}
    function turnPage() {{ drain(true); }}

    // A section normally opens a fresh sheet. A section marked data-flow="1"
    // may instead carry on down the current one, so long as enough of the
    // sheet is left to be worth it. The teaching plan flows nothing: an
    // instructor turns to a part and expects it at the top of a page. The
    // lecture notes flow, because six forced breaks in a document this size
    // were costing four pages of white paper and stranding single paragraphs
    // on sheets of their own.
    var flow = sec.getAttribute('data-flow') === '1';
    // Not scrollHeight: on an underfull sheet that returns the height of the
    // box, not the height of what is in it, so the sheet always looks full.
    var room = page ? BODY_H - used() : 0;
    if (!flow || page === null || room < {SECTION_MIN_MM} * PX_PER_MM) {{
      newPage(foot);
    }} else {{
      footer.querySelector('.ff-left').textContent = foot;
    }}
    var blocks = Array.prototype.slice.call(sec.children);

    for (var bi = 0; bi < blocks.length; bi++) {{
      var blk = blocks[bi];
      var glued = blk.getAttribute('data-glue') === '1' && bi + 1 < blocks.length;

      if (glued) {{
        // A heading and the block after it move together, so a heading can
        // never be stranded at the foot of a sheet.
        var next = blocks[bi + 1];
        if (place(blk)) {{
          if (place(next)) {{ bi++; continue; }}
          body.removeChild(blk);
        }}
        turnPage();
        place(blk);
        if (!place(next)) {{ body.appendChild(next); overflowed.push(next); }}
        bi++;
        continue;
      }}

      if (place(blk)) {{
        // A float cannot drift far from the paragraph that refers to it.
        if (deferred.length && ++sinceDefer >= 6) turnPage();
        continue;
      }}

      // Only defer when enough blocks follow to fill the space the float
      // gave up. Deferring the last figure in a section strands it alone on a
      // sheet, which is worse than the gap it was avoiding.
      if (blk.getAttribute('data-float') === '1' && deferred.length < 2
          && bi + 3 < blocks.length) {{
        deferred.push(blk);
        sinceDefer = 0;
        continue;
      }}

      // Splittable prose splits between its own paragraphs, and, when it is
      // a single paragraph with nowhere else to break, between its sentences.
      // Without the second case the last paragraph of a part lands alone on a
      // sheet of its own, which is what put one sentence on page 23.
      if (blk.getAttribute('data-split') === '1') {{
        var main = blk.querySelector('.main');
        var paras = Array.prototype.slice.call(main.children);

        if (paras.length === 1) {{
          var solo = blk.cloneNode(true);
          var soloP = solo.querySelector('.main').children[0];
          var pieces = explode(soloP);
          if (pieces.length > 1) {{
            body.appendChild(solo);
            var took = 0;
            for (var k = 0; k < pieces.length; k++) {{
              soloP.appendChild(pieces[k]);
              if (overflows()) {{ soloP.removeChild(pieces[k]); break; }}
              took++;
            }}
            if (took > 0 && took < pieces.length) {{
              turnPage();
              var rest = blk.cloneNode(true);
              var restP = rest.querySelector('.main').children[0];
              while (restP.firstChild) restP.removeChild(restP.firstChild);
              for (var m = took; m < pieces.length; m++) restP.appendChild(pieces[m]);
              if (!place(rest)) {{ body.appendChild(rest); overflowed.push(rest); }}
              continue;
            }}
            body.removeChild(solo);
          }}
        }}

        if (paras.length > 1) {{
          var head = blk.cloneNode(true);
          var headMain = head.querySelector('.main');
          while (headMain.firstChild) headMain.removeChild(headMain.firstChild);
          var moved = 0;
          body.appendChild(head);
          for (var pi = 0; pi < paras.length; pi++) {{
            headMain.appendChild(paras[pi]);
            if (overflows()) {{ headMain.removeChild(paras[pi]); break; }}
            moved++;
          }}
          if (moved === 0) {{ body.removeChild(head); }}
          if (moved >= paras.length) continue;
          turnPage();
          var tail = blk.cloneNode(true);
          var tailMain = tail.querySelector('.main');
          var tailRail = tail.querySelector('.rail');
          if (moved > 0 && tailRail) tailRail.textContent = '';
          while (tailMain.firstChild) tailMain.removeChild(tailMain.firstChild);
          for (var qi = moved; qi < paras.length; qi++) tailMain.appendChild(paras[qi]);
          if (!place(tail)) {{ body.appendChild(tail); overflowed.push(tail); }}
          continue;
        }}
      }}

      turnPage();
      if (!place(blk)) {{ body.appendChild(blk); overflowed.push(blk); }}
    }}

    // Whatever is still waiting goes on this sheet if it fits, and only opens
    // a new one when it does not.
    drain(false);
  }}

  // Page numbers, once the sheet count is final.
  var pages = out.querySelectorAll('.page');
  for (var i = 0; i < pages.length; i++) {{
    pages[i].querySelector('.ff-right').textContent =
      (i + 1) + ' / ' + pages.length;
  }}

  src.parentNode.removeChild(src);
  document.documentElement.setAttribute('data-pages', pages.length);
  document.documentElement.setAttribute('data-overflow', overflowed.length);
  window.__layout = {{ pages: pages.length, overflow: overflowed.length }};
  document.documentElement.classList.add('laid-out');
}})();
"""


_PAGINATOR = paginator_js(BODY_H_MM)


def render(notes: Notes, res: Resolver, deck: DeckFacts) -> str:
    """Return the complete HTML document."""
    sections: list[str] = []

    # Front matter. The first sheet carries the cover strip above its content,
    # because a separate title page is a page the instructor has to turn past.
    for i, s in enumerate(notes.front):
        head = (_cover(notes, deck) if i == 0 else "") + _sheet_head(s, res)
        blocks = "".join(render_block(b, res) for b in s.blocks)
        sections.append(
            f'<section data-footer="{html.escape(s.footer or s.title)}">'
            f"{head}{blocks}</section>"
        )

    for p in notes.parts:
        mast = _masthead(p, res, notes.plans, deck)
        ladder = _ladder_html(p.ladder, res, notes.plan_row)
        blocks = "".join(render_block(b, res) for b in p.blocks)
        foot = f"Part {p.number} of 6  |  {p.short}"
        sections.append(
            f'<section data-footer="{html.escape(foot)}">'
            f"{mast}{ladder}{blocks}</section>"
        )

    for s in notes.back:
        head = _sheet_head(s, res)
        blocks = "".join(render_block(b, res) for b in s.blocks)
        sections.append(
            f'<section data-footer="{html.escape(s.footer or s.title)}">'
            f"{head}{blocks}</section>"
        )

    title = f"{notes.code} {notes.chapter} - Teaching notes"
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
<script>{_PAGINATOR}</script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# The rules the build enforces, in the spirit of deckkit._validate
# --------------------------------------------------------------------------

# The project bans both dashes everywhere. deckkit enforces it for the deck;
# this enforces it for the notes, on the rendered HTML so nothing can sneak in
# through a template.
BANNED = {"—": "em dash", "–": "en dash"}

# Butterick's band, and the reason the measure is what it is.
MIN_MEASURE = 45
MAX_MEASURE = 90


def validate(document: str, res: Resolver) -> list[str]:
    problems: list[str] = []

    if res.unresolved:
        for key in sorted(set(res.unresolved)):
            problems.append(
                f"slide key does not resolve against the deck: {key!r}. "
                "The notes name slides by key so they cannot drift; either the "
                "key is misspelled or the deck no longer has that slide."
            )

    for ch, name in BANNED.items():
        if ch in document:
            where = document.find(ch)
            problems.append(
                f"{name} at character {where}: "
                f"{document[max(0, where - 60):where + 60]!r}"
            )

    # 10pt Arial averages close to half its point size per character.
    chars = MAIN_MM / (10 * 0.5 * 25.4 / 72)
    if not (MIN_MEASURE <= chars <= MAX_MEASURE):
        problems.append(
            f"main column is about {chars:.0f} characters, outside the "
            f"{MIN_MEASURE} to {MAX_MEASURE} band"
        )

    return problems
