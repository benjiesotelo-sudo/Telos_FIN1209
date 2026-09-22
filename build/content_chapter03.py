"""Chapter 3 content for FIN1209 - Mechanics and Dynamics of Charting.

This file is pure data. It carries no drawing code, so the renderers in
deckkit.py are the same ones Chapters 1 and 2 use.

Everything here is written from scratch in teaching language. There is no
Quote slide in this chapter: the book offers no attributed sentence students
are expected to reproduce word for word, so nothing is quoted. Source of the
chapter scope is Lim, M. (2016), The Handbook of Technical Analysis, chapter
3, printed pages 65 to 98, which students have in the course text.

Where the standing rule bites, and how each place is handled. Every one is
named on a slide, and no check rests on any of them.

  * Ratio scaling. The book defines it as equal distances for equal
    percentage changes, and two sentences later says equal distances do not
    equate to equal percentage changes. Part 4 names the contradiction and
    teaches the definition, which the book states twice and draws twice.

  * Equivolume. The book says equivolume bars require OHLCV data, and on the
    same subject says they are built from the high and the low with the open
    and the close disregarded. Part 3 says both and names the difference.

  * Figure 3.26 labels its level a resistance level; its own title and the
    text call it support. Part 5 says so and teaches it as support.

  * Long and short in the bid-ask section. The book's rule says long exits
    are hurt and short exits are not, and it defines shorting there as
    selling to open or close a position. Part 5 says plainly that long must
    then be read as any buy, or the rule contradicts the book's own example.

  * Things the chapter names and never teaches: Gann bars, Kagi charts, Gann
    swing charts, the breadth and sentiment data items, the averaging in the
    average true range, the expected spot price that normal contango needs,
    the 100 dollar threshold for ratio charts, a volatility neutral chart,
    and a futures contract itself. Each is named where it appears, and the
    closing slides collect them.
"""

from deckkit import (
    Chapter,
    Chart,
    Check,
    Closing,
    Content,
    Figure,
    Question,
    Recap,
    Section,
    Term,
)

Q = Question

# ==========================================================================
# Part 1 - From price to OHLC
# ==========================================================================

PART1 = Section(
    number=1,
    title="From Price to OHLC",
    short="OHLC",
    minutes="About 25 minutes",
    covers=(
        "What a chart is for, who reads one, and the four families of data behind it.",
        "How a stream of trades is filtered into four prices: open, high, low and close.",
        "How long bars are built from short ones, and why auto-scaling misleads.",
    ),
    slides=(
        Content(
            title="What this chapter is for",
            lines=(
                "Charting is a two dimensional matrix on which technical data is viewed.",
                "It reveals repetitive price behaviour, volatility, price distortions and illiquidity.",
                "It is where trendlines, channels, envelopes and chart patterns get drawn.",
            ),
            accent="Chapter 2 kept only the close. This chapter brings back the other three prices.",
            notes=(
                "Link back: Dow Theory recognized only closing prices. Today we build the whole bar.",
                "Say the chapter is about how a chart is made, so almost every idea has a picture.",
            ),
        ),
        Term(
            term="Chartist",
            plain="Someone who studies the market by looking at charts of its data.",
            example="Anyone in this room who opens a daily chart of a PSE listed share and reads its peaks and troughs is working as a chartist.",
            formal="Analysts who use charts to study technical data are called chartists. They study classical chart patterns, trendlines, window oscillators, overlay indicators and other price formations.",
            notes=(
                "Contrast with the quants: they work in numbers, time series and back testing, and charts are optional for them.",
                "The traditional analyst prefers the picture. That is who this chapter is written for.",
            ),
        ),
        Term(
            term="Price-time chart",
            plain="The ordinary chart: price up the side, time along the bottom.",
            example="On a daily chart of a share, each step to the right is one more trading day and each step up is more pesos.",
            formal="The usual graphical form of technical data, where the vertical axis tracks the movement of price and the horizontal axis tracks the motion of time. The price axis may be scaled arithmetically (linear) or logarithmically (ratio).",
            notes=(
                "Point at the two axes on any chart in the room. Price vertical, time horizontal.",
                "Linear and ratio scaling get the whole of Part 4. Only name them here.",
            ),
        ),
        Content(
            title="When the time axis is only a counter",
            lines=(
                "On some charts the time axis is not plotted in equal units of time.",
                "It acts as a counter for each new block of data instead.",
                "On such charts, time is regarded as implicit along the x axis.",
            ),
            accent="Hold this. Part 3 is full of charts that work this way.",
            notes=(
                "Say implicit slowly. Time still passes, the chart just does not measure it.",
                "Do not name the charts yet. Point and figure and Renko are the examples in Part 3.",
            ),
        ),
        Content(
            title="Four families of technical data",
            lines=(
                "Price data: open, high, low and close.",
                "Transaction related data: volume and open interest.",
                "Market breadth data: advances, declines, new highs and new lows, and more.",
                "Sentiment data: the put/call ratio, margin debt, implied volatility (VIX), and more.",
            ),
            accent="The chapter lists all four families and works only with the first two.",
            caption="The chapter names every breadth and sentiment item and defines none of them. Do not learn them from here.",
            notes=(
                "The book's full list has thirteen breadth and sentiment items. Say they come back later in the book.",
                "Volume and open interest are Chapter 6. Today they appear only where a chart needs them.",
            ),
        ),
        Check(
            label="Chartists and the time axis",
            questions=(
                Q(
                    stem="Analysts who use charts to study technical data are called:",
                    options=("Quantitative analysts",
                             "Statisticians",
                             "Chartists",
                             "Arbitrageurs"),
                    answer="C",
                    reason="The book's own word. Quants may use charts too, but for them it is optional.",
                ),
                Q(
                    stem="On a chart where the time axis acts only as a counter for new blocks of data, time is:",
                    options=("Plotted in equal units of time",
                             "Regarded as implicit along the x axis",
                             "Plotted on the vertical axis",
                             "Left off the chart altogether"),
                    answer="B",
                    reason="The time axis still runs left to right, but it no longer measures equal time.",
                ),
            ),
        ),
        Term(
            term="Quantization of price",
            plain="Cutting a stream of trades into equal slices of time, one bar per slice.",
            example="Take one trading morning and cut it into five minute slices: 9:30 to 9:35, 9:35 to 9:40, and so on. Each slice becomes one bar.",
            formal="To create OHLC data, price activity is separated, or quantized, with respect to time, for each successive interval or period. An interval may be of any duration; the most popular are 1 minute, 5 minutes, 15 minutes, 1 hour, 4 hours, daily, weekly, monthly and yearly.",
            notes=(
                "Quantize is the book's word. Filter is the word it uses as a synonym. Say both.",
                "Ask which interval they looked at in Activity 1. Daily, almost certainly.",
            ),
        ),
        Term(
            term="OHLC data",
            plain="The four numbers left once a slice of trading has been summarised: where it started, its highest point, its lowest point, and where it finished.",
            example="In one five minute slice a share opens at 50.00 pesos, trades up to 50.80, down to 49.60, and ends at 50.40. Its OHLC is 50.00, 50.80, 49.60 and 50.40.",
            formal="The price at the beginning and end of an interval is the opening (O) and closing (C) price; the highest and lowest prices within it are the high (H) and low (L). Price activity is summarized into these four pieces of information.",
            notes=(
                "Read the four numbers in order and let them name each one back to you.",
                "Everything inside the slice other than these four is thrown away. That is the filtering.",
            ),
        ),
        Figure(
            title="Four pieces of information",
            number="3.1",
            shows="One five minute interval of jagged price filtered into four prices and drawn three ways: a 5 minute bar, a 5 minute candlestick and a 5 minute Gann bar, with the range marked.",
            notes=(
                "Trace the jagged line, then point at the three summaries of it on the right.",
                "Say the bar and the candlestick carry exactly the same four numbers. Only the drawing differs.",
            ),
        ),
        Content(
            title="The range, and where the next bar opens",
            lines=(
                "The range of a bar is the absolute difference between its high and low: range = |H - L|.",
                "In most cases the close of one interval is also the open of the next, unless there is a gap.",
                "OHLC data also builds bar charts, Gann bars and Japanese candlesticks.",
            ),
            accent="High 50.80 and low 49.60 give a range of 1.20 pesos.",
            caption="The chapter names Gann bars and draws one in Figure 3.1, but never says how to read one. Nothing is set on it.",
            notes=(
                "Absolute means the range is never negative. Say it once.",
                "The gap exception gets the second half of Part 2. Just flag it.",
            ),
        ),
        Check(
            label="Quantization and OHLC",
            questions=(
                Q(
                    stem="In one five minute interval a share opens at 50.00, trades as high as 50.80 and as low as 49.60, and ends at 50.40. What is its closing price?",
                    options=("50.00",
                             "50.80",
                             "49.60",
                             "50.40"),
                    answer="D",
                    reason="The close is the price at the end of the interval. The options are listed in the order O, H, L, C.",
                ),
                Q(
                    stem="A bar has a high of 50.80 and a low of 49.60. Its range is:",
                    options=("0.40",
                             "0.80",
                             "1.20",
                             "1.60"),
                    answer="C",
                    reason="Range is the absolute difference between the high and the low, 50.80 minus 49.60.",
                ),
            ),
        ),
        Term(
            term="Higher timeframe bar",
            plain="A longer bar built out of several shorter ones, by summarising them all at once.",
            example="Three five minute bars. The first opens at 50.00, the highest high of the three is 50.90, the lowest low is 49.40, and the third closes at 50.30. The fifteen minute bar is 50.00, 50.90, 49.40, 50.30.",
            formal="To create OHLC data over a longer period, take the opening price of the first period, the closing price of the last period, and the highest and lowest prices between them. Such composite bars are referred to as higher timeframe bars and candlesticks.",
            notes=(
                "Open of the first, close of the last, highest high, lowest low. Make them say the rule back.",
                "The longer the interval, the higher the timeframe. Nothing new is added, only filtered more.",
            ),
        ),
        Figure(
            title="Three short bars make one long one",
            number="3.2",
            shows="Fifteen minutes of price, three five minute intervals, summarised as one 15 minute bar and one 15 minute candlestick carrying the first open, the last close, and the extreme high and low.",
            notes=(
                "Find the open of the first interval and the close of the last one on the chart.",
                "Then find the highest high and lowest low. They can fall in any of the three intervals.",
            ),
        ),
        Figure(
            title="Quantization, bar by bar",
            number="3.3",
            shows="Eight successive five minute intervals of unfiltered price action, with the bar each interval produces drawn beneath it and the equivalent Japanese candlestick beneath that.",
            notes=(
                "Pick two neighbouring intervals and show the close of one becoming the open of the next.",
                "This figure is the first thing to drop if the clock is against you.",
            ),
        ),
        Figure(
            title="Most charts start from OHLC",
            number="3.4",
            shows="A family tree with OHLC data feeding the line, bar, candlestick, point and figure, three line break, Renko, Kagi and Gann swing charts, and a branch adding volume for the equivolume chart.",
            notes=(
                "Read the family across once. Every chart in Part 3 is on this tree.",
                "Point at the one branch that needs volume as well. That is the next slide.",
            ),
        ),
        Content(
            title="The one chart that needs a fifth number",
            lines=(
                "Most charts are created from OHLC data alone.",
                "The equivolume chart also needs volume, so the book says it requires OHLCV data.",
                "Kagi charts and Gann swing charts appear on the family tree and nowhere else in the chapter.",
            ),
            accent="OHLC plus V. That is the one exception.",
            caption="The chapter never explains Kagi or Gann swing charts. Nothing is set on them.",
            notes=(
                "V is volume. Equivolume comes back in Part 3 with a complication worth waiting for.",
                "Be straight about Kagi and Gann swing: the book names them and moves on, and so do we.",
            ),
        ),
        Figure(
            title="Three pictures of the same prices",
            number="3.5",
            shows="The same sequence of OHLC data drawn three ways: as a line chart, as a bar chart and as a candlestick chart.",
            notes=(
                "Same data, three drawings. Ask which one they find easiest to read at a glance.",
                "The line chart looks smoothest because it throws the most away. Part 3 says why.",
            ),
        ),
        Term(
            term="Auto-scaling",
            plain="A chart setting that stretches or squeezes the price axis so that whatever is on the screen fills the screen.",
            example="Scroll a flat, quiet month into view and its bars suddenly look tall and wild. Scroll a strong trend into the same window and those same bars shrink.",
            formal="Auto-scaling attempts to fill the entire screen with price activity, so the heights of bars and candlesticks keep changing with whether price is ranging or trending. The vertical scaling is not preserved or constant, and volatility is misrepresented.",
            notes=(
                "Most charting sites switch it on by default. Show them where the setting usually lives.",
                "The bars did not change. Only the scale did. Say that sentence.",
            ),
        ),
        Content(
            title="Why the book says switch it off",
            lines=(
                "When prices are flat, auto-scaling makes low volatility activity look more volatile.",
                "When prices trend, it makes volatile activity look less volatile.",
                "Switching it off normalizes volatility on the charts, for more accurate price visualization.",
            ),
            accent="It is always best to turn auto-scaling off. That is the book's instruction.",
            caption="The learning objectives ask for a volatility neutral chart. The text never uses that phrase; this is the nearest it comes.",
            notes=(
                "This slide is review question 2: why normalize charts for volatility.",
                "Be honest that the objective's phrase does not appear in the chapter's text.",
            ),
        ),
        Figure(
            title="The same stretch of price, magnified and shrunk",
            number="3.6",
            shows="Four panels of the same prices: with auto-scaling on, an encircled quiet stretch looks volatile and then shrinks when a trend comes into view; with it off, the stretch keeps its true height.",
            notes=(
                "Compare the circled area top left and top right. Same prices, different heights.",
                "Then the bottom pair: nothing changes. That is what switched off looks like.",
            ),
        ),
        Check(
            label="Higher timeframes and auto-scaling",
            questions=(
                Q(
                    stem="To build one 15 minute bar out of three 5 minute bars, its opening price is:",
                    options=("The open of the first 5 minute bar",
                             "The open of the last 5 minute bar",
                             "The highest of the three opens",
                             "The average of the three opens"),
                    answer="A",
                    reason="Open of the first period, close of the last, and the highest high and lowest low between them.",
                ),
                Q(
                    stem="According to the book, leaving auto-scaling switched on:",
                    options=("Preserves the vertical scale",
                             "Is needed to see a gap",
                             "Affects only line charts",
                             "Misrepresents volatility on the charts"),
                    answer="D",
                    reason="Flat prices are stretched to look volatile and trending prices are squeezed to look calm.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Chartists, and the price-time chart",
            "A time axis that is only a counter",
            "The four families of technical data",
            "Quantization, OHLC data and the range",
            "Higher timeframe bars",
            "Auto-scaling, and why to switch it off",
        ),
        notes=(
            "Ask for the rule for a higher timeframe bar. First open, last close, highest high, lowest low.",
            "Next: the four prices are not equally important, and the space between two bars has a name.",
        ),
    ),
)

# ==========================================================================
# Part 2 - What the four prices mean, and four kinds of gap
# ==========================================================================

PART2 = Section(
    number=2,
    title="What the Four Prices Mean, and Four Kinds of Gap",
    short="Significance and gaps",
    minutes="About 25 minutes",
    covers=(
        "Why the high and the low carry more weight than the open and the close.",
        "The three conditions that make the open and the close matter more.",
        "The four ways to measure a gap, and which ones need the next bar to close.",
    ),
    slides=(
        Content(
            title="Not all four prices are equal",
            lines=(
                "The open and the close are merely a function of time stamping.",
                "They mark where an arbitrary interval happened to start and stop.",
                "The high and the low are created by actual market forces of supply and demand.",
            ),
            accent="Two of the four are set by the clock. Two are set by traders.",
            caption="The book's figure labels the high a function of supply and the low a function of demand.",
            notes=(
                "Ask why the close of a five minute bar should mean anything. It is just where the clock stopped.",
                "Past papers ask which price is a function of supply. It is the high.",
            ),
        ),
        Term(
            term="Price rejection",
            plain="The high and low are where the market tried to go further and was pushed back.",
            example="A share trades up to 52 pesos and sellers meet it there; it trades down to 49 and buyers meet it there. Both prices were set by people risking money, not by the clock.",
            formal="The highs and lows represent areas of price rejection, caused by the responsive actions of market participants, who react to high and low prices by risking capital. This makes them more significant than the open and close, and the longer the interval, the more significant the high and low formed.",
            notes=(
                "Responsive actions is the book's phrase. Somebody saw the price and acted against it.",
                "A weekly high means more than a five minute high. Say that as the last line.",
            ),
        ),
        Figure(
            title="What sets each of the four",
            number="3.7",
            shows="One period of price with the open and the close each labelled a function of an arbitrary time stamp, the high labelled a function of supply and the low a function of demand, both as market forces.",
            notes=(
                "Read the four labels off the figure: time stamp, supply, time stamp, demand.",
                "Supply caps the high, demand holds the low. That is the picture to keep.",
            ),
        ),
        Content(
            title="When the open and the close gain importance",
            lines=(
                "1.  The durations between active trading sessions are longer.",
                "2.  The open and close belong to a higher timeframe bar or candlestick.",
                "3.  There is a larger gap between the previous close and the new open.",
            ),
            accent="Any of the three makes the open and close more reliable and actionable.",
            notes=(
                "These three are review question 3. Number them out loud.",
                "Say that the book starts by demoting the open and close and then gives three ways back.",
            ),
        ),
        Figure(
            title="Sessions separated by no trading",
            number="3.8",
            shows="Three trading sessions, each with its own open, high, low and close, separated by stretches of no trading, annotated that longer breaks raise the significance of the open and close.",
            notes=(
                "Point at the shaded blocks. The longer the market is shut, the more its next open means.",
                "This is condition one in a picture.",
            ),
        ),
        Content(
            title="Daily against intraday, and markets that never close",
            lines=(
                "The daily open and close draw more interest than the opens and closes between morning and afternoon sessions.",
                "The break overnight is longer than the break between the two sessions of one day.",
                "In markets that trade continuously, such as spot foreign exchange, the open and close matter less than the high and low.",
            ),
            accent="The longer the market has been shut, the more its opening price means.",
            notes=(
                "Spot foreign exchange trades continuously from Sunday evening to the Friday close. Say that.",
                "A daily open or close is also a higher timeframe than a five minute one. Two conditions at once.",
            ),
        ),
        Check(
            label="Significance of OHLC",
            questions=(
                Q(
                    stem="According to the book, the opening and closing prices are:",
                    options=("Created by the forces of supply and demand",
                             "Merely a function of time stamping",
                             "The most significant prices in a bar",
                             "Areas of price rejection"),
                    answer="B",
                    reason="They mark where an arbitrary interval started and stopped. The high and low are set by traders.",
                ),
                Q(
                    stem="In which market does the book say the opening and closing prices matter less than the high and low?",
                    options=("Spot foreign exchange",
                             "A stock exchange with a lunch break",
                             "Any market on a weekly chart",
                             "Futures near expiry"),
                    answer="A",
                    reason="It trades continuously through the week, so there is no long break to give an open weight.",
                ),
            ),
        ),
        Term(
            term="Gap",
            plain="A stretch of prices where nothing traded at all. Price jumped over it.",
            example="A share closes at 102 pesos and opens the next morning at 106. Nobody traded at 103, 104 or 105 in between.",
            formal="A gap is represented by a range of prices where no trading activity takes place. There are essentially four ways to define one, Types 1 to 4.",
            notes=(
                "Keep the numbers 102 and 106 on the board. The next two slides reuse them.",
                "Four ways to define a gap means four ways to measure the same jump.",
            ),
        ),
        Term(
            term="Type 1 and Type 2 gaps",
            plain="Both are measured to the new bar's open, so both exist the moment it opens.",
            example="The last bar had a high of 104 and closed at 102. The new bar opens at 106. The Type 1 gap, close to open, is 4 pesos. The Type 2 gap, high to open, is 2 pesos.",
            formal="Type 1 is measured from the close of the previous bar to the open of the next or current bar. Type 2 is measured from the high or low of the previous bar to the open of the next or current bar. Both are created instantaneously at the open, with no trading within that range.",
            notes=(
                "Do the two subtractions on the board: 106 minus 102, then 106 minus 104.",
                "For a gap down, swap high for low. The book says high or low for that reason.",
            ),
        ),
        Term(
            term="Type 3 and Type 4 gaps",
            plain="Both are measured to the new bar's high or low, so both wait for it to close.",
            example="The new bar's low turns out to be 105.50. Type 3, high 104 to low 105.50, is 1.50 pesos. Type 4, close 102 to low 105.50, is 3.50 pesos.",
            formal="Type 3 is measured from the highs or lows of the previous bar to the highs or lows of the current bar, and is the gap usually called a window in candlestick and bar charts. Type 4 is measured from the close of the previous bar to the high or low of the next. Both are created only after the current bar has closed.",
            notes=(
                "Window is the name to underline. Type 3 is the gap candlestick readers talk about.",
                "Type 3 means the two bars do not overlap at all. Ask them to check that on the numbers.",
            ),
        ),
        Chart(
            title="The four gaps, measured on one pair of bars",
            letter="A",
            shows="Two bars in pesos, the first with a high of 104 and a close of 102, the second opening at 106 with a low of 105.50, and the four gaps measured between them: 4, 2, 1.50 and 3.50.",
            tier="core",
            notes=(
                "Walk the four brackets from left to right and read each number aloud.",
                "Ask which two brackets end at the open. Those are the two you can see at nine thirty.",
            ),
        ),
        Figure(
            title="Four definitions of a gap",
            number="3.9",
            shows="Four schematic pairs of bars, Types 1 to 4, each gap marked by an arrow; Types 1 and 2 grouped as created when the next bar opens, Types 3 and 4 as needing the next bar to close.",
            notes=(
                "Use the figure's own grouping: left pair at the open, right pair after the close.",
                "Cover the labels and ask them to name each type from the arrow alone.",
            ),
        ),
        Check(
            label="The four gaps",
            questions=(
                Q(
                    stem="The last bar had a high of 104 and closed at 102. The new bar opens at 106. What is the Type 1 gap?",
                    options=("1.50 pesos",
                             "2 pesos",
                             "3.50 pesos",
                             "4 pesos"),
                    answer="D",
                    reason="Type 1 is measured from the previous close to the new open: 106 minus 102.",
                ),
                Q(
                    stem="Which gap is usually referred to as a window in Japanese candlestick and bar charts?",
                    options=("Type 1",
                             "Type 2",
                             "Type 3",
                             "Type 4"),
                    answer="C",
                    reason="Type 3, measured from the previous bar's high or low to the current bar's low or high.",
                ),
            ),
        ),
        Content(
            title="What a gap usually does afterwards",
            lines=(
                "A gap normally represents an area of support or resistance, depending on whether price is above or below it.",
                "This is especially so for a Type 3 gap, and larger gaps are more significant.",
                "Prices are generally expected to return and fill the gap later, although often they do not.",
            ),
            accent="Expected to fill, and often does not. The book says both.",
            caption="The chapter uses support and resistance without defining them. Chapter 5 is where the book defines them.",
            notes=(
                "Read the hedge in line three. Students remember gaps always fill, and the book does not say that.",
                "Do not define support and resistance. Chapter 2 flagged the same two words.",
            ),
        ),
        Content(
            title="The true range, and the Type 4 gap",
            lines=(
                "The book notes that the average true range (ATR) is somewhat related to a Type 4 gap.",
                "The true range is the greater of the new bar's range and the distance from the last close to its high or low.",
                "In the example, last close 102 to new high 108 is 6 pesos, more than the new range of 2.50.",
            ),
            accent="The chapter gives the true range, not the average. The averaging is taught in Chapter 8.",
            notes=(
                "The new bar in the running example has a high of 108 and a low of 105.50. ATR returns in Part 3.",
                "Do not teach how ATR averages. The book leaves that to Chapter 8 and so do we.",
            ),
        ),
        Content(
            title="Four market gaps, named for later",
            lines=(
                "Chapter 5 analyses gaps in relation to market phase.",
                "The four it covers are common gaps, breakaway gaps, runaway gaps and exhaustion gaps.",
                "Runaway gaps are also called continuation or midway gaps.",
            ),
            accent="Names only today. Types 1 to 4 are ways to measure a gap, not kinds of gap.",
            notes=(
                "This slide exists to stop the two lists being confused. Say the accent twice.",
                "Nothing is set on the four names in this chapter.",
            ),
        ),
        Check(
            label="What gaps do",
            questions=(
                Q(
                    stem="Once a gap has formed, the book says prices are generally expected to:",
                    options=("Never return to it",
                             "Return to fill it later, although often they do not",
                             "Fill it before the same bar closes",
                             "Reverse the trend immediately"),
                    answer="B",
                    reason="The book expects a gap to fill and says in the same sentence that many do not.",
                ),
                Q(
                    stem="The last close was 102. The new bar has a high of 108 and a low of 105.50. What is its true range?",
                    options=("2.50 pesos",
                             "3.50 pesos",
                             "6 pesos",
                             "8.50 pesos"),
                    answer="C",
                    reason="The greater of the range, 2.50, and the distance from the last close to the new high, 6.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The open and close as time stamps, the high and low as price rejection",
            "The three conditions that raise the open and close",
            "Daily against intraday, and continuous markets",
            "A gap, and Types 1 to 4",
            "What a gap usually does afterwards, and the true range",
        ),
        notes=(
            "Ask which two gap types exist the moment the market opens. Types 1 and 2.",
            "Next is the biggest part: five ways to decide when a bar is finished.",
        ),
    ),
)

# ==========================================================================
# Part 3 - Five constant measures
# ==========================================================================

PART3 = Section(
    number=3,
    title="Five Constant Measures",
    short="Constant measures",
    minutes="About 40 minutes",
    covers=(
        "The five things that can decide when a bar is finished.",
        "The four constant time charts, and what each one keeps or loses.",
        "The charts that ignore the clock, and the one chart with no constant at all.",
    ),
    slides=(
        Content(
            title="The five constant measures",
            lines=(
                "1.  Constant time: the bar closes when a set interval of time is met.",
                "2.  Constant range: the bar closes when a set excursion in price is met.",
                "3.  Constant volume: the bar closes when a set volume is met.",
                "4.  Constant transaction, or tick: the bar closes when a set number of trades is met.",
                "5.  Constant volatility: the bar closes when a set amount of standard deviation or ATR is met.",
            ),
            caption="Every bar has a range, a duration, a volume, a number of transactions and a volatility. Each chart holds one of them constant.",
            notes=(
                "This list is review question 4. Read all five numbered.",
                "Each chart holds one thing fixed and lets the rest move. That is the whole idea of the part.",
            ),
        ),
        Term(
            term="Constant time chart",
            plain="Every bar covers the same length of time, whatever happened in it.",
            example="On a daily chart, a quiet day and a wild day each get exactly one bar, and each takes up the same width.",
            formal="Constant time charts quantize price activity into units of time, so each bar is complete once a specified amount of time has elapsed; they are also called interval charts. The bar duration is constant, and the range, volume, transactions per bar and volatility are variable.",
            notes=(
                "Interval chart is the second name. Every chart in Part 1 was one of these.",
                "The examples the book gives: candlestick, bar, equivolume and line charts.",
            ),
        ),
        Content(
            title="Why constant time is the default",
            lines=(
                "Constant time charts work with both numerically and geometrically based overlay indicators.",
                "Charts that are not constant time should use numerical and horizontal overlays only.",
                "Their time axis is not linear, which affects trendlines, channels and chart pattern analysis.",
            ),
            accent="Constant time charts are the most popular form of chart construction.",
            caption="The book sorts overlays into numerical, geometrical and horizontal ones and treats them fully in Chapter 8.",
            notes=(
                "Geometric means drawn from points on the chart, like a trendline. Numeric means computed, like a moving average.",
                "This is why a non linear time axis matters: a line between two points depends on the spacing.",
            ),
        ),
        Term(
            term="Bar chart",
            plain="Each interval drawn as one vertical line from high to low, with a small tick on the left for the open and on the right for the close.",
            example="A day that opened at 50, ran up to 52, fell to 49 and closed at 51 is one line from 49 to 52, with a tick on the left at 50 and a tick on the right at 51.",
            formal="A bar chart is created by the quantization of price into specified time intervals. Bar charts clearly depict levels of supply and demand in the market, but the open and close markers are hard to read from a distance when the chart holds many bars.",
            notes=(
                "The ticks are drawn this way in the book's own Figure 3.1. Left open, right close.",
                "Supply and demand again: the high and low are on the bar, so the rejection is visible.",
            ),
        ),
        Term(
            term="Line chart",
            plain="Just the closing prices, joined up. Everything else in each bar is thrown away.",
            example="Five days closing at 50, 51, 50.50, 52 and 53 pesos are five dots joined by a line. The highs and lows of those days do not appear anywhere.",
            formal="Line charts are created by connecting all of the closing prices. They give little information about levels of supply and demand, since they ignore the high and low prices, which are the true indicators of market force. They are used as a trend identifier or a simple summary of price activity.",
            notes=(
                "This is Dow's chart. Only closing prices, which is why it works as a trend identifier.",
                "Past papers ask what a line chart filters out. More than a bar chart does.",
            ),
        ),
        Chart(
            title="What a line chart keeps",
            letter="B",
            shows="Each day's range drawn as a pale bar with its close marked on it and the closes joined into a line; the line never reaches the highs and lows that the pale bars show.",
            tier="enrichment",
            notes=(
                "Point at a tall pale bar and then at where the line crosses it. The extremes are gone.",
                "Say: this is what the line chart threw away, and it is exactly the supply and demand.",
            ),
        ),
        Check(
            label="Constant time, bar and line charts",
            questions=(
                Q(
                    stem="On a constant time chart, which of these is the same for every bar?",
                    options=("The range",
                             "The duration",
                             "The volume",
                             "The volatility"),
                    answer="B",
                    reason="Each bar closes when the set interval of time has elapsed. Everything else varies.",
                ),
                Q(
                    stem="Compared with a bar chart, a line chart:",
                    options=("Shows more about supply and demand",
                             "Needs volume data to construct",
                             "Filters out more of the price information",
                             "Records the high and low of every bar"),
                    answer="C",
                    reason="It keeps only the closes and ignores the highs and lows, the true indicators of market force.",
                ),
            ),
        ),
        Term(
            term="Japanese candlestick",
            plain="A bar with the stretch between the open and the close drawn as a box.",
            example="Open 50, close 51: the box runs from 50 up to 51 and is hollow, or white. Open 51, close 50: the same box, filled, or black.",
            formal="Japanese candlesticks are created in essentially the same manner as price bars. The only difference is that the space between the opening and closing price is boxed up and referred to as the real body, which may be filled or hollow, black or white, depending on where the open lies relative to the close.",
            notes=(
                "Real body is the phrase. The thin lines above and below are the shadows, tails or wicks.",
                "Neither a bar nor a candle tells you whether the high or the low came first. Say that.",
            ),
        ),
        Figure(
            title="A bullish and a bearish candlestick",
            number="3.10",
            shows="A white bullish candlestick and a black bearish one labelled part by part: real body, open, close, and the upper and lower shadows, also called tails or wicks, running to the high and low.",
            notes=(
                "Name each part on the white one, then ask them to name the parts on the black one.",
                "Candlestick formations are classified bullish or bearish, reversal or continuation, simple, double or multiple. Chapter 14.",
            ),
        ),
        Term(
            term="Equivolume chart",
            plain="Each bar's width shows how much traded: a busy day wide, a quiet day narrow.",
            example="Two days with the same high and low. One traded 3 million shares and the other 1 million. The first is drawn as the wider bar.",
            formal="Equivolume charts are based on constant time bars, displaying volume over the interval as bar width rather than height. They are constructed using high and low prices, and open and close prices are disregarded. Larger volume results in a wider bar.",
            notes=(
                "Width, not height. Volume usually lives in a panel underneath; here it is inside the bar.",
                "Do not say how much wider. The book says only that larger volume means a wider bar.",
            ),
        ),
        Content(
            title="Equivolume: constant time, non linear axis, two accounts",
            lines=(
                "Every equivolume bar still covers one interval of time, so it is a constant time chart.",
                "But because the widths vary, its time axis is not plotted in a linear fashion.",
                "The book says equivolume needs OHLCV data, and also that its open and close are disregarded.",
            ),
            accent="What the bar actually draws on is the high, the low and the volume.",
            caption="The book says both things about its data. Learn both, and know which prices the bar uses.",
            notes=(
                "Constant time with a non linear time axis is a favourite trap. Trendlines distort on it.",
                "Name the inconsistency and move on. No check rests on OHLCV against HLV.",
            ),
        ),
        Figure(
            title="Candlestick and equivolume, same stock",
            number="3.11",
            shows="The same daily prices of Apple Inc. as a candlestick chart with a linear time axis and as an equivolume chart with a non linear one, the trendline on each ending at a different price.",
            notes=(
                "Look along the bottom axis of each. Even spacing on top, uneven below.",
                "Then point at where the two trendlines end. Same prices, different lines.",
            ),
        ),
        Check(
            label="Candlesticks and equivolume",
            questions=(
                Q(
                    stem="The space between the opening and closing price of a candlestick is called:",
                    options=("The real body",
                             "The shadow",
                             "The range",
                             "The wick"),
                    answer="A",
                    reason="The body is boxed up between the open and the close. Shadows run out to the high and low.",
                ),
                Q(
                    stem="Which of these is true of an equivolume chart?",
                    options=("Volume is shown as bar height",
                             "It is not a constant time chart",
                             "Its bars are built from the open and the close",
                             "Its time axis is not plotted in a linear fashion"),
                    answer="D",
                    reason="Each bar covers one interval, but the varying widths make the time axis non linear.",
                ),
            ),
        ),
        Term(
            term="Constant range chart",
            plain="A chart that draws a new bar only when price has moved a set amount, however long that takes.",
            example="Set the size at 1 peso. A share that drifts 40 centavos all week draws nothing. A share that moves 3 pesos in a morning draws three.",
            formal="On constant range charts each bar, box or brick is complete once a specified excursion in price is met. The bar range and the bar volatility are constant; the duration, volume and transactions per bar are variable.",
            notes=(
                "Time has dropped out completely. A quiet week can be invisible on this chart.",
                "The two examples the book gives are point and figure and Renko. Next two terms.",
            ),
        ),
        Term(
            term="Point and figure chart",
            plain="Columns of X's while price rises and O's while it falls, one box per set move.",
            example="Box size 1 peso, reversal size 3 boxes. Price must move 1 peso to add a box, and at least 3 pesos against the column before a new column starts.",
            formal="The most popular form of constant range charting. A continuation box is the minimum excursion for a new box in the trend's direction; the reversal size is the number of boxes needed to plot a reversal. The box size is arbitrarily chosen, and closing prices are normally used, though many use the high and low.",
            notes=(
                "Do the arithmetic: 3 boxes of 1 peso is a 3 peso reversal. It is asked directly.",
                "Arbitrarily chosen is the book's phrase. There is no correct box size.",
            ),
        ),
        Chart(
            title="Point and figure, one box at a time",
            letter="C",
            shows="A price path and, below it, the point and figure columns it makes with a 1 peso box and a 3 box reversal: X's while price rises, O's while it falls, a new column only after a 3 peso reversal.",
            tier="core",
            notes=(
                "Follow the price path with a finger and add a box each time it moves a full peso.",
                "Stop at the first reversal and count: three boxes against the column, then the new column.",
            ),
        ),
        Content(
            title="Why point and figure draws its lines at 45 degrees",
            lines=(
                "As a constant range chart, point and figure has a non linear time axis.",
                "So geometrically based overlays would give inconsistent readings on it.",
                "Its trendlines need only one point, and rise and fall along 45 and minus 45 degree angles.",
            ),
            accent="Point and figure uses bullish support and bearish resistance lines in place of conventional trendlines.",
            notes=(
                "One point, not two. That is the whole difference from a conventional trendline.",
                "This is the Part 1 idea of an implicit time axis doing real work.",
            ),
        ),
        Figure(
            title="Point and figure on Google",
            number="3.12",
            shows="A point and figure chart of Google Inc. in columns of X's and O's, with a plus 45 degree line under the rise and a minus 45 degree line over the decline, and the note that the time axis is non linear.",
            notes=(
                "Find one X column and one O column. Then find the two 45 degree lines.",
                "Read the date labels along the bottom and point at how unevenly they are spaced.",
            ),
        ),
        Term(
            term="Renko chart",
            plain="White bricks for each set rise, black for each set fall, one column per brick.",
            example="Brick size 1 peso. From 50, a rise to 52.40 adds two white bricks. For a black brick, price must now move at least two bricks, 2 pesos, the other way.",
            formal="A form of constant range charting whose bars are bricks, bullish white and bearish black, each plotted in a new column once the minimum price excursion is met. All reversals require price to move at least two bricks the other way, so Renko charts are essentially two brick reversal charts. Brick size is arbitrary.",
            notes=(
                "Compare with point and figure: every brick gets its own column, and the reversal is two bricks.",
                "The 40 centavos above 52 do nothing. Only whole bricks are drawn.",
            ),
        ),
        Figure(
            title="A Renko chart",
            number="3.13",
            shows="A Renko chart of the iPath Dow Jones-AIG Coffee Total Return Sub-Index in white and black bricks, with the note that its time axis is non linear.",
            notes=(
                "Point at a run of white bricks and then the first black one. At least two bricks against.",
                "Again, read the dates along the bottom. Months are squeezed and stretched.",
            ),
        ),
        Check(
            label="Point and figure and Renko",
            questions=(
                Q(
                    stem="A point and figure chart uses a 1 peso box and a 3 box reversal. How far must price move against the current column before a reversal is plotted?",
                    options=("1 peso",
                             "2 pesos",
                             "3 pesos",
                             "4 pesos"),
                    answer="C",
                    reason="Three boxes of 1 peso each.",
                ),
                Q(
                    stem="Renko charts are essentially:",
                    options=("One brick reversal charts",
                             "Two brick reversal charts",
                             "Three line break charts",
                             "Constant time charts"),
                    answer="B",
                    reason="All Renko reversals need price to move at least two bricks the other way.",
                ),
            ),
        ),
        Term(
            term="Constant volume chart",
            plain="A new bar every time a set number of shares has traded, however long that takes.",
            example="Set 100,000 shares a bar. A busy morning might draw ten bars; a slow afternoon might draw one.",
            formal="In constant volume charts a new bar is plotted once the minimum volume traded is met. The bar volume is constant; the range, duration, transactions per bar and volatility are variable. Since a new bar is not time dependent, the time axis is plotted in a non linear fashion.",
            notes=(
                "The book gives no figure of this one. The chart after this slide is ours.",
                "Busy stretches get many bars and quiet ones get few. The chart stretches the busy hours.",
            ),
        ),
        Chart(
            title="Where a constant volume bar closes",
            letter="D",
            shows="One session's price above its volume, with a mark on the time axis wherever another fixed block of shares has traded: the marks crowd together in the busy hours and spread out in the quiet ones.",
            tier="reinforcement",
            notes=(
                "Each mark is where one constant volume bar would close. Count how many fall in the first hour.",
                "Then count the quiet middle of the day. Same number of shares per bar, very different time.",
            ),
        ),
        Term(
            term="Constant transaction chart",
            plain="A new bar after every set number of trades. Also called a tick chart.",
            example="Set 50 trades a bar. Fifty trades of 100 shares and fifty trades of 10,000 shares each make exactly one bar.",
            formal="In constant transaction or tick charts a new bar is plotted once the minimum number of transactions is met. Each transaction is represented by one tick, and the volume per transaction is unspecified. The transactions per bar are constant; everything else is variable, and the time axis is non linear.",
            notes=(
                "One tick is one trade. Five ticks, five trades, whatever their size.",
                "Unspecified volume is the point: a tick chart does not care how big each trade was.",
            ),
        ),
        Term(
            term="Constant volatility chart",
            plain="Like constant range, but volatility sets the size of move each bar needs.",
            example="Set each bar at 2 x ATR. If the ATR is 0.50 pesos a bar needs a 1 peso move; if the ATR widens to 1.50, it needs 3 pesos.",
            formal="A new bar is plotted once a minimum price excursion determined by volatility is met, for example 2 x ATR. The bar volatility is constant; range, duration, volume and transactions are variable. It is objective, as volatility sets the size, and subjective in the choice of the ATR multiple.",
            notes=(
                "Do the two multiplications on the board. 2 times 0.50, then 2 times 1.50.",
                "Objective and subjective at once. The market sets the unit, you still choose the multiple.",
            ),
        ),
        Figure(
            title="ATR box sizing against standard box sizing",
            number="3.14",
            shows="Two point and figure charts of one market: box size set to 1 x ATR on the left, less volatile and more directional; standard box sizing on the right, more volatile and less directional.",
            notes=(
                "Read the two annotations off the figure. The book prefers the left one for spotting trends.",
                "Same market, same kind of chart. Only the way the box size was chosen differs.",
            ),
        ),
        Check(
            label="Volume, tick and volatility charts",
            questions=(
                Q(
                    stem="Which chart plots a new bar once a set number of transactions has taken place?",
                    options=("A constant volume chart",
                             "A constant range chart",
                             "A constant volatility chart",
                             "A constant transaction chart"),
                    answer="D",
                    reason="Constant transaction, or tick, charts count trades, whatever the size of each one.",
                ),
                Q(
                    stem="A constant volatility chart sets each bar at 2 x ATR. The ATR is 0.50 pesos. How far must price move to complete a bar?",
                    options=("0.25 peso",
                             "0.50 peso",
                             "1 peso",
                             "2 pesos"),
                    answer="C",
                    reason="Two multiples of an ATR of 0.50 pesos.",
                ),
            ),
        ),
        Term(
            term="Three line break chart",
            plain="No fixed measure at all: a new line only when price closes beyond the last one.",
            example="After three white lines in a row, price has to fall to the low of those last three lines before a black line can be drawn.",
            formal="Three line break charts possess no measures of constancy. Once price closes above the previous high or below a previous low, a new line is created. After three successive lines, a reversal may only be plotted if price meets or exceeds the low, or in an upside reversal the high, of the last three.",
            notes=(
                "Unique is the book's word for it: the only construct in the chapter with nothing held constant.",
                "Bullish lines are white and bearish lines are black, as with Renko bricks.",
            ),
        ),
        Figure(
            title="Three line break against Renko",
            number="3.15",
            shows="The same period of the Currency Shares Euro Trust drawn as a Renko chart and as a three line break chart side by side.",
            notes=(
                "Ask what the two charts agree on. The big turns appear on both.",
                "Then point at how differently they space the same months.",
            ),
        ),
        Content(
            title="Which one each chart holds constant",
            lines=(
                "Constant time: the duration.",
                "Constant range: the range, and the volatility.",
                "Constant volume: the volume.",
                "Constant transaction: the number of transactions per bar.",
                "Constant volatility: the volatility.",
                "Three line break: nothing at all.",
            ),
            caption="The book lists volatility as constant for both constant range and constant volatility charts. What separates them is how the size is set.",
            notes=(
                "This is the slide to photograph. Everything not named on a line is variable.",
                "Past papers ask which is not variable on a constant volatility chart. The volatility.",
            ),
        ),
        Check(
            label="Which measure is constant",
            questions=(
                Q(
                    stem="Which chart possesses no measures of constancy at all?",
                    options=("A Renko chart",
                             "A three line break chart",
                             "A tick chart",
                             "An equivolume chart"),
                    answer="B",
                    reason="Range, duration, volume, transactions and volatility are all variable on a three line break chart.",
                ),
                Q(
                    stem="On which of these is the time axis plotted in a non linear fashion? I. Bar chart. II. Point and figure chart. III. Line chart. IV. Constant volume chart.",
                    options=("Only I and III",
                             "Only II and IV",
                             "Only IV",
                             "All are correct"),
                    answer="B",
                    reason="Bar and line charts are constant time with a linear axis. The other two do not run on time.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The five constant measures",
            "Constant time: bar, line, candlestick and equivolume charts",
            "Constant range: point and figure and Renko",
            "Constant volume, constant transaction and constant volatility",
            "Three line break, with nothing constant",
            "Why a non linear time axis bends trendlines",
        ),
        notes=(
            "Ask what a constant range chart holds constant. You want range, and volatility.",
            "Next: the price axis. Same prices, three ways to space them.",
        ),
    ),
)

# ==========================================================================
# Part 4 - Chart scaling
# ==========================================================================

PART4 = Section(
    number=4,
    title="Chart Scaling",
    short="Scaling",
    minutes="About 25 minutes",
    covers=(
        "Three ways to scale a price axis, and what each one preserves.",
        "Which overlays scaling changes, and which it leaves alone.",
        "Why the same prices can look bullish on one scale and bearish on the other.",
    ),
    slides=(
        Content(
            title="Three ways to scale a price axis",
            lines=(
                "1.  Linear, or arithmetic, scale.",
                "2.  Ratio, or logarithmic, scale.",
                "3.  Square root scale.",
            ),
            accent="Linear and ratio are the common two. Square root lies between them and is rarely offered.",
            notes=(
                "Chapter 2 called the first two arithmetic and logarithmic. Same things, the book uses both names.",
                "Chapter 2 gave the signal timing. This part gives the arithmetic behind it.",
            ),
        ),
        Term(
            term="Linear scaling",
            plain="Equal distances up the chart mean equal amounts of money.",
            example="A rise from 10 to 20 pesos and a rise from 90 to 100 pesos are drawn the same height: 10 pesos each. But the first is a 100 percent rise and the second only 11.1 percent.",
            formal="In linear or arithmetic scaling, equal distances on the chart represent equal price changes: the change P(N) minus P(N-1) is constant for every equal distance moved on the chart. The percentage change is not preserved for equal units of price change.",
            notes=(
                "Do the division on the board: 10 over 90 is 11.1 percent.",
                "Same height, very different importance to the person holding the share.",
            ),
        ),
        Term(
            term="Ratio scaling",
            plain="Equal distances up the chart mean equal percentage moves.",
            example="A rise from 10 to 20 pesos is 100 percent. On a ratio scale it is drawn the same height as a rise from 90 to 180 pesos, which is also 100 percent but a 90 peso move.",
            formal="In ratio or logarithmic scaling, equal distances on the chart represent equal percentage changes: (P(N) minus P(N-1)) divided by P(N-1) is constant for every equal distance moved, which is also what is called stock returns. The price change is not preserved per equal unit of percentage change.",
            notes=(
                "Stock returns is the phrase to link it to finance they already know.",
                "Ratio preserves the percentage and gives up the peso amount. Linear does the reverse.",
            ),
        ),
        Content(
            title="One sentence in the book says the opposite",
            lines=(
                "The book defines ratio scaling as equal distances for equal percentage changes.",
                "Two sentences later it says equal distances on the chart do not equate to equal percentage changes.",
                "That sentence contradicts the definition just given, which the book states twice and draws twice.",
            ),
            accent="Learn the definition. Equal distance on a ratio scale is equal percentage change.",
            notes=(
                "Name it plainly and move on. Textbooks have errors and this is one.",
                "No check rests on the stray sentence. Every check uses the definition.",
            ),
        ),
        Chart(
            title="One price axis, three scales",
            letter="E",
            shows="Price levels from 10 to 100 pesos on a linear, a square root and a ratio axis side by side, with the rises from 10 to 20 and from 90 to 100 marked on each.",
            tier="core",
            notes=(
                "Start with the left axis: evenly spaced. Then the right: bunched at the top.",
                "The middle one is square root. Say it sits between, which is all the book claims.",
            ),
        ),
        Figure(
            title="Linear scaling",
            number="3.16",
            shows="A price axis from 0 to 6 dollars with each 1 dollar step the same height, annotated that the price changes are constant from level to level and are of equal distances on the chart.",
            notes=(
                "Every one dollar step is the same height. That is the whole of linear scaling.",
                "Ask what percentage the step from 1 to 2 is, and the step from 5 to 6.",
            ),
        ),
        Figure(
            title="Ratio scaling, and where the halfway point falls",
            number="3.17",
            shows="A ratio scaled axis from 10 to 100 with the log of each level beside it: 55, the arithmetic halfway point, sits well above the middle, and prices are compressed at the upper end.",
            notes=(
                "The log of 55 is 1.74, above the midpoint of 1.50. So 55 sits high on the axis.",
                "That is compression at the upper end, in numbers.",
            ),
        ),
        Figure(
            title="Ratio scaling, in equal percentage steps",
            number="3.18",
            shows="A ratio scaled axis doubling from 1 to 64 dollars, every doubling the same height and 0.3 apart in logs, annotated that equal distances are equal percentage changes.",
            notes=(
                "Each doubling is the same height: 2 to 4, 4 to 8, 32 to 64.",
                "This figure and 3.17 make the same point. If time is short, show this one.",
            ),
        ),
        Check(
            label="Linear and ratio",
            questions=(
                Q(
                    stem="On a linear scale, a rise from 10 to 20 pesos and a rise from 90 to 100 pesos:",
                    options=("Are drawn the same height",
                             "Represent the same percentage change",
                             "Cannot be shown on one chart",
                             "Are drawn the same height only on a weekly chart"),
                    answer="A",
                    reason="Equal price changes, equal distances. Their percentages are 100 and 11.1.",
                ),
                Q(
                    stem="On a ratio scale, a rise from 10 to 20 pesos is drawn the same height as a rise from 90 to:",
                    options=("100 pesos",
                             "110 pesos",
                             "135 pesos",
                             "180 pesos"),
                    answer="D",
                    reason="Both are 100 percent rises, and equal percentage changes are equal distances on a ratio scale.",
                ),
            ),
        ),
        Content(
            title="Compressed at the top, expanded at the bottom",
            lines=(
                "The ratio scale compresses price action at higher prices and expands it at lower prices.",
                "Linear scaling represents price evenly across the whole range.",
                "So linear gives better definition at the upper end, and ratio gives better definition at the lower end.",
            ),
            accent="Each scale is clear at one end and poor at the other.",
            notes=(
                "Relate it to the axis they just saw: the top of the ratio axis is crowded.",
                "Past papers invert this. The ratio scale compresses the top, not the bottom.",
            ),
        ),
        Content(
            title="Which scale to use",
            lines=(
                "Use linear when the price range under observation is relatively small.",
                "For stock price ranges exceeding 100 dollars ratio may be more appropriate, and it is best for very long term equity charts.",
                "For futures, foreign exchange and anything traded on very low margin, use linear.",
            ),
            accent="Ratio would compress those highly leveraged markets too much at higher prices.",
            caption="The book gives the 100 dollar threshold without saying whether it means the price or the distance from low to high.",
            notes=(
                "Say the guideline is the book's, and that it calls it a general guideline, not a rule.",
                "Name the ambiguity in the threshold. No check rests on it.",
            ),
        ),
        Term(
            term="Square root scale",
            plain="A third way to scale the axis, lying between linear and ratio.",
            example="Equal price steps get shorter as price rises, but not as much shorter as they do on a ratio scale.",
            formal="The square root scale lies somewhere between the linear and ratio scales with respect to its scale increments, and is not commonly used on most platforms. It indicates an uptrend line penetration later than ratio scaling but earlier than linear scaling.",
            notes=(
                "The book calls that rather disconcerting: most traders react on linear or ratio charts.",
                "So a square root user enters and exits too early or too late relative to everyone else.",
            ),
        ),
        Check(
            label="Choosing a scale",
            questions=(
                Q(
                    stem="According to the book, ratio scaling provides:",
                    options=("Better definition at the upper end of prices",
                             "Equal definition across the whole range",
                             "Better definition at the lower end of prices",
                             "No definition of volatility"),
                    answer="C",
                    reason="It compresses higher prices and expands lower ones, so the lower end is clearer.",
                ),
                Q(
                    stem="Which scale does the book recommend for futures and highly leveraged foreign exchange?",
                    options=("Linear",
                             "Ratio",
                             "Square root",
                             "Logarithmic"),
                    answer="A",
                    reason="Ratio would compress price too much at higher prices in markets traded on very low margin.",
                ),
            ),
        ),
        Content(
            title="What scaling changes, and what it does not",
            lines=(
                "Geometric overlays are affected: trendlines, channels and chart patterns. Change the scale and every angle changes.",
                "Numerical overlays are not affected: moving averages and price envelopes.",
                "Horizontal overlays are not affected: prior support and resistance, Fibonacci levels, and Gann retracements and Square of Nine projections.",
            ),
            accent="Geometry moves with the scale. Computed values and horizontal levels do not.",
            caption="The chapter only names these overlays. Each one is taught later in the book.",
            notes=(
                "This is review question 5 in one slide.",
                "A horizontal line is the same price on any scale. That is why it survives.",
            ),
        ),
        Content(
            title="Trendlines break at different times",
            lines=(
                "On ratio charts, uptrend lines are penetrated sooner and downtrend lines later.",
                "On linear charts, uptrend lines are penetrated later and downtrend lines sooner.",
            ),
            accent="Chapter 2 gave you the uptrend half. This is the whole rule.",
            notes=(
                "Say it as a pair: ratio, up sooner, down later. Linear, up later, down sooner.",
                "The book uses trendline without defining it here. Chapter 5 is trend analysis.",
            ),
        ),
        Figure(
            title="Uptrend lines on the two scales",
            number="3.19",
            shows="The SPDR Dow Jones Industrial Average on an arithmetic and on a logarithmic scale side by side, with the uptrend line penetrated later on the arithmetic chart and sooner on the logarithmic one.",
            notes=(
                "Find the crossing on the right hand chart first. It comes earlier.",
                "Same prices. The scale moved the signal.",
            ),
        ),
        Figure(
            title="Downtrend lines on the two scales",
            number="3.20",
            shows="The U.S. Natural Gas Fund on an arithmetic and on a logarithmic scale side by side, with the downtrend line penetrated sooner on the arithmetic chart and later on the logarithmic one.",
            notes=(
                "The mirror of the last figure. On a decline, linear signals first.",
                "If time is short, skip this one. The rule is on the slide before.",
            ),
        ),
        Check(
            label="Overlays and trendlines",
            questions=(
                Q(
                    stem="Switching a chart from linear to ratio scaling will change the reading of:",
                    options=("A moving average",
                             "A prior support level",
                             "A trendline",
                             "A Fibonacci retracement"),
                    answer="C",
                    reason="A trendline is geometric. Moving averages are numerical and the other two are horizontal.",
                ),
                Q(
                    stem="Which pair describes a linear scaled chart?",
                    options=("Uptrend lines penetrated sooner, downtrend lines later",
                             "Uptrend lines penetrated later, downtrend lines sooner",
                             "Both penetrated sooner",
                             "Both penetrated later"),
                    answer="B",
                    reason="The reverse of the ratio chart, where uptrend lines break sooner.",
                ),
            ),
        ),
        Content(
            title="The same prices can look bullish or bearish",
            lines=(
                "Rising, ratio chart: decelerating, concave, a rounding top. Bearish.",
                "Falling, ratio chart: accelerating, convex, a parabolic decline. Bearish.",
                "Rising, linear chart: accelerating or even, convex, parabolic. Bullish.",
                "Falling, linear chart: decelerating, concave, a rounding bottom. Bullish.",
            ),
            accent="Ratio makes both directions look bearish. Linear makes both look bullish.",
            notes=(
                "Read the four lines, then give them the accent line as the thing to remember.",
                "The book says may take on an appearance. The prices did not change their meaning.",
            ),
        ),
        Figure(
            title="A123 Systems on both scales",
            number="3.21",
            shows="The same decline in A123 Systems Inc. on a semilog scale, where it takes a convex, parabolic and bearish appearance, and on a linear scale, where it takes a concave and more bullish appearance.",
            notes=(
                "Semilog is another name the book uses for a ratio scale. Say so.",
                "Point at the shape of the decline on each. Convex above, concave below.",
            ),
        ),
        Figure(
            title="Apple on both scales",
            number="3.22",
            shows="The same advance in Apple Inc. on a ratio chart, where it appears to flatten out with a bearish appearance, and on a linear chart, where it does not flatten and appears bullish.",
            notes=(
                "Chapter 2 showed this stock flattening too. Here the book names the shape: concave.",
                "Ask which chart a nervous holder would rather not look at.",
            ),
        ),
        Figure(
            title="Channels drawn on both scales",
            number="3.23",
            shows="Energy Services of America Corp. on semilog and linear charts: channels drawn from the same inflection points land in different places, while the moving average reads the same on both.",
            notes=(
                "Read the two lines of text on the figure: geometric overlays affected, numerical not.",
                "This figure repeats the overlay slide. It is on the first cut.",
            ),
        ),
        Check(
            label="Appearances",
            questions=(
                Q(
                    stem="On a ratio scaled chart, rising prices may take on:",
                    options=("A bearish appearance, decelerating like a rounding top",
                             "A bullish appearance, accelerating like a parabolic move",
                             "A bullish appearance, rising evenly",
                             "No change in appearance"),
                    answer="A",
                    reason="Ratio charts compress higher prices, so a rise decelerates in a concave curve.",
                ),
                Q(
                    stem="On a linear scaled chart, falling prices may take on:",
                    options=("A bearish appearance, accelerating like a parabolic move",
                             "A bearish appearance, like a rounding top",
                             "No change in appearance",
                             "A bullish appearance, decelerating like a rounding bottom"),
                    answer="D",
                    reason="Linear makes a decline decelerate in a concave curve, which looks like a rounding bottom.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Linear, ratio and square root scaling",
            "What each scale preserves, and where each is clearer",
            "Which scale for which market",
            "Geometric overlays move with the scale; numerical and horizontal ones do not",
            "Trendline penetration on each scale",
            "Four appearances of the same prices",
        ),
        notes=(
            "Ask for the one line summary: ratio makes both look bearish, linear makes both look bullish.",
            "Next: the price the chart shows is not the price you pay.",
        ),
    ),
)

# ==========================================================================
# Part 5 - The bid-ask spread
# ==========================================================================

PART5 = Section(
    number=5,
    title="The Bid-Ask Spread",
    short="Bid-ask spread",
    minutes="About 20 minutes",
    covers=(
        "Why most charts are drawn on the bid, and what that does to a buyer.",
        "Expensive longs, early longs and late longs.",
        "How the spread bends the reward to risk ratio, and how to shrink its cost.",
    ),
    slides=(
        Term(
            term="Bid-ask spread",
            plain="The gap between the price you can sell at, the bid, and the higher price you must pay to buy, the ask.",
            example="Bid 10.00 pesos, ask 10.20 pesos. The spread is 20 centavos, and every trade that buys and then sells pays it.",
            formal="The bid-ask spread is the price difference between the bid and the ask price. A buy must accept the ask price and a sell is made at the bid. Since a trade consists of a buy and a sell, the bid-ask spread affects all trades.",
            notes=(
                "The book's worked examples are in dollars. We use pesos; the arithmetic is identical.",
                "Keep 10.00 and 10.20 on the board. Every example in this part uses them.",
            ),
        ),
        Content(
            title="Charts are usually drawn on the bid",
            lines=(
                "Charts are typically drawn on bid prices, though many platforms can also draw the ask or the mid price.",
                "On a bid-based chart, performance is adversely affected when initiating long entries and executing long exits.",
                "The book says it does not specifically affect short entries or short exits.",
            ),
            accent="Selling happens at the bid, which is the price the chart shows. Buying does not.",
            caption="The book defines shorting here as selling to open or close a position. Read long the same way, as any buy, or its rule contradicts its own example.",
            notes=(
                "This is the one place the chapter's wording is confusing. Name it and read long as buy.",
                "A long exit in the book's sense is a buy that closes a short. It pays the ask.",
            ),
        ),
        Figure(
            title="Shorting resistance at the bid",
            number="3.24",
            shows="A price rising to a 10.00 dollar resistance level on a bid-based chart, the ask 20 cents above at 10.20, and the short entered at the bid at exactly the level intended.",
            notes=(
                "Price tests 10.00 on the bid chart, you sell at market, you get 10.00, slippage aside.",
                "A sell limit at 10.00 fills there or better. Same answer if the sell is a stop loss or a target.",
            ),
        ),
        Term(
            term="Expensive longs",
            plain="You buy at exactly the right moment on the chart, and still pay more than the chart showed.",
            example="The breakout level is 10.00 and you plan to buy at 10.05. Price touches 10.05 on the bid chart, you buy at market, and you are filled at the ask, 10.25.",
            formal="The problem of the expensive longs: a long initiated with a market order at precisely the right time on a bid-priced chart is nevertheless bought at a higher price than intended, because a buy must accept the ask price.",
            notes=(
                "Right time, wrong price. Say that as the one line summary.",
                "10.05 plus the 20 centavo spread is 10.25. Do the addition on the board.",
            ),
        ),
        Figure(
            title="Going long at the breakout",
            number="3.25",
            shows="A price breaking up through a 10.00 dollar resistance level, with the long entered as price reaches 10.05 on the bid chart and filled at the ask of 10.25, twenty cents above.",
            notes=(
                "Point at the gap between the two horizontal lines. That is the spread you paid.",
                "The chart said 10.05. The account says 10.25.",
            ),
        ),
        Term(
            term="Early longs",
            plain="You use a pending buy order so the price is exact, and it fills before the breakout has really happened on the chart.",
            example="A buy stop at 10.05 fills at 10.05, which is the ask. At that moment the bid is 9.85, still below the 10.00 breakout level.",
            formal="The problem of the early longs: a buy stop entry order is filled at the intended price, the ask, while the bid is still below the breakout level, so the trader has bought into the position before the breakout on the bid-priced chart.",
            notes=(
                "Right price, wrong time. The mirror of the last term.",
                "So on a breakout you choose: pay more, or buy early. The book says either way the spread costs you.",
            ),
        ),
        Check(
            label="Expensive and early longs",
            questions=(
                Q(
                    stem="The spread is 20 centavos. You buy at market the moment the bid chart touches 10.05. You are most likely filled at:",
                    options=("9.85",
                             "10.05",
                             "10.25",
                             "10.45"),
                    answer="C",
                    reason="A buy accepts the ask, 20 centavos above the bid. This is the expensive longs.",
                ),
                Q(
                    stem="A buy stop at 10.05 fills at 10.05 while the bid is 9.85, below the 10.00 breakout. The book calls this the problem of:",
                    options=("The late longs",
                             "The early longs",
                             "The expensive longs",
                             "Negative slippage"),
                    answer="B",
                    reason="Filled at the intended price, but before the breakout on the bid chart.",
                ),
            ),
        ),
        Term(
            term="Late longs",
            plain="You try to buy at support with a pending order, and it fills only after the bid has already broken below support.",
            example="Support is at 10.00. A pending order to buy at 10.00 fills at the ask of 10.00, but the bid is then 9.80: support had already been breached.",
            formal="The problem of the late longs: a pending order to buy at a support level is filled at the intended price, the ask, only when the bid is already below the support level on the bid-priced chart.",
            notes=(
                "A breakout makes you early, a support level makes you late. Same spread, both times.",
                "If you buy at market at support instead, you are filled at 10.20. That is expensive longs again.",
            ),
        ),
        Content(
            title="Two ways to buy support, and both cost",
            lines=(
                "Buy at market as price tests support at 10.00, and you are filled at the ask, 10.20: expensive longs again.",
                "Use a pending order instead, and you get 10.00, but only after support has broken on the bid chart: late longs.",
            ),
            accent="At a breakout the pending order is early. At support it is late.",
            caption="Figure 3.26 labels its level a resistance level. Its own title and the text call it support. Read it as support.",
            notes=(
                "The label on the figure is an error in the book. Say so before you show it.",
                "Market order: pay more. Pending order: wrong moment. That is the part in two lines.",
            ),
        ),
        Figure(
            title="Going long at support",
            number="3.26",
            shows="Price falling back to a 10.00 dollar level, ask 10.00 and bid 9.80, the long filled at the ask by a pending order once the bid is below the level. The figure labels the level resistance.",
            notes=(
                "Point at the bid line below the level. That is where the market really was when you bought.",
                "Say again that the label should read support.",
            ),
        ),
        Check(
            label="Buying at support",
            questions=(
                Q(
                    stem="A pending order to buy at a 10.00 support level fills at 10.00 while the bid is already 9.80. This is the problem of:",
                    options=("The late longs",
                             "The early longs",
                             "The expensive longs",
                             "Positive slippage"),
                    answer="A",
                    reason="The order filled at the intended price, but only after support had broken on the bid chart.",
                ),
                Q(
                    stem="With a 20 centavo spread, you buy at market as the bid chart tests support at 10.00. You are filled at:",
                    options=("9.80",
                             "10.00",
                             "10.10",
                             "10.20"),
                    answer="D",
                    reason="A market buy accepts the ask, 20 centavos above the bid.",
                ),
            ),
        ),
        Content(
            title="The spread and the reward to risk ratio",
            lines=(
                "The spread increases the probability of exiting at the stop loss: loss promoting.",
                "It reduces the probability of exiting at the profit target: profit restricting.",
                "With a market order it is deducted from the profit and added to the loss, and shows in the account.",
            ),
            accent="Bid 1.00, spread 0.20, bought at 1.20. Target 1.50 and stop 0.50 give 0.30 against 0.70: an R/r of 0.43, not 1.",
            notes=(
                "Do the example slowly. Profit 1.50 minus 1.20 is 0.30. Loss 1.20 minus 0.50 is 0.70.",
                "0.30 divided by 0.70 is 0.43. The trade looked like one to one and it is not.",
            ),
        ),
        Figure(
            title="Market order long entries",
            number="3.27",
            shows="A long bought when the bid was 1.00 dollar and filled at the ask of 1.20, stop 0.50 and target 1.50: expected R/r of 0.50/0.50 = 1 against a spread adjusted 0.30/0.70 = 0.43.",
            notes=(
                "Point at the two boxes on the right: expected, then spread adjusted.",
                "Loss promoting on the left arrow, profit restricting on the right one.",
            ),
        ),
        Content(
            title="With a pending order the cost is hidden",
            lines=(
                "The spread is not deducted from the profit or added to the loss, and does not show in the account.",
                "Instead price has to travel further to reach the profit, and less far to reach the stop.",
                "The expected R/r ratio is unchanged, but the probability of a winning trade falls.",
            ),
            accent="Same ratio on paper. Worse odds in the market.",
            notes=(
                "Hidden is the book's word. The cost is still there, it just moved.",
                "Ask which is worse, a cost you can see or one you cannot. Let them argue it.",
            ),
        ),
        Figure(
            title="Pending order long entries",
            number="3.28",
            shows="A long bought at the ask of 1.00 dollar by pending order while the bid is 0.80, stop 0.50 and target 1.50: R/r stays 1, but price must rise 0.70 to win and fall only 0.30 to lose.",
            notes=(
                "Read the two distances: 0.70 up to win, 0.30 down to lose.",
                "The ratio still says one to one. The distances say otherwise.",
            ),
        ),
        Content(
            title="How to shrink the spread's cost",
            lines=(
                "Increase the size of the target and the stop relative to the spread.",
                "The obvious way is to trade a higher timeframe, or a larger wave cycle.",
                "Scalpers need to buy at the bid and sell at the ask, which a standard level one (L1) platform will not allow.",
            ),
            accent="The spread hurts the short term trader most, and the scalper above all.",
            notes=(
                "A 20 centavo spread on a 5 peso target is small. On a 30 centavo target it is most of it.",
                "Wave cycle and level one platform are the book's words and are not defined further here.",
            ),
        ),
        Check(
            label="The spread and R/r",
            questions=(
                Q(
                    stem="You buy at market when the bid is 1.00 and the spread is 0.20, with a target of 1.50 and a stop of 0.50. The spread adjusted reward to risk ratio is:",
                    options=("0.30",
                             "0.43",
                             "0.70",
                             "1.00"),
                    answer="B",
                    reason="Bought at 1.20: a profit of 0.30 against a loss of 0.70, and 0.30 over 0.70 is 0.43.",
                ),
                Q(
                    stem="The book's most obvious way to reduce the relative cost of the spread is to:",
                    options=("Trade a higher timeframe or a larger wave cycle",
                             "Use market orders only",
                             "Trade a lower timeframe",
                             "Switch to a line chart"),
                    answer="A",
                    reason="The larger the target and stop, the smaller the spread is relative to them.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The bid-ask spread, and the bid-based chart",
            "Expensive longs, early longs and late longs",
            "Loss promoting and profit restricting",
            "The spread adjusted R/r ratio, and the hidden cost of a pending order",
            "Why the spread hurts the scalper most",
        ),
        notes=(
            "Ask for the three problems in one line each: pay more, too early, too late.",
            "Last part: futures, where the chart itself has to be stitched together.",
        ),
    ),
)

# ==========================================================================
# Part 6 - Futures contracts
# ==========================================================================

PART6 = Section(
    number=6,
    title="Futures Contracts",
    short="Futures",
    minutes="About 35 minutes",
    covers=(
        "Why futures exist, why they expire, and which contract to trade.",
        "Rolling over at a premium or a discount, contango and backwardation.",
        "Three ways to chart a string of contracts, and what each one costs you.",
    ),
    slides=(
        Content(
            title="What futures were created for",
            lines=(
                "Futures were originally created to let commodity producers hedge against falling prices.",
                "By shorting an equal amount in the futures market, a producer locks in costs and profit before harvest.",
                "So the book calls futures essentially a bearish mechanism.",
            ),
            accent="Unlike shares, every futures contract eventually expires.",
            caption="The chapter describes what futures are for and how they behave. It never defines a futures contract itself.",
            notes=(
                "Be honest that there is no formal definition here. Do not supply one from outside.",
                "The whole part follows from one fact: contracts expire, so positions have to be moved.",
            ),
        ),
        Term(
            term="Rollover",
            plain="Swapping an expiring contract for a later one, so you can keep holding the position.",
            example="You hold the June contract. Before June expires you sell it and buy September.",
            formal="Unlike the equity markets, all futures contracts eventually expire, requiring a trader who intends to hold a position to roll over into the next available contract. Expiration months are usually quarterly, in March, June, September and December, often extending beyond a year.",
            notes=(
                "Quarterly: March, June, September, December. Say the four months.",
                "The book advises rolling slightly before expiry, to avoid the volatility of last minute exits.",
            ),
        ),
        Content(
            title="When a contract is liquid",
            lines=(
                "A futures contract is normally fairly illiquid until the last three to six months before expiry.",
                "Volume and open interest are greatest about two to three months before expiry.",
                "As expiry approaches, volume subsides as traders roll into the next contract.",
            ),
            accent="Trade the contract with the largest volume and open interest. It may not be the nearby one.",
            notes=(
                "Two to three months is the number to write down.",
                "Open interest is a Chapter 6 idea. Here it is just a second measure of activity.",
            ),
        ),
        Figure(
            title="Volume on two silver contracts",
            number="3.29",
            shows="Daily charts of the July and September 2011 silver futures side by side: volume contracting on the expiring July contract while it expands on the September contract, which has become the nearby one.",
            notes=(
                "Left panel: volume falling. Right panel, same weeks: volume rising.",
                "Nobody lost interest in silver. They moved contracts.",
            ),
        ),
        Content(
            title="Read volume on a continuous chart",
            lines=(
                "Falling volume toward expiry can lead an analyst to believe a trend is weak.",
                "A quick look at the next contract will normally show volume rising over the same period.",
                "To gauge true volume and open interest across rollover points, use a continuous chart.",
            ),
            accent="Falling volume on an expiring contract is traders leaving, not the trend weakening.",
            notes=(
                "Link to Chapter 2: volume must confirm the trend. This is how volume can lie about it.",
                "Continuous charts get the second half of this part.",
            ),
        ),
        Figure(
            title="Volume on the continuous silver chart",
            number="3.30",
            shows="The continuous daily chart of silver with its volume, giving one balanced view of volume action across multiple contracts and marking a volume blow off.",
            notes=(
                "The same months as the last figure, now as one unbroken volume record.",
                "This figure is on the first cut. The slide before carries the point.",
            ),
        ),
        Term(
            term="Front month contract",
            plain="The contract that expires soonest. Also called the nearby or nearest contract.",
            example="It is March and the March contract has just expired. June is now the front month.",
            formal="The contract with the closest expiry is the nearby, nearest or front month contract. It has the expiration date closest to the current date, the narrowest bid-ask spread, the narrowest spread with respect to the spot price, and it is the most liquid contract.",
            notes=(
                "Four characteristics. Past papers list them with one of the four reversed.",
                "Narrowest is the word to underline twice: bid-ask spread, and spread to the spot price.",
            ),
        ),
        Content(
            title="Next month, back months, and the month codes",
            lines=(
                "The next contract is the second one out, with the expiry closest to the nearby contract.",
                "Contracts further out than that are back month contracts.",
                "Codes: F Jan, G Feb, H Mar, J Apr, K May, M Jun, N Jul, Q Aug, U Sep, V Oct, X Nov, Z Dec.",
            ),
            accent="The quarterly four are H, M, U and Z.",
            caption="A trader may also hold one contract closer and one further out at once. The book calls that a calendar spread.",
            notes=(
                "With June as front month: September is next, and December and the following March are back months.",
                "Say H, M, U, Z out loud. It is the most memorable thing on the slide.",
            ),
        ),
        Figure(
            title="Front, next and back months",
            number="3.31",
            shows="Quarterly contracts over twelve months, March to March, showing for each starting point which contract is the nearby or front month, which is the next month and which is the back month.",
            notes=(
                "Start from the top row and read across: front, next, back.",
                "Then drop one row and watch every label move one contract along.",
            ),
        ),
        Check(
            label="Liquidity and the front month",
            questions=(
                Q(
                    stem="Volume and open interest in a futures contract are normally greatest:",
                    options=("In its first month of trading",
                             "About two to three months before expiry",
                             "In its last week before expiry",
                             "On the expiry day itself"),
                    answer="B",
                    reason="Volume subsides nearer expiry as traders roll into the next contract.",
                ),
                Q(
                    stem="The front month contract has:",
                    options=("The widest bid-ask spread",
                             "The largest spread with respect to the spot price",
                             "The expiration date closest to the current date",
                             "The least liquidity of all the contracts"),
                    answer="C",
                    reason="It also has the narrowest spreads and is the most liquid. The other three are reversed.",
                ),
            ),
        ),
        Term(
            term="Negative roll yield",
            plain="The loss from rolling into a new contract that costs more than the old one.",
            example="You sell March at 11 pesos and must buy June at 12. You pay 1 peso to stay in the trade.",
            formal="When the new contract trades at a higher price, it is trading at a premium to the previous contract, and rolling over at a premium causes the trader to experience negative roll yields. It is possible to lose money being long in a rising or sideways market if the rollover premiums are large enough.",
            notes=(
                "The last sentence is the surprising one. Read it twice.",
                "Successive premiums accumulate. One peso a quarter is four pesos a year.",
            ),
        ),
        Figure(
            title="Rolling over at a premium",
            number="3.32",
            shows="A long bought in March at 10 dollars and sold at 11 when March expires, then rolled into the June contract at 12, paying a 1 dollar premium: a negative roll yield.",
            notes=(
                "Follow the arrow: sell at 11, buy at 12. The gap is the premium.",
                "The March trade made money. The roll gave some of it back.",
            ),
        ),
        Term(
            term="Positive roll yield",
            plain="The gain from rolling into a new contract that costs less than the old one.",
            example="You sell March at 12 pesos and buy June at 11. You collect 1 peso for staying in the trade.",
            formal="When the new contract trades at a lower price, it trades at a discount to the previous contract, and rolling over at a discount causes the trader to experience positive roll yields. It is possible to make a profit being long in a declining or sideways market if the rollover discounts are large enough.",
            notes=(
                "The mirror image. Same sentence with premium swapped for discount.",
                "Ask which one a long holder would rather see every quarter.",
            ),
        ),
        Figure(
            title="Rolling over at a discount",
            number="3.33",
            shows="A long bought in March at 10 dollars and sold at 12 when March expires, then rolled into the June contract at 11, collecting a 1 dollar discount: a positive roll yield.",
            notes=(
                "Sell at 12, buy at 11. This time the gap is paid to you.",
                "Put 3.32 and 3.33 side by side in their heads. Only the direction of the gap differs.",
            ),
        ),
        Term(
            term="Normal contango",
            plain="Contracts further out cost successively more than the price the market is expected to be at when they expire.",
            example="The spot price is expected to be 100 at expiry, and the contracts further out trade at 101, 102, 103 and 104.",
            formal="When further out contracts are trading at successively higher prices compared to the expected spot price at expiry, the market is in normal contango.",
            notes=(
                "The comparison is with the expected spot price at expiry. That is what normal means here.",
                "Contango goes with premiums, so with negative roll yields for a long holder.",
            ),
        ),
        Term(
            term="Normal backwardation",
            plain="The mirror image: contracts further out cost successively less than the expected spot price.",
            example="The spot price is expected to be 100 at expiry, and the contracts further out trade at 99, 98, 97 and 96.",
            formal="If further out contracts are trading at successively lower prices compared to the expected spot price at expiry, the market is in normal backwardation.",
            notes=(
                "Same numbers either side of 100. Contango above, backwardation below.",
                "Backwardation goes with discounts, so with positive roll yields.",
            ),
        ),
        Content(
            title="Contango without the word normal",
            lines=(
                "Traders often drop the word normal and compare further out contracts with the nearby contract or the current spot price.",
                "The book calls that an informal use of the terms, but common practice among futures traders.",
            ),
            accent="Simple contango can be read off a chart. Normal contango needs the expected spot price at expiry.",
            caption="The book does not say how to estimate the expected spot price at expiry. It says only that you need some knowledge of it.",
            notes=(
                "Two comparisons: against the expected spot at expiry, or against today's nearby price.",
                "Past papers ask which comparison defines normal contango. The expected spot at expiry.",
            ),
        ),
        Figure(
            title="Gold in simple contango",
            number="3.34",
            shows="A daily chart of 2012 gold futures, with the further out contracts stacked beneath it trading at successively higher prices than the nearby December contract.",
            notes=(
                "Read the prices down the stack. Each is higher than the one above.",
                "The book says this is simple contango and may or may not be normal contango.",
            ),
        ),
        Check(
            label="Roll yields and contango",
            questions=(
                Q(
                    stem="A long holder who can profit in a declining or sideways market is one whose rollovers are at:",
                    options=("A premium large enough",
                             "A discount large enough",
                             "The spot price exactly",
                             "The front month price exactly"),
                    answer="B",
                    reason="Rolling at a discount pays the trader, a positive roll yield, at every rollover.",
                ),
                Q(
                    stem="Further out contracts trade at 99, 98, 97 and 96 against an expected spot price of 100 at expiry. The market is in:",
                    options=("Normal contango",
                             "Simple contango",
                             "Normal backwardation",
                             "Negative roll yield"),
                    answer="C",
                    reason="Successively lower than the expected spot price at expiry is normal backwardation.",
                ),
            ),
        ),
        Term(
            term="Convergence",
            plain="At expiry, the futures price and the spot price become the same price.",
            example="The spot stays at 100. A contango contract at 104 has to fall to 100 by expiry; a backwardated one at 96 has to rise to 100.",
            formal="Futures prices always converge to the spot price at expiry. With the spot price constant, a contract in contango will eventually decline, experiencing negative yields, and a contract in backwardation will eventually rise, experiencing positive yields.",
            notes=(
                "Always is the book's word. Convergence is the one certainty in the part.",
                "With some mispricing, a long far out backwardated contract against a short nearby one locks in that convergence.",
            ),
        ),
        Figure(
            title="Futures and spot converge at expiry",
            number="3.35",
            shows="Contracts converging on a spot price assumed to stay at 100 dollars: backwardated prices of 99 to 96 rising to it with a positive yield, contango prices of 101 to 104 falling with a negative yield.",
            notes=(
                "Point at the arrows: up from backwardation, down from contango, both to 100.",
                "Read the boxed line: it is possible to profit or lose from convergence with the spot unchanged.",
            ),
        ),
        Content(
            title="Rising gas, falling fund",
            lines=(
                "Natural gas rallied strongly through 2009.",
                "The U.S. Natural Gas Fund, which tracks gas through futures, rolled at large premiums and lost money.",
                "Very short term traders who never roll are not affected by roll yields either way.",
            ),
            accent="Contango can take a whole rally away from a holder who has to roll.",
            notes=(
                "This is the book's real example of negative roll yield. Report it as the book reports it.",
                "The book does not tell us what happened to the fund after 2009, so neither do we.",
            ),
        ),
        Figure(
            title="Natural gas against the fund that tracks it",
            number="3.36",
            shows="The continuous daily chart of natural gas, in contango and rallying, beside the U.S. Natural Gas Fund over the same months.",
            notes=(
                "Left panel up, right panel not. Same commodity underneath.",
                "This figure and the next are on the first cut. The slide before carries the point.",
            ),
        ),
        Figure(
            title="The fund's underperformance",
            number="3.37",
            shows="A relative strength chart of the U.S. Natural Gas Fund against spot natural gas, falling steadily and labelled as the effect of negative roll yield.",
            notes=(
                "A falling relative strength line means the fund lagged gas the whole way.",
                "Relative strength charts come back at the end of this part with perpetual contracts.",
            ),
        ),
        Check(
            label="Convergence",
            questions=(
                Q(
                    stem="At expiry, a futures price:",
                    options=("Always converges to the spot price",
                             "Always stays above the spot price",
                             "Always stays below the spot price",
                             "Converges only in backwardation"),
                    answer="A",
                    reason="Convergence at expiry holds for every contract, in contango or in backwardation.",
                ),
                Q(
                    stem="With the spot price constant, a contract in contango will:",
                    options=("Rise toward the spot, with positive yields",
                             "Stay where it is until expiry",
                             "Rise, with negative yields",
                             "Decline toward the spot, with negative yields"),
                    answer="D",
                    reason="It trades above the spot and must converge down to it by expiry.",
                ),
            ),
        ),
        Term(
            term="Unadjusted nearest futures chart",
            plain="Join the nearest contracts end to end and leave the jumps between them in.",
            example="March expires at 110 and June is trading at 120. The chart simply jumps 10 at the roll.",
            formal="Connecting the nearest contracts without accounting for the spread between them. It preserves the actual sequence of nearby prices and is an accurate record of historical prices, but technical analysis cannot be applied to it meaningfully, and back and forward testing are impossible because of the gaps.",
            notes=(
                "The three approaches are unadjusted, back adjusted and perpetual. This is the first.",
                "Accurate history, useless analysis. Hold that trade off in mind for the next two terms.",
            ),
        ),
        Figure(
            title="An unadjusted nearest futures chart",
            number="3.38",
            shows="A price series made of successive contracts joined end to end without adjustment, with a price gap distortion at every rollover.",
            notes=(
                "Count the jumps. Each one is a rollover, not a market move.",
                "A trendline drawn across these jumps means nothing. That is the book's objection.",
            ),
        ),
        Term(
            term="Back-adjusted continuous chart",
            plain="Shift the old contract's history to meet the new contract's price.",
            example="March expires at 110 while June trades at 120. Every March price is raised by 10, so its troughs at 80 and 90 become 90 and 100.",
            formal="Back adjusting raises or lowers the previous contract price at expiry, or N days before, to match the new contract, removing the spread and creating a continuous flow of prices. It always displays the current market price and allows technical analysis and back and forward testing.",
            notes=(
                "Do the example on the board. 80 plus 10 is 90, 90 plus 10 is 100.",
                "Then say: if September trades at a further 10 premium, they move again to 100 and 110. The book also calls it spread adjusted.",
            ),
        ),
        Figure(
            title="How back adjusting is done",
            number="3.40",
            shows="A March contract expiring at 110 dollars while June trades at 120; March prices are adjusted up by the 10 dollar spread, lifting its troughs at 80 and 90 to 90 and 100.",
            notes=(
                "This comes before Figure 3.39 on purpose: the mechanism first, the real case after.",
                "Point at the adjust upward box, then at the new trough values.",
            ),
        ),
        Content(
            title="The price of back adjusting",
            lines=(
                "Past prices no longer reflect what the contracts actually traded at.",
                "At every roll the history shifts again, so past peaks and troughs keep changing.",
                "If newer contracts keep trading at a discount, past prices may even become negative.",
            ),
            accent="Historical prices end up adjusted to the net accumulated spread.",
            notes=(
                "Negative prices sound absurd. Ask the room how it could happen before showing them.",
                "The shifting history also spoils relative strength ratios. That sets up perpetual contracts.",
            ),
        ),
        Chart(
            title="Back adjusting through several rolls",
            letter="F",
            shows="Contracts joined end to end, each new one at a discount to the last, and the same string back adjusted into one continuous line whose earliest prices fall below zero.",
            tier="reinforcement",
            notes=(
                "Follow the unadjusted line: a drop at every roll. Then the adjusted line: no drops.",
                "Point at the left end of the adjusted line, below zero. Nobody ever traded at that price.",
            ),
        ),
        Figure(
            title="Continuous gold against the contract itself",
            number="3.39",
            shows="The continuous, spread adjusted daily chart of gold above the December 2013 gold contract over the same period, with the OHLC readings for 7 November 2011 boxed on each and differing between the two.",
            notes=(
                "Read the two boxed sets of OHLC numbers. Same day, different prices.",
                "The continuous chart's history was rewritten by adjustment. The contract's was not.",
            ),
        ),
        Check(
            label="Unadjusted and back adjusted",
            questions=(
                Q(
                    stem="In a back-adjusted continuous chart:",
                    options=("Historical prices remain unchanged",
                             "The current market price is always displayed",
                             "There are gaps at every rollover",
                             "Back testing is impossible"),
                    answer="B",
                    reason="The history is shifted to meet the current contract, so today's price is the real one.",
                ),
                Q(
                    stem="An unadjusted nearest futures chart:",
                    options=("Removes the gaps between contracts",
                             "Always displays an estimated price",
                             "Is best for back testing",
                             "Is an accurate record of historical prices"),
                    answer="D",
                    reason="It keeps the actual nearby prices, gaps and all, which is also why analysis on it fails.",
                ),
            ),
        ),
        Term(
            term="Perpetual contract",
            plain="It never rewrites history, and it shows an estimated price, not the real one.",
            example="Between two expiries, a perpetual series blends the nearby and further out contract prices by a weighting, so the value on the chart is not a price anyone traded at.",
            formal="Perpetual contracts are not back shifted with each new front month contract. They display an estimated price rather than the current market price, interpolated between expiration dates by a weighting factor. That makes them useless for trading, but useful as a basis for constructing relative strength charts.",
            notes=(
                "Estimated is the key word. You cannot place an order at a perpetual price.",
                "The book does not give the weighting. Do not supply one.",
            ),
        ),
        Content(
            title="Which chart for which job",
            lines=(
                "Trading, and back or forward testing: the back-adjusted continuous chart.",
                "An accurate record of what actually traded: the unadjusted nearest futures chart.",
                "Relative strength charts: perpetual contracts, because back adjusting keeps shifting the ratio.",
            ),
            accent="None of the three does every job.",
            notes=(
                "This slide answers review question 8 and most of what past papers ask about futures charts.",
                "Ask which one they would use to test a trading rule. Back adjusted.",
            ),
        ),
        Check(
            label="Perpetual contracts",
            questions=(
                Q(
                    stem="Perpetual contracts:",
                    options=("Display the current market price",
                             "Keep changing historical prices at each roll",
                             "Display an estimated price, which is useless for trading",
                             "Contain a gap at every rollover"),
                    answer="C",
                    reason="The price is interpolated between expiries by a weighting factor, so nobody traded at it.",
                ),
                Q(
                    stem="For relative strength charts the book prefers:",
                    options=("Perpetual contracts",
                             "Back-adjusted continuous charts",
                             "Unadjusted nearest futures charts",
                             "Tick charts"),
                    answer="A",
                    reason="Their history is not back shifted, so the ratio between two series is not distorted.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Why futures exist and why they must be rolled",
            "When a contract is liquid, and reading volume on a continuous chart",
            "Front, next and back months, and the month codes",
            "Negative and positive roll yields",
            "Normal contango, normal backwardation and convergence",
            "Unadjusted, back-adjusted and perpetual charts",
        ),
        notes=(
            "Ask which futures chart always shows today's real price. Back adjusted.",
            "That is the whole chapter. Move to the wrap up.",
        ),
    ),
)

# ==========================================================================
# Closing
# ==========================================================================

CLOSING = (
    Content(
        title="Chapter 3 in five sentences",
        lines=(
            "A chart filters each interval into four prices: open, high, low and close.",
            "Supply and demand set the high and low; the clock sets the open and close.",
            "A bar can close on time, range, volume, transactions or volatility.",
            "Scaling moves every trendline, and the spread moves every entry.",
            "Futures expire, each roll costs or pays, and no futures chart does every job.",
        ),
        accent="Say those five and you can answer most of this chapter.",
        notes=(
            "Read all five slowly. This is the summary students should copy down.",
            "Then ask for the five constant measures one last time, with the slide hidden.",
        ),
    ),
    Content(
        title="The review questions to prepare",
        lines=(
            "How is OHLC data derived, and what increases its significance?",
            "Why should traders normalize their charts for volatility?",
            "Describe the five measures of constancy in charting.",
            "How does chart scaling affect the use of overlay indicators?",
            "How does the bid-ask spread affect the reward to risk ratio?",
            "Link contango to negative roll yields; describe back-adjusted charts.",
        ),
        caption="All eight of the book's questions, on six lines. Every one is answerable from this chapter.",
        notes=(
            "Say where each answer sits: Parts 1 and 2, Part 1, Part 3, Part 4, Part 5, Part 6.",
            "Lines one and six each carry two of the book's eight questions.",
        ),
    ),
    Content(
        title="What this chapter names and does not teach",
        lines=(
            "Gann bars, Kagi charts and Gann swing charts.",
            "The breadth and sentiment data items.",
            "How the average true range is averaged, and how to estimate the expected spot price.",
            "What a futures contract is, formally.",
        ),
        accent="Nothing on this slide is examinable from Chapter 3.",
        caption="Do not fill these from outside the book. Where the book takes one up later, we will too.",
        notes=(
            "Be straight with them: the chapter uses these words and never explains them.",
            "Support, resistance and trendlines are Chapter 5. ATR is Chapter 8.",
        ),
    ),
    Closing(
        title="Next: market phase analysis",
        lines=(
            "Chapter 4 studies the structure and behaviour of the three market phases.",
            "Its objectives include reading a potential change of market regime from volume.",
            "Before then: switch one chart between linear and ratio scaling and see which trendline breaks first.",
        ),
        accent="FIN1209  Technical Analysis in Investment  |  Institute of Accounts, Business and Finance",
        notes=(
            "The last line is a suggestion, not homework. It takes five minutes on any free charting site.",
            "Tell them when the quiz on this chapter falls.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 3",
    title="Mechanics and Dynamics of Charting",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    objectives=(
        "Understand chart construction and how technical data is incorporated and displayed.",
        "Describe the process by which OHLC data is created and its relationship to various charts.",
        "Identify and differentiate between contango and backwardation, and their connection with negative and positive roll yields.",
        "Understand the adverse effects of the bid-ask spread on trading performance.",
        "Construct various charts using constant measures of time, range, volatility, trade volume and number of transactions.",
        "Set up a volatility neutral chart for consistent viewing of price action.",
    ),
    roadmap=(
        "Part 1  From price to OHLC",
        "Part 2  What the four prices mean, and four kinds of gap",
        "Part 3  Five constant measures",
        "Part 4  Chart scaling",
        "Part 5  The bid-ask spread",
        "Part 6  Futures contracts",
    ),
    sections=(PART1, PART2, PART3, PART4, PART5, PART6),
    closing=CLOSING,
)
