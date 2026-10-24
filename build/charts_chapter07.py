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

from pathlib import Path

import chartkit as ck
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def _bars(values):
    return tuple(ck.Bar(open=o, high=h, low=l, close=c)
                 for o, h, l, c in values)


def _bar_notes(*items):
    return tuple(ck.Note(x=x, y=y, label=label, dx=dx, dy=dy,
                         notice=notice)
                 for x, y, label, dx, dy, notice in items)


def _sentiment_table(path: Path, *, size, footnote="", display_font=None) -> Path:
    """Draw the four sentiment cases as a readable trend/form table."""
    plt.close("all")
    fig = plt.figure(figsize=size, dpi=ck.DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    left, right = 0.20, 0.98
    bottom, top = 0.13, 0.80
    split_x = left + (right - left) / 2
    split_y = bottom + (top - bottom) / 2
    cells = (
        (left, split_y, split_x - left, top - split_y,
         "CONTINUATION", "uptrend + bullish formation", ck.GREEN_DEEP),
        (split_x, split_y, right - split_x, top - split_y,
         "POTENTIAL\nREVERSAL", "uptrend + bearish formation", ck.GOLD),
        (left, bottom, split_x - left, split_y - bottom,
         "POTENTIAL\nREVERSAL", "downtrend + bullish formation", ck.GOLD),
        (split_x, bottom, right - split_x, split_y - bottom,
         "CONTINUATION", "downtrend + bearish formation", ck.GREEN_DEEP),
    )
    for x, y, w, h, result, example, tone in cells:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=ck.WHITE,
                               edgecolor=ck.BORDER, linewidth=1.0))
        # A small directional example makes the trend/form relationship
        # visible without relying on percentages or a numerical axis.
        rising = "uptrend" in example
        form_bullish = "bullish formation" in example
        x0, x1 = x + 0.07 * w, x + 0.93 * w
        y0 = y + 0.70 * h
        trend = [y0 - 0.10 * h, y0 + (0.11 if rising else -0.11) * h,
                 y0 - (0.02 if rising else 0.02) * h]
        ax.plot((x0, x + 0.47 * w, x1), trend, color=ck.GREEN_DEEP,
                linewidth=2.2, solid_capstyle="round")
        last_y = trend[-1]
        form_y = last_y + (0.08 if form_bullish else -0.08) * h
        ax.plot((x + 0.57 * w, x + 0.78 * w, x + 0.90 * w),
                (last_y, form_y, form_y),
                color=ck.GREEN_DEEP if form_bullish else ck.GOLD,
                linewidth=2.2, solid_capstyle="round")
        ax.text(x + w / 2, y + 0.23 * h, result, ha="center", va="center",
                fontsize=15, fontweight="bold", color=tone,
                linespacing=0.95)
        ax.text(x + w / 2, y + 0.08 * h, example, ha="center", va="center",
                fontsize=10.5, color=ck.MUTED)

    ax.text((left + split_x) / 2, top + 0.08, "Bullish formation",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=ck.GREEN_DEEP)
    ax.text((split_x + right) / 2, top + 0.08, "Bearish formation",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=ck.GREEN_DEEP)
    ax.text(0.095, (split_y + top) / 2, "Uptrend\n(bullish trend)",
            ha="center", va="center", fontsize=13.5, fontweight="bold",
            color=ck.GREEN_DEEP, linespacing=1.0)
    ax.text(0.095, (bottom + split_y) / 2, "Downtrend\n(bearish trend)",
            ha="center", va="center", fontsize=13.5, fontweight="bold",
            color=ck.GREEN_DEEP, linespacing=1.0)
    if footnote:
        fig.text(0.012, 0.018, footnote, fontsize=8.5, color=ck.MUTED,
                 style="italic", ha="left", va="bottom")
    fig.savefig(path, dpi=ck.DPI, facecolor=ck.WHITE)
    plt.close(fig)
    return path


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
        draw=_sentiment_table,
        kwargs=dict(
            size=ck.pair_size(5.0),
            footnote=("Ours, invented examples. Agreement means continuation; "
                      "disagreement means potential reversal. Lim, p. 211."),
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
    ck.ChartArt(
        letter="U",
        draw=ck.panels,
        kwargs=dict(
            panes=(
                ck.Pane(
                    name="Invented five-bar context and two-bar formation",
                    bars=_bars(((45.0, 46.0, 44.2, 45.6),
                                (45.6, 47.2, 45.0, 46.8),
                                (46.8, 48.5, 46.2, 48.1),
                                (49.7, 51.0, 50.2, 50.5),
                                (50.6, 51.2, 49.4, 49.8))),
                    notes=(
                        ck.Note(x=3, y=50.2, label="first L 50.20",
                                dx=-28, dy=-12, notice=True),
                        ck.Note(x=4, y=49.8, label="second C 49.80",
                                dx=-8, dy=-12, notice=True),
                    ),
                    ticks=(44.0, 46.0, 48.0, 50.0, 52.0),
                    height=1.0,
                ),
            ),
            size=ck.pair_size(5.55),
            xticks=((2, "rising context"), (3, "first"), (4, "second")),
            footnote="Ours, invented PHP bars. The final two bars are the double formation.",
        ),
    ),
)
