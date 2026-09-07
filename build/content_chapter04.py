"""Chapter 4 content for FIN1209 - Market Phase Analysis.

This file is pure data. It carries no drawing code.

Source of the chapter scope is Lim, M. (2016), The Handbook of Technical
Analysis, chapter 4, printed pages 99 to 124, which students have in the
course text. Everything here is written from scratch in teaching language.

This chapter is a trial of a much leaner deck, and it is shaped differently
from Chapters 1 to 3 on purpose:

  * The parts are the book's own sections, 4.1 to 4.9, not the six part
    template of the earlier chapters. Section 4.10 is the book's summary and
    feeds the closing slides.

  * There is no divider slide and no recap slide. The first slide of every
    part carries the book's section number in its title, the progress marker
    says where the room is, and the last check of a part is its recap.

  * A check reveals its answers on the question slide (InlineCheck), so a
    check is one slide and not two.

  * A picture sits beside the idea it shows (Pair) instead of on a slide of
    its own. Nineteen of the book's thirty two figures are placed, one for
    each point: where several figures make the same point, one is used.

  * Three sections are taught in full because they are this chapter's own
    material: 4.1 (the phases themselves), 4.2 (chart patterns, intrinsic
    and extrinsic bias) and 4.7 (Sakata). Six are kept light because each
    previews a tool that has a chapter of its own later in the book: 4.3
    volume and open interest, 4.4 moving averages, 4.5 divergence and
    momentum, 4.6 sentiment, 4.8 Elliott and 4.9 cycles. A light section
    teaches what the section says about market phase and not the tool.

Where the standing rule bites, and how each place is handled. Every one is
named on a slide, and no check rests on any of them.

  * Consolidation. Review question 1 asks for a definition and the book
    never sets one apart. The term slide joins its sentence in 4.1 (two
    basic phases) with its sentence in 4.2 (how a market consolidates), and
    the speaker cue says that is what was done.

  * Broadening formations. The book's list of patterns that are bullish with
    respect to an uptrend includes them, and its next paragraph and its own
    Figure 4.5 treat them as reversal formations that disagree with the
    trend. The slide says so and teaches the paragraph.

  * The abc correction. The book gives it to accumulation "in most cases"
    and to distribution "usually", in consecutive sentences. The slide says
    both and no question is set on it.

  * Things the chapter names and never teaches: the shapes of the chart
    patterns, open interest, whipsaws, divergence, MACD and RSI, the
    thirteen sentiment indicators, Elliott's rules, how a cycle is found,
    price based volume, and the inertial characteristics its own learning
    objectives promise. Each is named where it appears and the closing
    slides collect them.

No chart of our own is drawn for this chapter. See charts_chapter04.py.
"""

from deckkit import (
    Chapter,
    Content,
    Figure,
    InlineCheck,
    Pair,
    Question,
    Section,
    Term,
)

Q = Question

# ==========================================================================
# 4.1 - Dow theory of market phase. Taught in full.
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Dow Theory of Market Phase",
    short="4.1 Dow",
    minutes="",
    covers=(),
    slides=(
        Content(
            title="4.1  Markets move in phases",
            lines=(
                "Chapter 2 gave a primary trend three phases: accumulation, trending and distribution.",
                "That description is now regarded as the basic underlying characteristic of market action.",
                "Phase analysis applies across all time frames, from the long term to the very short term.",
            ),
            accent="Not recognizing the phases and their transitions greatly disadvantages the practitioner.",
            notes=(
                "Link back: these are the three phases of Dow Theory from Chapter 2. Today they get the whole chapter.",
                "Say the one question now: which phase is this market in? Every section answers it a different way.",
            ),
        ),
        Pair(
            left=Term(
                term="Consolidation phase",
                plain="The sideways stretch. Price ranges, or makes small corrective moves, instead of trending.",
                example="A share that swings between PHP 40 and PHP 44 for four months, going nowhere, is consolidating.",
                formal="One of only two basic phases, the other being the trending phase. A market consolidates, when expressing indecision, rest or exhaustion, by ranging or by making relatively small corrective moves. It subdivides into accumulation and distribution.",
            ),
            picture=Figure(
                number="4.1",
                shows="A tree: market phase splits into consolidation and trend, and consolidation splits again into accumulation and distribution.",
            ),
            text_w=6.6,
            notes=(
                "Review question 1 asks for this definition. The book never sets one apart: this joins its sentence in 4.1 with its sentence in 4.2.",
                "Read the figure top down: two phases, and consolidation splits in two. Three phases, but only two kinds.",
            ),
        ),
        Pair(
            left=Content(
                title="Accumulation or distribution? Known only afterwards",
                lines=(
                    "If the market rises after consolidating, the consolidation was accumulation: buying activity.",
                    "If it declines after consolidating, it was distribution: selling activity.",
                    "Which one it is can only be ascertained after the fact.",
                ),
                accent="One objective of technical analysis is to look for evidence of which is taking place.",
            ),
            picture=Figure(
                number="4.2",
                shows="The daily Dow Jones Industrial Average with its accumulation, trending and distribution phases boxed and named, and a volume panel below with the decline through each consolidation drawn in.",
            ),
            notes=(
                "Point at each grey box and say what came after it. The label was only possible once the next move was known.",
                "The box at the top right is labelled only consolidation: nobody knew yet. That is the point of the slide.",
            ),
        ),
        Pair(
            left=Content(
                title="The same phases at every time scale",
                lines=(
                    "A primary trend typically spans months to years in the equity markets.",
                    "In commodity futures it tends to be shorter: high leverage induces greater volatility.",
                    "On a daily chart a consolidation normally lasts about three to six months, sometimes longer.",
                ),
                accent="The same phases show on sub-hourly charts. The book calls that micro phase action.",
            ),
            picture=Figure(
                number="4.3",
                shows="A 15 minute EURUSD chart with distribution, trend and accumulation phases boxed one after another, titled micro phase action.",
            ),
            text_w=5.6,
            notes=(
                "The figure is a 15 minute chart and it has every phase the daily Dow chart had.",
                "Macro phase behaviour shapes the micro phases inside it. That is why the chapter recommends multiple time frames.",
            ),
        ),
        Content(
            title="Accumulation: the informed buy from the frightened",
            lines=(
                "It normally follows a deep and rapid decline, with very negative data and bearish headlines.",
                "The uninformed are extremely bearish and sell at whatever price is available.",
                "The informed buy against the crowd: a contrarian approach that needs deep pockets.",
                "They gather shares very gradually, careful not to drive prices up too fast.",
            ),
            accent="The sell-off that ends the preceding downtrend is called a selling climax.",
            notes=(
                "Chapter 2 named the two sides. What is new is how the informed buy: slowly, so the price stays low.",
                "In a selling climax the uninformed are the sellers and the informed are the buyers.",
            ),
        ),
        Content(
            title="Distribution: the same story upside down",
            lines=(
                "It normally follows a strong and rapid rise, with very positive data and bullish headlines.",
                "The uninformed buy at whatever price is available: a state of irrational exuberance.",
                "Margin debt is skyrocketing.",
                "The informed sell very gradually, careful not to drive prices down too rapidly.",
            ),
            accent="The surge that ends the preceding uptrend is called a blow-off, or buying climax.",
            notes=(
                "Irrational exuberance came up in Chapter 2. Margin debt is new here and comes back in the sentiment section.",
                "Mirror the last slide line by line. Students should be able to write one from the other.",
            ),
        ),
        Content(
            title="The trend phase feeds on itself",
            lines=(
                "Technical traders get in early, on a clear upside breakout from consolidation.",
                "Market savvy investors follow, then the public as the uptrend becomes obvious.",
                "Regret bias: those who missed out, or sold too early, buy at every dip.",
                "At even higher prices the herd uses more margin, even borrowing to invest.",
            ),
            accent="The book calls it a vicious positive feedback cycle. A downtrend runs the same way, downward.",
            notes=(
                "A downtrend begins with a breakdown from the distribution range. Liquidation and margin limits then force more selling.",
                "Regret bias is the term to underline: the fear of having missed out keeps the buying going.",
            ),
        ),
        Content(
            title="Why tops are shorter and rougher than bottoms",
            lines=(
                "Accumulation normally lasts longer than distribution.",
                "The uptrend tends to be more prolonged than the downtrend.",
                "Distributions tend to be much more volatile than accumulations.",
            ),
            accent="One reason covers all three: at higher prices more capital, and more unrealized profit, is at risk.",
            notes=(
                "Ask why before showing the gold line. The book gives the same reason three times.",
                "At the bottom there is less to lose, so nobody is in a hurry. At the top everyone has profit to protect.",
            ),
        ),
        Content(
            title="What a consolidation looks like on the chart",
            lines=(
                "Accumulation: after a relatively rapid decline, near a significant prior bottom, with no lower troughs forming.",
                "Distribution: after a prolonged uptrend, near a significant prior top, with no higher peaks forming.",
                "In both, volume subsides as a potential breakout approaches.",
            ),
            accent="The longer it lasts, the more powerful the breakout, typically with a surge in volume.",
            notes=(
                "This is review question 4: how would you determine if accumulation is taking place? These are the signs.",
                "The book says the breakout can be to either side of the range. The signs are evidence, not proof.",
            ),
        ),
        InlineCheck(
            label="The phases",
            questions=(
                Q(
                    stem="A market consolidates for four months and then rises. The consolidation represented:",
                    options=("Distribution",
                             "Accumulation",
                             "A trending phase",
                             "A selling climax"),
                    answer="B",
                    reason="If the market rises after consolidating, the consolidation was accumulation: buying activity.",
                ),
                Q(
                    stem="Accumulation normally lasts longer than distribution because, at the bottom of the market:",
                    options=("Less capital is at risk at the lower prices",
                             "Volume is always higher",
                             "The uninformed are buying heavily",
                             "Leverage is higher than at the top"),
                    answer="A",
                    reason="Lower prices mean a lower amount of capital at risk, so the bottom takes its time.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="When is a consolidation over?",
                lines=(
                    "There is no absolute consensus on the exact point where a consolidation ends.",
                    "Some look for a 3 to 5 percent rise above the highest peak of the range.",
                    "Some wait for the minimum measuring objective to be met.",
                    "Most look for a clear and simple technical breakout from the range.",
                ),
                accent="Even then, where the breakout occurs depends on the price filter used.",
            ),
            picture=Figure(
                number="4.4",
                shows="A consolidation range with the three popular completion levels marked above it: a technical breakout, a 3 to 5 percent rise above the highest peak, and a one to one minimum target projection of the range.",
            ),
            text_w=5.4,
            notes=(
                "Subjectivity again, as in Chapter 1: three analysts, three completion points, one chart.",
                "Once a consolidation is complete, a trend may already be in effect. The book says that follows logically.",
            ),
        ),
        Term(
            term="Minimum measuring objective",
            plain="The least a breakout is expected to travel: usually the height of the range it broke out of.",
            example="A share ranges between PHP 40 and PHP 44, a height of PHP 4. On an upside breakout the minimum target is 44 + 4 = PHP 48.",
            formal="The expected minimum price target, which is usually a price excursion equal to the range or height of the consolidation.",
            notes=(
                "Do the arithmetic on the board: the top of the range plus the height of the range.",
                "Figure 4.4 called this the one to one minimum target projection. It is the same thing.",
            ),
        ),
        InlineCheck(
            label="When a consolidation ends",
            questions=(
                Q(
                    stem="A share ranges between PHP 50 and PHP 56, then breaks out upward. Its minimum measuring objective is:",
                    options=("PHP 56",
                             "PHP 59",
                             "PHP 62",
                             "PHP 68"),
                    answer="C",
                    reason="The range is PHP 6 high, and 56 + 6 = PHP 62.",
                ),
                Q(
                    stem="Most traders and analysts take as evidence that a consolidation has completed:",
                    options=("A 3 to 5 percent rise above the highest peak",
                             "The minimum measuring objective being met",
                             "Very high volume inside the range",
                             "A clear and simple technical breakout from the range"),
                    answer="D",
                    reason="Some practitioners use the percentage rise or the measuring objective, but the simple technical breakout is the most popular.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.2 - Chart pattern interpretation of market phase. Taught in full.
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Chart Pattern Interpretation of Market Phase",
    short="4.2 Chart patterns",
    minutes="",
    covers=(),
    slides=(
        Content(
            title="4.2  Patterns come in two groups",
            lines=(
                "Most chart patterns belong to one of two groups: reversal or continuation.",
                "Accumulation and distribution tend to be populated by reversal patterns.",
                "Continuation patterns belong to the trend phase.",
            ),
            accent="So the kind of pattern on the chart is evidence of the phase the market is in.",
            caption="This chapter names the patterns and does not teach their shapes. Chapter 13 does.",
            notes=(
                "Do not teach the shapes today. Students need the names and which way each one leans.",
                "Say why it matters: a pattern is one more piece of evidence for accumulation or distribution.",
            ),
        ),
        Term(
            term="Consolidation pattern",
            plain="A pattern that stays boxed inside a range and is not trending anywhere.",
            example="A share drifts between PHP 40 and PHP 44 for six weeks while a triangle forms: a confined range and no trend.",
            formal="A chart pattern is usually regarded as a consolidation pattern if it unfolds within a relatively confined and well defined price range, and lacks any significant trend component.",
            notes=(
                "Two tests, both needed: a confined range, and no significant trend component.",
                "Hold the two tests. The next slide uses them to throw one kind of pattern out.",
            ),
        ),
        Pair(
            left=Content(
                title="Most patterns consolidate. V reversals do not.",
                lines=(
                    "A market showing indecision, rest or exhaustion ranges or makes small corrective moves.",
                    "So most reversal and continuation patterns are also consolidation patterns.",
                    "V tops and V bottoms are the exception: no confined range, and a strong trend component.",
                ),
                accent="V reversals are the hardest to forecast. They are normally identified only in hindsight.",
            ),
            picture=Figure(
                number="4.8",
                shows="A 4 hour USDCAD chart: a head and shoulders distribution, a decline into a sharp V bottom labelled a rapid accumulation phase, and a new consolidation after the rise.",
            ),
            text_w=5.4,
            notes=(
                "This is review question 3: why are most chart patterns consolidation patterns? The first two lines are the answer.",
                "The book adds that V reversals occur more often during distributions than accumulations.",
            ),
        ),
        Pair(
            left=Term(
                term="Intrinsic bias",
                plain="The bullish or bearish lean a pattern carries in itself, wherever it appears.",
                example="An ascending triangle is intrinsically bullish. Wherever it occurs, it is a bullish indication.",
                formal="The inherent bullish or bearish sentiment associated with a chart pattern that is independent of location, where sentiment is strictly based on the nature of the pattern.",
            ),
            picture=Figure(
                number="4.6",
                shows="A EURUSD chart with an inverted head and shoulders boxed at the bottom of a decline, labelled an intrinsically bullish pattern, and the trend phase rising out of it.",
            ),
            text_w=5.9,
            notes=(
                "The figure's pattern is an inverted head and shoulders. The label says intrinsically bullish and nothing about location.",
                "The book points out this chart cannot tell us the extrinsic bias: it shows no price history. Hold that word.",
            ),
        ),
        Content(
            title="Which way each pattern leans",
            lines=(
                "Bullish: bullish pennants and flags, ascending triangles, inverted head and shoulders, rounding bottoms, cup and handles, falling wedges, and double, triple and multiple bottoms.",
                "Bearish: bearish pennants and flags, descending triangles, standard head and shoulders, rounding tops, rising wedges, and double, triple and multiple tops.",
                "Neutral: symmetrical triangles and horizontal channels.",
            ),
            accent="The book lists eight intrinsically bullish patterns and seven bearish. Review question 2 asks for the eight.",
            notes=(
                "They do not need the shapes yet. They need to be able to list the eight.",
                "Pairs help: pennants and flags come in both kinds, triangles ascend or descend, wedges fall or rise, bottoms mirror tops.",
            ),
        ),
        InlineCheck(
            label="Consolidation patterns and intrinsic bias",
            questions=(
                Q(
                    stem="Which of these is NOT normally regarded as a consolidation pattern?",
                    options=("A symmetrical triangle",
                             "A horizontal channel",
                             "A V bottom",
                             "An ascending triangle"),
                    answer="C",
                    reason="A V bottom does not unfold within a confined range, and it has a significant trend component.",
                ),
                Q(
                    stem="Intrinsic bias is the sentiment of a chart pattern that is:",
                    options=("Independent of location and based strictly on the nature of the pattern",
                             "Set by the direction of the preceding trend",
                             "Taken from where the pattern sits on the chart",
                             "Read from the volume inside the pattern"),
                    answer="A",
                    reason="Intrinsic bias is inherent: it comes from the nature of the pattern and not from where it forms.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="Extrinsic bias",
                plain="The lean a pattern takes from where it sits, not from its shape.",
                example="An ascending triangle at a historically significant market top is extrinsically bearish: it sits at resistance.",
                formal="Location-based sentiment: sentiment that is dependent on factors that are external, or extrinsic, to the pattern.",
            ),
            picture=Figure(
                number="4.12",
                shows="The daily gold chart with a symmetrical triangle forming on a well tested accumulation zone beside a downtrend line, labelled extrinsically bullish, inside a larger consolidation.",
            ),
            notes=(
                "The triangle in the figure is intrinsically neutral. Its bullish bias comes entirely from where it formed: on a zone tested by multiple bottoms.",
                "The same ascending triangle at a significant bottom is bullish both ways. The location changes, the shape does not.",
            ),
        ),
        Content(
            title="What sets the extrinsic bias",
            lines=(
                "The direction of the preceding trend.",
                "Location with respect to historical extremes in price.",
                "Location with respect to the phase of an underlying market cycle.",
                "Location with respect to other supportive and resistive overlay barriers.",
                "Bullish or bearish divergent formations.",
            ),
            accent="For an intrinsically neutral pattern, these alone decide whether it is a reversal or a continuation.",
            notes=(
                "Five factors, all outside the pattern. The book gives this list for the neutral patterns.",
                "Divergence and cycles each get a section later today, and a chapter later in the course.",
            ),
        ),
        Pair(
            left=Content(
                title="When the biases agree",
                lines=(
                    "Intrinsic and extrinsic bias in agreement: a reversal at a top or bottom is more reliable.",
                    "Intrinsic bias in agreement with the trend: a continuation is more likely.",
                    "Any disagreement is a sign the reversal or continuation may be inherently weak.",
                ),
                accent="As a general guide, reversal patterns disagree with the trend and continuation patterns agree with it.",
            ),
            picture=Figure(
                number="4.5",
                shows="A summary diagram sorting the chart patterns into accumulation based, distribution based and continuation based, with reversal patterns marked as disagreeing with trend sentiment and continuation patterns as agreeing with it.",
            ),
            text_w=5.8,
            notes=(
                "Trend sentiment is the book's name for the directionality of the trend. The figure uses that phrase.",
                "Read the figure's two footers: reversal patterns, in disagreement; continuation patterns, in agreement.",
            ),
        ),
        Content(
            title="Neutral patterns borrow their bias",
            lines=(
                "Symmetrical triangles and horizontal channels take their bias from the trend.",
                "In an uptrend they are extrinsically bullish; in a downtrend, extrinsically bearish.",
                "Broadening, diamond and island formations are also intrinsically neutral, but are regarded as reversal formations, so their bias disagrees with the trend.",
            ),
            accent="A neutral pattern has no lean of its own. Its surroundings supply one.",
            caption="The book's list of patterns that are bullish in an uptrend includes broadening formations. Its next paragraph and Figure 4.5 treat them as reversals, which is what is taught here.",
            notes=(
                "The book contradicts itself on broadening formations: one list against one paragraph and one figure. Say so and move on.",
                "Nothing on broadening, diamond or island formations is examined from this chapter.",
            ),
        ),
        Pair(
            left=Content(
                title="Probabilities, never certainties",
                lines=(
                    "Two ascending triangles form the accumulation, and price breaks out on a large upside gap.",
                    "After the trend a third ascending triangle forms, then breaks down instead.",
                    "Trend sentiment and intrinsic bias agreed perfectly, and the pattern still failed.",
                ),
                accent="Technical forecasting is based on probabilities, and never on certainties.",
            ),
            picture=Figure(
                number="4.11",
                shows="The daily iShares Silver Trust chart: two ascending triangles as accumulation, a gap up into the trend phase, then a new ascending triangle that breaks down unexpectedly, with volume declining into each breakout.",
            ),
            text_w=5.4,
            notes=(
                "The book adds that failed patterns often lead to a more powerful reaction, so a failure is information too.",
                "Point at the volume panel: it declines as each breakout approaches. Section 4.3 picks that up.",
            ),
        ),
        InlineCheck(
            label="Extrinsic bias, and agreement",
            questions=(
                Q(
                    stem="An ascending triangle forms at the price level of a historically significant market top. It is:",
                    options=("Intrinsically bearish and extrinsically bearish",
                             "Intrinsically bullish and extrinsically bullish",
                             "Intrinsically neutral and extrinsically bearish",
                             "Intrinsically bullish and extrinsically bearish"),
                    answer="D",
                    reason="The shape is bullish wherever it forms. The location, at significant resistance, is bearish.",
                ),
                Q(
                    stem="A symmetrical triangle forms in the middle of an uptrend. Its extrinsic bias is:",
                    options=("Bearish, because triangles are reversal patterns",
                             "Bullish, taken from the uptrend",
                             "Neutral, because the pattern is neutral",
                             "Unknown until volume confirms it"),
                    answer="B",
                    reason="A neutral pattern is extrinsically bullish in an uptrend and extrinsically bearish in a downtrend.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.3 - Volume and open interest. Kept light: Chapter 6 teaches the tools.
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Volume and Open Interest Interpretation of Market Phase",
    short="4.3 Volume",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.3  Volume falls before the phase changes",
                lines=(
                    "Each phase has its typical volume action: down through a consolidation, up through a trend.",
                    "Volume tends to decline to relatively low levels just before a phase transition.",
                    "So volume can be used as a timing indicator for potential phase transitions.",
                ),
                accent="Very low volume says a consolidation may be ending. It does not say which way.",
            ),
            picture=Figure(
                number="4.15",
                shows="A schematic cycle of accumulation, trend, distribution, trend and accumulation, with volume marked down through each consolidation and up through each trend.",
            ),
            text_w=5.4,
            notes=(
                "This is the chapter objective on regime changes: the book's summary calls a phase transition a market regime change.",
                "Volume and open interest get Chapter 6. Today is only what they say about phase.",
            ),
        ),
        Pair(
            left=Content(
                title="Two more things volume says",
                lines=(
                    "A fall-off in volume during a trend is a sign of trend exhaustion.",
                    "It signals a potentially earlier onset of distribution or accumulation.",
                    "Higher than normal volume at the start of a consolidation strongly indicates a top or bottom has formed.",
                ),
                accent="Price levels with historically high volume are potential levels of accumulation or distribution.",
            ),
            picture=Figure(
                number="4.16",
                shows="The same schematic cycle with volume turning down partway through each trend, the turn circled and labelled trend exhaustion.",
            ),
            text_w=5.4,
            notes=(
                "Volume should rise through a trend. When it turns down early, the trend is inherently weak.",
                "The book's Facebook example uses price based volume. It names that and does not explain it.",
            ),
        ),
        Pair(
            left=Content(
                title="Open interest: watch for disagreement",
                lines=(
                    "For the most part, open interest action correlates fairly closely with volume action.",
                    "It is when the two diverge significantly that open interest adds evidence.",
                    "If open interest increases during a consolidation instead of decreasing, the breakout and the trend after it tend to be much more rapid and extended.",
                ),
                caption="Open interest is named here and taught in Chapter 6.",
            ),
            picture=Figure(
                number="4.17",
                shows="The schematic cycle with open interest rising through the distribution instead of falling, and the downside breakout that follows labelled strong.",
            ),
            text_w=5.4,
            notes=(
                "Chapter 3 listed open interest as transaction data. It has still not been defined: that is Chapter 6.",
                "One sentence is enough today: open interest rising inside a range means a harder breakout.",
            ),
        ),
    ),
)

# ==========================================================================
# 4.4 - Moving averages. Kept light: Chapter 11 teaches the tool.
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Moving Average Interpretation of Market Phase",
    short="4.4 Moving averages",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.4  Averages spread in a trend and tangle in a range",
                lines=(
                    "In a trend, multiple moving average lines diverge from each other.",
                    "The greater the divergence, the stronger the ensuing trend.",
                    "When the lines begin to converge, that is an early indication of a potential consolidation.",
                ),
                accent="In a consolidation the average flattens out and whipsaws increase significantly.",
            ),
            picture=Figure(
                number="4.21",
                shows="A daily chart with four moving averages: the lines overlap through an accumulation, fan apart through the trend phase, and overlap again in the consolidation that follows.",
            ),
            notes=(
                "This is review question 6: lines fanning apart, a trend; lines converging and overlapping, a consolidation.",
                "Whipsaw is used here and not defined. Moving averages are Chapter 11; say that and move on.",
            ),
        ),
        InlineCheck(
            label="Volume and moving averages",
            questions=(
                Q(
                    stem="Volume falls off partway through an uptrend. This is a sign of:",
                    options=("A stronger trend ahead",
                             "A selling climax",
                             "Trend exhaustion, and an earlier consolidation",
                             "An upside breakout"),
                    answer="C",
                    reason="A fall-off in volume during a trend is trend exhaustion: expect distribution or accumulation sooner.",
                ),
                Q(
                    stem="Several moving average lines that had spread apart begin to converge. This is an early indication of:",
                    options=("A potential consolidation",
                             "A stronger trend",
                             "A selling climax",
                             "A minimum measuring objective"),
                    answer="A",
                    reason="Diverging lines mean a trend. Converging lines are an early indication of a potential consolidation.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.5 - Divergence and momentum. Kept light: Chapter 9 teaches the tool.
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="Divergence and Momentum Interpretation of Market Phase",
    short="4.5 Divergence",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.5  Momentum turns before price",
                lines=(
                    "Divergence may be used to track the changes in price momentum.",
                    "That makes it useful for identifying potential consolidations and the strength of a trend.",
                    "Once divergence is observed, look for a slowing of the trend.",
                ),
                accent="At the tail end of a trend, momentum turning first warns that a consolidation may be forming.",
                caption="The chapter uses divergence, MACD and RSI without defining them. Divergence is Chapter 9.",
            ),
            picture=Figure(
                number="4.22",
                shows="An hourly EURUSD chart: price makes a higher peak inside a distribution while the MACD below it makes a lower one, labelled standard bearish divergence and momentum turning before price.",
            ),
            text_w=6.2,
            notes=(
                "This is review question 8: divergence shows momentum slowing, and a slowing trend is a consolidation forming.",
                "The book adds one rule for volume: for bullish divergence in volume, falling prices must come with decreasing volume.",
            ),
        ),
    ),
)

# ==========================================================================
# 4.6 - Sentiment. Kept light: Chapter 23 teaches the indicators.
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Sentiment Interpretation of Market Phase",
    short="4.6 Sentiment",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.6  Sentiment is clearest at the extremes",
                lines=(
                    "Sentiment indicators track the aggregate sentiment, emotions and psychology of participants.",
                    "They are most accurate at market extremes.",
                    "At distribution the put/call ratio and VIX are low but starting to increase. A/D, margin debt, new highs minus new lows and the Bullish Percent Index are high but starting to decrease.",
                ),
                accent="At accumulation every one of those readings is reversed.",
                caption="The book lists thirteen sentiment indicators here and explains none. They are Chapter 23.",
            ),
            picture=Figure(
                number="4.25",
                shows="A price curve from a distribution at the top to an accumulation at the bottom, with six sentiment readings listed beside each: put/call ratio, A/D, VIX, margin debt, new highs minus new lows and the Bullish Percent Index.",
            ),
            text_w=6.2,
            notes=(
                "This is review question 5: which sentiment indicators best describe distributions? Read the top list in the figure.",
                "Fear, greed and hope: participants swing between them and repeat the same patterns, most visibly at extremes.",
            ),
        ),
        InlineCheck(
            label="Divergence and sentiment",
            questions=(
                Q(
                    stem="At the tail end of a trend, a momentum indicator turns before price does. This is an early sign that:",
                    options=("The trend is strengthening",
                             "A consolidation may be forming",
                             "Volume is about to surge",
                             "The pattern is intrinsically neutral"),
                    answer="B",
                    reason="Momentum turning before price shows the trend slowing, which is how a consolidation begins.",
                ),
                Q(
                    stem="At a distribution, margin debt is:",
                    options=("Low and starting to increase",
                             "Low and starting to decrease",
                             "High and starting to increase",
                             "High and starting to decrease"),
                    answer="D",
                    reason="At a top margin debt is high and starting to decrease. At a bottom it is low and starting to increase.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.7 - Sakata's interpretation of market phase. Taught in full.
# ==========================================================================

SECTION7 = Section(
    number=7,
    title="Sakata's Interpretation of Market Phase",
    short="4.7 Sakata",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Term(
                term="4.7  Sakata's Five Methods",
                plain="A Japanese way of reading the market that divides it into five phases, not Dow's three.",
                example="In the left panel: three bottoms, three thrusts with a correction after each, then three tops.",
                formal="A unique Japanese approach for interpreting and understanding the markets, which originated with Munehisa Honma. The market is divided into five distinct phases, as opposed to the conventional three-phase model by Dow.",
            ),
            picture=Figure(
                number="4.26",
                shows="Two panels side by side: Sakata's five market phases, with San Sen at the bottom, San Pei, San Poh and San Ku through the rise and San Zan at the top, beside Elliott's 5-3 wave structure.",
            ),
            text_w=6.3,
            notes=(
                "The left panel is Sakata, the right is Elliott. Leave Elliott for the next section.",
                "Honma's name is all the history the book gives. Do not add to it.",
            ),
        ),
        Content(
            title="The five methods, by name",
            lines=(
                "San Zan, three mountains: the Western triple top. The distribution phase.",
                "San Sen, three rivers: the Western triple bottom. The accumulation phase.",
                "San Ku, three gaps: the breakaway, runaway and exhaustion gaps of the trend.",
                "San Pei, three thrusts: three trending phases, accumulation to distribution.",
                "San Poh, three methods: the three corrections, one after each thrust.",
            ),
            accent="Two of the five are consolidations. Three describe the trend between them.",
            notes=(
                "The book glosses every name as three of something. That is the handle for remembering all five.",
                "Chapter 3 named the breakaway, runaway and exhaustion gaps. Sakata counts the same three.",
            ),
        ),
        Pair(
            left=Content(
                title="Five phases inside three",
                lines=(
                    "Dow's three phases may seem inconsistent with Sakata's five.",
                    "Simple chart patterns show the two need not be viewed as distinct.",
                    "A triple bottom, three thrusts with flags and gaps between them, then a triple top.",
                ),
                accent="The book offers this as a plausible resolution between Eastern and Western approaches.",
            ),
            picture=Figure(
                number="4.27",
                shows="Dow's three-phase market drawn with Sakata's pieces: a triple bottom as the accumulation phase, a rising channel of thrusts, bullish flags and the breakaway, runaway and exhaustion gaps as the trend phase, and a triple top as the distribution phase.",
            ),
            text_w=5.4,
            notes=(
                "This is the chapter objective on comparing Eastern and Western approaches. The answer is that one fits inside the other.",
                "Sakata's model is less rigid than Elliott's, which has specific rules for wave construction. That is the bridge to 4.8.",
            ),
        ),
        InlineCheck(
            label="Sakata's five methods",
            questions=(
                Q(
                    stem="San Zan, three mountains, is equivalent to the Western:",
                    options=("Triple bottom, the accumulation phase",
                             "Triple gap, in the trending phase",
                             "Triple top, the distribution phase",
                             "Three corrections, one after each thrust"),
                    answer="C",
                    reason="San Zan is the triple top and represents distribution. San Sen, three rivers, is the triple bottom.",
                ),
                Q(
                    stem="San Poh, three methods, represents:",
                    options=("The three corrections, one after each thrust",
                             "The three gaps of the trending phase",
                             "The triple bottom",
                             "The three trending phases"),
                    answer="A",
                    reason="San Poh is the three corrections. The thrusts themselves are San Pei.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.8 - Elliott. Kept light: Chapter 18 teaches the waves.
# ==========================================================================

SECTION8 = Section(
    number=8,
    title="Elliott's Interpretation of Market Phase",
    short="4.8 Elliott",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.8  Elliott: five waves up, three waves down",
                lines=(
                    "Elliott described markets as moving in an impulsive five-wave up, then a corrective three-wave down.",
                    "The trending phase is impulse waves 1, 3 and 5.",
                    "The accumulation phase is corrective waves 2 and 4. Distribution is usually the abc correction.",
                ),
                accent="Sakata's San Pei closely resembles waves 1, 3 and 5. Elliott has specific rules; Sakata's model is less rigid.",
                caption="One sentence earlier the book also places the abc correction under accumulation, 'in most cases'. Elliott waves are Chapter 18.",
            ),
            picture=Figure(
                number="4.28",
                shows="Elliott's wave structure: five numbered motive waves rising, with waves 1, 3 and 5 marked impulsive, then three lettered corrective waves a, b and c falling. Eight waves of one degree.",
            ),
            text_w=6.2,
            notes=(
                "The book gives the abc correction to accumulation in most cases and to distribution usually, in consecutive sentences. Say so; do not pick one.",
                "Nothing on the abc correction is examined from this chapter. Waves 1, 3 and 5 as the trend is.",
            ),
        ),
    ),
)

# ==========================================================================
# 4.9 - Cycle analysis. Kept light: Chapter 20 teaches cycles.
# ==========================================================================

SECTION9 = Section(
    number=9,
    title="Cycle Analysis Interpretation of Market Phase",
    short="4.9 Cycles",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.9  Where in the cycle decides what the pattern is",
                lines=(
                    "Formations between cycle extremes tend to be continuations.",
                    "Formations at cycle peaks tend to be distributions.",
                    "Formations at cycle troughs tend to be accumulations.",
                ),
                accent="A neutral symmetrical triangle takes all three roles, depending only on where it forms.",
                caption="The guideline is for formations on the same cycle degree. Finding the cycle is Chapter 20.",
            ),
            picture=Figure(
                number="4.31",
                shows="A price cycle with the same symmetrical triangle drawn at three places: as accumulation at a cycle trough, as continuation between the extremes, and as distribution at the cycle peak.",
            ),
            text_w=5.4,
            notes=(
                "This is review question 7, and it is extrinsic bias again: the phase of the cycle was one of the five factors.",
                "The book makes the same point with a rising price channel in place of the cycle: bottom of the channel, middle, top.",
            ),
        ),
        InlineCheck(
            label="Elliott and cycles",
            questions=(
                Q(
                    stem="In Elliott's description, the trending phase is represented by:",
                    options=("Corrective waves 2 and 4",
                             "Impulse waves 1, 3 and 5",
                             "Waves a, b and c",
                             "All eight waves"),
                    answer="B",
                    reason="The impulse waves 1, 3 and 5 are the trend. Waves 2 and 4 are corrective.",
                ),
                Q(
                    stem="A formation that unfolds at a cycle trough tends to be:",
                    options=("A continuation",
                             "A distribution",
                             "A V top",
                             "An accumulation"),
                    answer="D",
                    reason="Troughs tend to hold accumulations, peaks distributions, and the stretch between them continuations.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# Opening and closing. Section 4.10, the book's summary, feeds the closing.
# ==========================================================================

OPENERS = (
    Content(
        title="What you will be able to do",
        lines=(
            "Understand the structural and functional characteristics of the three market phases.",
            "Forecast market phase accurately via its behavioral and cyclical properties.",
            "Identify potential market regime changes via volume action.",
            "Describe the inertial and momentum characteristics for each market phase.",
            "Identify specific price pattern formations associated with each phase.",
            "Compare and contrast Eastern and Western approaches to interpreting market phases.",
        ),
        notes=(
            "These are the book's six learning objectives for the chapter, in its own words.",
            "Do not read all six aloud. Say the first and the last, and that every one is examinable.",
        ),
    ),
    Content(
        title="How this chapter is laid out",
        lines=(
            "4.1  Dow: the three phases themselves, and when a consolidation is over.",
            "4.2  Chart patterns: which pattern belongs to which phase, and why.",
            "4.3 to 4.6  Volume, moving averages, divergence and sentiment.",
            "4.7  Sakata: the Japanese five phase model.",
            "4.8 and 4.9  Elliott waves and cycles.",
        ),
        accent="4.1, 4.2 and 4.7 are taught in full. The other six preview tools that have chapters of their own.",
        notes=(
            "One question runs through all nine sections: which phase is the market in?",
            "Say the checks carry no marks. Each answer is on its own check slide and appears on a click.",
        ),
    ),
)

CLOSING = (
    Content(
        title="Chapter 4 in five sentences",
        lines=(
            "Markets consolidate or trend; a consolidation is accumulation or distribution.",
            "Which one it was is known only afterwards, so the analyst gathers evidence.",
            "Chart patterns are evidence: their intrinsic and extrinsic bias should agree.",
            "Volume, moving averages, divergence, sentiment and cycles each add evidence.",
            "Sakata's five phases and Elliott's waves fit inside Dow's three.",
        ),
        accent="Recognizing a phase transition tells you which technical tool or setup to use.",
        notes=(
            "Read all five slowly. This is the summary to copy down.",
            "Next is Chapter 5, which takes the trend phase in more detail.",
        ),
    ),
    Content(
        title="The review questions to prepare",
        lines=(
            "Define the term consolidation, and explain why most chart patterns are consolidation patterns.",
            "List eight chart patterns that are intrinsically bullish.",
            "Describe how you would determine if accumulation is taking place.",
            "Which sentiment indicators best describe distributions?",
            "How would you use moving averages, and a cycle, to gauge market phase?",
            "How do you use divergence to identify potential consolidations?",
        ),
        caption="All eight of the book's questions, on six lines. Each is answered on a slide in this deck.",
        notes=(
            "Lines one and five each carry two of the book's eight questions.",
            "Say where each answer sits: 4.1 and 4.2, 4.2, 4.1, 4.6, 4.4 and 4.9, 4.5.",
        ),
    ),
    Content(
        title="What this chapter names and does not teach",
        lines=(
            "Chart pattern shapes: Chapter 13. Open interest: Chapter 6.",
            "Moving averages and whipsaws: Chapter 11. Divergence: Chapter 9.",
            "The thirteen sentiment indicators: Chapter 23. Elliott's rules: Chapter 18. Cycles: Chapter 20.",
            "The objectives promise inertial characteristics; the text never uses the word.",
        ),
        accent="From this chapter, only what each tool says about market phase is examinable.",
        caption="Do not fill these from outside the book. Each comes back in its own chapter.",
        notes=(
            "Be straight with them: six of the nine sections borrow tools the book has not taught yet.",
            "MACD, RSI and price based volume are also used and not explained. Same answer: later chapters.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 4",
    title="Market Phase Analysis",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    # The objectives and the roadmap are drawn by OPENERS below, one slide
    # each. These two fields are what the generated frame would have used.
    objectives=OPENERS[0].lines,
    roadmap=OPENERS[1].lines,
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6,
              SECTION7, SECTION8, SECTION9),
    closing=CLOSING,
    openers=OPENERS,
    title_notes=(
        "Greet the room, then say what today buys them: one question, which phase is the market in, answered nine ways.",
        "Say this deck is short on purpose. Three sections are taught in full and six are previews of later chapters.",
    ),
    dividers=False,
)
