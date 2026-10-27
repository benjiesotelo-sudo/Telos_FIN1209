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
'r3a-m': {'items': (ck.Cell(name='Bullish three-bar reversal', note='strong outer bars; quiet middle bar', panes=(ck.Pane(bars=(ck.Bar(open=42.0, high=44.0, low=41.0, close=43.8), ck.Bar(open=43.7, high=44.1, low=43.2, close=43.5), ck.Bar(open=43.4, high=46.8, low=43.0, close=46.5)), notes=(ck.Note(label='L 41.00', dx=-20, dy=-10, y=41.0), ck.Note(label='H 44.00', dx=-20, dy=8, y=44.0), ck.Note(x=1, label='L 43.20', dx=-20, dy=-10, y=43.2), ck.Note(x=1, label='H 44.10', dx=18, dy=8, y=44.1), ck.Note(x=1, label='middle C 43.50', dx=18, dy=7, y=43.5, notice=True), ck.Note(x=2, label='C 46.50', dx=18, dy=-8, y=46.5, notice=True)), height=1.7), ck.Pane(columns=(4.0, 0.6, 4.2), tags=((0, '4.0m'), (1, '0.6m'), (2, '4.2m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.22, y0=0.75, x1=0.29, y1=0.84, color='gold', at=(0.14, 0.55)), dk.Mark(number=2, kind='circle', x0=0.47, y0=0.75, x1=0.54, y1=0.84, color='red', at=(0.42, 0.7)), dk.Mark(number=3, kind='circle', x0=0.73, y0=0.75, x1=0.8, y1=0.84, color='blue', at=(0.86, 0.7))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3a',
'letter': 'M'},
'r3a-n': {'items': (ck.Cell(name='Bearish island reversal', note='gap up, isolated bars, gap down', panes=(ck.Pane(bars=(ck.Bar(open=48.0, high=50.0, low=47.5, close=49.5), ck.Bar(open=50.8, high=52.0, low=50.6, close=51.5), ck.Bar(open=51.4, high=52.2, low=50.9, close=51.1), ck.Bar(open=49.4, high=50.0, low=48.2, close=48.8)), strokes=(ck.Stroke(points=((0, 50.0), (3, 50.0)), tone='quiet', dashed=True, label='prior high 50.00', dx=-24, dy=-10),), notes=(ck.Note(x=1, label='gap-up O 50.80', dx=-85, dy=15, y=50.8, notice=True), ck.Note(x=2, label='island', dx=18, dy=-8, y=51.5, notice=True), ck.Note(x=3, label='gap-down O 49.40', dx=-82, dy=15, y=49.4, notice=True)), height=1.7), ck.Pane(columns=(2.3, 0.7, 0.6, 2.1), tags=((0, '2.3m'), (1, '0.7m'), (2, '0.6m'), (3, '2.1m')), height=0.55))),),
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
'r3b-lc': {'items': (ck.Cell(name='Exhaustion bar', note='wide bar opens above the prior high and is followed without a gap', panes=(ck.Pane(bars=(ck.Bar(open=62.0, high=65.0, low=61.0, close=64.0), ck.Bar(open=65.4, high=66.2, low=60.0, close=60.5), ck.Bar(open=60.2, high=62.0, low=59.0, close=61.2)), strokes=(ck.Stroke(points=((0, 65.0), (2, 65.0)), tone='quiet', dashed=True, label='prior high 65.00', dx=-20, dy=-10),), notes=(ck.Note(x=1, label='O 65.40', dx=18, dy=8, y=65.4, notice=True), ck.Note(x=1, label='H 66.20', dx=18, dy=8, y=66.2, notice=True), ck.Note(x=1, label='L 60.00', dx=-18, dy=-10, y=60.0), ck.Note(x=1, label='C 60.50', dx=18, dy=-4, y=60.5, notice=True), ck.Note(x=2, label='next O 60.20', dx=18, dy=-8, y=60.2, notice=True)), height=1.8), ck.Pane(columns=(2.0, 5.5, 2.2), tags=((0, '2.0m'), (1, '5.5m'), (2, '2.2m')), height=0.55))),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='line', x0=0.18, y0=0.27, x1=0.48, y1=0.27, color='gold', at=(0.17, 0.21)), dk.Mark(number=2, kind='box', x0=0.48, y0=0.12, x1=0.6, y1=0.78, color='red', at=(0.66, 0.19)), dk.Mark(number=3, kind='line', x0=0.72, y0=0.6, x1=0.8, y1=0.6, color='blue', at=(0.84, 0.54))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LC'},
'r3b-ld': {'items': (ck.Cell(name='Emotion spike', note='wide range and high volume', panes=(ck.Pane(bars=(ck.Bar(open=60.0, high=61.5, low=58.5, close=61.0), ck.Bar(open=61.0, high=62.5, low=59.5, close=62.0), ck.Bar(open=62.0, high=70.0, low=62.0, close=63.0), ck.Bar(open=63.0, high=64.0, low=61.0, close=62.0), ck.Bar(open=62.0, high=63.0, low=59.8, close=60.5), ck.Bar(open=60.5, high=61.0, low=57.8, close=58.5)), notes=(ck.Note(x=2, label='H 70.00', dx=18, dy=8, y=70.0, notice=True), ck.Note(x=2, label='L 62.00', dx=-18, dy=-10, y=62.0), ck.Note(x=3, label='C 62.00', dx=18, dy=-8, y=62.0, notice=True), ck.Note(x=4, label='C 60.50', dx=18, dy=-8, y=60.5, notice=True), ck.Note(x=5, label='C 58.50', dx=18, dy=-8, y=58.5, notice=True)), height=1.8), ck.Pane(columns=(1.5, 1.4, 6.0, 2.2, 2.0, 2.4), tags=((0, '1.5m'), (1, '1.4m'), (2, '6.0m'), (3, '2.2m'), (4, '2.0m'), (5, '2.4m')), height=0.55))),),
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
'r3b-lf': {'items': (ck.Cell(name='False upside breakout', note='the course drawing; return below resistance', panes=(ck.Pane(bars=(ck.Bar(open=58.0, high=60.0, low=57.0, close=59.0), ck.Bar(open=59.0, high=62.0, low=58.5, close=59.4)), strokes=(ck.Stroke(points=((0, 60.0), (1, 60.0)), tone='quiet', dashed=True, label='resistance 60.00', dx=-18, dy=-10), ck.Stroke(points=((0, 62.2), (1, 62.2)), tone='quiet', dashed=True, label='stop 62.20', at=1, dx=18, dy=-10)), notes=(ck.Note(x=1, label='H 62.00', dx=18, dy=8, y=62.0, notice=True), ck.Note(x=1, label='C 59.40', dx=18, dy=-6, y=59.4, notice=True)), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='line', x0=0.34, y0=0.5, x1=0.68, y1=0.5, color='gold', at=(0.25, 0.43)), dk.Mark(number=2, kind='circle', x0=0.645, y0=0.235, x1=0.674, y1=0.285, color='red', at=(0.8, 0.11)), dk.Mark(number=3, kind='circle', x0=0.645, y0=0.535, x1=0.674, y1=0.59, color='blue', at=(0.8, 0.63)), dk.Mark(number=4, kind='line', x0=0.35, y0=0.23, x1=0.68, y1=0.23, color='purple', at=(0.81, 0.3))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LF'},
'r3b-lg': {'items': (ck.Cell(name='Double Repo', note='two crossings of a forward-shifted three-day SMA', panes=(ck.Pane(bars=(ck.Bar(open=48.0, high=49.5, low=47.5, close=49.2), ck.Bar(open=49.2, high=50.2, low=48.8, close=49.6), ck.Bar(open=49.6, high=50.8, low=49.2, close=50.0), ck.Bar(open=50.0, high=51.2, low=49.6, close=50.4), ck.Bar(open=50.4, high=51.5, low=50.0, close=50.8), ck.Bar(open=50.8, high=52.0, low=50.4, close=51.2), ck.Bar(open=51.2, high=52.2, low=50.8, close=51.5), ck.Bar(open=51.5, high=52.4, low=51.0, close=51.7), ck.Bar(open=51.7, high=52.6, low=51.3, close=51.8), ck.Bar(open=51.8, high=52.0, low=50.2, close=50.8), ck.Bar(open=50.8, high=51.0, low=49.2, close=49.6), ck.Bar(open=49.6, high=51.0, low=49.3, close=50.7), ck.Bar(open=50.7, high=50.9, low=48.5, close=49.0), ck.Bar(open=49.0, high=49.5, low=46.8, close=47.5)), strokes=(ck.Stroke(points=((0, 50.0), (4, 50.0)), tone='quiet', dashed=True, label='SMA 50.00', dx=12, dy=-10),), notes=(ck.Note(x=9, label='50.80 up', dx=10, dy=8, y=50.8, notice=True), ck.Note(x=10, label='49.60 down', dx=-145, dy=-8, y=49.6, notice=True), ck.Note(x=11, label='50.70 up', dx=-10, dy=8, y=50.7, notice=True), ck.Note(x=12, label='49.00 down', dx=-60, dy=26, y=49.0, notice=True), ck.Note(x=13, label='47.50', dx=-10, dy=4, y=47.5, notice=True)), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.645, y0=0.4, x1=0.673, y1=0.45, color='gold', at=(0.57, 0.33)), dk.Mark(number=2, kind='circle', x0=0.708, y0=0.53, x1=0.735, y1=0.57, color='red', at=(0.77, 0.67)), dk.Mark(number=3, kind='box', x0=0.775, y0=0.32, x1=0.89, y1=0.7, color='blue', at=(0.94, 0.25))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LG'},
'r3b-lh': {'items': (ck.Cell(name='Bearish Hikkake', note='inside bar, false high, then short re-entry', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=52.0, low=49.0, close=51.0), ck.Bar(open=51.0, high=53.0, low=50.0, close=52.5), ck.Bar(open=52.5, high=52.8, low=48.5, close=49.0)), strokes=(ck.Stroke(points=((0, 52.0), (2, 52.0)), tone='quiet', dashed=True, label='inside high 52.00', dx=10, dy=-10),), notes=(ck.Note(label='inside high 52.00', dx=-18, dy=-8, y=52.0, notice=True), ck.Note(x=1, label='false high 53.00', dx=18, dy=8, y=53.0, notice=True), ck.Note(x=2, label='short below 49.00', dx=18, dy=-8, y=49.0, notice=True)), height=1.4),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.22, y0=0.35, x1=0.29, y1=0.78, color='gold', at=(0.16, 0.3)), dk.Mark(number=2, kind='circle', x0=0.47, y0=0.18, x1=0.53, y1=0.28, color='red', at=(0.58, 0.14)), dk.Mark(number=3, kind='arrow', x0=0.67, y0=0.6, x1=0.75, y1=0.77, color='blue', at=(0.65, 0.55))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LH'},
'r3b-li': {'items': (ck.Cell(name='Bullish Hikkake', note='inside bar, false low, then long re-entry', panes=(ck.Pane(bars=(ck.Bar(open=41.0, high=43.0, low=40.0, close=42.0), ck.Bar(open=41.0, high=42.0, low=39.0, close=40.0), ck.Bar(open=40.0, high=44.0, low=39.8, close=43.0)), strokes=(ck.Stroke(points=((0, 43.0), (2, 43.0)), tone='quiet', dashed=True, label='inside high 43.00', dx=8, dy=-10), ck.Stroke(points=((0, 40.0), (2, 40.0)), tone='quiet', dashed=True, label='inside low 40.00', dx=8, dy=10)), notes=(ck.Note(dx=-18, dy=8, y=43.0, notice=True), ck.Note(x=1, label='false low', dx=-18, dy=-8, y=39.0, notice=True), ck.Note(x=2, label='long >43.00', dx=-12, dy=8, y=43.0, notice=True)), height=1.5),)), ck.Cell(name='Bearish Hikkake', note='inside bar, false high, then short re-entry', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=52.0, low=49.0, close=51.0), ck.Bar(open=51.0, high=53.0, low=50.0, close=52.5), ck.Bar(open=52.5, high=52.8, low=48.5, close=49.0)), strokes=(ck.Stroke(points=((0, 52.0), (2, 52.0)), tone='quiet', dashed=True, label='inside high 52.00', dx=8, dy=-10), ck.Stroke(points=((0, 49.0), (2, 49.0)), tone='quiet', dashed=True, label='inside low 49.00', dx=8, dy=10)), notes=(ck.Note(dx=-18, dy=8, y=52.0, notice=True), ck.Note(x=1, label='false high', dx=18, dy=8, y=53.0, notice=True), ck.Note(x=2, label='short <49.00', dx=-12, dy=-8, y=49.0, notice=True)), height=1.5),))),
'special': '',
'old_marks': (dk.Mark(number=1, kind='box', x0=0.16, y0=0.25, x1=0.29, y1=0.72, color='gold', at=(0.1, 0.2)), dk.Mark(number=2, kind='circle', x0=0.23, y0=0.8, x1=0.27, y1=0.86, color='red', at=(0.4, 0.84)), dk.Mark(number=3, kind='circle', x0=0.35, y0=0.34, x1=0.39, y1=0.38, color='blue', at=(0.43, 0.25)), dk.Mark(number=4, kind='box', x0=0.62, y0=0.25, x1=0.68, y1=0.72, color='gold', at=(0.57, 0.2)), dk.Mark(number=5, kind='circle', x0=0.73, y0=0.21, x1=0.77, y1=0.27, color='red', at=(0.93, 0.25)), dk.Mark(number=6, kind='circle', x0=0.85, y0=0.75, x1=0.878, y1=0.8, color='blue', at=(0.95, 0.67))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r3b',
'letter': 'LI'},
'r4-n': {'items': (ck.Cell(name="Bearish Oops: bar 2 opens above bar 1's high", note='', panes=(ck.Pane(bars=(ck.Bar(open=50.0, high=52.0, low=49.5, close=51.0), ck.Bar(open=53.0, high=54.0, low=50.5, close=51.5)), strokes=(ck.Stroke(points=((0, 52.0), (1, 52.0)), dashed=True, label='bar 1 high, sell-stop 52.00'), ck.Stroke(points=((0, 54.0), (1, 54.0)), dashed=True, label='bar 2 high, stoploss 54.00')), notes=(ck.Note(label='the previous bar'), ck.Note(x=1, label='gaps up, then falls')), height=1.8),)),),
'special': '',
'old_marks': (dk.Mark(number=1, kind='circle', x0=0.64, y0=0.27, x1=0.69, y1=0.33, color='gold', at=(0.51, 0.37)), dk.Mark(number=2, kind='circle', x0=0.64, y0=0.49, x1=0.69, y1=0.55, color='red', at=(0.78, 0.62)), dk.Mark(number=3, kind='circle', x0=0.64, y0=0.21, x1=0.69, y1=0.27, color='blue', at=(0.78, 0.13))),
'old_size': (8.222999781277341, 3.84),
'owner': 'r4',
'letter': 'N'},
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
DATA['r3a-n']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'open')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 3, 'open')}]
DATA['r3b-la']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 2, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'close')}]
DATA['r3b-lb']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 0, 'high')}]
DATA['r3b-lc']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'high')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'range')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'open')}]
DATA['r3b-ld']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 2, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 2, 'volume')}, {'number': 3, 'color': 'blue', 'target': (0, 4, 'high')}]
DATA['r3b-lj']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'level:40.0')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}]
DATA['r3b-le']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'high')}, {'number': 2, 'color': 'red', 'target': (1, 1, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}, {'number': 4, 'color': 'purple', 'target': (1, 1, 'close')}]
DATA['r3b-lf']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 1, 'level:60.0')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 1, 'close')}, {'number': 4, 'color': 'purple', 'target': (0, 1, 'level:62.2')}]
DATA['r3b-lg']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 9, 'close')}, {'number': 2, 'color': 'red', 'target': (0, 10, 'close')}, {'number': 3, 'color': 'blue', 'target': (0, 11, 'close')}]
DATA['r3b-lh']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'high')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'close')}]
DATA['r3b-li']["targets"] = [{'number': 1, 'color': 'gold', 'target': (0, 0, 'range')}, {'number': 2, 'color': 'red', 'target': (0, 1, 'low')}, {'number': 3, 'color': 'blue', 'target': (0, 2, 'close')}, {'number': 4, 'color': 'gold', 'target': (1, 0, 'range')}, {'number': 5, 'color': 'red', 'target': (1, 1, 'high')}, {'number': 6, 'color': 'blue', 'target': (1, 2, 'close')}]
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
DATA['r3b-lg']['targets'][2]['target'] = (0,11,'group')
DATA['r3b-lg']['groups'] = {(0,11,'group'): (0,11,12)}

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
P2.update(_pair(('BE', 'Bearish form 5: overextended bar', ((50.0, 50.8, 49.8, 50.6), (51.0, 53.6, 50.8, 51.0))),
                ('UE', 'Bullish form 5: overextended bar'),
                targets=((0, 1, 'high'), (0, 1, 'close'))))
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
# Figures 7.6 to 7.9: the six triple bar forms, pp. 213 to 215.
P2['p2-tr'] = _form('TR', 'A triple pattern that meets the rules',
                    ((49.2, 51.0, 48.0, 50.8), (50.6, 50.9, 50.1, 50.3), (50.2, 50.4, 47.0, 47.2)),
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
               'special': '', 'owner': 'p2', 'letter': 'WA', 'old_marks': (),
               'targets': [{'number': 1, 'color': 'gold', 'target': (0, 10, 'line')},
                           {'number': 2, 'color': 'red', 'target': (0, 8, 'line')},
                           {'number': 3, 'color': 'blue', 'target': (0, 11, 'line')}]}
DATA.update(P2)


for _key in ('r4-n', 'r4-v', 'r4-o', 'r4-w', 'r4-t'):
    DATA[_key]['marks_by_sentence'] = True

from chartlayout_chapter07 import artwork
CHARTS = artwork(DATA)
