"""Chapter 9's own charts, as plain data for the shared measured layout.

The letters restart at A in this chapter and the output folder is build/generated/charts-09.
Every chart is a plain-data spec in specs_chapter09, drawn by oscillatorcharts_chapter08.paint_spec,
the data-driven painter Chapter 8 wrote (it knows nothing about any chapter). Chart keys, letters and
asset names must all be unique across the whole chapter: a key used twice would have the later chart
overwrite the earlier picture (Chapter 8's MACD did exactly that), so the build refuses a duplicate.
"""
import oscillatorcharts_chapter08 as oc
from specs_chapter09 import SPECS

NOTE = 'The numbers are ours, made up to show the idea.'
_COLORS = ('gold', 'red', 'blue', 'purple')


def _paint(letter, painter, targets, caption=NOTE):
    return {'items': (), 'special': 'paint', 'paint': painter, 'owner': 'sh', 'letter': letter,
            'old_marks': (), 'caption': caption, 'group_gap': .18, 'marks_by_sentence': True,
            'targets': [{'number': n, 'color': t[0], 'target': t[1], **({'angles': t[2]} if len(t) > 2 else {})}
                        for n, t in enumerate(targets, 1)]}


def _spec(letter, spec, caption=NOTE, angles=None):
    """One chart from a plain-data spec; its marks are the spec's 'marks', in order."""
    targets = []
    for n, m in enumerate(spec['marks'], 1):
        kind = 'group' if m[0] == 'box' else 'pt'
        item = (_COLORS[(n - 1) % 4], (0, n, kind))
        if angles and n in angles:
            item = item + (angles[n],)
        targets.append(item)
    return _paint(letter, lambda c: oc.paint_spec(c, spec), targets, caption)


DATA = {}
_letters = [e['letter'] for e in SPECS.values()]
assert len(_letters) == len(set(_letters)), 'a chart letter is used twice'
for _key, _entry in SPECS.items():
    DATA[_key] = _spec(_entry['letter'], _entry['spec'], _entry.get('caption', NOTE), _entry.get('angles'))

from chartlayout_chapter09 import artwork  # noqa: E402
CHARTS = artwork(DATA)
