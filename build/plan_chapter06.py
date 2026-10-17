"""FIN1209 Chapter 6 run card, as plain data.

Three pages, the Chapter 2 shape: the clock, the cuts in order, and the
floor. See the docstring of build/plan_chapter02.py for why it is a run card
and not a teaching plan, and build/plan_chapter04.py for the lean deck's
version of it, which this one copies.

**This chapter does not fit one session, and the card says so.** Chapter 6
is 136 slides and 238 minutes at the calibrated rate, against a 180 minute
session. Chapter 4 fitted with time in hand; this chapter is the book's 36
pages with a picture beside every idea, and it does not. The card gives two
honest ways through it:

  * **One session**, with Cut 1 and Cut 2 taken before starting. Cut 1 is
    twenty slides that show, on one more chart, a point the slides around
    them have already made; Cut 2 is seven checks, each in a part that
    keeps at least one other. The chapter then costs 179 minutes.
  * **Two sessions**, uncut: stop at the end of Part 4 and carry Parts 5
    and 6 with the closing slides, 74 minutes, to the next session.

No check rests on a cut slide and no later slide refers back to one. The
floor on page 3 names every group of slides a kept check or a review
question rests on.

**The minutes are checked by the build.** CLOCK, LADDER, CUT_1_LATE and
CARRY below are the only places a minute is typed. build_plan6.py costs the
deck, and every cut slide by slide, at the weights in chapter-03/README.md
and refuses a card whose numbers disagree. A row may be rounded up or down
so the column adds up to the true total; build_plan6.py says why.

**No check answer is printed on this card.** The answers are instructor
material and live outside this public repository, in the answer sheet
build_chapter6.py writes to the home directory. The card points there.

Layout is build/notekit.py, which knows nothing about any chapter. This file
carries no layout and no typed slide numbers: slides are named by stable key
and build_plan6.py resolves them against the deck, so a content change moves
this card with it and a broken reference fails the build.
"""

from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table

SESSION = 180

# One row for the opening, one for each of the six parts, one for the
# closing: (label, slides, minutes uncut, minutes with Cuts 1 and 2).
CLOCK = (
    ("Title, objectives, roadmap", 3, 4, 4),
    ("1  Confirmation and divergence", 24, 43, 34),
    ("2  Timing, VWMA, climaxes", 23, 42, 30),
    ("3  Barriers and filtering", 17, 30, 23),
    ("4  Open interest and breadth", 26, 45, 34),
    ("5  Bar range and cycles", 20, 36, 23),
    ("6  Volume oscillators", 20, 35, 28),
    ("Closing", 3, 3, 3),
)

# The cuts, in the order to take them: (label, the slides, minutes bought).
LADDER = (
    ("1", ("slide:Our example: one uptrend, period by period", "fig:6.5",
           "fig:6.8", "fig:6.10", "fig:6.13", "chart:O", "fig:6.15",
           "chart:Q", "fig:6.21", "fig:6.23", "fig:6.26", "fig:6.28",
           "fig:6.29", "fig:6.31", "fig:6.32", "fig:6.34", "fig:6.36",
           "fig:6.37", "fig:6.40", "fig:6.43"), 39),
    ("2", ("check:1", "check:6", "check:8", "check:10", "check:12",
           "check:15", "check:18"), 20),
)

# What Cut 1 still buys when it is taken late: from this row of CLOCK on.
CUT_1_LATE_ROW = 3
CUT_1_LATE = 24

# The two session plan carries Parts 5 and 6 and the closing slides, uncut.
# Rows of CLOCK, and their minutes.
CARRY_ROWS = (5, 6, 7)
CARRY = 74

SLIDES = sum(row[1] for row in CLOCK)
FULL = sum(row[2] for row in CLOCK)
CUT = sum(row[3] for row in CLOCK)
OVER = FULL - SESSION
AFTER_1 = FULL - LADDER[0][2]
AFTER_2 = AFTER_1 - LADDER[1][2]
FIRST = FULL - CARRY


def _clock(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60:02d}"


def _clock_rows() -> tuple[tuple[str, ...], ...]:
    """The table on page 1. The start times are running sums of the rows."""
    rows = []
    start = start_cut = 0
    for label, slides, full, cut in CLOCK:
        rows.append((label, str(slides), str(full), _clock(start), str(cut),
                     _clock(start_cut)))
        start += full
        start_cut += cut
    rows.append(("Whole chapter", str(SLIDES), str(FULL),
                 f"ends {_clock(start)}", str(CUT),
                 f"ends {_clock(start_cut)}"))
    return tuple(rows)


# ==========================================================================
# Page 1 - the clock
# ==========================================================================

THE_CLOCK = Sheet(
    title="Where you should be, minute by minute",
    kicker="Read this before you open the deck",
    footer="The clock",
    blocks=(
        Prose(
            cue="The honest number",
            text=(
                f"Chapter 6 is {SLIDES} slides. At the pace you actually "
                f"taught Chapter 1, that is **about {FULL} minutes, and the "
                f"session is {SESSION}.** It is {OVER} minutes over. Better "
                "to know that now than at the 90 minute mark."
                "\n\n"
                "**Choose before you start.** One session: take Cut 1 and "
                f"Cut 2 from page 2 first, and the chapter runs {CUT}. Two "
                "sessions: teach Parts 1 to 4 uncut, then stop and carry "
                f"Parts 5 and 6 with the closing slides, {CARRY} minutes. "
                "The rate was measured on a deck with one thing on each "
                "slide, and this deck prices a picture and its idea as "
                "the two together, so treat the clock as the test."
            ),
        ),
        Table(
            cue="One session: the Cut columns",
            title="Minutes per part, and the clock time to start it",
            full=True,
            compact=False,
            headers=("Part", "Slides", "Full", "Start at", "Cut", "Start at"),
            align=("l", "n", "n", "n", "n", "n"),
            rows=_clock_rows(),
            note=(
                "Full is the deck with nothing dropped. Cut is the deck "
                "with Cuts 1 and 2 taken before you start. Slide counts "
                "include each check's question and its reveal. A row may "
                "be rounded up or down so the column adds up to the true "
                "total."
            ),
        ),
        Flag(
            kind="rule",
            cue="At every part boundary",
            title="Check the clock against the column you are running",
            text=(
                "**If you are more than five minutes behind at a part "
                "boundary, take whatever is left of Cut 1 before you begin "
                "the next part, not during it.** Taken from Part 3 on, it "
                f"still buys {CUT_1_LATE} minutes. If the session is two, "
                "stop at the end of Part 4, slide `{s:end:4}`. Page 3 has "
                "the detail."
            ),
        ),
    ),
)


# ==========================================================================
# Page 2 - the two cuts
# ==========================================================================

THE_CUTS = Sheet(
    title="What to cut, in this order",
    kicker="For one session, take both before you start",
    footer="Cuts 1 and 2",
    blocks=(
        Table(
            cue="The ladder",
            title="What each cut buys",
            compact=True,
            headers=("Cut", "What comes out", "Minutes", "Chapter runs"),
            align=("l", "l", "n", "n"),
            rows=(
                ("None", "The whole deck", "", str(FULL)),
                ("1", "Twenty second examples", str(LADDER[0][2]),
                 str(AFTER_1)),
                ("2", "Seven checks", str(LADDER[1][2]), str(AFTER_2)),
            ),
            note=(
                f"With both taken the chapter runs {AFTER_2} minutes in a "
                f"{SESSION} minute session. In two sessions take neither."
            ),
        ),
        Prose(
            cue="Cut 1",
            text=(
                "**Twenty slides that show, on one more chart, a point the "
                "slides around them have already made.** Each goes as a "
                "whole slide, idea and picture together. No check and no "
                "review question rests on any of them, and no later slide "
                "refers back to one. The students keep them in the student "
                "edition and the lecture notes."
            ),
        ),
        Bullets(
            cue="Skip these",
            title="Cut 1, twenty slides",
            items=(
                "Part 1: slides `{s:fig:6.5}`, Isis, and `{s:fig:6.8}`, "
                "both kinds on one chart; slide `{s:slide:Our example: one "
                "uptrend, period by period}`, which repeats Figure 6.6.",
                "Part 2: slides `{s:fig:6.10}`, silver breakouts, "
                "`{s:fig:6.13}`, blow-offs, `{s:chart:O}`, our two levels, "
                "`{s:fig:6.15}`, volatility, and `{s:chart:Q}`, our "
                "timeframes.",
                "Part 3: slides `{s:fig:6.21}`, the three-sigma filter on "
                "a real chart, and `{s:fig:6.23}`, the further channels.",
                "Part 4: slides `{s:fig:6.26}`, the bearish TRIN day, "
                "`{s:fig:6.28}`, 3M's traded range, and `{s:fig:6.29}`, "
                "the four steps on 3M. Slide `{s:chart:AG}` teaches the "
                "steps.",
                "Part 5: slides `{s:fig:6.31}`, `{s:fig:6.32}` and "
                "`{s:fig:6.34}`, three reversal bars on the dollar fund, "
                "and `{s:fig:6.36}` and `{s:fig:6.37}`, the EURUSD volume "
                "cycles. Keep `{s:fig:6.33}`: Check 15 names it.",
                "Part 6: slides `{s:fig:6.40}`, OBV on copper, and "
                "`{s:fig:6.43}`, the Chaikin pair.",
            ),
        ),
        Prose(
            cue="Cut 2",
            text=(
                "**Seven checks, each in a part that keeps at least one "
                "other.** Three minutes each, question and reveal together. "
                "The slides that answer them stay: they teach the chapter."
            ),
        ),
        Bullets(
            cue="Skip both slides",
            title="Cut 2, seven checks and their reveals",
            items=(
                "Check 1, slides `{s:check:1}` and `{s:reveal:1}`. Part 1 "
                "keeps Checks 2 and 3.",
                "Check 6, slides `{s:check:6}` and `{s:reveal:6}`. Part 2 "
                "keeps Checks 4 and 5.",
                "Check 8, slides `{s:check:8}` and `{s:reveal:8}`. Part 3 "
                "keeps Checks 7 and 9.",
                "Checks 10 and 12, slides `{s:check:10}`, `{s:reveal:10}`, "
                "`{s:check:12}` and `{s:reveal:12}`. Part 4 keeps Checks "
                "11 and 13.",
                "Check 15, slides `{s:check:15}` and `{s:reveal:15}`. Part "
                "5 keeps Checks 14 and 16.",
                "Check 18, slides `{s:check:18}` and `{s:reveal:18}`. Part "
                "6 keeps Checks 17 and 19.",
            ),
        ),
    ),
)


# ==========================================================================
# Page 3 - two sessions, and what is not on the table
# ==========================================================================

THE_FLOOR = Sheet(
    title="Two sessions, and the floor",
    kicker="Below this, do not go",
    footer="The carry, and what must stay",
    blocks=(
        Prose(
            cue="Two sessions",
            text=(
                "**To teach the chapter uncut, stop at the end of Part 4, "
                "slide `{s:end:4}`, and carry the rest.** Parts 5 and 6 "
                "start at slide `{s:part:5}`: bar range, volume cycles and "
                "the volume oscillators. Part 6 uses Part 1's two kinds of "
                "volume oscillator and Part 4's open interest, so it must "
                "come after them, never before."
                "\n\n"
                "Carry the three closing slides with them, slides "
                "`{s:slide:Chapter 6 in five sentences}` to `{s:slide:What "
                "the book uses, and where it says two things}`. The summary "
                "and the review questions cover all six parts. The first "
                f"session runs {FIRST} minutes and the carry {CARRY}."
            ),
        ),
        Prose(
            cue="The floor",
            text=(
                "Twelve groups of slides carry a kept check or one of the "
                "book's eight review questions. **They stay in at "
                f"{FULL} minutes and they stay in at {AFTER_2}.**"
            ),
        ),
        Bullets(
            cue="These stay",
            numbered=True,
            title="What must not be cut, and why",
            items=(
                "**Bullish and bearish volume**, slides "
                "`{s:term:Volume}` to `{s:slide:Volume that does not "
                "confirm the trend}`. Review question 2.",
                "**Divergence and confirmation**, slides `{s:term:Volume "
                "divergence and volume confirmation}` to `{s:slide:Not the "
                "divergence Chapters 4 and 5 drew}`. Check 2, review "
                "question 3.",
                "**The two kinds of oscillator**, slides `{s:term:Price-"
                "based and non-price-based volume oscillators}` to "
                "`{s:fig:6.7}`. Check 3.",
                "**Timing and climaxes**, slides `{s:part:2}`, "
                "`{s:term:Low volume breakout signal}`, `{s:slide:Tops and "
                "bottoms: volume at the extremes}` and `{s:slide:Where to "
                "set the overextension level}`. Checks 4 and 5, review "
                "question 4.",
                "**Barriers**, slides `{s:part:3}` and `{s:slide:What each "
                "of the five tells}`. Check 7.",
                "**Filtering**, slides `{s:slide:Filtering volume action: "
                "four ways}` to `{s:fig:6.22}`, except `{s:fig:6.21}`. "
                "Check 9, review question 5.",
                "**Relative volume and open interest**, slides `{s:part:4}`, "
                "`{s:term:Open interest}` and `{s:slide:Open interest is "
                "read like volume}`. Check 11, review questions 6 and 7.",
                "**Tick volume and two-dimensional volume**, slides "
                "`{s:term:Tick volume}`, `{s:term:Volume by price and "
                "volume by time}` and `{s:chart:AG}`. Check 13, review "
                "question 1.",
                "**The named bars**, slides `{s:term:Rest, reversal and "
                "continuation bars}` to `{s:slide:The rest bar and the "
                "continuation bar}`. Check 14.",
                "**Volume cycles and the time axis**, slides "
                "`{s:term:Intraday volume cycle}` and `{s:fig:6.38}`. "
                "Check 16, review question 8.",
                "**The OBV**, slides `{s:term:On Balance Volume, OBV}` and "
                "`{s:slide:The OBV: a disadvantage and a weakness}`. Check "
                "17.",
                "**The Chaikin pair and the Herrick index**, slides "
                "`{s:term:Chaikin Money Flow and Chaikin Oscillator}` and "
                "`{s:term:Herrick Payoff Index}`. Check 19.",
            ),
        ),
        Prose(
            cue="The answers",
            text=(
                "**This card prints no check answers, on purpose.** The "
                "repository this card lives in is public. The answers to "
                "all 19 checks, with the reason for each, are in your "
                "private answer sheet, which the deck build writes outside "
                "the repository:"
                "\n\n"
                "`~/FIN1209-Chapter-06-In-Class-Checks (answer sheet).md`"
            ),
        ),
    ),
)


# ==========================================================================

PLAN = Notes(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 6",
    title="Volume and Open Interest",
    presenter="Benjamin C. Sotelo, Institute of Accounts, Business and "
              "Finance, FEU Manila",
    doc_kind="run card",
    # One session or two, one run each. See plan_chapter02.py.
    plans=(),
    front=(THE_CLOCK, THE_CUTS, THE_FLOOR),
    parts=(),
    back=(),
)
