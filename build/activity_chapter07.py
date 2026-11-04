"""Chapter 7, Activity 2: First Automation FIN1209. The handout's content.

Data about the activity, not drawing code; build/activitykit.py draws it. Three
things are computed rather than typed so they cannot drift:

* the running script's stages come from build/activity_chapter07_code.py, and
  the last one is the committed example script itself;
* what R printed at each stage is read from the file build/run_stages.py wrote
  after really running every stage;
* the marks are added up here, and the build stops if they are not 100.

The rule is Williams' Oops, quoted from the Chapter 7 student edition
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
        ol = out.splitlines()
        if len(ol) > 8:                  # a long answer: show the start, say how much more
            out = "\n".join(ol[:8]) + f"\n... ({len(ol) - 8} more lines)"
        # Stages that print nothing (the chart ones) say what to look at.
        blocks.append(Head(text=st.title, number=f"B{n}"))
        blocks.append(Para(text=st.text, glue=True))
        all_lines = code.splitlines()
        new = _new_lines(prev, code)
        CH = 34
        for i in range(0, len(all_lines), CH):
            last = i + CH >= len(all_lines)
            tag = f"The script so far, step B{n}"
            if len(all_lines) > CH:
                tag += f" (lines {i + 1} to {min(i + CH, len(all_lines))})"
            blocks.append(Code(lines=tuple(all_lines[i:i + CH]), first=i + 1,
                               new=new, output=out if last else "",
                               label=tag))
        png = STAGE_OUTPUTS.parent / f"stage-{st.key}.png"
        if st.key == "chart" and png.is_file():
            blocks.append(Figure(
                path=png, height_mm=70.0,
                caption=("What `output/KO.png` looks like after step "
                         f"B{n}."),
                credit="Drawn by this script from the KO file you download in Part 3."))
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
            "expected to know how. The script is under 50 lines. Part 6 "
            "shows what it does as a flowchart, and Part 7 builds it in seven "
            "small steps, typing a few lines at a time and running each piece. "
            "You only write your own script in Part 10.")),
        Table(
            title="What you hand in",
            headers=("File", "What it is"),
            widths=(46, 54),
            rows=(
                ("Your R script", "One `.R` file that follows the contract in Part 5."),
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
                (f"{NAME}.mp4 and a narration script", "A short video that "
                 "shows every step being done on screen."),
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
            "Go to **https://docs.posit.co/ide/user/download.html** and "
            "click the big **Download for Windows** button. Open the file "
            "and click Next through the installer.",
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
            "Go to **https://docs.posit.co/ide/user/download.html**, click **Download for macOS**, "
            "open the file, and drag RStudio into the "
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
    title="4. The rule the example uses",
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
                 "stoploss closes the position. Lim adds that a stop and "
                 "reverse order starts at the stoploss level. The example "
                 "script reports the stoploss and does not go further."),
                ("193", "A sell-stop is filled only if price falls to it, a "
                 "buy-stop only if price rises to it, and a stoploss closes "
                 "a position that moves against us."),
                ("195", "Lim says it is best to look for a bullish Oops in "
                 "an uptrend and a bearish Oops in a downtrend."),
            ),
        ),
        Table(
            title="The rule as the script reads it",
            headers=("Case", "Test, day i against day i - 1", "Entry", "Stoploss"),
            widths=(18, 46, 18, 18),
            rows=(
                ("SELL (bearish Oops)", "Open[i] is above High[i-1], and Low[i] is at or below High[i-1]",
                 "High[i-1]", "High[i]"),
                ("BUY (bullish Oops)", "Open[i] is below Low[i-1], and High[i] is at or above Low[i-1]",
                 "Low[i-1]", "Low[i]"),
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
            "**No profit exit.** The slides give a stoploss, and a stop and "
            "reverse order, and nothing about taking profit. The script "
            "reports the entry and the stoploss and nothing else.")),
    ),
)

CONTRACT = Section(
    title="5. The contract: what every script must do",
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
                ("Date", "Oldest row first. Any of `2026-07-02`, "
                 "`2026-07-02 16:00:00` or `7/2/2026 16:00:00`, which is "
                 "how Google Sheets writes it. Use the file as it comes."),
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
            ),
            note="The five columns are required and marked; your own extra columns "
                 "may follow them. The rows "
                 "go ticker by ticker, then date by date. The chart number "
                 "of a signal is its row number within its ticker.",
        ),
    ),
)

SOURCES = Section(
    title="2. Where to get price data, and what kind",
    kicker="Checked on the public sites on 4 November 2026. Where a claim "
           "needs an account, it says so instead of guessing.",
    footer="Price data",
    blocks=(
        Para(text=(
            "Chapter 1 names the data technical analysis reads: **price, "
            "volume and open interest**. For this activity you need one "
            "bar per trading day, with six columns.")),
        Table(
            title="The data and what each column is for",
            headers=("Column", "What it is", "Where the course's rules use it"),
            widths=(14, 34, 52),
            mono_cols=(0,),
            rows=(
                ("Date", "The trading day", "Puts the bars in order and names each signal."),
                ("Open", "The first price of the day", "The Oops tests the open against the previous bar's high or low (slides 194, 199)."),
                ("High", "The highest price of the day", "The Oops sell-stop entry is the previous high and its stoploss is the new high."),
                ("Low", "The lowest price of the day", "The Oops buy-stop entry is the previous low and its stoploss is the new low."),
                ("Close", "The last price of the day", "Colours the candle white or black. Other Chapter 7 rules use the close."),
                ("Volume", "Shares traded in the day", "The Oops does not use it. Chapter 7 mentions volume in some bar patterns, and Chapter 6 covers it in full. Keep the column if your rule's slides use it."),
            ),
            note="**Open interest** is the number of futures contracts "
                 "still open, so it exists only for futures. A stock has "
                 "no open interest, and none of the sources below gives "
                 "one for a share.",
        ),
        Table(
            title="The free sources, and what we found",
            headers=("Source", "Open, high, low, close, volume", "Account", "CSV file"),
            widths=(20, 36, 18, 26),
            rows=(
                ("**Google Sheets, GOOGLEFINANCE**", "Yes, daily or weekly, all five, with the formula `\"all\"`. The Help page lists them.", "A Google account", "Yes: File, Download, CSV. **This handout uses it, for US-listed stocks only.** `PSE:JFC` returned `#N/A`, so there is no daily history for Philippine stocks."),
                ("**PSE EDGE** (edge.pse.com.ph), the exchange's own site", "Today's open, high, low, last price and volume, and the 52-week range, for each Philippine stock. We found no table of past days.", "None to read", "No download link found. The site says its content is copyrighted."),
                ("**Yahoo Finance**", "A history table of date, open, high, low, close, adjusted close and volume for US stocks, readable without signing in. We found no Philippine stocks.", "None to read the table", "No Download button when signed out. Whether one appears after signing in is not checked."),
                ("**Investing.com**", "Not checked: the site refused our automated visit. It is a common place to look for Philippine stocks, so check what it offers for the one you want.", "Not checked", "Not checked"),
                ("**TradingView**", "Charts Philippine stocks, for example PSE:BDO, with a free public page. Export of the chart data was not checked.", "None to view; export needs an account", "Not checked, needs an account"),
                ("**Your broker's platform**, for example COL Financial", "Not checked: it sits behind a login.", "Yes, a brokerage account", "Not checked"),
            ),
            note="Prices in the **adjusted close** column are corrected for "
                 "splits and dividends. The example does not use it.",
        ),
        Para(text=(
            "**The script works with any source** whose CSV has the columns "
            "of Part 5. Google Sheets is the one route this handout walks "
            "through step by step, because every student already has an "
            "account and it exports a CSV in the right layout. If you find "
            "Philippine data elsewhere and can save it as a CSV with those "
            "column names, it will run.")),
    ),
)

EXAMPLE_TICKERS = (("NYSE:KO", "KO"), ("NYSE:F", "F"))


def _gf(sym: str, end: str) -> str:
    return f'=GOOGLEFINANCE("{sym}","all",DATE(2026,7,1),DATE({end}),"DAILY")'


DATA = Section(
    title="3. Get the example prices yourself",
    kicker="The same route you will use for your own task. We give you no "
           "price files.",
    footer="Get prices",
    blocks=(
        Para(text=(
            "**Google Sheets** can fetch daily prices with one formula, and "
            "it gives exactly the columns the contract needs: Date, Open, "
            "High, Low, Close, Volume. It works for **US-listed stocks**. "
            "You do this once per stock, and you use the same dates as "
            "below so your numbers match this handout.")),
        Step(title="Open a blank spreadsheet",
             text=("Go to **https://sheets.new** while signed in to your "
                   "Google account. A blank spreadsheet opens. Click cell "
                   "**A1**."),
             shot=Shot("g1-blank-sheet", width_pct=62)),
        Step(title="Type the formula",
             text="In A1 type this formula for Coca-Cola, then press Enter:",
             type_this=_gf(EXAMPLE_TICKERS[0][0], "2026,9,30"),
             then=("The picture shows the formula being typed. Its end date "
                   "in that capture reads 2026,10,30; **use 2026,9,30** for "
                   "this first run."),
             shot=Shot("g2-formula", width_pct=62)),
        Step(title="Check the result",
             text=("Wait a moment. About 64 rows fill down from A1, with the "
                   "six column names in row 1. The dates read like "
                   "`7/1/2026 16:00:00`: that is the layout Google Sheets "
                   "gives, and the script reads it as it is, so you never "
                   "edit a date. If you see `#N/A`, check the quote marks "
                   "are straight and the ticker is spelled `NYSE:KO`."),
             shot=Shot("g3-result", width_pct=62)),
        Step(title="Download it as a CSV",
             text=("Choose **File, Download, Comma Separated Values (.csv)**. "
                   "The file holds the values, not the formula, so there is "
                   "nothing more to do to it. Your browser saves a file "
                   "named after the spreadsheet."),
             shot=Shot("g4-download-menu", width_pct=62)),
        Para(text=(
            "Rename the file **KO.csv** and move it into your `data` folder. "
            "The name matters: the script takes the ticker from it. Then do "
            "the same for a second stock in a new spreadsheet, with this "
            "formula, and save it as **F.csv** in `data`. Part 8 runs the "
            "script on these two files.")),
        TypeBox(text=_gf(EXAMPLE_TICKERS[1][0], "2026,9,30"),
                label="Cell A1, for F (Ford)"),
        Para(text=(
            "**Later, for the update in Part 8:** in each spreadsheet change "
            "`DATE(2026,9,30)` in the formula to `DATE(2026,10,30)`, "
            "download again, and replace the file in `data`, still named "
            "KO.csv and F.csv. There is no capture of that second download "
            "because it is the same four steps.")),
        Callout(label="Swap the ticker, nothing else", tone="gold", text=(
            "To use another US stock, change only the text inside the first "
            "quotes of the formula, for example `\"NASDAQ:AMD\"`. "
            "**Philippine stocks do not work here.** We tried `PSE:JFC` and "
            "Sheets answered `#N/A`: GOOGLEFINANCE gives no daily history "
            "for Philippine stocks. For a PSE stock you need another source "
            "from Part 2, for example Investing.com, then save its data as "
            "a CSV with the columns of Part 5.")),
    ),
)

# --------------------------------------------------------------------------
# 4 R basics, built from the script
# --------------------------------------------------------------------------


def script_section(fills: dict) -> Section:
    return Section(
        title="7. Write the script in 7 small steps",
        kicker="One running script that grows. Each step adds one idea. The "
               "new lines are highlighted in yellow, and what R printed is "
               "shown under each step. Type each step yourself if you can: "
               "it is the quickest way to learn.",
        footer="Write the script",
        blocks=(
            Step(title="Set up the folder",
                 text=("Make a folder called `" + NAME + "` inside your "
                       "Documents folder. Inside it make a folder called "
                       "`data`, and put in it the two files `KO.csv` and "
                       "`F.csv` you downloaded in Part 3."),
                 then="The folder holds `data` and, next, your script.",
                 shot=Shot("r01-folder", width_pct=70)),
            Step(title="Start a new script and point R at the folder",
                 text=("In RStudio choose **File, New File, R Script**, then "
                       "**File, Save As**, and save it in that folder with a "
                       "name such as `oops_steps`. Then choose **Session, "
                       "Set Working Directory, To Source File Location**. "
                       "The Console prints a `setwd(...)` line. This is the "
                       "step people forget: without it R cannot find "
                       "`data`."),
                 shot=Shot("r03-working-dir")),
            Para(text=(
                "Run what you have typed with the **Source** button at the "
                "top right of the script pane, or with Code, Source. Each "
                "step below shows the whole script so far.")),
        ) + basics_blocks(fills),
    )


def run_section(counts: dict) -> Section:
    """`counts` holds the real signal counts from the real runs."""
    return Section(
        title="8. Run it and read the answer",
        kicker="Run the finished script, read what it says for each stock, "
               "then feed it new data and run it again.",
        footer="Run it",
        blocks=(
            Step(title="Run it",
                 text=("With the finished script open, click **Source**. R "
                       "reads every file in `data`, finds the signals, draws "
                       "one chart per stock and writes the table."),
                 then=(f"The Console prints every signal with a plain **Why** built "
                       f"from that day's own prices, for example `SELL at 84.56 "
                       f"stoploss 85.68` and why. Then, for each stock, how "
                       f"many signals it found and the latest one. On the "
                       f"first-run files that is {counts.get('KO_start', '?')} "
                       f"signals for KO and {counts.get('F_start', '?')} for F. "
                       f"That is the answer: **the price the rule says to act "
                       f"at, and where its stoploss is**."),
                 shot=Shot("r04-source")),
            Step(title="Look at what it made",
                 text=("The **Files** pane now has an `output` folder with "
                       "`signals.csv`, `KO.png` and `F.png`."),
                 shot=Shot("r05-output-folder", width_pct=75)),
            Step(title="Read the table",
                 text=("Open `signals.csv`. Each row is one Oops: `side` says "
                       "SELL or BUY, `entry` is the price the rule says to "
                       "trade at, and `stoploss` is where the trade is "
                       "closed if price goes the wrong way."),
                 shot=Shot("r06-signals-csv")),
            Step(title="Read the chart",
                 text=("Open `KO.png`. The line is the closing price. A "
                       "**red triangle pointing down** is a SELL at its "
                       "entry price and a **green triangle pointing up** is "
                       "a BUY. The number beside it is the signal's row in "
                       "`signals.csv`. Part 9 explains why each triangle is "
                       "where it is."),
                 shot=Shot("r07-chart")),
            Step(title="Add new data",
                 text=("This is the automation. Download both files again "
                       "from Google Sheets with the later end date (the "
                       "update at the end of Part 3) and replace the ones in "
                       "`data`. They are the same stocks with a month of new "
                       "rows."),
                 shot=Shot("r08-new-data", width_pct=75)),
            Step(title="Run it again",
                 text="Click **Source** again. You change nothing else.",
                 then=(f"The counts go up: KO from {counts.get('KO_start', '?')} "
                       f"to {counts.get('KO_update', '?')} signals and F from "
                       f"{counts.get('F_start', '?')} to "
                       f"{counts.get('F_update', '?')}. `signals.csv` and both "
                       f"charts have been rewritten."),
                 shot=Shot("r09-rerun")),
            Step(title="See the updated chart",
                 text=("Open `KO.png` again. The chart is longer and the new "
                       "signals continue the numbering."),
                 shot=Shot("r10-chart-updated")),
        ),
    )


def why_section(info: dict) -> Section:
    sell, buy = info.get("sell", {}), info.get("buy", {})
    why = STAGE_OUTPUTS.parent / "why"
    return Section(
        title="9. Why the script says sell or buy there",
        kicker="Two real signals from the KO output, drawn bar by bar.",
        footer="Why",
        blocks=(
            Para(text=(
                "The signals are not magic. Each one is the Oops rule applied "
                "to two bars: **yesterday's** and **today's**. Here is a real "
                "SELL from your KO output, zoomed in to just those two bars.")),
            Figure(path=why / "why-sell.png", height_mm=88.0,
                   caption=(f"KO, {sell.get('date', '')}: the SELL. Real prices "
                            "from the file you downloaded."),
                   credit="Drawn by build/r/explain_oops.R from the KO price file."),
            Points(numbered=True, title="Read the marks in order", items=(
                f"**Yesterday's high, {sell.get('entry', '')}.** Slide 194 "
                "puts the sell-stop here.",
                "**Today opens above it.** The day gaps up past yesterday's "
                "high, which is where the Oops starts.",
                f"**Price comes back to {sell.get('entry', '')}.** Today's low "
                "is at or below yesterday's high, so the sell-stop is filled. "
                "**This is the SELL, at the entry price.** The gap failed: "
                "buyers pushed it up at the open and could not hold it.",
                f"**The stoploss, {sell.get('stop', '')}.** Slide 194 puts it "
                "at today's high. If price went there the sale was wrong, and "
                "the trade is closed with a small loss.",
            )),
            Para(text="The BUY is the mirror image (slide 199)."),
            Figure(path=why / "why-buy.png", height_mm=88.0,
                   caption=(f"KO, {buy.get('date', '')}: the BUY. Real prices "
                            "from the file you downloaded."),
                   credit="Drawn by build/r/explain_oops.R from the KO price file."),
            Points(numbered=True, title="Read the marks in order", items=(
                f"**Yesterday's low, {buy.get('entry', '')}.** Slide 199 puts "
                "the buy-stop here.",
                "**Today opens below it.** The day gaps down past yesterday's "
                "low.",
                f"**Price comes back up to {buy.get('entry', '')}.** Today's "
                "high reaches yesterday's low, so the buy-stop is filled. "
                "**This is the BUY, at the entry price.** The gap down failed: "
                "sellers pushed it down at the open and could not hold it.",
                f"**The stoploss, {buy.get('stop', '')}.** Slide 199 puts it "
                "at today's low.",
            )),
            Callout(label="A signal is not a forecast", tone="gold", text=(
                "The rule says where to act if the gap fails. It does not say "
                "price will rise or fall. Chapter 1's point still holds: a "
                "forecast cannot be checked when it is made, so a signal is "
                "only a statement of what the rule says at that moment.")),
        ),
    )


def flow_section() -> Section:
    rows = (
        ("Start event", "Run the script", "the moment you click Source"),
        ("1", "List the CSV files in the data folder", _span("for (path in list.files")),
        ("Gateway", "Another file left?", _span("for (path in list.files")),
        ("2", "Read the file and clean its dates", _span("ticker <- sub", "bars$Date <- as.Date")),
        ("Gateway", "Another day left?", _span("for (i in seq_along")),
        ("Gateway", "Gap up, then back to yesterday's high?", _span("if (bars$Open[i] > prev_high")),
        ("3", "Record a SELL signal", _span('side = "SELL"', "signals <- rbind(signals, row)")),
        ("Gateway", "Gap down, then back to yesterday's low?", _span("} else if (bars$Open[i] < prev_low")),
        ("4", "Record a BUY signal", _span('side = "BUY"', "signals <- rbind(signals, row)")),
        ("5", "Draw the chart with the signals marked", _span("png(file.path", "dev.off()")),
        ("6", "Print the answer for this stock", _span("cat(ticker", "format(last$date)")),
        ("7", "Add its signals to the full list", _span("all_signals <- rbind(all_signals, signals)")),
        ("8", "Write output/signals.csv", _span("write.csv(all_signals")),
        ("End event", "Signals, charts and answers ready", "the last line of the script"),
    )
    return Section(
        title="6. The flowchart: what the script does",
        kicker="A flowchart says, in shapes, what the script does and in "
               "what order. Yours must match your script line for line.",
        footer="The flowchart",
        blocks=(
            Para(text=(
                f"The file `{FLOW_NAME}.pdf` is the example's flowchart, "
                f"drawn in **BPMN**, a standard set of shapes for describing "
                f"a process. Open `{FLOW_NAME}.bpmn` in bpmn.io to see it "
                f"as a file you can move around.")),
            Figure(path=STUDENT / f"{FLOW_NAME}.svg", height_mm=72.0,
                   caption="The example script as a BPMN flowchart. The "
                           "numbers match the table below.",
                   credit="Drawn for this course by build/bpmnkit.py."),
            Table(
                title="What the script does, in three parts",
                headers=("Part", "What happens"),
                widths=(16, 84),
                rows=(
                    ("**Input**", "The CSV files in the `data` folder, one "
                     "per stock. Each row is one trading day."),
                    ("**Process**", "For every stock, look at every day "
                     "against the day before. Did it open above yesterday's "
                     "high and then come back down to it? Then record a SELL "
                     "at yesterday's high, with the stoploss at today's high. "
                     "Did it open below yesterday's low and come back up to "
                     "it? Then record a BUY at yesterday's low, with the "
                     "stoploss at today's low."),
                    ("**Output**", "The answer: a line per stock in the "
                     "Console, a chart per stock with every signal marked, "
                     "and one table, `output/signals.csv`."),
                ),
            ),
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
                "once per file and the **inner loop** once per day. Only "
                "when no day is left does the chart get drawn.")),
            Table(
                title="Which lines of the example script each shape stands for",
                headers=("Shape", "Says", "Lines"),
                widths=(14, 50, 36),
                rows=tuple(rows),
                note="Open the script and read each range beside its shape. "
                     "Yours should be able to do the same: every shape on "
                     "your flowchart should point at lines of your script.",
            ),
        ),
    )



# --------------------------------------------------------------------------
# 10 Your task
# --------------------------------------------------------------------------

TASK = Section(
    title="10. Your task",
    kicker="Your own script, and a flowchart of it.",
    footer="Your task",
    blocks=(
        Para(text=(
            "Write **your own R script** that applies one rule from "
            "Chapters 1 to 7 and meets the contract in Part 5, and draw a "
            "**flowchart** of how it works.")),
        Points(title="Choose your rule", items=(
            "**Williams' Oops**, as in the example. You may reuse the "
            "example's rule, but the script and flowchart must be yours to "
            "explain.",
            "**Hikkake**, which Lim gives with exact prices in Chapter 7 "
            "(the end of Part 3 of the Chapter 7 slides).",
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
            "Real stocks, a different period, in the layout of Part 5. Some "
            "files write dates as `2026-07-02`, some as `7/2/2026 16:00:00`. One file may have no signals at all. A script that "
            "only works on the example files will not pass.")),
        Para(text=(
            "**Getting prices for your own testing.** Use Part 3: the "
            "same formula, a different ticker and dates, then "
            "File, Download, CSV. Several stocks and several periods make "
            "the best test.")),
    ),
)

# --------------------------------------------------------------------------
# 8 AI
# --------------------------------------------------------------------------

AI = Section(
    title="11. Using AI",
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
    title="12. The marks",
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


def build_activity(fills: dict, counts: dict, info: dict | None = None) -> Activity:
    info = info or {}
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
        source_note=("Prices are pulled by each student with GOOGLEFINANCE "
                     "in Google Sheets; none are distributed with the "
                     "course. The rule is Lim (2016) p. 231."),
        sections=(BRIEF, INSTALL, SOURCES, DATA, RULE, CONTRACT, flow_section(),
                  script_section(fills), run_section(counts), why_section(info),
                  TASK, AI, MARKS,
                  RUBRIC_SECTION),
    )
