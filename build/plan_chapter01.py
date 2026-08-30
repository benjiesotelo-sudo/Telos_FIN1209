#!/usr/bin/env python3
"""FIN1209 Chapter 1 teaching plan, as plain data.

This is the instructor's document: timing, cut tiers, what to say, which check
comes next. The student-facing document is a different artifact built by
build/build_lecture_notes.py from build/lecture_chapter01.py. Both exist on
purpose; see chapter-01/README.md for the split.

This is the file a contributor edits. There is no markdown source any more:
the plan PDF is generated from here the same way the deck is generated from
content_chapter01.py.

    .venv/bin/python build/build_plan.py

No drawing code lives here. Layout is build/notekit.py, and the reasoning
behind the layout, with sources, is chapter-01/teaching-plan-design.md.

Slides are never referred to by number. They are named by stable key and the
build resolves them against the deck's own content, so the numbers cannot drift
when the deck changes and a stale key fails the build:

    {s:fig:1.11}     {s:check:13}     {s:term:Price}
    {s:slide:The four ways a trade actually makes money}
    {s:part:3}       {s:recap:3}      {a:13}

Chapter 2 is a copy of this file with different content in it.
"""

from __future__ import annotations

from notekit import (Board, Bullets, CheckCard, FigureRef, Flag, Heading,
                     Ladder, Notes, Part, Prose, Sheet, Table)

# ==========================================================================
# Front matter
# ==========================================================================

RUN_CARD = Sheet(
    title="Pick a run plan before you open the deck",
    kicker="Read this first",
    footer="Run card",
    blocks=(
        Prose(
            cue="Why this exists",
            text=(
                "The deck is 195 minutes at full length and most sessions are "
                "not. Nobody has confirmed how long this one is, so choose a "
                "plan now rather than discovering the problem at the 90 minute "
                "mark. All four plans below cover the same chapter and all "
                "seven booklet objectives. They differ in how much of it you "
                "say out loud."
            ),
        ),
        Flag(
            kind="rule",
            cue="Any plan",
            title="If you fall behind mid-session",
            text=(
                "Drop the next figure that only redraws a slide you have "
                "already taught. **Never a check, and never anything between "
                "Figures 1.9 and 1.15.**"
            ),
        ),
        Table(
            cue="The decision",
            title="Minutes per part, by plan",
            headers=("Part", "Slides", "Figs", "Full", "Long", "Standard",
                     "Short"),
            align=("l", "n", "n", "n", "n", "n", "n"),
            rows=(
                ("1  Why we analyze", "25", "1", "26", "22", "13", "10"),
                ("2  Forecasting", "42", "3", "33", "24", "22", "15"),
                ("3  Classifications", "27", "3", "28", "23", "15", "12"),
                ("4  Subjectivity", "39", "13", "42", "34", "20", "15"),
                ("5  Assumptions", "47", "8", "38", "26", "22", "16"),
                ("6  Participants", "22", "3", "28", "21", "13", "7"),
                ("Whole chapter", "202", "31", "195", "150", "105", "75"),
                ("Checks kept, of 25", "", "", "25", "25", "25", "19"),
                ("Minutes that are checks", "", "", "50", "50", "50", "38"),
                ("Minutes that are teaching", "", "", "145", "100", "55", "37"),
            ),
            note=(
                "Slide counts run from the part divider to the recap, which is "
                "what the progress marker counts. The other seven slides are "
                "the openers and closers: five minutes, in every plan."
            ),
        ),
        Prose(
            cue="Read this",
            text=(
                "**Read the last three rows first.** Teaching content falls by "
                "three quarters between Full and Short. Checks fall by a "
                "quarter. That is deliberate and not negotiable: the checks are "
                "how you read the room. Cut talk faster than you cut checks."
            ),
        ),
        Prose(
            cue="Before you start",
            text=(
                "**A live chart in a second window**, because Parts 1, 4 and 5 "
                "all want one. **The board free**, because Parts 1 and 5 both "
                "want writing that stays up for the rest of the session. "
                "**Nothing else.** No handouts, no printing."
            ),
        ),
    ),
)


HOW_TO_RUN = Sheet(
    title="How this deck is meant to be run",
    kicker="Standing instructions",
    footer="How to run this deck",
    blocks=(
        Prose(
            cue="Which deck",
            text=(
                "Teach from the locally built deck with the artwork in it, "
                "not the committed one, which carries placeholders where the 31 "
                "figures go. `README.md` here has both build commands, and "
                "`in-class-checks.md` has every question in full."
            ),
        ),
        Prose(
            cue="The shape",
            text=(
                "The deck is built for a room that includes students with ADHD, "
                "so it is many small slides rather than a few dense ones. Do "
                "not slow down to fill a slide. Most teaching slides are one "
                "idea and should take under a minute.\n\n"
                "Every slide carries its own speaker cue in the PowerPoint "
                "notes, two or three lines each, so **run the deck in Presenter "
                "View.** These notes carry what is not on the screen and not in "
                "Presenter View: the timing, the cut decision, the board work, "
                "the traps, the folds, what the department examines, and the "
                "answer letters."
            ),
        ),
        Heading(cue="", text="Three things carry the session"),
        Bullets(
            cue="",
            numbered=True,
            items=(
                "**The progress marker.** Bottom left of every slide: "
                "`Part 3 of 6 - Classifications | 7 of 16`. Students always "
                "know where they are. If someone asks how much is left, point "
                "at it rather than answering.",
                "**The checks.** Twenty five of them, two questions each, fifty "
                "items. A dark green slide with a gold CHECK chip means a "
                "question is coming. The room learns that colour within the "
                "first twenty minutes.",
                "**The section boundaries.** Six parts. Each opens with what it "
                "covers and closes with a you-now-know recap. Any boundary is a "
                "clean stop if you run out of time or the room runs out of "
                "attention.",
            ),
        ),
        Heading(cue="", text="Running a check",
                sub="Twenty five times today. It is the same procedure every time."),
        Prose(
            cue="Question slide",
            text=(
                "Read Q1 aloud, then Q2. **Sixty seconds, no discussion, no "
                "phones.** Ask for a show of hands on each option before you "
                "advance. The silence is the point: it is the processing time "
                "that makes the question answerable by everyone in the room, "
                "not only by the fastest three."
            ),
        ),
        Prose(
            cue="Reveal slide",
            text=(
                "The reveal gives the letter, the option text and a one-line "
                "reason. **Say the reason out loud.** The letter alone teaches "
                "nothing, and immediate feedback is the half of a check that "
                "does the work."
            ),
        ),
        Flag(
            kind="rule",
            cue="Every check",
            title="If more than about a third of the room misses an item",
            text=(
                "Go back one slide and reteach it. That is what the checks are "
                "for. They carry no marks and you should say so the first time, "
                "or the room will freeze."
            ),
        ),
        Heading(cue="", text="Running a figure slide",
                sub="31 of them, and 13 are in Part 4 alone."),
        Prose(
            cue="Every figure",
            text=(
                "**Name what they are looking at first.** The instrument, the "
                "timeframe, the axes. Then stop talking and let the room look "
                "at it. Only then make the point, off the slide's own speaker "
                "cue. Do not improvise a second reading of the chart."
            ),
        ),
    ),
)


EVIDENCE = Sheet(
    title="What the department actually examines",
    kicker="Why the markers say what they say",
    footer="Evidence",
    blocks=(
        Prose(
            cue="Three documents",
            text=(
                "The cut markers are not taste. They come from the department's "
                "Quiz 1, from Homework 1, and from the seven objectives printed "
                "in the course booklet."
            ),
        ),
        Table(
            cue="Quiz 1",
            title="Quiz 1 is 20 items. Items 1 to 10 are Chapter 1.",
            headers=("Item", "What it asks", "Part", "Slide"),
            align=("n", "l", "n", "n"),
            compact=False,
            rows=(
                ("1", "The four profitable scenarios", "1",
                 "{s:slide:The four ways a trade actually makes money}"),
                ("2", "The dual function", "1",
                 "{s:slide:Technical analysis does exactly two jobs}"),
                ("3", "Intrinsic value, with undervalued and overvalued "
                      "reversed as a trap, and a CAPM line", "2",
                 "{s:term:Intrinsic value}"),
                ("4", "The three ways to forecast, plus flow of funds", "2",
                 "{s:slide:Three approaches, one question}"),
                ("5", "That technical analysis studies price and market action",
                 "2", "{s:term:Technical analysis}"),
                ("6", "That flow of funds means margin debt", "2",
                 "{s:slide:The six streams of market action}"),
                ("7", "Effect against cause, and the two profiles", "2",
                 "{s:slide:The fundamentalist, in four lines}"),
                ("8", "Momentum, the Darvas Box, and contrarians", "3",
                 "{s:term:The non-mean reverting or momentum approach}"),
                ("9", "The mean reverting tool set, naming limit entry orders",
                 "3", "{s:term:Limit and stop entry orders}"),
                ("10", "Random walk", "5", "{s:term:Random walk}"),
            ),
            note=(
                "Items 11 to 20 are Dow Theory and belong to Chapter 2. Every "
                "row above is Core in every plan."
            ),
        ),
        Prose(
            cue="Homework 1",
            text=(
                "A single charting exercise worth 20 points: find live charts "
                "showing different trends, draw trendlines, interpret. That "
                "makes the price-time chart in Part 1 (slide "
                "{s:term:The price-time chart}) and the trendline material in "
                "Part 4 **Core, including at 75 minutes.** It is also the "
                "closing exercise of Part 4, so setting that exercise today is "
                "preparation for it."
            ),
        ),
        Table(
            cue="The booklet",
            title="Seven objectives, printed across slides "
                  "{s:open:objectives1} and {s:open:objectives2}",
            headers=("", "Objective", "Where it lives"),
            align=("n", "l", "l"),
            compact=False,
            rows=(
                ("1", "Understand the key concepts underlying technical "
                      "analysis", "Part 5, s{s:part:5} to s{s:recap:5}"),
                ("2", "Identify the different forms of chart analysis",
                 "Part 3, s{s:slide:Four branches, one subject} "
                 "to s{s:term:Behavioral analysis}"),
                ("3", "Describe the objectives of technical analysis",
                 "Part 1, "
                 "s{s:slide:Technical analysis does exactly two jobs}"),
                ("4", "Understand what subjectivity means in technical "
                      "analysis", "Part 4, s{s:part:4} to s{s:recap:4}"),
                ("5", "Recognize the strengths and weaknesses of technical "
                      "analysis", "Part 3, "
                 "s{s:slide:What technical analysis is genuinely good at} to "
                 "s{s:slide:The three big objections}"),
                ("6", "Categorize market participants by style and by time in "
                      "markets", "Part 6, s{s:part:6} to s{s:recap:6}"),
                ("7", "Identify the various styles and approaches in technical "
                      "analysis", "Parts 3 and 6"),
            ),
        ),
        Flag(
            kind="evidence",
            cue="Do not misread this",
            title="Quiz 1 examines nothing from Part 4 and nothing from Part 6",
            text=(
                "That is not permission to drop them. Objectives 4, 6 and 7 "
                "live there, review questions 3 and 4 are answered in Part 4, "
                "and Homework 1 is Part 4's closing exercise. The old "
                "\"Parts 1 to 3 are a complete unit\" escape hatch threw away "
                "three objectives, which is why it is gone."
            ),
        ),
    ),
)


RUN_PLANS = Sheet(
    title="The four run plans in detail",
    kicker="Mark the deck before the session, not during it",
    footer="Run plans",
    blocks=(
        Flag(
            kind="rule",
            cue="Short session",
            title="Compress the chapter. Do not truncate it.",
            text=(
                "Parts 4, 5 and 6 carry three of the seven booklet objectives "
                "between them, so stopping at Part 3 throws away subjectivity, "
                "the assumptions and the market participants. **Do not split "
                "inside a part.**"
            ),
        ),
        Flag(
            kind="rule",
            cue="Every plan",
            title="Never cut the two learning objectives slides",
            text=(
                "Slides {s:open:objectives1} and {s:open:objectives2}. They are "
                "the only place the students see what they are accountable for, "
                "and the seven objectives are printed across them four and "
                "three."
            ),
        ),
        Ladder(
            core="A booklet objective depends on it, the department's Quiz 1 "
                 "tests it, or a later chapter needs it. Every part page opens "
                 "with its own Core list.",
            reinforcement="It teaches a core idea a second way. This is where "
                          "the Long plan gets its 21 minutes back.",
            enrichment="Interesting, deepens the subject, nothing downstream "
                       "depends on it.",
            fold="Do not show the slide, but do say the one sentence it exists "
                 "for, because a check or a quiz item hangs off it. **Folding "
                 "is how you lose slides without losing content.**",
        ),
        Heading(cue="195 min", text="Full",
                sub="Everything, in the order it is built."),
        Prose(
            cue="",
            text=(
                "All 25 checks. All seven objectives, at full depth. Skip "
                "nothing. Use this only if you have a genuine three and a "
                "quarter hours of teaching time after attendance and setup."
            ),
        ),
        Heading(cue="150 min", text="Long",
                sub="Drop every Enrichment block, plus every figure that only "
                    "redraws a slide you have already taught."),
        Prose(
            cue="Why figures",
            text=(
                "The figures are what took this deck from 165 minutes to 195, "
                "so they are the cheapest 21 minutes in the chapter to hand "
                "back. Ten of the 31 survive. The slides that come off are in "
                "the table at the end of this section."
            ),
        ),
        Table(
            cue="Figures",
            headers=("", "Figures"),
            compact=False,
            rows=(
                ("Skip these 21",
                 "1.1, 1.2, 1.3, 1.4, 1.6, 1.7, 1.8, 1.16, 1.18, 1.19, 1.21, "
                 "1.25, 1.26, 1.27, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35"),
                ("Keep these 10",
                 "**1.9 through 1.15 as one unbroken sequence** "
                 "(slides {s:fig:1.9} to {s:fig:1.15}), plus 1.17, 1.20 and 1.28"),
            ),
        ),
        Prose(cue="Checks", text="All 25. No exceptions. All seven objectives, fully covered."),

        Heading(cue="105 min", text="Standard",
                sub="Core only, with the folds done so no check is stranded."),
        Prose(
            cue="The point",
            text=(
                "Everything marked Reinforcement or Enrichment comes out. Fifty "
                "of the 105 minutes are checks, which is the whole point of this "
                "plan: **it is the shortest run that still teaches the chapter "
                "properly rather than mentioning it.**"
            ),
        ),
        Prose(
            cue="Skip",
            text=(
                "The same 21 figures as Long, plus every Reinforcement and "
                "Enrichment slide. The table below is the whole list for both "
                "plans, in deck order, so you can mark the deck once."
            ),
        ),
        Flag(
            kind="rule",
            cue="Pace",
            title="One pass per accent line at this plan",
            text=(
                "No second example, and no show of hands on a teaching slide. "
                "**The show of hands inside a check stays, in every plan**, "
                "because that is the reading of the room you are paying for.\n\n"
                "Keep the board work in Parts 1 and 5, keep the handclap in "
                "Part 5, and keep the oil example in Part 4. Those four things "
                "cost about six minutes between them and they are the most "
                "memorable minutes in the session."
            ),
        ),
        Prose(cue="Checks",
              text="All 25. All seven objectives, fully covered. Nothing degrades."),

        Heading(cue="75 min", text="Short",
                sub="The floor. Core only, run hard, and six checks come out."),
        Prose(
            cue="What it costs",
            text=(
                "This is the least you can teach and still say honestly that "
                "you covered Chapter 1. Skip everything Standard skips, and "
                "then these six checks: **5, 7, 16, 21, 22 and 24.** Keep 1, 2, "
                "3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 23 and "
                "25. Every check you keep sits on department-examined material "
                "or on a booklet objective."
            ),
        ),
        Table(
            cue="Fold harder",
            title="On top of the Standard folds, by part",
            headers=("Part", "What to do instead"),
            compact=False,
            rows=(
                ("1", "Teach the four trading verbs off the board square "
                      "instead of the four term slides "
                      "(s{s:term:To go long} to s{s:term:To cover}). Draw the "
                      "square, say the four words, say that covering is a buy "
                      "that ends a bearish position, move."),
                ("2", "Run two definitions on screen, Murphy's first and "
                      "Edwards and Magee on the market itself and not the "
                      "goods. Say the Pring probabilities line aloud off the "
                      "Murphy slide. If they remember one sentence today it is "
                      "still that one."),
                ("3", "Run the advantages and the disadvantages slides as a "
                      "single pass. Do not take the show of hands on the two "
                      "bets, just tell them neither bet is right and that this "
                      "is the difficulty of the subject. The checks in this "
                      "part still get theirs."),
                ("4", "The sequence 1.9 to 1.15 runs exactly as written, at "
                      "full speed, with the closing question. Everything around "
                      "it goes to one pass. The oil example gets 60 seconds, "
                      "not three minutes."),
                ("5", "Teach the three forms of EMH off the ladder table on the "
                      "Part 5 page rather than the three term slides "
                      "(s{s:term:The weak form of EMH} to "
                      "s{s:term:The strong form of EMH}). Write it on the board "
                      "once."),
                ("6", "Seven minutes. The four contrast pairs and the "
                      "discretionary pair read as a list, then the time ladder, "
                      "then the method ladder, then stop."),
            ),
        ),
        Flag(
            kind="evidence",
            cue="Objective 6",
            title="At Short, objective 6 degrades. Compensate, cheaply.",
            text=(
                "Objectives one through five and seven are still covered. Part "
                "6 gets seven minutes, so the eight categories become a list "
                "read once rather than a set taught in contrast pairs. Three "
                "compensations, all cheap: keep checks 23 and 25, because check "
                "25's second question is the time ladder; post Figures 1.33 and "
                "1.34 to Canvas **before** the session so the two ladders are "
                "in front of them while you read the list; and say out loud "
                "that objective 6 is examinable and is in the assigned reading."
            ),
        ),
        Bullets(
            cue="Assign it",
            title="Reading you must assign if you run Short. Name it in class "
                  "and put it in Canvas the same day. Lim, The Handbook of "
                  "Technical Analysis, Chapter 1:",
            numbered=True,
            items=(
                "The survival instinct and its four components, and Figure 1.1 "
                "on the mechanics of profiting from a change.",
                "The financial ratios, the top-down and bottom-up approaches, "
                "and all six definitions of technical analysis.",
                "The second list of advantages of technical analysis.",
                "Figures 1.16, 1.18, 1.19 and 1.21, and the price, time and "
                "algorithmic filters.",
                "The four applied assumptions, Figures 1.25 through 1.32, and "
                "price against value.",
                "All of the market participants material, including Figures "
                "1.33, 1.34 and 1.35, and the five ways to participate in gold. "
                "**This is the objective 6 makeup and you should say so.**",
            ),
        ),
        Heading(
            cue="Mark the deck",
            text="What comes off at Long and at Standard",
            sub="Every slide that leaves the deck, in deck order, with the "
                "sentence to say when one is folded rather than dropped. "
                "Standard removes everything in this table; Long removes only "
                "the rows marked Long.",
        ),
        Table(
            cue="",
            headers=("Slide", "What it is", "Off at", "Say this instead"),
            align=("n", "l", "l", "l"),
            compact=False,
            rows=(
                ("{s:slide:What the survival instinct contains}",
                 "What the survival instinct contains", "**Long**",
                 "The herd line, off s{s:slide:Markets run on three instincts}, "
                 "because Part 5 closes that loop."),
                ("{s:slide:What identification hands you before you risk a peso}",
                 "What identification hands you before you risk a peso",
                 "Standard", ""),
                ("{s:slide:How a fundamentalist turns accounts into a number}",
                 "The ratios", "**Long**",
                 "None of them has a time axis, and CAPM balances risk against "
                 "expected return over a risk-free rate. Quiz 1 item 3 carries "
                 "a CAPM line."),
                ("{s:term:The top-down approach}, {s:term:The bottom-up approach}",
                 "Top-down and bottom-up", "**Long**",
                 "Name the pair in one sentence, or check 5 loses its first "
                 "question."),
                ("{s:quote:2:2}", "Edwards and Magee, recorded history and the "
                 "word probable", "**Long**", ""),
                ("{s:quote:2:4}", "Pring, the art of catching a reversal early",
                 "Standard",
                 "Say the takeaway aloud, or check 7 loses its second question."),
                ("{s:quote:2:6}", "Pring, people continue to make the same "
                 "mistakes", "**Long**",
                 "Part 5 says it again on "
                 "s{s:slide:Assumption two: behavior repeats}."),
                ("{s:slide:What technically based timing gives you, continued}",
                 "What technically based timing gives you, continued",
                 "**Long**", ""),
                ("{s:slide:What technical analysis is genuinely good at, continued}",
                 "The advantages, continued", "**Long**",
                 "Keep its third line: it names the self-fulfilling prophecy "
                 "before s{s:term:The self-fulfilling prophecy} does."),
                ("{s:term:The price filter} to {s:term:The algorithmic filter}",
                 "The price, time and algorithmic filters", "**Long**",
                 "Name all three in one minute, because check 16 asks for the "
                 "time filter."),
                ("{s:slide:Price is not the same as value}",
                 "Price is not the same as value", "Standard", ""),
                ("{s:term:Applied assumption one: persistence} to "
                 "{s:term:Applied assumption four: significance is attributed}",
                 "The four applied assumption term slides", "**Long**",
                 "Read the four off the summary slide "
                 "s{s:slide:Four assumptions you apply at the chart} as a set. "
                 "Check 22 still works."),
                ("{s:slide:Where technical analysis works best}",
                 "Where technical analysis works best", "**Long**", ""),
                ("{s:slide:The cast of a market}", "The cast of a market",
                 "**Long**", ""),
                ("{s:slide:Five ways to own gold}", "Five ways to own gold",
                 "**Long**",
                 "A gold backed exchange traded fund is a derivative, because "
                 "check 25 asks for exactly that."),
            ),
            note="Fifteen rows, and six of them cost you nothing but the "
                 "slide. The Short plan cuts on top of all of this; the Short "
                 "section above says how.",
        ),
    ),
)


# ==========================================================================
# Part 1
# ==========================================================================

PART1 = Part(
    number=1,
    title="Why anybody analyzes a market",
    short="Why we analyze",
    minutes=(26, 22, 13, 10),
    terms=("The three motivational instincts, variable of change, price, the "
           "buy low sell high principle, the price-time chart, the dual "
           "function, identification, forecasting, go long, liquidate, go "
           "short, cover, the four profitable scenarios."),
    open_line=("Markets are a survival behavior before they are a financial "
               "one. Say that, then start."),
    close_line=("You cannot profit from something that never moves. Leave the "
                "four-verb square on the board."),
    figures=(FigureRef("1.1", "cut at Long"),),
    ladder=Ladder(
        core=("Markets run on three instincts. To make a profit, something has "
              "to change. Price. The buy low, sell high principle. The rule is "
              "easy, obeying it is not. The price-time chart. Technical "
              "analysis does exactly two jobs. Identification. Forecasting. The "
              "four verb slides. The four ways a trade actually makes money. "
              "Quiz 1 opens with the four scenarios and its second item is the "
              "dual function, so none of this moves. Homework 1 is a charting "
              "exercise, which is why the price-time chart survives even at 75 "
              "minutes."),
        reinforcement=("What identification hands you before you risk a peso, "
                       "s{s:slide:What identification hands you before you risk a peso}, "
                       "which is the Identification slide told a second time. "
                       "Figure 1.1, s{s:fig:1.1}, which redraws the four "
                       "scenarios."),
        enrichment=("What the survival instinct contains, "
                    "s{s:slide:What the survival instinct contains}."),
        fold=("When you cut the survival instinct slide, still say the herd "
              "line in one sentence on the instincts slide "
              "(s{s:slide:Markets run on three instincts}), because Part 5 "
              "closes that loop on the real-world discounting slide, "
              "s{s:slide:What actually happens in the real world}. At Short, "
              "teach the four verbs off the board square instead of the four "
              "term slides, s{s:term:To go long} to s{s:term:To cover}."),
    ),
    blocks=(
        Prose(
            cue="s{s:slide:Markets run on three instincts}",
            text=(
                "Open on the instincts. It reads like an odd place to begin a "
                "finance subject and that is the point: **markets are a "
                "survival behavior before they are a financial one.** Ask which "
                "of the three they would give up last, take two answers, move."
            ),
        ),
        Prose(
            cue="s{s:slide:What the survival instinct contains}",
            text=(
                "Point at the herd line and tell them it comes back in Part 5. "
                "It does, on the real-world discounting slide "
                "s{s:slide:What actually happens in the real world}, and "
                "closing that loop later is worth more than the thirty seconds "
                "it costs here."
            ),
        ),
        Prose(
            cue="s{s:slide:To make a profit, something has to change} to "
                "s{s:term:The buy low, sell high principle}",
            text=(
                "The move from survival to profit is the spine of the part. You "
                "cannot profit from something that never moves, so you need a "
                "variable of change, and price is the most convenient one we "
                "have. Then the mechanical rule, which sounds obvious."
            ),
        ),
        CheckCard(
            index=1, label="Instincts, price, and the basic rule",
            cue="s{s:check:1}, reveal s{s:reveal:1}",
            text=("First check of the session. Say out loud that the checks "
                  "carry no marks before you read Q1, or the room will freeze."),
        ),
        Prose(
            cue="s{s:slide:The rule is easy. Obeying it is not.}",
            text=(
                "Then the trap. **To buy low you must first know today's price "
                "is low. That is a claim about the future.** Everything else "
                "this semester is an attempt to answer it."
            ),
        ),
        Prose(
            cue="s{s:term:The price-time chart}",
            text=(
                "Homework 1 is a charting exercise on live charts with "
                "trendlines drawn and interpreted, so this slide is Core at "
                "every plan length including 75 minutes."
            ),
        ),
        Prose(
            cue="s{s:slide:Technical analysis does exactly two jobs} to "
                "s{s:term:Forecasting}",
            text=(
                "The dual function is Quiz 1 item 2. Identification first, then "
                "forecasting, in that order, and say that the second depends on "
                "the first."
            ),
        ),
        CheckCard(
            index=2, label="The chart and the two jobs",
            cue="s{s:check:2}, reveal s{s:reveal:2}",
            text="",
        ),
        Board(
            cue="s{s:term:To go long} to s{s:term:To cover}",
            title="Write this and leave it up for the rest of the session",
            lines=(
                "            OPEN          CLOSE",
                "BUY         go long       cover",
                "SELL        go short      liquidate",
            ),
            text=(
                "The confusion is never with long. **It is that buying is not "
                "always bullish, because covering is a buy that ends a bearish "
                "position.** Say that sentence explicitly. Leaving the square up "
                "gives the room something to copy from at their own pace, and "
                "Part 6 points back at it."
            ),
        ),
        CheckCard(
            index=3, label="The four words for a trade",
            cue="s{s:check:3}, reveal s{s:reveal:3}",
            text="",
        ),
        Flag(
            kind="trap",
            cue="s{s:slide:The four ways a trade actually makes money}",
            title="Buying high and selling higher counts",
            text=(
                "Warn them explicitly. **The department's Quiz 1 opens with "
                "exactly that item** and students who skim lose the mark."
            ),
        ),
        Prose(
            cue="s{s:fig:1.1}",
            text=(
                "Figure 1.1, the mechanics of profiting from a change. It "
                "redraws the four scenarios, so it is the first thing to drop "
                "in this part and it goes at Long."
            ),
        ),
        Prose(
            cue="s{s:recap:1}",
            text=(
                "Recap, then move. This is a clean stop if you need one, but "
                "Part 2 is the most examined part in the chapter, so do not "
                "spend the buffer here."
            ),
        ),
    ),
)


# ==========================================================================
# Part 2
# ==========================================================================

PART2 = Part(
    number=2,
    title="Three ways to forecast a price",
    short="Forecasting",
    minutes=(33, 24, 22, 15),
    terms=("Fundamental analysis, intrinsic value, undervalued and overvalued, "
           "the ratios, top-down, bottom-up, CAPM in passing, information "
           "analysis, non-public material information, technical analysis, the "
           "six famous definitions, technically and fundamentally based market "
           "timing, the fundamentalist profile, the technical analyst profile, "
           "the six streams of market action, OHLC."),
    open_line=("Three approaches, one question. Not three rivals: three answers "
               "to the same question."),
    close_line=("The fundamentalist is cause, company, value. The technical "
                "analyst is effect, price, timing. Most professionals use both."),
    figures=(FigureRef("1.2", "cut at Long"),
             FigureRef("1.3", "cut at Long"),
             FigureRef("1.4", "cut at Long")),
    ladder=Ladder(
        core=("Three approaches, one question. Fundamental analysis. Intrinsic "
              "value. Undervalued and overvalued. Where fundamental analysis "
              "runs out of road. Information analysis. Why public information "
              "is usually late. Technical analysis. Murphy's first definition. "
              "Edwards and Magee on the market itself and not the goods. Pring "
              "on probabilities, never certainties. Murphy's second quote, "
              "price leads the known fundamentals. What technically based "
              "timing gives you. What fundamentally based timing gives you. The "
              "fundamentalist, in four lines. The technical analyst, in four "
              "lines. The six streams of market action. OHLC. **Quiz 1 spends "
              "items 3, 4, 5, 6 and 7 on this material, more than any other "
              "part gets**, which is why Part 2 loses the least between Long "
              "and Standard of any part in the chapter."),
        reinforcement=("Figure 1.2, s{s:fig:1.2}. Figures 1.3 and 1.4, "
                       "s{s:fig:1.3} and s{s:fig:1.4}. The top-down approach "
                       "and the bottom-up approach, s{s:term:The top-down approach} "
                       "and s{s:term:The bottom-up approach}. How a "
                       "fundamentalist turns accounts into a number, "
                       "s{s:slide:How a fundamentalist turns accounts into a number}. "
                       "Pring on the art of catching a reversal early, "
                       "s{s:quote:2:4}."),
        enrichment=("Edwards and Magee on recorded history and the word "
                    "probable, and Pring on people continuing to make the same "
                    "mistakes, which Part 5 says again on the behavior repeats "
                    "slide s{s:slide:Assumption two: behavior repeats}. What "
                    "technically based timing gives you, continued, "
                    "s{s:slide:What technically based timing gives you, continued}."),
        fold=("Cutting the ratios slide is fine, losing its two sentences is "
              "not: **none of them has a time axis**, and **CAPM balances risk "
              "against expected return over a risk-free rate**. Quiz 1 item 3 "
              "carries a CAPM line. Name top-down and bottom-up as a pair in "
              "one sentence or check 5 loses its first question. Say the Pring "
              "art takeaway aloud or check 7 loses its second."),
    ),
    blocks=(
        Flag(
            kind="rule",
            cue="Whole part",
            title="This is the longest part and the one with the most examinable content",
            text="Keep moving. Nothing here is safe to linger on.",
        ),
        Prose(
            cue="s{s:slide:Three approaches, one question}",
            text=(
                "Frame the three approaches as **three answers to the same "
                "question** rather than as rivals. Fundamental analysis asks "
                "what the thing is worth, information analysis asks what the "
                "news says, technical analysis asks what the market is doing."
            ),
        ),
        Flag(
            kind="trap",
            cue="s{s:term:Intrinsic value}, "
                "s{s:slide:Undervalued and overvalued}",
            title="A stock is overvalued when price is ABOVE intrinsic value",
            text=(
                "Intrinsic value is the single most examinable term in this "
                "part, so make them write it down. Then the undervalued and "
                "overvalued pair, in that order, and say the trap out loud: "
                "the department has quizzed the reversed version."
            ),
        ),
        CheckCard(
            index=4, label="Value and the three approaches",
            cue="s{s:check:4}, reveal s{s:reveal:4}",
            text="Written in the department's I, II, III, IV combination style. "
                 "Point that out the first time it appears.",
        ),
        Prose(
            cue="s{s:slide:How a fundamentalist turns accounts into a number}",
            text=(
                "On the ratios slide, name them and move. They belong to "
                "financial statement analysis, not to this subject. **The line "
                "that matters is that none of them has a time axis.**"
            ),
        ),
        CheckCard(
            index=5, label="Approaches and their limits",
            cue="s{s:check:5}, reveal s{s:reveal:5}",
            text="Q1 asks for top-down, so the fold sentence has to be said "
                 "even when the two term slides come out. Cut at Short.",
        ),
        Prose(
            cue="s{s:term:Information analysis} to "
                "s{s:slide:Why public information is usually late}",
            text=(
                "Information analysis is short. The point is the lateness: by "
                "the time it is public it is usually in the price. That sets up "
                "Murphy's second quote later in this part."
            ),
        ),
        Heading(
            cue="s{s:term:Technical analysis} to s{s:slide:What technically based timing gives you}",
            text="The six definitions",
            sub="Six consecutive quote slides. Do not rush them, do not read "
                "them twice. Each has a takeaway line in green underneath and "
                "that is the sentence to say aloud.",
        ),
        Bullets(
            cue="",
            items=(
                "**Murphy.** Charts are the main tool, and the target is future "
                "price trends. This is the definition to give if an exam asks "
                "for one.",
                "**Edwards and Magee.** Recorded history, and the word that "
                "matters is **probable**.",
                "**Edwards and Magee.** The market itself, not the goods the "
                "market deals in. Cleanest one-line separation from fundamental "
                "analysis there is.",
                "**Pring.** It is an art, and the job is to catch a reversal "
                "early and stay until the evidence turns.",
                "**Pring.** Probabilities, never certainties. **If they remember "
                "one sentence from today, make it this one.**",
                "**Pring.** People continue to make the same mistakes. This is "
                "the behavioral reason the whole subject works.",
                "**Murphy again.** Market price leads the known fundamentals. "
                "This is the bridge into Part 5.",
            ),
        ),
        CheckCard(
            index=6, label="Information, and the first definition",
            cue="s{s:check:6}, reveal s{s:reveal:6}",
            text="",
        ),
        CheckCard(
            index=7, label="Three definitions in a row",
            cue="s{s:check:7}, reveal s{s:reveal:7}",
            text="Q2 asks for the Pring art takeaway, so say it aloud even if "
                 "the quote slide is cut. Cut at Short.",
        ),
        Prose(
            cue="s{s:slide:What technically based timing gives you} to "
                "s{s:slide:What fundamentally based timing gives you}",
            text=(
                "Make them notice for themselves that every fundamental line "
                "ends with \"no precise price or time\". **Do not point it out "
                "first.** Ask what the three lines have in common."
            ),
        ),
        CheckCard(
            index=8, label="Timing, and who answers which question",
            cue="s{s:check:8}, reveal s{s:reveal:8}",
            text="Combination style again.",
        ),
        Prose(
            cue="s{s:slide:The fundamentalist, in four lines} to "
                "s{s:slide:The technical analyst, in four lines}",
            text=(
                "Close on the two profiles. Say the three-word summaries side "
                "by side: **the fundamentalist is cause, company, value; the "
                "technical analyst is effect, price, timing.** Then be fair and "
                "say most professionals use both."
            ),
        ),
        Flag(
            kind="evidence",
            cue="s{s:slide:The six streams of market action}",
            title="Flow of funds includes margin debt",
            text=("That has been a past quiz item, almost verbatim. It is Quiz "
                  "1 item 6."),
        ),
        CheckCard(
            index=9, label="Market action and its data",
            cue="s{s:check:9}, reveal s{s:reveal:9}",
            text="",
        ),
        Prose(
            cue="s{s:recap:2}",
            text=("Recap, then stop. This is the cleanest break point in the "
                  "chapter: Parts 1 and 2 are the whole of the fundamental "
                  "against technical argument, and Part 3 starts a new one."),
        ),
    ),
)


# ==========================================================================
# Part 3
# ==========================================================================

PART3 = Part(
    number=3,
    title="Classifying technical analysis",
    short="Classifications",
    minutes=(28, 23, 15, 12),
    terms=("Classical, statistical, sentiment and behavioral analysis, the mean "
           "reverting or contrarian approach, the non-mean reverting or "
           "momentum approach, limit and stop entry orders, Darvas Box and "
           "Donchian channel breakouts, the advantages, the disadvantages, the "
           "self-fulfilling prophecy, the six-stage cycle, preempting."),
    open_line=("The four branches are a filing system. Every tool in the whole "
               "book lands in exactly one of them."),
    close_line=("The crowd destroys the edge it created, and once everyone "
                "abandons it, the edge comes back. Part 5 answers the other two "
                "objections."),
    figures=(FigureRef("1.6", "cut at Long"),
             FigureRef("1.7", "cut at Long"),
             FigureRef("1.8", "cut at Long")),
    ladder=Ladder(
        core=("Four branches, one subject, and all four branch terms, because "
              "booklet objective 2 is naming the forms of chart analysis. Two "
              "opposite bets about price. The mean reverting or contrarian "
              "approach. The non-mean reverting or momentum approach. Limit and "
              "stop entry orders. The Darvas Box line, said out loud. What "
              "technical analysis is genuinely good at. The honest "
              "disadvantages. The three big objections. The self-fulfilling "
              "prophecy, and both cycle slides. Quiz 1 item 8 is momentum and "
              "Darvas Box and contrarians, item 9 is the mean reverting tool "
              "set and names limit entry orders, and item 10 is random walk, "
              "which the room meets on the three objections slide. Objectives 5 "
              "and 7 both live here."),
        reinforcement=("Figure 1.6, s{s:fig:1.6}. Figure 1.7, s{s:fig:1.7}. "
                       "Figure 1.8, s{s:fig:1.8}. What technical analysis is "
                       "genuinely good at, continued, "
                       "s{s:slide:What technical analysis is genuinely good at, continued}."),
        enrichment=("None. **Part 3 is the most heavily examined part per "
                    "minute in the chapter.** What you save here you save on "
                    "pace, not on slides."),
        fold=("The advantages continued slide folds into the previous one, but "
              "keep its third line, because that line is what names the "
              "self-fulfilling prophecy before the term slide "
              "s{s:term:The self-fulfilling prophecy} arrives. At Short, run "
              "advantages and disadvantages as a single pass and skip the show "
              "of hands on the two bets."),
    ),
    blocks=(
        Prose(
            cue="s{s:slide:Four branches, one subject} to "
                "s{s:term:Behavioral analysis}",
            text=(
                "The four branches are a filing system. Every tool in the whole "
                "book lands in exactly one of them, and students should be able "
                "to sort a named technique into a branch on demand. **That is "
                "the examinable skill here, not the contents of any branch.**\n\n"
                "The quickest way to fix the branches is by contrast. Classical "
                "is qualitative and visual, statistical is quantitative. "
                "Sentiment studies the mood, behavioral studies the participant."
            ),
        ),
        CheckCard(
            index=10, label="The four branches",
            cue="s{s:check:10}, reveal s{s:reveal:10}",
            text="Booklet objective 2 in one check.",
        ),
        Prose(
            cue="s{s:slide:Two opposite bets about price}",
            text=(
                "Ask for a show of hands on which feels more natural **before** "
                "you teach either. Then say neither is right, they are right at "
                "different times, and that this is the whole difficulty of the "
                "subject."
            ),
        ),
        Flag(
            kind="evidence",
            cue="s{s:term:The non-mean reverting or momentum approach}",
            title="Name the Darvas Box out loud",
            text="The department has quizzed it as a momentum example. Quiz 1 "
                 "item 8.",
        ),
        Prose(
            cue="s{s:term:Limit and stop entry orders}",
            text=(
                "**The order type gives the trader away.** Contrarians want a "
                "good price so they use limit orders; momentum traders want "
                "confirmation so they use stop orders. Ask which a contrarian "
                "prefers before you reveal it."
            ),
        ),
        CheckCard(
            index=11, label="The two approaches",
            cue="s{s:check:11}, reveal s{s:reveal:11}",
            text="Combination style.",
        ),
        Flag(
            kind="rule",
            cue="s{s:slide:What technical analysis is genuinely good at} to "
                "s{s:slide:The three big objections}",
            title="Be honest about the disadvantages",
            text=(
                "A course that only sells the method is a bad course. Three big "
                "objections get named on one slide: random walk, the strong "
                "form of EMH, and the self-fulfilling prophecy. **Say clearly "
                "that only the third is taught here and that Part 5 answers the "
                "other two properly**, so nobody spends Part 3 worrying about a "
                "term they have not met."
            ),
        ),
        Prose(
            cue="s{s:term:The self-fulfilling prophecy} to "
                "s{s:slide:The cycle, stages four to six}",
            text=(
                "The cycle runs over two slides, stages one to three then four "
                "to six. Stages one to three are the advantage, which is when "
                "the signal is worth trading. **Ask what happens when a "
                "strategy becomes too popular, then show stage four.** The crowd "
                "destroys the edge it created, and then, once everyone abandons "
                "it, the edge comes back. The process repeats."
            ),
        ),
        CheckCard(
            index=12, label="Strengths, weaknesses, and the prophecy",
            cue="s{s:check:12}, reveal s{s:reveal:12}",
            text="",
        ),
        Prose(
            cue="s{s:recap:3}",
            text=("Recap, then move. Say before you leave the part that Part 5 "
                  "answers random walk and the strong form of EMH properly, so "
                  "the two loose objections do not sit there unanswered."),
        ),
    ),
)


# ==========================================================================
# Part 4
# ==========================================================================

PART4 = Part(
    number=4,
    title="Subjectivity",
    short="Subjectivity",
    minutes=(42, 34, 20, 15),
    terms=("Objective and subjective aspects, the three activities, "
           "subjectivity, the twofold problem, contradictory, confirmatory and "
           "complementary signals, why indicators disagree, tick volume, the "
           "pattern size rule, interpretational and inferential subjectivity, "
           "selective perception, subjective objectivity, price, time and "
           "algorithmic filters, practice."),
    open_line=("The chart is objective, the reading is subjective. The data is "
               "not the problem, the reader is."),
    close_line=("Subjectivity is not a technical analysis problem, it is an "
                "analysis problem. Set the two-student trendline exercise "
                "before they leave."),
    figures=(FigureRef("1.9", "keep, all plans"),
             FigureRef("1.10", "keep, all plans"),
             FigureRef("1.11", "keep, all plans"),
             FigureRef("1.12", "keep, all plans"),
             FigureRef("1.13", "keep, all plans"),
             FigureRef("1.14", "keep, all plans"),
             FigureRef("1.15", "keep, all plans"),
             FigureRef("1.16", "cut at Long"),
             FigureRef("1.17", "keep to Standard"),
             FigureRef("1.18", "cut at Long"),
             FigureRef("1.19", "cut at Long"),
             FigureRef("1.20", "keep to Standard"),
             FigureRef("1.21", "cut at Long")),
    ladder=Ladder(
        core=("Objective and subjective at the same time. Analysis is three "
              "separate activities. Subjectivity. The problem is twofold. "
              "**Figures 1.9 through 1.15, the whole sequence, in every plan "
              "including the 75 minute one.** Contradictory, confirmatory and "
              "complementary signals. Why indicators disagree in the first "
              "place. Resolving conflicting chart patterns, with Figure 1.17. "
              "The same fact, read two ways. Selective perception. Even the "
              "entry point is subjective, with Figure 1.20. Subjectivity "
              "shrinks with practice."),
        reinforcement=("Figure 1.16, s{s:fig:1.16}. Figure 1.18, "
                       "s{s:fig:1.18}. Figure 1.19, s{s:fig:1.19}. Figure "
                       "1.21, s{s:fig:1.21}. The price, time and algorithmic "
                       "filters as three separate term slides, "
                       "s{s:term:The price filter} to "
                       "s{s:term:The algorithmic filter}."),
        enrichment="None. Nothing in this part is decorative.",
        fold=("Teach the three filters together off one slide in a minute "
              "rather than losing them, because check 16 asks for the time "
              "filter. At Short the sequence still runs exactly as written, at "
              "full speed, with the closing question; everything around it goes "
              "to one pass and the oil example gets 60 seconds."),
    ),
    blocks=(
        Flag(
            kind="evidence",
            cue="Whole part",
            title="Quiz 1 examines nothing from this part. Ignore that.",
            text=(
                "Booklet objective 4 is this part by name, review questions 3 "
                "and 4 are answered here, and Homework 1 asks for trendlines "
                "drawn on a live chart and interpreted, which is Figure 1.20's "
                "argument and the closing exercise. **Part 4 is the last thing "
                "you cut, not the first.**"
            ),
        ),
        Prose(
            cue="s{s:slide:Objective and subjective at the same time} to "
                "s{s:slide:The problem is twofold}",
            text=(
                "This part makes students uncomfortable and it is supposed to. "
                "Say the frame early and repeat it: **the chart is objective, "
                "the reading is subjective. The data is not the problem, the "
                "reader is.**\n\n"
                "Most students assume only the inference step is subjective. "
                "Step one already is, because you chose which two troughs to "
                "connect. Make them repeat the three activities back: "
                "identifying, interpreting, inferring."
            ),
        ),
        Flag(
            kind="rule",
            cue="s{s:fig:1.9} to s{s:fig:1.15}",
            title="The seven readings are one move, not seven slides",
            text=(
                "Same price chart every time: bare, then trendlines, moving "
                "averages, chart patterns, regression with divergence, "
                "regression with volume, and volatility bands with volume and "
                "MACD. **Run them straight through without stopping to teach "
                "any single one**, naming each reading in a few words as it "
                "comes up.\n\n"
                "When the seventh is on screen, ask the room what changed "
                "between the first slide and this one. The answer is nothing "
                "except the analyst, and that is the argument of the whole "
                "part. It only lands if they have watched all seven go past in "
                "a row, so do not summarise the sequence, do not skip ahead, "
                "and **do not take questions in the middle of it.**"
            ),
        ),
        CheckCard(
            index=13, label="Where subjectivity lives",
            cue="s{s:check:13}, reveal s{s:reveal:13}",
            text="Straight after the sequence. Let the discomfort sit before "
                 "you resolve it.",
        ),
        Prose(
            cue="s{s:term:Contradictory signals} to "
                "s{s:term:Complementary signals}",
            text=(
                "**Complementary signals is the most useful idea in this part.** "
                "Walk the example slowly. A 20 period reading says slightly "
                "overbought and a 100 period reading says slightly oversold. "
                "That is not a contradiction, it is short term stretched and "
                "long term cheap, and the astute trader waits for cheap on both "
                "horizons and enters there."
            ),
        ),
        CheckCard(
            index=14, label="Three kinds of signal",
            cue="s{s:check:14}, reveal s{s:reveal:14}",
            text="",
        ),
        Flag(
            kind="trap",
            cue="s{s:slide:Resolving conflicting chart patterns}",
            title="The pattern size rule is review question three",
            text=(
                "Say so and make them write it down: **measure the patterns, "
                "and the larger formation's sentiment takes precedence, because "
                "larger formations speak for the longer term.** Give the caution "
                "too: an upside break of a large bearish formation can be "
                "violent precisely because it is unexpected, and short covering "
                "fuels it."
            ),
        ),
        Prose(
            cue="s{s:slide:The same fact, read two ways}",
            text=(
                "The oil example is worth the time. Two fundamentalists, one "
                "fact, two opposite and defensible conclusions. Then land the "
                "caption: both of those analysts are fundamentalists. "
                "**Subjectivity is not a technical analysis problem, it is an "
                "analysis problem.** That is the fair-minded conclusion of the "
                "whole part and students should leave able to say it."
            ),
        ),
        CheckCard(
            index=15, label="Conflicts, and how to settle them",
            cue="s{s:check:15}, reveal s{s:reveal:15}",
            text="",
        ),
        Prose(
            cue="s{s:term:Selective perception}",
            text=(
                "Selective perception is the most expensive habit in the room "
                "and every one of them will do it. Give the antidote plainly: "
                "**a signal that disagrees with you is the most informative "
                "thing on your screen.**"
            ),
        ),
        Prose(
            cue="s{s:slide:Even the entry point is subjective}, "
                "s{s:fig:1.20}",
            text=(
                "**Subjective objectivity is review question four.** "
                "Individually objective, collectively subjective. Use the "
                "program trading point to stop them believing that automation "
                "escapes the problem: the moment a parameter can be adjusted, "
                "subjectivity is back."
            ),
        ),
        CheckCard(
            index=16, label="Bias, entries, and filters",
            cue="s{s:check:16}, reveal s{s:reveal:16}",
            text="Q2 asks for the time filter, so the three filters have to be "
                 "named even when their term slides are folded. Cut at Short.",
        ),
        Prose(
            cue="s{s:slide:Subjectivity shrinks with practice}",
            text=(
                "Close on practice, and set the exercise before they leave: "
                "**two students, one chart, draw trendlines separately, then "
                "compare.** The point is to be comfortable with the difference, "
                "not to find a winner. This is Homework 1 in miniature."
            ),
        ),
        Prose(
            cue="s{s:recap:4}",
            text=("Recap. The sentence they should leave the part able to say "
                  "is that subjectivity is an analysis problem, not a technical "
                  "analysis problem. If that did not land, this is the recap to "
                  "spend an extra thirty seconds on."),
        ),
    ),
)


# ==========================================================================
# Part 5
# ==========================================================================

PART5 = Part(
    number=5,
    title="The assumptions underneath everything",
    short="Assumptions",
    minutes=(38, 26, 22, 16),
    terms=("Market discounting, what markets can and cannot discount, what "
           "markets are really discounting, EMH, instantaneous and rational, "
           "the semi-efficient market, the weak, semi-strong and strong forms, "
           "random walk and the Markovian condition, real-world discounting, "
           "price versus value, behavior repeats, preempting and program "
           "trading, the market moves in trends, the challenges of trend "
           "following, the four applied assumptions, efficacy at various "
           "timeframes."),
    open_line=("Write the three assumptions on the board and leave them there. "
               "Remove any one and technical analysis stops making sense."),
    close_line=("An indicator that is badly designed will still become reliable "
                "if enough capital follows it. That closes the Part 3 loop."),
    figures=(FigureRef("1.28", "keep to Standard"),
             FigureRef("1.29", "cut at Long"),
             FigureRef("1.27", "cut at Long"),
             FigureRef("1.30", "cut at Long"),
             FigureRef("1.31", "cut at Long"),
             FigureRef("1.32", "cut at Long"),
             FigureRef("1.25", "cut first"),
             FigureRef("1.26", "cut first")),
    ladder=Ladder(
        core=("Three assumptions hold the subject up. Market discounting. What "
              "the market can and cannot discount. What the market is really "
              "discounting, with Figure 1.28. The Efficient Market Hypothesis. "
              "Efficient, under EMH, means two things. Why perfect efficiency "
              "cannot happen, with the handclap. The semi-efficient market. The "
              "weak, semi-strong and strong forms. Random walk. Random walk is "
              "not the same as EMH. What actually happens in the real world. "
              "Assumption two, behavior repeats. Three things that erode "
              "repeatability. Assumption three, the market moves in trends. "
              "Trend following is not free. Four assumptions you apply at the "
              "chart. **This part is booklet objective 1 on its own.** Quiz 1 "
              "item 10 is random walk, review questions 2, 5 and 6 all live "
              "here, and review question 1 needs the erosion slide for the "
              "shocks and algorithmic trading half of its answer."),
        reinforcement=("Figure 1.27, s{s:fig:1.27}. Figure 1.29, "
                       "s{s:fig:1.29}. Figure 1.30, s{s:fig:1.30}. Figures "
                       "1.31 and 1.32, s{s:fig:1.31} and s{s:fig:1.32}. Price "
                       "is not the same as value, "
                       "s{s:slide:Price is not the same as value}. The four "
                       "applied assumption term slides, "
                       "s{s:term:Applied assumption one: persistence} to "
                       "s{s:term:Applied assumption four: significance is attributed}, "
                       "which restate the four numbered lines on the summary "
                       "slide one at a time."),
        enrichment=("Figures 1.25 and 1.26, s{s:fig:1.25} and s{s:fig:1.26}, "
                    "the angular symmetries and the ordered structure of price. "
                    "Where technical analysis works best, "
                    "s{s:slide:Where technical analysis works best}. **These two "
                    "are the first things to leave the chapter.**"),
        fold=("Teach the applied assumptions as a set off the summary slide "
              "s{s:slide:Four assumptions you apply at the chart} and you lose "
              "four slides and no content, and check 22 still works. At Short, "
              "teach the three forms of EMH off the ladder table below rather "
              "than the three term slides, and write the table on the board "
              "once. **Keep the handclap in every plan; it costs ten seconds.**"),
    ),
    blocks=(
        Board(
            cue="s{s:slide:Three assumptions hold the subject up}",
            title="Write this first and leave it up",
            lines=(
                "1.  The market discounts everything.",
                "2.  Market behavior repeats itself.",
                "3.  The market moves in trends.",
            ),
            text=("The heaviest part of the chapter. **Remove any one and "
                  "technical analysis stops making sense.** Leaving all three "
                  "on the board gives the room a fixed reference for the next "
                  "38 minutes."),
        ),
        Flag(
            kind="trap",
            cue="s{s:slide:What the market can and cannot discount}",
            title="The two CANNOT lines are where the exam question lives",
            text=(
                "Read them twice. Then explain the insider point carefully: "
                "insider information is non-public, but insider **trading** is "
                "visible in the market, so the market can discount it."
            ),
        ),
        Prose(
            cue="s{s:slide:What the market is really discounting}, "
                "s{s:fig:1.28}",
            text=(
                "The five-line slide should be read at pace. The effect is "
                "cumulative. Then the payoff, which is the caption: **this is "
                "why a company can beat expectations and still fall.**"
            ),
        ),
        CheckCard(
            index=17, label="Discounting",
            cue="s{s:check:17}, reveal s{s:reveal:17}",
            text="",
        ),
        Flag(
            kind="evidence",
            cue="s{s:term:The Efficient Market Hypothesis} to "
                "s{s:slide:Efficient, under EMH, means two things}",
            title="EMH against market discounting is review question two",
            text=(
                "Give the answer explicitly, dictate it if you have to: EMH "
                "requires that every participant reacts instantaneously and "
                "rationally. Technical analysis requires no such thing. **It "
                "requires only that the market discounts everything that "
                "becomes known to it, timely or untimely, rational or "
                "irrational.**"
            ),
        ),
        Flag(
            kind="rule",
            cue="s{s:slide:Why perfect efficiency cannot happen}",
            title="Do the handclap test. Every plan. Ten seconds.",
            text=(
                "Ask the whole room to clap the instant you say now. You will "
                "not get one sound. **If a hundred students in one room cannot "
                "coordinate, a million traders across a market certainly "
                "cannot.** That is the argument against perfect efficiency, "
                "delivered in a form they will remember."
            ),
        ),
        CheckCard(
            index=18, label="EMH against market discounting",
            cue="s{s:check:18}, reveal s{s:reveal:18}",
            text="",
        ),
        Table(
            cue="s{s:term:The weak form of EMH} to "
                "s{s:term:The strong form of EMH}",
            title="The three forms are the highest value item in this part. "
                  "Make them write the ladder in order.",
            headers=("Form", "Covers", "Kills"),
            rows=(
                ("Weak", "Past price information", "Technical analysis"),
                ("Semi-strong", "All public information",
                 "Fundamental analysis as well"),
                ("Strong", "Public and private information",
                 "All analysis and forecasting"),
            ),
            note="At Short, teach the three forms off this table and write it "
                 "on the board once, instead of running the three term slides.",
        ),
        CheckCard(
            index=19, label="The three forms",
            cue="s{s:check:19}, reveal s{s:reveal:19}",
            text="Combination style.",
        ),
        Flag(
            kind="trap",
            cue="s{s:term:Random walk} to "
                "s{s:slide:Random walk is not the same as EMH}",
            title="Random walk is review question five, and the answer is no",
            text=(
                "Draw the distinction in one sentence: **EMH says the market is "
                "too fast to beat, random walk says the market is meaningless.** "
                "Then the argument against it: watch how precisely price tests "
                "and reacts at a round number or an old high. Chance does not "
                "aim."
            ),
        ),
        Prose(
            cue="s{s:slide:What actually happens in the real world}",
            text=(
                "**This is where you close the herd loop from Part 1.** "
                "Insiders accumulate, the public joins, the crowd overreacts, "
                "the insiders sell into it, a top forms. That is why a chart "
                "looks nothing like a coin flip."
            ),
        ),
        CheckCard(
            index=20, label="Random walk and real markets",
            cue="s{s:check:20}, reveal s{s:reveal:20}",
            text="",
        ),
        Prose(
            cue="s{s:slide:Assumption two: behavior repeats} to "
                "s{s:slide:Trend following is not free}",
            text=(
                "On trend following, **emphasize the low winning percentage.** "
                "Students assume a good method wins most of its trades. It does "
                "not, and the drawdowns are the price of the profits.\n\n"
                "The erosion slide "
                "s{s:slide:Three things that erode repeatability} carries the "
                "shocks and algorithmic trading half of review question one, so "
                "it is Core even though it looks like a side note."
            ),
        ),
        CheckCard(
            index=21, label="Repetition and trends",
            cue="s{s:check:21}, reveal s{s:reveal:21}",
            text="Cut at Short.",
        ),
        Prose(
            cue="s{s:slide:Four assumptions you apply at the chart}",
            text=(
                "The four applied assumptions are examinable as a set. Number "
                "them on the board. The fourth one is the self-fulfilling "
                "prophecy in formal dress, so close that loop from Part 3 and "
                "deliver the uncomfortable corollary: **an indicator that is "
                "badly designed will still become reliable if enough capital "
                "follows it.**"
            ),
        ),
        CheckCard(
            index=22, label="The four applied assumptions",
            cue="s{s:check:22}, reveal s{s:reveal:22}",
            text="Cut at Short.",
        ),
        Prose(
            cue="s{s:recap:5}",
            text=("Recap. The three assumptions are still on the board from the "
                  "start of the part, so read the recap against them, and rub "
                  "the board only once Part 6 is under way."),
        ),
    ),
)


# ==========================================================================
# Part 6
# ==========================================================================

PART6 = Part(
    number=6,
    title="Who is in the market",
    short="Participants",
    minutes=(28, 21, 13, 7),
    terms=("The eight categories, retail and institutional, speculator and "
           "investor, supply side and demand side, professional and novice, "
           "discretionary and nondiscretionary, participants by time in the "
           "market, participants by method, the five main markets, derivatives, "
           "the five ways to participate in gold."),
    open_line=("A trade requires two people who disagree about price and agree "
               "on a number. Every price on every chart is that disagreement."),
    close_line=("One underlying, five instruments, five different risk "
                "profiles, and only the first one needs a vault."),
    figures=(FigureRef("1.33", "cut at Long"),
             FigureRef("1.34", "cut at Long"),
             FigureRef("1.35", "cut at Long")),
    ladder=Ladder(
        core=("The four contrast pair slides that carry the eight categories: "
              "retail and institutional, speculators and investors, supply side "
              "and demand side, professionals and novices. Discretionary and "
              "nondiscretionary traders. Sorted by time spent in the market. "
              "Sorted by method. The main markets, and Derivative, which hangs "
              "off it and which check 25 asks about. **Booklet objective 6 is "
              "categorizing participants by style and by time in markets, and "
              "objective 7 closes on the method ladder.** This is the part the "
              "old \"Parts 1 to 3 are a complete unit\" escape hatch threw "
              "away, and it is a stated objective, so it does not get thrown "
              "away again."),
        reinforcement=("Figure 1.33, s{s:fig:1.33}. Figure 1.34, "
                       "s{s:fig:1.34}. Figure 1.35, s{s:fig:1.35}. The cast of "
                       "a market, s{s:slide:The cast of a market}. Five ways to "
                       "own gold, s{s:slide:Five ways to own gold}."),
        enrichment="None.",
        fold=("Fold gold into the Derivative term slide "
              "s{s:term:Derivative} in one sentence, **a gold backed exchange "
              "traded fund is a derivative**, because check 25 asks for exactly "
              "that. The two ladders stay on screen in every plan down to "
              "Standard; at Short they are the only two slides in this part "
              "that get their full minute."),
    ),
    blocks=(
        Flag(
            kind="evidence",
            cue="Whole part",
            title="Quiz 1 examines nothing from this part either. The booklet does, twice.",
            text=(
                "At Short this is the one objective that degrades, and the "
                "compensation is on the run plans page. The lightest part, and "
                "a good one to end on."
            ),
        ),
        Prose(
            cue="s{s:slide:The cast of a market}",
            text=(
                "Open by saying **a trade requires two people who disagree "
                "about price and agree on a number.** Every price on every "
                "chart is that disagreement."
            ),
        ),
        Prose(
            cue="s{s:term:Retail and institutional participants} to "
                "s{s:term:Professionals and novices}",
            text=(
                "The eight categories are a list to be able to reproduce: "
                "retail, institutional, speculator, supply side, demand side, "
                "professional, investor, novice. The deck teaches them in four "
                "contrast pairs, which is how they stick."
            ),
        ),
        Bullets(
            cue="",
            title="Two of them are worth a sentence beyond the definition",
            items=(
                "**The book lists supply side and demand side and defines "
                "neither.** Give the common industry reading, the supply side "
                "provides the market service and the demand side consumes it, "
                "then name the second reading, producers hedging output "
                "against consumers hedging input. Do not rule between them.",
                "**Novice is a stage, not a verdict.** Everyone in the room is "
                "one today, and Part 4 already said that subjectivity in "
                "pattern recognition falls with practice.",
            ),
        ),
        CheckCard(
            index=23, label="Who is who",
            cue="s{s:check:23}, reveal s{s:reveal:23}",
            text="Kept in every plan, including Short.",
        ),
        CheckCard(
            index=24, label="Categories and methods",
            cue="s{s:check:24}, reveal s{s:reveal:24}",
            text="Cut at Short.",
        ),
        Prose(
            cue="s{s:slide:Sorted by time spent in the market}, "
                "s{s:slide:Sorted by method}",
            text=(
                "**Both ladders are stated learning objectives in the course "
                "booklet, so make sure both slides get their minute.** The "
                "method ladder closes the loop with Part 3: reversal traders "
                "are the contrarians, trend traders are the momentum side."
            ),
        ),
        Flag(
            kind="trap",
            cue="s{s:slide:Sorted by method}",
            title="Give the scale trading warning plainly",
            text=(
                "Averaging against price until it turns is the highest risk "
                "method on that list, and **it is how accounts end.**"
            ),
        ),
        Prose(
            cue="s{s:slide:The main markets} to "
                "s{s:slide:Five ways to own gold}",
            text=(
                "Finish on the gold slide. One underlying, five instruments, "
                "five different risk profiles, and only the first one needs a "
                "vault."
            ),
        ),
        CheckCard(
            index=25, label="Markets and instruments",
            cue="s{s:check:25}, reveal s{s:reveal:25}",
            text="Last check of the session. Q2 is the time ladder, which is "
                 "why this one survives at Short even though objective 6 "
                 "degrades there.",
        ),
        Prose(
            cue="s{s:recap:6} to s{s:slide:Next: Dow Theory}",
            text=("Recap, then the three closing slides. Do not let the session "
                  "end on a check: the last thing they hear should be what "
                  "Chapter 1 was for, and what is coming next."),
        ),
    ),
)


# ==========================================================================
# Back matter
# ==========================================================================

CLOSE_OUT = Sheet(
    title="Before they leave",
    kicker="The review crib, and what to say about the quiz",
    footer="Before they leave",
    blocks=(
        Heading(
            cue="s{s:slide:The review questions to prepare}",
            text="The chapter review questions",
            sub="Short crib. The full answers are in the deck, in the parts "
                "named.",
        ),
        Table(
            cue="",
            headers=("", "Question", "Where", "Answer in one line"),
            align=("n", "l", "l", "l"),
            compact=False,
            rows=(
                ("1", "Challenges to technical analysis", "Part 3",
                 "Subjectivity of interpretation, disruption of repeatability "
                 "by shocks and by algorithmic trading, the difficulty of "
                 "inference, random walk, the strong form of EMH, and the "
                 "self-fulfilling prophecy."),
                ("2", "Market discounting against EMH", "Part 5",
                 "EMH requires instantaneous and rational reaction by all "
                 "participants. Technical analysis requires only that the "
                 "market discounts what becomes known to it."),
                ("3", "Resolving conflicting signals or patterns", "Part 4",
                 "Check the time horizons first, since apparently conflicting "
                 "signals are often complementary. For chart patterns, measure "
                 "them: the larger formation's sentiment takes precedence "
                 "until its own level is breached."),
                ("4", "Why identifying a trend change is subjective", "Part 4",
                 "Each act of identification is objective, but you chose the "
                 "trendline, and an alternative trendline gives a different "
                 "answer. Individually objective, collectively subjective."),
                ("5", "Is random walk a true reflection of the markets?",
                 "Part 5",
                 "No. Markets are driven by perception and expectation, and "
                 "participants react in predictable ways at psychologically "
                 "significant prices."),
                ("6", "The three levels of discounting under EMH", "Part 5",
                 "Weak, semi-strong and strong. The ladder table is on the "
                 "Part 5 page."),
                ("7", "A good definition of technical analysis", "Part 2",
                 "Murphy: the study of market action, primarily through the "
                 "use of charts, for the purpose of forecasting future price "
                 "trends. Slide {s:quote:2:1}."),
                ("8", "Advantages and disadvantages", "Part 3",
                 "Four slides, s{s:slide:What technical analysis is genuinely good at} "
                 "to s{s:slide:The three big objections}."),
            ),
        ),
        Heading(
            cue="s{s:slide:Chapter 1 in five sentences} to "
                "s{s:slide:Next: Dow Theory}",
            text="Quiz preparation to mention",
            sub="The last three slides.",
        ),
        Flag(
            kind="rule",
            cue="Say this",
            title="Quiz 1 covers Chapters 1 and 2 together",
            text=(
                "Many department items use the \"I, II, III, IV, which "
                "combination is correct\" style, so five of the twenty five "
                "checks are written that way: **checks 4, 8, 11, 19 and 25.** "
                "Tell them to expect it, and that the trick is to find the one "
                "false statement rather than to verify all four."
            ),
        ),
        Prose(
            cue="Homework 1",
            text=(
                "Homework 1 is a charting exercise, not multiple choice. It "
                "asks for a live chart with trendlines drawn and the trend "
                "interpreted, which is exactly the Part 4 closing exercise. "
                "**Setting that exercise today is preparation for it.**"
            ),
        ),
        Prose(
            cue="s{s:slide:Next: Dow Theory}",
            text=(
                "Close by naming what comes next. Dow Theory is Chapter 2 and "
                "the other half of Quiz 1, so the preview is not a courtesy."
            ),
        ),
    ),
)


PLAN = Notes(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 1",
    title="Introduction to the Art and Science of Technical Analysis",
    presenter="Benjamin C. Sotelo, Institute of Accounts, Business and Finance, "
              "FEU Manila",
    plans=("Full", "Long", "Standard", "Short"),
    front=(RUN_CARD, HOW_TO_RUN, EVIDENCE, RUN_PLANS),
    parts=(PART1, PART2, PART3, PART4, PART5, PART6),
    back=(CLOSE_OUT,),
)
