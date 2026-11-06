"""The example script, block by block, in plain words.

The handout and the video both walk the script this way: a labelled block, then each important line shown whole and
highlighted, then the key part of the line boxed, each with one plain sentence. Line numbers are found in the committed
script by its text, so this file never holds a number that can drift. No pipe operators are used anywhere in the script.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT_FILE = REPO / "chapter-07" / "activity" / "First Automation FIN1209" / "First Automation FIN1209 - Example Script.R"

# (block header text in the script, plain title, what the block is for, rows)
# row: (the line starts with, key part, what the line does, what the key part is)
BLOCKS = (
    ("1 SETTINGS", "Settings", "The only lines you edit. Change a value, run the script, read the answer.", (
        ('mode <-', '"buy"',
         'Your question. "buy" asks: should I buy today? "sell" asks: I already own it, should I sell?',
         'The word in quotes is the setting. Type buy or sell exactly, in small letters.'),
        ('stock <-', '"KO"', 'Which price file to read. This one reads data/KO.csv.',
         'Your stock\'s name. It must match the file name in the data folder.'),
        ('bought_price <-', '87.29', 'Sell mode only: the price you paid for each share.',
         'A plain number, with no quotes.'),
        ('bought_date <-', '"2026-08-12"', 'Sell mode only: the day you bought it.',
         'Year, month, day, in quotes. It must be a trading day in your file.'),
    )),
    ("2 READ THE DATA", "Read the data", "Loads the indicator package and your stock's prices.", (
        ('library(TTR)', 'TTR', 'Loads the package that works out the moving average, the RSI, the MACD and the stochastic.',
         'TTR is the only package we use. Install it once, in the Console, with install.packages("TTR").'),
        ('bars <- read.csv', 'paste0(stock, ".csv")',
         'Reads your stock\'s file into a table called bars, one row for each trading day.',
         'paste0 glues pieces of text together: the stock KO and .csv make KO.csv.'),
        ('bars$Date <-', 'sub(" .*", "", bars$Date)',
         'Turns the Google Sheets dates into real dates, so R can sort and plot them.',
         'Sheets writes a time after the date. This cuts off everything from the first space.'),
        ('n <- nrow(bars)', 'nrow(bars)',
         'n is the number of rows. Row n, the last row, is the latest trading day in the file: "today".',
         'Today is the last day in your download, not a live price. Sheets prices can be about 20 minutes late.'),
    )),
    ("3 THE FIVE VOTES", "The five votes", "Each vote is +1 for BUY, -1 for SELL or 0 for nothing.", (
        ('before <- function', 'c(NA, head(x, -1))', 'A small helper: yesterday\'s value, placed in today\'s row.',
         'Head with minus one is the list without its last value. The NA in front moves everything down one day.'),
        ('cross <- function', 'function(a, b)',
         'A helper that spots a crossing: +1 the day line a crosses above line b, -1 the day it crosses below, 0 otherwise.',
         'A function packs lines under a name, so we write them once and use them three times.'),
        ('s <- ifelse(a > b', 'a > b & before(a) <= before(b)',
         'Above b today but not above b yesterday: that is a crossing up.',
         'ifelse picks a value for every day at once: the first value when the test is true, the second when it is false. The ampersand means and.'),
        ('pldot <- SMA', 'SMA(bars$Close, 3)',
         'The three day average of the closes: the PLdot line of Chapter 5 (slides 109, 110).',
         'SMA is a simple moving average: the average of the last 3 closes.'),
        ('trend_vote <- ifelse', 'bars$Close > pldot',
         'Vote 1, the price trend: +1 when the close is above its average, -1 when it is below.',
         'Greater than: it asks whether the close is bigger than its average.'),
        ('bar_vote <- ifelse', 'bars$Low < before(bars$Low) & bars$Close >= before(bars$Close)',
         'Vote 2, the price bar, a key reversal (Chapter 7, slides 123, 126): a lower low that closes at or above yesterday\'s close votes BUY; a higher high that closes at or below it votes SELL.',
         'The ampersand joins two conditions: both must be true on the same day.'),
        ('rsi <- RSI', 'n = 14', 'The RSI over 14 days (Chapter 8, slides 193 to 195).',
         'n = 14 is how many days it looks back.'),
        ('macd <- MACD', 'nFast = 12, nSlow = 26, nSig = 9',
         'The MACD: two averages (12 and 26 days) and a 9 day signal line (slides 166 to 168).',
         'These numbers are the settings the slides use.'),
        ('sto <- stoch', 'nFastK = 14, nFastD = 3',
         'The stochastic: %K over 14 days and %D, its 3 day average (slides 185, 187).',
         'It needs the High, Low and Close columns, so we hand it those three.'),
        ('rsi_sig <- cross', 'cross(rsi, 50)',
         'Votes 3 to 5: +1 when the RSI crosses above 50 and -1 below (slide 74). The next two lines do the same for the MACD and its signal line (slide 83) and for %K and %D (slide 187).',
         'The three lines use the same cross helper from above.'),
        ('votes <- cbind', 'cbind(trend_vote',
         'Puts the five votes side by side: one column each, one row for each day.',
         'cbind binds columns together.'),
    )),
    ("4 DECIDE", "Decide: signal days, then buy or sell", "Counts the votes, finds the signal days, then your setting decides what to answer.", (
        ('buys <- rowSums', 'rowSums(votes == 1)', 'For each day, counts how many of the five votes say BUY. The next line counts SELL.',
         'Where a vote says BUY the test is true. rowSums adds up the true values across the five votes.'),
        ('day <- which', 'buys >= 3 | sells >= 3',
         'A signal day is a day when at least 3 of the 5 votes agree. which() gives the row numbers of those days.',
         'The vertical bar means or: 3 or more BUY, or 3 or more SELL.'),
        ('signals <- data.frame', 'data.frame', 'Builds the table of signal days, one row for each signal.',
         'data.frame makes a table from columns of equal length.'),
        ('entry = ifelse', 'bars$High[day], bars$Low[day]',
         'The trigger level. A buy triggers above the signal day\'s high (slide 201). A sell triggers below its low: the mirror, our choice. The trade happens only if price later goes beyond the level.',
         'Square brackets pick rows: this is the High column, on the signal days only.'),
        ('if (mode == "buy")', 'mode == "buy"', 'Now your setting decides. Everything in the first brackets is buy mode.',
         'The double equals sign asks: is it equal to?'),
        ('if (n %in% day[side == "BUY"])', 'n %in% day', 'Is today, row n, one of the buy signal days?',
         '%in% asks whether a value is in a list.'),
        ('answer <- paste0("BUY: enter if', 'bars$High[n]', 'BUY: enter if price trades above today\'s high, with the stop at today\'s low.',
         'Square brackets pick row n, today.'),
        ('answer <- paste0("WAIT', 'buys[n]', 'WAIT: no buy signal today. It says how many votes say BUY today and that 3 are needed.',
         'Square brackets again: the count for today.'),
        ('i <- max(which(bars$Date <= as.Date(bought_date)))', 'bars$Date <= as.Date(bought_date)',
         'Sell mode starts here: finds the row of the day you bought.',
         'Max of which takes the last row that is on or before your date.'),
        ('stop_at <- bars$Low[i]', 'bars$Low[i]',
         'The stop: the low of the day you bought. Our choice. Chapter 5, slide 74 says a stop sits just below a significant trough but gives no rule.',
         'i is the row of your buy day.'),
        ('sell_day <- day[side == "SELL" & day > i]', 'day > i', 'The sell signal days after the day you bought.',
         'Only days after your buy day count.'),
        ('below <- later[', 'bars$Close[later] < stop_at', 'The days after you bought that closed below your stop.',
         'Less than: it asks whether the close is smaller than your stop.'),
        ('pct <- sprintf', 'sprintf("%+.1f%%"', 'Your gain or loss so far, in percent, with a plus or minus sign.',
         'sprintf turns a number into text in the layout you choose.'),
        ('if (length(sell_day) > 0 || length(below) > 0)', '||',
         'SELL now if there was a sell signal or a close below the stop. Otherwise the answer is HOLD.',
         'The double bar means or.'),
    )),
    ("5 DRAW THE CHART", "Draw the chart", "One picture: price, volume and the three oscillators, with today's answer marked.", (
        ('png(file.path', 'width = 1200, height = 1200', 'Opens a picture file in the output folder, named after your stock.',
         'The size of the picture in pixels.'),
        ('plot(bars$Date, bars$Close', 'type = "l"', 'Draws the closing price against the date. The title carries today\'s answer.',
         'type = "l" means a line.'),
        ('points(signals$date', 'pch = ifelse(side == "BUY", 24, 25)',
         'A triangle on every signal day: green pointing up for a buy, red pointing down for a sell.',
         'pch is the shape of the mark: 24 points up, 25 points down.'),
        ('abline(v = bars$Date[n]', 'abline(v = bars$Date[n]', 'Today\'s answer on the chart: a dashed line at the latest day, labelled BUY, WAIT, SELL or HOLD.',
         'abline draws a straight line. v is for vertical.'),
        ('if (mode == "sell")', 'points(bars$Date[i], bought_price', 'In sell mode only: a cross where you bought and a dotted red line at your stop.',
         'The cross is drawn at your buy date and the price you paid.'),
        ('plot(bars$Date, bars$Volume', 'type = "h"', 'The panels below: volume (gold on confirmed days), then the RSI, the MACD and the stochastic.',
         'type = "h" draws a thin bar for each day.'),
        ('invisible(dev.off())', 'dev.off()', 'Closes the picture file. Until then nothing is saved.',
         'dev.off() turns the drawing off.'),
    )),
    ("6 WRITE THE ANSWER", "Write the answer", "Saves the signal days and today's answer, and prints the answer.", (
        ('write.csv(signals', 'row.names = FALSE', 'Saves the table of signal days as output/signals.csv.',
         'row.names = FALSE leaves out the row numbers.'),
        ('writeLines(answer', '"output/answer.txt"', 'Saves today\'s answer as output/answer.txt, a fixed file anyone can open.',
         'writeLines writes each piece of text on its own line.'),
        ('cat(answer', 'cat(answer', 'Prints the answer in the Console, one line each.',
         'cat prints text as it is.'),
    )),
)


def script_lines() -> list:
    return SCRIPT_FILE.read_text(encoding="utf-8").splitlines()


def blocks():
    """[(number, title, purpose, first line, last line, [(line no, text, key, line says, key says)])] from the script."""
    lines = script_lines()
    heads = [i for i, ln in enumerate(lines) if ln.startswith("# ========")]
    out = []
    for k, (hdr, title, purpose, rows) in enumerate(BLOCKS, 1):
        a = next(i for i in heads if hdr in lines[i])
        nxt = [i for i in heads if i > a]
        b = (nxt[0] if nxt else len(lines)) - 1
        got, at = [], a
        for start, key, says, keys in rows:
            i = next((j for j in range(at, b + 1) if lines[j].strip().startswith(start)), None)
            if i is None:
                raise SystemExit(f"walkthrough: no line starting {start!r} in block {hdr}")
            if key not in lines[i]:
                raise SystemExit(f"walkthrough: key part {key!r} is not in line {i + 1}")
            got.append((i + 1, lines[i], key, says, keys))
            at = i
        out.append((k, title, purpose, a + 1, b + 1, got))
    return out
