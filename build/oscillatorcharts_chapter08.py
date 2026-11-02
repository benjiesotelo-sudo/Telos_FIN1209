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
    for index, (i, word, wx, wy, ha) in enumerate(((4, 'above 50', -.2, -.8, 'right'),
                                                   (9, 'below 50', -.2, -.8, 'right'))):
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
            c.text(x - .3, zero + .5, 'above zero', ha='right', color=GREEN_DEEP)
        else:
            c.text(x + .3, zero + .5, 'below zero', ha='left', color=GREEN_DEEP)


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
        c.text(x + (.45 if index == 0 else .4), y + (.85 if index == 0 else .6), word, ha='left', color=GREEN_DEEP)


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
    ticks = [panel.bar(i, *row, tag=i) for i, row in enumerate(LOOKBACK)]
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
