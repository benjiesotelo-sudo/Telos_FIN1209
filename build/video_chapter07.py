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


def _corr() -> dict:
    import json
    from pathlib import Path
    f = Path(__file__).resolve().parent / "generated" / "activity2" / "why_info.json"
    try:
        return json.loads(f.read_text()).get("corr", {})
    except OSError:
        return {}


_C = _corr()

SCENES = (
    Scene("Welcome",
          "This is a short guide to your first automation. You will teach R to read three window oscillators from "
          "Chapter 8: the R S I, the M A C D, and the stochastic. For each day it finds each oscillator's buy or sell "
          "signal, counts how many agree, and gives the price to act at. You need R and RStudio, both free, and one "
          "package, T T R. The handout has the links.",
          "web", "posit-rstudio"),
) + _sheets_scenes() + (
    Scene("The flowchart",
          "Here is what the script does, as a B P M N flowchart in four stages. Data in: one price file per stock, with a "
          "date, four prices, and a volume. Measure: for each day, the R S I, the M A C D and the stochastic, each with "
          "its rule written beside it, and its slide. A signal is the day one line crosses another. Decide: count how "
          "many of the three crossed the same way. None means skip the day. Otherwise choose buy or sell by the net "
          "vote, and set the price: a buy at the day's high, which is Lim's trigger, and a sell at the close, which is "
          "our choice. Report: a chart, a summary for each stock, and one table of the signals.",
          "web", "bpmn-example-open"),

    Scene("Start a script",
          "Now we write it. In RStudio choose File, New File, R Script. Save it in your First Automation folder, next "
          "to the data folder. Then Session, Set Working Directory, To Source File Location.",
          "clip", "00-new-script"),
    Scene("Step 1: read a file",
          "Step one: read a price file. A variable holds a value. Read dot csv opens the file as a table, one row per "
          "day, and as dot Date turns the Google Sheets date into a real date. Run it with Code, Source.",
          "clip", "01-read"),
    Scene("Step 2: the RSI",
          "Step two: a package. T T R holds the indicators, and you install it once with install dot packages. "
          "Library loads it. R S I gives the relative strength index, fourteen days, plain averages as on slide "
          "195.",
          "clip", "02-rsi"),
    Scene("Step 3: a crossing",
          "Step three: a crossing is a signal. This small function gives plus one on the day one line crosses above "
          "another, and minus one when it crosses below. The R S I crossing fifty is the signal on slide 74. Here are "
          "the days it happened.",
          "clip", "03-cross", speed=1.4),
    Scene("Step 4: three oscillators",
          "Step four: the other two. The M A C D is a twelve day average minus a twenty six day average, with a nine "
          "day signal line, slides 166 to 168. Its signal line crossing is on slide 83. The stochastic is on slide "
          "187. Add the three signals to get a vote: positive is a buy, negative a sell.",
          "clip", "04-three", speed=1.6),
    Scene("Step 5: the table",
          "Step five: the table. One row per signal day: the date, buy or sell, the entry price, what each "
          "oscillator said, and how many agree. A buy uses the day's high, slide 201. The slides give no sell "
          "trigger, so a sell uses the close. That is our choice, not Lim's rule.",
          "clip", "05-table", speed=1.6),
    Scene("Step 6: the chart",
          "Step six: the chart. Price on top, the three oscillators below, and a triangle on every signal day. Green "
          "up is a buy, red down is a sell, and the big numbered ones are where two or more agree.",
          "clip", "06-chart", speed=1.5),
    Scene("Step 7: every file",
          "Step seven: do it for every file in the data folder, and print a line per stock. That is the whole "
          "script. Source it.",
          "clip", "07-files", speed=3.0),

    Scene("The answer",
          "Here is the answer for each stock: how many signal days, and how many had two or more oscillators "
          "agreeing. The numbers are in the table.",
          "frame", "07-files", crop=(0, 545, 650, 900)),
    Scene("The table",
          "Here is the table. Each row is a signal day, with the side, the entry price, each oscillator's signal, "
          "and the agree count.",
          "clip", "08-outputs"),
    Scene("The chart",
          "And the chart. Price on top, then the R S I with its fifty line, the M A C D with its signal line, and "
          "the stochastic. The big numbered triangles are the days two oscillators agreed. Notice the M A C D panel is empty at the start: it needs about thirty four days of history first. So for your own stock, pull about a year.",
          "gen", "start/KO"),
    Scene("Add new data",
          "That is the automation. Download the files again with a later end date, replace them, and run the script "
          "again. The table and the charts update.",
          "clip", "09-update", speed=1.5),

    Scene("Why a buy",
          "Now the justification. The script gives numbers. This is what they mean. Take a real buy from the KO "
          "table. On the day line, the R S I crosses up through fifty, and the stochastic crosses up through its "
          "signal line. Two of three agree, and that is the buy signal. The price to act at is that day's high, the "
          "entry, as slide 201 says. The M A C D did not cross that day, so it is empty in the table.",
          "gen", "why/why-buy"),
    Scene("Why a sell",
          "The sell is the mirror image. Here the M A C D crosses down through its signal line, and the stochastic "
          "crosses down too. The slides give no sell trigger, so the entry is that day's close. That is our choice, not Lim's rule.",
          "gen", "why/why-sell"),
    Scene("False consensus",
          "But agreeing is not proof. All three are built from the same closing prices. On this data the R S I and "
          "the stochastic correlate at " + str(_C.get("rsi_stoch", "")) + ", and the R S I and M A C D at " +
          str(_C.get("rsi_macd", "")) + ". Lim calls this multicollinearity, a false consensus and a false sense of "
          "confidence. His cure is oscillators built from different data, such as volume.",
          "card", card=("Agreeing is not proof", f"RSI and stochastic: correlation {_C.get('rsi_stoch', '')}",
                        f"RSI and MACD: correlation {_C.get('rsi_macd', '')}", "Lim, slide 78: multicollinearity = false consensus")),

    Scene("Your task",
          "Your task: your own stock, and your own pair of the three oscillators. Write your script, and draw its "
          "flowchart. The due date is in the manual.",
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
