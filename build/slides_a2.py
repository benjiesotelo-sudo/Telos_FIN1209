"""first class slides, section 8.2 (outline rows 57 to 124), written by hand in teaching order.

Marks on Lim's figures are fractions of the whole master figure, read off a 0.05 grid; each box
starts clear of the printed labels. Our numbers never go on a Lim figure.
"""
from deckkit import Content, Mark, Question
from chartlayout_chapter08 import CourseCheck, StackedFigureCheck, WidePair, book_crop, course_chart

OUR = 'The numbers are invented for teaching.'
G, R, B, P = 'gold', 'red', 'blue', 'purple'


def M(n, color, x0, y0, x1, y1, at=None, kind='box'):
    return Mark(number=n, kind=kind, x0=x0, y0=y0, x1=x1, y1=y1, color=color, at=at, size=0.28)


def fig(num, window, shows, marks, page, extra=''):
    f = book_crop(num, window, shows, marks=tuple(marks))
    f.origin = f'Lim (2016), p. {page}, Figure {num}, courtesy of Stockcharts.com. The marks are ours, added for teaching.' if extra == 'sc' else f'Lim (2016), p. {page}, Figure {num}. The marks are ours, added for teaching.'
    return f


def chart(asset, letter, title, shows, notes):
    origin = {'AW': "FIN1209 table, from Lim's four definitions (pp. 246 to 247).",
              'AX': "FIN1209 table: examples from the slides of this class, our charts and Lim's figures."}.get(letter, f'FIN1209 teaching chart {letter}. ' + OUR)
    return course_chart(asset, notes=notes, origin=origin, title=title, letter=letter, shows=shows, tier='core', marks=())


def pair(title, lines, picture, notes, origin, accent='', w=4.4):
    return WidePair(notes=notes, origin=origin, left=Content(title=title, lines=lines, accent=accent), picture=picture, text_w=w)


# ---------------------------------------------------------------- Lim's figures
F84_A = fig('8.4', (0, 0, 1, 1), 'Figure 8.4: a price chart with an oscillator under it, and Lim\'s arrows and labels for a crossover, an overbought reading, an oversold reading, a divergence and a chart pattern.',
            [M(1, G, 0.266, 0.672, 0.376, 0.718, at=(0.40, 0.69)), M(2, R, 0.166, 0.93, 0.256, 0.972, at=(0.145, 0.95))], 242)
F84_B = fig('8.4', (0, 0, 1, 1), 'Figure 8.4 again, with all five labels marked: crossover, overbought, oversold, divergence and chart pattern.',
            [M(1, G, 0.266, 0.672, 0.376, 0.718, at=(0.40, 0.69)), M(2, R, 0.166, 0.93, 0.256, 0.972, at=(0.145, 0.95)),
             M(3, B, 0.044, 0.67, 0.146, 0.716, at=(0.02, 0.62)), M(4, P, 0.46, 0.53, 0.568, 0.582, at=(0.435, 0.50)),
             M(5, G, 0.748, 0.67, 0.876, 0.716, at=(0.73, 0.62))], 242)
F85 = fig('8.5', (0, 0, 1, 1), 'Figure 8.5: Amazon.com with its MACD under it, a dotted overbought level in the MACD window and six dashed time lines numbered 1 to 6 by Lim.',
          [M(1, G, 0.03, 0.785, 0.955, 0.818, at=(0.985, 0.80)), M(2, R, 0.02, 0.105, 0.89, 0.205, at=(0.92, 0.155))], 243, 'sc')
F86 = fig('8.6', (0, 0, 1, 1), 'Figure 8.6: silver with a cycle-tuned stochastic under it, its oversold levels, and six up arrows at the bottoms.',
          [M(1, G, 0.195, 0.83, 0.315, 0.915, at=(0.17, 0.87)),
           M(2, R, 0.141, 0.451, 0.181, 0.521, kind='circle', at=(0.115, 0.486)), M(3, B, 0.351, 0.394, 0.391, 0.464, kind='circle', at=(0.325, 0.43)),
           M(4, P, 0.474, 0.295, 0.514, 0.365, kind='circle', at=(0.448, 0.33)), M(5, G, 0.527, 0.295, 0.567, 0.365, kind='circle', at=(0.595, 0.33)),
           M(6, R, 0.623, 0.40, 0.663, 0.47, kind='circle', at=(0.597, 0.435)), M(7, B, 0.73, 0.394, 0.77, 0.464, kind='circle', at=(0.80, 0.43))], 243)
F88 = fig('8.8', (0, 0, 1, 1), 'Figure 8.8: Apple with the RSI, MACD and ROC under it and Lim\'s labels for similar crossover points and similar divergences.',
          [M(1, G, 0.11, 0.07, 0.31, 0.23, at=(0.32, 0.06)), M(2, R, 0.60, 0.30, 0.86, 0.355, at=(0.89, 0.33))], 245, 'sc')
F88 = fig('8.8', (0, 0, 1, 1), 'Figure 8.8: Apple with the RSI, MACD and ROC under it. Lim labels similar crossover points on the price chart and similar divergences by arrows.',
          [M(1, G, 0.155, 0.07, 0.345, 0.222, at=(0.37, 0.05)), M(2, R, 0.713, 0.312, 0.878, 0.388, at=(0.90, 0.35)),
           M(3, B, 0.02, 0.515, 0.93, 0.642, at=(0.955, 0.58)), M(4, P, 0.02, 0.655, 0.93, 0.80, at=(0.955, 0.73)),
           M(5, R, 0.02, 0.81, 0.93, 0.985, at=(0.955, 0.90))], 245, 'sc')
F89 = fig('8.9', (0, 0.25, 1, 1), 'Figure 8.9: Goldman Sachs with its MACD and signal line under it, vertical time lines, and Lim\'s label for the signal line crossovers.',
          [M(1, G, 0.425, 0.485, 0.585, 0.592, at=(0.405, 0.44)), M(2, R, 0.275, 0.795, 0.315, 0.857, kind='circle', at=(0.25, 0.77)),
           M(3, B, 0.415, 0.72, 0.455, 0.784, kind='circle', at=(0.39, 0.69))], 246, 'sc')
F810_L = fig('8.10', (0, 0, 0.55, 1), 'Figure 8.10, left half: the GBPUSD chart with its MACD and Lim\'s labelled divergence lines: standard bullish, standard bearish and reverse bullish.',
             [M(1, G, 0.012, 0.535, 0.1, 0.628, at=(0.115, 0.50)), M(2, R, 0.14, 0.222, 0.23, 0.328, at=(0.245, 0.19)),
              M(3, B, 0.35, 0.438, 0.446, 0.548, at=(0.335, 0.41))], 247)
F810_R = fig('8.10', (0.45, 0, 1, 1), 'Figure 8.10, right half: Lim\'s labelled divergence lines: standard bearish, reverse bearish, standard bullish and reverse bullish.',
             [M(1, G, 0.47, 0.37, 0.556, 0.47, at=(0.49, 0.34)), M(2, R, 0.57, 0.405, 0.658, 0.505, at=(0.60, 0.375)),
              M(3, B, 0.68, 0.46, 0.766, 0.562, at=(0.71, 0.60)), M(4, P, 0.78, 0.45, 0.868, 0.558, at=(0.82, 0.42)), M(5, G, 0.882, 0.448, 0.968, 0.548, at=(0.955, 0.415))], 247)
F811_U = fig('8.11', (0, 0, 1, 0.76), 'Figure 8.11, upper part: the S&P 500 and the whole S&P Bullish Percent Index window, with time lines 1 to 4 and Lim\'s labels for the reverse bullish, standard bearish and standard bullish divergences.',
             [M(1, G, 0.1, 0.23, 0.22, 0.325, at=(0.245, 0.21)), M(2, R, 0.328, 0.065, 0.635, 0.108, at=(0.66, 0.085)),
              M(3, B, 0.332, 0.462, 0.634, 0.502, at=(0.66, 0.482)), M(4, P, 0.692, 0.315, 0.81, 0.405, at=(0.835, 0.36))], 248, 'sc')
F811_L = fig('8.11', (0, 0.5, 1, 1), 'Figure 8.11, lower part: the Bullish Percent Index window and the MACD window with Lim\'s divergence arrows.',
             [M(1, G, 0.005, 0.515, 0.93, 0.665, at=(0.96, 0.59)), M(2, R, 0.005, 0.70, 0.93, 0.985, at=(0.96, 0.84))], 248, 'sc')
F812_L = fig('8.12', (0, 0.4, 0.55, 1), 'Figure 8.12, left half: the 30-minute Nikkei 225 with its momentum oscillator under it, a symmetrical triangle breakout and the sell signal under it.',
             [M(1, G, 0.172, 0.66, 0.438, 0.706, at=(0.15, 0.63)), M(2, R, 0.298, 0.86, 0.392, 0.91, at=(0.27, 0.885))], 249)
F812_R = fig('8.12', (0.5, 0.4, 1, 1), 'Figure 8.12, right half: the oscillator channel, the trendlines, a second sell signal and the buy signal.',
             [M(1, G, 0.578, 0.655, 0.743, 0.706, at=(0.56, 0.62)), M(2, R, 0.848, 0.805, 0.953, 0.857, at=(0.975, 0.83)),
              M(3, B, 0.873, 0.868, 0.968, 0.912, at=(0.985, 0.90)), M(4, P, 0.748, 0.855, 0.805, 0.915, at=(0.725, 0.885))], 249)
F812_C = fig('8.12', (0.5, 0.55, 1, 1), 'Figure 8.12, cropped to its oscillator channel on the right and the buy signal at its bottom edge.',
             [M(1, G, 0.578, 0.925, 0.87, 0.975, at=(0.56, 0.90)), M(2, R, 0.873, 0.868, 0.968, 0.912, at=(0.985, 0.85))], 249)
F813 = fig('8.13', (0, 0, 1, 1), 'Figure 8.13: Starbucks with its RSI and Bollinger bands drawn on the RSI, Lim\'s overbought and oversold levels, and four arrows labelled RSI at Bollinger lower band.',
           [M(1, G, 0.40, 0.755, 0.96, 0.815, at=(0.985, 0.785)),
            M(2, R, 0.50, 0.78, 0.54, 0.835, kind='circle', at=(0.475, 0.86)), M(3, B, 0.56, 0.78, 0.60, 0.835, kind='circle', at=(0.57, 0.86)),
            M(4, P, 0.675, 0.78, 0.715, 0.835, kind='circle', at=(0.66, 0.86)), M(5, G, 0.81, 0.775, 0.85, 0.83, kind='circle', at=(0.87, 0.86))], 250, 'sc')
F813_C = fig('8.13', (0.0, 0.62, 1, 1), 'Figure 8.13, cropped to the RSI window: the lower Bollinger band, the RSI and Lim\'s oversold level label.',
             [M(1, G, 0.40, 0.755, 0.96, 0.815, at=(0.985, 0.785)), M(2, R, 0.36, 0.845, 0.62, 0.863, at=(0.64, 0.855))], 250, 'sc')
F814 = fig('8.14', (0, 0.45, 0.66, 1), 'Figure 8.14, left part: the 30-minute Nikkei 225 with its oscillator under it, Lim\'s oscillator resistance line and his label for sell signals at resistance.',
           [M(1, G, 0.155, 0.683, 0.555, 0.747, at=(0.135, 0.66)), M(2, R, 0.475, 0.575, 0.642, 0.64, at=(0.45, 0.55))], 251)
F814_R = fig('8.14', (0.45, 0.45, 1, 1), 'Figure 8.14, right part: the sell signals at the oscillator resistance and the buy signals at the oscillator support.',
             [M(1, G, 0.475, 0.575, 0.642, 0.64, at=(0.46, 0.55)), M(2, R, 0.608, 0.686, 0.762, 0.752, at=(0.785, 0.72)),
              M(3, B, 0.455, 0.9, 0.752, 0.982, at=(0.775, 0.95))], 251)
F815 = fig('8.15', (0, 0, 1, 1), 'Figure 8.15: Apple with the StochRSI under it, Lim\'s label Bullish oversold signals and five dotted arrows.',
           [M(1, G, 0.112, 0.115, 0.325, 0.215, at=(0.345, 0.09)),
            M(2, R, 0.085, 0.265, 0.125, 0.325, kind='circle', at=(0.062, 0.30)), M(3, B, 0.185, 0.27, 0.225, 0.33, kind='circle', at=(0.16, 0.305)),
            M(4, P, 0.38, 0.30, 0.42, 0.36, kind='circle', at=(0.355, 0.335)), M(5, G, 0.515, 0.24, 0.555, 0.30, kind='circle', at=(0.49, 0.275)),
            M(6, R, 0.665, 0.10, 0.705, 0.16, kind='circle', at=(0.64, 0.135)),
            M(7, B, 0.04, 0.885, 0.745, 0.945, at=(0.775, 0.915))], 251, 'sc')
F87_CCI = fig('8.7', (0, 0.5, 1, 1), 'Figure 8.7, lower half: the RSI and the CCI with Lim\'s label for the 50 percent and zero line crossovers.',
              [M(1, G, 0.178, 0.885, 0.212, 0.94, kind='circle', at=(0.14, 0.93)), M(2, R, 0.51, 0.875, 0.545, 0.93, kind='circle', at=(0.575, 0.84)),
               M(3, B, 0.178, 0.635, 0.212, 0.69, kind='circle', at=(0.14, 0.62)), M(4, P, 0.51, 0.64, 0.545, 0.695, kind='circle', at=(0.575, 0.60))], 244, 'sc')
F84_PLAIN = fig('8.4', (0, 0, 1, 1), 'Figure 8.4: a price chart with an oscillator under it, and Lim\'s arrows and labels for a crossover, an overbought reading, an oversold reading, a divergence and a chart pattern.', [], 242)


def slides(S, equilibrium, signal, check6):
    return (
        # ---- row 57
        pair('Eight ways to read an oscillator',
             ("We now know the kinds of indicator; next is how to read an oscillator. Lim lists eight ways to read a window oscillator for potential buy and sell signals (p. 240): overbought and oversold; equilibrium crossovers; signal line crossovers; divergence; geometric, numerical and horizontal pattern analysis; and oscillator on oscillator. Chapter 6 listed all eight and used three of them; now each one is taught.",
              "Lim's Figure 8.4 shows several of the eight on one chart; we mark it as each is taught."),
             F84_PLAIN, ('Chapter 6 listed eight and used three.',), 'Lim (2016), pp. 240 and 242, Figure 8.4. Chapter 6, "Eight ways to read an oscillator; three used here".', w=5.6),
        # ---- rows 58 to 60
        Content(
            notes=('The signal comes from the oscillator, the trigger from price.',),
            origin='Lim (2016), pp. 241 and 256; Chapter 5, "A filter and a trigger together". The chart on the next slide is ours.',
            title='An oscillator gives a signal; price gives the trigger',
            lines=("Many practitioners require price confirmation: price must breach an overlay. An oscillator breaching an overlay is only a signal of potential bullishness or bearishness (p. 241).",
                   "The next sentences are Lim's own: the trigger for entry or exit \"must always be based on price action\" (p. 241), and oscillators \"only generate trade signals, not trade triggers\" (p. 256). Chapter 5 called a stochastic crossing a trigger; for Lim the trigger is price."),
        ),
        Content(
            notes=('Signal first, trigger later.',),
            origin='Lim (2016), pp. 241 and 256. ' + OUR,
            title='Here is a signal that comes before its trigger',
            lines=("On our chart the oscillator crosses 50 [1], a signal, while price is still under its resistance. The trigger comes later, when price breaches the resistance [2].",),
        ),
        chart('trig', 'AC', 'Here is a signal that comes before its trigger',
              'Our price under a resistance of 50.00 and an oscillator under it that crosses 50 first; price breaches the resistance two bars later.',
              ('Gold 1 the oscillator crossing 50, the signal. Red 2 price breaching 50.00, the trigger.',)),
        Content(
            notes=('Which overlays count as price confirmation.',),
            origin='Lim (2016), p. 241. The chart on the next slide is ours.',
            title='Which overlays count as price confirmation',
            lines=("For a valid price confirmation, price may breach a numerically, horizontally or geometrically based overlay (p. 241). The most reliable and popular are prior support and resistance levels, simple trendlines, moving averages and chart pattern breakouts or reactions (p. 241). The book does not say why it leaves the algorithmic overlays out.",),
        ),
        Content(
            notes=('Price breaches an overlay; here are three.',),
            origin='Lim (2016), p. 241. ' + OUR,
            title='Here is price breaching three of those overlays',
            lines=("On our charts price breaches a prior resistance [1], a trendline through two troughs [2] and a 3-bar moving average [3]. Each is a price confirmation, because price, not the oscillator, does the breaching (p. 241).",),
        ),
        chart('pc', 'AU', 'Here is price breaching three of those overlays',
              'Three small charts of ours: price breaching a prior resistance, a rising trendline and a moving average.',
              ('Gold 1 the resistance breach, red 2 the trendline breach, blue 3 the moving average breach.',)),
        Content(
            notes=('Overbought and oversold: how far is too far.',),
            origin='Lim (2016), pp. 237 and 241; Chapters 5, 6 and 7. The chart on the next slide is ours.',
            title='Overbought and oversold: how far is too far',
            lines=("Overbought and oversold (OBOS) levels on an oscillator are indicative of overextensions in price, where a potential reversal in price is expected (p. 241). Overbought is first and foremost a strong uptrend with a high probability of a bearish reversal; oversold is the mirror, and price confirmation is required (p. 241).",
                   "A bounded oscillator can also stay overbought for long in a strong trend (p. 237); price confirmation is what decides. Chapters 5 to 7 used overextended for price past a barrier, for volume and for a long bar; here the overextension is still in price, and the oscillator's overbought or oversold zone is how we see it."),
        ),
        Content(
            notes=('Ten readings above 80 while price keeps rising.',),
            origin='Lim (2016), pp. 237 and 241. ' + OUR,
            title='Here is an oscillator that stays overbought',
            lines=("On our chart the oscillator sits above 80 for ten readings [1] while price keeps rising [2], so the reading alone is not a turn.",),
        ),
        chart('stuck', 'R', 'Here is an oscillator that stays overbought',
              'Our steadily rising price with a bounded oscillator staying above 80 for ten readings.',
              ('Gold 1 the ten readings above 80, red 2 price still rising.',)),
        # ---- rows 61 to 64
        Content(
            notes=('Levels for a bounded oscillator.',),
            origin='Lim (2016), p. 241. ' + OUR,
            title='Levels for a bounded oscillator',
            lines=("For a bounded oscillator Lim gives overbought as relatively high readings, usually at or above 70 or 80 percent, and oversold as relatively low readings, usually at or below 20 or 30 percent, depending on the oscillator (p. 241). On our chart the readings are 82 [1], 71 [2], 48, 27 [3] and 19 [4]. 82 [1] is overbought on either level and 19 [4] oversold on either; 71 [2] counts only against 70 and 27 [3] only against 30; 48 is neither.",),
        ),
        chart('lev', 'AD', 'Levels for a bounded oscillator',
              'Our five readings 82, 71, 48, 27 and 19 with lines at 80, 70, 30 and 20.',
              ('Gold 1 the 82, red 2 the 71, blue 3 the 27, purple 4 the 19.',)),
        Content(
            notes=('Unbounded: levels come from history.',),
            origin='Lim (2016), pp. 241 to 242. The chart on the next slide is ours.',
            title='Levels for an unbounded oscillator come from its history',
            lines=("An unbounded oscillator has no fixed percentage. Lim reads overbought as historical or significant peaks and oversold as historical or significant troughs (p. 241). These levels are best found by looking at the chart (p. 242). He gives no number of periods for historical.",),
        ),
        Content(
            notes=('Three peaks at about the same height give a historical level.',),
            origin='Lim (2016), pp. 241 to 242. ' + OUR,
            title='Here is a historical level on one oscillator of ours',
            lines=("Our unbounded oscillator turned down at 3.9 [1], 3.8 [2] and 4.0 [3]. Peaks at about the same height give a historical overbought level, near 3.9.",),
        ),
        chart('unb', 'S', 'Here is a historical level on one oscillator of ours',
              'Our unbounded oscillator with three peaks at 3.9, 3.8 and 4.0 and a historical level drawn at 3.9.',
              ('Gold 1, red 2 and blue 3 the three peaks near 3.9.',)),
        Content(
            notes=('The 90 and 30 shift.',),
            origin='Lim (2016), p. 241. The chart on the next slide is ours.',
            title='Two defaults to know',
            lines=("The stochastic's default levels are overbought at 80 percent and oversold at 20; the RSI's are 70 and 30 (p. 241). Many practitioners shift the stochastic's levels up by ten points, to 90 and 30, to account for the upside bias in certain markets or during strong and prolonged uptrends (p. 241). On our chart the stochastic reaches the shifted 90 [1] and dips under both 30 and 20 [2]; our RSI reaches its 70 [3].",),
        ),
        chart('def', 'AE', 'Here are the default levels and the shifted ones',
              'Our stochastic with its default lines at 80 and 20 and its shifted lines at 90 and 30, and our RSI with lines at 70 and 30.',
              ('Gold 1 the stochastic over 90, red 2 under 30, blue 3 the RSI over 70.',)),
        # ---- rows 65 and 66
        Content(
            notes=('CCI and standard deviation levels.',),
            origin='Lim (2016), p. 242; Chapter 5, standard deviation. The chart on the next slide is ours.',
            title='CCI and standard deviation oscillator levels',
            lines=("For the CCI Lim gives overbought at plus 100 and oversold at minus 100, and says these are measures of volatility; they coincide well with the Bollinger band's 1 standard deviation values, and plus and minus 200 match its 2 standard deviation bands (p. 242). The standard deviation oscillator uses plus or minus 1 or 2 sigma, the book's other word for standard deviation (p. 242), which Chapter 5 met. Most unbounded oscillators have no widely accepted levels.",),
        ),
        Content(
            notes=('Readings beyond the lines.',),
            origin='Lim (2016), p. 242. ' + OUR,
            title='Here are the CCI levels on one oscillator of ours',
            lines=("The CCI's own calculation is not in this chapter. On our unbounded oscillator a reading of 210 [1] is beyond plus 200 and a reading of -240 [2] is beyond minus 200.",),
        ),
        chart('sd', 'AF', 'Here are the CCI levels on one oscillator of ours',
              'Our unbounded oscillator with lines at plus and minus 100 and plus and minus 200 and readings beyond each.',
              ('Gold 1 a reading beyond plus 200, red 2 a reading beyond minus 200.',)),
        # ---- rows 67 to 69: Figures 8.4, 8.5, 8.6
        pair('Figure 8.4 shows signals on one chart',
             ("Lim's chart marks several signals. For now only two matter: the oscillator at an overbought reading [1] and at an oversold reading [2] (p. 242). Its crossover, divergence and chart pattern labels belong to later ways; we come back to them after all eight are taught.",),
             F84_A, ('Gold 1 overbought, red 2 oversold. The other labels come later.',), 'Lim (2016), p. 242, Figure 8.4. The marks are ours, added for teaching.'),
        pair('Figure 8.5: a historically overbought MACD',
             ("The MACD is an unbounded oscillator, so its overbought level comes from its own history. On Lim's Amazon chart that level is the dotted line in the MACD window [1]; the book gives no number. Lim says every time the MACD tests or exceeds it, a reversal or correction in price followed, at his time lines 1 to 6 [2] (p. 242).",),
             F85, ('Gold 1 the dotted overbought level in the MACD window, red 2 Lim\'s numbered time lines 1 to 6.',), 'Lim (2016), pp. 242 to 243, Figure 8.5, courtesy of Stockcharts.com. The marks are ours, added for teaching.', w=4.0),
        pair('Figure 8.6: oversold on a cycle-tuned stochastic',
             ("A cycle-tuned stochastic has its lookback set to the market's cycle; the second class explains that. Lim says its oversold levels [1] coincided perfectly with bottoms in silver, shown by all six up arrows [2] to [7], and he used historical levels in place of 80 and 20 (p. 242). The figure also prints \"to confirm the RSI oversold indication\"; that is not price confirmation.",),
             F86, ('Gold 1 the oversold levels, then the six arrows.',), 'Lim (2016), pp. 242 to 243, Figure 8.6. The marks are ours, added for teaching.', w=4.4),
        # ---- rows 70 and 71: Check 5
        StackedFigureCheck(
            notes=('Both answers come from the overbought and oversold slides.',),
            origin='Questions are ours, answerable from the overbought and oversold slides before; Lim (2016), pp. 241 to 243.',
            label='Overbought and oversold',
            questions=(
                Question(stem='In Figure 8.6, what do the up arrows (marks 2 to 7) show?',
                         options=('Overbought levels at tops', 'Oversold levels coinciding with bottoms', 'Crossovers of 50', 'Price breaching resistance'), answer='B',
                         reason='Lim says oversold levels coincided with silver bottoms (p. 242).'),
                Question(stem='Where do the levels for an unbounded oscillator come from?',
                         options=('The oscillator\'s own history', 'A fixed 70 and 30', 'The stochastic\'s default', 'A fixed 80 and 20'), answer='A',
                         reason='They are its historical or significant peaks and troughs (p. 241).'),
            ),
            picture=F86, text_w=5.3,
        ),
        # ---- rows 72 and 73: equilibrium (approved samples), row 74 trigger, row 75 CCI, rows 76 and 77 check 6
    ) + tuple(equilibrium) + (
        Content(
            notes=('Signal, not trigger, again, on the equilibrium cross.',),
            origin='Lim (2016), p. 244. The chart is on slide 58 and is ours.',
            title='An oscillator signal is not a trigger',
            lines=("Lim says these crossings are signals and should not be regarded as triggers for entry (p. 244). On our chart the oscillator crosses 50 [1] before price breaks its resistance [2].",),
        ),
        chart('trig', 'AC', 'An oscillator signal is not a trigger',
              'Our price under a resistance of 50.00 and an oscillator under it that crosses 50 first; price breaches the resistance two bars later.',
              ('Gold 1 the oscillator crossing 50, red 2 price breaching the resistance.',)),
        pair('Figure 8.7 again: the CCI crosses its zero line',
             ("The CCI is unbounded, so its equilibrium is zero. In the lower half of Lim's chart the CCI crosses zero at [1] and [2], on the same vertical lines where the RSI crosses 50 [3] and [4], so the signals are nearly identical (p. 244).",),
             F87_CCI, ('Gold 1 and red 2 the CCI zero line crossings at Lim\'s arrow tips; blue 3 and purple 4 the RSI crossings of 50 above them.',), 'Lim (2016), p. 244, Figure 8.7, courtesy of Stockcharts.com. The marks are ours, added for teaching.', w=3.6),
        check6,
        # ---- rows 78 to 83: collinearity, check 7
        Content(
            notes=('Multicollinearity: two oscillators from the same prices.',),
            origin='Lim (2016), p. 245. The chart on the next slide is ours.',
            title='Two oscillators that agree may be one oscillator',
            lines=("Many oscillators give the same buy and sell signals because they are highly correlated, being built from the same price data. Lim calls this similarity multicollinearity, and says it creates a false consensus and a false sense of confidence (p. 245). Collinearity provides redundant information.",),
        ),
        Content(
            notes=('Two oscillators, one set of closes.',),
            origin='Lim (2016), p. 245. ' + OUR,
            title='Here are two oscillators from one set of prices',
            lines=("Our two oscillators come from the same eight closes, drawn above them. A crosses 50 [1] at the same reading that B does [2]; two lines, one piece of information.",),
        ),
        chart('mc', 'AG', 'Here are two oscillators from one set of prices',
              'Our eight closes drawn as a price line, and two oscillators made from them, both crossing 50 at the same reading.',
              ('Gold 1 oscillator A crossing 50, red 2 oscillator B crossing 50 at the same reading.',)),
        pair('Figure 8.8: RSI, MACD and ROC on one Apple chart',
             ("Lim's Apple chart shows the effect: the RSI, MACD and ROC give similar crossover points [1] and similar divergences [2], where price and the oscillator move apart, which Chapters 4 and 5 met and which we teach for oscillators a little later (p. 245). The windows from the top are the RSI [3], the MACD [4] and the ROC [5].",),
             F88, ('Gold 1 the similar crossover points, red 2 the similar divergences, blue 3 the RSI window, purple 4 the MACD window.',), 'Lim (2016), p. 245, Figure 8.8, courtesy of Stockcharts.com. The marks are ours, added for teaching.'),
        Content(
            notes=('How to avoid collinearity; both readings of the stochastic.',),
            origin='Lim (2016), pp. 245 and 262; Chapter 6, Chaikin Money Flow.',
            title='How to avoid collinearity',
            lines=("The cure is to use oscillators built from data other than price alone. Lim names a combination of stochastics, Chaikin's money flow index, which uses volume, and sentiment or breadth oscillators such as the McClellan Oscillator and the Put/Call ratio (p. 245). Chapter 6 taught the Chaikin Money Flow; Lim's money flow index may or may not be the same, and he does not say.",
                   "Two things Lim does not reconcile. He lists stochastics here and, in the next sentence, among the price-based oscillators novices wrongly stack together (p. 245). And on p. 262 he says many practitioners find a stochastic and RSI agreement more reliable. We give both and no ruling."),
        ),
        Content(
            notes=('Different data, different signals.',),
            origin='Lim (2016), p. 245. ' + OUR,
            title='Here are two oscillators built from different data',
            lines=("On our chart one oscillator is built from price and one from volume. They cross their equilibrium at different points [1] [2], and they are built from different data, so the signals are not one signal twice. Breadth, how many stocks are taking part, is another source Lim names.",),
        ),
        chart('pv', 'AV', 'Here are two oscillators built from different data',
              'Our price-based oscillator and our volume-based oscillator crossing 50 at different points.',
              ('Gold 1 the price-based crossing, red 2 the volume-based crossing, at different readings.',)),
        StackedFigureCheck(
            notes=('Both answers come from the collinearity slides.',),
            origin='Questions are ours, answerable from the collinearity slides before; Lim (2016), p. 245.',
            label='Collinearity',
            questions=(
                Question(stem='Why can several price-based oscillators agreeing be misleading?',
                         options=('They use volume', 'They never cross', 'They have no levels', 'They are built from the same price data'), answer='D',
                         reason='Same price data gives a false consensus (p. 245).'),
                Question(stem='In Figure 8.8, marks 1 and 2 show what?',
                         options=('Different signals', 'Pivot points', 'Similar crossovers and divergences', 'Volume spikes'), answer='C',
                         reason='Lim labels them similar crossovers and divergences (p. 245).'),
            ),
            picture=F88, text_w=5.3,
        ),
    ) + tuple(signal) + (
        # ---- rows 85 and 86: signal line extras, Figure 8.9, check 8
        Content(
            notes=('The MACD signal line is a nine-period EMA.',),
            origin='Lim (2016), p. 246. The chart on the next slide is ours.',
            title='A crossing near oversold counts for more',
            lines=("The default signal line for the MACD is usually a nine-period exponential moving average of the MACD (p. 246). Many practitioners call an upward crossover significantly more bullish near an oversold level, and a downward crossover significantly more bearish near an overbought level (p. 246).",
                   "Our chart is a bounded oscillator, not the MACD, with a three-reading average as its signal line. It crosses up near the oversold 30 [1], the stronger buy, and crosses down at about 60 [2], far from the overbought 70, so that sell counts for less."),
        ),
        chart('sig2', 'AH', 'A crossing near oversold counts for more',
              'Our oscillator and its signal line crossing near an oversold reading of 22 and again near 50.',
              ('Gold 1 the crossing near oversold, red 2 the crossing at about 60, far from the overbought 70.',)),
        pair('Figure 8.9: MACD signal line crossovers',
             ("On Lim's Goldman Sachs chart the signal line crossovers [1] are marked at the vertical time lines, with an S for a sell and a B for a buy. The MACD crosses its signal line at [2] and again at [3]. The signal line is the smoother of the two lines, since it is an average. Lim finds these fairly effective in forecasting tops and bottoms in the stock (p. 246).",),
             F89, ('Gold 1 Lim\'s label, red 2 an early crossing, blue 3 a later one.',), 'Lim (2016), p. 246, Figure 8.9, courtesy of Stockcharts.com. The marks are ours, added for teaching.'),
        StackedFigureCheck(
            notes=('Both answers come from the signal line slides.',),
            origin='Questions are ours, answerable from the signal line slides before; Lim (2016), p. 246.',
            label='Signal line crossovers',
            questions=(
                Question(stem='What is a signal line?',
                         options=('A price trendline', 'A moving average of the oscillator', 'The 50 percent level', 'A volume line'), answer='B',
                         reason='It is a moving average of the oscillator, so it lags (p. 246).'),
                Question(stem='When is an upward crossover of the signal line seen as more bullish?',
                         options=('Near an overbought level', 'Above 90', 'Only in a downtrend', 'Near an oversold level'), answer='D',
                         reason='Many treat it as more bullish near oversold (p. 246).'),
            ),
            picture=F89, text_w=5.3,
        ),
        # ---- rows 89 to 94: divergence
        Content(
            notes=('Divergence: price and the oscillator disagree.',),
            origin='Lim (2016), pp. 244 and 246 to 247; Chapter 4, 4.5; Chapter 5, characteristic 16. The charts are on the next slides and are ours.',
            title='Divergence: when price and the oscillator disagree',
            lines=("A crossover reads the oscillator against a level or against its own signal line. Divergence compares price with the oscillator (p. 246). Chapter 4 and Chapter 5 met it; Chapter 6's volume divergence is a different measure. Lim said earlier that an equilibrium signal can be misrepresented by divergence, where higher highs in price are accompanied by lower highs in the oscillator (p. 244).",
                   "Lim's list opens with divergence indicating potential reversals, yet two of its four kinds expect a continuation. Each kind gets its own slide next."),
        ),
        Content(
            notes=('Standard bullish divergence.',),
            origin='Lim (2016), p. 246. ' + OUR,
            title='Standard bullish divergence',
            lines=("Standard bullish divergence is a lower trough in price accompanied by a higher trough in the oscillator. It is a bullish setup awaiting price confirmation, and a potential upside reversal is expected (p. 246). On our chart price troughs at 44 then 41 [1] while the oscillator troughs at 22 then 30 [2].",),
        ),
        chart('d1', 'AI', 'Standard bullish divergence',
              'Our price making a lower trough, 41 after 44, while the oscillator makes a higher trough, 30 after 22.',
              ('Gold 1 the lower price trough, red 2 the higher oscillator trough.',)),
        Content(
            notes=('Standard bearish divergence.',),
            origin='Lim (2016), pp. 246 to 247. ' + OUR,
            title='Standard bearish divergence',
            lines=("Standard bearish divergence is a higher peak in price accompanied by a lower peak in the oscillator. It is a bearish setup awaiting price confirmation, and a potential downside reversal is expected (pp. 246 to 247). On our chart price peaks at 60 then 63 [1] while the oscillator peaks at 78 then 66 [2].",),
        ),
        chart('d2', 'AJ', 'Standard bearish divergence',
              'Our price making a higher peak, 63 after 60, while the oscillator makes a lower peak, 66 after 78.',
              ('Gold 1 the higher price peak, red 2 the lower oscillator peak.',)),
        Content(
            notes=('Reverse bullish divergence.',),
            origin='Lim (2016), p. 247. ' + OUR,
            title='Reverse bullish divergence',
            lines=("Reverse bullish divergence is a higher trough in price accompanied by a lower trough in the oscillator. It is a bullish setup awaiting price confirmation, and a potential upside continuation is expected (p. 247). On our chart price troughs at 44 then 46 [1] while the oscillator troughs at 30 then 22 [2].",),
        ),
        chart('d3', 'AK', 'Reverse bullish divergence',
              'Our price making a higher trough, 46 after 44, while the oscillator makes a lower trough, 22 after 30.',
              ('Gold 1 the higher price trough, red 2 the lower oscillator trough.',)),
        Content(
            notes=('Reverse bearish divergence.',),
            origin='Lim (2016), p. 247. ' + OUR,
            title='Reverse bearish divergence',
            lines=("Reverse bearish divergence is a lower peak in price accompanied by a higher peak in the oscillator. It is a bearish setup awaiting price confirmation, and a potential downside continuation is expected (p. 247). On our chart price peaks at 63 then 60 [1] while the oscillator peaks at 66 then 78 [2].",),
        ),
        chart('d4', 'AL', 'Reverse bearish divergence',
              'Our price making a lower peak, 60 after 63, while the oscillator makes a higher peak, 78 after 66.',
              ('Gold 1 the lower price peak, red 2 the higher oscillator peak.',)),
        Content(
            notes=('The four kinds in one table; Chapter 9 adds more.',),
            origin='Lim (2016), pp. 246 to 247. The table on the next slide is ours.',
            title='The four kinds in one table',
            lines=("Lim's four definitions side by side: the standard kinds expect a reversal and the reverse kinds a continuation (pp. 246 to 247). Chapter 9 adds more on divergence; these four are in Chapter 8.",),
        ),
        chart('dtb', 'AW', 'Here are the four kinds in one table',
              'A table of ours with the four kinds of divergence, what price makes, what the oscillator makes and what is expected.',
              ('Standard bullish and bearish expect a reversal; reverse bullish and bearish a continuation.',)),
        pair('Figure 8.10: the left half',
             ("Lim's GBPUSD chart prints a label on each divergence line. On the left half you can read standard bullish [1], standard bearish [2] and reverse bullish [3] divergence by their printed names (p. 247). The label at the right edge is read on the next slide.",),
             F810_L, ('Gold 1 standard bullish, red 2 standard bearish, blue 3 reverse bullish.',), 'Lim (2016), p. 247, Figure 8.10. The marks are ours, added for teaching.'),
        pair('Figure 8.10: the right half',
             ("On the right half the labels are standard bearish [1], reverse bearish [2], standard bullish [3] and reverse bullish [4]. The label at the far right is standard bearish again [5]. The kinds are interleaved across the figure, which is why we read it by halves and not by bullish and bearish (p. 247).",),
             F810_R, ('Gold 1 standard bearish, red 2 reverse bearish, blue 3 standard bullish, purple 4 reverse bullish.',), 'Lim (2016), p. 247, Figure 8.10. The marks are ours, added for teaching.'),
        pair('Figure 8.11: the S&P 500 against the Bullish Percent Index',
             ("In Lim's S&P 500 chart the arrows are labelled reverse bullish [1], standard bearish [2], standard bullish [3] and, again, reverse bullish [4] divergence. Lim's own large black numbers 1 to 4 mark his time lines; our marks are the coloured badges. The Bullish Percent Index is named in the book, not defined (p. 247).",),
             F811_U, ('Gold 1 reverse bullish, red 2 standard bearish, blue 3 standard bullish, purple 4 reverse bullish.',), 'Lim (2016), p. 247, Figure 8.11, courtesy of Stockcharts.com. The marks are ours, added for teaching.'),
        pair('Figure 8.11: the S&P 500 against the MACD',
             ("The lower part of the figure puts the Bullish Percent Index [1] and the MACD [2] under the price chart. Using oscillators based on price and on market breadth is a good way to soften the effects of multicollinearity (p. 247).",),
             F811_L, ('Gold 1 the index window, red 2 the MACD window.',), 'Lim (2016), p. 247, Figure 8.11, courtesy of Stockcharts.com. The marks are ours, added for teaching.'),
        Content(
            notes=('Divergence between two oscillators exists but is less pertinent.',),
            origin='Lim (2016), p. 247. The chart on the next slide is ours.',
            title='Divergence between two oscillators',
            lines=("On our chart oscillator A makes a higher peak [1] while oscillator B makes a lower one [2]. Divergence can be found between two oscillators, but Lim says the divergence between price and an oscillator is the more pertinent (p. 247). He sends the reader to Chapter 9 for more on divergence and for George Lane's setups (p. 247); we teach nothing more than the pointer here.",),
        ),
        chart('od', 'AT', 'Divergence between two oscillators',
              'Our two oscillators from the same prices, oscillator A making a higher peak, 76 after 66, while oscillator B makes a lower peak, 66 after 80.',
              ('Gold 1 the higher peak of oscillator A, red 2 the lower peak of oscillator B.',)),
        # ---- check 9
        StackedFigureCheck(
            notes=('Both answers come from the divergence slides.',),
            origin='Questions are ours, answerable from the divergence slides before; Lim (2016), pp. 246 to 247.',
            label='Divergence',
            questions=(
                Question(stem='Lower price trough, higher oscillator trough: what is it?',
                         options=('Reverse bullish', 'Standard bearish', 'Reverse bearish', 'Standard bullish'), answer='D',
                         reason='Lower price troughs, higher oscillator troughs: standard bullish (p. 246).'),
                Question(stem='Which kind expects an upside continuation?',
                         options=('Reverse bullish', 'Standard bearish', 'Reverse bearish', 'Standard bullish'), answer='A',
                         reason='Reverse bullish divergence expects an upside continuation (p. 247).'),
            ),
            picture=F810_L, text_w=5.3,
        ),
        # ---- rows 102 to 108: patterns on an oscillator, geometric
        Content(
            notes=('The last four ways draw on the oscillator what we draw on price.',),
            origin='Lim (2016), pp. 247 to 248. The charts on the next slides are ours.',
            title='Patterns and overlays drawn on an oscillator',
            lines=("The last four ways draw on the oscillator what we draw on price. Geometrically based overlays usually used are trendlines, channels, chart patterns and apex reactions; apex reaction is only named here (p. 248). The signals are four: breaching upward is a buy, testing from below a sell, breaching downward a sell and testing from above a buy (p. 248).",),
        ),
        Content(notes=('Breach upward.',), origin='Lim (2016), p. 248. ' + OUR, title='Breach upward is a buy signal',
                lines=("An oscillator breaching a geometrically based overlay to the upside is a buy (bullish) signal (p. 248). On our chart a falling trendline runs through the oscillator's two earlier peaks [1] [2], and the oscillator breaks up through it [3].",)),
        chart('g1', 'AM', 'Breach upward is a buy signal', 'Our oscillator breaking up through a falling trendline.', ('Gold 1 and red 2 the two earlier peaks, blue 3 the breach upward.',)),
        Content(notes=('Test from below.',), origin='Lim (2016), p. 248. ' + OUR, title='Testing from below is a sell signal',
                lines=("An oscillator testing a geometrically based overlay from below is a sell (bearish) signal (p. 248). Our falling trendline runs through the two earlier peaks [1] [2], and the oscillator rises to it and turns back [3].",)),
        chart('g2', 'AN', 'Testing from below is a sell signal', 'Our oscillator rising to a falling trendline and turning back.', ('Gold 1 and red 2 the two earlier peaks, blue 3 the test from below.',)),
        Content(notes=('Breach downward.',), origin='Lim (2016), p. 248. ' + OUR, title='Breach downward is a sell signal',
                lines=("An oscillator breaching a geometrically based overlay to the downside is a sell (bearish) signal (p. 248). Our rising trendline runs through the two earlier troughs [1] [2], and the oscillator falls through it [3].",)),
        chart('g3', 'AO', 'Breach downward is a sell signal', 'Our oscillator falling through a rising trendline.', ('Gold 1 and red 2 the two earlier troughs, blue 3 the breach downward.',)),
        Content(notes=('Test from above.',), origin='Lim (2016), p. 248. ' + OUR, title='Testing from above is a buy signal',
                lines=("An oscillator testing a geometrically based overlay from above is a buy (bullish) signal (p. 248). Our rising trendline runs through the two earlier troughs [1] [2], and the oscillator falls to it and holds [3].",)),
        chart('g4', 'AP', 'Testing from above is a buy signal', 'Our oscillator falling to a rising trendline and holding.', ('Gold 1 and red 2 the two earlier troughs, blue 3 the test from above.',)),
        pair('Figure 8.12: the triangle and the first sell signal',
             ("In Lim's 30-minute Nikkei 225 chart the momentum oscillator (MOM) carries a symmetrical triangle breakout [1], and the sell signal under it [2] (pp. 248 to 249).",),
             F812_L, ('Gold 1 the triangle, red 2 the sell signal.',), 'Lim (2016), p. 249, Figure 8.12. The marks are ours, added for teaching.', w=3.5),
        pair('Figure 8.12: the channel, the trendlines and the buy signal',
             ("On the right half the oscillator carries a channel [1], trendlines [2] and a buy signal [3]. The Sell signal label in the middle of this half [4] is Lim's second sell signal, after the one on the last slide (pp. 248 to 249).",),
             F812_R, ('Gold 1 the channel, red 2 the trendlines, blue 3 the buy signal.',), 'Lim (2016), p. 249, Figure 8.12. The marks are ours, added for teaching.', w=3.5),
        pair('Figure 8.12: the projected channel bottom',
             ("On the right, the oscillator channel is projected down to its bottom edge [1], where Lim marks a projected channel bottom buy signal [2] (p. 248).",),
             F812_C, ('Gold 1 the channel, red 2 the buy signal at its bottom edge.',), 'Lim (2016), p. 249, Figure 8.12. The marks are ours, added for teaching.'),
        # ---- rows 109 to 112: numerical
        Content(
            notes=('Numerically based overlays on an oscillator.',),
            origin='Lim (2016), p. 249. The chart on the next slide is ours.',
            title='Numerically based overlays on an oscillator',
            lines=("The numerically based overlays usually employed are Bollinger Bands, moving averages, moving average bands, Fibonacci levels and linear regression bands (p. 249). The four signals are the same: breaching upward is a buy, testing from below a sell, breaching downward a sell and testing from above a buy (p. 249).",),
        ),
        Content(notes=('An oscillator against its own moving average.',), origin='Lim (2016), p. 249. ' + OUR, title='Here is an oscillator against its own moving average',
                lines=("Our oscillator breaks up through its 3-reading moving average at 47 [1], a buy, and later falls back to touch the average from above at about 61.5 [2], also a buy (p. 249).",)),
        chart('num', 'AQ', 'Here is an oscillator against its own moving average', 'Our oscillator breaking up through its 3-reading moving average at 47 and later falling back to touch it from above at about 61.5.', ('Gold 1 the breach upward, red 2 the test from above.',)),
        pair('Figure 8.13: the RSI finds support at the lower Bollinger band',
             ("In Lim's Starbucks chart the Bollinger bands [1] are drawn on the RSI, and the RSI finds support at the lower band at the four arrows [2] to [5]. Prices also bottomed each time (p. 249). On p. 250 Lim says the RSI reacted at the upper and lower bands; his figure and his p. 249 text show only the lower band, so we read the lower one.",),
             F813, ('Gold 1 the band, then the four arrows labelled RSI at Bollinger lower band.',), 'Lim (2016), pp. 249 to 250, Figure 8.13, courtesy of Stockcharts.com. The marks are ours, added for teaching.'),
        pair('Figure 8.13: what oversold means here',
             ("Lim says the actual oversold was a fair distance below the Bollinger band oversold levels. His figure labels the line Oversold level [2], and his next sentence calls it the 30 percent oversold line, well below the lower band [1] (p. 249). The method catches bottoms in a rising market without waiting for the RSI to fall to 30.",),
             F813_C, ('Gold 1 the lower band, red 2 the Oversold level label.',), 'Lim (2016), p. 249, Figure 8.13, courtesy of Stockcharts.com. The marks are ours, added for teaching.', w=3.5),
        # ---- rows 113 to 116: horizontal
        Content(
            notes=('Horizontally based overlays on an oscillator.',),
            origin='Lim (2016), p. 250. The chart on the next slide is ours.',
            title='Horizontally based overlays on an oscillator',
            lines=("Practitioners look for prior support and resistance in the oscillator itself (p. 250). Breaching a resistance level is a buy, displaying resistance at a prior resistance level is a sell, breaching a support level is a sell and displaying support at a prior support level is a buy (p. 250).",),
        ),
        Content(notes=('Resistance and support in an oscillator.',), origin='Lim (2016), p. 250. ' + OUR, title='Here are resistance and support in an oscillator',
                lines=("On our oscillator the prior resistance is the earlier peak at 70 and the prior support the earlier trough at 30. It breaks through the resistance [1], a buy, and holds near the support at 32 [2], also a buy.",)),
        chart('hosc', 'AR', 'Here are resistance and support in an oscillator', 'Our oscillator with an earlier peak at 70 and an earlier trough at 30, later breaking the resistance and holding near the support.', ('Gold 1 the breach of resistance, red 2 the hold at support.',)),
        pair('Figure 8.14: oscillator support and resistance',
             ("On Lim's Nikkei 225 chart the oscillator resistance [1] is drawn, with sell signals where the oscillator shows resistance [2] (p. 251). The support and the buy signals are on the next slide.",),
             F814, ('Gold 1 the resistance line, red 2 the sell signals label.',), 'Lim (2016), p. 251, Figure 8.14. The marks are ours, added for teaching.', w=3.5),
        pair('Figure 8.14: the signals in order',
             ("Looking at the right part: the sell signals at the resistance [1] come first, then the buy signals at the support [2], with the oscillator support line [3] under them (p. 251).",),
             F814_R, ('Gold 1 the sell signals at resistance, red 2 the buy signals at support, blue 3 the support line.',), 'Lim (2016), p. 251, Figure 8.14. The marks are ours, added for teaching.', w=3.5),
        # ---- rows 117 and 118: oscillator on oscillator
        Content(
            notes=('Oscillator on oscillator: the StochRSI; formula in 8.4.',),
            origin='Lim (2016), pp. 250 to 251. The figure is on the next slide.',
            title='Oscillator on oscillator',
            lines=("Buy and sell signals may also come from the interaction between window oscillators. Lim writes \"similarly\" (p. 250): the Bollinger band on the Starbucks RSI is indicator on oscillator, and this is oscillator on oscillator. His example is the Stochastic RSI, where the stochastic of RSI values is calculated and plotted (p. 251); the formula comes in 8.4. Any of the earlier seven ways can be applied to it.",),
        ),
        pair('Figure 8.15: buying dips in an uptrend',
             ("On Lim's Apple chart the StochRSI points to potential buying dips, shown by his label Bullish oversold signals [1] and the five dotted lines his label points to, [2] to [6]. Lim says these are buying dips in an uptrend (p. 251); the chart draws no trendline, so the uptrend is the rising price. Under the first five dotted lines the StochRSI is below its 0.2 line [7]. Its axis runs 0.0 to 1.0, not 0 to 100, because the formula in 8.4, in the second class, has no x 100 (p. 254).",),
             F815, ('Gold 1 Lim\'s label, then arrowed lines.',), 'Lim (2016), p. 251, Figure 8.15, courtesy of Stockcharts.com. The marks are ours, added for teaching.', w=5.0),
        # ---- checks 10 and 11
        StackedFigureCheck(
            notes=('Both answers come from the oscillator pattern slides.',),
            origin='Questions are ours, answerable from the oscillator pattern slides before; Lim (2016), pp. 248 to 251.',
            label='Patterns on an oscillator',
            questions=(
                Question(stem='An oscillator breaks above its own resistance. The signal is:',
                         options=('A sell signal', 'No signal', 'A buy signal', 'A trigger for entry'), answer='C',
                         reason='Breaching a resistance level is a buy signal (p. 250).'),
                Question(stem='In Figure 8.14, what do marks 1 and 2 show?',
                         options=('Buy signals at resistance', 'Divergence', 'Pivot points', 'Sell at resistance, buy at support'), answer='D',
                         reason='Lim labels sell signals at resistance, buy at support (p. 251).'),
            ),
            picture=F814_R, text_w=5.3,
        ),
        CourseCheck(
            notes=('Each answer names one of the eight ways.',),
            origin='Questions are ours, answerable from the first class slides before; Lim (2016), pp. 240 to 251.',
            label='The eight ways',
            questions=(
                Question(stem='An RSI crosses above 50. Which of the eight ways is that?',
                         options=('Overbought and oversold', 'Equilibrium crossover', 'Divergence', 'Oscillator on oscillator'), answer='B',
                         reason='50 is the equilibrium of a bounded oscillator, so this is an equilibrium crossover (p. 244).'),
                Question(stem='A MACD crosses its own moving average. Which way is that?',
                         options=('Equilibrium crossover', 'Overbought and oversold', 'Signal line crossover', 'Horizontally based pattern'), answer='C',
                         reason='A signal line is a moving average of the oscillator, so crossing it is a signal line crossover (p. 246).'),
            ),
        ),
        # ---- row 123 recap of Figure 8.4
        pair('Figure 8.4 again, all five signals',
             ("Now every label on Lim's chart has been taught. At the oscillator the overbought [1] and oversold [2] readings; the crossover [3] of two lines; the divergence [4] between price and the oscillator; and the chart pattern [5] drawn on the oscillator (p. 242).",),
             F84_B, ('Gold 1 overbought, red 2 oversold, blue 3 crossover, purple 4 divergence, gold 5 chart pattern.',), 'Lim (2016), p. 242, Figure 8.4. The marks are ours, added for teaching.'),
        # ---- row 124
        Content(
            notes=('The first class closes; the second class tunes the lookback and builds the oscillators.',),
            origin='Lim (2016), pp. 240 to 251. The table on the next slide is ours.',
            title='What you can now do after the first class',
            lines=("You can name the four kinds of overlay and the two kinds of window oscillator, and say what scale invariant, static and dynamic mean. You can read an oscillator eight ways, each with one example in the table below.",
                   "The second class tunes the lookback to the market's cycle and then goes through the main oscillators one by one: the rate of change (ROC), momentum (MOM), the MACD, the average true range (ATR), the stochastic and the RSI, and then pivot points."),
        ),
        chart('ew', 'AX', 'What you can now do after the first class',
              'A table of ours with the eight ways of reading an oscillator and one example from this class for each.',
              ('One example for each of the eight ways.',)),
    )
