# Chapter 7, Activity 2 - First Automation FIN1209

A take-home in which students automate one of Lim's rules in R: drop price
files in a folder, run a script, get a signals table and a chart, add rows and
run it again. It is the second activity of the semester and the first that asks
students to build something. Worth **100** points.

| File (in `First Automation FIN1209/`) | Who | What |
|---|---|---|
| `First Automation FIN1209.pdf` | Students | The handout: install, the rule, the contract, R in 14 steps, running the example, the flowchart, the task, the marks and the course rubric |
| `... - Example Script.R` | Students | The finished example, base R only. Williams' Oops, Lim p. 231, slides 194 to 201 |
| `... - Example Flowchart.pdf / .bpmn / .svg` | Students | The example's BPMN flowchart; the `.bpmn` opens in bpmn.io with layout intact |
| `... - Narration Script.md` | Instructor | What to say over the screenshots, to record in his own voice |
| `data/`, `output/` | Nobody | Gitignored. Where a run reads and writes; see **The data** below |

The grading key, the unseen test files, the expected signals and the grader are
**not in this repository**. They live outside it, in the instructor's private
task folder, because they would hand a student the answer.

Nothing here is hand-edited except this file. Build order:

```
.venv/bin/python build/run_stages.py --data <folder with start/ and update/>
.venv/bin/python build/build_flowchart.py
.venv/bin/python build/build_activity2.py
.venv/bin/python build/build_video.py --video-out <path outside the repo>.mp4
```

`run_stages.py` really runs every step of the guide in R (`Rscript`) and records
what R printed, so no output in the handout is typed. `build/activity_chapter07_code.py`
holds the 14 stages; the last is read from the committed script, so the guide's
last step and the file students get cannot differ. `build/activity_chapter07.py`
is the handout's content, `build/activitykit.py` (which gained a `Code` block)
draws it, `build/bpmnkit.py` and `build/flowchart_chapter07.py` draw the flowchart,
and `build/video_chapter07.py` holds the scenes that make both the narration script
and the video.

## The rule, and what is ours

Quoted from the Chapter 7 student edition built from `origin/main`: slide 193
(stop orders), 194 (bearish Oops), 195 (trend), 197 (stop and reverse), 199
(bullish Oops). The slides leave four things open and the handout says so and
calls each the script's own choice: only the gap bar can fill the order; the
order of high and low inside a daily bar is not needed; no trend filter (slide
195 gives no computable test); no profit exit. No outside indicator is used.

## The data: what was tried, and why it is not committed

The script needs open, high, low and close, because Oops needs the open and the
previous bar's range. FRED, which Activity 1 used, carries closes only.

* **Yahoo Finance**: Philippine tickers (`.PS`) return nothing; the history page
  shows no download for a signed-out user. Its terms do not allow redistribution.
* **Stooq**: has no Philippine stocks and refused automated download. Same terms
  problem.
* **PSE Edge**: the exchange's own data is copyrighted ("protected by copyright",
  its terms page) and offers no CSV.
* **Google Sheets `GOOGLEFINANCE`**: gives Date, Open, High, Low, Close, Volume for
  **US-listed stocks** and exports to CSV (File, Download, CSV saves values, not
  formulas) with a signed-in Google account, which students have. Tested on
  4 November 2026: `NYSE:KO` filled 64 rows; **`PSE:JFC` returned `#N/A`, so there is
  no daily history for Philippine stocks.** Its Date column reads `7/1/2026 16:00:00`
  (month/day/year plus a time), and the example script reads that as it is. This is
  the route the handout walks through; for PSE stocks it says to use another source
  (for example Investing.com, which could not be checked) and save a CSV in the
  contract's layout.

So no price data is committed, and none is handed out either: the class Drive
is publicly readable, so a vendor file there would be redistribution too. Every
student pulls the example's prices themselves with `GOOGLEFINANCE` (handout
Part 4a, fixed dates so the numbers match), the same route as their own task.
The ticker is one swappable string in the formula. Copies of the files used to
build the handout's outputs are kept privately, as test fixtures, outside the
repository.

## Screenshots and the video

`screens/` holds real captures of the RStudio window and a Finder window, taken from a
clean `~/Documents/First Automation FIN1209` folder, plus four Google Sheets captures
(`g1` to `g4`, cropped to the sheet; they show no account name). `r07` and `r10` are the
script's own chart PNGs. RStudio is open source (AGPL) software from Posit; unlike the
Google captures in Activity 1 no written permission note was found for its screenshots,
so confirm you are content to publish them. There is no capture of the second download
(the update), because it is the same four steps, and the handout says so. In the
formula capture the end date reads 2026,10,30 while the handout's first run uses
2026,9,30; the handout says so beside it. Every PNG was checked for local paths and
agent names before it was committed.

The video (`build/build_video.py`, macOS `say` plus ffmpeg) covers the whole handout in
its order with a title card per part: real browser captures of the CRAN, Posit and
bpmn.io pages (shapes placed live in bpmn.io), the Sheets and RStudio captures, the 14 R
steps drawn from the guide's own stages, and zoomed handout pages where nothing honest
can be recorded. It is about 25 minutes and too large for git, so it is delivered with the
student set outside the repository.

## Verification

The example was run with R 4.6.2 on both data sets, as exported by Google Sheets. Its signals match an
independent Python implementation of the same rule exactly (33 on the start set,
46 after the update). Every stage of the guide was run and its output recorded.
