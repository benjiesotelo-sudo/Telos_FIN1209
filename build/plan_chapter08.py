"""FIN1209 Chapter 8 Part A run card, as plain data: the clock, the cuts, the floor.

Three pages, the Chapter 2 shape. Part A is one class meeting of 180 minutes.
The minutes are the outline's rate, 50 slides an hour (1.2 minutes a slide),
counted from the deck by build_plan8.py; no minute is typed here. Slides are
named by stable key and resolved against the deck, so a content change moves
this card with it. No check answer is printed: they live outside the
repository.
"""
from __future__ import annotations

from notekit import Bullets, Flag, Notes, Prose, Sheet, Table

SESSION = 180
RATE = 1.2   # minutes a slide, from "about 50 slides an hour"


def _clock(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60:02d}"


def make(stats):
    """``stats`` has total, opening, part1, part2 (slide counts) and checks."""
    total = stats['total']
    full = round(total * RATE)
    rows, start = [], 0
    for label, n in (('Title, objectives, route', stats['opening']),
                     ('8.1  Defining indicators and oscillators', stats['part1']),
                     ('8.2  Eight ways to analyze an oscillator', stats['part2'])):
        m = round(n * RATE)
        rows.append((label, str(n), str(m), _clock(start)))
        start += m
    rows.append(('Whole of Part A', str(total), str(full), f'ends {_clock(start)}'))
    check_slides = stats['checks'] * 2
    cut_minutes = round(check_slides * RATE)
    after = full - cut_minutes
    room = SESSION - full

    clock = Sheet(
        title='Where you should be, minute by minute',
        kicker='Read this before you open the deck',
        footer='The clock',
        blocks=(
            Prose(cue='The honest number', text=(
                f"Part A is {total} slides. At about 50 slides an hour that is **about {full} minutes in a {SESSION} minute meeting**, "
                f"so {room} minutes in hand. The build stops at 150 slides, so this part cannot grow past about {round(150 * RATE)} minutes. "
                "The rate was measured on Chapter 1, where 155 slides took the 180 minutes, so treat the clock as the test.")),
            Table(cue='The clock', title='Minutes per part, and the clock time to start it', full=True, compact=False,
                  headers=('Part', 'Slides', 'Minutes', 'Start at'), align=('l', 'n', 'n', 'n'), rows=tuple(rows),
                  note='Slide counts include each check\'s question and its answer slide.'),
            Flag(kind='rule', cue='At the boundary', title='Check the clock when 8.2 begins',
                 text=("8.2 starts at slide `{s:part:2}`. **If you are more than five minutes behind at that slide, take the cut on page 2 "
                       "before you begin 8.2.** Nothing from the book is cut: the cut is only the in-class checks.")),
        ),
    )

    cuts = Sheet(
        title='What to cut, if you must',
        kicker='Only the checks, never the book',
        footer='The cut',
        blocks=(
            Table(cue='The ladder', title='What the cut buys', compact=True,
                  headers=('Cut', 'What comes out', 'Minutes', 'Part A runs'), align=('l', 'l', 'n', 'n'),
                  rows=(('None', 'The whole part', '', str(full)),
                        ('1', f'{stats["checks"]} checks and their answers', str(cut_minutes), str(after))),
                  note='Each check is two slides, the question and the answers. No slide that teaches a check\'s answer is cut.'),
            Prose(cue='The cut', text=("**Every check, question slide and answer slide, goes whole.** Each check follows the slides that answer it, "
                                       "so no later slide refers back to one. The student edition has no checks at all.")),
            Bullets(cue='Skip these', title='The checks in 8.1', items=(
                'Check 1, slides `{s:check:1}` and `{s:reveal:1}`: the four kinds of overlay.',
                'Check 2, slides `{s:check:2}` and `{s:reveal:2}`: bounded and unbounded.',
                'Check 3, slides `{s:check:3}` and `{s:reveal:3}`: scale and trendlines.',
                'Check 4, slides `{s:check:4}` and `{s:reveal:4}`: static or dynamic.')),
            Bullets(cue='Skip these', title='The checks in 8.2', items=(
                'Check 5, slides `{s:check:5}` and `{s:reveal:5}`: overbought and oversold.',
                'Check 6, slides `{s:check:6}` and `{s:reveal:6}`: equilibrium crossovers.',
                'Check 7, slides `{s:check:7}` and `{s:reveal:7}`: collinearity.',
                'Check 8, slides `{s:check:8}` and `{s:reveal:8}`: signal line crossovers.',
                'Check 9, slides `{s:check:9}` and `{s:reveal:9}`: divergence.',
                'Check 10, slides `{s:check:10}` and `{s:reveal:10}`: patterns on an oscillator.',
                'Check 11, slides `{s:check:11}` and `{s:reveal:11}`: the eight ways.')),
        ),
    )

    floor = Sheet(
        title='The floor, and the answers',
        kicker='Below this, do not go',
        footer='What must stay',
        blocks=(
            Prose(cue='The floor', text=(
                "**All of the teaching slides stay.** Part A reads Lim's figures and our charts together, and every chart is the picture of the idea "
                "on the slide before it or beside it, so cutting a chart leaves an explanation with nothing to show. Lim's eight review "
                "questions are answered in Part B, which also closes the chapter.")),
            Bullets(cue='These stay', numbered=True, title='What must not be cut', items=(
                '**The kinds of overlay**, slides `{s:part:1}` to `{s:check:1}`. Review questions 1 and 2.',
                '**Bounded, unbounded and scale**, slides `{s:slide:A bounded oscillator stays between 0 and 100 percent}` to `{s:check:3}`. Review questions 3 and 4.',
                '**Static and dynamic**, slides `{s:slide:Static overlays do not move with time}` to `{s:check:4}`. Review question 5.',
                '**The eight ways**, slides `{s:part:2}` to `{s:slide:What you can now do after the first class}`. Review question 6.')),
            Prose(cue='The answers', text=(
                "**This card prints no check answers, on purpose.** The repository this card lives in is public. "
                "The answers to all 11 checks, with the reason for each, are on the answer slide that follows each check in your copy of the deck, "
                "and in the teaching edition only.")),
        ),
    )

    return Notes(course='Technical Analysis in Investment', code='FIN1209', chapter='Chapter 8',
                 title='Window Oscillators and Overlay Indicators, Part A', presenter='Benjamin C. Sotelo, Institute of Accounts, Business and Finance, FEU Manila',
                 doc_kind='run card', plans=(), front=(clock, cuts, floor), parts=(), back=())
