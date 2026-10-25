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
from matplotlib.transforms import Bbox


def _bars(values):
    return tuple(ck.Bar(open=o, high=h, low=l, close=c)
                 for o, h, l, c in values)


def _bar_notes(*items):
    return tuple(ck.Note(x=x, y=y, label=label, dx=dx, dy=dy,
                         notice=notice)
                 for x, y, label, dx, dy, notice in items)


def _assert_layout(fig, labels, bars, overlays):
    """Fail if rendered labels, bars, rings or badges collide."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    text_boxes = []
    seen = set()
    for artist, target in labels:
        if id(artist) in seen or not artist.get_visible():
            continue
        seen.add(id(artist))
        box = artist.get_window_extent(renderer)
        if box.width and box.height:
            text_boxes.append((artist.get_text(), box, target))
    for artist in (text for axis in fig.axes for text in axis.texts):
        if id(artist) in seen or not artist.get_visible():
            continue
        box = artist.get_window_extent(renderer)
        if box.width and box.height:
            text_boxes.append((artist.get_text(), box, None))

    def overlaps(left, right):
        return (left.x0 < right.x1 and right.x0 < left.x1 and
                left.y0 < right.y1 and right.y0 < left.y1)

    failures = []
    for i, (name, box, _target) in enumerate(text_boxes):
        for other_name, other_box, _other_target in text_boxes[i + 1:]:
            if overlaps(box, other_box):
                failures.append(f"text boxes overlap: {name!r} / {other_name!r}")

    bar_segments = []
    for axis, index, bar in bars:
        trans = axis.transData
        points = tuple(trans.transform(point) for point in (
            (index, bar.low), (index, bar.high),
            (index - 0.30, bar.open), (index, bar.open),
            (index, bar.close), (index + 0.30, bar.close),
        ))
        segments = (
            (points[0], points[1]),
            (points[2], points[3]),
            (points[4], points[5]),
        )
        for start, end in segments:
            bar_segments.append((axis, index, Bbox.from_extents(
                min(start[0], end[0]) - 2,
                min(start[1], end[1]) - 2,
                max(start[0], end[0]) + 2,
                max(start[1], end[1]) + 2)))
    for name, box, target in text_boxes:
        if target is not None and target[0] == "stroke":
            continue
        for axis, index, bar_box in bar_segments:
            if target is not None and target[0] is axis and target[1] == index:
                continue
            if target is not None and target[0] is not axis:
                continue
            if overlaps(box, bar_box):
                failures.append(f"label box overlaps bar {index}: {name!r}")

    for i, (name, box) in enumerate(overlays):
        for other_name, other_box in overlays[i + 1:]:
            if overlaps(box, other_box):
                failures.append(f"overlay boxes overlap: {name!r} / {other_name!r}")
    if failures:
        raise AssertionError("Chart A layout validation failed: " + "; ".join(failures))


def _readable_cells(path: Path, items, *, cols, size, footnote="",
                    display_font=None, title_pt=14.5, note_pt=13.0,
                    label_pt=13.5, footnote_pt=12.5, tag_offset=10,
                    tag_dx=0, validate_layout=False) -> Path:
    """Draw the Chapter 7 cells with projection-sized labels.

    The shared cell form is intentionally compact for ordinary chart bands.
    These five worked charts are projected on their own slides, so their
    values, callouts and pane labels need the larger teaching size here.
    """
    plt.close("all")
    fig = plt.figure(figsize=size, dpi=ck.DPI)
    w_in, h_in = size
    rows = -(-len(items) // cols)
    foot_lines = footnote.count("\n") + 1 if footnote else 0
    foot = 0.08 + 0.16 * foot_lines
    pad = 0.08
    cell_w = (w_in - pad) / cols
    cell_h = (h_in - foot - pad) / rows
    tones = {"structure": ck.GREEN, "notice": ck.GOLD, "quiet": ck.MUTED}
    labels = []
    bars = []

    for i, cell in enumerate(items):
        row, col = divmod(i, cols)
        x = pad + col * cell_w
        top = h_in - pad - row * cell_h
        name_lines = cell.name.count("\n") + 1 if cell.name else 0
        note_lines = cell.note.count("\n") + 1 if cell.note else 0
        label_h = 0.17 * name_lines + 0.14 * note_lines + 0.06
        frame = fig.add_axes([x / w_in, (top - cell_h + pad) / h_in,
                              (cell_w - pad) / w_in,
                              (cell_h - pad) / h_in])
        frame.set_xticks([])
        frame.set_yticks([])
        for side in ("top", "right", "left", "bottom"):
            frame.spines[side].set_color(ck.BORDER)
            frame.spines[side].set_linewidth(0.9)
        frame.set_facecolor(ck.WHITE)
        frame.set_zorder(0)
        if cell.name:
            fig.text(
                (x + (cell_w - pad) / 2) / w_in, (top - 0.05) / h_in,
                cell.name, ha="center", va="top", fontsize=title_pt,
                color=ck.GOLD if cell.tone == "notice" else ck.GREEN_DEEP,
                fontweight="bold", linespacing=1.05)
        if cell.note:
            fig.text(
                (x + (cell_w - pad) / 2) / w_in,
                (top - 0.07 - 0.17 * name_lines) / h_in,
                cell.note, ha="center", va="top", fontsize=note_pt,
                color=ck.MUTED, style="italic", linespacing=1.05)

        n = max(len(p.bars) or len(p.line) or len(p.columns) or 1
                for p in cell.panes)
        inner_top = top - label_h - 0.05
        inner_h = inner_top - (top - cell_h + pad) - 0.06
        total = sum(p.height for p in cell.panes)
        gap = 0.05
        avail = inner_h - gap * (len(cell.panes) - 1)
        y = inner_top
        for pane in cell.panes:
            pane_h = avail * pane.height / total
            y -= pane_h
            ax = fig.add_axes([(x + 0.10) / w_in, y / h_in,
                               (cell_w - pad - 0.20) / w_in,
                               pane_h / h_in])
            ax.set_axis_off()
            xs = [pt[0] for stroke in pane.strokes for pt in stroke.points]
            x_hi = max([n - 0.5] + xs) + 0.5
            x_lo = min([-0.5] + xs) - 0.5
            reach = [v for bar in pane.bars for v in (bar.low, bar.high)]
            reach += list(pane.line)
            reach += [v for v in pane.columns]
            reach += [pt[1] for stroke in pane.strokes for pt in stroke.points]
            lo, hi = min(reach), max(reach)
            span = (hi - lo) or 1.0
            if pane.columns and not (pane.bars or pane.line) and lo >= 0:
                ax.set_ylim(0, hi + span * pane.top)
            else:
                ax.set_ylim(lo - span * pane.bottom,
                            hi + span * pane.top)
            ax.set_xlim(x_lo, x_hi)

            for stroke in pane.strokes:
                color = tones[stroke.tone]
                ax.plot([p[0] for p in stroke.points],
                        [p[1] for p in stroke.points], color=color,
                        lw=stroke.width, ls=(0, (5, 4)) if stroke.dashed else "-",
                        zorder=4, solid_capstyle="round")
                if stroke.label:
                    point = stroke.points[stroke.at]
                    artist = ax.annotate(
                        stroke.label, xy=point,
                        xytext=(stroke.dx, stroke.dy),
                        textcoords="offset points",
                        ha="right" if stroke.dx < 0 else
                        ("left" if stroke.dx > 0 else "center"),
                        va="center", fontsize=label_pt,
                        color=ck.GREEN_DEEP if stroke.tone == "structure"
                        else (ck.GOLD if stroke.tone == "notice" else ck.MUTED),
                        fontweight="bold", zorder=7,
                        bbox=dict(boxstyle="square,pad=0.12",
                                  facecolor=ck.WHITE, edgecolor="none"))
                    labels.append((artist, ("stroke", ax)))

            if pane.columns:
                colors = [ck.GOLD if j in pane.picks else
                          (ck.BORDER if j in pane.dims else ck.GREEN)
                          for j in range(len(pane.columns))]
                ax.bar(range(len(pane.columns)), pane.columns, width=0.62,
                       color=colors, zorder=3, linewidth=0)
            if pane.bars:
                bars.extend((ax, j, bar) for j, bar in enumerate(pane.bars))
                for j, bar in enumerate(pane.bars):
                    ax.plot([j, j], [bar.low, bar.high], color=ck.INK,
                            lw=2.4, zorder=3, solid_capstyle="butt")
                    ax.plot([j - 0.30, j], [bar.open, bar.open], color=ck.INK,
                            lw=2.4, zorder=3, solid_capstyle="butt")
                    ax.plot([j, j + 0.30], [bar.close, bar.close], color=ck.INK,
                            lw=2.4, zorder=3, solid_capstyle="butt")

            def value_at(index):
                if pane.bars:
                    return pane.bars[int(index)].close
                if pane.line:
                    return pane.line[int(index)]
                return pane.columns[int(index)]

            for tag in pane.tags:
                index, label = tag[:2]
                tag_dx_value, tag_offset_value = (
                    (tag[2], tag[3]) if len(tag) >= 4
                    else (tag_dx, tag_offset)
                )
                value = value_at(index)
                artist = ax.annotate(
                    label, xy=(index, value),
                    xytext=(tag_dx_value, tag_offset_value),
                    textcoords="offset points", ha="center",
                    va="bottom", fontsize=label_pt,
                    color=ck.GREEN_DEEP, fontweight="bold", zorder=7)
                labels.append((artist, None))
            for note in pane.notes:
                value = value_at(note.x) if note.y is None else note.y
                if note.dot:
                    ax.scatter([note.x], [value], s=34,
                               color=ck.GOLD if note.notice else ck.GREEN,
                               edgecolors=ck.INK, linewidths=0.5, zorder=6)
                if note.label:
                    artist = ax.annotate(
                        note.label, xy=(note.x, value),
                        xytext=(note.dx, note.dy),
                        textcoords="offset points",
                        ha="center" if note.dx == 0 else
                        ("right" if note.dx < 0 else "left"),
                        va="center", fontsize=label_pt,
                        color=ck.GREEN_DEEP if note.notice else ck.INK,
                        fontweight="bold", zorder=7,
                        bbox=dict(boxstyle="square,pad=0.12",
                                  facecolor=ck.WHITE,
                                  edgecolor=ck.BORDER))
                    labels.append((artist, (ax, int(note.x))))
            y -= gap

    if footnote:
        fig.text(0.008, 0.012, footnote, fontsize=footnote_pt, color=ck.MUTED,
                 style="italic", ha="left", va="bottom", linespacing=1.1)
    if validate_layout:
        width, height = fig.bbox.width, fig.bbox.height

        def norm_box(x0, y0, x1, y1):
            return Bbox.from_extents(x0 * width, (1 - y1) * height,
                                     x1 * width, (1 - y0) * height)

        overlays = []
        rings = (
            ("ring 1", 0.245, 0.225, 0.265, 0.265),
            ("ring 2", 0.245, 0.170, 0.265, 0.210),
            ("ring 3", 0.360, 0.480, 0.390, 0.540),
            ("ring 5", 0.735, 0.820, 0.770, 0.910),
            ("ring 6", 0.735, 0.370, 0.770, 0.430),
        )
        badges = (
            ("badge 1", 0.290, 0.240), ("badge 2", 0.225, 0.140),
            ("badge 3", 0.430, 0.510), ("badge 4", 0.900, 0.500),
            ("badge 5", 0.810, 0.860), ("badge 6", 0.700, 0.430),
        )
        overlays.extend((name, norm_box(x0, y0, x1, y1))
                        for name, x0, y0, x1, y1 in rings)
        overlays.extend((name, norm_box(x - 0.018, y - 0.028,
                                        x + 0.018, y + 0.028))
                        for name, x, y in badges)
        _assert_layout(fig, labels, bars, overlays)
    fig.savefig(path, dpi=ck.DPI, facecolor=ck.WHITE)
    plt.close(fig)
    return path


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
        ax.text(x + w / 2, y + 0.20 * h, result.replace("\n", " "),
                ha="center", va="center", fontsize=14, fontweight="bold",
                color=tone, linespacing=0.95)

    ax.text((left + split_x) / 2, top + 0.08, "Bullish formation",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=ck.GREEN_DEEP)
    ax.text((split_x + right) / 2, top + 0.08, "Bearish formation",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=ck.GREEN_DEEP)
    ax.text(0.13, (split_y + top) / 2, "Uptrend\n(bullish trend)",
            ha="center", va="center", fontsize=12.5, fontweight="bold",
            color=ck.GREEN_DEEP, linespacing=1.0)
    ax.text(0.13, (bottom + split_y) / 2, "Downtrend\n(bearish trend)",
            ha="center", va="center", fontsize=12.5, fontweight="bold",
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
        draw=_readable_cells,
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
                                    (1, 65.4, "O 65.40", -38, 28, True),
                                    (1, 66.2, "H 66.20", 28, 18, False),
                                    (1, 60.0, "L 60.00", -30, -16, False),
                                    (1, 60.5, "C 60.50", 28, -30, False),
                                    (2, 60.2, "next O\n60.20", -8, -2, True))),
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
                                    dx=52, dy=-14),),
                                notes=_bar_notes(
                                    (1, 38.8, "low 38.80", 4, 0, True),
                                    (1, 40.6, "close 40.60", 5, -50, False),
                                    (1, 42.0, "pin bar", 0, -24, True))),
                        ck.Pane(columns=(1.6, 0.8, 1.5), height=0.55,
                                tags=((0, "1.6m"), (1, "0.8m"),
                                      (2, "1.5m", 24, 28))),
                    ),
                ),
            ),
            cols=2,
            size=ck.pair_size(2.8),
            title_pt=13.5,
            note_pt=11.5,
            label_pt=10.5,
            footnote_pt=11.5,
            tag_offset=10,
            footnote="These prices and volume values are invented for teaching.",
            validate_layout=True,
        ),
    ),
    ck.ChartArt(
        letter="B",
        draw=_readable_cells,
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
            footnote="These prices and volume values are invented for teaching.",
        ),
    ),
    ck.ChartArt(
        letter="TA",
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
        letter="TB",
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
    ck.ChartArt(
        letter="V",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Bullish Oops: two-bar worked example",
                    note="invented PHP values; buy-stop then stoploss",
                    panes=(
                        ck.Pane(
                            bars=_bars(((49.0, 50.0, 48.0, 49.5),
                                       (47.0, 49.0, 46.0, 48.5))),
                            height=1.75,
                            strokes=(
                                ck.Stroke(points=((0, 48.0), (1, 48.0)),
                                          tone="structure", dashed=True,
                                          label="buy-stop 48.00", at=0,
                                          dx=-24, dy=8),
                                ck.Stroke(points=((0, 46.0), (1, 46.0)),
                                          tone="notice", dashed=True,
                                          label="stoploss 46.00", at=1,
                                          dx=20, dy=10),
                            ),
                            notes=_bar_notes(
                                (1, 47.0, "open 47.00", -24, 14, True),
                                (1, 46.0, "low 46.00", 20, 8, True),
                                (0, 48.0, "prior low 48.00", -24, 8, True),
                            ),
                        ),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP values. The bullish Oops order rule follows Lim (2016), p. 231.",
        ),
    ),
    ck.ChartArt(
        letter="W",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Inside Month/NR5: worked example",
                    note="invented monthly ranges; upward breakout after the count",
                    panes=(
                        ck.Pane(
                            bars=_bars(((28.0, 30.0, 18.0, 26.0),
                                       (26.0, 29.0, 19.0, 27.0),
                                       (27.0, 30.0, 21.0, 28.0),
                                       (28.0, 31.0, 24.0, 29.0),
                                       (29.0, 30.0, 25.0, 28.0),
                                       (28.0, 33.0, 27.0, 32.0))),
                            height=1.75,
                            strokes=(
                                ck.Stroke(points=((3, 31.0), (5.8, 31.0)),
                                          tone="structure", dashed=True,
                                          label="breakout 31.00", at=1,
                                          dx=0, dy=-10),
                            ),
                            notes=_bar_notes(
                                (0, 30.0, "range 12", -20, 8, False),
                                (1, 29.0, "range 10", -12, 10, False),
                                (2, 30.0, "range 9", -12, 8, False),
                                (3, 31.0, "range 7", 12, 8, False),
                                (4, 30.0, "range 5", 14, 8, False),
                                (5, 33.0, "break 31.00", 16, 8, True),
                            ),
                        ),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented monthly PHP ranges. The inside-month extension follows Lim (2016), p. 232.",
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
                        ck.Bar(open=50.00, high=50.70, low=49.40, close=50.20),
                        ck.Bar(open=50.20, high=50.90, low=49.80, close=50.00),
                        ck.Bar(open=50.00, high=50.60, low=49.70, close=50.30),
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
                ck.Cell(name="1  continuation", note="uptrend +4.0%; bullish +2.0%",
                        tone="notice", panes=(ck.Pane(
                            columns=(4.0, 2.0), height=1.0,
                            tags=((0, "+4.0% trend"), (1, "+2.0% form"))),)),
                ck.Cell(name="2  continuation", note="downtrend -4.0%; bearish -2.0%",
                        tone="notice", panes=(ck.Pane(
                            columns=(4.0, 2.0), height=1.0,
                            tags=((0, "-4.0% trend"), (1, "-2.0% form"))),)),
                ck.Cell(name="3  potential reversal", note="uptrend +4.0%; bearish -2.0%",
                        panes=(ck.Pane(
                            columns=(4.0, -2.0), height=1.0,
                            tags=((0, "+4.0% trend"), (1, "-2.0% form"))),)),
                ck.Cell(name="4  potential reversal", note="downtrend -4.0%; bullish +2.0%",
                        panes=(ck.Pane(
                            columns=(-4.0, 2.0), height=1.0,
                            tags=((0, "-4.0% trend"), (1, "+2.0% form"))),)),
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
                                dx=-82, dy=-8, notice=True),
                        ck.Note(x=4, y=49.8, label="second C 49.80",
                                dx=-82, dy=-30, notice=True),
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
    ck.ChartArt(
        letter="RA",
        draw=_readable_cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Two-day bearish reversal",
                    note="first close near high; second near low",
                    panes=(
                        ck.Pane(
                            bars=_bars(((50.0, 52.2, 49.7, 51.8),
                                       (51.7, 52.0, 49.0, 49.6))),
                            height=1.7,
                            notes=_bar_notes(
                                (0, 51.8, "C 51.80", -20, 8, True),
                                (1, 49.6, "C 49.60", 55, -8, True),
                                (0, 52.2, "H 52.20", -18, 10, False),
                                (1, 49.0, "L 49.00", 18, -10, False)),
                        ),
                        ck.Pane(columns=(2.4, 3.1), height=0.55,
                                tags=((0, "2.4m"), (1, "3.1m"))),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            tag_dx=-35,
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
    ck.ChartArt(
        letter="RB",
        draw=_readable_cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Bullish three-bar reversal",
                    note="strong outer bars; quiet middle bar",
                    panes=(
                        ck.Pane(
                            bars=_bars(((42.0, 44.0, 41.0, 43.8),
                                       (43.7, 44.1, 43.2, 43.5),
                                       (43.4, 46.8, 43.0, 46.5))),
                            height=1.7,
                            notes=_bar_notes(
                                (0, 41.0, "L 41.00", -20, -10, False),
                                (0, 44.0, "H 44.00", -20, 8, False),
                                (1, 43.2, "L 43.20", -20, -10, False),
                                (1, 44.1, "H 44.10", 18, 8, False),
                                (1, 43.5, "middle C 43.50", 18, 7, True),
                                (2, 46.5, "C 46.50", 18, -8, True)),
                        ),
                        ck.Pane(columns=(4.0, 0.6, 4.2), height=0.55,
                                tags=((0, "4.0m"), (1, "0.6m"),
                                      (2, "4.2m"))),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            tag_offset=32,
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
    ck.ChartArt(
        letter="RC",
        draw=_readable_cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Bearish island reversal",
                    note="gap up, isolated bars, gap down",
                    panes=(
                        ck.Pane(
                            bars=_bars(((48.0, 50.0, 47.5, 49.5),
                                       (50.8, 52.0, 50.6, 51.5),
                                       (51.4, 52.2, 50.9, 51.1),
                                       (49.4, 50.0, 48.2, 48.8))),
                            height=1.7,
                            strokes=(
                                ck.Stroke(points=((0, 50.0), (3, 50.0)),
                                          tone="quiet", dashed=True,
                                          label="prior high 50.00", at=0,
                                          dx=-24, dy=-10),
                            ),
                            notes=_bar_notes(
                                (1, 50.8, "gap-up O 50.80", -85, 15, True),
                                (2, 51.5, "island", 18, -8, True),
                                (3, 49.4, "gap-down O 49.40", -82, 15, True)),
                        ),
                        ck.Pane(columns=(2.3, 0.7, 0.6, 2.1), height=0.55,
                                tags=((0, "2.3m"), (1, "0.7m"),
                                      (2, "0.6m"), (3, "2.1m"))),
                    ),
                ),
            ),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
)


# The reworked first-half examples use fresh K-series filenames. Their data
# keeps the approved OHLC values, while the new names prevent an old chart
# image from being mistaken for this pass's artwork.
_CHART_BY_LETTER = {art.letter: art for art in CHARTS}
CHARTS = CHARTS + tuple(
    ck.ChartArt(letter=new, draw=_CHART_BY_LETTER[source].draw,
               kwargs=dict(_CHART_BY_LETTER[source].kwargs))
    for new, source in (("K", "B"), ("L", "RA"), ("M", "RB"), ("N", "RC"))
)

# Charts SA to SH belong to the inside-bar through Hikkake range. The letters
# deliberately start at S so parallel Chapter 7 workers can add their own
# charts without colliding with this lane or with the approved A and B.
CHARTS = CHARTS + (
    ck.ChartArt(
        letter="SA",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="Outside bar",
                note="contains two prior bars and closes near its low",
                panes=(
                    ck.Pane(
                        bars=_bars(((49.0, 51.5, 48.0, 51.2),
                                   (50.5, 52.0, 49.5, 51.8),
                                   (52.0, 53.0, 47.0, 47.5))),
                        height=1.8,
                        strokes=(ck.Stroke(points=((0, 52.0), (2, 52.0)),
                                           tone="quiet", dashed=True,
                                           label="prior high 52.00", at=0,
                                           dx=-18, dy=-10),),
                        notes=_bar_notes(
                            (2, 53.0, "H 53.00", 18, 8, True),
                            (2, 47.0, "L 47.00", -18, -10, False),
                            (2, 47.5, "C 47.50", 20, -4, True),
                        ),
                    ),
                    ck.Pane(columns=(1.5, 1.4, 5.0), height=0.55,
                            tags=((0, "1.5m"), (1, "1.4m"), (2, "5.0m"))),
                ),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
    ck.ChartArt(
        letter="SB",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="Inside bar",
                note="second bar stays inside the first",
                panes=(
                    ck.Pane(
                        bars=_bars(((50.0, 53.0, 48.0, 52.4),
                                   (51.8, 52.5, 49.2, 50.1))),
                        height=1.8,
                        strokes=(ck.Stroke(points=((0, 53.0), (1, 53.0)),
                                           tone="quiet", dashed=True,
                                           label="resistance 53.00", at=0,
                                           dx=-20, dy=-10),),
                        notes=_bar_notes(
                            (0, 53.0, "H 53.00", -18, 8, True),
                            (1, 52.5, "H 52.50", 18, 8, True),
                            (1, 50.1, "C 50.10", 20, -6, True),
                        ),
                    ),
                    ck.Pane(columns=(4.5, 0.5), height=0.55,
                            tags=((0, "4.5m"), (1, "0.5m"))),
                ),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
    ck.ChartArt(
        letter="SC",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="Emotion spike",
                note="wide range and high volume",
                panes=(
                    ck.Pane(
                        bars=_bars(((60.0, 61.5, 58.5, 61.0),
                                   (61.0, 62.5, 59.5, 62.0),
                                   (62.0, 70.0, 62.0, 63.0),
                                   (63.0, 64.0, 61.0, 62.0),
                                   (62.0, 63.0, 59.8, 60.5),
                                   (60.5, 61.0, 57.8, 58.5))),
                        height=1.8,
                        notes=_bar_notes(
                            (2, 70.0, "H 70.00", 18, 8, True),
                            (2, 62.0, "L 62.00", -18, -10, False),
                            (3, 62.0, "C 62.00", 18, -8, True),
                            (4, 60.5, "C 60.50", 18, -8, True),
                            (5, 58.5, "C 58.50", 18, -8, True),
                        ),
                    ),
                    ck.Pane(columns=(1.5, 1.4, 6.0, 2.2, 2.0, 2.4), height=0.55,
                            tags=((0, "1.5m"), (1, "1.4m"), (2, "6.0m"),
                                  (3, "2.2m"), (4, "2.0m"), (5, "2.4m"))),
                ),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP bars and million-share volume.",
        ),
    ),
    ck.ChartArt(
        letter="SD",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="False upside breakout",
                    note="close returns below resistance",
                    panes=(ck.Pane(
                        bars=_bars(((58.0, 60.0, 57.0, 59.0),
                                   (59.0, 62.0, 58.5, 59.4))),
                        height=1.4,
                        strokes=(ck.Stroke(points=((0, 60.0), (1, 60.0)),
                                           tone="quiet", dashed=True,
                                           label="resistance 60.00", at=0,
                                           dx=-18, dy=-10),),
                        notes=_bar_notes((1, 62.0, "H 62.00", 18, 8, True),
                                         (1, 59.4, "C 59.40", 18, -6, True)),
                    ),),
                ),
                ck.Cell(
                    name="False downside breakout",
                    note="close returns above support",
                    panes=(ck.Pane(
                        bars=_bars(((42.0, 43.0, 40.0, 41.0),
                                   (41.0, 41.5, 38.5, 40.6))),
                        height=1.4,
                        strokes=(ck.Stroke(points=((0, 40.0), (1, 40.0)),
                                           tone="quiet", dashed=True,
                                           label="support 40.00", at=0,
                                           dx=-18, dy=-10),),
                        notes=_bar_notes((1, 38.5, "L 38.50", -18, -8, True),
                                         (1, 40.6, "C 40.60", 18, 6, True)),
                    ),),
                ),
            ),
            cols=2,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP barriers and closes.",
        ),
    ),
    ck.ChartArt(
        letter="SE",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="False upside breakout",
                note="the course drawing; return below resistance",
                panes=(ck.Pane(
                    bars=_bars(((58.0, 60.0, 57.0, 59.0),
                               (59.0, 62.0, 58.5, 59.4))),
                    height=1.8,
                    strokes=(ck.Stroke(points=((0, 60.0), (1, 60.0)),
                                       tone="quiet", dashed=True,
                                       label="resistance 60.00", at=0,
                                       dx=-18, dy=-10),
                             ck.Stroke(points=((0, 62.2), (1, 62.2)),
                                       tone="quiet", dashed=True,
                                       label="stop 62.20", at=1,
                                       dx=18, dy=-10)),
                    notes=_bar_notes((1, 62.0, "H 62.00", 18, 8, True),
                                     (1, 59.4, "C 59.40", 18, -6, True)),
                ),),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Course drawing, invented PHP values; the book's drawing follows.",
        ),
    ),
    ck.ChartArt(
        letter="SF",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="Double Repo",
                note="two crossings of a forward-shifted three-day SMA",
                panes=(
                    ck.Pane(
                        bars=_bars(((48.0, 49.5, 47.5, 49.2),
                                   (49.2, 50.2, 48.8, 49.6),
                                   (49.6, 50.8, 49.2, 50.0),
                                   (50.0, 51.2, 49.6, 50.4),
                                   (50.4, 51.5, 50.0, 50.8),
                                   (50.8, 52.0, 50.4, 51.2),
                                   (51.2, 52.2, 50.8, 51.5),
                                   (51.5, 52.4, 51.0, 51.7),
                                   (51.7, 52.6, 51.3, 51.8),
                                   (51.8, 52.0, 50.2, 50.8),
                                   (50.8, 51.0, 49.2, 49.6),
                                   (49.6, 51.0, 49.3, 50.7),
                                   (50.7, 50.9, 48.5, 49.0),
                                   (49.0, 49.5, 46.8, 47.5))),
                        height=1.8,
                        strokes=(ck.Stroke(points=((0, 50.0), (4, 50.0)),
                                           tone="quiet", dashed=True,
                                           label="SMA 50.00", at=0,
                                           dx=12, dy=-10),),
                        notes=_bar_notes((9, 50.8, "1st above 50.80", 18, 8, True),
                                         (10, 49.6, "1st below 49.60", 18, -8, True),
                                         (11, 50.7, "2nd above 50.70", 18, 8, True),
                                         (12, 49.0, "2nd below 49.00", 18, -8, True),
                                         (13, 47.5, "decline", 18, 4, True)),
                    ),
                ),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP closes and a three-day SMA.",
        ),
    ),
    ck.ChartArt(
        letter="SG",
        draw=ck.cells,
        kwargs=dict(
            items=(ck.Cell(
                name="Bearish Hikkake",
                note="inside bar, false high, then short re-entry",
                panes=(ck.Pane(
                    bars=_bars(((50.0, 52.0, 49.0, 51.0),
                               (51.0, 53.0, 50.0, 52.5),
                               (52.5, 52.8, 48.5, 49.0))),
                    height=1.4,
                    strokes=(ck.Stroke(points=((0, 52.0), (2, 52.0)),
                                       tone="quiet", dashed=True,
                                       label="inside high 52.00", at=0,
                                       dx=10, dy=-10),),
                    notes=_bar_notes((0, 52.0, "inside high 52.00", -18, -8, True),
                                     (1, 53.0, "false high 53.00", 18, 8, True),
                                     (2, 49.0, "short below 49.00", 18, -8, True)),
                ),),
            ),),
            cols=1,
            size=ck.pair_size(2.8),
            footnote="Ours, invented PHP levels and entries.",
        ),
    ),
    ck.ChartArt(
        letter="SH",
        draw=ck.cells,
        kwargs=dict(
            items=(
                ck.Cell(
                    name="Bullish Hikkake",
                    note="inside bar, false low, then long re-entry",
                    panes=(ck.Pane(
                        bars=_bars(((41.0, 43.0, 40.0, 42.0),
                                   (41.0, 42.0, 39.0, 40.0),
                                   (40.0, 44.0, 39.8, 43.0))),
                        height=1.5,
                        strokes=(
                            ck.Stroke(points=((0, 43.0), (2, 43.0)),
                                      tone="quiet", dashed=True,
                                      label="inside high 43.00", at=0,
                                      dx=8, dy=-10),
                            ck.Stroke(points=((0, 40.0), (2, 40.0)),
                                      tone="quiet", dashed=True,
                                      label="inside low 40.00", at=0,
                                      dx=8, dy=10),
                        ),
                        notes=_bar_notes((0, 43.0, "inside high", -18, 8, True),
                                         (1, 39.0, "false low", -18, -8, True),
                                         (2, 43.0, "long above", 18, 8, True)),
                    ),),
                ),
                ck.Cell(
                    name="Bearish Hikkake",
                    note="inside bar, false high, then short re-entry",
                    panes=(ck.Pane(
                        bars=_bars(((50.0, 52.0, 49.0, 51.0),
                                   (51.0, 53.0, 50.0, 52.5),
                                   (52.5, 52.8, 48.5, 49.0))),
                        height=1.5,
                        strokes=(
                            ck.Stroke(points=((0, 52.0), (2, 52.0)),
                                      tone="quiet", dashed=True,
                                      label="inside high 52.00", at=0,
                                      dx=8, dy=-10),
                            ck.Stroke(points=((0, 49.0), (2, 49.0)),
                                      tone="quiet", dashed=True,
                                      label="inside low 49.00", at=0,
                                      dx=8, dy=10),
                        ),
                        notes=_bar_notes((0, 52.0, "inside high", -18, 8, True),
                                         (1, 53.0, "false high", 18, 8, True),
                                         (2, 49.0, "short below", 18, -8, True)),
                    ),),
                ),
            ),
            cols=2,
            size=ck.pair_size(2.8),
            footnote="Course drawing, invented PHP values; the book's drawing follows.",
        ),
    ),
)
