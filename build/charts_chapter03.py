"""Chapter 3 teaching charts for FIN1209, as plain data.

Six charts, each on a companion slide immediately after the term it belongs
to. This file carries no drawing code: the forms live in build/chartkit.py,
which knows nothing about any chapter, and every entry below is data handed
to one of them. Chart B reuses a Chapter 2 form; the other five forms were
added to chartkit for this chapter.

Chapter 3 comes with forty figures of its own, so a chart earns its place
only where the book describes a construction that none of its figures
actually draws:

  * **A** measures the four gap types on one pair of bars, in pesos. The
    book's Figure 3.9 draws the four as schematics with no prices on them.
  * **B** is a line chart drawn over the highs and lows it throws away.
  * **C** builds point and figure columns box by box from a price path. The
    book states the arithmetic of a 3 box reversal and shows only a finished
    chart.
  * **D** is the constant volume chart, which the book describes and never
    draws.
  * **E** puts the book's own example, 10 to 20 against 90 to 100, on the
    three scales, including the square root scale the book describes and
    never draws.
  * **F** back adjusts through several rolls at a discount until the early
    history goes below zero, which the book warns can happen and never draws.

**Teach only what the textbook teaches.** No trendline, support or
resistance is drawn on any of them. Chart C uses closing prices, which the
book says is normal for point and figure, and starts each new column one box
away from the last, which is how the book's own point and figure figure is
drawn; it states no other rule, so no other rule is drawn. Chart A shows no
fill of the gap, because the book says a gap may or may not be filled.

**The data is invented.** We hold no market data licence. Every series comes
from chartkit.walk() with a fixed seed, offline and reproducible, and every
chart carries the credit line deckkit.chart_credit() prints under it. No
chart is labelled with a real instrument, an index, a contract month or a
date.
"""

from __future__ import annotations

import chartkit as ck
from chartkit import Bar, ChartArt, Mark, Measure

DAILY = "Time, one point per trading day"

# --------------------------------------------------------------------------
# Chart A. The four gaps, measured on one pair of bars.
#
# The running example from the three gap slides: the last bar has a high of
# 104 and closes at 102, the new bar opens at 106 with a low of 105.50. The
# four definitions join four different pairs of those prices.
# --------------------------------------------------------------------------

A_LAST = Bar(open=101.0, high=104.0, low=100.0, close=102.0)
A_NEW = Bar(open=106.0, high=108.0, low=105.5, close=107.0)

# --------------------------------------------------------------------------
# Chart B. What a line chart keeps.
#
# The same device as Chapter 2's Chart B, for a different point: there it was
# what Dow Theory records, here it is what a line chart draws. The pale bars
# are the highs and lows, which the chapter calls the true indicators of
# market force, and the line never touches them.
# --------------------------------------------------------------------------

B_CLOSES = ck.walk(
    ((0, 48.0), (8, 50.6), (15, 49.4), (24, 52.8), (31, 51.6), (40, 54.2),
     (46, 53.5)),
    seed=301, noise=0.004,
)
_B = ck.ranges(B_CLOSES, seed=307, reach=0.022)
_B[24] = (B_CLOSES[24] - 1.55, B_CLOSES[24] + 1.30)
B_RANGES = tuple(_B)

# --------------------------------------------------------------------------
# Chart C. Point and figure, one box at a time.
#
# Closing prices around 50 pesos, a 1 peso box and a 3 box reversal. The
# first dip is deliberately too shallow to reverse; the second one is exactly
# deep enough. The gold column is that first reversal.
# --------------------------------------------------------------------------

C_CLOSES = ck.walk(
    ((0, 50.3), (8, 53.6), (14, 56.4), (20, 53.6), (28, 58.3), (34, 56.9),
     (40, 54.4), (48, 51.3), (54, 53.2), (60, 55.8), (66, 57.5)),
    seed=311, noise=0.0025, wobble=0.04,
)

# --------------------------------------------------------------------------
# Chart D. Where a constant volume bar closes.
#
# One session of five minute periods. Volume is heavy at the start and the
# end and light in the middle, and a gold line drops wherever another fixed
# block of shares has traded. The price line is only there so the picture
# reads as a session; nothing on it is marked.
# --------------------------------------------------------------------------

D_SERIES = ck.walk(
    ((0, 72.0), (8, 73.4), (20, 72.9), (34, 73.3), (46, 72.8), (54, 74.0),
     (59, 74.6)),
    seed=317, noise=0.0025,
)
_D_SHAPE = [1.0 + 2.6 * ((i - 29.5) / 29.5) ** 4 for i in range(60)]
D_VOLUME = [shape * base for shape, base in zip(
    _D_SHAPE, ck.volume(D_SERIES, seed=331, base=100.0, lift=0.5))]
D_BLOCK = sum(D_VOLUME) / 15.0

# --------------------------------------------------------------------------
# Chart E. One price axis, three scales.
#
# The book's own worked example: 10 to 20 is 100 percent and 90 to 100 is
# 11.1 percent. On a linear axis they are the same height, on a ratio axis
# they are not, and on a square root axis they fall in between, which is the
# whole of what the book says about square root.
# --------------------------------------------------------------------------

E_LEVELS = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# --------------------------------------------------------------------------
# Chart F. Back adjusting through several rolls.
#
# Five contracts in turn. Each one rises over its own life, and each new one
# starts at a discount to where the last one finished. Joined as they
# traded, the record is a falling saw; back adjusted, it is one continuous
# line whose earliest prices sit below zero.
# --------------------------------------------------------------------------

F_CONTRACTS = (
    ck.walk(((0, 14.0), (10, 16.4), (21, 18.0)), seed=337, noise=0.008),
    ck.walk(((0, 11.0), (10, 13.8), (21, 16.0)), seed=347, noise=0.008),
    ck.walk(((0, 9.0), (10, 11.6), (21, 14.0)), seed=349, noise=0.008),
    ck.walk(((0, 8.0), (10, 10.4), (21, 13.0)), seed=353, noise=0.008),
    ck.walk(((0, 7.0), (10, 9.6), (21, 12.0)), seed=359, noise=0.008),
)


# --------------------------------------------------------------------------
# The six charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.measured_bars,
        kwargs=dict(
            first=A_LAST,
            second=A_NEW,
            measures=(
                Measure(lo=102.0, hi=106.0, label="Type 1\nclose to open\n4 pesos"),
                Measure(lo=104.0, hi=106.0, label="Type 2\nhigh to open\n2 pesos"),
                Measure(lo=104.0, hi=105.5, label="Type 3\nhigh to low\n1.50 pesos",
                        notice=True),
                Measure(lo=102.0, hi=105.5, label="Type 4\nclose to low\n3.50 pesos"),
            ),
            price_ticks=(100, 101, 102, 103, 104, 105, 106, 107, 108),
            labels=("Last bar", "New bar"),
            footnote=("Open ticks on the left, close ticks on the right. The "
                      "gold one, Type 3, is the gap called a window."),
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.closes_only,
        kwargs=dict(
            closes=B_CLOSES,
            spans_hl=B_RANGES,
            marks=(
                Mark(x=24, label="A wide day. The line\nsees only its close.",
                     dx=-46, dy=44),
            ),
            xlabel=DAILY,
            close_label="The line chart: closes, joined",
            range_label="The highs and lows it throws away",
            footnote=("The pale bars are everything the line chart leaves "
                      "out."),
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.point_figure,
        kwargs=dict(
            closes=C_CLOSES,
            box=1.0,
            reversal=3,
            notice_column=1,
            xlabel=DAILY,
            price_label="Closing prices, day by day",
            figure_label="Point and figure: one column per swing, no time",
            footnote=("A 1 peso box and a 3 box reversal, on closing prices. "
                      "Gold is the first reversal."),
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.volume_clock,
        kwargs=dict(
            series=D_SERIES,
            volume=D_VOLUME,
            block=D_BLOCK,
            xlabel="Time, one bar per five minutes of one session",
            volume_label="Volume",
            marks_label="Gold: where each constant volume bar closes",
            callouts=(
                Mark(x=5, label="Busy: bars close quickly", dx=0, dy=4),
                Mark(x=30, label="Quiet: each bar takes far longer",
                     dx=0, dy=4),
            ),
            footnote=("Every gold line marks the same number of shares "
                      "traded. Only the time between them changes."),
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.price_scales,
        kwargs=dict(
            levels=E_LEVELS,
            low=10.0,
            high=100.0,
            moves=(
                (10.0, 20.0, "10 to 20, up 100 percent", False),
                (90.0, 100.0, "90 to 100, up 11.1 percent", True),
            ),
            footnote=("All three axes are the same height and carry the same "
                      "prices. Only where the prices land differs."),
        ),
    ),
    ChartArt(
        letter="F",
        draw=ck.back_adjusted,
        kwargs=dict(
            contracts=F_CONTRACTS,
            xlabel="Time, one point per trading day, five contracts in turn",
            raw_label="Grey: each contract joined as it traded",
            adjusted_label="Black: the same prices back adjusted",
            zero_label="zero",
            callout=Mark(x=3, label="Adjusted history below zero",
                         dx=40, dy=40),
            footnote=("Every new contract here starts at a discount to the "
                      "last, the case in which the book warns of this."),
        ),
    ),
)
