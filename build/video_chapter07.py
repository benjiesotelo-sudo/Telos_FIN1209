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
  code    the stage's code with its new lines marked and what R printed (`ref` = stage key)

Placeholders {T_SHORT}, {T_OUT} (on screen, mm:ss) and {S_SHORT}, {S_OUT} (spoken) are filled in by
build_video.py from the real start of the short version and of the outputs in the finished video.
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
    after: bool = False      # clip: play the recording first, then speak over its last frame
    popup: str = ""         # banner drawn on the picture; may hold {T_SHORT} / {T_OUT}


def _sheets_scenes() -> tuple:
    """The captain's own screen recording of Google Sheets, cut into four pieces; the voice holds the last
    frame of a piece when it needs longer than the piece lasts."""
    return (
        Scene("Sheets: a blank spreadsheet",
              "First, the data. Open sheets dot new in your Google account, and click cell A1.", "clip", "sheets-1"),
        Scene("Sheets: the formula",
              "Type the GOOGLEFINANCE formula: the ticker, in quotes, the word all, a start date, an end date, and daily. "
              "Our start is the first of July twenty twenty six, and our end is the thirtieth of September. For Coca Cola "
              "the ticker is N Y S E colon K O. About sixty rows fill in, with Date, Open, High, Low, Close and Volume.",
              "clip", "sheets-2"),
        Scene("Sheets: another company",
              "To pick another US company, change only the ticker. Here it is N Y S E colon F, for Ford. The dates look "
              "like seven slash one slash twenty twenty six. The script reads them as they are.",
              "clip", "sheets-3"),
        Scene("Sheets: download",
              "Choose File, Download, Comma Separated Values. Rename the file K O dot csv, and put it in a folder called data. "
              "Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.",
              "clip", "sheets-4"),
    )


def _info() -> dict:
    import json
    from pathlib import Path
    f = Path(__file__).resolve().parent / "generated" / "activity2" / "why_info.json"
    try:
        return json.loads(f.read_text())
    except OSError:
        return {}



def _long_form() -> tuple:
    """Every line typed at real speed, then explained: manifest-free, from the shared typing plan."""
    from typing_plan import clip_names
    import explain_chapter07 as EX
    out, prev = [], "00-new-script"
    for step in range(1, 8):
        out.append(Scene(f"Step {step}: {EX.STEPS[step][0]}", EX.STEPS[step][1], "frame", prev))
        for name, c in clip_names(step):
            if c["kind"] == "run":
                out.append(Scene(f"Step {step}: run it", EX.STEPS[step][2], "clip", name, after=True))
            elif c["kind"] == "delete":
                out.append(Scene(f"Step {step}: remove the check line", EX.DELETE_SAY, "clip", name, after=True))
            else:
                out.append(Scene(f"Step {step}: " + c["lines"][0].strip()[:40], c["say"], "clip", name, after=True))
            prev = name
    return tuple(out)


def _short_form() -> tuple:
    import explain_chapter07 as EX
    from activity_chapter07_code import KEYS
    out = [Scene("The short version",
                 "This is the short version: the same seven steps, but we do not type. Each block of the finished script is "
                 "shown, with what it does and what it produces.",
                 "card", card=("The short version", "Seven blocks, explained as blocks"))]
    for i, key in enumerate(KEYS, 1):
        out.append(Scene(f"Block {i}: {EX.STEPS[i][0]}", EX.SHORT[i], "code", key))
    return tuple(out)


_I = _info()
_C = _I.get("corr", {})
_B = _I.get("bar", {})

_FOOLPROOF = ("This program is not foolproof. It follows rules from our slides. Its signals can be wrong, and they can lose "
              "money. It is a class exercise, not advice.")
_FOOLPROOF_CARD = ("This program is not foolproof", "It follows rules from our slides",
                   "Its signals can be wrong and can lose money", "A class exercise, not advice")

SCENES = (
    Scene("Teaser",
          "In the next half hour you will build a program that reads a stock's prices and, for every day, counts five votes "
          "for buy or sell. It draws this chart. It writes this table. And when new prices arrive, it updates both by "
          "itself. You do not need to know how to code, because we type every line together, and explain it. Let's build it.",
          "teaser", "teaser"),
    Scene("Welcome",
          "This is a short guide to your first automation. You will teach R to read price, bars and volume, from "
          "Chapters 1 to 7, and three window oscillators from Chapter 8. For each day it takes five votes for buy or "
          "sell, counts how many agree, checks the volume, and gives a trigger price. You need R and RStudio, both "
          "free, and one package, T T R. The manual has the links.",
          "web", "posit-rstudio"),
    Scene("Not foolproof", "Before we start. " + _FOOLPROOF, "card", card=_FOOLPROOF_CARD),
) + _sheets_scenes() + (
    Scene("The flowchart",
          "Here is what the script does, as a B P M N flowchart in four stages. Data in: one price file per stock, with a "
          "date, four prices, and a volume. Measure: five votes for each day. The price trend, from Chapter 5. The price "
          "bar, a key reversal, from Chapter 7. And the R S I, the M A C D and the stochastic from Chapter 8, each with "
          "its rule beside it and its slide. Decide: add the votes. A signal day is a day the bar or an oscillator fires "
          "and the votes do not cancel. Choose buy or sell by the net vote, and set the trigger: a buy above the day's high, "
          "which is Lim's trigger on slide 201, and a sell below the day's low, which is the mirror of it and our choice. Volume is not a vote: above average "
          "volume marks the day confirmed. Report: a chart, a summary for each stock, and one table of the signals.",
          "web", "bpmn-example-open"),

    Scene("The long version",
          "From here there are two versions of the coding. This is the long version: we type every line, at a speed you "
          "can follow, and explain each one. If you only want the short version, which explains each block of code and "
          "not each line, skip to {S_SHORT}.",
          "card", card=("The long version", "Every line typed and explained"),
          popup="Short version: skip to {T_SHORT}"),
    Scene("Start a script",
          "Now we write it. In RStudio choose File, New File, R Script. Save it in your First Automation folder, next "
          "to the data folder. Then Session, Set Working Directory, To Source File Location.",
          "clip", "00-new-script"),
) + _long_form() + (
    Scene("Skip the short version",
          "That was the long version. Already watched it? Skip to {S_OUT}, where the outputs start, and leave out the short "
          "version.",
          "frame", "07z-run", popup="Already watched the long version? Skip to {T_OUT}"),
) + _short_form() + (
    Scene("The answer",
          "Here is the answer for each stock: how many signal days, how many had three or more votes agreeing, and how "
          "many were on above average volume. The details are in the table.",
          "frame", "07z-run", crop=(0, 594, 645, 664)),
    Scene("The table",
          "Here is the table. Each row is a signal day: the side, the trigger level, each vote, how many agree, and "
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
          "through its signal line. Those two vote buy, and the trigger is above that day's high, as slide 201 says. The trade happens only if price later goes above it.",
          "gen", "why/why-buy"),
    Scene("Why an oscillator sell",
          "The sell is the mirror image. Here the R S I and the M A C D cross down, and the trigger is below that day's low. The "
          "slides give no sell trigger, so this is the mirror of Lim's buy trigger, our choice. The trade happens only if price later falls below it.",
          "gen", "why/why-sell"),
    Scene("False consensus",
          "But agreeing is not proof. The R S I, the M A C D and the stochastic are all built from the same closing "
          "prices. On this data the R S I and the stochastic correlate at " + str(_C.get("rsi_stoch", "")) + ", and the "
          "R S I and M A C D at " + str(_C.get("rsi_macd", "")) + ". Lim calls this multicollinearity, a false "
          "consensus. His cure is data other than price, such as volume, which is why the volume check stands apart.",
          "card", card=("Agreeing is not proof", f"RSI and stochastic: correlation {_C.get('rsi_stoch', '')}",
                        f"RSI and MACD: correlation {_C.get('rsi_macd', '')}", "Lim, slide 78: multicollinearity = false consensus")),

    Scene("Not foolproof, again", "One more reminder before your task. " + _FOOLPROOF, "card", card=_FOOLPROOF_CARD),
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
