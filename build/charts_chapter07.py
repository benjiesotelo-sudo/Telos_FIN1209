"""Chapter 7 teaching chart data.

Chart A is the invented comparison used in the approved sample: an
exhaustion bar opens beyond the previous high and has no following gap; a pin
bar penetrates support and closes back above it. The book does not provide one
side-by-side figure for review question 1, so the comparison is ours and is
labelled as such on the chart.

Chart B is the invented two-bar worked example for the key reversal. It keeps
all five OHLC and volume values on the picture so the numbered reading can be
checked without looking back to the prose.
"""

from __future__ import annotations

import chartkit as ck


def _bars(values):
    return tuple(ck.Bar(open=o, high=h, low=l, close=c)
                 for o, h, l, c in values)


def _bar_notes(*items):
    return tuple(ck.Note(x=x, y=y, label=label, dx=dx, dy=dy,
                         notice=notice)
                 for x, y, label, dx, dy, notice in items)


CHARTS = (
    ck.ChartArt(
        letter="A",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Exhaustion bar",
                    note="opens beyond prior high; no following gap",
                    panes=(
                        ck.Pane(bars=_bars(((62.0, 65.0, 61.0, 64.0),
                                            (65.4, 66.2, 60.0, 60.5),
                                            (60.2, 62.0, 59.8, 61.6))),
                                height=1.6,
                                strokes=(ck.Stroke(
                                    points=((0, 65.0), (2, 65.0)),
                                    tone="quiet", dashed=True,
                                    label="prior high 65.00", at=0,
                                    dx=-34, dy=-10),),
                                notes=_bar_notes(
                                    (1, 65.4, "O 65.40", -14, 16, True),
                                    (1, 66.2, "H 66.20", 18, 8, False),
                                    (1, 60.0, "L 60.00", -18, -10, False),
                                    (1, 60.5, "C 60.50", 20, -2, False),
                                    (2, 60.2, "next O 60.20", 18, 10, True))),
                        ck.Pane(columns=(1.8, 4.8, 2.1), height=0.55,
                                tags=((0, "1.8m"), (1, "4.8m"), (2, "2.1m"))),
                    ),
                ),
                ck.Cell(
                    name="Pin bar",
                    note="penetrates support; closes back above it",
                    panes=(
                        ck.Pane(bars=_bars(((41.0, 42.0, 40.2, 41.5),
                                            (41.5, 42.0, 38.8, 40.6),
                                            (40.6, 42.2, 40.0, 41.8))),
                                height=1.6,
                                strokes=(ck.Stroke(
                                    points=((0, 40.0), (2, 40.0)),
                                    tone="quiet", dashed=True,
                                    label="support 40.00", at=0,
                                    dx=-20, dy=-10),),
                                notes=_bar_notes(
                                    (1, 38.8, "low 38.80", -22, -10, True),
                                    (1, 40.6, "close 40.60", 18, 5, False),
                                    (1, 41.5, "pin bar", 18, 12, True))),
                        ck.Pane(columns=(1.6, 0.8, 1.5), height=0.55,
                                tags=((0, "1.6m"), (1, "0.8m"), (2, "1.5m"))),
                    ),
                ),
            ),
            cols=2,
            size=ck.pair_size(2.8),
            footnote=("Ours, invented PHP bars and million-share volume. "
                      "The comparison follows Lim pp. 226 to 227."),
        ),
    ),
    ck.ChartArt(
        letter="B",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Key reversal: two-bar worked example",
                    note="all values are invented PHP values",
                    panes=(
                        ck.Pane(
                            bars=_bars(((50.80, 52.00, 50.60, 51.10),
                                       (52.30, 53.20, 49.90, 50.80))),
                            height=1.7,
                            strokes=(
                                ck.Stroke(points=((0, 52.00), (1, 52.00)),
                                          tone="quiet", dashed=True,
                                          label="prior high 52.00", at=0,
                                          dx=-24, dy=-10),
                                ck.Stroke(points=((0, 51.10), (1, 51.10)),
                                          tone="quiet", dashed=True,
                                          label="prior close 51.10", at=0,
                                          dx=-25, dy=-10),
                            ),
                            notes=_bar_notes(
                                (1, 52.30, "O 52.30", -18, 16, True),
                                (1, 53.20, "H 53.20", 18, 9, True),
                                (1, 50.80, "C 50.80", 20, -8, True),
                                (0, 50.60, "L 50.60", -18, -8, False),
                            ),
                        ),
                        ck.Pane(columns=(2.0, 4.2), height=0.55,
                                tags=((0, "2.0m"), (1, "4.2m"))),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
)
