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
FIGURE_8_1 = book_crop('8.1', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.1: a price chart with overlays on it, and under it the RSI and the stochastics, both bounded 0 to 100 percent, and the MACD, which is unbounded.",
    marks=(
        Mark(number=1, kind='box', x0=0.005, y0=0.0, x1=0.74, y1=0.485, color='gold', at=(0.77, 0.06), size=0.3),
        Mark(number=2, kind='box', x0=0.005, y0=0.495, x1=0.74, y1=0.60, color='red', at=(0.77, 0.545), size=0.3),
        Mark(number=3, kind='box', x0=0.005, y0=0.61, x1=0.74, y1=0.785, color='blue', at=(0.77, 0.70), size=0.3),
        Mark(number=4, kind='box', x0=0.005, y0=0.795, x1=0.74, y1=0.965, color='purple', at=(0.77, 0.88), size=0.3),
    ))
FIGURE_8_1.origin = 'Lim (2016), p. 238, Figure 8.1, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

# The book's own %K example, Figure 8.22. Its own numbers may sit on its own picture.
FIGURE_8_22 = book_crop('8.22', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.22: a bar with open 1.4590, high 1.5020, low 1.4900 and close 1.5000, and the working of %K as 83.3 percent.",
    marks=(
        Mark(number=1, kind='circle', x0=0.132, y0=0.331, x1=0.168, y1=0.397, color='gold', at=(0.075, 0.27), size=0.3),
        Mark(number=2, kind='circle', x0=0.292, y0=0.46, x1=0.328, y1=0.526, color='red', at=(0.245, 0.62), size=0.3),
        Mark(number=3, kind='circle', x0=0.292, y0=0.895, x1=0.328, y1=0.961, color='blue', at=(0.43, 0.90), size=0.3),
    ))
FIGURE_8_22.origin = 'Lim (2016), p. 260, Figure 8.22. The marks are ours, added for teaching.'

# (e) Figure 8.7, the RSI pane: where the RSI crosses its 50 percent level.
FIGURE_8_7 = book_crop('8.7', (0.0, 0.28, 0.56, 0.75),
    "Figure 8.7, cropped to its RSI: a line that rises and falls between 0 and 100 percent, crossing its dashed 50 percent level, with mark 1 on its first crossing downward and mark 2 on the next crossing upward.",
    marks=(
        Mark(number=1, kind='circle', x0=0.176, y0=0.652, x1=0.212, y1=0.692, color='gold', at=(0.235, 0.62), size=0.3),
        Mark(number=2, kind='circle', x0=0.248, y0=0.652, x1=0.284, y1=0.692, color='red', at=(0.31, 0.62), size=0.3),
    ))
FIGURE_8_7.origin = 'Lim (2016), p. 244, Figure 8.7, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

PART_A = Section(
    number=1,
    title='Indicators and Oscillators',
    short='8.1 and 8.2 samples',
    minutes='sample',
    covers=('indicator', 'overlay indicator', 'window oscillator', 'stochastic', 'crossover'),
    slides=(
        # (a) The opener: what we are talking about, and why, before any number.
        Content(
            notes=('This is the chapter opener. Say what an indicator is before showing any chart.',),
            origin='Lim (2016), p. 235.',
            title='Indicators show strength and weakness that price alone hides',
            lines=("So far we have read price directly: bars, patterns and trends. This chapter adds a second kind of tool, the indicator. Lim says oscillators and indicators can reveal underlying strengths and weaknesses of price action that would not have been obvious otherwise (p. 235).",
                   "We use them to forecast reversals and breakouts, the same two things the earlier chapters were after (p. 235)."),
            accent='An indicator is a second view of the same market, calculated from price.',
        ),
        Content(
            notes=('Two names to learn: overlay indicator and window oscillator. The next slide shows both on one chart.',),
            origin='Lim (2016), pp. 235 to 236.',
            title='Indicators come in two kinds: overlays and window oscillators',
            lines=("Lim sorts indicators into two categories (p. 235). An overlay indicator is plotted on the same chart as price, where it acts as a barrier, that is, support and resistance (p. 235).",
                   "A window oscillator is a mathematically derived indicator, normally based on open, high, low and close, volume or open interest, drawn in a window of its own (p. 236)."),
            accent='Overlays sit on the price chart. Window oscillators get a window of their own.',
        ),
        # (b) A book figure read with numbered marks.
        WidePair(
            notes=('Walk the four boxes top to bottom: gold 1 price with overlays, red 2 the RSI, blue 3 the stochastics, purple 4 the MACD.',
                   'Bounded and unbounded are taught on the next slides; here only read what Lim labels.'),
            origin='Lim (2016), p. 238, Figure 8.1. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.1 puts both kinds of indicator on one chart',
                lines=("The top part is price, with overlay indicators drawn on it [1]. Under it sit three window oscillators: the RSI [2], the stochastics [3] and the MACD [4].",
                       "Lim labels the RSI and the stochastics bounded, 0 to 100 percent, and the MACD unbounded (p. 238)."),
                accent='Bounded and unbounded come next.',
            ),
            picture=FIGURE_8_1,
            text_w=4.2,
        ),
        # The idea named before the numbers: raw %K.
        Content(
            notes=('Name the idea first: where does the close sit in the recent range?', 'The numbers come two slides on.'),
            origin='Lim (2016), pp. 259 to 260.',
            title='The stochastic asks where the close sits in the recent range',
            lines=("The stochastic is one of the window oscillators we just saw on the chart. Lim describes it as tracking the position of the latest close as a percentage of the price range over a chosen number of periods, measured from the lowest low of that range. The result is called the raw %K (p. 259).",
                   "In Lim's notation, C is the closing price, Ln the lowest low of the last n periods and Hn the highest high. Raw %K = (C - Ln) / (Hn - Ln) x 100 percent (p. 260). The usual lookback is 14 periods (p. 259)."),
            accent='Close at the lowest low gives 0 percent. Close at the highest high gives 100 percent.',
        ),
        Content(
            notes=('Why bounded: the top of the fraction can never exceed the bottom.',),
            origin='Lim (2016), p. 260.',
            title='Raw %K always stays between 0 and 100 percent',
            lines=("The close can never be below the lowest low or above the highest high of the same lookback. So the top of the fraction is never larger than the bottom, and %K stays between 0 and 100 percent (p. 260).",
                   "That is what Lim means by a bounded oscillator: its readings are confined to 0 to 100 percent (p. 236). Lim labels the stochastics and the RSI bounded this way (p. 238)."),
        ),
        WidePair(
            notes=('This is the book\'s own example, so its numbers belong on its own picture.',
                   'Gold 1 the high, 100 percent. Red 2 the close. Blue 3 the low, 0 percent.',
                   'The table says open 1.4590 but the bar is drawn with its open at 1.4950. %K does not use the open, so the answer is unaffected.'),
            origin='Lim (2016), p. 260, Figure 8.22. The marks are ours, added for teaching.',
            left=Content(
                title="The book's example puts the close at 83.3 percent of the range",
                lines=("Lim's bar has a high of 1.5020 [1], a close of 1.5000 [2] and a low of 1.4900 [3]. So %K = (1.5000 - 1.4900) / (1.5020 - 1.4900) x 100 = 83.3 percent (p. 260).",
                       "The table gives the open as 1.4590 but the bar is drawn with it at 1.4950, and the book does not say which is right. %K does not use the open."),
                accent='83.3 percent: the close sits well toward the top of the range.',
            ),
            picture=FIGURE_8_22,
            text_w=4.9,
        ),
        # (c) A worked example on our own chart.
        Content(
            notes=('Same formula, our own numbers. Say plainly that the numbers are made up.',),
            origin='Lim (2016), p. 260 for the formula. The numbers are ours, made up for teaching.',
            title='A raw %K worked on a bar of ours',
            lines=("Now the same formula with numbers of ours, made up to show the idea. Over the last 14 bars the highest high is PHP 56.00 [1] and the lowest low is PHP 50.00 [2]. Today's close is PHP 54.00 [3].",
                   "So %K = (54.00 - 50.00) / (56.00 - 50.00) x 100 = 4.00 / 6.00 x 100 = 66.7 percent. The close sits two thirds of the way up the range."),
        ),
        course_chart('k',
            notes=('Gold 1 is the highest high, 100 percent. Red 2 is the lowest low, 0 percent. Blue 3 is the close.',),
            origin='FIN1209 teaching chart A. The numbers are invented for teaching.',
            title='A raw %K worked on a bar of ours',
            letter='A',
            shows='Our bar with its close at PHP 54.00 between a highest high of PHP 56.00 and a lowest low of PHP 50.00, giving a raw %K of 66.7 percent.',
            tier='core',
            marks=(),
        ),
        CourseCheck(
            notes=('Both answers come from the raw %K slides. Do not reveal them here.',),
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
                    reason='%K is 100 percent only when C equals Hn, so the numerator and denominator match (p. 260).',
                ),
            ),
        ),
        # (d) Two look-alikes, each on its own slide with its own chart.
        Content(
            notes=('Two crossovers sound alike. Take the first alone, then the second.',),
            origin='Lim (2016), p. 244.',
            title='Crossing the middle of its range is an equilibrium crossover',
            lines=("An oscillator can be read by its equilibrium, the central value it swings around: 50 percent for a bounded oscillator, zero for an unbounded one (p. 244). Crossing above is a buy signal and crossing below a sell signal (p. 244).",
                   "Our oscillator runs 0 to 100. It crosses above 50 [1] between readings 44 and 53 and below 50 [2] between 55 and 47."),
        ),
        course_chart('eq',
            notes=('Gold 1 the upward crossing of 50, red 2 the downward crossing.',),
            origin='FIN1209 teaching chart B. The numbers are invented for teaching.',
            title='Crossing the middle of its range is an equilibrium crossover',
            letter='B',
            shows='Our oscillator crossing above and then below its 50 percent equilibrium.',
            tier='core',
            marks=(),
        ),
        WidePair(
            notes=('The book shows the same idea on a real chart. Gold 1 the RSI crossing below 50, red 2 crossing back above.',),
            origin='Lim (2016), p. 244, Figure 8.7. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.7 shows the RSI crossing its 50 percent level',
                lines=("Lim's RSI, a bounded oscillator, crosses below its dashed 50 percent level at mark 1 [1], a sell signal, and back above it at mark 2 [2], a buy signal (p. 244).",),
                accent='The signal comes from the RSI. Lim still waits for price to trigger the trade.',
            ),
            picture=FIGURE_8_7,
            text_w=3.6,
        ),
        Content(
            notes=('Now the second crossover, on the same oscillator. It crosses a different line.',),
            origin='Lim (2016), p. 246.',
            title='Crossing its own average is a signal line crossover',
            lines=("A signal line is a moving average of the oscillator itself, so it lags the oscillator (p. 246). Crossing above the signal line is a buy signal and crossing below it a sell signal (p. 246).",
                   "Ours is the average of the last three readings. The same oscillator crosses above it [1] between readings 31 and 36 and below it [2] between 66 and 63."),
        ),
        course_chart('sg',
            notes=('Gold 1 the upward crossing of the signal line, red 2 the downward one. Note the first comes before the oscillator reaches 50.',),
            origin='FIN1209 teaching chart C. The numbers are invented for teaching.',
            title='Crossing its own average is a signal line crossover',
            letter='C',
            shows='Our oscillator and its signal line, the average of its last three readings, crossing twice.',
            tier='core',
            marks=(),
        ),
        # (e) One check and its answer on the next slide, the figure on both.
        CourseFigureCheck(
            notes=('Both answers come from the equilibrium crossover slides. Do not reveal them here.',),
            origin='Questions are ours, answerable from the equilibrium crossover slides before; Lim (2016), p. 244.',
            label='Equilibrium crossovers',
            questions=(
                Question(
                    stem='On a bounded oscillator such as the RSI, which level is the equilibrium that a crossover is read against?',
                    options=('0 percent', '30 percent', '50 percent', '100 percent'),
                    answer='C',
                    reason='It runs 0 to 100 percent, so its equilibrium is 50 percent (p. 244).',
                ),
                Question(
                    stem='In the figure, the RSI crosses below its 50 percent level at mark 1. What does Lim call that?',
                    options=('A buy signal', 'A sell signal', 'A trigger for entry', 'A signal line crossover'),
                    answer='B',
                    reason='Crossing below the equilibrium is a sell signal. Lim calls such signals, not triggers for entry (p. 244).',
                ),
            ),
            picture=FIGURE_8_7,
            text_w=6.8,
        ),
    ),
)

CHAPTER = Chapter(
    course='Technical Analysis in Investment',
    code='FIN1209',
    chapter='Chapter 8',
    title='Window Oscillators and Overlay Indicators',
    subtitle='Indicators are calculated from price and drawn on the chart. Learn what kinds there are, how to read an oscillator, and why a signal still waits for price to confirm it.',
    presenter='Faculty of Economics University',
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
