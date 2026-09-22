# Chapter 3 - Check answerability audit

**A check must be answerable from the slides alone.** The student edition
carries no speaker notes, so a fact that lives only in a cue is a fact the
student never meets, and nothing in the room guarantees the instructor said
it out loud anyway. The same goes for the lecture notes and for the book.
Two things have to hold for every item:

1. Some slide in the deck carries the answer, in text the student can read.
2. **That slide comes before the check**, not after it.

`deckkit.validate()` cannot see either one. Chapter 1 was audited to this
standard after it shipped and two of its fifty items failed. Chapters 2 and 3
were built to the standard from the start and audited before they shipped.

## Result

**46 items, 46 pass.** Every item has an answering slide, every answering
slide is a term slide or a content slide whose text a student can read, and
every one of them comes earlier in the deck than the check that examines it.
No item rests on a speaker cue, on a figure caption alone, or on the book.

Three consequences worth recording, because they are what makes the run card
safe:

- **No item rests on one of this course's own charts.** All six charts
  illustrate a term that has already been taught, which is why the run card
  can drop all six as one cut.
- **No item rests on any figure.** Chapter 3 has forty figures and every
  check is answered by a term or content slide, so the eleven figures the
  run card's first cut drops cannot break a check.
- **No item needs a slide the run card's second cut drops.** One item comes
  close and is recorded below: Check 11, Q2.

No item rests on any of the places where the book is silent or contradicts
itself. Every one of those is named on a slide and none is examined: the
ratio scaling sentence that contradicts its own definition, the two accounts
of the equivolume bar's data, Figure 3.26's resistance label on a support
level, the long and short wording in the bid-ask rule, and the terms the
chapter names without teaching.

## Method

For each of the 46 items, the answering slide was identified by hand and its
slide number compared against the check's own slide number. The slide numbers
below are the teaching edition's, which is the edition the instructor
presents from; the student edition renumbers, but only by removing checks, so
the ordering is unaffected.

Speaker notes were excluded from the search on purpose. So were the lecture
notes. A student sitting in the room with the student edition open is the
reader this audit is written for.

## The 46 items

| Check | Q | Ans | Part | Answering slide | Check slide | Before? |
|---|---|---|---|---|---|---|
| 1 | Q1 | C | 1 | 7 (term) Chartist | 11 | yes |
| 1 | Q2 | B | 1 | 9 (content) When the time axis is only a counter | 11 | yes |
| 2 | Q1 | D | 1 | 14 (term) OHLC data | 17 | yes |
| 2 | Q2 | C | 1 | 16 (content) The range, and where the next bar opens | 17 | yes |
| 3 | Q1 | A | 1 | 19 (term) Higher timeframe bar | 28 | yes |
| 3 | Q2 | D | 1 | 25 (term) Auto-scaling | 28 | yes |
| 4 | Q1 | B | 2 | 32 (content) Not all four prices are equal | 38 | yes |
| 4 | Q2 | A | 2 | 37 (content) Daily against intraday, and markets that never close | 38 | yes |
| 5 | Q1 | D | 2 | 41 (term) Type 1 and Type 2 gaps | 45 | yes |
| 5 | Q2 | C | 2 | 42 (term) Type 3 and Type 4 gaps | 45 | yes |
| 6 | Q1 | B | 2 | 47 (content) What a gap usually does afterwards | 50 | yes |
| 6 | Q2 | C | 2 | 48 (content) The true range, and the Type 4 gap | 50 | yes |
| 7 | Q1 | B | 3 | 55 (term) Constant time chart | 60 | yes |
| 7 | Q2 | C | 3 | 58 (term) Line chart | 60 | yes |
| 8 | Q1 | A | 3 | 62 (term) Japanese candlestick | 67 | yes |
| 8 | Q2 | D | 3 | 65 (content) Equivolume: constant time, non linear axis, two accounts | 67 | yes |
| 9 | Q1 | C | 3 | 70 (term) Point and figure chart | 76 | yes |
| 9 | Q2 | B | 3 | 74 (term) Renko chart | 76 | yes |
| 10 | Q1 | D | 3 | 80 (term) Constant transaction chart | 83 | yes |
| 10 | Q2 | C | 3 | 81 (term) Constant volatility chart | 83 | yes |
| 11 | Q1 | B | 3 | 85 (term) Three line break chart | 88 | yes |
| 11 | Q2 | B | 3 | 72 (content) Why point and figure draws its lines at 45 degrees | 88 | yes |
| 12 | Q1 | A | 4 | 93 (term) Linear scaling | 100 | yes |
| 12 | Q2 | D | 4 | 94 (term) Ratio scaling | 100 | yes |
| 13 | Q1 | C | 4 | 102 (content) Compressed at the top, expanded at the bottom | 105 | yes |
| 13 | Q2 | A | 4 | 103 (content) Which scale to use | 105 | yes |
| 14 | Q1 | C | 4 | 107 (content) What scaling changes, and what it does not | 111 | yes |
| 14 | Q2 | B | 4 | 108 (content) Trendlines break at different times | 111 | yes |
| 15 | Q1 | A | 4 | 113 (content) The same prices can look bullish or bearish | 117 | yes |
| 15 | Q2 | D | 4 | 113 (content) The same prices can look bullish or bearish | 117 | yes |
| 16 | Q1 | C | 5 | 124 (term) Expensive longs | 127 | yes |
| 16 | Q2 | B | 5 | 126 (term) Early longs | 127 | yes |
| 17 | Q1 | A | 5 | 129 (term) Late longs | 132 | yes |
| 17 | Q2 | D | 5 | 130 (content) Two ways to buy support, and both cost | 132 | yes |
| 18 | Q1 | B | 5 | 134 (content) The spread and the reward to risk ratio | 139 | yes |
| 18 | Q2 | A | 5 | 138 (content) How to shrink the spread's cost | 139 | yes |
| 19 | Q1 | B | 6 | 145 (content) When a contract is liquid | 152 | yes |
| 19 | Q2 | C | 6 | 149 (term) Front month contract | 152 | yes |
| 20 | Q1 | B | 6 | 156 (term) Positive roll yield | 162 | yes |
| 20 | Q2 | C | 6 | 159 (term) Normal backwardation | 162 | yes |
| 21 | Q1 | A | 6 | 164 (term) Convergence | 169 | yes |
| 21 | Q2 | D | 6 | 164 (term) Convergence | 169 | yes |
| 22 | Q1 | B | 6 | 173 (term) Back-adjusted continuous chart | 178 | yes |
| 22 | Q2 | D | 6 | 171 (term) Unadjusted nearest futures chart | 178 | yes |
| 23 | Q1 | C | 6 | 180 (term) Perpetual contract | 182 | yes |
| 23 | Q2 | A | 6 | 180 (term) Perpetual contract | 182 | yes |

## The items that were closest to failing

None of these fail. They are recorded because they are where a later edit
would break the standard first.

**Check 11, Q2.** Which charts have a non linear time axis: bar, point and
figure, line, constant volume. Point and figure is answered by slide 72 and
constant volume by its term slide, 78. That bar and line charts do **not**
have one is read from the constant time term slide, 55, whose example says
every bar takes up the same width, set against slide 65, which says the
equivolume chart is the exception because its widths vary. Slide 56 says it
most directly, and slide 56 is on the run card's second cut; the item is
answerable without it, and Check 11 is on the run card's third cut in any
case. If slide 65 or the example on slide 55 is ever trimmed, restore the
link before keeping this item.

**Check 7, Q2.** The key says a line chart filters out more of the price
information than a bar chart. No slide uses those exact words: the line chart
term slide says everything else in each bar is thrown away and that line
charts ignore the high and low. The other three options are each contradicted
by a slide, so the item stands, but it is the one most sensitive to rewording.

**The worked examples.** Checks 2, 5, 6, 9, 10, 12, 16, 17 and 18 reuse the
numbers of the examples on the slides before them: 50.00 to 50.40, the bars at
102 and 106, the 1 peso box, the 2 x ATR bar, 10 to 20 against 90 to 100, and
the 20 centavo spread. That is deliberate, because it makes the check test
the method and not a new calculation, but it means an edit to one of those
examples has to be carried into its check.

## What is not audited here

The answer key distribution is enforced by the build and does not need an
audit: no letter may hold more than 35 percent or fewer than 15 percent of
the items and no three consecutive items may share an answer. Chapter 3 comes
out at A 22 percent, B 28, C 28, D 22, with no run of three. `build/README.md`
has the rule and why it exists.
