"""Chapter 5 content for FIN1209 - Trend Analysis.

This file is pure data. It carries no drawing code.

Source of the chapter scope is Lim, M. (2016), The Handbook of Technical
Analysis, chapter 5, printed pages 125 to 171, which students have in the
course text. Everything here is written from scratch in teaching language.

This chapter follows the lean form the instructor approved in Chapter 4, and
the three rules that form was sent back for and rewritten to:

  * **Every idea has a picture beside it.** Every teaching slide is a Pair:
    the idea on the left and a picture on the right. Where the book has a
    figure, it is the book's, and all 59 of the chapter's figures are
    placed. Where the book makes the point only in words, it is one of our
    own charts; see charts_chapter05.py for which and why. Five slides
    carry no picture, and each is a list the book gives without one: the
    sixteen characteristics by name, the one sentence on divergence that
    the book sends to Chapter 9, the other orders, the strengths and
    weaknesses of trendline analysis, and the reversal signs that need a
    tool a later chapter teaches. No two of them are next to each other.

  * **A question and its answer are separate slides.** Every check is an
    ordinary Check: a question slide, then a reveal slide.

  * **The book's content is not cut.** The lean rule cuts a slide that
    teaches nothing new: a divider, a recap, a figure standing alone with no
    words. It never cuts what the book says.

And one rule the instructor added when he reviewed the first build of this
chapter, which had marked the uptrend as new and left HWC and MWC unmarked:

  * **A Term slide is a term's first teaching in the course, and nothing
    else.** Every name in this chapter was checked against
    content_chapter01.py to content_chapter04.py. The uptrend, and stop and
    limit orders, were terms in Chapters 2 and 1, so they are ordinary
    slides here with the recall in the speaker cue. Twenty seven names the
    book introduces in this chapter gained the marker. TEMPLATE.md has the
    rule and chapter-05/README.md the list, with what was left alone and
    why.

And one he added when he reviewed the second, which named HWC, MWC and LWC
on a slide that spoke of wave degrees before any slide had said what one is:

  * **A word is explained before a slide leans on it.** The wave cycle and
    the wave degree get a plain slide and a chart of their own before the
    term that is built from them. A word that arrives ahead of the section
    that teaches it carries that section's number on the slide, and a word
    the book never explains is said to be unexplained, on the slide and not
    only in the cue. chapter-05/README.md has the list.

And one from his third review, when the degree slide and Figure 5.5 still
left him asking what the three lines are and what they are drawn from:

  * **A drawing convention is taught, not assumed.** Two slides after the
    term say how the three cycles are drawn and how to tell them apart, on
    one price drawn as bars with the two larger waves over it. The book
    gives no rule for either, and each slide says which part is the book's
    and which is our drawing choice.

And one from his fourth, when the breakout slide read as a contradiction of
Chapters 2 and 4, which had used the word only of price leaving a range:

  * **A word from an earlier chapter means what it meant there, or the
    slide says what changed.** Breakout is recalled by chapter, then
    widened to any level, then shown at each wave degree, on four slides
    with three charts of our own. Every other term of Chapters 1 to 4 was
    checked the same way, and each recall names its chapter on the slide
    and not only in the cue, because the instructor studies from a PDF that
    has no cues. Three more book sketches got a companion chart on price
    bars: Figures 5.7, 5.8 and 5.9. chapter-05/README.md has the table.

What is lean, against Chapters 1 to 3:

  * The parts are the book's own sections, 5.1 to 5.11. Section 5.12 is the
    book's summary and feeds the closing slides.
  * No divider slide and no recap slide. The first slide of a part carries
    the book's section number in its title.
  * A picture sits beside its idea, not on a slide of its own after it.
    Figure 5.32 is the one exception: it is a wide table of small type, and
    a slide of its own is the only size it can be read at.

A check sits in the part whose last slide it follows, so one check can ask
about two short sections: Check 19 covers 5.7 and 5.8, and Check 20 covers
5.9 and 5.10.

Where the standing rule bites, and how each place is handled. Every one is
named on a slide, and no check rests on any of them.

  * Sixteen or twelve. Section 5.2 lists 16 price characteristics, and so
    does the chapter summary. Review question 4 asks for "the 12 ways in
    which price action may be understood". The deck teaches the sixteen and
    the review slide says so.

  * Four modes or five. Section 5.5 announces "four simple ways" of
    initiating an entry and lists five. The slide lists the five and says
    so.

  * Figure 5.24. The text gives Gold's trend rate as about $3.30 a day and
    the figure itself prints $3.80. The book's caption under 5.24 is the
    caption of Figure 5.25. The slide says both.

  * Figure 5.46. Its printed caption repeats Figure 5.45's and says Silver;
    the text says USDCAD. The slide says so.

  * Algorithmic filters. Section 5.3 files them as one branch of the
    event-based filters. Review question 8 names "time and algorithmic
    filters" as though algorithmic were the third category, which is how
    Chapter 1's prose put it. The slide says so.

  * Limit orders "or better, that is, higher". The book says this of all
    four limit cases, the buy limits included. The slide quotes it and
    teaches "at the specified price, or better".

  * The stop order sentence. The book writes that a stop order "cannot
    guarantee that an order will be executed, or filled at the specified
    price, but it can guarantee execution". Its later sentences say three
    times that a stop exit is guaranteed and its exact price unknown. The
    slide teaches that reading and the speaker cue quotes the sentence.

  * Ninety percent. The book says ninety percent of period ranges stay
    below the two standard deviation value. The slide gives it as the
    book's figure.

  * Things the chapter uses and never explains: typical price, the
    cycle-tuned stochastic, MACD, the standard stochastic and %K, the CCI,
    Floor Trader's Pivot Points, Bollinger and linear regression bands,
    candlestick patterns, DeMark's qualification of a trough, and
    divergence, which it sends to Chapter 9. Each is named where it appears
    and the closing slides collect them. The true range was Chapter 3; how
    it is averaged into the ATR is Chapter 8.
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

# The text column beside one of our own charts. charts_chapter05.py draws
# every chart to fill the picture column these two widths leave.
CHART_W = 5.6
TERM_CHART_W = 6.2

# ==========================================================================
# 5.1 - Definitions of a trend.
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Definitions of a Trend",
    short="5.1 Definitions",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.1  Dow sorts trends by how long they last",
                lines=(
                    "Primary, or major, trends are longer term: months to years.",
                    "Secondary trends, or reactions, are medium term: weeks to months.",
                    "Minor trends are shorter term: days to weeks.",
                ),
                accent="In Dow Theory, trends are classified and defined by their duration and extent.",
                caption="Chapter 2 taught all three: the primary trend, the secondary reaction and the minor trend.",
            ),
            picture=Chart(
                letter="A",
                shows="One invented price line: a primary trend rising across the whole chart, a secondary reaction falling against it for a while, and the small minor trends inside both.",
            ),
            text_w=CHART_W,
            notes=(
                "Link back to Chapter 2: the same three trends. Today's question is what a trend is, and how to tell a healthy one.",
                "Point at the chart: the long rise is the primary trend, the fall inside it a secondary reaction, the small swings minor trends.",
            ),
        ),
        Pair(
            left=Content(
                title="An uptrend: higher highs and higher lows",
                lines=(
                    "An uptrend is represented by a series of successively higher highs, the peaks, and lows, the troughs.",
                    "Each rally carries above the last peak: a higher high, HH.",
                    "Each dip holds above the last trough: a higher low, HL.",
                ),
                accent="The same definition as Chapter 2: Dow's peak and trough analysis.",
                caption="A share peaks at PHP 50, dips to 46, peaks at 54, dips to 49: higher highs and higher lows.",
            ),
            picture=Figure(
                number="5.1",
                shows="A rising bar chart with every peak marked HH and every trough HL, labelled an uptrend as a sequence of higher highs and higher lows, and a flat stretch at the end where the uptrend has technically ended.",
            ),
            text_w=5.6,
            notes=(
                "A recall, not a new term: Chapter 2 defined the uptrend the same way. This is review question 1, what is a trend.",
                "HH is a higher high and HL a higher low. Where the sequence stops, the figure says the uptrend has technically ended.",
            ),
        ),
        Pair(
            left=Content(
                title="A downtrend: lower highs and lower lows",
                lines=(
                    "A downtrend is represented by a series of successively lower highs and lows.",
                    "Each rally stops below the last peak: a lower high, LH.",
                    "Each decline carries below the last trough: a lower low, LL.",
                ),
                accent="Peak and trough analysis is the most popular definition of a trend.",
            ),
            picture=Figure(
                number="5.2",
                shows="A falling bar chart labelled a downtrend unfolding, with its first peak marked H, its first trough L, and after them three lower highs marked LH and three lower lows marked LL.",
            ),
            text_w=6.8,
            notes=(
                "Read the labels left to right: H, L, then LH and LL three times over.",
                "The definition asks for both, lower highs and lower lows, one after another.",
            ),
        ),
        Pair(
            left=Content(
                title="Where the definition runs out",
                lines=(
                    "Scenarios 1 and 2 show higher highs and higher lows: uptrends under Dow.",
                    "Scenario 3 has no higher highs or lows. Scenario 4 has no highs or lows at all.",
                    "Under the definition neither is an uptrend. Yet in all four, price went from A to B.",
                ),
                accent="All definitions impose limitations: an actual trend may go unrecognized.",
                caption="Erratic or chaotic price action can also make peaks and troughs extremely hard to identify.",
            ),
            picture=Figure(
                number="5.3",
                shows="Four paths from a point A up to a point B. The first two zigzag through higher highs and higher lows and are labelled uptrend. The third has one high and one low, the fourth is a straight line, and both are labelled uptrend with a question mark.",
            ),
            text_w=5.2,
            notes=(
                "This is review question 2: the disadvantages of defining market and price action.",
                "Ask the room: do we deny that scenarios 3 and 4 were trends? The book leaves it as a question.",
            ),
        ),
        Pair(
            left=Content(
                title="Three other ways to call a trend intact",
                lines=(
                    "To avoid depending on how price behaves, many practitioners use other means:",
                    "Price remaining above or below an overlay indicator: a trendline, a moving average.",
                    "Price remaining above or below an arbitrarily chosen price level.",
                    "The absence of a reversal of a specified amount: Point and Figure, Renko.",
                ),
                accent="An absolute measure: the distance traversed, not the behavior of price.",
            ),
            picture=Figure(
                number="5.4",
                shows="Three rising prices, each labelled trend still intact: one remaining above a dotted trendline, one remaining above a chosen level, and one climbing through stacked boxes with the minimum reversal amount not breached.",
            ),
            text_w=5.6,
            notes=(
                "Left to right in the figure: above a trendline, above a chosen level, no reversal of the minimum amount. The converse holds for downtrends.",
                "Other overlays the book names: the lower Bollinger, linear regression and moving average band, and the lower boundary of a chart pattern.",
                "The chosen level is often a historically significant support, whose violation implies a very high probability of the trend reversing.",
            ),
        ),
        Check(
            label="What a trend is",
            questions=(
                Q(
                    stem="Under Dow's peak and trough definition, an uptrend is a series of successively:",
                    options=("Higher highs and lower lows",
                             "Higher highs and higher lows",
                             "Lower highs and lower lows",
                             "Higher closes only"),
                    answer="B",
                    reason="An uptrend is successively higher highs, the peaks, and higher lows, the troughs.",
                ),
                Q(
                    stem="Price rises from A to B in one straight move, with no peaks or troughs at all. Under Dow's definition this is:",
                    options=("A primary uptrend",
                             "A secondary reaction",
                             "A downtrend",
                             "Not classified as an uptrend"),
                    answer="D",
                    reason="With no higher highs or lows there is nothing for the definition to recognize, even though price travelled from A to B.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="What a wave degree is",
                lines=(
                    "Price moves in swings, up and back down. The book calls a swing a wave cycle.",
                    "Small swings ride inside bigger ones. The smaller is a subwave of the bigger.",
                    "Degree is the rank of a wave by size: the bigger swing is of a higher degree, its subwaves of a lower one.",
                    "The book: any trend or consolidation can be described in wave cycles, which exist at various wave degrees.",
                ),
                caption="Chapters 3 and 4 said wave cycle and cycle degree in passing. The book defines neither; this reading is from its figures.",
            ),
            picture=Chart(
                letter="AA",
                shows="One wave drawn three times, side by side. First a single large wave cycle, alone: the highest degree. Then the same wave with smaller wave cycles inside it, its subwaves, of a lower degree. Then with smaller ones again inside those, the lowest degree of the three.",
            ),
            text_w=CHART_W,
            notes=(
                "Teach this slide before anything is named. Left drawing: one wave. Middle: the same wave, in green, with smaller waves riding along it. Right: smaller ones again riding along those.",
                "Each added wave is a subwave of the one it rides on, and one degree lower. Two drawings are two degrees, three are three.",
                "A degree is not an angle and not a fixed size: it only says which of two waves is the bigger. The reading rests on the book's figures and its words larger, smaller and subwave; Chapters 3 and 4 used the words and explained neither.",
            ),
        ),
        Pair(
            left=Term(
                term="Wave cycles: HWC, MWC and LWC",
                plain="Three wave degrees on one chart, named by size against each other.",
                example="In the figure: HWC thick, MWC dotted, LWC thin. Three degrees here; the minimum in any trend is two.",
                formal="HWC, the higher wave cycle: the highest wave degree. MWC, the medium wave cycle: a subwave of the HWC, of a lower degree. LWC, the lower wave cycle: a subwave of both, at the lowest degree.",
            ),
            picture=Figure(
                number="5.5",
                shows="A wave of three degrees: one thick line rising and falling, the higher wave cycle; a dotted line weaving around it, the medium wave cycle; and a thin jagged line weaving around that, the lower wave cycle.",
            ),
            text_w=6.0,
            notes=(
                "Three wave cycles laid over one another: the thick line is the HWC, the dotted line the MWC, the thin line the LWC.",
                "Higher, medium and lower are relative to each other. The book fixes no size or duration for any of them.",
                "It gives the minimum of two degrees as a note, with no reason. Do not supply one.",
            ),
        ),
        Pair(
            left=Content(
                title="How the three cycles are drawn",
                lines=(
                    "The LWC is the price itself: a thin line in the book, the bars on a price chart.",
                    "The MWC and HWC are not prices. Each is a smooth line through the middle of the smaller swings, to show the bigger swing.",
                    "The book gives no rule for drawing them: no formula, no indicator, no number of bars.",
                ),
                accent="They look like moving averages. The book does not say they are.",
                caption="The book's: thick, dotted, thin. Ours: the bars, and where the two smooth lines sit.",
            ),
            picture=Chart(
                letter="AB",
                shows="One invented price drawn as bars, the lower wave cycle. A dotted line runs through the middle of the small swings of the bars, the medium wave cycle. A thick line runs through the middle of the dotted line's swings, rising once and falling once across the chart, the higher wave cycle.",
            ),
            text_w=CHART_W,
            notes=(
                "The question a student asks of Figure 5.5 is what the three lines are. The thin one is price. The other two are drawn over price to show its bigger swings.",
                "Why draw them at all: the book calls it critical that a trader be able to visualize price cycles on the chart. Its figures are freehand sketches, with no bars and no price axis.",
                "Be plain that the book stops there. It names no indicator and gives no length, so do not say the lines are moving averages of any period. Moving averages are Chapter 11.",
            ),
        ),
        Pair(
            left=Content(
                title="Telling the three cycles apart",
                lines=(
                    "Compare the swings with each other. The book fixes no size, duration or timeframe.",
                    "The smallest swings in view: the LWC. The bigger swing they ride on: the MWC. The biggest: the HWC.",
                    "Subwave test: LWC swings sit inside one MWC swing, MWC swings inside the HWC swing.",
                ),
                accent="Relative: a wave has a degree only against another wave.",
                caption="Bar counts and pesos are read off our invented chart, not the book.",
            ),
            picture=Chart(
                letter="AC",
                shows="The same price bars with the dotted medium wave cycle and the thick higher wave cycle, and three rulers underneath: one lower wave cycle swing is 8 bars and about 6 pesos, one medium wave cycle swing is 32 bars and about 12 pesos, and the higher wave cycle swing is all 96 bars and 24 pesos.",
            ),
            text_w=CHART_W,
            notes=(
                "Read the three rulers from the top: each swing is longer and taller than the one above it, and holds four of it. Four is this chart's number, not a rule.",
                "Each degree also has its own average size of swing. The book's words are the average wave amplitude and volatility associated with that particular wave degree, and they come up with breakouts in a moment.",
                "Chapter 9 comes back to wave degrees and says the relationship between them is relative. Chapter 18 gives Elliott's named degrees. Neither is needed here.",
            ),
        ),
        Pair(
            left=Content(
                title="Know which wave cycle you are trading",
                lines=(
                    "Without knowing which one is traded, a trader may be unable to:",
                    "Select consistent breakout levels, or effective stoploss levels.",
                    "Apply effective stopsizing.",
                    "Distinguish between trend and consolidation mode.",
                    "Determine the direction of the predominant trend.",
                ),
                caption="Breakout levels: later in 5.1. Stoploss: 5.4. Stopsizing: 5.5. Elliott, met in Chapter 4, is Chapter 18.",
            ),
            picture=Figure(
                number="5.6",
                shows="One rise labelled at three wave degrees: i to v and a to c at the lowest degree, 1 to 3 at the medium degree, and [1] at the highest, under the heading Elliott wave in terms of wave degrees.",
            ),
            text_w=5.4,
            notes=(
                "The book calls it critical that a trader be able to visualize price cycles on the chart. Its five inabilities sit on four lines here.",
                "The figure labels one rise three ways. Point at the three sets of labels and do not teach the count: that is Chapter 18.",
            ),
        ),
        Pair(
            left=Content(
                title="Trending and consolidating at once",
                lines=(
                    "Chapter 4: a market is either trending or consolidating.",
                    "Chapter 5 adds: it may be both at the same time, depending on the wave cycle being observed.",
                    "In the figure the small LWC climbs each swing: trend mode. The MWC swings across one level: ranging mode. The large HWC is flat: flatline mode.",
                ),
                accent="Ask at which wave degree before asking whether it is trending.",
            ),
            picture=Figure(
                number="5.7",
                shows="A flat thick arrow, the higher wave cycle in flatline mode; a dashed wave swinging above and below it, the medium wave cycle in ranging mode; and a thin jagged line climbing each swing, the lower wave cycle in trend mode.",
            ),
            text_w=5.8,
            notes=(
                "Three answers to one question on one chart: flat, ranging, trending. Ranging and flatline are the figure's labels; the text says only trend and consolidation, and says mode where Chapter 4 said phase.",
                "Chapter 4's consolidation phase was the sideways stretch, one of only two basic phases. Nothing there is withdrawn; this chapter adds that the phase depends on the wave being read.",
            ),
        ),
        Pair(
            left=Content(
                title="One market, three modes, on price bars",
                lines=(
                    "The bars are the LWC. Bar by bar they climb, then fall: trend mode, up and then down.",
                    "The dotted MWC swings between about PHP 54 and PHP 66 and gets nowhere: ranging mode.",
                    "The thick HWC stays at PHP 60: flatline mode.",
                ),
                accent="One chart. Whether it is trending depends on which wave is read.",
                caption="The three modes are the book's. The bars and the pesos are our invented chart.",
            ),
            picture=Chart(
                letter="AH",
                shows="One invented price drawn as bars that rise and fall three times between about 54 and 66 pesos. A gold arrow under one rise marks the lower wave cycle in trend mode, the dotted medium wave cycle swings across one level in ranging mode, and the thick higher wave cycle is a flat line at 60 pesos in flatline mode.",
            ),
            text_w=CHART_W,
            notes=(
                "The same idea as the book's sketch, on bars. Point at the gold arrow first: along it every small swing ends higher than the last, an uptrend to anyone trading the bars.",
                "Then the dotted line: up to 66, down to 54, three times over. To the trader of that wave nothing has happened.",
                "Then the thick line. Three traders, one chart, three true answers.",
            ),
        ),
        Check(
            label="Wave cycles",
            questions=(
                Q(
                    stem="Of the three wave cycles, the one that is a subwave of both of the others is the:",
                    options=("Higher wave cycle, HWC",
                             "Lower wave cycle, LWC",
                             "Medium wave cycle, MWC",
                             "None: each is a subwave of only one"),
                    answer="B",
                    reason="The LWC is a subwave of both the HWC and the MWC, at the lowest wave degree. The MWC is a subwave of the HWC only.",
                ),
                Q(
                    stem="A market's lower wave cycle is rising while its medium wave cycle moves sideways. The market is in:",
                    options=("Trend mode only",
                             "Consolidation mode only",
                             "Both, depending on the wave cycle observed",
                             "Neither, until a breakout occurs"),
                    answer="C",
                    reason="A market may be in trend and consolidation modes at the same time, depending on the wave cycle being observed.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Breakout, as Chapters 2 and 4 used it",
                lines=(
                    "Chapter 2: a line, a narrow sideways range, usually results in a strong breakout.",
                    "Chapter 4: most call a consolidation over on a clear technical breakout from the range, and the trend phase follows.",
                    "In both, price leaves a sideways range through its top or its bottom.",
                ),
                accent="So far, a breakout has been price getting out of a range.",
                caption="No chapter gave breakout a definition of its own, and neither does the book. This is how the word has been used.",
            ),
            picture=Chart(
                letter="AD",
                shows="An invented share that falls, then ranges between 40 and 44 pesos, the consolidation, boxed. A gold line marks the top of the range at 44. Price leaves the range through that top, the breakout, and the trend that follows carries it to 56.",
            ),
            text_w=CHART_W,
            notes=(
                "A recall, not a new term, and it is here because the word is about to be used more widely. Chapter 2's line and Chapter 4's consolidation both ended in a breakout from a range.",
                "The chart is Chapter 4's own example again: a share ranging between PHP 40 and PHP 44. The gold line is the top of the range, and the breakout is where price gets through it.",
                "Ask the room what the breakout was a breakout of. The answer to hold on to is a level: the top of the range.",
            ),
        ),
        Pair(
            left=Content(
                title="Chapter 5: a breakout is through a level",
                lines=(
                    "The edge of a range is one kind of level. Chapter 5 breaks out of others:",
                    "a prior peak or trough, a trendline, a channel line, any price overlay.",
                    "Each time, a level holds price and then price gets through it.",
                ),
                accent="Same word, wider use: the level need not be the edge of a range.",
                caption="The book never defines breakout. Chapter 2 called price going through a previous peak or trough a penetration.",
            ),
            picture=Chart(
                letter="AE",
                shows="Four small drawings, each with the level price gets through in green: the top of a range, from Chapters 2 and 4; a prior peak, of which there is one at every wave degree, section 5.1; a trendline, sections 5.2 and 5.6; and a channel line, section 5.6.",
            ),
            text_w=CHART_W,
            notes=(
                "This is the slide that reconciles the two uses. A breakout is price getting through a level that was holding it. The top of a range is such a level, and so is a prior peak, a trendline or a channel line.",
                "It is not new to this chapter either. Chapter 1's price filter asked price to move a set distance past the level, and Chapter 3's breakout level was 10.00.",
                "Be straight that the definition is ours, from use. The book says breakout, penetration, violation and breach of a level and never sets one against another; in Chapter 2 it wrote inflection point breakouts for what it had called penetration.",
            ),
        ),
        Pair(
            left=Content(
                title="A breakout for every wave degree",
                lines=(
                    "Breakouts can be defined by the degree of the wave cycle: lower, medium or higher.",
                    "The breakout level depends on the wave degree being traded.",
                    "Knowing the degree lets the trader size the stoploss to that degree's average wave amplitude and volatility.",
                ),
                accent="Volatility at one wave degree may not manifest at a higher or lower degree.",
                caption="In the figure each B/OUT LEVEL is a line across a prior peak of one wave cycle. Amplitude: 5.2. Stoploss: 5.4.",
            ),
            picture=Figure(
                number="5.8",
                shows="One price path with breakout levels drawn at three sizes: short LWC breakout levels on the small swings, two MWC breakout levels on the medium swings, and one HWC breakout level across the top of the whole move.",
            ),
            text_w=5.4,
            notes=(
                "Count the levels in the figure: several small ones, two medium, one large. Each is a horizontal line across a peak, and each is a breakout to somebody.",
                "Each wave cycle has peaks of its own, so each has levels of its own. That is read off the figure; the three lines are the book's sentences.",
                "Stopsizing comes back in section 5.5. For now: a stop sized for one degree is the wrong size for another.",
            ),
        ),
        Pair(
            left=Content(
                title="One price passes three breakout levels",
                lines=(
                    "LWC: passes the last small peak, PHP 57.",
                    "MWC: passes the last medium peak, PHP 60.",
                    "HWC: passes the top of the whole move, PHP 71.",
                    "The 67 bars under that top are a consolidation at a higher degree, and this is its breakout.",
                ),
                accent="Chapter 4's breakout from a range is one of these.",
                caption="Levels are read off our invented chart. The last line is our reading; the book does not join the two uses.",
            ),
            picture=Chart(
                letter="AF",
                shows="One invented price drawn as bars that rises to a top near 71 pesos, falls to about 48 and climbs back through it. Three gold lines mark breakout levels, each across a prior peak: a short one at about 57, the lower wave cycle; a longer one at about 60, the medium wave cycle; and the longest at about 71, the higher wave cycle, across the top of the whole move.",
            ),
            text_w=CHART_W,
            notes=(
                "Three traders watch one price. Each is waiting for a different gold line, and each calls a different bar the breakout.",
                "Then the link back. This section has just said a market can trend at one degree and consolidate at another. The long stretch under the top is that: a fall and a recovery to one trader, a sideways range to a trader of a larger wave.",
                "So nothing taught in Chapters 2 and 4 is withdrawn. A breakout from a range is a breakout through a level, at the degree where the range can be seen.",
            ),
        ),
        Pair(
            left=Term(
                term="Wave-degree convergence",
                plain="When the biggest wave turns, every smaller wave turns with it. That is why bigger turning points matter more.",
                example="At a major top the HWC, the MWC and the LWC all turn down together.",
                formal="When a large wave cycle reverses, all the wave cycles of lower degrees reverse in sync with it. Waves of higher degrees need not reverse when waves of lower degrees reverse.",
            ),
            picture=Figure(
                number="5.9",
                shows="The three wave cycles rising to one peak and turning down together, with the peak labelled all subwaves reversing in sync with the highest wave degree.",
            ),
            text_w=5.6,
            notes=(
                "The arrow at the top of the figure marks the one moment all three degrees turn at once.",
                "It runs one way only: the small waves reverse many times on the way up without the large one turning.",
            ),
        ),
        Pair(
            left=Content(
                title="Lower degrees turn alone. The highest does not.",
                lines=(
                    "On the way up the LWC turns down again and again, and the rise goes on.",
                    "The MWC turns down as well, with the LWC, and the HWC still rises.",
                    "At the top the HWC turns down, and the MWC and the LWC turn with it.",
                ),
                accent="A turn of the largest wave is a turn of every wave. That is why it is the significant one.",
                caption="Convergence in Chapter 3 was a futures price meeting the spot price. Here it is wave degrees turning together.",
            ),
            picture=Chart(
                letter="AI",
                shows="One invented price drawn as bars that rises to a single top and falls, with the dotted medium wave cycle and the thick higher wave cycle over it. Three points are marked: on the way up, a place where the medium and lower wave cycles turn down and the higher does not; a place where only the lower wave cycle turns down; and the top, where the higher wave cycle turns down and both smaller cycles turn with it.",
            ),
            text_w=CHART_W,
            notes=(
                "The book's two sentences, one after the other on the same bars: all subwaves of the largest wave reverse together, and waves of higher degrees need not reverse when waves of lower degrees do.",
                "Left mark: the dotted line and the bars turn down and the thick line keeps rising. Middle mark: only the bars turn. Gold mark: all three.",
                "Chapter 3 used convergence for futures and spot prices at expiry. Same word, a different thing, and the caption says so.",
            ),
        ),
        Pair(
            left=Term(
                term="Correction and pullback",
                plain="A small move against the trend: shallow, usually no more than a few percent.",
                example="A share climbs from PHP 40 to PHP 50, then dips to PHP 49: a correction, or pullback.",
                formal="Reversals and retracements imply a turnaround in prices, and may be of any amount or degree. Corrections and pullbacks tend to imply a more shallow reversal or retracement, usually no more than a few percent.",
            ),
            picture=Chart(
                letter="B",
                shows="An uptrend with one small dip marked a correction or pullback, usually no more than a few percent, and later one large fall marked a reversal or retracement, which may be of any amount or degree.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Reversal and retracement have been in use since Chapter 2, and correction has appeared in passing. This slide is where correction and pullback get their meaning: the small case.",
                "The book uses all four words through the rest of the chapter. This is the one place it says how they differ.",
            ),
        ),
        Pair(
            left=Content(
                title="A trend in the highs, the lows or the closes",
                lines=(
                    "Trend may also be defined on individual open, high, low and close data.",
                    "Peak and trough analysis can show a flat market while the closes rise bar after bar.",
                    "Rising closes are an uptrend as far as close prices are concerned: Chapter 3's line chart in action.",
                    "The same holds for the highs, the lows, and the mid or typical prices.",
                ),
                caption="The book names typical price, and the CCI oscillator and Floor Trader's Pivot Points that are based on it, and defines none of them here.",
            ),
            picture=Figure(
                number="5.10",
                shows="Three rows of bars under the heading OHLC-based trend: bar highs rising while bar lows fall, bar closes rising steadily and labelled equivalent to a line chart, and flatline action based on typical and midprices.",
            ),
            text_w=5.8,
            notes=(
                "Top row of the figure: the highs rise and the lows fall together, an uptrend by one measure and a downtrend by the other.",
                "Typical price is named and not defined in this chapter. Do not supply a formula.",
            ),
        ),
        Check(
            label="Degrees, reversals and OHLC trends",
            questions=(
                Q(
                    stem="Turning points of larger wave cycles are more significant than those of smaller ones because:",
                    options=("Larger cycles always carry more volume",
                             "Smaller cycles never reverse",
                             "Larger cycles are easier to see",
                             "All the lower degree cycles reverse in sync with it"),
                    answer="D",
                    reason="Wave-degree convergence: when a large wave cycle reverses, all the wave cycles of lower degrees reverse with it.",
                ),
                Q(
                    stem="A correction or pullback, as opposed to a reversal or retracement, tends to imply a move that is:",
                    options=("Shallow, usually no more than a few percent",
                             "Of any amount or degree",
                             "At least half of the prior trend",
                             "Always followed by a new trend"),
                    answer="A",
                    reason="Reversals and retracements may be of any amount. Corrections and pullbacks tend to be shallow, usually no more than a few percent.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.2 - Quality of trend: 16 price characteristics.
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Quality of Trend: 16 Price Characteristics",
    short="5.2 Quality of trend",
    minutes="",
    covers=(),
    slides=(
        Content(
            title="5.2  Sixteen price characteristics",
            lines=(
                "1 Cycle amplitude.  2 Cycle period.  3 Bar retracement symmetry.",
                "4 Average bar range.  5 Price persistence.  6 Bar stochastic ratio.",
                "7 Real body to range ratio.  8 Angular symmetry and momentum.",
                "9 Barrier proximity.  10 Oscillation frequency and depth.",
                "11 Consolidation size and duration.  12 Third gap exhaustion.",
                "13 Average period range.  14 Overextension.  15 Volume spread.  16 Divergence.",
            ),
            caption="Variations in these may impact future price activity. The book calls reading pure price action the highest skill any trader can aspire to.",
            notes=(
                "Do not teach from this slide. It is the map of this part: say that each number gets a slide and a picture of its own.",
                "Price is regarded as the most important indicator of potential future price action. That is why the list is about price.",
                "Review question 4 asks for 12 ways price action may be understood. The section lists 16. Teach the 16.",
            ),
        ),
        Pair(
            left=Term(
                term="1  Cycle amplitude",
                plain="Each swing's height, as the figure marks it.",
                example="Up swings of PHP 6, then 4, then 2: decreasing amplitude.",
                formal="Decreasing cycle amplitude is an early indication of potential underlying weakness in an uptrend, and a bullish indication in a downtrend. In an uptrend the up cycle amplitudes must, on average, be larger than the down ones; the converse in a downtrend. The change in successive amplitudes matters most.",
            ),
            picture=Figure(
                number="5.11",
                shows="A rising wave between two converging dashed lines, each swing smaller than the last, with the up cycle amplitudes and the down cycle amplitudes measured by vertical arrows, labelled gradually decreasing up and down cycle amplitudes.",
            ),
            text_w=6.8,
            notes=(
                "In the figure the long arrows are up cycle amplitudes and the short ones down cycle amplitudes. Both shrink, swing after swing.",
                "The book never defines cycle amplitude in words. The plain line is how Figure 5.11 measures it, and the pesos are ours.",
                "The pattern for all sixteen: a variation in something, and what that variation says about the trend.",
            ),
        ),
        Pair(
            left=Content(
                title="Contracting, even and expanding amplitude",
                lines=(
                    "Contracting formations are bearish in an uptrend and bullish in a downtrend.",
                    "Expanding formations, with both boundary lines pointing upward, are generally bullish in an uptrend.",
                    "Steady, consistent amplitude is bullish in an uptrend and bearish in a downtrend.",
                ),
                accent="The steady trend is generally regarded as the most reliable in extent and duration.",
            ),
            picture=Figure(
                number="5.12",
                shows="Three idealized uptrends side by side: contracting price action between converging lines, labelled bearish; even price action between parallel lines, labelled neutral or bullish; and expanding price action between diverging lines, labelled bullish or volatile.",
            ),
            text_w=5.2,
            notes=(
                "The figure's three labels are bearish, neutral or bullish, and bullish or volatile. The text calls the even one bullish in an uptrend.",
                "For expanding formations in a downtrend the book says only that the converse applies.",
            ),
        ),
        Pair(
            left=Term(
                term="2  Cycle period",
                plain="How long each swing takes, as the figure marks it: across, from one peak to the next.",
                example="An uptrend's peaks come 30 bars apart, then 20, then 12: a decreasing cycle period.",
                formal="Decreasing cycle periods are also an early indication of potential weakness in a trend. A gradual reduction in the cycle period during an uptrend: there may be underlying weakness in the uptrend. During a downtrend: a bullish indication.",
            ),
            picture=Figure(
                number="5.13",
                shows="A rising wave between two converging lines whose peaks come closer and closer together, with the horizontal distance between peaks marked by arrows that shorten, labelled gradually decreasing cycle periods.",
            ),
            text_w=6.6,
            notes=(
                "Same reading as amplitude, with the swings measured sideways: each one takes less time than the one before.",
                "The book defines neither word. The two figures do it by where they put their arrows.",
                "Chapter 4 named the cycle period once, as the business of Chapter 20. This is the first time it is read.",
            ),
        ),
        Pair(
            left=Term(
                term="3  Bar retracement symmetry",
                plain="In a strong trend each retracement takes about the same number of bars. Count them.",
                example="In the figure three retracements take 28, 30 and 26 bars: consistent symmetry. The next takes 14: symmetry broken, and a strong upside move follows.",
                formal="A change in the number of bars in a retracement is an early indication of a potential change in trend behavior.",
            ),
            picture=Figure(
                number="5.14",
                shows="A rising channel in which three retracements of 28, 30 and 26 bars are labelled consistent symmetry indicates strong trend action, then a retracement of only 14 bars circled as symmetry broken, a trend behavior change, before price leaves the channel upward at a point A.",
            ),
            text_w=5.6,
            notes=(
                "Consistent symmetry indicates strong trend action: that is the figure's own label.",
                "The same figure comes back with channels: here price also fails to reach the lower channel line before it breaks out.",
            ),
        ),
        Check(
            label="Amplitude, period and symmetry",
            questions=(
                Q(
                    stem="In an uptrend, the cycle amplitude decreases swing after swing. This is:",
                    options=("A sign that the trend is strengthening",
                             "A bullish indication",
                             "An early indication of potential weakness",
                             "Of no significance"),
                    answer="C",
                    reason="Decreasing cycle amplitude in an uptrend is an early indication of potential underlying weakness. In a downtrend it would be bullish.",
                ),
                Q(
                    stem="Retracements in an uptrend have taken 28, 30 and 26 bars. The next one takes 14. This suggests:",
                    options=("A potential change in trend behavior",
                             "Nothing, because the trend is still up",
                             "An increase in cycle amplitude",
                             "That a downtrend has begun"),
                    answer="A",
                    reason="A change in the number of bars in a retracement is an early indication of a potential change in trend behavior.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="4  Average bar range",
                plain="The average height of the bars, low to high.",
                example="Daily ranges of PHP 3.00, then 2.40, then 1.80 as price climbs: a decreasing average bar range.",
                formal="A decrease in the average bar range is an early indication of potential weakness in an uptrend, and a bullish indication in a downtrend. It can be tracked with the average true range, ATR, oscillator which, unlike average bar range, accounts for gaps between the bars as well.",
            ),
            picture=Figure(
                number="5.15",
                shows="A rising run of candlesticks, each shorter than the one before, labelled gradually decreasing bar range, over a lower panel in which the ATR declines.",
            ),
            text_w=6.8,
            notes=(
                "Same shape of rule as the first two: something shrinking in an uptrend is weakness, in a downtrend it is bullish.",
                "Chapter 3 gave the true range: the greater of the bar's range and the distance from the last close. That is why the ATR sees gaps. How it is averaged is Chapter 8.",
            ),
        ),
        Pair(
            left=Content(
                title="A declining ATR in a steady uptrend",
                lines=(
                    "GLD, the SPDR Gold Trust Shares, weekly: a steady uptrend with a declining ATR.",
                    "Volume is bullish, but the ATR is indicating otherwise.",
                    "A large bearish candlestick completes the bearish picture.",
                ),
                accent="Price declined after the volume climax.",
            ),
            picture=Figure(
                number="5.16",
                shows="The weekly GLD chart in three panels: price in a strong uptrend to a circled pair of candlesticks at the top, volume increasing beneath it, and the ATR declining all the way up before turning.",
            ),
            text_w=7.0,
            notes=(
                "Three panels: price, volume, ATR. Price and volume rise together while the ATR falls the whole way up.",
                "One characteristic disagreed with everything else on the chart, and it was the one that was right.",
            ),
        ),
        Pair(
            left=Content(
                title="5  Price persistence",
                lines=(
                    "Prices tend to persist for longer when price is of high quality.",
                    "High quality prices have relatively small, and approximately equal, bar ranges.",
                    "Price then moves predictably. Trends and reversals are clear and decisive.",
                ),
                accent="In this mode prices exhibit relatively low volatility.",
                caption="Chapter 1's first applied assumption: price behavior persists. Here persistence is the continuity of trend action.",
            ),
            picture=Figure(
                number="5.17",
                shows="An hourly GBPJPY chart with two boxes: higher quality price action with greater persistence, where the swings are long and clean, and lower quality price action with lesser persistence, where they are short and choppy.",
            ),
            text_w=5.2,
            notes=(
                "A recall, not a new term: persistence was Chapter 1's first applied assumption. Here the book says which kind of price persists.",
                "Two tests for high quality price, both about the bars: small ranges, and ranges about equal to each other.",
                "Left box against right box: the same market, a week apart, easy to track and then hard to track.",
            ),
        ),
        Pair(
            left=Term(
                term="Bar stochastic",
                plain="Where a bar closed inside its own range: near the top, the middle or the bottom.",
                example="A bar with a low of PHP 40, a high of PHP 50 and a close of PHP 48: (48 - 40) / (50 - 40) = 0.80. It closed near its high.",
                formal="The relative position of the closing price within the bar itself, measured as a ratio: (C - L) / (H - L). The book calls it essentially a one-period %K, and does not explain %K here.",
            ),
            picture=Chart(
                letter="AG",
                shows="One bar drawn three times with a low of 40 pesos and a high of 50, and only the close moved. Close 48: a bar stochastic of 0.80, near the high of the bar. Close 45: 0.50, the middle of the bar. Close 42: 0.20, near the low of the bar.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The text gives the words and the book's next figure prints the formula. The pesos are ours.",
                "Read the three bars left to right. The bar is the same height each time; only the right tick, the close, moves down it, and the ratio falls from 0.80 to 0.20.",
                "The standard stochastic oscillator compares the close with the last N periods. This one looks inside a single bar. %K is named, not taught.",
            ),
        ),
        Pair(
            left=Content(
                title="6  The average bar stochastic ratio",
                lines=(
                    "In an uptrend, a gradual decline in closes with respect to the bar is an early indication of potential weakness.",
                    "In a downtrend, a gradual increase is an early indication of potential bullishness.",
                ),
                accent="In the figure the bars climb while each close sits lower within its bar.",
            ),
            picture=Figure(
                number="5.18",
                shows="A rising run of bars whose closes sit lower and lower within each bar, labelled declining closing prices with respect to the bar range, with the formula bar stochastic = (C - L) / (H - L) and a lower panel in which the bar stochastic declines.",
            ),
            text_w=6.2,
            notes=(
                "Price keeps rising while the closes sink within their bars. That is the characteristic: the ratio falling in an uptrend.",
                "The lower panel is the ratio itself, bar by bar, sliding down.",
            ),
        ),
        Pair(
            left=Content(
                title="The ratio, averaged, on a real chart",
                lines=(
                    "The ratio is monitored with a simple moving average of it.",
                    "Weekly EURUSD: a 3-period SMA of the bar stochastic, in the panel under the price.",
                    "The figure marks bearish divergences at three tops and bullish divergences at three bottoms.",
                ),
                caption="Divergence: met in Chapter 4, on the MACD. Taught in Chapter 9.",
            ),
            picture=Figure(
                number="5.19",
                shows="A weekly EURUSD chart over a lower panel carrying a 3-period SMA of the bar stochastic, with three tops labelled bearish divergence and three bottoms labelled bullish divergence.",
            ),
            text_w=5.2,
            notes=(
                "Read the figure's labels and stop. Chapter 4 showed one divergence and did not define it. What divergence is, formally, waits for Chapter 9.",
                "A simple moving average is used here and not built. Moving averages are Chapter 11.",
            ),
        ),
        Pair(
            left=Term(
                term="7  Real body to range ratio, BRR",
                plain="How much of a candlestick is real body: the open-to-close move as a share of the whole bar.",
                example="Open PHP 42, close PHP 48, low PHP 40, high PHP 50: (48 - 42) / (50 - 40) = 0.60.",
                formal="BRR = (C - O) / (H - L). A gradual decrease in the real body to candlestick range is an early indication of potential weakness in an uptrend, and a bullish indicator in a downtrend. A simple moving average of the ratio is used to monitor it.",
            ),
            picture=Figure(
                number="5.20",
                shows="A rising run of candlesticks whose real bodies shrink while their ranges do not, labelled declining BRR, with the formula body to range ratio (BRR) = (C - O) / (H - L) and a lower panel in which the BRR declines.",
            ),
            text_w=6.8,
            notes=(
                "The formula is printed on Figure 5.20 and the pesos are ours. The real body was Chapter 3: the boxed space between the open and the close.",
                "Bar stochastic asks where the bar closed. This one asks how much of the bar the open-to-close move covered.",
            ),
        ),
        Check(
            label="Bar range, and where the bar closes",
            questions=(
                Q(
                    stem="A bar has a low of PHP 20, a high of PHP 30 and a close of PHP 22. Its bar stochastic is:",
                    options=("0.20",
                             "0.50",
                             "0.80",
                             "2.00"),
                    answer="A",
                    reason="(C - L) / (H - L) = (22 - 20) / (30 - 20) = 0.20. The bar closed near its low.",
                ),
                Q(
                    stem="Unlike the average bar range, the average true range (ATR) oscillator:",
                    options=("Ignores the closing price",
                             "Accounts for gaps between the bars",
                             "Works only in uptrends",
                             "Measures volume, and not price"),
                    answer="B",
                    reason="The ATR will account for gaps between the bars as well, which a plain average of bar ranges does not.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="8  Angular symmetry and momentum",
                plain="A trend rising at one steady angle.",
                example="3M Co. over three years: consistent angular symmetry. Trendlines 1 and 2 are parallel, a strong prognosticator of potential bullishness.",
                formal="Any change in angular symmetry is an early indication of potential bullishness or bearishness. Generally an increase in the angle of ascent is bullish, and a decrease bearish.",
            ),
            picture=Figure(
                number="5.21",
                shows="A three year chart of 3M Co. with many trendlines, labelled all lines are rising at the same angle and underlying angular symmetry in 3M Co., two of them dotted and numbered 1 and 2, a point 3 above the second, and a box marked bullish indication.",
            ),
            text_w=6.0,
            notes=(
                "Trendline 1 was followed by a steady rise, so the book expects the same after trendline 2, following a minor correction at point 3.",
                "It says 3M went on to rise above $140, which the chart does not show. The caption says hourly; the chart itself is daily.",
                "Chapter 1's Figure 1.25 showed angular symmetries on a chart and did not say how to read them. This is where the book does.",
            ),
        ),
        Pair(
            left=Content(
                title="Acceleration and deceleration",
                lines=(
                    "Upside acceleration in price is bullish. Upside deceleration is bearish.",
                    "Downside acceleration is bearish. Downside deceleration is bullish.",
                    "Upside and downside acceleration is normally parabolic in nature.",
                ),
                accent="An uptrend may not be self-sustaining if its rate of ascent was excessive.",
                caption="Such rises usually end in a blow-off or buying climax. Downside acceleration may end in a selling climax.",
            ),
            picture=Figure(
                number="5.22",
                shows="Four curves. Uptrends: one bending upward, upside acceleration, bullish; one flattening, upside deceleration, bearish. Downtrends: one bending downward, downside acceleration, bearish; one flattening, downside deceleration, bullish.",
            ),
            text_w=5.2,
            notes=(
                "Speeding up is with the trend, slowing down is against it. Four cases, one rule.",
                "After a blow-off or buying climax prices subsequently collapse, the book says. Both climaxes came up in Chapter 4.",
            ),
        ),
        Pair(
            left=Content(
                title="Deceleration with a diminishing bar range",
                lines=(
                    "An even more potentially bearish scenario in an uptrend.",
                    "Two characteristics at once: a deceleration in price, and a diminishing bar range.",
                ),
                accent="The trend flattens out, and each bar covers less ground than the last.",
            ),
            picture=Figure(
                number="5.23",
                shows="A run of candlesticks rising along a curve that flattens out, each candlestick shorter than the last, labelled gradually decreasing bar range and flattening out action.",
            ),
            text_w=7.0,
            notes=(
                "Characteristic 4 and characteristic 8 on one chart. Two warnings agreeing is worth more than either alone.",
                "The book's caption calls it diminishing angular momentum.",
            ),
        ),
        Pair(
            left=Content(
                title="A change in the trend rate",
                lines=(
                    "Gold rises at a consistent trend rate, leg after leg.",
                    "Once the rate changes, the market switches to a new regime: greater volatility and larger swings.",
                    "The new rate of $10.30 a day may be unsustainable over the longer term.",
                ),
                accent="Gold in fact declined rapidly thereafter, not shown on the chart.",
                caption="The text says about $3.30 a day; the figure prints $3.80. The book's caption under 5.24 is Figure 5.25's.",
            ),
            picture=Figure(
                number="5.24",
                shows="A daily Gold chart headed trend rate analysis on Gold: five rising legs each drawn at an uptrend rate of $3.80 a day, labelled previous market behavior, then steeper legs at $10.30 a day, an approximately 270 percent increase, labelled new market behavior, more volatile.",
            ),
            text_w=5.2,
            notes=(
                "The five parallel strokes on the left are the same angle: angular symmetry again, stated as dollars per day.",
                "Two slips in the book on this one figure. Say them once, plainly, and teach the idea: a change of rate is a change of regime.",
            ),
        ),
        Pair(
            left=Term(
                term="9  Barrier proximity",
                plain="How near a trend has come to a strong price barrier. The nearer, the likelier a turn.",
                example="iShares MSCI Emerging Markets rebounds after testing a strong support level, with the cycle-tuned stochastic oversold. This chapter uses that oscillator and never explains it.",
                formal="There is always a high probability that a trend may reverse as it approaches a strong and significant price barrier.",
            ),
            picture=Figure(
                number="5.25",
                shows="A daily chart of iShares MSCI Emerging Markets: a strong downtrend falls to a support barrier drawn from an earlier low and price rebounds, with the cycle-tuned stochastic below circled at oversold.",
            ),
            text_w=5.8,
            notes=(
                "The barrier here is a support level set by an earlier low. A strong downtrend meets it and turns.",
                "Say overbought and oversold as the figure does. The oscillator itself is Chapter 8.",
            ),
        ),
        Check(
            label="Angles, acceleration and barriers",
            questions=(
                Q(
                    stem="Upside deceleration in an uptrend is regarded as:",
                    options=("Bullish",
                             "Bearish",
                             "Neutral",
                             "A buying climax"),
                    answer="B",
                    reason="Upside acceleration is bullish and upside deceleration is bearish. For downtrends the two are reversed.",
                ),
                Q(
                    stem="A strong downtrend approaches a strong and significant support level. The probability of a reversal is:",
                    options=("Low, because the trend is strong",
                             "Unchanged by the level",
                             "Zero until volume rises",
                             "High, because of barrier proximity"),
                    answer="D",
                    reason="There is always a high probability that a trend may reverse as it approaches a strong and significant price barrier.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="10  Frequency and depth of oscillations",
                lines=(
                    "An uptrend is more reliable with a reasonable number of oscillations: fairly frequent, not too shallow or too deep.",
                    "That is indicative of healthy profit taking.",
                    "With little profit taken, more pent-up, unrealized profit is at risk.",
                    "Traders then exit rapidly at the slightest hint of bearishness.",
                ),
                accent="Such a trend is potentially more bearish at higher prices.",
            ),
            picture=Figure(
                number="5.26",
                shows="Two uptrends. On the left a large number of deep price oscillations, with less chance of a severe retracement because more profit is taken along the way. On the right a smaller number of shallow oscillations, with a high probability of a more severe retracement.",
            ),
            text_w=5.4,
            notes=(
                "With some profit taken off the table, traders react less emotionally at higher prices. That is the book's reason.",
                "The grey boxes in the figure say it in full: pent-up profit and emotions create more fear of losing capital and profit.",
            ),
        ),
        Pair(
            left=Content(
                title="Oscillations on the Apple chart",
                lines=(
                    "Apple first oscillates in a steady, rising channel.",
                    "Then price rises rapidly, with the minimum of oscillations and little profit taking.",
                    "Between time lines 1 and 2 the ATR declines as prices rise: a bearish indication.",
                ),
                accent="Apple prices decline substantially thereafter.",
                caption="Profit-taking oscillations also occur at various wave degrees within a trend.",
            ),
            picture=Figure(
                number="5.27",
                shows="A daily Apple chart: a relatively healthy trend with deep oscillations inside a rising channel, then a rapidly rising trend with little price oscillation, an eventual sell-off, and an ATR panel displaying bearish divergence between two dotted time lines.",
            ),
            text_w=5.2,
            notes=(
                "Two of the sixteen on one stock: few oscillations, characteristic 10, and a falling ATR, characteristic 4.",
                "The second rise toward the historical high has a similar rate and as little profit taking as the first.",
            ),
        ),
        Pair(
            left=Content(
                title="11  Size and duration of a consolidation",
                lines=(
                    "A trend interruption, Chapter 4's consolidation, is more significant the greater its magnitude: a taller chart pattern.",
                    "And if it develops over a longer period: a wider chart pattern.",
                    "Larger trend interruptions normally lead to a greater probability of a reversal.",
                ),
                accent="In short, size takes precedence over form.",
                caption="A larger head and shoulders is more bearish in an uptrend; a larger rounding bottom more bullish in a downtrend.",
            ),
            picture=Chart(
                letter="C",
                shows="One uptrend interrupted twice: first by a small consolidation, shorter and narrower, and later by a large one, taller and wider, which is the more significant interruption.",
            ),
            text_w=CHART_W,
            notes=(
                "The longer a consolidation takes to unfold, the greater its disruptive power with respect to the trend, should a reversal occur.",
                "The two boxes on the chart hold the same kind of sideways movement. Only their size differs.",
            ),
        ),
        Pair(
            left=Term(
                term="12  Third gap exhaustion",
                plain="Count the gaps in a trend. Watch the third.",
                example="The SPDR Dow Jones Industrial Average ETF tops after a third gap in its uptrend, and bottoms after another third gap in the downtrend that follows. The cycle-tuned stochastic is overbought at the first and oversold at the second.",
                formal="The appearance of a third gap in a trend is an indication of potential trend exhaustion and a possible reversal.",
            ),
            picture=Figure(
                number="5.28",
                shows="A daily chart of the SPDR Dow Jones Industrial Average ETF: a breakaway, a runaway and an exhaustion gap numbered 1, 2 and 3 on the way up, the same three numbered on the way down, and a cycle-tuned stochastic indicating overextension at both third gaps.",
            ),
            text_w=7.0,
            notes=(
                "The figure names the three gaps breakaway, runaway and exhaustion. Section 5.8 defines them.",
                "Chapter 4 met the same three as Sakata's San Ku, three gaps.",
            ),
        ),
        Check(
            label="Oscillations, size and gaps",
            questions=(
                Q(
                    stem="An uptrend rises rapidly with very few oscillations. Compared with an uptrend that oscillates frequently, it is:",
                    options=("More reliable, because nothing interrupts it",
                             "Certain to continue",
                             "Potentially more bearish at higher prices",
                             "Free of unrealized profit"),
                    answer="C",
                    reason="Little profit taking leaves more pent-up and unrealized profit at risk, so traders exit rapidly at the slightest hint of bearishness.",
                ),
                Q(
                    stem="Two head and shoulders formations appear in strong uptrends. The larger of the two is deemed:",
                    options=("Less bearish than the smaller one",
                             "More bearish than the smaller one",
                             "Bullish",
                             "Equally bearish, because the form is the same"),
                    answer="B",
                    reason="Larger trend interruptions lead to a greater probability of a reversal. Size takes precedence over form.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="13  Average period range",
                plain="The usual distance price travels in one period.",
                example="A FOREX pair's average daily range is 120 pips. Price beyond that, either way, before the trading day completes: a potential sign of exhaustion, and a reversal may be expected.",
                formal="One of the most reliable characteristics of price activity. Found with the ATR, or as the 2 standard deviation value of bar range: ninety percent of ranges stay below it, the book says.",
            ),
            picture=Chart(
                letter="D",
                shows="One trading day of an invented currency pair with its average daily range of 120 pips drawn as a band from the day's low: price reaches the top of the band well before the day ends, which is a potential sign of exhaustion.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The period can be any chosen duration of observation. The book's example is a day.",
                "When looking for the reversal, pay special attention to supportive and resistive confluences.",
                "The book advises a simple backtest to find the most reliable lookback period for either method.",
            ),
        ),
        Pair(
            left=Content(
                title="14  Overextension past an overlay barrier",
                lines=(
                    "A price penetration above an uptrending line is generally regarded as a potential sign of exhaustion, with a reversal expected.",
                    "Similarly for a penetration below a downtrending line.",
                    "Short term penetrations below an uptrending line, or above a downtrending one, are usually regarded as false breakouts.",
                ),
                accent="With the line's slope: exhaustion. Against it: a false breakout.",
                caption="Chapter 2: penetration of a peak or trough. Here: of a line.",
            ),
            picture=Figure(
                number="5.29",
                shows="Four small charts. Top: price spiking above an uptrending line, and price spiking below a downtrending line, each circled as price exhaustion. Bottom: price dipping below an uptrending line, and price poking above a downtrending line, each circled as a false breakout.",
            ),
            text_w=5.6,
            notes=(
                "Top row of the figure is overextension, bottom row is the false breakout. The lines are the same; the side differs.",
                "The book's caption for this figure is simply price exhaustion.",
            ),
        ),
        Pair(
            left=Content(
                title="15  Volume spread action",
                lines=(
                    "Large range, large volume: trend promoting. Bullish if the bar closes at or near its high, very bearish near its low.",
                    "Large range, low volume: trend inhibiting. A lack of commitment.",
                    "Small range, large volume: a stronger sign of a potential reversal. The squat bar.",
                    "Small range, low volume: trend inhibiting.",
                ),
                accent="Price and volume matter most together when both are extreme.",
            ),
            picture=Chart(
                letter="E",
                shows="Four small drawings, each of three bars over their volume, the last bar being the extreme one: a large range on large volume, a large range on low volume, a small range on large volume, which is the squat bar, and a small range on low volume.",
            ),
            text_w=CHART_W,
            notes=(
                "The book says very large and very small, very large and very low, each time. The slide drops the word very to fit.",
                "Only the squat bar is called a significantly stronger indication of reversal: a large commitment of capital and no further extension in price.",
                "The two low volume cases are trend inhibiting, though not necessarily a reversal.",
            ),
        ),
        Content(
            title="16  Volume and oscillator divergence",
            lines=(
                "Standard or reverse divergence may appear between price and volume, or between price and any oscillator.",
                "It may give an early indication of potential reversals or continuations in the market.",
                "Chapter 4 showed one: price made a higher peak while the MACD made a lower one.",
            ),
            accent="The book gives divergence this one sentence here and refers to Chapter 9 for more.",
            caption="That completes the sixteen. The chapter summary advises paying particular attention to all of them.",
            notes=(
                "No picture on this slide: the book explains nothing about divergence here and sends the reader to Chapter 9.",
                "Two of this chapter's figures have already labelled divergences, and Chapter 4 showed one on the MACD. That is as far as the book has taken it.",
            ),
        ),
        Check(
            label="Exhaustion and volume",
            questions=(
                Q(
                    stem="A currency pair has an average daily range of 120 pips. By midday it has already moved 130 pips. This is regarded as:",
                    options=("A breakaway gap",
                             "A potential sign of exhaustion",
                             "Proof that the trend will continue",
                             "A decrease in cycle period"),
                    answer="B",
                    reason="Price activity beyond the average range before the trading day completes is a potential sign of exhaustion, and a reversal may be expected.",
                ),
                Q(
                    stem="A very small bar range on very large volume, the squat bar, is regarded as:",
                    options=("Trend promoting",
                             "A sign of weak commitment only",
                             "Of no significance",
                             "A significantly stronger indication of a potential reversal"),
                    answer="D",
                    reason="A large commitment of capital with no further extension in price implies strong opposition to the existing trend.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.3 - Price and trend filters.
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Price and Trend Filters",
    short="5.3 Filters",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.3  Three categories of filter",
                lines=(
                    "Price-based filters indicate the exact price of entry, but not when.",
                    "Time-based filters indicate the exact time of entry, but not the price.",
                    "Event-based filters indicate neither, until an event has occurred.",
                ),
                accent="The type of filter, and the extent to which it is employed, sets the exact point of entry and exit.",
                caption="Chapter 1: filters validate breakouts. Unfiltered intraday ones are virtually impossible to backtest, an undefined word.",
            ),
            picture=Chart(
                letter="F",
                shows="One breakout above a level, filtered three ways: a price-based filter that enters at a set price beyond the level, a time-based filter that enters after N closed bars, and an event-based filter that enters when a bar closes beyond the level.",
            ),
            text_w=CHART_W,
            notes=(
                "Chapter 1 taught the price, time and algorithmic filters as terms. This section sorts them by what each one pins down: the price, the time, or neither.",
                "Without a filter a profitable performance is unrepeatable, the book says, because it cannot be backtested.",
            ),
        ),
        Pair(
            left=Content(
                title="The filters, one level down",
                lines=(
                    "Price-based. Absolute: a fixed price excursion. Relative: a percentage of the breakout price. Volatility: multiples of average true range or of standard deviation.",
                    "Time-based: a duration of N closed bars.",
                    "Event-based. Algorithmic: a specific sequence of closed bars, or of new highs or lows. Event-based measure: a closing price violation, or a barrier retest after a confirmed breakout.",
                ),
                caption="Chapter 1 and review question 8 call the third family algorithmic. Here algorithmic is one branch of event-based.",
            ),
            picture=Figure(
                number="5.30",
                shows="A price falling through an uptrend line after a failure swing, with a question mark on how far below the line it must go, beside the full list: (A) price-based filters, absolute, relative and volatility measures; (B) time-based filters; (C) event-based filters, algorithmic filters and event-based measures.",
            ),
            text_w=5.6,
            notes=(
                "The figure is the same list beside a trendline penetration: how far through the line must price go before it counts?",
                "Chapter 1's prose called the third family algorithmic and its Figure 1.21 called it event-based. This chapter's list settles it one way and its review question the other.",
            ),
        ),
        Pair(
            left=Content(
                title="Two-stage filtering",
                lines=(
                    "A closing violation triggers entry. But prices may close too far beyond the entry level.",
                    "So an additional price-based filter limits entry to within a specified distance.",
                    "Time and event filters do not specify the exact price of entry, so controlling risk is ineffective, if not impossible.",
                ),
                accent="This is why price-based filters are the preferred mode of filtering.",
                caption="With no control of the maximum risk per trade, a system may meet risk of ruin, which the book does not define.",
            ),
            picture=Chart(
                letter="G",
                shows="Two closes above the same entry level: one inside the specified distance a price-based filter allows, where the entry is taken, and one far beyond it, where the entry is refused.",
            ),
            text_w=CHART_W,
            notes=(
                "This is review question 8: a price-based filter names the price, so the risk on the trade is known before it is taken.",
                "The closing violation is still the trigger. The price filter is only there to limit risk should the violation be overextended.",
            ),
        ),
        Check(
            label="Filters",
            questions=(
                Q(
                    stem="A filter that indicates the exact price of entry, but not when the entry will be initiated, is:",
                    options=("Time-based",
                             "Event-based",
                             "Price-based",
                             "Algorithmic"),
                    answer="C",
                    reason="Price-based filters give the exact price and not the time. Time-based filters give the time and not the price.",
                ),
                Q(
                    stem="A trader enters on a closing violation and adds a price-based filter. The second filter is there to:",
                    options=("Limit entry to within a specified distance",
                             "Delay the entry by N closed bars",
                             "Confirm the trend with volume",
                             "Replace the closing violation"),
                    answer="A",
                    reason="Prices may close too far beyond the entry level. The price-based filter limits entry to within a specified distance.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.4 - Trend participation.
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Trend Participation",
    short="5.4 Participation",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.4  Four ways into and out of the market",
                lines=(
                    "To go long: buying to open a new position.",
                    "To go short: selling to open a new position.",
                    "To liquidate: selling to close an old long position.",
                    "To cover: buying to close an old short position.",
                ),
                accent="In the figure: long from $50 to $70 is $20. Short from $70 to $40 is $30.",
                caption="Chapter 1's four terms, unchanged. New: in cash, holding no open positions; to square a position, to exit it.",
            ),
            picture=Figure(
                number="5.31",
                shows="One price swing with the four orders marked on it: go long, buy to open at a low price of $50; liquidate, sell to close at a higher price of $70; go short, sell to open at a high price of $70; cover, buy to close at a lower price of $40. A box works out the long profit as $20 and the short profit as $30.",
            ),
            text_w=5.6,
            notes=(
                "Two words open a position and two close one. Liquidate belongs to a long, cover belongs to a short.",
                "Work the box in the figure aloud: 70 less 50, then 70 less 40. The short made more because it sold high and bought back lower.",
            ),
        ),
        Pair(
            left=Content(
                title="Buying low and selling high, four ways",
                lines=(
                    "Buying low and selling high.",
                    "Buying high and selling higher.",
                    "Selling high and buying back lower.",
                    "Selling low and buying back even lower.",
                ),
                accent="Two are longs and two are shorts. All four follow Chapter 1's one principle.",
                caption="Hedging: equal and opposite positions, to reduce or neutralize all directional risk. Buying at the current price is buying at the market.",
            ),
            picture=Chart(
                letter="H",
                shows="One rise and one fall with four trades marked: a long bought low and sold high, a long bought high and sold higher, a short sold high and bought back lower, and a short sold low and bought back even lower.",
            ),
            text_w=CHART_W,
            notes=(
                "The book lists these four as what the principle of buying low and selling high involves.",
                "Follow the numbers on the chart: trades 1 and 2 ride the rise, trades 3 and 4 ride the fall.",
            ),
        ),
        Pair(
            left=Content(
                title="Stop orders: execution, but not the price",
                lines=(
                    "Instructions to enter or exit a market immediately, at any price.",
                    "Once triggered, a stop order turns into a market order.",
                    "A buystop or sellstop entry is placed when a continuation in price is expected.",
                    "The stop exit is the stoploss.",
                ),
                accent="It can guarantee execution, but not the fill price.",
                caption="Chapter 1 taught stop and limit entry orders. New: the exits.",
            ),
            picture=Chart(
                letter="I",
                shows="The current market price with two pending stop entry orders: a buystop above the market, triggered if price rises to it, and a sellstop below the market, triggered if price falls to it. Both are placed when a continuation in price is expected.",
            ),
            text_w=CHART_W,
            notes=(
                "A recall, not a new term: Chapter 1 taught limit and stop entry orders. New today: the exits, and what each order can guarantee.",
                "The book's sentence reads 'cannot guarantee that an order will be executed, or filled at the specified price, but it can guarantee execution'. Its later sentences settle it: execution yes, price no.",
                "Stop orders may wait as pending, or working, orders. For entry: a buystop or a sellstop. To exit a position that moves adversely: a stoploss.",
            ),
        ),
        Pair(
            left=Term(
                term="Slippage",
                plain="You asked for one price and were filled at another. The difference is slippage.",
                example="A stoploss waits at PHP 48. Price gaps down and the order is filled at PHP 46.50: negative slippage of PHP 1.50 a share.",
                formal="The difference between the specified order price and the actual filled price. Stoploss orders may experience additional loss under gapping price action, due to negative slippage.",
            ),
            picture=Chart(
                letter="J",
                shows="A long position with a stoploss at PHP 48: price gaps down through the level and the order is filled at PHP 46.50, a negative slippage of PHP 1.50.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "A stop becomes a market order, and the market had no price between 48 and 46.50 to give.",
                "Slippage can be positive too. The next slide is the order that only ever gets the positive kind.",
                "Chapters 1 and 3 used the word slippage without saying what it is. This is its definition.",
            ),
        ),
        Pair(
            left=Content(
                title="Limit orders: the price, but not execution",
                lines=(
                    "Instructions to enter or exit a market at a specified price, or better.",
                    "If the broker cannot fill it at that price or better, it is not executed.",
                    "A buy limit or sell limit entry is placed when a reversal in price is expected.",
                    "Placed only as a pending order. Only positive slippage is possible.",
                ),
                accent="It can guarantee the intended price or better, but not execution.",
            ),
            picture=Chart(
                letter="K",
                shows="The current market price with two pending limit entry orders: a sell limit above the market and a buy limit below it. Both are placed when a reversal in price is expected at that level.",
            ),
            text_w=CHART_W,
            notes=(
                "Also a recall from Chapter 1, and the mirror of the stop order: the price is guaranteed and the execution is not.",
                "A share trades at PHP 50 and a buy limit waits at PHP 47. If it cannot be filled at 47 or better, nothing happens.",
                "Limit orders can only be placed as pending, or working, orders, never instantaneously. Only positive slippage is possible with them.",
            ),
        ),
        Check(
            label="Stop orders, limit orders and slippage",
            questions=(
                Q(
                    stem="Which order can guarantee execution, but not the price at which it is filled?",
                    options=("A limit order",
                             "A sell limit order",
                             "A stop order",
                             "A buy limit order"),
                    answer="C",
                    reason="Once triggered a stop order turns into a market order: it is executed, at whatever price the market gives.",
                ),
                Q(
                    stem="A stoploss is placed at PHP 30. Price gaps, and the order is filled at PHP 28.80. The slippage is:",
                    options=("PHP 1.20, positive",
                             "PHP 1.20, negative",
                             "PHP 28.80",
                             "Zero, because the order was filled"),
                    answer="B",
                    reason="Slippage is the difference between the specified order price and the actual filled price: 30.00 - 28.80 = 1.20, against the trader.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Exits, and orders at the market",
                lines=(
                    "Taking profit is a limit order: a sell limit above the market, a buy limit below it.",
                    "Cutting a loss is a stop order, the stoploss: a buystop above the market, a sellstop below.",
                    "A limit exit is not guaranteed. A stop exit is, but its exact price is unknown.",
                    "At the current price: a market order. Instantaneous, with no guarantee of the quoted price.",
                ),
                caption="The book says 'or better, that is, higher' of every limit order, the buy limits included.",
            ),
            picture=Chart(
                letter="L",
                shows="The current market price with the four exit orders around it. Above: a sell limit to take profit on a long, and a buystop to cut the loss on a short. Below: a sellstop to cut the loss on a long, and a buy limit to take profit on a short.",
            ),
            text_w=CHART_W,
            notes=(
                "Profit is taken with a limit and a loss is cut with a stop, on either side of the market.",
                "The limit exit is the profit-take, or take profit, order. Under gapping price action it can exit with greater profit.",
                "Negative slippage may sometimes occur when placing market orders.",
            ),
        ),
        Figure(
            title="Every order, above, below and at the market",
            number="5.32",
            shows="A table around the current market price. Orders allowable above the market: buy stop or limit entry, sell limit entry, MIT sell, buy stop to exit a loss, sell limit to exit with profit. Orders allowable under the market: sell stop or limit entry, buy limit entry, MIT buy, sell stop to exit a loss, buy limit to exit with profit.",
            notes=(
                "The book's summary of the section. Read the top row, then the bottom row as its mirror.",
                "Entries above the market: a buystop if prices are expected to rise higher, a sell limit if they are expected to reverse there.",
                "Entries below: a sellstop if prices are expected to continue to decline, a buy limit if they are expected to reverse.",
            ),
        ),
        Content(
            title="Other orders the book names",
            lines=(
                "Market if Touched, MIT: an MIT sell to short above the market, an MIT buy to long below it.",
                "Day orders keep an order pending only until the end of the trading day.",
                "Good till Cancelled orders keep an order active until further notice.",
                "Market on Close orders are executed in the last minutes of the trading day, at or near the close.",
                "Contingent orders are executed once another order is filled or triggered: OCO and OTO.",
            ),
            caption="OCO is one cancel other. OTO is one trigger other.",
            notes=(
                "No picture: these are instructions about time and conditions, and the book gives each one line.",
                "MIT sits in Figure 5.32 as a profit exit, or an entry at any price. The book describes it as shorting above the market using a stop order.",
            ),
        ),
        Check(
            label="Placing orders",
            questions=(
                Q(
                    stem="A trader is long and wants to take profit if price rises to a level above the market. The order to place is:",
                    options=("A buystop",
                             "A sellstop",
                             "A buy limit",
                             "A sell limit"),
                    answer="D",
                    reason="Profit taking above the market is a sell limit, normally referred to as a profit-take order.",
                ),
                Q(
                    stem="An order that stays pending only until the end of the trading day is a:",
                    options=("Day order",
                             "Good till Cancelled order",
                             "Market on Close order",
                             "Contingent order"),
                    answer="A",
                    reason="Day orders instruct the broker to keep an order pending only until the end of the trading day.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.5 - Price inflection points.
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="Price Inflection Points",
    short="5.5 Inflection points",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.5  Ways of initiating an entry",
                lines=(
                    "Overlay breakout entries: on an upside or downside breakout of a price overlay.",
                    "Overlay barrier entries: buying at a barrier support, shorting at a barrier resistance, or at a retest of a barrier.",
                    "Failed breakout entries: in the opposite direction, after a failed breakout.",
                    "Random entries, and pattern or sequence-based entries.",
                ),
                caption="Overlays include channels, trendlines, pivot points and price envelopes. Four ways are announced and five listed; each may be with or against the predominant trend.",
            ),
            picture=Chart(
                letter="M",
                shows="One barrier and three entries on it: a barrier entry, shorting where price turns down at the resistance; a breakout entry, buying as price breaks above it; and a failed breakout entry, shorting once the breakout fails and price falls back below.",
            ),
            text_w=CHART_W,
            notes=(
                "The chart shows the first three. A random entry and a pattern entry have nothing to mark on one line.",
                "Pattern or sequence-based entries follow a particular sequence of bars, or a completed pattern. The book's examples are DeMark Sequential and Japanese candlestick entries.",
            ),
        ),
        Pair(
            left=Content(
                title="Three variations of a top and a bottom",
                lines=(
                    "Failure swing: the second peak fails to penetrate the previous peak.",
                    "Double top: the second peak matches the level of the previous peak.",
                    "Non-failure swing: the second peak succeeds in penetrating the previous peak.",
                    "Bottoms are the mirror: a failure swing, a double bottom and a non-failure swing, read on the second trough.",
                ),
                caption="All three were Chapter 2 terms, unchanged. More complex: a head and shoulders, a broadening formation, an island, a diamond, a rounding top or bottom.",
            ),
            picture=Figure(
                number="5.33",
                shows="Two rows of three drawings. Three basic variations of a top reversal: failure swing, double top and non-failure swing, each with its second peak and its sell signal marked. Three basic variations of a bottom reversal: the same three on the second trough, each with its buy signal.",
            ),
            text_w=7.0,
            notes=(
                "A recall: all three were Chapter 2 terms in this course, under Dow Theory. The book's own sentence here says Chapter 4.",
                "In each drawing the signal is marked where price breaks the level between the two peaks, or the two troughs.",
            ),
        ),
        Pair(
            left=Term(
                term="Inflection point of strength N",
                plain="An inflection point, a peak or trough, counts for more the more bars flank it.",
                example="A peak with ten bars on either side of its highest bar is of strength 10. One with only two is of strength 2.",
                formal="N bars on either side of the highest peak or lowest trough is an inflection point of strength N. The more bars, the more significant the peak and the stronger its resistance level.",
            ),
            picture=Chart(
                letter="N",
                shows="Two peaks on one line: a small one flanked by two bars on either side, an inflection point of strength 2, and a large one flanked by ten bars on either side, an inflection point of strength 10, whose resistance level is the stronger barrier.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book's other name for an inflection point is a swing point. Peaks give resistance levels and troughs give support levels.",
                "Fewer flanking bars: the level is considered less significant and less reliable.",
                "Chapters 2 and 3 used the words inflection point in passing. Its strength, and the definition, are new today.",
            ),
        ),
        Pair(
            left=Term(
                term="Support and resistance role reversal",
                plain="A breached barrier changes sides.",
                example="A share holds at PHP 40, then falls through it. On the next rally PHP 40 stops it.",
                formal="Price barriers change roles once breached: support turns into future resistance, and resistance turns into future support. This applies to all overlay barriers, which include channels, trendlines, pivot points and price envelopes.",
            ),
            picture=Figure(
                number="5.34",
                shows="Four drawings in two columns, resistance turning into support and support turning into resistance: the top pair on horizontal levels, the bottom pair on a downtrend line and an uptrend line.",
            ),
            text_w=5.4,
            notes=(
                "Top row of the figure: horizontal levels. Bottom row: the same thing on sloping trendlines.",
                "Follow one drawing through: price is stopped by the line, breaks it, comes back, and is held from the other side.",
            ),
        ),
        Pair(
            left=Content(
                title="Role reversal in a trend",
                lines=(
                    "In a downtrend, support turns into resistance, level after level.",
                    "In an uptrend, resistance turns into support, level after level.",
                ),
                accent="Each horizontal line in the figure is one level, met first from one side and then from the other.",
            ),
            picture=Figure(
                number="5.35",
                shows="A price chart falling and then rising, with short horizontal lines at the levels where support turned into resistance in the downtrend and where resistance turned into support in the uptrend.",
            ),
            text_w=4.8,
            notes=(
                "The book gives this figure no sentence of its own. Its two labels are the two lines on the slide.",
                "Count the levels on the way down, then on the way up. Every one was used twice.",
            ),
        ),
        Pair(
            left=Content(
                title="Prior peaks, prior troughs and a channel",
                lines=(
                    "EURUSD, 30 minutes: price finds support and resistance at prior peaks and troughs.",
                    "It finds them on the rising channel as well.",
                    "The cycle-tuned stochastic adds confirmation: overbought at resistance, oversold at support.",
                ),
                accent="Resistance turning into support, again and again, in an uptrend.",
            ),
            picture=Figure(
                number="5.36",
                shows="A 30 minute EURUSD chart headed resistance turning into support in an uptrend: horizontal levels each marked resistance and then support, a rising channel around them, and a cycle-tuned stochastic below with arrows from its lows up to the support levels.",
            ),
            text_w=4.8,
            notes=(
                "Horizontal levels and the channel's sloping lines are both barriers, and both change roles.",
                "The vertical arrows join each oversold reading to the support it confirmed.",
            ),
        ),
        Check(
            label="Entries, swing points and role reversal",
            questions=(
                Q(
                    stem="At a market top, the second peak fails to penetrate the previous peak. This variation is called a:",
                    options=("Double top",
                             "Failure swing",
                             "Non-failure swing",
                             "Rounding top"),
                    answer="B",
                    reason="A failure swing fails to penetrate. A double top matches the previous peak, and a non-failure swing succeeds in penetrating it.",
                ),
                Q(
                    stem="A support level is breached. In technical analysis it is now expected to act as:",
                    options=("Stronger support",
                             "A runaway gap",
                             "Future resistance",
                             "Nothing: a breached level is discarded"),
                    answer="C",
                    reason="Price barriers change roles once breached: support turns into future resistance, and resistance into future support.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Trade in the direction of the trend",
                lines=(
                    "It means to buy in an uptrend and short in a downtrend. It is generally easier and safer.",
                    "Buying dips and selling rallies gets positions at the most advantageous prices, with the smallest stopsizes: the stop sits close to the entry.",
                    "Positions taken with the trend can be held, and so extract greater profit from the markets.",
                ),
                accent="Buying a dip and selling a rally are retracement entries in the direction of the existing trend.",
                caption="Simple up and down trendlines or channels time the entries. A cycle-tuned oscillator helps fine-tune them.",
            ),
            picture=Figure(
                number="5.37",
                shows="Two drawings: buying dips in an uptrend, with arrows at each trough along a rising dotted trendline, and selling into rallies in a downtrend, with arrows at each peak along a falling one.",
            ),
            text_w=7.0,
            notes=(
                "The book gives two of its reasons. Both are about where the entry sits: near the trendline, so the stop is small.",
                "In the figure every entry is at the trendline. That is a barrier entry from the first slide of this part.",
            ),
        ),
        Pair(
            left=Term(
                term="Trend filter",
                plain="Says whether a trend is on. Not 5.3's filters.",
                example="A double moving average crossover. Shorter above longer: a potential uptrend starts. Shorter below longer: a potential downtrend.",
                formal="It helps to identify a trend amidst the market noise and price volatility. Two more: a longer-term oscillator crossing its signal line, and price contained above or below an overlay barrier, such as a moving average or trendline.",
            ),
            picture=Chart(
                letter="O",
                shows="A price line with a shorter and a longer moving average: the shorter crosses above the longer, signifying the start of a potential uptrend, and later crosses back below it, signifying the start of a potential downtrend.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "For the oscillator filter: crossing above its signal line signifies potential longer-term bullishness, crossing below potential bearishness.",
                "For containment: price staying above the moving average or trendline signifies an uptrend still intact. That was section 5.1.",
                "Three popular filters, which the book says is by no means exhaustive. Moving averages are Chapter 11: the chart draws two and explains neither.",
            ),
        ),
        Pair(
            left=Content(
                title="A filter and a trigger together",
                lines=(
                    "The MACD is the trend filter. The stochastic crossing its signal line times the entries.",
                    "Long entries: the stochastic crosses above its signal line with the MACD above zero. Short: the reverse.",
                    "Stops: just below the previous trough for a long, just above the previous peak for a short, trailing price.",
                ),
                accent="Divergence in the MACD helps to warn of a potential reversal.",
                caption="MACD (Chapter 4) and the stochastic are not taught here.",
            ),
            picture=Figure(
                number="5.38",
                shows="A EURUSD chart with long entries, short entries and trailing stops marked on price, a stochastic panel with the entry crossovers circled, and a MACD panel with three divergences drawn on it.",
            ),
            text_w=5.4,
            notes=(
                "Trailing: the stop advances to the next higher trough in an uptrend, and to the next lower peak in a downtrend.",
                "Read the figure top down: where the trades were, what triggered them, what filtered them.",
            ),
        ),
        Check(
            label="With the trend",
            questions=(
                Q(
                    stem="Buying on a dip in an uptrend is an example of:",
                    options=("A failed breakout entry",
                             "A random entry",
                             "A breakout entry against the trend",
                             "A retracement entry in the direction of the existing trend"),
                    answer="D",
                    reason="Buying on a dip and selling into a rally are retracement entries taken in the direction of the existing trend.",
                ),
                Q(
                    stem="In a double moving average crossover, the start of a potential uptrend is signified by:",
                    options=("The shorter average crossing above the longer",
                             "The longer average crossing above the shorter",
                             "Price touching either average",
                             "Both averages turning flat"),
                    answer="A",
                    reason="The shorter crossing above the longer signifies the start of a potential uptrend. Crossing below it, a potential downtrend.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Where the stop goes, and how big it is",
                lines=(
                    "A stop is usually placed just below significant troughs for longs, and just above significant peaks for shorts.",
                    "Too far from one: a multiple of ATR or standard deviations from the entry.",
                    "Barrier entries: stopsizes are always approximately the same, just behind the barrier.",
                    "Breakout entries: stopsizes vary with each entry.",
                ),
                caption="Stopsize: the distance from entry to stop, the figure's brackets. The book never defines the word.",
            ),
            picture=Figure(
                number="5.39",
                shows="Two columns. Breakout entries: go long at a breakout with the stoploss just below the trough, where the stopsize will vary with each entry. Barrier entries: go long at support with the stoploss just below the barrier, where the stopsize need not vary with each entry. Each is shown on a level and on a trendline.",
            ),
            text_w=5.6,
            notes=(
                "The brackets in the figure are the stopsizes: wide and changing on the left, narrow and steady on the right.",
                "For a barrier entry the significant peak or trough is usually the point of entry itself. That is why its stop is always close.",
            ),
        ),
        Pair(
            left=Content(
                title="The trouble with a varying stopsize",
                lines=(
                    "A significant problem for traders risking a fixed percentage or fixed unit size per trade.",
                    "The tradesize varies with the stopsize, which affects the system's performance.",
                    "Worst if narrow stops, on a fixed percentage of current capital, are taken out frequently.",
                    "Or wide stops, on a fixed percentage of original capital.",
                ),
                accent="Either way the result is significant loss.",
            ),
            picture=Chart(
                letter="P",
                shows="Tradesize against stopsize for a fixed risk of PHP 10,000 a trade: 2,000 shares at a stopsize of PHP 5.00, 5,000 shares at PHP 2.00, and 20,000 shares at PHP 0.50. The narrower the stop, the larger the tradesize.",
            ),
            text_w=CHART_W,
            notes=(
                "The chart is one line of arithmetic: tradesize is the risk per trade divided by the stopsize.",
                "A narrow stop is hit more often, and with a fixed risk it is hit at full size every time.",
            ),
        ),
        Pair(
            left=Term(
                term="Proportional stopsizing",
                plain="One tradesize for every stop up to a threshold. A smaller one for any wider stop.",
                example="Threshold PHP 3.00, risk limit PHP 10,000. Stops up to PHP 3.00 trade 3,333 shares. A PHP 5.00 stop trades 10,000 / 5 = 2,000.",
                formal="It limits the losses in either scenario by allocating a fixed percentage of original capital to narrow stops, and of current capital for stopsizes that exceed a fixed threshold size.",
            ),
            picture=Chart(
                letter="Q",
                shows="Tradesize against stopsize under proportional stopsizing, for PHP 10,000 at risk: for every stopsize up to the proportional stopsize of PHP 3.00 the tradesize is held at 3,333 shares, and above PHP 3.00 it falls as PHP 10,000 divided by the stopsize.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "This is review question 7. The advantage: losses are limited whether the stops that get hit are the narrow ones or the wide ones.",
                "The author says he first introduced it in The Wiley Trading Guide Volume II. Tradesizing gets Chapter 28.",
            ),
        ),
        Pair(
            left=Content(
                title="Five steps to the proportional tradesize",
                lines=(
                    "1  Backtest 300 to 500 trades for the average stopsize. Say PHP 2.00.",
                    "2  Calculate the two standard deviation value of those stopsizes. Say PHP 1.00.",
                    "3  Add them: 2.00 + 1.00 = PHP 3.00, the proportional stopsize.",
                    "4  Set the maximum risk per trade: 1 percent of PHP 1,000,000 is PHP 10,000.",
                    "5  Divide: 10,000 / 3.00 = 3,333 shares, the proportional tradesize.",
                ),
                caption="Wider stop than PHP 3.00: divide PHP 10,000 by the stopsize.",
            ),
            picture=Chart(
                letter="R",
                shows="The percentage of capital at risk against stopsize under proportional stopsizing: it rises in proportion to the stopsize, 0.5 percent at PHP 1.50, to the maximum of 1 percent at the proportional stopsize of PHP 3.00, and stays capped at 1 percent for every wider stop.",
            ),
            text_w=CHART_W,
            notes=(
                "This is the chapter objective on calculating the optimum tradesize for breakout trades. The pesos are ours; the five steps are the book's.",
                "Why proportional: for stops at or below the threshold the percentage risk varies proportionally with the stopsize, and is always capped at the maximum.",
                "Step 4 is a percentage of current capital. The book says 300 to 500 trades if possible.",
            ),
        ),
        Check(
            label="Stops and tradesize",
            questions=(
                Q(
                    stem="A backtest gives an average stopsize of PHP 4.00 and a two standard deviation value of PHP 2.00. The risk per trade is PHP 12,000. The proportional tradesize is:",
                    options=("1,000 shares",
                             "2,000 shares",
                             "3,000 shares",
                             "6,000 shares"),
                    answer="B",
                    reason="The proportional stopsize is 4.00 + 2.00 = PHP 6.00, and 12,000 / 6.00 = 2,000 shares.",
                ),
                Q(
                    stem="Compared with breakout entries, the stopsizes of barrier entries are:",
                    options=("Always wider",
                             "Different with every entry",
                             "Always approximately the same size",
                             "Not needed at all"),
                    answer="C",
                    reason="At a barrier the significant peak or trough is usually the point of entry itself, so the stop sits just behind the barrier every time.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.6 - Trendlines, channels and fan lines.
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Trendlines, Channels, and Fan Lines",
    short="5.6 Trendlines",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Term(
                term="5.6  Trendline",
                plain="A straight line through two turning points, carried forward. It must not cut through price.",
                example="Join an uptrend's troughs at PHP 40 and PHP 44 and extend the line. A third touch confirms it.",
                formal="A line projected forward into the future from two significant inflection points: troughs for an uptrend, peaks for a downtrend. It is tentative until tested at the third point of price contact, then confirmed, or valid.",
            ),
            picture=Chart(
                letter="S",
                shows="An uptrend line drawn through two significant troughs and projected forward into the future: tentative from the second trough, and confirmed where price tests it at a third point of contact.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "The book's rule is that lines must not cut through any price action at any point along the line. Its other word for tentative is provisionary.",
                "Tentative and valid apply only to conventional trendlines, and not to fan lines, which come at the end of this part.",
                "Chapter 1 drew trendlines on its figures and never said how one is made. This is where the book does.",
            ),
        ),
        Pair(
            left=Content(
                title="Short, medium and longer-term trendlines",
                lines=(
                    "A trendline is short, medium or longer term depending on the amount of price activity it contains above or below it.",
                    "Longer-term uptrend lines contain more price activity above them than shorter-term uptrend lines.",
                    "The converse is true for downtrend lines.",
                ),
                accent="A longer-term trendline contains, or supports, more of the price action.",
                caption="Point and Figure's bullish support and bearish resistance lines are drawn from one reference point, not two.",
            ),
            picture=Figure(
                number="5.40",
                shows="One rising price with three dotted uptrend lines fanning out from the same low: a steep short-term line, a medium-term line, and a shallow longer-term line that contains or supports more of the price action.",
            ),
            text_w=5.2,
            notes=(
                "All three lines start at the same trough. The term is set by how much price sits above the line, not by the calendar.",
                "The Point and Figure lines are the one exception to two inflection points that the book names. Chapter 15 is Point and Figure.",
            ),
        ),
        Pair(
            left=Content(
                title="Why a trendline holds: behavior",
                lines=(
                    "All price overlays, trendlines included, are barriers to price action.",
                    "Most participants place buy orders above a barrier and short orders below it.",
                    "From above, price triggers the buy orders: an upside reaction, temporary support.",
                    "From below, it triggers the sell orders: a downside reaction, temporary resistance.",
                ),
                accent="Support and resistance are behavioral: human psychology, biases and emotions.",
            ),
            picture=Chart(
                letter="T",
                shows="One rising trendline met from both sides: price approaching from above triggers the buy orders resting above it and bounces, temporary support; later price approaching from below triggers the sell orders resting below it and turns down, temporary resistance.",
            ),
            text_w=CHART_W,
            notes=(
                "The book's words: support and resistance are regarded as behavioral consequences of human psychology, biases and emotions.",
                "This is the same role reversal as section 5.5, explained: one line, support from above and resistance from below.",
            ),
        ),
        Pair(
            left=Term(
                term="Internal line",
                plain="A breached trendline, kept under a new name.",
                example="A head and shoulders neckline is breached, and price very frequently comes back to retest it.",
                formal="A trendline is invalidated once it is breached, and is thereafter referred to as an internal line. The new uptrend line is drawn between the original lower trough and the new significant trough; for downtrends, between the original higher peak and the new significant peak.",
            ),
            picture=Figure(
                number="5.41",
                shows="A 30 minute EURUSD chart following one uptrend line: drawn from two troughs at points 1 and 2, confirmed or validated at its first retest, the third point on the line, then invalidated, and a new uptrend line redrawn between points 1 and 3.",
            ),
            text_w=6.0,
            notes=(
                "The figure runs the whole life of a line: drawn, confirmed at the circle, invalidated, redrawn.",
                "Invalidated does not mean ineffective. Price often comes back to an old line, as it does to a neckline.",
            ),
        ),
        Pair(
            left=Content(
                title="What counts as a valid penetration?",
                lines=(
                    "It depends on the filtering employed.",
                    "Closing filter rule: a penetration is valid only once price closes beyond the line.",
                    "A very significant intraday penetration that closes back above an uptrend line: significant, but invalid.",
                    "The book's answer: price-based filters only, or double-stage filtering with a price-based second filter.",
                ),
                caption="Either way a new trendline may still be drawn. The trader monitors price reactions at both lines.",
            ),
            picture=Chart(
                letter="U",
                shows="An uptrend line with one bar whose intraday low goes well through the line while its close comes back above it: significant, but invalid under the closing filter rule. A dashed line below marks the price a price-based filter would require.",
            ),
            text_w=CHART_W,
            notes=(
                "The answer depends on the type and extent of filtering. The book: we yet again observe the problems with defining price action.",
                "A price-based filter lets the trader decide exactly how much price excursion represents a valid penetration.",
            ),
        ),
        Check(
            label="Drawing and breaking a trendline",
            questions=(
                Q(
                    stem="A trendline drawn from two troughs becomes a confirmed, or valid, trendline when:",
                    options=("It is first drawn",
                             "Price breaches it",
                             "Price tests it at a third point of contact",
                             "Volume rises along it"),
                    answer="C",
                    reason="A trendline is only provisionary, or tentative, until it is tested for the first time, at the third point of price contact.",
                ),
                Q(
                    stem="Once a trendline has been invalidated, it is thereafter referred to as:",
                    options=("A tentative line",
                             "A valid line",
                             "A neckline",
                             "An internal line"),
                    answer="D",
                    reason="A breached trendline is invalidated, but not unusable. It is thereafter referred to as an internal line.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="A reliable trendline: angle and duration",
                lines=(
                    "A reliable trendline gives consistent support and resistance. A lot of whipsaws: unreliable.",
                    "Angle: above 45 degrees a steep uptrend is less stable. So is a very shallow one.",
                    "The most reliable uptrend line rises at approximately 35 to 45 degrees.",
                    "Duration: longer-term trendlines are generally more reliable than shorter-term ones.",
                ),
                caption="A longer-term line is more obvious to all participants and attracts more and larger orders, institutions included. Whipsaw: still undefined, as in Chapter 4.",
            ),
            picture=Chart(
                letter="V",
                shows="Three small drawings of an uptrend line under its price: one steeper than 45 degrees, less stable; one at about 35 to 45 degrees, the most reliable; and one with a very shallow angle of ascent, also less stable.",
            ),
            text_w=CHART_W,
            notes=(
                "This and the next slide are review question 6: the factors that impact trendline reliability. Six of them, two here.",
                "The steep trend may not be able to sustain itself over the longer term. Chapter 4 said the book uses whipsaw without defining it, and it still does.",
            ),
        ),
        Pair(
            left=Content(
                title="A reliable trendline: the other four",
                lines=(
                    "Number of retests: the more a line is retested, the more orders it attracts.",
                    "Clarity of the retests: the more precise, the more formidable the barrier.",
                    "Confluence with other indicators at the point of contact: a stronger rejection of price.",
                    "Preceding action: contracting cycle amplitude, cycle period, bar range or body-to-range ratio makes a line suspect.",
                ),
                caption="Retests show that traders are aware of the line and paying attention to it.",
            ),
            picture=Chart(
                letter="W",
                shows="An uptrend line retested four times, each retest precise: price comes down to the line, touches it, and is rejected.",
            ),
            text_w=CHART_W,
            notes=(
                "The first three share one mechanism: the more visible the line, the more orders gather around it, as on the behavior slide.",
                "The fourth is section 5.2 again: a line under a weakening trend is unreliable over the longer term.",
            ),
        ),
        Pair(
            left=Content(
                title="A trendline's minimum price target",
                lines=(
                    "Find the distance that price moved farthest from the trendline.",
                    "Apply a one-to-one projection of that distance from the breakout point.",
                    "Farthest distance PHP 6, breakout at PHP 50: the minimum target is 50 - 6 = PHP 44.",
                ),
                accent="In the figure prices bottom very close to the minimum projected target.",
                caption="Chapter 4's minimum measuring objective, from a trendline.",
            ),
            picture=Figure(
                number="5.42",
                shows="A 30 minute EURUSD chart: the maximum distance of price from the uptrend line measured as a vertical arrow, the same height projected one to one down from the breakout point, and profit-taking activity around the minimum target projection.",
            ),
            text_w=5.0,
            notes=(
                "The same idea as Chapter 4's minimum measuring objective, measured from a trendline and not from a range.",
                "The pesos are ours. The figure shows the method on EURUSD: one arrow up, the same arrow down.",
            ),
        ),
        Content(
            title="Strengths and weaknesses of trendline analysis",
            lines=(
                "Strength: straight lines catch any trend change effectively, with no need to identify price patterns.",
                "Strength: simple to construct, and applied and viewable across all timeframes and markets.",
                "Weakness: subject to whipsaws, like moving averages, and less effective in erratic, volatile or ranging markets.",
                "Weakness: affected by the type of scaling used, Chapter 3's ratio or linear.",
                "Weakness: a consolidation may breach a line without a legitimate reversal.",
            ),
            notes=(
                "No picture: this is the book's own list of four strengths and three weaknesses, on five lines.",
                "The scaling weakness is Chapter 3: a straight line on a linear scale is not straight on a ratio scale.",
            ),
        ),
        Check(
            label="Reliability and targets",
            questions=(
                Q(
                    stem="The most reliable uptrend line has an angle of ascent of approximately:",
                    options=("10 to 20 degrees",
                             "35 to 45 degrees",
                             "50 to 60 degrees",
                             "75 to 90 degrees"),
                    answer="B",
                    reason="Above 45 degrees a trend is less stable, and so is a very shallow one. Approximately 35 to 45 degrees is the most reliable.",
                ),
                Q(
                    stem="Price moved at most PHP 8 away from an uptrend line, then broke below the line at PHP 60. The minimum price target is:",
                    options=("PHP 44",
                             "PHP 52",
                             "PHP 60",
                             "PHP 68"),
                    answer="B",
                    reason="A one-to-one projection of the farthest distance from the breakout point: 60 - 8 = PHP 52.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="Continuation and reversal trendlines",
                plain="Named by the breakout a trendline allows.",
                example="A falling line over a pullback in an uptrend, broken upward: a continuation trendline.",
                formal="Trendlines that allow a breakout in the direction of the existing trend are continuation trendlines. Those that allow a breakout in the opposite direction are reversal trendlines. First ascertain which wave degree is being observed.",
            ),
            picture=Figure(
                number="5.43",
                shows="Two existing uptrends. In the first a falling dotted line over a pullback is broken upward: a continuation trendline, with the breakout in the direction of the existing trend. In the second a rising dotted line under the trend is broken downward: a reversal trendline.",
            ),
            text_w=5.8,
            notes=(
                "The left line is a downtrend line of a lower wave degree, drawn inside an uptrend of a higher one. Breaking it continues the larger trend.",
                "Wave degrees, from section 5.1, are what make one breach a continuation and another a reversal.",
            ),
        ),
        Pair(
            left=Term(
                term="Channel, and its return line",
                plain="A trendline and a parallel across price.",
                example="Rising: an uptrend line on troughs 1 and 2, with a parallel from peak 3. Falling: a downtrend line on peaks 4 and 5, with a parallel from trough 6, which violates the uptrend line.",
                formal="A line projected parallel to the trendline from a significant peak or trough is the channel, or return, line. Channels indicate potential entry, profit-taking, price target and stoploss levels.",
            ),
            picture=Figure(
                number="5.44",
                shows="A rising channel turning into a falling channel, headed channel transition: an uptrend line through points 1 and 2 with its channel or return line from point 3, then a downtrend line through points 4 and 5 with its channel or return line from point 6.",
            ),
            text_w=6.0,
            notes=(
                "A channel is a trendline and one parallel to it, on the other side of price. Earlier chapters showed channels and never built one.",
                "In the figure the rising channel transitions into a falling one. Trough 6 violating the uptrend line may be an early indication of a potential trend change.",
                "For alternative approaches to constructing a channel the book refers to Chapter 13.",
            ),
        ),
        Pair(
            left=Term(
                term="Nested channels",
                plain="Channels inside a bigger channel.",
                example="Silver, 4 hour: price transitions through smaller channels within a larger falling channel.",
                formal="The smaller channels are contained, or nested, within the larger channel. Nesting can occur at multiple levels, with large channels comprised of ever-decreasing channel sizes. Channel nesting has fractal-like properties.",
            ),
            picture=Figure(
                number="5.45",
                shows="A 4 hour Silver chart with one larger falling channel drawn across it and many smaller channels, rising and falling, nested within the larger one.",
            ),
            text_w=5.8,
            notes=(
                "The wave degrees of section 5.1, drawn as channels: a small channel inside a medium one inside a large one.",
                "Fractal-like is the book's phrase. The same shape repeats at every size.",
            ),
        ),
        Pair(
            left=Content(
                title="Nested channels at Fibonacci levels",
                lines=(
                    "Nested channeling again, this time on a chart of the USDCAD.",
                    "Notice the channels reacting at the Fibonacci retracement levels.",
                ),
                caption="The book's caption under this figure repeats Figure 5.45's and says Silver. Its text says USDCAD. Retracements are section 5.7.",
            ),
            picture=Figure(
                number="5.46",
                shows="A price chart with nested channels drawn in solid and dashed lines over a set of horizontal Fibonacci retracement levels, from 0.0 to 100.0, with the channel turns falling on those levels.",
            ),
            text_w=4.8,
            notes=(
                "Two kinds of barrier on one chart: the sloping channel lines and the horizontal retracement levels.",
                "Say the slip once: the printed caption belongs to the figure before it.",
            ),
        ),
        Pair(
            left=Content(
                title="Projecting a price target with a channel",
                lines=(
                    "Channels are extremely useful for projecting potential price targets.",
                    "The return line serves as a possible price target, providing resistance to the motion of price.",
                    "In the figure the price targets at points 5 and 6 were forecast accurately by channel projection.",
                ),
                accent="Project the return line forward, and read the target where price meets it.",
            ),
            picture=Figure(
                number="5.47",
                shows="A EURUSD chart: a rising line through troughs 1 and 2 carried on to trough 4, channel projection 1 drawn parallel to it from peak 3 and met by price at point 5, and channel projection 2 carried on to point 6.",
            ),
            text_w=5.4,
            notes=(
                "Channel projection 1 runs from point 3 and was met at point 5. Projection 2 was met at point 6.",
                "This is review question 5: a channel pinpoints where a move may stop before price gets there.",
            ),
        ),
        Pair(
            left=Content(
                title="Anticipating a channel breakout",
                lines=(
                    "Price failing to test one of the channel boundaries may be an early indication of a breakout in the opposite direction.",
                    "A failure to test a channel bottom in an uptrend, or a channel top in a downtrend, is even stronger evidence of a continuation of the existing trend.",
                    "Especially so if the channel breakout bar is accompanied by large volume.",
                ),
                caption="The book's example is its Figure 5.14: price fails to test the lower channel boundary, then breaks out upward at point A.",
            ),
            picture=Chart(
                letter="X",
                shows="A rising channel in which price tests both boundaries several times, then on its last decline fails to reach the channel bottom, turns up early, and breaks out through the channel top.",
            ),
            text_w=CHART_W,
            notes=(
                "The other half of review question 5: a failed test of one boundary points at a breakout through the other.",
                "The chart is ours. The book makes the point on the figure it used for bar retracement symmetry.",
            ),
        ),
        Check(
            label="Channels",
            questions=(
                Q(
                    stem="In a rising channel, the line projected parallel to the uptrend line from a significant peak is called the:",
                    options=("Channel, or return, line",
                             "Internal line",
                             "Neckline",
                             "Reversal trendline"),
                    answer="A",
                    reason="The uptrend line is drawn on two significant troughs, and the parallel from a significant peak is the channel or return line.",
                ),
                Q(
                    stem="In an uptrend, price fails to test the bottom of its rising channel. This is evidence of:",
                    options=("A reversal to the downside",
                             "A failure swing",
                             "A potential continuation of the existing uptrend",
                             "An invalid trendline"),
                    answer="C",
                    reason="A failed test of one boundary points to a breakout in the opposite direction. In an uptrend that is the top: a continuation.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="Sperandeo trendlines",
                plain="Sperandeo's rule for which two points to join.",
                example="An uptrend's lowest trough is PHP 40, and its highest minor trough before the PHP 60 peak is PHP 55: the line runs from the first through the second.",
                formal="Uptrend line: from the lowest trough to the highest minor trough preceding the highest peak. Downtrend line: from the highest peak to the lowest minor peak preceding the lowest trough. From Victor Sperandeo's book Trader Vic: Methods of a Wall Street Master.",
            ),
            picture=Figure(
                number="5.48",
                shows="Two drawings. A Sperandeo uptrend line from the lowest trough through the highest minor trough preceding the highest peak, and a Sperandeo downtrend line from the highest peak through the lowest minor peak preceding the lowest trough.",
            ),
            text_w=6.6,
            notes=(
                "Find the extreme first, the highest peak, then walk back to the last minor trough before it. The line joins that to the lowest trough.",
                "The author writes that there is no way he can do justice to the approach here, and advises reading Sperandeo's book. The pesos are ours.",
            ),
        ),
        Pair(
            left=Term(
                term="DeMark trendlines",
                plain="A more responsive line: newest points first.",
                example="Of three uptrend lines in the figure, only the one through the two most recent troughs is marked correct.",
                formal="Uptrend line: from the two most recent qualified troughs. Downtrend line: from the two most recent qualified peaks. From Thomas DeMark's The New Science of Technical Analysis, where the book sends the reader for how a point qualifies.",
            ),
            picture=Figure(
                number="5.49",
                shows="A rising candlestick chart with three uptrend lines drawn from different pairs of troughs: the one through the two most recent troughs is marked correct and the two drawn from older troughs are marked wrong.",
            ),
            text_w=6.0,
            notes=(
                "A conventional trendline starts from the oldest troughs. DeMark's starts from the newest, which is why it is more responsive.",
                "Do not teach the pivot selection process. The book sends the reader to DeMark for it.",
            ),
        ),
        Pair(
            left=Term(
                term="Standard fan lines",
                plain="Three trendlines fanning out from one point.",
                example="Decelerating: three uptrend lines from a significant lower trough to gradually declining higher troughs. Accelerating: the mirror, three downtrend lines from a significant higher peak.",
                formal="They indicate a change in trend: violation of the third fan line is strong confirmation. They provide support and resistance, change roles when breached, and trade like any trendline.",
            ),
            picture=Figure(
                number="5.50",
                shows="Two drawings: decelerating fan lines, three uptrend lines fanning out from one trough and numbered 1st, 2nd and 3rd as they flatten, and accelerating fan lines, three downtrend lines fanning out from one peak.",
            ),
            text_w=6.0,
            notes=(
                "All three lines share one starting point: a trough for the decelerating set, a peak for the accelerating one.",
                "Tentative and valid do not apply to fan lines. A fan line uses two inflection points but only one is at a peak or trough.",
                "Accelerating fan lines run from a significant higher peak to gradually rising lower peaks. The book says to draw only three of either.",
            ),
        ),
        Pair(
            left=Term(
                term="Fibonacci fan lines",
                plain="Fan lines through three Fibonacci levels.",
                example="A range from PHP 40 to PHP 60 gives a vertical line PHP 20 tall, with three marks on it.",
                formal="To construct a bearish one: identify a significant Fibonacci retracement range. Draw a vertical line from the peak of the range to the trough's price level. Divide it into 38.2, 50 and 61.8 percent levels. Project three lines from the trough, intercepting those three levels.",
            ),
            picture=Figure(
                number="5.51",
                shows="A rise from a trough to a peak with a vertical line dropped from the peak to the base, divided at 38.2, 50.0 and 61.8 percent, and three lines projected from the trough through those three points.",
            ),
            text_w=6.2,
            notes=(
                "This is the fan line whose second point is not a peak or trough: it sits along a predetermined vertical axis.",
                "Fibonacci ratios are Chapter 10. Today the three percentages are given, not derived. The pesos are ours.",
            ),
        ),
        Pair(
            left=Term(
                term="Speed lines",
                plain="Fibonacci fan lines, drawn with thirds.",
                example="The same vertical line, divided into thirds: a 1/3 speed line and a 2/3 speed line.",
                formal="Edson Gould's speed lines also track the progress of a trend as it attempts to bottom or top. They are created in exactly the same way as Fibonacci fan lines, except that the retracement ratios are one-third and two-thirds.",
            ),
            picture=Figure(
                number="5.52",
                shows="A rise from a trough to a peak with a vertical line dropped from the peak to the base and divided into three thirds, and two lines projected from the trough through the division points: the 1/3 speed line and the 2/3 speed line.",
            ),
            text_w=5.6,
            notes=(
                "One construction, two sets of ratios: Fibonacci's three percentages, or Gould's two thirds.",
                "One-third and two-thirds are also the retracements Dow watched, which is the next section.",
            ),
        ),
        Pair(
            left=Term(
                term="Andrew's Pitchfork",
                plain="Three parallel lines; a geometric overlay.",
                example="Daily Silver: support at the median line and upper band. Bullish: the converse.",
                formal="A geometrically based price overlay whose lines provide support and resistance. Bearish: after a significant peak, take an upside retracement that does not exceed it. The median line runs from the peak through the midpoint between the retracement trough and peak. Project parallels from both.",
            ),
            picture=Figure(
                number="5.53",
                shows="A daily Silver chart with a falling pitchfork: a significant peak, a retracement trough and a retracement peak, three parallel falling lines, and labels where prices react at the median line and tag the upper band.",
            ),
            text_w=6.2,
            notes=(
                "Three points make it: the significant peak, the retracement trough, the retracement peak. The middle line is called the median.",
                "It is a channel with a centre line, drawn from three points and not two.",
            ),
        ),
        Check(
            label="Other trendlines and fan lines",
            questions=(
                Q(
                    stem="DeMark trendlines in an uptrend are constructed from:",
                    options=("The lowest trough and the highest peak",
                             "The two most recent qualified troughs",
                             "The two oldest troughs on the chart",
                             "The lowest trough and the highest minor trough"),
                    answer="B",
                    reason="DeMark uses the two most recent qualified troughs in an uptrend, and the two most recent qualified peaks in a downtrend.",
                ),
                Q(
                    stem="Speed lines differ from Fibonacci fan lines in that their retracement ratios are:",
                    options=("38.2, 50 and 61.8 percent",
                             "One-eighth and one-quarter",
                             "25, 50 and 75 percent",
                             "One-third and two-thirds"),
                    answer="D",
                    reason="Speed lines are created in exactly the same way as Fibonacci fan lines, except the ratios are one-third and two-thirds.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.7 - Trend retracements. Chapter 10 is Fibonacci and Chapter 19 Gann.
# ==========================================================================

SECTION7 = Section(
    number=7,
    title="Trend Retracements",
    short="5.7 Retracements",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.7  Three ways to measure a retracement",
                lines=(
                    "Fibonacci retracements are based on various ratios related to the Fibonacci Phi ratio.",
                    "Dow, as in Chapter 2, paid particular attention to the one-third and two-thirds retracements.",
                    "Gann employed one-third and one-eighth retracement ranges.",
                ),
                accent="Gann and Dow both regarded 50 percent as the most significant, with most major tops and bottoms forming around it.",
                caption="The book leaves the detail to 'a subsequent chapter', unnamed. Its Chapter 10 is Fibonacci and its Chapter 19 Gann.",
            ),
            picture=Figure(
                number="5.54",
                shows="A table of retracement percentages in three columns. Fibonacci: 23.6, 38.2, 50 in brackets, 61.8 and 78.6. Dow: 33, 50 and 66. Gann: 12.5, 25.0, 37.5, 50.0, 62.5, 75.0 and 87.5.",
            ),
            text_w=6.2,
            notes=(
                "A retracement percentage is a share of the move being retraced, as in Chapter 2. Read the table across, not down: each row is one zone and three ways of naming it.",
                "The Gann column is in eighths: 12.5 percent is one-eighth. Nothing here is derived; that waits for the later chapters.",
            ),
        ),
        Pair(
            left=Content(
                title="Where the three approaches agree",
                lines=(
                    "Set side by side, the retracement percentages converge strongly around specific ranges.",
                    "Between 33 and 38.2 percent.",
                    "At 50 percent.",
                    "Between 61.8 and 66 percent.",
                ),
                accent="Probably the most important retracement percentage of all is the 50 percent level.",
            ),
            picture=Chart(
                letter="Y",
                shows="A rise from PHP 40 to PHP 60 and the retracement after it, with the three ranges where the approaches converge shaded: 33 to 38.2 percent, 50 percent at PHP 50, and 61.8 to 66 percent.",
            ),
            text_w=CHART_W,
            notes=(
                "The rise on the chart is PHP 20, so a 50 percent retracement gives back PHP 10 and stands at PHP 50.",
                "Three people measuring three ways still watch the same three zones. That is what convergence buys.",
            ),
        ),
    ),
)

# ==========================================================================
# 5.8 - Gaps and trends.
# ==========================================================================

SECTION8 = Section(
    number=8,
    title="Gaps and Trends",
    short="5.8 Gaps",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Term(
                term="5.8  Common, breakaway, runaway and exhaustion gaps",
                plain="Each is named for where in the trend it opens.",
                example="Weekly Wheat shows all four of Chapter 3's gaps.",
                formal="Common: within a trading range, considered insignificant. Breakaway: as price breaks away from a consolidation or chart pattern. Runaway, measuring, midway or continuation: in a strong trend phase; there may be more than one. Exhaustion: at the end of a trend, before a consolidation or reversal.",
            ),
            picture=Figure(
                number="5.55",
                shows="A weekly Wheat chart with each kind of gap boxed and named: common gaps inside the consolidation, then a breakaway gap, a runaway gap and an exhaustion gap up the trend, with arrows from the three trend gaps to later levels of support.",
            ),
            text_w=6.2,
            notes=(
                "Chapter 3 defined a gap and named these four for later, and Chapter 4 met three of them as San Ku. This is where the book says what each one is.",
                "Runaway, measuring, midway and continuation are four names for one gap. On the Wheat chart: common gaps inside the consolidation, then the three trend gaps.",
                "Prices top after the third gap, the exhaustion gap: characteristic 12 from section 5.2.",
            ),
        ),
        Pair(
            left=Content(
                title="Gaps forecasting trend exhaustion",
                lines=(
                    "Weekly Wheat: common gaps within the consolidation, then the trend-related gaps.",
                    "Prices top after the third gap: potential trend exhaustion.",
                    "The exhaustion is at a significant resistance level, created by a strong price rejection.",
                ),
                accent="Gaps help to define the stages within a trend, and so indicate potential tops and bottoms.",
                caption="The rejection is at the high of what the book calls a very bearish shooting star pattern. Candlesticks are Chapter 14.",
            ),
            picture=Figure(
                number="5.56",
                shows="A weekly Wheat chart: a strong price rejection at an early high, a dashed line carrying that level across as prior resistance, an accumulation box holding a common gap, then a breakaway gap, a midway gap and an exhaustion gap rising into a distribution box at the resistance.",
            ),
            text_w=5.6,
            notes=(
                "Chapter 4's phases, located by gaps: common gaps in the accumulation, the exhaustion gap opening the distribution.",
                "Two signs agree at the top: a third gap, and a significant resistance level. Barrier proximity again.",
            ),
        ),
        Pair(
            left=Content(
                title="Gaps become support and resistance",
                lines=(
                    "Gaps tend to create areas of potential support and resistance.",
                    "On the weekly Wheat chart the gaps give rise to subsequent levels of support.",
                    "On a 15 minute chart of GLD, gaps give rise to areas of both support and resistance.",
                ),
                accent="The cycle-tuned stochastic helps to corroborate the levels: overbought at resistance, oversold at support.",
            ),
            picture=Figure(
                number="5.57",
                shows="A 15 minute chart of the SPDR Gold Trust Shares headed gaps as support and resistance: horizontal lines drawn from each gap, parallel dashed lines showing angular symmetry in GLD, and a cycle-tuned stochastic below with its extremes circled.",
            ),
            text_w=5.0,
            notes=(
                "A gap is a price range nobody traded in. Its edges are levels, and levels act as barriers.",
                "The figure also marks angular symmetry in GLD: characteristic 8, on a different chart.",
            ),
        ),
        Check(
            label="Retracements and gaps",
            questions=(
                Q(
                    stem="Both Gann and Dow regarded which retracement percentage as the most significant?",
                    options=("33 percent",
                             "38.2 percent",
                             "50 percent",
                             "61.8 percent"),
                    answer="C",
                    reason="Both regarded 50 percent as the most significant, with most major tops and bottoms forming around that level.",
                ),
                Q(
                    stem="A gap created as price leaves a consolidation or chart pattern is a:",
                    options=("Breakaway gap",
                             "Common gap",
                             "Runaway gap",
                             "Exhaustion gap"),
                    answer="A",
                    reason="Common gaps sit within a range, runaway gaps in a strong trend phase, and exhaustion gaps at the end of a trend.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.9 - Trend directionality.
# ==========================================================================

SECTION9 = Section(
    number=9,
    title="Trend Directionality",
    short="5.9 Directionality",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Term(
                term="5.9  Unidirectional and bidirectional entries",
                plain="Trade one way only, or whichever way it breaks.",
                example="Take only breakouts with the trend and, over the long term, you have traded both ways: micro-unidirectional entries are equivalent to a macro-bidirectional approach, unless a qualified trade is skipped.",
                formal="A unidirectional entry is a trade taken only in the direction of the existing trend, up or down. A bidirectional entry is a trade taken in either direction, depending on which way the breakout occurs.",
            ),
            picture=Figure(
                number="5.58",
                shows="A price rising and falling between two levels, with longs marked only on the way up and shorts only on the way down, labelled micro-unidirectional entries, over the words equivalent to a macro-bidirectional mechanism: a buy-sell straddle, buying above one line and selling below the other.",
            ),
            text_w=7.0,
            notes=(
                "Micro means very short-term and macro means longer-term. The trader only ever trades one way at any one time.",
                "The figure's lower half is the bidirectional trader: one buy level above, one sell level below, whichever breaks.",
            ),
        ),
    ),
)

# ==========================================================================
# 5.10 - Drummond geometry.
# ==========================================================================

SECTION10 = Section(
    number=10,
    title="Drummond Geometry",
    short="5.10 Drummond",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Term(
                term="5.10  Drummond geometry",
                plain="Drummond's way to stay on the right side.",
                example="Price above the PLdot: the market is regarded as bullish. Below the PLdot: bearish. Some buy when it turns up and sell when it turns down.",
                formal="Charles Drummond's method: a short-term moving average, the PLdot line, and inter-bar trendlines that forecast support and resistance. The PLdot is a simple three-period moving average of typical price, and may be forward shifted by one period.",
            ),
            picture=Figure(
                number="5.59",
                shows="A weekly EURUSD chart with a short moving average hugging price, labelled PLdot approximated by a 3-period SMA of typical price: price above the SMA is bullish, price below it is bearish, and buy when the SMA turns up and sell when it turns down.",
            ),
            text_w=6.4,
            notes=(
                "For a detailed look the book refers the reader to The Ultimate Trading Guide, by Hill, Pruitt and Hill.",
                "Typical price is named and not defined in this chapter. The forward shift is there to give an early prognostication of market sentiment.",
                "The inter-bar trendlines connect the highs and the lows.",
            ),
        ),
        Check(
            label="Directionality and Drummond",
            questions=(
                Q(
                    stem="A trade taken in either direction, depending on which way the breakout occurs, is a:",
                    options=("Unidirectional entry",
                             "Barrier entry",
                             "Retracement entry",
                             "Bidirectional entry"),
                    answer="D",
                    reason="A unidirectional entry is taken only in the direction of the existing trend. A bidirectional one goes whichever way the breakout does.",
                ),
                Q(
                    stem="In Drummond geometry, price above the PLdot line means the market is regarded as:",
                    options=("Bearish",
                             "Bullish",
                             "Overbought",
                             "In consolidation"),
                    answer="B",
                    reason="When price is above the PLdot the market is regarded as bullish, and when it is below, bearish.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 5.11 - Forecasting trend reversals. The book's own summary by technique.
# ==========================================================================

SECTION11 = Section(
    number=11,
    title="Forecasting Trend Reversals",
    short="5.11 Reversals",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="5.11  Signs that a trend may reverse",
                lines=(
                    "Volume: diminishing volume in a trend, or extreme volume in a buying or selling climax.",
                    "Chart patterns: bearish after a strong, prolonged uptrend, bullish after a downtrend.",
                    "Cycles: peaks at tops, troughs at bottoms, or decreasing cycle amplitude or period in a trend.",
                    "Tops at significant historical resistance levels, bottoms at historical support levels.",
                ),
                caption="Also a chart pattern sign: the appearance of a large broadening, diamond or island formation.",
            ),
            picture=Chart(
                letter="Z",
                shows="A long uptrend into a market top with four of the book's signs marked: cycle amplitude decreasing during the trend, volume diminishing as price rises and then extreme in a buying climax, and the top forming at a significant historical resistance level.",
            ),
            text_w=CHART_W,
            notes=(
                "The book calls this section a summary. These four are the ones this chapter and the last have already taught.",
                "Diminishing volume indicates potential weakness in the trend. Extreme volume is indicative of market tops and bottoms.",
            ),
        ),
        Content(
            title="Reversal signs from tools taught later",
            lines=(
                "Oscillators: overbought signals at tops, oversold signals at bottoms.",
                "Bearish divergence with price at market tops, bullish divergence at bottoms.",
                "The oscillator crossing below its signal and equilibrium line at tops, above at bottoms.",
                "Candlesticks: bearish formations at market tops, bullish formations at bottoms.",
                "Intermarket: bearish action in the broad markets leading to a top in the stock, bullish action in highly correlated markets leading to a bottom.",
            ),
            caption="The book calls this section a summary and refers to the relevant chapters for each approach.",
            notes=(
                "No picture: each of these needs a tool the book has not taught yet. Oscillators are Chapter 8, divergence Chapter 9, candlesticks Chapter 14.",
                "With the last slide these are the book's seven headings, a to g. Together they answer review question 3.",
            ),
        ),
        Check(
            label="Forecasting reversals",
            questions=(
                Q(
                    stem="Which volume behavior tends to accompany a potential market reversal?",
                    options=("Steady, average volume throughout",
                             "Volume rising in step with the trend",
                             "Diminishing volume, or extreme volume in a climax",
                             "None: volume has no bearing on reversals"),
                    answer="C",
                    reason="Diminishing volume indicates potential weakness in the trend, and buying or selling climaxes are indicative of market tops and bottoms.",
                ),
                Q(
                    stem="Potential market tops tend to form at:",
                    options=("Significant historical resistance levels",
                             "Significant historical support levels",
                             "Cycle troughs",
                             "Oversold oscillator signals"),
                    answer="A",
                    reason="Tops tend to form at significant historical resistance levels, and bottoms at significant historical support levels.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Opening and closing. Section 5.12, the book's summary, feeds the closing.
# ==========================================================================

OPENERS = (
    Content(
        title="What you will be able to do",
        lines=(
            "Understand the significance of a market trend and its underlying characteristics.",
            "Recognize the limitations of defining trend and market action.",
            "Identify early indications of a potential market reversal.",
            "Read the markets in terms of wave cycles of various degrees.",
            "Set up effective price filtering, and calculate the optimum tradesize for breakout trades.",
            "Use channels, trendlines, fan lines and Drummond geometry to track the market.",
        ),
        notes=(
            "These are the book's seven learning objectives, trimmed to six lines. The fifth line joins its fifth and sixth.",
            "Do not read all of them aloud. Say the first and the last, and that every one is examinable.",
        ),
    ),
    Content(
        title="How this chapter is laid out",
        lines=(
            "5.1  What a trend is, and where any definition runs out.",
            "5.2  Sixteen price characteristics that show the quality of a trend.",
            "5.3 to 5.5  Filters, orders, entries, stops and tradesize.",
            "5.6  Trendlines, channels and fan lines.",
            "5.7 to 5.11  Retracements, gaps, directionality, Drummond, reversal signs.",
        ),
        accent="Eleven sections, the book's own. Two of them are long: 5.2 and 5.6.",
        notes=(
            "The parts are the book's own sections. The marker at the bottom left of every slide says which one we are in.",
            "Say the checks carry no marks. Each question slide is followed by its answers on a slide of their own.",
        ),
    ),
)

CLOSING = (
    Content(
        title="Chapter 5 in five sentences",
        lines=(
            "Dow defines a trend by its peaks and troughs, and every definition has limits.",
            "Sixteen price characteristics show a trend's quality: watch each for a change.",
            "Filters, orders, stops and tradesize settle how a trend is entered and exited.",
            "Trendlines, channels and fan lines are barriers: support, resistance, targets.",
            "Retracements, gaps and the signs in 5.11 warn that a trend may reverse.",
        ),
        accent="The book's own summary: pay particular attention to the 16 characteristics.",
        notes=(
            "Read all five slowly. This is the summary to copy down.",
            "The book's summary is three sentences long. Its one piece of advice is the gold line.",
        ),
    ),
    Content(
        title="The review questions to prepare",
        lines=(
            "What is a trend? Explain the disadvantages of defining market and price action.",
            "What are the early indications of a potential reversal?",
            "Briefly describe the ways in which price action may be understood.",
            "How can channel analysis help pinpoint potential reversals and continuations?",
            "What are the factors that impact trendline reliability?",
            "Explain the advantages of proportional sizing, and of price-based filters.",
        ),
        caption="All eight of the book's questions, on six lines. Question 4 says 12 ways; section 5.2 lists 16.",
        notes=(
            "Lines one and six each carry two of the book's eight questions.",
            "Say where each answer sits: 5.1, 5.11, 5.2, 5.6, 5.6, then 5.5 and 5.3.",
        ),
    ),
    Content(
        title="What the book uses, and where it says two things",
        lines=(
            "Never defined here: breakout, wave cycle, wave degree. Used, not taught: typical price, the cycle-tuned stochastic, MACD, candlesticks.",
            "Sent ahead: divergence, Chapter 9. Channels, Chapter 13. Elliott, Chapter 18. Tradesizing, Chapter 28.",
            "Sixteen characteristics in 5.2, twelve in review question 4. Four entry modes announced, five listed.",
            "Figure 5.24: $3.30 a day in the text, $3.80 on the figure.",
        ),
        accent="Where the book disagrees with itself, the slide says so.",
        notes=(
            "Be straight with them: this chapter leans on oscillators and candlesticks the book has not taught yet.",
            "Next is Chapter 6, Volume and Open Interest.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 5",
    title="Trend Analysis",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    # The objectives and the roadmap are drawn by OPENERS above, one slide
    # each. These two fields are what the generated frame would have used.
    objectives=OPENERS[0].lines,
    roadmap=OPENERS[1].lines,
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6,
              SECTION7, SECTION8, SECTION9, SECTION10, SECTION11),
    closing=CLOSING,
    openers=OPENERS,
    title_notes=(
        "Greet the room, then say what today buys them: what a trend is, how to judge its quality, and how to get in and out of one.",
        "Say every idea today has a picture beside it. Where the book drew one it is the book's; the rest are ours.",
    ),
    dividers=False,
)
