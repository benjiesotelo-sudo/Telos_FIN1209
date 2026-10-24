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
                                    dx=8, dy=-10),),
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
    ck.ChartArt(
        letter="T",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Gap up Oops",
                    note="invented PHP values; sell-stop then stoploss",
                    panes=(
                        ck.Pane(
                            bars=_bars(((50.0, 52.0, 49.5, 51.0),
                                       (53.0, 54.0, 50.5, 51.5))),
                            height=1.75,
                            strokes=(
                                ck.Stroke(points=((0, 52.0), (1, 52.0)),
                                          tone="structure", dashed=True,
                                          label="prior high 52.00", at=0,
                                          dx=-24, dy=-10),
                                ck.Stroke(points=((0, 54.0), (1, 54.0)),
                                          tone="notice", dashed=True,
                                          label="stoploss 54.00", at=1,
                                          dx=20, dy=-10),
                            ),
                            notes=_bar_notes(
                                (1, 53.0, "open 53.00", -24, 14, True),
                                (1, 54.0, "high 54.00", 20, 8, True),
                                (0, 52.0, "sell-stop 52.00", -24, 8, True),
                            ),
                        ),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP values. The order rule follows Lim (2016), p. 231.",
        ),
    ),
    ck.ChartArt(
        letter="U",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="ID/NR6",
                    note="last bar is inside and narrowest; either trigger is possible",
                    panes=(
                        ck.Pane(
                            bars=_bars(((50.0, 54.0, 49.0, 52.0),
                                       (52.0, 55.2, 50.0, 53.5),
                                       (53.5, 56.3, 51.2, 54.0),
                                       (54.0, 56.1, 52.2, 55.0),
                                       (55.0, 56.6, 54.4, 55.8),
                                       (55.7, 56.5, 55.3, 56.1))),
                            height=1.75,
                            strokes=(
                                ck.Stroke(points=((4.5, 56.6), (5.8, 56.6)),
                                          tone="notice", dashed=True, arrow=True,
                                          label="long trigger 56.60", at=1,
                                          dx=0, dy=-10),
                                ck.Stroke(points=((4.5, 54.4), (5.8, 54.4)),
                                          tone="notice", dashed=True, arrow=True,
                                          label="short trigger 54.40", at=1,
                                          dx=0, dy=10),
                            ),
                            notes=_bar_notes(
                                (0, 54.0, "range 4.0", -20, 10, False),
                                (1, 55.2, "range 3.2", -12, 12, False),
                                (2, 56.3, "range 2.8", -12, 10, False),
                                (3, 56.1, "range 2.1", -12, 10, False),
                                (4, 56.6, "range 1.6", 14, 8, False),
                                (5, 56.5, "range 1.2", 14, 8, True),
                            ),
                        ),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP ranges. The ID/NR6 rule follows Lim (2016), p. 232.",
        ),
    ),
)
