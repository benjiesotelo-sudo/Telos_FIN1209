"""Chapter 7 teaching chart data.

Chart A is the invented comparison used in the approved sample: an
exhaustion bar opens beyond the previous high and has no following gap; a pin
bar penetrates support and closes back above it. The book does not provide one
side-by-side figure for review question 1, so the comparison is ours and is
labelled as such on the chart.
"""

from __future__ import annotations

import chartkit as ck


def _bars(values):
    return tuple(ck.Bar(open=o, high=h, low=l, close=c)
                 for o, h, l, c in values)


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
                                height=1.6),
                        ck.Pane(columns=(1.8, 4.8, 2.1), height=0.55),
                    ),
                ),
                ck.Cell(
                    name="Pin bar",
                    note="penetrates support; closes back above it",
                    panes=(
                        ck.Pane(bars=_bars(((41.0, 42.0, 40.2, 41.5),
                                            (41.5, 42.0, 38.8, 40.6),
                                            (40.6, 42.2, 40.0, 41.8))),
                                height=1.6),
                        ck.Pane(columns=(1.6, 0.8, 1.5), height=0.55),
                    ),
                ),
            ),
            cols=2,
            size=ck.pair_size(5.1),
            footnote=("Ours, invented PHP bars and million-share volume. "
                      "The comparison follows Lim pp. 226 to 227."),
        ),
    ),
)
