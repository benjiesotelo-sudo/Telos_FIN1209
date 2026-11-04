"""Chapter 7, Activity 2: First Automation FIN1209. The handout's content.

Data about the activity, not drawing code; build/activitykit.py draws it. Three
things are computed rather than typed so they cannot drift:

* the running script's stages come from build/activity_chapter07_code.py, and
  the last one is the committed example script itself;
* what R printed at each stage is read from the file build/run_stages.py wrote
  after really running every stage;
* the marks are added up here, and the build stops if they are not 100.

The rule is Lim's Williams' Oops, quoted from the Chapter 7 student edition
built from origin/main (slides 194 to 201). Where the slides leave something
open, the guide says so and calls the choice the student's own.
"""

from __future__ import annotations

import json
from pathlib import Path

from activitykit import (Activity, Applied, Callout, Code, Figure, Head, Para, Points,
                         Section, Shot, Step, Table, TypeBox, Worked,
                         show_marks, written_rubric)
from activity_chapter07_code import STAGES
from rubric import WRITTEN

REPO = Path(__file__).resolve().parent.parent
STUDENT = REPO / "chapter-07" / "activity" / "First Automation FIN1209"
SCRIPT_FILE = STUDENT / "First Automation FIN1209 - Example Script.R"
STAGE_OUTPUTS = REPO / "build" / "generated" / "activity2" / "stage_outputs.json"

NAME = "First Automation FIN1209"
SCRIPT_NAME = "First Automation FIN1209 - Example Script.R"
FLOW_NAME = "First Automation FIN1209 - Example Flowchart"

# --------------------------------------------------------------------------
# The marks, in one place
# --------------------------------------------------------------------------

CHECKABLE = (
    ("The script runs", 10,
     "On a folder of files you have never seen, with no changes and no "
     "installs, in under 60 seconds."),
    ("It writes the files the contract names", 10,
     "`output/signals.csv` with the required columns (5), and one "
     "`output/<ticker>.png` for every input file (5)."),
    ("It finds the right signals", 20,
     "The ticker, date and side of every signal match the record, with none "
     "missing and none extra."),
    ("It gets the prices right", 10,
     "Entry and stoploss match the record, to the cent."),
    ("The chart shows them", 10,
     "Each chart is a real chart with every signal marked and numbered."),
)
JUDGED = (
    ("The flowchart is correct BPMN", 10),
    ("The flowchart matches your script", 15),
    ("The flowchart explains each step", 15),
)
CHECK_TOTAL = sum(m for _, m, _ in CHECKABLE)
JUDGE_TOTAL = sum(m for _, m in JUDGED)
TOTAL = CHECK_TOTAL + JUDGE_TOTAL
assert TOTAL == 100, TOTAL


# --------------------------------------------------------------------------
# Helpers that keep the guide true to the script
# --------------------------------------------------------------------------


def _script_lines() -> list[str]:
    return SCRIPT_FILE.read_text(encoding="utf-8").splitlines()


def _span(start: str, end: str | None = None, after: int = 0) -> str:
    """'lines a to b' of the example script, found by text, not typed."""
    lines = _script_lines()
    a = next(i for i, ln in enumerate(lines) if i >= after and start in ln)
    b = a
    if end is not None:
        # "=}" means a line that is exactly "}" (the end of a function)
        hit = ((lambda ln: ln.rstrip() == end[1:]) if end.startswith("=")
               else (lambda ln: end in ln))
        b = next(i for i, ln in enumerate(lines) if i >= a and hit(ln))
    return f"line {a + 1}" if a == b else f"lines {a + 1} to {b + 1}"


def _after(text: str) -> int:
    return next(i for i, ln in enumerate(_script_lines()) if text in ln)


def _stage_code(stage, fills: dict) -> str:
    if stage.code == "":
        return SCRIPT_FILE.read_text(encoding="utf-8").rstrip("\n")
    out = stage.code
    for k, v in fills.items():
        out = out.replace("{" + k + "}", str(v))
    return out


def _new_lines(prev: str, cur: str) -> tuple[int, ...]:
    """1-based lines of `cur` whose text (ignoring indentation) is not in
    `prev`. Comments and blank lines are never highlighted."""
    seen: dict[str, int] = {}
    for ln in prev.splitlines():
        t = ln.strip()
        seen[t] = seen.get(t, 0) + 1
    new = []
    for n, ln in enumerate(cur.splitlines(), 1):
        t = ln.strip()
        if not t or t.startswith("#"):
            continue
        if seen.get(t, 0) > 0:
            seen[t] -= 1
        else:
            new.append(n)
    return tuple(new)


def _outputs() -> dict:
    try:
        return json.loads(STAGE_OUTPUTS.read_text(encoding="utf-8"))
    except OSError:
        return {}


def basics_blocks(fills: dict) -> tuple:
    outs = _outputs()
    blocks = []
    prev = ""
    for n, st in enumerate(STAGES, 1):
        code = _stage_code(st, fills)
        marker = "" if st.key in outs else "(output appears after the real run)"
        out = outs.get(st.key, marker)
        # Stages that print nothing (the chart ones) say what to look at.
        blocks.append(Head(text=st.title, number=f"B{n}"))
        blocks.append(Para(text=st.text))
        blocks.append(Code(lines=tuple(code.splitlines()),
                           new=_new_lines(prev, code), output=out,
                           label=f"The script so far, step B{n}"))
        png = STAGE_OUTPUTS.parent / f"stage-{st.key}.png"
        if st.key in ("plot", "marks") and png.is_file():
            blocks.append(Figure(
                path=png, height_mm=70.0,
                caption=("What `output/KO.png` looks like after step "
                         f"B{n}."),
                credit="Drawn by this script from the start-here KO price file."))
        if st.after:
            blocks.append(Para(text=st.after))
        prev = code
    return tuple(blocks)


# --------------------------------------------------------------------------
# What this is
# --------------------------------------------------------------------------

BRIEF = Section(
    title="What you are making",
    kicker="Read this page first. It is short.",
    footer="What you are making",
    flow=True,
    blocks=(
        Para(text=(
            "A **trading rule** is a rule that says exactly when to buy or "
            "sell and at what price. In Chapter 7 you met several whose "
            "prices are exact. In this activity you teach a computer one of "
            "them. You will write a small **R script**: you drop price files "
            "into a folder, run the script, and it tells you where the rule "
            "says to buy or sell, writes the signals into a table, and draws "
            "a chart with each signal marked. Add new prices, run it again, "
            "and the table and the chart are updated. That is **automation**: "
            "the rule is applied the same way every time without you "
            "re-reading the chart by eye.")),
        Callout(label="You do not need to know R", tone="gold", text=(
            "Nobody in this class was taught to code, and you are not "
            "expected to know how. Part 4 teaches the R you need, one idea at "
            "a time, using the very script you will run. Part 5 runs it with "
            "a picture of every step. You only start your own script in "
            "Part 7, when you have seen all of this work.")),
        Table(
            title="What you hand in",
            headers=("File", "What it is"),
            widths=(46, 54),
            rows=(
                ("Your R script", "One `.R` file that follows the contract in Part 7."),
                ("Your flowchart", "A picture of how your script works, as a "
                 "BPMN diagram in a PDF (best), a `.bpmn` file, or a Markdown "
                 "file with a Mermaid flowchart."),
            ),
        ),
        Table(
            title="What is in this folder",
            headers=("File", "What it is"),
            widths=(46, 54),
            rows=(
                (f"{NAME}.pdf", "This handout."),
                (SCRIPT_NAME, "The finished example script. It works."),
                (f"{FLOW_NAME}.pdf / .bpmn", "The example's flowchart, as a "
                 "picture and as a file you can open and edit."),
                ("data (start here), data (October update)",
                 "Price files for the example, KO and F. The second set is "
                 "the same two stocks with a month of new rows."),
                (f"{NAME}.mp4 and a narration script", "A video of Part 5, "
                 "if the video is in the folder."),
            ),
        ),
        Callout(label="What these signals are", text=(
            "The output is **the signals of one rule, applied to past "
            "prices**. It is not investment advice and it does not say what "
            "price will do next. Chapter 1's point still holds: a forecast "
            "cannot be checked when it is made, so a signal is only a "
            "statement of what the rule says at that moment."),),
        Para(text=(
            "**Later.** This is the first of two pieces. Later in the "
            "semester a bigger version comes, and you may be grouped for it. "
            "Everything you build here is the start of that.")),
    ),
)

# --------------------------------------------------------------------------
# 1 Install
# --------------------------------------------------------------------------

INSTALL = Section(
    title="1. What to install",
    kicker="Free, and about 30 minutes. If you cannot install, use the "
           "browser option.",
    footer="Install",
    blocks=(
        Para(text=(
            "You need two programs. **R** is the language, and it does the "
            "work. **RStudio Desktop** is a friendly window for writing and "
            "running R. Install R first, then RStudio.")),
        Callout(label="No R packages", text=(
            "The example needs **no packages at all**. It uses only what "
            "comes with R. You never type `install.packages`. Your own "
            "script should not need one either, because the marker's "
            "computer will not have it.")),
        Head(text="Windows", number="W"),
        Points(numbered=True, items=(
            "Go to **https://cran.r-project.org/bin/windows/base/** and "
            "click the **Download R** link at the top. Open the file you "
            "downloaded and click Next through the installer, keeping every "
            "default.",
            "Go to **https://posit.co/download/rstudio-desktop/**, scroll to "
            "the list, and download the **Windows** installer. Open it and "
            "click Next through the installer.",
            "Open **RStudio** from the Start menu. A window opens with a "
            "pane called Console on the left. That is where R talks.",
        )),
        Head(text="Mac", number="M"),
        Points(numbered=True, items=(
            "Go to **https://cran.r-project.org/bin/macosx/**. Click the "
            "first `.pkg` under the latest release, the one for your chip "
            "(the Apple icon, then About This Mac, tells you whether it is "
            "Apple silicon or Intel). Open the file and click Continue "
            "through the installer.",
            "Go to **https://posit.co/download/rstudio-desktop/**, download "
            "the **macOS** installer, open it, and drag RStudio into the "
            "Applications folder.",
            "Open **RStudio** from Applications. A window opens with a pane "
            "called Console on the left.",
        )),
        Head(text="If you cannot install anything", number="C"),
        Para(text=(
            "Use **Posit Cloud**, which runs RStudio in your browser. Go to "
            "**https://posit.cloud**, make a free account, then **New "
            "Project**, then **New RStudio Project**. Everything in this "
            "handout works the same way. To put the example folder in, use "
            "the **Upload** button in the Files pane.")),
        Head(text="For the flowchart", number="F"),
        Para(text=(
            "Draw it in **bpmn.io** at **https://demo.bpmn.io/**. It runs in "
            "the browser, is free, and needs no account. Or install **Camunda "
            "Modeler** from **https://camunda.com/download/modeler/**. Both "
            "draw BPMN and both save a `.bpmn` file and export a picture. If "
            "you would rather use Markdown, **https://mermaid.live** draws a "
            "Mermaid flowchart in the browser.")),
    ),
)

# --------------------------------------------------------------------------
# 2 The rule, and 3 the contract
# --------------------------------------------------------------------------

RULE = Section(
    title="2. The rule the example uses",
    kicker="Larry Williams' Oops, exactly as the Chapter 7 slides give it.",
    footer="The rule",
    blocks=(
        Para(text=(
            "The slide numbers are those of the Chapter 7 student edition "
            "deck. Every price the script uses is on one of these slides.")),
        Table(
            title="What the slides say",
            headers=("Slide", "What it says"),
            widths=(10, 90),
            rows=(
                ("194", "Williams' Oops starts with a bar that opens beyond "
                 "the range of the previous bar: an open above the previous "
                 "high or below the previous low, which the bar may then "
                 "trade back through. If the new bar opens above the "
                 "previous bar's high, Lim places a sell-stop entry order at "
                 "the previous bar's high and a stoploss at the new bar's "
                 "high. We sell only if price falls back to the previous "
                 "high."),
                ("199", "The bullish Oops is the mirror image. If the new "
                 "bar opens below the previous bar's low, Lim places a "
                 "buy-stop entry order at the previous bar's low and a "
                 "stoploss at the new bar's low."),
                ("197", "If price turned back through the stoploss, the "
                 "stoploss closes the position, and Lim adds that a stop and "
                 "reverse order is initiated at the stoploss level, so we "
                 "would also take the opposite side there."),
                ("193", "A sell-stop is filled only if price falls to it, a "
                 "buy-stop only if price rises to it, and a stoploss closes "
                 "a position that moves against us."),
                ("195", "Lim says it is best to look for a bullish Oops in "
                 "an uptrend and a bearish Oops in a downtrend."),
            ),
        ),
        Table(
            title="The rule as the script reads it",
            headers=("Case", "Test, bar i against bar i - 1", "Entry", "Stoploss", "Then"),
            widths=(14, 40, 14, 14, 18),
            rows=(
                ("SELL (bearish Oops)", "Open[i] is above High[i-1], and Low[i] is at or below High[i-1]",
                 "High[i-1]", "High[i]", "reverse: BUY at the stoploss"),
                ("BUY (bullish Oops)", "Open[i] is below Low[i-1], and High[i] is at or above Low[i-1]",
                 "Low[i-1]", "Low[i]", "reverse: SELL at the stoploss"),
            ),
            note="The second half of each test is the slides' words made "
                 "exact: the order is filled only if price comes back to it.",
        ),
        Callout(label="The slides leave four things open. These are our "
                "choices, not Lim's rule", tone="gold", text=(
            "**One bar only.** The slides draw the pull-back happening on "
            "the same bar as the gap, so the script looks only at that bar. "
            "Whether a later bar could fill the order is not stated.\n\n"
            "**Order inside a bar.** A daily bar gives the high and the low "
            "but not which came first. The slides draw the high first and "
            "then the fall; the script does not need to know.\n\n"
            "**No trend filter.** Slide 195 says to prefer a bullish Oops in "
            "an uptrend and a bearish Oops in a downtrend, but the slides do "
            "not give a test a computer can run. The script reports every "
            "Oops and leaves the trend for you to look at on the chart. "
            "Adding a trend test is a decision you would make and explain.\n\n"
            "**No profit exit.** The slides give a stoploss and a stop and "
            "reverse, and nothing about taking profit. The script reports "
            "the stoploss and the reverse side and nothing else.")),
    ),
)

CONTRACT = Section(
    title="3. The contract: what every script must do",
    kicker="Your script is marked by running it on files you have never "
           "seen. It can only work if everybody follows this exactly.",
    footer="The contract",
    blocks=(
        Table(
            title="Folders and files",
            headers=("What", "Rule"),
            widths=(28, 72),
            rows=(
                ("Where it runs", "The script is run from the folder that "
                 "holds it. That folder holds a folder called `data`."),
                ("Input", "Every file in `data` ending `.csv` is one stock. "
                 "The ticker is the file name without `.csv`, so `KO.csv` is "
                 "ticker `KO`."),
                ("Output folder", "`output`. The script makes it if it is not "
                 "there."),
                ("Signals file", "`output/signals.csv`, one row per signal, "
                 "every input file together. If there are no signals it is "
                 "still written, with only the header row."),
                ("Chart files", "`output/<ticker>.png`, one per input file, "
                 "with every signal marked and numbered."),
                ("Packages", "None. Base R only. No `install.packages`, no "
                 "`library()` of anything that is not already in R."),
                ("Time", "Under 60 seconds for ten files of a year each."),
            ),
        ),
        Table(
            title="The input columns",
            headers=("Column", "Meaning"),
            widths=(20, 80),
            mono_cols=(0,),
            rows=(
                ("Date", "Oldest row first. Either `2026-07-02` or "
                 "`2026-07-02 16:00:00`."),
                ("Open", "The opening price of the bar."),
                ("High", "The highest price of the bar."),
                ("Low", "The lowest price of the bar."),
                ("Close", "The closing price of the bar."),
                ("Volume", "May be there. The example does not use it."),
            ),
            note="The first row of the file is these names, spelled and "
                 "capitalised exactly so. One row is one trading day. A file "
                 "may have other columns; ignore them.",
        ),
        Table(
            title="The columns of output/signals.csv, in this order",
            headers=("Column", "Meaning", "Example"),
            widths=(18, 56, 26),
            mono_cols=(0, 2),
            rows=(
                ("ticker", "The file name without `.csv`", "KO"),
                ("date", "The day the signal happened, as `YYYY-MM-DD`", "2026-07-07"),
                ("side", "`BUY` or `SELL`, capitals", "SELL"),
                ("entry", "The entry price the rule gives", "84.56"),
                ("stoploss", "The stoploss price the rule gives", "85.68"),
                ("reverse", "Optional. The side of the stop and reverse "
                 "order at the stoploss. Your own extra columns may follow.", "BUY"),
            ),
            note="The first five columns are required and marked. The rows "
                 "go ticker by ticker, then date by date. The chart number "
                 "of a signal is its row number within its ticker.",
        ),
    ),
)

# --------------------------------------------------------------------------
# 4 R basics, built from the script
# --------------------------------------------------------------------------


def basics_section(fills: dict) -> Section:
    return Section(
        title="4. R in 14 small steps",
        kicker="One running script that grows. Each step adds exactly one "
               "idea. The new lines are highlighted in yellow. Type each "
               "step yourself if you can: it is the quickest way to learn.",
        footer="R basics",
        blocks=(
            Para(text=(
                "Before you start, make a folder on your computer called "
                f"`{NAME}` and put the folder `data` inside it with the "
                "start-here price files KO and F. In RStudio use **File, New "
                "File, R Script**, save it in that folder, then choose "
                "**Session, Set Working Directory, To Source File "
                "Location**. This tells R which folder you are working in, "
                "and every `data/KO.csv` below is relative to it. Run a "
                "script with the **Source** button at the top right of the "
                "script pane, or select lines and press Ctrl+Enter "
                "(Cmd+Enter on a Mac).")),
            Para(text=(
                "Each step shows the whole script so far, with this step's "
                "new lines highlighted, and then **exactly what R printed** "
                "when we ran it. Your output should match.")),
        ) + basics_blocks(fills),
    )


# --------------------------------------------------------------------------
# 5 Run the finished example
# --------------------------------------------------------------------------

def run_section(counts: dict) -> Section:
    """`counts` holds the real signal counts from the real runs."""
    return Section(
        title="5. Run the finished example",
        kicker="No typing of code. Open it, run it, read the result, then "
               "feed it new data and run it again.",
        footer="Run the example",
        blocks=(
            Step(title="Set up the folder",
                 text=("Copy the folder `" + NAME + "` from the class Drive "
                       "to your computer. Inside it are the script, the "
                       "flowchart files, and two folders of prices. Make a "
                       "folder called `data` next to the script, and copy "
                       "the two files from **data (start here)**, `KO.csv` "
                       "and `F.csv`, into it."),
                 then="The folder now holds the script and a `data` folder "
                      "with two `.csv` files in it.",
                 shot=Shot("r01-folder")),
            Step(title="Open the script in RStudio",
                 text=("In RStudio choose **File, Open File**, and pick `" +
                       SCRIPT_NAME + "`. The script appears in the top-left "
                       "pane."),
                 shot=Shot("r02-open-script")),
            Step(title="Point R at the folder",
                 text=("Choose **Session, Set Working Directory, To Source "
                       "File Location**. The Console prints a `setwd(...)` "
                       "line. This is the step people forget: without it R "
                       "cannot find `data`."),
                 shot=Shot("r03-working-dir")),
            Step(title="Run it",
                 text=("Click **Source** at the top right of the script "
                       "pane. R reads both files, finds the signals, draws "
                       "two charts and writes the table."),
                 then=(f"The Console prints one line per file and the name "
                       f"of the file it wrote. On the start-here files that "
                       f"is {counts.get('KO_start', '?')} signals for KO and "
                       f"{counts.get('F_start', '?')} for F."),
                 shot=Shot("r04-source")),
            Step(title="Look at what it made",
                 text=("The **Files** pane (bottom right) now has an "
                       "`output` folder. Open it: `signals.csv`, `KO.png` "
                       "and `F.png`."),
                 shot=Shot("r05-output-folder")),
            Step(title="Read the signals",
                 text=("Open `signals.csv` (click it, then View File). Each "
                       "row is one Oops. `side` says SELL or BUY, `entry` is "
                       "the price the stop order waits at, `stoploss` is "
                       "where the trade is closed, and `reverse` is the "
                       "opposite side Lim starts at the stoploss."),
                 shot=Shot("r06-signals-csv")),
            Step(title="Read the chart",
                 text=("Open `KO.png`. White candles closed up and black "
                       "candles closed down. A **red triangle pointing "
                       "down** is a SELL entry, a **green triangle pointing "
                       "up** is a BUY entry, the **short dash** beside each "
                       "is its stoploss, and the **number** is the "
                       "signal's row for KO in `signals.csv`. Check one: "
                       "find signal 1 in the table, find the bar with that "
                       "date, and see that the triangle sits at the entry "
                       "price."),
                 shot=Shot("r07-chart")),
            Step(title="Add new data",
                 text=("This is the automation. Close nothing. Copy the two "
                       "files from **data (October update)** over the ones "
                       "in `data`, replacing them. They are the same two "
                       "stocks with a month of new rows added at the "
                       "bottom."),
                 shot=Shot("r08-new-data")),
            Step(title="Run it again",
                 text="Click **Source** again. You change nothing else.",
                 then=(f"The counts go up: KO from {counts.get('KO_start', '?')} "
                       f"to {counts.get('KO_update', '?')} signals and F from "
                       f"{counts.get('F_start', '?')} to "
                       f"{counts.get('F_update', '?')}. `signals.csv` and both "
                       f"charts have been rewritten. Open them: the new "
                       f"signals are at the end of the table and the right "
                       f"side of each chart."),
                 shot=Shot("r09-rerun")),
            Step(title="See the updated chart",
                 text=("Open `KO.png` again. The chart is longer and the "
                       "new marks continue the numbering."),
                 shot=Shot("r10-chart-updated")),
        ),
    )


# --------------------------------------------------------------------------
# 6 The flowchart
# --------------------------------------------------------------------------


def flow_section() -> Section:
    # Which lines each shape stands for, found in the real script by text.
    f = _script_lines()
    after_find = _after("find_oops <- function")
    rows = (
        ("Start event", "Run the script", "the moment you click Source"),
        ("1", "Name the data and output folders", _span("data_folder   <-", "output_folder <-")),
        ("2", "List the CSV files in the data folder", _span("files <- list.files")),
        ("Gateway", "Another file left?", _span("for (path in files)")),
        ("3", "Read the file into a table",
         _span("read_bars <- function", "=}") + " and " + _span("bars    <- read_bars")),
        ("4", "Start an empty signals table",
         _span("signals <- data.frame(ticker = character()", "stringsAsFactors = FALSE)", after_find)),
        ("Gateway", "Another bar left?", _span("for (i in 2:nrow(bars))")),
        ("Gateway", "Gap up and back to the previous high?", _span("if (bars$Open[i] > prev_high")),
        ("5", "Record a SELL signal", _span('side = "SELL"', "signals <- rbind(signals, row)")),
        ("Gateway", "Gap down and back to the previous low?", _span("} else if (bars$Open[i] < prev_low")),
        ("6", "Record a BUY signal", _span('side = "BUY"', "signals <- rbind(signals, row)")),
        ("7", "Draw the chart and mark the signals",
         _span("draw_chart <- function", "  dev.off()") + " and " + _span("draw_chart(bars, signals, ticker")),
        ("8", "Add this file's signals to the list", _span("all_signals <- rbind(all_signals, signals)")),
        ("9", "Write output/signals.csv", _span("write.csv(all_signals")),
        ("End event", "Signals and charts updated", _span('cat("Wrote"')),
    )
    return Section(
        title="6. The flowchart of the example",
        kicker="A flowchart says, in shapes, what the script does and in "
               "what order. Yours must match your script line for line.",
        footer="The flowchart",
        blocks=(
            Para(text=(
                f"The file `{FLOW_NAME}.pdf` is the example's flowchart, "
                f"drawn in **BPMN**, a standard set of shapes for describing "
                f"a process. Open `{FLOW_NAME}.bpmn` in bpmn.io to see it "
                f"as a file you can move around. You need only five shapes.")),
            Table(
                title="The BPMN shapes you need",
                headers=("Shape", "Name", "Use it for"),
                widths=(22, 24, 54),
                rows=(
                    ("Thin circle", "Start event", "Where the script begins. Exactly one."),
                    ("Thick circle", "End event", "Where it finishes. Every path must reach one."),
                    ("Rounded rectangle", "Task", "One thing the script does, named with a verb: Read the file."),
                    ("Diamond with X", "Exclusive gateway", "A yes or no question. Exactly one way out is taken. Label each arrow leaving it, `yes` and `no`."),
                    ("Arrow", "Sequence flow", "The order. A loop is an arrow that goes back to a gateway."),
                ),
            ),
            Para(text=(
                "Two loops make the whole script. The **outer loop** goes "
                "once per file: the first gateway asks whether a file is "
                "left, and task 8 sends the flow back to it. The **inner "
                "loop** goes once per bar: the second gateway asks whether a "
                "bar is left, and every branch sends the flow back to it. "
                "Only when no bar is left does the chart get drawn.")),
            Table(
                title="Which lines of the example script each shape stands for",
                headers=("Shape", "Says", "Lines"),
                widths=(14, 50, 36),
                rows=tuple(rows),
                note="Open the script and read each range beside its shape. "
                     "Yours should be able to do the same: every shape on "
                     "your flowchart should point at lines of your script.",
            ),
            Para(text=(
                "**Reading it.** Start. Name the folders. List the files. "
                "Is a file left? If yes, read it, start an empty table, "
                "and go to the bars. For each bar, ask whether it gapped up "
                "and came back: if yes, record a SELL. If not, ask whether "
                "it gapped down and came back: if yes, record a BUY. Either "
                "way, go to the next bar. When the bars are done, draw the "
                "chart, add the signals to the list, and ask about the next "
                "file. When no file is left, write `signals.csv` and end.")),
        ),
    )


# --------------------------------------------------------------------------
# 7 Your task
# --------------------------------------------------------------------------

TASK = Section(
    title="7. Your task",
    kicker="Your own script, and a flowchart of it.",
    footer="Your task",
    blocks=(
        Para(text=(
            "Write **your own R script** that applies one rule from "
            "Chapters 1 to 7 and meets the contract in Part 3, and draw a "
            "**flowchart** of how it works.")),
        Points(title="Choose your rule", items=(
            "**Williams' Oops**, as in the example. You may reuse the "
            "example's rule, but the script and flowchart must be yours to "
            "explain.",
            "**Hikkake**, which Lim gives with exact prices in Chapter 7 "
            "(the end of Part 3 of the slides).",
            "**Another rule of your choice** from Chapters 1 to 7, as long "
            "as the slides or Lim give exact buy and stop prices for it. "
            "Write the rule's name and the slide numbers you used in a "
            "comment at the top of your script, so the marker can check it "
            "against the slides.",
        )),
        Callout(label="Say what you decided", tone="gold", text=(
            "Where the slides leave something open, as they did for the "
            "example, choose the simplest thing and **say so** in a comment "
            "and on your flowchart. Do not bring in an indicator or a "
            "definition that is not in the course.")),
        Table(
            title="Name your files exactly",
            headers=("File", "Name"),
            widths=(26, 74),
            mono_cols=(1,),
            rows=(
                ("Your script", "FirstAutomation_Surname_Firstname.R"),
                ("Your flowchart, PDF (preferred)", "FirstAutomation_Surname_Firstname_Flowchart.pdf"),
                ("Or the .bpmn file", "FirstAutomation_Surname_Firstname_Flowchart.bpmn"),
                ("Or a Markdown file", "FirstAutomation_Surname_Firstname_Flowchart.md"),
            ),
            note="Two files, nothing else. Do not send price files or "
                 "output: they are rebuilt from your script. If you send a "
                 "PDF and a .bpmn, send the same flowchart.",
        ),
        Points(title="Before you submit, check", numbered=True, items=(
            "Put your script in a clean folder with a `data` folder of the "
            "example files and run it. It must run **with no changes and no "
            "installs**.",
            "`output/signals.csv` has the five required columns, and one "
            "`.png` per input file is in `output`.",
            "Delete the `output` folder and run it again. It must come back.",
            "Run it with an empty `data` folder. It should not crash, and "
            "`signals.csv` should still be written, with only its header.",
            "Open your flowchart next to your script. Every shape has lines "
            "behind it and every loop and decision in the code is a shape.",
        )),
        Callout(label="The marker runs your script on files you have not "
                "seen", text=(
            "Real stocks, a different period, in the layout of Part 3. Some "
            "files have `2026-07-02` dates and some have `2026-07-02 "
            "16:00:00`. One file may have no signals at all. A script that "
            "only works on the example files will not pass.")),
        Para(text=(
            "**Getting prices for your own testing.** In Google Sheets, in "
            "any cell, type `=GOOGLEFINANCE(\"NASDAQ:KO\",\"all\",DATE(2026,1,2),DATE(2026,4,30))`, "
            "then **File, Download, Comma-separated values (.csv)**. The "
            "columns it makes are Date, Open, High, Low, Close and Volume, "
            "which is the contract. Use a US-listed ticker such as "
            "`NYSE:F` or `NASDAQ:AMD`. If you want a Philippine stock, try "
            "`PSE:` followed by the ticker; if Sheets answers `#N/A` the "
            "exchange is not covered, so use a US stock.")),
    ),
)

# --------------------------------------------------------------------------
# 8 AI
# --------------------------------------------------------------------------

AI = Section(
    title="8. Using AI",
    kicker="Allowed, with one condition.",
    footer="AI policy",
    flow=True,
    blocks=(
        Para(text=(
            "You may use AI to help write your script. The condition is "
            "that **you can properly visualise and explain it in your "
            "flowchart**. The flowchart is where you show that you "
            "understand the script, so:")),
        Points(items=(
            "The flowchart must match **the script you actually submit**, "
            "not an earlier version and not what the AI described.",
            "Each task must say, in your own words, what that part of the "
            "code does, and where the rule has a number, which slide it "
            "comes from.",
            "If you cannot explain a part of the script, do not submit it. "
            "Ask for a simpler version you can explain, or go back to the "
            "example.",
        )),
        Para(text=(
            "A script that runs perfectly with a flowchart that does not "
            "match it loses the flowchart marks. A modest script with a "
            "flowchart that matches it and explains every step does well.")),
    ),
)

# --------------------------------------------------------------------------
# 9 The marks
# --------------------------------------------------------------------------

MARKS = Section(
    title="9. The marks",
    kicker=f"{show_marks(TOTAL)} points. {show_marks(CHECK_TOTAL)} are checked "
           f"against the record by running your script, and "
           f"{show_marks(JUDGE_TOTAL)} are judged from your flowchart.",
    footer="The marks",
    blocks=(
        Table(
            title="Checked against the record",
            headers=("What", "Marks", "How"),
            widths=(30, 10, 60),
            rows=tuple((a, show_marks(m), h) for a, m, h in CHECKABLE)
                 + (("**Subtotal**", f"**{show_marks(CHECK_TOTAL)}**", ""),),
            note="Right or wrong. No rubric is needed because the record "
                 "decides.",
        ),
        Table(
            title="Judged, with the course rubric on the next pages",
            headers=("What", "Marks"),
            widths=(60, 40),
            rows=tuple((a, show_marks(m)) for a, m in JUDGED)
                 + (("**Subtotal**", f"**{show_marks(JUDGE_TOTAL)}**"),),
        ),
        Callout(label="Not marked", text=(
            "**How your code looks.** Neat or messy, short or long, with "
            "comments or without: not marked. Only whether it works and "
            "whether the flowchart explains it.")),
        Callout(label="Your flowchart is marked on its own pages, and the "
                "signals are not a forecast", tone="gold", text=(
            "The script reports what a rule says at a point in the past. "
            "Nothing here is marked on whether a signal would have made "
            "money.")),
    ),
)

# --------------------------------------------------------------------------
# The rubric, applied to the three flowchart marks
# --------------------------------------------------------------------------

WRITTEN_MARKS = tuple(
    Applied(what=a, out_of=m, means=means)
    for (a, m), means in zip(JUDGED, (
        ("Points at something checkable in your diagram: a start and an end "
         "event, a labelled `yes` and `no` leaving every gateway, an arrow "
         "back for every loop.",
         "The shapes are used for what they mean: a diamond is a question, a "
         "rectangle is an action, and no path stops without an end event."),
        ("Points at the line of your script each shape stands for, and at "
         "every loop and decision in the code having a shape.",
         "Following the arrows reproduces what running the script does, in "
         "the same order, with no shape for code that is not there."),
        ("Each task says what its lines do, with the actual column, price or "
         "file the code uses, and names the slide where the rule has a "
         "price.",
         "The explanation tells the reader why that step is there, not only "
         "what it is called."),
    ))
)

WORKED = (
    Worked("Full",
           "Task 5, Record a SELL signal: it runs when bar i opened above the "
           "previous high and its low came back to that high. It stores "
           "entry = High[i-1] and stoploss = High[i], as slide 194 says, and "
           "reverse = BUY from slide 197.",
           "Names the exact prices and the slides, and the explanation "
           "follows from them."),
    Worked("Partial",
           "Task 5, Record a SELL signal: it saves the entry price and the "
           "stoploss from slide 194 when the gap up fails.",
           "Right idea and the slide, but it never says which price is the "
           "entry and which the stoploss, so it cannot be checked."),
    Worked("Partial",
           "Task 5, Record a SELL signal: it records High[i-1] as the entry "
           "and High[i] as the stoploss, because the market is likely to "
           "keep falling.",
           "Checkable prices, but the reason given does not follow from "
           "them: the code does not predict anything."),
    Worked("Minimal",
           "Task 5, Record a SELL signal: this is where the program decides "
           "to sell, because that is what the rule is for.",
           "A reason, but general: it could describe any task."),
    Worked("None",
           "Task 5, Record a SELL signal: sell.",
           "A label with no reasoning."),
)

HONEST = (
    "A strong flowchart also says where its script is not Lim's rule: "
    "\"the slides do not say whether a later bar can fill the order, so "
    "this script looks at one bar only.\" It is never marked, and it is "
    "the habit that makes a rule you automated one you can trust."
)

RUBRIC_SECTION = Section(
    title=WRITTEN.title,
    kicker=(f"For the {show_marks(JUDGE_TOTAL)} points that a record cannot "
            "check. The same rubric marks every written answer in this "
            "course."),
    footer="The written-answer rubric",
    blocks=written_rubric(
        WRITTEN,
        applied=WRITTEN_MARKS,
        question=("Here is task 5 of the example flowchart explained five "
                  "ways, one at each level, and two at Partial because "
                  "there are two ways to be partial. They are written on "
                  "the example, not on yours."),
        worked=WORKED,
        honest=HONEST,
    ),
)


def build_activity(fills: dict, counts: dict) -> Activity:
    return Activity(
        code="FIN1209",
        course="Technical Analysis in Investment",
        chapter="Chapter 7",
        title=NAME + ": automate one of Lim's rules in R",
        subtitle="Write a small R script that reads price files, finds where "
                 "a rule says to buy or sell, and draws the signals. Then "
                 "draw a flowchart that explains it.",
        presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business "
                  "and Finance, FEU Manila",
        points=TOTAL,
        duration="a few hours over a week",
        replaces="a take-home automation activity",
        source_note=("Example prices are daily bars for KO and F, "
                     "downloaded from Yahoo Finance for classroom use and "
                     "not redistributed in the public course repository. "
                     "The rule is Lim (2016) p. 231."),
        sections=(BRIEF, INSTALL, RULE, CONTRACT, basics_section(fills),
                  run_section(counts), flow_section(), TASK, AI, MARKS,
                  RUBRIC_SECTION),
    )
