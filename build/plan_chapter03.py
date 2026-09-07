"""FIN1209 Chapter 3 run card, as plain data.

Three pages, the Chapter 2 shape: the clock, the cuts in order, and the
floor. See the docstring of build/plan_chapter02.py for why it is a run card
and not a teaching plan.

**The minutes are calibrated, not estimated.** Chapter 1's front matter plus
its first four parts is 155 slides, and that is what 180 minutes bought in
the room on 2026-09-02. Every minute figure below is Chapter 3's own slide
mix costed at that rate. The rate is written down in chapter-03/README.md
for the first time, with the check that it reproduces Chapter 2's card to
the minute.

Chapter 3 is heavier than Chapter 2: forty figures instead of twenty six. It
costs 219 minutes uncut, and it reaches 180 only with all three cuts taken
before the session. The card says so on its first page and offers the one
clean alternative, which is to run Parts 1 to 5 uncut and carry Part 6.

Layout is build/notekit.py, which knows nothing about any chapter. This file
carries no layout and no typed slide numbers: slides are named by stable key
and build_plan3.py resolves them against the deck, so a content change moves
this card with it and a broken reference fails the build.
"""

from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table


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
                "Chapter 3 is 188 slides. At the pace you actually taught "
                "Chapter 1, that is **about 219 minutes, and the session is "
                "180.** It is heavier than Chapter 2, mostly because the book "
                "gives this chapter forty figures, and it does not fit as it "
                "stands."
                "\n\n"
                "The rate is measured, not guessed: 155 slides of Chapter 1 "
                "is what 180 minutes bought. Every minute below is Chapter "
                "3's own mix of slides priced at that rate."
            ),
        ),
        Table(
            cue="Read the last two columns",
            title="Minutes per part, and the clock time to start it",
            full=True,
            compact=False,
            headers=("Part", "Slides", "Full", "Start at", "Cut", "Start at"),
            align=("l", "n", "n", "n", "n", "n"),
            rows=(
                ("Openers and roadmap", "4", "5", "0:00", "5", "0:00"),
                ("1  OHLC", "26", "30", "0:05", "25", "0:05"),
                ("2  Significance and gaps", "22", "26", "0:35", "21", "0:30"),
                ("3  Constant measures", "38", "45", "1:01", "38", "0:51"),
                ("4  Scaling", "29", "32", "1:46", "24", "1:29"),
                ("5  Bid-ask spread", "22", "26", "2:18", "22", "1:53"),
                ("6  Futures", "43", "50", "2:44", "39", "2:15"),
                ("Wrap up", "4", "5", "3:34", "5", "2:54"),
                ("Whole chapter", "188", "219", "ends 3:39", "179",
                 "ends 2:59"),
            ),
            note=(
                "Full is the deck with nothing dropped. Cut is the same deck "
                "with Cuts 1, 2 and 3 from pages 2 and 3 all taken before "
                "you start. Slide counts run from the part divider to the "
                "recap, which is what the progress marker counts."
            ),
        ),
        Flag(
            kind="rule",
            cue="At every part boundary",
            title="Check the clock against the column you are running",
            text=(
                "If you are more than five minutes late starting a part on "
                "the Cut column, you have no cut left to take. **Stop at the "
                "end of Part 5 and carry Part 6.** Do not cut inside a part; "
                "that is how a session ends in the middle of an argument."
            ),
        ),
        Prose(
            cue="The other way to run it",
            text=(
                "**Parts 1 to 5 uncut, with the openers and the wrap up, are "
                "169 minutes.** If you would rather keep every figure, chart "
                "and check, run those and carry Part 6 whole to the next "
                "session. Part 6 is futures, and it is the one part that is "
                "self contained: nothing in Parts 1 to 5 depends on it."
                " **Either way, run the four wrap up slides at the end.** "
                "They carry the eight review questions."
            ),
        ),
    ),
)


# ==========================================================================
# Page 2 - the first two cuts
# ==========================================================================

THE_CUTS = Sheet(
    title="What to cut, in this order",
    kicker="Take all three before you start",
    footer="Cuts 1 and 2",
    blocks=(
        Table(
            cue="The ladder",
            title="What each cut buys",
            compact=True,
            headers=("Cut", "What comes out", "Minutes", "Chapter runs"),
            align=("l", "l", "n", "n"),
            rows=(
                ("None", "The whole deck", "", "219"),
                ("1", "Eleven repeat pictures", "10", "209"),
                ("2", "All six charts, and eight slides", "12", "197"),
                ("3", "Six checks", "18", "179"),
            ),
            note=(
                "In a 180 minute session all three come out before you "
                "start. Cut 3 is on page 3, with what must never go."
            ),
        ),
        Prose(
            cue="Cut 1",
            text=(
                "**Eleven pictures that repeat a picture or a slide you have "
                "already shown.** Nothing is lost but the second telling. "
                "Each one is under a minute."
            ),
        ),
        Bullets(
            cue="Skip these",
            title="Cut 1, eleven figures",
            items=(
                "Slide `{s:fig:3.3}`, Figure 3.3. Eight intervals; Figure 3.2 "
                "already builds a bar.",
                "Slide `{s:fig:3.13}`, Figure 3.13. Figure 3.15 shows a "
                "Renko chart too.",
                "Slides `{s:fig:3.17}` and `{s:fig:3.23}`, Figures 3.17 and "
                "3.23. Figure 3.18 and the overlay slide make both points.",
                "Slides `{s:fig:3.20}` and `{s:fig:3.21}`, Figures 3.20 and "
                "3.21. Figures 3.19 and 3.22 carry each pair.",
                "Slide `{s:fig:3.30}`, Figure 3.30. The slide before it "
                "carries the point.",
                "Slide `{s:fig:3.34}`, Figure 3.34. Simple contango is on "
                "the slide before it.",
                "Slides `{s:fig:3.36}` and `{s:fig:3.37}`, Figures 3.36 and "
                "3.37. The natural gas slide says it.",
                "Slide `{s:fig:3.39}`, Figure 3.39. Figure 3.40 shows the "
                "mechanism already.",
            ),
        ),
        Prose(
            cue="Cut 2",
            text=(
                "**Every chart, and eight slides that restate their "
                "neighbour or name something the chapter never examines.** "
                "No check needs any of them. The charts are ours and only "
                "illustrate a term already taught."
            ),
        ),
        Bullets(
            cue="Skip these too",
            title="Cut 2, six charts and eight slides",
            items=(
                "All six charts: slides `{s:chart:A}`, `{s:chart:B}`, "
                "`{s:chart:C}`, `{s:chart:D}`, `{s:chart:E}` and "
                "`{s:chart:F}`.",
                "Slide `{s:slide:Four families of technical data}`, the "
                "data families. The notes carry the full list.",
                "Slide `{s:slide:Four market gaps, named for later}`, the "
                "Chapter 5 gap names.",
                "Slide `{s:slide:Why constant time is the default}`, "
                "overlays. Part 4 teaches them again.",
                "Slide `{s:slide:Which one each chart holds constant}`, the "
                "summary. Every line is on a term slide.",
                "Slide `{s:slide:Three ways to scale a price axis}`, the "
                "list. The three terms follow it.",
                "Slide `{s:slide:Read volume on a continuous chart}`, "
                "continuous volume. The notes carry it.",
                "Slide `{s:slide:Next month, back months, and the month "
                "codes}`, month codes. Nothing is set on them.",
                "Slide `{s:slide:Which chart for which job}`, the summary. "
                "The three terms carry it.",
            ),
        ),
    ),
)


# ==========================================================================
# Page 3 - the third cut, and what is not on the table
# ==========================================================================

THE_FLOOR = Sheet(
    title="The third cut, and the floor",
    kicker="Below this, do not go",
    footer="Cut 3, and what must stay",
    blocks=(
        Prose(
            cue="Cut 3",
            text=(
                "**Six checks, and only these six.** Each sits beside another "
                "check in the same part, every part keeps at least two, and "
                "the seventeen left still put a check after every few terms. "
                "Three minutes each."
            ),
        ),
        Bullets(
            cue="Skip both slides",
            title="Cut 3, six checks and their reveals",
            items=(
                "Check 1, slide `{s:check:1}`, chartists. Check 2 in Part 1 "
                "reads the room.",
                "Check 6, slide `{s:check:6}`, what gaps do. Check 5 sets the "
                "gap types.",
                "Check 11, slide `{s:check:11}`, the constant measure. Checks "
                "7 to 10 set each chart.",
                "Check 13, slide `{s:check:13}`, choosing a scale. Check 12 "
                "sets the two scales.",
                "Check 17, slide `{s:check:17}`, buying at support. Check 16 "
                "sets the fill problems.",
                "Check 21, slide `{s:check:21}`, convergence. Check 20 sets "
                "contango and backwardation.",
            ),
        ),
        Flag(
            kind="trap",
            cue="Never",
            title="Two things that are never a cut",
            text=(
                "**Never drop a reveal without its question, or a question "
                "without its reveal.** The letter alone teaches nothing."
                "\n\n"
                "**Never drop a term slide.** Every check is answered by a "
                "term or content slide before it, and the student edition "
                "has no speaker notes to fall back on."
            ),
        ),
        Prose(
            cue="The floor",
            text=(
                "Seven things carry a check or a past paper item. **They stay "
                "in at 219 minutes and they stay in at 179.**"
            ),
        ),
        Bullets(
            cue="These stay",
            numbered=True,
            title="What must not be cut, and why",
            items=(
                "**OHLC and higher timeframe bars**, slides `{s:term:OHLC "
                "data}` and `{s:term:Higher timeframe bar}`. Checks 2 and 3, "
                "and review question 1.",
                "**What the four prices mean**, slides `{s:slide:Not all four "
                "prices are equal}` to `{s:slide:Daily against intraday, and "
                "markets that never close}`. Check 4; the high as supply is "
                "a past paper item.",
                "**The four gaps**, slides `{s:term:Gap}` to `{s:term:Type 3 "
                "and Type 4 gaps}`. Check 5, and a past paper item.",
                "**The constant measures**, slide `{s:slide:The five constant "
                "measures}` and every term after it in Part 3. Checks 7 to "
                "10, four past paper items, and review question 4.",
                "**Scaling**, slides `{s:term:Linear scaling}`, "
                "`{s:term:Ratio scaling}`, `{s:slide:What scaling changes, "
                "and what it does not}`, `{s:slide:Trendlines break at "
                "different times}` and `{s:slide:The same prices can look "
                "bullish or bearish}`. Checks 12, 14 and 15, and three past "
                "paper items.",
                "**The spread**, the four term slides from `{s:term:Bid-ask "
                "spread}` to `{s:term:Late longs}`, and `{s:slide:The spread "
                "and the reward to risk ratio}`. Checks 16 and 18, and review "
                "question 7.",
                "**Futures**, every term slide in Part 6, from "
                "`{s:term:Rollover}` to `{s:term:Perpetual contract}`. Checks "
                "19, 20, 22 and 23, and six past paper items.",
            ),
        ),
        Prose(
            cue="One more",
            text=(
                "The answers to all 23 checks are in "
                "`chapter-03/in-class-checks.md`, generated from the same "
                "content as the deck. **Print that, not this.**"
            ),
        ),
    ),
)


# ==========================================================================

PLAN = Notes(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 3",
    title="Mechanics and Dynamics of Charting",
    presenter="Benjamin C. Sotelo, Institute of Accounts, Business and "
              "Finance, FEU Manila",
    doc_kind="run card",
    # One session, one run. See plan_chapter02.py.
    plans=(),
    front=(THE_CLOCK, THE_CUTS, THE_FLOOR),
    parts=(),
    back=(),
)
