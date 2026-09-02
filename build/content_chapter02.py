"""Chapter 2 content for FIN1209 - Introduction to Dow Theory.

This file is pure data. It carries no drawing code, so the renderers in
deckkit.py are the same ones Chapter 1 uses.

Everything here is written from scratch in teaching language. The only
verbatim text is the two short attributed quotations students should be able
to reproduce: Rhea on the three movements and Hamilton on the daily
fluctuation. Source of the chapter scope is Lim, M. (2016), The Handbook of
Technical Analysis, chapter 2, printed pages 45 to 64, which students have in
the course text.

Two places where the standing rule bites, and how they are handled:

  * The chapter's own review question 8 asks for the differences between
    Dow's and Ralph N. Elliott's determination of a trend. Chapter 2 never
    mentions Elliott. The closing slides name the gap, say where in the book
    Elliott is actually taught, and no check is set on it. This is the same
    move Chapter 1 made for supply side and demand side.

  * Figure 2.1 asks whether the market was discounting information nobody yet
    had, and the book does not answer its own question. The slide asks it and
    leaves it open, and no check rests on it.
"""

from deckkit import (
    Chapter,
    Chart,
    Check,
    Closing,
    Content,
    Figure,
    Question,
    Quote,
    Recap,
    Section,
    Term,
)

Q = Question

# ==========================================================================
# Part 1 - Where Dow Theory came from
# ==========================================================================

PART1 = Section(
    number=1,
    title="Where Dow Theory Came From",
    short="Origins",
    minutes="About 20 minutes",
    covers=(
        "The four men whose writing became Dow Theory, and which one wrote it down.",
        "The three assumptions Robert Rhea built it on.",
        "Why Dow wanted an average of many stocks instead of one.",
    ),
    slides=(
        Content(
            title="What this chapter is for",
            lines=(
                "Dow Theory lays the basic foundation for modern day technical analysis.",
                "Its premises underpin the very study of market action.",
                "The book says they have withstood the test of time.",
            ),
            accent="Almost everything in the rest of this course sits on top of today.",
            notes=(
                "Say this out loud: Chapter 1 was what analysis is. Chapter 2 is the first actual theory.",
                "Promise them the six tenets by name before the session ends. That is the examinable list.",
            ),
        ),
        Term(
            term="Dow Theory",
            plain="A set of basic statements about how markets move, taken from what Charles H. Dow wrote and organized by the people who came after him.",
            example="It is not a formula and there is nothing to compute. It is six statements, and we take them one at a time.",
            formal="Dow Theory is the body of basic premises credited to Charles H. Dow and codified by later writers, which lays the basic foundation for modern day technical analysis.",
            notes=(
                "Warn them now that Dow himself never published anything called Dow Theory.",
                "Ask who has heard of the Dow Jones. Almost every hand goes up. Tell them that is this man.",
            ),
        ),
        Content(
            title="Charles H. Dow",
            lines=(
                "Dow is credited for much of the early work that led to Dow Theory.",
                "His writing was not a book. It was editorials in the Wall Street Journal.",
                "They were published around the beginning of the twentieth century.",
            ),
            accent="Dow wrote the ideas. Other people assembled them into a theory.",
            notes=(
                "Point out that a newspaper column is where this whole subject starts.",
                "Do not linger. The name that matters for the quiz is two slides away.",
            ),
        ),
        Content(
            title="The three who came after him",
            lines=(
                "William P. Hamilton, Dow's successor. Book: The Stock Market Barometer.",
                "S. A. Nelson, a close acquaintance of Dow's. Book: The ABC of Stock Speculation.",
                "Robert Rhea, a student of Hamilton. Book: The Dow Theory.",
            ),
            accent="Nelson was the first person to call the ideas the Dow Theory.",
            notes=(
                "Read the three names and the three books slowly. Tell them the pairing is examinable.",
                "Ask the room which one gave the theory its name before you show them.",
            ),
        ),
        Content(
            title="What each of them actually did",
            lines=(
                "Hamilton carried on developing and organizing Dow's original early writings.",
                "Nelson published a book about Dow's work, and named the theory.",
                "Rhea did the categorizing, the refining and the formal codification.",
            ),
            accent="It was Rhea's work that really developed the theory and laid its foundation.",
            notes=(
                "Land Rhea hard. Every past paper that asks about a proponent has asked about him.",
                "Say the word codification and then say it in plain words: he wrote the rules down as rules.",
            ),
        ),
        Check(
            label="The four proponents",
            questions=(
                Q(
                    stem="Which proponent was responsible for much of the categorizing, refining and formal codification of Dow's basic premises, later laid out in his book The Dow Theory?",
                    options=("William P. Hamilton",
                             "Charles H. Dow",
                             "Robert Rhea",
                             "S. A. Nelson"),
                    answer="C",
                    reason="Rhea, a student of Hamilton, did the codification and wrote The Dow Theory.",
                ),
                Q(
                    stem="Who was the first person to refer to Dow's concepts and ideas as the Dow Theory?",
                    options=("S. A. Nelson",
                             "Robert Rhea",
                             "Charles H. Dow",
                             "William P. Hamilton"),
                    answer="A",
                    reason="Nelson, a close acquaintance, named it in The ABC of Stock Speculation.",
                ),
            ),
        ),
        Content(
            title="Rhea built the theory on three assumptions",
            lines=(
                "1.  The primary trend is not susceptible to manipulation.",
                "2.  The averages discount everything. Price reflects all information.",
                "3.  Dow Theory is not perfect. It will not guarantee profitability.",
            ),
            accent="At most, Rhea said, treat it as a set of guidelines for investing.",
            notes=(
                "These three are the foundation Rhea laid. Number them out loud.",
                "Tell them number one comes back in Part 6, where the book itself argues against it.",
            ),
        ),
        Term(
            term="The primary trend is not susceptible to manipulation",
            plain="Rhea's first assumption. The long movement of a market is too big for anyone to push around, though a shorter stretch of it might be.",
            example="One large buyer can move a small listed company for a week. Rhea's claim is that nobody can hold a whole market up for two years.",
            formal="Rhea's first assumption is that the primary trend is not susceptible to manipulation, although there is a possibility that manipulation could occur over the shorter term.",
            notes=(
                "This assumption is why Dow Theory only trades the primary trend. Say that link out loud.",
                "Flag that the book returns in Part 6 and says this is no longer true. Do not explain why yet.",
            ),
        ),
        Term(
            term="Dow Theory is not perfect",
            plain="Rhea's third assumption. Investing by these principles will not guarantee that you make money.",
            example="The theory can tell you the primary trend is up. It cannot tell you this particular trade will profit.",
            formal="Rhea's third assumption is that Dow Theory itself is not perfect and that investing according to its principles will not guarantee profitability. At most it should be regarded as a set of guidelines for investing.",
            notes=(
                "Say plainly that the man who codified the theory is the one telling you it is fallible.",
                "This is a past paper favourite. The wrong answers all claim the theory is infallible.",
            ),
        ),
        Check(
            label="Rhea's assumptions",
            questions=(
                Q(
                    stem="One of Rhea's basic assumptions was:",
                    options=("The averages do not discount everything",
                             "That Dow Theory itself is perfect",
                             "That the markets are efficient",
                             "The primary trend is not susceptible to manipulation"),
                    answer="D",
                    reason="Rhea's first assumption. Manipulation is possible only over the shorter term.",
                ),
                Q(
                    stem="According to Rhea, Dow Theory should at most be regarded as:",
                    options=("A guaranteed method of making a profit",
                             "A set of guidelines for investing",
                             "A mathematical model of price",
                             "A replacement for fundamental analysis"),
                    answer="B",
                    reason="Rhea's third assumption says the theory is not perfect and guarantees nothing.",
                ),
            ),
        ),
        Content(
            title="1884: eleven stocks",
            lines=(
                "In 1884 Dow published a stock market average of 11 stocks.",
                "He later developed it into a 12 stock Industrial Index and a 20 stock Railroad Average.",
            ),
            accent="He wanted a number for the market, not a number for one company.",
            notes=(
                "The three numbers, 11, 12 and 20, have all appeared as options in past papers.",
                "Ask why he would bother. Take one answer, then show them.",
            ),
        ),
        Term(
            term="A stock market average",
            plain="One number that stands for a group of companies, so you can talk about what the market did rather than what one share did.",
            example="The PSEi is the same idea: one number that moves with thirty listed companies at once.",
            formal="A stock market average is an index of stocks created to better reflect the general action of the markets, instead of gauging market behavior through individual stock action.",
            notes=(
                "Use the PSEi because they have all seen it on the news. Then come straight back to Dow.",
                "Say the word barometer once here. It is coming up in two slides.",
            ),
        ),
        Chart(
            title="One share, and the average of several",
            letter="A",
            shows="Three separate issues drawn as thin lines jumping about, and the bold line that is their average moving far more calmly than any one of them.",
            tier="enrichment",
            notes=(
                "Trace one thin line with a finger and ask what it tells you about the market. Very little.",
                "Then trace the bold one. Say: that is what Dow was trying to build.",
            ),
        ),
        Content(
            title="Why Dow wanted the average",
            lines=(
                "Individual stock action at the time was fairly erratic and open to manipulation.",
                "The index was meant to average out or smooth those erratic price movements.",
                "The action of the averages was meant to act as a barometer of the market environment.",
            ),
            accent="Barometer is the word to hold on to. It reads the weather. It does not make it.",
            notes=(
                "Barometer is Hamilton's own word and the title of his book. Point that out.",
                "Ask what a barometer is for. Somebody will say predicting rain. That is exactly the claim.",
            ),
        ),
        Content(
            title="What those two averages are called now",
            lines=(
                "The 12 stock Industrial Index has gradually evolved into 30 stocks.",
                "It is known today as the Dow Jones Industrial Average.",
                "The Railroad Average is known today as the Dow Jones Transportation Average.",
            ),
            accent="Two averages. In Part 6 they will have to agree with each other.",
            notes=(
                "Say both modern names slowly. Students know the first and have never heard the second.",
                "Do not explain confirmation yet. Just plant that the pair matters.",
            ),
        ),
        Check(
            label="The averages",
            questions=(
                Q(
                    stem="Dow published his first stock market average in 1884. How many stocks were in it?",
                    options=("Eleven",
                             "Twelve",
                             "Twenty",
                             "Thirty"),
                    answer="A",
                    reason="Eleven in 1884. Twelve industrials and twenty railroads came later, and thirty is the modern industrial count.",
                ),
                Q(
                    stem="The Railroad Average is known today as:",
                    options=("The 12 stock Industrial Index",
                             "The Dow Jones Industrial Average",
                             "The Dow Jones Transportation Average",
                             "The 11 stock average of 1884"),
                    answer="C",
                    reason="The Railroad Average became the Dow Jones Transportation Average.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Dow Theory, and that Dow never published it",
            "Dow, Hamilton, Nelson and Rhea, and their three books",
            "Rhea's three assumptions",
            "A stock market average, and why Dow wanted one",
            "The Industrial Average and the Transportation Average",
        ),
        notes=(
            "Ask for the man who codified the theory and the man who named it. Two answers, ten seconds.",
            "Then move. The six tenets are next and they are the spine of the chapter.",
        ),
    ),
)

# ==========================================================================
# Part 2 - The six tenets, and the first one
# ==========================================================================

PART2 = Section(
    number=2,
    title="The Six Tenets, and the First One",
    short="Discounting",
    minutes="About 20 minutes",
    covers=(
        "The six basic tenets of Dow Theory, which is the list the paper asks for.",
        "What it means to say the averages discount everything.",
        "The one price Dow Theory keeps, and everything it throws away.",
    ),
    slides=(
        Content(
            title="The six basic tenets of Dow Theory",
            lines=(
                "1.  The averages discount everything.",
                "2.  The market has three trends.",
                "3.  Primary trends have three phases.",
                "4.  A trend persists until its reversal is indicated.",
                "5.  The averages must confirm one another.",
                "6.  Volume must confirm the trend.",
            ),
            caption="Learn this list. Parts 2 to 6 take them one at a time, in order. There is no gold line on this slide because all six of them matter.",
            notes=(
                "Read all six out loud, numbered. Then read them again. This slide is the chapter.",
                "Point at number three and say the word primary twice. It is the trap in every past paper.",
            ),
        ),
        Content(
            title="And one more rule that is not on the list",
            lines=(
                "In addition to the six basic tenets, only closing prices are recognized in Dow Theory.",
            ),
            accent="Six tenets, plus that. The book states it separately, so we will too.",
            notes=(
                "Say it is a seventh rule that the book deliberately does not number. Do not pretend it is a tenet.",
                "We come back to it properly at the end of this part.",
            ),
        ),
        Check(
            label="The six tenets",
            questions=(
                Q(
                    stem="Pick the statements below that represent the tenets of Dow Theory. I. The averages discount everything. II. The market has three trends. III. All trends have three phases. IV. Volume must confirm the trend.",
                    options=("Only I and III",
                             "Only III and IV",
                             "Only I, II and IV",
                             "All are correct"),
                    answer="C",
                    reason="Statement III overstates it. The tenet is that primary trends have three phases, not all trends.",
                ),
                Q(
                    stem="In addition to the six basic tenets, Dow Theory recognizes:",
                    options=("Only opening prices",
                             "Only the day's high and low",
                             "Both opening and closing prices",
                             "Only closing prices"),
                    answer="D",
                    reason="The book states it separately from the six: only closing prices are recognized.",
                ),
            ),
        ),
        Term(
            term="The averages discount everything",
            plain="The market has already priced in everything anybody knows. What you see is the sum of what every participant did about what they knew.",
            example="By the time good results are on the evening news, the people acting on them have already bought. The price moved before the bulletin.",
            formal="The first tenet: the market is the end result of all participatory action, which represents all information that may be known to the markets.",
            notes=(
                "Ask why the price sometimes falls on good news. Somebody will get close. This is the answer.",
                "Tell them this is the same discounting assumption Chapter 1 introduced, now stated as a tenet.",
            ),
        ),
        Content(
            title="How information gets into the price",
            lines=(
                "The mechanism is participation: somebody puts capital in, or takes it out.",
                "Information nobody acts on has not reached the market at all.",
            ),
            accent="The price is not what people think. It is what they did about what they think.",
            notes=(
                "This is the sentence to write on the board if you write one thing all session.",
                "Ask: if everyone in this room believes a stock is cheap and nobody buys, what happens to the price?",
            ),
        ),
        Content(
            title="Four things discounting does not require",
            lines=(
                "It need not be instantaneous.",
                "It need not be driven by rational participants.",
                "Participants need not act on all information all of the time.",
                "They need not react in the same manner as each other.",
            ),
            accent="This is a much weaker claim than it first sounds, and that is deliberate.",
            notes=(
                "Contrast with the efficient market hypothesis from Chapter 1, which demands all four.",
                "Say plainly: Dow Theory survives irrational, slow, partial and inconsistent participants.",
            ),
        ),
        Term(
            term="Acts of God",
            plain="The one thing the market cannot discount: an event nobody knew was coming.",
            example="An earthquake at nine in the morning is not in yesterday's closing price. Nothing could have put it there.",
            formal="The market discounts everything except acts of God, that is, unexpected events or unknown information. It can still absorb, react and adjust to such shocks fairly rapidly.",
            notes=(
                "Note the second half carefully: it cannot discount the shock, but it adjusts to it quickly.",
                "Ask the room for a local example. A typhoon usually comes up. Take one and move on.",
            ),
        ),
        Figure(
            title="Prices before September 11, 2001",
            number="2.1",
            shows="A daily chart of the Nasdaq 100 index through 2001, with prices already declining ahead of the September 11 event, and the question printed on the chart: is the market discounting unknown information?",
            notes=(
                "Read the book's own question off the chart and then stop. It does not answer it.",
                "Say that plainly: the author asks whether this is discounting or coincidence and leaves it open.",
            ),
        ),
        Figure(
            title="Gold, after the same event",
            number="2.2",
            shows="A daily chart of spot gold around September 2001, with the price adjusting very rapidly once the information is known, annotated as the market discounting all information once it has become known.",
            notes=(
                "This one is the second half of the acts of God definition: the shock cannot be priced in advance, but it is absorbed fast.",
                "Contrast the two figures out loud. One is a question, this one is an illustration.",
            ),
        ),
        Check(
            label="Discounting",
            questions=(
                Q(
                    stem="In Dow Theory, the market discounts everything except:",
                    options=("Company earnings",
                             "Acts of God",
                             "Interest rate changes",
                             "Government policy"),
                    answer="B",
                    reason="Only unexpected events and unknown information escape it, and even those are absorbed quickly.",
                ),
                Q(
                    stem="As far as Dow Theory is concerned:",
                    options=("The market must discount everything instantaneously",
                             "The participants must be rational",
                             "It is not infallible",
                             "All participants must act on all information"),
                    answer="C",
                    reason="Rhea's third assumption. The other three are precisely the requirements Dow Theory does not make.",
                ),
            ),
        ),
        Content(
            title="What the analyst does with that",
            lines=(
                "Price is the ultimate reflection and embodiment of everything that is knowable.",
                "So the technical analyst need not be concerned with the causes of market action.",
                "Only with the effects of the underlying causes.",
            ),
            accent="Effects, not causes. You met that in Chapter 1. Here it is again as a tenet.",
            notes=(
                "Say the phrase effects not causes and make them repeat it. It is on every paper.",
                "Remind them the fundamentalist takes the opposite side of exactly this sentence.",
            ),
        ),
        Term(
            term="Only closing prices are recognized",
            plain="Whatever the price did during the day, Dow Theory uses only the number it finished at.",
            example="A share swings between 96 and 104 pesos and closes at 100. Dow Theory records 100. The eight peso swing is not recorded at all.",
            formal="In Dow Theory only closing prices are recognized: regardless of how large the high and low price excursions may be on any one day, only the final closing price is used.",
            notes=(
                "Do the arithmetic on the board. 96 to 104 is an eight peso range and none of it survives.",
                "Tell them Part 6 lists this as one of the criticisms of the theory, so hold the objection.",
            ),
        ),
        Content(
            title="And the size of the move does not matter",
            lines=(
                "It does not matter how miniscule the amount is.",
                "A close one centavo above yesterday's close is a higher close.",
                "A close one centavo below yesterday's close is a lower close.",
            ),
            accent="The test is the close, and any amount above or below it counts.",
            notes=(
                "Past papers phrase this as a valid breakout being a closing violation. Say that wording once.",
                "Point at the tension: huge intraday swings are noise, one centavo on the close is a signal.",
            ),
        ),
        Chart(
            title="The day's whole excursion, and the one number kept",
            letter="B",
            shows="Each day drawn as the distance its price travelled, with the closing price marked on it and the closes joined; a wide day and a very quiet day are called out, and both count for exactly one closing price.",
            tier="reinforcement",
            notes=(
                "Point at the pale bars first: that is everything Dow Theory throws away.",
                "Then the joined dots: that is the entire record the theory works from.",
            ),
        ),
        Check(
            label="Closing prices",
            questions=(
                Q(
                    stem="A share trades between 96 and 104 pesos during the day and closes at 100. What does Dow Theory record?",
                    options=("The whole range, 96 to 104",
                             "The high and the low, 104 and 96",
                             "The average of the high and the low",
                             "The close, 100"),
                    answer="D",
                    reason="Only the final closing price is used, however large the day's excursion was.",
                ),
                Q(
                    stem="Under Dow Theory, a close one centavo above the previous close is:",
                    options=("Too small to count",
                             "A higher close",
                             "Counted only if volume expands",
                             "Counted only on a weekly chart"),
                    answer="B",
                    reason="It does not matter how miniscule the amount above or below the previous close is.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The six tenets, in order",
            "The averages discount everything",
            "How information reaches a price, and the four things discounting does not require",
            "Acts of God, the one exception",
            "Only closing prices are recognized",
        ),
        notes=(
            "Ask for the six tenets. Accept four and prompt for the rest.",
            "Say we now spend the next two parts on tenet number two alone. It is the biggest one.",
        ),
    ),
)

# ==========================================================================
# Part 3 - Three trends, and the primary one
# ==========================================================================

PART3 = Section(
    number=3,
    title="Three Trends, and the Primary One",
    short="Primary trend",
    minutes="About 35 minutes",
    covers=(
        "The three movements the book says are running at the same time.",
        "What an uptrend actually is, and what ends one.",
        "Why the signal always arrives late, and why Dow was content with that.",
    ),
    slides=(
        Term(
            term="The market has three trends",
            plain="At any moment the market is doing three things at once: a long movement, a shorter movement against it, and daily noise.",
            example="The ocean does all three at the same time as well. That is the picture Rhea used, and we will use it too.",
            formal="The second tenet of Dow Theory is that the market comprises three trends: the primary trend, the secondary reaction and the minor trend.",
            notes=(
                "Say at once twice. Students expect the three to take turns and they do not.",
                "Tell them this tenet takes the whole of this part and the whole of the next one.",
            ),
        ),
        Quote(
            text="There are three movements of the averages, all of which may be in progress at one and the same time.",
            source="Robert Rhea, The Dow Theory, quoted in Lim, The Handbook of Technical Analysis",
            takeaway="All three at once. Not one after the other.",
            notes=(
                "Read it once, then read only the last eight words again.",
                "This is one of two sentences in the chapter worth memorising word for word.",
            ),
        ),
        Content(
            title="The three, named",
            lines=(
                "1.  Primary trend, the major trend. Months to years. Long term.",
                "2.  Secondary reaction, the intermediate trend. Weeks to months. Medium term.",
                "3.  Minor trend. Days to weeks. Short term.",
            ),
            accent="Rhea called the primary the most important and the secondary the most deceptive.",
            notes=(
                "Read the three durations out loud. Every past paper has tested one of them.",
                "Write the word deceptive next to the secondary. Part 4 explains why.",
            ),
        ),
        Content(
            title="Tides, waves and ripples",
            lines=(
                "The primary trend is sometimes called the tides of the ocean.",
                "The secondary reaction is the waves on the tides.",
                "The minor trend is the ripples on the waves.",
            ),
            accent="A ripple never tells you whether the tide is coming in or going out.",
            notes=(
                "This is the analogy students remember a year later. Spend twenty seconds on it, not two minutes.",
                "Ask which of the three you would want to know about if you were mooring a boat.",
            ),
        ),
        Chart(
            title="All three, on one line",
            letter="C",
            shows="One price line carrying all three trends at the same time: an arrow along the long movement, a shaded stretch where price moves against it, and a callout on the day to day fluctuation.",
            tier="core",
            notes=(
                "Trace the arrow, then the shaded block, then one small wiggle. Three fingers, one line.",
                "Land it: nothing on this chart happened at a different time from anything else.",
            ),
        ),
        Figure(
            title="All three trends on one index",
            number="2.3",
            shows="A daily chart of the NYSE Composite Index with the primary trend, a secondary reaction and the minor trends all labelled on the same price action, and the primary trend resuming on a breakout of the secondary peak.",
            notes=(
                "Make them find the secondary reaction before you point at it.",
                "Note the resumption label on the right. We come back to it in Part 4.",
            ),
        ),
        Check(
            label="The three trends",
            questions=(
                Q(
                    stem="In Dow Theory, the three trends:",
                    options=("Take turns, one at a time",
                             "May all be in progress at one and the same time",
                             "Are all of equal importance",
                             "Appear only on weekly charts"),
                    answer="B",
                    reason="Rhea's own words. All three movements may be running together.",
                ),
                Q(
                    stem="Which trend does Dow Theory call the most deceptive?",
                    options=("The primary trend",
                             "The minor trend",
                             "The secondary reaction",
                             "None of them is called deceptive"),
                    answer="C",
                    reason="Rhea calls the secondary reaction the second and most deceptive movement.",
                ),
            ),
        ),
        Term(
            term="Primary trend",
            plain="The long movement, and the biggest one on the chart. Normally months to years.",
            example="A share that goes from 40 pesos to 140 pesos over three years is in a primary bull trend, whatever it did in any given week.",
            formal="The primary or major trend is the largest trend, normally expected to last from months to years, and the one Rhea held to be a more reliable barometer for investment decisions.",
            notes=(
                "Link back to Rhea's first assumption: it is reliable because it cannot be manipulated.",
                "Say that every trading decision in this theory is made on this trend and no other.",
            ),
        ),
        Content(
            title="Two kinds of primary trend",
            lines=(
                "Primary bull trend, which is a bull market.",
                "Primary bear trend, which is a bear market.",
            ),
            accent="Rhea also said it is very difficult to forecast the extent or the duration of either.",
            notes=(
                "The accent line matters: the theory names the trend, it does not size it.",
                "Ask what use a trend is if you cannot say how far it goes. Let the question sit.",
            ),
        ),
        Term(
            term="Uptrend",
            plain="Price makes a high, falls back to a low above the last low, then makes a high above the last high. Then it does it again.",
            example="Peaks at 104, 116 and 128 pesos, with troughs at 98, 108 and 119 between them. Every peak beats the last peak and every trough beats the last trough.",
            formal="In Dow Theory, an uptrend is defined primarily as successively higher peaks and troughs.",
            notes=(
                "Read the six numbers out slowly and let them check the pattern themselves.",
                "Stress the word primarily. The chapter says there is a second way to define it and they can disagree.",
            ),
        ),
        Term(
            term="Downtrend",
            plain="The same thing upside down. Each peak lower than the last, and each trough lower than the last.",
            example="Peaks at 128, 116 and 104 pesos, with troughs at 119, 108 and 98 between them.",
            formal="In Dow Theory, a downtrend is defined as successively lower peaks and troughs.",
            notes=(
                "Same numbers, read backwards. Say so, it saves a minute.",
                "Ask what a market doing neither looks like. Somebody will describe a line, which is Part 4.",
            ),
        ),
        Chart(
            title="An uptrend, drawn as its own definition",
            letter="D",
            shows="A rising price line with every peak and every trough marked and labelled higher than the one before it, and then the first lower peak marked in gold.",
            tier="core",
            notes=(
                "Walk the dots left to right, saying higher, higher, higher. Then stop dead on the gold one.",
                "Ask what changed. Nothing about the company changed. The sequence changed.",
            ),
        ),
        Figure(
            title="An uptrend, and its first lower high",
            number="2.4",
            shows="A rising price with successive higher highs and higher lows labelled HH and HL, the appearance of the first lower high circled, and the note that the uptrend has technically ended.",
            notes=(
                "Read the book's own words off the figure: the uptrend has technically ended.",
                "Point at the word technically. The price is still high. The definition is what failed.",
            ),
        ),
        Content(
            title="What the first lower peak means",
            lines=(
                "The appearance of a lower high in an uptrend may be an early indication that the uptrend is coming to an end.",
                "Nothing else had to change. The sequence changed.",
            ),
            accent="A trend is a sequence of points, so a trend ends when the sequence breaks.",
            notes=(
                "Note the word may. The book does not say the trend has certainly ended.",
                "This is the whole of tenet four in miniature. We do it properly in Part 5.",
            ),
        ),
        Check(
            label="Uptrend and downtrend",
            questions=(
                Q(
                    stem="In Dow Theory, an uptrend is defined primarily as:",
                    options=("A rise of more than twenty percent",
                             "A close above the previous close for three days",
                             "Successively higher peaks and troughs",
                             "Any advance lasting more than three weeks"),
                    answer="C",
                    reason="The definition is the sequence of peaks and troughs, not a size or a duration.",
                ),
                Q(
                    stem="An uptrend has run 104, 98, 116, 108, 128, 119, 141, 128, and now makes a peak at 134. What has just happened?",
                    options=("The trend has made another higher peak",
                             "The trend has made a lower trough",
                             "Nothing Dow Theory takes any notice of",
                             "The first lower peak has appeared"),
                    answer="D",
                    reason="134 is below the previous peak of 141, so the uptrend has technically ended.",
                ),
            ),
        ),
        Term(
            term="Penetration",
            plain="Price going through a previous peak or a previous trough. That is the event Dow Theory watches for.",
            example="The last peak was 141 pesos. Price closes at 143. The peak has been penetrated.",
            formal="In Dow Theory, an indication of a trend continuation or reversal is signaled by the penetration of a previous peak or trough.",
            notes=(
                "Say the word closes in the example on purpose. Penetration is judged on the close.",
                "This is the single most examined sentence in the chapter. Repeat it.",
            ),
        ),
        Content(
            title="The price of waiting for it",
            lines=(
                "One of the main criticisms of Dow Theory is that its buy and sell signals arrive too late.",
                "They usually miss out on one third or more of the entire trend.",
            ),
            accent="You buy after the bottom, and you sell after the top. Always.",
            notes=(
                "One third or more is a number they should write down. It is asked directly.",
                "Ask whether they would accept that trade. Some will say no. That is the right instinct to have.",
            ),
        ),
        Content(
            title="Dow thought the trade was worth it",
            lines=(
                "It is more important to participate once the trend has been confirmed.",
                "Losing some potential profit for the added safety of a confirmed trend is well worth the sacrifice.",
            ),
            accent="That is Dow's own position. The book reports it as his, not as a fact.",
            notes=(
                "Be careful here. The book states this as Dow's belief. Do not upgrade it to a conclusion.",
                "Say Part 6 gives them the arguments on the other side.",
            ),
        ),
        Figure(
            title="Where the buy and the sell signals fall",
            number="2.5",
            shows="An idealized primary trend with the buy signal marked well above the low and the sell signal well below the high, and the profit potential based on Dow's signals shaded against the maximum profit potential.",
            notes=(
                "Point at the gap at the bottom and the gap at the top. That is the one third being given away.",
                "Ask which of the two blocks they would rather have. Then say nobody gets the bigger one.",
            ),
        ),
        Content(
            title="What Dow Theory says you may trade",
            lines=(
                "All investment and trading decisions are based strictly on the primary trend alone.",
                "The one exception is trading lines, which form out of the daily price fluctuations.",
            ),
            accent="Two tradable things in the whole theory. We meet the second one in Part 4.",
            notes=(
                "Say strictly. The theory is unusually restrictive and students find that surprising.",
                "Do not define a line yet. Just promise it.",
            ),
        ),
        Check(
            label="Signals on the primary trend",
            questions=(
                Q(
                    stem="In Dow Theory, buy and sell signals are indicated by:",
                    options=("The penetration of a previous peak or trough in the primary trend",
                             "Retracements exceeding twenty percent of the primary trend's range",
                             "The primary trend lasting more than one year",
                             "A close above the day's opening price"),
                    answer="A",
                    reason="Penetration of a previous peak or trough is the signal, and it is judged on the close.",
                ),
                Q(
                    stem="Critics say Dow Theory's signals usually miss:",
                    options=("The whole of the trend",
                             "One third or more of the entire trend",
                             "Only the first week of the trend",
                             "Nothing that can be measured"),
                    answer="B",
                    reason="Waiting for confirmation costs one third or more of the move, which Dow accepted.",
                ),
            ),
        ),
        Figure(
            title="A primary bull trend that ran twelve years",
            number="2.6",
            shows="A long term chart of gold labelled as a primary bull trend lasting approximately twelve years.",
            notes=(
                "Say twelve years out loud and let it land. This is what months to years really means.",
                "Ask how many secondary reactions are inside it. The honest answer is many.",
            ),
        ),
        Figure(
            title="A primary bear trend that ran twenty three years",
            number="2.7",
            shows="A long term chart of the 30 year Treasury bond yield labelled as a primary bear trend lasting approximately twenty three years.",
            notes=(
                "Twenty three years is longer than most of the room has been alive. Say that.",
                "Then say the obvious problem out loud: a stop loss on that trend is not a real trade.",
            ),
        ),
        Content(
            title="Two ways to define a trend, and they can disagree",
            lines=(
                "One way is the sequence of rising or falling peaks and troughs, which is the definition we just learned.",
                "The other way is a trendline violation.",
            ),
            accent="The book says the two may date a change of trend differently.",
            notes=(
                "This is the chapter admitting its own definition is not the only one in use.",
                "The next four slides show what that costs, using the same prices twice.",
            ),
        ),
        Term(
            term="Arithmetic scaling",
            plain="A price axis where equal distances up the page mean equal amounts of money.",
            example="The gap from 100 to 110 pesos is exactly the same height as the gap from 200 to 210 pesos.",
            formal="An arithmetically scaled chart plots price in equal price increments. Arithmetically scaled charts tend to give slower trend change signals, as uptrend lines are violated much later.",
            notes=(
                "Draw the two gaps in the air with your hands. Same height, same ten pesos.",
                "Slower signal is the phrase to remember, and it is the one that gets asked.",
            ),
        ),
        Term(
            term="Logarithmic scaling",
            plain="A price axis where equal distances up the page mean equal percentage moves.",
            example="The gap from 100 to 110 pesos is the same height as the gap from 200 to 220 pesos, because both are ten percent.",
            formal="A logarithmically scaled chart plots price in equal proportional increments. Logarithmically scaled charts tend to give earlier trend change signals, since uptrend lines are violated sooner.",
            notes=(
                "Same two gaps, different arithmetic. Ten pesos on 200 is only five percent, so it is half the height.",
                "Earlier signal. Pair it with the previous slide out loud: log early, arithmetic late.",
            ),
        ),
        Figure(
            title="Log scaling, the earlier signal",
            number="2.8",
            shows="A logarithmically scaled chart of the Nasdaq 100 index through a bull market turning into a bear market, annotated with an earlier trend change signal.",
            notes=(
                "Name the scale before you name what happened. The scale is the subject here.",
                "Hold this image in mind. The next slide is the same prices.",
            ),
        ),
        Figure(
            title="Arithmetic scaling, the later signal",
            number="2.9",
            shows="The same Nasdaq 100 index over the same period on an arithmetic scale, annotated with a slower trend change signal.",
            notes=(
                "Same index, same dates, same closes. Say all three.",
                "Ask which analyst got out first, and then ask which one was right.",
            ),
        ),
        Figure(
            title="One stock, flattening out",
            number="2.10",
            shows="A logarithmically scaled chart of Apple Inc. where the advance appears to be flattening out, which the book reads as more bearish behaviour.",
            notes=(
                "The word on the chart is flattening. That is the reading this scale produces.",
                "One more slide and they will see the same stock refuse to flatten.",
            ),
        ),
        Figure(
            title="The same stock, not flattening",
            number="2.11",
            shows="The same period of Apple Inc. on an arithmetic scale, where the same price action appears as a stronger and steadier uptrend.",
            notes=(
                "Put 2.10 and 2.11 side by side in their heads. Same company, same period, opposite conclusion.",
                "This is Chapter 1's subjectivity argument arriving inside Dow Theory.",
            ),
        ),
        Content(
            title="Two analysts, two habits, two readings",
            lines=(
                "Sometimes it is hard to decide which scaling to use.",
                "An analyst who always uses log charts may read the same price differently from one who always uses arithmetic charts.",
            ),
            accent="Same prices, same period, different conclusion. Chapter 1 called that subjectivity.",
            notes=(
                "Do not resolve it. The book does not resolve it either.",
                "Tell them to state their scaling when they hand in Homework 1. It is part of the answer.",
            ),
        ),
        Check(
            label="Scaling",
            questions=(
                Q(
                    stem="Logarithmically scaled charts tend to give:",
                    options=("Earlier trend change signals",
                             "Later trend change signals",
                             "Exactly the same signals as arithmetic charts",
                             "No trend change signals at all"),
                    answer="A",
                    reason="Uptrend lines are violated sooner on a log scale, so the signal comes earlier.",
                ),
                Q(
                    stem="On a logarithmic price axis, equal vertical distances represent:",
                    options=("Equal amounts of pesos",
                             "Equal numbers of trading days",
                             "Equal percentage moves",
                             "Equal volumes traded"),
                    answer="C",
                    reason="Log scaling is proportional, so 100 to 110 and 200 to 220 are the same height.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The three trends, and that they run together",
            "The primary trend, and its two kinds",
            "Uptrend and downtrend, as sequences of peaks and troughs",
            "Penetration, and why the signal is always late",
            "Arithmetic and logarithmic scaling, and the two readings they produce",
        ),
        notes=(
            "Ask for the definition of an uptrend. You want the words peaks and troughs back.",
            "Say the next part finishes tenet two: the other two trends, and the only small thing you may trade.",
        ),
    ),
)

# ==========================================================================
# Part 4 - The secondary reaction and the minor trend
# ==========================================================================

PART4 = Section(
    number=4,
    title="The Secondary Reaction and the Minor Trend",
    short="Secondary and minor",
    minutes="About 25 minutes",
    covers=(
        "How far back a reaction against the primary trend usually comes.",
        "The moment a reaction stops being a reaction.",
        "The one small formation Dow Theory says you are allowed to trade.",
    ),
    slides=(
        Term(
            term="Secondary reaction",
            plain="A move against the primary trend that is big enough to notice but not big enough to be a new primary trend.",
            example="A market that has run from 4,000 to 5,200 and falls back to 4,400 is in a secondary reaction, not a bear market.",
            formal="The secondary trend, also called the secondary reaction, moves in the opposite direction of the existing primary trend. It usually lasts from weeks to approximately three months, and frequently slightly longer.",
            notes=(
                "Say the word reaction. It reacts against something, so it only exists relative to a primary trend.",
                "The duration, weeks to about three months, is directly examinable.",
            ),
        ),
        Content(
            title="How far back a reaction usually comes",
            lines=(
                "The secondary reaction usually retraces from one third to two thirds of the primary trend's range.",
                "Any retracement beyond two thirds on high volume usually signifies it may in fact be a new primary bear market.",
            ),
            accent="One third to two thirds is normal. Past two thirds, start worrying.",
            notes=(
                "One third to two thirds is the single most asked number in this chapter. Write it up.",
                "Note the words on high volume. The depth alone is not the whole test.",
            ),
        ),
        Content(
            title="And the level in the middle",
            lines=(
                "Dow Theory stresses the importance and psychological significance of the 50 percent retracement level.",
                "It is a view shared by another prominent technician, W. D. Gann.",
            ),
            accent="Half back is the level people watch, and the book says so plainly.",
            notes=(
                "Gann gets a whole chapter later in the book. Here he is just a second opinion.",
                "The book does not say why half matters. It says it is psychological. Leave it there.",
            ),
        ),
        Chart(
            title="How far back a reaction comes",
            letter="E",
            shows="One advance with the reaction against it shaded, and the one third, one half and two thirds levels drawn across the chart, all measured down from the top of the advance.",
            tier="core",
            notes=(
                "Point at the top of the advance and say the fractions are measured from here, not from zero.",
                "Then run a finger down to where the reaction stopped. Ask the room which line it landed on.",
            ),
        ),
        Check(
            label="How deep a reaction goes",
            questions=(
                Q(
                    stem="In Dow Theory, the secondary trend:",
                    options=("Moves in the direction of the primary trend",
                             "Lasts from months to years",
                             "Normally retraces from one third to two thirds of the primary trend's range",
                             "Is always accompanied by very low volume"),
                    answer="C",
                    reason="It moves against the primary trend, lasts weeks to about three months, and retraces one to two thirds.",
                ),
                Q(
                    stem="A retracement that goes beyond two thirds on high volume usually signifies:",
                    options=("A deeper than usual secondary reaction",
                             "That the minor trend has taken over",
                             "That volume has stopped confirming",
                             "That it may in fact be a new primary bear market"),
                    answer="D",
                    reason="Past two thirds on high volume, the book stops calling it a reaction.",
                ),
            ),
        ),
        Content(
            title="When the primary trend resumes",
            lines=(
                "A primary bull trend resumes its uptrend once price breaches the highest peak formed by the secondary reaction.",
                "A primary bear trend resumes its downtrend once price breaches the lowest trough formed by the secondary reaction.",
            ),
            accent="The reaction is over when the peak it made is taken out.",
            notes=(
                "This is penetration again, applied to the reaction instead of the trend. Say that link.",
                "Make them state the bear market version back to you. It is the same sentence upside down.",
            ),
        ),
        Figure(
            title="A reaction of 75 percent, and the resumption",
            number="2.12",
            shows="The Dow Jones Industrial Average with a secondary reaction retracing about 75 percent of the primary trend's range, and the primary bull market resuming its uptrend on breaching the highest peak formed during the reaction.",
            notes=(
                "Seventy five percent is past two thirds, and it still turned out to be a reaction. Say so.",
                "That is exactly why the book calls the secondary the deceptive movement.",
            ),
        ),
        Figure(
            title="Reactions of several depths on one chart",
            number="2.13",
            shows="A daily chart of the EURUSD with several secondary reactions marked at roughly one third, one half and two thirds retracements.",
            notes=(
                "Walk the three marked reactions in order and read each fraction aloud.",
                "Ask which one they would have called a new trend at the time. Nobody can tell.",
            ),
        ),
        Check(
            label="Resumption",
            questions=(
                Q(
                    stem="A primary bull trend resumes its uptrend once price:",
                    options=("Breaches the highest peak formed by the secondary reaction",
                             "Falls back by less than half of the primary trend's range",
                             "Closes above its own opening price",
                             "Retraces beyond two thirds"),
                    answer="A",
                    reason="The reaction ends when the peak it formed is penetrated.",
                ),
                Q(
                    stem="A reaction retraces about 75 percent, and the primary bull trend then resumes. What does that tell you?",
                    options=("The one third to two thirds guide is a rule with no exceptions",
                             "Depth alone does not settle what a move is",
                             "Retracements are always measured on weekly charts",
                             "The primary trend had already ended"),
                    answer="B",
                    reason="It is why Rhea called the secondary reaction the most deceptive movement.",
                ),
            ),
        ),
        Term(
            term="Minor trend",
            plain="The day to day movement. Dow Theory does not regard it as important.",
            example="A share closes up 40 centavos on Tuesday and down 30 centavos on Wednesday. Dow Theory calls that noise.",
            formal="Minor trends usually last from days to weeks. Under Dow Theory the day's erratic fluctuations represent market noise, and no investment decision should be based on such activity, with the exception of lines being formed.",
            notes=(
                "Read the last clause twice. The exception is the whole of the next three slides.",
                "Ask how much of financial news is about the minor trend. Almost all of it.",
            ),
        ),
        Quote(
            text="The stock market is not logical in its movements from day to day.",
            source="William P. Hamilton, The Stock Market Barometer, quoted in Lim, The Handbook of Technical Analysis",
            takeaway="Which is exactly why Dow Theory refuses to trade the daily movement.",
            notes=(
                "The second sentence in this chapter worth memorising word for word.",
                "Ask whether they agree. Most of them will not, which is a useful thing for them to notice.",
            ),
        ),
        Term(
            term="Line",
            plain="A narrow sideways range on the daily chart. The market stops going anywhere for a while.",
            example="Price spends five weeks between 63 and 66 pesos ahead of an announcement, then breaks sharply out of that range.",
            formal="Lines are narrow horizontal ranging formations on the daily chart. They are usually formed in anticipation of some significant news or economic announcement, and these narrow consolidations usually result in strong breakouts.",
            notes=(
                "Line here does not mean a line you draw. It means a stretch of flat price. Say that explicitly.",
                "Students confuse it with a trendline every single year.",
            ),
        ),
        Content(
            title="Why the book lets you trade a line",
            lines=(
                "Dow Theory recognizes lines as potentially profitable formations, even though they are essentially minor trends.",
                "A line is the only tradable formation under Dow Theory other than inflection point breakouts in the primary trend.",
            ),
            accent="So the whole theory gives you two things to trade: the primary trend, and lines.",
            notes=(
                "Count them on two fingers. Two. That is the complete list.",
                "Ask why a narrow range would break out strongly. The answer is on the definition slide: news.",
            ),
        ),
        Figure(
            title="A line, and its breakout",
            number="2.14",
            shows="A daily chart of the GBPUSD with a narrow horizontal range lasting 106 days and spanning about 4.2 percent of the midrange price, and the breakout out of it marked.",
            notes=(
                "Read the two numbers on the chart: 106 days, and a range of about 4.2 percent.",
                "Narrow is relative. Four percent over a hundred days is very flat for a currency.",
            ),
        ),
        Check(
            label="Minor trends and lines",
            questions=(
                Q(
                    stem="Which of the following did Dow consider tradable? I. Primary trend. II. Secondary trend. III. Minor trends. IV. Lines in the market.",
                    options=("Only I and IV",
                             "Only I, II and III",
                             "Only I",
                             "All are correct"),
                    answer="A",
                    reason="The primary trend, and lines. Nothing else is tradable under Dow Theory.",
                ),
                Q(
                    stem="A line is best described as:",
                    options=("A trendline drawn through the lows",
                             "The direction of the primary trend",
                             "A narrow horizontal ranging formation on the daily chart",
                             "The 50 percent retracement level"),
                    answer="C",
                    reason="A line is flat price action, not a line anybody draws on the chart.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The secondary reaction, and how long it lasts",
            "One third to two thirds, and the 50 percent level",
            "When a reaction stops being a reaction",
            "How a primary trend resumes",
            "The minor trend, market noise, and the line",
        ),
        notes=(
            "Ask for the two things Dow Theory lets you trade. You want primary trend and lines.",
            "That finishes tenet two. Next is tenet three, and it is the one about crowds.",
        ),
    ),
)

# ==========================================================================
# Part 5 - Three phases, and when a trend reverses
# ==========================================================================

PART5 = Section(
    number=5,
    title="Three Phases, and When a Trend Reverses",
    short="Phases and reversal",
    minutes="About 30 minutes",
    covers=(
        "The three phases every primary trend passes through, and who is buying in each.",
        "Why one phase always lasts longer than the other.",
        "The three formations that say a trend has turned.",
    ),
    slides=(
        Content(
            title="The third tenet: primary trends have three phases",
            lines=(
                "1.  Accumulation phase.",
                "2.  Trending phase.",
                "3.  Distribution phase.",
            ),
            accent="Primary trends. Not all trends. That distinction is asked directly.",
            notes=(
                "Say primary twice. The paper's wrong answer is always all trends have three phases.",
                "Tell them this tenet is really about who is buying, not about price.",
            ),
        ),
        Term(
            term="Accumulation phase",
            plain="The quiet stretch after a bad fall, where informed buyers pick up shares cheaply from people who have given up.",
            example="A share falls from 180 to 95 pesos on bad results. It then goes nowhere for a year while somebody quietly buys it.",
            formal="Accumulation normally occurs after a deep and rapid decline in prices following companies releasing very negative data. The uninformed participants are extremely bearish and sell at any price available, while the better informed start accumulating at extremely cheap prices.",
            notes=(
                "Two groups, opposite behaviour, same price. Say that out loud.",
                "Ask which group they would rather be in, then ask how they would know.",
            ),
        ),
        Content(
            title="Who is on each side during accumulation",
            lines=(
                "The uninformed participants are usually extremely bearish, selling off whatever shares they have left at any price.",
                "The better informed participants start accumulating shares at extremely cheap prices.",
            ),
            accent="The sentiment is worst exactly where the informed money is buying.",
            notes=(
                "This is the crowd psychology idea Chapter 1 set up, now attached to a phase of a trend.",
                "Do not moralise about the uninformed. Their information really is worse.",
            ),
        ),
        Term(
            term="Trending phase",
            plain="The middle stretch, where the move becomes obvious and the public arrives.",
            example="The share leaves 95 pesos, reaches 140, and only then starts appearing in the news as a good buy.",
            formal="The trend phase consists of the uptrend and the downtrend phase. The uptrend phase is driven by participants expecting higher prices after an accumulation.",
            notes=(
                "The book calls it the trending phase in the list and the trend phase in the prose. Say both.",
                "The trending phase is where most people meet a stock for the first time.",
            ),
        ),
        Content(
            title="The uptrend phase",
            lines=(
                "The initial general sentiment tends to be slightly less bearish.",
                "The public begins to participate as rising prices become obvious and more bullish news is reported.",
                "At higher prices margin debt starts to increase as the public scrambles to invest.",
            ),
            accent="It lasts longer than the downtrend phase, because there is less capital and profit at risk at lower prices.",
            notes=(
                "Margin debt was one of the flow of funds items in Chapter 1. Point at the link.",
                "The accent line is a reason, not a fact to memorise. Make them say the reason back.",
            ),
        ),
        Content(
            title="The downtrend phase",
            lines=(
                "It normally accelerates as more companies report increasingly bearish news.",
                "The uninformed begin to unload, and as prices fall unexpectedly the public liquidates.",
                "Bearish sentiment intensifies as prices sink to new depths.",
            ),
            accent="It is shorter lived than the uptrend phase, because more capital and unrealized profit is at risk at higher prices.",
            notes=(
                "Same reason, opposite direction. Markets fall faster than they rise and this is the book's explanation.",
                "Ask the room whether that matches what they have seen. It usually does.",
            ),
        ),
        Term(
            term="Distribution phase",
            plain="The noisy stretch at the top, where informed holders sell gradually to a crowd that is certain prices will keep rising.",
            example="Everyone is buying the share at 178 pesos and the headlines are all positive. That is when the early buyers are selling to them.",
            formal="Distribution normally occurs after a prolonged and rapid rise in prices. The uninformed tend to be extremely optimistic, buying whatever is available at any price, a state normally referred to as irrational exuberance. The smart investors liquidate gradually so as not to drive prices down too rapidly.",
            notes=(
                "Irrational exuberance is the phrase to underline. It appears in the book and in past papers.",
                "Note the word gradually. Selling fast would spoil their own price, so they cannot.",
            ),
        ),
        Content(
            title="Why accumulation lasts longer than distribution",
            lines=(
                "Accumulation happens at low prices, where less capital and less profit is at risk.",
                "Distribution happens at the top, where much more capital and unrealized profit is at risk.",
                "So there is more urgency to get out than there ever was to get in.",
            ),
            accent="The reason is risk at the price, not sentiment. That is the answer the paper wants.",
            notes=(
                "This is review question 6: in what ways is accumulation similar to distribution.",
                "Similar in mechanism, opposite in direction, different in duration. Give them that sentence.",
            ),
        ),
        Chart(
            title="The three phases, and their relative lengths",
            letter="F",
            shows="One primary bull trend with the accumulation, trending and distribution stretches shaded and named, the first drawn visibly longer than the third, and the breakout out of the base marked.",
            tier="reinforcement",
            notes=(
                "Compare the width of the first block with the width of the third. That difference is the point.",
                "Then point at the breakout mark and say that is the only tradable event on this chart.",
            ),
        ),
        Figure(
            title="The idealized three phases",
            number="2.15",
            shows="A schematic primary bull trend with accumulation at the base, the trending stretch rising out of it, and distribution across the top.",
            notes=(
                "Idealized is the word on the caption. Say it. No real chart looks this tidy.",
                "Have them find each of the three phases before you name them.",
            ),
        ),
        Figure(
            title="The same three phases on a real chart",
            number="2.16",
            shows="A real market example of the three phases of a primary bull trend, with a strong breakout out of the accumulation phase and stronger breakouts marked out of the wider distribution.",
            notes=(
                "Now compare with the idealized one. Ask which phase was hardest to see live.",
                "Point at the label about wider formations giving stronger breakouts. That is the next slide.",
            ),
        ),
        Content(
            title="The longer the base, the bigger the move out of it",
            lines=(
                "The longer the accumulation or the distribution lasts, the greater its subsequent breakout move will be.",
            ),
            accent="A year of going nowhere is not nothing happening. It is the setup.",
            notes=(
                "One sentence, and the book gives no formula for it. Do not supply one.",
                "Ask them to hold this. Chapter 4 is market phase analysis and it starts here.",
            ),
        ),
        Check(
            label="The three phases",
            questions=(
                Q(
                    stem="Under Dow Theory, three phases belong to:",
                    options=("All trends",
                             "Secondary reactions only",
                             "Minor trends only",
                             "Primary trends"),
                    answer="D",
                    reason="The tenet is that primary trends have three phases. Any wider claim is wrong.",
                ),
                Q(
                    stem="The accumulation phase normally lasts longer than the distribution phase because:",
                    options=("There is less capital and profit at risk at the lower prices",
                             "Informed buyers are slower than informed sellers",
                             "Accumulation always follows a bear market",
                             "Volume is lower at the bottom of a market"),
                    answer="A",
                    reason="Distribution happens at the top, where much more capital and unrealized profit is at risk.",
                ),
            ),
        ),
        Check(
            label="Who is buying, and when",
            questions=(
                Q(
                    stem="During accumulation, the uninformed market participants are usually:",
                    options=("Extremely optimistic and buying at any price",
                             "Extremely bearish and selling at any price available",
                             "Absent from the market entirely",
                             "Buying on margin"),
                    answer="B",
                    reason="Accumulation follows very negative data, so the uninformed are selling into it.",
                ),
                Q(
                    stem="The state in which uninformed participants buy up whatever shares are available at any price is normally referred to as:",
                    options=("Market noise",
                             "Non confirmation",
                             "Irrational exuberance",
                             "A secondary reaction"),
                    answer="C",
                    reason="The book uses the phrase for the crowd at the top, during distribution.",
                ),
            ),
        ),
        Term(
            term="A trend persists until its reversal is indicated",
            plain="The fourth tenet. You assume the trend you can see is still running until something tells you it is not.",
            example="A market has been rising for two years. Until a previous significant peak or trough is penetrated, you assume it is still rising.",
            formal="In Dow Theory a trend is assumed to persist until there is evidence to the contrary. Trend changes are identified by a penetration of a previous significant peak or trough.",
            notes=(
                "This tenet is the reason the theory is late and the reason it is safe. Both at once.",
                "Ask what the alternative is. Guessing the top. That is the comparison being made.",
            ),
        ),
        Content(
            title="Until a level is breached, nothing has happened",
            lines=(
                "Unless a prior support or resistance level is breached, the trend is assumed to be still intact.",
                "The book uses those two words here and does not define them in this chapter.",
            ),
            accent="Treat them for now as the previous trough and the previous peak.",
            caption="Chapter 5 is where the book defines support and resistance properly.",
            notes=(
                "Be honest that the chapter borrows two words it has not defined. Do not import a definition.",
                "The working reading, previous trough and previous peak, is what the chapter's own figures show.",
            ),
        ),
        Figure(
            title="A primary bull trend ending on a breach",
            number="2.17",
            shows="A chart of a primary bull trend terminated by a violation of a prior support level, with the accumulation, the trend and the distribution marked and the reversal signalled at the breach.",
            notes=(
                "All three phases are labelled on this one as well. Point at them again, quickly.",
                "Then point at the breach and say that is the moment the theory changes its mind.",
            ),
        ),
        Content(
            title="Three formations that signal a reversal",
            lines=(
                "1.  Failure swings.",
                "2.  Non failure swings.",
                "3.  Double tops and double bottoms.",
            ),
            accent="Three shapes, one question: did the second attempt beat the first one?",
            notes=(
                "The three differ only in what the second peak or trough did. Say that before defining them.",
                "The term failure swing comes from Welles Wilder, describing swings on the RSI indicator.",
            ),
        ),
        Term(
            term="Failure swing",
            plain="The second peak fails to reach the first one. The market tried again and could not get there.",
            example="Price makes a peak at 141 pesos, falls back, then rallies only to 134 and turns down again.",
            formal="In a top reversal, a failure swing is the variation in which the second peak fails to penetrate the previous peak. A breach of the prior support then signals a potential change in the direction of the trend.",
            notes=(
                "The word failure describes the second peak, not the trader. Say that, it prevents confusion.",
                "Bottom version: the second trough fails to reach down to the first one.",
            ),
        ),
        Term(
            term="Non failure swing",
            plain="The second peak does beat the first one, and the market still turns down afterwards.",
            example="Price peaks at 141, falls back, rallies to 146, and then rolls over anyway.",
            formal="In a non failure swing, the second peak succeeds in penetrating the previous peak. Because the formation was still making a higher peak, more evidence is required, so the conclusive sell signal comes at the penetration of the second and lower support level rather than the first.",
            notes=(
                "This is the one students get wrong. The trend looked fine and then failed anyway.",
                "Point out the practical consequence on the next slide before moving on.",
            ),
        ),
        Term(
            term="Double top and double bottom",
            plain="The second attempt matches the first one almost exactly. The market got back to the same level and stopped there twice.",
            example="Price peaks at 141 pesos, falls back, and rallies to 141 again before turning down.",
            formal="A double top is the top reversal variation in which the second peak matches the level of the previous peak. A double bottom is its mirror image, where the second trough matches the level of the previous trough.",
            notes=(
                "Three variations, and this is the middle case: not higher, not lower, the same.",
                "Chapter 13 is chart pattern analysis and it takes double tops much further. Not today.",
            ),
        ),
        Figure(
            title="The three top reversal patterns",
            number="2.18",
            shows="Three schematic top reversals side by side: a failure swing where the second peak does not reach the first, a double top where it matches, and a non failure swing where it exceeds it, each with its sell signal marked.",
            notes=(
                "Read them left to right and name each one. Then cover the labels and ask again.",
                "Point at the two support levels on the non failure swing. That is the next slide.",
            ),
        ),
        Figure(
            title="The three bottom reversal patterns",
            number="2.19",
            shows="The same three formations inverted as bottom reversals, with the buy signal marked on each.",
            notes=(
                "Say the same rationale applies except in reverse, which is the book's own sentence.",
                "Do not spend long here. The room has already seen the argument once.",
            ),
        ),
        Content(
            title="Why the non failure swing needs the lower level",
            lines=(
                "The formation was still in the process of making a higher peak, so more evidence is needed.",
                "The conclusive sell signal is the penetration of the second and lower support level.",
                "Many traders scale out at the first, higher level and finish at the second.",
            ),
            accent="A stronger looking top needs stronger evidence before you call it a top.",
            notes=(
                "Scaling out is the practical answer to the tension. Mention it and move.",
                "Ask which of the three formations gives the earliest signal. The failure swing does.",
            ),
        ),
        Check(
            label="Reversal formations",
            questions=(
                Q(
                    stem="In Dow Theory, a trend is assumed to persist:",
                    options=("For at least three months",
                             "Until there is evidence to the contrary",
                             "Until volume stops expanding",
                             "Until the averages disagree"),
                    answer="B",
                    reason="Trend changes are identified by penetration of a previous significant peak or trough.",
                ),
                Q(
                    stem="A top reversal in which the second peak succeeds in penetrating the previous peak is:",
                    options=("A failure swing",
                             "A double top",
                             "A non failure swing",
                             "A secondary reaction"),
                    answer="C",
                    reason="Fails to reach it is a failure swing, matches it is a double top, exceeds it is a non failure swing.",
                ),
            ),
        ),
        Check(
            label="Where the signal falls",
            questions=(
                Q(
                    stem="The conclusive sell signal on a non failure swing comes at the penetration of:",
                    options=("The first and higher support level",
                             "The second and lower support level",
                             "The previous peak",
                             "The 50 percent retracement level"),
                    answer="B",
                    reason="The formation was still making a higher peak, so more evidence is required.",
                ),
                Q(
                    stem="A top reversal in which the second peak matches the level of the previous peak is:",
                    options=("A double top",
                             "A failure swing",
                             "A non failure swing",
                             "A line"),
                    answer="A",
                    reason="Matching the previous peak is the double top, the middle of the three variations.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The three phases, and that they belong to primary trends",
            "Accumulation, and who is on each side of it",
            "The uptrend and downtrend phases, and why one is longer",
            "Distribution, and irrational exuberance",
            "A trend persists until its reversal is indicated",
            "Failure swings, non failure swings, double tops and bottoms",
        ),
        notes=(
            "Ask for the three formations. Then ask what distinguishes them: the second peak.",
            "One part left, and it holds two tenets and every criticism of the theory.",
        ),
    ),
)

# ==========================================================================
# Part 6 - Confirmation, volume, and the challenges
# ==========================================================================

PART6 = Section(
    number=6,
    title="Confirmation, Volume, and the Challenges",
    short="Confirmation and volume",
    minutes="About 35 minutes",
    covers=(
        "Why one average is not allowed to call a trend on its own.",
        "What volume has to do before a trend counts as healthy.",
        "The seven arguments the book itself makes against Dow Theory.",
    ),
    slides=(
        Term(
            term="The averages must confirm one another",
            plain="The fifth tenet. One average moving is not a signal. Two averages moving the same way is.",
            example="If the Industrials clear their earlier peak in March and the Transportation Average does not clear its own until May, the signal is dated May.",
            formal="In Dow Theory both the Industrials Average and the Railroad Average must extend beyond their secondary peaks in order for a trend to be established. The trend in one average must be confirmed by the other.",
            notes=(
                "Say the modern names too: Industrials and Transportation. The paper uses Railroad.",
                "The word is extend beyond their secondary peaks. Not rise, not rally. Penetrate.",
            ),
        ),
        Content(
            title="The signal is dated by the later average",
            lines=(
                "One average penetrates its secondary peak at a time we will call T1.",
                "The other penetrates its own secondary peak later, at T2.",
                "As far as Dow Theory is concerned, the uptrend was not confirmed until T2.",
            ),
            accent="The slower average sets the date. The faster one on its own proves nothing.",
            notes=(
                "T1 and T2 are the book's own labels on the next two figures. Introduce them here.",
                "Ask what you would have lost between T1 and T2. Some of the move, again.",
            ),
        ),
        Chart(
            title="One average confirming the other",
            letter="G",
            shows="Two stacked price panels, each with its own earlier peak drawn across it; the upper panel penetrates its peak at T1 and the lower panel penetrates its own later, at T2, which is where the signal is dated.",
            tier="core",
            notes=(
                "Cover the lower panel with your hand and ask whether the trend is confirmed. It is not.",
                "Uncover it. The date is T2 and there is nothing to argue about.",
            ),
        ),
        Figure(
            title="Confirmation of the averages",
            number="2.20",
            shows="A schematic of two averages, with the Industrials Average penetrating its secondary peak at T1 and the Railroad Average penetrating its own a little later at T2, at which point the uptrend is confirmed.",
            notes=(
                "This is the definition slide in picture form. Point at T1, then T2, then say confirmed.",
                "Have somebody read the caption out. The book's own words are the safest wording.",
            ),
        ),
        Figure(
            title="The same thing on real averages",
            number="2.21",
            shows="The Dow Jones Industrial Average breaching its secondary peak at T1 and the Dow Jones Transportation Average breaching its own at T2, with the secondary reaction marked on both.",
            notes=(
                "Same shape, real data, two panels. Make them find T2 before you point at it.",
                "Say the confirmation date out loud: the uptrend is confirmed at T2, not at T1.",
            ),
        ),
        Term(
            term="Non confirmation",
            plain="One average gives a signal and the other refuses to. Dow Theory then treats the signal as unproven.",
            example="The Industrials give a sell signal, the Transportation Average does not, and the book reads that as a bullish indication rather than a bearish one.",
            formal="Non confirmation occurs when a signal in one average is not confirmed by the other. A bearish signal that is not confirmed is regarded as a bullish indication, and the trend may simply resume.",
            notes=(
                "The counterintuitive bit: a sell signal nobody confirms is read as bullish. Say it twice.",
                "This is the tenet doing real work, not just delaying a trade.",
            ),
        ),
        Figure(
            title="A sell signal that was not confirmed",
            number="2.22",
            shows="The Dow Jones Industrial Average making a weak non failure swing sell signal with support breached, while the Dow Jones Transportation Average does not breach its own support, after which the Industrials resume the uptrend.",
            notes=(
                "Name the formation on the Industrials: a non failure swing. They met it in Part 5.",
                "Then point at the average below that did not break. That is the whole argument.",
            ),
        ),
        Content(
            title="Confirmation between closely correlated markets",
            lines=(
                "The concept may also be applied to closely correlated markets, not only to the two averages.",
                "Practitioners also compare a large cap index with a small cap index.",
            ),
            accent="The idea is general: one market alone is not evidence.",
            notes=(
                "The book extends this itself, so it is fair game. It uses gold and silver, and two US indices.",
                "Ask the room for a pair of Philippine listings that usually move together.",
            ),
        ),
        Figure(
            title="Two correlated markets disagreeing",
            number="2.23",
            shows="Gold and silver side by side, with silver breaching its support while gold does not, which the book reads as either a bearish signal for gold or a bullish one for silver.",
            notes=(
                "Note that the book offers two readings and does not pick one. Say so plainly.",
                "It does add that a penetration of gold's support would generally be bearish for silver.",
            ),
        ),
        Figure(
            title="A large cap index and a small cap index",
            number="2.24",
            shows="The S&P500 large cap index showing sell signals that the Russell 2000 small cap index does not confirm, which the book construes as an oversold indication on the S&P500.",
            notes=(
                "This pairing comes back in the criticisms, so flag it now: many practitioners prefer it.",
                "Do not go deeper. Oversold is a Chapter 8 word and this chapter does not define it.",
            ),
        ),
        Check(
            label="Confirmation",
            questions=(
                Q(
                    stem="Confirmation of the averages means that:",
                    options=("Both averages must rise by more than twenty percent",
                             "Both the Industrials Average and the Railroad Average must extend beyond their secondary peaks",
                             "Both averages must close higher on the same day",
                             "Both averages must breach their minor peaks"),
                    answer="B",
                    reason="Secondary peaks, and the trend in one average must be confirmed by the other.",
                ),
                Q(
                    stem="One average penetrates its secondary peak at T1 and the other penetrates its own at T2, which is later. When is the uptrend confirmed?",
                    options=("At T1",
                             "Halfway between T1 and T2",
                             "At T2",
                             "It is never confirmed"),
                    answer="C",
                    reason="The later average dates the signal. Until then the move is unconfirmed.",
                ),
            ),
        ),
        Term(
            term="Volume must confirm the trend",
            plain="The sixth tenet. Volume has to grow when price moves with the trend and shrink when it moves against it.",
            example="A share rising on 3 million shares a day and pulling back on 1 million is behaving the way the tenet wants.",
            formal="In Dow Theory, volume has to increase or expand in the direction of the existing trend. If volume does not expand in the direction of the existing trend, this is seen as a sign of weakness in the trend, and may potentially lead to a weakening or reversal of it.",
            notes=(
                "The formal wording is the answer to review question 5, so read it as written.",
                "Expand in the direction of the trend is the phrase. Not simply high volume.",
            ),
        ),
        Content(
            title="The four conditions, in full",
            lines=(
                "1.  In an uptrend, volume should be increasing.",
                "2.  In an uptrend, volume should be decreasing during a downside retracement.",
                "3.  In a downtrend, volume should be increasing.",
                "4.  In a downtrend, volume should be decreasing during an upside retracement.",
            ),
            accent="Volume grows with the trend and shrinks against it. All four say only that.",
            notes=(
                "Read all four. Then say the accent line and let them see that it is one idea, not four.",
                "Past papers quote these four almost word for word, so the wording matters.",
            ),
        ),
        Content(
            title="If any one of the four is not met",
            lines=(
                "The existing trend may be potentially weaker than expected.",
                "That may lead to a reversal in the existing trend.",
            ),
            accent="May, and potentially. The book does not promise a reversal and neither should you.",
            notes=(
                "Point at the hedging words. Students overstate this every year.",
                "Ask what you would do about it. The honest answer is watch more carefully, not sell.",
            ),
        ),
        Content(
            title="And volume is only a secondary indicator",
            lines=(
                "The book notes that volume is considered to be a secondary indicator.",
            ),
            accent="Price first. Volume confirms or fails to confirm. It does not lead.",
            notes=(
                "One line, and it is the sentence that keeps volume in its place.",
                "Chapter 6 is volume and open interest in full. Today it is a confirmation tool.",
            ),
        ),
        Chart(
            title="Volume expanding with the trend, and easing against it",
            letter="H",
            shows="A rising price line above a panel of volume bars, with volume clearly larger while price advances with the trend and clearly smaller through the stretch where price moves against it.",
            tier="core",
            notes=(
                "Do not talk about the price panel. Point only at the bars and let the pattern do the work.",
                "Then ask which of the four conditions this chart shows. It shows the first two.",
            ),
        ),
        Figure(
            title="Volume expanding with a primary bull trend",
            number="2.25",
            shows="A long term chart of gold with volume expanding in the direction of the existing primary bull trend in one marked area, and declining on average during the retracement in another.",
            notes=(
                "Find area A and area B on the chart with them. A is with the trend, B is the retracement.",
                "The book calls this a bullish indication for gold. Report it as the book's reading.",
            ),
        ),
        Figure(
            title="The same test, period by period",
            number="2.26",
            shows="A weekly chart of the GLD SPDR Gold Trust Shares with ten numbered periods, volume expanding with the trend in the odd numbered ones and declining during each correction or retracement.",
            notes=(
                "Ten numbered periods is more than the room needs. Do two of them and move on.",
                "This figure is the first thing to drop if the clock is against you.",
            ),
        ),
        Check(
            label="Volume",
            questions=(
                Q(
                    stem="In Dow Theory, volume confirmation of the existing trend implies that:",
                    options=("In an uptrend, volume should be increasing",
                             "In an uptrend, volume should be increasing during a downside retracement",
                             "In a downtrend, volume should be decreasing",
                             "Volume should increase during accumulation and decrease during distribution"),
                    answer="A",
                    reason="Volume expands with the trend and contracts against it. The other three reverse that.",
                ),
                Q(
                    stem="If volume does not expand in the direction of the existing trend, the book says this is:",
                    options=("Proof that the trend has reversed",
                             "A sign of weakness that may lead to a reversal",
                             "Irrelevant, since volume is a secondary indicator",
                             "A confirmation of the secondary reaction"),
                    answer="B",
                    reason="A sign of weakness, and only potentially a reversal. The book hedges and so should you.",
                ),
            ),
        ),
        Content(
            title="There are many criticisms of Dow Theory",
            lines=(
                "The book lists seven of the more significant arguments against it.",
                "They are the book's own, not ours, and several attack Rhea's assumptions directly.",
            ),
            accent="A textbook that argues with itself is worth reading carefully.",
            notes=(
                "Set this up as the honest part of the chapter. The author is not selling the theory.",
                "Two of the review questions are answered entirely out of the next seven slides.",
            ),
        ),
        Content(
            title="1. It suits the equity markets better than anything else",
            lines=(
                "A commodity trader might wait months or years for a signal on the primary trend.",
                "Hedgers would have few or no counterparties to take the other side.",
                "The capital risk is astronomically high if the stop loss is set by the primary trend.",
            ),
            accent="A twenty three year bear trend is not a trade anybody can actually hold.",
            notes=(
                "Read the accent line and then say stop loss out loud. Twenty three years of it.",
                "This is the criticism about faster markets and lower timeframes.",
            ),
        ),
        Content(
            title="2. The primary trend is susceptible to manipulation",
            lines=(
                "Near zero interest rates over extended periods, colossal stimulus and quantitative easing.",
                "Collective energy market rigging, and the Libor scandal.",
            ),
            accent="This attacks Rhea's first assumption directly, and it is the book making the attack.",
            notes=(
                "Take them back to Part 1 and Rhea's first assumption. The book has just contradicted it.",
                "This is review question 2, give examples of the primary trend being manipulated.",
            ),
        ),
        Content(
            title="3. The averages are not a true barometer any more",
            lines=(
                "Most indices are themselves tradable today, so they are open to manipulation.",
                "The VIX was meant to reflect fear, and heavy speculative trading works against that.",
                "Physical gold is at the mercy of shorting in its ETFs, futures and options.",
            ),
            accent="Such products never existed in Dow's time.",
            notes=(
                "The barometer word from Part 1 comes back here. A barometer you can trade is a strange barometer.",
                "Do not explain the VIX or ETFs beyond what is on the slide. The chapter does not.",
            ),
        ),
        Content(
            title="4. Only closing prices are recognized",
            lines=(
                "Recognizing only the close ignores potentially large intraday ranges.",
                "Those important price rejection levels are totally disregarded.",
            ),
            accent="And there is a conceptual conflict: one centavo on the close counts, a huge swing does not.",
            notes=(
                "This is the objection you told them to hold in Part 2. Give it back to them now.",
                "Price rejection level is a phrase the chapter uses and does not define. Leave it undefined.",
            ),
        ),
        Content(
            title="5. The signals on the primary trend are said to be safer",
            lines=(
                "This may or may not be true.",
                "Detractors argue such signals usually occur late in the trend and miss a large part of it.",
            ),
            accent="Note the wording. The book does not settle this one either way.",
            notes=(
                "Contrast with Dow's own position from Part 3, that the sacrifice is well worth it.",
                "Two positions, both reported, neither endorsed. That is the standard to hold them to.",
            ),
        ),
        Content(
            title="6. Telling a new primary trend from a reaction",
            lines=(
                "It is difficult to establish whether a retracement is part of a secondary reaction.",
                "Or whether it is the inception of a new primary trend in the opposite direction.",
                "Investing on the wrong reading runs a higher risk of losing capital.",
            ),
            accent="This is why the secondary reaction is the most deceptive of the three movements.",
            notes=(
                "This is review question 7 answered in full: why the secondary reaction is more problematic.",
                "Take them back to the 75 percent reaction in Part 4. Nobody could have called it live.",
            ),
        ),
        Content(
            title="7. The two averages no longer measure what they used to",
            lines=(
                "The logic was that industry produces goods and the transports ship them.",
                "But the Industrial Average today holds many companies that produce nothing needing shipping.",
                "Many are in financial products, telecommunications and insurance.",
            ),
            accent="Many practitioners prefer large cap against small cap, such as the S&P500 and the Russell 2000.",
            notes=(
                "The original logic is worth stating: confirmation was an economic argument, not a chart one.",
                "That is why practitioners now pair a large cap index with a small cap one instead.",
            ),
        ),
        Check(
            label="The challenges",
            questions=(
                Q(
                    stem="Which criticism attacks Rhea's first assumption directly?",
                    options=("Only closing prices are recognized",
                             "The signals arrive late in the trend",
                             "The primary trend is susceptible to manipulation",
                             "Dow Theory suits the equity markets best"),
                    answer="C",
                    reason="Rhea assumed the primary trend could not be manipulated. The book now says it can.",
                ),
                Q(
                    stem="Why does the book say confirmation between the Industrials and the Transports has become less effective?",
                    options=("The two averages now hold the same companies",
                             "Many industrial companies no longer produce anything that needs shipping",
                             "The Transportation Average is no longer published",
                             "Transport costs are no longer reported"),
                    answer="B",
                    reason="The original logic was industry producing goods and transport shipping them.",
                ),
            ),
        ),
        Content(
            title="What the book still claims for Dow Theory",
            lines=(
                "Dow Theory forms the basis for much of technical analysis in the twenty first century.",
                "Many practitioners still regard it as one of the most reliable ways to confirm a trend exists.",
                "Market phase and volume confirmation changed how investors participate.",
            ),
            accent="More than a century after it was introduced, and after all seven of those criticisms.",
            notes=(
                "Read the summary as written. The author criticises the theory and still defends it.",
                "This is review question 3: is Dow Theory still relevant in today's market.",
            ),
        ),
        Check(
            label="What survives",
            questions=(
                Q(
                    stem="The book's own summary says Dow Theory is still widely regarded as reliable for:",
                    options=("Forecasting the exact extent of a primary trend",
                             "Timing entries on the minor trend",
                             "Pricing derivatives on the averages",
                             "Determining and confirming that a trend exists"),
                    answer="D",
                    reason="Determining and confirming the existence of a trend, which is the whole claim.",
                ),
                Q(
                    stem="A commodity trader following Dow Theory strictly would most likely complain that:",
                    options=("The theory ignores volume",
                             "A signal on the primary trend can take months or years to arrive",
                             "The theory has too many tenets to apply",
                             "Closing prices are unavailable in commodities"),
                    answer="B",
                    reason="The first criticism: the theory suits equities, and slow signals make hedging impractical.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The averages must confirm one another, and the signal is dated by the later one",
            "Non confirmation, and why an unconfirmed sell signal reads as bullish",
            "Volume must confirm the trend, and the four conditions",
            "Volume is a secondary indicator",
            "The seven criticisms, two of which attack Rhea's own assumptions",
            "What the book still claims for the theory",
        ),
        notes=(
            "Ask for the four volume conditions. Accept two and give them the summary line instead.",
            "That is the whole chapter. Move to the wrap up.",
        ),
    ),
)

# ==========================================================================
# Closing
# ==========================================================================

CLOSING = (
    Content(
        title="Chapter 2 in five sentences",
        lines=(
            "Dow Theory is six tenets, codified by Robert Rhea out of Charles Dow's editorials.",
            "The averages discount everything, and only closing prices are recognized.",
            "Three trends run at once, and only the primary one and lines may be traded.",
            "A primary trend has three phases and persists until a peak or trough is penetrated.",
            "The averages must confirm one another, and volume must confirm the trend.",
        ),
        accent="If you can say those five, you can answer most of what this chapter is asked about.",
        notes=(
            "Read all five slowly. This is the summary students should copy word for word.",
            "Then ask for the six tenets one last time, from the room, with the slide hidden.",
        ),
    ),
    Content(
        title="The review questions to prepare",
        lines=(
            "Describe the basic tenets of Dow Theory.",
            "Give examples of the primary trend being manipulated.",
            "Is Dow Theory still relevant today, and what are its main weaknesses?",
            "Explain why volume should expand in the direction of the existing trend.",
            "In what ways is accumulation similar to distribution?",
            "Why is the secondary reaction more problematic than the primary trend?",
        ),
        accent="Seven of the book's eight questions. The eighth is on the next slide.",
        notes=(
            "Say where each answer sits: Part 2, Part 6, Part 6, Part 6, Part 5, Parts 4 and 6.",
            "Line three carries two of the book's eight questions, so there are seven here, not six.",
            "Set the expectation that these appear on the quiz in the department's four statement format.",
        ),
    ),
    Content(
        title="The one question this chapter does not answer",
        lines=(
            "Review question 8 asks for the differences between Dow's and Ralph N. Elliott's determination of a trend.",
            "Chapter 2 never mentions Elliott. It gives you Dow's half and nothing else.",
            "The book takes up Elliott properly in Chapter 4 and Chapter 18.",
        ),
        accent="Answer the Dow half now, and finish the question when we reach Elliott.",
        caption="Do not fill the gap from outside the book. The paper is set on the book.",
        notes=(
            "Be straight with them: the chapter's own review question runs past the chapter.",
            "Give them Dow's determination of a trend, which is successively higher or lower peaks and troughs.",
            "Say we will not invent Elliott's half today. That is a promise about how this course works.",
        ),
    ),
    Closing(
        title="Next: mechanics and dynamics of charting",
        lines=(
            "Chapter 3 builds the chart itself: open, high, low and close, and how a bar is made.",
            "Bring the closing price with you. Chapter 3 explains the other three you were told to ignore.",
            "Before then: find a chart with a clear trend, mark its peaks and troughs, and say where the trend ended.",
        ),
        accent="FIN1209  Technical Analysis in Investment  |  Institute of Accounts, Business and Finance",
        notes=(
            "Name the exact preparation. That last line is Homework 1 in one sentence.",
            "Remind them quiz 1 covers chapters 1 and 2 together.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 2",
    title="Introduction to Dow Theory",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    objectives=(
        "Understand the basic concepts and assumptions of Dow Theory.",
        "Apply the concepts of Dow Theory to forecast potential entry and exit points in the market.",
        "Identify the strengths and weaknesses of applying Dow Theory.",
        "Explain the importance of price and volume confirmation as a basis for determining potential market action.",
        "Highlight the current challenges to Dow Theory.",
    ),
    roadmap=(
        "Part 1  Where Dow Theory came from",
        "Part 2  The six tenets, and the first one",
        "Part 3  Three trends, and the primary one",
        "Part 4  The secondary reaction and the minor trend",
        "Part 5  Three phases, and when a trend reverses",
        "Part 6  Confirmation, volume, and the challenges",
    ),
    sections=(PART1, PART2, PART3, PART4, PART5, PART6),
    closing=CLOSING,
)
