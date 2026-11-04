"""The walkthrough video's scenes, as data: one picture and what is said over it.

The same list makes the narration script the captain can record himself and
the computer-voice video, so the two cannot differ. It covers the whole
handout in the handout's order, with a title card at the start of each part.

`kind` says where the picture comes from:
  card    a title card drawn from `card`
  shot    a screenshot in chapter-07/activity/screens/ (`ref` = name)
  web     a capture of a public web page, in build/generated/video/web/
  page    a region of the built handout PDF (`ref` = text that finds the page,
          `crop` = (top, bottom) as fractions of the page height). Used where
          there is nothing honest to record on a screen.
  code    one step of the R basics guide, drawn from its stage (`ref` = key)
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from activity_chapter07_code import STAGES


@dataclass(frozen=True)
class Scene:
    title: str
    say: str
    kind: str = "card"
    ref: str = ""
    crop: tuple = (0.0, 1.0)
    card: tuple = ()


def part(n: str, title: str, sub: str = "") -> Scene:
    return Scene(f"Part {n}: {title}", f"Part {n}. {title}.", "card",
                 card=(f"Part {n}", title) + ((sub,) if sub else ()))


def _plain(t: str) -> str:
    t = re.sub(r"`([^`]*)`", r"\1", t)
    return t.replace("**", "").replace("\n\n", " ").replace("<-", "arrow").replace("\n", " ")


def _basics() -> tuple:
    out = []
    for n, st in enumerate(STAGES, 1):
        out.append(Scene(f"B{n}: {st.title}",
                         f"Step {n} of 14. {st.title}. {_plain(st.text)} "
                         "The new lines are highlighted, and what R printed is below the code.",
                         "code", st.key))
    return tuple(out)


SCENES = (
    Scene("Welcome",
          "Welcome to First Automation, FIN1209. This video goes through the whole activity, in the "
          "same order as the handout, with a title card at the start of each part. You will teach a "
          "computer one of the rules from Chapter 7. You write a small R script. You drop price files "
          "in a folder, run the script, and it tells you where the rule says to buy or sell, saves "
          "those signals in a table, and draws a chart with each signal marked. Nobody needs to know "
          "R already.",
          "card", card=("First Automation FIN1209", "Automate one of Lim's rules in R", "The whole activity, start to finish")),

    part("0", "What you are making", "and what you hand in"),
    Scene("What you are making",
          "A trading rule says exactly when to buy or sell and at what price. You will automate one. "
          "Run the script, add new prices, run it again, and the signals and the chart update. That is "
          "automation: the rule is applied the same way every time. You hand in two files: your R "
          "script, and a flowchart of how it works. The whole activity is worth one hundred points.",
          "page", "What you are making", (0.0, 0.55)),
    Scene("Signals, not advice",
          "One plain line before we start. The output is the signals of one rule, applied to past "
          "prices. It is not investment advice, and it does not say what price will do next. Chapter "
          "one's point still holds: a forecast cannot be checked when it is made. Later in the semester "
          "a bigger version of this comes, and you may be grouped for it.",
          "page", "What you are making", (0.5, 1.0)),

    part("1", "What to install", "R, RStudio Desktop, and a flowchart tool"),
    Scene("Install R",
          "Install R first. On Windows, go to the CRAN page for Windows and click Download R at the "
          "top. On a Mac, go to the CRAN page for macOS and pick the package for your chip, Apple "
          "silicon or Intel. Open the file and click through the installer, keeping every default.",
          "web", "cran-windows"),
    Scene("Install R on a Mac",
          "This is the Mac page. The first package is for Apple silicon, the second is for older "
          "Intel Macs. The Apple menu, About This Mac, tells you which you have.",
          "web", "cran-mac"),
    Scene("Install RStudio",
          "Then install RStudio Desktop. Go to the RStudio download page on docs dot posit dot co, "
          "and click the big download button for your system. On a Mac, drag RStudio into "
          "Applications. The example needs no R packages at all.",
          "web", "posit-rstudio"),
    Scene("Posit Cloud",
          "If you cannot install anything, use Posit Cloud. It runs RStudio in your browser. Make a "
          "free account, start a new RStudio project, and use the Upload button in the Files pane to "
          "put the example folder in. Everything in the handout works the same way.",
          "web", "posit-cloud"),
    Scene("The flowchart tool",
          "For the flowchart, use bpmn dot io. It runs in the browser, is free, and needs no account. "
          "You can also use Camunda Modeler, or draw a Mermaid flowchart in Markdown at mermaid dot live.",
          "web", "bpmn-io"),

    part("2", "The rule the example uses", "Williams' Oops, from Chapter 7"),
    Scene("The rule",
          "The example uses Larry Williams' Oops from Chapter 7. On slide 194: if a bar opens above "
          "the previous bar's high, Lim places a sell-stop at the previous high and a stoploss at the "
          "new bar's high. We sell only if price falls back to the previous high. On slide 199 the "
          "bullish Oops is the mirror image: open below the previous low, a buy-stop at the previous "
          "low, and a stoploss at the new low. Slide 197 adds that a stop and reverse order starts at "
          "the stoploss.",
          "page", "2. The rule the example uses", (0.0, 0.62)),
    Scene("What the slides leave open",
          "The slides leave four things open, and the handout says so. These are our choices, not "
          "Lim's rule. Only the gap bar can fill the order. The order of high and low inside a daily "
          "bar is not needed. There is no trend filter, because slide 195 gives no test a computer "
          "can run. And there is no profit exit. Where your rule leaves something open, choose the "
          "simplest thing and say so.",
          "page", "2. The rule the example uses", (0.55, 1.0)),

    part("3", "The contract", "what every script must do"),
    Scene("Folders and files",
          "Your script is marked by running it on files you have never seen, so everybody follows "
          "the same contract. The script runs from the folder that holds it, next to a folder called "
          "data. Every CSV in data is one stock, and the file name without dot csv is the ticker. The "
          "script writes output slash signals dot csv, and one chart per input file. Base R only, no "
          "packages, under sixty seconds.",
          "page", "3. The contract", (0.0, 0.5)),
    Scene("Input and output columns",
          "Input files have the columns Date, Open, High, Low, Close, and maybe Volume, with the "
          "oldest row first. Output signals dot csv has ticker, date, side, entry and stoploss, "
          "in that order, and may add your own columns after. If there are no signals, the file is "
          "still written with only the header.",
          "page", "3. The contract", (0.45, 1.0)),

    part("3b", "Where to get price data, and what kind"),
    Scene("The data and what it is for",
          "You need one bar per trading day, with date, open, high, low, close and volume. Open, "
          "high and low are what the Oops uses. The close colours the candle. The Oops does not use "
          "volume, but Chapter 7 mentions it in some patterns and Chapter 6 covers it in full. Open "
          "interest exists only for futures, so a stock has none.",
          "page", "3b. Where to get price data", (0.0, 0.5)),
    Scene("The free sources",
          "Here are the free sources, checked on the public sites. Google Sheets with GOOGLEFINANCE "
          "gives daily open, high, low, close and volume, needs a Google account, and exports a CSV. "
          "P S E Edge shows today's prices only, with no download. Yahoo Finance shows a history "
          "table for US stocks but no Philippine stocks and no download button when signed out. "
          "Investing dot com, TradingView and broker platforms could not be checked without an "
          "account, and the handout says so. The script works with any source whose CSV matches "
          "the contract.",
          "page", "The free sources", (0.0, 0.75)),

    part("4a", "Get the example prices yourself", "Google Sheets"),
    Scene("The GOOGLEFINANCE steps",
          "Google Sheets is the one route this handout walks through. Open sheets dot new, type the "
          "GOOGLEFINANCE formula in cell A1 with the dates from the handout, wait for the rows to "
          "fill, then choose File, Download, comma separated values. Rename the file K O dot csv "
          "and put it in your data folder. Do the same for F. To update later, change the end date "
          "in the formula, download again, and replace the file. To use another stock, change only "
          "the ticker inside the first quotes.",
          "page", "4a. Get the example prices", (0.0, 0.8)),

    part("4", "R in 14 small steps", "one running script that grows"),
) + _basics() + (
    part("5", "Run the finished example"),
    Scene("Step 1: the folder",
          "Step one. Copy the First Automation folder to your Documents folder. Next to the script, "
          "make a folder called data, and copy into it the two price files you downloaded: K O dot "
          "csv and F dot csv.", "shot", "r01-folder"),
    Scene("Step 2: open the script",
          "Step two. In RStudio, choose File, Open File, and pick the example script. It opens in "
          "the top left pane.", "shot", "r02-open-script"),
    Scene("Step 3: set the folder",
          "Step three, the one people forget. Choose Session, Set Working Directory, To Source File "
          "Location. Without this, R cannot find the data folder.", "shot", "r03-working-dir"),
    Scene("Step 4: run it",
          "Step four. Click Source. R reads both files, finds the signals, draws two charts and "
          "writes the table. The console says how many signals it found in each file.",
          "shot", "r04-source"),
    Scene("Step 5: what it made",
          "Step five. The Files pane now has an output folder. Inside are signals dot csv, and one "
          "chart for each stock.", "shot", "r05-output-folder"),
    Scene("Step 6: the signals",
          "Step six. Open signals dot csv. Each row is one Oops. Side says sell or buy. Entry is the "
          "price where the stop order waits. Stoploss is where the trade is closed. Reverse is the "
          "opposite side Lim starts at the stoploss.", "shot", "r06-signals-csv"),
    Scene("Step 7: the chart",
          "Step seven. Open the K O chart. White candles closed up and black candles closed down. A "
          "red triangle pointing down is a sell entry. A green triangle pointing up is a buy entry. "
          "The short dash is its stoploss, and the number is the signal's row in the table. Check "
          "one yourself: find signal one in the table and see that the triangle sits at that entry "
          "price.", "shot", "r07-chart"),
    Scene("Step 8: add new data",
          "Step eight. This is the automation. Download both files again from Google Sheets with the "
          "later end date, and copy them over the ones in your data folder. They are the same two "
          "stocks with a month of new rows at the bottom.", "shot", "r08-new-data"),
    Scene("Step 9: run it again",
          "Step nine. Click Source again, and change nothing else. The counts go up, and the table "
          "and both charts are rewritten.", "shot", "r09-rerun"),
    Scene("Step 10: the updated chart",
          "Step ten. Open the K O chart again. It is longer, and the new signals continue the "
          "numbering. That is what automation means: the rule is applied the same way every time "
          "you add data.", "shot", "r10-chart-updated"),

    part("6", "The flowchart", "BPMN, with bpmn.io"),
    Scene("The example flowchart",
          "A flowchart says, in shapes, what the script does and in what order. This is the "
          "example's flowchart in BPMN, opened in bpmn dot io from the dot bpmn file. A thin circle "
          "starts it. Tasks are rounded rectangles, named with a verb. A diamond with an X is a "
          "yes or no question, with every arrow labelled. There are two loops: one gateway asks "
          "whether a file is left, and one asks whether a bar is left.",
          "web", "bpmn-example-open"),
    Scene("Shapes tied to code",
          "Each numbered shape stands for lines of the example script, and the handout's table "
          "gives them. Your flowchart must do the same: every shape should point at lines of your "
          "script, and every loop and decision in your code should be a shape.",
          "page", "Which lines of the example script", (0.0, 0.7)),
    Scene("Drawing: a blank diagram",
          "Now let's draw a few shapes in bpmn dot io. Open demo dot bpmn dot io and choose create "
          "a new diagram. It starts with one start event. Double click it and name it, for example "
          "Run the script.", "web", "bpmn-draw-1"),
    Scene("Drawing: a task",
          "Pick the rounded rectangle from the palette on the left, or use the arrow on the start "
          "event, and place a task after it. Name it with a verb: Read the file into a table.",
          "web", "bpmn-draw-2"),
    Scene("Drawing: a gateway",
          "Add a diamond gateway for a question, and name it with the question: Gap up and back to "
          "the previous high?",
          "web", "bpmn-draw-3"),
    Scene("Drawing: label the arrow",
          "Add the task that happens when the answer is yes, and click the arrow to label it yes. "
          "Every arrow leaving a gateway needs a label.", "web", "bpmn-draw-4"),
    Scene("Drawing: an end event",
          "Finish with a thick circle, an end event. Every path must reach one. When you are done, "
          "use the buttons at the bottom left to download your diagram as a dot bpmn file, and as "
          "an image or print it to a PDF. The PDF is the preferred submission.",
          "web", "bpmn-draw-5"),

    part("7", "Your task", "your own script and flowchart"),
    Scene("Your task",
          "Your task is your own R script that applies one rule from Chapters one to seven and meets "
          "the contract, and a flowchart of how it works. Reuse Oops, or choose Hikkake, or another "
          "rule where the slides give exact buy and stop prices. Write the rule's name and slide "
          "numbers in a comment at the top. Where the slides leave something open, choose the "
          "simplest thing and say so. Do not bring in outside indicators.",
          "page", "7. Your task", (0.0, 0.45)),
    Scene("What to submit",
          "Submit two files, named exactly. Your script: FirstAutomation, underscore, your surname, "
          "underscore, your first name, dot R. Your flowchart: the same name with underscore "
          "Flowchart, as a PDF, which is preferred, or a dot bpmn file, or a Markdown file with a "
          "Mermaid flowchart. Do not send price files or output.",
          "page", "7. Your task", (0.35, 0.72)),
    Scene("Check before you submit",
          "Before you submit, check five things. Run your script in a clean folder with no changes "
          "and no installs. Check signals dot csv has the five columns and a chart exists for each "
          "file. Delete the output folder and run again. Run with an empty data folder, and it "
          "should not crash. And open your flowchart next to your script: every shape has lines "
          "behind it. The marker runs your script on files you have not seen, in both date layouts, "
          "and one file may have no signals.",
          "page", "7. Your task", (0.6, 1.0)),

    part("8", "Using AI"),
    Scene("The AI rule",
          "You may use AI to help write your script. The condition is that you can properly "
          "visualise and explain it in your flowchart. The flowchart must match the script you "
          "actually submit. Each task must say, in your own words, what that part of the code does, "
          "and where the rule has a number, which slide it comes from. If you cannot explain a part "
          "of the script, do not submit it. A script that runs perfectly with a flowchart that does "
          "not match it loses the flowchart marks.",
          "page", "8. Using AI", (0.0, 0.6)),

    part("9", "How it is marked", "one hundred points"),
    Scene("The marks",
          "One hundred points. Sixty are checked against the record by running your script on files "
          "you have never seen: ten for running, ten for writing the files the contract names, "
          "twenty for finding the right signals, ten for the right prices, and ten for the chart "
          "showing them. Forty are judged from your flowchart: ten for correct BPMN, fifteen for "
          "matching your script, and fifteen for explaining each step. How your code looks is not "
          "marked.",
          "page", "9. The marks", (0.0, 0.6)),
    Scene("The rubric",
          "The judged marks use the course's written answer rubric. An answer is marked on whether "
          "it is grounded, pointing at something specific you can check, and connected, so the "
          "conclusion follows. Naming what argues against you is never marked, but it is what the "
          "best answers do. The levels are full, partial, minimal and none, and the handout shows "
          "an example of every level.",
          "page", "How a written answer is marked", (0.0, 0.7)),

    Scene("Good luck",
          "That is the whole activity. Install R and RStudio, get your prices from Google Sheets, "
          "run the example, then write your own script and draw its flowchart. Read the handout "
          "again whenever you are stuck, and good luck.",
          "card", card=("Good luck", "Script + flowchart", "100 points")),
)
