"""Plain-data chart specs for Chapter 9. Every number is ours, invented for teaching.

A spec carries no teaching text: every word on a slide is written by hand in the content files.
The letters restart at A in this chapter. The key is the asset name; both must be unique.
"""
import chartkit as ck

SPECS = {}
INK, MUTED, DEEP = ck.INK, ck.MUTED, ck.GREEN_DEEP


def pane(id='p', x=(1.3, 10.3), y=(.8, 3.25), lo=0, hi=1, n=10, **kw):
    return dict(id=id, x=x, y=y, lo=lo, hi=hi, n=n, **kw)


def _two(price, osc, plo, phi, olo, ohi, n):
    """Price pane over an oscillator pane, the way every divergence chart is laid out."""
    return [pane('p', y=(1.95, 3.3), lo=plo, hi=phi, n=n, title='Main data series: price'),
            pane('o', y=(.45, 1.6), lo=olo, hi=ohi, n=n, title='Supporting data series: oscillator')]


# ---- the opener: a main and a supporting series that disagree (price peaks 52 then 55, oscillator 74 then 61)
_P = [41, 48, 52, 44, 49, 55, 46, 41]
_O = [40, 62, 74, 48, 52, 61, 44, 36]
SPECS['dv'] = dict(letter='A', spec=dict(
    panes=_two(_P, _O, 38, 65, 28, 105, 8),
    series=[dict(pane='p', values=_P, labels=[(2, '52.00', 0, .3), (5, '55.00', 0, .3)]),
            dict(pane='o', values=_O, labels=[(2, '74', 0, .3), (5, '61', 0, .3)])],
    marks=[('pt', 'p', 5, 55), ('pt', 'o', 5, 61)]))

# ---- the worked example: two adjacent peaks in each series, and the direction each gives
_PA = [41, 48, 52, 44, 49, 54, 46, 41]
SPECS['adj'] = dict(letter='B', spec=dict(
    panes=_two(_PA, _O, 38, 65, 28, 105, 8),
    series=[dict(pane='p', values=_PA, labels=[(2, '52.00', 0, .3), (5, '54.00', 0, .3)]),
            dict(pane='o', values=_O, labels=[(2, '74', 0, .3), (5, '61', 0, .3)])],
    marks=[('box', 'p', 1.6, 5.4, 48.5, 64.5), ('box', 'o', 1.6, 5.4, 46, 104)]))

# ---- confirmation: both series make higher peaks (price 52 then 55, oscillator 61 then 70)
_O2 = [40, 52, 61, 46, 54, 70, 50, 42]
SPECS['cf'] = dict(letter='C', spec=dict(
    panes=_two(_P, _O2, 38, 65, 28, 105, 8),
    series=[dict(pane='p', values=_P, labels=[(2, '52.00', 0, .3), (5, '55.00', 0, .3)]),
            dict(pane='o', values=_O2, labels=[(2, '61', 0, .3), (5, '70', 0, .3)])],
    marks=[('box', 'p', 1.6, 5.4, 48.5, 64.5), ('box', 'o', 1.6, 5.4, 46, 104)]))

# ---- price confirmation: the divergence of the opener, then price breaks the support under its trough
_PC = [42, 49, 52, 48, 51, 55, 50, 46.5, 44.5, 43]
_OC = [42, 62, 74, 52, 54, 61, 46, 40, 36, 34]
SPECS['pc'] = dict(letter='D', spec=dict(
    panes=_two(_PC, _OC, 40, 61, 28, 100, 10),
    series=[dict(pane='p', values=_PC, labels=[(2, '52.00', 0, .3), (5, '55.00', 0, .3), (7, '46.50', .45, -.4)]),
            dict(pane='o', values=_OC, labels=[(2, '74', 0, .3), (5, '61', 0, .3)])],
    levels=[dict(pane='p', value=48.0, slots=(3, 9), color=DEEP)],
    texts=[(8.7, 3.12, 'support 48.00, under the trough', 'center', DEEP)],
    marks=[('pt', 'p', 3, 48), ('pt', 'p', 7, 46.5)]))
