"""second class slides, sections 8.3, 8.4 and 8.5 (outline rows 1 to 44), written by hand in teaching order.

A Content slide written in front of a chart is folded onto the chart's own slide by
expand_chart_pages, so a row that is a text slide and the row for its chart are one slide.
Every number on a chart is ours, invented for teaching; every Lim figure is read with Lim's
words only, and our numbers never go on his picture. Marks on Lim's figures are fractions of
the whole master figure, read off a grid and checked on a zoomed crop.
"""
from deckkit import Content, Mark, Question
from chartlayout_chapter08 import CourseCheck, TopPair, WidePair, book_crop, course_chart
from samples_chapter08 import FIGURE_8_17, FIGURE_8_7_CCI, FIGURE_8_8
from slides_a2 import B, G, M, P, R, fig
from slides_a2 import pair as _pair

OUR = 'The numbers are invented for teaching.'
LETTERS = 'ACBDABCADBCADCBAADBCADCA'   # the answer key of the second class, question by question
TABLES = {'BA': "FIN1209 table, from Lim's three formulas (p. 252).", 'BC': "FIN1209 table, from the book's own numbers (p. 253).",
          'BE': "FIN1209 table: the book's method (p. 253), worked on our numbers.", 'BF': "FIN1209 table, worked by the book's method (p. 253).",
          'BH': "FIN1209 table, from Lim's list (p. 253)."}


def chart(asset, letter, title, shows, notes):
    origin = TABLES.get(letter, f'FIN1209 teaching chart {letter}. ' + OUR)
    return course_chart(asset, notes=notes, origin=origin, title=title, letter=letter, shows=shows, tier='core', marks=())


def Q(n, stem, right, wrong, reason):
    """Question n of the second class: the right option goes where the key says, the rest keep their order."""
    at = 'ABCD'.index(LETTERS[n - 1])
    options = list(wrong)
    options.insert(at, right)
    return Question(stem=stem, options=tuple(options), answer=LETTERS[n - 1], reason=reason)


# ---------------------------------------------------------------- Lim's figure 8.16
F816_ALL = fig('8.16', (0, 0, 1, 1), 'Figure 8.16: the GBPUSD daily chart with six measured cycles, the label Dominant cycle = 75 bars, the 38 period cycle-tuned stochastic under the price and the default 14 period stochastic under that.',
               [M(1, G, 0.062, 0.185, 0.385, 0.28, at=(0.415, 0.23)), M(2, R, 0.335, 0.435, 0.46, 0.565, at=(0.31, 0.50)),
                M(3, B, 0.205, 0.895, 0.375, 0.985, at=(0.18, 0.945))], 252)
F816_CYC = fig('8.16', (0, 0, 1, 0.62), "Figure 8.16, cropped to the price chart: six cycles measured from trough to trough, 78, 75, 78, 105, 68 and 47 bars, and the label Dominant cycle = 75 bars.",
               [M(1, G, 0.125, 0.135, 0.215, 0.135, at=(0.17, 0.175), kind='line'), M(2, R, 0.222, 0.135, 0.303, 0.135, at=(0.262, 0.175), kind='line'),
                M(3, B, 0.31, 0.135, 0.395, 0.135, at=(0.352, 0.175), kind='line'), M(4, P, 0.405, 0.135, 0.515, 0.135, at=(0.46, 0.175), kind='line'),
                M(5, G, 0.524, 0.135, 0.596, 0.135, at=(0.56, 0.175), kind='line'), M(6, R, 0.604, 0.135, 0.668, 0.135, at=(0.695, 0.09), kind='line'),
                M(7, B, 0.062, 0.29, 0.385, 0.29, kind='line', at=(0.415, 0.29))], 252)
F816_OSC = fig('8.16', (0, 0.6, 1, 1), "Figure 8.16, cropped to its two stochastics: the 38 period cycle-tuned one with its circled troughs, and under it the default 14 period one.",
               [M(1, G, 0.0, 0.68, 0.975, 0.752, at=(0.988, 0.665)), M(2, R, 0.0, 0.762, 0.975, 0.895, at=(0.988, 0.835))], 253)
F816_MATH = fig('8.16', (0, 0, 1, 0.62), "Figure 8.16, cropped to the price chart again: the six measured cycles and, on the right, Lim's working for the half cycle.",
                [M(1, G, 0.12, 0.04, 0.672, 0.125, at=(0.095, 0.085)), M(2, R, 0.49, 0.345, 0.945, 0.52, at=(0.465, 0.43))], 252)

# Figure 8.17, cropped to its three oscillator windows. Mark pairs sit on the same weeks: the StochRSI above, the RSI below.
F817_RESP = fig('8.17', (0, 0.46, 1, 1), 'Figure 8.17, cropped to its three oscillator windows. From the top: the StochRSI, the slow stochastic and the RSI, under the Dow Jones.',
                [M(1, G, 0.292, 0.518, 0.348, 0.668, at=(0.27, 0.60)), M(2, R, 0.292, 0.878, 0.348, 0.93, at=(0.32, 0.955)),
                 M(3, B, 0.37, 0.518, 0.408, 0.668, at=(0.425, 0.60)), M(4, P, 0.37, 0.878, 0.408, 0.93, at=(0.39, 0.955))], 254, 'sc')
F817_ALL = fig('8.17', (0, 0.46, 1, 1), 'Figure 8.17, cropped to its three oscillator windows. From the top: the StochRSI, the slow stochastic and the RSI, under the Dow Jones.',
               [M(1, G, 0.005, 0.508, 0.91, 0.668, at=(1.035, 0.59)), M(2, R, 0.005, 0.672, 0.91, 0.83, at=(1.035, 0.75)),
                M(3, B, 0.005, 0.834, 0.91, 0.995, at=(1.035, 0.915))], 254, 'sc')


def pair(title, lines, picture, notes, origin, accent='', w=4.4):
    return _pair(title, (lines,) if isinstance(lines, str) else tuple(lines), picture, notes, origin, accent, w)


def top(title, lines, picture, notes, origin):
    return TopPair(notes=notes, origin=origin, left=Content(title=title, lines=(lines,) if isinstance(lines, str) else tuple(lines)),
                   picture=picture, text_w=8.0)


def _m(n, color, x0, y0, x1, y1, at, kind='box'):
    return Mark(number=n, kind=kind, x0=x0, y0=y0, x1=x1, y1=y1, color=color, at=at, size=0.28)


REF_17 = book_crop('8.17', (0.0, 0.30, 1.0, 1.0), FIGURE_8_17.shows,
                   marks=(_m(1, 'gold', 0.005, 0.834, 0.91, 0.995, (1.035, 0.915)), _m(2, 'red', 0.005, 0.672, 0.91, 0.83, (1.035, 0.75)),
                          _m(3, 'blue', 0.005, 0.508, 0.91, 0.668, (1.035, 0.59))))
REF_17.origin = FIGURE_8_17.origin
REF_88 = book_crop('8.8', (0.0, 0.30, 1.0, 1.0), FIGURE_8_8.shows,
                   marks=(_m(1, 'gold', 0.005, 0.662, 0.935, 0.812, (1.035, 0.74)), _m(2, 'red', 0.005, 0.816, 0.935, 0.985, (1.035, 0.90))))
REF_88.origin = FIGURE_8_8.origin
REF_CCI = book_crop('8.7', (0.0, 0.5, 1.0, 1.0), FIGURE_8_7_CCI.shows,
                    marks=(_m(1, 'gold', 0.005, 0.814, 0.93, 0.992, (0.45, 0.795)), _m(2, 'red', 0.60, 0.892, 0.80, 0.892, (1.035, 0.862), 'line'),
                           _m(3, 'blue', 0.60, 0.9375, 0.80, 0.9375, (1.035, 0.968), 'line')))
REF_CCI.origin = FIGURE_8_7_CCI.origin


def reference(title, lines, picture, notes, page, w=4.9):
    return pair(title, lines, picture, notes, f"Lim (2016), p. {page}. The marks are ours, added for teaching.", w=w)


def slides(S):
    """S is the tuple of approved sample slides; this returns the slides of 8.3, 8.4 and 8.5."""
    return (
        # ---- rows 1 to 3: the oscillators again, before they are tuned
        WidePair(
            notes=('The same Figure 8.17 as the first class. Now they are tuned and then built.',),
            origin='Lim (2016), pp. 251, 254, 259 and 262, Figure 8.17. The marks are ours, added for teaching.',
            left=Content(
                title='The bounded oscillators we now tune and build (1 of 3)',
                lines=("We tune these, then build them. The bounded oscillators, 0 to 100 percent, are the relative strength index or RSI [1], average gain over average loss; the stochastic [2], where the close sits in the recent range; and the StochRSI [3], the stochastic applied to RSI values. First we tune each one's lookback, the number of periods it looks back over (p. 252). Lim prints the StochRSI from 0 to 1.",),
            ),
            picture=REF_17, text_w=3.7),
        WidePair(
            notes=('The same Figure 8.8 as the first class.',),
            origin='Lim (2016), pp. 245, 253 and 257, Figure 8.8. The marks are ours, added for teaching.',
            left=Content(
                title='The unbounded oscillators we now tune and build (2 of 3)',
                lines=("The moving average convergence divergence or MACD [1] and the rate of change or ROC [2] are unbounded. The MACD has three numbers to set: a 12 period and a 26 period moving average and a 9 period signal line (pp. 253, 257). When we move to another timeframe in a few slides, all three change.",),
            ),
            picture=REF_88, text_w=4.6),
        top('The unbounded oscillators we now tune and build (3 of 3)',
            "The commodity channel index or CCI [1] is the last on our list, with its plus 100 line [2] and minus 100 line [3] (pp. 242, 244). The chapter gives no calculation for it, so we do not tune or build it. The rest of the list is built in this class, and so are two more: the momentum oscillator, MOM, and the average true range, ATR.",
            REF_CCI, ('The same lower half of Figure 8.7 as the first class.',), 'Lim (2016), pp. 242 and 244, Figure 8.7. The marks are ours, added for teaching.'),
        # ---- row 4: tune to the cycle
        top('Tune an oscillator to the cycle, not just the default',
            "Lim says oscillators and most overlays normally give better signals tuned to the dominant half cycle, half the dominant cycle's length, than at the default lookback, which may give too few or too many (p. 252). On Figure 8.16 see his labels for the dominant cycle [1], the tuned stochastic [2] and the default 14 period [3].",
            F816_ALL, ('Gold 1 the dominant cycle label, red 2 the tuned stochastic, blue 3 the default stochastic.', 'Say that Lim does not define dominant.'), 'Lim (2016), p. 252, Figure 8.16. The marks are ours, added for teaching.'),
        # ---- rows 5 and 8: the first formula
        Content(
            notes=('Formula 1 and our chart of it.', 'Gold 1 and red 2 the two troughs, blue 3 the half cycle.'),
            origin="Lim (2016), p. 252. " + OUR,
            title='Half the cycle, formula 1: (N + 1) / 2',
            lines=("Lim gives three ways to find the half cycle from the period N of the dominant cycle, and sends worked examples of them to Chapter 12 (p. 252). The first is (N + 1) / 2, rounded up if N is even. On our chart the troughs [1] [2] are 76 bars apart, so N is 76, and half of it is (76 + 1) / 2 = 38.5, rounded up to 39 bars [3]: our lookback.",),
        ),
        chart('cy1', 'AY', 'Half the cycle, formula 1: (N + 1) / 2',
              'Our cycle of 76 bars from one trough to the next, and a bracket for its half, 39 bars.',
              ('Gold 1 and red 2 the two troughs 76 bars apart, blue 3 the end of the 39 bar half cycle.',)),
        # ---- rows 6 and 7: the second and third formulas on one cycle of 75
        Content(
            notes=('Formula 2 on a cycle of 75.', 'Gold 1 and red 2 the troughs, blue 3 the half cycle.'),
            origin="Lim (2016), p. 252. " + OUR,
            title='Half the cycle, formula 2: (N / 2) + 1',
            lines=("The second is (N / 2) + 1, rounded down if N is odd (p. 252). On our second cycle the troughs [1] [2] are 75 bars apart, so N is 75, which is odd. (75 / 2) + 1 = 38.5, rounded down to 38 [3].",),
        ),
        chart('cy2a', 'CR', 'Half the cycle, formula 2: (N / 2) + 1',
              'Our cycle of 75 bars from one trough to the next, and a bracket for its half, 38 bars, worked two ways.',
              ('Gold 1 and red 2 the two troughs 75 bars apart, blue 3 the end of the 38 bar half cycle.',)),
        Content(
            notes=('Formula 3 on the same cycle of 75.', 'Two formulas, one lookback.'),
            origin="Lim (2016), p. 252. " + OUR,
            title='Half the cycle, formula 3: (2N + 3) / 4',
            lines=("The third is (2N + 3) / 4, rounded to the closest whole number (p. 252). On the same cycle, N = 75 [1] [2]: (2 x 75 + 3) / 4 = 38.25, which rounds to 38 [3]. Formulas 2 and 3 give the same lookback here.",),
        ),
        chart('cy2', 'AZ', 'Half the cycle, formula 3: (2N + 3) / 4',
              'The same cycle of 75 bars and its 38 bar half, worked two ways.',
              ('Gold 1 and red 2 the troughs, blue 3 the half cycle.',)),
        # ---- row 9: the book's example in a table
        Content(
            notes=("Lim's own example, then all three formulas on it.",),
            origin='Lim (2016), p. 252. The all-three comparison is our arithmetic.',
            title="The book's example: a cycle of 75 days gives 38",
            lines=("Lim's example is the GBPUSD currency pair on a daily chart, 2005 to 2007, where the average dominant cycle is 75 days (p. 252). He works only the second formula: 75 / 2 + 1 = 38.5, rounded down because 75 is odd, so the stochastic's lookback is 38. That all three formulas give 38 for N = 75 is our arithmetic; the first needs no rounding at all.",),
        ),
        chart('t3', 'BA', "The book's example: a cycle of 75 days gives 38",
              'A table of the three half cycle formulas worked on N = 75, each giving 38.',
              ('All three formulas give 38 for N = 75.',)),
        # ---- row 10: the six cycles on Figure 8.16
        top('Figure 8.16: six cycles and their dominant length',
             ("Figure 8.16 is Lim's example. He measures six cycles from trough to trough: 78 [1], 75 [2], 78 [3], 105 [4], 68 [5] and 47 [6] bars, and labels the average \"Dominant cycle = 75 bars\" [7] (p. 252)."),
             F816_CYC, ('Gold 1 to purple 4, then 5 and 6, the six lengths; blue 7 the label.',), 'Lim (2016), p. 252, Figure 8.16. The marks are ours, added for teaching.'),
        # ---- row 11: the tuned stochastic against the default
        top('Figure 8.16: the 38 period stochastic against the default',
             ("Lim set the stochastic's lookback to 38. His circles [1] mark the troughs it forecast: he says the 38 period setting tracked and forecast the cycle troughs perfectly, including on out of sample data, the period after the sample period (p. 252). The standard 14 period stochastic under it [2] generated too many oversold signals (p. 253)."),
             F816_OSC, ('Gold 1 the circled troughs, red 2 the default 14 period panel.',), 'Lim (2016), pp. 252 and 253, Figure 8.16. The marks are ours, added for teaching.'),
        # ---- row 12: the figure's own arithmetic
        top("Checking the figure's own arithmetic",
             ("The six lengths [1] add to 78 + 75 + 78 + 105 + 68 + 47 = 451, so they average 75.2; the figure prints 75.1. Its working [2] halves that and rounds up to 38 bars (p. 252). The text adds 1 and rounds down: 75 / 2 + 1 = 38.5, down to 38. The two workings differ and give the same 38."),
             F816_MATH, ('Gold 1 the six lengths, red 2 the figure working.', 'Say the figure halves; the text adds 1.'), 'Lim (2016), p. 252, Figure 8.16. The marks are ours, added for teaching.'),
        # ---- rows 13 and 14: Check 12
        CourseCheck(
            notes=('Both answers come from the half cycle slides.',),
            origin='Questions are ours, answerable from the half cycle slides before; Lim (2016), p. 252.',
            label='The half cycle',
            questions=(
                Q(1, 'A dominant cycle averages 75 bars. Using Lim\'s second formula, (N / 2) + 1, what lookback do we set?', '38', ('37', '39', '75'),
                  '75 / 2 + 1 = 38.5. N is odd, so round down to 38 (p. 252).'),
                Q(2, 'Lim works the half cycle of the 75 day cycle two ways: halving the average and rounding up, or adding 1 and rounding down. What does each give?', 'Both give 38',
                  ('The first gives 38 and the second 39', 'The first gives 37 and the second 38', 'Both give 75'),
                  'Halving the average, 75.1, and rounding up gives 38; adding 1 to half of 75 and rounding down gives 38 (p. 252).'),
            ),
        ),
        # ---- rows 15 to 19: several timeframes
        Content(
            notes=('Three RSI lines on one chart.', 'Gold 1 the 5 minute RSI, red 2 the 15 minute, blue 3 the hourly.'),
            origin='Lim (2016), p. 253. ' + OUR,
            title='Several timeframes on one chart',
            lines=("Plot the same indicator from several timeframes on one chart, for more effective comparison of oscillator action and price action (p. 253). Lim's example is the 5 minute, 15 minute and 1 hour RSI on a 5 minute chart. Our lines are made up: the swing of the 5 minute RSI [1] is widest, the 15 minute [2] narrower, the hourly [3] narrowest.",),
        ),
        chart('mtf', 'BB', 'Several timeframes on one chart',
              'Three RSI lines of ours, one for each timeframe, the 5 minute one jumpy and the hourly one smooth.',
              ('Gold 1 the 5 minute RSI, red 2 the 15 minute RSI, blue 3 the hourly RSI.',)),
        Content(
            notes=('MF is the indicator timeframe over the chart timeframe.',),
            origin='Lim (2016), p. 253. The table is ours, from the book\'s numbers.',
            title='The multiplying factor',
            lines=("A 5 minute chart can show a 15 minute indicator because of the multiplying factor, MF: the indicator's timeframe divided by the chart's timeframe (p. 253). For the 15 minute RSI, MF = 15 / 5 = 3. For the 1 hour RSI, which is 60 minutes, MF = 60 / 5 = 12.",),
        ),
        chart('mf', 'BC', 'The multiplying factor',
              'A table of the multiplying factor for a 5, a 15 and a 60 minute indicator on a 5 minute chart.',
              ('MF is 1, 3 and 12.',)),
        Content(
            notes=('14 x 3 = 42 and 14 x 12 = 168.', 'Gold 1 the 14 period swing, red 2 the 42 period line at the same time.'),
            origin='Lim (2016), pp. 253 and 262. ' + OUR,
            title='A 14 period RSI becomes 42 and 168',
            lines=("To put a 15 minute RSI on a 5 minute chart, multiply its 14 periods by the MF: 14 x 3 = 42. The hourly RSI is 14 x 12 = 168 (p. 253). On our closes the 14 period RSI [1] swings from about 10 to 89 and the 42 period RSI [2] only from about 40 to 60. Ours uses plain averages of gains and losses; the RSI's own averaging is built in 8.6.",),
        ),
        chart('rsi42', 'BD', 'A 14 period RSI becomes 42 and 168',
              'Our closes with a 14 period RSI that swings widely and a 42 period RSI that stays near the middle.',
              ('Gold 1 the 14 period RSI at one bar, red 2 the 42 period RSI at the same bar.',)),
        Content(
            notes=('Increase all the variables.', 'The book works only the moving average.'),
            origin='Lim (2016), p. 253. The MACD numbers are ours, worked by the book\'s method.',
            title='The MACD: every number is multiplied',
            lines=("Lim says to increase all the variables via the MF (p. 253). The MACD, built in 8.6, has a 12 period and a 26 period average and a 9 period signal line. For a 15 minute MACD on a 5 minute chart MF = 3, so they become 36, 78 and 27 (ours). His example: a 20 period hourly average is 240 periods on a 5 minute chart, differing very slightly from the real one (p. 253).",),
        ),
        chart('mfm', 'BE', 'The MACD: every number is multiplied',
              'A table of the MACD settings 12, 26 and 9 multiplied by 3, and the book\'s 20 period moving average multiplied by 12 to give 240.',
              ('36, 78, 27 and 240.',)),
        Content(
            notes=('Review question 7.', 'The numbers are ours; the book does not print them.'),
            origin='Lim (2016), pp. 253 and 266, review question 7. The numbers are ours, worked by the book\'s method.',
            title='Review question 7: hourly and 4 hour MACD',
            lines=("Lim's review question 7 asks for the MACD of two higher timeframes on a 15 minute chart (p. 266). For the hourly, MF = 60 / 15 = 4, so 12, 26 and 9 become 48, 104 and 36. For the 4 hour, 240 minutes, MF = 240 / 15 = 16, so they become 192, 416 and 144. The book does not print these numbers; they are ours, worked by its method.",),
        ),
        chart('rq7', 'BF', 'Review question 7: hourly and 4 hour MACD',
              'A table of the MACD settings on a 15 minute chart for the hourly and the 4 hour timeframes.',
              ('Hourly 48, 104, 36; 4 hour 192, 416, 144.',)),
        # ---- rows 20 and 21: Check 13
        CourseCheck(
            notes=('Both answers come from the timeframe slides.',),
            origin='Questions are ours, answerable from the timeframe slides before; Lim (2016), p. 253.',
            label='Timeframes',
            questions=(
                Q(3, 'On a 5 minute chart, what is the multiplying factor for a 1 hour indicator?', '12', ('3', '5', '60'),
                  'MF is the indicator timeframe over the chart timeframe: 60 / 5 = 12 (p. 253).'),
                Q(4, 'A 14 period RSI from the 15 minute timeframe is shown on a 5 minute chart. How many periods does it have there?', '42', ('14', '15', '168'),
                  'MF = 15 / 5 = 3, so 14 x 3 = 42 periods (p. 253). 168 is the hourly RSI.'),
            ),
        ),
        # ---- rows 22 and 23: lagging
        Content(
            notes=('Oscillators lag; divergence is the exception.', 'Gold 1 the price peak, red 2 the later peak of the line.'),
            origin='Lim (2016), p. 253. ' + OUR,
            title='Oscillators usually lag price',
            lines=("Lim says oscillators usually lag price action because they are derived from price (p. 253). Our line is the average of the last four closes. Price peaks at 62.00 [1] and the line peaks two bars later, at 60.50 [2]. Divergence is the exception: Lim calls it a leading signal, one that comes before price turns (p. 253); the next slide lists what leads.",),
        ),
        chart('lag', 'BG', 'Oscillators usually lag price',
              'Our price peaking at 62.00 and a line derived from it, the average of four closes, peaking two bars later at 60.50.',
              ('Gold 1 the price peak at 62.00, red 2 the peak of the derived line two bars later.',)),
        # ---- row 24: what leads and what lags
        Content(
            notes=('Lim lists what leads; he does not define leading or lagging.',),
            origin='Lim (2016), p. 253. The table is ours, from his list.',
            title='What leads and what lags',
            lines=("Lim lists divergence, early momentum reversals, horizontally and geometrically based overlays and Fibonacci levels as leading, and says moving averages are not (p. 253). He does not define leading and lagging. We use them as his examples do: leading means a signal before price turns, lagging means one after.",),
        ),
        chart('ldt', 'BH', 'What leads and what lags',
              'A table of what Lim lists as leading price, divergence, early momentum reversals, horizontal and geometric overlays and Fibonacci levels, and as not leading, moving averages.',
              ('Moving averages are the one named as not leading.',)),
        # ---- rows 25 and 26: Check 14
        CourseCheck(
            notes=('Both answers come from the lagging slides.',),
            origin='Questions are ours, answerable from the lagging slides before; Lim (2016), p. 253.',
            label='Leading and lagging',
            questions=(
                Q(5, 'Which of these does Lim list as leading?', 'Divergence', ('A moving average', 'The 14 period RSI', 'A signal line crossover'),
                  'Divergence is a leading signal; moving averages are not (p. 253).'),
                Q(6, 'Why does an oscillator usually lag price?', 'It is derived from price action', ('It uses volume only', 'It is always unbounded', 'It sits in its own window'),
                  'Lim says oscillators usually lag price action because they are derived from it (p. 253).'),
            ),
        ),
    )


def slides_84():
    return (
        # ---- rows 27 and 28: an oscillator fed an oscillator
        Content(
            notes=('The StochRSI replaces price with RSI.',),
            origin='Lim (2016), pp. 253 and 254.',
            title='An oscillator can be fed another oscillator',
            lines=("So far our oscillators were calculated from price. Lim says an oscillator can use other data, even another oscillator's readings (p. 253). His example is the StochRSI. It starts from the stochastic fraction (C - Ln) / (Hn - Ln): C is the latest value, Ln the lowest and Hn the highest of the last n periods, and Lim calls the fraction the raw %K. The StochRSI puts RSI values where the prices were; the next slides give it as Lim prints it (p. 254).",),
            accent='Same fraction, but fed RSI readings instead of prices.',
        ),
        Content(
            notes=('Gold 1 the RSI peak, red 2 the fraction at its top, blue 3 at its bottom.',),
            origin='Lim (2016), p. 253. ' + OUR,
            title='The fraction on RSI readings',
            lines=("Here the top window is an RSI of ours [1]. Under it is the fraction on those readings with n = 5: it is 1 whenever the latest RSI is the highest of the last five [2] and 0 whenever it is the lowest of the last five [3].",),
        ),
        chart('srf', 'BI', 'The fraction on RSI readings',
              'Our RSI readings and under them the stochastic fraction worked on those readings with five readings in the window, reaching 1 at the RSI peak and 0 at its low.',
              ('Gold 1 the RSI peak at 72, red 2 the fraction at 1.00, blue 3 the fraction at 0.00.',)),
        # ---- row 29: the formula as printed, and the fraction worked
        Content(
            notes=('Five RSI readings, n = 5.', 'The book gives no length for the average, so we stop at the fraction.'),
            origin='Lim (2016), p. 254. ' + OUR,
            title='The StochRSI as printed, and its fraction worked',
            lines=("As printed, the StochRSI is a moving average of (RSI now - lowest RSI of n) / (highest RSI of n - lowest RSI) (p. 254). Lim gives a default lookback of 14 bars, but not the length of the average, and no x 100, as his charts run 0 to 1. Five RSI readings of ours, 40, 55, 70, 60 and 50: highest 70 [1], lowest 40 [2]; the latest, 50 [3], gives 0.33.",),
        ),
        chart('srw', 'BJ', 'The StochRSI as printed, and its fraction worked',
              'Our five RSI readings 40, 55, 70, 60 and 50 with lines at the highest, 70, and the lowest, 40.',
              ('Gold 1 the highest reading 70, red 2 the lowest 40, blue 3 the latest 50.',)),
        # ---- row 30: Figure 8.17 and its three panels
        top("Figure 8.17: the StochRSI, the stochastic and the RSI together",
                  ("Lim's Figure 8.17 draws three oscillators under the Dow Jones, from the top: the StochRSI [1], the stochastic [2], which his chart labels Slow STO (slow and fast come in 8.6), and the RSI [3]. His text lists them in another order, stochastic, StochRSI, RSI (p. 254); we read the figure. The StochRSI runs 0 to 1, the other two 0 to 100."),
                  F817_ALL, ('Gold 1 the StochRSI, red 2 the slow stochastic, blue 3 the RSI.',), 'Lim (2016), p. 254, Figure 8.17. The marks are ours, added for teaching.'),
        # ---- row 31: the StochRSI is more responsive
        top('Figure 8.17: the StochRSI is more responsive',
                  ("Lim says the StochRSI is faster and more responsive than the RSI (p. 254). Watch October first. The StochRSI [1] swings from the top of its window to the bottom and back, while the RSI under it [2] over the same weeks hardly moves. November shows it again: the StochRSI [3] against the RSI [4]."),
                  F817_RESP, ('Gold 1 and blue 3 the StochRSI swings, red 2 and purple 4 the RSI over the same weeks.',), 'Lim (2016), p. 254, Figure 8.17. The marks are ours, added for teaching.'),
        # ---- rows 32 and 33: the data drop-off
        Content(
            notes=('An average that drops an old value and adds a new one can jump.', 'Gold 1 the dropped $7, red 2 the added $4, blue 3 and purple 4 the two averages.'),
            origin='Lim (2016), p. 254. ' + OUR,
            title='The data drop-off effect',
            lines=("An average of the last n values drops the oldest and adds a new one each period, so it jumps when the dropped value is large (p. 254). Lim's seven prices, $7, $4, $3, $3, $2, $4, $5, average $4.00. The $7 [1] drops out, a new $4 [2] comes in: $25 / 7 = $3.57. Our chart: $4.00 [3] becomes $3.57 [4].",),
        ),
        chart('dr1', 'BK', 'The data drop-off effect',
              'Seven prices of $7, $4, $3, $3, $2, $4 and $5 and a new $4, with their averages of $4.00 and $3.57.',
              ('Gold 1 the $7 that drops out, red 2 the new $4, blue 3 the first average, purple 4 the next.',)),
        # ---- row 34: a big old value
        Content(
            notes=('A bigger old value, a bigger jump.', 'The book prints $3.75 for $3.57 once; say so.'),
            origin='Lim (2016), pp. 254 and 255. ' + OUR,
            title='A big old value makes a big jump',
            lines=("Replace the $7 by $9: the first average is $30 / 7 = $4.29 [3]. The $9 [1] drops out, the $4 [2] comes in, and the average is $3.57 again [4], a fall of (30/7 - 25/7) / (30/7) = 16.7 percent, against ($4.00 - $3.57) / $4.00 = 10.75 percent for the $7 (pp. 254 to 255). Lim prints 16.72, and once $3.75 for $3.57.",),
        ),
        chart('dr2', 'BL', 'A big old value makes a big jump',
              'Seven prices of $9, $4, $3, $3, $2, $4 and $5 and a new $4, with averages of $4.29 and $3.57.',
              ('Gold 1 the $9 that drops out, red 2 the new $4, blue 3 the first average, purple 4 the next.',)),
        # ---- row 35: softening the jump
        Content(
            notes=('Longer lookback or front weighted averages.', 'The weighting formula is not in the book.'),
            origin='Lim (2016), p. 255. ' + OUR,
            title='Ways to soften the jump',
            lines=("Lim names two remedies (p. 255). A longer lookback: the same $9 [1] leaving a window of 14 prices as a new $4 [2] arrives moves the average from $4.07 [3] to $3.71 [4], 8.8 percent, not 16.7. And a more front weighted average, exponential or linear, giving recent prices more weight; no formula is given.",),
        ),
        chart('dr3', 'BM', 'Ways to soften the jump',
              'Fourteen prices starting with a $9 and a new $4, with averages of $4.07 and $3.71.',
              ('Gold 1 the $9, red 2 the new $4, blue 3 the first average, purple 4 the next.',)),
        # ---- rows 36 and 37: Check 15
        CourseCheck(
            notes=('Both answers come from the drop-off slides.',),
            origin='Questions are ours, answerable from the drop-off slides before; Lim (2016), pp. 254 to 255.',
            label='The data drop-off effect',
            questions=(
                Q(7, "In Lim's seven price example the first average is $4.00. The $7 drops out and a $4 comes in. What is the new average?", '$3.57', ('$3.50', '$4.29', '$3.00'),
                  '($28 - $7 + $4) / 7 = $25 / 7 = $3.57 (p. 254). The $3.75 the book prints once is a typing slip.'),
                Q(8, 'Which change makes the data drop-off jump smaller?', 'A longer lookback', ('A shorter lookback', 'A larger old value dropping out', 'Plotting a different timeframe'),
                  'With more prices in the window, one dropped value moves the average less; Lim also names front weighted averages (p. 255).'),
            ),
        ),
    )


def slides_85():
    return (
        # ---- rows 38 to 40: buy signals in an uptrend
        Content(
            notes=('Trade with the larger trend.', 'Gold 1 the uptrend, red 2 the dip to oversold, blue 3 the signal line, purple 4 the 50 crossing.'),
            origin='Lim (2016), p. 255; Chapter 6, "Why the larger trend matters, with numbers". ' + OUR,
            title='Trade with the larger trend',
            lines=("Lim says to time continuations and breakouts in the direction of the existing trend: it is always best to trade with the larger trend (p. 255), as Chapter 6 showed. Here price is in an uptrend of higher lows [1]; a pullback pushes the oscillator to oversold [2], and its rise across its signal line [3] and then across 50 [4] gives the buy signal.",),
        ),
        chart('tru', 'BN', 'Trade with the larger trend',
              'Our price in an uptrend of higher lows with a pullback, and under it an oscillator and its signal line, dipping below 30 and rising back across the signal line and across 50.',
              ('Gold 1 the uptrend line, red 2 the oversold dip, blue 3 the signal line crossing, purple 4 the crossing of 50.',)),
        Content(
            notes=('Lim\'s five buy signals.',),
            origin='Lim (2016), p. 255.',
            title='In an uptrend there are five buy signals',
            lines=("In an existing uptrend Lim lists five buy signals (p. 255): the oscillator crossing above its equilibrium; crossing above its signal line; reaching oversold or rising back above it; a bullish divergence, standard or reverse; and the oscillator breaking a chart pattern or trendline drawn on it, upward.",),
            accent='Divergence and the pattern break are drawn later in this class; the first three are on the next chart.',
        ),
        Content(
            notes=('Three of the five on one chart.',),
            origin='Lim (2016), p. 255. ' + OUR,
            title='Three of the five on one chart',
            lines=("Here the uptrend [1] pulls back and the oscillator reaches oversold [2]. Its rise crosses 30 and its signal line in one bar [3] and then crosses 50 [4], so three of the five buy signals show on this chart.",),
        ),
        chart('tru', 'BN', 'Three of the five on one chart',
              'The same uptrend with the oversold dip, the signal line crossing and the crossing of 50 marked.',
              ('Gold 1 the uptrend, red 2 the dip, blue 3 the signal line crossing, purple 4 the crossing of 50.',)),
        # ---- rows 41 and 42: sell signals in a downtrend
        Content(
            notes=('The mirror: five sell signals in a downtrend.',),
            origin='Lim (2016), p. 255.',
            title='In a downtrend there are five sell signals',
            lines=("In an existing downtrend Lim lists the mirror five sell signals (p. 255): the oscillator crossing below its equilibrium; crossing below its signal line; reaching overbought or falling back below it; a bearish divergence, standard or reverse; and the oscillator breaking a pattern or trendline drawn on it, downward.",),
        ),
        Content(
            notes=('Gold 1 the downtrend line, red 2 the overbought bounce, blue 3 the signal line crossing, purple 4 the crossing of 50.',),
            origin='Lim (2016), p. 255. ' + OUR,
            title='Three of the five sell signals on one chart',
            lines=("Here price is in a downtrend of lower highs [1] and a bounce lifts the oscillator to overbought [2]. Its fall crosses 70 and its signal line in one bar [3] and then crosses 50 [4], so three of the five sell signals show on this chart.",),
        ),
        chart('trd', 'BO', 'Three of the five sell signals on one chart',
              'Our price in a downtrend of lower highs with a bounce, and under it an oscillator and its signal line, rising above 70 and falling back across the signal line and across 50.',
              ('Gold 1 the downtrend line, red 2 the overbought bounce, blue 3 the signal line crossing, purple 4 the crossing of 50.',)),
        # ---- rows 43 and 44: Check 16
        CourseCheck(
            notes=('Both answers come from the trend trading slides.',),
            origin='Questions are ours, answerable from the trend trading slides before; Lim (2016), p. 255.',
            label='Trend trading',
            questions=(
                Q(9, 'In an existing uptrend, which of these is one of Lim\'s buy signals?', 'The oscillator rising back above oversold',
                  ('The oscillator falling below its signal line', 'The oscillator reaching overbought', 'A bearish divergence'),
                  'Reaching oversold or rising back above it is one of the five buy signals in an uptrend (p. 255). The other three are the mirror signals Lim gives for a downtrend; in an uptrend they are not buy signals.'),
                Q(10, "Lim's rule for using an oscillator in a trend is to", 'trade in the direction of the larger existing trend', ('trade only against the trend', 'ignore the larger trend', 'trade only at overbought'),
                  'It is always best to trade in the direction of the larger existing trend (p. 255).'),
            ),
        ),
    )
