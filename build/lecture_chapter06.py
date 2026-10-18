"""FIN1209 Chapter 6 student lecture notes, as plain data.

This is the file a contributor edits. Layout lives in build/lecturekit.py and
knows nothing about any chapter; the reasoning behind the layout, with the
research it came from, is chapter-01/lecture-notes-design.md.

    .venv/bin/python build/build_lecture_notes6.py

Written for a student reading alone, with no instructor in the room. Full
sentences that explain, not bullets that gesture. The six sections are the
deck's six parts in the deck's order. Sections 1 to 5 are the book's section
6.1, in its own order of sub-headings, and Section 6 is its section 6.2, so a
student can move between the slides, the book and these pages.

Nothing here is timing, cuts, speaker cues, check answers or slide numbers.
Those belong to the instructor: the timing and the cuts are in
build/plan_chapter06.py, and the check answers are not in this repository at
all.

**Every picture the deck places is placed here too**, all 44 of the book's
figures and all 44 of our own charts, and build_lecture_notes6.py fails if
one is missing. The lean rule is that the book's content is never cut, and
the notes are held to it.

Figure descriptions are never retyped here. The build takes them from
content_chapter06.py, which is also where the deck's own placeholder takes
them, so the two documents cannot describe the same figure differently.

The definitions are not retyped either. Every Define block below takes its
wording from the deck's own term slide through ``formal()``, so a term is
defined in the same words in both documents by construction. The plain words
and the example belong in the paragraphs around it. The learning objectives
are read from the deck the same way.

Bold covers whole sentences, never a phrase inside one: the paginator moves
a bold element whole, so a bold phrase lets a page break fall inside its
sentence. AGENTS.md has the history.
"""

from __future__ import annotations

import re

import deckkit
from content_chapter06 import CHAPTER
from lecturekit import (Define, Fig, Head, LectureNotes, Panel, Para, Points,
                        Section, SelfCheck)


def term_name(slide: deckkit.Term) -> str:
    """The term a slide teaches, without a book section number.

    No Chapter 6 term opens a part, so none carries one; the rule is kept
    from Chapter 4 so that a later edit cannot leak one into the index.
    """
    return re.sub(r"^\d+\.\d+\s+", "", slide.term)


def _term_slides():
    for part in CHAPTER.sections:
        for slide in part.slides:
            if isinstance(slide, deckkit.Pair):
                slide = slide.left
            if isinstance(slide, deckkit.Term):
                yield slide


_FORMAL = {term_name(slide): slide.formal for slide in _term_slides()}


def formal(term: str) -> Define:
    """The deck's own formal definition of ``term``, as a Define block."""
    return Define(term=term, text=_FORMAL[term])


def figure(number: str, caption: str, height_mm: float = 62.0) -> Fig:
    """One of the book's figures, alone on the measure."""
    return Fig(panels=(Panel(number=number),), cols=1, height_mm=height_mm,
               caption=caption)


def chart(letter: str, caption: str, height_mm: float = 76.0) -> Fig:
    """One of our own charts.

    They are drawn for the slide's picture column, about 140mm wide beside
    a teaching slide and 115mm beside a term, with 10 point labels. On this
    page the height sets the width, and at 76mm the labels are a little
    over 7 point. Shorter than that and they cannot be read in print.
    """
    return Fig(panels=(Panel(number=letter),), kind="chart",
               height_mm=height_mm, caption=caption)


# ==========================================================================
# Section 1 - confirmation and divergence (the book's 6.1, pp.173 to 180)
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Confirmation and Divergence",
    standfirst="What volume is, when it is bullish and when bearish, what "
               "volume divergence and confirmation mean, how they differ "
               "from the divergence of Chapters 4 and 5, and the two kinds "
               "of volume oscillator. The book's section 6.1, pages 173 to "
               "180.",
    blocks=(
        Head(number="1.1", text="Price first, volume as evidence"),
        Para(text=(
            "The chapter opens by putting volume in its place. Price is "
            "regarded as the best indicator of potential future price "
            "behavior. Volume and open interest offer additional evidence "
            "to corroborate a bullish or bearish setup, can show underlying "
            "weakness, and can work as timing indicators for potential "
            "breakouts. The book also warns that many novices misread "
            "declining volume as a weakness in a consolidation; Section 2 "
            "explains why that is a misreading."
        )),
        chart("A", "Price bars over their volume, one day picked out."),
        Para(text=(
            "Chart A shows how every figure in this chapter is drawn. The "
            "price bars are in the upper panel and the volume bars in the "
            "lower panel, one volume bar standing directly under each price "
            "bar. Find the gold day: its price bar says where it traded and "
            "closed, and the bar under it says how much traded."
        )),

        Head(number="1.2", text="Chapter 2's tenet, recalled"),
        Para(text=(
            "Chapter 2 taught Dow's sixth tenet: volume must confirm the "
            "trend. Volume should expand in the direction of the "
            "preexisting trend. In an uptrend it should rise as price rises "
            "and fall in downside retracements; the book calls that bullish "
            "volume action. In a downtrend it should rise as price falls "
            "and fall in upside retracements: bearish volume action. "
            "Volume is a supporting, or secondary, indicator. Any volume "
            "action contrary to this is an indication that an uptrend may "
            "potentially be bearish and a downtrend bullish."
        )),
        figure("6.1", "Volume confirming a preexisting trend."),
        Para(text=(
            "Figure 6.1 draws both halves of the tenet. In each sketch, "
            "look for where the tall volume bars sit: under the move that "
            "goes with the trend. The short ones sit under the retracement."
        )),

        Head(number="1.3", text="Volume, and the two principles"),
        Para(text=(
            "Volume has been on our charts since Chapter 1, and this is "
            "where the book defines it. Suppose one day sees five trades, "
            "of 0.1, 0.6, 0.3, 1.2 and 0.2 million shares. That day's "
            "volume is their total, 2.4 million shares. For a futures "
            "market the count is in contracts."
        )),
        formal("Volume"),
        chart("B", "One day's five trades, added up to its volume."),
        Para(text=(
            "Chart B sets out that sum: five columns, one per trade, and "
            "the day's total in gold at the right."
            "\n\n"
            "The book asks for two principles to be remembered whenever "
            "volume is studied. First, a rise in volume means participants "
            "want to see price go higher in an uptrend, or lower in a "
            "downtrend, and are willing to buy higher or sell lower to "
            "take part. Second, a decline in volume means they are losing "
            "interest, and would rather buy lower in an uptrend or sell "
            "higher in a downtrend, if they are not exiting altogether. "
            "**Volume, in short, measures participation.**"
        )),
        chart("C", "Two rallies: one on rising volume, one on falling."),
        Para(text=(
            "In Chart C both rallies rise. Read the gold arrows in the "
            "volume panel: under the first rally, numbered 1, volume grows "
            "as buyers join; under the second, numbered 2, it shrinks as "
            "they lose interest."
        )),

        Head(number="1.4", text="Bullish volume and bearish volume"),
        Para(text=(
            "The book states the next rule four times, once for each trend "
            "and each direction of volume, and all four say the same "
            "thing. Volume that moves with price is bullish; volume that "
            "moves against price is bearish. A share that rallies on "
            "rising volume and dips on falling volume shows bullish volume "
            "both times. A share that falls on rising volume and bounces on "
            "falling volume shows bearish volume both times."
        )),
        formal("Bullish volume and bearish volume"),
        chart("D", "The four cases of price and volume together."),
        Para(text=(
            "Chart D puts the four cases in a grid. The top row is volume "
            "moving with price, bullish; the bottom row is volume moving "
            "against it, bearish. Notice that falling volume appears in "
            "both rows: on its own it means nothing until the direction of "
            "price is known."
            "\n\n"
            "That is the point of the book's warning. Declining volume does "
            "not necessarily imply bearishness, and rising volume does not "
            "imply bullishness. The book calls the opposite reading a "
            "simple mistake that many novices make."
        )),
        figure("6.2", "Bullish volume in gold's primary bull trend."),
        Para(text=(
            "Figure 6.2 is the continuous daily chart of gold. Look at the "
            "volume panel through the long rise, expanding with the trend, "
            "and then at the retracement at the right, where price and "
            "volume fall together. That fall in volume is bullish."
        )),
        figure("6.3", "Volume not confirming a preexisting trend."),
        Para(text=(
            "Figure 6.3 swaps the volume of Figure 6.1. In an uptrend whose "
            "volume shrinks on the rises and grows in the retracements, "
            "the volume is bearish: a potentially weak or bearish uptrend. "
            "In a downtrend whose volume shrinks on the falls and grows in "
            "the upside retracements, it is bullish: a potentially bullish "
            "downtrend."
        )),
        SelfCheck(text=(
            "In an uptrend, price dips for a week and volume falls during "
            "the dip. Is that volume bullish or bearish, and why does the "
            "fall in volume not settle it on its own?"
        )),

        Head(number="1.5", text="Volume divergence and confirmation"),
        Para(text=(
            "The book now introduces a second pair of words, and this pair "
            "ignores price altogether. Volume falling is divergence. "
            "Volume rising is confirmation, which the book also calls "
            "convergence. If a share rises from 40 to 46 pesos while its "
            "daily volume shrinks from 3 million to 1 million shares, that "
            "is volume divergence; had volume grown to 5 million, it would "
            "be confirmation."
        )),
        formal("Volume divergence and volume confirmation"),
        chart("E", "Divergence and confirmation, each under both kinds of "
                   "price move."),
        Para(text=(
            "Read Chart E by its columns. The left column is volume "
            "falling, divergence, once under a rising price and once under "
            "a falling one. The right column is volume rising, "
            "confirmation, under both. Price goes both ways in each column."
            "\n\n"
            "Divergence says participants are not interested in seeing "
            "price go further: bearish for an uptrend, bullish for a "
            "downtrend. Confirmation says they are interested in taking "
            "part: bullish for an uptrend, bearish for a downtrend. "
            "**Confirmation is an early indication of a potential "
            "continuation of the trend, and divergence of a potential "
            "reversal.** The book adds that divergence always indicates "
            "potential weakness in an existing trend and confirmation "
            "always potential strength."
        )),
        chart("F", "Confirmation continuing, divergence turning."),
        Para(text=(
            "Chart F shows the two side by side. In the left uptrend volume "
            "rises with price and the trend continues. In the right one "
            "volume falls as price rises, and price turns down at the end. "
            "That ending is one possibility, drawn to show what the warning "
            "means; divergence warns and does not guarantee."
        )),

        Head(number="1.6", text="Four names"),
        Para(text=(
            "Put the two pairs together and there are four names. Price and "
            "volume falling together is bullish divergence. Both rising is "
            "bullish confirmation. Volume falling while price rises is "
            "bearish divergence, and volume rising while price falls is "
            "bearish confirmation. That list is the book's own summary of "
            "every scenario."
        )),
        formal("Bullish and bearish divergence and confirmation"),
        figure("6.4", "The four names, as price over a supporting series."),
        Para(text=(
            "Figure 6.4 draws the four as columns, each a price path over "
            "a supporting series. The book's figure lists volume bars, a "
            "volume moving average, open interest, and, in brackets, the "
            "ATR as supporting series. The ATR appears in no sentence of "
            "the chapter's text."
            "\n\n"
            "One place where the book says two things. It says bullish "
            "divergence can only occur in a downtrend, yet Figure 6.6 "
            "below finds bullish divergence in two dips inside an uptrend. "
            "These notes read downtrend there as price falling, for any "
            "stretch, which is how the summary list reads it. That reading "
            "is ours."
        )),

        Head(number="1.7", text="Not the divergence of Chapters 4 and 5"),
        Para(text=(
            "Chapters 4 and 5 showed standard divergence: price makes a "
            "higher peak while an oscillator, the MACD in Chapter 4 or the "
            "averaged bar stochastic in Chapter 5, makes a lower one. That "
            "test compares two peaks on two lines. Volume divergence does "
            "not. **Unlike standard price-based oscillators, the direction "
            "of price is irrelevant to whether volume diverges.** Price's "
            "direction is still needed to say whether the divergence is "
            "bullish or bearish. The book also says there is no reverse "
            "divergence classification for volume, and sends the "
            "classification of divergence in general to its Chapter 9. "
            "This is review question 3."
        )),
        chart("G", "Standard divergence beside volume divergence."),
        Para(text=(
            "Chart G puts the two tests side by side. On the left, follow "
            "the two gold arrows: price's second peak is higher, the "
            "oscillator's lower. On the right there are no peaks to "
            "compare: the price rises and the volume under it falls, and "
            "that alone is volume divergence."
        )),

        Head(number="1.8", text="Two worked charts"),
        figure("6.5", "Bullish volume divergence on Isis Pharmaceuticals."),
        Para(text=(
            "Figure 6.5 is Isis Pharmaceuticals tracing out a bullish "
            "rounding bottom, a pattern Chapter 4 named. Look at the two "
            "dashed lines in the volume panel, each labelled bullish volume "
            "divergence: price falls and volume falls with it. The book "
            "calls it divergence providing additional evidence of a bullish "
            "chart formation."
        )),
        figure("6.6", "Ten periods of bullish volume in the SPDR Gold "
                      "Trust.", height_mm=66.0),
        Para(text=(
            "Figure 6.6 splits the SPDR Gold Trust into ten periods; its "
            "caption says daily, though the chart is labelled weekly. "
            "Periods 1, 3, 7 and 9 show bullish confirmation, 4 and 6 "
            "bullish divergence, and 5 flat volume. In periods 2, 8 and 10 "
            "volume declines during a consolidation, where it works as a "
            "breakout timing indicator: at the end of each, price breaks "
            "out as volume reaches its minimum for the period."
        )),
        chart("H", "One invented uptrend in four periods."),
        Para(text=(
            "Chart H is the same reading on one invented uptrend, so each "
            "kind of period can be seen. Period 1 rises on rising volume, "
            "bullish confirmation. Period 2 dips on falling volume, bullish "
            "divergence. Period 3 moves sideways while volume falls to its "
            "minimum, a consolidation. Period 4 breaks out and rises on "
            "rising volume. Every period is bullish volume."
        )),
        SelfCheck(text=(
            "Price makes a higher high while volume makes a lower high. Is "
            "that volume divergence? Would it still be volume divergence if "
            "price had made a lower high instead?"
        )),

        Head(number="1.9", text="Two kinds of volume oscillator"),
        Para(text=(
            "The book calls volume indicators drawn in their own panel "
            "under price volume oscillators, and sorts them into two kinds "
            "for the purpose of reading divergence. Plain volume bars count "
            "shares and nothing else. A line that adds the day's volume "
            "when the close rises and subtracts it when the close falls "
            "uses price as well."
        )),
        formal("Price-based and non-price-based volume oscillators"),
        chart("I", "Price, volume bars, and a price-based line from the "
                   "same days."),
        Para(text=(
            "Chart I draws three panels over the same days: the closes, the "
            "volume bars, which are non-price-based, and a line that needs "
            "the closes to be drawn, which is price-based. That bottom line "
            "is the On Balance Volume, taught in Section 6."
        )),
        Points(
            title="The book's two lists",
            items=(
                "Price-based: On Balance Volume (OBV), the "
                "Accumulation/Distribution Line (ADL), Chaikin Money Flow, "
                "the Chaikin Oscillator, the Demand Index and the Herrick "
                "Payoff Index.",
                "Non-price-based: standard volume bars, smoothed volume, "
                "detrended volume, the rate of change of volume (ROC "
                "volume) and the percentage volume oscillator (PVO).",
            ),
        ),
        Para(text=(
            "The OBV, the ADL, the two Chaikin indicators and the Herrick "
            "index are taught in Section 6 and smoothed volume in Section "
            "3. The Demand Index, detrended volume, ROC volume and the PVO "
            "are named in the chapter and never explained."
        )),
        figure("6.7", "Reading divergence on the two kinds."),
        Para(text=(
            "Figure 6.7 is eight pairs of arrows. Compare the boxes left "
            "with right. Bearish divergence and bullish confirmation are "
            "read the same way on both kinds. The two differ in bullish "
            "divergence, where price falls and a non-price-based oscillator "
            "falls with it but a price-based one rises, and in bearish "
            "confirmation, where price falls and a non-price-based "
            "oscillator rises but a price-based one falls. In short, a "
            "price-based oscillator diverges by moving against price, and "
            "plain volume by falling. That one-line summary is ours."
        )),
        figure("6.8", "Both kinds read on the Currency Shares Euro Trust.",
               height_mm=70.0),
        Para(text=(
            "Figure 6.8 reads one rise both ways. The volume with its "
            "smoothed line and the detrended PVO, both non-price-based, "
            "show bearish divergence. The ADL, price-based, shows bullish "
            "confirmation. Each kind is read by its own rule; the book does "
            "not say which to believe."
        )),
    ),
)

# ==========================================================================
# Section 2 - timing, the VWMA and climaxes (the book's 6.1, pp.180 to 186)
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Timing, the VWMA and Climaxes",
    standfirst="Why minimum volume times a breakout or a reversal, the "
               "volume-weighted moving average and its two readings, the "
               "four kinds of top and bottom, where to set an "
               "overextension level, and how the timeframe changes what "
               "volume shows. The book's section 6.1, pages 180 to 186.",
    blocks=(
        Head(number="2.1", text="Volume as a timing indicator"),
        Para(text=(
            "Inside a consolidation, whenever volume declines close to its "
            "lowest historical level, a breakout is expected. The book's "
            "reason is that by then most buyers who wanted to buy have "
            "bought and most sellers who wanted to sell have sold. Stop "
            "orders, taught in Chapters 1 and 5, accumulate above and below "
            "the range over the consolidation, and once triggered they are "
            "the catalyst for the breakout, up or down. Breakout here is "
            "the use of Chapters 2 and 4: price leaving a range."
            "\n\n"
            "This answers the novice error of Section 1. **There is no "
            "divergence reading during a consolidation, because price is "
            "moving sideways.** Falling volume inside a range is not "
            "weakness; it is the clock running down to the breakout."
        )),
        chart("J", "A range, its stops, and volume falling to its lowest "
                   "level."),
        Para(text=(
            "In Chart J find the box, the range, with buy stops drawn above "
            "it and sell stops below. Then follow the volume panel to "
            "point 1, where volume tests its lowest level, and up to point "
            "2, where price breaks out of the top of the box and volume "
            "surges. Where the stops sit is our drawing of the book's "
            "sentence."
        )),
        formal("Low volume breakout signal"),
        figure("6.9", "Volume as a reversal and breakout timing indicator "
                      "on Apple.", height_mm=74.0),
        Para(text=(
            "Figure 6.9 is a daily Apple chart. Find the box at the bottom "
            "right of the price panel, an accumulation, and the circle "
            "under it where volume sits on its low volume level: price "
            "then breaks out of the box. The same figure also shows two "
            "turns on low volume, at time lines 1 and 2, before the "
            "consolidation."
            "\n\n"
            "Those turns are the second use of minimum volume. The book "
            "says there is a tendency for price to reverse when volume is "
            "at its minimum or lowest historical levels."
        )),
        formal("Low volume reversal"),
        chart("K", "A low volume reversal at a peak and at a trough."),
        Para(text=(
            "Chart K draws it on one invented line. At 1 price peaks and at "
            "2 it bottoms, and at both the volume bar under the turn "
            "touches the dashed low volume level. The book gives no rule "
            "for where that level goes; Figure 6.9 draws it by eye, and so "
            "does the chart."
        )),
        figure("6.10", "Three breakouts at minimum volume in silver."),
        Para(text=(
            "Figure 6.10 shows the breakout signal three times on the "
            "iShares Silver Trust: one accumulation breakout up and two "
            "distribution breakouts down, at bars 1, 2 and 3, each as volume "
            "tests the threshold. Notice that the breakout bars themselves "
            "carry more volume than the bars before them: volume falls "
            "into the breakout and surges on it."
        )),

        Head(number="2.2", text="The volume-weighted moving average"),
        Para(text=(
            "The book introduces a volume-weighted moving average, VWMA, "
            "as a line of average price on the chart, weighted by volume as "
            "its name says. It defers the calculation to its Chapter 11, "
            "and moving averages themselves, met in Chapters 4 and 5, are "
            "taught there. For now the line matters by which side of it "
            "price is on: a share at 52 pesos above a VWMA at 50 is "
            "potentially bullish, and at 48, below it, potentially bearish."
        )),
        formal("Volume-weighted moving average, VWMA"),
        chart("L", "A price and its 10-bar VWMA, with two crossings."),
        Para(text=(
            "Chart L draws an invented price and a 10-bar VWMA we computed. "
            "Find the two labelled crossings: below the line, potentially "
            "bearish; above it, potentially bullish."
        )),
        figure("6.11", "The VWMA on the S&P 500 SPDR."),
        Para(text=(
            "Figure 6.11 shows price rising decisively every time it "
            "crosses above the line and declining when it crosses below. "
            "Follow the dashed arrows from the circled volume peaks to the "
            "crossovers: the book notes that the crossovers occur at the "
            "daily volume cycle peaks, which Section 5 explains. The figure "
            "also marks the line acting as support and as resistance. Its "
            "caption says VWMA on a daily chart; the figure itself is "
            "labelled VWAP and is a 10-minute chart."
            "\n\n"
            "A paragraph later the book reads the same line a second way. "
            "A stock below the VWMA is undervalued and above it "
            "overvalued, so many institutional traders look for buy "
            "signals only when it is below and sell signals only when it is "
            "above. **So above the line is potentially bullish and also "
            "where institutions look to sell; the book gives both readings "
            "and does not reconcile them.**"
        )),
        chart("M", "Undervalued below the line, overvalued above it."),
        Para(text=(
            "Chart M shades one stretch below the VWMA, undervalued, where "
            "institutions look to buy, and one above it, overvalued, where "
            "they look to sell."
        )),
        SelfCheck(text=(
            "Volume in a range has fallen to its lowest level in a year. "
            "What does the book expect next, and can it tell you which way?"
        )),

        Head(number="2.3", text="Climaxes, and the overextended levels"),
        Para(text=(
            "A market top or bottom is usually accompanied by relatively "
            "large or extreme volume, or by relatively low or minimal "
            "volume. That gives four cases. A top on extreme volume is a "
            "blow-off or buying climax, and a bottom on extreme volume a "
            "sell-off or selling climax. Chapter 4 named the climaxes that "
            "end a trend by who buys and who sells in them; Chapter 6 adds "
            "their extreme volume. A top on extremely low volume is a low "
            "volume top, and a bottom on it a low volume bottom."
        )),
        chart("N", "Four turns, named by place and by volume."),
        Para(text=(
            "Chart N sketches the four. In each, the green bar is the "
            "volume on the day of the turn: towering in the top row, the "
            "climaxes, and the smallest of all in the bottom row."
            "\n\n"
            "To use extreme volume as a signal, the book draws a line "
            "across the volume panel at the height that only extreme volume "
            "reaches. A lower line catches smaller turns."
        )),
        formal("Upper and lower overextended volume levels"),
        figure("6.12", "Selling climaxes at the upper overextended level, "
                       "Exxon Mobil."),
        Para(text=(
            "Figure 6.12 is the daily chart of Exxon Mobil, which the book "
            "spells Exxon Mobile. Look at the ellipse around the market "
            "bottom and follow its arrows down to two volume spikes, both "
            "of which reach the upper line: two selling climaxes."
        )),
        figure("6.13", "Blow-offs on the E-TRACS CMCI Food ETN."),
        Para(text=(
            "Figure 6.13 is the mirror case: a couple of blow-offs, or "
            "buying climaxes, at relatively high volume. Follow each "
            "BLOW-OFF arrow to its circled spike and up to its top."
        )),
        figure("6.14", "Volume overextensions in the SPDR Gold Trust."),
        Para(text=(
            "Where should the line go? The book's answer is by visual "
            "inspection, at a level where only the most significant tops "
            "or bottoms are found. **Set lower, it signals more often, and "
            "the tops and bottoms it signals are less significant.** In "
            "Figure 6.14 the overextended spikes are all above the rolling "
            "100-day 2-sigma level, a computed line that Section 3 builds, "
            "and at the right price breaks a significant support on extreme "
            "volume."
        )),
        chart("O", "A higher and a lower overextension level on one chart."),
        Para(text=(
            "Chart O draws both lines on one invented chart. Only the "
            "spikes at the two major turns, numbered 1 and 2, reach the "
            "upper line. Three more, at smaller corrections lettered a to "
            "c, reach only the lower one. Both lines are drawn by eye."
        )),
        figure("6.15", "Volatility spikes at the same turns in silver."),
        Para(text=(
            "Figure 6.15 adds a second kind of evidence. A Bollinger "
            "Bandwidth oscillator times volatility in silver, and its "
            "spikes coincide with the volume overextensions at the top, 1, "
            "and the bottom, 2. Many practitioners filter out volatility "
            "below a threshold and regard it as noise. The Bollinger Band "
            "and its Bandwidth are named and not explained in this chapter."
        )),

        Head(number="2.4", text="Low volume tops and bottoms"),
        Para(text=(
            "Tops and bottoms can also form on very little volume. These "
            "are the low volume reversals of Section 2.1, now named by "
            "where they turn."
        )),
        formal("Low volume top and low volume bottom"),
        figure("6.16", "Low volume reversals on Apple."),
        Para(text=(
            "Figure 6.16 has nine time lines on a daily Apple chart, each "
            "rising from a circle where volume tests a lower volume "
            "threshold. Follow each line up to price: some are tops and "
            "some are bottoms."
        )),

        Head(number="2.5", text="Overbought or oversold only afterwards"),
        Para(text=(
            "Extreme buying and extreme selling both generate volume, so an "
            "overextension in volume can signal either a top or a bottom. "
            "That is why the book will not call a volume extreme overbought "
            "or oversold until it can be tied to a top or a bottom. We can "
            "pinpoint the overextension when it happens, but the overbought "
            "or oversold reading comes only in retrospect. Overbought and "
            "oversold were met in Chapters 1 and 5 and are used here "
            "without a definition; oscillators are the book's Chapter 8."
        )),
        chart("P", "The same volume extreme after a rise and after a fall."),
        Para(text=(
            "In Chart P the two volume records are identical. Only what "
            "price did tells them apart: after a rise the spike was a top, "
            "overbought in retrospect; after a fall, a bottom, oversold in "
            "retrospect."
        )),

        Head(number="2.6", text="The timeframe changes what volume shows"),
        figure("6.17", "Gold's volume on five timeframes.", height_mm=74.0),
        Para(text=(
            "Figure 6.17 shows the same gold volume on daily, weekly, "
            "monthly, quarterly and yearly panels. Daily and weekly volume "
            "peak in 2013; monthly and higher peak in 2011. **Lower "
            "timeframe charts are more sensitive to volume action, and at "
            "higher timeframes the overall trend or behavior of volume is "
            "more obvious.**"
        )),
        chart("Q", "One volume record by day and by month."),
        Para(text=(
            "Chart Q shows why. Its upper panel is 240 invented days, whose "
            "tallest bar is a single spike late in the record, at 1. Its "
            "lower panel is the same days added up month by month, and the "
            "busiest month, at 2, comes earlier: one day's spike is "
            "outweighed by the busy months around it."
        )),
        SelfCheck(text=(
            "A volume spike towers over everything around it. Why can you "
            "not call it overbought on the day it happens?"
        )),
    ),
)

# ==========================================================================
# Section 3 - price barriers and filtering (the book's 6.1, pp.187 to 190)
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Price Barriers and Filtering",
    standfirst="What volume says about the strength of a support or a "
               "resistance, the five kinds of volume action at a barrier, "
               "the four ways to filter volume, and trendlines and "
               "channels drawn only from heavily traded points. The book's "
               "section 6.1, pages 187 to 190.",
    blocks=(
        Head(number="3.1", text="Volume and the strength of a barrier"),
        Para(text=(
            "Chapter 5 called a support below price or a resistance above "
            "it a barrier. The book now asks which barriers to trust. "
            "**Support and resistance formed at a volume peak are regarded "
            "as the most reliable and the strongest barrier to future "
            "retests.** The reason it gives: even with the surge in "
            "volume, price could not get through, which gives traders "
            "confidence that the barrier will hold, and since expectation "
            "is everything in the market, that confidence goes a long way. "
            "A barrier formed across a volume dip or trough is less "
            "reliable: it held only because nobody was interested in "
            "taking price through it."
        )),
        figure("6.18", "Which price barrier is more reliable?"),
        Para(text=(
            "Figure 6.18 poses the question in four sketches. Resistance 1 "
            "and Support 1 are touched as volume peaks and are the more "
            "reliable; Resistance 2 and Support 2 are touched as volume "
            "dips."
        )),
        Points(
            title="The five kinds of volume action at a barrier",
            numbered=True,
            items=(
                "Volume increasing across support or resistance.",
                "Volume decreasing across support or resistance.",
                "Volume peaking at support or resistance.",
                "Volume bottoming at support or resistance.",
                "Volume flatlining across support or resistance.",
            ),
        ),
        figure("6.19", "The five kinds at a resistance and at a support."),
        Para(text=(
            "Figure 6.19 draws all five at a resistance, top row, and at a "
            "support, bottom row. Increasing or decreasing volume across a "
            "barrier signifies a change in sentiment there. With increasing "
            "volume, volume picks up as price reverses at the barrier and "
            "drives price away from it with bullish or bearish "
            "confirmation. With decreasing volume, there seems too little "
            "force to drive price through, and volume falls further as "
            "price reverses. **Decreasing volume across a barrier tends to "
            "see a retest, and in more extreme circumstances price may "
            "return to penetrate it.** Peaking is the most reliable case "
            "and bottoming the less reliable, as above, and flatlining "
            "volume does not give enough information."
        )),
        chart("R", "What each of the five tells, at a support."),
        Para(text=(
            "Chart R sketches the five at a support, with the book's "
            "outcome written under each name. Read each case as what "
            "volume does, then what price does next: in the decreasing "
            "case, price drifts back down for a retest."
        )),
        SelfCheck(text=(
            "Two supports have held. One held on the heaviest volume of "
            "the month, the other on the lightest. Which would the book "
            "trust more on a retest, and why?"
        )),

        Head(number="3.2", text="Four ways to filter volume"),
        Para(text=(
            "Filtering picks out the most significant volume action. The "
            "book lists four ways: a moving average filter, a volatility "
            "filter, prior volume peaks and volume cycles. Prior volume "
            "peaks are the overextended levels of Section 2, and volume "
            "cycles come in Section 5. This is review question 5."
        )),
        chart("S", "One sketch of each of the four filters."),
        Para(text=(
            "Chart S sketches each filter on invented volume, with the "
            "volume each picks out in gold: spikes above a moving average, "
            "the largest bar above a higher band, a bar that reaches the "
            "level of an earlier peak, and peaks that repeat in a cycle."
            "\n\n"
            "The first is a moving average of volume, a line of the "
            "average of recent volume drawn over the volume bars, so that "
            "a spike well above it stands out."
        )),
        formal("Smoothed volume filter"),
        chart("T", "A 20-bar average of volume, and four spikes far above "
                   "it."),
        Para(text=(
            "In Chart T each point of the line is the average of the last "
            "20 volume bars, computed. Four spikes stand far above it, in "
            "gold, and the dashed lines numbered 1 to 4 run from each up to "
            "a top or a bottom in price. The book gives no measure of how "
            "far above the line a spike must be."
            "\n\n"
            "How long should the average be? The book says a simple "
            "backtest may be needed to find the lookback period right for "
            "a setup, and that some practitioners set it to the dominant "
            "trading cycle period, or half of it. A backtest, as Chapter 5 "
            "glossed it, runs a method against past prices, and the cycle "
            "period is the Chapter 5 term for how long each swing takes. "
            "The book gives no number."
        )),
        figure("6.20", "A smoothed volume filter on USDJPY."),
        Para(text=(
            "Figure 6.20 draws the smoothed volume line, labelled moving "
            "average overextension threshold, across the volume panel of "
            "daily USDJPY. Follow the dotted arrows from the overextensions "
            "in volume up to tops and bottoms in price."
            "\n\n"
            "The second is the volatility filter. Sigma is the Greek letter "
            "for a standard deviation, which Chapter 5 glossed as how far "
            "values typically spread from their average. A line two or "
            "three standard deviations above average volume lets only the "
            "biggest surges through. The book builds it from a Bollinger "
            "Band, which Chapter 5 named and this chapter does not explain; "
            "only the band's upper line is needed."
        )),
        formal("Two- or three-sigma volume filter"),
        chart("U", "A 20-bar average of volume and a three-sigma line "
                   "above it."),
        Para(text=(
            "Chart U draws both lines on invented volume: the 20-bar "
            "average, and above it the three-sigma line, the average plus "
            "three standard deviations of the same 20 bars. Only three bars "
            "cross the upper line, in gold. A three-sigma line is stricter "
            "than a two-sigma one, so fewer bars cross it."
        )),
        figure("6.21", "A three-sigma volume filter on USDJPY."),
        Para(text=(
            "Figure 6.21 is the same USDJPY chart with a three-sigma "
            "threshold: there are fewer arrows than in Figure 6.20, at the "
            "most significant tops and bottoms. The book notes that a "
            "standard deviation oscillator could be used instead, but it "
            "is less useful, because it gives no overlay on which volume "
            "can be seen crossing the threshold."
        )),

        Head(number="3.3", text="Volume filtered inflection points"),
        Para(text=(
            "Chapter 5 taught inflection points, a peak or a trough, and "
            "drew trendlines and channels through them. Many practitioners "
            "use volume to choose which inflection points to draw through: "
            "only those that came with heavy volume."
        )),
        formal("Volume filtered inflection points"),
        chart("V", "A channel drawn only through heavily traded turns."),
        Para(text=(
            "In Chart V six turns came on light volume and are greyed out. "
            "Three came on volume above the threshold and are numbered 1, "
            "2 and 3. The solid line joins 1 and 2, and the dashed line is "
            "its parallel through 3: a channel built only from significant "
            "points."
        )),
        figure("6.22", "A channel from tick volume filtered points in "
                       "silver."),
        Para(text=(
            "Figure 6.22 uses tick volume, a count of trades defined in "
            "Section 4, with a threshold drawn by visual inspection so that "
            "only the most significant peaks reach it. Points 1, 2 and 3 "
            "came with overextended tick volume. A trendline is drawn from "
            "1 to 2 and a parallel from 3, and at X price reacts to the "
            "channel, a short-term buying opportunity, before the market "
            "turned down through it."
        )),
        figure("6.23", "Further channels from filtered points in silver."),
        Para(text=(
            "Figure 6.23 builds more channels on the same chart. A "
            "parallel from 3 is breached by a large bearish candlestick; a "
            "parallel from 4, taken back in time, meets the trough at X, "
            "which the book admits was found in retrospect but still calls "
            "a valid rising channel; parallels from 5 and 6 contain price "
            "as resistance and support. The book calls it near perfect "
            "angular symmetry, a Chapter 5 term. Its text calls Figure 6.23 "
            "the same daily chart of USDJPY and then the Silver market; "
            "both captions and charts say silver."
        )),
    ),
)

# ==========================================================================
# Section 4 - relative volume, open interest and breadth (pp.190 to 197)
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Relative Volume, Open Interest and Breadth",
    standfirst="Relative against absolute volume, why bull markets trade "
               "more, open interest and how it is read, tick volume, the "
               "TRIN, and volume by price against volume by time. The "
               "book's section 6.1, pages 190 to 197.",
    blocks=(
        Head(number="4.1", text="Relative and absolute volume"),
        Para(text=(
            "**Absolute volume is not as important as relative volume: it "
            "is the change in volume that gives the most information.** "
            "Rising and declining volume show the interest at various "
            "prices and whether a trend is bullish or bearish, and "
            "historical peaks and troughs in volume, the overextensions, "
            "give a reference level for future tops and bottoms. This is "
            "review question 7."
            "\n\n"
            "The book adds a caution: a change in volume is not an "
            "absolute requirement for a trend to develop. A trend can "
            "persist for long periods on flat volume."
        )),
        chart("W", "A trend that persists on flat volume."),
        Para(text=(
            "Chart W is that caution drawn: an invented share rising for "
            "the whole chart while every volume bar stays about the same "
            "height."
            "\n\n"
            "Relative volume also shows a difference between bull and bear "
            "markets, and the first of the book's reasons for it is a name "
            "of its own. Bought at 50 pesos and now at 38, a holder may "
            "keep the share, waiting for 50 again, rather than sell at a "
            "loss."
        )),
        formal("Loss aversion bias"),
        chart("X", "A holder waiting for breakeven while volume shrinks."),
        Para(text=(
            "In Chart X the dashed gold line is the 50 peso entry. Follow "
            "the price down to 38 and the volume under the fall shrinking: "
            "holders who will not sell add no volume. Chapter 1 listed loss "
            "aversion among the behavioral biases in one line; this is "
            "where it is explained."
        )),
        Points(
            title="Why bull market volume outweighs bear market volume",
            items=(
                "Loss aversion: holding on to losing positions in a falling "
                "market does not contribute to its trading.",
                "In a rising market, investors and traders can use house "
                "money, their profit, to fund new positions.",
                "More investment funds market their services in a bull "
                "market, drawing more investors in.",
            ),
        ),
        chart("Y", "Bull market volume against bear market volume."),
        Para(text=(
            "Chart Y shows only the result: the volume bars under the rise "
            "are taller than those under the fall. The book says these are "
            "a few of a variety of reasons."
            "\n\n"
            "Absolute volume has its own uses. It helps find potential "
            "price rejection levels, a Chapter 3 term, at significant or "
            "historical prices. It compares participation across stocks, "
            "sectors, industries or commodities in search of greater "
            "liquidity, the book's word, not defined here. And total "
            "turnover against the shares outstanding gives the absolute "
            "level of participation in a stock."
        )),
        chart("Z", "Turnover: two invented shares compared."),
        Para(text=(
            "Chart Z works turnover for two invented shares. Share A trades "
            "5 million a day of 2,000 million outstanding, 0.25 percent. "
            "Share B trades 1 million of 40 million, 2.5 percent. A trades "
            "more shares; B has ten times the participation."
            "\n\n"
            "Finally, volume distortions. A surge in arbitrage, program "
            "trading and high frequency trading may distort the "
            "traditional meaning of volume, so the volume traders read may "
            "not be totally indicative of true volume action in the "
            "classical sense. Chapter 1 named all three; the book explains "
            "none of them here and gives no remedy."
        )),

        Head(number="4.2", text="Open interest"),
        Para(text=(
            "Chapter 3 listed open interest as transaction data and Chapter "
            "4 used it in a consolidation; this is where it is defined. "
            "Unlike stocks, all futures and options contracts eventually "
            "expire, and each contract is one long position and one short "
            "position. A contract stays open until both sides are out. "
            "Suppose A buys one contract from B, both new: open interest "
            "is 1. C buys two from D, both new: 3. A sells his to a new "
            "buyer, E: still 3, because one side was replaced. D buys two "
            "back from C, both leaving: 1."
        )),
        formal("Open interest"),
        chart("AA", "Open interest over four days."),
        Para(text=(
            "Chart AA draws those four days as columns of 1, 3, 3 and 1 "
            "contracts, each labelled with what moved it. Only both sides "
            "arriving together, or both leaving together, changes the "
            "count."
            "\n\n"
            "Generally, open interest is interpreted the same way as "
            "volume: it shows the level of interest in seeing price rise "
            "or fall, and its divergence is read the same way as for "
            "non-price-based volume oscillators."
        )),
        Points(
            title="Price, volume and open interest together",
            items=(
                "Price, volume and open interest all rising: bullish, "
                "predominantly driven by buying pressure.",
                "Price rising while volume and open interest decline: "
                "bearish, driven by shorts covering and longs leaving.",
                "Price falling while volume and open interest rise: "
                "bearish, driven by short selling.",
                "All three falling: bullish, as fewer longs are liquidated "
                "and fewer shorts initiated; participants are less "
                "interested in seeing the market decline further.",
            ),
        ),
        chart("AB", "The four cases as arrows."),
        Para(text=(
            "Chart AB draws each case as three arrows, price in gold. The "
            "rule is Section 1's with open interest alongside volume: with "
            "price, bullish; against it, bearish. This is review question "
            "6."
            "\n\n"
            "The trader's actions follow from the four. With price, open "
            "interest and volume all rising, look for buy signals. With "
            "rising prices on declining open interest and volume, look to "
            "exit and liquidate longs. In a declining market with open "
            "interest and volume rising, look to go short, and rapidly "
            "cover all shorts when both start to decline together. Going "
            "long, liquidating, going short and covering are Chapter 1 "
            "terms."
        )),
        figure("6.24", "Open interest diverging from silver's rise.",
               height_mm=74.0),
        Para(text=(
            "Figure 6.24 is silver rising from A to B. Volume peaks with "
            "the price at 1, bullish confirmation, but open interest makes "
            "a lower peak at 2, bearish divergence: many longs are "
            "liquidating as prices rise. Silver then retraced "
            "significantly."
        )),
        chart("AC", "High open interest and a rapid reversal, low and a "
                    "gradual one."),
        Para(text=(
            "The level of open interest may also indicate the nature of a "
            "reversal or breakout. If it is very high, the reversal may be "
            "significantly more rapid, because of the large number of open "
            "contracts liquidating and covering. Chart AC sketches the two "
            "on one scale: the fall after a top on very high open interest "
            "is steep, and on low open interest gradual. May, says the "
            "book: a tendency."
        )),
        SelfCheck(text=(
            "A trader holding a long futures contract sells it to a "
            "newcomer who takes over the long. What happens to open "
            "interest, and why?"
        )),

        Head(number="4.3", text="Tick volume"),
        Para(text=(
            "Chapter 1 met tick volume in a caption, as transactions "
            "counted regardless of size, and Chapter 3's tick chart drew a "
            "new bar after a set number of trades. The book now defines "
            "it. One tick is one trade, and one trade may be 1 contract or "
            "1,000. In the over the counter, OTC, foreign exchange market "
            "many brokers offer tick volume instead of actual volume. The "
            "five trades of Section 1.3 give a volume of 2.4 million shares "
            "and a tick volume of 5. This is review question 1."
        )),
        formal("Tick volume"),
        chart("AD", "The same five trades counted by size and by number."),
        Para(text=(
            "Chart AD counts the five trades both ways: by size, columns "
            "of 0.1 to 1.2 million adding to 2.4 million shares; by number, "
            "five equal ticks adding to 5. The book says tick volume may "
            "serve as a proxy for actual volume as far as comparing "
            "relative levels of overbought and oversold goes."
        )),

        Head(number="4.4", text="Breadth volume and the TRIN"),
        Para(text=(
            "The Arms Index, or TRIN, sets breadth against volume. "
            "Advances and declines were listed as breadth data in Chapter "
            "3 and never defined; read them here as the number of stocks "
            "rising and falling, and up volume and down volume as the "
            "volume in each. That reading of the names is ours. With 1,500 "
            "advances and 1,000 declines the first ratio is 1.5; with up "
            "volume of 600 million and down volume of 800 million the "
            "second is 0.75; the TRIN is 1.5 divided by 0.75, which is 2.0."
        )),
        formal("The Arms Index, or TRIN"),
        chart("AE", "The TRIN worked as arithmetic."),
        Para(text=(
            "Chart AE sets the sum out in three columns: advances over "
            "declines, up volume over down volume, and the first divided by "
            "the second."
            "\n\n"
            "The book reads the TRIN together with a second indicator it "
            "calls the tick, and never says what that tick measures; it is "
            "not shown to be the tick volume above. Its short-term rule: a "
            "rising but not overbought tick with a falling but not oversold "
            "TRIN is bullish, and the converse bearish. Its longer-term "
            "rule: a tick that is oversold, above its two-sigma level on a "
            "weekly chart, with a TRIN that is overbought, near or above "
            "3.0 on the daily chart, is bullish, and the converse bearish."
        )),
        figure("6.25", "The tick and the TRIN both oversold on the S&P 500."),
        Para(text=(
            "Figure 6.25 is a 1-minute chart of the S&P 500 index, though "
            "its caption says daily. The box marks the tick and the TRIN "
            "both at oversold levels, and the index rose. **Here the book "
            "says two things: its text calls a bullish TRIN overbought, and "
            "its figure calls its bullish TRIN reading oversold.** Both "
            "readings are bullish; the word differs. Overbought and "
            "oversold are used without a definition, as in Section 2."
        )),
        figure("6.26", "A bearish rising TRIN on the S&P 500."),
        Para(text=(
            "Figure 6.26 shows a short-term downtrend in the S&P 500 with a "
            "bearish rising TRIN, boxed, and a tick largely absent of "
            "activity between 1:45 p.m. and 2:45 p.m. Together, the book "
            "calls it a short-term bearish signal. The figure also labels "
            "balanced tick action as a potential consolidation, which the "
            "text does not discuss."
        )),

        Head(number="4.5", text="Volume by price and volume by time"),
        Para(text=(
            "Volume may be analyzed two dimensionally. The usual volume "
            "bars, one a period, are volume by time. Volume by price adds "
            "up all the volume traded at each price level and draws it as "
            "bars running sideways from the price axis. If a share trades 9 "
            "million shares between 48 and 50 pesos in three months and 2 "
            "million between 54 and 56, its longest sideways bar is at 48 "
            "to 50."
        )),
        formal("Volume by price and volume by time"),
        chart("AF", "Volume by price and volume by time on one chart."),
        Para(text=(
            "Chart AF draws both on one invented share. Each sideways bar "
            "is the volume of every day that closed in its two-peso band; "
            "the bars under the chart are one a day."
            "\n\n"
            "Chapter 4's Figure 4.19 showed the same thing and called it "
            "price-based volume. That is this chapter's volume by price, "
            "and not the price-based volume oscillators of Section 1, which "
            "build price into a line."
        )),
        figure("6.27", "Volume by price marking support in silver."),
        Para(text=(
            "Figure 6.27 shows a large volume turnover around the $17 level "
            "in the iShares Silver Trust: find the longest sideways bars "
            "and then price returning to that level. That $17 is a "
            "significant support, and this is not obvious from "
            "conventional volume bar action."
        )),
        Points(
            title="The book's four steps to support and resistance",
            numbered=True,
            items=(
                "Locate the largest volume by price range.",
                "Locate the largest volume by time intervals.",
                "Find the area where the two intersect.",
                "The closest peak or peaks above that area is potentially "
                "the most significant resistance; the closest trough or "
                "troughs below it, the most significant support.",
            ),
        ),
        figure("6.28", "The most traded range on 3M."),
        Para(text=(
            "Figure 6.28 brackets a lot of volume turnover between $77 and "
            "$86 on the daily chart of 3M, the most traded range, with some "
            "resistance at $90 to $92. These price ranges are potential "
            "future support and resistance levels, and the four steps above "
            "pin the most significant of them down."
        )),
        chart("AG", "The four steps, numbered on one invented chart."),
        Para(text=(
            "Chart AG numbers the steps on the chart in the book's order. "
            "Step 1 is the gold band, the largest volume by price. Step 2 "
            "is the two shaded stretches, the busiest days. Step 3 is the "
            "two small gold boxes where they cross. Step 4 is the two "
            "lines: resistance at the nearest peak above the boxes and "
            "support at the nearest trough below."
        )),
        figure("6.29", "The four steps on 3M."),
        Para(text=(
            "Figure 6.29 does the same on 3M: the $74 to $80 band is the "
            "largest volume by price, the dark columns are the largest "
            "volume by time, the two white boxes are where they cross, and "
            "the dashed arrows mark the closest resistance above and "
            "support below. Both acted as effective barriers to price."
        )),
        SelfCheck(text=(
            "Advances 1,200, declines 800, up volume 900 million, down "
            "volume 600 million. Work out the TRIN."
        )),
    ),
)

# ==========================================================================
# Section 5 - bar range, volume cycles and non-constant time (pp.197-202)
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="Bar Range, Volume Cycles and Non-Constant Time",
    standfirst="The four named bars of bar range against volume, the "
               "constant volume chart, whether volume leads price, the "
               "intraday volume cycle, and what a non-linear time axis does "
               "to a line. The book's section 6.1, pages 197 to 202.",
    blocks=(
        Head(number="5.1", text="Volume against bar range"),
        Para(text=(
            "Chapter 5's characteristic 15, volume spread action, set a "
            "bar's range against its volume four ways. The book's heading "
            "here says spread too, meaning bar range as in Chapter 5, and "
            "not Chapter 3's bid-ask spread. In this chapter the four cases "
            "forecast potential breakouts and reversals, and each bar gets "
            "a name."
        )),
        figure("6.30", "The four combinations of bar range and volume."),
        Para(text=(
            "Figure 6.30 is the book's whole picture of them: for each of "
            "four numbered cases, an empty box for the bar range above a "
            "black box for the volume. Narrow and wide, low and high, are "
            "against the trend's usual bars and volume; the book gives no "
            "number for either. Suppose a fast uptrend's usual bar is one "
            "peso on 2 million shares: a 20 centavo bar on 5 million "
            "shares is a narrow range on high volume."
        )),
        formal("Rest, reversal and continuation bars"),
        chart("AH", "The four named bars, each at the end of a short "
                    "uptrend."),
        Para(text=(
            "Chart AH ends each of four short uptrends in one of the named "
            "bars, boxed in gold, with its volume in gold beneath."
        )),
        Points(
            title="What each bar indicates",
            items=(
                "Low Volume Rest Bar: a lack of participation. In a strong "
                "and rapid trend, a potential reversal; in a weak to "
                "average trend, a point of rest.",
                "High Volume Reversal Bar: a strong potential for reversal. "
                "If the volume represented buying in an uptrend the range "
                "would be much wider, so sellers are attempting to take "
                "control. Bearish in an uptrend; the converse in a "
                "downtrend.",
                "Low Volume Reversal Bar: a large move on relatively low "
                "participation, a lack of interest. The longer the bar, the "
                "more bearish in an uptrend and bullish in a downtrend.",
                "High Volume Continuation Bar: a large move backed by very "
                "large participation, interest in seeing price continue. "
                "Bullish in an uptrend, bearish in a downtrend.",
            ),
        ),
        chart("AI", "The two reversal bars."),
        Para(text=(
            "Chart AI draws the two reversal bars: on the left a narrow bar "
            "on very heavy volume at the top, on the right a very long bar "
            "on light volume, and price falls after each. One is too little "
            "movement for the volume, the other too little volume for the "
            "movement. Chapter 5 called a large range on low volume only "
            "trend inhibiting; Chapter 6 calls it a reversal bar."
        )),
        chart("AJ", "The rest bar in two trends, and the continuation bar."),
        Para(text=(
            "Chart AJ draws the same rest bar in two trends. At the top of "
            "a strong, rapid rise price reverses after it; in a slow, "
            "average rise price rests and rises again. The third cell is "
            "the continuation bar, wide on high volume, after which the "
            "rise continues. **The rest bar depends on the trend it is in; "
            "the continuation bar does not.**"
        )),
        figure("6.31", "High volume reversal bars on a dollar fund."),
        Para(text=(
            "Figure 6.31 is the PowerShares DB U.S. Dollar Bullish Fund "
            "with two narrow range candlesticks on high volume at Points 1 "
            "and 2; price reverses rapidly after each. On the left it also "
            "shows a low volume breakout signal near the apex of a "
            "descending triangle in August, the point where the triangle's "
            "two lines meet, and a large volume surge on the breakout."
        )),
        figure("6.32", "A high volume reversal bar at a bottom."),
        Para(text=(
            "Figure 6.32 is the converse case: a narrow range candlestick "
            "on high volume at a low around the beginning of November, "
            "followed by a significant rebound."
        )),
        figure("6.33", "A reversal bar within the larger downtrend."),
        Para(text=(
            "Figure 6.33 shows a high volume reversal bar around 23 May "
            "2011, after bearish divergence in volume and on the MACD, an "
            "oscillator Chapter 4 met and this chapter does not teach. "
            "**The book regards it as potentially more reliable because it "
            "formed within a larger downtrend.** At Point X there is a "
            "high volume continuation bar, and continuation bars too are "
            "more reliable in the direction of the predominant trend."
        )),
        figure("6.34", "A reversal bar at a historically overextended "
                       "volume level."),
        Para(text=(
            "Figure 6.34 shows a high volume reversal bar around the end "
            "of October 2011 whose volume reaches a historically "
            "overextended volume level drawn across the chart: two signals "
            "from this chapter agreeing at one bar."
        )),

        Head(number="5.2", text="Constant volume charts"),
        Para(text=(
            "Chapter 3 taught the constant volume chart, which draws a new "
            "bar each time a set volume has traded. Because every bar holds "
            "the same volume, a potential reversal bar can be found from "
            "the bar range alone and its height against the rest. A narrow "
            "bar there means a lot of volume for little movement; a very "
            "tall one, little volume for a lot."
        )),
        figure("6.35", "Reversal bars on a constant volume chart."),
        Para(text=(
            "Figure 6.35 sketches two rises on a constant volume chart, "
            "every volume bar the same height. On the left a narrow range "
            "bar on relatively high volume is bearish, sellers taking "
            "control; on the right a very tall bar on relatively low volume "
            "shows a lack of interest in the rise."
        )),

        Head(number="5.3", text="Does volume lead price?"),
        Para(text=(
            "Most practitioners agree that without participation, volume, "
            "price cannot move in a significant manner. Yet technical buy "
            "and sell signals need not have much volume to appear. A small "
            "breakout of a very significant trendline may set off a larger "
            "breakout, inviting tremendous volume as the penetration "
            "becomes obvious; then price leads volume. The book adds that "
            "with technical analysis so widely used, price may lead volume "
            "more often. Breakout here is Chapter 5's use of the word: "
            "price getting through a level, here a trendline."
        )),
        chart("AK", "Price breaks the line first, the volume comes after."),
        Para(text=(
            "In Chart AK price breaks a falling trendline by a little at 1, "
            "on ordinary volume. Only at 2, as the breakout becomes "
            "obvious, does volume surge."
        )),

        Head(number="5.4", text="The intraday volume cycle"),
        Para(text=(
            "Volume also rises and falls on a daily rhythm, which the book "
            "uses to anticipate price. Its examples are EURUSD, and the "
            "peak it gives, 1:30 p.m. to 2:30 p.m. GMT, is 9:30 p.m. to "
            "10:30 p.m. in Manila. The book does not say the hour holds for "
            "every market. This is review question 8."
        )),
        formal("Intraday volume cycle"),
        chart("AL", "Three days of hourly bars and their volume cycle."),
        Para(text=(
            "Chart AL draws three invented days of hourly bars. Volume "
            "swells each day in the shaded peak hours; at the peaks, "
            "numbered 1 to 3, price reverses, continues and reverses again, "
            "and never stays where it was."
        )),
        figure("6.36", "Volume cycle peaks at support and resistance on "
                       "EURUSD."),
        Para(text=(
            "Figure 6.36 is a 30-minute EURUSD chart with its daily volume "
            "cycles along the bottom: almost every reversal comes at an "
            "intraday tick volume peak, which is especially useful when "
            "price retests a previous support or resistance. Many "
            "practitioners use a bidirectional, or straddle, entry at the "
            "peak, catching price whichever way it goes. Chapter 5 taught "
            "the bidirectional entry: a trade taken either way, depending "
            "on which way the breakout occurs."
        )),
        figure("6.37", "Trendline retests at volume cycle peaks on hourly "
                       "EURUSD."),
        Para(text=(
            "In Figure 6.37 price rebounds off trendline retests at Points "
            "1, 4 and 5, each during a tick volume cycle peak, with a "
            "cycle-tuned stochastic oscillator showing oversold conditions. "
            "At Points 2 and 3 the trendline failed, and there the "
            "stochastic showed no clear oversold condition, at X and Y. "
            "The cycle-tuned stochastic was named in Chapter 5; oscillators "
            "are the book's Chapter 8."
        )),

        Head(number="5.5", text="Volume on non-constant time charts"),
        Para(text=(
            "Point and figure, Renko and three line break charts, all "
            "Chapter 3 terms, do not plot the time axis in a linear "
            "fashion, and that changes the angle of trendlines, channels "
            "and chart patterns drawn on them. The equivolume chart, also "
            "Chapter 3, is unique: each bar is a constant time interval, "
            "but its width varies with volume, so its time axis is "
            "non-linear too."
        )),
        figure("6.38", "One trendline violated at different points on a "
                       "standard and an equivolume chart.", height_mm=74.0),
        Para(text=(
            "Figure 6.38 draws the same rising trendline on a standard "
            "daily Apple chart and on an equivolume chart of the same "
            "months. Compare the two circles: the line is violated at "
            "different places, because wide bars on heavy days stretch the "
            "equivolume chart's time axis."
        )),
        SelfCheck(text=(
            "In an uptrend a bar prints a very narrow range on the heaviest "
            "volume of the month. Which named bar is it, and what does the "
            "book read from it?"
        )),
    ),
)

# ==========================================================================
# Section 6 - volume oscillators (the book's 6.2, pp.203 to 208)
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Volume Oscillators",
    standfirst="The book's eight volume oscillators and the eight methods "
               "of reading them, the On Balance Volume and its weakness, "
               "the Accumulation Distribution Line, the two Chaikin "
               "indicators, the NYSE Up/Down Volume, the Herrick Payoff "
               "Index and the COT report. The book's section 6.2, pages "
               "203 to 208.",
    blocks=(
        Head(number="6.1", text="Eight oscillators, eight methods"),
        Para(text=(
            "The book lists eight popular volume oscillators: the VWMA of "
            "Section 2, the Accumulation Distribution Line (ADL), On "
            "Balance Volume (OBV), the Chaikin Money Flow, the Chaikin "
            "Oscillator, the Demand Index, the Herrick Payoff Index and the "
            "NYSE Up/Down Volume Line. The Demand Index is never explained."
            "\n\n"
            "Each is read for bullish and bearish signals by eight standard "
            "methods of observation, which the book teaches in its Chapter "
            "8: OBOS overextended levels, OBOS being its short form for "
            "overbought and oversold; equilibrium and zero line crossovers; "
            "signal line crossovers; price-oscillator divergence; "
            "geometrically, numerically and horizontally based oscillator "
            "pattern analysis; and oscillator-on-oscillator analysis. Only "
            "divergence is used in this chapter."
        )),

        Head(number="6.2", text="On Balance Volume"),
        Para(text=(
            "The OBV is a running total of volume in which only the "
            "direction of the close matters. Take closes of 50.00, 50.50, "
            "50.20, 50.20, 50.80 and 50.60 pesos, with volumes after the "
            "first day of 2.0, 1.5, 1.0, 3.0 and 1.0 million shares. Day 2 "
            "closes up, so 2.0 is added; day 3 down, 1.5 subtracted; day 4 "
            "unchanged, nothing; day 5 up, 3.0 added; day 6 down, 1.0 "
            "subtracted. The OBV runs 0, 2.0, 0.5, 0.5, 3.5 and 2.5."
        )),
        formal("On Balance Volume, OBV"),
        chart("AM", "The OBV worked day by day."),
        Para(text=(
            "Chart AM lays the sum out in three panels: the closes, each "
            "day's volume signed by its close, and the running total."
            "\n\n"
            "The book names a disadvantage and a weakness. The "
            "disadvantage: the OBV's absolute value depends on the start "
            "date. Its relative changes do not, so all eight methods can "
            "still be used. The weakness: the whole of a period's volume is "
            "added or subtracted regardless of how the bar behaved. A bar "
            "that closes just below the previous close is subtracted in "
            "full, even if it made a new high far above the previous bar's "
            "high. To redress this, many practitioners prefer the ADL, the "
            "Chaikin Money Flow or the Chaikin Oscillator."
        )),
        chart("AN", "The start date, and a new high subtracted."),
        Para(text=(
            "Chart AN draws both. On the left, the same OBV started on two "
            "days: two lines of the same shape at different heights. On the "
            "right, the second bar makes a much higher high but closes a "
            "little lower, and its whole 3.0 million is taken away."
        )),
        figure("6.39", "OBV bullish divergence on Citigroup."),
        Para(text=(
            "Figure 6.39 shows Citigroup's price falling to a lower low "
            "while the OBV makes a higher low, bullish divergence; prices "
            "rebounded strongly. The OBV is price-based, so by Section 1's "
            "rule its bullish divergence is price falling while it rises."
        )),
        figure("6.40", "OBV bearish divergence on copper."),
        Para(text=(
            "Figure 6.40 is the mirror: copper's price rises twice while "
            "the OBV falls, bearish divergence, which reads the same on "
            "both kinds of oscillator. Prices fell strongly thereafter."
        )),

        Head(number="6.3", text="The Accumulation Distribution Line"),
        Para(text=(
            "The ADL also keeps a running total of volume, but each bar "
            "adds or subtracts only a share of its volume, set by where it "
            "closed in its range. C, H and L are the bar's close, high and "
            "low, from Chapter 1's OHLC. Take a bar with a high of 52 "
            "pesos and a low of 48, on 2 million shares. Closing at 52, its "
            "factor is 1 and it adds 2.0 million; at 50, the middle, the "
            "factor is 0 and it adds nothing; at 49 the factor is (1 minus "
            "3) over 4, minus one half, and it subtracts 1.0 million."
        )),
        formal("Accumulation Distribution Line, ADL"),
        chart("AO", "Three closes of one bar, worked through the ADL."),
        Para(text=(
            "Chart AO works those three closes: the bar and its factor, the "
            "factor times the volume, and the running total, 2.0, 2.0 and "
            "1.0 million. The name echoes the accumulation and "
            "distribution phases of Chapters 2 and 4; the book does not "
            "connect the two."
            "\n\n"
            "The algebra is the book's. If C minus L equals H minus C, "
            "then 2C equals H plus L and C is the midpoint, so a bar that "
            "closes at its midpoint adds nothing. The further above the "
            "midpoint it closes, the more volume is added, and the further "
            "below, the more subtracted. Putting the high in place of the "
            "close makes the factor exactly 1, so at most the day's total "
            "volume is added, never a multiple of it."
        )),
        chart("AP", "The ADL's multiplying factor from the low to the "
                    "high."),
        Para(text=(
            "Chart AP draws the factor as one straight line: minus 1 when "
            "the bar closes at its low, 0 at its midpoint, plus 1 at its "
            "high. **The ADL accounts for the current bar's price action, "
            "which the OBV does not.**"
        )),
        figure("6.41", "The ADL confirms while volume diverges on EURUSD."),
        Para(text=(
            "Figure 6.41 is hourly EURUSD. The ADL rises with price, "
            "bullish confirmation, while the volume bars fall, bearish "
            "divergence: an underlying weakness in the uptrend. The book "
            "does not pick one; it says the trader should wait for price "
            "to confirm a reversal before taking part."
        )),
        figure("6.42", "OBV and ADL together, trend and range, on Exxon "
                       "Mobil."),
        Para(text=(
            "Figure 6.42 reads the OBV and the ADL together. Where they "
            "rise or fall together, price trends decisively; where they "
            "move in opposite directions, price tends to range or "
            "consolidate. Compare the left ellipse, non-confirmation under "
            "an erratic price, with the right one, confirmation under a "
            "pronounced trend. The book says this helps gauge regime "
            "changes and decide between a trend-following and a "
            "range-bound strategy."
        )),

        Head(number="6.4", text="The Chaikin Money Flow and Oscillator"),
        Para(text=(
            "Both are built from the ADL's signed volume, S, the "
            "multiplying factor times the period's volume. N is a number "
            "of periods. Over three bars with signed volumes of 2.0, 0 and "
            "minus 0.5 million on volumes of 2.0, 1.0 and 1.0 million, the "
            "sum of S is 1.5 and the sum of volume 4.0, so the CMF is "
            "0.375. The book then says to keep a running total of the CMF, "
            "as for the ADL, and to take the Chaikin oscillator from it as "
            "a shorter-term EMA less a longer-term EMA. An EMA is an "
            "exponential moving average, taught in the book's Chapter 11, "
            "and the book gives no lengths for the two."
        )),
        formal("Chaikin Money Flow and Chaikin Oscillator"),
        chart("AQ", "The Chaikin Money Flow worked for three bars."),
        Para(text=(
            "Chart AQ sets the CMF out as three columns: the signed "
            "volumes and their sum, the volumes and their sum, and the one "
            "divided by the other."
        )),
        figure("6.43", "The Chaikin pair on copper."),
        Para(text=(
            "In Figure 6.43 the Chaikin oscillator gives an earlier sell, "
            "or bearish, signal than the CMF: follow the dashed arrows from "
            "each panel up to the top, and the oscillator's comes first. "
            "Oversold levels on both point to a potential bottom in copper "
            "around October 2011. The figure prints settings of 20 for the "
            "CMF and 3 and 10 for the oscillator; the text gives none."
        )),

        Head(number="6.5", text="The NYSE Up/Down Volume, the Herrick index "
                                "and the COT report"),
        Para(text=(
            "The NYSE Up/Down Volume sets the volume in the exchange's "
            "rising stocks against the volume in its falling ones. It is "
            "non-price-based, so its divergence is read like plain volume."
        )),
        formal("NYSE Up/Down Volume"),
        figure("6.44", "The NYSE Up/Down Volume line giving an early bearish "
                       "signal."),
        Para(text=(
            "In Figure 6.44 the volume line breaks its rising trendline "
            "first, an early bearish signal, and the NYSE Composite Index "
            "breaks its own line later, the price confirmation. **The book "
            "says two things here: its text calls the indicator a ratio, "
            "while its figure labels the line cumulative and the line runs "
            "below zero, which a ratio cannot.**"
            "\n\n"
            "The Herrick Payoff Index uses open interest in its "
            "calculations, so it can only be used with futures and "
            "options, which have open interest; a share on the PSE has "
            "none. It incorporates price, so its divergence is read as for "
            "any price-based volume oscillator. The book gives no formula "
            "and no figure for it."
        )),
        formal("Herrick Payoff Index"),
        Para(text=(
            "Last, the Commitment of Traders, COT, report, which says who "
            "holds the open positions behind a futures market's open "
            "interest. Hedgers were named among the market participants in "
            "Chapter 1. Traders and investors use the report to identify "
            "potential tops and bottoms, looking for changes in the net "
            "commercial or non-commercial open positions, and for a test of "
            "any significant or historical open interest level. The book "
            "does not define net."
        )),
        formal("Commitment of Traders, COT, report"),
        chart("AR", "Open interest testing its earlier historical peak."),
        Para(text=(
            "Chart AR draws the second of those uses: an invented futures "
            "price rising to a top while its open interest climbs back to "
            "the dashed line at its earlier peak, a test of a historical "
            "open interest level."
        )),
        SelfCheck(text=(
            "A bar closes exactly at the midpoint of its range on 4 million "
            "shares. What does it add to the OBV if its close is higher "
            "than yesterday's, and what does it add to the ADL?"
        )),
    ),
)

# ==========================================================================

NOTES = LectureNotes(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 6",
    title="Volume and Open Interest",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    term="First semester",
    source_note="Chapter scope follows Lim, M. (2016), The Handbook of "
                "Technical Analysis, chapter 6. Figures are reproduced from "
                "that text and remain the publisher's copyright. Charts "
                "are drawn for this course on invented prices.",
    orientation=(
        "These notes are the record of what Chapter 6 covered, written to "
        "be read on their own. If you were in the room, they are what to "
        "revise from. If you missed the session, they are the session. "
        "They follow the lecture in the same order. Sections 1 to 5 are "
        "the book's long section 6.1, in its own order, and Section 6 is "
        "its section 6.2; the book's 6.3, its summary, is the summary at "
        "the back."
        "\n\n"
        "The chapter reads volume, and then open interest, against price. "
        "Read it with the pictures beside you. A figure is the book's. A "
        "chart is one this course drew, on invented prices, where the book "
        "makes a point in words, in a sketch, or on a real chart too dense "
        "to read the point off. Every term is defined once, in the same "
        "words as the slides, and listed again at the back. The check "
        "yourself boxes are not assessed."
        "\n\n"
        "The chapter leans on tools a later chapter of the book teaches, "
        "oscillators above all, and in a few places it says two different "
        "things. Where that happens these notes say so rather than "
        "filling the gap from somewhere else. One of the book's six "
        "learning objectives, reading volume across successive contract "
        "months in futures, is not taught in this chapter's text; Chapter "
        "3 covered it."
    ),
    # The book's six learning objectives. The deck's objectives slide is
    # where they are maintained.
    objectives=tuple(CHAPTER.objectives),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6),
    # The summary and the review questions are the book's, and the deck's
    # closing slides are where they are maintained. build_lecture_notes6.py
    # reads them from there and fills these in, so editing the closing slide
    # moves the notes with it. Do not retype them here.
    summary=(),
    review_questions=(),
    sources=(
        "Lim, M. (2016). The Handbook of Technical Analysis. Wiley. "
        "Chapter 6, and the source of every figure here.",
    ),
)
