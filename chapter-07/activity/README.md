# Chapter 7, Activity 2 - First Automation FIN1209 (v6: buy or sell)

A take-home in which students automate one question for a stock they choose: should I buy today, or, if I own it, should I sell?
A script of six labelled blocks takes four settings at the top (`mode`, `stock`, `bought_price`, `bought_date`), reads a Google Sheets
price file, takes five votes a day (price trend, Chapter 5; price bar, Chapter 7; RSI, MACD and stochastic, Chapter 8), keeps the
days when at least 3 of the 5 agree, and answers: BUY or WAIT in buy mode, SELL now or HOLD in sell mode. It writes
`output/answer.txt`, `output/signals.csv` and a chart with today's answer marked. Worth **100** points (60 run against the record in
both modes, 40 from the student's flowchart). Students get the manual, a video, the example script and the example flowchart, and
**no price files**. The manual says on its first page that the program is not foolproof.

| File (in `First Automation FIN1209/`) | Who | What |
|---|---|---|
| `First Automation FIN1209.pdf` | Students | The manual, with a block by block walkthrough of the script |
| `... - Example Script.R` | Students | About 90 lines, base R plus `TTR`, no pipe operators |
| `... - Example Flowchart.pdf / .svg / .bpmn` | Students | BPMN in five stages: settings and data, five votes, signal days, answer (mode, buy signal today, sell signal or stop), report |
| `... - Narration Script.md`, `... .srt` | Instructor | What the video says, scene by scene; the subtitles |

The grading key, the unseen test files, the oracle and the grader are **not in this repository**.

## What the script answers, and what is our choice

| Answer | Rule | Source |
|---|---|---|
| signal day | at least 3 of the 5 votes agree | **our choice** (the slides do not say how many) |
| BUY (buy mode) | last row is a buy signal day: enter above its high, stop at its low | Chapter 8 slide 201 for the trigger; the stop is our choice |
| WAIT | not a buy signal day: shows the last buy signal and "3 of 5 on BUY" | |
| SELL now (sell mode) | a sell signal day after the bought day, or a later close below the stop | the sell trigger is the mirror of slide 201 (our choice) |
| HOLD | neither | |
| stop | the low of the signal day (buy) or of the bought day (sell) | **our choice**; Chapter 5 slide 74 gives the idea (a stop just below a significant trough) and no rule |
| today | the last row of the file: the latest trading day in the download, **not a live price** (Google Sheets can be about 20 minutes late) | said plainly in the manual |

## The rules behind each vote, and the slide each comes from

Votes are +1 BUY, -1 SELL; each is cited in the script comment and the manual.

| Vote or check | Rule | Slides (student edition) |
|---|---|---|
| trend | close above its 3 bar average (PLdot) is up | Chapter 5, 109 "Drummond geometry", 110 "Reading a PLdot line" |
| bar | key reversal: bearish = higher high and close at or below the previous close; bullish = lower low and close at or above | Chapter 7, 123 "The key reversal is when a strong move suddenly turns", 126 "The bullish key reversal is the same rule in the opposite direction" |
| volume (not a vote) | above-average volume marks a signal CONFIRMED | Chapter 7, 128 "Figure 7.15 shows the key reversal on the book's chart" |
| rsi | RSI 14 (plain averages) crossing 50 | Chapter 8, 74, 193 to 195 |
| macd | MACD 12/26 (EMAs) over its 9 signal line | Chapter 8, 83, 166 to 168 |
| stoch | fast %K 14 over %D 3 | Chapter 8, 185, 187, 189 |
| entry | a BUY triggers above the signal day's high | Chapter 8, 201 |

**Our choices, said in the manual and the video:** a SELL triggers below the signal day's low, the mirror of slide 201 (the slides give no sell trigger; the Chapter 1 to 8
Student Editions were searched again for one. The only short trigger Lim draws is for the ID/NR6 pattern, Chapter 7 slide 207, at
the low of a bar, one pattern only, so it is cited as support, not used as the rule). `entry` is a trigger level for both sides:
the trade happens only if price later goes beyond it. The manual's first page says the program is not foolproof;
the trend averages closes (slide 110's own chart; the book's PLdot averages typical price, which Chapter 5 does not
define); "near or below the previous close" is read as at or below; "above-average volume" is the average of the
whole file, because the slides give no period (it looks ahead, which is a known limit); Chapter 2's peaks and
troughs trend is not computed. A signal day needs at least 3 of the 5 votes on one side (our choice); `agree` counts the votes on the winning side. Lim's warning that oscillators built from the same prices give a false
consensus (slides 78 and 81) is the point of the justification part. The script prints no "why" text.

## Build order

```
.venv/bin/python build/run_stages.py --data <folder with start/ and update/ price files>
.venv/bin/python build/build_flowchart.py
.venv/bin/python build/build_activity2.py
.venv/bin/python build/build_video.py --video-out <path outside the repo>.mp4 [--voice NAME]
```

`run_stages.py` runs the committed script for real in six scenarios (buy WAIT on Coca Cola, buy BUY on Ford on a file downloaded a day
earlier, sell SELL now on Coca Cola, sell SELL now on Ford for the video's opening example, sell HOLD, plus buy mode on the update file)
by changing only the four settings lines, and records the printed answers, the first rows of
`signals.csv` and the charts (`build/generated/activity2/modes.json`); it also draws the two "why" charts (`build/r/explain_osc.R`,
`explain_bar.R`). The manual's walkthrough (Part 5) and the video's code scenes both come from `build/walk_chapter07.py`, which finds every
line number in the committed script by its text and fails the build if a line or key part is not there, so the manual, the file and the
video cannot differ. The narration is audio made from the scene list, so swapping the voice is `--voice` on the last command.

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

## The video

One block by block walkthrough, no RStudio recording needed: the labelled blocks and highlighted lines are drawn from the committed script,
and each printed answer is real Rscript output. Order: a real opening example (Coca Cola in buy mode, then Ford in sell mode, both run for
real with Rscript so the trigger price, stop, and gain or loss are not invented), welcome, a "not foolproof" card, the instructor's
own Google Sheets recording (four pieces, his account picture covered), the flowchart as bpmn.io draws it, the six blocks (each important
line highlighted whole and explained, then its key part boxed and explained), the four answers, the chart and table, new data, the why part,
"not foolproof" again, and the task. Subtitles are burned in and match the narration word for word (spelled-out letters and code names are
written as typed); every caption is its own `say` clip, timed from its own ffprobe duration, never a share of a longer sentence guessed by
character count. Every picture leaves a blank strip below it for the caption (the canvas is taller than the picture itself: see
`build/build_video.py`'s PICTURE_H and SUBH), so a caption never covers the chart, the code, the output or the Sheets recording.
`First Automation FIN1209.srt` carries the same text as the burned-in captions. The video (about 17 minutes) is too large for git and is
delivered with the student set. `screens/r03-working-dir.png` is the only RStudio capture the manual still uses.
