"""second class slides, section 8.6 second half (outline rows 76 to 105): the stochastic and the RSI.

Rows 76 to 85 are the approved sample slides (the stochastic, raw %K and Check 20), taken as built from
samples_chapter08 and placed by content_chapter08. This file writes rows 86 to 105.
"""
from deckkit import Content
from chartlayout_chapter08 import CourseCheck, StackedFigureCheck
from slides_a2 import B, G, M, P, R, fig
from slides_b1 import OUR, Q, chart, pair, top

F823 = fig('8.23', (0, 0, 1, 1), "Figure 8.23: daily silver with a cycle-tuned stochastic under it, its overbought and oversold levels set from its own history, and three of its bottoms.",
           [M(1, G, 0.01, 0.74, 0.78, 0.775, at=(0.80, 0.757)), M(2, R, 0.01, 0.935, 0.78, 0.965, at=(0.80, 0.95)),
            M(3, B, 0.12, 0.925, 0.16, 0.97, kind='circle', at=(0.12, 0.885)), M(4, P, 0.335, 0.925, 0.375, 0.97, kind='circle', at=(0.335, 0.885)),
            M(5, G, 0.61, 0.925, 0.65, 0.97, kind='circle', at=(0.61, 0.885))], 261, 'sc')
F823_R = fig('8.23', (0.55, 0.2, 0.99, 1.0), "Figure 8.23, right part: the price chart with Lim's label about a higher frequency of stochastic signals over the previous 140 days, his ellipse and Fibonacci retracements, and the cycle-tuned stochastic under it.",
             [M(1, G, 0.625, 0.235, 0.775, 0.31, at=(0.60, 0.29)), M(2, R, 0.785, 0.272, 0.985, 0.548, at=(0.995, 0.40)),
              M(3, B, 0.584, 0.41, 0.62, 0.465, kind='circle', at=(0.575, 0.37)), M(4, P, 0.555, 0.745, 0.94, 0.97, at=(0.987, 0.86))], 262, 'sc')
F824 = fig('8.24', (0, 0, 1, 1), "Figure 8.24: Starbucks with its RSI and its full stochastic under it, both circled where they rise back above oversold, and Lim's label about the buy trigger.",
           [M(1, G, 0.42, 0.638, 0.512, 0.775, kind='circle', at=(0.545, 0.61)), M(2, R, 0.427, 0.836, 0.51, 0.964, kind='circle', at=(0.545, 0.80))], 263, 'sc')
F824_TRIG = fig('8.24', (0.3, 0.3, 0.9, 0.645), "Figure 8.24, cropped to the price bars around the buy signal, with Lim's dotted line at the high of the bar and his label.",
                [M(1, G, 0.455, 0.445, 0.585, 0.48, at=(0.615, 0.45)), M(2, R, 0.53, 0.5, 0.77, 0.583, at=(0.795, 0.545)), M(3, B, 0.46, 0.466, 0.476, 0.553, at=(0.435, 0.52))], 262, 'sc')
F824_CHK = fig('8.24', (0, 0, 1, 1), "Figure 8.24: Starbucks with its RSI and its full stochastic under it, both circled where they rise back above oversold.",
               [M(1, G, 0.42, 0.638, 0.512, 0.775, kind='circle', at=(0.545, 0.61)), M(2, R, 0.427, 0.836, 0.51, 0.964, kind='circle', at=(0.545, 0.80))], 263, 'sc')


def slides():
    return (
        # ---- row 86: the fast stochastic
        Content(
            notes=('Fast %K is the raw %K; fast %D is its 3 period average.',),
            origin='Lim (2016), p. 260. ' + OUR,
            title='The fast stochastic',
            lines=("The fast stochastic: fast %K is the raw %K, and fast %D is a 3 period average of it (p. 260). Here, with a lookback of 3, bar 7 [3] has a highest high of 53.60, a lowest low of 50.60 and a close of 53.20, so raw %K = 2.60 / 3.00 = 86.7 [1]; with bars 5 and 6 at 15.4 and 46.4, fast %D = 49.5 [2].",),
        ),
        chart('fs', 'CC', 'The fast stochastic',
              'Ten of our bars with the raw %K and the fast %D worked on them, 86.7 and 49.5 on bar 7.',
              ('Gold 1 the raw %K, red 2 the fast %D, blue 3 the box round bars 5 to 7, the lookback for bar 7.',)),
        # ---- row 87: the slow stochastic
        Content(
            notes=('Slow %K is a 3 period average of the raw %K.', 'By the formulas slow %K is the same line as fast %D.'),
            origin='Lim (2016), pp. 260 to 261. ' + OUR,
            title='The slow stochastic',
            lines=("The slow stochastic: slow %K is a 3 period average of the raw %K, and slow %D is a 3 period average of slow %K (pp. 260 to 261). By Lim's formulas slow %K is the same line as fast %D, the gold line of the last slide, here drawn black. On the same ten bars, bar 8 gives slow %K 66.6 [1] and slow %D 51.8 [2].",),
        ),
        chart('ss', 'CD', 'The slow stochastic',
              'The same ten bars with the slow %K, the same line as the fast %D, and the slow %D worked on them, 66.6 and 51.8 on bar 8.',
              ('Gold 1 the slow %K, red 2 the slow %D, both on bar 8.',)),
        # ---- rows 88 and 89: signal line crossovers
        Content(
            notes=('Fast %K above fast %D buys.', 'The book prints slow %D in the second fast rule.'),
            origin='Lim (2016), p. 261. ' + OUR,
            title='Fast signal line crossovers',
            lines=("Fast %K crossing above fast %D is a buy; crossing below is a sell (p. 261). Lim writes slow %D in the second rule; we read it as fast %D. Here: %K falls through %D [1], a sell, and later climbs back through it [2], a buy.",),
        ),
        chart('fx', 'CE', 'Fast signal line crossovers',
              'Our fast %K and fast %D crossing downward and then upward.',
              ('Gold 1 the sell crossing, red 2 the buy crossing.',)),
        Content(
            notes=('The same rule on the slow lines.', 'The smoother lines cross later.'),
            origin='Lim (2016), p. 261. ' + OUR,
            title='Slow signal line crossovers',
            lines=("The same rule works on the slow lines: slow %K crossing above slow %D is a buy, below a sell (p. 261). On our lines the slow lines are smoother, so the crossings come later than on the fast lines: a sell at [1] and a buy at [2].",),
        ),
        chart('sx', 'CF', 'Slow signal line crossovers',
              'Our slow %K and slow %D crossing downward and then upward, later than the fast lines did.',
              ('Gold 1 the sell crossing, red 2 the buy crossing.',)),
        # ---- row 90: defaults
        Content(
            notes=('80 and 20, and 14 periods.',),
            origin='Lim (2016), pp. 259 to 261. ' + OUR,
            title='Defaults, and where 14 comes from',
            lines=("The stochastic's default levels are 80 and 20, and its default lookback is 14 periods, which Lim says was originally used to track the monthly commodity half cycle (pp. 259 to 261). Here: a reading of 90 is overbought [1] and 12 is oversold [2].",),
        ),
        chart('sdf', 'CG', 'Defaults, and where 14 comes from',
              'Our stochastic reaching 90 above the 80 line and falling to 12 below the 20 line.',
              ('Gold 1 the reading of 90, red 2 the reading of 12.',)),
        # ---- rows 91 and 92: Figure 8.23
        top('Figure 8.23: levels set by the market, not by 80 and 20',
            ("Lim's cycle tuned stochastic on silver does not use 80 and 20. He sets historical levels by eye, an overbought level [1] and an oversold level [2], which he says better reflect what market participants do, and calls this behaviorally tuned (pp. 261 to 262). For example three bottoms [3] [4] [5] touch the oversold level."),
            F823, ('Gold 1 the overbought level, red 2 the oversold level, then three bottoms.',), 'Lim (2016), pp. 261 to 262, Figure 8.23. The marks are ours, added for teaching.'),
        pair('Figure 8.23: more swings, more short term traders',
             ("Lim's label [2] says a higher frequency of stochastic signals shows short term participation increasing over the previous 140 days; the ellipse [1] points at the stretch, where the stochastic [4] alternates between its overbought and oversold boxes: Lim's text calls it a higher frequency of alternation between overbought and oversold (p. 262). He gives no count. Silver reversed at the Fibonacci retracement levels, 50 and 38.2 percent [3], while overbought."),
             F823_R, ('Gold 1 the ellipse, red 2 the label, blue 3 the reversal at the retracements, purple 4 the alternating stochastic.',), 'Lim (2016), p. 262, Figure 8.23. The marks are ours, added for teaching.', w=4.4),
        # ---- rows 93 and 94: normalizing
        Content(
            notes=('To normalize is to bind data between limits.', 'A narrow range gives big swings.'),
            origin='Lim (2016), p. 262. ' + OUR,
            title='Normalizing, and its drawback',
            lines=("To normalize is to bind data between an upper and a lower limit (p. 262); %K does it to price. The drawback is erratic swings between overbought and oversold when the range of the lookback is very narrow (p. 262). Here two closes 0.03 and 0.17 above the lowest low read 15 [1] and 85 [2] in a range of 0.20, but 1.5 and 8.5 [3] in a range of 2.00.",),
        ),
        chart('nm', 'CH', 'Normalizing, and its drawback',
              'Two small charts of ours: the same two closes read 15 and 85 percent in a narrow range, oversold to overbought, and 1.5 and 8.5 in a wide one.',
              ('Gold 1 and red 2 the narrow range readings, blue 3 the wide range reading.',)),
        # ---- rows 95 and 96: Check 21
        CourseCheck(
            notes=('Both answers come from the stochastic slides.',),
            origin='Questions are ours, answerable from the stochastic slides before; Lim (2016), pp. 259 to 262.',
            label='The stochastic',
            questions=(
                Q(19, 'In the fast stochastic, what is fast %D?', 'A 3 period average of the raw %K', ('The raw %K itself', 'A 3 period average of fast %D', 'The highest high of 14 periods'),
                  'Fast %K is the raw %K and fast %D is its 3 period average (p. 260).'),
                Q(20, 'The range of a lookback is 0.20 and the close is 0.10 above the lowest low. What does the raw %K read?', '50 percent', ('10 percent', '75 percent', '5 percent'),
                  '(C - Ln) / (Hn - Ln) = 0.10 / 0.20 = 50 percent (p. 260). In a range of 2.00 the same close would read 5 percent.'),
            ),
        ),
        # ---- rows 97 to 99: the RSI
        Content(
            notes=('Welles Wilder; how much of the move was up.',),
            origin='Lim (2016), p. 262.',
            title='RSI: how much of the move was up',
            lines=("The relative strength index, RSI, is Welles Wilder's measure of how much of the recent move was up: the average gain over the average loss across the last n periods (p. 262). Its default is 14 periods, and the next slide turns it into a formula.",),
            accent='When the moves are mostly gains the RSI rises; when they are mostly losses it falls.',
        ),
        Content(
            notes=('RS = G / L and RSI = 100 x G / (G + L).', 'Gold 1 G, red 2 L, blue 3 the RSI.'),
            origin='Lim (2016), p. 262. ' + OUR,
            title='The RSI formula',
            lines=("RS = G / L, with G the average gain and L the average loss, taken as a positive size, and RSI = 100 - 100 / (1 + G/L) = 100 x G / (G + L) (p. 262). Wilder's averaging is a form of exponential moving average; no formula is given. Here: G 1.20 [1], L 0.80 [2], RS 1.5, RSI 60 [3].",),
        ),
        chart('rsf', 'CI', 'The RSI formula',
              'Our average gain 1.20 and average loss 0.80 as two columns and the RSI they give, 60, on a 0 to 100 scale.',
              ('Gold 1 the average gain, red 2 the average loss, blue 3 the RSI of 60.',)),
        Content(
            notes=('The same numbers on five bars.',),
            origin='Lim (2016), p. 262. ' + OUR,
            title='Our RSI worked on five bars',
            lines=("The same numbers on five changes: +3, -1, +2, -3 and +1. The gains 3 + 2 + 1 = 6, the biggest +3 [1], make G = 6 / 5 = 1.20; the losses 1 + 3 = 4, the biggest -3 [2], make L = 0.80. The RSI at the last close [3] is 100 x 1.20 / 2.00 = 60. We use plain averages, as the book gives no formula for Wilder's.",),
        ),
        chart('r5', 'CJ', 'Our RSI worked on five bars',
              'Six of our closes from 100 to 102 with the five changes, the gains of 6 and the losses of 4 and an RSI of 60.',
              ('Gold 1 the biggest gain, red 2 the biggest loss, blue 3 the last close.',)),
        # ---- row 100: RSI against the stochastic
        Content(
            notes=('The RSI is less volatile.', 'Lim says identical, then similar; we say similar.'),
            origin='Lim (2016), p. 262. ' + OUR,
            title='RSI against the stochastic',
            lines=("Lim calls the RSI less volatile than the stochastic, a good replacement for it in volatile markets, with defaults of 70 and 30 (p. 262). He says the %K process is identical to the RSI's, then similar; we say similar. On closes of ours, the stochastic reaches 100 [1] while the RSI reads 60.8 [2].",),
        ),
        chart('rvs', 'CK', 'RSI against the stochastic',
              'Our closes with a 14 period stochastic that reaches 100 and a 14 period RSI that reads 60.8 at the same bar.',
              ('Gold 1 the stochastic at its peak, red 2 the RSI at the same bar.',)),
        # ---- row 101: when both agree
        Content(
            notes=('Both dip below oversold, then both rise back.', 'Lim does not reconcile this with p. 245.'),
            origin='Lim (2016), pp. 245 and 262. ' + OUR,
            title='When both agree',
            lines=("Many practitioners count a confluence of signals, a dip below oversold on both the stochastic [1] and the RSI [2], then a rise back above on both [3] [4], as more reliable (p. 262). Lim also warns that price based oscillators agreeing can be a false consensus (p. 245). He does not reconcile the two, and neither do we.",),
        ),
        chart('ag', 'CL', 'When both agree',
              'Our price, stochastic and RSI, both oscillators falling below oversold together and rising back above it.',
              ('Gold 1 and red 2 the dips below oversold, blue 3 and purple 4 the rises back above.',)),
        # ---- rows 102 and 103: Figure 8.24
        pair('Figure 8.24: a buy signal on both oscillators',
             ("Figure 8.24 is Starbucks: the caption says Goldman Sachs, but the text and the image are Starbucks. The RSI [1] and the stochastic [2] both dip below oversold and rise back above it, which Lim reads as a buy signal (p. 262)."),
             F824, ('Gold 1 the RSI circle, red 2 the stochastic circle.',), 'Lim (2016), p. 263, Figure 8.24. The marks are ours, added for teaching.', w=4.4),
        top('Figure 8.24: the trigger',
            ("The signal is on the oscillators; the trigger is on price. Lim says the trigger for entry is normally the high of the bar or candlestick tied to the buy signal (p. 262): the dotted line [1] at the high of the lowest candlestick [3], with his label buy above the high of the lowest candlestick [2]."),
            F824_TRIG, ('Gold 1 the dotted line at the high, red 2 the label, blue 3 the lowest candlestick.',), 'Lim (2016), p. 262, Figure 8.24. The marks are ours, added for teaching.'),
        # ---- rows 104 and 105: Check 22
        StackedFigureCheck(
            notes=('Both answers come from the Figure 8.24 slides.',),
            origin='Questions are ours, answerable from the slides before; Lim (2016), pp. 262 to 263.',
            label='Stochastic and RSI together',
            questions=(
                Q(21, 'Lim reads a buy on Figure 8.24 when', 'both dip below oversold, then rise back', ('only the RSI crosses 50', 'the stochastic passes 80', 'price breaks a trendline'),
                  'A dip below oversold on both, then a rise back above on both, is the buy signal (p. 262).'),
                Q(22, 'What is normally the trigger for entry?', 'The high of the bar tied to the buy signal', ('The RSI crossing 50', 'The stochastic reaching 100', 'The low of the bar'),
                  'The trigger is normally the high of the bar or candlestick tied to the buy signal (p. 262).'),
            ),
            picture=F824_CHK, text_w=5.3,
        ),
    )
