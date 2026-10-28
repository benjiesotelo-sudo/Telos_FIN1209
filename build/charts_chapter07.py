"""Immutable owner chart data; the shared engine owns layout only."""
import chartkit as ck
import numpy as np
import deckkit as dk

DATA = {'r1-j': {'items': (ck.Cell(panes=(ck.Pane(bars=(ck.Bar(open=50, high=52.4, low=49.6, close=51.1),)),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.46, y0=0.64, x1=0.54, y1=0.72, color='gold', at=(0.24, 0.66), size=0.26), dk.Mark(number=2, kind='circle', x0=0.46, y0=0.2, x1=0.54, y1=0.28, color='red', at=(0.86, 0.13), size=0.23), dk.Mark(number=3, kind='circle', x0=0.46, y0=0.74, x1=0.54, y1=0.81, color='blue', at=(0.86, 0.89), size=0.23), dk.Mark(number=4, kind='circle', x0=0.46, y0=0.44, x1=0.54, y1=0.52, color='purple', at=(0.69, 0.56), size=0.26)),
'old_size': (18.0, 3.5),
'owner': 'r1',
'caption': 'Prices are invented for teaching.',
'letter': 'J'},
'r1-m': {'items': (ck.Cell(name='A rise, then a two-bar formation', panes=(ck.Pane(bars=(ck.Bar(open=45.0, high=46.0, low=44.2, close=45.6), ck.Bar(open=45.6, high=48.5, low=45.4, close=48.1), ck.Bar(open=48.1, high=49.2, low=47.9, close=49.0), ck.Bar(open=49.1, high=49.4, low=47.3, close=47.5)), strokes=(ck.Stroke(points=((2, 47.9), (3, 47.9)), dashed=True),), notes=(ck.Note(x=0, label='the rise'), ck.Note(x=1, label='the rise'), ck.Note(x=2, label='first of the pair'), ck.Note(x=3, label='second of the pair'))),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=2, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=3, kind='box', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=4, kind='circle', x0=0, y0=0, x1=0, y1=0)),
'old_size': (18.0, 3.5),
'owner': 'r1',
'caption': 'Prices are invented for teaching.',
'right_margin': 1.95,
'span_levels': True,
'group_gap': 0.1,
'letter': 'S'},
'r1-p': {'items': (ck.Cell(name='Five trades of ours inside one five-minute interval', panes=(ck.Pane(line=(50.0, 50.8, 49.6, 52.4, 51.1)),)),),
'special': '',
'line_format': '{:.2f}',
'trough_below': True,
'line_captions': ('Trade 1', 'Trade 2', 'Trade 3', 'Trade 4', 'Trade 5'),
'old_marks': (dk.Mark(number=1, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=2, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=3, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=4, kind='circle', x0=0, y0=0, x1=0, y1=0)),
'old_size': (18.0, 3.5),
'owner': 'r1',
'caption': 'Prices are invented for teaching.',
'protect_line': True,
'letter': 'P'},
'r1-r': {'items': (ck.Cell(name='Three five-minute bars of ours and the 15-minute bar they make', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=50.6, low=49.8, close=50.2), ck.Bar(open=50.2, high=50.9, low=49.4, close=50.1), ck.Bar(open=50.1, high=50.5, low=49.7, close=50.3), ck.Bar(open=50.0, high=50.9, low=49.4, close=50.3)), notes=(ck.Note(x=0, label='minutes 1 to 5'), ck.Note(x=1, label='minutes 6 to 10'), ck.Note(x=2, label='minutes 11 to 15'), ck.Note(x=3, label='the 15-minute bar'))),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=2, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=3, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=4, kind='circle', x0=0, y0=0, x1=0, y1=0)),
'old_size': (18.0, 3.5),
'owner': 'r1',
'caption': 'Prices are invented for teaching.',
'letter': 'R'},
'r1-g': {'items': (),
'special': 'counts',
'count_groups': ((1, 'Single: 1 bar'), (2, 'Double: 2 bars'), (3, 'Triple: 3 bars'), (5, 'Multiple: 5 bars')),
'count_centres': (1.2, 3.3, 5.9, 9.2),
'caption': 'The bars are drawn only to be counted; they carry no prices.',
'group_gap': 0.1,
'old_marks': (dk.Mark(number=1, kind='box', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=2, kind='box', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=3, kind='box', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=4, kind='box', x0=0, y0=0, x1=0, y1=0)),
'old_size': (18.0, 3.5),
'owner': 'r1',
'letter': 'G'},
'r3a-k': {'items': (ck.Cell(name='Key reversal: yesterday and today', panes=(ck.Pane(bars=(ck.Bar(open=50.8, high=52.0, low=50.6, close=51.1), ck.Bar(open=52.3, high=53.2, low=49.9, close=50.8)), strokes=(ck.Stroke(points=((0, 52), (1, 52)), dashed=True, label='Prior high 52.00'), ck.Stroke(points=((0, 51.1), (1, 51.1)), dashed=True, label='Prior close 51.10'))), ck.Pane(columns=(2.0, 4.2)))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=np.float64(0.7018510869565218), y0=np.float64(0.2853929924242434), x1=np.float64(0.7249489130434783), y1=np.float64(0.32966382575757675), color='gold', at=(np.float64(0.7134), np.float64(0.24841382575757676)), size=0.26), dk.Mark(number=2, kind='circle', x0=np.float64(0.7309510869565218), y0=np.float64(0.15755208333333334), x1=np.float64(0.7540489130434783), y1=np.float64(0.20182291666666666), color='red', at=(np.float64(0.7733423913043479), np.float64(0.1796875)), size=0.26), dk.Mark(number=3, kind='circle', x0=np.float64(0.7600510869565217), y0=np.float64(0.4984611742424257), x1=np.float64(0.7831489130434782), y1=np.float64(0.542732007575759), color='blue', at=(np.float64(0.7716), np.float64(0.46148200757575897)), size=0.26), dk.Mark(number=4, kind='circle', x0=np.float64(0.7309510869565218), y0=np.float64(0.8320312500000001), x1=np.float64(0.7540489130434783), y1=np.float64(0.8763020833333334), color='purple', at=(np.float64(0.7733423913043479), np.float64(0.8541666666666667)), size=0.26)),
'old_size': (7.36, 3.84),
'owner': 'r3a',
'letter': 'K'},
'r3a-a': {'items': (ck.Cell(name='Exhaustion bar', panes=(ck.Pane(bars=(ck.Bar(open=62.0, high=65.0, low=61.0, close=64.0), ck.Bar(open=65.4, high=66.2, low=60.0, close=60.5), ck.Bar(open=60.2, high=62.0, low=59.8, close=61.6)), strokes=(ck.Stroke(points=((0, 65), (2, 65)), dashed=True, label='Prior high 65.00'),)), ck.Pane(columns=(1.8, 4.8, 2.1)))), ck.Cell(name='Pin bar', panes=(ck.Pane(bars=(ck.Bar(open=41.0, high=42.0, low=40.2, close=41.5), ck.Bar(open=41.5, high=42.0, low=38.8, close=40.6), ck.Bar(open=40.6, high=42.2, low=40.0, close=41.8)), strokes=(ck.Stroke(points=((0, 40), (2, 40)), dashed=True, label='Support 40.00'),)), ck.Pane(columns=(1.6, 0.8, 1.5))))),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=np.float64(0.48602608695652183), y0=np.float64(0.1813151041666667), x1=np.float64(0.5091239130434784), y1=np.float64(0.22558593750000003), color='gold', at=(np.float64(0.4975750000000001), np.float64(0.2625651041666667)), size=0.26), dk.Mark(number=2, kind='circle', x0=np.float64(0.5151260869565218), y0=np.float64(0.1705729166666667), x1=np.float64(0.5382239130434784), y1=np.float64(0.21484375000000003), color='red', at=(np.float64(0.557517391304348), np.float64(0.19270833333333337)), size=0.26), dk.Mark(number=3, kind='circle', x0=np.float64(0.7940010869565216), y0=np.float64(0.2511393229166666), x1=np.float64(0.8170989130434781), y1=np.float64(0.29541015624999994), color='blue', at=(np.float64(0.8055499999999999), np.float64(0.21416015624999996)), size=0.26), dk.Mark(number=4, kind='circle', x0=np.float64(0.5199760869565218), y0=np.float64(0.6439185049019608), x1=np.float64(0.5430739130434783), y1=np.float64(0.688189338235294), color='purple', at=(np.float64(0.5006826086956522), np.float64(0.6660539215686274)), size=0.26), dk.Mark(number=5, kind='circle', x0=np.float64(0.5151260869565218), y0=np.float64(0.8776041666666667), x1=np.float64(0.5382239130434784), y1=np.float64(0.921875), color='gold', at=(np.float64(0.557517391304348), np.float64(0.8997395833333334)), size=0.26), dk.Mark(number=6, kind='circle', x0=np.float64(0.5442260869565219), y0=np.float64(0.6149662990196079), x1=np.float64(0.5673239130434784), y1=np.float64(0.6592371323529411), color='red', at=(np.float64(0.5557750000000001), np.float64(0.5779871323529411)), size=0.26)),
'old_size': (7.36, 3.84),
'owner': 'r3a',
'letter': 'A'},
'r3a-l': {'items': (ck.Cell(name='Two-day bearish reversal', note='first close near high; second near low', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=52.2, low=49.7, close=51.8), ck.Bar(open=51.7, high=52.0, low=49.0, close=49.6)), notes=(ck.Note(label='C 51.80', dx=-20, dy=8, y=51.8, notice=True), ck.Note(x=1, label='C 49.60', dx=55, dy=-8, y=49.6, notice=True), ck.Note(label='H 52.20', dx=-18, dy=10, y=52.2), ck.Note(x=1, label='L 49.00', dx=18, dy=-10, y=49.0)), height=1.7), ck.Pane(columns=(2.4, 3.1), tags=((0, '2.4m'), (1, '3.1m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.27, y0=0.28, x1=0.34, y1=0.36, color='gold', at=(0.12, 0.28), size=0.25), dk.Mark(number=2, kind='circle', x0=0.64, y0=0.56, x1=0.72, y1=0.65, color='red', at=(0.8, 0.52), size=0.25)),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3a',
'letter': 'L'},
'r3a-m': {'items': (ck.Cell(name='Bullish three-bar reversal', note='strong outer bars; quiet middle bar', panes=(ck.Pane(bars=(ck.Bar(open=46.0, high=46.2, low=42.8, close=43.0), ck.Bar(open=43.1, high=43.6, low=42.7, close=43.3), ck.Bar(open=43.2, high=46.5, low=43.0, close=46.3)), notes=(ck.Note(label='H 46.20', dx=-20, dy=8, y=46.2), ck.Note(label='C 43.00', dx=-20, dy=-10, y=43.0, notice=True), ck.Note(x=1, label='L 42.70', dx=-20, dy=-10, y=42.7), ck.Note(x=1, label='H 43.60', dx=18, dy=8, y=43.6), ck.Note(x=1, label='middle C 43.30', dx=18, dy=7, y=43.3, notice=True), ck.Note(x=2, label='C 46.30', dx=18, dy=-8, y=46.3, notice=True)), height=1.7), ck.Pane(columns=(4.0, 0.6, 4.2), tags=((0, '4.0m'), (1, '0.6m'), (2, '4.2m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.22, y0=0.75, x1=0.29, y1=0.84, color='gold', at=(0.14, 0.55)), dk.Mark(number=2, kind='circle', x0=0.47, y0=0.75, x1=0.54, y1=0.84, color='red', at=(0.42, 0.7)), dk.Mark(number=3, kind='circle', x0=0.73, y0=0.75, x1=0.8, y1=0.84, color='blue', at=(0.86, 0.7))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3a',
'letter': 'M'},
'r3a-n': {'items': (ck.Cell(name='Bearish island reversal', note='gap up, isolated bars, gap down', panes=(ck.Pane(bars=(ck.Bar(open=48.0, high=50.0, low=47.5, close=49.5), ck.Bar(open=50.8, high=52.0, low=50.6, close=51.5), ck.Bar(open=51.4, high=52.2, low=50.9, close=51.1), ck.Bar(open=49.4, high=50.0, low=48.2, close=48.8)), strokes=(ck.Stroke(points=((0, 50.0), (3, 50.0)), tone='quiet', dashed=True, label='prior high 50.00', dx=-24, dy=-10),), notes=(ck.Note(x=1, label='gap up (window)', dx=-85, dy=15, y=50.3, notice=True), ck.Note(x=2, label='island', dx=18, dy=-8, y=51.5, notice=True), ck.Note(x=3, label='gap down (window)', dx=-82, dy=15, y=50.45, notice=True)), height=1.7), ck.Pane(columns=(2.3, 0.7, 0.6, 2.1), tags=((0, '2.3m'), (1, '0.7m'), (2, '0.6m'), (3, '2.1m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.3, y0=0.2, x1=0.39, y1=0.3, color='gold', at=(0.25, 0.15)), dk.Mark(number=2, kind='box', x0=0.38, y0=0.22, x1=0.76, y1=0.52, color='red', at=(0.78, 0.54)), dk.Mark(number=3, kind='circle', x0=0.7, y0=0.2, x1=0.8, y1=0.3, color='blue', at=(0.86, 0.15))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3a',
'letter': 'N'},
'r3b-la': {'items': (ck.Cell(name='Outside bar', note='contains two prior bars and closes near its low', panes=(ck.Pane(bars=(ck.Bar(open=49.0, high=51.5, low=48.0, close=51.2), ck.Bar(open=50.5, high=52.0, low=49.5, close=51.8), ck.Bar(open=52.0, high=53.0, low=47.0, close=47.5)), strokes=(ck.Stroke(points=((0, 52.0), (2, 52.0)), tone='quiet', dashed=True, label='prior high 52.00', dx=-18, dy=-10),), notes=(ck.Note(x=2, label='H 53.00', dx=18, dy=8, y=53.0, notice=True), ck.Note(x=2, label='L 47.00', dx=-18, dy=-10, y=47.0), ck.Note(x=2, label='C 47.50', dx=20, dy=-4, y=47.5, notice=True)), height=1.8), ck.Pane(columns=(1.5, 1.4, 5.0), tags=((0, '1.5m'), (1, '1.4m'), (2, '5.0m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.7, y0=0.18, x1=0.8, y1=0.65, color='gold', at=(0.64, 0.24)), dk.Mark(number=2, kind='circle', x0=0.735, y0=0.175, x1=0.775, y1=0.225, color='red', at=(0.84, 0.12)), dk.Mark(number=3, kind='circle', x0=0.72, y0=0.58, x1=0.79, y1=0.66, color='blue', at=(0.84, 0.7))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LA'},
'r3b-lb': {'items': (ck.Cell(name='Inside bar', note='second bar stays inside the first', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=53.0, low=48.0, close=52.4), ck.Bar(open=51.8, high=52.5, low=49.2, close=50.1)), strokes=(ck.Stroke(points=((0, 53.0), (1, 53.0)), tone='quiet', dashed=True, label='resistance 53.00', dx=-20, dy=-10),), notes=(ck.Note(label='H 53.00', dx=-18, dy=8, y=53.0, notice=True), ck.Note(x=1, label='H 52.50', dx=18, dy=8, y=52.5, notice=True), ck.Note(x=1, label='C 50.10', dx=20, dy=-6, y=50.1, notice=True)), height=1.8), ck.Pane(columns=(4.5, 0.5), tags=((0, '4.5m'), (1, '0.5m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.32, y0=0.16, x1=0.4, y1=0.78, color='gold', at=(0.25, 0.12)), dk.Mark(number=2, kind='box', x0=0.63, y0=0.21, x1=0.69, y1=0.55, color='red', at=(0.75, 0.28)), dk.Mark(number=3, kind='line', x0=0.28, y0=0.2, x1=0.77, y1=0.2, color='blue', at=(0.82, 0.12))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LB'},
'r3b-lc': {'items': (ck.Cell(name='Exhaustion bar', note='wide bar opens above the prior high and is followed without a gap', panes=(ck.Pane(bars=(ck.Bar(open=62.0, high=65.0, low=61.0, close=64.0), ck.Bar(open=65.4, high=66.2, low=60.0, close=60.5), ck.Bar(open=60.2, high=62.0, low=59.8, close=61.6)), strokes=(ck.Stroke(points=((0, 65.0), (2, 65.0)), tone='quiet', dashed=True, label='prior high 65.00', dx=-20, dy=-10),), notes=(ck.Note(x=1, label='O 65.40', dx=18, dy=8, y=65.4, notice=True), ck.Note(x=1, label='H 66.20', dx=18, dy=8, y=66.2, notice=True), ck.Note(x=1, label='L 60.00', dx=-18, dy=-10, y=60.0), ck.Note(x=1, label='C 60.50', dx=18, dy=-4, y=60.5, notice=True), ck.Note(x=2, label='next O 60.20', dx=18, dy=-8, y=60.2, notice=True)), height=1.8), ck.Pane(columns=(1.8, 4.8, 2.1), tags=((0, '1.8m'), (1, '4.8m'), (2, '2.1m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='line', x0=0.18, y0=0.27, x1=0.48, y1=0.27, color='gold', at=(0.17, 0.21)), dk.Mark(number=2, kind='box', x0=0.48, y0=0.12, x1=0.6, y1=0.78, color='red', at=(0.66, 0.19)), dk.Mark(number=3, kind='line', x0=0.72, y0=0.6, x1=0.8, y1=0.6, color='blue', at=(0.84, 0.54))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LC'},
'r3b-ld': {'items': (ck.Cell(name='Emotion spike', note='wide range and high volume', panes=(ck.Pane(bars=(ck.Bar(open=60.0, high=61.5, low=58.5, close=61.0), ck.Bar(open=61.0, high=62.5, low=59.5, close=62.0), ck.Bar(open=62.0, high=70.0, low=62.0, close=63.0), ck.Bar(open=63.0, high=64.0, low=61.0, close=61.5)), notes=(ck.Note(x=2, label='spike'),), height=1.8), ck.Pane(columns=(1.5, 1.5, 6.0, 1.5), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.4, y0=0.14, x1=0.46, y1=0.58, color='gold', at=(0.34, 0.22)), dk.Mark(number=2, kind='circle', x0=0.4, y0=0.7, x1=0.46, y1=0.8, color='red', at=(0.51, 0.84)), dk.Mark(number=3, kind='box', x0=0.58, y0=0.28, x1=0.92, y1=0.66, color='blue', at=(0.94, 0.2))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LD'},
'r3b-lj': {'items': (ck.Cell(name='Pin bar', note='false support break returns above the barrier', panes=(ck.Pane(bars=(ck.Bar(open=42.0, high=43.0, low=40.5, close=42.2), ck.Bar(open=42.0, high=42.5, low=38.8, close=40.6)), strokes=(ck.Stroke(points=((0, 40.0), (1, 40.0)), tone='quiet', dashed=True, label='support 40.00', dx=-18, dy=-10),), notes=(ck.Note(x=1, label='L 38.80', dx=-18, dy=-8, y=38.8, notice=True), ck.Note(x=1, label='C 40.60', dx=18, dy=6, y=40.6, notice=True)), height=1.8), ck.Pane(columns=(2.0, 0.8), tags=((0, '2.0m'), (1, '0.8m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='line', x0=0.36, y0=0.53, x1=0.8, y1=0.53, color='gold', at=(0.18, 0.45)), dk.Mark(number=2, kind='circle', x0=0.648, y0=0.64, x1=0.672, y1=0.69, color='red', at=(0.71, 0.68)), dk.Mark(number=3, kind='circle', x0=0.648, y0=0.45, x1=0.672, y1=0.49, color='blue', at=(0.73, 0.38))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LJ'},
'r3b-le': {'items': (ck.Cell(name='False upside breakout', note='close returns below resistance', panes=(ck.Pane(bars=(ck.Bar(open=58.0, high=60.0, low=57.0, close=59.0), ck.Bar(open=59.0, high=62.0, low=58.5, close=59.4)), strokes=(ck.Stroke(points=((0, 60.0), (1, 60.0)), tone='quiet', dashed=True, label='resistance 60.00', dx=-18, dy=-10),), notes=(ck.Note(x=1, label='H 62.00', dx=18, dy=8, y=62.0, notice=True), ck.Note(x=1, label='C 59.40', dx=18, dy=-6, y=59.4, notice=True)), height=1.4),)), ck.Cell(name='False downside breakout', note='close returns above support', panes=(ck.Pane(bars=(ck.Bar(open=42.0, high=43.0, low=40.0, close=41.0), ck.Bar(open=41.0, high=41.5, low=38.5, close=40.6)), strokes=(ck.Stroke(points=((0, 40.0), (1, 40.0)), tone='quiet', dashed=True, label='support 40.00', dx=-18, dy=-10),), notes=(ck.Note(x=1, label='L 38.50', dx=-18, dy=-8, y=38.5, notice=True), ck.Note(x=1, label='C 40.60', dx=18, dy=6, y=40.6, notice=True)), height=1.4),))),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.3, y0=0.2, x1=0.36, y1=0.3, color='gold', at=(0.28, 0.16)), dk.Mark(number=2, kind='circle', x0=0.79, y0=0.84, x1=0.87, y1=0.95, color='red', at=(0.72, 0.96)), dk.Mark(number=3, kind='circle', x0=0.3, y0=0.54, x1=0.36, y1=0.64, color='blue', at=(0.42, 0.52)), dk.Mark(number=4, kind='circle', x0=0.79, y0=0.53, x1=0.87, y1=0.63, color='purple', at=(0.91, 0.5))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LE'},
'r3b-lf': {'items': (ck.Cell(name='False upside breakout', note='the course drawing; return below resistance', panes=(ck.Pane(bars=(ck.Bar(open=58.0, high=60.0, low=57.0, close=59.0), ck.Bar(open=59.0, high=62.0, low=58.5, close=59.4)), strokes=(ck.Stroke(points=((0, 60.0), (1, 60.0)), tone='quiet', dashed=True, label='resistance 60.00', dx=-18, dy=-10), ck.Stroke(points=((0, 62.5), (1, 62.5)), tone='quiet', dashed=True, label='stop 62.50', at=1, dx=18, dy=-10)), notes=(ck.Note(x=1, label='H 62.00', dx=18, dy=8, y=62.0, notice=True), ck.Note(x=1, label='C 59.40', dx=18, dy=-6, y=59.4, notice=True)), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='line', x0=0.34, y0=0.5, x1=0.68, y1=0.5, color='gold', at=(0.25, 0.43)), dk.Mark(number=2, kind='circle', x0=0.645, y0=0.235, x1=0.674, y1=0.285, color='red', at=(0.8, 0.11)), dk.Mark(number=3, kind='circle', x0=0.645, y0=0.535, x1=0.674, y1=0.59, color='blue', at=(0.8, 0.63)), dk.Mark(number=4, kind='line', x0=0.35, y0=0.23, x1=0.68, y1=0.23, color='purple', at=(0.81, 0.3))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LF'},
'r3b-lg': {'items': (ck.Cell(name='Ten bullish days come first', note='closes for bars 1 to 10; dashed line: three-day SMA shifted three days forward', panes=(ck.Pane(line=(45.0, 45.6, 46.2, 46.9, 47.5, 48.2, 48.8, 49.5, 50.1, 50.7), strokes=(ck.Stroke(points=((5, 45.6), (6, 46.2333), (7, 46.8667), (8, 47.5333), (9, 48.1667)), tone='quiet', dashed=True),), notes=(ck.Note(x=5, label='SMA 45.60'), ck.Note(x=9, label='SMA 48.17'))),)), ck.Cell(name='The top: two closes below the line', note='closes for bars 10 to 16; dashed line: the same shifted SMA', panes=(ck.Pane(line=(50.7, 50.4, 49.8, 49.2, 50.7, 49.4, 48.3), strokes=(ck.Stroke(points=((0, 48.1667), (1, 48.8333), (2, 49.4667), (3, 50.1), (4, 50.4), (5, 50.3), (6, 49.8)), tone='quiet', dashed=True),), notes=(ck.Note(x=3, label='SMA 50.10'), ck.Note(x=4, label='SMA 50.40'), ck.Note(x=5, label='SMA 50.30'))),))),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.645, y0=0.4, x1=0.673, y1=0.45, color='gold', at=(0.57, 0.33)), dk.Mark(number=2, kind='circle', x0=0.708, y0=0.53, x1=0.735, y1=0.57, color='red', at=(0.77, 0.67)), dk.Mark(number=3, kind='box', x0=0.775, y0=0.32, x1=0.89, y1=0.7, color='blue', at=(0.94, 0.25))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LG'},
'r3b-lh': {'items': (ck.Cell(name='Bearish Hikkake', note="dashed lines: the inside bar's high and low", panes=(ck.Pane(bars=(ck.Bar(open=49.0, high=53.5, low=48.0, close=52.8), ck.Bar(open=51.5, high=52.0, low=49.0, close=50.2), ck.Bar(open=50.4, high=53.0, low=50.0, close=52.5), ck.Bar(open=52.3, high=52.6, low=48.5, close=48.7)), strokes=(ck.Stroke(points=((0, 52.0), (3, 52.0)), tone='quiet', dashed=True), ck.Stroke(points=((0, 49.0), (3, 49.0)), tone='quiet', dashed=True)), notes=(ck.Note(x=1, label='inside bar'), ck.Note(x=2, label='false break'), ck.Note(x=3, label='short')), height=1.5),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.22, y0=0.35, x1=0.29, y1=0.78, color='gold', at=(0.16, 0.3)), dk.Mark(number=2, kind='circle', x0=0.47, y0=0.18, x1=0.53, y1=0.28, color='red', at=(0.58, 0.14)), dk.Mark(number=3, kind='arrow', x0=0.67, y0=0.6, x1=0.75, y1=0.77, color='blue', at=(0.65, 0.55))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LH'},
'r3b-li': {'items': (ck.Cell(name='Bullish Hikkake', note="dashed lines: the inside bar's high and low", panes=(ck.Pane(bars=(ck.Bar(open=43.5, high=44.5, low=39.5, close=40.2), ck.Bar(open=40.8, high=43.0, low=40.0, close=42.2), ck.Bar(open=41.8, high=42.2, low=39.0, close=39.4), ck.Bar(open=39.6, high=44.0, low=39.5, close=43.4)), strokes=(ck.Stroke(points=((0, 43.0), (3, 43.0)), tone='quiet', dashed=True), ck.Stroke(points=((0, 40.0), (3, 40.0)), tone='quiet', dashed=True)), notes=(ck.Note(x=1, label='inside bar'), ck.Note(x=2, label='false break'), ck.Note(x=3, label='long')), height=1.5),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.16, y0=0.25, x1=0.29, y1=0.72, color='gold', at=(0.1, 0.2)), dk.Mark(number=2, kind='circle', x0=0.23, y0=0.8, x1=0.27, y1=0.86, color='red', at=(0.4, 0.84)), dk.Mark(number=3, kind='circle', x0=0.35, y0=0.34, x1=0.39, y1=0.38, color='blue', at=(0.43, 0.25)), dk.Mark(number=4, kind='box', x0=0.62, y0=0.25, x1=0.68, y1=0.72, color='gold', at=(0.57, 0.2)), dk.Mark(number=5, kind='circle', x0=0.73, y0=0.21, x1=0.77, y1=0.27, color='red', at=(0.93, 0.25)), dk.Mark(number=6, kind='circle', x0=0.85, y0=0.75, x1=0.878, y1=0.8, color='blue', at=(0.95, 0.67))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LI'},
'r3b-lk': {'items': (ck.Cell(name='Bearish three-bar reversal', note='first close near its high, third close near its low', panes=(ck.Pane(bars=(ck.Bar(open=49.2, high=52.2, low=49.0, close=52.0), ck.Bar(open=52.0, high=52.4, low=51.4, close=51.7), ck.Bar(open=51.8, high=52.1, low=48.7, close=48.8)), height=1.8),)),),
'special': '',
'old_marks': (),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LK'},
'r4-n': {'items': (ck.Cell(name="Bearish Oops: bar 2 opens above bar 1's high", note='', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=52.0, low=49.5, close=51.0), ck.Bar(open=53.0, high=54.0, low=50.5, close=51.5)), strokes=(ck.Stroke(points=((0, 52.0), (1, 52.0)), dashed=True, label='bar 1 high, sell-stop 52.00'), ck.Stroke(points=((0, 54.0), (1, 54.0)), dashed=True, label='bar 2 high, stoploss 54.00')), notes=(ck.Note(label='the previous bar'), ck.Note(x=1, label='gaps up, then falls')), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.64, y0=0.27, x1=0.69, y1=0.33, color='gold', at=(0.51, 0.37)), dk.Mark(number=2, kind='circle', x0=0.64, y0=0.49, x1=0.69, y1=0.55, color='red', at=(0.78, 0.62)), dk.Mark(number=3, kind='circle', x0=0.64, y0=0.21, x1=0.69, y1=0.27, color='blue', at=(0.78, 0.13))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r4',
'letter': 'ON'},
'r4-v': {'items': (ck.Cell(name="Bullish Oops: bar 2 opens below bar 1's low", note='', panes=(ck.Pane(bars=(ck.Bar(open=49.0, high=50.0, low=48.0, close=49.5), ck.Bar(open=47.0, high=49.0, low=46.0, close=48.5)), strokes=(ck.Stroke(points=((0, 48.0), (1, 48.0)), dashed=True, label='bar 1 low, buy-stop 48.00'), ck.Stroke(points=((0, 46.0), (1, 46.0)), dashed=True, label='bar 2 low, stoploss 46.00')), notes=(ck.Note(label='the previous bar'), ck.Note(x=1, label='gaps down, then rises')), height=1.75),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='arrow', x0=0.67, y0=0.55, x1=0.67, y1=0.7, color='gold', at=(0.76, 0.58), size=0.3), dk.Mark(number=2, kind='line', x0=0.39, y0=0.54, x1=0.63, y1=0.54, color='red', at=(0.78, 0.47), size=0.3), dk.Mark(number=3, kind='line', x0=0.39, y0=0.84, x1=0.63, y1=0.84, color='blue', at=(0.8, 0.87), size=0.3)),
'old_size': (8.222999781277341, 3.84),
'owner': 'r4',
'letter': 'V'},
'r4-o': {'items': (ck.Cell(name='ID/NR6: six daily bars of ours', note='', panes=(ck.Pane(bars=(ck.Bar(open=51.0, high=54.0, low=50.0, close=53.5), ck.Bar(open=53.4, high=54.6, low=51.4, close=52.0), ck.Bar(open=52.2, high=54.8, low=52.0, close=54.4), ck.Bar(open=54.4, high=55.0, low=52.9, close=53.2), ck.Bar(open=53.4, high=54.8, low=53.2, close=54.5), ck.Bar(open=54.4, high=54.6, low=53.4, close=53.8)), notes=(ck.Note(label='range 4.0'), ck.Note(x=1, label='range 3.2'), ck.Note(x=2, label='range 2.8'), ck.Note(x=3, label='range 2.1'), ck.Note(x=4, label='range 1.6'), ck.Note(x=5, label='range 1.2')), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.68, y0=0.25, x1=0.84, y1=0.43, color='gold', at=(0.63, 0.48)), dk.Mark(number=2, kind='line', x0=0.8, y0=0.22, x1=0.8, y1=0.43, color='red', at=(0.88, 0.47)), dk.Mark(number=3, kind='line', x0=0.88, y0=0.18, x1=0.88, y1=0.49, color='blue', at=(0.92, 0.6))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r4',
'letter': 'O'},
'r4-w': {'items': (ck.Cell(name='Inside Month/NR5: six monthly bars of ours', note='', panes=(ck.Pane(bars=(ck.Bar(open=28.0, high=30.0, low=18.0, close=26.0), ck.Bar(open=26.0, high=29.0, low=19.0, close=27.0), ck.Bar(open=27.0, high=30.0, low=21.0, close=28.0), ck.Bar(open=28.0, high=31.0, low=24.0, close=29.0), ck.Bar(open=29.0, high=30.0, low=25.0, close=28.0), ck.Bar(open=28.0, high=36.0, low=27.0, close=36.0)), notes=(ck.Note(label='range 12'), ck.Note(x=1, label='range 10'), ck.Note(x=2, label='range 9'), ck.Note(x=3, label='range 7'), ck.Note(x=4, label='range 5'), ck.Note(x=5, label='breakout')), height=1.75),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.53, y0=0.38, x1=0.7, y1=0.59, color='gold', at=(0.49, 0.63), size=0.3), dk.Mark(number=2, kind='line', x0=0.67, y0=0.39, x1=0.67, y1=0.55, color='red', at=(0.74, 0.63), size=0.3), dk.Mark(number=3, kind='circle', x0=0.78, y0=0.18, x1=0.84, y1=0.49, color='blue', at=(0.91, 0.55), size=0.3)),
'old_size': (8.222999781277341, 3.84),
'owner': 'r4',
'letter': 'W'}}

DATA['r1-j']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 0, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 0, 'low')}, {'number': 4, 'color': 'purple', 'target': (0, 0, 'close')}]
DATA['r1-m']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'close')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'close')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'group')}, {'number': 4, 'color': 'purple', 'target': (0, 3, 'close')}]
DATA['r1-g']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'group')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'group')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'group')}, {'number': 4, 'color': 'purple', 'target': (0, 3, 'group')}]
DATA['r1-p']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'line')}, {'number': 2, 'color': 'red', 'target': (0, 3, 'line')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'line')}, {'number': 4, 'color': 'purple', 'target': (0, 4, 'line')}]
DATA['r1-r']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'low')}, {'number': 4, 'color': 'purple', 'target': (0, 2, 'close')}]
DATA['r3a-k']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}, {'number': 4, 'color': 'purple', 'target': (0, 1, 'volume')}]
DATA['r3a-a']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'open')}, {'number': 4, 'color': 'purple', 'target': (1, 1, 'level:40')}, {'number': 5, 'color': 'gold', 'target': (1, 1, 'volume')}, {'number': 6, 'color': 'red', 'target': (1, 1, 'close')}]
DATA['r3a-l']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'close')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'close')}]
DATA['r3a-m']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'volume')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'volume')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'volume')}]
DATA['r3a-n']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'gap')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 3, 'gap')}]
DATA['r3b-la'].update(spans={(0, 2, 'span')})
DATA['r3b-la']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 2, 'span')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'close')}]
DATA['r3b-lb']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 0, 'high')}]
DATA['r3b-lc']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'high')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'open')}]
DATA['r3b-ld']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 2, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'volume')}]
DATA['r3b-lg']['line_format'] = '{:.2f}'
DATA['r3b-lg']['bar_offsets'] = {1: 9}
DATA['r3b-lj']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'level:40.0')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}]
DATA['r3b-le']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'high')}, {'number': 2, 'color': 'red', 'target': (1, 1, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}, {'number': 4, 'color': 'purple', 'target': (1, 1, 'close')}]
DATA['r3b-lf']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'level:60.0')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}, {'number': 4, 'color': 'purple', 'target': (0, 0, 'level:62.5')}]
DATA['r3b-lg']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 9, 'line')}, {'number': 2, 'color': 'red', 'target': (1, 3, 'line')}, {'number': 3, 'color': 'blue', 'target': (1, 4, 'line')}, {'number': 4, 'color': 'purple', 'target': (1, 5, 'line')}]
DATA['r3b-lh']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 3, 'close')}]
DATA['r3b-li']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 3, 'close')}]
DATA['r3b-lk']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'close')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'close')}]
DATA['r4-t'] = {'items': (), 'special': 'nr_table', 'owner': 'r4', 'letter': 'T',
    'old_marks': (dk.Mark(number=1, kind='circle', x0=0, y0=0, x1=0, y1=0), dk.Mark(number=2, kind='circle', x0=0, y0=0, x1=0, y1=0)),
    'caption': 'The ranges are invented for teaching.',
    'nr_ranges': (1.0, 4.0, 3.2, 2.8, 2.1, 1.6, 1.2),
    'targets': [{'number': 1, 'color': 'gold', 'target': (0, 0, 'yes')}, {'number': 2, 'color': 'red', 'target': (0, 7, 'answer')}]}
DATA['r4-n']['caption'] = 'Prices are invented for teaching.'
DATA['r4-n']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'level:52.0')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'high')}]
DATA['r4-v']['caption'] = 'Prices are invented for teaching.'
DATA['r4-v']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'level:48.0')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'low')}]
DATA['r4-o']['caption'] = 'Prices are invented for teaching.'
DATA['r4-o']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 5, 'span')}, {'number': 2, 'color': 'red', 'target': (0, 4, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 4, 'low')}]
# All six bars on one page; prices only where the sentences read them.
DATA['r4-o'].update(one_page=True, stack_captions=True, spans={(0, 5, 'span')},
                    bar_labels={0: '', 1: '', 2: '', 3: '', 4: 'HL', 5: 'HL'})
DATA['r4-w']['caption'] = 'Prices are invented for teaching.'
DATA['r4-w']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 4, 'span')}, {'number': 2, 'color': 'red', 'target': (0, 4, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 5, 'close')}]
DATA['r4-w'].update(one_page=True, stack_captions=True, spans={(0, 4, 'span')},
                    bar_labels={0: '', 1: '', 2: '', 3: 'HL', 4: 'HLC', 5: 'HC'})

DATA['r1-m']['groups'] = {(0,2,'group'): (0,2,3)}

# Part 2, section 7.2. One chart per generic form in Figures 7.4 to 7.12,
# drawn from Lim's own label for that form with invented prices, plus the
# reliability and barrier examples. A bullish form mirrors its bearish twin
# about PHP 45 (each price p becomes 90 - p), so it keeps the label's shape.
SPLIT = 8.7   # inches: a chart that shares its slide with the book's drawing


def _mirror(rows):
    return tuple((round(90-o, 2), round(90-l, 2), round(90-h, 2), round(90-c, 2))
                 for o, h, l, c in rows)


def _form(letter, name, rows, targets, *, note='', volume=(), levels=(),
          groups=None, width=SPLIT):
    bars = tuple(ck.Bar(open=o, high=h, low=l, close=c) for o, h, l, c in rows)
    strokes = tuple(ck.Stroke(points=((0, value), (len(rows) - 1, value)),
                              dashed=True, label=label) for label, value in levels)
    panes = (ck.Pane(bars=bars, strokes=strokes),)
    if volume:
        panes += (ck.Pane(columns=tuple(volume)),)
    spec = {'items': (ck.Cell(name=name, note=note, panes=panes),), 'special': '',
            'owner': 'p2', 'letter': letter, 'old_marks': (),
            'targets': [{'number': n, 'color': ('gold', 'red', 'blue', 'purple')[n - 1],
                         'target': t} for n, t in enumerate(targets, 1)]}
    if groups:
        spec['groups'] = groups
    if width:
        spec['width'] = width
    return spec


def _pair(bear, bull, *, levels=(), bull_levels=(), **kwargs):
    """A bearish form and its bullish mirror, keyed by their two letters."""
    (b_letter, b_name, rows), (u_letter, u_name) = bear, bull
    # Turned upside down, a high becomes a low, so the marks swap with it.
    swap = {'high': 'low', 'low': 'high'}
    targets = kwargs.pop('targets')
    flipped = tuple((c, i, swap.get(name, name)) for c, i, name in targets)
    return {
        'p2-' + b_letter.lower(): _form(b_letter, b_name, rows, targets, levels=levels, **kwargs),
        'p2-' + u_letter.lower(): _form(u_letter, u_name, _mirror(rows), flipped, levels=bull_levels, **kwargs),
    }


MIDDLE = {(0, 1, 'group'): (0, 1, 2)}
P2 = {}
# Figures 7.4 and 7.5: the seven single and double bar forms, p. 212.
P2.update(_pair(('BA', 'Bearish form 1: key reversal bar', ((50.2, 51.0, 49.9, 50.8), (51.4, 52.0, 49.8, 50.3))),
                ('UA', 'Bullish form 1: key reversal bar'),
                levels=(('prior high 51.00', 51.0),), bull_levels=(('prior low 39.00', 39.0),),
                targets=((0, 1, 'open'), (0, 1, 'range'), (0, 1, 'close'))))
P2.update(_pair(('BB', 'Bearish form 2: close below a previous low', ((50.4, 51.2, 50.2, 51.0), (51.1, 51.5, 49.4, 49.6))),
                ('UB', 'Bullish form 2: close above a previous high'),
                levels=(('prior low 50.20', 50.2),), bull_levels=(('prior high 39.80', 39.8),),
                targets=((0, 0, 'low'), (0, 1, 'range'), (0, 1, 'close'))))
P2.update(_pair(('BC', 'Bearish form 3: close below a gap', ((51.2, 52.0, 51.0, 51.8), (50.6, 50.6, 49.6, 49.8))),
                ('UC', 'Bullish form 3: close above a gap'),
                levels=(('prior low 51.00', 51.0),), bull_levels=(('prior high 39.00', 39.0),),
                targets=((0, 1, 'open'), (0, 1, 'gap'), (0, 1, 'close'))))
P2.update(_pair(('BD', 'Bearish form 4: inside bar', ((49.4, 52.0, 49.0, 51.8), (51.6, 51.8, 50.8, 51.0))),
                ('UD', 'Bullish form 4: inside bar'), volume=(3.0, 0.9),
                targets=((0, 0, 'range'), (0, 1, 'range'), (0, 1, 'volume'))))
P2.update(_pair(('BE', 'Bearish form 5: overextended bar', ((50.0, 50.8, 49.8, 50.6), (51.0, 54.8, 50.8, 51.0))),
                ('UE', 'Bullish form 5: overextended bar'),
                targets=((0, 0, 'range'), (0, 1, 'range'), (0, 1, 'close'))))
P2.update(_pair(('BF', 'Bearish form 6: outside bar', ((51.0, 51.4, 50.8, 51.2), (51.3, 51.9, 49.9, 50.0))),
                ('UF', 'Bullish form 6: outside bar'),
                targets=((0, 0, 'range'), (0, 1, 'range'), (0, 1, 'close'))))
P2.update(_pair(('BG', 'Bearish form 7: two large bars', ((49.2, 51.6, 49.0, 51.6), (51.5, 51.8, 49.2, 49.4))),
                ('UG', 'Bullish form 7: two large bars'),
                targets=((0, 0, 'close'), (0, 1, 'close'))))
# The reliability condition: an overextended last bar near its extreme on
# high volume, p. 212.
P2.update(_pair(('RL', 'A bearish last bar worth trusting more', ((50.6, 51.4, 50.4, 51.2), (51.3, 51.6, 47.6, 47.8))),
                ('RM', 'A bullish last bar worth trusting more'), volume=(1.5, 4.5), width=None,
                targets=((0, 1, 'range'), (0, 1, 'close'), (0, 1, 'volume'))))
# The last-bar size contrast shown on the multiple bar and bullish triple
# rule slides: an ordinary PHP 1.00 bar beside an overextended PHP 4.00 bar.
_OVER = ((50.0, 50.8, 49.8, 50.6), (51.0, 54.8, 50.8, 51.0))
_OVER_T = ((0, 0, 'range'), (0, 1, 'range'), (0, 1, 'close'))
P2['p2-ob'] = _form('OB', 'Bearish last bar: ordinary beside overextended', _OVER, _OVER_T)
P2['p2-oa'] = _form('OA', 'Bullish last bar: ordinary beside overextended', _mirror(_OVER), _OVER_T)
P2['p2-oc'] = _form('OC', 'Bullish last bar: ordinary beside overextended', _mirror(_OVER), _OVER_T)
# Figures 7.6 to 7.9: the six triple bar forms, pp. 213 to 215.
P2['p2-tr'] = _form('TR', 'A triple pattern that meets the rules',
                    ((49.2, 51.0, 48.0, 50.8), (50.6, 50.9, 50.1, 50.3), (50.2, 50.4, 44.4, 44.6)),
                    volume=(2.6, 0.7, 4.2), width=None,
                    targets=((0, 0, 'range'), (0, 1, 'range'), (0, 1, 'volume'), (0, 2, 'range')))
_TRIPLE_1 = ((49.2, 50.6, 49.0, 50.5), (50.8, 52.8, 50.4, 50.6), (50.5, 50.7, 48.8, 49.0))
# Lim states the larger-middle-volume exception for bearish pattern 1 only,
# so the bullish mirror carries no volume to read.
P2['p2-ta'] = _form('TA', 'Bearish triple 1: large middle bar', _TRIPLE_1, volume=(1.8, 3.6, 3.0),
                    targets=((0, 0, 'close'), (0, 1, 'close'), (0, 1, 'volume'), (0, 2, 'close')))
P2['p2-tg'] = _form('TG', 'Bullish triple 1: large middle bar', _mirror(_TRIPLE_1),
                    targets=((0, 0, 'close'), (0, 1, 'close'), (0, 2, 'close')))
P2.update(_pair(('TB', 'Bearish triple 2: narrow middle bar', ((49.0, 51.2, 48.8, 51.0), (50.6, 50.9, 50.3, 50.5), (50.4, 50.7, 48.4, 48.6))),
                ('TH', 'Bullish triple 2: narrow middle bar'), volume=(2.8, 0.8, 3.2),
                targets=((0, 0, 'close'), (0, 1, 'range'), (0, 1, 'volume'), (0, 2, 'close'))))
P2.update(_pair(('TC', 'Bearish triple 3: a gap and a close back below it', ((49.0, 50.0, 48.8, 49.8), (50.6, 51.4, 50.4, 51.2), (51.0, 51.2, 49.4, 49.6))),
                ('TI', 'Bullish triple 3: a gap and a close back above it'),
                targets=((0, 1, 'gap'), (0, 1, 'close'), (0, 2, 'close'))))
P2.update(_pair(('TD', 'Bearish triple 4: single island reversal bar', ((49.2, 50.0, 49.0, 49.8), (50.6, 51.0, 50.4, 50.7), (49.8, 50.0, 48.4, 48.6))),
                ('TJ', 'Bullish triple 4: single island reversal bar'), volume=(2.0, 0.7, 2.6),
                targets=((0, 1, 'gap'), (0, 1, 'volume'), (0, 2, 'gap'), (0, 2, 'close'))))
P2.update(_pair(('TE', 'Bearish triple 5: third bar engulfs the second', ((49.2, 50.0, 49.0, 49.8), (50.5, 50.9, 50.4, 50.8), (50.9, 51.2, 49.2, 49.4))),
                ('TK', 'Bullish triple 5: third bar engulfs the second'), volume=(2.0, 0.6, 3.0),
                targets=((0, 1, 'gap'), (0, 1, 'volume'), (0, 2, 'range'), (0, 2, 'close'))))
P2.update(_pair(('TF', 'Bearish triple 6: close below the second low', ((49.0, 50.4, 48.8, 50.2), (50.3, 51.4, 50.1, 51.3), (51.2, 51.3, 49.6, 49.8))),
                ('TL', 'Bullish triple 6: close above the second high'), volume=(2.2, 0.8, 2.8),
                targets=((0, 1, 'close'), (0, 1, 'volume'), (0, 2, 'close'))))
# Figures 7.10 and 7.11: the four multiple bar forms, pp. 214 to 216. Two
# intermediate bars stand for Lim's several, so all four prices still fit.
P2.update(_pair(('XA', 'Bearish multiple 1: narrow bars near the first high', ((48.4, 50.2, 48.2, 50.0), (50.0, 50.4, 49.8, 50.1), (50.1, 50.5, 49.9, 50.2), (50.1, 50.3, 48.0, 48.2))),
                ('XE', 'Bullish multiple 1: narrow bars near the first low'), width=None, groups=MIDDLE,
                targets=((0, 0, 'close'), (0, 1, 'group'), (0, 3, 'close'))))
P2.update(_pair(('XB', 'Bearish multiple 2: wide bars closing near their lows', ((48.4, 50.2, 48.2, 50.0), (51.8, 52.0, 50.0, 50.2), (51.9, 52.2, 50.1, 50.3), (50.2, 50.4, 48.0, 48.2))),
                ('XF', 'Bullish multiple 2: wide bars closing near their highs'), width=None, groups=MIDDLE,
                volume=(2.0, 3.8, 3.6, 3.0),
                targets=((0, 0, 'close'), (0, 1, 'group'), (0, 1, 'volumes:2'), (0, 3, 'close'))))
P2.update(_pair(('XC', 'Bearish multiple 3: narrow bars inside the first', ((48.2, 50.4, 48.0, 50.2), (49.4, 49.7, 49.2, 49.5), (49.5, 49.8, 49.3, 49.4), (50.2, 50.4, 47.8, 48.0))),
                ('XG', 'Bullish multiple 3: narrow bars inside the first'), width=None, groups=MIDDLE,
                targets=((0, 0, 'close'), (0, 1, 'group'), (0, 3, 'close'))))
P2.update(_pair(('XD', 'Bearish multiple 4: island reversal formation', ((48.2, 50.0, 48.0, 49.8), (50.6, 50.9, 50.4, 50.7), (50.7, 51.0, 50.5, 50.8), (49.8, 50.0, 48.2, 48.4))),
                ('XH', 'Bullish multiple 4: island reversal formation'), width=None, groups=MIDDLE,
                targets=((0, 0, 'high'), (0, 1, 'group'), (0, 3, 'high'), (0, 3, 'close'))))
# Figure 7.12: the two bullish continuation bars, pp. 216 to 217.
P2['p2-ca'] = _form('CA', 'Continuation 1: a high-volume breach of the prior high',
                    ((48.4, 51.0, 48.2, 50.8), (50.9, 53.4, 50.6, 53.2)), volume=(2.0, 4.0),
                    levels=(('prior high 51.00', 51.0),),
                    targets=((0, 0, 'high'), (0, 1, 'close'), (0, 1, 'volume')))
P2['p2-cb'] = _form('CB', 'Continuation 2: a halfway retrace, then a breach',
                    ((48.2, 52.0, 48.0, 51.6), (51.4, 52.8, 50.0, 52.6)), volume=(2.2, 4.2),
                    levels=(('midpoint 50.00', 50.0),),
                    targets=((0, 1, 'low'), (0, 1, 'high'), (0, 1, 'volume')))
# Barrier proximity, p. 217: the same key reversal bar at and away from a
# barrier, then the bullish converse at support.
_KEY_AT_60 = ((58.6, 59.8, 58.4, 59.6), (60.2, 60.6, 58.6, 59.0))
P2['p2-ra'] = _form('RA', 'Key reversal bar at resistance', _KEY_AT_60, width=None,
                    levels=(('resistance 60.00', 60.0),),
                    targets=((0, 1, 'level:60.0'), (0, 1, 'high'), (0, 1, 'close')))
P2['p2-rb'] = _form('RB', 'The same bar with no barrier nearby', _KEY_AT_60, width=None,
                    targets=((0, 1, 'high'), (0, 1, 'close')))
P2['p2-rc'] = _form('RC', 'Bullish key reversal bar at support',
                    ((41.4, 41.6, 40.2, 40.4), (39.8, 41.4, 39.4, 41.0)), width=None,
                    levels=(('support 40.00', 40.0),),
                    targets=((0, 1, 'level:40.0'), (0, 1, 'low'), (0, 1, 'close')))
# Figure 7.13's warnings, pp. 217 to 218, with an invented path: 40 to 80
# in twelve bars, two one-point dips, the last bar 3 points over the band.
P2['p2-wa'] = {'items': (ck.Cell(name='An exponential rise into an upper band', panes=(
                   ck.Pane(line=(40, 41, 42, 44, 43, 46, 49, 53, 52, 58, 66, 80),
                           strokes=(ck.Stroke(points=((0, 77), (11, 77)), dashed=True,
                                              label='upper band 77'),)),)),),
               'special': '', 'owner': 'p2', 'letter': 'WA', 'old_marks': (), 'level_ink': True,
               'targets': [{'number': 1, 'color': 'gold', 'target': (0, 10, 'line'), 'angles': (300, 315)},
                           {'number': 2, 'color': 'red', 'target': (0, 8, 'line'), 'angles': (270, 255)},
                           {'number': 3, 'color': 'blue', 'target': (0, 11, 'line'), 'angles': (50, 40, 60)}]}
DATA.update(P2)


for _key in ('r4-n', 'r4-v', 'r4-o', 'r4-w', 'r4-t'):
    DATA[_key]['marks_by_sentence'] = True

# Chart M: volume is the point, so its columns get the Part 2 boxes and room.
DATA['r3a-m'].update(volume_boxes=True, volume_top=0.84)

# Slides that named a shape or a price relationship without showing it
# (28 October 2026 audit). A close against the previous low is an ordinary
# two-bar chart; the rest are painted by shapecharts_chapter07.
import shapecharts_chapter07 as sc


def _paint(letter, painter, targets, caption):
    return {'items': (), 'special': 'paint', 'paint': painter, 'owner': 'sh', 'letter': letter,
            'old_marks': (), 'caption': caption, 'group_gap': .18,
            'targets': [{'number': n, 'color': t[0], 'target': t[1], **({'angles': t[2]} if len(t) > 2 else {})}
                        for n, t in enumerate(targets, 1)]}


DRAWN = 'The shapes are sketches of ours; they carry no prices.'
SH = {
    'sh-hs': _paint('HS', sc.paint_head_shoulders,
                    (('gold', (0, 0, 'group')), ('red', (0, 1, 'group'))), DRAWN),
    'sh-b': {'items': (ck.Cell(name='A close below the previous low', panes=(ck.Pane(
        bars=(ck.Bar(open=48.1, high=49.2, low=47.9, close=49.0), ck.Bar(open=49.1, high=49.4, low=47.3, close=47.5)),
        strokes=(ck.Stroke(points=((0, 47.9), (1, 47.9)), dashed=True),),
        notes=(ck.Note(x=0, label='the previous bar'), ck.Note(x=1, label='the next bar'))),)),),
        'special': '', 'owner': 'sh', 'letter': 'LW', 'old_marks': (), 'span_levels': True,
        'caption': 'Prices are invented for teaching.', 'group_gap': .1,
        'targets': [{'number': 1, 'color': 'gold', 'target': (0, 0, 'low')},
                    {'number': 2, 'color': 'red', 'target': (0, 1, 'close')}]},
    'sh-x': _paint('EX', sc.paint_expectation,
                   (('gold', (0, 0, 'group')), ('red', (0, 1, 'group'))),
                   'The bars are drawn to show direction only; they carry no prices.'),
    'sh-t': _paint('TT', sc.paint_two_trends,
                   (('gold', (0, 11, 'close')), ('red', (0, 10, 'high')),
                    ('blue', (0, 0, 'group')), ('purple', (0, 1, 'group'))),
                   'Prices are invented for teaching.'),
    'sh-c': _paint('FC', sc.paint_four_cases,
                   (('gold', (0, 0, 'group')), ('red', (0, 1, 'group')),
                    ('blue', (0, 2, 'group')), ('purple', (0, 3, 'group'))),
                   'The bars are drawn to show direction only; they carry no prices.'),
    'sh-hn': _paint('HN', sc.paint_head_shoulders_trend if hasattr(sc, 'paint_head_shoulders_trend') else sc.paint_trend_shapes,
                    (('gold', (0, 0, 'group'), (90, 60)), ('red', (0, 1, 'group')), ('blue', (0, 2, 'group'))),
                    'Prices are invented for teaching.'),
    'sh-pu': _paint('PU', lambda c: sc.paint_prior_bar(c, up=True),
                    (('gold', (0, 0, 'ref'), (45, 60, 75)), ('red', (0, 1, 'today')),
                     ('blue', (0, 2, 'today')), ('purple', (0, 3, 'ref'), (45, 60, 75))),
                    'Prices are invented for teaching.'),
    'sh-pd': _paint('PD', lambda c: sc.paint_prior_bar(c, up=False),
                    (('gold', (0, 0, 'ref'), (45, 60, 75)), ('red', (0, 1, 'today')),
                     ('blue', (0, 2, 'today')), ('purple', (0, 3, 'ref'), (315, 300, 285))),
                    'Prices are invented for teaching.'),
    'sh-g': _paint('GP', sc.paint_gap,
                   (('gold', (0, 0, 'group')), ('red', (0, 1, 'close')),
                    ('blue', (0, 2, 'group')), ('purple', (0, 3, 'close'))),
                   'Prices are invented for teaching.'),
}
SH['sh-t']['group_gap'] = .22   # the rise's box sits close to the formation's bars
DATA.update(SH)

# The 16 reversal characteristics, two sketches to a slide (slides 111 to 118
# of the earlier build). Marks 1 and 2 are the first sketch's, 3 and 4 the second's.
def _characteristic_chart(n):
    left, right = sc.CHARACTERISTICS[n], sc.CHARACTERISTICS[n + 1]
    targets = []
    for number, feature in enumerate(left['features'] + right['features'], 1):
        box = feature[0] == 'box'
        targets.append((('gold', 'red', 'blue', 'purple')[number - 1],
                        (0, number, 'group' if box else 'dot'), *(((0, 15, 345),) if box else ())))
    volume = n in (15,)
    caption = ('The sketches and the volumes are invented from the numbers on the slide.'
               if n + 1 == 16 or n == 15 else
               'The sketches are invented from the numbers on the slide.')
    return _paint('K%d' % n, sc.paint_characteristics(left, right), targets, caption)


SH.update({'sh-k%d' % n: _characteristic_chart(n) for n in range(1, 16, 2)})
DATA.update({'sh-k%d' % n: SH['sh-k%d' % n] for n in range(1, 16, 2)})


# Part 3 and 4 reading (29 October 2026): a reversal chart draws the trend it
# reverses. ``_after_trend`` puts the run in front of a chart's first bar and
# moves every bar index, level line, note and mark target along with it.
def _after_trend(key, bars, volumes=(), label='after a rise', level_from=None):
    from dataclasses import replace
    n = len(bars)
    spec = DATA[key]
    cell = spec['items'][0]
    panes = list(cell.panes)
    price = panes[0]
    notes = tuple(replace(m, x=m.x + n) for m in price.notes)
    strokes = tuple(replace(t, points=tuple((x + n, y) for x, y in t.points)) for t in price.strokes)
    if level_from is not None:
        strokes = tuple(replace(t, points=((level_from, t.points[0][1]),) + t.points[1:])
                        for t in strokes)
    panes[0] = replace(price, bars=tuple(bars) + price.bars, strokes=strokes, notes=notes)
    if len(panes) > 1 and panes[1].columns:
        vol = panes[1]
        assert len(volumes) == n
        panes[1] = replace(vol, columns=tuple(volumes) + vol.columns,
                           tags=tuple((i + n, t) for i, t in vol.tags))
    note = label + ('; ' + cell.note if cell.note else '')
    spec['items'] = (replace(cell, panes=tuple(panes), note=note),) + tuple(spec['items'][1:])
    spec['targets'] = [{**t, 'target': (t['target'][0], t['target'][1] + n, t['target'][2])}
                       if t['target'][0] == 0 else t for t in spec['targets']]
    spec['spans'] = {(c, i + n, k) if c == 0 else (c, i, k) for c, i, k in spec.get('spans', ())}
    # The run stays on the pattern's own page and carries no price labels.
    spec['one_page'] = True
    spec['bar_labels'] = {i: '' for i in range(n)}
    spec['run'] = n

# Chart K, and its bullish converse drawn beside it for slide 148.
DATA['r3a-kb'] = {**DATA['r3a-k'], 'letter': 'KB', 'items': (ck.Cell(
    name='Bullish key reversal: yesterday and today',
    panes=(ck.Pane(bars=(ck.Bar(open=42.0, high=42.2, low=41.0, close=41.5),
                         ck.Bar(open=41.3, high=43.4, low=40.5, close=43.2)),
                   strokes=(ck.Stroke(points=((0, 41.0), (1, 41.0)), dashed=True, label='Prior low 41.00'),
                            ck.Stroke(points=((0, 41.5), (1, 41.5)), dashed=True, label='Prior close 41.50'))),
           ck.Pane(columns=(2.0, 4.0)))),),
    'targets': [{'number': 1, 'color': 'gold', 'target': (0, 1, 'low')},
                {'number': 2, 'color': 'red', 'target': (0, 1, 'close')},
                {'number': 3, 'color': 'blue', 'target': (0, 1, 'volume')}]}
_after_trend('r3a-kb', (ck.Bar(open=44.6, high=44.8, low=43.8, close=44.0),
                        ck.Bar(open=43.9, high=44.0, low=42.8, close=43.0),
                        ck.Bar(open=42.9, high=43.0, low=41.9, close=42.1)),
             volumes=(1.5, 1.7, 1.9), label='after a fall')
_after_trend('r3a-k', (ck.Bar(open=48.4, high=49.0, low=48.2, close=48.6),
                       ck.Bar(open=48.7, high=49.7, low=48.5, close=49.4),
                       ck.Bar(open=49.5, high=50.6, low=49.3, close=50.3)),
             volumes=(1.4, 1.6, 1.8))
_after_trend('r3a-l', (ck.Bar(open=47.2, high=48.4, low=47.0, close=48.2),
                       ck.Bar(open=48.3, high=49.4, low=48.1, close=49.2),
                       ck.Bar(open=49.3, high=50.3, low=49.1, close=50.0)),
             volumes=(1.6, 1.8, 2.0))
_after_trend('r3b-lk', (ck.Bar(open=46.4, high=47.2, low=46.2, close=47.0),
                        ck.Bar(open=47.0, high=48.2, low=46.9, close=48.0),
                        ck.Bar(open=48.1, high=49.3, low=47.8, close=49.1)))
_after_trend('r3a-m', (ck.Bar(open=48.4, high=48.6, low=47.8, close=48.0),
                       ck.Bar(open=48.0, high=48.1, low=47.0, close=47.2),
                       ck.Bar(open=47.1, high=47.2, low=46.2, close=46.3)),
             volumes=(1.8, 2.0, 2.2), label='after a fall')
_after_trend('r3b-la', (ck.Bar(open=45.6, high=46.8, low=45.4, close=46.6),
                        ck.Bar(open=46.7, high=48.0, low=46.5, close=47.8),
                        ck.Bar(open=47.9, high=49.0, low=47.6, close=48.8)),
             volumes=(1.2, 1.3, 1.4))
_after_trend('r3b-lb', (ck.Bar(open=45.0, high=46.4, low=44.8, close=46.2),
                        ck.Bar(open=46.3, high=48.2, low=46.0, close=48.0),
                        ck.Bar(open=48.1, high=50.0, low=47.9, close=49.8)),
             volumes=(1.5, 1.8, 2.2))
_after_trend('r3b-lc', (ck.Bar(open=57.6, high=58.8, low=57.4, close=58.6),
                        ck.Bar(open=58.7, high=60.4, low=58.5, close=60.2),
                        ck.Bar(open=60.3, high=62.2, low=60.0, close=62.0)),
             volumes=(1.2, 1.4, 1.6))
_after_trend('r3b-lj', (ck.Bar(open=40.4, high=41.4, low=40.2, close=41.2),
                        ck.Bar(open=41.2, high=42.4, low=41.0, close=42.2),
                        ck.Bar(open=42.2, high=43.4, low=42.0, close=43.2),
                        ck.Bar(open=43.2, high=43.5, low=41.7, close=41.9)),
             volumes=(2.0, 2.2, 2.4, 1.9), level_from=0)
_after_trend('r3a-a', (ck.Bar(open=57.6, high=58.8, low=57.4, close=58.6),
                       ck.Bar(open=58.7, high=60.4, low=58.5, close=60.2),
                       ck.Bar(open=60.3, high=62.2, low=60.0, close=62.0)),
             volumes=(1.2, 1.4, 1.6))
_after_trend('r4-n', (ck.Bar(open=56.0, high=56.4, low=54.6, close=54.8),
                      ck.Bar(open=54.7, high=55.0, low=53.0, close=53.2),
                      ck.Bar(open=53.1, high=53.4, low=51.2, close=51.6)), label='after a fall')
_after_trend('r4-v', (ck.Bar(open=43.8, high=45.0, low=43.6, close=44.8),
                      ck.Bar(open=44.9, high=46.8, low=44.7, close=46.6),
                      ck.Bar(open=46.7, high=48.6, low=46.5, close=48.4)))
_after_trend('p2-tr', (ck.Bar(open=45.2, high=46.2, low=45.0, close=46.0),
                       ck.Bar(open=46.0, high=47.4, low=45.8, close=47.2),
                       ck.Bar(open=47.3, high=48.8, low=47.1, close=48.6)),
             volumes=(1.8, 2.0, 2.2))

from chartlayout_chapter07 import artwork
CHARTS = artwork(DATA)
