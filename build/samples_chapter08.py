"""Chapter 8, Window Oscillators and Overlay Indicators: the approved-samples scaffold.

Only the sample slides exist so far. The full deck is written by hand, part
by part, after the instructor approves the outline and these samples (rule 37:
no code generates or drops teaching text). Part A will be 8.1 and 8.2; Part B
8.3 to 8.8. Each sample below is a kind of slide the chapter needs:

  (a) an opener that names the idea before any number
  (b) a book figure read with numbered marks
  (c) a worked example on our own chart
  (d) two ideas easily confused, each on its own slide with its own chart
  (e) one check and its answer, the figure on both

Marks on book figures were read off a 0.05 grid of the master figure in
~/.fin1209-figures/chapter-08. Our own numbers are never marked on a book figure.
"""

from deckkit import Chapter, Content, Figure, Mark, Question, Section
from deckkit import Check
from chartlayout_chapter08 import (CourseCheck, StackedFigureCheck, WidePair, book_crop,
                                   course_chart, expand_chart_pages)

# (b) Figure 8.1, the whole figure: a price chart with overlays, and three window oscillators under it.
# Each box starts above its own printed label and ends where the next begins, so no box edge cuts a word.
FIGURE_8_1 = book_crop('8.1', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.1: a price chart with overlays on it, and under it the RSI and the stochastics, both bounded 0 to 100 percent, and the MACD, which is unbounded.",
    marks=(
        Mark(number=1, kind='box', x0=0.005, y0=0.0, x1=0.74, y1=0.488, color='gold', at=(0.77, 0.06), size=0.3),
        Mark(number=2, kind='box', x0=0.005, y0=0.492, x1=0.74, y1=0.595, color='red', at=(0.77, 0.545), size=0.3),
        Mark(number=3, kind='box', x0=0.005, y0=0.599, x1=0.74, y1=0.752, color='blue', at=(0.77, 0.68), size=0.3),
        Mark(number=4, kind='box', x0=0.005, y0=0.756, x1=0.74, y1=0.995, color='purple', at=(0.77, 0.88), size=0.3),
    ))
FIGURE_8_1.origin = 'Lim (2016), p. 238, Figure 8.1, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

# Reference slides: each oscillator named on the list is shown on one of Lim's own charts.
# Figure 8.17 shows the StochRSI, the slow stochastic and the RSI together, top to bottom.
FIGURE_8_17 = book_crop('8.17', (0.0, 0.30, 1.0, 1.0),
    "Figure 8.17, cropped to its three oscillator windows. From the top: the StochRSI, the slow stochastic and the RSI, each under the Dow Jones price chart.",
    marks=(
        Mark(number=1, kind='box', x0=0.005, y0=0.834, x1=0.91, y1=0.995, color='gold', at=(0.957, 0.955), size=0.26),
        Mark(number=2, kind='box', x0=0.005, y0=0.672, x1=0.91, y1=0.83, color='red', at=(0.957, 0.715), size=0.26),
        Mark(number=3, kind='box', x0=0.005, y0=0.508, x1=0.91, y1=0.668, color='blue', at=(0.957, 0.62), size=0.26),
    ))
FIGURE_8_17.origin = 'Lim (2016), p. 254, Figure 8.17, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

# Figure 8.8 shows the MACD and the ROC under the Apple price chart.
FIGURE_8_8 = book_crop('8.8', (0.0, 0.30, 1.0, 1.0),
    "Figure 8.8, cropped to its three oscillator windows. From the top: the RSI, the MACD and the ROC, each under the Apple price chart.",
    marks=(
        Mark(number=1, kind='box', x0=0.005, y0=0.662, x1=0.935, y1=0.812, color='gold', at=(0.965, 0.74), size=0.3),
        Mark(number=2, kind='box', x0=0.005, y0=0.816, x1=0.935, y1=0.985, color='red', at=(0.965, 0.9), size=0.3),
    ))
FIGURE_8_8.origin = 'Lim (2016), p. 245, Figure 8.8, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

# Figure 8.7 again, its lower half: the RSI window and the CCI window under it.
FIGURE_8_7_CCI = book_crop('8.7', (0.0, 0.5, 1.0, 1.0),
    "Figure 8.7, cropped to its lower half: the RSI window and, under it, the CCI window with its plus 100 and minus 100 lines and its zero line.",
    marks=(
        Mark(number=1, kind='box', x0=0.005, y0=0.814, x1=0.93, y1=0.992, color='gold', at=(0.035, 0.795), size=0.28),
        Mark(number=2, kind='line', x0=0.60, y0=0.892, x1=0.80, y1=0.892, color='red', at=(0.835, 0.862), size=0.28),
        Mark(number=3, kind='line', x0=0.60, y0=0.9375, x1=0.80, y1=0.9375, color='blue', at=(0.835, 0.968), size=0.28),
    ))
FIGURE_8_7_CCI.origin = 'Lim (2016), p. 244, Figure 8.7, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

# The book's own %K example, Figure 8.22. Its own numbers may sit on its own picture.
# Rings sit on the bar itself: the top of the wick, the bottom of the wick, the top of the body where the close dash starts.
FIGURE_8_22 = book_crop('8.22', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.22: a bar with open 1.4590, high 1.5020, low 1.4900 and close 1.5000, and the working of raw %K as 83.3 percent.",
    marks=(
        Mark(number=1, kind='circle', x0=0.176, y0=0.345, x1=0.204, y1=0.395, color='gold', at=(0.255, 0.43), size=0.3),
        Mark(number=2, kind='circle', x0=0.172, y0=0.90, x1=0.208, y1=0.964, color='red', at=(0.229, 0.87), size=0.3),
        Mark(number=3, kind='circle', x0=0.187, y0=0.462, x1=0.223, y1=0.526, color='blue', at=(0.243, 0.545), size=0.3),
    ))
FIGURE_8_22.origin = 'Lim (2016), p. 260, Figure 8.22. The marks are ours, added for teaching.'

# (e) Figure 8.7: the RSI crossing its dashed 50 percent level, with Lim's S and B on the price above it.
FIGURE_8_7 = book_crop('8.7', (0.31, 0.04, 1.0, 0.75),
    "Figure 8.7, cropped to its second pair of crossings: the price chart with Lim's S and B letters, and under it the RSI with its dashed 50 percent level and its axis. Mark 1 is where the RSI drops below 50, mark 2 the S above it, mark 3 where the RSI climbs back above 50, mark 4 the B above it.",
    marks=(
        Mark(number=1, kind='circle', x0=0.472, y0=0.653, x1=0.508, y1=0.695, color='gold', at=(0.46, 0.71), size=0.3),
        Mark(number=2, kind='circle', x0=0.455, y0=0.105, x1=0.495, y1=0.155, color='red', at=(0.445, 0.13), size=0.3),
        Mark(number=3, kind='circle', x0=0.527, y0=0.651, x1=0.563, y1=0.693, color='blue', at=(0.58, 0.63), size=0.3),
        Mark(number=4, kind='circle', x0=0.51, y0=0.16, x1=0.545, y1=0.21, color='purple', at=(0.529, 0.148), size=0.3),
    ))
FIGURE_8_7.origin = 'Lim (2016), p. 244, Figure 8.7, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

PART_A = Section(
    number=1,
    title='Sample slides for approval',
    short='Chapter 8 samples',
    minutes='',
    covers=('indicator', 'overlay indicator', 'window oscillator', 'stochastic', 'crossover'),
    slides=(
        # (a) The opener: what we are talking about, and why, before any number, with our chart of the idea.
        Content(
            notes=('Open by saying what the chapter is: the place where the oscillators used since Chapter 4 finally get taught.', 'Then show one picture of the claim: price alone looks strong, the indicator under it does not.'),
            origin='Lim (2016), p. 235; Chapter 6. The chart on the next slide is ours.',
            title='Indicators show strength and weakness that price alone hides',
            lines=("Up to now we have mostly read price itself: bars, patterns and trends. The book has also kept using indicators such as the MACD, the RSI and the stochastic without explaining them, and Chapter 6 told you Chapter 8 is where oscillators get taught. This is that chapter.",
                   "Why bother? Lim says oscillators and indicators can reveal underlying strengths and weaknesses of price action that would not have been obvious otherwise, which helps us forecast potential reversals and breakouts (p. 235).",
                   ),
            accent='Indicators can show you strength or weakness you would not have spotted from price alone.',
        ),
        Content(
            notes=('One picture of the claim, made up by us.',),
            origin='Our own example of what Lim means (p. 235). The numbers are ours.',
            title='Here is what an indicator can show that price alone does not',
            lines=("Here is one example of ours of what that can look like: price makes a higher peak [1] while the indicator under it makes a lower one [2]. Price alone shows only strength. Lim calls this divergence, and we meet it later in this chapter (pp. 240, 244).",),
        ),
        course_chart('hd',
            notes=('Gold 1 the second price peak, higher than the first, 63 against 60. Red 2 the second indicator peak, lower, 66 against 78.', 'This is our example of what Lim means; the next slides say what the indicator is.'),
            origin='FIN1209 teaching chart H. The numbers are invented for teaching.',
            title='Here is what an indicator can show that price alone does not',
            letter='H',
            shows='Our price line making a higher second peak, 63 after 60, with an indicator window under it making a lower second peak, 66 after 78.',
            tier='core',
            marks=(),
        ),
        Content(
            notes=('Two names to learn: overlay indicator and window oscillator. The next slide shows both on one chart.',),
            origin='Lim (2016), pp. 235, 236 and 238.',
            title='Indicators come in two kinds: overlays and window oscillators',
            lines=("Lim sorts indicators, the word for the whole family here, into two categories (p. 235). An overlay indicator is plotted on the same chart as price, or on an oscillator, where it acts as a barrier, that is, support and resistance (p. 235).",
                   "A window oscillator is a mathematically derived indicator, normally based on open, high, low and close, volume and open interest (p. 236). On Lim's charts it sits in its own window under price (p. 238)."),
            accent='An overlay goes on top of price or an oscillator. A window oscillator gets a window of its own.',
        ),
        # (b) A book figure read with numbered marks.
        WidePair(
            notes=('Walk the four boxes top to bottom: gold 1 price with overlays, red 2 the RSI, blue 3 the stochastics, purple 4 the MACD.',
                   'Point out the label at the bottom of the MACD window: Lim draws overlays on oscillators too.'),
            origin='Lim (2016), p. 238, Figure 8.1. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.1 puts both kinds of indicator on one chart',
                lines=("The top part is price, with overlay indicators drawn on it [1]. Under it sit three window oscillators: the relative strength index or RSI [2], the stochastics [3] and the moving average convergence divergence or MACD [4].",
                       "Inside the MACD window [4], see Lim's label \"Overlays on oscillators\": he draws overlays there as well."),
                accent='Price and its overlays on top. Oscillators in their own windows below.',
            ),
            picture=FIGURE_8_1,
            text_w=4.4,
        ),
        # Reference slides: each oscillator on the list is shown on one of Lim's own charts.
        WidePair(
            notes=('The bounded oscillators, read on Lim\'s own chart. Part B builds each one.',),
            origin='Lim (2016), pp. 251, 254, 259 and 262, Figure 8.17. The marks are ours, added for teaching.',
            left=Content(
                title='The oscillators you will meet before we build them (1 of 3)',
                lines=("Bounded, 0 to 100 percent: the relative strength index or RSI [1] tracks a stock's strength through its average gain and loss over the last n periods, n being the lookback (p. 262). The stochastic [2] is the position of the latest close in the recent price range (p. 259). The StochRSI [3] is the stochastic calculation applied to RSI values (p. 251). Lim's chart prints the StochRSI [3] from 0 to 1 instead of 0 to 100: 0.8 there is 80 percent. That reading is ours.",),
            ),
            picture=FIGURE_8_17,
            text_w=4.9,
        ),
        Content(
            notes=('Overbought, oversold and equilibrium, drawn on one oscillator of ours.',),
            origin='Lim (2016), pp. 236, 241 and 244. The chart on the next slide is ours.',
            title='Overbought, oversold and equilibrium on one oscillator',
            lines=("Overbought and oversold are the high and low ends of an oscillator's readings (pp. 236, 241). Lim calls them overextensions. That is not Chapter 7's overextended bar: here the word describes an oscillator's reading. Equilibrium is the central value it swings around (p. 244).",
                   ),
        ),
        Content(
            notes=('Drawn on one oscillator of ours.',),
            origin='Lim (2016), pp. 236, 241 and 244. The chart is ours.',
            title='Here they are on one oscillator of ours',
            lines=("Lim says overbought is usually at or above 70 or 80 percent and oversold at or below 20 or 30, depending on the oscillator (p. 241). Our chart uses the RSI's 70 and 30. On our oscillator the reading of 78 is overbought [1], the 26 is oversold [2], and 50 is the equilibrium [3].",),
        ),
        course_chart('zn',
            notes=('Gold 1 the overbought reading of 78, red 2 the oversold reading of 26, blue 3 the equilibrium line at 50.', 'The 70 and 30 lines are the RSI defaults Lim gives on p. 241; the readings are ours.'),
            origin='FIN1209 teaching chart G. The numbers are invented for teaching.',
            title='Here they are on one oscillator of ours',
            letter='G',
            shows='Our bounded oscillator with its overbought zone from 70, its oversold zone to 30 and its equilibrium at 50, and the readings 78 and 26 written on it.',
            tier='core',
            marks=(),
        ),
        WidePair(
            notes=('The unbounded ones. Part B builds the MACD, ROC and MOM; the CCI is on the next slide.',),
            origin='Lim (2016), pp. 245, 256 and 257, Figure 8.8. The marks are ours, added for teaching.',
            left=Content(
                title='The oscillators you will meet before we build them (2 of 3)',
                lines=("Unbounded, no top or bottom: the moving average convergence divergence or MACD [1] is the 12-period exponential moving average (EMA) minus the 26-period EMA (p. 257). The rate of change or ROC [2] is the percent change in price over n periods, and momentum or MOM is the price difference over n periods (p. 256).",
                       "Lim's chart draws the MACD and the ROC; the MOM is drawn later. The top window is the RSI; the lines and arrows Lim draws on it belong to a later topic."),
            ),
            picture=FIGURE_8_8,
            text_w=4.9,
        ),
        WidePair(
            notes=('The CCI has no calculation in this chapter. Its zero line is drawn on Lim\'s chart.',),
            origin='Lim (2016), pp. 242 and 244, Figure 8.7. The marks are ours, added for teaching.',
            left=Content(
                title='The oscillators you will meet before we build them (3 of 3)',
                lines=("The CCI, the commodity channel index [1], gets an overbought level of plus 100 and an oversold level of minus 100 (pp. 242, 244). This chapter gives no calculation for it. On Lim's chart the plus 100 level is the solid line [2] and the minus 100 level the solid line [3]. The zero line crossovers marked there come later.",
                       "Part A only reads these oscillators on Lim's charts; Part B builds them. Where you meet one before Part B builds it, the slide says what you need and no more."),
            ),
            picture=FIGURE_8_7_CCI,
            text_w=4.9,
        ),
        # The idea named before the numbers: raw %K, and our chart of two closes in one range.
        Content(
            notes=('Name the idea first: where does the latest close sit in the recent range? Then the chart.',),
            origin='Lim (2016), p. 259. The chart on the next slide is ours.',
            title='The stochastic asks where the close sits in the recent range',
            lines=("The stochastic is one of the oscillators from our list. Now we build it. It answers one question: is the latest close near the top or near the bottom of the recent range?",
                   "Lim describes it as the position of the latest close as a percentage of the price range over a chosen number of periods, measured from the lowest low. The result is called the raw %K (p. 259).",
                   ),
            accent='Raw %K: where the latest close sits in the recent range, as a percentage.',
        ),
        Content(
            notes=('The same range, two different closes.',),
            origin='Lim (2016), p. 259. The chart is ours.',
            title='Here is the idea drawn: two closes in one range',
            lines=("On our chart the first close [1] sits near the top of the range and the second [2] near the bottom. C is the close; Hn and Ln are the highest high and lowest low of the lookback, and the next slide turns them into a formula.",),
        ),
        course_chart('ci',
            notes=('Gold 1 a close near the top of the range, 90 percent. Red 2 a close near the bottom, 10 percent. The range is the same.',),
            origin='FIN1209 teaching chart D. The numbers are invented for teaching.',
            title='Here is the idea drawn: two closes in one range',
            letter='D',
            shows='Our range from a lowest low of 50.00 to a highest high of 56.00, with one close near the top at 55.40, 90 percent, and one near the bottom at 50.60, 10 percent.',
            tier='core',
            marks=(),
        ),
        Content(
            notes=('Chapter 5 taught the bar stochastic inside one bar; the raw %K does the same over n periods.', 'The chart shows the two ends and the middle of the same range.'),
            origin='Lim (2016), pp. 259 to 260; Chapter 5, "Bar stochastic". The chart on the next slide is ours.',
            title='Raw %K compares the close with the n-period high and low',
            lines=("Chapter 5's bar stochastic asked this inside one bar, (C - L) / (H - L). The raw %K asks it over n periods. C is the closing price, Ln the lowest low of the last n periods and Hn the highest high.",
                   "Raw %K = (C - Ln) / (Hn - Ln) x 100 percent (p. 260). The usual lookback is 14 periods (p. 259).",
                   ),
            accent='Close at the lowest low gives 0 percent. Close at the highest high gives 100 percent.',
        ),
        Content(
            notes=('The two ends and the middle of one range.',),
            origin='Lim (2016), p. 260. The chart is ours.',
            title='Here are the two ends and the middle of one range',
            lines=("On our chart a close at the lowest low [1] gives 0 percent, one in the middle [2] gives 50 and one at the highest high [3] gives 100.",),
        ),
        course_chart('ce',
            notes=('Gold 1 a close at the lowest low, 0 percent. Red 2 a close in the middle, 50. Blue 3 a close at the highest high, 100.',),
            origin='FIN1209 teaching chart E. The numbers are invented for teaching.',
            title='Here are the two ends and the middle of one range',
            letter='E',
            shows='Our range from 50.00 to 56.00 with a close at the lowest low, 0 percent, one in the middle at 53.00, 50 percent, and one at the highest high, 100 percent.',
            tier='core',
            marks=(),
        ),
        Content(
            notes=('Why bounded: the top of the fraction can never exceed the bottom. Lim says this of the RSI on p. 262.',),
            origin='Lim (2016), pp. 236, 260 and 262. The chart on the next slide is ours.',
            title='Raw %K always stays between 0 and 100 percent',
            lines=("The close can never be below the lowest low or above the highest high of the same lookback. So the top of the fraction is never larger than the bottom, and raw %K stays between 0 and 100 percent (pp. 260, 262).",
                   "That makes it a bounded oscillator, the kind from Part A.",
                   ),
            accent="Every stock's raw %K runs on the same 0 to 100 scale, which is why Lim says bounded oscillators can be compared between stocks or markets over the same number of periods (p. 236).",
        ),
        Content(
            notes=('Every close lands between 0 and 100.',),
            origin='Lim (2016), pp. 260 and 262. The chart is ours.',
            title='Here is every close of one lookback on the 0 to 100 scale',
            lines=("On our chart the highest high [1] is 100 percent, the lowest low [2] is 0, and every close [3] lands between them. The bars are the fourteen of our worked example a few slides on.",),
        ),
        course_chart('rp',
            notes=('Gold 1 the highest high, 100 percent. Red 2 the lowest low, 0. Blue 3 the fourteen closes, all between them.',),
            origin='FIN1209 teaching chart F. The numbers are invented for teaching.',
            title='Here is every close of one lookback on the 0 to 100 scale',
            letter='F',
            shows='Our fourteen bars, the same as in the worked example, between a highest high of 56.00 and a lowest low of 50.00, and each bar\'s close shown as one dot on a 0 to 100 percent scale, all between the 0 and the 100.',
            tier='core',
            marks=(),
        ),
        WidePair(
            notes=("This is the book's own example, so its numbers belong on its own picture.",
                   'Gold 1 the high, red 2 the low, blue 3 the close at the top of the body.',
                   'The table prints an open of 1.4590, below the bar low of 1.4900. That cannot happen; the bar is drawn with its open at 1.4950. Raw %K does not use the open.'),
            origin='Lim (2016), pp. 259 to 260, Figure 8.22. The marks are ours, added for teaching.',
            left=Content(
                title="The book's example puts the close at 83.3 percent of the range",
                lines=("Lim's example uses a lookback of one bar, so the highest high and lowest low are just this bar's high of 1.5020 [1] and low of 1.4900 [2] (p. 259). The close is 1.5000 [3]. So raw %K = (1.5000 - 1.4900) / (1.5020 - 1.4900) x 100 = 83.3 percent (p. 260). Chapter 5 met this one-bar version as the bar stochastic.",
                       "One slip to ignore: the table gives the open as 1.4590, which is below the bar's low and cannot happen. The bar is drawn with it at 1.4950, so we read 1.4950. Raw %K does not use the open anyway."),
            ),
            picture=FIGURE_8_22,
            text_w=5.3,
        ),
        # (c) A worked example on our own chart.
        Content(
            notes=('Same formula, our own numbers. Say plainly that the numbers are made up.',),
            origin='Lim (2016), p. 260 for the formula. The numbers are ours, made up for teaching.',
            title="Let's work out a raw %K on our own numbers",
            lines=("Numbers of ours, made up to show the idea. Over the last 14 bars the highest high is PHP 56.00 [1] and the lowest low is PHP 50.00 [2], on different bars. Today's close is PHP 54.00 [3], so raw %K = (54.00 - 50.00) / (56.00 - 50.00) x 100 = 66.7 percent, two thirds of the way up the range.",),
        ),
        course_chart('k',
            notes=('Gold 1 is the highest high on the 4th bar, red 2 the lowest low on the 8th, blue 3 today\'s close.',),
            origin='FIN1209 teaching chart A. The numbers are invented for teaching.',
            title="Let's work out a raw %K on our own numbers",
            letter='A',
            shows='Fourteen bars of ours: the highest high of PHP 56.00 on the 4th bar, the lowest low of PHP 50.00 on the 8th, and today\'s close of PHP 54.00, giving a raw %K of 66.7 percent.',
            tier='core',
            marks=(),
        ),
        CourseCheck(
            notes=('Both answers come from the raw %K slides.',),
            origin='Questions are ours, answerable from the raw %K slides before; Lim (2016), p. 260.',
            label='Raw %K',
            questions=(
                Question(
                    stem='Over the last 14 bars the lowest low is PHP 50.00 and the highest high PHP 56.00. Today closes at PHP 50.00. What is raw %K?',
                    options=('0 percent', '50 percent', '66.7 percent', '100 percent'),
                    answer='A',
                    reason='(50.00 - 50.00) / (56.00 - 50.00) x 100 = 0 percent: a close at the lowest low (p. 260).',
                ),
                Question(
                    stem='What does a raw %K of 100 percent tell you about the close?',
                    options=('It equals the lowest low of the lookback', 'It sits at the midpoint of the range', 'It is below the lowest low', 'It equals the highest high of the lookback'),
                    answer='D',
                    reason='Raw %K is 100 percent only when C equals Hn, so the top of the fraction equals the bottom (p. 260).',
                ),
            ),
        ),
        # (d) Two look-alikes, each on its own slide with its own chart.
        Content(
            notes=('Two crossovers sound alike. Take the first alone, then the second.',),
            origin='Lim (2016), p. 244.',
            title='Crossing its equilibrium level is a buy or sell signal',
            lines=("An oscillator can be read by its equilibrium, the central value it swings around: 50 percent for a bounded oscillator and zero for an unbounded one (p. 244). Crossing above it is a buy signal and crossing below it a sell signal (p. 244).",
                   "On our chart the bounded one crosses above 50 [1] and below 50 [2]; the unbounded one crosses above zero [3] and below zero [4]."),
        ),
        course_chart('eq',
            notes=('Gold 1 and red 2 on the bounded oscillator at 50, blue 3 and purple 4 on the unbounded one at zero.',),
            origin='FIN1209 teaching chart B. The numbers are invented for teaching.',
            title='Crossing its equilibrium level is a buy or sell signal',
            letter='B',
            shows='Our bounded oscillator crossing above and below 50, and our unbounded oscillator crossing above and below zero.',
            tier='core',
            marks=(),
        ),
        WidePair(
            notes=('The book shows the same idea on a real chart. Gold 1 the RSI dropping below 50, red 2 the S above it, blue 3 the RSI climbing back above 50, purple 4 the B above it.',),
            origin='Lim (2016), p. 244, Figure 8.7. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.7 shows the RSI crossing its 50 percent level',
                lines=("Here is the RSI on Lim's daily chart of Goldman Sachs. It drops below its dashed 50 percent level [1]. Follow the vertical line up from there and Lim has marked a sell with an S [2]. Later the RSI climbs back above the level [3], and the next vertical line leads up to a buy, marked with a B [4] (p. 244).",),
                accent='The RSI gives the signal. The trigger to enter still has to come from price (pp. 241, 244).',
            ),
            picture=FIGURE_8_7,
            text_w=3.9,
        ),
        Content(
            notes=('Now the second crossover, on the same oscillator. It crosses a different line.',),
            origin='Lim (2016), p. 246.',
            title='Crossing its own average is a signal line crossover',
            lines=("A signal line is a moving average of the oscillator itself, so it lags it. Crossing above it is a buy signal and crossing below it a sell signal (p. 246).",
                   "Ours averages the last three readings. The oscillator from our equilibrium chart crosses above it [1] between readings 31 and 36 and below it [2] between 66 and 63."),
        ),
        course_chart('sg',
            notes=('Gold 1 the upward crossing of the signal line, red 2 the downward one. The first comes before the oscillator reaches 50.',),
            origin='FIN1209 teaching chart C. The numbers are invented for teaching.',
            title='Crossing its own average is a signal line crossover',
            letter='C',
            shows='Our oscillator and its signal line, the average of its last three readings, crossing twice.',
            tier='core',
            marks=(),
        ),
        # (e) One check and its answer on the next slide, the figure on both.
        StackedFigureCheck(
            notes=('Both answers come from the equilibrium crossover slides.',),
            origin='Questions are ours, answerable from the equilibrium crossover slides before; Lim (2016), p. 244.',
            label='Equilibrium crossovers',
            questions=(
                Question(
                    stem='On a bounded oscillator such as the RSI, which level is the equilibrium?',
                    options=('0 percent', '30 percent', '50 percent', '100 percent'),
                    answer='C',
                    reason='It runs 0 to 100 percent, so its equilibrium is 50 percent (p. 244).',
                ),
                Question(
                    stem='In the figure, the RSI drops below 50 at mark 1. What does Lim call that?',
                    options=('A buy signal', 'A sell signal', 'A trigger for entry', 'A signal line crossover'),
                    answer='B',
                    reason='Crossing below the equilibrium is a sell signal. Lim calls such signals, not triggers for entry (p. 244).',
                ),
            ),
            picture=FIGURE_8_7,
            text_w=5.3,
        ),
    ),
)

CHAPTER = Chapter(
    course='Technical Analysis in Investment',
    code='FIN1209',
    chapter='Chapter 8',
    title='Window Oscillators and Overlay Indicators',
    subtitle='Institute of Accounts, Business and Finance  |  Far Eastern University Manila',
    presenter='Benjamin C. Sotelo',
    title_notes=('Chapter 8 is where the oscillators used since Chapter 4 are finally taught.',
                 'Part A reads them and classifies indicators; Part B builds them one by one.'),
    objectives=('Understand the significance of oscillators and indicators and how to use them to forecast reversals and breakouts.',
                'Describe the difference between overlay indicators and window oscillators.',
                'Identify the types of overlay indicator and understand how chart scaling affects each.',
                'Set up multiple timeframe charts to better observe price and indicator action.'),
    roadmap=('Part A  8.1 and 8.2: classifying indicators and eight ways to read an oscillator',
             'Part B  8.3 to 8.8: cycles, timeframes, input data, trend trading, the oscillators and pivot points'),
    sections=(PART_A,),
    closing=(),
)

CHAPTER = expand_chart_pages(CHAPTER)
