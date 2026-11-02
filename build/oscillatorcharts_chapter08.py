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


def paint_equilibrium_crossing(c):
    """The oscillator crossing its 50 level, up and then down."""
    panel = _oscillator_panel(c)
    _line(c, panel, OSC)
    c.text(panel.x(0), panel.y(80), 'our oscillator', ha='left', color=GREEN_DEEP)
    # Readings either side of each crossing, written on the chart.
    for i, dx, dy in ((4, 0, -.26), (5, -.12, .28), (9, 0, .28), (10, .12, -.28)):
        c.text(panel.x(i) + dx, panel.y(OSC[i]) + dy, str(OSC[i]), color=INK)
    # Up through 50 between readings 4 and 5, down through it between 9 and 10.
    for index, (i, word, wx, wy, ha) in enumerate(((4, 'crosses above 50', -.35, -.95, 'right'),
                                                   (9, 'crosses below 50', -.2, -.95, 'right'))):
        a, b = OSC[i], OSC[i + 1]
        t = (50 - a) / (b - a)
        x = panel.x(i) + t * (panel.x(i + 1) - panel.x(i))
        c.point((0, index + 1, 'cross'), x, panel.y(50))
        c.text(x + wx, panel.y(50) + wy, word, ha=ha, color=GREEN_DEEP)
    c.text(panel.x(OSC.__len__() - 1) + .3, panel.y(OSC[-1]), '41', ha='left')


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
        for j in ((i, i + 1) if index == 0 else (i, i + 2)):
            c.text(panel.x(j), panel.y(OSC[j]) + (.2 if OSC[j] >= sig[j] else -.5), str(OSC[j]), color=INK)
            c.text(panel.x(j), panel.y(sig[j]) + (-.5 if OSC[j] >= sig[j] else .2), f'{sig[j]:.1f}', color=ck.GOLD)
        c.point((0, index + 1, 'cross'), x, y)
        c.text(x + .3, y + (.95 if index == 0 else .65), word, ha='left', color=GREEN_DEEP)


def paint_raw_k(c):
    """One bar of ours against the highest high and lowest low of its lookback."""
    hi, lo = 56.0, 50.0
    bar = (52.5, 54.8, 52.1, 54.0)    # open, high, low, close
    panel = Panel(c, 2.9, 3.9, .85, 3.25, 49.0, 57.0, 1)
    x = panel.x(0)
    for price, words in ((hi, 'Hn 56.00 = 100%'), (lo, 'Ln 50.00 = 0%')):
        y = panel.y(price)
        c.stroke((1.0, 10.9), (y, y), color=MUTED, lw=1.6, dashed=True)
        c.text(1.05, y + (.2 if price == hi else -.2), words, ha='left',
               va='bottom' if price == hi else 'top', color=GREEN_DEEP)
    ticks = panel.bar(0, *bar, tag='bar')
    close_x, close_y = ticks['close']
    c.text(close_x + .12, close_y, 'C 54.00', ha='left')
    c.text(x, panel.y(bar[2]) - .3, "today's bar", va='top', color=MUTED)
    c.stroke((close_x + 1.5, x + 1.95), (close_y, close_y), color=MUTED, lw=1.4, dashed=True)
    c.stroke((x + 1.95, x + 1.95), (panel.y(lo), panel.y(bar[3])), color=ck.GOLD, lw=3)
    c.text(x + 2.15, (panel.y(lo) + panel.y(bar[3])) / 2, 'C - Ln = 4.00', ha='left', color=GREEN_DEEP)
    c.stroke((x + 4.95, x + 4.95), (panel.y(lo), panel.y(hi)), color=GREEN_DEEP, lw=3)
    c.text(x + 5.15, (panel.y(lo) + panel.y(hi)) / 2 + .15, 'Hn - Ln = 6.00', ha='left', color=GREEN_DEEP)
    c.text(x + 5.15, (panel.y(lo) + panel.y(hi)) / 2 - .25, '%K = 66.7%', ha='left', color=ck.GOLD)
    c.point((0, 1, 'hi'), 1.0 + .05, panel.y(hi))
    c.point((0, 2, 'lo'), 1.0 + .05, panel.y(lo))
    c.point((0, 3, 'close'), close_x, close_y)
