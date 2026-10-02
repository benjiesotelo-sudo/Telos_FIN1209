"""Chapter 4 content for FIN1209 - Market Phase Analysis.

This file is pure data. It carries no drawing code.

Source of the chapter scope is Lim, M. (2016), The Handbook of Technical
Analysis, chapter 4, printed pages 99 to 124, which students have in the
course text. Everything here is written from scratch in teaching language.

This chapter is a trial of a leaner deck than Chapters 1 to 3, and this is
its second build. The instructor read the first one, 46 slides, and sent it
back for three reasons, which are the three rules this file is written to:

  * **Every idea has a picture beside it.** The first build left the book's
    three pages on who buys and who sells in each phase as five slides of
    text, and they could not be taught from. Every teaching slide here is a
    Pair: the idea on the left and a picture on the right. Where the book
    has a figure, it is the book's. Where the book makes the point only in
    words, it is one of our own charts; see charts_chapter04.py for which
    and why. One slide has no picture, the list of thirteen sentiment
    indicators, because the book names them and explains none.

  * **A question and its answer are separate slides.** The first build
    revealed each answer on the question slide. The instructor could not
    present that, so every check is an ordinary Check again: a question
    slide, then a reveal slide, as in Chapters 1 to 3.

  * **The book's content is not cut.** The lean rule cuts a slide that
    teaches nothing new: a divider, a recap, a figure standing alone with no
    words. It never cuts what the book says. All 32 of the book's figures
    are placed, each with what the book says about it, and section 4.2
    teaches every one of the book's lists.

What is still lean, against Chapters 1 to 3:

  * The parts are the book's own sections, 4.1 to 4.9, not six parts.
    Section 4.10 is the book's summary and feeds the closing slides.
  * No divider slide and no recap slide. The first slide of a part carries
    the book's section number in its title.
  * A picture sits beside its idea, not on a slide of its own after it.

Every section is taught as fully as the book teaches it. Sections 4.3 to
4.6, 4.8 and 4.9 borrow a tool that a later chapter of the book teaches, and
there the deck takes what the section says about market phase and names,
on the slide, what it uses without explaining.

Where the standing rule bites, and how each place is handled. Every one is
named on a slide, and no check rests on any of them.

  * Consolidation. Review question 1 asks for a definition and the book
    never sets one apart. The term slide joins its sentence in 4.1 (two
    basic phases) with its sentence in 4.2 (how a market consolidates), and
    the speaker cue says that is what was done.

  * The shapes of the chart patterns. Section 4.2 lists seventeen patterns
    by name and shows seven of them on real charts, Figures 4.6 to 4.14,
    which are all placed. It describes no shape in words; the book does
    that in its Chapter 13. Charts M, N and O sketch the shapes from
    Chapter 13's own one line descriptions, say so on their face, and no
    check asks for a shape.

  * Broadening formations. The book's list of patterns that are bullish with
    respect to an uptrend includes them, and its next paragraph and its own
    Figure 4.5 treat them as reversal formations that disagree with the
    trend. The slide says so and teaches the paragraph.

  * The abc correction. The book gives it to accumulation "in most cases"
    and to distribution "usually", in consecutive sentences. The slide says
    both and no question is set on it.

  * The Bullish Percent Index. Figure 4.25 names it and the book's list of
    thirteen sentiment indicators names a Bullish Sentiment Index instead.
    The slide says the book does not say whether they are the same.

  * Things the chapter uses and never explains: open interest, whipsaws,
    divergence, MACD and RSI, the thirteen sentiment indicators, Elliott's
    rules, Fibonacci projections, how a cycle is found, price based volume,
    and the inertial characteristics its own learning objectives promise.
    Each is named where it appears and the closing slides collect them.
"""

from deckkit import (
    Chapter,
    Chart,
    Check,
    Content,
    Figure,
    Pair,
    Question,
    Section,
    Term,
)

Q = Question

# The text column beside one of our own charts. charts_chapter04.py draws
# every chart to fill the picture column these two widths leave.
CHART_W = 5.4
TERM_CHART_W = 5.8

# ==========================================================================
# 4.1 - Dow theory of market phase.
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Dow Theory of Market Phase",
    short="4.1 Dow",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.1  Markets move in phases",
                lines=(
                    "Dow Theory, in Chapter 2: a primary trend has three phases. Accumulation, trending, distribution.",
                    "That description is now regarded as the basic underlying characteristic of market action.",
                    "Phase analysis applies across all time frames.",
                ),
                accent="Not recognizing the phases and their transitions greatly disadvantages the practitioner.",
            ),
            picture=Chart(
                letter="A",
                shows="One invented price line through an accumulation, the trend up out of it, a distribution, and the trend down out of that.",
            ),
            text_w=CHART_W,
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
            picture=Chart(
                letter="B",
                shows="One consolidation with two dashed paths leaving it: up, in which case it was accumulation, and down, in which case it was distribution.",
            ),
            text_w=CHART_W,
            notes=(
                "Cover the two dashed paths with a hand. The range looks the same either way; the label needs the next move.",
                "The rest of the chapter is the hunt for evidence: volume, patterns, averages, momentum, sentiment, cycles.",
            ),
        ),
        Pair(
            left=Content(
                title="The first evidence: volume in a consolidation",
                lines=(
                    "Volume normally declines gradually during a consolidation.",
                    "Very low volume is a strong sign the consolidation may be ending, and a trend starting.",
                    "On a daily chart a consolidation normally lasts about three to six months, or longer.",
                ),
                accent="The last box on the chart says only consolidation. What follows was not yet known.",
            ),
            picture=Figure(
                number="4.2",
                shows="The daily Dow Jones Industrial Average with its accumulation, trending and distribution phases boxed and named, a last box named only consolidation, and a volume panel below with the decline in volume through each consolidation drawn in.",
            ),
            text_w=5.2,
            notes=(
                "Point at each grey box, then at the arrow under it in the volume panel: volume falls through every one.",
                "The box at the top right is labelled only consolidation: nobody knew yet. Which one it was could only be said afterwards.",
            ),
        ),
        Pair(
            left=Content(
                title="The same phases at every time scale",
                lines=(
                    "A primary trend typically spans months to years in the equity markets.",
                    "In commodity futures it tends to be shorter: high leverage induces greater volatility.",
                    "Dow described the equity markets, but the phases are found across all markets.",
                ),
                accent="They show on sub-hourly charts too: micro phase action, shaped by the macro phase behavior around it.",
            ),
            picture=Figure(
                number="4.3",
                shows="A 15 minute EURUSD chart with distribution, trend and accumulation phases boxed one after another, titled micro phase action.",
            ),
            text_w=5.2,
            notes=(
                "The figure is a 15 minute chart and it has every phase the daily Dow chart had.",
                "Multiple time frames are how the book says to see it: the macro phase first, then the micro phases inside it.",
            ),
        ),
        Pair(
            left=Content(
                title="Accumulation: the informed buy from the frightened",
                lines=(
                    "It normally follows a deep and rapid decline, on very negative data and bearish headlines.",
                    "The uninformed are extremely bearish and sell at whatever price is available.",
                    "The informed buy from them: a contrarian approach that needs deep pockets.",
                    "They gather shares very gradually, careful not to drive prices up too fast.",
                ),
                accent="The sell-off that ends the downtrend is called a selling climax.",
            ),
            picture=Chart(
                letter="C",
                shows="A deep, rapid decline ending in a selling climax, where the uninformed sell and the informed buy, then a long accumulation range through which the informed keep gathering shares.",
            ),
            text_w=CHART_W,
            notes=(
                "Chapter 2 named the two sides. What is new is how the informed buy: slowly, so the price stays low.",
                "Their buying is what creates the final and decisive bottom. The book calls it very large responsive buying.",
            ),
        ),
        Pair(
            left=Content(
                title="The uptrend feeds on itself",
                lines=(
                    "Technical traders get in early, on a clear upside breakout. Market savvy investors follow.",
                    "As the uptrend becomes obvious the public is drawn in, and the bears cover their shorts.",
                    "Regret bias: those who missed out, or sold too early, buy at every dip.",
                    "At even higher prices the herd uses more margin, even borrowing to invest.",
                ),
                accent="A vicious positive feedback cycle.",
            ),
            picture=Chart(
                letter="D",
                shows="An uptrend out of an accumulation, with the five groups marked in the order they arrive: technical traders, market savvy investors, the public, the regretful buying each dip, and the herd on margin.",
            ),
            text_w=CHART_W,
            notes=(
                "Read the five numbers on the chart in order. Each group pays more than the one before it.",
                "Regret bias is the term to underline: the fear of having missed out keeps the buying going.",
            ),
        ),
        Pair(
            left=Content(
                title="The downtrend: the same cycle, downward",
                lines=(
                    "It begins with a breakdown from a distribution range, on increasingly bearish data.",
                    "The uninformed begin to unload, and previously bullish participants liquidate.",
                    "Past the threshold of pain and the margin limits, capital flows out of the market.",
                ),
                accent="Bearish sentiment intensifies as prices sink: the same vicious feedback cycle.",
            ),
            picture=Chart(
                letter="E",
                shows="A downtrend out of a distribution, marked in order: the breakdown, the uninformed beginning to unload, bullish holders liquidating, and capital flowing out once margin limits are passed.",
            ),
            text_w=CHART_W,
            notes=(
                "Mirror the uptrend slide: each step is the same feedback with the sign reversed.",
                "Further unexpected declines attract more public attention, and that causes the larger liquidation.",
            ),
        ),
        Pair(
            left=Content(
                title="Distribution: the same story upside down",
                lines=(
                    "It normally follows a strong and rapid rise, on very positive data and the most bullish headlines.",
                    "The uninformed buy at whatever price is available: irrational exuberance. Margin debt is skyrocketing.",
                    "The informed sell to them very gradually, careful not to drive prices down too rapidly.",
                ),
                accent="The surge that ends the uptrend is called a blow-off, or buying climax.",
            ),
            picture=Chart(
                letter="F",
                shows="A strong, rapid rise ending in a blow-off, or buying climax, where the uninformed buy and the informed sell, then a distribution range through which the informed keep selling.",
            ),
            text_w=CHART_W,
            notes=(
                "Irrational exuberance came up in Chapter 2. Margin debt is new here and comes back in the sentiment section.",
                "Mirror the accumulation slide line by line. Students should be able to write one from the other.",
            ),
        ),
        Check(
            label="Who is on each side",
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
                    stem="In a selling climax, who is doing the buying?",
                    options=("The uninformed, in a state of irrational exuberance",
                             "The general public, on margin",
                             "Technical traders, on an upside breakout",
                             "The informed, taking a contrarian approach"),
                    answer="D",
                    reason="The uninformed sell at whatever price is available, and the informed buy from them.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Why tops are shorter and rougher than bottoms",
                lines=(
                    "Accumulation normally lasts longer than distribution.",
                    "The uptrend tends to be more prolonged than the downtrend.",
                    "Distributions tend to be much more volatile than accumulations.",
                ),
                accent="One reason covers all three: at higher prices more capital, and more unrealized profit, is at risk.",
            ),
            picture=Chart(
                letter="G",
                shows="One cycle drawn to the book's three comparisons: a long, quiet accumulation, a prolonged uptrend, a short and volatile distribution, and a short downtrend.",
            ),
            text_w=CHART_W,
            notes=(
                "Ask why before showing the gold line. The book gives the same reason three times.",
                "At the bottom there is less to lose, so nobody is in a hurry. At the top everyone has profit to protect.",
            ),
        ),
        Pair(
            left=Content(
                title="The signs of an accumulation",
                lines=(
                    "It comes after a relatively rapid decline, ideally near a significant prior bottom.",
                    "There is no evidence of lower troughs being formed.",
                    "Volume begins to subside as a potential upside breakout approaches.",
                    "The longer it lasts, the more powerful the breakout, typically on a surge in volume.",
                ),
                accent="It starts a new primary bull market, or a shorter-term uptrend.",
            ),
            picture=Chart(
                letter="H",
                shows="An accumulation after a rapid decline, sitting on the level of a significant prior bottom with no lower troughs, over a volume panel that subsides through the range and surges on the breakout.",
            ),
            text_w=CHART_W,
            notes=(
                "This is review question 4: how would you determine if accumulation is taking place? These are the signs.",
                "The book says the breakout can be to either side of the range. The signs are evidence, not proof.",
            ),
        ),
        Pair(
            left=Content(
                title="The signs of a distribution",
                lines=(
                    "It comes after a prolonged uptrend, ideally near a significant prior top.",
                    "Signs of market exhaustion show, and no higher peaks form.",
                    "Volume begins to subside as a potential downside breakout approaches.",
                    "The longer it lasts, the more powerful the breakout, typically on a surge in volume.",
                ),
                accent="It starts a new primary bear market, or a shorter-term downtrend.",
            ),
            picture=Chart(
                letter="I",
                shows="A distribution after a prolonged uptrend, under the level of a significant prior top with no higher peaks, over a volume panel that subsides through the range and surges on the breakout.",
            ),
            text_w=CHART_W,
            notes=(
                "The same list as accumulation with every direction reversed, plus one extra: signs of exhaustion.",
                "It is shorter and more volatile than the accumulation, for the reason already given: more capital at risk.",
            ),
        ),
        Check(
            label="Reading a consolidation",
            questions=(
                Q(
                    stem="Accumulation normally lasts longer than distribution because, at the bottom of the market:",
                    options=("Less capital is at risk at the lower prices",
                             "Volume is always higher",
                             "The uninformed are buying heavily",
                             "Leverage is higher than at the top"),
                    answer="A",
                    reason="Lower prices mean a lower amount of capital at risk, so the bottom takes its time.",
                ),
                Q(
                    stem="Which of these is a sign that accumulation, and not distribution, is taking place?",
                    options=("The range follows a prolonged uptrend",
                             "No higher peaks form, near a significant prior top",
                             "No lower troughs form, near a significant prior bottom",
                             "Margin debt is skyrocketing"),
                    answer="C",
                    reason="Accumulation follows a rapid decline, near a significant prior bottom, with no lower troughs. The other three belong to distribution.",
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
            text_w=5.6,
            notes=(
                "Subjectivity again, as in Chapter 1: three analysts, three completion points, one chart.",
                "Once a consolidation is complete, a trend may already be in effect. The book says that follows logically.",
            ),
        ),
        Pair(
            left=Term(
                term="Minimum measuring objective",
                plain="The least a breakout is expected to travel: usually the height of the range it broke out of.",
                example="A share ranges between PHP 40 and PHP 44, a height of PHP 4. On an upside breakout the minimum target is 44 + 4 = PHP 48.",
                formal="The expected minimum price target, which is usually a price excursion equal to the range or height of the consolidation.",
            ),
            picture=Chart(
                letter="J",
                shows="A range between PHP 40 and PHP 44 and the three completion levels above it in pesos: the breakout at 44, the band 3 to 5 percent above the peak at 45.32 to 46.20, and the minimum measuring objective at 48.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Do the arithmetic on the board: the top of the range plus the height of the range.",
                "Figure 4.4 called this the one to one minimum target projection. It is the same thing.",
            ),
        ),
        Check(
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
# 4.2 - Chart pattern interpretation of market phase.
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Chart Pattern Interpretation of Market Phase",
    short="4.2 Chart patterns",
    minutes="",
    covers=(),
    slides=(
        Pair(
            left=Content(
                title="4.2  Chart patterns show the phase",
                lines=(
                    "Market phase can also be identified by the type of chart pattern at each stage.",
                    "Most chart patterns belong to one of two groups: reversal or continuation.",
                    "Accumulation and distribution tend to hold reversal patterns. Continuation patterns form within the trend.",
                ),
                accent="So the kind of pattern on the chart is evidence of the phase the market is in.",
            ),
            picture=Chart(
                letter="K",
                shows="One price line with three patterns boxed: a reversal pattern at the bottom as accumulation, a continuation pattern inside the trend, and a reversal pattern at the top as distribution.",
            ),
            text_w=CHART_W,
            notes=(
                "Say why it matters: a pattern is one more piece of evidence for accumulation or distribution.",
                "Reversal and continuation are the two words to hold. Every pattern in this section is filed under one.",
            ),
        ),
        Pair(
            left=Term(
                term="Consolidation pattern",
                plain="A pattern that stays inside a range and is not trending anywhere.",
                example="A share drifts between PHP 40 and PHP 44 for six weeks as a triangle forms.",
                formal="A chart pattern is usually regarded as a consolidation pattern if it unfolds within a relatively confined and well defined price range, and lacks any significant trend component.",
            ),
            picture=Chart(
                letter="L",
                shows="A pattern boxed inside a confined range with no trend component, beside a V bottom, which has no confined range and a strong trend component.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "Two tests, both needed: a confined range, and no significant trend component.",
                "Hold the two tests against the V on the right of the chart. It fails both.",
            ),
        ),
        Pair(
            left=Content(
                title="Most patterns consolidate. V reversals do not.",
                lines=(
                    "A market in indecision, rest or exhaustion ranges, or makes small corrective moves.",
                    "So most reversal and continuation patterns are also consolidation patterns.",
                    "V tops and V bottoms are the exception: no confined range, a strong trend component.",
                ),
                accent="V reversals are the hardest to forecast: seen only in hindsight.",
                caption="They occur more often during distributions than accumulations.",
            ),
            picture=Figure(
                number="4.8",
                shows="A 4 hour USDCAD chart: a head and shoulders distribution labelled intrinsically bearish, a decline into a sharp V bottom labelled a rapid accumulation phase, and a new consolidation after the rise.",
            ),
            text_w=5.2,
            notes=(
                "This is review question 3: why are most chart patterns consolidation patterns? The first two lines are the answer.",
                "In the figure the V bottom is the accumulation: a very rapid one, with no range to see it forming in.",
            ),
        ),
        Pair(
            left=Term(
                term="Intrinsic bias",
                plain="The bullish or bearish lean a pattern carries in itself, wherever it appears.",
                example="An ascending triangle is intrinsically bullish. Wherever it occurs, it is inherently a bullish indication.",
                formal="The inherent bullish or bearish sentiment associated with a chart pattern that is independent of location, where sentiment is strictly based on the nature of the pattern.",
            ),
            picture=Figure(
                number="4.6",
                shows="A EURUSD chart with an inverted head and shoulders boxed at the bottom of a decline, labelled an intrinsically bullish pattern and a reversal pattern, and the trend phase rising out of it.",
            ),
            text_w=5.8,
            notes=(
                "The figure's pattern is an inverted head and shoulders, as accumulation. The trend phase kicks in after the upside breakout.",
                "The book points out this chart cannot tell us the pattern's extrinsic bias: it shows no price history, cycle or barrier.",
            ),
        ),
        Pair(
            left=Content(
                title="Intrinsically bullish: the book's eight",
                lines=(
                    "Bullish pennants, and bullish flags.",
                    "Ascending triangles, and inverted head and shoulders.",
                    "Rounding bottoms, and cup and handles.",
                    "Falling wedges, and double, triple and multiple bottoms.",
                ),
                accent="Wherever one of these forms, it is inherently a bullish indication.",
                caption="Review question 2 asks for these eight.",
            ),
            picture=Chart(
                letter="M",
                shows="Eight small sketches, one for each intrinsically bullish pattern on the book's list, drawn from the descriptions in the book's Chapter 13.",
            ),
            text_w=CHART_W,
            notes=(
                "They need to be able to list the eight. The sketches are a preview: Chapter 13 teaches each shape properly.",
                "Pairs help: pennants and flags, the two with a pole; the two rounded ones; the triangle and the wedge.",
            ),
        ),
        Pair(
            left=Content(
                title="Intrinsically bearish: the book's seven",
                lines=(
                    "Bearish pennants, and bearish flags.",
                    "Descending triangles, and standard head and shoulders.",
                    "Rounding tops, and rising wedges.",
                    "Double, triple and multiple tops.",
                ),
                accent="Each is a bullish pattern turned upside down.",
                caption="The cup and handle is on the bullish list and has no twin on this one.",
            ),
            picture=Chart(
                letter="N",
                shows="Seven small sketches, one for each intrinsically bearish pattern on the book's list, each the mirror image of a bullish one.",
            ),
            text_w=CHART_W,
            notes=(
                "Put this beside the last slide: a falling wedge is bullish, a rising wedge is bearish. Students get that one backwards.",
                "Seven and not eight, because the book lists no bearish cup and handle.",
            ),
        ),
        Pair(
            left=Content(
                title="Intrinsically neutral patterns",
                lines=(
                    "Symmetrical triangles and horizontal channels have no obvious bias in sentiment.",
                    "Some authors classify them as continuation patterns, others as reversal patterns.",
                    "Broadening, diamond and island formations are also neutral, but are regarded as reversal formations.",
                ),
                accent="Whether a neutral pattern reverses or continues is decided beyond the pattern itself.",
            ),
            picture=Chart(
                letter="O",
                shows="Four small sketches: a symmetrical triangle and a horizontal channel, the two intrinsically neutral patterns, and a broadening formation and an island formation, which are neutral but regarded as reversals.",
            ),
            text_w=CHART_W,
            notes=(
                "The accent is the bridge to the next term: if the shape does not decide, the location must.",
                "Diamonds are named with the others and have no sketch. The book gives no description to draw from.",
            ),
        ),
        Check(
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
                    stem="Which of these patterns is intrinsically bullish?",
                    options=("A falling wedge",
                             "A rising wedge",
                             "A symmetrical triangle",
                             "A standard head and shoulders"),
                    answer="A",
                    reason="Falling wedges are on the book's list of eight. Rising wedges and standard head and shoulders are bearish, and the symmetrical triangle is neutral.",
                ),
            ),
        ),
        Pair(
            left=Term(
                term="Extrinsic bias",
                plain="The lean a pattern takes from where it sits, not from its shape.",
                example="An ascending triangle at the price level of a historically significant market top is extrinsically bearish: it sits at a significant resistance.",
                formal="Location-based sentiment: sentiment that is dependent on factors that are external, or extrinsic, to the pattern.",
            ),
            picture=Chart(
                letter="P",
                shows="The same ascending triangle drawn at three locations: at a historically significant bottom, where it is intrinsically and extrinsically bullish; in the middle of an uptrend, where a continuation is likelier; and at a historically significant top, where it is extrinsically bearish.",
            ),
            text_w=TERM_CHART_W,
            notes=(
                "This is the book's own worked example. The shape never changes: bullish. Only the location does.",
                "At the bottom both biases are bullish, so the tendency for a reversal is greater. At the top they disagree.",
            ),
        ),
        Pair(
            left=Content(
                title="What sets the extrinsic bias",
                lines=(
                    "The direction of the preceding trend.",
                    "Location with respect to historical extremes in price.",
                    "Location with respect to the phase of an underlying market cycle.",
                    "Location with respect to other supportive and resistive overlay barriers.",
                    "Bullish or bearish divergent formations.",
                ),
                caption="Figure 4.12: a neutral triangle on a well tested accumulation zone, beside trendline support, is extrinsically bullish.",
            ),
            picture=Figure(
                number="4.12",
                shows="The daily gold chart: a symmetrical triangle labelled extrinsically bullish, forming on a strong accumulation zone tested by multiple bottoms, beside a downtrend line acting as support, all inside a larger consolidation that contains smaller distributions and accumulations.",
            ),
            text_w=5.2,
            notes=(
                "Five factors, all outside the pattern. The figure shows the second and the fourth at work on a neutral triangle.",
                "The trend phase follows after a short return move to the triangle's breakout barrier. Divergence and cycles come later today.",
            ),
        ),
        Pair(
            left=Content(
                title="When the biases agree",
                lines=(
                    "Intrinsic and extrinsic bias agree: a reversal at a top or bottom is more reliable.",
                    "Intrinsic bias in agreement with the trend sentiment, the direction of the trend: a continuation is more likely.",
                    "Any disagreement: the reversal or continuation may be inherently weak.",
                ),
                accent="An ascending triangle in an uptrend: bullish pattern, bullish trend.",
            ),
            picture=Figure(
                number="4.13",
                shows="A 15 minute EURUSD chart with an ascending triangle, a flat top and a rising lower line, forming partway up an uptrend and labelled as continuation in a trend phase.",
            ),
            text_w=5.2,
            notes=(
                "Trend sentiment is the book's name for the directionality of the trend. It is used from here on.",
                "When attempting to judge the reliability of a reversal or a continuation, the book says: look for agreement.",
            ),
        ),
        Pair(
            left=Content(
                title="Continuation patterns agree with the trend",
                lines=(
                    "Bullish with respect to an uptrend: bullish pennants and flags, ascending triangles, inverted head and shoulders, rounding bottoms, cup and handles, falling wedges.",
                    "Bearish with respect to a downtrend: bearish pennants and flags, descending triangles, standard head and shoulders, rising wedges.",
                ),
                accent="A continuation pattern's bias should agree with the trend sentiment.",
                caption="Figure 4.10: a bear flag, confirmed once price violates the pattern.",
            ),
            picture=Figure(
                number="4.10",
                shows="A 15 minute EURUSD chart: a distribution, a downside breakout, then a bear flag labelled intrinsically bearish and as continuation, with prices consolidating in a diagonally constrained manner before the trend resumes.",
            ),
            text_w=5.2,
            notes=(
                "The flag's intrinsic bias agrees with the bearish trend sentiment, which greatly increases the potential for a reliable follow through.",
                "These two lists are the book's patterns with respect to trend sentiment. The neutral patterns on them get their own slide.",
            ),
        ),
        Figure(
            title="A rounding bottom, or cup and handle, as continuation",
            number="4.14",
            shows="A 4 hour EURUSD chart with a rounding bottom, or cup and handle, forming partway up an uptrend and labelled as continuation in a trend phase.",
            notes=(
                "The book gives this with the ascending triangle in one sentence: two bullish patterns acting as continuation in trend phases.",
                "It is the only place the chapter draws a rounding bottom. Trace the cup, then the line across its rim.",
            ),
        ),
        Check(
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
                    stem="A bear flag forms during a downtrend. Its intrinsic bias and the trend sentiment are:",
                    options=("In disagreement, so a reversal is likely",
                             "In agreement, so a continuation is more likely",
                             "Both neutral, so nothing can be said",
                             "Unknown until volume confirms them"),
                    answer="B",
                    reason="A bearish pattern in a bearish trend: when intrinsic bias agrees with the trend sentiment, the potential for a continuation is greater.",
                ),
            ),
        ),
        Pair(
            left=Content(
                title="Reversal patterns disagree with the trend",
                lines=(
                    "As a general guide, intrinsic bias and trend sentiment disagree for reversal patterns.",
                    "A standard head and shoulders, intrinsically bearish, ends an uptrend as distribution.",
                    "An inverted one, intrinsically bullish, ends a downtrend as accumulation.",
                ),
                accent="Figure 4.7: at the minimum price objective a new consolidation forms.",
                caption="The objective is a 1:1 projection of the pattern's height from the neckline breakout.",
            ),
            picture=Figure(
                number="4.7",
                shows="A 15 minute EURUSD chart with a head and shoulders boxed as a consolidation range and labelled as distribution, a breakdown through its neckline, and a new consolidation forming at the projected target below.",
            ),
            text_w=5.2,
            notes=(
                "Same pattern family, two directions: the standard one tops a market, the inverted one bottoms it.",
                "The minimum price objective is the minimum measuring objective again, measured on a pattern and not on a range.",
            ),
        ),
        Pair(
            left=Content(
                title="Figure 4.5: the reversal patterns, by phase",
                lines=(
                    "Accumulation based, in downtrends: inverted head and shoulders, cup and handles, rounding bottoms, falling wedges, ascending triangles, and double, triple and multiple bottoms.",
                    "Distribution based, in uptrends: standard head and shoulders, rounding tops, rising wedges, descending triangles, and double, triple and multiple tops.",
                ),
                accent="Bullish in a downtrend, bearish in an uptrend: bias and trend disagree.",
                caption="Both lists add broadening, island and diamond formations. V bottoms and V tops are reversals too.",
            ),
            picture=Figure(
                number="4.5",
                shows="The book's summary diagram, Phase-Based Chart Patterns: three lists, accumulation based, distribution based and continuation based, with the first two marked as reversal patterns whose intrinsic and trend sentiment disagree, and the third as patterns whose intrinsic and trend sentiment should agree.",
            ),
            text_w=6.2,
            notes=(
                "The figure is the whole section on one page. Its type is small: the two lists are written out on the left for that reason.",
                "Its third box is the continuation list, which matches the two lists already taught with the bear flag.",
            ),
        ),
        Pair(
            left=Content(
                title="Neutral patterns borrow their bias",
                lines=(
                    "A neutral formation's extrinsic bias is derived from the trend sentiment.",
                    "A symmetrical triangle is extrinsically bullish in an uptrend, bearish in a downtrend.",
                    "Broadening, diamond and island formations are reversals: their bias opposes the trend.",
                ),
                accent="A neutral pattern has no lean of its own. Its surroundings supply one.",
                caption="One list in the book files broadening formations with the trend; its next paragraph and Figure 4.5, as reversals.",
            ),
            picture=Figure(
                number="4.9",
                shows="A 15 minute EURUSD chart with a symmetrical triangle forming partway up an uptrend, prices consolidating in a convergent manner, labelled intrinsically neutral, extrinsically bullish, and as continuation.",
            ),
            text_w=5.4,
            notes=(
                "In the figure the preexisting uptrend imbues the triangle with extrinsic bullishness. Imbues is the book's word.",
                "The book contradicts itself on broadening formations: one list against one paragraph and one figure. Say so and move on.",
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
                caption="Failed patterns often lead to a more powerful reaction.",
            ),
            picture=Figure(
                number="4.11",
                shows="The daily iShares Silver Trust chart: two ascending triangles as accumulation, the second labelled intrinsically and extrinsically bullish, a gap up into the trend phase, then a new ascending triangle that breaks down unexpectedly, with volume declining into each breakout.",
            ),
            text_w=5.2,
            notes=(
                "The second triangle is bullish both ways: it forms inside the clear support the first one made.",
                "Had the third formed at a significant historical peak it would be extrinsically bearish. Volume declines as each breakout approaches.",
            ),
        ),
        Check(
            label="Reversals, neutral patterns and failure",
            questions=(
                Q(
                    stem="A symmetrical triangle forms in the middle of an uptrend. Its extrinsic bias is:",
                    options=("Bullish, taken from the uptrend",
                             "Bearish, because triangles are reversal patterns",
                             "Neutral, because the pattern is neutral",
                             "Unknown until volume confirms it"),
                    answer="A",
                    reason="A neutral pattern is extrinsically bullish in an uptrend and extrinsically bearish in a downtrend.",
                ),
                Q(
                    stem="As a general guide, for a reversal pattern the intrinsic bias and the trend sentiment are:",
                    options=("In agreement, as they are for a continuation",
                             "Both neutral",
                             "In disagreement with each other",
                             "Set by the volume inside the pattern"),
                    answer="C",
                    reason="A reversal pattern leans against the trend it ends: a bearish pattern in an uptrend, a bullish one in a downtrend.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.3 - Volume and open interest. Chapter 6 teaches the two tools.
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
                title="A trend that loses volume is running out",
                lines=(
                    "If an uptrend or downtrend is inherently weak, volume falls off during the trend phase.",
                    "That is a sign of trend exhaustion.",
                    "It signals a potentially earlier onset of a distribution or accumulation phase.",
                ),
                accent="Volume should rise through a trend. When it turns down partway, expect the consolidation sooner.",
            ),
            picture=Figure(
                number="4.16",
                shows="The same schematic cycle with volume turning down partway through each trend, the turn circled and labelled trend exhaustion.",
            ),
            text_w=5.4,
            notes=(
                "Compare with the last figure: there volume rose all the way through each trend. Here it turns early.",
                "Earlier onset is the practical point: the trend ends sooner than its start suggested.",
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
                caption="Open interest is used here and taught in Chapter 6.",
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
        Pair(
            left=Content(
                title="Volume and phase on a real chart",
                lines=(
                    "The extended distribution is violated by a downside gap, on high volume.",
                    "The trend phase follows, with bullish volume divergence, and passes into an accumulation.",
                    "Volume gradually decreases as the accumulation progresses.",
                ),
                accent="Falling volume signals a potentially imminent breakout, to the upside or the downside.",
            ),
            picture=Figure(
                number="4.18",
                shows="An intraday Isis Pharmaceuticals chart: a long distribution phase broken by a downside gap, a trend phase curving down into an accumulation phase, and a volume panel labelled bullish volume divergence under the trend and again under the accumulation.",
            ),
            text_w=5.2,
            notes=(
                "Everything from the three schematics, on one stock: high volume at the break, falling volume through the range.",
                "Bullish volume divergence is the figure's own label. Divergence is section 4.5; do not explain it yet.",
            ),
        ),
        Pair(
            left=Content(
                title="Heavy volume marks a top or a bottom",
                lines=(
                    "Higher than normal volume at the start of an accumulation or distribution strongly indicates a bottom or top has formed.",
                    "In Figure 4.19 large price-based volume coincides with the distribution and accumulation zones.",
                ),
                accent="Price levels with historically high volume are potential levels of accumulation or distribution.",
                caption="Price-based volume, as opposed to time-based volume, is used here and not explained.",
            ),
            picture=Figure(
                number="4.19",
                shows="An hourly Facebook chart with horizontal volume bars drawn against price levels: the largest coincide with a distribution zone and an accumulation zone, with order flow marked seeking out additional liquidity at the edges of each.",
            ),
            text_w=5.2,
            notes=(
                "Two uses of volume now: falling volume times the end of a consolidation, heavy volume marks where one began.",
                "The market tests the consolidation boundaries for additional liquidity: the figure marks order flow seeking it out.",
            ),
        ),
        Check(
            label="Volume and open interest",
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
                    stem="Open interest increases during a consolidation instead of decreasing. The breakout and the trend that follow tend to be:",
                    options=("Weaker and short lived",
                             "Much more rapid and extended",
                             "Delayed by several months",
                             "In the direction of the old trend"),
                    answer="B",
                    reason="When open interest rises through a consolidation, the breakout move and the subsequent trend tend to be much more rapid and extended.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.4 - Moving averages. Chapter 11 teaches the tool.
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
                title="4.4  A moving average across the phases",
                lines=(
                    "Market phase can also be identified by the behavior of moving averages.",
                    "During a trending phase a moving average shows the minimum incidence of whipsaws.",
                    "During a consolidation, whipsaw action increases significantly.",
                ),
                accent="The cause is the flattening-out effect of averages in a sideways or ranging market.",
                caption="The book uses whipsaw without defining it; Figure 4.20 points at them. Moving averages are Chapter 11.",
            ),
            picture=Figure(
                number="4.20",
                shows="One simple moving average under a rising price, labelled as containing the trend with fewer whipsaws, then flattening inside a boxed consolidation where price crosses it again and again, labelled whipsaws during the consolidation phase.",
            ),
            text_w=5.0,
            notes=(
                "In the figure the whipsaws are the places where price crosses back and forth over the flat average.",
                "That reading comes from the figure's own labels. The definition waits for Chapter 11.",
            ),
        ),
        Pair(
            left=Content(
                title="Several averages: spread in a trend, tangle in a range",
                lines=(
                    "In a trend, multiple moving average lines start to diverge from each other.",
                    "The greater the divergence, the stronger the ensuing trend.",
                    "When the lines begin to converge, that is an early indication of a potential consolidation.",
                ),
                accent="Overlapping lines: consolidation. Diverging lines: a strong trend in place.",
            ),
            picture=Figure(
                number="4.21",
                shows="A daily chart with four moving averages, 20, 50, 100 and 200 day: the lines overlap through an accumulation phase, fan apart through the trend phase, where they also act as support, and overlap again in the consolidation that follows.",
            ),
            text_w=5.2,
            notes=(
                "This is review question 6: lines fanning apart, a trend; lines converging and overlapping, a consolidation.",
                "The figure also labels the averages acting as support. The book's text does not discuss that here.",
            ),
        ),
    ),
)

# ==========================================================================
# 4.5 - Divergence and momentum. Chapter 9 teaches divergence.
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
                title="4.5  Divergence tracks momentum",
                lines=(
                    "Divergence may be used to track the changes in price momentum.",
                    "That makes it extremely useful for identifying potential consolidations, and the strength of a trend.",
                    "Once divergence is observed, look for a slowing of the trend.",
                ),
                accent="In Figure 4.22 price makes a higher peak while the MACD makes a lower one: standard bearish divergence.",
                caption="The chapter uses divergence, MACD and RSI without defining them. Divergence is Chapter 9.",
            ),
            picture=Figure(
                number="4.22",
                shows="An hourly EURUSD chart: price makes a higher peak inside a distribution while the MACD below it makes a lower one, labelled standard bearish divergence and momentum turning before price.",
            ),
            text_w=6.4,
            notes=(
                "This is review question 8: divergence shows momentum slowing, and a slowing trend is a consolidation forming.",
                "Describe the two sloping lines in the figure and stop there. What divergence is, formally, is Chapter 9.",
            ),
        ),
        Pair(
            left=Content(
                title="Bullish divergence supports an accumulation",
                lines=(
                    "The accumulation takes the form of an inverted head and shoulders pattern.",
                    "It is further supported by standard bullish divergence on the MACD.",
                    "The left shoulder, head and right shoulder coincide with the projected cycle lows.",
                ),
                accent="This bullish confluence within the accumulation greatly increases the probability of a strong upside move.",
            ),
            picture=Figure(
                number="4.23",
                shows="The daily 3M chart: an accumulation in the form of an inverted head and shoulders, with standard bullish divergence marked on the MACD below it and vertical lines marking consistent cycle lows at the shoulders and the head.",
            ),
            text_w=5.6,
            notes=(
                "Three kinds of evidence agree here: the pattern, the divergence and the cycle. Confluence is the book's word for that.",
                "The figure also labels a reverse bullish and a standard bearish divergence. The text discusses neither.",
            ),
        ),
        Pair(
            left=Content(
                title="Momentum turns before price",
                lines=(
                    "Volume, MACD and RSI all show bullish divergence with price in the accumulation.",
                    "The MACD and the RSI are both momentum-based indicators.",
                    "At the tail end of a trend, a sign that a consolidation may be forming helps a trader anticipate an early entry.",
                ),
                accent="We see momentum turning before price.",
                caption="For bullish divergence in volume, falling prices must be accompanied by decreasing volume.",
            ),
            picture=Figure(
                number="4.24",
                shows="A 5 minute GBPUSD chart: a downtrend into an accumulation, with bullish divergence marked on volume, on the MACD and on the RSI inside the accumulation, and a new trend rising out of it.",
            ),
            text_w=5.2,
            notes=(
                "Price is still falling in the box while both indicators are already rising. That is momentum turning first.",
                "The volume rule is the one sentence of method the book gives. It is on the slide as the book states it.",
            ),
        ),
        Check(
            label="Moving averages and divergence",
            questions=(
                Q(
                    stem="Several moving average lines that had spread apart begin to converge. This is an early indication of:",
                    options=("A potential consolidation",
                             "A stronger trend",
                             "A selling climax",
                             "A minimum measuring objective"),
                    answer="A",
                    reason="Diverging lines mean a trend. Converging lines are an early indication of a potential consolidation.",
                ),
                Q(
                    stem="At the tail end of a trend, a momentum indicator turns before price does. This is an early sign that:",
                    options=("The trend is strengthening",
                             "Volume is about to surge",
                             "The pattern is intrinsically neutral",
                             "A consolidation may be forming"),
                    answer="D",
                    reason="Momentum turning before price shows the trend slowing, which is how a consolidation begins.",
                ),
            ),
        ),
    ),
)

# ==========================================================================
# 4.6 - Sentiment. Chapter 23 teaches the indicators.
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
                    "Participants swing between fear, greed and hope, responding to news and each other.",
                    "Identifiable patterns repeat fairly consistently, especially at market extremes.",
                    "Sentiment indicators track participants' aggregate sentiment, emotions and psychology.",
                ),
                accent="They are most accurate at extremes of optimism or pessimism.",
            ),
            picture=Chart(
                letter="Q",
                shows="One market swing with its top and its bottom boxed: at the top the crowd is extremely bullish, at the bottom extremely bearish, and those two extremes are where sentiment indicators are most accurate.",
            ),
            text_w=CHART_W,
            notes=(
                "Tie it to 4.1: the uninformed were extremely bullish at distribution and extremely bearish at accumulation.",
                "Sentiment indicators measure that crowd. So they read best exactly where the crowd is most one sided.",
            ),
        ),
        Content(
            title="Thirteen sentiment indicators, by name",
            lines=(
                "Put-call ratios, Arm's Index, and odd lot sales.",
                "Margin debt, the COT report, and the VIX.",
                "The short interest ratio, the cash asset ratio, and the advance-decline line.",
                "New highs minus new lows, up volume minus down volume, Market Vane reports, and the Bullish Sentiment Index.",
            ),
            accent="The book gives these as examples and explains none of them here.",
            caption="Chapter 23 is the detailed discussion. How any one of them is built is not examined from this chapter.",
            notes=(
                "Names only. Do not explain what any of them measures: the book does not, until Chapter 23.",
                "Six of the thirteen come back on the next slide, with what each reads at a top and at a bottom.",
            ),
        ),
        Pair(
            left=Content(
                title="What the indicators read at a top and a bottom",
                lines=(
                    "At distribution the put/call ratio and the VIX are low, but starting to increase.",
                    "A/D, margin debt, new highs minus new lows and the Bullish Percent Index are high, but starting to decrease.",
                    "At accumulation every one of those readings is reversed.",
                ),
                accent="Each reading is at an extreme and has just started to turn.",
                caption="The figure says Bullish Percent Index, the list Bullish Sentiment Index. The book does not say if they are the same.",
            ),
            picture=Figure(
                number="4.25",
                shows="A price curve from a distribution at the top to an accumulation at the bottom, with six sentiment readings listed beside each: put/call ratio, A/D, VIX, margin debt, new highs minus new lows and the Bullish Percent Index.",
            ),
            text_w=5.8,
            notes=(
                "This is review question 5: which sentiment indicators best describe distributions? Read the top list in the figure.",
                "Two start low at a top, four start high. At a bottom, swap the words high and low.",
            ),
        ),
        Check(
            label="Sentiment",
            questions=(
                Q(
                    stem="Sentiment indicators are most accurate:",
                    options=("In the middle of a trend phase",
                             "At market extremes",
                             "On sub-hourly charts",
                             "When volume is at its lowest"),
                    answer="B",
                    reason="It is at market extremes that they best reflect the underlying mood of optimism or pessimism.",
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
# 4.7 - Sakata's interpretation of market phase.
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
                "The left panel is Sakata, the right is Elliott. The book says the two are very similar in appearance.",
                "Honma's name is all the history the book gives. Do not add to it.",
            ),
        ),
        Pair(
            left=Content(
                title="The five methods, by name",
                lines=(
                    "San Zan, three mountains: the Western triple top. The distribution phase.",
                    "San Sen, three rivers: the Western triple bottom. The accumulation phase.",
                    "San Ku, three gaps: the breakaway, runaway and exhaustion gaps of the trend.",
                    "San Pei, three thrusts: the three trending phases between the two.",
                    "San Poh, three methods: the three corrections, one after each thrust.",
                ),
            ),
            picture=Chart(
                letter="R",
                shows="Sakata's five methods on one invented line, each with the book's English: San Sen the triple bottom, San Pei the three thrusts, San Poh the corrections after them, San Ku the three gaps, and San Zan the triple top.",
            ),
            text_w=CHART_W,
            notes=(
                "The book glosses every name as three of something. That is the handle for remembering all five.",
                "Two of the five are consolidations and three describe the trend between them. Chapter 3 named the same three gaps.",
            ),
        ),
        Pair(
            left=Content(
                title="Five phases inside three",
                lines=(
                    "Dow's three phases may seem inconsistent with Sakata's five, and with Elliott's waves.",
                    "Simple chart patterns show the models need not be viewed as distinct.",
                    "A triple bottom, thrusts with bullish flags and gaps between them, then a triple top.",
                ),
                accent="A plausible resolution between Eastern and Western approaches.",
            ),
            picture=Figure(
                number="4.27",
                shows="Dow's three-phase market drawn with Sakata's pieces: a triple bottom as the accumulation phase, a rising channel of thrusts, bullish flags and the breakaway, runaway and exhaustion gaps as the trend phase, and a triple top as the distribution phase.",
            ),
            text_w=5.4,
            notes=(
                "This is the chapter objective on comparing Eastern and Western approaches. The answer is that one fits inside the other.",
                "The summary calls the two approaches complementary. That is the word to leave them with.",
            ),
        ),
        Check(
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
# 4.8 - Elliott. Chapter 18 teaches the waves.
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
                    "Elliott described markets as an impulsive five-wave up, then a corrective three-wave down.",
                    "The trending phase is impulse waves 1, 3 and 5.",
                    "The accumulation phase is corrective waves 2 and 4. Distribution is usually the abc correction.",
                ),
                accent="Sakata's San Pei closely resembles waves 1, 3 and 5. San Poh somewhat resembles waves a, b and c.",
                caption="The book also places the abc correction under accumulation, 'in most cases'. Elliott's waves have specific rules; Sakata's model is less rigid.",
            ),
            picture=Figure(
                number="4.28",
                shows="Elliott's wave structure: five numbered motive waves rising, with waves 1, 3 and 5 marked impulsive, then three lettered corrective waves a, b and c falling. Eight waves of one degree.",
            ),
            text_w=5.8,
            notes=(
                "The book gives the abc correction to accumulation in most cases and to distribution usually, in consecutive sentences. Say so; do not pick one.",
                "Nothing on the abc correction is examined from this chapter. Waves 1, 3 and 5 as the trend is.",
            ),
        ),
        Pair(
            left=Content(
                title="Elliott's waves on the gold chart",
                lines=(
                    "Primary waves 1 and 2 sit in the accumulation, the powerful wave 3 in the trend.",
                    "Volume gradually decreases over each significant consolidation.",
                    "Volume peaks around the top of wave 5, within a new area of consolidation.",
                ),
                accent="Fibonacci price and time projections help gauge where each wave ends.",
                caption="Fibonacci projection is not taught here. Elliott waves: Chapter 18.",
            ),
            picture=Figure(
                number="4.29",
                shows="The weekly gold chart from 2000 to 2012 with an Elliott wave count on log scaling: an accumulation phase, two trend phases with a consolidation between them, a potential distribution phase at the top, and volume marked falling across three consolidations.",
            ),
            text_w=5.2,
            notes=(
                "The volume panel is section 4.3 again: it falls through each consolidation, at the points numbered 1, 2 and 3.",
                "The book describes the new consolidation at the top as an inverted head and shoulders. Read it as the book states it.",
            ),
        ),
    ),
)

# ==========================================================================
# 4.9 - Cycle analysis. Chapter 20 teaches cycles.
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
                    "Whether a formation reverses or continues depends on where in the cycle it unfolds.",
                    "Between cycle extremes, formations tend to be continuations.",
                    "At cycle peaks they tend to be distributions. At cycle troughs, accumulations.",
                ),
                accent="If the intrinsic and extrinsic biases agree as well, it is potentially more reliable.",
                caption="For formations on the same cycle degree. Finding the cycle period is Chapter 20.",
            ),
            picture=Figure(
                number="4.30",
                shows="A price cycle with four formations boxed on it: a reversal as accumulation at each cycle trough, a continuation between the extremes, and a reversal as distribution at the cycle peak.",
            ),
            text_w=5.6,
            notes=(
                "This is review question 7, and it is extrinsic bias again: the phase of the cycle was one of the five factors.",
                "Once a cycle period is identified, the book says, placing the formation on it is fairly simple.",
            ),
        ),
        Pair(
            left=Content(
                title="One triangle, three roles",
                lines=(
                    "The intrinsically neutral symmetrical triangle takes three distinct roles.",
                    "Accumulation at the bottom of the cycle, continuation between the top and the bottom, distribution at the top.",
                    "It adopts a bullish extrinsic bias at cycle troughs, and a bearish one at cycle peaks.",
                ),
                accent="Between the extremes it adopts the preexisting trend sentiment.",
            ),
            picture=Figure(
                number="4.31",
                shows="A price cycle with the same symmetrical triangle drawn at four places: as accumulation at each cycle trough, as continuation between the extremes, and as distribution at the cycle peak.",
            ),
            text_w=5.4,
            notes=(
                "The same shape four times in the figure, three different names. Only the place on the cycle differs.",
                "Neutral patterns borrow their bias: here the lender is the cycle and not the trend.",
            ),
        ),
        Pair(
            left=Content(
                title="The same in a price channel",
                lines=(
                    "In a rising channel the triangle is accumulation at the bottom, continuation in the middle, distribution at the top.",
                    "Had the pattern been an inverted head and shoulders, a reversal at the bottom or a continuation in the middle would be more probable.",
                ),
                accent="Confluences with other overlay barriers, such as Fibonacci levels, give more reliable forecasts of where price may react.",
            ),
            picture=Figure(
                number="4.32",
                shows="An uptrending price channel with the symmetrical triangle drawn as accumulation at the bottom of the channel, as continuation in the middle, and as distribution at the top, headed look for supportive and resistive confluences.",
            ),
            text_w=5.4,
            notes=(
                "The inverted head and shoulders is intrinsically bullish, so at the channel bottom both biases would agree.",
                "Confluence again: more than one barrier at the same price. Fibonacci levels are named, and not taught, here.",
            ),
        ),
        Check(
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
            "4.1  Dow: the phases, who is on each side, and when a consolidation is over.",
            "4.2  Chart patterns: which pattern belongs to which phase, and why.",
            "4.3 to 4.6  Volume, moving averages, divergence and sentiment.",
            "4.7  Sakata: the Japanese five phase model.",
            "4.8 and 4.9  Elliott waves and cycles.",
        ),
        accent="One question runs through all nine: which phase is the market in?",
        notes=(
            "The parts are the book's own sections. The marker at the bottom left of every slide says which one we are in.",
            "Say the checks carry no marks. Each question slide is followed by its answers on a slide of their own.",
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
        title="What this chapter uses and does not teach",
        lines=(
            "The shapes of the chart patterns: Chapter 13. Open interest: Chapter 6.",
            "Moving averages and whipsaws: Chapter 11. Divergence, MACD and RSI: Chapter 9.",
            "The thirteen sentiment indicators: Chapter 23. Elliott's rules: Chapter 18. Cycles: Chapter 20.",
            "The objectives promise inertial characteristics; the text never uses the word.",
        ),
        accent="From this chapter, only what each tool says about market phase is examinable.",
        caption="Do not fill these from outside the book. Each comes back in its own chapter.",
        notes=(
            "Be straight with them: six of the nine sections borrow tools the book has not taught yet.",
            "Price based volume and Fibonacci projections are also used and not explained. Same answer: later chapters.",
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
        "Say every idea today has a picture beside it. Where the book drew one it is the book's; the rest are ours.",
    ),
    dividers=False,
)
