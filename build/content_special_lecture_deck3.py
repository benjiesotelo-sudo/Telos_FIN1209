"""Deck 3: build a simple stock tool with structured prompts, then view it.

Plain data, read by build_special_lecture_deck3.py. Presented by Benjamin
C. Sotelo for now; Denver to confirm (per the 25 Nov answer). Built only
from the firstmate home's data/fin1209-deck3-run/report.md and its
screens/ folder: a scout worker designed and actually ran this five-prompt
sequence twice from an empty folder, on a real machine, with no sign-in,
no repository, and no paid key, and recorded the real terminal transcripts
and two real browser screenshots that prove it. Nothing here is invented;
every terminal excerpt is copied verbatim from that worker's own
screens/terminal-*.txt, and the screenshots are its own genuine captures
of the page the server actually served.

Every "If it did not work" line is that worker's own account of what
actually went wrong running this twice, not a guess.

Each prompt is shown in full, never truncated (his own fix, 25 Nov: a
student cannot type a truncated prompt): one slide for the exact words to
type, a second for the real result. The same full text is also written,
verbatim, to data/fin1209-special-lecture/deck3-prompts.txt by the build
script, as a handout he can share.

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
        "Nothing here is staged; every terminal excerpt and every "
        "screenshot is genuine, from that worker's own run.",
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
            "popup; have that run once before class on a fresh Mac (deck "
            "1 now has this same step, next to the Git check)."),
)

# Rewritten per his 25 Nov fix: say the decision plainly, no internal
# "flagged rather than decided" framing; he already decided (indexes as
# the main path, one stock as the bonus).
SCOPE_NOTE = deckkit.Content(
    title="Why indexes, with one stock as a bonus",
    lines=(
        "This tool's main path is three broad market indexes (S&P 500, "
        "Nasdaq Composite, Dow Jones): free, no account, no key, and "
        "reliable, every time this was tested.",
        "Chapter 8's trend, RSI and five-bar rule apply identically to an "
        "index's closing price; nothing about the rule changes.",
        "A bonus prompt at the end lets you load one individual stock "
        "instead, such as NVDA, the same way; it can be slower to answer "
        "with a whole class on one network, so it is optional.",
    ),
    accent=("The three indexes always work. The bonus stock is a nice "
            "extra, not something to depend on in front of the class."),
)

# Six prompts in all (five required, one optional bonus), each now a pair
# of slides: the exact words to type, in full, never truncated (his own
# 25 Nov fix), then the real result. prompt_text is copied verbatim from
# that prompt's own report; term_lines, where present, is a verbatim
# excerpt of the real transcript (screens/terminal-0N-*.txt or
# terminal-bonus-codex.txt), trimmed to what fits the result slide, never
# invented. image_file, where present, is a real screenshot instead of a
# generated terminal mockup.
PROMPTS = [
    dict(
        number=1,
        title="Prompt 1: the plan, no code yet",
        goal=("Goal: a short, checkable plan before any code exists, "
              "naming the real Chapter 8 rule rather than inventing one."),
        prompt_text=(
            "Write a short PLAN.md in this empty folder for a tiny local "
            "web app called Stock Desk Mini. Rules: only Python 3 "
            "standard library, no pip installs, no npm, no other "
            "packages. One web page: pick one of three indexes (S&P 500, "
            "Nasdaq Composite, Dow Jones Industrial Average), see a line "
            "chart of its last 6 months of daily closing prices with its "
            "20-day and 50-day moving averages, and one reading of BUY, "
            "SELL, or HOLD. Trend is price versus the 50-day average, "
            "momentum is 14-day RSI versus 50, and the trigger is the "
            "day's close breaking above the prior 5 trading days' high or "
            "below the prior 5 trading days' low. Data must be free, need "
            "no account and no API key: use the FRED fredgraph.csv "
            "endpoint, for example https://fred.stlouisfed.org/graph/"
            "fredgraph.csv?id=SP500 for the S&P 500, id=NASDAQCOM for "
            "Nasdaq, id=DJIA for Dow. A browser page cannot fetch that "
            "URL directly, so a small Python server must fetch the CSV "
            "itself and hand the page JSON. List the exact files you "
            "will create and how the BUY, SELL, HOLD reading is "
            "computed. Do not write any code yet, only the plan."
        ),
        term_lines=(
            "codex",
            "Created PLAN.md with exact files, FRED data flow, chart",
            "requirements, and precise BUY/SELL/HOLD rules.",
            "No code written.",
        ),
        fallback=("if Codex writes code anyway, just say \"that was "
                 "supposed to be a plan only, please remove the code and "
                 "only write PLAN.md\" and it will remove the code."),
        notes=("Verified twice, start to finish: Codex did not write code "
              "early in either real run.",),
    ),
    dict(
        number=2,
        title="Prompt 2: the data and the math, checked by eye",
        goal=("Goal: the server logic working and checked on numbers a "
              "student can sanity-check themselves, before any page "
              "exists to hide a bug behind."),
        prompt_text=(
            "Build server.py from the plan. Fetch the FRED CSV by "
            "running the system curl command (not Python's urllib, "
            "which hangs on this network) with a 15 second timeout, and "
            "raise a clear error if curl is missing or fails. Compute "
            "the 20-day and 50-day moving averages, the 14-day RSI, and "
            "the BUY, SELL, or HOLD reading. Before building anything "
            "else, run the data function directly from the command line "
            "for the S&P 500, with up to 3 retries if the network call "
            "fails, and print the latest date, close, 20-day average, "
            "50-day average, RSI, and reading so I can check the math by "
            "eye."
        ),
        term_lines=(
            "Latest date: 2026-11-23",
            "Close: 7237.170000",
            "20-day average: 7477.251500",
            "50-day average: 7617.600200",
            "14-day RSI: 41.337146",
            "Reading: HOLD",
        ),
        fallback=("if Codex seems stuck and never prints the readout, "
                 "the fetch may be hanging; say \"use curl instead of "
                 "urllib to fetch the data\" and it will recover."),
        notes=("The one real failure across both verification runs: "
              "Python's own urllib timed out fetching FRED on that "
              "network every time, while curl on the same URL succeeded "
              "instantly; the fix is now in the prompt text itself, so "
              "this should not come up, but the recovery line is there "
              "if it does.",),
    ),
    dict(
        number=3,
        title="Prompt 3: the actual page",
        goal=("Goal: turn the working server logic into something a "
              "student can look at and read a signal off of."),
        prompt_text=(
            "Now build index.html, app.js, and style.css so the page is "
            "actually usable: a dropdown for the three indexes, a chart "
            "of the daily close with the 20-day and 50-day averages "
            "drawn on top in different colors with a small legend, the "
            "latest close and date, and a clear BUY, SELL, or HOLD "
            "reading in large text with the three conditions (trend, "
            "momentum, trigger) shown as pass or fail under it. Wire it "
            "to server.py's /api/prices endpoint. Keep it on one page, "
            "plain HTML, CSS, and JavaScript, no build step, no "
            "frameworks."
        ),
        term_lines=(
            "codex",
            "Built the page with the index dropdown, three-color chart",
            "and legend, latest close/date, large reading, and",
            "BUY/SELL pass/fail conditions. Running at",
            "http://127.0.0.1:8765.",
        ),
        fallback=("if the page loads but the chart is blank, ask Codex "
                 "to check that the dropdown's value matches the "
                 "server's three index keys exactly."),
        notes=("Did not fail in either verification run.",),
    ),
    dict(
        number=4,
        title="Prompt 4: start it",
        goal=("Goal: the \"see it\" moment, on this computer and, if "
              "time allows, on a phone on the same Wi-Fi."),
        prompt_text=(
            "Make server.py listen on all local network addresses "
            "(0.0.0.0), not only this Mac, then tell me the exact "
            "command to start it so it keeps running, the exact address "
            "to open in a browser on this same Mac, and this Mac's "
            "local Wi-Fi address so I can open the same page on my "
            "phone on the same Wi-Fi."
        ),
        term_lines=(
            "codex",
            "Updated server.py to listen on 0.0.0.0. Verified it",
            "responds through localhost and 192.168.x.x.",
            "nohup python3 -u server.py --port 8000 > server.log &",
        ),
        fallback=("if a phone cannot reach the page, check that Wi-Fi is "
                 "genuinely turned on (not just an Ethernet connection), "
                 "that both devices are on the exact same network, and "
                 "that the Mac's firewall is not blocking incoming "
                 "connections."),
        notes=("On the machine this was verified on, macOS reported "
              "Wi-Fi as \"off\" even though the interface still carried "
              "an address; a classroom Mac mini should not have this "
              "problem, but it is worth a quick glance at System "
              "Settings beforehand.",),
    ),
    dict(
        number=5,
        title="Prompt 5: one last check, across all three indexes",
        goal=("Goal: a fast confidence check immediately before using "
              "the tool live in front of the class."),
        prompt_text=(
            "Quickly check all three indexes once more by requesting "
            "/api/prices for each from the running server, and tell me "
            "in one line whether each one returns a reading of BUY, "
            "SELL, or HOLD with no errors."
        ),
        term_lines=(
            "codex",
            "S&P 500: HOLD; Nasdaq Composite: SELL; Dow Jones",
            "Industrial Average: HOLD -- all three endpoints",
            "returned HTTP 200 with no errors.",
        ),
        fallback=("if one index errors, wait a few seconds and ask Codex "
                 "to retry just that one; it is almost always FRED "
                 "briefly rate-limiting a burst of three requests, and "
                 "the server caches each result for 5 minutes once it "
                 "succeeds."),
        notes=("Did not fail in either verification run.",),
    ),
]

# A sixth, optional prompt, added after his 25 Nov decision to keep both
# data paths: FRED's three indexes stay the required main path; a single
# stock ticker via an external source becomes this one bonus prompt at
# the end. Built from data/fin1209-deck3-bonus/report.md: verified for
# real, twice over, against a copy of the finished Stock Desk Mini. The
# one real screenshot that exists shows the safe rate-limit fallback, not
# a chart; both outcomes are genuine, live responses, not simulated.
BONUS = dict(
    number=6,
    title="Bonus, optional: one stock ticker",
    goal=("Optional, after the five required prompts above, which "
          "already stand on their own: type any single stock ticker, "
          "like NVDA, instead of picking an index."),
    prompt_text=(
        "Add one more data option to Stock Desk Mini, as a bonus "
        "alongside the three indexes: let the student type a single "
        "stock ticker (for example NVDA) and load it the same way. "
        "Fetch the ticker's last 6 months of daily closes from Yahoo "
        "Finance's chart JSON endpoint using the same curl-based "
        "approach as the FRED fetch, for example https://query1."
        "finance.yahoo.com/v8/finance/chart/NVDA?range=6mo&interval=1d. "
        "Yahoo's chart endpoint returns 429 Too Many Requests for a "
        "request sent with no User-Agent header, but returns 200 for "
        "the exact same request sent with an ordinary desktop browser "
        "User-Agent string, so send one. Parse the JSON into the same "
        "daily close series the index path already uses, and compute "
        "the same 20-day and 50-day moving averages, 14-day RSI, and "
        "BUY/SELL/HOLD reading for it, exactly as for the indexes. Add "
        "a small text box on the page where the student can type a "
        "ticker, with a button to load it, next to the existing index "
        "dropdown. If Yahoo still answers 429 even with the browser "
        "User-Agent, show the message \"too many requests, wait a "
        "minute and retry\" on the page instead of a stack trace or raw "
        "error. Keep everything to the Python standard library, no pip "
        "installs, no npm, no other packages."
    ),
    image_file="browser-bonus-nvda-429.png",
    fallback=('with a whole class on one network, you may see exactly '
             'this message instead of a chart: "too many requests, wait '
             'a minute and retry," with a Try again button. Test this '
             'once well before class; if it fires during the lecture, '
             'expect to wait a few minutes, not one, before trying '
             'again. None of the five required prompts depend on this '
             'working.'),
    notes=(
        "Added after his 25 Nov decision to keep both data paths: FRED's "
        "three indexes stay the required main path; this is one optional "
        "bonus prompt at the end.",
        "Verified live, twice over, against a copy of the finished Stock "
        "Desk Mini: the ticker returned a real BUY reading with its own "
        "three-line chart once, early in the same session, before this "
        "network started answering 429 for the rest of it; those "
        "retries took longer than a minute to clear, up to 13 minutes. "
        "No screenshot of that chart exists, since the rate limit was "
        "already in effect by the time of the dedicated screenshot "
        "attempt; the pictured state is the other real, verified "
        "outcome, not a failure.",
        "Source: data/fin1209-deck3-bonus/report.md.",
    ),
)

VIEW_SHOTS = [
    dict(
        title="View it: a HOLD reading",
        image_file="browser-04-sp500-hold.png",
        credit="S&P 500, the real page, real FRED data through Nov 23, 2026.",
        notes=(
            "Close below its 50-day average and RSI below 50, but the "
            "five-bar trigger has not fired either way, so the rule "
            "correctly withholds a signal rather than forcing one.",
        ),
    ),
    dict(
        title="View it: a SELL reading",
        image_file="browser-04-nasdaq-sell.png",
        credit="Nasdaq Composite, the same real page: all three SELL conditions pass.",
        notes=(
            "A good second example to show in class, since it "
            "demonstrates both outcomes without waiting for the market "
            "to move.",
        ),
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
