"""The guide video's scenes, as data: one picture or recording and what is said over it.

The same list makes the narration script the captain can record himself and the
computer-voice video, so the two cannot differ. It is a guide, not a reading of the
handout: every scene shows the real screen, a chart, or one large clean visual of what
the voice says. Order: get the data, the flowchart (shown, not drawn), write the script
(typed for real in RStudio), run it and read the answer, why each signal is where it is,
then the task.

`kind` says where the picture comes from:
  card    a title or summary card drawn from `card`
  shot    a screenshot in chapter-07/activity/screens/ (`ref` = name)
  web     a capture of a public web page in build/generated/video/web/
  clip    a screen recording in data/.../rec/ (`ref` = file stem), paced to the narration
          (`speed` plays it faster)
  frame   the last frame of a recording, optionally cropped to `crop` (pixels), enlarged
  gen     an image R drew, in build/generated/activity2/ (`ref` = path without .png)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Scene:
    title: str
    say: str
    kind: str = "card"
    ref: str = ""
    card: tuple = ()
    label: str = ""
    speed: float = 1.0
    crop: tuple = ()


SHEETS_SLOT = "sheets-recording"      # rec/sheets-recording.mp4 replaces the four stills when it exists


def _sheets_scenes() -> tuple:
    from pathlib import Path
    rec = Path("/Users/benjie/.treehouse/benjie-agent-workspace-8bf1b0/1/benjie-agent-workspace/data/fin1209-activity2/rec") / f"{SHEETS_SLOT}.mp4"
    steps = (
        ("Sheets: a blank spreadsheet",
         "First, the data. Open sheets dot new in your Google account, and click cell A1.", "g1-blank-sheet"),
        ("Sheets: the formula",
         "Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. "
         "Change only the ticker to pick another US company. For Coca Cola it is N Y S E colon K O.", "g2-formula"),
        ("Sheets: the result",
         "Sixty four rows fill in, with Date, Open, High, Low, Close and Volume. The dates look like seven slash one "
         "slash twenty twenty six. The script reads them as they are.", "g3-result"),
        ("Sheets: download",
         "Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. "
         "Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.",
         "g4-download-menu"),
    )
    if rec.is_file():
        return (Scene("Sheets: the whole routine, recorded", " ".join(x[1] for x in steps), "clip", SHEETS_SLOT),)
    return tuple(Scene(t, say, "shot", ref, label="STILL SCREENSHOT: the screen recording of this step is still to be added")
                 for t, say, ref in steps)


SCENES = (
    Scene("Welcome",
          "This is a short guide to your first automation. You will teach R one rule from Chapter 7, Larry Williams' "
          "Oops, so that it finds the buy and sell prices for you. You need R and RStudio, both free. The handout has "
          "the download links.",
          "web", "posit-rstudio"),
) + _sheets_scenes() + (
    Scene("The flowchart",
          "Here is what the script will do, as a B P M N flowchart. The input is the price files in the data folder. "
          "The process: for every stock, go day by day. Did the day open above yesterday's high, then come back down "
          "to it? That is a sell, with the stoploss at today's high. Did it open below yesterday's low, then come back "
          "up to it? That is a buy, with the stoploss at today's low. The output is three things: an answer for each "
          "stock, a chart with every signal marked, and a table of all the signals.",
          "web", "bpmn-example-open"),

    Scene("Start a script",
          "Now we write it. In RStudio, choose File, New File, R Script. Save it in your First Automation folder, "
          "next to the data folder. Then choose Session, Set Working Directory, To Source File Location, so R looks "
          "for the data folder here.",
          "clip", "00-new-script"),
    Scene("Step 1: read a file",
          "Step one: read a file. A variable holds a value, so ticker holds the text KO. Read dot csv opens the file as "
          "a table, one row per day. Run it with Code, Source, and the first three rows appear.",
          "clip", "01-read"),
    Scene("Step 2: clean the date",
          "Step two: clean the date. Cut the time off the text, and turn it into a real date. Google Sheets writes "
          "month, day, year, and the script copes with that.",
          "clip", "02-date"),
    Scene("Step 3: test one day",
          "Step three: test one day. Yesterday is row i minus one. Did today open above yesterday's high? Did "
          "today's low come back down to it? Both true means the Oops on slide 194 happened that day.",
          "clip", "03-test"),
    Scene("Step 4: test every day",
          "Step four: test every day. A for loop repeats the test for each day. If the Oops happened, print a sell, "
          "with the entry and the stoploss. Else if the day mirrors it, slide 199, print a buy. Here are the signals.",
          "clip", "04-loop", speed=1.3),
    Scene("Step 5: keep the signals",
          "Step five: keep them. Each signal becomes a row in a table, and write dot csv saves the table in an "
          "output folder.",
          "clip", "05-table", speed=1.6),
    Scene("Step 6: draw the chart",
          "Step six: draw the chart. The price line, a red triangle at each sell price, a green triangle at each buy "
          "price, and each signal's number.",
          "clip", "06-chart", speed=1.5),
    Scene("Step 7: every file",
          "Step seven: do it for every file in the data folder, and print a plain answer for each stock. That is the "
          "whole script, about forty lines. Source it.",
          "clip", "07-files", speed=2.5),

    Scene("The answer",
          "Here is the answer. For each stock, how many signals, and the latest one: sell at eighty seven twenty eight, "
          "with the stoploss at eighty seven fifty two. That is the price the rule says to act at.",
          "frame", "07-files", crop=(0, 545, 650, 900)),
    Scene("The table",
          "And the table. Every signal, with the date, side, entry price and stoploss.",
          "clip", "08-outputs"),
    Scene("The chart",
          "And the chart. The line is the closing price. Each red triangle is a sell, each green triangle is a buy, "
          "at the entry price, numbered like the table.",
          "gen", "start/KO"),
    Scene("Add new data",
          "That is the automation. Download the files again with a later end date, replace them, and run the "
          "script again. The table and the charts update. Nothing else changes.",
          "clip", "09-update", speed=1.5),

    Scene("Why a sell",
          "Why is that a sell? Take one real signal from the KO table, zoomed in. One: yesterday's high, eighty seven "
          "fifteen. Two: today opens above it, at eighty seven eighty six. Three: price comes back down to eighty "
          "seven fifteen. The sell order waits there, so that is the sell price. The gap failed, which is the idea "
          "of the Oops. Four: the stoploss, today's high. If price went there instead, the sale was wrong, and the "
          "trade is closed.",
          "gen", "why/why-sell"),
    Scene("Why a buy",
          "The buy is the mirror image. One: yesterday's low. Two: today opens below it. Three: price comes back up "
          "to it, and that is the buy price. Four: the stoploss, today's low. These are the prices a rule gives, "
          "not a forecast.",
          "gen", "why/why-buy"),

    Scene("Your task",
          "Your task: write your own script for Oops, Hikkake, or another Chapter 1 to 7 rule with exact prices, "
          "and draw its flowchart.",
          "card", card=("Your task", "Your own script", "plus a flowchart of it", "Oops, Hikkake or another exact-price rule")),
    Scene("Submit",
          "Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. "
          "And the flowchart, with the same name plus Flowchart, as a P D F, a dot bpmn file, or a Markdown file.",
          "card", card=("Submit two files", "FirstAutomation_Surname_Firstname.R",
                        "FirstAutomation_Surname_Firstname_Flowchart.pdf", "(or .bpmn, or .md with Mermaid)")),
    Scene("AI",
          "You may use AI to help write the script. The condition: your flowchart must match the script you submit "
          "and explain each step in your own words.",
          "card", card=("AI is allowed", "if you can explain it", "The flowchart must match the script you submit")),
    Scene("Marks",
          "One hundred points. Sixty are checked by running your script on files you have never seen. Forty are "
          "judged from your flowchart. The handout has the details. Good luck.",
          "card", card=("100 points", "60: your script, run on unseen files", "40: your flowchart", "Code style is not marked")),
)
