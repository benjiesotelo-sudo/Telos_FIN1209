#!/usr/bin/env python3
"""Build the Chapter 7 take-home, "First Automation FIN1209": the handout PDF.

    .venv/bin/python build/run_stages.py --data <folder with start/ and update/>
    .venv/bin/python build/build_flowchart.py
    .venv/bin/python build/build_activity2.py

run_stages.py really runs every step of the guide in R and records what R
printed, so no output in the handout is typed. The handout is one PDF; the
grading key and grader are private and live outside the repository.
`--draft` renders missing screenshots as empty boxes, for layout work only.
"""
import argparse, json, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activitykit  # noqa: E402
import build_activity as ba  # noqa: E402
import chrome  # noqa: E402
import activity_chapter07 as A  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = A.STUDENT / f"{A.NAME}.pdf"
SCREENS = REPO / "chapter-07" / "activity" / "screens"
GENERATED = REPO / "build" / "generated" / "activity2"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", action="store_true")
    ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    modes = json.loads((GENERATED / "modes.json").read_text())
    info = json.loads((GENERATED / "why_info.json").read_text())
    act = A.build_activity(modes, info)
    for sec in act.sections:          # steps restart at 1 in every part
        n = 0
        for blk in sec.blocks:
            if isinstance(blk, activitykit.Step):
                n += 1
                blk.number = n
    shots = ba.prepare_shots(act, SCREENS, GENERATED / "shots")
    problems = activitykit.validate(act, shots)
    if a.draft:
        problems = [p for p in problems if "screenshot" not in p]
    if "(run build/run_stages.py)" in json.dumps(
            [getattr(b, "output", "") for s in act.sections for b in s.blocks]):
        problems.append("a run has no real R output; run build/run_stages.py")
    if problems:
        raise SystemExit("Rules violated:\n  " + "\n  ".join(problems))
    pages = ba.build_one(act, shots, a.out, chrome.CHROME, key=False, keep_html=False)
    print(f"{a.out.name}: {pages} pages, {len(act.steps())} steps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
