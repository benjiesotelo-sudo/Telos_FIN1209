"""The guide's running script: seven steps, each adding one idea, ending in the example script.

Every stage is a whole script that runs by itself on data/KO.csv. The last stage is the committed
example script, read from disk, so the guide's last step, the file students get and what is typed
in the video cannot differ.
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


HEAD = '''# Three Chapter 8 window oscillators, each with the buy and sell rule from the slides:
# RSI crossing 50 (slide 74), MACD crossing its signal line (slide 83), stochastic %K crossing %D (slide 187).
# Put CSV files in the data folder, run this script, read output/signals.csv. Signals of rules, not advice.'''

READ = '''ticker <- "KO"
bars <- read.csv(paste0("data/", ticker, ".csv"))
bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))'''

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

VOTES = '''votes <- rsi_sig + macd_sig + stoch_sig
day <- which(votes != 0)
side <- ifelse(votes[day] > 0, "BUY", "SELL")'''

TABLE = '''signals <- data.frame(ticker = ticker, date = bars$Date[day], side = side,
                      entry = ifelse(side == "BUY", bars$High[day], bars$Close[day]),
                      rsi = word(rsi_sig[day]), macd = word(macd_sig[day]), stoch = word(stoch_sig[day]),
                      agree = rowSums(cbind(rsi_sig, macd_sig, stoch_sig)[day, , drop = FALSE] == ifelse(side == "BUY", 1, -1)))
dir.create("output", showWarnings = FALSE)
write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)'''

CHART = '''png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 1000)
layout(matrix(1:4), heights = c(3, 1, 1, 1))
par(mar = c(2, 4, 3, 1))
plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(ticker, "- window oscillator signals"))
big <- signals$agree >= 2
points(signals$date, signals$entry, pch = ifelse(side == "BUY", 24, 25), bg = ifelse(side == "BUY", "darkgreen", "red"), cex = ifelse(big, 1.8, 0.7))
if (any(big)) text(signals$date[big], signals$entry[big], labels = which(big), pos = 3)
plot(bars$Date, rsi, type = "l", xlab = "", ylab = "RSI"); abline(h = 50, lty = 2)
matplot(bars$Date, macd, type = "l", lty = 1, xlab = "", ylab = "MACD"); abline(h = 0, lty = 2)
matplot(bars$Date, sto[, c("fastK", "fastD")], type = "l", lty = 1, xlab = "", ylab = "Stochastic")
dev.off()'''

STAGES = (
    Stage("read", "Read a price file",
          "A **variable** is a name that holds a value: `ticker <- \"KO\"` puts the text KO into the name `ticker`. "
          "`read.csv()` opens a CSV file as a table, one row per trading day. `paste0()` joins text. "
          "Google Sheets writes dates like `7/1/2026 16:00:00`: `sub()` cuts the time off and `as.Date()` makes a real "
          "date. A line starting with `#` is a note for people.",
          HEAD + '\n' + READ + '\nprint(head(bars, 3))'),
    Stage("rsi", "Use a package: the RSI",
          "R's maths comes in **packages**. TTR holds the technical indicators. Install it once, with "
          "`install.packages(\"TTR\")` typed in the Console, then `library(TTR)` loads it. `RSI()` returns the "
          "relative strength index, 14 days, with the plain averages the slides use (slide 195). "
          "`tail()` shows the last rows. The RSI swings between 0 and 100 around its equilibrium, 50 (slide 74).",
          HEAD + '\nlibrary(TTR)\n' + READ + '\nrsi <- RSI(bars$Close, n = 14, maType = "SMA")\nprint(tail(rsi, 3))'),
    Stage("cross", "A crossing is a signal",
          "A **function** packs lines under a name. `cross(a, b)` gives +1 on the day line a crosses above line b and "
          "-1 on the day it crosses below: the RSI crossing 50 is a buy or sell signal on slide 74. `which()` finds "
          "the days that are not zero.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\nrsi <- RSI(bars$Close, n = 14, maType = "SMA")\n'
          'rsi_sig <- cross(rsi, 50)\nprint(bars$Date[which(rsi_sig != 0)])'),
    Stage("three", "Two more oscillators, and a vote",
          "The same `cross()` reads the other two rules. The MACD is a 12 day average minus a 26 day average, with a "
          "9 day signal line (slides 166, 168), and its crossing of the signal line is a signal (slide 83). The "
          "stochastic %K crossing %D is a signal on slide 187. Adding the three signals gives a vote: positive is a "
          "buy, negative a sell, and the size says how many agree.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + OSC + '\n' + VOTES + '\nprint(table(side))'),
    Stage("table", "Keep the signals in a table",
          "Each signal day becomes a row: the date, buy or sell, the entry price, what each oscillator said, and how "
          "many agree. The entry is the day's high for a buy (slide 201) and the close for a sell, because the "
          "slides give no sell trigger. `write.csv()` saves the table in an output folder.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + OSC + '\n' + VOTES + '\n' + TABLE),
    Stage("chart", "Draw the chart",
          "Price on top, the three oscillators in panels below. `points()` marks each signal day with a triangle, "
          "green up for a buy and red down for a sell, and the days where two or more oscillators agree are bigger "
          "and numbered with their row in `signals.csv`. `dev.off()` closes the picture file.",
          HEAD + '\nlibrary(TTR)\n' + CROSS + '\n' + READ + '\n' + OSC + '\n' + VOTES + '\n' + TABLE + '\n' + CHART),
    Stage("files", "Do it for every file",
          "A `for` loop over `list.files()` runs everything once for each CSV in the data folder, adds each stock's "
          "signals to one table, and prints how many signal days it found. This is the finished script, exactly the "
          "file you were given.",
          ""),
)
