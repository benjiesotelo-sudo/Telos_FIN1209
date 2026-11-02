"""second class slides, section 8.6 first half (outline rows 45 to 75): momentum, the ROC, the MOM, the MACD and the ATR.

Same rules as slides_b1. A text slide in front of one of our charts is folded onto the chart's slide, so each
such text stays to three lines.
"""
from deckkit import Content
from chartlayout_chapter08 import CourseCheck, StackedFigureCheck, TopPair, WidePair
from slides_a2 import B, G, M, P, R, fig
from slides_b1 import OUR, Q, chart, pair, top

PURPLE = P


# ------------------------------------------------------------------ Lim's figures
F818_A = fig('8.18', (0, 0, 0.442, 1), "Figure 8.18, left part: Goldman Sachs with its ROC under it. In the first box the price is flat or ranging and the ROC declines; in the second the price rises steadily and the ROC is flat or ranging.",
             [M(1, G, 0.28, 0.76, 0.43, 0.935, at=(0.25, 0.85)), M(2, R, 0.055, 0.755, 0.222, 0.93, at=(0.032, 0.80))], 256)
F818_B = fig('8.18', (0.455, 0, 1, 1), "Figure 8.18, right part: the ROC with Lim's historical overbought level, his zero line crossovers and his Points 1, 2 and 3.",
             [M(1, G, 0.525, 0.855, 0.70, 0.935, at=(0.51, 0.80)), M(2, R, 0.64, 0.765, 0.965, 0.81, at=(0.985, 0.70)),
              M(3, B, 0.652, 0.20, 0.695, 0.30, kind='circle', at=(0.625, 0.34)), M(4, P, 0.776, 0.19, 0.82, 0.29, kind='circle', at=(0.752, 0.34)),
              M(5, G, 0.91, 0.19, 0.955, 0.29, kind='circle', at=(0.885, 0.34))], 256, 'sc')
F818_B.masks = ((0.455, 0.015, 0.497, 0.052), (0.455, 0.715, 0.476, 0.738), (0.455, 0.935, 0.476, 0.975))
F819_TOP = fig('8.19', (0, 0, 1, 0.8), "Figure 8.19, upper part: Goldman Sachs with its 12 and 26 day EMAs, and under it the MACD, with Lim's solid arrows from the crossings of the two averages down to the MACD at zero.",
               [M(1, G, 0.19, 0.69, 0.222, 0.76, kind='circle', at=(0.235, 0.66)), M(2, R, 0.263, 0.70, 0.295, 0.77, kind='circle', at=(0.31, 0.665)),
                M(3, B, 0.485, 0.69, 0.517, 0.76, kind='circle', at=(0.535, 0.66))], 257, 'sc')
F819_LOW = fig('8.19', (0, 0.55, 1, 1), "Figure 8.19, lower part: the MACD with its signal line and, under it, the MACD histogram, with Lim's dotted arrows from the signal line crossings down to the histogram at zero.",
               [M(1, G, 0.074, 0.835, 0.106, 0.89, kind='circle', at=(0.05, 0.80)), M(2, R, 0.409, 0.84, 0.441, 0.895, kind='circle', at=(0.385, 0.805)),
                M(3, B, 0.664, 0.84, 0.696, 0.895, kind='circle', at=(0.64, 0.805)), M(4, P, 0.804, 0.84, 0.836, 0.895, kind='circle', at=(0.78, 0.805))], 258, 'sc')
F820 = fig('8.20', (0, 0, 1, 1), "Figure 8.20: the hourly USDJPY with its MACD under it, a historically overbought level marked in the MACD window and three arrows from the MACD peaks up to the price tops.",
           [M(1, G, 0.2, 0.69, 0.48, 0.745, at=(0.50, 0.72)), M(2, R, 0.165, 0.655, 0.205, 0.715, kind='circle', at=(0.12, 0.60)),
            M(3, B, 0.515, 0.655, 0.555, 0.715, kind='circle', at=(0.47, 0.60)), M(4, P, 0.81, 0.655, 0.85, 0.715, kind='circle', at=(0.765, 0.60))], 258, 'sc')
F821 = fig('8.21', (0, 0, 1, 1), "Figure 8.21: daily gold with its true range under it, a historically overextended level, and the 16 times since August 2007 that the true range has reached it, numbered 1 to 16.",
           [M(1, G, 0.445, 0.70, 0.73, 0.75, at=(0.42, 0.725)), M(2, R, 0.088, 0.775, 0.13, 0.865, kind='circle', at=(0.108, 0.725)),
            M(3, B, 0.724, 0.775, 0.766, 0.865, kind='circle', at=(0.745, 0.725)), M(4, P, 0.874, 0.775, 0.916, 0.865, kind='circle', at=(0.895, 0.725))], 259, 'sc')


def slides():
    return (
        # ---- rows 45 and 46: momentum turns before price
        Content(
            notes=('Momentum is acceleration.', 'Gold 1 price still rising, red 2 momentum already turned down.'),
            origin='Lim (2016), p. 255; Chapter 4, "Momentum turns before price". ' + OUR,
            title='Momentum oscillators track acceleration',
            lines=("Momentum oscillators such as the MOM, ROC, MACD and stochastics track how fast price speeds up or slows down (p. 255). Momentum tends to weaken and strengthen before price, as Chapter 4 said. Here: price still rises [1] while momentum, the change over one bar, has already turned down [2].",),
        ),
        chart('mo', 'BP', 'Momentum oscillators track acceleration',
              'Our price still rising at 60.00 while our momentum, its one bar change, peaked at 2.0 and has fallen to 0.3.',
              ('Gold 1 price still rising, red 2 the momentum peak.',)),
        # ---- row 47: when momentum oscillators let you down
        Content(
            notes=('Chart R again, from the first class.',),
            origin='Lim (2016), pp. 255 to 256. ' + OUR,
            title='When momentum oscillators let you down',
            lines=("In strong, long trends a momentum oscillator stays overbought or oversold (p. 255). Lim turns to price overlays such as support and resistance, trendlines, moving averages and channels, perhaps the ADX, and advises mastering one oscillator (pp. 255 to 256). Ten readings above 80 [1] while price still rises [2].",),
        ),
        chart('stuck', 'R', 'When momentum oscillators let you down',
              'Our steadily rising price with a bounded oscillator staying above 80 for ten readings.',
              ('Gold 1 the ten readings above 80, red 2 price still rising.',)),
        # ---- rows 48 to 51: the ROC
        Content(
            notes=('Percent change over N periods.', 'Typical price, midprice and weighted close are not defined.'),
            origin='Lim (2016), p. 256. ' + OUR,
            title='ROC: the percent change over N periods',
            lines=("The rate of change, ROC, is the percent change in price over N periods: (latest price - price N periods back) / price N periods back, times 100 percent (p. 256). It usually uses closes; Lim also names typical price, midprice and weighted close without defining them. Here: latest $110 [1], ten periods back $100 [2], so 10 percent.",),
        ),
        chart('rcp', 'BQ', 'ROC: the percent change over N periods',
              'Our price rising from $100 to $110 over ten periods, a ROC of 10 percent.',
              ('Gold 1 the latest price, red 2 the price ten periods back.',)),
        Content(
            notes=('The book says $90 once where its numbers use $100.',),
            origin='Lim (2016), p. 256. ' + OUR,
            title='A ROC worked two ways',
            lines=("Lim works two cases (p. 256). A move from $1 to $11 is (11 - 1) / 1 x 100 = 1000 percent [1] [2]; one from $100 to $110 is (110 - 100) / 100 x 100 = 10 percent [3] [4]. The dollar gain is the same $10 and the ROC is not. His text says $90 where the numbers use $100; we use the numbers.",),
        ),
        chart('rcw', 'BR', 'A ROC worked two ways',
              'Two small charts of ours: $1 rising to $11, a ROC of 1000 percent, and $100 rising to $110, a ROC of 10 percent.',
              ('Gold 1 and red 2 the $1 and $11, blue 3 and purple 4 the $100 and $110.',)),
        Content(
            notes=('A steady rise in dollars makes the ROC fall.',),
            origin='Lim (2016), p. 256. This part is our arithmetic from his formula. ' + OUR,
            title='A steady rise in dollars makes the ROC fall',
            lines=("Lim says that if prices rise $10 every 10 periods the ROC flattens out as prices rise (p. 256). Here: price $100, $110, $120, $130 [1]; the ROC over 10 periods falls from 10.0 [2] to 9.1 to 8.3 percent [3], because the same $10 is a smaller share of a bigger price.",),
        ),
        chart('rcd', 'BS', 'A steady rise in dollars makes the ROC fall',
              'Our price rising $10 every ten periods from $100 and its ROC falling from 10.0 to 9.1 to 8.3 percent.',
              ('Gold 1 the price, red 2 the first ROC 10.0, blue 3 the last ROC 8.3.',)),
        Content(
            notes=('Steady in percent keeps the ROC flat.', 'Say that this is our reading of his formula.'),
            origin='Lim (2016), p. 256. This part is our arithmetic from his formula. ' + OUR,
            title='A steady rise in percent keeps the ROC flat',
            lines=("Lim says the ROC stays flat when price rises at a steady rate, yet he used steady for dollars just before. Only a steady percentage keeps it flat; that reading is ours, from his formula. Here: price rises 10 percent every 10 periods, $100, $110, $121, $133.10 [1], and the ROC stays 10.0 [2] [3].",),
        ),
        chart('rcpc', 'BT', 'A steady rise in percent keeps the ROC flat',
              'Our price rising 10 percent every ten periods from $100 and its ROC staying at 10.0 percent.',
              ('Gold 1 the price, red 2 and blue 3 the ROC, 10.0 each time.',)),
        # ---- rows 52 and 53: Figure 8.18
        pair('Figure 8.18: flat, then declining',
             ("Lim's Figure 8.18 shows the ROC on Goldman Sachs. Where price rises at a constant rate the ROC stays flat [1]; where price starts ranging the ROC declines [2] (p. 256). Lim's words: the ROC declines when prices are flat and remains flat during constant rates of price increase.",),
             F818_A, ('Gold 1 the flat ROC during the steady rise, red 2 the declining ROC.',), 'Lim (2016), p. 256, Figure 8.18. The marks are ours, added for teaching.', w=4.4),
        pair('Figure 8.18: the zero line, the overbought level and Points 1 to 3',
             ("On the right Lim marks the zero line crossovers [1] and a historically overbought level [2], and Points 1 [3], 2 [4] and 3 [5] where the ROC reaches it. He says the ROC reverses before price at Points 1 to 3, the most important and useful characteristic of momentum oscillators (p. 257). His text calls them tops and bottoms; all three are tops.",),
             F818_B, ('Gold 1 the zero crossovers, red 2 the level, then the three points.',), 'Lim (2016), pp. 256 to 257, Figure 8.18. The marks are ours, added for teaching.', w=4.4),
        # ---- rows 54 and 55: the MOM
        Content(
            notes=('MOM is the price difference.', 'The ROC has a non-linearity the MOM lacks.'),
            origin='Lim (2016), pp. 256 to 257. This part is our arithmetic from his formula. ' + OUR,
            title='MOM: the price difference over N periods',
            lines=("Momentum, MOM, is the price difference over N periods: latest price minus price N periods back, usually on closes (pp. 256 to 257). Lim says it lacks the ROC's non-linearity (p. 257): a rise of $10 gives MOM 10 at any price. Here: $100, $110, $120, $130 [1] and MOM 10, 10, 10 [2] [3], so it does not flatten.",),
        ),
        chart('mom', 'BU', 'MOM: the price difference over N periods',
              'Our price rising $10 every ten periods from $100 and its MOM staying at 10.',
              ('Gold 1 the price, red 2 and blue 3 the MOM, 10 each time.',)),
        # ---- row 56: ROC and MOM side by side
        Content(
            notes=('Review question 8.',),
            origin='Lim (2016), p. 257, review question 8. The table is ours, from his two formulas.',
            title='ROC and MOM on the same prices',
            lines=("Review question 8 asks how the two differ. Lim says that in most ways they act alike; the difference he names is the ROC's non-linearity (p. 257). On our prices the ROC falls, 10.0, 9.1, 8.3 percent, while the MOM stays at 10 dollars.",),
        ),
        chart('rm', 'BV', 'ROC and MOM on the same prices',
              'A table of ours with the ROC falling and the MOM staying at 10 over three equal dollar rises.',
              ('ROC 10.0, 9.1, 8.3; MOM 10, 10, 10.',)),
        # ---- rows 57 and 58: Check 17
        CourseCheck(
            notes=('Both answers come from the ROC and MOM slides.',),
            origin='Questions are ours, answerable from the ROC and MOM slides before; Lim (2016), pp. 256 to 257.',
            label='ROC and MOM',
            questions=(
                Q(11, 'Price rises $10 every 10 periods from $100. What does the ROC over 10 periods do?', 'It falls: 10.0, 9.1, 8.3 percent', ('It stays at 10 percent', 'It rises', 'It is zero'),
                  '$10 is a smaller share of each higher price: 10 / 100, 10 / 110, 10 / 120 (p. 256).'),
                Q(12, 'What difference between the ROC and the MOM does Lim name?', 'The ROC has a non-linearity the MOM lacks', ('The MOM uses volume', 'The ROC is bounded', 'The MOM needs two lines'),
                  'Lim says the MOM does not have the non-linearity of the ROC (p. 257).'),
            ),
        ),
        # ---- rows 59 and 60: the MACD
        Content(
            notes=('Gerald Appel; one moving average minus another.', 'Gold 1 the EMA crossing, red 2 the MACD at zero.'),
            origin='Lim (2016), p. 257. ' + OUR,
            title='The MACD: two moving averages detrended',
            lines=("The MACD, created by Gerald Appel, subtracts one moving average from another, which Lim calls detrending them (p. 257): MACD = 12 period EMA minus 26 period EMA. Here: the 12 period EMA crosses above the 26 period EMA [1] and the MACD crosses above zero [2] at the same bar; it stays positive while the 12 is above the 26.",),
        ),
        chart('mc', 'BW', 'The MACD: two moving averages detrended',
              'Our 12 and 26 period EMAs crossing, and under them the MACD, their difference, crossing zero at the same bar.',
              ('Gold 1 the EMAs crossing, red 2 the MACD crossing zero.',)),
        # ---- row 61: Figure 8.19, upper part
        pair('Figure 8.19: the MACD tests zero when the EMAs cross',
             ("Lim says every time the 12 EMA tests or crosses the 26 EMA, the MACD tests zero (p. 257). His solid arrows [1] [2] [3] run from where the averages meet down to the MACD at zero. His text points to Figure 8.16 here; the MACD is Figure 8.19. When the averages diverge the MACD moves away from zero, and when they converge it moves toward it.",),
             F819_TOP, ('Gold 1, red 2 and blue 3 the arrowheads at the MACD zero level.',), 'Lim (2016), p. 257, Figure 8.19. The marks are ours, added for teaching.', w=4.2),
        # ---- row 62: the histogram
        Content(
            notes=('MACD minus its nine period signal line.', 'Gold 1 the MACD crossing its signal line, red 2 the histogram crossing zero.'),
            origin='Lim (2016), p. 258. ' + OUR,
            title='The MACD histogram',
            lines=("The MACD histogram is the MACD minus its 9 period signal line; Lim calls it a double detrended oscillator (p. 258). It reaches zero when the MACD crosses its signal line. Here: the MACD crosses its signal line [1] and the histogram crosses zero [2] at that bar, before the MACD itself reaches zero.",),
        ),
        chart('mh', 'BX', 'The MACD histogram',
              'Our MACD and its signal line, and under them the histogram, their difference, crossing zero when the MACD crosses its signal line.',
              ('Gold 1 the MACD crossing its signal line, red 2 the histogram at zero.',)),
        # ---- row 63: Figure 8.19, lower part
        top('Figure 8.19: the histogram reacts first',
            ("Lim's dotted arrows [1] [2] [3] [4] run from the MACD crossing its signal line down to the histogram at zero. He says the histogram tends to react faster than the MACD by reversing before it (p. 258). He also says detrending removes the trend component (p. 257) and then that it removes the lag (p. 258); the book does not reconcile the two."),
            F819_LOW, ('Gold 1 to purple 4 the histogram zero crossings.',), 'Lim (2016), p. 258, Figure 8.19. The marks are ours, added for teaching.'),
        # ---- row 64: Figure 8.20
        pair('Figure 8.20: a historically overbought MACD',
             ("Lim's Figure 8.20 gives the MACD a historically overbought level [1]. Each time the MACD reaches it [2] [3] [4], Lim reads a potential top in the price (p. 258). He uses the hourly USDJPY in his text and the chart's own header says hourly; the caption says 4-hour, and we use hourly.",),
             F820, ('Gold 1 the level, red 2, blue 3 and purple 4 the three tops.',), 'Lim (2016), pp. 258 to 259, Figure 8.20. The marks are ours, added for teaching.', w=4.2),
        # ---- rows 65 and 66: Check 18, Figure 8.19 on both
        StackedFigureCheck(
            notes=('Both answers come from the MACD slides.',),
            origin='Questions are ours, answerable from the MACD slides before; Lim (2016), pp. 257 to 258.',
            label='The MACD',
            questions=(
                Q(13, 'What is the MACD histogram?', 'The MACD minus its signal line', ('12 EMA minus 26 EMA', 'Signal line minus ROC', 'MACD divided by price'),
                  'Lim calls it a double detrended oscillator: the MACD minus its signal line (p. 258).'),
                Q(14, 'On Figure 8.19, when the 12 EMA crosses the 26 EMA, the MACD', 'crosses its zero level', ('crosses 100', 'reaches its signal line first', 'stays away from zero'),
                  'The MACD is the 12 EMA minus the 26 EMA, so it tests zero when they cross (p. 257).'),
            ),
            picture=F819_TOP, text_w=5.3,
        ),
        # ---- rows 67 to 70: the ATR
        Content(
            notes=('ATR is Welles Wilder\'s volatility measure.', 'The true range comes first.'),
            origin='Lim (2016), p. 258.',
            title='ATR: how far price moves in a bar',
            lines=("The average true range, ATR, is Welles Wilder's measure of volatility: how far price moves in a bar (p. 258). It is built from the true range, so we build that first, then average it.",),
            accent='Volatility is the size of the moves; the ATR gives it one number.',
        ),
        Content(
            notes=('Largest of three.', 'Gold 1 the bar range, red 2 close to high, blue 3 close to low.'),
            origin='Lim (2016), p. 258; Chapter 3, true range. ' + OUR,
            title='The true range is the largest of three',
            lines=("The true range is the largest of three distances (p. 258; Chapter 3): the bar's own range, the previous close to the high, and the previous close to the low. Here: previous close 102.00, bar high 108.00, low 105.50. The range [1] is 2.50, close to high [2] is 6.00, close to low [3] is 3.50, so the true range is 6.00.",),
        ),
        chart('tr', 'BY', 'The true range is the largest of three',
              'Our previous bar closing at 102.00 and a bar with high 108.00 and low 105.50, with the three distances 2.50, 6.00 and 3.50.',
              ('Gold 1 the bar range 2.50, red 2 the close to high 6.00, blue 3 the close to low 3.50.',)),
        Content(
            notes=('Simple moving average of true range.', 'Stopsize is a multiple of the ATR.'),
            origin='Lim (2016), p. 259; Chapter 5, stopsize. ' + OUR,
            title='ATR is the average of the true range',
            lines=("The ATR is a simple moving average of the true range (p. 259). Here: true ranges of 6.00 [1], 2.50 [2] and 3.50 [3] average 4.00 [4]. Chapter 5 sized a stop; Lim says stopsizes are some multiple of the ATR (p. 259).",),
        ),
        chart('atr', 'BZ', 'ATR is the average of the true range',
              'Three of our true ranges, 6.00, 2.50 and 3.50, and their average, 4.00, drawn as a line.',
              ('Gold 1, red 2 and blue 3 the three true ranges, purple 4 their average.',)),
        # ---- rows 71 and 72: what the ATR says
        Content(
            notes=('The book gives no reason.',),
            origin='Lim (2016), p. 259. The table is ours, from his sentences.',
            title='What the ATR says in a trend',
            lines=("In an uptrend a rising ATR is bullish and a falling one bearish; in a downtrend a falling ATR is bullish and a rising one bearish; and a high or extreme ATR usually comes with price peaks and troughs (p. 259). The book gives no reason for these readings.",),
        ),
        chart('atrt', 'CA', 'What the ATR says in a trend',
              'A table of ours: a rising ATR is bullish in an uptrend and bearish in a downtrend, a falling ATR the reverse.',
              ('Rising: bullish, bearish. Falling: bearish, bullish.',)),
        Content(
            notes=('A falling ATR in an uptrend is a warning.', 'Gold 1 price, red 2 the ATR, blue 3 the warning.'),
            origin='Lim (2016), p. 259. ' + OUR,
            title='A falling ATR in an uptrend',
            lines=("Here is the bearish case from the table. Price keeps rising [1] while the ATR falls [2]; Lim reads a falling ATR in an uptrend as bearish, and the last bars [3] are where that warning stands (p. 259). The book gives no reason, so we state none.",),
        ),
        chart('atru', 'CB', 'A falling ATR in an uptrend',
              'Our price rising throughout while our ATR rises to 4.0 and then falls to 1.6.',
              ('Gold 1 the rising price, red 2 the falling ATR, blue 3 the last bars.',)),
        # ---- row 73: Figure 8.21
        top('Figure 8.21: the true range reaching its overextended level',
            ("Figure 8.21 is the true range, an ATR with a lookback of 1, on gold. Lim marks a historically overextended level [1] reached 16 times since August 2007, for example touches 1 [2], 8 [3] and 16 [4]. His text says a correction follows every time it is passed (p. 259); the figure says prices normally stall or retrace (p. 260). We show both."),
            F821, ('Gold 1 the level, red 2, blue 3 and purple 4 touches 1, 8 and 16.',), 'Lim (2016), pp. 259 to 260, Figure 8.21. The marks are ours, added for teaching.'),
        # ---- rows 74 and 75: Check 19
        CourseCheck(
            notes=('Both answers come from the ATR slides.',),
            origin='Questions are ours, answerable from the ATR slides before; Lim (2016), pp. 258 to 259.',
            label='The ATR',
            questions=(
                Q(15, 'The previous close is 102.00 and the bar has a high of 108.00 and a low of 105.50. What is the true range?', '6.00', ('2.50', '3.50', '4.00'),
                  'The three distances are 2.50, 6.00 and 3.50; the true range is the largest, 6.00 (p. 258).'),
                Q(16, 'What is the ATR?', 'A simple moving average of the true range', ('The largest of three ranges in one bar', 'The previous close minus the low', 'An exponential average of volume'),
                  'Lim defines it as a simple moving average of the true range (p. 259).'),
            ),
        ),
    )
