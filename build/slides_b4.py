"""second class slides, sections 8.7 and 8.8 (outline rows 106 to 135): overlay indicators, pivot points and the review questions.

The pivot level PP is the previous day's typical price, which Lim never defines. Figure 8.25's own numbers
(H 100, L 0, C 80, PP 60) fit (H + L + C) / 3, and every slide that uses it says it is our reading.
"""
from deckkit import Content
from chartlayout_chapter08 import CourseCheck
from slides_a2 import B, G, M, P, R, fig
from slides_b1 import OUR, Q, chart, pair, course_chart

F825 = fig('8.25', (0, 0, 1, 1), "Figure 8.25: the trend-following nature of pivot points: a daily bar with high 100, low 0 and close 80, a pivot level PP of 60, R1 of 120 and S1 of 20.",
           [M(1, G, 0.085, 0.30, 0.15, 0.40, kind='circle', at=(0.05, 0.35)), M(2, R, 0.085, 0.80, 0.15, 0.91, kind='circle', at=(0.05, 0.86)),
            M(3, B, 0.145, 0.46, 0.215, 0.54, kind='circle', at=(0.25, 0.43)), M(4, P, 0.40, 0.535, 0.495, 0.585, at=(0.52, 0.50)),
            M(5, G, 0.60, 0.205, 0.70, 0.275, at=(0.565, 0.24)), M(6, R, 0.59, 0.76, 0.69, 0.84, at=(0.575, 0.80)),
            M(7, B, 0.86, 0.20, 0.97, 0.82, at=(0.83, 0.52))], 263, 'sc')
F826 = fig('8.26', (0, 0, 1, 1), "Figure 8.26: the volatility characteristic of pivot points: the same bar with R2 of 160 and S2 of minus 40, each the PP of 60 plus or minus the day's range of 100.",
           [M(1, G, 0.61, 0.585, 0.69, 0.67, kind='circle', at=(0.73, 0.55)), M(2, R, 0.46, 0.215, 0.70, 0.31, at=(0.74, 0.26)),
            M(3, B, 0.46, 0.885, 0.70, 0.97, at=(0.74, 0.93)), M(4, P, 0.05, 0.45, 0.21, 0.90, at=(0.30, 0.50))], 264, 'sc')
F827 = fig('8.27', (0, 0, 1, 1), "Figure 8.27: R3 of 220 and R4 of 260 above, and S3 of minus 80 and S4 of minus 140 below, each a step of the day's range of 100 beyond the one before.",
           [M(1, G, 0.31, 0.075, 0.53, 0.165, at=(0.58, 0.115)), M(2, R, 0.31, 0.0, 0.53, 0.07, at=(0.58, 0.035)),
            M(3, B, 0.28, 0.805, 0.52, 0.89, at=(0.58, 0.85)), M(4, P, 0.28, 0.925, 0.52, 0.998, at=(0.58, 0.96))], 265, 'sc')
F828_L = fig('8.28', (0, 0, 0.5, 1), "Figure 8.28, left part: Goldman Sachs daily with pivot level lines and Lim's arrows to the places where price reacts to them.",
             [M(1, G, 0.094, 0.810, 0.126, 0.866, kind='circle', at=(0.09, 0.89)),
              M(2, R, 0.173, 0.618, 0.205, 0.674, kind='circle', at=(0.22, 0.62)),
              M(3, B, 0.264, 0.772, 0.296, 0.828, kind='circle', at=(0.25, 0.835)),
              M(4, P, 0.295, 0.672, 0.327, 0.728, kind='circle', at=(0.345, 0.675)),
              M(5, G, 0.442, 0.265, 0.474, 0.321, kind='circle', at=(0.49, 0.255))], 265, 'sc')
F828_R = fig('8.28', (0.49, 0, 1, 1), "Figure 8.28, right part: Lim's label Price reacting and its arrows to four reactions.",
             [M(1, G, 0.496, 0.465, 0.528, 0.521, kind='circle', at=(0.495, 0.545)),
              M(2, R, 0.544, 0.541, 0.576, 0.597, kind='circle', at=(0.585, 0.6)),
              M(3, B, 0.654, 0.311, 0.686, 0.367, kind='circle', at=(0.7, 0.305)),
              M(4, P, 0.839, 0.352, 0.871, 0.408, kind='circle', at=(0.885, 0.345))], 265, 'sc')


PCK = course_chart('pck', notes=(), origin='FIN1209 teaching chart CT. ' + OUR, title='One more day to work', letter='CT',
                   shows='Our day with high 110, low 90 and close 106 and its pivot level PP of 102 drawn forward.', tier='core', marks=())


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
            lines=("Floor Trader's Pivot Points are a numerically based overlay. From the previous day's range they project levels for the next day: a pivot level PP, resistance levels R1, R2, R3 and so on, and support levels S1, S2, S3 and so on (p. 263). Lim calls them a trend following and volatility indicator. He lists them as static (p. 240), yet new levels appear each period; in our reading a level holds for its period and a new period brings new ones.",),
            accent="Lim's own picture of the first levels comes next.",
        ),
        # ---- rows 109 and 110: Figure 8.25
        pair('Figure 8.25: the pivot level, first resistance and support',
             ("Lim says PP is the previous day's typical price (p. 263) and never defines it. On his figure the bar has a high [1] of 100, a low [2] of 0 and a close [3] of 80, and PP [4] is 60. He builds S1 [6] by projecting the distance from the high down to PP downward from PP, and R1 [5] by projecting the distance from PP down to the low upward from PP (pp. 263 to 264): 60 - 40 = 20 and 60 + 60 = 120. The \"?\" bracket [7] spans 100 points, the day's range, our arithmetic; the O tick on the left is the open."),
             F825, ('Gold 1 the high, red 2 the low, blue 3 the close, purple 4 PP, then R1, S1 and the bracket.',), 'Lim (2016), pp. 263 to 264, Figure 8.25. The marks are ours, added for teaching.', w=4.9),
        # ---- row 111: first levels worked
        Content(
            notes=('Our reading of PP, labelled as ours.', 'S1 = PP - (H - PP), R1 = PP + (PP - L).'),
            origin='Lim (2016), pp. 263 to 264. PP as (H + L + C) / 3 is our reading from Figure 8.25. ' + OUR,
            title='The first levels, worked on a day of ours',
            lines=("The book gives no formula for the typical price. Figure 8.25's numbers fit (H + L + C) / 3, so we use that, as our reading. Yesterday H 52.00 [1], L 48.00 [2], C 51.20 [3]: PP = 151.20 / 3 = 50.40 [4]. Lim's rule (pp. 263 to 264): S1 = PP - (H - PP) = 50.40 - 1.60 = 48.80 [6]; R1 = PP + (PP - L) = 50.40 + 2.40 = 52.80 [5].",),
        ),
        chart('pv1', 'CN', 'The first levels, worked on a day of ours',
              'Our yesterday bar with high 52.00, low 48.00 and close 51.20 and the levels PP 50.40, R1 52.80 and S1 48.80 drawn forward.',
              ('Gold 1 the high, red 2 the low, blue 3 the close, purple 4 PP, then R1 and S1.',)),
        # ---- row 112: why pivot points follow the trend
        Content(
            notes=('If the close is above its midprice, every level is raised.', 'Midprice is not defined in the book.'),
            origin='Lim (2016), p. 264. The reading of midprice is ours. ' + OUR,
            title='Why pivot points follow the trend',
            lines=("Lim says that if the previous close was above its midprice, all the projected levels are raised (p. 264). He does not define midprice or say raised compared with what. Our reading: midprice is the middle of the range, (H + L) / 2, and raised means higher than if the close had been at the midprice. Here both days have H 52.00 and L 48.00 [1]. A close at the middle, 50.00 [2], gives PP 50.00; a close of 51.20 [3] gives PP 50.40, R1 52.80 and S1 48.80, each raised [4].",),
        ),
        chart('pv1b', 'CS', 'Why pivot points follow the trend',
              'Two of our days with the same high and low and the middle of the range at 50.00: a close at the middle gives PP 50.00, R1 52.00 and S1 48.00, and a close of 51.20 gives PP 50.40, R1 52.80 and S1 48.80.',
              ('Gold 1 the shared high and low, red 2 the close at the middle, blue 3 the higher close, purple 4 the raised levels.',)),
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
            lines=("On our day H is 52.00 and L 48.00, so the range [4] is 4.00, and PP is 50.40 [1]. R2 = 50.40 + 4.00 = 54.40 [2] and S2 = 50.40 - 4.00 = 46.40 [3].",),
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
             ("On Lim's Figure 8.27 R3 [1] is 220, a range of 100 above R1's 120, and R4 [2] is 260, a range above R2's 160. S3 [3] is minus 80, a range below S1's 20, and S4 [4] is minus 140, a range below S2's minus 40 (pp. 264 to 265). Minus 80 and minus 140 show the method and are not real prices."),
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
            lines=("Lim's popular ways to read the day (p. 265): an open below PP suggests a lower day and above PP a higher one; breaching a second level signals a strong trend; third levels mark extreme overbought and oversold in price, not an oscillator's; a quiet day stays inside the first levels; and many use the levels for exits. Here the day opens at 51.00 [1], above PP at 50.40 [2], and breaches R2 [3] at 54.70.",),
        ),
        chart('pvd', 'CQ', 'Reading the day from the pivot',
              'Our day opening at 51.00 above PP 50.40 and rising through R1 to breach R2 at 54.70.',
              ('Gold 1 the open, red 2 PP, blue 3 the breach of R2.',)),
        # ---- rows 121 and 122: Figure 8.28
        pair('Figure 8.28: price reacting to pivot points',
             ("Lim's Figure 8.28 is Goldman Sachs on a daily chart with pivot levels, and his arrows point at places where price reacts to them (p. 265): the October low [1], the November high [2], two December reactions [3] [4] and the March high [5]. On the figure each set of levels lasts about a month, our reading, and Lim's rule is written in days; the book does not say which period this chart uses, so read the figure for how price reacts at the levels, not for the daily rule."),
             F828_L, ('Gold 1 the October low, red 2 the November high, blue 3 and purple 4 the December reactions, gold 5 the March high.',), 'Lim (2016), p. 265, Figure 8.28. The marks are ours, added for teaching.', w=4.4),
        pair('Figure 8.28: the right half',
             ("On the right Lim's label \"Price reacting\" points to four reactions [1] [2] [3] [4] (p. 265). The book gives no count of how often price reacts, so treat these as examples, not a success rate."),
             F828_R, ('Gold 1 to purple 4 the four arrow tips from the label.',), 'Lim (2016), p. 265, Figure 8.28. The marks are ours, added for teaching.', w=4.4),
        Content(
            notes=('A second worked day, the one the check uses.',),
            origin='Lim (2016), pp. 263 to 264. The PP reading is ours. ' + OUR,
            title='One more day to work',
            lines=("Take a day with H 110 [1], L 90 [2] and C 106. PP = (110 + 90 + 106) / 3 = 102 [3], and S1 = PP - (H - PP) = 102 - 8 = 94.",),
        ),
        PCK,
        # ---- rows 123 and 124: Check 23, on a day of ours so no answer is printed on the question
        CourseCheck(
            notes=('Both answers come from the pivot point slides.',),
            origin='Questions are ours, answerable from the pivot point slides before; Lim (2016), pp. 263 to 264.',
            label='Pivot points',
            questions=(
                Q(23, 'Yesterday H was 110, L 90 and C 106, so PP is 102. What is S1?', '94', ('98', '90', '114'),
                  'S1 = PP - (H - PP) = 102 - (110 - 102) = 94 (pp. 263 to 264).'),
                Q(24, 'The second resistance R2 is the PP plus', "the previous day's range", ("the previous day's close", "the previous day's low", 'half the range'),
                  "R2 = PP + the previous day's range (p. 264)."),
            ),
        ),
    )


def slides_88():
    return (
        # ---- row 125: the chapter summary
        Content(
            notes=("Lim's own sentence; the book gives no count behind 'especially effective'.",),
            origin='Lim (2016), p. 266.',
            title="Lim's chapter summary",
            lines=("Lim's summary: indicators and oscillators are \"especially effective in predicting reversals when they coincide with price barriers\" like support and resistance, trendlines, channel boundaries and Floor Trader's pivot levels (p. 266).",),
            accent="The book gives no count behind 'especially effective', so read it as advice: look for the oscillator signal at a price barrier, and act on price confirmation, as in 8.2.",
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
            lines=("The ROC is the percent change over N periods and the MOM the price difference. Lim says in most ways the MOM is identical to the ROC; the ROC has a non-linearity the MOM lacks (p. 257). When price rises $10 every 10 periods from $100, the 10 period ROC falls, 10.0, 9.1, 8.3 percent, while the MOM stays at 10 (p. 256).",),
        ),
    )
