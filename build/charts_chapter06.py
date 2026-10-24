"""Chapter 6 teaching charts for FIN1209, as plain data.

Forty four charts, lettered A to Z and then AA to AR, in the order the deck
shows them. This file carries no drawing code: the forms it uses, panels
and cells, were added to build/chartkit.py for this chapter, which reads
volume and open interest against price, and every entry below is data
handed to one of them.

Chapter 6 has 44 figures and every one is placed in the deck. A chart is
drawn here only where the book makes a point in words that none of its own
figures shows, where its figure is a sketch or a dense real chart that does
not carry the idea alone, or where a slide works a number through:

  * **A, B** how a chart draws volume, and what one day's volume adds up.
  * **C to I** Part 1: the two principles, bullish and bearish volume,
    divergence and confirmation, standard divergence against volume
    divergence, Figure 6.6's periods on one invented uptrend, and the two
    kinds of volume oscillator.
  * **J to Q** Part 2: why a breakout is expected at minimum volume, a low
    volume reversal, the VWMA and its two readings, the four kinds of top
    and bottom, a higher and a lower overextension level, a volume extreme
    read only in retrospect, and one volume record on two timeframes.
  * **R to V** Part 3: why a volume peak makes the stronger barrier (RA),
    the five volume actions at a barrier and what each tells (R, RB, RC,
    lettered beside R until the deck is lettered again), the four filters
    and filters 1 and 2 in numbers (SA), a smoothed volume filter, a three-sigma
    filter and a channel drawn from volume filtered points.
  * **W to AG** Part 4: a trend on flat volume, loss aversion, bull and
    bear market volume, turnover, open interest day by day, the four cases
    of price, volume and open interest, open interest and reversal speed,
    tick volume, the TRIN worked, volume by price, and the book's four
    steps to support and resistance.
  * **AH to AL** Part 5: the four named bars, the two reversal bars, the
    rest and continuation bars, price leading volume, and the intraday
    volume cycle.
  * **FA, AM to AR, FB, FC** Part 6: the three readings of an oscillator
    the part uses (FA), the OBV worked, its start date (AN) and its
    weakness (FC), the ADL worked, its multiplying factor, the CMF worked,
    the NYSE Up/Down Volume worked (FB), and the test of a historical open
    interest level the COT report is read for. FA, FB and FC were added by
    the Part 6 rework under letters of their own, so that ranges reworked in
    parallel could not collide; they are lettered out of the deck's order.

**Teach only what the textbook teaches.** Every label on these charts is a
statement the book's Chapter 6 makes, or arithmetic it sets out. Where a
chart computes something the book names and does not define here (the
VWMA of L and M, the averages of T, U and S, the OBV of I), its small print
says how we computed it and that the book's own calculation is elsewhere.

**The data is invented.** We hold no market data licence. Every price and
volume here comes from a fixed seed or is set by hand, offline and
reproducible, and every chart carries the credit line deckkit.chart_credit()
prints under it. The sketches in the cells charts are not prices at all,
and say so.

**An annotation is in the slide's own words.** Every thing a slide names is
marked on its chart: numbered points, labelled lines, the arithmetic written
beside the columns it adds up.
"""

from __future__ import annotations

import math
import random

import chartkit as ck
from chartkit import (Bar, Box, Bracket, Cell, ChartArt, Guide, Note, Pane,
                      Span, Stroke, Trace)

# Every chart sits in the picture column of a Pair. Beside a teaching slide
# the text column is 5.6in wide; beside a term it is 6.2in and the picture
# column starts lower. These two widths are CHART_W and TERM_CHART_W in
# content_chapter06.py.
PAIR = ck.pair_size(5.6)
TERM = ck.pair_size(6.6, term=True)
# Beside a 6.0in text column, WIDE_W in content_chapter06.py.
WIDE = ck.pair_size(6.0)

INVENTED = "Invented prices and volume."
SKETCH = "Not prices: sketches."


# --------------------------------------------------------------------------
# Helpers that make series. Arithmetic only; nothing here draws.
# --------------------------------------------------------------------------


def _line(pivots, seed, noise=0.004, wobble=0.05):
    return ck.walk(tuple(pivots), seed=seed, wobble=wobble, noise=noise)


def _bars(closes, seed, reach=0.010):
    """Price bars around a run of closes: each opens near the last close."""
    rng = random.Random(seed)
    out = []
    prev = closes[0]
    for c in closes:
        o = prev + (c - prev) * rng.uniform(0.0, 0.4)
        hi = max(o, c) + abs(c) * reach * rng.uniform(0.3, 1.0)
        lo = min(o, c) - abs(c) * reach * rng.uniform(0.3, 1.0)
        out.append(Bar(open=round(o, 3), high=round(hi, 3), low=round(lo, 3),
                       close=round(c, 3)))
        prev = c
    return tuple(out)


def _noisy(levels, seed, spread=0.18):
    rng = random.Random(seed)
    return tuple(round(v * rng.uniform(1 - spread, 1 + spread), 3)
                 for v in levels)


def _ramp(a, b, n):
    """n values from a to b, evenly."""
    if n == 1:
        return [a]
    return [a + (b - a) * i / (n - 1) for i in range(n)]


def _sma(values, n):
    out = []
    for i in range(len(values)):
        window = values[max(0, i - n + 1):i + 1]
        out.append(sum(window) / len(window))
    return tuple(round(v, 4) for v in out)


def _band(values, n, k):
    """The n-bar average plus k standard deviations of the same n bars."""
    out = []
    for i in range(len(values)):
        window = values[max(0, i - n + 1):i + 1]
        mean = sum(window) / len(window)
        var = sum((v - mean) ** 2 for v in window) / len(window)
        out.append(round(mean + k * math.sqrt(var), 4))
    return tuple(out)


def _vwma(closes, volumes, n):
    out = []
    for i in range(len(closes)):
        lo = max(0, i - n + 1)
        pv = sum(c * v for c, v in zip(closes[lo:i + 1], volumes[lo:i + 1]))
        vv = sum(volumes[lo:i + 1])
        out.append(round(pv / vv, 4))
    return tuple(out)


def _obv(closes, volumes, start=0):
    total, out = 0.0, []
    for i, (c, v) in enumerate(zip(closes, volumes)):
        if i > start:
            if c > closes[i - 1]:
                total += v
            elif c < closes[i - 1]:
                total -= v
        out.append(round(total, 4))
    return tuple(out)


def _arrow(p0, p1, tone="structure", width=2.0):
    return Stroke(points=(p0, p1), arrow=True, tone=tone, width=width)


# ==========================================================================
# Part 1
# ==========================================================================

# A - a price chart and its volume panel. Day 40 closes at PHP 52.40 on
# 2.4 million shares.
A_DAY = 40
_a_close = list(_line(((0, 46.0), (14, 50.5), (22, 48.6), (A_DAY, 52.4),
                       (48, 51.2), (59, 54.0)), seed=601, noise=0.003))
A_BARS = _bars(_a_close, seed=602)
_a_vol = list(_noisy([1.6 + 0.4 * math.sin(i / 4.0) for i in range(60)],
                     seed=603, spread=0.25))
_a_vol[A_DAY] = 2.4
A_VOL = tuple(_a_vol)

# C - two rallies: the first on rising volume, the second on falling.
_c_close = _line(((0, 40.0), (22, 47.0), (32, 44.5), (58, 51.0)), seed=611,
                 noise=0.003)
C_BARS = _bars(_c_close, seed=612)
C_VOL = _noisy(_ramp(1.2, 3.0, 22) + _ramp(2.6, 1.6, 10)
               + _ramp(2.4, 0.9, 27), seed=613, spread=0.12)


def _cell(name, note, price, volume, *, tone="structure", vol_line=None):
    """A price sketch over volume columns, for the 2x2 cells."""
    panes = [Pane(line=tuple(price), height=1.2, top=0.15, bottom=0.15)]
    panes.append(Pane(columns=tuple(volume), height=1.0, top=0.10))
    return Cell(name=name, note=note, panes=tuple(panes), tone=tone)


_UP = (1.0, 1.6, 1.4, 2.2, 2.0, 2.8, 2.6, 3.4)
_DOWN = tuple(reversed(_UP))
_RISE = (1.0, 1.4, 1.8, 2.2, 2.6, 3.0, 3.4, 3.8)
_FALL = tuple(reversed(_RISE))

# F - confirmation continues, divergence turns.
_f_up = _line(((0, 40.0), (30, 50.0), (44, 55.0)), seed=621, noise=0.004)
_f_turn = _line(((0, 40.0), (30, 50.0), (36, 51.0), (44, 46.0)), seed=622,
                noise=0.004)
F_VOL_UP = _noisy(_ramp(1.0, 3.2, 45), seed=623, spread=0.15)
F_VOL_DOWN = _noisy(_ramp(3.2, 0.9, 37) + _ramp(1.2, 1.4, 8), seed=624,
                    spread=0.15)

# G - standard divergence against volume divergence.
G_PRICE = _line(((0, 50.0), (12, 58.0), (20, 54.0), (32, 60.0), (40, 56.0)),
                seed=631, noise=0.002, wobble=0.02)
G_OSC = _line(((0, 20.0), (12, 80.0), (20, 40.0), (32, 62.0), (40, 30.0)),
              seed=632, noise=0.01, wobble=0.02)
G_RISE = _line(((0, 50.0), (40, 60.0)), seed=633, noise=0.004)
G_VOL = _noisy(_ramp(3.0, 1.0, 41), seed=634, spread=0.15)

# H - one uptrend in four periods.
H_CUTS = (0, 20, 32, 56, 79)
_h_close = _line(((0, 40.0), (20, 48.0), (32, 45.5), (40, 47.3), (46, 45.6),
                  (52, 47.0), (56, 46.2), (79, 55.0)), seed=641, noise=0.003)
H_BARS = _bars(_h_close, seed=642)
_h_vol = (_ramp(1.2, 3.0, 20) + _ramp(2.6, 1.3, 12) + _ramp(1.8, 0.55, 24)
          + _ramp(2.6, 3.4, 23))
H_VOL = _noisy(_h_vol, seed=643, spread=0.12)

# I - price, volume, and a price-based line from the same data.
_i_close = list(_line(((0, 50.0), (10, 54.0), (18, 51.0), (28, 56.0),
                       (39, 53.0)), seed=651, noise=0.006))
I_CLOSE = tuple(round(c, 2) for c in _i_close)
I_VOL = _noisy([2.0] * 40, seed=652, spread=0.35)
I_OBV = _obv(I_CLOSE, I_VOL)

# ==========================================================================
# Part 2
# ==========================================================================

# J - a range with stops above and below, volume falling to its lowest,
# and the breakout.
J_TOP, J_BOT = 52.0, 48.0
J_BREAK = 60
_j_close = _line(((0, 44.0), (12, 50.0), (18, 51.4), (24, 48.6), (31, 51.5),
                  (38, 48.5), (45, 51.2), (52, 48.8), (J_BREAK - 1, 51.0),
                  (J_BREAK, 52.6), (72, 57.5)), seed=661, noise=0.002,
                 wobble=0.03)
J_BARS = _bars(_j_close, seed=662, reach=0.006)
_j_vol = (_ramp(2.4, 2.0, 12) + _ramp(1.9, 0.5, J_BREAK - 12)
          + [3.4] + _ramp(2.8, 2.2, 72 - J_BREAK))
J_VOL = list(_noisy(_j_vol, seed=663, spread=0.12))
J_VOL[J_BREAK - 1] = 0.42
J_VOL[J_BREAK] = 3.6
J_VOL = tuple(J_VOL)
J_LOW = 0.45

# K - a low volume reversal at a peak and at a trough.
K_PEAK, K_TROUGH = 28, 54
_k_close = _line(((0, 44.0), (K_PEAK, 56.0), (K_TROUGH, 47.0), (78, 55.0)),
                 seed=671, noise=0.003)
K_LINE = tuple(_k_close)
_k_vol = []
for i in range(79):
    d = min(abs(i - K_PEAK), abs(i - K_TROUGH))
    _k_vol.append(0.6 + min(d, 14) * 0.13)
K_VOL = list(_noisy(_k_vol, seed=672, spread=0.10))
K_VOL[K_PEAK] = 0.55
K_VOL[K_TROUGH] = 0.55
K_VOL = tuple(K_VOL)
K_LOW = 0.6

# L and M - a price and its 10-bar VWMA.
_l_close = list(_line(((0, 50.0), (14, 55.0), (26, 49.0), (40, 54.5),
                       (52, 50.0), (66, 57.0), (79, 53.0)), seed=681,
                      noise=0.004))
L_CLOSE = tuple(round(c, 3) for c in _l_close)
L_VOL = _noisy([2.0 + 0.8 * math.sin(i / 3.0) for i in range(80)],
               seed=682, spread=0.3)
L_VWMA = _vwma(L_CLOSE, L_VOL, 10)


def _crossings(closes, line, start=12):
    ups, downs = [], []
    for i in range(start, len(closes)):
        if closes[i - 1] <= line[i - 1] and closes[i] > line[i]:
            ups.append(i)
        if closes[i - 1] >= line[i - 1] and closes[i] < line[i]:
            downs.append(i)
    return ups, downs


L_UPS, L_DOWNS = _crossings(L_CLOSE, L_VWMA)

# N - four turns, each sketched over its volume.
_TOP = (1.0, 2.0, 3.0, 3.6, 3.0, 2.0, 1.0)
_BOTTOM = tuple(4.6 - v for v in _TOP)
_EXTREME = (1.0, 1.2, 1.4, 4.0, 1.4, 1.2, 1.0)
_MINIMAL = (2.0, 1.8, 1.6, 0.4, 1.6, 1.8, 2.0)

# O - two major turns and three corrections, with two volume levels.
O_TURNS = {"1": 30, "2": 70, "a": 14, "b": 48, "c": 88}
_o_close = _line(((0, 50.0), (O_TURNS["a"], 55.0), (19, 53.0),
                  (O_TURNS["1"], 60.0), (40, 52.0), (O_TURNS["b"], 49.5),
                  (54, 51.0), (O_TURNS["2"], 42.0), (80, 48.0),
                  (O_TURNS["c"], 50.5), (99, 47.5)), seed=691, noise=0.003)
O_LINE = tuple(_o_close)
_o_vol = list(_noisy([1.2] * 100, seed=692, spread=0.25))
for key, x in O_TURNS.items():
    _o_vol[x] = 4.6 if key in "12" else 2.6
O_VOL = tuple(_o_vol)
O_UPPER, O_LOWER = 4.0, 2.2

# Q - one daily record with a late spike, and its months.
_q_days = []
rng_q = random.Random(701)
for d in range(240):
    month = d // 20
    level = 1.0 + 1.6 * math.exp(-((month - 4.5) ** 2) / 6.0)
    _q_days.append(round(level * rng_q.uniform(0.6, 1.4), 3))
Q_SPIKE = 225
_q_days[Q_SPIKE] = 6.0
Q_DAYS = tuple(_q_days)
Q_MONTHS = tuple(round(sum(Q_DAYS[m * 20:(m + 1) * 20]), 2)
                 for m in range(12))
Q_BUSIEST = max(range(12), key=lambda m: Q_MONTHS[m])

# ==========================================================================
# Part 3
# ==========================================================================

# The barrier sketches of R and RB: seven bars, the touch on the middle one,
# volume in whole millions of shares so every bar can carry its number. At
# a support price falls to the line and turns up; at a resistance it rises
# to the line and turns down, the two rows of the book's Figure 6.19.
_V_SHAPE = (6.0, 4.0, 2.4, 1.0, 2.4, 4.0, 6.0)
_A_SHAPE = (1.0, 3.0, 4.6, 6.0, 4.6, 3.0, 1.0)
_TOUCH = 3


def _barrier(name, note, volume, *, side, retest=False):
    """One case at a support or a resistance, its volume numbered.

    ``retest`` adds three bars after the turn in which price comes back to
    the barrier, with no volume drawn under them: the book says a retest
    is likely and gives no volume for it.
    """
    support = side == "support"
    price = list(_V_SHAPE if support else _A_SHAPE)
    vol = list(volume)
    level = 0.85 if support else 6.15
    x1 = 4.5
    notes = ()
    if retest:
        price += [4.4, 2.6, 1.1] if support else [2.6, 4.4, 5.9]
        vol += [0, 0, 0]
        x1 = 9.5
        notes = (Note(x=9, label="retest", dx=-2, dy=16 if support else -16,
                      dot=True, notice=True),)
    line = Stroke(points=((1.5, level), (x1, level)), tone="structure",
                  width=2.4)
    return Cell(name=name, note=note, panes=(
        Pane(line=tuple(price), strokes=(line,), notes=notes, height=1.3,
             top=0.30 if not support else 0.12,
             bottom=0.12 if not support else 0.30),
        Pane(columns=tuple(vol), picks=(_TOUCH,),
             dims=tuple(range(7, len(vol))),
             tags=tuple((i, f"{v:g}") for i, v in enumerate(volume)),
             height=1.0, top=0.30)))


# RA - two resistances at PHP 60, one touched on the most volume of the
# move and one on the least, each followed by a retest whose outcome is not
# drawn: the book says only which barrier is more reliable.
RA_PRICE = (52.0, 55.0, 57.5, 59.0, 60.0, 59.0, 57.5, 55.5, 54.5, 56.0,
            58.0, 59.8)
RA_PEAK = (2, 3, 5, 7, 9, 6, 4, 3, 2)
RA_DIP = (7, 5, 3, 1.5, 0.5, 1.5, 3, 5, 7)


def _resistance_60(name, note, volume):
    vol = list(volume) + [0, 0, 0]
    return Cell(name=name, note=note, panes=(
        Pane(line=RA_PRICE, height=1.4, top=0.42, bottom=0.10,
             strokes=(Stroke(points=((2.5, 60.15), (11.5, 60.15)),
                             tone="structure", width=2.4,
                             label="PHP 60", at=0, dx=-4, dy=0),),
             notes=(Note(x=11, y=59.8, label="retest", dx=-6, dy=-22,
                         notice=True),)),
        Pane(columns=tuple(vol), picks=(4,),
             tags=tuple((i, f"{v:g}") for i, v in enumerate(volume)),
             height=1.0, top=0.28)))


# S - four filters, sketched on invented volume.
_s_base = _noisy([1.0 + 0.25 * math.sin(i / 2.0) for i in range(30)],
                 seed=711, spread=0.2)
S_MA_VOL = list(_s_base)
for x, v in ((8, 3.0), (21, 2.8)):
    S_MA_VOL[x] = v
S_MA_VOL = tuple(S_MA_VOL)
S_MA = _sma(S_MA_VOL, 8)
# SA - our rule for "well above": more than twice the 8-bar average.
S_TWICE = tuple(round(2 * v, 4) for v in S_MA)
S_BAND_VOL = list(_s_base)
S_BAND_VOL[17] = 3.2
S_BAND_VOL[8] = 1.9
S_BAND_VOL = tuple(S_BAND_VOL)
S_BAND = tuple(round(v + 1.6, 3) for v in _sma(S_BAND_VOL, 8))
S_PEAK_VOL = list(_s_base)
S_PEAK_VOL[6] = 2.6
S_PEAK_VOL[24] = 2.6
S_PEAK_VOL = tuple(S_PEAK_VOL)
S_CYCLE_VOL = _noisy([1.0 + 0.9 * max(0.0, math.sin(i * math.pi / 7.5))
                      for i in range(30)], seed=712, spread=0.10)
# The tallest bar of each swell of the cycle.
S_CYCLE_PEAKS = tuple(max(range(a, min(a + 15, 30)), key=lambda i: S_CYCLE_VOL[i])
                      for a in range(0, 30, 15))

# T - a smoothed volume filter: a 20-bar average, four spikes at turns.
T_TURNS = (18, 38, 62, 84)
_t_close = _line(((0, 50.0), (T_TURNS[0], 57.0), (T_TURNS[1], 49.0),
                  (T_TURNS[2], 58.5), (T_TURNS[3], 50.5), (99, 54.0)),
                 seed=721, noise=0.004)
T_LINE = tuple(_t_close)
_t_vol = list(_noisy([1.5] * 100, seed=722, spread=0.35))
for x in T_TURNS:
    _t_vol[x] = 4.4
T_VOL = tuple(_t_vol)
T_MA = _sma(T_VOL, 20)

# U - a three-sigma filter: a 20-bar average plus three standard
# deviations of the same 20 bars.
_u_vol = list(_noisy([1.5] * 100, seed=731, spread=0.40))
for x, v in ((24, 4.2), (57, 4.6), (83, 4.4), (40, 2.6), (70, 2.5)):
    _u_vol[x] = v
U_VOL = tuple(_u_vol)
U_MA = _sma(U_VOL, 20)
U_BAND = _band(U_VOL, 20, 3.0)
U_PICKS = tuple(i for i in range(20, 100) if U_VOL[i] > U_BAND[i - 1])

# V - volume filtered inflection points: which turns count. Every peak and
# trough is dotted. Three came on 3.0 million, above a threshold set by eye
# at 2.5; the other seven, X among them, on 1.0, below the average bar.
#
# VA - the same price and volume, with the channel drawn from 1, 2 and 3 for
# the step by step slide. The line through peaks 1 and 2 rises PHP 4.00 over
# 40 bars, PHP 0.10 a bar; its parallel through trough 3 is the channel's
# lower line, and price comes back to that line at X, bar 72, PHP 51.80,
# 28 bars after trough 3, and turns up. Bar numbers are on its time axis.
V_POINTS = {"1": 22, "2": 62, "3": 44}
V_SKIPPED = (10, 16, 34, 38, 52, 56)
V_X = 72
V_THRESHOLD = 2.5
_v_close = _line(((0, 46.0), (V_SKIPPED[0], 49.0), (V_SKIPPED[1], 47.6),
                  (V_POINTS["1"], 52.0), (V_SKIPPED[2], 49.4),
                  (V_SKIPPED[3], 51.0), (V_POINTS["3"], 49.0),
                  (V_SKIPPED[4], 53.0), (V_SKIPPED[5], 51.8),
                  (V_POINTS["2"], 56.0), (V_X, 51.8), (84, 55.0)),
                 seed=741, noise=0.002, wobble=0.02)
V_LINE = tuple(_v_close)
_v_vol = list(_noisy([1.3] * 85, seed=742, spread=0.25))
for x in V_POINTS.values():
    _v_vol[x] = 3.0
for x in V_SKIPPED + (V_X,):
    _v_vol[x] = 1.0
V_VOL = tuple(_v_vol)
V_AVERAGE = sum(V_VOL) / len(V_VOL)
V_SLOPE = (V_LINE[V_POINTS["2"]] - V_LINE[V_POINTS["1"]]) / (
    V_POINTS["2"] - V_POINTS["1"])


def _v_top(x):
    return V_LINE[V_POINTS["1"]] + V_SLOPE * (x - V_POINTS["1"])


def _v_bottom(x):
    return V_LINE[V_POINTS["3"]] + V_SLOPE * (x - V_POINTS["3"])


# ==========================================================================
# Part 4
# ==========================================================================

W_LINE = _line(((0, 40.0), (20, 44.0), (28, 43.0), (50, 49.0), (58, 48.0),
                (80, 55.0)), seed=751, noise=0.003)
W_VOL = _noisy([2.0] * 81, seed=752, spread=0.12)

X_LINE = _line(((0, 50.0), (12, 47.0), (18, 48.5), (34, 42.0), (40, 43.4),
                (60, 38.0)), seed=761, noise=0.003)
X_VOL = _noisy(_ramp(2.6, 0.7, 61), seed=762, spread=0.15)

Y_LINE = _line(((0, 40.0), (40, 56.0), (80, 44.0)), seed=771, noise=0.004)
Y_VOL = _noisy(_ramp(2.6, 3.0, 40) + _ramp(1.5, 1.2, 41), seed=772,
               spread=0.18)

# AF and AG - a price whose volume by price is added up from its own days.
# A long range between about PHP 47.4 and PHP 50.9 trades heavily, with two
# bursts of volume inside it; price then rises away and comes back.
_af_close = list(_line(((0, 56.0), (10, 52.0), (18, 49.5), (24, 47.4),
                        (32, 50.9), (38, 48.6), (44, 47.5), (50, 50.8),
                        (56, 49.0), (64, 55.0), (72, 58.6), (80, 57.0),
                        (88, 52.0), (99, 54.0)),
                       seed=781, noise=0.002, wobble=0.03))
AF_LINE = tuple(round(c, 3) for c in _af_close)
_af_vol = [1.2] * 100
for i in range(100):
    _af_vol[i] = 1.0 + (1.6 if 18 <= i <= 56 else 0.0) * random.Random(
        782 + i).uniform(0.6, 1.2)
for i in (26, 27, 28, 29, 30, 46, 47, 48, 49):
    _af_vol[i] += 1.6
AF_VOL = _noisy(_af_vol, seed=783, spread=0.12)
AF_EDGES = tuple(range(46, 62, 2))


def _profile(closes, volumes, edges):
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        amount = sum(v for c, v in zip(closes, volumes) if lo <= c < hi)
        rows.append((lo, hi, round(amount, 3)))
    return tuple(rows)


AF_PROFILE = _profile(AF_LINE, AF_VOL, AF_EDGES)
AF_BIG = max(range(len(AF_PROFILE)), key=lambda i: AF_PROFILE[i][2])
AF_LABELS = tuple(f"{round(row[2])}m" for row in AF_PROFILE)
AG_LO, AG_HI = AF_PROFILE[AF_BIG][0], AF_PROFILE[AF_BIG][1]
# Step 2: the two busiest stretches of days, the bursts set above.
AG_SPANS = ((25.5, 30.5), (45.5, 49.5))


def _turns(series, sign, width=3):
    """Indices of the peaks (sign 1) or troughs (sign -1) of a series."""
    out = []
    for i in range(width, len(series) - width):
        window = series[i - width:i + width + 1]
        if series[i] == (max(window) if sign > 0 else min(window)):
            out.append(i)
    return out


# Step 4: the closest peak above the intersection and the closest trough
# below it, found from the line itself.
AG_PEAK = min((i for i in _turns(AF_LINE, 1) if AF_LINE[i] > AG_HI),
              key=lambda i: AF_LINE[i])
AG_TROUGH = max((i for i in _turns(AF_LINE, -1) if AF_LINE[i] < AG_LO),
                key=lambda i: AF_LINE[i])
AG_RES = AF_LINE[AG_PEAK]
AG_SUP = AF_LINE[AG_TROUGH]

# AK - price breaks a falling trendline a little, then volume follows.
AK_BREAK = 44
_ak_close = _line(((0, 60.0), (8, 57.0), (14, 58.6), (24, 54.0), (30, 55.4),
                   (40, 51.5), (AK_BREAK, 53.4), (50, 54.4), (54, 58.5),
                   (64, 63.0)), seed=791, noise=0.002, wobble=0.03)
AK_LINE = tuple(_ak_close)
_ak_vol = list(_noisy([1.3] * 65, seed=792, spread=0.2))
for i in range(52, 65):
    _ak_vol[i] = 2.8 + 0.4 * random.Random(793 + i).uniform(0, 1)
_ak_vol[AK_BREAK] = 1.3
AK_VOL = tuple(_ak_vol)

# AL - three days of hourly bars and their intraday volume cycle.
_al_close = []
rng_al = random.Random(801)
level = 1.3000
plan = {13: +1, 37: +1, 61: -1}
direction = -1
for h in range(72):
    hour = h % 24
    if h in (13, 37, 61):
        direction = {13: +1, 37: +1, 61: -1}[h]
    step = 0.0006 * direction if hour >= 13 else 0.0002 * rng_al.uniform(-1, 1)
    if h < 13:
        step = -0.0004 + 0.0002 * rng_al.uniform(-1, 1)
    level += step + 0.00015 * rng_al.uniform(-1, 1)
    _al_close.append(round(level, 5))
AL_BARS = _bars(_al_close, seed=802, reach=0.0004)
AL_VOL = _noisy([0.6 + 2.4 * math.exp(-(((h % 24) - 13.5) ** 2) / 3.0)
                 for h in range(72)], seed=803, spread=0.10)

# FA - an invented price and oscillator carrying the three readings Part 6
# uses: A a divergence of peaks at bars 14 and 34, B a rising line under the
# oscillator's lows at bars 5 and 22 that it falls through after bar 34, C a
# flat oversold level it touches at the price low, bar 48.
FA_LINE = _line(((0, 48.0), (14, 54.0), (22, 51.0), (34, 56.0), (48, 46.0),
                 (56, 49.0)), seed=871, noise=0.002, wobble=0.03)


def _fa_osc():
    pivots = ((0, 0.0), (5, -0.4), (14, 0.9), (22, 0.1), (34, 0.55),
              (48, -1.0), (56, -0.3))
    out = []
    for (x0, y0), (x1, y1) in zip(pivots, pivots[1:]):
        for x in range(x0, x1):
            out.append(y0 + (y1 - y0) * (x - x0) / (x1 - x0)
                       + 0.04 * math.sin(x * 1.7))
    out.append(pivots[-1][1])
    return tuple(round(v, 4) for v in out)


FA_OSC = _fa_osc()
FA_FLOOR = -0.9
# The first bar at which the oscillator is below the rising line: bar 35.
FA_BREAK = 35


def FA_RISE(x):
    """The rising line through the oscillator's lows at bars 5 and 22."""
    return round(-0.4 + (0.1 - -0.4) * (x - 5) / (22 - 5), 4)


# AM - six days of OBV.
AM_CLOSE = (50.00, 50.50, 50.20, 50.20, 50.80, 50.60)
AM_VOL = (1.0, 2.0, 1.5, 1.0, 3.0, 1.0)
AM_OBV = _obv(AM_CLOSE, AM_VOL)

# AN - AM's OBV started on day 3 instead of day 1: 0, 0, 3.0, 2.0 from day 3
# to day 6, the same changes 2.0 lower.
AN_LATE = tuple((i, round(v - AM_OBV[2], 4)) for i, v in enumerate(AM_OBV)
                if i >= 2)

# AR - a price top and its open interest testing an earlier peak.
AR_LINE = _line(((0, 40.0), (20, 50.0), (30, 46.0), (56, 58.0), (64, 53.0)),
                seed=821, noise=0.004)
AR_OI = _line(((0, 60.0), (18, 92.0), (30, 70.0), (55, 91.5), (64, 80.0)),
              seed=822, noise=0.006, wobble=0.03)
AR_LEVEL = 92.0


# AH, AI, AJ - short trends of hand-set bars, ending in a named bar.


def _run(start, step, rng, n, seed):
    """n bars whose closes move by ``step``, each ``rng`` from low to high."""
    r = random.Random(seed)
    out, close = [], start
    for _ in range(n):
        nxt = close + step * r.uniform(0.7, 1.3)
        lo_c, hi_c = min(close, nxt), max(close, nxt)
        pad = max(0.0, (rng - (hi_c - lo_c)) / 2)
        out.append(Bar(open=round(close, 3), high=round(hi_c + pad, 3),
                       low=round(lo_c - pad, 3), close=round(nxt, 3)))
        close = nxt
    return out


def _named(after, span, up=True):
    """One bar starting at the close of ``after``, ``span`` from low to
    high: a narrow bar is all but flat, a wide one runs the way of the
    trend."""
    o = after[-1].close
    if span < 1.0:
        return Bar(open=o, high=o + span * 0.6, low=o - span * 0.4,
                   close=o + span * 0.2)
    return Bar(open=o, high=o + span if up else o + 0.1,
               low=o - 0.1 if up else o - span,
               close=o + span * 0.9 if up else o - span * 0.9)


def _trend_bars(span):
    bars = _run(50.0, 0.6, 1.4, 7, seed=831)
    return tuple(bars + [_named(bars, span)])


def _box(bars, i):
    b = bars[i]
    return Box(x0=i - 0.45, x1=i + 0.45, lo=b.low - 0.12, hi=b.high + 0.12,
               tone="notice")


def _after(bars, step, rng, n, seed):
    last = bars[-1]
    return _run(last.close, step, rng, n, seed)


_ai_up = _run(50.0, 0.8, 1.0, 7, seed=841)
_ai_narrow = _ai_up + [_named(_ai_up, 0.25)]
AI_NARROW = tuple(_ai_narrow + _after(_ai_narrow, -1.0, 1.1, 4, seed=842))
_ai_wide = _ai_up + [_named(_ai_up, 3.4)]
AI_WIDE = tuple(_ai_wide + _after(_ai_wide, -1.2, 1.2, 4, seed=843))
AI_VOL_HIGH = (2.0, 2.1, 1.9, 2.0, 2.2, 1.9, 2.0, 4.4, 2.6, 2.4, 2.2, 2.0)
AI_VOL_LOW = (2.0, 2.1, 1.9, 2.0, 2.2, 1.9, 2.0, 0.7, 2.4, 2.2, 2.0, 1.9)

_aj_fast = _run(50.0, 1.6, 1.8, 6, seed=851)
_aj_fast = _aj_fast + [_named(_aj_fast, 0.3)]
AJ_FAST = tuple(_aj_fast + _after(_aj_fast, -1.4, 1.5, 4, seed=852))
_aj_slow = _run(50.0, 0.45, 0.8, 6, seed=853)
_aj_slow = _aj_slow + [_named(_aj_slow, 0.3)]
AJ_SLOW = tuple(_aj_slow + _after(_aj_slow, 0.05, 0.6, 2, seed=854)
                + _after(_aj_slow + _after(_aj_slow, 0.05, 0.6, 2, seed=854),
                         0.45, 0.8, 3, seed=855))
_aj_cont = _run(50.0, 0.8, 1.0, 6, seed=856)
_aj_cont = _aj_cont + [_named(_aj_cont, 3.0)]
AJ_CONT = tuple(_aj_cont + _after(_aj_cont, 0.9, 1.1, 4, seed=857))
AJ_VOL_REST_FAST = (2.6, 2.8, 3.0, 3.1, 3.3, 3.4, 0.8, 2.6, 2.4, 2.2, 2.0)
AJ_VOL_REST_SLOW = (1.6, 1.7, 1.5, 1.6, 1.7, 1.6, 0.6, 1.0, 1.1, 1.6, 1.7,
                    1.8)
AJ_VOL_CONT = (2.0, 2.1, 1.9, 2.0, 2.2, 1.9, 4.4, 2.6, 2.5, 2.4, 2.3)

# AK - the falling trendline through the peaks at bars 14 and 30.
_AK_P1, _AK_P2 = (14, 58.6), (30, 55.4)


def AK_TL(x):
    slope = (_AK_P2[1] - _AK_P1[1]) / (_AK_P2[0] - _AK_P1[0])
    return round(_AK_P1[1] + slope * (x - _AK_P1[0]), 3)


# AM - the OBV's volumes with their signs: day 1 is the start.
AM_SIGNED = (0.0, 2.0, -1.5, 0.0, 3.0, -1.0)
AM_SIGNS = ("start", "+2.0", "-1.5", "0", "+3.0", "-1.0")

# FC - a bar that makes a new high and closes a little lower.
FC_BARS = (Bar(open=50.0, high=51.0, low=49.6, close=50.8),
           Bar(open=50.9, high=54.0, low=50.5, close=50.7))

# FD - the Chaikin oscillator's steps on invented bars: thirty CMF values,
# their running total, a 3-bar and a 10-bar EMA of that total, and their
# difference. The EMA is the usual one, each value weighted 2 / (n + 1) and
# started at the first total; the book's chapter does not give its formula.
# Bar 17 reads 1.0 - 0.5 = +0.5 and bar 27 reads 0.6 - 0.8 = -0.2.
_fd_cmf = [(-0.10 if i < 8 else 0.20 if i < 20 else -0.15)
           + 0.03 * math.sin(i * 1.3) for i in range(30)]
FD_TOTAL = tuple(round(sum(_fd_cmf[:i + 1]), 4) for i in range(30))


def _ema(values, n):
    a = 2 / (n + 1)
    out = [values[0]]
    for v in values[1:]:
        out.append(a * v + (1 - a) * out[-1])
    return tuple(round(v, 4) for v in out)


FD_FAST = _ema(FD_TOTAL, 3)
FD_SLOW = _ema(FD_TOTAL, 10)
FD_OSC = tuple(round(f - w, 4) for f, w in zip(FD_FAST, FD_SLOW))
FD_UP, FD_DOWN = 17, 27

# AO - three bars from PHP 48 to PHP 52, closing at 52, 50 and 49.
AO_BARS = (Bar(open=50.0, high=52.0, low=48.0, close=52.0),
           Bar(open=50.0, high=52.0, low=48.0, close=50.0),
           Bar(open=50.5, high=52.0, low=48.0, close=49.0))


# ==========================================================================
# The charts, in the order the deck shows them.
# ==========================================================================

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=A_BARS, ylabel="Price (PHP)", ticks=(46, 50, 54),
                     height=2.0, top=0.30,
                     notes=(Note(x=A_DAY, label="Day 40's price bar:\n"
                                 "closes at PHP 52.40", dx=-92, dy=22,
                                 notice=True),),
                     name="Price: the main evidence"),
                Pane(columns=A_VOL, picks=(A_DAY,), ylabel="Volume",
                     ticks=(1, 2), height=1.0, top=0.55,
                     tags=((A_DAY, "2.4 million"),),
                     name="Volume: one bar under each price bar"),
            ),
            guides=(Guide(x=A_DAY, notice=True),),
            size=WIDE, xlabel="Time, one bar a day",
            footnote=INVENTED + " Volume in millions of shares.",
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(columns=(0.1, 0.6, 0.3, 1.2, 0.2, 0.0, 2.4),
                     picks=(6,), ylabel="Shares (million)", ticks=(0, 1, 2),
                     top=0.45,
                     tags=((0, "0.1"), (1, "0.6"), (2, "0.3"), (3, "1.2"),
                           (4, "0.2"), (6, "2.4")),
                     notes=(Note(x=6, y=2.4, label="The day's volume:\n"
                                 "0.1 + 0.6 + 0.3 + 1.2 + 0.2\n= 2.4 million",
                                 dx=-60, dy=12, dot=False, notice=True),)),
            ),
            xticks=((0, "Trade 1"), (1, "2"), (2, "3"), (3, "4"), (4, "5"),
                    (6, "The day")),
            size=TERM, xlabel="",
            footnote="Our example: one day's five trades, in million shares.",
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=C_BARS, ylabel="Price (PHP)", ticks=(40, 45, 50),
                     height=1.8, top=0.12,
                     tags=((0, "40"), (22, "47"), (58, "51")),
                     notes=(Note(x=32, label="44.5", dx=0, dy=-26,
                                 dot=False),)),
                Pane(columns=C_VOL, ylabel="Volume (million)", ticks=(1, 2, 3),
                     height=1.0, top=0.35,
                     tags=((0, "1.1"), (19, "2.9"), (34, "2.4"), (58, "0.9")),
                     strokes=(
                         _arrow((1, 2.0), (16, 3.6), tone="notice"),
                         _arrow((34, 3.4), (57, 1.7), tone="notice"),
                     )),
            ),
            spans=(Span(x0=0, x1=21, label="1  Rising volume:\ninterest",
                        tone="quiet"),
                   Span(x0=33, x1=58, label="2  Declining volume:\nlosing "
                        "interest", tone="quiet")),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " Both rallies rise; only the volume under "
                     "them differs.",
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _cell("Price up, volume up", "together: bullish volume",
                      _RISE, _UP),
                _cell("Price down, volume down", "together: bullish volume",
                      _FALL, _DOWN),
                _cell("Price up, volume down", "opposite: bearish volume",
                      _RISE, _DOWN),
                _cell("Price down, volume up", "opposite: bearish volume",
                      _FALL, _UP),
            ),
            cols=2, size=TERM,
            footnote=SKETCH + " In each case a price line over its volume.",
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _cell("Volume falling: divergence", "price rising", _RISE,
                      _DOWN),
                _cell("Volume rising: confirmation", "price rising", _RISE,
                      _UP),
                _cell("Volume falling: divergence",
                      "price falling: still divergence", _FALL, _DOWN),
                _cell("Volume rising: confirmation",
                      "price falling: still confirmation", _FALL, _UP),
            ),
            cols=2, size=TERM,
            footnote=SKETCH + " Left column: volume falls. Right: it "
                     "rises.\nPrice goes both ways in each column.",
        ),
    ),
    ChartArt(
        letter="F",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Volume rising: confirmation",
                     note="the trend continues",
                     panes=(Pane(line=tuple(_f_up), height=1.3, top=0.15,
                                 tags=((0, "40"), (44, "55"))),
                            Pane(columns=F_VOL_UP, height=1.0, top=0.25,
                                 tags=((0, "0.9"), (44, "3.4"))))),
                Cell(name="Volume falling: divergence",
                     note="a potential reversal",
                     panes=(Pane(line=tuple(_f_turn), height=1.3, top=0.15,
                                 tags=((0, "40"), (36, "51"), (44, "46"))),
                            Pane(columns=F_VOL_DOWN, height=1.0, top=0.25,
                                 tags=((0, "2.9"),),
                                 notes=(Note(x=36, label="0.8", dx=0, dy=22,
                                             dot=False),)))),
            ),
            cols=2, size=WIDE,
            footnote=INVENTED + " Prices in PHP, volume in millions. The "
                     "right-hand ending\nis one possibility, drawn to show the "
                     "warning.",
        ),
    ),
    ChartArt(
        letter="G",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Standard divergence,\nChapters 4 and 5",
                     note="peak against peak",
                     panes=(
                         Pane(line=tuple(G_PRICE), height=1.0, top=0.35,
                              tags=((12, "58"), (32, "60")),
                              strokes=(_arrow((12, 60.6), (32, 62.6),
                                              tone="notice"),)),
                         Pane(line=tuple(G_OSC), height=1.0, top=0.35,
                              tags=((12, "80"), (32, "62")),
                              strokes=(_arrow((12, 95.0), (32, 77.0),
                                              tone="notice"),)),
                     )),
                Cell(name="Volume divergence,\nChapter 6",
                     note="volume falling, whatever price does",
                     panes=(
                         Pane(line=tuple(G_RISE), height=1.0, top=0.20),
                         Pane(columns=G_VOL, height=1.0, top=0.25,
                              strokes=(_arrow((1, 3.6), (39, 1.5),
                                              tone="notice"),)),
                     )),
            ),
            cols=2, size=PAIR,
            footnote=INVENTED + " Left: price over an oscillator. Right: "
                     "price over its volume.",
        ),
    ),
    ChartArt(
        letter="H",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=H_BARS, ylabel="Price (PHP)", ticks=(40, 45, 50, 55),
                     height=1.8, top=0.10,
                     tags=((0, "40"), (20, "48"), (32, "45.5"), (79, "55"))),
                Pane(columns=H_VOL, ylabel="Volume (million)", ticks=(1, 2, 3),
                     height=1.0, top=0.45,
                     notes=(Note(x=55, label="3  Minimum:\n0.5 million",
                                 dx=-36, dy=40),)),
            ),
            guides=tuple(Guide(x=x - 0.5) for x in H_CUTS[1:-1]),
            spans=(Span(x0=0, x1=19.5, label="1\nconfirmation"),
                   Span(x0=20.5, x1=31.5, label="2\ndivergence",
                        tone="quiet"),
                   Span(x0=32.5, x1=55.5, label="3\nconsolidation"),
                   Span(x0=56.5, x1=79, label="4\nconfirmation",
                        tone="quiet")),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " 1, 2 and 4: bullish volume. 3: price "
                     "sideways, no reading.",
        ),
    ),
    ChartArt(
        letter="I",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=I_CLOSE, name="Price: the closes", height=1.0,
                     top=0.35),
                Pane(columns=I_VOL, name="Volume bars: non-price-based",
                     height=0.9, top=0.55),
                Pane(line=I_OBV, name="A line that needs price: "
                     "price-based", height=1.0, top=0.45),
            ),
            size=TERM, xlabel="Time",
            footnote=INVENTED + " Bottom line: add the day's volume on a "
                     "higher close,\nsubtract it on a lower one. Part 6 "
                     "names it the OBV.",
        ),
    ),
    ChartArt(
        letter="J",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=J_BARS, ylabel="Price (PHP)", ticks=(45, 50, 55),
                     height=1.9, top=0.22,
                     boxes=(Box(x0=13, x1=J_BREAK - 0.5, lo=J_BOT, hi=J_TOP,
                                label="", tone="quiet"),),
                     strokes=(
                         Stroke(points=((20, J_TOP + 0.9), (55, J_TOP + 0.9)),
                                dashed=True, tone="structure",
                                label="buy stops above the range", at=0,
                                dx=0, dy=9),
                         Stroke(points=((20, J_BOT - 0.9), (55, J_BOT - 0.9)),
                                dashed=True, tone="structure",
                                label="sell stops below", at=1, dx=-4,
                                dy=-9),
                     ),
                     notes=(Note(x=J_BREAK, label="2  Breakout", dx=-80,
                                 dy=22, notice=True),)),
                Pane(columns=J_VOL, ylabel="Volume", height=1.0, top=0.28,
                     picks=(J_BREAK,),
                     strokes=(Stroke(points=((0, J_LOW), (72, J_LOW)),
                                     dashed=True, tone="quiet"),),
                     notes=(Note(x=J_BREAK - 1, label="1  Volume tests\n"
                                 "its lowest level", dx=-110, dy=20),)),
            ),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " Dashed: volume's lowest level.\nThe "
                     "book says a breakout may be up or down; this one is up.",
        ),
    ),
    ChartArt(
        letter="K",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=K_LINE, ylabel="Price (PHP)", ticks=(45, 50, 55),
                     height=1.6, top=0.25, bottom=0.18,
                     notes=(Note(x=K_PEAK, label="1  Turns down", dx=18,
                                 dy=12, notice=True),
                            Note(x=K_TROUGH, label="2  Turns up", dx=18,
                                 dy=-10, notice=True))),
                Pane(columns=K_VOL, ylabel="Volume", height=1.0, top=0.25,
                     strokes=(Stroke(points=((0, K_LOW), (78, K_LOW)),
                                     dashed=True, tone="quiet"),)),
            ),
            guides=(Guide(x=K_PEAK, label="1", notice=True),
                    Guide(x=K_TROUGH, label="2", notice=True)),
            size=TERM, xlabel="Time",
            footnote=INVENTED + " Dashed: the low volume level, drawn by "
                     "eye.",
        ),
    ),
    ChartArt(
        letter="L",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=L_CLOSE, ylabel="Price (PHP)", ticks=(50, 55),
                     height=1.8, top=0.42, bottom=0.55,
                     traces=(Trace(values=L_VWMA, tone="structure",
                                   width=2.4),),
                     notes=(Note(x=L_UPS[1], label="Crosses above:\n"
                                 "potentially bullish", dx=-12, dy=-48,
                                 notice=True),
                            Note(x=L_DOWNS[0], label="Crosses below:\n"
                                 "potentially bearish", dx=-14, dy=40),
                            Note(x=70, y=L_VWMA[70], label="Green: the VWMA",
                                 dx=-10, dy=26, dot=False))),
                Pane(columns=L_VOL, ylabel="Volume", height=0.8, top=0.15),
            ),
            size=TERM, xlabel="Time",
            footnote="Invented. Green: a 10-bar VWMA we computed.\nThe "
                     "book's method is in its Chapter 11.",
        ),
    ),
    ChartArt(
        letter="M",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=L_CLOSE, ylabel="Price (PHP)", ticks=(50, 55),
                     height=1.8, top=0.14, bottom=0.45,
                     traces=(Trace(values=L_VWMA, tone="structure",
                                   width=2.4),),
                     notes=(Note(x=L_DOWNS[0] + 1, y=48.0,
                                 label="Grey: below the\nline, undervalued:\n"
                                 "look to buy", dx=-6, dy=0,
                                 dot=False),
                            Note(x=L_DOWNS[1] - 1, y=48.0,
                                 label="Gold: above the\nline, overvalued:\n"
                                 "look to sell", dx=6, dy=0,
                                 dot=False, notice=True))),
                Pane(columns=L_VOL, ylabel="Volume", height=0.8, top=0.15),
            ),
            spans=(Span(x0=L_DOWNS[0], x1=L_UPS[0] - 1),
                   Span(x0=L_UPS[0], x1=L_DOWNS[1] - 1, tone="notice")),
            size=PAIR, xlabel="Time",
            footnote="Invented. Green: a 10-bar VWMA we computed. Shaded: "
                     "the stretches the labels name.",
        ),
    ),
    ChartArt(
        letter="N",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Top, extreme volume",
                     note="blow-off, or buying climax",
                     panes=(Pane(line=_TOP, height=1.2, top=0.15),
                            Pane(columns=_EXTREME, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
                Cell(name="Bottom, extreme volume",
                     note="sell-off, or selling climax",
                     panes=(Pane(line=_BOTTOM, height=1.2, top=0.15),
                            Pane(columns=_EXTREME, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
                Cell(name="Top, minimal volume", note="low volume top",
                     panes=(Pane(line=_TOP, height=1.2, top=0.15),
                            Pane(columns=_MINIMAL, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
                Cell(name="Bottom, minimal volume", note="low volume bottom",
                     panes=(Pane(line=_BOTTOM, height=1.2, top=0.15),
                            Pane(columns=_MINIMAL, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " The green bar is the volume on the day of "
                     "the turn.",
        ),
    ),
    ChartArt(
        letter="O",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=O_LINE, ylabel="Price (PHP)", ticks=(45, 50, 55, 60),
                     height=1.6, top=0.18, bottom=0.16),
                Pane(columns=O_VOL, ylabel="Volume", height=1.2, top=0.10,
                     picks=(O_TURNS["1"], O_TURNS["2"]),
                     strokes=(
                         Stroke(points=((0, O_UPPER), (99, O_UPPER)),
                                dashed=True, tone="notice",
                                label="upper level", at=0, dx=2, dy=9),
                         Stroke(points=((0, O_LOWER), (99, O_LOWER)),
                                dashed=True, tone="quiet",
                                label="lower level", at=0, dx=2, dy=9),
                     )),
            ),
            guides=tuple(Guide(x=x, label=k, notice=k in "12")
                         for k, x in sorted(O_TURNS.items(),
                                            key=lambda kv: kv[1])),
            size=PAIR, xlabel="Time",
            footnote="Invented. 1 and 2: the major turns. a to c: smaller "
                     "corrections. Levels drawn by eye.",
        ),
    ),
    ChartArt(
        letter="P",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="After a rise", note="a top: overbought,\nin "
                     "retrospect",
                     panes=(Pane(line=_TOP, height=1.2, top=0.15),
                            Pane(columns=_EXTREME, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
                Cell(name="After a fall", note="a bottom: oversold,\nin "
                     "retrospect",
                     panes=(Pane(line=_BOTTOM, height=1.2, top=0.15),
                            Pane(columns=_EXTREME, dims=(0, 1, 2, 4, 5, 6),
                                 height=1.0, top=0.10))),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " The two volume records are identical; only "
                     "price tells them apart.",
        ),
    ),
    ChartArt(
        letter="Q",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Daily volume", note="the tallest bar: one spike, "
                     "late, at 1",
                     panes=(Pane(columns=Q_DAYS, picks=(Q_SPIKE,),
                                 notes=(Note(x=Q_SPIKE, label="1", dx=-14,
                                             dy=-4, dot=False,
                                             notice=True),),
                                 top=0.10),)),
                Cell(name="The same days, added up by month",
                     note="the tallest bar: a busy month, earlier, at 2",
                     panes=(Pane(columns=Q_MONTHS, picks=(Q_BUSIEST,),
                                 tags=((Q_BUSIEST, "2"),
                                       (Q_SPIKE // 20, "the spike's month")),
                                 top=0.22),)),
            ),
            cols=1, size=PAIR,
            footnote="Invented volume: 240 trading days, then twelve months "
                     "of twenty days each.",
        ),
    ),
    ChartArt(
        letter="RA",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _resistance_60("A  9 million at the touch",
                               "the most volume of the move:\nthe most "
                               "reliable",
                               RA_PEAK),
                _resistance_60("B  0.5 million at the touch",
                               "the least volume of the move:\nless "
                               "reliable",
                               RA_DIP),
            ),
            cols=2, size=PAIR,
            footnote="Invented: price, and volume in millions of shares. "
                     "Gold: the bar at the touch.\nThe retest's volume and "
                     "whether PHP 60 holds are not drawn: the book gives "
                     "neither.",
        ),
    ),
    ChartArt(
        letter="R",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _barrier("Increasing, at a resistance",
                         "driven down and away:\nbearish confirmation",
                         (1, 2, 3, 4, 5, 6, 7), side="resistance"),
                _barrier("Increasing, at a support",
                         "driven up and away:\nbullish confirmation",
                         (1, 2, 3, 4, 5, 6, 7), side="support"),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " Volume in millions of shares, invented. "
                     "Gold: the touch.",
        ),
    ),
    ChartArt(
        letter="RB",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _barrier("Decreasing, at a resistance",
                         "price comes back up:\na retest is likely",
                         (7, 6, 5, 4, 3, 2, 1), side="resistance",
                         retest=True),
                _barrier("Decreasing, at a support",
                         "price comes back down:\na retest is likely",
                         (7, 6, 5, 4, 3, 2, 1), side="support",
                         retest=True),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " Volume in millions of shares, invented. "
                     "Gold: the touch.\nThe retests are drawn from the "
                     "book's words, with no volume under them; Figure 6.19 "
                     "draws none.",
        ),
    ),
    ChartArt(
        letter="RC",
        draw=ck.cells,
        kwargs=dict(
            items=(
                _barrier("Peaking", "the most reliable",
                         (1, 2, 4, 7, 4, 2, 1), side="resistance"),
                _barrier("Bottoming", "less reliable",
                         (7, 4, 2, 1, 2, 4, 7), side="resistance"),
                _barrier("Flatlining", "not enough information",
                         (4,) * 7, side="resistance"),
                _barrier("Peaking", "the most reliable",
                         (1, 2, 4, 7, 4, 2, 1), side="support"),
                _barrier("Bottoming", "less reliable",
                         (7, 4, 2, 1, 2, 4, 7), side="support"),
                _barrier("Flatlining", "not enough information",
                         (4,) * 7, side="support"),
            ),
            cols=3, size=PAIR,
            footnote=SKETCH + " Top row at a resistance, bottom row at a "
                     "support. Volume in\nmillions of shares, invented. "
                     "Gold: the touch.",
        ),
    ),
    ChartArt(
        letter="S",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="1  Moving average filter",
                     note="spikes above the average",
                     panes=(Pane(columns=S_MA_VOL, picks=(8, 21),
                                 tags=((8, "3.0"), (21, "2.8")),
                                 traces=(Trace(values=S_MA, tone="deep",
                                               width=2.0),),
                                 notes=(Note(x=13.5, y=S_MA[13],
                                             label="average\nabout 1",
                                             dx=0, dy=30, dot=False),),
                                 top=0.22),)),
                Cell(name="2  Volatility filter",
                     note="only the largest crosses",
                     panes=(Pane(columns=S_BAND_VOL, picks=(17,),
                                 tags=((17, "3.2"), (8, "1.9")),
                                 traces=(Trace(values=S_BAND, tone="deep",
                                               width=2.0),),
                                 top=0.22),)),
                Cell(name="3  Prior volume peaks",
                     note="ours: a level at an earlier peak",
                     panes=(Pane(columns=S_PEAK_VOL, picks=(24,),
                                 tags=((6, "2.6"), (24, "2.6")),
                                 strokes=(Stroke(points=((6, 2.6),
                                                         (29, 2.6)),
                                                 dashed=True,
                                                 tone="structure"),),
                                 top=0.22),)),
                Cell(name="4  Volume cycles", note="peaks that repeat",
                     panes=(Pane(columns=S_CYCLE_VOL, picks=S_CYCLE_PEAKS,
                                 top=0.15),)),
            ),
            cols=2, size=PAIR,
            footnote="Invented volume, in millions of shares. Gold: the "
                     "volume each filter keeps.\nPanels 1 and 2 are worked "
                     "in numbers next. Panel 3 is our reading.",
        ),
    ),
    ChartArt(
        letter="SA",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Filter 1: the average of the last 8 bars",
                     note="kept, by our rule: over twice the average",
                     panes=(Pane(columns=S_MA_VOL, picks=(8, 21),
                                 tags=((4, "1.4"), (8, "3.0"), (21, "2.8")),
                                 traces=(Trace(values=S_MA, tone="deep",
                                               width=2.0),
                                         Trace(values=S_TWICE,
                                               tone="notice", width=2.4,
                                               dotted=True)),
                                 notes=(Note(x=11, y=S_MA[11],
                                             label="average", dx=0, dy=12,
                                             dot=False),
                                        Note(x=15, y=S_TWICE[15],
                                             label="twice the average",
                                             dx=0, dy=34, dot=False)),
                                 top=0.75),)),
                Cell(name="Filter 2: a higher line",
                     note="kept: only the bar that crosses it",
                     panes=(Pane(columns=S_BAND_VOL, picks=(17,),
                                 tags=((8, "1.9"), (17, "3.2")),
                                 traces=(Trace(values=S_BAND, tone="deep",
                                               width=2.0),),
                                 top=0.22),)),
            ),
            cols=1, size=PAIR,
            footnote="Invented volume, in millions of shares. Filter 2's "
                     "line is the average plus a fixed 1.6,\na stand-in: "
                     "its real line is computed on the sigma filter's "
                     "slides.",
        ),
    ),
    ChartArt(
        letter="T",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=T_LINE, ylabel="Price (PHP)", ticks=(50, 55),
                     height=1.5, top=0.12, bottom=0.10),
                Pane(columns=T_VOL, picks=T_TURNS, ylabel="Volume",
                     height=1.2, top=0.10,
                     traces=(Trace(values=T_MA, tone="deep", width=2.4),),
                     notes=(Note(x=42, y=T_MA[42], label="20-bar\naverage",
                                 dx=8, dy=34, dot=False),)),
            ),
            guides=tuple(Guide(x=x, label=str(i + 1), notice=True)
                         for i, x in enumerate(T_TURNS)),
            size=TERM, xlabel="Time",
            footnote="Invented. Line: the average of the last 20 volume "
                     "bars,\ncomputed. Gold: four spikes.",
        ),
    ),
    ChartArt(
        letter="U",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(columns=U_VOL, picks=U_PICKS, ylabel="Volume",
                     height=1.0, top=0.12,
                     traces=(Trace(values=U_MA, tone="deep", width=2.0),
                             Trace(values=U_BAND, tone="structure",
                                   width=2.0, dotted=True)),
                     notes=(Note(x=30, y=U_BAND[30], label="3-sigma line: "
                                 "average plus 3\nstandard deviations", dx=6,
                                 dy=34, dot=False),
                            Note(x=64, y=U_MA[64], label="20-bar\naverage",
                                 dx=6, dy=26, dot=False))),
            ),
            size=TERM, xlabel="Time",
            footnote="Invented volume. Both lines are computed over the "
                     "last 20 bars.\nGold: the bars above the 3-sigma line. The "
                     "dotted line jumps when\na spike enters the last 20 "
                     "bars, and falls back 20 bars later.",
        ),
    ),
    ChartArt(
        letter="V",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=V_LINE, ylabel="Price (PHP)",
                     ticks=(46, 50, 54),
                     height=1.8, top=0.22, bottom=0.12,
                     notes=(Note(x=V_POINTS["1"], label="1  PHP 52.00",
                                 dx=-12, dy=-18, notice=True),
                            Note(x=V_POINTS["2"], label="2  PHP 56.00",
                                 dx=-30, dy=8, notice=True),
                            Note(x=V_POINTS["3"], label="3  PHP 49.00",
                                 dx=-10, dy=-24, notice=True))
                     + tuple(Note(x=x, label="", dx=0.1, dy=0.1, dot=True)
                             for x in V_SKIPPED + (V_X,))),
                Pane(columns=V_VOL, ylabel="Volume (m)", ticks=(1, 2, 3),
                     height=1.1, top=0.28,
                     picks=tuple(V_POINTS.values()),
                     dims=V_SKIPPED + (V_X,),
                     tags=tuple((x, "3.0") for x in V_POINTS.values()),
                     strokes=(Stroke(points=((0, V_THRESHOLD),
                                             (84, V_THRESHOLD)),
                                     dashed=True, tone="quiet",
                                     label="threshold, by eye: 2.5", at=1,
                                     dx=-4, dy=-12),
                              Stroke(points=((0, V_AVERAGE),
                                             (84, V_AVERAGE)),
                                     tone="quiet", width=1.0,
                                     label="average: 1.3", at=1, dx=-58,
                                     dy=-14))),
            ),
            size=TERM, xlabel="Time",
            footnote="Invented, ours; volume in millions. Gold: turns on "
                     "3.0, kept.\nGrey: turns on 1.0, below the average, "
                     "dropped.",
        ),
    ),
    ChartArt(
        letter="VA",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=V_LINE, ylabel="Price (PHP)",
                     ticks=(46, 50, 54, 58),
                     height=1.9, top=0.10, bottom=0.26,
                     strokes=(
                         Stroke(points=((V_POINTS["1"],
                                         _v_top(V_POINTS["1"])),
                                        (84, _v_top(84))), tone="structure",
                                width=1.8),
                         Stroke(points=((V_POINTS["3"] - 6,
                                         _v_bottom(V_POINTS["3"] - 6)),
                                        (84, _v_bottom(84))),
                                tone="structure", width=1.8, dashed=True),
                         Stroke(points=((V_POINTS["1"], 52.0),
                                        (V_POINTS["2"], 52.0)),
                                tone="quiet", width=1.0, dashed=True),
                     ),
                     brackets=(Bracket(x=V_POINTS["2"] + 1, lo=52.0,
                                       hi=56.0, label="+4.00\nin 40 bars"),),
                     notes=(Note(x=V_POINTS["1"], label="1  bar 22\nPHP 52.00",
                                 dx=-12, dy=16, notice=True),
                            Note(x=V_POINTS["2"], label="2  bar 62, PHP 56.00",
                                 dx=-30, dy=8, notice=True),
                            Note(x=V_POINTS["3"], label="3  bar 44, PHP 49.00",
                                 dx=-10, dy=-26, notice=True),
                            Note(x=V_X, label="X  bar 72, PHP 51.80",
                                 dx=-4, dy=-52))
                     + tuple(Note(x=x, label="", dx=0.1, dy=0.1, dot=True)
                             for x in V_SKIPPED)),
                Pane(columns=V_VOL, ylabel="Volume (m)", ticks=(1, 3),
                     height=0.9, top=0.20,
                     picks=tuple(V_POINTS.values()),
                     dims=V_SKIPPED + (V_X,),
                     strokes=(Stroke(points=((0, V_THRESHOLD),
                                             (84, V_THRESHOLD)),
                                     dashed=True, tone="quiet",
                                     label="threshold 2.5", at=1, dx=-4,
                                     dy=-12),)),
            ),
            size=PAIR, xlabel="Bar",
            xticks=tuple((x, str(x)) for x in (0, 20, 40, 60, 80)),
            footnote="Invented, ours. Solid: trendline through peaks 1 "
                     "and 2.\nDashed: its parallel through trough 3.",
        ),
    ),
    ChartArt(
        letter="W",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=W_LINE, ylabel="Price (PHP)", ticks=(40, 45, 50, 55),
                     height=1.7, top=0.20,
                     notes=(Note(x=50, label="The trend persists ...",
                                 dx=-30, dy=40, notice=True),)),
                Pane(columns=W_VOL, ylabel="Volume", height=1.0, top=0.80,
                     notes=(Note(x=50, y=2.2, label="... on flat volume:\n"
                                 "every bar about 2 million",
                                 dx=-30, dy=26, dot=False),)),
            ),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " No change in volume, so relative volume "
                     "says nothing new.",
        ),
    ),
    ChartArt(
        letter="X",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=X_LINE, ylabel="Price (PHP)", ticks=(40, 45, 50),
                     height=1.7, top=0.20, bottom=0.12,
                     strokes=(Stroke(points=((0, 50.0), (60, 50.0)),
                                     dashed=True, tone="notice",
                                     label="Bought here, PHP 50", at=1,
                                     dx=-4, dy=10),),
                     notes=(Note(x=60, label="PHP 38: still holding,\n"
                                 "waiting for PHP 50", dx=-60, dy=-4),)),
                Pane(columns=X_VOL, ylabel="Volume", height=1.0, top=0.45,
                     notes=(Note(x=48, label="Holders who will not\nsell "
                                 "add no volume", dx=-30, dy=30),)),
            ),
            size=TERM, xlabel="Time",
            footnote=INVENTED + " One holder's story; the pesos are ours.",
        ),
    ),
    ChartArt(
        letter="Y",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=Y_LINE, ylabel="Price (PHP)", ticks=(40, 45, 50, 55),
                     height=1.7, top=0.12),
                Pane(columns=Y_VOL, ylabel="Volume", height=1.0, top=0.15),
            ),
            spans=(Span(x0=0, x1=40, label="Bull market volume:\nabout "
                        "2.8 million a day"),
                   Span(x0=41, x1=80, label="Bear market volume:\nabout "
                        "1.3 million a day", tone="notice")),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " The book gives three reasons; the chart "
                     "shows only the result.",
        ),
    ),
    ChartArt(
        letter="Z",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(columns=(5.0, 1.0), name="Shares traded a day",
                     tags=((0, "5 million"), (1, "1 million")), top=0.65),
                Pane(columns=(0.25, 2.5), picks=(1,),
                     name="Turnover: traded / outstanding",
                     tags=((0, "0.25%"), (1, "2.5%")), top=0.65),
            ),
            xticks=((0, "Share A: 2,000 million\nshares outstanding"),
                    (1, "Share B: 40 million\nshares outstanding")),
            size=PAIR, xlabel="",
            footnote="Our example: two invented shares.",
        ),
    ),
    ChartArt(
        letter="AA",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(columns=(1, 3, 3, 1), picks=(2,), ylabel="Open contracts",
                     ticks=(0, 1, 2, 3), top=0.30,
                     tags=((0, "1"), (1, "3"), (2, "3"), (3, "1"))),
            ),
            xticks=((0, "Day 1\nnew: +1"), (1, "Day 2\nnew: +2"),
                    (2, "Day 3\nreplaced: 0"), (3, "Day 4\nexit: -2")),
            size=TERM, xlabel="",
            footnote="Our example: traders A to E, one contract market.",
        ),
    ),
    ChartArt(
        letter="AB",
        draw=ck.cells,
        kwargs=dict(
            items=tuple(
                Cell(name=name, note=note, panes=(Pane(strokes=tuple(
                    Stroke(points=((3, base + (0 if up else 1)),
                                   (8, base + (1 if up else 0))),
                           arrow=True, width=2.2,
                           tone="notice" if label == "price" else "structure",
                           label=label, at=0, dx=-6, dy=0)
                    for label, base, up in (("price", 6, ups[0]),
                                            ("volume", 3, ups[1]),
                                            ("open interest", 0, ups[2]))),
                    top=0.05, bottom=0.05),))
                for name, note, ups in (
                    ("All three rising", "bullish: buying pressure",
                     (True, True, True)),
                    ("Price up, the other two down",
                     "bearish: shorts covering, longs leaving",
                     (True, False, False)),
                    ("Price down, the other two up",
                     "bearish: short selling", (False, True, True)),
                    ("All three falling",
                     "bullish: the selling drying up",
                     (False, False, False)),
                )),
            cols=2, size=PAIR,
            footnote=SKETCH + " Each arrow is the direction of one series.",
        ),
    ),
    ChartArt(
        letter="AC",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Open interest very high",
                     note="the reversal is rapid",
                     panes=(Pane(line=(1.0, 2.0, 3.0, 3.6, 3.0, 1.2, -0.6,
                                       -2.4), height=1.4, top=0.10),
                            Pane(columns=(80, 82, 85, 86, 84, 70, 50, 35),
                                 name="open interest: about 85,000",
                                 top=0.25))),
                Cell(name="Open interest low", note="the reversal is gradual",
                     panes=(Pane(line=(1.0, 2.0, 3.0, 3.6, 3.3, 3.0, 2.7,
                                       2.4), height=1.4, top=0.10,
                                 # An invisible point, so both price
                                 # sketches share one scale.
                                 strokes=(Stroke(points=((0, -2.4),
                                                         (0, -2.4)),
                                                 width=0.0),)),
                            Pane(columns=(20, 21, 22, 22, 21, 20, 19, 18),
                                 name="open interest: about 20,000",
                                 top=3.3))),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " The open interest panels share one scale. "
                     "The book says may: a tendency.",
        ),
    ),
    ChartArt(
        letter="AD",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Volume: by size",
                     note="adds to 2.4 million shares",
                     panes=(Pane(columns=(0.1, 0.6, 0.3, 1.2, 0.2),
                                 tags=((0, "0.1"), (1, "0.6"), (2, "0.3"),
                                       (3, "1.2"), (4, "0.2")), top=0.25),)),
                Cell(name="Tick volume: by number",
                     note="1 + 1 + 1 + 1 + 1 = 5 trades", tone="notice",
                     panes=(Pane(columns=(1, 1, 1, 1, 1),
                                 tags=tuple((i, "1") for i in range(5)),
                                 top=3.8),)),
            ),
            cols=2, size=TERM,
            footnote="Our example: Part 1's five trades, counted two ways.",
        ),
    ),
    ChartArt(
        letter="AE",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Advances / declines", note="1,500 / 1,000 = 1.5",
                     panes=(Pane(columns=(1500, 1000),
                                 tags=((0, "1,500"), (1, "1,000")),
                                 top=0.30),)),
                Cell(name="Up / down volume", note="600m / 800m = 0.75",
                     panes=(Pane(columns=(600, 800),
                                 tags=((0, "600m"), (1, "800m")),
                                 top=0.30),)),
                Cell(name="TRIN", note="1.5 / 0.75 = 2.0", tone="notice",
                     panes=(Pane(columns=(1.5, 0.75, 2.0), picks=(2,),
                                 tags=((0, "1.5"), (1, "0.75"), (2, "2.0")),
                                 top=0.30),)),
            ),
            cols=3, size=TERM,
            footnote="Our example: invented counts and volumes.",
        ),
    ),
    ChartArt(
        letter="AF",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AF_LINE, profile=AF_PROFILE, profile_reach=0.45,
                     profile_labels=AF_LABELS,
                     ylabel="Price (PHP)", ticks=(48, 52, 56, 60),
                     height=1.8, top=0.10, bottom=0.04,
                     ),
                Pane(columns=AF_VOL, ylabel="Volume", height=0.9, top=0.55,
                     notes=(Note(x=62, label="Volume by time:\none bar a "
                                 "day", dx=8, dy=30, dot=False),)),
            ),
            size=TERM, xlabel="Time",
            footnote="Invented, million shares, 100 days. Sideways bars, volume "
                     "by price: the\nvolume of the days that closed in each "
                     "PHP 2 band.",
        ),
    ),
    ChartArt(
        letter="AG",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AF_LINE, profile=AF_PROFILE,
                     profile_picks=(AF_BIG,), profile_reach=0.30,
                     ylabel="Price (PHP)", ticks=(48, 52, 56, 60),
                     height=1.9, top=0.10, bottom=0.06,
                     boxes=tuple(Box(x0=a, x1=b, lo=AG_LO, hi=AG_HI,
                                     tone="notice") for a, b in AG_SPANS),
                     strokes=(
                         Stroke(points=((AG_PEAK - 30, AG_RES),
                                        (99, AG_RES)), tone="structure",
                                label=f"4  Resistance, PHP {AG_RES:.2f}",
                                at=1, dx=-2, dy=9, width=1.8),
                         Stroke(points=((AG_TROUGH - 30, AG_SUP),
                                        (99, AG_SUP)), tone="structure",
                                label=f"4  Support, PHP {AG_SUP:.2f}",
                                at=1, dx=-2, dy=-9, width=1.8),
                     ),
                     profile_labels=tuple(label if i == AF_BIG else ""
                                          for i, label in
                                          enumerate(AF_LABELS)),
                     notes=(Note(x=6, y=(AG_LO + AG_HI) / 2, label="1",
                                 dx=-1, dy=24, dot=False, notice=True),
                            Note(x=AG_SPANS[0][0] - 2, y=AG_HI, label="3",
                                 dx=-4, dy=16, dot=False, notice=True),
                            Note(x=AG_SPANS[1][0] - 1, y=AG_HI, label="3",
                                 dx=-4, dy=16, dot=False, notice=True))),
                Pane(columns=AF_VOL, ylabel="Volume", height=0.9, top=0.30,
                     picks=tuple(range(26, 31)) + tuple(range(46, 50))),
            ),
            spans=tuple(Span(x0=a, x1=b, label="2", tone="notice")
                        for a, b in AG_SPANS),
            size=PAIR, xlabel="Time",
            footnote="Invented. 1, 2 and 3 are the book's first three "
                     "steps; 4 is the two levels.",
        ),
    ),
    ChartArt(
        letter="AH",
        draw=ck.cells,
        kwargs=dict(
            items=tuple(
                Cell(name=name, note=note, panes=(
                    Pane(bars=_trend_bars(rng_last), height=1.3, top=0.12,
                         boxes=(Box(x0=6.55, x1=7.45,
                                    lo=_trend_bars(rng_last)[7].low - 0.15,
                                    hi=_trend_bars(rng_last)[7].high + 0.15,
                                    tone="notice"),)),
                    Pane(columns=(2.0, 2.1, 1.9, 2.0, 2.2, 1.9, 2.0, vol),
                         picks=(7,), height=1.0, top=0.10)))
                for name, note, rng_last, vol in (
                    ("Low Volume Rest Bar", "narrow range, low volume",
                     0.25, 0.7),
                    ("High Volume Reversal Bar", "narrow range, high volume",
                     0.25, 4.2),
                    ("Low Volume Reversal Bar", "wide range, low volume",
                     3.2, 0.7),
                    ("High Volume Continuation Bar",
                     "wide range, high volume", 3.2, 4.2),
                )),
            cols=2, size=TERM,
            footnote=SKETCH + " Seven ordinary bars, then the named one, "
                     "boxed in gold.",
        ),
    ),
    ChartArt(
        letter="AI",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="High Volume Reversal Bar",
                     note="narrow range on heavy volume, then down",
                     panes=(Pane(bars=AI_NARROW, height=1.3, top=0.12,
                                 boxes=(_box(AI_NARROW, 7),)),
                            Pane(columns=AI_VOL_HIGH, picks=(7,),
                                 height=1.0, top=0.10))),
                Cell(name="Low Volume Reversal Bar",
                     note="a long bar on light volume, then down",
                     panes=(Pane(bars=AI_WIDE, height=1.3, top=0.12,
                                 boxes=(_box(AI_WIDE, 7),)),
                            Pane(columns=AI_VOL_LOW, picks=(7,), height=1.0,
                                 top=0.10))),
            ),
            cols=2, size=PAIR,
            footnote=SKETCH + " The named bar is boxed; its volume is gold.",
        ),
    ),
    ChartArt(
        letter="AJ",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Rest bar,\nstrong rapid trend",
                     note="a potential reversal",
                     panes=(Pane(bars=AJ_FAST, height=1.3, top=0.12,
                                 boxes=(_box(AJ_FAST, 6),)),
                            Pane(columns=AJ_VOL_REST_FAST, picks=(6,),
                                 height=1.0, top=0.10))),
                Cell(name="Rest bar,\nweak or average trend",
                     note="a point of rest",
                     panes=(Pane(bars=AJ_SLOW, height=1.3, top=0.12,
                                 boxes=(_box(AJ_SLOW, 6),)),
                            Pane(columns=AJ_VOL_REST_SLOW, picks=(6,),
                                 height=1.0, top=0.10))),
                Cell(name="Continuation bar,\nany trend",
                     note="the move continues",
                     panes=(Pane(bars=AJ_CONT, height=1.3, top=0.12,
                                 boxes=(_box(AJ_CONT, 6),)),
                            Pane(columns=AJ_VOL_CONT, picks=(6,),
                                 height=1.0, top=0.10))),
            ),
            cols=3, size=PAIR,
            footnote=SKETCH + " The named bar is boxed; its volume is gold.",
        ),
    ),
    ChartArt(
        letter="AK",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AK_LINE, ylabel="Price (PHP)", ticks=(50, 55, 60),
                     height=1.7, top=0.15, bottom=0.10,
                     strokes=(Stroke(points=((8, AK_TL(8)), (60, AK_TL(60))),
                                     tone="structure", width=1.8,
                                     label="trendline", at=0, dx=4,
                                     dy=10),),
                     notes=(Note(x=AK_BREAK, label="1  A small breakout",
                                 dx=-20, dy=-34, notice=True),)),
                Pane(columns=AK_VOL, ylabel="Volume", height=1.0, top=0.35,
                     picks=tuple(range(52, 65)),
                     notes=(Note(x=AK_BREAK, label="ordinary volume",
                                 dx=-30, dy=26),
                            Note(x=56, label="2  Then the volume", dx=-20,
                                 dy=16, notice=True))),
            ),
            size=PAIR, xlabel="Time",
            footnote=INVENTED + " Price breaks the line first; the volume "
                     "comes after.",
        ),
    ),
    ChartArt(
        letter="AL",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=AL_BARS, ylabel="Price", height=1.6, top=0.20,
                     bottom=0.10,
                     notes=(Note(x=14, label="1  Reverses", dx=40, dy=0,
                                 notice=True),
                            Note(x=38, label="2  Continues", dx=-20, dy=30,
                                 notice=True),
                            Note(x=62, label="3  Reverses", dx=-8, dy=-34,
                                 notice=True))),
                Pane(columns=AL_VOL, ylabel="Volume", height=1.0, top=0.15),
            ),
            spans=tuple(Span(x0=d * 24 + 13, x1=d * 24 + 14.6, tone="notice")
                        for d in range(3)),
            xticks=((0, "Day 1"), (13.8, "13:30 to\n14:30 GMT"),
                    (24, "Day 2"), (48, "Day 3")),
            size=TERM, xlabel="",
            footnote=INVENTED + " Hourly bars.\nGold: the peak hours, "
                     "13:30 to 14:30 GMT.",
        ),
    ),
    ChartArt(
        letter="FA",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=FA_LINE, name="Price", height=1.3, top=0.60,
                     bottom=0.45,
                     strokes=(Stroke(points=((14, 54.4), (34, 56.4)),
                                     arrow=True, label="A  higher peak",
                                     at=0, dx=-6, dy=10),),
                     notes=(Note(x=48, label="then falls", dx=-30, dy=-10,
                                 dot=False),)),
                Pane(line=FA_OSC, name="Oscillator", height=1.5, top=0.45,
                     bottom=0.30,
                     strokes=(Stroke(points=((14, 0.98), (34, 0.63)),
                                     arrow=True, label="A  lower peak",
                                     at=0, dx=10, dy=12),
                              Stroke(points=((2, FA_RISE(2)),
                                             (40, FA_RISE(40)))),
                              Stroke(points=((0, FA_FLOOR), (56, FA_FLOOR)),
                                     dashed=True, tone="quiet",
                                     label="C  oversold level", at=0,
                                     dx=2, dy=-16)),
                     notes=(Note(x=24, y=FA_RISE(24), label="B  rising line",
                                 dx=4, dy=-22, dot=False),
                            Note(x=FA_BREAK, label="B  falls through",
                                 dx=22, dy=10, notice=True),)),
            ),
            size=ck.pair_size(7.5), xlabel="Time",
            footnote="Invented price and oscillator. A, B and C: the three "
                     "readings\nPart 6 uses, as the slide lists them.",
        ),
    ),
    ChartArt(
        letter="AM",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AM_CLOSE, name="Close (PHP)", height=1.0, top=0.80,
                     bottom=0.25,
                     tags=tuple((i, f"{c:.2f}") for i, c in
                                enumerate(AM_CLOSE))),
                Pane(columns=AM_SIGNED, name="Volume, signed by the close",
                     height=1.1, top=0.70, bottom=0.30, zero=True,
                     tags=tuple((i, t) for i, t in enumerate(AM_SIGNS))),
                Pane(line=AM_OBV, name="OBV, the running total",
                     height=1.0, top=0.80, bottom=0.25, picks=(),
                     tags=tuple((i, f"{v:.1f}") for i, v in
                                enumerate(AM_OBV))),
            ),
            xticks=tuple((i, f"Day {i + 1}") for i in range(6)),
            size=TERM, xlabel="",
            footnote="Our example, in million shares. Day 4's close is "
                     "unchanged, so nothing is added.",
        ),
    ),
    ChartArt(
        letter="AN",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AM_OBV,
                     name="OBV, black: started day 1. Gold: started day 3.",
                     top=0.35, bottom=0.30,
                     tags=((0, "0"), (2, "0.5"), (5, "2.5")),
                     strokes=(Stroke(points=AN_LATE, tone="notice",
                                     width=2.4),),
                     notes=(Note(x=2, y=0.0, label="0", dx=-14, dy=-12),
                            Note(x=5, y=2.0, label="2.0", dx=-6, dy=-18))),
            ),
            xticks=tuple((i, f"Day {i + 1}") for i in range(6)),
            size=PAIR, xlabel="",
            footnote="Our example, in million shares. From day 3 to day 6 "
                     "both lines\nrise by 2.0: 0.5 to 2.5, and 0 to 2.0.",
        ),
    ),
    ChartArt(
        letter="FC",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=FC_BARS, name="Two bars (PHP)", height=1.5,
                     top=0.25, bottom=0.10,
                     notes=(Note(x=0, y=51.0, label="high 51.00", dx=-14,
                                 dy=10, dot=False),
                            Note(x=0, y=50.8, label="close 50.80", dx=14,
                                 dy=-14, dot=False),
                            Note(x=1, y=54.0, label="new high 54.00",
                                 dx=-20, dy=4, dot=False),
                            Note(x=1, y=50.7, label="close 50.70",
                                 dx=16, dy=-10, dot=False, notice=True))),
                Pane(columns=(2.0, -3.0), picks=(1,), zero=True,
                     name="OBV: volume, signed by the close", height=1.1,
                     top=1.10, bottom=0.30,
                     tags=((0, "+2.0"), (1, "-3.0"))),
            ),
            xticks=((0, "Bar 1"), (1, "Bar 2")),
            size=PAIR, xlabel="",
            footnote="Our example, in million shares. Bar 1 closed above the "
                     "bar before it.\nBar 2 closed lower, so its whole 3.0 "
                     "million is taken away.",
        ),
    ),
    ChartArt(
        letter="AO",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(bars=AO_BARS, ylabel="Bar (PHP)", ticks=(48, 50, 52),
                     height=1.4, top=0.15, bottom=0.10,
                     notes=(Note(x=0, label="factor 1", dx=14, dy=-8,
                                 dot=False),
                            Note(x=1, label="factor 0", dx=14, dy=0,
                                 dot=False),
                            Note(x=2, label="factor -0.5", dx=14, dy=0,
                                 dot=False))),
                Pane(columns=(2.0, 0.0, -1.0), zero=True,
                     ylabel="x volume", height=1.0, top=0.45,
                     bottom=0.35,
                     tags=((0, "+2.0"), (1, "0"), (2, "-1.0"))),
                Pane(line=(2.0, 2.0, 1.0), ylabel="ADL",
                     height=1.0, top=0.60, bottom=0.30,
                     tags=((0, "2.0"), (1, "2.0"), (2, "1.0"))),
            ),
            xticks=((0, "Close 52,\nthe high"), (1, "Close 50,\nthe middle"),
                    (2, "Close 49")),
            size=TERM, xlabel="",
            footnote="Our example: each bar from PHP 48 to PHP 52 on 2 "
                     "million shares.",
        ),
    ),
    ChartArt(
        letter="AP",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=tuple(round(-1 + 0.2 * i, 2) for i in range(11)),
                     ylabel="Multiplying factor", ticks=(-1, 0, 1), zero=True,
                     top=0.25, bottom=0.25,
                     notes=(Note(x=0, label="-1: subtract all\nthe volume",
                                 dx=14, dy=-6, notice=True),
                            Note(x=5, label="0: nothing", dx=14, dy=-14),
                            Note(x=10, label="+1: add all\nthe volume",
                                 dx=-14, dy=6, notice=True))),
            ),
            xticks=((0, "the low"), (5, "the midpoint"), (10, "the high")),
            size=PAIR, xlabel="Where the bar closes in its range",
            footnote="Not prices: the factor [(C - L) - (H - C)] / (H - L), "
                     "for every close from low to high.",
        ),
    ),
    ChartArt(
        letter="AQ",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Signed volume, S", note="2.0 + 0 - 1.0 = 1.0",
                     panes=(Pane(columns=(2.0, 0.0, -1.0), zero=True,
                                 tags=((0, "2.0"), (1, "0"), (2, "-1.0")),
                                 top=0.25, bottom=0.25),)),
                Cell(name="Volume", note="2.0 + 2.0 + 2.0 = 6.0",
                     panes=(Pane(columns=(2.0, 2.0, 2.0),
                                 tags=((0, "2.0"), (1, "2.0"), (2, "2.0")),
                                 top=0.25),)),
                Cell(name="CMF", note="1.0 / 6.0 = 0.17", tone="notice",
                     panes=(Pane(columns=(1.0, 6.0, 0.17), picks=(2,),
                                 tags=((0, "1.0"), (1, "6.0"),
                                       (2, "0.17")), top=0.25),)),
            ),
            cols=3, size=TERM,
            footnote="Our example: the ADL's three bars, closing at 52, 50 "
                     "and 49,\neach on 2.0 million shares.",
        ),
    ),
    ChartArt(
        letter="FD",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=FD_TOTAL, name="Running total of the CMF, black",
                     height=1.4, top=0.35, bottom=0.10,
                     traces=(Trace(values=FD_FAST, tone="notice"),
                             Trace(values=FD_SLOW, tone="structure")),
                     notes=(Note(x=FD_UP, y=FD_FAST[FD_UP],
                                 label="3-bar EMA, gold: 1.0", dx=-60,
                                 dy=14),
                            Note(x=FD_UP, y=FD_SLOW[FD_UP],
                                 label="10-bar EMA, green: 0.5", dx=10,
                                 dy=-22))),
                Pane(columns=FD_OSC, picks=(FD_UP, FD_DOWN), zero=True,
                     name="Oscillator: 3-bar EMA less 10-bar EMA",
                     height=1.1, top=0.90, bottom=0.30,
                     tags=((FD_UP, "+0.5"), (FD_DOWN, "-0.2"))),
            ),
            guides=(Guide(x=FD_UP), Guide(x=FD_DOWN)),
            size=ck.pair_size(6.6), xlabel="Bars",
            footnote="Invented CMF values. Our EMA weights each new value "
                     "2 / (n + 1);\nthe chapter does not give its formula. "
                     "Dashed lines: 1.0 - 0.5, then 0.6 - 0.8.",
        ),
    ),
    ChartArt(
        letter="FB",
        draw=ck.cells,
        kwargs=dict(
            items=(
                Cell(name="Volume, million shares",
                     note="rising stocks 600, falling 400",
                     panes=(Pane(columns=(600, 400),
                                 tags=((0, "600 up"), (1, "400 down")),
                                 top=0.30),)),
                Cell(name="Up/Down Volume", note="600 / 400 = 1.5",
                     tone="notice",
                     panes=(Pane(columns=(1.0, 1.5), picks=(1,),
                                 tags=((0, "1 = even"), (1, "1.5")),
                                 top=0.30),)),
            ),
            cols=2, size=TERM,
            footnote="Our example: one invented day. Above 1, more volume "
                     "went into\nthe stocks that rose than the stocks that "
                     "fell.",
        ),
    ),
    ChartArt(
        letter="AR",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                Pane(line=AR_LINE, ylabel="Price", height=1.5, top=0.15,
                     notes=(Note(x=56, label="A top", dx=-30, dy=12),)),
                Pane(line=AR_OI, ylabel="Open interest", height=1.3,
                     top=0.35, bottom=0.75,
                     strokes=(Stroke(points=((18, AR_LEVEL), (64, AR_LEVEL)),
                                     dashed=True, tone="quiet",
                                     label="its earlier peak, 92,000", at=0,
                                     dx=2, dy=10),),
                     notes=(Note(x=55, label="back to 92,000: a test of\na "
                                 "historical open interest level", dx=-40,
                                 dy=-62, notice=True),)),
            ),
            size=TERM, xlabel="Time, weekly",
            footnote="Invented prices and open interest, in contracts.\nThe "
                     "COT report gives the positions behind this open "
                     "interest.",
        ),
    ),
)
