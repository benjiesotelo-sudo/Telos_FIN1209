"""chartkit - the FIN1209 teaching charts.

This module draws charts. Like deckkit it knows nothing about any chapter:
the data, the labels and the letters live in a chapter module (see
charts_chapter01.py) as plain data, and every drawing routine here takes that
data as arguments.

Three things make these charts different from the textbook figures, and all
three are deliberate.

  * **They are ours.** The book's figures are Wiley's, they are copyrighted,
    and they are not in this repository. These are drawn from code that is,
    so a fresh clone builds the real slide rather than a placeholder.

  * **The data is invented.** Every series below comes out of a fixed seed
    with no network and no data file. We hold no market data licence, and a
    definitional graphic makes no claim about markets that being real would
    support. Every chart says so on its face: deckkit.chart_credit() is the
    one place that sentence is written.

  * **They are in their own namespace.** Chart A, Chart B, and so on, never a
    figure number, so a student can always tell which pictures are the book's.

Drawing rules, taken from the deck:

  * The deck's palette and the deck's fonts, both imported from deckkit so
    there is one copy of each.
  * The band a figure is drawn into, so a chart fills the slide exactly.
  * Green carries structure, gold marks the single thing to notice. One gold
    thing per chart, never two.
  * Two hairline spines, muted labels, and no grid loud enough to fight the
    line.
  * **No title inside the image.** The slide already carries one above the
    band and the lecture notes carry a caption below it, so a third heading
    in the artwork said the same thing twice on the same page. The chart's
    subject is named by whatever places it.

Determinism: the .pptx build is byte reproducible and these images are
embedded in it, so the images have to be byte reproducible too. Two things
buy that. The series come from random.Random with a fixed seed and use only
uniform(), whose stream is stable. And savefig is told to write no Software
metadata, which otherwise stamps the matplotlib version into the file. A
matplotlib upgrade will still move the bytes, the same way a python-pptx
upgrade does; see build/README.md.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

import deckkit  # noqa: E402

# --------------------------------------------------------------------------
# The deck's identity, read from deckkit rather than copied
# --------------------------------------------------------------------------


def _hex(color) -> str:
    return "#" + str(color)


GREEN = _hex(deckkit.GREEN)
GREEN_DEEP = _hex(deckkit.GREEN_DEEP)
GOLD = _hex(deckkit.GOLD)
INK = _hex(deckkit.INK)
PAPER = _hex(deckkit.PAPER)
MUTED = _hex(deckkit.MUTED)
BORDER = _hex(deckkit.BORDER)
WHITE = _hex(deckkit.WHITE)

# A gold wash for a shaded span. The palette has no tint, and a span painted
# in GOLD itself buries the price line under it.
GOLD_WASH = "#FDF0D2"
GREY_WASH = "#EDEDE8"

# The largest image deckkit.render_figure will place in the figure band: the
# band, less the 0.13in inset it puts around the artwork. Drawing at exactly
# this ratio fills the band, which is about twice the area a textbook scan
# takes on the same slide.
INSET = 0.13
FIG_W = deckkit.CONTENT_W.inches - 2 * INSET
FIG_H = deckkit.FIGURE_H - 2 * INSET
DPI = 200


# --------------------------------------------------------------------------
# The data: invented, seeded, and reproducible with no network
# --------------------------------------------------------------------------


def walk(pivots: tuple[tuple[int, float], ...], *, seed: int,
         wobble: float = 0.09, noise: float = 0.012) -> list[float]:
    """A price line through hand placed pivots.

    ``pivots`` are (index, price) points the series must pass through. Between
    two pivots the line runs to the next one with a shallow counter-swing
    inside the leg and a little noise on every point, so it reads as a price
    rather than as a zigzag. ``noise`` is a fraction of price, so a series at
    620 pesos is no noisier in proportion than one at 40.
    """
    rng = random.Random(seed)
    out: list[float] = []
    for k in range(len(pivots) - 1):
        (x0, y0), (x1, y1) = pivots[k], pivots[k + 1]
        span = x1 - x0
        for x in range(x0, x1):
            t = (x - x0) / span
            # A half cycle of a sine, scaled to the leg, is the counter swing:
            # price gives some of the move back before carrying on.
            swing = _half_swing(t) * abs(y1 - y0) * wobble
            level = y0 + (y1 - y0) * t
            out.append(level + swing + level * rng.uniform(-noise, noise))
    out.append(float(pivots[-1][1]))
    # The pivots are the teaching points and callouts are placed on them, so
    # they are restored exactly after the noise has been laid on.
    for x, y in pivots:
        out[x] = float(y)
    return out


def _half_swing(t: float) -> float:
    """A smooth up-then-down bump over 0 to 1, without importing math."""
    # 16 t^2 (1-t)^2 peaks at 1.0 in the middle and is 0 at both ends; the
    # sign flips at the halfway point so the leg gives some of the move back.
    bump = 16.0 * t * t * (1 - t) * (1 - t)
    return bump if t < 0.5 else -bump


def gap(series: list[float], at: int, size: float) -> list[float]:
    """Lift everything from ``at`` onwards, so the line jumps at one point.

    A gap is a break in the record: the market reopened away from where it
    closed. The chapter names gapping and never defines it, so a chart may
    point at one and must not explain it.
    """
    return [v + (size if i >= at else 0.0) for i, v in enumerate(series)]


# --------------------------------------------------------------------------
# Chart chrome
# --------------------------------------------------------------------------


def _new(display_font: str):
    plt.rcParams.update({
        "font.family": deckkit.BODY_FONT,
        "font.size": 11,
        "axes.edgecolor": BORDER,
        "axes.labelcolor": MUTED,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "figure.facecolor": WHITE,
        "axes.facecolor": WHITE,
        "savefig.facecolor": WHITE,
    })
    return plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)


def _dress(ax, *, ylabel="Price (PHP)", xlabel="Time", grid=True):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(BORDER)
        ax.spines[side].set_linewidth(1.0)
    ax.tick_params(length=3, width=0.8, labelsize=10)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11, color=MUTED, labelpad=6)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11, color=MUTED, labelpad=4)
    if grid:
        ax.yaxis.grid(True, color=BORDER, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.set_xticks([])


def _footnote(fig, text):
    """The honest small print: what the chart does and does not claim.

    Never the credit line. deckkit and lecturekit both print the credit under
    the artwork from deckkit.chart_credit(), so putting it in the image as
    well would say it twice.
    """
    if text:
        fig.text(0.006, 0.015, text, fontsize=9.5, color=MUTED, style="italic",
                 ha="left", va="bottom")


def _frac(x, series) -> float:
    """An x index as a fraction of the axes, which is what axhspan wants."""
    return (x + 2) / (len(series) + 3)


def _headroom(ax, series, *, top=0.16, bottom=0.10):
    """Room above and below the line for the labels to sit in.

    Generous, and deliberately so: a callout is placed as an offset in points
    from its own point, so a label on the lowest price in the series needs
    somewhere inside the axes to go. Without the room it lands on the axis
    title underneath, which is what it looked like the first time.
    """
    lo, hi = min(series), max(series)
    span = hi - lo or 1.0
    ax.set_ylim(lo - span * bottom, hi + span * top)


def _save(fig, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    # metadata Software=None: matplotlib otherwise stamps its own version into
    # the PNG, which would move the bytes of a committed deck on every upgrade
    # for no change in what is drawn.
    fig.savefig(path, dpi=DPI, facecolor=WHITE, metadata={"Software": None})
    plt.close(fig)
    return path


# --------------------------------------------------------------------------
# Callout helpers
# --------------------------------------------------------------------------


def _dot(ax, x, y, *, tone=GOLD, size=11, dim=False):
    ax.plot(x, y, marker="o", ms=size, zorder=6,
            color=BORDER if dim else tone,
            markeredgecolor=MUTED if dim else GREEN_DEEP, markeredgewidth=1.1)


def _tag(color=WHITE):
    """A quiet plate behind a label.

    A callout on a price chart will sometimes land on the line however
    carefully it is placed, and a label that has to be legible from the back
    of a lecture hall cannot afford to be read through a black stroke. The
    plate makes the overlap deliberate instead of accidental.
    """
    return dict(boxstyle="round,pad=0.30", facecolor=color, edgecolor=BORDER,
                linewidth=0.8)


def _callout(ax, x, y, text, *, dx, dy, tone=INK, weight="bold", size=12.5):
    """A short label on a plate, joined to its point by a gold hairline.

    ``dx`` and ``dy`` are offsets in typographic points, not data units, so a
    chapter module places a label without knowing the price scale and the
    same offset means the same distance on every chart in the set.
    """
    ax.annotate(text, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                ha="right" if dx < 0 else "left", va="center", fontsize=size,
                color=tone, fontweight=weight, zorder=7, bbox=_tag(),
                arrowprops=dict(arrowstyle="-", color=GOLD, lw=1.4,
                                shrinkA=0, shrinkB=4))


# --------------------------------------------------------------------------
# The chart forms. Each one takes data and knows nothing about any chapter.
# --------------------------------------------------------------------------


@dataclass
class Reading:
    """One price read off the line, at one moment."""

    x: int = 0
    label: str = ""
    dx: float = 0.0     # offset of the label, in points
    dy: float = 0.0


def readings(path: Path, series, marks: tuple[Reading, ...], *,
             xlabel, footnote="", display_font=None) -> Path:
    """A price line with the number read off it at two or three moments.

    The teaching point is that the same public number is different every time
    you look, which is what makes price a variable of change.
    """
    display_font = display_font or deckkit.DISPLAY_FONT
    fig = _new(display_font)
    ax = fig.add_axes([0.062, 0.20, 0.918, 0.71])
    ax.plot(range(len(series)), series, color=INK, lw=1.7, zorder=3)
    _dress(ax, xlabel=xlabel)
    ax.set_xlim(-2, len(series) + 1)
    _headroom(ax, series, top=0.22, bottom=0.26)

    for m in marks:
        y = series[m.x]
        ax.plot([m.x, m.x], [ax.get_ylim()[0], y], color=BORDER, lw=1.0,
                zorder=2)
        _dot(ax, m.x, y)
        _callout(ax, m.x, y, m.label, dx=m.dx, dy=m.dy)

    _footnote(fig, footnote)
    return _save(fig, path)


@dataclass
class Gain:
    """What was kept between the two legs of a closed position.

    ``x0`` and ``x1`` bound the shaded block in time, so it reads as the
    distance between this open and this close rather than as a price zone
    that holds across the whole chart.
    """

    low: float = 0.0
    high: float = 0.0
    label: str = ""
    x0: int = 0
    x1: int = 0
    label_y: float = 0.0    # where the label sits; 0 means halfway up


@dataclass
class Leg:
    """One end of a position: where it was opened, or where it was closed."""

    x: int = 0
    price: float = 0.0
    label: str = ""
    dx: float = 0.0     # offset of the label, in points
    dy: float = 0.0
    dim: bool = False


def trade(path: Path, series, legs: tuple[Leg, ...], *, xlabel,
          direction="", gain=None, footnote="", display_font=None) -> Path:
    """A position drawn on a price-time chart.

    ``legs`` are the markers. A dim leg is one an earlier chart already made
    the point about, so the eye goes to the gold one. ``direction`` is the
    arrow saying which way the holder wants price to go, and it is drawn only
    on the two opening charts. ``gain`` is a Gain and shades what
    was kept between the open and the close.
    """
    display_font = display_font or deckkit.DISPLAY_FONT
    fig = _new(display_font)
    ax = fig.add_axes([0.062, 0.20, 0.918, 0.71])
    ax.plot(range(len(series)), series, color=INK, lw=1.7, zorder=3)
    _dress(ax, xlabel=xlabel)
    ax.set_xlim(-2, len(series) + 1)
    _headroom(ax, series, top=0.24, bottom=0.30)

    if gain is not None:
        lo, hi = min(gain.low, gain.high), max(gain.low, gain.high)
        x0, x1 = _frac(gain.x0, series), _frac(gain.x1, series)
        ax.axhspan(lo, hi, xmin=x0, xmax=x1, color=GOLD_WASH, zorder=0)
        y = gain.label_y or (lo + hi) / 2
        ax.text((x0 + x1) / 2, y, gain.label, fontsize=12.5,
                transform=ax.get_yaxis_transform(), color=GREEN_DEEP,
                fontweight="bold", va="center", ha="center", zorder=4,
                bbox=_tag(GOLD_WASH))

    for leg in legs:
        ax.axhline(leg.price, color=BORDER, lw=1.0, zorder=1,
                   xmax=_frac(leg.x, series))
        _dot(ax, leg.x, leg.price, dim=leg.dim)
        _callout(ax, leg.x, leg.price, leg.label, dx=leg.dx, dy=leg.dy,
                 tone=MUTED if leg.dim else INK,
                 weight="normal" if leg.dim else "bold",
                 size=11.5 if leg.dim else 12.5)

    if direction:
        up, text = direction
        sign = 1.0 if up else -1.0
        lo, hi = ax.get_ylim()
        span = hi - lo
        base = hi - span * 0.19 if sign > 0 else lo + span * 0.19
        x = len(series) * 0.66
        ax.annotate("", xy=(x, base + sign * span * 0.15), xytext=(x, base),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.4,
                                    mutation_scale=24), zorder=6)
        ax.text(x + len(series) * 0.022, base + sign * span * 0.075, text,
                fontsize=12.5, color=GREEN, fontweight="bold", va="center",
                ha="left", zorder=6, bbox=_tag())

    _footnote(fig, footnote)
    return _save(fig, path)


def axes_lesson(path: Path, series, *, price_label, time_label,
                footnote="", display_font=None) -> Path:
    """The price-time chart itself: what the two axes are.

    The one chart in the set whose subject is the object rather than anything
    on it, so the axis names are set large and everything else is quiet.
    """
    display_font = display_font or deckkit.DISPLAY_FONT
    fig = _new(display_font)
    ax = fig.add_axes([0.105, 0.235, 0.865, 0.68])
    ax.plot(range(len(series)), series, color=INK, lw=1.7, zorder=3)
    _dress(ax, ylabel="", xlabel="")
    ax.set_xlim(-2, len(series) + 1)
    _headroom(ax, series, top=0.14)

    lo, hi = ax.get_ylim()
    ax.annotate("", xy=(-2, hi), xytext=(-2, lo),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.4,
                                mutation_scale=20),
                annotation_clip=False, zorder=6)
    ax.annotate("", xy=(len(series) + 1, lo), xytext=(-2, lo),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.4,
                                mutation_scale=20),
                annotation_clip=False, zorder=6)
    ax.text(-0.085, 0.5, price_label, transform=ax.transAxes, rotation=90,
            ha="center", va="center", fontsize=17, color=GREEN,
            fontweight="bold", fontname=display_font)
    ax.text(0.5, -0.155, time_label, transform=ax.transAxes, ha="center",
            va="center", fontsize=17, color=GREEN, fontweight="bold",
            fontname=display_font)
    _footnote(fig, footnote)
    return _save(fig, path)


@dataclass
class Mark:
    """One plain fact marked on the record."""

    x: int = 0
    label: str = ""
    dx: float = 0.0     # offset of the label, in points
    dy: float = 0.0


@dataclass
class Span:
    """A stretch of the record worth naming, shaded behind the line."""

    x0: int = 0
    x1: int = 0
    label: str = ""
    tone: str = "quiet"     # quiet (grey) or notice (gold)


def record(path: Path, series, marks: tuple[Mark, ...],
           spans: tuple[Span, ...] = (), *, xlabel, footnote="",
           display_font=None) -> Path:
    """The descriptive half: facts read off the record, with no opinion.

    Everything marked here is something that already happened, which is the
    whole distinction the chart is drawn to carry.
    """
    display_font = display_font or deckkit.DISPLAY_FONT
    fig = _new(display_font)
    ax = fig.add_axes([0.062, 0.20, 0.918, 0.71])

    for s in spans:
        ax.axvspan(s.x0, s.x1, color=GREY_WASH if s.tone == "quiet"
                   else GOLD_WASH, zorder=0)
    ax.plot(range(len(series)), series, color=INK, lw=1.7, zorder=3)
    _dress(ax, xlabel=xlabel)
    ax.set_xlim(-2, len(series) + 1)
    _headroom(ax, series, top=0.24, bottom=0.30)

    for s in spans:
        if s.label:
            ax.text((s.x0 + s.x1) / 2, 1.02, s.label,
                    transform=ax.get_xaxis_transform(), ha="center",
                    va="bottom", fontsize=12, color=MUTED, fontweight="bold")

    for m in marks:
        y = series[m.x]
        _dot(ax, m.x, y)
        _callout(ax, m.x, y, m.label, dx=m.dx, dy=m.dy)

    _footnote(fig, footnote)
    return _save(fig, path)


def claim(path: Path, series, *, level: float, level_label: str,
          touches: tuple[int, ...], future: int, xlabel,
          record_label: str, claim_label: str, footnote="",
          display_font=None) -> Path:
    """The inferential half: the record, and then the claim made from it.

    Everything left of ``future`` happened. Everything right of it is the
    forecast, and it is drawn as an empty band rather than as a line, because
    a drawn line would be the one thing this chart must not assert.
    """
    display_font = display_font or deckkit.DISPLAY_FONT
    fig = _new(display_font)
    ax = fig.add_axes([0.062, 0.20, 0.918, 0.71])
    end = len(series) + int(len(series) * 0.30)

    ax.axvspan(future, end, color=PAPER, zorder=0)
    ax.plot(range(len(series)), series, color=INK, lw=1.7, zorder=3)
    ax.axhline(level, color=GREEN, lw=1.3, ls=(0, (5, 4)), zorder=2)
    ax.text(0.008, level, level_label, fontsize=11.5,
            transform=ax.get_yaxis_transform(), color=GREEN, va="bottom",
            ha="left", fontweight="bold", zorder=4)
    _dress(ax, xlabel=xlabel)
    ax.set_xlim(-2, end)
    _headroom(ax, series, top=0.24, bottom=0.14)

    for x in touches:
        _dot(ax, x, series[x], size=10)

    ax.axvline(future, color=MUTED, lw=1.2, zorder=2)
    # Inside the axes, not above them: the heading already owns the strip
    # over the plot and two lines of type there collide.
    ax.text(future / 2, 0.95, record_label,
            transform=ax.get_xaxis_transform(), ha="center", va="top",
            fontsize=12.5, color=GREEN_DEEP, fontweight="bold", zorder=6,
            bbox=_tag())
    ax.text((future + end) / 2, 0.95, claim_label,
            transform=ax.get_xaxis_transform(), ha="center", va="top",
            fontsize=12.5, color=GOLD, fontweight="bold", zorder=6,
            bbox=_tag())

    lo, hi = ax.get_ylim()
    ax.annotate("", xy=((future + end) / 2 + (end - future) * 0.22,
                        level + (hi - lo) * 0.015),
                xytext=(future + (end - future) * 0.14,
                        level + (hi - lo) * 0.015),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2.0,
                                ls=(0, (4, 3)), mutation_scale=20), zorder=6)
    _footnote(fig, footnote)
    return _save(fig, path)


# --------------------------------------------------------------------------
# What a chapter module hands back, and how the builds ask for it
# --------------------------------------------------------------------------


@dataclass
class ChartArt:
    """One drawable chart: the deck's letter, and how to draw it.

    ``draw`` is one of the forms above, already carrying its data. The chapter
    module builds these; nothing here knows what is in them.
    """

    letter: str = ""
    draw: object = None
    kwargs: dict = field(default_factory=dict)


def generate(arts, out_dir, *, display_font=None) -> list[Path]:
    """Draw every chart into ``out_dir`` and return the files written.

    Called by both PDF builds and by the deck build, so a fresh clone that has
    never drawn a chart produces the real slide on its first run.
    """
    out_dir = Path(out_dir)
    written = []
    for art in arts:
        path = out_dir / f"chart-{art.letter.lower()}.png"
        written.append(art.draw(path, display_font=display_font,
                                **art.kwargs))
    return written
