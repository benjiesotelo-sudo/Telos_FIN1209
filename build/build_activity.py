#!/usr/bin/env python3
"""Build the FIN1209 Chapter 1 take-home activity: worksheet and answer key.

    .venv/bin/python build/build_activity.py

Two PDFs come out of one content module:

    chapter-01/activity/FIN1209-Chapter-01-Activity-1.pdf            students
    chapter-01/activity/FIN1209-Chapter-01-Activity-1-Answer-Key.pdf instructor

The key is the worksheet plus the answers, the rubric notes and the reveal. It
is not a separate document and nothing in it is retyped, so an answer cannot
drift from the question it answers. Content is data in
build/activity_chapter01.py; the numbers are computed in
build/activity_data.py from the committed price files; layout is
build/activitykit.py, which knows nothing about any chapter.

Three things happen here that do not happen in the other builds.

**The screenshots are prepared.** The repository holds the unaltered 1440 by
900 captures. The crop and the highlight each step places them with are
declared beside the step, and this script applies them into
build/generated/activity/, which is gitignored the way the charts folder is.
The capture on disk is never modified.

**The reveal charts are drawn.** Like the deck's nine charts they are redrawn
on every build, so a fresh clone gets the real picture. Unlike the deck's
nine, they are drawn from real prices; build/activity_charts.py says why that
is allowed here and nowhere else.

**The steps are numbered here, not in the content.** Insert a step and the
rest renumber themselves.

After building, look at the result. Every page of both PDFs:

    DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
    $DATA/pdfpng chapter-01/activity/FIN1209-Chapter-01-Activity-1.pdf \\
        /tmp/act $(seq 1 14)
"""

from __future__ import annotations

import argparse
import dataclasses
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import activity_charts  # noqa: E402
import activitykit  # noqa: E402
import chrome  # noqa: E402
from activity_chapter01 import ACTIVITY  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "chapter-01" / "activity"
WORKSHEET = OUT_DIR / "FIN1209-Chapter-01-Activity-1.pdf"
ANSWER_KEY = OUT_DIR / "FIN1209-Chapter-01-Activity-1-Answer-Key.pdf"

SCREENS = OUT_DIR / "screens"

# Build output, gitignored, redrawn every time. Same reason as
# build/generated/charts: it is ours, so it never needs to be committed.
#
# Two folders, not one. prepare_shots empties the folder it writes into, so
# pointing both at the same place silently deleted the reveal charts after
# they had been drawn and printed two blank boxes into the answer key.
GENERATED = REPO / "build" / "generated" / "activity"
GENERATED_CHARTS = GENERATED / "charts"
GENERATED_SHOTS = GENERATED / "shots"

HIGHLIGHT = "#F2A900"


def number_steps(activity) -> None:
    """Walk the student's sections and number every step from one."""
    n = 0
    for section in activity.sections:
        for block in section.blocks:
            if isinstance(block, activitykit.Step):
                n += 1
                block.number = n


def place_charts(activity, charts: dict) -> None:
    """Give the key's Figure blocks the files this build just drew.

    The content module leaves the paths empty on purpose: it is data about the
    chapter and it should not know where a build writes its output.
    """
    wanted = ["reveal-full", "reveal-trendline"]
    figures = [b for s in activity.key_sections for b in s.blocks
               if isinstance(b, activitykit.Figure)]
    if len(figures) != len(wanted):
        raise SystemExit(
            f"the answer key places {len(figures)} charts but this build "
            f"draws {len(wanted)}. Name them in build_activity.py."
        )
    for figure, name in zip(figures, wanted):
        path = charts[name]
        if not path.is_file():
            raise SystemExit(
                f"{path} was not written, so the answer key would print an "
                "empty box where the reveal chart goes."
            )
        figure.path = path
        figure.credit = activity_charts.CREDIT


def prepare_shots(activity, source: Path, out: Path) -> activitykit.Shots:
    """Crop and annotate every capture a step places, into a build folder.

    Pillow is already a dependency of the chart build. Nothing here writes to
    the committed capture: a crop is a new file, so what the repository holds
    stays exactly what the screen showed.
    """
    from PIL import Image, ImageDraw

    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.png"):
        old.unlink()

    shots = activitykit.Shots(directory=source)
    seen: dict[str, int] = {}
    for section in activity.sections + activity.key_sections:
        for block in section.blocks:
            shot = getattr(block, "shot", None)
            if shot is None:
                continue
            src = source / f"{shot.name}.png"
            if not src.is_file():
                continue                      # validate() reports this
            if shot.crop is None and shot.box is None:
                shots.prepared[id(shot)] = src
                with Image.open(src) as im:
                    shots.sizes[id(shot)] = im.size
                continue
            seen[shot.name] = seen.get(shot.name, 0) + 1
            target = out / f"{shot.name}-{seen[shot.name]}.png"
            with Image.open(src) as im:
                im = im.convert("RGB")
                if shot.box is not None:
                    draw = ImageDraw.Draw(im)
                    x, y, w, h = shot.box
                    draw.rectangle([x, y, x + w, y + h],
                                   outline=HIGHLIGHT, width=4)
                if shot.crop is not None:
                    im = im.crop(shot.crop)
                im.save(target)
                shots.sizes[id(shot)] = im.size
            shots.prepared[id(shot)] = target
    return shots


def build_one(activity, shots, out_path: Path, chrome_bin: Path,
              key: bool, keep_html: bool) -> int:
    document = activitykit.render(activity, shots, key=key)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "activity.html"
        html_path.write_text(document, encoding="utf-8")
        chrome.render_pdf(html_path, out_path, chrome_bin)
        if keep_html:
            kept = out_path.with_suffix(".html")
            shutil.copyfile(html_path, kept)
            print(f"html   : {kept}")
    return chrome.page_count(out_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--chrome", type=Path, default=chrome.CHROME)
    parser.add_argument("--screens", type=Path, default=SCREENS)
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside each PDF")
    args = parser.parse_args()

    activity = ACTIVITY
    number_steps(activity)

    charts = activity_charts.generate(GENERATED_CHARTS)
    place_charts(activity, charts)

    shots = prepare_shots(activity, args.screens, GENERATED_SHOTS)

    problems = activitykit.validate(activity, shots)
    if problems:
        raise SystemExit(
            "Activity design rules violated:\n  " + "\n  ".join(problems))

    worksheet = args.out_dir / WORKSHEET.name
    key_pdf = args.out_dir / ANSWER_KEY.name

    w_pages = build_one(activity, shots, worksheet, args.chrome,
                        key=False, keep_html=args.keep_html)
    k_pages = build_one(activity, shots, key_pdf, args.chrome,
                        key=True, keep_html=args.keep_html)

    steps = activity.steps()
    with_shots = sum(1 for s in steps if s.shot is not None)
    print(f"worksheet : {_relative(worksheet)}  {w_pages} pages")
    print(f"answer key: {_relative(key_pdf)}  {k_pages} pages")
    print(f"steps     : {len(steps)}, {with_shots} of them with a screenshot")
    print(f"questions : {len(activity.questions())} identification answers, "
          f"all computed from the price files")
    print(f"charts    : {len(charts)} redrawn by this build into "
          f"{_relative(GENERATED_CHARTS)}")
    print(f"screens   : {len(shots.prepared)} prepared from "
          f"{_relative(args.screens)}, originals untouched")
    print("look at both PDFs: every page, as an image, before you commit.")
    return 0


def _relative(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(REPO))
    except ValueError:
        return str(p)


if __name__ == "__main__":
    raise SystemExit(main())
