"""FIN1209 Chapter 7 foundation deck.

This scaffold contains the three approved sample ideas in their real teaching
form. The source map and outline in the instructor's plan folder define the
full deck that follows approval.
"""

from deckkit import Chapter, Check, Content, Figure, Mark, Pair, Question, Section

Q = Question

KEY_FIGURE = Figure(
    title="Bearish key reversal: the five steps",
    number="7.15",
    aspect=701 / 413,
    marks=(
        Mark(1, "circle", 0.515, 0.03, 0.585, 0.23,
             color="gold", at=(0.62, 0.03)),
        Mark(2, "circle", 0.515, 0.22, 0.585, 0.39,
             color="red", at=(0.63, 0.39)),
        Mark(3, "circle", 0.505, 0.74, 0.595, 0.98,
             color="blue", at=(0.64, 0.86)),
    ),
    shows=("Apple daily chart. The marked bar opens above the previous high, "
           "makes a new high, closes below the previous close, and has above "
           "average volume."),
    notes=(
        "Start with the five steps in the body, then point to the same three "
        "numbered places on Figure 7.15.",
        "The book says the bar opens above the previous high, makes a new high, "
        "and closes below the previous close. Above average volume strengthens "
        "the reading, but does not guarantee a rapid decline.",
        "The figure also shows consolidation before the later decline. Keep the "
        "word potentially: this is a warning, not a promise.",
    ),
    origin=("Lim (2016), pp. 218 to 219, Figure 7.15. The worked PHP values "
            "are ours, invented to show the rule."),
)

BULLISH_FIGURE = Figure(
    title="Bullish key reversal: the converse",
    number="7.14",
    aspect=701 / 416,
    marks=(
        Mark(1, "circle", 0.415, 0.55, 0.485, 0.78,
             color="gold", at=(0.36, 0.55)),
        Mark(2, "circle", 0.415, 0.69, 0.485, 0.86,
             color="red", at=(0.35, 0.86)),
        Mark(3, "circle", 0.405, 0.78, 0.50, 0.99,
             color="blue", at=(0.34, 0.98)),
    ),
    shows=("Apple daily chart. The marked bar makes a new low, closes above "
           "the previous close, and is followed by a rapid rebound on high "
           "volume."),
    notes=(
        "This is the exact converse: a new low, then a close above the previous "
        "close, in a downtrend.",
        "The book says the bullish key reversal occurs on high volume and price "
        "rebounds rapidly in this example.",
    ),
    origin=("Lim (2016), p. 218, Figure 7.14. The worked PHP values are ours, "
            "invented to show the converse."),
)

COMPARISON_CHART = __import__("deckkit").Chart(
    letter="A",
    title="Exhaustion bar and pin bar: same-looking warning, different reason",
    shows=("Two invented three-bar examples. Left: an exhaustion bar opens "
            "beyond the prior high and is followed without a gap. Right: a "
            "pin bar penetrates support and closes back above it."),
    marks=(),
    tier="core",
    notes=(
        "Read left to right. The exhaustion bar opens beyond the previous high, "
        "but its distinction is the absence of a following gap.",
        "The pin bar gives a false impression of breaking support, then retraces "
        "back above it. Its volume is low in the invented example.",
        "The book's difference is the false barrier penetration, not the size of "
        "the bar alone.",
    ),
    origin=("Lim (2016), pp. 226 to 227. Chart A is ours, with invented PHP "
            "bars and volume to answer review question 1."),
)

KEY_CHECK = Check(
    label="Key reversal bars",
    questions=(
        Q(
            stem=("A bearish key reversal bar must make a higher high than the "
                  "previous bar and then:") ,
            options=(
                "Close near or below the previous close",
                "Close above the previous high",
                "Open below the previous low",
                "Trade on low volume only",
            ),
            answer="A",
            reason=("Lim defines the bearish pattern as a higher high followed "
                    "by a close near or below the previous close."),
        ),
        Q(
            stem=("In the invented example, what does the blue mark identify "
                  "on Figure 7.15?") ,
            options=(
                "The previous bar's close",
                "The new high",
                "The above-average volume",
                "The later consolidation",
            ),
            answer="C",
            reason=("Blue mark 3 identifies the above-average volume below the "
                    "key reversal bar."),
        ),
    ),
    picture=KEY_FIGURE,
    text_w=6.4,
    layout="top",
    notes=(
        "Let the room answer from the earlier marked slide. Do not reveal the "
        "answers on this question slide.",
    ),
    origin="Questions are ours and answerable from the preceding sample slide.",
)

SECOND_CHECK = Check(
    label="Key reversal review",
    questions=(
        Q(
            stem="A wider key reversal bar makes downside follow-through:",
            options=("Impossible", "Always certain", "Unrelated", "Potentially more reliable"),
            answer="D",
            reason="The book says a wider bar makes follow-through potentially more reliable.",
        ),
        Q(
            stem="The bullish converse is read in a:",
            options=("Downtrend", "Flat market only", "Monthly chart only", "Volume panel"),
            answer="B",
            reason="The bullish key reversal is the converse in a downtrend.",
        ),
    ),
    picture=KEY_FIGURE,
    text_w=6.4,
    layout="top",
    notes=("Use this second two-item check so the foundation build keeps a balanced answer key.",),
    origin="Questions are ours and answerable from the preceding sample slides.",
)

SECTION1 = Section(
    number=1,
    title="The Price Bar",
    short="7.1 Price bar",
    minutes="",
    covers=("OHLC", "range", "higher timeframe"),
    slides=(),
)

SECTION2 = Section(
    number=2,
    title="Reading a Pattern",
    short="7.2 Pattern reading",
    minutes="",
    covers=("continuation", "reversal", "16 characteristics"),
    slides=(),
)

SECTION3 = Section(
    number=3,
    title="Popular Reversal Patterns",
    short="7.3 Popular reversals",
    minutes="",
    covers=("key reversal", "exhaustion", "pin bar"),
    slides=(
        Pair(
            left=Content(
                title="Bearish key reversal: five steps",
                lines=(
                    "In an uptrend, the bar makes a higher high, then closes near or below the previous close.",
                    "Ours: previous high 52.00, close 51.10. New bar opens 52.30, reaches 53.20, closes 50.80, volume 4.2 million versus 2.0 million.",
                    "[1] Open above the old high. [2] Make a new high. [3] Close below the old close; read the above-average volume.",
                    "A wider bar can make downside follow-through potentially more reliable. A decline may wait through consolidation.",
                ),
                accent="A warning of potential reversal, not a promise of immediate decline.",
                caption="",
            ),
            picture=KEY_FIGURE,
            text_w=6.8,
            notes=KEY_FIGURE.notes,
            origin=KEY_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="The bullish converse",
                lines=(
                    "In a downtrend, a bullish key reversal makes a new low, then closes near or above the previous close.",
                    "Ours: previous low PHP 42.00 and close PHP 41.00. New bar reaches PHP 40.50 and closes PHP 43.20 on 4.0 million shares.",
                    "[1] New low. [2] Close above the previous close. [3] High volume supports the potential reversal.",
                ),
                accent="Same five-step reading, reversed direction.",
                caption="Book p. 218 and Figure 7.14. The values are ours, invented to show the converse.",
            ),
            picture=BULLISH_FIGURE,
            text_w=6.4,
            notes=BULLISH_FIGURE.notes,
            origin=BULLISH_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Exhaustion bar versus pin bar",
                lines=(
                    "Exhaustion, ours: prior high 65.00; open 65.40, high 66.20, low 60.00, close 60.50; next open 60.20, so no gap.",
                    "Pin bar, ours: support 40.00; low 38.80, close 40.60, volume 0.8 million. It penetrates support, then closes back above it.",
                    "Exhaustion does not usually falsely penetrate a barrier. Pin bars do, and the book says they usually form on low volume.",
                ),
                accent="The difference is the false barrier penetration, not simply a long wick.",
                caption="",
            ),
            picture=COMPARISON_CHART,
            text_w=6.4,
            notes=COMPARISON_CHART.notes,
            origin=COMPARISON_CHART.origin,
        ),
        KEY_CHECK,
        SECOND_CHECK,
    ),
)

SECTION4 = Section(
    number=4,
    title="Volatility-Based Breakouts",
    short="7.4 Volatility breakouts",
    minutes="",
    covers=("Williams’ Oops", "ID/NR4 to NR7"),
    slides=(),
)

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 7",
    title="Bar Chart Analysis",
    subtitle="How a bar can warn of a potential reversal",
    presenter="Faculty of Economics University",
    objectives=(
        "Read OHLC construction and the range of a price bar.",
        "Separate intrinsic sentiment from trend sentiment.",
        "Read the book’s bar reversal patterns with numbers and figures.",
        "Use the 16 reversal characteristics as context, not certainty.",
    ),
    roadmap=(
        "Part 1  The price bar",
        "Part 2  Reading a pattern",
        "Part 3  Popular reversal patterns",
        "Part 4  Volatility-based breakouts",
    ),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4),
    closing=(
        Content(
            title="Foundation build close",
            lines=(
                "The full Chapter 7 deck follows the approved outline in four parts.",
                "These samples establish the five-step teaching pattern, readable figures, numbered marks, and separate question and answer slides.",
            ),
            accent="Approval of the outline and samples is the gate for the full build.",
            notes=("Point back to the plan folder PDF, not to an unbuilt slide number.",),
            origin="Foundation scaffold for the approved Chapter 7 plan.",
        ),
    ),
    dividers=True,
)
