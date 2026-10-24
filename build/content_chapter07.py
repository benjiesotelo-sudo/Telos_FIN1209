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
    aspect=1120 / 450,
    crop=(),
    marks=(
        Mark(1, "circle", 0.74, 0.60, 0.80, 0.68,
             color="gold", at=(0.69, 0.72), size=0.30),
        Mark(2, "line", 0.78, 0.66, 0.91, 0.66,
             color="red", at=(0.70, 0.73), size=0.30),
        Mark(3, "line", 0.78, 0.61, 0.91, 0.61,
             color="blue", at=(0.94, 0.50), size=0.30),
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
    aspect=1180 / 680,
    crop=(0.015, 0.0, 0.015, 0.0),
    marks=(
        Mark(1, "box", 0.27, 0.06, 0.55, 0.98,
             color="gold", at=(0.15, 0.82), size=0.30),
        Mark(2, "box", 0.50, 0.56, 0.55, 0.95,
             color="red", at=(0.58, 0.90), size=0.30),
        Mark(3, "line", 0.53, 0.57, 0.53, 0.95,
             color="blue", at=(0.70, 0.90), size=0.30),
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
    aspect=1180 / 680,
    marks=(
        Mark(1, "line", 0.53, 0.57, 0.53, 0.95,
             color="gold", at=(0.59, 0.90), size=0.30),
        Mark(2, "box", 0.50, 0.56, 0.55, 0.95,
             color="red", at=(0.58, 0.40), size=0.30),
        Mark(3, "box", 0.58, 0.61, 0.65, 0.78,
             color="blue", at=(0.90, 0.86), size=0.30),
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
    aspect=1120 / 440,
    marks=(
        Mark(1, "circle", 0.47, 0.62, 0.53, 0.80,
             color="gold", at=(0.42, 0.84), size=0.30),
        Mark(2, "arrow", 0.22, 0.88, 0.54, 0.88,
             color="red", at=(0.18, 0.93), size=0.30),
        Mark(3, "circle", 0.53, 0.17, 0.59, 0.42,
             color="blue", at=(0.63, 0.12), size=0.30),
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
    aspect=1100 / 670,
    marks=(
        Mark(1, "box", 0.22, 0.02, 0.40, 0.68,
             color="gold", at=(0.17, 0.34), size=0.30),
        Mark(2, "box", 0.45, 0.02, 0.63, 0.68,
             color="red", at=(0.40, 0.34), size=0.30),
        Mark(3, "circle", 0.24, 0.48, 0.32, 0.60,
             color="blue", at=(0.16, 0.58), size=0.30),
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
    aspect=1090 / 620,
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
    aspect=1060 / 450,
    marks=(
        Mark(1, "box", 0.76, 0.74, 0.93, 0.98,
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
