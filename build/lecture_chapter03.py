"""FIN1209 Chapter 3 student lecture notes, as plain data.

This is the file a contributor edits. Layout lives in build/lecturekit.py and
knows nothing about any chapter; the reasoning behind the layout, with the
research it came from, is chapter-01/lecture-notes-design.md.

    .venv/bin/python build/build_lecture_notes3.py

Written for a student reading alone, with no instructor in the room. Full
sentences that explain, not bullets that gesture. The six sections are the
deck's six parts in the deck's order, so a student can move between the two.

Nothing here is timing, cut tiers, speaker cues, check answers or slide
numbers. Those belong to the instructor and they live in
build/plan_chapter03.py.

Figure descriptions are never retyped here. The build takes them from
content_chapter03.py, which is also where the deck's own placeholder takes
them, so the two documents cannot describe the same figure differently.

The definitions are not retyped either. Every Define block below takes its
wording from the deck's own term slide through ``formal()``, so a term is
defined in the same words in both documents by construction rather than by
care. The plain words and the example belong in the paragraphs around it.
"""

from __future__ import annotations

import deckkit
from content_chapter03 import CHAPTER
from lecturekit import (Define, Fig, Head, LectureNotes, Panel, Para, Points,
                        Section, SelfCheck)

_FORMAL = {slide.term: slide.formal
           for part in CHAPTER.sections for slide in part.slides
           if isinstance(slide, deckkit.Term)}


def formal(term: str) -> Define:
    """The deck's own formal definition of ``term``, as a Define block."""
    return Define(term=term, text=_FORMAL[term])


# ==========================================================================
# Section 1 - From price to OHLC
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="From Price to OHLC",
    standfirst="What a chart is for and who reads one, the four families of "
               "data behind it, how a stream of trades becomes four prices, "
               "and why auto-scaling should be switched off.",
    blocks=(
        Head(number="1.1", text="What a chart is, and who reads one"),
        Para(text=(
            "Chapter 2 was a theory that kept only the closing price. This "
            "chapter builds the thing that theory is read from. The book "
            "describes traditional charting as a two dimensional matrix on "
            "which technical data is viewed."
        )),
        Para(text=(
            "A chart reveals repetitive price behaviour and market volatility, "
            "it shows up price distortions and illiquidity, and it is the "
            "surface on which trendlines, channels, envelopes and chart "
            "patterns are drawn."
            "\n\n"
            "Market data can be displayed as numbers or as a graph, and any "
            "numbers can be graphed. Quantitative analysts and statisticians "
            "work mainly with the numbers, using time series and stochastic "
            "analysis and back and forward testing, and for them a chart is "
            "optional. More traditional analysts prefer to work from the "
            "picture alone. **The book has a name for them.**"
        )),
        formal("Chartist"),
        Para(text=(
            "The picture a chartist works from is almost always the same shape:"
            " price up the side and time along the bottom. On a daily chart of "
            "a share, each step to the right is one more trading day and each "
            "step up is more pesos."
        )),
        formal("Price-time chart"),
        Para(text=(
            "One qualification about the time axis matters for the rest of the "
            "chapter. On some charts it is not plotted in equal units of time "
            "at all. **It acts instead as a counter for each new block of data,"
            " and on such charts time is regarded as implicit along the x "
            "axis.** Section 3 is full of charts that work this way."
        )),
        Points(
            title="The four families of technical data",
            items=(
                "**Price data**: open, high, low and close.",
                "**Transaction related data**: volume and open interest.",
                "**Market breadth data**: advances, declines, total issues, "
                "up and down volume, new highs and new lows, and bullish "
                "percent data.",
                "**Sentiment data**: the put/call ratio, the short interest "
                "ratio, the specialist/public ratio, the cash/asset ratio, "
                "investor and advisor poll data, margin debt, and implied "
                "volatility (VIX).",
            ),
        ),
        Para(text=(
            "The chapter lists all four families and then works only with the "
            "first two. **None of the breadth or sentiment items is defined in "
            "this chapter, and these notes do not define them either.** Where "
            "the book takes one up later, so will the course."
        )),
        SelfCheck(text=(
            "On a chart whose time axis is only a counter, has time stopped "
            "passing? If not, what exactly has changed?"
        )),

        Head(number="1.2", text="From a stream of trades to four prices"),
        Para(text=(
            "The majority of charts are simple price-time charts built from "
            "four prices per period, popularly called OHLC data. To make them, "
            "the continuous stream of trades is first cut into equal slices of "
            "time. Take one trading morning and cut it into five minute slices,"
            " 9:30 to 9:35, 9:35 to 9:40, and so on: each slice will become one"
            " bar."
        )),
        formal("Quantization of price"),
        Para(text=(
            "Quantize is the book's word, and filter is the word it uses beside"
            " it. Everything that happened inside the slice is then summarised "
            "as four numbers. Suppose that in one five minute slice a share "
            "opens at 50.00 pesos, trades up to 50.80, down to 49.60, and ends "
            "at 50.40. Its OHLC is 50.00, 50.80, 49.60 and 50.40, and every "
            "other trade in those five minutes has been thrown away."
        )),
        formal("OHLC data"),
        Fig(
            panels=(Panel(number="3.1"),), cols=1, height_mm=62.0,
            caption="One interval of price filtered into four prices and "
                    "drawn three ways.",
        ),
        Para(text=(
            "Figure 3.1 shows the filtering happen. On the left is the jagged "
            "price action inside one five minute interval; on the right are the"
            " same four prices drawn as a bar, as a Japanese candlestick and as"
            " a Gann bar. **The bar and the candlestick carry exactly the same "
            "information; only the drawing differs.** The chapter names Gann "
            "bars and draws one here, but never says how to read one, so "
            "nothing in this course is set on them."
            "\n\n"
            "Two more facts come with OHLC data. The range of a bar or "
            "candlestick is simply the absolute difference between its high and"
            " its low, range = |H - L|, so a bar with a high of 50.80 and a low"
            " of 49.60 has a range of 1.20 pesos. **And in most cases the "
            "closing price of one interval is also the opening price of the "
            "next, unless there is a gap in price.** Gaps are the second half "
            "of Section 2."
        )),

        Head(number="1.3", text="Long bars built from short ones"),
        Para(text=(
            "Once you have short bars, longer ones are built from them, not "
            "from the trades again. Take three five minute bars. The first "
            "opens at 50.00, the highest high of the three is 50.90, the lowest"
            " low is 49.40, and the third closes at 50.30. The fifteen minute "
            "bar they make is 50.00, 50.90, 49.40 and 50.30."
        )),
        formal("Higher timeframe bar"),
        Fig(
            panels=(Panel(number="3.2", label="Three intervals, one bar."),
                    Panel(number="3.3", label="Eight intervals, bar by bar.")),
            cols=2, height_mm=56.0,
            caption="A higher timeframe bar, and the quantization of a run "
                    "of intervals.",
        ),
        Para(text=(
            "Figure 3.2 builds one 15 minute bar and one 15 minute candlestick "
            "out of three five minute intervals: the open of the first, the "
            "close of the last, and the extreme high and low wherever they "
            "fell. Figure 3.3 does the quantization for eight successive "
            "intervals and draws each bar and each candlestick underneath the "
            "price that produced it. Pick two neighbours and you can watch the "
            "close of one become the open of the next."
            "\n\n"
            "**OHLC data is therefore simply a summary of price activity within"
            " an interval, and the longer the interval, the higher the "
            "timeframe of the bars it produces.** Nothing new is added by going"
            " to a higher timeframe; the same trading is only filtered more "
            "coarsely."
        )),
        Fig(
            panels=(Panel(number="3.4"),), cols=1, height_mm=52.0,
            caption="OHLC data as the basis of most chart constructions.",
        ),
        Para(text=(
            "Figure 3.4 is a family tree with OHLC data at the top. Almost "
            "every chart in this chapter hangs off it: line, bar, Japanese "
            "candlestick, point and figure, three line break and Renko. The one"
            " exception has its own branch. **The equivolume chart also needs "
            "volume, so the book says it requires OHLCV data, where V is "
            "volume.** Section 3 comes back to that claim, because the book "
            "says something slightly different about it later."
            "\n\n"
            "The tree also names Kagi charts and Gann swing charts. They appear"
            " there and nowhere else in the chapter, which never explains "
            "either one, so neither is examinable from Chapter 3."
        )),
        Fig(
            panels=(Panel(number="3.5"),), cols=1, height_mm=56.0,
            caption="Three representations of the same price flow.",
        ),
        Para(text=(
            "Figure 3.5 draws one sequence of OHLC data three ways, as a line "
            "chart, a bar chart and a candlestick chart. The line chart looks "
            "smoothest because it has thrown the most away, which Section 3 "
            "explains."
        )),

        Head(number="1.4", text="Switch auto-scaling off"),
        Para(text=(
            "Most charting software will, by default, stretch or squeeze the "
            "price axis so that whatever is on the screen fills it. Scroll a "
            "flat, quiet month into view and its bars suddenly look tall and "
            "wild; scroll a strong trend into the same window and those same "
            "bars shrink. **The bars did not change. Only the scale did.**"
        )),
        formal("Auto-scaling"),
        Para(text=(
            "When prices are flat or ranging, auto-scaling stretches them "
            "across the screen and makes low volatility activity look more "
            "volatile. When prices are trending, it shortens every bar to fit "
            "the trend in and makes volatile activity look less volatile. "
            "Either way the vertical scaling is not preserved, so it becomes "
            "very difficult to learn what price behaviour at a given timeframe "
            "really looks like. **The book's instruction is plain: it is always"
            " best to turn auto-scaling off, because switching it off "
            "normalizes volatility on the charts and gives more accurate price "
            "visualization.** That is the answer to the chapter's second review"
            " question."
        )),
        Fig(
            panels=(Panel(number="3.6"),), cols=1, height_mm=62.0,
            caption="Auto-scaling misrepresenting volatility.",
        ),
        Para(text=(
            "In Figure 3.6 the top two panels have auto-scaling on. The "
            "encircled quiet stretch is portrayed as more volatile than it is "
            "while the screen is flat, and then suddenly shrinks once a later "
            "trend has to be fitted in. The bottom two panels have it off, and "
            "the encircled stretch keeps its true height."
            "\n\n"
            "One honest note. The chapter's learning objectives ask you to set "
            "up a volatility neutral chart. **That phrase never appears in the "
            "chapter's text; switching off auto-scaling, which the book says "
            "normalizes volatility, is the nearest it comes.**"
        )),
        SelfCheck(text=(
            "Three five minute bars are 50.00, 50.60, 49.70, 50.20, then "
            "50.20, 50.90, 50.10, 50.70, then 50.70, 50.75, 49.40, 50.30. "
            "Write down the fifteen minute bar before you look back."
        )),
    ),
)


# ==========================================================================
# Section 2 - What the four prices mean, and four kinds of gap
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="What the Four Prices Mean, and Four Kinds of Gap",
    standfirst="Why the high and the low carry more weight than the open and "
               "the close, the three conditions that make the open and "
               "close matter more, and the four ways the book measures a "
               "gap.",
    blocks=(
        Head(number="2.1", text="Two prices set by the clock, two by traders"),
        Para(text=(
            "OHLC data is the result of filtering price over an interval, but "
            "the four prices do not carry the same significance. **The open and"
            " the close are merely a function of time stamping: they mark where"
            " an arbitrary interval happened to start and stop, and once the "
            "interval ends, the price at that instant becomes the close of one "
            "bar and usually the open of the next.**"
            "\n\n"
            "The high and the low are different in kind. They are created by "
            "actual market forces of supply and demand. **The book's own figure"
            " labels the high a function of supply and the low a function of "
            "demand: sellers capped the high, buyers held the low.** A share "
            "trades up to 52 pesos and sellers meet it there; it trades down to"
            " 49 and buyers meet it there. Both prices were set by people "
            "risking money, not by the clock."
        )),
        formal("Price rejection"),
        Fig(
            panels=(Panel(number="3.7"),), cols=1, height_mm=56.0,
            caption="What sets each of the four prices.",
        ),
        Para(text=(
            "Figure 3.7 labels one period's four prices by what sets them: time"
            " stamp, supply, time stamp, demand. The final sentence of the "
            "definition is the practical one. **A weekly high means more than a"
            " five minute high, because the longer the interval, the more "
            "significant the high and low it forms.**"
        )),

        Head(number="2.2", text="When the open and the close matter more"),
        Para(text=(
            "Having demoted the open and the close, the book gives three "
            "conditions under which they gain importance and attention from "
            "market participants, and become more reliable and actionable. They"
            " are the answer to the chapter's third review question."
        )),
        Points(
            title="The three conditions",
            numbered=True,
            items=(
                "The durations between active trading sessions are longer.",
                "The opening and closing prices belong to a higher timeframe "
                "bar or candlestick.",
                "There is a larger price gap between the previous close and "
                "the new open.",
            ),
        ),
        Fig(
            panels=(Panel(number="3.8"),), cols=1, height_mm=52.0,
            caption="Longer breaks between sessions raise the significance "
                    "of the open and close.",
        ),
        Para(text=(
            "Figure 3.8 is the first condition in a picture: three trading "
            "sessions separated by stretches of no trading. **The longer the "
            "market has been shut, the more its opening price means.** That is "
            "why the daily open and close draw more interest than the opens and"
            " closes between the morning and afternoon sessions of one day: the"
            " break overnight is longer than the break at lunch. A daily open "
            "is also a higher timeframe price than a five minute one, so it "
            "meets the second condition at the same time."
            "\n\n"
            "The other side of the same argument is a market with no break at "
            "all. **Spot foreign exchange trades continuously through the week,"
            " from Sunday evening to the Friday close, and in continuously "
            "traded markets the open and close matter less than the high and "
            "the low.**"
        )),
        SelfCheck(text=(
            "Why should a daily closing price be taken more seriously than "
            "the close of a five minute bar in the middle of the morning? "
            "Give two of the three conditions."
        )),

        Head(number="2.3", text="Four ways to measure a gap"),
        Para(text=(
            "A share closes at 102 pesos and opens the next morning at 106. "
            "Nobody traded at 103, 104 or 105 in between: price jumped over "
            "them."
        )),
        formal("Gap"),
        Para(text=(
            "The four types are four ways of measuring the same jump, and they "
            "are easiest to learn on one pair of bars. Say the last bar had a "
            "high of 104 and closed at 102, and the new bar opens at 106, then "
            "trades between a low of 105.50 and a high of 108. **Types 1 and 2 "
            "are measured to the new bar's open, so both exist the moment the "
            "market opens: close to open is 4 pesos, and high to open is 2.**"
        )),
        formal("Type 1 and Type 2 gaps"),
        Para(text=(
            "**Types 3 and 4 are measured to the new bar's high or low, so you "
            "only know them once the new bar has closed: previous high to new "
            "low is 1.50 pesos, and previous close to new low is 3.50.** For a "
            "gap downward, read low for high and high for low; that is why "
            "every definition says high or low."
        )),
        formal("Type 3 and Type 4 gaps"),
        Fig(
            panels=(Panel(number="A"),), kind="chart", height_mm=57.0,
            caption="The four gaps measured on one pair of bars, in pesos.",
        ),
        Para(text=(
            "Chart A draws exactly that pair of bars with the four brackets "
            "measured between them. Follow each bracket back along its dashed "
            "guides to see which two prices it joins. The gold one is Type 3, "
            "the gap usually called a window in Japanese candlestick and bar "
            "charts: the two bars do not overlap at all."
        )),
        Fig(
            panels=(Panel(number="3.9"),), cols=1, height_mm=52.0,
            caption="Four definitions of a gap.",
        ),
        Para(text=(
            "Figure 3.9 is the book's schematic of the same four, grouped the "
            "useful way: Types 1 and 2 created instantaneously when the next "
            "bar opens, Types 3 and 4 requiring the next bar to close before "
            "the gap can be identified."
        )),

        Head(number="2.4", text="What a gap does afterwards"),
        Para(text=(
            "A gap normally represents an area of support or resistance, "
            "depending on whether price is above or below it, and this is "
            "especially so for a Type 3 gap. Larger gaps are more significant. "
            "**Prices are generally expected to return and fill the gap at a "
            "later date, although there are many instances where this does not "
            "occur.** Read both halves of that sentence: the book does not say "
            "that gaps always fill."
            "\n\n"
            "The chapter uses support and resistance here without defining "
            "them, exactly as Chapter 2 did. Chapter 5 is where the book "
            "defines them, and these notes do not borrow a definition in the "
            "meantime."
        )),
        Para(text=(
            "The book also notes that the average true range (ATR) is somewhat "
            "related to a Type 4 gap. The true range of a bar is the greater of"
            " its own range and the distance from the last close to its high or"
            " low. On the running example the new bar's range is 108 minus "
            "105.50, which is 2.50, but the distance from the last close of 102"
            " to the new high of 108 is 6, so its true range is 6 pesos. **The "
            "chapter gives the true range and not the average; how ATR is "
            "averaged is taught in Chapter 8.** ATR comes back in Section 3, as"
            " one way to size a constant volatility bar."
        )),
        Para(text=(
            "Finally, the book looks ahead. Chapter 5 analyses gaps in relation"
            " to market phase, and the four it covers are common gaps, "
            "breakaway gaps, runaway gaps (also called continuation or midway "
            "gaps) and exhaustion gaps. Those are names for later. **Do not "
            "confuse the two lists: Types 1 to 4 are ways of measuring a gap, "
            "and the Chapter 5 list is kinds of gap.**"
        )),
        SelfCheck(text=(
            "The last bar closed at 60 with a low of 58. The new bar opens "
            "at 55 and trades between 53 and 56. Measure all four gap types "
            "for this gap downward."
        )),
    ),
)


# ==========================================================================
# Section 3 - Five constant measures
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Five Constant Measures",
    standfirst="The five things that can decide when a bar is finished, the "
               "four constant time charts, the charts that ignore the "
               "clock, and the one chart with no constant at all.",
    blocks=(
        Head(number="3.1", text="What decides when a bar is finished"),
        Para(text=(
            "Every chart has to decide when one bar ends and the next begins. "
            "Every bar has a range, a duration, a volume, a number of "
            "transactions and a volatility, and each kind of chart holds one of"
            " those constant and lets the rest vary. The book calls them the "
            "five types of constant measure chart, and this list is the answer "
            "to its fourth review question."
        )),
        Points(
            title="The five constant measures",
            numbered=True,
            items=(
                "**Constant time**: the bar closes when a specified time "
                "interval is met. Candlestick, bar, equivolume and line "
                "charts.",
                "**Constant range**: the bar closes when a specified "
                "excursion in price is met. Point and figure and Renko "
                "charts.",
                "**Constant volume**: the bar closes when a specified volume "
                "is met.",
                "**Constant transaction**, or tick: the bar closes when a "
                "specified number of transactions is met.",
                "**Constant volatility**: the bar closes when a specified "
                "amount of standard deviation or ATR is met.",
            ),
        ),

        Head(number="3.2", text="Constant time charts"),
        Para(text=(
            "On a daily chart, a quiet day and a wild day each get exactly one "
            "bar of the same width. That is the defining property of the "
            "commonest kind of chart."
        )),
        formal("Constant time chart"),
        Para(text=(
            "Constant time charts are the most popular form of chart "
            "construction, and the book gives a reason that matters later. It "
            "sorts overlay indicators into three kinds and treats them fully in"
            " Chapter 8: geometric ones drawn from points on the chart, such as"
            " trendlines, channels and chart patterns; numerical ones computed "
            "from the prices, such as moving averages; and horizontal ones, "
            "such as prior support and resistance levels. Constant time charts "
            "work with both numerically and geometrically based overlays. "
            "Charts that are not constant time should use numerical and "
            "horizontal overlays only, because their time axis is not linear, "
            "and a line drawn between two points depends on how far apart the "
            "points are."
        )),
        Para(text=(
            "The first constant time chart draws each interval as one vertical "
            "line. A day that opened at 50, ran up to 52, fell to 49 and closed"
            " at 51 is a line from 49 to 52, with a small tick on the left at "
            "50 for the open and a tick on the right at 51 for the close, which"
            " is how the book's own figures draw it."
        )),
        formal("Bar chart"),
        Para(text=(
            "The second throws nearly all of that away. Five days closing at "
            "50, 51, 50.50, 52 and 53 pesos become five dots joined by a line, "
            "and the highs and lows of those days appear nowhere."
        )),
        formal("Line chart"),
        Fig(
            panels=(Panel(number="B"),), kind="chart", height_mm=57.0,
            caption="A line chart drawn over the highs and lows it leaves "
                    "out.",
        ),
        Para(text=(
            "Chart B shows the loss. The pale bars are each day's high and low;"
            " the joined dots are the line chart. The line never reaches the "
            "extremes, and those extremes are precisely the prices Section 2 "
            "called the true indicators of market force. **So a line chart "
            "filters out more price information than a bar chart, which is why "
            "it says little about supply and demand and is still useful as a "
            "trend identifier.** It is, in effect, the chart Chapter 2's Dow "
            "Theory reads."
        )),
        Para(text=(
            "The third constant time chart is a bar with the stretch between "
            "the open and the close drawn as a box. Open 50 and close 51 is a "
            "hollow, or white, box from 50 up to 51. Open 51 and close 50 is "
            "the same box filled, or black."
        )),
        formal("Japanese candlestick"),
        Fig(
            panels=(Panel(number="3.10"),), cols=1, height_mm=56.0,
            caption="Bullish and bearish Japanese candlesticks.",
        ),
        Para(text=(
            "Figure 3.10 labels both kinds part by part: the real body between "
            "open and close, and the upper and lower shadows, also called tails"
            " or wicks, running out to the high and the low. Candlestick "
            "formations may be classified as bullish or bearish, reversal or "
            "continuation, and simple, double or multiple; Chapter 14 takes "
            "them further. **One limit applies to bars and candles alike: "
            "neither can tell you whether the high or the low came first, "
            "because the intrabar detail has been filtered out.**"
        )),
        Para(text=(
            "The fourth constant time chart puts volume inside the bar. Two "
            "days have the same high and low; one traded 3 million shares and "
            "the other 1 million. On an equivolume chart the first is drawn as "
            "the wider bar. The book says only that larger volume gives a wider"
            " bar, not in what proportion, so these notes say no more."
        )),
        formal("Equivolume chart"),
        Para(text=(
            "Two things about equivolume are traps. **The first is that every "
            "bar still covers one interval of time, so it is a constant time "
            "chart, and yet its time axis is not plotted in a linear fashion, "
            "because the bars are different widths.** Trendlines, channels and "
            "chart patterns are therefore distorted on it, while numerical and "
            "horizontal overlays are not."
            "\n\n"
            "The second is that the book gives two accounts of its data. Beside"
            " Figure 3.4 it says equivolume bars require OHLCV data. Here it "
            "says they are constructed using the high and the low, with the "
            "open and the close disregarded. **Learn both statements, and know "
            "that the bar itself draws on the high, the low and the volume.** "
            "No assessment in this course will turn on the difference."
        )),
        Fig(
            panels=(Panel(number="3.11"),), cols=1, height_mm=62.0,
            caption="A candlestick chart and an equivolume chart of the same "
                    "prices.",
        ),
        Para(text=(
            "Figure 3.11 draws the same daily prices of one stock both ways. "
            "Look along the bottom of each: even spacing on the candlestick "
            "chart, uneven spacing on the equivolume chart. Then look at where "
            "the two trendlines end, at different prices, although they were "
            "drawn on the same data."
        )),
        SelfCheck(text=(
            "Which of the four constant time charts would you use to see "
            "supply and demand, and which to see only the trend? Why?"
        )),

        Head(number="3.3", text="Constant range charts"),
        Para(text=(
            "Set a size of 1 peso. A share that drifts 40 centavos all week "
            "draws nothing at all; a share that moves 3 pesos in a morning "
            "draws three. **Time has dropped out of the chart completely.**"
        )),
        formal("Constant range chart"),
        Para(text=(
            "The most popular constant range chart draws rising prices as a "
            "column of X's and falling prices as a column of O's. **With a box "
            "size of 1 peso and a reversal size of 3 boxes, price must move at "
            "least 1 peso to add a box in the direction of the column, and at "
            "least 3 x 1 = 3 pesos against the column before a reversal can be "
            "plotted in a new column.**"
        )),
        formal("Point and figure chart"),
        Fig(
            panels=(Panel(number="C"),), kind="chart", height_mm=57.0,
            caption="Point and figure columns built from a closing price "
                    "path, 1 peso box, 3 box reversal.",
        ),
        Para(text=(
            "Chart C builds the columns from a price path, using closing prices"
            " as the book says is normal. Follow the left panel with a finger "
            "and compare it with the right. The first dip is too shallow to "
            "reverse the X column, because it is less than three boxes; the "
            "second one is exactly deep enough, and the gold O column starts. "
            "Notice that the right panel has no time axis at all: one column "
            "per swing, however many days the swing took."
            "\n\n"
            "That missing time axis has a consequence. Because the time axis is"
            " non linear, geometrically based overlays would give inconsistent "
            "readings, so point and figure charting uses its own kind of "
            "trendline. **It needs only one point, and rises and falls along 45"
            " and minus 45 degree angles.** The book calls these bullish "
            "support and bearish resistance lines, used in place of "
            "conventional trendlines."
        )),
        Fig(
            panels=(Panel(number="3.12"),), cols=1, height_mm=66.0,
            caption="A point and figure chart with its 45 degree lines.",
        ),
        Para(text=(
            "Figure 3.12 is a point and figure chart of one stock with a plus "
            "45 degree line under the rise and a minus 45 degree line over the "
            "decline. Read the date labels along the bottom and see how "
            "unevenly they are spaced."
            "\n\n"
            "The second constant range chart uses bricks. With a brick size of "
            "1 peso, a rise from 50 to 52.40 adds two white bricks, and the 40 "
            "centavos over 52 do nothing. For a black brick, price must move at"
            " least two bricks, 2 pesos, the other way."
        )),
        formal("Renko chart"),
        Fig(
            panels=(Panel(number="3.13"),), cols=1, height_mm=56.0,
            caption="A Renko chart, with its non linear time axis.",
        ),
        Para(text=(
            "Figure 3.13 is a Renko chart of a commodity index in white and "
            "black bricks. **Compare it with point and figure: every brick gets"
            " a column of its own, and a reversal needs two bricks, which is "
            "why the book calls Renko charts essentially two brick reversal "
            "charts.**"
        )),

        Head(number="3.4", text="Volume, transactions and volatility"),
        Para(text=(
            "The next two charts count trading instead of price. Set 100,000 "
            "shares a bar, and a busy morning might draw ten bars while a slow "
            "afternoon draws one."
        )),
        formal("Constant volume chart"),
        Fig(
            panels=(Panel(number="D"),), kind="chart", height_mm=57.0,
            caption="Where each constant volume bar would close in one "
                    "session.",
        ),
        Para(text=(
            "The book gives no figure of a constant volume chart, so Chart D is"
            " ours. It draws one session's price and volume on an ordinary time"
            " axis and drops a gold line wherever another fixed block of shares"
            " has traded. **Every gold line marks the same volume; only the "
            "time between them changes.** The lines crowd together in the busy "
            "hours and spread out in the quiet ones, and that spacing is "
            "exactly what a non linear time axis means."
            "\n\n"
            "A tick chart counts trades rather than shares. Set 50 trades a "
            "bar, and fifty trades of 100 shares and fifty trades of 10,000 "
            "shares each make exactly one bar."
        )),
        formal("Constant transaction chart"),
        Para(text=(
            "The last constant measure lets volatility set the size of each "
            "bar. Set each bar at 2 x ATR: if the ATR is 0.50 pesos a bar needs"
            " a 1 peso move, and if the ATR widens to 1.50 it needs 3 pesos. It"
            " resembles a constant range chart, except that the minimum price "
            "excursion is determined by volatility rather than fixed."
        )),
        formal("Constant volatility chart"),
        Fig(
            panels=(Panel(number="3.14"),), cols=1, height_mm=62.0,
            caption="Constant volatility against constant range charting.",
        ),
        Para(text=(
            "Figure 3.14 draws the same market twice as point and figure: once "
            "with the box size set to 1 x ATR, which the book annotates as less"
            " volatile and more directional, and once with standard box sizing,"
            " annotated as more volatile and less directional. The book's point"
            " is that the volatility based version identifies trends more "
            "effectively. **It is objective, because the market's volatility "
            "sets the size, and subjective in the choice of how many multiples "
            "of ATR to use.**"
        )),

        Head(number="3.5", text="The chart with no constant at all"),
        formal("Three line break chart"),
        Para(text=(
            "After three white lines in a row, price has to fall to the low of "
            "those last three lines before a black line can be drawn. The book "
            "calls the three line break chart unique, because it is the only "
            "construct in the chapter with nothing held constant: range, "
            "duration, volume, transactions and volatility all vary. Bullish "
            "lines are white and bearish lines black, as with Renko bricks."
        )),
        Fig(
            panels=(Panel(number="3.15"),), cols=1, height_mm=56.0,
            caption="Three line break and Renko charts of the same market.",
        ),
        Para(text=(
            "Figure 3.15 puts a Renko chart and a three line break chart of the"
            " same period side by side. The big turns appear on both; the "
            "spacing of the same months does not match."
        )),
        Points(
            title="Which one each chart holds constant",
            items=(
                "**Constant time**: the duration.",
                "**Constant range**: the range, and the volatility.",
                "**Constant volume**: the volume.",
                "**Constant transaction**: the number of transactions per "
                "bar.",
                "**Constant volatility**: the volatility.",
                "**Three line break**: nothing at all.",
            ),
        ),
        Para(text=(
            "Everything not named on its line is variable. **One oddity is "
            "worth noticing rather than resolving: the book lists volatility as"
            " constant for both constant range and constant volatility "
            "charts.** What separates them is the range, which is fixed on one "
            "and set by volatility on the other."
        )),
        SelfCheck(text=(
            "On which of these is the time axis non linear: a bar chart, an "
            "equivolume chart, a Renko chart, a tick chart? Explain the one "
            "that surprises people."
        )),
    ),
)


# ==========================================================================
# Section 4 - Chart scaling
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Chart Scaling",
    standfirst="Three ways to scale a price axis and what each preserves, "
               "which overlays scaling changes and which it leaves alone, "
               "and why the same prices can look bullish on one scale and "
               "bearish on another.",
    blocks=(
        Head(number="4.1", text="Three ways to scale a price axis"),
        Para(text=(
            "The book names three scales: linear or arithmetic, ratio or "
            "logarithmic, and square root. The first two are the common ones "
            "and Chapter 2 already used them under their arithmetic and "
            "logarithmic names. This section gives the arithmetic behind them."
            "\n\n"
            "On a linear scale, a rise from 10 to 20 pesos and a rise from 90 "
            "to 100 pesos are drawn the same height, because both are 10 pesos."
            " But the first is a 100 percent rise and the second is only 11.1 "
            "percent, 10 divided by 90."
        )),
        formal("Linear scaling"),
        Para(text=(
            "A ratio scale makes the opposite trade. A rise from 10 to 20 pesos"
            " is 100 percent, and on a ratio scale it is drawn the same height "
            "as a rise from 90 to 180 pesos, which is also 100 percent even "
            "though it is a 90 peso move."
        )),
        formal("Ratio scaling"),
        Para(text=(
            "**One sentence in the book contradicts this definition.** Two "
            "sentences after defining ratio scaling as equal distances for "
            "equal percentage changes, it says that equal distances on the "
            "chart do not equate to equal percentage changes. The definition is"
            " stated twice and drawn twice, and the stray sentence is neither, "
            "so learn the definition. No assessment in this course rests on the"
            " stray sentence."
        )),
        Fig(
            panels=(Panel(number="E"),), kind="chart", height_mm=57.0,
            caption="The same prices on a linear, a square root and a ratio "
                    "axis.",
        ),
        Para(text=(
            "Chart E places the same prices, 10 to 100, on all three axes, each"
            " drawn to the same height, and marks the book's two moves on each."
            " On the linear axis the two bars are the same height. On the ratio"
            " axis the rise from 10 to 20 is far taller than the rise from 90 "
            "to 100. The square root axis falls in between, which is the whole "
            "of what the book says about it."
        )),
        Fig(
            panels=(Panel(number="3.16", label="Linear."),
                    Panel(number="3.17", label="Ratio, and the halfway "
                                                 "point.")),
            cols=2, height_mm=48.0,
            caption="Equal price steps, and where 55 lands on a ratio "
                    "scale.",
        ),
        Para(text=(
            "Figure 3.16 shows a linear axis in equal one dollar steps. Figure "
            "3.17 shows a ratio axis from 10 to 100 with the logarithm of each "
            "level beside it: 55, the arithmetic halfway point, has a log of "
            "1.74, above the midpoint of 1.50, so it sits high on the axis. "
            "**That is compression at the upper end, in numbers.**"
        )),
        Fig(
            panels=(Panel(number="3.18"),), cols=1, height_mm=48.0,
            caption="Equal percentage steps on a ratio scale.",
        ),
        Para(text=(
            "Figure 3.18 makes the same point the other way round: an axis "
            "doubling from 1 to 64, with every doubling drawn the same height "
            "and 0.3 apart in logarithms."
        )),

        Head(number="4.2", text="Which scale to use"),
        Para(text=(
            "**The ratio scale compresses price action at higher prices and "
            "expands it at lower prices, while linear scaling spreads price "
            "evenly across the whole range.** So linear scaling gives better "
            "definition and visualization at the upper end of prices and poorer"
            " clarity at the lower end, and ratio scaling gives better "
            "definition at the lower end and poorer clarity at the upper end."
            "\n\n"
            "The book's general guideline follows from that. Use linear charts "
            "when the price range under observation is relatively small. For "
            "stock price ranges exceeding 100 dollars it may be more "
            "appropriate to use ratio charting, and ratio charts are best for "
            "very long term market action, mainly in equities. **For futures, "
            "foreign exchange, and any instrument traded on very low margin, "
            "that is very high leverage, linear charts are more suitable, "
            "because ratio charts would compress price too much at higher "
            "prices.** The book does not say whether its 100 dollar threshold "
            "means the price itself or the distance from low to high, and these"
            " notes do not guess."
        )),
        formal("Square root scale"),
        Para(text=(
            "Equal price steps on a square root axis get shorter as price "
            "rises, but not as much shorter as on a ratio axis. **The book "
            "calls its in between signal rather disconcerting: most traders "
            "react to uptrend line violations on either a linear or a ratio "
            "chart, so a trader using square root scaling will enter and exit "
            "either too early or too late relative to the levels everyone else "
            "is watching.**"
        )),
        SelfCheck(text=(
            "You are charting a highly leveraged currency pair over three "
            "months. Which scale does the book recommend, and why not the "
            "other one?"
        )),

        Head(number="4.3", text="What scaling changes, and what it does not"),
        Para(text=(
            "This is the answer to the chapter's fifth review question. "
            "**Scaling affects every overlay that relies on geometry in its "
            "construction: trendlines, channels and chart patterns.** Change "
            "the scale and the angle of every trendline changes with it, so it "
            "indicates different levels of potential support and resistance. "
            "Scaling does not affect overlays constructed numerically, such as "
            "moving averages and price envelopes, and it does not affect "
            "overlays that mark horizontal levels: prior support and "
            "resistance, Fibonacci extensions, retracements, projections and "
            "expansions, Gann one eighth and one third retracements, and Gann "
            "Square of Nine projections. A horizontal line is the same price on"
            " any scale. The chapter only names these overlays; each is taught "
            "later in the book."
        )),
        Points(
            title="When trendlines are penetrated",
            items=(
                "On **ratio** charts, uptrend lines are penetrated sooner and "
                "downtrend lines later.",
                "On **linear** charts, uptrend lines are penetrated later and "
                "downtrend lines sooner.",
            ),
        ),
        Fig(
            panels=(Panel(number="3.19", label="Uptrend lines."),
                    Panel(number="3.20", label="Downtrend lines.")),
            cols=2, height_mm=56.0,
            caption="The same trendlines broken at different times on the "
                    "two scales.",
        ),
        Para(text=(
            "Figure 3.19 draws the same uptrend on an arithmetic and a "
            "logarithmic chart, and the line breaks first on the logarithmic "
            "one. Figure 3.20 does the same for a downtrend, and there the "
            "arithmetic chart breaks first. Chapter 2 gave the uptrend half of "
            "this rule; this is the whole of it."
        )),
        Para(text=(
            "Switching scales can change the whole mood of a chart. **The book "
            "gives four cases, and they reduce to one sentence: ratio makes "
            "both directions look bearish, and linear makes both look "
            "bullish.**"
        )),
        Points(
            title="The four appearances",
            items=(
                "Rising prices on a **ratio** chart may decelerate in a "
                "concave curve, like a flattening out or rounding top: a "
                "potentially bearish appearance.",
                "Declining prices on a **ratio** chart may accelerate in a "
                "convex curve, like a downward parabolic move: a potentially "
                "bearish appearance.",
                "Rising prices on a **linear** chart may accelerate, or rise "
                "evenly, in a convex curve, like an upward parabolic move: a "
                "potentially bullish appearance.",
                "Declining prices on a **linear** chart may decelerate in a "
                "concave curve, like a flattening out or rounding bottom: a "
                "potentially bullish appearance.",
            ),
        ),
        Fig(
            panels=(Panel(number="3.21", label="A decline."),
                    Panel(number="3.22", label="An advance.")),
            cols=2, height_mm=62.0,
            caption="The same prices looking bearish on one scale and "
                    "bullish on the other.",
        ),
        Para(text=(
            "Figure 3.21 is a decline drawn on a semilog scale, another name "
            "the book uses for ratio, where it takes a convex, parabolic and "
            "bearish appearance, and on a linear scale, where it looks concave "
            "and more bullish. Figure 3.22 is an advance that appears to "
            "flatten out on a ratio chart and does not flatten on a linear one."
            " **The prices did not change their meaning; the scale supplied the"
            " mood.**"
        )),
        Fig(
            panels=(Panel(number="3.23"),), cols=1, height_mm=62.0,
            caption="Channels on linear and ratio scaling.",
        ),
        Para(text=(
            "Figure 3.23 closes the argument on channels. The same inflection "
            "points produce channels in different places on a semilog and a "
            "linear chart, while the moving average reads the same on both: "
            "geometric overlays are affected by scaling, numerical ones are "
            "not."
        )),
        SelfCheck(text=(
            "A share has risen steadily for five years. On which scale is it "
            "more likely to look as though it is rounding over, and would "
            "that be a fact about the share?"
        )),
    ),
)


# ==========================================================================
# Section 5 - The bid-ask spread
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="The Bid-Ask Spread",
    standfirst="Why most charts are drawn on the bid and what that does to a "
               "buyer, the three problems of the expensive, early and late "
               "longs, and how the spread bends the reward to risk ratio.",
    blocks=(
        Head(number="5.1", text="The price on the chart and the price you pay"),
        Para(text=(
            "The book's worked examples in this part are in dollars. These "
            "notes use pesos; the arithmetic is identical. Suppose the bid, the"
            " price you can sell at, is 10.00 pesos, and the ask, the price you"
            " must pay to buy, is 10.20. The spread is 20 centavos, and every "
            "trade that buys and then sells pays it."
        )),
        formal("Bid-ask spread"),
        Para(text=(
            "**Charts are typically drawn on bid prices, although many "
            "platforms can also draw price on the ask or on the mid price.** "
            "The book's rule is that on a bid-based chart, trade performance is"
            " adversely affected when initiating long entries and executing "
            "long exits, and that it does not specifically affect short entries"
            " or short exits."
            "\n\n"
            "That rule needs one reading note. The book defines shorting, in "
            "this part, as selling to open or close a position. **Read long the"
            " same way, as any buy, whether it opens a position or closes "
            "one.** Read like that, the rule says buying is hurt and selling is"
            " not, which is what the book's own examples show. Read long as the"
            " position rather than the order, and the rule would contradict the"
            " example that follows it."
        )),
        Fig(
            panels=(Panel(number="3.24"),), cols=1, height_mm=48.0,
            caption="Shorting resistance at the bid.",
        ),
        Para(text=(
            "Figure 3.24 is the easy case. Resistance sits at 10.00 on the bid "
            "chart, price tests it, and you sell at market. **You are filled at"
            " 10.00, slippage aside, because selling happens at the bid, which "
            "is the price the chart shows.** A sell limit order at 10.00 fills "
            "there or better, and the same is true when the sell is an exit, a "
            "stop loss or a profit target."
        )),

        Head(number="5.2", text="Three ways a buyer gets the wrong fill"),
        Para(text=(
            "Now buy instead. The breakout level is 10.00 and you plan to buy "
            "at 10.05. Price touches 10.05 on the bid chart, you buy at market,"
            " and you are filled at the ask: 10.25. **Right time, wrong "
            "price.**"
        )),
        formal("Expensive longs"),
        Fig(
            panels=(Panel(number="3.25"),), cols=1, height_mm=48.0,
            caption="Going long at the breakout.",
        ),
        Para(text=(
            "Figure 3.25 shows the two lines that make the problem: the chart "
            "said 10.05 and the account says 10.25, twenty cents above, which "
            "is the spread you paid."
            "\n\n"
            "Use a pending order to get the price exact and the problem moves "
            "rather than going away. A buy stop at 10.05 fills at 10.05, the "
            "ask, but at that moment the bid is 9.85, still below the 10.00 "
            "breakout level on the chart. **Right price, wrong time.**"
        )),
        formal("Early longs"),
        Para(text=(
            "Support is the mirror case. Buy at market as price tests a 10.00 "
            "support level and you are filled at the ask, 10.20: the expensive "
            "longs again. Use a pending order to buy at 10.00 instead and you "
            "are filled at 10.00, but only once the bid has already fallen to "
            "9.80, below the support level. **At a breakout the pending order "
            "is early; at support it is late.**"
        )),
        formal("Late longs"),
        Fig(
            panels=(Panel(number="3.26"),), cols=1, height_mm=48.0,
            caption="Going long at support.",
        ),
        Para(text=(
            "Figure 3.26 shows the late fill: the ask at 10.00 and the bid at "
            "9.80, the long filled at the ask by a pending order once the bid "
            "is already below the level. **The figure labels its level a "
            "resistance level, while its own title and the text call it "
            "support.** It is support, and these notes read it that way."
        )),
        SelfCheck(text=(
            "With a 20 centavo spread, name the problem in each case: a "
            "market buy at a breakout, a buy stop at a breakout, and a "
            "pending buy at support."
        )),

        Head(number="5.3", text="The spread and the reward to risk ratio"),
        Para(text=(
            "The spread also bends the odds of every trade. It increases the "
            "probability of exiting at the stop loss, which the book calls loss"
            " promoting, and it reduces the probability of exiting at the "
            "profit target, which it calls profit restricting. How it shows "
            "depends on the kind of order."
            "\n\n"
            "With a market order, the spread is deducted from the profit and "
            "added to the loss, and it is reflected in the trading account. A "
            "trader buys when the bid is 1.00; the spread is 0.20, so the "
            "trader is long at 1.20. With a profit target at 1.50, the most the"
            " trade can make is 0.30, not 0.50. With a stop at 0.50, the most "
            "it can lose is 0.70, not 0.50. **The spread adjusted reward to "
            "risk ratio is 0.30 divided by 0.70, which is 0.43, not 1.**"
        )),
        Fig(
            panels=(Panel(number="3.27", label="A market order."),
                    Panel(number="3.28", label="A pending order.")),
            cols=2, height_mm=56.0,
            caption="The spread against market and pending long entries.",
        ),
        Para(text=(
            "Figure 3.27 sets that out, the expected ratio of 0.50/0.50 = 1 "
            "beside the spread adjusted 0.30/0.70 = 0.43. Figure 3.28 is the "
            "pending order version, and there the cost is hidden. The spread is"
            " not deducted from the profit or added to the loss, and it does "
            "not show in the account: the ratio stays 0.50/0.50 = 1. But the "
            "order was filled at the ask of 1.00 while the bid was 0.80, so "
            "price must rise 0.70 from the bid to reach the target and fall "
            "only 0.30 to reach the stop. **Same ratio on paper, worse odds in "
            "the market.**"
        )),
        Para(text=(
            "The remedy is to make the spread small relative to the trade: "
            "increase the size of the profit target and the stop loss relative "
            "to the spread, and the obvious way to do that is to trade a higher"
            " timeframe or a larger wave cycle. A 20 centavo spread is small "
            "against a 5 peso target and most of a 30 centavo one. **That is "
            "why the spread hurts the short term trader most, and the scalper "
            "above all.** Scalpers need to buy at the bid and sell at the ask "
            "to reduce their costs, and a standard level one (L1) trading "
            "platform will not let a trader do either. This part answers the "
            "chapter's seventh review question."
        )),
        SelfCheck(text=(
            "Bid 2.00, spread 0.10, bought at market. Target 2.40, stop "
            "1.80. Work out the expected and the spread adjusted reward to "
            "risk ratios."
        )),
    ),
)


# ==========================================================================
# Section 6 - Futures contracts
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Futures Contracts",
    standfirst="Why futures exist and why they expire, which contract to "
               "trade, rolling over at a premium or a discount, contango and "
               "backwardation, and three ways to chart a string of "
               "contracts.",
    blocks=(
        Head(number="6.1", text="Contracts that expire"),
        Para(text=(
            "Futures contracts were originally created to let commodity "
            "producers hedge against falling prices. By shorting an equal "
            "amount in the futures market, a producer need not worry about "
            "prices falling at harvest time, having locked in production costs "
            "and any potential profit whatever prices do afterwards. **That is "
            "why the book calls futures essentially a bearish mechanism.**"
            "\n\n"
            "**The chapter describes what futures are for and how they behave, "
            "and it never defines a futures contract itself.** These notes do "
            "not supply a definition from elsewhere. Everything in this section"
            " follows from one fact the book does state: unlike shares, every "
            "futures contract eventually expires, so a position has to be moved"
            " from one contract to the next."
        )),
        formal("Rollover"),
        Para(text=(
            "A contract is normally fairly illiquid through most of its life, "
            "until the last three to six months before expiry. **Volume and "
            "open interest are greatest about two to three months before "
            "expiry, and as expiry approaches, volume subsides as traders roll "
            "into the next contract.** That decline can mislead an analyst into"
            " thinking a trend is weak, when a quick look at the next contract "
            "would show volume rising over the same period. To gauge the true "
            "volume and open interest across rollover points, the book says to "
            "use a continuous chart."
        )),
        Fig(
            panels=(Panel(number="3.29", label="Two contracts."),
                    Panel(number="3.30", label="One continuous chart.")),
            cols=2, height_mm=56.0,
            caption="Volume on two silver contracts, and on the continuous "
                    "chart.",
        ),
        Para(text=(
            "Figure 3.29 shows it happening: volume contracting on the expiring"
            " July silver contract while it expands on the September contract, "
            "which has become the nearby one. Figure 3.30 is the continuous "
            "chart of the same months, one balanced view of volume across "
            "several contracts. **Falling volume on an expiring contract is "
            "traders leaving, not the trend weakening.** The practical advice "
            "follows: trade the contract with the largest volume and open "
            "interest, which may not be the nearby one, and roll slightly "
            "before expiry to avoid the volatility of traders exiting at the "
            "last moment."
        )),

        Head(number="6.2", text="Naming the contracts"),
        Para(text=(
            "It is March and the March contract has just expired. June is now "
            "the contract that expires soonest."
        )),
        formal("Front month contract"),
        Para(text=(
            "The next contract is the second one out, with the expiry closest "
            "to the nearby contract; with June as the front month, September is"
            " next. **Contracts further out than that, December and the "
            "following March, are back month contracts.** Traders may keep "
            "rolling into the next nearby contract, may roll only into the next"
            " month contract two contracts further out, or may hold one "
            "contract closer and another further out at once to create a "
            "calendar spread or for other hedging purposes."
        )),
        Fig(
            panels=(Panel(number="3.31"),), cols=1, height_mm=44.0,
            caption="Identifying the front, next and back month contracts.",
        ),
        Para(text=(
            "Figure 3.31 lays out quarterly contracts over twelve months and "
            "shows, for each starting point, which contract is the front month,"
            " which is the next month and which is the back month. Drop down "
            "one row and every label moves one contract along."
            "\n\n"
            "Delivery months are identified by letters: F January, G February, "
            "H March, J April, K May, M June, N July, Q August, U September, V "
            "October, X November and Z December. **The quarterly four are H, M,"
            " U and Z.**"
        )),
        SelfCheck(text=(
            "List the four characteristics of the front month contract, and "
            "say which way each of the two spreads runs."
        )),

        Head(number="6.3", text="Rolling at a premium or a discount"),
        Para(text=(
            "The new contract may not be trading at the same price as the one "
            "expiring. Sell March at 11 pesos and buy June at 12, and you pay 1"
            " peso to stay in the trade."
        )),
        formal("Negative roll yield"),
        Para(text=(
            "Reverse the prices, selling March at 12 and buying June at 11, and"
            " you collect 1 peso for staying in the trade."
        )),
        formal("Positive roll yield"),
        Fig(
            panels=(Panel(number="3.32", label="At a premium."),
                    Panel(number="3.33", label="At a discount.")),
            cols=2, height_mm=52.0,
            caption="Losses from negative roll yields, and profits from "
                    "positive ones.",
        ),
        Para(text=(
            "Figures 3.32 and 3.33 are the two cases drawn side by side, each a"
            " long bought in March at 10 dollars and rolled into June. In "
            "Figure 3.32 the roll pays a 1 dollar premium; in Figure 3.33 it "
            "collects a 1 dollar discount. **Successive rolls accumulate, which"
            " is how the two surprising sentences in the definitions come "
            "about: a long position can lose money in a rising market, and make"
            " money in a falling one, if the premiums or discounts are large "
            "enough.**"
        )),

        Head(number="6.4", text="Contango, backwardation and convergence"),
        Para(text=(
            "Contracts further out may trade at successively higher or lower "
            "prices. Suppose the spot price is expected to be 100 at expiry, "
            "and the contracts further out trade at 101, 102, 103 and 104."
        )),
        formal("Normal contango"),
        Para(text=(
            "Now suppose they trade at 99, 98, 97 and 96 against the same "
            "expected spot price of 100."
        )),
        formal("Normal backwardation"),
        Para(text=(
            "Traders often drop the word normal and compare the further out "
            "contracts with the nearby contract or the current spot price "
            "instead. The book calls that an informal use of the terms, but "
            "common practice among futures traders. **The difference matters: "
            "simple contango can be read off a chart, while normal contango "
            "needs the expected spot price at expiry.** The book does not say "
            "how to estimate that expected price; it says only that some "
            "knowledge of it is required."
        )),
        Fig(
            panels=(Panel(number="3.34"),), cols=1, height_mm=62.0,
            caption="Simple contango in 2012 gold futures.",
        ),
        Para(text=(
            "Figure 3.34 shows gold futures with each further out contract "
            "trading higher than the nearby December one. That is simple "
            "contango, and the book notes that it may or may not be normal "
            "contango. The next fact ties the two ideas together."
        )),
        formal("Convergence"),
        Fig(
            panels=(Panel(number="3.35"),), cols=1, height_mm=52.0,
            caption="Futures and spot prices converge at expiration.",
        ),
        Para(text=(
            "Figure 3.35 draws it with the spot assumed to stay at 100: the "
            "backwardated contracts at 99 to 96 rise to meet it, with a "
            "positive yield, and the contango contracts at 101 to 104 fall to "
            "meet it, with a negative yield. With some mispricing, the book "
            "adds, a trader may go long a far out backwardated contract and "
            "short a nearby one and lock in the gain from convergence whatever "
            "the direction of price, although the spread and trading costs "
            "still decide whether it pays."
            "\n\n"
            "The book's real example of negative roll yield is natural gas in "
            "2009. Natural gas rallied strongly through the year, but the U.S. "
            "Natural Gas Fund, which tracks gas through futures and so has to "
            "roll, rolled at relatively large premiums and lost money. "
            "**Contango can take a whole rally away from a holder who has to "
            "roll.** Very short term traders who trade individual contracts and"
            " never roll are neither hurt by negative roll yields nor helped by"
            " positive ones."
        )),
        Fig(
            panels=(Panel(number="3.36", label="Gas and the fund."),
                    Panel(number="3.37", label="The fund relative to gas.")),
            cols=2, height_mm=52.0,
            caption="Natural gas in contango against the fund that tracks "
                    "it.",
        ),
        Para(text=(
            "Figure 3.36 puts the rallying continuous chart of natural gas "
            "beside the fund over the same months, and Figure 3.37 is the "
            "fund's relative strength against spot gas, falling steadily and "
            "labelled as the effect of negative roll yield. The book does not "
            "say what happened to the fund afterwards, and neither do these "
            "notes. Together this subsection is the answer to the chapter's "
            "sixth review question."
        )),
        SelfCheck(text=(
            "Why does a contract in contango tend to fall toward expiry even "
            "if the spot price does not move at all?"
        )),

        Head(number="6.5", text="Charting a string of contracts"),
        Para(text=(
            "Between the nearby and the next contract there may be a premium or"
            " discount gap. For a trader it is only a payment made or received "
            "at rollover. For the chartist it is a problem, because a chart "
            "needs a continuous record of price and the contracts do not join "
            "up. The book gives three popular approaches."
            "\n\n"
            "The simplest is to join the nearest contracts end to end and leave"
            " the jumps in. March expires at 110 and June is trading at 120, so"
            " the chart simply jumps 10 at the roll."
        )),
        formal("Unadjusted nearest futures chart"),
        Fig(
            panels=(Panel(number="3.38"),), cols=1, height_mm=48.0,
            caption="An unadjusted nearest futures chart.",
        ),
        Para(text=(
            "Figure 3.38 shows the jumps, a price gap distortion at every "
            "rollover. Each jump is a roll, not a market move, which is why a "
            "trendline drawn across them means nothing. **Accurate history, "
            "useless analysis.**"
            "\n\n"
            "The second approach shifts history instead. March expires at 110 "
            "while June trades at 120, so every March price is raised by 10, "
            "and its troughs at 80 and 90 become 90 and 100. When June expires "
            "the process repeats: if September trades at a further 10 premium, "
            "the same troughs move again, to 100 and 110. The book also calls "
            "this a spread adjusted chart."
        )),
        formal("Back-adjusted continuous chart"),
        Fig(
            panels=(Panel(number="3.40"),), cols=1, height_mm=48.0,
            caption="Back adjusting in continuous charts.",
        ),
        Para(text=(
            "Figure 3.40 draws the mechanism: the March contract lifted by the "
            "10 dollar spread to meet June. **The cost of back adjusting is "
            "that past prices no longer reflect what the contracts actually "
            "traded at, and at every roll the history shifts again, so past "
            "peaks and troughs keep changing.** Historical prices end up "
            "adjusted to the net accumulated spread. If newer contracts keep "
            "trading at a discount, past prices may even become negative."
        )),
        Fig(
            panels=(Panel(number="F"),), kind="chart", height_mm=57.0,
            caption="Back adjusting through several rolls at a discount.",
        ),
        Para(text=(
            "Chart F shows that last warning, which the book gives no figure "
            "for. Five contracts, each starting at a discount to the one "
            "before, are drawn as they traded, a falling saw in grey, and again"
            " back adjusted, one continuous black line. **The earliest adjusted"
            " prices sit below zero, where nobody ever traded.**"
        )),
        Fig(
            panels=(Panel(number="3.39"),), cols=1, height_mm=62.0,
            caption="A continuous chart against the contract itself.",
        ),
        Para(text=(
            "Figure 3.39 is the effect on a real market: the continuous, spread"
            " adjusted chart of gold above the December 2013 gold contract, "
            "with the OHLC readings for the same day boxed on each. They "
            "differ, because the continuous chart's history has been rewritten "
            "by adjustment and the contract's has not."
            "\n\n"
            "The shifting history causes one more problem. Relative or "
            "comparative strength charts will not display accurate ratios if "
            "past prices keep changing every time the data is back adjusted. "
            "For that job the book prefers the third approach."
        )),
        formal("Perpetual contract"),
        Para(text=(
            "Between two expiries, a perpetual series blends the nearby and "
            "further out contract prices by a weighting, so the value on the "
            "chart is not a price anyone traded at. The book does not give the "
            "weighting, and these notes do not supply one."
        )),
        Points(
            title="Which chart for which job",
            items=(
                "**Trading, and back or forward testing**: the back-adjusted "
                "continuous chart, which always displays the current price.",
                "**An accurate record of what actually traded**: the "
                "unadjusted nearest futures chart.",
                "**Relative strength charts**: perpetual contracts, because "
                "back adjusting keeps shifting the ratio.",
            ),
        ),
        Para(text=(
            "None of the three does every job. The list above, with Figure "
            "3.40, answers the chapter's eighth review question."
        )),

        Head(number="6.6", text="What this chapter names and does not teach"),
        Para(text=(
            "A chapter about how charts are built uses a great many words it "
            "does not stop to explain, and it is worth collecting them in one "
            "place. **None of the following is examinable from Chapter 3, and "
            "none of it should be filled in from outside the book.**"
            "\n\n"
            "Gann bars, Kagi charts and Gann swing charts are named and drawn "
            "but never explained. The breadth and sentiment data items are "
            "listed and never defined. The average true range is used without "
            "its averaging, which Chapter 8 teaches. Support, resistance, "
            "trendlines and channels are used throughout and defined in Chapter"
            " 5. Normal contango needs an expected spot price the book does not"
            " say how to estimate. The ratio chart guideline gives a 100 dollar"
            " threshold without saying what it is measured on. The learning "
            "objectives ask for a volatility neutral chart, a phrase the text "
            "never uses. And a futures contract is never defined at all."
            "\n\n"
            "The book also contradicts itself twice and mislabels one figure, "
            "and all three are named where they occur: one stray sentence "
            "against the definition of ratio scaling, two accounts of the data "
            "an equivolume bar uses, and a support level labelled resistance in"
            " Figure 3.26. **In each case the right answer is to say what the "
            "book says and to mark the edge of it, rather than to borrow a "
            "tidier answer from somewhere the examiner is not reading.**"
        )),
    ),
)


# ==========================================================================
# The document
# ==========================================================================

NOTES = LectureNotes(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 3",
    title="Mechanics and Dynamics of Charting",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    term="First semester",
    source_note="Chapter scope follows Lim, M. (2016), The Handbook of "
                "Technical Analysis, chapter 3. Figures are reproduced from "
                "that text and remain the publisher's copyright.",
    orientation=(
        "These notes are the record of what Chapter 3 covered, written to be "
        "read on their own. If you were in the room, they are what to revise "
        "from. If you missed the session, they are the session. They follow "
        "the lecture in the same order and split into the same six parts, so "
        "you can move between the slides and these pages without hunting."
        "\n\n"
        "The chapter is about how a chart is built, so read it with the "
        "figures beside you. Every term is defined once, in the same words "
        "as the slides, and listed again at the back. The check yourself "
        "boxes are not assessed. Where the book leaves a question open, uses "
        "a word it has not defined, or says two different things, these "
        "notes say so rather than filling the gap from somewhere else, and "
        "Section 6.6 collects every one of those places."
    ),
    objectives=(
        "Understand chart construction and how technical data is "
        "incorporated and displayed.",
        "Describe the process by which OHLC data is created and its "
        "relationship to various charts.",
        "Identify and differentiate between contango and backwardation, and "
        "their connection with negative and positive roll yields.",
        "Understand the adverse effects of the bid-ask spread on trading "
        "performance.",
        "Construct various charts using constant measures of time, range, "
        "volatility, trade volume and number of transactions.",
        "Set up a volatility neutral chart for consistent viewing of price "
        "action.",
    ),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6),
    # The summary and the review questions are the book's, and the deck's
    # closing slides are where they are maintained. build_lecture_notes3.py
    # reads them from there and fills these in, so editing the closing slide
    # moves the notes with it. Do not retype them here.
    summary=(),
    review_questions=(),
    sources=(
        "Lim, M. (2016). The Handbook of Technical Analysis. Wiley. "
        "Chapter 3, and the source of every figure here.",
        "Murphy, J. (1999). Technical Analysis of the Financial Markets. New "
        "York Institute of Finance.",
        "Nison, S. (1994). Beyond Candlesticks. Wiley.",
        "Nison, S. (2001). Japanese Candlestick Charting Techniques. New "
        "York Institute of Finance.",
        "Schwager, J. D. (1996). Schwager on Futures. Wiley.",
    ),
)
