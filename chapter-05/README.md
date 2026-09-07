# Chapter 5 - Trend Analysis

138 slides, eleven parts, 21 in-class checks carrying 42 multiple choice
items, 32 terms, all 59 of the book's figures, and 26 charts of our own.

**This chapter is built to the lean form the instructor approved in Chapter
4**: the content decides the length, each question is followed by its own
answer slide, every idea that needs a picture has one beside it, and nothing
the book says is cut. `chapter-04/README.md` has the history of that form and
`TEMPLATE.md` the rules.

**Only the teaching deck is built so far.** There is no student edition, no
run card, no lecture notes, no answer sheet and no check audit document for
this chapter yet. The `--edition student` switch still works, because it
lives in `deckkit`; nothing has been built or checked with it.

| File | Who it is for | What it is | Generated from |
|---|---|---|---|
| `FIN1209-Chapter-05.pptx` | The room | The committed deck, teaching edition. Our own charts, and a placeholder where each of the book's figures goes. | `build/content_chapter05.py` |

**Nothing in this folder is hand-edited except this file.** The deck is
build output, and the next build overwrites it.

**A committed deck is not a teaching deck.** The file here carries a
placeholder where each of the 59 figures goes. The deck to teach from is the
build with the artwork, made outside the repository; see **Building it**.

## The shape

| Chapters 1 to 3 | Chapter 5 |
|---|---|
| Six parts, the template's own convention | Eleven parts, the book's sections 5.1 to 5.11. Section 5.12 is the book's summary and feeds the closing slides. |
| A divider slide and a recap slide for every part | Neither. The first slide of a part carries the book's section number in its title. |
| A picture is a slide of its own, after the slide that needs it | A picture sits beside the idea it shows, on the same slide |
| Two objectives slides and a roadmap slide, generated | One of each, written in the content module |

What did not change: one idea per slide, six body lines at the most, every
term taught plain words first and the book's own definition last, nothing
taught that the book does not teach, **a check is a question slide and then
a reveal slide**, every check answerable from slides that come before it, no
slide that refers back to a check or a chart, the answer key spread across A
to D, and no em dash anywhere. The build refuses a deck that breaks any of
the rules it can check.

A check sits in the part whose last slide it follows, so two checks ask about
two short sections each: Check 19 covers 5.7 and 5.8, and Check 20 covers 5.9
and 5.10.

## Every idea has a picture

Of the 90 teaching slides, 85 carry a picture: 84 with the picture beside
the text and one, Figure 5.32, on a slide of its own. The other 48 slides are
the 21 checks, at two slides each, and the six slides of the frame.

- **A book figure where the book has one.** All 59 are placed, each beside
  what the book says about it. Figure 5.32 stands alone because it is a wide
  table of small type, and a slide of its own is the only size it can be
  read at.
- **One of our own charts otherwise.** 26 of them, lettered A to Z. See the
  table below.

**Five slides carry no picture, and no two of them are next to each other.**
Each is a list the book gives without a figure:

| Slide | Why it has no picture |
|---|---|
| 5.2, the sixteen characteristics by name | It is the map of the part. Each of the sixteen then gets a slide and a picture of its own. |
| 5.2, characteristic 16, divergence | The book gives it one sentence and refers to Chapter 9. |
| 5.4, the other orders | Four instructions about time and conditions, one line each in the book. |
| 5.6, strengths and weaknesses | The book's own list of four strengths and three weaknesses. |
| 5.11, reversal signs from tools taught later | Oscillators, candlesticks and intermarket action: each needs a tool the book has not taught yet. |

**The 26 letters are a hard limit.** `deckkit` names a chart by one capital
letter, so a chapter can draw at most 26. This chapter uses every one. A
later chapter that needs more will have to add to the kit first.

A check may rest on what a slide's text says and never on what only its
picture shows, because the committed build prints a placeholder where a book
figure goes. All 42 items were checked against that by hand, and each is
answered by the text of a slide that comes before its check.

## The new-term marker

**A term slide is a term's first teaching in the course, and nothing else.**
The instructor's review of the first build: the uptrend carried the marker
though Chapter 2 introduced it, and HWC and MWC, which are new, did not.
Every name in the chapter was then checked against
`build/content_chapter01.py` to `content_chapter04.py`. `TEMPLATE.md` has
the rule. This is the result: 32 terms, where the first build had 8.

**Three lost the marker.** Each is now an ordinary slide, and its speaker
cue says it is a recall:

| Was a term here | Already a term in | Now |
|---|---|---|
| Uptrend | Chapter 2, *Uptrend* | An uptrend: higher highs and higher lows |
| Stop order | Chapter 1, *Limit and stop entry orders* | Stop orders: execution, but not the price |
| Limit order | Chapter 1, *Limit and stop entry orders* | Limit orders: the price, but not execution |

**Twenty seven gained it.** Each was an ordinary slide in the first build,
and each is a name the book introduces in this chapter:

| Section | Terms that gained the marker |
|---|---|
| 5.1 | Wave cycles: HWC, MWC and LWC. Wave-degree convergence. Correction and pullback. |
| 5.2 | 1 Cycle amplitude. 2 Cycle period. 3 Bar retracement symmetry. 4 Average bar range. 7 Real body to range ratio, BRR. 8 Angular symmetry and momentum. 9 Barrier proximity. 12 Third gap exhaustion. 13 Average period range. |
| 5.5 | Support and resistance role reversal. Trend filter. |
| 5.6 | Internal line. Continuation and reversal trendlines. Channel, and its return line. Nested channels. Sperandeo trendlines. DeMark trendlines. Standard fan lines. Fibonacci fan lines. Speed lines. Andrew's Pitchfork. |
| 5.8 | Common, breakaway, runaway and exhaustion gaps. |
| 5.9 | Unidirectional and bidirectional entries. |
| 5.10 | Drummond geometry. |

**Five kept it:** Bar stochastic, Slippage, Inflection point of strength N,
Proportional stopsizing and Trendline.

**A word only used earlier is still new.** Eight of the terms above were
met before without being taught, and each cue says where: slippage,
correction and inflection point were words in a sentence; trendlines,
channels and angular symmetry were drawn in earlier figures; the cycle
period was named in Chapter 4 as Chapter 20's; and the four gaps were named
in Chapter 3 "for later" and three of them met in Chapter 4 as Sakata's San
Ku. This chapter is the first to say what each one means.

**Left on ordinary slides, and why:**

| Slide | Why it carries no marker |
|---|---|
| Dow's three trends, the downtrend | Chapter 2 terms. |
| The three categories of filter | The price, time and algorithmic filters were Chapter 1 terms. |
| To go long, go short, liquidate, cover | Chapter 1 terms. |
| Failure swing, double top, non-failure swing | Chapter 2 terms. |
| 5 Price persistence | Persistence was Chapter 1's first applied assumption. |
| A trendline's minimum price target | Chapter 4's minimum measuring objective, measured from a trendline. |
| 6 The average bar stochastic ratio | Its term, bar stochastic, has the slide before it. |
| 10, 11 and 14 of the sixteen | The book's heading describes what to watch and names nothing. |
| 15 Volume spread action | Four cases. The squat bar is named as one of them. |
| 16 Divergence | One sentence, and the book defers it to Chapter 9. |
| Two-stage filtering | The book calls it two-stage, double and double-stage filtering in three sentences and settles on no name. |
| Reversal and retracement | In use since Chapter 2. They share the slide that teaches correction and pullback. |
| The other orders, the five entry modes, the exit orders, the three retracement approaches | Lists the book gives one line each. A term slide teaches one idea. |

**What the three rows cost.** A term slide has no accent and no caption, so
on eight converted slides a detail moved from the slide to its speaker cue.
None of them carries a check:

- 4 Average bar range: that the true range was Chapter 3 and its averaging
  is Chapter 8.
- Trend filter: that the three filters are by no means exhaustive. That
  moving averages are Chapter 11 is still on the slide, in the chart's
  footnote.
- Channel: that trough 6 violating the uptrend line may be an early
  indication of a trend change, and that other constructions are Chapter 13.
- Sperandeo trendlines: that the book gives only this much and advises
  reading Sperandeo's own.
- Standard fan lines: where the accelerating set ends, at gradually rising
  lower peaks, and that the book says to draw only three.
- Drummond geometry: that the inter-bar trendlines join highs and lows.
- Stop orders and limit orders: the peso example of each, which the chart
  beside each now carries.

## What each section teaches

Every section is taught as fully as the book teaches it.

| Section | Slides | Checks | Figures | Our charts |
|---|---|---|---|---|
| 5.1 Definitions of a trend | 18 | 3 | 5.1 to 5.10 | A, B |
| 5.2 Quality of trend: 16 price characteristics | 34 | 5 | 5.11 to 5.29 | C, D, E |
| 5.3 Price and trend filters | 5 | 1 | 5.30 | F, G |
| 5.4 Trend participation | 12 | 2 | 5.31, 5.32 | H to L |
| 5.5 Price inflection points | 19 | 3 | 5.33 to 5.39 | M to R |
| 5.6 Trendlines, channels and fan lines | 29 | 4 | 5.40 to 5.53 | S to X |
| 5.7 Trend retracements | 2 | | 5.54 | Y |
| 5.8 Gaps and trends | 5 | 1 | 5.55 to 5.57 | |
| 5.9 Trend directionality | 1 | | 5.58 | |
| 5.10 Drummond geometry | 3 | 1 | 5.59 | |
| 5.11 Forecasting trend reversals | 4 | 1 | | Z |

The other six slides are the title, the objectives, the roadmap and three
closing slides.

**What is short, and why.** These sections are short because the book is
short on them, not by choice:

| Section | Teaching slides | Why |
|---|---|---|
| 5.3 Filters | 3 | A page and a half in the book, and one figure. |
| 5.7 Retracements | 2 | One paragraph and one table. The book leaves the detail to "a subsequent chapter", unnamed; its Chapter 10 is Fibonacci and its Chapter 19 Gann. |
| 5.9 Directionality | 1 | Two paragraphs and one figure. |
| 5.10 Drummond geometry | 1 | One paragraph and one figure. The book refers the reader to *The Ultimate Trading Guide*. |
| 5.11 Forecasting reversals | 2 | The book calls it a summary and refers to the relevant chapters for each approach. |

Inside 5.6 the same holds for Sperandeo and DeMark trendlines, one slide
each: the book gives a brief description and sends the reader to each
author's own book.

**Used and not explained by the book here.** Each is named on the slide
where it appears, and no check rests on any of them:

| Used | Where the slide says so | Taught in |
|---|---|---|
| Typical price | 5.1 caption, 5.10 cue | not said |
| The CCI and Floor Trader's Pivot Points | 5.1, caption | not said |
| How the true range is averaged into the ATR | 5.2, cue | Chapter 8; the true range was Chapter 3 |
| The cycle-tuned stochastic | 5.2, on the slide | Chapter 8 is oscillators |
| Divergence | 5.2, characteristic 16 | Chapter 9 |
| MACD and the stochastic | 5.5, caption | not said |
| Moving averages | 5.5, the chart's footnote and the cue | Chapter 11 |
| Candlestick patterns, the shooting star | 5.8, caption | Chapter 14 |
| Elliott waves | 5.1, caption | Chapter 18 |
| How DeMark qualifies a trough | 5.6, on the slide | DeMark's own book |
| Alternative channel constructions | 5.6, cue | Chapter 13 |
| Tradesizing in general | 5.5, cue | Chapter 28 |

## The twenty six charts

A chart is drawn where the book makes a point in words that none of its own
figures shows. `build/charts_chapter05.py` holds the data and the reasoning.

| Chart | Beside | What it shows |
|---|---|---|
| A | Dow sorts trends by how long they last | Primary, secondary and minor on one line |
| B | Correction and pullback | A shallow dip beside a turn of any amount |
| C | 11 Size and duration of a consolidation | A small interruption and a large one |
| D | 13 Average period range | A day that completes its 120 pips early |
| E | 15 Volume spread action | The book's four cases, as bars over their volume |
| F | Three categories of filter | One breakout, entered three ways |
| G | Two-stage filtering | A close inside the allowed distance, and one beyond it |
| H | Buying low and selling high, four ways | Two longs and two shorts on one swing |
| I | Stop orders | A buystop above the market and a sellstop below |
| J | Slippage | A gap through a stoploss, in pesos |
| K | Limit orders | A sell limit above the market and a buy limit below |
| L | Exits, and orders at the market | The four exit orders around the current price |
| M | Ways of initiating an entry | Barrier, breakout and failed breakout entries |
| N | Inflection point of strength N | Strength 2 beside strength 10 |
| O | Trend filter | A double moving average crossover |
| P | The trouble with a varying stopsize | Tradesize against stopsize, for a fixed risk |
| Q | Proportional stopsizing | The same, capped at the proportional stopsize |
| R | Five steps to the proportional tradesize | The percentage risk that results |
| S | 5.6 Trendline | Drawn, tentative, confirmed at the third contact |
| T | Why a trendline holds: behavior | One line met from above, then from below |
| U | What counts as a valid penetration? | An intraday low through the line, and a close back above |
| V | A reliable trendline: angle and duration | Too steep, about right, too shallow |
| W | A reliable trendline: the other four | Four precise retests |
| X | Anticipating a channel breakout | A failed test of the bottom, then a break through the top |
| Y | Where the three approaches agree | The three ranges where the percentages converge |
| Z | Signs that a trend may reverse | Three kinds of sign at one market top |

**Charts P, Q and R are the book's five steps with pesos put in.** An
average stopsize of PHP 2.00, a two standard deviation value of PHP 1.00,
and PHP 10,000 at risk, so a proportional stopsize of PHP 3.00 and a
proportional tradesize of 3,333 shares. The steps are the book's and the
numbers are ours. Each chart is one line of arithmetic, not a price, and
says so.

**Chart O computes two simple moving averages** of the line it draws and
marks where they cross. How a moving average is built is Chapter 11, and no
label on the chart explains it.

Every other chart's data is invented from a fixed seed, and each says so.

**Two things about drawing them, both found by looking.** A label on a
`Stroke` is not drawn at all if the point it is attached to lies outside the
plot, so a line that runs past the last price loses its label silently; end
it inside. And a `Note` whose offset is negative is right aligned, so near
the left edge it runs off the picture.

**A chart is drawn for the slide type it sits beside.** The picture column
beside a term starts lower and is narrower than the one beside a teaching
slide, so `charts_chapter05.py` draws at two sizes, `PAIR` and `TERM`.
When the marker moved, charts B, D and O went to the term size and I and K
to the teaching size, and three of the five needed a label moved: B ran off
the left edge, D covered its own price line and an axis label, and O sat on
the time axis.

## How long the chapter takes

**245 minutes at the calibrated rate, against a 180 minute session.** That is
information, not a target: nothing was cut to reach a length, and nothing was
added. It is 65 minutes more than one session holds. No run card exists for
this chapter, so nothing here says what to cut; that is a decision for
whoever writes one. The first build cost 238: the slide count has not moved,
and the seven minutes are the 24 more slides now costed as terms.

The rate is the one written down in `chapter-03/README.md`: a content slide
1, a term 1.25, a figure 0.75, a chart 0.5, a check with its reveal 2.5,
each opening and closing slide 1, all scaled by 1.150 into minutes. A slide
with a picture beside it is costed as the sum of its two parts.
`build_chapter5.py` prints the sum on every build.

| Part | Slides | Minutes |
|---|---|---|
| Title, objectives, roadmap | 3 | 3.4 |
| 5.1 Definitions | 18 | 33.1 |
| 5.2 Quality of trend | 34 | 63.0 |
| 5.3 Filters | 5 | 8.3 |
| 5.4 Participation | 12 | 18.7 |
| 5.5 Inflection points | 19 | 34.2 |
| 5.6 Trendlines | 29 | 54.3 |
| 5.7 Retracements | 2 | 3.7 |
| 5.8 Gaps | 5 | 9.2 |
| 5.9 Directionality | 1 | 2.3 |
| 5.10 Drummond | 3 | 5.2 |
| 5.11 Reversals | 4 | 5.8 |
| Closing | 3 | 3.4 |

The weights sum to 212.75 and 212.75 times 1.150 is 244.7. The chapter is 47
pages of the book against Chapter 4's 26, and comes to 138 slides against
79, so it is the same density.

## Building it

From the repository root:

```
.venv/bin/python build/build_chapter5.py      # teaching, 138 slides
```

The build draws the 26 charts and is deterministic: a second run leaves
`git status` clean. It writes no answer sheet; see `build_chapter5.py` for
why that was taken out of the script it was copied from.

The version with the book's artwork must be written outside the repository.
Its PDF is the copy for an iPad:

```
.venv/bin/python build/build_chapter5.py \
    --with-figures --out ~/FIN1209-Chapter-05-with-figures-and-charts.pptx
soffice --headless --convert-to pdf --outdir ~ \
    ~/FIN1209-Chapter-05-with-figures-and-charts.pptx
```

Before committing the deck, confirm it embeds no artwork that is not ours.
It must hold exactly 26 images, and their hashes must match this chapter's
own chart folder:

```
unzip -l chapter-05/FIN1209-Chapter-05.pptx | grep -c ppt/media          # 26
unzip -o -d /tmp/media chapter-05/FIN1209-Chapter-05.pptx 'ppt/media/*'
diff <(shasum -a256 /tmp/media/ppt/media/*.png | awk '{print $1}' | sort) \
     <(shasum -a256 build/generated/charts-05/*.png | awk '{print $1}' | sort)
```

The deck with the book's artwork in it holds 85: the 26 charts and one for
each of the 59 figures.

Then look at every page, as an image, in the build with the artwork, because
that is what the room sees:

```
pdftoppm -r 62 -png ~/FIN1209-Chapter-05-with-figures-and-charts.pdf /tmp/ch5
```

**One thing to look for that the build does not catch.** On a reveal slide
the answer is set in the monospace face, and an answer long enough to wrap to
a second line pushes its reason past the bottom of the card when the deck is
converted to PDF. Keep every correct option to about 58 characters. Three
were shortened for that.

## `assets/figures/`

Gitignored, and never committed. The build looks for one PNG per figure,
named by the book's own figure number:

```
assets/figures/figure-5-01.png    ->    Figure 5.1
assets/figures/figure-5-59.png    ->    Figure 5.59
```

The book PDF embeds all 59 as one image each on PDF pages 152 to 195, so
`pdfimages -png -f 151 -l 197` on the course text yields 59 files. **Two
things are not as they come out.**

- **They are not all in figure order.** The two images on PDF page 162 come
  out as 5.18 and then 5.17: the bars with the bar stochastic formula are
  5.18, and the hourly GBPJPY chart is 5.17. Every other page is in order.
- **Figure 5.2 has its labels as page text, not in the image.** The
  extracted image is the bare bars: the H, L, LH and LL labels and the words
  "A downtrend unfolding" are missing. Render the figure from the page
  instead: `pdftoppm -r 300 -f 152 -l 152 -x 870 -y 1946 -W 1010 -H 988
  -png`. It is the only figure in the chapter with text laid over it.

## Where the book is silent or contradicts itself

Every one of these is named on a slide, and no check rests on any of them.

**Sixteen or twelve.** Section 5.2 lists 16 price characteristics, and so
does the chapter summary. Review question 4 asks for "the 12 ways in which
price action may be understood". The deck teaches the sixteen and the review
slide says so.

**Four modes or five.** Section 5.5 announces "four simple ways" of
initiating an entry and lists five. The slide lists the five and says so.

**Figure 5.24.** The text gives Gold's earlier trend rate as about $3.30 a
day and the figure itself prints $3.80. The book's caption under 5.24 is the
caption of Figure 5.25. The slide says both.

**Figure 5.46.** Its printed caption repeats Figure 5.45's and says Silver;
the text says USDCAD. The slide says so.

**Figure 5.21.** The caption calls it an hourly chart of 3M; the chart is
daily and the text says it covers three years. The speaker cue says so.

**Algorithmic filters.** Section 5.3 files them as one branch of the
event-based filters. Review question 8 names "time and algorithmic filters"
as though algorithmic were the third category, which is how Chapter 1's
prose put it. The slide says so.

**Limit orders "or better, that is, higher".** The book says this of all
four limit cases, the buy limits included. The slide quotes it and teaches
"at the specified price, or better".

**The stop order sentence.** The book writes that a stop order "cannot
guarantee that an order will be executed, or filled at the specified price,
but it can guarantee execution". Its later sentences say three times that a
stop exit is guaranteed and its exact price unknown. The slide teaches
that reading and the speaker cue quotes the sentence.

**Ninety percent.** The book says ninety percent of period ranges stay
below the two standard deviation value. The slide gives it as the book's
figure.

**Cycle amplitude and cycle period** are never defined in words. The two
figures define them by where they put their arrows. Each is a term slide
whose plain line is the figure's measure and says so, whose formal row is
the book's statement of how to read it, and whose cue says the book gives
no definition.
