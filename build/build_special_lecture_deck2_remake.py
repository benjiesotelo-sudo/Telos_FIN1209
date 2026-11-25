#!/usr/bin/env python3
"""Deck 2 remake: the Stock Desk, plain talk style, diagrams only.

    .venv/bin/python build/build_special_lecture_deck2_remake.py

Same last-minute remake as decks 1 and 3: cut hard to essentials. Per
the captain's own words, this keeps only the "how it works" picture and
the BPMN decision-process diagram, redrawn large; the step-by-step guide
is dropped (he handles the walkthrough live). Both diagrams reuse
special_lecture_kit's own drawing code (already checked read-only
against the real stock-desk source; see content_special_lecture_deck2.py
for where an earlier draft differed from the code), just placed in the
new plain style instead of the old chrome.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import special_lecture_kit as slk  # noqa: E402
import content_special_lecture_deck2 as content  # noqa: E402
import talk_kit as kit  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PHOTOS = REPO / "build" / "assets" / "speaker-photos"
OUT = REPO / "special-lecture" / "FIN1209-Special-Lecture-2-StockDesk.pptx"
GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck2-remake"

COURSE = "FIN1209 - Technical Analysis in Investment"


def build() -> int:
    GENERATED.mkdir(parents=True, exist_ok=True)
    slk.GENERATED = GENERATED
    slk.apply_metropolis_style()  # sets METRO_ACCENT used by the diagrams

    data_flow_png = GENERATED / "data-flow.png"
    kit.make_flow_png(data_flow_png, tuple(t for t, _ in content.DATA_FLOW_NODES))

    bpmn1_png = GENERATED / "bpmn-1.png"
    slk.make_bpmn_vision_png_part1(bpmn1_png)
    bpmn2_png = GENERATED / "bpmn-2.png"
    slk.make_bpmn_vision_png_part2(bpmn2_png)

    slides: list[tuple[str, dict]] = [
        ("title", dict(
            course=COURSE,
            title="Stock Desk",
            subtitle="working name",
            notes=("Presenter: Benjamin C. Sotelo. Captain handles the "
                  "discussion live; these slides are the two diagrams "
                  "only, the live tool is demonstrated separately. "
                  "\"Stock Desk\" is not the final name; no other slide "
                  "uses it as a brand.",),
        )),
        ("speakers", dict(speakers=(
            ("Benjamin C. Sotelo", PHOTOS / "benjamin-sotelo.jpg"),
        ))),
        ("picture", dict(
            label="How it works",
            image_path=data_flow_png,
            notes=(
                "Yahoo prices + SEC filings: live quotes and company "
                "financial filings, both free sources.",
                "An automatic job: three Cloudflare crons in the real "
                "code (price every minute in market hours, once at the "
                "close, and SEC fundamentals one company per minute), "
                "simplified to one box here.",
                "The database: prices, indicators, signals, outcomes, "
                "and your buys.",
                "Chapter 8's rule: trend, momentum, the five-day "
                "trigger. Checked read-only against the real code: the "
                "gate is three checks only, volume is reported but "
                "never gates the signal (a correction from an earlier "
                "draft).",
                "Your page: behind your own passphrase.",
            ),
        )),
        ("picture", dict(
            label="The vision (1 of 2)",
            image_path=bpmn1_png,
            notes=(
                "This is the VISION, not today's build: where this could "
                "go, not the current code. Captain discusses live.",
                "Live prices, every minute. Choose a bar size, 5 minutes "
                "to weekly. Rules vote: a parallel split, all six run at "
                "once, every time (trend, momentum via RSI/MACD, "
                "breakout, volume, trendlines, support and resistance).",
                "Agreement score: e.g. \"4 of 6 agree: bullish.\" Never "
                "called a probability, only a count.",
                "Draw what's next: a projected trendline, zones, a stop "
                "and target, then handed to you (link A, continued on "
                "the next slide).",
                "Link B, entering the same parallel split: the feedback "
                "loop from part 2, once real outcomes are in.",
            ),
        )),
        ("picture", dict(
            label="The vision (2 of 2)",
            image_path=bpmn2_png,
            notes=(
                "This is the VISION, not today's build. Captain discusses "
                "live.",
                "You read the call, then a gateway: Buy, Sell, or Wait. "
                "Whatever you choose, you log it.",
                "Later, the tool checks the real outcome and learns which "
                "rules actually worked (data for a future machine "
                "learning pass), feeding that back (link B) into part "
                "1's parallel split, so the vote itself can improve.",
            ),
        )),
        ("closing", dict(line="Thank you", notes=())),
    ]

    return kit.build_presentation(
        slides, out_path=OUT,
        title="FIN1209 Special Lecture 2 - Stock Desk",
        course=COURSE, author="Benjamin C. Sotelo",
    )


if __name__ == "__main__":
    count = build()
    print(f"{OUT}: {count} slides")
