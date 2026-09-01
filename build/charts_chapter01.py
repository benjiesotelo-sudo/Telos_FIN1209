"""Chapter 1 teaching charts for FIN1209, as plain data.

Nine charts, one for each term slide in Part 1, each drawn on a companion
slide immediately after the term it belongs to. This file carries no drawing
code: the forms live in build/chartkit.py, which knows nothing about any
chapter, and every entry below is data handed to one of them.

Three rules govern what is on these charts, and they are not style
preferences.

**Teach only what the textbook teaches.** Every chart illustrates something
Lim states in Chapter 1, and where possible it uses the numbers the deck's own
worked example already uses, so the chart and the slide beside it agree. Three
things the chapter mentions and never defines are deliberately absent: support
and resistance, the OHLC bar (a Part 2 term, so no bars appear in Part 1), and
any rule for what counts as a peak or a trough. Gapping is named on the
identification chart and not explained, because the chapter names it and does
not explain it either.

**The data is invented.** We hold no market data licence. Every series comes
from chartkit.walk() with a fixed seed, offline and reproducible, and every
chart carries the credit line deckkit.chart_credit() prints under it. Where a
chart uses a price from a worked example that names a real company, its
footnote says the two prices are the example's and the path between them is
not.

**One idea per chart.** A companion slide carries one picture making one
point. Charts F to I are four views of the same price line with different
markers on it, which is what makes the four verbs a sequence rather than a
list.
"""

from __future__ import annotations

import chartkit as ck
from chartkit import ChartArt, Gain, Leg, Mark, Reading, Span

# --------------------------------------------------------------------------
# The series. Invented, seeded, offline.
#
# Each pivot list is hand placed to make its teaching point land, and the
# seeds are fixed so the same numbers come out on any machine forever. The
# prices that carry meaning (40 and 52, 620, 660 and 610, 100, 240 and 244)
# are pivots, so chartkit.walk restores them exactly and a callout can sit on
# the number the slide says out loud.
# --------------------------------------------------------------------------

# Chart A. Price, watched. Ends on the two closes the Price slide quotes.
A_SERIES = ck.walk(
    ((0, 231.0), (18, 218.0), (34, 236.0), (52, 224.0), (70, 252.0),
     (86, 238.0), (98, 247.0), (108, 240.0), (109, 244.0)),
    seed=17,
)

# Chart B. The mechanical rule, on the buy low sell high slide's own numbers.
B_SERIES = ck.walk(
    ((0, 46.0), (10, 43.5), (22, 40.0), (36, 45.5), (48, 42.5), (62, 49.0),
     (78, 52.0), (90, 48.5), (99, 50.5)),
    seed=23,
)

# Chart C. A plain price line. Nothing is marked on it; the axes are the
# subject, so the series only has to look like a price.
C_SERIES = ck.walk(
    ((0, 96.0), (16, 104.0), (30, 92.0), (46, 112.0), (60, 103.0),
     (76, 124.0), (90, 114.0), (104, 129.0), (114, 121.0)),
    seed=31,
)

# Chart D. The record: a high, a low, a calm stretch, and a gap. The gap is
# applied after the walk so the line genuinely breaks at one point rather
# than being drawn steep.
D_SERIES = ck.gap(
    ck.walk(
        ((0, 168.0), (14, 158.0), (26, 176.0), (40, 149.0), (54, 162.0),
         (66, 160.0), (78, 163.0), (88, 158.0), (100, 181.0), (112, 172.0),
         (119, 177.0)),
        seed=41, noise=0.009,
    ),
    at=89, size=9.0,
)
D_HIGH = D_SERIES.index(max(D_SERIES))
D_LOW = D_SERIES.index(min(D_SERIES))

# Chart E. Four bounces off 100 pesos, which is the Forecasting slide's own
# example, and then the edge of the record.
E_SERIES = ck.walk(
    ((0, 118.0), (12, 100.0), (26, 116.0), (40, 100.0), (56, 121.0),
     (70, 100.0), (84, 114.0), (96, 100.0), (108, 109.0)),
    seed=53, noise=0.010,
)

# Charts F to I. One position taken and closed, then one taken the other way
# and closed, on a single line. 620, 660 and 610 are the four verb slides'
# own worked example, in the order the slides teach them.
VERB_SERIES = ck.walk(
    ((0, 616.0), (18, 620.0), (32, 605.0), (46, 638.0), (62, 660.0),
     (76, 631.0), (88, 646.0), (102, 610.0), (114, 623.0)),
    seed=67, noise=0.008,
)

VERB_XLABEL = "Time, one point per trading day"
VERB_FOOTNOTE = ("The three prices are the slides' own worked example. "
                 "The path between them is illustrative.")


# --------------------------------------------------------------------------
# The nine charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.readings,
        kwargs=dict(
            series=A_SERIES,
            marks=(
                Reading(x=18, label="In April, 218", dx=52, dy=-20),
                Reading(x=70, label="In June, 252", dx=-52, dy=18),
                Reading(x=108, label="Yesterday, 240", dx=-56, dy=-34),
                Reading(x=109, label="Today, 244", dx=-46, dy=30),
            ),
            xlabel="Time, one point per trading day",
            footnote=("The last two closes are the slide's own worked "
                      "example. The path between them is illustrative."),
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.trade,
        kwargs=dict(
            series=B_SERIES,
            legs=(
                Leg(x=22, price=40.0, label="Buy here, at 40",
                    dx=52, dy=-20),
                Leg(x=78, price=52.0, label="Sell here, at 52",
                    dx=-52, dy=22),
            ),
            gain=Gain(low=40.0, high=52.0, x0=22, x1=78,
                      label="12 pesos a share, kept"),
            xlabel="Time, one point per trading day",
            footnote=("Knowing that 40 was the low one is the part the rule "
                      "does not give you."),
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.axes_lesson,
        kwargs=dict(
            series=C_SERIES,
            price_label="PRICE",
            time_label="TIME",
            footnote=("Nothing is marked on it. The two axes are the whole "
                      "object."),
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.record,
        kwargs=dict(
            series=D_SERIES,
            marks=(
                Mark(x=D_HIGH, label="The highest price paid", dx=-58, dy=22),
                Mark(x=D_LOW, label="The lowest", dx=48, dy=-20),
                Mark(x=89, label="Here it gapped", dx=-58, dy=30),
            ),
            spans=(
                Span(x0=54, x1=78, label="the calmest stretch"),
            ),
            xlabel="Time, one point per trading day",
            footnote=("The chapter names gapping and does not define it. "
                      "This chart points at one and leaves it there."),
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.claim,
        kwargs=dict(
            series=E_SERIES,
            level=100.0,
            level_label="100 pesos",
            touches=(12, 40, 70, 96),
            future=108,
            xlabel="Time, one point per trading day",
            record_label="What happened",
            claim_label="What you are claiming",
            footnote=("The forecast is not drawn as a line, because a line "
                      "would assert the one thing nobody yet knows."),
        ),
    ),
    ChartArt(
        letter="F",
        draw=ck.trade,
        kwargs=dict(
            series=VERB_SERIES,
            legs=(
                Leg(x=18, price=620.0, label="Buy to open: long at 620",
                    dx=44, dy=42),
            ),
            direction=(True, "you profit if price rises"),
            xlabel=VERB_XLABEL,
            footnote=VERB_FOOTNOTE,
        ),
    ),
    ChartArt(
        letter="G",
        draw=ck.trade,
        kwargs=dict(
            series=VERB_SERIES,
            legs=(
                Leg(x=18, price=620.0, label="opened here", dx=-40, dy=-34,
                    dim=True),
                Leg(x=62, price=660.0, label="Sell to close: liquidated at 660",
                    dx=-44, dy=22),
            ),
            gain=Gain(low=620.0, high=660.0, x0=18, x1=62,
                      label="40 pesos a share, kept"),
            xlabel=VERB_XLABEL,
            footnote=VERB_FOOTNOTE,
        ),
    ),
    ChartArt(
        letter="H",
        draw=ck.trade,
        kwargs=dict(
            series=VERB_SERIES,
            legs=(
                Leg(x=62, price=660.0, label="Sell to open: short at 660",
                    dx=-44, dy=22),
            ),
            direction=(False, "you profit if price falls"),
            xlabel=VERB_XLABEL,
            footnote=VERB_FOOTNOTE,
        ),
    ),
    ChartArt(
        letter="I",
        draw=ck.trade,
        kwargs=dict(
            series=VERB_SERIES,
            legs=(
                Leg(x=62, price=660.0, label="opened here", dx=-40, dy=22,
                    dim=True),
                Leg(x=102, price=610.0, label="Buy to close: covered at 610",
                    dx=-46, dy=-20),
            ),
            # Placed low in the block on purpose: at its midpoint the label
            # sits exactly on the falling line and hides it.
            gain=Gain(low=610.0, high=660.0, x0=62, x1=102, label_y=620.0,
                      label="50 pesos a share, kept"),
            xlabel=VERB_XLABEL,
            footnote=VERB_FOOTNOTE,
        ),
    ),
)
