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
        Mark(1, "circle", 0.625, 0.345, 0.705, 0.425,
             color="gold", at=(0.59, 0.31), size=0.30),
        Mark(2, "circle", 0.735, 0.125, 0.815, 0.205,
             color="red", at=(0.86, 0.10), size=0.30),
        Mark(3, "circle", 0.735, 0.685, 0.815, 0.765,
             color="blue", at=(0.86, 0.83), size=0.30),
    ),
    shows=("Figure 7.1: five minutes of changing price are filtered into one "
           "bar that keeps only the open, high, low and close. The range is "
           "the distance from high to low."),
    notes=(
        "Read the left-hand price activity, then the single bar on the right. "
        "The gold mark is the open, the red mark the high, and the blue mark the low.",
        "The close is the fourth retained price, and the bracket on the right "
        "shows the high to low range. The figure labels these as filtered price action.",
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
        Mark(2, "circle", 0.50, 0.05, 0.60, 0.18,
             color="red", at=(0.63, 0.04), size=0.30),
        Mark(3, "circle", 0.81, 0.37, 0.91, 0.49,
             color="blue", at=(0.94, 0.50), size=0.30),
    ),
    shows=("Figure 7.1 construction panel, cropped to the five-minute price "
           "path. The first trade, highest trade and last trade become the "
           "bar's open, high and close; the lowest trade supplies the low."),
    notes=(
        "The crop enlarges the construction panel so the sequence can be read. "
        "Gold 1 is the first trade, red 2 the highest trade, and blue 3 the last trade.",
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
                    "A price bar filters one interval into four prices: open (O), high (H), low (L), and close (C).",
                    "Ours: O 50.00, H 52.40, L 49.60, C 51.10 [1]. Range = |H - L| = |52.40 - 49.60| = PHP 2.80.",
                    "[2] and [3] show the high and low that bound the range. These four values preserve the interval's price action.",
                ),
                accent="Next, trace the five trades that became these four prices.",
            ),
            picture=Chart(
                letter="P",
                title="Chart P: the four prices",
                shows=("One invented OHLC bar with O 50.00, H 52.40, L 49.60 "
                       "and C 51.10, plus its PHP 2.80 high to low range."),
                marks=(
                    Mark(1, "circle", 0.49, 0.63, 0.56, 0.72,
                         color="gold", at=(0.38, 0.60)),
                    Mark(2, "circle", 0.49, 0.08, 0.56, 0.18,
                         color="red", at=(0.67, 0.08)),
                    Mark(3, "circle", 0.49, 0.78, 0.56, 0.87,
                         color="blue", at=(0.67, 0.92)),
                ),
            ),
            text_w=5.2,
            notes=(
                "Start with the bar's four retained prices. O, H, L and C are the book's acronym OHLC.",
                "Point to the arithmetic on Chart P: the range is an absolute high to low distance, PHP 2.80.",
            ),
            origin=("Lim (2016), pp. 209 to 210. Chart P is ours, with invented "
                    "PHP values and marks."),
        ),
        Pair(
            left=Content(
                title="Figure 7.1: the same four prices on the book's diagram",
                lines=(
                    "The book calls OHLC a summary of price activity over a specified time interval [1].",
                    "Gold [1] marks O, the first retained price. Red [2] marks H and blue [3] marks L, the two ends of the PHP 2.80 range.",
                    "The close C is the fourth retained price. Meaning: a bar is a compact record, not every trade inside the interval.",
                ),
                accent="Now make the compact record from the trades that produced it.",
            ),
            picture=PRICE_BAR_FULL,
            text_w=5.15,
            notes=PRICE_BAR_FULL.notes,
            origin=PRICE_BAR_FULL.origin,
        ),
        Pair(
            left=Content(
                title="Five trades become one bar",
                lines=(
                    "Ours: five trades are 50.00, 50.80, 49.60, 52.40, and 51.10 PHP.",
                    "The first trade becomes O 50.00 [1]. The highest and lowest trades become H 52.40 and L 49.60 [2].",
                    "The last trade becomes C 51.10 [3]. The result is one bar with range PHP 2.80, not five separate closes.",
                ),
                accent="The interval is summarized by first, extreme, and last prices.",
            ),
            picture=Chart(
                letter="Q",
                title="Chart Q: five trades",
                shows=("Five invented one-minute observations, with the first, "
                       "highest and last observations numbered."),
                marks=(
                    Mark(1, "circle", 0.27, 0.62, 0.33, 0.72,
                         color="gold", at=(0.20, 0.78)),
                    Mark(2, "circle", 0.55, 0.12, 0.61, 0.24,
                         color="red", at=(0.66, 0.10)),
                    Mark(3, "circle", 0.74, 0.32, 0.80, 0.44,
                         color="blue", at=(0.84, 0.52)),
                ),
            ),
            text_w=5.15,
            notes=(
                "Read the invented observations left to right. The labels give every number used in the prose.",
                "The lowest observation is also retained as L, while the three numbered observations make the construction order visible.",
            ),
            origin=("Lim (2016), p. 210, Figure 7.1. Chart Q is ours, with "
                    "invented PHP observations and marks."),
        ),
        Pair(
            left=Content(
                title="Figure 7.1: read the construction panel",
                lines=(
                    "The book's construction panel shows the same rule: the first price is O [1], the highest is H [2], and the last is C [3].",
                    "Its lowest point is L. The right-hand bar filters the changing path into OHLC and draws the range from H to L.",
                    "What to do: read the four retained prices before interpreting any bar pattern.",
                ),
                accent="Several intervals can be filtered into one higher-timeframe bar.",
            ),
            picture=PRICE_BAR_CONSTRUCTION,
            text_w=5.15,
            notes=PRICE_BAR_CONSTRUCTION.notes,
            origin=PRICE_BAR_CONSTRUCTION.origin,
        ),
        Pair(
            left=Content(
                title="Three small bars become one larger bar",
                lines=(
                    "Ours: three five-minute bars are combined. Their first open is 50.00; their highest high is 50.90; their lowest low is 49.40; their last close is 50.30.",
                    "Chart R marks [1] first O, [2] highest H, [3] lowest L, and [4] last C. The composite is O 50.00, H 50.90, L 49.40, C 50.30.",
                    "The intermediate opens and closes are not carried into the higher-timeframe OHLC record.",
                ),
                accent="The same four-price rule works when the interval becomes longer.",
            ),
            picture=Chart(
                letter="R",
                title="Chart R: three bars and their surviving values",
                shows=("Three invented lower-timeframe bars with the first open, "
                       "highest high, lowest low and last close labelled."),
                marks=(
                    Mark(1, "circle", 0.30, 0.56, 0.38, 0.66,
                         color="gold", at=(0.24, 0.60)),
                    Mark(2, "circle", 0.49, 0.08, 0.56, 0.18,
                         color="red", at=(0.63, 0.06)),
                    Mark(3, "arrow", 0.64, 0.62, 0.53, 0.76,
                         color="blue", at=(0.66, 0.58)),
                    Mark(4, "circle", 0.69, 0.34, 0.75, 0.44,
                         color="purple", at=(0.82, 0.32)),
                ),
            ),
            text_w=5.0,
            notes=(
                "Walk the three bars left to right, then read the four labelled survivors.",
                "The composite does not average the prices. It keeps first, extreme and last values exactly as the book states.",
            ),
            origin=("Lim (2016), p. 210, Figure 7.2. Chart R is ours, with "
                    "invented PHP bars and marks."),
        ),
        Pair(
            left=Content(
                title="Figure 7.2: the higher-timeframe rule",
                lines=(
                    "Figure 7.2 combines three five-minute bars into one 15-minute bar [1].",
                    "Gold [1] is the first open, red [2] the highest high, blue [3] the lowest low, and purple [4] the last close.",
                    "Meaning/action: when changing timeframe, preserve first O, highest H, lowest L and last C. Do not average them.",
                ),
                accent="The next question is how many bars make a formation.",
            ),
            picture=HIGHER_TIMEFRAME_FIGURE,
            text_w=5.15,
            notes=HIGHER_TIMEFRAME_FIGURE.notes,
            origin=HIGHER_TIMEFRAME_FIGURE.origin,
        ),
        Content(
            title="First classification question: how many bars?",
            lines=(
                "A formation may use one bar, two bars, three bars, or several bars. Count the bars before naming the formation.",
                "Ours: one bar is single; two are double; three are triple; five are multiple. The count describes structure, not direction.",
                "A three-bar formation is therefore triple even if its bars are bullish or bearish. The number alone is not a buy or sell signal.",
            ),
            accent="Count first. Then ask what bias the formation carries.",
            notes=(
                "This is the first classification question in Lim's list on p. 210.",
                "Use the invented counts to separate structure from direction. A count does not predict price by itself.",
            ),
            origin="Lim (2016), p. 210. The counts and examples are ours, invented to show the classification.",
        ),
        Content(
            title="Second classification question: intrinsic sentiment",
            lines=(
                "Intrinsic sentiment is the pattern's own bullish or bearish bias. It belongs to the formation, not to the trend around it.",
                "Ours: an intrinsically bullish pattern stays bullish when placed in an uptrend or a downtrend. Its location does not rename its bias.",
                "Lim points back to Chapter 4 for intrinsic sentiment. Use that earlier meaning before asking what the trend expects next.",
            ),
            accent="The pattern's own bias comes before the market-context question.",
            notes=(
                "Keep intrinsic sentiment separate from trend sentiment. Chapter 4 is the named pointer for the earlier term.",
                "The invented example is only a classification test, not a claim that every bullish pattern works in every trend.",
            ),
            origin="Lim (2016), p. 211, with a pointer to Chapter 4. The placement example is ours.",
        ),
        Content(
            title="Third classification question: continuation or reversal?",
            lines=(
                "Continuation means the pattern's intrinsic sentiment agrees with the existing trend. Reversal means the two sentiments disagree.",
                "Ours: a bearish pattern in an uptrend disagrees, so it is a potential reversal. A bullish pattern in an uptrend agrees, so it is a potential continuation.",
                "These are directional expectations, not certainties. The next part applies the agreement rule to generic patterns.",
            ),
            accent="Agreement suggests continuation; disagreement suggests reversal.",
            notes=(
                "Lim states the agreement rule on p. 211. Keep the word potential because a classification is not a guarantee.",
                "The full four-cell table and the book's head and shoulders examples begin in Part 2.",
            ),
            origin="Lim (2016), p. 211. The two invented placements illustrate the book's agreement rule.",
        ),
        Content(
            title="Part 1 in one worked read",
            lines=(
                "Ours: two bars make a double formation. The second closes at 49.80, below the first bar's low of 50.20, so its intrinsic bias is bearish.",
                "The surrounding trend is up, so trend sentiment is bullish. Bearish intrinsic sentiment disagrees with bullish trend sentiment.",
                "Read: a double-bar potential reversal. The classification tells us what to examine next; it does not promise a fall.",
            ),
            accent="The four-price record comes first, then count, bias, and expectation.",
            notes=(
                "This worked read combines the three classification questions without introducing a new pattern name.",
                "Say potential reversal, not reversal certainty. The next slide checks the construction arithmetic.",
            ),
            origin="Lim (2016), pp. 210 to 211. The PHP values and classification are ours, invented to show the sequence.",
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
            notes=(
                "Let students calculate before revealing. Both answers are stated in the preceding worked slides.",
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
            notes=(
                "Ask the room to separate count, intrinsic bias, and expected direction.",
                "The question tests the definitions, not a figure. Part 2 adds the four-cell table.",
            ),
            origin="Questions are ours and answerable from the preceding Part 1 slides.",
        ),
    ),
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
    dividers=True,
)
