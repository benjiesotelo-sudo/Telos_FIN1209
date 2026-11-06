"""The guide video's scenes, as data: one picture or recording and what is said over it.

The same list makes the narration script and the computer-voice video, so the two cannot differ.
Order: teaser, welcome, not foolproof, get the data (the instructor's own Google Sheets recording), the flowchart, then the
script block by block (each block labelled; each important line shown whole and highlighted, then its key part boxed, with a caption
that is also spoken), the four answers run for real (BUY, WAIT, SELL now, HOLD), why the signals are where they are, not
foolproof again, and the task. No RStudio recording: every code picture is drawn from the committed script, every printed answer is
real Rscript output (build/run_stages.py).

`kind` says where the picture comes from:
  card    a title or summary card drawn from `card`
  web     a capture of a public web page in build/generated/video/web/
  clip    a screen recording in data/.../rec/ (`ref` = file stem)
  gen     an image R drew, in build/generated/activity2/ (`ref` = path without .png)
  teaser  the finished chart, the answer and the table filling in
  block   a labelled block of the script, drawn from the script (`ref` = "b3")
  walk    one line of a block highlighted whole (phase 1) or with its key part boxed (phase 2) (`ref` = "b3:r5:1")
  run     the four settings lines and the real answer of a mode (`ref` = "buy_wait")
"""

from __future__ import annotations

import re
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
    after: bool = False
    popup: str = ""


SPEAK = (            # how code and symbols are read aloud: the voice and the subtitles say the same words
    ("install.packages", "install dot packages"), ("answer.txt", "answer dot text"), ("signals.csv", "signals dot csv"),
    (".csv", " dot csv"), ("%in%", "the in operator"), ("%K", "percent K"), ("%D", "percent D"),
    ("+1", "plus one"), ("-1", "minus one"), ("RSI", "R S I"), ("MACD", "M A C D"), ("TTR", "T T R"), ("SMA", "S M A"),
    ("PLdot", "P L dot"), (" NA ", " N A "), ("KO", "K O"), ("TRUE", "true"), ("FALSE", "false"),
)


def speak(text: str) -> str:
    for a, b in SPEAK:
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


SHEETS_SLOT = "sheets-recording"


def _sheets_scenes() -> tuple:
    """The instructor's own screen recording of Google Sheets, cut into four pieces; the voice holds the last frame of a
    piece when it needs longer than the piece lasts."""
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
              "The last row is the latest trading day in your download, not the live price, and Google prices can be about "
              "twenty minutes late. Philippine stocks do not work in Sheets, so for those, see the handout's list of other sources.",
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


def _walk_scenes() -> tuple:
    import walk_chapter07 as W
    out = []
    for k, title, purpose, a, b, rows in W.blocks():
        out.append(Scene(f"Block {k}: {title}",
                         speak(f"Block {k} of 6: {title}. Lines {a} to {b}. {purpose}"), "block", f"b{k}"))
        for r, (ln, text, key, says, keys) in enumerate(rows, 1):
            out.append(Scene(f"Block {k}, line {ln}", speak(f"Line {ln}. {says}"), "walk", f"b{k}:r{r}:1"))
            if keys:
                out.append(Scene(f"Block {k}, line {ln}: the boxed part", speak(keys), "walk", f"b{k}:r{r}:2"))
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
          "In the next fifteen minutes you will build a program that looks at a stock's prices and tells you one of four things: "
          "buy today, wait, sell now, or hold. You type buy or sell, and your stock, at the top. It draws this chart, writes "
          "this table, and when new prices arrive it answers again. You do not need to know how to code, because we go through "
          "every line together. Let's build it.",
          "teaser", "teaser"),
    Scene("Welcome",
          "This is a short guide to your first automation. You will teach R to read price, bars and volume, from "
          "Chapters 1 to 7, and three window oscillators from Chapter 8. Every day it takes five votes for buy or "
          "sell, and keeps the days when at least three of the five agree. Then your setting decides: buy mode says buy "
          "or wait, and sell mode says sell now or hold. You need R and RStudio, both free, and one package, T T R. The "
          "manual has the links.",
          "web", "posit-rstudio"),
    Scene("Not foolproof", "Before we start. " + _FOOLPROOF, "card", card=_FOOLPROOF_CARD),
) + _sheets_scenes() + (
    Scene("The flowchart",
          "Here is what the script does, as a B P M N flowchart. Settings and data: you type four settings, and the script "
          "reads your stock's file. Measure: five votes for each day. The price trend, from Chapter 5. The price bar, a key "
          "reversal, from Chapter 7. And the R S I, the M A C D and the stochastic from Chapter 8, each with its rule beside "
          "it and its slide. Signal days: a day counts only when at least three of the five votes agree. Answer: if the mode "
          "is buy, today is either a buy signal, so enter above the signal day's high with a stop at its low, or you wait. If "
          "the mode is sell, you sell now if there was a sell signal since you bought or the price closed below your stop, and "
          "otherwise you hold. Report: a chart with today's answer marked, the table of signal days, and the answer file.",
          "web", "bpmn-example-open"),
    Scene("The script, block by block",
          "Now the script. It has six labelled blocks: settings, read the data, the five votes, decide, draw the chart, and "
          "write the answer. For each block we look at the important lines. First the whole line is highlighted and explained, "
          "then the key part of it is boxed. The script uses no pipe operators: every line is plain R.",
          "card", card=("The script, block by block", "Six labelled blocks", "Each line shown whole, then its key part")),
) + _walk_scenes() + (
    Scene("Run it: buy mode, wait",
          "Now we run it. In buy mode, for Coca Cola, with the file to the thirtieth of September. The answer is WAIT: no buy "
          "signal today, because none of the five votes say buy. It also shows the last buy signal in the file, with the level "
          "to enter above and the stop, and what has to happen next: three of the five votes on buy.",
          "run", "buy_wait"),
    Scene("The chart",
          "And the chart. Price on top with its three bar average, a triangle on every signal day, and a dashed line at today, "
          "labelled with the answer. Below are the volume, the R S I, the M A C D and the stochastic. Notice the M A C D panel "
          "is empty at the start: it needs about thirty four days of history first. So for your own stock, pull about a year.",
          "gen", "modes/buy_wait"),
    Scene("Run it: buy mode, buy",
          "The same file for Ford, downloaded a day earlier, ends on a day with a buy signal. The answer is BUY: enter if price "
          "trades above that day's high, with the stop at its low. This is a trigger level: the trade happens only if price "
          "later goes above it.",
          "run", "buy_signal"),
    Scene("Run it: sell mode, sell now",
          "Now sell mode. You tell the script what you paid and the day you bought. Here you bought Coca Cola on the twelfth of "
          "August. A sell signal appeared after that, so the answer is SELL now, at about the last close, with your gain or "
          "loss in percent, and the reason.",
          "run", "sell_now"),
    Scene("Run it: sell mode, hold",
          "And with the file to the thirtieth of October, and a purchase on the twelfth of October, there is no sell signal and no "
          "close below the stop, so the answer is HOLD, with your stop and your gain so far.",
          "run", "sell_hold"),
    Scene("The chart in sell mode",
          "In sell mode the chart also shows a cross where you bought, and a dotted red line at your stop.",
          "gen", "modes/sell_hold"),
    Scene("The table",
          "And the table. Each row of signals dot csv is a signal day: the side, the trigger level, the stop, what each vote "
          "said, how many agree, and whether the volume confirmed it.",
          "run", "table"),
    Scene("Add new data",
          "That is the automation. Download the file again with a later end date, replace it, and run the script again. The "
          "answer, the table and the chart update.",
          "run", "buy_update"),

    Scene("Why: a price bar on volume",
          "Now the justification. The script gives an answer. This is what the signals mean. Take a real bearish key reversal "
          "from the " + str(_B.get("ticker", "KO")) + " table. One: yesterday's high. Two: today makes a new high. Three: "
          "today closes below yesterday's close. Buyers pushed price up and could not hold it, so the bar votes sell. "
          "Four: the volume is above average, so the day is confirmed. Volume does not vote. It tells you how much "
          "weight the move carried.",
          "gen", "why/why-bar"),
    Scene("Why an oscillator buy",
          "An oscillator vote is a crossing. Here the R S I crosses up through fifty, and the stochastic crosses up "
          "through its signal line. Those two vote buy, and the trigger is above that day's high, as slide 201 says. The trade "
          "happens only if price later goes above it.",
          "gen", "why/why-buy"),
    Scene("Why an oscillator sell",
          "The sell is the mirror image. Here the R S I and the M A C D cross down, and the trigger is below that day's low. The "
          "slides give no sell trigger, so this is the mirror of Lim's buy trigger, our choice. The trade happens only if price "
          "later falls below it.",
          "gen", "why/why-sell"),
    Scene("The stop",
          "The stop is our choice too. Chapter 5, slide 74, says a stop is usually placed just below a significant trough for a "
          "long position, but it gives no rule. Ours is the low of the signal day in buy mode, and the low of the day you bought "
          "in sell mode.",
          "card", card=("Our stop", "Buy mode: the signal day's low", "Sell mode: the low of the day you bought",
                        "Our choice. Chapter 5, slide 74 gives the idea only")),
    Scene("False consensus",
          "But agreeing is not proof. The R S I, the M A C D and the stochastic are all built from the same closing "
          "prices. On this data the R S I and the stochastic correlate at " + str(_C.get("rsi_stoch", "")) + ", and the "
          "R S I and M A C D at " + str(_C.get("rsi_macd", "")) + ". Lim calls this multicollinearity, a false "
          "consensus. His cure is data other than price, such as volume, which is why the volume check stands apart.",
          "card", card=("Agreeing is not proof", f"RSI and stochastic: correlation {_C.get('rsi_stoch', '')}",
                        f"RSI and MACD: correlation {_C.get('rsi_macd', '')}", "Lim, slide 78: multicollinearity = false consensus")),

    Scene("Not foolproof, again", "One more reminder before your task. " + _FOOLPROOF, "card", card=_FOOLPROOF_CARD),
    Scene("Your task",
          "Your task: your own stock, and your own script. It has the same four settings at the top, takes the five votes, keeps "
          "the days when at least three agree, and answers in both modes. Test it: run it in buy mode, then change the mode to "
          "sell, type a price and a day you bought, and run it again. Then draw its flowchart. The due date is in the manual.",
          "card", card=("Your task", "Your own stock", "Both modes: buy and sell", "Script + flowchart")),
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
          "One hundred points. Sixty come from running your script, in both modes, on a file you have never seen. Forty come from "
          "your flowchart. Good luck.",
          "card", card=("100 points", "60: your script, run in both modes on an unseen file", "40: your flowchart",
                        "Code style is not marked")),
)
