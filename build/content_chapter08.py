"""Chapter 8, Window Oscillators and Overlay Indicators: Part A (sections 8.1 and 8.2).

Every slide is written by hand in teaching order in slides_a1.py and slides_a2.py, from the
approved outline's Part A rows; nothing here generates, expands or drops teaching text.
The 12 approved sample slides are taken as built from samples_chapter08. Part B (8.3 to 8.8)
is built after Part A is delivered.
"""
from deckkit import Chapter, Content, Section
from chartlayout_chapter08 import expand_chart_pages
import samples_chapter08 as _samples
import slides_a1
import slides_a2

S = _samples.PART_A.slides
SAMPLE_OPENING = S[0:11]      # rows 1 to 9: opener, chart H, two kinds, Figure 8.1, the oscillator list, zones
SAMPLE_EQUILIBRIUM = S[24:27]  # row 72 (chart B) and row 73 (Figure 8.7)
SAMPLE_SIGNAL = S[27:29]       # row 84 (chart C)
SAMPLE_CHECK_6 = S[29]         # check 6, as built

OPENERS = (
    Content(
        notes=("Four objectives, in Lim's words.", 'Say them plainly; each one is a part of today or of Part B.'),
        origin='Lim (2016), p. 235.',
        title='What this chapter lets you do',
        lines=("Lim's four objectives for Chapter 8 (p. 235): understand why oscillators and indicators matter and how to use them to forecast reversals and breakouts in the market; describe the difference between overlay indicators and window oscillators; identify the types of overlay indicator and understand how chart scaling affects each; and set up multiple timeframe charts to better observe price and indicator action.",),
    ),
    Content(
        notes=('Part A is today; Part B is the next meeting.', 'Say which half each section belongs to.'),
        origin='Lim (2016), pp. 235 to 266.',
        title='The route through Chapter 8',
        lines=("The chapter has two halves for two class meetings. Part A is sections 8.1 and 8.2: what indicators are, the kinds of overlay and oscillator, and eight ways to read an oscillator. Part B is sections 8.3 to 8.8: tuning an oscillator, other timeframes, input data, trading with the trend, the main oscillators one by one, and pivot points.",),
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

CHAPTER = Chapter(
    course='Technical Analysis in Investment',
    code='FIN1209',
    chapter='Chapter 8',
    title='Window Oscillators and Overlay Indicators',
    subtitle='Institute of Accounts, Business and Finance  |  Far Eastern University Manila',
    presenter='Benjamin C. Sotelo',
    title_notes=('Chapter 8 is where the oscillators used since Chapter 4 are finally taught.',
                 'Part A reads them and classifies indicators; Part B builds them one by one.'),
    objectives=OPENERS[0].lines,
    roadmap=OPENERS[1].lines,
    openers=OPENERS,
    sections=(SECTION_1, SECTION_2),
    closing=(),
)

CHAPTER = expand_chart_pages(CHAPTER)
