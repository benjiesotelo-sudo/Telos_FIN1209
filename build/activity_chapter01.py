#!/usr/bin/env python3
"""FIN1209 Chapter 1 take-home activity, as plain data.

This is the file a contributor edits. Layout lives in build/activitykit.py and
knows nothing about any chapter. The numbers live in build/activity_data.py and
are computed from the committed price files, never typed here.

    .venv/bin/python build/build_activity.py

It replaces the course booklet's Homework 1, which read in full: "CHARTING
EXERCISES: Using different trading platform, Search for a latest charts that
shows different trend. Add trend lines for a clear vision of trend then
interpret the chart. (20 points)". It is worth 100 here, not 20. Every
checkable answer is worth 2 points, which makes each identification block 32
and leaves no fraction anywhere on the sheet. The published version promised
sixteen answers at half a mark each and then gave them six marks. Same
charting platform at the end, and a rubric the original never had.

The teaching idea is the chapter's own dual function. Identification records
what price did and can be marked right or wrong. Forecasting cannot, and the
sheet says so out loud, twice, because a student who thinks the forecast is
the graded part has learned the opposite of Part 4.

**Every term used here is one Lim defines in Chapter 1.** Price, the
price-time chart, identification, forecasting, subjectivity, trend as
successively higher or lower peaks and troughs. There is no support, no
resistance, no moving average and no indicator, because the chapter defines
none of them.

**The written-answer rubric is not in this file.** It is the course's, it
lives once in build/rubric.py, and this module only says which of its marks
the rubric decides and supplies the worked examples, which have to be written
on this activity's own prices.
"""

from __future__ import annotations

import datetime as dt

import activity_data as ad
from activitykit import (Activity, Applied, Callout, Figure, Head, Lines,
                         Para, Points, Question, QuestionSet, Section, Shot,
                         Step, Table, TypeBox, Worked, show_marks,
                         written_rubric)
from rubric import WRITTEN

# --------------------------------------------------------------------------
# The one thing in this file that is a live address
#
# The captain owns this spreadsheet. It holds both price windows, one tab
# each, and it is shared "anyone with the link can view". Students never edit
# it: they pull from it with IMPORTRANGE, which needs read access and nothing
# more. If it is ever deleted, chapter-01/activity/README.md has the one
# command that rebuilds it from the committed CSV files, and this line is the
# only thing that then has to change.
# --------------------------------------------------------------------------

SOURCE_SHEET = "1y3ybzmZ7fqcvday1YMGuBIeiS228Xe8m6q0cH-7TjZ8"

PLATFORM = "TradingView"
PLATFORM_URL = "www.tradingview.com/chart/"


def _pull(series: ad.Series, tab: str) -> str:
    return f'=IMPORTRANGE("{SOURCE_SHEET}","{tab}!{series.data_range}")'


def _d(day) -> str:
    return f"{day:%d %B %Y}".lstrip("0")


def _dm(iso: str) -> str:
    """A date inside the window, without the year every reader already has."""
    return f"{dt.date.fromisoformat(iso):%d %B}".lstrip("0")


def _trading_days_between(series: ad.Series, first, last) -> int:
    """Rows apart on the student's own sheet, which is what they can count."""
    return series.dates.index(last) - series.dates.index(first)


# ==========================================================================
# Front matter
# ==========================================================================

A, B = ad.PART_A, ad.PART_B

BRIEFING = Section(
    title="Before you start",
    kicker="What this is, what it is worth, and what is actually being "
           "marked.",
    flow=True,
    footer="Before you start",
    blocks=(
        Para(text=(
            "Chapter 1 says technical analysis does exactly two jobs. "
            "**Identification** is the descriptive job: it records and "
            "describes past and present price and market action. "
            "**Forecasting** is the inferential job: it interprets what was "
            "identified to infer what price might do next."
            "\n\n"
            "The difference between them is the whole of this activity. An "
            "identification can be marked right or wrong, because the record "
            "either says that or it does not. A forecast cannot be marked "
            "right or wrong at the moment you write it, because nobody has "
            "seen what happens next. You will do both, and you will be "
            "marked on them differently."
        )),
        Callout(
            label="Read this twice",
            tone="gold",
            text=(
                "**Your forecast in Part B is not marked right or wrong.** It "
                "is marked on whether the reasons you give are things your "
                "own chart actually shows, and whether your forecast follows "
                "from them. Looking up what the price did next "
                "will not earn you a single mark, and copying it will lose "
                "you the reasoning marks. In the session after this is due "
                "you will be shown what price really did, and the point of "
                "that reveal is not to find out who was lucky."
            ),
        ),
        Callout(
            label="How your written answers are marked",
            text=(
                f"{WRITTEN.disclaimer} The rubric itself, with an answer "
                f"worked at every level, comes straight after the table of "
                f"marks near the end of this sheet."
            ),
        ),
        Points(
            title="What you need",
            items=(
                "Any computer, tablet or phone with a web browser. A borrowed "
                "one is fine.",
                "A free Google account. Nothing to install and nothing to pay "
                "for.",
                "About 90 minutes. Part A takes the longest because every "
                "click is spelled out.",
                "Nothing to print. Every mark you make, on both charts, is "
                "made in the spreadsheet you hand in.",
            ),
        ),
        Para(text=(
            "The activity is built in Google Sheets because the screen looks "
            "the same for everyone, which is what lets this sheet show you a "
            "picture of every step. **Everything you do here transfers to "
            "Microsoft Excel.** The menus sit in different places and the "
            "formulas are identical."
        )),
        Head(text="Where the numbers come from"),
        Para(text=(
            f"Both price series are published by **FRED**, the economic "
            f"database of the Federal Reserve Bank of St. Louis, and both are "
            f"measured by the **{ad.EIA}**. FRED marks them public domain, "
            f"which is why this course can hand them to you rather than ask "
            f"you to hunt for data of your own."
        )),
        Table(
            headers=("", "Part A", "Part B"),
            widths=(24, 38, 38),
            rows=(
                ("What it is", A.name, B.name),
                ("FRED code", A.fred_id, B.fred_id),
                ("Price is measured in", A.unit, B.unit),
                ("First trading day", _d(A.dates[0]), _d(B.dates[0])),
                ("Last trading day", _d(A.dates[-1]), _d(B.dates[-1])),
                ("Trading days", str(A.rows), str(B.rows)),
            ),
            note=(f"Retrieved from FRED on {ad.RETRIEVED}. The only change "
                  f"made to either file was to remove the days the market did "
                  f"not trade, which FRED leaves in the file with the price "
                  f"blank: {A.dropped} of them in Part A and {B.dropped} in "
                  f"Part B, all of them United States public holidays. No "
                  f"price was altered, added or removed."),
        ),
        Callout(
            label="Closing prices only",
            text=(
                "These series carry one price per day, the closing price. "
                "They carry no opening price, no high, no low and no volume, "
                "so this activity never asks you for any of those. Chapter 1 "
                "calls the full set of four **OHLC**, and you will meet it "
                "properly when we get to bar charts."
            ),
        ),
    ),
)


# ==========================================================================
# Part A, fully worked
# ==========================================================================

STEPS_A = (
    Step(
        title="Open a new, empty spreadsheet",
        text=("In your browser's address bar type `sheets.new` and press "
              "Enter. Sign in to your Google account if you are asked to. An "
              "empty spreadsheet opens, called Untitled spreadsheet."),
        shot=Shot(
            name="s01-blank-english", crop=(0, 0, 900, 330),
            caption="An empty Google Sheet. The grid of lettered columns and "
                    "numbered rows is where the prices will land.",
        ),
    ),
    Step(
        title="Make sure your menus are in English",
        text=("Look along the top. It must read File, Edit, View, Insert, "
              "Format, Data, Tools, Extensions, Help. If it reads File, "
              "I-edit, Tingnan, Ipasok, Format, Data, Mga tool, Mga "
              "Extension, Tulong, Google has decided you want Filipino and "
              "the rest of this sheet will not match your screen."),
        then=("To fix it, click at the end of the web address at the very top "
              "of your browser, add `?hl=en` to it, and press Enter. The page "
              "reloads in English. Do this now, before anything else."),
        shot=Shot(
            name="s02-filipino", crop=(0, 0, 700, 62),
            caption="Filipino menus. If your screen looks like this, add "
                    "?hl=en to the web address and reload.",
        ),
    ),
    Step(
        title="Give the file its name",
        text=("Click the words Untitled spreadsheet at the top left, type "
              "`FIN1209 Activity 1` and press Enter. Do not put your own name "
              "in the file name. You write your name on this printed sheet."),
        shot=Shot(
            name="s03-named-blank", crop=(0, 0, 900, 200),
            caption="The file is named. It saves itself, so there is no save "
                    "button to look for.",
        ),
    ),
    Step(
        title="Click cell A1, then type in the formula that fetches the prices",
        text=("Click the very first cell, the one where column A meets row 1. "
              "Then type this, exactly, including every bracket and quotation "
              "mark. It is one line. Do not press Enter yet."),
        type_this=_pull(A, "PartA"),
        then=("`IMPORTRANGE` reaches into the spreadsheet your instructor "
              "shared and copies a block of it into yours. The long string of "
              "letters is that spreadsheet's address. `PartA!A1:B103` is the "
              "part being copied: the tab called PartA, from cell A1 down to "
              f"cell B{A.last_row}."),
        shot=Shot(
            name="s04-formula-typed", crop=(0, 108, 900, 195),
            caption="The formula sits in cell A1 and is repeated in the "
                    "formula bar above the grid. Check it character by "
                    "character before you go on.",
        ),
    ),
    Step(
        title="Press Enter and watch the prices arrive",
        text=(f"Column A fills with dates and column B with prices, "
              f"{A.rows} rows of them. Row 1 holds the headers that came with "
              f"the file: `observation_date` and `{A.fred_id}`, which is "
              f"FRED's own code for this price. Leave them alone. They are "
              f"the proof of where your numbers came from."),
        then=("If instead you see `#REF!`, you have mistyped the long "
              "address. Click A1, compare it character by character with the "
              "box above, and fix it. If a message appears asking you to "
              "connect the two sheets, click Allow access."),
        shot=Shot(
            name="s05-data-loaded", crop=(0, 108, 700, 470),
            caption="Dates down column A, closing prices down column B.",
        ),
    ),
    Step(
        title="Check that all of it arrived",
        text=(f"Click the small white box at the top left that currently says "
              f"A1. That is the Name Box. Type `B{A.last_row}` into it and "
              f"press Enter. The spreadsheet jumps to the last price."),
        then=(f"The Name Box now reads `B{A.last_row}` and the formula bar "
              f"beside it reads `{A.last:.2f}`. Row {A.last_row} shows "
              f"`{A.dates[-1]}`. If yours says anything else, your range is "
              f"wrong. Go back to step 4."),
        shot=Shot(
            name="s06-check-b103", crop=(0, 108, 760, 190),
            caption="The Name Box and the formula bar are how you check any "
                    "cell without hunting for it.",
        ),
    ),
    Step(
        title="Select every date and every price",
        text=(f"Type `{A.data_range}` into the Name Box and press Enter. "
              f"Columns A and B go blue from row 1 to row {A.last_row}. Down "
              f"in the bottom right corner the sheet counts what you have "
              f"selected: 206 cells, which is {A.rows} dates plus {A.rows} "
              f"prices plus the two headers."),
        shot=Shot(
            name="s07-range-selected", crop=(0, 108, 900, 320),
            caption="The Name Box selects a whole block in one move, which is "
                    "faster and far more reliable than dragging.",
        ),
    ),
    Step(
        title="Insert the chart",
        text=("With that block still selected, click **Insert** in the menu "
              "bar and then **Chart**."),
        shot=Shot(
            name="s08-insert-menu", crop=(150, 25, 700, 420), width_pct=62,
            caption="Insert, then Chart.",
        ),
    ),
    Step(
        title="Look at what you have made",
        text=("A chart appears, and a Chart editor panel opens on the right. "
              "Google has already worked out that dates along the bottom and "
              "prices up the side make a line chart, so it has drawn one."),
        then=("This is the object Chapter 1 calls a **price-time chart**: "
              "price on the vertical axis, time on the horizontal axis, one "
              "price line plotted against both. Everything else in this "
              "course is drawn on top of this."),
        shot=Shot(
            name="s09-chart-inserted", crop=(250, 295, 862, 695),
            caption="Your first price-time chart, built from a column of "
                    "numbers you did not type.",
        ),
    ),
    Step(
        title="Open the titling controls",
        text=("In the Chart editor on the right, click **Customize**, then "
              "click **Chart and axis titles** to open it."),
        shot=Shot(
            name="s10-customize-titles", crop=(1100, 128, 1435, 470),
            width_pct=46,
            caption="The Customize tab, with Chart and axis titles open.",
        ),
    ),
    Step(
        title="Title the chart",
        text=("The box under Title text holds Google's guess. Delete it and "
              "type this instead."),
        type_this="Henry Hub natural gas spot price, daily close",
        then=("The title on the chart changes as you type."),
        shot=Shot(
            name="s11-title-set", crop=(1100, 290, 1435, 430), width_pct=62,
            caption="Title text, typed in. Nothing needs saving.",
        ),
    ),
    Step(
        title="Switch from the chart title to the axis titles",
        text=("Click the dropdown that currently says Chart title. Four "
              "choices appear. Choose **Horizontal axis title**, and in the "
              "Title text box type `Time`."),
        shot=Shot(
            name="s12-title-type-dropdown", crop=(1110, 285, 1320, 430),
            width_pct=40,
            caption="The same dropdown gives you the chart title, the "
                    "subtitle and both axis titles.",
        ),
    ),
    Step(
        title="Now name the other axis",
        text=("Open that dropdown again, choose **Vertical axis title**, and "
              "type this into the Title text box."),
        type_this="Price (US dollars per million BTU)",
        then=("Both axes are now named. You have just labelled the two "
              "dimensions of the price-time chart by hand, which is worth "
              "doing once so that you never again look at a chart without "
              "asking what its axes are."),
        shot=Shot(
            name="s13-axis-titles", crop=(250, 295, 862, 695),
            caption="Price up the side, time along the bottom, both labelled.",
        ),
    ),
    Step(
        title="Give the chart a page of its own",
        text=("Click the three dots at the top right corner of the chart "
              "itself, not the editor. Choose **Move to own sheet**."),
        shot=Shot(
            name="s14-move-to-own-sheet", crop=(828, 335, 1035, 570),
            width_pct=40,
            caption="The chart's own menu. Move to own sheet is near the "
                    "bottom.",
        ),
    ),
    Step(
        title="This is your finished chart",
        text=("The chart now fills a tab of its own, called Chart1, and the "
              "tabs along the bottom let you move between it and your "
              "numbers. It is big enough to read at a glance."),
        then=("Leave it on its own tab. It is the chart that is marked for "
              "Part A, and your Part B chart will sit on a tab of its own "
              "the same way."),
        shot=Shot(
            name="s15-chart-own-sheet", crop=(0, 0, 1440, 900),
            caption="The finished Part A chart on its own tab.",
        ),
    ),
    Step(
        title="Go back to the numbers and start a third column",
        text=("Click the **Sheet1** tab at the bottom. Using the Name Box, go "
              "to cell `C1` and type `Daily change`. Then go to cell `C3` and "
              "type this."),
        type_this="=B3-B2",
        then=("C3 now shows how much the price moved between the first day "
              "and the second. C2 stays empty on purpose: the first day has "
              "no day before it to be compared with."),
        shot=Shot(
            name="s16-change-formula", crop=(0, 108, 700, 240),
            caption="One day's change, in one cell.",
        ),
    ),
    Step(
        title="Copy that formula down all the way",
        text=(f"Click C3. Press **Ctrl and C** together to copy it, or "
              f"**Command and C** on a Mac. Then type `C4:C{A.last_row}` into "
              f"the Name Box, press Enter, and press **Ctrl and V**, or "
              f"**Command and V** on a Mac, to paste."),
        then=(f"The spreadsheet adjusts the formula for every row as it "
              f"pastes: C4 becomes `=B4-B3`, C5 becomes `=B5-B4`, and so on "
              f"down to C{A.last_row}. This is the single most useful thing a "
              f"spreadsheet does. Do not use the Edit menu for this: it asks "
              f"you to install an extension. Use the keyboard."),
        shot=Shot(
            name="s17-copy-paste-dialog", crop=(440, 290, 1000, 615),
            width_pct=58,
            caption="What the Edit menu offers instead. If you see this, "
                    "click Cancel and use the keyboard.",
        ),
    ),
    Step(
        title="Check the column filled correctly",
        text=(f"Go to `C{A.last_row}` in the Name Box. The formula bar should "
              f"read `=B{A.last_row}-B{A.last_row - 1}`. Column C is now a "
              f"record of every single day's move, in the same units as the "
              f"price."),
        shot=Shot(
            name="s18-answers", crop=(0, 145, 420, 560),
            width_pct=42,
            caption="Dates, prices and daily changes, side by side.",
        ),
    ),
    Step(
        title="Set up the answer block",
        text=("Go to cell `E1` and type these sixteen labels, pressing Enter "
              "after each one so you move down the column: Trading days, "
              "First close, Last close, Change over the window, Percent "
              "change, Highest close, Date of highest close, Lowest close, "
              "Date of lowest close, Days price rose, Days price fell, Days "
              "price did not move, Biggest one day rise, Date of biggest "
              "rise, Biggest one day fall, Date of biggest fall."),
        then=("They will look as though they spill into column F. They do "
              "not: column F is empty, so the text simply shows across it. "
              "Leave column F alone."),
    ),
    Step(
        title="Type the sixteen formulas",
        text=("Now go to cell `G1` and type the formula from the first row of "
              "the table below. Press Enter, which moves you to G2, and type "
              "the second. Carry on to G16. Every one of them is a question "
              "about the record, and every answer is a fact you could not "
              "argue with."),
        then=("`MAX` and `MIN` find the largest and smallest number in a "
              "block. `COUNT` counts how many numbers are in it. `COUNTIF` "
              "counts only the ones that pass a test. `INDEX` with `MATCH` is "
              "the pair that answers **when**: MATCH finds which row a value "
              "sits on, and INDEX reads the date off that same row."),
        shot=Shot(
            name="s18-answers", crop=(440, 145, 800, 240), width_pct=52,
            caption="The top of your answer block. Check these three against "
                    "your own screen before you type the rest. The other "
                    "thirteen answers are yours to produce.",
        ),
    ),
    Table(
        title="The sixteen formulas, in order, down column G",
        headers=("Cell", "Type this"),
        widths=(12, 88),
        mono_cols=(0, 1),
        rows=tuple(
            (f"G{i}", formula) for i, formula in enumerate((
                f"=COUNT({A.price_range})",
                "=B2",
                f"=B{A.last_row}",
                "=G3-G2",
                "=ROUND(G4/G2*100,2)",
                f"=MAX({A.price_range})",
                f"=INDEX({A.date_range},MATCH(G6,{A.price_range},0))",
                f"=MIN({A.price_range})",
                f"=INDEX({A.date_range},MATCH(G8,{A.price_range},0))",
                f'=COUNTIF({A.change_range},">0")',
                f'=COUNTIF({A.change_range},"<0")',
                f'=COUNTIF({A.change_range},"=0")',
                f"=MAX({A.change_range})",
                f"=INDEX(A3:A{A.last_row},MATCH(G13,{A.change_range},0))",
                f"=MIN({A.change_range})",
                f"=INDEX(A3:A{A.last_row},MATCH(G15,{A.change_range},0))",
            ), start=1)
        ),
        note="Each formula sits beside the label you typed into column E on "
             "the row above, so G1 answers the label in E1.",
    ),
)

# Every identification answer is worth this much, and a part's points are this
# times the number of questions, never a number typed beside it. The published
# version said "sixteen answers, half a mark each" and then gave them six
# marks, which a student would find in a minute. Two points an answer also
# means nothing on this sheet is ever a fraction.
PER_ANSWER = 2


def _identified(questions: tuple[Question, ...]) -> int:
    return len(questions) * PER_ANSWER


_A_QUESTIONS = (
    Question(text="Trading days in the window", cell="G1",
             answer=str(A.rows)),
    Question(text="First close", cell="G2", answer=f"{A.first:.2f}"),
    Question(text="Last close", cell="G3", answer=f"{A.last:.2f}"),
    Question(text="Change over the window", cell="G4",
             answer=f"{A.change:.2f}"),
    Question(text="Percent change", cell="G5",
             answer=f"{A.pct_change:.2f}"),
    Question(text="Highest close", cell="G6", answer=f"{A.high:.2f}"),
    Question(text="Date of the highest close", cell="G7",
             answer=str(A.high_date)),
    Question(text="Lowest close", cell="G8", answer=f"{A.low:.2f}"),
    Question(text="Date of the lowest close", cell="G9",
             answer=str(A.low_date)),
    Question(text="Days price rose", cell="G10", answer=str(A.up_days)),
    Question(text="Days price fell", cell="G11", answer=str(A.down_days)),
    Question(text="Days price did not move", cell="G12",
             answer=str(A.flat_days)),
    Question(text="Biggest one day rise", cell="G13",
             answer=f"{A.biggest_rise:.2f}"),
    Question(text="Date of the biggest rise", cell="G14",
             answer=str(A.biggest_rise_date)),
    Question(text="Biggest one day fall", cell="G15",
             answer=f"{A.biggest_fall:.2f}"),
    Question(text="Date of the biggest fall", cell="G16",
             answer=str(A.biggest_fall_date)),
)

PART_A_QUESTIONS = QuestionSet(
    title="Part A answers: copy them off your own screen",
    intro=("Read each one out of column G of your spreadsheet and write it "
           "here. Give prices to two decimal places and dates as they appear."),
    questions=_A_QUESTIONS,
    key_note=(f"2 points each, {show_marks(_identified(_A_QUESTIONS))} "
              f"in total. The one "
              f"to watch is Days price did not move. {A.flat_days} of the "
              f"{A.rows - 1} changes are exactly zero, so rose plus fell does "
              f"not come to {A.rows - 1}. A student who assumed it would has "
              f"told you they did not read their own column C."),
)

PART_A = Section(
    title="Part A. Build it once, with every click shown",
    kicker=(f"{A.name}, {_d(A.dates[0])} to {_d(A.dates[-1])}. "
            f"Follow the steps in order. Do not skip one because it looks "
            f"obvious."),
    footer="Part A",
    flow=True,
    blocks=STEPS_A + (
        Head(text="What the record says"),
        Para(text=(
            "Every question below is an act of **identification**. Not one of "
            "them is a prediction, an opinion or an interpretation. Each has "
            "exactly one right answer, your spreadsheet has already worked it "
            "out, and your answer will be marked against it."
        )),
        PART_A_QUESTIONS,
        Head(text="One thing to notice before you go on"),
        Para(text=(
            f"Look at your chart again. It is not a trend. Price drifted "
            f"gently for three months, went almost vertical in February, and "
            f"came most of the way back down. From the first day to the last "
            f"it rose {A.pct_change:.0f} percent. At the high on "
            f"{_d(A.high_date)} it had risen "
            f"{(A.high / A.first - 1) * 100:.0f} percent, and it gave almost "
            f"all of that back in seven weeks."
            f"\n\n"
            f"That is worth seeing once. The shape of a chart and the change "
            f"from the first day to the last are different facts, and a chart "
            f"that ends near where it began has not necessarily been quiet. "
            f"Both are identification. Neither is a forecast."
        )),
    ),
)


# ==========================================================================
# Part B, on their own
# ==========================================================================

_B_QUESTIONS = (
    Question(text="Trading days in the window", cell="G1",
             answer=str(B.rows)),
    Question(text="First close", cell="G2", answer=f"{B.first:.2f}"),
    Question(text="Last close", cell="G3", answer=f"{B.last:.2f}"),
    Question(text="Change over the window", cell="G4",
             answer=f"{B.change:.2f}"),
    Question(text="Percent change", cell="G5",
             answer=f"{B.pct_change:.2f}"),
    Question(text="Highest close", cell="G6", answer=f"{B.high:.2f}"),
    Question(text="Date of the highest close", cell="G7",
             answer=str(B.high_date)),
    Question(text="Lowest close", cell="G8", answer=f"{B.low:.2f}"),
    Question(text="Date of the lowest close", cell="G9",
             answer=str(B.low_date)),
    Question(text="Days price rose", cell="G10", answer=str(B.up_days)),
    Question(text="Days price fell", cell="G11", answer=str(B.down_days)),
    Question(text="Days price did not move", cell="G12",
             answer=str(B.flat_days)),
    Question(text="Biggest one day rise", cell="G13",
             answer=f"{B.biggest_rise:.2f}"),
    Question(text="Date of the biggest rise", cell="G14",
             answer=str(B.biggest_rise_date)),
    Question(text="Biggest one day fall", cell="G15",
             answer=f"{B.biggest_fall:.2f}"),
    Question(text="Date of the biggest fall", cell="G16",
             answer=str(B.biggest_fall_date)),
)

PART_B_QUESTIONS = QuestionSet(
    title="Part B answers",
    intro=("The same sixteen questions, about a different market. Read them "
           "off column G of your Part B tab."),
    questions=_B_QUESTIONS,
    key_note=(f"2 points each, {show_marks(_identified(_B_QUESTIONS))} "
              f"in total. Part B "
              f"has no flat days at all, so G12 is {B.flat_days} and rose "
              f"plus fell does come to {B.rows - 1} this time. A student who "
              f"wrote {A.flat_days} here has copied their Part A answer."),
)

PART_B_SECTION = Section(
    title="Part B. Now do it yourself",
    kicker=(f"{B.name}, {_d(B.dates[0])} to {_d(B.dates[-1])}. "
            f"The same build, the same sixteen questions, no pictures."),
    footer="Part B",
    flow=True,
    blocks=(
        Para(text=(
            "This is a different market: crude oil rather than natural gas, "
            "priced in dollars a barrel rather than dollars a million BTU. "
            "The method does not change at all, which is the point of doing "
            "it twice."
        )),
        TypeBox(
            intro="This is the formula for step 2 below. It is the Part A "
                  "formula with one word and two row numbers changed.",
            text=_pull(B, "PartB"),
        ),
        Points(
            title="Build it",
            numbered=True,
            items=(
                "In the same spreadsheet, click the plus sign at the bottom "
                "left to add a new tab. It appears as Sheet2.",
                "Click cell A1 of the new tab and type the formula in the "
                "box above.",
                f"Check cell B{B.last_row}. It should read "
                f"{B.last:.2f}, on {B.dates[-1]}.",
                f"Select {B.data_range} with the Name Box, then Insert and "
                f"Chart. Title it, name both axes, and move it to its own "
                f"sheet, exactly as in steps 10 to 15. The vertical axis is "
                f"`Price (US dollars per barrel)` this time.",
                f"Build column C the same way: `Daily change` in C1, `=B3-B2` "
                f"in C3, copied down to C{B.last_row}.",
                f"Build the same sixteen labels in column E and the same "
                f"sixteen formulas in column G, changing every 103 to "
                f"{B.last_row} and every 102 to {B.rows}.",
            ),
        ),
        PART_B_QUESTIONS,
        Head(text="Mark the peaks and the troughs"),
        Para(text=(
            "Look at your Part B chart and find every point where the price "
            "line turned. A **peak** is a point with lower prices on both "
            "sides of it. A **trough** is a point with higher prices on both "
            "sides. You mark them in two new columns of your Part B tab."
            "\n\n"
            "Type `Peaks` in cell H1 and `Troughs` in cell I1. For each peak, "
            "find its date in column A and type `=B` and that row number into "
            "column H of the same row, so a peak in row 50 gets `=B50` in "
            "H50. Do the same for each trough in column I. Every other row of "
            "both columns stays empty. The chart shows them once you add them "
            "to it, below."
            "\n\n"
            "Chapter 1 gives the most widely accepted definition of a trend "
            "as **successively higher or lower peaks and troughs**. You now "
            "have the marks to test that definition against, so answer the "
            "two questions below from your own marks."
        )),
        Lines(
            count=2,
            title="Are your troughs getting higher, lower, or neither?",
        ),
        Lines(
            count=2,
            title="Are your peaks getting higher, lower, or neither?",
        ),
        Callout(
            label="Expect to disagree",
            text=(
                "The person beside you will not mark the same peaks and "
                "troughs you did, and neither of you will have made a "
                "mistake. Chapter 1 calls that **subjectivity**: two "
                "competent analysts, given the same chart, reaching different "
                "and equally defensible conclusions. You met it in class with "
                "the book's USDCAD chart. Here it is again, in your own "
                "marks."
            ),
        ),
        Head(text="Draw one trendline"),
        Para(text=(
            "Choose **one** straight line that touches at least two of your "
            "troughs and that no part of the price line drops below between "
            "them. You build it as a formula in column J of your Part B tab, "
            "then extend it past the right hand edge of the chart, into the "
            "empty space where the future would be."
            "\n\n"
            "Type `Trendline` in cell J1. Find the row numbers of the two "
            "troughs your line rests on. The formula below is written for "
            "troughs in rows 2 and 104. Type it into column J in the row of "
            "your first trough, with your first row number in place of every "
            "2 and your second row number in place of every 104."
        )),
        TypeBox(
            label="The pattern, written for rows 2 and 104",
            text="=$B$2+($B$104-$B$2)*($A2-$A$2)/($A$104-$A$2)",
        ),
        Para(text=(
            "Leave `$A2` in the middle without a dollar sign before its 2: "
            "that is what moves the line along as you copy it down."
            "\n\n"
            f"Now extend it. In cell A{B.last_row + 1}, type `2014-07-30`, "
            f"one month after the chart ends, and leave B{B.last_row + 1} "
            f"empty. Copy your formula from column J down to "
            f"J{B.last_row + 1}. J{B.last_row + 1} is the price your line "
            f"sits at one month after the chart ends."
        )),
        Head(text="Put your marks on the chart"),
        Points(
            numbered=True,
            items=(
                f"Open your Part B chart and click **Edit chart**. Under "
                f"Setup, change the last number in the Data range from "
                f"{B.last_row} to {B.last_row + 1}, unless Google has already "
                f"done it for you. That gives the chart room past the last "
                f"price for your line to run into.",
                f"Under Series, click **Add Series**, then the small grid "
                f"icon. Type your Part B tab's name, an exclamation mark and "
                f"`H1:H{B.last_row + 1}`, and click OK. On a tab called "
                f"Sheet2 that is `Sheet2!H1:H{B.last_row + 1}`. A name with a "
                f"space goes in single quotes, as in "
                f"`'Part B'!H1:H{B.last_row + 1}`.",
                f"Do the same twice more, for `I1:I{B.last_row + 1}` and "
                f"`J1:J{B.last_row + 1}`.",
                "Click **Customize**, then **Series**. Choose Peaks and set "
                "Point size to 7px. Choose Troughs and set Point size to 7px "
                "as well. Your peaks, your troughs and your line are now on "
                "the chart, and the line runs on past the last price.",
            ),
        ),
        Lines(
            count=2,
            title=f"The two dates your line touches, and where it sits one "
                  f"month after the chart ends (cell J{B.last_row + 1})",
        ),
        Head(text="Now, and only now, forecast"),
        Para(text=(
            "Everything up to this point has been identification. This part "
            "is not. Write a short paragraph saying what you think the price "
            "does next, and why."
            "\n\n"
            "**You are marked on the reasons, not on the answer.** A forecast "
            "that turns out wrong and is argued from what your chart shows "
            "earns full marks. A forecast that turns out right with no "
            "reasons earns nothing. Say which way you think price goes, name "
            "the marks on your own chart that make you think so, and say why "
            "they point that way. The best answers also name one thing on "
            "the chart that argues against them. Nobody loses a mark for "
            "leaving it out."
        )),
        Lines(count=11),
    ),
)


# ==========================================================================
# The platform step, and handing in
# ==========================================================================

PLATFORM_SECTION = Section(
    title="Last step. Five minutes on a real charting platform",
    kicker="Because the department's version of this homework asks for one, "
           "and because you should see one before the next chapter.",
    footer="The platform step",
    flow=True,
    blocks=(
        Para(text=(
            f"A spreadsheet is where you learn what a chart is made of. A "
            f"charting platform is where the work is actually done. Open one, "
            f"find a chart, draw a line on it, and stop."
        )),
        Points(
            numbered=True,
            items=(
                f"Go to `{PLATFORM_URL}`. It is free and you do not have to "
                f"sign in to draw on a chart.",
                "Click the symbol name at the top left and search for any "
                "market you like. A share, a currency pair, gold, oil, "
                "anything.",
                "Set the timeframe to daily using the D button at the top, "
                "and pick a stretch of chart where price clearly went one "
                f"way for a while.",
                f"On the toolbar down the left hand side, the second button "
                f"from the top is the **Trendline** tool. Click it, then "
                f"click once at one end of your line and once at the other.",
                "Take a screenshot of the result with your line on it.",
            ),
        ),
        Callout(
            label="One sentence, underneath",
            text=(
                "Write one sentence saying what your line touches and what "
                "would have to happen for price to break it. That sentence is "
                "what the mark is for. The screenshot is what lets anyone "
                "check it."
            ),
        ),
        Lines(count=2, title="Your one sentence"),
    ),
)

# The four marks no record can check, and what the course's written-answer
# rubric (build/rubric.py) looks for in each. `means` follows the rubric's own
# order of marked criteria: grounded, then connected.
TRENDLINE_MARK = Applied(
    what="Peaks, troughs and one trendline",
    out_of=8,
    means=(
        "Your marks in columns H and I sit on real turning points of your own "
        "Part B chart, and your line rests on two of your own troughs with no "
        "part of the price line below it between them.",
        "Your answers to the two questions, higher, lower or neither, follow "
        "from the marks you made, and the price you give for one month on is "
        "where your own line reaches.",
    ),
)
FORECAST_MARK = Applied(
    what="The forecast",
    out_of=4,
    means=(
        "Your reasons are things anyone could find on your own Part B chart: "
        "a price, a date, a shape.",
        "The direction you forecast follows from those reasons. Whether price "
        "really went that way is never marked.",
    ),
)
PLATFORM_MARK = Applied(
    what="The platform step",
    out_of=4,
    means=(
        "Your sentence names what your line touches, on the chart in your "
        "screenshot.",
        "What you say would have to happen for price to break the line "
        "follows from where you drew it.",
    ),
)
WRITTEN_MARKS = (TRENDLINE_MARK, FORECAST_MARK, PLATFORM_MARK)

# The rubric, as data, so the sheet cannot claim a total it does not add up
# to. The last field says whether those marks are checkable against the
# record, which is the distinction the whole activity is about.
RUBRIC = (
    ("Part A, built", 10,
     "The chart exists, has a title and two named axes, and the prices are "
     "the right ones.", True),
    ("Part A, identified", _identified(_A_QUESTIONS),
     "Sixteen answers, 2 points each. Right or wrong against the record.",
     True),
    ("Part B, built", 10,
     "The same, done without the pictures.", True),
    ("Part B, identified", _identified(_B_QUESTIONS),
     "The same sixteen questions, 2 points each.", True),
    (TRENDLINE_MARK.what, TRENDLINE_MARK.out_of,
     "Marked in the Peaks and Troughs columns of your Part B tab. One "
     "trendline, built as its own series on your Part B chart, that touches "
     "at least two troughs and is extended past the last price. Marked with "
     "the written-answer rubric.", False),
    (FORECAST_MARK.what, FORECAST_MARK.out_of,
     "What you think price does next, and why, argued from your own chart. "
     "Marked with the written-answer rubric. Never marked right or wrong.",
     False),
    (PLATFORM_MARK.what, PLATFORM_MARK.out_of,
     "A screenshot of a chart you found, with a trendline you drew, and one "
     "sentence about it. The sentence is marked with the written-answer "
     "rubric.", False),
)
TOTAL = sum(m for _, m, _, _ in RUBRIC)

if ({what for what, _, _, checkable in RUBRIC if not checkable}
        != {a.what for a in WRITTEN_MARKS}):
    raise ValueError("every mark the record cannot check must be one the "
                     "written-answer rubric decides, and the other way round")


HANDIN = Section(
    title="What to hand in, and how it is marked",
    footer="Handing in",
    flow=True,
    blocks=(
        Points(
            title="Four things, in one submission",
            numbered=True,
            items=(
                "This sheet, filled in, with your name on the front.",
                "Your Part A chart and your Part B chart, each on a tab of "
                "its own, with your peaks, your troughs and your one "
                "trendline added to the Part B one.",
                "The link to your spreadsheet, or a screenshot of your Part B "
                "tab showing columns A to G.",
                f"Your {PLATFORM} screenshot with its one sentence.",
            ),
        ),
        Table(
            title=f"The {show_marks(TOTAL)} points",
            headers=("What", "Points", "What earns them"),
            widths=(30, 12, 58),
            rows=tuple((what, show_marks(marks), how)
                       for what, marks, how, _ in RUBRIC),
            note=(f"{show_marks(TOTAL)} in total. "
                  f"{show_marks(sum(m for _, m, _, c in RUBRIC if c))} of "
                  f"them are for work that can be marked right or wrong "
                  f"against the record. "
                  f"{show_marks(sum(m for _, m, _, c in RUBRIC if not c))} "
                  f"are not, and those are marked on the reasoning, with the "
                  f"written-answer rubric in the next section."),
        ),
        Callout(
            label="What happens next",
            tone="gold",
            text=(
                "The Part B window stops on a day chosen before you were "
                "given it, and the price kept going after that day. In the "
                "session after this is due you will be shown exactly what it "
                "did. Your identification answers will be marked right or "
                "wrong. Your forecast will only be compared. That difference "
                "is the whole of Chapter 1's dual function, and it is why "
                "this activity exists."
            ),
        ),
    ),
)


# ==========================================================================
# The written-answer rubric, printed from build/rubric.py
#
# Only two things here are this activity's own: which marks the rubric
# decides, above, and the worked examples below. The examples are set on the
# Part A chart on purpose. A full-marks forecast written on Part B would be a
# model answer to the one question every student is marked on, and a student
# could copy it. Part A asks for no forecast, so nothing here answers anything
# that is marked.
# ==========================================================================

_T1, _T2, _T3 = "2014-02-13", "2014-02-27", "2014-03-21"   # three troughs
_P = "2014-03-04"          # the highest close after the February high


def _at(iso: str) -> str:
    return f"{A.on(iso):.2f} on {_dm(iso)}"


_FULL = (f"Down. Each trough since the February spike is lower than the one "
         f"before it: {_at(_T1)}, {_at(_T2)}, {_at(_T3)}. The best close "
         f"after the spike, {_at(_P)}, stayed below the February high. Lower "
         f"troughs and a lower peak since the spike fit Chapter 1's "
         f"definition of a trend, pointing down, so I expect the next trough "
         f"to be lower again.")

WORKED = (
    Worked(
        level="Full",
        answer=_FULL,
        why=("Grounded: three troughs and a peak, each with a date and a "
             "price anyone can find on the chart. Connected: lower troughs "
             "under a lower peak is exactly what the conclusion says. It "
             "names nothing that argues against it, and loses nothing for "
             "that."),
    ),
    Worked(
        level="Partial",
        answer=("Down. Since the big spike in February the chart has looked "
                "weak and the lows keep sliding, so I expect the fall to "
                "carry on."),
        why=("The conclusion follows, but the evidence is vague. Which lows, "
             "on what dates, at what prices? Nobody can find \"looked weak\" "
             "on a chart."),
    ),
    Worked(
        level="Partial",
        answer=(f"Down, and below 3.00 by June. Each trough since the "
                f"February spike is lower than the one before it: "
                f"{_at(_T1)}, {_at(_T2)}, {_at(_T3)}."),
        why=("The evidence is precise and it supports down. Nothing named "
             "supports 3.00, or June, so the conclusion goes further than "
             "the evidence does."),
    ),
    Worked(
        level="Minimal",
        answer="Down. Whatever goes up must come down.",
        why=("There is a reason, but a general one. It would be the same "
             "sentence under any chart ever drawn, so nothing in it comes "
             "from this one."),
    ),
    Worked(
        level="None",
        answer="Down.",
        why=("A conclusion with no reasoning. It could turn out right, and "
             "it would still earn nothing."),
    ),
)

# The examples make claims about the record, so the record is asked. A
# change to the price files that made one of them false stops the build.
if not A.on(_T1) > A.on(_T2) > A.on(_T3):
    raise ValueError("the worked examples say the three troughs fall, and "
                     "they do not")
if (max(A.closes[A.dates.index(A.high_date) + 1:]) != A.on(_P)
        or A.on(_P) >= A.high):
    raise ValueError("the worked examples name the wrong best close after "
                     "the February high")
if min(A.closes[A.dates.index(dt.date.fromisoformat(_T3)) + 1:]) <= A.on(_T3):
    raise ValueError("the honest sentence says every later close is above "
                     "the last trough, and the data says otherwise")

HONEST = (
    f"The Full answer, with one more sentence: \"Against me, every close "
    f"since {_dm(_T3)} has been above {A.on(_T3):.2f}, so a higher trough "
    f"could be forming there.\" It earns exactly the same marks as the Full "
    f"answer, because honesty is never marked. It is still the better "
    f"answer, and it is the kind this course wants you to learn to write."
)

RUBRIC_SECTION = Section(
    title=WRITTEN.title,
    kicker=(f"For the {show_marks(sum(a.out_of for a in WRITTEN_MARKS))} "
            f"points on this sheet that no record can check. The same rubric "
            f"marks every written answer in this course."),
    footer="The written-answer rubric",
    # Not flowed: the rubric opens a sheet of its own, so its disclaimer is
    # the first thing on a page and the two pages can be read on their own.
    blocks=written_rubric(
        WRITTEN,
        applied=WRITTEN_MARKS,
        question=(
            f"Suppose Part A had asked for a forecast: what does its price do "
            f"after {_d(A.dates[-1])}, and why? Here are five answers, one at "
            f"each level and two at Partial, because there are two ways to be "
            f"partial. They are written on your Part A chart, not your Part B "
            f"one, so that none of them is an answer to anything you are "
            f"marked on."
        ),
        worked=WORKED,
        honest=HONEST,
    ),
)


# ==========================================================================
# The answer key, which only the instructor's build carries
# ==========================================================================

_TL = ad.trendline_facts()
_LINE_A, _LINE_B = _TL[0], _TL[1]


def _swing_rows():
    return tuple((kind.title(), str(day), f"{price:.2f}")
                 for kind, day, price in B.swings())


def _swing_list(kind: str) -> str:
    return ", ".join(f"{price:.2f}"
                     for k, _, price in B.swings() if k == kind)


def _swings_after(kind: str, when: str) -> str:
    import datetime as _dt
    cut = _dt.date.fromisoformat(when)
    return ", ".join(f"{price:.2f}" for k, day, price in B.swings()
                     if k == kind and day >= cut)


REVEAL_SECTION = Section(
    title="The reveal, and how to run it",
    kicker="Instructor's copy. Do not hand this page out before the answers "
           "are collected.",
    footer="The reveal",
    flow=True,
    blocks=(
        Para(text=(
            f"The Part B window stops on {_d(B.dates[-1])} at "
            f"{B.last:.2f} dollars a barrel. Over those {B.rows} trading days "
            f"price rose {B.pct_change:.1f} percent, made its high of "
            f"{B.high:.2f} "
            f"{_trading_days_between(B, B.high_date, B.dates[-1])} trading "
            f"days before the end, and finished "
            f"{B.high - B.last:.2f} below it. From the March low onwards its "
            f"peaks and its troughs both climb, which is the chapter's own "
            f"definition of a trend, and on the last day of the window that "
            f"uptrend is still intact."
            f"\n\n"
            f"That is why the window ends there. A student reading it "
            f"honestly has two defensible forecasts available: the uptrend "
            f"continues, or the failure at {B.high:.2f} was the top. Most "
            f"will choose the first, because the picture in front of them "
            f"looks strong."
        )),
        Figure(
            path=None,          # filled in by the build
            caption=(f"What price actually did. Green is the {B.rows} days "
                     f"the students analysed. Gold is the "
                     f"{ad.REVEAL.rows} trading days after it, to "
                     f"{_d(ad.REVEAL.dates[-1])}."),
            credit="",
            height_mm=86.0,
        ),
        Para(text=(
            f"Price fell from {B.last:.2f} to {ad.REVEAL.low:.2f} by "
            f"{_d(ad.REVEAL.low_date)}, a fall of "
            f"{abs((ad.REVEAL.low - B.last) / B.last * 100):.0f} percent in "
            f"under nine months. The single worst day was "
            f"{_d(ad.REVEAL.biggest_fall_date)}, "
            f"{ad.REVEAL.biggest_fall:.2f} dollars in one session."
            f"\n\n"
            f"**Say this out loud, because it is the lesson.** Every "
            f"identification answer on this sheet was right on the day it was "
            f"written, and is still right today. Every forecast, including "
            f"the ones that turned out lucky, was an opinion when it was "
            f"written and could not have been marked. The record and the "
            f"claim are different objects. That is the dual function."
        )),
        Head(text="The trendline, and the two answers to it"),
        Para(text=(
            f"Line {_LINE_A['name']}, {_LINE_A['label']}, joins the trough of "
            f"{_d(_LINE_A['first'])} at {_LINE_A['first_price']:.2f} to the "
            f"trough of {_d(_LINE_A['second'])} at "
            f"{_LINE_A['second_price']:.2f}. No close in the whole window "
            f"sits below it. Extended, it was broken on "
            f"{_d(_LINE_A['broke_on'])}, when price closed at "
            f"{_LINE_A['broke_at']:.2f} against a line sitting at "
            f"{_LINE_A['line_at']:.2f}."
            f"\n\n"
            f"Line {_LINE_B['name']}, {_LINE_B['label']}, joins the trough of "
            f"{_d(_LINE_B['first'])} at {_LINE_B['first_price']:.2f} to the "
            f"trough of {_d(_LINE_B['second'])} at "
            f"{_LINE_B['second_price']:.2f}. It grazes the close of 5 June by "
            f"four cents, which on a printed chart is inside the thickness of "
            f"a pencil. It was broken on {_d(_LINE_B['broke_on'])}, the very "
            f"first trading day after the window closes, at "
            f"{_LINE_B['broke_at']:.2f}."
        )),
        Figure(
            path=None,
            caption=(f"Two honest lines under the same troughs, calling the "
                     f"reversal "
                     f"{(_LINE_A['broke_on'] - _LINE_B['broke_on']).days} days "
                     f"and "
                     f"{_LINE_B['broke_at'] - _LINE_A['broke_at']:.2f} dollars "
                     f"apart. This is the chapter's Figure 1.20, happening to "
                     f"real prices."),
            credit="",
            height_mm=86.0,
        ),
        Callout(
            label="How to mark a trendline",
            text=(
                "Mark this row with the written-answer rubric. For the line, "
                "grounded means it touches at least two troughs, has no close "
                "below it between them, and is extended past the right hand "
                "edge, and any line that does all three meets it. **Do not "
                "mark a line down for "
                "being a different line from the two above.** A student who "
                "drew line B and called the reversal on 1 July was reading "
                "the same chart as a student who drew line A and called it on "
                "11 July. Saying one of them is wrong teaches the opposite of "
                "Part 4."
            ),
        ),
        Head(text="Peaks and troughs, one defensible reading"),
        Para(text=(
            "Marked by rule rather than by eye: a point that is the highest "
            "or lowest close of the eleven days centred on it. Students "
            "working by eye will produce fewer marks than this and will miss "
            "the shallow ones. That is expected and is not an error."
        )),
        Table(
            headers=("", "Date", "Close"),
            widths=(18, 40, 42),
            rows=_swing_rows(),
            note=(f"Troughs in order: {_swing_list('trough')}. Peaks in "
                  f"order: {_swing_list('peak')}. Neither sequence is tidy "
                  f"and the key should not pretend it is: the very first "
                  f"trough is the second highest of the six, and two in the "
                  f"middle are six cents apart. What is true, and what a "
                  f"student can defend, is that from the March low onwards "
                  f"both climb: troughs "
                  f"{_swings_after('trough', '2014-03-12')} and peaks "
                  f"{_swings_after('peak', '2014-03-12')}. That is the "
                  f"chapter's definition of a trend behaving the way "
                  f"definitions behave in a real market, which is roughly "
                  f"rather than exactly."),
        ),
        Head(text="Running the reveal in class"),
        Points(
            numbered=True,
            items=(
                "Collect the sheets first. Nothing works if anyone can still "
                "change an answer.",
                "Put the Part B chart up as they last saw it, ending on "
                f"{_d(B.dates[-1])}. Ask for a show of hands: who forecast "
                "up, who forecast down.",
                "Ask two students from each side to give one reason. Write "
                "both reasons on the board without judging either.",
                "Now show the first chart above. Wait. Do not talk over it.",
                "Ask the students who forecast down whether they were right "
                "or lucky, and make them answer honestly. Most will say "
                "lucky, and they will be correct.",
                "Show the second chart. Ask who drew line A and who drew line "
                "B, then give both groups the same marks in front of "
                "everybody.",
                "Close on the sentence: the identification half of this sheet "
                "was markable the day you wrote it, and the forecast half "
                "still is not.",
            ),
        ),
        Head(text="If a student is stuck"),
        Table(
            headers=("What they report", "What it is", "What to tell them"),
            widths=(26, 30, 44),
            rows=(
                ("`#REF!` in cell A1", "A mistyped spreadsheet address, or "
                 "the sharing was turned off",
                 "Have them retype the formula from the sheet. If several "
                 "students report it at once, check the source spreadsheet is "
                 "still shared to anyone with the link as a viewer."),
                ("A box asking to connect the sheets",
                 "Normal on some accounts", "Click Allow access once."),
                ("The menus are in Filipino", "Google guessing from location",
                 "Add `?hl=en` to the end of the web address and reload. "
                 "Step 2."),
                ("Edit, then Copy, asks to install something",
                 "Browsers do not let a web page read the clipboard from a "
                 "menu", "Use Ctrl and C, or Command and C. Step 17."),
                ("The chart is a bar chart, not a line",
                 "They selected the wrong block",
                 f"Reselect {A.data_range} with the Name Box and insert the "
                 f"chart again."),
            ),
        ),
    ),
)


# ==========================================================================
# The document
# ==========================================================================

ACTIVITY = Activity(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 1",
    title="Activity 1: Reading a Price Chart",
    subtitle="Build two price-time charts from real market data, identify "
             "what the record says, and then forecast what it does not.",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    points=TOTAL,
    duration="about 90 minutes",
    replaces="Homework 1, Charting Exercises",
    source_note=(f"Price data from FRED, Federal Reserve Bank of St. Louis, "
                 f"series {A.fred_id} and {B.fred_id}, both sourced from the "
                 f"{ad.EIA} and both in the public domain. Retrieved "
                 f"{ad.RETRIEVED}."),
    sections=(BRIEFING, PART_A, PART_B_SECTION, PLATFORM_SECTION, HANDIN,
              RUBRIC_SECTION),
    key_sections=(REVEAL_SECTION,),
)
