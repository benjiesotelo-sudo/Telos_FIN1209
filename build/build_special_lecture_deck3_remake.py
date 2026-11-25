#!/usr/bin/env python3
"""Deck 3 remake: build a simple stock tool, plain talk style.

    .venv/bin/python build/build_special_lecture_deck3_remake.py

Same last-minute remake as deck 1: plain conference-talk style, cut hard
to essentials. The five prompts, in full, one per slide, exactly as
verified in data/fin1209-deck3-run/report.md; nothing else. No fallback
lines, no explanation sentences; speaker notes carry the detail.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import talk_kit as kit  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "special-lecture" / "FIN1209-Special-Lecture-3-BuildIt.pptx"

COURSE = "FIN1209 - Technical Analysis in Investment"

PROMPTS = [
    (
        "Write a short PLAN.md in this empty folder for a tiny local "
        "web app called Stock Desk Mini. Rules: only Python 3 standard "
        "library, no pip installs, no npm, no other packages. One web "
        "page: pick one of three indexes (S&P 500, Nasdaq Composite, "
        "Dow Jones Industrial Average), see a line chart of its last 6 "
        "months of daily closing prices with its 20-day and 50-day "
        "moving averages, and one reading of BUY, SELL, or HOLD. Trend "
        "is price versus the 50-day average, momentum is 14-day RSI "
        "versus 50, and the trigger is the day's close breaking above "
        "the prior 5 trading days' high or below the prior 5 trading "
        "days' low. Data must be free, need no account and no API key: "
        "use the FRED fredgraph.csv endpoint, for example https://fred."
        "stlouisfed.org/graph/fredgraph.csv?id=SP500 for the S&P 500, "
        "id=NASDAQCOM for Nasdaq, id=DJIA for Dow. A browser page "
        "cannot fetch that URL directly, so a small Python server must "
        "fetch the CSV itself and hand the page JSON. List the exact "
        "files you will create and how the BUY, SELL, HOLD reading is "
        "computed. Do not write any code yet, only the plan.",
        ("Verified: Codex did not write code early, in either real run.",),
    ),
    (
        "Build server.py from the plan. Fetch the FRED CSV by running "
        "the system curl command (not Python's urllib, which hangs on "
        "this network) with a 15 second timeout, and raise a clear "
        "error if curl is missing or fails. Compute the 20-day and "
        "50-day moving averages, the 14-day RSI, and the BUY, SELL, or "
        "HOLD reading. Before building anything else, run the data "
        "function directly from the command line for the S&P 500, with "
        "up to 3 retries if the network call fails, and print the "
        "latest date, close, 20-day average, 50-day average, RSI, and "
        "reading so I can check the math by eye.",
        ("The one real failure across both verification runs: Python's "
         "own urllib timed out fetching FRED on that network every "
         "time, while curl on the same URL succeeded instantly; the fix "
         "is in the prompt text itself.",),
    ),
    (
        "Now build index.html, app.js, and style.css so the page is "
        "actually usable: a dropdown for the three indexes, a chart of "
        "the daily close with the 20-day and 50-day averages drawn on "
        "top in different colors with a small legend, the latest close "
        "and date, and a clear BUY, SELL, or HOLD reading in large text "
        "with the three conditions (trend, momentum, trigger) shown as "
        "pass or fail under it. Wire it to server.py's /api/prices "
        "endpoint. Keep it on one page, plain HTML, CSS, and "
        "JavaScript, no build step, no frameworks.",
        ("Did not fail in either verification run.",),
    ),
    (
        "Make server.py listen on all local network addresses "
        "(0.0.0.0), not only this Mac, then tell me the exact command "
        "to start it so it keeps running, the exact address to open in "
        "a browser on this same Mac, and this Mac's local Wi-Fi "
        "address so I can open the same page on my phone on the same "
        "Wi-Fi.",
        ("On the machine this was verified on, macOS reported Wi-Fi as "
         "\"off\" even though the interface still carried an address; "
         "worth a quick glance at System Settings beforehand.",),
    ),
    (
        "Quickly check all three indexes once more by requesting "
        "/api/prices for each from the running server, and tell me in "
        "one line whether each one returns a reading of BUY, SELL, or "
        "HOLD with no errors.",
        ("Did not fail in either verification run.",),
    ),
]

SLIDES: list[tuple[str, dict]] = [
    ("title", dict(
        course=COURSE,
        title="Build a Simple Stock Tool, Then View It",
        notes=("Presenter: Benjamin C. Sotelo. Captain handles the "
              "discussion live; these slides are the five prompts, "
              "verbatim, nothing else.",),
    )),
    ("speakers", dict(
        speakers=(("Benjamin C. Sotelo", None),),
    )),
]
for i, (text, notes) in enumerate(PROMPTS, start=1):
    SLIDES.append(("line", dict(label="Prompt", line=f'"{text}"',
                                notes=notes)))
SLIDES.append(("closing", dict(line="Thank you", notes=())))


def build() -> int:
    return kit.build_presentation(
        SLIDES, out_path=OUT,
        title=f"FIN1209 Special Lecture 3 - Build a Simple Stock Tool",
        course=COURSE, author="Benjamin C. Sotelo",
    )


if __name__ == "__main__":
    count = build()
    print(f"{OUT}: {count} slides")
