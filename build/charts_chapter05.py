"""Chapter 5 teaching charts for FIN1209, as plain data.

Thirty five charts, A to Z and then AA to AI: the nine after Z were added
in review, once the alphabet was used up, and deckkit letters a twenty
seventh chart the way a spreadsheet letters its columns.
This file carries no drawing code: the three forms it uses, annotated,
gallery and bar_waves, live in build/chartkit.py, which knows nothing about any chapter,
and every entry below is data handed to one of them.

Chapter 5 has 59 figures and every one is placed in the deck. A chart is
drawn here only where the book makes a point in words that none of its own
figures shows:

  * **A** Dow's three trends by duration, which 5.1 states as a list.
  * **B** a correction or pullback beside a reversal or retracement.
  * **C** characteristic 11, the size and duration of a consolidation.
  * **D** characteristic 13, the average period range completed early.
  * **E** characteristic 15, the four cases of volume spread action.
  * **F and G** the three categories of filter on one breakout, and
    two-stage filtering. Figure 5.30 lists the filters and draws neither.
  * **H** the four scenarios of buying low and selling high.
  * **I, J, K and L** a stop order, slippage, a limit order, and the four
    exit orders. Figure 5.32 is a table of all of them and is placed too.
  * **M** three of the ways of initiating an entry, on one barrier.
  * **N** an inflection point of strength 2 beside one of strength 10.
  * **O** a double moving average crossover as a trend filter.
  * **P, Q and R** the book's proportional stopsizing, worked in pesos:
    what a fixed risk does to the tradesize, the tradesize capped, and the
    percentage risk that results.
  * **S** a trendline drawn, tentative, and confirmed.
  * **T** why a trendline holds: the orders on either side of it.
  * **U** an intraday penetration that closes back above the line.
  * **V and W** the factors of trendline reliability: angle, and retests.
  * **X** price failing to test a channel boundary before breaking out.
    The book makes this point on its Figure 5.14, which is placed with the
    characteristic it was drawn for.
  * **Y** the three ranges where Fibonacci, Dow and Gann converge.
  * **Z** the signs of a reversal that can be drawn on one top.
  * **AA** what a wave degree is: one wave drawn alone, then with its
    subwaves, then with theirs. It sits before Figure 5.5, which shows all
    three degrees at once and is where the book starts.
  * **AB** how the three wave cycles are drawn: one price as bars, the
    lower wave cycle, with the medium wave cycle dotted and the higher one
    thick over it, the line styles of Figure 5.5. It sits after that figure.
  * **AC** the same chart with a ruler under it for one swing of each
    cycle, so the three can be told apart by comparing them.
  * **AD** a breakout as Chapters 2 and 4 used the word: price leaving a
    consolidation range through its top, on Chapter 4's own PHP 40 to
    PHP 44 example. It is a recall, drawn so the next slide can widen it.
  * **AE** the four kinds of level this chapter breaks out of: the top of a
    range, a prior peak, a trendline and a channel line. The book never
    defines a breakout and no figure sets the four side by side.
  * **AF** Figure 5.8's three breakouts on price bars: one level at a prior
    peak of each wave cycle, and the bar that closes above it.
  * **AG** the bar stochastic measured on one bar with three closes. Figure
    5.18 shows the ratio falling over a run of bars, which is characteristic
    6, and not what the ratio is.
  * **AH** Figure 5.7 on price bars: one market that is flat, ranging and
    trending at once, by wave cycle.
  * **AI** Figure 5.9 on price bars, with the two places the smaller cycles
    turn and the largest does not, which the figure does not mark.

**Teach only what the textbook teaches.** Every label on these charts is a
statement the book's Chapter 5 makes, or arithmetic it sets out. Charts P,
Q and R are the book's five step procedure with numbers put in: an average
stopsize of PHP 2.00, a two standard deviation value of PHP 1.00, and
PHP 10,000 at risk. The pesos are ours and the steps are the book's.
Chart O computes two simple moving averages of the line it draws, a short
one and a long one, and marks where they cross; how a moving average is
built is Chapter 11 and no label explains it.
Chart AA is the one place the labels are a reading and not a quotation: the
book defines neither wave cycle nor wave degree in a sentence, so the chart
says what its Figure 5.5 and its words larger, smaller and subwave show, and
the slide beside it says that is where the reading comes from.

**The data is invented.** We hold no market data licence. Every price
series comes from chartkit.walk() with a fixed seed, offline and
reproducible, and every chart carries the credit line
deckkit.chart_credit() prints under it. Charts P, Q and R are not prices at
all: each is one line of arithmetic, and says so. Chart AA is not prices
either: it is three sine waves added one at a time, and says so.
Charts AB and AC are the same three waves with a little seeded noise, made
into price bars. The book draws its wave cycles freehand and gives no rule
for where the two smooth lines go, so their place on these two charts is
our drawing choice, and the bar counts and pesos on Chart AC's rulers are
read off our own chart. Both charts and both slides say so.
Charts AF, AH and AI are built the same way, each with its waves arranged
to show one thing: a slow rise added so the largest wave passes its own
peak, the largest wave left flat, and the three waves set to peak on one
bar. Chart AF's levels are the highs of its own bars and its breakouts the
first bar to close above each; nothing on it is the book's but the idea.
Chart AD is Chapter 4's worked range again. Charts AE and AG are not prices
at all: four shapes, and one bar drawn three times.
"""

from __future__ import annotations

import chartkit as ck
from chartkit import (Bar, Box, Bracket, ChartArt, Note, Sketch, Span, Stroke,
                      Trace)

# Every chart sits in the picture column of a Pair. Beside a teaching slide
# the text column is 5.6in wide; beside a term it is 6.2in, because a formal
# definition needs the room, and the picture column starts lower. These two
# widths are CHART_W and TERM_CHART_W in content_chapter05.py.
PAIR = ck.pair_size(5.6)
TERM = ck.pair_size(6.2, term=True)

INVENTED = "Invented prices."


def _line(pivots, seed, noise=0.004, wobble=0.05):
    return ck.walk(tuple(pivots), seed=seed, noise=noise, wobble=wobble)


def _straight(pivots):
    """A line through its pivots with nothing added: for a construction."""
    return ck.walk(tuple(pivots), seed=1, noise=0.0, wobble=0.0)


def _shaped(n, shape, seed, jitter=0.22):
    """Volume bars that follow a shape given as (index, level) knots."""
    import random
    rng = random.Random(seed)
    out = []
    for i in range(n):
        for (x0, y0), (x1, y1) in zip(shape[:-1], shape[1:]):
            if x0 <= i <= x1:
                level = y0 + (y1 - y0) * (i - x0) / max(1, x1 - x0)
                break
        out.append(level * rng.uniform(1 - jitter, 1 + jitter))
    return out


def _sma(series, n):
    """A simple moving average as (index, value) points, for a Stroke."""
    return tuple((i, sum(series[i - n + 1:i + 1]) / n)
                 for i in range(n - 1, len(series)))


def _on(x, x0=0.0, y0=40.0, slope=1 / 3):
    """The height of a sloping line at x."""
    return y0 + (x - x0) * slope


# --------------------------------------------------------------------------
# Chart A. Dow's three trends, by how long each lasts.
# --------------------------------------------------------------------------

A_SERIES = _line(
    ((0, 40), (9, 47), (13, 44), (24, 56), (28, 53), (40, 67), (44, 64),
     (54, 76), (58, 73), (62, 74.5), (68, 65), (71, 66.5), (76, 59),
     (86, 70), (90, 67), (102, 82), (106, 79), (118, 94), (122, 91),
     (128, 96)),
    seed=503)

# --------------------------------------------------------------------------
# Chart B. A correction or pullback, and a reversal or retracement.
# --------------------------------------------------------------------------

B_SERIES = _line(
    ((0, 40), (12, 49), (15, 47.5), (30, 60), (34, 58.2), (52, 76),
     (57, 73), (61, 75), (84, 50), (89, 53), (98, 46)),
    seed=509)

# --------------------------------------------------------------------------
# Chart C. Size and duration of a consolidation.
# --------------------------------------------------------------------------

C_SERIES = _line(
    ((0, 30), (14, 43), (17, 40.6), (20, 43.2), (23, 40.8), (26, 43.4),
     (46, 62), (52, 54), (59, 64), (66, 54.4), (73, 63.6), (80, 54),
     (87, 64), (94, 55), (100, 62)),
    seed=521)

# --------------------------------------------------------------------------
# Chart D. The average period range, completed before the day ends.
# --------------------------------------------------------------------------

D_SERIES = _line(
    ((0, 14), (7, 0), (20, 46), (25, 38), (40, 88), (45, 80), (58, 124),
     (62, 118), (68, 127), (76, 108), (82, 114), (96, 96)),
    seed=523, noise=0.0, wobble=0.06)

# --------------------------------------------------------------------------
# Chart E. Volume spread action: the four cases the book lists.
#
# Each cell is three bars over their volume. The first two are ordinary and
# the third is the extreme one, so the range and the volume are read against
# what came before and not against the other cells.
# --------------------------------------------------------------------------


def _vsa(name, note, last_bar, last_volume):
    """Three bars and three volume boxes. A bar is (open, high, low, close)."""
    bars = ((10.0, 13.0, 9.5, 12.4), (12.4, 15.2, 11.8, 14.6), last_bar)
    volumes = (3.0, 3.2, last_volume)
    points, sides, breaks = [], [], []
    for k, (o, h, l, c) in enumerate(bars):
        x = 2.0 + 3.0 * k
        if k:
            breaks.append(len(points))
        points += [(x - 0.45, o), (x, o), (x, l), (x, h), (x, c),
                   (x + 0.45, c)]
    for k, v in enumerate(volumes):
        x = 2.0 + 3.0 * k
        sides += [((x - 0.7, 0.0), (x - 0.7, v)), ((x - 0.7, v), (x + 0.7, v)),
                  ((x + 0.7, v), (x + 0.7, 0.0)),
                  ((x - 0.7, 0.0), (x + 0.7, 0.0))]
    # A floor under the volume and a gap between it and the prices, the same
    # in every cell.
    sides.append(((0.4, 0.0), (9.6, 0.0)))
    return Sketch(name=name, note=note, points=tuple(points),
                  sides=tuple(sides), breaks=tuple(breaks))


VSA = (
    _vsa("Large range, large volume", "trend promoting",
         (14.6, 25.0, 14.0, 24.4), 9.0),
    _vsa("Large range, low volume", "trend inhibiting: lack of commitment",
         (14.6, 25.0, 14.0, 24.4), 1.0),
    _vsa("Small range, large volume", "the squat bar: a potential reversal",
         (14.6, 15.6, 14.2, 15.0), 9.0),
    _vsa("Small range, low volume", "trend inhibiting",
         (14.6, 15.6, 14.2, 15.0), 1.0),
)

# --------------------------------------------------------------------------
# Charts F and G. One breakout filtered three ways, and two-stage filtering.
# --------------------------------------------------------------------------

F_SERIES = _line(
    ((0, 44), (8, 49.6), (14, 46), (22, 49.8), (28, 46.4), (36, 49.7),
     (40, 48), (46, 50.8), (50, 50.3), (58, 52.6), (62, 51.9), (72, 56)),
    seed=541, noise=0.002, wobble=0.03)

G_SERIES = _line(
    ((0, 46), (7, 49.4), (13, 47), (20, 49.6), (26, 47.4), (33, 49.5),
     (40, 48.4)),
    seed=643, noise=0.001, wobble=0.03)

# --------------------------------------------------------------------------
# Chart H. Buying low and selling high, four ways.
# --------------------------------------------------------------------------

H_SERIES = _line(
    ((0, 40), (20, 60), (23, 58.5), (44, 80), (48, 78), (66, 60),
     (69, 61.5), (88, 40)),
    seed=547, noise=0.002, wobble=0.02)

# --------------------------------------------------------------------------
# Charts I, J, K and L. Stop orders, slippage, limit orders and exits.
# --------------------------------------------------------------------------

I_SERIES = _line(
    ((0, 49.2), (6, 50.6), (12, 49.4), (18, 50.8), (24, 49.5), (30, 50.5),
     (36, 50)),
    seed=557, noise=0.001, wobble=0.02)

J_SERIES = (
    _line(((0, 53.2), (8, 51.4), (12, 52.2), (20, 50.2), (24, 49.2)),
          seed=563, noise=0.001, wobble=0.03)
    + _line(((0, 46.5), (5, 45.9), (10, 46.8), (18, 45.4), (24, 46)),
            seed=569, noise=0.001, wobble=0.03))

K_SERIES = I_SERIES

L_SERIES = _line(
    ((0, 49.4), (6, 50.5), (12, 49.5), (18, 50.6), (24, 49.6), (30, 50)),
    seed=571, noise=0.001, wobble=0.02)

# --------------------------------------------------------------------------
# Chart M. Three ways of initiating an entry, on one barrier.
# --------------------------------------------------------------------------

M_SERIES = _line(
    ((0, 47), (18, 59.6), (30, 52.5), (44, 59.4), (50, 63.6), (58, 59.5),
     (72, 53)),
    seed=577, noise=0.002, wobble=0.03)

# --------------------------------------------------------------------------
# Chart N. An inflection point of strength 2, and one of strength 10.
#
# One point is one bar. The small peak has two lower bars on either side
# and the third bar out is higher; the large one has ten.
# --------------------------------------------------------------------------

N_SERIES = _straight(
    ((0, 40), (6, 46), (8, 49), (10, 47.2), (11, 49.6), (20, 60),
     (30, 78), (40, 62), (46, 66), (56, 60)))

# --------------------------------------------------------------------------
# Chart O. A double moving average crossover as a trend filter.
# --------------------------------------------------------------------------

O_SERIES = _line(
    ((0, 54), (10, 50), (18, 47), (26, 50), (34, 57), (38, 55), (48, 66),
     (52, 63.5), (62, 73), (68, 70), (76, 62), (80, 64), (90, 54),
     (96, 52)),
    seed=587, noise=0.004, wobble=0.04)
O_SHORT = _sma(O_SERIES, 6)
O_LONG = _sma(O_SERIES, 18)


def _crossings(short, long):
    """Where the shorter average crosses the longer, as (x, y, upward)."""
    a = dict(short)
    out = []
    xs = [x for x, _y in long]
    for x0, x1 in zip(xs[:-1], xs[1:]):
        b = dict(long)
        d0, d1 = a[x0] - b[x0], a[x1] - b[x1]
        if d0 <= 0 < d1:
            out.append((x1, b[x1], True))
        elif d0 >= 0 > d1:
            out.append((x1, b[x1], False))
    return out


O_CROSS = _crossings(O_SHORT, O_LONG)
O_UP = next(c for c in O_CROSS if c[2])
O_DOWN = next(c for c in O_CROSS if not c[2] and c[0] > O_UP[0])

# --------------------------------------------------------------------------
# Charts P, Q and R. Proportional stopsizing, worked in pesos.
#
# One point is five centavos of stopsize. The book's five steps with numbers
# in: average stopsize 2.00, two standard deviations 1.00, so a proportional
# stopsize of 3.00; PHP 10,000 at risk, so a proportional tradesize of
# 10,000 / 3 = 3,333 shares.
# --------------------------------------------------------------------------

RISK = 10_000.0
THRESHOLD = 3.00
CAPITAL = 1_000_000.0

P_STOPS = [0.50 + 0.05 * i for i in range(111)]          # 0.50 to 6.00
P_SERIES = [RISK / s for s in P_STOPS]


def _at(stops, stop):
    return min(range(len(stops)), key=lambda i: abs(stops[i] - stop))


Q_SERIES = [min(RISK / THRESHOLD, RISK / s) for s in P_STOPS]
Q_UNCAPPED = tuple((i, RISK / s) for i, s in enumerate(P_STOPS)
                   if 1.00 <= s <= THRESHOLD)

R_STOPS = [0.05 * i for i in range(121)]                 # 0 to 6.00
R_SERIES = [min(RISK, RISK / THRESHOLD * s) / CAPITAL * 100 for s in R_STOPS]

# --------------------------------------------------------------------------
# Charts S to X. Trendlines and channels.
# --------------------------------------------------------------------------

S_SERIES = _line(
    ((0, 45), (10, 40), (22, 49.5), (34, 44), (46, 54), (58, 48),
     (70, 57.5)),
    seed=593, noise=0.002, wobble=0.03)

T_SERIES = _line(
    ((0, 44), (8, 52.5), (16, _on(16) + 0.2), (26, 58.5), (36, _on(36) + 0.2),
     (44, 62.5), (56, 52.6), (62, 51), (74, _on(74) - 0.3), (86, 56)),
    seed=599, noise=0.002, wobble=0.03)

U_SERIES = _line(
    ((0, 43), (10, 52.5), (20, _on(20) + 0.7), (30, 58.5), (40, _on(40) + 1.0),
     (50, 64.5), (60, _on(60) + 0.8), (70, 70)),
    seed=601, noise=0.002, wobble=0.03)

# Three uptrends side by side: one line each, on one pair of axes so the
# three slopes can be compared honestly.
V_STEEP = _straight(((0, 40), (4, 52), (6, 49), (10, 61), (12, 58),
                     (16, 70), (18, 67), (22, 79)))
V_MID = _straight(((0, 40), (7, 47.5), (10, 43.5), (17, 51.5), (20, 47.5),
                   (27, 55.5), (30, 51.5), (34, 57)))
V_FLAT = _straight(((0, 40), (7, 44), (10, 41.5), (17, 45.5), (20, 43),
                    (27, 47), (30, 44.5), (34, 48)))
# The three are laid end to end with a few idle points between them. The
# line is lifted at every one of those points, so nothing is drawn there.
V_GAP = 8
V_SERIES = V_STEEP + [40.0] * V_GAP + V_MID + [40.0] * V_GAP + V_FLAT
V_X1 = len(V_STEEP) + V_GAP
V_X2 = V_X1 + len(V_MID) + V_GAP
V_BREAKS = (tuple(range(len(V_STEEP), V_X1 + 1))
            + tuple(range(V_X1 + len(V_MID), V_X2 + 1)))

W_SERIES = _line(
    ((0, 46), (12, _on(12)), (21, 54.5), (30, _on(30)), (39, 60.5),
     (48, _on(48)), (57, 66.5), (66, _on(66)), (76, 73)),
    seed=607, noise=0.0015, wobble=0.03)

X_SERIES = _line(
    ((0, _on(0)), (9, _on(9) + 10), (18, _on(18)), (27, _on(27) + 10),
     (36, _on(36)), (45, _on(45) + 10), (54, _on(54) + 5.2),
     (63, _on(63) + 12.6), (72, _on(72) + 17)),
    seed=613, noise=0.0015, wobble=0.03)

# --------------------------------------------------------------------------
# Chart Y. Where the three approaches to retracement converge.
# --------------------------------------------------------------------------

Y_SERIES = _line(
    ((0, 42), (8, 40), (24, 51), (28, 49), (48, 60), (58, 54.5), (61, 56),
     (72, 50.3), (80, 53.5), (84, 52)),
    seed=617, noise=0.0015, wobble=0.03)

# --------------------------------------------------------------------------
# Chart Z. The signs of a reversal that can be drawn on one top.
# --------------------------------------------------------------------------

Z_SERIES = _line(
    ((0, 38), (14, 62), (22, 49), (36, 74), (43, 63.5), (56, 83), (62, 75.5),
     (72, 88), (76, 83.5), (84, 90), (88, 86.5), (92, 89.4), (104, 70),
     (108, 73), (114, 64)),
    seed=619, noise=0.003, wobble=0.04)
Z_VOLUME = _shaped(
    115, ((0, 150), (14, 160), (40, 120), (70, 78), (82, 52), (83, 230),
          (85, 240), (86, 110), (104, 130), (114, 120)), seed=631)


# --------------------------------------------------------------------------
# Chart AA. One wave, drawn at one, two and three wave degrees.
# --------------------------------------------------------------------------
# Not a price series: three sine waves of three sizes, added one at a time,
# so that the only thing that changes from one drawing to the next is the
# subwave that was added. Each drawing carries the one before it in green.

def _wave(parts, n=420):
    """(x, y) along a sum of sine waves, each given as (height, cycles)."""
    import math
    return tuple(
        (i / (n - 1),
         sum(h * math.sin(2 * math.pi * c * i / (n - 1)) for h, c in parts))
        for i in range(n))


def _trace(points):
    """A curve as the run of short straight sides a Sketch draws in green."""
    return tuple(zip(points[:-1], points[1:]))


AA_LARGE = ((10.0, 0.5),)
AA_MEDIUM = AA_LARGE + ((2.4, 4.5),)
AA_SMALL = AA_MEDIUM + ((1.1, 15.5),)

WAVES = (
    Sketch(name="1  One wave cycle",
           note="the largest: the highest degree",
           points=_wave(AA_LARGE)),
    Sketch(name="2  With its subwaves",
           note="smaller waves: a lower degree",
           points=_wave(AA_MEDIUM), sides=_trace(_wave(AA_LARGE))),
    Sketch(name="3  With their subwaves",
           note="smaller again: the lowest degree",
           points=_wave(AA_SMALL), sides=_trace(_wave(AA_MEDIUM))),
)


# --------------------------------------------------------------------------
# Charts AB and AC. One price as bars, with its two larger waves drawn on it.
# --------------------------------------------------------------------------
# The price is three waves added together, like Chart AA's third drawing,
# with a little seeded noise, and turned into open, high, low and close.
# The largest wave swings once across the chart in 96 bars, the medium one
# every 32 bars and the smallest every 8, so three medium swings fit inside
# the largest and four small ones inside a medium one. The sizes were picked
# for the picture, each wave three or four times as long as the next and
# twice as tall, and the slides say so: the instructor asked where the
# numbers came from. The two smooth lines are the waves the price was built from: the
# thick one is the largest alone and the dotted one is the largest plus the
# medium, which is why each runs through the middle of the smaller swings.
# The book gives no rule for drawing either line, so where they sit is our
# drawing choice and both slides say so.

AB_BARS = 97
AB_HIGH = (12.0, 96)    # half the swing in pesos, and bars in one swing
AB_MEDIUM = (6.0, 32)
AB_LOW = (3.0, 8)


def _degree_waves():
    import math
    import random
    rng = random.Random(977)
    higher, medium, closes = [], [], []
    for x in range(AB_BARS):
        h = 60.0 - AB_HIGH[0] * math.cos(2 * math.pi * x / AB_HIGH[1])
        m = h + AB_MEDIUM[0] * math.sin(2 * math.pi * x / AB_MEDIUM[1])
        low = AB_LOW[0] * math.sin(2 * math.pi * (x + 0.5) / AB_LOW[1])
        higher.append(h)
        medium.append(m)
        closes.append(m + low + rng.uniform(-0.3, 0.3))
    bars = []
    for x, c in enumerate(closes):
        o = closes[x - 1] if x else c - 0.6
        bars.append(Bar(open=o, close=c,
                        high=max(o, c) + rng.uniform(0.2, 0.7),
                        low=min(o, c) - rng.uniform(0.2, 0.7)))
    return tuple(bars), tuple(medium), tuple(higher)


AB_PRICE, AB_MWC, AB_HWC = _degree_waves()
AB_TRACES = (
    Trace(values=AB_HWC, tone="deep", width=3.4),
    Trace(values=AB_MWC, tone="structure", dotted=True, width=2.6),
)


# --------------------------------------------------------------------------
# Chart AJ. The three waves Charts AB and AC are built from, and their sum.
# --------------------------------------------------------------------------
# The same three waves as _degree_waves, each drawn alone and then added,
# with no noise and no bars, so the slide that says the price is invented
# can show what it was invented from. All four cells share one scale: a
# gallery fits every shape to its own cell, so each one carries two lone
# points at the top and bottom of the tallest, which draw nothing and hold
# the scale.

AJ_REACH = 22.0


def _ingredient(name, note, wave):
    import math
    points = tuple((x, wave(x, math)) for x in range(AB_BARS))
    return Sketch(
        name=name, note=note,
        points=points + ((0, AJ_REACH), (0, -AJ_REACH)),
        breaks=(len(points), len(points) + 1),
        sides=(((0, 0.0), (AB_BARS - 1, 0.0)),))


def _aj_big(x, math):
    return -AB_HIGH[0] * math.cos(2 * math.pi * x / AB_HIGH[1])


def _aj_medium(x, math):
    return AB_MEDIUM[0] * math.sin(2 * math.pi * x / AB_MEDIUM[1])


def _aj_small(x, math):
    return AB_LOW[0] * math.sin(2 * math.pi * (x + 0.5) / AB_LOW[1])


INGREDIENTS = (
    _ingredient("1  The big wave", "one swing: 96 bars, PHP 24 tall", _aj_big),
    _ingredient("2  The medium wave", "one swing: 32 bars, PHP 12 tall",
                _aj_medium),
    _ingredient("3  The small wave", "one swing: 8 bars, PHP 6 tall",
                _aj_small),
    _ingredient("4  Added together", "the invented price, before its noise",
                lambda x, math: (_aj_big(x, math) + _aj_medium(x, math)
                                 + _aj_small(x, math))),
)


# --------------------------------------------------------------------------
# Charts AD and AE. Breakout as Chapters 2 and 4 used it, and what Chapter 5
# adds.
# --------------------------------------------------------------------------
# AD is Chapter 4's own example again: a share ranging between PHP 40 and
# PHP 44 that leaves the range through its top. AE is four small shapes, each
# with the level price gets through in green: the top of a range, which is
# the earlier chapters' case, and the three this chapter adds to it.

AD_SERIES = _line(
    ((0, 51), (10, 40.8), (14, 43.5), (19, 40.4), (24, 43.6), (29, 40.5),
     (34, 43.5), (39, 40.6), (44, 43.4), (48, 41.6), (54, 46.2), (57, 45.2),
     (67, 52.5), (70, 51), (76, 56)),
    seed=571, noise=0.003, wobble=0.03)

LEVELS = (
    Sketch(name="The top of a range",
           note="Chapters 2 and 4",
           points=((0, 2.4), (1, 3.9), (2, 1.1), (3, 3.9), (4, 1.1), (5, 3.9),
                   (6, 1.1), (7, 3.8), (8, 2.8), (9.4, 6.4), (10.1, 5.7),
                   (11, 7.4)),
           sides=(((0.4, 4.1), (11, 4.1)),)),
    Sketch(name="A prior peak",
           note="one at every wave degree: section 5.1",
           points=((0, 0), (3, 5), (5, 2.4), (8.4, 7.4), (9.2, 6.6),
                   (10.4, 8.4)),
           sides=(((3, 5), (10.4, 5)),)),
    Sketch(name="A trendline",
           note="sections 5.2 and 5.6",
           points=((0, 8), (1.5, 5.4), (3, 6.9), (4.5, 4.1), (6, 5.6),
                   (7.2, 3.2), (9.5, 7.2), (10.2, 6.4), (11, 8)),
           sides=(((0, 8.1), (11, 4.4)),)),
    Sketch(name="A channel line",
           note="section 5.6",
           points=((0, 1), (1.5, 4.15), (3, 2.6), (4.5, 5.65), (6, 4.1),
                   (7.5, 7.15), (8.6, 6.2), (10.4, 10.4), (11, 9.8)),
           sides=(((0, 3.5), (11, 9.0)), ((0, 0.9), (11, 6.4)))),
)

# --------------------------------------------------------------------------
# Chart AF. The three breakouts of Figure 5.8, on price bars.
# --------------------------------------------------------------------------
# The same three waves as Chart AB with a slow rise added, so that the
# largest wave peaks, falls back and then passes its own peak, which is what
# Figure 5.8 draws. Each level is the high of a prior peak, read off the
# bars, and each breakout is the first bar that closes above it.

AF_BARS = 121


def _breakout_waves():
    import math
    import random
    rng = random.Random(431)
    higher, medium, closes = [], [], []
    for x in range(AF_BARS):
        h = 55.0 + 0.10 * x + 10.0 * math.sin(2 * math.pi * x / 96)
        m = h + 5.0 * math.sin(2 * math.pi * x / 32)
        low = 2.5 * math.sin(2 * math.pi * (x + 0.5) / 8)
        higher.append(h)
        medium.append(m)
        closes.append(m + low + rng.uniform(-0.3, 0.3))
    bars = []
    for x, c in enumerate(closes):
        o = closes[x - 1] if x else c - 0.6
        bars.append(Bar(open=o, close=c,
                        high=max(o, c) + rng.uniform(0.2, 0.7),
                        low=min(o, c) - rng.uniform(0.2, 0.7)))
    return tuple(bars), tuple(medium), tuple(higher)


def _level(bars, first, last):
    """A prior peak between two bars, and the first bar to close above it:
    (bar of the peak, its high, bar of the breakout)."""
    at = max(range(first, last + 1), key=lambda x: bars[x].high)
    high = bars[at].high
    out = next(x for x in range(at + 1, len(bars)) if bars[x].close > high)
    return at, high, out


AF_PRICE, AF_MWC, AF_HWC = _breakout_waves()
AF_TRACES = (
    Trace(values=AF_HWC, tone="deep", width=3.0),
    Trace(values=AF_MWC, tone="structure", dotted=True, width=2.4),
)
AF_HIGH = _level(AF_PRICE, 20, 50)      # the top of the whole move
AF_MED = _level(AF_PRICE, 68, 78)       # the last medium peak before it
AF_LOW = _level(AF_PRICE, 79, 85)       # the last small peak before that

# --------------------------------------------------------------------------
# Chart AG. The bar stochastic, measured on three bars.
# --------------------------------------------------------------------------
# One bar three times, with a low of PHP 40 and a high of PHP 50 each time
# and only the close moved: PHP 48, PHP 45 and PHP 42. The ratio is the
# book's, printed on its Figure 5.18; the pesos are ours.


def _stochastic_bar(name, note, close):
    low, high, open_ = 40.0, 50.0, 44.0
    return Sketch(
        name=name, note=note,
        points=((-0.5, open_), (0, open_), (0, low), (0, high), (0, close),
                (0.5, close)),
        sides=(((-1.6, high), (1.6, high)), ((-1.6, low), (1.6, low))))


STOCHASTIC = (
    _stochastic_bar("Close PHP 48: 0.80", "near the high of the bar", 48.0),
    _stochastic_bar("Close PHP 45: 0.50", "the middle of the bar", 45.0),
    _stochastic_bar("Close PHP 42: 0.20", "near the low of the bar", 42.0),
)

# --------------------------------------------------------------------------
# Charts AH and AI. Figure 5.7 and Figure 5.9, on price bars.
# --------------------------------------------------------------------------
# AH is a market whose largest wave is flat: the medium wave swings across
# one level and the small one climbs and falls along it, so the one chart is
# flat, ranging and trending at once. AI is Chart AB's price with the three
# waves set to peak on the same bar, so the one turn of the largest wave is
# also a turn of the two smaller ones.


def _mode_waves():
    import math
    import random
    rng = random.Random(613)
    higher, medium, closes = [], [], []
    for x in range(AB_BARS):
        h = 60.0
        m = h - 6.0 * math.cos(2 * math.pi * x / 32)
        low = 2.2 * math.sin(2 * math.pi * (x + 0.5) / 8)
        higher.append(h)
        medium.append(m)
        closes.append(m + low + rng.uniform(-0.3, 0.3))
    bars = []
    for x, c in enumerate(closes):
        o = closes[x - 1] if x else c - 0.6
        bars.append(Bar(open=o, close=c,
                        high=max(o, c) + rng.uniform(0.2, 0.7),
                        low=min(o, c) - rng.uniform(0.2, 0.7)))
    return tuple(bars), tuple(medium), tuple(higher)


def _synced_waves():
    import math
    import random
    rng = random.Random(829)
    top = AB_BARS // 2
    higher, medium, closes = [], [], []
    for x in range(AB_BARS):
        h = 60.0 - AB_HIGH[0] * math.cos(2 * math.pi * x / AB_HIGH[1])
        m = h + AB_MEDIUM[0] * math.cos(2 * math.pi * (x - top) / AB_MEDIUM[1])
        low = AB_LOW[0] * math.cos(2 * math.pi * (x - top) / AB_LOW[1])
        higher.append(h)
        medium.append(m)
        closes.append(m + low + rng.uniform(-0.3, 0.3))
    bars = []
    for x, c in enumerate(closes):
        o = closes[x - 1] if x else c - 0.6
        bars.append(Bar(open=o, close=c,
                        high=max(o, c) + rng.uniform(0.2, 0.7),
                        low=min(o, c) - rng.uniform(0.2, 0.7)))
    return tuple(bars), tuple(medium), tuple(higher)


AH_PRICE, AH_MWC, AH_HWC = _mode_waves()
AH_TRACES = (
    Trace(values=AH_HWC, tone="deep", width=3.4),
    Trace(values=AH_MWC, tone="structure", dotted=True, width=2.6),
)
AI_PRICE, AI_MWC, AI_HWC = _synced_waves()
AI_TRACES = (
    Trace(values=AI_HWC, tone="deep", width=3.4),
    Trace(values=AI_MWC, tone="structure", dotted=True, width=2.6),
)


# --------------------------------------------------------------------------
# The thirty six charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.annotated,
        kwargs=dict(
            series=A_SERIES,
            size=PAIR,
            spans=(Span(x0=58, x1=76,
                        label="Secondary reaction:\nweeks to months"),),
            strokes=(
                Stroke(points=((6, 33), (124, 84)), arrow=True,
                       label="Primary trend: months to years", at=0,
                       dx=74, dy=6),
            ),
            notes=(
                Note(x=26, label="Minor trends:\ndays to weeks", dx=-16,
                     dy=46),
            ),
            top=0.10, bottom=0.20,
            footnote=INVENTED + " One line holds all three of Dow's trends.",
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.annotated,
        kwargs=dict(
            series=B_SERIES,
            size=TERM,
            notes=(
                Note(x=34, label="Correction or\npullback: shallow,\n"
                     "usually no more than\na few percent", dx=-4, dy=56),
                Note(x=84, label="Reversal or retracement:\nmay be of any "
                     "amount\nor degree", dx=-34, dy=-34, notice=True),
            ),
            top=0.10, bottom=0.34,
            footnote=INVENTED + " Four words in the book, and two sizes of "
                     "move.",
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.annotated,
        kwargs=dict(
            series=C_SERIES,
            size=PAIR,
            boxes=(
                Box(x0=13, x1=27, lo=39.8, hi=44.2),
                Box(x0=45, x1=95, lo=53, hi=65, where="above", tone="notice",
                    label="Taller and wider: a more significant\ninterruption "
                          "of the trend"),
            ),
            notes=(
                Note(x=24, y=39.8, label="Shorter and narrower:\na lesser "
                     "interruption", dx=26, dy=-26, dot=False),
            ),
            top=0.26, bottom=0.10,
            footnote=INVENTED + " The same kind of sideways movement, at two "
                     "sizes.",
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.annotated,
        kwargs=dict(
            series=D_SERIES,
            size=TERM,
            xlabel="One trading day",
            ylabel="Pips from the day's low",
            price_ticks=(0, 60, 120),
            strokes=(
                Stroke(points=((0, 0), (98, 0)), dashed=True, tone="quiet"),
                Stroke(points=((0, 120), (98, 120)), dashed=True,
                       tone="notice",
                       label="120 pips: the average daily range", at=0,
                       dx=4, dy=11),
            ),
            notes=(
                Note(x=58, label="Beyond the average\nrange before the day\n"
                     "completes: potential\nexhaustion", dx=-70, dy=-33,
                     notice=True),
                Note(x=96, label="The day\nends", dx=-10, dy=-46, dot=False),
            ),
            top=0.20, bottom=0.08,
            footnote="An invented currency pair. Its average daily range is "
                     "the book's example, 120 pips.\nThe book does not say "
                     "what a pip is.",
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.gallery,
        kwargs=dict(sketches=VSA, cols=2, size=PAIR,
                    footnote="Each drawing: three bars over their volume. "
                             "The third bar is the extreme one."),
    ),
    ChartArt(
        letter="F",
        draw=ck.annotated,
        kwargs=dict(
            series=F_SERIES,
            size=PAIR,
            spans=(Span(x0=46, x1=54, label="N closed bars"),),
            strokes=(
                Stroke(points=((0, 50), (74, 50)), dashed=True, tone="quiet",
                       label="The level", at=0, dx=4, dy=9),
                Stroke(points=((40, 52.6), (74, 52.6)), dashed=True,
                       tone="notice"),
            ),
            notes=(
                Note(x=46, label="Event-based: enter when\na bar closes "
                     "beyond the level", dx=-96, dy=44),
                Note(x=54, label="Time-based: enter after\nN closed bars",
                     dx=-44, dy=-66),
                Note(x=58, label="Price-based: enter at a\nset price beyond "
                     "the level", dx=-74, dy=62, notice=True),
            ),
            top=0.50, bottom=0.34,
            footnote=INVENTED + " One breakout, and three different entries.",
        ),
    ),
    ChartArt(
        letter="G",
        draw=ck.annotated,
        kwargs=dict(
            series=G_SERIES,
            size=PAIR,
            extend=44,
            boxes=(
                Box(x0=-1, x1=84, lo=50, hi=51.6, tone="notice"),
            ),
            strokes=(
                Stroke(points=((-1, 50), (84, 50)), tone="quiet",
                       label="The entry level", at=1, dx=-4, dy=-10),
                Stroke(points=((-1, 51.6), (84, 51.6)), tone="notice",
                       width=1.0,
                       label="The price-based filter:\nenter only within "
                             "this distance", at=0, dx=6, dy=20),
                Stroke(points=((40, 48.4), (54, 50.9)), dashed=True,
                       arrow=True,
                       label="Closes within the\ndistance: entry taken",
                       at=1, dx=8, dy=-58),
                Stroke(points=((40, 48.4), (54, 55.4)), dashed=True,
                       arrow=True, tone="notice",
                       label="Closes too far beyond:\nentry refused", at=1,
                       dx=8, dy=4),
            ),
            top=0.20, bottom=0.14,
            footnote=INVENTED + " The same closing violation, two ways. "
                     "Only the distance differs.",
        ),
    ),
    ChartArt(
        letter="H",
        draw=ck.annotated,
        kwargs=dict(
            series=H_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((7, 40.5), (19, 52.5)), arrow=True,
                       label="1  Buy low,\nsell high", at=1, dx=8, dy=-16),
                Stroke(points=((29, 62.5), (41, 74.5)), arrow=True,
                       label="2  Buy high,\nsell higher", at=0, dx=-8,
                       dy=40),
                Stroke(points=((51, 80.5), (63, 68.5)), arrow=True,
                       tone="notice",
                       label="3  Sell high,\nbuy back lower", at=1, dx=8,
                       dy=30),
                Stroke(points=((72, 60.5), (84, 48.5)), arrow=True,
                       tone="notice",
                       label="4  Sell low,\nbuy back\neven lower", at=0,
                       dx=12, dy=22),
            ),
            top=0.22, bottom=0.10,
            footnote=INVENTED + " Green arrows are the two longs, gold the "
                     "two shorts.",
        ),
    ),
    ChartArt(
        letter="I",
        draw=ck.annotated,
        kwargs=dict(
            series=I_SERIES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(48, 50, 52),
            extend=44,
            strokes=(
                Stroke(points=((0, 52), (80, 52)), dashed=True,
                       tone="quiet", label="Buystop at PHP 52", at=0, dx=4,
                       dy=9),
                Stroke(points=((0, 48), (80, 48)), dashed=True,
                       tone="quiet", label="Sellstop at PHP 48", at=0, dx=4,
                       dy=-9),
                Stroke(points=((36, 50), (50, 52), (55, 51.6), (74, 55)),
                       dashed=True, arrow=True,
                       label="Triggered at 52:\nbuys at the market", at=3,
                       dx=-4, dy=20),
                Stroke(points=((36, 50), (50, 48), (55, 48.4), (74, 45)),
                       dashed=True, arrow=True, tone="notice",
                       label="Triggered at 48:\nsells at the market", at=3,
                       dx=-4, dy=-20),
            ),
            notes=(
                Note(x=36, label="Now: PHP 50", dx=-58, dy=0),
            ),
            top=0.42, bottom=0.42,
            footnote=INVENTED + " Stop entries are placed when a "
                     "continuation is expected.",
        ),
    ),
    ChartArt(
        letter="J",
        draw=ck.annotated,
        kwargs=dict(
            series=J_SERIES,
            size=TERM,
            ylabel="Price (PHP)",
            price_ticks=(46.5, 48, 50, 52),
            breaks=(25,),
            strokes=(
                Stroke(points=((0, 48), (50, 48)), dashed=True, tone="quiet",
                       label="Stoploss at PHP 48", at=0, dx=4, dy=9),
            ),
            brackets=(
                Bracket(x=25, lo=46.5, hi=48, label="Slippage:\nPHP 1.50",
                        notice=True, side="left"),
            ),
            notes=(
                Note(x=24, label="Last price before\nthe gap: PHP 49.20",
                     dx=14, dy=30),
                Note(x=25, label="Filled at PHP 46.50", dx=24, dy=-32,
                     notice=True),
            ),
            top=0.14, bottom=0.30,
            footnote=INVENTED + " The line is lifted at the gap: nothing "
                     "traded between.",
        ),
    ),
    ChartArt(
        letter="K",
        draw=ck.annotated,
        kwargs=dict(
            series=K_SERIES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(47, 50, 53),
            extend=44,
            strokes=(
                Stroke(points=((0, 53), (80, 53)), dashed=True,
                       tone="quiet", label="Sell limit at PHP 53", at=0,
                       dx=4, dy=-9),
                Stroke(points=((0, 47), (80, 47)), dashed=True,
                       tone="quiet", label="Buy limit at PHP 47", at=0, dx=4,
                       dy=9),
                Stroke(points=((36, 50), (52, 53), (58, 52.2), (76, 49.4)),
                       dashed=True, arrow=True, tone="notice",
                       label="Filled at 53 or better:\nsold, expecting a "
                             "reversal", at=1, dx=-4, dy=28),
                Stroke(points=((36, 50), (52, 47), (58, 47.8), (76, 50.6)),
                       dashed=True, arrow=True,
                       label="Filled at 47 or better:\nbought, expecting a "
                             "reversal", at=1, dx=-4, dy=-28),
            ),
            notes=(
                Note(x=36, label="Now: PHP 50", dx=-58, dy=0),
            ),
            top=0.50, bottom=0.50,
            footnote=INVENTED + " Limit entries are placed when a reversal "
                     "is expected.",
        ),
    ),
    ChartArt(
        letter="L",
        draw=ck.annotated,
        kwargs=dict(
            series=L_SERIES,
            size=PAIR,
            extend=62,
            strokes=(
                Stroke(points=((34, 55), (92, 55)), dashed=True,
                       label="Sell limit: take profit on a long", at=0,
                       dx=4, dy=10),
                Stroke(points=((34, 52.6), (92, 52.6)), dashed=True,
                       tone="quiet",
                       label="Buystop: cut the loss on a short", at=0, dx=4,
                       dy=10),
                Stroke(points=((34, 47.4), (92, 47.4)), dashed=True,
                       tone="quiet",
                       label="Sellstop: cut the loss on a long", at=0, dx=4,
                       dy=-10),
                Stroke(points=((34, 45), (92, 45)), dashed=True,
                       label="Buy limit: take profit on a short", at=0,
                       dx=4, dy=-10),
            ),
            notes=(
                Note(x=30, label="The current\nmarket price", dx=-58,
                     dy=-56),
            ),
            top=0.28, bottom=0.28,
            footnote=INVENTED + " Green lines are limit orders, grey lines "
                     "are stop orders.",
        ),
    ),
    ChartArt(
        letter="M",
        draw=ck.annotated,
        kwargs=dict(
            series=M_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, 60), (74, 60)), dashed=True, tone="quiet",
                       label="A barrier: resistance", at=0, dx=4, dy=10),
            ),
            notes=(
                Note(x=18, label="Barrier entry: short\nat the resistance",
                     dx=-22, dy=-66),
                Note(x=47, label="Breakout entry: buy as\nprice breaks "
                     "above", dx=-70, dy=52),
                Note(x=60, label="Failed breakout entry:\nshort as price "
                     "falls back", dx=-14, dy=-70, notice=True),
            ),
            top=0.46, bottom=0.44,
            footnote=INVENTED + " Random and pattern-based entries have "
                     "nothing to mark on one line.",
        ),
    ),
    ChartArt(
        letter="N",
        draw=ck.annotated,
        kwargs=dict(
            series=N_SERIES,
            size=TERM,
            spans=(
                Span(x0=6, x1=10, label="2 bars\neach side"),
                Span(x0=20, x1=40, label="10 bars on either side",
                     tone="notice"),
            ),
            strokes=(
                Stroke(points=((30, 78), (58, 78)), dashed=True,
                       tone="notice", label="Its resistance level", at=1,
                       dx=-4, dy=10),
            ),
            notes=(
                Note(x=8, label="Strength 2", dx=14, dy=-34),
                Note(x=30, label="Strength 10:\na significant\npeak", dx=-40,
                     dy=0, notice=True),
            ),
            top=0.16, bottom=0.30,
            footnote="An invented line. One point is one bar.",
        ),
    ),
    ChartArt(
        letter="O",
        draw=ck.annotated,
        kwargs=dict(
            series=O_SERIES,
            size=TERM,
            strokes=(
                Stroke(points=O_SHORT, tone="structure",
                       label="Shorter average", at=len(O_SHORT) - 1, dx=-6,
                       dy=-19, width=1.8),
                Stroke(points=O_LONG, tone="notice", label="Longer average",
                       at=len(O_LONG) - 1, dx=-6, dy=70, width=1.8),
            ),
            notes=(
                Note(x=O_UP[0], y=O_UP[1],
                     label="Shorter crosses above the\nlonger: a potential "
                           "uptrend", dx=26, dy=-26),
                Note(x=O_DOWN[0], y=O_DOWN[1],
                     label="Shorter crosses below:\na potential downtrend",
                     dx=-34, dy=52, notice=True),
            ),
            top=0.50, bottom=0.34,
            footnote=INVENTED + " Simple moving averages of 6 and 18 bars:"
                     "\nlengths we chose so the crossings show. Moving "
                     "averages are Chapter 11.",
        ),
    ),
    ChartArt(
        letter="P",
        draw=ck.annotated,
        kwargs=dict(
            series=P_SERIES,
            size=PAIR,
            xlabel="Stopsize, from PHP 0.50 to PHP 6.00",
            ylabel="Tradesize (shares)",
            price_ticks=(2000, 5000, 10000, 20000),
            notes=(
                Note(x=_at(P_STOPS, 0.50), label="PHP 0.50 stop:\n20,000 "
                     "shares", dx=26, dy=-6, notice=True),
                Note(x=_at(P_STOPS, 2.00), label="PHP 2.00 stop:\n5,000 "
                     "shares", dx=22, dy=44),
                Note(x=_at(P_STOPS, 5.00), label="PHP 5.00 stop:\n2,000 "
                     "shares", dx=-20, dy=46),
            ),
            top=0.08, bottom=0.08,
            footnote="Arithmetic, not prices: PHP 10,000 at risk, divided by "
                     "the stopsize.",
        ),
    ),
    ChartArt(
        letter="Q",
        draw=ck.annotated,
        kwargs=dict(
            series=Q_SERIES,
            size=TERM,
            xlabel="Stopsize, from PHP 0.50 to PHP 6.00",
            ylabel="Tradesize (shares)",
            price_ticks=(2000, 3333, 10000),
            strokes=(
                Stroke(points=Q_UNCAPPED, dashed=True, tone="quiet",
                       label="Without it", at=4, dx=16, dy=4),
            ),
            notes=(
                Note(x=_at(P_STOPS, 1.50), label="Held at 3,333 shares", dx=6,
                     dy=-26),
                Note(x=_at(P_STOPS, 3.00), label="The proportional\nstopsize: "
                     "PHP 3.00", dx=22, dy=72, notice=True),
                Note(x=_at(P_STOPS, 5.00), label="PHP 5.00 stop:\n2,000 "
                     "shares", dx=-6, dy=36),
            ),
            top=0.06, bottom=0.22,
            footnote="Arithmetic, not prices: the worked example beside "
                     "this chart.",
        ),
    ),
    ChartArt(
        letter="R",
        draw=ck.annotated,
        kwargs=dict(
            series=R_SERIES,
            size=PAIR,
            xlabel="Stopsize, from zero to PHP 6.00",
            ylabel="Risk per trade (% of capital)",
            price_ticks=(0, 0.5, 1.0),
            notes=(
                Note(x=_at(R_STOPS, 1.50), label="PHP 1.50 stop: 3,333 "
                     "shares\nrisk PHP 5,000, or 0.5%", dx=22, dy=-22),
                Note(x=_at(R_STOPS, 3.00), label="PHP 3.00 stop: PHP 10,000,"
                     "\nthe 1% maximum", dx=-14, dy=40, notice=True),
                Note(x=_at(R_STOPS, 5.00), label="PHP 5.00 stop:\n2,000 "
                     "shares, still 1%", dx=-14, dy=-44),
            ),
            top=0.34, bottom=0.10,
            footnote="Arithmetic, not prices. The risk varies in proportion "
                     "to the stopsize, then is capped.",
        ),
    ),
    ChartArt(
        letter="S",
        draw=ck.annotated,
        kwargs=dict(
            series=S_SERIES,
            size=TERM,
            ylabel="Price (PHP)",
            price_ticks=(40, 44, 48),
            extend=10,
            spans=(
                Span(x0=34, x1=58, label="Tentative"),
                Span(x0=58, x1=80, label="Confirmed", tone="notice"),
            ),
            strokes=(
                Stroke(points=((10, 40), (34, 44))),
                Stroke(points=((34, 44), (58, 48), (80, 51.67)), dashed=True,
                       arrow=True),
            ),
            notes=(
                Note(x=10, label="Trough 1:\nPHP 40", dx=14, dy=-22),
                Note(x=34, label="Trough 2:\nPHP 44", dx=10, dy=-26),
                Note(x=58, label="Third contact", dx=10, dy=-30,
                     notice=True),
            ),
            top=0.12, bottom=0.34,
            footnote=INVENTED + " The dashed part is the line projected "
                     "into the future.",
        ),
    ),
    ChartArt(
        letter="T",
        draw=ck.annotated,
        kwargs=dict(
            series=T_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, _on(0)), (86, _on(86))),
                       label="The trendline", at=0, dx=8, dy=-14),
            ),
            notes=(
                Note(x=16, label="From above: buy orders\ntriggered. "
                     "Temporary support.", dx=44, dy=-52),
                Note(x=74, label="From below: sell orders\ntriggered. "
                     "Temporary resistance.", dx=-132, dy=42, notice=True),
            ),
            top=0.30, bottom=0.26,
            footnote=INVENTED + " One line, met first from above and later "
                     "from below.",
        ),
    ),
    ChartArt(
        letter="U",
        draw=ck.annotated,
        kwargs=dict(
            series=U_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, _on(0)), (70, _on(70)))),
                Stroke(points=((0, _on(0) - 5), (70, _on(70) - 5)),
                       dashed=True, tone="notice",
                       label="A price-based filter:\nvalid only beyond here",
                       at=1, dx=-4, dy=-26),
                Stroke(points=((40, _on(40) + 1.0), (40, _on(40) - 3.4)),
                       tone="quiet", width=2.6),
            ),
            notes=(
                Note(x=40, y=_on(40) - 3.4, label="The intraday low:\nwell "
                     "through the line", dx=-30, dy=-46, dot=False),
                Note(x=40, label="The close: back above.\nSignificant, but "
                     "invalid.", dx=-30, dy=62, notice=True),
            ),
            top=0.22, bottom=0.26,
            footnote=INVENTED + " Black: closing prices. Green: the uptrend "
                     "line. Grey bar: one day's low.",
        ),
    ),
    ChartArt(
        letter="V",
        draw=ck.annotated,
        kwargs=dict(
            series=V_SERIES,
            size=PAIR,
            breaks=V_BREAKS,
            xlabel="",
            ylabel="",
            strokes=(
                Stroke(points=((0, 40), (22, 73)),
                       label="Above 45 degrees:\nsteep, less stable", at=1,
                       dx=8, dy=20, tone="quiet"),
                Stroke(points=((V_X1, 39.5), (V_X1 + 34, 53.1)),
                       label="About 35 to 45\ndegrees: the\nmost reliable",
                       at=1, dx=-4, dy=62),
                Stroke(points=((V_X2, 40), (V_X2 + 34, 45.1)),
                       label="Very shallow:\nweak, less stable", at=1,
                       dx=-6, dy=38, tone="quiet"),
            ),
            top=0.12, bottom=0.06,
            footnote="Three invented uptrends on one pair of axes. The "
                     "angle of a line depends on the scaling used.",
        ),
    ),
    ChartArt(
        letter="W",
        draw=ck.annotated,
        kwargs=dict(
            series=W_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((4, _on(4)), (76, _on(76)))),
            ),
            notes=(
                Note(x=12, label="1", dx=4, dy=-22),
                Note(x=30, label="2", dx=4, dy=-22),
                Note(x=48, label="3", dx=4, dy=-22),
                Note(x=66, label="4", dx=4, dy=-22),
                Note(x=48, label="Four retests, each\none precise: price "
                     "touches\nthe line and is rejected", dx=-84, dy=78,
                     notice=True),
            ),
            top=0.34, bottom=0.20,
            footnote=INVENTED + " The green line is the trendline. More and "
                     "cleaner retests: more orders at it.",
        ),
    ),
    ChartArt(
        letter="X",
        draw=ck.annotated,
        kwargs=dict(
            series=X_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, _on(0)), (72, _on(72))),
                       label="Channel bottom", at=0, dx=30, dy=-12),
                Stroke(points=((0, _on(0) + 10), (72, _on(72) + 10)),
                       label="Channel top", at=0, dx=6, dy=16),
            ),
            notes=(
                Note(x=54, label="Fails to test the\nchannel bottom", dx=4,
                     dy=-60, notice=True),
                Note(x=63, label="Breaks out through\nthe channel top",
                     dx=-126, dy=26),
            ),
            top=0.14, bottom=0.14,
            footnote=INVENTED + " The failed test comes first, and the "
                     "breakout is on the other side.",
        ),
    ),
    ChartArt(
        letter="Y",
        draw=ck.annotated,
        kwargs=dict(
            series=Y_SERIES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(40, 50, 60),
            extend=34,
            boxes=(
                Box(x0=48, x1=118, lo=52.36, hi=53.40, tone="notice"),
                Box(x0=48, x1=118, lo=49.80, hi=50.20, tone="notice"),
                Box(x0=48, x1=118, lo=46.80, hi=47.64, tone="notice"),
            ),
            brackets=(
                Bracket(x=2, lo=40, hi=60, label="The rise:\nPHP 20"),
            ),
            notes=(
                Note(x=118, y=52.88, label="33 to 38.2%", dx=-66, dy=20,
                     dot=False),
                Note(x=118, y=50.0, label="50%: PHP 50", dx=-66, dy=-17,
                     notice=True, dot=False),
                Note(x=118, y=47.22, label="61.8 to 66%", dx=-66, dy=-18,
                     dot=False),
            ),
            top=0.10, bottom=0.08,
            footnote=INVENTED + " The three bands are where Fibonacci, Dow "
                     "and Gann converge.",
        ),
    ),
    ChartArt(
        letter="Z",
        draw=ck.annotated,
        kwargs=dict(
            series=Z_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((30, 91.5), (114, 91.5)), dashed=True,
                       tone="quiet",
                       label="A significant historical resistance level",
                       at=0, dx=4, dy=11),
            ),
            notes=(
                Note(x=62, label="Cycle amplitude decreasing\nduring the "
                     "trend", dx=-10, dy=-70),
            ),
            volume=Z_VOLUME,
            volume_label="Volume",
            volume_strokes=(
                Stroke(points=((16, 250), (78, 130)), arrow=True,
                       tone="structure", label="Diminishing volume", at=0,
                       dx=26, dy=16),
            ),
            volume_notes=(
                Note(x=84, y=250, label="Buying climax:\nextreme volume",
                     dx=10, dy=6, notice=True, dot=False),
            ),
            top=0.22, bottom=0.30,
            footnote=INVENTED + " Three kinds of sign at one market top.",
        ),
    ),
    ChartArt(
        letter="AA",
        draw=ck.gallery,
        kwargs=dict(sketches=WAVES, cols=3, size=PAIR,
                    footnote="Not prices: one wave, drawn three times. In "
                             "green, the wave of the drawing before."),
    ),
    ChartArt(
        letter="AJ",
        draw=ck.gallery,
        kwargs=dict(sketches=INGREDIENTS, cols=2, size=PAIR,
                    footnote="Not a market: the three waves this course added "
                             "together, all four drawn to one scale.\nIn "
                             "green, the level each one swings around."),
    ),
    ChartArt(
        letter="AB",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AB_PRICE, traces=AB_TRACES, size=PAIR,
            notes=(
                Note(x=33, label="LWC: the price\nitself, here\nas bars",
                     dx=-24, dy=40),
                Note(x=57, y=AB_MWC[57], label="MWC: the dotted line",
                     dx=-30, dy=-92),
                Note(x=84, y=AB_HWC[84], label="HWC: the\nthick line",
                     dx=-4, dy=118),
            ),
            price_ticks=(40, 50, 60, 70, 80),
            top=0.12, bottom=0.08,
            footnote="Invented: three waves added together. Dotted: big plus "
                     "medium. Thick: big alone.\nThe bars and the place of "
                     "both lines are our drawing; the book gives no rule.",
        ),
    ),
    ChartArt(
        letter="AC",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AB_PRICE, traces=AB_TRACES, size=PAIR,
            strokes=(
                Stroke(points=((0, 33.0), (8, 33.0)), width=3.0,
                       label="One LWC swing: 8 bars, about PHP 6", at=1,
                       dx=8, dy=0),
                Stroke(points=((0, 27.5), (32, 27.5)), width=3.0,
                       label="One MWC swing: 32 bars, about PHP 12", at=1,
                       dx=8, dy=0),
                Stroke(points=((0, 22.0), (96, 22.0)), width=3.0,
                       label="The HWC swing: 96 bars, PHP 24", at=1,
                       dx=-8, dy=-12),
            ),
            price_ticks=(40, 50, 60, 70, 80),
            top=0.05, bottom=0.12,
            footnote=INVENTED + " Bars: LWC. Dotted: MWC. Thick: HWC. The "
                     "rulers show the sizes we built in.",
        ),
    ),
    ChartArt(
        letter="AD",
        draw=ck.annotated,
        kwargs=dict(
            series=AD_SERIES,
            size=PAIR,
            boxes=(Box(x0=9, x1=50, lo=40, hi=44,
                       label="A consolidation range: PHP 40 to PHP 44",
                       where="below"),),
            strokes=(
                Stroke(points=((9, 44), (78, 44)), dashed=True,
                       tone="notice"),
            ),
            notes=(
                Note(x=52, y=44, label="The breakout: price leaves\n"
                     "the range through its top", dx=-12, dy=46,
                     notice=True),
                Note(x=67, label="The trend\nthat follows", dx=-70, dy=30),
            ),
            price_ticks=(40, 44, 48, 52, 56),
            ylabel="Price (PHP)",
            top=0.22, bottom=0.26,
            footnote=INVENTED + " The range is Chapter 4's own example. In "
                     "gold, the top of the range.",
        ),
    ),
    ChartArt(
        letter="AE",
        draw=ck.gallery,
        kwargs=dict(sketches=LEVELS, cols=2, size=PAIR,
                    footnote="Not prices: four shapes. In green, the level "
                             "that price gets through."),
    ),
    ChartArt(
        letter="AF",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AF_PRICE, traces=AF_TRACES, size=PAIR,
            strokes=(
                Stroke(points=((AF_HIGH[0], AF_HIGH[1]),
                               (AF_HIGH[2] + 2, AF_HIGH[1])),
                       tone="notice", width=2.0),
                Stroke(points=((AF_MED[0], AF_MED[1]),
                               (AF_MED[2] + 2, AF_MED[1])),
                       tone="notice", width=2.0),
                Stroke(points=((AF_LOW[0], AF_LOW[1]),
                               (AF_LOW[2] + 2, AF_LOW[1])),
                       tone="notice", width=2.0),
            ),
            notes=(
                Note(x=AF_LOW[2], y=AF_LOW[1],
                     label="LWC breakout:\nprice passes the\nlast small peak",
                     dx=10, dy=-70),
                Note(x=AF_MED[2], y=AF_MED[1],
                     label="MWC breakout:\nprice passes the\n"
                     "last medium peak", dx=-40, dy=28),
                Note(x=AF_HIGH[2], y=AF_HIGH[1],
                     label="HWC breakout: price passes\n"
                     "the top of the whole move", dx=-36, dy=46,
                     notice=True),
            ),
            price_ticks=(50, 60, 70, 80),
            top=0.22, bottom=0.34,
            footnote="Invented: the same three waves, on a slow rise. Gold "
                     "lines: three breakout levels,\neach the high of a prior "
                     "peak on this chart. Our drawing.",
        ),
    ),
    ChartArt(
        letter="AG",
        draw=ck.gallery,
        kwargs=dict(sketches=STOCHASTIC, cols=3, size=TERM,
                    footnote="One bar, three closes. Green: its high, "
                             "PHP 50, and its low, PHP 40."),
    ),
    ChartArt(
        letter="AH",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AH_PRICE, traces=AH_TRACES, size=PAIR,
            strokes=(
                Stroke(points=((33, AH_PRICE[33].low - 1.6),
                               (46, AH_PRICE[46].low - 1.6)),
                       tone="notice", width=2.0, arrow=True),
            ),
            notes=(
                Note(x=40, y=AH_PRICE[40].low - 1.9,
                     label="LWC: higher swing after\nswing here. Trend mode",
                     dx=12, dy=-58, dot=False),
                Note(x=48, y=AH_MWC[48],
                     label="MWC: swings across\none level. Ranging mode",
                     dx=-24, dy=64),
                Note(x=92, y=60.0,
                     label="HWC: flat.\nFlatline mode", dx=-6, dy=100),
            ),
            price_ticks=(50, 55, 60, 65, 70),
            top=0.44, bottom=0.46,
            footnote="Invented: a flat line at PHP 60 plus a 32 bar wave and "
                     "an 8 bar wave.\nBars: LWC. Dotted: MWC. Thick: HWC. One "
                     "market, three readings.",
        ),
    ),
    ChartArt(
        letter="AI",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AI_PRICE, traces=AI_TRACES, size=PAIR,
            notes=(
                Note(x=16, label="The MWC and LWC\nturn down here.\n"
                     "The HWC does not", dx=-16, dy=72),
                Note(x=40, label="Only the LWC\nturns down here", dx=34,
                     dy=-122),
                Note(x=48, label="The HWC turns down,\nand both smaller "
                     "cycles\nturn with it", dx=28, dy=6, notice=True),
            ),
            price_ticks=(40, 50, 60, 70, 80),
            top=0.20, bottom=0.08,
            footnote=INVENTED + " Bars: LWC. Dotted: MWC. Thick: HWC. The "
                     "three are drawn to peak on one bar.",
        ),
    ),
)
