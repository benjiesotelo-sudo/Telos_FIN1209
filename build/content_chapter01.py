"""Chapter 1 content for FIN1209 - Introduction to the Art and Science of
Technical Analysis.

This file is pure data. It carries no drawing code, so a second chapter is a
second file like this one rather than a rewrite of the builder.

Everything here is written from scratch in teaching language. The only
verbatim text is the handful of short, famous, attributed definitions that
students are expected to be able to quote back: Murphy, Edwards and Magee,
and Pring. Source of the chapter scope is Lim, M. (2016), The Handbook of
Technical Analysis, chapter 1, which students have in the course text.
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
# Part 1 - Why anybody analyzes a market at all
# ==========================================================================

PART1 = Section(
    number=1,
    title="Why Anybody Analyzes a Market",
    short="Why we analyze",
    minutes="About 25 minutes",
    covers=(
        "Where the urge to make a profit actually comes from.",
        "The one rule every trade in the world is trying to satisfy.",
        "The two jobs technical analysis does, and the four words for a trade.",
    ),
    slides=(
        Content(
            title="Markets run on three instincts",
            lines=(
                "1.  The instinct to survive.",
                "2.  The instinct for comfort.",
                "3.  The instinct to propagate.",
            ),
            accent="Survival is the strongest of the three. It usually comes first.",
            notes=(
                "Ask the room which of the three they would give up last. Let two people answer.",
                "Say that the text opens here on purpose: markets are a survival behavior before they are a financial one.",
            ),
        ),
        Content(
            title="What the survival instinct contains",
            lines=(
                "Stay alive.",
                "Satisfy hunger.",
                "Seek safety, which means staying with the group or herd.",
                "Avoid danger, through natural fears of fire, loud noise, heights.",
            ),
            accent="Notice the third one. Herding will come back on almost every chart we read.",
            notes=(
                "Point at the herd line and say we will meet it again in Part 5 when the market overreacts.",
                "Keep this fast. It is background, not an exam item on its own.",
            ),
        ),
        Content(
            title="To make a profit, something has to change",
            lines=(
                "You cannot profit from something that never moves.",
                "You need a variable of change: something you own whose value shifts.",
                "It could be a house, a sack of rice, a currency, or a share.",
            ),
            accent="Markets exist because value moves. Analysis exists because we want to know which way.",
            notes=(
                "Ask for one thing they own whose value changed this year. Take one answer.",
                "Land the accent line, then move straight to price.",
            ),
        ),
        Term(
            term="Price",
            plain="Price is the most convenient variable of change we have. It is visible, it is public, and it updates constantly.",
            example="Jollibee shares closed at 240 pesos yesterday and 244 pesos today. You did not need anyone's permission to see that.",
            formal="Price is the observable variable of change on which market participants act, and the primary data of technical analysis.",
            notes=(
                "Say why price beats the alternatives: it is cheap to observe and it is the same number for everyone.",
                "Tell them price is the single most important input in this subject, followed by volume.",
            ),
        ),
        Chart(
            title="Price is a number that will not sit still",
            letter="A",
            shows="One price line over several months, with the number read off it on four different days, so the same public figure is a different figure every time you look.",
            notes=(
                "Point at the four readings and say each one was public, free and correct on the day it was read.",
                "Land it: this is what a variable of change looks like. Nothing here is anyone's opinion yet.",
            ),
        ),
        Term(
            term="The buy low, sell high principle",
            plain="A simple mechanical rule that would guarantee a profit every single time: buy when the price is low and sell when it is higher.",
            example="Buy at 40 pesos, sell at 52 pesos, keep 12 pesos a share. Nothing clever happened.",
            formal="The buy low, sell high principle is the mechanical rule that profit is realized by acquiring at a lower price and disposing at a higher one.",
            notes=(
                "Say the rule out loud and let it sound obvious, because it is.",
                "Then set the trap: ask them how they know today's price is a low one.",
            ),
        ),
        Chart(
            title="Buy low, sell high, drawn once",
            letter="B",
            shows="A buy marked at 40 pesos, a sell marked at 52, and the 12 pesos a share kept between them shaded on the chart.",
            notes=(
                "Trace it with a finger: in here, out there, that block is the profit. It really is that simple.",
                "Then ask the question the chart cannot answer: standing at the buy marker, how did you know 40 was low?",
            ),
        ),
        Check(
            label="Instincts, price, and the basic rule",
            questions=(
                Q(
                    stem="Which instinct does the text treat as the strongest driver of market behavior?",
                    options=("The instinct for comfort",
                             "The instinct to propagate",
                             "The instinct to survive",
                             "The instinct to compete"),
                    answer="C",
                    reason="Survival almost always precedes the need for comfort or to propagate.",
                ),
                Q(
                    stem="Price is described as a variable of change mainly because:",
                    options=("It moves, and everyone can observe it",
                             "It is set by the company's accountants",
                             "It is fixed for the trading day",
                             "It equals the intrinsic value of the asset"),
                    answer="A",
                    reason="Price is popular precisely because it is both changing and openly observable.",
                ),
            ),
        ),
        Content(
            title="The rule is easy. Obeying it is not.",
            lines=(
                "To buy low you must first know that today's price is low.",
                "To sell high you must know that today's price is high.",
                "Both of those are statements about the future, not the present.",
            ),
            accent="This is where chance enters, and this is why the subject exists.",
            notes=(
                "Say plainly: everything else this semester is an attempt to answer those two questions.",
                "Warn them that the honest answer is always a probability, never a certainty.",
            ),
        ),
        Term(
            term="The price-time chart",
            plain="A picture with price up the side and time along the bottom. It is how traders keep track of two things at once.",
            example="Any chart on your trading app. The vertical axis is pesos, the horizontal axis is days.",
            formal="A price-time chart is a two dimensional visualization that plots price on the vertical axis against time on the horizontal axis.",
            notes=(
                "Draw the two axes in the air. Say profit needs effective action in both dimensions, price and time.",
                "Tell them a fundamental analyst can give them the price axis but rarely the time axis.",
            ),
        ),
        Chart(
            title="The two axes, drawn",
            letter="C",
            shows="The price-time chart itself: price up the vertical axis, time along the horizontal axis, and one price line plotted against both.",
            tier="core",
            notes=(
                "Say the two axis names out loud while pointing at each one. Price up the side, time along the bottom.",
                "Tell them Homework 1 is drawn on exactly this object, so it is worth a second look now.",
            ),
        ),
        Content(
            title="Technical analysis does exactly two jobs",
            lines=(
                "Job one: it identifies and describes what already happened.",
                "Job two: it forecasts what might happen next.",
            ),
            accent="Everything in this course is one of those two jobs.",
            caption="This is called the dual function of technical analysis.",
            notes=(
                "Hold up two fingers and keep them up. Identification, then forecasting.",
                "Say that job one is a record and job two is an opinion, and students must never confuse the two.",
            ),
        ),
        Term(
            term="Identification",
            plain="The record keeping job. The chart tells you what the market has already done, with no opinion attached.",
            example="From a five year chart you can read the highest price ever paid, the calmest month, and the days that gapped.",
            formal="Identification is the descriptive function of technical analysis: it records and describes past and present price and market action.",
            notes=(
                "Say this half is objective. The chart is a historical record and it does not argue with you.",
                "List two or three things a chart tells you before you interpret anything: volatility, extremes, liquidity.",
            ),
        ),
        Chart(
            title="Four facts, and not one of them is an opinion",
            letter="D",
            shows="One chart with the highest and the lowest price in the window marked, the calmest stretch shaded, and the one day price gapped picked out.",
            notes=(
                "Point at each of the four in turn and ask the room whether anyone could disagree with it. Nobody can.",
                "Name the gap and move on. The chapter names gapping too and never explains it, and neither will we today.",
            ),
        ),
        Term(
            term="Forecasting",
            plain="The opinion job. You take what the chart recorded and make a claim about what comes next, and the claim worth most is where a new trend begins.",
            example="Prices bounced off 100 pesos four times, so you expect buyers to show up there again.",
            formal="Forecasting is the inferential function of technical analysis: it interprets identified market action to infer potential future price behavior, especially the start of a new trend.",
            notes=(
                "Say the forecasting half rests entirely on one assumption: that price behavior repeats to some reasonable degree.",
                "Promise them we will test that assumption properly in Part 5.",
            ),
        ),
        Chart(
            title="Four bounces are the record. A fifth is the claim.",
            letter="E",
            shows="Four times price fell to 100 pesos and turned, marked on the record, and then the edge of the record, with the forecast left as an empty band because nobody has seen it yet.",
            notes=(
                "Cover the right hand band with your hand, then take it away. Left of the line is Chart D again; right of it is new.",
                "Say why nothing is drawn in the empty band: a line there would be the one thing nobody actually knows.",
            ),
        ),
        Check(
            label="The chart and the two jobs",
            questions=(
                Q(
                    stem="A price-time chart tracks which two dimensions?",
                    options=("Price and time",
                             "Price and volume",
                             "Volume and open interest",
                             "Value and time"),
                    answer="A",
                    reason="Price sits on the vertical axis and time on the horizontal axis.",
                ),
                Q(
                    stem="Recording that a stock's widest daily range last year was 8 pesos is an example of:",
                    options=("Forecasting",
                             "Intrinsic valuation",
                             "Identification",
                             "Sentiment analysis"),
                    answer="C",
                    reason="Describing what already happened is the identification function, with no claim about the future.",
                ),
            ),
        ),
        Content(
            title="What identification hands you before you risk a peso",
            lines=(
                "The average size of a normal day's move.",
                "The highest and lowest prices ever paid.",
                "Where the market usually stalls and goes sideways.",
                "How much trading actually happens, and how often price gaps.",
            ),
            accent="This is the homework you do before any trade, and it is free.",
            notes=(
                "Say this is the part students skip and professionals never skip.",
                "Ask them which of the four they would most want to know before buying.",
            ),
        ),
        Term(
            term="To go long",
            plain="To buy in order to open a new position. You now own it and you want the price to rise.",
            example="You buy 1,000 shares of Ayala at 620 pesos. You are long Ayala.",
            formal="To go long means to buy to open a new position.",
            notes=(
                "Write the word long on the board and keep it there. All four verbs go up together.",
                "Say that long simply means you profit if price rises.",
            ),
        ),
        Chart(
            title="Going long: a buy that opens",
            letter="F",
            shows="One price line with a single buy marked at 620 pesos, and an arrow saying the holder now profits if price rises.",
            notes=(
                "Say the next three charts are this same price line with different marks on it, so watch the marks and not the line.",
                "One dot so far. Nothing has been closed and nothing has been made yet.",
            ),
        ),
        Term(
            term="To liquidate",
            plain="To sell in order to close a position you already held. It is the exit from a long.",
            example="You sell those 1,000 Ayala shares at 660 pesos. You have liquidated.",
            formal="To liquidate means to sell to close a position previously held.",
            notes=(
                "Stress that liquidating is not the same as going short. It only closes what you had.",
                "Pair it visually with go long on the board.",
            ),
        ),
        Chart(
            title="Liquidating: a sell that closes the long",
            letter="G",
            shows="The same price line, with the buy at 620 now greyed out and a sell marked at 660, and the 40 pesos a share kept shaded between them.",
            notes=(
                "Point at the grey dot and say the position is now gone. The block is what it was worth.",
                "Ask what would have happened if they had sold at 605 instead. The verb does not change; only the number does.",
            ),
        ),
        Term(
            term="To go short",
            plain="To sell in order to open a new position, before you own it. You want the price to fall.",
            example="You sell 1,000 borrowed shares at 660 pesos hoping to buy them back cheaper.",
            formal="To go short means to sell to open a new position.",
            notes=(
                "Acknowledge that shorting feels backwards the first time. Say it slowly.",
                "Note that in the Philippine market short selling is restricted, but the concept is examinable.",
            ),
        ),
        Chart(
            title="Going short: a sell that opens",
            letter="H",
            shows="The same price line with a single sell marked at 660 pesos, and an arrow saying the holder now profits if price falls.",
            notes=(
                "Say the two words that matter: sell, and open. This is the only sell in the course that starts something.",
                "Compare it to Chart F on the same line: same object, opposite direction, one dot each.",
            ),
        ),
        Term(
            term="To cover",
            plain="To buy in order to close a position you had shorted. It is the exit from a short.",
            example="You buy back those 1,000 shares at 610 pesos and return them. You have covered.",
            formal="To cover means to buy to close a position previously shorted.",
            notes=(
                "Complete the square on the board: long and liquidate, short and cover.",
                "Say buying is not always bullish. Covering is a buy that ends a bearish position.",
            ),
        ),
        Chart(
            title="Covering: a buy that closes the short",
            letter="I",
            shows="The same price line, with the sell at 660 now greyed out and a buy marked at 610, and the 50 pesos a share kept shaded between them.",
            notes=(
                "This is the slide that fixes the misconception. A buy, and the position it ends was a bearish one.",
                "Put Charts F to I side by side in one sentence: open, close, open, close, and only the direction changed.",
            ),
        ),
        Check(
            label="The four words for a trade",
            questions=(
                Q(
                    stem="Selling to close a position you already held is called:",
                    options=("Liquidating",
                             "Going short",
                             "Covering",
                             "Going long"),
                    answer="A",
                    reason="Liquidating is selling to close; covering is buying to close a short.",
                ),
                Q(
                    stem="A trader borrows shares and sells them at 90 pesos. Two weeks later they buy them back at 74 pesos. The second action is:",
                    options=("Going long",
                             "Covering",
                             "Liquidating",
                             "Scaling in"),
                    answer="B",
                    reason="Buying to close a previously shorted position is covering.",
                ),
            ),
        ),
        Content(
            title="The four ways a trade actually makes money",
            lines=(
                "1.  Long at a low price, liquidate at a higher price.",
                "2.  Long at a high price, liquidate at an even higher price.",
                "3.  Short at a high price, cover at a lower price.",
                "4.  Short at a relatively low price, cover at an even lower price.",
            ),
            accent="Buy low, sell high is only scenario 1. Three other ways exist.",
            caption="The department's quiz has asked which of these count as buy low, sell high. Read them carefully.",
            notes=(
                "Warn them explicitly: the quiz asks about buy high and sell higher. It counts.",
                "Say the only losing pattern is buying high and selling lower, which is not on this list.",
            ),
        ),
        Figure(
            title="The mechanics of profiting from a change",
            number="1.1",
            shows="The two ways to profit side by side: buy low then sell high, or sell high then buy back low, with the jargon and the demand or supply behind each.",
            notes=(
                "Trace the left column with your finger, then the right, saying go long and go short as you land on them.",
                "Point at the bottom row: every trade on this page is either demand or supply. Nothing else is happening.",
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The three motivational instincts, and why survival leads",
            "Variable of change",
            "Price",
            "The buy low, sell high principle",
            "The price-time chart",
            "The dual function of technical analysis",
            "Identification",
            "Forecasting",
            "To go long, and to liquidate",
            "To go short, and to cover",
            "The four profitable trade scenarios",
        ),
        notes=(
            "Read the list, then ask the room to name any two without looking.",
            "This is a clean stopping point if you are running behind.",
        ),
    ),
)

# ==========================================================================
# Part 2 - The three ways to forecast a price
# ==========================================================================

PART2 = Section(
    number=2,
    title="Three Ways to Forecast a Price",
    short="Forecasting",
    minutes="About 30 minutes",
    covers=(
        "Fundamental analysis, information analysis, and technical analysis.",
        "Six definitions of technical analysis worth memorizing.",
        "What each approach can and cannot tell you about timing.",
    ),
    slides=(
        Content(
            title="Three approaches, one question",
            lines=(
                "1.  Fundamental analysis: what is this thing worth?",
                "2.  Information analysis: what does the news say?",
                "3.  Technical analysis: what is the market itself doing?",
            ),
            accent="All three are trying to answer the same question: where does price go next?",
            notes=(
                "Say none of the three is the enemy. They answer different halves of the question.",
                "Tell them we take each in turn, and that technical analysis gets the longest look.",
            ),
        ),
        Figure(
            title="The three approaches on one page",
            number="1.2",
            shows="Fundamental analysis using intrinsic value, technical analysis using price, volume and sentiment, information analysis using public and non-public information.",
            notes=(
                "Read across the three columns, then stop on the middle one and say the whole course lives under that arrow.",
                "Point at the eight items under technical analysis and say they meet every one of them by Chapter 10.",
            ),
        ),
        Term(
            term="Fundamental analysis",
            plain="Working out what a company is really worth by reading its financial statements, then comparing that to the price.",
            example="You read San Miguel's annual report, decide the business is worth 130 pesos a share, and see it trading at 98 pesos.",
            formal="Fundamental analysis estimates the value of a security from its financial performance and position, in order to judge whether the current price is justified.",
            notes=(
                "Ask who has already taken a financial statement analysis subject. Connect to it.",
                "Say fundamental analysis answers what to buy, and rarely when to buy.",
            ),
        ),
        Term(
            term="Intrinsic value",
            plain="What the security is genuinely worth once you account for everything the business owns, owes, and earns.",
            example="Holdings, debt, earnings, dividends, income, balance sheet activity and cash flow, all reduced to one number per share.",
            formal="Intrinsic value is the worth of a security in light of all its holdings, debt, earnings, dividends, income, balance sheet activity, and cash flow.",
            notes=(
                "Say this is the single most examinable term in Part 2. Make them write it down.",
                "Note the technical analyst usually cannot compute this, and does not try.",
            ),
        ),
        Content(
            title="Undervalued and overvalued",
            lines=(
                "Price below intrinsic value means undervalued. Buyers should appear, creating demand.",
                "Price above intrinsic value means overvalued. Sellers should appear, creating supply.",
            ),
            accent="Undervalued means cheap relative to worth. It does not mean the price will rise today.",
            caption="The department's quiz has reversed this pair to catch inattentive students.",
            notes=(
                "Say the trap out loud: a stock is overvalued when price is ABOVE intrinsic value, not below.",
                "Ask the room to say which one generates demand before you reveal it.",
            ),
        ),
        Figure(
            title="Undervalued: price below intrinsic value",
            number="1.3",
            shows="Intrinsic value of 25 dollars against a current price of 20 dollars, so the stock is underpriced and the expected reaction is potential demand.",
            notes=(
                "Point at the two numbers first, then at the arrow. The gap between them is the whole argument.",
                "Ask what the fundamentalist expects next, and make them say the word demand.",
            ),
        ),
        Figure(
            title="Overvalued: price above intrinsic value",
            number="1.4",
            shows="The same diagram inverted: a current price of 25 dollars against intrinsic value of 20 dollars, so the stock is overpriced and the expected reaction is potential supply.",
            notes=(
                "Say this is the previous slide turned upside down, and let them spot the flip themselves.",
                "Note the sell or stay in cash line. A fundamentalist waits; a technical analyst can go short.",
            ),
        ),
        Check(
            label="Value and the three approaches",
            questions=(
                Q(
                    stem="A share trades at 45 pesos and its estimated intrinsic value is 60 pesos. The share is:",
                    options=("Overvalued, and supply should be generated",
                             "Undervalued, and demand should be generated",
                             "Fairly valued",
                             "Overbought"),
                    answer="B",
                    reason="Price below estimated intrinsic value means undervalued, which potentially generates demand.",
                ),
                Q(
                    stem="Select the accurate statements. I. Fundamental analysis estimates intrinsic value. II. Technical analysis asks what a business is worth. III. Information analysis draws on public sources such as news reports. IV. All three try to forecast future price.",
                    options=("Only I, III, and IV are correct",
                             "Only I and II are correct",
                             "Only II and III are correct",
                             "All are correct"),
                    answer="A",
                    reason="Statement II is false: valuing the business is the fundamentalist's job, not the technician's.",
                ),
            ),
        ),
        Content(
            title="How a fundamentalist turns accounts into a number",
            lines=(
                "Price to earnings, or P/E. Price to earnings growth, or PEG.",
                "Price to book, and price to sales.",
                "Debt to equity, and earnings per share.",
                "Asset pricing models like the capital asset pricing model, or CAPM.",
                "CAPM seeks the best balance between risk and expected returns over a risk free rate.",
            ),
            accent="None of this tells you what to do at 9:31 tomorrow morning.",
            notes=(
                "Do not teach the ratios here. Name them and move. They belong to another subject.",
                "Say CAPM out loud and repeat the phrase over a risk free rate. The department has quizzed it.",
                "Land the accent: none of these has a time axis.",
            ),
        ),
        Term(
            term="The top-down approach",
            plain="Start with the big picture, then narrow down. Pick the strong sector first, then the best company inside it.",
            example="You decide banking will do well this year, then you compare BDO, BPI and Metrobank.",
            formal="A top-down approach studies broad market factors and sector rotation models in order to select stocks within a strengthening industry or sector.",
            notes=(
                "Draw a funnel in the air, wide at the top.",
                "Say this is how active asset allocation and sector rotation strategies are built.",
            ),
        ),
        Term(
            term="The bottom-up approach",
            plain="Start with the company. If the business is excellent, you buy it whatever the sector is doing.",
            example="You like one shipping firm's balance sheet and buy it even though shipping as a whole is weak.",
            formal="A bottom-up approach relies primarily on a specific company's own fundamental performance rather than on sector or market conditions.",
            notes=(
                "Contrast in one sentence with top-down. Do not belabor it.",
                "Call back to CAPM from the ratios slide: it is the formal attempt to balance risk against expected return over a risk free rate.",
            ),
        ),
        Content(
            title="Where fundamental analysis runs out of road",
            lines=(
                "Accounts can be dressed up, misreported, or outright falsified.",
                "By the time an audited report is published, the information is already old.",
                "It never gives you a precise price or a precise moment to act.",
            ),
            accent="Fundamental data suits long term investment. It is poor at short term timing.",
            notes=(
                "Say the third point is the one that matters for this course.",
                "Be fair: say fundamental analysis is genuinely valuable, just not for timing.",
            ),
        ),
        Check(
            label="Approaches and their limits",
            questions=(
                Q(
                    stem="An analyst first identifies a strengthening industry, then screens for the best company inside it. This is:",
                    options=("A bottom-up approach",
                             "A top-down approach",
                             "A contrarian approach",
                             "Information analysis"),
                    answer="B",
                    reason="Starting from broad market or sector conditions and narrowing down is top-down.",
                ),
                Q(
                    stem="The main weakness of fundamental analysis, for a trader, is that it:",
                    options=("Cannot value a company",
                             "Ignores a company's debt",
                             "Cannot provide clear short term price and time levels to act on",
                             "Requires a chart"),
                    answer="C",
                    reason="Its stated main weakness is the inability to give specific short term price levels or timing.",
                ),
            ),
        ),
        Content(
            title="When a policy decision becomes a price level",
            lines=(
                "Interest rate announcements and central bank policy move supply and demand too.",
                "The Swiss National Bank held a ceiling on the franc: EURCHF at or above 1.2000.",
                "That decision created a technical demand for the euro right at 1.2000.",
                "Traders bought each time the rate neared it, with stops a reasonable distance below.",
            ),
            accent="A policy decision, read off a chart as a price level.",
            caption="The ceiling holds only for as long as the bank defends it.",
            notes=(
                "This is the one place in the chapter where fundamental and technical analysis sit on the same chart. Say so.",
                "The book writes as though the ceiling still stands and does not tell us what came after, so neither will we.",
            ),
        ),
        Figure(
            title="The ceiling, drawn as a line",
            number="1.5",
            shows="A long term EURCHF chart with a horizontal line at 1.2000 labeled the SNB exchange rate ceiling on the CHF, and the shaded period from September 2011 in which price sits above that line.",
            notes=(
                "Point at the flat floor under price and say that is a central bank, not a chart pattern.",
                "Ask which kind of analyst could have traded that level. Both could, and that is the point.",
            ),
        ),
        Term(
            term="Information analysis",
            plain="Forecasting from what you read: newspapers, bulletins, online reports, company announcements.",
            example="A quarterly result beats expectations, so you expect the share to open higher tomorrow.",
            formal="Information analysis forms an opinion about potential market action from information gleaned from public sources.",
            notes=(
                "Ask how many of them have bought or sold anything because of something they read online.",
                "Then deliver the bad news on the next slide.",
            ),
        ),
        Content(
            title="Why public information is usually late",
            lines=(
                "Those with non-public material information have already moved the market.",
                "By the time it is public, only an inconsequential amount of the move is left.",
                "Acting on non-public material information is insider trading, and it is illegal.",
            ),
            accent="The technical analyst sees the move on the chart and acts, without waiting for the reason.",
            caption="In unregulated over the counter markets, brokers front running large client orders is the same problem wearing a different name.",
            notes=(
                "Be clear on the law: insider trading is illegal in the equity markets, full stop.",
                "Land the accent line, because it is the whole argument for technical analysis.",
            ),
        ),
        Term(
            term="Technical analysis",
            plain="Reading the market's own behavior, mainly price, volume and open interest, to work out what it is likely to do next.",
            example="You do not know why the buyers came. You only know they came at 250 pesos, three times.",
            formal="Technical analysis is the identification and forecasting of potential market behavior based largely on the action and dynamics of the market itself.",
            notes=(
                "Say the technician studies the effect, not the cause. That distinction is examinable.",
                "Tell them the next six slides are quotable definitions and they should copy them exactly.",
            ),
        ),
        Quote(
            text="Technical analysis is the study of market action, primarily through the use of charts, for the purpose of forecasting future price trends.",
            source="John Murphy, Technical Analysis of the Financial Markets (NYIF, 1999)",
            takeaway="Charting is the main tool, and the target is future price trends.",
            notes=(
                "This is the definition to give if an exam asks for one. Say so.",
                "Point at the two working words: charts, and forecasting.",
            ),
        ),
        Check(
            label="Information, and the first definition",
            questions=(
                Q(
                    stem="Why is publicly available information usually of limited forecasting value?",
                    options=("Those with non-public material information have already moved the market",
                             "It is difficult to find",
                             "It is always inaccurate",
                             "It cannot be plotted on a chart"),
                    answer="A",
                    reason="By the time news is public, the substantial move has usually already happened.",
                ),
                Q(
                    stem="Murphy's definition identifies the main tool of technical analysis as:",
                    options=("Financial statements",
                             "Polls and surveys",
                             "Regression models",
                             "Charts"),
                    answer="D",
                    reason="Murphy defines it as the study of market action primarily through the use of charts.",
                ),
            ),
        ),
        Quote(
            text="Technical analysis is the science of recording, usually in graphic form, the actual history of trading ... then deducing from that pictured history the probable future trend.",
            source="Edwards and Magee, Technical Analysis of Stock Trends (AMACOM, 2007)",
            takeaway="Past information, recorded as a picture, is what the forecast is built from.",
            notes=(
                "Point out the word probable. Nothing here is promised.",
                "Say this definition is the one that names the raw material: recorded history.",
            ),
        ),
        Quote(
            text="It refers to the study of the action of the market itself as opposed to the study of the goods in which the market deals.",
            source="Edwards and Magee, Technical Analysis of Stock Trends (AMACOM, 2007)",
            takeaway="You study the market, not the product the market trades.",
            notes=(
                "Say this is the cleanest one line separation between technical and fundamental analysis.",
                "Use a concrete pair: the share price of a mining firm, versus the ore in the ground.",
            ),
        ),
        Quote(
            text="The art of technical analysis, for it is an art, is to identify a trend reversal at a relatively early stage and ride on that trend until the weight of the evidence shows or proves that the trend has reversed.",
            source="Martin Pring, Technical Analysis Explained, 4th Edition (McGraw-Hill, 2002)",
            takeaway="The goal is to catch a reversal early, and then to stay until the evidence turns.",
            notes=(
                "Note the chapter title calls this an art and a science. This quote is the art half.",
                "Say the second half matters as much as the first: you stay until evidence says otherwise.",
            ),
        ),
        Check(
            label="Three definitions in a row",
            questions=(
                Q(
                    stem="Which definition draws the line between studying the market and studying the goods the market deals in?",
                    options=("Murphy",
                             "Pring",
                             "Lim",
                             "Edwards and Magee"),
                    answer="D",
                    reason="That line is Edwards and Magee's, from Technical Analysis of Stock Trends.",
                ),
                Q(
                    stem="Pring describes the art of technical analysis as identifying:",
                    options=("The intrinsic value of a stock",
                             "The exact top of a market",
                             "A trend reversal at a relatively early stage",
                             "The cause of a price move"),
                    answer="C",
                    reason="Pring's phrasing is to identify a trend reversal at a relatively early stage and ride the trend.",
                ),
            ),
        ),
        Quote(
            text="Technical analysis deals in probabilities, never in certainties.",
            source="Martin Pring, Technical Analysis Explained, 4th Edition (McGraw-Hill, 2002)",
            takeaway="This is the definition that keeps you solvent. Weigh risk against return, every time.",
            notes=(
                "If they remember one sentence from today, make it this one.",
                "Say that any classmate who promises a certain trade has just failed this chapter.",
            ),
        ),
        Quote(
            text="Technical analysis is based on the assumption that people will continue to make the same mistakes they have made in the past.",
            source="Martin Pring, Technical Analysis Explained, 4th Edition (McGraw-Hill, 2002)",
            takeaway="This is the behavioral reason the whole subject works at all.",
            notes=(
                "Say patterns repeat because people repeat. Fear, greed, hope, anger and regret do not update.",
                "Connect forward to Part 5, where repeatability becomes a formal assumption.",
            ),
        ),
        Quote(
            text="Market price tends to lead the known fundamentals ... Market price acts as a leading indicator of the fundamentals.",
            source="John Murphy, Technical Analysis of the Financial Markets (NYIF, 1999)",
            takeaway="Price often moves before the news explains why. That is the timing advantage.",
            notes=(
                "This quote is the bridge into the discounting assumption in Part 5.",
                "Say price is a reflection of all known information acted upon in the markets.",
            ),
        ),
        Content(
            title="What technically based timing gives you",
            lines=(
                "Precise entry and exit prices, and the precise time of entry and exit.",
                "Real time bullish and bearish signals, and real time price triggers.",
                "The ability to scale in and out at significant price levels.",
                "Entries and exits timed to volatility behavior and to market order flow.",
            ),
            accent="Notice how many of these contain the word precise.",
            caption="A precise entry level is not a predicted reversal price. It says where you will act, not where the market will turn.",
            notes=(
                "Do not read all four aloud. Read two and let them read the rest.",
                "Land the accent: precision is the technician's whole claim.",
                "Then say the caption twice. Quiz 1 asks them to reject the claim that technical analysis gives the exact price at which a reversal will occur.",
            ),
        ),
        Content(
            title="What technically based timing gives you, continued",
            lines=(
                "Exit an extended trend at a technically significant reversal level.",
                "Define risk as a percentage, in terms of real price levels.",
                "Use volume and open interest to gauge the strength of a move.",
                "Use market breadth and sentiment to gauge that strength more broadly.",
                "Forecast peaks and troughs through cycle and seasonality analysis.",
            ),
            accent="Every one of these is a technique we will build over the semester.",
            notes=(
                "Tell them this slide is a preview of the syllabus. They are not expected to do any of it yet.",
                "Point at cycle and seasonality and name the chapter it arrives in.",
            ),
        ),
        Content(
            title="What fundamentally based timing gives you",
            lines=(
                "Undervalued stocks that could appreciate, with no precise price or time to go long.",
                "Overvalued stocks that could depreciate, with no precise price or time to go short.",
                "Fundamentally strong stocks to rotate into, again with no precise price or time.",
            ),
            accent="Read the ending of all three lines. The gap is always timing.",
            notes=(
                "Make them notice the repeated phrase themselves before you point it out.",
                "Be fair to the fundamentalist: they answer what, we answer when.",
            ),
        ),
        Content(
            title="The fundamentalist, in four lines",
            lines=(
                "Mainly concerned with intrinsic value.",
                "Strives to understand the underlying cause of a market move.",
                "Focused on which company to participate in.",
                "Can tell you which company to buy, but not the best moment to start.",
            ),
            accent="Cause, company, value.",
            notes=(
                "Read the fourth line twice. It is the one the department quizzes.",
                "Keep the pace up; the contrast slide is next.",
            ),
        ),
        Content(
            title="The technical analyst, in four lines",
            lines=(
                "Mainly concerned with the structure and dynamics of price and market action.",
                "More concerned with the effects of a move than with its cause.",
                "Usually cannot determine intrinsic value or whether a stock is under or overvalued.",
                "Can determine precisely when to start, purely from price performance.",
            ),
            accent="Effect, price, timing.",
            caption="Neither column is complete on its own. Most professionals use both.",
            notes=(
                "Put the two three word summaries side by side out loud: cause, company, value against effect, price, timing.",
                "Say the honest professional position is that these are complements, not rivals.",
            ),
        ),
        Check(
            label="Timing, and who answers which question",
            questions=(
                Q(
                    stem="Which is offered by technically based market timing but not by fundamentally based market timing?",
                    options=("Identifying an undervalued stock",
                             "An estimate of intrinsic value",
                             "A precise price and time of entry",
                             "A view on a company's debt level"),
                    answer="C",
                    reason="Precise entry and exit price and time is exactly what fundamental timing lacks.",
                ),
                Q(
                    stem="Pick the accurate statements. I. A technical analyst is more concerned with effects than causes. II. A fundamentalist is mainly concerned with intrinsic value. III. A technical analyst usually cannot determine intrinsic value. IV. A fundamentalist can tell you the most advantageous moment to enter.",
                    options=("Only I, II, and III are correct",
                             "Only I and II are correct",
                             "Only II and IV are correct",
                             "All are correct"),
                    answer="A",
                    reason="Statement IV is false: the fundamentalist can tell you which company, not the best moment.",
                ),
            ),
        ),
        Content(
            title="The six streams of market action",
            lines=(
                "Price action, and volume action.",
                "Open interest action.",
                "Sentiment, and market breadth.",
                "Flow of funds.",
            ),
            accent="Price is the most important, followed closely by volume.",
            caption="Flow of funds includes things like margin debt. The department has quizzed exactly that.",
            notes=(
                "Make them count six on their fingers. This list is a standing exam item.",
                "Flag the margin debt point explicitly; it appeared on a past quiz.",
            ),
        ),
        Term(
            term="OHLC",
            plain="The four numbers that describe any single bar on a chart: where it opened, its high, its low, and where it closed.",
            example="A daily bar for Globe: opened 1,800, high 1,845, low 1,792, closed 1,838.",
            formal="OHLC denotes the opening, high, low, and closing prices of a bar over any chosen interval, from one minute to one year.",
            notes=(
                "Draw a single bar and label the four points.",
                "Stress that OHLC is not only daily. Any interval has an OHLC.",
            ),
        ),
        Check(
            label="Market action and its data",
            questions=(
                Q(
                    stem="Flow of funds analysis involves the study of:",
                    options=("Oscillators",
                             "Linear regression",
                             "Point and figure charts",
                             "Margin debt"),
                    answer="D",
                    reason="Margin debt is a flow of funds measure; the other three are chart or statistical studies.",
                ),
                Q(
                    stem="Of all the data technical analysts use, the most important is:",
                    options=("Open interest",
                             "Sentiment",
                             "Price",
                             "Market breadth"),
                    answer="C",
                    reason="Price is the most important, followed closely by volume action.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Fundamental, information and technical analysis",
            "Intrinsic value",
            "Undervalued and overvalued",
            "Top-down and bottom-up approaches",
            "Non-public material information and insider trading",
            "Murphy: study of market action through charts",
            "Edwards and Magee: recording history, deducing the probable trend",
            "Edwards and Magee: the market itself, not the goods",
            "Pring: an art, catching a reversal early",
            "Pring: probabilities, never certainties",
            "Pring: people repeat their mistakes",
            "Murphy: price leads the known fundamentals",
            "Technically and fundamentally based market timing",
            "The fundamentalist and the technical analyst",
            "The six streams of market action, and OHLC",
        ),
        notes=(
            "Ask for the six streams of market action out loud before you move on.",
            "This is the natural stop if the session is being split across two meetings.",
        ),
    ),
)

# ==========================================================================
# Part 3 - Classifying technical analysis
# ==========================================================================

PART3 = Section(
    number=3,
    title="Classifying Technical Analysis",
    short="Classifications",
    minutes="About 25 minutes",
    covers=(
        "The four branches every technique in this course belongs to.",
        "The two opposite bets a trader can make about price.",
        "The honest advantages and disadvantages of the whole method.",
    ),
    slides=(
        Content(
            title="Four branches, one subject",
            lines=(
                "1.  Classical technical analysis.",
                "2.  Statistical analysis.",
                "3.  Sentiment analysis.",
                "4.  Behavioral analysis.",
            ),
            accent="Whatever branch you use, you still interpret it through your own biases.",
            notes=(
                "Say these four are a filing system. Every tool in the book lands in one of them.",
                "Warn them the fourth one, behavioral, is about the analyst as much as the market.",
            ),
        ),
        Figure(
            title="The four branches on one page",
            number="1.6",
            shows="Classical, statistical, sentiment and behavioral analysis, each with its own list of studies, all funnelling into one line at the bottom.",
            notes=(
                "Read the bottom line of the diagram aloud: everything above it is interpreted through filters and biases unique to each analyst.",
                "Say that bottom line is Part 4 arriving early, and that it is the reason Part 4 exists.",
            ),
        ),
        Term(
            term="Classical technical analysis",
            plain="The traditional, visual, hand-drawn kind. Patterns on charts, and indicators drawn over or under the price.",
            example="Bar and candlestick patterns, support and resistance, oscillators, market breadth, cycle analysis.",
            formal="Classical technical analysis uses conventional bar, chart and candlestick patterns, oscillator and overlay indicators, market breadth, relative strength, and cycle analysis.",
            notes=(
                "Say this is most of what this course teaches, and it is qualitative by nature.",
                "Name two examples they will already recognize from the app on their phone.",
            ),
        ),
        Term(
            term="Statistical analysis",
            plain="The mathematical kind. Instead of looking at a shape you compute a number and test it.",
            example="Volatility, linear regression, correlation, time series analysis, hypothesis testing.",
            formal="Statistical analysis is the quantitative branch, studying dispersion, central tendency, skewness, volatility, regression, hypothesis testing, correlation and covariance.",
            notes=(
                "Contrast in one line: classical is qualitative, statistical is quantitative.",
                "Reassure them that no statistics is examined today; only the classification is.",
            ),
        ),
        Term(
            term="Sentiment analysis",
            plain="Measuring the mood of the crowd. How optimistic or pessimistic are participants right now?",
            example="Put to call ratios, short interest, margin debt, bullish percent readings, opinion polls of professionals.",
            formal="Sentiment analysis studies the psychology of market participants through polls and surveys, flow of funds, and the positions taken by large institutions and hedgers.",
            notes=(
                "Ask what the mood of the room is right now. Use it as the joke that anchors the term.",
                "Note that sentiment data is where flow of funds and margin debt live.",
            ),
        ),
        Term(
            term="Behavioral analysis",
            plain="Studying how participants actually react, including their biases and their bad habits.",
            example="Herd behavior, loss aversion, confirmation bias, overconfidence, the gambler's fallacy.",
            formal="Behavioral analysis studies how market participants react to news, to profits and losses, to the actions of others, and to their own psychological and emotional biases.",
            notes=(
                "Say this branch studies the participant, not the price. That is the difference from sentiment.",
                "Name one bias, confirmation bias, and promise it returns in Part 4.",
            ),
        ),
        Check(
            label="The four branches",
            questions=(
                Q(
                    stem="Studying skewness, regression and volatility of returns belongs to which branch?",
                    options=("Statistical",
                             "Classical",
                             "Sentiment",
                             "Behavioral"),
                    answer="A",
                    reason="Those are quantitative measures, which is the statistical branch.",
                ),
                Q(
                    stem="Japanese candlestick patterns and overlay indicators belong to:",
                    options=("Classical technical analysis",
                             "Statistical analysis",
                             "Sentiment analysis",
                             "Behavioral analysis"),
                    answer="A",
                    reason="Candlesticks, oscillators and overlays are the conventional, classical toolkit.",
                ),
            ),
        ),
        Content(
            title="Two opposite bets about price",
            lines=(
                "Bet one: price has gone far enough and will come back.",
                "Bet two: price is going somewhere and will keep going.",
            ),
            accent="Almost every strategy you will ever meet is one of these two.",
            caption="The technical studies you choose follow directly from which bet you are making.",
            notes=(
                "Ask the room which bet feels more natural to them. Take a show of hands.",
                "Say neither is right. They are right at different times, which is the whole difficulty.",
            ),
        ),
        Figure(
            title="Mean reverting against non-mean reverting",
            number="1.7",
            shows="The two camps compared column by column: their study preferences, their order types, where each one enters, and the rationale behind each.",
            notes=(
                "Do not read all of it. Pick the entry rows and contrast them: cycle extremes against cycle midpoints.",
                "Land the last row: one is a counter-trend trader, the other is a trend trader. That is the whole difference.",
            ),
        ),
        Term(
            term="The mean reverting or contrarian approach",
            plain="You expect price to snap back to an average. You do not expect it to travel far.",
            example="You buy at support and short at resistance, using divergence, regression lines, moving average bands and Bollinger bands.",
            formal="A mean reverting approach expects price to return to an average or to a balance between supply and demand, enters at cycle extremes, and acts on the overbought and oversold conditions its studies pinpoint.",
            notes=(
                "Say contrarians prefer consolidations to trends, and limit entry orders to stop orders.",
                "List two tools only, then move. The tools get their own chapters later.",
            ),
        ),
        Term(
            term="The non-mean reverting or momentum approach",
            plain="You expect price to keep travelling. Demand creates more demand, supply creates more supply.",
            example="You buy the breakout of a chart pattern, a moving average, a Darvas Box or a Donchian channel.",
            formal="A non-mean reverting approach expects trends to continue through a positive feedback cycle, enters at cycle midpoints, and acts on the crossover of the oscillator equilibrium level.",
            notes=(
                "Say this trader longs the breach of resistance and shorts the breach of support, the exact opposite of the contrarian.",
                "Name Darvas Box out loud; the department has quizzed it as a momentum example.",
            ),
        ),
        Term(
            term="Limit and stop entry orders",
            plain="A limit order buys only at your price or better. A stop order buys only once price has pushed through a level.",
            example="Contrarians prefer limit orders, because they want a good price. Momentum traders prefer stop orders, because they want confirmation.",
            formal="Limit entry orders execute at a specified price or better; stop entry orders trigger once price trades through a specified level.",
            notes=(
                "Say the order type gives away the trader's belief. That is the point of this slide.",
                "Ask which order type a contrarian prefers before you show the answer.",
            ),
        ),
        Check(
            label="The two approaches",
            questions=(
                Q(
                    stem="A trader who buys at support, shorts at resistance and prefers limit entry orders is following:",
                    options=("A momentum seeking approach",
                             "A mean reverting approach",
                             "An arbitrage approach",
                             "A random walk approach"),
                    answer="B",
                    reason="Buying support, shorting resistance and using limit orders is the contrarian, mean reverting profile.",
                ),
                Q(
                    stem="Pick the accurate statements. I. A momentum seeking approach is usually trend based. II. Darvas Box trading is an example of a momentum seeking approach. III. Contrarians expect price to be more mean reverting. IV. Contrarians look for impending reversals.",
                    options=("Only I is correct",
                             "Only I, II, and IV are correct",
                             "Only I and IV are correct",
                             "All are correct"),
                    answer="D",
                    reason="All four statements are accurate descriptions of the two approaches.",
                ),
            ),
        ),
        Content(
            title="What technical analysis is genuinely good at",
            lines=(
                "It works the same way on every market, instrument and timeframe.",
                "You do not need to learn a new company to trade a new stock.",
                "It is visual, so market risk and volatility are easy to see.",
            ),
            accent="One skill, applied everywhere. That is the strongest practical argument for it.",
            notes=(
                "Contrast with the fundamentalist, who must learn each company from scratch.",
                "Say the visual point matters more than students expect; numbers hide volatility, charts show it.",
            ),
        ),
        Content(
            title="What technical analysis is genuinely good at, continued",
            lines=(
                "It gives timely, precise entry and exit levels.",
                "Those levels arrive with a signal, bullish or bearish, before the move.",
                "When many participants act on the same obvious level, the reaction is more reliable.",
            ),
            accent="That last advantage has a name, and it is also a criticism. We meet it shortly.",
            notes=(
                "Tease the self-fulfilling prophecy here without naming it yet.",
                "Say the same fact is listed by the text as both an advantage and a disadvantage.",
            ),
        ),
        Content(
            title="The honest disadvantages",
            lines=(
                "It is subjective. The same pattern can be read several ways.",
                "The repeating tendency can be disrupted by shocks, or by algorithmic and high frequency trading.",
                "Reading a chart takes practice; inferring from it takes much more.",
            ),
            accent="Every bullish reading has an equal and opposite bearish reading.",
            notes=(
                "Say the first disadvantage is so important it gets the whole of Part 4.",
                "Be honest here. A course that only sells the method is a bad course.",
            ),
        ),
        Content(
            title="The three big objections",
            lines=(
                "Random walk: prices are pure chance, so patterns mean nothing.",
                "The strong form of the Efficient Market Hypothesis: price already reflects everything.",
                "The self-fulfilling prophecy: signals work only because everyone watches them.",
            ),
            accent="We take the first two apart in Part 5. We take the third apart right now.",
            notes=(
                "Name all three, then say clearly that only the third is taught in this part.",
                "Promise them Part 5 answers the other two properly.",
            ),
        ),
        Term(
            term="The self-fulfilling prophecy",
            plain="The claim that a technical signal works not because it is meaningful, but because enough people act on it at the same moment.",
            example="A trendline breaks and thousands of traders buy on the break, so price rises, so the trendline looks like it worked.",
            formal="The self-fulfilling prophecy holds that prices react to technical signals because of the concerted action of participants acting on those signals rather than because of the signals themselves.",
            notes=(
                "Say this is an objection that can be turned into a tool: pick only the clear and obvious signals.",
                "Warn them the effect does not last, and show the cycle next.",
            ),
        ),
        Content(
            title="The self-fulfilling prophecy cycle, stages one to three",
            lines=(
                "1.  A clear and obvious signal attracts participants.",
                "2.  Their concerted action creates reliable price reactions.",
                "3.  Reliable reactions attract even more participants.",
            ),
            accent="These three stages are the advantage. This is when the signal is worth trading.",
            notes=(
                "Say we are three stages into a six stage cycle, so stop them from relaxing.",
                "Ask what they think happens when a strategy becomes too popular.",
            ),
        ),
        Content(
            title="The cycle, stages four to six",
            lines=(
                "4.  Participants start to preempt each other for better fills.",
                "5.  Reactions drift from expected entry levels and participants abandon the signal.",
                "6.  With preempting gone, reliable reactions begin to appear again.",
            ),
            accent="Then the process repeats. The signal is never permanently dead or permanently alive.",
            notes=(
                "Say the cruel part out loud: the crowd destroys the edge it created.",
                "Name preempting here, since it returns as a challenge in Part 5.",
            ),
        ),
        Figure(
            title="The six stages as one loop",
            number="1.8",
            shows="The self-fulfilling prophecy cycle drawn as a circle, with stages one to three bracketed as advantageous entries and stages four to six as disadvantageous.",
            notes=(
                "Walk the circle once with your finger, naming each stage, then show them the two brackets down the sides.",
                "Ask where in the loop they would want to be trading. The answer is the right hand bracket.",
            ),
        ),
        Check(
            label="Strengths, weaknesses, and the prophecy",
            questions=(
                Q(
                    stem="A random walk view of the market implies that:",
                    options=("Technical analysis is still useful because patterns may arise by chance",
                             "Technical analysis is unreliable only in volatile markets",
                             "Technical analysis works only on long timeframes",
                             "Technical analysis is pointless because chart patterns arise out of pure chance"),
                    answer="D",
                    reason="If all action is random, patterns carry no information and analysis is pointless.",
                ),
                Q(
                    stem="In the self-fulfilling prophecy cycle, participants preempting each other for better fills happens at:",
                    options=("Stage 1",
                             "Stage 2",
                             "Stage 4",
                             "Stage 6"),
                    answer="C",
                    reason="Preempting is stage 4, and it is what erodes the reliability of the signal.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Classical technical analysis",
            "Statistical analysis",
            "Sentiment analysis",
            "Behavioral analysis",
            "The mean reverting or contrarian approach",
            "The non-mean reverting or momentum approach",
            "Limit entry orders and stop entry orders",
            "Darvas Box and Donchian channel breakouts",
            "The advantages of technical analysis",
            "The disadvantages of technical analysis",
            "The self-fulfilling prophecy",
            "The six stage prophecy cycle, and preempting",
        ),
        notes=(
            "Ask for the four branches without looking. That is the highest value item here.",
            "Clean stopping point. Part 4 is a self contained topic.",
        ),
    ),
)

# ==========================================================================
# Part 4 - Subjectivity
# ==========================================================================

PART4 = Section(
    number=4,
    title="Subjectivity",
    short="Subjectivity",
    minutes="About 35 minutes",
    covers=(
        "Which half of technical analysis is objective, and which half is not.",
        "Why two honest analysts read the same chart differently.",
        "How to resolve conflicting signals instead of freezing.",
    ),
    slides=(
        Content(
            title="Objective and subjective at the same time",
            lines=(
                "The chart is objective. It is a historical record and it does not argue.",
                "The analysis is subjective. It happens inside a human being.",
            ),
            accent="The data is not the problem. The reader is.",
            notes=(
                "Say this part is the one students find uncomfortable, and that is the point.",
                "Repeat: objective record, subjective reading.",
            ),
        ),
        Content(
            title="Analysis is three separate activities",
            lines=(
                "1.  Identifying price and indicator patterns.",
                "2.  Interpreting what the data means.",
                "3.  Inferring what price might do next.",
            ),
            accent="Subjectivity enters at every one of the three, not just the last.",
            notes=(
                "Number them on your fingers and make them repeat the three back.",
                "Say most students assume only step three is subjective. Step one already is.",
            ),
        ),
        Term(
            term="Subjectivity",
            plain="Two competent analysts, given exactly the same chart, can reach different and equally defensible conclusions.",
            example="One reads an overbought oscillator as a strong trend continuing. Another reads it as a market about to reverse.",
            formal="Subjectivity is the dependence of analysis on behavioral traits, filters and biases unique to each analyst or observer.",
            notes=(
                "Say the crucial line: this is not a flaw unique to technical analysis. Every kind of analysis has it.",
                "Ask them to hold that thought until the end of Part 4, when we prove it.",
            ),
        ),
        Content(
            title="The problem is twofold",
            lines=(
                "First: which form of analysis should be applied to this chart at all?",
                "Second: which indicators should be applied to it?",
            ),
            accent="Neither question has a correct answer. Both have consequences.",
            caption="One plain chart can carry trendlines, moving averages, chart patterns, regression bands, divergence, volatility bands and volume study.",
            notes=(
                "List two or three of the caption items aloud, then say the list is not exhaustive.",
                "Say these are the questions that plague novices, and that they are supposed to feel unresolved.",
            ),
        ),
        Figure(
            title="One chart, reading one: nothing on it",
            number="1.9",
            shows="A plain price chart with no analysis drawn on it at all, the raw record before anybody has interpreted it.",
            notes=(
                "Say this is the objective half. Nobody in the room can disagree with this picture.",
                "Tell them the next six slides are this identical chart, and to watch what people put on it.",
            ),
        ),
        Figure(
            title="Reading two: trendlines",
            number="1.10",
            shows="The same chart with a short-term downtrend line, a longer-term uptrend line, an uptrend line and a downtrend line drawn across it.",
            notes=(
                "Say every line on this slide was a human choice about which two points to connect.",
                "Ask which of the four lines matters most. They will not agree, and that is the lesson.",
            ),
        ),
        Figure(
            title="Reading three: moving averages",
            number="1.11",
            shows="The same chart with a moving average through it, marked where it acts as support with buy points and where it acts as resistance with a short.",
            notes=(
                "Point out the buy and short labels, then say the chart never used those words. The reader did.",
                "Note that a different average length moves every one of those labels.",
            ),
        ),
        Figure(
            title="Reading four: chart patterns",
            number="1.12",
            shows="The same chart annotated with an ascending triangle, a head and shoulders, a parabolic move, a symmetrical triangle breakout and a channel retest.",
            notes=(
                "Ask how many patterns they can see before you name them. Usually one or two.",
                "Say a trained eye sees all six here, and a different trained eye sees a different six.",
            ),
        ),
        Figure(
            title="Reading five: regression and divergence",
            number="1.13",
            shows="The same chart with regression lines showing higher highs in price while the CCI panel below makes lower highs, marked standard bearish divergence.",
            notes=(
                "Make them look at the two panels together. Price up, indicator down. That gap is the signal.",
                "Say this reading forecasts a reversal, which none of the previous four slides did.",
            ),
        ),
        Figure(
            title="Reading six: regression with volume",
            number="1.14",
            shows="The same chart with regression lines and a volume panel underneath, marking a parabolic buying climax with a volume spike at the blow off.",
            notes=(
                "Point at the volume spike and the price spike above it and say they happened on the same bar.",
                "This is the same forecast as the last slide, reached by a completely different route.",
            ),
        ),
        Figure(
            title="Reading seven: volatility bands, volume and MACD",
            number="1.15",
            shows="The same chart again with volatility bands, price exceeding the upper band, the volume spike, and MACD at a historically overbought level.",
            notes=(
                "Say it out loud: seven slides, one chart, seven defensible readings, and not one of them was wrong.",
                "That is the argument of Part 4. Stop here for a moment before you move on.",
            ),
        ),
        Check(
            label="Where subjectivity lives",
            questions=(
                Q(
                    stem="Which part of technical analysis is described as objective?",
                    options=("The interpretation of indicators",
                             "The chart as a historical record of price and market action",
                             "The inference of future price",
                             "The choice of which indicator to apply"),
                    answer="B",
                    reason="The chart is an objective record; everything done to it afterwards is subjective.",
                ),
                Q(
                    stem="Analyzing price and market action consists of which three activities?",
                    options=("Buying, holding, selling",
                             "Recording, charting, publishing",
                             "Screening, valuing, timing",
                             "Identifying, interpreting, inferring"),
                    answer="D",
                    reason="The three activities are identifying patterns, interpreting the data, and inferring future behavior.",
                ),
            ),
        ),
        Term(
            term="Contradictory signals",
            plain="Two indicators point in opposite directions at the same moment.",
            example="The MACD says the market is strengthening while the stochastic says it is exhausted.",
            formal="Contradictory signals are indications from two or more studies that are in clear and direct opposition to one another.",
            notes=(
                "Say this is inevitable, not a malfunction. Each oscillator is built differently.",
                "Promise a resolution rule before the end of this part.",
            ),
        ),
        Term(
            term="Confirmatory signals",
            plain="Two indicators agree, so your confidence in the reading goes up.",
            example="A chart pattern breaks upward and volume expands on the same bar.",
            formal="Confirmatory signals are indications from separate studies that agree with and reinforce the same conclusion.",
            notes=(
                "Say confirmation is comfortable and therefore dangerous; it feeds the bias in the next term.",
                "Keep this short. It is the easiest of the three.",
            ),
        ),
        Term(
            term="Complementary signals",
            plain="Two signals look contradictory but are actually describing different time horizons, and together they say more than either alone.",
            example="A 20 period reading says slightly overbought while a 100 period reading says slightly oversold: cheap for the long term, stretched for the short term.",
            formal="Complementary signals are apparently opposing indications that, once their differing time horizons are recognized, combine into a fuller reading of the market.",
            notes=(
                "Walk the CCI example slowly. This is the single most useful idea in Part 4.",
                "Say the astute trader looks for cheap on both horizons at once, and enters there.",
            ),
        ),
        Check(
            label="Three kinds of signal",
            questions=(
                Q(
                    stem="A 20 period oscillator reads overbought while a 100 period oscillator on the same chart reads oversold. This is best described as:",
                    options=("A contradiction that invalidates both",
                             "A complementary reading across two time horizons",
                             "A confirmatory signal",
                             "A data error on the platform"),
                    answer="B",
                    reason="Different time horizons are not a real conflict; read together they describe short and long term position.",
                ),
                Q(
                    stem="Signals that agree with each other and reinforce the same conclusion are:",
                    options=("Confirmatory",
                             "Contradictory",
                             "Complementary",
                             "Contrarian"),
                    answer="A",
                    reason="Agreement and reinforcement is the definition of a confirmatory signal.",
                ),
            ),
        ),
        Content(
            title="Why indicators disagree in the first place",
            lines=(
                "The mathematics behind each indicator is different.",
                "Each one tracks a different time horizon.",
                "Data may be missing on one charting platform.",
                "Data quality, accuracy and type vary between platforms.",
            ),
            accent="Two identical indicators on two platforms can honestly disagree.",
            caption="Tick volume, which counts transactions regardless of size, is one common source of the difference.",
            notes=(
                "Ask if anyone has seen two apps show different indicator readings. Someone always has.",
                "Define tick volume from the caption: number of transactions, not size of them.",
            ),
        ),
        Figure(
            title="Two oscillators, one chart, opposite answers",
            number="1.16",
            shows="A daily Alcoa chart with two oscillators below it: the faster one reads overbought at the same moment the slower one reads oversold.",
            notes=(
                "Circle the two readings with your hand and ask the room which one to obey.",
                "Then give them the answer from the last section: different periods, so this is complementary, not contradictory.",
            ),
        ),
        Content(
            title="Resolving conflicting chart patterns",
            lines=(
                "First, measure the size of each pattern.",
                "The sentiment of the larger formation takes precedence.",
                "Larger patterns speak for the longer term, smaller ones for the short term.",
            ),
            accent="A bullish ascending triangle that contains a bearish head and shoulders stays bullish until the neckline breaks.",
            caption="This one rule removes a large slice of the subjectivity in reading chart formations.",
            notes=(
                "This is review question three from the chapter. Say so, and tell them to write the rule down.",
                "Give the caution: an upside break of a large bearish formation can be violent, because it is unexpected.",
            ),
        ),
        Figure(
            title="Conflicting patterns in one formation",
            number="1.17",
            shows="An ascending triangle marked bullish, a symmetrical triangle marked neutral, and a complex head and shoulders marked bearish, all in the same stretch of price.",
            notes=(
                "Name the three patterns, then ask which one wins. Apply the rule: the largest formation takes precedence.",
                "The ascending triangle is the largest here, so it stays bullish until the neckline breaks.",
            ),
        ),
        Figure(
            title="Patterns that agree",
            number="1.18",
            shows="A larger descending triangle and a smaller descending triangle, both bearish, over a complex head and shoulders that is also bearish.",
            notes=(
                "Contrast this with the last slide: different shapes, but every one of them points the same way.",
                "Say this is what confirmation looks like on a chart, and why it feels so comfortable.",
            ),
        ),
        Content(
            title="The same fact, read two ways",
            lines=(
                "Oil rises sharply. One analyst calls it bearish: costs go up across the economy.",
                "Another calls it bullish: demand is rising, so the economy is healthy.",
                "Both are reading the identical fact.",
            ),
            accent="For every bullish interpretation there is an equal and opposite bearish one.",
            caption="Notice that both of those analysts are fundamentalists. Subjectivity is not a technical problem.",
            notes=(
                "Ask the room which reading they prefer, then point out both are defensible.",
                "Land the caption hard: this objection applies to every kind of analysis.",
            ),
        ),
        Check(
            label="Conflicts, and how to settle them",
            questions=(
                Q(
                    stem="Two identical oscillators on two different platforms give different readings. The most likely reason is:",
                    options=("One platform is fraudulent",
                             "Oscillators are random by design",
                             "The market was closed",
                             "Differences in data availability, accuracy or type between the platforms"),
                    answer="D",
                    reason="Missing data, or variation in data quality and type between platforms, produces inconsistent readings.",
                ),
                Q(
                    stem="A large bullish ascending triangle contains a smaller bearish complex head and shoulders. Until the neckline breaks, the formation is read as:",
                    options=("Bearish, because the smaller pattern is more recent",
                             "Bullish, because the larger formation takes precedence",
                             "Neutral, because the signals cancel",
                             "Unreadable, because the patterns conflict"),
                    answer="B",
                    reason="The larger formation carries the longer term sentiment and takes precedence until its own level is breached.",
                ),
            ),
        ),
        Term(
            term="Selective perception",
            plain="Quietly ignoring the signals that disagree with the view you already hold.",
            example="You use three oscillators. Two are bullish, one is not, so you decide the third one is unreliable today.",
            formal="Selective perception is the tendency to heed only those signals that support a preconceived view of the market, discarding those that conflict with it.",
            notes=(
                "Say this is the most expensive habit in the room, and every one of them will do it.",
                "Give the antidote: a disagreeing signal is the most informative thing on your screen.",
            ),
        ),
        Figure(
            title="Selective perception, drawn",
            number="1.19",
            shows="A head and shoulders in price with three oscillators below it. MACD is bullish and is crossed out with the word ignore written across it; RSI and stochastics are bearish.",
            notes=(
                "Point at the word ignore written across the MACD panel. Somebody drew that, and meant it.",
                "Ask what that trader actually did: kept two signals, deleted one, and called it analysis.",
            ),
        ),
        Content(
            title="Even the entry point is subjective",
            lines=(
                "A trendline break looks like a hard, objective fact.",
                "But you chose which two troughs to connect, and another analyst chose differently.",
                "Each act of identification is objective. The choice between them is not.",
            ),
            accent="Individually objective, collectively subjective.",
            caption="The same is true of automated trading: the moment a parameter can be adjusted, subjectivity returns.",
            notes=(
                "This is review question four. Flag it as almost certain to appear.",
                "Use the program trading point to stop them believing automation escapes the problem.",
            ),
        ),
        Figure(
            title="Which trendline calls the reversal?",
            number="1.20",
            shows="One market top with two different uptrend lines drawn under it, A and B, each penetrated at a different price and a different moment.",
            notes=(
                "Make them choose out loud between trendline A and trendline B before you say anything.",
                "Both are correctly drawn. That is individually objective and collectively subjective, in one picture.",
            ),
        ),
        Term(
            term="The price filter",
            plain="You require price to move a set distance past the level before you accept the breakout.",
            example="A fixed peso excursion, a percentage of the breakout price, or a multiple of average true range.",
            formal="A price-based filter validates a breakout by requiring a specified absolute, relative, or volatility-scaled price excursion beyond the trigger level.",
            notes=(
                "Say all three filters exist to solve one problem: the false breakout.",
                "Note these get a full treatment in Chapter 5.",
            ),
        ),
        Term(
            term="The time filter",
            plain="You require the market to hold beyond the level for a set amount of time before you accept it.",
            example="Wait for a set number of bars to close beyond the trendline before entering.",
            formal="A time-based filter validates a breakout by requiring the market to sustain the excursion for a specified duration or number of closed bars.",
            notes=(
                "Ask which filter is more patient. The answer is obvious and that is fine.",
                "Say a time filter costs you price but buys you certainty.",
            ),
        ),
        Term(
            term="The algorithmic filter",
            plain="You require a specific sequence of events, not just a distance or a delay.",
            example="A particular sequence of closed bars, or a sequence of new peaks or troughs, or a retest of the barrier after the break.",
            formal="An algorithmic filter validates a breakout by requiring a defined sequence of price events, such as bar sequences, successive peaks or troughs, or a barrier retest.",
            notes=(
                "Name the three filter families together: price, time, algorithmic.",
                "Say the choice between them is itself subjective, which is the joke of this whole part.",
            ),
        ),
        Figure(
            title="The three filter families beside the trade",
            number="1.21",
            shows="A trendline penetration on the left with a question mark on the entry, and on the right the full list: price-based, time-based and event-based filters.",
            notes=(
                "Read the three headings A, B and C only. Do not read the sub-items; those are Chapter 5.",
                "Point at the question mark on the chart and say every filter on the right is an answer to it.",
                "Name the disagreement honestly: the book's prose calls the third family algorithmic, this diagram of its own calls it event-based, and the book never resolves it.",
            ),
        ),
        Check(
            label="Bias, entries, and filters",
            questions=(
                Q(
                    stem="A chartist uses three oscillators and disregards the one that disagrees with their bullish view. This is:",
                    options=("Complementary analysis",
                             "A confirmatory signal",
                             "Selective perception",
                             "Mean reversion"),
                    answer="C",
                    reason="Heeding only signals that support a preconceived view is selective perception.",
                ),
                Q(
                    stem="Requiring price to close beyond a trendline for a set number of bars before entering is an example of:",
                    options=("A time filter",
                             "A price filter",
                             "An algorithmic filter",
                             "A limit entry order"),
                    answer="A",
                    reason="A requirement expressed in duration or closed bars is a time-based filter.",
                ),
            ),
        ),
        Content(
            title="An exercise: read the chart yourself",
            lines=(
                "1.  You get a plain four hourly chart of USDCAD with nothing drawn on it.",
                "2.  Draw the trendlines you think mark the trend changes.",
                "3.  Compare with the person beside you, then compare with the book.",
            ),
            accent="No marks and no right answer. The differences are the lesson.",
            caption="This is the book's own exercise, on printed pages 27 to 29. You can run it again at home.",
            notes=(
                "Set the rules before the chart goes up: paper or a phone photo, four minutes, no talking on the first pass.",
                "Say the exercise carries no marks, twice if you have to, or half the room will not draw anything.",
            ),
        ),
        Figure(
            title="The chart. Draw your trendlines now.",
            number="1.22",
            shows="A plain four hourly bar chart of USDCAD with no lines, no indicators and no annotations, captioned a basic bar chart and asking what the technical analyst can see.",
            notes=(
                "Stay on this slide for four minutes. Do not advance early, even when the room goes quiet.",
                "Walk the room and look. Do not correct anybody's lines.",
            ),
        ),
        Content(
            title="Now compare with the person beside you",
            lines=(
                "Put the two charts side by side.",
                "Find one trendline you both drew, and one that only one of you drew.",
                "Neither of you has made a mistake.",
            ),
            accent="Two honest analysts, one chart, two readings. You have just produced the argument of this part.",
            notes=(
                "Two minutes. Then ask two pairs to say out loud what differed.",
                "Do not adjudicate. If you pick a winner you have taught the opposite of this part.",
            ),
        ),
        Figure(
            title="Now compare with the book",
            number="1.23",
            shows="The same four hourly USDCAD chart carrying the book's own trendline analysis: a rising line under the first advance, a falling line from the high, a second rising line, and a final falling line down the right hand side.",
            notes=(
                "Show of hands: who drew a line the book does not have? Almost every hand goes up.",
                "Say plainly that the book's lines are not an answer key. They are one more analyst's reading.",
            ),
        ),
        Content(
            title="Second pass: find the chart patterns",
            lines=(
                "Go back to your own chart, the one with no lines on it.",
                "Mark any chart pattern you can name.",
                "If you cannot name any yet, that is expected. We learn them properly later in the course.",
            ),
            accent="Two minutes, then we compare again.",
            notes=(
                "Be explicit that pattern names are not examinable today. This is a look, not a test.",
                "If the room has no vocabulary at all, ask instead where price paused and where it accelerated.",
            ),
        ),
        Figure(
            title="The book's patterns, for comparison",
            number="1.24",
            shows="The same USDCAD chart with six named formations marked: an expanding triangle for uncertainty, a bearish rising wedge, two bearish downtrending channels, a bullish inverted head and shoulders, and a bearish symmetrical triangle at a resistance zone.",
            notes=(
                "Read the six labels off the chart and stop there. Naming patterns properly is a later chapter.",
                "Ask who found the head and shoulders. Somebody usually did, without knowing what it was called.",
            ),
        ),
        Content(
            title="Were there differences? Good.",
            lines=(
                "The book's own answer is that differences here are not errors.",
                "They are merely a consequence of subjectivity.",
                "The fact that you can draw alternate trendlines at all is where subjectivity enters.",
            ),
            accent="You have just watched identification, interpretation and inference happen to one chart, twice.",
            caption="Homework 1 is this exercise on a live platform: find charts showing different trends, draw the trendlines, interpret them.",
            notes=(
                "Land the book's own sentence: do not worry if there are differences, it is merely a consequence of subjectivity.",
                "Bridge forward. The same three steps on a real charting platform is the homework, and the platform session follows this one.",
            ),
        ),
        Content(
            title="Subjectivity shrinks with practice",
            lines=(
                "A novice cannot see the trendlines, the patterns or the angles at first.",
                "With enough chart hours, the same formations become obvious.",
                "The subjectivity never reaches zero, but it falls a long way.",
            ),
            accent="Nothing on this slide can be achieved by reading. Only by looking at charts.",
            caption="Run the exercise again in a month. Your lines will change. The chart will not.",
            notes=(
                "Point back at the exercise they just did and say the second pass will look different in a month.",
                "Say that the point of all of it was to be comfortable with the difference, not to find a winner.",
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Objective chart, subjective analysis",
            "Identifying, interpreting, inferring",
            "Subjectivity in the choice of analysis and studies",
            "Contradictory signals",
            "Confirmatory signals",
            "Complementary signals",
            "Why indicators disagree, and tick volume",
            "The larger formation takes precedence",
            "Equal and opposite interpretations",
            "Selective perception",
            "Individually objective, collectively subjective",
            "Price, time and algorithmic filters",
            "Your own trendlines, against a classmate's and against the book's",
        ),
        notes=(
            "Ask for the three kinds of signal and the rule for resolving pattern conflicts.",
            "Good place to break. Part 5 is the heaviest section of the chapter.",
        ),
    ),
)

# ==========================================================================
# Part 5 - The assumptions the whole subject rests on
# ==========================================================================

PART5 = Section(
    number=5,
    title="The Assumptions Underneath Everything",
    short="Assumptions",
    minutes="About 30 minutes",
    covers=(
        "The three assumptions that make technical analysis possible.",
        "Market discounting, the Efficient Market Hypothesis, and random walk.",
        "The four assumptions you apply at the chart.",
    ),
    slides=(
        Content(
            title="Three assumptions hold the subject up",
            lines=(
                "1.  The market discounts everything.",
                "2.  Market behavior tends to repeat itself.",
                "3.  The market tends to move in trends.",
            ),
            accent="Remove any one of these and technical analysis stops making sense.",
            notes=(
                "Say these three are the load bearing walls. Everything else is decoration.",
                "Tell them assumption one takes the longest, because it has two famous rivals.",
            ),
        ),
        Term(
            term="Market discounting",
            plain="The price you see already contains everything the market knows and expects. You do not need to hunt for the reason.",
            example="A share drifts up for two weeks before good news is announced. The market was already discounting it.",
            formal="Market discounting is the assumption that market action, including price action, reflects all known information in the markets.",
            notes=(
                "Say this is the assumption without which technical analysis would be pointless.",
                "Give the standard caveat straight away: the market discounts everything except acts of God.",
            ),
        ),
        Content(
            title="What the market can and cannot discount",
            lines=(
                "It CAN discount known information.",
                "It CAN discount expectations about known information.",
                "It CAN discount expectations about potential events.",
                "It CANNOT discount unexpected events.",
                "It CANNOT discount unknown information.",
            ),
            accent="Insider activity counts as known information, because the insider's buying moves the price.",
            notes=(
                "Read the two CANNOT lines twice. That is where the exam question lives.",
                "Explain the insider point: the information is non-public, but the trading is visible in the market.",
            ),
        ),
        Content(
            title="What the market is really discounting",
            lines=(
                "Information about actual events.",
                "Expectation about actual events.",
                "Information about expected events.",
                "Expectation about expected events.",
                "Expectation about the possibility of unexpected events.",
            ),
            accent="Not the news alone, but what everyone expects about it.",
            caption="This is why a company can beat expectations and still fall. The good result was already priced.",
            notes=(
                "Read the five lines at pace; the effect is cumulative, not individual.",
                "The caption is the practical payoff. Give a local example if one is fresh.",
            ),
        ),
        Figure(
            title="A semi-efficient market absorbing news",
            number="1.28",
            shows="Three data releases on a price and time axis, with dashed curves showing price adjusting gradually rather than instantly at each one.",
            notes=(
                "Trace one dashed curve with your finger and say that curve is the hour after a jobs report.",
                "Say the gradual bend is where a technical analyst earns a living. A vertical line would leave nothing to trade.",
            ),
        ),
        Figure(
            title="The same thing, on a real chart",
            number="1.29",
            shows="A EURUSD chart around the non-farm payrolls release of 2 August 2013, annotated with the range before the data, the breakout, the traders buying the news and the early traders exiting into it.",
            notes=(
                "Find the labeled release on the chart, then walk the annotations left to right in order.",
                "Say the market took hours, not milliseconds, to settle. That is the semi-efficient market, observed.",
            ),
        ),
        Check(
            label="Discounting",
            questions=(
                Q(
                    stem="Under the basic assumption of technical analysis, the market cannot discount:",
                    options=("Known information",
                             "Expectations about known information",
                             "Insider buying and selling activity",
                             "Unexpected events and unknown information"),
                    answer="D",
                    reason="Unexpected events and unknown information are the two things the market cannot discount.",
                ),
                Q(
                    stem="A company reports strong earnings and the share price falls. The best explanation is that:",
                    options=("The market is irrational",
                             "The strong result was already discounted by expectation",
                             "Technical analysis has failed",
                             "The earnings report was false"),
                    answer="B",
                    reason="Markets discount expectations as well as events, so an anticipated result is already in the price.",
                ),
            ),
        ),
        Term(
            term="The Efficient Market Hypothesis",
            plain="A rival theory saying the market prices everything so perfectly and so fast that no analysis can beat it.",
            example="If EMH held completely, reading a chart or an annual report would both be a waste of an afternoon.",
            formal="The Efficient Market Hypothesis states that for a market to efficiently discount and reflect all information perfectly, all participants must act on all information in the same rational manner instantaneously.",
            notes=(
                "Say this is the most serious academic objection to the whole subject, so treat it seriously.",
                "Warn them the difference between EMH and market discounting is review question two.",
            ),
        ),
        Content(
            title="Efficient, under EMH, means two things",
            lines=(
                "1.  Participants react instantaneously to all market information.",
                "2.  Participants react rationally to all market information.",
            ),
            accent="Both conditions must hold. Failing either one is enough to break the hypothesis.",
            caption="Technical analysis needs neither condition. It only assumes the market discounts what becomes known to it.",
            notes=(
                "The caption is the answer to review question two. Dictate it if you have to.",
                "Say EMH demands perfection; market discounting demands only that the market absorbs what reaches it.",
            ),
        ),
        Figure(
            title="What a perfectly efficient market would look like",
            number="1.27",
            shows="The same three data releases, but price jumps vertically at each one with the time taken to adjust marked as zero.",
            notes=(
                "Point at the vertical jumps and say this is what instantaneous means. No slope, no delay, nothing to trade.",
                "Ask whether any chart they have ever seen looks like this. Their answer is the answer to EMH.",
            ),
        ),
        Content(
            title="Why perfect efficiency cannot happen",
            lines=(
                "Not everyone reacts the same way. Some trade against the news.",
                "Not everyone reacts at the same time. Some act early, some act late.",
                "Not everyone can access the information, and information is never free.",
            ),
            accent="Ask a hundred people to clap the instant a bell rings. You will not get one sound.",
            notes=(
                "Actually do the handclap test with the room. It takes ten seconds and it lands.",
                "Say that if a hundred students cannot coordinate, neither can a million traders.",
            ),
        ),
        Term(
            term="The semi-efficient market",
            plain="The realistic middle ground. The market does absorb new information, just gradually and imperfectly.",
            example="After a jobs report, price swings back and forth for an hour as traders compete for fills, then settles.",
            formal="A semi-efficient market discounts new information at a slower rate, adjusting gradually as participants compete with one another for the best fills.",
            notes=(
                "Say this is the author's position, and it is the defensible one.",
                "Land the conclusion: technical analysis stays valid until markets become perfectly efficient, which they are not.",
            ),
        ),
        Check(
            label="EMH against market discounting",
            questions=(
                Q(
                    stem="Efficient, under EMH, requires that participants react:",
                    options=("Eventually and profitably",
                             "Instantaneously and rationally",
                             "Collectively and cautiously",
                             "Gradually and competitively"),
                    answer="B",
                    reason="EMH requires instantaneous and rational reaction to all market information.",
                ),
                Q(
                    stem="The key difference between market discounting in technical analysis and efficient discounting under EMH is that:",
                    options=("Technical analysis requires perfect efficiency, EMH does not",
                             "EMH ignores insider activity",
                             "There is no real difference between them",
                             "Technical analysis requires only that the market discounts what becomes known to it"),
                    answer="D",
                    reason="Technical analysis imposes no requirement of perfect efficiency, only that everything known is discounted.",
                ),
            ),
        ),
        Term(
            term="The weak form of EMH",
            plain="Current prices already reflect all past price information, so past prices cannot help you.",
            example="If it were true, no chart pattern, trendline or moving average could ever have value.",
            formal="The weak form of EMH suggests that all current prices have already fully discounted all past price information and therefore cannot impact future prices.",
            notes=(
                "Say plainly which analysis each form kills. Weak form kills technical analysis.",
                "Make them write the three forms in order; the department quizzes them directly.",
            ),
        ),
        Term(
            term="The semi-strong form of EMH",
            plain="Once information is public it is already in the price, so public information is useless too.",
            example="Reading the annual report the day it is published gains you nothing.",
            formal="The semi-strong form of EMH suggests that all information, once public, is already reflected in price, making its use unprofitable and pointless.",
            notes=(
                "Say the semi-strong form kills fundamental analysis as well as technical analysis.",
                "That escalation is the pattern they should memorize.",
            ),
        ),
        Term(
            term="The strong form of EMH",
            plain="Everything is in the price, public or private. Nothing anyone knows can help.",
            example="Even an insider with genuinely secret information could not profit from it.",
            formal="The strong form of EMH suggests that all information, whether public or private, is already fully reflected in current price, so all forms of analysis and forecasting are pointless.",
            notes=(
                "Complete the ladder: weak kills technical, semi-strong adds fundamental, strong kills everything.",
                "Ask which form is hardest to believe. The answer is the strong form, and reality agrees.",
            ),
        ),
        Check(
            label="The three forms",
            questions=(
                Q(
                    stem="Which form of EMH holds that even non-public information is already reflected in price?",
                    options=("The strong form",
                             "The weak form",
                             "The semi-strong form",
                             "The random walk form"),
                    answer="A",
                    reason="The strong form covers all information, public and private alike.",
                ),
                Q(
                    stem="Select the accurate statements. I. The weak form implies technical analysis is pointless. II. The semi-strong form implies fundamental analysis is pointless. III. The strong form implies all analysis is pointless. IV. The weak form implies insider information is worthless.",
                    options=("Only I and II are correct",
                             "Only II and III are correct",
                             "Only I, II, and III are correct",
                             "All are correct"),
                    answer="C",
                    reason="Statement IV is false: it is the strong form, not the weak form, that covers non-public information.",
                ),
            ),
        ),
        Term(
            term="Random walk",
            plain="The claim that prices move purely by chance, so nothing that happened before tells you anything. Its second half, that current price has no influence over future price, is the Markovian condition.",
            example="Flipping a coin every minute and plotting the running total. It will look like a chart, and it will mean nothing.",
            formal="Random walk suggests that prices move in a purely random manner, that past prices do not influence current price, and that current price does not influence future price.",
            notes=(
                "Point at the Markovian condition on the slide and say it is the half the exam asks about.",
                "Say this is review question five, and the author's answer is no.",
            ),
        ),
        Figure(
            title="Random walk, EMH, and what they would imply",
            number="1.30",
            shows="Random walk feeding into the three forms of EMH, and both feeding a box listing the consequences: no technical, fundamental or behavioral analysis, no active investing, nobody beats the market.",
            notes=(
                "Read the five consequences in the right hand box out loud. They are deliberately uncomfortable.",
                "Then say the rest of this chapter is an argument that the premises on the left do not hold.",
            ),
        ),
        Content(
            title="Random walk is not the same as EMH",
            lines=(
                "Under EMH, prices do adjust, they just adjust instantly to new information.",
                "Under random walk, prices do not adjust to anything. The motion is purely random.",
            ),
            accent="Markets are driven by perception and expectation, not by random acts of buying and selling.",
            caption="Watch how precisely price reacts at a round number or an old high. Chance does not aim.",
            notes=(
                "Say the distinction in one sentence: EMH says the market is too fast, random walk says it is meaningless.",
                "Give the answer to review question five: no, random walk is not a true reflection of the markets.",
            ),
        ),
        Content(
            title="What actually happens in the real world",
            lines=(
                "Insiders accumulate before the announcement, so price starts moving early.",
                "The public joins after the news is published.",
                "More participants join the now obvious move, and the market overreacts.",
                "The insiders sell into that enthusiasm, and a top forms.",
            ),
            accent="This is herding, and it is the survival instinct from Part 1 doing its work.",
            notes=(
                "Point back to the herd line from the first section. Close the loop.",
                "Say this is why a chart looks nothing like a coin flip.",
            ),
        ),
        Figure(
            title="Insider activity moving price before the news",
            number="1.31",
            shows="Accumulation curving up ahead of each bullish release and distribution curving down ahead of the bearish one, in every case before the announcement.",
            notes=(
                "Point at where the curve starts moving, then at where the news arrives. Mind the gap between them.",
                "Say this is why the market discounts non-public information: the trading is visible even when the information is not.",
            ),
        ),
        Figure(
            title="Market inertia, and the overreaction",
            number="1.32",
            shows="The same releases again, with herd behavior carrying price past the level it should have settled at, then inefficient discounting pulling it back.",
            notes=(
                "Show them the overshoot above the step, then the fall back. That bulge is the crowd arriving late.",
                "Name it: this is the herding instinct from Part 1, drawn as a price curve.",
            ),
        ),
        Content(
            title="Price is not the same as value",
            lines=(
                "A stock valued at 10 pesos can trade at 30 pesos with no change in its fundamentals.",
                "What is being traded is expectation, not absolute worth.",
                "Current price is the result of expectations about future price and value.",
            ),
            accent="Market action is the collective expectation of all its participants.",
            notes=(
                "Ask them for an example of something priced far above what it is worth. They will have one.",
                "Say this reconciles Parts 2 and 5: intrinsic value is real, and price is still about expectation.",
            ),
        ),
        Check(
            label="Random walk and real markets",
            questions=(
                Q(
                    stem="The Markovian condition in random walk states that:",
                    options=("Current price has no influence on future price",
                             "Past prices determine current price",
                             "Prices always revert to a mean",
                             "Volume must confirm the trend"),
                    answer="A",
                    reason="The Markovian condition is that current price carries no influence over future price.",
                ),
                Q(
                    stem="A stock valued at 10 pesos trades at 30 pesos with no change in fundamentals. This best illustrates that:",
                    options=("The market is inefficient by definition",
                             "Price reflects expectation rather than absolute intrinsic value",
                             "Random walk is correct",
                             "The intrinsic value was miscalculated"),
                    answer="B",
                    reason="What is traded is expected value, so price and intrinsic value can diverge widely.",
                ),
            ),
        ),
        Content(
            title="Assumption two: behavior repeats",
            lines=(
                "Past price and chart patterns give a reasonable basis for forecasting.",
                "The reason is human psychology, which changes very slowly.",
                "Fear, greed, hope, anger and regret do not get software updates.",
            ),
            accent="Patterns repeat because people repeat.",
            caption="Every other forecasting method also uses past data: accounting, regression, behavioral finance.",
            notes=(
                "Use the caption to defend the method: criticizing technical analysis for using past data condemns all forecasting.",
                "Connect back to the Pring quote from Part 2.",
            ),
        ),
        Figure(
            title="Repetition you can see: angular symmetries",
            number="1.25",
            shows="A four-hourly USDCAD bar chart with a shallow angle of ascent and a steeper one marked, and the correction that followed each.",
            notes=(
                "Compare the shallow angle with the steeper one, then compare the two falls that followed them.",
                "Say the market did not have to behave this way. It did, and it does, and that is assumption two.",
            ),
        ),
        Figure(
            title="The underlying ordered structure of price",
            number="1.26",
            shows="The same USDCAD chart overlaid with a converging channel and a lattice of symmetry lines, labeled visual evidence of the semi-random nature of price behavior.",
            notes=(
                "Say the word on the chart is semi-random, not random, and that the difference is this whole course.",
                "Warn them honestly: you can draw lines on noise too. That is why Part 4 came first.",
            ),
        ),
        Content(
            title="Three things that erode repeatability",
            lines=(
                "Preempting: traders outbid each other ahead of the trigger, from the self-fulfilling prophecy.",
                "Program trading: machines trade in ways humans cannot replicate.",
                "New participants: each new cohort brings a slightly different approach.",
            ),
            accent="The assumption is reasonable, not guaranteed. That is why Pring said probabilities.",
            notes=(
                "Say preempting is the same stage 4 they met in Part 3. Reward them for remembering.",
                "Do not let this become gloom. The assumption still holds well enough to trade on.",
            ),
        ),
        Content(
            title="Assumption three: the market moves in trends",
            lines=(
                "Trends give the largest profit over the shortest time in the market.",
                "That is why trend based methods dominate the field.",
                "But what exactly is a trend, and when does it stop being one?",
            ),
            accent="Successively higher or lower peaks and troughs is the most widely accepted definition.",
            caption="A trend on one timeframe can be a sideways market on another. Chapter 5 settles the definitions.",
            notes=(
                "Ask the room to define a trend. Their answers will disagree, which proves Part 4.",
                "Say the peaks and troughs definition is the one to write down for now.",
            ),
        ),
        Content(
            title="Trend following is not free",
            lines=(
                "Poor performance in ranging markets, and whipsaws during consolidation.",
                "Low winning percentages, which means large drawdowns.",
                "Trend changes are hard to identify early, and fast markets produce slippage.",
                "Too many trend systems chasing the same move produce inefficient fills.",
            ),
            accent="Every method in this course has a cost. Know the cost before you use the method.",
            notes=(
                "Emphasize low winning percentage. Students assume a good method wins most trades. It does not.",
                "Say back and forward testing is also listed as a difficulty, and we will meet it later.",
            ),
        ),
        Check(
            label="Repetition and trends",
            questions=(
                Q(
                    stem="The underlying reason market behavior tends to repeat is:",
                    options=("Regulation forces similar outcomes",
                             "Prices are mathematically periodic",
                             "Human psychology seldom changes over time",
                             "Charting software enforces patterns"),
                    answer="C",
                    reason="Repetition rests on the reliability and consistency of human behavior.",
                ),
                Q(
                    stem="Which is listed as a challenge to trend following?",
                    options=("It cannot be applied to currencies",
                             "It requires knowledge of intrinsic value",
                             "It only works on daily charts",
                             "Large drawdowns caused by low winning percentages"),
                    answer="D",
                    reason="Low winning percentages and the resulting drawdowns are an explicit challenge to trend following.",
                ),
            ),
        ),
        Content(
            title="Four assumptions you apply at the chart",
            lines=(
                "1.  Price behavior persists until there is evidence to the contrary.",
                "2.  Every bullish reading has an equal and opposite bearish reading.",
                "3.  Extreme bullishness is potentially bearish, and the reverse.",
                "4.  A technical tool matters only because participants say it does.",
            ),
            accent="These four are applied assumptions. They govern what you do, not what you believe.",
            notes=(
                "Say all four are examinable as a set. Number them on the board.",
                "Take them one at a time on the next four slides.",
            ),
        ),
        Term(
            term="Applied assumption one: persistence",
            plain="Whatever the market is currently doing, assume it keeps doing it until something proves otherwise.",
            example="A trend is assumed to continue, a consolidation is assumed to keep ranging, a cycle is assumed to hold until it clearly fails.",
            formal="Price behavior is expected to persist until there is evidence to the contrary. Persistence is the assumed status quo.",
            notes=(
                "Say this is the grand premise from which most other assumptions derive.",
                "Give the practical version: do not fight the market until it gives you a reason.",
            ),
        ),
        Term(
            term="Applied assumption two: equal and opposite",
            plain="Any signal you can read as bullish, someone competent can read as bearish, from the same data.",
            example="Rising oil prices as evidence of a recovering economy, or as evidence of rising costs.",
            formal="For every bullish indication or interpretation, there exists an equal and opposite bearish indication or interpretation for the same price behavior.",
            notes=(
                "Point back to Part 4. This assumption is the formal statement of what subjectivity means.",
                "Say this is why you always need a plan for being wrong.",
            ),
        ),
        Term(
            term="Applied assumption three: extremes invert",
            plain="A reading that is extremely bullish is also a warning, because the market may be exhausted.",
            example="A stochastic reading of 100 percent is explicitly bullish and implicitly bearish at the same time.",
            formal="Extreme bullishness is potentially bearish, and extreme bearishness is potentially bullish, because extremes indicate overextension or exhaustion.",
            notes=(
                "Use the words explicitly and implicitly; the text does, and it is a clean distinction.",
                "Note the exception: this does not always hold for cumulative indicators.",
            ),
        ),
        Term(
            term="Applied assumption four: significance is attributed",
            plain="An indicator has no power of its own. It has exactly as much power as the number of people acting on it.",
            example="A famous trendline produces a big penetration bar because it is famous, not because the line is magic.",
            formal="A technical tool or indicator has no real significance except that attributed to it by market participants.",
            notes=(
                "Say this is the self-fulfilling prophecy in formal dress. Close that loop from Part 3.",
                "Deliver the uncomfortable corollary: even a badly designed indicator becomes reliable if enough capital follows it.",
            ),
        ),
        Check(
            label="The four applied assumptions",
            questions=(
                Q(
                    stem="A stochastic reading of 100 percent is explicitly bullish but potentially bearish. This illustrates which applied assumption?",
                    options=("Persistence",
                             "Equal and opposite readings",
                             "Significance is attributed by participants",
                             "Extreme bullishness is potentially bearish"),
                    answer="D",
                    reason="An extreme reading signals overextension, so extreme bullishness carries a bearish warning.",
                ),
                Q(
                    stem="A poorly designed indicator starts producing reliable signals because a large number of traders risk capital on it. This illustrates:",
                    options=("The weak form of EMH",
                             "Random walk",
                             "Applied assumption four, significance attributed by participants",
                             "Mean reversion"),
                    answer="C",
                    reason="A tool has only the significance participants give it, which is the self-fulfilling prophecy formalized.",
                ),
            ),
        ),
        Content(
            title="Where technical analysis works best",
            lines=(
                "On long timeframes, fundamental analysis carries a lot of the forecasting load.",
                "On very short timeframes, fundamental analysis is nearly useless.",
                "The smaller your stop, the more the forecast depends on technical work.",
            ),
            accent="This is why technical analysis is generally more reliable at lower timeframes.",
            notes=(
                "Say this quietly contradicts what most beginners assume, which is that short term is pure noise.",
                "Explain the stop size argument in one sentence before moving on.",
            ),
        ),
    ),
    recap=Recap(
        items=(
            "Market discounting, and what it cannot discount",
            "What markets are really discounting",
            "The Efficient Market Hypothesis",
            "Instantaneous and rational reaction",
            "The semi-efficient market",
            "The weak, semi-strong and strong forms",
            "Random walk and the Markovian condition",
            "Real world discounting, insiders and overreaction",
            "Price versus value, and expected value",
            "Behavior repeats, and what erodes it",
            "The market moves in trends, and what that costs",
            "The four assumptions in application",
        ),
        notes=(
            "Ask for the three forms of EMH in order. Do not move on until someone gets it.",
            "This is the heaviest recap in the chapter. Take a full minute on it.",
        ),
    ),
)

# ==========================================================================
# Part 6 - Who is in the market, and what they trade
# ==========================================================================

PART6 = Section(
    number=6,
    title="Who Is In The Market",
    short="Participants",
    minutes="About 25 minutes",
    covers=(
        "The eight categories of market participant.",
        "Two other ways to sort them: by time, and by method.",
        "The main markets, and the instruments derived from them.",
    ),
    slides=(
        Content(
            title="The cast of a market",
            lines=(
                "Average investors and traders. Financial institutions.",
                "Commercial banks and central banks. Hedgers and arbitrageurs.",
                "Brokers, hedge funds, mutual funds and pension funds.",
            ),
            accent="Every price you see is one of these people disagreeing with another one.",
            notes=(
                "Say a trade requires two people who disagree about price and agree on a number.",
                "Ask which of these groups the students themselves would be. Most will say retail.",
            ),
        ),
        Term(
            term="Retail and institutional participants",
            plain="Retail means individuals trading their own money. Institutional means organizations trading other people's money at scale.",
            example="You with a 20,000 peso account are retail. A pension fund moving 200 million pesos is institutional.",
            formal="Retail participants trade their own capital in comparatively small size; institutional participants deploy pooled or corporate capital in size sufficient to move markets.",
            notes=(
                "Say size is the real difference, and size changes what strategies are even possible.",
                "Note institutions cannot enter or exit quickly, which is a disadvantage the retail trader has.",
            ),
        ),
        Term(
            term="Speculators and investors",
            plain="A speculator is paid for taking on price risk over a shorter horizon. An investor holds for the longer term return.",
            example="A speculator buys expecting a move this month. An investor buys expecting dividends and growth for a decade.",
            formal="Speculators assume price risk in pursuit of gain from price movement; investors commit capital for longer term return from the asset itself.",
            notes=(
                "Say the word speculator is not an insult. Speculators supply the liquidity everyone else uses.",
                "Draw the line by holding period, not by attitude.",
            ),
        ),
        Check(
            label="Who is who",
            questions=(
                Q(
                    stem="A pension fund deploying pooled retirement contributions is best classified as:",
                    options=("An institutional participant",
                             "A retail participant",
                             "A hedger",
                             "A novice"),
                    answer="A",
                    reason="Institutional participants deploy pooled or corporate capital at scale.",
                ),
                Q(
                    stem="How many main categories of market participant does the chapter identify?",
                    options=("Four",
                             "Six",
                             "Eight",
                             "Ten"),
                    answer="C",
                    reason="Eight: retail, institutional, speculator, supply side, demand side, professional, investor and novice.",
                ),
            ),
        ),
        Term(
            term="Supply side and demand side",
            # The book lists these two among its eight categories and defines
            # neither, anywhere. The deck teaches only what the text teaches,
            # so the gap is the lesson and the readings are an aside. There is
            # deliberately no formal definition row: render_term skips an empty
            # one, and its absence is the point.
            plain="The book lists both of these among its eight categories of market participant, and then defines neither of them anywhere in the book.",
            example="Aside, not examinable. Two readings circulate outside the text. One makes the supply side the providers of the market service, brokers, exchanges, market makers and data vendors, and the demand side the funds and traders who use them. The other makes the supply side producers hedging their output and the demand side consumers hedging their input.",
            formal="",
            notes=(
                "Say plainly that this is the one pair in the chapter the book leaves undefined, so we teach the gap and not a ruling.",
                "Read the aside once, name both readings, and tell them no quiz item is set on either.",
            ),
        ),
        Term(
            term="Professionals and novices",
            plain="A professional does this for a living, with a process. A novice is still building one.",
            example="Everyone in this room is a novice today. That is the correct and useful answer.",
            formal="Professionals participate as an occupation, with defined process and risk control; novices participate without established process or experience.",
            notes=(
                "Say novice is a stage, not a verdict, and every professional was one.",
                "Connect to Part 4: subjectivity in pattern recognition falls with practice.",
            ),
        ),
        Term(
            term="Discretionary and nondiscretionary traders",
            plain="A discretionary trader decides each trade themselves. A nondiscretionary trader follows a fixed system without overriding it.",
            example="Reading the chart and deciding is discretionary. Letting a coded rule fire the order is nondiscretionary.",
            formal="Discretionary traders exercise judgement on each decision; nondiscretionary traders execute a predefined rule set without discretionary intervention.",
            notes=(
                "Remind them of Part 4: even a nondiscretionary system was designed subjectively.",
                "Ask which one they think they would be. Most say nondiscretionary and most are wrong.",
            ),
        ),
        Check(
            label="Categories and methods",
            questions=(
                Q(
                    stem="A trader who executes a fully coded rule set without overriding it is:",
                    options=("Nondiscretionary",
                             "Discretionary",
                             "A hedger",
                             "A scalper"),
                    answer="A",
                    reason="Nondiscretionary means following the predefined rules without discretionary intervention.",
                ),
                Q(
                    stem="Which pair is distinguished mainly by holding period and by who is paid for taking on price risk?",
                    options=("Retail and institutional",
                             "Speculator and investor",
                             "Professional and novice",
                             "Discretionary and nondiscretionary"),
                    answer="B",
                    reason="A speculator is paid for assuming price risk over a shorter horizon; an investor commits capital for the longer term return from the asset itself.",
                ),
            ),
        ),
        Content(
            title="Sorted by time spent in the market",
            lines=(
                "Scalpers: in and out within seconds or minutes.",
                "Day traders: every trade closed within the same trading day.",
                "Swing traders: technical reversals lasting a few days to a week.",
                "Position traders: a few months up to a year.",
                "Investors: buy and hold.",
            ),
            accent="Same market, five completely different jobs.",
            notes=(
                "Ask which rung they would want to be on. Then ask which one has the most screen time.",
                "Say the course objective explicitly names categorizing participants by time in markets.",
            ),
        ),
        Figure(
            title="Participants by time in the market",
            number="1.33",
            shows="Scalpers, day traders, swing traders, position traders and investors laid out left to right, from seconds at one end to buy and hold at the other.",
            notes=(
                "Read the five boxes left to right and let the holding period stretch as you go.",
                "Ask them to place themselves on the diagram. Most will land between swing and investor.",
            ),
        ),
        Content(
            title="Sorted by method",
            lines=(
                "Scalpers: very rapid long and short trades, buying the bid and selling the ask.",
                "Trend traders: catching trends and trailing the position.",
                "Reversal traders: catching key levels, often through mean reversion.",
                "Scale traders: averaging against price until it turns.",
                "Investors: buy and hold.",
            ),
            accent="The same two bets from Part 3, wearing different clothes.",
            caption="Scale trading is the highest risk method on this list. Averaging into a loss is how accounts end.",
            notes=(
                "Close the loop with Part 3 explicitly; these are the same two bets in different clothes.",
                "Give the warning on scale trading plainly. It is the one item here with a real hazard.",
            ),
        ),
        Figure(
            title="Participants by trading methodology",
            number="1.34",
            shows="The same five columns re-sorted by method: scalpers, trend traders, reversal traders, scale traders and investors, each with what it is attempting to do.",
            notes=(
                "Hold this beside the previous diagram: the same word scalper, but sorted by method rather than by clock.",
                "Point at reversal traders and trend traders and say those are the two bets from Part 3.",
            ),
        ),
        Content(
            title="The main markets",
            lines=(
                "Stocks. Fixed income.",
                "Foreign exchange. Commodities.",
                "Real estate.",
            ),
            accent="These are the underlying markets. Everything else is built on top of them.",
            notes=(
                "Count five. Ask which of the five they have personally participated in.",
                "Bridge to derivatives on the next slide.",
            ),
        ),
        Figure(
            title="The markets, and the instruments built on them",
            number="1.35",
            shows="Five underlying markets on the right, stocks through real estate, and five derivative instruments on the left, options through exchange traded funds.",
            notes=(
                "Read the right hand column first: those are the real things. Then the left: those are claims on them.",
                "Say both lists run to five, and both are the kind of list a quiz asks you to reproduce.",
            ),
        ),
        Term(
            term="Derivative",
            plain="An instrument whose value comes from something else. You get exposure to the thing without owning the thing.",
            example="Options, futures, contracts for difference, spread betting, and exchange traded funds.",
            formal="A derivative is an instrument that provides access to an underlying market, deriving its value from that underlying.",
            notes=(
                "Say the word derivative simply means derived from. That deflates most of the fear around it.",
                "Name the five instrument types once; they are a list students are expected to reproduce.",
            ),
        ),
        Content(
            title="Five ways to own gold",
            lines=(
                "Buy physical gold. That is the main market.",
                "Buy or sell a gold futures contract. Derivative.",
                "Buy or sell a gold options contract. Derivative.",
                "Buy shares in a gold backed exchange traded fund. Derivative.",
                "Trade gold through a contract for difference. Derivative.",
            ),
            accent="One underlying, five different instruments, five different risk profiles.",
            notes=(
                "Walk down the list and ask which one requires a vault. Only the first.",
                "Say the choice of instrument is a separate decision from the choice of market.",
            ),
        ),
        Check(
            label="Markets and instruments",
            questions=(
                Q(
                    stem="Buying shares in a gold backed exchange traded fund is participation in gold through:",
                    options=("The main market",
                             "A derivative",
                             "A hedge",
                             "Arbitrage"),
                    answer="B",
                    reason="Only buying the physical metal is main market participation; an ETF derives its value from gold.",
                ),
                Q(
                    stem="Select the accurate statements. I. Scalpers are normally in and out within seconds or minutes. II. Position traders hold for a few months to a year. III. Swing traders close all trades within the same day. IV. Investors follow a buy and hold strategy.",
                    options=("Only I and II are correct",
                             "Only II, III, and IV are correct",
                             "Only I, II, and IV are correct",
                             "All are correct"),
                    answer="C",
                    reason="Statement III describes day traders; swing traders hold for a few days to a week.",
                ),
            ),
        ),
    ),
    recap=Recap(
        items=(
            "The eight categories of market participant",
            "Retail and institutional",
            "Speculator and investor",
            "Supply side and demand side",
            "Professional and novice",
            "Discretionary and nondiscretionary traders",
            "Sorted by time: scalper to investor",
            "Sorted by method: scalper to investor",
            "The five main markets",
            "Derivatives and the five instruments",
            "Five ways to participate in gold",
        ),
        notes=(
            "Ask for the eight categories. Accept six and prompt for the rest.",
            "That is the whole chapter. Move to the wrap up.",
        ),
    ),
)

# ==========================================================================
# Closing
# ==========================================================================

CLOSING = (
    Content(
        title="Chapter 1 in five sentences",
        lines=(
            "Technical analysis is the study of market action.",
            "It identifies what has happened, and it forecasts what might.",
            "It rests on discounting, repetition, and trends.",
            "It is subjective, and so is every other kind of analysis.",
            "It deals in probabilities, never in certainties.",
        ),
        accent="If you remember the last line, you will make fewer expensive mistakes than most people.",
        notes=(
            "Read all five slowly. This is the summary students should copy verbatim.",
            "Return to the Pring quote and end on it.",
        ),
    ),
    Content(
        title="The review questions to prepare",
        lines=(
            "What is a good definition of technical analysis?",
            "List as many advantages and disadvantages of technical analysis as you can.",
            "What are the challenges to technical analysis?",
            "How does market discounting differ from EMH, and what are its three levels?",
            "How are conflicting signals resolved, and why is a trend change subjective?",
            "Is random walk a true reflection of the markets?",
        ),
        accent="All eight of the book's review questions, answered today.",
        notes=(
            "Tell them where each answer sits: Part 2, Part 3, Part 3, Part 5, Part 4, Part 5.",
            "Say lines four and five each carry two of the book's eight questions.",
            "Set the expectation that these appear on the quiz in the department's four statement format.",
        ),
    ),
    Closing(
        title="Next: Dow Theory",
        lines=(
            "Chapter 2 gives us the six tenets that modern technical analysis is built on.",
            "Bring the four trading verbs and the three assumptions with you. You will need them.",
            "Before then: open any chart, draw your trendlines, and compare with a classmate.",
        ),
        accent="FIN1209  Technical Analysis in Investment  |  Institute of Accounts, Business and Finance",
        notes=(
            "Name the exact preparation you want done before the next meeting.",
            "Remind them that quiz 1 covers chapters 1 and 2 together.",
        ),
    ),
)

# ==========================================================================

CHAPTER = Chapter(
    course="Technical Analysis in Investment",
    code="FIN1209",
    chapter="Chapter 1",
    title="Introduction to the Art and Science of Technical Analysis",
    subtitle="Institute of Accounts, Business and Finance  |  Far Eastern University Manila",
    presenter="Benjamin C. Sotelo",
    objectives=(
        "Understand the key concepts underlying technical analysis.",
        "Identify the different forms of chart analysis.",
        "Describe the objectives of technical analysis.",
        "Understand what subjectivity means in technical analysis.",
        "Recognize the strengths and weaknesses of technical analysis.",
        "Categorize market participants by style and time in markets.",
        "Identify the various styles and approaches in technical analysis.",
    ),
    roadmap=(
        "Part 1  Why anybody analyzes a market",
        "Part 2  Three ways to forecast a price",
        "Part 3  Classifying technical analysis",
        "Part 4  Subjectivity",
        "Part 5  The assumptions underneath everything",
        "Part 6  Who is in the market",
    ),
    sections=(PART1, PART2, PART3, PART4, PART5, PART6),
    closing=CLOSING,
)
