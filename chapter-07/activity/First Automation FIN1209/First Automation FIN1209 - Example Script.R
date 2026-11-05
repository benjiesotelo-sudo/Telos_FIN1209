# Price, bars and volume (Chapters 1 to 7) and three oscillators (Chapter 8), each a vote for BUY (+1) or SELL (-1):
#   trend  price above its 3 bar average of closes is up (Chapter 5, slides 109 and 110, "Drummond geometry", "Reading a PLdot line")
#   bar    key reversal day (Chapter 7, slides 123 and 126, "The key reversal is when a strong move suddenly turns")
#   rsi    RSI crossing 50 (Chapter 8, slide 74), macd  MACD crossing its signal line (slide 83), stoch  %K crossing %D (slide 187)
# Volume is not a vote: a signal day on above-average volume is CONFIRMED (Chapter 7, slide 128, "Figure 7.15 shows the key reversal").
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
  before <- function(x) c(NA, head(x, -1))
  pldot <- SMA(bars$Close, 3)
  trend_vote <- ifelse(bars$Close > pldot, 1, -1)
  trend_vote[is.na(trend_vote)] <- 0
  bar_vote <- ifelse(bars$Low < before(bars$Low) & bars$Close >= before(bars$Close), 1,
                     ifelse(bars$High > before(bars$High) & bars$Close <= before(bars$Close), -1, 0))
  bar_vote[is.na(bar_vote)] <- 0
  rsi <- RSI(bars$Close, n = 14, maType = "SMA")
  macd <- MACD(bars$Close, nFast = 12, nSlow = 26, nSig = 9, percent = FALSE)
  sto <- stoch(bars[, c("High", "Low", "Close")], nFastK = 14, nFastD = 3)
  rsi_sig <- cross(rsi, 50)
  macd_sig <- cross(macd[, "macd"], macd[, "signal"])
  stoch_sig <- cross(sto[, "fastK"], sto[, "fastD"])
  votes <- cbind(trend_vote, bar_vote, rsi_sig, macd_sig, stoch_sig)
  fired <- bar_vote != 0 | rsi_sig != 0 | macd_sig != 0 | stoch_sig != 0
  day <- which(fired & rowSums(votes) != 0)
  side <- ifelse(rowSums(votes)[day] > 0, "BUY", "SELL")
  signals <- data.frame(ticker = ticker, date = bars$Date[day], side = side,
                        entry = ifelse(side == "BUY", bars$High[day], bars$Close[day]),
                        trend = word(trend_vote[day]), bar = word(bar_vote[day]), rsi = word(rsi_sig[day]),
                        macd = word(macd_sig[day]), stoch = word(stoch_sig[day]),
                        agree = rowSums(votes[day, , drop = FALSE] == ifelse(side == "BUY", 1, -1)),
                        volume = ifelse(bars$Volume[day] > mean(bars$Volume), "CONFIRMED", "NOT"))
  png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 1200)
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
  dev.off()
  all_signals <- rbind(all_signals, signals)
  cat(ticker, ":", nrow(signals), "signal days,", sum(signals$agree >= 3), "with three or more votes agreeing,", sum(signals$volume == "CONFIRMED"), "on above-average volume\n")
}
write.csv(all_signals, "output/signals.csv", row.names = FALSE, quote = FALSE)
