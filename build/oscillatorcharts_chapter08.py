"""Chapter 8 charts that draw an oscillator under or beside a price path.

Painters for the 'paint' form of ``chartlayout_chapter07``: each draws in
inches from the chart's bottom left corner on a ``shapecharts_chapter07``
Canvas and registers the targets its marks sit on. Every value is ours,
invented for teaching, and printed on the chart.
"""
from __future__ import annotations

import chartkit as ck
from shapecharts_chapter07 import Panel

MUTED, GREEN_DEEP, INK = ck.MUTED, ck.GREEN_DEEP, ck.INK

# One bounded oscillator of ours, twelve readings, and its signal line: the
# simple moving average of its last three readings (ours, as the book says
# only that a signal line is a moving average of the oscillator, p. 246).
OSC = (38, 34, 31, 36, 44, 53, 61, 66, 63, 55, 47, 41)


def signal_line(values=OSC, n=3):
    return tuple(None if i < n - 1 else sum(values[i - n + 1:i + 1]) / n
                 for i in range(len(values)))


def _oscillator_panel(c, *, x0=1.25, x1=10.6, y0=.75, y1=3.2):
    panel = Panel(c, x0, x1, y0, y1, 0, 100, len(OSC))
    for level, words in ((100, '100'), (50, '50 (equilibrium)'), (0, '0')):
        y = panel.y(level)
        c.stroke((panel.x(0) - .2, panel.x(len(OSC) - 1) + .2), (y, y),
                 color=MUTED, lw=1.4, dashed=(level == 50))
    c.text(panel.x(0) - .3, panel.y(100), '100', ha='right')
    c.text(panel.x(0) - .3, panel.y(50), '50', ha='right')
    c.text(panel.x(0) - .3, panel.y(0), '0', ha='right')
    return panel


def _line(c, panel, values, *, color=INK, lw=2.8):
    pts = [(i, v) for i, v in enumerate(values) if v is not None]
    return panel.path(pts, color=color, lw=lw)


def _cross(a0, a1, b0, b1):
    """Where two straight segments between readings meet, as a fraction."""
    return (b0 - a0) / ((a1 - a0) - (b1 - b0))


UNBOUNDED = (-1.2, -0.4, 0.6, 1.4, 0.9, -0.3, -1.1, -0.8)


def paint_equilibrium_crossing(c):
    """A bounded oscillator against its 50 level, and an unbounded one against zero."""
    panel = _oscillator_panel(c, x0=1.0, x1=5.6)
    _line(c, panel, OSC)
    c.text(panel.x(0), panel.y(88), 'bounded: 0 to 100', ha='left', color=GREEN_DEEP)
    # Readings either side of each crossing, written on the chart.
    for i, dx, dy in ((4, 0, -.26), (5, -.12, .28), (9, 0, .28), (10, .12, -.28)):
        c.text(panel.x(i) + dx, panel.y(OSC[i]) + dy, str(OSC[i]), color=INK)
    # Up through 50 between readings 4 and 5, down through it between 9 and 10.
    for index, (i, word, wx, wy, ha) in enumerate(((4, 'crosses\nabove 50', -.35, .5, 'right'),
                                                   (9, 'crosses\nbelow 50', .7, -.45, 'left'))):
        a, b = OSC[i], OSC[i + 1]
        t = (50 - a) / (b - a)
        x = panel.x(i) + t * (panel.x(i + 1) - panel.x(i))
        c.point((0, index + 1, 'cross'), x, panel.y(50))
        c.text(x + wx, panel.y(50) + wy, word, ha=ha, color=GREEN_DEEP)
    # The unbounded one: no top or bottom, so its equilibrium is zero.
    right = Panel(c, 7.0, 10.9, .75, 3.2, -1.6, 1.8, len(UNBOUNDED))
    zero = right.y(0)
    c.stroke((right.x(0) - .2, right.x(len(UNBOUNDED) - 1) + .2), (zero, zero), color=MUTED, lw=1.4, dashed=True)
    c.text(right.x(0) - .3, zero, '0', ha='right')
    right.path(list(enumerate(UNBOUNDED)), color=INK, lw=2.8)
    c.text(right.x(0), 3.5, 'unbounded: no top or bottom', ha='left', color=GREEN_DEEP)
    for i, dx, dy in ((1, .35, -.2), (2, -.25, .28), (4, 0, .3), (5, .45, 0)):
        c.text(right.x(i) + dx, right.y(UNBOUNDED[i]) + dy, f'{UNBOUNDED[i]:g}', color=INK)
    for index, i in enumerate((1, 4), 3):
        a, b = UNBOUNDED[i], UNBOUNDED[i + 1]
        t = (0 - a) / (b - a)
        x = right.x(i) + t * (right.x(i + 1) - right.x(i))
        c.point((0, index, 'cross'), x, zero)
        if index == 3:
            c.text(x - .3, zero + .5, 'crosses\nabove zero', ha='right', color=GREEN_DEEP)
        else:
            c.text(x - .15, zero - .9, 'crosses\nbelow zero', ha='right', color=GREEN_DEEP)


def paint_signal_crossing(c):
    """The same oscillator against its own signal line."""
    panel = _oscillator_panel(c)
    sig = signal_line()
    _line(c, panel, OSC)
    _line(c, panel, sig, color=ck.GOLD, lw=2.8)
    c.text(panel.x(0), panel.y(92), 'black line: the oscillator.  gold line: its signal line.', ha='left', color=INK)
    # Up through the signal line between readings 2 and 3, down between 7 and 8.
    for index, (i, word) in enumerate(((2, 'crosses above signal'), (7, 'crosses below signal'))):
        a0, a1 = OSC[i], OSC[i + 1]
        # the signal line has no reading at 0 or 1, but is defined from 2 on
        b0, b1 = sig[i], sig[i + 1]
        t = _cross(a0, a1, b0, b1)
        x = panel.x(i) + t * (panel.x(i + 1) - panel.x(i))
        y = panel.y(a0 + t * (a1 - a0))
        for j in (i, i + 1):
            c.text(panel.x(j), panel.y(OSC[j]) + (.2 if OSC[j] >= sig[j] else -.5), str(OSC[j]), color=INK)
            if index == 1 and j == 8:   # the crossing is just left of this reading, so keep its badge's side clear
                c.text(panel.x(j) + .5, panel.y(sig[j]) + .3, f'{sig[j]:.1f}', color=ck.GOLD)
            else:
                c.text(panel.x(j), panel.y(sig[j]) + (-.5 if OSC[j] >= sig[j] else .2), f'{sig[j]:.1f}', color=ck.GOLD)
        c.point((0, index + 1, 'cross'), x, y)
        c.text(*((x + .7, y - .55) if index == 0 else (x + .4, y + .6)), word, ha='left', color=GREEN_DEEP)


# The fourteen bars of one lookback, oldest first, today's last. One reaches
# 56.00 (the highest high), a different one 50.00 (the lowest low); each is
# a possible bar, low <= open and close <= high.
LOOKBACK = ((52.0, 52.8, 51.6, 52.4), (52.4, 53.6, 52.2, 53.4), (53.4, 54.6, 53.2, 54.2),
            (54.2, 56.0, 54.0, 55.4), (55.4, 55.6, 54.0, 54.4), (54.4, 54.8, 53.0, 53.2),
            (53.2, 53.6, 51.8, 52.0), (52.0, 52.4, 50.0, 50.8), (50.8, 52.2, 50.6, 52.0),
            (52.0, 53.0, 51.8, 52.8), (52.8, 53.4, 52.2, 52.6), (52.6, 53.8, 52.4, 53.6),
            (53.6, 54.0, 52.8, 53.0), (52.5, 54.8, 52.1, 54.0))


def paint_raw_k(c):
    """Fourteen bars of ours, and today's close placed between their highest high and lowest low."""
    import deckkit as dk
    gold, red = '#' + str(dk.MARK_COLORS['gold']), '#' + str(dk.MARK_COLORS['red'])
    hi, lo = 56.0, 50.0
    panel = Panel(c, 1.0, 6.4, .85, 3.25, 49.0, 57.0, len(LOOKBACK))
    ticks = [panel.bar(i, *row, tag=i, half=.09) for i, row in enumerate(LOOKBACK)]
    top, bottom, today = ticks[3], ticks[7], ticks[-1]
    end = panel.x(len(LOOKBACK) - 1) + .3
    # Each level runs from the bar that sets it to today's bar, in its mark's colour.
    c.stroke((top['high'][0], end), (panel.y(hi), panel.y(hi)), color=gold, lw=2.2, dashed=True)
    c.stroke((bottom['low'][0], end), (panel.y(lo), panel.y(lo)), color=red, lw=2.2, dashed=True)
    c.text(panel.x(4.2), panel.y(hi) + .17, 'Hn 56.00 = 100%', ha='left', va='bottom', color=GREEN_DEEP)
    c.text(panel.x(8.4), panel.y(lo) - .17, 'Ln 50.00 = 0%', ha='left', va='top', color=GREEN_DEEP)
    close_x, close_y = today['close']
    c.text(close_x + .3, close_y, 'C 54.00', ha='left')
    c.text(panel.x(6.5), .55, 'the 13 bars before today', color=MUTED)
    c.text(panel.x(13), .55, 'today', color=MUTED)
    bx = end + 1.5
    c.stroke((close_x + 1.35, bx), (close_y, close_y), color=MUTED, lw=1.4, dashed=True)
    c.stroke((bx, bx), (panel.y(lo), panel.y(54.0)), color=ck.GOLD, lw=3)
    c.text(bx + .2, (panel.y(lo) + panel.y(54.0)) / 2 - .15, 'C - Ln = 4.00', ha='left', color=GREEN_DEEP)
    bx2 = bx + 2.6
    c.stroke((bx2, bx2), (panel.y(lo), panel.y(hi)), color=GREEN_DEEP, lw=3)
    c.text(bx2 - .2, panel.y(55.0) + .1, 'Hn - Ln = 6.00', ha='right', color=GREEN_DEEP)
    c.text(bx2 - .2, panel.y(55.0) - .3, 'raw %K = 66.7%', ha='right', color=ck.GOLD)
    c.point((0, 1, 'hi'), *top['high'])
    c.point((0, 2, 'lo'), *bottom['low'])
    c.point((0, 3, 'close'), close_x, close_y)


# ---------------------------------------------------------------------------
# Charts that pair with the idea slides: one explanation, one chart.

def _bar_row(panel, rows, slots, *, tags=None):
    return [panel.bar(slot, *row, tag=None, half=.14) for slot, row in zip(slots, rows)]


def paint_closes(c, *, variant):
    """The same range of ours with closes at different places in it.

    'idea': one close near the top and one near the bottom. 'ends': a close
    at the lowest low, one in the middle and one at the highest high."""
    import deckkit as dk
    gold = red = '#' + ck.GREEN_DEEP.lstrip('#')   # a colour no mark uses, so no mark colour points at a level
    hi, lo = 56.0, 50.0
    if variant == 'idea':
        bars = ((53.0, 55.6, 52.8, 55.4), (52.4, 52.6, 50.0, 50.6))
        notes = ('close near the top of the range', 'close near the bottom of the range')
    else:
        bars = ((51.0, 51.6, 50.0, 50.0), (52.6, 53.4, 52.2, 53.0), (54.8, 56.0, 54.6, 56.0))
        notes = ('close at the lowest low', 'close in the middle', 'close at the highest high')
    panel = Panel(c, 1.4, 9.0, .85, 3.25, 49.0, 57.0, 6)
    slots = (1.0, 4.0) if variant == 'idea' else (0.6, 2.9, 5.2)
    c.stroke((1.2, 10.9), (panel.y(hi), panel.y(hi)), color=gold, lw=2.2, dashed=True)
    c.stroke((1.2, 10.9), (panel.y(lo), panel.y(lo)), color=red, lw=2.2, dashed=True)
    c.text(1.25, panel.y(hi) + .17, 'highest high of the lookback, Hn 56.00 = 100%', ha='left', va='bottom', color=GREEN_DEEP)
    c.text(1.25, panel.y(lo) - .17, 'lowest low, Ln 50.00 = 0%', ha='left', va='top', color=GREEN_DEEP)
    ticks = []
    for index, (slot, row, note) in enumerate(zip(slots, bars, notes), 1):
        t = panel.bar(slot, *row, half=.17)
        ticks.append(t)
        pct = (row[3] - lo) / (hi - lo) * 100
        cx, cy = t['close']
        dy = .3 if pct <= 0 else -.3 if pct >= 100 else 0
        c.text(cx + .3, cy + dy, f'C {row[3]:.2f} = {pct:.0f}%' if variant == 'ends' else f'C {row[3]:.2f} = {pct:.1f}%', ha='left')
        c.text(panel.x(slot) + .1, .45, note, ha='center', color=MUTED)
        c.point((0, index, 'close'), cx, cy)


def paint_range_percent(c):
    """The fourteen bars of the worked example, and every close as one dot on a 0 to 100 scale."""
    import deckkit as dk
    gold = red = '#' + ck.GREEN_DEEP.lstrip('#')
    hi, lo = 56.0, 50.0
    bars = Panel(c, 1.0, 5.2, .85, 3.25, 49.0, 57.0, len(LOOKBACK))
    dots = Panel(c, 6.4, 9.3, .85, 3.25, 49.0, 57.0, len(LOOKBACK))
    ticks = [bars.bar(i, *row, half=.07) for i, row in enumerate(LOOKBACK)]
    c.stroke((1.0, 9.6), (bars.y(hi), bars.y(hi)), color=gold, lw=2.2, dashed=True)
    c.stroke((1.0, 9.6), (bars.y(lo), bars.y(lo)), color=red, lw=2.2, dashed=True)
    c.text(1.0, bars.y(hi) + .17, 'Hn 56.00', ha='left', va='bottom', color=GREEN_DEEP)
    c.text(1.0, bars.y(lo) - .17, 'Ln 50.00', ha='left', va='top', color=GREEN_DEEP)
    for pct, price in ((100, hi), (50, 53.0), (0, lo)):
        c.text(10.2, bars.y(price), f'{pct}%', ha='left', color=INK)
    ys = []
    for i, row in enumerate(LOOKBACK):
        y = dots.y(row[3])
        x = dots.x(i)
        c.stroke((x - .012, x + .012), (y, y), color=INK, lw=8)
        ys.append(y)
    c.text(3.1, .55, 'the 14 bars of our worked example', color=MUTED)
    c.text(7.9, .55, "each bar's close on the 0 to 100 scale", color=MUTED)
    c.point((0, 1, 'hi'), *ticks[3]['high'])
    c.point((0, 2, 'lo'), *ticks[7]['low'])
    c.box((0, 3, 'group'), dots.x(0) - .15, min(ys) - .1, dots.x(len(LOOKBACK) - 1) + .15, max(ys) + .1, frac=.5)


def paint_zones(c):
    """One bounded oscillator of ours with its overbought and oversold zones and its equilibrium."""
    readings = (46, 52, 58, 66, 74, 78, 72, 62, 52, 44, 34, 26, 29, 38)
    panel = Panel(c, 1.0, 8.6, .75, 3.3, 0, 100, len(readings))
    from matplotlib.patches import Rectangle
    left, right = panel.x(0) - .2, panel.x(len(readings) - 1) + .2
    for lo_, hi_, tint in ((70, 100, '#FDF0D2'), (0, 30, '#E3EEE6')):
        c.fig.add_artist(Rectangle((left, panel.y(lo_)), right - left, panel.y(hi_) - panel.y(lo_),
                                   transform=c.fig.dpi_scale_trans, facecolor=tint, edgecolor='none', zorder=0))
    for level, words, color in ((70, 'overbought: 70 and above', GREEN_DEEP), (50, 'equilibrium: 50', MUTED),
                                (30, 'oversold: 30 and below', GREEN_DEEP)):
        y = panel.y(level)
        c.stroke((panel.x(0) - .2, panel.x(len(readings) - 1) + .2), (y, y), color=color, lw=1.6, dashed=True)
    c.text(9.2, panel.y(70) + .02, 'overbought:\n70 and above', ha='left', color=GREEN_DEEP)
    c.text(9.2, panel.y(50), 'equilibrium:\n50', ha='left', color=MUTED)
    c.text(9.2, panel.y(30), 'oversold:\n30 and below', ha='left', color=GREEN_DEEP)
    panel.path(list(enumerate(readings)), color=INK, lw=2.8)
    c.text(panel.x(5), panel.y(78) + .3, '78', color=INK)
    c.text(panel.x(11), panel.y(26) - .3, '26', color=INK)
    c.point((0, 1, 'high'), panel.x(5), panel.y(78))
    c.point((0, 2, 'low'), panel.x(11), panel.y(26))
    c.point((0, 3, 'mid'), panel.x(0) - .2, panel.y(50))


def paint_hidden(c):
    """Price over an indicator: the price makes a higher peak, the indicator a lower one."""
    price = (52, 55, 58, 60, 57, 56, 59, 63, 61)
    osc = (40, 55, 70, 78, 62, 56, 64, 66, 58)
    top = Panel(c, 1.6, 9.2, 2.2, 3.45, 50, 66, len(price))
    low = Panel(c, 1.6, 9.2, .6, 1.8, 0, 100, len(osc))
    top.path(list(enumerate(price)), color=INK, lw=2.8)
    low.path(list(enumerate(osc)), color=INK, lw=2.8)
    c.text(.5, 2.95, 'price', ha='left', color=GREEN_DEEP)
    c.text(.5, 1.2, 'indicator\nbelow', ha='left', color=GREEN_DEEP)
    c.text(top.x(3), top.y(60) + .3, '60', color=INK)
    c.text(top.x(7), top.y(63) + .3, '63', color=INK)
    c.text(low.x(3), low.y(78) + .3, '78', color=INK)
    c.text(low.x(7), low.y(66) + .3, '66', color=INK)
    c.point((0, 1, 'price'), top.x(7), top.y(63))
    c.point((0, 2, 'osc'), low.x(7), low.y(66))
