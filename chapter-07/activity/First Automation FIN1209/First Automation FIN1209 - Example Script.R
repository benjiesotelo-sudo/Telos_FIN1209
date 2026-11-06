# FIN1209 First Automation. Plain R plus the TTR package. Signals of rules, not advice. Not foolproof.
# ======== 1 SETTINGS: the only lines you edit ========
mode <- "buy"                  # "buy" or "sell"
stock <- "KO"                  # which file in the data folder: data/KO.csv
bought_price <- 87.29          # sell mode only: the price you paid
bought_date <- "2026-08-12"    # sell mode only: the day you bought it
# ======== 2 READ THE DATA ========
library(TTR)
bars <- read.csv(file.path("data", paste0(stock, ".csv")))
bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
n <- nrow(bars)                # the last row is the latest trading day in the file: "today"
# ======== 3 THE FIVE VOTES: +1 for BUY, -1 for SELL, 0 for nothing ========
before <- function(x) c(NA, head(x, -1))      # yesterday's value, in today's row
cross <- function(a, b) {      # +1 on the day a crosses above b, -1 on the day it crosses below
  a <- round(a, 6)
  b <- round(rep(b, length.out = length(a)), 6)
  s <- ifelse(a > b & before(a) <= before(b), 1, ifelse(a < b & before(a) >= before(b), -1, 0))
  s[is.na(s)] <- 0
  s
}
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
# ======== 4 DECIDE: a signal day is a day when at least 3 of the 5 votes agree ========
buys <- rowSums(votes == 1)
sells <- rowSums(votes == -1)
day <- which(buys >= 3 | sells >= 3)
side <- ifelse(buys[day] >= 3, "BUY", "SELL")
word <- function(s) ifelse(s == 1, "BUY", ifelse(s == -1, "SELL", ""))
signals <- data.frame(ticker = rep(stock, length(day)), date = bars$Date[day], side = side,
                      entry = ifelse(side == "BUY", bars$High[day], bars$Low[day]),
                      stop = ifelse(side == "BUY", bars$Low[day], bars$High[day]),
                      trend = word(trend_vote[day]), bar = word(bar_vote[day]), rsi = word(rsi_sig[day]),
                      macd = word(macd_sig[day]), stoch = word(stoch_sig[day]), agree = pmax(buys, sells)[day],
                      volume = ifelse(bars$Volume[day] > mean(bars$Volume), "CONFIRMED", "NOT"))
if (mode == "buy") {           # BUY: the latest day is a buy signal. WAIT: it is not.
  last_buy <- tail(which(signals$side == "BUY"), 1)
  if (n %in% day[side == "BUY"]) {
    answer <- paste0("BUY: enter if price trades above ", bars$High[n], ", stop at ", bars$Low[n])
  } else {
    answer <- paste0("WAIT: no buy signal today, ", buys[n], " of 5 votes say BUY and 3 are needed")
    answer <- c(answer, if (length(last_buy) > 0) paste0("Last buy signal: ", signals$date[last_buy], ", enter above ",
                signals$entry[last_buy], ", stop at ", signals$stop[last_buy]) else "No buy signal in this file yet")
    answer <- c(answer, "Next one: at least 3 of the 5 votes must say BUY on the same day")
  }
} else {                       # SELL: a sell signal or a close below the stop since you bought. HOLD: neither.
  i <- max(which(bars$Date <= as.Date(bought_date)))
  stop_at <- bars$Low[i]       # our choice: the low of the day you bought (Chapter 5, slide 74: a stop sits below a trough)
  later <- if (i < n) (i + 1):n else integer(0)
  sell_day <- day[side == "SELL" & day > i]
  below <- later[bars$Close[later] < stop_at]
  pct <- sprintf("%+.1f%%", (bars$Close[n] / bought_price - 1) * 100)
  if (length(sell_day) > 0 || length(below) > 0) {
    answer <- paste0("SELL now, at about ", bars$Close[n], ", ", pct)
    answer <- c(answer, if (length(sell_day) > 0) paste0("Reason: sell signal on ", bars$Date[sell_day[1]]) else
                paste0("Reason: price closed below the stop (", stop_at, ") on ", bars$Date[below[1]]))
  } else {
    answer <- paste0("HOLD: stop at ", stop_at, ", ", pct, " so far")
  }
}
# ======== 5 DRAW THE CHART ========
dir.create("output", showWarnings = FALSE)
png(file.path("output", paste0(stock, ".png")), width = 1200, height = 1200)
layout(matrix(1:5), heights = c(3, 1, 1, 1, 1))
par(mar = c(2, 4, 3, 1))
plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(stock, "-", answer[1]))
lines(bars$Date, pldot, col = "orange")
points(signals$date, signals$entry, pch = ifelse(side == "BUY", 24, 25), bg = ifelse(side == "BUY", "darkgreen", "red"), cex = 1.5)
abline(v = bars$Date[n], lty = 2)
text(bars$Date[n], max(bars$High), strsplit(answer[1], "[: ]")[[1]][1], pos = 2, font = 2)
if (mode == "sell") { points(bars$Date[i], bought_price, pch = 4, cex = 2, lwd = 3); abline(h = stop_at, lty = 3, col = "red") }
plot(bars$Date, bars$Volume, type = "h", xlab = "", ylab = "Volume", col = ifelse(bars$Date %in% signals$date[signals$volume == "CONFIRMED"], "gold", "gray"))
abline(h = mean(bars$Volume), lty = 2)
plot(bars$Date, rsi, type = "l", xlab = "", ylab = "RSI"); abline(h = 50, lty = 2)
matplot(bars$Date, macd, type = "l", lty = 1, xlab = "", ylab = "MACD"); abline(h = 0, lty = 2)
matplot(bars$Date, sto[, c("fastK", "fastD")], type = "l", lty = 1, xlab = "", ylab = "Stochastic")
invisible(dev.off())
# ======== 6 WRITE THE ANSWER ========
write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)
writeLines(answer, "output/answer.txt")
cat(answer, sep = "\n")
