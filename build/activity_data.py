#!/usr/bin/env python3
"""The price series the Chapter 1 activity is built on, and every answer.

The worksheet, the answer key and the reveal chart all read their numbers from
here, so a student's expected answer, the marker's key and the picture cannot
disagree. Nothing in this module is typed by hand: every figure is computed
from the committed CSV files in chapter-01/activity/data/.

**Where the data came from, and why it may be committed.** Both series are
distributed by FRED, the Federal Reserve Bank of St. Louis, and both are
sourced from the U.S. Energy Information Administration. FRED tags them
"public domain: citation requested" and declares the licence at
https://fred.stlouisfed.org/legal/#copyright-public-domain, so unlike the
textbook figures they may live in a public repository. See
chapter-01/activity/README.md for how they were retrieved and cleaned.

Closing prices are all these series carry. There is no open, no high, no low
and no volume, so every identification question the activity asks is a
question a column of closes can actually answer. Nothing is invented to fill
a gap.
"""

from __future__ import annotations

import csv
import datetime as dt
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "chapter-01" / "activity" / "data"

# The day the three CSV files were pulled from FRED. Printed on the worksheet
# because the captain asked that students be told exactly where the numbers
# came from and when.
RETRIEVED = "4 September 2026"

FRED_LICENCE = "https://fred.stlouisfed.org/legal/#copyright-public-domain"


def _fred_url(series: str, start: str, end: str) -> str:
    return (f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
            f"&cosd={start}&coed={end}")


# --------------------------------------------------------------------------
# One window of one series
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Series:
    """A window of daily closes, plus everything identification can ask of it.

    Every attribute below is a fact about the record. Not one of them is a
    forecast, and that is the distinction the whole activity turns on.
    """

    key: str                 # part-a, part-b, reveal
    fred_id: str             # the series code, printed on the worksheet
    name: str                # what a human calls it
    unit: str                # what one unit of price buys
    origin: str              # the agency that measured it
    filename: str
    start: str
    end: str
    dates: tuple[dt.date, ...]
    closes: tuple[float, ...]
    dropped: int             # non-trading days removed from the raw file

    # -- shape of the sheet the student builds ----------------------------

    @property
    def rows(self) -> int:
        """Trading days, which is also the number of data rows."""
        return len(self.closes)

    @property
    def last_row(self) -> int:
        """The spreadsheet row the last price lands on, header included."""
        return self.rows + 1

    @property
    def data_range(self) -> str:
        return f"A1:B{self.last_row}"

    @property
    def price_range(self) -> str:
        return f"B2:B{self.last_row}"

    @property
    def date_range(self) -> str:
        return f"A2:A{self.last_row}"

    @property
    def change_range(self) -> str:
        return f"C3:C{self.last_row}"

    @property
    def fred_url(self) -> str:
        return _fred_url(self.fred_id, self.start, self.end)

    # -- the identification answers ---------------------------------------

    @property
    def first(self) -> float:
        return self.closes[0]

    @property
    def last(self) -> float:
        return self.closes[-1]

    @property
    def change(self) -> float:
        return round(self.last - self.first, 2)

    @property
    def pct_change(self) -> float:
        return (self.last - self.first) / self.first * 100.0

    @property
    def high(self) -> float:
        return max(self.closes)

    @property
    def high_date(self) -> dt.date:
        return self.dates[self.closes.index(self.high)]

    @property
    def low(self) -> float:
        return min(self.closes)

    @property
    def low_date(self) -> dt.date:
        return self.dates[self.closes.index(self.low)]

    @property
    def moves(self) -> tuple[float, ...]:
        """Close to close change, one per day after the first."""
        return tuple(round(b - a, 2)
                     for a, b in zip(self.closes, self.closes[1:]))

    @property
    def biggest_rise(self) -> float:
        return max(self.moves)

    @property
    def biggest_rise_date(self) -> dt.date:
        return self.dates[1 + self.moves.index(self.biggest_rise)]

    @property
    def biggest_fall(self) -> float:
        return min(self.moves)

    @property
    def biggest_fall_date(self) -> dt.date:
        return self.dates[1 + self.moves.index(self.biggest_fall)]

    @property
    def up_days(self) -> int:
        return sum(1 for m in self.moves if m > 0)

    @property
    def down_days(self) -> int:
        return sum(1 for m in self.moves if m < 0)

    @property
    def flat_days(self) -> int:
        return sum(1 for m in self.moves if m == 0)

    # -- swings, for the peaks and troughs half of Part B -----------------

    def swings(self, k: int = 5) -> tuple[tuple[str, dt.date, float], ...]:
        """Local highs and lows: the extreme of a window k days either side.

        A rule, not an opinion, so the key can print a defensible list. The
        worksheet never asks a student to reproduce it, because the chapter's
        whole point in Part 4 is that two analysts mark different swings.
        """
        out = []
        n = len(self.closes)
        for i in range(k, n - k):
            window = self.closes[i - k:i + k + 1]
            if self.closes[i] == max(window):
                out.append(("peak", self.dates[i], self.closes[i]))
            elif self.closes[i] == min(window):
                out.append(("trough", self.dates[i], self.closes[i]))
        return tuple(out)

    def on(self, when: str) -> float:
        """The close on a named date, so prose never retypes a number."""
        return self.closes[self.dates.index(dt.date.fromisoformat(when))]


def _load(key: str, fred_id: str, name: str, unit: str, origin: str,
          filename: str, start: str, end: str, dropped: int) -> Series:
    dates: list[dt.date] = []
    closes: list[float] = []
    with (DATA / filename).open() as fh:
        reader = csv.reader(fh)
        header = next(reader)
        if header != ["observation_date", fred_id]:
            raise SystemExit(
                f"{filename} does not carry FRED's own header for {fred_id}. "
                "The worksheet tells students the header they will see, so "
                "the file has to keep it."
            )
        for row in reader:
            dates.append(dt.date.fromisoformat(row[0]))
            closes.append(float(row[1]))
    if dates[0].isoformat() != start or dates[-1].isoformat() != end:
        raise SystemExit(
            f"{filename} runs {dates[0]} to {dates[-1]}, but this module "
            f"declares {start} to {end}. The worksheet prints the declared "
            "range, so the two have to agree."
        )
    return Series(key=key, fred_id=fred_id, name=name, unit=unit,
                  origin=origin, filename=filename, start=start, end=end,
                  dates=tuple(dates), closes=tuple(closes), dropped=dropped)


EIA = "U.S. Energy Information Administration"

PART_A = _load(
    key="part-a",
    fred_id="DHHNGSP",
    name="Henry Hub natural gas spot price",
    unit="US dollars per million British thermal units",
    origin=EIA,
    filename="part-a-DHHNGSP-2013-11-01-to-2014-03-31.csv",
    start="2013-11-01", end="2014-03-31", dropped=5,
)

PART_B = _load(
    key="part-b",
    fred_id="DCOILWTICO",
    name="West Texas Intermediate crude oil spot price, Cushing, Oklahoma",
    unit="US dollars per barrel",
    origin=EIA,
    filename="part-b-DCOILWTICO-2014-02-03-to-2014-06-30.csv",
    start="2014-02-03", end="2014-06-30", dropped=3,
)

REVEAL = _load(
    key="reveal",
    fred_id="DCOILWTICO",
    name="West Texas Intermediate crude oil spot price, Cushing, Oklahoma",
    unit="US dollars per barrel",
    origin=EIA,
    filename="reveal-DCOILWTICO-2014-07-01-to-2015-03-31.csv",
    start="2014-07-01", end="2015-03-31", dropped=7,
)


# --------------------------------------------------------------------------
# The trendline the key draws, and the day it broke
# --------------------------------------------------------------------------


def rising_line(series: Series, first: str, second: str
                ) -> tuple[dt.date, float, dt.date, float]:
    """The straight line through two named troughs, as two points."""
    a, b = dt.date.fromisoformat(first), dt.date.fromisoformat(second)
    return a, series.on(first), b, series.on(second)


def line_value(anchor: tuple[dt.date, float, dt.date, float],
               when: dt.date) -> float:
    """Where that line sits on a later day, measured in calendar days."""
    d1, p1, d2, p2 = anchor
    span = (d2 - d1).days
    return p1 + (p2 - p1) * ((when - d1).days / span)


# The two rising lines the key draws, each named by the two troughs it joins.
#
# There are two on purpose. Part 4 of the chapter runs Figure 1.20, one market
# top with two different uptrend lines under it, "each penetrated at a
# different price and a different moment", and asks the room to choose. These
# two are that figure happening to real prices: the long line holds for the
# whole window and breaks on 11 July, the steep one breaks on the first
# trading day after the window closes. Neither is the answer. That is the
# point, and the key says so beside the chart.
#
# Line A is a strict support line: no close in the window sits below it. Line
# B grazes the close of 5 June by four cents, which on a printed chart is
# inside the thickness of a pencil, and the key says that too.
TRENDLINES = (
    ("A", "the long line", "2014-02-03", "2014-05-05"),
    ("B", "the steep line", "2014-05-06", "2014-06-06"),
)


def trendline_break(first: str, second: str) -> tuple[dt.date, float, float]:
    """The first day after the window that closed below a rising line."""
    anchor = rising_line(PART_B, first, second)
    for day, close in zip(REVEAL.dates, REVEAL.closes):
        if close < line_value(anchor, day):
            return day, close, round(line_value(anchor, day), 2)
    raise SystemExit(
        f"the line through {first} and {second} was never broken in the "
        "reveal window, so the key has nothing to show"
    )


def trendline_facts():
    """Both lines, resolved: anchors, prices, and the day each one broke."""
    out = []
    for name, label, first, second in TRENDLINES:
        day, close, line = trendline_break(first, second)
        out.append({
            "name": name, "label": label,
            "first": dt.date.fromisoformat(first), "first_price": PART_B.on(first),
            "second": dt.date.fromisoformat(second), "second_price": PART_B.on(second),
            "broke_on": day, "broke_at": close, "line_at": line,
        })
    return out


def summary() -> str:
    """A one screen dump of every computed answer, for checking by eye."""
    out = []
    for s in (PART_A, PART_B, REVEAL):
        out.append(f"{s.key}  {s.fred_id}  {s.start} .. {s.end}")
        out.append(f"  rows {s.rows}  last row {s.last_row}  "
                   f"dropped {s.dropped}")
        out.append(f"  first {s.first}  last {s.last}  change {s.change}  "
                   f"pct {s.pct_change:+.2f}%")
        out.append(f"  high {s.high} on {s.high_date}  "
                   f"low {s.low} on {s.low_date}")
        out.append(f"  biggest rise {s.biggest_rise} on {s.biggest_rise_date}"
                   f"  biggest fall {s.biggest_fall} on "
                   f"{s.biggest_fall_date}")
        out.append(f"  up {s.up_days}  down {s.down_days}  "
                   f"flat {s.flat_days}")
        out.append("")
    for t in trendline_facts():
        out.append(f"line {t['name']} ({t['label']}) through {t['first']} "
                   f"{t['first_price']} and {t['second']} {t['second_price']}: "
                   f"broken {t['broke_on']} at {t['broke_at']} against "
                   f"{t['line_at']}")
    out.append("part B swings:")
    for kind, day, price in PART_B.swings():
        out.append(f"  {kind:7} {day} {price}")
    return "\n".join(out)


if __name__ == "__main__":                                # pragma: no cover
    print(summary())
