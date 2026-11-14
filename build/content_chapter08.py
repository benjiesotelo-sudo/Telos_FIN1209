"""Chapter 8, Window Oscillators and Overlay Indicators: the first class (8.1 and 8.2) and the second class (8.3 to 8.8).

Every slide is written by hand in teaching order in slides_a1.py and slides_a2.py, from the
approved outline's the first class rows; nothing here generates, expands or drops teaching text.
The approved sample slides are taken as built from samples_chapter08. The second class is
slides_b1 to slides_b4. CHAPTER_A is the first class alone, CHAPTER_B the second class alone and
CHAPTER the whole chapter, which is what the committed decks are built from.
"""
from dataclasses import replace

from deckkit import Chapter, Content, Section
from chartlayout_chapter08 import expand_chart_pages
import samples_chapter08 as _samples
import slides_a1
import slides_a2
import slides_b1
import slides_b2
import slides_b3
import slides_b4

S = _samples.PART_A.slides
SAMPLE_OPENING = S[0:11]      # rows 1 to 9: opener, chart H, two kinds, Figure 8.1, the oscillator list, zones
SAMPLE_EQUILIBRIUM = S[24:27]  # row 72 (chart B) and row 73 (Figure 8.7)
SAMPLE_SIGNAL = S[27:29]       # row 84 (chart C)
SAMPLE_CHECK_6 = S[29]         # check 6, as built

OPENERS = (
    Content(
        notes=("Four objectives, in Lim's words.", 'Say them plainly; each one is a part of today or of the second class.'),
        origin='Lim (2016), p. 235.',
        title='What this chapter lets you do',
        lines=("Lim's four objectives for Chapter 8 (p. 235): understand why oscillators and indicators matter and how to use them to forecast reversals and breakouts in the market; describe the difference between overlay indicators and window oscillators; identify the types of overlay indicator and understand how chart scaling affects each; and set up multiple timeframe charts to better observe price and indicator action.",),
    ),
    Content(
        notes=('The first class is today; the second class is the next meeting.', 'Say which half each section belongs to.'),
        origin='Lim (2016), pp. 235 to 266.',
        title='The route through Chapter 8',
        lines=("The chapter has two halves for two class meetings. The first class is sections 8.1 and 8.2: what indicators are, the kinds of overlay and oscillator, and eight ways to read an oscillator. The second class is sections 8.3 to 8.8: tuning an oscillator, other timeframes, input data, trading with the trend, the main oscillators one by one, and pivot points.",),
    ),
)

SECTION_1 = Section(
    number=1, title='Defining Indicators and Oscillators', short='8.1 Indicators', minutes='about 70 minutes',
    covers=('indicator', 'overlay', 'window oscillator', 'bounded', 'scale invariant'),
    slides=SAMPLE_OPENING + slides_a1.slides(S), recap=None)
SECTION_2 = Section(
    number=2, title='Eight Ways to Analyze an Oscillator', short='8.2 Eight ways', minutes='about 80 minutes',
    covers=('overbought', 'crossover', 'divergence', 'confirmation', 'signal'),
    slides=slides_a2.slides(S, SAMPLE_EQUILIBRIUM, SAMPLE_SIGNAL, SAMPLE_CHECK_6), recap=None)

SECTION_3 = Section(
    number=3, title='Cycle Period, Multiple Timeframes and Lagging Indicators', short='8.3 Tuning', minutes='about 30 minutes',
    covers=('dominant cycle', 'half cycle', 'multiplying factor', 'leading', 'lagging'),
    slides=slides_b1.slides(S), recap=None)
SECTION_4 = Section(
    number=4, title='Input Data', short='8.4 Input data', minutes='about 20 minutes',
    covers=('StochRSI', 'data drop-off effect'),
    slides=slides_b1.slides_84(), recap=None)
SECTION_6 = Section(
    number=6, title='Window Oscillators', short='8.6 Window oscillators', minutes='about 100 minutes',
    covers=('ROC and MOM', 'MACD', 'ATR', 'stochastic', 'RSI'),
    slides=slides_b2.slides() + _samples.PART_A.slides[11:24] + slides_b3.slides(), recap=None)
SECTION_7 = Section(
    number=7, title='Overlay Indicators', short='8.7 Overlays', minutes='about 30 minutes',
    covers=('confluence', 'pivot points', 'PP, R1 to R4, S1 to S4'),
    slides=slides_b4.slides_87(), recap=None)
SECTION_8 = Section(
    number=8, title='Chapter Summary and Review Questions', short='8.8 Review', minutes='about 10 minutes',
    covers=('chapter summary', 'review questions'),
    slides=slides_b4.slides_88(), recap=None)
SECTION_5 = Section(
    number=5, title='Trend Trading Using Oscillators', short='8.5 Trend trading', minutes='about 10 minutes',
    covers=('larger trend', 'buy signals', 'sell signals'),
    slides=slides_b1.slides_85(), recap=None)

PART_A_SECTIONS = (SECTION_1, SECTION_2)
PART_B_SECTIONS = (SECTION_3, SECTION_4, SECTION_5, SECTION_6, SECTION_7, SECTION_8)


OPENERS_B = (
    replace(OPENERS[0], notes=("Four objectives, in Lim's words.", "Say them plainly; each one is a part of the first class or of today's.")),
    replace(OPENERS[1], notes=("The first class was 8.1 and 8.2; today, the second class, is 8.3 to 8.8.", 'Say which half each section belongs to.')),
)


def _chapter(sections, openers=OPENERS):
    return expand_chart_pages(Chapter(
        course='Technical Analysis in Investment',
        code='FIN1209',
        chapter='Chapter 8',
        title='Window Oscillators and Overlay Indicators',
        subtitle='Institute of Accounts, Business and Finance  |  Far Eastern University Manila',
        presenter='Benjamin C. Sotelo',
        title_notes=('Chapter 8 is where the oscillators used since Chapter 4 are finally taught.',
                     'The first class reads them and classifies indicators; the second class builds them one by one.'),
        objectives=OPENERS[0].lines,
        roadmap=OPENERS[1].lines,
        openers=openers,
        sections=sections,
        closing=(),
    ))


CHAPTER_A = _chapter(PART_A_SECTIONS)
CHAPTER_B = _chapter(PART_B_SECTIONS, OPENERS_B)
CHAPTER = _chapter(PART_A_SECTIONS + PART_B_SECTIONS)
