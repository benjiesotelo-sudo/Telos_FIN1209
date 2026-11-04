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
         "Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. Our start is the third of November twenty twenty five. "
         "Change only the ticker to pick another US company. For Coca Cola it is N Y S E colon K O.", "g2-formula"),
        ("Sheets: the result",
         "About two hundred rows fill in, with Date, Open, High, Low, Close and Volume. The dates look like seven slash one "
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


def _info() -> dict:
    import json
    from pathlib import Path
    f = Path(__file__).resolve().parent / "generated" / "activity2" / "why_info.json"
    try:
        return json.loads(f.read_text())
    except OSError:
        return {}


_I = _info()
_C = _I.get("corr", {})
_B = _I.get("bar", {})

SCENES = (
    Scene("Welcome",
          "This is a short guide to your first automation. You will teach R to read price, bars and volume, from "
          "Chapters 1 to 7, and three window oscillators from Chapter 8. For each day it takes five votes for buy or "
          "sell, counts how many agree, checks the volume, and gives the price to act at. You need R and RStudio, both "
          "free, and one package, T T R. The manual has the links.",
          "web", "posit-rstudio"),
) + _sheets_scenes() + (
    Scene("The flowchart",
          "Here is what the script does, as a B P M N flowchart in four stages. Data in: one price file per stock, with a "
          "date, four prices, and a volume. Measure: five votes for each day. The price trend, from Chapter 5. The price "
          "bar, a key reversal, from Chapter 7. And the R S I, the M A C D and the stochastic from Chapter 8, each with "
          "its rule beside it and its slide. Decide: add the votes. A signal day is a day the bar or an oscillator fires "
          "and the votes do not cancel. Choose buy or sell by the net vote, and set the price: a buy at the day's high, "
          "which is Lim's trigger, and a sell at the close, which is our choice. Volume is not a vote: above average "
          "volume marks the day confirmed. Report: a chart, a summary for each stock, and one table of the signals.",
          "web", "bpmn-example-open"),

    Scene("Start a script",
          "Now we write it. In RStudio choose File, New File, R Script. Save it in your First Automation folder, next "
          "to the data folder. Then Session, Set Working Directory, To Source File Location.",
          "clip", "00-new-script"),
    Scene("Step 1: read a file",
          "Step one: read a price file. A variable holds a value. Read dot csv opens the file as a table, one row per "
          "day, and as dot Date turns the Google Sheets date into a real date. Run it with Code, Source.",
          "clip", "01-read"),
    Scene("Step 2: the price trend",
          "Step two, vote one: the price trend. T T R is a package of indicators. You install it once with install dot "
          "packages, and library loads it. S M A is a simple moving average. Chapter 5, slides 109 and 110: price above "
          "its three bar average is bullish, below it is bearish. Plus one for up, minus one for down.",
          "clip", "02-trend", speed=1.3),
    Scene("Step 3: the price bar",
          "Step three, vote two: the price bar. The key reversal day, Chapter 7, slides 123 and 126. A higher high "
          "than yesterday with a close at or below yesterday's close is bearish. A lower low with a close at or above "
          "is bullish. Here are the days it happened.",
          "clip", "03-bar", speed=1.3),
    Scene("Step 4: the oscillators",
          "Step four, votes three to five. A function packs lines under a name. This one gives plus one on the day one "
          "line crosses above another, and minus one when it crosses below. The R S I crossing fifty, slide 74. The M A "
          "C D crossing its signal line, slide 83. The stochastic percent K crossing percent D, slide 187.",
          "clip", "04-osc", speed=1.8),
    Scene("Step 5: the votes and the table",
          "Step five: count the votes. A signal day is a day the bar or an oscillator fires and the votes do not "
          "cancel. Positive is a buy, negative a sell, and agree counts the votes on that side. A buy uses the day's "
          "high, slide 201. The slides give no sell trigger, so a sell uses the close. That is our choice, not Lim's "
          "rule. Volume above the average marks the day confirmed, slide 128.",
          "clip", "05-table", speed=1.8),
    Scene("Step 6: the chart",
          "Step six: the chart. Price on top with its three bar average, then volume, then the three oscillators. A "
          "triangle on every signal day, green up for a buy and red down for a sell, and the big numbered ones are "
          "where three or more votes agree.",
          "clip", "06-chart", speed=1.6),
    Scene("Step 7: every file",
          "Step seven: do it for every file in the data folder, and print a line per stock. That is the whole script. "
          "Source it.",
          "clip", "07-files", speed=3.0),

    Scene("The answer",
          "Here is the answer for each stock: how many signal days, how many had three or more votes agreeing, and how "
          "many were on above average volume. The details are in the table.",
          "frame", "07-files", crop=(0, 545, 650, 900)),
    Scene("The table",
          "Here is the table. Each row is a signal day: the side, the entry price, each vote, how many agree, and "
          "whether the volume confirmed it.",
          "clip", "08-outputs"),
    Scene("The chart",
          "And the chart. Price on top, then volume, the R S I with its fifty line, the M A C D with its signal line, "
          "and the stochastic. Notice the M A C D panel is empty at the start: it needs about thirty four days of "
          "history first. So for your own stock, pull about a year.",
          "gen", "start/KO"),
    Scene("Add new data",
          "That is the automation. Download the files again with a later end date, replace them, and run the script "
          "again. The table and the charts update.",
          "clip", "09-update", speed=1.5),

    Scene("Why: a price bar on volume",
          "Now the justification. The script gives numbers. This is what they mean. Take a real bearish key reversal "
          "from the " + str(_B.get("ticker", "KO")) + " table. One: yesterday's high. Two: today makes a new high. Three: "
          "today closes below yesterday's close. Buyers pushed price up and could not hold it, so the bar votes sell. "
          "Four: the volume is above average, so the day is confirmed. Volume does not vote. It tells you how much "
          "weight the move carried.",
          "gen", "why/why-bar"),
    Scene("Why an oscillator buy",
          "An oscillator vote is a crossing. Here the R S I crosses up through fifty, and the stochastic crosses up "
          "through its signal line. Those two vote buy, and the price to act at is that day's high, as slide 201 says.",
          "gen", "why/why-buy"),
    Scene("Why an oscillator sell",
          "The sell is the mirror image. Here the R S I and the M A C D cross down, and the entry is the close. The "
          "slides give no sell trigger, so that is our choice.",
          "gen", "why/why-sell"),
    Scene("False consensus",
          "But agreeing is not proof. The R S I, the M A C D and the stochastic are all built from the same closing "
          "prices. On this data the R S I and the stochastic correlate at " + str(_C.get("rsi_stoch", "")) + ", and the "
          "R S I and M A C D at " + str(_C.get("rsi_macd", "")) + ". Lim calls this multicollinearity, a false "
          "consensus. His cure is data other than price, such as volume, which is why the volume check stands apart.",
          "card", card=("Agreeing is not proof", f"RSI and stochastic: correlation {_C.get('rsi_stoch', '')}",
                        f"RSI and MACD: correlation {_C.get('rsi_macd', '')}", "Lim, slide 78: multicollinearity = false consensus")),

    Scene("Your task",
          "Your task: your own stock, and your own pair of the three oscillators, with the price trend, price bar and "
          "volume check. Write your script, and draw its flowchart. The due date is in the manual.",
          "card", card=("Your task", "Your own stock", "Your own pair of oscillators", "Script + flowchart")),
    Scene("Submit",
          "Submit two files. Your script, named First Automation, underscore, surname, underscore, first name, dot R. "
          "And the flowchart with the same name plus Flowchart, as a P D F, a dot bpmn file, or Markdown.",
          "card", card=("Submit two files", "FirstAutomation_Surname_Firstname.R",
                        "FirstAutomation_Surname_Firstname_Flowchart.pdf", "(or .bpmn, or .md with Mermaid)")),
    Scene("AI",
          "You may use AI to help. Your flowchart must match the script you submit and explain each step in your own "
          "words.",
          "card", card=("AI is allowed", "if you can explain it", "The flowchart must match the script you submit")),
    Scene("Marks",
          "One hundred points. Sixty come from running your script on files you have never seen. Forty come from "
          "your flowchart. Good luck.",
          "card", card=("100 points", "60: your script, run on unseen files", "40: your flowchart", "Code style is not marked")),
)
