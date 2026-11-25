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
    slk.make_bpmn_signal_png_part1(bpmn1_png)
    bpmn2_png = GENERATED / "bpmn-2.png"
    slk.make_bpmn_signal_png_part2(bpmn2_png)

    slides: list[tuple[str, dict]] = [
        ("title", dict(
            course=COURSE,
            title="The Stock Desk",
            notes=("Presenter: Benjamin C. Sotelo. Captain handles the "
                  "discussion live; these slides are the two diagrams "
                  "only, the live tool is demonstrated separately.",),
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
            label="The decision process (1 of 2)",
            image_path=bpmn1_png,
            notes=content.BPMN_SLIDE["notes"] + (
                "What each step is worth: Compute indicators, one shared "
                "formula, every stock, no arguing over the math. Three "
                "checks, no signal fires on a hunch (volume is shown "
                "beside it, not required to fire one). Show signal, you "
                "see it the moment it is real, never a stale page. You "
                "decide, your money, your call, always.",
            ),
        )),
        ("picture", dict(
            label="The decision process (2 of 2)",
            image_path=bpmn2_png,
            notes=(
                "What each step is worth: Log a buy, one record, so the "
                "scoreboard can grade it later. Stop, target: advice, a "
                "number to check yourself against, never an auto-sell. "
                "Sell or hold, still your call. Log a sell, closes the "
                "record the scoreboard will grade. Scoreboard, +5 days "
                "(a sub-process, runs on the close cron, not inline): "
                "proof the rule works, or does not, in public.",
            ),
        )),
        ("closing", dict(line="Thank you", notes=())),
    ]

    return kit.build_presentation(
        slides, out_path=OUT,
        title="FIN1209 Special Lecture 2 - The Stock Desk",
        course=COURSE, author="Benjamin C. Sotelo",
    )


if __name__ == "__main__":
    count = build()
    print(f"{OUT}: {count} slides")
