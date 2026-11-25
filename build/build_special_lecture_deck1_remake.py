#!/usr/bin/env python3
"""Deck 1 remake: set up Codex, cut to essentials, plain talk style.

    .venv/bin/python build/build_special_lecture_deck1_remake.py

Last-minute remake per the captain's own 25 Nov words: too cluttered,
too long, too wordy; wants a plain conference-talk look (one soft
background, one large line, almost nothing else), far fewer slides, and
no sentences of explanation anywhere on a slide; he handles the
discussion live. Every slide is a few words, one command, or one
prompt. Speaker detail (who presents which part, verification notes)
lives only in speaker notes.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import talk_kit as kit  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
PHOTOS = REPO / "build" / "assets" / "speaker-photos"
OUT = REPO / "special-lecture" / "FIN1209-Special-Lecture-1-Setup.pptx"

COURSE = "FIN1209 - Technical Analysis in Investment"
TYRONE = "Tyrone Miguel Arrollado"

SLIDES: list[tuple[str, dict]] = [
    ("title", dict(
        course=COURSE,
        title="Set Up Codex, Git and GitHub",
        notes=("Presenters: Benjamin C. Sotelo and Tyrone Miguel "
              "Arrollado. He does Mac, Tyrone does Windows; no tag on "
              "any slide, assign verbally in the room. The captain "
              "handles the discussion live; these slides are prompts "
              "and commands only.",),
    )),
    ("speakers", dict(
        speakers=(
            ("Benjamin C. Sotelo", PHOTOS / "benjamin-sotelo.jpg"),
            (TYRONE, PHOTOS / "tyrone-arrollado.jpg"),
        ),
    )),
    ("line", dict(
        line="You type what you want. It writes and runs the commands.",
        notes=("Both presenters. What an AI CLI tool is, in one line; "
              "captain discusses live.",),
    )),
    ("line", dict(
        label="CLI vs GUI",
        line="GUI: click where it is. CLI: say what you want.",
        notes=("Both presenters.",),
    )),
    ("line", dict(
        label="Install Codex: macOS",
        line='curl -fsSL https://chatgpt.com/codex/install.sh | sh',
        mono=True,
        notes=(
            "Benjamin presents this one.",
            "Verified today: installer's own real end-of-run message, "
            "\"Codex CLI 0.164.0 installed successfully.\"",
            "If codex: command not found right after: open a new "
            "terminal window (PATH is not active in this one yet).",
        ),
    )),
    ("line", dict(
        label="Install Codex: Windows",
        line='powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"',
        mono=True,
        notes=(
            f"{TYRONE} presents this one.",
            "Exact command quoted verbatim from github.com/openai/"
            "codex's README, fetched 25 Nov 2026 (native Windows "
            "install, no WSL).",
            "If it fails outright: close this PowerShell window, open a "
            "brand-new one (the installer only updates new windows), "
            f"and run: codex. If it still fails, {TYRONE} sets up WSL2, "
            "a supported path in the project's own docs.",
        ),
    )),
    ("line", dict(
        label="Sign in",
        line="codex login",
        mono=True,
        notes=(
            "Both presenters. A browser tab opens: sign in with your "
            "ChatGPT account.",
            "Real capture, 25 Nov 2026: isolated empty config, stopped "
            "the instant the real URL printed, before any sign-in "
            "completed; the real machine's own signed-in session was "
            "never touched.",
        ),
    )),
    ("line", dict(
        label="What we set up",
        line="Python. Git. GitHub.",
        notes=("Both presenters. Codex sets up each one from a prompt; "
              "captain discusses live, next four slides are the exact "
              "prompts.",),
    )),
    ("line", dict(
        label="Prompt",
        line='"Check whether python3 works on this computer. If macOS '
             'asks to install the command line developer tools, '
             'install them."',
        notes=(
            "Both presenters.",
            "On a genuinely fresh Mac this triggers a real Command Line "
            "Tools install dialog, which takes a few minutes and needs "
            "a mouse click; Codex cannot click through it alone. Doing "
            "this once before class means Codex is not blocked "
            "mid-lecture.",
        ),
    )),
    ("line", dict(
        label="Prompt",
        line='"Check whether Git is installed on this computer. If it '
             'is not, install it, then tell me how to confirm it '
             'worked."',
        notes=(
            "Both presenters.",
            "Same real Command Line Tools dialog as the python3 check "
            "on a fresh Mac; already handled if that step ran first.",
            "Verified real answer on an already-set-up Mac: git version "
            "2.50.1 (Apple Git-155).",
        ),
    )),
    ("line", dict(
        label="Prompt",
        line='"I just created a GitHub account. Help me sign in to '
             'GitHub from this terminal."',
        notes=(
            "Both presenters. Create the account yourself first, at "
            "github.com.",
            "Codex offers to install GitHub's own CLI (gh) first; "
            "approve it. It then runs gh auth login, which opens a "
            "browser tab to finish signing in.",
            "If signup is refused (\"This email can't be used\" or "
            "\"We couldn't create your account\"), try another browser "
            "or network.",
        ),
    )),
    ("line", dict(
        label="Prompt",
        line='"Set my Git name to [your name] and my email to [your '
             'email], for every project on this computer."',
        notes=(
            "Both presenters.",
            "Real, captured for real with an isolated git config so "
            "the machine's own identity was never touched: "
            "git config --global user.name / user.email, confirmed "
            "with git config --global --get-regexp.",
        ),
    )),
    ("closing", dict(
        line="Thank you",
        notes=(),
    )),
]


def build() -> int:
    return kit.build_presentation(
        SLIDES, out_path=OUT,
        title="FIN1209 Special Lecture 1 - Set Up Codex, Git and GitHub",
        course=COURSE, author="Benjamin C. Sotelo",
    )


if __name__ == "__main__":
    count = build()
    print(f"{OUT}: {count} slides")
