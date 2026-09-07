"""FIN1209 Chapter 4 run card, as plain data.

Three pages, the Chapter 2 shape: the clock, the cuts in order, and the
floor. See the docstring of build/plan_chapter02.py for why it is a run card
and not a teaching plan.

**This chapter fits, and the card says so.** Chapter 4 is the lean deck: 79
slides and 136 minutes at the calibrated rate, against a 180 minute session.
Chapters 2 and 3 were over the session and their cards name the cuts to take
before starting. This one names no cut to take before starting. It gives the
clock time each part should start at, the latest time each part can start
and still end on the hour uncut, and the cuts in order for a session that
runs slow.

It may run slow. The rate was measured on a deck with one thing on a slide.
Here an idea and its picture share a slide and are costed as the sum of the
two, and at the time of writing nobody has timed that in a room.

**The minutes are checked by the build.** CLOCK, LADDER and CARRY below are
the only places a minute is typed. build_plan4.py costs the deck, and every
cut slide by slide, at the weights in chapter-03/README.md and refuses a card
whose numbers disagree. The clock times and the totals in the prose are
computed from those same rows, here, so they cannot disagree with the table.

**No check answer is printed on this card.** The answers are instructor
material and live outside this public repository, in the answer sheet
build_chapter4.py writes to the home directory. The card points there.

Layout is build/notekit.py, which knows nothing about any chapter. This file
carries no layout and no typed slide numbers: slides are named by stable key
and build_plan4.py resolves them against the deck, so a content change moves
this card with it and a broken reference fails the build. A slide in this
deck is usually an idea with a picture beside it, and either name finds it:
`{s:slide:Its title}` and `{s:fig:4.18}` are the same slide.
"""

from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table

SESSION = 180

# One row for the opening, one for each of the book's nine sections, one for
# the closing: (label, slides, minutes uncut, minutes with Cuts 1 and 2).
CLOCK = (
    ("Title, objectives, roadmap", 3, 3, 3),
    ("4.1  Dow", 20, 35, 32),
    ("4.2  Chart patterns", 22, 39, 35),
    ("4.3  Volume", 7, 13, 11),
    ("4.4  Moving averages", 2, 4, 4),
    ("4.5  Divergence", 5, 9, 7),
    ("4.6  Sentiment", 5, 8, 8),
    ("4.7  Sakata", 5, 9, 9),
    ("4.8  Elliott", 2, 4, 2),
    ("4.9  Cycles", 5, 9, 7),
    ("Closing", 3, 3, 3),
)

# The cuts, in the order to take them: (label, the slides, minutes bought).
LADDER = (
    ("1", ("fig:4.14", "fig:4.18", "fig:4.23", "fig:4.29", "fig:4.32"), 9),
    ("2", ("check:2", "check:6"), 6),
)

# What Cut 1 still buys when it is taken late: from this row of CLOCK on.
CUT_1_LATE_ROW = 3
CUT_1_LATE = 8

# The last resort is a stop and not a cut: sections 4.7 to 4.9 and the
# closing slides move to the next session. Rows of CLOCK, and their minutes.
CARRY_ROWS = (7, 8, 9, 10)
CARRY = 25

SLIDES = sum(row[1] for row in CLOCK)
FULL = sum(row[2] for row in CLOCK)
CUT = sum(row[3] for row in CLOCK)
SPARE = SESSION - FULL
AFTER_1 = FULL - LADDER[0][2]
AFTER_2 = AFTER_1 - LADDER[1][2]


def _clock(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60:02d}"


def _clock_rows() -> tuple[tuple[str, ...], ...]:
    """The table on page 1. The start times are running sums of the rows."""
    rows = []
    start = 0
    for label, slides, full, cut in CLOCK:
        rows.append((label, str(slides), str(full), _clock(start),
                     _clock(start + SPARE), str(cut)))
        start += full
    rows.append(("Whole chapter", str(SLIDES), str(FULL),
                 f"ends {_clock(start)}", f"ends {_clock(start + SPARE)}",
                 str(CUT)))
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
                f"Chapter 4 is {SLIDES} slides. At the pace you actually "
                f"taught Chapter 1, that is **about {FULL} minutes, and the "
                f"session is {SESSION}.** It fits, with {SPARE} minutes in "
                "hand, and nothing has to come out before you start."
                "\n\n"
                "One caution. The rate was measured on a deck with one thing "
                "on each slide. This deck puts a picture beside every idea "
                "and prices the slide as the two together, and that has not "
                "been timed in a room. **So the clock below is the test, and "
                "the cuts are here in case it runs slow.**"
            ),
        ),
        Table(
            cue="The clock columns",
            title="Minutes per part, and the clock time to start it",
            full=True,
            compact=False,
            headers=("Part", "Slides", "Full", "Start at", "Latest start",
                     "Cut"),
            align=("l", "n", "n", "n", "n", "n"),
            rows=_clock_rows(),
            note=(
                "Full is the deck with nothing dropped. Latest start is "
                f"{SPARE} minutes after Start at: begin a part later than "
                f"that and the uncut deck ends past {_clock(SESSION)}. Cut "
                "is the part with Cuts 1 and 2 taken. Slide counts include "
                "each check's question and its reveal."
            ),
        ),
        Flag(
            kind="rule",
            cue="At every part boundary",
            title="Check the clock against Latest start",
            text=(
                "**If you begin a part after its Latest start, take Cut 1 "
                "before you begin it, not during it.** It still buys "
                f"{CUT_1_LATE} minutes at the start of 4.3. Cut 2 is for a "
                "session that starts late: its two checks are in 4.1 and "
                "4.2. If neither is enough, stop at the end of 4.6, slide "
                "`{s:end:6}`, and carry the rest. Page 3 has the detail."
            ),
        ),
    ),
)


# ==========================================================================
# Page 2 - the two cuts
# ==========================================================================

THE_CUTS = Sheet(
    title="What to cut, in this order",
    kicker="Only if the clock is against you",
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
                ("1", "Five second examples", str(LADDER[0][2]),
                 str(AFTER_1)),
                ("2", "Two checks", str(LADDER[1][2]), str(AFTER_2)),
            ),
            note=(
                f"None of this is needed in a {SESSION} minute session that "
                "runs to the rate. The last resort is on page 3 and is a "
                "stop, not a cut."
            ),
        ),
        Prose(
            cue="Cut 1",
            text=(
                "**Five slides that show, on one more chart, a point the "
                "slides around them have already made.** In this deck a "
                "picture sits beside its idea, so each of these goes as a "
                "whole slide, idea and picture together. No check and no "
                "review question rests on any of them, and no later slide "
                "refers back to one."
            ),
        ),
        Bullets(
            cue="Skip these",
            title="Cut 1, five slides",
            items=(
                "Slide `{s:fig:4.14}`, Figure 4.14, the rounding bottom as "
                "continuation. Figure 4.13 on slide `{s:fig:4.13}` is the "
                "same point on a triangle.",
                "Slide `{s:fig:4.18}`, Figure 4.18, volume and phase on a "
                "real chart. The three schematics before it, slides "
                "`{s:fig:4.15}` to `{s:fig:4.17}`, teach every line of it.",
                "Slide `{s:fig:4.23}`, Figure 4.23, bullish divergence in an "
                "accumulation. Slides `{s:fig:4.22}` and `{s:fig:4.24}` "
                "carry the section and the check.",
                "Slide `{s:fig:4.29}`, Figure 4.29, the wave count on gold. "
                "Slide `{s:fig:4.28}` teaches the waves and the phases.",
                "Slide `{s:fig:4.32}`, Figure 4.32, the triangle in a price "
                "channel. Slide `{s:fig:4.31}` shows its three roles on a "
                "cycle.",
            ),
        ),
        Prose(
            cue="Cut 2",
            text=(
                "**Two checks, and only these two.** Each sits in a part "
                "that has three, so 4.1 and 4.2 still read the room twice "
                "each. Three minutes each. The slides that answer them stay: "
                "they carry review questions."
            ),
        ),
        Bullets(
            cue="Skip both slides",
            title="Cut 2, two checks and their reveals",
            items=(
                "Check 2, slides `{s:check:2}` and `{s:reveal:2}`, reading a "
                "consolidation. Checks 1 and 3 read the room in 4.1.",
                "Check 6, slides `{s:check:6}` and `{s:reveal:6}`, reversals "
                "and neutral patterns. Checks 4 and 5 read the room in 4.2.",
            ),
        ),
        Flag(
            kind="trap",
            cue="Never",
            title="Three things that are never a cut",
            text=(
                "**Never drop a reveal without its question, or a question "
                "without its reveal.** The letter alone teaches nothing."
                "\n\n"
                "**Never drop a check in 4.3 to 4.9.** Each of those parts "
                "has one check or shares one with its neighbour, and it is "
                "the only reading of the room there."
                "\n\n"
                "**Never skip the first slide of a part.** There are no "
                "divider slides: the first slide carries the book's section "
                "number and is how the room knows a part has started."
            ),
        ),
    ),
)


# ==========================================================================
# Page 3 - the last resort, and what is not on the table
# ==========================================================================

THE_FLOOR = Sheet(
    title="The last resort, and the floor",
    kicker="Below this, do not go",
    footer="The carry, and what must stay",
    blocks=(
        Prose(
            cue="The carry",
            text=(
                "**If Cuts 1 and 2 are not enough, stop at a part boundary "
                "and carry the rest.** The clean stop is the end of 4.6, "
                "slide `{s:end:6}`. Sections 4.7, 4.8 and 4.9 start at slide "
                "`{s:part:7}`: Sakata, Elliott and cycles. They use what 4.1 "
                "and 4.2 taught, and nothing before them needs them."
                "\n\n"
                "Carry the three closing slides with them, slides "
                "`{s:slide:Chapter 4 in five sentences}` to `{s:slide:What "
                "this chapter uses and does not teach}`. The summary and the "
                "review questions cover all nine sections, so they belong to "
                f"the session that finishes the chapter. That is {CARRY} "
                "minutes moved, uncut."
            ),
        ),
        Prose(
            cue="The floor",
            text=(
                "Seven groups of slides carry a check or one of the book's "
                "review questions. **They stay in at "
                f"{FULL} minutes and they stay in at {AFTER_2}.**"
            ),
        ),
        Bullets(
            cue="These stay",
            numbered=True,
            title="What must not be cut, and why",
            items=(
                "**The two consolidations and who is on each side**, slides "
                "`{s:term:Consolidation phase}` to `{s:slide:Distribution: "
                "the same story upside down}`. Check 1, and review question "
                "1.",
                "**Tops, bottoms and the signs**, slides `{s:slide:Why tops "
                "are shorter and rougher than bottoms}` to `{s:slide:The "
                "signs of a distribution}`. Check 2, and review question 4.",
                "**When a consolidation is over**, slides `{s:slide:When is "
                "a consolidation over?}` and `{s:term:Minimum measuring "
                "objective}`. Check 3.",
                "**Consolidation patterns and intrinsic bias**, slides "
                "`{s:term:Consolidation pattern}` to `{s:slide:"
                "Intrinsically neutral patterns}`. Check 4, and review "
                "questions 2 and 3.",
                "**Extrinsic bias, agreement and disagreement**, slides "
                "`{s:term:Extrinsic bias}`, `{s:slide:When the biases "
                "agree}`, `{s:slide:Continuation patterns agree with the "
                "trend}`, `{s:slide:Reversal patterns disagree with the "
                "trend}` and `{s:slide:Neutral patterns borrow their "
                "bias}`. Checks 5 and 6.",
                "**What each tool says about phase**, slides `{s:slide:A "
                "trend that loses volume is running out}`, `{s:slide:Open "
                "interest: watch for disagreement}`, `{s:fig:4.21}`, "
                "`{s:fig:4.22}`, `{s:fig:4.24}`, `{s:chart:Q}` and "
                "`{s:fig:4.25}`. Checks 7, 8 and 9, and review questions 5, "
                "6 and 8.",
                "**Sakata, Elliott and the cycle**, slides `{s:slide:The "
                "five methods, by name}`, `{s:fig:4.28}` and `{s:fig:4.30}`. "
                "Checks 10 and 11, and review question 7.",
            ),
        ),
        Prose(
            cue="The answers",
            text=(
                "**This card prints no check answers, on purpose.** The "
                "repository this card lives in is public. The answers to "
                "all 11 checks, with the reason for each, are in your "
                "private answer sheet, which the deck build writes outside "
                "the repository:"
                "\n\n"
                "`~/FIN1209-Chapter-04-In-Class-Checks (answer sheet).md`"
                "\n\n"
                "Print that if you want the answers in your hand. This card "
                "is for the clock."
            ),
        ),
    ),
)


# ==========================================================================

PLAN = Notes(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 4",
    title="Market Phase Analysis",
    presenter="Benjamin C. Sotelo, Institute of Accounts, Business and "
              "Finance, FEU Manila",
    doc_kind="run card",
    # One session, one run. See plan_chapter02.py.
    plans=(),
    front=(THE_CLOCK, THE_CUTS, THE_FLOOR),
    parts=(),
    back=(),
)
