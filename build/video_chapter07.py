"""The walkthrough video's scenes, as data: one picture and what is said over it.

The same list makes the narration script the captain can record himself and
the computer-voice video, so the two cannot differ. A scene whose `shot` is
None is drawn as a title card from `card`. Screenshots are the handout's own,
by name, in chapter-07/activity/screens/.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Scene:
    title: str
    say: str
    shot: str | None = None
    card: tuple[str, ...] = ()


SCENES = (
    Scene("Welcome",
          "Welcome to First Automation, FIN1209. In this activity you teach a "
          "computer one of the rules from Chapter 7. You will write a small "
          "R script. You drop price files in a folder, run the script, and it "
          "tells you where the rule says to buy or sell, saves those signals "
          "in a table, and draws a chart with each signal marked. This video "
          "follows Part 5 of the handout, where we run a finished example. "
          "Nobody needs to know R already.",
          card=("First Automation FIN1209", "Automate one of Lim's rules in R")),
    Scene("The rule",
          "The example uses Larry Williams' Oops from Chapter 7, slides 194 to "
          "199. If a bar opens above the previous bar's high, Lim places a "
          "sell-stop at the previous high and a stoploss at the new bar's "
          "high. If it opens below the previous low, it is the mirror image: "
          "a buy-stop at the previous low and a stoploss at the new low. "
          "These are the signals of a rule. They are not investment advice.",
          card=("Williams' Oops", "Gap up, then back to the previous high: SELL",
                "Gap down, then back to the previous low: BUY")),
    Scene("Before you start",
          "Install R first, then RStudio Desktop, both free. The handout has "
          "the links and the Windows and Mac steps. If you cannot install, "
          "use Posit Cloud in your browser. The example needs no R packages "
          "at all.",
          card=("Install", "1. R", "2. RStudio Desktop", "Or: Posit Cloud in the browser")),
    Scene("Step 1: the folder",
          "Step one. Copy the First Automation folder to your computer. Next "
          "to the script, make a folder called data, and copy into it the two "
          "price files from data, start here: K O dot csv and F dot csv.",
          shot="r01-folder"),
    Scene("Step 2: open the script",
          "Step two. In RStudio, choose File, Open File, and pick the example "
          "script. It opens in the top left pane.", shot="r02-open-script"),
    Scene("Step 3: set the folder",
          "Step three, the one people forget. Choose Session, Set Working "
          "Directory, To Source File Location. Without this, R cannot find "
          "the data folder.", shot="r03-working-dir"),
    Scene("Step 4: run it",
          "Step four. Click Source. R reads both files, finds the signals, "
          "draws two charts and writes the table. The console says how many "
          "signals it found in each file.", shot="r04-source"),
    Scene("Step 5: what it made",
          "Step five. The Files pane now has an output folder. Inside are "
          "signals dot csv, and one chart for each stock.",
          shot="r05-output-folder"),
    Scene("Step 6: the signals",
          "Step six. Open signals dot csv. Each row is one Oops. Side says "
          "sell or buy. Entry is the price where the stop order waits. "
          "Stoploss is where the trade is closed. Reverse is the opposite "
          "side Lim starts at the stoploss.", shot="r06-signals-csv"),
    Scene("Step 7: the chart",
          "Step seven. Open the K O chart. White candles closed up and black "
          "candles closed down. A red triangle pointing down is a sell entry. "
          "A green triangle pointing up is a buy entry. The short dash is "
          "its stoploss, and the number is the signal's row in the table. "
          "Check one yourself: find signal one in the table and see that the "
          "triangle sits at that entry price.", shot="r07-chart"),
    Scene("Step 8: add new data",
          "Step eight. This is the automation. Copy the two files from data, "
          "October update, over the ones in your data folder. They are the "
          "same two stocks with a month of new rows at the bottom.",
          shot="r08-new-data"),
    Scene("Step 9: run it again",
          "Step nine. Click Source again, and change nothing else. The "
          "counts go up, and the table and both charts are rewritten.",
          shot="r09-rerun"),
    Scene("Step 10: the updated chart",
          "Step ten. Open the K O chart again. It is longer, and the new "
          "signals continue the numbering. That is what automation means: "
          "the rule is applied the same way every time you add data.",
          shot="r10-chart-updated"),
    Scene("Your turn",
          "Now it is your turn. Write your own script for Oops, Hikkake, or "
          "another rule from Chapters 1 to 7 with exact prices, following "
          "the contract in Part 3. Then draw a flowchart of how your script "
          "works, in BPMN. AI may help you write the script, as long as your "
          "flowchart matches what you submit and explains each step. Read "
          "Parts 6 to 9 of the handout, and good luck.",
          card=("Your turn", "Script + flowchart", "Marks: 100", "Read Parts 6 to 9")),
)
