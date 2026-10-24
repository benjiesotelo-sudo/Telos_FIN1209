"""Chapter 6 content for FIN1209 - Volume and Open Interest.

This file is pure data. It carries no drawing code.

Source of the chapter scope is Lim, M. (2016), The Handbook of Technical
Analysis, chapter 6, printed pages 173 to 208, which students have in the
course text. Everything here is written from scratch in teaching language.

This chapter is built to the lean form the instructor approved in Chapter 4
and to every rule his reviews of Chapter 5 added, from the first build:

  * **Every idea has a picture beside it.** Every teaching slide is a Pair:
    the idea on the left and a picture on the right. Where the book has a
    figure, it is the book's, and all 44 of the chapter's figures are
    placed. Where the book makes the point only in words, or in a sketch or
    a dense real chart that does not carry the idea alone, it is one of our
    own charts; see charts_chapter06.py for which and why. Four slides
    carry no picture, and no two are next to each other: three lists the
    book gives without a figure (its two lists of volume oscillators, its
    eight oscillators and eight methods, and the volume distortions), and
    the Herrick Payoff Index, for which it gives no formula and no figure.

  * **A question and its answer are separate slides.** Every check is an
    ordinary Check: a question slide, then a reveal slide. Every item is
    answered by the text of a slide before it, never by a picture alone or
    a speaker cue.

  * **The book's content is not cut.** The lean rule cuts a slide that
    teaches nothing new: a divider, a recap. It never cuts what the book
    says.

  * **A Term slide is a term's first teaching in the course, and nothing
    else.** Every name in this chapter was checked against
    content_chapter01.py to content_chapter05.py. Where an earlier chapter
    gave a word a term slide, this one recalls it on an ordinary slide and
    names that chapter on the slide: Dow's volume tenet (Chapter 2), the
    climaxes (Chapter 4), volume spread action (Chapter 5), the equivolume
    and constant volume charts (Chapter 3), inflection points, channels,
    the cycle period and the bidirectional entry (Chapter 5). A word an
    earlier chapter only used, such as volume, open interest and tick
    volume, is taught here with the marker, and its slide says where it
    was met before.

  * **A word from an earlier chapter means what it meant there, or the
    slide says what changed.** Divergence is the one that bites. Chapters 4
    and 5 showed standard divergence, price against an oscillator, peak
    against peak. Volume divergence is volume declining, whatever price
    does, and a slide of its own says so. Chapter 4's price-based volume
    is this chapter's volume by price, and not its price-based volume
    oscillators; that slide says so too.

  * **Nothing is stated without its explanation.** Every slide carries an
    origin line, bottom right: the book page, the figure, whose the numbers
    are, and where the book gives no reason, that it gives none. A chart of
    ours says what it was built from.

  * **A slide has to be followed by a student alone.** Every thing the
    words point at is marked on the picture, in the slide's own words:
    numbered steps, labelled lines, measured bars, the arithmetic written
    on it.

The parts follow the book's own sub-sections, grouped in its order into six
parts so that a part is a session's worth of slides and the progress marker
can say where the room is. Section 6.1 is five of them and 6.2 the sixth.
Section 6.3 is the book's summary and feeds the closing slides.

Where the standing rule bites, and how each place is handled. Every one is
named on a slide, and no check rests on any of them.

  * Bullish divergence "can only occur in a downtrend" (p.177), yet Figure
    6.6 finds it in two dips inside an uptrend. The slide says so and reads
    downtrend as price falling, however briefly, and says that reading is
    ours.

  * Figure 6.4 lists ATR among its supporting series; the text never
    mentions it.

  * The VWMA: price above it is "potentially bullish", and above it the
    stock is also "overvalued", where institutions look to sell. Both are
    the book's, a paragraph apart. Figure 6.11 is labelled VWAP on a 10
    minute chart and captioned VWMA on a daily one.

  * Figures 6.22 and 6.23 are captioned Silver and the text calls 6.23 "the
    same daily chart of USDJPY", then "the Silver market".

  * The tick read with the TRIN is never said to be anything; it is not
    shown to be the tick volume of the slide before. The text calls a
    bullish TRIN overbought and Figure 6.25 calls its bullish TRIN oversold.
    Figure 6.25's caption says daily, its chart and its text 1-minute.

  * The NYSE Up/Down Volume indicator is "the ratio of advancing volume
    over declining volume"; Figure 6.44 labels its line cumulative and the
    line runs below zero, which a ratio cannot.

  * The book's sixth learning objective, reading volume across successive
    contract months, is not taught in this chapter's text. Chapter 3 did
    it. The objectives slide says so.

  * Things the chapter uses and never explains: overbought and oversold,
    the Bollinger Band and the Bollinger Bandwidth, the MACD, the
    cycle-tuned stochastic, the EMA, detrended volume, the rate of change
    of volume, the PVO, the Demand Index, program trading, the advances and
    declines of the TRIN, and how the VWMA is calculated (Chapter 11). Each
    is named where it appears and the closing slides collect them.
"""

from deckkit import (
    Chapter,
    Mark,
    Chart,
    Check,
    Content,
    Figure,
    Mark,
    Pair,
    Question,
    Section,
    Term,
)

Q = Question

# The text column beside one of our own charts. charts_chapter06.py draws
# every chart to fill the picture column these two widths leave.
CHART_W = 5.6
TERM_CHART_W = 6.6
# A wider text column, for the Part 1 slides whose worked numbers need it.
WIDE_W = 6.0

# ==========================================================================
# Part 1 - 6.1, pp.173 to 180: Dow's volume confirmation, volume divergence
# and confirmation, and how divergence is read on the two kinds of volume
# oscillator.
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="The Mechanics of Volume Action: Confirmation and Divergence",
    short="6.1 Confirmation",
    minutes="",
    covers=(),
    slides=(
        Pair(
            origin="Book p.173, the chapter's opening paragraph. The chart is ours, on invented prices, to show how the book's figures draw volume.",
            left=Content(
                title="6.1  Price first: volume and open interest as evidence",
                lines=(
                    "Price is regarded as the best indicator of future price. Volume and open interest are extra evidence: they back up, or corroborate, a setup, show weakness, time breakouts.",
                    "Chart A, ours: every chart today has price bars on top, one volume bar under each. Day 40: PHP 52.40, 2.4 million shares.",
                ),
                accent="Novices misread falling volume in a consolidation as weakness: it times the breakout.",
                caption="Why: Part 2. Volume: defined below. Open interest: Part 4.",
            ),
            picture=Chart(
                letter="A",
                shows="An invented share drawn the way the book's figures draw a chart: price bars in the upper panel and, in the lower panel, one volume bar for each price bar, standing directly under it. One day is picked out in gold in both panels, its close and its volume labelled.",
            ),
            text_w=WIDE_W,
            notes=(
                "The book's opening paragraph, and the shape of every figure today: price on top, volume underneath, one volume bar under each price bar.",
                "Point at the gold day. The price bar says where it traded; the volume bar under it says how much traded. Every figure in the chapter is read that way.",
                "The novice error in the gold line is answered in Part 2: falling volume inside a consolidation is normal, and it times the breakout.",
            ),
        ),
        Pair(
            origin="Book pp.173-174 and Figure 6.1. The tenet was a Chapter 2 term, Volume must confirm the trend.",
            left=Content(
                title="Chapter 2's tenet: volume confirms the trend",
                lines=(
                    "Chapter 2, Dow Theory: volume should expand in the direction of the trend. Big on moves with the trend, small on retracements, the moves against it.",
                    "[1] Uptrend: volume rises as price rises, falls on the dips: bullish volume action, the book says.",
                    "[2] Downtrend: volume rises as price falls, falls on the bounces: bearish volume action.",
                ),
                accent="Both confirm their trend. Numbers on the next slide.",
                caption="Volume is a supporting, or secondary, indicator. Volume doing the opposite: an uptrend may be bearish, a downtrend bullish.",
            ),
            picture=Figure(
                number="6.1",
                aspect=1.340,
                marks=(
                    Mark(1, "box", 0.181, 0.107, 0.675, 0.315, at=(0.675, 0.315)),
                    Mark(2, "box", 0.181, 0.788, 0.682, 0.982, at=(0.682, 0.960)),
                ),
                shows="Two sketches of volume confirming a trend. Top: a rising price with volume bars that grow on the rise and shrink in the downside retracement, labelled bullish volume action in an uptrend. Bottom: a falling price with volume that grows on the fall and shrinks in the upside retracement, labelled bearish volume action in a downtrend.",
            ),
            text_w=6.2,
            notes=(
                "A recall: Chapter 2 gave this as its sixth tenet, with the same four conditions. Nothing in it changes.",
                "Read the figure's two halves. In each, the tall volume bars sit under the move that goes with the trend, and the short ones under the retracement.",
                "What is new today is the vocabulary on the next slides: volume is bullish or bearish, and it confirms or diverges.",
            ),
        ),
        Content(
            origin="Book pp.173-174 states the tenet and its two names. The prices and share counts are ours.",
            title="The tenet with numbers",
            lines=(
                "Uptrend, ours: price climbs PHP 40 to 46 as volume grows from 2 to 4 million shares a day, then dips to 44 on 1 million. Confirmed.",
                "Downtrend, ours: price falls PHP 50 to 46 as volume grows from 2 to 4 million a day, then bounces to 48 on 1 million. Confirmed.",
                "Same pattern, big with the trend and small against it, but two names. Uptrend: price and volume move the same way, bullish. Downtrend: opposite ways, bearish.",
            ),
            accent="Bearish here is not a warning. It is volume backing a fall.",
            caption="Why opposite ways is called bearish: the term Bullish volume and bearish volume, and the slide after it.",
            notes=(
                "Walk both lines with the numbers. In each trend the big volume is on the move with the trend and the small volume on the move against it.",
                "The trap the room falls into: price falling on rising volume sounds bullish. It is not. Name it now and the next two slides explain it.",
            ),
        ),
        Pair(
            origin="Book p.174 gives the definition. The trades and the share counts in the example and on the chart are ours.",
            left=Term(
                term="Volume",
                plain="How much was traded in one period: the bar under each price bar. Used since Chapter 1, first defined here.",
                example="Five trades in one day: 0.1, 0.6, 0.3, 1.2 and 0.2 million shares. That day's volume is 2.4 million shares.",
                formal="Volume is an indication of market participation. It is the total number of shares or contracts traded over a specific time interval.",
            ),
            picture=Chart(
                letter="B",
                shows="One trading day's five trades drawn as five columns of 0.1, 0.6, 0.3, 1.2 and 0.2 million shares, stacked into one volume bar of 2.4 million shares, the day's volume.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The word has been on our charts since Chapter 1, and Chapter 2 made a tenet of it, but this is the first slide that defines it.",
                "Shares for a stock, contracts for a futures market. The interval is whatever the chart's bar is: a day, an hour, five minutes.",
                "Keep the five trades in mind: in Part 4 the same five trades give a tick volume of five.",
            ),
        ),
        Pair(
            origin="Book p.174: its two basic principles, in plainer words. The chart is ours, on invented prices; the numbers are read off it.",
            left=Content(
                title="Two principles: rising and declining volume",
                lines=(
                    "1  Rising volume: more want price to keep going the trend's way, and will buy higher in an uptrend or sell lower in a downtrend.",
                    "2  Declining volume: losing interest. They would rather buy lower in an uptrend, sell higher in a downtrend, or leave.",
                    "Chart C: rally 1, PHP 40 to 47, on volume rising 1.1 to 2.9 million. Rally 2, 44.5 to 51, on volume falling 2.4 to 0.9 million.",
                ),
                accent="Volume measures participation.",
            ),
            picture=Chart(
                letter="C",
                shows="An invented uptrend over its volume. In the first rally, numbered 1, price climbs from PHP 40 to 47 as volume rises from 1.1 to 2.9 million shares: participants buy higher to take part. In the last rally, numbered 2, price still climbs, from 44.5 to 51, but volume declines from 2.4 to 0.9 million as they lose interest.",
            ),
            text_w=CHART_W,
            notes=(
                "The book says to remember these two whenever volume is studied. Every reading later in the chapter comes back to them.",
                "On the chart, 1 is a rally the market wants: volume grows as price rises. 2 is a rally fewer want: price still rises, on shrinking volume.",
            ),
        ),
        Pair(
            origin="Book pp.174-175 states it for an uptrend, then a downtrend. Joined into one line here: our summary of its four sentences. The numbers are ours.",
            left=Term(
                term="Bullish volume and bearish volume",
                plain="Compare price's direction with volume's. Same way: bullish volume. Opposite: bearish volume.",
                example="Ours: price PHP 50 to 46 as volume grows 2 to 4 million: opposite, bearish. Price 50 to 46 as volume shrinks 4 to 2 million: same way, bullish.",
                formal="Both rising and declining volume are regarded as bullish volume if volume and price rise and decline together, and as bearish volume if they move in opposite directions.",
            ),
            picture=Chart(
                letter="D",
                shows="Four small cases, each a price arrow over volume bars. Price up with volume rising, and price down with volume falling: volume and price together, bullish volume. Price up with volume falling, and price down with volume rising: opposite directions, bearish volume.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book says it four times, trend by trend. Every one of the four is the same rule: together is bullish, opposite is bearish.",
                "So the same falling volume is bullish under a falling price and bearish under a rising one. Volume alone says nothing until price's direction is known.",
                "This answers review question 2, describe bullish and bearish volume.",
            ),
        ),
        Content(
            origin="Book p.174: the definition and the two principles. Ours: the buyer and seller point, which follows from the definition, and the numbers.",
            title="Why falling price on rising volume is bearish",
            lines=(
                "Volume counts shares that changed hands. Every share traded has a buyer and a seller, so volume alone never says buyers outnumber sellers.",
                "Principle 1: rising volume is more people taking part in the move. PHP 50 to 46 on 2 to 4 million: more sell lower. The fall has backing: bearish.",
                "Principle 2, the other way: price 50 to 46 on 4 to 2 million shares: fewer willing to sell lower. The fall is losing its backing, so bullish.",
            ),
            accent="Rising volume is not demand. It is more trading in the direction price is already going.",
            notes=(
                "This is the question the room asks: more volume as price falls, is that not more demand? No. Each of those shares was sold by someone as well as bought.",
                "Volume says how many take part. Price says which way they are pushing. Together they say whether the push has backing.",
            ),
        ),
        Pair(
            origin="Book p.175 and Figure 6.2, its prices read off the figure. The peso example is ours.",
            left=Content(
                title="Rising volume is not always bullish",
                lines=(
                    "The book: declining volume does not imply bearishness, nor rising volume bullishness. PHP 50 to 46 on 2 to 4 million: rising, yet bearish.",
                    "Figure 6.2, gold: [1] about 260 in 2001 to 1,900 in 2011 as volume expands [2]: bullish. [3] Then to about 1,200 in 2013 as volume declines: bullish too.",
                ),
                accent="Read price's direction first, then volume's.",
                caption="The book calls reading volume alone, falling means bad, a simple mistake many novices make.",
            ),
            picture=Figure(
                number="6.2",
                aspect=1.645,
                marks=(
                    Mark(1, "arrow", 0.556, 0.720, 0.895, 0.164),
                    Mark(2, "box", 0.551, 0.767, 0.883, 0.944, at=(0.883, 0.767)),
                    Mark(3, "circle", 0.846, 0.052, 0.952, 0.268),
                ),
                shows="The continuous daily chart of gold from 1989 to 2013: a primary bull trend from 2001, its volume expanding in the direction of the trend, and volume declining in the retracement at the end, labelled bullish.",
            ),
            text_w=WIDE_W,
            notes=(
                "Point at the end of the chart: price falls and volume falls with it. That is bullish volume in an uptrend, not a warning.",
                "The mistake is reading volume alone: falling equals bad. Ask the room which way price was going first.",
            ),
        ),
        Pair(
            origin="Book p.175 and Figure 6.3. The prices and share counts are ours: the tenet's numbers with the volume swapped.",
            left=Content(
                title="Volume that does not confirm the trend",
                lines=(
                    "Confirming volume is big with the trend, small against it. Not confirming is the reverse.",
                    "[1] Uptrend, ours: PHP 40 to 46 as volume shrinks 4 to 2 million, dip to 44 as it grows to 3. Opposite ways: bearish volume, a potentially weak uptrend.",
                    "[2] Downtrend, ours: PHP 50 to 46 as volume shrinks 4 to 2 million, bounce to 48 as it grows to 3. Same way: bullish volume, a potentially bullish downtrend.",
                ),
                accent="A warning, not a reversal.",
            ),
            picture=Figure(
                number="6.3",
                aspect=1.344,
                marks=(
                    Mark(1, "box", 0.189, 0.183, 0.654, 0.328),
                    Mark(2, "box", 0.189, 0.855, 0.707, 0.994, at=(0.707, 0.960)),
                ),
                shows="Two sketches of volume not confirming a trend. Top: a rising price whose volume shrinks on the rise and grows in the retracement, labelled bearish volume action in an uptrend. Bottom: a falling price whose volume shrinks on the fall and grows in the upside retracement, labelled bullish volume action in a downtrend.",
            ),
            text_w=6.2,
            notes=(
                "Set this beside Figure 6.1. The prices are the same shapes; only the volume is swapped.",
                "Not confirming is still only a potential: the book says weak or bearish uptrend, not a reversal.",
            ),
        ),
        Content(
            origin="Our summary of the book's pp.174-175, which states both for each trend. The prices and share counts are ours.",
            title="Two questions, asked in order",
            lines=(
                "1  Bullish or bearish volume? Price and volume only, no trend: same direction bullish, opposite bearish.",
                "2  Does it confirm the trend? In an uptrend bullish volume confirms; in a downtrend bearish volume confirms. The other kind does not.",
                "Downtrend, PHP 50 to 46, volume 2 to 4 million: bearish, so it confirms.",
                "Uptrend dip, PHP 46 to 44, volume 1 to 3 million: bearish, so it does not.",
            ),
            accent="Bearish is not the same as not confirming.",
            notes=(
                "Two layers. The first is mechanical and needs only two arrows. The second brings in the trend, and asks whether the volume backs it.",
                "Volume that does not confirm is the other kind: bearish volume in an uptrend, bullish volume in a downtrend.",
            ),
        ),
        Check(
            label="Bullish and bearish volume",
            questions=(
                Q(
                    stem="In an uptrend, price dips in a retracement and volume declines during the dip. That volume is:",
                    options=("Bearish volume, because volume is falling",
                             "Bullish volume, because price and volume fall together",
                             "Neither, because the trend is up",
                             "Volume not confirming the uptrend"),
                    answer="B",
                    reason="Price and volume fall together: bullish volume. In an uptrend bullish volume is the confirming kind, so D is wrong too.",
                ),
                Q(
                    stem="Volume rises while price declines in a preexisting downtrend. The book calls this:",
                    options=("Bullish volume action",
                             "A potentially bullish downtrend",
                             "Volume that does not confirm the trend",
                             "Bearish volume action, confirming the downtrend"),
                    answer="D",
                    reason="Price down, volume up: opposite ways, bearish volume. In a downtrend that is the confirming kind: volume expanding with the trend.",
                ),
            ),
        ),
        Pair(
            origin="Book p.175 defines both. The prices and share counts are ours; the chart is ours, sketches, not prices.",
            left=Term(
                term="Volume divergence and volume confirmation",
                plain="Leave price out. Volume falling: divergence. Volume rising: confirmation, or convergence.",
                example="Ours: price PHP 40 to 46 as volume shrinks 3 to 1 million: divergence. Volume 3 to 5 million instead: confirmation.",
                formal="Volume divergence occurs whenever volume declines, irrespective of the direction of price. Volume convergence or confirmation occurs whenever volume rises, irrespective of the direction of price.",
            ),
            picture=Chart(
                letter="E",
                shows="Four small cases in two columns. Left column, volume divergence: volume bars falling, once under a rising price and once under a falling price, still divergence. Right column, volume confirmation: volume bars rising, once under a rising price and once under a falling price, still confirmation.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Read the columns of the chart, not the rows: each column is one volume direction, with price going both ways.",
                "Bullish or bearish volume needs price. Divergence or confirmation does not: it is volume's direction alone.",
            ),
        ),
        Content(
            origin="Book p.175 defines both pairs. The comparison and the numbers are ours.",
            title="Not bullish and bearish renamed",
            lines=(
                "Bullish or bearish asks about price and volume together. Divergence or confirmation asks about volume alone. Two questions, two answers.",
                "Ours: price PHP 40 to 46 on volume 2 to 4 million. Same way: bullish. Volume up: confirmation. Here the two answers line up.",
                "Price PHP 50 to 46 on volume 2 to 4 million. Opposite ways: bearish. Volume up: still confirmation. Here they do not.",
            ),
            accent="Bullish or bearish needs price. Divergence or confirmation needs only volume.",
            notes=(
                "The room will try to map bullish onto confirmation and bearish onto divergence. The second example breaks that mapping.",
                "Keep both answers. The next slides put them together into one name.",
            ),
        ),
        Pair(
            origin="Book pp.175-176. The chart is ours, on invented prices; the numbers are read off it.",
            left=Content(
                title="What divergence and confirmation say",
                lines=(
                    "Divergence, volume falling: on a rise, fewer will buy higher, bearish for an uptrend; on a fall, fewer will sell lower, bullish for a downtrend.",
                    "Confirmation, volume rising: with a rise, bullish for an uptrend; with a fall, bearish for a downtrend.",
                    "Chart F: left, PHP 40 to 55, volume 0.9 to 3.4 million: it continues. Right, 40 to 51, volume 2.9 to 0.8: it turns.",
                ),
                accent="Both are early warnings, not certainties.",
            ),
            picture=Chart(
                letter="F",
                shows="Two invented uptrends side by side. Left: price climbs from PHP 40 to 55 as volume rises from 0.9 to 3.4 million, confirmation, and the trend continues. Right: price climbs from 40 to 51 as volume falls from 2.9 to 0.8 million, divergence, and price turns down to 46 at the end.",
            ),
            text_w=WIDE_W,
            notes=(
                "Confirmation is called convergence too: price and volume coming together in one direction. Both words mean volume rising.",
                "The right-hand chart is one possible ending, drawn to show what potential reversal means. Divergence is an early warning, not a certainty.",
            ),
        ),
        Content(
            origin="Book p.174 (the tenet) and p.175 (volume confirmation). The prices and share counts are the tenet's, ours.",
            title="Confirms the trend, or volume confirmation",
            lines=(
                "Volume confirms the trend (Chapter 2, p.174): over the whole trend, big with it and small against it. It judges the pattern.",
                "Volume confirmation (p.175): on one stretch, volume rising. It judges one leg at a time.",
                "Ours: PHP 40 to 46 on 2 to 4 million, a dip to 44 on 1 million. The trend is confirmed. The dip alone, volume falling with price, is bullish divergence.",
            ),
            accent="One dip can be a bullish divergence inside a confirmed uptrend.",
            caption="The next slide finds both on the book's own chart.",
            notes=(
                "Two phrases share a word. The tenet looks at the whole trend; volume confirmation looks at one stretch of volume.",
                "So the uptrend dip on falling volume is bullish volume that confirms the trend, and on its own it is a bullish divergence. Both are the book's.",
            ),
        ),
        Pair(
            origin="Book p.178 and Figure 6.6: the book labels the whole trend bullish volume and two of its dips bullish divergence.",
            left=Content(
                title="Both on one chart: Figure 6.6",
                lines=(
                    "[1] Over the whole rise, volume expands: the trend is confirmed.",
                    "[2] and [3] The dips of periods 4 and 6, on falling volume: the book labels each bullish divergence.",
                ),
                accent="A confirmed uptrend with two bullish divergences inside it.",
            ),
            picture=Figure(
                number="6.6",
                aspect=1.396,
                marks=(
                    Mark(1, "arrow", 0.131, 0.956, 0.881, 0.695),
                    Mark(2, "circle", 0.522, 0.143, 0.598, 0.265),
                    Mark(3, "circle", 0.610, 0.195, 0.677, 0.363),
                ),
                shows="The SPDR Gold Trust over about four years, split by dashed lines into ten numbered periods. Volume expands across the whole uptrend, and periods 4 and 6 are dips on falling volume, labelled bullish divergence by the book.",
            ),
            text_w=WIDE_W,
            notes=(
                "Trace the gold arrow, mark 1, across the volume panel: bigger volume as the trend rises. Then the two circles, marks 2 and 3, the dips.",
                "Both readings are the book's, on one chart: the whole trend confirmed, and each dip a bullish divergence.",
            ),
        ),
        Pair(
            origin="Book pp.176-178 and Figure 6.4. The formal row is its p.178 summary. The ATR on the figure is in no sentence of the text. The numbers are ours.",
            left=Term(
                term="Bullish and bearish divergence and confirmation",
                plain="One name from two answers: bullish or bearish, then divergence or confirmation.",
                example="Ours: PHP 50 to 46, volume 2 to 4 million: opposite, bearish; volume up, confirmation. Figure 6.4's third column [1]: price top, volume below.",
                formal="Volume and price declining together: bullish divergence. Rising together: bullish confirmation. Volume declining, price rising: bearish divergence. Volume rising, price declining: bearish confirmation.",
            ),
            picture=Figure(
                number="6.4",
                aspect=1.558,
                marks=(
                    Mark(1, "box", 0.595, 0.007, 0.803, 0.857),
                ),
                shows="Four columns, each a price path over a supporting series. Bearish divergence: price rising, the supporting series falling. Bullish confirmation: both rising. Bearish confirmation: price falling, the supporting series rising. Bullish divergence: both falling. The supporting series is listed as volume bars, a volume moving average, open interest, and the ATR in brackets.",
            ),
            text_w=6.6,
            notes=(
                "The formal row is the book's own summary of all four scenarios, page 178. The next slide is what each one warns of.",
                "Bullish or bearish comes from the term Bullish volume and bearish volume: together or apart. Divergence or confirmation from the term before this one: volume down or up.",
                "The figure lists four kinds of supporting series. Volume, its moving average and open interest are all in the text; the ATR is not mentioned anywhere in it.",
            ),
        ),
        Content(
            origin="Book pp.175-177: what each name indicates, from its two principles on p.174.",
            title="What each of the four tells",
            lines=(
                "Bullish divergence, PHP 50 to 46 as volume falls 3 to 1 million: fewer will sell lower. A potential upside reversal.",
                "Bearish divergence, PHP 46 to 50 as volume falls 3 to 1 million: fewer will buy higher. A potential downside reversal.",
                "Bullish or bearish confirmation, volume rising with the move: more are taking part. A potential continuation.",
            ),
            accent="Divergence warns of a turn. Confirmation, of backing.",
            caption="The book: divergence always indicates potential weakness, confirmation potential strength.",
            notes=(
                "Each name says something about participation, which is the two principles again: more or fewer want to take part in the move price is making.",
                "Where each can occur is the next slide, and there the book's sentence and its figure disagree.",
            ),
        ),
        Pair(
            origin="Book pp.176-177 for where each can occur, and Figure 6.6 (p.178). Our reading is said to be ours.",
            left=Content(
                title="Where divergence can occur: the book and its figure",
                lines=(
                    "The book: bullish divergence can only occur in a downtrend, bearish only in an uptrend (p.176).",
                    "[1] Yet on Figure 6.6, price rises from about 42 to about 120, the span on the right: an uptrend.",
                    "Inside it, the book labels the dips of periods 4 [2] and 6 [3], price and volume falling together, bullish divergence.",
                ),
                accent="Our reading: the p.178 summary applies to any stretch, so a dip inside an uptrend can be bullish divergence.",
            ),
            picture=Figure(
                number="6.6",
                aspect=1.396,
                marks=(
                    Mark(1, "arrow", 0.935, 0.590, 0.935, 0.110, at=(0.935, 0.640)),
                    Mark(2, "circle", 0.522, 0.143, 0.598, 0.265),
                    Mark(3, "circle", 0.610, 0.195, 0.677, 0.363),
                ),
                shows="The SPDR Gold Trust over about four years, rising from about 42 to about 120, split into ten numbered periods. Periods 4 and 6 are dips on falling volume inside that uptrend, labelled bullish divergence by the book.",
            ),
            text_w=WIDE_W,
            notes=(
                "Downtrend and uptrend are the book's words for where each divergence can occur. Mark 1 is the uptrend, mark 2 the dips the book calls bullish divergence inside it.",
                "Be plain that the reading is ours: the book's sentence says downtrend, its figure says inside an uptrend. No check rests on it.",
            ),
        ),
        Pair(
            origin="A recall of this course's Chapters 4 and 5, against the book's p.176. The chart is ours, on invented prices; its peaks are read off it.",
            left=Content(
                title="Not the divergence Chapters 4 and 5 drew",
                lines=(
                    "Chapters 4 and 5, standard divergence: compare two peaks. Ours: price peaks at PHP 58, then higher at 60; an oscillator peaks at 80, then lower at 62.",
                    "Volume divergence compares no peaks: volume declining, whatever price does. Price's direction still decides bullish or bearish.",
                ),
                accent="Volume has no reverse divergence (p.176): one kind only, volume falling.",
                caption="Chapter 5 only named reverse divergence, left to Chapter 9. Chapter 4: bullish divergence in volume is falling price on decreasing volume.",
            ),
            picture=Chart(
                letter="G",
                shows="Two invented charts side by side. Left, standard divergence as Chapters 4 and 5 drew it: price peaks at PHP 58 and then higher at 60, while an oscillator below peaks at 80 and then lower at 62, peak against peak. Right, volume divergence: price rises and the volume bars under it shrink, with no peaks compared.",
            ),
            text_w=CHART_W,
            notes=(
                "Same word, different test. Standard divergence compares two peaks on two lines. Volume divergence asks one question: is volume falling?",
                "This answers review question 3, how volume divergence differs from standard oscillator divergence.",
                "The oscillators there were the MACD and the bar stochastic. Reverse divergence was named in Chapter 5 and left to Chapter 9; the book says volume has no such classification.",
            ),
        ),
        Pair(
            origin="Book p.177 and Figure 6.5, its prices read off the figure. Its caption says daily; the chart is labelled 10 min. Rounding bottom: Chapter 4.",
            left=Content(
                title="Bullish volume divergence: Isis Pharmaceuticals",
                lines=(
                    "[1] Isis Pharmaceuticals falls from about 12 to about 9 and curves into a rounding bottom, a bullish pattern from Chapter 4.",
                    "In two stretches, [2] and [3], volume falls as price falls: volume falling, divergence; with price, bullish. Fewer are willing to sell lower.",
                ),
                accent="Divergence provides additional evidence of a bullish chart formation.",
                caption="The chart's note: Isis rose past the previous day's close though the Dow Jones Industrial Average fell 219 points, a bullish indication.",
            ),
            picture=Figure(
                number="6.5",
                aspect=1.670,
                marks=(
                    Mark(1, "box", 0.500, 0.240, 0.956, 0.727),
                    Mark(2, "box", 0.504, 0.735, 0.700, 0.956, at=(0.504, 0.956)),
                    Mark(3, "box", 0.740, 0.777, 0.953, 0.965, at=(0.953, 0.965)),
                ),
                shows="An intraday chart of Isis Pharmaceuticals: price falls steeply and curves into a larger rounding bottom pattern, and the volume panel under it carries two dashed lines falling to the right, each labelled bullish volume divergence.",
            ),
            text_w=5.6,
            notes=(
                "Price falling and volume falling together: bullish divergence, by the last slides. Point at the two dashed lines in the volume panel.",
                "Evidence, not a signal: the pattern is the setup and the volume corroborates it, which is the chapter's first sentence again.",
                "Chapter 4's Figure 4.18 was an intraday chart of this stock too.",
            ),
        ),
        Pair(
            origin="Book p.178 and Figure 6.6. Its caption says a daily chart; the chart itself is labelled weekly.",
            left=Content(
                title="Ten periods of bullish volume: gold",
                lines=(
                    "1, 3 [1], 7 and 9: price and volume rise, bullish confirmation. 4 [2] and 6 [3]: price dips as volume falls, bullish divergence. 5: volume flat, no reading.",
                    "2 [4], 8 and 10: volume falls as price moves sideways, a consolidation (Chapter 4). At volume's minimum, price breaks out.",
                ),
                accent="In a consolidation, volume times the breakout: Part 2.",
                caption="4 and 6 are dips inside this uptrend, yet the book labels them bullish divergence: its p.178 summary applied to a falling stretch.",
            ),
            picture=Figure(
                number="6.6",
                aspect=1.396,
                marks=(
                    Mark(1, "box", 0.432, 0.108, 0.535, 0.977, at=(0.535, 0.977)),
                    Mark(2, "circle", 0.522, 0.143, 0.598, 0.265),
                    Mark(3, "circle", 0.610, 0.195, 0.677, 0.363),
                    Mark(4, "box", 0.219, 0.300, 0.426, 0.977, at=(0.219, 0.977)),
                ),
                shows="The SPDR Gold Trust over about four years, split by dashed lines into ten numbered periods, with arrows on the volume panel showing volume rising or falling in each, under the label volume expanding in the direction of the existing trend.",
            ),
            text_w=5.4,
            notes=(
                "Go period by period with the arrows on the volume panel. Up arrows with price rising: confirmation. Down arrows with price dipping: divergence.",
                "The breakout timing in 2, 8 and 10 is Part 2's subject. Here it is enough that a consolidation's falling volume is not divergence.",
                "Be plain about the gap: the book's sentence says downtrend, its figure says inside an uptrend. The slide gives our reading and says it is ours.",
            ),
        ),
        Pair(
            origin="Ours: Figure 6.6's readings on one invented uptrend, so each period can be seen. The periods, prices and volumes are ours, read off the chart.",
            left=Content(
                title="Our example: one uptrend, period by period",
                lines=(
                    "1  PHP 40 to 48, volume about 1.2 to 3.3 million: both rise, bullish confirmation.",
                    "2  Dip to 45.5, volume about 2.7 to 1.4 million: both fall, bullish divergence. Fewer will sell lower: a weak dip, and 4 resumes the trend.",
                    "3  Sideways, 45.5 to 47.3, volume down to 0.5 million: a consolidation.",
                    "4  Breakout, 46 to 55, volume about 2.5 to 3 million: bullish confirmation.",
                ),
                accent="3: no direction, no reading (p.180).",
            ),
            picture=Chart(
                letter="H",
                shows="An invented uptrend over its volume, split by dashed lines into four numbered periods: 1 a rise from PHP 40 to 48 on volume rising from about 1.2 to 3.3 million, bullish confirmation; 2 a dip to 45.5 on volume falling to about 1.4 million, bullish divergence; 3 a sideways range with volume falling to its minimum, 0.5 million, a consolidation; 4 a breakout and rise to 55 on volume rising to about 3 million, bullish confirmation.",
            ),
            text_w=CHART_W,
            notes=(
                "The book's figure has ten periods on a real chart and they are hard to see. Here are four, one of each kind it names.",
                "Ask the room for each period before reading the label: which way is price, which way is volume, together or apart.",
                "Period 3: the book says there is no divergence reading in a consolidation, because price moves sideways. Part 2 is where that page is taught.",
            ),
        ),
        Check(
            label="Divergence and confirmation",
            questions=(
                Q(
                    stem="Price and volume are declining together. By the book's summary this is:",
                    options=("Bearish confirmation",
                             "Bearish divergence",
                             "Bullish divergence",
                             "Bullish confirmation"),
                    answer="C",
                    reason="Volume declining is divergence, and volume moving with price is bullish: bullish divergence.",
                ),
                Q(
                    stem="Which statement about volume divergence is the book's?",
                    options=("It occurs whenever volume declines, irrespective of the direction of price",
                             "It needs price to make a higher peak while volume makes a lower one",
                             "It has a reverse divergence classification",
                             "It always indicates potential strength in a trend"),
                    answer="A",
                    reason="Volume divergence is volume declining, whatever price does. No reverse classification, and it indicates weakness.",
                ),
            ),
        ),
        Pair(
            origin="Book pp.178-179 defines both; our gloss of oscillator. The numbers are ours. The chart is ours, on invented prices; its line is the rule taught in Part 6.",
            left=Term(
                term="Price-based and non-price-based volume oscillators",
                plain="Oscillator: an indicator under price. Price-based: price built in. Non-price-based: volume only.",
                example="Ours: closes PHP 50, 51, 50.5 on 2, 3, 1 million. Bars: 2, 3, 1. Line: start at 0; 51 is higher, add 3: 3; 50.5 is lower, subtract 1: 2.",
                formal="Price-based volume oscillators incorporate price data in their construction, whereas non-price-based volume oscillators only incorporate volume data in their construction.",
            ),
            picture=Chart(
                letter="I",
                shows="Three panels over one invented stretch of price. The price line; under it the volume bars, built from volume alone, non-price-based; and under those a line that adds each day's volume when the close rises and subtracts it when the close falls, which needs price, price-based.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Oscillator here means an indicator drawn in its own panel under the price. That gloss is ours: this chapter never defines the word, and Chapter 8 is oscillators.",
                "The example's second line starts at 0, adds 3 on the higher close, subtracts 1 on the lower: 0, 3, 2. It cannot be drawn without the closes. Part 6 names it the On Balance Volume.",
                "Volume bars are on the book's non-price-based list, so plain volume counts as one of these oscillators.",
            ),
        ),
        Content(
            origin="Book p.179: its two lists, as printed. Where each is taught is this course's note.",
            title="The book's two lists",
            lines=(
                "Price-based: On Balance Volume (OBV), Accumulation/Distribution Line (ADL), Chaikin Money Flow, Chaikin Oscillator, Demand Index, Herrick Payoff Index.",
                "Non-price-based: standard volume bars, smoothed volume, detrended volume, rate of change of volume (ROC volume), percentage volume oscillator (PVO).",
                "So plain volume bars count as a non-price-based volume oscillator.",
            ),
            accent="Reading divergence on one kind differs from reading it on the other.",
            caption="Taught later: OBV, ADL, the two Chaikin indicators and the Herrick index in Part 6, smoothed volume in Part 3. The Demand Index, detrended volume, ROC volume and the PVO are named and never explained.",
            notes=(
                "The book gives these as two lists and no figure, so this slide has no picture. The next two slides show how the two kinds are read.",
                "Do not explain the four the book never explains. Say they are names only.",
            ),
        ),
        Pair(
            origin="Book p.179 and Figure 6.7. The two rules are our summary of the figure's eight arrows; the book gives no reason the two kinds differ.",
            left=Content(
                title="Reading divergence on the two kinds",
                lines=(
                    "[1] Non-price-based, plain volume included: bullish if it moves with price, bearish if against. Divergence if it falls, confirmation if it rises.",
                    "[2] Price-based, such as the OBV: bullish if it rises, bearish if it falls. Divergence if it moves against price, confirmation if with it.",
                    "Figure 6.7: top half divergence, bottom half confirmation; left [1] plain volume, right [2] price-based. Two arrows flip, [3] and [4].",
                ),
                accent="First ask which kind you are reading.",
                caption="Book: only bullish divergence and bearish confirmation differ.",
            ),
            picture=Figure(
                number="6.7",
                aspect=1.313,
                marks=(
                    Mark(1, "box", 0.015, 0.023, 0.497, 0.986, at=(0.015, 0.986)),
                    Mark(2, "box", 0.509, 0.023, 0.988, 0.986, at=(0.509, 0.986)),
                    Mark(3, "circle", 0.800, 0.270, 0.975, 0.410, at=(0.975, 0.410)),
                    Mark(4, "circle", 0.799, 0.722, 0.982, 0.913, at=(0.982, 0.722)),
                ),
                shows="Eight pairs of arrows, a price arrow over a volume arrow, in four boxes: divergence and confirmation, each for non-price-based and price-based volume oscillators. The two kinds differ only in bullish divergence and bearish confirmation, where the price-based volume arrow points the other way.",
            ),
            text_w=6.2,
            notes=(
                "Go box by box. Top left and top right differ only in the bullish divergence pair; bottom left and bottom right only in the bearish confirmation pair.",
                "Read a price-based line the way you read price itself: up is bullish, down is bearish. Then compare it with price for divergence or confirmation.",
                "Why the two kinds differ: the book gives the figure and no reason, so give none.",
            ),
        ),
        Content(
            origin="Book p.179: the four names on both kinds. The prices and the volume and OBV numbers are ours.",
            title="The four names on both kinds, with numbers",
            lines=(
                "Price rising, PHP 46 to 50: both kinds read alike. Volume 3 to 5 million, OBV 5 to 7: bullish confirmation. Both down: bearish divergence.",
                "Price falling, 50 to 46, bullish divergence: volume falls 3 to 1 million, with price; the OBV rises 5 to 7 million, against price.",
                "Price falling, 50 to 46, bearish confirmation: volume rises 3 to 5 million, against price; the OBV falls 5 to 3 million, with price.",
            ),
            accent="Price falling: same names, opposite arrows.",
            caption="Plain volume: rising is confirmation. A price-based line: moving with price is confirmation.",
            notes=(
                "Only two of the eight cases change between the kinds, and they are both with price falling. Read those two lines slowly.",
                "Plain volume: up is confirmation, down is divergence. A price-based line: with price is confirmation, against price is divergence.",
            ),
        ),
        Pair(
            origin="Book p.179 and Figure 6.7: where the two kinds' arrows match and where they differ.",
            left=Content(
                title="The same four on Figure 6.7's arrows",
                lines=(
                    "[1] and [2] Bullish confirmation, price rising: the volume arrows match on both kinds.",
                    "[3] and [4] Bullish divergence: plain volume falls with price; the price-based arrow rises.",
                    "[5] and [6] Bearish confirmation: plain volume rises; the price-based arrow falls with price.",
                ),
                accent="Only the two price-falling cases flip.",
            ),
            picture=Figure(
                number="6.7",
                aspect=1.313,
                marks=(
                    Mark(1, "box", 0.010, 0.520, 0.225, 0.890, color="gold", at=(0.010, 0.890)),
                    Mark(2, "box", 0.515, 0.520, 0.725, 0.890, color="gold", at=(0.515, 0.890)),
                    Mark(3, "box", 0.300, 0.020, 0.491, 0.380, color="red", at=(0.300, 0.020)),
                    Mark(4, "box", 0.800, 0.020, 0.994, 0.380, color="red", at=(0.800, 0.020)),
                    Mark(5, "box", 0.300, 0.520, 0.491, 0.890, color="blue", at=(0.491, 0.520)),
                    Mark(6, "box", 0.800, 0.520, 0.994, 0.890, color="blue", at=(0.994, 0.520)),
                ),
                shows="Eight pairs of arrows, a price arrow over a volume arrow, in four boxes. With price rising the two kinds of oscillator match; with price falling, in bullish divergence and bearish confirmation, the price-based volume arrow points the other way.",
            ),
            text_w=WIDE_W,
            notes=(
                "Gold boxes first: price rising, the two kinds agree. Then red, then blue: the two cases where the price-based arrow points the other way.",
                "The numbers on the slide before are these arrows: 3 to 1 million falling, the OBV 5 to 7 rising.",
            ),
        ),
        Pair(
            origin="Book p.180 and Figure 6.8, its prices read off the figure. Shown: its price and volume panels.",
            left=Content(
                title="Both kinds on one chart: price and volume",
                lines=(
                    "[1] The trust rises from about 129 to 133, October to January.",
                    "[2] Volume and smoothed volume, a 20-day average, non-price-based: falling, against price: bearish divergence.",
                ),
                accent="Plain volume falling under a rising price: bearish divergence.",
                caption="Smoothed volume: Part 3. The figure's two lower panels come next.",
            ),
            picture=Figure(
                number="6.8",
                aspect=0.895,
                crop=(0.0, 0.0, 0.0, 0.387),
                marks=(
                    Mark(1, "arrow", 0.346, 0.306, 0.754, 0.207),
                    Mark(2, "box", 0.007, 0.689, 0.993, 0.995),
                ),
                shows="The top of Figure 6.8: a daily chart of the Currency Shares Euro Trust rising from about 129 to 133, and under it volume with a smoothed line, labelled bearish divergence.",
            ),
            text_w=WIDE_W,
            notes=(
                "Price rises across the arrow at the top, mark 1. The volume panel under it falls, mark 2: non-price-based and falling, so bearish divergence.",
                "The figure is cut in two so each panel can be read; the PVO and the ADL under it are the next slide.",
            ),
        ),
        Pair(
            origin="Book p.180 and Figure 6.8. Shown: its two lower panels. PVO and detrending are on the figure and not explained by the book.",
            left=Content(
                title="Both kinds on one chart: the PVO and the ADL",
                lines=(
                    "The same months, the same price rising from about 129 to 133.",
                    "[1] The PVO, a detrended volume oscillator the book never explains: non-price-based, falling: bearish divergence too.",
                    "[2] ADL, price-based: rising, with price: bullish confirmation.",
                ),
                accent="Each kind read by its own rule.",
                caption="The book gives no rule for which reading to believe.",
            ),
            picture=Figure(
                number="6.8",
                aspect=0.895,
                crop=(0.0, 0.606, 0.0, 0.0),
                marks=(
                    Mark(1, "box", 0.007, 0.024, 0.993, 0.476, at=(0.993, 0.476)),
                    Mark(2, "box", 0.007, 0.492, 0.993, 0.992, at=(0.993, 0.992)),
                ),
                shows="The bottom of Figure 6.8: a detrended volume oscillator, the PVO, labelled bearish divergence, and under it the accumulation distribution line rising, labelled bullish confirmation.",
            ),
            text_w=5.0,
            notes=(
                "The PVO falls, mark 1, bearish divergence; the ADL rises with price, mark 2, bullish confirmation.",
                "Do not resolve the disagreement. The book shows the figure to show each kind read by its own rule; it does not say which to believe.",
            ),
        ),
        Check(
            label="The two kinds of volume oscillator",
            questions=(
                Q(
                    stem="Which of these is a non-price-based volume oscillator?",
                    options=("On Balance Volume",
                             "Chaikin Money Flow",
                             "Smoothed volume",
                             "Accumulation/Distribution Line"),
                    answer="C",
                    reason="Smoothed volume uses volume data only. The other three incorporate price.",
                ),
                Q(
                    stem="Price falls while a price-based volume oscillator rises. On the book's reading this is:",
                    options=("Bearish confirmation",
                             "Bullish divergence",
                             "Bearish divergence",
                             "Bullish confirmation"),
                    answer="B",
                    reason="On a price-based oscillator, rising is bullish and moving against price is divergence: bullish divergence.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Part 2 - 6.1, pp.180 to 186: volume as a timing indicator, the VWMA,
# buying and selling climaxes, low volume tops and bottoms, and how the
# timeframe changes what volume shows.
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="The Mechanics of Volume Action: Timing, the VWMA and Climaxes",
    short="6.1 Timing",
    minutes="",
    covers=(),
    slides=(
        Pair(
            origin="Book p.180. Consolidation and breakout: Chapters 2 and 4. The chart is ours, on invented prices and volume; the numbers are read off it.",
            left=Content(
                title="6.1  Volume as a timing indicator",
                lines=(
                    "Consolidation: price moving sideways in a range, here PHP 48 to 52.",
                    "The book: as volume falls close to its lowest historical level, a breakout from the range is expected.",
                    "Ours: an earlier low, 0.45 million, sets the dashed level. Volume falls back to 0.42 at 1, testing it; at 2 price breaks out on 3.6 million.",
                ),
                accent="No divergence reading in a range: price moves sideways.",
                caption="So falling volume in a range is not weakness. How far back historical reaches, the book does not say.",
            ),
            picture=Chart(
                letter="J",
                shows="An invented share ranging sideways between PHP 48 and PHP 52, with rows of buy stops marked above the box and sell stops below it. Under it the volume, in millions of shares: an early low of 0.45 sets a dashed level, and volume falls from about 2.5 back to it, 0.42 at 1. At 2 price breaks out of the top of the box on 3.6 million.",
            ),
            text_w=CHART_W,
            notes=(
                "This answers the novice error from the first slide. Sideways price cannot diverge from anything, so shrinking volume inside a range is not a warning: it is the clock running down.",
                "Read the numbers off the chart with the room: the earlier low of 0.45 that sets the line, 0.42 at 1 where volume tests it, 3.6 on the breakout bar at 2.",
            ),
        ),
        Content(
            origin="Book p.180: the reasons are the book's. Stop orders: Chapters 1 and 5. The PHP 48 and 52 edges are ours.",
            title="Why the lowest volume times the breakout",
            lines=(
                "1  Volume shrinks as each side finishes: most who wanted to buy have bought, most who wanted to sell have sold.",
                "2  Stop orders pile up outside the range: buy stops above PHP 52, sell stops below PHP 48 (Chapter 1: they trade once price pushes through their level).",
                "3  When price reaches one edge, those stops trigger together and push it out: the catalyst.",
                "4  Up or down, the book does not say: let price show the way.",
            ),
            accent="What to do: volume back at an earlier low, expect a breakout.",
            notes=(
                "Walk the four steps in order. Step 2 is the one students miss: the orders that start the move were placed during the quiet range.",
                "Step 4 is the book's either an upside or downside breakout. The signal is about timing only.",
            ),
        ),
        Pair(
            origin="Book p.180's four reasons, drawn on our invented range, PHP 48 to 52. Every price and volume is ours.",
            left=Content(
                title="The four steps on one range",
                lines=(
                    "1  Volume shrinks, to 0.42 million.",
                    "2  Buy stops wait above PHP 52, sell stops below PHP 48.",
                    "3  Price reaches the top edge: the buy stops trigger.",
                    "4  It breaks out up, on 3.6 million.",
                ),
                accent="The quiet range is where the breakout is loaded.",
            ),
            picture=Chart(
                letter="GA",
                shows="The invented range of Chart J, PHP 48 to 52, with the four steps marked: 1, volume shrinking from about 2 million to 0.42; 2, the buy stops above PHP 52 and the sell stops below PHP 48; 3, price reaching the top edge, where the buy stops trigger; 4, the breakout up on 3.6 million.",
            ),
            text_w=CHART_W,
            notes=(
                "Each number on the chart is the step of the same number on the slide before. Walk them in order.",
                "This one broke up. The same range could have broken down through the sell stops: price decides.",
            ),
        ),
        Pair(
            origin="Book pp.180-181 and Figure 6.9. Accumulation: Chapters 2 and 4.",
            left=Term(
                term="Low volume breakout signal",
                plain="A signal, not a trade: in a range, volume falls back to a low it has touched before, testing it. Expect price to leave the range soon, up or down.",
                example="Figure 6.9, Apple: in late March, inside the Accumulation box [2], a buying range (Chapters 2 and 4), volume falls back to the dashed low volume level [1], at [3]. In April price breaks out of the top.",
                formal="Whenever the volume is testing a significant minimum or its lowest historical levels, a breakout is expected. We refer to this as a low volume breakout signal.",
            ),
            picture=Figure(
                number="6.9",
                aspect=0.789,
                crop=(0.0, 0.45, 0.0, 0.0),
                marks=(
                    Mark(1, "line", 0.010, 0.874, 0.990, 0.874),
                    Mark(2, "box", 0.592, 0.215, 0.916, 0.456),
                    Mark(3, "circle", 0.804, 0.731, 0.924, 0.914, at=(0.940, 0.914)),
                ),
                shows="A daily Apple chart with a low volume level drawn across its volume panel. Circles mark two low volume reversals at time lines 1 and 2, a bearish divergence and a bearish confirmation, and later an accumulation box that price leaves on a low volume breakout signal.",
            ),
            text_w=6.2,
            notes=(
                "Find the box at the bottom right of the price panel, then the circle under it where volume sits on the low volume level. The breakout follows.",
                "The figure also labels a bearish divergence into the top and a bearish confirmation on the fall: Part 1's names on a real chart. The two circles at 1 and 2 are the next slide.",
            ),
        ),
        Pair(
            origin="Book p.180 gives the term; Figure 6.9 (p.181) has two. The chart is ours, on invented prices, because that figure is dense. The book does not say how the low is set.",
            left=Term(
                term="Low volume reversal",
                plain="Price turns as volume sits at its minimum. In a trend, volume testing its low says the trend may turn, the book's tendency; price shows which way.",
                example="Ours: volume shrinks to 0.55 million at 1, the PHP 56 peak, and price turns down. That low is the dashed line. At 2, PHP 47, volume falls back to it and price turns up.",
                formal="There is a tendency for price to reverse when volume is at its minimum or lowest historical levels. We refer to such reversals as low volume reversals.",
            ),
            picture=Chart(
                letter="K",
                shows="An invented price that rises to a peak at PHP 56, falls to a trough at PHP 47 and rises again, over its volume in millions of shares. At 1, the peak, volume shrinks to 0.55 million and price turns down; a dashed line marks that low. At 2, the trough, volume falls back to it and price turns up.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Two uses of the same low volume: in a range it times a breakout, in a trend it marks a turn. Figure 6.9 has two, at its time lines 1 and 2.",
                "The book gives a tendency and no rule for where the low volume level goes. Figure 6.9 draws it at earlier lows, and this chart draws it at the low set at 1.",
            ),
        ),
        Pair(
            origin="Book p.181 and Figure 6.10. Accumulation and distribution: Chapters 2 and 4. The 10 million is read by eye off the figure's scale.",
            left=Content(
                title="Breakouts at the lowest volume: silver",
                lines=(
                    "The three boxes are consolidations. The low volume threshold [1] runs low across the volume panel, near 10 million shares.",
                    "Dotted arrows: volume falls to it in each box. Then price breaks out: up at 1, from an accumulation; down at 2 and 3, from distributions, ranges where informed holders sell.",
                    "Volume rises on the breakout bars, [2], [3] and [4], under the book's 1, 2 and 3.",
                ),
                accent="One signal, three times: it said when; price chose the way.",
            ),
            picture=Figure(
                number="6.10",
                aspect=1.667,
                marks=(
                    Mark(1, "line", 0.006, 0.908, 0.994, 0.908),
                    Mark(2, "circle", 0.333, 0.817, 0.378, 0.933),
                    Mark(3, "circle", 0.754, 0.829, 0.799, 0.933),
                    Mark(4, "circle", 0.887, 0.796, 0.934, 0.933),
                ),
                shows="The daily iShares Silver Trust with three consolidations boxed and a low volume threshold drawn across the volume panel. Dotted arrows show volume falling to the threshold in each box, and the breakouts at bars 1, 2 and 3 follow, with volume rising on each breakout bar.",
            ),
            text_w=5.6,
            notes=(
                "The figure shows the signal three times: an accumulation breakout up at 1, distribution breakouts down at 2 and 3. Each comes as volume touches the line.",
                "Notice the breakout bars themselves carry more volume than the bars before them.",
            ),
        ),
        Check(
            label="Volume as a timing indicator",
            questions=(
                Q(
                    stem="Inside a consolidation, volume falls to its lowest level in a year. The book expects:",
                    options=("A breakout, to the upside or the downside",
                             "An upside breakout only",
                             "Bearish divergence, so a decline",
                             "The consolidation to last longer"),
                    answer="A",
                    reason="Volume testing its lowest historical level in a consolidation is a low volume breakout signal, either way.",
                ),
                Q(
                    stem="Why is there no divergence reading during a consolidation?",
                    options=("Volume is always flat in a consolidation",
                             "Divergence needs open interest",
                             "Consolidations only occur on low volume",
                             "Price is moving sideways, so neither direction can be read"),
                    answer="D",
                    reason="With price moving sideways it is not possible to tell divergence from convergence, let alone bullish from bearish.",
                ),
            ),
        ),
        Pair(
            origin="Book p.181. It defers the calculation to Chapter 11. Moving averages: met in Chapters 4 and 5. The chart is ours; its line is a 10-bar VWMA we computed.",
            left=Term(
                term="Volume-weighted moving average, VWMA",
                plain="A moving average: the average of the last few closes, redone at each new bar. Volume-weighted: each close counts by its volume, so heavy days pull the line toward their price.",
                example="Line at PHP 50: price at 52, above it, is potentially bullish; at 48, below it, potentially bearish. Our chart: the gold dot crosses above, the green dot below.",
                formal="A VWMA may be created to track overvalued and undervalued stock. Typically, price is considered potentially bullish when it is above the VWMA, and bearish when below it.",
            ),
            picture=Chart(
                letter="L",
                shows="An invented price line with its volume-weighted moving average drawn over it as a green line. Where price crosses above the line, a gold dot, it is labelled potentially bullish, and where it crosses below, a green dot, potentially bearish.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book's heading is Volume-Weighted Average Price/Moving Average, and its figure says VWAP. It treats the two names as one line here.",
                "The arithmetic is the next slide, and it is ours: the book leaves its own calculation to Chapter 11.",
            ),
        ),
        Content(
            origin="Ours: how our charts compute the line, read from build/charts_chapter06.py, on invented numbers. The book's own calculation is in its Chapter 11.",
            title="How our VWMA line is computed, with numbers",
            lines=(
                "Ours: three bars close at PHP 50, 52 and 54, on 1, 1 and 2 million shares.",
                "Plain average: (50 + 52 + 54) / 3 = PHP 52. Every bar counts the same.",
                "Volume-weighted: each close times its volume, added up, divided by the total volume: (50 x 1 + 52 x 1 + 54 x 2) / 4 = 210 / 4 = PHP 52.50.",
                "The heavy PHP 54 day pulls the line up toward it. At the next bar, drop the oldest, add the newest, compute again; our charts use 10 bars.",
            ),
            accent="The VWMA: the average price, weighted by how much traded at it.",
            notes=(
                "Do the plain average first, then the weighted one, and ask why the second is higher. The answer is the heavy day.",
                "Say plainly this is our computation, the one the two VWMA charts use. The book's own is in Chapter 11 and is not examined here.",
            ),
        ),
        Pair(
            origin="Book p.181 and Figure 6.11. The figure is labelled VWAP on a 10-minute chart; the caption says VWMA, daily. Support and resistance: Chapter 5.",
            left=Content(
                title="The VWMA on a chart",
                lines=(
                    "A 10-minute chart of the S&P 500 SPDR. Dashed [1]: the line labelled VWAP, volume-weighted average price; the book treats VWAP and VWMA as one line here.",
                    "[2] Price rises decisively each time it crosses above the line, and falls after crossing below.",
                    "[3] The four circles: each day's volume peak, its busiest stretch (Part 5). Dashed arrows run up from each: the crossovers came at those peaks.",
                ),
                accent="Above the line, bullish; below it, bearish.",
                caption="So watch each day's busiest stretch: the crossovers came there, and the book gives no rule beyond that. The line also acts as support, a floor, and resistance, a ceiling (Chapter 5).",
            ),
            picture=Figure(
                number="6.11",
                aspect=1.724,
                marks=(
                    Mark(1, "arrow", 0.470, 0.200, 0.400, 0.440, at=(0.470, 0.200)),
                    Mark(2, "circle", 0.472, 0.504, 0.537, 0.621, at=(0.452, 0.640)),
                    Mark(3, "box", 0.080, 0.770, 0.730, 0.900, at=(0.050, 0.835)),
                ),
                shows="A 10-minute chart of the S&P 500 SPDR over four days with a dashed volume weighted average price line, labelled price above it bullish and below it bearish, and the line marked as support and as resistance. Circles on the volume panel mark the daily volume cycle peaks, with arrows from them to the crossovers.",
            ),
            text_w=6.0,
            notes=(
                "Follow each dashed arrow from a circled volume peak up to a crossover. That is the book's point about timing.",
                "Name the mismatch and move on: the caption says VWMA and daily, the figure says VWAP and 10 minutes.",
            ),
        ),
        Pair(
            origin="Book p.181. Both readings are the book's, a paragraph apart; it does not reconcile them. The chart and the PHP 50 example are ours.",
            left=Content(
                title="Undervalued below, overvalued above",
                lines=(
                    "The book also calls a stock undervalued below the VWMA and overvalued above it.",
                    "Its buy signals come from another method, unnamed; the VWMA only decides whether to take one.",
                    "Institutions buy only below the line, sell only above. Ours, line at PHP 50: a buy signal at 48, yes; at 52, no.",
                    "So above the line is bullish for the trend, yet overvalued: not where institutions buy.",
                ),
                accent="Two readings of one line, both the book's.",
            ),
            picture=Chart(
                letter="M",
                shows="The same kind of invented price and VWMA line. Stretches below the line are shaded and labelled undervalued, where institutions look to buy; stretches above are labelled overvalued, where they look to sell.",
            ),
            text_w=CHART_W,
            notes=(
                "Read both sentences from the book. One says above the line is bullish; the next says above the line is overvalued, where institutions sell.",
                "Do not invent a reconciliation. If a student asks, the answer is that the book gives both and the course teaches both.",
            ),
        ),
        Pair(
            origin="Book pp.182-183, its four scenarios. Chapter 4 named the climaxes by who trades. The chart is ours: sketches, with our invented volumes.",
            left=Content(
                title="Tops and bottoms: volume at the extremes",
                lines=(
                    "Back from the VWMA to volume itself: how much trades on the day a market turns?",
                    "The book: tops and bottoms usually come on relatively large or extreme volume, or relatively low or minimal volume.",
                    "Ours, usual volume 2 million a day. On 9 million: a top is a blow-off or buying climax; a bottom, a sell-off or selling climax.",
                    "On 0.3 million: a low volume top, or a low volume bottom.",
                ),
                accent="Four turns, named by place and by volume.",
            ),
            picture=Chart(
                letter="N",
                shows="Four small cases, each a price turn over its volume, the other days at about 2 million shares. A top on one towering bar of 9 million, the blow-off or buying climax. A bottom on a towering bar of 9 million, the sell-off or selling climax. A top on a bar of 0.3 million, a low volume top. A bottom on 0.3 million, a low volume bottom.",
            ),
            text_w=CHART_W,
            notes=(
                "The climaxes are a recall: Chapter 4 told who buys and sells in them. What is new is the volume, and the two low volume names.",
                "Ask for the two choices that make the four names: where the turn is, and whether volume is huge or tiny.",
            ),
        ),
        Content(
            origin="Book pp.182-185. Who trades in each climax: Chapter 4, its accumulation and distribution slides.",
            title="Why the quiet pair matters, and why sell-off",
            lines=(
                "Ours: one peak at PHP 60. On 9 million the rise ends in a frenzy; on 0.3 million it runs out of interest. Watch only spikes and you miss the second.",
                "Every trade has a buyer and a seller; the names say who was rushing.",
                "Selling climax, Chapter 4: a deep fall ends as the uninformed sell at any price and the informed buy from them.",
                "Buying climax, the mirror: a strong rise ends as the uninformed buy at any price and the informed sell to them.",
            ),
            accent="The quiet pair are the low volume reversals: turns on silence.",
            notes=(
                "This answers the question a student asks first: if every share sold was bought, why call it a sell-off? Because of who is rushing, and which way price had been going.",
                "The heavy volume of a selling climax is the panicked selling, and the informed buyers absorbing it. The quiet turns get their own figure after the climaxes, in the book's order.",
            ),
        ),
        Pair(
            origin="Book p.183 and Figure 6.12. Exxon Mobil is spelt Exxon Mobile by the book.",
            left=Term(
                term="Upper and lower overextended volume levels",
                plain="Overextended volume: far above usual. The upper level is a line only the most extreme spikes reach; a lower one, still high, is reached more often.",
                example="Figure 6.12, Exxon Mobil: the extreme volume of two selling climaxes [1], under the ellipse, sets the upper level [2].",
                formal="The extreme volume level is the upper overextended volume level, a signal for predicting potential bottoms or tops. A lower overextended volume level forecasts less significant corrections.",
            ),
            picture=Figure(
                number="6.12",
                aspect=1.295,
                marks=(
                    Mark(1, "box", 0.340, 0.600, 0.590, 0.760, at=(0.465, 0.690)),
                    Mark(2, "line", 0.222, 0.617, 0.929, 0.617, at=(0.929, 0.617)),
                ),
                shows="The daily chart of Exxon Mobil from 2006 to 2013: an ellipse around a market bottom made by two selling climaxes, with arrows down to two volume spikes. Across the volume panel run two lines, upper level volume overextension, near 120 million shares, and lower level volume overextension, near 70 million.",
            ),
            text_w=6.2,
            notes=(
                "Point at the two arrows from the ellipse down to the volume panel: each joins a selling climax to its spike.",
                "Upper for the big turns, lower for the corrections. What each tells, with the figure's numbers, is the next slide.",
            ),
        ),
        Pair(
            origin="Book p.183 and Figure 6.12, its scale read by eye.",
            left=Content(
                title="Figure 6.12's two levels, read off its scale",
                lines=(
                    "[1] Most days trade under 40 million shares.",
                    "[2] The lower line: a little under 70 million.",
                    "[3] The upper line: a little above 120 million.",
                    "[4] and [5] The two spikes that reach it sit under bottoms.",
                ),
                accent="Both lines are far above a usual day.",
            ),
            picture=Figure(
                number="6.12",
                aspect=1.295,
                marks=(
                    Mark(1, "box", 0.007, 0.866, 0.935, 0.973),
                    Mark(2, "line", 0.041, 0.778, 0.935, 0.778, at=(0.860, 0.778)),
                    Mark(3, "line", 0.222, 0.617, 0.935, 0.617, at=(0.935, 0.617)),
                    Mark(4, "circle", 0.334, 0.559, 0.391, 0.663, at=(0.334, 0.700)),
                    Mark(5, "circle", 0.540, 0.640, 0.585, 0.740, at=(0.585, 0.740)),
                ),
                shows="The daily chart of Exxon Mobil from 2006 to 2013. Most volume bars sit under 40 million shares; a lower overextension line runs near 70 million and an upper one near 120 million, and the two spikes that reach the upper line sit under the market bottom in the ellipse.",
            ),
            text_w=WIDE_W,
            notes=(
                "Read the scale with the room: the gold box is an ordinary day, the red line the lower level, the blue line the upper.",
                "The two green circles are the selling climaxes from the term slide, the only spikes to reach the upper level.",
            ),
        ),
        Content(
            origin="Book p.183. Correction: Chapter 5. Not a promise: the book's word potential, said plainly.",
            title="What the two levels tell you",
            lines=(
                "Both are high volume: lower means less extreme, not low volume.",
                "Upper: potential tops or bottoms, a warning and not a promise. Lower: less significant corrections, smaller moves against the trend.",
                "Exxon's chart shows only bottoms; the book says the same level signals tops too.",
            ),
            accent="Above the line: a potential turn. Which way: price, afterwards.",
            notes=(
                "The trap is the word lower. A lower overextended level is still high volume, only less extreme.",
                "Which way the turn goes is the book's caution at the end of this part: overbought or oversold, only in retrospect.",
            ),
        ),
        Pair(
            origin="Book p.183 and Figure 6.13. The volumes are read by eye off the figure's scale.",
            left=Content(
                title="Blow-offs: buying climaxes",
                lines=(
                    "A blow-off, or buying climax: a market top on extreme volume, the mirror of Exxon's selling climaxes.",
                    "Follow each arrow from BLOW-OFF to its circled volume spike, [1] and [2], then up to the top above it, [3] and [4]. Price falls after each.",
                    "Relatively high, the book says: the first spike tops 200 thousand shares, the second only about 100 thousand, yet each towers over its neighbours.",
                ),
                accent="Compare a spike with its own neighbours, not with the biggest bar.",
            ),
            picture=Figure(
                number="6.13",
                aspect=1.932,
                marks=(
                    Mark(1, "circle", 0.182, 0.665, 0.215, 0.827, at=(0.120, 0.800)),
                    Mark(2, "circle", 0.733, 0.816, 0.765, 0.947, at=(0.790, 0.860)),
                    Mark(3, "circle", 0.170, 0.326, 0.228, 0.495),
                    Mark(4, "circle", 0.723, 0.085, 0.777, 0.229),
                ),
                shows="The daily chart of the E-TRACS UBS Bloomberg CMCI Food ETN with two circled volume spikes labelled blow-off, each under a market top: the first above 200 thousand shares, the second about 100 thousand.",
            ),
            text_w=5.6,
            notes=(
                "The mirror of the last figure: tops this time. Follow each arrow from BLOW-OFF to its spike and up to its top.",
                "The second blow-off is on a much smaller spike than the first in absolute terms. Compare it with the volume around it, not with the first.",
            ),
        ),
        Pair(
            origin="Book pp.183-184 and Figure 6.14. Support: Chapter 5.",
            left=Content(
                title="Where to set the overextension level",
                lines=(
                    "By visual inspection, the book says: by eye, no formula. Find the spikes under the most significant tops and bottoms; draw the line just below them.",
                    "Set lower, more spikes cross it: more frequent signals, at less significant tops and bottoms.",
                    "Figure 6.14, gold: the circled spikes [2] cross the dashed level [1]. At the far right price breaks a significant support [3], a level where falls had stopped, on extreme volume.",
                ),
                accent="Higher level, fewer and bigger turns.",
                caption="The figure's second, computed line: next slide.",
            ),
            picture=Figure(
                number="6.14",
                aspect=1.646,
                marks=(
                    Mark(1, "line", 0.006, 0.819, 0.994, 0.819),
                    Mark(2, "circle", 0.497, 0.737, 0.578, 0.864),
                    Mark(3, "circle", 0.902, 0.206, 0.988, 0.329),
                ),
                shows="The daily SPDR Gold Trust: a dashed volume overextension line across the volume panel with circled spikes above it, a stepped computed line under it, and a dashed support line on the price that is broken at the right on extreme volume, labelled above the rolling 100-day 2-sigma level.",
            ),
            text_w=5.6,
            notes=(
                "By eye is the book's method: there is no formula for the line. Ask the room where they would draw it on this chart to catch only the circled spikes.",
                "Find the support break at the far right: price falls through a significant level on extreme volume.",
            ),
        ),
        Content(
            origin="Book p.184 names the rolling 100-day 2-sigma level. Ours: the arithmetic and the 20 and 10 million.",
            title="The figure's second line: a rolling 2-sigma level",
            lines=(
                "Rolling 100-day 2-sigma level = 100-day average volume + 2 x sigma. Sigma, the standard deviation: how far volume typically strays from its average.",
                "Ours: average 20 million, sigma 10 million: 20 + 2 x 10 = 40 million. A 35 million day stays under; 55 million crosses.",
                "Rolling: redone daily over the latest 100 days, so the level moves as old days leave the window.",
            ),
            accent="By eye or by formula: only volume above the line counts.",
            notes=(
                "Keep it to the arithmetic. Part 3 teaches the sigma filter properly, with its own worked example and the bar-by-bar method.",
                "The next slide finds this line on the gold chart and shows it moving.",
            ),
        ),
        Pair(
            origin="Book p.184 names the rolling line. Ours: why it steps, read by eye off Figure 6.14.",
            left=Content(
                title="The rolling line on Figure 6.14",
                lines=(
                    "[1] On Figure 6.14, the solid line under the dashed level is the rolling level.",
                    "[2] The August 2011 spikes enter its window: the line steps up.",
                    "[3] Some 100 days later they leave, and it drops back.",
                ),
                accent="The level follows volume's recent past: what counts as extreme changes over time.",
            ),
            picture=Figure(
                number="6.14",
                aspect=1.646,
                marks=(
                    Mark(1, "arrow", 0.269, 0.975, 0.312, 0.889),
                    Mark(2, "arrow", 0.490, 0.979, 0.522, 0.852),
                    Mark(3, "arrow", 0.675, 0.979, 0.642, 0.864),
                ),
                shows="The daily SPDR Gold Trust with its volume panel: the solid rolling 100-day 2-sigma line steps up after the August 2011 volume spikes and drops back some 100 days later.",
            ),
            text_w=WIDE_W,
            notes=(
                "Find the solid line first, mark 1. Then the step up under the August 2011 spikes, mark 2, and where it drops back, mark 3.",
                "A fixed line, drawn by eye, does not move; this one does, because only the latest 100 days count.",
            ),
        ),
        Pair(
            origin="Ours, drawing the book's p.183 rule on one invented chart. Both levels, every price and every volume are ours.",
            left=Content(
                title="Our example: a higher level and a lower one",
                lines=(
                    "Ours: ordinary bars trade 0.9 to 1.5 million shares. Upper level 4.0 million, lower 2.2, both by eye.",
                    "Upper: only the spikes of 4.6 million cross it, at 1, the top at PHP 60, and at 2, the bottom at PHP 42. Two signals, both major turns.",
                    "Lower: those two, plus spikes of 2.6 million at a, b and c, smaller corrections. Five signals.",
                ),
                accent="Where the line goes decides which turns it signals.",
                caption="Only the major turns: the upper line. The corrections too: the lower, which flags smaller moves.",
            ),
            picture=Chart(
                letter="O",
                shows="An invented price with two major turns and three smaller corrections, over its volume in millions of shares. Two dashed lines cross the volume panel, an upper level at 4.0 and a lower at 2.2. Only the spikes of 4.6 at the major turns, numbered 1 and 2, cross the upper line; the spikes of 2.6 at the corrections, lettered a to c, cross only the lower one.",
            ),
            text_w=CHART_W,
            notes=(
                "The numbers are the big turns and the letters the small ones. Ask the room which line they would draw to trade only the big ones.",
                "Both lines were placed by eye, the way the book says to.",
            ),
        ),
        Pair(
            origin="Book p.184 and Figure 6.15. The book does not explain the Bollinger Bandwidth. The figure's caption calls 1 and 2 selling climaxes.",
            left=Content(
                title="Volatility spikes at the same turns",
                lines=(
                    "Volatility: how widely price swings. The bottom panel, a Bollinger Bandwidth oscillator, is the book's gauge of it here; the chapter does not say how it is calculated.",
                    "Thin upright lines join circled volatility spikes [1] to volume crossing the overextension lines [2], and up to turns in price.",
                    "At the book's 1 and 2, lows after sharp falls, volume and volatility spike together.",
                ),
                accent="Two different measures flag the same turns.",
            ),
            picture=Figure(
                number="6.15",
                aspect=1.751,
                marks=(
                    Mark(1, "box", 0.244, 0.840, 0.765, 0.937, at=(0.210, 0.840)),
                    Mark(2, "box", 0.460, 0.510, 0.865, 0.652, at=(0.500, 0.510)),
                ),
                shows="The continuous daily chart of silver with an upper and a lower volume overextension line, and under it a bandwidth oscillator labelled volatility, with its own historical volatility level. Thin lines join circled volatility spikes to volume overextensions and to two lows after sharp falls, at 1 and 2.",
            ),
            text_w=6.0,
            notes=(
                "Two kinds of evidence agree at 1 and 2: volume overextended, and volatility spiking.",
                "Do not teach the bandwidth. Say it is a measure of volatility the book uses here and explains elsewhere.",
            ),
        ),
        Pair(
            origin="Book p.184 and Figure 6.15, its two volatility lines read by eye.",
            left=Content(
                title="Figure 6.15's two volatility lines",
                lines=(
                    "[1] The dashed line, near 15: below it is noise, which many practitioners filter out. All four circled spikes clear it.",
                    "[2] The historical volatility level, near 40: only the spikes under the book's two lows reach it.",
                ),
                accent="A low line for noise, a high one for the major turns.",
            ),
            picture=Figure(
                number="6.15",
                aspect=1.751,
                marks=(
                    Mark(1, "line", 0.006, 0.897, 0.863, 0.897),
                    Mark(2, "line", 0.575, 0.766, 0.863, 0.766),
                ),
                shows="The continuous daily chart of silver, its volume with two overextension lines, and under it a bandwidth oscillator labelled volatility: a dashed noise line near 15 that four circled spikes clear, and a historical volatility level near 40 that only the two spikes under the book's lows 1 and 2 reach.",
            ),
            text_w=WIDE_W,
            notes=(
                "The wavy stretch under the gold line is what the figure labels noise. Then the red line: only two spikes reach it.",
                "The book's own labels 1 and 2 on the price are the two lows; the coloured numbers are ours.",
            ),
        ),
        Content(
            origin="Book p.184. Evidence that corroborates: the chapter's first slide, p.173.",
            title="What the volatility spike adds",
            lines=(
                "A second, separate measure, price's swings, agreeing with volume at the same turns: evidence that corroborates, the chapter's first idea.",
                "A spike above the noise line is a real one; a spike at the historical level marks a major turn, as on the volume panel's upper line.",
                "Both crossing together is stronger evidence; the book gives no weighting.",
            ),
            accent="As on volume: a low line for noise, a high one for the major turns.",
            notes=(
                "Volume and volatility are two separate measures. When both cross their high lines on the same day, two kinds of evidence agree.",
                "This slide goes with the two before: drop all three or none.",
            ),
        ),
        Check(
            label="Climaxes and overextension",
            questions=(
                Q(
                    stem="A market top forms on extreme volume. The book calls it:",
                    options=("A low volume top",
                             "A selling climax",
                             "A low volume breakout signal",
                             "A blow-off or buying climax"),
                    answer="D",
                    reason="A market top associated with extreme volume is a blow-off or buying climax.",
                ),
                Q(
                    stem="A trader lowers the volume overextension level on a chart. The signals will be:",
                    options=("Fewer, at more significant tops and bottoms",
                             "More frequent, at less significant tops and bottoms",
                             "Unchanged, because the level is set by eye",
                             "Limited to selling climaxes"),
                    answer="B",
                    reason="Setting the level lower tends to signal less significant tops or bottoms more frequently.",
                ),
            ),
        ),
        Pair(
            origin="Book pp.183, 185 and Figure 6.16. The 2 and 0.3 million are ours.",
            left=Term(
                term="Low volume top and low volume bottom",
                plain="A top, or a bottom, made on very little volume. Ours: usual volume 2 million a day; a peak, or a trough, on 0.3 million.",
                example="Figure 6.16, Apple: seven circles where volume dips to a lower threshold [1], set by a rule the book does not give. Each time line runs up to a turn [2].",
                formal="A market top associated with extremely low or minimal volume is called a low volume top. A market bottom associated with extremely low volume is called a low volume bottom.",
            ),
            picture=Figure(
                number="6.16",
                aspect=1.649,
                marks=(
                    Mark(1, "line", 0.037, 0.911, 0.935, 0.911),
                    Mark(2, "arrow", 0.345, 0.862, 0.345, 0.161, at=(0.310, 0.200)),
                ),
                shows="A daily Apple chart with a low volume threshold drawn across its volume panel and circled wherever volume tests it. Dashed time lines run up from each circle to a top or a bottom in price, labelled low volume reversals.",
            ),
            text_w=6.2,
            notes=(
                "These are the low volume reversals of the part's start, now named by where they turn: at a top or at a bottom.",
                "The tops are in late 2007, the clearest bottom in March 2009. The book says only that the threshold is tested.",
            ),
        ),
        Content(
            origin="Book pp.180 and 185. The reason is the book's for breakouts, p.180; it gives none for these turns.",
            title="Reading a low volume turn",
            lines=(
                "What it means: when volume falls to its threshold, expect a turn, the book's tendency.",
                "Why, by the book's reason for breakouts: those who wanted to trade have traded, so the move runs out of participants. The book gives that reason for breakouts, not for turns.",
                "Top or bottom: the touch does not say. Wait for price to show which it was.",
            ),
            accent="Volume going quiet says a turn may come; price says which.",
            notes=(
                "This is the quiet mirror of the climaxes: a turn on silence. The catch is the same as for the spikes on the next slide: volume does not say which way.",
                "Be plain that the reason is borrowed from the breakout passage, and the slide says so.",
            ),
        ),
        Pair(
            origin="Book p.186. The chart is ours: sketches, with our invented volumes. Overbought and oversold are used and not defined in this chapter.",
            left=Content(
                title="Overbought or oversold? Only afterwards",
                lines=(
                    "Back to the spikes, with one caution.",
                    "Overextended volume can signal a top or a bottom: extreme buying and selling both generate volume.",
                    "Overbought: an extreme tied to a top; oversold, to a bottom: the book's usage. Plain words, ours: risen too far, fallen too far.",
                    "Our chart: the same 9 million spike twice. Price rose into it, then fell: a top. Or fell, then rose: a bottom.",
                ),
                accent="Overextension: pinpointed now. Overbought or oversold: only in retrospect.",
            ),
            picture=Chart(
                letter="P",
                shows="Two small cases with the same volume record, one bar of 9 million among bars of about 2 million. In one, price had been rising and it turns out to be a top: overbought, in retrospect. In the other, price had been falling and it turns out to be a bottom: oversold, in retrospect.",
            ),
            text_w=CHART_W,
            notes=(
                "The two volume bars are identical. Only what price did next tells you which one it was.",
                "This slide is where it is because the book puts the caution here, after the low volume tops and bottoms. Say so, and point back to the climaxes it is about.",
            ),
        ),
        Content(
            origin="Book p.186. Where the caution sits is the book's order. That it is silent on the quiet turns is a reading of p.186, which names overextensions only.",
            title="What the caution teaches",
            lines=(
                "The point: a volume spike tells you something is happening, not what. Volume alone cannot call a market overbought or oversold.",
                "So do not trade the spike alone: name the overextension now, and wait for price to show which way it turned.",
                "It returns to the spikes because the book puts the caution here, p.186.",
                "The book is silent on two things: whether the quiet turns carry it too, and what overbought and oversold mean.",
            ),
            accent="Volume says a turn is likely; price says which kind it was.",
            notes=(
                "This is the slide that answers why the deck goes back to high volume: it is the book's order, and the caution is about the spikes.",
                "Do not extend the caution to the low volume turns. The book does not, so the course does not.",
            ),
        ),
        Pair(
            origin="Book p.186 and Figure 6.17.",
            left=Content(
                title="Lower timeframes are more sensitive",
                lines=(
                    "Timeframe: the time one bar covers. A monthly bar adds up every day of the month.",
                    "Figure 6.17, gold: daily and weekly volume peak in 2013 [1]; monthly, quarterly and yearly peak in 2011 [2].",
                ),
                accent="Lower timeframes are more sensitive: one day's burst shows. Higher ones show the overall trend of volume.",
            ),
            picture=Figure(
                number="6.17",
                aspect=0.862,
                crop=(0.0, 0.36, 0.0, 0.0),
                marks=(
                    Mark(1, "box", 0.876, 0.004, 0.944, 0.271, at=(0.770, 0.050)),
                    Mark(2, "box", 0.757, 0.406, 0.811, 0.988),
                ),
                shows="The continuous chart of gold with five volume panels under it: daily, weekly, monthly, quarterly and yearly. Lines over each mark where its volume peaks: in 2013 on the daily and weekly panels, in 2011 on the monthly, quarterly and yearly ones.",
            ),
            text_w=4.6,
            notes=(
                "Find the circled spike in 2013 on the daily and weekly panels. Then find where monthly and above peak: 2011.",
                "Lower timeframes are more sensitive: the one-day burst shows on daily and weekly bars and vanishes into the monthly ones.",
            ),
        ),
        Content(
            origin="Book p.186's point, worked. The 10, 3 and 6 million are ours, to show the arithmetic.",
            title="Why the peaks differ: the arithmetic",
            lines=(
                "Ours: a record 2013 day of 10 million, in a month of 19 quiet days of 3 million: 10 + 57 = 67 million for the month.",
                "A 2011 month with no record day, 20 days of 6 million: 20 x 6 = 120 million, the monthly peak.",
                "So the record day tops the daily bars, and the steady month tops the monthly ones.",
            ),
            accent="Daily to spot a single burst; monthly or higher to see the trend in volume.",
            notes=(
                "Work the two sums on the board: 67 million for the record day's month against 120 million for the busy month.",
                "One big day cannot outweigh twenty busy ones once the days are added up.",
            ),
        ),
        Pair(
            origin="Ours: the book's p.186 point on one invented volume record. The days, the spike and the months are ours, and the sums are read from it.",
            left=Content(
                title="Our example: one record, two timeframes",
                lines=(
                    "Daily: the tallest bar is one spike of 6.0 million shares, late in the record, at 1.",
                    "Monthly, the same days added twenty at a time: the spike's month comes to only 24.4 million, one big day and nineteen of about 1 million.",
                    "The busiest month, 2, comes earlier: no day above 3.5 million, but twenty of them add to 55.7 million.",
                ),
                accent="One volume record, two different peaks: it depends on the timeframe.",
            ),
            picture=Chart(
                letter="Q",
                shows="One invented volume record drawn twice. Upper panel, daily bars: the tallest is a single spike of 6.0 million late in the record, marked 1. Lower panel, the same days summed into monthly bars: the tallest is a busy month earlier on, 55.7 million, marked 2, and the late spike's month comes to only 24.4 million.",
            ),
            text_w=CHART_W,
            notes=(
                "Nothing changes between the two panels but the length of the bar: the same shares, added up by day or by month.",
                "So the daily chart reacts to one day; the monthly chart shows the broad shape of participation.",
            ),
        ),
        Check(
            label="Low volume turns and timeframes",
            questions=(
                Q(
                    stem="A market bottom forms on extremely low volume. The book calls it:",
                    options=("A sell-off",
                             "A low volume bottom",
                             "A selling climax",
                             "An upper overextended volume level"),
                    answer="B",
                    reason="A market bottom associated with extremely low volume is a low volume bottom.",
                ),
                Q(
                    stem="Why does the book say volume extremes can be called overbought or oversold only in retrospect?",
                    options=("Volume is not an oscillator",
                             "Volume extremes only occur at bottoms",
                             "An overextension can signal either a top or a bottom",
                             "Overbought levels are set by eye"),
                    answer="C",
                    reason="Extreme buying and selling both generate volume, so only the top or bottom that follows tells which it was.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Part 3 - 6.1, pp.187 to 190: volume and the strength of a price barrier,
# and the ways of filtering volume.
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="The Mechanics of Volume Action: Price Barriers and Filtering",
    short="6.1 Filtering",
    minutes="",
    covers=(),
    slides=(
        Pair(
            origin="Book p.187 and Figure 6.18. Barrier and retest: Chapter 5's words. The book gives no volume number for a peak or a dip.",
            left=Content(
                title="6.1  Volume and the strength of a price barrier",
                lines=(
                    "Barrier (Chapter 5): a resistance above price stops a rise; a support below price stops a fall.",
                    "Retest (Chapter 5): price coming back later to a barrier it touched before.",
                    "Volume peak: the tallest bar comes at the touch, the bar where price meets the barrier. Resistance 1 [1], Support 1 [2].",
                    "Volume dip or trough: the shortest bar comes at the touch. Resistance 2 [3], Support 2 [4].",
                ),
                accent="The book: the peak is the most reliable.",
            ),
            picture=Figure(
                number="6.18",
                shows="Four sketches under the question which price barrier is more reliable. Resistance 1 and Support 1 are each touched as volume peaks; Resistance 2 and Support 2 are each touched as volume dips to its lowest.",
                aspect=1.282,
                marks=(
                    Mark(1, "box", 0.19, 0.30, 0.31, 0.51, at=(0.19, 0.53)),
                    Mark(2, "box", 0.71, 0.33, 0.84, 0.53, at=(0.70, 0.55)),
                    Mark(3, "box", 0.19, 0.90, 0.31, 0.995),
                    Mark(4, "box", 0.71, 0.90, 0.84, 0.995),
                ),
            ),
            text_w=6.0,
            notes=(
                "Ask the question on the figure before answering it. Point at the touch in each sketch, then at the volume bar under it: tallest in the top row, shortest in the bottom row.",
                "Barrier is Chapter 5's word, from barrier proximity: a support below price or a resistance above it. Retest was Chapter 5's too, price returning to a level it touched before.",
                "Why the peak wins comes on the next slide, with numbers.",
            ),
        ),
        Pair(
            origin="Book p.187: the reasons are the book's. Ours: PHP 60 and every volume number, invented to show the two shapes.",
            left=Content(
                title="Why a volume peak makes the stronger barrier",
                lines=(
                    "Ours: twice, price rises to PHP 60 and turns down. Volume in millions of shares.",
                    "A: 9 million at the touch, more than any other bar. Even that surge could not get through, so traders expect PHP 60 to hold.",
                    "B: 0.5 million at the touch, less than any other bar. It held only for lack of buying: hardly anyone tried.",
                ),
                accent="On a retest, A is the stronger barrier.",
                caption="The book: since expectation is everything in the market, that confidence goes a long way.",
            ),
            picture=Chart(
                letter="RA",
                shows="Two invented sketches side by side, each a price rising to a resistance at PHP 60, turning down, then coming back to it for a retest, over its volume in millions of shares with every bar numbered. A: 9 million at the touch, the most of the move, the most reliable. B: 0.5 million at the touch, the least, less reliable.",
            ),
            text_w=CHART_W,
            notes=(
                "Read A first: the biggest push of the move hit PHP 60 and still failed. Then B: nobody pushed, so the level was never really tested.",
                "The chart does not draw what happens at the retest. The book says only which barrier is more reliable, not that B will break.",
            ),
        ),
        Pair(
            origin="Book pp.187-188 and Figure 6.19. Across: the book does not define it; this reading is ours, from the figure.",
            left=Content(
                title="Five kinds of volume action at a barrier",
                lines=(
                    "Across: the bars before, at and after the touch, which the dashed arrow marks. Only the volume differs between sketches.",
                    "[1] Increasing: each bar taller. [2] Decreasing: each shorter. [3] Peaking: tallest at the touch.",
                    "[4] Bottoming: shortest at the touch. [5] Flatlining: all alike.",
                ),
                accent="Top: resistance. Bottom: support.",
                caption="The book: increasing or decreasing volume there signifies a change in sentiment, the crowd's mood (Chapter 1).",
            ),
            picture=Figure(
                number="6.19",
                shows="Ten sketches in two rows, five at a resistance and five at a support, each with volume bars under the turn: increasing, decreasing, peaking, bottoming and flatlining across the barrier.",
                aspect=1.479,
                marks=tuple(Mark(n + 1, "box", 0.01 + 0.2 * n, 0.17,
                                 0.19 + 0.2 * n, 0.37) for n in range(5)),
            ),
            text_w=5.2,
            notes=(
                "Peaking and bottoming are the two cases of Figure 6.18. Increasing, decreasing and flatlining are new.",
                "In every sketch the price curve is the same; only the volume bars change. Read the bars left to right.",
            ),
        ),
        Pair(
            origin="Book p.188. Confirmation, bullish and bearish: Part 1. The chart is ours: sketches and invented volume.",
            left=Content(
                title="Increasing volume: price driven away",
                lines=(
                    "Increasing, ours: 1, 2, 3 million on the way in, 4 at the touch, 5, 6, 7 on the way out.",
                    "The book: rising volume on the way in looks strong enough to break through. Instead price turns, and the rising volume drives it away.",
                    "At a resistance price falls as volume rises: Part 1's bearish confirmation. At a support both rise: bullish confirmation.",
                ),
                accent="Rising volume across a barrier confirms the turn away from it.",
            ),
            picture=Chart(
                letter="R",
                shows="Two small sketches, each a price over its volume in millions of shares, every bar numbered 1 to 7 and the touch in gold. At a resistance, price rises to the line and is driven down and away: bearish confirmation. At a support, price falls to the line and is driven up and away: bullish confirmation.",
            ),
            text_w=CHART_W,
            notes=(
                "The book's sentences on increasing and decreasing volume are hard going. This slide takes increasing alone: what volume does, then what price does next.",
                "Price down with volume up is bearish confirmation, Part 1's name for it: at a resistance the rising volume is the selling that drives price down.",
            ),
        ),
        Pair(
            origin="Book p.188. Penetration: Chapter 2. The chart is ours: sketches and invented volume, its retests drawn from the book's words.",
            left=Content(
                title="Decreasing volume: a retest is likely",
                lines=(
                    "Decreasing, ours: 7, 6, 5 million on the way in, 4 at the touch, 3, 2, 1 on the way out.",
                    "The book: falling volume on the way in looks like too little force to take price through.",
                    "Price turns, and volume falls even further: little force is driving price away.",
                    "So a retest is likely; in extreme cases price goes through, a penetration (Chapter 2).",
                ),
                accent="Falling volume across a barrier invites a retest.",
            ),
            picture=Chart(
                letter="RB",
                shows="Two small sketches, each a price over its volume in millions of shares, every bar numbered 7 down to 1 and the touch in gold. At a resistance, price turns down and then comes back up to the line: a retest. At a support, price turns up and then comes back down to the line: a retest.",
            ),
            text_w=CHART_W,
            notes=(
                "Decreasing volume across the barrier is the one to watch: the book says it tends to see a retest, and in more extreme circumstances price may return to penetrate it.",
                "Figure 6.19 draws price turning cleanly in every case. The retests on our chart are drawn from the book's words, and the chart gives them no volume because the book gives none.",
            ),
        ),
        Pair(
            origin="Book pp.187-188. The chart is ours: sketches and invented volume.",
            left=Content(
                title="Peaking, bottoming and flatlining",
                lines=(
                    "Peaking, ours: 1, 2, 4, 7 at the touch, 4, 2, 1. The book: most reliable.",
                    "Bottoming: 7, 4, 2, 1 at the touch, 2, 4, 7. The book: less reliable.",
                    "Flatlining: 4 on every bar. The book: not enough information about price's next move.",
                    "The other two: increasing confirms the turn, decreasing invites a retest.",
                ),
                accent="A peak is the most reliable; the book does not rank it against increasing.",
            ),
            picture=Chart(
                letter="RC",
                shows="Six small sketches, top row at a resistance and bottom row at a support, each over its volume in millions of shares with every bar numbered and the touch in gold. Peaking, 7 at the touch: the most reliable. Bottoming, 1 at the touch: less reliable. Flatlining, 4 on every bar: not enough information.",
            ),
            text_w=CHART_W,
            notes=(
                "Peaking and bottoming are the volume peak and the volume dip of Figure 6.18, now with numbers. Flatlining is the only new one.",
                "Flatlining is not a weak barrier or a strong one. The book says it gives too little information to tell.",
            ),
        ),
        Check(
            label="Volume at a price barrier",
            questions=(
                Q(
                    stem="Which support is regarded as the most reliable barrier to future retests?",
                    options=("One formed at a volume peak",
                             "One formed across a volume trough",
                             "One formed on flatlining volume",
                             "One formed on decreasing volume"),
                    answer="A",
                    reason="Support formed at a volume peak held against a large surge in volume, so traders expect it to hold.",
                ),
                Q(
                    stem="Volume decreases across a support as price touches it and turns. The book says this tends to see:",
                    options=("Price driven away with bullish confirmation",
                             "Not enough information to say",
                             "The strongest possible barrier",
                             "A retest of the barrier, or even a penetration"),
                    answer="D",
                    reason="Decreasing volume across support or resistance tends to see a retest, and in extreme cases a penetration.",
                ),
            ),
        ),
        Pair(
            origin="Book pp.188-189: the four are the book's, from among numerous ways. Prior volume peaks: named on p.188 only. The chart is ours, on invented volume.",
            left=Content(
                title="Filtering volume action: four ways",
                lines=(
                    "Filtering picks out the most significant volume: what may lead to a top or bottom.",
                    "Four of the book's numerous ways: 1 a moving average filter, which it calls the smoothed volume filter, 2 a volatility filter, 3 prior volume peaks, 4 volume cycles.",
                    "1 and 2 are worked next. 3 is named and never explained. 4 comes in Part 5.",
                ),
                accent="Gold: the volume each filter keeps.",
                caption="Panel 3 is our reading, not examinable: like Part 2's upper overextended volume level, set at earlier climax volume.",
            ),
            picture=Chart(
                letter="S",
                shows="Four small sketches of invented volume in millions of shares, one per filter, the volume each keeps in gold. 1: an average line near 1 million, with two spikes of 3.0 and 2.8 above it. 2: a line set higher still, crossed only by a bar of 3.2. 3, our reading: a level drawn at an earlier peak of 2.6, reached again later. 4: volume that rises and falls in a repeating cycle, its peaks marked.",
            ),
            text_w=CHART_W,
            notes=(
                "This answers review question 5, the modes of volume filtering. Four ways, and the book explains two of them in this passage: the smoothed volume filter, then the two- or three-sigma filter.",
                "Prior volume peaks: the book names them on p.188 and never explains them. Part 2's upper overextended volume level was set at the volume of earlier climaxes, which is the nearest the book comes; that reading is ours and is not examinable.",
            ),
        ),
        Pair(
            origin="Book pp.188-189: a spike above the line is significant; no measure of how far. Ours: the volume, the 8 bars, the twice rule and filter 2's stand-in line.",
            left=Content(
                title="Filters 1 and 2 in numbers",
                lines=(
                    "Ours, filter 1: the line is the average of the last 8 bars, about 1 million.",
                    "How far above counts? The book gives no measure. Our rule: over twice the average.",
                    "1.4 million is just over the line: ordinary. The 3.0 and 2.8 million spikes: kept.",
                    "Filter 2: only the 3.2 bar crosses its higher line; the 1.9 bar is dropped.",
                ),
                accent="Filter 1 is the book's smoothed volume filter: next.",
            ),
            picture=Chart(
                letter="SA",
                shows="Two strips of invented volume in millions of shares. Filter 1: the average of the last 8 bars as a solid line and twice that average as a dotted gold line; a bar of 1.4 sits just over the average and is not kept, and the spikes of 3.0 and 2.8 rise over the dotted line, in gold. Filter 2: a higher line crossed only by the bar of 3.2, in gold; a bar of 1.9 stays under it.",
            ),
            text_w=CHART_W,
            notes=(
                "The twice rule is ours, to make the reading concrete. The book says only that a spike above the line is significant, and its own Figure 6.20 marks only the tallest spikes.",
                "Filter 2's line here is a stand-in, the average plus a fixed amount. The real line, the two- or three-sigma filter, is computed on its own slides after the smoothed volume filter.",
            ),
        ),
        Pair(
            origin="Book p.188. The chart is ours, on invented volume; its line is a 20-bar simple average of volume we computed.",
            left=Term(
                term="Smoothed volume filter",
                plain="An average of recent volume, drawn over the volume bars. A spike well above it stands out.",
                example="Our chart: each point is the average of the last 20 volume bars. Four spikes stand well above it.",
                formal="A smoothed volume filter is simply a moving average based on volume, instead of price. Volume spiking above this overextended moving average line is considered significant, and may lead to a top or bottom.",
            ),
            picture=Chart(
                letter="T",
                shows="An invented price over its volume, with a 20-bar average of volume drawn as a line across the volume panel. Four volume spikes stand far above the line, in gold, and dashed lines run up from each to a top or a bottom in price, numbered 1 to 4.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "A moving average is met again: Chapters 4 and 5 used them, Chapter 11 teaches them. Here it is an average of volume, not of price.",
                "The book says a spike above the line is significant and gives no measure of how far above. On its own Figure 6.20 the arrows mark only the tallest spikes, and so does this chart.",
            ),
        ),
        Pair(
            origin="Book pp.188-189 and Figure 6.20.",
            left=Content(
                title="Choosing the average's length",
                lines=(
                    "The average [1] is the smoothed volume filter of the term slide, over the last N bars. N, the lookback, is how many bars go into it.",
                    "Short N, 5 bars say: hugs the bars closely, ordinary ones cross it too, many false signals.",
                    "Long N, 100 bars say: slow and flat, only huge spikes cross it, few signals, some turns missed.",
                ),
                accent="The right N sits in between. How to find it: next slide.",
                caption="Figure 6.20: each dotted arrow runs from a spike crossing the line [2] up to a top or a bottom [3].",
            ),
            picture=Figure(
                number="6.20",
                shows="The daily USDJPY chart with a smoothed volume line across its volume panel, labelled moving average overextension threshold. Dotted arrows rise from the overextensions in volume to tops and bottoms in price.",
                aspect=1.837,
                marks=(
                    Mark(1, "line", 0.02, 0.885, 0.82, 0.885, at=(0.02, 0.885)),
                    Mark(2, "box", 0.245, 0.76, 0.29, 0.90, at=(0.33, 0.74)),
                    Mark(3, "circle", 0.235, 0.33, 0.295, 0.47),
                ),
            ),
            text_w=6.0,
            notes=(
                "Lookback is the number of bars averaged. A longer one smooths more.",
                "Follow two or three of the dotted arrows from a spike to a turn in price.",
            ),
        ),
        Content(
            origin="Book pp.188-189. Ours: the worked cycle number and the actionable backtest description.",
            title="Choosing the length, continued",
            lines=(
                "Backtest: run the filter on past prices with a few different N, and see which one actually caught the real tops and bottoms. Keep that N.",
                "Rule of thumb: set N to the dominant trading cycle period, or half of it. Ours, invented: swings about 40 bars peak to peak give N = 40, or N = 20.",
                "The book gives no fixed N. Not that any N works: the right N is found for each market, by backtest or by this rule of thumb.",
            ),
            accent="No universal lookback. A method for finding one, for this market.",
            notes=(
                "This slide has no picture: it works through the book's two rules of thumb, not a new reading of a chart. Figure 6.20 was the last slide's.",
                "Walk the backtest sentence slowly: try N = 10, 20 and 50 on last year's chart, and see which flagged the real turns.",
            ),
        ),
        Pair(
            origin="Book p.189. Chart: ours, computed; divisor and window read from build/charts_chapter06.py, not guessed.",
            left=Term(
                term="Two- or three-sigma volume filter",
                plain="Sigma, the standard deviation: how far volume typically strays from its mean over the same N bars. The line: mean + k x sigma, k = 3 here, or 2.",
                example="Ours: 20 bars average 10 million, sigma 2 million. 3-sigma line: 10 + 3 x 2 = 16 million; 12 million stays under, 18 million crosses. 2-sigma, 14 million, flags more.",
                formal="A 2- or 3-sigma filter, a volatility filter, keeps only the most significant surges: the upper Bollinger Band of volume, k standard deviations above its average.",
            ),
            picture=Chart(
                letter="U",
                shows="An invented volume record with two lines across it: the 20-bar average volume, and above it a three-sigma line, the average plus three standard deviations. Only three bars cross the upper line, in gold.",
            ),
            text_w=7.4,
            notes=(
                "Sigma is the Greek letter for a standard deviation: how far values typically spread from their average.",
                "Bollinger Bands were named in Chapter 1, in the mean reverting approach, and are not explained there either. All this filter needs is the upper line.",
                "Three sigma is stricter than two: fewer bars cross it.",
            ),
        ),
        Pair(
            origin="Book p.189 gives only the words. Ours: how build/charts_chapter06.py actually computes it, read from the code, not guessed.",
            left=Content(
                title="How the dotted line is drawn, bar by bar",
                lines=(
                    "At each bar: take its last 20 volume bars, this one included. Mean, then sigma. Plot mean + 3 x sigma. Move forward one bar, repeat.",
                    "That is why it jumps, at 1: a spike entering the window raises both at once, so the line leaps up. It stays high until the spike leaves 20 bars later, at 2.",
                ),
                accent="Recomputed from nothing at every bar: no memory beyond its window.",
            ),
            picture=Chart(
                letter="HU",
                shows="The invented volume record of the three-sigma term slide, its 20-bar average and its dotted three-sigma line. At 1, bar 24, a spike enters the last 20 bars and the dotted line jumps; at 2, bar 44, twenty bars later, the spike leaves and the line falls back.",
            ),
            text_w=6.0,
            notes=(
                "Point at 1, where the line leaps as the spike comes in, then count along twenty bars to 2, where it drops as the spike goes out.",
            ),
        ),
        Content(
            origin="Book p.189 gives only the words. Ours: how build/charts_chapter06.py computes the line, read from the code.",
            title="Two things the book leaves open",
            lines=(
                "The book never says if sigma divides by 20 or by 19.",
                "Nor does it say if the bar sits in its own window of 20.",
                "Our code divides by 20 and includes the bar.",
            ),
            accent="The method is the book's; these two choices are ours.",
            notes=(
                "This closes the two gaps the review found: the divisor and the window. Both are read straight from the code that drew the chart.",
                "No picture: nothing here is read off a chart.",
            ),
        ),
        Pair(
            origin="Book p.189 and Figure 6.21. Ours: the April top, read off the figure.",
            left=Content(
                title="A three-sigma filter on USDJPY",
                lines=(
                    "Daily USDJPY with a three-sigma filter on its volume. Three surges cross the line; the book marks each with an arrow up to price [1] [2] [3].",
                    "Stricter than the smoothed filter, this line skips the April 2011 top [4], the highest price on the chart.",
                ),
                accent="The book: such surges tend to come at the most significant tops and bottoms.",
            ),
            picture=Figure(
                number="6.21",
                shows="The daily USDJPY chart with a stepped line across its volume panel labelled 3-sigma volume overextension threshold, and dotted arrows from the three overextensions in volume above it up to turns in price; the April 2011 top has no arrow.",
                aspect=1.657,
                marks=(
                    Mark(1, "circle", 0.295, 0.40, 0.355, 0.64),
                    Mark(2, "circle", 0.615, 0.50, 0.675, 0.64),
                    Mark(3, "circle", 0.81, 0.58, 0.87, 0.71),
                    Mark(4, "circle", 0.345, 0.0, 0.405, 0.13, at=(0.405, 0.065)),
                ),
            ),
            text_w=5.0,
            notes=(
                "Follow each of the three arrows down to the surge under it: marks 1, 2 and 3 ring where they reach price. Then find the April 2011 top, mark 4: a dotted upright, and no arrow.",
                "The smoothed filter on the same market, Figure 6.20, marked six; this stricter line marks three.",
            ),
        ),
        Pair(
            origin="Book p.189 and Figure 6.21, its volume panel. Ours: what the lines do, read off the figure.",
            left=Content(
                title="The three-sigma line, close up",
                lines=(
                    "Stepped line [1]: the three-sigma filter, drawn over the volume bars.",
                    "Three surges cross it [2] [3] [4], each under an arrow up to price.",
                    "It stays high for months after the March spike [2], far beyond our 20 bars. The book never gives its N.",
                    "The two lower lines [5] [6] are drawn and not named by the book; only the top one is the filter.",
                ),
            ),
            picture=Figure(
                number="6.21",
                shows="The volume panel of the daily USDJPY chart, drawn larger: the stepped 3-sigma volume overextension threshold over the volume bars, the three surges that cross it, and two lower lines the book does not name.",
                aspect=1.657,
                crop=(0.28, 0.66, 0.10, 0.01),
                marks=(
                    Mark(1, "line", 0.089, 0.521, 0.726, 0.521, at=(0.16, 0.40)),
                    Mark(2, "circle", 0.032, 0.303, 0.113, 0.727),
                    Mark(3, "circle", 0.548, 0.303, 0.629, 0.727, at=(0.588, 0.07)),
                    Mark(4, "circle", 0.863, 0.303, 0.944, 0.727, at=(0.903, 0.07)),
                    Mark(5, "line", 0.194, 0.742, 0.968, 0.742, at=(0.968, 0.742)),
                    Mark(6, "line", 0.194, 0.894, 0.968, 0.894, color="green",
                         at=(0.194, 0.894)),
                ),
            ),
            text_w=4.4,
            notes=(
                "Point at mark 1, the stepped line, and follow it from the March spike, mark 2: it stays up for months, then steps.",
                "Marks 5 and 6 are the two lines under it. The book draws them and never says what they are.",
            ),
        ),
        Content(
            origin="Book p.189. It names the oscillator and does not describe it.",
            title="Why the book draws the line on the bars",
            lines=(
                "The book also names a standard deviation oscillator: an indicator in its own panel (Part 1). It does not describe or draw one.",
                "It is less useful, the book says, because it gives no overlay: a line drawn over the volume bars themselves, so a bar can be seen crossing it.",
            ),
            accent="What to do: pick N as for the smoothed filter, and draw the 3-sigma line over the bars; a bar above it may mark a top or bottom.",
            notes=(
                "No picture: this slide reads the book's one sentence on the oscillator, not a chart. The overlay it praises is the line on the last slide.",
                "Oscillator is Part 1's word: an indicator in a panel under price.",
            ),
        ),
        Check(
            label="Filtering volume",
            questions=(
                Q(
                    stem="A smoothed volume filter is:",
                    options=("A Bollinger Band on price",
                             "A moving average based on volume, instead of price",
                             "The lowest historical volume level",
                             "A count of trades"),
                    answer="B",
                    reason="The book: a smoothed volume filter is simply a moving average based on volume, instead of price.",
                ),
                Q(
                    stem="In a two- or three-sigma volume filter, which part of the Bollinger Band is used?",
                    options=("The lower band only",
                             "Both bands",
                             "The upper band only",
                             "The middle line only"),
                    answer="C",
                    reason="Only the Bollinger upper band is used: the filter keeps the most significant surges.",
                ),
            ),
        ),
        Pair(
            origin="Book p.189. Inflection point: Chapter 5. The chart is ours, invented.",
            left=Term(
                term="Volume filtered inflection points",
                plain="Only peaks and troughs (Chapter 5's inflection points) that came on heavy volume are used to draw lines.",
                example="Ours, in millions: 1, 2, 3 came on 3.0, above our 2.5 line. Seven grey turns came on 1.0: dropped.",
                formal="Many practitioners use only peaks and troughs that are considered significant, that is, associated with above average volume, to construct trendlines and channels.",
            ),
            picture=Chart(
                letter="V",
                shows="An invented price over its volume, every peak and trough dotted. Turns 1, 2 and 3, at PHP 52.00, 56.00 and 49.00, came on 3.0 million, above a threshold of 2.5 drawn by eye, and are gold; the seven grey turns came on 1.0, below the 1.3 average.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Trendlines and channels were Chapter 5, and so were inflection points. This adds one rule for which points to use: only the heavily traded ones.",
                "The grey turns are real peaks and troughs too. They are skipped because too little traded at them.",
            ),
        ),
        Pair(
            origin="Ours: the steps and every number, invented. The method and both rules for the threshold are the book's, p.189.",
            left=Content(
                title="Drawing a volume filtered channel, step by step",
                lines=(
                    "Step 1. Mark every peak and trough.",
                    "Step 2. The book's rule: above average volume, 1.3 here. Its example draws a higher line by eye, and it never says which governs. Ours: 2.5. Only 1, 2, 3 reach it.",
                    "Step 3. Join peaks 1 (bar 22, PHP 52.00) and 2 (bar 62, PHP 56.00): PHP 4.00 in 40 bars, 0.10 a bar.",
                    "Step 4. The same slope through trough 3 (bar 44, PHP 49.00): the channel.",
                ),
            ),
            picture=Chart(
                letter="VA",
                shows="The same invented price and volume, with bar numbers on the time axis. A solid line joins peak 1, bar 22, PHP 52.00, and peak 2, bar 62, PHP 56.00, rising PHP 4.00 in 40 bars, measured on the chart; a dashed parallel runs through trough 3, bar 44, PHP 49.00. Price comes back to the dashed line at X, bar 72, PHP 51.80. Only the three gold volume bars reach the 2.5 threshold.",
            ),
            text_w=CHART_W,
            notes=(
                "Read the steps against the chart: each bar number and price is printed on it.",
                "A turn on 2.0 million would pass the book's definition and fail its example's line. The book does not settle that, and neither do we: our chart has no turn in between.",
            ),
        ),
        Pair(
            origin="Book p.189 and Figure 6.22.",
            left=Content(
                title="A channel from filtered points: silver",
                lines=(
                    "The book's example: daily silver, with tick volume, the number of trades (Part 4).",
                    "A threshold drawn by visual inspection [1], so only the most significant peaks reach it. The oval [2] rings July to August.",
                    "Two arrows: under Points 1 and 3, days apart, and under 2. Trendline 1 to 2, parallel from 3.",
                ),
                accent="At X [3] price bounces off the lower line, a short-term buy, then falls through it [4].",
            ),
            picture=Figure(
                number="6.22",
                shows="The daily silver chart, XAGUSD, with a tick volume overextension threshold across its volume panel. Arrows rise from the circled tick volume peaks to points 1, 2 and 3; a channel is drawn from 1 and 2 with a parallel from 3, and price reacts at X.",
                aspect=1.994,
                marks=(
                    Mark(1, "line", 0.10, 0.902, 0.97, 0.902),
                    Mark(2, "box", 0.495, 0.79, 0.615, 0.93),
                    Mark(3, "circle", 0.555, 0.40, 0.62, 0.53, at=(0.52, 0.47)),
                    Mark(4, "arrow", 0.64, 0.40, 0.655, 0.72, at=(0.70, 0.56)),
                ),
            ),
            text_w=5.6,
            notes=(
                "Follow the two arrows from the oval up to points 1 and 3, then 2. Those are the only points used.",
                "Falls through it: the book says the market reversed downward, violating the rising channel.",
            ),
        ),
        Pair(
            origin="Book pp.189-190. Ours: the channel, its numbers and the arithmetic at X, on the step by step chart's invented prices.",
            left=Content(
                title="What the channel is for: the lower line at X",
                lines=(
                    "Ours: the lower line rises at the slope of peaks 1 to 2: PHP 4.00 in 40 bars, 0.10 a bar.",
                    "X is bar 72, 28 bars after trough 3 at bar 44, shaded. The lower line is there at 49.00 + 28 x 0.10 = PHP 51.80; price touches it and turns up.",
                ),
                accent="What to do: at the lower line, look for a short-term buy. Falling through it violates the channel, the book's word.",
                caption="Chapter 5's uptrend line joined troughs; here the book joins two peaks, 1 and 2, and gives no reason.",
            ),
            picture=Chart(
                letter="HV",
                shows="The invented channel of the step by step chart: a solid line through peaks 1 and 2 and a dashed parallel through trough 3, bar 44, PHP 49.00, rising PHP 0.10 a bar. The 28 bars from trough 3 to X are shaded, and at X, bar 72, price touches the dashed line at 49.00 + 28 x 0.10 = PHP 51.80.",
            ),
            text_w=6.0,
            notes=(
                "Count along the shaded stretch: trough 3 at bar 44 to X at bar 72 is 28 bars, and 28 times 0.10 is 2.80 on top of 49.00.",
                "The buy at the lower line is the book's reading of silver's X on the last slide's figure; here it is worked on our own numbers.",
            ),
        ),
        Pair(
            origin="Book pp.189-190 and Figure 6.22. Ours: what the figure's volume panel shows that the text does not explain.",
            left=Content(
                title="What Figure 6.22 leaves open",
                lines=(
                    "The channel uses only the July to August peaks in tick volume [4], under the arrows to Points 1, 2 and 3.",
                    "Yet silver's April bars [5], at the line labelled High tick volume level, and late September bars [6], reach the threshold too; the book does not say why it skips them.",
                ),
                accent="Use heavily traded turns; which of them is left to the eye.",
            ),
            picture=Figure(
                number="6.22",
                shows="The daily silver chart, XAGUSD, with its tick volume overextension threshold. The July to August tick volume peaks are ringed under Points 1, 2 and 3; the April bars, at the line labelled high tick volume level, and the late September bars also reach the threshold and are not used.",
                aspect=1.994,
                crop=(0.15, 0.55, 0.20, 0.03),
                marks=(
                    Mark(4, "box", 0.531, 0.571, 0.715, 0.905, color="gold"),
                    Mark(5, "box", 0.162, 0.69, 0.285, 0.905, color="red",
                         at=(0.323, 0.548)),
                    Mark(6, "box", 0.761, 0.69, 0.884, 0.905, color="blue"),
                ),
            ),
            text_w=4.6,
            notes=(
                "Point at mark 4, the ringed July to August bars, then at marks 5 and 6: both reach the threshold, and neither is used. The marks start at 4 so they are not taken for the figure's own Points 1 to 3.",
                "Why only heavily traded turns? The book says only that it shows the importance of significant inflection points; the next figure's slide quotes it. Part 3's first rule, a barrier formed at a volume peak is the most reliable, fits, and that link is ours.",
            ),
        ),
        Pair(
            origin="Book pp.189-190 and Figure 6.23. Candlestick and valid: Chapters 3 and 5.",
            left=Content(
                title="More channels from filtered points",
                lines=(
                    "Points numbered afresh. Ovals ring heavy volume under 1, under 3 and 2, under 5 and 6.",
                    "Trendline 1 to 2, parallel from 3: a large bearish candlestick, closing far below its open, breaks it [7].",
                    "A parallel from 4, carried back, meets the trough at X [8], January 2011: valid, the book says, with no third touch (Chapter 5).",
                    "Parallels from 5 and 6: a new channel [9].",
                ),
                accent="Every line runs parallel to 1 to 2.",
            ),
            picture=Figure(
                number="6.23",
                shows="The same silver chart with more volume filtered points, numbered 1 to 6 and X. Several parallel rising lines are drawn through them, each from a point that came on overextended volume, forming channels that contain price.",
                aspect=1.982,
                marks=(
                    Mark(7, "circle", 0.62, 0.36, 0.675, 0.64, color="gold"),
                    Mark(8, "line", 0.105, 0.925, 0.45, 0.66, color="red",
                         at=(0.12, 0.72)),
                    Mark(9, "box", 0.645, 0.56, 0.85, 0.92, color="blue",
                         at=(0.75, 0.56)),
                ),
            ),
            text_w=5.6,
            notes=(
                "Count the parallels: five lines, every one at the slope of the line from 1 to 2.",
                "The book admits the line through X was found looking back. It still calls the channel valid.",
            ),
        ),
        Pair(
            origin="Book pp.189-190 and Figure 6.23. Angular symmetry: Chapter 5. Ours: what the figure rings and what it does not.",
            left=Content(
                title="What Figure 6.23 shows, and two things it leaves open",
                lines=(
                    "Every line has the slope of trendline 1 to 2 [7]: one steady angle, the book's near perfect angular symmetry (Chapter 5).",
                    "The 5 and 6 channel [8]: resistance at its top, support at its bottom.",
                    "Open: the text says USDJPY; the chart, silver.",
                    "Open: no heavy volume is ringed under 4 [9] or X, yet both anchor lines.",
                ),
                accent="Build lines on heavily traded turns; watch the parallels for resistance and support.",
            ),
            picture=Figure(
                number="6.23",
                shows="The same silver chart with volume filtered points 1 to 6 and X. Every line runs parallel to the trendline from 1 to 2; the last channel runs from 5 and 6; the volume panel rings heavy volume under 1, under 3 and 2, and under 5 and 6, and nothing under 4 or X.",
                aspect=1.982,
                marks=(
                    Mark(7, "line", 0.345, 0.425, 0.66, 0.185, color="gold",
                         at=(0.50, 0.22)),
                    Mark(8, "box", 0.645, 0.56, 0.85, 0.92, color="red"),
                    Mark(9, "box", 0.40, 0.84, 0.50, 0.93, color="blue",
                         at=(0.40, 0.84)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Point at mark 7, the line from 1 to 2, and lay a ruler along it: every other line has its angle. The marks start at 7 so they are not taken for the figure's own points 1 to 6.",
                "Then mark 8, the channel from 5 and 6, and mark 9: no oval under 4, and none under X at the far left either, though each anchors a line.",
            ),
        ),
        Check(
            label="Filtered inflection points",
            questions=(
                Q(
                    stem="Which peaks and troughs are used to construct volume filtered trendlines and channels?",
                    options=("Every peak and trough on the chart",
                             "Only those associated with above average volume",
                             "Only those formed on minimal volume",
                             "Only those within a consolidation"),
                    answer="B",
                    reason="Only significant inflection points are used: those associated with above average volume.",
                ),
                Q(
                    stem="On Figure 6.22, how is the volume threshold drawn?",
                    options=("By visual inspection, so only the most significant peaks reach it",
                             "As a 100-day moving average",
                             "At three standard deviations",
                             "At the lowest historical volume"),
                    answer="A",
                    reason="The book draws a simple tick volume overextension level [1] by visual inspection.",
                ),
            ),
            picture=Figure(
                number="6.22",
                shows="The daily silver chart, XAGUSD, with a tick volume overextension threshold drawn across its volume panel by eye; the tick volume peaks that reach it are ringed under points 1, 2 and 3.",
                aspect=1.994,
                crop=(0.30, 0.70, 0.03, 0.02),
                marks=(
                    Mark(1, "line", 0.03, 0.721, 0.97, 0.721),
                ),
            ),
            layout="top",
        ),
    ),
)

# ==========================================================================
# Part 4 - 6.1, pp.190 to 197: relative and absolute volume, distortions,
# open interest, tick volume, breadth volume and the TRIN, and volume by
# price against volume by time.
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="The Mechanics of Volume Action: Relative Volume, Open Interest and Breadth",
    short="6.1 Open interest",
    minutes="",
    covers=(),
    slides=(
        Pair(
            origin="Book pp.190-191. It never defines the two names; these readings are ours, from its contrast. The share counts and the chart are ours, on invented prices.",
            left=Content(
                title="6.1  Relative and absolute volume",
                lines=(
                    "Absolute volume is the raw count: today, 3 million shares traded.",
                    "Relative volume compares it with its own past: 3 million against a usual 1.5 million is double.",
                    "The book: absolute volume is not as important as relative. The change in volume tells the most about price.",
                ),
                accent="Yet a trend can persist for long periods on flat volume.",
            ),
            picture=Chart(
                letter="W",
                shows="An invented share that rises steadily for the whole chart while its volume stays flat, every bar about 2 million shares, labelled no change in volume, and the trend persists anyway.",
            ),
            text_w=CHART_W,
            notes=(
                "Work the double out loud: 3 million today, 1.5 million usually, so twice the usual. That comparison is relative volume.",
                "This is review question 7, which is more useful. The book's answer: relative, for reading trends; absolute has the uses two slides on.",
                "The chart is the warning in the gold line: no change in volume, and the trend goes on anyway.",
            ),
        ),
        Content(
            origin="Book p.191. The share counts in the example are ours.",
            title="What the change in volume tells",
            lines=(
                "Rising and falling volume show interest at each price. Part 1's tests: rising is confirmation, falling divergence; with price bullish, against bearish.",
                "Past extremes, Part 2's overextended levels, are a reference. Ours: busiest day 9 million, quietest 0.4 million; volume reaching either again warns of a top or bottom.",
                "Flat volume is no sign a trend is ending; the book gives no rule for it.",
            ),
            accent="Read the change in volume for the trend, and past extremes for the turns.",
            notes=(
                "This slide has no picture: it ties the book's two sentences to Parts 1 and 2, which drew them.",
                "Peaks and troughs both count: the book says historical volume peaks and troughs give the reference level.",
            ),
        ),
        Pair(
            origin="Book p.191 names the bias. The pesos, the share and the chart are ours, on invented prices.",
            left=Term(
                term="Loss aversion bias",
                plain="Holding a losing position, not selling at a loss, hoping it comes back. Holding is not trading: it adds no volume.",
                example="Bought at PHP 50, now PHP 38: an unrealized loss of PHP 12, on paper only, unsold. You hold for breakeven, PHP 50.",
                formal="Many investors hold on to losing positions in a falling market, hoping they rebound to breakeven or profitability, believing unrealized losses are not real losses: loss aversion bias.",
            ),
            picture=Chart(
                letter="X",
                shows="An invented share falling from 50 to 38 pesos, with a dashed line at the 50 peso entry price labelled bought here. A label on the fall says holders wait for breakeven instead of selling, and the volume bars under the fall shrink.",
            ),
            text_w=7.4,
            notes=(
                "Chapter 1 listed loss aversion among behavioral biases in one line. This is the first slide that says what it is.",
                "The book says many investors treat a paper loss as no loss, and so they hold. Breakeven is the price at which you neither gain nor lose.",
                "Why it is in a chapter on volume: holding is not trading, so a bear market trades less. That is the next slide.",
            ),
        ),
        Pair(
            origin="Book p.191: its three reasons, nearly word for word. The chart and its share counts are ours, on invented prices.",
            left=Content(
                title="Bull market volume outweighs bear market volume",
                lines=(
                    "1  Loss aversion: losing positions held in a falling, bear market add nothing to its trading.",
                    "2  In a rising, bull market, traders can fund new positions with house money: profit already made.",
                    "3  More investment funds market their services in a bull market, drawing in investors.",
                ),
                accent="So bull market volume tends to outweigh bear market volume. Ours: 2.8 million shares a day rising, 1.3 million falling.",
                caption="A few of the book's reasons; it draws no trading rule from them.",
            ),
            picture=Chart(
                letter="Y",
                shows="An invented share that rises for half the chart and falls for the other half. The volume bars under the rise average about 2.8 million shares a day, those under the fall about 1.3 million, labelled bull market volume and bear market volume.",
            ),
            text_w=6.0,
            notes=(
                "The book says a variety of reasons, a few being these three. They are its list, not a complete one.",
                "House money is the book's phrase for profit already made, spent again.",
            ),
        ),
        Pair(
            origin="Book p.191. The two shares, their volumes and their shares outstanding are ours: a share-count example of turnover.",
            left=Content(
                title="What absolute volume is good for",
                lines=(
                    "1  Price rejection levels, Chapter 3: prices the market was pushed back from. The book gives no method.",
                    "2  Comparing participation in stocks, sectors or commodities, seeking liquidity: the book's word, not defined.",
                    "3  Turnover: shares traded / shares outstanding, all the company's shares. A: 5m / 2,000m = 0.25%. B: 1m / 40m = 2.5%.",
                ),
                accent="A trades five times the shares; B has ten times the participation.",
            ),
            picture=Chart(
                letter="Z",
                shows="Two invented shares compared. Share A trades 5 million shares a day of 2,000 million outstanding, a turnover of 0.25 percent. Share B trades 1 million of 40 million outstanding, 2.5 percent. A trades more shares; B has ten times the participation.",
            ),
            text_w=6.6,
            notes=(
                "Absolute volume is the raw count of the first slide of this part. Work the turnover out loud: 5 million of 2,000 million is a quarter of one percent; 1 million of 40 million is two and a half percent.",
                "Liquidity is the book's word, used here and not defined in this chapter. Do not define it for them.",
            ),
        ),
        Content(
            origin="Book p.192. Chapter 1 named arbitrage, program trading and HFT. The share counts in the example are ours.",
            title="Volume distortions",
            lines=(
                "A surge in arbitrage, program trading and high frequency trading (HFT) may distort volume's traditional meaning: traders' interest in a rise or fall.",
                "Chapter 1: program trading is machines trading in ways humans cannot replicate. Chapter 1 named arbitrage and HFT without defining them; so does this chapter.",
                "Ours: a day trades 4 million shares, 3 million of them program trades. The bar reads 4 million; traders taking part in the move traded 1 million.",
            ),
            accent="So a volume bar may count machine trades as well as interest: here only 1 of 4 million. The book gives no way to separate them.",
            notes=(
                "The book gives two sentences and no figure, so this slide has no picture.",
                "The example is ours and only shows the size of the problem: the bar counts every share, whoever traded it.",
            ),
        ),
        Check(
            label="Relative and absolute volume",
            questions=(
                Q(
                    stem="According to the book, which gives the most information about potential price action?",
                    options=("Absolute volume",
                             "The change in volume",
                             "Turnover against shares outstanding",
                             "Tick volume"),
                    answer="B",
                    reason="Absolute volume is not as important as relative volume: it is the change in volume that gives the most information.",
                ),
                Q(
                    stem="An investor holds a losing share, believing an unrealized loss is not a real loss. The book calls this:",
                    options=("House money",
                             "A low volume reversal",
                             "A volume distortion",
                             "Loss aversion bias"),
                    answer="D",
                    reason="Holding losing positions in hope of breakeven, treating unrealized losses as not real, is loss aversion bias.",
                ),
            ),
        ),
        Pair(
            origin="Book p.192 gives the definition and the three rules. The traders and contract counts are ours.",
            left=Term(
                term="Open interest",
                plain="Every futures or options contract has a buyer, the long, and a seller, the short. Open interest counts the contracts still open.",
                example="Plus 1 when a new long and short both open; minus 1 when both close; no change when one side is replaced.",
                formal="The total amount of outstanding contracts in the futures and options markets. It increases when a new long and short are initiated, decreases when both exit, and is unchanged when one is replaced.",
            ),
            picture=Chart(
                letter="AA",
                shows="Open interest over four days, drawn as columns of 1, 3, 3 and 1 contracts, each labelled with what happened: day 1 a new long and a new short, plus 1; day 2 the same for 2 contracts, plus 2; day 3 one side replaced by a new trader, no change; day 4 both sides exit, minus 2.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Chapter 3 listed open interest as transaction data and Chapter 4 used it in a consolidation. This is the first slide that defines it.",
                "Each contract is one long and one short, so a contract is open until both sides are out. Long and short are Chapter 1's go long and go short.",
                "The chart is the next slide's four days, one column a day. Read its labels against the three rules in the example row.",
            ),
        ),
        Pair(
            origin="Book p.192: the rules, and why count: unlike stocks, futures and options contracts expire. Traders and counts: ours.",
            left=Content(
                title="Open interest, day by day",
                lines=(
                    "Day 1: A buys 1 from B, both new, A long and B short: plus 1. Open interest 1.",
                    "Day 2: C buys 2 from D, both new: plus 2. Open interest 3.",
                    "Day 3: A sells that 1 to E, the new long; B is still short: no change. Still 3.",
                    "Day 4: D buys back 2 from C: D's short and C's long close: minus 2. Now 1.",
                ),
                accent="Only both sides opening, or both closing, moves the count.",
            ),
            picture=Chart(
                letter="HA",
                shows="Open interest over the slide's four days, one column a day: 1, 3, 3 and 1 contracts. Under each, what the day did to the count: day 1 new, plus 1; day 2 new, plus 2; day 3 one side replaced, no change, in gold; day 4 closed, minus 2.",
            ),
            text_w=5.6,
            notes=(
                "Read each day's line, then its column: the label under the column is the line's rule.",
                "On day 4, D buying back is covering and C selling is liquidating: Chapter 1's words for closing a short and a long.",
            ),
        ),
        Pair(
            origin="Book p.192: the reading and its reasons are the book's. The chart is ours: arrows, not prices.",
            left=Content(
                title="Open interest is read like volume",
                lines=(
                    "Like volume, open interest shows interest in seeing price rise or fall. With price: bullish. Against: bearish.",
                    "Price rising. Both rising: bullish, buying pressure. Both falling: bearish, shorts covering (buying back) and longs leaving.",
                    "Price falling. Both rising: bearish, short selling. Both falling: bullish, fewer longs liquidating, fewer new shorts.",
                ),
                accent="Rising is confirmation, falling is divergence: as for non-price-based volume.",
            ),
            picture=Chart(
                letter="AB",
                shows="Four small cases, each with arrows for price, volume and open interest. All three rising: bullish, buying pressure. Price rising with volume and open interest falling: bearish, shorts covering and longs leaving. Price falling with the other two rising: bearish, short selling. All three falling: bullish, less liquidation and short selling.",
            ),
            text_w=7.0,
            notes=(
                "The same rule as Part 1's bullish and bearish volume, with open interest moving alongside volume. Both words, both rules: the book says open interest divergence is read as for non-price-based volume oscillators.",
                "The book's reason for the last case: participants are less interested in seeing the market decline further.",
                "This is review question 6, the relationship between volume, open interest and price.",
            ),
        ),
        Pair(
            origin="Book p.192 gives the four readings and their reasons. The contract, its prices and its counts are ours, invented.",
            left=Content(
                title="The four readings, worked",
                lines=(
                    "1  Ours: a futures contract rises, PHP 100 to 110. Open interest 50,000 to 60,000, volume 8,000 to 12,000 a day: bullish confirmation, buying pressure.",
                    "2  Same rise; open interest 50,000 to 40,000, volume 8,000 to 5,000: bearish divergence, shorts covering, longs leaving.",
                    "Falling, PHP 110 to 100: 3, both rising, bearish confirmation, short selling; 4, both falling, bullish divergence.",
                ),
                accent="Same price move, opposite readings: volume and open interest decide.",
            ),
            picture=Chart(
                letter="HB",
                shows="The four cases as arrows for price, volume and open interest, numbered as the slide numbers them. 1 all three rising, open interest 50,000 to 60,000 and volume 8,000 to 12,000. 2 price up, the other two down, open interest 50,000 to 40,000 and volume 8,000 to 5,000. 3 price down, the other two up: bearish confirmation. 4 all three falling: bullish divergence.",
            ),
            text_w=7.4,
            notes=(
                "This slide puts numbers on the four sketches of the last slide. The names are Part 1's: bullish or bearish, confirmation or divergence.",
                "Ask the room to name the case before you read the answer: price up, open interest down, volume down.",
            ),
        ),
        Pair(
            origin="Book p.192 and Figure 6.24; the prices are read off the figure by eye. Go long, liquidate, go short and cover are Chapter 1 terms.",
            left=Content(
                title="What a trader does with the four",
                lines=(
                    "All three rising, bullish: look for buy signals.",
                    "Price rising, open interest and volume falling, bearish: look to exit, liquidating (selling) your longs.",
                    "Price falling, both rising, bearish: look to go short. Once both start to fall together, bullish: rapidly cover (buy back) all shorts.",
                ),
                accent="Figure 6.24, silver: from A, about $20, price rose to B, about $49 [1], then fell to under $30 [2]. Which of the four was it at B? Next slide.",
            ),
            picture=Figure(
                number="6.24",
                shows="The price panel of the continuous daily chart of silver: from A, about $20 in 2008, price rises to B, about $49 in 2011, then falls to under $30.",
                aspect=0.784,
                crop=(0.34, 0.0, 0.0, 0.50),
                marks=(
                    Mark(1, "arrow", 0.098, 0.8, 0.644, 0.09, at=(0.08, 0.64)),
                    Mark(2, "arrow", 0.674, 0.12, 0.795, 0.58, at=(0.80, 0.255)),
                ),
            ),
            text_w=7.4,
            notes=(
                "The four actions are the four cases of the last slide, turned into what to do.",
                "Mark 1 is the rise from A to B; mark 2 the fall after it. The next slide reads the two panels under this one at B.",
            ),
        ),
        Pair(
            origin="Book p.192 and Figure 6.24; the prices are read off the figure by eye. Confirmation and divergence: Part 1.",
            left=Content(
                title="Figure 6.24: volume and open interest disagree at B",
                lines=(
                    "Volume peaks higher at B than at A [1]: price and volume rise together, bullish confirmation.",
                    "Open interest peaks lower at B than at A [2]: price rises as open interest falls, bearish divergence.",
                    "They disagree. The book reads the open interest: longs liquidating, early. Silver then fell from about $49 to under $30.",
                ),
                accent="When the two disagree, the book reads open interest.",
            ),
            picture=Figure(
                number="6.24",
                shows="The open interest and volume panels of the continuous daily chart of silver, from 2005 to 2012. At B, early 2011, volume makes a higher peak than at A, marked 1, labelled bullish confirmation; open interest makes a lower peak, marked 2, labelled bearish divergence.",
                aspect=0.784,
                crop=(0.34, 0.54, 0.0, 0.0),
                marks=(
                    Mark(1, "circle", 0.576, 0.489, 0.758, 0.674),
                    Mark(2, "circle", 0.576, 0.239, 0.758, 0.402),
                ),
            ),
            text_w=5.6,
            notes=(
                "Point at mark 1, the volume peak at B, taller than the one at A; then mark 2, the open interest peak at B, lower than the one at A.",
                "On the figure, volume and open interest disagree at the top: volume peaks at the highest price, open interest does not. The book reads the open interest: longs leaving.",
            ),
        ),
        Pair(
            origin="Book p.192: one sentence and its reason. The chart is ours: two invented reversals, the open interest in each made up to show the point.",
            left=Content(
                title="Very high open interest: a faster reversal",
                lines=(
                    "The level of open interest may indicate the nature of a reversal or breakout: here, its speed.",
                    "If open interest is very high, the reversal may be significantly more rapid.",
                    "Ours: about 85,000 open contracts against 20,000. After the same top, the first falls steeply.",
                ),
                accent="The reason: many open contracts liquidating and covering at once.",
                caption="Liquidating: longs selling to close. Covering: shorts buying back. The book sets no number for very high.",
            ),
            picture=Chart(
                letter="AC",
                shows="Two small invented cases of a top and the fall after it. Left: open interest very high, about 85,000 contracts, and the fall is steep. Right: open interest low, about 20,000, and the fall is gradual.",
            ),
            text_w=6.0,
            notes=(
                "Chapter 4 said rising open interest in a consolidation makes the breakout more rapid. This is the same idea at a reversal.",
                "May be, says the book: a tendency, not a rule.",
            ),
        ),
        Check(
            label="Open interest",
            questions=(
                Q(
                    stem="A trader with a long futures contract sells it to a new buyer, who takes over the long. Open interest:",
                    options=("Increases by one",
                             "Decreases by one",
                             "Stays unchanged",
                             "Doubles"),
                    answer="C",
                    reason="Open interest is unchanged when one side is replaced by a new position, but not both.",
                ),
                Q(
                    stem="Prices are rising while volume and open interest are both declining. The book reads this as:",
                    options=("Bearish: shorts covering and longs leaving the market",
                             "Bullish: buying pressure",
                             "Bearish: short selling",
                             "Bullish: liquidation drying up"),
                    answer="A",
                    reason="Rising prices on declining volume and open interest are bearish, driven by shorts covering and longs leaving.",
                ),
            ),
        ),
        Pair(
            origin="Book pp.192-193. OTC fx is the book's over the counter foreign exchange market. The five trades are Part 1's, ours. Chapter 3 counted trades the same way.",
            left=Term(
                term="Tick volume",
                plain="A count of trades, not shares: one tick is one trade, of any size. Met in Chapters 1 and 3.",
                example="Part 1's five trades of 0.1, 0.6, 0.3, 1.2 and 0.2 million shares: volume 2.4 million shares, tick volume 5.",
                formal="One tick represents one trade: tick volume is transaction volume. Many OTC fx brokers offer it instead of actual volume; strongly correlated with it, it may be used as a proxy.",
            ),
            picture=Chart(
                letter="AD",
                shows="The same five trades counted two ways. Left, by size: columns of 0.1, 0.6, 0.3, 1.2 and 0.2 million shares, adding to a volume of 2.4 million. Right, by number: five equal ticks of one trade each, adding to a tick volume of 5.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "This is review question 1: volume counts what was traded, tick volume counts how many trades. One trade may be 1 contract or 1,000.",
                "OTC fx and proxy are spelled out on the next slide.",
            ),
        ),
        Content(
            origin="Book pp.192-193. The trade counts and amounts in the example are ours, invented.",
            title="Tick volume as a stand-in for volume",
            lines=(
                "Where: the over the counter (OTC) foreign exchange (fx) market, where many brokers offer tick volume instead of actual volume. The book does not say why.",
                "Strongly correlated: the two rise and fall together. Ours: a busy hour, 900 trades and 60 million in currency; a quiet hour, 200 trades and 14 million.",
                "So tick volume may be a proxy, a stand-in, for actual volume, for comparing relative levels of overbought and oversold: Part 2's words, never defined.",
            ),
            accent="Compare tick volume with its own past: 900 trades does not say how much changed hands.",
            notes=(
                "This slide has no picture: the chart beside the term already counts the same trades both ways.",
                "Relative levels is the book's phrase: higher or lower than before, as on the first slide of this part.",
            ),
        ),
        Pair(
            origin="Book p.193 gives the ratio. The counts and volumes in the example are ours. Advances and declines: Chapter 3's breadth data, never defined.",
            left=Term(
                term="The Arms Index, or TRIN",
                plain="Breadth: advances, stocks that rose, over declines, stocks that fell. Divided by up volume over down volume, the shares each side traded. Our readings.",
                example="1,500 advances / 1,000 declines = 1.5. Up volume 600 million / down volume 800 million = 0.75. TRIN = 1.5 / 0.75 = 2.0.",
                formal="The Arms Index, or TRIN, incorporates breadth volume, advances and declines: TRIN = (advances / declines) / (up volume / down volume).",
            ),
            picture=Chart(
                letter="AE",
                shows="The TRIN worked as arithmetic in three columns. Advances 1,500 against declines 1,000, a ratio of 1.5. Up volume 600 million against down volume 800 million, a ratio of 0.75. Then 1.5 divided by 0.75, a TRIN of 2.0.",
            ),
            text_w=7.0,
            notes=(
                "Advances and declines were listed in Chapter 3 as breadth data and never defined. The plain row reads them as the number of stocks rising and falling; that reading is ours.",
                "Up volume and down volume: the volume in the rising stocks and in the falling ones, again our reading of the names.",
                "Work the arithmetic slowly. The TRIN is a ratio of two ratios.",
            ),
        ),
        Pair(
            origin="Book p.193 gives the ratio. It names breadth volume, advances, declines, up and down volume and never defines them; our readings. The numbers are ours.",
            left=Content(
                title="The TRIN, step by step",
                lines=(
                    "1  Advances / declines = 1,500 / 1,000 = 1.5 rising stocks for each falling one.",
                    "2  Up volume / down volume = 600m / 800m = 0.75: the falling stocks traded more shares.",
                    "3  TRIN = 1.5 / 0.75 = 2.0. Rearranged: down volume per falling stock, 800m / 1,000 = 0.8m, over up volume per rising stock, 600m / 1,500 = 0.4m.",
                ),
                accent="A TRIN of 2.0: each falling stock traded, on average, twice the volume of each rising stock.",
                caption="Step 3 and the gold line are our arithmetic; the book never reads one value such as 2.0.",
            ),
            picture=Chart(
                letter="HE",
                shows="The TRIN worked as the slide's three steps, numbered. 1 advances 1,500 against declines 1,000, a ratio of 1.5. 2 up volume 600 million against down volume 800 million, a ratio of 0.75. 3 the two ratios and their quotient, a TRIN of 2.0, in gold.",
            ),
            text_w=6.6,
            notes=(
                "Each step on the slide is the cell with its number on the chart: read the columns, then the division under them.",
                "Step 3 is only the same division rearranged. Check it on the board: 0.8 / 0.4 = 2.0.",
            ),
        ),
        Pair(
            origin="Book p.193 and Figure 6.25; the levels are read off the figure by eye. The caption says daily; the chart and the text say 1-minute.",
            left=Content(
                title="Reading the tick and the TRIN",
                lines=(
                    "The tick: the book never says what it measures. On Figure 6.25 it goes below zero [1], so it is not tick volume, a count of trades.",
                    "Short term, the book's rule: tick rising but not overbought, TRIN falling but not oversold: bullish, look for a long entry.",
                    "Figure 6.25 shows something else: tick down to about -1,000 [1], TRIN up to about 2.2 [2], both at levels it labels oversold. The index then rose [3].",
                ),
                accent="Both at the labelled oversold extremes: the book reads short-term bullish, look for a long entry.",
                caption="The book does not say why its figure departs from its short-term rule.",
            ),
            picture=Figure(
                number="6.25",
                shows="A 1-minute chart of the S&P 500 index falling and then rising, with a $TICK panel and a $TRIN panel under it. A box around the low marks both labelled oversold, with the note that short-term bullishness was predicated on the confluence of oversold signals.",
                aspect=1.382,
                crop=(0.44, 0.15, 0.0, 0.05),
                marks=(
                    Mark(1, "box", 0.223, 0.65, 0.393, 0.806),
                    Mark(2, "box", 0.223, 0.813, 0.393, 0.894, at=(0.20, 0.80)),
                    Mark(3, "arrow", 0.357, 0.55, 0.679, 0.4),
                ),
            ),
            text_w=7.4,
            notes=(
                "Read the short-term rule, then point at the box: the tick dips and the TRIN rises, the opposite of the rule's bullish case. Say so; do not reconcile it.",
                "The converse, the longer-term rule and the book's gaps are the next slide.",
            ),
        ),
        Content(
            origin="Book p.193. The weekly tick numbers are ours, in invented units; the book never says what the tick measures.",
            title="The longer-term rule, and the book's gaps",
            lines=(
                "Short term, the converse: tick falling but not oversold, TRIN rising but not overbought: bearish, look for a short entry.",
                "Longer term: tick oversold, above its weekly two-sigma level, and TRIN overbought, near or above 3.0 daily: bullish, long. Reverse: bearish, short.",
                "Two sigma: Part 3's line, k = 2. Ours: weekly tick mean 200, sigma 300: 200 + 2 x 300 = 800; above it, oversold. Daily TRIN 3.2: overbought.",
            ),
            accent="The book gives no reason for either rule.",
            notes=(
                "No picture: this slide states the book's rules; the next one sets them against its figure.",
                "No check rests on these rules. The check after this part tests only tick volume and the TRIN's arithmetic.",
            ),
        ),
        Pair(
            origin="Book p.193 and Figure 6.25; the levels are read off the figure by eye.",
            left=Content(
                title="Figure 6.25 against the text's rules",
                lines=(
                    "The text calls a bullish TRIN overbought. Figure 6.25 labels its TRIN oversold [2], at the low, before the index rose.",
                    "The text's longer-term oversold tick is above a two-sigma level. The figure's oversold tick [1] sits at its low.",
                ),
                accent="The book does not say why its figure and its text differ.",
            ),
            picture=Figure(
                number="6.25",
                shows="The 1-minute S&P 500 chart of the last slides. In the box at the low, the TRIN reaches about 2.2 at the line the figure labels TRIN oversold, and the tick drops to about -1,000 at the line it labels TICK oversold: both at the bottom of their swing, not above a two-sigma level.",
                aspect=1.382,
                crop=(0.44, 0.15, 0.0, 0.05),
                marks=(
                    Mark(1, "box", 0.223, 0.65, 0.393, 0.806),
                    Mark(2, "box", 0.223, 0.813, 0.393, 0.894, at=(0.20, 0.80)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Marks numbered as on the slide before last. Point at mark 2, the TRIN the figure calls oversold, then read the text's rule: a bullish TRIN is overbought. Do not settle the gap; name it.",
                "Then mark 1, the tick at its low. The text's longer-term oversold tick is above a two-sigma level, so the figure is not that rule either.",
            ),
        ),
        Pair(
            origin="Book p.194 and Figure 6.26; the TRIN values are read off the figure. Its caption says daily; the times show a 1-minute chart.",
            left=Content(
                title="A bearish day on the tick and the TRIN",
                lines=(
                    "Figure 6.26: the S&P 500 falls all afternoon. The boxed TRIN rises from about 0.9 to 1.34 [1]: bearish, by the short-term rule.",
                    "1:45 to 2:45 p.m.: the text says largely absent of activity; the figure says absent of uptick action. In its shaded box [2] the tick barely rises above zero and twice drops to about -1,000, circled as extreme bearish ticks [3].",
                ),
                accent="Together, a short-term bearish signal: look for a short entry.",
                caption="The book gives no reason this is bearish, and does not define uptick.",
            ),
            picture=Figure(
                number="6.26",
                shows="A 1-minute chart of the S&P 500 index on an intraday decline, with a $TICK panel showing stretches marked bearish and balanced tick action, and a $TRIN panel whose last stretch is boxed and labelled rising TRIN, bearish.",
                aspect=1.401,
                crop=(0.555, 0.28, 0.0, 0.02),
                marks=(
                    Mark(1, "arrow", 0.169, 0.907, 0.843, 0.743, at=(0.236, 0.964)),
                    Mark(2, "box", 0.112, 0.521, 0.506, 0.65),
                    Mark(3, "arrow", 0.03, 0.693, 0.146, 0.693, at=(0.03, 0.693)),
                ),
            ),
            text_w=6.6,
            notes=(
                "A rising TRIN is bearish, by the short-term rule two slides back. Point at the boxed stretch, then at the shaded tick stretch labelled bearish after 1:45.",
                "Uptick is the figure's word and is not defined by the book. Read it only as the label on the figure.",
            ),
        ),
        Check(
            label="Tick volume and the TRIN",
            questions=(
                Q(
                    stem="One trade of 1,000 contracts and one trade of 1 contract are made. Tick volume is:",
                    options=("1,001",
                             "1,000",
                             "1",
                             "2"),
                    answer="D",
                    reason="One tick represents one trade, whatever its size: two trades, a tick volume of 2.",
                ),
                Q(
                    stem="Advances 1,200, declines 800, up volume 900 million, down volume 600 million. The TRIN is:",
                    options=("1.0",
                             "1.5",
                             "2.25",
                             "0.67"),
                    answer="A",
                    reason="(1,200 / 800) / (900 / 600) = 1.5 / 1.5 = 1.0.",
                ),
            ),
        ),
        Pair(
            origin="Book p.194 defines both. The chart is ours: the volume by price is added up from its own invented bars and volume.",
            left=Term(
                term="Volume by price and volume by time",
                plain="One volume record added up two ways. By time: the usual bars, one a day. By price: sideways bars, one per price band.",
                example="Our chart, 100 days: 68 million shares at PHP 48 to 50, the longest sideways bar; 12 million at PHP 54 to 56. Five days worked: next slide.",
                formal="Volume by time represents the total volume traded over a specified time interval or period. Volume by price identifies the total volume traded at each price level.",
            ),
            picture=Chart(
                letter="AF",
                shows="An invented share over 100 days with its volume drawn both ways: sideways bars from the left edge, one for each two-peso price band, each labelled in million shares, the longest, 68 million, at 48 to 50 pesos; and the usual volume bars under the chart, one for each day.",
            ),
            text_w=7.0,
            notes=(
                "The same trades, added up two ways: by when they happened, and by the price they happened at.",
                "Each sideways bar on the chart is the total of every day's volume while price sat in that band.",
            ),
        ),
        Content(
            origin="Book p.194 defines both. The five days, their closes and their volumes are ours, invented.",
            title="Adding up volume by price, worked",
            lines=(
                "Ours, five days: closes of PHP 49.10, 49.80, 51.20, 48.60 and 50.50, on 2, 3, 1, 4 and 2 million shares.",
                "By time: one bar a day, 2, 3, 1, 4, 2 million: the usual volume panel.",
                "By price: each day's volume goes in the band of its close. PHP 48 to 50: 2 + 3 + 4 = 9 million. PHP 50 to 52: 1 + 2 = 3 million.",
            ),
            accent="The same 12 million shares: most traded between PHP 48 and 50. Using both splits: two-dimensional volume analysis.",
            caption="The book does not say how a day's volume is split across its prices; ours puts it all at the close.",
            notes=(
                "This slide has no picture: the chart beside the term is the same sum done over 100 days.",
                "Do the sum on the board: which days closed between 48 and 50? Days 1, 2 and 4.",
            ),
        ),
        Pair(
            origin="Book p.194 and Figure 6.27. Chapter 4 showed the same thing and called it price-based volume.",
            left=Content(
                title="Volume by price marks a support: silver",
                lines=(
                    "Figure 6.27, iShares Silver Trust: sideways bars longest around $17 [1]. The book's volume turnover here is shares traded, not the turnover ratio.",
                    "So $17 [2] represents a significant support: a floor where a fall may stop. The figure: significant capital commitment.",
                    "Also marked: high volume at about $35 [3], a new consolidation level, not in the text.",
                ),
                accent="Ordinary volume bars show when, not at what price.",
                caption="Chapter 4's price-based volume; not Part 1's oscillators.",
            ),
            picture=Figure(
                number="6.27",
                shows="The daily iShares Silver Trust with volume by price drawn as horizontal bars from the left edge. The longest bars sit around the $17 level, labelled significant capital commitment, strong support, and another cluster at the newer consolidation level higher up.",
                aspect=1.569,
                marks=(
                    Mark(1, "box", 0.005, 0.775, 0.48, 0.875),
                    Mark(2, "line", 0.50, 0.805, 0.70, 0.805, at=(0.61, 0.73)),
                    Mark(3, "box", 0.005, 0.49, 0.285, 0.585),
                ),
            ),
            text_w=6.0,
            notes=(
                "Find the longest sideways bars, near $17, and then find price returning to that level.",
                "Clear up the word: Chapter 4's price-based volume is this, volume by price. Part 1's price-based oscillators are a different thing.",
            ),
        ),
        Pair(
            origin="Book p.194 and Figure 6.28.",
            left=Content(
                title="The most traded range: 3M",
                lines=(
                    "Figure 6.28, 3M: the longest sideways bars, bracketed, $77 to $86 [1]: the most traded range, more shares than at any other price.",
                    "With 3M last at about $88 [2], $77 to $86 lies below: potential support, the figure's label. $90 to $92 above [3]: some resistance, says the book, not how it was found.",
                ),
                accent="These price ranges are potential future support and resistance levels.",
            ),
            picture=Figure(
                number="6.28",
                shows="The price panel of the daily chart of 3M with volume by price as horizontal bars, the longest bracketed between about $77 and $86 and labelled maximum capital commitment in this range, an important support zone in the future; 3M last at about $88.",
                aspect=1.613,
                crop=(0.0, 0.0, 0.0, 0.30),
                marks=(
                    Mark(1, "box", 0.005, 0.429, 0.47, 0.70),
                    Mark(2, "circle", 0.885, 0.336, 0.955, 0.443, at=(0.79, 0.429)),
                    Mark(3, "box", 0.005, 0.221, 0.35, 0.321),
                ),
            ),
            text_w=5.6,
            notes=(
                "The bracket on the figure is the $77 to $86 range. Price later falls through it and returns.",
                "Read the price axis on the right: $88 now, the bracket below it, $90 to $92 above.",
            ),
        ),
        Pair(
            origin="Book p.194 and Figure 6.28. Confirmation and divergence: Part 1.",
            left=Content(
                title="The volume panel on 3M",
                lines=(
                    "The figure's own lines carry Part 1's names.",
                    "Bearish confirmation [4]: price falling, May to October, on rising volume.",
                    "Bearish divergence [5]: price rising, November to February, on falling volume.",
                ),
                accent="Volume read against price, as in Part 1, on the same chart.",
            ),
            picture=Figure(
                number="6.28",
                shows="The daily chart of 3M from May 2011 to February 2012: a falling price line with a rising volume line under it, labelled bearish confirmation, then a rising price line with a falling volume line under it, labelled bearish divergence.",
                aspect=1.613,
                crop=(0.36, 0.08, 0.0, 0.02),
                marks=(
                    Mark(4, "line", 0.005, 0.811, 0.477, 0.722, color="gold"),
                    Mark(5, "line", 0.562, 0.739, 0.891, 0.878, color="red"),
                ),
            ),
            text_w=5.6,
            notes=(
                "Point at mark 4, the volume line rising under the falling price, then mark 5, the volume line falling under the rising price.",
                "The figure's own labels name both: Part 1's names again.",
            ),
        ),
        Pair(
            origin="Book pp.196-197, its steps. The chart is ours, on invented prices, with the steps numbered in the book's order.",
            left=Content(
                title="Support and resistance in four steps",
                lines=(
                    "1  Largest volume by price range: ours, PHP 48 to 50.",
                    "2  Largest volume by time intervals: ours, two bursts of 3.4 to 4.1 million a day.",
                    "3  Intersection, the boxes: most shares at one price, step 1's band, in one stretch, step 2's days.",
                    "4  Closest peak above the intersection: resistance, PHP 50.80. Closest trough below: support, PHP 47.50.",
                ),
                accent="Potentially the most significant and reliable support and resistance.",
                caption="No reason given; largest is picked by eye.",
            ),
            picture=Chart(
                letter="AG",
                shows="An invented share with volume by price and volume by time, and the book's four steps numbered on it: 1 the longest sideways bars, a gold band; 2 the busiest stretches of days, shaded; 3 the boxes where the band and the stretches cross; 4 a resistance line at the nearest peak above the boxes, PHP 50.80, and a support line at the nearest trough below, PHP 47.50.",
            ),
            text_w=6.6,
            notes=(
                "Follow the numbers on the chart in order. The band is step 1, the shaded columns step 2, the boxes step 3, the two lines step 4.",
                "The book takes the nearest turn either side of the intersection. The next slide says what our two levels then did.",
            ),
        ),
        Pair(
            origin="Book pp.196-197. The prices are our chart's, read from the series that drew it.",
            left=Content(
                title="What the two levels did on our chart",
                lines=(
                    "Support at PHP 47.50: price turned up near it twice, at 1, PHP 47.40, and 2, PHP 47.50.",
                    "Resistance at PHP 50.80: price turned down near it twice, at 3, PHP 50.90, and 4, PHP 50.80, then broke above it and rose to about PHP 58.60, at 5.",
                ),
                accent="Potential levels, the book says, not certain ones: ours held twice, then broke. It does not say what a break means.",
            ),
            picture=Chart(
                letter="HG",
                shows="The invented share of the four steps chart with its two step 4 levels, resistance at PHP 50.80 and support at PHP 47.50. Price turns up near support at 1, PHP 47.40, and 2, PHP 47.50; turns down near resistance at 3, PHP 50.90, and 4, PHP 50.80; then breaks above and rises to about PHP 58.60 at 5.",
            ),
            text_w=6.0,
            notes=(
                "Read the five numbers in order: two turns up at support, two turns down at resistance, then the break.",
                "Do not add a rule for the break. The book gives none.",
            ),
        ),
        Pair(
            origin="Book pp.196-197 and Figure 6.29; the two levels are read off the figure by eye.",
            left=Content(
                title="The four steps on 3M",
                lines=(
                    "[1]  $74 to $80: the book's largest volume by price range, the dark sideways bars.",
                    "[2]  The dark columns, where volume reaches the dotted overextended volume level (Part 2), cross it in two white boxes, [3] and [5].",
                    "[4]  Closest peak above, about $80: resistance. Closest trough below, about $72.50: support.",
                ),
                accent="Both act as effective barriers to price on the daily chart of 3M.",
                caption="A page earlier the book gave 3M's most traded range as $77 to $86. It does not say why they differ.",
            ),
            picture=Figure(
                number="6.29",
                shows="The daily chart of 3M with the $74 to $80 volume by price band and two dark time columns over the high volume intervals; where they cross are two white boxes. Dashed lines mark the closest resistance above and the closest support below, and an overextended volume level runs across the volume panel.",
                aspect=1.656,
                marks=(
                    Mark(1, "box", 0.005, 0.33, 0.45, 0.50),
                    Mark(2, "box", 0.555, 0.76, 0.765, 0.97, at=(0.65, 0.76)),
                    Mark(3, "box", 0.56, 0.37, 0.61, 0.50, at=(0.585, 0.33)),
                    Mark(5, "box", 0.70, 0.37, 0.75, 0.50, at=(0.725, 0.33)),
                    Mark(4, "box", 0.79, 0.35, 0.945, 0.56),
                ),
            ),
            text_w=5.6,
            notes=(
                "Read the figure with the last slide's numbers. The two white boxes are step 3.",
                "The dashed arrows mark the two levels of step 4: resistance at about $80, at the top of the zone, and support at about $72.50, below it. The overextended volume level on the volume panel is Part 2's.",
            ),
        ),
        Check(
            label="Two-dimensional volume",
            questions=(
                Q(
                    stem="Volume by price identifies:",
                    options=("The total volume over a time interval",
                             "The number of trades at each price",
                             "The total volume traded at each price level",
                             "The open interest at each price"),
                    answer="C",
                    reason="Volume by price identifies the total volume traded at each price level.",
                ),
                Q(
                    stem="In the book's two-dimensional method, the most significant resistance is:",
                    options=("The highest price on the chart",
                             "The top of the largest volume by price range",
                             "The level of the largest volume by time bar",
                             "The closest peak above the area of intersection"),
                    answer="D",
                    reason="Locate the intersection of the largest volume by price and by time; the closest peak above it is the resistance.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Part 5 - 6.1, pp.197 to 202: volume against bar range, constant volume
# charts, volume leading price, volume cycles, and volume on charts whose
# time axis is not constant.
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="The Mechanics of Volume Action: Bar Range, Cycles and Non-Constant Time",
    short="6.1 Bar range",
    minutes="",
    covers=(),
    slides=(
        Pair(
            origin="Book p.197 and Figure 6.30; Chapter 5, characteristic 15. The pesos are ours. Spread is the book's word for bar range here.",
            left=Content(
                title="6.1  Volume and bar range: Chapter 5's four cases",
                lines=(
                    "Bar range, as in Chapter 5: a bar's high minus its low. High PHP 52.00, low PHP 51.20: range PHP 0.80. The book also says spread, not Chapter 3's bid-ask spread.",
                    "Set range against volume: four cases. Figure 6.30 draws each as an empty box, the range, over a black box, the volume.",
                    "[1] short range, low volume; [2] short, high; [3] tall, low; [4] tall, high. The book uses them to forecast breakouts and reversals.",
                ),
                accent="Chapter 5's squat bar, a small range on large volume, is case 2.",
            ),
            picture=Figure(
                number="6.30",
                shows="Four numbered pairs: an empty box for the bar range over a black box for the volume. 1 short on low, 2 short on high, 3 tall on low, 4 tall on high.",
                aspect=1.174,
                marks=tuple(Mark(n + 1, "line", x0, top, x0, 0.86,
                                 at=(x0, 0.55))
                            for n, (x0, top) in enumerate(
                                ((0.33, 0.22), (0.52, 0.22),
                                 (0.71, 0.02), (0.90, 0.02)))),
            ),
            text_w=7.4,
            notes=(
                "A recall first: Chapter 5 drew these four as Chart R and called the second one the squat bar.",
                "Do the subtraction out loud: 52.00 minus 51.20 is 0.80. That is all bar range means.",
                "The figure is the book's whole picture of them: a box for the range, a box for the volume. The next slides name each and put it in a trend.",
            ),
        ),
        Pair(
            origin="Book p.197: the four names. The pesos and share counts in the example are ours. The chart is ours: sketches, not prices.",
            left=Term(
                term="Rest, reversal and continuation bars",
                plain="One name for each of four kinds of bar: narrow or wide range, on low or high volume, each judged against the trend's usual bars.",
                example="Usual bar: PHP 1.00 on 2 million shares. PHP 0.20 on 5 million: narrow, high, a High Volume Reversal Bar.",
                formal="Narrow range on low volume: Low Volume Rest Bar. Narrow, high volume: High Volume Reversal Bar. Wide, low volume: Low Volume Reversal Bar. Wide, high volume: High Volume Continuation Bar.",
            ),
            picture=Chart(
                letter="AH",
                shows="Four small cases, each a short uptrend of price bars over volume, ending in the named bar picked out in gold with its volume bar: a narrow bar on low volume, the rest bar; a narrow bar on high volume, the high volume reversal bar; a wide bar on low volume, the low volume reversal bar; a wide bar on high volume, the continuation bar.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The example is the second of the four, the high volume reversal bar: Chapter 5's squat bar, now with a name.",
                "Narrow and wide are against the trend's usual bars, as low and high are against its usual volume. The next slide works all four with numbers.",
            ),
        ),
        Pair(
            origin="Book p.197: the four names. Ours: every number, the comparison with the usual bar, which the book does not put a number on, and the chart: sketches, not prices.",
            left=Content(
                title="Naming a bar, step by step",
                lines=(
                    "Step 1, the usual bar, grey: about PHP 1.00 high to low, on 2 million shares; ours, as the book gives no number.",
                    "Step 2, compare. [1] PHP 0.20 on 1 million: narrow, low: Low Volume Rest Bar. [2] PHP 0.20 on 5 million: narrow, high: High Volume Reversal Bar.",
                    "[3] PHP 2.50 on 1 million: wide, low: Low Volume Reversal Bar. [4] PHP 2.50 on 5 million: wide, high: High Volume Continuation Bar.",
                ),
                accent="Judge each bar against the bars around it.",
            ),
            picture=Chart(
                letter="JA",
                shows="The four named bars on the slide's numbers, numbered 1 to 4. In each case seven grey usual bars, about PHP 1.00 on 2 million shares, then the named bar boxed in gold over its gold volume: 1 PHP 0.20 on 1 million, 2 PHP 0.20 on 5 million, 3 PHP 2.50 on 1 million, 4 PHP 2.50 on 5 million.",
                marks=(
                    Mark(1, "box", 0.395, 0.12, 0.455, 0.43, at=(0.36, 0.25)),
                    Mark(2, "box", 0.895, 0.12, 0.955, 0.43, at=(0.86, 0.25)),
                    Mark(3, "box", 0.395, 0.57, 0.455, 0.86, at=(0.36, 0.72)),
                    Mark(4, "box", 0.895, 0.57, 0.955, 0.86, at=(0.86, 0.72)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Go round the chart 1 to 4. For each, say the range against the grey bars, then the volume against the grey columns, then the name.",
                "Ask the room for a fifth: PHP 0.90 on 2.1 million. Neither narrow nor wide, neither low nor high: an ordinary bar, no name.",
            ),
        ),
        Pair(
            origin="Book p.197: the readings are the book's; the gold line is our summary. The chart is ours: sketches, not prices.",
            left=Content(
                title="The two reversal bars",
                lines=(
                    "[1] High Volume Reversal Bar, narrow on high volume, chart left: a strong potential for reversal. Bearish in an uptrend; the converse, bullish, in a downtrend.",
                    "[2] Low Volume Reversal Bar, wide on low volume, right: a potential for reversal. The longer the bar, the more bearish in an uptrend, bullish in a downtrend.",
                ),
                accent="Too little movement for the volume, or too little volume for the move.",
            ),
            picture=Chart(
                letter="AI",
                shows="Two small invented uptrends of price bars over volume. Left: a narrow bar on very high volume at the top, the high volume reversal bar, then price falls. Right: a very wide bar on low volume at the top, the low volume reversal bar, then price falls.",
                marks=(
                    Mark(1, "box", 0.265, 0.13, 0.335, 0.93, at=(0.37, 0.55)),
                    Mark(2, "box", 0.765, 0.13, 0.835, 0.93, at=(0.87, 0.52)),
                ),
            ),
            text_w=5.8,
            notes=(
                "Left cell: find the tall gold volume bar, then the tiny price bar above it. Right cell: the short gold volume bar, then the long price bar above it.",
                "In both cells price falls after the named bar, because both are drawn in an uptrend, where both are bearish.",
            ),
        ),
        Pair(
            origin="Book p.197: the reason is the book's, and the converse is its word for the downtrend case. Ours: every number, and the chart: a sketch, not prices.",
            left=Content(
                title="Why the reversal bars warn, with numbers",
                lines=(
                    "[1] Ours: the usual bar moves PHP 1.00 on 2 million shares. Today 5 million trade, 2.5 times usual, and price moves only PHP 0.20.",
                    "The book: were that volume buying, the range would be much wider. So sellers are attempting to take control. In a downtrend, the converse.",
                ),
                accent="A warning of a potential turn, not a certainty: the book gives no entry rule.",
            ),
            picture=Chart(
                letter="JB",
                shows="The high volume reversal bar on the slide's numbers: a rise of usual bars, about PHP 1.00 on 2 million, topped by a PHP 0.20 bar on 5 million, boxed, then a fall.",
                marks=(
                    Mark(1, "box", 0.56, 0.14, 0.645, 0.875, at=(0.69, 0.50)),
                ),
            ),
            text_w=6.8,
            notes=(
                "Point at the tall gold volume column, then the tiny boxed bar above it: a lot of volume, almost no movement.",
                "Participation is the book's word for volume: how many shares changed hands.",
            ),
        ),
        Pair(
            origin="Book p.197: the reason is the book's. Ours: every number, and the chart: a sketch, not prices.",
            left=Content(
                title="Why the low volume reversal bar warns, with numbers",
                lines=(
                    "[1] Ours: price jumps PHP 3.00 on 0.7 million shares, a third of the usual 2 million.",
                    "The book: a large move on little participation, its word for volume: a lack of interest. Bearish in an uptrend, bullish in a downtrend.",
                ),
                accent="Too little volume for the move: a potential reversal.",
            ),
            picture=Chart(
                letter="JN",
                shows="The low volume reversal bar on the slide's numbers: a rise of usual bars, about PHP 1.00 on 2 million, topped by a PHP 3.00 bar on 0.7 million, boxed, then a fall.",
                marks=(
                    Mark(1, "box", 0.56, 0.14, 0.645, 0.875, at=(0.69, 0.50)),
                ),
            ),
            text_w=6.8,
            notes=(
                "Point at the short gold volume column, then the long boxed bar above it: a big move that few shares paid for.",
                "Both reversal bars warn of a turn; neither is a signal to trade on its own, the book gives no entry rule.",
            ),
        ),
        Pair(
            origin="Book p.197: the readings and reasons are the book's. The chart is ours: sketches, not prices.",
            left=Content(
                title="The rest bar and the continuation bar",
                lines=(
                    "Low Volume Rest Bar, narrow on low volume: a lack of participation. In a strong, rapid trend [1], a potential reversal; in a weak to average one [2], a point of rest.",
                    "[3] High Volume Continuation Bar, wide on high volume: backed by very large participation. Bullish in an uptrend, bearish in a downtrend.",
                ),
                accent="The rest bar reads by the trend's speed; the continuation bar, by its direction.",
            ),
            picture=Chart(
                letter="AJ",
                shows="Three small invented cases of price bars over volume. A rest bar, narrow on low volume, at the top of a strong, rapid rise, after which price reverses. A rest bar in a slow, average rise, after which price rests and rises again. A continuation bar, wide on high volume, after which the rise continues.",
                marks=(
                    Mark(1, "box", 0.16, 0.18, 0.225, 0.93, at=(0.25, 0.52)),
                    Mark(2, "box", 0.48, 0.27, 0.545, 0.93, at=(0.450, 0.230)),
                    Mark(3, "box", 0.815, 0.29, 0.885, 0.93, at=(0.785, 0.250)),
                ),
            ),
            text_w=CHART_W,
            notes=(
                "The first two cells are the same kind of bar in two trends. The book's point is that the trend decides what it means.",
                "The continuation bar is Chapter 5's trend promoting case, named.",
            ),
        ),
        Pair(
            origin="Book p.197; Chapter 5, characteristic 15. Ours: every number, the chart, and a pause as the plain reading of point of rest. The book gives no reason speed matters.",
            left=Content(
                title="The rest bar's two readings, with numbers",
                lines=(
                    "[1] Ours: a rise of PHP 1.60 a bar stalls on a PHP 0.30 bar with a quarter of the usual volume. That fast, then that quiet: a potential reversal.",
                    "[2] The same quiet bar in a rise of PHP 0.45 a bar: a point of rest, a pause before the rise goes on. The book gives no speed for strong and rapid.",
                    "Chapter 5 called both low volume bars only trend inhibiting, holding the trend back. Here each can also mark a reversal.",
                ),
                accent="Read the rest bar with the trend's speed.",
            ),
            picture=Chart(
                letter="JC",
                shows="Two sketched rises, each with the same quiet rest bar boxed over its short gold volume column. 1: a steep rise of PHP 1.60 a bar, after which price reverses. 2: a slow rise of PHP 0.45 a bar, after which price pauses and rises again.",
                marks=(
                    Mark(1, "box", 0.26, 0.18, 0.32, 0.91, at=(0.35, 0.47)),
                    Mark(2, "box", 0.735, 0.29, 0.795, 0.91, at=(0.705, 0.250)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Same boxed bar in both cells; only the slope before it differs. Point at the slope first, then the bar.",
                "The change from Chapter 5 is the one to say twice: a quiet bar was only a brake there. Here it can be a turn.",
            ),
        ),
        Check(
            label="Bar range and volume",
            questions=(
                Q(
                    stem="In an uptrend, a bar has a narrow range on very large volume. The book calls it:",
                    options=("A High Volume Continuation Bar",
                             "A Low Volume Rest Bar",
                             "A High Volume Reversal Bar",
                             "A Low Volume Reversal Bar"),
                    answer="C",
                    reason="Narrow range on high volume is the High Volume Reversal Bar: sellers taking control, bearish in an uptrend.",
                ),
                Q(
                    stem="A Low Volume Rest Bar appears in a weak to average trend. It tends to indicate:",
                    options=("A point of rest",
                             "A strong reversal",
                             "A continuation on heavy buying",
                             "A selling climax"),
                    answer="A",
                    reason="In weak to average trends the rest bar tends to indicate a point of rest; in strong, rapid trends, a potential reversal.",
                ),
            ),
        ),
        Pair(
            origin="Book p.198 and Figure 6.31, the PowerShares DB U.S. Dollar Bullish Fund. Ours: volumes read by eye. The curved lines are Bollinger Bands, not discussed.",
            left=Content(
                title="High volume reversal bars: a dollar fund",
                lines=(
                    "At [1] and [2]: a narrow range candle on one of the tallest volume bars, about 11 to 13 million shares against 5 million most days.",
                    "Point 1, late October, at a low: price then rises. Point 2, at the year end, ends a dip from about 22.6 to 22.35: price turns back up to 22.72.",
                    "[3] August: volume falls into a triangle's apex, where its lines meet: Part 2's low volume breakout signal. Then a volume surge.",
                ),
                accent="Narrow bar, heavy volume, then a turn.",
            ),
            picture=Figure(
                number="6.31",
                shows="The daily dollar fund: narrow range candlesticks on high volume circled at 1, at a low, and 2, at a dip near the highs, lined to tall volume bars; a triangle at the left.",
                aspect=1.639,
                marks=(
                    Mark(1, "circle", 0.51, 0.49, 0.62, 0.66, at=(0.520, 0.500)),
                    Mark(2, "circle", 0.855, 0.16, 0.94, 0.29, at=(0.865, 0.170)),
                    Mark(3, "box", 0.07, 0.44, 0.32, 0.72, at=(0.040, 0.400)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Both points are reversal bars after a fall, so the converse applies: bullish. Point 1 ends a decline, Point 2 a short dip near the highs; price turns up after each, as the book says.",
                "The triangle on the left is Part 2's low volume breakout signal again: volume falling into the apex, then surging. The book calls it a descending triangle; its shape is the book's Chapter 13.",
            ),
        ),
        Pair(
            origin="Book p.198 and Figure 6.32, the PowerShares DB U.S. Dollar Bullish Fund. Ours: the prices and volumes, read by eye.",
            left=Content(
                title="A reversal bar at a bottom",
                lines=(
                    "The dollar fund in 2010: a narrow range candlestick on high volume, circled at a low around the start of November [1].",
                    "The volume bars under the circle are among the chart's tallest. Price then rebounds [2], from about 22.0 to about 23.5 within the month.",
                ),
                accent="The converse case: in a decline, a high volume reversal bar is bullish.",
            ),
            picture=Figure(
                number="6.32",
                shows="The daily PowerShares DB U.S. Dollar Bullish Fund with a narrow range candlestick on high volume circled at a low at the start of November, followed by a strong rise.",
                aspect=2.145,
                marks=(
                    Mark(1, "circle", 0.10, 0.79, 0.215, 0.99, at=(0.110, 0.800)),
                    Mark(2, "arrow", 0.20, 0.74, 0.355, 0.17, at=(0.200, 0.680)),
                ),
            ),
            text_w=5.8,
            notes=(
                "Find the circle at the low. The volume bars under it are some of the tallest on the chart.",
                "Converse is the book's word: in a downtrend the same bar is bullish.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.33, the dollar fund. Ours: prices read by eye. The MACD: met in Chapter 4, not taught. The RSI panel and the two moving averages are not discussed.",
            left=Content(
                title="More reliable inside the larger trend",
                lines=(
                    "The dollar fund, 2011: a larger downtrend [1], about 23.4 in January to 21.0 in May. A short rally ends at a circled high volume reversal bar [2], May 23.",
                    "Before it, bearish divergence [3]: price rising while volume fell, and the MACD too.",
                    "Bearish, the larger trend's way: potentially more reliable, the book says. Prices then fell.",
                    "[4] X, early May: a high volume continuation bar.",
                ),
                accent="Agreeing with the larger trend: more reliable.",
            ),
            picture=Figure(
                number="6.33",
                shows="The daily dollar fund in a long decline: a circled high volume reversal bar at a short rally's top in late May, falling lines over volume and the MACD before it, and a continuation bar at X.",
                aspect=1.246,
                marks=(
                    Mark(1, "arrow", 0.17, 0.25, 0.70, 0.66, at=(0.170, 0.190)),
                    Mark(2, "circle", 0.80, 0.47, 0.92, 0.59, at=(0.810, 0.480)),
                    Mark(3, "box", 0.76, 0.60, 0.91, 0.72, at=(0.83, 0.765)),
                    Mark(4, "circle", 0.69, 0.57, 0.765, 0.67, at=(0.66, 0.53)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Bearish divergence in volume is Part 1's: price rising into the bar while volume falls.",
                "The MACD is an oscillator the book has not taught. Point at its falling line and leave it there.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.33. Ours: levels read by eye, and the larger trend read as the whole move. The book does not define the larger trend.",
            left=Content(
                title="Why the larger trend matters, with numbers",
                lines=(
                    "Larger, or predominant, trend: the whole move, our reading, as the book gives none. [1] Here, about 23.4 in January down to 21.0 in May.",
                    "[2] The circled high volume reversal bar is bearish, with that fall: potentially more reliable, the book says.",
                ),
                accent="Ask which way the larger trend runs. The book gives no further reason.",
            ),
            picture=Figure(
                number="6.33",
                shows="The daily dollar fund in a long decline from about 23.4 in January to 21.0 in May, with a circled high volume reversal bar at a short rally's top in late May.",
                aspect=1.246,
                marks=(
                    Mark(1, "arrow", 0.17, 0.25, 0.70, 0.66, at=(0.17, 0.19)),
                    Mark(2, "circle", 0.80, 0.47, 0.92, 0.59, at=(0.81, 0.48)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Same figure as the last slide, read for its one sentence of reason: trace the fall at 1 with a finger, then the circle at 2.",
                "The reversal bar points down, the same way as the six-month fall. That agreement is all the book means by more reliable.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.33. Ours: the reading of X, and its length read by eye. The book does not discuss X.",
            left=Content(
                title="X: a continuation bar against the larger trend",
                lines=(
                    "The book: continuation bars, too, are more reliable in the direction of the predominant trend.",
                    "[1] X, our reading, as the book does not say: a high volume continuation bar rising against the larger downtrend, so the less reliable kind.",
                    "Its rally lasted about two and a half weeks before the fall went on.",
                ),
                accent="With the larger trend: more reliable. Against it: less.",
            ),
            picture=Figure(
                number="6.33",
                shows="The daily dollar fund in a long decline, with X marking a high volume continuation bar in early May that rises against the decline.",
                aspect=1.246,
                marks=(
                    Mark(1, "circle", 0.69, 0.57, 0.765, 0.67, at=(0.66, 0.53)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Point at X: a wide bar up on heavy volume, but inside a decline. The book gives no reading of it; this one is ours.",
                "The rally after X ran about two and a half weeks, then the decline resumed: the less reliable kind, as the rule would say.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.34, the dollar fund. Ours: volume and direction read by eye. The book does not say which way price went.",
            left=Content(
                title="A reversal bar at an overextended level",
                lines=(
                    "The dollar fund, end of October 2011: a high volume reversal bar, circled [1].",
                    "Its volume reaches the line across the volume panel [2], about 13 million: the book's historically overextended volume level, Part 2's upper level.",
                    "Historically is not defined; the line runs level with the September peaks, the oval [3]. Price had fallen into the bar, and rose after it.",
                ),
                accent="Two signals agree: the reversal bar, and Part 2's overextended volume.",
            ),
            picture=Figure(
                number="6.34",
                shows="The daily PowerShares DB U.S. Dollar Bullish Fund with a line across the volume panel labelled historically overextended volume level, and a circled reversal bar at the end of October whose volume reaches that line.",
                aspect=2.133,
                marks=(
                    Mark(1, "circle", 0.755, 0.66, 0.845, 0.92, at=(0.765, 0.670)),
                    Mark(2, "line", 0.44, 0.705, 0.93, 0.705, at=(0.93, 0.705)),
                    Mark(3, "circle", 0.51, 0.62, 0.72, 0.81, at=(0.520, 0.630)),
                ),
            ),
            text_w=6.2,
            notes=(
                "The overextended level is Part 2's upper overextended volume level, drawn by eye. Here it runs through the September peaks.",
                "The book says only that the bar sat at the level; which way price went is read off the figure.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.35. The constant volume chart was a Chapter 3 term.",
            left=Content(
                title="Constant volume charts find reversal bars",
                lines=(
                    "Chapter 3: a constant volume chart starts a new bar each time a set volume has traded, so every volume bar is the same height [3].",
                    "So the book finds reversal bars from the bar range alone and its height against the rest of the bars.",
                    "Figure 6.35: a narrow bar [1], sellers taking control; a very tall bar [2], a lack of interest in the rise. Both bearish.",
                ),
                accent="Especially useful for reversal bars on high or low volume.",
            ),
            picture=Figure(
                number="6.35",
                shows="Two sketches of a constant volume chart, all volume bars equal. Left: a rise topped by a narrow bar on relatively high volume. Right: by a very tall bar on relatively low volume. Both bearish.",
                aspect=1.531,
                marks=(
                    Mark(1, "box", 0.265, 0.13, 0.34, 0.245, at=(0.375, 0.19)),
                    Mark(2, "box", 0.835, 0.05, 0.895, 0.60, at=(0.8, 0.3)),
                    Mark(3, "box", 0.11, 0.83, 0.455, 0.995, at=(0.080, 0.790)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Every bar holds the same volume, so a narrow bar is a lot of volume for the price moved, and a tall bar is little volume for it.",
                "That is this part's two reversal bars, read off a chart where volume never changes. The next slide puts numbers on it.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.35, whose labels say relatively high and relatively low volume. Ours: every number, and the per-peso reading.",
            left=Content(
                title="High and low volume when every bar's volume is fixed",
                lines=(
                    "Ours: every bar holds 100,000 shares; a usual bar spans PHP 1.00: 100,000 shares a peso of range.",
                    "[1] A PHP 0.20 bar: 100,000 shares moved price 20 centavos, 500,000 a peso, five times usual. Figure 6.35's label: relatively high volume.",
                    "[2] A PHP 4.00 bar: 100,000 shares over 4 pesos, 25,000 a peso, a quarter of usual. Its label: relatively low volume.",
                ),
                accent="Volume is fixed, so the range alone says if it was a lot or a little.",
            ),
            picture=Figure(
                number="6.35",
                shows="Two sketches of a constant volume chart, all volume bars equal. 1, left: a rise topped by a narrow bar labelled relatively high volume. 2, right: a rise topped by a very tall bar labelled relatively low volume.",
                aspect=1.531,
                marks=(
                    Mark(1, "box", 0.265, 0.13, 0.34, 0.245, at=(0.375, 0.19)),
                    Mark(2, "box", 0.835, 0.05, 0.895, 0.60, at=(0.8, 0.3)),
                ),
            ),
            text_w=6.2,
            notes=(
                "The figure again, for its two labels: 1 is the narrow bar on the left, 2 the tall bar on the right. Every volume bar under them is the same height.",
                "Divide shares by pesos of range, three times: 100,000 over 1.00, over 0.20, over 4.00.",
            ),
        ),
        Check(
            label="Reversal bars on charts",
            picture=Figure(
                number="6.33",
                shows="The daily dollar fund in a long decline from about 23.4 in January to 21.0 in May, with a circled high volume reversal bar at a short rally's top in late May.",
                aspect=1.246,
                marks=(Mark(1, "circle", 0.80, 0.47, 0.92, 0.59, at=(0.810, 0.480)),),
            ),
            text_w=6.6,
            questions=(
                Q(
                    stem="Why is the high volume reversal bar of Figure 6.33 regarded as potentially more reliable?",
                    options=("It formed on a constant volume chart",
                             "It formed within a larger downtrend",
                             "Its volume was the lowest of the year",
                             "It formed on flat volume"),
                    answer="B",
                    reason="The bearish reversal bar occurred within a larger downtrend, the direction of the predominant trend.",
                ),
                Q(
                    stem="On a constant volume chart, potential reversal bars are found from:",
                    options=("The volume bars alone",
                             "The time axis",
                             "The open interest",
                             "The bar range alone and its height against the rest"),
                    answer="D",
                    reason="Volume is fixed for each bar, so reversal bars are identified by bar range and height alone.",
                ),
            ),
        ),
        Pair(
            origin="Book p.200. Ours: the reading of leading, and the chart, on invented prices. Breakout of a trendline: Chapter 5's use of the word.",
            left=Content(
                title="Volume leading price, or price leading volume",
                lines=(
                    "Volume leading price, our reading: volume rises first, price moves after. Most agree price cannot move significantly without volume.",
                    "Price leading volume: price breaks first. Signals need little volume to appear. [1] A small trendline breakout on ordinary volume.",
                    "As the break becomes obvious it invites tremendous volume. [2] Volume more than doubles.",
                ),
                accent="Price moved first: price led volume.",
            ),
            picture=Chart(
                letter="AK",
                shows="An invented share under a falling trendline. At 1 price breaks the trendline by a little, on ordinary volume. At 2 the breakout becomes obvious, price runs and volume surges: price leads, volume follows.",
                marks=(
                    Mark(1, "circle", 0.665, 0.33, 0.745, 0.43, at=(0.675, 0.340)),
                    Mark(2, "box", 0.79, 0.62, 0.98, 0.88, at=(0.975, 0.6)),
                ),
            ),
            text_w=CHART_W,
            notes=(
                "The book asks the question, does volume lead price, and answers both ways.",
                "On the chart, the breakout at 1 comes first and the volume at 2 after it. That order is what price leading volume means.",
            ),
        ),
        Pair(
            origin="Book p.200, one paragraph. Ours: the numbers and the chart, Chart AK's line with its numbers. The book gives no test for when a light volume signal will draw volume in.",
            left=Content(
                title="What price leading volume means for a signal",
                lines=(
                    "Ours: a usual day trades 1.3 million. [1] Price closes PHP 0.80 above a two-month falling trendline, [2] on 1.3 million: an ordinary day.",
                    "By volume alone, nothing happened. But the break shows on every chart: [3] days later, 3 million trade.",
                    "Light volume on a break does not cancel it: watch whether volume follows. The book does not say for how long.",
                ),
                accent="Volume can follow the signal: more often now, the book says, as technical analysis is widely used.",
            ),
            picture=Chart(
                letter="JE",
                shows="An invented share under a falling two-month trendline. 1: price closes PHP 0.80 above the line. 2: that day's volume, 1.3 million, an ordinary day. 3: days later the volume columns rise to about 3 million as price runs.",
                marks=(
                    Mark(1, "circle", 0.675, 0.335, 0.755, 0.435, at=(0.72, 0.495)),
                    Mark(2, "box", 0.70, 0.75, 0.735, 0.88, at=(0.755, 0.715)),
                    Mark(3, "box", 0.80, 0.64, 0.975, 0.88, at=(0.97, 0.595)),
                ),
            ),
            text_w=6.8,
            notes=(
                "Read the chart in the slide's order: the close above the line at 1, the ordinary column under it at 2, the tall gold columns at 3.",
                "Do not turn this into a rule. The book describes the case and gives no test for when a light volume break will draw volume in.",
            ),
        ),
        Pair(
            origin="Book p.200. The hours are the book's; its examples are EURUSD. The chart and the Manila time are ours.",
            left=Term(
                term="Intraday volume cycle",
                plain="Intraday: within one day. Volume swells and fades daily, peaking at about the same hour each day.",
                example="GMT, Greenwich Mean Time: 1:30 to 2:30 p.m. GMT is 9:30 to 10:30 p.m. in Manila. Our chart: reversals at [1] and [3], a continuation at [2].",
                formal="The intraday volume cycle normally peaks around 1:30 p.m. to 2:30 p.m. GMT. At these volume peaks, price will either reverse or continue, but very rarely remain unchanged.",
            ),
            picture=Chart(
                letter="AL",
                shows="Three days of invented hourly bars over their volume. Volume swells to a peak each day between 13:30 and 14:30 GMT, shaded. At the peaks, numbered 1 to 3, price reverses, continues, and reverses again; it does not stay where it was.",
                marks=(
                    Mark(1, "circle", 0.21, 0.355, 0.29, 0.465, at=(0.220, 0.365)),
                    Mark(2, "circle", 0.465, 0.19, 0.545, 0.29, at=(0.475, 0.200)),
                    Mark(3, "circle", 0.80, 0.08, 0.88, 0.19, at=(0.810, 0.090)),
                ),
            ),
            text_w=TERM_CHART_W,
            notes=(
                "This is review question 8: volume cycles, and where you find them. The book's answer is intraday, with the peak at that hour.",
                "Reverse or continue: the peak does not say which. It says something is about to happen.",
            ),
        ),
        Content(
            origin="Book pp.200-201. Ours: the EURUSD prices, the timing and the order levels. EURUSD: the euro priced in US dollars. Bidirectional entry: a Chapter 5 term.",
            title="Using the cycle: when to watch, not which way",
            lines=(
                "The book: the cycle lets us anticipate price action. At the peak hour price will reverse or continue, very rarely stay put.",
                "It does not say which way, so many use a straddle, Chapter 5's bidirectional entry: one order each way.",
                "Ours: EURUSD at 1.3000 before 1:30 p.m. GMT. A buy stop at 1.3020 buys only if price rises to it; a sell stop at 1.2980 sells only if price falls to it.",
            ),
            accent="The book gives no reason for the hour, no distance for the orders, and nothing on the order not filled.",
            notes=(
                "This slide has no picture: it is the book's use of the cycle, with the straddle worked in one market.",
                "The 20-point distance is ours. The book gives no distance for the two orders, and does not say what is done with the one not filled.",
            ),
        ),
        Pair(
            origin="Book pp.200-201 and Figure 6.36. Retest: our plain reading; the book does not define it. The figure's labels and dotted lines are not explained in the text.",
            left=Content(
                title="Volume cycle peaks at support and resistance",
                lines=(
                    "30-minute EURUSD: almost every reversal comes at a peak in tick volume, Part 4's count of trades: the daily spikes in the bottom panel [2].",
                    "Follow the solid line down from Market bottom [1]: it lands on one of the tallest spikes.",
                    "Especially useful when price retests a support or resistance level [3]: comes back to one it turned at before.",
                ),
                accent="Many straddle the peak: catch price either way.",
            ),
            picture=Figure(
                number="6.36",
                shows="A 30-minute EURUSD chart over weeks, with support and resistance lines, a triangle and a channel, over daily volume cycles; price turns at the peaks.",
                aspect=1.948,
                marks=(
                    Mark(1, "circle", 0.345, 0.65, 0.425, 0.75, at=(0.355, 0.660)),
                    Mark(2, "box", 0.02, 0.83, 0.98, 0.975, at=(0.985, 0.9)),
                    Mark(3, "box", 0.45, 0.32, 0.63, 0.56, at=(0.420, 0.280)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Straddle is the book's second name for the bidirectional entry: orders above and below, so either move is caught.",
                "The daily spikes in the volume panel are the cycle. Line a few of them up with turns in price.",
            ),
        ),
        Pair(
            origin="Book pp.201-202 and Figure 6.37. Oversold and the cycle-tuned stochastic are named, not taught: oscillators are the book's Chapter 8. The pip label is not in the text.",
            left=Content(
                title="Trendline retests at volume peaks",
                lines=(
                    "Hourly EURUSD: at the book's 1, 4 and 5 price rebounds off a rising trendline [1], each time at a tick volume peak [2].",
                    "A cycle-tuned stochastic, bottom panel, read oversold there [3]: its line on the lower line, the grey boxes. The book never defines oversold.",
                    "At 2 and 3 the trendline failed: at circles Y and X [4] the stochastic was still mid-panel, not clearly oversold.",
                ),
                accent="Volume peak and oscillator both: the line held.",
            ),
            picture=Figure(
                number="6.37",
                shows="Hourly EURUSD with rising trendlines and retests 1 to 5, daily volume cycles below, and a stochastic panel: oversold under 1, 4 and 5, not at X and Y.",
                aspect=2.036,
                marks=(
                    Mark(1, "line", 0.645, 0.505, 0.955, 0.335, at=(0.645, 0.445)),
                    Mark(2, "box", 0.005, 0.625, 0.995, 0.725, at=(0.985, 0.585)),
                    Mark(3, "box", 0.08, 0.89, 0.95, 0.96, at=(0.050, 0.850)),
                    Mark(4, "box", 0.21, 0.79, 0.60, 0.88, at=(0.180, 0.750)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Match each number to the shaded marks in the bottom panel. The successful retests had the oscillator oversold; the failures did not.",
                "Do not teach the stochastic. Oversold is used as in Part 2: named, not defined here.",
            ),
        ),
        Pair(
            origin="Book p.202 and Figure 6.38, its upper panel. Point and figure, Renko, three line break and equivolume charts were Chapter 3 terms.",
            left=Content(
                title="Volume on non-constant time charts",
                lines=(
                    "Chapter 3: point and figure, Renko and three line break charts are not plotted linearly in time: equal steps along the axis are not equal times.",
                    "That changes the angle of trendlines, channels and chart patterns. Figure 6.38, top: Apple on a standard daily chart, with a trendline [2].",
                ),
                accent="[1] Circled, late May: on the standard chart, price stays above the line.",
            ),
            picture=Figure(
                number="6.38",
                shows="The upper panel of Figure 6.38: Apple on a standard daily chart, a rising trendline under it, and a circle in late May where price stays above the line.",
                aspect=0.797,
                crop=(0.0, 0.0, 0.0, 0.505),
                marks=(
                    Mark(1, "circle", 0.71, 0.42, 0.82, 0.61, at=(0.720, 0.430)),
                    Mark(2, "line", 0.23, 0.905, 0.92, 0.475, at=(0.230, 0.845)),
                ),
            ),
            text_w=6.4,
            notes=(
                "Chapter 3 built these charts. The point here is only what a non-linear time axis does to a line drawn across it.",
                "This is the top half of the book's figure. Find the line first, then the circle: price holds above it.",
            ),
        ),
        Pair(
            origin="Book p.202 and Figure 6.38, its lower panel: the same prices and the same line as the slide before, on an equivolume chart.",
            left=Content(
                title="The same line on the equivolume chart",
                lines=(
                    "Equivolume: each bar covers the same time, but is wider on heavier volume, so its time axis is non-linear too.",
                    "Figure 6.38, bottom: the same Apple prices on an equivolume chart, and the same trendline [2].",
                    "So the same line meets late May at a different place.",
                ),
                accent="[1] Circled, late May: on the equivolume chart, price cuts through the line.",
            ),
            picture=Figure(
                number="6.38",
                shows="The lower panel of Figure 6.38: the same Apple prices on an equivolume chart, the same trendline, and a circle in late May where price cuts through the line.",
                aspect=0.797,
                crop=(0.0, 0.51, 0.0, 0.0),
                marks=(
                    Mark(1, "circle", 0.70, 0.35, 0.82, 0.55, at=(0.710, 0.360)),
                    Mark(2, "line", 0.25, 0.905, 0.84, 0.385, at=(0.250, 0.845)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Same prices, same line as the last slide. Point at the wide bars in early May: heavy days, so wide.",
                "On top price held above the line in late May; here it cuts through. The next slide puts numbers on why.",
            ),
        ),
        Pair(
            origin="Book p.202. Ours: every number and the chart. The book says the angle is affected and shows the result in Figure 6.38; it does not work the arithmetic.",
            left=Content(
                title="Why the trendline moves, with numbers",
                lines=(
                    "Ours: lows of PHP 100 and 110, ten ordinary days apart, one step a day on both charts: the line rises PHP 1.00 a step.",
                    "Then five heavy days: [1] one step each on the daily chart, [2] two each on the equivolume one. The lines reach PHP 115 and PHP 120.",
                    "That day's low of PHP 117 holds above the daily line and cuts the equivolume one. Equal widths would move nothing.",
                ),
                accent="The book shows the discrepancy, not which break to trust.",
            ),
            picture=Chart(
                letter="JG",
                shows="The same trendline, rising PHP 1.00 a step from a low of 100 through a low of 110, on two charts. 1, daily: five heavy days take one step each and a low of 117 lands at step 15, above the line at 115. 2, equivolume: the same five days take two steps each and the low of 117 lands at step 20, under the line at 120.",
                marks=(
                    Mark(1, "circle", 0.695, 0.105, 0.765, 0.195, at=(0.84, 0.06)),
                    Mark(2, "circle", 0.885, 0.535, 0.955, 0.635, at=(0.965, 0.675)),
                ),
            ),
            text_w=6.8,
            notes=(
                "Count the steps on the chart: 15 on the daily chart at 1, 10 plus 10 on the equivolume chart at 2. The grey boxes are the five heavy days.",
                "If heavy days fell between the two lows instead, the line's angle itself would change, which is the book's word: angle.",
            ),
        ),
        Check(
            label="Volume cycles and the time axis",
            questions=(
                Q(
                    stem="The book says the intraday volume cycle normally peaks around:",
                    options=("The market open",
                             "1:30 p.m. to 2:30 p.m. GMT",
                             "The market close",
                             "Midnight GMT"),
                    answer="B",
                    reason="The intraday volume cycle normally peaks around 1:30 p.m. to 2:30 p.m. GMT.",
                ),
                Q(
                    stem="Why may a trendline be violated at a different point on an equivolume chart than on a standard chart?",
                    options=("Equivolume charts ignore volume",
                             "Equivolume charts use closing prices only",
                             "Bar width varies with volume, so the time axis is non-linear",
                             "Equivolume charts are not constant time"),
                    answer="C",
                    reason="Bars are constant time but their width varies with volume, so the time axis is non-linear and a line's angle changes.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Part 6 - 6.2, pp.203 to 208: the volume oscillators.
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Volume Oscillators",
    short="6.2 Oscillators",
    minutes="",
    covers=(),
    slides=(
        Content(
            origin="Book p.203 lists the eight. p.179 sorts the price-based ones and p.206 the NYSE line; the VWMA is on neither list.",
            title="6.2  Volume oscillators, and how they are read",
            lines=(
                "An oscillator (Part 1): an indicator in its own panel under price. Section 6.2 names eight built from volume.",
                "Price-based: the OBV, the ADL, the Chaikin Money Flow and Oscillator, the Herrick Payoff Index, the Demand Index (never explained).",
                "Non-price-based: the NYSE Up/Down Volume Line. The eighth, the VWMA (Part 2), is on neither of Part 1's lists.",
            ),
            accent="Plain volume diverges by falling; price-based, against price.",
            notes=(
                "The book gives the list without a figure, so this slide has no picture. Say the names and the kind of each.",
                "Part 1's rule: on plain volume, divergence is volume falling; on a price-based oscillator, it is the oscillator moving against price.",
            ),
        ),
        Pair(
            origin="Book p.203 lists the eight methods and sends them to Chapter 8; p.206 reads the oversold level. The chart is ours, invented.",
            left=Content(
                title="Eight ways to read an oscillator; three used here",
                lines=(
                    "Eight methods, taught in Chapter 8, listed below. Part 6 uses only three:",
                    "A  Price, a higher peak; oscillator, a lower one. Against price: divergence. Falling: bearish. Price then falls (method 4).",
                    "B  A rising line under the oscillator; falling through it is a sell signal (the Chaikin pair, later). No method is named.",
                    "C  An oversold level (method 1): a potential bottom, the book says (p.206). It never says how it is set.",
                ),
                caption="The eight: 1 OBOS (overbought and oversold) overextended levels, 2 equilibrium and zero line crossovers, 3 signal line crossovers, 4 price-oscillator divergence, 5 to 7 geometric, numeric and horizontal pattern analysis, 8 oscillator on oscillator.",
            ),
            picture=Chart(
                letter="FA",
                shows="An invented price over an invented oscillator, with the three readings this part uses lettered. A: price makes a higher peak while the oscillator makes a lower one, divergence. B: a rising line drawn under the oscillator's lows, which it then falls through. C: a flat line low in the oscillator panel, labelled oversold, which the oscillator touches at the price low.",
            ),
            text_w=7.5,
            notes=(
                "Read the letters in order on the chart. A is Part 1's divergence; B and C are the two other readings Figures 6.43 and 6.44 use.",
                "Do not teach the other five methods: the book sends them to Chapter 8.",
            ),
        ),
        Pair(
            origin="Book p.203 gives the rule. The closes and volumes in the example and on the chart are ours.",
            left=Term(
                term="On Balance Volume, OBV",
                plain="A running total of volume: a close above the day before's adds the day's volume; below, subtracts it; the same, nothing.",
                example="Ours: day 2 closes up, add 2.0 million: OBV 2.0. Day 3 down, take 1.5: 0.5. Day 4 unchanged: 0.5. Day 5 up, add 3.0: 3.5. Day 6 down, take 1.0: 2.5.",
                formal="A cumulative running total of each period's volume: added if the close is higher than the preceding close, subtracted if lower, and nothing if unchanged.",
            ),
            picture=Chart(
                letter="AM",
                shows="Six invented days worked through. Top, the closes from 50.00 to 50.60 pesos. Middle, each day's volume, marked plus when the close rose, minus when it fell, and zero when it was unchanged. Bottom, the running total, the OBV: 0, 2.0, 0.5, 0.5, 3.5 and 2.5 million.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Work it with the room, day by day, pointing at the middle panel: the sign comes from the close, the size from the volume.",
                "Only the direction of the close matters, not how far it moved. That is the weakness a few slides on.",
            ),
        ),
        Pair(
            origin="Book p.203 gives the rule and no starting value. The arithmetic and the chart are ours, on Chart AM's six days. The reading rule is Part 1's, Figure 6.7.",
            left=Content(
                title="What the OBV's number says, and which kind it is",
                lines=(
                    "The book sets no start; we start at 0 on day 1, with no day before it. [1] Up days: 2.0 + 3.0 = 5.0 million; [2] down days: 1.5 + 1.0 = 2.5. [3] OBV: 2.5.",
                    "Rising OBV: more volume on up closes than down closes. Falling: the reverse.",
                    "Price-based, as the close sets the sign. Part 1's two questions: rising (bullish) or falling (bearish)? With price (confirmation) or against it (divergence)?",
                ),
                accent="Read it by rises and falls against price, not by level: next slide.",
            ),
            picture=Chart(
                letter="JH",
                shows="The OBV's six invented days. Top: each day's volume signed by its close, the up days gold, 1, adding 2.0 + 3.0 = 5.0, and the down days grey, 2, adding 1.5 + 1.0 = 2.5. Bottom: the running total, ending at 3, 5.0 - 2.5 = 2.5.",
                marks=(
                    Mark(1, "box", 0.20, 0.095, 0.565, 0.165, at=(0.17, 0.13)),
                    Mark(2, "box", 0.555, 0.41, 0.965, 0.48, at=(0.525, 0.370)),
                    Mark(3, "circle", 0.765, 0.60, 0.835, 0.69, at=(0.775, 0.610)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Point at the gold columns for 1, the grey ones for 2, and the last point of the line for 3. Ask the room what day 6 would read had it closed up.",
                "Day 6 closing up would add 1.0 instead of taking it away: 3.5 + 1.0 = 4.5.",
            ),
        ),
        Pair(
            origin="Book pp.203-204: the disadvantage and its consequence are the book's. The chart is ours: the OBV's six days, started twice.",
            left=Content(
                title="The OBV's disadvantage: the start date",
                lines=(
                    "Its level, the book's absolute value, depends on the start date. Start our six days on day 3: day 6 reads 2.0 [2], not 2.5 [1].",
                    "Its changes, the relative value, do not. From day 3 [3] to day 6, both lines rise 2.0: 0.5 to 2.5, 0 to 2.0.",
                    "The book: so all eight methods may still be used. Divergence reads rises and falls.",
                ),
                accent="An OBV reading of 2.5 means nothing alone; a rise or a fall does.",
            ),
            picture=Chart(
                letter="AN",
                shows="The OBV of the six days drawn twice. Started on day 1, it reads 0.5 on day 3 and 2.5 on day 6. Started on day 3, it reads 0 there and 2.0 on day 6. Two lines of the same shape at different heights, each rising 2.0 from day 3 to day 6.",
                marks=(
                    Mark(1, "circle", 0.765, 0.26, 0.835, 0.365, at=(0.875, 0.25)),
                    Mark(2, "circle", 0.765, 0.365, 0.835, 0.455, at=(0.875, 0.38)),
                    Mark(3, "box", 0.40, 0.555, 0.48, 0.735, at=(0.370, 0.515)),
                ),
            ),
            text_w=5.8,
            notes=(
                "Shift the start and the whole line moves up or down, but every rise and fall stays the same.",
                "Absolute value and relative value are the book's words; level and changes are the plain ones.",
            ),
        ),
        Pair(
            origin="Book pp.203-204: the weakness and its example are the book's. The two bars and their numbers are ours.",
            left=Content(
                title="The OBV's weakness: only the close counts",
                lines=(
                    "Volume is added or subtracted regardless of the bar's own behavior.",
                    "Ours: bar 1 has a high of 51.00 and closes 50.80. Bar 2 rallies to a new high of 54.00 [1], far above, and closes 50.70 [2], just under 50.80.",
                    "Bar 2 closed lower, so all its 3.0 million is subtracted [3].",
                ),
                accent="To redress it, that is, to put it right, many prefer the ADL or the two Chaikin indicators: next.",
            ),
            picture=Chart(
                letter="FC",
                shows="Two invented bars and their signed volume. Bar 1, high 51.00, closes 50.80 and adds 2.0 million. Bar 2 makes a new high of 54.00 far above it but closes at 50.70, just under 50.80, and its whole 3.0 million is marked as subtracted.",
                marks=(
                    Mark(1, "circle", 0.575, 0.05, 0.665, 0.15, at=(0.7, 0.07)),
                    Mark(2, "circle", 0.59, 0.31, 0.71, 0.40, at=(0.74, 0.3)),
                    Mark(3, "box", 0.535, 0.685, 0.705, 0.80, at=(0.505, 0.645)),
                ),
            ),
            text_w=6.2,
            notes=(
                "The second bar went far higher and still counts as a down day, because it closed a little lower.",
                "Redress is the book's word: to put right.",
            ),
        ),
        Pair(
            origin="Book p.204 and Figure 6.39. The dollar levels are read off the figure, roughly.",
            left=Content(
                title="OBV bullish divergence: Citigroup",
                lines=(
                    "[1] Price: a lower low, August to October 2011: the falling line.",
                    "[2] OBV: a higher low, same weeks: the rising line.",
                    "Price-based rule: rising, so bullish; against price, so divergence.",
                    "[3] Then, the book: prices rebound strongly, here about 22 to 34 dollars.",
                ),
                accent="On plain volume, bullish divergence is instead volume falling as price falls.",
            ),
            picture=Figure(
                number="6.39",
                shows="The daily chart of Citigroup with an On Balance Volume panel under it. A falling line marks price's lower lows in August to October 2011, and a rising line under the OBV, labelled bullish divergence, marks its higher lows.",
                aspect=1.629,
                marks=(
                    Mark(1, "line", 0.72, 0.555, 0.83, 0.71, at=(0.720, 0.495)),
                    Mark(2, "line", 0.73, 0.955, 0.845, 0.915, at=(0.730, 0.895)),
                    Mark(3, "arrow", 0.835, 0.66, 0.875, 0.37, at=(0.835, 0.600)),
                ),
            ),
            text_w=5.4,
            notes=(
                "A lower low is a low below the last one; a higher low, above it. Point at the two lines: same weeks, opposite directions.",
                "Part 1: divergence is an early indication of a potential reversal. Here the fall did reverse.",
            ),
        ),
        Pair(
            origin="Book p.204 and Figure 6.40. The price levels are read off the figure, roughly.",
            left=Content(
                title="OBV bearish divergence: copper",
                lines=(
                    "[1] First arrow, March to April 2011: equal peaks near 4.5; the OBV falls.",
                    "[2] Second, June to August: price rises from about 4.1 to 4.5; the OBV falls.",
                    "The book calls both bearish divergence: the OBV falls [3] while price holds or rises.",
                    "[4] Prices then fell strongly, the book says: here to about 3.0 by October.",
                ),
                accent="Bearish divergence: price flat or up, the price-based indicator down.",
            ),
            picture=Figure(
                number="6.40",
                shows="The daily chart of copper with an On Balance Volume panel under it. Two arrows mark price holding level and then rising to a peak in 2011 while two arrows under the OBV fall, labelled bearish divergence.",
                aspect=1.787,
                marks=(
                    Mark(1, "box", 0.38, 0.07, 0.50, 0.15, at=(0.350, 0.195)),
                    Mark(2, "box", 0.55, 0.06, 0.69, 0.24, at=(0.520, 0.285)),
                    Mark(3, "box", 0.38, 0.73, 0.73, 0.85, at=(0.350, 0.690)),
                    Mark(4, "arrow", 0.725, 0.22, 0.82, 0.64, at=(0.725, 0.160)),
                ),
            ),
            text_w=5.4,
            notes=(
                "Two divergences, each an arrow on price and an arrow down on the OBV. The first price arrow, March to April, holds level.",
                "Plain volume falling as price rises would also be bearish divergence: this is the case the two kinds read alike.",
            ),
        ),
        Check(
            label="On Balance Volume",
            questions=(
                Q(
                    stem="Today's close is lower than yesterday's, on volume of 3 million shares. The OBV:",
                    options=("Is unchanged",
                             "Rises by 3 million",
                             "Rises by part of 3 million",
                             "Falls by 3 million"),
                    answer="D",
                    reason="If the close is lower than the preceding close, the period's whole volume is subtracted from the running total.",
                ),
                Q(
                    stem="The book's disadvantage of the OBV is that:",
                    options=("Its absolute value depends on the start date",
                             "It cannot show divergence",
                             "It uses open interest",
                             "It ignores volume"),
                    answer="A",
                    reason="Its absolute reading depends on the start date; its relative changes do not, so the eight methods still work.",
                ),
            ),
        ),
        Pair(
            origin="Book pp.204-205 gives the calculation. C, H and L are Chapter 1's OHLC. The bars and their volume are ours.",
            left=Term(
                term="Accumulation Distribution Line, ADL",
                plain="Like the OBV, a running total, but each bar adds a share of its volume set by where it closes in its range.",
                example="Ours: bar PHP 48 to 52, 2 million shares. Close 52: add 2.0. At 50: add 0. At 49: take 1.0.",
                formal="C, H, L: close, high, low. Calculate the multiplying factor [(C - L) - (H - C)] / (H - L) times the period's volume, and add it to its running total: the ADL.",
            ),
            picture=Chart(
                letter="AO",
                shows="Three invented bars, each from 48 to 52 pesos on 2 million shares, worked through. Closing at the high, the factor is 1 and 2.0 million is added. Closing at the midpoint, 50, the factor is 0 and nothing is added. Closing at 49, the factor is minus one half and 1.0 million is subtracted. The ADL runs 2.0, 2.0, 1.0.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "C, H and L are the close, high and low: the OHLC of Chapter 1. The next slide works all three bars.",
                "The name echoes the accumulation and distribution phases of Chapters 2 and 4. The book does not connect the two.",
            ),
        ),
        Pair(
            origin="Book pp.204-205 gives the factor. The bars, volumes, arithmetic and chart are ours, Chart AO's three bars.",
            left=Content(
                title="The ADL worked, bar by bar",
                lines=(
                    "Each bar: low L = 48, high H = 52, range H - L = 4, volume 2.0 million. C - L: the close's height above the low. H - C: its depth below the high.",
                    "[1] Close 52: (4 - 0) / 4 = 1, add 2.0.   [2] Close 50: (2 - 2) / 4 = 0, add nothing.   [3] Close 49: (1 - 3) / 4 = -0.5, take 1.0.",
                    "The running total, bar by bar: 2.0, then 2.0 + 0 = 2.0, then 2.0 - 1.0 = 1.0. That total is the ADL.",
                ),
                accent="The factor scores where the close sits: -1 at the low, 0 at the midpoint, +1 at the high.",
            ),
            picture=Chart(
                letter="JI",
                shows="Three invented bars from 48 to 52, numbered 1 to 3 by their closes, 52, 50 and 49, each with its factor worked under it; the third bar's C - L of 1 and H - C of 3 measured beside it. Below, each factor times 2.0 million, +2.0, 0 and -1.0, and the ADL's running total, 2.0, 2.0, 1.0.",
                marks=(
                    Mark(1, "box", 0.34, 0.03, 0.46, 0.31, at=(0.31, 0.17)),
                    Mark(2, "box", 0.50, 0.03, 0.62, 0.31, at=(0.62, 0.36)),
                    Mark(3, "box", 0.66, 0.03, 0.77, 0.31, at=(0.76, 0.36)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Work bar 3 off the chart: the green measure is C - L, 1; the gold one H - C, 3. So (1 - 3) / 4 = -0.5.",
                "Ask the room for a close at 51: (3 - 1) / 4 = 0.5, so add 1.0 million.",
            ),
        ),
        Pair(
            origin="Book p.205: the algebra and the maximum are the book's. The chart is ours: the factor against where the close sits.",
            left=Content(
                title="How the ADL redresses the OBV",
                lines=(
                    "[1] Midpoint, nothing added: if C - L = H - C, then C = (H + L) / 2. For 48 and 52, 50.",
                    "Further above it, more is added; below it, more subtracted.",
                    "[2] At most the day's volume: at the high, C = H, the factor is (H - L) / (H - L) = 1, however wide the bar.",
                ),
                accent="The ADL accounts for the current bar's price action. The OBV does not.",
            ),
            picture=Chart(
                letter="AP",
                shows="A straight line for the ADL's multiplying factor against where the close sits in its bar: minus 1 when the bar closes at its low, 0 at its midpoint, and plus 1 at its high.",
                marks=(
                    Mark(1, "circle", 0.515, 0.375, 0.595, 0.465, at=(0.525, 0.385)),
                    Mark(2, "circle", 0.845, 0.105, 0.925, 0.195, at=(0.885, 0.27)),
                ),
            ),
            text_w=CHART_W,
            notes=(
                "The line is the whole idea: the factor slides from minus one to plus one as the close moves from the low to the high.",
                "No matter how wide the range, the maximum is the day's volume, not some multiple of it: the book's words.",
            ),
        ),
        Pair(
            origin="Ours: one invented bar and the chart, read by the book's two rules from pp.203 and 205.",
            left=Content(
                title="One bar, two answers: the OBV against the ADL",
                lines=(
                    "Ours: yesterday closed 50.00. Today runs from 46.00 to 51.00 on 2.0 million shares and closes at 49.75.",
                    "[1] OBV: 49.75 is below 50.00, so subtract all 2.0 million.",
                    "[2] ADL: C - L = 3.75, H - C = 1.25, range 5. Factor (3.75 - 1.25) / 5 = 0.5: add 1.0 million.",
                ),
                accent="The OBV sees only yesterday's close; the ADL sees where today closed in today's bar.",
            ),
            picture=Chart(
                letter="JJ",
                shows="Yesterday's bar closing at 50.00, dashed, and today's bar from 46.00 to 51.00 closing at 49.75, with C - L of 3.75 and H - C of 1.25 measured beside it. Beside them, what each adds for today: 1 the OBV, -2.0 million, and 2 the ADL, +1.0 million.",
                marks=(
                    Mark(1, "box", 0.62, 0.40, 0.735, 0.76, at=(0.590, 0.360)),
                    Mark(2, "box", 0.765, 0.21, 0.885, 0.43, at=(0.735, 0.170)),
                ),
            ),
            text_w=6.0,
            notes=(
                "Today closed near the top of its own range, which the ADL counts as buying. The OBV counts only the tiny fall from 50.00, the dashed line.",
                "The two columns are the whole point: one bar, minus 2.0 by one rule, plus 1.0 by the other.",
            ),
        ),
        Pair(
            origin="Book p.205 and Figure 6.41. Price confirmation as Figure 6.44, p.206, labels it.",
            left=Content(
                title="The ADL confirms, volume diverges: EURUSD",
                lines=(
                    "Hourly EURUSD, June 2011: price makes new highs [1].",
                    "[2] ADL, price-based: rising with price, so bullish confirmation.",
                    "[3] Volume, plain: falling as price rises, so bearish divergence: an underlying weakness, the book says.",
                ),
                accent="They disagree: wait for price itself to confirm a reversal, by breaking its own trendline.",
            ),
            picture=Figure(
                number="6.41",
                shows="An hourly EURUSD chart rising to a top, with an A/D line panel rising alongside it, labelled bullish confirmation, and a volume panel falling, labelled bearish divergence, under the heading divergence between volume and ADL.",
                aspect=1.995,
                marks=(
                    Mark(1, "box", 0.53, 0.19, 0.78, 0.36, at=(0.500, 0.150)),
                    Mark(2, "box", 0.54, 0.62, 0.75, 0.70, at=(0.510, 0.580)),
                    Mark(3, "box", 0.46, 0.80, 0.84, 0.95, at=(0.430, 0.760)),
                ),
            ),
            text_w=5.4,
            notes=(
                "The two kinds again, disagreeing: the price-based ADL rises with price, plain volume falls.",
                "The book does not pick one. Taking part, its word, means trading on the signal.",
            ),
        ),
        Pair(
            origin="Book pp.205-206 and Figure 6.42. Regime is the book's word, not defined; the reading of it is ours.",
            left=Content(
                title="OBV and ADL together: trend or range",
                lines=(
                    "Both rising, or both falling: price trends in a decisive manner. Right ellipse [1].",
                    "Opposite directions: price tends to range or consolidate, going sideways. Left ellipse [2].",
                    "Regime: whether the market trends or ranges. Trend-following trades with a trend; range-bound, inside a range.",
                ),
                accent="The book: it may help choose. Together, trend-following; apart, range-bound.",
            ),
            picture=Figure(
                number="6.42",
                shows="The daily chart of Exxon Mobil with OBV and ADL panels. On the left the two move apart, non-confirmation, under an erratic and volatile price; on the right they rise together, confirmation, under a pronounced trend.",
                aspect=1.325,
                marks=(
                    Mark(1, "circle", 0.55, 0.59, 0.89, 0.96, at=(0.560, 0.600)),
                    Mark(2, "circle", 0.02, 0.57, 0.50, 0.99, at=(0.530, 0.960)),
                ),
            ),
            text_w=5.8,
            notes=(
                "Left ellipse: the OBV falls while the ADL rises, and price goes nowhere; the figure calls it a lack of clarity and strength. Right ellipse: both rise, and price trends.",
                "Range or consolidate, the book's words: Chapter 4's consolidation, price going sideways between a high and a low.",
            ),
        ),
        Check(
            label="The ADL",
            questions=(
                Q(
                    stem="A bar closes exactly at the midpoint of its range. What does it add to the ADL?",
                    options=("Its whole volume",
                             "Half its volume",
                             "Nothing",
                             "Minus its whole volume"),
                    answer="C",
                    reason="When C = (H + L) / 2, the factor (C - L) - (H - C) is zero, so nothing is added or subtracted.",
                ),
                Q(
                    stem="The OBV and the ADL move in opposite directions. Price tends to:",
                    options=("Trend decisively",
                             "Range or consolidate",
                             "Make a buying climax",
                             "Gap"),
                    answer="B",
                    reason="When the two move in opposite directions there is a tendency for price to range or consolidate.",
                ),
            ),
        ),
        Pair(
            origin="Book p.206 gives the calculation, not the lengths. The bars and volumes are ours.",
            left=Term(
                term="Chaikin Money Flow and Chaikin Oscillator",
                plain="CMF: add the ADL's signed volumes S over the last N bars, and divide by those bars' total volume.",
                example="Ours, the ADL's three bars, N = 3: S of 2.0, 0 and -1.0 million make 1.0; volumes of 2.0 each make 6.0. CMF = 1.0 / 6.0 = 0.17.",
                formal="S: the multiplying factor times volume. N-period CMF: the sum of S over the sum of volume. Chaikin oscillator: a shorter-term EMA less a longer-term EMA of the CMF's running total.",
            ),
            picture=Chart(
                letter="AQ",
                shows="The Chaikin Money Flow worked on the ADL's three invented bars. Left, each bar's signed volume S: 2.0, 0 and minus 1.0 million, adding to 1.0. Middle, each bar's volume: 2.0 million each, adding to 6.0. Right, the result: 1.0 divided by 6.0, a CMF of 0.17.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "S is the same signed volume as the ADL's: the factor times the bar's volume. N is the number of bars, as in Part 3's lookback.",
                "What the CMF's number means comes next, then the oscillator step by step.",
            ),
        ),
        Pair(
            origin="Ours: arithmetic on the book's p.206 definition and the ADL's factor, p.205, and the chart. The book gives no reading of the CMF's value.",
            left=Content(
                title="What the CMF's number says",
                lines=(
                    "The ADL's factor runs from -1 to +1, so no S exceeds its bar's volume: the CMF also runs from -1 to +1.",
                    "[1] -1: every bar closed at its low. [2] 0: on balance, closes at their midpoints. +1: every bar closed at its high.",
                    "[3] Our 0.17: of 6.0 million traded, a net 1.0 million counts as added: volume came, on balance, with closes above their midpoints.",
                ),
                accent="Our arithmetic. The book reads the CMF only by a line and an oversold level, three slides on.",
            ),
            picture=Chart(
                letter="JK",
                shows="The CMF's range as four columns: 1 at -1, every close at its low; 2 at 0, on balance at the midpoints; 3 our 0.17, 1.0 divided by 6.0, in gold; and +1, every close at its high.",
                marks=(
                    Mark(1, "box", 0.255, 0.385, 0.375, 0.685, at=(0.41, 0.56)),
                    Mark(2, "circle", 0.42, 0.335, 0.50, 0.445, at=(0.46, 0.50)),
                    Mark(3, "box", 0.555, 0.27, 0.665, 0.385, at=(0.61, 0.47)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Our 0.17 sits just above the 0 column: a little more volume counted as added than taken away. Ask what the CMF would be had all three bars closed at their highs: 6.0 / 6.0 = 1.",
                "Do not call a positive CMF bullish on the book's authority: the book does not say so.",
            ),
        ),
        Pair(
            origin="Book p.206 gives the steps, no lengths, no reading of the sign and no EMA formula. The chart is ours: invented CMF values, our EMAs.",
            left=Content(
                title="The Chaikin oscillator, step by step",
                lines=(
                    "1  Each bar's CMF, over its last N bars.",
                    "[2] A running total of the CMF, as for the ADL: black.",
                    "[3] Two EMAs of that total, here over 3 and 10 bars: gold and green.",
                    "[4] Oscillator = shorter EMA - longer EMA, bottom panel. At the dashed lines: 1.0 - 0.5 = +0.5; 0.6 - 0.8 = -0.2.",
                ),
                accent="The oscillator is the gap between the two averages.",
            ),
            picture=Chart(
                letter="FD",
                shows="The Chaikin oscillator's steps on invented bars. Top, the running total of the CMF in black, with its 3-bar EMA in gold and its 10-bar EMA in green. Bottom, the oscillator, the 3-bar EMA less the 10-bar, as columns above and below zero. Two dashed lines mark a bar reading 1.0 less 0.5, plus 0.5, and a bar reading 0.6 less 0.8, minus 0.2.",
                marks=(
                    Mark(2, "arrow", 0.75, 0.06, 0.645, 0.13, at=(0.77, 0.06)),
                    Mark(3, "box", 0.04, 0.10, 0.97, 0.38, at=(0.02, 0.24)),
                    Mark(4, "box", 0.04, 0.58, 0.96, 0.83, at=(0.02, 0.70)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Follow the steps down the chart: the black total, the two averages that trail it, and their gap in the bottom panel.",
                "The gold average follows the total closely, the green one slowly. When the total turns down, gold crosses below green and the oscillator goes negative.",
            ),
        ),
        Pair(
            origin="Book p.206 gives the steps, no EMA formula and no reading of the sign. The reading of the sign is our arithmetic; the chart is Chart FD's invented values.",
            left=Content(
                title="The EMA, and what the oscillator's sign says",
                lines=(
                    "EMA, exponential moving average: a moving average of the last few values, like Part 3's smoothed volume. This chapter never says how it weights them.",
                    "A 3-bar EMA follows the running total closely; a 10-bar one follows it slowly.",
                    "[1] Above 0, the recent average is above the longer one: the total has been rising lately. [2] Below 0, falling. Ours: the book gives no reading of the sign.",
                ),
                accent="Read a label CMF(20) as N = 20, and ChiOsc(3,10) as EMAs of 3 and 10 bars.",
            ),
            picture=Chart(
                letter="JL",
                shows="Chart FD's running total of the CMF in black, its 3-bar EMA in gold hugging it and its 10-bar EMA in green trailing it. Below, the oscillator's columns: 1 gold above 0 while the total rises, 2 grey below 0 while it falls.",
                marks=(
                    Mark(1, "box", 0.35, 0.63, 0.785, 0.79, at=(0.31, 0.7)),
                    Mark(2, "box", 0.07, 0.765, 0.37, 0.84, at=(0.040, 0.725)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Follow the gold line hugging the black and the green one lagging. Where gold is above green, the columns below are gold, 1; where below, grey, 2.",
                "A rising total means the CMFs being added are positive, by the last slides' arithmetic.",
            ),
        ),
        Pair(
            origin="Book p.206 and Figure 6.43. The text gives no settings. Oversold is not defined in this chapter.",
            left=Content(
                title="The Chaikin pair on copper",
                lines=(
                    "[1] Each indicator falls through the rising line under its lows: the sell signal.",
                    "The oscillator falls through first, the CMF later. The dashed arrows run up to the price top near 4.5, early August [2].",
                    "Copper then fell to about 3.0 by October, where both touched the line labelled oversold [3]: a potential bottom, the book says.",
                ),
                accent="The Chaikin oscillator gives the earlier sell, or bearish, signal.",
            ),
            picture=Figure(
                number="6.43",
                shows="The daily chart of copper with a Chaikin oscillator panel and a Chaikin Money Flow panel. Rising lines mark both before a top in August, with dashed arrows to the top, and both panels carry a line labelled oversold that both touch near the October low.",
                aspect=1.278,
                marks=(
                    Mark(1, "box", 0.51, 0.61, 0.73, 0.95, at=(0.480, 0.570)),
                    Mark(2, "circle", 0.61, 0.07, 0.72, 0.18, at=(0.620, 0.080)),
                    Mark(3, "box", 0.775, 0.73, 0.86, 0.955, at=(0.745, 0.690)),
                ),
            ),
            text_w=5.4,
            notes=(
                "Follow the dashed arrows from each panel up to the top near 4.5 in early August: the oscillator's comes first.",
                "Readings B and C of the part's second slide: a line on the indicator, and an oversold level, used and not defined.",
            ),
        ),
        Pair(
            origin="Book p.206. Advancing and declining volume: our reading of the names, as for the TRIN in Part 4. The numbers are ours.",
            left=Term(
                term="NYSE Up/Down Volume",
                plain="Volume traded in NYSE stocks that rose that day, divided by volume in those that fell.",
                example="Ours: 600 million shares in rising stocks, 400 million in falling: 600 / 400 = 1.5. Read like plain volume: falling is divergence, rising confirmation.",
                formal="The ratio of advancing volume over declining volume. Being non-price-based, its divergence is read like volume bars and smoothed and detrended volume.",
            ),
            picture=Chart(
                letter="FB",
                shows="The NYSE Up/Down Volume worked for one invented day in three columns. Advancing volume, 600 million shares in the stocks that rose. Declining volume, 400 million in the stocks that fell. Then 600 divided by 400, a ratio of 1.5.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book gives the ratio and no example; the numbers are ours. Up and down volume were read the same way for the TRIN in Part 4.",
                "Non-price-based: it holds no price of its own, so it is read like plain volume: falling is divergence, rising confirmation; with price, bullish.",
            ),
        ),
        Pair(
            origin="Book p.206 and Figure 6.44. Its line is labelled cumulative and runs below zero, which a ratio cannot; the book does not explain.",
            left=Content(
                title="The NYSE Up/Down Volume on a chart",
                lines=(
                    "[1] Top: the indicator falls through its rising trendline in mid 2011: an early bearish signal.",
                    "[2] Bottom: the NYSE Composite, an index of NYSE share prices, breaks its own line later: price confirmation.",
                    "The book says ratio; the figure's line is cumulative and runs below zero [3]. It does not explain.",
                ),
                accent="The volume line warned first; price confirmed later.",
            ),
            picture=Figure(
                number="6.44",
                shows="Two daily panels, 2009 to 2011: the NYSE Advance-Decline Volume line above, labelled cumulative, breaking its rising trendline at a point marked early bearish signal; and the NYSE Composite Index below, breaking its own trendline later, circled as price confirmation.",
                aspect=1.625,
                marks=(
                    Mark(1, "circle", 0.72, 0.08, 0.81, 0.21, at=(0.730, 0.090)),
                    Mark(2, "circle", 0.785, 0.72, 0.865, 0.86, at=(0.795, 0.730)),
                    Mark(3, "box", 0.04, 0.60, 0.16, 0.71, at=(0.190, 0.560)),
                ),
            ),
            text_w=5.6,
            notes=(
                "The NYSE Composite Index is the price the indicator is read against. The arrow joins the two breaks.",
                "Say the gap plainly: a ratio of two volumes cannot be negative. The book does not reconcile them.",
            ),
        ),
        Term(
            origin="Book pp.207-208. The book gives no formula and no figure for it, so this slide has no picture.",
            term="Herrick Payoff Index",
            plain="Uses price and open interest, so futures and options only. Price-based: rising bullish, falling bearish; against price, divergence.",
            example="Gold futures: yes. A PSE share, with no open interest: no. The book gives no formula.",
            formal="The Herrick Payoff Index uses open interest in its calculations, so it may only be used with futures and options. It incorporates price, so its divergence is read as for all price-based volume oscillators. As with all volume oscillators, bearish signals: money flowing out; bullish: money flowing in.",
            notes=(
                "Price-based, so Part 1's rule: rising is bullish, falling bearish; against price, divergence. It may be read with any or all of the eight methods.",
                "Money flowing out and in are the book's words for what a bearish and a bullish signal indicate.",
            ),
        ),
        Pair(
            origin="Book p.208 gives the report and its two uses. The chart is ours, on invented prices and open interest.",
            left=Term(
                term="Commitment of Traders, COT, report",
                plain="A weekly report of all open positions, listed by who holds them: three groups.",
                example="Ours: open interest returns to its 92,000 peak as price tops: a test of a historical level.",
                formal="Released every Friday, it reports all open positions held by commercials (hedgers, non-cash positions), non-commercials (hedge funds, financial institutions, large traders) and, in aggregate, small traders.",
            ),
            picture=Chart(
                letter="AR",
                shows="An invented futures price rising to a top, with its open interest underneath peaking at 92,000 contracts, falling back, then climbing to a dashed line drawn at that earlier peak. The test of that level, at the price top, is marked: one of the two things the book says traders look for in the report.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Hedgers were named in Chapter 1 among the participants. Commercial and non-commercial are the report's own groups.",
                "A test means open interest coming back to a level it reached before, the way price retests a barrier in Part 3.",
            ),
        ),
        Pair(
            origin="Book p.208. It does not define net or non-cash positions and gives no worked figures. The what-to-do line is ours, from p.205; the chart is ours, invented.",
            left=Content(
                title="What traders read in the COT report",
                lines=(
                    "Commercials: hedgers, holding non-cash positions, a phrase the book never explains.",
                    "The book: traders use it to identify potential tops and bottoms, by two things.",
                    "One: changes in net commercial or non-commercial positions. Net: never defined, so not drawn.",
                    "Two: open interest testing a significant or historical level: back at an old level [1].",
                ),
                accent="Ours: treat either as a warning, and wait for price to confirm [2], as for the ADL.",
            ),
            picture=Chart(
                letter="JM",
                shows="An invented futures price rising to a top over its open interest. 2: open interest climbs back to its earlier peak of 92,000 contracts, dashed, at the price top: a test of a historical level. 3: price then falls away, confirming.",
                marks=(
                    Mark(1, "circle", 0.80, 0.48, 0.88, 0.58, at=(0.810, 0.490)),
                    Mark(2, "circle", 0.905, 0.09, 0.985, 0.21, at=(0.915, 0.100)),
                ),
            ),
            text_w=6.6,
            notes=(
                "Use 1 has no picture because the book never says what net is. Use 2 is on the chart: open interest back at the dashed line.",
                "Commercials are hedgers, Chapter 1's participants; non-commercials are hedge funds, financial institutions and large traders.",
            ),
        ),
        Check(
            label="The other volume oscillators",
            questions=(
                Q(
                    stem="Why may the Herrick Payoff Index only be used with futures and options?",
                    options=("It uses tick volume",
                             "It is non-price-based",
                             "It uses open interest in its calculations",
                             "It is released every Friday"),
                    answer="C",
                    reason="The Herrick Payoff Index uses open interest, which only futures and options have.",
                ),
                Q(
                    stem="On the Chaikin Money Flow, three bars have signed volumes of 3.0, 1.0 and -2.0 million on volumes of 4.0, 2.0 and 2.0 million. The CMF is:",
                    options=("0.25",
                             "2.0",
                             "0.5",
                             "-2.0"),
                    answer="A",
                    reason="The sum of S, 2.0, divided by the sum of volume, 8.0, is 0.25.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# The frame: two opening slides and three closing ones.
# ==========================================================================

OPENERS = (
    Content(
        origin="Book p.173: its six learning objectives, nearly word for word.",
        title="What you will be able to do",
        lines=(
            "Understand volume action and its implications for market action.",
            "Recognize early trend weakness via volume and open interest divergence.",
            "Identify bullish and bearish signals on volume and open interest indicators.",
            "Forecast potential reversals and corrections via volume cycles.",
            "Set up effective volume filtering, for better timed entries and exits.",
            "Read volume across successive contract months in futures markets.",
        ),
        caption="The last is not taught in this chapter's text; Chapter 3 read volume across contract months. Every other idea here gets its own slide when its part comes.",
        notes=(
            "These are the book's six learning objectives. Say the first and the fifth, and that every one is examinable.",
            "Be straight about the sixth: the chapter's text never comes back to contract months. Chapter 3's rollover slides are where it was taught.",
        ),
    ),
    Content(
        origin="The parts are the book's own sub-sections, pp.173 to 208, grouped in its order.",
        title="How this chapter is laid out",
        lines=(
            "Part 1  Confirmation and divergence.  Part 2  Timing, the volume-weighted moving average (VWMA), climaxes.",
            "Part 3  Price barriers and filtering.  Part 4  Open interest, tick volume, the Arms Index (TRIN).",
            "Part 5  Bar range and volume cycles.  Part 6  The volume oscillators, section 6.2.",
        ),
        accent="Parts 1 to 5 are the book's section 6.1, in its order.",
        caption="Bottom right of every teaching slide: the book page it comes from, and whose the numbers are. Lettered charts are ours, invented, drawn where the book gives only words, a sketch or a dense chart. Peso amounts are our examples.",
        notes=(
            "Section 6.1 is thirty pages with twenty sub-headings, so it is five parts here. The marker at the bottom left of every slide says which one we are in.",
            "Say the checks carry no marks. Each question slide is followed by its answers on a slide of their own.",
        ),
    ),
)

CLOSING = (
    Content(
        origin="Book p.208: its summary is three sentences. These five are ours, of the whole chapter, each with the part that teaches it.",
        title="Chapter 6 in five sentences",
        lines=(
            "Part 1: volume with price is bullish volume; against price, bearish.",
            "Part 1: falling volume is divergence, rising confirmation, whatever price does.",
            "Parts 2, 5: minimum volume, extreme volume and reversal bars time the turns.",
            "Parts 3, 4: filters pick out key volume; open interest reads like volume.",
            "Part 6: price-based oscillators diverge by moving against price.",
        ),
        accent="The book: price-based and non-price-based oscillators read differently.",
        notes=(
            "Read all five slowly. This is the summary to copy down.",
            "The book's summary adds that volume divergence and filtering are used throughout the rest of the book.",
        ),
    ),
    Content(
        origin="Book p.208.",
        title="The review questions to prepare",
        lines=(
            "Volume and tick volume: what is the difference? Bearish and bullish volume?",
            "How is volume divergence distinct from standard oscillator divergence?",
            "How would you use volume as a timing indicator?",
            "The various modes of volume filtering?",
            "The relationship between volume, open interest and price?",
            "Absolute or relative volume, which is more useful? Volume cycles: use, where?",
        ),
        caption="The book's eight, shortened to fit six lines. Its full wording, with where each is answered, is on the next two slides.",
        notes=(
            "Read them through. The next slide says where in the deck each is answered.",
            "Question 3 is the one most likely to be answered wrongly: volume divergence ignores price's direction.",
        ),
    ),
    Content(
        origin="Book p.208, the questions word for word. Where each is answered is this course's own map onto the parts of this deck.",
        title="The review questions in full: 1 to 4",
        lines=(
            "1  What is the difference between volume and tick volume? Part 4.",
            "2  Describe bearish and bullish volume. Part 1.",
            "3  How is volume divergence distinct from standard oscillator divergence? Part 1.",
            "4  How would you use volume as a timing indicator? Part 2.",
        ),
        accent="The part after each question is where its answer is taught.",
        notes=(
            "Say each part's name as you read its line, so the room can find the slides again.",
            "Question 3's answer is the slide on standard divergence against volume divergence, in Part 1.",
        ),
    ),
    Content(
        origin="Book p.208, the questions word for word. Where each is answered is this course's own map onto the parts of this deck.",
        title="The review questions in full: 5 to 8",
        lines=(
            "5  Describe the various modes of volume filtering. Part 3.",
            "6  Describe the relationship between volume, open interest, and price. Part 4.",
            "7  Which is more useful, absolute or relative volume? Part 4.",
            "8  How are volume cycles useful and where would you normally find them? Part 5.",
        ),
        accent="The part after each question is where its answer is taught.",
        notes=(
            "Question 5 is the four filters of Part 3; question 8 is the intraday volume cycle of Part 5.",
            "Question 7 is Part 4's opening: relative volume compares, absolute volume measures participation.",
        ),
    ),
    Content(
        origin="This course's own list, drawn from the chapter's slides. The chapter numbers and pages are the book's.",
        title="What the book uses here and teaches later, or never",
        lines=(
            "Not explained in the book's chapter: overbought, oversold, the MACD, the EMA, the tick, the cycle-tuned stochastic, the Bollinger Band and Bandwidth (Part 3 gives the Band a one-line meaning).",
            "Named only: the Demand Index, detrended volume, ROC volume, the PVO.",
            "Sent ahead: oscillator analysis, Chapter 8 (p.203); the classification of divergence, Chapter 9 (p.176); the VWMA's calculation, Chapter 11 (p.181).",
        ),
        accent="Where a slide uses one of these, it says so on the slide.",
        notes=(
            "Be straight with them: this chapter leans on oscillators the book teaches in Chapter 8.",
            "Do not teach any of these today. Each is named where it appears.",
        ),
    ),
    Pair(
        origin="This course's own list. Book p.181 and Figure 6.11 (Part 2). Each is also named on its own slide.",
        left=Content(
            title="Where the book says two different things: the VWMA",
            lines=(
                "Above the VWMA (Part 2): the text calls price potentially bullish, then, a paragraph later, overvalued, where institutions look to sell.",
                "Figure 6.11, the book's VWMA picture, prints price above its line as bullish [1].",
                "Its caption says a VWMA on a daily chart; its own labels say VWAP on 10-minute bars [2].",
            ),
            accent="No check rests on any of these. If asked, give both readings.",
        ),
        picture=Figure(
            number="6.11",
            shows="The SPY on 10-minute bars with its VWAP line: the label price above VWAP, bullish, and the chart's own labels, SPY 10 min and VWAP, top left.",
            aspect=1.724,
            marks=(
                Mark(1, "box", 0.495, 0.09, 0.695, 0.145, at=(0.465, 0.050)),
                Mark(2, "box", 0.0, 0.03, 0.175, 0.095, at=(0.040, 0.140)),
            ),
        ),
        text_w=6.0,
        notes=(
            "Do not pick a side for the book. Say both readings and move on.",
            "Box 2 is the chart's own label: 10 min and VWAP, against a caption that says daily and VWMA.",
        ),
    ),
    Pair(
        origin="This course's own list. Book p.193 and Figure 6.25 (Part 4). Each is also named on its own slide.",
        left=Content(
            title="Where the book says two different things: the TRIN",
            lines=(
                "A bullish TRIN (Part 4): the text calls it overbought. Figure 6.25 labels it TRIN oversold [1].",
                "Its caption says a daily chart; its own label and its time axis say 1-minute bars [2], within one day.",
            ),
            accent="No check rests on either. Name both.",
        ),
        picture=Figure(
            number="6.25",
            shows="The S&P 500 on 1-minute bars over its tick and TRIN panels, with the TRIN's high marked TRIN oversold and the chart's own label, SPX 1 min, top left.",
            aspect=1.382,
            marks=(
                Mark(1, "box", 0.615, 0.81, 0.97, 0.88, at=(0.585, 0.770)),
                Mark(2, "box", 0.015, 0.03, 0.215, 0.07, at=(0.055, 0.115)),
            ),
        ),
        text_w=6.0,
        notes=(
            "The two words are opposites. The book uses both for the same reading and never reconciles them.",
            "Read the time axis aloud: 10:00, 11:00, 12:00. That is one day, not a daily chart.",
        ),
    ),
    Pair(
        origin="This course's own list. Book p.206 and Figure 6.44 (Part 6). Each is also named on its own slide.",
        left=Content(
            title="Where the book says two different things: the NYSE line",
            lines=(
                "NYSE Up/Down Volume (Part 6): the text calls it the ratio of advancing volume over declining volume.",
                "Figure 6.44 labels its line cumulative [1], and the line runs below zero [2], which a ratio of two volumes cannot.",
            ),
            accent="The book does not reconcile them. If asked, give both.",
        ),
        picture=Figure(
            number="6.44",
            shows="The NYSE Advance-Decline Volume line, labelled cumulative top left, dipping below zero in early 2009, over the NYSE Composite Index.",
            aspect=1.625,
            marks=(
                Mark(1, "box", 0.0, 0.035, 0.40, 0.08, at=(0.040, 0.125)),
                Mark(2, "box", 0.04, 0.595, 0.165, 0.71, at=(0.080, 0.555)),
            ),
        ),
        text_w=6.0,
        notes=(
            "A ratio of two volumes is never negative. Point at box 2: the line is below the zero on the scale.",
            "Cumulative, box 1, suggests a running total. The book never says it is one.",
        ),
    ),
    Pair(
        origin="This course's own list. Book pp.176 and 178 and Figure 6.6 (Part 1). Each is also named on its own slide.",
        left=Content(
            title="Where the book says two different things: divergence",
            lines=(
                "Bullish divergence (Part 1): the text says it can only occur in a downtrend.",
                "Yet the book reads periods 4 [1] and 6 [2] of Figure 6.6 as bullish divergence: dips inside a four-year uptrend.",
                "Its caption says a daily chart; its own label says weekly [3].",
            ),
            accent="No check rests on any of these. If asked, give both readings.",
        ),
        picture=Figure(
            number="6.6",
            shows="The SPDR Gold Trust over about four years in ten numbered periods: periods 4 and 6 are dips inside the uptrend, and the label top left says weekly.",
            aspect=1.396,
            marks=(
                Mark(1, "box", 0.525, 0.12, 0.59, 0.28, at=(0.495, 0.080)),
                Mark(2, "box", 0.61, 0.16, 0.67, 0.37, at=(0.580, 0.120)),
                Mark(3, "box", 0.0, 0.035, 0.225, 0.08, at=(0.040, 0.125)),
            ),
        ),
        text_w=6.0,
        notes=(
            "Point at the two boxed dips: the price is falling for a while, but inside a rise from about 40 to 120.",
            "Our reading in Part 1 was a downtrend as price falling, for any stretch, and we said that reading was ours.",
        ),
    ),
    Pair(
        origin="This course's own list, from the book's figures and their captions. Book pp.189-190 and Figure 6.23 (Part 3).",
        left=Content(
            title="Figure captions that disagree: silver or USDJPY",
            lines=(
                "Figure 6.23 (Part 3) is captioned silver.",
                "The text calls 6.23 the same daily chart of USDJPY, then, a sentence on, the Silver market.",
                "The chart's own label, top left [1], names its market; the book never refers to it.",
            ),
            accent="No check rests on it. Read the chart, and name both.",
        ),
        picture=Figure(
            number="6.23",
            shows="A daily chart with a volume filtered channel drawn through numbered turns, X and 1 to 6, and the chart's own label top left.",
            aspect=1.982,
            marks=(
                Mark(1, "box", 0.0, 0.0, 0.215, 0.045, at=(0.040, 0.090)),
            ),
        ),
        text_w=6.0,
        notes=(
            "These are labelling slips in the book, not ideas to learn.",
            "The channel itself was Part 3's subject. Here only the label matters.",
        ),
    ),
    Pair(
        origin="This course's own list, from the book's figures and their captions. Book p.194 and Figure 6.26 (Part 4).",
        left=Content(
            title="Figure captions that disagree: daily or intraday",
            lines=(
                "Figure 6.26 (Part 4) is captioned daily.",
                "Its own label says 1-minute bars [1], and its time axis runs from 10:00 to 3:30 [2]: one day, an intraday chart.",
            ),
            accent="No check rests on it. Read the chart, and name both.",
        ),
        picture=Figure(
            number="6.26",
            shows="The S&P 500 on 1-minute bars over its tick and TRIN panels, the label SPX 1 min top left and a time axis from 10:00 to 3:30.",
            aspect=1.401,
            marks=(
                Mark(1, "box", 0.015, 0.035, 0.215, 0.075, at=(0.055, 0.120)),
                Mark(2, "box", 0.02, 0.955, 0.86, 0.998, at=(0.060, 0.915)),
            ),
        ),
        text_w=6.0,
        notes=(
            "These are labelling slips in the book, not ideas to learn.",
            "Next is Chapter 7, Bar Chart Analysis.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 6",
    title="Volume and Open Interest",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    # The objectives and the roadmap are drawn by OPENERS above, one slide
    # each. These two fields are what the generated frame would have used.
    objectives=OPENERS[0].lines,
    roadmap=OPENERS[1].lines,
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6),
    closing=CLOSING,
    openers=OPENERS,
    title_notes=(
        "Greet the room, then say what today buys them: how to read volume and open interest against price, and the indicators built from them.",
        "Say every idea today has a picture beside it. Where the book drew one it is the book's; the rest are ours.",
    ),
    dividers=False,
)
