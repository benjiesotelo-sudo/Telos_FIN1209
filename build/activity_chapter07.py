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
     "The trigger level (`entry`) matches the record, to the cent: a buy's is the signal day's high, a sell's is its low."),
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


# --------------------------------------------------------------------------
# What this is
# --------------------------------------------------------------------------

def _video_line() -> str:
    """The guide video's two versions and where its outputs start, as the finished video has them."""
    try:
        t = json.loads((Path(__file__).resolve().parent / "video_times.json").read_text(encoding="utf-8"))["label"]
    except (OSError, ValueError, KeyError):
        t = {"long": "mm:ss", "short": "mm:ss", "out": "mm:ss"}
    return (f"**Long version from {t['long']}, short version from {t['short']}, outputs from {t['out']}.** "
            "The long version types every line and explains it. The short version explains each block of code and what it "
            "produces. Watch one of the two, then carry on from the outputs.")


BRIEF = Section(
    title="What you are making",
    kicker="Read this page first. It is short.",
    footer="What you are making",
    flow=True,
    blocks=(
        Para(text=(
            "You will teach R to read **price, bars and volume** (Chapters 1 to 7) and the three **window oscillators** of "
            "Chapter 8. You put a Google Sheets price file in a folder, run a short **R script**, and it works out, day by "
            "day, five votes for buy or sell: the **price trend**, the **price bar**, the **RSI**, the **MACD** and the "
            "**stochastic**. It counts how many agree, checks the **volume**, and gives a trigger price. It writes a "
            "table and a chart. Add new prices and run it again, and both update. That is **automation**.")),
        Callout(label="This program is not foolproof", tone="gold", text=(
            "**It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class "
            "exercise, not advice.**")),
        Callout(label="The guide video has two versions", tone="gold", text=_video_line()),
        Callout(label="You do not need to know R", tone="gold", text=(
            "Nobody in this class was taught to code. The script is about 60 lines, Part 3 shows what it does, and "
            "Part 5 builds it in seven small steps. The numbers it prints are not advice: Part 7 shows what they "
            "mean, and why signals that agree may agree for a bad reason.")),
        Table(
            title="What you get, and what you hand in",
            headers=("", "What"),
            widths=(26, 74),
            rows=(
                ("**You get**", "This manual, a video that shows every step on screen, the finished example script "
                 "and the example flowchart (`.pdf` and `.bpmn`). No price files: you download them yourself."),
                ("**You hand in**", "Your own R script and a flowchart of how it works. Your own stock, and your own "
                 "pair of Chapter 8 oscillators (Part 9)."),
                ("**Due date**", "______________ (to be filled in: after the Saturday 7 November Chapter 8 class)"),
            ),
        ),
        Callout(label="What these signals are", text=(
            "The output is **the signals of three rules, applied to past prices**. It is not investment advice and it "
            "does not say what price will do next. Chapter 1's point still holds: a forecast cannot be checked when "
            "it is made.")),
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
    title="4. The five votes and the volume check",
    kicker="Each rule as the slides give it, with the slide number and title. Chapter 5, 7 and 8 student editions.",
    footer="The rules",
    blocks=(
        Table(
            title="What the slides say",
            headers=("Slide", "Rule"),
            widths=(16, 84),
            rows=(
                ("Ch 5: 109, 110 \"Drummond geometry\", \"Reading a PLdot line\"",
                 "**Trend vote.** A three bar moving average of price: price above it is bullish, below it is bearish."),
                ("Ch 7: 123, 126 \"The key reversal is when a strong move suddenly turns\"",
                 "**Bar vote.** A bearish key reversal bar forms a higher high than the previous bar and closes near or "
                 "below the previous close. The bullish one is the opposite: a new low, then a close near or above."),
                ("Ch 7: 128 \"Figure 7.15 shows the key reversal on the book's chart\"",
                 "**Volume check.** The key reversal day is marked with above-average volume. Volume is not a vote: it "
                 "marks a signal CONFIRMED or not."),
                ("Ch 8: 74", "**RSI vote.** Crossing above the 50 equilibrium line is a buy and below it a sell."),
                ("Ch 8: 83, 166 to 168", "**MACD vote.** 12 period EMA minus 26 period EMA, 9 period signal line. Crossing "
                 "above the signal line is a buy, below it a sell."),
                ("Ch 8: 185, 187, 189", "**Stochastic vote.** %K over 14 bars, %D its 3 period average. %K crossing above "
                 "%D is a buy, below it a sell."),
                ("Ch 8: 193 to 195", "The RSI uses 14 periods and plain averages of gains and losses."),
                ("Ch 8: 201", "The trigger for entry is normally the high of the bar tied to the buy signal."),
                ("Ch 8: 78, 81", "Oscillators built from the same prices are highly correlated: multicollinearity, a "
                 "false consensus."),
            ),
        ),
        Callout(label="Our choices, not Lim's rule", tone="gold", text=(
            "**Trend.** Slide 110's own chart averages closes, and the book's PLdot averages typical price, which "
            "Chapter 5 does not define. We average the closes. Chapter 2's peaks and troughs trend is not computed.\n\n"
            "**Key reversal.** The slides say \"near or below\" the previous close. We read it as at or below, and at or "
            "above for the bullish one.\n\n**Volume.** The slides give no period for \"average\", so it is the "
            "average volume of the whole file.\n\n**Entry.** A buy triggers above the signal day's high, as slide 201 says. The "
            "slides give no sell trigger, so a sell triggers below the signal day's low: the mirror of Lim's buy trigger on "
            "slide 201, our choice, not Lim's rule. (Lim's own drawing of the ID/NR6 pattern, Chapter 7 slide 207, puts its long "
            "trigger at a bar's high and its short trigger at that bar's low, but that is one pattern.) For both sides the "
            "price is a trigger level: the trade happens only if price later goes beyond it.\n\n**Signal day.** Any day the bar or an "
            "oscillator fires and the five votes do not cancel. `agree` counts the votes on the winning side.")),
    ),
)

CONTRACT = Section(
    title="8. The contract: what every script must do",
    kicker="Your script is marked by running it on files you have never seen, so everybody follows this exactly.",
    footer="The contract",
    blocks=(
        Table(
            title="Folders and files",
            headers=("What", "Rule"),
            widths=(24, 76),
            rows=(
                ("Where it runs", "From the folder that holds the script, which holds a folder called `data`."),
                ("Input", "Every `.csv` in `data` is one stock; the ticker is the file name without `.csv`. At least "
                 "60 daily rows each, oldest first. Columns `Date, Open, High, Low, Close, Volume` exactly. `Date` "
                 "may be `2026-07-02`, `2026-07-02 16:00:00` or `7/2/2026 16:00:00` (Google Sheets)."),
                ("Output", "`output/signals.csv`, every stock together, and one `output/<ticker>.png` per file: price "
                 "on top, your oscillators below, signal days marked."),
                ("Packages", "Base R and `TTR`. Nothing else, and no `install.packages` inside the script."),
                ("Time", "Under two minutes for three files of a year each."),
            ),
        ),
        Table(
            title="The columns of output/signals.csv, in this order",
            headers=("Column", "Meaning", "Example"),
            widths=(18, 56, 26),
            mono_cols=(0, 2),
            rows=(
                ("ticker", "The file name without `.csv`", "KO"),
                ("date", "The signal day, `YYYY-MM-DD`", "2026-04-08"),
                ("side", "`BUY` or `SELL`: the side most oscillators gave", "BUY"),
                ("entry", "The trigger level. A buy: the signal day's high. A sell: the signal day's low", "77.37"),
                ("trend, bar", "The two price votes: `BUY`, `SELL` or empty", "BUY"),
                ("rsi, macd, stoch", "One column for each oscillator you use, from `rsi`, `macd`, `stoch`. "
                 "`BUY`, `SELL` or empty. **Use at least two.** The columns you use tell the marker your pair.", "BUY"),
                ("agree", "How many of your votes gave the `side`", "3"),
                ("volume", "`CONFIRMED` if that day's volume is above the file's average, else `NOT`", "CONFIRMED"),
            ),
            note="One row per signal day: the bar or an oscillator fires and the votes do not cancel. Rows go ticker by ticker, then by date. "
                 "The chart number of a day is its row number in the file.",
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
        Para(text=(
            "The script needs six columns: Date, Open, High, Low, Close and Volume. The RSI and the MACD use the "
            "close; the stochastic uses the high, low and close; a buy's trigger uses the high and a sell's the low. Volume is not "
            "used here (Chapter 6 covers it). **Open interest** exists only for futures, so a stock has none, and "
            "no source below gives one for a share.")),
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
    title="2b. Get the example prices yourself",
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
             shot=Shot("g1-blank-sheet", width_pct=33)),
        Step(title="Type the formula",
             text="In A1 type this formula for Coca-Cola, then press Enter:",
             type_this=_gf(EXAMPLE_TICKERS[0][0], "2026,9,30"),
             then=("The picture shows the formula being typed. Its end date "
                   "in that capture reads 2026,10,30; **use 2026,9,30** for "
                   "this first run."),
             shot=Shot("g2-formula", width_pct=33)),
        Step(title="Check the result",
             text=("Wait a moment. About 64 rows fill down from A1, with the "
                   "six column names in row 1. The dates read like "
                   "`7/1/2026 16:00:00`: that is the layout Google Sheets "
                   "gives, and the script reads it as it is, so you never "
                   "edit a date. If you see `#N/A`, check the quote marks "
                   "are straight and the ticker is spelled `NYSE:KO`."),
             shot=Shot("g3-result", width_pct=33)),
        Step(title="Download it as a CSV",
             text=("Choose **File, Download, Comma Separated Values (.csv)**. "
                   "The file holds the values, not the formula, so there is "
                   "nothing more to do to it. Your browser saves a file "
                   "named after the spreadsheet."),
             shot=Shot("g4-download-menu", width_pct=33)),
        Para(text=(
            "Rename the file **KO.csv** and move it into your `data` folder. "
            "The name matters: the script takes the ticker from it. Then do "
            "the same for a second stock in a new spreadsheet, with this "
            "formula, and save it as **F.csv** in `data`. Part 6 runs the "
            "script on these two files.")),
        TypeBox(text=_gf(EXAMPLE_TICKERS[1][0], "2026,9,30"),
                label="Cell A1, for F (Ford)"),
        Para(text=(
            "**Later, for the update in Part 6:** in each spreadsheet change "
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


def basics_blocks(fills: dict) -> tuple:
    """Each step: what it adds, line by line in plain words (the same words as the video), then what R printed."""
    from activity_chapter07_code import stage_code
    from explain_chapter07 import GROUPS, STEPS, written
    outs = _outputs()
    blocks = []
    prev = ""
    for n, st in enumerate(STAGES, 1):
        code = _stage_code(st, fills)
        out = outs.get(st.key, "(output appears after the real run)")
        ol = out.splitlines()
        if len(ol) > 7:
            out = "\n".join(ol[:7]) + f"\n... ({len(ol) - 7} more lines)"
        blocks.append(Head(text=STEPS[n][0], number=f"{n}"))
        blocks.append(Para(text=STEPS[n][1] + " Type each group of lines, read what it does, then move on.", glue=True))
        rows = tuple((f"{a}" if a == b else f"{a} to {b}", written(t)) for (s_, a, b, t) in GROUPS if s_ == n)
        if rows:
            blocks.append(Table(title=f"What the new lines do (line numbers of the finished script)",
                                headers=("Lines", "What they do"), widths=(14, 86), rows=rows))
        new_idx = _new_lines(prev, code)
        lines = code.splitlines()
        shown = tuple(lines[i - 1] for i in new_idx if not lines[i - 1].lstrip().startswith("#"))
        if n < 7 and shown:
            blocks.append(Code(lines=shown[:20], output=out,
                               label=f"Typed in step {n}, and the line that prints the result"))
        else:
            last = tuple(x for x in lines if x.lstrip().startswith("cat("))
            blocks.append(Code(lines=last, output=out, label="Typed in step 7, and what R printed"))
        blocks.append(Para(text="**Run it** with Code, Source. " + written(STEPS[n][2]), glue=False))
        prev = code
    return tuple(blocks)


EXAMPLE_TICKERS = (("NYSE:KO", "KO"), ("NYSE:F", "F"))


def _gf(sym: str, end: str) -> str:
    return f'=GOOGLEFINANCE("{sym}","all",DATE(2026,7,1),DATE({end}),"DAILY")'


DATA = Section(
    title="2b. Get the example prices yourself",
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
             shot=Shot("g1-blank-sheet", width_pct=40)),
        Step(title="Type the formula",
             text="In A1 type this formula for Coca-Cola, then press Enter:",
             type_this=_gf(EXAMPLE_TICKERS[0][0], "2026,9,30"),
             then=("The picture shows the formula being typed. Its end date "
                   "in that capture reads 2026,10,30; **use 2026,9,30** for "
                   "this first run."),
             shot=Shot("g2-formula", width_pct=40)),
        Step(title="Check the result",
             text=("Wait a moment. About 64 rows fill down from A1, with the "
                   "six column names in row 1. The dates read like "
                   "`7/1/2026 16:00:00`: that is the layout Google Sheets "
                   "gives, and the script reads it as it is, so you never "
                   "edit a date. If you see `#N/A`, check the quote marks "
                   "are straight and the ticker is spelled `NYSE:KO`."),
             shot=Shot("g3-result", width_pct=40)),
        Step(title="Download it as a CSV",
             text=("Choose **File, Download, Comma Separated Values (.csv)**. "
                   "The file holds the values, not the formula, so there is "
                   "nothing more to do to it. Your browser saves a file "
                   "named after the spreadsheet."),
             shot=Shot("g4-download-menu", width_pct=40)),
        Para(text=(
            "Rename the file **KO.csv** and move it into your `data` folder. "
            "The name matters: the script takes the ticker from it. Then do "
            "the same for a second stock in a new spreadsheet, with this "
            "formula, and save it as **F.csv** in `data`. Part 6 runs the "
            "script on these two files.")),
        TypeBox(text=_gf(EXAMPLE_TICKERS[1][0], "2026,9,30"),
                label="Cell A1, for F (Ford)"),
        Para(text=(
            "**Later, for the update in Part 6:** in each spreadsheet change "
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


def flow_section() -> Section:
    rows = (
        ("Start event", "Run the script", "the moment you click Source"),
        ("1", "List the CSV files in the data folder", _span("for (path in list.files")),
        ("2", "Read each file and clean its dates", _span("ticker <- sub", "bars$Date <- as.Date")),
        ("3", "Vote 1: price trend", _span("pldot <- SMA", "trend_vote[is.na")),
        ("4", "Vote 2: price bar (key reversal)", _span("bar_vote <- ifelse", "bar_vote[is.na")),
        ("5", "Vote 3: RSI crossing 50", _span("rsi <- RSI") + " and " + _span("rsi_sig <- cross")),
        ("6", "Vote 4: MACD crossing its signal line", _span("macd <- MACD") + " and " + _span("macd_sig <- cross")),
        ("7", "Vote 5: stochastic %K crossing %D", _span("sto <- stoch") + " and " + _span("stoch_sig <- cross")),
        ("8", "Add the five votes for each day", _span("votes <- cbind")),
        ("Gateway", "Signal day?", _span("fired <- ") + " and " + _span("day <- which")),
        ("9", "Choose BUY or SELL by the net vote", _span("side <- ifelse(rowSums")),
        ("10, 11", "BUY trigger = high, SELL trigger = low", _span("entry = ifelse(side")),
        ("12", "Record the signal day", _span("signals <- data.frame", "agree = rowSums")),
        ("13", "Mark the volume CONFIRMED or NOT", _span("volume = ifelse")),
        ("14", "Draw the chart", _span("png(file.path", "dev.off()")),
        ("15", "Print a summary for this stock", _span("cat(ticker")),
        ("16", "Add its signals to the full list", _span("all_signals <- rbind(all_signals, signals)")),
        ("17", "Write the signals table", _span("write.csv(all_signals")),
    )
    return Section(
        title="3. What the script does",
        kicker="Input, process, output. A flowchart says it in shapes; yours must match your script line for line.",
        footer="What the script does",
        blocks=(
            Figure(path=STUDENT / f"{FLOW_NAME}.svg", height_mm=122.0,
                   caption=f"The example script as a BPMN flowchart. `{FLOW_NAME}.bpmn` opens in bpmn.io.",
                   credit="Drawn for this course by build/bpmnkit.py."),
            Table(
                title="Input, process, output",
                headers=("Part", "What happens"),
                widths=(14, 86),
                rows=(
                    ("**Input**", "A price file per stock in the `data` folder, from Google Sheets: a date, four prices "
                     "and a volume for each trading day."),
                    ("**Process**", "For every stock and every day, five votes for buy or sell: the price trend and the "
                     "price bar (Chapters 5 and 7), then the RSI, the MACD and the stochastic crossing (Chapter 8). A "
                     "signal day is a day the bar or an oscillator fires and the votes do not cancel. `agree` counts the "
                     "votes on the winning side, and above-average volume marks the day CONFIRMED."),
                    ("**Output**", "A table of the signal days with a trigger level, a chart of price, volume and the "
                     "three oscillators, and a summary line per stock."),
                ),
            ),
            Table(
                title="Which lines each shape stands for",
                headers=("Shape", "Says", "Lines"),
                widths=(14, 50, 36),
                rows=tuple(rows),
                note="BPMN needs five shapes: a thin circle starts, a thick circle ends, a rounded rectangle is a "
                     "task named with a verb, a diamond with an X is a yes or no question with every arrow labelled, "
                     "and an arrow is the order. A page-shaped data object is a file, and a text annotation says a rule. "
                     "Every shape on your flowchart should point at lines of your script.",
            ),
        ),
    )


def script_section(fills: dict) -> Section:
    return Section(
        title="5. Write the script in seven steps",
        kicker="Each step adds one idea. The new lines are highlighted, and what R printed is under them.",
        footer="Write the script",
        blocks=(
            Step(title="Set up",
                 text=("Make a folder `" + NAME + "` in your Documents folder with a folder `data` inside it, and put "
                       "the two Part 2 files `KO.csv` and `F.csv` in `data`. In RStudio choose **File, New File, R "
                       "Script**, save it in the folder, then **Session, Set Working Directory, To Source File "
                       "Location**. Type `install.packages(\"TTR\")` in the Console once. Run your script with "
                       "**Code, Source**."),
                 shot=Shot("r03-working-dir", width_pct=70)),
        ) + basics_blocks(fills),
    )


def run_section(counts: dict) -> Section:
    return Section(
        title="6. Run it and read the output",
        kicker="One answer per stock, a table, a chart. Then new data, and run it again.",
        footer="Run it",
        blocks=(
            Step(title="Run it",
                 text="With the finished script open, click **Source**.",
                 then=(f"The Console prints one line per stock: how many signal days, how many had three or more votes "
                       f"agreeing, and how many were on above-average volume. First-run files: KO "
                       f"{counts.get('KO_start', '?')} signal days, F {counts.get('F_start', '?')}."),
                 shot=Shot("r04-source")),
            Step(title="Read the table",
                 text=("Open `output/signals.csv`. Each row is a signal day: `side`, the `entry` price, what each vote "
                       "said (`trend`, `bar`, `rsi`, `macd`, `stoch`), `agree`, and `volume`: CONFIRMED when the day's "
                       "volume is above the file's average."),
                 shot=Shot("r06-signals-csv")),
            Step(title="Read the chart",
                 text=("Open `output/KO.png`. Price is on top with its orange three bar average. Every triangle is a "
                       "signal day, green up for a buy and red down for a sell; the bigger numbered ones are days "
                       "three or more votes agreed. Below are the volume (gold on CONFIRMED days) and the three "
                       "oscillators. **The MACD panel is empty at the start:** the MACD needs about 34 "
                       "days of history before it can give a signal, so the first weeks of this 64 day example show none. "
                       "For your own stock pull about a year."),
                 shot=Shot("r07-chart")),
            Step(title="Add new data and run again",
                 text=("Download both files again with the later end date (Part 2), replace the ones in `data`, and "
                       "click **Source** again. Nothing else changes."),
                 then=(f"The counts go up: KO from {counts.get('KO_start', '?')} to {counts.get('KO_update', '?')} "
                       f"signal days, F from {counts.get('F_start', '?')} to {counts.get('F_update', '?')}."),
                 shot=Shot("r09-rerun")),
        ),
    )


def why_section(info: dict) -> Section:
    b, s_, c, bar = info.get("buy", {}), info.get("sell", {}), info.get("corr", {}), info.get("bar", {})
    why = STAGE_OUTPUTS.parent / "why"
    return Section(
        title="7. Why the signals are where they are",
        kicker="Real signals from the example tables, drawn for the days around them. The script prints numbers only.",
        footer="Why",
        blocks=(
            Para(text=(
                "**A price bar on volume.** The bar vote is the key reversal day (slides 123 and 126). In the picture, "
                "mark 1 is yesterday's high, mark 2 is today's new high, and mark 3 is the close, below yesterday's "
                "close: the buyers pushed price up and could not hold it, so the vote is SELL. Mark 4 is the volume: "
                "above the average of the file, so the day is CONFIRMED (slide 128). Volume does not vote. It says "
                "how much weight the move carried.")),
            Figure(path=why / "why-bar.png", height_mm=104.0,
                   caption=(f"{bar.get('ticker', '')}, {bar.get('date', '')}: a key reversal day, vote {bar.get('side', '')}, on "
                            f"{bar.get('volume', '')} million shares against an average of {bar.get('avg', '')}."),
                   credit="Drawn by build/r/explain_bar.R from the example price file."),
            Para(text=(
                "**An oscillator buy.** On the day the RSI, the MACD or the stochastic crosses upward, that oscillator "
                "votes BUY. The trigger is above that day's high (slide 201): the trade happens only if price later goes above it. Gold circles mark the oscillators that "
                "crossed and white ones those that did not.")),
            Figure(path=why / "why-buy.png", height_mm=100.0,
                   caption=(f"{b.get('ticker', '')}, {b.get('date', '')}: a BUY where {' and '.join(x.upper() for x in b.get('agree', []))} "
                            f"cross. Trigger {b.get('entry', '')}."),
                   credit="Drawn by build/r/explain_osc.R from the example price files."),
            Para(text=(
                "**A sell** is the mirror image: an oscillator crosses downward. The slides give no sell trigger, so "
                "the trigger is below the signal day's low: the mirror of Lim's buy trigger on slide 201, our choice, not "
                "Lim's rule. The trade happens only if price later falls below it.")),
            Figure(path=why / "why-sell.png", height_mm=100.0,
                   caption=(f"{s_.get('ticker', '')}, {s_.get('date', '')}: a SELL where {' and '.join(x.upper() for x in s_.get('agree', []))} "
                            f"cross. Trigger {s_.get('entry', '')}."),
                   credit="Drawn by build/r/explain_osc.R from the example price files."),
            Callout(label="Agreeing is not proof", tone="gold", text=(
                "Votes agreeing sounds like witnesses agreeing. It is not. The RSI, the MACD and the stochastic are all "
                f"built from the same closing prices, so they move together: on the example data the RSI and the "
                f"stochastic have a correlation of {c.get('rsi_stoch', '')} and the RSI and MACD {c.get('rsi_macd', '')}. "
                "Lim calls this **multicollinearity** and warns that it creates a **false consensus** and a false sense of "
                "confidence (slide 78). His cure (slide 81) is to use data other than price, such as volume, which is "
                "why the volume check is separate. A signal is only a statement of what a rule says that day, not a "
                "forecast.")),
        ),
    )


TASK = Section(
    title="9. Your task",
    kicker="Your own script, on your own stock, and a flowchart of it.",
    footer="Your task",
    blocks=(
        Para(text=(
            "Choose **your own stock** (a US stock, downloaded as in Part 2, about a year of daily rows) and **your own pair** "
            "of the three oscillators: RSI and MACD, RSI and stochastic, or MACD and stochastic. Your script keeps the "
            "price trend vote, the price bar vote and the volume check, adds your pair, and meets the contract in Part 8. "
            "Then draw a **flowchart** of how it works.")),
        Callout(label="Due date", tone="gold", text="______________  (to be filled in: after the Saturday 7 November class)"),
        Table(
            title="Name your files exactly",
            headers=("File", "Name"),
            widths=(26, 74),
            mono_cols=(1,),
            rows=(
                ("Your script", "FirstAutomation_Surname_Firstname.R"),
                ("Flowchart, PDF (preferred)", "FirstAutomation_Surname_Firstname_Flowchart.pdf"),
                ("Or the .bpmn file", "FirstAutomation_Surname_Firstname_Flowchart.bpmn"),
                ("Or a Markdown file", "FirstAutomation_Surname_Firstname_Flowchart.md"),
            ),
            note="Two files, nothing else. No price files or output: they are rebuilt from your script.",
        ),
        Points(title="Before you submit, check", numbered=True, items=(
            "Put your script in a clean folder with a `data` folder of the example files and run it, with no changes.",
            "`output/signals.csv` has `ticker, date, side, entry`, your oscillator columns and `agree`, and a `.png` "
            "per file is in `output`.",
            "Delete `output` and run again. It must come back.",
            "Open your flowchart next to your script. Every shape has lines behind it.",
        )),
        Callout(label="The marker runs your script on files you have not seen", text=(
            "Real stocks, a different period, in the layout of Part 8. Some files write dates as `2026-07-02`, some "
            "as `7/2/2026 16:00:00`. A script that only works on the example files will not pass.")),
    ),
)


# --------------------------------------------------------------------------
# 8 AI
# --------------------------------------------------------------------------

AI = Section(
    title="10. Using AI",
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
    title="11. The marks",
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
           "Task 5, Add the votes and keep the signal days: it adds the three crossing signals, so a day with one "
           "buy and one sell cancels to zero and is skipped. Days with a total above zero are BUYs with entry = "
           "High, as slide 201 says, and SELLs with entry = Low, the mirror, and `agree` counts the oscillators that gave that side.",
           "Names what the code adds, a real consequence (cancelling), the exact price rule and the slide."),
    Worked("Partial",
           "Task 5, Add the votes and keep the signal days: it adds the signals and keeps the days with a signal, "
           "using the slide 201 entry price.",
           "Right idea and a slide, but it never says what is added or what `agree` counts, so it cannot be checked."),
    Worked("Partial",
           "Task 5, Add the votes and keep the signal days: it adds the three signals and keeps the days that are not "
           "zero, because three oscillators agreeing means price will rise.",
           "Checkable action, but the reason does not follow: the code does not predict anything."),
    Worked("Minimal",
           "Task 5, Add the votes and keep the signal days: this is where the program decides which days matter.",
           "A reason, but general: it could describe any task."),
    Worked("None",
           "Task 5, Add the votes and keep the signal days: votes.",
           "A label with no reasoning."),
)

HONEST = (
    "A strong flowchart also says where its script is not Lim's rule: "
    "\"the slides give no sell trigger, so this script uses the low, the mirror of the buy trigger.\" "
    "It is never marked, and it is the habit that makes a rule you automated one you can trust."
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
        title=NAME + ": automate price, bars, volume and three oscillators in R",
        subtitle="Write a short R script that reads price files and takes five votes a day (the price trend and price bar, "
                 "then the RSI, the MACD and the stochastic), counts how many agree, checks the volume, and draws the signals. "
                 "Then draw a flowchart that explains it.",
        presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business "
                  "and Finance, FEU Manila",
        points=TOTAL,
        duration="a few hours over a week",
        replaces="a take-home automation activity",
        source_note=("Prices are pulled by each student with GOOGLEFINANCE "
                     "in Google Sheets; none are distributed with the "
                     "course. The rules are from Lim (2016), Chapter 8."),
        sections=(BRIEF, INSTALL, SOURCES, DATA, flow_section(), RULE, script_section(fills),
                  run_section(counts), why_section(info), CONTRACT, TASK, AI, MARKS,
                  RUBRIC_SECTION),
    )
