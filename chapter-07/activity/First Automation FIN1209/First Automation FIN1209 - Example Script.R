# First Automation FIN1209 - Example Script
# Lim's Williams' Oops (FIN1209 Chapter 7, slides 194 to 201, Lim 2016 p. 231)
# as an R script.
# Put CSV files in the data folder, run this script, read output/signals.csv
# and look at the charts in output. Add new rows and run it again.
# These are a rule's signals, not investment advice.

# ---- Settings -------------------------------------------------------------
data_folder   <- "data"
output_folder <- "output"

# ---- Read one CSV file into a table ---------------------------------------
read_bars <- function(path) {
  bars <- read.csv(path, stringsAsFactors = FALSE)
  # The Date column may carry a time ("2026-07-02 16:00:00"); keep the day.
  bars$Date <- substr(bars$Date, 1, 10)
  bars
}

# ---- Find the Oops signals in one table -----------------------------------
# Lim p. 231 (slides 194 and 199): a bar that opens above the previous bar's high puts a sell-stop
# at the previous high and a stoploss at the new bar's high (bearish Oops).
# A bar that opens below the previous bar's low puts a buy-stop at the
# previous low and a stoploss at the new bar's low (bullish Oops).
# A stop and reverse order starts at the stoploss level (slide 197), so the
# reverse column names the opposite side, to be taken at the stoploss price.
# OUR OWN CHOICES, not Lim's (the slides leave them open): a signal needs the
# fill on the same bar as the gap; no trend filter; no profit target.
find_oops <- function(bars, ticker) {
  signals <- data.frame(ticker = character(), date = character(),
                        side = character(), entry = numeric(),
                        stoploss = numeric(), reverse = character(),
                        stringsAsFactors = FALSE)
  if (nrow(bars) < 2) {
    return(signals)
  }
  for (i in 2:nrow(bars)) {
    prev_high <- bars$High[i - 1]
    prev_low  <- bars$Low[i - 1]
    if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
      # Gap up, then price falls back to the previous high: the sell-stop fills.
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "SELL",
                        entry = prev_high, stoploss = bars$High[i],
                        reverse = "BUY", stringsAsFactors = FALSE)
      signals <- rbind(signals, row)
    } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
      # Gap down, then price rises back to the previous low: the buy-stop fills.
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "BUY",
                        entry = prev_low, stoploss = bars$Low[i],
                        reverse = "SELL", stringsAsFactors = FALSE)
      signals <- rbind(signals, row)
    }
  }
  signals
}

# ---- Draw the chart with the signals marked -------------------------------
# Black and white candles; a red down triangle is a SELL entry, a green up
# triangle is a BUY entry, the short dash is its stoploss, and the number is
# the signal's row number for this ticker in signals.csv.
draw_chart <- function(bars, signals, ticker, path) {
  n <- nrow(bars)
  png(path, width = 1400, height = 800, res = 120)
  plot(NA, xlim = c(0.5, n + 0.5), ylim = range(bars$Low, bars$High),
       xaxt = "n", xlab = "", ylab = "Price",
       main = paste(ticker, "- Williams' Oops signals"))
  ticks <- unique(round(seq(1, n, length.out = 8)))
  axis(1, at = ticks, labels = bars$Date[ticks], cex.axis = 0.8)
  segments(1:n, bars$Low, 1:n, bars$High)
  rect(1:n - 0.3, pmin(bars$Open, bars$Close),
       1:n + 0.3, pmax(bars$Open, bars$Close),
       col = ifelse(bars$Close >= bars$Open, "white", "black"))
  if (nrow(signals) > 0) {
    x <- match(signals$date, bars$Date)
    is_sell <- signals$side == "SELL"
    mark_col <- ifelse(is_sell, "red", "darkgreen")
    points(x, signals$entry, pch = ifelse(is_sell, 25, 24),
           bg = mark_col, col = mark_col, cex = 1.6)
    points(x, signals$stoploss, pch = 95, col = mark_col, cex = 2)
    text(x, signals$stoploss, labels = seq_len(nrow(signals)),
         pos = ifelse(is_sell, 3, 1), col = mark_col, cex = 0.9, font = 2)
  }
  legend("topleft", legend = c("SELL entry", "BUY entry", "stoploss"),
         pch = c(25, 24, 95), col = c("red", "darkgreen", "gray30"),
         pt.bg = c("red", "darkgreen", NA), bg = "white", cex = 0.8)
  dev.off()
}

# ---- Main: every CSV in the data folder ------------------------------------
dir.create(output_folder, showWarnings = FALSE)
files <- list.files(data_folder, pattern = "\\.csv$", full.names = TRUE)
all_signals <- NULL
for (path in files) {
  ticker  <- sub("\\.csv$", "", basename(path))
  bars    <- read_bars(path)
  signals <- find_oops(bars, ticker)
  draw_chart(bars, signals, ticker,
             file.path(output_folder, paste0(ticker, ".png")))
  all_signals <- rbind(all_signals, signals)
  cat(ticker, ":", nrow(signals), "signals\n")
}
if (is.null(all_signals)) {
  all_signals <- data.frame(ticker = character(), date = character(),
                            side = character(), entry = numeric(),
                            stoploss = numeric(), reverse = character())
}
write.csv(all_signals, file.path(output_folder, "signals.csv"),
          row.names = FALSE, quote = FALSE)
cat("Wrote", file.path(output_folder, "signals.csv"), "\n")
