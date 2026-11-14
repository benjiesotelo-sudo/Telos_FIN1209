"""Chapter 9, Divergence Analysis: the sample slides for approval.

Only the sample slides exist so far. The full deck is written by hand, part by part, after the
instructor approves the outline and these samples (rule 37: no code generates or drops teaching
text). Each sample is a kind of slide the chapter needs:

  (a) an opener that says what divergence analysis is and why we care, before any number
  (b) a book figure read with numbered marks
  (c) a worked example with possible numbers on our own chart
  (d) two ideas easily confused, each with its own chart
  (e) one check and its answer, the figure on both

Marks on book figures were read off a 0.05 grid of the master figure in ~/.fin1209-figures/chapter-09.
Our own made-up numbers are never marked on a book figure (rule 34).
"""
from deckkit import Chapter, Content, Mark, Question, Section
from chartlayout_chapter09 import (CourseCheck, StackedFigureCheck, WidePair, book_crop,
                                   course_chart, expand_chart_pages)

CREDIT = 'The marks are ours, added for teaching.'

# (b) Figure 9.1: direction from two adjacent peaks, three cases, each in its own third of the figure.
FIGURE_9_1 = book_crop('9.1', (0.0, 0.0, 1.0, 1.0),
    "Figure 9.1: three pairs of adjacent peaks. The second peak is higher than the first, so the direction is up. It is lower, so the direction is down. It is level, so the direction is sideways.",
    marks=(
        Mark(number=1, kind='box', x0=0.16, y0=0.0, x1=0.58, y1=0.15, color='gold', at=(0.64, 0.025), size=0.3),
        Mark(number=2, kind='box', x0=0.16, y0=0.385, x1=0.58, y1=0.525, color='red', at=(0.65, 0.375), size=0.3),
        Mark(number=3, kind='box', x0=0.14, y0=0.735, x1=0.58, y1=0.86, color='blue', at=(0.65, 0.715), size=0.3),
    ))
FIGURE_9_1.origin = 'Lim (2016), p. 270, Figure 9.1. ' + CREDIT

# (e) Figure 9.5, left half: price makes a higher peak while the oscillator makes a lower one.
FIGURE_9_5 = book_crop('9.5', (0.0, 0.0, 0.58, 0.97),
    "Figure 9.5, its left half: price above, with a higher second peak, and the oscillator below it, with a lower second peak. Mark 1 is the pair of price peaks and mark 2 the pair of oscillator peaks.",
    marks=(
        Mark(number=1, kind='box', x0=0.25, y0=0.04, x1=0.52, y1=0.40, color='gold', at=(0.2, 0.06), size=0.3),
        Mark(number=2, kind='box', x0=0.25, y0=0.47, x1=0.52, y1=0.82, color='red', at=(0.2, 0.47), size=0.3),
    ))
FIGURE_9_5.origin = 'Lim (2016), p. 273, Figure 9.5. ' + CREDIT

SAMPLES = Section(
    number=1,
    title='Sample slides for approval',
    short='Chapter 9 samples',
    minutes='',
    covers=('divergence', 'main data series', 'supporting data series', 'confirmation', 'price confirmation'),
    slides=(
        # (a) The opener: what we are talking about and why, before any number, tied to Chapter 8.
        # ---- row 4
        Content(
            notes=('Open by saying what the chapter is: the full story of divergence, which Chapter 8 introduced in four kinds.',
                   'Then show the picture of the claim on the next slide.'),
            origin='Lim (2016), pp. 267 to 268; Chapter 8, "Divergence: when price and the oscillator disagree". The chart on the next slide is ours.',
            title='Divergence: price and an indicator telling different stories',
            lines=("In Chapter 8 you met four kinds of divergence: standard and reverse, bullish and bearish. This chapter is the whole story behind them. Lim says divergence, used with other indicators, is one of the most effective ways of forecasting a reversal or a continuation in price (p. 267).",
                   "The idea is a comparison of two data series. The main data series is usually price, and the supporting data series is usually an oscillator or another indicator (p. 268). We ask whether the two agree. The oldest example is Dow Theory: the Industrials against the Transports (p. 267)."),
            accent='Divergence analysis: does the supporting series agree with price?',
        ),
        # ---- row 5
        Content(
            notes=('Gold 1 the higher price peak, red 2 the lower oscillator peak.', 'The same idea as the first example of Chapter 8; this time with Lim\'s two names on it.'),
            origin='Our own example of what Lim means (p. 268). The numbers are ours.',
            title='Here is a main and a supporting series that disagree',
            lines=("Numbers of ours, made up to show the idea. The main data series, price, makes a higher peak [1] while the supporting data series, an oscillator, makes a lower peak [2]. Price alone looks strong, and the oscillator does not agree. That disagreement is what divergence analysis looks for.",),
        ),
        course_chart('dv',
            notes=('Gold 1 the second price peak, 55.00 after 52.00. Red 2 the second oscillator peak, 61 after 74.',),
            origin='FIN1209 teaching chart A. The numbers are invented for teaching.',
            title='Here is a main and a supporting series that disagree',
            letter='A',
            shows='Our price making a higher second peak, 55.00 after 52.00, with an oscillator window under it making a lower second peak, 61 after 74.',
            tier='core',
            marks=(),
        ),
        # (b) A book figure read with numbered marks.
        # ---- row 23
        WidePair(
            notes=('Gold 1 two peaks, the second higher: up. Red 2 the second lower: down. Blue 3 level: sideways.',
                   'Lim says this two-peak test is used only for the current larger trend at the point of non-confirmation.'),
            origin='Lim (2016), pp. 269 to 271, Figure 9.1. The marks are ours, added for teaching.',
            left=Content(
                title='Direction comes from comparing two adjacent peaks',
                lines=("To say two series disagree we first need each one's direction. Lim's test here compares two adjacent peaks, the next peak against the one before it (p. 270). Higher, as in the first pair [1], means the direction is up. Lower [2] means down. Level [3] means sideways.",
                       "Troughs work the same way (Figure 9.2). Lim uses this two-peak test only to find the current larger trend at the point of non-confirmation (p. 271)."),
                accent='Higher peak: up. Lower peak: down. Equal peaks: sideways.',
            ),
            picture=FIGURE_9_1,
            text_w=4.9,
        ),
        # (c) A worked example on our own chart.
        # ---- row 25
        Content(
            notes=('Same test, our own numbers. Say plainly that the numbers are made up.',),
            origin='Lim (2016), pp. 270, 273 and 291. The numbers are ours, made up for teaching.',
            title="Let's find the direction of each series on our own numbers",
            lines=("Numbers of ours, made up to show the idea. Our price peaks at PHP 52.00 and then at PHP 54.00, so by the adjacent peak test its direction is up [1]. The oscillator beside it peaks at 74 and then at 61, so its direction is down [2].",
                   "One series is going up while the other goes down. Lim calls that non-confirmation (p. 273). A higher price peak against a lower oscillator peak is the standard bearish divergence from Chapter 8 (p. 291)."),
        ),
        course_chart('adj',
            notes=('Gold 1 the price peaks, 52.00 then 54.00: up. Red 2 the oscillator peaks, 74 then 61: down.',),
            origin='FIN1209 teaching chart B. The numbers are invented for teaching.',
            title="Let's find the direction of each series on our own numbers",
            letter='B',
            shows='Our price peaking at 52.00 and then 54.00, direction up, and the oscillator beneath peaking at 74 and then 61, direction down.',
            tier='core',
            marks=(),
        ),
        # The first check: direction, the figure on both slides.
        # ---- rows 27 to 28
        StackedFigureCheck(
            notes=('Both answers come from the slides on the adjacent peak test.',),
            origin='Questions are ours, answerable from the direction slides before; Lim (2016), p. 270.',
            label='Direction from adjacent peaks',
            questions=(
                Question(
                    stem="In the figure, mark 2 is a pair of peaks with a lower second peak. What direction does Lim's test give it?",
                    options=('Down', 'Up', 'Sideways', 'No direction'),
                    answer='A',
                    reason='A lower second peak means the direction is down (p. 270).',
                ),
                Question(
                    stem='Two adjacent peaks are at exactly the same height. What direction is that?',
                    options=('Up', 'Down', 'Sideways', 'Confirmation'),
                    answer='C',
                    reason='Equal peaks mean the direction is sideways, as in mark 3 (p. 270).',
                ),
            ),
            picture=FIGURE_9_1,
            text_w=6.6,
        ),
        # (d) Two look-alikes, each on its own slide with its own chart.
        # ---- row 48
        Content(
            notes=('Two words that sound alike. Take the first alone, then the second.',),
            origin='Lim (2016), p. 273.',
            title='Confirmation and price confirmation are not the same thing',
            lines=("Lim uses both words in a very specific way (p. 273). Confirmation is about the two data series: it says whether the main and the supporting series agree in direction. Price confirmation is about price alone: it says price has broken through some barrier, which proves a setup is working.",
                   "We take them one at a time, each on its own chart."),
            accent='Confirmation: the two series agree. Price confirmation: price breaks a barrier.',
        ),
        # ---- row 49
        Content(
            notes=('Agreement of the two series.',),
            origin='Lim (2016), pp. 273 to 274. The numbers are ours.',
            title='Confirmation: the two series agree',
            lines=("Numbers of ours, made up to show the idea. Price peaks at 52.00 and then at 55.00, direction up [1]. The oscillator peaks at 61 and then at 70, direction up as well [2]. The two agree, so Lim says there is confirmation, which suggests the current larger trend continues (pp. 273 to 274).",),
        ),
        course_chart('cf',
            notes=('Gold 1 the price peaks, 52.00 then 55.00. Red 2 the oscillator peaks, 61 then 70. Both up.',),
            origin='FIN1209 teaching chart C. The numbers are invented for teaching.',
            title='Confirmation: the two series agree',
            letter='C',
            shows='Our price peaking at 52.00 and then 55.00 and the oscillator peaking at 61 and then 70, both directions up.',
            tier='core',
            marks=(),
        ),
        # ---- row 55
        WidePair(
            notes=('Gold 1 the price peaks, the second higher. Red 2 the oscillator peaks, the second lower.',
                   'Lim: non-confirmation implies a potential reversal or weakening of the current larger trend.'),
            origin='Lim (2016), p. 274, Figure 9.5. The marks are ours, added for teaching.',
            left=Content(
                title='Figure 9.5 shows non-confirmation, price against an oscillator',
                lines=("This is the left half of Lim's figure. The price pair of peaks [1] goes up, because the second peak is higher. The oscillator pair [2] goes down, because its second peak is lower. The two series disagree.",
                       "Lim calls that non-confirmation, and says it implies a potential reversal or a weakening of the current larger trend (p. 274)."),
                accent='Non-confirmation: the two series disagree in direction.',
            ),
            picture=FIGURE_9_5,
            text_w=4.9,
        ),
        # ---- row 58
        Content(
            notes=('Price alone breaks the support.',),
            origin='Lim (2016), pp. 323 to 324. The numbers are ours.',
            title='Price confirmation: price itself breaks a barrier',
            lines=("Numbers of ours, made up to show the idea. Take the divergence from the last chart: price peaks at 52.00 and 55.00 while the oscillator peaks at 74 and 61. The trough between the two price peaks, 48.00, is a support [1]. Lim says the divergence is only a signal. Price confirmation is the trigger, and it comes when price alone breaks a significant barrier (p. 323). Here price falls to 46.50, below the support [2]. No indicator can confirm a divergence; only price can (p. 323).",),
        ),
        course_chart('pc',
            notes=('Gold 1 the support at 48.00, the trough between the price peaks. Red 2 price at 46.50, below it.',),
            origin='FIN1209 teaching chart D. The numbers are invented for teaching.',
            title='Price confirmation: price itself breaks a barrier',
            letter='D',
            shows='Our price peaking at 52.00 and 55.00, the support at 48.00 under the trough between them, and price falling to 46.50 below that support, with the oscillator under it peaking at 74 and 61.',
            tier='core',
            marks=(),
        ),
        # (e) One check and its answer on the next slide, the figure on both.
        # ---- rows 59 to 60
        StackedFigureCheck(
            notes=('Both answers come from the slides on direction, confirmation and price confirmation.',),
            origin='Questions are ours, answerable from the slides before; Lim (2016), pp. 273 and 323.',
            label='Confirmation and price confirmation',
            questions=(
                Question(
                    stem='In the figure, price peaks rise and oscillator peaks fall. What does Lim call that?',
                    options=('Confirmation', 'Non-confirmation', 'Price confirmation', 'Sideways direction'),
                    answer='B',
                    reason='One series is going up and the other down, so they disagree. Lim calls that non-confirmation (p. 273).',
                ),
                Question(
                    stem='A setup shows non-confirmation. What proves it is working?',
                    options=('The oscillator turns back up', 'A second indicator agrees', 'The two series move together', 'Price breaks a significant barrier'),
                    answer='D',
                    reason='That is price confirmation: only price, never an indicator, confirms a divergence (p. 323).',
                ),
            ),
            picture=FIGURE_9_5,
            text_w=6.2,
        ),
    ),
)

OBJECTIVES = (
    'Understand the narrow and the broader meanings of divergence and convergence.',
    'Use the concept of confirmation to categorize divergence.',
    'Tell standard, reverse, bullish and bearish divergence apart.',
    'Recognize and forecast the alternation of standard and reverse divergence signals.',
    "Tell George Lane's setups from contemporary reverse divergence.",
    'See what divergence means in terms of wave degrees, cycles and trend referencing.',
    'Apply divergence analysis to the market in an integrated way.',
)

CHAPTER = Chapter(
    course='Technical Analysis in Investment',
    code='FIN1209',
    chapter='Chapter 9',
    title='Divergence Analysis',
    subtitle='Institute of Accounts, Business and Finance  |  Far Eastern University Manila',
    presenter='Benjamin C. Sotelo',
    title_notes=('Chapter 9 is the full story of divergence, which Chapter 8 introduced in four kinds.',
                 'It defines the terms, shows the figures and then looks at examples across markets.'),
    objectives=OBJECTIVES,
    roadmap=('Four class meetings, split at section edges',
             'Definition and direction; confirmation and wave degrees; standard and reverse divergence; price confirmation; examples across markets'),
    sections=(SAMPLES,),
    closing=(),
)

CHAPTER = expand_chart_pages(CHAPTER)
