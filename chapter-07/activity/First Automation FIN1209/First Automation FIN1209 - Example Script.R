# Three Chapter 8 window oscillators, each with the buy and sell rule from the slides:
# RSI crossing 50 (slide 74), MACD crossing its signal line (slide 83), stochastic %K crossing %D (slide 187).
# Put CSV files in the data folder, run this script, read output/signals.csv. Signals of rules, not advice.
library(TTR)
cross <- function(a, b) {        # +1 on the day a crosses above b, -1 on the day it crosses below
  a <- round(a, 6)
  b <- round(rep(b, length.out = length(a)), 6)     # rounding stops a rounding-error tie from counting as a cross
  before <- function(x) c(NA, head(x, -1))
  s <- ifelse(a > b & before(a) <= before(b), 1, ifelse(a < b & before(a) >= before(b), -1, 0))
  s[is.na(s)] <- 0
  s
}
word <- function(s) ifelse(s == 1, "BUY", ifelse(s == -1, "SELL", ""))
all_signals <- NULL
dir.create("output", showWarnings = FALSE)
for (path in list.files("data", pattern = "\\.csv$", full.names = TRUE)) {
  ticker <- sub("\\.csv$", "", basename(path))
  bars <- read.csv(path)
  bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
  rsi <- RSI(bars$Close, n = 14, maType = "SMA")
  macd <- MACD(bars$Close, nFast = 12, nSlow = 26, nSig = 9, percent = FALSE)
  sto <- stoch(bars[, c("High", "Low", "Close")], nFastK = 14, nFastD = 3)
  rsi_sig <- cross(rsi, 50)
  macd_sig <- cross(macd[, "macd"], macd[, "signal"])
  stoch_sig <- cross(sto[, "fastK"], sto[, "fastD"])
  votes <- rsi_sig + macd_sig + stoch_sig
  day <- which(votes != 0)
  side <- ifelse(votes[day] > 0, "BUY", "SELL")
  signals <- data.frame(ticker = ticker, date = bars$Date[day], side = side,
                        entry = ifelse(side == "BUY", bars$High[day], bars$Close[day]),
                        rsi = word(rsi_sig[day]), macd = word(macd_sig[day]), stoch = word(stoch_sig[day]),
                        agree = rowSums(cbind(rsi_sig, macd_sig, stoch_sig)[day, , drop = FALSE] == ifelse(side == "BUY", 1, -1)))
  png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 1000)
  layout(matrix(1:4), heights = c(3, 1, 1, 1))
  par(mar = c(2, 4, 3, 1))
  plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(ticker, "- window oscillator signals"))
  big <- signals$agree >= 2
  points(signals$date, signals$entry, pch = ifelse(side == "BUY", 24, 25), bg = ifelse(side == "BUY", "darkgreen", "red"), cex = ifelse(big, 1.8, 0.7))
  if (any(big)) text(signals$date[big], signals$entry[big], labels = which(big), pos = 3)
  plot(bars$Date, rsi, type = "l", xlab = "", ylab = "RSI"); abline(h = 50, lty = 2)
  matplot(bars$Date, macd, type = "l", lty = 1, xlab = "", ylab = "MACD"); abline(h = 0, lty = 2)
  matplot(bars$Date, sto[, c("fastK", "fastD")], type = "l", lty = 1, xlab = "", ylab = "Stochastic")
  dev.off()
  all_signals <- rbind(all_signals, signals)
  cat(ticker, ":", nrow(signals), "signal days,", sum(signals$agree >= 2), "with two or more oscillators agreeing\n")
}
write.csv(all_signals, "output/signals.csv", row.names = FALSE, quote = FALSE)
