"""Chapter-local regression checks; run with unittest from the repo root."""
import dataclasses
import hashlib
import json
from pathlib import Path
import unittest

from charts_chapter07 import DATA
from chartlayout_chapter07 import CAPTION, PAGE_TITLES, CourseChart, _refs, layout, page_specs
from content_chapter07 import CHAPTER
import deckkit
import chartkit


class ChartLayoutTests(unittest.TestCase):
    def test_owner_prices_and_volume_are_immutable(self):
        expected = json.loads((Path(__file__).parents[1] / 'chapter-07' /
                               'chart-owner-fingerprints.json').read_text())
        for key, spec in DATA.items():
            values = [[dict(bars=[dataclasses.astuple(b) for b in p.bars],
                            line=p.line, columns=p.columns)
                       for p in cell.panes] for cell in spec['items']]
            actual = hashlib.sha256(json.dumps(values, sort_keys=True).encode()).hexdigest()
            self.assertEqual(actual, expected['prices_and_volume_sha256'][key], key)

    def test_every_label_and_mark_passes_the_shared_assertion(self):
        for key, spec in DATA.items():
            seen = set()
            for page in range(len(page_specs(spec))):
                fig, marks = layout(key, page)
                texts = [text.get_text() for text in fig.texts]
                self.assertEqual(texts.count(CAPTION), 1, key)
                self.assertTrue(all('Ours, invented' not in text for text in texts))
                self.assertTrue(all(mark.size >= .24 for mark in marks))
                seen.update(mark.number for mark in marks)
            self.assertEqual(seen, {m.number for m in spec['old_marks']}, key)

    def test_all_ohlc_values_have_one_line_labels_on_their_page(self):
        for key, spec in DATA.items():
            if spec['special']:
                continue
            for page, (cell, start, end) in enumerate(page_specs(spec)):
                fig, _marks = layout(key, page)
                labels = [text.get_text() for text in fig.texts]
                for pane in spec['items'][cell].panes:
                    for bar in pane.bars[start:end]:
                        for prefix, value in zip('OHLC', dataclasses.astuple(bar)):
                            self.assertIn(f'{prefix} {value:.2f}', labels)

    def test_open_and_close_labels_stay_on_their_real_price_ticks(self):
        for key, spec in DATA.items():
            if spec['special']:
                continue
            for page, (cell, start, end) in enumerate(page_specs(spec)):
                fig, _marks = layout(key, page)
                for pane in spec['items'][cell].panes:
                    for index, bar in enumerate(pane.bars[start:end], start):
                        for prefix, name, value in (('O', 'open', bar.open), ('C', 'close', bar.close)):
                            tick_x, tick_y = fig.chart_targets[cell, index, name]
                            candidates = [t for t in fig.texts if t.get_text() == f'{prefix} {value:.2f}']
                            same_y = [t for t in candidates if abs(t.get_position()[1]*fig.bbox.height-tick_y)<.01]
                            self.assertTrue(same_y, (key, index, name))
                            self.assertTrue(any((t.get_position()[0]*fig.bbox.width<tick_x if prefix=='O' else t.get_position()[0]*fig.bbox.width>tick_x) for t in same_y))

    def test_full_deck_and_unique_asset_pages_validate(self):
        self.assertEqual(deckkit._validate(CHAPTER), [])
        pages = [s.filename for section in CHAPTER.sections
                 for s in section.slides if isinstance(s, CourseChart)]
        self.assertEqual(len(set(pages)), sum(len(page_specs(spec)) for spec in DATA.values()))

    def test_every_sentence_is_read_beside_its_marks(self):
        charts = [s for section in CHAPTER.sections for s in section.slides
                  if isinstance(s, CourseChart)]
        for slide in charts:
            numbers = {mark.number for mark in slide.marks}
            for sentence in slide.teaching:
                self.assertLessEqual(_refs(sentence), numbers, (slide.asset, sentence))
        titles = [s.title for s in charts if s.asset == 'r3a-a']
        self.assertEqual(titles, list(PAGE_TITLES['r3a-a']))

    def test_look_alike_slides_come_after_both_bars_and_before_their_check(self):
        slides = [s for section in CHAPTER.sections for s in section.slides]
        at = [i for i, s in enumerate(slides) if getattr(s, 'asset', '') == 'r3a-a']
        self.assertEqual(at, [at[0], at[0] + 1])
        after = slides[at[-1] + 1]
        self.assertIsInstance(after, deckkit.Check)
        self.assertEqual(after.label, 'From exhaustion and pin bars')
        taught = [i for i, s in enumerate(slides) if getattr(s, 'asset', '') in ('r3b-lc', 'r3b-lj')]
        self.assertLess(max(taught), at[0])
        for slide in slides[at[0]:at[-1] + 1]:
            self.assertEqual(sorted(m.number for m in slide.marks), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
