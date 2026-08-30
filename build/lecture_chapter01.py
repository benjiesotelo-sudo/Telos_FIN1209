"""FIN1209 Chapter 1 student lecture notes, as plain data.

This is the file a contributor edits. Layout lives in build/lecturekit.py and
knows nothing about any chapter; the reasoning behind the layout, with the
research it came from, is chapter-01/lecture-notes-design.md.

    .venv/bin/python build/build_lecture_notes.py

Written for a student reading alone, with no instructor in the room. Full
sentences that explain, not bullets that gesture. The six sections are the
deck's six parts in the deck's order, so a student can move between the two.

Nothing here is timing, cut tiers, speaker cues, check answers or slide
numbers. Those belong to the instructor and they live in
build/plan_chapter01.py.

Figure descriptions are never retyped here. The build takes them from
content_chapter01.py, which is also where the deck's own placeholder takes
them, so the two documents cannot describe the same figure differently.

Chapter 2 is a copy of this file with different content in it.
"""

from __future__ import annotations

from lecturekit import (Define, Fig, Head, LectureNotes, Panel, Para, Points,
                        Quote, Section, SelfCheck)


# ==========================================================================
# Section 1 - Why anybody analyses a market
# ==========================================================================

SECTION1 = Section(
    number=1,
    title="Why Anybody Analyses a Market",
    standfirst="Where the urge to make a profit comes from, the one rule "
               "every trade in the world is trying to obey, and the two jobs "
               "technical analysis actually does.",
    blocks=(
        Head(number="1.1", text="The instincts underneath a market"),
        Para(text=(
            "A market looks like an institution, but the behaviour running "
            "underneath it is older than any institution. The chapter opens "
            "on three human instincts: to survive, to seek comfort, and to "
            "propagate. Survival is the strongest and usually comes first, "
            "and what it contains matters more than the list: staying alive, "
            "satisfying hunger, seeking safety by staying with the group or "
            "the herd, and avoiding danger. Hold on to the third one. "
            "**Herding explains more charts in this course than any other "
            "single behaviour**, and it returns in Section 5."
            "\n\n"
            "Profit needs one more ingredient: something has to change. You "
            "cannot profit from a thing whose value never moves, so you need "
            "a variable of change, something you can hold whose value shifts. "
            "A house, a sack of rice, a currency, a share. Markets exist "
            "because value moves, and analysis exists because we would like "
            "to know which way."
        )),

        Head(number="1.2", text="Price, and the rule every trade is obeying"),
        Para(text=(
            "Of all the variables of change available to us, price is the "
            "most convenient: visible, public, free to observe, and updated "
            "constantly. If Jollibee closed at 240 pesos yesterday and 244 "
            "today, you needed nobody's permission to know it. Price is the "
            "primary data of this subject, followed closely by volume."
        )),
        Define(
            term="Price",
            text="Price is the observable variable of change on which market "
                 "participants act, and the primary data of technical "
                 "analysis.",
        ),
        Para(text=(
            "Once you have a variable that moves, one mechanical rule would "
            "guarantee a profit every time. Buy at 40 pesos, sell at 52, keep "
            "12 a share. Nothing clever has happened, and yet the rule is "
            "complete."
        )),
        Define(
            term="The buy low, sell high principle",
            text="The buy low, sell high principle is the mechanical rule "
                 "that profit is realised by acquiring at a lower price and "
                 "disposing at a higher one.",
        ),
        Para(text=(
            "The rule is easy. Obeying it is not. To buy low you must know "
            "that today's price is a low one, and to sell high that today's "
            "is a high one. Both are statements about the future, not the "
            "present. **That gap between the rule and the knowledge it needs "
            "is where chance enters, and it is the whole reason this subject "
            "exists.**"
        )),

        Head(number="1.3", text="The price-time chart"),
        Para(text=(
            "Profit requires effective action in two dimensions, not one, so "
            "traders track price against time. It is not enough to know that "
            "a share is worth more than it costs; you also have to know when "
            "to act. Any chart on a trading app is this object: pesos up the "
            "side, days along the bottom."
        )),
        Define(
            term="The price-time chart",
            text="A price-time chart is a two dimensional visualisation that "
                 "plots price on the vertical axis against time on the "
                 "horizontal axis.",
        ),

        Head(number="1.4", text="The two jobs technical analysis does"),
        Para(text=(
            "Everything in this course is one of two jobs. The first is "
            "record keeping: the chart says what the market has already done, "
            "with no opinion attached. The second is opinion: you take the "
            "record and make a claim about what comes next. The pair is the "
            "dual function of technical analysis, and separating them matters, "
            "because the first is objective and the second is not."
        )),
        Define(
            term="Identification",
            text="Identification is the descriptive function of technical "
                 "analysis: it records and describes past and present price "
                 "and market action.",
        ),
        Define(
            term="Forecasting",
            text="Forecasting is the inferential function of technical "
                 "analysis: it interprets identified market action to infer "
                 "potential future price behaviour.",
        ),
        Para(text=(
            "Identification alone hands you a great deal before you risk a "
            "peso, and it is free. A five year chart gives the average size "
            "of a normal day's move, the highest and lowest prices ever paid, "
            "the levels where the market stalls and drifts sideways, how much "
            "trading actually happens, and how often price gaps. None of that "
            "is a forecast, and all of it is homework worth doing before any "
            "trade."
            "\n\n"
            "Forecasting rests on an assumption, that price behaviour repeats "
            "to some reasonable degree, and Section 5 tests it. For now: "
            "prices bouncing off 100 pesos four times is a fact, expecting "
            "buyers a fifth time is an opinion."
        )),

        Head(number="1.5", text="Four words, and four ways to make money"),
        Para(text=(
            "Four verbs describe every position anyone can hold, in two "
            "pairs: one pair opens and closes a bet that price will rise, the "
            "other a bet that price will fall."
        )),
        Define(term="To go long", text="To go long means to buy to open a new "
                                       "position."),
        Define(term="To liquidate", text="To liquidate means to sell to close "
                                         "a position previously held."),
        Define(term="To go short", text="To go short means to sell to open a "
                                        "new position."),
        Define(term="To cover", text="To cover means to buy to close a "
                                     "position previously shorted."),
        Para(text=(
            "Shorting feels backwards the first time. You sell borrowed "
            "shares at 660 pesos, buy them back at 610, return them, and keep "
            "the difference. Short selling is restricted in the Philippine "
            "market, but the concept is examinable and standard elsewhere. "
            "Note that **buying is not always bullish**: covering is a "
            "purchase that ends a bearish position."
        )),
        Fig(
            panels=(Panel(number="1.1"),),
            cols=1,
            height_mm=64.0,
            caption="The two directions a trade can run, with the jargon for "
                    "each leg and the demand or supply that each one creates.",
        ),
        Para(text=(
            "Figure 1.1 draws both directions side by side, and it corrects "
            "a common misreading: there are four ways a trade makes money, "
            "not one. Long at a low price, liquidate higher. Long at a high "
            "price, liquidate higher still. Short at a high price, cover "
            "lower. Short at a relatively low price, cover lower again. **Buy "
            "low, sell high is only the first of the four**, and the other "
            "three are just as ordinary."
        )),
        SelfCheck(text=(
            "A trader sells 1,000 shares at 92 pesos that they do not own, "
            "then buys them back at 78 pesos. Which two of the four verbs "
            "have they used, in which order, and did they buy low and sell "
            "high?"
        )),
    ),
)


# ==========================================================================
# Section 2 - Three ways to forecast a price
# ==========================================================================

SECTION2 = Section(
    number=2,
    title="Three Ways to Forecast a Price",
    standfirst="Fundamental, information and technical analysis all answer "
               "the same question. They disagree about what evidence counts, "
               "and only one of them is any good at timing.",
    blocks=(
        Head(number="2.1", text="Three approaches, one question"),
        Para(text=(
            "Three main approaches forecast potential price action. "
            "Fundamental analysis asks what the thing is worth, information "
            "analysis asks what the news says, and technical analysis asks "
            "what the market itself is doing. All three are answering the "
            "same question: where does price go next?"
        )),
        Fig(
            panels=(Panel(number="1.2"),),
            cols=1,
            height_mm=68.0,
            caption="The three approaches to price forecasting, each with the "
                    "evidence it is willing to use.",
        ),
        Para(text=(
            "Figure 1.2 sets them out with their inputs. Notice how much "
            "wider the technical column is: price, volume, sentiment, open "
            "interest, market cycles, flow of funds, relative strength, broad "
            "market activity. Fundamental analysis works from one quantity, "
            "intrinsic value; information analysis from public and non-public "
            "information."
        )),

        Head(number="2.2", text="Fundamental analysis and intrinsic value"),
        Para(text=(
            "A fundamentalist reads a company's financial statements, works "
            "out what the business is genuinely worth, and compares that to "
            "the price on the screen: San Miguel's annual report says 130 "
            "pesos a share, the market says 98."
        )),
        Define(
            term="Fundamental analysis",
            text="Fundamental analysis estimates the value of a security from "
                 "its financial performance and position, in order to judge "
                 "whether the current price is justified.",
        ),
        Define(
            term="Intrinsic value",
            text="Intrinsic value is the worth of a security in light of all "
                 "its holdings, debt, earnings, dividends, income, balance "
                 "sheet activity and cash flow.",
        ),
        Para(text=(
            "Comparing the two gives the pair of words most often reversed "
            "on quizzes. Price below intrinsic value means the stock is "
            "**undervalued**: buyers should appear, creating potential "
            "demand. Price above intrinsic value means it is **overvalued**: "
            "sellers should appear, creating potential supply."
        )),
        Fig(
            panels=(Panel(number="1.3", label="Price below value: potential "
                                              "demand."),
                    Panel(number="1.4", label="Price above value: potential "
                                              "supply.")),
            cols=2,
            height_mm=50.0,
            caption="The same diagram twice, inverted. Read the direction of "
                    "the arrow before you read the labels.",
        ),
        Para(text=(
            "Figure 1.3 puts a value of 25 dollars above a price of 20, so "
            "investors buy. Figure 1.4 inverts it, a price of 25 against a "
            "value of 20, so investors sell or stay in cash. Be careful with "
            "undervalued. **It means cheap relative to worth. It does not mean "
            "the price will rise today**, and nothing in the diagram says when "
            "the buying arrives."
        )),
        Para(text=(
            "The route from accounts to a number runs through ratios: price "
            "to earnings, price to earnings growth, price to book, price to "
            "sales, debt to equity, earnings per share. Analysts reach them "
            "from two directions."
        )),
        Define(
            term="The top-down approach",
            text="A top-down approach studies broad market factors and sector "
                 "rotation models in order to select stocks within a "
                 "strengthening industry or sector.",
        ),
        Define(
            term="The bottom-up approach",
            text="A bottom-up approach relies primarily on a specific "
                 "company's own fundamental performance rather than on sector "
                 "or market conditions.",
        ),
        Para(text=(
            "Deciding that banking will do well and then choosing between "
            "BDO, BPI and Metrobank is top-down. Liking one shipping firm's "
            "balance sheet and buying it although shipping is weak is "
            "bottom-up."
            "\n\n"
            "Fundamental analysis has three honest limits. Accounts can be "
            "dressed up, misreported or falsified. An audited report is "
            "already old by the time it is published. And it never gives a "
            "precise price or a precise moment to act. **None of those ratios "
            "tells you what to do at 9:31 tomorrow morning.**"
        )),

        Head(number="2.3", text="Information analysis"),
        Para(text=(
            "The second approach forecasts from what you read: newspapers, "
            "bulletins, online reports, company announcements. A quarterly "
            "result beats expectations, so you expect a higher open."
        )),
        Define(
            term="Information analysis",
            text="Information analysis forms an opinion about potential "
                 "market action from information gleaned from public sources.",
        ),
        Para(text=(
            "The difficulty is that public information is usually late. "
            "Whoever held non-public material information has already moved "
            "the market, so by the time the news is public only an "
            "inconsequential part of the move remains. Acting on non-public "
            "material information is insider trading and it is illegal. In "
            "unregulated over the counter markets, brokers front running "
            "large client orders is the same problem under another name. "
            "**The technical analyst sees the move on the chart and acts, "
            "without waiting to be told the reason.**"
        )),

        Head(number="2.4", text="Technical analysis, in six definitions"),
        Para(text=(
            "The third approach reads the market's own behaviour. You do not "
            "know why the buyers came, only that they came at 250 pesos, "
            "three times."
        )),
        Define(
            term="Technical analysis",
            text="Technical analysis is the identification and forecasting of "
                 "potential market behaviour based largely on the action and "
                 "dynamics of the market itself.",
        ),
        Para(text=(
            "Six short definitions from the standard authorities are worth "
            "memorising, because each adds something the others leave out."
        )),
        Quote(text="Technical analysis is the study of market action, "
                   "primarily through the use of charts, for the purpose of "
                   "forecasting future price trends.",
              source="John Murphy, Technical Analysis of the Financial "
                     "Markets (NYIF, 1999)"),
        Quote(text="Technical analysis is the science of recording, usually "
                   "in graphic form, the actual history of trading ... then "
                   "deducing from that pictured history the probable future "
                   "trend.",
              source="Edwards and Magee, Technical Analysis of Stock Trends "
                     "(AMACOM, 2007)"),
        Quote(text="It refers to the study of the action of the market itself "
                   "as opposed to the study of the goods in which the market "
                   "deals.",
              source="Edwards and Magee, Technical Analysis of Stock Trends "
                     "(AMACOM, 2007)"),
        Quote(text="The art of technical analysis, for it is an art, is to "
                   "identify a trend reversal at a relatively early stage and "
                   "ride on that trend until the weight of the evidence shows "
                   "or proves that the trend has reversed.",
              source="Martin Pring, Technical Analysis Explained, 4th edition "
                     "(McGraw-Hill, 2002)"),
        Quote(text="Technical analysis deals in probabilities, never in "
                   "certainties.",
              source="Martin Pring, Technical Analysis Explained, 4th edition "
                     "(McGraw-Hill, 2002)"),
        Quote(text="Market price tends to lead the known fundamentals ... "
                   "Market price acts as a leading indicator of the "
                   "fundamentals.",
              source="John Murphy, Technical Analysis of the Financial "
                     "Markets (NYIF, 1999)"),
        Para(text=(
            "Read them as a set. Murphy names the tool and the target. "
            "Edwards and Magee put the record first and the deduction second, "
            "and make the subject of study the market rather than the goods. "
            "Pring gives the objective, catch a reversal early and stay until "
            "the evidence turns, and then the sentence that keeps a trader "
            "solvent: **probabilities, never certainties**. Murphy's second "
            "line is the timing claim: price often moves before the news "
            "explains it."
        )),

        Head(number="2.5", text="What each approach gives you"),
        Para(text=(
            "The practical difference between the two main approaches is "
            "timing, and the vocabulary makes it obvious. Technically based "
            "timing gives precise entry and exit prices and the precise time "
            "of each; real time bullish and bearish signals and price "
            "triggers; scaling in and out at significant levels; entries "
            "timed to volatility and order flow; exits from an extended trend "
            "at a technically significant reversal level; risk defined as a "
            "percentage of real price levels; volume and open interest to "
            "gauge the strength of a move, and breadth and sentiment to gauge "
            "it more broadly; and forecast peaks and troughs from cycle and "
            "seasonality analysis. **Count how many of those contain the word "
            "precise.**"
            "\n\n"
            "Fundamentally based timing gives undervalued stocks that could "
            "appreciate, overvalued stocks that could depreciate, and strong "
            "stocks to rotate into. All three arrive without a precise price "
            "and without a precise time."
            "\n\n"
            "So the fundamentalist works from intrinsic value, wants the "
            "underlying cause of a move, focuses on which company to hold, "
            "and can say what to buy but not when. The technical analyst "
            "works from the structure and dynamics of price, is more "
            "interested in effects than causes, usually cannot determine "
            "intrinsic value at all, and can say precisely when. Cause, "
            "company, value against effect, price, timing. **Neither column "
            "is complete alone, and most professionals use both.**"
        )),

        Head(number="2.6", text="What the market gives you to read"),
        Para(text=(
            "Market action arrives in six streams: price action, volume "
            "action, open interest action, sentiment, market breadth and flow "
            "of funds. Price matters most, followed closely by volume; flow "
            "of funds includes measures such as margin debt. The smallest "
            "unit of price action is a single bar, and any bar on any "
            "interval is described by four numbers."
        )),
        Define(
            term="OHLC",
            text="OHLC denotes the opening, high, low and closing prices of a "
                 "bar over any chosen interval, from one minute to one year.",
        ),
        Para(text=(
            "A daily bar for Globe might open at 1,800, reach 1,845, fall to "
            "1,792 and close at 1,838. **OHLC is not only daily.** A five "
            "minute bar and a yearly bar each have their own four numbers, and "
            "choosing the interval is the first subjective decision an analyst "
            "makes."
        )),
        SelfCheck(text=(
            "Your classmate says a stock is undervalued and therefore he is "
            "buying it this morning. Which half of that sentence does "
            "fundamental analysis support, and which half does it not?"
        )),
    ),
)


# ==========================================================================
# Section 3 - Classifying technical analysis
# ==========================================================================

SECTION3 = Section(
    number=3,
    title="Classifying Technical Analysis",
    standfirst="Four branches, two opposite bets, and an honest account of "
               "what the method is good at and what it is not.",
    blocks=(
        Head(number="3.1", text="The four branches"),
        Para(text=(
            "Every technique in this course belongs to one of four branches: "
            "one qualitative and visual, one quantitative, one measuring the "
            "mood of the crowd, and one studying the participants themselves."
        )),
        Define(
            term="Classical technical analysis",
            text="Classical technical analysis uses conventional bar, chart "
                 "and candlestick patterns, oscillator and overlay "
                 "indicators, market breadth, relative strength and cycle "
                 "analysis.",
        ),
        Define(
            term="Statistical analysis",
            text="Statistical analysis is the quantitative branch, studying "
                 "dispersion, central tendency, skewness, volatility, "
                 "regression, hypothesis testing, correlation and covariance.",
        ),
        Define(
            term="Sentiment analysis",
            text="Sentiment analysis studies the psychology of market "
                 "participants through polls and surveys, flow of funds, and "
                 "the positions taken by large institutions and hedgers.",
        ),
        Define(
            term="Behavioral analysis",
            text="Behavioral analysis studies how market participants react "
                 "to news, to profits and losses, to the actions of others, "
                 "and to their own psychological and emotional biases.",
        ),
        Fig(
            panels=(Panel(number="1.6"),),
            cols=1,
            height_mm=82.0,
            caption="The four branches with the studies that belong to each, "
                    "and the one line at the foot that applies to all four.",
        ),
        Para(text=(
            "Most of what this course teaches is the first column of Figure "
            "1.6. Pin down the difference between the third and fourth: "
            "sentiment analysis measures what the crowd currently feels, "
            "using put to call ratios, short interest, margin debt and "
            "bullish percent readings, while behavioral analysis studies how "
            "people react, including herd behaviour, loss aversion, "
            "confirmation bias and the gambler's fallacy. **Read the line "
            "across the bottom of the figure.** Whichever branch you use, the "
            "output is still interpreted through filters and biases unique to "
            "you, which is Section 4."
        )),

        Head(number="3.2", text="Two opposite bets about price"),
        Para(text=(
            "Almost every strategy you will meet is one of two bets: that "
            "price has travelled far enough and will come back, or that price "
            "is going somewhere and will keep going. The studies an analyst "
            "chooses follow directly from which bet they are making."
        )),
        Define(
            term="The mean reverting or contrarian approach",
            text="A mean reverting approach expects price to return to an "
                 "average or to a balance between supply and demand, and "
                 "favours studies that pinpoint overbought and oversold "
                 "activity.",
        ),
        Define(
            term="The non-mean reverting or momentum approach",
            text="A non-mean reverting approach expects trends to continue "
                 "through a positive feedback cycle, and favours breakout and "
                 "continuation studies.",
        ),
        Fig(
            panels=(Panel(number="1.7"),),
            cols=1,
            height_mm=84.0,
            caption="The two camps compared column by column: study "
                    "preferences, order types, entry points and rationale.",
        ),
        Para(text=(
            "Figure 1.7 is a useful page to keep. The contrarian buys at "
            "support and sells at resistance, using divergence, regression "
            "lines, moving average bands and Bollinger bands. The momentum "
            "trader does the exact opposite at the same levels, going long on "
            "the breach of resistance and short on the breach of support, "
            "using chart pattern, moving average, Darvas Box and Donchian "
            "channel breakouts. **The line in the figure that gives away the "
            "belief is the order type.**"
        )),
        Define(
            term="Limit and stop entry orders",
            text="Limit entry orders execute at a specified price or better; "
                 "stop entry orders trigger once price trades through a "
                 "specified level.",
        ),
        Para(text=(
            "A contrarian prefers limit orders, because the point is a good "
            "price. A momentum trader prefers stop orders, because the point "
            "is confirmation that the move is under way, and confirmation is "
            "worth paying for."
        )),

        Head(number="3.3", text="Advantages, and honest disadvantages"),
        Para(text=(
            "Technical analysis has three real advantages. It works the same "
            "way on every market, instrument and timeframe, so you need not "
            "learn a new company to trade a new stock. It is visual, so risk "
            "and volatility are easy to see. And it gives timely, precise "
            "entry and exit levels, each arriving with a bullish or bearish "
            "signal before the move rather than after. **One skill, applied "
            "everywhere, is the strongest practical argument for the method.** "
            "A fourth advantage is more awkward: when many participants act "
            "on the same obvious level, the reaction there becomes more "
            "reliable. That one has a name, and it is also a criticism."
            "\n\n"
            "The disadvantages are equally real. The method is subjective, so "
            "one pattern can be read several ways. The repeating tendency it "
            "depends on can be disrupted by shocks and by algorithmic and "
            "high frequency trading. And reading a chart takes practice, "
            "while inferring from one takes far more. Underneath all three "
            "sits one uncomfortable fact: **every bullish reading has an "
            "equal and opposite bearish reading**, which Section 5 states as "
            "a formal assumption."
        )),

        Head(number="3.4", text="The three objections, and the third one"),
        Para(text=(
            "Three serious objections are made to the subject. Random walk "
            "says prices move by pure chance, so patterns mean nothing. The "
            "strong form of the Efficient Market Hypothesis says price "
            "already reflects everything, so no analysis helps. Section 5 "
            "takes both apart. The third objection belongs here."
        )),
        Define(
            term="The self-fulfilling prophecy",
            text="The self-fulfilling prophecy holds that prices react to "
                 "technical signals because of the concerted action of "
                 "participants acting on those signals rather than because of "
                 "the signals themselves.",
        ),
        Para(text=(
            "A trendline breaks, thousands of traders buy the break, price "
            "rises, and the line appears to have worked. The objection is "
            "that nothing about the line was meaningful; only the crowd was. "
            "The effect is genuine, and rather than deny it the text turns it "
            "into a tool: if signals work because they are widely watched, "
            "trade only the clear and obvious ones. But it does not last, "
            "because it runs in a cycle of six stages."
        )),
        Points(numbered=True, items=(
            "A clear and obvious signal attracts participants.",
            "Their concerted action creates reliable price reactions.",
            "Reliable reactions attract even more participants.",
            "Participants begin to preempt each other for better fills.",
            "Reactions drift away from the expected entry level, and "
            "participants abandon the signal.",
            "With the preempting gone, reliable reactions begin to appear "
            "again.",
        )),
        Fig(
            panels=(Panel(number="1.8"),),
            cols=1,
            height_mm=64.0,
            caption="The six stages drawn as a loop, with the advantageous "
                    "and disadvantageous halves marked.",
        ),
        Para(text=(
            "Figure 1.8 draws the cycle as a circle for a reason. Stages one "
            "to three are the advantage, when the signal is worth trading; "
            "stages four to six are the disadvantage; then it repeats. **A "
            "signal is never permanently dead and never permanently alive**, "
            "and the practical question is which part of the loop you are "
            "standing in."
        )),
        SelfCheck(text=(
            "A widely followed moving average has stopped producing clean "
            "bounces, and traders are entering earlier and earlier to get "
            "ahead of each other. Which stage of the cycle is that, and what "
            "does the cycle say happens next?"
        )),
    ),
)


# ==========================================================================
# Section 4 - Subjectivity
# ==========================================================================

SECTION4 = Section(
    number=4,
    title="Subjectivity",
    standfirst="Which half of technical analysis is objective, why two honest "
               "analysts read the same chart differently, and what to do when "
               "your own indicators disagree.",
    blocks=(
        Head(number="4.1", text="An objective chart and a subjective reader"),
        Para(text=(
            "Technical analysis is objective and subjective at once, and it "
            "matters which half is which. The chart is objective: a "
            "historical record that argues with nobody. The analysis is "
            "subjective, because it happens inside a human being. **The data "
            "is not the problem. The reader is.** It also helps to see that "
            "analysis is three activities, not one: identifying price and "
            "indicator patterns, interpreting what the data means, and "
            "inferring what price might do next. Subjectivity enters at all "
            "three, not only the last."
        )),
        Define(
            term="Subjectivity",
            text="Subjectivity is the dependence of analysis on behavioural "
                 "traits, filters and biases unique to each analyst or "
                 "observer.",
        ),
        Para(text=(
            "The practical problem is twofold: which form of analysis should "
            "be applied to this chart at all, and then which indicators? "
            "Neither question has a correct answer. Both have consequences."
        )),

        Head(number="4.2", text="One chart, seven defensible readings"),
        Para(text=(
            "The clearest demonstration in the chapter is one price chart "
            "read seven ways. Figure 1.9 is the chart with nothing on it, the "
            "raw record before anyone has interpreted anything. Everything "
            "after it was added by an analyst."
        )),
        Fig(
            panels=(
                Panel(number="1.9", label="The bare record."),
                Panel(number="1.10", label="Trendlines, short and long term."),
                Panel(number="1.11", label="A moving average as support and "
                                           "resistance."),
                Panel(number="1.12", label="Chart patterns."),
                Panel(number="1.13", label="Regression, and bearish "
                                           "divergence on the CCI."),
                Panel(number="1.14", label="Regression with volume: the "
                                           "buying climax."),
                Panel(number="1.15", label="Volatility bands, volume and "
                                           "MACD."),
            ),
            cols=2,
            height_mm=158.0,
            caption="The same price chart read seven ways. Every reading is "
                    "defensible, and several of them disagree about what "
                    "happens next.",
        ),
        Para(text=(
            "Work through the plate in order. Figure 1.10 adds a short term "
            "downtrend line and a longer term uptrend line, and already the "
            "picture holds an opinion. Figure 1.11 replaces them with a "
            "moving average, marking where it acted as support and where as "
            "resistance. Figure 1.12 annotates chart patterns instead: an "
            "ascending triangle, a head and shoulders, a parabolic move, a "
            "symmetrical triangle breakout, a channel retest. Figure 1.13 "
            "draws regression lines and points out higher highs in price "
            "against lower highs on the CCI, which is standard bearish "
            "divergence. Figure 1.14 keeps the regression and adds volume, "
            "marking a parabolic buying climax with a spike at the blow off. "
            "Figure 1.15 uses volatility bands, volume and MACD, with price "
            "beyond the upper band and MACD historically overbought."
            "\n\n"
            "**Seven analysts, one chart, seven defensible readings, and no "
            "way to call any of them wrong.** That is subjectivity in "
            "practice, and it is not a flaw unique to technical analysis."
        )),

        Head(number="4.3", text="Three ways two signals can relate"),
        Para(text=(
            "Use more than one indicator and they will eventually disagree. "
            "Three relationships are worth naming."
        )),
        Define(
            term="Contradictory signals",
            text="Contradictory signals are indications from two or more "
                 "studies that are in clear and direct opposition to one "
                 "another.",
        ),
        Define(
            term="Confirmatory signals",
            text="Confirmatory signals are indications from separate studies "
                 "that agree with and reinforce the same conclusion.",
        ),
        Define(
            term="Complementary signals",
            text="Complementary signals are apparently opposing indications "
                 "that, once their differing time horizons are recognised, "
                 "combine into a fuller reading of the market.",
        ),
        Para(text=(
            "Contradiction is inevitable rather than a malfunction. "
            "Indicators disagree because the mathematics behind each is "
            "different, because each tracks a different time horizon, because "
            "data may be missing on one platform, and because data quality, "
            "accuracy and type vary between platforms. Tick volume, which "
            "counts transactions regardless of size, is one common source, "
            "and it is why two identical indicators on two platforms can "
            "honestly disagree."
            "\n\n"
            "Confirmation feels comfortable, which makes it dangerous: it "
            "feeds the bias in 4.5. The genuinely useful case is the third. A "
            "20 period reading of slightly overbought beside a 100 period "
            "reading of slightly oversold is not a contradiction. It says the "
            "instrument is cheap for the long term and stretched for the "
            "short term. **The astute trader looks for cheap on both horizons "
            "at once, and enters there.**"
        )),
        Fig(
            panels=(Panel(number="1.16"),),
            cols=1,
            height_mm=60.0,
            caption="One chart with two oscillators below it, reading "
                    "overbought and oversold at the same moment.",
        ),
        Para(text=(
            "Figure 1.16 is that situation on a real chart: the faster "
            "oscillator reads overbought at the exact moment the slower one "
            "reads oversold. Neither instrument is broken."
        )),

        SelfCheck(text=(
            "Your 14 period stochastic says overbought and your 100 period "
            "stochastic says oversold. Are those contradictory or "
            "complementary signals, and what would each answer lead you to "
            "do?"
        )),

        Head(number="4.4", text="Resolving conflicting chart patterns"),
        Para(text=(
            "Chart patterns conflict in the same way, and here the chapter "
            "gives an actual rule. Measure the size of each pattern; the "
            "sentiment of the larger formation takes precedence, because "
            "larger patterns speak for the longer term. A bullish ascending "
            "triangle containing a bearish head and shoulders stays bullish "
            "until the neckline breaks. **That one rule removes a large slice "
            "of the subjectivity in reading formations.**"
        )),
        Fig(
            panels=(
                Panel(number="1.17", label="Conflicting: bullish, neutral and "
                                           "bearish at once."),
                Panel(number="1.18", label="Agreeing: every formation "
                                           "bearish."),
            ),
            cols=2,
            height_mm=54.0,
            caption="The hard case beside the easy one.",
        ),
        Para(text=(
            "Figure 1.17 is the hard case: an ascending triangle marked "
            "bullish, a symmetrical triangle neutral, and a complex head and "
            "shoulders bearish, all inside the same stretch of price. Figure "
            "1.18 is the idealised case where two descending triangles and a "
            "complex head and shoulders all point the same way. Real charts "
            "look like the first more often than the second."
        )),

        Head(number="4.5", text="The same fact, read two ways"),
        Para(text=(
            "Oil rises sharply. One analyst calls it bearish, because costs "
            "rise across the economy. Another calls it bullish, because "
            "demand is rising and the economy must be healthy. They are "
            "reading the identical fact. Notice that **both are "
            "fundamentalists**, which settles whether subjectivity is a "
            "technical problem. It is not. It is an analysis problem. The "
            "expensive habit that follows is quietly ignoring whatever "
            "disagrees with the view you already hold."
        )),
        Define(
            term="Selective perception",
            text="Selective perception is the tendency to heed only those "
                 "signals that support a preconceived view of the market, "
                 "discarding those that conflict with it.",
        ),
        Fig(
            panels=(Panel(number="1.19"),),
            cols=1,
            height_mm=60.0,
            caption="A trader with three oscillators, two of which agree with "
                    "the view already held.",
        ),
        Para(text=(
            "Figure 1.19 draws it honestly: a head and shoulders in price, "
            "MACD bullish and crossed out with the word ignore across it, RSI "
            "and stochastics bearish and kept. Everyone does this. **The "
            "antidote is to treat a disagreeing signal as the most "
            "informative thing on the screen**, because it is the only one "
            "telling you something you did not already believe."
        )),

        Head(number="4.6", text="Even the entry point is subjective"),
        Para(text=(
            "A trendline break looks like a hard, objective fact. But you "
            "chose which two troughs to connect and another analyst chose "
            "differently, so the break happened at a different price and "
            "moment for each of you."
        )),
        Fig(
            panels=(Panel(number="1.20"),),
            cols=1,
            height_mm=58.0,
            caption="One market top with two defensible uptrend lines beneath "
                    "it, penetrated at two different prices.",
        ),
        Para(text=(
            "Figure 1.20 shows exactly that: lines A and B under the same "
            "top, each broken at a different point. Each act of "
            "identification is objective; the choice between them is not. "
            "**Individually objective, collectively subjective.** The same "
            "holds for automated trading: the moment a parameter can be "
            "adjusted, subjectivity returns. Because breakouts can be false, "
            "three families of filter exist to validate one before you act."
        )),
        Define(
            term="The price filter",
            text="A price-based filter validates a breakout by requiring a "
                 "specified absolute, relative or volatility-scaled price "
                 "excursion beyond the trigger level.",
        ),
        Define(
            term="The time filter",
            text="A time-based filter validates a breakout by requiring the "
                 "market to sustain the excursion for a specified duration or "
                 "number of closed bars.",
        ),
        Define(
            term="The algorithmic filter",
            text="An algorithmic filter validates a breakout by requiring a "
                 "defined sequence of price events, such as bar sequences, "
                 "successive peaks or troughs, or a barrier retest.",
        ),
        Fig(
            panels=(Panel(number="1.21"),),
            cols=1,
            height_mm=58.0,
            caption="A trendline penetration with a question mark on the "
                    "entry, and the three filter families that answer it.",
        ),
        Para(text=(
            "Figure 1.21 puts the question mark on the entry and the three "
            "answers beside it. A price filter is cheap but accepts some "
            "false breaks; a time filter costs you price and buys certainty; "
            "an algorithmic filter demands a whole sequence. Chapter 5 treats "
            "all three properly. **Choosing between them is itself "
            "subjective**, which is the joke this section has been building "
            "towards."
        )),

        Head(number="4.7", text="Subjectivity shrinks with practice"),
        Para(text=(
            "None of this is an argument for giving up. A novice cannot see "
            "the trendlines, the patterns or the angles at first; with enough "
            "chart hours they become obvious. Subjectivity never reaches "
            "zero, but it falls a long way. **Nothing in this section can be "
            "achieved by reading, only by looking at charts.** Draw "
            "trendlines on the same chart as a classmate and compare. The "
            "differences are not errors. They are the consequence of "
            "everything above."
        )),
    ),
)


# ==========================================================================
# Section 5 - The assumptions underneath everything
# ==========================================================================

SECTION5 = Section(
    number=5,
    title="The Assumptions Underneath Everything",
    standfirst="Three assumptions hold the subject up. This section states "
               "them, states the two theories that attack them, and settles "
               "which side the evidence is on.",
    blocks=(
        Head(number="5.1", text="Three assumptions"),
        Para(text=(
            "Technical analysis rests on three assumptions: that the market "
            "discounts everything, that market behaviour tends to repeat "
            "itself, and that the market tends to move in trends. **Remove "
            "any one and the subject stops making sense.** This section takes "
            "them in order."
        )),

        Head(number="5.2", text="Market discounting"),
        Para(text=(
            "Without the first assumption chart reading would be pointless. "
            "It says the price you can see already contains everything the "
            "market knows and expects, so you need not hunt for the reason "
            "behind a move in order to trade it."
        )),
        Define(
            term="Market discounting",
            text="Market discounting is the assumption that market action, "
                 "including price action, reflects all known information in "
                 "the markets.",
        ),
        Para(text=(
            "The assumption has limits, and they are examinable. The market "
            "can discount known information, expectations about known "
            "information, and expectations about potential events. It cannot "
            "discount unexpected events or unknown information. Insider "
            "activity counts as known information, because the insider's "
            "buying moves the price whether or not you know why."
            "\n\n"
            "What is really discounted is subtler than the news: information "
            "about actual events, expectation about actual events, "
            "information about expected events, expectation about expected "
            "events, and expectation about the possibility of unexpected "
            "events. **This is why a company can beat expectations and still "
            "fall.** The good result was already in the price; what moved was "
            "the expectation about it."
        )),
        Fig(
            panels=(
                Panel(number="1.28", label="Three releases, absorbed "
                                           "gradually."),
                Panel(number="1.29", label="The same behaviour on EURUSD."),
            ),
            cols=2,
            height_mm=54.0,
            caption="Discounting as it actually happens: not a jump, but an "
                    "adjustment with a duration.",
        ),
        Para(text=(
            "Figure 1.28 draws three data releases with dashed curves "
            "showing price adjusting gradually rather than instantly. Figure "
            "1.29 is the same behaviour on a real chart: EURUSD around the "
            "non-farm payrolls release of 2 August 2013, with the range "
            "before the data, the breakout, the traders buying the news, and "
            "the early traders selling into them."
        )),

        Head(number="5.3", text="The Efficient Market Hypothesis"),
        Para(text=(
            "The most serious academic objection to the subject is a rival "
            "theory that sounds like market discounting and is not the same "
            "thing at all. **The difference between the two is one of the "
            "chapter's review questions**, so be careful here."
        )),
        Define(
            term="The Efficient Market Hypothesis",
            text="The Efficient Market Hypothesis states that for a market to "
                 "efficiently discount and reflect all information perfectly, "
                 "all participants must act on all information in the same "
                 "rational manner instantaneously.",
        ),
        Para(text=(
            "Efficient there means two things at once: that participants "
            "react instantaneously to all market information, and that they "
            "react rationally to it. Both must hold, and failing either is "
            "enough to break the hypothesis. **Technical analysis needs "
            "neither condition.** It assumes only that the market discounts "
            "what becomes known to it, at whatever speed it manages."
        )),
        Fig(
            panels=(Panel(number="1.27"),),
            cols=1,
            height_mm=64.0,
            caption="What a perfectly efficient market would look like: "
                    "vertical adjustments, with the time taken marked as "
                    "zero.",
        ),
        Para(text=(
            "Figure 1.27 shows what perfect efficiency would look like: "
            "price jumps vertically at each release and the time taken to "
            "adjust is marked as zero. Set it beside Figure 1.28 and the "
            "difference is the whole argument. Perfect efficiency cannot "
            "happen, for three ordinary reasons. Not everyone reacts the same "
            "way, and some trade against the news. Not everyone reacts at the "
            "same time. And not everyone can access the information, which is "
            "never free. Ask a hundred people to clap the instant a bell "
            "rings and you will not get one sound."
        )),
        Define(
            term="The semi-efficient market",
            text="A semi-efficient market discounts new information at a "
                 "slower rate, adjusting gradually as participants compete "
                 "with one another for the best fills.",
        ),
        Para(text=(
            "That is the defensible middle ground and the author's position. "
            "After a jobs report, price swings back and forth for an hour as "
            "traders compete for fills, then settles. **Technical analysis "
            "stays valid until markets become perfectly efficient, which they "
            "are not.**"
        )),

        SelfCheck(text=(
            "Market discounting and the Efficient Market Hypothesis both say "
            "that price reflects information. State the difference in one "
            "sentence, and say which of the two technical analysis actually "
            "requires."
        )),

        Head(number="5.4", text="The three forms of EMH"),
        Para(text=(
            "EMH comes in three strengths, best remembered by what each one "
            "would destroy."
        )),
        Define(
            term="The weak form of EMH",
            text="The weak form of EMH suggests that all current prices have "
                 "already fully discounted all past price information and "
                 "therefore cannot impact future prices.",
        ),
        Define(
            term="The semi-strong form of EMH",
            text="The semi-strong form of EMH suggests that all information, "
                 "once public, is already reflected in price, making its use "
                 "unprofitable and pointless.",
        ),
        Define(
            term="The strong form of EMH",
            text="The strong form of EMH suggests that all information, "
                 "whether public or private, is already fully reflected in "
                 "current price, so all forms of analysis and forecasting are "
                 "pointless.",
        ),
        Para(text=(
            "The weak form kills technical analysis: no chart pattern, "
            "trendline or moving average could ever have value. The "
            "semi-strong form kills fundamental analysis too, since reading "
            "the annual report on publication day would gain you nothing. The "
            "strong form kills everything, including the insider with "
            "genuinely secret information. **That escalation is the pattern "
            "to memorise**, and the strong form is the hardest to believe, "
            "because reality disagrees with it daily."
        )),

        Head(number="5.5", text="Random walk"),
        Para(text=(
            "The second objection is older and blunter: prices move purely "
            "by chance, so nothing that happened before tells you anything."
        )),
        Define(
            term="Random walk",
            text="Random walk suggests that prices move in a purely random "
                 "manner, that past prices do not influence current price, "
                 "and that current price does not influence future price.",
        ),
        Para(text=(
            "The second half of that definition is the Markovian condition. "
            "Flip a coin every minute and plot the running total: it will "
            "look like a chart and mean nothing."
        )),
        Fig(
            panels=(Panel(number="1.30"),),
            cols=1,
            height_mm=50.0,
            caption="Random walk feeding the three forms of EMH, and the "
                    "consequences both would have if true.",
        ),
        Para(text=(
            "Figure 1.30 lays out what would follow if either theory held "
            "completely: no technical, fundamental or behavioural analysis, "
            "no active investing, and nobody beating the market. Notice that "
            "**random walk and EMH are not the same claim**. Under EMH prices "
            "do adjust, just instantly. Under random walk prices do not "
            "adjust to anything, because the motion is not a response to "
            "anything. Markets are driven by perception and expectation, not "
            "by random acts of buying and selling, and you can watch how "
            "precisely price reacts at a round number or an old high. Chance "
            "does not aim."
        )),

        Head(number="5.6", text="What actually happens"),
        Para(text=(
            "The real sequence around a piece of news is neither instant nor "
            "random. Insiders accumulate before the announcement, so price "
            "starts moving early. The public joins after publication. More "
            "participants pile into the now obvious move and the market "
            "overreacts. The insiders sell into that enthusiasm and a top "
            "forms. **This is herding, and it is the survival instinct from "
            "Section 1 doing its work.**"
        )),
        Fig(
            panels=(
                Panel(number="1.31", label="Accumulation and distribution "
                                           "ahead of the news."),
                Panel(number="1.32", label="Inertia, overreaction, and the "
                                           "correction."),
            ),
            cols=2,
            height_mm=54.0,
            caption="Two departures from efficiency, both visible on ordinary "
                    "charts.",
        ),
        Para(text=(
            "Figure 1.31 shows accumulation curving up ahead of each bullish "
            "release and distribution curving down ahead of the bearish one, "
            "in every case before the announcement. Figure 1.32 shows the "
            "other half: herd behaviour carrying price past the level it "
            "should have settled at, then inefficient discounting pulling it "
            "back."
            "\n\n"
            "One consequence deserves its own sentence. A stock valued at 10 "
            "pesos can trade at 30 with no change at all in its fundamentals. "
            "**Price is not value.** What is traded is expectation, and "
            "current price is the result of expectations about future price "
            "and value. Market action is the collective expectation of all "
            "its participants."
        )),

        Head(number="5.7", text="Assumption two: behaviour repeats"),
        Para(text=(
            "The second assumption is that past price and chart patterns "
            "give a reasonable basis for forecasting. The reason is human "
            "psychology, which changes very slowly. Fear, greed, hope, anger "
            "and regret do not get software updates. **Patterns repeat "
            "because people repeat.** Nor is this peculiar to technical "
            "analysis: accounting, regression and behavioural finance all "
            "forecast from past data."
        )),
        Fig(
            panels=(
                Panel(number="1.25", label="Angular symmetries and the "
                                           "corrections that followed."),
                Panel(number="1.26", label="The same chart with its "
                                           "underlying structure drawn in."),
            ),
            cols=2,
            height_mm=52.0,
            caption="Repetition you can see on a four-hourly USDCAD chart.",
        ),
        Para(text=(
            "Figure 1.25 marks a shallow angle of ascent and a steeper one "
            "on a four-hourly USDCAD bar chart, with the correction that "
            "followed each. Figure 1.26 overlays the same chart with a "
            "converging channel and a lattice of symmetry lines, offered as "
            "visual evidence of the semi-random nature of price behaviour."
            "\n\n"
            "Three things erode repeatability. Preempting, where traders "
            "outbid each other ahead of the trigger, which is stage four of "
            "the cycle in 3.4. Program trading, where machines trade in ways "
            "humans cannot replicate. And new participants, since each cohort "
            "brings a slightly different approach. **The assumption is "
            "reasonable, not guaranteed**, which is why Pring said "
            "probabilities."
        )),

        Head(number="5.8", text="Assumption three: markets move in trends"),
        Para(text=(
            "The third assumption is the commercial one. Trends give the "
            "largest profit for the shortest time in the market, which is why "
            "trend based methods dominate the field. The most widely accepted "
            "definition of a trend is successively higher or successively "
            "lower peaks and troughs, and even that is not the end of it, "
            "because a trend on one timeframe is a sideways market on "
            "another. Chapter 5 settles the definitions."
            "\n\n"
            "Trend following is not free. It performs poorly in ranging "
            "markets and whipsaws during consolidation. Winning percentages "
            "are low, which means large drawdowns. Trend changes are hard to "
            "identify early, and fast markets produce slippage. And when too "
            "many trend systems chase one move, everyone's fills are worse. "
            "**Every method in this course has a cost. Know the cost before "
            "you use the method.**"
        )),

        Head(number="5.9", text="Four assumptions you apply at the chart"),
        Para(text=(
            "Those three assumptions are about the market. Four more are "
            "about what you do in front of a chart, and they govern practice "
            "rather than belief."
        )),
        Define(
            term="Applied assumption one: persistence",
            text="Price behaviour is expected to persist until there is "
                 "evidence to the contrary. Persistence is the assumed status "
                 "quo.",
        ),
        Define(
            term="Applied assumption two: equal and opposite",
            text="For every bullish indication or interpretation there exists "
                 "an equal and opposite bearish indication or interpretation "
                 "for the same price behaviour.",
        ),
        Define(
            term="Applied assumption three: extremes invert",
            text="Extreme bullishness is potentially bearish, and extreme "
                 "bearishness is potentially bullish, because extremes "
                 "indicate overextension or exhaustion.",
        ),
        Define(
            term="Applied assumption four: significance is attributed",
            text="A technical tool or indicator has no real significance "
                 "except that attributed to it by market participants.",
        ),
        Para(text=(
            "The first is the grand premise most of the others derive from, "
            "and its practical form is: do not fight the market until it "
            "gives you a reason. The second is the formal statement of "
            "everything in Section 4, and it is why you always need a plan "
            "for being wrong. The third turns on explicitly and implicitly: a "
            "stochastic reading of 100 percent is explicitly bullish and "
            "implicitly bearish at the same moment, though this does not "
            "always hold for cumulative indicators. The fourth is the "
            "self-fulfilling prophecy in formal dress, with an uncomfortable "
            "corollary: **even a badly designed indicator becomes reliable if "
            "enough capital follows it.**"
        )),

        Head(number="5.10", text="Where technical analysis works best"),
        Para(text=(
            "Over long timeframes fundamental analysis carries much of the "
            "forecasting load. Over very short ones it is nearly useless. And "
            "the smaller your stop loss, the more the forecast depends on "
            "technical work, because the position has no room to survive "
            "being early. **That is why technical analysis is generally more "
            "reliable at lower timeframes.**"
        )),
    ),
)


# ==========================================================================
# Section 6 - Who is in the market
# ==========================================================================

SECTION6 = Section(
    number=6,
    title="Who Is In The Market",
    standfirst="Every price is two participants disagreeing. This section "
               "sorts them by capital, by motive, by time and by method, and "
               "then names the markets they trade.",
    blocks=(
        Head(number="6.1", text="Five ways to sort the cast"),
        Para(text=(
            "The cast includes average investors and traders, financial "
            "institutions, commercial and central banks, hedgers and "
            "arbitrageurs, brokers, hedge funds, mutual funds and pension "
            "funds. **Every price you see is one of them disagreeing with "
            "another.** They sort five ways, and the categories cut across "
            "each other rather than nesting."
        )),
        Define(
            term="Retail and institutional participants",
            text="Retail participants trade their own capital in "
                 "comparatively small size; institutional participants deploy "
                 "pooled or corporate capital in size sufficient to move "
                 "markets.",
        ),
        Para(text=(
            "Size is the real difference, and it changes which strategies "
            "are even possible. An institution cannot enter or exit quickly "
            "without moving price against itself, which is a genuine "
            "advantage the retail trader holds."
        )),
        Define(
            term="Speculators and investors",
            text="Speculators assume price risk in pursuit of gain from price "
                 "movement; investors commit capital for longer term return "
                 "from the asset itself.",
        ),
        Para(text=(
            "Speculator is not an insult. Speculators are paid for absorbing "
            "price risk, and the liquidity everyone else relies on is the "
            "by-product. Draw the line by holding period, not attitude."
        )),
        Define(
            term="Supply side and demand side",
            text="Supply side participants provide market access, liquidity "
                 "and services; demand side participants consume those "
                 "services in order to take positions.",
        ),
        Para(text=(
            "Brokers, exchanges, market makers and data vendors are supply "
            "side. The funds and traders who use them are demand side. **The "
            "supply side gets paid whether the demand side wins or loses.**"
        )),
        Define(
            term="Professionals and novices",
            text="Professionals participate as an occupation, with defined "
                 "process and risk control; novices participate without "
                 "established process or experience.",
        ),
        Define(
            term="Discretionary and nondiscretionary traders",
            text="Discretionary traders exercise judgement on each decision; "
                 "nondiscretionary traders execute a predefined rule set "
                 "without discretionary intervention.",
        ),
        Para(text=(
            "Novice is a stage rather than a verdict, and every professional "
            "was one. The last pair connects back to Section 4: reading the "
            "chart and deciding is discretionary, letting a coded rule fire "
            "the order is nondiscretionary, and **the nondiscretionary system "
            "was still designed by somebody making subjective choices.**"
        )),

        Head(number="6.2", text="Sorted by time, and by method"),
        Para(text=(
            "Two further sorts change what a participant is trying to do. By "
            "time in the market: scalpers are in and out within seconds or "
            "minutes; day traders close every trade within the same day; "
            "swing traders hold technical reversals lasting a few days to a "
            "week; position traders hold for a few months up to a year; and "
            "investors buy and hold."
        )),
        Fig(
            panels=(
                Panel(number="1.33", label="By time in the market."),
                Panel(number="1.34", label="By trading methodology."),
            ),
            cols=2,
            height_mm=52.0,
            caption="The same participants sorted twice, first by how long "
                    "they stay and then by what they are attempting.",
        ),
        Para(text=(
            "Figure 1.33 lays the five out from seconds at one end to buy "
            "and hold at the other. Figure 1.34 re-sorts them by method: "
            "scalpers making very rapid trades by buying the bid and selling "
            "the ask; trend traders catching trends and trailing the "
            "position; reversal traders catching key levels, often through "
            "mean reversion; scale traders averaging against price until it "
            "turns; and investors buying and holding. **The two bets from "
            "Section 3 are here wearing different clothes.** One warning "
            "about the fourth: scale trading is the highest risk method on "
            "the list, because averaging into a loss is how accounts end."
        )),

        SelfCheck(text=(
            "A pension fund and a scalper both buy the same stock this "
            "morning. Using the sorts in this section, name three categories "
            "that separate them and one that does not."
        )),

        Head(number="6.3", text="The markets, and what is built on them"),
        Para(text=(
            "There are five main underlying markets: stocks, fixed income, "
            "foreign exchange, commodities and real estate. Everything else "
            "is built on top of them."
        )),
        Define(
            term="Derivative",
            text="A derivative is an instrument that provides access to an "
                 "underlying market, deriving its value from that underlying.",
        ),
        Fig(
            panels=(Panel(number="1.35"),),
            cols=1,
            height_mm=56.0,
            caption="Five underlying markets, and five instruments derived "
                    "from them.",
        ),
        Para(text=(
            "Figure 1.35 puts the five markets beside the five main "
            "instruments: options, futures, contracts for difference, spread "
            "betting and exchange traded funds. Derivative simply means "
            "derived from, which deflates most of the fear around the word: "
            "**a derivative gives you exposure to the thing without owning "
            "the thing.**"
            "\n\n"
            "Gold makes the point concretely. Buy physical gold and you are "
            "in the main market. Buy or sell a gold futures contract, a gold "
            "options contract, shares in a gold backed exchange traded fund, "
            "or a contract for difference on gold, and you are in a "
            "derivative. One underlying, five instruments, five risk "
            "profiles, and the same chart underneath all of them, which is "
            "the point of this course."
        )),
    ),
)


# ==========================================================================
# The document
# ==========================================================================

NOTES = LectureNotes(
    code="FIN1209",
    course="Technical Analysis in Investment",
    chapter="Chapter 1",
    title="Introduction to the Art and Science of Technical Analysis",
    presenter="Benjamin C. Sotelo  |  Institute of Accounts, Business and "
              "Finance, FEU Manila",
    term="First semester",
    source_note="Chapter scope follows Lim, M. (2016), The Handbook of "
                "Technical Analysis, chapter 1. Figures are reproduced from "
                "that text and remain the publisher's copyright.",
    orientation=(
        "These notes are the record of what Chapter 1 covered, written to be "
        "read on their own. If you were in the room, they are what to revise "
        "from. If you missed the session, they are the session. They follow "
        "the lecture in the same order and split into the same six parts, so "
        "you can move between the slides and these pages without hunting."
        "\n\n"
        "Read them with the chapter's figures beside you, because half the "
        "argument in this chapter is visual. Every term is defined once, "
        "where it first appears, and listed again at the back with the "
        "subsection that defines it. The check yourself boxes are not "
        "assessed; they are there to catch the places where a reader working "
        "alone usually loses the thread."
    ),
    objectives=(
        "Understand the key concepts underlying technical analysis.",
        "Identify the different forms of chart analysis.",
        "Describe the objectives of technical analysis.",
        "Understand what subjectivity means in technical analysis.",
        "Recognise the strengths and weaknesses of technical analysis.",
        "Categorise market participants by style and time in markets.",
        "Identify the various styles and approaches in technical analysis.",
    ),
    sections=(SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6),
    summary=(
        "Technical analysis is the study of market action.",
        "It identifies what has happened, and it forecasts what might.",
        "It rests on discounting, repetition, and trends.",
        "It is subjective, and so is every other kind of analysis.",
        "It deals in probabilities, never in certainties.",
    ),
    review_questions=(
        "What are the challenges to technical analysis?",
        "How does market discounting differ from the Efficient Market "
        "Hypothesis?",
        "How may an analyst resolve conflicting signals or chart patterns?",
        "Why is identifying a trend change largely subjective?",
        "Is random walk a true reflection of the markets?",
        "Describe the three levels of discounting under the Efficient Market "
        "Hypothesis.",
    ),
    sources=(
        "Lim, M. (2016). The Handbook of Technical Analysis. Wiley. "
        "Chapter 1, and the source of every figure here.",
        "Murphy, J. (1999). Technical Analysis of the Financial Markets. New "
        "York Institute of Finance.",
        "Edwards, R. and Magee, J. (2007). Technical Analysis of Stock "
        "Trends, 9th edition. AMACOM.",
        "Pring, M. (2002). Technical Analysis Explained, 4th edition. "
        "McGraw-Hill.",
    ),
)
