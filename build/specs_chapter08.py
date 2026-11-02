"""Plain-data chart specs for Chapter 8 Part A. Every number is ours, invented for teaching."""
import chartkit as ck

SPECS = {}
INK, MUTED, DEEP = ck.INK, ck.MUTED, ck.GREEN_DEEP


def pane(id='p', x=(1.3, 10.3), y=(.8, 3.25), lo=0, hi=1, n=10, **kw):
    return dict(id=id, x=x, y=y, lo=lo, hi=hi, n=n, **kw)


# ----------------------------------------------------------------- 8.1 overlays
SPECS['ob'] = dict(letter='I', spec=dict(
    panes=[pane(lo=42, hi=51.6, n=14)],
    series=[dict(pane='p', values=[43, 44, 45, 46, 47, 48, 49, 49.6, 48.6, 49.7, 48.8, 49.5, 48.2, 47.5],
                 labels=[(7, '49.60', 0, -.55), (9, '49.70', 0, -.55), (11, '49.50', 0, -.55)])],
    levels=[dict(pane='p', value=50.0, label='the line: resistance at 50.00', dy=.15)],
    marks=[('box', 'p', 0, 13, 49.88, 50.12), ('pt', 'p', 9, 49.7)]))

SPECS['op'] = dict(letter='J', spec=dict(
    panes=[pane('l', x=(1.0, 4.9), y=(1.0, 3.0), lo=25, hi=80, n=8, title='RSI laid on the price chart'),
           pane('t', x=(6.4, 10.4), y=(2.25, 3.0), lo=50, hi=62, n=8, title='RSI in its own window'),
           pane('b', x=(6.4, 10.4), y=(.7, 1.9), lo=0, hi=100, n=8)],
    series=[dict(pane='l', values=[52, 54, 53, 56, 58, 57, 60, 59], labels=[(3, 'price', 0, -.4)]),
            dict(pane='l', values=[35, 48, 62, 70, 64, 52, 58, 66], color=DEEP, labels=[(3, 'RSI 70', 0, .28)]),
            dict(pane='t', values=[52, 54, 53, 56, 58, 57, 60, 59]),
            dict(pane='b', values=[35, 48, 62, 70, 64, 52, 58, 66], color=DEEP, labels=[(3, 'RSI 70', 0, .28)])],
    marks=[('pt', 'l', 3, 70), ('pt', 'b', 3, 70)]))

SPECS['ovo'] = dict(letter='K', spec=dict(
    panes=[pane(lo=0, hi=100, n=14, ref=[(100, '100'), (50, '50'), (0, '0')])],
    series=[dict(pane='p', values=[50, 44, 36, 31, 34, 46, 58, 66, 62, 50, 40, 30, 26, 38], labels=[(3, 'RSI 31', 0, -.35), (12, 'RSI 26', 0, -.35)]),
            dict(pane='p', values=[40, 37, 34, 31, 30, 32, 36, 40, 36, 32, 28, 26, 25, 27], color=MUTED, lw=2.0),
            dict(pane='p', values=[66, 64, 62, 60, 62, 66, 72, 76, 72, 66, 62, 60, 62, 66], color=MUTED, lw=2.0)],
    texts=[(1.5, 3.05, 'upper band', 'left', MUTED), (1.5, 1.35, 'lower band', 'left', MUTED)],
    marks=[('pt', 'p', 7, 76), ('pt', 'p', 3, 31)]))

SPECS['fib'] = dict(letter='L', spec=dict(
    panes=[pane(lo=37, hi=66, n=12)],
    series=[dict(pane='p', values=[40, 43, 47, 50, 48, 47, 46, 49, 53, 57, 60, 61],
                 labels=[(0, 'A 40.00', 0, -.4), (3, 'B 50.00', 0, .28), (6, 'C 46.00', 0, -.4)])],
    levels=[dict(pane='p', value=62.18, label='target 62.18 = 46.00 + 1.618 x 10.00', dy=.15, slots=(6, 11))],
    marks=[('pt', 'p', 0, 40), ('pt', 'p', 3, 50), ('pt', 'p', 6, 46), ('pt', 'p', 11, 62.18)]))

SPECS['hor'] = dict(letter='M', spec=dict(
    panes=[pane(lo=42, hi=51.8, n=14)],
    series=[dict(pane='p', values=[44, 46, 47, 49.6, 47.5, 46, 45, 46, 47, 48, 49, 49.7, 48, 46],
                 labels=[(3, '49.60', 0, -.5), (11, '49.70', 0, -.5)])],
    levels=[dict(pane='p', value=50.0, label='resistance 50.00, the same on day 4 and day 12', dy=.15)],
    marks=[('pt', 'p', 3, 49.6), ('pt', 'p', 11, 49.7)]))

_GAP = [(46, 47, 45.6, 46.8), (46.8, 47.8, 46.5, 47.6), (47.6, 48.4, 47.2, 48.0), (48.0, 48.4, 47.8, 48.2),
        (49.6, 50.4, 49.4, 50.2), (50.2, 51.0, 50.0, 50.8), (50.8, 51.4, 50.5, 51.0), (51.0, 51.2, 49.8, 50.0),
        (50.0, 50.3, 49.5, 49.9), (49.9, 50.9, 49.7, 50.8)]
SPECS['gap'] = dict(letter='N', spec=dict(
    panes=[pane(lo=45, hi=52.2, n=10)],
    bars=[dict(pane='p', rows=_GAP, labels=[(3, 'H 48.40', -.3, -.6)])],
    levels=[dict(pane='p', value=49.4, label='top of the gap 49.40', dy=-.4, slots=(4, 9), lslot=5, color=DEEP)],
    marks=[('box', 'p', 3, 4, 48.4, 49.4), ('pt', 'p', 8, 49.5)]))

SPECS['trl'] = dict(letter='O', spec=dict(
    panes=[pane(lo=38, hi=63, n=21)],
    series=[dict(pane='p', values=[40 + d for d in range(21)], color=MUTED, lw=2.2),
            dict(pane='p', values=[40.8, 42, 42.8, 44, 44.8, 46, 46.8, 48, 48.8, 50, 50.0, 52, 52.8, 54, 54.8, 56, 56.8, 58, 58.8, 60.2, 60.0],
                 labels=[(10, 'day 10: line 50.00', 0, -.5), (20, 'day 20: line 60.00', -1.3, .45)])],
    texts=[(1.3, 3.25, 'the trendline: 40.00 plus 1.00 a day', 'left', MUTED)],
    marks=[('pt', 'p', 10, 50.0), ('pt', 'p', 20, 60.0)]))

_FD = [(49.8, 51, 49.5, 50.6), (50.6, 52, 50.2, 51.4), (50.8, 51, 50.2, 50.5), (50.5, 53, 50.4, 52.5),
       (51.8, 52, 51.2, 51.6), (51.7, 53.6, 51.5, 53.4)]
SPECS['fd'] = dict(letter='P', spec=dict(
    panes=[pane(lo=48.5, hi=55, n=6, x=(1.6, 9.2))],
    bars=[dict(pane='p', rows=_FD, labels=[(0, 'H 51', 0, .3), (1, 'H 52', 0, .3), (2, 'H 51', 0, .3), (3, 'H 53', 0, .3), (4, 'H 52', 0, .22), (5, '53.60', .6, 0)])],
    levels=[dict(pane='p', value=53.0, label='five-day high 53.00', dy=.5, slots=(3, 5), lslot=3)],
    marks=[('pt', 'p', 3.5, 53.0), ('pt', 'p', 5, 53.6)]))

# ------------------------------------------------------- 8.1 bounded and unbounded
SPECS['cmp'] = dict(letter='Q', spec=dict(
    panes=[pane(lo=0, hi=100, n=7, ref=[(100, '100'), (50, '50'), (0, '0')], x=(1.3, 8.8))],
    series=[dict(pane='p', values=[50, 58, 66, 72, 78, 82], labels=[(5, 'stock A: 82', 1.2, 0)]),
            dict(pane='p', values=[44, 48, 52, 58, 62, 64], color=MUTED, labels=[(5, 'stock B: 64', 1.2, 0)])],
    marks=[('pt', 'p', 5, 82), ('pt', 'p', 5, 64)]))

SPECS['stuck'] = dict(letter='R', spec=dict(
    panes=[pane('t', y=(2.1, 3.4), lo=48, hi=78, n=14, title='price'),
           pane('b', y=(.65, 1.8), lo=40, hi=100, n=14, ref=[(80, '80', True, DEEP)])],
    series=[dict(pane='t', values=[50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]),
            dict(pane='b', values=[55, 68, 78, 84, 88, 90, 87, 89, 91, 86, 88, 90, 85, 78], labels=[(5, '90', 0, .3)])],
    texts=[(1.2, .5, 'oscillator, above 80 for ten readings in a row', 'left', DEEP)],
    marks=[('box', 'b', 3, 12, 82, 93), ('pt', 't', 12, 72)]))

_PK = [0.4, 1.2, 2.6, 3.9, 2.0, 0.6, -0.5, 0.8, 2.4, 3.8, 1.9, 0.2, -0.8, 1.1, 2.8, 4.0, 2.2, 0.9]
SPECS['unb'] = dict(letter='S', spec=dict(
    panes=[pane(lo=-1.6, hi=5, n=18, ref=[(0, '0')])],
    series=[dict(pane='p', values=_PK, labels=[(3, '3.9', 0, .28), (9, '3.8', 0, .28), (15, '4.0', 0, .28)])],
    levels=[dict(pane='p', value=3.9, label='historical level 3.9', dy=.12, lslot=4, slots=(0, 17), color=DEEP)],
    marks=[('pt', 'p', 3, 3.9), ('pt', 'p', 9, 3.8), ('pt', 'p', 15, 4.0)]))

SPECS['unb2'] = dict(letter='T', spec=dict(
    panes=[pane('a', y=(2.1, 3.3), lo=-1, hi=5, n=18, title='stock A'),
           pane('b', y=(.7, 1.8), lo=-0.2, hi=1.0, n=18, title='stock B')],
    series=[dict(pane='a', values=_PK, labels=[(15, '4.0', 0, .28)]),
            dict(pane='b', values=[round(v * 0.2, 2) for v in _PK], labels=[(15, '0.8', 0, .28)])],
    marks=[('pt', 'a', 15, 4.0), ('pt', 'b', 15, 0.8)]))

SPECS['semi'] = dict(letter='U', spec=dict(
    panes=[pane(lo=-0.6, hi=4.4, n=12)],
    series=[dict(pane='p', values=[1.2, 2.4, 3.6, 2.0, 0.8, 0.3, 0.6, 1.8, 3.2, 2.2, 1.0, 0.4],
                 labels=[(2, '3.6', 0, .28), (5, '0.3', 0, .3)])],
    levels=[dict(pane='p', value=0.0, label='zero: the floor', dy=-.5, color=INK, dashed=False, lw=2.2)],
    marks=[('pt', 'p', 5, 0.3), ('pt', 'p', 9.4, 0.0)]))

_RAW = [-2, 1, 4, 6, 3, 0, -3, -5, -1, 2, 5, 7]
SPECS['norm'] = dict(letter='V', spec=dict(
    panes=[pane('t', y=(2.15, 3.35), lo=-7, hi=9, n=12, title='readings in points', ref=[(0, '0')]),
           pane('b', y=(.65, 1.75), lo=-10, hi=110, n=12, title='the same readings rescaled to 0 to 100', ref=[(100, '100'), (0, '0')])],
    series=[dict(pane='t', values=_RAW, labels=[(3, '6', 0, .28), (7, '-5', 0, -.4), (11, '7', 0, .28)]),
            dict(pane='b', values=[round((v + 5) / 12 * 100, 1) for v in _RAW], labels=[(3, '91.7', 0, -.4), (7, '0', 0, .3), (11, '100', 0, -.45)])],
    texts=[(1.0, .42, 'rescaled = (reading + 5) / 12 x 100;  (6 + 5) / 12 x 100 = 91.7', 'left', DEEP)],
    marks=[('pt', 't', 3, 6), ('pt', 'b', 3, 91.7)]))

SPECS['osc2'] = dict(letter='W', spec=dict(
    panes=[pane('l', x=(1.0, 4.9), y=(.9, 3.0), lo=-4.5, hi=5, n=8, title='swings around its central value', ref=[(0, 'central value 0')]),
           pane('r', x=(6.4, 10.3), y=(.9, 3.0), lo=0, hi=20, n=8, title='a running total keeps climbing')],
    series=[dict(pane='l', values=[2, -1, 3, -2, 1, -3, 2, -1]),
            dict(pane='r', values=[3, 5, 6, 9, 11, 12, 15, 18])],
    marks=[('pt', 'l', 0, 0), ('pt', 'r', 7, 18)]))

# ------------------------------------------------------------- 8.1 scale and time
_ARITH = [(9.5, 10.5, 9.4, 10.0), (11.5, 12.4, 11.2, 12.0), (13.4, 14.5, 13.2, 14.0)]
import math
_LOG = [tuple(round(math.log(v), 4) for v in row) for row in _ARITH]
SPECS['mas'] = dict(letter='X', spec=dict(
    panes=[pane('l', x=(1.5, 4.8), y=(.8, 3.0), lo=9, hi=15, n=3, title='arithmetic scale'),
           pane('r', x=(6.9, 10.2), y=(.8, 3.0), lo=round(math.log(9), 4), hi=round(math.log(15), 4), n=3, title='ratio (log) scale')],
    bars=[dict(pane='l', rows=_ARITH, labels=[(0, 'close 10', .85, 0), (1, 'close 12', .85, -.6), (2, 'close 14', .85, -.6)], half=.2),
          dict(pane='r', rows=_LOG, labels=[(0, 'close 10', .85, 0), (1, 'close 12', .85, -.6), (2, 'close 14', .85, -.6)], half=.2)],
    levels=[dict(pane='l', value=12.0, label='average 12.00', dy=.2, color=DEEP),
            dict(pane='r', value=round(math.log(12.0), 4), label='average 12.00', dy=.2, color=DEEP)],
    marks=[('xy', 3.65, 1.9), ('xy', 9.1, 2.04)]))

_FDL = [tuple(round(math.log(v), 4) for v in row) for row in _FD]
SPECS['fds'] = dict(letter='Y', spec=dict(
    panes=[pane('l', x=(1.2, 5.0), y=(.8, 3.0), lo=48.5, hi=55, n=6, title='arithmetic scale'),
           pane('r', x=(6.6, 10.4), y=(.8, 3.0), lo=round(math.log(48.5), 4), hi=round(math.log(55), 4), n=6, title='ratio (log) scale')],
    bars=[dict(pane='l', rows=_FD, half=.1), dict(pane='r', rows=_FDL, half=.1)],
    levels=[dict(pane='l', value=53.0, label='53.00', dy=.15, color=DEEP, slots=(3, 5)),
            dict(pane='r', value=round(math.log(53.0), 4), label='53.00', dy=.15, color=DEEP, slots=(3, 5))],
    texts=[(3.1, .5, 'the level is 53.00 on both', 'center', DEEP)],
    marks=[('xy', 4.7, 2.32), ('xy', 10.1, 2.36)]))

SPECS['sta'] = dict(letter='Z', spec=dict(
    panes=[pane(lo=42, hi=66, n=10)],
    series=[dict(pane='p', values=[44, 46, 47, 49.6, 48, 47, 49, 49.8, 48.4, 47.6])],
    levels=[dict(pane='p', value=50.0, label='prior resistance 50.00, day 1 to day 10', dy=.12, color=DEEP),
            dict(pane='p', value=62.18, label='Fibonacci target 62.18, day 1 to day 10', dy=.12, color=DEEP)],
    marks=[('xy', 10.1, 1.62), ('xy', 10.1, 2.86)]))

_DC = [44, 46, 45.5, 47.5, 49, 48, 51, 50, 52.5, 51.5]
_DMA = [None, None] + [round(sum(_DC[i - 2:i + 1]) / 3, 2) for i in range(2, 10)]
_DTL = [round(45.5 + (5 / 6) * (i - 2), 2) for i in range(10)]
SPECS['dyn'] = dict(letter='AA', spec=dict(
    panes=[pane(lo=42, hi=56, n=10)],
    series=[dict(pane='p', values=_DC, color=INK),
            dict(pane='p', values=_DMA, color=DEEP, lw=2.4),
            dict(pane='p', values=_DTL, color=MUTED, lw=2.0)],
    texts=[(1.4, 3.3, 'black: price   green: 3-day moving average   grey: trendline through two troughs', 'left', DEEP),
           (1.4, 3.0, 'moving average, days 3, 6, 9: 45.17, 48.17, 51.17', 'left', DEEP),
           (1.4, 2.7, 'trendline, days 3, 6, 9: 45.50, 48.00, 50.50', 'left', MUTED)],
    marks=[('pt', 'p', 2, 45.17), ('pt', 'p', 5, 48.17), ('pt', 'p', 8, 51.17)]))

# ----------------------------------------------------- the four kinds in one sketch
def _four():
    xs = [(0.9, 3.0), (3.5, 5.6), (6.1, 8.2), (8.7, 10.8)]
    panes = [pane('a', x=xs[0], y=(.9, 3.0), lo=36, hi=66, n=6, title='a formula'),
             pane('b', x=xs[1], y=(.9, 3.0), lo=44, hi=52, n=6, title='a level'),
             pane('c', x=xs[2], y=(.9, 3.0), lo=38, hi=52, n=6, title='a sloping line'),
             pane('d', x=xs[3], y=(.9, 3.0), lo=48.5, hi=54.5, n=6, title='a rule on bars')]
    return dict(
        panes=panes,
        series=[dict(pane='a', values=[40, 44, 50, 47, 46, 51], labels=[(0, 'A', 0, -.4), (2, 'B', -.3, .1), (4, 'C', 0, -.4)]),
                dict(pane='b', values=[46, 48, 49.6, 47.5, 46.5, 49.7]),
                dict(pane='c', values=[41, 43, 44.5, 46.5, 48, 50.2])],
        bars=[dict(pane='d', rows=_FD, half=.08)],
        levels=[dict(pane='a', value=62.18, dashed=True, color=DEEP, label='C + 1.618\nx AB', dy=-.6, lslot=2),
                dict(pane='b', value=49.6, dashed=True, color=DEEP, slots=(2, 5), label='prior peak', dy=.12, lslot=2),
                dict(pane='d', value=53.0, dashed=True, color=DEEP, slots=(3, 5))],
        texts=[(5.0 + 1.2, 1.55, '', 'center')] if False else [],
        marks=[('box', 'a', 0, 5, 36, 66), ('box', 'b', 0, 5, 44, 52), ('box', 'c', 0, 5, 38, 52), ('box', 'd', 0, 5, 48.5, 54.5)])


_FSPEC = _four()
_FSPEC['series'].append(dict(pane='c', values=[40.0 + 2 * k for k in range(6)], color=MUTED, lw=2.2))
SPECS['four'] = dict(letter='AB', caption='The sketches are ours, drawn to show the idea.', spec=_FSPEC)


# ============================================================== 8.2 charts
def _avg3(v):
    return [None if i < 2 else round(sum(v[i - 2:i + 1]) / 3, 2) for i in range(len(v))]


def _cross(a, b, lo=0, rising=True):
    """The first slot pair where series a crosses b, as (slot, value) by straight lines."""
    for i in range(max(lo, 0), len(a) - 1):
        if None in (a[i], b[i], a[i + 1], b[i + 1]):
            continue
        d0, d1 = a[i] - b[i], a[i + 1] - b[i + 1]
        if (d0 < 0 <= d1) if rising else (d0 > 0 >= d1):
            t = d0 / (d0 - d1)
            return round(i + t, 3), round(a[i] + t * (a[i + 1] - a[i]), 3)
    raise ValueError('no crossing')


_TP = [44, 45.5, 47, 46, 47.5, 48.5, 49.2, 49.6, 50.8]
_TO = [38, 42, 46, 50, 56, 61, 64, 66, 70]
SPECS['trig'] = dict(letter='AC', spec=dict(
    panes=[pane('t', y=(2.0, 3.4), lo=43, hi=52, n=9, title='price'), pane('b', y=(.65, 1.75), lo=0, hi=100, n=9, title='oscillator', ref=[(50, '50')])],
    series=[dict(pane='t', values=_TP, labels=[(7, '49.60', 0, -.5), (8, '50.80', 0, .3)]),
            dict(pane='b', values=_TO, labels=[(3, '50', 0, -.45)])],
    levels=[dict(pane='t', value=50.0, label='resistance 50.00', dy=.12, slots=(0, 8), lslot=0)],
    marks=[('pt', 'b', 3, 50), ('pt', 't', 8, 50.8)]))

SPECS['lev'] = dict(letter='AD', spec=dict(
    panes=[pane(lo=0, hi=100, n=5, x=(1.6, 7.4))],
    series=[dict(pane='p', values=[82, 71, 48, 27, 19], labels=[(0, '82', .1, .3), (1, '71', 0, -.45), (2, '48', 0, .3), (3, '27', .6, .3), (4, '19', 0, -.5)])],
    levels=[dict(pane='p', value=v, label=t, side='right', dy=-.1, slots=(0, 4)) for v, t in ((80, '80: stochastic overbought'), (70, '70: RSI overbought'), (30, '30: RSI oversold'), (20, '20: stochastic oversold'))],
    marks=[('pt', 'p', 0, 82), ('pt', 'p', 1, 71), ('pt', 'p', 3, 27), ('pt', 'p', 4, 19)]))

_SV = [50, 62, 74, 86, 92, 84, 62, 40, 24, 12, 22, 40]
SPECS['def'] = dict(letter='AE', spec=dict(
    panes=[pane('s', y=(1.95, 3.4), lo=0, hi=100, n=12, title='a stochastic of ours', x=(1.3, 8.2)),
           pane('r', y=(.6, 1.7), lo=0, hi=100, n=12, title='an RSI of ours', x=(1.3, 8.2))],
    series=[dict(pane='s', values=_SV), dict(pane='r', values=[48, 55, 64, 72, 68, 60, 50, 38, 28, 34, 44, 52])],
    levels=[dict(pane='s', value=90, label='shifted: 90', side='right', dy=-.1, color=DEEP),
            dict(pane='s', value=80, label='default: 80', side='right', dy=-.4, color=MUTED, tcolor=MUTED),
            dict(pane='s', value=30, label='shifted: 30', side='right', dy=-.1, color=DEEP),
            dict(pane='s', value=20, label='default: 20', side='right', dy=-.4, color=MUTED, tcolor=MUTED),
            dict(pane='r', value=70, label='RSI: 70', side='right', dy=-.1, color=DEEP),
            dict(pane='r', value=30, label='RSI: 30', side='right', dy=-.1, color=DEEP)],
    marks=[('pt', 's', 4, 92), ('pt', 's', 9, 12), ('pt', 'r', 3, 72)]))

SPECS['sd'] = dict(letter='AF', spec=dict(
    panes=[pane(lo=-290, hi=290, n=12, x=(1.4, 8.4), ref=[(0, '0')])],
    series=[dict(pane='p', values=[20, 90, 150, 210, 120, 30, -60, -140, -240, -150, -40, 40], labels=[(3, '210', 0, .28), (8, '-240', 0, -.45)])],
    levels=[dict(pane='p', value=v, label=t, side='right', dy=-.1, slots=(0, 11), color=DEEP) for v, t in ((200, '+200: two sigma'), (100, '+100: one sigma'), (-100, '-100: one sigma'), (-200, '-200: two sigma'))],
    marks=[('pt', 'p', 3, 210), ('pt', 'p', 8, -240)]))

_MA = [40, 44, 48, 56, 62, 58, 52, 46]
_MB = [36, 42, 47, 58, 67, 60, 51, 43]
_c1 = _cross(_MA, [50] * 8); _c2 = _cross(_MA, [50] * 8, 3, rising=False)
SPECS['mc'] = dict(letter='AG', spec=dict(
    panes=[pane('c', y=(2.7, 3.25), lo=18, hi=33, n=8, title='the eight closes'),
           pane('a', y=(1.6, 2.4), lo=20, hi=80, n=8, title='oscillator A', ref=[(50, '50')]),
           pane('b', y=(.5, 1.3), lo=20, hi=80, n=8, title='oscillator B', ref=[(50, '50')])],
    series=[dict(pane='c', values=[20, 22, 24, 28, 31, 29, 26, 23], color=MUTED), dict(pane='a', values=_MA), dict(pane='b', values=_MB)],
    marks=[('pt', 'a', _c1[0], 50), ('pt', 'b', _cross(_MB, [50] * 8)[0], 50)]))

_SO = [44, 36, 26, 22, 28, 38, 50, 58, 64, 60, 52, 46]
_SS = _avg3(_SO)
_x1 = _cross(_SO, _SS, 0, True); _x2 = _cross(_SO, _SS, 6, False)
SPECS['sig2'] = dict(letter='AH', spec=dict(
    panes=[pane(lo=0, hi=100, n=12, ref=[(100, '100'), (70, '70 (overbought)'), (50, '50'), (30, '30 (oversold)'), (0, '0')], x=(1.3, 8.6))],
    series=[dict(pane='p', values=_SO), dict(pane='p', values=_SS, color='#E09B00', lw=2.8)],
    texts=[(1.4, .45, 'black: oscillator   gold: its signal line (average of three readings)', 'left', DEEP)],
    marks=[('pt', 'p', _x1[0], _x1[1]), ('pt', 'p', _x2[0], _x2[1])]))


def _div(letter, price, osc, pslots, oslots, plabel, olabel, plo, phi):
    pv = [price[i] for i in pslots]; ov = [osc[i] for i in oslots]
    mid = lambda a, b: (a + b) / 2
    return dict(letter=letter, spec=dict(
        panes=[pane('t', y=(2.05, 3.4), lo=plo, hi=phi, n=9, title='price'), pane('b', y=(.6, 1.7), lo=0, hi=100, n=9, title='oscillator')],
        series=[dict(pane='t', values=price, labels=[(pslots[0], f'{pv[0]:g}', 0, .3 if plabel == 'peak' else -.45), (pslots[1], f'{pv[1]:g}', 0, .3 if plabel == 'peak' else -.45)]),
                dict(pane='b', values=osc, labels=[(oslots[0], f'{ov[0]:g}', 0, .3 if olabel == 'peak' else -.45), (oslots[1], f'{ov[1]:g}', 0, .3 if olabel == 'peak' else -.45)])],
        segs=[dict(pane='t', a=(pslots[0], pv[0]), b=(pslots[1], pv[1]), color=DEEP, dashed=False),
              dict(pane='b', a=(oslots[0], ov[0]), b=(oslots[1], ov[1]), color=DEEP, dashed=False)],
        marks=[('pt', 't', mid(*pslots), mid(*pv)), ('pt', 'b', mid(*oslots), mid(*ov))]))


SPECS['d1'] = _div('AI', [50, 47, 44, 48, 51, 46, 41, 46, 49], [60, 40, 22, 45, 58, 42, 30, 48, 55], (2, 6), (2, 6), 'trough', 'trough', 38, 54)
SPECS['d2'] = _div('AJ', [52, 56, 60, 55, 52, 58, 63, 57, 54], [40, 60, 78, 58, 45, 62, 66, 50, 42], (2, 6), (2, 6), 'peak', 'peak', 50, 66)
SPECS['d3'] = _div('AK', [50, 47, 44, 48, 51, 48, 46, 50, 53], [58, 40, 30, 46, 58, 38, 22, 44, 56], (2, 6), (2, 6), 'trough', 'trough', 41, 56)
SPECS['d4'] = _div('AL', [52, 56, 63, 57, 52, 56, 60, 55, 52], [40, 56, 66, 52, 44, 60, 78, 52, 42], (2, 6), (2, 6), 'peak', 'peak', 50, 66)


def _geo(letter, line, osc, mark):
    return dict(letter=letter, spec=dict(
        panes=[pane(lo=15, hi=92, n=10, x=(1.4, 9.4))],
        series=[dict(pane='p', values=line, color=MUTED, lw=2.4), dict(pane='p', values=osc)],
        texts=[(1.5, 3.4, 'black: oscillator   grey: trendline drawn on it', 'left', DEEP)],
        marks=[('pt', 'p', mark[0], mark[1])]))


SPECS['g1'] = _geo('AM', [88 - 4 * i for i in range(10)], [60, 58, 62, 64, 66, 68, 66, 70, 72, 74], (5, 68))
SPECS['g2'] = _geo('AN', [82 - 3 * i for i in range(10)], [40, 44, 48, 52, 56, 60, 62, 60, 54, 48], (6, 62))
SPECS['g3'] = _geo('AO', [22 + 4 * i for i in range(10)], [62, 56, 50, 44, 40, 34, 30, 26, 24, 22], (4.2, 38.8))
SPECS['g4'] = _geo('AP', [18 + 4 * i for i in range(10)], [70, 64, 58, 52, 48, 46, 44, 48, 54, 60], (6, 44))

_NO = [44, 48, 52, 58, 62, 56, 54, 53, 57, 60]
_NM = [48, 48, 49, 51, 53, 54, 53, 53, 54, 55]
SPECS['num'] = dict(letter='AQ', spec=dict(
    panes=[pane(lo=20, hi=80, n=10, x=(1.4, 9.4))],
    series=[dict(pane='p', values=_NO, labels=[(2, '52', 0, .3), (7, '53', 0, -.45)]), dict(pane='p', values=_NM, color=DEEP, lw=2.4, labels=[(1, '48', 0, -.45)])],
    texts=[(1.5, 3.4, 'black: oscillator   green: its own moving average', 'left', DEEP)],
    marks=[('pt', 'p', 1.2, 48), ('pt', 'p', 7, 53)]))

SPECS['hosc'] = dict(letter='AR', spec=dict(
    panes=[pane(lo=20, hi=84, n=13, x=(1.4, 8.4))],
    series=[dict(pane='p', values=[56, 44, 30, 46, 62, 70, 58, 44, 32, 46, 62, 72, 76],
                 labels=[(2, 'prior trough 30', 0, -.45), (5, 'prior peak 70', 0, .3), (8, '32', 0, -.45), (12, '76', 0, .3)])],
    levels=[dict(pane='p', value=70, label='resistance 70', side='right', dy=-.1, color=DEEP),
            dict(pane='p', value=30, label='support 30', side='right', dy=-.1, color=DEEP)],
    marks=[('pt', 'p', 10.8, 70), ('pt', 'p', 8, 32)]))


SPECS['od'] = dict(letter='AT', spec=dict(
    panes=[pane('a', y=(2.05, 3.4), lo=0, hi=100, n=9, title='oscillator A', ref=[(50, '50')]),
           pane('b', y=(.6, 1.7), lo=0, hi=100, n=9, title='oscillator B', ref=[(50, '50')])],
    series=[dict(pane='a', values=[40, 55, 66, 55, 46, 58, 76, 60, 48], labels=[(2, '66', 0, .3), (6, '76', 0, .3)]),
            dict(pane='b', values=[42, 58, 80, 62, 50, 60, 66, 58, 46], labels=[(2, '80', 0, .3), (6, '66', 0, .3)])],
    marks=[('pt', 'a', 6, 76), ('pt', 'b', 6, 66)]))

_PA = [48, 50, 54, 52, 49, 51, 55, 58, 61]
SPECS['pc'] = dict(letter='AU', spec=dict(
    panes=[pane('a', x=(0.9, 3.1), y=(.9, 3.0), lo=44, hi=54, n=7, title='prior resistance'),
           pane('b', x=(3.7, 5.9), y=(.9, 3.0), lo=44, hi=56, n=7, title='trendline'),
           pane('c', x=(6.5, 8.7), y=(.9, 3.0), lo=44, hi=56, n=7, title='moving average')],
    series=[dict(pane='a', values=[45, 47, 49.6, 48, 49, 50.4, 52]),
            dict(pane='b', values=[47.5, 49.5, 49, 50.5, 50.5, 48.5, 47]),
            dict(pane='b', values=[46, 47, 48, 49, 50, 51, 52], color=MUTED, lw=2.2),
            dict(pane='c', values=[46, 48, 47, 49, 51, 50, 53]),
            dict(pane='c', values=[47, 47.3, 47.6, 48.0, 48.8, 49.6, 50.6], color=DEEP, lw=2.2)],
    levels=[dict(pane='a', value=50.0, color=DEEP, slots=(0, 6))],
    marks=[('pt', 'a', 5.0, 50.4), ('pt', 'b', 4.17, 50.2), ('pt', 'c', 3.4, 49.4)]))

SPECS['pv'] = dict(letter='AV', spec=dict(
    panes=[pane('a', y=(2.05, 3.4), lo=0, hi=100, n=10, title='a price-based oscillator', ref=[(50, '50')]),
           pane('b', y=(.6, 1.7), lo=0, hi=100, n=10, title='a volume-based oscillator', ref=[(50, '50')])],
    series=[dict(pane='a', values=[38, 44, 52, 60, 66, 60, 52, 44, 40, 46]),
            dict(pane='b', values=[56, 60, 62, 64, 58, 50, 40, 34, 38, 44])],
    marks=[('pt', 'a', 2.2, 50.0), ('pt', 'b', 5.0, 50.0)]))
