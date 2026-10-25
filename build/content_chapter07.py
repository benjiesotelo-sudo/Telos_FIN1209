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

KEY_CAVEAT_FIGURE = Figure(
    title="Figure 7.15: consolidation before decline",
    number="7.15",
    aspect=701 / 413,
    crop=(0.25, 0.04, 0.05, 0.02),
    marks=(
        Mark(1, "box", 0.49, 0.14, 0.60, 0.29,
             color="gold", at=(0.44, 0.10), size=0.28),
        Mark(2, "box", 0.65, 0.16, 0.76, 0.42,
             color="red", at=(0.81, 0.45), size=0.28),
    ),
    shows=("The Apple daily chart, cropped to the key reversal day and the "
           "later consolidation and decline."),
    notes=(
        "The book's point is timing: a decline may pause near the key bar. "
        "Marks 1 and 2 identify the hover and the later decline.",
    ),
    origin=("Lim (2016), p. 219, Figure 7.15. The PHP path is ours, invented "
            "to show consolidation."),
)

KEY_CROP_FIGURE = Figure(
    title="Figure 7.15: read the warning",
    number="7.15",
    aspect=701 / 413,
    # Keep the marked day readable on the check answer slides. The earlier
    # narrow crop made the picture portrait-shaped and too small beside the
    # two answer cards.
    crop=(0.20, 0.0, 0.05, 0.02),
    marks=(
        Mark(1, "circle", 0.42, 0.10, 0.47, 0.18,
             color="gold", at=(0.36, 0.06), size=0.34),
        Mark(2, "circle", 0.45, 0.02, 0.49, 0.10,
             color="red", at=(0.55, 0.01), size=0.34),
        Mark(3, "circle", 0.47, 0.24, 0.52, 0.32,
             color="blue", at=(0.59, 0.35), size=0.34),
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
                 color="red", at=(0.88, 0.18)),
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
        Mark(1, "circle", 0.245, 0.225, 0.265, 0.265,
             color="gold", at=(0.20, 0.16), size=0.25),
        Mark(2, "circle", 0.245, 0.17, 0.265, 0.21,
             color="red", at=(0.31, 0.15), size=0.25),
        Mark(3, "circle", 0.245, 0.57, 0.27, 0.63,
             color="blue", at=(0.30, 0.67), size=0.25),
        Mark(4, "line", 0.27, 0.60, 0.37, 0.58,
             color="purple", at=(0.42, 0.55), size=0.25),
        Mark(5, "circle", 0.735, 0.60, 0.77, 0.67,
             color="gold", at=(0.70, 0.73), size=0.25),
        Mark(6, "circle", 0.735, 0.37, 0.77, 0.43,
             color="red", at=(0.83, 0.38), size=0.25),
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
    text_w=5.0,
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
    text_w=5.0,
    layout="beside",
    notes=("Use this second two-item check so the foundation build keeps a balanced answer key.",),
    origin="Questions are ours and answerable from the preceding sample slides.",
)

PRICE_BAR_FULL = Figure(
    title="Figure 7.1: four prices summarize one interval",
    number="7.1",
    aspect=560 / 404,
    marks=(
        Mark(1, "circle", 0.62, 0.38, 0.69, 0.46,
             color="gold", at=(0.57, 0.38), size=0.30),
        Mark(2, "circle", 0.62, 0.20, 0.69, 0.28,
             color="red", at=(0.76, 0.15), size=0.30),
        Mark(3, "circle", 0.62, 0.68, 0.69, 0.76,
             color="blue", at=(0.76, 0.82), size=0.30),
        Mark(4, "circle", 0.69, 0.45, 0.76, 0.53,
             color="purple", at=(0.83, 0.53), size=0.30),
    ),
    shows=("Figure 7.1: five minutes of changing price are filtered into one "
           "bar that keeps only the open, high, low and close. The range is "
           "the distance from high to low."),
    notes=(
        "Read the left-hand price activity, then the single bar on the right. "
        "The gold mark is the open, red the high, blue the low, and purple 4 the close.",
        "Purple 4 is the close, and the bracket on the right shows the high-to-low range. The figure labels these as filtered price action.",
    ),
    origin=("Lim (2016), p. 210, Figure 7.1. The marks and worked PHP values "
            "are ours, added for teaching."),
)

PRICE_BAR_CONSTRUCTION = Figure(
    title="Figure 7.1: the trades that make one bar",
    number="7.1",
    aspect=560 / 404,
    crop=(0.0, 0.08, 0.49, 0.08),
    marks=(
        Mark(1, "circle", 0.23, 0.36, 0.33, 0.48,
             color="gold", at=(0.18, 0.48), size=0.30),
        Mark(2, "circle", 0.38, 0.15, 0.48, 0.28,
             color="red", at=(0.53, 0.09), size=0.30),
        Mark(3, "circle", 0.50, 0.42, 0.60, 0.55,
             color="blue", at=(0.65, 0.58), size=0.30),
        Mark(4, "circle", 0.46, 0.68, 0.56, 0.80,
             color="purple", at=(0.60, 0.84), size=0.30),
    ),
    shows=("Figure 7.1 construction panel, cropped to the five-minute price "
           "path. The first trade, highest trade and last trade become the "
           "bar's open, high and close; the lowest trade supplies the low."),
    notes=(
        "The crop enlarges the construction panel so the sequence can be read. "
        "Gold 1 is the first trade, red 2 the highest trade, blue 3 the last trade, and purple 4 the lowest trade.",
        "The lowest trade is also retained as the low, even though this crop's "
        "three teaching marks focus on first, highest and last.",
    ),
    origin=("Lim (2016), p. 210, Figure 7.1, construction panel. The crop, "
            "marks and worked PHP values are ours, added for teaching."),
)

HIGHER_TIMEFRAME_FIGURE = Figure(
    title="Figure 7.2: the composite bar keeps the extremes",
    number="7.2",
    aspect=661 / 450,
    crop=(0.50, 0.06, 0.02, 0.20),
    marks=(
        Mark(1, "circle", 0.58, 0.36, 0.72, 0.46,
             color="gold", at=(0.54, 0.39), size=0.27),
        Mark(2, "circle", 0.58, 0.15, 0.72, 0.25,
             color="red", at=(0.88, 0.10), size=0.27),
        Mark(3, "circle", 0.58, 0.86, 0.72, 0.96,
             color="blue", at=(0.88, 0.98), size=0.27),
        Mark(4, "circle", 0.58, 0.59, 0.72, 0.70,
             color="purple", at=(0.54, 0.62), size=0.27),
    ),
    shows=("Figure 7.2 composite-bar panel, cropped to the 15-minute bar. "
           "Three five-minute bars are summarized by the first open, highest "
           "high, lowest low and last close."),
    notes=(
        "The crop isolates the higher-timeframe bar. Gold 1 is the first open, "
        "red 2 the highest high, blue 3 the lowest low, and purple 4 the last close.",
        "The labels show what survives when three lower-timeframe intervals are "
        "combined. No intermediate open or close survives in the composite.",
    ),
    origin=("Lim (2016), p. 210, Figure 7.2, composite-bar panel. The crop, "
            "marks and worked PHP values are ours, added for teaching."),
)

FORMATION_FULL = Figure(
    title="Figure 7.3: read each interval before classifying it",
    number="7.3",
    aspect=697 / 409,
    marks=(
        Mark(1, "circle", 0.035, 0.28, 0.105, 0.43,
             color="gold", at=(0.02, 0.23), size=0.28),
        Mark(2, "circle", 0.56, 0.30, 0.63, 0.45,
             color="red", at=(0.67, 0.25), size=0.28),
        Mark(3, "circle", 0.57, 0.66, 0.64, 0.80,
             color="blue", at=(0.68, 0.84), size=0.28),
    ),
    shows=("Figure 7.3 shows a series of five-minute price intervals above "
           "the corresponding OHLC bars below. Each interval becomes one "
           "bar before a formation is classified."),
    notes=(
        "Read one interval at a time from left to right. Gold 1 identifies "
        "the first interval, red 2 a later sequence, and blue 3 the "
        "corresponding OHLC bars below.",
        "The figure shows the book's sequence, not a new trading signal. "
        "Classification comes only after the intervals have been read.",
    ),
    origin="Lim (2016), p. 210, Figure 7.3. Marks are ours, added for teaching.",
)

WORKED_CROP = Figure(
    title="Figure 7.3: the worked classification read",
    number="7.3",
    aspect=697 / 409,
    crop=(0.62, 0.02, 0.04, 0.0),
    marks=(
        Mark(1, "box", 0.20, 0.54, 0.69, 0.96,
             color="gold", at=(0.12, 0.52), size=0.28),
        Mark(2, "circle", 0.51, 0.60, 0.68, 0.94,
             color="red", at=(0.72, 0.58), size=0.28),
        Mark(3, "circle", 0.55, 0.08, 0.80, 0.43,
             color="blue", at=(0.84, 0.05), size=0.28),
    ),
    shows=("Figure 7.3 crop showing the two counted OHLC bars, the second "
           "bar's location, and the rising price context used in the worked read."),
    notes=(
        "Gold 1 brackets the two counted bars. Red 2 circles the second bar, "
        "whose own close is the invented bearish example. Blue 3 circles the "
        "rising price path that supplies bullish trend sentiment.",
        "The crop is repeated wherever this classification evidence is read, "
        "so the picture claim stays visible when it is tested.",
    ),
    origin="Lim (2016), p. 210, Figure 7.3. Crop and marks are ours, added for teaching.",
)

CLASSIFICATION_CROP = Figure(
    title="Figure 7.3: three classification cues",
    number="7.3",
    aspect=697 / 409,
    crop=(0.62, 0.02, 0.04, 0.0),
    marks=WORKED_CROP.marks,
    shows=WORKED_CROP.shows,
    notes=WORKED_CROP.notes,
    origin=WORKED_CROP.origin,
)

SENTIMENT_CHART = Chart(
    letter="S",
    title="The two-by-two sentiment table",
    shows=("A plain two-by-two table. Rows are uptrend and downtrend; columns "
           "are bullish and bearish formations. Each cell shows continuation "
           "or potential reversal."),
)

WORKED_CHART = Chart(
    letter="U",
    title="Part 1 worked read",
    marks=(
        Mark(1, "box", 0.60, 0.11, 0.83, 0.30,
             color="gold", at=(0.56, 0.16), size=0.20),
        Mark(2, "circle", 0.74, 0.23, 0.80, 0.30,
             color="red", at=(0.84, 0.23), size=0.18),
        Mark(3, "arrow", 0.27, 0.65, 0.56, 0.42,
             color="blue", at=(0.60, 0.38), size=0.20),
    ),
    shows=("Our invented five-bar chart makes the two-bar formation and its "
           "rising price context visible, including the first low 50.20 and "
           "second close 49.80."),
    notes=(
        "Gold 1 brackets the two bars that make the double formation. Red 2 "
        "marks the second bar and its close below the first low. Blue 3 marks "
        "the rising context before the pair.",
        "All prices are invented and written on our own chart so the worked "
        "read can be checked without the prose alone.",
    ),
    origin="FIN1209 teaching chart U. All PHP values, marks and labels are ours, invented.",
)

# --------------------------------------------------------------------------
# Part 3, first half: the sample sequence above is kept unchanged.  The
# figures below are the book's figures, with the teaching marks in this
# chapter's colours.  The three charts are ours and use letters R onward so
# they cannot collide with the approved sample charts A and B.
# --------------------------------------------------------------------------

KEY_PLAIN = Content(
    title="Key reversal: plain words",
    lines=(
        "A bearish key reversal starts in an uptrend, makes a higher high, then closes near or below the previous close.",
        "It is a warning, not a promise. Lim says a wider bar may make follow-through more reliable, but an immediate decline is not guaranteed (p. 218).",
        "Next, put the rule into invented prices before reading the book's chart.",
    ),
    accent="The definition is about the higher high and the close, not the bar's name.",
    notes=(
        "Say the plain rule first. The worked example on the next approved sample slide supplies the numbers.",
        "Keep may and potential: Lim describes a possible reversal, not a certainty.",
    ),
    origin="Lim (2016), p. 218. The plain-language teaching sequence is ours.",
)

KEY_CAVEAT = Pair(
    left=Content(
        title="Key reversal: consolidation can come first",
        lines=(
            "Lim says a rapid decline may not follow. The market can hover near the key bar [1] before falling [2] (p. 219).",
            "Ours: the key bar closes PHP 50.80, then prices hover at PHP 50.60 [1] before declining to PHP 48.90 [2].",
            "Meaning/action: treat the bar as a potential warning; wait for the surrounding context rather than assuming timing.",
        ),
        accent="A wide bar may make follow-through more reliable, but width does not guarantee it.",
    ),
    picture=KEY_CAVEAT_FIGURE,
    text_w=6.8,
    notes=(
        "Point to mark 1 for the hover and mark 2 for the later decline. The book's point is delayed follow-through.",
        "Separate the pattern definition from the later price path. The latter is a caveat, not part of the definition.",
    ),
    origin="Lim (2016), p. 219, Figure 7.15. The PHP path is ours, invented to show consolidation.",
)

KEY_16_FIGURE = Figure(
    title="Bullish key reversal with context",
    number="7.16",
    aspect=575 / 555,
    marks=(
        Mark(1, "circle", 0.40, 0.43, 0.53, 0.68,
             color="gold", at=(0.34, 0.44), size=0.30),
        Mark(2, "circle", 0.44, 0.70, 0.54, 0.86,
             color="red", at=(0.34, 0.73), size=0.30),
        Mark(3, "line", 0.47, 0.43, 0.49, 0.89,
             color="blue", at=(0.63, 0.50), size=0.26),
    ),
    shows="The ITC Holdings daily chart: a bullish key reversal below the lower volatility band, an oversold StochRSI label, and high volume under the reversal bar.",
    notes=(
        "Mark 1 is the bullish key reversal below the lower band. Mark 2 is the book's oversold StochRSI label.",
        "Mark 3 is the high-volume reading. Lim calls these conditions greater potential, not certainty.",
    ),
    origin="Lim (2016), p. 220, Figure 7.16. Bollinger Bands and StochRSI are shown by the book but not defined here.",
)

TWO_DAY_FIGURE = Figure(
    title="Bearish two-day reversal",
    number="7.17",
    aspect=575 / 470,
    marks=(
        Mark(1, "circle", 0.53, 0.20, 0.61, 0.32,
             color="gold", at=(0.45, 0.16), size=0.30),
        Mark(2, "circle", 0.62, 0.18, 0.70, 0.31,
             color="red", at=(0.78, 0.18), size=0.30),
        Mark(3, "circle", 0.42, 0.70, 0.65, 0.91,
             color="blue", at=(0.70, 0.78), size=0.30),
    ),
    shows="The TSX Composite daily chart: the first bar closes near its high, the second near its low, and the lower panel labels bearish CCI divergence.",
    notes=(
        "Read marks 1 and 2 as the two closing positions. The book prefers wider ranges for both bars.",
        "CCI is a label in Lim's figure. Chapter 7 does not define its formula, so do not infer one.",
    ),
    origin="Lim (2016), p. 220, Figure 7.17. The CCI label is reproduced as the book's observation, not taught as a formula.",
)

THREE_BEAR_FIGURE = Figure(
    title="Bearish three-bar reversal",
    number="7.18",
    aspect=560 / 400,
    marks=(
        Mark(1, "box", 0.64, 0.12, 0.69, 0.34,
             color="gold", at=(0.59, 0.10), size=0.28),
        Mark(2, "box", 0.69, 0.13, 0.74, 0.35,
             color="red", at=(0.80, 0.10), size=0.28),
        Mark(3, "line", 0.77, 0.24, 0.55, 0.76,
             color="blue", at=(0.89, 0.55), size=0.26),
    ),
    shows="The Apple daily chart in a clear, strong uptrend: the first of three bars closes near its high, the third near its low, and the lower panel labels bearish +DM divergence.",
    notes=(
        "Marks 1, 2 and 3 identify the first, middle and third bars. The first closes near its high and the third near its low.",
        "The figure also labels bearish +DM divergence and shows rapid later decline, not a guaranteed result.",
    ),
    origin="Lim (2016), p. 221, Figure 7.18. +DM is shown as a book label and is not defined in this chapter.",
)

THREE_BULL_FIGURE = Figure(
    title="Bullish three-bar reversal and volume",
    number="7.19",
    aspect=560 / 390,
    marks=(
        Mark(1, "circle", 0.49, 0.77, 0.54, 0.91,
             color="gold", at=(0.43, 0.72), size=0.25),
        Mark(2, "circle", 0.54, 0.79, 0.58, 0.92,
             color="red", at=(0.62, 0.74), size=0.25),
        Mark(3, "circle", 0.58, 0.77, 0.63, 0.91,
             color="blue", at=(0.69, 0.72), size=0.25),
    ),
    shows="The ITC Holdings daily chart: a three-bar bottom reversal with high-volume outer bars and a below-average-volume middle bar.",
    notes=(
        "Mark 1 is the first outer volume bar, mark 2 is the quiet middle volume bar, and mark 3 is the final outer bar.",
        "The volume relationship is the book's clue. It does not make the reversal certain.",
    ),
    origin="Lim (2016), p. 221, Figure 7.19. Volume labels are the book's observations.",
)

THREE_CONTEXT_FIGURE = Figure(
    title="Bullish three-bar reversal with oversold context",
    number="7.20",
    aspect=565 / 455,
    marks=(
        Mark(1, "box", 0.37, 0.38, 0.51, 0.63,
             color="gold", at=(0.30, 0.36), size=0.30),
        Mark(2, "circle", 0.42, 0.75, 0.55, 0.92,
             color="red", at=(0.66, 0.84), size=0.30),
        Mark(3, "circle", 0.43, 0.42, 0.52, 0.56,
             color="blue", at=(0.58, 0.37), size=0.28),
    ),
    shows="The ITC Holdings daily chart: the three-bar reversal, an oversold StochRSI label, and the final close between the two volatility bands.",
    notes=(
        "Mark 1 boxes the three-bar group. Mark 2 is the oversold StochRSI label.",
        "Mark 3 points to the last close between the bands, which Lim calls bullish. The formulas are not taught here.",
    ),
    origin="Lim (2016), p. 222, Figure 7.20. StochRSI and Bollinger Bands are shown but not defined in Chapter 7.",
)

THREE_OUTSIDE_FIGURE = Figure(
    title="Bullish three-bar reversal followed by an outside day",
    number="7.21",
    aspect=565 / 405,
    marks=(
        Mark(1, "box", 0.35, 0.41, 0.50, 0.68,
             color="gold", at=(0.29, 0.38), size=0.30),
        Mark(2, "circle", 0.43, 0.40, 0.50, 0.57,
             color="red", at=(0.54, 0.34), size=0.28),
        Mark(3, "circle", 0.66, 0.20, 0.73, 0.28,
             color="blue", at=(0.83, 0.18), size=0.26),
        Mark(4, "box", 0.52, 0.10, 0.63, 0.40,
             color="purple", at=(0.47, 0.43), size=0.24),
    ),
    shows="The Newmont Mining daily chart: a three-bar bottom reversal, then a separate outside day engulfing four preceding bars, with high volume under the outside bar.",
    notes=(
        "Mark 1 keeps the first three-bar reversal separate. Mark 2 identifies its large third bar near its high.",
        "Mark 3 boxes the later outside day and its close near the low. Lim says the third bar adds bullishness, not certainty.",
    ),
    origin="Lim (2016), p. 222, Figure 7.21. The outside day and volume are the book's observations.",
)

THREE_PATTERN6_FIGURE = Figure(
    title="Bullish three-bar reversal: pattern 6",
    number="7.22",
    aspect=565 / 400,
    marks=(
        Mark(1, "circle", 0.49, 0.77, 0.55, 0.92,
             color="gold", at=(0.43, 0.72), size=0.25),
        Mark(2, "box", 0.52, 0.48, 0.59, 0.71,
             color="red", at=(0.64, 0.43), size=0.28),
        Mark(3, "circle", 0.54, 0.77, 0.60, 0.92,
             color="blue", at=(0.68, 0.72), size=0.25),
    ),
    shows="The TSX Composite daily chart: a bullish three-bar reversal whose large middle bar has lower volume than the first bar.",
    notes=(
        "Mark 1 boxes the first bar, mark 2 identifies the lower-volume middle bar, and mark 3 identifies the third bar.",
        "Lim links this arrangement to pattern 6 in Figure 7.9. That link recalls the earlier generic pattern; it adds no new formula.",
    ),
    origin="Lim (2016), p. 223, Figure 7.22. The reference to pattern 6 is Lim's cross-reference.",
)

ISLAND_FIGURE = Figure(
    title="Bearish island reversal",
    number="7.23",
    aspect=565 / 515,
    marks=(
        Mark(1, "circle", 0.43, 0.28, 0.50, 0.43,
             color="gold", at=(0.37, 0.23), size=0.27),
        Mark(2, "box", 0.48, 0.16, 0.60, 0.48,
             color="red", at=(0.66, 0.11), size=0.27),
        Mark(3, "circle", 0.62, 0.29, 0.70, 0.44,
             color="blue", at=(0.76, 0.23), size=0.27),
        Mark(4, "box", 0.37, 0.68, 0.56, 0.81,
             color="purple", at=(0.30, 0.84), size=0.25),
        Mark(5, "box", 0.49, 0.83, 0.59, 0.96,
             color="green", at=(0.66, 0.95), size=0.25),
    ),
    shows="The Direxion Gold Miners daily chart: a gap up, an isolated group of bars, a gap down, low volume, and an overbought stochastic label.",
    notes=(
        "An island is isolated by two gaps: mark 1 is the gap up and mark 3 the gap down.",
        "Mark 2 is the isolated formation. Lim also observes low volume and an overbought stochastic label; no formula is taught here.",
    ),
    origin="Lim (2016), p. 224, Figure 7.23. Gap meaning points back to Chapter 3; stochastic is shown but not defined here.",
)

TRIPLE_CHECK = Check(
    label="From the two-day and three-bar reversal readings",
    questions=(
        Q(
            stem="In the bearish three-bar reversal, the outer closes are:",
            options=(
                "Both near the middle",
                "First near high, third near low",
                "First near low, third near high",
                "Both at the exact high",
            ),
            answer="B",
            reason="First near high; third near low (Lim, p. 221).",
        ),
        Q(
            stem="In the bullish three-bar examples, the middle bar can support the reading when it has:",
            options=(
                "The highest volume",
                "A new all-time high",
                "No price range",
                "Below-average volume between stronger outer bars",
            ),
            answer="D",
            reason="Lim describes a below-average-volume middle bar between high-volume outer bars (pp. 221 to 223).",
        ),
    ),
    picture=THREE_BEAR_FIGURE,
    text_w=5.8,
    layout="beside",
    notes=(
        "Let students use the marked Figure 7.18 and the prior body text, not speaker cues.",
        "Reveal the close positions first, then explain that the middle bar's low volume signals uncertainty in the bullish examples.",
    ),
    origin="Questions are ours and answerable from the preceding marked three-bar slides.",
)

KEY_CONTEXT = Pair(
    left=Content(
        title="Key reversal: the bullish context",
        lines=(
            "In a downtrend, the converse makes a new low [1], then closes near or above the previous close [2].",
            "Ours: the prior low is PHP 42.00 and close PHP 41.00; the new low is PHP 40.50, then the close is PHP 43.20 on 4.0 million shares [3].",
            "Lim's Figure 7.14 observes a rapid rebound after a high-volume bullish key reversal.",
        ),
        accent="The direction changes, but the reading still uses the new extreme and the prior close.",
    ),
    picture=BULLISH_FIGURE,
    text_w=5.8,
    notes=(
        "Walk the converse with the invented prices before reading the figure.",
        "The rapid rebound is the book's observation in Figure 7.14, not a promise for every bullish key reversal.",
    ),
    origin="Lim (2016), p. 218, Figure 7.14. The PHP values are ours, invented.",
)

KEY_16_PAIR = Pair(
    left=Content(
        title="Figure 7.16: context can strengthen the warning",
        lines=(
            "The bullish key reversal is below the lower Bollinger band [1], with StochRSI oversold [2].",
            "It closes near its high and has extreme volume [3], which Lim calls indicative of a selling climax (p. 220).",
            "The book gives no formulas here. These labels are context, not a promise of reversal.",
        ),
        accent="Use the labels as context, not as a promise of a reversal.",
    ),
    picture=KEY_16_FIGURE,
    text_w=7.0,
    notes=KEY_16_FIGURE.notes,
    origin=KEY_16_FIGURE.origin,
)

TWO_DAY_WORKED = Pair(
    left=Content(
        title="Two-day reversal: read the closes",
        lines=(
            "First close near high [1]; second near low [2].",
            "Ours: PHP 51.80, then PHP 49.60; the second range is wider.",
            "Meaning/action: potential bearish reversal, not a guarantee.",
        ),
        accent="",
    ),
    picture=Chart(
        letter="RA",
        title="Two-day bearish reversal",
        shows="Two invented PHP bars with OHLC values, closing positions and million-share volume labelled. Mark 1 is the first close near the high and mark 2 the second near the low.",
        tier="core",
        marks=(
            Mark(1, "circle", 0.27, 0.28, 0.34, 0.36, color="gold", at=(0.12, 0.28), size=0.25),
            Mark(2, "circle", 0.64, 0.56, 0.72, 0.65, color="red", at=(0.80, 0.52), size=0.25),
        ),
    ),
    text_w=4.0,
    picture_extra=0.1,
    notes=(
        "Read the first close near the high, then the second near the low.",
        "The values and volume are ours, invented. The wider-range preference comes from Lim, p. 220.",
    ),
    origin="Lim (2016), p. 220. Chart RA is ours, with invented PHP bars and volume.",
)

TWO_DAY_READ = Pair(
    left=Content(
        title="Figure 7.17: the book adds CCI divergence",
        lines=(
            "Mark 1 is the first close near its high; mark 2 is the second close near its low.",
            "The book says wider ranges would be preferable and labels bearish CCI divergence [3].",
            "CCI is not defined in Chapter 7. Treat the label as the book's supporting observation, not as a formula to calculate.",
        ),
        accent="The close sequence is the pattern; CCI is context shown by the figure.",
    ),
    picture=TWO_DAY_FIGURE,
    text_w=5.7,
    notes=TWO_DAY_FIGURE.notes,
    origin=TWO_DAY_FIGURE.origin,
)

THREE_WORKED = Pair(
    left=Content(
        title="Bullish three-bar reversal: volume",
        lines=(
            "Read volume: strong [1], quiet [2], strong [3].",
            "Ours: 4.0m, 0.6m, then 4.2m shares.",
            "Meaning/action: a quiet middle shows uncertainty, not a guarantee.",
        ),
        accent="",
    ),
    picture=Chart(
        letter="RB",
        title="Bullish three-bar reversal",
        shows="Three invented PHP bars with OHLC values and volumes labelled. Marks 1, 2 and 3 identify the first, middle and third volume readings.",
        tier="core",
        marks=(
            Mark(1, "circle", 0.22, 0.75, 0.29, 0.84, color="gold", at=(0.14, 0.55)),
            Mark(2, "circle", 0.47, 0.75, 0.54, 0.84, color="red", at=(0.42, 0.70)),
            Mark(3, "circle", 0.73, 0.75, 0.80, 0.84, color="blue", at=(0.86, 0.70)),
        ),
    ),
    text_w=4.0,
    picture_extra=0.1,
    notes=(
        "Read volumes left to right: strong, quiet, strong.",
        "The arithmetic and volume are ours, invented; the interpretation follows Lim, pp. 221 to 223.",
    ),
    origin="Lim (2016), pp. 221 to 223. Chart RB is ours, with invented PHP bars and volume.",
)

THREE_BEAR_READ = Pair(
    left=Content(
        title="Figure 7.18: the bearish three-bar structure",
        lines=(
            "In a clear, strong uptrend, mark 1 is the first bar, mark 2 the middle bar, and mark 3 the third bar.",
            "The first closes near its high and the third near its low. The figure also labels bearish +DM divergence [3].",
            "Meaning/action: read the three bars with trend and volume context; the later decline is not guaranteed.",
        ),
        accent="The first and third bars carry the outer close reading; the middle bar separates them.",
    ),
    picture=THREE_BEAR_FIGURE,
    text_w=6.3,
    notes=THREE_BEAR_FIGURE.notes,
    origin=THREE_BEAR_FIGURE.origin,
)

THREE_BULL_READ = Pair(
    left=Content(
        title="Figure 7.19: the volume pattern",
        lines=(
            "The three-bar bottom reversal has high-volume outer columns [1] and [3], with a below-average middle column [2].",
            "This is the same uncertainty-between-strengthers reading shown in the invented example.",
            "Volume supports the potential reversal. Lim does not say it guarantees follow-through.",
        ),
        accent="Keep the quiet middle bar between the stronger outer bars.",
    ),
    picture=THREE_BULL_FIGURE,
    text_w=6.0,
    notes=THREE_BULL_FIGURE.notes,
    origin=THREE_BULL_FIGURE.origin,
)

THREE_CONTEXT_PAIR = Pair(
    left=Content(
        title="Figure 7.20:\noversold context",
        lines=(
            "Mark 1 is the three-bar bullish reversal. The full pattern occurs at an oversold StochRSI [2].",
            "The last close sits between the Bollinger bands [3], which Lim calls bullish.",
            "The book links this example to pattern 5 in Figure 7.9. It gives no indicator formula here.",
        ),
        accent="The pattern is read first; the indicator labels add context.",
    ),
    picture=THREE_CONTEXT_FIGURE,
    text_w=6.0,
    notes=THREE_CONTEXT_FIGURE.notes,
    origin=THREE_CONTEXT_FIGURE.origin,
)

THREE_OUTSIDE_PAIR = Pair(
    left=Content(
        title="Figure 7.21: a separate outside day follows",
        lines=(
            "The three-bar reversal is marked 1. Its large third bar near its high [2] adds bullishness.",
            "Later, the outside day engulfs four preceding bars [4] and closes near its low [3].",
            "Keep the two formations separate: the later outside day is a new event and can reverse the preceding move.",
        ),
        accent="Below-average middle volume and high-volume outer bars are the three-bar clue; the outside day is separate.",
    ),
    picture=THREE_OUTSIDE_FIGURE,
    text_w=6.35,
    notes=THREE_OUTSIDE_FIGURE.notes,
    origin=THREE_OUTSIDE_FIGURE.origin,
)

THREE_PATTERN6_PAIR = Pair(
    left=Content(
        title="Figure 7.22:\nthe pattern 6 link",
        lines=(
            "Mark 1 is the first-bar volume. Mark 2 is the large middle-bar range.",
            "Mark 3 is the middle-bar volume, lower than the first. Lim links this arrangement to pattern 6 in Figure 7.9.",
            "The link recalls the generic pattern; it does not add a new trading rule or formula.",
        ),
        accent="A large price bar can still carry lower volume than the first bar.",
    ),
    picture=THREE_PATTERN6_FIGURE,
    text_w=6.1,
    notes=THREE_PATTERN6_FIGURE.notes,
    origin=THREE_PATTERN6_FIGURE.origin,
)

ISLAND_WORKED = Pair(
    left=Content(
        title="Island reversal: two gaps",
        lines=(
            "Read the gap up [1], isolated bars [2], then gap down [3].",
            "Ours: PHP 50.00 to 50.80, then PHP 49.40.",
            "Meaning/action: two gaps isolate a potential reversal warning.",
        ),
        accent="",
    ),
    picture=Chart(
        letter="RC",
        title="Bearish island reversal",
        shows="Four invented PHP bars with the prior high, gap-up open, isolated bars, gap-down open and volume values labelled. Marks 1, 2 and 3 identify the two gaps and the island.",
        tier="core",
        marks=(
            Mark(1, "circle", 0.30, 0.20, 0.39, 0.30, color="gold", at=(0.25, 0.15)),
            Mark(2, "box", 0.38, 0.22, 0.76, 0.52, color="red", at=(0.78, 0.54)),
            Mark(3, "circle", 0.70, 0.20, 0.80, 0.30, color="blue", at=(0.86, 0.15)),
        ),
    ),
    text_w=4.0,
    picture_extra=0.1,
    notes=(
        "Read the gap up, the isolated bars, then the gap down.",
        "Gap meaning points back to Chapter 3. The prices and volume are ours, invented.",
    ),
    origin="Lim (2016), pp. 223 to 224. Chart RC is ours, with invented PHP bars and volume; gap meaning points to Chapter 3.",
)

ISLAND_READ = Pair(
    left=Content(
        title="Figure 7.23: the book's island context",
        lines=(
            "Gap keeps Chapter 3 meaning in ‘Gaps’. Mark 1 is the gap up, mark 2 the island, and mark 3 the gap down.",
            "The book observes low volume [4] and an overbought stochastic label [5], calling low volume lack of conviction.",
            "No stochastic method is given in Chapter 7. These labels are context; the island is a potential warning.",
        ),
        accent="The two gaps do the defining work; volume and stochastic are supporting context.",
    ),
    picture=ISLAND_FIGURE,
    text_w=6.4,
    notes=ISLAND_FIGURE.notes,
    origin=ISLAND_FIGURE.origin,
)

ISLAND_CHECK = Check(
    label="From the island reversal reading",
    questions=(
        Q(
            stem="What isolates an island reversal?",
            options=(
                "A gap up followed by a gap down",
                "A single wide bar",
                "A high-volume middle bar",
                "A trendline only",
            ),
            answer="A",
            reason="Figure 7.23 shows a gap up before and a gap down after the island.",
        ),
        Q(
            stem="What is the stochastic label here?",
            options=(
                "As the island definition",
                "As a formula taught in this chapter",
                "As supporting context; Chapter 7 gives no method",
                "As a guaranteed reversal signal",
            ),
            answer="C",
            reason="It is supporting context; Chapter 7 gives no method.",
        ),
    ),
    picture=ISLAND_FIGURE,
    text_w=5.0,
    layout="beside",
    notes=(
        "Let students answer from the preceding island slides. The two gaps define the formation; the stochastic label is not a Chapter 7 formula.",
    ),
    origin="Questions are ours and answerable from the preceding Figure 7.23 teaching slides.",
)

def _book_figure(number, title, aspect, shows, marks, notes, page, crop=()):
    return Figure(
        title=title,
        number=number,
        aspect=aspect,
        crop=crop,
        marks=marks,
        shows=shows,
        notes=notes,
        origin=(f"Lim (2016), p. {page}, Figure {number}. The crop and marks "
                "are for teaching; the worked PHP values are ours, invented."),
    )


OUTSIDE_FIGURE = _book_figure(
    "7.24", "Figure 7.24: an outside bar contains the prior bars", 672 / 404,
    "ITC Holdings daily chart. The marked outside bar contains 11 preceding "
    "bars, breaks the uptrend line, and closes near its low.",
    (
        Mark(1, "box", 0.35, 0.08, 0.54, 0.42, color="gold", at=(0.29, 0.06)),
        Mark(2, "line", 0.54, 0.08, 0.54, 0.42, color="red", at=(0.60, 0.22)),
        Mark(3, "circle", 0.49, 0.34, 0.55, 0.41, color="blue", at=(0.60, 0.46)),
    ),
    (
        "Point first to the 11 contained bars, then to the outside high and low.",
        "The book says a trendline violation with the bearish breakout should be a reliable short-entry signal.",
    ),
    224,
)

OUTSIDE_FULL_FIGURE = _book_figure(
    "7.24", "Figure 7.24: outside bar and trendline violation", 672 / 404,
    "ITC Holdings daily chart. The marked outside bar contains 11 preceding "
    "bars, breaks the uptrend line, and closes near its low.",
    (
        Mark(1, "box", 0.35, 0.08, 0.54, 0.42, color="gold", at=(0.29, 0.06)),
        Mark(2, "circle", 0.52, 0.25, 0.58, 0.39, color="red", at=(0.60, 0.22)),
        Mark(3, "circle", 0.52, 0.36, 0.58, 0.44, color="blue", at=(0.61, 0.47)),
    ),
    (
        "Gold [1] marks the 11 preceding bars contained in the outside range.",
        "Red [2] marks the trendline violation at the outside-bar break. Blue [3] marks the bearish close near the low.",
    ),
    224,
)

INSIDE_FIGURE = _book_figure(
    "7.25", "Figure 7.25: two inside bars test resistance", 672 / 402,
    "ITC Holdings daily chart. Two inside-bar reversals test the same resistance; "
    "the lower panel labels bearish StochRSI divergence.",
    (
        Mark(1, "circle", 0.55, 0.18, 0.63, 0.31, color="gold", at=(0.48, 0.14)),
        Mark(2, "circle", 0.64, 0.17, 0.72, 0.30, color="red", at=(0.77, 0.15)),
        Mark(3, "circle", 0.66, 0.75, 0.75, 0.87, color="blue", at=(0.82, 0.88)),
    ),
    (
        "The two dark bars are the inside-bar reversals at the same resistance.",
        "The figure labels the oscillator as StochRSI and shows bearish divergence; this deck does not define its formula.",
    ),
    225,
)

LOWER_INSIDE_FIGURE = _book_figure(
    "7.26", "Figure 7.26: lower inside bars and an outside bar", 701 / 310,
    "Silver Wheaton daily chart. Three successively lower inside bars form below "
    "the lower band, followed by a bearish outside bar.",
    (
        Mark(1, "box", 0.43, 0.69, 0.57, 0.96, color="gold", at=(0.36, 0.65)),
        Mark(2, "line", 0.35, 0.78, 0.58, 0.78, color="red", at=(0.30, 0.83)),
        Mark(3, "circle", 0.77, 0.19, 0.86, 0.34, color="blue", at=(0.90, 0.18)),
    ),
    (
        "Read the three nested bars from left to right, then the later outside bar.",
        "The book says the exhaustion reading is especially strong when the declines also have bearish volume.",
    ),
    225,
)

COMBINED_FIGURE = _book_figure(
    "7.27", "Figure 7.27: inside, outside, and three-bar reversals", 800 / 487,
    "Alacer Gold daily chart. The marked examples show inside, outside, and "
    "three-bar reversals aligned with stochastic overbought or oversold readings.",
    (
        Mark(1, "circle", 0.24, 0.16, 0.31, 0.29, color="gold", at=(0.20, 0.13)),
        Mark(2, "circle", 0.70, 0.25, 0.77, 0.38, color="red", at=(0.83, 0.22)),
        Mark(3, "circle", 0.56, 0.52, 0.63, 0.68, color="blue", at=(0.67, 0.71)),
    ),
    (
        "The figure places three named reversal families on one chart.",
        "This slide names the three price-bar families; the indicator panels are outside this slide's scope.",
    ),
    226,
)

EXHAUSTION_FIGURE = _book_figure(
    "7.28", "Figure 7.28: a bullish exhaustion bar at a bottom", 701 / 312,
    "J.P. Morgan Chase daily chart. The marked exhaustion bar forms a bottom; "
    "the preceding gap and later rebound show the context.",
    (
        Mark(1, "circle", 0.50, 0.52, 0.56, 0.61, color="gold", at=(0.46, 0.50)),
        Mark(2, "box", 0.53, 0.55, 0.59, 0.71, color="red", at=(0.64, 0.52)),
        Mark(3, "arrow", 0.61, 0.82, 0.78, 0.40, color="blue", at=(0.82, 0.36)),
    ),
    (
        "The marked bar is the bullish converse of the uptrend case: it closes near its high in a downtrend.",
        "There is a gap before the marked bar in this figure, but the book's rule concerns no gap between an exhaustion bar and the subsequent bar.",
    ),
    226,
)

EXHAUSTION_COMPARE_FIGURE = _book_figure(
    "7.28", "Figure 7.28: compare the exhaustion reading", 701 / 312,
    "J.P. Morgan Chase daily chart. The crop keeps the bullish exhaustion bar "
    "and its following bar readable for the comparison.",
    (
        Mark(1, "circle", 0.50, 0.52, 0.56, 0.61, color="gold", at=(0.46, 0.50)),
        Mark(2, "circle", 0.53, 0.54, 0.59, 0.61, color="red", at=(0.64, 0.51)),
        Mark(3, "line", 0.56, 0.60, 0.63, 0.60, color="blue", at=(0.68, 0.68)),
    ),
    (
        "Gold [1] marks the exhaustion bar's open context, red [2] its close near the trend-side extreme, and blue [3] the no-gap relationship to the following bar.",
        "The crop is read with the invented numbers on the left, not as a second definition of the pattern.",
    ),
    226,
)

SPIKE_FIGURE = _book_figure(
    "7.29", "Figure 7.29: a wide, high-volume emotion spike", 701 / 428,
    "Mad Catz Interactive daily chart. A wide price spike occurs on high volume "
    "and a three-bar bearish reversal forms near the top.",
    (
        Mark(1, "circle", 0.40, 0.20, 0.47, 0.53, color="gold", at=(0.36, 0.17)),
        Mark(2, "circle", 0.42, 0.80, 0.48, 0.95, color="red", at=(0.53, 0.96)),
        Mark(3, "circle", 0.74, 0.06, 0.82, 0.20, color="blue", at=(0.87, 0.14)),
    ),
    (
        "The price panel shows the wide spike; the lower panel shows its high volume.",
        "Lim also identifies a typical three-bar bearish reversal at the top of the move.",
    ),
    227,
)

PIN_FIGURE = _book_figure(
    "7.30", "Figure 7.30: a bullish pin bar breaches support", 750 / 329,
    "Micron Technology daily chart. The marked pin bar penetrates support and "
    "then retraces above the level.",
    (
        Mark(1, "line", 0.08, 0.86, 0.70, 0.86, color="gold", at=(0.05, 0.92)),
        Mark(2, "circle", 0.19, 0.84, 0.24, 0.93, color="red", at=(0.16, 0.95)),
        Mark(3, "circle", 0.19, 0.45, 0.25, 0.56, color="blue", at=(0.29, 0.41)),
    ),
    (
        "Mark 1 is the support barrier, mark 2 the penetration, and mark 3 the rapid retrace.",
        "The book says pin bars are usually breakouts formed on low volume.",
    ),
    227,
)

FALSE_ONE_FIGURE = _book_figure(
    "7.31", "Figure 7.31: a false upside breakout", 401 / 337,
    "Bearish non-failure swing. Price breaks above resistance, returns below it, "
    "and creates a short entry with a stop above the breakout high.",
    (
        Mark(1, "line", 0.07, 0.10, 0.60, 0.10, color="gold", at=(0.08, 0.20)),
        Mark(2, "circle", 0.29, 0.03, 0.36, 0.12, color="red", at=(0.26, 0.18)),
        Mark(3, "circle", 0.36, 0.10, 0.42, 0.18, color="blue", at=(0.48, 0.14)),
        Mark(4, "line", 0.27, 0.03, 0.42, 0.03, color="purple", at=(0.20, 0.04)),
    ),
    (
        "Lim calls this a non-failure swing and attributes the setup to a 2B entry.",
        "The short begins after the close returns below resistance; the stop sits just above the breakout high.",
    ),
    228,
)

FALSE_BOTH_FIGURE = _book_figure(
    "7.32", "Figure 7.32: false breakouts in both directions", 676 / 347,
    "Silver daily chart. The marked examples return through resistance for shorts "
    "or through support for longs.",
    (
        Mark(1, "circle", 0.29, 0.23, 0.36, 0.34, color="gold", at=(0.25, 0.20)),
        Mark(2, "circle", 0.53, 0.46, 0.61, 0.59, color="red", at=(0.67, 0.66)),
        Mark(3, "circle", 0.33, 0.29, 0.39, 0.37, color="blue", at=(0.43, 0.39)),
        Mark(4, "circle", 0.77, 0.57, 0.84, 0.68, color="purple", at=(0.89, 0.53)),
    ),
    (
        "Read the two directions separately: short below resistance after a false upside break, long above support after a false downside break.",
        "The book does not give a complete trade plan beyond these entry and stop descriptions.",
    ),
    229,
)

REPO_FIGURE = _book_figure(
    "7.33", "Figure 7.33: DiNapoli's Double Repo", 800 / 357,
    "Continuous daily sugar chart. The marked sequence crosses a forward-shifted "
    "three-day SMA twice before the rapid decline.",
    (
        Mark(1, "circle", 0.38, 0.20, 0.44, 0.29, color="gold", at=(0.35, 0.17)),
        Mark(2, "circle", 0.50, 0.20, 0.56, 0.29, color="red", at=(0.60, 0.17)),
        Mark(3, "arrow", 0.59, 0.40, 0.77, 0.68, color="blue", at=(0.81, 0.72)),
    ),
    (
        "The two crossings are the pattern's named structure; the later decline is the observed follow-through.",
        "Lim directs readers to DiNapoli's original text for a complete discussion.",
    ),
    229,
)

REPO_LIMITS_FIGURE = _book_figure(
    "7.33", "Figure 7.33: Double Repo conditions", 800 / 357,
    "Continuous daily sugar chart. The marked sequence crosses a forward-shifted "
    "three-day SMA twice before the rapid decline.",
    (
        Mark(1, "line", 0.53, 0.22, 0.73, 0.34, color="gold", at=(0.76, 0.18)),
        Mark(2, "circle", 0.20, 0.18, 0.40, 0.30, color="red", at=(0.17, 0.14)),
        Mark(3, "box", 0.39, 0.04, 0.55, 0.27, color="blue", at=(0.60, 0.05)),
    ),
    (
        "Gold [1] marks the forward-shifted three-day SMA. Red [2] marks the long bullish run before the pattern.",
        "Blue [3] marks the topping formation, which the book limits to eight to ten bars.",
    ),
    229,
)

HIKKAKE_FIGURE = _book_figure(
    "7.34", "Figure 7.34: bullish and bearish Hikkake", 604 / 281,
    "Schematic bullish and bearish Hikkake patterns. Each takes the opposite "
    "re-entry after an inside-bar breakout fails.",
    (
        Mark(1, "box", 0.13, 0.27, 0.29, 0.70, color="gold", at=(0.09, 0.23)),
        Mark(2, "circle", 0.68, 0.27, 0.80, 0.47, color="red", at=(0.84, 0.23)),
        Mark(3, "arrow", 0.77, 0.52, 0.91, 0.72, color="blue", at=(0.92, 0.78)),
    ),
    (
        "The left schematic is bullish after a failed downside breakout; the right is bearish after a failed upside breakout.",
        "Only the re-entry opposite the failed breakout is taken, and it must occur within three bars.",
    ),
    230,
)

BULLISH_HIKKAKE_FIGURE = _book_figure(
    "7.34", "Figure 7.34: bullish Hikkake", 604 / 281,
    "The bullish schematic: an inside bar, a failed downside breakout, and the "
    "opposite re-entry above the inside high.",
    (
        Mark(1, "box", 0.26, 0.27, 0.58, 0.70, color="gold", at=(0.18, 0.22)),
        Mark(2, "circle", 0.46, 0.53, 0.56, 0.72, color="red", at=(0.64, 0.75)),
        Mark(3, "arrow", 0.73, 0.48, 0.86, 0.25, color="blue", at=(0.91, 0.20)),
    ),
    (
        "Gold [1] marks the inside bar, red [2] the failed downside breakout, and blue [3] the bullish re-entry above the inside high.",
        "Only the opposite re-entry is taken, and it must occur within three bars.",
    ),
    230, crop=(0.0, 0.0, 0.50, 0.0),
)

BEARISH_HIKKAKE_FIGURE = _book_figure(
    "7.34", "Figure 7.34: bearish Hikkake", 604 / 281,
    "The bearish schematic: an inside bar, a failed upside breakout, and the "
    "opposite re-entry below the inside low.",
    (
        Mark(1, "box", 0.10, 0.27, 0.34, 0.70, color="gold", at=(0.04, 0.22)),
        Mark(2, "circle", 0.36, 0.27, 0.60, 0.47, color="red", at=(0.66, 0.22)),
        Mark(3, "arrow", 0.54, 0.52, 0.82, 0.72, color="blue", at=(0.91, 0.80)),
    ),
    (
        "Gold [1] marks the inside bar, red [2] the failed upside breakout, and blue [3] the bearish re-entry below the inside low.",
        "Only the opposite re-entry is taken, and it must occur within three bars.",
    ),
    230, crop=(0.50, 0.0, 0.0, 0.0),
)

HIKKAKE_EXAMPLE_FIGURE = _book_figure(
    "7.35", "Figure 7.35: a bullish Hikkake at a bottom", 622 / 513,
    "iShares Emerging Markets daily chart. A bullish Hikkake forms at a linear "
    "regression channel bottom.",
    (
        Mark(1, "box", 0.42, 0.42, 0.50, 0.56, color="gold", at=(0.37, 0.40)),
        Mark(2, "circle", 0.47, 0.52, 0.52, 0.63, color="red", at=(0.56, 0.66)),
        Mark(3, "arrow", 0.52, 0.58, 0.58, 0.38, color="blue", at=(0.62, 0.34)),
    ),
    (
        "The figure includes indicator panels, but this slide does not interpret their formulas.",
        "Read the formation, failed downside breakout, and upside re-entry only.",
    ),
    230,
)

OUTSIDE_CHART = Chart(
    letter="SA",
    title="Outside bar: an invented containment example",
    shows="Three invented PHP bars. The third range contains the first two and closes near its low on high volume.",
    tier="core",
    marks=(
        Mark(1, "box", 0.55, 0.18, 0.69, 0.62, color="gold", at=(0.50, 0.13)),
        Mark(2, "circle", 0.61, 0.18, 0.70, 0.28, color="red", at=(0.76, 0.18)),
        Mark(3, "circle", 0.61, 0.55, 0.70, 0.68, color="blue", at=(0.77, 0.73)),
    ),
    notes=(
        "The first two bars run from PHP 48.00 to PHP 52.00. The outside bar runs from PHP 47.00 to PHP 53.00 and closes at PHP 47.50.",
        "Its 5.0 million volume is invented to show the book's high-volume reliability condition.",
    ),
    origin="Chart SA is ours, with invented PHP bars and million-share volume.",
)

INSIDE_CHART = Chart(
    letter="SB",
    title="Inside bar: an invented quiet reversal",
    shows="Two invented PHP bars at resistance. The second bar stays inside the first and has much lower volume.",
    tier="core",
    marks=(
        Mark(1, "box", 0.35, 0.18, 0.56, 0.76, color="gold", at=(0.27, 0.13)),
        Mark(2, "box", 0.61, 0.31, 0.72, 0.64, color="red", at=(0.77, 0.28)),
        Mark(3, "line", 0.28, 0.20, 0.77, 0.20, color="blue", at=(0.80, 0.14)),
    ),
    notes=(
        "The first bar is O 50.00, H 53.00, L 48.00, C 52.40 on 4.5 million shares.",
        "The second is O 51.80, H 52.50, L 49.20, C 50.10 on 0.5 million shares. It stays inside the first range.",
    ),
    origin="Chart SB is ours, with invented PHP bars and million-share volume.",
)

SPIKE_CHART = Chart(
    letter="SC",
    title="Emotion spike: a wide bar on high volume",
    shows="Six invented PHP bars. The third bar is much wider and carries much higher volume, followed by a bearish three-bar reversal.",
    tier="reinforcement",
    marks=(
        Mark(1, "box", 0.45, 0.14, 0.57, 0.56, color="gold", at=(0.39, 0.10)),
        Mark(2, "circle", 0.45, 0.72, 0.57, 0.88, color="red", at=(0.64, 0.92)),
        Mark(3, "box", 0.58, 0.28, 0.92, 0.66, color="blue", at=(0.94, 0.20)),
    ),
    notes=(
        "The ordinary bars have a PHP 3.0 range and 1.5 million shares. The spike has an 8.0 range and 6.0 million shares.",
        "The numbers are invented to make Lim's wide-range and high-volume description visible.",
    ),
    origin="Chart SC is ours, with invented PHP bars and million-share volume.",
)

FALSE_CHART = Chart(
    letter="SD",
    title="False breakouts: return through the barrier",
    shows="Two invented cases. The upper case breaks PHP 60.00 and closes at 59.40; the lower case breaks PHP 40.00 and closes at 40.60.",
    tier="core",
    marks=(
        Mark(1, "circle", 0.30, 0.20, 0.36, 0.30, color="gold", at=(0.28, 0.16)),
        Mark(2, "circle", 0.79, 0.84, 0.87, 0.95, color="red", at=(0.72, 0.96)),
        Mark(3, "circle", 0.30, 0.54, 0.36, 0.64, color="blue", at=(0.42, 0.52)),
        Mark(4, "circle", 0.79, 0.53, 0.87, 0.63, color="purple", at=(0.91, 0.50)),
    ),
    notes=(
        "The upper barrier is resistance at PHP 60.00; the false high is PHP 62.00 and the short close is PHP 59.40.",
        "The lower barrier is support at PHP 40.00; the false low is PHP 38.50 and the long close is PHP 40.60.",
    ),
    origin="Chart SD is ours, with invented PHP barriers and closes.",
)

FALSE_OWN_CHART = Chart(
    letter="SE",
    title="Figure 7.31: own course drawing",
    shows="A large invented two-bar false upside breakout with resistance, return, and stop values written on the drawing.",
    tier="core",
    marks=(
        Mark(1, "line", 0.18, 0.43, 0.82, 0.43, color="gold", at=(0.12, 0.36)),
        Mark(2, "circle", 0.61, 0.14, 0.74, 0.28, color="red", at=(0.80, 0.10)),
        Mark(3, "circle", 0.61, 0.47, 0.74, 0.59, color="blue", at=(0.82, 0.63)),
        Mark(4, "line", 0.61, 0.20, 0.74, 0.20, color="purple", at=(0.82, 0.12)),
    ),
    notes=(
        "The course drawing labels resistance PHP 60.00, high PHP 62.00, close PHP 59.40, and stop PHP 62.20.",
        "The book's drawing follows on its own slide.",
    ),
    origin="Chart SE is ours, with invented PHP values; the book's drawing is shown separately.",
)

REPO_CHART = Chart(
    letter="SF",
    title="Double Repo: two crossings of a three-day SMA",
    shows="Invented closes cross a forward-shifted three-day SMA twice after nine bullish days, then decline.",
    tier="reinforcement",
    marks=(
        Mark(1, "circle", 0.64, 0.28, 0.70, 0.40, color="gold", at=(0.60, 0.22)),
        Mark(2, "circle", 0.70, 0.48, 0.76, 0.60, color="red", at=(0.78, 0.62)),
        Mark(3, "box", 0.73, 0.28, 0.82, 0.60, color="blue", at=(0.86, 0.22)),
    ),
    notes=(
        "The forward-shifted three-day SMA is PHP 50.00. Invented closes cross above at 50.80, below at 49.60, then repeat after nine bullish days.",
        "The book says the full method belongs in DiNapoli's original text, so this chart teaches only the named Chapter 7 structure.",
    ),
    origin="Chart SF is ours, with invented PHP closes and a three-day SMA.",
)

HIKKAKE_CHART = Chart(
    letter="SG",
    title="Hikkake: failed breakout, opposite re-entry",
    shows="Two invented inside-bar cases. The breakout fails and the entry is taken only in the opposite direction within three bars.",
    tier="core",
    marks=(
        Mark(1, "box", 0.10, 0.32, 0.20, 0.76, color="gold", at=(0.07, 0.27)),
        Mark(2, "circle", 0.22, 0.15, 0.30, 0.34, color="red", at=(0.34, 0.13)),
        Mark(3, "arrow", 0.66, 0.58, 0.75, 0.82, color="blue", at=(0.64, 0.70)),
    ),
    notes=(
        "In the bearish case, the inside high is PHP 52.00, the false high is PHP 53.00, and the short re-entry is below PHP 49.00.",
        "The bullish converse uses an inside low of PHP 40.00, a false low of PHP 39.20, and an upside re-entry at PHP 41.00.",
    ),
    origin="Chart SG is ours, with invented PHP levels and entries.",
)

HIKKAKE_OWN_CHART = Chart(
    letter="SH",
    title="Figure 7.34: own course drawings",
    shows="Large invented bullish and bearish Hikkake drawings with inside levels, failed breakouts, and opposite re-entries written on the bars.",
    tier="core",
    marks=(
        Mark(1, "box", 0.16, 0.25, 0.29, 0.72, color="gold", at=(0.10, 0.20)),
        Mark(2, "circle", 0.31, 0.61, 0.39, 0.77, color="red", at=(0.43, 0.82)),
        Mark(3, "circle", 0.42, 0.27, 0.50, 0.41, color="blue", at=(0.51, 0.20)),
        Mark(4, "box", 0.67, 0.25, 0.79, 0.72, color="gold", at=(0.63, 0.20)),
        Mark(5, "circle", 0.80, 0.14, 0.88, 0.29, color="red", at=(0.92, 0.10)),
        Mark(6, "circle", 0.80, 0.61, 0.88, 0.77, color="blue", at=(0.91, 0.55)),
    ),
    notes=(
        "Left: inside high 43.00, inside low 40.00, false low 39.00, long re-entry at 43.00.",
        "Right: inside high 52.00, inside low 49.00, false high 53.00, short re-entry at 49.00.",
    ),
    origin="Chart SH is ours, with invented PHP values; the book's drawing is shown separately.",
)


OUTSIDE_CHECK = Check(
    label="From outside bars",
    questions=(
        Q(
            stem="What must a bearish outside bar's range contain?",
            options=("Only the current bar's body", "One or more prior bars", "A gap on both sides", "Only the volume bars"),
            answer="B",
            reason="It engulfs preceding bars (Lim, p. 223).\n",
        ),
        Q(
            stem="Which close is more reliable for a bearish outside-bar reading?",
            options=("A close near the low", "A close near the middle", "A close near the high", "The close does not matter"),
            answer="A",
            reason="Lim says closes near the low are generally more reliable for the bearish reading (p. 223).",
        ),
    ),
    picture=OUTSIDE_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Answer from the preceding outside-bar definition and marked figure.",),
    origin="Questions are ours and answerable from the preceding outside-bar slides.",
)

INSIDE_IDEAL_CHECK = Check(
    label="From ideal inside bars",
    questions=(
        Q(
            stem="Which bar should be wide in an ideal inside reversal?",
            options=("The first bar", "The second bar", "Neither bar", "Only the volume bar"),
            answer="A",
            reason="Lim says the first bar should be wide (p. 224).",
        ),
        Q(
            stem="Which bar should have very low volume?",
            options=("The first bar", "The second bar", "Both bars", "The resistance line"),
            answer="B",
            reason="Lim says the second bar should be narrow on very low volume (p. 224).",
        ),
    ),
    picture=INSIDE_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Keep the marked two tests visible while the room answers.",),
    origin="Questions are ours and answerable from Lim (2016), p. 224.",
)

COMBINED_CHECK = Check(
    label="From the reversal families",
    questions=(
        Q(
            stem="Is every inside bar a Harami?",
            options=("No; Harami has a stricter one-fourth to one-third proportion", "Yes; the terms are identical", "Only on high volume", "Only below support"),
            answer="A",
            reason="Lim keeps inside bar and Harami rules separate; Harami has the stricter proportion (p. 226).",
        ),
        Q(
            stem="What proportion does the book give for a Harami body?",
            options=("One-half to two-thirds", "One-fourth to one-third", "One to two points", "No proportion"),
            answer="B",
            reason="The book gives one-fourth to one-third of the preceding candlestick range (p. 226).",
        ),
    ),
    picture=COMBINED_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("The figure stays visible while the check tests the stricter Harami distinction.",),
    origin="Questions are ours and answerable from Lim (2016), p. 226.",
)

ISLAND_CHECK = Check(
    label="From island, outside, and inside bars",
    questions=(
        Q(
            stem="What isolates an island reversal?",
            options=("One wide bar", "A resistance line", "A gap up followed by a gap down", "Very low volume only"),
            answer="C",
            reason="The island is isolated by a gap up and a later gap down (Lim, p. 223).",
        ),
        Q(
            stem="Which volume pairing is ideal for an inside reversal?",
            options=("Narrow first, high second", "Wide and high-volume first, narrow and very-low-volume second", "Both low", "Both high"),
            answer="B",
            reason="The first bar should be wide on high volume and the second narrow on very low volume (Lim, p. 224).",
        ),
    ),
    picture=INSIDE_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("The island answer is supplied by the earlier Figure 7.23 slide; keep the approved Figure 7.25 crop readable.",),
    origin="Questions are ours and answerable from Lim (2016), pp. 223 to 224.",
)

EXHAUSTION_CHECK = Check(
    label="From exhaustion and pin bars",
    questions=(
        Q(
            stem="What separates an exhaustion bar from a pin bar?",
            options=("Exhaustion uses no trend context", "A pin bar gives a false barrier-penetration impression", "A pin bar must gap from the next bar", "Exhaustion is always narrow"),
            answer="B",
            reason="Lim says exhaustion bars do not usually provide a false impression of penetrating a barrier, while pin bars do (p. 227).",
        ),
        Q(
            stem="Pin bars usually form on:",
            options=("High volume", "The same volume as the prior bar", "Low volume", "No volume data"),
            answer="C",
            reason="Lim says pin bars are usually breakouts that form on low volume (p. 227).",
        ),
    ),
    picture=EXHAUSTION_COMPARE_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("The key difference is the false impression of breaking a barrier. The pin-bar volume tendency is a separate book statement.",),
    origin="Questions are ours and answerable from the preceding exhaustion and pin-bar slides.",
)

REVERSAL_CHECK = Check(
    label="From false breakouts and Hikkake",
    questions=(
        Q(
            stem="After a false upside breakout, the bearish entry is:",
            options=("At the new high", "Above support", "Only after a gap down", "At a close below resistance"),
            answer="D",
            reason="The book says a short is normally initiated when price closes below resistance after the false upside breakout (p. 229).",
        ),
        Q(
            stem="A Hikkake opposite re-entry must occur within:",
            options=("One bar", "Two bars", "Three bars", "Ten bars"),
            answer="C",
            reason="Lim says the breakout must occur within three bars of the initial failed breakout (p. 230).",
        ),
    ),
    picture=BEARISH_HIKKAKE_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Read the two directions separately, then reveal the timing rule.",),
    origin="Questions are ours and answerable from the preceding false-breakout and Hikkake slides.",
)

EXHAUSTION_FIGURE_CHECK = Check(
    label="From the exhaustion figure",
    questions=(
        Q(
            stem="What does the next bar help distinguish in an exhaustion reading?",
            options=("Whether the next bar gaps away", "Whether volume is absent", "Whether resistance is horizontal", "Whether the bar is an inside bar"),
            answer="A",
            reason="Lim requires no gap between the exhaustion bar and the subsequent bar (p. 226).",
        ),
        Q(
            stem="Where is the bullish exhaustion converse more reliable?",
            options=("At the top of a downtrend", "Only in a flat market", "Only above resistance", "At the bottom of a downtrend"),
            answer="D",
            reason="The bullish converse appears in a downtrend at a bottom (p. 226).",
        ),
    ),
    picture=EXHAUSTION_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Keep the gap and later rebound marks visible while the room answers.",),
    origin="Questions are ours and answerable from Lim (2016), p. 226.",
)

PIN_FIGURE_CHECK = Check(
    label="From the pin-bar figure",
    questions=(
        Q(
            stem="What does a pin bar penetrate during the interval?",
            options=("A volume average", "A prior close only", "A stochastic formula", "A barrier such as support or resistance"),
            answer="D",
            reason="Lim describes a pin bar as penetrating a barrier and then retracing (p. 227).",
        ),
        Q(
            stem="What does the rapid retrace imply?",
            options=("The barrier break is certain", "The apparent breakout may be false", "The trend must continue", "The volume is high"),
            answer="B",
            reason="The retrace shows that the initial impression of breaking the barrier was false (p. 227).",
        ),
    ),
    picture=PIN_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Keep support, penetration, and close-back-above marks visible.",),
    origin="Questions are ours and answerable from Lim (2016), p. 227.",
)

FALSE_BREAKOUT_CHECK = Check(
    label="From false breakouts",
    questions=(
        Q(
            stem="After a false upside breakout, the bearish entry is:",
            options=("At a close below resistance", "At the new high", "Only after a gap down", "Above support"),
            answer="A",
            reason="The short is normally initiated when price closes below resistance after the false upside breakout (p. 229).",
        ),
        Q(
            stem="After a false downside breakout, the bullish entry is:",
            options=("Below support", "At the false low", "Only after a gap up", "At a close above support"),
            answer="D",
            reason="The opposite entry is taken when price closes back above support after the false downside breakout (p. 229).",
        ),
    ),
    picture=FALSE_BOTH_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Keep both barrier directions visible; the question asks for the returned closes.",),
    origin="Questions are ours and answerable from Lim (2016), p. 229.",
)

REPO_LIMITS_CHECK = Check(
    label="From Double Repo limits",
    questions=(
        Q(
            stem="How many crossing pairs generate the named Double Repo sell signal?",
            options=("One pair", "Three pairs", "Two pairs", "No pairs"),
            answer="C",
            reason="The named bearish Double Repo has two closes above and below the forward-shifted SMA (p. 229).",
        ),
        Q(
            stem="Where does Lim place the complete Double Repo method?",
            options=("DiNapoli's original text", "The volume panel", "The Hikkake figure", "No source"),
            answer="A",
            reason="Lim sends readers to DiNapoli's original text for the detailed method (p. 229).",
        ),
    ),
    picture=REPO_LIMITS_FIGURE,
    text_w=5.5,
    layout="beside",
    notes=("Keep the SMA, bullish-day run, and topping formation marks visible.",),
    origin="Questions are ours and answerable from Lim (2016), p. 229.",
)

HIKKAKE_EXAMPLE_CHECK = Check(
    label="From the Hikkake example",
    questions=(
        Q(
            stem="Within how many bars must the opposite Hikkake re-entry occur?",
            options=("One bar", "Three bars", "Eight bars", "Ten bars"),
            answer="B",
            reason="Lim says the breakout must occur within three bars of the initial failed breakout (p. 230).",
        ),
        Q(
            stem="Which direction is taken after the initial Hikkake failure?",
            options=("The failed direction", "No direction", "The opposite direction", "Only the trend direction"),
            answer="C",
            reason="Hikkake takes the opposite re-entry after the inside-bar breakout fails (p. 230).",
        ),
    ),
    picture=HIKKAKE_EXAMPLE_FIGURE,
    text_w=5.45,
    layout="beside",
    notes=("Keep the marked formation, failed downside breakout, and upside re-entry visible.",),
    origin="Questions are ours and answerable from Lim (2016), p. 230.",
)


B4_SLIDES = (
    Content(
        title="Outside bar: containment and direction",
        lines=(
            "We now turn from key reversals to containment: an outside bar engulfs preceding bars.",
            "Ours: prior 48.00 to 52.00; outside 47.00 to 53.00; close 47.50 near low.",
            "Larger range and more contained bars generally strengthen; near-edge close and high volume add reliability (pp. 223 to 224).",
            "Continuation is possible when the close follows the existing trend (p. 223).",
        ),
        accent="Trendline break plus bearish outside bar can support a short.",
        notes=("Define containment before naming direction. Keep the book's generally and can qualifiers.", "The next chart puts the invented values on the bars."),
        origin="Lim (2016), pp. 223 to 224. The worked PHP values are ours, invented.",
    ),
    OUTSIDE_CHART,
    Pair(
        left=Content(
            title="Figure 7.24: the outside bar read",
            lines=(
                "Lim defines it: “Outside bars are bars that engulf one or more preceding bars.” (Lim, p. 223).",
                "Gold [1] marks the 11 bars contained inside the outside range. Red [2] marks the outside bar's high-to-low range.",
                "Blue [3] marks the close near the low. Meaning/action: a bearish outside bar can support a short entry.",
            ),
            notes=(),
        ),
        picture=OUTSIDE_FIGURE,
        text_w=5.55,
        notes=OUTSIDE_FIGURE.notes,
        origin=OUTSIDE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.24: the outside bar's break",
            lines=(
                "The same figure keeps the context visible: the marked outside bar contains 11 preceding bars.",
                "Gold [1] marks those contained bars. Red [2] marks the trendline violation at the outside-bar break.",
                "Blue [3] marks the bearish close near the low. Meaning/action: use the break and close together, not either mark alone.",
            ),
            notes=(),
        ),
        picture=OUTSIDE_FULL_FIGURE,
        text_w=5.55,
        notes=OUTSIDE_FULL_FIGURE.notes,
        origin=OUTSIDE_FULL_FIGURE.origin,
    ),
    OUTSIDE_CHECK,
    Content(
        title="Inside bar: quiet containment",
        lines=(
            "We keep the containment idea and reverse it: an inside bar stays within the preceding bar's high and low.",
            "Ours: first range 48.00 to 53.00 on 4.5m; second range 49.20 to 52.50 on 0.5m.",
            "Reliable case: wide, high-volume first bar; narrow, very-low-volume second bar.",
            "The same resistance is tested in the next figure, then lower bars add exhaustion context.",
        ),
        accent="Inside means containment. It is not Harami.",
        notes=("Keep inside bar separate from outside bar: the second bar is contained rather than engulfing.", "The next chart shows the volume contrast."),
        origin="Lim (2016), p. 224. The worked PHP values are ours, invented.",
    ),
    INSIDE_CHART,
    Pair(
        left=Content(
            title="Figure 7.25: inside bars at resistance",
            lines=(
                "Lim says inside bars are considered reversal bars. The first should be wide on high volume; the second narrow on very low volume (p. 224).",
                "Gold [1] and red [2] mark the two inside-bar reversals testing one resistance level.",
                "Blue [3] marks bearish StochRSI divergence. Meaning/action: repeated failure at resistance warns of a possible reversal; no oscillator formula is taught here.",
            ),
            notes=(),
        ),
        picture=INSIDE_FIGURE,
        text_w=5.5,
        notes=INSIDE_FIGURE.notes,
        origin=INSIDE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.25: volume and resistance",
            lines=(
                "Read the two tests again, this time with the book's volume condition.",
                "Gold [1] and red [2] are the two inside-bar reversals at one resistance. Blue [3] is the figure's bearish StochRSI divergence.",
                "Meaning/action: prefer the wide, high-volume first bar and narrow, very-low-volume second bar, but keep the oscillator reading contextual.",
            ),
            notes=(),
        ),
        picture=INSIDE_FIGURE,
        text_w=5.5,
        notes=INSIDE_FIGURE.notes,
        origin=INSIDE_FIGURE.origin,
    ),
    INSIDE_IDEAL_CHECK,
    Pair(
        left=Content(
            title="Figure 7.26: lower inside bars",
            lines=(
                "Gold [1] marks three successively lower inside bars below the lower band. Red [2] marks the band context.",
                "Blue [3] marks the later bearish outside bar. Lim says the exhaustion reading is stronger when declines also show bearish volume (p. 225).",
                "Meaning/action: lower inside bars can warn of exhaustion, but the book leaves the volume judgement contextual.",
            ),
            notes=(),
        ),
        picture=LOWER_INSIDE_FIGURE,
        text_w=5.5,
        notes=LOWER_INSIDE_FIGURE.notes,
        origin=LOWER_INSIDE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.27: three reversal families together",
            lines=(
                "Gold [1] is an inside-bar reversal; red [2] an outside-bar reversal; blue [3] a three-bar reversal.",
                "Ours: inside range 6.0 points; outside bar contains four bars; outer volumes 4.0m and 4.2m.",
                "This slide names the three price-bar families; the indicator panels are outside this slide's scope.",
            ),
            notes=(),
        ),
        picture=COMBINED_FIGURE,
        text_w=5.45,
        notes=COMBINED_FIGURE.notes,
        origin=COMBINED_FIGURE.origin,
    ),
    Content(
        title="Inside bar versus Harami",
        lines=(
            "Both describe a smaller formation inside a larger one, but the book keeps their rules separate.",
            "Ours: if the preceding candlestick range is 6.0 points, a Harami's narrow range is at most 1.5 to 2.0 points, one-fourth to one-third.",
            "An inside bar has no such one-fourth to one-third restriction (Lim, p. 226).",
            "Meaning/action: do not rename every inside bar as Harami; check the internal proportion first.",
        ),
        accent="The names are related, not interchangeable.",
        notes=("State the proportion arithmetic. It is the distinction the book gives.", "The check now returns to the containment and volume rules."),
        origin="Lim (2016), p. 226. The 6.0-point example is ours, invented.",
    ),
    COMBINED_CHECK,
    ISLAND_CHECK,
    Content(
        title="Exhaustion bar: plain words",
        lines=(
            "We now move from containment to a bar that can exhaust a trend.",
            "In an uptrend, it opens above the previous high, is larger in context, and closes near its low.",
            "There is no gap between the exhaustion bar and the subsequent bar (Lim, p. 226).",
            "Meaning/action: read the larger bar, trend context, close, and next-bar gap together; the pattern is a reversal warning, not certainty.",
        ),
        accent="The bullish exhaustion bar is the converse in a downtrend.",
        notes=("Keep all four book conditions visible before the figure.", "The next slide works the numbers without artwork."),
        origin="Lim (2016), p. 226. The transition wording is ours.",
    ),
    Pair(
        left=Content(
            title="Exhaustion bar: worked numbers",
            lines=(
                "Ours, invented: prior high 65.00; exhaustion O 65.40, H 66.20, L 60.00, C 60.50.",
                "65.40 is above 65.00; the 6.20-point range is large in this uptrend; 60.50 is near low 60.00.",
                "Next O 60.20 lies inside 60.00 to 66.20, so there is no following gap. Meaning/action: all four observations support the reading; now read Figure 7.28.",
            ),
            accent="Numbers first: compare each value with the named level.",
            notes=("Say the comparison aloud: 65.40 > 65.00 and 60.20 lies between 60.00 and 66.20.",),
        ),
        picture=EXHAUSTION_FIGURE,
        text_w=6.0,
        notes=EXHAUSTION_FIGURE.notes,
        origin="The worked PHP values are ours, invented to show Lim's p. 226 rule.",
    ),
    Pair(
        left=Content(
            title="Figure 7.28: bullish exhaustion",
            lines=(
                "The book's bullish exhaustion case is in a downtrend. Gold [1] marks the gap before the bar, red [2] the exhaustion bar, and blue [3] the later rebound.",
                "Ours: support PHP 40.00; low PHP 39.60 and close PHP 41.20. The bar closes near its high, the bullish converse.",
                "Meaning/action: the larger bar matters in trend context. The prior gap is visible, but the rule concerns no gap after the exhaustion bar.",
            ),
            notes=(),
        ),
        picture=EXHAUSTION_FIGURE,
        text_w=5.45,
        notes=EXHAUSTION_FIGURE.notes,
        origin=EXHAUSTION_FIGURE.origin,
    ),
    EXHAUSTION_FIGURE_CHECK,
    Content(
        title="From exhaustion to emotion spike",
        lines=(
            "Next, the book shifts from exhaustion's next-bar gap test to an emotion spike read by range and volume.",
            "The next chart uses invented values as context, not as a prediction.",
        ),
        accent="Read range and volume together.",
        notes=("Use this line to signal the shift from the gap test to the range-and-volume read.",),
        origin="Transition wording is ours; the next chart is invented.",
    ),
    SPIKE_CHART,
    Pair(
        left=Content(
            title="Figure 7.29: emotion spike",
            lines=(
                "In an emotional market, a price spike is usually wide-ranging and accompanied by high volume.",
                "Gold [1] marks the wide spike; red [2] its high volume; blue [3] the three-bar bearish reversal at the top (Lim, p. 227).",
                "Ours: ordinary range 3.0 and volume 1.5 million; spike range 8.0 and volume 6.0 million. Treat it as reversal context, not a prediction.",
            ),
            notes=(),
        ),
        picture=SPIKE_FIGURE,
        text_w=5.55,
        notes=SPIKE_FIGURE.notes,
        origin=SPIKE_FIGURE.origin,
    ),
    Content(
        title="Pin bar: a false barrier story",
        lines=(
            "We now add a barrier test: a pin bar penetrates a barrier during the interval, then rapidly retraces.",
            "Ours: support PHP 40.00, low PHP 38.80, close PHP 40.60, volume 0.8m.",
            "Book-named barriers are moving averages, support or resistance, and trendlines. Pin bars usually form on low volume (Lim, p. 227).",
            "Meaning/action: the breach can fool a trader; wait for the return through the barrier.",
        ),
        accent="The false impression separates pin from exhaustion.",
        notes=("Use the exact plural definition on the next slide.", "The next figure places the barrier and retrace on the real chart."),
        origin="Lim (2016), p. 227. The worked PHP values are ours, invented.",
    ),
    Pair(
        left=Content(
            title="Figure 7.30: pin bar at support",
            lines=(
                "Lim defines it: “single bar misrepresentations of market strength or weakness.” (p. 227).",
                "Gold [1] marks support, red [2] the intra-period penetration, and blue [3] the close back above support.",
                "Meaning/action: the breach suggests a potential breakout, but the rapid retrace warns that impression was false. The book says pin bars usually form on low volume.",
            ),
            notes=(),
        ),
        picture=PIN_FIGURE,
        text_w=5.5,
        notes=PIN_FIGURE.notes,
        origin=PIN_FIGURE.origin,
    ),
    PIN_FIGURE_CHECK,
    Pair(
        left=Content(
            title="Exhaustion versus pin bar",
            lines=(
                "Transition: compare exhaustion with pin's false-barrier story.",
                "Exhaustion: O65.40 > prior high 65.00; H66.20; C60.50; next O60.20 means no gap [3].",
                "Gold [1] open; red [2] close; blue [3] no-gap relationship in Figure 7.28.",
                "No next-bar gap separates the exhaustion bar from its next bar (p. 226); trend may tire.",
                "Next: pin definition, barriers, low-volume tendency, marked return.",
            ),
            notes=(),
        ),
        picture=EXHAUSTION_COMPARE_FIGURE,
        text_w=6.0,
        notes=EXHAUSTION_COMPARE_FIGURE.notes,
        origin="Lim (2016), pp. 226 to 227. The comparison values are ours, invented.",
    ),
    Pair(
        left=Content(
            title="Pin bar: the false barrier story",
            lines=(
                "Lim calls a pin bar a “single bar misrepresentations of market strength or weakness” (p. 227).",
                "Ours: support 40.00; low 38.80; close 40.60; volume 0.8m.",
                "Gold [1] support; red [2] penetration; blue [3] close above it.",
                "Barriers: moving average, support/resistance, or trendline; low volume is usual. Action: wait for return; penetration can look like a breakout.",
            ),
            notes=(),
        ),
        picture=PIN_FIGURE,
        text_w=6.0,
        notes=PIN_FIGURE.notes,
        origin="Lim (2016), p. 227. The worked PHP values are ours, invented.",
    ),
    EXHAUSTION_CHECK,
    Content(
        title="From pin bar to false breakout",
        lines=(
            "We now generalise the pin-bar false-barrier read to support and resistance breakouts.",
            "The next chart uses invented values to show both returned directions.",
        ),
        accent="Wait for the return through the barrier.",
        notes=("Use this transition before showing the two-direction chart.",),
        origin="Transition wording is ours; the next chart is invented.",
    ),
    FALSE_CHART,
    FALSE_OWN_CHART,
    Pair(
        left=Content(
            title="Figure 7.31: false upside breakout (the book's drawing)",
            lines=(
                "Lim calls this a non-failure swing and credits Sperandeo's 2B entry (p. 228).",
                "Gold [1] resistance; red [2] false high; blue [3] close back below; purple [4] stop above high.",
                "This slide reads Lim's drawing; the source drawing supplies no PHP values.",
                "Action: short after return below resistance; stop just above breakout high.",
            ),
            notes=(),
        ),
        picture=FALSE_ONE_FIGURE,
        text_w=5.35,
        notes=FALSE_ONE_FIGURE.notes,
        origin=FALSE_ONE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.32: both breakout directions",
            lines=(
                "Gold [1] marks the false upside high, red [2] the false downside low, blue [3] the upper close back below resistance, and purple [4] the lower close back above support.",
                "Ours: upside barrier PHP 60.00 and downside barrier PHP 40.00; returned closes PHP 59.40 and PHP 40.60.",
                "Meaning/action: short below resistance after a false upside break, or long above support after a false downside break.",
            ),
            notes=(),
        ),
        picture=FALSE_BOTH_FIGURE,
        text_w=5.55,
        notes=FALSE_BOTH_FIGURE.notes,
        origin=FALSE_BOTH_FIGURE.origin,
    ),
    FALSE_BREAKOUT_CHECK,
    Content(
        title="Double Repo: the named crossings",
        lines=(
            "We now use a moving average as the crossing level: a bearish Double Repo closes above and below a three-day SMA twice.",
            "Forward-shifted means plotted three days forward (Lim, p. 229). Ours: SMA 50.00; first pair 50.80 above, 49.60 below.",
            "After 9 bullish days, the second pair is 50.70 above and 49.00 below. Lim requires 8 to 10 days first and a top no more than 8 to 10 bars (p. 229).",
            "Meaning/action: the second pair gives the sell signal; the complete method is in DiNapoli's text.",
        ),
        accent="",
        notes=("Do not import a formula beyond the book's wording. The chart shows both pairs.",),
        origin="Lim (2016), p. 229. The worked PHP values are ours, invented.",
    ),
    REPO_CHART,
    Pair(
        left=Content(
            title="Figure 7.33: Double Repo in the book",
            lines=(
                "Gold [1] and red [2] mark the first two closes across the forward-shifted three-day SMA. Blue [3] marks the later decline.",
                "Meaning/action: Lim presents a bearish reversal in an uptrend; the reverse applies in a downtrend.",
                "The book sends the reader to DiNapoli's original text for detailed and complete discussion.",
            ),
            notes=(),
        ),
        picture=REPO_FIGURE,
        text_w=5.5,
        notes=REPO_FIGURE.notes,
        origin=REPO_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.33: Double Repo limits",
            lines=(
                "Gold [1] marks the forward-shifted three-day SMA. Red [2] marks the required 8 to 10 bullish days before the pattern.",
                "Blue [3] marks the topping formation. The book says it should not exceed 8 to 10 bars (Lim, p. 229).",
                "Meaning/action: count both limits before treating the two crossings as the named sell signal.",
            ),
            notes=(),
        ),
        picture=REPO_LIMITS_FIGURE,
        text_w=5.5,
        notes=REPO_LIMITS_FIGURE.notes,
        origin=REPO_LIMITS_FIGURE.origin,
    ),
    REPO_LIMITS_CHECK,
    Content(
        title="Hikkake: trap, then the opposite entry",
        lines=(
            "We finish this reversal group with Hikkake, an inside-bar breakout that fails; take only the opposite re-entry.",
            "Ours bearish: inside high 52.00, inside low 49.00, false high 53.00, re-entry below 49.00 within 3 bars.",
            "“Trap or ensnare” is the meaning. The bullish converse follows a failed downside break (Lim, p. 230).",
            "Action: wait for the opposite re-entry, never the failed direction.",
        ),
        accent="The three-bar window is part of the rule.",
        notes=("Define the term before showing both directions.", "The next chart puts the levels on an invented example."),
        origin="Lim (2016), p. 230. The worked PHP values are ours, invented.",
    ),
    HIKKAKE_CHART,
    HIKKAKE_OWN_CHART,
    Pair(
        left=Content(
            title="Figure 7.34: bullish Hikkake",
            lines=(
                "Gold [1] marks the inside bar, red [2] the failed downside breakout, and blue [3] the re-entry above the inside high.",
                "Meaning/action: take only the opposite re-entry, within three bars (Lim, p. 230).",
            ),
            notes=(),
        ),
        picture=BULLISH_HIKKAKE_FIGURE,
        text_w=5.5,
        notes=BULLISH_HIKKAKE_FIGURE.notes,
        origin=BULLISH_HIKKAKE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.34: bearish Hikkake",
            lines=(
                "Gold [1] marks the inside bar, red [2] the failed upside breakout, and blue [3] the re-entry below the inside low.",
                "Meaning/action: take only the opposite re-entry, within three bars (Lim, p. 230).",
            ),
            notes=(),
        ),
        picture=BEARISH_HIKKAKE_FIGURE,
        text_w=5.5,
        notes=BEARISH_HIKKAKE_FIGURE.notes,
        origin=BEARISH_HIKKAKE_FIGURE.origin,
    ),
    Pair(
        left=Content(
            title="Figure 7.35: bullish Hikkake at a bottom",
            lines=(
                "Gold [1] marks the Hikkake formation at the channel bottom, red [2] its failed downside breakout, and blue [3] the upside re-entry.",
                "Ours: low PHP 40.00, false low PHP 39.20, re-entry PHP 41.00.",
                "Meaning/action: the re-entry is the signal described by the book; this slide does not interpret the indicator panels.",
            ),
            notes=(),
        ),
        picture=HIKKAKE_EXAMPLE_FIGURE,
        text_w=5.45,
        notes=HIKKAKE_EXAMPLE_FIGURE.notes,
        origin=HIKKAKE_EXAMPLE_FIGURE.origin,
    ),
    HIKKAKE_EXAMPLE_CHECK,
    REVERSAL_CHECK,
)

SECTION1 = Section(
    number=1,
    title="The Price Bar",
    short="7.1 Price bar",
    minutes="16 minutes",
    covers=("OHLC", "range", "higher timeframe"),
    slides=(
        Pair(
            left=Content(
                title="The four prices in one bar",
                lines=(
                    "Lim writes, \"A standard price bar comprises an open (O), high (H), low (L), and close (C) price\" (p. 209).",
                    "Lim defines range as |H - L| (p. 209). Ours, invented: O 50.00, H 52.40, L 49.60, C 51.10; range = Philippine pesos (PHP) 2.80.",
                    "Action: read these four prices before a pattern. Figure 7.1 marks the close (4).",
                ),
                accent="Now show how five trades become these four prices.",
            ),
            picture=PRICE_BAR_FULL,
            text_w=6.2,
            notes=(
                "Start with the book's definition and the invented arithmetic. The figure shows the same four prices as a compact record.",
                "Point to gold 1, red 2 and blue 3 in the figure as the open, high and low. The close is named in the body and shown on the bar.",
            ),
            origin=PRICE_BAR_FULL.origin,
        ),
        Pair(
            left=Content(
                title="Five minutes become one bar",
                lines=(
                    "Now trace Figure 7.1's five invented trades: 50.00, 50.80, 49.60, 52.40, and 51.10 Philippine pesos.",
                    "First becomes O 50.00 [1]; highest H 52.40 [2]; last C 51.10 [3].",
                    "Lowest 49.60 supplies L [4]. Keep first, highest, lowest, and last.",
                ),
                accent="One interval is one OHLC bar. Next, combine several intervals.",
            ),
            picture=PRICE_BAR_CONSTRUCTION,
            text_w=5.8,
            notes=PRICE_BAR_CONSTRUCTION.notes,
            origin=PRICE_BAR_CONSTRUCTION.origin,
        ),
        Pair(
            left=Content(
                title="Three small bars become one larger bar",
                lines=(
                    "Now extend the same rule to three invented five-minute bars: first O 50.00, highest H 50.90, lowest L 49.40, last C 50.30.",
                    "Figure 7.2 keeps O [1], H [2], L [3], and C [4] in the 15-minute composite.",
                    "Action: a higher-timeframe bar preserves first, extreme, and last values; it does not average intermediate opens or closes.",
                ),
                accent="The book's composite rule is the same four-price rule at a longer interval.",
            ),
            picture=HIGHER_TIMEFRAME_FIGURE,
            text_w=5.8,
            notes=HIGHER_TIMEFRAME_FIGURE.notes,
            origin=HIGHER_TIMEFRAME_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Read each interval before naming it",
                lines=(
                    "The book next shows five-minute intervals before it classifies a formation (Lim, p. 210).",
                    "Gold [1] marks the first interval, red [2] a later interval, and blue [3] the OHLC bar below one interval.",
                    "Action: read each interval first; then count bars, identify intrinsic sentiment, and ask continuation or reversal.",
                ),
                accent="The three classification questions come after the interval read.",
            ),
            picture=FORMATION_FULL,
            text_w=5.8,
            notes=FORMATION_FULL.notes,
            origin=FORMATION_FULL.origin,
        ),
        Content(
            title="First question: how many bars?",
            lines=(
                "With the intervals read, first count the bars in the formation. The book's four categories are single, double, triple, and multiple (Lim, p. 210).",
                "Ours, invented: one bar is single, two are double, three are triple, and five are multiple.",
                "Meaning/action: the count describes structure, not direction. A triple formation is not automatically bullish or bearish.",
            ),
            accent="Count first. Next ask what bias the formation carries.",
            notes=(
                "This is the first classification question in Lim's list on p. 210.",
                "Use the invented counts to separate structure from direction. A count does not predict price by itself.",
            ),
            origin="Lim (2016), p. 210. The counts and examples are ours, invented to show the classification.",
        ),
        Content(
            title="Second question: intrinsic sentiment",
            lines=(
                "Now identify intrinsic sentiment, the formation's own bullish or bearish bias. Lim points back to Chapter 4 for intrinsic bias (Lim, p. 211).",
                "Ours, invented: an intrinsically bullish formation stays bullish in either an uptrend or a downtrend; location does not rename it.",
                "Meaning/action: separate the formation's own bias from what the surrounding trend expects next.",
            ),
            accent="The pattern's own bias comes before the trend-context question.",
            notes=(
                "Keep intrinsic sentiment separate from trend sentiment. Chapter 4 is the named pointer for the earlier term.",
                "The invented example is only a classification test, not a claim that every bullish pattern works in every trend.",
            ),
            origin="Lim (2016), p. 211, with a pointer to Chapter 4. The placement example is ours.",
        ),
        Content(
            title="Third question: continuation or reversal?",
            lines=(
                "Trend sentiment is bullish in an uptrend and bearish in a downtrend (Lim, p. 211).",
                "Compare intrinsic sentiment: agreement suggests continuation; disagreement suggests potential reversal (p. 211).",
                "Ours: bearish formation plus uptrend means potential reversal; bullish plus uptrend means potential continuation, not certainty.",
            ),
            accent="Agreement suggests continuation; disagreement suggests reversal.",
            notes=(
                "Lim states the agreement rule on p. 211. Keep the word potential because a classification is not a guarantee.",
                "The full four-cell table and the book's head and shoulders examples begin in Part 2.",
            ),
            origin="Lim (2016), p. 211. The two invented placements illustrate the book's agreement rule.",
        ),
        Pair(
            left=Content(
                title="Part 1 in one worked read",
                lines=(
                    "Ours, invented: two bars make a double formation [1]. The second closes at 49.80 below first low 50.20.",
                    "The second bar's intrinsic sentiment is bearish [2]. The rising upper price sequence beside the pair is bullish trend context [3].",
                    "Read: potential reversal, not a promise of a fall.",
                ),
                accent="Count, intrinsic bias, and trend expectation now have one worked read.",
            ),
            picture=WORKED_CHART,
            text_w=5.55,
            notes=(
                "This worked read combines the three classification questions without introducing a new pattern name.",
                "Say potential reversal, not reversal certainty. The next slide checks the construction arithmetic.",
            ),
            origin=WORKED_CHART.origin,
        ),
        Check(
            label="Building a price bar",
            questions=(
                Q(
                    stem="With H 52.40 and L 49.60, what is the range?",
                    options=("PHP 1.40", "PHP 2.80", "PHP 3.80", "PHP 102.00"),
                    answer="B",
                    reason="Range is the absolute distance from high to low: |52.40 - 49.60| = PHP 2.80 (Lim, p. 209).",
                ),
                Q(
                    stem="Which price comes from the last trade in the interval?",
                    options=("Open", "High", "Low", "Close"),
                    answer="D",
                    reason="The last trade becomes the close. The first trade becomes the open; extremes become high and low (Lim, p. 210).",
                ),
            ),
            picture=PRICE_BAR_FULL,
            text_w=5.0,
            layout="beside",
            notes=(
                "Let students calculate before revealing. Both answers are stated in the preceding worked slides and the marked bar remains visible.",
                "Remind the room that range is a distance, not a fourth OHLC price.",
            ),
            origin="Questions are ours and answerable from the preceding Part 1 slides.",
        ),
        Check(
            label="Classifying a formation",
            questions=(
                Q(
                    stem="Single, double, triple and multiple describe what?",
                    options=("Number of bars", "Trading volume", "The high price", "The trend duration"),
                    answer="A",
                    reason="The first classification asks for the number of bars in the formation (Lim, p. 210).",
                ),
                Q(
                    stem="When intrinsic and trend sentiments disagree, the expectation is:",
                    options=("A continuation", "A wider range", "A potential reversal", "A new timeframe"),
                    answer="C",
                    reason="Lim says agreement indicates continuation and disagreement indicates reversal (Lim, p. 211).",
                ),
            ),
            picture=CLASSIFICATION_CROP,
            text_w=5.0,
            layout="beside",
            notes=(
                "Ask the room to separate count, intrinsic bias, and expected direction.",
                "The crop keeps the three classification cues visible. Part 2 adds the four-cell table.",
            ),
            origin="Questions are ours and answerable from the preceding Part 1 slides and Figure 7.3.",
        ),
    ),
)

SECTION2 = Section(
    number=2,
    title="Reading a Pattern",
    short="7.2 Pattern reading",
    minutes="",
    covers=("continuation", "reversal", "16 characteristics"),
    slides=(
        Content(
            title="Trend sentiment and intrinsic sentiment",
            lines=(
                "With the three questions in place, define trend sentiment: bullish in an uptrend, bearish in a downtrend. Intrinsic sentiment is a formation's own bullish or bearish bias (Lim, p. 211).",
                "Chapter 4 defines an inverted head and shoulders as bullish; in an uptrend, bullish biases agree.",
                "Four invented cells: uptrend plus bullish formation and downtrend plus bearish formation are continuation; the mixed pairs are potential reversals.",
            ),
            accent="Agreement gives continuation; disagreement gives reversal.",
            notes=(
                "This is the book's explicit distinction on p. 211. Chapter 4 supplies the earlier intrinsic-bias meaning.",
            ),
            origin="Lim (2016), p. 211. The placement example is ours, invented to show agreement.",
        ),
        Pair(
            left=Content(
                title="The two-by-two rule",
                lines=(
                    "Read the rows first: an uptrend has bullish trend sentiment; a downtrend has bearish trend sentiment. Columns show bullish or bearish formation.",
                    "The two agreement cells are continuation; the two mixed cells are potential reversal.",
                    "Lim's rule: agreement means continuation; disagreement means reversal (p. 211). Compare both sentiments.",
                ),
                accent="",
            ),
            picture=SENTIMENT_CHART,
            text_w=5.0,
            notes=(
                "Read the four cases as a table. Keep potential for every directional expectation.",
            ),
            origin="Lim (2016), p. 211. The four cases are ours, invented to show the rule.",
        ),
        Check(
            label="Continuation or reversal",
            questions=(
                Q(
                    stem="A bearish formation in an uptrend is a potential:",
                    options=("Continuation", "Reversal", "Higher timeframe", "Range"),
                    answer="B",
                    reason="The bearish intrinsic bias disagrees with bullish trend sentiment in an uptrend, so Lim classifies it as a potential reversal (p. 211).",
                ),
                Q(
                    stem="An inverted head and shoulders in an uptrend is a potential:",
                    options=("Reversal", "Single bar", "Low volume", "Continuation"),
                    answer="D",
                    reason="Chapter 4 calls it bullish. In an uptrend, bullish biases agree: potential continuation (p. 211).",
                ),
            ),
            picture=SENTIMENT_CHART,
            text_w=5.0,
            layout="beside",
            notes=(
                "This check is the first Part 2 question. Its answers are stated on the two preceding slides.",
            ),
            origin="Questions are ours and answerable from the preceding Part 2 slides.",
        ),
    ),
)

# Part 2 pattern-reading content.
def _book_figure(number, title, shows, page, *, crop=(), marks=None,
                 aspect=1.48):
    """A marked placeholder for a copyrighted figure supplied on the art build."""
    default_marks = (
        Mark(1, "circle", 0.18, 0.24, 0.28, 0.34,
             color="gold", at=(0.14, 0.20), size=0.30),
        Mark(2, "circle", 0.46, 0.42, 0.56, 0.52,
             color="red", at=(0.42, 0.38), size=0.30),
        Mark(3, "circle", 0.74, 0.62, 0.84, 0.72,
             color="blue", at=(0.88, 0.58), size=0.30),
    )
    return Figure(
        title=title,
        number=number,
        aspect=aspect,
        crop=crop,
        marks=tuple(default_marks if marks is None else marks),
        shows=shows,
        notes=(
            "Read the invented numbers in the body, then locate the same three "
            "features with the numbered marks.",
            "The marks identify only the feature named beside the same number. "
            "Keep the book's potentially and generally qualifiers.",
        ),
        origin=f"Lim (2016), p. {page}, Figure {number}. The worked values are ours, invented to show the rule.",
    )


FIG_73 = _book_figure("7.3", "Figure 7.3: read before classifying",
                      "Five-minute intervals and examples classified by bar count, intrinsic sentiment, and expected direction.", 211)
FIG_74 = _book_figure("7.4", "Figure 7.4: seven bearish forms",
                      "A readable crop of one bearish single-bar formation: a large bar opens above the previous high and closes near or below the previous close.", 212,
                      aspect=940 / 620,
                      marks=(
                          Mark(1, "box", .153, .058, .218, .325, color="gold", at=(.13, .08)),
                          Mark(2, "line", .177, .279, .218, .279, color="red", at=(.30, .25)),
                          Mark(3, "line", .177, .105, .177, .325, color="blue", at=(.30, .12)),
                      ))
FIG_74B = _book_figure("7.4", "Figure 7.4: bearish form 2",
                       "A readable crop of bearish form 2: a large bar closes near or below the previous low.", 212,
                       aspect=940 / 620, crop=(0.235, 0.0, 0.615, 0.419),
                       marks=(
                           Mark(1, "circle", .46, .38, .72, .58, color="gold", at=(.28, .66)),
                           Mark(2, "line", .46, .18, .46, .42, color="red", at=(.82, .18)),
                           Mark(3, "line", .46, .38, .46, .78, color="blue", at=(.82, .86)),
                       ))
FIG_74C = _book_figure("7.4", "Figure 7.4: bearish form 3",
                       "A readable crop of bearish form 3: the bar closes below a gap between its open and the prior low.", 212,
                       aspect=940 / 620, crop=(0.385, 0.0, 0.445, 0.419),
                       marks=(
                           Mark(1, "line", .28, .38, .72, .38, color="gold", at=(.20, .28)),
                           Mark(2, "circle", .46, .18, .70, .60, color="red", at=(.82, .16)),
                           Mark(3, "line", .50, .58, .50, .84, color="blue", at=(.84, .82)),
                       ))
FIG_75 = _book_figure("7.5", "Figure 7.5: seven bullish forms",
                      "A readable crop of one bullish single-bar formation: a large bar opens below the previous low and closes near or above the previous close.", 212,
                      aspect=940 / 620,
                      marks=(
                          Mark(1, "circle", .156, .826, .203, .930, color="gold", at=(.13, .72)),
                          Mark(2, "line", .180, .721, .205, .721, color="red", at=(.30, .64)),
                          Mark(3, "line", .180, .756, .180, .970, color="blue", at=(.30, .96)),
                      ))
FIG_75B = _book_figure("7.5", "Figure 7.5: bullish form 2",
                       "A readable crop of bullish form 2: a large bar closes near or above the previous high.", 212,
                       aspect=940 / 620, crop=(0.235, 0.419, 0.615, 0.0),
                       marks=(
                           Mark(1, "circle", .46, .46, .72, .66, color="gold", at=(.28, .38)),
                           Mark(2, "line", .46, .54, .46, .82, color="red", at=(.82, .58)),
                           Mark(3, "line", .46, .20, .46, .58, color="blue", at=(.82, .86)),
                       ))
FIG_75C = _book_figure("7.5", "Figure 7.5: bullish form 3",
                       "A readable crop of bullish form 3: the bar closes above a gap between its open and the prior high.", 212,
                       aspect=940 / 620, crop=(0.385, 0.419, 0.445, 0.0),
                       marks=(
                           Mark(1, "line", .28, .56, .72, .56, color="gold", at=(.20, .68)),
                           Mark(2, "circle", .46, .34, .70, .76, color="red", at=(.82, .32)),
                           Mark(3, "line", .50, .18, .50, .52, color="blue", at=(.84, .16)),
                       ))
FIG_76 = _book_figure("7.6", "Figure 7.6: triple bearish forms",
                      "A readable crop of the first triple bearish formation: a large middle bar closes near its low between two outer bars.", 213,
                      aspect=650 / 550, crop=(0.123, 0.0, 0.585, 0.364),
                      marks=(
                          Mark(1, "circle", .40, .15, .72, .42, color="gold", at=(.24, .10)),
                          Mark(2, "circle", .49, .28, .62, .55, color="red", at=(.84, .36)),
                          Mark(3, "line", .42, .52, .78, .52, color="blue", at=(.84, .62)),
                      ))
FIG_77 = _book_figure("7.7", "Figure 7.7: triple bearish forms",
                      "A readable crop of the fourth triple bearish formation: a gap up followed by a gap down, the single-island reversal bar.", 214,
                      aspect=620 / 570, crop=(0.081, 0.0, 0.597, 0.351),
                      marks=(
                          Mark(1, "circle", .35, .10, .65, .30, color="gold", at=(.22, .08)),
                          Mark(2, "line", .42, .24, .65, .24, color="red", at=(.84, .18)),
                          Mark(3, "line", .42, .33, .72, .33, color="blue", at=(.85, .40)),
                      ))
FIG_78 = _book_figure("7.8", "Figure 7.8: triple bullish forms",
                      "A readable crop of the first triple bullish formation: the first bar closes near its low, the middle bar closes near its high, and the third bar closes near its high.", 214,
                      aspect=680 / 570, crop=(0.074, 0.0, 0.5, 0.0),
                      marks=(
                          Mark(1, "circle", .38, .70, .52, .95, color="gold", at=(.27, .65)),
                          Mark(2, "circle", .56, .70, .68, .98, color="red", at=(.80, .65)),
                          Mark(3, "circle", .72, .68, .86, .95, color="blue", at=(.88, .56)),
                      ))
FIG_79 = _book_figure("7.9", "Figure 7.9: triple bullish forms",
                      "A readable crop of the fourth triple bullish formation: the second bar gaps down and the third bar gaps up and closes near its high.", 215,
                      aspect=900 / 650,
                      marks=(
                          Mark(1, "circle", .31, .68, .35, .82, color="gold", at=(.28, .68)),
                          Mark(2, "line", .34, .72, .38, .72, color="red", at=(.42, .67)),
                          Mark(3, "circle", .39, .68, .43, .84, color="blue", at=(.45, .88)),
                      ))
FIG_710 = _book_figure("7.10", "Figure 7.10: multiple bearish forms",
                       "A readable crop of the first multiple bearish formation: a high first close followed by narrow bars and a final close near its low.", 215,
                       aspect=940 / 595,
                       marks=(
                           Mark(1, "circle", .13, .14, .20, .29, color="gold", at=(.11, .08)),
                           Mark(2, "box", .185, .10, .263, .26, color="red", at=(.30, .10)),
                           Mark(3, "line", .269, .137, .269, .323, color="blue", at=(.30, .62)),
                       ))
FIG_711 = _book_figure("7.11", "Figure 7.11: multiple bullish forms",
                       "A readable crop of the first multiple bullish formation: a low first close followed by narrow bars and a final close near its high.", 216,
                       aspect=940 / 720,
                       marks=(
                           Mark(1, "circle", .16, .62, .19, .75, color="gold", at=(.12, .57)),
                           Mark(2, "box", .187, .615, .255, .806, color="red", at=(.31, .56)),
                           Mark(3, "line", .272, .629, .272, .806, color="blue", at=(.31, .88)),
                       ))
FIG_712 = _book_figure("7.12", "Figure 7.12: bullish continuation forms",
                       "The first simple bullish continuation formation: a second bar closing near its high.", 216,
                       aspect=680 / 525,
                       marks=(
                           Mark(1, "line", .318, .246, .471, .246, color="gold", at=(.23, .20)),
                           Mark(2, "circle", .403, .058, .480, .217, color="red", at=(.52, .12)),
                           Mark(3, "circle", .394, .058, .480, .217, color="blue", at=(.52, .35)),
                       ))
FIG_712B = _book_figure("7.12", "Figure 7.12: bullish continuation form two",
                        "The second simple bullish continuation formation: a second bar retracing to the first bar's midpoint before rebounding.", 216,
                        aspect=680 / 525,
                        marks=(
                            Mark(1, "circle", .60, .23, .68, .52, color="gold", at=(.55, .19)),
                            Mark(2, "line", .58, .27, .75, .27, color="red", at=(.82, .32)),
                            Mark(3, "circle", .68, .06, .74, .30, color="blue", at=(.78, .04)),
                        ))
FIG_712_ALL = _book_figure("7.12", "Figure 7.12: both bullish continuation forms",
                           "The two simple bullish continuation formations shown together: a second bar closing near its high and a 50% retrace followed by a rebound.", 216,
                           aspect=680 / 525, marks=())
FIG_713 = _book_figure("7.13", "Figure 7.13: reversal context",
                       "A rapid rise, fewer oscillations, and an overextended bar against the upper band.", 217,
                       aspect=2.0,
                       marks=(
                           Mark(1, "circle", .30, .45, .40, .62,
                                color="gold", at=(.24, .38), size=.28),
                           Mark(2, "circle", .56, .64, .68, .80,
                               color="red", at=(.74, .60), size=.28),
                           Mark(3, "box", .365, .08, .445, .42,
                                color="blue", at=(.58, .46), size=.28),
                       ))
FIG_713_CHECK = _book_figure(
    "7.13", "Figure 7.13: reversal context check", FIG_713.shows, 217,
    aspect=2.0, crop=(0.001, 0.0, 0.001, 0.0), marks=FIG_713.marks,
)


def _figure_reading(figure, title, *lines):
    """Attach the plain-language reading printed beside a source crop."""
    figure.reading_title = title
    figure.reading_lines = tuple(lines)
    return figure


_figure_reading(
    FIG_74, "Figure 7.4, form 1: the key reversal bar",
    "Gold [1] marks the final close near the previous close. Red [2] marks the opening above the previous high. Blue [3] marks the wide range.",
    "Lim calls this generally bearish and potentially more reliable when context supports it. The book drawing has no volume panel; the course chart supplies the invented volume.",
    "Next we compare the second bearish form.",
)
_figure_reading(
    FIG_74B, "Figure 7.4, form 2: a close near the prior low",
    "Gold [1] marks the large bar closing near the previous low. Red [2] marks the opening relationship, and blue [3] marks the wide range.",
    "The book drawing shows shape and close direction only. Use the course chart for invented prices and volume.",
    "Next we read the gap form.",
)
_figure_reading(
    FIG_74C, "Figure 7.4, form 3: a gap before the close",
    "Gold [1] marks the gap, red [2] the bearish bar, and blue [3] the close below the gap.",
    "This is a potential bearish clue, not a promise. The crop has no volume panel.",
    "Now we turn the same test upward for bullish forms.",
)
_figure_reading(
    FIG_75, "Figure 7.5, form 1: the bullish key reversal",
    "Gold [1] marks the final close near the previous close. Red [2] marks the opening below the previous low. Blue [3] marks the wide range.",
    "The book's bullish reading is potential and context-dependent; its crop has no volume panel.",
    "Next we compare the second bullish form.",
)
_figure_reading(
    FIG_75B, "Figure 7.5, form 2: a close near the prior high",
    "Gold [1] marks the large bar closing near the previous high. Red [2] marks the opening relationship, and blue [3] marks the range.",
    "The crop shows the formation, not volume. The course chart carries the invented numerical example.",
    "Next we read the bullish gap form.",
)
_figure_reading(
    FIG_75C, "Figure 7.5, form 3: a gap before the close",
    "Gold [1] marks the gap, red [2] the bullish bar, and blue [3] the close above the gap.",
    "The shape suggests a potential bullish reversal when the broader trend is down.",
    "The triple-bar families add a middle bar next.",
)
_figure_reading(
    FIG_76, "Figure 7.6, form 1: three bearish bars",
    "Gold [1] marks the first outer close, red [2] the middle bar, and blue [3] the final outer close.",
    "The outer closes and the middle bar frame a potential bearish reversal; the crop has no volume panel.",
    "The next triple drawing adds an island gap.",
)
_figure_reading(
    FIG_77, "Figure 7.7, form 4: the island reversal",
    "Gold [1] marks the gap up, red [2] the island bar, and blue [3] the gap down into the bearish close.",
    "The figure shows the gap structure and close direction. Volume belongs to the invented course chart, not this crop.",
    "Now compare the bullish triple forms.",
)
_figure_reading(
    FIG_78, "Figure 7.8, form 1: three bullish bars",
    "Gold [1] marks the first bar closing near its low, red [2] the middle bar closing near its high, and blue [3] the final bar closing near its high.",
    "Those close directions give the formation its potential bullish reading. The crop has no volume panel.",
    "The next bullish drawing keeps the same close-direction test.",
)
_figure_reading(
    FIG_79, "Figure 7.9, form 4: the bullish island reversal",
    "Gold [1] marks the gap down, red [2] the middle bar, and blue [3] the final bar closing near its high after the gap up.",
    "The figure shows the bars and gaps only. Use the course chart for invented volume values.",
    "Multiple-bar forms now add a longer intermediate sequence.",
)
_figure_reading(
    FIG_712, "Figure 7.12, continuation form 1",
    "Gold [1] marks the prior high, red [2] the second bar, and blue [3] its close near the high.",
    "Lim presents this as bullish continuation when the pattern agrees with the trend. The crop has no volume panel.",
    "The second continuation form adds a midpoint retrace.",
)
_figure_reading(
    FIG_712B, "Figure 7.12, continuation form 2",
    "Gold [1] marks the first bar, red [2] the 50% midpoint retrace, and blue [3] the rebound through the old high.",
    "The crop shows the midpoint level but no volume panel; the course chart supplies invented volume separately.",
    "The 16 reversal characteristics explain when a move may be losing energy.",
)
_figure_reading(
    FIG_710, "Figure 7.10: multiple bearish forms",
    "Gold [1] marks the first bar, red [2] the intermediate sequence, and blue [3] the final close near its low.",
    "The crop has no volume panel. Lim's volume exception belongs to the surrounding explanation, not this mark.",
    "The bullish multiple family reverses this direction.",
)
_figure_reading(
    FIG_711, "Figure 7.11: multiple bullish forms",
    "Gold [1] marks the first bar, red [2] the narrow middle sequence, and blue [3] the final close near its high.",
    "The crop has no volume panel, so its marks do not claim the pattern 2 volume exception.",
    "We finish by reading the warning context in Figure 7.13.",
)
_figure_reading(
    FIG_713, "Figure 7.13: reversal context",
    "Gold [1] marks characteristic 8, the rapid rise and changing momentum; red [2] marks characteristic 10, the fewer oscillations; blue [3] marks characteristic 14, the actual overextended price bar against the upper band.",
    "The source label is not the target: the blue box sits on the price bar itself. The book names the upper band but gives no formula here.",
    "Barrier proximity is the next reliability rule.",
)

# The checks repeat the book crop with marks, because the question and answer
# must carry the visual evidence they ask students to read. The ordinary
# teaching slides keep the source drawing cropped and marked beside our chart.
FIG_74_CHECK = _book_figure(
    "7.4", "Figure 7.4: check reading", FIG_74.shows, 212,
    aspect=940 / 620, crop=FIG_74.crop,
    marks=(
        Mark(1, "box", .40, .10, .78, .56, color="gold", at=(.28, .08)),
        Mark(2, "line", .54, .48, .78, .48, color="red", at=(.84, .46)),
        Mark(3, "line", .54, .18, .54, .56, color="blue", at=(.84, .18)),
    ),
)
FIG_76_CHECK = _book_figure(
    "7.6", "Figure 7.6: check reading", FIG_76.shows, 213,
    aspect=650 / 550, crop=FIG_76.crop,
    marks=(
        Mark(1, "circle", .40, .15, .72, .42, color="gold", at=(.24, .10)),
        Mark(2, "circle", .49, .28, .62, .55, color="red", at=(.84, .36)),
        Mark(3, "line", .42, .52, .78, .52, color="blue", at=(.84, .62)),
    ),
)
FIG_712_CHECK = _book_figure(
    "7.12", "Figure 7.12: check reading", FIG_712.shows, 216,
    aspect=680 / 525, crop=FIG_712.crop,
    marks=(
        Mark(1, "line", .40, .34, .76, .34, color="gold", at=(.20, .28)),
        Mark(2, "circle", .60, .08, .78, .30, color="red", at=(.84, .12)),
        Mark(3, "circle", .58, .08, .78, .30, color="blue", at=(.84, .40)),
    ),
)


def _c(title, lines, *, accent="", caption="", notes=(), origin="Lim (2016), Chapter 7; worked values are ours, invented to show the rule."):
    return Content(title=title, lines=tuple(lines), accent=accent,
                   caption=caption, notes=tuple(notes) or (
                       "Read the plain-language rule first, then ask students to explain the numbers.",
                       "Keep the book's potential reading separate from a guarantee.",
                   ), origin=origin)


def _form_chart(letter, title, shows, marks):
    """The marked, invented counterpart placed beside a readable book crop."""
    return Chart(letter=letter, title=title, shows=shows,
                 marks=tuple(marks), tier="core")


CHART_QL = _form_chart("QL", "Chart QL: bearish single-bar form",
                       "Our invented bearish single-bar form with values on the bars.", (
                           Mark(1, "circle", .655, .39, .675, .43, color="gold", at=(.56, .48), size=.28),
                           Mark(2, "line", .57, .43, .70, .43, color="red", at=(.80, .36)),
                           Mark(3, "line", .66, .22, .66, .90, color="blue", at=(.84, .94)),
                       ))
CHART_QM = _form_chart("QM", "Chart QM: bullish single-bar form",
                       "Our invented bullish single-bar form with values on the bars.", (
                           Mark(1, "circle", .645, .29, .685, .35, color="gold", at=(.55, .20)),
                           Mark(2, "line", .57, .62, .70, .62, color="red", at=(.80, .55)),
                           Mark(3, "line", .66, .22, .66, .90, color="blue", at=(.84, .94)),
                       ))
CHART_QN = _form_chart("QN", "Chart QN: triple bearish form one",
                       "Our invented triple bearish form with ranges and volumes.", (
                           Mark(1, "circle", .24, .38, .30, .48, color="gold", at=(.16, .32)),
                           Mark(2, "circle", .48, .52, .54, .62, color="red", at=(.42, .66)),
                           Mark(3, "line", .72, .69, .78, .69, color="blue", at=(.86, .62)),
                       ))
CHART_QO = _form_chart("QO", "Chart QO: island reversal form",
                       "Our invented island reversal form with gaps and volume.", (
                           Mark(1, "circle", .48, .34, .54, .44, color="gold", at=(.42, .28)),
                           Mark(2, "circle", .48, .20, .54, .32, color="red", at=(.42, .16)),
                           Mark(3, "line", .72, .69, .78, .69, color="blue", at=(.86, .62)),
                       ))
CHART_QP = _form_chart("QP", "Chart QP: triple bullish form one",
                       "Our invented triple bullish form with ranges and volumes.", (
                           Mark(1, "circle", .24, .55, .30, .65, color="gold", at=(.16, .70)),
                           Mark(2, "line", .48, .54, .54, .54, color="red", at=(.62, .46)),
                           Mark(3, "circle", .72, .26, .78, .36, color="blue", at=(.86, .22)),
                       ))
CHART_QQ = _form_chart("QQ", "Chart QQ: triple bullish gap form",
                       "Our invented triple bullish gap form with ranges and volume.", (
                           Mark(1, "circle", .48, .48, .54, .58, color="gold", at=(.42, .42)),
                           Mark(2, "line", .72, .25, .78, .25, color="red", at=(.86, .16)),
                           Mark(3, "circle", .72, .80, .78, .88, color="blue", at=(.86, .92)),
                       ))
CHART_QR = _form_chart("QR", "Chart QR: multiple bearish form",
                       "Our invented multiple bearish form with intermediate volumes.", (
                           Mark(1, "circle", .24, .27, .30, .35, color="gold", at=(.16, .22)),
                           Mark(2, "box", .40, .20, .68, .56, color="red", at=(.38, .12)),
                           Mark(3, "line", .78, .69, .84, .69, color="blue", at=(.90, .60)),
                       ))
CHART_QS = _form_chart("QS", "Chart QS: multiple bullish form",
                       "Our invented multiple bullish form with intermediate volumes.", (
                           Mark(1, "circle", .24, .55, .30, .65, color="gold", at=(.16, .70)),
                           Mark(2, "box", .40, .28, .68, .56, color="red", at=(.38, .22)),
                           Mark(3, "line", .78, .25, .84, .25, color="blue", at=(.90, .16)),
                       ))
CHART_QT = _form_chart("QT", "Chart QT: continuation pattern one",
                       "Our invented continuation form with the prior high and breach.", (
                           Mark(1, "line", .18, .35, .80, .35, color="gold", at=(.14, .30)),
                           Mark(2, "line", .70, .23, .78, .23, color="red", at=(.88, .14)),
                           Mark(3, "circle", .72, .15, .80, .25, color="blue", at=(.84, .31)),
                       ))
CHART_QU = _form_chart("QU", "Chart QU: continuation pattern two",
                       "Our invented continuation form with the 50 percent midpoint and rebound.", (
                           Mark(1, "circle", .20, .42, .30, .58, color="gold", at=(.14, .68)),
                           Mark(2, "circle", .46, .43, .54, .51, color="red", at=(.62, .36)),
                           Mark(3, "line", .76, .25, .84, .25, color="blue", at=(.92, .16)),
                       ))
CHART_QK = _form_chart("QK", "Chart QK: reversal context",
                      "Our invented reversal context chart with rapid rise, pullbacks, high volume, and an upper band.", (
                          Mark(1, "arrow", .24, .72, .58, .28, color="gold", at=(.18, .74)),
                          Mark(2, "circle", .62, .22, .70, .32, color="red", at=(.78, .37)),
                          Mark(3, "circle", .87, .17, .93, .25, color="blue", at=(.78, .10)),
                      ))
CHART_QV = Chart(letter="QV", title="Chart QV: characteristics 7 and 8",
                 shows="A plain-language recall of BRR and angular symmetry and momentum.",
                 marks=())
CHART_QW = _form_chart("QW", CHART_QL.title, CHART_QL.shows, CHART_QL.marks)
CHART_QX = _form_chart("QX", CHART_QL.title, CHART_QL.shows, CHART_QL.marks)
CHART_QY = _form_chart("QY", CHART_QM.title, CHART_QM.shows, CHART_QM.marks)
CHART_QZ = _form_chart("QZ", CHART_QM.title, CHART_QM.shows, CHART_QM.marks)
CHART_RD = _form_chart("RD", CHART_QN.title, CHART_QN.shows, CHART_QN.marks)
CHART_RE = _form_chart("RE", CHART_QT.title, CHART_QT.shows, CHART_QT.marks)
CHART_RF = _form_chart("RF", CHART_QK.title, CHART_QK.shows, CHART_QK.marks)
CHART_RG = _form_chart("RG", CHART_QL.title, CHART_QL.shows, CHART_QL.marks)
CHART_RH = _form_chart("RH", CHART_QM.title, CHART_QM.shows, CHART_QM.marks)


def _p(left, picture, *, companion=None, text_w=5.55, notes=(), origin="Lim (2016), Chapter 7; worked values are ours, invented to show the rule."):
    pair = Pair(left=left, picture=picture, text_w=text_w,
                notes=tuple(notes) or left.notes,
                origin=origin)
    # The base kit has no companion field, so keep this range's source-level
    # expansion metadata on the Pair and expand it before the final chapter.
    pair.companion = companion
    return pair


SECTION2_SLIDES = (
    _c("Trend sentiment and intrinsic sentiment", (
        "Trend sentiment is the direction of the wider move: bullish in an uptrend and bearish in a downtrend.",
        "Pattern polarity means the pattern's own bullish or bearish direction. The book's head and shoulders example is bearish; its inverted head and shoulders example is bullish. (Lim, p. 211.)",
        "Use both sentiments before classifying the pattern: agreement suggests continuation, while disagreement suggests a potential reversal.",
    ), accent="The examples supply the polarity used in the next check."),
    _p(_c("The two-by-two rule", (
        "Agreement: +4.0% uptrend with +2.0% bullish formation, or -4.0% downtrend with -2.0% bearish formation, suggests continuation.",
        "Disagreement: +4.0% with -2.0%, or -4.0% with +2.0%, suggests a potential reversal. These invented values never make certainty.",
    ), accent="Compare the wider trend with the pattern's own polarity."),
       Chart(letter="T", title="Chart T: four sentiment cases",
             shows="Four invented percentage cases: two agreements are continuation and two disagreements are potential reversal.", marks=()), text_w=3.75),
    Check(
        label="Continuation or reversal",
        questions=(
            Q(stem="A bearish pattern in an uptrend is a:",
              options=("Reversal", "Continuation", "Neutral bar", "Volume pattern"),
              answer="A", reason="The sentiments disagree: bearish intrinsic sentiment meets bullish trend sentiment."),
            Q(stem="An inverted head and shoulders in an uptrend is a:",
              options=("Reversal", "Continuation", "Bearish pattern", "Gap"),
              answer="B", reason="Both the pattern's intrinsic sentiment and the uptrend are bullish, so they agree."),
        ),
        notes=("Ask for the two sentiments before accepting an answer.",),
        picture=Chart(letter="T", title="Chart T: four sentiment cases",
                      shows="Four invented percentage cases that make agreement and disagreement visible.", marks=()),
        layout="top", text_w=5.1,
        origin="Questions are ours and answerable from the preceding two slides.",
    ),
    _c("Answer: continuation or reversal", (
        "A bearish pattern in an uptrend is a reversal because bearish intrinsic sentiment disagrees with bullish trend sentiment.",
        "An inverted head and shoulders in an uptrend is a continuation because both sentiments are bullish.",
        "The four cases are a classification rule. They do not forecast with certainty.",
    ), accent="Next, the book assumes an uptrend while it draws bearish reversals."),

    _p(_c("A bearish reversal bar can warn that buying is weakening", (
        "We are looking at a bearish single-bar reversal: the close turns down, the range is wide, and volume can add confidence to the reading.",
        "Here is the same pattern with simple prices. The prior close is PHP 51.10 and the final close is PHP 50.80, below it. Gold [1] marks that close.",
        "The final bar is wide, near its low, with 4.0m shares: red [2] marks range; blue [3] marks volume.",
        "Narrow or low volume is uncertainty; wide, near-low, high volume is potentially more reliable.",
    )), Chart(letter="QA", title="Chart QA: bearish close and volume", shows="Two invented PHP bars. Mark 1 is the close below the prior close; mark 2 is the wide final range; mark 3 is the 4.0 million volume.", marks=(
        Mark(1, "circle", .63, .36, .69, .43, color="gold", at=(.56, .50)),
        Mark(2, "line", .66, .22, .66, .72, color="red", at=(.78, .48)),
        Mark(3, "circle", .64, .78, .70, .84, color="blue", at=(.80, .88)),
    ), tier="core"), text_w=5.45),
    _p(_c("Now let us compare the first three bearish forms", (
        "We are comparing the book's first three generic bearish forms, where the final bar turns against the preceding move.",
        "On our course chart, gold [1] marks the final close near the previous close. Red [2] marks the final bar opening above the previous high; blue [3] marks its large range and volume.",
        "Lim's first three forms become stronger when the close falls below the previous low; a narrow or low-volume bar shows uncertainty.",
        "The next slide supplies the book's cropped drawing with the same numbered reading. (Lim, p. 212.)",
    )), CHART_QL, companion=FIG_74, text_w=5.45),
    _p(_c("The next three bearish forms use the same test", (
        "These forms still ask whether the final bar turns bearish against the preceding move.",
        "Our chart repeats the generic bearish form: gold [1] is the final close; red [2] is the opening relationship; blue [3] is the wide range and volume.",
        "A close below the previous low strengthens the bearish reading, while a narrow or low-volume bar shows uncertainty.",
        "The next slide supplies the book's drawing, cropped to this same form. (Lim, p. 212.)",
        "The book figure has no volume panel. Use our chart for the invented PHP and volume example.",
        "The shape is a potential reversal clue, not a guaranteed outcome.",
    )), CHART_QW, companion=FIG_74B, text_w=5.45),
    _p(_c("The seventh bearish form adds a reliability question", (
        "After identifying the bearish form, we ask whether its context makes the reading more reliable.",
        "Our course chart marks the close, opening relationship, and large range with gold [1], red [2], and blue [3].",
        "The next slide supplies the book's cropped drawing with the same numbered reading. (Lim, p. 212.)",
        "The book figure has no volume panel, so do not infer volume from it. Lim discusses high volume in the surrounding text.",
        "Treat the pattern as potentially more reliable, then check its context.",
    )), CHART_QX, companion=FIG_74C, text_w=5.45),
    Check(
        label="Generic single and double reversals",
        questions=(
            Q(stem="Which final bearish bar is potentially more reliable?", options=(
                "Overextended, near its low, high volume", "Narrow, low volume", "Near its high, low volume", "Any bar"),
              answer="A", reason="Lim's reliability qualifiers are an overextended final bar, a close near its low, and high volume."),
            Q(stem="What does a narrow or low-volume bar show?", options=(
                "Uncertainty", "A guaranteed reversal", "High volume", "Trend agreement"),
              answer="A", reason="The preceding reading says a narrow or low-volume bar shows uncertainty."),
        ),
        picture=FIG_74_CHECK,
        layout="beside",
        text_w=5.1,
        origin="Questions are ours and answerable from the preceding Figure 7.4 readings.",
    ),
    _p(_c("The bullish converse starts with the same question", (
        "We are now looking for the bullish converse: does the final bar close above the previous close or high while the broader trend is down?",
        "Gold [1] marks the final close above the previous close; red [2] the opening relationship; blue [3] the large range.",
        "A close above the previous high strengthens the bullish reading; a narrow or low-volume bar shows uncertainty.",
        "The crop has no volume panel, so volume is read from the surrounding book text, not from this image.",
        "A bullish pattern in a downtrend is a potential reversal. (Lim, p. 212.)",
    )), CHART_QM, companion=FIG_75, text_w=5.45),
    _p(_c("The remaining bullish forms turn the close upward", (
        "These forms keep the same bullish test: the final close must finish above the prior close or high.",
        "Gold [1] marks the final close above the prior close or high; red [2] the opening relationship; blue [3] the large range.",
        "Read the final close above the prior close or high; the crop's large near-high final bar is the visible clue.",
        "The figure has no volume panel; Lim discusses high volume around it.",
        "Bullish intrinsic sentiment in a downtrend is a potential reversal, not a guarantee.",
    )), CHART_QY, companion=FIG_75B, text_w=5.45),
    _p(_c("The seventh bullish form asks whether the close is convincing", (
        "The last bullish form still depends on the final close finishing above the prior high: the invented prior high is PHP 46.00 and the final close is PHP 47.20.",
        "The final bar runs from PHP 44.20 to PHP 47.20, so its range is PHP 3.00; its volume is 4.5 million shares.",
        "Gold [1] marks the final close; red [2] the opening relationship; blue [3] the large range.",
        "The crop's near-high close is the visible bullish reliability clue.",
        "The figure has no volume panel, so do not claim that blue [3] marks volume.",
        "Lim's qualifiers apply in the converse direction: potential, not certainty. (Lim, p. 212.)",
    )), CHART_QZ, companion=FIG_75C, text_w=5.45),

    _p(_c("In a triple bearish form, the gaps add pressure", (
        "We are looking at a triple bearish form, where gaps between the bars add to the pressure of the reversal reading.",
        "Here is an invented three-bar example with successive gaps of PHP 0.30, PHP 0.60, and PHP 1.10.",
        "Gold [1] marks the first gap, red [2] the middle bar, and blue [3] the larger final gap.",
        "A larger gap adds a stronger bearish clue in the triple pattern; the gap term keeps Chapter 3's meaning.",
        "The first three drawings share rules; they are not a shopping list of promises.",
    )), Chart(letter="QC", title="Chart QC: triple bearish gaps", shows="Three invented bars with gaps of PHP 0.30, PHP 0.60, and PHP 1.10 marked in the sequence.", marks=(
        Mark(1, "circle", .24, .22, .30, .30, color="gold", at=(.14, .16)),
        Mark(2, "circle", .48, .34, .54, .49, color="red", at=(.42, .60)),
        Mark(3, "line", .72, .62, .78, .62, color="blue", at=(.86, .54)),
    ), tier="core"), text_w=5.45),
    _p(_c("The first three triple bearish drawings", (
        "The book's first triple group uses the outer-bar closes and the gaps to frame the reversal.",
        "Gold [1] marks the first outer close, red [2] the middle bar, and blue [3] the final outer close.",
        "Pattern 1 can be more bearish when the middle bar has larger volume; larger first and third ranges help reliability.",
        "These are potential readings, not a complete trade plan. (Lim, p. 213.)",
    )), CHART_QN, companion=FIG_76, text_w=5.45),
    _p(_c("The triple pattern also compares ranges and volume", (
        "The triple bearish reading also asks how wide the three ranges are and whether the middle and final bars carry meaningful volume.",
        "Here is the invented example: the first range is PHP 3.0, the middle range PHP 0.8, and the final range PHP 3.4.",
        "Middle volume is 0.7 million; final volume is 4.2 million.",
        "Gold [1] marks the first wide range, red [2] the quiet middle range, and blue [3] the final wide range beside its 4.2 million volume.",
        "The middle bar is normally low volume, except pattern 1 can be more bearish with larger volume.",
        "A final bar that is overextended, near its low, and high volume is potentially more reliable.",
    )), Chart(letter="QD", title="Chart QD: triple ranges and volume", shows="Three invented bars with ranges PHP 3.0, PHP 0.8, PHP 3.4 and volumes 0.7m and 4.2m marked.", marks=(
        Mark(1, "circle", .24, .34, .32, .48, color="gold", at=(.14, .30)),
        Mark(2, "circle", .48, .36, .56, .46, color="red", at=(.42, .58)),
        Mark(3, "line", .76, .34, .76, .88, color="blue", at=(.88, .52)),
    ), tier="core"), text_w=5.45),
    _p(_c("The next triple bearish drawings add an island bar", (
        "Gold [1] marks the gap above the first bar; red [2] marks the island bar; blue [3] marks the final bearish bar.",
        "This crop shows the gap structure and the final close near the low. It has no volume panel.",
        "Lim discusses volume in the surrounding text, but this image cannot show it.",
        "The triple pattern is a potential reversal clue, not a trade guarantee. (Lim, p. 214.)",
    )), CHART_QO, companion=FIG_77, text_w=5.45),
    Check(
        label="Triple and multiple reversals",
        questions=(
            Q(stem="Why do larger gaps matter in the triple bearish forms?", options=(
                "They remove the trend", "They guarantee a top", "They define volume", "They add a stronger bearish clue"),
              answer="D", reason="Lim says larger gaps make the triple pattern more bearish."),
            Q(stem="Which final bearish bar is potentially more reliable?", options=(
                "Narrow, near high, low volume", "Overextended, near low, high volume", "Any middle bar", "Low range only"),
              answer="B", reason="The book's final-bar qualifiers are overextension, a near-low close, and high volume."),
        ),
        picture=FIG_76_CHECK,
        layout="beside",
        text_w=5.1,
        origin="Questions are ours and answerable from the preceding triple-pattern readings.",
    ),
    _p(_c("The bullish triple pattern reverses the outer closes", (
        "We are now reading the bullish triple form. Its outer bars reverse the close direction: the first is near its low and the final bar near its high.",
        "Gold [1], red [2], and blue [3] mark the first, middle, and final bars in the crop.",
        "The figure shows bar shape and close direction, but no volume panel. The course chart carries the invented volume example.",
        "The same potential range and volume tests apply in the bullish direction.",
    )), Chart(letter="QE", title="Chart QE: triple bullish outer bars", shows="Three invented bars with strong outer closes and a quiet middle bar.", marks=(
        Mark(1, "circle", .18, .55, .24, .61, color="gold", at=(.12, .58)),
        Mark(2, "circle", .46, .55, .52, .61, color="red", at=(.42, .64)),
        Mark(3, "circle", .74, .24, .80, .30, color="blue", at=(.86, .22)),
    ), tier="core"), text_w=5.45),
    _p(_c("The first three triple bullish drawings", (
        "The first three bullish drawings reverse the outer-bar close direction.",
        "Gold [1] marks the first bar, red [2] the middle bar, and blue [3] the final bar near its high.",
        "The figure has no volume panel. Use the course chart for the invented quiet-middle and high-volume comparison.",
        "Read the next group for the remaining three forms. (Lim, p. 214.)",
    )), CHART_QP, companion=FIG_78, text_w=5.45),
    _p(_c("The final bullish group uses the same volume test", (
        "The final bullish group asks whether the middle bar stays quiet while the final bar closes near its high.",
        "Here is the invented example: middle volume is 0.7 million and the final bar closes near its high.",
        "Gold [1] marks the quiet middle, red [2] the final high, and blue [3] the volume evidence.",
        "A high-volume final bar near its high can make the bullish reversal potentially more reliable.",
        "The figure's labels are observations; Chapter 7 does not define an oscillator formula here.",
    )), Chart(letter="QJ", title="Chart QJ: triple bullish final group", shows="The invented triple bullish bars, with the quiet middle and strong final close.", marks=(
        Mark(1, "circle", .46, .55, .52, .61, color="gold", at=(.42, .64)),
        Mark(2, "line", .74, .27, .80, .27, color="red", at=(.86, .22)),
        Mark(3, "line", .74, .81, .80, .81, color="blue", at=(.86, .88)),
    ), tier="core"), text_w=5.45),
    _p(_c("The next triple bullish drawings complete the group", (
        "Gold [1] marks the middle bar, red [2] the final high, and blue [3] the final volume column.",
        "The outer bars carry the bullish direction while the middle bar is commonly quieter.",
        "The course chart makes the volume evidence visible; the book figure has no volume panel.",
        "Keep the final-bar rule potential, not certain. (Lim, p. 215.)",
    )), CHART_QQ, companion=FIG_79, text_w=5.45),
    _p(_c("Multiple bearish forms can contain a volume exception", (
        "We are looking at multiple bearish forms, where the intermediate bars are usually quiet but one pattern allows a wide, high-volume exception.",
        "Here is the invented sequence: intermediate volumes are 0.6, 0.8, 3.8, and 0.7 million.",
        "Intermediate volume is normally low, but pattern 2 can be bearish with high volume.",
        "Gold [1] marks a gap, red [2] the intermediate bars, and blue [3] the final bar.",
        "Extremely high or low volume in a wide intermediate bar can also be bearish.",
    )), Chart(letter="QF", title="Chart QF: multiple bearish sequence", shows="Four invented bars with intermediate volume exceptions and a final bearish bar.", marks=(
        Mark(1, "circle", .34, .32, .42, .44, color="gold", at=(.28, .24)),
        Mark(2, "box", .44, .30, .68, .58, color="red", at=(.56, .24)),
        Mark(3, "line", .74, .61, .80, .61, color="blue", at=(.86, .60)),
    ), tier="core"), text_w=5.45),
    _p(_c("The bullish multiple forms reverse that sequence", (
        "The bullish multiple forms use the same idea in the other direction: intermediate bars are usually quiet, with a possible wide, high-volume exception.",
        "Here is the invented sequence: the two quiet middle volumes are 0.6 and 0.8 million shares; the wide exception is 3.8 million.",
        "The bullish converse normally has one narrow intermediate bar and a final close near its high.",
        "Gold [1] marks that narrow bar, red [2] the high-volume exception, and blue [3] the final close.",
        "In pattern 2, a wide-ranging intermediate bar on high or above-average volume can support the bullish reading.",
        "Narrow intermediate bars on very low volume show the quiet case.",
    )), Chart(letter="QG", title="Chart QG: multiple bullish sequence", shows="Four invented bars with quiet middle bars, a high-volume exception, and a final high close.", marks=(
        Mark(1, "circle", .38, .55, .45, .68, color="gold", at=(.30, .48)),
        Mark(2, "box", .54, .76, .66, .96, color="red", at=(.72, .70)),
        Mark(3, "line", .76, .26, .82, .26, color="blue", at=(.90, .16)),
    ), tier="core"), text_w=5.45),

    _p(_c("A continuation bar can confirm the trend", (
        "Continuation keeps the pattern aligned with an uptrend when a later bar breaks the previous high.",
        "Invented example: prior high PHP 52.00; second high PHP 53.20, with volume 4.0 million versus 2.0 million.",
        "Gold [1] marks the prior high, red [2] the breach, and blue [3] the high volume.",
        "The second bar breaches the previous high on high volume, so intrinsic and trend sentiment agree.",
        "This is continuation, not a reversal. (Lim, p. 216.)",
    )), Chart(letter="QH", title="Chart QH: bullish continuation breach", shows="Two invented PHP bars: the second breaches prior high 52.00 at 53.20 on 4.0 million shares.", marks=(
        Mark(1, "line", .18, .35, .80, .35, color="gold", at=(.14, .30)),
        Mark(2, "line", .70, .20, .75, .20, color="red", at=(.75, .30)),
        Mark(3, "circle", .68, .78, .78, .93, color="blue", at=(.84, .88)),
    ), tier="core"), text_w=5.45),
    _p(_c("The book's first continuation example breaks the prior high", (
        "We are checking the same continuation rule in the book figure: the second bar takes out the previous high and closes near its high.",
        "Gold [1] marks the prior high, red [2] the breach, and blue [3] the second bar closing near its high.",
        "The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "Lim presents this as a bullish continuation example, where the pattern and trend agree.",
        "The bearish reverse uses the same structure downward. (Lim, p. 216.)",
    )), CHART_QT, companion=FIG_712, text_w=5.45),
    _p(_c("A 50 percent retrace can still continue the trend", (
        "The second bullish continuation pattern starts with a retracement to the 50 percent level, then asks whether price rebounds through the old high.",
        "Here is the invented example. The previous bar runs from PHP 48.00 to PHP 52.00, so its 50 percent level is PHP 50.00.",
        "The next price retraces to PHP 50.00, rebounds to PHP 52.40 on 4.0 million shares, and breaches PHP 52.00.",
        "Gold [1] marks the midpoint, red [2] the rebound, and blue [3] the breach.",
        "Lim says large volume on the second bar may mean the trend remains potentially strong.",
    )), Chart(letter="QI", title="Chart QI: bullish 50 percent retrace", shows="An invented PHP 48.00 to PHP 52.00 bar, midpoint 50.00, then a rebound through 52.00 to 52.40.", marks=(
        Mark(1, "circle", .42, .56, .48, .62, color="gold", at=(.36, .64)),
        Mark(2, "circle", .75, .28, .81, .36, color="red", at=(.66, .40)),
        Mark(3, "line", .78, .23, .84, .23, color="blue", at=(.90, .20)),
    ), tier="core"), text_w=5.45),
    Check(
        label="Continuation bars",
        questions=(
            Q(stem="What does bullish continuation pattern 1 show?", options=(
                "A gap down", "A lower close", "A second bar closing near its high", "A close below support"),
              answer="C", reason="The Figure 7.12 crop shows a second bar closing near its high after the prior bar."),
            Q(stem="What makes pattern 2 bullish continuation?", options=(
                "It stops at the midpoint", "It makes no new high", "It uses only volume", "50% retrace, then breach old high"),
              answer="D", reason="Pattern 2 needs a 50 percent retrace, then a rebound above the old high."),
        ),
        picture=FIG_712_CHECK,
        layout="beside",
        text_w=5.1,
        origin="Questions are ours and answerable from the preceding continuation slides.",
    ),
    _p(_c("The book's second continuation example retraces halfway", (
        "Gold [1] marks the first continuation bar, red [2] the midpoint retrace, and blue [3] the rebound above it.",
        "The book labels the midpoint as 50% of the first bar. The crop has no volume panel.",
        "The second bar rebounds to the upside. The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "The bearish reverse applies the same structure downward. (Lim, p. 216.)",
    )), CHART_QU, companion=FIG_712B, text_w=5.45),

    _c("Four characteristics show a move losing energy", (
        "We are starting the 16 reversal characteristics with the way a price move can lose energy before a reversal or retracement.",
        "Characteristics 1 and 2 are cycle amplitude and cycle period: amplitude decreases from 40 to 30 points, while period decreases from 20 to 12 bars.",
        "Characteristics 3 and 4 are bar retracement symmetry and average range: symmetry changes from 28, 30, and 26 bars to 14 bars, while range falls from 3.0 to 2.0.",
        "These are invented values showing the direction. The characteristics indicate potential, never certainty.",
    )),
    _p(_c("Four more characteristics describe weaker follow-through", (
        "Characteristics 5 to 8 ask whether price persists and bar measures weaken.",
        "Characteristic 5 is price persistence, whose quality falls; characteristic 6 is bar stochastic, which falls from 0.80 to 0.40.",
        "Characteristic 7 is BRR, taught in Chapter 5, and falls from 0.60 to 0.25; characteristic 8 is angular symmetry and momentum, changing from 20 to 35 degrees.",
    ), accent="The book's terms stay connected to their earlier FIN1209 definitions."), CHART_QV, text_w=5.45),
    Check(
        label="The 16 characteristics, first half",
        questions=(
            Q(stem="Which earlier chapter taught BRR, the real body to range ratio?", options=(
                "Chapter 8", "Chapter 5", "Chapter 1", "Not named"),
              answer="B", reason="Chapter 5 taught the real body to range ratio, recalled here as characteristic 7."),
            Q(stem="Which characteristic names angular symmetry and momentum?", options=(
                "6", "7", "8", "16"),
              answer="C", reason="Characteristic 8 is changes in angular symmetry and momentum."),
        ), picture=CHART_QV, layout="beside", text_w=5.0,
        origin="Questions are ours and answerable from the preceding numbered list.",
    ),
    _c("Location and consolidation add four more warnings", (
        "Characteristics 9 to 12 move from bar behaviour to context: barrier proximity, fewer oscillations, larger consolidation, and an exhaustion gap.",
        "Characteristic 9 is PHP 1.00 below resistance; characteristic 10 is fewer or shallower oscillations, from 6 to 2.",
        "Characteristic 11 is consolidation becoming larger and longer, from 3 to 12 bars; characteristic 12 is an exhaustion gap at PHP 0.80.",
        "The gap and barrier terms keep the meanings taught in Chapters 3 and 5.",
    ), accent="The location of the pattern matters as much as its shape."),
    _c("The last four characteristics combine range, volume, and divergence", (
        "Characteristics 13 to 16 ask whether the move is nearly complete, overextended, unusually active, or diverging.",
        "Characteristics 13 and 14 are range completion at 9 of 10 points and overextension at PHP 1.00 above resistance.",
        "Characteristics 15 and 16 are extreme volume at 5.0 million versus 1.2 million and standard divergence. Chapter 7 gives no oscillator formula.",
    ), accent="The list ends with range completion, overextension, volume, and divergence."),
    _p(_c("Three reversal warnings appear together", (
        "We are using this warning chart to see several reversal characteristics on one price path: changing momentum, fewer oscillations, and overextension.",
        "Here is our invented path: price rises from PHP 40.00 to PHP 80.00 in 12 bars, with only two pullbacks.",
        "Gold [1] marks characteristic 8, changing angular rise and momentum; red [2] marks characteristic 10, the few oscillations.",
        "Blue [3] marks characteristic 14, the overextended bar against the upper band.",
        "The book names the Bollinger upper band but never gives its formula here. These are potential warnings, not certainty.",
    )), CHART_QK, companion=FIG_713, text_w=5.45),
    _p(_c("The book figure shows reversal context", (
        "Gold [1] marks characteristic 8, the exponential rise and changing momentum; red [2] marks characteristic 10, the few trend oscillations.",
        "Blue [3] marks characteristic 14, price overextension against the Bollinger upper band.",
        "The figure has no separate volume panel, so this reading does not mark volume.",
        "Read the chart as potential evidence, then apply the barrier rule.",
    )), FIG_713, text_w=5.45),
    _p(_c("Barrier proximity is the reliability rule", (
        "Lim defines barrier proximity as one of the most important reversal characteristics: patterns are more reliable at significant barriers.",
        "In Chart RF, gold [1] marks the changing rise, red [2] the visible oscillating segment, and blue [3] the overextended bar against the upper band.",
        "The upper band is the visible barrier in this book figure. The scan does not provide a numeric barrier level.",
        "Check the pattern's barrier context. A barrier raises potential reliability, not certainty.",
    )), CHART_RF, companion=FIG_713, text_w=5.45),
    Check(
        label="The 16 characteristics",
        questions=(
            Q(stem="Which item is proximity to a price barrier?", options=("8", "10", "14", "9"),
              answer="D", reason="Characteristic 9 is proximity to a price barrier."),
            Q(stem="Which three characteristics do Figure 7.13's marks show?", options=(
                "8, 10, and 14", "1, 2, and 3", "5, 7, and 9", "13, 15, and 16"),
              answer="A", reason="The figure reads characteristic 8, fewer oscillations in 10, and overextension against a barrier in 14."),
        ),
        picture=FIG_713_CHECK,
        layout="beside",
        text_w=5.1,
        origin="Questions are ours and answerable from the preceding numbered list and Figure 7.13.",
    ),
    _p(_c("The 16 characteristics point to a potential change", (
        "Item 9 is proximity to a price barrier, one of the most important reversal characteristics.",
        "Figure 7.13's marks read characteristics 8, 10, and 14: angular change and momentum, fewer oscillations, and overextension against a barrier.",
        "The book says these are strong indications of a potential trend change or retracement, not a guarantee.",
        "Part 3 now applies the context to named reversal bars.",
    )), FIG_713, text_w=5.45),
    _p(_c("Let us read the first dedicated bearish figure", (
        "We are matching the book's drawing to the generic bearish test: gold [1] points to the final close, red [2] to the opening relationship, and blue [3] to the large range.",
        "The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "The book's wording is generally and potentially: context changes reliability.",
        "Next we compare the bullish converse.",
    )), CHART_RG, companion=FIG_74, text_w=5.45),
    _p(_c("Now let us read the dedicated bullish figure", (
        "We are matching the bullish converse to its book drawing: the formation closes above the prior close or high.",
        "On our course chart, gold [1] points to the final close, red [2] to the opening relationship, and blue [3] to the large range.",
        "The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "A bullish pattern in a downtrend is a potential reversal; the same bias in an uptrend is continuation.",
    )), CHART_RH, companion=FIG_75, text_w=5.45),
    _p(_c("The dedicated multiple-bearish figure shows the final turn", (
        "We are reading the multiple-bearish family from left to right: a high first close, narrow intermediate bars, and a final close near its low.",
        "Gold [1] marks the first bar, red [2] the intermediate sequence, and blue [3] the final bearish bar.",
        "The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "The final bar remains the potential decision point.",
    )), CHART_QR, companion=FIG_710, text_w=5.45),
    _p(_c("The dedicated multiple-bullish figure reverses that direction", (
        "We are reading the multiple-bullish family as the directional converse of Figure 7.10.",
        "Gold [1] marks the first bar, red [2] the narrow middle sequence, and blue [3] the final close near its high.",
        "The book crop has no volume panel; the course chart adds invented volume only to illustrate Lim's surrounding comment.",
        "The figure supplies a potential reading, not a complete trade plan.",
    )), CHART_QS, companion=FIG_711, text_w=5.45),
    _p(_c("The dedicated warning chart keeps the context visible", (
        "We are checking the same three context clues in the book figure: gold [1] marks changing angular momentum, red [2] fewer oscillations, and blue [3] overextension at the upper band.",
        "The crop has no separate volume panel, so this marked reading does not claim high volume.",
        "Bollinger Bands are named but not defined in Chapter 7, so no formula is imported.",
        "Barrier proximity is the next reliability rule.",
    )), FIG_713, text_w=5.45),
)


def _chart_reading_slides(slides):
    """Keep every authored chart at projected-reading width.

    A chart paired with a book crop cannot make both visuals large beside a
    full teaching paragraph. The teaching paragraph therefore keeps the
    course chart at the right-hand 4.2-inch text / 7.58-inch chart split, and
    the copyrighted crop follows on its own Figure slide. This keeps the
    source drawing readable without shrinking our chart below the 55 percent
    slide-width rule.
    """
    expanded = []
    for slide in slides:
        if not isinstance(slide, Pair) or not isinstance(slide.picture, Chart):
            expanded.append(slide)
            continue
        first_count = 2
        first = Content(
            title=slide.left.title,
            lines=slide.left.lines[:first_count],
            accent=slide.left.accent,
            caption=slide.left.caption,
            notes=slide.left.notes,
            origin=slide.left.origin,
        )
        first_pair = Pair(
            left=first,
            picture=slide.picture,
            text_w=4.55,
            picture_extra=0.75,
            notes=slide.notes,
            origin=slide.origin,
        )
        first_pair.companion = None
        expanded.append(first_pair)
        if len(slide.left.lines) > first_count:
            remaining = slide.left.lines[first_count:]
            # The continuation is deliberately a text-only transition. Any
            # line that reads a mark, chart, figure, crop, or slide belongs
            # on the picture slide itself; carrying it here would leave a
            # student with a sentence whose evidence is not on the slide.
            picture_words = ("mark", "chart", "figure", "crop", "slide",
                             "picture", "image")
            carry = tuple(line for line in remaining
                          if not any(word in line.lower()
                                     for word in picture_words))
            continuation = Content(
                title="Carry this rule into the next step",
                lines=((f"Continuing this rule: {carry[0]}" if carry else
                        "Carry this rule into the next worked example."),),
                notes=slide.left.notes,
                origin=slide.left.origin,
            )
            expanded.append(continuation)
        if slide.companion is not None:
            companion = slide.companion
            companion_pair = Pair(
                left=Content(
                    title=getattr(companion, "reading_title", companion.title),
                    lines=getattr(companion, "reading_lines", (
                        companion.shows,
                        "The marked crop carries the same numbered reading as the course chart.",
                        "Carry this potential rule into the next example.",
                    )),
                    notes=companion.notes,
                    origin=companion.credit,
                ),
                picture=companion,
                text_w=4.2,
                notes=companion.notes,
                origin=companion.credit,
            )
            companion_pair.companion = None
            expanded.append(companion_pair)
    return tuple(expanded)


SECTION2_SLIDES = _chart_reading_slides(SECTION2_SLIDES)

SECTION2 = Section(
    number=2,
    title="Reading a Pattern",
    short="7.2 Pattern reading",
    minutes="",
    covers=("continuation", "reversal", "16 characteristics"),
    slides=SECTION2_SLIDES,
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
                title="Bearish key reversal: numbers first",
                lines=(
                    "Read the prior high and close first.",
                    "1. Open 52.30 above prior high 52.00 [1].",
                    "2. New high 53.20 [2]. 3. Close 50.80 below prior close 51.10 [3].",
                    "4. Volume 4.2m versus 2.0m [4].",
                    "Meaning/action: bearish key reversal, a potential warning (Lim, p. 218).",
                ),
                accent="",
                caption="",
            ),
            picture=KEY_WORKED_CHART,
            text_w=4.0,
            picture_extra=0.1,
            notes=KEY_WORKED_CHART.notes,
            origin=KEY_WORKED_CHART.origin,
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
            text_w=7.0,
            notes=BULLISH_FIGURE.notes,
            origin=BULLISH_FIGURE.origin,
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
            text_w=7.3,
            notes=KEY_READ_FIGURE.notes,
            origin=KEY_READ_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Exhaustion bar versus pin bar",
                lines=(
                "Before the key-reversal check, compare two one-bar warnings: exhaustion has no following gap; pin falsely penetrates a barrier.",
                "Exhaustion O65.40 > prior high65.00; H66.20; next O60.20 means no gap. Pin support40.00; low38.80; C40.60; return.",
                "Meaning/action: exhaustion warns a tiring trend; pin warns of a false breakout.",
                ),
                accent="",
                caption="",
            ),
            picture=COMPARISON_CHART,
            text_w=4.0,
            picture_extra=0.8,
            notes=COMPARISON_CHART.notes,
            origin=COMPARISON_CHART.origin,
        ),
        KEY_CHECK,
        SECOND_CHECK,
        KEY_CAVEAT,
        KEY_CONTEXT,
        KEY_16_PAIR,
        TWO_DAY_WORKED,
        TWO_DAY_READ,
        THREE_WORKED,
        THREE_BEAR_READ,
        THREE_BULL_READ,
        THREE_CONTEXT_PAIR,
        THREE_OUTSIDE_PAIR,
        THREE_PATTERN6_PAIR,
        TRIPLE_CHECK,
        ISLAND_WORKED,
        ISLAND_READ,
        ISLAND_CHECK,
        *B4_SLIDES,
    ),
)

OOPS_FIGURE = Figure(
    title="Figure 7.36: Williams' Oops entry",
    number="7.36",
    aspect=920 / 450,
    crop=(),
    marks=(
        Mark(1, "line", 0.16, 0.66, 0.29, 0.66,
             color="gold", at=(0.12, 0.55), size=0.30),
        Mark(2, "line", 0.30, 0.57, 0.46, 0.57,
             color="red", at=(0.51, 0.52), size=0.30),
        Mark(3, "line", 0.30, 0.75, 0.48, 0.75,
             color="blue", at=(0.53, 0.81), size=0.30),
    ),
    shows=("The book's two Williams' Oops schematics: a gap below the prior "
           "range with a buy-stop at the prior low, and a gap above it with "
           "a sell-stop at the prior high; each stoploss is at the new extreme."),
    notes=(
        "Read the left setup first, then the exact directional converse on the right.",
        "Mark 1 is the opening gap, mark 2 is the prior-bar trigger level, and mark 3 is the stoploss at the new extreme.",
        "If price reverses through the stoploss, the book says to stop and reverse.",
    ),
    origin="Lim (2016), p. 231, Figure 7.36. The numbered marks are for teaching.",
)

OOPS_EXAMPLE_FIGURE = Figure(
    title="Figure 7.37: bearish Williams' Oops example",
    number="7.37",
    aspect=750 / 338,
    crop=(),
    marks=(
        Mark(1, "circle", 0.735, 0.55, 0.79, 0.68,
             color="gold", at=(0.68, 0.70), size=0.30),
        Mark(2, "line", 0.78, 0.615, 0.91, 0.615,
             color="red", at=(0.72, 0.48), size=0.30),
        Mark(3, "line", 0.78, 0.565, 0.91, 0.565,
             color="blue", at=(0.72, 0.52), size=0.30),
    ),
    shows=("The book's daily Dynegy chart marked at the bearish Oops opening "
           "gap, sell-stop at the prior high, stop-and-reverse buy level, and "
           "expected downside move."),
    notes=(
        "The crop enlarges the Oops annotations and leaves the price sequence visible.",
        "The book gives a bearish example; the exact order rule was defined on the previous slide.",
        "Keep this as a potential setup. The book does not give a complete trade plan here.",
    ),
    origin="Lim (2016), p. 231, Figure 7.37. The crop and marks are for teaching.",
)

OOPS_CONTEXT_FIGURE = Figure(
    title="Figure 7.36: Oops context",
    number="7.36",
    aspect=920 / 450,
    marks=(
        Mark(1, "circle", 0.25, 0.43, 0.33, 0.55,
             color="gold", at=(0.20, 0.38), size=0.30),
        Mark(2, "circle", 0.69, 0.43, 0.77, 0.55,
             color="red", at=(0.84, 0.38), size=0.30),
    ),
    shows=("Figure 7.36's two Oops panels, with marks on the bullish and "
           "bearish setups; the chapter's named candlestick companions are "
           "not shown or defined here."),
    notes=(
        "Use mark 1 for the buy setup and mark 2 for the sell setup. The exact order levels were defined on the earlier slides.",
        "The companion names are not attached to an unrelated mark. Chapter 7 does not define or show them here.",
    ),
    origin="Lim (2016), p. 231, Figure 7.36. The numbered marks are for teaching.",
)

IDNR_FIGURE = Figure(
    title="Figure 7.38: ID/NR6",
    number="7.38",
    aspect=493 / 503,
    crop=(0.015, 0.0, 0.015, 0.0),
    marks=(
        Mark(1, "box", 0.00, 0.04, 0.43, 0.84,
             color="gold", at=(0.48, 0.90), size=0.30),
        Mark(2, "box", 0.36, 0.54, 0.43, 0.75,
             color="red", at=(0.47, 0.48), size=0.30),
        Mark(3, "box", 0.47, 0.54, 0.70, 0.79,
             color="blue", at=(0.73, 0.53), size=0.30),
    ),
    shows=("The book's ID/NR6 schematic: six numbered bars, with the sixth "
           "bar inside the prior range and the narrowest range, followed by "
           "long and short trigger levels."),
    notes=(
        "Count the last six bars in the source schematic, then locate its final inside bar and narrowest range.",
        "The two trigger arrows show that direction is not built into ID/NR.",
        "The next slide extends the same count to NR4, NR5, NR6, and NR7.",
    ),
    origin="Lim (2016), p. 232, Figure 7.38. The numbered marks are for teaching.",
)

IDNR_DIRECTION_FIGURE = Figure(
    title="Figure 7.38: neutral until breakout",
    number="7.38",
    aspect=493 / 503,
    marks=(
        Mark(1, "line", 0.36, 0.58, 0.36, 0.74,
             color="gold", at=(0.31, 0.50), size=0.30),
        Mark(2, "box", 0.34, 0.54, 0.43, 0.75,
             color="red", at=(0.47, 0.48), size=0.30),
        Mark(3, "box", 0.47, 0.54, 0.70, 0.79,
             color="blue", at=(0.73, 0.53), size=0.30),
    ),
    shows=("Figure 7.38's ID/NR6 schematic, with the narrowest inside bar "
           "and both possible trigger directions visible."),
    notes=(
        "Mark 1 is the narrowest final bar and mark 2 boxes its inside relationship with the prior bar.",
        "Mark 3's top and bottom edges sit on the printed long and short trigger levels; either direction is possible before the break.",
    ),
    origin="Lim (2016), p. 232, Figure 7.38. The numbered marks are for teaching.",
)

INSIDE_MONTH_FIGURE = Figure(
    title="Figure 7.39: Inside Month/NR5",
    number="7.39",
    aspect=688 / 316,
    marks=(
        Mark(1, "circle", 0.325, 0.59, 0.365, 0.70,
             color="gold", at=(0.30, 0.74), size=0.30),
        Mark(2, "arrow", 0.10, 0.88, 0.36, 0.88,
             color="red", at=(0.50, 0.92), size=0.30),
        Mark(3, "circle", 0.375, 0.18, 0.425, 0.70,
             color="blue", at=(0.45, 0.15), size=0.30),
    ),
    shows=("The book's monthly Dynegy chart: an inside month after five "
           "monthly ranges, followed by an upside breakout."),
    notes=(
        "This is the monthly extension, not an ordinary daily ID/NR example.",
        "Mark 1 identifies the inside month, mark 2 spans the five-month range count, and mark 3 is on the first upside breakout bar.",
        "The count and neutral direction rule remain the same before breakout.",
    ),
    origin="Lim (2016), p. 232, Figure 7.39. The numbered marks are for teaching.",
)

TRIPLE_BEARISH_FIGURE = Figure(
    title="Figure 7.6: two bearish triple-bar structures",
    number="7.06",
    aspect=650 / 550,
    marks=(
        Mark(1, "box", 0.07, 0.02, 0.34, 0.34,
             color="gold", at=(0.05, 0.38), size=0.30),
        Mark(2, "box", 0.40, 0.02, 0.57, 0.34,
             color="red", at=(0.38, 0.38), size=0.30),
        Mark(3, "circle", 0.15, 0.33, 0.24, 0.63,
             color="blue", at=(0.10, 0.30), size=0.30),
    ),
    shows=("Figure 7.6's three bearish triple-bar schematics, with the first "
           "two structures marked for the review answer."),
    notes=(
        "Gold mark 1 brackets pattern 1 and red mark 2 brackets pattern 2.",
        "Blue mark 3 sits beside the source's uptrend context. Read the source conditions rather than inventing a trade rule.",
    ),
    origin="Lim (2016), p. 213, Figure 7.6. The numbered marks are for teaching.",
)

INSIDE_BAR_FIGURE = Figure(
    title="Figure 7.25: bearish inside-day reversal",
    number="7.25",
    aspect=672 / 402,
    marks=(
        Mark(1, "circle", 0.57, 0.15, 0.63, 0.39,
             color="gold", at=(0.53, 0.10), size=0.30),
        Mark(2, "circle", 0.67, 0.15, 0.73, 0.39,
             color="red", at=(0.77, 0.10), size=0.30),
        Mark(3, "circle", 0.58, 0.69, 0.65, 0.86,
             color="blue", at=(0.72, 0.91), size=0.30),
    ),
    shows=("Figure 7.25's ITC Holdings chart, with the wide first bar, the "
           "narrow inside bar, and the lower oscillator region marked."),
    notes=(
        "Gold mark 1 identifies the wide first bar near resistance; red mark 2 identifies the narrow inside bar.",
        "Blue mark 3 identifies the lower oscillator region shown in the source. Chapter 7 does not teach its calculation.",
    ),
    origin="Lim (2016), p. 225, Figure 7.25. The numbered marks are for teaching.",
)

OSCILLATOR_BOUNDARY_FIGURE = Figure(
    title="Figure 7.13: the labelled oscillator region",
    number="7.13",
    aspect=1200 / 600,
    marks=(
        Mark(1, "box", 0.76, 0.73, 0.94, 0.84,
             color="gold", at=(0.95, 0.70), size=0.30),
    ),
    shows=("Figure 7.13's overextension chart, with mark 1 on the lower "
           "labelled oscillator region."),
    notes=(
        "Point to the lower labelled oscillator region, not to a formula.",
        "The book uses the label as context in Chapter 7; the method is deferred to Chapter 8.",
    ),
    origin="Lim (2016), p. 218, Figure 7.13. The numbered mark is for teaching.",
)

OOPS_CHART = Chart(
    letter="TA",
    title="Williams' Oops: invented numbers",
    shows=("An invented bullish Oops example with every relevant price written "
           "on the chart: a gap-up open, sell-stop at the prior high, and "
           "stoploss at the new high."),
    tier="core",
    marks=(
        Mark(1, "arrow", 0.67, 0.50, 0.67, 0.37,
             color="gold", at=(0.75, 0.43), size=0.30),
        Mark(2, "circle", 0.61, 0.45, 0.67, 0.51,
             color="red", at=(0.75, 0.50), size=0.30),
        Mark(3, "circle", 0.61, 0.12, 0.67, 0.18,
             color="blue", at=(0.75, 0.14), size=0.30),
    ),
    notes=(
        "The previous bar closes at 51.00 and has a high of 52.00. The next bar opens at 53.00, so it gaps above the prior range.",
        "The sell-stop is 52.00, the prior high. The stoploss is 54.00, the new bar's high.",
    ),
    origin="Chart TA is ours, with invented PHP values to show Lim (2016), p. 231.",
)

OOPS_BULLISH_CHART = Chart(
    letter="V",
    title="Williams' Oops: bullish converse values",
    shows=("An invented bullish Oops example with the prior low, gap-down open, "
            "buy-stop, and new low with stoploss labelled on the chart."),
    tier="core",
    marks=(
        Mark(1, "arrow", 0.67, 0.55, 0.67, 0.65,
             color="gold", at=(0.76, 0.58), size=0.30),
        Mark(2, "line", 0.39, 0.54, 0.63, 0.54,
             color="red", at=(0.78, 0.47), size=0.30),
        Mark(3, "line", 0.39, 0.84, 0.63, 0.84,
             color="blue", at=(0.80, 0.87), size=0.30),
    ),
    notes=(
        "The previous bar's low is PHP 48.00. The next bar opens at PHP 47.00, below that low.",
        "The buy-stop is PHP 48.00 and the new low and stoploss are PHP 46.00.",
    ),
    origin="Chart V is ours, with invented PHP values to show Lim (2016), p. 231.",
)

IDNR_CHART = Chart(
    letter="TB",
    title="ID/NR6: invented ranges",
    shows=("Six invented daily bars with ranges 4.0, 3.2, 2.8, 2.1, 1.6, "
           "and 1.2 PHP; the sixth is inside the fifth and is the narrowest."),
    tier="core",
    marks=(
        Mark(1, "box", 0.68, 0.25, 0.84, 0.43,
             color="gold", at=(0.63, 0.48), size=0.30),
        Mark(2, "line", 0.80, 0.22, 0.80, 0.43,
             color="red", at=(0.88, 0.47), size=0.30),
        Mark(3, "line", 0.73, 0.21, 0.73, 0.40,
             color="blue", at=(0.68, 0.55), size=0.30),
    ),
    notes=(
        "The six range labels are invented teaching numbers. Compare each with the same six-bar window.",
        "The last bar is the narrowest and remains inside the prior bar. A later break can go up or down.",
    ),
    origin="Chart TB is ours, with invented PHP ranges to show Lim (2016), p. 232.",
)

INSIDE_MONTH_CHART = Chart(
    letter="W",
    title="Inside Month/NR5: invented worked example",
    shows=("Six invented monthly bars with ranges 12, 10, 9, 7, and 5 PHP; "
            "the fifth is inside the fourth, followed by an upward break "
            "through PHP 31.00."),
    tier="core",
    marks=(
        Mark(1, "box", 0.53, 0.38, 0.70, 0.59,
             color="gold", at=(0.49, 0.63), size=0.30),
        Mark(2, "line", 0.67, 0.39, 0.67, 0.55,
             color="red", at=(0.74, 0.63), size=0.30),
        Mark(3, "circle", 0.78, 0.18, 0.84, 0.49,
             color="blue", at=(0.91, 0.55), size=0.30),
    ),
    notes=(
        "The five counted monthly ranges are 12, 10, 9, 7, and 5 PHP; the fifth bar is inside the fourth.",
        "The sixth bar breaks above PHP 31.00. The example is invented to show the extension.",
    ),
    origin="Chart W is ours, with invented monthly PHP values to show Lim (2016), p. 232.",
)

SECTION4 = Section(
    number=4,
    title="Volatility-Based Breakouts",
    short="7.4 Volatility breakouts",
    minutes="16 minutes",
    covers=("Williams’ Oops", "ID/NR4 to NR7"),
    slides=(
        Pair(
            left=Content(
                title="Williams' Oops: gap up and reverse",
                lines=(
                    "Plain words: an Oops begins when a bar opens beyond the previous bar's range. After a gap up, the bearish setup places a sell-stop at the previous high and the stoploss at the new high.",
                    "Ours: prior high PHP 52.00; new open PHP 53.00; sell-stop PHP 52.00; new high and stoploss PHP 54.00 [1] [2] [3].",
                    "If price reverses through the stoploss, stop and reverse there. Lim says to seek this bearish Oops in a downtrend.",
                ),
                accent="Gap up means bearish Oops; gap down is its bullish converse.",
                caption="Lim (2016), p. 231. Values are ours, invented to show the order sequence.",
            ),
            picture=OOPS_CHART,
            text_w=6.8,
            picture_extra=0.2,
            notes=OOPS_CHART.notes,
            origin=OOPS_CHART.origin,
        ),
        Pair(
            left=Content(
                title="Figure 7.36: both Oops directions",
                lines=(
                    "Definition: an Oops opens beyond the previous bar's range. Left [1] gaps down: buy-stop at previous low [2], stoploss at new low [3].",
                    "Right is the unmarked converse: gap up, sell-stop at previous high, stoploss at new high.",
                    "Action: if price reverses, stop and reverse at the stoploss. The book promises no result.",
                ),
                accent="Read the bearish and bullish order locations as exact opposites.",
                caption="Lim (2016), p. 231. The four named candlestick companions are not defined in Chapter 7.",
            ),
            picture=OOPS_FIGURE,
            text_w=6.8,
            picture_extra=0.1,
            notes=OOPS_FIGURE.notes,
            origin=OOPS_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Williams' Oops: gap down and reverse",
                lines=(
                    "The bullish converse opens below the previous low. Ours: prior low PHP 48.00; new open PHP 47.00; buy-stop PHP 48.00; new low and stoploss PHP 46.00 [1] [2] [3].",
                    "If price reverses through PHP 46.00, stop and reverse at that stoploss. Lim says to seek this bullish Oops in an uptrend.",
                    "Morning star, evening star, piercing line, and dark cloud cover are named as possible companions, not defined here.",
                ),
                accent="Gap down means bullish Oops; gap up is its bearish converse.",
                caption="Lim (2016), p. 231. Values are ours, invented to show the bearish converse.",
            ),
            picture=OOPS_BULLISH_CHART,
            text_w=6.8,
            picture_extra=0.15,
            notes=OOPS_BULLISH_CHART.notes,
            origin=OOPS_BULLISH_CHART.origin,
        ),
        Pair(
            left=Content(
                title="Figure 7.37: a bearish Oops on a daily chart",
                lines=(
                    "Dynegy shows a bearish Oops: mark [1] is the opening gap, [2] the sell-stop at the previous high, and [3] the current high where stop-and-reverse buys.",
                    "The expected downside is the book's chart annotation, not a guarantee.",
                    "The four companion names remain undefined here; import no outside formula.",
                ),
                accent="The example applies the rule; it does not complete a trade plan.",
                caption="Lim (2016), p. 231, Figure 7.37. The figure is a Dynegy daily chart.",
            ),
            picture=OOPS_EXAMPLE_FIGURE,
            text_w=6.8,
            picture_extra=0.1,
            notes=OOPS_EXAMPLE_FIGURE.notes,
            origin=OOPS_EXAMPLE_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Oops context and undefined companions",
                lines=(
                    "Prefer bullish Oops in an uptrend and bearish Oops in a downtrend. Figure 7.36 shows the directions [1] [2].",
                    "The book names morning star, evening star, piercing line, and dark cloud cover, but Figure 7.36 does not show them.",
                    "Chapter 7 defines none of the four; they are context names only.",
                ),
                accent="Context chooses which Oops direction to study; the chapter leaves the companion definitions open.",
                caption="Lim (2016), p. 231. The named candlestick companions are not defined in this chapter.",
            ),
            picture=OOPS_CONTEXT_FIGURE,
            text_w=6.8,
            picture_extra=0.05,
            notes=OOPS_CONTEXT_FIGURE.notes,
            origin=OOPS_CONTEXT_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="ID/NR: inside day plus narrowest range",
                lines=(
                    "Plain words: ID/NR means an inside-day breakout from the narrowest bar in the last n days. An inside day stays within the previous day's high and low.",
                    "Ours: six ranges are 4.0, 3.2, 2.8, 2.1, 1.6, and 1.2 PHP. Bar 6 is inside bar 5 [1] and has the narrowest range [2].",
                    "A later breakout can occur in either direction [3]. The pattern is a volatility breakout, not a bullish or bearish signal by itself.",
                ),
                accent="Count the window first, then wait for direction from the breakout.",
                caption="Lim (2016), p. 232. Ranges are ours, invented to show the six-bar count.",
            ),
            picture=IDNR_CHART,
            text_w=7.2,
            picture_extra=0.2,
            notes=IDNR_CHART.notes,
            origin=IDNR_CHART.origin,
        ),
        Pair(
            left=Content(
                title="Figure 7.38: ID/NR6",
                lines=(
                    "The book's schematic shows the last six bars counted for ID/NR6 [1]. The final bar is inside the prior range [2] and is the narrowest of those six [3].",
                    "Lim calls this an ID/NR6 volatility breakout. It has no bearish or bullish sentiment before the breakout, so either trigger direction remains possible.",
                    "Meaning/action: identify the exact n-day window and the inside condition before reading the breakout.",
                ),
                accent="The number 6 names the count, not a direction.",
                caption="Lim (2016), p. 232, Figure 7.38.",
            ),
            picture=IDNR_FIGURE,
            text_w=6.5,
            picture_extra=0.15,
            notes=IDNR_FIGURE.notes,
            origin=IDNR_FIGURE.origin,
        ),
        Content(
                title="ID/NR4, NR5, NR6, and NR7",
                lines=(
                    "The n in ID/NR n is the number of bars counted: ID/NR4 counts four, NR5 counts five, NR6 counts six, and NR7 counts seven.",
                    "Ours: separate invented windows make the arithmetic visible: NR4 ranges 3.1, 2.4, 2.0, 1.6 PHP; NR5 adds 1.2 PHP; NR6 adds 1.8 PHP; NR7 adds 1.0 PHP.",
                    "Every version still needs the inside-day condition. The label says how far back to count, not which way price must break.",
                ),
                accent="A volatility breakout compresses recent range; direction comes later.",
                caption="Lim (2016), p. 232. The comparative ranges are ours, invented to show the n-day windows.",
            notes=(
                "Use the marked schematic as the anchor, then read the four window lengths from the body.",
                "The book defines the pattern in words rather than giving these comparative ranges; they are ours.",
            ),
            origin="Lim (2016), p. 232. The comparative ranges are ours, invented.",
        ),
        Pair(
            left=Content(
                title="ID/NR has no built-in direction",
                lines=(
                    "The inside and narrowest-range conditions describe compression, not sentiment. Figure 7.38 marks the narrowest bar [1] and its inside condition [2].",
                    "Before the breakout, the same setup can trigger long or short [3]. The direction comes from the later price break.",
                    "Meaning/action: do not label ID/NR bullish or bearish before the trigger; count the window and wait.",
                ),
                accent="Neutral first, directional only after the breakout.",
                caption="Lim (2016), p. 232. ID/NR has no bearish or bullish sentiment before its breakout.",
            ),
            picture=IDNR_DIRECTION_FIGURE,
            text_w=7.2,
            picture_extra=0.05,
            notes=IDNR_DIRECTION_FIGURE.notes,
            origin=IDNR_DIRECTION_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Inside Month/NR5",
                lines=(
                    "Inside month applies the idea to monthly bars. Ours: ranges 12, 10, 9, 7, 5 PHP; the fifth is inside the fourth and narrowest [1] [2]. Invented, not the book figure.",
                    "The sixth invented bar breaks upward through PHP 31.00 [3]. Before the break, the pattern is neutral.",
                    "Figure 7.39 is a separate Dynegy extension, not a source for these values.",
                ),
                accent="The timeframe changes; the inside plus narrowest-range logic stays.",
                caption="Lim (2016), p. 232. Monthly ranges and breakout are ours, invented to show the extension.",
            ),
            picture=INSIDE_MONTH_CHART,
            text_w=7.2,
            picture_extra=0.2,
            notes=INSIDE_MONTH_CHART.notes,
            origin=INSIDE_MONTH_CHART.origin,
        ),
        Pair(
            left=Content(
                title="Figure 7.39: Inside Month/NR5 breakout",
                lines=(
                    "The book's monthly chart shows the inside-month setup [1], the five-month range count [2], and the later upside breakout [3].",
                    "The observed breakout is the book's example, not a promise that every inside month breaks upward.",
                    "Meaning/action: keep the pattern neutral until the monthly bar actually breaks, then read direction from price.",
                ),
                accent="The monthly figure extends ID/NR without adding a new direction rule.",
                caption="Lim (2016), p. 232, Figure 7.39. The monthly chart is Dynegy Inc.",
            ),
            picture=INSIDE_MONTH_FIGURE,
            text_w=7.2,
            picture_extra=0.05,
            notes=INSIDE_MONTH_FIGURE.notes,
            origin=INSIDE_MONTH_FIGURE.origin,
        ),
        Check(
            label="From Williams' Oops and ID/NR",
            questions=(
                Q(
                    stem="After a gap up, the Williams' Oops sell-stop is placed at:",
                    options=("The previous bar's high", "The new bar's high", "The previous bar's low", "The midpoint of both bars"),
                    answer="A",
                    reason="Lim places the sell-stop at the previous bar's high after a gap above that high (p. 231).",
                ),
                Q(
                    stem="What does ID/NR6 count?",
                    options=("Six months", "Six bars and the narrowest range", "Six volume readings only", "Six bullish closes"),
                    answer="B",
                    reason="ID/NR6 uses an inside day and the narrowest bar over the last six days (p. 232).",
                ),
            ),
            picture=IDNR_FIGURE,
            text_w=5.9,
            layout="beside",
            notes=(
                "Let the room answer from the earlier order diagram and marked ID/NR6 slide.",
                "Do not reveal the answers here; the next slide gives the reasons.",
            ),
            origin="Questions are ours and answerable from the preceding Part 4 slides.",
        ),
    ),
)

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 7",
    title="Bar Chart Analysis",
    subtitle=("A price bar records opening, highest, lowest and closing prices; "
              "it can warn of a possible top or bottom. First, make one bar "
              "from the trades that made it."),
    presenter="Faculty of Economics University",
    objectives=(
        "Understand bar chart analysis as pure price action used to forecast potential tops and bottoms.",
        "Recognise potential early trend change through commonly used bar patterns.",
        "Identify potential buy and sell signals through single, double, triple, and multiple bullish and bearish formations.",
        "Read bar action with the 16 price and volume reversal characteristics, as context rather than certainty.",
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
            title="Summary: read the bar, then the context",
            lines=(
                "Bar action, indicator action, and volume action may indicate future price activity, especially when significant indicator and volume action accompanies the bar.",
                "Chapter 7 reads OHLC, formation count, sentiment, gaps, barriers, volume, and the 16 reversal characteristics.",
                "Breakout patterns may catch continuations or reversals, but readings remain potential. Oscillator method is deferred to Chapter 8.",
            ),
            accent="The summary is a reading habit, not a complete trade plan.",
            notes=(
                "Read the book's summary on p. 233 as the scope of the chapter.",
                "Emphasise that potential evidence is not a guarantee or a complete trading system.",
            ),
            origin="Lim (2016), p. 233. The chapter summary is paraphrased for teaching.",
        ),
        Content(
            title="Review answers 1 to 3",
            lines=(
                "1. Exhaustion versus pin bar: exhaustion opens beyond the prior extreme and has no following gap; a pin bar falsely penetrates a barrier and rapidly retraces.",
                "2. ID/NR7 is a volatility breakout because it combines an inside day with the narrowest range in the last seven days.",
                "3. A key reversal makes a higher high then closes near or below the prior close, or the bullish converse in a downtrend. A wider bar and high volume may strengthen the potential reading.",
            ),
            accent="The first three answers distinguish pattern structure from reliability context.",
            notes=(
                "Ask students to say the difference before reading the answer text.",
                "Keep the words may and potential: the book does not promise follow-through.",
            ),
            origin="Lim (2016), pp. 218 to 232. Review answers are written from the preceding slides.",
        ),
        Content(
            title="Review answer 4: the 16 characteristics (1 of 2)",
            lines=(
                "1 to 4: decrease in price cycle amplitude; decrease in price cycle period; change in bar retracement symmetry; decrease in average bar range.",
                "5 to 8: lack of the quality of price persistence; decrease in average bar stochastic ratio; decrease in average candlestick real body to range ratio; changes in angular symmetry and momentum.",
            ),
            accent="These first eight are potential reversal clues, not guarantees. Chapter 5 gives the detailed discussion.",
            notes=(
                "Point back to the earlier Chapter 5 terms for the first eight characteristics.",
                "Read every name as evidence, not certainty.",
            ),
            origin="Lim (2016), pp. 216 to 218; the 16 names follow the book's order.",
        ),
        Content(
            title="Review answer 4: the 16 characteristics (2 of 2)",
            lines=(
                "9 to 12: proximity to a price barrier; reduction in frequency and decrease in depth of trend-based oscillations; appearance of relatively larger and longer lasting consolidations; appearance of an exhaustion gap.",
                "13 to 16: completion of the average range for the period under observation; overextended price action with respect to a price barrier; price accompanied by extremely high or low volume; standard divergences between price, volume, and oscillators.",
            ),
            accent="Barrier proximity is the especially important context; these clues still do not guarantee reversal.",
            notes=(
                "Point back to the earlier Chapter 5 terms for the remaining definitions the book says to recall.",
                "Read barrier proximity as the strongest reliability emphasis in this chapter.",
            ),
            origin="Lim (2016), pp. 216 to 218; the 16 names follow the book's order.",
        ),
        Pair(
            left=Content(
                title="Review answers 5 and 6",
                lines=(
                    "5. Volume: high volume can strengthen a wide final reversal bar; low volume can signal uncertainty. Pattern 1 allows larger middle volume to be more bearish.",
                    "6. Figure 7.6: pattern 1 [1] has first and third closes near low with a large middle bar; pattern 2 [2] has a narrow, low-volume middle bar. Blue [3] marks shared uptrend.",
                    "Wider outer ranges and gaps add potential reliability. Chapter 7 supplies evidence, not a complete trade plan.",
                ),
                accent="Pattern evidence does not make a complete trade plan.",
                caption="",
            ),
            picture=TRIPLE_BEARISH_FIGURE,
            text_w=7.2,
            picture_extra=0.1,
            notes=TRIPLE_BEARISH_FIGURE.notes,
            origin=TRIPLE_BEARISH_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Review answer 7: ideal inside-bar reversal",
                lines=(
                    "Inside reversal: the inside bar stays within the prior high and low, then breaks in the reversal direction.",
                    "Ideal: wide/high-volume first bar; narrow/very-low-volume second bar. Barrier and trend context add weight.",
                    "Figure 7.25 marks wide [1], narrow inside [2], and oscillator region [3]. Chapter 7 gives no formula.",
                    "Harami is one-fourth to one-third the prior range; an inside bar has no restriction.",
                ),
                accent="The inside condition comes first; reversal direction comes from the later break.",
                caption="",
            ),
            picture=INSIDE_BAR_FIGURE,
            text_w=7.6,
            picture_extra=0.1,
            notes=INSIDE_BAR_FIGURE.notes,
            origin=INSIDE_BAR_FIGURE.origin,
        ),
        Pair(
            left=Content(
                title="Review answer 8: the Chapter 8 boundary",
                lines=(
                    "The book asks how oscillators can help gauge bullishness or bearishness in bar reversal patterns.",
                    "Figure 7.13 labels an oscillator region [1], but Chapter 7 does not teach the method or a formula for using oscillators.",
                    "The full treatment belongs to Chapter 8. This is a forward pointer, not an assessed Chapter 7 method.",
                ),
                accent="Use the figure as context only; do not import a method the chapter does not teach.",
                caption="Lim (2016), p. 233, review question 8; Figure 7.13, p. 218. Oscillator method is deferred to Chapter 8.",
            ),
            picture=OSCILLATOR_BOUNDARY_FIGURE,
            text_w=6.2,
            picture_extra=0.1,
            notes=OSCILLATOR_BOUNDARY_FIGURE.notes,
            origin=OSCILLATOR_BOUNDARY_FIGURE.origin,
        ),
    ),
    openers=(
        Content(
            title="What this chapter lets you do",
            lines=(
                "A price bar is a compact record of opening, highest, lowest, and closing prices. This chapter teaches how to read that four-price record.",
                "You will calculate a bar, classify a formation by its number of bars and its own bullish or bearish bias, and judge a possible continuation or reversal.",
                "You will also recall the book's 16 price and volume reversal characteristics. Every signal is a potential warning, not a promise.",
            ),
            accent="The route follows the book from one bar to the full pattern.",
            notes=(
                "Read the four objectives in plain words. The title slide has already introduced the four retained prices.",
                "Keep potential visible: the chapter teaches warnings and expectations, not certainty.",
            ),
            origin="Lim (2016), pp. 209 to 217. The plain-language objectives follow the book's four learning objectives.",
        ),
        Content(
            title="Four parts, one reading habit",
            lines=(
                "Part 1 makes and combines the four prices in a bar.",
                "Part 2 compares continuation and reversal using trend sentiment and intrinsic sentiment.",
                "Part 3 reads popular reversal patterns. Part 4 reads volatility breakouts.",
                "A check follows key ideas, and each part stops cleanly. The route follows the book from one bar to the full pattern.",
            ),
            accent="Part 1 starts with the four prices every bar keeps.",
            notes=(
                "Say four parts, not six. The checks are for reading the room, not for marks.",
                "Point to Part 1 as the first stop: one interval becomes one bar before patterns are named.",
            ),
            origin="Lim (2016), Chapter 7 sections 7.1 to 7.4. The four-part route follows the approved outline.",
        ),
    ),
    dividers=False,
)
