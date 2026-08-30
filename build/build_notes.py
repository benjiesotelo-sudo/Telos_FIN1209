#!/usr/bin/env python3
"""Build the FIN1209 Chapter 1 teaching notes as a print-ready PDF.

    .venv/bin/python build/build_notes.py

Content is data in build/notes_chapter01.py. Layout is build/notekit.py, which
knows nothing about any chapter. This script wires the two together, resolves
every slide reference against the deck's own content so the notes cannot drift
away from the deck, writes HTML with real print CSS, and renders it with
headless Chrome.

Chapters 2 to 10 are a content file away, not a rewrite.

Why Chrome and not LibreOffice: the previous notes PDF went through an HTML
path that collapsed every table to one character per column. Chrome's
--headless --print-to-pdf renders the same engine the CSS was written for.

After building, look at the result. Every page:

    DATA=/Users/benjie/benjie-agent-workspace/data/fin1209-notes-rebuild
    $DATA/pdfpng chapter-01/FIN1209-Chapter-01-Notes.pdf /tmp/notes $(seq 1 24)

See chapter-01/notes-design.md for why the document looks the way it does.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deckkit  # noqa: E402
import notekit  # noqa: E402
from content_chapter01 import CHAPTER  # noqa: E402
from notes_chapter01 import NOTES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PDF_OUT = REPO / "chapter-01" / "FIN1209-Chapter-01-Notes.pdf"

CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


# --------------------------------------------------------------------------
# The deck, walked for slide numbers
# --------------------------------------------------------------------------


def index_deck(chapter) -> tuple[dict[str, int], dict[int, str],
                                notekit.DeckFacts, list[str]]:
    """Number every slide exactly the way deckkit.build numbers them.

    Returns the key to slide-number map, the check answer letters, the counts
    the notes quote, and any ambiguous keys.

    This deliberately mirrors the traversal in deckkit.build rather than
    opening the .pptx: the notes are built from the same source the deck is,
    so a content change moves both together.
    """
    slides: dict[str, int] = {}
    answers: dict[int, str] = {}
    part_checks: dict[int, list[int]] = {}
    collisions: list[str] = []
    n = 0

    def put(key: str) -> None:
        nonlocal n
        if key in slides:
            collisions.append(key)
            return
        slides[key] = n

    n += 1                                   # 1, title
    put("open:title")
    for i in range(0, len(chapter.objectives), 4):
        n += 1                               # 2 and 3, learning objectives
        put(f"open:objectives{i // 4 + 1}")
    n += 1                                   # 4, roadmap
    put("open:roadmap")

    check_index = 0
    figures = 0
    for section in chapter.sections:
        n += 1
        put(f"part:{section.number}")
        quote_index = 0
        for slide in section.slides:
            if isinstance(slide, deckkit.Check):
                check_index += 1
                n += 1
                put(f"check:{check_index}")
                n += 1
                put(f"reveal:{check_index}")
                answers[check_index] = "".join(
                    q.answer for q in slide.questions
                )
                part_checks.setdefault(section.number, []).append(check_index)
                continue
            n += 1
            if isinstance(slide, deckkit.Figure):
                figures += 1
                put(f"fig:{slide.number}")
            elif isinstance(slide, deckkit.Term):
                put(f"term:{slide.term}")
            elif isinstance(slide, deckkit.Quote):
                # Quotes repeat their source, so they are named by their
                # position within the part: quote:2:4 is the fourth quote
                # slide in Part 2.
                quote_index += 1
                put(f"quote:{section.number}:{quote_index}")
            elif isinstance(slide, deckkit.Content):
                put(f"slide:{slide.title}")
        n += 1
        put(f"recap:{section.number}")

    for slide in chapter.closing:
        n += 1
        title = getattr(slide, "title", "")
        if title:
            put(f"slide:{title}")

    facts = notekit.DeckFacts(
        total_slides=n,
        total_checks=check_index,
        total_figures=figures,
        part_checks=part_checks,
    )
    return slides, answers, facts, collisions


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------


def render_pdf(html_path: Path, pdf_path: Path, chrome: Path,
               timeout: float = 120.0) -> None:
    """Render with headless Chrome, then stop waiting for it.

    Chrome 151 writes the PDF within a few seconds and then, in --headless=new
    --print-to-pdf mode on macOS, frequently does not exit at all. Waiting on
    the process is therefore not a completion signal. What is: the file
    appearing, its size settling, and it ending in the PDF end-of-file marker.
    Once all three hold, the render is finished and Chrome is terminated.

    Do not replace this with the LibreOffice HTML path. That is what collapsed
    every table in the previous notes PDF to one character per column.
    """
    if not chrome.exists():
        raise SystemExit(
            f"headless Chrome not found at {chrome}. Install Google Chrome or "
            "pass --chrome."
        )
    if pdf_path.exists():
        pdf_path.unlink()

    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.resolve().as_uri(),
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        try:
            deadline = time.monotonic() + timeout
            last = -1
            stable = 0
            while time.monotonic() < deadline:
                time.sleep(0.5)
                if not pdf_path.exists():
                    if proc.poll() is not None:
                        raise SystemExit(
                            "Chrome exited without writing a PDF. Run the same "
                            "command by hand to see why."
                        )
                    continue
                size = pdf_path.stat().st_size
                if size == last and size > 0:
                    stable += 1
                    if stable >= 2 and _looks_complete(pdf_path):
                        return
                else:
                    stable = 0
                last = size
            raise SystemExit(
                f"Chrome did not finish a PDF within {timeout:.0f}s. The "
                f"in-page paginator may be looping; open {html_path} in a "
                "browser and check the console."
            )
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()


def _looks_complete(pdf_path: Path) -> bool:
    """A PDF Chrome has finished writing ends in its end-of-file marker."""
    with pdf_path.open("rb") as fh:
        fh.seek(max(0, pdf_path.stat().st_size - 2048))
        return b"%%EOF" in fh.read()


def pdf_page_count(pdf_path: Path) -> int:
    """Count pages without a PDF library: the page tree declares the total."""
    blob = pdf_path.read_bytes()
    counts = [int(m) for m in re.findall(rb"/Count\s+(\d+)", blob)]
    if counts:
        return max(counts)
    return len(re.findall(rb"/Type\s*/Page[^s]", blob))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PDF_OUT)
    parser.add_argument("--chrome", type=Path, default=CHROME)
    parser.add_argument(
        "--keep-html", action="store_true",
        help="also write the intermediate HTML beside the PDF, for inspection",
    )
    args = parser.parse_args()

    slides, answers, facts, collisions = index_deck(CHAPTER)
    if collisions:
        print("warning: ambiguous slide keys, first occurrence wins: "
              + ", ".join(sorted(set(collisions))), file=sys.stderr)

    res = notekit.Resolver(slides, answers)
    document = notekit.render(NOTES, res, facts)

    problems = notekit.validate(document, res)
    if problems:
        raise SystemExit(
            "Notes design rules violated:\n  " + "\n  ".join(problems)
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "notes.html"
        html_path.write_text(document, encoding="utf-8")
        render_pdf(html_path, args.out, args.chrome)
        if args.keep_html:
            kept = args.out.with_suffix(".html")
            shutil.copyfile(html_path, kept)
            print(f"html   : {kept.relative_to(REPO)}")

    pages = pdf_page_count(args.out)
    print(f"notes  : {args.out.relative_to(REPO)}")
    print(f"pages  : {pages}")
    print(f"deck   : {facts.total_slides} slides, {facts.total_checks} checks, "
          f"{facts.total_figures} figures")
    print(f"keys   : {len(slides)} slide references resolvable")
    print("look at it: every page, as an image, before you commit it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
