"""Chapter 7, Activity 2: First Automation FIN1209. The handout's content.

Data about the activity, not drawing code; build/activitykit.py draws it. Three
things are computed rather than typed so they cannot drift:

* the script's walkthrough (Part 5) is read from build/walk_chapter07.py, which finds every
  line number in the committed example script by its text;
* what R printed in each mode is read from the file build/run_stages.py wrote after really
  running the example script four ways;
* the marks are added up here, and the build stops if they are not 100.

The rules are the five votes of Chapters 5, 7 and 8, quoted by slide number and title, and a buy or sell answer built on them.
Where the slides leave something open (the sell trigger, the stop, how many votes must agree), the guide says so and calls the
choice our own. The script is walked block by block from build/walk_chapter07.py; what R printed comes from build/run_stages.py.
"""

from __future__ import annotations

import json
from pathlib import Path

from activitykit import (Activity, Applied, Callout, Code, Figure, Head, Para, Points,
                         Section, Shot, Step, Table, TypeBox, Worked,
                         show_marks, written_rubric)
import walk_chapter07 as W
from activitykit import Walk
from rubric import WRITTEN

REPO = Path(__file__).resolve().parent.parent
STUDENT = REPO / "chapter-07" / "activity" / "First Automation FIN1209"
SCRIPT_FILE = STUDENT / "First Automation FIN1209 - Example Script.R"
STAGE_OUTPUTS = REPO / "build" / "generated" / "activity2" / "modes.json"

NAME = "First Automation FIN1209"
SCRIPT_NAME = "First Automation FIN1209 - Example Script.R"
FLOW_NAME = "First Automation FIN1209 - Example Flowchart"

# --------------------------------------------------------------------------
# The marks, in one place
# --------------------------------------------------------------------------

CHECKABLE = (
    ("The script runs", 10,
     "In buy mode and in sell mode, on a file you have never seen, with no change except the four settings lines and "
     "no installs, in under 30 seconds each."),
    ("It writes the files the contract names", 10,
     "`output/signals.csv` with the required columns (4), `output/answer.txt` (3), and `output/<stock>.png` (3)."),
    ("It finds the signal days your own rules give", 15,
     "The date and side of every signal day match what you stated in your comments, with none missing and none extra."),
    ("The buy mode answer follows your own rules", 10,
     "BUY or WAIT, and the numbers in the answer, follow what you stated, not the example's rules."),
    ("The sell mode answers follow your own rules", 15,
     "SELL now or HOLD, and the numbers in the answer, follow what you stated, for two different bought dates."),
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


def _modes() -> dict:
    try:
        return json.loads(STAGE_OUTPUTS.read_text(encoding="utf-8"))
    except OSError:
        return {}


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
            "You will teach R to answer one question for a stock you choose: **should I buy it today, or, if I already "
            "own it, should I sell it?** You put a Google Sheets price file in a folder, type four settings at the top of a "
            "short **R script**, and run it. It reads **price, bars and volume** (Chapters 1 to 7) and the three **window "
            "oscillators** of Chapter 8, takes five votes for buy or sell every day, and keeps the days when **at least 3 "
            "of the 5 agree**. In **buy mode** it says BUY, with a level to enter above and a stop, or WAIT. In **sell mode**, "
            "from the price and the day you bought, it says SELL now or HOLD, with a stop. It writes the answer, a table and "
            "a chart. Add new prices and run it again, and the answer updates. That is **automation**.")),
        Callout(label="This program is not foolproof", tone="gold", text=(
            "**It follows rules from our slides. Its signals can be wrong, and they can lose money. It is a class "
            "exercise, not advice.**")),
        Callout(label="You do not need to know R", tone="gold", text=(
            "Nobody in this class was taught to code. The script is about 90 lines in six labelled blocks. Part 5 "
            "walks through it block by block: each line shown whole and highlighted, then its key part, with one plain "
            "sentence on each. The script uses no pipe operators, only plain R and one package.")),
        Table(
            title="What you get, and what you hand in",
            headers=("", "What"),
            widths=(26, 74),
            rows=(
                ("**You get**", "This manual, a guide video, the finished example script and the example flowchart (`.pdf` and "
                 "`.bpmn`). No price files: you download them yourself."),
                ("**You hand in**", "Your own R script, built on your own rules, not a copy of the example with the stock changed "
                 "(Part 9), with the four settings lines at the top, and a flowchart that also shows where your script differs "
                 "from the example. Your own stock. Upload into the folder linked in your email, as Part 9 describes."),
                ("**Due date**", "Sunday, 15 November 2026, 11:59 PM."),
            ),
        ),
        Callout(label="This also counts as your Chapter 8 quiz and your final quiz", tone="gold", text=(
            "**There will be no reschedules for this activity: late or missing work is not re-opened.** This "
            "is too hard to check case by case, so there is no exception.")),
        Callout(label="What the answer is, and is not", text=(
            "The answer is what the rules say about past prices **up to the last row of your file**. That row is the latest "
            "trading day in your download, not the live market price: Google Sheets prices can be up to about 20 minutes late, and "
            "the script does not read a live price. It does not say what price will do next. Chapter 1's point still "
            "holds: a forecast cannot be checked when it is made.")),
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
        Callout(label="One package: TTR", text=(
            "The example uses one package, **TTR**, which works out the moving average, the RSI, the MACD and the "
            "stochastic. Install it once, in the Console, by typing `install.packages(\"TTR\")`. Never put "
            "`install.packages` inside your script. Use no other package: the marker's computer has TTR and nothing else.")),
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
            "price is a trigger level: the trade happens only if price later goes beyond it.\n\n**Signal day.** The slides do not say "
            "how many votes must agree. At least 3 of the 5 is our choice. `agree` counts the votes on the winning side.\n\n"
            "**Your stop.** Chapter 5, slide 74 says a stop is usually placed just below a significant trough for a long position, "
            "and gives no rule or number. Ours is the low of the signal day in buy mode, and the low of the day you bought in "
            "sell mode. It is our choice, not the book's rule.")),
        Table(
            title="What the script answers",
            headers=("Answer", "When, and what it prints"),
            widths=(22, 78),
            rows=(
                ("**Signal day**", "A day when at least 3 of the 5 votes agree: 3 or more BUY, or 3 or more SELL. `agree` counts them."),
                ("**Today**", "The last row of your file: the latest trading day in the download. It is not a live price; Google "
                 "Sheets prices can be up to about 20 minutes late."),
                ("**BUY** (buy mode)", "Today is a buy signal day. Enter if price trades above today's high (slide 201), with a "
                 "stop at today's low."),
                ("**WAIT** (buy mode)", "Today is not a buy signal day. It says how many votes say BUY today, shows the last buy "
                 "signal in the file with its levels, and says what must happen next: 3 of the 5 votes on BUY."),
                ("**SELL now** (sell mode)", "Since the day you bought there was a sell signal, or the price closed below your "
                 "stop. It prints about the last close and your gain or loss in percent, and why."),
                ("**HOLD** (sell mode)", "Neither happened. It prints your stop and your gain or loss so far."),
            ),
            note="In sell mode you give the script the price you paid and the day you bought, in the four settings lines. "
                 "In buy mode it assumes today's price is the last row of your file.",
        ),
    ),
)

CONTRACT = Section(
    title="8. The contract: what every script must do",
    kicker="Your script is marked by running it on a file you have never seen, in buy mode and in sell mode, so everybody follows this exactly.",
    footer="The contract",
    blocks=(
        Table(
            title="Folders and files",
            headers=("What", "Rule"),
            widths=(24, 76),
            rows=(
                ("Where it runs", "From the folder that holds the script, which holds a folder called `data`."),
                ("The settings", "The first lines of your script are these four, in this order, with exactly these names, each on its "
                 "own line, so the marker can change them: `mode <- \"buy\"`, `stock <- \"KO\"`, `bought_price <- 87.29`, "
                 "`bought_date <- \"2026-08-12\"`. `mode` is `\"buy\"` or `\"sell\"`. A comment after a value is fine."),
                ("Input", "`data/<stock>.csv`, at least 60 daily rows, oldest first. Columns `Date, Open, High, Low, Close, "
                 "Volume` exactly. `Date` may be `2026-07-02`, `2026-07-02 16:00:00` or `7/2/2026 16:00:00` (Google Sheets)."),
                ("Output", "`output/signals.csv`, `output/answer.txt` and `output/<stock>.png`: price on top, volume and the "
                 "three oscillators below, signal days marked, today's answer marked."),
                ("Packages", "Base R and `TTR`. Nothing else, and no `install.packages` inside the script."),
                ("Time", "Under 30 seconds for each run."),
            ),
        ),
        Table(
            title="The columns of output/signals.csv, in this order",
            headers=("Column", "Meaning", "Example"),
            widths=(18, 56, 26),
            mono_cols=(0, 2),
            rows=(
                ("ticker", "The stock: your `stock` setting", "KO"),
                ("date", "The signal day, `YYYY-MM-DD`", "2026-09-22"),
                ("side", "`BUY` or `SELL`: the side your rule says agrees enough that day", "BUY"),
                ("entry", "The trigger level, by your rule. The example: a buy is the signal day's high, a sell its low", "88.97"),
                ("stop", "The stop, by your rule. The example: a buy's is the signal day's low, a sell's its high", "87.46"),
                ("trend, bar, rsi, macd, stoch", "What each vote said that day: `BUY`, `SELL` or empty. These five are the "
                 "example's. Your script has one column per vote of its own, named to match", "BUY"),
                ("agree", "How many of your votes gave the `side`", "3"),
                ("volume", "`CONFIRMED` if that day's volume is above the file's average, else `NOT`", "CONFIRMED"),
            ),
            note="One row for each signal day, oldest first. Zero rows is fine: the file still has its header.",
        ),
        Table(
            title="output/answer.txt: what the marker reads",
            headers=("Mode and answer", "The first line starts with, and contains"),
            widths=(26, 74),
            rows=(
                ("buy mode, BUY", "`BUY` and the two levels: the level to enter above (today's high) and the stop (today's low)."),
                ("buy mode, WAIT", "`WAIT`. Further lines give the last buy signal in the file: its date, its high and its low."),
                ("sell mode, SELL", "`SELL` and the last close and your gain or loss in percent."),
                ("sell mode, HOLD", "`HOLD` and your stop and your gain or loss in percent."),
            ),
            note="Use your own words if you like, but the first word and these numbers must be in the file. The example script is the model.",
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
            "close; the stochastic uses the high, low and close; a buy's trigger uses the high and a sell's the low. Volume marks a signal "
            "CONFIRMED when it is above the file's average. **Open interest** exists only for futures, so a stock has none, and "
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
                   "are straight and the ticker is spelled `NYSE:KO`. The last row is the latest trading day, and Google prices can "
                   "be up to about 20 minutes late."),
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
        ("1", "Read the settings: mode, stock, bought price, bought date", _span("mode <-", "bought_date <-")),
        ("2", "Read the data file for the stock", _span("bars <- read.csv", "n <- nrow")),
        ("3", "Vote 1: price trend", _span("pldot <- SMA", "trend_vote[is.na")),
        ("4", "Vote 2: price bar (key reversal)", _span("bar_vote <- ifelse", "bar_vote[is.na")),
        ("5", "Vote 3: RSI crossing 50", _span("rsi <- RSI") + " and " + _span("rsi_sig <- cross")),
        ("6", "Vote 4: MACD crossing its signal line", _span("macd <- MACD") + " and " + _span("macd_sig <- cross")),
        ("7", "Vote 5: stochastic %K crossing %D", _span("sto <- stoch") + " and " + _span("stoch_sig <- cross")),
        ("8", "Count the BUY and SELL votes for each day", _span("votes <- cbind", "sells <- rowSums")),
        ("Gateway", "3 or more of the 5 votes agree?", _span("day <- which")),
        ("9", "Record the signal day: side, trigger, stop, agree, volume", _span("side <- ifelse(buys", "volume = ifelse")),
        ("Gateway", "Mode: buy or sell?", _span("if (mode == \"buy\")")),
        ("Gateway", "Buy signal today?", _span("if (n %in% day")),
        ("10", "BUY: enter above the signal day's high, stop at its low", _span("answer <- paste0(\"BUY: enter")),
        ("11", "WAIT: the last buy signal and what must happen next", _span("answer <- paste0(\"WAIT", "Next one:")),
        ("Gateway", "Sell signal since you bought, or close below the stop?", _span("if (length(sell_day)")),
        ("12", "SELL now, at about the last close, with the percent", _span("answer <- paste0(\"SELL now")),
        ("13", "HOLD: your stop and the percent so far", _span("answer <- paste0(\"HOLD")),
        ("14", "Draw the chart with today's answer marked", _span("png(file.path", "dev.off()")),
        ("15", "Write signals.csv and answer.txt, print the answer", _span("write.csv(signals", "cat(answer")),
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
                    ("**Input**", "Four settings you type (buy or sell, your stock, and for a sale the price and day you bought), "
                     "and a price file from Google Sheets: a date, four prices and a volume for each trading day."),
                    ("**Process**", "Five votes for buy or sell every day: the price trend and the price bar (Chapters 5 and 7), then "
                     "the RSI, the MACD and the stochastic crossing (Chapter 8). A signal day is a day when at least 3 of the 5 "
                     "agree. Then your mode decides: BUY or WAIT, or SELL now or HOLD."),
                    ("**Output**", "The answer, in the Console and in `answer.txt`; a table of the signal days; a chart of price, "
                     "volume and the three oscillators with today's answer marked."),
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


def script_section() -> Section:
    """Part 5: the script block by block. Each block is labelled; each important line is shown whole and highlighted,
    then its key part is boxed, with one plain sentence on each."""
    blocks = [
        Step(title="Set up",
             text=("Make a folder `" + NAME + "` in your Documents folder with a folder `data` inside it, and put "
                   "the two Part 2 files `KO.csv` and `F.csv` in `data`. In RStudio choose **File, New File, R "
                   "Script**, save it in the folder, then **Session, Set Working Directory, To Source File "
                   "Location**. Type `install.packages(\"TTR\")` in the Console once. Run your script with "
                   "**Code, Source**."),
             shot=Shot("r03-working-dir", width_pct=60)),
        Para(text=("The example script, `" + SCRIPT_NAME + "`, has six labelled blocks. Read them in order. Each line below "
                   "is shown whole on a yellow bar, then the key part of it is boxed, with one plain sentence on each. "
                   "The script uses **no pipe operators**: every line is plain R."), glue=False),
    ]
    for k, title, purpose, a, b, rows in W.blocks():
        blocks.append(Head(text=title, number=f"{k}"))
        blocks.append(Para(text=f"**Block {k}, lines {a} to {b}.** {purpose}", glue=True))
        for i in range(0, len(rows), 3):
            blocks.append(Walk(rows=tuple(rows[i:i + 3])))
    return Section(
        title="5. The script, block by block",
        kicker="Six labelled blocks. Each important line is shown whole, then its key part, with one plain sentence each.",
        footer="The script",
        blocks=tuple(blocks),
    )


def run_section(modes: dict) -> Section:
    def run(name: str):
        r = modes.get(name, {})
        return r.get("settings", "").splitlines(), r.get("answer", "(run build/run_stages.py)")

    st_b, out_b = run("buy_wait")
    st_s, out_s = run("buy_signal")
    st_n, out_n = run("sell_now")
    st_h, out_h = run("sell_hold")
    st_u, out_u = run("buy_update")
    sig = modes.get("buy_wait", {}).get("head", [])[:5]
    modes_dir = STAGE_OUTPUTS.parent / "modes"
    return Section(
        title="6. Run it and read the answer",
        kicker="Real runs of the example script, one for each answer. Change the four settings, click Source, read the answer.",
        footer="Run it",
        blocks=(
            Head(text="Buy mode: WAIT", number="1"),
            Para(text=("Settings: `mode` is `\"buy\"` and the stock is KO, the file you downloaded with the end date 30 September. "
                       "Click **Source**. The Console prints the answer, and the same lines go to `output/answer.txt`."), glue=True),
            Code(lines=tuple(st_b), first=3, label="The four settings lines, as typed", output=out_b),
            Para(text=("No buy signal today: the latest day has 0 of the 5 votes on BUY. It also shows the last buy signal in the "
                       "file and what has to happen for the next one."), glue=False),
            Head(text="Buy mode: BUY", number="2"),
            Para(text=("The same file for Ford (F), downloaded a day earlier, ends on 29 October, a day with a buy signal."), glue=True),
            Code(lines=tuple(st_s), first=3, label="The four settings lines, as typed", output=out_s),
            Para(text=("Enter if price trades above that day's high, with the stop at its low. Remember that this is a trigger level: "
                       "the trade happens only if price later goes above it."), glue=False),
            Head(text="Sell mode: SELL now", number="3"),
            Para(text=("Now change `mode` to `\"sell\"` and tell the script what you paid and when. Here you bought KO on 12 August."), glue=True),
            Code(lines=tuple(st_n), first=3, label="The four settings lines, as typed", output=out_n),
            Para(text=("A sell signal appeared after you bought, so the answer is SELL now, at about the last close, with your gain or "
                       "loss in percent and the reason."), glue=False),
            Head(text="Sell mode: HOLD", number="4"),
            Para(text=("The KO file with the end date 30 October, and a purchase on 12 October."), glue=True),
            Code(lines=tuple(st_h), first=3, label="The four settings lines, as typed", output=out_h),
            Para(text=("No sell signal and no close below the stop since you bought, so you hold, with your stop and your gain so far."),
                 glue=False),
            Head(text="Read the table and the chart", number="5"),
            Para(text=("`output/signals.csv` has one row for each signal day: the `side`, the trigger level `entry`, the `stop`, what "
                       "each vote said, `agree`, and `volume`, CONFIRMED when the day's volume is above the file's average."),
                 glue=True),
            Code(lines=tuple(sig), label="output/signals.csv, the first rows (buy mode, KO)"),
            Para(text=("`output/KO.png`: price on top with its orange three bar average. Each triangle is a signal day, green up for a "
                       "buy and red down for a sell. The dashed line is today, labelled with the answer. In sell mode a cross shows "
                       "where you bought and a dotted red line is your stop. Below are the volume (gold on CONFIRMED days) and the "
                       "three oscillators. **The MACD panel is empty at the start:** it needs about 34 days of history, so the "
                       "first weeks of this 64 day example show none. For your own stock pull about a year."), glue=True),
            Figure(path=modes_dir / "buy_wait.png", height_mm=112.0,
                   caption="Buy mode on KO: the answer is WAIT, marked at the right edge.",
                   credit="Drawn by the example script from the Part 2 price file."),
            Figure(path=modes_dir / "sell_hold.png", height_mm=112.0,
                   caption="Sell mode on KO with the file to 30 October: HOLD, with the cross where you bought and the dotted stop.",
                   credit="Drawn by the example script from the Part 2 price file."),
            Head(text="Add new data and run again", number="6"),
            Para(text=("Download the file again with a later end date (Part 2), replace the one in `data`, and click **Source** again. "
                       "Nothing else changes. For KO with the file to 30 October, buy mode now answers:"), glue=True),
            Code(lines=tuple(st_u), first=3, label="The four settings lines, as typed", output=out_u),
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
    kicker="Your own program, on your own stock: the rules are yours to write, not the example's.",
    footer="Your task",
    blocks=(
        Para(text=(
            "**Your job is not to copy the example script.** Your job is to write your own program. Choose your own stock "
            "(a US stock, downloaded as in Part 2, about a year of daily rows) and write your own rules for at least **two** "
            "of these three: (a) which indicators vote, or how a vote is decided, (b) how many votes must agree for a signal "
            "day, (c) where the stop goes. State your rules in comments at the top of your script, plainly, so the marker can "
            "read them. Everything else stays fixed so the marker can run every script the same way: the same four settings "
            "lines at the top (`mode`, `stock`, `bought_price`, `bought_date`), the same answer words (BUY or WAIT in buy "
            "mode, SELL now or HOLD in sell mode, with the numbers), and the three output files of Part 8. Test it yourself: "
            "run it in buy mode, then change `mode` to `\"sell\"`, type a price and a day you bought, and run it again. Then "
            "draw a **flowchart** of how it works, and mark on it where your program differs from the example.")),
        Callout(label="A copy is worth zero for the script part", tone="gold", text=(
            "**A script that is the example with only the stock changed, or that matches the example line for line, gets "
            "zero for the 60 script points**, even if it runs and writes the right files. Changing one of the three things "
            "above is not enough either: you need at least two.")),
        Callout(label="Due date", tone="gold", text="Sunday, 15 November 2026, 11:59 PM."),
        Callout(label="This also counts as your Chapter 8 quiz and your final quiz", tone="gold", text=(
            "**There will be no reschedules for this activity: late or missing work is not re-opened.** This "
            "is too hard to check case by case, so there is no exception.")),
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
        Points(title="How to submit", numbered=True, items=(
            "Use the folder linked in your email. Do not make your own folder, and do not share anything.",
            "Upload your two files into it, named as in the table above. Upload the actual files, not shortcuts "
            "or links to files in your own Drive.",
            "Do not change the files after the deadline: the time each file was uploaded is checked.",
            "If you already shared a folder of your own, upload your files into the linked folder instead: "
            "that is the one that gets graded.",
        )),
        Points(title="Before you submit, check", numbered=True, items=(
            "Your comments at the top state which two (or more) of the three things you changed, plainly.",
            "Put your script in a clean folder with a `data` folder holding your stock's file, and run it in buy mode and "
            "again in sell mode, changing only the four settings lines.",
            "`output` has `signals.csv` with the columns of Part 8, `answer.txt` and a `.png` named after your stock.",
            "Delete `output` and run again. It must come back.",
            "Open your flowchart next to your script. Every shape has lines behind it, and it marks where you differ "
            "from the example.",
        )),
        Callout(label="The marker runs your script on files you have not seen", text=(
            "A file you have not seen, in the layout of Part 8, run in buy mode and in sell mode with settings the marker "
            "chooses. Some files write dates as `2026-07-02`, some as `7/2/2026 16:00:00`. A script that only works on "
            "the example file, or that needs more than the four settings lines changed, will not pass. The answers it "
            "writes are checked against your own stated rules, not against the example's.")),
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
            "Ask for a simpler version you can explain, but it still has "
            "to be your own program on your own rules (Part 9), not the "
            "example with the stock changed.",
        )),
        Para(text=(
            "A script that runs perfectly with a flowchart that does not "
            "match it loses the flowchart marks. A modest script with a "
            "flowchart that matches it and explains every step does well. "
            "None of this is a reason to hand in the example itself: that "
            "scores zero for the script part, however good the flowchart.")),
    ),
)

# --------------------------------------------------------------------------
# 9 The marks
# --------------------------------------------------------------------------

MARKS = Section(
    title="11. The marks",
    kicker=f"{show_marks(TOTAL)} points. {show_marks(CHECK_TOTAL)} are checked "
           f"by running your script and reading your stated rules, and "
           f"{show_marks(JUDGE_TOTAL)} are judged from your flowchart.",
    footer="The marks",
    blocks=(
        Table(
            title="Checked by running your script",
            headers=("What", "Marks", "How"),
            widths=(30, 10, 60),
            rows=tuple((a, show_marks(m), h) for a, m, h in CHECKABLE)
                 + (("**Subtotal**", f"**{show_marks(CHECK_TOTAL)}**", ""),),
            note="Right or wrong against the rules you stated in your comments, not against the example's rules. A "
                 "script that is the example with only the stock changed, or that matches it line for line, scores "
                 "zero here, whatever it prints.",
        ),
        Table(
            title="Judged, with the course rubric on the next pages",
            headers=("What", "Marks"),
            widths=(60, 40),
            rows=tuple((a, show_marks(m)) for a, m in JUDGED)
                 + (("**Subtotal**", f"**{show_marks(JUDGE_TOTAL)}**"),),
            note="Includes whether your flowchart shows where your program differs from the example.",
        ),
        Callout(label="Not marked", text=(
            "**How your code looks.** Neat or messy, short or long: not "
            "marked. Only whether it works, whether your comments state "
            "your own rules plainly enough to check, and whether the "
            "flowchart explains it.")),
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
         "every loop and decision in the code having a shape, with the "
         "shapes that differ from the example marked as such.",
         "Following the arrows reproduces what running the script does, in "
         "the same order, with no shape for code that is not there, and a "
         "reader can see where your rules depart from the example's."),
        ("Each task says what its lines do, with the actual column, price or "
         "file the code uses, and names the slide where the rule has a "
         "price.",
         "The explanation tells the reader why that step is there, not only "
         "what it is called."),
    ))
)

WORKED = (
    Worked("Full",
           "Task 9, Record the signal day: it keeps only the days when 3 or more of the five votes agree, so a day with two "
           "BUY votes is skipped. A BUY day's trigger is its High, as slide 201 says, a SELL day's is its Low, the mirror, "
           "and `agree` counts the votes on that side.",
           "Names what the code keeps, a real consequence (days skipped), the exact price rule and the slide."),
    Worked("Partial",
           "Task 9, Record the signal day: it keeps the days with a signal and writes the trigger using the slide 201 rule.",
           "Right idea and a slide, but it never says how many votes make a signal or what `agree` counts, so it cannot be checked."),
    Worked("Partial",
           "Task 9, Record the signal day: it keeps the days with 3 or more votes, because three votes agreeing means price "
           "will rise.",
           "Checkable action, but the reason does not follow: the code does not predict anything."),
    Worked("Minimal",
           "Task 9, Record the signal day: this is where the program decides which days matter.",
           "A reason, but general: it could describe any task."),
    Worked("None",
           "Task 9, Record the signal day: signals.",
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
        question=("Here is task 9 of the example flowchart explained five "
                  "ways, one at each level, and two at Partial because "
                  "there are two ways to be partial. They are written on "
                  "the example, not on yours."),
        worked=WORKED,
        honest=HONEST,
    ),
)


def build_activity(modes: dict, info: dict | None = None) -> Activity:
    info = info or {}
    return Activity(
        code="FIN1209",
        course="Technical Analysis in Investment",
        chapter="Chapter 7",
        title=NAME + ": ask R whether to buy or sell",
        subtitle="Write a short R script that reads a stock's prices, takes five votes a day (price trend, price bar, RSI, MACD "
                 "and stochastic), and answers: buy today or wait, or, if you own it, sell now or hold. Then draw a flowchart "
                 "that explains it.",
        presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business "
                  "and Finance, FEU Manila",
        points=TOTAL,
        duration="a few hours over a week",
        replaces="a take-home automation activity",
        source_note=("Prices are pulled by each student with GOOGLEFINANCE "
                     "in Google Sheets; none are distributed with the "
                     "course. The rules are from Lim (2016), Chapters 5, 7 and 8."),
        sections=(BRIEF, INSTALL, SOURCES, DATA, flow_section(), RULE, script_section(),
                  run_section(modes), why_section(info), CONTRACT, TASK, AI, MARKS,
                  RUBRIC_SECTION),
    )
