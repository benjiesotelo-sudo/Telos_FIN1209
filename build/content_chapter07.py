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
    title="Four invented sentiment cases",
    shows=("Four invented numeric cases. Trend sentiment is the direction of "
           "the existing trend; intrinsic sentiment is the formation's own "
           "bullish or bearish bias."),
)

SECTION1 = Section(
    number=1,
    title="The Price Bar",
    short="7.1 Price bar",
    minutes="",
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
                "Finally ask whether intrinsic sentiment agrees with trend sentiment. Agreement is continuation; disagreement is reversal (Lim, p. 211).",
                "Ours, invented: bearish intrinsic sentiment in an uptrend disagrees, so it is a potential reversal; bullish intrinsic sentiment agrees, so it is a potential continuation.",
                "Meaning/action: these are directional expectations, not certainties. Part 2 makes the agreement rule explicit.",
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
            picture=WORKED_CROP,
            text_w=5.55,
            notes=(
                "This worked read combines the three classification questions without introducing a new pattern name.",
                "Say potential reversal, not reversal certainty. The next slide checks the construction arithmetic.",
            ),
            origin="Lim (2016), pp. 210 to 211, Figure 7.3. The PHP values and classification are ours, invented to show the sequence.",
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
                "Four invented trend/form cells: +4.0%/+2.0% and -4.0%/-2.0% continue; +4.0%/-2.0% and -4.0%/+2.0% are potential reversals.",
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
                    "Now apply four invented cases: +4.0% trend/+2.0% formation and -4.0%/-2.0% agree, so both continue.",
                    "+4.0%/-2.0% disagrees, so potential reversal; -4.0%/+2.0% also disagrees, so potential reversal.",
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
