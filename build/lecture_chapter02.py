"""FIN1209 Chapter 2 student lecture notes, as plain data.

This is the file a contributor edits. Layout lives in build/lecturekit.py and
knows nothing about any chapter; the reasoning behind the layout, with the
research it came from, is chapter-01/lecture-notes-design.md.

    .venv/bin/python build/build_lecture_notes2.py

Written for a student reading alone, with no instructor in the room. Full
sentences that explain, not bullets that gesture. The six sections are the
deck's six parts in the deck's order, so a student can move between the two.

Nothing here is timing, cut tiers, speaker cues, check answers or slide
numbers. Those belong to the instructor and they live in
build/plan_chapter02.py.

Figure descriptions are never retyped here. The build takes them from
content_chapter02.py, which is also where the deck's own placeholder takes
them, so the two documents cannot describe the same figure differently.
"""

from __future__ import annotations

from lecturekit import (Define, Fig, Head, LectureNotes, Panel, Para, Points,
                        Quote, Section, SelfCheck)


# ==========================================================================
# Section 1 - Where Dow Theory came from
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Where Dow Theory Came From",
    standfirst="The four men whose writing became Dow Theory, the three "
               "assumptions the theory was built on, and why Dow wanted an "
               "average of many stocks instead of a price for one.",
    blocks=(
        Head(number="1.1", text="A theory nobody set out to write"),
        Para(text=(
            "Dow Theory lays the basic foundation for modern day technical "
            "analysis. Its premises underpin the very study of market "
            "action, and the book's claim for them is that they have "
            "withstood the test of time. Almost everything in the rest of "
            "this course rests on the six statements set out in Section 2."
            "\n\n"
            "The odd thing about it is that Charles H. Dow never wrote a "
            "book called Dow Theory, and never used the phrase. He is "
            "credited for much of the early work that led to it, but his "
            "writing was journalism: editorials in the Wall Street Journal, "
            "published around the beginning of the twentieth century. "
            "**The theory is what other people made of what he wrote.**"
        )),
        Define(
            term="Dow Theory",
            text="Dow Theory is the body of basic premises credited to "
                 "Charles H. Dow and codified by later writers, which lays "
                 "the basic foundation for modern day technical analysis.",
        ),
        Para(text=(
            "Three men did the making, and it is worth keeping them apart "
            "because examinations ask which one did what."
        )),
        Points(
            title="The three who came after Dow",
            items=(
                "**William P. Hamilton**, Dow's successor, carried on "
                "developing and organizing Dow's original early writings. "
                "His book is The Stock Market Barometer.",
                "**S. A. Nelson**, a close acquaintance of Dow's, published "
                "a book about Dow's work called The ABC of Stock "
                "Speculation, and was the first person to refer to Dow's "
                "concepts and ideas as the Dow Theory.",
                "**Robert Rhea**, a student of Hamilton, was responsible for "
                "much of the categorizing, refining and formal codification "
                "of Dow's basic premises. His book is The Dow Theory.",
            ),
        ),
        Para(text=(
            "It was Rhea's work that really developed Dow's theory and laid "
            "its basic foundation, and he did it on three assumptions. They "
            "are worth learning as three, because the chapter comes back and "
            "attacks two of them at the end."
        )),
        Points(
            title="Rhea's three assumptions",
            numbered=True,
            items=(
                "The primary trend is not susceptible to manipulation, "
                "although there is a possibility that manipulation could "
                "occur over the shorter term.",
                "The averages discount everything, and price is a reflection "
                "of all information.",
                "Dow Theory itself is not perfect, and investing according "
                "to its principles will not guarantee profitability.",
            ),
        ),
        Define(
            term="The primary trend is not susceptible to manipulation",
            text="Rhea's first assumption is that the primary trend is not "
                 "susceptible to manipulation, although there is a "
                 "possibility that manipulation could occur over the shorter "
                 "term.",
        ),
        Para(text=(
            "That first assumption is doing more work than it looks. It is "
            "the reason Dow Theory bases every decision on the primary trend "
            "and almost nothing else: the long movement is held to be the "
            "one nobody can push around. One large buyer can move a small "
            "listed company for a week. Rhea's claim is that nobody can hold "
            "a whole market up for two years. **Section 6 is where the book "
            "itself says this is no longer true.**"
        )),
        Define(
            term="Dow Theory is not perfect",
            text="Rhea's third assumption is that Dow Theory itself is not "
                 "perfect and that investing according to its principles "
                 "will not guarantee profitability. At most it should be "
                 "regarded as a set of guidelines for investing.",
        ),
        Para(text=(
            "Notice who is saying it. The man who codified the theory is the "
            "one telling you it is fallible, and that at most it is a set of "
            "guidelines. Any statement that Dow Theory is infallible, or "
            "that it guarantees a profit, is wrong on the theory's own terms."
        )),
        SelfCheck(text=(
            "Without looking back: which of the four men named the theory, "
            "and which one wrote its premises down as premises?"
        )),

        Head(number="1.2", text="Why an average, and not a price"),
        Para(text=(
            "In 1884 Dow published a stock market average of 11 stocks. He "
            "later developed it into a 12 stock Industrial Index and a 20 "
            "stock Railroad Average. He wanted a number for the market, not "
            "a number for one company."
        )),
        Define(
            term="A stock market average",
            text="A stock market average is an index of stocks created to "
                 "better reflect the general action of the markets, instead "
                 "of gauging market behavior through individual stock "
                 "action.",
        ),
        Para(text=(
            "The reason was practical. Individual stock action at the time "
            "was fairly erratic and open to manipulation, and an index was "
            "meant to average out or smooth those erratic price movements. "
            "The action of the averages was then meant to act as a barometer "
            "of the current market environment. **Barometer is the word to "
            "hold on to**: it reads the weather, it does not make it, and "
            "Hamilton put it in the title of his book."
        )),
        Fig(
            panels=(Panel(number="A"),), kind="chart", height_mm=57.0,
            caption="Three separate issues, and the line that is their "
                    "average.",
        ),
        Para(text=(
            "Chart A shows what the smoothing buys you. Any one of the thin "
            "lines tells you a great deal about one company and very little "
            "about the market. The bold line, which is simply their average, "
            "moves far more calmly than any of its members and is much "
            "harder for any one participant to push. The Philippine Stock "
            "Exchange index is the same idea: one number that moves with "
            "thirty listed companies at once."
            "\n\n"
            "Both of Dow's averages still exist under different names. The "
            "12 stock Industrial Index has gradually evolved into 30 stocks "
            "and is known today as the **Dow Jones Industrial Average**. The "
            "Railroad Average is known today as the **Dow Jones "
            "Transportation Average**. Keep the pair in mind, because in "
            "Section 6 they will be required to agree with each other before "
            "anything counts as a signal."
        )),
    ),
)


# ==========================================================================
# Section 2 - The six tenets, and the first one
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="The Six Tenets, and the First One",
    standfirst="The list the whole chapter is built on, what it means to say "
               "that the averages discount everything, and the single price "
               "Dow Theory is willing to record.",
    blocks=(
        Head(number="2.1", text="The six basic tenets"),
        Para(text=(
            "Everything else in this chapter is one of these six statements "
            "explained at length. Learn them as a list, in this order, "
            "because that is how they are asked."
        )),
        Points(
            title="The six basic tenets of Dow Theory",
            numbered=True,
            items=(
                "The averages discount everything.",
                "The market has three trends.",
                "Primary trends have three phases.",
                "A trend persists until its reversal is indicated.",
                "The averages must confirm one another.",
                "Volume must confirm the trend.",
            ),
        ),
        Para(text=(
            "Read the third one again. It says **primary** trends have three "
            "phases, not all trends. A statement that all trends have three "
            "phases is not a tenet of Dow Theory, and that substitution is "
            "the most common way this list is set as a trick."
            "\n\n"
            "In addition to the six basic tenets, only closing prices are "
            "recognized in Dow Theory. The book states that separately "
            "rather than numbering it, so it is a seventh rule and not a "
            "seventh tenet. It is dealt with at the end of this section."
        )),

        Head(number="2.2", text="The averages discount everything"),
        Define(
            term="The averages discount everything",
            text="The first tenet: the market is the end result of all "
                 "participatory action, which represents all information "
                 "that may be known to the markets.",
        ),
        Para(text=(
            "In plain words, the market has already priced in everything "
            "anybody knows, and what you see on the chart is the sum of what "
            "every participant did about what they knew. This is why prices "
            "so often move before the announcement rather than after it: by "
            "the time a company's good results reach the evening news, the "
            "people who were going to act on them have already bought."
            "\n\n"
            "The mechanism matters. Information becomes known to the market "
            "through actual participation, that is, through capital being "
            "put in or taken out. **Information that nobody acts on has not "
            "reached the market at all.** The price is not what people "
            "think; it is what they did about what they think."
        )),
        Para(text=(
            "The claim is weaker than it first sounds, and deliberately so. "
            "Discounting need not be instantaneous. It need not be driven by "
            "rational participants. There is no requirement that all "
            "participants act on all information all of the time, or that "
            "they react in the same manner as one another. Compare that with "
            "the efficient market hypothesis from Chapter 1, which needs all "
            "four of those conditions: Dow Theory survives slow, irrational, "
            "partial and inconsistent participants, and that is why the "
            "assumption is usable."
        )),
        Define(
            term="Acts of God",
            text="The market discounts everything except acts of God, that "
                 "is, unexpected events or unknown information. It can still "
                 "absorb, react and adjust to such shocks fairly rapidly.",
        ),
        Para(text=(
            "The exception has two halves and students usually remember only "
            "the first. An earthquake at nine in the morning cannot be in "
            "yesterday's closing price, because nothing could have put it "
            "there. But once the event is known, the market absorbs and "
            "adjusts to it fairly rapidly."
        )),
        Fig(
            panels=(Panel(number="2.1", label="Discounting, or coincidence?"),
                    Panel(number="2.2", label="Adjusting once the news is "
                                              "known.")),
            cols=2, height_mm=52.0,
            caption="The book's own question, and the case where the answer "
                    "is not in doubt.",
        ),
        Para(text=(
            "Figure 2.1 shows prices falling before the September 11 event, "
            "and the book prints its own question on the chart: is the "
            "market trying to discount information that is not yet known, or "
            "is this merely coincidental? **The chapter does not answer it.** "
            "That is worth noticing rather than resolving, and no assessment "
            "in this course will ask you to settle it. Figure 2.2 is the "
            "second half of the definition and is not in doubt at all: gold "
            "adjusts very rapidly to the same event once the information has "
            "become known to the market."
            "\n\n"
            "The consequence for the analyst is the one Chapter 1 already "
            "made. Price is the ultimate reflection and embodiment of "
            "everything that is knowable, so the technical analyst need not "
            "concern themselves with the causes giving rise to market "
            "action, but only with the effects of the underlying causes. "
            "**Effects, not causes.**"
        )),
        SelfCheck(text=(
            "Dow Theory does not require participants to be rational. Why is "
            "that a strength of the assumption rather than a weakness in it?"
        )),

        Head(number="2.3", text="Only closing prices are recognized"),
        Define(
            term="Only closing prices are recognized",
            text="In Dow Theory only closing prices are recognized: "
                 "regardless of how large the high and low price excursions "
                 "may be on any one day, only the final closing price is "
                 "used.",
        ),
        Para(text=(
            "Suppose a share swings between 96 and 104 pesos during the day "
            "and finishes at 100. Dow Theory records 100. The eight peso "
            "swing is not recorded anywhere, and neither is the order in "
            "which the high and the low happened."
            "\n\n"
            "It also does not matter how miniscule the amount is. A close "
            "one centavo above yesterday's close is a higher close; one "
            "centavo below is a lower close. The test is the close, and any "
            "amount above or below it counts, which is why a valid breakout "
            "under this theory is a closing violation rather than an "
            "intraday one."
        )),
        Fig(
            panels=(Panel(number="B"),), kind="chart", height_mm=57.0,
            caption="Everything the theory throws away, and the one number "
                    "it keeps.",
        ),
        Para(text=(
            "Chart B draws both at once. The pale bars are how far the price "
            "travelled on each day, and every one of them is discarded. The "
            "joined dots are the entire record Dow Theory works from. A day "
            "that swung a long way and a day that barely moved contribute "
            "exactly one closing price each. **Section 6 lists this as one "
            "of the seven criticisms of the theory**, so if the rule already "
            "bothers you, hold the objection until then."
        )),
    ),
)


# ==========================================================================
# Section 3 - Three trends, and the primary one
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Three Trends, and the Primary One",
    standfirst="The three movements the book says are running at the same "
               "time, what an uptrend actually is, and why a Dow Theory "
               "signal always arrives late.",
    blocks=(
        Head(number="3.1", text="Three movements at once"),
        Define(
            term="The market has three trends",
            text="The second tenet of Dow Theory is that the market "
                 "comprises three trends: the primary trend, the secondary "
                 "reaction and the minor trend.",
        ),
        Quote(
            text="There are three movements of the averages, all of which "
                 "may be in progress at one and the same time.",
            source="Robert Rhea, The Dow Theory, quoted in Lim, The Handbook "
                   "of Technical Analysis",
        ),
        Para(text=(
            "The last eight words are the ones to keep. The three trends do "
            "not take turns. At any given moment a market is doing all three "
            "at once, which is why two people looking at the same chart can "
            "describe it correctly in completely different terms."
        )),
        Points(
            title="The three trends, with their durations",
            numbered=True,
            items=(
                "**Primary trend**, also called the major trend. Months to "
                "years, so long term.",
                "**Secondary reaction**, also called the intermediate trend. "
                "Weeks to months, so medium term.",
                "**Minor trend**. Days to weeks, so short term.",
            ),
        ),
        Para(text=(
            "Rhea called the primary the most important of the three and the "
            "secondary the most deceptive, and Section 4 shows why that "
            "second description is earned. The chapter also gives the "
            "analogy that people remember longest: the primary trend is the "
            "tides of the ocean, the secondary reaction is the waves on the "
            "tides, and the minor trend is the ripples on the waves. A "
            "ripple never tells you whether the tide is coming in."
        )),
        Fig(
            panels=(Panel(number="C"),), kind="chart", height_mm=57.0,
            caption="One price line carrying a primary trend, a secondary "
                    "reaction and daily fluctuation together.",
        ),
        Para(text=(
            "Chart C puts all three on a single line so the claim is "
            "visible: the arrow, the shaded stretch and the small wiggles "
            "are not three periods of time, they are three descriptions of "
            "the same period. Figure 2.3 does the same thing on a real "
            "index, with the primary trend, a secondary reaction and the "
            "minor trends all labelled, and with the primary trend resuming "
            "when price breaks out above the peak the reaction made."
        )),
        Fig(
            panels=(Panel(number="2.3"),), cols=1, height_mm=62.0,
            caption="All three trends labelled on one index at the same "
                    "time.",
        ),

        Head(number="3.2", text="The primary trend"),
        Define(
            term="Primary trend",
            text="The primary or major trend is the largest trend, normally "
                 "expected to last from months to years, and the one Rhea "
                 "held to be a more reliable barometer for investment "
                 "decisions.",
        ),
        Para(text=(
            "It comes in two kinds, a primary bull trend and a primary bear "
            "trend, and Rhea's own warning attaches to both: it is very "
            "difficult to forecast the extent or the duration of a primary "
            "trend. The theory will tell you a trend exists. It will not "
            "tell you how far it goes or when it stops."
        )),
        Define(
            term="Uptrend",
            text="In Dow Theory, an uptrend is defined primarily as "
                 "successively higher peaks and troughs.",
        ),
        Define(
            term="Downtrend",
            text="In Dow Theory, a downtrend is defined as successively "
                 "lower peaks and troughs.",
        ),
        Para(text=(
            "Read those two definitions as instructions rather than "
            "descriptions, because they are the test you actually apply. "
            "Peaks at 104, 116 and 128 pesos with troughs at 98, 108 and 119 "
            "between them is an uptrend: every peak beats the last peak and "
            "every trough beats the last trough. The same six numbers read "
            "backwards are a downtrend. **A trend, in this theory, is a "
            "sequence of points and nothing else.**"
        )),
        Fig(
            panels=(Panel(number="D"),), kind="chart", height_mm=57.0,
            caption="Every peak and trough marked, and then the one that "
                    "breaks the sequence.",
        ),
        Para(text=(
            "Chart D walks that sequence and then stops on the point where "
            "it fails. Figure 2.4 does the same with the book's own "
            "shorthand, HH for a higher high and HL for a higher low, and "
            "circles the appearance of the first lower high. The caption is "
            "worth quoting: at that point the uptrend has technically ended. "
            "Nothing about the company changed and the price is still high. "
            "The sequence changed, and the sequence was the trend."
        )),
        Fig(
            panels=(Panel(number="2.4"),), cols=1, height_mm=56.0,
            caption="An uptrend in terms of successively higher highs and "
                    "lows, and the first lower high.",
        ),
        Para(text=(
            "Note that the book says a lower high **may** represent an early "
            "indication that the uptrend is coming to an end. It does not "
            "say the trend has certainly ended. Section 5 sets out the "
            "formations that make the case properly."
        )),
        SelfCheck(text=(
            "An uptrend has run 104, 98, 116, 108, 128, 119, 141, 128, and "
            "now makes a peak at 134. Has anything happened that Dow Theory "
            "notices?"
        )),

        Head(number="3.3", text="Penetration, and the cost of waiting"),
        Define(
            term="Penetration",
            text="In Dow Theory, an indication of a trend continuation or "
                 "reversal is signaled by the penetration of a previous peak "
                 "or trough.",
        ),
        Para(text=(
            "This is the single most examined sentence in the chapter, and "
            "it combines with the closing price rule from Section 2: the "
            "peak or trough has to be penetrated on a closing basis, and any "
            "amount counts."
            "\n\n"
            "Waiting for that event has a price. One of the main criticisms "
            "of Dow Theory is that its buy and sell signals arrive too late, "
            "usually missing out on one third or more of the entire trend. "
            "You buy after the bottom and you sell after the top, every "
            "time. Dow's own answer was that it is more important to "
            "participate in a primary trend once it has been confirmed, and "
            "that losing out on some potential profit for the added safety "
            "of a confirmed trend is well worth the sacrifice. **That is "
            "reported as Dow's position, not as a settled fact**, and "
            "Section 6 gives the argument on the other side."
        )),
        Fig(
            panels=(Panel(number="2.5"),), cols=1, height_mm=58.0,
            caption="The profit available on Dow's signals, against the "
                    "profit that was theoretically there.",
        ),
        Para(text=(
            "Figure 2.5 shades both, and the gap at the bottom and the gap "
            "at the top are what confirmation costs. It is also worth being "
            "clear about how little the theory lets you trade: all "
            "investment and trading decisions are based strictly on the "
            "primary trend alone, with the single exception of lines, which "
            "form out of the daily price fluctuations and are defined in "
            "Section 4."
            "\n\n"
            "Two real examples show the scale of a primary trend. Figure 2.6 "
            "is a primary bull trend in gold that lasted approximately "
            "twelve years. Figure 2.7 is a primary bear trend in the 30 year "
            "Treasury bond yield that lasted approximately twenty three "
            "years. Read those two durations beside the phrase stop loss and "
            "you have already met the first of the criticisms in Section 6."
        )),
        Fig(
            panels=(Panel(number="2.6", label="Twelve years of primary bull "
                                              "trend."),
                    Panel(number="2.7", label="Twenty three years of primary "
                                              "bear trend.")),
            cols=2, height_mm=50.0,
            caption="What months to years means when it is drawn to scale.",
        ),

        Head(number="3.4", text="Two definitions of a trend, and two scales"),
        Para(text=(
            "There is a second way to decide when a trend has changed, and "
            "the chapter is honest that it can disagree with the first. If "
            "trends are defined by trendline violations rather than by the "
            "sequence of rising or falling peaks and troughs, there may be "
            "discrepancies about exactly when a change of trend occurred. "
            "The discrepancy gets larger when the chart is scaled "
            "differently."
        )),
        Define(
            term="Arithmetic scaling",
            text="An arithmetically scaled chart plots price in equal price "
                 "increments. Arithmetically scaled charts tend to give "
                 "slower trend change signals, as uptrend lines are violated "
                 "much later.",
        ),
        Define(
            term="Logarithmic scaling",
            text="A logarithmically scaled chart plots price in equal "
                 "proportional increments. Logarithmically scaled charts "
                 "tend to give earlier trend change signals, since uptrend "
                 "lines are violated sooner.",
        ),
        Para(text=(
            "The difference is easiest to feel with two numbers. On an "
            "arithmetic axis the gap from 100 to 110 pesos is the same "
            "height as the gap from 200 to 210, because both are ten pesos. "
            "On a logarithmic axis the gap from 100 to 110 is the same "
            "height as the gap from 200 to 220, because both are ten "
            "percent. **Log early, arithmetic late** is the pairing to "
            "remember."
        )),
        Fig(
            panels=(Panel(number="2.8", label="Log scale: the earlier "
                                              "signal."),
                    Panel(number="2.9", label="Arithmetic scale: the later "
                                              "signal.")),
            cols=2, height_mm=50.0,
            caption="One index, one period, two scales, two dates for the "
                    "same change of trend.",
        ),
        Para(text=(
            "Figure 2.8 is an index through a bull market turning into a "
            "bear market, on a logarithmic scale, and Figure 2.9 is the same "
            "index over the same period on an arithmetic one. The only "
            "difference between them is the scale, and the trend change "
            "signal arrives at a different time on each. The next pair "
            "pushes it further. Figure 2.10 shows a stock that looks like it "
            "is flattening out, which the book reads as more bearish, and "
            "Figure 2.11 shows the same stock over the same period looking "
            "like a stronger and steadier uptrend."
        )),
        Fig(
            panels=(Panel(number="2.10", label="Flattening, on a log "
                                               "chart."),
                    Panel(number="2.11", label="Not flattening, on an "
                                               "arithmetic chart.")),
            cols=2, height_mm=50.0,
            caption="The same company over the same period, read two ways.",
        ),
        Para(text=(
            "The chapter's conclusion is a concession rather than a rule: "
            "sometimes it is hard to decide which scaling to use, and an "
            "analyst who habitually uses one may interpret price action "
            "differently from an analyst who habitually uses the other. Same "
            "prices, same period, different conclusion. **Chapter 1 called "
            "that subjectivity, and here it is inside Dow Theory.** When you "
            "hand in chart work for this course, say which scale you used."
        )),
    ),
)


# ==========================================================================
# Section 4 - The secondary reaction and the minor trend
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="The Secondary Reaction and the Minor Trend",
    standfirst="How far back a reaction usually comes, the moment it stops "
               "being a reaction, and the one small formation the theory "
               "lets you trade.",
    blocks=(
        Head(number="4.1", text="The secondary reaction"),
        Define(
            term="Secondary reaction",
            text="The secondary trend, also called the secondary reaction, "
                 "moves in the opposite direction of the existing primary "
                 "trend. It usually lasts from weeks to approximately three "
                 "months, and frequently slightly longer.",
        ),
        Para(text=(
            "It only exists relative to a primary trend, which is why it is "
            "called a reaction: it reacts against something. The chapter's "
            "own analogy calls it the waves on the tides."
            "\n\n"
            "Its depth is the number most often asked for. The secondary "
            "reaction usually retraces from one third to two thirds of the "
            "primary trend's range. Any retracement or correction beyond two "
            "thirds on high volume usually signifies that the secondary "
            "reaction may in fact be a new primary bear market. Note both "
            "halves of that sentence: the depth **and** the volume. Dow "
            "Theory also stresses the importance and psychological "
            "significance of the 50 percent retracement level, a view shared "
            "by another prominent technician, W. D. Gann. The book does not "
            "explain why half should matter; it says the significance is "
            "psychological and leaves it there."
        )),
        Fig(
            panels=(Panel(number="E"),), kind="chart", height_mm=57.0,
            caption="One advance, the reaction against it, and the three "
                    "fractions measured from the top.",
        ),
        Para(text=(
            "Chart E draws the three levels where the chapter puts them, "
            "measured down from the top of the advance rather than up from "
            "the bottom. A market that has run from 4,000 to 5,200 and falls "
            "back to 4,400 has given back two thirds of its advance."
        )),
        Para(text=(
            "A reaction ends the way everything else in this theory ends, by "
            "penetration. A primary bull trend resumes its uptrend once "
            "price breaches the highest peak formed by the secondary "
            "reaction, and a primary bear trend resumes its downtrend once "
            "price breaches the lowest trough formed by the secondary "
            "reaction."
        )),
        Fig(
            panels=(Panel(number="2.12", label="A 75 percent reaction, and "
                                               "the resumption."),
                    Panel(number="2.13", label="Reactions of several depths "
                                               "on one chart.")),
            cols=2, height_mm=52.0,
            caption="Why the secondary reaction earns the description "
                    "deceptive.",
        ),
        Para(text=(
            "Figure 2.12 is the reason Rhea called this movement the most "
            "deceptive of the three. The reaction retraced about 75 percent, "
            "which is past the two thirds guide, and it was still only a "
            "secondary reaction: the primary bull market resumed as soon as "
            "price breached the highest peak the reaction had formed. "
            "**Depth alone does not settle what a move is.** Figure 2.13 "
            "marks several reactions of different depths on one currency "
            "chart, and standing at the right hand edge of any of them there "
            "was no way to tell which was which."
        )),
        SelfCheck(text=(
            "A primary bull trend runs from 4,000 to 5,200 and price falls "
            "to 4,300. Is that within the usual range for a secondary "
            "reaction, and what else would you want to know?"
        )),

        Head(number="4.2", text="The minor trend, and lines"),
        Define(
            term="Minor trend",
            text="Minor trends usually last from days to weeks. Under Dow "
                 "Theory the day's erratic fluctuations represent market "
                 "noise, and no investment decision should be based on such "
                 "activity, with the exception of lines being formed.",
        ),
        Quote(
            text="The stock market is not logical in its movements from day "
                 "to day.",
            source="William P. Hamilton, The Stock Market Barometer, quoted "
                   "in Lim, The Handbook of Technical Analysis",
        ),
        Para(text=(
            "That sentence is the whole justification for ignoring the minor "
            "trend, and it is worth sitting with, because almost all "
            "financial news is about the minor trend. A share closing up 40 "
            "centavos on Tuesday and down 30 on Wednesday is, in this "
            "theory, noise."
            "\n\n"
            "The exception at the end of the definition is the one thing in "
            "this chapter that is small and still tradable."
        )),
        Define(
            term="Line",
            text="Lines are narrow horizontal ranging formations on the "
                 "daily chart. They are usually formed in anticipation of "
                 "some significant news or economic announcement, and these "
                 "narrow consolidations usually result in strong breakouts.",
        ),
        Para(text=(
            "A line here is not a line anybody draws. It is a stretch of "
            "flat price: the market stops going anywhere, often while it "
            "waits for an announcement, and then leaves the range sharply. "
            "Dow Theory recognizes lines as potentially profitable "
            "formations even though they are essentially minor trends, and "
            "**a line is the only tradable formation under Dow Theory other "
            "than inflection point breakouts in the primary trend.** That is "
            "the complete list of what this theory lets you trade: the "
            "primary trend, and lines."
        )),
        Fig(
            panels=(Panel(number="2.14"),), cols=1, height_mm=58.0,
            caption="A narrow range of 106 days, and the breakout out of it.",
        ),
        Para(text=(
            "Figure 2.14 gives the scale. The range lasted 106 days and "
            "spanned about 4.2 percent of the midrange price, which is very "
            "flat for a currency over that length of time, and the breakout "
            "out of it is correspondingly decisive."
        )),
    ),
)


# ==========================================================================
# Section 5 - Three phases, and when a trend reverses
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="Three Phases, and When a Trend Reverses",
    standfirst="The three phases every primary trend passes through, who is "
               "buying in each of them, and the three formations that say a "
               "trend has turned.",
    blocks=(
        Head(number="5.1", text="The three phases of a primary trend"),
        Para(text=(
            "The third tenet says that **primary** trends have three phases. "
            "It does not say all trends do. The three are the accumulation "
            "phase, the trending phase and the distribution phase, and the "
            "tenet is really about who is buying rather than about what "
            "price is doing."
        )),
        Define(
            term="Accumulation phase",
            text="Accumulation normally occurs after a deep and rapid "
                 "decline in prices following companies releasing very "
                 "negative data. The uninformed participants are extremely "
                 "bearish and sell at any price available, while the better "
                 "informed start accumulating at extremely cheap prices.",
        ),
        Para(text=(
            "Two groups, opposite behaviour, the same price. That is the "
            "whole of accumulation, and it is why the sentiment around a "
            "market is at its worst exactly where the informed money is "
            "buying. There is nothing mysterious about the uninformed group "
            "here: their information really is worse."
        )),
        Define(
            term="Trending phase",
            text="The trend phase consists of the uptrend and the downtrend "
                 "phase. The uptrend phase is driven by participants "
                 "expecting higher prices after an accumulation.",
        ),
        Para(text=(
            "In the uptrend phase the initial general sentiment tends to be "
            "slightly less bearish, and the public begins to participate as "
            "rising prices become more obvious and more bullish news is "
            "reported. At higher prices, margin debt starts to increase as "
            "the public scrambles to invest in a rapidly rising market. The "
            "uptrend phase tends to last longer than the downtrend phase, "
            "because there is less capital and less unrealized profit at "
            "risk at the lower prices."
            "\n\n"
            "The downtrend phase normally starts to accelerate as more "
            "companies report increasingly bearish news. The uninformed "
            "begin to unload positions, and as prices fall unexpectedly the "
            "public liquidates. Bearish sentiment intensifies as prices sink "
            "to new depths. It tends to be shorter lived than the uptrend "
            "phase, for the mirror image of the same reason: much more "
            "capital and unrealized profit is at risk at the higher prices."
        )),
        Define(
            term="Distribution phase",
            text="Distribution normally occurs after a prolonged and rapid "
                 "rise in prices. The uninformed tend to be extremely "
                 "optimistic, buying whatever is available at any price, a "
                 "state normally referred to as irrational exuberance. The "
                 "smart investors liquidate gradually so as not to drive "
                 "prices down too rapidly.",
        ),
        Para(text=(
            "Note the word gradually. The informed sellers cannot dump "
            "stock, because doing so would spoil their own price, so they "
            "sell into the enthusiasm in a very measured way and keep "
            "selling at the higher prices for as long as the enthusiasm "
            "lasts. **Irrational exuberance is the phrase the book uses for "
            "the crowd at the top**, and margin debt is at extreme levels "
            "while it is happening."
            "\n\n"
            "This also answers a question the chapter sets at the end. "
            "Accumulation and distribution are the same mechanism running in "
            "opposite directions, but they are not the same length: "
            "accumulation normally lasts longer than distribution, because "
            "distribution happens at the top of the market where much more "
            "capital and unrealized profit is at risk. There is more urgency "
            "about getting out than there ever was about getting in."
        )),
        Fig(
            panels=(Panel(number="F"),), kind="chart", height_mm=57.0,
            caption="Accumulation, trend and distribution, drawn at the "
                    "lengths the chapter's claim implies.",
        ),
        Para(text=(
            "Chart F draws the difference in length rather than asserting "
            "it, and marks the breakout out of the base. Figure 2.15 is the "
            "idealized version of the same structure, and the word idealized "
            "in its caption is doing real work: no live chart is that tidy. "
            "Figure 2.16 is a real market example of the same three phases, "
            "and it carries one more claim worth writing down: **the longer "
            "the accumulation or the distribution lasts, the greater will be "
            "its subsequent breakout move.** A year of going nowhere is not "
            "nothing happening. The book gives no formula for this, and you "
            "should not supply one."
        )),
        Fig(
            panels=(Panel(number="2.15", label="The idealized three "
                                               "phases."),
                    Panel(number="2.16", label="The same three phases on a "
                                               "real chart.")),
            cols=2, height_mm=52.0,
            caption="The structure as it is drawn, and the structure as it "
                    "actually appears.",
        ),
        SelfCheck(text=(
            "In what ways is accumulation similar to distribution, and in "
            "what one way is it reliably different?"
        )),

        Head(number="5.2", text="A trend persists until its reversal is "
                                "indicated"),
        Define(
            term="A trend persists until its reversal is indicated",
            text="In Dow Theory a trend is assumed to persist until there is "
                 "evidence to the contrary. Trend changes are identified by "
                 "a penetration of a previous significant peak or trough.",
        ),
        Para(text=(
            "This is the fourth tenet, and it is both why the theory is late "
            "and why it is safe. You do not guess the top. You assume the "
            "trend you can see is still running until a previous significant "
            "peak or trough has been penetrated."
            "\n\n"
            "The chapter states it a second way, using two words it does not "
            "define anywhere in this chapter: unless a prior support or "
            "resistance level is breached, the trend is assumed to be still "
            "intact. **Read those, for now, as the previous trough and the "
            "previous peak**, which is what the chapter's own figures show. "
            "The book defines support and resistance properly in a later "
            "chapter, and there is nothing to be gained by importing a "
            "definition from elsewhere in the meantime."
        )),
        Fig(
            panels=(Panel(number="2.17"),), cols=1, height_mm=58.0,
            caption="A primary bull trend ended by the violation of a prior "
                    "support level.",
        ),
        Para(text=(
            "Figure 2.17 puts the two ideas together on one chart: the three "
            "phases are labelled across it, and the reversal is signalled at "
            "the moment the prior level is breached. That is the moment the "
            "theory changes its mind."
            "\n\n"
            "There are basically three types of reversal formation that "
            "signal a change in the direction of the existing trend: failure "
            "swings, non failure swings, and double tops or bottoms. They "
            "differ in exactly one respect, which is what the second peak "
            "did relative to the first. The term failure swing was first "
            "used by Welles Wilder when describing oscillator swings on the "
            "relative strength index."
        )),
        Define(
            term="Failure swing",
            text="In a top reversal, a failure swing is the variation in "
                 "which the second peak fails to penetrate the previous "
                 "peak. A breach of the prior support then signals a "
                 "potential change in the direction of the trend.",
        ),
        Define(
            term="Double top and double bottom",
            text="A double top is the top reversal variation in which the "
                 "second peak matches the level of the previous peak. A "
                 "double bottom is its mirror image, where the second trough "
                 "matches the level of the previous trough.",
        ),
        Define(
            term="Non failure swing",
            text="In a non failure swing, the second peak succeeds in "
                 "penetrating the previous peak. Because the formation was "
                 "still making a higher peak, more evidence is required, so "
                 "the conclusive sell signal comes at the penetration of the "
                 "second and lower support level rather than the first.",
        ),
        Fig(
            panels=(Panel(number="2.18", label="The three top reversals."),
                    Panel(number="2.19", label="The same three, inverted.")),
            cols=2, height_mm=50.0,
            caption="Failure swing, double top and non failure swing, at a "
                    "top and at a bottom.",
        ),
        Para(text=(
            "Figure 2.18 sets out all three at a top and Figure 2.19 sets "
            "out the same three at a bottom, and the bottom versions work by "
            "exactly the same rationale in reverse. The word failure describes the second "
            "peak, not the trader: it failed to get back to the first one."
            "\n\n"
            "The non failure swing is the one students misread. The "
            "formation was still in the process of making a higher peak, so "
            "more evidence is required to establish that a trend change is "
            "on the way, and the conclusive sell signal is therefore the "
            "penetration of the second and lower support level rather than "
            "the first and higher one. **A stronger looking top needs "
            "stronger evidence before you call it a top.** In practice many "
            "traders scale out of some of the position at the first level "
            "and the rest at the second."
        )),
    ),
)


# ==========================================================================
# Section 6 - Confirmation, volume, and the challenges
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Confirmation, Volume, and the Challenges",
    standfirst="Why one average is not allowed to call a trend on its own, "
               "what volume has to do before a trend counts as healthy, and "
               "the seven arguments the book itself makes against the "
               "theory.",
    blocks=(
        Head(number="6.1", text="The averages must confirm one another"),
        Define(
            term="The averages must confirm one another",
            text="In Dow Theory both the Industrials Average and the "
                 "Railroad Average must extend beyond their secondary peaks "
                 "in order for a trend to be established. The trend in one "
                 "average must be confirmed by the other.",
        ),
        Para(text=(
            "One average moving is not a signal. Two averages moving the "
            "same way is. The mechanism is dating: one average penetrates "
            "its own secondary peak at a moment the book labels T1, the "
            "other penetrates its own later, at T2, and **as far as Dow "
            "Theory is concerned the uptrend was not confirmed until T2.** "
            "The slower average sets the date."
        )),
        Fig(
            panels=(Panel(number="G"),), kind="chart", height_mm=57.0,
            caption="Two averages, and the later of the two moments that "
                    "dates the signal.",
        ),
        Para(text=(
            "Chart G shows the shape with nothing else on it. Cover the "
            "lower panel and the upper one looks like a clean signal at T1; "
            "uncover it and the signal is dated T2. Figure 2.20 is the "
            "book's own schematic of the same thing, with the Industrials "
            "penetrating first and the Railroad Average following, and "
            "Figure 2.21 shows it happening on the two real averages."
        )),
        Fig(
            panels=(Panel(number="2.20", label="The requirement, drawn."),
                    Panel(number="2.21", label="The requirement on the two "
                                               "real averages.")),
            cols=2, height_mm=52.0,
            caption="Confirmation at T2, not at T1.",
        ),
        Define(
            term="Non confirmation",
            text="Non confirmation occurs when a signal in one average is "
                 "not confirmed by the other. A bearish signal that is not "
                 "confirmed is regarded as a bullish indication, and the "
                 "trend may simply resume.",
        ),
        Para(text=(
            "The consequence is counterintuitive and it is the tenet doing "
            "real work rather than merely delaying a trade. In Figure 2.22 "
            "the Industrials give a weak non failure swing sell signal, the "
            "Transportation Average does not confirm it, and the book reads "
            "the non confirmation as a **bullish** indication. The "
            "Industrials then resumed the uptrend."
        )),
        Fig(
            panels=(Panel(number="2.22"),), cols=1, height_mm=58.0,
            caption="A sell signal in one average that the other refused to "
                    "confirm.",
        ),
        Para(text=(
            "The chapter then extends the idea itself: the concept of "
            "confirmation may also be applied to closely correlated markets, "
            "not only to the two averages. Figure 2.23 shows silver "
            "breaching its support while gold does not, and the book offers "
            "two readings of that without choosing between them, adding only "
            "that a penetration of gold's support would generally be bearish "
            "for silver. Figure 2.24 shows a large cap index giving sell "
            "signals that a small cap index does not confirm, which the book "
            "construes as an oversold indication on the larger one. Hold on "
            "to that last pairing, because it comes back as a criticism at "
            "the end of this section."
        )),
        Fig(
            panels=(Panel(number="2.23", label="Two correlated metals "
                                               "disagreeing."),
                    Panel(number="2.24", label="A large cap and a small cap "
                                               "index disagreeing.")),
            cols=2, height_mm=50.0,
            caption="Confirmation applied outside the two averages.",
        ),

        Head(number="6.2", text="Volume must confirm the trend"),
        Define(
            term="Volume must confirm the trend",
            text="In Dow Theory, volume has to increase or expand in the "
                 "direction of the existing trend. If volume does not expand "
                 "in the direction of the existing trend, this is seen as a "
                 "sign of weakness in the trend, and may potentially lead to "
                 "a weakening or reversal of it.",
        ),
        Para(text=(
            "That definition is the answer to the chapter's own review "
            "question about why volume should expand in the direction of the "
            "trend, so it is worth reproducing in those words. The tenet "
            "unpacks into four conditions, and all four say the same thing."
        )),
        Points(
            title="Expanding in the direction of the existing trend means",
            numbered=True,
            items=(
                "In an uptrend, volume should be increasing.",
                "In an uptrend, volume should be decreasing during a "
                "downside retracement.",
                "In a downtrend, volume should be increasing.",
                "In a downtrend, volume should be decreasing during an "
                "upside retracement.",
            ),
        ),
        Para(text=(
            "**Volume grows with the trend and shrinks against it.** If any "
            "one of the four conditions is not met, the existing trend may "
            "be potentially weaker than expected and may lead to a reversal. "
            "Read the hedging words rather than past them: the book says "
            "may, and potentially, and it does not promise a reversal. It "
            "also notes that volume is considered to be a secondary "
            "indicator. Price comes first; volume confirms or fails to "
            "confirm, and it does not lead."
        )),
        Fig(
            panels=(Panel(number="H"),), kind="chart", height_mm=57.0,
            caption="Volume expanding with the trend and easing off against "
                    "it.",
        ),
        Para(text=(
            "Chart H shows the first two conditions on one picture: larger "
            "bars while price advances with the trend, visibly smaller ones "
            "through the stretch where price moves against it. Figure 2.25 "
            "is the same test on a real market, with one area marked where "
            "volume expands in the direction of the primary bull trend and "
            "another where it declines on average through the retracement, "
            "which the book reads as a bullish indication. Figure 2.26 runs "
            "the test period by period across ten numbered stretches of the "
            "same market, and finds the pattern holding in every one."
        )),
        Fig(
            panels=(Panel(number="2.25", label="Volume expanding with a "
                                               "primary bull trend."),
                    Panel(number="2.26", label="The same test, ten periods "
                                               "in a row.")),
            cols=2, height_mm=52.0,
            caption="Volume confirming a trend, once and then repeatedly.",
        ),
        SelfCheck(text=(
            "Prices are rising and volume is falling. What does Dow Theory "
            "say has happened, and what does it stop short of saying?"
        )),

        Head(number="6.3", text="The seven challenges to Dow Theory"),
        Para(text=(
            "The chapter closes by arguing with itself, and it is the most "
            "useful part of it. There are many criticisms of Dow Theory, and "
            "the book sets out seven of the more significant. Two of them "
            "attack Rhea's own assumptions from Section 1."
        )),
        Points(
            title="The book's seven arguments against the theory",
            numbered=True,
            items=(
                "**It is more applicable to the equity markets.** A "
                "commodity trader might wait months or even years for a "
                "signal based on the penetration of a previous peak or "
                "trough, hedgers would have few or no counterparties, and "
                "the capital risk is astronomically high if a stop loss has "
                "to be placed on the motion of the primary trend.",
                "**The primary trend is susceptible to manipulation.** Near "
                "zero interest rates held over extended periods, colossal "
                "stimulus packages and quantitative easing create an "
                "artificially bullish environment, and collective energy "
                "market rigging and the Libor scandal are further evidence "
                "that markets remain open to manipulation.",
                "**The averages are not a true barometer.** The majority of "
                "indices are themselves tradable today and are therefore "
                "open to manipulation. The VIX was meant to reflect fear and "
                "is thwarted by speculative trading in it, and physical gold "
                "is at the mercy of heavy shorting in its exchange traded "
                "funds, futures and options. Such products never existed in "
                "Dow's time.",
                "**Only closing prices are recognized.** This ignores "
                "potentially large intraday ranges and disregards those "
                "price rejection levels entirely. There is also a conceptual "
                "conflict in recognizing the smallest amount required to "
                "close higher or lower while dismissing large day to day "
                "fluctuations as noise.",
                "**The signals on the primary trend are said to be safer.** "
                "This may or may not be true, and detractors argue that such "
                "signals usually occur late in the trend and miss a large "
                "part of it.",
                "**Identifying a new primary trend is hard.** It is "
                "difficult to establish whether a retracement is part of a "
                "secondary reaction or the inception of a new primary trend "
                "in the opposite direction, and investing on the wrong "
                "reading runs a higher risk of losing capital.",
                "**The averages no longer measure what they used to.** The "
                "logic of confirmation was that industry produces goods and "
                "the transports ship them, but the Industrial Average today "
                "holds many companies that produce nothing needing "
                "transport, being involved instead in financial products, "
                "telecommunications and insurance. Many practitioners "
                "therefore prefer confirmation between large cap and smaller "
                "cap indices.",
            ),
        ),
        Para(text=(
            "The sixth of those is the full answer to why the secondary "
            "reaction is more problematic than the primary trend, and the "
            "seventh explains why Figure 2.24 in this section compared two "
            "indices rather than the two averages."
            "\n\n"
            "The chapter's own summary is not a retreat from any of that. "
            "Dow Theory forms the basis for much of technical analysis in "
            "the twenty first century, and although technical analysis has "
            "evolved significantly since Dow's time, many practitioners "
            "still regard the basic application of Dow Theory as one of the "
            "most reliable approaches in determining and confirming the "
            "existence of a trend. The incorporation of market phase and "
            "volume confirmation has significantly affected how investors "
            "and traders participate, more than a century after the theory "
            "was introduced."
        )),

        Head(number="6.4", text="One question this chapter does not answer"),
        Para(text=(
            "The chapter's eighth review question asks for the main "
            "differences between Dow's and Ralph N. Elliott's determination "
            "of a trend. **Chapter 2 never mentions Elliott.** It gives you "
            "Dow's half of the answer, which is that a trend is a sequence "
            "of successively higher or successively lower peaks and troughs, "
            "and it does not give you Elliott's."
            "\n\n"
            "This is worth naming rather than papering over. The book takes "
            "up Elliott's interpretation later, in the chapter on market "
            "phase and again in its own chapter on Elliott wave analysis. "
            "Answer the Dow half now from Section 3, and finish the question "
            "when the course reaches Elliott. Do not fill the gap from "
            "outside the book: this course is assessed on the book."
            "\n\n"
            "The habit is worth carrying into the rest of the course, "
            "because this chapter is full of the same situation on a smaller "
            "scale. Figure 2.1 asks a question the text never answers. "
            "Support and resistance are used in Section 5 and defined "
            "nowhere in this chapter. The 50 percent retracement level is "
            "said to be psychologically significant, with no account of why. "
            "**In each of those places the right answer is to say what the "
            "book says and to mark the edge of it**, rather than to borrow a "
            "tidier answer from somewhere the examiner is not reading."
        )),
    ),
)


# ==========================================================================
# The document
# ==========================================================================

NOTES = LectureNotes(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 2",
    title="Introduction to Dow Theory",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    term="First semester",
    source_note="Chapter scope follows Lim, M. (2016), The Handbook of "
                "Technical Analysis, chapter 2. Figures are reproduced from "
                "that text and remain the publisher's copyright.",
    orientation=(
        "These notes are the record of what Chapter 2 covered, written to be "
        "read on their own. If you were in the room, they are what to revise "
        "from. If you missed the session, they are the session. They follow "
        "the lecture in the same order and split into the same six parts, so "
        "you can move between the slides and these pages without hunting."
        "\n\n"
        "Read them with the chapter's figures beside you. Every term is "
        "defined once, where it first appears, and listed again at the back "
        "with the subsection that defines it. The check yourself boxes are "
        "not assessed; they are there to catch the places where a reader "
        "working alone usually loses the thread. Where the book leaves a "
        "question open or uses a word it has not defined, these notes say so "
        "rather than filling the gap from somewhere else."
    ),
    objectives=(
        "Understand the basic concepts and assumptions of Dow Theory.",
        "Apply the concepts of Dow Theory to forecast potential entry and "
        "exit points in the market.",
        "Identify the strengths and weaknesses of applying Dow Theory.",
        "Explain the importance of price and volume confirmation as a basis "
        "for determining potential market action.",
        "Highlight the current challenges to Dow Theory.",
    ),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6),
    # The summary and the review questions are the book's, and the deck's
    # closing slides are where they are maintained. build_lecture_notes2.py
    # reads them from there and fills these in, so editing the closing slide
    # moves the notes with it. Do not retype them here.
    summary=(),
    review_questions=(),
    sources=(
        "Lim, M. (2016). The Handbook of Technical Analysis. Wiley. "
        "Chapter 2, and the source of every figure here.",
        "Rhea, R. (1994). The Dow Theory. Fraser Publishing Co.",
        "Hamilton, W. P. (2006). The Stock Market Barometer. Cosimo "
        "Classics.",
        "Nelson, S. A. (2007). The ABC of Stock Speculation. Marketplace "
        "Books.",
        "Schannep, J. (2008). Dow Theory for the 21st Century. Wiley.",
    ),
)
