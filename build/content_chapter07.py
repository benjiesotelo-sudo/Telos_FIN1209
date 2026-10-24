"""FIN1209 Chapter 7 foundation deck.

This scaffold contains the three approved sample ideas in their real teaching
form. The source map and outline in the instructor's plan folder define the
full deck that follows approval.
"""

from deckkit import (Chapter, Check, Chart, Content, Figure, Mark, Pair,
                     Question, Section)

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

KEY_CROP_FIGURE = Figure(
    title="Figure 7.15: read the warning",
    number="7.15",
    aspect=701 / 413,
    crop=(0.30, 0.0, 0.20, 0.02),
    marks=(
        Mark(1, "circle", 0.43, 0.10, 0.51, 0.18,
             color="gold", at=(0.34, 0.06), size=0.39),
        Mark(2, "circle", 0.47, 0.02, 0.54, 0.10,
             color="red", at=(0.63, 0.01), size=0.39),
        Mark(3, "circle", 0.50, 0.24, 0.58, 0.32,
             color="blue", at=(0.69, 0.35), size=0.39),
    ),
    shows=("The Apple daily chart, cropped to the key reversal day and its "
           "surrounding bars. The marked bar opens above the previous high, "
           "forms a new high, and closes below the previous close."),
    notes=(
        "Read the worked PHP example first. Then use the crop to locate the "
        "same three actions in the book's chart.",
        "The three marks identify open, new high, and close. The later bars show "
        "that the decline does not have to be immediate.",
    ),
    origin=("Lim (2016), pp. 218 to 219, Figure 7.15. The crop and marks are "
            "for teaching; the worked PHP values are ours, invented."),
)

KEY_READ_FIGURE = Figure(
    title="Figure 7.15: the same reading on a real chart",
    number="7.15",
    aspect=701 / 413,
    crop=(0.35, 0.04, 0.27, 0.02),
    marks=(
        Mark(1, "circle", 0.48, 0.065, 0.56, 0.105,
             color="gold", at=(0.25, 0.09), size=0.30),
        Mark(2, "circle", 0.49, 0.035, 0.55, 0.075,
             color="red", at=(0.73, 0.06), size=0.30),
        Mark(3, "circle", 0.51, 0.15, 0.59, 0.195,
             color="blue", at=(0.75, 0.22), size=0.30),
        Mark(4, "circle", 0.48, 0.77, 0.56, 0.85,
             color="purple", at=(0.64, 0.84), size=0.30),
    ),
    shows=("The Apple daily chart, cropped to the key reversal day and its "
           "surrounding bars. The marked day opens above the previous high, "
           "forms a new high, closes below the previous close, and has above "
           "average volume."),
    notes=(
        "Read the book's definition first, then explain marks 1 to 4 in the "
        "same order: gap/open, new high, close, and above-average volume.",
        "The figure shows consolidation before the later decline. Keep the "
        "word potentially: this is a warning, not a promise.",
    ),
    origin=("Lim (2016), pp. 218 to 219, Figure 7.15. The crop and marks are "
            "for teaching; no invented example is on this slide."),
)

KEY_WORKED_CHART = Chart(
    letter="B",
    title="Bearish key reversal: a two-bar worked example",
    shows=("Two invented PHP bars with every OHLC value and volume value "
            "labelled. Marks 1 to 4 show the five-step reading."),
    tier="core",
    marks=(
        Mark(1, "circle", 0.64, 0.29, 0.69, 0.34,
             color="gold", at=(0.52, 0.34)),
        Mark(2, "circle", 0.64, 0.18, 0.69, 0.23,
             color="red", at=(0.77, 0.13)),
        Mark(3, "circle", 0.64, 0.52, 0.69, 0.57,
             color="blue", at=(0.77, 0.62)),
        Mark(4, "circle", 0.64, 0.78, 0.70, 0.84,
             color="purple", at=(0.80, 0.88), size=0.32),
    ),
    notes=(
        "Read the prior high and prior close lines before reading marks 1 to 4.",
        "The second bar opens above 52.00, reaches a new high of 53.20, and "
        "closes at 50.80, below the prior close of 51.10. Mark 4 identifies "
        "the 4.2 million-share volume bar.",
    ),
    origin="Chart B is ours, with invented PHP bars and million-share volume.",
)

COMPARISON_CHART = Chart(
    letter="A",
    title="Exhaustion bar and pin bar: same-looking warning, different reason",
    shows=("Two invented three-bar examples. Left: an exhaustion bar opens "
            "beyond the prior high and is followed without a gap. Right: a "
            "pin bar penetrates support and closes back above it."),
    marks=(
        Mark(1, "circle", 0.25, 0.29, 0.30, 0.34,
             color="gold", at=(0.12, 0.23)),
        Mark(2, "circle", 0.25, 0.55, 0.30, 0.60,
             color="red", at=(0.12, 0.69)),
        Mark(3, "circle", 0.75, 0.45, 0.80, 0.50,
             color="blue", at=(0.88, 0.58)),
    ),
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
    label="From “Figure 7.15: three observations”",
    questions=(
        Q(
            stem="A bearish key reversal makes a higher high, then:",
            options=(
                "Near or below prior close",
                "Above prior high",
                "Below prior low",
                "On low volume only",
            ),
            answer="A",
            reason=("Lim defines the bearish pattern as a higher high followed "
                    "by a close near or below the previous close."),
        ),
        Q(
            stem="On Figure 7.15, blue mark 3 identifies:",
            options=(
                "Prior close",
                "New high",
                "Close below prior close",
                "Later bars",
            ),
            answer="C",
            reason=("The preceding slide maps blue mark 3 to the close below "
                    "the previous close (Lim, p. 219)."),
        ),
    ),
    picture=KEY_CROP_FIGURE,
    text_w=5.8,
    layout="beside",
    notes=(
        "Let the room answer from the earlier marked slide. Do not reveal the "
        "answers on this question slide.",
    ),
    origin="Questions are ours and answerable from the preceding sample slide.",
)

SECOND_CHECK = Check(
    label="From “Figure 7.15: three observations”",
    questions=(
        Q(
            stem="A wider key reversal bar makes downside follow-through:",
            options=("Impossible", "Always certain", "Unrelated", "Potentially more reliable"),
            answer="D",
            reason="The book says a wider bar makes follow-through potentially more reliable.",
        ),
        Q(
            stem="The bullish converse is read in a:",
            options=("Monthly chart only", "Downtrend", "Flat market only", "Volume panel"),
            answer="B",
            reason="The bullish key reversal is the converse in a downtrend.",
        ),
    ),
    picture=KEY_CROP_FIGURE,
    text_w=5.8,
    layout="beside",
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
                title="Bearish key reversal: the numbers first",
                lines=(
                    "Step 1. Prior bar: open 50.80, high 52.00, low 50.60, close 51.10.",
                    "Step 2. It opens at 52.30 above prior high 52.00 [1].",
                    "Step 3. It makes a new high of 53.20 [2].",
                    "Step 4. It closes at 50.80 below prior close 51.10 [3].",
                    "Step 5. Volume is 4.2 million versus 2.0 million [4]. That is a bearish key reversal (Lim, p. 218).",
                ),
                accent="",
                caption="",
            ),
            picture=KEY_WORKED_CHART,
            text_w=4.25,
            picture_extra=0.0,
            notes=KEY_WORKED_CHART.notes,
            origin=KEY_WORKED_CHART.origin,
        ),
        Pair(
            left=Content(
                title="Figure 7.15: the same reading on a real chart",
                lines=(
                    "Lim defines it: “A bearish key reversal bar forms a higher high than the previous bar and closes near or below the close of the previous bar.” (Lim, p. 218).",
                    "Gold [1] marks the key reversal day opening above the prior high. Red [2] marks its new high.",
                    "Blue [3] marks its close below the prior close. Purple [4] marks the above-average volume under it.",
                    "Meaning/action: a potential warning, not a promise. The book's chart shows consolidation before the decline. Check the 16 characteristics and barrier proximity.",
                ),
                accent="",
                caption="",
            ),
            picture=KEY_READ_FIGURE,
            text_w=6.6,
            notes=KEY_READ_FIGURE.notes,
            origin=KEY_READ_FIGURE.origin,
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
                    "Exhaustion: in an uptrend, it opens at 65.40 above prior high 65.00, reaches 66.20, and closes at 60.50; the next bar opens at 60.20 with no gap.",
                    "Pin bar: it penetrates support at 40.00 to 38.80, then rapidly retraces and closes at 40.60.",
                    "Meaning/action: exhaustion warns of a tiring trend; a pin bar warns of a false breakout.",
                ),
                accent="",
                caption="",
            ),
            picture=COMPARISON_CHART,
            text_w=3.6,
            picture_extra=0.8,
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
