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
        letter="P",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                ck.Pane(
                    name="One five-minute bar",
                    bars=(ck.Bar(open=50.00, high=52.40, low=49.60,
                                 close=51.10),),
                    notes=(
                                ck.Note(x=0, y=50.00, label="O 50.00", dx=-24, dy=18),
                                ck.Note(x=0, y=52.40, label="H 52.40", dx=32, dy=12,
                                notice=True),
                                ck.Note(x=0, y=49.60, label="L 49.60", dx=28, dy=-10),
                        ck.Note(x=0, y=51.10, label="C 51.10", dx=10, dy=-8),
                    ),
                    ticks=(49.60, 51.10, 52.40),
                    height=2.0,
                ),
            ),
            size=ck.pair_size(4.8),
            xticks=((0, "one interval"),),
            footnote=("Ours, invented PHP values. Range: |H - L| = "
                      "|52.40 - 49.60| = PHP 2.80."),
        ),
    ),
    ck.ChartArt(
        letter="Q",
        draw=ck.readings,
        kwargs=dict(
            series=(50.00, 50.80, 49.60, 52.40, 51.10),
            marks=(
                ck.Reading(x=0, label="1 first trade 50.00", dx=-8, dy=18),
                ck.Reading(x=3, label="2 highest 52.40", dx=42, dy=18),
                ck.Reading(x=4, label="3 last trade 51.10", dx=10, dy=-14),
            ),
            xlabel="Five one-minute observations inside one five-minute bar",
            footnote=("Ours, invented PHP observations. First trade becomes O; "
                      "highest and lowest become H and L; last becomes C."),
        ),
    ),
    ck.ChartArt(
        letter="R",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                ck.Pane(
                    name="Three lower-timeframe bars",
                    bars=(
                        ck.Bar(open=50.00, high=50.70, low=49.40,
                               close=50.20),
                        ck.Bar(open=50.20, high=50.90, low=49.80,
                               close=50.00),
                        ck.Bar(open=50.00, high=50.60, low=49.70,
                               close=50.30),
                    ),
                    notes=(
                        ck.Note(x=0, y=50.00, label="1 first O", dx=-8, dy=18),
                        ck.Note(x=1, y=50.90, label="2 highest H", dx=28, dy=18,
                                notice=True),
                        ck.Note(x=1, y=49.40, label="3 lowest L", dx=10, dy=-12),
                        ck.Note(x=2, y=50.30, label="4 last C", dx=10, dy=-12),
                    ),
                    ticks=(49.40, 50.30, 50.90),
                    height=2.0,
                ),
            ),
            size=ck.pair_size(4.8),
            xticks=((0, "bar 1"), (1, "bar 2"), (2, "bar 3")),
            footnote=("Ours, invented PHP bars. The composite keeps first O "
                      "50.00, highest H 50.90, lowest L 49.40, last C 50.30."),
        ),
    ),
    ck.ChartArt(
        letter="S",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="1  continuation",
                    note="uptrend +4.0%; bullish +2.0%",
                    tone="notice",
                    panes=(ck.Pane(columns=(4.0, 2.0), height=1.0,
                                   tags=((0, "+4.0% trend"), (1, "+2.0% form"))),),
                ),
                ck.Cell(
                    name="2  continuation",
                    note="downtrend -4.0%; bearish -2.0%",
                    tone="notice",
                    panes=(ck.Pane(columns=(4.0, 2.0), height=1.0,
                                   tags=((0, "-4.0% trend"), (1, "-2.0% form"))),),
                ),
                ck.Cell(
                    name="3  potential reversal",
                    note="uptrend +4.0%; bearish -2.0%",
                    panes=(ck.Pane(columns=(4.0, -2.0), height=1.0,
                                   tags=((0, "+4.0% trend"), (1, "-2.0% form"))),),
                ),
                ck.Cell(
                    name="4  potential reversal",
                    note="downtrend -4.0%; bullish +2.0%",
                    panes=(ck.Pane(columns=(-4.0, 2.0), height=1.0,
                                   tags=((0, "-4.0% trend"), (1, "+2.0% form"))),),
                ),
            ),
            cols=2,
            size=ck.pair_size(3.6),
            footnote=("Ours, invented percentage changes. Trend is the existing "
                      "direction; form is intrinsic sentiment. Lim, p. 211."),
        ),
    ),
    ck.ChartArt(
        letter="T",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="1  continuation",
                    note="uptrend +4.0%; bullish +2.0%",
                    tone="notice",
                    panes=(ck.Pane(columns=(4.0, 2.0), height=1.0,
                                   tags=((0, "+4.0% trend"), (1, "+2.0% form"))),),
                ),
                ck.Cell(
                    name="2  continuation",
                    note="downtrend -4.0%; bearish -2.0%",
                    tone="notice",
                    panes=(ck.Pane(columns=(4.0, 2.0), height=1.0,
                                   tags=((0, "-4.0% trend"), (1, "-2.0% form"))),),
                ),
                ck.Cell(
                    name="3  potential reversal",
                    note="uptrend +4.0%; bearish -2.0%",
                    panes=(ck.Pane(columns=(4.0, -2.0), height=1.0,
                                   tags=((0, "+4.0% trend"), (1, "-2.0% form"))),),
                ),
                ck.Cell(
                    name="4  potential reversal",
                    note="downtrend -4.0%; bullish +2.0%",
                    panes=(ck.Pane(columns=(-4.0, 2.0), height=1.0,
                                   tags=((0, "-4.0% trend"), (1, "+2.0% form"))),),
                ),
            ),
            cols=2,
            size=ck.pair_size(3.6),
            footnote=("Ours, invented percentage changes. Agreement means "
                      "continuation; disagreement means potential reversal. Lim, p. 211."),
        ),
    ),
)
