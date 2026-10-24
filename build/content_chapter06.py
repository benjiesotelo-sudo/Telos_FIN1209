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
    Chart,
    Check,
    Content,
    Figure,
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
                    "Price is regarded as the best indicator of potential future price behavior.",
                    "Volume and open interest offer additional evidence to corroborate bullish or bearish setups.",
                    "They can show underlying weakness, and work as timing indicators for potential breakouts.",
                ),
                accent="Many novices misread declining volume as a weakness in a consolidation.",
                caption="Why that is a misreading: Part 2. Volume is defined two slides on, open interest in Part 4.",
            ),
            picture=Chart(
                letter="A",
                shows="An invented share drawn the way the book's figures draw a chart: price bars in the upper panel and, in the lower panel, one volume bar for each price bar, standing directly under it. One day is picked out in gold in both panels, its close and its volume labelled.",
            ),
            text_w=CHART_W,
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
                    "Chapter 2: under Dow Theory, volume should expand in the direction of the trend.",
                    "Uptrend: volume rises as price rises and falls in downside retracements: bullish volume action.",
                    "Downtrend: volume rises as price declines and falls in upside retracements: bearish volume action.",
                ),
                accent="Volume is a supporting, or secondary, indicator.",
                caption="Volume action contrary to this: an uptrend may potentially be bearish, a downtrend bullish.",
            ),
            picture=Figure(
                number="6.1",
                shows="Two sketches of volume confirming a trend. Top: a rising price with volume bars that grow on the rise and shrink in the downside retracement, labelled bullish volume action in an uptrend. Bottom: a falling price with volume that grows on the fall and shrinks in the upside retracement, labelled bearish volume action in a downtrend.",
            ),
            text_w=6.2,
            notes=(
                "A recall: Chapter 2 gave this as its sixth tenet, with the same four conditions. Nothing in it changes.",
                "Read the figure's two halves. In each, the tall volume bars sit under the move that goes with the trend, and the short ones under the retracement.",
                "What is new today is the vocabulary on the next slides: volume is bullish or bearish, and it confirms or diverges.",
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
            origin="Book p.174: its two basic principles, nearly word for word. The chart is ours, on invented prices.",
            left=Content(
                title="Two principles: rising and declining volume",
                lines=(
                    "1  Rising volume: participants want to see price go higher in an uptrend, lower in a downtrend, and will buy higher or sell lower to take part.",
                    "2  Declining volume: they are losing interest, would rather buy lower in an uptrend or sell higher in a downtrend, if not exiting.",
                ),
                accent="Volume measures participation: how many want to take part in the move.",
            ),
            picture=Chart(
                letter="C",
                shows="An invented uptrend over its volume. In the first rally, numbered 1, volume rises as participants buy higher to take part. In the last rally, numbered 2, price still rises but volume declines as they lose interest.",
            ),
            text_w=CHART_W,
            notes=(
                "The book says to remember these two whenever volume is studied. Every reading later in the chapter comes back to them.",
                "On the chart, 1 is a rally the market wants: volume grows as price rises. 2 is a rally fewer want: price still rises, on shrinking volume.",
            ),
        ),
        Pair(
            origin="Book pp.174-175 states it for an uptrend, then a downtrend. Joined into one line here: our summary of its four sentences.",
            left=Term(
                term="Bullish volume and bearish volume",
                plain="Bullish volume moves with price. Bearish volume moves against it.",
                example="A share rallies on rising volume and dips on falling volume: bullish both times. Falling on rising volume, bouncing on falling volume: bearish.",
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
        Pair(
            origin="Book p.175 and Figure 6.2.",
            left=Content(
                title="Rising volume is not always bullish",
                lines=(
                    "Declining volume does not necessarily imply bearishness. Rising volume does not imply bullishness.",
                    "The bullish or bearish sentiment of volume depends on the direction of the price.",
                    "Figure 6.2: volume expands with gold's primary bull trend and declines in the retracement. Bullish, both times.",
                ),
                accent="The book calls the opposite reading a simple mistake many novices make.",
            ),
            picture=Figure(
                number="6.2",
                shows="The continuous daily chart of gold from 1989 to 2013: a primary bull trend from 2001, its volume expanding in the direction of the trend, and volume declining in the retracement at the end, labelled bullish.",
            ),
            text_w=5.6,
            notes=(
                "Point at the end of the chart: price falls and volume falls with it. That is bullish volume in an uptrend, not a warning.",
                "The mistake is reading volume alone: falling equals bad. Ask the room which way price was going first.",
            ),
        ),
        Pair(
            origin="Book p.175 and Figure 6.3.",
            left=Content(
                title="Volume that does not confirm the trend",
                lines=(
                    "Uptrend: volume decreases as price rises and increases in downside retracements. Bearish volume: a potentially weak or bearish uptrend.",
                    "Downtrend: volume decreases as price falls and increases in upside retracements. Bullish volume: a potentially bullish downtrend.",
                ),
                accent="The trend goes one way and its volume says the other.",
            ),
            picture=Figure(
                number="6.3",
                shows="Two sketches of volume not confirming a trend. Top: a rising price whose volume shrinks on the rise and grows in the retracement, labelled bearish volume action in an uptrend. Bottom: a falling price whose volume shrinks on the fall and grows in the upside retracement, labelled bullish volume action in a downtrend.",
            ),
            text_w=5.8,
            notes=(
                "Set this beside Figure 6.1. The prices are the same shapes; only the volume is swapped.",
                "Not confirming is still only a potential: the book says weak or bearish uptrend, not a reversal.",
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
                    reason="Volume and price declining together is bullish volume, whatever the volume does on its own.",
                ),
                Q(
                    stem="Volume rises while price declines in a preexisting downtrend. The book calls this:",
                    options=("Bullish volume action",
                             "A potentially bullish downtrend",
                             "Volume that does not confirm the trend",
                             "Bearish volume action, confirming the downtrend"),
                    answer="D",
                    reason="Volume expanding in the direction of a downtrend is bearish volume action: it confirms the trend.",
                ),
            ),
        ),
        Pair(
            origin="Book p.175 defines both. The chart is ours: sketches, not prices.",
            left=Term(
                term="Volume divergence and volume confirmation",
                plain="Volume falling is divergence. Volume rising is confirmation, also called convergence.",
                example="Price rises from PHP 40 to PHP 46 as volume shrinks from 3 to 1 million a day: divergence. Had it grown to 5 million: confirmation.",
                formal="Volume divergence occurs whenever volume declines, irrespective of the direction of price. Volume convergence or confirmation occurs whenever volume rises, irrespective of the direction of price.",
            ),
            picture=Chart(
                letter="E",
                shows="Four small cases in two columns. Left column, volume divergence: volume bars falling, once under a rising price and once under a falling price. Right column, volume confirmation: volume bars rising, once under a rising price and once under a falling price.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Read the columns of the chart, not the rows: each column is one volume direction, with price going both ways.",
                "Bullish or bearish volume needs price. Divergence or confirmation does not: it is volume's direction alone.",
            ),
        ),
        Pair(
            origin="Book pp.175-176. The chart is ours, on invented prices.",
            left=Content(
                title="What divergence and confirmation say",
                lines=(
                    "Divergence: participants are not interested in seeing price go further. Bearish for an uptrend, bullish for a downtrend.",
                    "Confirmation: they are interested in taking part in the move. Bullish for an uptrend, bearish for a downtrend.",
                ),
                accent="Confirmation is an early indication of a potential continuation; divergence, of a potential reversal.",
                caption="The book: divergence always indicates potential weakness in an existing trend, confirmation always potential strength.",
            ),
            picture=Chart(
                letter="F",
                shows="Two invented uptrends side by side. Left: volume rises with price, confirmation, and the trend continues. Right: volume falls as price rises, divergence, and price turns down at the end.",
            ),
            text_w=CHART_W,
            notes=(
                "Confirmation is called convergence too: price and volume coming together in one direction. Both words mean volume rising.",
                "The right-hand chart is one possible ending, drawn to show what potential reversal means. Divergence is an early warning, not a certainty.",
            ),
        ),
        Pair(
            origin="Book pp.176-178 and Figure 6.4. The four names are its p.178 summary. The ATR on the figure is in no sentence of the text.",
            left=Term(
                term="Bullish and bearish divergence and confirmation",
                plain="Four names: is volume falling or rising, and does it move with price or against it?",
                example="Both falling: bullish divergence. Both rising: bullish confirmation. Volume down, price up: bearish divergence. Volume up, price down: bearish confirmation.",
                formal="Bullish divergence can only occur in a downtrend, a potential upside reversal; bearish divergence only in an uptrend, a potential downside reversal.",
            ),
            picture=Figure(
                number="6.4",
                shows="Four columns, each a price path over a supporting series. Bearish divergence: price rising, the supporting series falling. Bullish confirmation: both rising. Bearish confirmation: price falling, the supporting series rising. Bullish divergence: both falling. The supporting series is listed as volume bars, a volume moving average, open interest, and the ATR in brackets.",
            ),
            text_w=6.8,
            notes=(
                "The example row is the book's own summary of all four scenarios, page 178. The formal row is its two sentences on where each divergence can occur.",
                "Bullish or bearish comes from the last slide but one: together or apart. Divergence or confirmation from the last slide: volume down or up.",
                "The figure lists four kinds of supporting series. Volume, its moving average and open interest are all in the text; the ATR is not mentioned anywhere in it.",
            ),
        ),
        Pair(
            origin="A recall of this course's Chapters 4 and 5, against the book's p.176. The chart is ours, on invented prices.",
            left=Content(
                title="Not the divergence Chapters 4 and 5 drew",
                lines=(
                    "Chapters 4 and 5: standard divergence. Price makes a higher peak while an oscillator, the MACD or the bar stochastic, makes a lower one.",
                    "Volume divergence is volume declining, whatever price does.",
                    "Price's direction still decides bullish or bearish.",
                ),
                accent="Volume has no reverse divergence classification.",
                caption="Chapter 4 gave the volume case: falling price on decreasing volume. Reverse divergence: Chapter 9.",
            ),
            picture=Chart(
                letter="G",
                shows="Two invented charts side by side. Left, standard divergence as Chapters 4 and 5 drew it: price makes a higher second peak while an oscillator below makes a lower one, peak against peak. Right, volume divergence: price rises and the volume bars under it shrink, with no peaks compared.",
            ),
            text_w=CHART_W,
            notes=(
                "Same word, different test. Standard divergence compares two peaks on two lines. Volume divergence asks one question: is volume falling?",
                "This answers review question 3, how volume divergence differs from standard oscillator divergence.",
                "Reverse divergence was named in Chapter 5 and left to Chapter 9. The book says there is no such classification for volume.",
            ),
        ),
        Pair(
            origin="Book p.177 and Figure 6.5. Rounding bottom: named in Chapter 4. Chapter 4's Figure 4.18 was an intraday chart of this stock too.",
            left=Content(
                title="Bullish volume divergence: Isis Pharmaceuticals",
                lines=(
                    "Isis Pharmaceuticals traces out a bullish rounding bottom.",
                    "As price falls, volume falls with it, twice: bullish volume divergence.",
                ),
                accent="Divergence provides additional evidence of a bullish chart formation.",
                caption="The chart's own note: Isis penetrated the previous day's close though the Dow Jones Industrial Average fell 219 points.",
            ),
            picture=Figure(
                number="6.5",
                shows="An intraday chart of Isis Pharmaceuticals: price falls steeply and curves into a larger rounding bottom pattern, and the volume panel under it carries two dashed lines falling to the right, each labelled bullish volume divergence.",
            ),
            text_w=5.6,
            notes=(
                "Price falling and volume falling together: bullish divergence, by the last slides. Point at the two dashed lines in the volume panel.",
                "Evidence, not a signal: the pattern is the setup and the volume corroborates it, which is the chapter's first sentence again.",
            ),
        ),
        Pair(
            origin="Book p.178 and Figure 6.6. Its caption says a daily chart; the chart itself is labelled weekly.",
            left=Content(
                title="Ten periods of bullish volume: gold",
                lines=(
                    "Periods 1, 3, 7 and 9: bullish confirmation. 4 and 6: bullish divergence. 5: volume flat.",
                    "2, 8 and 10: volume declines in a consolidation, timing the breakout (why: Part 2).",
                ),
                accent="At the end of 2, 8 and 10, price breaks out as volume reaches its minimum.",
                caption="The book says bullish divergence occurs only in a downtrend; 4 and 6 are dips in this uptrend. Our reading, price falling for any stretch: no check rests on it.",
            ),
            picture=Figure(
                number="6.6",
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
            origin="Ours: Figure 6.6's readings on one invented uptrend, so each period can be seen. The periods' lengths and volumes are ours.",
            left=Content(
                title="Our example: one uptrend, period by period",
                lines=(
                    "1  Price rises, volume rises: bullish confirmation.",
                    "2  Price dips, volume falls: bullish divergence.",
                    "3  Price moves sideways, volume falls to its minimum: a consolidation.",
                    "4  Price breaks out and rises, volume rises: bullish confirmation.",
                ),
                accent="1, 2 and 4 are bullish volume. In 3 price moves sideways: no reading, Part 2.",
            ),
            picture=Chart(
                letter="H",
                shows="An invented uptrend over its volume, split by dashed lines into four numbered periods: 1 a rise on rising volume, bullish confirmation; 2 a dip on falling volume, bullish divergence; 3 a sideways range with volume falling to its minimum, a consolidation; 4 a breakout and rise on rising volume, bullish confirmation.",
            ),
            text_w=CHART_W,
            notes=(
                "The book's figure has ten periods on a real chart and they are hard to see. Here are four, one of each kind it names.",
                "Ask the room for each period before reading the label: which way is price, which way is volume, together or apart.",
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
            origin="Book pp.178-179 defines both. The chart is ours, on invented prices; its OBV line is computed by the rule taught in Part 6.",
            left=Term(
                term="Price-based and non-price-based volume oscillators",
                plain="Oscillator: an indicator in a panel under price. Non-price-based: volume only. Price-based: price built in.",
                example="Volume bars count shares. A line adding volume on up closes, subtracting on down closes, uses price.",
                formal="Price-based volume oscillators incorporate price data in their construction, whereas non-price-based volume oscillators only incorporate volume data in their construction.",
            ),
            picture=Chart(
                letter="I",
                shows="Three panels over one invented stretch of price. The price line; under it the volume bars, built from volume alone, non-price-based; and under those a line that adds each day's volume when the close rises and subtracts it when the close falls, which needs price, price-based.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Oscillator is the book's word for any indicator drawn in its own panel under the price. Chapter 8 is oscillators; nothing more about them is needed today.",
                "The bottom line on the chart is the On Balance Volume, taught in Part 6. Here it only shows what price-based means: the close decides the sign.",
                "Volume bars are on the book's non-price-based list, so plain volume counts as one of these oscillators.",
            ),
        ),
        Content(
            origin="Book p.179: its two lists, as printed. Where each is taught is this course's note.",
            title="The book's two lists",
            lines=(
                "Price-based: On Balance Volume (OBV), Accumulation/Distribution Line (ADL), Chaikin Money Flow, Chaikin Oscillator, Demand Index, Herrick Payoff Index.",
                "Non-price-based: standard volume bars, smoothed volume, detrended volume, rate of change of volume (ROC volume), percentage volume oscillator (PVO).",
            ),
            accent="Reading divergence on one kind differs from reading it on the other.",
            caption="Taught later: OBV, ADL, the two Chaikin indicators and the Herrick index in Part 6, smoothed volume in Part 3. The Demand Index, detrended volume, ROC volume and the PVO are named and never explained.",
            notes=(
                "The book gives these as two lists and no figure, so this slide has no picture. The next two slides show how the two kinds are read.",
                "Do not explain the four the book never explains. Say they are names only.",
            ),
        ),
        Pair(
            origin="Book p.179 and Figure 6.7. The last line is our summary of the figure's eight arrows.",
            left=Content(
                title="Reading divergence on the two kinds",
                lines=(
                    "Bearish divergence and bullish confirmation are read the same way on both kinds.",
                    "Bullish divergence: price falls. Volume falls on a non-price-based one; a price-based one rises.",
                    "Bearish confirmation: price falls. Volume rises on a non-price-based one; a price-based one falls.",
                ),
                accent="A price-based oscillator diverges by moving against price; plain volume, by falling.",
            ),
            picture=Figure(
                number="6.7",
                shows="Eight pairs of arrows, a price arrow over a volume arrow, in four boxes: divergence and confirmation, each for non-price-based and price-based volume oscillators. The two kinds differ only in bullish divergence and bearish confirmation, where the price-based volume arrow points the other way.",
            ),
            text_w=5.8,
            notes=(
                "Go box by box. Top left and top right differ only in the bullish divergence pair; bottom left and bottom right only in the bearish confirmation pair.",
                "Why the price-based one differs: price is built into it, so when price falls it would fall too, unless buying is underneath. Ours, not the book's words: the book gives the figure and no reason.",
            ),
        ),
        Pair(
            origin="Book p.180 and Figure 6.8. PVO and detrending are on the figure and not explained by the book.",
            left=Content(
                title="Both kinds on one chart",
                lines=(
                    "Volume and smoothed volume, non-price-based: bearish divergence as the euro trust rises.",
                    "The detrended PVO, non-price-based: bearish divergence too.",
                    "The ADL, price-based: bullish confirmation, rising with price.",
                ),
                accent="The same rise, read two ways: each kind by its own rule.",
            ),
            picture=Figure(
                number="6.8",
                shows="A daily chart of the Currency Shares Euro Trust rising, with three panels under it: volume with a smoothed line, labelled bearish divergence; a detrended volume oscillator, the PVO, also labelled bearish divergence; and the accumulation distribution line, labelled bullish confirmation.",
            ),
            text_w=7.0,
            notes=(
                "Price rises across the arrow at the top. Two volume panels fall under it, bearish divergence; the ADL rises with it, bullish confirmation.",
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
                    reason="On a price-based oscillator, bullish divergence is price falling while the oscillator rises.",
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
            origin="Book p.180: the reason is the book's. Stop orders: Chapters 1 and 5. The chart is ours, on invented prices; where the stops sit is our drawing of the book's sentence.",
            left=Content(
                title="6.1  Volume as a timing indicator",
                lines=(
                    "When volume nears its lowest historical level, a breakout from the consolidation is expected.",
                    "Why: most who wanted to buy have bought; most who wanted to sell have sold.",
                    "Stop orders build up above and below the range: once triggered, the catalyst.",
                ),
                accent="No divergence reading in a range: price moves sideways.",
                caption="So falling volume in a range is not weakness. Breakout here: out of a range, as in Chapters 2 and 4.",
            ),
            picture=Chart(
                letter="J",
                shows="An invented share ranging sideways in a box, with rows of buy stops marked above the box and sell stops below it. Under it the volume falls through the range to its lowest level, a dashed line. At 1 volume tests that level; at 2 price breaks out of the top of the box and volume surges.",
            ),
            text_w=CHART_W,
            notes=(
                "This answers the novice error from the first slide. Sideways price cannot diverge from anything, so shrinking volume inside a range is not a warning: it is the clock running down.",
                "The stops are stop orders, Chapter 1 and Chapter 5: buy stops above the range, sell stops below it. Whichever side is hit first starts the move.",
                "The book says either an upside or a downside breakout. Low volume does not say which way.",
            ),
        ),
        Pair(
            origin="Book pp.180-181 and Figure 6.9.",
            left=Term(
                term="Low volume breakout signal",
                plain="Volume sinks to its lowest level inside a range: expect price to leave the range soon, either way.",
                example="Figure 6.9: Apple ranges in an accumulation, the box, while volume falls to its lowest level. Price then breaks out of the box, upward.",
                formal="Whenever the volume is testing a significant minimum or its lowest historical levels, a breakout is expected. We refer to this as a low volume breakout signal.",
            ),
            picture=Figure(
                number="6.9",
                shows="A daily Apple chart with a low volume level drawn across its volume panel. Circles mark two low volume reversals at time lines 1 and 2, a bearish divergence and a bearish confirmation, and later an accumulation box that price leaves on a low volume breakout signal.",
            ),
            text_w=7.2,
            notes=(
                "Find the box at the bottom right of the price panel, then the circle under it where volume sits on the low volume level. The breakout follows.",
                "The figure also labels a bearish divergence into the top and a bearish confirmation on the fall: Part 1's names on a real chart. The two circles at 1 and 2 are the next slide.",
            ),
        ),
        Pair(
            origin="Book p.180 gives the term; Figure 6.9 (p.181) has two. The chart is ours, on invented prices, because that figure is dense.",
            left=Term(
                term="Low volume reversal",
                plain="Price turns while volume sits at its minimum.",
                example="Figure 6.9 turns twice on low volume, at time lines 1 and 2. On our chart: at 1 a peak, at 2 a trough, each as volume touches its low level.",
                formal="There is a tendency for price to reverse when volume is at its minimum or lowest historical levels. We refer to such reversals as low volume reversals.",
            ),
            picture=Chart(
                letter="K",
                shows="An invented price that rises to a peak, falls to a trough and rises again, over its volume. A dashed low volume level runs across the volume panel. At 1, the peak, and at 2, the trough, volume touches the level and price turns.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Two uses of the same low volume: in a range it times a breakout, in a trend it marks a turn.",
                "The book gives a tendency and no rule for where the low volume level goes. Figure 6.9 draws it by eye, and so does this chart.",
            ),
        ),
        Pair(
            origin="Book p.181 and Figure 6.10.",
            left=Content(
                title="Breakouts at the lowest volume: silver",
                lines=(
                    "Three consolidation breakouts, each as the lowest or minimum volume level is tested.",
                    "Volume increases on the breakout bars, bars 1, 2 and 3.",
                ),
                accent="Volume falls into the breakout, then surges on it.",
            ),
            picture=Figure(
                number="6.10",
                shows="The daily iShares Silver Trust with three consolidations boxed and a low volume threshold drawn across the volume panel. Dotted arrows show volume falling to the threshold in each box, and the breakouts at bars 1, 2 and 3 follow, with volume rising on each breakout bar.",
            ),
            text_w=5.4,
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
            origin="Book p.181. It defers the calculation to Chapter 11. The chart is ours, on invented prices; its line is a 10-bar VWMA we computed.",
            left=Term(
                term="Volume-weighted moving average, VWMA",
                plain="A line of average price on the chart, weighted by volume as its name says. Chapter 11 says how.",
                example="A share at PHP 52, above its VWMA at PHP 50: potentially bullish. At PHP 48, below it: potentially bearish.",
                formal="A VWMA may be created to track overvalued and undervalued stock. Typically, price is considered potentially bullish when it is above the VWMA, and bearish when below it.",
            ),
            picture=Chart(
                letter="L",
                shows="An invented price line with its volume-weighted moving average drawn over it as a green line. Where price crosses above the line it is labelled potentially bullish, and where it crosses below, potentially bearish.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book's heading is Volume-Weighted Average Price/Moving Average, and its figure says VWAP. It treats the two names as one line here.",
                "How the average is weighted is Chapter 11. Today it is a line over price, and what matters is which side of it price is on.",
                "Moving averages were met in Chapters 4 and 5 and are taught in Chapter 11.",
            ),
        ),
        Pair(
            origin="Book p.181 and Figure 6.11. The figure is labelled VWAP on a 10-minute chart; the caption says VWMA, daily.",
            left=Content(
                title="The VWMA on a chart",
                lines=(
                    "Price rises decisively every time it crosses above the VWMA, and declines in a similar manner when it crosses below.",
                    "The crossovers occur at the daily volume cycle peaks.",
                    "The figure also marks the line acting as support and resistance.",
                ),
                accent="Above the line, bullish. Below it, bearish.",
                caption="Volume cycles, and their peaks: Part 5.",
            ),
            picture=Figure(
                number="6.11",
                shows="A 10-minute chart of the S&P 500 SPDR over four days with a dashed volume weighted average price line, labelled price above it bullish and below it bearish, and the line marked as support and as resistance. Circles on the volume panel mark the daily volume cycle peaks, with arrows from them to the crossovers.",
            ),
            text_w=5.4,
            notes=(
                "Follow each dashed arrow from a circled volume peak up to a crossover. That is the book's point about timing.",
                "Name the mismatch and move on: the caption says VWMA and daily, the figure says VWAP and 10 minutes.",
            ),
        ),
        Pair(
            origin="Book p.181. Both readings are the book's, a paragraph apart; it does not reconcile them. The chart is ours, on invented prices.",
            left=Content(
                title="Undervalued below, overvalued above",
                lines=(
                    "The book also calls a stock undervalued below the VWMA and overvalued above it.",
                    "Many institutional traders look for buy signals only when it is undervalued, and sell signals only when it is above.",
                    "So above the line is potentially bullish, and also where institutions look to sell.",
                ),
                accent="Two readings of one line, both the book's.",
                caption="Know both. The book leaves the tension between them unresolved, and so does this slide.",
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
            origin="Book pp.182-183, its four scenarios. Chapter 4 named the climaxes by who trades. The chart is ours: sketches, not prices.",
            left=Content(
                title="Tops and bottoms: volume at the extremes",
                lines=(
                    "A top or bottom usually comes on relatively large or extreme volume, or on relatively low or minimal volume.",
                    "Extreme volume: a top is a blow-off or buying climax, a bottom a sell-off or selling climax.",
                    "Extremely low volume: a low volume top, or a low volume bottom.",
                ),
                accent="Four turns, named by place and by volume.",
                caption="Chapter 4 named the climaxes that end a trend. Chapter 6 adds their extreme volume.",
            ),
            picture=Chart(
                letter="N",
                shows="Four small cases, each a price turn over its volume. A top on one towering volume bar, the blow-off or buying climax. A bottom on a towering bar, the sell-off or selling climax. A top on the smallest bar, a low volume top. A bottom on the smallest bar, a low volume bottom.",
            ),
            text_w=CHART_W,
            notes=(
                "The climaxes are a recall: Chapter 4 told who buys and sells in them. What is new is the volume, and the two low volume names.",
                "The low volume top and bottom get their own slide after the climax figures, in the book's order.",
            ),
        ),
        Pair(
            origin="Book p.183 and Figure 6.12. Exxon Mobil is spelt Exxon Mobile by the book.",
            left=Term(
                term="Upper and lower overextended volume levels",
                plain="A line across the volume panel that only extreme volume reaches. A lower one catches smaller turns.",
                example="Figure 6.12: Exxon Mobil bottoms on two selling climaxes, and both spikes reach the upper level.",
                formal="The extreme volume level is the upper overextended volume level, a signal for potential bottoms or tops. A lower overextended volume level forecasts less significant corrections.",
            ),
            picture=Figure(
                number="6.12",
                shows="The daily chart of Exxon Mobil from 2006 to 2013: an ellipse around a market bottom made by two selling climaxes, with arrows down to two volume spikes. Across the volume panel run two lines, upper level volume overextension and lower level volume overextension.",
            ),
            text_w=6.2,
            notes=(
                "Point at the two spikes under the ellipse: each is a selling climax, and each reaches the upper line.",
                "Upper for the big turns, lower for the corrections. Where to draw them is the slide after next.",
            ),
        ),
        Pair(
            origin="Book p.183 and Figure 6.13.",
            left=Content(
                title="Blow-offs: buying climaxes",
                lines=(
                    "A couple of blow-offs, or buying climaxes, at relatively high volume.",
                    "Each is a market top on a volume spike, and price falls after it.",
                ),
                accent="The same overextension that marks a selling climax marks a buying one.",
            ),
            picture=Figure(
                number="6.13",
                shows="The daily chart of the E-TRACS UBS Bloomberg CMCI Food ETN with two circled volume spikes labelled blow-off, each under a market top.",
            ),
            text_w=5.4,
            notes=(
                "The mirror of the last figure: tops this time. Follow each arrow from BLOW-OFF to its spike and up to its top.",
                "The second blow-off is on a much smaller spike than the first in absolute terms. Compare it with the volume around it, not with the first.",
            ),
        ),
        Pair(
            origin="Book pp.183-184 and Figure 6.14. Sigma, a standard deviation, is taught in Part 3.",
            left=Content(
                title="Where to set the overextension level",
                lines=(
                    "Set by visual inspection, where only the most significant tops or bottoms are found.",
                    "Set lower, it signals more often, at less significant tops and bottoms.",
                    "Figure 6.14: the spikes are all above the rolling 100-day 2-sigma level; one breaks a significant support.",
                ),
                accent="Higher level, fewer and bigger turns.",
            ),
            picture=Figure(
                number="6.14",
                shows="The daily SPDR Gold Trust: a dashed volume overextension line across the volume panel with circled spikes above it, and a dashed support line on the price that is broken at the right on extreme volume, labelled above the rolling 100-day 2-sigma level.",
            ),
            text_w=5.4,
            notes=(
                "By eye is the book's method: there is no formula for the line. The 2-sigma level is a second, computed line, and Part 3 builds one.",
                "Find the support break at the far right: price falls through a significant level on extreme volume.",
            ),
        ),
        Pair(
            origin="Ours, drawing the book's p.183 rule on one invented chart. Both levels and every price are ours.",
            left=Content(
                title="Our example: a higher level and a lower one",
                lines=(
                    "Upper level: only two spikes reach it, at the two major turns, 1 and 2.",
                    "Lower level: three more spikes reach it, at smaller corrections, a, b and c.",
                ),
                accent="Where the line goes decides which turns it signals.",
            ),
            picture=Chart(
                letter="O",
                shows="An invented price with two major turns and three smaller corrections, over its volume. Two dashed lines cross the volume panel. Only the spikes at the major turns, numbered 1 and 2, reach the upper line; the spikes at the corrections, lettered a to c, reach only the lower one.",
            ),
            text_w=CHART_W,
            notes=(
                "The numbers are the big turns and the letters the small ones. Ask the room which line they would draw to trade only the big ones.",
                "Both lines were placed by eye, the way the book says to.",
            ),
        ),
        Pair(
            origin="Book p.184 and Figure 6.15. The book does not explain the Bollinger Bandwidth here.",
            left=Content(
                title="Volatility spikes at the same turns",
                lines=(
                    "A Bollinger Bandwidth oscillator times volatility in silver.",
                    "The volatility spikes coincide with the volume overextensions, signaling tops and bottoms.",
                ),
                accent="Many practitioners filter out volatility below a threshold and regard it as noise.",
                caption="Bandwidth and Bollinger Bands are named and not explained in this chapter.",
            ),
            picture=Figure(
                number="6.15",
                shows="The continuous daily chart of silver with an upper and a lower volume overextension line, and under it a bandwidth oscillator labelled volatility, with its own historical volatility level. Thin lines join circled volatility spikes to volume overextensions and to a top at 1 and a bottom at 2.",
            ),
            text_w=5.4,
            notes=(
                "Two kinds of evidence agree at 1 and 2: volume overextended, and volatility spiking. The lower, wavy stretch is what the book calls noise.",
                "Do not teach the bandwidth. Say it is a measure of volatility the book uses here and explains elsewhere.",
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
            origin="Book pp.183, 185 and Figure 6.16.",
            left=Term(
                term="Low volume top and low volume bottom",
                plain="A top, or a bottom, made on very little volume.",
                example="Figure 6.16: Apple turns at seven time lines, each where volume tests a lower volume threshold, circled. Some are tops and some are bottoms.",
                formal="A market top associated with extremely low or minimal volume is called a low volume top. A market bottom associated with extremely low volume is called a low volume bottom.",
            ),
            picture=Figure(
                number="6.16",
                shows="A daily Apple chart with a low volume threshold drawn across its volume panel and circled wherever volume tests it. Dashed time lines run up from each circle to a top or a bottom in price, labelled low volume reversals.",
            ),
            text_w=6.2,
            notes=(
                "These are the low volume reversals of the part's start, now named by where they turn: at a top or at a bottom.",
                "The threshold is again drawn by eye, and the circles are where volume tests it.",
            ),
        ),
        Pair(
            origin="Book p.186. The chart is ours: sketches, not prices. Overbought and oversold are used and not defined in this chapter.",
            left=Content(
                title="Overbought or oversold? Only afterwards",
                lines=(
                    "Overextended volume can signal either a top or a bottom: extreme buying and selling both generate volume.",
                    "So a volume extreme is not overbought or oversold until it is tied to a top or a bottom.",
                ),
                accent="We can pinpoint the overextension now. Overbought or oversold, only in retrospect.",
                caption="Overbought and oversold: met in Chapters 1 and 5, never defined there or here. Oscillators are Chapter 8.",
            ),
            picture=Chart(
                letter="P",
                shows="Two small cases with the same towering volume bar. In one, price had been rising and it turns out to be a top: overbought, in retrospect. In the other, price had been falling and it turns out to be a bottom: oversold, in retrospect.",
            ),
            text_w=CHART_W,
            notes=(
                "The two volume bars are identical. Only what price did next tells you which one it was.",
                "That is the book's reason for not calling volume overbought or oversold in advance.",
            ),
        ),
        Pair(
            origin="Book p.186 and Figure 6.17.",
            left=Content(
                title="Lower timeframes are more sensitive",
                lines=(
                    "The same gold volume, on five timeframes: daily, weekly, monthly, quarterly, yearly.",
                    "Daily and weekly volume peak in 2013. Monthly and higher peak in 2011.",
                    "Lower timeframe charts are more sensitive to volume action.",
                ),
                accent="At higher timeframes, the overall trend or behavior of volume is more obvious.",
            ),
            picture=Figure(
                number="6.17",
                shows="The continuous chart of gold with five volume panels under it: daily, weekly, monthly, quarterly and yearly. Lines over each mark where its volume peaks: in 2013 on the daily and weekly panels, in 2011 on the monthly, quarterly and yearly ones.",
            ),
            text_w=7.2,
            notes=(
                "Find the circled spike in 2013 on the daily and weekly panels. Then find where monthly and above peak: 2011.",
                "One day's spike dominates a daily panel. Added into a month or a year, it is outweighed by the busy months around it.",
            ),
        ),
        Pair(
            origin="Ours: the book's p.186 point on one invented volume record. The days, the spike and the months are ours.",
            left=Content(
                title="Our example: one record, two timeframes",
                lines=(
                    "Daily: the tallest bar is one spike, late in the record, at 1.",
                    "Monthly: the same days added up by month. The busiest month, 2, comes earlier.",
                ),
                accent="One volume record, two different peaks: it depends on the timeframe.",
            ),
            picture=Chart(
                letter="Q",
                shows="One invented volume record drawn twice. Upper panel, daily bars: the tallest is a single spike late in the record, marked 1. Lower panel, the same days summed into monthly bars: the tallest is a busy month earlier on, marked 2, and the late spike's month is not the highest.",
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
                    "Volume peak: the tallest bar comes at the touch, the bar where price meets the barrier. Resistance 1, Support 1.",
                    "Volume dip or trough: the shortest bar comes at the touch. Resistance 2, Support 2.",
                ),
                accent="The book: the peak is the most reliable.",
            ),
            picture=Figure(
                number="6.18",
                shows="Four sketches under the question which price barrier is more reliable. Resistance 1 and Support 1 are each touched as volume peaks; Resistance 2 and Support 2 are each touched as volume dips to its lowest.",
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
                    "1 Increasing: each bar taller. 2 Decreasing: each shorter. 3 Peaking: tallest at the touch.",
                    "4 Bottoming: shortest at the touch. 5 Flatlining: all alike.",
                ),
                accent="Top: resistance. Bottom: support.",
                caption="The book: increasing or decreasing volume there signifies a change in sentiment, the crowd's mood (Chapter 1).",
            ),
            picture=Figure(
                number="6.19",
                shows="Ten sketches in two rows, five at a resistance and five at a support, each with volume bars under the turn: increasing, decreasing, peaking, bottoming and flatlining across the barrier.",
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
                    "Peaking, ours: 1, 2, 4, 7 at the touch, 4, 2, 1. Figure 6.18's peak: most reliable.",
                    "Bottoming: 7, 4, 2, 1 at the touch, 2, 4, 7. Figure 6.18's dip: less reliable.",
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
                    "The average is slide 57's smoothed volume filter, over the last N bars. N, the lookback, is how many bars go into it.",
                    "Short N, 5 bars say: hugs the bars closely, ordinary ones cross it too, many false signals.",
                    "Long N, 100 bars say: slow and flat, only huge spikes cross it, few signals, some turns missed.",
                ),
                accent="The right N sits in between. How to find it: next slide.",
                caption="Figure 6.20: each dotted arrow runs from a spike crossing the line up to a top or a bottom.",
            ),
            picture=Figure(
                number="6.20",
                shows="The daily USDJPY chart with a smoothed volume line across its volume panel, labelled moving average overextension threshold. Dotted arrows rise from the overextensions in volume to tops and bottoms in price.",
            ),
            text_w=5.4,
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
                plain="Sigma is the standard deviation: how far volume typically strays from its own mean, over the same N bars. The line: Upper = mean + k x sigma, k = 3 here, or 2.",
                example="Worked, ours: the last 20 bars average 10 million shares, sigma 2 million. 3-sigma line = 10 + 3x2 = 16 million: 12 million does not cross, 18 million does. 2-sigma line = 14 million, so it flags more bars.",
                formal="A 2- or 3-sigma filter, also a volatility filter, keeps only the most significant surges: a Bollinger Band on volume, lines a set number of standard deviations above and below a moving average, upper band only, since only surges matter here.",
            ),
            picture=Chart(
                letter="U",
                shows="An invented volume record with two lines across it: the 20-bar average volume, and above it a three-sigma line, the average plus three standard deviations. Only three bars cross the upper line, in gold.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Sigma is the Greek letter for a standard deviation: how far values typically spread from their average.",
                "Bollinger Bands were named in Chapter 1, in the mean reverting approach, and are not explained there either. All this filter needs is the upper line.",
                "Three sigma is stricter than two: fewer bars cross it.",
            ),
        ),
        Content(
            origin="Book p.189 gives only the words. Ours: how build/charts_chapter06.py actually computes it, read from the code, not guessed.",
            title="How the dotted line is drawn, bar by bar",
            lines=(
                "At each bar: take its last 20 volume bars, this one included. Mean, then sigma. Plot mean + 3 x sigma. Move forward one bar, repeat.",
                "That is why it jumps: a spike entering the window raises both at once, so the line leaps up, staying high until the spike leaves 20 bars later.",
                "The book never says if sigma divides by 20 or 19, or if the bar sits in its own window. Our code divides by 20 and includes the bar.",
            ),
            accent="Recomputed from nothing at every bar: no memory beyond its window.",
            notes=(
                "This closes the two gaps the review found: the divisor and the window. Both are read straight from the code that drew the chart.",
                "The jump explanation matches the chart's own footnote, here given as the reason instead of just the fact.",
            ),
        ),
        Pair(
            origin="Book p.189 and Figure 6.21. Ours: the counts of arrows and the April top, read off Figures 6.20 and 6.21.",
            left=Content(
                title="A three-sigma filter on USDJPY",
                lines=(
                    "Stepped line: the three-sigma filter, on daily USDJPY. The book marks three surges over it, arrows up to price.",
                    "Figure 6.20, same market, marked six. Stricter, this line skips the April 2011 top, the highest price, that 6.20 caught.",
                    "The two lower lines are drawn and not named by the book; only the top one is the filter.",
                ),
                accent="The book: such surges tend to come at the most significant tops and bottoms.",
            ),
            picture=Figure(
                number="6.21",
                shows="The daily USDJPY chart with a stepped line across its volume panel labelled 3-sigma volume overextension threshold, and dotted arrows from the few overextensions in volume above it to tops and bottoms in price.",
            ),
            text_w=5.4,
            notes=(
                "Compare with Figure 6.20, the same market. The threshold here is higher, so only the largest surges cross it.",
                "Follow each of the three arrows down to the surge under it. Then find the April 2011 top: a dotted upright, and no arrow.",
            ),
        ),
        Content(
            origin="Book p.189. It names the oscillator and does not describe it.",
            title="Why the book draws the line on the bars",
            lines=(
                "The book also names a standard deviation oscillator: an indicator in its own panel, as Part 1 used the word. It does not describe or draw one.",
                "It is less useful, the book says, because it gives no overlay: a line drawn over the volume bars themselves, so a bar can be seen crossing it.",
                "Figure 6.21's line stays high for months after the March spike, far beyond our 20 bars. The book never gives its N.",
            ),
            accent="What to do: pick N as for the smoothed filter, then draw the 3-sigma line over the bars. A bar above it may mark a top or bottom.",
            notes=(
                "No picture: this slide reads the book's one sentence on the oscillator, beside the two figures already shown.",
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
                    "A threshold drawn by visual inspection, so only the most significant peaks reach it. The oval rings July to August.",
                    "Two arrows: under Points 1 and 3, days apart, and under 2. Trendline 1 to 2, parallel from 3.",
                ),
                accent="At X price bounces off the lower line, a short-term buy, then falls through it.",
            ),
            picture=Figure(
                number="6.22",
                shows="The daily silver chart, XAGUSD, with a tick volume overextension threshold across its volume panel. Arrows rise from the circled tick volume peaks to points 1, 2 and 3; a channel is drawn from 1 and 2 with a parallel from 3, and price reacts at X.",
            ),
            text_w=5.6,
            notes=(
                "Follow the two arrows from the oval up to points 1 and 3, then 2. Those are the only points used.",
                "Falls through it: the book says the market reversed downward, violating the rising channel.",
            ),
        ),
        Content(
            origin="Book pp.189-190 and Figure 6.22. Ours: the arithmetic at X, and what the figure's volume panel shows.",
            title="What the channel is for, and what the book leaves open",
            lines=(
                "Ours: X is bar 72, 28 bars after trough 3 at bar 44. The lower line is there at 49.00 + 28 x 0.10 = PHP 51.80; price touches it and turns up.",
                "Silver's April bars (labelled High tick volume level) and late September bars reach the line too; the channel uses only July to August, unexplained.",
                "Chapter 5's uptrend line joined troughs; here the book joins two peaks and gives no reason. Either way, two parallels make the channel.",
            ),
            accent="What to do: at the lower line, look for a short-term buy, as at silver's X. Falling through it violates the channel.",
            notes=(
                "28 is the number of bars from trough 3, bar 44, to X, bar 72, on the step by step chart.",
                "Why only heavily traded turns? The book says only that it shows the importance of significant inflection points; the next figure's slide quotes it. Part 3's first rule, a barrier formed at a volume peak is the most reliable, fits, and that link is ours.",
            ),
        ),
        Pair(
            origin="Book pp.189-190 and Figure 6.23. Candlestick and valid: Chapters 3 and 5.",
            left=Content(
                title="More channels from filtered points",
                lines=(
                    "Points numbered afresh. Ovals ring heavy volume under 1, under 3 and 2, under 5 and 6.",
                    "Trendline 1 to 2, parallel from 3: a large bearish candlestick, closing far below its open, breaks it.",
                    "A parallel from 4, carried back, meets the trough at X, January 2011: valid, the book says, with no third touch (Chapter 5).",
                    "Parallels from 5 and 6: a new channel.",
                ),
                accent="Every line runs parallel to 1 to 2.",
            ),
            picture=Figure(
                number="6.23",
                shows="The same silver chart with more volume filtered points, numbered 1 to 6 and X. Several parallel rising lines are drawn through them, each from a point that came on overextended volume, forming channels that contain price.",
            ),
            text_w=5.6,
            notes=(
                "Count the parallels: five lines, every one at the slope of the line from 1 to 2.",
                "The book admits the line through X was found looking back. It still calls the channel valid.",
            ),
        ),
        Content(
            origin="Book pp.189-190 and Figure 6.23. Angular symmetry: Chapter 5. Ours: what the figure rings and what it does not.",
            title="What Figure 6.23 shows, and two things it leaves open",
            lines=(
                "Every line has the slope of trendline 1 to 2, January to November 2011: one steady angle, which the book calls near perfect angular symmetry (Chapter 5).",
                "The 5 and 6 channel: resistance at its top, support at its bottom. The book's lesson: build patterns on significant inflection points.",
                "Open: the text calls it the same chart of USDJPY; caption and chart say silver.",
                "Open: the figure rings no heavy volume under 4 or X, though both anchor lines.",
            ),
            accent="Draw from heavily traded turns; watch the parallels for resistance and support.",
            notes=(
                "No picture of its own: it reads Figure 6.23, on the slide before, as a whole.",
                "Look at the three ovals on the volume panel: they sit under 1, under 2 and 3, and under 5 and 6.",
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
                    reason="The book draws a simple tick volume overextension level by visual inspection.",
                ),
            ),
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
                plain="Holding a losing position rather than selling at a loss, hoping it comes back. Holding is not trading: it adds no volume.",
                example="Bought at PHP 50, now PHP 38: an unrealized loss of PHP 12, on paper only, as you have not sold. You hold for breakeven, PHP 50.",
                formal="Many investors hold on to losing positions in a falling market, hoping they rebound to breakeven or profitability, believing unrealized losses are not real losses: loss aversion bias.",
            ),
            picture=Chart(
                letter="X",
                shows="An invented share falling from 50 to 38 pesos, with a dashed line at the 50 peso entry price labelled bought here. A label on the fall says holders wait for breakeven instead of selling, and the volume bars under the fall shrink.",
            ),
            text_w=TERM_CHART_W,
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
            text_w=CHART_W,
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
            text_w=CHART_W,
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
                example="Plus 1 a contract when a new long and short both open; minus 1 when both close; no change when one side is replaced. Worked: next slide.",
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
        Content(
            origin="Book p.192 gives the three rules and the reason. The traders and contract counts are ours.",
            title="Open interest, day by day",
            lines=(
                "Day 1: A buys 1 from B, both new, A long and B short: plus 1. Open interest 1.",
                "Day 2: C buys 2 from D, both new: plus 2. Open interest 3.",
                "Day 3: A sells that 1 to E, the new long; B is still short: no change. Still 3.",
                "Day 4: D buys back 2 from C: D's short and C's long close: minus 2. Now 1.",
            ),
            accent="Only both sides opening, or both closing, moves the count.",
            caption="The book's reason to count: unlike stocks, all futures and options contracts eventually expire.",
            notes=(
                "This slide has no picture of its own: the chart beside the term is these four days, one column each.",
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
            text_w=CHART_W,
            notes=(
                "The same rule as Part 1's bullish and bearish volume, with open interest moving alongside volume. Both words, both rules: the book says open interest divergence is read as for non-price-based volume oscillators.",
                "The book's reason for the last case: participants are less interested in seeing the market decline further.",
                "This is review question 6, the relationship between volume, open interest and price.",
            ),
        ),
        Content(
            origin="Book p.192 gives the four readings and their reasons. The contract, its prices and its counts are ours, invented.",
            title="The four readings, worked",
            lines=(
                "Ours: a futures contract rises from PHP 100 to PHP 110.",
                "Open interest 50,000 to 60,000 contracts, volume 8,000 to 12,000 a day: both rise with price. Bullish confirmation, buying pressure.",
                "Open interest 50,000 to 40,000, volume 8,000 to 5,000: both fall as price rises. Bearish divergence: shorts covering, longs leaving.",
                "Falling from PHP 110 to PHP 100 instead: both rising is bearish confirmation, short selling; both falling, bullish divergence.",
            ),
            accent="Same price move, opposite readings: volume and open interest decide.",
            notes=(
                "This slide has no picture: it puts numbers on the four sketches of the last slide. The names are Part 1's: bullish or bearish, confirmation or divergence.",
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
                accent="Figure 6.24, silver, A to B: volume peaks higher at 1, bullish confirmation; open interest peaks lower at 2, bearish divergence. They disagree; the book reads open interest: longs liquidating, early. Silver then fell from about $49 to under $30.",
            ),
            picture=Figure(
                number="6.24",
                shows="The continuous daily chart of silver rising from A to B, with an open interest panel showing a lower peak at 2, labelled bearish divergence, and a volume panel showing a higher peak at 1, labelled bullish confirmation.",
            ),
            text_w=7.4,
            notes=(
                "The four actions are the four cases of the last slide, turned into what to do.",
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
            text_w=CHART_W,
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
            origin="Book pp.192-193. OTC fx is the book's over the counter foreign exchange market. The five trades are Part 1's, ours. Chapter 3's tick chart counts trades the same way.",
            left=Term(
                term="Tick volume",
                plain="A count of trades, not shares: one tick is one trade, of any size. Met in Chapter 1's caption and Chapter 3's tick chart.",
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
            text_w=TERM_CHART_W,
            notes=(
                "Advances and declines were listed in Chapter 3 as breadth data and never defined. The plain row reads them as the number of stocks rising and falling; that reading is ours.",
                "Up volume and down volume: the volume in the rising stocks and in the falling ones, again our reading of the names.",
                "Work the arithmetic slowly. The TRIN is a ratio of two ratios.",
            ),
        ),
        Content(
            origin="Book p.193 gives the ratio. It names breadth volume, advances, declines, up and down volume and never defines them; our readings. The numbers are ours.",
            title="The TRIN, step by step",
            lines=(
                "1  Advances / declines = 1,500 / 1,000 = 1.5 rising stocks for each falling one.",
                "2  Up volume / down volume = 600m / 800m = 0.75: the falling stocks traded more shares.",
                "3  TRIN = 1.5 / 0.75 = 2.0. Rearranged: down volume per falling stock, 800m / 1,000 = 0.8m, over up volume per rising stock, 600m / 1,500 = 0.4m.",
            ),
            accent="A TRIN of 2.0: each falling stock traded, on average, twice the volume of each rising stock.",
            caption="Step 3 and the gold line are our arithmetic; the book never reads one value such as 2.0.",
            notes=(
                "This slide has no picture: the chart beside the term is these three steps as columns.",
                "Step 3 is only the same division rearranged. Check it on the board: 0.8 / 0.4 = 2.0.",
            ),
        ),
        Pair(
            origin="Book p.193 and Figure 6.25; the levels are read off the figure by eye. The caption says daily; the chart and the text say 1-minute.",
            left=Content(
                title="Reading the tick and the TRIN",
                lines=(
                    "The tick: the book never says what it measures. On Figure 6.25 it goes below zero, so it is not tick volume, a count of trades.",
                    "Short term, the book's rule: tick rising but not overbought, TRIN falling but not oversold: bullish, look for a long entry.",
                    "Figure 6.25 shows something else: tick down to about -1,000, TRIN up to about 2.2, both at levels it labels oversold. The index then rose.",
                ),
                accent="Both at the labelled oversold extremes: the book reads short-term bullish, look for a long entry.",
                caption="The book does not say why its figure departs from its short-term rule.",
            ),
            picture=Figure(
                number="6.25",
                shows="A 1-minute chart of the S&P 500 index falling and then rising, with a $TICK panel and a $TRIN panel under it. A box around the low marks both labelled oversold, with the note that short-term bullishness was predicated on the confluence of oversold signals.",
            ),
            text_w=7.2,
            notes=(
                "Read the short-term rule, then point at the box: the tick dips and the TRIN rises, the opposite of the rule's bullish case. Say so; do not reconcile it.",
                "The converse, the longer-term rule and the book's gaps are the next slide.",
            ),
        ),
        Content(
            origin="Book p.193 and Figure 6.25. The weekly tick numbers are ours, in invented units; the book never says what the tick measures.",
            title="The longer-term rule, and the book's gaps",
            lines=(
                "Short term, the converse: tick falling but not oversold, TRIN rising but not overbought: bearish, look for a short entry.",
                "Longer term: tick oversold, above its weekly two-sigma level, and TRIN overbought, near or above 3.0 daily: bullish, long. Reverse: bearish, short.",
                "Two sigma: Part 3's line, k = 2. Ours: weekly tick mean 200, sigma 300, line 200 + 2 x 300 = 800; above it, oversold. A daily TRIN of 3.2: overbought.",
            ),
            accent="Bullish TRIN: overbought in the text, oversold in Figure 6.25.",
            caption="No reasons for either rule. Figure 6.25's oversold tick sits at its low, not above two sigma.",
            notes=(
                "This slide has no picture: it finishes the book's rules from the last slide's figure. Do not settle the gaps; name them.",
                "No check rests on these rules. The check after this part tests only tick volume and the TRIN's arithmetic.",
            ),
        ),
        Pair(
            origin="Book p.194 and Figure 6.26; the TRIN values are read off the figure. Its caption says daily; the times show a 1-minute chart.",
            left=Content(
                title="A bearish day on the tick and the TRIN",
                lines=(
                    "Figure 6.26: the S&P 500 falls all afternoon. The boxed TRIN rises from about 0.9 to 1.34: bearish, by the short-term rule.",
                    "1:45 to 2:45 p.m.: the text says largely absent of activity; the figure says absent of uptick action. In its shaded box the tick barely rises above zero and twice drops to about -1,000, circled as extreme bearish ticks.",
                ),
                accent="Together, a short-term bearish signal: look for a short entry.",
                caption="The book gives no reason this is bearish, and does not define uptick.",
            ),
            picture=Figure(
                number="6.26",
                shows="A 1-minute chart of the S&P 500 index on an intraday decline, with a $TICK panel showing stretches marked bearish and balanced tick action, and a $TRIN panel whose last stretch is boxed and labelled rising TRIN, bearish.",
            ),
            text_w=5.4,
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
            text_w=TERM_CHART_W,
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
            origin="Book p.194 and Figure 6.27. Chapter 4's Figure 4.19 showed the same thing and called it price-based volume.",
            left=Content(
                title="Volume by price marks a support: silver",
                lines=(
                    "Figure 6.27, iShares Silver Trust: sideways bars longest around $17. The book's volume turnover here is shares traded, not the turnover ratio.",
                    "So $17 represents a significant support: a floor where a fall may stop. The figure: significant capital commitment.",
                    "Also marked: high volume at about $35, a new consolidation level, not in the text.",
                ),
                accent="Ordinary volume bars show when, not at what price.",
                caption="Chapter 4's price-based volume; not Part 1's oscillators.",
            ),
            picture=Figure(
                number="6.27",
                shows="The daily iShares Silver Trust with volume by price drawn as horizontal bars from the left edge. The longest bars sit around the $17 level, labelled significant capital commitment, strong support, and another cluster at the newer consolidation level higher up.",
            ),
            text_w=5.4,
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
                    "Figure 6.28, 3M: the longest sideways bars, bracketed, $77 to $86: the most traded range, more shares than at any other price.",
                    "With 3M last at about $88, $77 to $86 lies below: potential support, the figure's label. $90 to $92 above: some resistance, says the book, not how it was found.",
                    "Volume panel lines, Part 1's names: bearish confirmation, price falling on rising volume; bearish divergence, price rising on falling volume.",
                ),
                accent="These price ranges are potential future support and resistance levels.",
            ),
            picture=Figure(
                number="6.28",
                shows="The daily chart of 3M with volume by price as horizontal bars, the longest bracketed between about $77 and $86 and labelled maximum capital commitment in this range, an important support zone in the future.",
            ),
            text_w=5.4,
            notes=(
                "The bracket on the figure is the $77 to $86 range. Price later falls through it and returns.",
                "The figure's own labels also mark bearish confirmation and bearish divergence on the volume panel: Part 1's names again.",
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
            text_w=CHART_W,
            notes=(
                "Follow the numbers on the chart in order. The band is step 1, the shaded columns step 2, the boxes step 3, the two lines step 4.",
                "The book takes the nearest turn either side of the intersection. The next slide says what our two levels then did.",
            ),
        ),
        Content(
            origin="Book pp.196-197. The prices are our chart's, read from the series that drew it.",
            title="What the two levels did on our chart",
            lines=(
                "Support at PHP 47.50: price turned up near it twice, at PHP 47.40 and PHP 47.50.",
                "Resistance at PHP 50.80: price turned down near it twice, at PHP 50.90 and PHP 50.80, then broke above it and rose to about PHP 58.60.",
                "The book says potentially: likely levels, not certain ones. It does not say what a break through one means.",
            ),
            accent="A level from the four steps is potential: ours held twice, then broke.",
            notes=(
                "This slide has no picture: it reads the two lines of the chart on the last slide, after the step 4 prices were found.",
                "Do not add a rule for the break. The book gives none.",
            ),
        ),
        Pair(
            origin="Book pp.196-197 and Figure 6.29; the two levels are read off the figure by eye.",
            left=Content(
                title="The four steps on 3M",
                lines=(
                    "1  $74 to $80: the book's largest volume by price range, the dark sideways bars.",
                    "2 and 3  The dark columns, where volume reaches the dotted overextended volume level (Part 2), cross it in two white boxes.",
                    "4  Closest peak above, about $80: resistance. Closest trough below, about $72.50: support.",
                ),
                accent="Both act as effective barriers to price on the daily chart of 3M.",
                caption="Figure 6.28 gave 3M's most traded range as $77 to $86. The book does not say why they differ.",
            ),
            picture=Figure(
                number="6.29",
                shows="The daily chart of 3M with the $74 to $80 volume by price band and two dark time columns over the high volume intervals; where they cross are two white boxes. Dashed lines mark the closest resistance above and the closest support below, and an overextended volume level runs across the volume panel.",
            ),
            text_w=5.4,
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
                    "Set range against volume: four cases. Figure 6.30 draws each, 1 to 4, as an empty box, the range, over a black box, the volume.",
                    "1 short range, low volume; 2 short, high; 3 tall, low; 4 tall, high. The book uses them to forecast breakouts and reversals.",
                ),
                accent="Chapter 5's squat bar, a small range on large volume, is case 2.",
            ),
            picture=Figure(
                number="6.30",
                shows="Four numbered pairs: an empty box for the bar range over a black box for the volume. 1 short on low, 2 short on high, 3 tall on low, 4 tall on high.",
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
                plain="Four names for one bar: narrow or wide range, on low or high volume, each against the trend's usual bars.",
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
        Content(
            origin="Book p.197: the four names. Ours: every number, and the comparison with the usual bar, which the book does not put a number on.",
            title="Naming a bar, step by step",
            lines=(
                "Step 1, the usual bar. Ours: about PHP 1.00 high to low, on 2 million shares.",
                "Step 2, compare. PHP 0.20 on 1 million: narrow, low, Low Volume Rest Bar. PHP 0.20 on 5 million: narrow, high, High Volume Reversal Bar.",
                "PHP 2.50 on 1 million: wide, low, Low Volume Reversal Bar. PHP 2.50 on 5 million: wide, high, High Volume Continuation Bar.",
                "The book gives no number for narrow, wide, low or high; ours are for the example. Judge each bar against those around it.",
            ),
            accent="Range against usual, volume against usual: four names.",
            notes=(
                "This slide has no picture: it is the arithmetic of the term slide, done four times. Say each pair of numbers, then the name.",
                "Ask the room for a fifth: PHP 0.90 on 2.1 million. Neither narrow nor wide, neither low nor high: an ordinary bar, no name.",
            ),
        ),
        Pair(
            origin="Book p.197: the readings are the book's; the gold line is our summary. The chart is ours: sketches, not prices.",
            left=Content(
                title="The two reversal bars",
                lines=(
                    "High Volume Reversal Bar, narrow on high volume, chart left: a strong potential for reversal. Bearish in an uptrend; the converse, bullish, in a downtrend.",
                    "Low Volume Reversal Bar, wide on low volume, right: a potential for reversal. The longer the bar, the more bearish in an uptrend, bullish in a downtrend.",
                ),
                accent="Too little movement for the volume, or too little volume for the move.",
            ),
            picture=Chart(
                letter="AI",
                shows="Two small invented uptrends of price bars over volume. Left: a narrow bar on very high volume at the top, the high volume reversal bar, then price falls. Right: a very wide bar on low volume at the top, the low volume reversal bar, then price falls.",
            ),
            text_w=CHART_W,
            notes=(
                "Left cell: find the tall gold volume bar, then the tiny price bar above it. Right cell: the short gold volume bar, then the long price bar above it.",
                "In both cells price falls after the named bar, because both are drawn in an uptrend, where both are bearish.",
            ),
        ),
        Content(
            origin="Book p.197: both reasons are the book's, and the converse is its word for the downtrend case. Ours: every number.",
            title="Why the reversal bars warn, with numbers",
            lines=(
                "Ours: the usual bar moves PHP 1.00 on 2 million shares. Today 5 million trade, 2.5 times usual, and price moves only PHP 0.20.",
                "The book: were that volume buying, the range would be much wider. So sellers are attempting to take control. In a downtrend, the converse.",
                "Ours: price jumps PHP 3.00 on 0.7 million shares, a third of usual. The book: a large move on little participation, a lack of interest.",
            ),
            accent="A warning of a potential turn, not a certainty: the book gives no entry rule.",
            notes=(
                "This slide has no picture: it is the book's two reasons, worked with numbers.",
                "Participation is the book's word for volume: how many shares changed hands.",
            ),
        ),
        Pair(
            origin="Book p.197: the readings and reasons are the book's. The chart is ours: sketches, not prices.",
            left=Content(
                title="The rest bar and the continuation bar",
                lines=(
                    "Low Volume Rest Bar, narrow on low volume: a lack of participation. In a strong, rapid trend, chart left, a potential reversal; in a weak to average one, middle, a point of rest.",
                    "High Volume Continuation Bar, wide on high volume, right: backed by very large participation. Bullish in an uptrend, bearish in a downtrend.",
                ),
                accent="The rest bar reads by the trend's speed; the continuation bar, by its direction.",
            ),
            picture=Chart(
                letter="AJ",
                shows="Three small invented cases of price bars over volume. A rest bar, narrow on low volume, at the top of a strong, rapid rise, after which price reverses. A rest bar in a slow, average rise, after which price rests and rises again. A continuation bar, wide on high volume, after which the rise continues.",
            ),
            text_w=CHART_W,
            notes=(
                "The first two cells are the same kind of bar in two trends. The book's point is that the trend decides what it means.",
                "The continuation bar is Chapter 5's trend promoting case, named.",
            ),
        ),
        Content(
            origin="Book p.197; Chapter 5, characteristic 15. Ours: every number, and a pause as the plain reading of point of rest. The book gives no reason speed matters.",
            title="The rest bar's two readings, with numbers",
            lines=(
                "Ours: a rise of PHP 1.60 a bar stalls on a PHP 0.30 bar with a quarter of the usual volume. That fast, then that quiet: a potential reversal.",
                "The same quiet bar in a rise of PHP 0.45 a bar: a point of rest, a pause before the rise goes on. The book gives no speed for strong and rapid.",
                "Chapter 5 called both low volume bars only trend inhibiting, holding the trend back. Here each can also mark a reversal.",
            ),
            accent="Read the rest bar with the trend's speed.",
            notes=(
                "This slide has no picture: it puts numbers on the last slide's two rest bars and sets them against Chapter 5.",
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
                    "At 1 and 2: a narrow range candle on one of the tallest volume bars, about 12 million shares against 5 million most days.",
                    "Point 1, near a low: price then rises. Point 2, near a high: the chart ends before its reversal shows.",
                    "August: volume falls into a triangle's apex, where its lines meet: Part 2's low volume breakout signal. Then a volume surge.",
                ),
                accent="Narrow bar, heavy volume, then a turn.",
            ),
            picture=Figure(
                number="6.31",
                shows="The daily dollar fund. Narrow range candlesticks on high volume circled at 1, near a low, and 2, near a high, lined to their tall volume bars. At the left, a triangle and a low volume breakout signal.",
            ),
            text_w=6.0,
            notes=(
                "Point 1 is a reversal bar at a bottom, so the converse applies: bullish. Point 2 is at a top.",
                "The triangle on the left is Part 2's low volume breakout signal again: volume falling into the apex, then surging. The book calls it a descending triangle; its shape is the book's Chapter 13.",
            ),
        ),
        Pair(
            origin="Book p.198 and Figure 6.32, the PowerShares DB U.S. Dollar Bullish Fund. Ours: the prices and volumes, read by eye.",
            left=Content(
                title="A reversal bar at a bottom",
                lines=(
                    "The dollar fund in 2010: a narrow range candlestick on high volume, circled at a low around the start of November.",
                    "The volume bars under the circle are among the chart's tallest. Price then rebounds, from about 22.0 to about 23.5 within the month.",
                ),
                accent="The converse case: in a decline, a high volume reversal bar is bullish.",
            ),
            picture=Figure(
                number="6.32",
                shows="The daily PowerShares DB U.S. Dollar Bullish Fund with a narrow range candlestick on high volume circled at a low at the start of November, followed by a strong rise.",
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
                    "The dollar fund, 2011: a larger downtrend, about 23.4 in January to 21.0 in May. A short rally ends at a circled high volume reversal bar, May 23.",
                    "Before it, bearish divergence: price rising while volume fell, and the MACD too.",
                    "Bearish, the larger trend's way: potentially more reliable, the book says. Prices then fell.",
                    "X, early May: a high volume continuation bar.",
                ),
                accent="Agreeing with the larger trend: more reliable.",
            ),
            picture=Figure(
                number="6.33",
                shows="The daily dollar fund in a long decline: a circled high volume reversal bar at a short rally's top in late May, falling lines over volume and the MACD before it, and a continuation bar at X.",
            ),
            text_w=6.4,
            notes=(
                "Bearish divergence in volume is Part 1's: price rising into the bar while volume falls.",
                "The MACD is an oscillator the book has not taught. Point at its falling line and leave it there.",
            ),
        ),
        Content(
            origin="Book p.199. Ours: every number, the reading of larger trend as the whole move, and the reading of X. The book does not define the larger trend.",
            title="Why the larger trend matters, with numbers",
            lines=(
                "Larger, or predominant, trend: the whole move, not the last few bars. Ours: PHP 60 to PHP 45 in six months, then a two-week rally to PHP 48.",
                "A high volume reversal bar at PHP 48 is bearish, with the six-month fall: potentially more reliable. The book says the same of continuation bars.",
                "Figure 6.33's X, a high volume continuation bar, is a tall rising candle: against the larger downtrend. Its rally ended at the circle.",
            ),
            accent="Ask which way the larger trend runs. The book gives no further reason.",
            notes=(
                "This slide has no picture: it puts numbers on the last slide's one sentence of reason.",
                "The X reading is ours, from the figure. The book only says continuation bars are more reliable with the predominant trend.",
            ),
        ),
        Pair(
            origin="Book p.199 and Figure 6.34, the dollar fund. Ours: volume and direction read by eye. The book does not say which way price went.",
            left=Content(
                title="A reversal bar at an overextended level",
                lines=(
                    "The dollar fund, end of October 2011: a high volume reversal bar, circled.",
                    "Its volume reaches the line across the volume panel, about 13 million: the book's historically overextended volume level, Part 2's upper level.",
                    "Historically is not defined; the line runs level with the September peaks, the oval. Price had fallen into the bar, and rose after it.",
                ),
                accent="Two signals agree: the reversal bar, and Part 2's overextended volume.",
            ),
            picture=Figure(
                number="6.34",
                shows="The daily PowerShares DB U.S. Dollar Bullish Fund with a line across the volume panel labelled historically overextended volume level, and a circled reversal bar at the end of October whose volume reaches that line.",
            ),
            text_w=5.8,
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
                    "Chapter 3: a constant volume chart starts a new bar each time a set volume has traded, so every volume bar is the same height.",
                    "So the book finds reversal bars from the bar range alone and its height against the rest of the bars.",
                    "Figure 6.35: a narrow bar, sellers taking control; a very tall bar, a lack of interest in the rise. Both bearish.",
                ),
                accent="Especially useful for reversal bars on high or low volume.",
            ),
            picture=Figure(
                number="6.35",
                shows="Two sketches of a constant volume chart, all volume bars equal. Left: a rise topped by a narrow bar on relatively high volume. Right: by a very tall bar on relatively low volume. Both bearish.",
            ),
            text_w=6.0,
            notes=(
                "Every bar holds the same volume, so a narrow bar is a lot of volume for the price moved, and a tall bar is little volume for it.",
                "That is this part's two reversal bars, read off a chart where volume never changes. The next slide puts numbers on it.",
            ),
        ),
        Content(
            origin="Book p.199 and Figure 6.35, whose labels say relatively high and relatively low volume. Ours: every number, and the per-peso reading.",
            title="High and low volume when every bar's volume is fixed",
            lines=(
                "Ours: every bar holds 100,000 shares, and a usual bar spans PHP 1.00. That is 100,000 shares for each peso of range.",
                "A PHP 0.20 bar: 100,000 shares moved price only 20 centavos, 500,000 shares a peso, five times usual. Figure 6.35's label: relatively high volume.",
                "A PHP 4.00 bar: 100,000 shares moved price 4 pesos, 25,000 a peso, a quarter of usual. Its label: relatively low volume.",
            ),
            accent="Volume is fixed, so the range alone says whether it was a lot or a little for the move.",
            notes=(
                "This slide has no picture: it is the arithmetic behind the figure's two labels.",
                "Divide shares by pesos of range, three times: 100,000 over 1.00, over 0.20, over 4.00.",
            ),
        ),
        Check(
            label="Reversal bars on charts",
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
                    "Most agree that without volume, price cannot move significantly: volume leading price.",
                    "Yet signals need little volume to appear. Chart, 1: a small trendline breakout on ordinary volume.",
                    "As the break becomes obvious it invites tremendous volume. Chart, 2: volume more than doubles.",
                ),
                accent="Price moved first: price led volume. More often now, says the book.",
            ),
            picture=Chart(
                letter="AK",
                shows="An invented share under a falling trendline. At 1 price breaks the trendline by a little, on ordinary volume. At 2 the breakout becomes obvious, price runs and volume surges: price leads, volume follows.",
            ),
            text_w=CHART_W,
            notes=(
                "The book asks the question, does volume lead price, and answers both ways.",
                "On the chart, the breakout at 1 comes first and the volume at 2 after it. That order is what price leading volume means.",
            ),
        ),
        Content(
            origin="Book p.200, one paragraph. Ours: the numbers. The book gives no test for when a light volume signal will draw volume in.",
            title="What price leading volume means for a signal",
            lines=(
                "Ours: volume runs about 1.3 million a day. Price closes PHP 0.80 above a falling trendline that held for two months, on 1.3 million: an ordinary day.",
                "By volume alone, nothing happened. But the break is on every chart, and days later 3 million trade as the move becomes obvious.",
                "So a light volume signal is not dismissed for that alone, nor proven by it: the volume may come after.",
                "Why more often now, the book says: the widespread use of technical analysis.",
            ),
            accent="No significant move without volume, but volume can follow the signal.",
            notes=(
                "This slide has no picture: it is the last slide's small breakout with its numbers said aloud.",
                "Do not turn this into a rule. The book describes the case and gives no test for when a light volume break will draw volume in.",
            ),
        ),
        Pair(
            origin="Book p.200. The hours are the book's; its examples are EURUSD. The chart and the Manila time are ours.",
            left=Term(
                term="Intraday volume cycle",
                plain="Intraday: within one day. Volume swells and fades daily, peaking at about the same hour each day.",
                example="GMT, Greenwich Mean Time: 1:30 to 2:30 p.m. GMT is 9:30 to 10:30 p.m. in Manila. Our chart: reversals at 1 and 3, a continuation at 2.",
                formal="The intraday volume cycle normally peaks around 1:30 p.m. to 2:30 p.m. GMT. At these volume peaks, price will either reverse or continue, but very rarely remain unchanged.",
            ),
            picture=Chart(
                letter="AL",
                shows="Three days of invented hourly bars over their volume. Volume swells to a peak each day between 13:30 and 14:30 GMT, shaded. At the peaks, numbered 1 to 3, price reverses, continues, and reverses again; it does not stay where it was.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "This is review question 8: volume cycles, and where you find them. The book's answer is intraday, with the peak at that hour.",
                "Reverse or continue: the peak does not say which. It says something is about to happen.",
            ),
        ),
        Content(
            origin="Book pp.200-201. Ours: the EURUSD prices and order levels. Bidirectional entry: a Chapter 5 term. Stop orders: Chapter 1.",
            title="Using the cycle: when to watch, not which way",
            lines=(
                "The book: the cycle lets us anticipate potential price action. At the peak hour price will reverse or continue, very rarely stay put.",
                "It does not say which way, so many use a straddle, Chapter 5's bidirectional entry: a buy stop above price and a sell stop below.",
                "Ours: EURUSD, the euro against the US dollar, at 1.3000. Buy stop 1.3020, sell stop 1.2980: whichever price reaches first is the trade.",
            ),
            accent="The book gives no reason for the hour, no distance for the orders, and shows it only on EURUSD.",
            notes=(
                "This slide has no picture: it is the book's use of the cycle, with the straddle worked in one market.",
                "The 20-point distance is ours. The book gives no distance for the two orders, and does not say what is done with the one not filled.",
            ),
        ),
        Pair(
            origin="Book pp.200-201 and Figure 6.36. Retest: our plain reading; the book does not define it. The figure's apex and bottom labels are not in the text.",
            left=Content(
                title="Volume cycle peaks at support and resistance",
                lines=(
                    "30-minute EURUSD: almost every reversal comes at an intraday tick volume peak, the daily spikes in the bottom panel.",
                    "Tick volume, Part 4: a count of trades, given by fx brokers instead of volume.",
                    "Especially useful when price retests a support or resistance level: comes back to one it turned at before.",
                ),
                accent="Many straddle the peak: catch price either way.",
            ),
            picture=Figure(
                number="6.36",
                shows="A 30-minute EURUSD chart over several weeks with support and resistance lines, a triangle and a channel, and daily volume cycles in the volume panel; price reverses at the volume peaks.",
            ),
            text_w=5.8,
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
                    "Hourly EURUSD: price comes back to a rising trendline and rebounds at 1, 4 and 5, each during a tick volume cycle peak.",
                    "There a cycle-tuned stochastic, bottom panel, showed oversold too.",
                    "At 2 and 3 the line failed, with no clear oversold reading: circles Y and X.",
                ),
                accent="The volume peak times the retest; the oscillator confirms it.",
            ),
            picture=Figure(
                number="6.37",
                shows="An hourly EURUSD chart with three rising trendlines, retests marked at 1 to 5, a volume panel with daily volume cycles, and a stochastic panel whose oversold readings are marked under 1, 4 and 5, with circles at X and Y where it was not clearly oversold.",
            ),
            text_w=5.4,
            notes=(
                "Match each number to the shaded marks in the bottom panel. The successful retests had the oscillator oversold; the failures did not.",
                "Do not teach the stochastic. Oversold is used as in Part 2: named, not defined here.",
            ),
        ),
        Pair(
            origin="Book p.202 and Figure 6.38. Point and figure, Renko, three line break and equivolume charts were Chapter 3 terms.",
            left=Content(
                title="Volume on non-constant time charts",
                lines=(
                    "Chapter 3: point and figure, Renko and three line break charts are not plotted linearly in time: equal steps along the axis are not equal times.",
                    "Equivolume: each bar covers the same time, but is wider on heavier volume, so its time axis is non-linear too.",
                    "That changes the angle of trendlines, channels and chart patterns. Figure 6.38: same Apple prices, same line.",
                ),
                accent="Circled, late May: price stays above the line on top, and cuts through it below.",
            ),
            picture=Figure(
                number="6.38",
                shows="Apple, daily: a standard chart over an equivolume chart of the same months, the same trendline on both, circles where each is broken.",
            ),
            text_w=7.4,
            notes=(
                "Chapter 3 built these charts. The point here is only what a non-linear time axis does to a line drawn across it.",
                "Wide bars on heavy days stretch the axis, so the line's angle changes and so does where price crosses it.",
            ),
        ),
        Content(
            origin="Book p.202. Ours: every number. The book says the angle is affected and shows the result; it does not work the arithmetic.",
            title="Why the trendline moves, with numbers",
            lines=(
                "Ours: two lows, PHP 100 and PHP 110, ten days apart. On a daily chart each day is one step wide: the line rises PHP 1.00 a step.",
                "On an equivolume chart those ten days, if heavy, are drawn wider, say 20 steps. The same two lows give a line rising PHP 0.50 a step.",
                "Same prices, different angle, so later prices meet the line at different bars: cut on one chart, not on the other.",
            ),
            accent="The book shows the discrepancy and does not say which break to trust.",
            notes=(
                "This slide has no picture: it is the geometry of the last slide's two charts, in numbers.",
                "Rise over run: 10 pesos over 10 steps, then 10 pesos over 20. Same rise, longer run, flatter line.",
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
            origin="Book p.203: both lists, as printed. It refers the eight methods to Chapter 8.",
            title="6.2  Volume oscillators, and how they are read",
            lines=(
                "The book's eight: the VWMA, the Accumulation Distribution Line (ADL),",
                "On Balance Volume (OBV), the Chaikin Money Flow and Chaikin Oscillator,",
                "the Demand Index, the Herrick Payoff Index, the NYSE Up/Down Volume Line.",
            ),
            accent="Each is read by eight standard methods. Here: mostly divergence, plus oversold levels and trendlines on the indicator.",
            caption="The eight methods, Chapter 8: 1 OBOS overextended levels, 2 equilibrium and zero line crossovers, 3 signal line crossovers, 4 price-oscillator divergence, 5 to 7 geometrically, numerically and horizontally based oscillator pattern analysis, 8 oscillator-on-oscillator analysis. OBOS: overbought and oversold. The VWMA was Part 2; the Demand Index is never explained.",
            notes=(
                "Two lists the book gives without a figure, so this slide has no picture. Say the names, and that Chapter 8 teaches the methods.",
                "Divergence on a volume oscillator was Part 1: price-based ones read like standard divergence.",
            ),
        ),
        Pair(
            origin="Book p.203 gives the rule. The closes and volumes in the example and on the chart are ours.",
            left=Term(
                term="On Balance Volume, OBV",
                plain="A running total of volume: add the day's volume if the close rose, subtract it if the close fell.",
                example="Closes PHP 50.00, 50.50, 50.20, 50.20, 50.80, 50.60; volumes after day 1: 2.0, 1.5, 1.0, 3.0, 1.0 million. OBV: 0, 2.0, 0.5, 0.5, 3.5, 2.5.",
                formal="A cumulative running total of each period's volume: added if the close is higher than the preceding close, subtracted if lower, and nothing if unchanged.",
            ),
            picture=Chart(
                letter="AM",
                shows="Six invented days worked through. Top, the closes from 50.00 to 50.60 pesos. Middle, each day's volume, marked plus when the close rose, minus when it fell, and zero when it was unchanged. Bottom, the running total, the OBV: 0, 2.0, 0.5, 0.5, 3.5 and 2.5 million.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Work it with the room: day 2 closes up, add 2.0; day 3 down, take away 1.5; day 4 unchanged, nothing; day 5 up, add 3.0; day 6 down, take away 1.0.",
                "Only the direction of the close matters, not how far it moved. That is the weakness on the next slide.",
            ),
        ),
        Pair(
            origin="Book pp.203-204: the disadvantage, the weakness and its example are the book's. The chart is ours, on invented bars.",
            left=Content(
                title="The OBV: a disadvantage and a weakness",
                lines=(
                    "Disadvantage: its absolute value depends on the start date. Its relative changes do not, so the eight methods still work.",
                    "Weakness: volume is added or subtracted regardless of the bar's own behavior.",
                    "A bar closing just below the last close is subtracted, even after a new high far above the last bar's.",
                ),
                accent="To redress it, many prefer the ADL or the two Chaikin indicators.",
            ),
            picture=Chart(
                letter="AN",
                shows="Two small cases. Left: the same OBV started on two different days, two lines of the same shape at different heights. Right: two bars, the second making a much higher high but closing a little below the first, and its whole volume marked as subtracted.",
            ),
            text_w=CHART_W,
            notes=(
                "Left cell: shift the start and the whole line moves up or down, but every rise and fall stays the same. Divergence reads the rises and falls.",
                "Right cell: the second bar went far higher and still counts as a down day, because it closed a little lower.",
            ),
        ),
        Pair(
            origin="Book p.204 and Figure 6.39.",
            left=Content(
                title="OBV bullish divergence: Citigroup",
                lines=(
                    "Citigroup's price falls to a lower low while the OBV makes a higher one.",
                    "Prices rebound strongly thereafter.",
                ),
                accent="The OBV is price-based: bullish divergence is price falling while it rises.",
            ),
            picture=Figure(
                number="6.39",
                shows="The daily chart of Citigroup with an On Balance Volume panel under it. A falling line marks price's lower lows in August to October 2011, and a rising line under the OBV, labelled bullish divergence, marks its higher lows.",
            ),
            text_w=5.4,
            notes=(
                "Part 1's rule for a price-based oscillator: bullish divergence is price falling while the oscillator rises. Point at the two lines.",
                "Compare with plain volume, where bullish divergence is volume falling with price.",
            ),
        ),
        Pair(
            origin="Book p.204 and Figure 6.40.",
            left=Content(
                title="OBV bearish divergence: copper",
                lines=(
                    "Copper's price rises, twice, while the OBV falls.",
                    "Prices fell strongly thereafter.",
                ),
                accent="Bearish divergence reads the same on both kinds: price up, the indicator down.",
            ),
            picture=Figure(
                number="6.40",
                shows="The daily chart of copper with an On Balance Volume panel under it. Two arrows mark price rising to higher peaks in 2011 while two arrows under the OBV fall, labelled bearish divergence.",
            ),
            text_w=5.4,
            notes=(
                "Two divergences, each an arrow up on price and an arrow down on the OBV.",
                "After the second one, copper fell from about 4.5 to about 3.0.",
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
            origin="Book pp.204-205 gives the calculation. C, H and L: the close, high and low of the bar, Chapter 1's OHLC. The bars and their volume are ours.",
            left=Term(
                term="Accumulation Distribution Line, ADL",
                plain="A running total of volume, each bar adding or subtracting a share of its volume by where it closed.",
                example="High PHP 52, low PHP 48, 2 million shares. Close 52: add 2.0 million. Close 50, the middle: add nothing. Close 49: subtract 1.0 million.",
                formal="Calculate the multiplying factor [(C - L) - (H - C)] / (H - L) times the period's volume, and add it to its running total: the ADL.",
            ),
            picture=Chart(
                letter="AO",
                shows="Three invented bars, each from 48 to 52 pesos on 2 million shares, worked through. Closing at the high, the factor is 1 and 2.0 million is added. Closing at the midpoint, 50, the factor is 0 and nothing is added. Closing at 49, the factor is minus one half and 1.0 million is subtracted. The ADL runs 2.0, 2.0, 1.0.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "C, H and L are the close, high and low: the OHLC of Chapter 1. Work the 49 close: (49 - 48) - (52 - 49) is 1 - 3, minus 2; over the range of 4, minus one half.",
                "The name echoes the accumulation and distribution phases of Chapters 2 and 4. The book does not connect the two.",
            ),
        ),
        Pair(
            origin="Book p.205: the algebra is the book's. The chart is ours: the factor drawn against where the close sits.",
            left=Content(
                title="How the ADL redresses the OBV",
                lines=(
                    "A close at the midpoint adds nothing: if C - L = H - C, then C = (H + L) / 2.",
                    "The further above the midpoint price closes, the more volume is added; below, the more subtracted.",
                    "At most the day's total volume is added: a close at the high makes the factor exactly 1.",
                ),
                accent="The ADL accounts for the current bar's price action. The OBV does not.",
            ),
            picture=Chart(
                letter="AP",
                shows="A straight line for the ADL's multiplying factor against where the close sits in its bar: minus 1 when the bar closes at its low, 0 at its midpoint, and plus 1 at its high.",
            ),
            text_w=CHART_W,
            notes=(
                "The line is the whole idea: the factor slides from minus one to plus one as the close moves from the low to the high.",
                "No matter how wide the range, the maximum is the day's volume, not some multiple of it: the book's words.",
            ),
        ),
        Pair(
            origin="Book p.205 and Figure 6.41.",
            left=Content(
                title="The ADL confirms, volume diverges: EURUSD",
                lines=(
                    "The ADL shows bullish confirmation, rising with price.",
                    "The volume bars show bearish divergence: an underlying weakness in the uptrend.",
                ),
                accent="The trader should wait for price confirmation of a reversal before taking part.",
            ),
            picture=Figure(
                number="6.41",
                shows="An hourly EURUSD chart rising to a top, with an A/D line panel rising alongside it, labelled bullish confirmation, and a volume panel falling, labelled bearish divergence, under the heading divergence between volume and ADL.",
            ),
            text_w=5.4,
            notes=(
                "The two kinds again, disagreeing: the price-based ADL rises with price, plain volume falls.",
                "The book does not pick one. It says wait for price to confirm before acting.",
            ),
        ),
        Pair(
            origin="Book pp.205-206 and Figure 6.42.",
            left=Content(
                title="OBV and ADL together: trend or range",
                lines=(
                    "When the OBV and the ADL rise or fall together, price trends in a decisive manner.",
                    "When they move in opposite directions, price tends to range or consolidate.",
                    "Useful for gauging behavioral or regime changes in the market.",
                ),
                accent="It may help decide between a trend-following and a range-bound strategy.",
            ),
            picture=Figure(
                number="6.42",
                shows="The daily chart of Exxon Mobil with OBV and ADL panels. On the left the two move apart, non-confirmation, under an erratic and volatile price; on the right they rise together, confirmation, under a pronounced trend.",
            ),
            text_w=5.4,
            notes=(
                "Left ellipse: the OBV falls while the ADL rises, and price goes nowhere. Right ellipse: both rise, and price trends.",
                "Regime is the book's word for the market's mode: trending or ranging, as in Chapter 4's phases.",
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
            origin="Book p.206 gives the calculation, not the two EMA lengths. EMA: an exponential moving average, Chapter 11. N: a number of periods. The bars and volumes are ours.",
            left=Term(
                term="Chaikin Money Flow and Chaikin Oscillator",
                plain="CMF: the ADL's signed volume over N bars, over their volume. The oscillator: two averages of its running total.",
                example="Signed volumes 2.0, 0 and -0.5 million on volumes 2.0, 1.0 and 1.0 million: CMF = 1.5 / 4.0 = 0.375.",
                formal="S is the multiplying factor times volume. N-period CMF: the N-period sum of S over the N-period sum of volume. Chaikin oscillator: a shorter-term EMA less a longer-term EMA of the CMF's running total.",
            ),
            picture=Chart(
                letter="AQ",
                shows="The Chaikin Money Flow worked for three invented bars. Left, each bar's signed volume S: 2.0, 0 and minus 0.5 million, adding to 1.5. Middle, each bar's volume: 2.0, 1.0 and 1.0 million, adding to 4.0. Right, the result: 1.5 divided by 4.0, a CMF of 0.375.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "S is the same signed volume as the ADL's. The CMF divides its total over N bars by the volume of those bars, so it stays between minus one and one.",
                "The book says to make a running total of the CMF, as for the ADL, and take the oscillator from that. It gives no lengths for the two EMAs; its figure prints 3 and 10.",
                "EMA is an exponential moving average: named here, taught in Chapter 11. N is the number of periods, as in Chapter 5.",
            ),
        ),
        Pair(
            origin="Book p.206 and Figure 6.43. The figure prints CMF(20) and ChiOsc(3,10); the text gives no settings.",
            left=Content(
                title="The Chaikin pair on copper",
                lines=(
                    "The sell, or bearish, signal: each breaks the rising line drawn under it. The Chaikin oscillator breaks first, the CMF later.",
                    "Oversold levels on both point to a potential market bottom in copper around October 2011.",
                ),
                accent="The Chaikin oscillator gives the earlier signal.",
            ),
            picture=Figure(
                number="6.43",
                shows="The daily chart of copper with a Chaikin oscillator panel and a Chaikin Money Flow panel. Rising lines mark both before a top in August, with dashed arrows to the top, and both panels carry a line labelled oversold that both touch near the October low.",
            ),
            text_w=5.4,
            notes=(
                "Follow the dashed arrows from each panel up to the top: the oscillator's arrow comes first.",
                "Oversold again: used, not defined, as in Part 2.",
            ),
        ),
        Pair(
            origin="Book p.206 and Figure 6.44. Its line is labelled cumulative and runs below zero, which a ratio cannot; the book does not explain.",
            left=Term(
                term="NYSE Up/Down Volume",
                plain="Volume in the NYSE's rising stocks set against volume in its falling ones.",
                example="Figure 6.44: the indicator breaks its rising trendline first, an early bearish signal; the NYSE Composite breaks later.",
                formal="The ratio of advancing volume over declining volume. Being non-price-based, its divergence is read like volume bars and smoothed and detrended volume.",
            ),
            picture=Figure(
                number="6.44",
                shows="Two daily panels, 2009 to 2011: the NYSE Advance-Decline Volume line above, labelled cumulative, breaking its rising trendline at a point marked early bearish signal; and the NYSE Composite Index below, breaking its own trendline later, circled as price confirmation.",
            ),
            text_w=6.8,
            notes=(
                "Read it as the book does: the volume indicator breaks first, price confirms later.",
                "Say the gap plainly: the text says ratio; the figure's line is cumulative and goes negative. The book does not reconcile them.",
            ),
        ),
        Term(
            origin="Book pp.207-208. The book gives no formula and no figure for it, so this slide has no picture.",
            term="Herrick Payoff Index",
            plain="A price-based volume oscillator that also uses open interest, so it can only be used where there is open interest: futures and options.",
            example="On a gold futures chart it can be read. On a PSE share, which has no open interest, it cannot.",
            formal="The Herrick Payoff Index uses open interest in its calculations, so it may only be used with futures and options. It incorporates price, so its divergence is read as for all price-based volume oscillators. Bearish signals: money flowing out; bullish signals: money flowing in.",
            notes=(
                "Open interest was Part 4: only futures and options have it, which is why this index is limited to them.",
                "It may be read with any or all of the eight methods of the part's first slide.",
            ),
        ),
        Pair(
            origin="Book p.208 gives the report and its two uses; it does not define net. The chart is ours, on invented prices and open interest.",
            left=Term(
                term="Commitment of Traders, COT, report",
                plain="A weekly report of who holds the open positions in a futures market, group by group.",
                example="Traders look for changes in the net commercial or non-commercial positions, and for a test of a significant or historical open interest level.",
                formal="Released every Friday, it reports all open positions held by commercials (hedgers, non-cash positions), non-commercials (hedge funds, financial institutions, large traders) and, in aggregate, small traders.",
            ),
            picture=Chart(
                letter="AR",
                shows="An invented futures price rising to a top, with its open interest underneath climbing to a dashed line drawn at its earlier historical peak. The test of that level, at the top, is marked: one of the two things the book says traders look for in the report.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Traders use it to find potential tops and bottoms. The book says net position and does not define net; do not supply a formula.",
                "Hedgers were named in Chapter 1 among the participants. Commercial and non-commercial are the report's own groups.",
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
        caption="The last is not taught in this chapter's text. Chapter 3 read volume across contract months.",
        notes=(
            "These are the book's six learning objectives. Say the first and the fifth, and that every one is examinable.",
            "Be straight about the sixth: the chapter's text never comes back to contract months. Chapter 3's rollover slides are where it was taught.",
        ),
    ),
    Content(
        origin="The parts are the book's own sub-sections, pp.173 to 208, grouped in its order.",
        title="How this chapter is laid out",
        lines=(
            "Part 1  Confirmation and divergence.  Part 2  Timing, the VWMA, climaxes.",
            "Part 3  Price barriers and filtering.  Part 4  Open interest, tick volume, the TRIN.",
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
        origin="Book p.208: its summary is three sentences. These five are ours, of the whole chapter.",
        title="Chapter 6 in five sentences",
        lines=(
            "Volume is participation: moving with price, bullish; against it, bearish.",
            "Volume falling is divergence, rising is confirmation, whatever price does.",
            "Minimum volume times breakouts and reversals; extreme volume, climaxes.",
            "Barriers, filters and volume by price pick out the volume that matters.",
            "Open interest reads like volume; the OBV, ADL and Chaikin pair use price.",
        ),
        accent="The book's summary: price-based volume oscillators read differently.",
        notes=(
            "Read all five slowly. This is the summary to copy down.",
            "The book's summary adds that volume divergence and filtering are used throughout the rest of the book.",
        ),
    ),
    Content(
        origin="Book p.208.",
        title="The review questions to prepare",
        lines=(
            "Volume against tick volume? Bearish and bullish volume?",
            "How is volume divergence distinct from standard oscillator divergence?",
            "How would you use volume as a timing indicator?",
            "The various modes of volume filtering?",
            "The relationship between volume, open interest and price?",
            "Absolute or relative volume? Volume cycles: their use, and where?",
        ),
        caption="The book's eight questions, on six lines: the first and last lines carry two each.",
        notes=(
            "Say where each answer sits, line by line: Parts 4 and 1, Part 1, Part 2, Part 3, Part 4, then Parts 4 and 5.",
            "Question 3 is the one most likely to be answered wrongly: volume divergence ignores price's direction.",
        ),
    ),
    Content(
        origin="This course's own list, drawn from the chapter's slides. The numbers after Sent ahead are the book's chapters.",
        title="What the book uses, and where it says two things",
        lines=(
            "Used, not explained: overbought, oversold, Bollinger Bands and Bandwidth, MACD, EMA, the tick, the cycle-tuned stochastic.",
            "Named only: the Demand Index, detrended volume, ROC volume, the PVO.",
            "Sent ahead, by chapter: oscillators 8, divergence 9, moving averages and the VWMA's calculation 11.",
            "Two answers: above the VWMA, bullish or overvalued; a bullish TRIN, overbought or oversold; the up/down line, ratio or cumulative.",
        ),
        accent="Where the book disagrees with itself, the slide says so.",
        notes=(
            "Be straight with them: this chapter leans on oscillators the book teaches in Chapter 8.",
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
