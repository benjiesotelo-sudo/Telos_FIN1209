"""Chapter 2 teaching charts for FIN1209, as plain data.

Eight charts, each on a companion slide immediately after the term it
belongs to. This file carries no drawing code: the forms live in
build/chartkit.py, which knows nothing about any chapter, and every entry
below is data handed to one of them.

The three rules from Chapter 1 govern this set too, and the third one bites
harder here than it did there.

**Teach only what the textbook teaches.** Dow Theory has a large popular
literature the book does not follow, so these charts show only what Lim's
Chapter 2 states. Three consequences are visible in the code below and none
of them is an oversight:

  * **No trendline on Chart D.** The chapter defines a trend as a sequence
    of peaks and troughs and says plainly that defining it by trendline
    violation instead can date the change differently. Drawing a trendline on
    the chart that teaches the definition would settle that disagreement for
    the book. Chart C carries a direction arrow, which the book's own figures
    also do; it is not tangent to anything and is not a trendline.
  * **No support or resistance levels are named.** The chapter uses the words
    and never defines them, exactly as Chapter 1 found for supply side and
    demand side.
  * **No opening price, and no OHLC bar.** Chart B draws the distance each
    day's price travelled and the close that Dow Theory keeps. It does not
    draw an opening tick, because this chapter never mentions one; the bar is
    a Chapter 3 object.

**The data is invented.** We hold no market data licence. Every series comes
from chartkit.walk() with a fixed seed, offline and reproducible, and every
chart carries the credit line deckkit.chart_credit() prints under it. No
chart here is labelled with a real instrument, an index or a date, because
this chapter's own figures are full of real ones and a student must never
have to guess which pictures are the book's.

**One idea per chart.** A companion slide carries one picture making one
point. The set is deliberately smaller than Chapter 1's nine on a longer
chapter: Chapter 2 comes with twenty six figures of its own, so a chart
earns its place only where the book asserts something its figures do not
actually show.
"""

from __future__ import annotations

import chartkit as ck
from chartkit import ChartArt, Level, Mark, Panel, Span, Sweep, Swing

DAILY = "Time, one point per trading day"
WEEKLY = "Time, one point per week"

# --------------------------------------------------------------------------
# Chart A. Why Dow built an average at all.
#
# Three erratic issues and the line that is their average. The chapter says
# the index was meant to average out or smooth erratic movements that were
# open to manipulation, so the members are noisy and the average is not.
# --------------------------------------------------------------------------

A_MEMBERS = (
    ck.walk(((0, 104.0), (14, 118.0), (26, 96.0), (44, 126.0), (58, 101.0),
             (74, 132.0), (88, 112.0), (100, 138.0)), seed=101, noise=0.030),
    ck.walk(((0, 96.0), (16, 82.0), (30, 108.0), (42, 88.0), (60, 116.0),
             (76, 94.0), (90, 122.0), (100, 108.0)), seed=103, noise=0.032),
    ck.walk(((0, 88.0), (12, 101.0), (28, 84.0), (46, 106.0), (62, 90.0),
             (78, 114.0), (92, 98.0), (100, 118.0)), seed=107, noise=0.028),
)
A_AVERAGE = [sum(values) / len(values) for values in zip(*A_MEMBERS)]

# --------------------------------------------------------------------------
# Chart B. The one price Dow Theory keeps.
#
# The whole excursion of each day, and the close marked on it. The two days
# called out are the two the slide beside it argues over: a wide day whose
# close barely moved, and a quiet day that closed a hair above the last one
# and counts for exactly as much.
# --------------------------------------------------------------------------

B_CLOSES = ck.walk(
    ((0, 61.0), (9, 63.4), (18, 62.1), (27, 64.8), (36, 63.9), (44, 66.2),
     (52, 65.4), (58, 65.5)),
    seed=113, noise=0.004,
)
_B = ck.ranges(B_CLOSES, seed=127, reach=0.030)
# The two days the slide argues over are widened and narrowed by hand, so the
# picture actually shows what the sentence claims: one day that travelled a
# long way and one that barely moved, both worth exactly one closing price.
_B[27] = (B_CLOSES[27] - 2.05, B_CLOSES[27] + 1.75)
_B[44] = (B_CLOSES[44] - 0.16, B_CLOSES[44] + 0.14)
B_RANGES = tuple(_B)

# --------------------------------------------------------------------------
# Chart C. All three trends at once, on one line.
#
# The claim the chapter makes is that the three movements run together rather
# than taking turns, so they are drawn on a single series: the arrow for the
# primary, the shaded stretch for the secondary reaction against it, and a
# callout on the day to day fluctuation that is neither.
# --------------------------------------------------------------------------

C_SERIES = ck.walk(
    ((0, 1180.0), (16, 1290.0), (30, 1245.0), (46, 1420.0), (58, 1480.0),
     (72, 1330.0), (84, 1298.0), (98, 1455.0), (112, 1560.0), (124, 1610.0)),
    seed=131, noise=0.011,
)

# --------------------------------------------------------------------------
# Chart D. What an uptrend actually is.
#
# The chapter's definition is a list of points, so this chart is that list
# drawn: higher peaks, higher troughs, and then the one lower high that says
# the uptrend has technically ended. The swing points are pivots in the
# series, so the dots sit exactly on the prices the definition talks about.
# --------------------------------------------------------------------------

D_SERIES = ck.walk(
    ((0, 92.0), (10, 104.0), (20, 98.0), (32, 116.0), (42, 108.0),
     (54, 128.0), (64, 119.0), (76, 141.0), (88, 128.0), (98, 134.0),
     (112, 118.0)),
    seed=137, noise=0.005, wobble=0.06,
)

# --------------------------------------------------------------------------
# Chart E. How far a reaction comes back.
#
# One advance and the reaction against it, with the three fractions the
# chapter names measured down from the top of the advance. Nothing is drawn
# past the end of the reaction: how far it would have gone is the question,
# not the answer.
# --------------------------------------------------------------------------

E_LOW, E_HIGH = 4000.0, 5200.0
E_SERIES = ck.walk(
    ((0, 3880.0), (6, E_LOW), (22, 4460.0), (36, 4310.0), (52, E_HIGH),
     (66, 4760.0), (84, 4400.0), (100, 4880.0)),
    seed=139, noise=0.009,
)

# --------------------------------------------------------------------------
# Chart F. The three phases, and their relative lengths.
#
# The chapter states twice that accumulation runs longer than distribution
# and gives the reason, so the two shaded stretches are drawn at the lengths
# the claim implies. The mark is on the breakout, which is the only event on
# the chart the chapter treats as tradable.
# --------------------------------------------------------------------------

F_SERIES = ck.walk(
    ((0, 102.0), (14, 97.0), (28, 103.0), (40, 98.0), (52, 104.0),
     (58, 112.0), (72, 138.0), (86, 172.0), (96, 178.0), (106, 172.0),
     (116, 179.0), (124, 174.0)),
    seed=149, noise=0.010,
)

# --------------------------------------------------------------------------
# Chart G. One average confirming the other.
#
# Two panels, the same shape at two different moments. The upper one clears
# its own earlier peak first; the signal is dated by the lower one, later.
# Neither panel is named after a real index, because the deck's figures carry
# the real ones and the two must not be mistaken for each other.
# --------------------------------------------------------------------------

G_LEVEL_UPPER, G_LEVEL_LOWER = 100.0, 98.0
# The noise is low and the counter swing shallow on purpose: the whole point
# of the chart is that the earlier peak is not breached until the marked
# moment, and a wobble that pokes a pixel over the line would deny it.
G_UPPER = ck.walk(
    ((0, 84.0), (16, G_LEVEL_UPPER), (34, 91.0), (62, G_LEVEL_UPPER),
     (90, 110.0), (104, 106.0)),
    seed=151, noise=0.004, wobble=0.04,
)
G_LOWER = ck.walk(
    ((0, 82.0), (16, G_LEVEL_LOWER), (36, 89.0), (78, G_LEVEL_LOWER),
     (96, 104.0), (104, 102.0)),
    seed=157, noise=0.004, wobble=0.04,
)

# --------------------------------------------------------------------------
# Chart H. Volume confirming the trend.
#
# The volume is derived from the price line rather than invented beside it,
# so the two cannot contradict each other, and it is then damped through the
# retracement, which is exactly the second of the chapter's four conditions.
# --------------------------------------------------------------------------

H_SERIES = ck.walk(
    ((0, 100.0), (24, 124.0), (38, 118.0), (52, 150.0), (64, 141.0),
     (76, 132.0), (92, 156.0), (108, 172.0), (118, 168.0)),
    seed=163, noise=0.010,
)
H_RETRACE = (52, 76)
H_VOLUME = [
    value * (0.42 if H_RETRACE[0] <= i <= H_RETRACE[1] else 1.0)
    for i, value in enumerate(ck.volume(H_SERIES, seed=167))
]


# --------------------------------------------------------------------------
# The eight charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.smoothing,
        kwargs=dict(
            members=A_MEMBERS,
            average=A_AVERAGE,
            member_mark=Mark(x=44, label="One issue on its own",
                             dx=50, dy=14),
            average_mark=Mark(x=62, label="The average of them",
                              dx=-14, dy=-42),
            xlabel=DAILY,
            footnote=("Three issues and their average. The chapter says why "
                      "Dow wanted the second line and not the first."),
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.closes_only,
        kwargs=dict(
            closes=B_CLOSES,
            spans_hl=B_RANGES,
            marks=(
                Mark(x=27, label="A wide day.\nOnly the dot counts.",
                     dx=-50, dy=46),
                Mark(x=44, label="A quiet day.\nIt counts the same.",
                     dx=36, dy=-46),
            ),
            xlabel=DAILY,
            close_label="The closing price, joined",
            range_label="How far the price travelled that day",
            footnote=("No opening price is drawn. This chapter never "
                      "mentions one."),
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.trends,
        kwargs=dict(
            series=C_SERIES,
            sweep=Sweep(x0=4, y0=1160.0, x1=120, y1=1560.0,
                        label="The primary trend", dx=-6, dy=-30),
            spans=(
                Span(x0=58, x1=84, label="A secondary reaction",
                     tone="notice"),
            ),
            marks=(
                Mark(x=105, label="Daily fluctuation", dx=-56, dy=30),
            ),
            xlabel=DAILY,
            footnote=("All three are on this one line at the same time, "
                      "which is the claim being made."),
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.swings,
        kwargs=dict(
            series=D_SERIES,
            points=(
                Swing(x=10, tag="higher peak"),
                Swing(x=20, tag="higher trough", above=False),
                Swing(x=32, tag="higher peak"),
                Swing(x=42, tag="higher trough", above=False),
                Swing(x=54, tag="higher peak"),
                Swing(x=64, tag="higher trough", above=False),
                Swing(x=76, tag="higher peak"),
                Swing(x=88, tag="higher trough", above=False),
                Swing(x=98, notice=True, label="The first lower peak",
                      dx=-40, dy=54),
            ),
            xlabel=DAILY,
            footnote=("No trendline is drawn. The chapter says a trendline "
                      "can date the change differently."),
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.retracement,
        kwargs=dict(
            series=E_SERIES,
            low=E_LOW,
            high=E_HIGH,
            x_low=6,
            x_high=52,
            levels=(
                Level(frac=1 / 3, label="one third back"),
                Level(frac=0.5, label="half back"),
                Level(frac=2 / 3, label="two thirds back", notice=True),
            ),
            reaction=(52, 84, "The reaction"),
            xlabel=DAILY,
            footnote=("The fractions are measured from the top of the "
                      "advance, which is how the chapter states them."),
        ),
    ),
    ChartArt(
        letter="F",
        draw=ck.record,
        kwargs=dict(
            series=F_SERIES,
            spans=(
                Span(x0=0, x1=56, label="Accumulation"),
                Span(x0=56, x1=90, label="Trend", tone="notice"),
                Span(x0=90, x1=124, label="Distribution"),
            ),
            marks=(
                Mark(x=58, label="Out of the base", dx=52, dy=-24),
            ),
            xlabel=WEEKLY,
            footnote=("The first stretch is drawn longer than the third "
                      "because the chapter says twice that it is."),
        ),
    ),
    ChartArt(
        letter="G",
        draw=ck.confirmation,
        kwargs=dict(
            upper=Panel(series=G_UPPER, name="One average",
                        level=G_LEVEL_UPPER, level_label="its earlier peak",
                        cross=62, cross_label="T1"),
            lower=Panel(series=G_LOWER, name="The other average",
                        level=G_LEVEL_LOWER, level_label="its earlier peak",
                        cross=78, cross_label="T2"),
            xlabel=DAILY,
            footnote=("The signal is dated T2, the later of the two. Neither "
                      "panel is a real index."),
        ),
    ),
    ChartArt(
        letter="H",
        draw=ck.price_volume,
        kwargs=dict(
            series=H_SERIES,
            volume=H_VOLUME,
            spans=(
                Span(x0=0, x1=H_RETRACE[0], label="With the trend",
                     tone="notice"),
                Span(x0=H_RETRACE[0], x1=H_RETRACE[1],
                     label="Against it"),
            ),
            xlabel=WEEKLY,
            volume_label="Volume",
            footnote=("The volume is derived from the line above it, so the "
                      "two panels cannot contradict each other."),
        ),
    ),
)
