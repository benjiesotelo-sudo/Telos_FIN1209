# Chapter 7, Activity 2 - First Automation FIN1209

A take-home in which students automate what Chapters 1 to 8 teach about reading a chart: a price trend vote
(Chapter 5), a price bar vote (Chapter 7), a volume check (Chapter 7) and three window oscillators (Chapter 8).
A Google Sheets price file goes in a folder, a short script runs, and a signals table and a chart come out, and
again when rows are added. Worth **100** points. Students get the manual, a video, the example script and the
example flowchart (PDF and `.bpmn`), and **no price files**.

| File (in `First Automation FIN1209/`) | Who | What |
|---|---|---|
| `First Automation FIN1209.pdf` | Students | The manual |
| `... - Example Script.R` | Students | About 60 lines, base R plus `TTR`. Numbers only |
| `... - Example Flowchart.pdf / .svg / .bpmn` | Students | BPMN in four stages with the input's data types, every metric's rule and slide, the signal-day gateway, the volume check, the output objects and the next-file loop |
| `... - Narration Script.md` | Instructor | What the video says, scene by scene |

The grading key, the unseen test files, the oracle and the grader are **not in this repository**.

## The rules, and the slide each comes from

Votes are +1 BUY, -1 SELL; each is cited in the script comment and the manual.

| Vote or check | Rule | Slides (student edition) |
|---|---|---|
| trend | close above its 3 bar average (PLdot) is up | Chapter 5, 109 "Drummond geometry", 110 "Reading a PLdot line" |
| bar | key reversal: bearish = higher high and close at or below the previous close; bullish = lower low and close at or above | Chapter 7, 123 "The key reversal is when a strong move suddenly turns", 126 "The bullish key reversal is the same rule in the opposite direction" |
| volume (not a vote) | above-average volume marks a signal CONFIRMED | Chapter 7, 128 "Figure 7.15 shows the key reversal on the book's chart" |
| rsi | RSI 14 (plain averages) crossing 50 | Chapter 8, 74, 193 to 195 |
| macd | MACD 12/26 (EMAs) over its 9 signal line | Chapter 8, 83, 166 to 168 |
| stoch | fast %K 14 over %D 3 | Chapter 8, 185, 187, 189 |
| entry | a BUY at the signal day's high | Chapter 8, 201 |

**Our choices, said in the manual and the video:** a SELL's entry is the close (the slides give no sell trigger);
the trend averages closes (slide 110's own chart; the book's PLdot averages typical price, which Chapter 5 does not
define); "near or below the previous close" is read as at or below; "above-average volume" is the average of the
whole file, because the slides give no period (it looks ahead, which is a known limit); Chapter 2's peaks and
troughs trend is not computed. A signal day is a day the bar or an oscillator fires and the five votes do not cancel;
`agree` counts the votes on the winning side. Lim's warning that oscillators built from the same prices give a false
consensus (slides 78 and 81) is the point of the justification part. The script prints no "why" text.

## Build order

```
.venv/bin/python build/run_stages.py --data <folder with start/ and update/ price files>
.venv/bin/python build/build_flowchart.py
.venv/bin/python build/build_activity2.py
.venv/bin/python build/build_video.py --video-out <path outside the repo>.mp4 [--voice NAME]
```

`run_stages.py` runs every step of the guide in R and records what R printed and the two "why" charts
(`build/r/explain_osc.R`, `explain_bar.R`); `activity_chapter07_code.py` holds the seven stages and the last is read from the
committed script, so the manual, the file and what is typed in the video cannot differ. The narration is
audio made from the scene list, so swapping the voice is `--voice` on the last command.

## The data

The script needs open, high, low, close and volume. Tried: Yahoo Finance (no Philippine tickers; no
download for a signed-out user; no redistribution), Stooq (no Philippine stocks; refused automated
download), PSE EDGE (copyrighted; today's prices only; no CSV), Google Sheets `GOOGLEFINANCE` (US stocks
only: `PSE:JFC` returns `#N/A`; File, Download, CSV saves values, and the Date column reads
`7/1/2026 16:00:00`, which the script reads as it is). No price data is committed or handed out. Each
student pulls the example with `GOOGLEFINANCE` from 1 July 2026 (the MACD needs about 34 bars, so its first weeks show no
signal), ending 30 September 2026 and, for the update, 30 October 2026. The files used to build the outputs are kept
privately.

## Verification

R 4.6.2 with TTR 0.24.4. The R output matches an independent Python implementation of the same rules row
for row, and the private grader scores the example 60/60 on unseen files in all three date layouts, for
the three-oscillator example and for a two-oscillator variant.

## Screenshots and the video

`screens/` holds RStudio window captures cut from the recorded clips (`r03` to `r09`; `r07` is the chart R drew) and four
Google Sheets captures cropped to the sheet. RStudio is open source (AGPL) software from Posit; no written permission note
was found for its screenshots, so confirm you are content to publish them.

The video holds **both forms in one file**, in this order: welcome, Sheets, flowchart, the **long version** (every line typed at
real speed, one line or a short group at a time, then explained; the narration speaks over the last frame, never over the
typing), the **short version** (the same seven steps, one block each, what it does and what it produces), then the outputs, the
justification, and the task, submission, AI rule and marks. A popup at the start of the long version says where the short version
begins, and one at its end says where the outputs begin. The times are the real starts in the finished video: `build_video.py`
settles them over several passes, writes them to `build/video_times.json`, and the manual quotes that file, so **rebuild the
manual after the video** and never retype a time.

The typed order lives in `build/typing_plan.py` (shared by the recorder and the scenes) and the plain-word explanation of each
line in `build/explain_chapter07.py` (shared by the video and the manual). The recording itself is made by a private script
outside this repository that types into RStudio (frontmost check on every keystroke, menu items by name, no close shortcuts);
the video is too large for git and is delivered with the student set. The Sheets part is the instructor's own screen recording,
cut into four pieces with his account picture covered.
