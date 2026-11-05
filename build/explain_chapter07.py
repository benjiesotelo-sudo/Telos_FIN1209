"""What each line of the example script does, in plain words, written once.

The video's narration and the manual's step-by-step explanation both come from this file, so
they say the same thing. Line numbers are those of "First Automation FIN1209 - Example Script.R".
A group is a line or a short run of lines that belong together; the video types one group, then
pauses while the narration explains it, and the manual shows the group with the same words.

STEPS: the seven steps, each with the sentence that opens it and what to see after running it.
GROUPS: (step, first line, last line, explanation).
TEMPS: the throwaway line typed at the end of a step to show its result, and removed in the next step.
"""

STEPS = {
    1: ("Read every price file",
        "Step one: read every price file in the data folder.",
        "Now run it with Code, then Source. In the Console you should see the first three rows of each file, "
        "one after the other: a date, the open, high, low and close prices, and the volume. The dates are now "
        "real dates, written year, month, day."),
    2: ("Vote 1: the price trend",
        "Step two, the first vote: is the price trending up or down?",
        "Run it. The Console shows a small table with a count for minus one, plus one and zero. Most days are one or the "
        "other, and zero appears only on the first two days, which have no three day average yet."),
    3: ("Vote 2: the price bar",
        "Step three, the second vote: what is today's bar telling us?",
        "Run it. The Console lists the dates on which a key reversal bar happened, bullish or bearish. Not every day, "
        "only a handful."),
    4: ("Votes 3 to 5: the oscillators",
        "Step four, three more votes: the oscillators.",
        "Run it. The Console shows, for each stock, how many times each oscillator crossed. The stochastic crosses most "
        "often, the M A C D least. These are just counts of crossings."),
    5: ("Count the votes and keep the signal days",
        "Step five: add up the votes, and keep the signal days in a table.",
        "Run it. The Console shows the last three rows of the signals table. Each row is a signal day, with the side, "
        "the trigger level, each vote, how many agree, and whether the volume confirmed it. It is also saved as signals dot csv."),
    6: ("Draw the chart",
        "Step six: draw the chart.",
        "Run it. Nothing prints, because the chart goes into a picture file. In the output folder there is now one "
        "picture for each stock. Here is the K O chart."),
    7: ("A summary line for each stock",
        "Step seven: print one summary line for each stock.",
        "Run it for the last time. The Console now prints one line for each stock: how many signal days, how many had "
        "three or more votes agreeing, and how many were on above-average volume. That is the whole script."),
}

GROUPS = [
    (1, 1, 6, "These six lines are comments. Anything after a hash is a note for people, and R skips it. Ours say what the "
              "script does, and which Chapter and slide each vote comes from. Always write down where a rule comes from."),
    (1, 19, 19, "This is a loop. List dot files looks in the folder called data and gives back the name of every file "
                "that ends in dot csv. For path in means: take the files one at a time, and run everything inside the "
                "curly brackets once for each file. The script will work for one stock or twenty."),
    (1, 20, 21, "Ticker is a variable, a name that holds a value. Basename strips the folder from the path, and sub removes "
                "the dot csv, so K O dot csv becomes K O. Read dot csv then opens the file as a table, one row per day, "
                "and calls it bars."),
    (1, 22, 22, "Google Sheets writes dates like seven slash one slash twenty twenty six, followed by a time. Sub cuts "
                "off everything from the first space. As dot Date turns the text into a real date, and tryFormats lists "
                "the two layouts it may find. Now R can sort and plot by date."),
    (2, 7, 7, "R does a lot, but the indicators come in a package called T T R. Library loads it. You install it only "
              "once, with install dot packages, typed in the Console."),
    (2, 24, 24, "S M A is a simple moving average. Three means the average of the last three closes. Chapter 5, slides "
                "109 and 110, call this line the PLdot. Price above it is bullish, and below it bearish."),
    (2, 25, 25, "If the close is above the average, the vote is plus one, up. Otherwise it is minus one, down. If else "
                "makes that choice for every day at once. A vote is just a number, plus one for buy, minus one for sell."),
    (2, 26, 26, "The first two days have no three day average yet, so the vote is missing. Is dot na finds the missing "
                "ones, and we set them to zero, no vote."),
    (3, 23, 23, "Before gives yesterday's value in today's row. It shifts a column down by one, and the first day gets "
                "N A, because it has no yesterday. We need it to compare today's bar with yesterday's."),
    (3, 27, 28, "The key reversal, Chapter 7, slides 123 and 126. A bullish one: today's low is lower than yesterday's, "
                "but the close is at or above yesterday's close. That is plus one. Bearish: a higher high, and a close "
                "at or below yesterday's close. That is minus one. Otherwise zero. The book says near; we say at or."),
    (3, 29, 29, "The first day again has no yesterday, so the bar vote there is missing. Set it to zero."),
    (4, 8, 15, "A function packs lines under a name so we can reuse them. Cross takes two lines of numbers, a and b. "
               "It rounds them, so a rounding error is not mistaken for a cross. Then it gives plus one on the day a "
               "goes from at or below b to above it, minus one on the day it goes from at or above to below, and zero "
               "otherwise. A crossing is the signal."),
    (4, 16, 16, "Word turns a vote into text: plus one becomes B U Y, minus one S E L L, zero nothing. We use it for the "
                "table."),
    (4, 30, 30, "The R S I, the relative strength index. The input is the close. N equals fourteen means it looks "
                "at the last fourteen days. M A type S M A means plain averages, as slide 195 says. It swings between zero "
                "and one hundred."),
    (4, 31, 31, "The M A C D is a twelve day average minus a twenty six day average, and its signal line is a nine day "
                "average of that, slides 166 to 168. N fast, n slow and n sig are those three numbers. Percent false keeps "
                "it as a plain difference."),
    (4, 32, 32, "The stochastic uses the high, low and close. Fast K, fourteen days, says where the close sits within "
                "the last fourteen days' range. Fast D, three, is a three day average of it, slide 187."),
    (4, 33, 35, "Now find the crossings. The R S I crossing its fifty line, slide 74. The M A C D crossing its signal line, "
                "slide 83. The stochastic K crossing D, slide 187. Each result is plus one, minus one, or zero."),
    (5, 17, 18, "All signals will collect every stock's signals. Dir dot create makes the output folder if it is not "
                "there. Both go before the loop, because we only want them once."),
    (5, 36, 36, "Cbind puts the five votes side by side, one column each, one row per day. Rows sums will add them up "
                "for each day."),
    (5, 37, 38, "A signal day is a day the bar or an oscillator fired, written with the vertical bar for or, and the "
                "votes do not cancel out. Which gives the row numbers of those days."),
    (5, 39, 39, "If the votes add up above zero the side is B U Y, otherwise S E L L."),
    (5, 40, 41, "Now the table. Data dot frame builds it, one row for each signal day. Ticker, date and side. The entry "
                "is a trigger level. A buy triggers above the signal day's high, as Lim says on slide 201. A sell triggers "
                "below the signal day's low. That is the mirror of Lim's buy trigger, our choice, because the slides give no "
                "sell trigger. The trade happens only if price later goes beyond the level."),
    (5, 42, 45, "Then what each vote said, written as words, and agree: how many of the five votes are on the winning "
                "side. And the volume: if the day's volume is above the average volume of the file, it is CONFIRMED, as "
                "slide 128 marks the key reversal day. Volume is not a vote. It says how much weight the day carried."),
    (5, 60, 60, "R bind adds this stock's table under all the others."),
    (5, 63, 63, "After the loop, write dot csv saves the whole table as signals dot csv in the output folder."),
    (6, 46, 48, "Png opens a picture file in the output folder, named after the stock. Layout splits it into five panels, "
                "the first three times as tall as the others. Par sets the margins."),
    (6, 49, 50, "Plot draws the closing price as a line, against the date. Lines adds the orange three day average on top "
                "of it."),
    (6, 51, 53, "Now mark the signals. Big means three or more votes agree. Points puts a triangle at each signal's "
                "trigger level, green up for a buy, red down for a sell, and bigger when three or more agree. Text numbers "
                "the big ones with their row in the table."),
    (6, 54, 55, "The second panel is the volume as bars, gold on the days confirmed by volume, with a dashed line at the "
                "average."),
    (6, 56, 58, "Then one panel for each oscillator: the R S I with its fifty line, the M A C D with its signal line, and "
                "the stochastic."),
    (6, 59, 59, "Dev dot off closes the picture file. Until then nothing is saved."),
    (7, 61, 61, "Cat prints a line in the Console. It says the stock, how many signal days, how many had three or more "
                "votes agreeing, and how many were on above-average volume. The numbers come straight from the table."),
]

TEMPS = {
    1: "print(head(bars, 3))",
    2: "print(table(trend_vote))",
    3: "print(bars$Date[which(bar_vote != 0)])",
    4: "print(colSums(abs(cbind(rsi_sig, macd_sig, stoch_sig))))",
    5: "print(tail(signals, 3))",
}
TEMP_SAY = {
    1: "To see what we have read, print the first three rows. Head gives the top of a table.",
    2: "To see the votes, print a table of them. Table counts how many days gave each value.",
    3: "To see which days had a key reversal bar, print the dates where the vote is not zero.",
    4: "To check the oscillators, add up how many crossings each one found. Col sums adds each column.",
    5: "To see the table, print its last three rows. Tail gives the end of a table.",
}


def group_for(final_line: int):
    """The group that explains a line of the final script (1-based), or None."""
    for g in GROUPS:
        if g[1] <= final_line <= g[2]:
            return g
    return None


_WRITTEN = (
    ("R S I", "RSI"), ("M A C D", "MACD"), ("T T R", "TTR"), ("B U Y", "BUY"), ("S E L L", "SELL"),
    ("K O dot csv", "`KO.csv`"), ("K O", "KO"), ("N A", "NA"), ("S M A", "SMA"), ("signals dot csv", "`signals.csv`"),
    ("dot csv", "`.csv`"), ("List dot files", "`list.files()`"), ("Read dot csv", "`read.csv()`"),
    ("As dot Date", "`as.Date()`"), ("Dir dot create", "`dir.create()`"), ("install dot packages", "`install.packages()`"),
    ("Data dot frame", "`data.frame()`"), ("Write dot csv", "`write.csv()`"), ("Dev dot off", "`dev.off()`"),
    ("Is dot na", "`is.na()`"), ("seven slash one slash twenty twenty six", "7/1/2026"), ("N equals fourteen", "`n = 14`"),
    ("percent false", "`percent = FALSE`"), ("tryFormats", "`tryFormats`"),
)


def written(text: str) -> str:
    """The spoken explanation as it is written in the manual (letters joined, code in code font)."""
    for a, b in _WRITTEN:
        text = text.replace(a, b)
    return text


# Said while the throwaway check line is removed at the start of the next step.
DELETE_SAY = ("That print line was only there to let us look. We select it and delete it, "
              "so the finished script stays short.")


# The short version: the same seven steps, each block explained as a block (what it does, what it produces).
SHORT = {
    1: "Step one is the read block. It lists every csv file in the data folder and, for each one, works out the ticker "
       "from the file name, reads the file into a table called bars, and turns the Google Sheets dates into real dates. "
       "It produces a table of days with the open, high, low, close and volume.",
    2: "Step two is the price trend block. It loads the T T R package, takes the three day moving average of the close, "
       "and votes plus one when the close is above it and minus one when it is below. It produces the first vote for every "
       "day, with zero on the first two days that have no average yet.",
    3: "Step three is the price bar block. It looks at yesterday's bar and votes for a key reversal: a lower low that "
       "closes at or above yesterday's close is a buy, a higher high that closes at or below it is a sell. It produces "
       "the second vote, zero on every ordinary day.",
    4: "Step four is the oscillator block. A small function finds the day one line crosses another. The R S I is tested "
       "against fifty, the M A C D against its signal line, and the stochastic percent K against percent D. It produces "
       "three more votes, one for each oscillator.",
    5: "Step five is the table block. It puts the five votes side by side, keeps the days where the bar or an oscillator "
       "fired and the votes do not cancel, and decides buy or sell by the net vote. It sets the trigger level, a buy above the high and a sell below the low, counts how "
       "many votes agree, checks the volume, and saves everything as signals dot csv.",
    6: "Step six is the chart block. For each stock it draws one picture with five panels: price and its average with a "
       "triangle on every signal, then volume, then the R S I, the M A C D and the stochastic. It produces one picture "
       "file for each stock in the output folder.",
    7: "Step seven is the summary line. For each stock it prints the number of signal days, how many had three or more "
       "votes agreeing, and how many were on above average volume. That completes the script.",
}
