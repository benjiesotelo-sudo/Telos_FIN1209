# Williams' Oops (Lim 2016 p. 231, slides 194 and 199). Signals of a rule, not advice.
# Put CSV files in the data folder, run this script, read output/signals.csv.
empty <- data.frame(ticker = character(), date = as.Date(character()),
                    side = character(), entry = numeric(), stoploss = numeric())
all_signals <- empty
dir.create("output", showWarnings = FALSE)
for (path in list.files("data", pattern = "\\.csv$", full.names = TRUE)) {
  ticker <- sub("\\.csv$", "", basename(path))
  bars <- read.csv(path)
  bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
  signals <- empty
  for (i in seq_along(bars$Date)[-1]) {
    prev_high <- bars$High[i - 1]
    prev_low <- bars$Low[i - 1]
    if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "SELL",
                        entry = prev_high, stoploss = bars$High[i])
      signals <- rbind(signals, row)
      cat(format(bars$Date[i], "%d %b %Y"), "SELL at", prev_high, "stoploss", bars$High[i], "\n",
          " Why: it opened at", bars$Open[i], "above the previous day's high of", prev_high,
          "(a gap up), then fell back to", prev_high, "so the sell order filled.",
          "Stoploss is the day's high (Oops, slide 194)\n")
    } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "BUY",
                        entry = prev_low, stoploss = bars$Low[i])
      signals <- rbind(signals, row)
      cat(format(bars$Date[i], "%d %b %Y"), "BUY at", prev_low, "stoploss", bars$Low[i], "\n",
          " Why: it opened at", bars$Open[i], "below the previous day's low of", prev_low,
          "(a gap down), then rose back to", prev_low, "so the buy order filled.",
          "Stoploss is the day's low (Oops, slide 199)\n")
    }
  }
  png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 700)
  plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(ticker, "- Oops signals"))
  if (nrow(signals) > 0) {
    sell <- signals$side == "SELL"
    points(signals$date, signals$entry, pch = ifelse(sell, 25, 24), bg = ifelse(sell, "red", "darkgreen"), cex = 1.5)
    text(signals$date, signals$entry, labels = seq_len(nrow(signals)), pos = 3)
  }
  dev.off()
  cat(ticker, ":", nrow(signals), "signals\n")
  if (nrow(signals) > 0) {
    last <- signals[nrow(signals), ]
    cat("  latest:", last$side, "at", last$entry, "stoploss", last$stoploss, "on", format(last$date), "\n")
  }
  all_signals <- rbind(all_signals, signals)
}
write.csv(all_signals, "output/signals.csv", row.names = FALSE, quote = FALSE)
