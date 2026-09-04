#!/usr/bin/env python3
"""The two charts the Chapter 1 activity's answer key prints.

These are the only pictures in this repository drawn from **real** data. Every
other chart the course draws is invented from a fixed seed, because a
definitional graphic makes no claim about markets that being real would
support (see build/chartkit.py). These two make exactly that claim: they are
what the price actually did after the window the students analysed stopped,
and a reveal drawn from invented numbers would be a lie.

They may be drawn and committed because the series is public domain. See
build/activity_data.py for the licence.

The palette and the fonts come from chartkit, which takes them from deckkit,
so there is one copy of the course's identity and these charts are recognisably
the same course as the deck. The credit line is this module's own, because it
has to say something the deck's charts must never say: that the data is real.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

import activity_data as ad  # noqa: E402
import chartkit  # noqa: E402

# A page is 170mm of measure. At this ratio a chart fills it without the
# caption underneath being pushed off the sheet.
FIG_W = 9.2
FIG_H = 4.6
DPI = 200

CREDIT = ("Drawn for FIN1209 from FRED series DCOILWTICO. Source: U.S. Energy "
          "Information Administration, retrieved through FRED, Federal "
          "Reserve Bank of St. Louis. Public domain. Unlike the nine charts "
          "in the deck, the prices on this one are real.")


def _new():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=DPI)
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_linewidth(0.7)
        ax.spines[side].set_color(chartkit.BORDER)
    ax.tick_params(labelsize=8.5, colors=chartkit.MUTED, length=3, width=0.7)
    ax.grid(True, axis="y", color=chartkit.BORDER, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    return fig, ax


def _save(fig, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout(pad=0.6)
    fig.savefig(path, dpi=DPI, facecolor="#ffffff",
                metadata={"Software": None})
    plt.close(fig)
    return path


def _dates_prices(series: ad.Series):
    return list(series.dates), list(series.closes)


def reveal_full(path: Path) -> Path:
    """The window the students analysed, and the nine months after it."""
    fig, ax = _new()

    wd, wp = _dates_prices(ad.PART_B)
    rd, rp = _dates_prices(ad.REVEAL)

    # The join: the reveal's first day continues the window's last, so the
    # line has no gap in it and nobody can read the break as a data error.
    ax.plot([wd[-1]] + rd, [wp[-1]] + rp, color=chartkit.GOLD, linewidth=1.9,
            solid_capstyle="round", zorder=3)
    ax.plot(wd, wp, color=chartkit.GREEN_DEEP, linewidth=2.1,
            solid_capstyle="round", zorder=4)

    edge = wd[-1]
    ax.axvline(edge, color=chartkit.MUTED, linewidth=0.9, linestyle=(0, (4, 3)),
               zorder=2)

    lo, hi = min(rp), max(wp + rp)
    span = hi - lo
    ax.set_ylim(lo - 0.14 * span, hi + 0.20 * span)

    ax.annotate("Your chart stopped here",
                xy=(edge, wp[-1]), xytext=(-6, 24), textcoords="offset points",
                ha="right", fontsize=9.5, color=chartkit.INK, weight="bold")
    ax.annotate(f"{wp[-1]:.2f}", xy=(edge, wp[-1]), xytext=(-6, 10),
                textcoords="offset points", ha="right", fontsize=9,
                color=chartkit.GREEN_DEEP)

    low = min(zip(rp, rd))
    ax.plot([low[1]], [low[0]], marker="o", markersize=6,
            color=chartkit.GOLD, zorder=5)
    ax.annotate(f"{low[0]:.2f} on {low[1]:%d %b %Y}",
                xy=(low[1], low[0]), xytext=(-8, -18), ha="right",
                textcoords="offset points", fontsize=9,
                color=chartkit.INK, weight="bold")

    ax.set_ylabel("Price, US dollars per barrel", fontsize=9,
                  color=chartkit.MUTED)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    return _save(fig, path)


def reveal_trendline(path: Path) -> Path:
    """Two rising lines under the same troughs, broken ten days apart.

    This is the chapter's Figure 1.20 happening to real prices. Both lines are
    honest readings of the same record and they call the reversal at different
    moments, which is the whole of Part 4 in one picture.
    """
    fig, ax = _new()

    facts = ad.trendline_facts()
    last_break = max(t["broke_on"] for t in facts)
    stop = last_break + dt.timedelta(days=40)

    rd, rp = _dates_prices(ad.REVEAL)
    tail = [(d, p) for d, p in zip(rd, rp) if d <= stop]
    wd, wp = _dates_prices(ad.PART_B)

    ax.plot([wd[-1]] + [d for d, _ in tail], [wp[-1]] + [p for _, p in tail],
            color=chartkit.GOLD, linewidth=1.9, zorder=3)
    ax.plot(wd, wp, color=chartkit.GREEN_DEEP, linewidth=2.1, zorder=4)

    line_end = tail[-1][0]
    for t, dash, offset in zip(facts, ((0, (7, 3)), (0, (2, 2.5))),
                               ((10, -26), (10, 16))):
        anchor = (t["first"], t["first_price"], t["second"], t["second_price"])
        ax.plot([t["first"], line_end],
                [t["first_price"], ad.line_value(anchor, line_end)],
                color=chartkit.GREEN, linewidth=1.3, linestyle=dash, zorder=5)
        for when, price in ((t["first"], t["first_price"]),
                            (t["second"], t["second_price"])):
            ax.plot([when], [price], marker="o", markersize=5.5,
                    markerfacecolor="#ffffff", markeredgewidth=1.5,
                    markeredgecolor=chartkit.GREEN, zorder=6)
        ax.plot([t["broke_on"]], [t["broke_at"]], marker="o", markersize=7,
                color=chartkit.GOLD, zorder=7)
        ax.annotate(f"line {t['name']} broken {t['broke_on']:%d %b}",
                    xy=(t["broke_on"], t["broke_at"]), xytext=offset,
                    textcoords="offset points", fontsize=9, weight="bold",
                    color=chartkit.INK,
                    arrowprops=dict(arrowstyle="-", color=chartkit.MUTED,
                                    linewidth=0.8))

    ax.axvline(wd[-1], color=chartkit.MUTED, linewidth=0.9,
               linestyle=(0, (4, 3)), zorder=2)
    ax.annotate("window ends", xy=(wd[-1], 0.02), xytext=(-5, 0),
                textcoords="offset points", ha="right", fontsize=8.5,
                color=chartkit.MUTED, xycoords=("data", "axes fraction"))

    ax.set_ylabel("Price, US dollars per barrel", fontsize=9,
                  color=chartkit.MUTED)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    return _save(fig, path)


CHARTS = {
    "reveal-full": reveal_full,
    "reveal-trendline": reveal_trendline,
}


def generate(out_dir: Path) -> dict[str, Path]:
    """Draw both charts. Every build redraws them, the way the deck's are."""
    return {name: fn(out_dir / f"{name}.png") for name, fn in CHARTS.items()}


if __name__ == "__main__":                                # pragma: no cover
    import sys
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/charts")
    for name, path in generate(target).items():
        print(f"{name}: {path}")
