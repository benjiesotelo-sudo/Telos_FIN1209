# Chapter 7, Activity 2 - First Automation FIN1209

A take-home in which students automate three Chapter 8 window oscillators in R: a Google Sheets price
file in a folder, a short script, a signals table and a chart, and the same again when new rows are added.
Worth **100** points. The students get the manual, a video, the example script and the example
flowchart (PDF and `.bpmn`), and **no price files**.

| File (in `First Automation FIN1209/`) | Who | What |
|---|---|---|
| `First Automation FIN1209.pdf` | Students | The manual: install, where the data comes from, what the script does, the three rules, the script in seven steps, running it, why the signals are where they are, the contract, the task, the AI rule, the marks and the course rubric |
| `... - Example Script.R` | Students | About 47 lines, base R plus `TTR`. Numbers only |
| `... - Example Flowchart.pdf / .svg / .bpmn` | Students | BPMN with four stages, a data object for the input, each metric's rule and slide, the agreement gateway, the output objects and the next-file loop |
| `... - Narration Script.md` | Instructor | What the video says, scene by scene, to record in his own voice |

The grading key, the unseen test files, the oracle and the grader are **not in this repository**.

## The rules, from the Chapter 8 student edition

RSI over its 50 line (slides 74, 193 to 195: 14 days, plain averages); MACD (12, 26, 9, EMAs, not percent)
over its signal line (slides 83, 166 to 168); stochastic fast %K (14) over %D (3) (slides 185, 187, 189). A
signal day is a day at least one oscillator crosses; `agree` counts how many gave the winning side. A BUY's
entry is the signal day's high (slide 201). **The slides give no sell trigger, so a SELL uses the close; that is
our choice and the manual and video say so.** Lim's warning that oscillators built from the same prices give a
false consensus (multicollinearity, slides 78 and 81) is the point of the justification part: it is shown with
the real correlations of the example data. The script prints no "why" text; the video and manual explain.

## Build order

```
.venv/bin/python build/run_stages.py --data <folder with start/ and update/ price files>
.venv/bin/python build/build_flowchart.py
.venv/bin/python build/build_activity2.py
.venv/bin/python build/build_video.py --video-out <path outside the repo>.mp4 [--voice NAME]
```

`run_stages.py` runs every step of the guide in R and records what R printed and the two "why" charts
(`build/r/explain_osc.R`); `activity_chapter07_code.py` holds the seven stages and the last is read from the
committed script, so the manual, the file and what is typed in the video cannot differ. The narration is
audio made from the scene list, so swapping the voice is `--voice` on the last command.

## The data

The script needs open, high, low, close and volume. Tried: Yahoo Finance (no Philippine tickers; no
download for a signed-out user; no redistribution), Stooq (no Philippine stocks; refused automated
download), PSE EDGE (copyrighted; today's prices only; no CSV), Google Sheets `GOOGLEFINANCE` (US stocks
only: `PSE:JFC` returns `#N/A`; File, Download, CSV saves values, and the Date column reads
`7/1/2026 16:00:00`, which the script reads as it is). No price data is committed or handed out. Each
student pulls the example with `GOOGLEFINANCE` from 3 November 2025 (the MACD needs about 34 bars), ending
30 September 2026 and, for the update, 30 October 2026. The files used to build the outputs are kept
privately.

## Verification

R 4.6.2 with TTR 0.24.4. The R output matches an independent Python implementation of the same rules row
for row, and the private grader scores the example 60/60 on unseen files in all three date layouts, for
the three-oscillator example and for a two-oscillator variant.

## Screenshots and the video

`screens/` holds real captures of RStudio's window taken from a clean `~/Documents` folder, and four Google
Sheets captures cropped to the sheet. RStudio is open source (AGPL) software from Posit; no written permission
note was found for its screenshots, so confirm you are content to publish them. The video is a guide shown on
screen: the RStudio part is really recorded and typed live, the flowchart is shown, the justification uses
charts R drew from the data, and the Google Sheets segment is a marked slot of still screenshots until a
recording is dropped in as `rec/sheets-recording.mp4`. It is too large for git and is delivered with the
student set.
