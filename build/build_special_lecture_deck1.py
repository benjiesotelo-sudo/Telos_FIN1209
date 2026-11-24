#!/usr/bin/env python3
"""Build deck 1 of 3: set up Codex, Git and GitHub for the first time.

    .venv/bin/python build/build_special_lecture_deck1.py
    .venv/bin/python build/build_special_lecture_deck1.py --edition student

One of three special-lecture decks sharing build/special_lecture_kit.py
and a neutral (not FEU) visual style:

    1. (this file) Set up Codex, Git and GitHub.
    2. The Stock Desk guide (build_special_lecture_deck2.py), one feature
       per slide, built from the real screenshots in
       data/stock-desk-guide/guide/png/ in the firstmate home.
    3. Build a simple stock tool with structured prompts, then view it
       (build_special_lecture_deck3.py), built only from
       data/fin1209-deck3-run/report.md once that report lands; another
       worker is producing it.

This deck is not a textbook chapter, so it does not use deckkit.Chapter/
Section/build() (parts, dividers, checks, an answer sheet, a run card):
none of that exists here because nothing here claims to teach Lim's book.
It reuses deckkit's Content/TitleSlide/Closing slide types through
special_lecture_kit, with a neutral palette (apply_neutral_palette()), not
FEU's green and gold, and the two-edition switch: the teaching edition
carries speaker cues, the student edition does not.

Presenters, per the captain's own 25 Nov answer: both discuss the setup;
he presents the macOS run, Tyrone Miguel Arrollado presents the Windows
run; shared slides (what an AI CLI tool is, what Git/GitHub are, the
walkthrough, working as a group) are marked "both". Each slide's presenter
label is drawn automatically from its content data (content_special_
lecture_deck1.py), level with the progress marker.

Every command this deck shows was fetched or genuinely run today; see
content_special_lecture_deck1.py's module docstring and each slide's
speaker notes for the exact source or the exact command run. Never taken
from memory and never staged as something it is not.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import deckkit  # noqa: E402
import special_lecture_kit as kit  # noqa: E402
import content_special_lecture_deck1 as content  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "special-lecture"
DECK_OUT = OUT_DIR / "FIN1209-Special-Lecture-1-Setup.pptx"
STUDENT_OUT = OUT_DIR / "FIN1209-Special-Lecture-1-Setup-Student-Edition.pptx"
DEFAULT_OUT = {deckkit.TEACHING: DECK_OUT, deckkit.STUDENT: STUDENT_OUT}

GH_DOCS_ASSETS = REPO / "build" / "assets" / "github-docs-screenshots"


def _build_walkthrough_images() -> list[Path]:
    paths = []
    for i, step in enumerate(content.WALKTHROUGH):
        dst = kit.GENERATED / f"walkthrough-{i:02d}.png"
        if step["kind"] == "terminal":
            watermark = ("ILLUSTRATION"
                        if step.get("label") == "ILLUSTRATION" else None)
            kit.make_terminal_png(dst, step["term_lines"],
                                  diff_mode=step.get("diff_mode", False),
                                  watermark=watermark)
        elif step["kind"] == "doc":
            kit.make_doc_card_png(dst, site=step["doc_site"],
                                  lines=step["doc_lines"])
        elif step["kind"] == "dialog":
            kit.make_mac_dialog_png(dst, title=step["dialog_title"],
                                    message=step["dialog_message"],
                                    buttons=step["dialog_buttons"])
        elif step["kind"] == "image":
            dst = GH_DOCS_ASSETS / step["image_file"]
        else:
            raise ValueError(step["kind"])
        paths.append(dst)
    return paths


def build(edition: str, out_path: Path) -> int:
    deckkit.INCLUDE_NOTES = edition == deckkit.TEACHING
    kit.apply_neutral_palette()
    kit.GENERATED = REPO / "build" / "generated" / "special-lecture" / "deck1"

    mac_install_png = kit.GENERATED / "mac-install.png"
    kit.make_terminal_png(mac_install_png, content.MAC_INSTALL_STEP["term_lines"])
    win_install_png = kit.GENERATED / "win-install.png"
    kit.make_terminal_png(win_install_png, content.WIN_INSTALL_STEP["term_lines"])
    mac_error_png = kit.GENERATED / "codex-path-error-mac.png"
    kit.make_terminal_png(mac_error_png, content.MAC_ERROR_SHOT["term_lines"],
                          font_size=46, line_h=78)
    win_error_png = kit.GENERATED / "codex-path-error-win.png"
    kit.make_terminal_png(win_error_png, content.WIN_ERROR_SHOT["term_lines"],
                          font_size=46, line_h=78)
    signin_png = kit.GENERATED / "signin.png"
    kit.make_doc_card_png(signin_png, site=content.SIGNIN_STEP["doc_site"],
                          lines=content.SIGNIN_STEP["doc_lines"])
    git_github_png = kit.GENERATED / "git-github-flow.png"
    kit.make_git_github_flow_png(git_github_png)
    walkthrough_images = _build_walkthrough_images()

    prs_slides: list[tuple[str, object]] = []
    prs_slides.append(("title", content.TITLE))
    prs_slides.append(("speakers", dict(speakers=content.SPEAKERS)))
    prs_slides.append(("content", content.AI_CLI_INTRO))
    prs_slides.append(("step", content.MAC_INSTALL_STEP | {"path": mac_install_png}))
    prs_slides.append(("shot_text", content.MAC_ERROR_SHOT | {"path": mac_error_png}))
    prs_slides.append(("step", content.WIN_INSTALL_STEP | {"path": win_install_png}))
    prs_slides.append(("shot_text", content.WIN_ERROR_SHOT | {"path": win_error_png}))
    prs_slides.append(("step", content.SIGNIN_STEP | {"path": signin_png}))
    prs_slides.append(("content", content.TRANSITION))
    prs_slides.append(("shot", content.GIT_GITHUB_SHOT | {"path": git_github_png}))
    prs_slides.append(("content", content.WALKTHROUGH_INTRO))
    for step, image_path in zip(content.WALKTHROUGH, walkthrough_images):
        prs_slides.append(("step", {**step, "path": image_path}))
    prs_slides.append(("content", content.COLLAB_RULES))
    prs_slides.append(("closing", content.CLOSING))

    return kit.build_presentation(
        prs_slides, out_path=out_path,
        title=f"FIN1209 Special Lecture 1 - {content.TITLE.title}",
        course=content.TITLE.course, author="Benjamin C. Sotelo",
        edition=edition,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=deckkit.EDITIONS,
                        default=deckkit.TEACHING)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    out_path = args.out or DEFAULT_OUT[args.edition]
    count = build(args.edition, out_path)
    print(f"{out_path}: {count} slides ({args.edition} edition)")


if __name__ == "__main__":
    main()
