"""FIN1209 Chapter 8 second class run card, as plain data: the clock, the cuts, the floor.

Three pages, the same shape as the first class card. The second class is one meeting of 180 minutes.
The minutes are the outline's rate, 50 slides an hour (1.2 minutes a slide), counted from the deck by
build_plan8.py --part B; no minute is typed here. Slides are named by stable key and resolved against
the deck, so a content change moves this card with it. No check answer is printed: the repository is
public and they live on the answer slide of the teaching edition.
"""
from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table

SESSION = 180
RATE = 1.2   # minutes a slide, from "about 50 slides an hour"


def _clock(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60:02d}"


PARTS = ((3, '8.3  Cycle period, timeframes and lagging'), (4, '8.4  Input data'), (5, '8.5  Trend trading'),
         (6, '8.6  Window oscillators'), (7, '8.7  Overlay indicators and pivot points'), (8, '8.8  Summary and review questions'))


def make(stats):
    """``stats`` has total, opening, parts (section number to slide count), checks."""
    total = stats['total']
    full = round(total * RATE)
    rows, start = [], 0
    for label, n in (('Title, objectives, route', stats['opening']), *((lab, stats['parts'][num]) for num, lab in PARTS)):
        m = round(n * RATE)
        rows.append((label, str(n), str(m), _clock(start)))
        start += m
    rows.append(('Whole of the second class', str(total), str(full), f'ends {_clock(start)}'))
    cut_minutes = round(stats['checks'] * 2 * RATE)
    after = full - cut_minutes
    room = SESSION - full

    clock = Sheet(
        title='Where you should be, minute by minute',
        kicker='Read this before you open the deck',
        footer='The clock',
        blocks=(
            Prose(cue='The honest number', text=(
                f"The second class is {total} slides. At about 50 slides an hour that is **about {full} minutes in a {SESSION} minute meeting**, "
                f"so {room} minutes in hand. The build stops at 150 slides, so this class cannot grow past about {round(150 * RATE)} minutes. "
                "The rate was measured on Chapter 1, where 155 slides took the 180 minutes, so treat the clock as the test.")),
            Table(cue='The clock', title='Minutes per section, and the clock time to start it', full=True, compact=False,
                  headers=('Section', 'Slides', 'Minutes', 'Start at'), align=('l', 'n', 'n', 'n'), rows=tuple(rows),
                  note='Slide counts include each check\'s question and its answer slide, and each section\'s divider.'),
            Flag(kind='rule', cue='At the boundary', title='Check the clock when 8.6 begins',
                 text=("8.6 starts at slide `{s:part:6}` and is the longest section by far. **If you are more than five minutes behind at that slide, take the cut on page 2 "
                       "before you begin 8.6.** Nothing from the book is cut: the cut is only the in-class checks.")),
        ),
    )

    cuts = Sheet(
        title='What to cut, if you must',
        kicker='Only the checks, never the book',
        footer='The cut',
        blocks=(
            Table(cue='The ladder', title='What the cut buys', compact=True,
                  headers=('Cut', 'What comes out', 'Minutes', 'The class runs'), align=('l', 'l', 'n', 'n'),
                  rows=(('None', 'The whole class', '', str(full)),
                        ('1', f'{stats["checks"]} checks and their answers', str(cut_minutes), str(after)),
                        ('2', 'and the review walk becomes assigned reading', str(round((stats['parts'][8] - 3) * RATE)), str(after - round((stats['parts'][8] - 3) * RATE)))),
                  note='Each check is two slides, the question and the answers. No slide that teaches a check\'s answer is cut.'),
            Prose(cue='The cut', text=("**Every check, question slide and answer slide, goes whole.** Each check follows the slides that answer it, "
                                       "so no later slide refers back to one. The student edition has no checks at all. "
                                       "The second cut is the review question walk in 8.8, from slide `{s:slide:Review question 1: overlay and window oscillator}` "
                                       "to the last slide: the questions are answered on slides the class has already seen, so they can be set as reading.")),
            Bullets(cue='Skip these', title='The checks in 8.3 to 8.5', items=(
                'Check 12, slides `{s:check:1}` and `{s:reveal:1}`: the half cycle.',
                'Check 13, slides `{s:check:2}` and `{s:reveal:2}`: timeframes.',
                'Check 14, slides `{s:check:3}` and `{s:reveal:3}`: leading and lagging.',
                'Check 15, slides `{s:check:4}` and `{s:reveal:4}`: the data drop-off effect.',
                'Check 16, slides `{s:check:5}` and `{s:reveal:5}`: trend trading.')),
            Bullets(cue='Skip these', title='The checks in 8.6 and 8.7', items=(
                'Check 17, slides `{s:check:6}` and `{s:reveal:6}`: ROC and MOM.',
                'Check 18, slides `{s:check:7}` and `{s:reveal:7}`: the MACD.',
                'Check 19, slides `{s:check:8}` and `{s:reveal:8}`: the ATR.',
                'Check 20, slides `{s:check:9}` and `{s:reveal:9}`: raw %K.',
                'Check 21, slides `{s:check:10}` and `{s:reveal:10}`: the stochastic.',
                'Check 22, slides `{s:check:11}` and `{s:reveal:11}`: stochastic and RSI together.',
                'Check 23, slides `{s:check:12}` and `{s:reveal:12}`: pivot points.')),
        ),
    )

    floor = Sheet(
        title='The floor, and the answers',
        kicker='Below this, do not go',
        footer='What must stay',
        blocks=(
            Prose(cue='The floor', text=(
                "**All of the teaching slides stay.** Every chart and every Lim figure in this class is the picture of the idea named on the slide "
                "with it, so cutting one leaves an explanation with nothing to show. Where a slide only names an idea, the next slide is its picture.")),
            Bullets(cue='These stay', numbered=True, title='What must not be cut', items=(
                '**Tuning and timeframes**, slides `{s:part:3}` to `{s:end:3}`. Review question 7.',
                '**Input data and trend trading**, slides `{s:part:4}` to `{s:end:5}`.',
                '**The oscillators**, ROC, MOM, MACD and ATR, then the stochastic and the RSI, slides `{s:part:6}` to `{s:end:6}`. Review question 8.',
                '**Overlays and pivot points**, slides `{s:part:7}` to `{s:end:7}`.')),
            Prose(cue='The answers', text=(
                "**This card prints no check answers, on purpose.** The repository this card lives in is public. "
                "The answers to all 12 checks, with the reason for each, are on the answer slide that follows each check in your copy of the deck, "
                "and in the teaching edition only.")),
        ),
    )

    return Notes(course='Technical Analysis in Investment', code='FIN1209', chapter='Chapter 8',
                 title='Window Oscillators and Overlay Indicators, the second class', presenter='Benjamin C. Sotelo, Institute of Accounts, Business and Finance, FEU Manila',
                 doc_kind='run card', plans=(), front=(clock, cuts, floor), parts=(), back=())
