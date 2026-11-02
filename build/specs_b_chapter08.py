"""Plain-data chart specs for Chapter 8's second class (8.3 to 8.8). Every number is ours, invented for teaching.

Same form as specs_chapter08: panes, series, bars, levels, texts, segs and marks, drawn by
oscillatorcharts_chapter08.paint_spec. Letters continue after Part A's AX. Anything computed
(an average, a crossing, an RSI) is computed here from the plotted values, so the chart and the
sentence that quotes it cannot drift apart.
"""
import math

from specs_chapter08 import DEEP, INK, MUTED, _avg3, _cross, pane

SPECS_B = {}
GOLD = '#E09B00'


def X(p, s):
    return p['x'][0] + (p['x'][1] - p['x'][0]) * (s + .5) / p['n']


def Y(p, v):
    return p['y'][0] + (v - p['lo']) / (p['hi'] - p['lo']) * (p['y'][1] - p['y'][0])


# ============================================================ 8.3 the half cycle
def _wave(n, lo=35, hi=72):
    mid, amp = (lo + hi) / 2, (hi - lo) / 2
    return [round(mid - amp * math.cos(2 * math.pi * k / n), 2) for k in range(n + 1)]


def _cycle(letter, n, half, lines, caption):
    p = pane(x=(1.2, 10.4), y=(.7, 3.3), lo=-25, hi=105, n=n + 1)
    w = _wave(n)
    texts = [(1.3, 3.25, lines[0], 'left', DEEP)] + [(1.3, 2.97, t, 'left', DEEP) for t in lines[1:]]
    texts += [(X(p, n / 2), Y(p, 40), f'one full cycle, N = {n} bars', 'center', DEEP),
              (X(p, half / 2), Y(p, -14), f'{half} bars: half the cycle, our lookback', 'center', DEEP)]
    return dict(letter=letter, caption=caption, spec=dict(
        panes=[p],
        series=[dict(pane='p', values=w)],
        segs=[dict(pane='p', a=(0, 18), b=(n, 18), color=DEEP, dashed=False),
              dict(pane='p', a=(0, 2), b=(half, 2), color=GOLD, dashed=False)],
        texts=texts,
        marks=[('pt', 'p', 0, w[0]), ('pt', 'p', n, w[n]), ('pt', 'p', half, 2)]))


SPECS_B['cy1'] = _cycle('AY', 76, 39, ['(76 + 1) / 2 = 38.5, rounded up to 39'], 'The cycle is ours, made up to show the idea.')
SPECS_B['cy2'] = _cycle('AZ', 75, 38, ['(75 / 2) + 1 = 38.5, rounded down to 38', '(2 x 75 + 3) / 4 = 38.25, rounded to 38'],
                        'The cycle is ours, made up to show the idea.')

SPECS_B['t3'] = dict(letter='BA', caption="The table is ours, from Lim's formulas (p. 252).", spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.4, 6.4, 9.6), header=('formula for the half cycle', 'worked on N = 75', 'half cycle'), top=3.3, step=.7,
               rows=(('(N + 1) / 2', '(75 + 1) / 2 = 38', '38'),
                     ('(N / 2) + 1, round down', '75 / 2 + 1 = 38.5, down', '38'),
                     ('(2N + 3) / 4, round to nearest', '(150 + 3) / 4 = 38.25, nearest', '38')))))

# ------------------------------------------------------------ 8.3 several timeframes
def _sm(v, n):
    out = []
    for i in range(len(v)):
        w = v[max(0, i - n + 1):i + 1]
        out.append(round(sum(w) / len(w), 1))
    return out


_FAST = [48, 62, 55, 70, 58, 66, 52, 60, 46, 58, 44, 54, 62, 70, 60, 68, 76, 64, 72, 66]
_MED = _sm(_FAST, 3)
_SLOW = _sm(_FAST, 8)
SPECS_B['mtf'] = dict(letter='BB', spec=dict(
    panes=[pane('a', y=(2.8, 3.4), lo=40, hi=80, n=20, title='RSI on the 5 minute bars'),
           pane('b', y=(1.75, 2.35), lo=40, hi=80, n=20, title='RSI on the 15 minute bars'),
           pane('c', y=(.7, 1.3), lo=40, hi=80, n=20, title='RSI on the 1 hour bars')],
    series=[dict(pane='a', values=_FAST), dict(pane='b', values=_MED, color=DEEP), dict(pane='c', values=_SLOW, color=GOLD)],
    marks=[('pt', 'a', 10, _FAST[10]), ('pt', 'b', 10, _MED[10]), ('pt', 'c', 10, _SLOW[10])]))

SPECS_B['mf'] = dict(letter='BC', caption='The table is ours, from the book\'s own numbers (p. 253).', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.2, 5.4, 8.9), header=('indicator timeframe', 'chart timeframe', 'MF = indicator / chart'), top=3.3, step=.7,
               rows=(('5 minute', '5 minute', '5 / 5 = 1'),
                     ('15 minute', '5 minute', '15 / 5 = 3'),
                     ('1 hour = 60 minutes', '5 minute', '60 / 5 = 12')))))


def _rsi(closes, n):
    out = [None] * len(closes)
    for i in range(n, len(closes)):
        ch = [closes[j] - closes[j - 1] for j in range(i - n + 1, i + 1)]
        g = sum(c for c in ch if c > 0) / n
        l = sum(-c for c in ch if c < 0) / n
        out[i] = round(100 * g / (g + l), 1) if g + l else 50.0
    return out


def _closes(n=96):
    v, out = 50.0, []
    for k in range(n):
        v += 1.6 * math.sin(k / 3.1) + .9 * math.sin(k / 1.3) + .25 * math.sin(k / 11)
        out.append(round(v, 2))
    return out


_CL = _closes()
_R14, _R42 = _rsi(_CL, 14), _rsi(_CL, 42)
_hi14 = max(range(42, 96), key=lambda i: _R14[i])
SPECS_B['rsi42'] = dict(letter='BD', caption='The closes are ours, made up to show the idea. Both lines use plain averages of gains and losses.', spec=dict(
    panes=[pane('p', y=(.6, 3.0), lo=0, hi=100, n=96, x=(1.3, 10.3), ref=[(100, '100'), (50, '50'), (0, '0')])],
    series=[dict(pane='p', values=_R14, lw=1.8), dict(pane='p', values=_R42, color=GOLD, lw=3.4)],
    texts=[(1.45, 3.3, 'black: 14 period RSI   gold: 42 period RSI, the same closes', 'left', DEEP)],
    marks=[('pt', 'p', _hi14, _R14[_hi14]), ('pt', 'p', _hi14, _R42[_hi14])]))

SPECS_B['mfm'] = dict(letter='BE', caption='The table is ours: the book\'s method (p. 253) on the 15 minute timeframe.', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.2, 5.6, 9.3), header=('setting', 'on its own timeframe', 'times MF = 3'), top=3.3, step=.62,
               rows=(('MACD fast average', '12', '12 x 3 = 36'),
                     ('MACD slow average', '26', '26 x 3 = 78'),
                     ('MACD signal line', '9', '9 x 3 = 27'),
                     ('moving average, book (p. 253), MF = 12', '20', '20 x 12 = 240')))))

SPECS_B['rq7'] = dict(letter='BF', caption='The table is ours, worked by the book\'s method (p. 253). The book does not print these numbers.', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.0, 5.2, 7.7, 10.0), header=('15 minute chart', 'MACD fast', 'slow', 'signal'), top=3.3, step=.62,
               rows=(('own timeframe', '12', '26', '9'),
                     ('hourly: MF = 60 / 15 = 4', '12 x 4 = 48', '26 x 4 = 104', '9 x 4 = 36'),
                     ('4 hour: MF = 240 / 15 = 16', '12 x 16 = 192', '26 x 16 = 416', '9 x 16 = 144')))))

# ---------------------------------------------------------------- 8.3 lagging
_LP = [50, 52, 54, 56, 58, 60, 62, 61, 59, 57, 55]
_LO = [round(sum(_LP[max(0, i - 3):i + 1]) / len(_LP[max(0, i - 3):i + 1]), 2) for i in range(len(_LP))]
SPECS_B['lag'] = dict(letter='BG', spec=dict(
    panes=[pane('t', y=(2.1, 3.4), lo=46, hi=66, n=11, title='price', x=(1.3, 9.5)),
           pane('b', y=(.6, 1.75), lo=46, hi=66, n=11, title='our line derived from price: the average of the last four closes', x=(1.3, 9.5))],
    series=[dict(pane='t', values=_LP, labels=[(6, '62.00', 0, .3)]),
            dict(pane='b', values=_LO, labels=[(8, f'{_LO[8]:.2f}', 0, .3)])],
    marks=[('pt', 't', 6, 62), ('pt', 'b', 8, _LO[8])]))

SPECS_B['ldt'] = dict(letter='BH', caption='The table is ours, from Lim\'s list (p. 253).', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(3.3,), header=('leads price (Lim)',), top=3.4, step=.55,
               rows=(('divergence',), ('an early momentum reversal',), ('horizontally based overlays',),
                     ('geometrically based overlays',), ('Fibonacci levels',))),
    texts=[(8.2, 3.4, 'does not lead (Lim)', 'center', DEEP), (8.2, 2.85, 'moving averages', 'center', INK)]))

# =============================================================== 8.4 input data
_RS = [44, 52, 60, 68, 72, 64, 56, 48, 42, 50, 62, 70]
_SRn = 5
_SR = [None] * (_SRn - 1) + [round((_RS[i] - min(_RS[i - _SRn + 1:i + 1])) / (max(_RS[i - _SRn + 1:i + 1]) - min(_RS[i - _SRn + 1:i + 1])), 2) for i in range(_SRn - 1, len(_RS))]
SPECS_B['srf'] = dict(letter='BI', spec=dict(
    panes=[pane('t', y=(2.15, 3.4), lo=36, hi=92, n=12, title='RSI of ours, n = 5 readings in the window', x=(1.3, 9.5)),
           pane('b', y=(.6, 1.75), lo=-.1, hi=1.1, n=12, title='the stochastic fraction on those RSI readings, 0 to 1', x=(1.3, 9.5), ref=[(1, '1.00'), (0, '0.00')])],
    series=[dict(pane='t', values=_RS, labels=[(4, '72', 0, .3), (8, '42', 0, .28)]),
            dict(pane='b', values=_SR)],
    marks=[('pt', 't', 4, 72), ('pt', 'b', 4, 1.0), ('pt', 'b', 8, 0.0)]))

_RF = [40, 55, 70, 60, 50]
SPECS_B['srw'] = dict(letter='BJ', spec=dict(
    panes=[pane(lo=30, hi=80, n=5, x=(1.6, 7.6))],
    series=[dict(pane='p', values=_RF, labels=[(0, '40', 0, -.45), (1, '55', 0, .28), (2, '70', 0, .28), (3, '60', 0, .28), (4, '50', 0, .28)])],
    levels=[dict(pane='p', value=70, label='highest RSI of the 5: 70', dy=-.1, side='right', slots=(0, 4)),
            dict(pane='p', value=40, label='lowest RSI of the 5: 40', dy=-.1, side='right', slots=(0, 4), color=DEEP)],
    marks=[('pt', 'p', 2, 70), ('pt', 'p', 0, 40), ('pt', 'p', 4, 50)]))

# the data drop-off
_P1 = [7, 4, 3, 3, 2, 4, 5, 4]
_P2 = [9, 4, 3, 3, 2, 4, 5, 4]


def _drop(letter, prices, a1, a2, note):
    return dict(letter=letter, spec=dict(
        panes=[pane(y=(.8, 2.75), lo=0, hi=11, n=8, x=(1.5, 9.5))],
        series=[dict(pane='p', values=prices, labels=[(i, f'${v}', 0, .3 if v >= 4 else -.45) for i, v in enumerate(prices)])],
        segs=[dict(pane='p', a=(0, a1), b=(6, a1), color=DEEP, dashed=False),
              dict(pane='p', a=(1, a2), b=(7, a2), color=GOLD, dashed=False)],
        texts=[(1.5, 3.42, f'first window: the first seven prices, average ${a1:.2f}', 'left', DEEP),
               (1.5, 3.12, f'next window: drop the first, add the new $4, average ${a2:.2f}', 'left', GOLD)],
        marks=[('pt', 'p', 0, prices[0]), ('pt', 'p', 7, prices[7]), ('pt', 'p', 6, a1), ('pt', 'p', 7, a2)]))


SPECS_B['dr1'] = _drop('BK', _P1, round(sum(_P1[:7]) / 7, 2), round(sum(_P1[1:]) / 7, 2), 'the average falls from $4.00 to $3.57')
SPECS_B['dr2'] = _drop('BL', _P2, round(sum(_P2[:7]) / 7, 2), round(sum(_P2[1:]) / 7, 2), 'the average falls from $4.29 to $3.57')

_P14 = [9, 4, 3, 3, 2, 4, 5, 4, 3, 4, 3, 5, 4, 4, 4]
SPECS_B['dr3'] = dict(letter='BM', spec=dict(
    panes=[pane(y=(.8, 2.75), lo=0, hi=11, n=15, x=(1.3, 9.9))],
    series=[dict(pane='p', values=_P14, labels=[(0, '$9', 0, .3), (14, '$4', 0, -.45)])],
    segs=[dict(pane='p', a=(0, round(sum(_P14[:14]) / 14, 2)), b=(13, round(sum(_P14[:14]) / 14, 2)), color=DEEP, dashed=False),
          dict(pane='p', a=(1, round(sum(_P14[1:]) / 14, 2)), b=(14, round(sum(_P14[1:]) / 14, 2)), color=GOLD, dashed=False)],
    texts=[(1.4, 3.42, f'first window: the first 14 prices, average ${sum(_P14[:14]) / 14:.2f}', 'left', DEEP),
           (1.4, 3.12, f'next window: drop the $9, add the new $4, average ${sum(_P14[1:]) / 14:.2f}', 'left', GOLD)],
    marks=[('pt', 'p', 0, 9), ('pt', 'p', 14, 4), ('pt', 'p', 13, round(sum(_P14[:14]) / 14, 2)), ('pt', 'p', 14, round(sum(_P14[1:]) / 14, 2))]))

# ============================================================ 8.5 trend trading
_TPU = [44, 46, 48, 50, 52, 51, 49, 47.5, 47, 48.5, 51, 53, 55, 57]
_TOU = [44, 56, 66, 76, 82, 68, 50, 32, 22, 38, 58, 72, 82, 86]
_TSU = _avg3(_TOU)
_xu = _cross(_TOU, _TSU, 6, True)   # the oscillator crossing back above its signal line


def _trend(letter, up):
    price = _TPU if up else [100 - (v - 44) * 1.0 + 0 for v in _TPU]
    osc = _TOU if up else [100 - v for v in _TOU]
    sig = _avg3(osc)
    cx = _cross(osc, sig, 6, up)
    eq = _cross(osc, [50] * len(osc), 6, up)
    pl, ph = (42, 59) if up else (min(price) - 2, max(price) + 2)
    tl = [(0.0, 'oversold: 30' if up else 'overbought: 70')]
    lvl = 30 if up else 70
    return dict(letter=letter, spec=dict(
        panes=[pane('t', y=(2.35, 3.4), lo=pl, hi=ph, n=14, x=(1.3, 8.4), title='price: ' + ('an uptrend with a pullback' if up else 'a downtrend with a bounce')),
               pane('b', y=(.45, 1.95), lo=0, hi=100, n=14, title='oscillator and its signal line', x=(1.3, 8.4), ref=[(50, '50')])],
        series=[dict(pane='t', values=price), dict(pane='b', values=osc), dict(pane='b', values=sig, color=GOLD, lw=2.8)],
        levels=[dict(pane='b', value=lvl, label=tl[0][1], dy=-.35 if up else .1, side='right', color=DEEP, slots=(0, 13))],
        marks=[('pt', 't', 4 if up else 4, price[4]),
               ('pt', 'b', 8 if up else 8, osc[8]),
               ('pt', 'b', cx[0], cx[1])]))


SPECS_B['tru'] = _trend('BN', True)
SPECS_B['trd'] = _trend('BO', False)


# ============================================================== 8.6 window oscillators
# momentum turns before price: our momentum is the one bar price change, the simplest case of the book's MOM
_MP = [50, 52, 54, 56, 57.5, 58.5, 59.2, 59.7, 60.0]
_MM = [None] + [round(_MP[i] - _MP[i - 1], 2) for i in range(1, len(_MP))]
SPECS_B['mo'] = dict(letter='BP', spec=dict(
    panes=[pane('t', y=(2.1, 3.4), lo=48, hi=62, n=9, title='price', x=(1.3, 9.5)),
           pane('b', y=(.6, 1.75), lo=0, hi=2.8, n=9, title='momentum: the price change over one bar', x=(1.3, 9.5), ref=[(0, '0')])],
    series=[dict(pane='t', values=_MP, labels=[(8, '60.00', 0, .3)]),
            dict(pane='b', values=_MM, labels=[(3, '2.0', 0, .3), (4, '1.5', .2, .3), (8, '0.3', 0, .3)])],
    marks=[('pt', 't', 8, 60.0), ('pt', 'b', 3, 2.0)]))

# ROC and MOM
SPECS_B['rcp'] = dict(letter='BQ', spec=dict(
    panes=[pane(y=(.8, 3.0), lo=96, hi=114, n=11, x=(1.4, 7.4))],
    series=[dict(pane='p', values=[100 + i for i in range(11)], labels=[(0, '$100', 0, -.45), (10, '$110', 0, .3)])],
    levels=[dict(pane='p', value=100, label='price N = 10 periods back', dy=-.1, side='right', slots=(0, 10))],
    texts=[(1.5, 3.4, 'ROC = (110 - 100) / 100 x 100 = 10 percent', 'left', DEEP)],
    marks=[('pt', 'p', 10, 110), ('pt', 'p', 0, 100)]))

SPECS_B['rcw'] = dict(letter='BR', spec=dict(
    panes=[pane('l', x=(1.5, 4.8), y=(.8, 2.6), lo=0, hi=16, n=2, title='$1 to $11 over N periods'),
           pane('r', x=(6.8, 10.1), y=(.8, 2.6), lo=90, hi=120, n=2, title='$100 to $110 over N periods')],
    series=[dict(pane='l', values=[1, 11], labels=[(0, '$1', 0, -.45), (1, '$11', 0, .3)]),
            dict(pane='r', values=[100, 110], labels=[(0, '$100', 0, -.45), (1, '$110', 0, .3)])],
    texts=[(3.15, 3.35, '($11 - $1) / $1 x 100 = 1000 percent', 'center', DEEP),
           (8.45, 3.35, '($110 - $100) / $100 x 100 = 10 percent', 'center', DEEP)],
    marks=[('pt', 'l', 0, 1), ('pt', 'l', 1, 11), ('pt', 'r', 0, 100), ('pt', 'r', 1, 110)]))


def _roc_chart(letter, prices, roc, labels_roc, ytop, kind):
    return dict(letter=letter, spec=dict(
        panes=[pane('t', y=(2.1, 3.4), lo=90, hi=ytop, n=4, title='price, measured every 10 periods', x=(1.4, 8.8)),
               pane('b', y=(.6, 1.75), lo=0, hi=17 if kind != 'mom' else 18, n=4,
                    title={'roc': 'ROC over 10 periods, in percent', 'mom': 'MOM over 10 periods, in dollars'}[kind], x=(1.4, 8.8))],
        series=[dict(pane='t', values=prices, labels=[(i, f'${v:g}', 0, .3) for i, v in enumerate(prices)]),
                dict(pane='b', values=roc, labels=[(i + 1, t, 0, .28) for i, t in enumerate(labels_roc)])],
        marks=[('pt', 't', 2, prices[2]), ('pt', 'b', 1, roc[1]), ('pt', 'b', 3, roc[3])]))


_D = [100, 110, 120, 130]
_PC = [100, 110, 121, 133.1]
SPECS_B['rcd'] = _roc_chart('BS', _D, [None, 10.0, 9.09, 8.33], ['10.0', '9.1', '8.3'], 140, 'roc')
SPECS_B['rcpc'] = _roc_chart('BT', _PC, [None, 10.0, 10.0, 10.0], ['10.0', '10.0', '10.0'], 145, 'roc')
SPECS_B['mom'] = _roc_chart('BU', _D, [None, 10, 10, 10], ['10', '10', '10'], 140, 'mom')

SPECS_B['rm'] = dict(letter='BV', caption='The table is ours, worked from the book\'s two formulas (p. 256).', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.4, 6.0, 9.4), header=('price rises', 'ROC, percent', 'MOM, dollars'), top=3.3, step=.7,
               rows=(('$100 to $110', '10.0', '10'), ('$110 to $120', '9.1', '10'), ('$120 to $130', '8.3', '10')))))


# the MACD, on closes of ours: a flat stretch, a rise and a fall
def _ema(v, n):
    a, out = 2 / (n + 1), [v[0]]
    for x in v[1:]:
        out.append(out[-1] + a * (x - out[-1]))
    return out


def _macd_closes():
    out = []
    for i in range(80):
        if i < 28:
            out.append(100 + math.sin(i / 2.2))
        elif i < 54:
            out.append(100 + (i - 28) * 1.15 + math.sin(i / 2.5))
        else:
            out.append(100 + 26 * 1.15 - (i - 54) * 0.95 + math.sin(i / 2.5))
    return [round(x, 2) for x in out]


_MC = _macd_closes()
_E12, _E26 = _ema(_MC, 12), _ema(_MC, 26)
_MD = [round(a - b, 3) for a, b in zip(_E12, _E26)]
_cu = _cross(_E12, _E26, 20, True)
_cd = _cross(_E12, _E26, 54, False)
SPECS_B['mc'] = dict(letter='BW', caption='The closes are ours, made up to show the idea.', spec=dict(
    panes=[pane('t', y=(1.95, 3.1), lo=96, hi=132, n=80, title='the 12 period EMA (gold) and the 26 period EMA (green)', x=(1.3, 10.3)),
           pane('b', y=(.5, 1.5), lo=-5, hi=7, n=80, title='MACD = 12 period EMA minus 26 period EMA', x=(1.3, 10.3), ref=[(0, '0')])],
    series=[dict(pane='t', values=[round(x, 2) for x in _E12], color=GOLD, lw=2.8),
            dict(pane='t', values=[round(x, 2) for x in _E26], color=DEEP, lw=2.8), dict(pane='b', values=_MD)],
    marks=[('pt', 't', _cu[0], _cu[1]), ('pt', 'b', _cu[0], 0)]))

_SG = [round(x, 3) for x in _ema(_MD, 9)]
_HS = [round(a - b, 3) for a, b in zip(_MD, _SG)]
_hx = _cross(_MD, _SG, 20, True)
SPECS_B['mh'] = dict(letter='BX', caption='The closes are ours, made up to show the idea.', spec=dict(
    panes=[pane('t', y=(1.95, 3.1), lo=-3, hi=7, n=80, title='MACD and its 9 period signal line', x=(1.3, 10.3), ref=[(0, '0')]),
           pane('b', y=(.5, 1.5), lo=-2, hi=2, n=80, title='histogram = MACD minus signal line', x=(1.3, 10.3), ref=[(0, '0')])],
    series=[dict(pane='t', values=_MD), dict(pane='t', values=_SG, color=GOLD, lw=2.8)],
    hist=[dict(pane='b', values=_HS, color=DEEP, lw=3.6)],
    marks=[('pt', 't', _hx[0], _hx[1]), ('pt', 'b', _hx[0], 0)]))

# average true range
SPECS_B['tr'] = dict(letter='BY', spec=dict(
    panes=[pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4))],
    bars=[dict(pane='p', rows=[(100.5, 102.5, 99.5, 102.0), (106.0, 108.0, 105.5, 107.5)], labels=[], half=.2)],
    segs=[dict(pane='p', a=(2.4, 105.5), b=(2.4, 108.0), color=GOLD, dashed=False),
          dict(pane='p', a=(3.4, 102.0), b=(3.4, 108.0), color=DEEP, dashed=False),
          dict(pane='p', a=(4.4, 102.0), b=(4.4, 105.5), color=MUTED, dashed=False)],
    levels=[dict(pane='p', value=102.0, label='previous close 102.00', side='right', dy=-.1, slots=(0, 4.4), color=MUTED)],
    texts=[(X(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 2.4), Y(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 109), '2.50', 'center', INK),
           (X(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 3.4), Y(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 109), '6.00', 'center', INK),
           (X(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 4.4), Y(pane(y=(.7, 3.0), lo=98, hi=111, n=6, x=(1.4, 9.4)), 109), '3.50', 'center', INK)],
    marks=[('pt', 'p', 2.4, 106.75), ('pt', 'p', 3.4, 105.0), ('pt', 'p', 4.4, 103.75)]))

SPECS_B['atr'] = dict(letter='BZ', spec=dict(
    panes=[pane(y=(.7, 3.1), lo=0, hi=7.5, n=3, x=(1.6, 7.2))],
    hist=[dict(pane='p', values=[6.0, 2.5, 3.5], color='#DDE3DD', lw=40)],
    levels=[dict(pane='p', value=4.0, label='their average, ATR 4.00', side='right', dy=-.1, slots=(0, 2.7), color=DEEP)],
    series=[dict(pane='p', values=[6.0, None, None], labels=[(0, '6.00', 0, -.3)]), dict(pane='p', values=[None, 2.5, None], labels=[(1, '2.50', 0, -.3)]),
            dict(pane='p', values=[None, None, 3.5], labels=[(2, '3.50', 0, -.3)])],
    marks=[('pt', 'p', 0, 6.0), ('pt', 'p', 1, 2.5), ('pt', 'p', 2, 3.5), ('pt', 'p', 1, 4.0)]))

SPECS_B['atrt'] = dict(letter='CA', caption='The table is ours, from Lim\'s sentences (p. 259).', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.6, 6.0, 9.4), header=('the ATR is', 'in an uptrend', 'in a downtrend'), top=3.4, step=.65,
               rows=(('rising', 'bullish', 'bearish'), ('falling', 'bearish', 'bullish'))),
    texts=[(6.0, 1.55, 'A high or extreme ATR usually comes with price peaks and troughs.', 'center', DEEP)]))

_AP = [50, 52, 55, 58, 62, 65, 68, 70, 72, 73, 74.5, 75.5]
_AT = [3.0, 3.4, 3.8, 4.0, 3.7, 3.2, 2.8, 2.5, 2.2, 2.0, 1.8, 1.6]
SPECS_B['atru'] = dict(letter='CB', spec=dict(
    panes=[pane('t', y=(2.1, 3.4), lo=46, hi=82, n=12, title='price: an uptrend', x=(1.3, 9.0)),
           pane('b', y=(.6, 1.75), lo=0, hi=5, n=12, title='ATR', x=(1.3, 9.0))],
    series=[dict(pane='t', values=_AP, labels=[(6, '68', 0, .3)]), dict(pane='b', values=_AT, labels=[(3, '4.0', 0, .28)])],
    marks=[('pt', 't', 6, 68), ('pt', 'b', 6, 2.8), ('box', 'b', 9, 11, 1.2, 2.3)]))

# fast and slow stochastic on ten bars of ours, lookback 3
_SB = [(50.0, 51.0, 49.5, 50.5), (50.5, 52.0, 50.2, 51.8), (51.8, 53.0, 51.5, 52.4), (52.4, 53.4, 51.9, 52.0), (52.0, 52.6, 50.8, 51.2),
       (51.2, 52.2, 50.6, 51.9), (51.9, 53.6, 51.8, 53.2), (53.2, 54.2, 52.8, 53.0), (53.0, 53.5, 52.0, 52.3), (52.3, 52.9, 51.4, 51.6)]


def _rawk(bars, n=3):
    out = [None] * len(bars)
    for i in range(n - 1, len(bars)):
        hh = max(b[1] for b in bars[i - n + 1:i + 1])
        ll = min(b[2] for b in bars[i - n + 1:i + 1])
        out[i] = round((bars[i][3] - ll) / (hh - ll) * 100, 1)
    return out


def _sma(v, n=3):
    return [None if i < n - 1 or any(x is None for x in v[i - n + 1:i + 1]) else round(sum(v[i - n + 1:i + 1]) / n, 1) for i in range(len(v))]


_RK = _rawk(_SB)
_FD = _sma(_RK)          # fast %D, which is also the slow %K
_SD = _sma(_FD)          # slow %D


def _stoch_chart(letter, lines, labels, note):
    return dict(letter=letter, spec=dict(
        panes=[pane('t', y=(2.15, 3.4), lo=48.5, hi=55, n=10, title='ten bars of ours, lookback of 3', x=(1.3, 9.6)),
               pane('b', y=(.75, 1.8), lo=-15, hi=118, n=10, title=note, x=(1.3, 9.6), ref=[(0, '0')])],
        bars=[dict(pane='t', rows=_SB, half=.1)],
        series=lines,
        marks=labels))


SPECS_B['fs'] = _stoch_chart('CC', [dict(pane='b', values=_RK, labels=[(4, f'{_RK[4]}', 0, -.42), (6, f'{_RK[6]}', 0, .3), (9, f'{_RK[9]}', 0, -.42)]),
                                    dict(pane='b', values=_FD, color=GOLD, lw=3.0, labels=[(6, f'{_FD[6]}', .5, -.2), (8, f'{_FD[8]}', 0, .28)])],
                            [('pt', 'b', 6, _RK[6]), ('pt', 'b', 6, _FD[6])], 'black: raw %K   gold: fast %D')
SPECS_B['ss'] = _stoch_chart('CD', [dict(pane='b', values=_FD, color=GOLD, lw=3.0, labels=[(7, f'{_FD[7]}', 0, .3), (9, f'{_FD[9]}', 0, -.45)]),
                                    dict(pane='b', values=_SD, color=INK, lw=2.4, labels=[(7, f'{_SD[7]}', 0, -.6), (9, f'{_SD[9]}', 0, .28)])],
                            [('pt', 'b', 7, _FD[7]), ('pt', 'b', 7, _SD[7])], 'gold: slow %K   black: slow %D')

# signal line crossovers on lines of ours: the fast pair and the slow pair
_KF = [30, 46, 64, 78, 70, 54, 36, 26, 36, 54, 70, 76, 62, 48]
_DF = _avg3(_KF)
_KS = _avg3(_KF)
_DS = [None if i < 4 else round(sum(_KS[i - 2:i + 1]) / 3, 2) for i in range(len(_KS))]


def _xover(letter, k, d, name_k, name_d, c1, c2):
    ka = [None if v is None else round(v, 2) for v in k]
    sx = _cross(ka, d, 2, False)   # %K falls through %D: sell
    bx = _cross(ka, d, int(sx[0]) + 1, True)    # then climbs back through it: buy
    return dict(letter=letter, spec=dict(
        panes=[pane(lo=0, hi=100, n=14, x=(1.3, 9.0), ref=[(80, '80'), (50, '50'), (20, '20')])],
        series=[dict(pane='p', values=ka), dict(pane='p', values=d, color=GOLD, lw=3.0)],
        texts=[(1.4, 3.42, f'black: {name_k}   gold: {name_d}', 'left', DEEP)],
        marks=[('pt', 'p', sx[0], sx[1]), ('pt', 'p', bx[0], bx[1])]))


_KF2 = [None if v is None else round(v, 2) for v in _KF]
_DF2 = [None if v is None else round(v, 2) for v in _DF]
SPECS_B['fx'] = _xover('CE', _KF2, _DF2, 'fast %K', 'fast %D', 0, 0)
_KSl = [None if v is None else round(v, 2) for v in _KS]
SPECS_B['sx'] = _xover('CF', _KSl, _DS, 'slow %K', 'slow %D', 0, 0)

SPECS_B['sdf'] = dict(letter='CG', spec=dict(
    panes=[pane(lo=-20, hi=112, n=14, x=(1.3, 8.4))],
    series=[dict(pane='p', values=[60, 72, 84, 90, 82, 70, 52, 34, 18, 12, 22, 40, 58, 72], labels=[(3, '90', 0, .28), (9, '12', 0, -.45)])],
    levels=[dict(pane='p', value=80, label='overbought: 80', side='right', dy=-.1, color=DEEP, slots=(0, 13)),
            dict(pane='p', value=20, label='oversold: 20', side='right', dy=-.1, color=DEEP, slots=(0, 13))],
    marks=[('pt', 'p', 3, 90), ('pt', 'p', 9, 12)]))

SPECS_B['nm'] = dict(letter='CH', caption='The table is ours, made up to show the idea.', spec=dict(
    panes=[], marks=[],
    table=dict(xs=(2.3, 6.0, 9.6), header=('range of the lookback', 'close up 0.10', 'close up 0.15'), top=3.3, step=.75,
               rows=(('narrow: 0.20', '0.10 / 0.20 = 50 percent', '0.15 / 0.20 = 75 percent'),
                     ('wide: 2.00', '0.10 / 2.00 = 5 percent', '0.15 / 2.00 = 7.5 percent')))))

# RSI: the formula and a worked example
SPECS_B['rsf'] = dict(letter='CI', spec=dict(
    panes=[pane('a', x=(1.5, 5.0), y=(.7, 2.6), lo=0, hi=1.6, n=2, title='average gain G and average loss L'),
           pane('b', x=(7.4, 9.6), y=(.7, 2.6), lo=0, hi=100, n=1, title='RSI on 0 to 100')],
    hist=[dict(pane='a', values=[1.2, .8], color=MUTED, lw=40), dict(pane='b', values=[60], color=DEEP, lw=40)],
    series=[dict(pane='a', values=[1.2, None], labels=[(0, 'G = 1.20', 0, .3)]), dict(pane='a', values=[None, .8], labels=[(1, 'L = 0.80', 0, .3)]),
            dict(pane='b', values=[60], labels=[(0, '60', 0, .3)])],
    texts=[(3.2, 3.38, 'RS = G / L = 1.20 / 0.80 = 1.5', 'center', DEEP), (8.5, 3.38, 'RSI = 100 - 100 / (1 + 1.5) = 60', 'center', DEEP)],
    marks=[('pt', 'a', 0, 1.2), ('pt', 'a', 1, .8), ('pt', 'b', 0, 60)]))

_RC = [100, 103, 102, 104, 101, 102]
SPECS_B['r5'] = dict(letter='CJ', spec=dict(
    panes=[pane(y=(.8, 3.0), lo=98, hi=106, n=6, x=(1.4, 9.4))],
    series=[dict(pane='p', values=_RC, labels=[(0, '100', 0, -.45), (1, '103', 0, .3), (2, '102', 0, -.45), (3, '104', 0, .3), (4, '101', 0, -.45), (5, '102', 0, .3)])],
    texts=[(1.5, 3.42, 'changes: +3, -1, +2, -3, +1.  gains 3 + 2 + 1 = 6, losses 1 + 3 = 4', 'left', DEEP),
           (1.5, 3.12, 'G = 6 / 5 = 1.20, L = 4 / 5 = 0.80, RSI = 100 x 1.20 / (1.20 + 0.80) = 60', 'left', DEEP)],
    marks=[('pt', 'p', 1, 103), ('pt', 'p', 4, 101), ('pt', 'p', 5, 102)]))


def _closes2(n=44):
    v, out = 60.0, []
    for k in range(n):
        v += 2.2 * math.sin(k / 2.3) + .9 * math.sin(k / .9) + .25
        out.append(round(v, 2))
    return out


def _stoch14(cl, n=14):
    out = [None] * len(cl)
    for i in range(n - 1, len(cl)):
        w = cl[i - n + 1:i + 1]
        out[i] = round((cl[i] - min(w)) / (max(w) - min(w)) * 100, 1)
    return out


_C2 = _closes2()
_S2, _R2 = _stoch14(_C2), _rsi(_C2, 14)
_sp = max(range(14, 44), key=lambda i: _S2[i])
SPECS_B['rvs'] = dict(letter='CK', caption='The closes are ours, made up to show the idea. Closes only; both use 14 periods.', spec=dict(
    panes=[pane('t', y=(2.75, 3.4), lo=min(_C2) - 3, hi=max(_C2) + 3, n=44, title='price', x=(1.3, 9.5)),
           pane('a', y=(1.6, 2.3), lo=-5, hi=105, n=44, title='stochastic, raw %K', x=(1.3, 9.5), ref=[(80, '80'), (20, '20')]),
           pane('b', y=(.45, 1.15), lo=-5, hi=105, n=44, title='RSI', x=(1.3, 9.5), ref=[(70, '70'), (30, '30')])],
    series=[dict(pane='t', values=_C2), dict(pane='a', values=_S2), dict(pane='b', values=_R2, color=GOLD, lw=3.0)],
    marks=[('pt', 'a', _sp, _S2[_sp]), ('pt', 'b', _sp, _R2[_sp])]))

_AGS = [64, 52, 40, 26, 14, 10, 18, 34, 52, 64, 72, 66, 58, 50, 44]
_AGR = [58, 50, 42, 34, 28, 24, 30, 38, 48, 56, 62, 60, 56, 52, 48]
_AGP = [54, 52.5, 51, 49.5, 48.2, 47.6, 48.4, 49.6, 51, 52.4, 53.6, 53.2, 52.6, 52, 51.4]
SPECS_B['ag'] = dict(letter='CL', spec=dict(
    panes=[pane('t', y=(2.75, 3.4), lo=46, hi=56, n=15, title='price', x=(1.3, 9.0)),
           pane('a', y=(1.6, 2.3), lo=-10, hi=100, n=15, title='stochastic', x=(1.3, 9.0), ref=[(20, '20')]),
           pane('b', y=(.45, 1.15), lo=-10, hi=100, n=15, title='RSI', x=(1.3, 9.0), ref=[(30, '30')])],
    series=[dict(pane='t', values=_AGP), dict(pane='a', values=_AGS, labels=[(5, '10', 0, .28)]), dict(pane='b', values=_AGR, color=GOLD, lw=3.0, labels=[(5, '24', 0, .28)])],
    marks=[('pt', 'a', 3.5, 20), ('pt', 'b', 3.667, 30), ('pt', 'a', 6.125, 20), ('pt', 'b', 6.0, 30)]))


# ================================================================ 8.7 overlay indicators
_CF = [53.0, 52.2, 51.4, 50.8, 50.3, 50.1, 50.4, 51.0, 51.8, 52.4]
SPECS_B['cf'] = dict(letter='CM', spec=dict(
    panes=[pane(y=(.7, 3.2), lo=48.5, hi=55, n=10, x=(1.3, 8.2))],
    series=[dict(pane='p', values=_CF, labels=[(5, '50.10', 0, -.45)]),
            dict(pane='p', values=_sma(_CF, 3), color=DEEP, lw=2.4, role='average', of=0, n=5)],
    levels=[dict(pane='p', value=50.0, label='prior support 50.00', side='right', dy=-.35, color=MUTED, slots=(0, 9)),
            dict(pane='p', value=50.3, label='Fibonacci level 50.30', side='right', dy=.05, color=GOLD, slots=(0, 9))],
    marks=[('pt', 'p', .5, 50.0), ('pt', 'p', .5, 50.3), ('box', 'p', 7, 8, 50.35, 51.25), ('box', 'p', 4, 6, 49.85, 50.55)]))
# the moving average of the closes is drawn at the closes it names, so a machine check can test it
SPECS_B['cf']['spec']['series'][1]['values'] = [None] * 4 + [round(sum(_CF[i - 4:i + 1]) / 5, 2) for i in range(4, 10)]
SPECS_B['cf']['angles'] = {1: (270, 250, 290), 2: (90, 70, 110)}

# Floor Trader's Pivot Points on a day of ours: H 52.00, L 48.00, C 51.20
_H, _L, _CC = 52.0, 48.0, 51.2
_PP = round((_H + _L + _CC) / 3, 2)          # 50.40
_R1, _S1 = round(2 * _PP - _L, 2), round(2 * _PP - _H, 2)   # 52.80, 48.80
_RG = _H - _L
_R2, _S2P = round(_PP + _RG, 2), round(_PP - _RG, 2)        # 54.40, 46.40
_R3, _S3 = round(_R1 + _RG, 2), round(_S1 - _RG, 2)         # 56.80, 44.80
_R4, _S4 = round(_R2 + _RG, 2), round(_S2P - _RG, 2)        # 58.40, 42.40
_YB = [(49.0, 52.0, 48.0, 51.2)]


def _lv(value, label, color=MUTED, dy=.05, side='right', slots=(1, 7)):
    return dict(pane='p', value=value, label=label, side=side, dy=dy, color=color, slots=slots)


SPECS_B['pv1'] = dict(letter='CN', spec=dict(
    panes=[pane(y=(.7, 3.3), lo=46.5, hi=54.5, n=8, x=(1.3, 8.1))],
    bars=[dict(pane='p', rows=_YB, labels=[], half=.2)],
    levels=[_lv(_PP, f'PP = {_PP:.2f}', DEEP), _lv(_R1, f'R1 = {_R1:.2f}', GOLD), _lv(_S1, f'S1 = {_S1:.2f}', GOLD, dy=-.4)],
    texts=[(X(pane(y=(.7, 3.3), lo=46.5, hi=54.5, n=8, x=(1.3, 8.1)), 0), 3.4, 'yesterday', 'center', DEEP)],
    marks=[('pt', 'p', 0, 52.0), ('pt', 'p', 0, 48.0), ('pt', 'p', .2, 51.2), ('pt', 'p', 3, _PP), ('pt', 'p', 3, _R1), ('pt', 'p', 3, _S1)]))

SPECS_B['pv2'] = dict(letter='CO', spec=dict(
    panes=[pane(y=(.7, 3.3), lo=44.5, hi=56.5, n=8, x=(1.3, 8.1))],
    bars=[dict(pane='p', rows=_YB, labels=[], half=.2)],
    levels=[_lv(_PP, f'PP = {_PP:.2f}', DEEP), _lv(_R2, f'R2 = {_R2:.2f}', GOLD), _lv(_S2P, f'S2 = {_S2P:.2f}', GOLD, dy=-.4)],
    segs=[dict(pane='p', a=(5, _PP), b=(5, _R2), color=DEEP, dashed=False), dict(pane='p', a=(5, _PP), b=(5, _S2P), color=DEEP, dashed=False)],
    texts=[(X(pane(y=(.7, 3.3), lo=44.5, hi=56.5, n=8, x=(1.3, 8.1)), 0), 3.4, 'yesterday', 'center', DEEP)],
    marks=[('pt', 'p', 3, _PP), ('pt', 'p', 3, _R2), ('pt', 'p', 3, _S2P), ('pt', 'p', 0, 50.0)]))

SPECS_B['pv3'] = dict(letter='CP', spec=dict(
    panes=[pane(y=(.55, 3.3), lo=41, hi=59.5, n=8, x=(1.3, 8.1))],
    levels=[_lv(_R4, f'R4 = {_R4:.2f}', GOLD), _lv(_R3, f'R3 = {_R3:.2f}', GOLD), _lv(_R2, f'R2 = {_R2:.2f}', MUTED, dy=.0),
            _lv(_R1, f'R1 = {_R1:.2f}', MUTED, dy=.0), _lv(_PP, f'PP = {_PP:.2f}', DEEP, dy=.0), _lv(_S1, f'S1 = {_S1:.2f}', MUTED, dy=.0),
            _lv(_S2P, f'S2 = {_S2P:.2f}', MUTED, dy=.0), _lv(_S3, f'S3 = {_S3:.2f}', GOLD, dy=.0), _lv(_S4, f'S4 = {_S4:.2f}', GOLD, dy=.0)],
    marks=[('pt', 'p', 1, _R3), ('pt', 'p', 1, _R4), ('pt', 'p', 1, _S3), ('pt', 'p', 1, _S4)]),
    angles={n: (180, 165, 195, 150, 210) for n in (1, 2, 3, 4)})

_DP = [51.0, 51.6, 52.4, 53.2, 53.9, 54.7, 54.2, 53.6]
SPECS_B['pvd'] = dict(letter='CQ', spec=dict(
    panes=[pane(y=(.6, 3.3), lo=48, hi=56, n=8, x=(1.3, 8.1))],
    series=[dict(pane='p', values=_DP, labels=[(0, '51.00', 0, -.45), (5, '54.70', 0, .3)])],
    levels=[_lv(_PP, f'PP = {_PP:.2f}', DEEP, slots=(0, 7)), _lv(_R1, f'R1 = {_R1:.2f}', MUTED, slots=(0, 7)),
            _lv(_R2, f'R2 = {_R2:.2f}', MUTED, slots=(0, 7))],
    marks=[('pt', 'p', 0, 51.0), ('pt', 'p', 2.5, _PP), ('pt', 'p', 5, 54.7)]))
