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
from chartlayout_chapter08 import (CourseCheck, CourseFigureCheck, WidePair, book_crop,
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

# The book's own %K example, Figure 8.22. Its own numbers may sit on its own picture.
# Rings sit on the bar itself: the top of the wick, the bottom of the wick, the top of the body where the close dash starts.
FIGURE_8_22 = book_crop('8.22', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.22: a bar with open 1.4590, high 1.5020, low 1.4900 and close 1.5000, and the working of raw %K as 83.3 percent.",
    marks=(
        Mark(number=1, kind='circle', x0=0.172, y0=0.332, x1=0.208, y1=0.396, color='gold', at=(0.255, 0.43), size=0.3),
        Mark(number=2, kind='circle', x0=0.172, y0=0.90, x1=0.208, y1=0.964, color='red', at=(0.26, 0.82), size=0.3),
        Mark(number=3, kind='circle', x0=0.187, y0=0.462, x1=0.223, y1=0.526, color='blue', at=(0.11, 0.58), size=0.3),
    ))
FIGURE_8_22.origin = 'Lim (2016), p. 260, Figure 8.22. The marks are ours, added for teaching.'

# (e) Figure 8.7: the RSI crossing its dashed 50 percent level, with Lim's S and B on the price above it.
FIGURE_8_7 = book_crop('8.7', (0.33, 0.08, 1.0, 0.75),
    "Figure 8.7, cropped to its second pair of crossings: the price chart with Lim's S and B letters, and under it the RSI with its dashed 50 percent level and its axis, mark 1 where the RSI drops below 50 and mark 2 where it climbs back above.",
    marks=(
        Mark(number=1, kind='circle', x0=0.472, y0=0.653, x1=0.508, y1=0.695, color='gold', at=(0.45, 0.725), size=0.3),
        Mark(number=2, kind='circle', x0=0.527, y0=0.651, x1=0.563, y1=0.693, color='red', at=(0.585, 0.725), size=0.3),
    ))
FIGURE_8_7.origin = 'Lim (2016), p. 244, Figure 8.7, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

PART_A = Section(
    number=1,
    title='Sample slides for approval',
    short='Chapter 8 samples',
    minutes='',
    covers=('indicator', 'overlay indicator', 'window oscillator', 'stochastic', 'crossover'),
    slides=(
        # (a) The opener: what we are talking about, and why, before any number.
        Content(
            notes=('Open by saying what the chapter is: the place where the oscillators used since Chapter 4 finally get taught.',),
            origin='Lim (2016), p. 235; Chapter 6, "What the book uses here and teaches later, or never".',
            title='Indicators show strength and weakness that price alone hides',
            lines=("Up to now we have mostly read price itself: bars, patterns and trends. The book has also kept using indicators such as the MACD, the RSI and the stochastic without explaining them, and Chapter 6 told you Chapter 8 is where oscillators get taught. This is that chapter.",
                   "Why bother? Lim says oscillators and indicators can reveal underlying strengths and weaknesses of price action that would not have been obvious otherwise, which helps us forecast potential reversals and breakouts (p. 235)."),
            accent='Indicators can show you strength or weakness you would not have spotted from price alone.',
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
                       "Notice Lim draws overlays on the MACD window as well."),
                accent='Price and its overlays on top. Oscillators in their own windows below.',
            ),
            picture=FIGURE_8_1,
            text_w=4.4,
        ),
        # A reference slide: what Part A only reads and Part B builds.
        Content(
            notes=('Part A reads these oscillators on charts. Part B builds each one. Do not teach the calculations here.',),
            origin='Lim (2016), pp. 236, 241, 244, 251, 256, 257, 259 and 262.',
            title='The oscillators you will meet before we build them (1 of 2)',
            lines=("Part A only reads these oscillators on Lim's charts. Part B builds each one, in this order.",
                   "Bounded, 0 to 100 percent: the RSI tracks a stock's strength through its average gain and loss over the last n periods (p. 262). The stochastic is the position of the latest close in the recent price range (p. 259). The StochRSI is the stochastic calculation applied to RSI values (p. 251).",
                   "Overbought and oversold are the high and low ends of an oscillator's readings, which Lim calls overextensions (pp. 236, 241). Equilibrium is the central value it swings around (p. 244)."),
        ),
        Content(
            notes=('The unbounded ones. Part B builds the MACD, ROC and MOM; the CCI has no calculation in this chapter.',),
            origin='Lim (2016), pp. 242, 244, 256 and 257.',
            title='The oscillators you will meet before we build them (2 of 2)',
            lines=("Unbounded, no top or bottom: the MACD is the 12-period EMA minus the 26-period EMA (p. 257). The ROC is the percent change in price over N periods and the MOM the price difference over N periods (p. 256).",
                   "The CCI, the commodity channel index, gets an overbought level of plus 100 and an oversold level of minus 100 (pp. 242, 244). This chapter gives no calculation for it.",
                   "Where you meet one of these before Part B builds it, the slide says what you need and no more."),
        ),
        # The idea named before the numbers: raw %K.
        Content(
            notes=('Name the idea first: where does the latest close sit in the recent range? The formula comes on the next slide.',),
            origin='Lim (2016), p. 259.',
            title='The stochastic asks where the close sits in the recent range',
            lines=("The stochastic is one of the oscillators from our list. Now we build it. It answers one question: is the latest close near the top or near the bottom of the recent range?",
                   "Lim describes it as the position of the latest close as a percentage of the price range over a chosen number of periods, measured from the lowest low. The result is called the raw %K (p. 259)."),
            accent='Raw %K: where the latest close sits in the recent range, as a percentage.',
        ),
        Content(
            notes=('Chapter 5 taught the bar stochastic inside one bar; the raw %K does the same over n periods.', 'The slide on the next page says why raw %K cannot leave 0 to 100.'),
            origin='Lim (2016), pp. 259 to 260; Chapter 5, "Bar stochastic".',
            title='Raw %K compares the close with the n-bar high and low',
            lines=("Chapter 5's bar stochastic asked this inside one bar, (C - L) / (H - L). The raw %K asks it over n periods. C is the closing price, Ln the lowest low of the last n periods and Hn the highest high.",
                   "Raw %K = (C - Ln) / (Hn - Ln) x 100 percent (p. 260). The usual lookback is 14 periods (p. 259)."),
            accent='Close at the lowest low gives 0 percent. Close at the highest high gives 100 percent.',
        ),
        Content(
            notes=('Why bounded: the top of the fraction can never exceed the bottom. Lim says this of the RSI on p. 262.',),
            origin='Lim (2016), pp. 236, 260 and 262.',
            title='Raw %K always stays between 0 and 100 percent',
            lines=("The close can never be below the lowest low or above the highest high of the same lookback. So the top of the fraction is never larger than the bottom, and raw %K stays between 0 and 100 percent (pp. 260, 262).",
                   "That makes it a bounded oscillator, the kind from Part A."),
            accent="Every stock's raw %K runs on the same 0 to 100 scale, which is why Lim says bounded oscillators can be compared between stocks or markets (p. 236).",
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
            notes=('The book shows the same idea on a real chart. Gold 1 the RSI dropping below 50, red 2 climbing back above.',),
            origin='Lim (2016), p. 244, Figure 8.7. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.7 shows the RSI crossing its 50 percent level',
                lines=("Here is the RSI on Lim's daily chart of Goldman Sachs. It drops below its dashed 50 percent level [1], and Lim marks a sell with an S on the price chart. Later it climbs back above [2], and Lim marks a buy with a B (p. 244).",),
                accent='The RSI gives the signal. The trigger to enter still has to come from price (pp. 241, 244).',
            ),
            picture=FIGURE_8_7,
            text_w=4.2,
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
        CourseFigureCheck(
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
            text_w=6.3,
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
