"""first class slides, section 8.1 (outline rows 10 to 56), written by hand in teaching order.

Rows 1 to 9 are the approved samples and are taken as built from samples_chapter08.
Every number on a chart is ours, invented for teaching; every Lim figure is read
with Lim's words only, and our numbers never go on his picture.
"""
from deckkit import Content, Question
from chartlayout_chapter08 import CourseCheck, StackedFigureCheck, WidePair, book_crop, course_chart


def chart(asset, letter, title, shows, notes, origin):
    return course_chart(asset, notes=notes, origin=origin, title=title, letter=letter, shows=shows, tier='core', marks=())


# Lim's flow chart, Figure 8.2, cut into its two halves; the boxes start above their own words.
from deckkit import Mark  # noqa: E402
FIG_8_2_LEFT = book_crop('8.2', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.2: Lim's flow chart of indicators. The window oscillator side is marked: bounded, semi bounded and fully unbounded, each with his list of examples.",
    marks=(
        Mark(number=1, kind='box', x0=0.0, y0=0.335, x1=0.172, y1=0.725, color='gold', at=(0.085, 0.76), size=0.28),
        Mark(number=2, kind='box', x0=0.165, y0=0.335, x1=0.352, y1=0.875, color='red', at=(0.265, 0.91), size=0.28),
        Mark(number=3, kind='box', x0=0.345, y0=0.335, x1=0.53, y1=0.995, color='blue', at=(0.443, 0.30), size=0.28),
    ))
FIG_8_2_LEFT.origin = 'Lim (2016), p. 238, Figure 8.2. The marks are ours, added for teaching.'
FIG_8_2_RIGHT = book_crop('8.2', (0.0, 0.0, 1.0, 1.0),
    "Figure 8.2: Lim's flow chart of indicators. The overlay side is marked: numerically, geometrically, algorithmically and horizontally based, with his lists and his scale labels.",
    marks=(
        Mark(number=1, kind='box', x0=0.555, y0=0.285, x1=0.78, y1=0.855, color='gold', at=(0.535, 0.30), size=0.28),
        Mark(number=2, kind='box', x0=0.818, y0=0.245, x1=0.998, y1=0.60, color='red', at=(0.975, 0.215), size=0.28),
        Mark(number=3, kind='box', x0=0.818, y0=0.605, x1=0.998, y1=0.83, color='blue', at=(0.80, 0.70), size=0.28),
        Mark(number=4, kind='box', x0=0.555, y0=0.858, x1=0.785, y1=0.995, color='purple', at=(0.815, 0.93), size=0.28),
    ))
FIG_8_2_RIGHT.origin = 'Lim (2016), p. 238, Figure 8.2. The marks are ours, added for teaching.'

# Figure 8.3: the same Nasdaq 100 chart on a ratio scale (top) and a linear scale (bottom).
FIG_8_3_TOP = book_crop('8.3', (0.0, 0.0, 1.0, 0.5),
    "Figure 8.3, top chart: the Nasdaq 100 on a ratio scale with an uptrend line, and the price breaking through it early.",
    marks=(
        Mark(number=1, kind='line', x0=0.182, y0=0.443, x1=0.704, y1=0.160, color='gold', at=(0.20, 0.36), size=0.28),
        Mark(number=2, kind='circle', x0=0.632, y0=0.178, x1=0.668, y1=0.222, color='red', at=(0.60, 0.14), size=0.28),
    ))
FIG_8_3_TOP.origin = 'Lim (2016), p. 239, Figure 8.3, courtesy of Stockcharts.com. The marks are ours, added for teaching.'
FIG_8_3_BOT = book_crop('8.3', (0.0, 0.5, 1.0, 1.0),
    "Figure 8.3, bottom chart: the same Nasdaq 100 on a linear scale with its uptrend line, and the price breaking through it later.",
    marks=(
        Mark(number=1, kind='line', x0=0.30, y0=0.948, x1=0.757, y1=0.819, color='gold', at=(0.32, 0.90), size=0.28),
        Mark(number=2, kind='circle', x0=0.636, y0=0.835, x1=0.672, y1=0.879, color='red', at=(0.60, 0.80), size=0.28),
    ))
FIG_8_3_BOT.origin = 'Lim (2016), p. 239, Figure 8.3, courtesy of Stockcharts.com. The marks are ours, added for teaching.'

OUR = 'The numbers are invented for teaching.'


def slides(S):
    """S is the tuple of approved sample slides; this returns the 8.1 slides for rows 10 to 56."""
    return (
        # ---- row 10: an overlay is a barrier
        Content(
            notes=('Lim says an overlay acts as a barrier; Chapter 2 gave us the idea.', 'Gold 1 the line at 50.00, red 2 the stall under it.'),
            origin='Lim (2016), p. 235; Chapter 2, "Until a level is breached, nothing has happened". ' + OUR,
            title='An overlay is a barrier the price runs into',
            lines=("Lim says an overlay indicator acts as a barrier to price, that is, as support or resistance (p. 235). Chapter 2 gave us the idea: until a level is breached, nothing has happened. On our chart price climbs to a line at 50.00 [1] and stalls under it [2].",),
        ),
        chart('ob', 'I', 'An overlay is a barrier the price runs into',
              'Our price climbing to a resistance line at 50.00 and stalling under it three times, at 49.60, 49.70 and 49.50.',
              ('Gold 1 the resistance line at 50.00. Red 2 one of the stalls, 49.70.',), 'FIN1209 teaching chart I. ' + OUR),
        # ---- row 11: an oscillator on top of price
        Content(
            notes=('The warning: an oscillator laid on price is not an overlay.', 'Gold 1 the RSI drawn over price; red 2 the same RSI in its own window.'),
            origin='Lim (2016), p. 236. ' + OUR,
            title='An oscillator drawn on top of price tells us nothing',
            lines=("Lim warns that a window oscillator laid on the price chart is not a meaningful overlay. A MACD or RSI drawn on the price chart itself \"will not interact with price in any meaningful way\" (p. 236); the book gives no further reason. On our chart the RSI is drawn over price on the left [1] and sits in its own window on the right [2].",),
        ),
        chart('op', 'J', 'An oscillator drawn on top of price tells us nothing',
              'Our price and an RSI drawn together on one scale on the left, and the same RSI in its own window under the price on the right.',
              ('Gold 1 the RSI laid over the price; red 2 the same RSI in its own window.',), 'FIN1209 teaching chart J. ' + OUR),
        # ---- row 12: an overlay on an oscillator
        Content(
            notes=('The reverse works: an overlay on an oscillator is a valid barrier.', 'Gold 1 the band, red 2 the touch of its lower edge.'),
            origin='Lim (2016), p. 236. ' + OUR,
            title='An overlay drawn on an oscillator does work',
            lines=("The reverse is fine: an overlay drawn on a window oscillator is a valid barrier for the oscillator. Lim's example is a Bollinger band on an RSI, which marks overbought and oversold levels in the RSI (p. 236); this chapter does not say how the band is built. On our chart a band surrounds an RSI [1] and the RSI finds support at its lower edge [2].",),
        ),
        chart('ovo', 'K', 'An overlay drawn on an oscillator does work',
              'Our RSI with a band drawn around it, touching the lower edge of the band at 31 and again at 26.',
              ('Gold 1 the band; red 2 a touch of its lower edge.',), 'FIN1209 teaching chart K. ' + OUR),
        # ---- row 13: four kinds
        Content(
            notes=('Name the four kinds together, then one slide each.',),
            origin='Lim (2016), p. 236. The chart on the next slide is ours.',
            title='Four kinds of overlay, side by side',
            lines=("The oscillators we just met have a window of their own. Overlays do not, and Lim sorts them into four kinds by how they forecast a barrier (p. 236): numerically based, horizontally based, geometrically based and algorithmically based.",
                   "Each kind gets a slide and a chart of its own next. Lim's flow chart draws all four together a little later."),
            accent='Four kinds: a formula, a level, a line, a rule about bars.',
        ),
        Content(
            notes=('One tiny sketch of each kind.',),
            origin='Lim (2016), p. 236. The chart is ours.',
            title='Here are the four kinds in one small sketch each',
            lines=("In our sketch the numerically based overlay is a target from a formula, with the points A, B and C [1], the horizontally based one a level from the past, a prior peak [2], the geometrically based one a sloping line [3] and the algorithmically based one a high over a few bars [4].",),
        ),
        chart('four', 'AB', 'Here are the four kinds in one small sketch each',
              'Four small sketches of ours side by side: a target line from a formula, a flat level, a sloping line and the high of a few bars.',
              ('Gold 1 the formula target, red 2 the flat level, blue 3 the sloping line, purple 4 the high of a few bars.',), 'FIN1209 teaching chart AB. ' + OUR),
        # ---- rows 14 and 15: numerical
        Content(
            notes=('Numerically based: a formula.',),
            origin='Lim (2016), p. 236. The chart is on the next slide and is ours.',
            title='Numerically based overlays are worked out from a formula',
            lines=("A numerically based overlay forecasts a future price barrier mathematically, from a formula (p. 236).",),
            accent='If you can calculate the level, it is numerically based.',
        ),
        Content(
            notes=('Lim gives the formula but not the numbers; the numbers are ours.', 'Gold 1 A, red 2 B, blue 3 C, purple 4 the target.'),
            origin='Lim (2016), p. 236. ' + OUR,
            title='A Fibonacci target is the one formula Lim gives',
            lines=("Lim's example is a Fibonacci upside target from a 161.8 percent expansion of the range AB, measured from C: target = C + (1.618 x AB) (p. 236). He gives only the letters and does not say which points A, B and C are; we take A as the low, B as the high and C as the pullback low. On our chart A is 40.00 [1], B is 50.00 [2], so AB is 10.00, and C is 46.00 [3]. The target is 46.00 + 16.18 = 62.18 [4]. Lim adds that a Fibonacci level, once worked out, may also be classed as horizontally based, which is how Chapter 3 listed it; a moving average may not (p. 236). Here we keep it numerically based, because it comes from a formula.",),
        ),
        chart('fib', 'L', 'A Fibonacci target is the one formula Lim gives',
              'Our price from A at 40.00 up to B at 50.00, back to C at 46.00, and a target line at 62.18.',
              ('A 40.00 gold, B 50.00 red, C 46.00 blue, the target 62.18 purple.',), 'FIN1209 teaching chart L. ' + OUR),
        # ---- rows 16 and 17: horizontal
        Content(
            notes=('Horizontally based: levels from the past.',),
            origin='Lim (2016), p. 236. The chart on the next slide is ours.',
            title='Horizontally based overlays are levels from the past',
            lines=("A horizontally based overlay forecasts a barrier from a prior resistance or support level. The forecast does not depend on time, but Lim warns that the level can still be invalidated, especially when it has been breached many times (p. 236).",),
            accent='A level from the past is the same price whatever the day.',
        ),
        Content(
            notes=('Same level on day 4 and day 12.',),
            origin='Lim (2016), p. 236. ' + OUR,
            title='A horizontal level is the same price on any day',
            lines=("Our resistance is 50.00. Price tests it on day 4 [1], reaching 49.60, and again on day 12 [2], reaching 49.70. The level is the same price both times.",),
        ),
        chart('hor', 'M', 'A horizontal level is the same price on any day',
              'Our price testing a resistance line at 50.00 on day 4, at 49.60, and on day 12, at 49.70.',
              ('Gold 1 the test on day 4, red 2 the test on day 12.',), 'FIN1209 teaching chart M. ' + OUR),
        # ---- row 18: gap
        Content(
            notes=('Lim calls a gap a window; we say gap.', 'Gold 1 the gap, red 2 the later hold.'),
            origin='Lim (2016), p. 236; Chapter 3, "Gap". ' + OUR,
            title='A gap is also a horizontal overlay',
            lines=("Lim also lists price gaps, which he calls rising and falling windows, as horizontal overlays (p. 236). Here window means gap, not the window an oscillator sits in, so we say gap. Chapter 3 taught that this kind of gap is called a window. On our chart there is a gap between a high of 48.40 and a low of 49.40 [1], and later price comes back to its top edge and holds [2].",),
        ),
        chart('gap', 'N', 'A gap is also a horizontal overlay',
              'Our bars with a gap between a high of 48.40 and a low of 49.40, and a later bar holding at the top of the gap.',
              ('Gold 1 the gap from 48.40 to 49.40, red 2 the later bar holding at 49.40.',), 'FIN1209 teaching chart N. ' + OUR),
        # ---- rows 19 and 20: geometric
        Content(
            notes=('Geometrically based: lines drawn from peaks and troughs.',),
            origin='Lim (2016), p. 236; Chapter 5, trendlines. The chart on the next slide is ours.',
            title='Geometrically based overlays are lines drawn from peaks and troughs',
            lines=("A geometrically based overlay is a diagonal line, such as a trendline, drawn from peaks and troughs (p. 236). Chapter 5 taught the trendline. Because the line slopes, the barrier it forecasts depends on when price tests it.",),
        ),
        Content(
            notes=('The line is a different price on day 10 and day 20.',),
            origin='Lim (2016), p. 236. ' + OUR,
            title='A trendline is a different price on a different day',
            lines=("Our trendline rises 1.00 a day from 40.00. Price tests it on day 10 [1], when the line is at 50.00, and again on day 20 [2], when it is at 60.00.",),
        ),
        chart('trl', 'O', 'A trendline is a different price on a different day',
              'Our rising trendline, 50.00 on day 10 and 60.00 on day 20, with price testing it on both days.',
              ('Gold 1 the test on day 10, red 2 the test on day 20.',), 'FIN1209 teaching chart O. ' + OUR),
        # ---- rows 21 and 22: algorithmic
        Content(
            notes=('Algorithmically based: a rule about a sequence of bars.',),
            origin='Lim (2016), p. 236. The chart on the next slide is ours.',
            title='Algorithmically based overlays follow a rule about bars',
            lines=("An algorithmically based overlay forecasts a barrier or breakout level from a specific sequence of bar or candlestick action. Lim names two-bar breakouts, Guppy's count back line and DeMark's TD sequential (p. 236); we only name them.",),
        ),
        Content(
            notes=('Lim\'s own example is the five-day high.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='A five-day high is one such rule',
            lines=("Lim's own example is to buy at the breach of a five-day high (p. 237). On our chart the five highs are 51, 52, 51, 53 and 52, so the five-day high is 53.00 [1]. A sixth bar then trades through it, up to 53.60 [2].",),
        ),
        chart('fd', 'P', 'A five-day high is one such rule',
              'Our five bars with highs of 51, 52, 51, 53 and 52, a line at the five-day high of 53.00 and a sixth bar reaching 53.60.',
              ('Gold 1 the five-day high at 53.00, red 2 the breach at 53.60.',), 'FIN1209 teaching chart P. ' + OUR),
        # ---- rows 23 and 24: Check 1
        CourseCheck(
            notes=('Both answers come from the overlay slides before.',),
            origin='Questions are ours, answerable from the overlay slides before; Lim (2016), p. 236.',
            label='The four kinds of overlay',
            questions=(
                Question(stem='Which kind of overlay forecasts a barrier from a formula?',
                         options=('Horizontally based', 'Numerically based', 'Geometrically based', 'Algorithmically based'), answer='B',
                         reason='A numerically based overlay forecasts price barriers mathematically; Lim\'s example is the Fibonacci target, C + (1.618 x AB) (p. 236).'),
                Question(stem='A trendline gives a different price on a different day. Which kind of overlay is it?',
                         options=('Numerically based', 'Horizontally based', 'Algorithmically based', 'Geometrically based'), answer='D',
                         reason='A trendline is a geometrically based overlay: it is a sloping line, so the barrier depends on when price tests it (p. 236).'),
            ),
        ),
        # ---- rows 25 and 26: Figure 8.2
        WidePair(
            notes=('Gold 1 bounded, red 2 semi bounded, blue 3 fully unbounded. The names in the lists are Lim\'s.',),
            origin='Lim (2016), p. 238, Figure 8.2. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.2 sorts the window oscillators',
                lines=("Lim's flow chart puts the window oscillators in three boxes: bounded [1], semi bounded [2] and fully unbounded [3], each with his list of examples (p. 238). The text names only two kinds, bounded and unbounded; the semi bounded box holds the unbounded ones that stop at zero (pp. 236 to 237).",),
                accent='We only read the lists for now. The names are Lim\'s.',
            ),
            picture=FIG_8_2_LEFT,
            text_w=4.4,
        ),
        WidePair(
            notes=('Numerical, geometric, algorithmic, horizontal. The scale labels come in a few slides.',),
            origin='Lim (2016), p. 238, Figure 8.2. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 8.2 sorts the overlays',
                lines=("The overlays are in four boxes: numerically based [1], geometrically based [2], algorithmically based [3] and horizontally based [4], each with his list (p. 238). Beside each box Lim writes scale invariant or scale sensitive; we meet those words a few slides on. First the oscillator side, in detail.",),
            ),
            picture=FIG_8_2_RIGHT,
            text_w=4.4,
        ),
        # ---- rows 27 and 28: bounded
        Content(
            notes=('Bounded: 0 to 100 percent.',),
            origin='Lim (2016), p. 236. The chart on the next slide is ours.',
            title='A bounded oscillator stays between 0 and 100 percent',
            lines=("A bounded oscillator's readings run from 0 to 100 percent; Lim says the oscillator has been normalized (p. 236). The RSI and the stochastic from our list are bounded; the second class builds them.",
                   "The advantage is that the same scale lets us compare relative overextension, that is, overbought and oversold, between different stocks or markets over the same number of periods (p. 236)."),
            accent='Same scale, so two stocks can be compared.',
        ),
        Content(
            notes=('Gold 1 stock A at 82, red 2 stock B at 64.',),
            origin='Lim (2016), p. 236. ' + OUR,
            title='Here are two stocks on the same 0 to 100 scale',
            lines=("On our chart stock A ends at 82 [1] and stock B at 64 [2], on the same scale over the same number of periods, so we can say stock A is the more overextended.",),
        ),
        chart('cmp', 'Q', 'Here are two stocks on the same 0 to 100 scale',
              'Two of our stocks on one 0 to 100 scale, ending at 82 and at 64.',
              ('Gold 1 stock A at 82, red 2 stock B at 64.',), 'FIN1209 teaching chart Q. ' + OUR),
        # ---- row 29: strong trend
        Content(
            notes=('The disadvantage of a bounded oscillator.', 'Box 1 the ten readings above 80; red 2 the steady rise in price.'),
            origin='Lim (2016), p. 237. ' + OUR,
            title='In a strong trend a bounded oscillator stays at the top',
            lines=("The disadvantage is that in a strong trend the readings tend to stay overbought or oversold for long, which tells us little more than that a strong trend is in effect (pp. 236 to 237). On our chart the oscillator sits above 80 for ten readings in a row [1] while price rises steadily [2].",),
        ),
        chart('stuck', 'R', 'In a strong trend a bounded oscillator stays at the top',
              'Our steadily rising price with a bounded oscillator under it staying above 80 for ten readings in a row.',
              ('Gold 1 the ten readings above 80, red 2 the steady rise in price.',), 'FIN1209 teaching chart R. ' + OUR),
        # ---- rows 30 to 32: unbounded
        Content(
            notes=('Unbounded: no top or bottom.',),
            origin='Lim (2016), p. 237. The chart on the next slide is ours.',
            title='An unbounded oscillator has no top or bottom',
            lines=("An unbounded oscillator has no upper or lower limit (p. 237). The MACD, the ROC and the CCI from our list are unbounded.",
                   "The advantage is that it gives historical levels of overbought and oversold, specific to one stock or market and one timeframe (p. 237)."),
        ),
        Content(
            notes=('Three peaks at about the same height.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='Its overbought level comes from its own history',
            lines=("On our chart the oscillator turned down at 3.9 [1], at 3.8 [2] and at 4.0 [3]. Past peaks at about the same height give a historical overbought level, near 3.9. Lim says such levels are specific to a particular stock or market at a selected timeframe (p. 237).",),
        ),
        chart('unb', 'S', 'Its overbought level comes from its own history',
              'Our unbounded oscillator with three peaks at 3.9, 3.8 and 4.0 and a historical level drawn at 3.9.',
              ('Gold 1, red 2 and blue 3 the three peaks near 3.9.',), 'FIN1209 teaching chart S. ' + OUR),
        Content(
            notes=('Be careful comparing unbounded oscillators between stocks.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='Be careful comparing unbounded oscillators between stocks',
            lines=("Lim adds a care: because the levels are specific to one stock or market, take care when comparing the degree of overextension between different stocks or markets (p. 237). Our stock A peaks at 4.0 [1] and our stock B at 0.8 [2], yet the two lines have the same shape. So stock A at 4.0 is no more overextended than stock B at 0.8. Read each stock against its own history, never against another stock's numbers. Compare the bounded case two slides back, where the same scale made comparison fair.",),
        ),
        chart('unb2', 'T', 'Be careful comparing unbounded oscillators between stocks',
              'Two of our unbounded oscillators with the same shape, one peaking at 4.0 and one at 0.8.',
              ('Gold 1 stock A\'s peak, 4.0; red 2 stock B\'s peak, 0.8.',), 'FIN1209 teaching chart T. ' + OUR),
        # ---- row 33: semi bounded
        Content(
            notes=('Semi bounded: a floor at zero.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='Some unbounded oscillators stop at zero',
            lines=("Some unbounded oscillators do have a lower limit of zero: Lim names volume, ADX, Bollinger Bandwidth and ATR, and calls them semi bounded (p. 237). Our volume-like line dips to 0.3 [1] but cannot go below the zero floor [2].",),
        ),
        chart('semi', 'U', 'Some unbounded oscillators stop at zero',
              'Our volume-like oscillator with a floor at zero and a low of 0.3.',
              ('Gold 1 a low of 0.3, red 2 the zero floor.',), 'FIN1209 teaching chart U. ' + OUR),
        # ---- rows 34 and 35: normalization
        Content(
            notes=('Quote both of Lim\'s sentences and say the book does not reconcile them.',),
            origin='Lim (2016), p. 237. The chart on the next slide is ours.',
            title='Normalization can turn one kind into the other',
            lines=("Lim says an unbounded oscillator \"may sometimes\" be converted into a bounded one by normalization, which confines its readings between 0 and 100 percent. In the next sentence he says normalization \"will always\" convert a point-based oscillator such as the MACD, the MOM, the CCI, the ATR or the ADX into a percentage scaled one (p. 237). The book does not say when it fails. Point-based means the readings are in price points, not percent; Lim does not define it, so that reading is ours. We read the two sentences together: the oscillators he names can always be rescaled, and he does not name any that cannot.",),
        ),
        Content(
            notes=('Our own simple rescaling, once.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='Here is one set of readings rescaled to 0 to 100',
            lines=("Lim gives no method here, so this is our own simple rescaling. The readings run from -5 to 7 points. Our rescaling takes each reading's distance above the lowest and divides by the whole range: (6 - (-5)) / (7 - (-5)) x 100 = 11 / 12 x 100 = 91.7. So the reading of 6 [1] becomes 91.7 [2], the lowest, -5, becomes 0 and the highest, 7, becomes 100.",),
        ),
        chart('norm', 'V', 'Here is one set of readings rescaled to 0 to 100',
              'Our readings in points, from minus 5 to 7, and the same readings rescaled to a 0 to 100 scale, the 6 becoming 91.7.',
              ('Gold 1 the reading of 6 points, red 2 the same reading rescaled, 91.7.',), 'FIN1209 teaching chart V. ' + OUR),
        # ---- rows 36 and 37: indicators, not oscillators
        Content(
            notes=('Some practitioners say window indicator.',),
            origin='Lim (2016), p. 237; Chapter 6, OBV. The chart on the next slide is ours.',
            title='Some call unbounded oscillators indicators, not oscillators',
            lines=("Some practitioners call unbounded oscillators window indicators rather than oscillators, because an unbounded one need not revert to its central or equilibrium value; its values can rise or fall indefinitely (p. 237). Lim's examples are the cumulative ones, such as the Net Advance Decline Line and the OBV from Chapter 6, which tend to trend. This is a second use of the word. Earlier, indicator meant the whole family, overlays and oscillators together (p. 235). Here some practitioners use it only for unbounded oscillators that trend (p. 237). In this deck indicator keeps the first meaning.",),
        ),
        Content(
            notes=('One line swings around its centre, the other runs on.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='Here are one that oscillates and one that trends',
            lines=("On our chart the line on the left swings around its central value, zero [1], which is what an oscillator does. The running total on the right keeps climbing [2], so many practitioners would call it an indicator instead.",),
        ),
        chart('osc2', 'W', 'Here are one that oscillates and one that trends',
              'A line of ours swinging around zero beside a running total that keeps climbing.',
              ('Gold 1 the line swinging around its centre, red 2 the running total.',), 'FIN1209 teaching chart W. ' + OUR),
        # ---- rows 38 and 39: Check 2
        CourseCheck(
            notes=('Both answers come from the bounded and unbounded slides.',),
            origin='Questions are ours, answerable from the bounded and unbounded slides before; Lim (2016), pp. 236 to 237.',
            label='Bounded and unbounded',
            questions=(
                Question(stem='Why can a bounded oscillator be compared between stocks?',
                         options=('Its readings run on the same 0 to 100 scale', 'It never becomes overbought', 'It uses only volume', 'Its levels come from each stock\'s own history'), answer='A',
                         reason='The same 0 to 100 scale lets us compare overextension between stocks or markets over the same number of periods (p. 236).'),
                Question(stem='In a strong trend, what does a bounded oscillator tend to do?',
                         options=('Fall to zero', 'Stay overbought or oversold for long', 'Cross its equilibrium every day', 'Become unbounded'), answer='B',
                         reason='It tends to remain overbought or oversold for extended periods, which says little more than that a strong trend is in effect (p. 237).'),
            ),
        ),
        # ---- rows 40 to 45: scale
        Content(
            notes=('Scale invariant: unchanged by the scale.',),
            origin='Lim (2016), pp. 237 to 238; Chapter 2, scaling; Chapter 3, "What scaling changes, and what it does not". The chart on the next slide is ours.',
            title='Scaling changes some indicators and not others',
            lines=("Chapter 2 showed an arithmetic (linear) scale and a logarithmic (ratio) scale. Lim says scaling affects only the geometrically based indicators. An indicator that scaling does not change is scale invariant (p. 237), and he counts the numerical, horizontal and algorithmic overlays among them. Scaling does not change window oscillators either, because their values are calculated (p. 237). Chapter 3 named the geometric, numerical and horizontal kinds; the algorithmic kind is new here, and it is scale invariant too. Lim's flow chart of indicators calls the geometric kind scale sensitive.",),
        ),
        Content(
            notes=('The average of 10, 12 and 14 is 12 on either scale.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='A moving average is the same on either scale',
            lines=("A simple moving average is the average of the closing prices of the last N periods, so the scale cannot change it (p. 237). On our chart three closes of 10, 12 and 14 average 12.00 on the arithmetic scale [1] and on the ratio scale [2].",),
        ),
        chart('mas', 'X', 'A moving average is the same on either scale',
              'Our three bars with closes of 10, 12 and 14 drawn on an arithmetic scale and on a ratio scale, the average of 12.00 written on both.',
              ('Gold 1 the average on the arithmetic scale, red 2 the same average on the ratio scale.',), 'FIN1209 teaching chart X. ' + OUR),
        Content(
            notes=('The five-day high and a support level do not move either.',),
            origin='Lim (2016), p. 237. ' + OUR,
            title='A five-day high does not move either',
            lines=("The algorithmic example is also scale invariant: the high prices keep the same values whatever the scale, so the five-day high is still 53.00 (p. 237). A horizontal overlay depends only on the price axis; time is not an element (pp. 237 to 238). Our five bars and the sixth that breaks them give 53.00 on the arithmetic scale [1] and on the ratio scale [2].",),
        ),
        chart('fds', 'Y', 'A five-day high does not move either',
              'Our five bars on an arithmetic scale and on a ratio scale, with the five-day high of 53.00 on both.',
              ('Gold 1 the five-day high on the arithmetic scale, red 2 the same high on the ratio scale.',), 'FIN1209 teaching chart Y. ' + OUR),
        WidePair(
            notes=('Gold 1 the uptrend line, red 2 the early penetration on the ratio scale.',),
            origin='Lim (2016), p. 239, Figure 8.3. The marks are ours, added for teaching.',
            left=Content(
                title='Trendlines are the ones that change',
                lines=("Trendlines are geometrically based, and Lim calls them the only group that is not scale invariant. On his ratio scaled chart the uptrend line [1] is penetrated early [2]; the same line on a linear scale is penetrated later (p. 239).",),
                accent='The linear version is on the next slide.',
            ),
            picture=FIG_8_3_TOP,
            text_w=3.6,
        ),
        WidePair(
            notes=('Same index, linear scale, later penetration.',),
            origin='Lim (2016), p. 239, Figure 8.3. The marks are ours, added for teaching.',
            left=Content(
                title='The same trendline on the linear scale breaks later',
                lines=("Here is the same Nasdaq 100 on a linear scale. Its uptrend line [1] is penetrated late [2]. Lim says the compression that happens at higher prices on a ratio scaled chart changes the angle of every trendline, and ratio scaling produces earlier penetrations (p. 239).",),
            ),
            picture=FIG_8_3_BOT,
            text_w=3.6,
        ),
        Content(
            notes=('The same trendline chart, with the day 10 and day 20 levels.',),
            origin='Lim (2016), p. 238. ' + OUR,
            title='Why a trendline depends on time',
            lines=("Lim says the potential support from an uptrend line depends on when price tests it: the more time has elapsed, the higher the support (pp. 238 to 239). On our chart the line is 50.00 when price tests it on day 10 [1] and 60.00 on day 20 [2].",),
        ),
        chart('trl', 'O', 'Why a trendline depends on time',
              'Our rising trendline, 50.00 on day 10 and 60.00 on day 20, with price testing it on both days.',
              ('Gold 1 day 10, red 2 day 20.',), 'FIN1209 teaching chart O. ' + OUR),
        # ---- rows 46 and 47: Check 3 with Figure 8.3
        StackedFigureCheck(
            notes=('Both answers come from the scale slides.',),
            origin='Questions are ours, answerable from the scale slides before; Lim (2016), pp. 237 to 239.',
            label='Scale and trendlines',
            questions=(
                Question(stem='Which kind of overlay is not scale invariant?',
                         options=('Numerically based', 'Horizontally based', 'Geometrically based', 'Algorithmically based'), answer='C',
                         reason='Trendlines and other geometric overlays are the only ones scaling changes (p. 239).'),
                Question(stem='Why is a simple moving average scale invariant?',
                         options=('It averages N closes, on any scale', 'It is a diagonal line', 'It needs a ratio axis', 'It is a horizontal level'), answer='A',
                         reason='It is the average of N closes, which scaling does not change (p. 237).'),
            ),
            picture=FIG_8_3_TOP,
            text_w=5.3,
        ),
        # ---- rows 48 to 54: static and dynamic
        Content(
            notes=('Static overlays do not move with time.',),
            origin='Lim (2016), p. 239. The chart on the next slide is ours.',
            title='Static overlays do not move with time',
            lines=("A static overlay's forecast does not depend on time. Lim says all the horizontally based and algorithmically based overlays are static, and so are many numerically based ones. The forecast level stays where it is unless it is invalidated and a new forecast is needed (p. 239).",),
        ),
        Content(
            notes=('Both levels stay put for ten days.',),
            origin='Lim (2016), p. 239. ' + OUR,
            title='Here are two static levels staying put for ten days',
            lines=("On our chart a prior resistance at 50.00 [1] and a Fibonacci target at 62.18 [2] are the same price on day 1 and on day 10.",),
        ),
        chart('sta', 'Z', 'Here are two static levels staying put for ten days',
              'Our price over ten days with two levels that do not move, a prior resistance at 50.00 and a Fibonacci target at 62.18.',
              ('Gold 1 the prior resistance, red 2 the Fibonacci target.',), 'FIN1209 teaching chart Z. ' + OUR),
        Content(
            notes=('Lim\'s list of static overlays; names only.',),
            origin='Lim (2016), pp. 239 to 240.',
            title="Lim's list of static overlays",
            lines=("Lim's static overlays are prior support and resistance levels; Fibonacci projection, retracement, extension and expansion levels; Gann Square of Nine and squaring of the high and low projections; Gann's one-third and one-eighth retracements; Floor Trader's Pivot Points; reward-to-risk price targets; Gartley Butterfly projections; Parabolic SAR; Chandelier Exit levels; and horizontal channels (pp. 239 to 240).",),
            accent='We only name these. Pivot points get their own section, 8.7, in the second class.',
        ),
        Content(
            notes=('Dynamic overlays move as time goes by.',),
            origin='Lim (2016), p. 240. The chart on the next slide is ours.',
            title='Dynamic overlays move as time goes by',
            lines=("A dynamic overlay's forecast does depend on time. It includes all the geometrically based overlays and some numerically based ones. The exact level is only known once price tests, or is near, the overlay (p. 240).",),
        ),
        Content(
            notes=('The moving average reads 47.0, 49.0, 51.0.',),
            origin='Lim (2016), p. 240. ' + OUR,
            title='Here are two dynamic levels moving with the days',
            lines=("On our chart a 3-day simple moving average reads 45.17 on day 3 [1], 48.17 on day 6 [2] and 51.17 on day 9 [3]. The trendline, drawn through two troughs of the price line, moves too, reading 45.50, 48.00 and 50.50, so each is a different price on a different day.",),
        ),
        chart('dyn', 'AA', 'Here are two dynamic levels moving with the days',
              'Our price with a 3-day simple moving average reading 45.17, 48.17 and 51.17 on days 3, 6 and 9 and a trendline through two troughs reading 45.50, 48.00 and 50.50.',
              ('Gold 1, red 2 and blue 3 the moving average on days 3, 6 and 9.',), 'FIN1209 teaching chart AA. ' + OUR),
        Content(
            notes=('Lim\'s list of dynamic overlays; names only.',),
            origin='Lim (2016), p. 240.',
            title="Lim's list of dynamic overlays",
            lines=("Lim's dynamic overlays are Bollinger Bands, moving averages, moving average bands, Keltner Bands, STARC Bands, Ichimoku overlays, linear regression bands, Andrew's Pitchfork, trendlines, rising and falling channels, chart patterns and Wolfe Waves (p. 240).",),
            accent='Again we only name them.',
        ),
        Content(
            notes=('Review question 5. The table is on the next slide.',),
            origin='Lim (2016), pp. 236 and 239 to 240. The table on the next slide is ours.',
            title='Which kind goes where',
            lines=("Horizontally based and algorithmically based overlays are static; geometrically based overlays are dynamic; numerically based overlays can be either (pp. 239 to 240). Lim notes that a Fibonacci level may also be classed as horizontally based (p. 236), which is why it is static.",),
        ),
        chart('tbl', 'AS', 'Here are the four kinds sorted into static and dynamic',
              'A table of ours with two columns, static and dynamic, and the four kinds of overlay placed in them, numerically based appearing in both.',
              ('Static: horizontal, algorithmic, and the Fibonacci level. Dynamic: geometric, and the moving average.',), 'FIN1209 teaching chart AS. The table is ours, from Lim\'s lists (pp. 239 to 240).'),
        # ---- rows 55 and 56: Check 4
        CourseCheck(
            notes=('Both answers come from the static and dynamic slides.',),
            origin='Questions are ours, answerable from the static and dynamic slides before; Lim (2016), pp. 239 to 240.',
            label='Static or dynamic',
            questions=(
                Question(stem='Which of these is a dynamic overlay?',
                         options=('A prior resistance level', 'A Fibonacci retracement level', 'A five-day high', 'A moving average'), answer='D',
                         reason='A moving average is dynamic: its level depends on time. The other three are static (pp. 239 to 240).'),
                Question(stem='Which kinds of overlay are all static?',
                         options=('Geometrically based', 'Numerically based', 'Horizontally and algorithmically based', 'Chart patterns'), answer='C',
                         reason='Lim says all the horizontally based and algorithmically based overlays are static (p. 239).'),
            ),
        ),
    )
