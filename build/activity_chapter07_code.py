"""The guide's running script: seven steps, each adding one idea, ending in the example script.

Every stage is a whole script that runs by itself on data/KO.csv. The last stage is the committed
example script, read from disk, so the guide's last step, the file students get and what is typed
in the video cannot differ. The line blocks below are copied from that script.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    key: str
    title: str
    text: str
    code: str             # the whole script at this step ("" = the final file)
    after: str = ""


HEAD = '''# Price, bars and volume (Chapters 1 to 7) and three oscillators (Chapter 8), each a vote for BUY (+1) or SELL (-1):
#   trend  price above its 3 bar average of closes is up (Chapter 5, slides 109 and 110, "Drummond geometry", "Reading a PLdot line")
#   bar    key reversal day (Chapter 7, slides 123 and 126, "The key reversal is when a strong move suddenly turns")
#   rsi    RSI crossing 50 (Chapter 8, slide 74), macd  MACD crossing its signal line (slide 83), stoch  %K crossing %D (slide 187)
# Volume is not a vote: a signal day on above-average volume is CONFIRMED (Chapter 7, slide 128, "Figure 7.15 shows the key reversal").
# Put CSV files in the data folder, run this script, read output/signals.csv. Signals of rules, not advice.'''

READ = '''ticker <- "KO"
bars <- read.csv(paste0("data/", ticker, ".csv"))
bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))'''

BEFORE = '''before <- function(x) c(NA, head(x, -1))'''

TREND = '''pldot <- SMA(bars$Close, 3)
trend_vote <- ifelse(bars$Close > pldot, 1, -1)
trend_vote[is.na(trend_vote)] <- 0'''

BAR = '''bar_vote <- ifelse(bars$Low < before(bars$Low) & bars$Close >= before(bars$Close), 1,
                   ifelse(bars$High > before(bars$High) & bars$Close <= before(bars$Close), -1, 0))
bar_vote[is.na(bar_vote)] <- 0'''

CROSS = '''cross <- function(a, b) {        # +1 on the day a crosses above b, -1 on the day it crosses below
  a <- round(a, 6)
  b <- round(rep(b, length.out = length(a)), 6)     # rounding stops a rounding-error tie from counting as a cross
  before <- function(x) c(NA, head(x, -1))
  s <- ifelse(a > b & before(a) <= before(b), 1, ifelse(a < b & before(a) >= before(b), -1, 0))
  s[is.na(s)] <- 0
  s
}
word <- function(s) ifelse(s == 1, "BUY", ifelse(s == -1, "SELL", ""))'''

OSC = '''rsi <- RSI(bars$Close, n = 14, maType = "SMA")
macd <- MACD(bars$Close, nFast = 12, nSlow = 26, nSig = 9, percent = FALSE)
sto <- stoch(bars[, c("High", "Low", "Close")], nFastK = 14, nFastD = 3)
rsi_sig <- cross(rsi, 50)
macd_sig <- cross(macd[, "macd"], macd[, "signal"])
stoch_sig <- cross(sto[, "fastK"], sto[, "fastD"])'''

TABLE = '''votes <- cbind(trend_vote, bar_vote, rsi_sig, macd_sig, stoch_sig)
fired <- bar_vote != 0 | rsi_sig != 0 | macd_sig != 0 | stoch_sig != 0
day <- which(fired & rowSums(votes) != 0)
side <- ifelse(rowSums(votes)[day] > 0, "BUY", "SELL")
signals <- data.frame(ticker = ticker, date = bars$Date[day], side = side,
                      entry = ifelse(side == "BUY", bars$High[day], bars$Close[day]),
                      trend = word(trend_vote[day]), bar = word(bar_vote[day]), rsi = word(rsi_sig[day]),
                      macd = word(macd_sig[day]), stoch = word(stoch_sig[day]),
                      agree = rowSums(votes[day, , drop = FALSE] == ifelse(side == "BUY", 1, -1)),
                      volume = ifelse(bars$Volume[day] > mean(bars$Volume), "CONFIRMED", "NOT"))'''

CHART = '''png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 1200)
layout(matrix(1:5), heights = c(3, 1, 1, 1, 1))
par(mar = c(2, 4, 3, 1))
plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(ticker, "- price, bars, volume and oscillators"))
lines(bars$Date, pldot, col = "orange")
big <- signals$agree >= 3
points(signals$date, signals$entry, pch = ifelse(side == "BUY", 24, 25), bg = ifelse(side == "BUY", "darkgreen", "red"), cex = ifelse(big, 1.8, 0.7))
if (any(big)) text(signals$date[big], signals$entry[big], labels = which(big), pos = 3)
plot(bars$Date, bars$Volume, type = "h", xlab = "", ylab = "Volume", col = ifelse(bars$Date %in% signals$date[signals$volume == "CONFIRMED"], "gold", "gray"))
abline(h = mean(bars$Volume), lty = 2)
plot(bars$Date, rsi, type = "l", xlab = "", ylab = "RSI"); abline(h = 50, lty = 2)
matplot(bars$Date, macd, type = "l", lty = 1, xlab = "", ylab = "MACD"); abline(h = 0, lty = 2)
matplot(bars$Date, sto[, c("fastK", "fastD")], type = "l", lty = 1, xlab = "", ylab = "Stochastic")
dev.off()'''

WRITE = '''dir.create("output", showWarnings = FALSE)
write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)'''

STAGES = (
    Stage("read", "Read a price file",
          "A **variable** is a name that holds a value: `ticker <- \"KO\"` puts the text KO into the name `ticker`. "
          "`read.csv()` opens a CSV file as a table, one row per trading day. `paste0()` joins text. "
          "Google Sheets writes dates like `7/1/2026 16:00:00`: `sub()` cuts the time off and `as.Date()` makes a real "
          "date. A line starting with `#` is a note for people.",
          HEAD + '\n' + READ + '\nprint(head(bars, 3))'),
    Stage("trend", "Vote 1: the price trend",
          "R's maths comes in **packages**. TTR holds the technical indicators: install it once with "
          "`install.packages(\"TTR\")` in the Console, and `library(TTR)` loads it. `SMA()` is a simple moving average. "
          "Chapter 5 (slides 109 and 110) says price above its three bar average, the PLdot, is bullish and below it is "
          "bearish. That is the trend vote: +1 for up, -1 for down. `ifelse()` picks one of two values for every day.",
          HEAD + '\nlibrary(TTR)\n' + READ + '\n' + TREND + '\nprint(table(trend_vote))'),
    Stage("bar", "Vote 2: the price bar",
          "A bar is one day's open, high, low and close. Chapter 7 (slides 123 and 126) defines the key reversal day: "
          "a higher high than the previous bar with a close at or below the previous close is bearish, and a lower low "
          "with a close at or above the previous close is bullish. `before()` gives yesterday's value in today's row. "
          "That is the bar vote.",
          HEAD + '\nlibrary(TTR)\n' + READ + '\n' + BEFORE + '\n' + TREND + '\n' + BAR + '\nprint(bars$Date[which(bar_vote != 0)])'),
    Stage("osc", "Votes 3 to 5: the oscillators",
          "A **function** packs lines under a name. `cross(a, b)` gives +1 on the day line a crosses above line b and -1 "
          "on the day it crosses below. The RSI crossing 50 (slide 74), the MACD crossing its signal line (slide 83) and "
          "the stochastic %K crossing %D (slide 187) are the three oscillator votes.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + BEFORE + '\n' + TREND + '\n' + BAR + '\n' + OSC +
          '\nprint(colSums(abs(cbind(rsi_sig, macd_sig, stoch_sig))))'),
    Stage("table", "Count the votes, keep the signal days",
          "Add the five votes. A signal day is a day the bar or an oscillator fires and the votes do not cancel: positive is "
          "a BUY, negative a SELL, and `agree` counts the votes on the winning side. A buy's entry is the day's high "
          "(slide 201) and a sell's is the close, our choice. Volume is not a vote: above-average volume marks the day "
          "CONFIRMED (slide 128). `write.csv()` saves the table.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + BEFORE + '\n' + TREND + '\n' + BAR + '\n' + OSC + '\n' + TABLE + '\n' + WRITE),
    Stage("chart", "Draw the chart",
          "Price on top with its three bar average, then volume, then the three oscillators. A triangle marks every signal "
          "day, green up for a buy and red down for a sell, and the days with three or more votes are bigger and numbered "
          "with their row in `signals.csv`. Volume bars are gold on CONFIRMED days. `dev.off()` closes the picture file.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + BEFORE + '\n' + TREND + '\n' + BAR + '\n' + OSC + '\n' + TABLE + '\n' + WRITE + '\n' + CHART),
    Stage("files", "Do it for every file",
          "A `for` loop over `list.files()` runs everything once for each CSV in the data folder, adds each stock's signals to "
          "one table, and prints a line per stock. This is the finished script, exactly the file you were given.",
          ""),
)
