"""second class slides, sections 8.7 and 8.8 (outline rows 106 to 135): overlay indicators, pivot points and the review questions.

The pivot level PP is the previous day's typical price, which Lim never defines. Figure 8.25's own numbers
(H 100, L 0, C 80, PP 60) fit (H + L + C) / 3, and every slide that uses it says it is our reading.
"""
from deckkit import Content
from chartlayout_chapter08 import CourseCheck, StackedFigureCheck
from slides_a2 import B, G, M, P, R, fig
from slides_b1 import OUR, Q, chart, pair

F825 = fig('8.25', (0, 0, 1, 1), "Figure 8.25: the trend-following nature of pivot points: a daily bar with high 100, low 0 and close 80, a pivot level PP of 60, R1 of 120 and S1 of 20.",
           [M(1, G, 0.085, 0.30, 0.15, 0.40, kind='circle', at=(0.05, 0.35)), M(2, R, 0.085, 0.80, 0.15, 0.91, kind='circle', at=(0.05, 0.86)),
            M(3, B, 0.145, 0.46, 0.215, 0.54, kind='circle', at=(0.25, 0.43)), M(4, P, 0.40, 0.535, 0.495, 0.585, at=(0.52, 0.50)),
            M(5, G, 0.60, 0.205, 0.70, 0.275, at=(0.58, 0.17)), M(6, R, 0.59, 0.76, 0.69, 0.84, at=(0.575, 0.80)),
            M(7, B, 0.86, 0.20, 0.97, 0.82, at=(0.83, 0.52))], 263, 'sc')
F825_CHK = fig('8.25', (0, 0, 1, 1), "Figure 8.25: a daily bar with high 100, low 0 and close 80, a pivot level PP of 60, R1 of 120 and S1 of 20.", [
    M(1, G, 0.40, 0.535, 0.495, 0.585, at=(0.52, 0.50)), M(2, R, 0.60, 0.205, 0.70, 0.275, at=(0.58, 0.17)), M(3, B, 0.59, 0.76, 0.69, 0.84, at=(0.575, 0.80))], 263, 'sc')
F826 = fig('8.26', (0, 0, 1, 1), "Figure 8.26: the volatility characteristic of pivot points: the same bar with R2 of 160 and S2 of minus 40, each the PP of 60 plus or minus the day's range of 100.",
           [M(1, G, 0.61, 0.585, 0.69, 0.67, kind='circle', at=(0.73, 0.55)), M(2, R, 0.46, 0.215, 0.70, 0.31, at=(0.74, 0.26)),
            M(3, B, 0.46, 0.885, 0.70, 0.97, at=(0.74, 0.93)), M(4, P, 0.05, 0.45, 0.21, 0.90, at=(0.30, 0.50))], 264, 'sc')
F827 = fig('8.27', (0, 0, 1, 1), "Figure 8.27: R3 of 220 and R4 of 260 above, and S3 of minus 80 and S4 of minus 140 below, each a step of the day's range of 100 beyond the one before.",
           [M(1, G, 0.33, 0.075, 0.53, 0.16, at=(0.58, 0.115)), M(2, R, 0.33, 0.005, 0.53, 0.075, at=(0.58, 0.04)),
            M(3, B, 0.31, 0.81, 0.52, 0.885, at=(0.58, 0.85)), M(4, P, 0.31, 0.93, 0.52, 0.995, at=(0.58, 0.96))], 265, 'sc')
F828_L = fig('8.28', (0, 0, 0.5, 1), "Figure 8.28, left part: Goldman Sachs daily with pivot level lines and Lim's labels where price is reacting to them.",
             [M(1, G, 0.085, 0.18, 0.29, 0.385, at=(0.31, 0.27)), M(2, R, 0.32, 0.855, 0.49, 0.935, at=(0.30, 0.82)), M(3, B, 0.33, 0.095, 0.49, 0.165, at=(0.31, 0.06))], 265, 'sc')
F828_R = fig('8.28', (0.485, 0, 1, 1), "Figure 8.28, right part: more of Lim's price reacting labels and his arrows to the pivot levels.",
             [M(1, G, 0.49, 0.665, 0.655, 0.735, at=(0.51, 0.60)), M(2, R, 0.64, 0.30, 0.69, 0.39, kind='circle', at=(0.62, 0.25)), M(3, B, 0.825, 0.33, 0.875, 0.42, kind='circle', at=(0.80, 0.28))], 265, 'sc')

F828_R.masks = ((0.485, 0.09, 0.4925, 0.18), (0.485, 0.85, 0.4925, 0.95))


def slides_87():
    return (
        # ---- rows 106 and 107: confluence of overlays
        Content(
            notes=('Overlays work best when they bunch up.', 'Say that confluence here means overlays at one price.'),
            origin='Lim (2016), p. 263. ' + OUR,
            title='Overlays work best when they bunch up',
            lines=("Lim says clusters, or confluences, of indicators in a narrow price range make a strong barrier (p. 263). Here confluence means overlays at one price, not the stochastic and RSI agreeing. Here: a prior support [1], a Fibonacci level [2] and a moving average [3] near 50.00, and price reacting [4].",),
        ),
        chart('cf', 'CM', 'Overlays work best when they bunch up',
              'Our price falling to 50.10 where a prior support at 50.00, a Fibonacci level at 50.30 and a moving average bunch together, then rising.',
              ('Gold 1 the support, red 2 the Fibonacci level, blue 3 the moving average, purple 4 price reacting.',)),
        # ---- row 108: Floor Trader's Pivot Points
        Content(
            notes=('A numerically based overlay.', 'The next slide is Lim\'s own picture.'),
            origin='Lim (2016), pp. 240 and 263.',
            title="Floor Trader's Pivot Points",
            lines=("Floor Trader's Pivot Points are a numerically based overlay. From the previous day's range they project levels for the next day: a pivot level PP, resistance levels R1, R2 and R3, and support levels S1, S2 and S3 (p. 263). Lim calls them a trend following and volatility indicator. He lists them as static (p. 240), yet new levels appear each period; in our reading a level holds for its period and a new period brings new ones.",),
            accent="Lim's own picture of the first levels comes next.",
        ),
        # ---- rows 109 and 110: Figure 8.25
        pair('Figure 8.25: the pivot level, first resistance and support',
             ("Lim says PP is the previous day's typical price (p. 263) and never defines it. On his figure the bar has a high [1] of 100, a low [2] of 0 and a close [3] of 80, and PP [4] is 60. R1 [5] is 120 and S1 [6] is 20. The \"?\" bracket [7] spans 100 points, the day's range; that is our arithmetic."),
             F825, ('Gold 1 the high, red 2 the low, blue 3 the close, purple 4 PP, then R1, S1 and the bracket.',), 'Lim (2016), pp. 263 to 264, Figure 8.25. The marks are ours, added for teaching.', w=4.4),
        # ---- row 111: first levels worked
        Content(
            notes=('Our reading of PP, labelled as ours.', 'S1 = PP - (H - PP), R1 = PP + (PP - L).'),
            origin='Lim (2016), pp. 263 to 264. PP as (H + L + C) / 3 is our reading from Figure 8.25. ' + OUR,
            title='The first levels, worked on a day of ours',
            lines=("The book gives no formula for the typical price. Figure 8.25's numbers fit (H + L + C) / 3, so we use that, as our reading. Yesterday H 52.00 [1], L 48.00 [2], C 51.20 [3]: PP = 151.20 / 3 = 50.40 [4]. S1 = PP - (H - PP) = 48.80 [6]; R1 = PP + (PP - L) = 52.80 [5].",),
        ),
        chart('pv1', 'CN', 'The first levels, worked on a day of ours',
              'Our yesterday bar with high 52.00, low 48.00 and close 51.20 and the levels PP 50.40, R1 52.80 and S1 48.80 drawn forward.',
              ('Gold 1 the high, red 2 the low, blue 3 the close, purple 4 PP, then R1 and S1.',)),
        # ---- row 112: why pivot points follow the trend
        Content(
            notes=('If the close is above its midprice, every level is raised.', 'Midprice is not defined in the book.'),
            origin='Lim (2016), p. 264. The reading of midprice is ours. ' + OUR,
            title='Why pivot points follow the trend',
            lines=("Lim says that if the previous close was above its midprice, all the projected levels are raised (p. 264); he does not define midprice; Figure 8.25 fits the middle of the range, (H + L) / 2, our reading. Here: the high [1] and low [2] have a middle of 50.00, the close [3] is above it, so PP [4], R1 [5] and S1 [6] are raised.",),
        ),
        chart('pv1', 'CN', 'Why pivot points follow the trend',
              'The same yesterday bar and levels, the close above the middle of the range and the PP above it too.',
              ('Gold 1 the high, red 2 the low, blue 3 the close, purple 4 PP, then R1 and S1.',)),
        # ---- rows 113 to 115: second levels
        Content(
            notes=('R2 and S2 add and subtract the range.', 'The next slide is Lim\'s Figure 8.26.'),
            origin='Lim (2016), p. 264.',
            title='Second resistance and support',
            lines=("The second levels use the previous day's range, its high minus its low: R2 = PP + range and S2 = PP - range (p. 264). Lim calls pivot points essentially an indicator of potential future volatility, because a wider day sets wider levels.",),
        ),
        pair('Figure 8.26: R2 and S2',
             ("On Lim's Figure 8.26 PP [1] is 60 and the range [4] is 100, so R2 [2] is 160 and S2 [3] is minus 40. Lim's round numbers start from a low of 0, so minus 40 shows the method and is not a real price."),
             F826, ('Gold 1 PP, red 2 R2, blue 3 S2, purple 4 the bar.',), 'Lim (2016), p. 264, Figure 8.26. The marks are ours, added for teaching.', w=4.4),
        Content(
            notes=('Range 4.00.',),
            origin='Lim (2016), p. 264. ' + OUR,
            title='The second levels, worked on our day',
            lines=("On our day the range is 52.00 - 48.00 = 4.00 [4] and PP is 50.40 [1]. R2 = 50.40 + 4.00 = 54.40 [2] and S2 = 50.40 - 4.00 = 46.40 [3].",),
        ),
        chart('pv2', 'CO', 'The second levels, worked on our day',
              'Our yesterday bar with PP 50.40, R2 54.40 and S2 46.40 and the range of 4.00 added and subtracted.',
              ('Gold 1 PP, red 2 R2, blue 3 S2, purple 4 the bar and its range.',)),
        # ---- rows 116 to 118: third and fourth levels
        Content(
            notes=('R3 and S3 step from the first levels, R4 and S4 from the second.',),
            origin='Lim (2016), pp. 263 to 265.',
            title='The third and fourth levels',
            lines=("The third levels step the range beyond the first: R3 = R1 + range and S3 = S1 - range. The fourth step beyond the second: R4 = R2 + range and S4 = S2 - range (pp. 264 to 265). Lim lists R1, R2, R3 and so on (p. 263) without a limit.",),
        ),
        pair('Figure 8.27: R3, R4, S3 and S4',
             ("On Lim's Figure 8.27 R3 [1] is 220 and R4 [2] is 260 above, S3 [3] is minus 80 and S4 [4] is minus 140 below, each a range of 100 beyond the level before. Minus 80 and minus 140 show the method and are not real prices."),
             F827, ('Gold 1 R3, red 2 R4, blue 3 S3, purple 4 S4.',), 'Lim (2016), pp. 264 to 265, Figure 8.27. The marks are ours, added for teaching.', w=4.4),
        Content(
            notes=('All eight lines.',),
            origin='Lim (2016), pp. 264 to 265. ' + OUR,
            title='The third and fourth levels, worked on our day',
            lines=("On our day R3 = 52.80 + 4.00 = 56.80 [1], R4 = 54.40 + 4.00 = 58.40 [2], S3 = 48.80 - 4.00 = 44.80 [3] and S4 = 46.40 - 4.00 = 42.40 [4], drawn here with the other five levels.",),
        ),
        chart('pv3', 'CP', 'The third and fourth levels, worked on our day',
              'All nine of our levels, R4 58.40 down to S4 42.40, with PP 50.40 in the middle.',
              ('Gold 1 R3, red 2 R4, blue 3 S3, purple 4 S4.',)),
        # ---- rows 119 and 120: reading the day
        Content(
            notes=('A popular way, not a rule.', 'Third levels are price readings, not an oscillator\'s.'),
            origin='Lim (2016), p. 265. ' + OUR,
            title='Reading the day from the pivot',
            lines=("Lim says an open below PP suggests a lower day and above PP a higher one; breaching a second level signals a strong trend, and third levels mark extreme overbought and oversold in price, not an oscillator's. Here: the day opens at 51.00, above PP [1] [2], and breaches R2 [3] at 54.70.",),
        ),
        chart('pvd', 'CQ', 'Reading the day from the pivot',
              'Our day opening at 51.00 above PP 50.40 and rising through R1 to breach R2 at 54.70.',
              ('Gold 1 the open, red 2 PP, blue 3 the breach of R2.',)),
        # ---- rows 121 and 122: Figure 8.28
        pair('Figure 8.28: price reacting to pivot points',
             ("Lim's Figure 8.28 is Goldman Sachs on a daily chart with pivot levels, and his labels [1] [2] [3] mark where price reacts to them (p. 265). The level sets each last about a month and Lim's rule is written in days; the book does not say which period this chart uses."),
             F828_L, ('Gold 1, red 2 and blue 3 the labels of reactions.',), 'Lim (2016), p. 265, Figure 8.28. The marks are ours, added for teaching.', w=4.4),
        pair('Figure 8.28: the right half',
             ("On the right Lim labels more reactions [1] [2] [3]. Lim claims price reacts at these levels; the book gives no count of how often it does."),
             F828_R, ('Gold 1 the label, red 2 and blue 3 the arrow tips.',), 'Lim (2016), p. 265, Figure 8.28. The marks are ours, added for teaching.', w=4.4),
        # ---- rows 123 and 124: Check 23, Figure 8.25 on both
        StackedFigureCheck(
            notes=('Both answers come from the pivot point slides.',),
            origin='Questions are ours, answerable from the pivot point slides before; Lim (2016), pp. 263 to 264.',
            label='Pivot points',
            questions=(
                Q(23, 'On Figure 8.25 the high is 100, the low 0, the close 80 and PP 60. What is S1?', '20', ('40', '0', '60'),
                  'S1 = PP - (H - PP) = 60 - (100 - 60) = 20 (p. 263).'),
                Q(24, 'The second resistance R2 is the PP plus', "the previous day's range", ("the previous day's close", "the previous day's low", 'half the range'),
                  "R2 = PP + the previous day's range (p. 264)."),
            ),
            picture=F825_CHK, text_w=5.3,
        ),
    )


def slides_88():
    return (
        # ---- row 125: the chapter summary
        Content(
            notes=("Lim's own sentence; the book gives no count behind 'especially effective'.",),
            origin='Lim (2016), p. 266.',
            title="Lim's chapter summary",
            lines=("Lim's summary says indicators and oscillators are especially effective in predicting reversals when they coincide with price barriers like support and resistance, trendlines, channel boundaries and Floor Trader's pivot levels (p. 266).",),
            accent='The book gives no count behind especially effective.',
        ),
        # ---- row 126: what you can now do
        Content(
            notes=('What this class gave you.',),
            origin='Lim (2016), pp. 252 to 265.',
            title='What you can now do',
            lines=("Tune a lookback to the half cycle and set up an hourly indicator on a shorter chart. Read the stochastic, RSI, ROC, MOM, MACD and ATR, with their levels and signals. Trade with the larger trend. Build the pivot levels from yesterday's range.",),
            accent='Next, Lim\'s eight review questions.',
        ),
        # ---- row 127: the eight questions
        Content(
            notes=('All eight questions on one slide, in our words.',),
            origin="Lim (2016), p. 266, review questions 1 to 8, in our words.",
            title='Review questions 1 to 8',
            lines=("1. Overlay indicator against window oscillator. 2. Four types of overlay, one example each. 3. The advantages and disadvantages of an unbounded oscillator. 4. Scale invariance. 5. Static against dynamic overlays. 6. The eight ways to read an oscillator. 7. An hourly and a 4 hour MACD on a 15 minute chart. 8. ROC against MOM.",),
        ),
        # ---- rows 128 to 135: one slide for each
        Content(
            notes=('Review question 1.',),
            origin='Lim (2016), pp. 235, 236 and 238.',
            title='Review question 1: overlay and window oscillator',
            lines=("An overlay indicator is plotted on the same chart as price, or on an oscillator, and acts as a barrier, support or resistance (p. 235). A window oscillator is a mathematically derived indicator that sits in a window of its own under price (pp. 236, 238).",),
        ),
        Content(
            notes=('Review question 2.',),
            origin='Lim (2016), pp. 236 and 237.',
            title='Review question 2: four overlays, one example each',
            lines=("Numerically based: a Fibonacci target, C + 1.618 x AB. Horizontally based: a prior support or resistance level. Geometrically based: a trendline. Algorithmically based: a breach of a five day high (pp. 236, 237).",),
        ),
        Content(
            notes=('Review question 3.', 'The book names one advantage; the rest is our reading.'),
            origin='Lim (2016), p. 237. The disadvantages are our reading of the same page.',
            title='Review question 3: unbounded oscillators',
            lines=("An unbounded oscillator has no upper or lower limit. The advantage Lim names is that it gives historical overbought and oversold levels, specific to one stock and timeframe (p. 237). He names no list of disadvantages; our reading from the same page: take care comparing between stocks, and values can rise or fall with no reversion.",),
        ),
        Content(
            notes=('Review question 4.',),
            origin='Lim (2016), pp. 237 to 239.',
            title='Review question 4: scale invariance',
            lines=("An indicator that scaling does not change is scale invariant (p. 237). Numerical, horizontal and algorithmic overlays and window oscillators are; geometric overlays such as trendlines are not, because ratio scaling changes their angle (p. 239).",),
        ),
        Content(
            notes=('Review question 5.',),
            origin='Lim (2016), pp. 239 to 240.',
            title='Review question 5: static and dynamic',
            lines=("A static overlay's forecast does not depend on time: horizontally and algorithmically based overlays and many numerically based ones. A dynamic overlay's does: geometrically based overlays and some numerically based ones, such as moving averages (pp. 239 to 240).",),
        ),
        Content(
            notes=('Review question 6.',),
            origin='Lim (2016), p. 240.',
            title='Review question 6: the eight ways',
            lines=("Overbought and oversold; equilibrium crossovers; signal line crossovers; divergence; geometric, numerical and horizontal pattern analysis; and oscillator on oscillator (p. 240).",),
        ),
        Content(
            notes=('Review question 7.', 'The numbers are ours.'),
            origin='Lim (2016), p. 253. The numbers are ours, worked by the book\'s method.',
            title='Review question 7: hourly and 4 hour MACD',
            lines=("On a 15 minute chart MF = 60 / 15 = 4 for the hourly and 240 / 15 = 16 for the 4 hour. The MACD's 12, 26 and 9 become 48, 104 and 36 for the hourly and 192, 416 and 144 for the 4 hour (our numbers, by the method of p. 253).",),
        ),
        Content(
            notes=('Review question 8.',),
            origin='Lim (2016), pp. 256 to 257.',
            title='Review question 8: ROC and MOM',
            lines=("The ROC is the percent change over N periods and the MOM the price difference. In most ways they act alike; the ROC has a non-linearity the MOM lacks (p. 257). When price rises $10 a period the ROC falls and the MOM stays at 10.",),
        ),
    )
