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
OUT = REPO / "special-lecture" / "FIN1209-Special-Lecture-2-StockDesk.pptx"
GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck2-remake"

COURSE = "FIN1209 - Technical Analysis in Investment"


def build() -> int:
    GENERATED.mkdir(parents=True, exist_ok=True)
    slk.GENERATED = GENERATED
    slk.apply_metropolis_style()  # sets METRO_ACCENT used by the diagrams

    data_flow_png = GENERATED / "data-flow.png"
    slk.make_data_flow_png(data_flow_png, content.DATA_FLOW_NODES,
                           accent_index=content.DATA_FLOW_ACCENT_INDEX)

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
        ("speakers", dict(speakers=(("Benjamin C. Sotelo", None),))),
        ("picture", dict(
            label="How it works",
            image_path=data_flow_png,
            notes=("Checked read-only against the real code: three Cloudflare "
                  "crons (price/minute, close, SEC one-per-minute), the "
                  "database stores candles/indicators/signals/outcomes/buys, "
                  "the rule gates on three checks only (volume is reported, "
                  "not a gate, a correction from an earlier draft).",),
        )),
        ("picture", dict(
            label="The decision process (1 of 2)",
            image_path=bpmn1_png,
            notes=content.BPMN_SLIDE["notes"],
        )),
        ("picture", dict(
            label="The decision process (2 of 2)",
            image_path=bpmn2_png,
            notes=(),
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
