"""Chapter 4 teaching charts for FIN1209, as plain data.

Eighteen charts. This file carries no drawing code: the two forms it uses,
annotated and gallery, live in build/chartkit.py, which knows nothing about
any chapter, and every entry below is data handed to one of them.

Why so many, when Chapter 3 drew six. Chapter 4 has 32 figures, and every
one of them is placed in the deck. But the book's figures are bunched: its
section 4.1 describes who buys and who sells in each phase, why tops are
shorter than bottoms and what a consolidation looks like on a chart, over
three pages with no figure at all, and section 4.2 lists seventeen chart
patterns by name without drawing most of them. The first build of this
chapter left those slides as text and the instructor could not teach from
them. So a chart is drawn here wherever the book makes a point in words
that none of its own figures shows:

  * **A** one line through accumulation, the trend, distribution and the
    trend down, which the book states as a list.
  * **B** one consolidation and the two things it can turn out to have been.
  * **C to F** who is on each side in accumulation, in the uptrend, in the
    downtrend and in distribution: the book's four paragraphs on sentiment
    and participation.
  * **G** the three comparisons the book makes between tops and bottoms.
  * **H and I** the technical signs of an accumulation and of a
    distribution, with the volume under each.
  * **J** the three completion levels of Figure 4.4, in pesos.
  * **K** which kind of pattern sits in which phase.
  * **L** a consolidation pattern beside the V reversal that is not one.
  * **M, N and O** the shapes behind the book's lists of intrinsically
    bullish, bearish and neutral patterns.
  * **P** the book's own worked example: one ascending triangle in three
    locations.
  * **Q** where on the market's swing the sentiment indicators are most
    accurate.
  * **R** Sakata's five methods with the book's English for each.

**Teach only what the textbook teaches.** Every label on these charts is a
statement the book's Chapter 4 makes. The one place a chart goes past
Chapter 4 is the three galleries, M, N and O: Chapter 4 names the patterns
and draws only some of them, on its real charts, and Chapter 13 of the same
book is where each is described. The sketches are drawn from Chapter 13's
own one line descriptions and from nothing else, each gallery says so in
its footnote, and no check rests on a shape. Diamond formations get no
sketch, because the book describes them only as needing four trendlines.

**The data is invented.** We hold no market data licence. Every series
comes from chartkit.walk() with a fixed seed, offline and reproducible, and
every chart carries the credit line deckkit.chart_credit() prints under it.
The pesos on Chart J are the worked example on the slide beside it.
"""

from __future__ import annotations

import math

import chartkit as ck
from chartkit import Box, Bracket, ChartArt, Note, Sketch, Span, Stroke

# Every chart sits in the picture column of a Pair. Beside a teaching slide
# the text column is 5.4in wide; beside a term it is 5.8in, because a formal
# definition needs the room, and the picture column starts lower. These two
# widths are CHART_W and TERM_CHART_W in content_chapter04.py.
PAIR = ck.pair_size(5.4)
TERM = ck.pair_size(5.8, term=True)

INVENTED = "Invented prices."


def _line(pivots, seed, noise=0.004, wobble=0.05):
    return ck.walk(tuple(pivots), seed=seed, noise=noise, wobble=wobble)


def _shaped(n, shape, seed, jitter=0.22):
    """Volume bars that follow a shape given as (index, level) knots."""
    import random
    rng = random.Random(seed)
    out = []
    for i in range(n):
        for (x0, y0), (x1, y1) in zip(shape[:-1], shape[1:]):
            if x0 <= i <= x1:
                level = y0 + (y1 - y0) * (i - x0) / max(1, x1 - x0)
                break
        out.append(level * rng.uniform(1 - jitter, 1 + jitter))
    return out


# --------------------------------------------------------------------------
# Chart A. One line, the three phases.
# --------------------------------------------------------------------------

A_SERIES = _line(
    ((0, 42), (5, 44), (10, 41), (15, 44), (20, 41.5), (25, 44), (30, 42),
     (40, 52), (44, 49.5), (54, 62), (58, 59.5), (66, 70),
     (70, 73.5), (74, 69), (78, 74), (82, 69.5), (86, 73), (90, 69.5),
     (98, 58), (101, 60.5), (110, 48), (113, 50), (120, 41)),
    seed=401)

# --------------------------------------------------------------------------
# Chart B. One consolidation, two outcomes.
# --------------------------------------------------------------------------

B_SERIES = _line(
    ((0, 42), (6, 44), (12, 40.5), (18, 44), (24, 40.2), (30, 43.8),
     (36, 40.4), (42, 44), (48, 42)),
    seed=409)

# --------------------------------------------------------------------------
# Charts C to F. Who is on each side, phase by phase.
# --------------------------------------------------------------------------

C_SERIES = _line(
    ((0, 80), (6, 74), (8, 76), (18, 41), (22, 46.5), (28, 42.5), (34, 46),
     (40, 42.8), (46, 46.2), (52, 43), (58, 46), (64, 43.2), (70, 46),
     (76, 52), (79, 50.5), (86, 58)),
    seed=419)

D_SERIES = _line(
    ((0, 42), (4, 44), (8, 41.5), (12, 44), (18, 50), (21, 48), (30, 58),
     (34, 55.5), (44, 67), (48, 63.5), (58, 77), (62, 73), (72, 88),
     (75, 85.5), (84, 97)),
    seed=421)

E_SERIES = _line(
    ((0, 90), (4, 87), (8, 91), (12, 87), (16, 90), (22, 80), (25, 82.5),
     (32, 70), (35, 72.5), (42, 60), (45, 62), (52, 49), (55, 51), (62, 40)),
    seed=431)

F_SERIES = _line(
    ((0, 42), (6, 50), (8, 48), (18, 86), (22, 76.5), (27, 84), (32, 76),
     (37, 85), (42, 76.5), (47, 84), (52, 77), (58, 68), (61, 70.5),
     (68, 60)),
    seed=433, noise=0.006)

# --------------------------------------------------------------------------
# Chart G. Tops are shorter and rougher than bottoms.
# --------------------------------------------------------------------------

G_SERIES = _line(
    ((0, 43), (6, 44.5), (12, 42), (18, 44.5), (24, 42.2), (30, 44.6),
     (36, 42.2), (42, 44.5), (48, 42.5), (54, 45),
     (66, 56), (70, 53.5), (82, 67), (86, 64), (98, 78),
     (101, 86), (104, 75), (108, 87), (112, 75.5), (116, 86), (120, 76),
     (128, 62), (130, 65), (140, 44)),
    seed=439)

# --------------------------------------------------------------------------
# Charts H and I. The technical signs of a consolidation, with its volume.
# --------------------------------------------------------------------------

H_SERIES = _line(
    ((0, 52), (8, 40), (20, 60), (26, 57), (30, 61), (42, 41.5), (48, 47),
     (54, 42), (60, 47.2), (66, 42.6), (72, 47), (78, 43.2), (84, 47.2),
     (90, 44), (95, 47.5), (100, 53), (103, 51.5), (110, 60)),
    seed=443)
H_VOLUME = _shaped(
    111, ((0, 60), (8, 95), (14, 60), (30, 55), (42, 150), (50, 105),
          (70, 62), (93, 28), (96, 150), (100, 165), (110, 120)), seed=449)

I_SERIES = _line(
    ((0, 62), (8, 90), (16, 72), (22, 74), (40, 82), (44, 79.5), (54, 89.5),
     (58, 80), (63, 89), (68, 80.5), (73, 88.4), (78, 81), (83, 87.6),
     (87, 82), (92, 75), (95, 77), (102, 64)),
    seed=457, noise=0.006)
I_VOLUME = _shaped(
    103, ((0, 60), (8, 100), (16, 60), (40, 70), (54, 150), (60, 110),
          (72, 70), (86, 30), (88, 150), (92, 165), (102, 120)), seed=461)

# --------------------------------------------------------------------------
# Chart J. When a consolidation is over, in pesos.
# --------------------------------------------------------------------------

J_SERIES = _line(
    ((0, 37), (10, 44), (15, 40), (20, 44), (25, 40), (30, 44), (35, 40),
     (40, 44), (45, 40), (52, 45.2), (54, 44.6), (62, 48)),
    seed=463, noise=0.0015, wobble=0.02)

# --------------------------------------------------------------------------
# Chart K. Which kind of pattern sits in which phase.
# --------------------------------------------------------------------------

K_SERIES = _line(
    ((0, 70), (10, 46), (14, 50), (18, 44.5), (22, 50), (26, 45), (30, 50.5),
     (42, 62), (45, 59.5), (48, 62), (51, 60), (54, 62.4),
     (66, 76), (70, 80), (74, 75.5), (78, 80.5), (82, 75.5), (86, 80),
     (96, 62)),
    seed=467)

# --------------------------------------------------------------------------
# Chart L. A consolidation pattern, and the V reversal that is not one.
# --------------------------------------------------------------------------

L_SERIES = _line(
    ((0, 55), (5, 59), (10, 53), (15, 59), (20, 53.2), (25, 58.8),
     (30, 53), (35, 59), (40, 55),
     (46, 57), (60, 34), (74, 57), (78, 56)),
    seed=479, noise=0.003)

# --------------------------------------------------------------------------
# Charts M, N and O. The shapes behind the book's three lists.
#
# Every sketch is drawn from the one line description in the book's
# Chapter 13 and from nothing else:
#
#   head and shoulders   a peak, a higher peak, a lower peak, and a neckline
#                        through the troughs on either side of the head
#   double top/bottom    a retest of a prior resistance or support level
#   symmetrical triangle successively lower peaks and higher troughs
#   ascending triangle   successively higher troughs with equal peaks
#   descending triangle  successively lower peaks with equal troughs
#   broadening           successively higher peaks and lower troughs
#   flag                 a parallelogram sloping slightly against the trend,
#                        preceded by a pole
#   pennant              a small symmetrical triangle, preceded by a pole
#   wedge                slants up or down, both trendlines pointing the
#                        same way and converging
#   cup and handle       a rounding bottom with a handle
#   channel              price contained between two parallel lines
#   island top           preceded by an upside gap, followed by a downside gap
# --------------------------------------------------------------------------


def _arc(x0, x1, y_edge, y_mid, n=14):
    """A rounded bottom or top between two x positions."""
    out = []
    for k in range(n + 1):
        t = k / n
        out.append((x0 + (x1 - x0) * t,
                    y_edge + (y_mid - y_edge) * math.sin(math.pi * t)))
    return tuple(out)


def _mirror(sketch: Sketch, name: str, note: str = "") -> Sketch:
    """The same shape upside down: the bearish twin of a bullish pattern."""
    flip = lambda pts: tuple((x, -y) for x, y in pts)
    return Sketch(name=name, note=note, points=flip(sketch.points),
                  sides=tuple(flip(side) for side in sketch.sides),
                  breaks=sketch.breaks)


M_PENNANT = Sketch(
    name="Bullish pennant",
    points=((0, 0), (4, 8), (5, 6.2), (6, 7.7), (7, 6.5), (8, 7.4), (9, 6.8),
            (10, 7.2), (13, 12)),
    sides=(((4, 8), (10, 7.25)), ((5, 6.2), (10, 6.95))),
)
M_FLAG = Sketch(
    name="Bullish flag",
    points=((0, 0), (4, 8), (5, 6.6), (6, 7.6), (7, 6.2), (8, 7.2), (9, 5.8),
            (10, 6.8), (13, 12)),
    sides=(((4, 8), (10, 6.8)), ((5, 6.6), (9, 5.8))),
)
M_ASCENDING = Sketch(
    name="Ascending triangle",
    points=((0, 2), (2, 8), (4, 3.5), (6, 8), (8, 5), (10, 8), (11.5, 6.6),
            (12.5, 8), (15, 11.5)),
    sides=(((2, 8), (12.5, 8)), ((4, 3.5), (12.5, 7.3))),
)
M_INVERTED_HS = Sketch(
    name="Inverted head\nand shoulders",
    points=((0, 10), (2, 5), (4, 8), (6.5, 1), (9, 8), (11, 5), (13, 8),
            (15, 12)),
    sides=(((3, 8), (14, 8)),),
)
M_ROUNDING = Sketch(
    name="Rounding bottom",
    points=((0, 10),) + _arc(1, 12, 9, 1) + ((14, 12),),
)
M_CUP = Sketch(
    name="Cup and handle",
    points=((0, 10),) + _arc(1, 10, 9, 1) + ((11.5, 7), (12.6, 8.6),
                                             (15, 12.5)),
    sides=(((1, 9), (12.6, 9)),),
)
M_WEDGE = Sketch(
    name="Falling wedge",
    points=((0, 12), (2, 6.5), (4, 9.6), (6, 4.2), (8, 6.6), (10, 2.6),
            (11.5, 4.2), (14, 9)),
    sides=(((0, 12), (11.5, 4.2)), ((2, 6.5), (10, 2.6))),
)
M_DOUBLE = Sketch(
    name="Double, triple and\nmultiple bottoms",
    points=((0, 10), (3, 2), (6, 7), (9, 2), (12, 7), (14, 11)),
    sides=(((2, 2), (10, 2)),),
)

BULLISH = (M_PENNANT, M_FLAG, M_ASCENDING, M_INVERTED_HS, M_ROUNDING, M_CUP,
           M_WEDGE, M_DOUBLE)

BEARISH = (
    _mirror(M_PENNANT, "Bearish pennant"),
    _mirror(M_FLAG, "Bearish flag"),
    _mirror(M_ASCENDING, "Descending triangle"),
    _mirror(M_INVERTED_HS, "Standard head\nand shoulders"),
    _mirror(M_ROUNDING, "Rounding top"),
    _mirror(M_WEDGE, "Rising wedge"),
    _mirror(M_DOUBLE, "Double, triple and\nmultiple tops"),
)

NEUTRAL = (
    Sketch(
        name="Symmetrical triangle",
        note="intrinsically neutral",
        points=((0, 5), (2, 10), (4, 1.5), (6, 8.6), (8, 3), (10, 7.2),
                (12, 4.4), (13.5, 6)),
        sides=(((2, 10), (14, 5.8)), ((4, 1.5), (14, 5.4))),
    ),
    Sketch(
        name="Horizontal channel",
        note="intrinsically neutral",
        points=((0, 6), (2, 9), (4, 2), (6, 9), (8, 2), (10, 9), (12, 2),
                (14, 9)),
        sides=(((1, 9), (15, 9)), ((1, 2), (15, 2))),
    ),
    Sketch(
        name="Broadening formation",
        note="neutral, but regarded as a reversal",
        points=((0, 5), (2, 6.4), (4, 4.4), (6, 7.6), (8, 3), (10, 9),
                (12, 1.4), (13.5, 6)),
        sides=(((2, 6.4), (11.5, 9.8)), ((4, 4.4), (13, 0.9))),
    ),
    Sketch(
        name="Island formation",
        note="neutral, but regarded as a reversal",
        points=((0, 1), (2, 3.4), (3, 2.6), (5, 4.6),
                (6, 7.2), (7.5, 8.6), (9, 7.6), (10.5, 8.8), (12, 7.2),
                (13, 4.6), (14.5, 3), (15.5, 3.6), (17, 1)),
        breaks=(4, 9),
    ),
)

SKETCH_NOTE = ("Sketched from the one line descriptions in the book's "
               "Chapter 13, which teaches the shapes.")

# --------------------------------------------------------------------------
# Chart P. One ascending triangle, three locations.
# --------------------------------------------------------------------------

P_SERIES = _line(
    ((0, 44), (6, 30.5), (10, 37), (14, 32.5), (18, 37), (21, 34.6),
     (24, 37), (26, 35.8), (28, 37.2),
     (40, 52), (44, 58), (48, 53), (52, 58), (55, 55.2), (58, 58),
     (60, 56.6), (62, 58.2),
     (74, 73), (78, 80), (82, 74), (86, 80), (89, 76.6), (92, 80),
     (94, 78.4), (96, 80)),
    seed=487, noise=0.002, wobble=0.03)

# --------------------------------------------------------------------------
# Chart Q. Where the sentiment indicators are most accurate.
# --------------------------------------------------------------------------

Q_SERIES = [60 + 22 * math.sin(math.pi * (i - 8) / 44) for i in range(97)]

# --------------------------------------------------------------------------
# Chart R. Sakata's five methods, with the book's English for each.
#
# The line is lifted at each of the three gaps, so a gap reads as a gap.
# --------------------------------------------------------------------------

R_SERIES = _line(
    ((0, 26), (4, 12), (8, 20), (12, 12.4), (16, 20), (20, 12.2), (24, 21),
     (25, 25), (33, 44), (36, 40), (38, 42.4), (40, 38), (42, 40), (44, 36.4),
     (45, 40.5), (53, 60), (56, 56), (58, 58.4), (60, 54), (62, 56),
     (64, 52.6),
     (65, 56.5), (72, 73), (76, 64.5), (80, 73.4), (84, 64.8), (88, 73),
     (94, 60)),
    seed=491, noise=0.002, wobble=0.02)


# --------------------------------------------------------------------------
# The eighteen charts
# --------------------------------------------------------------------------

CHARTS = (
    ChartArt(
        letter="A",
        draw=ck.annotated,
        kwargs=dict(
            series=A_SERIES,
            size=PAIR,
            boxes=(
                Box(x0=-1, x1=31, lo=39.5, hi=45.5, label="Accumulation",
                    where="below"),
                Box(x0=67, x1=91, lo=67.5, hi=75.5, label="Distribution",
                    where="above"),
            ),
            strokes=(
                Stroke(points=((32, 56), (56, 74)), arrow=True,
                       label="Trending phase", at=0, dx=-6, dy=22),
                Stroke(points=((84, 58), (104, 41)), arrow=True,
                       label="Trending phase", at=1, dx=-10, dy=-12),
            ),
            top=0.16, bottom=0.20,
            footnote=INVENTED + " Two consolidations, and the trend that "
                     "follows each.",
        ),
    ),
    ChartArt(
        letter="B",
        draw=ck.annotated,
        kwargs=dict(
            series=B_SERIES,
            size=PAIR,
            extend=34,
            boxes=(
                Box(x0=-1, x1=49, lo=39.4, hi=44.8, label="Consolidation",
                    where="above"),
            ),
            strokes=(
                Stroke(points=((48, 42), (56, 46), (60, 45), (76, 55)),
                       dashed=True, arrow=True, tone="structure",
                       label="If it rises:\nit was accumulation",
                       at=3, dx=-52, dy=20),
                Stroke(points=((48, 42), (56, 38), (60, 39), (76, 29)),
                       dashed=True, arrow=True, tone="quiet",
                       label="If it declines:\nit was distribution",
                       at=3, dx=-52, dy=-20),
            ),
            notes=(
                Note(x=48, label="Today: nobody\nknows which", dx=-40,
                     dy=-58, notice=True),
            ),
            top=0.42, bottom=0.46,
            footnote=INVENTED + " The dashed paths have not happened yet.",
        ),
    ),
    ChartArt(
        letter="C",
        draw=ck.annotated,
        kwargs=dict(
            series=C_SERIES,
            size=PAIR,
            spans=(Span(x0=18, x1=70, label="Accumulation"),),
            notes=(
                Note(x=12, label="Deep, rapid decline:\nvery negative data,"
                     "\nbearish headlines", dx=22, dy=34),
                Note(x=18, label="Selling climax: the uninformed\nsell at "
                     "any price, the informed buy", dx=18, dy=-30,
                     notice=True),
                Note(x=46, label="The informed keep gathering\nshares, very "
                     "gradually", dx=8, dy=76),
            ),
            top=0.10, bottom=0.36,
            footnote=INVENTED + " The sell-off that ends the downtrend is "
                     "the selling climax.",
        ),
    ),
    ChartArt(
        letter="D",
        draw=ck.annotated,
        kwargs=dict(
            series=D_SERIES,
            size=PAIR,
            spans=(Span(x0=-2, x1=12, label="Accumulation"),),
            notes=(
                Note(x=14, label="1  Technical traders:\nthe upside breakout",
                     dx=22, dy=-22),
                Note(x=30, label="2  Market savvy\ninvestors follow",
                     dx=24, dy=-26),
                Note(x=44, label="3  The public notices.\nShorts cover.",
                     dx=-22, dy=34),
                Note(x=62, label="4  Regret bias:\ndips are bought",
                     dx=14, dy=-32, notice=True),
                Note(x=72, label="5  The herd,\non margin", dx=-30, dy=22),
            ),
            top=0.10, bottom=0.12,
            footnote=INVENTED + " Each group arrives later, and at a higher "
                     "price, than the last.",
        ),
    ),
    ChartArt(
        letter="E",
        draw=ck.annotated,
        kwargs=dict(
            series=E_SERIES,
            size=PAIR,
            spans=(Span(x0=-2, x1=16, label="Distribution"),),
            notes=(
                Note(x=18, label="1  Breakdown from the\ndistribution range",
                     dx=22, dy=24),
                Note(x=32, label="2  The uninformed\nbegin to unload",
                     dx=-22, dy=-30),
                Note(x=42, label="3  Bullish holders\nliquidate", dx=24,
                     dy=26),
                Note(x=52, label="4  Margin limits passed:\ncapital flows "
                     "out", dx=-24, dy=-30, notice=True),
            ),
            top=0.12, bottom=0.14,
            footnote=INVENTED + " The same feedback as the uptrend, running "
                     "downward and faster.",
        ),
    ),
    ChartArt(
        letter="F",
        draw=ck.annotated,
        kwargs=dict(
            series=F_SERIES,
            size=PAIR,
            spans=(Span(x0=18, x1=52, label="Distribution"),),
            notes=(
                Note(x=12, label="Strong, rapid rise:\nvery positive data,"
                     "\nbullish headlines", dx=24, dy=-38),
                Note(x=18, label="Blow-off, or buying climax:\nthe "
                     "uninformed buy at any price,\nthe informed sell",
                     dx=20, dy=24, notice=True),
                Note(x=42, label="The informed keep selling,\nvery gradually",
                     dx=6, dy=-74),
            ),
            top=0.34, bottom=0.10,
            footnote=INVENTED + " The surge that ends the uptrend is the "
                     "blow-off, or buying climax.",
        ),
    ),
    ChartArt(
        letter="G",
        draw=ck.annotated,
        kwargs=dict(
            series=G_SERIES,
            size=PAIR,
            spans=(
                Span(x0=0, x1=54, label="Accumulation\nlonger, less volatile"),
                Span(x0=98, x1=120, label="Distribution\nshorter, more volatile",
                     tone="notice"),
            ),
            strokes=(
                Stroke(points=((56, 40), (76, 40), (96, 40)),
                       tone="structure", label="Uptrend:\nmore prolonged",
                       at=1, dx=0, dy=-17),
                Stroke(points=((56, 38.6), (56, 41.4)), tone="structure"),
                Stroke(points=((96, 38.6), (96, 41.4)), tone="structure"),
                Stroke(points=((122, 40), (140, 40)), tone="structure",
                       label="Downtrend:\nshorter lived", at=1, dx=-1,
                       dy=-17),
                Stroke(points=((122, 38.6), (122, 41.4)), tone="structure"),
                Stroke(points=((140, 38.6), (140, 41.4)), tone="structure"),
            ),
            top=0.08, bottom=0.36,
            footnote=INVENTED + " At higher prices more capital, and more "
                     "unrealized profit, is at risk.",
        ),
    ),
    ChartArt(
        letter="H",
        draw=ck.annotated,
        kwargs=dict(
            series=H_SERIES,
            size=PAIR,
            spans=(Span(x0=42, x1=95, label="Accumulation"),),
            strokes=(
                Stroke(points=((8, 40), (95, 40)), dashed=True, tone="quiet",
                       label="A significant prior bottom", at=0, dx=6,
                       dy=-11),
            ),
            notes=(
                Note(x=36, label="A relatively\nrapid decline", dx=-26,
                     dy=22),
                Note(x=66, label="No lower troughs", dx=-10, dy=58),
            ),
            volume=H_VOLUME,
            volume_label="Volume",
            volume_strokes=(
                Stroke(points=((46, 175), (92, 70)), arrow=True,
                       tone="structure", label="Volume subsides", at=0,
                       dx=-6, dy=12),
            ),
            volume_notes=(
                Note(x=99, y=175, label="Surge on\nthe breakout", dx=-8,
                     dy=9, notice=True, dot=False),
            ),
            top=0.12, bottom=0.22,
            footnote=INVENTED + " The breakout can be to either side; these "
                     "signs are evidence, not proof.",
        ),
    ),
    ChartArt(
        letter="I",
        draw=ck.annotated,
        kwargs=dict(
            series=I_SERIES,
            size=PAIR,
            spans=(Span(x0=54, x1=87, label="Distribution"),),
            strokes=(
                Stroke(points=((8, 90), (87, 90)), dashed=True, tone="quiet",
                       label="A significant prior top", at=0, dx=6, dy=10),
            ),
            notes=(
                Note(x=34, label="A prolonged uptrend", dx=-6, dy=-34),
                Note(x=68, label="No higher peaks", dx=-22, dy=-50),
            ),
            volume=I_VOLUME,
            volume_label="Volume",
            volume_strokes=(
                Stroke(points=((57, 175), (85, 70)), arrow=True,
                       tone="structure", label="Volume\nsubsides", at=0,
                       dx=-22, dy=-2),
            ),
            volume_notes=(
                Note(x=91, y=175, label="Surge on\nthe breakout", dx=-6,
                     dy=9, notice=True, dot=False),
            ),
            top=0.20, bottom=0.14,
            footnote=INVENTED + " A distribution is shorter and more volatile "
                     "than an accumulation.",
        ),
    ),
    ChartArt(
        letter="J",
        draw=ck.annotated,
        kwargs=dict(
            series=J_SERIES,
            size=TERM,
            ylabel="Price (PHP)",
            price_ticks=(40, 44, 48),
            extend=36,
            boxes=(
                Box(x0=9, x1=46, lo=40, hi=44, where="below",
                    label="The range: PHP 40 to 44,\na height of PHP 4"),
                Box(x0=46, x1=68, lo=45.32, hi=46.20),
            ),
            strokes=(
                Stroke(points=((46, 44), (98, 44)), dashed=True,
                       tone="quiet", label="PHP 44: a technical breakout",
                       at=1, dx=-2, dy=-10),
                Stroke(points=((46, 48), (98, 48)), dashed=True,
                       tone="notice",
                       label="44 + 4 = PHP 48: minimum measuring objective",
                       at=1, dx=-2, dy=11),
            ),
            brackets=(
                Bracket(x=72, lo=44, hi=48, label="PHP 4", notice=True),
            ),
            notes=(
                Note(x=46, y=45.76, label="3 to 5 percent above\nthe highest "
                     "peak:\nPHP 45.32 to 46.20", dx=-8, dy=14, dot=False),
            ),
            top=0.30, bottom=0.30,
            footnote=INVENTED + " The range and the target are the worked "
                     "example beside this chart.",
        ),
    ),
    ChartArt(
        letter="K",
        draw=ck.annotated,
        kwargs=dict(
            series=K_SERIES,
            size=PAIR,
            boxes=(
                Box(x0=9, x1=31, lo=43, hi=52, where="below",
                    label="Accumulation:\nreversal patterns"),
                Box(x0=41, x1=55, lo=58.4, hi=63.6, where="below",
                    label="Trend:\ncontinuation patterns", tone="notice"),
                Box(x0=65, x1=87, lo=74, hi=82, where="above",
                    label="Distribution:\nreversal patterns"),
            ),
            top=0.26, bottom=0.30,
            footnote=INVENTED + " The kind of pattern on the chart is "
                     "evidence of the phase.",
        ),
    ),
    ChartArt(
        letter="L",
        draw=ck.annotated,
        kwargs=dict(
            series=L_SERIES,
            size=TERM,
            boxes=(Box(x0=3, x1=37, lo=52.4, hi=59.6, where="above",
                       label="A consolidation pattern"),),
            notes=(
                Note(x=10, label="Confined range,\nno trend component", dx=12,
                     dy=-50),
                Note(x=60, label="A V bottom: no confined range,\nand a "
                     "strong trend component", dx=-78, dy=-24, notice=True),
            ),
            top=0.22, bottom=0.34,
            footnote=INVENTED + " V tops and V bottoms are reversal "
                     "patterns, and not consolidation patterns.",
        ),
    ),
    ChartArt(
        letter="M",
        draw=ck.gallery,
        kwargs=dict(sketches=BULLISH, cols=4, size=PAIR,
                    footnote=SKETCH_NOTE),
    ),
    ChartArt(
        letter="N",
        draw=ck.gallery,
        kwargs=dict(sketches=BEARISH, cols=4, size=PAIR,
                    footnote=SKETCH_NOTE),
    ),
    ChartArt(
        letter="O",
        draw=ck.gallery,
        kwargs=dict(sketches=NEUTRAL, cols=2, size=PAIR,
                    footnote=SKETCH_NOTE + "\nDiamond formations are named "
                             "with these and are not described there."),
    ),
    ChartArt(
        letter="P",
        draw=ck.annotated,
        kwargs=dict(
            series=P_SERIES,
            size=TERM,
            strokes=(
                Stroke(points=((0, 30), (30, 30)), dashed=True, tone="quiet",
                       label="A historically significant bottom", at=0,
                       dx=2, dy=-10),
                Stroke(points=((66, 81), (106, 81)), dashed=True,
                       tone="quiet",
                       label="A historically significant top", at=1,
                       dx=-2, dy=10),
                Stroke(points=((10, 37), (28, 37))),
                Stroke(points=((6, 30.5), (28, 36.6))),
                Stroke(points=((44, 58), (62, 58))),
                Stroke(points=((40, 51.6), (62, 57.6))),
                Stroke(points=((78, 80), (96, 80)), tone="notice"),
                Stroke(points=((74, 72.6), (96, 79.4)), tone="notice"),
            ),
            notes=(
                Note(x=28, y=36, label="At the bottom: intrinsically\nand "
                     "extrinsically bullish", dx=40, dy=-4, dot=False),
                Note(x=44, y=58, label="In the uptrend:\na continuation "
                     "is likelier", dx=-12, dy=32, dot=False),
                Note(x=82, y=75, label="At the top:\nextrinsically\nbearish",
                     dx=10, dy=-56, notice=True, dot=False),
            ),
            extend=10,
            top=0.20, bottom=0.22,
            footnote=INVENTED + " The same ascending triangle three times. "
                     "Only its location changes.",
        ),
    ),
    ChartArt(
        letter="Q",
        draw=ck.annotated,
        kwargs=dict(
            series=Q_SERIES,
            size=PAIR,
            boxes=(
                Box(x0=18, x1=42, lo=74, hi=84, where="above",
                    label="Top: the crowd is extremely bullish",
                    tone="notice"),
                Box(x0=62, x1=86, lo=36, hi=46, where="below",
                    label="Bottom: the crowd is extremely bearish",
                    tone="notice"),
            ),
            notes=(
                Note(x=52, label="Between the extremes the\nindicators say "
                     "less", dx=22, dy=30),
            ),
            top=0.26, bottom=0.26,
            footnote=INVENTED + " Sentiment indicators are most accurate at "
                     "the two extremes.",
        ),
    ),
    ChartArt(
        letter="R",
        draw=ck.annotated,
        kwargs=dict(
            series=R_SERIES,
            size=PAIR,
            breaks=(25, 45, 65),
            boxes=(
                Box(x0=2, x1=22, lo=10.5, hi=22, where="below",
                    label="San Sen, three rivers:\nthe triple bottom"),
                Box(x0=70, x1=90, lo=63, hi=75, where="above",
                    label="San Zan, three mountains:\nthe triple top"),
            ),
            notes=(
                Note(x=49, label="San Pei, three thrusts:\nthe three trending"
                     " phases", dx=-30, dy=50),
                Note(x=40, label="San Poh, three methods:\nthe correction "
                     "after a thrust", dx=26, dy=-40),
                Note(x=65, y=54.5, label="San Ku, three gaps", dx=24, dy=-30,
                     notice=True, dot=False),
            ),
            top=0.24, bottom=0.26,
            footnote=INVENTED + " The line is lifted at each of the three "
                     "gaps.",
        ),
    ),
)
