# Chapter 1, Activity 1 - Reading a Price Chart

The take-home that replaces the course booklet's **Homework 1**, whose entire
text was: *"CHARTING EXERCISES: Using different trading platform, Search for a
latest charts that shows different trend. Add trend lines for a clear vision of
trend then interpret the chart. (20 points)"*. Same 20 points, still ends on a
charting platform, and it now carries a rubric, a data source and a right
answer.

| File | Who it is for | What it is |
|---|---|---|
| `FIN1209-Chapter-01-Activity-1.pdf` | The students | 17 pages. Every click of Part A with a real screenshot, Part B unaided, the rubric. |
| `FIN1209-Chapter-01-Activity-1-Answer-Key.pdf` | The instructor | 20 pages. The same sheet with all 32 answers filled in, plus the reveal, the two trendlines and how to run the session. |
| `data/` | Whoever rebuilds it | The three price windows, exactly as retrieved. Public domain. |
| `screens/` | The build | 19 unaltered screen captures of Google Sheets, 1440 by 900. |

**Nothing in this folder is hand-edited except this file.** Both PDFs are build
output and the next build overwrites them.

## What the activity actually teaches

Chapter 1's dual function, made into something a student does with their hands.

**Identification** is checkable. Sixteen questions, twice, all answered by
formulas in the student's own spreadsheet, all marked right or wrong against
the record. **Forecasting** is not checkable at the moment it is written, and
the sheet says so twice, in bold, and the rubric backs it up: the forecast is
marked on its reasoning and never on its accuracy.

The Part B window stops at a decision point. The reveal, in the following
session, is what price actually did next. A student's identification can be
marked; their forecast can only be compared. That is the point.

## The data, and why it may be committed

| | Part A | Part B | The reveal |
|---|---|---|---|
| Series | Henry Hub natural gas spot price | WTI crude oil spot, Cushing OK | the same WTI series |
| FRED code | `DHHNGSP` | `DCOILWTICO` | `DCOILWTICO` |
| Window | 2013-11-01 to 2014-03-31 | 2014-02-03 to 2014-06-30 | 2014-07-01 to 2015-03-31 |
| Trading days | 102 | 103 | 189 |

Both series come from **FRED**, the Federal Reserve Bank of St. Louis, and both
are measured by the **U.S. Energy Information Administration**. FRED tags them
`public domain: citation requested` and declares the licence at
<https://fred.stlouisfed.org/legal/#copyright-public-domain>. That is why they
are in a public repository and the textbook's figures are not. They were
retrieved on **4 September 2026**:

```
curl -s 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP&cosd=2013-11-01&coed=2014-03-31'
curl -s 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO&cosd=2014-02-03&coed=2014-06-30'
curl -s 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO&cosd=2014-07-01&coed=2015-03-31'
```

**The only change made to any of the three files** was to delete the rows FRED
returns with the price blank, which are the days the market did not trade: five
in Part A, three in Part B, seven in the reveal, all United States public
holidays. No price was altered, added or removed. The worksheet tells students
this in the same words.

These series carry **closing prices only**. There is no open, no high, no low
and no volume, so every question the activity asks is one a column of closes
can answer. Nothing was invented to fill a gap.

### Why this window

Part B's window is chosen so a reasonable person can read it two ways. From the
March low onwards its peaks and its troughs both climb, which is the chapter's
own definition of a trend, and it is still climbing on the last day. Price made
its high of 107.95 seven trading days before the end and finished 1.88 below
it. So either the uptrend continues, or the failure at the high was the top.
Most students choose the first, because the picture in front of them looks
strong.

Price then fell from 106.07 to 43.39 by 17 March 2015, a fall of 59 percent.
The reveal is decisive, and the reading most of the room will have chosen is
the one that was wrong. Nobody could have known.

The window also carries the chapter's Figure 1.20 for free: two defensible
rising lines under the same troughs are broken ten days and 4.58 dollars apart,
and the key prints both and tells the marker to give full marks to either.

## Building it

```
.venv/bin/python build/build_activity.py
```

That draws the two reveal charts, prepares the screenshots, and writes both
PDFs. It fails rather than shipping a worksheet that cannot be completed: a
step whose screenshot is missing, a question with no answer in the key, or an
em dash in the copy.

| To change | Edit |
|---|---|
| A step, a question, the rubric, any wording | `build/activity_chapter01.py` |
| Which prices, which window, any computed answer | `build/activity_data.py` and the files in `data/` |
| How a reveal chart is drawn | `build/activity_charts.py` |
| How a page is laid out | `build/activitykit.py` |

Then **render both PDFs back to images and look at every page**:

```
pdftoppm -r 110 -png chapter-01/activity/FIN1209-Chapter-01-Activity-1.pdf /tmp/ws
pdftoppm -r 110 -png chapter-01/activity/FIN1209-Chapter-01-Activity-1-Answer-Key.pdf /tmp/ak
```

Two faults in this document were invisible in the source and obvious in a
rendered page: screenshots measured zero height during pagination, so five
steps landed on one sheet with two of them clipped off the bottom; and the
reveal charts printed as empty boxes because the screenshot step was deleting
the folder they had just been drawn into.

## The one live dependency

Students pull their prices with a single formula:

```
=IMPORTRANGE("<spreadsheet id>","PartA!A1:B103")
```

That id belongs to **a spreadsheet on the instructor's Google Drive**, holding
both windows on two tabs called `PartA` and `PartB`, shared **anyone with the
link can view**. Students never edit it; IMPORTRANGE needs read access and
nothing else. The id is printed on the worksheet, so it is also the one thing
here that a deleted file can break.

**Do not delete that spreadsheet, and do not change its sharing.** If it goes:

```
.venv/bin/python build/make_source_sheet.py --upload
```

That rebuilds the workbook from the committed CSV files, uploads it as a Google
Sheet, shares it read only and prints the new id. Put the id into
`SOURCE_SHEET` in `build/activity_chapter01.py` and rebuild both PDFs. Without
`--upload` it just writes the `.xlsx` for uploading by hand.

The route was chosen because it is the only one where every step of Part A can
be shown with a real screenshot. `File` then `Import` and `File` then `Make a
copy` both need a signed-in account, so neither could be captured honestly; and
`IMPORTDATA` pointed straight at FRED returns `#REF!`, because FRED sits behind
Akamai bot protection that Google's fetcher does not get past.

## `screens/`

Nineteen captures of Google Sheets at 1440 by 900, taken through
`chrome-devtools-axi` against real spreadsheets, in English because the URL
carried `?hl=en`. They are **unaltered**. The crop and any highlight a step
places them with are declared beside that step in
`build/activity_chapter01.py`, and the build applies them into
`build/generated/activity/shots/`, which is gitignored.

`s02-filipino.png` is the odd one out and is deliberate: it is the same blank
sheet loaded **without** `?hl=en`, so the menus read *File, I-edit, Tingnan,
Ipasok*. Students in Manila will see that, and step 2 of the worksheet exists
to fix it.

Screenshots of Google products may be used in instructional material under
Google's own permission for them, which is why these are committed while the
textbook's figures are not. Google Sheets and Google Drive are trademarks of
Google LLC, and nothing here implies Google endorses this course.

**There is no screenshot of the charting platform in the final step.** The step
is written from the live site and names the tool exactly, but TradingView
publishes no comparable standing permission for its chart images, so nothing of
theirs is committed here. If one is ever wanted, get permission first.

## How long it takes a student

About 90 minutes. Part A is the long half, at roughly 40 minutes, because every
click is spelled out. Part B runs 25 to 30 minutes for someone who followed
Part A, the peaks, troughs, trendline and forecast take 15, and the platform
step takes five.
