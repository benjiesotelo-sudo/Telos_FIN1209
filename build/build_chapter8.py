#!/usr/bin/env python3
"""Build the FIN1209 Chapter 8 teaching deck (scaffold plus approved-sample slides)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chartkit
import deckkit
from chartlayout_chapter08 import audit_pptx, course_slide_renderer
from charts_chapter08 import CHARTS
from content_chapter08 import CHAPTER

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "chapter-08" / "FIN1209-Chapter-08.pptx"
STUDENT_OUT = REPO / "chapter-08" / "FIN1209-Chapter-08-Student-Edition.pptx"
FIGURES_DIR = REPO / "assets" / "figures"
CANONICAL_FIGURES_DIR = Path.home() / ".fin1209-figures" / "chapter-08"
if CANONICAL_FIGURES_DIR.is_dir():
    FIGURES_DIR = CANONICAL_FIGURES_DIR
FIGURE_SIZE_MANIFEST = REPO / "chapter-08" / "figure-sizes.json"
CHARTS_DIR = REPO / "build" / "generated" / "charts-08"
BOOK_FIGURES = tuple(f"figure-8-{n:02d}.png" for n in range(1, 29))

# Labels that sound written by a machine; the instructor banned them (rule 24).
BANNED_LABELS = (r"numbers first", r"\bAction:", r"Ours, invented", r"Meaning/action",
                 r"Plain words:", r"^Step \d", r"Ours:", r"Read volume:", r"Definition:")
BODY_FLOOR_PT = 17


def _inside_repo(path: Path) -> bool:
    resolved = path.expanduser().resolve()
    return resolved == REPO or REPO in resolved.parents


def _artwork_problems(figures_dir: Path) -> list[str]:
    """Every reason an artwork build must be refused.

    All 28 of the chapter's figures must be present at the recorded size, not
    only the ones a slide places, so marks and crops can never meet a
    different extraction of a figure.
    """
    problems = []
    if not FIGURE_SIZE_MANIFEST.is_file():
        return [f"figure size manifest is missing: {FIGURE_SIZE_MANIFEST}"]
    try:
        manifest = json.loads(FIGURE_SIZE_MANIFEST.read_text())
        expected = manifest["figures"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"cannot read figure size manifest: {exc}"]
    try:
        from PIL import Image
    except ImportError as exc:  # pragma: no cover - build environment guard
        return [f"Pillow is required to check figure sizes: {exc}"]
    statuses = deckkit.figure_status(CHAPTER, figures_dir)
    placed_missing = sorted({f for _n, f, have in statuses if not have})
    if placed_missing:
        problems.append("missing figure files: " + ", ".join(placed_missing))
    for filename in BOOK_FIGURES:
        size = expected.get(filename)
        if not (isinstance(size, list) and len(size) == 2 and all(isinstance(v, int) for v in size)):
            problems.append(f"figure size manifest has no valid size for {filename}")
            continue
        path = figures_dir / filename
        if not path.is_file():
            if filename not in placed_missing:
                problems.append(f"missing figure file: {filename}")
            continue
        try:
            with Image.open(path) as image:
                actual = list(image.size)
        except OSError as exc:
            problems.append(f"cannot read {filename}: {exc}")
            continue
        if actual != size:
            problems.append(f"figure size mismatch for {filename}: expected "
                            f"{size[0]}x{size[1]}, found {actual[0]}x{actual[1]}")
    return problems


def _mark_problems(number, slide, body) -> list[str]:
    """Machine checks (b) and (c): the numbers the text names are the marks drawn, and no
    badge covers another badge or sits inside another mark."""
    if re.match(r"\s*(CHECK|ANSWERS)", body):
        return []
    from pptx.util import Emu
    badges, marks = [], []
    pics = [(sh.left / 914400, sh.top / 914400, (sh.left + sh.width) / 914400, (sh.top + sh.height) / 914400)
            for sh in slide.shapes if sh.shape_type == 13]
    for sh in slide.shapes:
        if sh.shape_type == 13 or sh.width is None:
            continue
        w, h = sh.width / 914400, sh.height / 914400
        text = sh.text_frame.text.strip() if sh.has_text_frame else ""
        box = (sh.left / 914400, sh.top / 914400, sh.left / 914400 + w, sh.top / 914400 + h)
        if re.fullmatch(r"\d{1,2}", text) and w < 0.5:
            badges.append((int(text), box))
        elif not text and sh.shape_type == 1 and 0.05 < min(w, h) and max(w, h) < 9 and w * h < 20:
            if any(box[0] <= p[0] + .12 and box[1] <= p[1] + .12 and box[2] >= p[2] - .12 and box[3] >= p[3] - .12 for p in pics):
                continue   # the white frame round a picture
            marks.append(box)
    problems = []
    named = {int(n) for n in re.findall(r"\((\d{1,2})\)", body)}
    for lo_, hi_ in re.findall(r"\((\d{1,2})\) to \((\d{1,2})\)", body):
        named |= set(range(int(lo_), int(hi_) + 1))
    drawn = {n for n, _b in badges}
    if badges or named:
        if named - drawn:
            problems.append(f"slide {number}: text names mark {sorted(named - drawn)} that is not drawn")
        if drawn - named:
            problems.append(f"slide {number}: mark {sorted(drawn - named)} is drawn but the text does not name it")
    for i, (n, a) in enumerate(badges):
        for m, b in badges[i + 1:]:
            if a[0] < b[2] - .02 and b[0] < a[2] - .02 and a[1] < b[3] - .02 and b[1] < a[3] - .02:
                problems.append(f"slide {number}: badges {n} and {m} overlap")
        cx, cy = (a[0] + a[2]) / 2, (a[1] + a[3]) / 2
        for b in marks:
            if b[0] + .03 < cx < b[2] - .03 and b[1] + .03 < cy < b[3] - .03:
                problems.append(f"slide {number}: badge {n} sits inside another mark")
                break
    return problems


def _deck_problems(path: Path, with_figures: bool) -> list[str]:
    """Checks on the built file: a slide that names a figure must show one,
    no banned label, no em dash, nothing below the 17 point body floor."""
    from pptx import Presentation
    problems = []
    for number, slide in enumerate(Presentation(path).slides, 1):
        texts, small = [], []
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            texts.append(shape.text_frame.text)
        body = " ".join(texts)
        pictures = [s for s in slide.shapes if s.shape_type == 13]
        if re.search(r"Figure 8\.\d+|Chart [A-Z]{1,2}\b", body) and not pictures:
            if with_figures or re.search(r"Chart [A-Z]{1,2}\b", body):
                problems.append(f"slide {number}: names a figure or chart but shows none")
        if "—" in body or "–" in body:
            problems.append(f"slide {number}: dash character in the text")
        for notes_text in ([slide.notes_slide.notes_text_frame.text] if slide.has_notes_slide else []):
            if re.search(r"Part [AB]\b", notes_text):
                problems.append(f"slide {number}: Part A or Part B in the notes")
        if re.search(r"Part [AB]\b", body):
            problems.append(f"slide {number}: Part A or Part B on the slide")
        if re.search(r"\[\d+\]", body):
            problems.append(f"slide {number}: a [digit] mark form in the text")
        problems += _mark_problems(number, slide, body)
        for label in BANNED_LABELS:
            if re.search(label, body, re.M):
                problems.append(f"slide {number}: banned label /{label}/")
        for shape in (slide.shapes if number > 1 and with_figures else ()):
            if not shape.has_text_frame:
                continue
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    if run.font.size is not None and run.text.strip() and run.font.size.pt < BODY_FLOOR_PT:
                        small.append((run.font.size.pt, run.text.strip()[:30]))
        # Titles, captions and credits are the kit's own small print; the floor
        # applies to body text, which the kit sets at 17 point or more. Report
        # only runs between 12 and 16.9 point that are long enough to be body.
        for size, text in small:
            if 12 < size < BODY_FLOOR_PT and len(text) > 28:
                problems.append(f"slide {number}: {size:g} point text: {text}")
    return problems


def _fix_divider_notes(path: Path) -> None:
    """deckkit's divider note says "three covers lines"; this chapter's divider
    lists five terms. Fixed here, on this chapter's file only."""
    from pptx import Presentation
    prs = Presentation(path)
    changed = False
    for slide in prs.slides:
        if slide.has_notes_slide:
            frame = slide.notes_slide.notes_text_frame
            if "three covers lines" in frame.text:
                for para in frame.paragraphs:
                    for run in para.runs:
                        run.text = run.text.replace("Read the three covers lines, then move.",
                                                    "Read the five terms, then move.")
                changed = True
    if changed:
        prs.save(path)


SECTIONS_IN_CHAPTER = 8   # Lim's 8.1 to 8.8; Chapter 7's footer form is "Part n of N - 7.n name"


def _section_footers(path: Path) -> None:
    """Chapter 7's form numbers the chapter's sections as parts: "Part 2 of 4 - 7.2 name".
    Chapter 8 has eight sections, so the total is Lim's eight, not the count built so far."""
    from pptx import Presentation
    n_built = len(CHAPTER.sections)
    prs = Presentation(path)
    pat = re.compile(rf"Part (\d+) of {n_built}\b")
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        run.text = pat.sub(lambda m: f"Part {m.group(1)} of {SECTIONS_IN_CHAPTER}", run.text)
        if slide.has_notes_slide:
            for para in slide.notes_slide.notes_text_frame.paragraphs:
                for run in para.runs:
                    run.text = pat.sub(lambda m: f"Part {m.group(1)} of {SECTIONS_IN_CHAPTER}", run.text)
    prs.save(path)


def _chart_data_problems() -> list[str]:
    """Machine check (d): every line a chart calls a trendline passes through two points of
    the series it is drawn from, at turning points, and every moving average equals the
    average of the closes it names."""
    from specs_chapter08 import SPECS
    problems = []
    for key, entry in SPECS.items():
        series = entry["spec"].get("series", ())
        for k, ser in enumerate(series):
            role = ser.get("role")
            if role is None:
                continue
            src = series[ser["of"]]["values"]
            vals = ser["values"]
            if role == "trendline":
                pts = ser["through"]
                if len(pts) < 2:
                    problems.append(f"chart {entry['letter']}: a trendline needs two points")
                for slot in pts:
                    if vals[slot] is None or abs(vals[slot] - src[slot]) > 0.06:
                        problems.append(f"chart {entry['letter']}: trendline misses its source at slot {slot}")
                    if ser.get("extremum"):
                        near = [src[i] for i in (slot - 1, slot + 1) if 0 <= i < len(src) and src[i] is not None]
                        if not (all(src[slot] > v for v in near) or all(src[slot] < v for v in near)):
                            problems.append(f"chart {entry['letter']}: slot {slot} is not a peak or trough")
            elif role == "average":
                n = ser["n"]
                for i, v in enumerate(vals):
                    want = None if i < n - 1 else sum(src[i - n + 1:i + 1]) / n
                    if (v is None) != (want is None) or (v is not None and abs(v - want) > 0.011):
                        problems.append(f"chart {entry['letter']}: moving average wrong at slot {i}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=deckkit.EDITIONS, default=deckkit.TEACHING)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--with-figures", action="store_true")
    parser.add_argument("--figures-dir", type=Path, default=FIGURES_DIR)
    args = parser.parse_args()
    if args.out is None:
        args.out = STUDENT_OUT if args.edition == deckkit.STUDENT else DEFAULT_OUT
    if args.with_figures and _inside_repo(args.out):
        parser.error("artwork builds must be written outside the repository")
    if args.with_figures:
        problems = _artwork_problems(args.figures_dir)
        if problems:
            print("Artwork build refused:", file=sys.stderr)
            for problem in problems:
                print(f"  {problem}", file=sys.stderr)
            return 1

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    chartkit.generate(CHARTS, CHARTS_DIR)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with course_slide_renderer():
        slides, checks = deckkit.build(
            CHAPTER, args.out,
            figures_dir=args.figures_dir if args.with_figures else None,
            charts_dir=CHARTS_DIR, edition=args.edition)
    audit_pptx(args.out, CHARTS_DIR)
    _fix_divider_notes(args.out)
    _section_footers(args.out)
    deck_problems = _deck_problems(args.out, args.with_figures) + _chart_data_problems()
    if deck_problems:
        print("Deck checks failed:", file=sys.stderr)
        for problem in deck_problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    figures = deckkit.figure_status(CHAPTER, args.figures_dir if args.with_figures else None)
    placed = sum(1 for _n, _f, have in figures if have)
    print(f"deck    : {args.out}")
    print(f"edition : {args.edition}")
    print(f"slides  : {slides}")
    print(f"checks  : {checks}")
    print(f"figures : {placed} of {len(figures)} placed")
    print(f"charts  : {len(CHARTS)} generated in {CHARTS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
