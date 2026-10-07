"""Chapter 5 teaching charts for FIN1209, as plain data.

Forty seven charts, lettered A to Z and then AA to AU, in the order the deck
shows them: deckkit letters a twenty seventh chart the way a spreadsheet
letters its columns. They were first lettered in the order they were drawn,
which put a late addition between the second and third, and left one chart
(the bearish divergence chart, now O) carrying a placeholder letter outside
the sequence entirely; a later pass added three more (two recalls, of O and
of W, that needed their own letters once deckkit's own uniqueness check
caught the reuse; one new chart for the standard fan lines, Figure 5.50,
whose troughs and peaks the book draws too small to read). Every pass that
adds or moves a chart has relettered the whole sequence so a reader meets
every one of them in order, with no exceptions. The names in this
file that still begin `AB_`, `AF_` and so on are the charts' old letters
and nothing more.

This file carries no drawing code: the forms it uses, annotated, gallery,
bar_waves, wave_sum and measured_bars, live in build/chartkit.py, which knows nothing about
any chapter, and every entry below is data handed to one of them.

Chapter 5 has 59 figures and every one is placed in the deck. A chart is
drawn here only where the book makes a point in words that none of its own
figures shows, or beside a book sketch that does not carry the idea alone:

  * **A** Dow's three trends by duration, which 5.1 states as a list.
  * **B** what a wave degree is: one wave drawn alone, then with its
    subwaves, then with theirs. It sits before Figure 5.5.
  * **C** the invented price of the wave charts, set out as a sum: the big,
    the medium and the small wave one under another to one scale, each with
    one swing measured in bars and pesos, and their total as price bars.
  * **D** how the three wave cycles are drawn: that price as bars, the lower
    wave cycle, with the medium wave cycle dotted and the higher one thick
    over it, the line styles of Figure 5.5.
  * **E** the same chart with a counted ruler under it for each cycle, so
    the swings of one can be counted inside the swings of the next.
  * **F** Figure 5.7 on price bars: one market that is flat, ranging and
    trending at once, by wave cycle.
  * **G** a breakout as Chapters 2 and 4 used the word: price leaving a
    consolidation range through its top, on Chapter 4's own PHP 40 to
    PHP 44 example.
  * **H** the four kinds of level this chapter breaks out of: the top of a
    range, a prior peak, a trendline and a channel line.
  * **I** Figure 5.8's three breakouts on price bars: one level at a prior
    peak of each wave cycle, and the bar that closes above it.
  * **J** Figure 5.9 on price bars, with the two places the smaller cycles
    turn and the largest does not, which the figure does not mark.
  * **K** a correction or pullback beside a reversal or retracement.
  * **L** the true range on Chapter 3's own two bars: the new bar's range
    and its true range bracketed, so the gap the bar range misses shows.
  * **M** high and lower quality price: a stretch of small, equal bars
    beside a stretch of uneven ones. Figure 5.17 is too small to show a bar.
  * **N** the bar stochastic measured on one bar with three closes.
  * **O** one of Figure 5.19's bearish divergences, drawn on invented bars:
    price makes a higher second peak while the averaged bar stochastic
    makes a lower one. The figure's own panel is too fine to read.
  * **P** characteristic 11, the size and duration of a consolidation.
  * **Q** characteristic 13, the average period range completed early.
  * **R** characteristic 15, the four cases of volume spread action.
  * **S** a recall of O, drawn again beside characteristic 16: the book
    gives divergence one sentence there and no picture of its own.
  * **T and U** the three categories of filter on one breakout, and
    two-stage filtering. Figure 5.30 lists the filters and draws neither.
  * **V** the four scenarios of buying low and selling high.
  * **W, X and Y** a stop order, slippage, and a limit order, as entries.
  * **Z** the orders to place with no position: a market buy, a buy stop
    and a buy limit, numbered and arrowed to the price that triggers each.
  * **AA** the orders to place holding a long: a market sell, a sell limit
    to take profit and a sell stop to cut the loss, the same way. Figure
    5.32 is the book's own table of every order above and below the
    market, short side included, and is placed right after it.
  * **AB** a recall of W, drawn again beside the book's other named
    orders: an MIT is the same waiting-order shape, just named for its use.
  * **AC** four entries on one barrier: at it, through it, after the
    breakout fails, and at the retest.
  * **AD** an inflection point of strength 2 beside one of strength 10, on
    price bars with the flanking bars counted.
  * **AE** a double moving average crossover as a trend filter.
  * **AF, AG and AH** the book's proportional stopsizing, worked in pesos:
    what a fixed risk does to the tradesize, the tradesize capped, and the
    percentage risk that results.
  * **AI** a trendline drawn, tentative, and confirmed.
  * **AJ** why a trendline holds: the orders on either side of it.
  * **AK** two intraday penetrations that close back above the line, one
    short of a price filter and one beyond it.
  * **AL and AM** the factors of trendline reliability: angle, and retests.
  * **AN** a rising channel whose swings turn at three retracement levels,
    which is what the book says of its Figure 5.46 and cannot be seen on it.
  * **AO** price failing to test a channel boundary before breaking out.
    The book makes this point on its Figure 5.14, which is placed with the
    characteristic it was drawn for.
  * **AP** DeMark's line on four numbered troughs: Figure 5.49 redrawn so
    the troughs each line joins can be told apart.
  * **AQ** Figure 5.50's standard fan lines, redrawn and numbered: the
    book's own troughs and peaks are too small to tell apart on it.
  * **AR** the three ranges where Fibonacci, Dow and Gann converge.
  * **AS** a gap acting as support and a gap acting as resistance. The gaps
    on Figure 5.57 are too small to see.
  * **AT** a three-bar moving average standing in for the PLdot, with the
    book's three readings marked. The line cannot be seen on Figure 5.59.
  * **AU** the signs of a reversal that can be drawn on one top.

**Teach only what the textbook teaches.** Every label on these charts is a
statement the book's Chapter 5 makes, or arithmetic it sets out. Charts AF,
AG and AH are the book's five step procedure with numbers put in: an average
stopsize of PHP 2.00, a two standard deviation value of PHP 1.00, and
PHP 10,000 at risk. The pesos are ours and the steps are the book's.
Chart AE computes two simple moving averages of the line it draws, a short
one and a long one, and marks where they cross; how a moving average is
built is Chapter 11 and no label explains it.
Chart B is the one place the labels are a reading and not a quotation: the
book defines neither wave cycle nor wave degree in a sentence, so the chart
says what its Figure 5.5 and its words larger, smaller and subwave show, and
the slide beside it says that is where the reading comes from. Chart AD
draws a peak that is higher than the N bars on either side of it, which is
our reading of the book's "N bars on either side", and says in its small
print that the book does not say whether N is a maximum.

**The data is invented.** We hold no market data licence. Every price
series comes from chartkit.walk() with a fixed seed, offline and
reproducible, and every chart carries the credit line
deckkit.chart_credit() prints under it. Charts AF, AG and AH are not prices
at all: each is one line of arithmetic, and says so. Chart C is not prices
either: it is three sine waves added one at a time, and says so.
Charts C, D and E are three such waves with a little seeded noise, made
into price bars. The book draws its wave cycles freehand and gives no rule
for where the two smooth lines go, so their place on these charts is our
drawing choice. Every size on them is one we built in, and the slides say so.
Charts F, I and J are built the same way, each with its waves arranged
to show one thing: the largest wave left flat, a slow rise added so the
largest wave passes its own peak, and the three waves set to peak on one
bar. Chart I's levels are the highs of its own bars and its breakouts the
first bar to close above each; nothing on it is the book's but the idea.
Chart G is Chapter 4's worked range again. Charts H and N are not prices
at all: four shapes, and one bar drawn three times.

**An annotation is in the slide's own words.** The final pass put arrows,
numbers, rulers and labelled lines on these charts wherever the slide points
at something, so that every thing the words name can be found on the
picture: the measured swings on C, the counted rulers on E and AD, the
numbered breakouts on I and entries on AC, the two numbered days on AK,
the two bracketed ranges on L, and the numbered orders on Z and AA.
"""

from __future__ import annotations

import chartkit as ck
from chartkit import (Addend, Bar, Box, Bracket, ChartArt, Measure, Note,
                      Ruler, Sketch, Span, Stroke, Trace)

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
# Chart K. A correction or pullback, and a reversal or retracement.
# --------------------------------------------------------------------------

B_SERIES = _line(
    ((0, 40), (12, 49), (15, 47.5), (30, 60), (34, 58.2), (52, 76),
     (57, 73), (61, 75), (84, 50), (89, 53), (98, 46)),
    seed=509)

# --------------------------------------------------------------------------
# Chart O. Size and duration of a consolidation.
# --------------------------------------------------------------------------

C_SERIES = _line(
    ((0, 30), (14, 43), (17, 40.6), (20, 43.2), (23, 40.8), (26, 43.4),
     (46, 62), (52, 54), (59, 64), (66, 54.4), (73, 63.6), (80, 54),
     (87, 64), (93, 55)),
    seed=521)

# --------------------------------------------------------------------------
# Chart P. The average period range, completed before the day ends.
# --------------------------------------------------------------------------

D_SERIES = _line(
    ((0, 14), (7, 0), (20, 46), (25, 38), (40, 88), (45, 80), (58, 124),
     (62, 118), (68, 127), (76, 108), (82, 114), (96, 96)),
    seed=523, noise=0.0, wobble=0.06)

# --------------------------------------------------------------------------
# Chart Q. Volume spread action: the four cases the book lists.
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
    _vsa("Large range, large volume", "trend promoting; close near high: bullish",
         (14.6, 25.0, 14.0, 24.4), 9.0),
    _vsa("Large range, low volume", "trend inhibiting: lack of commitment",
         (14.6, 25.0, 14.0, 24.4), 1.0),
    _vsa("Small range, large volume", "squat bar: much capital, no extension in price",
         (14.6, 15.6, 14.2, 15.0), 9.0),
    _vsa("Small range, low volume", "trend inhibiting",
         (14.6, 15.6, 14.2, 15.0), 1.0),
)

# --------------------------------------------------------------------------
# Charts R and S. One breakout filtered three ways, and two-stage filtering.
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
# Chart T. Buying low and selling high, four ways.
# --------------------------------------------------------------------------

H_SERIES = _line(
    ((0, 40), (20, 60), (23, 58.5), (44, 80), (48, 78), (66, 60),
     (69, 61.5), (88, 40)),
    seed=547, noise=0.002, wobble=0.02)

# --------------------------------------------------------------------------
# Charts U, V, W and X. Stop orders, slippage, limit orders and exits.
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
# Chart Y. Three ways of initiating an entry, on one barrier.
# --------------------------------------------------------------------------

M_SERIES = _line(
    ((0, 47), (18, 59.6), (30, 52.5), (44, 59.4), (50, 63.6), (58, 59.5),
     (70, 53), (82, 59.5), (92, 54)),
    seed=577, noise=0.002, wobble=0.03)

# --------------------------------------------------------------------------
# Chart Z. An inflection point of strength 2, and one of strength 10.
#
# One point is one bar. The small peak has two lower bars on either side
# and the third bar out is higher; the large one has ten.
# --------------------------------------------------------------------------

def _strength_bars():
    """Thirty three bars: a small peak on bar 6 with two lower bars on
    either side, and a large peak on bar 22 with ten on either side."""
    import random
    rng = random.Random(593)
    highs = ([56.0, 54.5, 53.0, 51.6]            # falling into the picture
             + [48.0, 49.5, 51.0, 49.6, 48.4]    # the small peak, on bar 6
             + [52.0, 54.0, 56.0]
             + [57.5 + 2.0 * i for i in range(10)]   # ten lower bars
             + [80.0]                                # the large peak, bar 22
             + [77.0 - 2.1 * i for i in range(10)])  # ten lower bars
    bars = []
    for x, h in enumerate(highs):
        low = h - rng.uniform(2.2, 3.0)
        up = x == 0 or highs[x] >= highs[x - 1]
        o, c = (low + 0.6, h - 0.6) if up else (h - 0.6, low + 0.6)
        bars.append(Bar(open=o, high=h, low=low, close=c))
    return tuple(bars)


N_BARS = _strength_bars()

# --------------------------------------------------------------------------
# Chart AA. A double moving average crossover as a trend filter.
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
# Charts AB, AC and AD. Proportional stopsizing, worked in pesos.
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
# Charts AE to AK. Trendlines and channels.
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
# The middle one is drawn so that its line stands at about 40 degrees on the
# slide itself: 0.524 pesos a point, at this chart's size and scales.
V_MID = _straight(((0, 40), (7, 49.8), (10, 44.6), (17, 55.1), (20, 49.8),
                   (27, 60.3), (30, 55.1), (34, 62.3)))
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
# Chart AM. Where the three approaches to retracement converge.
# --------------------------------------------------------------------------

Y_SERIES = _line(
    ((0, 42), (8, 40), (24, 51), (28, 49), (48, 60), (58, 54.5), (61, 56),
     (72, 50.3), (80, 53.5), (84, 52)),
    seed=617, noise=0.0015, wobble=0.03)

# --------------------------------------------------------------------------
# Chart AP. The signs of a reversal that can be drawn on one top.
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
# Chart B. One wave, drawn at one, two and three wave degrees.
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
# Charts C, D and E. One invented price: how it is built, how its three
# wave cycles are drawn, and how they are told apart.
# --------------------------------------------------------------------------
# The price is three waves added together bar by bar, like Chart B's third
# drawing, with a little seeded noise, and turned into open, high, low and
# close. One swing of the big wave, up and back down, takes 96 bars and is
# PHP 24 from bottom to top; the medium wave takes 32 bars and PHP 12; the
# small one 8 bars and PHP 6. So three medium swings fit in the big one and
# four small swings in a medium one. The sizes were picked for the picture
# and the slides say so: the instructor asked where the numbers came from.
#
# All three waves start at a low, so a swing on every one of them runs from
# one low to the next and the lows line up: every fourth small low is a
# medium low, and every third medium low a big one. That is what lets Chart
# C rule one upright line through all three and Chart E number the swings.
#
# C sets the sum out the way a sum is set out in arithmetic: the three
# waves one under another to one scale, each with the length and height of
# one swing measured on it, and the total under a rule, drawn as bars.
# D is that total with two lines over it: the thick one is the big wave
# alone and the dotted one the big wave plus the medium, which is why each
# runs through the middle of the smaller swings. The book gives no rule for
# drawing either line, so where they sit is our drawing choice and the
# slides say so. E is D with a counted ruler under it for each cycle.

AB_BARS = 97
AB_HIGH = (12.0, 96)    # half the swing in pesos, and bars in one swing
AB_MEDIUM = (6.0, 32)
AB_LOW = (3.0, 8)
AB_MIDDLE = 60.0        # the price the big wave swings around


def _big(x):
    import math
    return -AB_HIGH[0] * math.cos(2 * math.pi * x / AB_HIGH[1])


def _medium(x):
    import math
    return -AB_MEDIUM[0] * math.cos(2 * math.pi * x / AB_MEDIUM[1])


def _small(x):
    import math
    return -AB_LOW[0] * math.cos(2 * math.pi * x / AB_LOW[1])


def _degree_waves():
    import random
    rng = random.Random(977)
    higher, medium, closes = [], [], []
    for x in range(AB_BARS):
        h = AB_MIDDLE + _big(x)
        m = h + _medium(x)
        higher.append(h)
        medium.append(m)
        closes.append(m + _small(x) + rng.uniform(-0.3, 0.3))
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

SUM_ROWS = (
    Addend(name="1  Big wave", values=tuple(_big(x) for x in range(AB_BARS)),
           swing=AB_HIGH[1], long="one swing: 96 bars", tall="PHP 24"),
    Addend(sign="+", name="2  Medium wave",
           values=tuple(_medium(x) for x in range(AB_BARS)),
           swing=AB_MEDIUM[1], long="one swing: 32 bars", tall="PHP 12"),
    Addend(sign="+", name="3  Small wave",
           values=tuple(_small(x) for x in range(AB_BARS)),
           swing=AB_LOW[1], long="one swing: 8 bars", tall="PHP 6"),
    Addend(sign="=", name="4  The price", note="drawn as bars",
           bars=AB_PRICE, total=True),
)


# --------------------------------------------------------------------------
# Charts G and H. Breakout as Chapters 2 and 4 used it, and what Chapter 5
# adds.
# --------------------------------------------------------------------------
# G is Chapter 4's own example again: a share ranging between PHP 40 and
# PHP 44 that leaves the range through its top. H is four small shapes, each
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
# Chart I. The three breakouts of Figure 5.8, on price bars.
# --------------------------------------------------------------------------
# Three waves of the same lengths as Chart D's on a slow rise, so that the
# largest wave peaks, falls back and then passes its own peak, which is what
# Figure 5.8 draws. The three are set to peak together on bar 28, so the top
# of the whole move is a top of all three, as the book's wave-degree
# convergence has it. Each level is the high of a prior peak, read off the
# bars, and each breakout is the first bar that closes above it.

AF_BARS = 125
AF_TOP = 28


def _breakout_waves():
    import math
    import random
    rng = random.Random(431)
    higher, medium, closes = [], [], []
    for x in range(AF_BARS):
        h = 55.0 + 0.10 * x + 10.0 * math.cos(2 * math.pi * (x - AF_TOP) / 96)
        m = h + 5.0 * math.cos(2 * math.pi * (x - AF_TOP) / 32)
        low = 2.5 * math.cos(2 * math.pi * (x - AF_TOP) / 8)
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
AF_HIGH = _level(AF_PRICE, 20, 40)      # the top of the whole move
# A medium and a small peak on the way down, far enough back that each
# level line has length before price comes back through it.
AF_MED = _level(AF_PRICE, 58, 63)       # a peak of the medium wave
AF_LOW = _level(AF_PRICE, 66, 70)       # a small peak after it

# --------------------------------------------------------------------------
# Chart N. The bar stochastic, measured on three bars.
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
# Charts F and J. Figure 5.7 and Figure 5.9, on price bars.
# --------------------------------------------------------------------------
# F is a market whose largest wave is flat: the medium wave swings across
# one level and the small one climbs and falls along it, so the one chart is
# flat, ranging and trending at once. J is Chart D's price with the three
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
# The true range on Chapter 3's own two bars, and price of two qualities.
# --------------------------------------------------------------------------
# Both were added in the final pass. The first is the recall the instructor
# asked for when Check 5 asked about the ATR: Chapter 3's last bar and new
# bar, with the new bar's own range and its true range bracketed, so the
# gap the bar range misses can be seen. The second puts the book's two tests
# for high quality price on bars, because its Figure 5.17 is too small to
# show a bar: thirty bars of one small range, then thirty of uneven ranges.

TR_LAST = Bar(open=101.0, high=104.0, low=100.0, close=102.0)
TR_NEW = Bar(open=106.0, high=108.0, low=105.5, close=107.0)


def _quality_bars():
    import random
    rng = random.Random(641)
    bars = []
    # High quality: every range about 1.2, a steady climb and one clean turn.
    c = 50.0
    for x in range(30):
        step = 0.55 if x < 19 else -0.60
        o, c = c, c + step + rng.uniform(-0.05, 0.05)
        bars.append(Bar(open=o, close=c, high=max(o, c) + 0.30,
                        low=min(o, c) - 0.30))
    # Lower quality: ranges from under one to over three, and no direction.
    rough = []
    for x in range(30):
        size = rng.choice((0.3, 0.5, 0.8, 1.6, 2.6, 3.4))
        step = rng.choice((-1, 1)) * rng.uniform(0.2, 1.0) * min(size, 1.8)
        o, c = c, min(56.5, max(49.5, c + step))
        rough.append(Bar(open=o, close=c, high=max(o, c) + size * 0.5,
                         low=min(o, c) - size * 0.5))
    return tuple(bars), tuple(rough)


Q_CLEAN, Q_ROUGH = _quality_bars()
Q_BARS = Q_CLEAN + Q_ROUGH

# --------------------------------------------------------------------------
# Four book figures redrawn, because what they show cannot be seen on them.
# --------------------------------------------------------------------------
# Added after the third round of fresh readers. Each sits on a slide of its
# own after the book's figure: DeMark's line with the troughs numbered, a
# channel turning at three retracement levels, a gap acting as support and
# one as resistance, and a short moving average standing in for the PLdot.

DM_TROUGHS = ((14, 43.0), (30, 50.0), (46, 59.0), (62, 70.0))
DM_SERIES = _line(
    ((0, 40), (8, 48.5), DM_TROUGHS[0], (24, 56.5), DM_TROUGHS[1], (40, 65),
     DM_TROUGHS[2], (56, 75), DM_TROUGHS[3], (72, 84)),
    seed=653, noise=0.0015, wobble=0.03)


def _through(a, b, x):
    """The price at ``x`` on the straight line through points a and b."""
    return a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0])


# A fall of PHP 20, then a rising channel whose three peaks stand on the
# 38.2, 50 and 61.8 percent retracement levels of that fall.
RC_LEVELS = (47.64, 50.00, 52.36)
RC_SERIES = _line(
    ((0, 60), (20, 40), (32, RC_LEVELS[0]), (38, 42.4), (50, RC_LEVELS[1]),
     (56, 44.8), (68, RC_LEVELS[2]), (74, 47.2), (80, 51.5)),
    seed=659, noise=0.0, wobble=0.02)

# Two stretches on one pair of axes: a gap up that later holds price from
# above, and a gap down that later stops it from below.
GAP_UP = _line(((0, 40), (12, 46), (13, 49), (26, 56), (38, 49.3), (50, 57)),
               seed=661, noise=0.0015, wobble=0.03)
GAP_DOWN = _line(((0, 58), (10, 53), (11, 50), (22, 45), (32, 49.7),
                  (44, 43)), seed=673, noise=0.0015, wobble=0.03)
GAP_IDLE = 8
GAP_X = len(GAP_UP) + GAP_IDLE
GAP_SERIES = GAP_UP + [50.0] * GAP_IDLE + GAP_DOWN
GAP_BREAKS = ((13,) + tuple(range(len(GAP_UP), GAP_X + 1)) + (GAP_X + 11,))


def _pldot_bars():
    import random
    rng = random.Random(677)
    closes, c = [], 50.0
    for x in range(38):
        c += (1.0 if x < 21 else -1.0) + rng.uniform(-0.25, 0.25)
        closes.append(c)
    bars = []
    for x, c in enumerate(closes):
        o = closes[x - 1] if x else c - 1.0
        bars.append(Bar(open=o, close=c, high=max(o, c) + 0.45,
                        low=min(o, c) - 0.45))
    # The average of the three closes before each bar: a three-bar average
    # shifted forward one bar, which the book allows and which keeps the
    # line clear of the bars it is read against.
    average = []
    for x in range(len(closes)):
        window = closes[max(0, x - 3):x] or [closes[0] - 1.0]
        average.append(sum(window) / len(window))
    return tuple(bars), tuple(average)


PL_BARS, PL_LINE = _pldot_bars()
PL_TURN = max(range(len(PL_LINE)), key=lambda x: PL_LINE[x])

# --------------------------------------------------------------------------
# One bearish divergence, between price and the averaged bar stochastic.
# --------------------------------------------------------------------------
# Added after the fourth round of readers: the lower panel of Figure 5.19
# cannot be read at slide size, so its six divergence labels have nothing to
# be checked against. Forty invented bars, each PHP 2 from low to high. The
# close sits high in the bar through the first rally and lower through the
# second, so price makes a higher peak while the three-bar average of the
# bar stochastic makes a lower one. The panel is computed from the bars.

def _divergence():
    legs = ((10, 0.62, 0.84), (6, -0.45, 0.30), (12, 0.66, 0.56),
            (12, -0.60, 0.22))
    lows, ratios = [], []
    low = 50.0
    for count, step, ratio in legs:
        for _ in range(count):
            low += step
            lows.append(low)
            ratios.append(ratio)
    # The ratio eases off towards the end of each rally, as a rally tires.
    for i in range(7, 10):
        ratios[i] = 0.80
    for i in range(24, 28):
        ratios[i] = 0.50
    closes = [l + 2.0 * r for l, r in zip(lows, ratios)]
    average = []
    for i in range(len(ratios)):
        window = ratios[max(0, i - 2):i + 1]
        average.append(sum(window) / len(window))
    return closes, average


DV_CLOSES, DV_AVERAGE = _divergence()
DV_P1, DV_P2 = 9, 27          # the two price peaks

# --------------------------------------------------------------------------
# The forty three charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.annotated,
        kwargs=dict(
            series=A_SERIES,
            size=PAIR,
            spans=(Span(x0=54, x1=76,
                        label="Secondary reaction:\nweeks to months"),),
            strokes=(
                Stroke(points=((6, 33), (124, 84)), arrow=True,
                       label="Primary trend: months to years", at=0,
                       dx=74, dy=6),
            ),
            boxes=(Box(x0=38.5, x1=45.5, lo=62.0, hi=69.0, tone="notice"),),
            notes=(
                Note(x=40, y=69.0, label="A minor trend:\none small swing,\n"
                     "days to weeks", dx=-14, dy=40, dot=False),
            ),
            top=0.10, bottom=0.20,
            footnote=INVENTED + " Arrow: the primary trend. Grey band: the "
                     "one secondary reaction.\nGold box: one minor trend. "
                     "Every small swing on the line is another.",
        ),
    ),
    ChartArt(
        letter="K",
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
        letter="P",
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
            strokes=(
                Stroke(points=((93, 55), (101, 45)), dashed=True, arrow=True,
                       tone="notice"),
            ),
            notes=(
                Note(x=24, y=39.8, label="Shorter and narrower:\na lesser "
                     "interruption.\nThe trend carries on", dx=26, dy=-34,
                     dot=False),
                Note(x=97, y=50, label="After the larger one,\na reversal "
                     "is more\nprobable", dx=-30, dy=-34, dot=False,
                     notice=True),
            ),
            extend=8,
            top=0.26, bottom=0.30,
            footnote=INVENTED + " The same kind of sideways movement, at two "
                     "sizes. Dashed: what the larger\none makes more "
                     "probable, not what must happen.",
        ),
    ),
    ChartArt(
        letter="Q",
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
                Stroke(points=((0, 150), (98, 150)), dashed=True,
                       tone="quiet",
                       label="The 2 standard deviation value: 90% of days "
                             "stay below", at=0, dx=4, dy=11),
            ),
            notes=(
                Note(x=58, label="Beyond the average\nrange before the day\n"
                     "completes: potential\nexhaustion", dx=-70, dy=-33,
                     notice=True),
                Note(x=96, label="The day\nends", dx=-10, dy=-46, dot=False),
            ),
            top=0.20, bottom=0.08,
            footnote="An invented currency pair. Its average daily range is "
                     "the book's example, 120 pips.\nThe book puts no number "
                     "on the higher mark.",
        ),
    ),
    ChartArt(
        letter="R",
        draw=ck.gallery,
        kwargs=dict(sketches=VSA, cols=2, size=PAIR,
                    footnote="Each drawing: three bars over their volume, "
                             "the green boxes. The third bar is the extreme "
                             "one.\nHad the first drawing's big bar closed "
                             "near its low, it would be very bearish."),
    ),
    ChartArt(
        letter="T",
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
        letter="U",
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
        letter="V",
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
        letter="W",
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
                Note(x=36, label="Now: PHP 50", dx=-30, dy=-21),
            ),
            top=0.42, bottom=0.42,
            footnote=INVENTED + " Stop entries are placed when a "
                     "continuation is expected.",
        ),
    ),
    ChartArt(
        letter="AB",
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
                Note(x=36, label="Now: PHP 50", dx=-30, dy=-21),
            ),
            top=0.42, bottom=0.42,
            footnote=INVENTED + " The same shape Chart W drew: the chart "
                     "a few slides back, which this one recalls.",
        ),
    ),
    ChartArt(
        letter="X",
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
        letter="Y",
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
                Note(x=36, label="Now: PHP 50", dx=-46, dy=-30),
            ),
            top=0.50, bottom=0.50,
            footnote=INVENTED + " Limit entries are placed when a reversal "
                     "is expected.",
        ),
    ),
    ChartArt(
        letter="Z",
        draw=ck.annotated,
        kwargs=dict(
            series=L_SERIES,
            size=PAIR,
            extend=62,
            strokes=(
                Stroke(points=((34, 50), (70, 50)), arrow=True, tone="quiet",
                       label="1  Market: buy now,\nwhatever is quoted",
                       at=1, dx=-70, dy=-24),
                Stroke(points=((34, 55), (92, 55)), dashed=True,
                       tone="quiet",
                       label="Buy stop at 55", at=0, dx=4, dy=10),
                Stroke(points=((38, 50.4), (46, 53), (52, 54.4), (58, 55)),
                       arrow=True, tone="quiet",
                       label="2  Buy stop: a\ncontinuation is expected.\n"
                             "Triggers at 55, then\nfills at the market.",
                       at=3, dx=8, dy=30),
                Stroke(points=((34, 45), (92, 45)), dashed=True,
                       label="Buy limit at 45", at=0, dx=4, dy=-10),
                Stroke(points=((38, 49.6), (46, 47), (52, 45.6), (58, 45)),
                       arrow=True,
                       label="3  Buy limit: a reversal\nis expected. Fills "
                             "only\nat 45 or better.",
                       at=3, dx=16, dy=-36),
            ),
            notes=(
                Note(x=30, label="The current\nmarket price", dx=-58,
                     dy=-56),
            ),
            top=0.55, bottom=0.50,
            footnote=INVENTED + " You do not own the position. Green: a "
                     "limit order. Grey: a stop or a market order.\nTo "
                     "open a short instead, mirror these with a sell "
                     "limit or a sell stop.",
        ),
    ),
    ChartArt(
        letter="AA",
        draw=ck.annotated,
        kwargs=dict(
            series=L_SERIES,
            size=PAIR,
            extend=62,
            strokes=(
                Stroke(points=((34, 50), (70, 50)), arrow=True, tone="quiet",
                       label="1  Market: sell now,\nwhatever is quoted",
                       at=1, dx=-70, dy=-24),
                Stroke(points=((34, 55), (92, 55)), dashed=True,
                       label="Sell limit at 55", at=0, dx=4, dy=10),
                Stroke(points=((38, 50.4), (46, 53), (52, 54.4), (58, 55)),
                       arrow=True,
                       label="2  Sell limit, take profit:\nfills only at "
                             "55 or better.\nNot guaranteed.",
                       at=3, dx=16, dy=30),
                Stroke(points=((34, 45), (92, 45)), dashed=True,
                       tone="quiet",
                       label="Sell stop at 45", at=0, dx=4, dy=-10),
                Stroke(points=((38, 49.6), (46, 47), (52, 45.6), (58, 45)),
                       arrow=True, tone="quiet",
                       label="3  Sell stop: cut\nthe loss. Triggers at 45,\n"
                             "then fills at the\nmarket. Price unknown.",
                       at=3, dx=8, dy=-42),
            ),
            notes=(
                Note(x=30, label="The current\nmarket price", dx=-58,
                     dy=-56),
            ),
            top=0.55, bottom=0.50,
            footnote=INVENTED + " You own the position. Green: a limit "
                     "order. Grey: a stop or a market order.\nThe mirror "
                     "for a short, and the book's own table of every "
                     "order, is Figure 5.32, next.",
        ),
    ),
    ChartArt(
        letter="AC",
        draw=ck.annotated,
        kwargs=dict(
            series=M_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, 60), (94, 60)), dashed=True, tone="quiet",
                       label="A barrier: resistance", at=1, dx=-4, dy=11),
            ),
            notes=(
                Note(x=18, label="1  Barrier entry: short\nat the "
                     "resistance", dx=4, dy=66),
                Note(x=47, label="2  Breakout entry: buy\nas price breaks "
                     "above", dx=30, dy=30),
                Note(x=60, label="3  Failed breakout entry:\nshort as "
                     "price falls back", dx=-58, dy=-74, notice=True),
                Note(x=82, label="4  Barrier entry at\na retest: short",
                     dx=-2, dy=-70),
            ),
            top=0.46, bottom=0.50,
            footnote=INVENTED + " Numbered in the order they happen here. "
                     "The breakout fails, which sets up entry 3.\nRandom and "
                     "pattern-based entries have nothing to mark on a line.",
        ),
    ),
    ChartArt(
        letter="AD",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=N_BARS, size=TERM,
            strokes=(
                Stroke(points=((22, 80.0), (33, 80.0)), dashed=True,
                       tone="notice"),
                Stroke(points=((6, 51.0), (10, 51.0)), dashed=True,
                       tone="quiet"),
            ),
            rulers=(
                Ruler(y=39.0, x0=3.5, x1=5.5, parts=2, repeat=2),
                Ruler(y=39.0, x0=6.5, x1=8.5, parts=2, repeat=2),
                Ruler(y=39.0, x0=11.5, x1=21.5, parts=10, numbered=False,
                      label="the 10 bars before"),
                Ruler(y=39.0, x0=22.5, x1=32.5, parts=10, numbered=False,
                      label="the 10 bars after"),
            ),
            notes=(
                Note(x=6, y=51.0, label="Strength 2: higher than\nthe two "
                     "bars each side", dx=2, dy=64),
                Note(x=22, y=80.0, label="Strength 10: higher than the\n"
                     "ten bars each side. Its level,\ndashed, is the "
                     "stronger resistance", dx=-8, dy=34, notice=True),
            ),
            xlabel="Time, one bar at a time", ylabel="Price",
            top=0.42, bottom=0.10,
            footnote="Invented bars. The small peak tops two bars each "
                     "side; the third bar out is higher.\nThe large one tops "
                     "ten each side. The book does not say if N is a "
                     "maximum.",
        ),
    ),
    ChartArt(
        letter="AE",
        draw=ck.annotated,
        kwargs=dict(
            series=O_SERIES,
            size=TERM,
            strokes=(
                Stroke(points=O_SHORT, tone="structure",
                       label="Shorter average", at=len(O_SHORT) - 1, dx=-6,
                       dy=-19, width=1.8),
                Stroke(points=O_LONG, tone="quiet", label="Longer average",
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
        letter="AF",
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
                     "the stopsize.\nWhatever the stopsize, a stop that is hit "
                     "loses the same PHP 10,000.",
        ),
    ),
    ChartArt(
        letter="AG",
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
                     "this chart.\nPast PHP 3.00 nothing changes: PHP 10,000 "
                     "divided by the stopsize, as before.",
        ),
    ),
    ChartArt(
        letter="AH",
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
        letter="AI",
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
                     "into the future.\nAs drawn, the line touches its two "
                     "troughs and cuts through no price.",
        ),
    ),
    ChartArt(
        letter="AJ",
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
                Note(x=50, y=_on(50), label="Price breaks\nthrough the line",
                     dx=10, dy=-58),
            ),
            top=0.30, bottom=0.26,
            footnote=INVENTED + " One line, met first from above and, after "
                     "price breaks through it,\nfrom below: the role "
                     "reversal of section 5.5.",
        ),
    ),
    ChartArt(
        letter="AK",
        draw=ck.annotated,
        kwargs=dict(
            series=U_SERIES,
            size=PAIR,
            strokes=(
                Stroke(points=((0, _on(0)), (70, _on(70)))),
                Stroke(points=((0, _on(0) - 5), (70, _on(70) - 5)),
                       dashed=True, tone="notice",
                       label="The price-based filter line",
                       at=0, dx=6, dy=-13),
                Stroke(points=((40, _on(40) + 1.0), (40, _on(40) - 2.2)),
                       tone="quiet", width=2.6),
                Stroke(points=((60, _on(60) + 0.8), (60, _on(60) - 6.6)),
                       tone="quiet", width=2.6),
            ),
            notes=(
                Note(x=40, y=_on(40) - 2.2, label="1  Low through the line,\n"
                     "short of the filter:\ninvalid by both rules", dx=-40,
                     dy=74, dot=False),
                Note(x=60, y=_on(60) - 6.6, label="2  Low beyond the filter:\n"
                     "valid by the price filter,\ninvalid by the close",
                     dx=-2, dy=-76, dot=False, notice=True),
            ),
            top=0.22, bottom=0.52,
            footnote=INVENTED + " Black: closing prices. Green: the uptrend "
                     "line. Dashed: a price-based\nfilter, a set distance "
                     "below it. Grey bars: the intraday lows\nof two days. Both days close back "
                     "above the uptrend line.",
        ),
    ),
    ChartArt(
        letter="AL",
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
                Stroke(points=((V_X1, 39.5), (V_X1 + 34, 57.3)),
                       label="About 35 to 45\ndegrees: the\nmost reliable",
                       at=1, dx=-4, dy=62),
                Stroke(points=((V_X2, 40), (V_X2 + 34, 45.1)),
                       label="Very shallow:\nweak, less stable", at=1,
                       dx=-6, dy=38, tone="quiet"),
            ),
            top=0.12, bottom=0.06,
            footnote="Three invented uptrends on one pair of axes; the "
                     "middle line stands at about 40 degrees here.\nAn angle "
                     "depends on the scaling used, and the book does not say "
                     "which scaling it means.",
        ),
    ),
    ChartArt(
        letter="AM",
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
                Note(x=48, label="1 and 2 draw the line.\n3 and 4 retest "
                     "it, each one\nprecise: price touches the\nline and is "
                     "rejected", dx=-84, dy=84, notice=True),
            ),
            top=0.34, bottom=0.20,
            footnote=INVENTED + " The green line is the trendline. More and "
                     "cleaner retests: more orders at it.\nNo other indicator "
                     "is drawn, so confluence is not shown here.",
        ),
    ),
    ChartArt(
        letter="AO",
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
            footnote=INVENTED + " Price fails to reach the bottom first, "
                     "and the breakout is on the other side.",
        ),
    ),
    ChartArt(
        letter="AR",
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
        letter="AU",
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
        letter="B",
        draw=ck.gallery,
        kwargs=dict(sketches=WAVES, cols=3, size=PAIR,
                    footnote="Not prices: one wave, drawn three times. In "
                             "green, the wave of the drawing before."),
    ),
    ChartArt(
        letter="C",
        draw=ck.wave_sum,
        kwargs=dict(
            rows=SUM_ROWS, size=PAIR, guides=(0, 32, 64, 96), label_w=1.52,
            footnote="Invented, not a market. All four rows are drawn to one "
                     "scale. Gold arrows: one swing of each wave.\nRow 4: "
                     "rows 1 to 3 added bar by bar around PHP 60, plus a "
                     "small random wobble.",
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AB_PRICE, traces=AB_TRACES, size=PAIR,
            notes=(
                Note(x=28, y=AB_PRICE[28].high, label="The bars are\nthe "
                     "price. Their\nsmall zigzags\nare the LWC", dx=-22,
                     dy=40, dot=False),
                Note(x=64, y=AB_MWC[64], label="MWC: the dotted line\n"
                     "= big + medium wave", dx=-12, dy=-52),
                Note(x=60, y=AB_HWC[60], label="HWC: the thick\n"
                     "line = the big\nwave alone", dx=26, dy=44),
            ),
            ylabel="Price (PHP)",
            price_ticks=(40, 50, 60, 70, 80),
            top=0.12, bottom=0.08,
            footnote="Invented: three waves added together. Dotted: big plus "
                     "medium. Thick: big alone.\nThe bars and the place of "
                     "both lines are our drawing; the book gives no rule.",
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AB_PRICE, traces=AB_TRACES, size=PAIR,
            guides=(0, 32, 64, 96),
            rulers=(
                Ruler(y=29.0, x0=0, x1=96, parts=12, repeat=4,
                      label="LWC: 12 swings, 8 bars each"),
                Ruler(y=17.0, x0=0, x1=96, parts=3,
                      label="MWC: 3 swings, 32 bars each"),
                Ruler(y=5.0, x0=0, x1=96, parts=1,
                      label="HWC: 1 swing of 96 bars"),
            ),
            ylabel="Price (PHP)",
            price_ticks=(40, 50, 60, 70, 80),
            top=0.04, bottom=0.10,
            footnote=INVENTED + " Bars: LWC. Dotted: MWC. Thick: HWC.\n"
                     "Each ruler counts the swings of one cycle, from one "
                     "low to the next.",
        ),
    ),
    ChartArt(
        letter="G",
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
        letter="H",
        draw=ck.gallery,
        kwargs=dict(sketches=LEVELS, cols=2, size=PAIR,
                    footnote="Not prices: four shapes. In green, the level "
                             "that price gets through. A level may slope.\n"
                             "All four are drawn upward; the same holds "
                             "downward, through a trough or a lower line."),
    ),
    ChartArt(
        letter="I",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AF_PRICE, traces=AF_TRACES, size=PAIR,
            strokes=(
                Stroke(points=((AF_HIGH[0], AF_HIGH[1]),
                               (AF_HIGH[2], AF_HIGH[1])),
                       tone="notice", width=2.4, dashed=True),
                Stroke(points=((AF_MED[0], AF_MED[1]),
                               (AF_MED[2], AF_MED[1])),
                       tone="notice", width=2.4, dashed=True),
                Stroke(points=((AF_LOW[0], AF_LOW[1]),
                               (AF_LOW[2], AF_LOW[1])),
                       tone="notice", width=2.4, dashed=True),
            ),
            notes=(
                Note(x=AF_HIGH[0], y=AF_HIGH[1],
                     label="HWC peak: the top\nof the whole move",
                     dx=14, dy=34),
                Note(x=AF_MED[0], y=AF_MED[1],
                     label="MWC peak: a peak\nof the dotted line",
                     dx=-56, dy=-74),
                Note(x=AF_LOW[0], y=AF_LOW[1],
                     label="LWC peak:\na small one", dx=4, dy=-80),
                Note(x=AF_LOW[2], y=AF_LOW[1],
                     label="1  LWC\nbreakout", dx=30, dy=-30, notice=True),
                Note(x=AF_MED[2], y=AF_MED[1],
                     label="2  MWC\nbreakout", dx=34, dy=-22, notice=True),
                Note(x=AF_HIGH[2], y=AF_HIGH[1],
                     label="3  HWC\nbreakout", dx=-26, dy=36, notice=True),
            ),
            price_ticks=(50, 60, 70, 80),
            ylabel="Price (PHP)",
            top=0.26, bottom=0.52,
            footnote="Invented: three waves on a slow rise, set to peak "
                     "together at the first top. Dashed gold: three\n"
                     "breakout levels, each from a prior peak (green dot) "
                     "to the first bar that closes above it (gold dot).",
        ),
    ),
    ChartArt(
        letter="N",
        draw=ck.gallery,
        kwargs=dict(sketches=STOCHASTIC, cols=3, size=TERM,
                    footnote="One bar, three closes. Green: its high, "
                             "PHP 50, and its low, PHP 40."),
    ),
    ChartArt(
        letter="F",
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
            ylabel="Price (PHP)",
            price_ticks=(50, 55, 60, 65, 70),
            top=0.44, bottom=0.46,
            footnote="Invented: a flat line at PHP 60 plus a 32 bar wave and "
                     "an 8 bar wave.\nBars: LWC. Dotted: MWC. Thick: HWC. One "
                     "market, three readings.",
        ),
    ),
    ChartArt(
        letter="J",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=AI_PRICE, traces=AI_TRACES, size=PAIR,
            notes=(
                Note(x=16, label="The MWC and LWC\nturn down here.\n"
                     "The HWC does not", dx=6, dy=78),
                Note(x=40, label="Only the LWC\nturns down here", dx=34,
                     dy=-122),
                Note(x=48, label="The HWC turns down,\nand both smaller "
                     "cycles\nturn with it", dx=28, dy=6, notice=True),
            ),
            ylabel="Price (PHP)",
            price_ticks=(40, 50, 60, 70, 80),
            top=0.20, bottom=0.08,
            footnote=INVENTED + " Bars: LWC. Dotted: MWC. Thick: HWC. The "
                     "three are drawn to peak on one bar.",
        ),
    ),
    ChartArt(
        letter="L",
        draw=ck.measured_bars,
        kwargs=dict(
            first=TR_LAST, second=TR_NEW, size=PAIR,
            measures=(
                Measure(lo=105.5, hi=108.0,
                        label="Bar range\nhigh less low\n2.50"),
                Measure(lo=102.0, hi=108.0,
                        label="True range\nlast close\nto high\n6.00",
                        notice=True),
            ),
            price_ticks=(100, 102, 104, 106, 108),
            labels=("Last bar", "New bar"),
            footnote="Chapter 3's own two bars, in pesos. The new bar gaps "
                     "up from the last close of 102.\nIts own range misses "
                     "the gap; its true range counts it. The ATR averages "
                     "true ranges.",
        ),
    ),
    ChartArt(
        letter="M",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=Q_BARS, size=PAIR,
            notes=(
                Note(x=8, y=Q_CLEAN[8].low, label="High quality:\nsmall, "
                     "equal bars", dx=16, dy=-34),
                Note(x=19, y=Q_CLEAN[19].high, label="A clear,\ndecisive "
                     "reversal", dx=-14, dy=34),
                Note(x=36, y=Q_BARS[36].high, label="Lower quality: uneven "
                     "bars,\nchoppy and hard to track", dx=4, dy=58,
                     dot=False),
            ),
            guides=(29.5,),
            xlabel="Time", ylabel="Price (PHP)",
            price_ticks=(50, 55, 60),
            top=0.42, bottom=0.14,
            footnote="Invented bars, in two stretches. Left of the dashed line: "
                     "every bar has about the\nsame small range. Right of it: "
                     "ranges run from very small to several pesos.",
        ),
    ),
    ChartArt(
        letter="AP",
        draw=ck.annotated,
        kwargs=dict(
            series=DM_SERIES,
            size=PAIR,
            extend=36,
            strokes=(
                Stroke(points=(DM_TROUGHS[2],
                               (80, _through(DM_TROUGHS[2], DM_TROUGHS[3], 80))),
                       label="Correct: 3 and 4", at=1, dx=6, dy=8),
                Stroke(points=(DM_TROUGHS[1],
                               (80, _through(DM_TROUGHS[1], DM_TROUGHS[2], 80))),
                       tone="quiet", dashed=True,
                       label="Wrong: 2 and 3", at=1, dx=6, dy=-4),
                Stroke(points=(DM_TROUGHS[0],
                               (80, _through(DM_TROUGHS[0], DM_TROUGHS[1], 80))),
                       tone="quiet", dashed=True,
                       label="Wrong: 1 and 2", at=1, dx=6, dy=-8),
            ),
            notes=(
                Note(x=DM_TROUGHS[0][0], y=DM_TROUGHS[0][1], label="1", dx=5, dy=-20),
                Note(x=DM_TROUGHS[1][0], y=DM_TROUGHS[1][1], label="2", dx=5, dy=-20),
                Note(x=DM_TROUGHS[2][0], y=DM_TROUGHS[2][1], label="3", dx=5, dy=-20),
                Note(x=DM_TROUGHS[3][0], y=DM_TROUGHS[3][1], label="4", dx=5, dy=-20,
                     notice=True),
            ),
            top=0.12, bottom=0.16,
            footnote=INVENTED + " Troughs numbered in the order they form. "
                     "DeMark's line joins the two most recent.\nWhich "
                     "troughs qualify is DeMark's own rule, which the book "
                     "does not give: here all four do.",
        ),
    ),
    ChartArt(
        letter="AQ",
        draw=ck.annotated,
        kwargs=dict(
            series=DM_SERIES,
            size=PAIR,
            extend=20,
            strokes=(
                Stroke(points=(DM_TROUGHS[0],
                               (80, _through(DM_TROUGHS[0], DM_TROUGHS[1], 80))),
                       label="1  1st: steepest", at=1, dx=-6, dy=10),
                Stroke(points=(DM_TROUGHS[0],
                               (80, _through(DM_TROUGHS[0], DM_TROUGHS[2], 80))),
                       tone="quiet",
                       label="2  2nd: flatter", at=1, dx=-6, dy=10),
                Stroke(points=(DM_TROUGHS[0],
                               (80, _through(DM_TROUGHS[0], DM_TROUGHS[3], 80))),
                       tone="notice",
                       label="3  3rd: flattest", at=1, dx=-6, dy=10),
            ),
            notes=(
                Note(x=DM_TROUGHS[0][0], y=DM_TROUGHS[0][1],
                     label="All three\nstart here", dx=10, dy=-30),
            ),
            top=0.14, bottom=0.10,
            footnote=INVENTED + " All three fan out from the one trough. "
                     "The book draws only three; a line beyond\nthe third "
                     "carries no special rule of its own.",
        ),
    ),
    ChartArt(
        letter="AN",
        draw=ck.annotated,
        kwargs=dict(
            series=RC_SERIES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(40, 50, 60),
            extend=22,
            strokes=(
                Stroke(points=((20, RC_LEVELS[0]), (102, RC_LEVELS[0])),
                       dashed=True, tone="notice", label="38.2%: PHP 47.64",
                       at=1, dx=-2, dy=-9),
                Stroke(points=((20, RC_LEVELS[1]), (102, RC_LEVELS[1])),
                       dashed=True, tone="notice", label="50%: PHP 50.00",
                       at=1, dx=-2, dy=9),
                Stroke(points=((20, RC_LEVELS[2]), (102, RC_LEVELS[2])),
                       dashed=True, tone="notice", label="61.8%: PHP 52.36",
                       at=1, dx=-2, dy=10),
                Stroke(points=((20, 40.0), (80, 48.0))),
                Stroke(points=((20, 46.04), (80, 54.04))),
            ),
            notes=(
                Note(x=0, y=60.0, label="The prior fall starts: PHP 60",
                     dx=10, dy=6),
                Note(x=20, y=40.0, label="and ends: PHP 40", dx=10, dy=-14),
                Note(x=32, y=RC_LEVELS[0], label="Turns at\n38.2%", dx=-6,
                     dy=40),
                Note(x=50, y=RC_LEVELS[1], label="Turns at\n50%", dx=-6,
                     dy=50),
                Note(x=68, y=RC_LEVELS[2], label="Turns at\n61.8%", dx=-6,
                     dy=52, notice=True),
            ),
            top=0.22, bottom=0.22,
            footnote=INVENTED + " Dashed: 38.2, 50 and 61.8 percent of the "
                     "PHP 20 fall, measured up from PHP 40.\nGreen: a rising "
                     "channel, drawn so that each of its swings turns at one "
                     "level.",
        ),
    ),
    ChartArt(
        letter="AS",
        draw=ck.annotated,
        kwargs=dict(
            series=GAP_SERIES,
            size=PAIR,
            breaks=GAP_BREAKS,
            boxes=(
                Box(x0=12.5, x1=len(GAP_UP), lo=46, hi=49, tone="notice"),
                Box(x0=GAP_X + 10.5, x1=len(GAP_SERIES), lo=50, hi=53,
                    tone="notice"),
            ),
            notes=(
                Note(x=12.5, y=47.5, label="Gap up", dx=-10, dy=44,
                     dot=False),
                Note(x=38, label="Price returns\nfrom above: the\ngap is "
                     "support", dx=-8, dy=-60, notice=True),
                Note(x=GAP_X + 10.5, y=51.5, label="Gap down", dx=14, dy=46,
                     dot=False),
                Note(x=GAP_X + 32, label="Price returns\nfrom below: the\n"
                     "gap is resistance", dx=-8, dy=-76, notice=True),
            ),
            xlabel="", ylabel="Price",
            top=0.30, bottom=0.50,
            footnote=INVENTED + " Two stretches. Each gold band is the price "
                     "range a gap skipped, carried forward.\nThe book says "
                     "area, and does not say which edge of a gap holds.",
        ),
    ),
    ChartArt(
        letter="AT",
        draw=ck.bar_waves,
        kwargs=dict(
            bars=PL_BARS, size=PAIR,
            traces=(Trace(values=PL_LINE, tone="structure", width=2.2),),
            notes=(
                Note(x=10, y=PL_LINE[10], label="Price above\nthe line:\n"
                     "bullish", dx=-10, dy=64),
                Note(x=PL_TURN, y=PL_LINE[PL_TURN], label="The line turns "
                     "down:\nsome sell here", dx=-24, dy=40, notice=True),
                Note(x=31, y=PL_LINE[31], label="Price below\nthe line:\n"
                     "bearish", dx=-10, dy=-54),
            ),
            xlabel="Time", ylabel="Price",
            top=0.34, bottom=0.12,
            footnote="Invented bars. Green: a three-bar average of the "
                     "closes, shifted forward one bar as the book\nallows, "
                     "standing in for the PLdot. The book's averages typical "
                     "price, undefined in this chapter.",
        ),
    ),
    ChartArt(
        letter="O",
        draw=ck.annotated,
        kwargs=dict(
            series=DV_CLOSES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(55, 60, 65),
            volume=DV_AVERAGE,
            volume_label="Ratio, averaged",
            strokes=(
                Stroke(points=((DV_P1, DV_CLOSES[DV_P1] + 1.2),
                               (DV_P2, DV_CLOSES[DV_P2] + 1.2)),
                       tone="notice", arrow=True, width=2.0),
            ),
            volume_strokes=(
                Stroke(points=((DV_P1, DV_AVERAGE[DV_P1] + 0.10),
                               (DV_P2, DV_AVERAGE[DV_P2] + 0.10)),
                       tone="notice", arrow=True, width=2.0),
            ),
            notes=(
                Note(x=18, y=(DV_CLOSES[DV_P1] + DV_CLOSES[DV_P2]) / 2 + 1.4,
                     label="Price: the second\npeak is higher", dx=-66,
                     dy=30, dot=False, notice=True),
            ),
            volume_notes=(
                Note(x=29, y=0.62,
                     label="The ratio:\nits second\npeak is lower",
                     dx=14, dy=2, notice=True),
            ),
            xlabel="Time",
            top=0.34, bottom=0.10,
            footnote="Invented: forty bars, each PHP 2 from low to high. "
                     "Line: their closes. Lower panel: the three-bar\n"
                     "average of their bar stochastic. Through the second "
                     "rally the closes sit lower in each bar.",
        ),
    ),
    ChartArt(
        letter="S",
        draw=ck.annotated,
        kwargs=dict(
            series=DV_CLOSES,
            size=PAIR,
            ylabel="Price (PHP)",
            price_ticks=(55, 60, 65),
            volume=DV_AVERAGE,
            volume_label="Ratio, averaged",
            strokes=(
                Stroke(points=((DV_P1, DV_CLOSES[DV_P1] + 1.2),
                               (DV_P2, DV_CLOSES[DV_P2] + 1.2)),
                       tone="notice", arrow=True, width=2.0),
            ),
            volume_strokes=(
                Stroke(points=((DV_P1, DV_AVERAGE[DV_P1] + 0.10),
                               (DV_P2, DV_AVERAGE[DV_P2] + 0.10)),
                       tone="notice", arrow=True, width=2.0),
            ),
            notes=(
                Note(x=18, y=(DV_CLOSES[DV_P1] + DV_CLOSES[DV_P2]) / 2 + 1.4,
                     label="Price: the second\npeak is higher", dx=-66,
                     dy=30, dot=False, notice=True),
            ),
            volume_notes=(
                Note(x=29, y=0.62,
                     label="The ratio:\nits second\npeak is lower",
                     dx=14, dy=2, notice=True),
            ),
            xlabel="Time",
            top=0.34, bottom=0.10,
            footnote="The same invented bars as the chart two topics back: "
                     "the one it is recalling. Line: their\ncloses. Lower "
                     "panel: the three-bar average of their bar stochastic.",
        ),
    ),
)
