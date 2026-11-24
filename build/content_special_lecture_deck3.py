"""Deck 3: build a simple stock tool with structured prompts, then view it.

Plain data, read by build_special_lecture_deck3.py. Presented by Benjamin
C. Sotelo for now; Denver to confirm (per the 25 Nov answer). Built only
from the firstmate home's data/fin1209-deck3-run/report.md and its
screens/ folder: a scout worker designed and actually ran this five-prompt
sequence twice from an empty folder, on a real machine, with no sign-in,
no repository, and no paid key, and recorded the real terminal transcripts
and two real browser screenshots that prove it. Nothing here is invented;
every terminal excerpt is copied verbatim from that worker's own
screens/terminal-*.txt, and the two screenshots are its own
screens/browser-04-*.png, genuine captures of the page the server actually
served.

Every "If it did not work" line is that worker's own account of what
actually went wrong running this twice, not a guess.

Neutral Metropolis visual style, not FEU's; see special_lecture_kit.py.
"""

from __future__ import annotations

import deckkit

SPEAKERS = (
    ("Benjamin C. Sotelo", "Lecturer, FIN1209"),
)

TITLE = deckkit.TitleSlide(
    course="FIN1209 - Technical Analysis in Investment",
    chapter="Special lecture 3 of 3",
    title="Build a Simple Stock Tool, Then View It",
    subtitle="Five prompts, one empty folder, no sign-in, no repository, no key",
    presenter="Benjamin C. Sotelo",
    notes=(
        "Presented by Benjamin C. Sotelo for now; Denver to confirm (25 "
        "Nov answer).",
        "Verified twice end to end by a scout worker before this deck was "
        "built: once finding and fixing one real problem, once clean as "
        "written, in about 6 minutes of Codex working time.",
        "Nothing here is staged; every terminal excerpt and both "
        "screenshots are genuine, from that worker's own run.",
    ),
)

INTRO = deckkit.Content(
    title="What we are building: Stock Desk Mini",
    lines=(
        "A tiny local web page: pick one of three market indexes, see six "
        "months of daily closes with 20 and 50-day averages, and read a "
        "live BUY, SELL, or HOLD from Chapter 8's rule.",
        "Only Python's own standard library and plain HTML, CSS and "
        "JavaScript; no pip install, no npm, no account, no API key.",
        "Verified twice, start to finish, in about 6 minutes of Codex "
        "working time; comfortably inside 30 minutes in class.",
    ),
    accent=("Prerequisite: python3 --version must already work with no "
            "popup; have that run once before class on a fresh Mac."),
)

SCOPE_NOTE = deckkit.Content(
    title="One decision worth a second look",
    lines=(
        "This tool offers three broad market indexes (S&P 500, Nasdaq "
        "Composite, Dow Jones) rather than individual stock tickers.",
        "Every individual-ticker source free enough to need no account "
        "either rate-limited or required solving a bot challenge; "
        "FRED's index series are confirmed free, keyless and public "
        "domain, so the tool uses those instead.",
        "Chapter 8's trend, RSI and five-bar rule apply identically to an "
        "index's closing price; nothing about the rule changes.",
    ),
    accent=("Real individual tickers would need a keyed data source "
            "instead; that is a scope change, not a fix, and is flagged "
            "here rather than decided alone."),
)

# Five prompts, typed one at a time into a single Codex session, waiting for
# each to finish before the next. term_lines in every step is a verbatim
# excerpt of that prompt's own real transcript (screens/terminal-0N-*.txt),
# trimmed to what fits a slide, never invented.
STEPS = [
    dict(
        title="Prompt 1: the plan, no code yet",
        do_lines=(
            "Goal: a short, checkable plan before any code exists, "
            "naming the real Chapter 8 rule rather than inventing one.",
        ),
        do_accent=('"Write a short PLAN.md ... no pip installs, no npm... '
                   'Trend is price versus the 50-day average, momentum is '
                   '14-day RSI versus 50, and the trigger is the day\'s '
                   'close breaking above the prior 5 trading days\' high '
                   'or below the prior 5 trading days\' low... Do not '
                   'write any code yet, only the plan."'),
        term_lines=(
            "codex",
            "Created PLAN.md with exact files, FRED data flow, chart",
            "requirements, and precise BUY/SELL/HOLD rules.",
            "No code written.",
        ),
        fallback=("if Codex writes code anyway, just say \"that was "
                 "supposed to be a plan only, please remove the code and "
                 "only write PLAN.md\"; it corrects itself. Did not "
                 "happen in either real run."),
    ),
    dict(
        title="Prompt 2: the data and the math, checked by eye",
        do_lines=(
            "Goal: the server logic working and checked on numbers a "
            "student can sanity-check themselves, before any page exists "
            "to hide a bug behind.",
        ),
        do_accent=('"Build server.py from the plan. Fetch the FRED CSV by '
                   'running the system curl command (not Python\'s '
                   'urllib, which hangs on this network)... run the data '
                   'function directly from the command line for the S&P '
                   '500... print the latest date, close, 20-day average, '
                   '50-day average, RSI, and reading."'),
        term_lines=(
            "Latest date: 2026-11-23",
            "Close: 7237.170000",
            "20-day average: 7477.251500",
            "50-day average: 7617.600200",
            "14-day RSI: 41.337146",
            "Reading: HOLD",
        ),
        fallback=("this is the one real failure across both runs: "
                 "Python's own urllib timed out fetching FRED on that "
                 "network every time, while curl on the same URL "
                 "succeeded instantly; the fix, now in the prompt above, "
                 "is to fetch with curl from the start."),
    ),
    dict(
        title="Prompt 3: the actual page",
        do_lines=(
            "Goal: turn the working server logic into something a "
            "student can look at and read a signal off of.",
        ),
        do_accent=('"Now build index.html, app.js, and style.css... a '
                   'dropdown for the three indexes, a chart of the daily '
                   'close with the 20-day and 50-day averages... and a '
                   'clear BUY, SELL, or HOLD reading in large text with '
                   'the three conditions shown as pass or fail under it. '
                   'Wire it to server.py\'s /api/prices endpoint."'),
        term_lines=(
            "codex",
            "Built the page with the index dropdown, three-color chart",
            "and legend, latest close/date, large reading, and",
            "BUY/SELL pass/fail conditions. Running at",
            "http://127.0.0.1:8765.",
        ),
        fallback=("did not fail in either run. If the page loads but the "
                 "chart is blank, the likely cause is the dropdown's "
                 "value not matching the server's three index keys "
                 "exactly; ask Codex to check the request URL."),
    ),
    dict(
        title="Prompt 4: start it",
        do_lines=(
            "Goal: the \"see it\" moment, on this computer and, if time "
            "allows, on a phone on the same Wi-Fi.",
        ),
        do_accent=('"Make server.py listen on all local network '
                   'addresses (0.0.0.0)... then tell me the exact command '
                   'to start it so it keeps running, the exact address to '
                   'open in a browser on this same Mac, and this Mac\'s '
                   'local Wi-Fi address so I can open the same page on my '
                   'phone."'),
        term_lines=(
            "codex",
            "Updated server.py to listen on 0.0.0.0. Verified it",
            "responds through localhost and 192.168.1.127.",
            "nohup python3 -u server.py --port 8000 > server.log &",
        ),
        fallback=("on the test machine, macOS reported Wi-Fi as \"off\" "
                 "even though the interface still carried an address; if "
                 "a phone cannot reach the page, check Wi-Fi is genuinely "
                 "on, both devices share the exact same network, and the "
                 "Mac's firewall is not blocking incoming connections."),
    ),
    dict(
        title="Prompt 5: one last check, across all three indexes",
        do_lines=(
            "Goal: a fast confidence check immediately before using the "
            "tool live in front of the class.",
        ),
        do_accent=('"Quickly check all three indexes once more by '
                   'requesting /api/prices for each from the running '
                   'server, and tell me in one line whether each one '
                   'returns a reading of BUY, SELL, or HOLD with no '
                   'errors."'),
        term_lines=(
            "codex",
            "S&P 500: HOLD; Nasdaq Composite: SELL; Dow Jones",
            "Industrial Average: HOLD -- all three endpoints",
            "returned HTTP 200 with no errors.",
        ),
        fallback=("did not fail in either run. If one index errors, it is "
                 "almost always FRED briefly rate-limiting a burst of "
                 "three requests; the server caches each result for 5 "
                 "minutes once it succeeds, so waiting a few seconds and "
                 "retrying that one index resolves it."),
    ),
]

VIEW_SHOTS = [
    dict(
        title="View it: a HOLD reading",
        image_file="browser-04-sp500-hold.png",
        credit=("S&P 500, the real page, real FRED data through Nov 23, "
               "2026: close below its 50-day average and RSI below 50, "
               "but the five-bar trigger has not fired either way, so "
               "the rule correctly withholds a signal rather than "
               "forcing one."),
    ),
    dict(
        title="View it: a SELL reading",
        image_file="browser-04-nasdaq-sell.png",
        credit=("Nasdaq Composite, the same real page: all three SELL "
               "conditions pass at once. A good second example to show "
               "in class, since it demonstrates both outcomes without "
               "waiting for the market to move."),
    ),
]

CLOSING = deckkit.Closing(
    title="Thank you",
    lines=(
        "Thank you for joining today's special lecture.",
        "Five prompts, one empty folder, no sign-in, no repository, no "
        "key: the same tools from set 1, used to build something real.",
        "Questions anytime, in class or after.",
    ),
)
