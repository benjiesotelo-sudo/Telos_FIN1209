"""Chapter 7 sketches that show a shape or a price relationship.

The OHLC pages in ``chartlayout_chapter07`` draw one cell of bars. These
painters draw what that layout cannot: two or four small panels on one chart,
a price path shaped like a head and shoulders, and a bar set against the
previous bar's close, low or high. They draw in inches from the chart's
bottom left corner and hand the layout the same three things its own pages
do: ink for badges and labels to avoid, boxes, and the targets that marks sit
on. Everything is our own drawing from invented prices.
"""
from __future__ import annotations

from matplotlib.lines import Line2D

import chartkit as ck

HALF = .17   # an OHLC tick's reach either side of the bar's stem


class Panel:
    """A band of the chart with a price scale and evenly spaced slots."""

    def __init__(self, c, x0, x1, y0, y1, lo, hi, slots):
        self.c, self.x0, self.x1, self.y0, self.y1 = c, x0, x1, y0, y1
        self.lo, self.hi, self.slots = lo, hi, slots

    def x(self, slot):
        return self.x0 + (self.x1 - self.x0) * (slot + .5) / self.slots

    def y(self, price):
        return self.y0 + (price - self.lo) / (self.hi - self.lo) * (self.y1 - self.y0)

    def bar(self, slot, o, h, l, cl, *, tag=None):
        """Draw one OHLC bar and return the tick positions, in inches."""
        x = self.x(slot)
        for xs, ys in (((x, x), (l, h)), ((x - HALF, x), (o, o)), ((x, x + HALF), (cl, cl))):
            self.c.stroke(xs, [self.y(v) for v in ys], color=ck.INK, lw=2.4)
        ticks = {'open': (x - HALF, self.y(o)), 'high': (x, self.y(h)),
                 'low': (x, self.y(l)), 'close': (x + HALF, self.y(cl))}
        if tag is not None:
            self.c.ticks[tag] = ticks
        return ticks

    def level(self, price, slot0, slot1, *, pad=.28):
        """A dashed level carried from one bar across to another."""
        y = self.y(price)
        self.c.stroke((self.x(slot0) - pad, self.x(slot1) + pad), (y, y), color=ck.INK,
                      lw=1.6, dashed=True)
        return y

    def path(self, points, *, color=ck.INK, lw=2.6):
        """A price path through (slot, price) points, with ink for badges."""
        xy = [(self.x(s), self.y(p)) for s, p in points]
        for (xa, ya), (xb, yb) in zip(xy, xy[1:]):
            self.c.stroke((xa, xb), (ya, yb), color=color, lw=lw)
        return xy


class Canvas:
    """What a painter draws on, and what it reports back to the layout."""

    def __init__(self, fig, width, text, segments, ink, groups, targets):
        self.fig, self.W, self.text = fig, width, text
        self._segments, self._ink, self.groups, self.targets = segments, ink, groups, targets
        self.ticks = {}

    def stroke(self, xs, ys, *, color, lw, dashed=False, ink=True):
        artist = Line2D(xs, ys, transform=self.fig.dpi_scale_trans, color=color, lw=lw,
                        ls=(0, (4, 3)) if dashed else '-')
        self.fig.add_artist(artist)
        if not ink:
            return
        # Every few hundredths of an inch the line is ink a badge must keep off.
        (xa, xb), (ya, yb) = xs, ys
        steps = max(2, int(((xb - xa) ** 2 + (yb - ya) ** 2) ** .5 / .08))
        for k in range(steps + 1):
            t = k / steps
            self._add_ink(xa + (xb - xa) * t, ya + (yb - ya) * t)

    def _add_ink(self, x, y, reach=.025):
        from matplotlib.transforms import Bbox
        dpi = ck.DPI
        box = Bbox.from_extents((x - reach) * dpi, (y - reach) * dpi,
                                (x + reach) * dpi, (y + reach) * dpi)
        self._segments.append(box)
        self._ink.append(box)

    def box(self, key, x0, y0, x1, y1, *, frac=.5):
        """A group mark: the box is the target, and the badge keeps outside it.
        ``frac`` is how far up its right edge the mark's badge starts looking."""
        bounds = (x0 * ck.DPI, y0 * ck.DPI, x1 * ck.DPI, y1 * ck.DPI)
        self.groups[key] = bounds
        self.targets[key] = (bounds[2], bounds[1] + (bounds[3] - bounds[1]) * frac)

    def point(self, key, x, y):
        self.targets[key] = (x * ck.DPI, y * ck.DPI)


GREEN_DEEP, MUTED = ck.GREEN_DEEP, ck.MUTED


def _title(c, x, y, words):
    c.text(x, y, words, color=GREEN_DEEP)


# ---------------------------------------------------------------- shapes


# One head and shoulders, in slots and heights: base, left shoulder, trough,
# head, trough, right shoulder, base. The inverted one is this turned over.
_HS = ((0, 0), (1, 1.3), (2, .75), (3.5, 2.0), (5, .75), (6, 1.3), (7, 0))


def paint_head_shoulders(c):
    """Slide 21: the standard shape and the inverted one, side by side."""
    for index, (x0, inverted) in enumerate(((.55, False), (6.05, True))):
        panel = Panel(c, x0, x0 + 4.4, .95, 2.75, 0, 2.0, 8)
        flip = (lambda h: 2.0 - h) if inverted else (lambda h: h)
        panel.path([(s, flip(h)) for s, h in _HS])
        neck = flip(.75)
        c.stroke((panel.x(1.3), panel.x(5.7)), (panel.y(neck), panel.y(neck)), color=MUTED,
                 lw=1.6, dashed=True)
        lift, va = (-.17, 'top') if inverted else (.17, 'bottom')
        for (s, h), words in ((_HS[1], 'left shoulder'), (_HS[3], 'head'), (_HS[5], 'right shoulder')):
            c.text(panel.x(s), panel.y(flip(h)) + lift, words, va=va)
        c.text(panel.x(3.5), panel.y(neck) + (.2 if inverted else -.2), 'neckline',
               va='bottom' if inverted else 'top', color=MUTED)
        c.box((0, index, 'group'), x0 - .3, .42, x0 + 4.7, 3.3)
        _title(c, x0 + 2.2, 3.6, 'Inverted head and shoulders' if inverted else 'Head and shoulders')


# -------------------------------------------------------- trend then bars


_RISE = ((45.0, 46.0, 44.8, 45.6), (45.7, 47.2, 45.5, 46.8), (46.9, 48.3, 46.7, 48.1))
_FALL = ((51.0, 51.2, 50.4, 50.6), (50.5, 50.6, 49.2, 49.4), (49.5, 49.6, 47.9, 48.1))


def _panels(c, lo, hi, slots, y0=.85, y1=2.95):
    left = Panel(c, .25, 5.45, y0, y1, lo, hi, slots)
    right = Panel(c, 5.95, 11.15, y0, y1, lo, hi, slots)
    return left, right


def paint_expectation(c):
    """Slide 25: the same uptrend, a bullish formation and a bearish one."""
    # An uptrend of three bars, then a two-bar formation in each panel.
    bullish = ((48.2, 48.9, 48.0, 48.8), (48.9, 50.0, 48.8, 49.9))
    bearish = ((48.2, 48.7, 47.8, 48.0), (47.9, 48.0, 46.9, 47.0))
    left, right = _panels(c, 44.4, 50.4, 5)
    for index, (panel, pair, name, words) in enumerate((
            (left, bullish, 'Bullish formation', 'agrees with the trend'),
            (right, bearish, 'Bearish formation', 'disagrees with the trend'))):
        for slot, row in enumerate(_RISE):
            panel.bar(slot, *row)
        for slot, row in enumerate(pair, 3):
            panel.bar(slot, *row)
        c.text(panel.x(1), .55, 'uptrend: bullish', color=MUTED)
        c.text(panel.x(3.5), .55, name.lower(), color=MUTED)
        _title(c, (panel.x0 + panel.x1) / 2, 3.45,
               ('Continuation' if index == 0 else 'Potential reversal') + ': ' + words)
        c.box((0, index, 'group'), panel.x(3) - .42, panel.y(min(r[2] for r in pair)) - .3,
              panel.x(4) + .42, panel.y(max(r[1] for r in pair)) + .3)


def _tile(c, x0, y0, trend, pair, name, result):
    """One of four small panels: two trend bars, a two-bar formation, a label."""
    lo = min(r[2] for r in (*trend, *pair))
    hi = max(r[1] for r in (*trend, *pair))
    panel = Panel(c, x0, x0 + 2.1, y0 + .18, y0 + 1.5, lo, hi, 4)
    for slot, row in enumerate((*trend, *pair)):
        panel.bar(slot, *row)
    c.text(x0 + 2.7, y0 + .98, name, ha='left', color=GREEN_DEEP)
    c.text(x0 + 2.7, y0 + .56, result, ha='left', color=GREEN_DEEP)
    return panel


def paint_four_cases(c):
    """Slide 27: trend sentiment against formation, all four cases."""
    up = ((46.0, 46.9, 45.8, 46.7), (46.8, 47.9, 46.6, 47.7))
    down = tuple((round(94 - o, 2), round(94 - l, 2), round(94 - h, 2), round(94 - cl, 2))
                 for o, h, l, cl in up)
    bull_up = ((47.8, 48.5, 47.6, 48.4), (48.5, 49.4, 48.4, 49.3))
    bear_up = ((47.8, 48.3, 47.2, 47.4), (47.3, 47.4, 46.4, 46.5))
    mirror = lambda pair: tuple((round(94 - o, 2), round(94 - l, 2), round(94 - h, 2), round(94 - cl, 2))
                                for o, h, l, cl in pair)
    cases = (
        (up, bull_up, 'Uptrend, bullish', 'CONTINUATION', 2.05, 3.65),
        (up, bear_up, 'Uptrend, bearish', 'POTENTIAL REVERSAL', 2.05, 3.65),
        (down, mirror(bear_up), 'Downtrend, bullish', 'POTENTIAL REVERSAL', 0.3, 1.65),
        (down, mirror(bull_up), 'Downtrend, bearish', 'CONTINUATION', 0.3, 1.65))
    for index, (trend, pair, name, result, y0, _top) in enumerate(cases):
        x0 = .3 if index % 2 == 0 else 6.0
        panel = _tile(c, x0, y0 + .08, trend, pair, name, result)
        rows = pair
        c.box((0, index, 'group'), panel.x(2) - .3, panel.y(min(r[2] for r in rows)) - .12,
              panel.x(3) + .3, panel.y(max(r[1] for r in rows)) + .12)


def paint_two_trends(c):
    """Slide 26: one two-bar formation after a rise and after a fall."""
    formation = ((48.1, 48.3, 47.8, 48.0), (48.1, 48.8, 48.0, 48.6))
    left, right = _panels(c, 44.9, 51.4, 5.6, y0=.95, y1=3.0)
    for index, (panel, trend, title) in enumerate((
            (left, _RISE, 'Prices rose before it'), (right, _FALL, 'Prices fell before it'))):
        for slot, row in enumerate(trend):
            panel.bar(slot, *row)
        for slot, row in enumerate(formation, 3):
            panel.bar(slot, *row, tag=(index, slot))
        _title(c, (panel.x0 + panel.x1) / 2, 3.5, title)
        first = trend[0][3]
        for slot, row in ((0, trend[0]), (2, trend[2])):
            c.text(panel.x(slot), panel.y(row[2]) - .12, f'C {row[3]:.2f}', va='top')
        hi_tick = c.ticks[(index, 3)]['high']
        c.text(panel.x(3), hi_tick[1] + .16, 'H 48.30', va='bottom')
        close_tick = c.ticks[(index, 4)]['close']
        c.text(close_tick[0] + .09, close_tick[1] + .06, 'C 48.60', ha='left', va='bottom')
        c.box((0, index, 'group'), panel.x(0) - .55, panel.y(min(r[2] for r in trend)) - .5,
              panel.x(2) + .47, panel.y(max(r[1] for r in trend)) + .15, frac=.85)
        if index == 0:
            c.point((0, 10, 'high'), *c.ticks[(0, 3)]['high'])
            c.point((0, 11, 'close'), *c.ticks[(0, 4)]['close'])
    c.text(5.7, .5, 'The same two bars after a rise and after a fall', color=MUTED)


def paint_prior_bar(c, *, up):
    """Slides 39 and 52: a close against the previous bar's close and extreme."""
    if up:
        yesterday = (50.0, 52.0, 49.0, 51.8)   # open, high, low, close
        today = ((51.7, 51.9, 50.9, 51.2), (51.5, 51.7, 48.4, 48.8))
        lo, hi = 47.6, 52.8
    else:
        yesterday = (40.6, 41.0, 38.0, 38.2)
        today = ((38.3, 39.0, 38.2, 38.8), (38.5, 41.5, 38.3, 41.2))
        lo, hi = 37.2, 42.2
    left, right = _panels(c, lo, hi, 2, y0=.95, y1=3.0)
    for index, (panel, bar) in enumerate(((left, today[0]), (right, today[1]))):
        panel.bar(0, *yesterday, tag=(index, 0))
        panel.bar(1, *bar, tag=(index, 1))
        c.text(panel.x(0), .55, 'yesterday', color=MUTED)
        c.text(panel.x(1), .55, 'today', color=MUTED)
        o, h, l, cl = yesterday
        xx = panel.x(0)
        c.text(xx, panel.y(h) + .15, f'H {h:.2f}', va='bottom')
        c.text(xx, panel.y(l) - .15, f'L {l:.2f}', va='top')
        c.text(xx - .26, panel.y(cl), f'C {cl:.2f}', ha='right')
        c.text(panel.x(1) + .26, panel.y(bar[3]), f'C {bar[3]:.2f}', ha='left')
    # The level each close is read against, carried across to today's bar.
    ref_a = yesterday[3] if up else yesterday[3]
    left.level(ref_a, 0, 1, pad=.2)
    right.level(yesterday[2] if up else yesterday[1], 0, 1, pad=.2)
    c.point((0, 0, 'ref'), *c.ticks[(0, 0)]['close'])
    c.point((0, 1, 'today'), *c.ticks[(0, 1)]['close'])
    c.point((0, 2, 'today'), *c.ticks[(1, 1)]['close'])
    c.point((0, 3, 'ref'), *c.ticks[(1, 0)]['low' if up else 'high'])


def paint_gap(c):
    """Slide 64: a PHP 0.40 gap and a PHP 1.00 gap, to the same scale."""
    first = (49.2, 50.0, 48.8, 49.8)
    smaller = (50.6, 51.2, 50.4, 51.0)
    larger = (51.4, 52.0, 51.0, 51.8)
    left, right = _panels(c, 48.7, 52.1, 2, y0=.95, y1=3.1)
    for index, (panel, middle, gap_to, title) in enumerate((
            (left, smaller, 50.4, 'A gap of PHP 0.40'), (right, larger, 51.0, 'A gap of PHP 1.00'))):
        panel.bar(0, *first)
        panel.bar(1, *middle)
        _title(c, (panel.x0 + panel.x1) / 2, 3.5, title)
        c.text(panel.x(0) - .26, panel.y(50.0), 'H 50.00', ha='right')
        c.text(panel.x(1) + .26, panel.y(gap_to), f'L {gap_to:.2f}', ha='left')
        c.text(panel.x(0), .55, 'first bar', color=MUTED)
        c.text(panel.x(1), .55, 'middle bar', color=MUTED)
        c.stroke((panel.x(0), panel.x(1)), (panel.y(50.0), panel.y(50.0)), color=MUTED, lw=1.4,
                 dashed=True, ink=False)
        c.stroke((panel.x(0), panel.x(1)), (panel.y(gap_to), panel.y(gap_to)), color=MUTED, lw=1.4,
                 dashed=True, ink=False)
        mid = panel.x(.5)
        c.box((0, index, 'group'), mid - .32, panel.y(50.0), mid + .32, panel.y(gap_to))


# ------------------------------------------------- head and shoulders in a trend


_DAYS = (40, 41.5, 40.8, 43, 44, 43.2, 45.5, 47, 46.2, 48.5, 50)


def paint_trend_shapes(c):
    """Slide 35: a ten day climb, then an inverted head and shoulders or a head and shoulders."""
    inverted = ((12, 48.0), (13, 49.5), (14.5, 46.5), (16, 49.5), (17, 48.0), (18, 50.0))
    standard = ((12, 52.0), (13, 50.6), (14.5, 54.0), (16, 50.6), (17, 52.0), (18, 50.0))
    left, right = _panels(c, 35.0, 56.0, 20, y0=.8, y1=3.0)
    for index, (panel, shape, title) in enumerate((
            (left, inverted, 'Inverted head and shoulders: continuation'),
            (right, standard, 'Head and shoulders: reversal'))):
        rise = panel.path([(s, p) for s, p in enumerate(_DAYS)])
        panel.path([(10, 50.0), *shape])
        _title(c, (panel.x0 + panel.x1) / 2, 3.5, title)
        c.text(rise[0][0], rise[0][1] - .18, 'PHP 40', ha='left', va='top')
        c.text(rise[-1][0] - .1, rise[-1][1] + .2, 'PHP 50', ha='right', va='bottom')
        c.stroke((panel.x(10), panel.x(18)), (panel.y(50.0), panel.y(50.0)), color=MUTED, lw=1.2,
                 dashed=True, ink=False)
        if index == 0:
            c.box((0, 0, 'group'), panel.x(0) - .15, panel.y(35.6), panel.x(10) + .1, panel.y(54.5), frac=1.0)
        lo = min(p for _s, p in shape)
        hi = max(p for _s, p in shape)
        c.box((0, index + 1, 'group'), panel.x(11.7), panel.y(lo) - .15, panel.x(18.3), panel.y(hi) + .15)


# ------------------------------------------- the 16 reversal characteristics
#
# One small sketch per characteristic, two to a slide, each drawn from the
# numbers the slide's own sentence gives. A sketch is a plain dict: a title, a
# data range, what to draw, and the features the numbered marks sit on.


class _Plot:
    def __init__(self, c, px0, px1, py0, py1, xr, yr):
        self.c, self.px0, self.px1, self.py0, self.py1, self.xr, self.yr = c, px0, px1, py0, py1, xr, yr

    def X(self, d):
        return self.px0 + (d - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.px1 - self.px0)

    def Y(self, v):
        return self.py0 + (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.py1 - self.py0)


def _draw_panel(c, spec, x0, x1, first):
    plot = _Plot(c, x0, x1, spec.get('py0', .85), spec.get('py1', 2.55), spec['xr'], spec['yr'])
    _title(c, (x0 + x1) / 2, 3.55, spec['title'])
    vol = spec.get('cols')
    for kind, *args in spec.get('draw', ()):
        if kind == 'path':
            for (xa, ya), (xb, yb) in zip(args[0], args[0][1:]):
                c.stroke((plot.X(xa), plot.X(xb)), (plot.Y(ya), plot.Y(yb)), color=ck.INK, lw=2.6)
        elif kind == 'path_m':
            for (xa, ya), (xb, yb) in zip(args[0], args[0][1:]):
                c.stroke((plot.X(xa), plot.X(xb)), (plot.Y(ya), plot.Y(yb)), color=MUTED, lw=1.8, dashed=True)
        elif kind == 'bar':
            x, o, h, l, cl = args
            px = plot.X(x)
            for xs, ys in (((px, px), (l, h)), ((px - HALF, px), (o, o)), ((px, px + HALF), (cl, cl))):
                c.stroke(xs, [plot.Y(v) for v in ys], color=ck.INK, lw=2.4)
        elif kind == 'candle':
            # A candlestick: a wick from low to high and a body from open to close.
            from matplotlib.patches import Rectangle
            x, o, h, l, cl = args
            px = plot.X(x)
            c.stroke((px, px), (plot.Y(l), plot.Y(h)), color=ck.INK, lw=2.4)
            top, bottom = plot.Y(max(o, cl)), plot.Y(min(o, cl))
            c.fig.add_artist(Rectangle((px - .15, bottom), .3, top - bottom, transform=c.fig.dpi_scale_trans,
                                       facecolor=ck.WHITE if cl >= o else ck.INK, edgecolor=ck.INK, lw=2.2, zorder=3))
            for k in range(0, 9):
                c._add_ink(px - .15 + .3 * k / 8, (top + bottom) / 2, reach=.0)
                c._add_ink(px, bottom + (top - bottom) * k / 8, reach=.15)
        elif kind == 'level':
            y, xa, xb = args
            c.stroke((plot.X(xa), plot.X(xb)), (plot.Y(y), plot.Y(y)), color=MUTED, lw=1.6, dashed=True)
        elif kind == 'col':
            x, v, base = args
            from matplotlib.patches import Rectangle
            r = Rectangle((plot.X(x) - .17, plot.Y(base)), .34, plot.Y(v) - plot.Y(base),
                          transform=c.fig.dpi_scale_trans, color=ck.GREEN, lw=0)
            c.fig.add_artist(r)
            c._add_ink(plot.X(x), (plot.Y(v) + plot.Y(base)) / 2, reach=.0)
            for k in range(0, 9):
                c._add_ink(plot.X(x), plot.Y(base) + (plot.Y(v) - plot.Y(base)) * k / 8, reach=.17)
        elif kind == 'text':
            x, y, words, kw = args
            c.text(plot.X(x), plot.Y(y), words, color=kw.get('color', ck.INK), ha=kw.get('ha', 'center'),
                   va=kw.get('va', 'center'))
    for number, feature in enumerate(spec['features'], 1 if first else 3):
        if feature[0] == 'box':
            _k, bx0, bx1, by0, by1, words, *place = feature
            c.box((0, number, 'group'), plot.X(bx0), plot.Y(by0), plot.X(bx1), plot.Y(by1), frac=.35)
            if place:
                c.text((plot.X(bx0) + plot.X(bx1)) / 2, plot.Y(by0) - .17, words, va='top')
            else:
                c.text((plot.X(bx0) + plot.X(bx1)) / 2, plot.Y(by1) + .17, words, va='bottom')
        else:
            _k, dx, dy, words, where = feature
            c.point((0, number, 'dot'), plot.X(dx), plot.Y(dy))
            ox, oy, ha, va = where
            c.text(plot.X(dx) + ox, plot.Y(dy) + oy, words, ha=ha, va=va)


def paint_characteristics(left, right):
    def paint(c):
        _draw_panel(c, left, .25, 5.45, True)
        _draw_panel(c, right, 5.95, 11.15, False)
    return paint


def _bars(rows, split=None):
    """Bars one slot apart; ``split`` leaves a wider gap after that many bars."""
    return [('bar', i + (.8 if split is not None and i >= split else 0), *row) for i, row in enumerate(rows)]


def _candles(rows, split=None):
    return [('candle',) + tuple(r[1:]) for r in _bars(rows, split)]


def _spec_pair(n):
    """The two sketches for the slide that carries characteristics n and n + 1."""
    return CHARACTERISTICS[n], CHARACTERISTICS[n + 1]


def _ranged(rows):
    return rows


CHARACTERISTICS = {
    1: dict(title='Each rise covers less ground', xr=(-.5, 5.5), yr=(95, 160),
            draw=[('path', [(0, 100), (1, 140), (2, 110), (3, 145), (4, 118), (5, 148)])],
            features=[('box', -.3, 1.3, 94, 144, 'a rise of 40'), ('box', 3.7, 5.3, 114, 152, 'a rise of 30')]),
    2: dict(title='Each swing takes fewer bars', xr=(-3, 51), yr=(95, 160),
            draw=[('path', [(0, 100), (20, 135), (36, 105), (48, 135)])],
            features=[('box', -1, 21, 96, 139, '20 bars'), ('box', 35, 49, 101, 139, '12 bars')]),
    3: dict(title='A pullback suddenly takes fewer bars', xr=(-3, 55), yr=(95, 170),
            draw=[('path', [(0, 100), (8, 130), (14, 112), (22, 142), (28, 122), (36, 150), (41, 132), (49, 160), (51, 150)])],
            features=[('box', 6, 16, 106, 136, 'took 6 bars'), ('box', 47.5, 53, 144, 166, 'takes 2 bars')]),
    4: dict(title='The bars get shorter', xr=(-.7, 6.5), yr=(47.5, 53),
            draw=_bars([(49.2, 51.5, 48.5, 51.0), (51.0, 51.8, 48.8, 49.5), (49.5, 51.4, 48.4, 50.8),
                        (50.0, 51.6, 49.6, 51.2), (51.2, 51.4, 49.4, 50.0), (50.0, 51.8, 49.8, 51.3)], split=3),
            features=[('box', -.4, 2.4, 47.9, 52.0, 'average range 3.00'), ('box', 3.2, 6.2, 48.9, 52.3, 'average range 2.00')]),
    5: dict(title='Even bars give way to uneven ones', xr=(-.7, 6.5), yr=(48.5, 53.5),
            draw=_bars([(49.9, 50.6, 49.6, 50.4), (50.4, 51.2, 50.2, 51.0), (51.0, 51.8, 50.8, 51.5),
                        (51.3, 51.6, 51.2, 51.5), (51.5, 51.9, 49.4, 50.0), (50.1, 50.8, 50.0, 50.6)], split=3),
            features=[('box', -.4, 2.4, 49.2, 52.1, 'about 1.00 each'), ('box', 3.2, 6.2, 48.9, 52.5, '0.40, 2.50 and 0.80')]),
    6: dict(title='Closes sit lower inside their bars', xr=(-.7, 6.5), yr=(47.3, 54),
            draw=_bars([(48.5, 50.0, 48.0, 49.6), (49.5, 51.0, 49.0, 50.6), (50.5, 52.0, 50.0, 51.6),
                        (51.6, 52.4, 50.4, 51.2), (52.0, 52.8, 50.8, 51.6), (52.4, 53.2, 51.2, 52.0)], split=3),
            features=[('box', -.4, 2.4, 47.6, 52.5, '0.80 of the range'), ('box', 3.2, 6.2, 50.0, 53.7, '0.40 of the range')]),
    7: dict(title='Real bodies shrink inside their candles', xr=(-.7, 6.5), yr=(47.3, 54),
            draw=_candles([(48.4, 50.0, 48.0, 49.6), (49.4, 51.0, 49.0, 50.6), (50.4, 52.0, 50.0, 51.6),
                        (50.75, 52.0, 50.0, 51.25), (50.95, 52.2, 50.2, 51.45), (51.15, 52.4, 50.4, 51.65)], split=3),
            features=[('box', -.4, 2.4, 47.6, 52.5, 'body 0.60 of the range'), ('box', 3.2, 6.2, 49.8, 52.9, 'body 0.25')]),
    8: dict(title='The trend gets steeper', xr=(0, 5.2), yr=(0, 1.8), py0=.85, py1=2.65,
            draw=[('path', [(.2, .2), (1.8, .2 + 1.6 * .364), (3.1, .2 + 1.6 * .364 + 1.3 * .700)])],
            features=[('box', .0, 1.65, .0, 1.0, 'about 20 degrees'), ('box', 2.05, 3.4, .8, 1.85, 'about 35 degrees')]),
    9: dict(title='Price sits just under resistance', xr=(-.7, 4.7), yr=(55.6, 60.6), py0=.75, py1=2.75,
            draw=_bars([(56.2, 57.0, 55.8, 56.8), (56.8, 57.8, 56.6, 57.6), (57.6, 58.4, 57.4, 58.2), (58.2, 59.2, 58.0, 59.0), (58.9, 59.4, 58.5, 59.0)]) + [('level', 60.0, -.6, 4.6)],
            features=[('dot', 4, 59.0, 'PHP 59', (.3, -.0, 'left', 'center')), ('dot', 4, 60.0, 'resistance PHP 60', (-.2, .3, 'right', 'bottom'))]),
    10: dict(title='Dips become fewer and shallower', xr=(-.5, 19.0), yr=(97, 132),
             draw=[('path', [(0, 100), (1, 105), (2, 102), (3, 107), (4, 104), (5, 109), (6, 106), (7, 111), (8, 108), (9, 113),
                             (10, 110), (11, 115), (12, 112), (13, 118), (14, 117), (15, 123), (16, 122), (17, 128)])],
             features=[('box', -.4, 12.4, 98, 118, 'six dips of about 3'), ('box', 12.7, 17.4, 110, 130, 'two dips of 1')]),
    11: dict(title='The pauses get longer', xr=(-2, 32), yr=(95, 137),
             draw=[('path', [(0, 100), (4, 110), (7, 110), (11, 120), (14, 120), (18, 130), (30, 130)])],
             features=[('box', 3.3, 7.7, 105, 114, '3 bars'), ('box', 17.3, 30.7, 125, 134, '12 bars')]),
    12: dict(title='A third gap in the trend', xr=(-.7, 3.7), yr=(48.4, 54.4), py0=.75, py1=2.75,
             draw=_bars([(49.0, 49.8, 48.8, 49.6), (50.4, 51.0, 50.2, 50.8), (51.7, 52.4, 51.5, 52.2), (53.4, 54.0, 53.2, 53.8)]),
             features=[('box', 2.6, 3.4, 52.4, 53.2, 'gap 0.80', 'below'), ('box', -.4, 2.4, 48.2, 53.0, 'two earlier gaps')]),
    13: dict(title='The average range is spent', xr=(-.7, 3.7), yr=(47.9, 54.0), py0=.75, py1=2.75,
             draw=_bars([(49.0, 51.4, 48.6, 51.0), (51.0, 52.2, 49.0, 49.6), (49.8, 52.4, 49.4, 51.9), (50.2, 53.0, 50.0, 52.8)]),
             features=[('box', -.4, 2.4, 48.0, 53.1, 'average range 3.00'), ('box', 2.6, 3.4, 49.6, 53.6, 'range so far 3.00')]),
    14: dict(title='Price overshoots a barrier', xr=(1.3, 7.2), yr=(56.2, 61.8), py0=.75, py1=2.75,
             draw=[('bar', 2, 56.8, 58.0, 56.6, 57.8), ('bar', 3, 57.8, 59.0, 57.6, 58.8), ('bar', 4, 58.8, 61.0, 58.6, 60.2), ('path_m', [(1.3, 58.0), (4, 60.0)])],
             features=[('dot', 4, 61.0, 'high at 61', (.3, .17, 'left', 'center')), ('dot', 4, 60.0, 'line at 60', (.3, -.14, 'left', 'center'))]),
    15: dict(title='Volume spikes far above its average', xr=(-.7, 5.6), yr=(0, 6.6), py0=.8, py1=2.6,
             draw=[('col', 0, 1.2, 0), ('col', 1, 1.1, 0), ('col', 2, 1.3, 0), ('col', 3, 1.2, 0), ('col', 4.8, 5.0, 0)],
             features=[('box', 4.2, 5.4, 0, 5.5, '5.0 million'), ('box', -.45, 3.45, 0, 2.2, 'average 1.2 million')]),
    16: dict(title='Price rises while volume falls', xr=(-.5, 7.5), yr=(76, 108), py0=.8, py1=2.75,
             draw=[('path', [(0, 94), (2, 100), (4, 96), (6, 104), (7, 101)]),
                   ('col', 2, 76 + 3.0 * 2, 76), ('col', 6, 76 + 1.8 * 2, 76)],
             features=[('box', 1.4, 2.6, 76, 102, 'volume 3.0 million'), ('box', 5.4, 6.6, 76, 106, 'volume 1.8 million')]),
}
