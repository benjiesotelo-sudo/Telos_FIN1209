"""Chapter 8's own charts, as plain data for the shared measured layout.

Every 'paint' entry names a painter in oscillatorcharts_chapter08. The letters
restart at A in this chapter and the output folder is build/generated/charts-08.
"""
import oscillatorcharts_chapter08 as oc

NOTE = 'The numbers are ours, made up to show the idea.'


def _paint(letter, painter, targets, caption=NOTE):
    return {'items': (), 'special': 'paint', 'paint': painter, 'owner': 'sh', 'letter': letter,
            'old_marks': (), 'caption': caption, 'group_gap': .18,
            'targets': [{'number': n, 'color': t[0], 'target': t[1], **({'angles': t[2]} if len(t) > 2 else {})}
                        for n, t in enumerate(targets, 1)]}


DATA = {
    'k': _paint('A', oc.paint_raw_k,
                (('gold', (0, 1, 'hi')), ('red', (0, 2, 'lo')), ('blue', (0, 3, 'close')))),
    'eq': _paint('B', oc.paint_equilibrium_crossing,
                 (('gold', (0, 1, 'cross')), ('red', (0, 2, 'cross')), ('blue', (0, 3, 'cross')), ('purple', (0, 4, 'cross'))),
                 'A bounded and an unbounded oscillator. The numbers are ours, made up to show the idea.'),
    'sg': _paint('C', oc.paint_signal_crossing,
                 (('gold', (0, 1, 'cross'), (270, 250, 290)), ('red', (0, 2, 'cross'), (110, 130, 150, 90))),
                 'Signal line: the average of the last three readings. The numbers are ours, made up to show the idea.'),
}

from chartlayout_chapter08 import artwork  # noqa: E402
CHARTS = artwork(DATA)
