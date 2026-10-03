"""FIN1209 Chapter 4 student lecture notes, as plain data.

This is the file a contributor edits. Layout lives in build/lecturekit.py and
knows nothing about any chapter; the reasoning behind the layout, with the
research it came from, is chapter-01/lecture-notes-design.md.

    .venv/bin/python build/build_lecture_notes4.py

Written for a student reading alone, with no instructor in the room. Full
sentences that explain, not bullets that gesture. The nine sections are the
deck's nine parts in the deck's order, which are the book's own sections 4.1
to 4.9, so a student can move between the slides, the book and these pages.

Nothing here is timing, cuts, speaker cues, check answers or slide numbers.
Those belong to the instructor: the timing and the cuts are in
build/plan_chapter04.py, and the check answers are not in this repository at
all.

**Every picture the deck places is placed here too**, all 32 of the book's
figures and all 18 of our own charts, and build_lecture_notes4.py fails if
one is missing. The deck was sent back once for teaching less than the book
does, and the notes are held to the same rule.

Figure descriptions are never retyped here. The build takes them from
content_chapter04.py, which is also where the deck's own placeholder takes
them, so the two documents cannot describe the same figure differently.

The definitions are not retyped either. Every Define block below takes its
wording from the deck's own term slide through ``formal()``, so a term is
defined in the same words in both documents by construction. The plain words
and the example belong in the paragraphs around it. The learning objectives
are read from the deck the same way.

Bold covers whole sentences, never a phrase inside one: the paginator moves
a bold element whole, so a bold phrase lets a page break fall inside its
sentence. AGENTS.md has the history.
"""

from __future__ import annotations

import re

import deckkit
from content_chapter04 import CHAPTER
from lecturekit import (Define, Fig, Head, LectureNotes, Panel, Para, Points,
                        Section, SelfCheck)


def term_name(slide: deckkit.Term) -> str:
    """The term a slide teaches, without the book's section number.

    The lean deck has no divider slides, so the first slide of a part carries
    the book's section number in its title. Where that slide is a term slide
    the number is on the term: "4.7  Sakata's Five Methods". It is not part
    of the term, and the notes and their index do not print it.
    """
    return re.sub(r"^\d+\.\d+\s+", "", slide.term)


def _term_slides():
    for part in CHAPTER.sections:
        for slide in part.slides:
            if isinstance(slide, deckkit.Pair):
                slide = slide.left
            if isinstance(slide, deckkit.Term):
                yield slide


_FORMAL = {term_name(slide): slide.formal for slide in _term_slides()}


def formal(term: str) -> Define:
    """The deck's own formal definition of ``term``, as a Define block."""
    return Define(term=term, text=_FORMAL[term])


def figure(number: str, caption: str, height_mm: float = 60.0) -> Fig:
    """One of the book's figures, alone on the measure."""
    return Fig(panels=(Panel(number=number),), cols=1, height_mm=height_mm,
               caption=caption)


def chart(letter: str, caption: str, height_mm: float = 76.0) -> Fig:
    """One of our own charts.

    They are drawn for the slide's picture column, at about 150mm wide with
    10 point labels. On this page the height sets the width, and at 76mm a
    chart is about 110mm wide and its labels are a little over 7 point.
    Shorter than that and the labels cannot be read in print.
    """
    return Fig(panels=(Panel(number=letter),), kind="chart",
               height_mm=height_mm, caption=caption)


# ==========================================================================
# Section 1 - Dow theory of market phase (the book's 4.1)
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Dow Theory of Market Phase",
    standfirst="The two basic phases and the two kinds of consolidation, "
               "why the kind is known only afterwards, who buys and who "
               "sells in each phase, the signs of each consolidation, and "
               "when a consolidation is over. This is the book's section "
               "4.1.",
    blocks=(
        Head(number="1.1", text="Markets move in phases"),
        Para(text=(
            "Chapter 2 gave Dow Theory's tenet that a primary trend has "
            "three phases: accumulation, trending and distribution. That "
            "description is now regarded as the basic underlying "
            "characteristic of market action, and this chapter is about "
            "nothing else. Phase analysis applies across all time frames. "
            "**The book puts the stakes plainly: not recognizing the phases "
            "and their transitions greatly disadvantages the practitioner.**"
            "\n\n"
            "One question runs through all nine sections: which phase is "
            "the market in? Each section answers it with a different kind "
            "of evidence."
        )),
        chart("A", "One price line through the phases, in order."),
        Para(text=(
            "Chart A draws the whole idea on one invented price line: an "
            "accumulation, the trend up out of it, a distribution, and the "
            "trend down out of that. Read it from left to right and name "
            "each stretch before you read its label."
            "\n\n"
            "Three phases, but only two kinds. Either the market is going "
            "somewhere or it is not, and the sideways stretch is the one "
            "that needs a definition. Picture a share that swings between "
            "40 and 44 pesos for four months and goes nowhere. It is "
            "consolidating: price ranges, or makes small corrective moves, "
            "instead of trending."
        )),
        formal("Consolidation phase"),
        Para(text=(
            "The book's first review question asks for that definition, and "
            "the book never sets one apart in a single place. **The wording "
            "above joins two of the book's own sentences: the one in its "
            "section 4.1 that there are only two basic phases, and the one "
            "in its section 4.2 on how a market consolidates.**"
        )),
        figure("4.1", "The phases as a tree.", height_mm=46.0),
        Para(text=(
            "Figure 4.1 is the same statement drawn as a tree. Read it from "
            "the top down: market phase splits into consolidation and "
            "trend, and consolidation splits again into accumulation and "
            "distribution."
        )),

        Head(number="1.2", text="Accumulation or distribution is known only "
                                "afterwards"),
        Para(text=(
            "If the market rises after consolidating, the consolidation was "
            "accumulation, which is buying activity. If it declines after "
            "consolidating, it was distribution, which is selling activity. "
            "**Which one it is can only be ascertained after the fact.**"
            "\n\n"
            "While the range is forming, the two look alike. That is why "
            "the book makes it one objective of technical analysis to look "
            "for evidence of which is taking place. The rest of the chapter "
            "is that hunt: volume, chart patterns, moving averages, "
            "momentum, sentiment and cycles."
        )),
        chart("B", "One consolidation, two outcomes."),
        Para(text=(
            "Chart B shows one consolidation with two dashed paths leaving "
            "it. Cover the two paths with your hand. The range is the same "
            "either way, and the name it earns depends on the move that "
            "comes next."
        )),

        Head(number="1.3", text="The first evidence: volume in a "
                                "consolidation"),
        Para(text=(
            "Volume normally declines gradually during a consolidation. "
            "Very low volume is a strong sign that the consolidation may be "
            "ending and a trend starting. On a daily chart a consolidation "
            "normally lasts about three to six months, or longer."
        )),
        figure("4.2", "The phases, and their volume, on the daily Dow.",
               height_mm=64.0),
        Para(text=(
            "Figure 4.2 is the daily Dow Jones Industrial Average with its "
            "accumulation, trending and distribution phases boxed and "
            "named. Look under each box, in the volume panel, where the "
            "decline in volume through that consolidation is drawn in. Then "
            "look at the last box, at the top right. **It is labelled only "
            "consolidation, because what followed it was not yet known.**"
        )),

        Head(number="1.4", text="The same phases at every time scale"),
        Para(text=(
            "A primary trend typically spans months to years in the equity "
            "markets. In commodity futures it tends to be shorter, because "
            "high leverage induces greater volatility. Dow described the "
            "equity markets, but the phases are found across all markets. "
            "They show on sub-hourly charts too. The book calls that micro "
            "phase action, and says it is shaped by the macro phase "
            "behavior around it."
        )),
        figure("4.3", "Micro phase action on a 15 minute chart.",
               height_mm=56.0),
        Para(text=(
            "Figure 4.3 is a 15 minute EURUSD chart, and it has a "
            "distribution, a trend and an accumulation boxed one after "
            "another, just as the daily chart of the Dow did. Looking at "
            "more than one time frame is how to see both at once: the macro "
            "phase first, then the micro phases inside it."
        )),
        SelfCheck(text=(
            "A share has ranged between 40 and 44 pesos for four months. "
            "Can you say today whether that is accumulation or "
            "distribution? What would you look for while you wait?"
        )),

        Head(number="1.5", text="Who buys and who sells in each phase"),
        Para(text=(
            "An accumulation normally follows a deep and rapid decline, on "
            "very negative data and bearish headlines. The uninformed are "
            "extremely bearish and sell at whatever price is available. The "
            "informed buy from them, which is a contrarian approach and "
            "needs deep pockets. They gather shares very gradually, careful "
            "not to drive prices up too fast. **The sell-off that ends the "
            "downtrend is called a selling climax.** The book describes the "
            "informed buying into it as very large responsive buying, and "
            "that buying is what creates the final and decisive bottom."
        )),
        chart("C", "Accumulation: the selling climax, and after."),
        Para(text=(
            "Chart C draws it: a deep, rapid decline ends in a selling "
            "climax, where the uninformed sell and the informed buy, and a "
            "long accumulation range follows through which the informed "
            "keep gathering shares."
            "\n\n"
            "The uptrend that follows feeds on itself. Technical traders "
            "get in early, on a clear upside breakout, and market savvy "
            "investors follow. As the uptrend becomes obvious the public is "
            "drawn in, and the bears cover their shorts. Then comes regret "
            "bias: those who missed out, or sold too early, buy at every "
            "dip. At even higher prices the herd uses more margin, even "
            "borrowing to invest. **The book calls this a vicious positive "
            "feedback cycle.**"
        )),
        chart("D", "The uptrend: who joins, in the order they join."),
        Para(text=(
            "Chart D marks the five groups in the order they arrive, "
            "numbered 1 to 5. Each group arrives later, and at a higher "
            "price, than the one before it."
            "\n\n"
            "The downtrend is the same cycle running downward. It begins "
            "with a breakdown from a distribution range, on increasingly "
            "bearish data. The uninformed begin to unload, and previously "
            "bullish participants liquidate. Past the threshold of pain and "
            "the margin limits, capital flows out of the market. Bearish "
            "sentiment intensifies as prices sink. Further unexpected "
            "declines attract more public attention, and that causes the "
            "larger liquidation."
        )),
        chart("E", "The downtrend: the same feedback, downward."),
        Para(text=(
            "Chart E is Chart D turned over, marked in order: the "
            "breakdown, the uninformed beginning to unload, bullish holders "
            "liquidating, and capital flowing out once margin limits are "
            "passed."
            "\n\n"
            "A distribution is the accumulation story upside down. It "
            "normally follows a strong and rapid rise, on very positive "
            "data and the most bullish headlines. The uninformed buy at "
            "whatever price is available, a state normally referred to as "
            "irrational exuberance, and margin debt is skyrocketing. The "
            "informed sell "
            "to them very gradually, careful not to drive prices down too "
            "rapidly. **The surge that ends the uptrend is called a "
            "blow-off, or buying climax.**"
        )),
        chart("F", "Distribution: the blow-off, and after."),
        Para(text=(
            "Chart F is the mirror of Chart C. A strong, rapid rise ends in "
            "a blow-off, where the uninformed buy and the informed sell, "
            "and a distribution range follows through which the informed "
            "keep selling. You should be able to write the accumulation "
            "paragraph from the distribution one, line by line, and the "
            "other way round."
        )),

        Head(number="1.6", text="Why tops are shorter and rougher than "
                                "bottoms"),
        Para(text=(
            "The book makes three comparisons. Accumulation normally lasts "
            "longer than distribution. The uptrend tends to be more "
            "prolonged than the downtrend. Distributions tend to be much "
            "more volatile than accumulations. **One reason covers all "
            "three: at higher prices more capital, and more unrealized "
            "profit, is at risk.** At the bottom, lower prices mean a lower "
            "amount of capital at risk, so nobody is in a hurry. At the top "
            "everyone has profit to protect."
        )),
        chart("G", "The three comparisons on one cycle."),
        Para(text=(
            "Chart G draws one cycle to those three comparisons: a long, "
            "quiet accumulation, a prolonged uptrend, a short and volatile "
            "distribution, and a short downtrend."
        )),

        Head(number="1.7", text="The signs of each consolidation"),
        Para(text=(
            "The label is known only afterwards, but the book lists what to "
            "look for while a consolidation is still forming. The two lists "
            "mirror each other, and the second adds one item: signs of "
            "exhaustion."
        )),
        Points(
            title="The signs of an accumulation",
            items=(
                "It comes after a relatively rapid decline, ideally near a "
                "significant prior bottom.",
                "There is no evidence of lower troughs being formed.",
                "Volume begins to subside as a potential upside breakout "
                "approaches.",
                "The longer it lasts, the more powerful the breakout, "
                "typically on a surge in volume.",
                "It starts a new primary bull market, or a shorter-term "
                "uptrend.",
            ),
        ),
        chart("H", "The signs of an accumulation, over volume."),
        Points(
            title="The signs of a distribution",
            items=(
                "It comes after a prolonged uptrend, ideally near a "
                "significant prior top.",
                "Signs of market exhaustion show, and no higher peaks form.",
                "Volume begins to subside as a potential downside breakout "
                "approaches.",
                "The longer it lasts, the more powerful the breakout, "
                "typically on a surge in volume.",
                "It starts a new primary bear market, or a shorter-term "
                "downtrend.",
            ),
        ),
        chart("I", "The signs of a distribution, over volume."),
        Para(text=(
            "Chart H draws the first list: an accumulation after a rapid "
            "decline, sitting on the level of a significant prior bottom "
            "with no lower troughs, over a volume panel that subsides "
            "through the range and surges on the breakout. Chart I is its "
            "mirror, under the level of a significant prior top with no "
            "higher peaks."
            "\n\n"
            "The first list is the answer to the review question that asks "
            "how you would determine if accumulation is taking place. "
            "**Treat both lists as evidence and not as proof.** The book "
            "says the breakout can be to either side of the range."
        )),

        Head(number="1.8", text="When is a consolidation over?"),
        Para(text=(
            "There is no absolute consensus on the exact point where a "
            "consolidation ends. Some practitioners look for a 3 to 5 "
            "percent rise above the highest peak of the range. Some wait "
            "for the minimum measuring objective to be met. **Most look for "
            "a clear and simple technical breakout from the range.** Even "
            "then, where the breakout occurs depends on the price filter "
            "used. Once a consolidation is complete, the book adds, it "
            "follows logically that a trend may already be in effect."
        )),
        figure("4.4", "Three popular completion levels.", height_mm=58.0),
        Para(text=(
            "Figure 4.4 marks the three levels above one consolidation "
            "range: a technical breakout, a 3 to 5 percent rise above the "
            "highest peak, and a one to one minimum target projection of "
            "the range. That last label is the minimum measuring objective "
            "under another name."
            "\n\n"
            "The minimum measuring objective is the least a breakout is "
            "expected to travel, and it is usually the height of the range "
            "it broke out of. Take the share that ranges between 40 and 44 "
            "pesos. The range is 4 pesos high, so on an upside breakout the "
            "minimum target is 44 + 4 = 48 pesos."
        )),
        formal("Minimum measuring objective"),
        chart("J", "The three completion levels, in pesos."),
        Para(text=(
            "Chart J puts all three levels on that same range, in pesos: "
            "the breakout at 44, the band 3 to 5 percent above the peak at "
            "45.32 to 46.20, and the minimum measuring objective at 48."
        )),
        SelfCheck(text=(
            "A share ranges between 30 and 35 pesos and then breaks out "
            "upward. Work out its minimum measuring objective, and the "
            "band that is 3 to 5 percent above the highest peak."
        )),
    ),
)


# ==========================================================================
# Section 2 - Chart pattern interpretation (the book's 4.2)
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Chart Pattern Interpretation of Market Phase",
    standfirst="Reversal and continuation patterns, what makes a pattern a "
               "consolidation pattern, the bias a pattern carries in itself "
               "and the bias it takes from where it sits, and why agreement "
               "between the two is what to look for. This is the book's "
               "section 4.2.",
    blocks=(
        Head(number="2.1", text="Chart patterns show the phase"),
        Para(text=(
            "Market phase can also be identified by the type of chart "
            "pattern found at each stage. Most chart patterns belong to one "
            "of two groups, reversal or continuation. Accumulation and "
            "distribution tend to hold reversal patterns, and continuation "
            "patterns form within the trend. **So the kind of pattern on "
            "the chart is evidence of the phase the market is in.**"
        )),
        chart("K", "Which kind of pattern sits in which phase."),
        Para(text=(
            "Chart K boxes three patterns on one price line: a reversal "
            "pattern at the bottom as accumulation, a continuation pattern "
            "inside the trend, and a reversal pattern at the top as "
            "distribution. Reversal and continuation are the two words to "
            "hold on to, because every pattern in this section is filed "
            "under one of them."
        )),

        Head(number="2.2", text="Consolidation patterns, and the one "
                                "exception"),
        Para(text=(
            "A pattern that stays inside a range and is not trending "
            "anywhere is a consolidation pattern. A share that drifts "
            "between 40 and 44 pesos for six weeks while a triangle forms "
            "is making one. The book's wording sets two tests, and both "
            "are needed: a confined range, and no significant trend "
            "component."
        )),
        formal("Consolidation pattern"),
        chart("L", "A consolidation pattern, beside a V bottom."),
        Para(text=(
            "Chart L holds the two tests against two shapes. On the left a "
            "pattern is boxed inside a confined range with no trend "
            "component. On the right is a V bottom, which has no confined "
            "range and a strong trend component, and so fails both."
            "\n\n"
            "A market that is expressing indecision, rest or exhaustion "
            "ranges, or makes relatively small corrective moves. **That is "
            "why most reversal and continuation patterns are also "
            "consolidation patterns, and it is the answer to the review "
            "question that asks why.** V tops and V bottoms are the "
            "exception. They are the hardest reversals to forecast, seen "
            "only in hindsight, and they occur more often during "
            "distributions than accumulations."
        )),
        figure("4.8", "A head and shoulders top, and a V bottom."),
        Para(text=(
            "Figure 4.8, a 4 hour USDCAD chart, has one of each. A head and "
            "shoulders forms the distribution and is labelled intrinsically "
            "bearish, a word the next subsection defines. The decline that "
            "follows ends in a sharp V bottom, labelled a rapid "
            "accumulation phase: an accumulation with no range to watch it "
            "forming in. A new consolidation follows the rise."
        )),

        Head(number="2.3", text="Intrinsic bias, and the book's three lists"),
        Para(text=(
            "Some patterns lean one way in themselves, wherever they "
            "appear. An ascending triangle is intrinsically bullish: "
            "wherever it occurs, it is inherently a bullish indication."
        )),
        formal("Intrinsic bias"),
        figure("4.6", "An intrinsically bullish reversal pattern."),
        Para(text=(
            "Figure 4.6 shows an inverted head and shoulders boxed at the "
            "bottom of a decline on a EURUSD chart, labelled an "
            "intrinsically bullish pattern and a reversal pattern. It is "
            "the accumulation, and the trend phase kicks in after the "
            "upside breakout. The book points out that this chart cannot "
            "tell us the pattern's extrinsic bias, the subject of 2.4, "
            "because it shows no price history, cycle or barrier."
        )),
        Points(
            title="Intrinsically bullish: the book's eight",
            items=(
                "Bullish pennants.",
                "Bullish flags.",
                "Ascending triangles.",
                "Inverted head and shoulders.",
                "Rounding bottoms.",
                "Cup and handles.",
                "Falling wedges.",
                "Double, triple and multiple bottoms.",
            ),
        ),
        chart("M", "The eight intrinsically bullish patterns, sketched.",
              height_mm=82.0),
        Para(text=(
            "The second review question asks for those eight, so learn "
            "them as a list. Wherever one of them forms, it is inherently "
            "a bullish indication. Chart M sketches all eight. Pairs help: "
            "the pennant and the flag, which both follow a pole, the two "
            "rounded ones, and the triangle and the wedge."
        )),
        Points(
            title="Intrinsically bearish: the book's seven",
            items=(
                "Bearish pennants.",
                "Bearish flags.",
                "Descending triangles.",
                "Standard head and shoulders.",
                "Rounding tops.",
                "Rising wedges.",
                "Double, triple and multiple tops.",
            ),
        ),
        chart("N", "The seven intrinsically bearish patterns, sketched.",
              height_mm=82.0),
        Para(text=(
            "Each is a bullish pattern turned upside down, as Chart N "
            "shows. There are seven and not eight because the cup and "
            "handle is on the bullish list and has no twin on this one. "
            "Take care with the wedges, which are easy to get backwards: a "
            "falling wedge is bullish, and a rising wedge is bearish."
            "\n\n"
            "The third list is the neutral one. Symmetrical triangles and "
            "horizontal channels have no obvious bias in sentiment. Some "
            "authors classify them as continuation patterns, others as "
            "reversal patterns. Broadening, diamond and island formations "
            "are also neutral, but are regarded as reversal formations. "
            "**Whether a neutral pattern reverses or continues is decided "
            "beyond the pattern itself.**"
        )),
        chart("O", "Four of the five neutral patterns, sketched.",
              height_mm=70.0),
        Para(text=(
            "Chart O sketches a symmetrical triangle and a horizontal "
            "channel, the two intrinsically neutral patterns, and a "
            "broadening formation and an island formation, which are "
            "neutral but regarded as reversals."
            "\n\n"
            "**An honest note about the three sketches: the chapter names "
            "these seventeen patterns and describes no shape in words.** "
            "It shows seven of them on real charts, in Figures 4.6 to "
            "4.14, and the book teaches the shapes in its Chapter 13. The "
            "sketches are drawn from Chapter 13's own one line "
            "descriptions, as a preview, and from nothing outside the "
            "book. What this chapter asks of you is the lists, not the "
            "drawings. Diamond formations are named with the others and "
            "have no sketch, because the book gives no description to draw "
            "one from."
        )),

        Head(number="2.4", text="Extrinsic bias"),
        Para(text=(
            "A pattern also takes a lean from where it sits, and not from "
            "its shape."
        )),
        formal("Extrinsic bias"),
        Para(text=(
            "The book's own worked example uses one shape in three places. "
            "An ascending triangle at the price level of a historically "
            "significant market bottom is intrinsically and extrinsically "
            "bullish, so the tendency for a reversal is greater. In the "
            "middle of an uptrend, a continuation is likelier. **At the "
            "price level of a historically significant market top the same "
            "triangle is extrinsically bearish, because it sits at a "
            "significant resistance.** The shape never changes and is "
            "bullish throughout. Only the location does."
        )),
        chart("P", "One ascending triangle in three locations."),
        Para(text=(
            "Chart P draws that example: the same ascending triangle at a "
            "historically significant bottom, in the middle of an uptrend, "
            "and at a historically significant top."
        )),
        Points(
            title="What sets the extrinsic bias",
            numbered=True,
            items=(
                "The direction of the preceding trend.",
                "Location with respect to historical extremes in price.",
                "Location with respect to the phase of an underlying market "
                "cycle.",
                "Location with respect to other supportive and resistive "
                "overlay barriers.",
                "Bullish or bearish divergent formations.",
            ),
        ),
        figure("4.12", "A neutral triangle made extrinsically bullish.",
               height_mm=58.0),
        Para(text=(
            "All five factors are outside the pattern. Figure 4.12, the "
            "daily gold chart, shows the second and the fourth at work on "
            "a neutral pattern. A symmetrical triangle forms on a strong "
            "accumulation zone that multiple bottoms have tested, beside a "
            "downtrend line acting as support, and so it is labelled "
            "extrinsically bullish. The trend phase follows after a short "
            "return move to the triangle's breakout barrier. The whole of "
            "it sits inside a larger consolidation that contains smaller "
            "distributions and accumulations. Divergence and cycles, the "
            "fifth and third factors, come back in Sections 5 and 9."
        )),

        Head(number="2.5", text="When the biases agree"),
        Para(text=(
            "Three rules of thumb follow, and the book's instruction for "
            "judging the reliability of a reversal or a continuation is to "
            "look for agreement. When intrinsic and extrinsic bias agree, "
            "a reversal at a top or bottom is more reliable. When the "
            "intrinsic bias agrees with the trend sentiment, a "
            "continuation is more likely. **Any disagreement means the "
            "reversal or continuation may be inherently weak.** Trend "
            "sentiment is the book's name for the direction of the trend, "
            "and it is used from here on."
            "\n\n"
            "A continuation pattern's bias should therefore agree with the "
            "trend sentiment. Bullish with respect to an uptrend, the book "
            "lists bullish pennants and flags, ascending triangles, "
            "inverted head and shoulders, rounding bottoms, cup and "
            "handles and falling wedges. Bearish with respect to a "
            "downtrend, it lists bearish pennants and flags, descending "
            "triangles, standard head and shoulders and rising wedges."
        )),
        figure("4.10", "A bear flag as continuation in a downtrend."),
        Para(text=(
            "Figure 4.10 is a bear flag on a 15 minute EURUSD chart. After "
            "a distribution and a downside breakout, prices consolidate in "
            "a diagonally constrained manner, and the flag is labelled "
            "intrinsically bearish and as continuation. Its bias agrees "
            "with the bearish trend sentiment, which greatly increases the "
            "potential for a reliable follow through. The flag is "
            "confirmed once price violates the pattern."
        )),
        Fig(
            panels=(Panel(number="4.13", label="An ascending triangle."),
                    Panel(number="4.14", label="A rounding bottom, or cup "
                                               "and handle.")),
            cols=2, height_mm=54.0,
            caption="Two bullish patterns as continuation in an uptrend.",
        ),
        Para(text=(
            "The book gives the bullish case in one sentence and two "
            "figures: two bullish patterns acting as continuation in trend "
            "phases. Figure 4.13 is an ascending triangle, a flat top over "
            "a rising lower line, forming partway up an uptrend on a 15 "
            "minute EURUSD chart: a bullish pattern in a bullish trend. "
            "Figure 4.14 is a rounding bottom, or cup and handle, partway "
            "up an uptrend on a 4 hour chart. It is the only place the "
            "chapter draws a rounding bottom, so trace the cup, then the "
            "line across its rim."
        )),

        Head(number="2.6", text="Reversal patterns disagree with the trend"),
        Para(text=(
            "As a general guide, intrinsic bias and trend sentiment "
            "disagree for reversal patterns. A standard head and "
            "shoulders, intrinsically bearish, ends an uptrend as "
            "distribution. An inverted one, intrinsically bullish, ends a "
            "downtrend as accumulation."
        )),
        figure("4.7", "A head and shoulders as distribution."),
        Para(text=(
            "In Figure 4.7 a head and shoulders is boxed as a "
            "consolidation range and labelled as distribution. Price "
            "breaks down through its neckline, and at the projected target "
            "below a new consolidation forms. That target is the minimum "
            "price objective: a 1:1 projection of the pattern's height "
            "from the neckline breakout. It is the minimum measuring "
            "objective of Section 1 again, measured on a pattern and not "
            "on a range."
        )),
        figure("4.5", "The book's summary of the section: Phase-Based "
                      "Chart Patterns.", height_mm=78.0),
        Para(text=(
            "Figure 4.5 is the whole section on one page: three lists, "
            "accumulation based, distribution based and continuation "
            "based. Its type is small, so the first two lists are written "
            "out here."
        )),
        Points(
            title="Figure 4.5: the reversal patterns, by phase",
            items=(
                "**Accumulation based, in downtrends**: inverted head and "
                "shoulders, cup and handles, rounding bottoms, falling "
                "wedges, ascending triangles, and double, triple and "
                "multiple bottoms.",
                "**Distribution based, in uptrends**: standard head and "
                "shoulders, rounding tops, rising wedges, descending "
                "triangles, and double, triple and multiple tops.",
                "Both lists add broadening, island and diamond formations. "
                "V bottoms and V tops are reversals too.",
            ),
        ),
        Para(text=(
            "Bullish in a downtrend, bearish in an uptrend: in both lists "
            "the bias and the trend disagree, and the figure marks them as "
            "reversal patterns for that reason. Its third box is the "
            "continuation list, patterns whose intrinsic and trend "
            "sentiment should agree, which matches the two lists in 2.5."
        )),

        Head(number="2.7", text="Neutral patterns borrow their bias"),
        Para(text=(
            "A neutral pattern has no lean of its own, so its surroundings "
            "supply one. A neutral formation's extrinsic bias is derived "
            "from the trend sentiment: a symmetrical triangle is "
            "extrinsically bullish in an uptrend and extrinsically bearish "
            "in a downtrend. Broadening, diamond and island formations are "
            "reversals, so their bias opposes the trend."
        )),
        figure("4.9", "A neutral triangle borrowing the uptrend's bias."),
        Para(text=(
            "Figure 4.9 shows a symmetrical triangle forming partway up an "
            "uptrend, prices consolidating in a convergent manner, "
            "labelled intrinsically neutral, extrinsically bullish, and as "
            "continuation. The preexisting uptrend, in the book's word, "
            "imbues the triangle with extrinsic bullishness."
            "\n\n"
            "**The book contradicts itself on broadening formations.** "
            "Its list of patterns that are bullish with respect to an "
            "uptrend includes them, which files them with the trend. Its "
            "next paragraph says broadening, diamond and island formations "
            "are regarded as reversal formations, and its own Figure 4.5 "
            "puts them on both reversal lists. These notes teach the "
            "paragraph and the figure, and say plainly that the list "
            "disagrees."
        )),

        Head(number="2.8", text="Probabilities, never certainties"),
        figure("4.11", "Two triangles that worked, and one that failed.",
               height_mm=64.0),
        Para(text=(
            "Figure 4.11, the daily iShares Silver Trust chart, is the "
            "book's warning. Two ascending triangles form the "
            "accumulation. The second forms inside the clear support the "
            "first one made, so it is labelled intrinsically and "
            "extrinsically bullish, and price breaks out on a large upside "
            "gap into the trend phase. After the trend a third ascending "
            "triangle forms, and then breaks down instead. Trend sentiment "
            "and intrinsic bias agreed perfectly, and the pattern still "
            "failed. **Technical forecasting is based on probabilities, "
            "and never on certainties.**"
            "\n\n"
            "Failed patterns often lead to a more powerful reaction. Had "
            "the third triangle formed at a significant historical peak, "
            "the book adds, it would have been extrinsically bearish. "
            "Notice also the volume panel: volume declines as each "
            "breakout approaches, which is where Section 3 begins."
        )),
        SelfCheck(text=(
            "A symmetrical triangle forms in the middle of a downtrend. "
            "What is its intrinsic bias, what is its extrinsic bias, and "
            "where does the second one come from?"
        )),
    ),
)


# ==========================================================================
# Section 3 - Volume and open interest (the book's 4.3)
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Volume and Open Interest Interpretation of Market Phase",
    standfirst="What volume normally does in each phase, why it falls "
               "before a phase changes, what a trend that loses volume is "
               "saying, where open interest adds evidence, and what heavy "
               "volume marks. This is the book's section 4.3.",
    blocks=(
        Head(number="3.1", text="Volume falls before the phase changes"),
        Para(text=(
            "Each phase has its typical volume action: down through a "
            "consolidation, and up through a trend. Volume tends to "
            "decline to relatively low levels just before a phase "
            "transition, so it can be used as a timing indicator for "
            "potential phase transitions. **Very low volume says a "
            "consolidation may be ending. It does not say which way.** The "
            "book's summary calls a phase transition a market regime "
            "change, which is the phrase in the chapter's third learning "
            "objective."
            "\n\n"
            "Volume should rise through a trend. If an uptrend or "
            "downtrend is inherently weak, volume falls off during the "
            "trend phase. That is a sign of trend exhaustion, and it "
            "signals a potentially earlier onset of a distribution or "
            "accumulation phase: the trend ends sooner than its start "
            "suggested."
        )),
        Fig(
            panels=(Panel(number="4.15", label="Typical volume action."),
                    Panel(number="4.16", label="Trend exhaustion.")),
            cols=2, height_mm=60.0,
            caption="Volume through the cycle, in the normal case and in a "
                    "weak trend.",
        ),
        Para(text=(
            "Figure 4.15 is the normal case as a schematic cycle of "
            "accumulation, trend, distribution, trend and accumulation, "
            "with volume marked down through each consolidation and up "
            "through each trend. Figure 4.16 is the same cycle with volume "
            "turning down partway through each trend, the turn circled and "
            "labelled trend exhaustion. Compare the two trends: in the "
            "first, volume rises all the way through."
        )),

        Head(number="3.2", text="Open interest: watch for disagreement"),
        Para(text=(
            "For the most part, open interest action correlates fairly "
            "closely with volume action. It is when the two diverge "
            "significantly that open interest adds evidence. **If open "
            "interest increases during a consolidation instead of "
            "decreasing, the breakout and the trend after it tend to be "
            "much more rapid and extended.**"
            "\n\n"
            "Open interest is used here and has still not been defined. "
            "Chapter 3 listed it as transaction data, and the book teaches "
            "it in its Chapter 6. These notes do not borrow a definition "
            "in the meantime."
        )),
        figure("4.17", "Open interest rising through a distribution.",
               height_mm=56.0),
        Para(text=(
            "Figure 4.17 shows the schematic cycle with open interest "
            "rising through the distribution instead of falling, and the "
            "downside breakout that follows labelled strong."
        )),

        Head(number="3.3", text="Volume and phase on a real chart"),
        figure("4.18", "Distribution, trend and accumulation, with volume."),
        Para(text=(
            "Figure 4.18, an intraday Isis Pharmaceuticals chart, puts the "
            "three schematics on one stock. An extended distribution is "
            "violated by a downside gap, on high volume. The trend phase "
            "follows and passes into an accumulation, and volume gradually "
            "decreases as the accumulation progresses. **Falling volume "
            "signals a potentially imminent breakout, to the upside or the "
            "downside.** The figure labels its volume panel bullish volume "
            "divergence, under the trend and again under the accumulation. "
            "Divergence is the subject of Section 5."
        )),

        Head(number="3.4", text="Heavy volume marks a top or a bottom"),
        Para(text=(
            "Higher than normal volume at the start of an accumulation or "
            "distribution strongly indicates that a bottom or top has "
            "formed. **Price levels with historically high volume are "
            "therefore potential levels of accumulation or distribution.**"
        )),
        figure("4.19", "Price-based volume at the two consolidation zones.",
               height_mm=58.0),
        Para(text=(
            "In Figure 4.19, an hourly Facebook chart, horizontal volume "
            "bars are drawn against price levels, and the largest coincide "
            "with a distribution zone and an accumulation zone. The figure "
            "also marks order flow seeking out additional liquidity at the "
            "edges of each zone: the market tests the boundaries of a "
            "consolidation. This is price-based volume, as opposed to "
            "time-based volume, and the chapter uses it without explaining "
            "it."
            "\n\n"
            "So volume has two uses in this section. Falling volume times "
            "the end of a consolidation, and heavy volume marks where one "
            "began."
        )),
        SelfCheck(text=(
            "Volume has been falling for weeks inside a range. What does "
            "that tell you about the range, and what does it not tell you?"
        )),
    ),
)


# ==========================================================================
# Section 4 - Moving averages (the book's 4.4)
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Moving Average Interpretation of Market Phase",
    standfirst="How one moving average behaves in a trend and in a "
               "consolidation, and what several of them do together. This "
               "is the book's section 4.4.",
    blocks=(
        Head(number="4.1", text="One moving average across the phases"),
        Para(text=(
            "Market phase can also be identified by the behavior of moving "
            "averages. During a trending phase a moving average shows the "
            "minimum incidence of whipsaws. During a consolidation, "
            "whipsaw action increases significantly. The cause is the "
            "flattening-out effect of averages in a sideways or ranging "
            "market."
        )),
        figure("4.20", "One moving average in a trend and in a range.",
               height_mm=54.0),
        Para(text=(
            "Figure 4.20 shows one simple moving average under a rising "
            "price, labelled as containing the trend with fewer whipsaws. "
            "The average then flattens inside a boxed consolidation, where "
            "price crosses it again and again, labelled whipsaws during "
            "the consolidation phase. **The book uses the word whipsaw "
            "without defining it.** In the figure the whipsaws are the "
            "places where price crosses back and forth over the flat "
            "average. That reading comes from the figure's own labels; "
            "moving averages, and the definition, are the book's Chapter "
            "11."
        )),

        Head(number="4.2", text="Several averages: spread in a trend, "
                                "tangled in a range"),
        Para(text=(
            "In a trend, multiple moving average lines start to diverge "
            "from each other, and the greater the divergence, the stronger "
            "the ensuing trend. When the lines begin to converge, that is "
            "an early indication of a potential consolidation. "
            "**Overlapping lines mean a consolidation, and diverging lines "
            "mean a strong trend in place.** That is the answer to the "
            "review question on using moving averages to gauge market "
            "phase."
        )),
        figure("4.21", "Four moving averages through the phases."),
        Para(text=(
            "Figure 4.21 is a daily chart with four moving averages, of "
            "20, 50, 100 and 200 days. The lines overlap through an "
            "accumulation phase, fan apart through the trend phase, and "
            "overlap again in the consolidation that follows. The figure "
            "also labels the averages acting as support during the trend. "
            "The book's text does not discuss that here."
        )),
    ),
)


# ==========================================================================
# Section 5 - Divergence and momentum (the book's 4.5)
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="Divergence and Momentum Interpretation of Market Phase",
    standfirst="What divergence is used for in phase analysis, how it "
               "joins with a pattern and a cycle, and why momentum turning "
               "before price is an early sign. This is the book's section "
               "4.5.",
    blocks=(
        Head(number="5.1", text="Divergence tracks momentum"),
        Para(text=(
            "Divergence may be used to track the changes in price "
            "momentum. That makes it extremely useful for identifying "
            "potential consolidations, and the strength of a trend. Once "
            "divergence is observed, look for a slowing of the trend."
            "\n\n"
            "**The chapter uses divergence, MACD and RSI without defining "
            "any of them.** Divergence is taught in the book's Chapter 9. "
            "What follows describes what each figure shows, in the book's "
            "own labels, and stops there."
        )),
        figure("4.22", "Standard bearish divergence in a distribution.",
               height_mm=80.0),
        Para(text=(
            "In Figure 4.22, an hourly EURUSD chart, price makes a higher "
            "peak inside a distribution while the MACD below it makes a "
            "lower one. The figure labels this standard bearish "
            "divergence, and momentum turning before price. Divergence "
            "shows momentum slowing, and a slowing trend is a "
            "consolidation forming, which is the answer to the review "
            "question on divergence."
        )),

        Head(number="5.2", text="Bullish divergence supports an "
                                "accumulation"),
        figure("4.23", "A pattern, a divergence and a cycle in agreement.",
               height_mm=74.0),
        Para(text=(
            "Figure 4.23 is the daily 3M chart. The accumulation takes the "
            "form of an inverted head and shoulders pattern, and it is "
            "further supported by standard bullish divergence on the MACD. "
            "The left shoulder, the head and the right shoulder coincide "
            "with the projected cycle lows, which the figure draws as "
            "vertical lines. **This bullish confluence within the "
            "accumulation greatly increases the probability of a strong "
            "upside move.** Confluence is the book's word for several "
            "kinds of evidence agreeing: here a pattern, a divergence and "
            "a cycle. The figure also labels a reverse bullish and a "
            "standard bearish divergence, and the text discusses neither."
        )),

        Head(number="5.3", text="Momentum turns before price"),
        figure("4.24", "Bullish divergence on volume, the MACD and the "
                       "RSI.", height_mm=62.0),
        Para(text=(
            "Figure 4.24 is a 5 minute GBPUSD chart of a downtrend passing "
            "into an accumulation, with a new trend rising out of it. "
            "Volume, the MACD and the RSI all show bullish divergence with "
            "price in the accumulation, and the MACD and the RSI are both "
            "momentum-based indicators. Price is still falling inside the "
            "box while both indicators are already rising. **We see "
            "momentum turning before price.** At the tail end of a trend, "
            "a sign that a consolidation may be forming helps a trader "
            "anticipate an early entry."
            "\n\n"
            "The book gives one sentence of method, and it is about "
            "volume: for bullish divergence in volume, falling prices must "
            "be accompanied by decreasing volume."
        )),
        SelfCheck(text=(
            "Price makes a higher peak while a momentum indicator makes a "
            "lower one. What should you look for in the trend next, and "
            "which phase may be forming?"
        )),
    ),
)


# ==========================================================================
# Section 6 - Sentiment (the book's 4.6)
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Sentiment Interpretation of Market Phase",
    standfirst="Why sentiment reads best at market extremes, the thirteen "
               "indicators the book names, and what six of them read at a "
               "top and at a bottom. This is the book's section 4.6.",
    blocks=(
        Head(number="6.1", text="Sentiment is clearest at the extremes"),
        Para(text=(
            "Market participants swing between fear, greed and hope, "
            "responding to news and to each other. Identifiable patterns "
            "repeat fairly consistently, especially at market extremes. "
            "Sentiment indicators track participants' aggregate sentiment, "
            "emotions and psychology. **They are most accurate at extremes "
            "of optimism or pessimism.**"
            "\n\n"
            "Section 1 already described that crowd. The uninformed were "
            "extremely bullish at the distribution and extremely bearish "
            "at the accumulation. Sentiment indicators measure them, so "
            "they read best exactly where the crowd is most one sided."
        )),
        chart("Q", "Where sentiment indicators are most accurate."),
        Para(text=(
            "Chart Q boxes the top and the bottom of one market swing. At "
            "the top the crowd is extremely bullish, at the bottom "
            "extremely bearish, and those two extremes are where sentiment "
            "indicators are most accurate."
        )),

        Head(number="6.2", text="Thirteen indicators, by name"),
        Para(text=(
            "The book gives thirteen sentiment indicators as examples: "
            "put-call ratios, Arm's Index, odd lot sales, margin debt, the "
            "COT report, the VIX, the short interest ratio, the cash asset "
            "ratio, the advance-decline line, new highs minus new lows, up "
            "volume minus down volume, Market Vane reports, and the "
            "Bullish Sentiment Index. **It explains none of them in this "
            "chapter, and these notes do not either.** The book's Chapter "
            "23 is the detailed discussion. How any one of them is built "
            "is not examined from this chapter."
        )),

        Head(number="6.3", text="What the indicators read at a top and at "
                                "a bottom"),
        Para(text=(
            "At a distribution the put/call ratio and the VIX are low, but "
            "starting to increase. A/D, margin debt, new highs minus new "
            "lows and the Bullish Percent Index are high, but starting to "
            "decrease. At an accumulation every one of those readings is "
            "reversed. **Each reading is at an extreme and has just "
            "started to turn.** This is the answer to the review question "
            "that asks which sentiment indicators best describe "
            "distributions."
        )),
        figure("4.25", "Six sentiment readings at a top and at a bottom.",
               height_mm=70.0),
        Para(text=(
            "Figure 4.25 draws a price curve from a distribution at the "
            "top to an accumulation at the bottom and lists the six "
            "readings beside each. Two start low at a top and four start "
            "high. At a bottom, swap the words high and low."
            "\n\n"
            "One loose end. The figure says Bullish Percent Index, and the "
            "list of thirteen says Bullish Sentiment Index. The book does "
            "not say whether they are the same."
        )),
        SelfCheck(text=(
            "Cover Figure 4.25 and write out the six readings for an "
            "accumulation. Which two are high, and which way has each "
            "started to turn?"
        )),
    ),
)


# ==========================================================================
# Section 7 - Sakata (the book's 4.7)
# ==========================================================================

SECTION7 = Section(
    number=7,
    title="Sakata's Interpretation of Market Phase",
    standfirst="A Japanese model that divides the market into five phases, "
               "the five names and what each stands for, and how the five "
               "fit inside Dow's three. This is the book's section 4.7.",
    blocks=(
        Head(number="7.1", text="Five phases, not three"),
        Para(text=(
            "Dow's model has three phases. The Japanese way of reading the "
            "market divides it into five: three bottoms, three thrusts "
            "with a correction after each, and three tops."
        )),
        formal("Sakata's Five Methods"),
        figure("4.26", "Sakata's five phases, beside Elliott's waves."),
        Para(text=(
            "Figure 4.26 sets two panels side by side. On the left are "
            "Sakata's five market phases: San Sen at the bottom, San Pei, "
            "San Poh and San Ku through the rise, and San Zan at the top. "
            "On the right is Elliott's 5-3 wave structure, which is "
            "Section 8. The book says the two are very similar in "
            "appearance. Munehisa Honma's name is all the history the book "
            "gives, and these notes add none."
        )),

        Head(number="7.2", text="The five methods, by name"),
        Points(
            items=(
                "**San Zan, three mountains.** The Western triple top. The "
                "distribution phase.",
                "**San Sen, three rivers.** The Western triple bottom. The "
                "accumulation phase.",
                "**San Ku, three gaps.** The breakaway, runaway and "
                "exhaustion gaps of the trend.",
                "**San Pei, three thrusts.** The three trending phases "
                "between the two.",
                "**San Poh, three methods.** The three corrections, one "
                "after each thrust.",
            ),
        ),
        chart("R", "The five methods on one line."),
        Para(text=(
            "The book glosses every name as three of something, which is "
            "the handle for remembering all five. Two of the five are "
            "consolidations, and three describe the trend between them. "
            "Chart R puts all five on one invented line, each with the "
            "book's English. The three gaps are among the four that "
            "Chapter 3 named."
        )),

        Head(number="7.3", text="Five phases inside three"),
        Para(text=(
            "Dow's three phases may seem inconsistent with Sakata's five, "
            "and with Elliott's waves. The book's answer is that simple "
            "chart patterns show the models need not be viewed as "
            "distinct: a triple bottom, then thrusts with bullish flags "
            "and gaps between them, then a triple top. **It calls this a "
            "plausible resolution between Eastern and Western approaches, "
            "and its summary calls the two approaches complementary.**"
        )),
        figure("4.27", "Dow's three phases drawn with Sakata's pieces.",
               height_mm=66.0),
        Para(text=(
            "Figure 4.27 draws Dow's three-phase market with Sakata's "
            "pieces: a triple bottom as the accumulation phase, a rising "
            "channel of thrusts, bullish flags and the breakaway, runaway "
            "and exhaustion gaps as the trend phase, and a triple top as "
            "the distribution phase. This is the chapter's sixth learning "
            "objective, comparing Eastern and Western approaches, and the "
            "comparison comes out as one fitting inside the other."
        )),
        SelfCheck(text=(
            "Without looking back, give the English for each of the five "
            "names, and say which two are consolidations."
        )),
    ),
)


# ==========================================================================
# Section 8 - Elliott (the book's 4.8)
# ==========================================================================

SECTION8 = Section(
    number=8,
    title="Elliott's Interpretation of Market Phase",
    standfirst="Elliott's five waves up and three waves down mapped onto "
               "the phases, and a wave count on a real chart. This is the "
               "book's section 4.8.",
    blocks=(
        Head(number="8.1", text="Five waves up, three waves down"),
        Para(text=(
            "Elliott described markets as an impulsive five-wave up, then "
            "a corrective three-wave down. **The trending phase is impulse "
            "waves 1, 3 and 5, and the accumulation phase is corrective "
            "waves 2 and 4.** Sakata's San Pei closely resembles waves 1, "
            "3 and 5, and San Poh somewhat resembles waves a, b and c. "
            "Elliott's waves have specific rules; Sakata's model is less "
            "rigid."
        )),
        figure("4.28", "Elliott's wave structure.", height_mm=48.0),
        Para(text=(
            "Figure 4.28 is the structure: five numbered motive waves "
            "rising, with waves 1, 3 and 5 marked impulsive, then three "
            "lettered corrective waves a, b and c falling. That is eight "
            "waves of one degree."
            "\n\n"
            "**The book gives the abc correction to both consolidations.** "
            "It says the accumulation phase includes the abc correction in "
            "most cases, and in the next sentence that distribution is "
            "usually the abc correction. These notes record both and do "
            "not pick one."
        )),

        Head(number="8.2", text="The waves on the gold chart"),
        figure("4.29", "An Elliott wave count on weekly gold.",
               height_mm=60.0),
        Para(text=(
            "Figure 4.29 is the weekly gold chart from 2000 to 2012 with "
            "an Elliott wave count, on log scaling. Primary waves 1 and 2 "
            "sit in the accumulation, and the powerful wave 3 in the "
            "trend. Volume gradually decreases over each significant "
            "consolidation, at the three places the figure numbers, which "
            "is Section 3 again. Volume peaks around the top of wave 5, "
            "within a new area of consolidation that the figure marks as a "
            "potential distribution phase. The book describes that "
            "consolidation at the top as an inverted head and shoulders, "
            "and these notes report it as the book states it."
            "\n\n"
            "The book adds that Fibonacci price and time projections help "
            "gauge where each wave ends. Fibonacci projection is not "
            "taught in this chapter, and Elliott's rules are the book's "
            "Chapter 18."
        )),
    ),
)


# ==========================================================================
# Section 9 - Cycle analysis (the book's 4.9), and what the chapter borrows
# ==========================================================================

SECTION9 = Section(
    number=9,
    title="Cycle Analysis Interpretation of Market Phase",
    standfirst="How a formation's place on a cycle decides whether it is a "
               "reversal or a continuation, shown on one neutral pattern "
               "in three roles, and a list of what this chapter uses "
               "without teaching. This is the book's section 4.9.",
    blocks=(
        Head(number="9.1", text="Where in the cycle decides what the "
                                "pattern is"),
        Para(text=(
            "Whether a formation reverses or continues depends on where in "
            "the cycle it unfolds. Between cycle extremes, formations tend "
            "to be continuations. At cycle peaks they tend to be "
            "distributions, and at cycle troughs, accumulations. **If the "
            "intrinsic and extrinsic biases agree as well, the formation "
            "is potentially more reliable.** All of this is for formations "
            "on the same cycle degree, and it is the answer to the review "
            "question on using a cycle to gauge market phase."
            "\n\n"
            "It is also extrinsic bias again: the phase of an underlying "
            "market cycle was the third of the five factors in Section 2. "
            "Once a cycle period is identified, the book says, placing the "
            "formation on it is fairly simple. How the period is found is "
            "the book's Chapter 20."
        )),
        Fig(
            panels=(Panel(number="4.30", label="Formations on a cycle."),
                    Panel(number="4.31", label="One triangle, three "
                                               "roles.")),
            cols=2, height_mm=58.0,
            caption="Where a formation sits on the cycle, and what that "
                    "makes it.",
        ),
        Para(text=(
            "Figure 4.30 boxes four formations on a price cycle: a "
            "reversal as accumulation at each cycle trough, a continuation "
            "between the extremes, and a reversal as distribution at the "
            "cycle peak. Figure 4.31 does the same with a single pattern, "
            "the symmetrical triangle, drawn at four places. The shape is "
            "the same each time, and only its place on the cycle differs."
        )),

        Head(number="9.2", text="One triangle, three roles"),
        Para(text=(
            "The intrinsically neutral symmetrical triangle takes three "
            "distinct roles: accumulation at the bottom of the cycle, "
            "continuation between the top and the bottom, and distribution "
            "at the top. It adopts a bullish extrinsic bias at cycle "
            "troughs and a bearish one at cycle peaks. Between the "
            "extremes it adopts the preexisting trend sentiment. Section 2 "
            "said that neutral patterns borrow their bias, and here the "
            "lender is the cycle and not the trend."
        )),
        figure("4.32", "The same triangle in a price channel.",
               height_mm=62.0),
        Para(text=(
            "Figure 4.32 moves the triangle into an uptrending price "
            "channel: accumulation at the bottom of the channel, "
            "continuation in the middle, and distribution at the top. Had "
            "the pattern been an inverted head and shoulders, the book "
            "says, a reversal at the bottom or a continuation in the "
            "middle would be more probable. That pattern is intrinsically "
            "bullish, so at the bottom of the channel both biases would "
            "agree."
            "\n\n"
            "The figure is headed with an instruction to look for "
            "supportive and resistive confluences. **Confluences with "
            "other overlay barriers, such as Fibonacci levels, give more "
            "reliable forecasts of where price may react.** Fibonacci "
            "levels are named here and not taught."
        )),
        SelfCheck(text=(
            "A symmetrical triangle forms at a cycle peak. What role does "
            "it take, and what extrinsic bias does it adopt?"
        )),

        Head(number="9.3", text="What this chapter uses and does not teach"),
        Para(text=(
            "Six of the nine sections borrow a tool that a later chapter "
            "of the book teaches. Each was named where it appeared, and "
            "they are collected here."
        )),
        Points(
            items=(
                "The shapes of the chart patterns: Chapter 13.",
                "Open interest: Chapter 6. Price-based volume is also used "
                "and not explained.",
                "Moving averages and whipsaws: Chapter 11.",
                "Divergence, MACD and RSI: Chapter 9.",
                "The thirteen sentiment indicators: Chapter 23.",
                "Elliott's rules: Chapter 18. Fibonacci projections are "
                "also used and not explained.",
                "How a cycle period is found: Chapter 20.",
                "The learning objectives promise the inertial "
                "characteristics of each phase. The text never uses the "
                "word.",
            ),
        ),
        Para(text=(
            "**From this chapter, only what each tool says about market "
            "phase is examinable.** Do not fill these gaps from outside "
            "the book. Each comes back in its own chapter."
            "\n\n"
            "Three more places are worth remembering, because the book "
            "says two different things or leaves a question open. "
            "Broadening formations are filed two ways, in 2.7. The abc "
            "correction is given to both consolidations, in 8.1. And the "
            "Bullish Percent Index of Figure 4.25 may or may not be the "
            "Bullish Sentiment Index of the list, in 6.3."
        )),
    ),
)


# ==========================================================================

NOTES = LectureNotes(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 4",
    title="Market Phase Analysis",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    term="First semester",
    source_note="Chapter scope follows Lim, M. (2016), The Handbook of "
                "Technical Analysis, chapter 4. Figures are reproduced from "
                "that text and remain the publisher's copyright. Charts "
                "are drawn for this course on invented prices.",
    orientation=(
        "These notes are the record of what Chapter 4 covered, written to "
        "be read on their own. If you were in the room, they are what to "
        "revise from. If you missed the session, they are the session. "
        "They follow the lecture in the same order. The nine sections are "
        "the book's own sections 4.1 to 4.9, so Section 3 of these notes "
        "is the book's section 4.3, and the book's 4.10, its summary, is "
        "the summary at the back."
        "\n\n"
        "The chapter asks one question nine ways: which phase is the "
        "market in? Read it with the pictures beside you. A figure is the "
        "book's. A chart is one this course drew, on invented prices, "
        "where the book makes a point in words and draws nothing. Every "
        "term is defined once, in the same words as the slides, and listed "
        "again at the back. The check yourself boxes are not assessed."
        "\n\n"
        "Six of the nine sections borrow a tool that a later chapter of "
        "the book teaches. Where that happens, or where the book says two "
        "different things, these notes say so rather than filling the gap "
        "from somewhere else, and Section 9.3 collects every one of those "
        "places."
    ),
    # The book's six learning objectives, in its own words. The deck's
    # objectives slide is where they are maintained.
    objectives=tuple(CHAPTER.objectives),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6,
              SECTION7, SECTION8, SECTION9),
    # The summary and the review questions are the book's, and the deck's
    # closing slides are where they are maintained. build_lecture_notes4.py
    # reads them from there and fills these in, so editing the closing slide
    # moves the notes with it. Do not retype them here.
    summary=(),
    review_questions=(),
    sources=(
        "Lim, M. (2016). The Handbook of Technical Analysis. Wiley. "
        "Chapter 4, and the source of every figure here.",
    ),
)
