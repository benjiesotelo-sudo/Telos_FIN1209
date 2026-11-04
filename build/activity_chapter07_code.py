"""The R basics guide's running script, one stage per step.

Every stage is a whole script that runs by itself on data/KO.csv. The last
stage is not typed here: it is the committed example script, read from disk,
so the guide's last step and the file students are given cannot differ.
Placeholders {SELL_I} and {BUY_I} are filled by the build with the row of a
real SELL and a real BUY in the example file, so the prints are true.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    key: str
    title: str            # the one new idea, as a heading
    text: str             # what the step teaches, plain words
    code: str             # the whole script at this step ("" = the final file)
    after: str = ""       # a sentence after the output


READ = '''data_file <- "data/KO.csv"
bars <- read.csv(data_file, stringsAsFactors = FALSE)'''

TRIM = '''bars$Date <- substr(bars$Date, 1, 10)'''

LOOP_BODY = '''  prev_high <- bars$High[i - 1]
  prev_low  <- bars$Low[i - 1]
  if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
    cat(bars$Date[i], "SELL at", prev_high, "stoploss", bars$High[i], "\\n")
  } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
    cat(bars$Date[i], "BUY at", prev_low, "stoploss", bars$Low[i], "\\n")
  }'''

TABLE_HEAD = '''signals <- data.frame(ticker = character(), date = character(),
                      side = character(), entry = numeric(),
                      stoploss = numeric(), reverse = character(),
                      stringsAsFactors = FALSE)'''

LOOP_COLLECT = '''for (i in 2:nrow(bars)) {
  prev_high <- bars$High[i - 1]
  prev_low  <- bars$Low[i - 1]
  if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
    row <- data.frame(ticker = "KO", date = bars$Date[i], side = "SELL",
                      entry = prev_high, stoploss = bars$High[i],
                      reverse = "BUY", stringsAsFactors = FALSE)
    signals <- rbind(signals, row)
  } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
    row <- data.frame(ticker = "KO", date = bars$Date[i], side = "BUY",
                      entry = prev_low, stoploss = bars$Low[i],
                      reverse = "SELL", stringsAsFactors = FALSE)
    signals <- rbind(signals, row)
  }
}'''

WRITE = '''dir.create("output", showWarnings = FALSE)
write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)'''

CANDLES = '''n <- nrow(bars)
png("output/KO.png", width = 1400, height = 800, res = 120)
plot(NA, xlim = c(0.5, n + 0.5), ylim = range(bars$Low, bars$High),
     xaxt = "n", xlab = "", ylab = "Price", main = "KO")
ticks <- unique(round(seq(1, n, length.out = 8)))
axis(1, at = ticks, labels = bars$Date[ticks], cex.axis = 0.8)
segments(1:n, bars$Low, 1:n, bars$High)
rect(1:n - 0.3, pmin(bars$Open, bars$Close),
     1:n + 0.3, pmax(bars$Open, bars$Close),
     col = ifelse(bars$Close >= bars$Open, "white", "black"))'''

MARKS = '''x <- match(signals$date, bars$Date)
is_sell <- signals$side == "SELL"
mark_col <- ifelse(is_sell, "red", "darkgreen")
points(x, signals$entry, pch = ifelse(is_sell, 25, 24),
       bg = mark_col, col = mark_col, cex = 1.6)
points(x, signals$stoploss, pch = 95, col = mark_col, cex = 2)
text(x, signals$stoploss, labels = seq_len(nrow(signals)),
     pos = ifelse(is_sell, 3, 1), col = mark_col, cex = 0.9, font = 2)
legend("topleft", legend = c("SELL entry", "BUY entry", "stoploss"),
       pch = c(25, 24, 95), col = c("red", "darkgreen", "gray30"),
       pt.bg = c("red", "darkgreen", NA), bg = "white", cex = 0.8)
dev.off()'''

FUNCS_BODY = '''read_bars <- function(path) {
  bars <- read.csv(path, stringsAsFactors = FALSE)
  bars$Date <- substr(bars$Date, 1, 10)
  bars
}

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
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "SELL",
                        entry = prev_high, stoploss = bars$High[i],
                        reverse = "BUY", stringsAsFactors = FALSE)
      signals <- rbind(signals, row)
    } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
      row <- data.frame(ticker = ticker, date = bars$Date[i], side = "BUY",
                        entry = prev_low, stoploss = bars$Low[i],
                        reverse = "SELL", stringsAsFactors = FALSE)
      signals <- rbind(signals, row)
    }
  }
  signals
}

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
}'''

STAGES = (
    Stage("variable", "A named value (a variable)",
          "A variable is a name that holds a value. The arrow `<-` puts the "
          "value on the right into the name on the left. Text goes inside "
          "quotes. A line that starts with `#` is a comment: a note for "
          "people, which R skips.\n\n`print()` shows a value in the Console.",
          '# the file we will read\ndata_file <- "data/KO.csv"\nprint(data_file)'),
    Stage("read", "Read a CSV file into a table",
          "`read.csv()` opens a CSV file and returns a table, which R calls a "
          "data frame. Each row is one trading day (one bar) and each column "
          "is one kind of price. `head(bars, 3)` shows only the first three "
          "rows.",
          '# the file we will read\n' + READ + '\nprint(head(bars, 3))'),
    Stage("column", "One column is a list of values (a vector)",
          "`bars$High` is the whole High column. R calls a list of values "
          "like this a vector. Square brackets pick a position: `highs[4]` "
          "is the fourth value and `highs[1:5]` is the first five.",
          READ + '\nhighs <- bars$High\nprint(highs[1:5])\nprint(highs[4])'),
    Stage("trim", "Cut text down (the date)",
          "The Date column is text and may carry a time, like "
          "`2026-07-02 16:00:00`. `substr(text, 1, 10)` keeps only the first "
          "ten characters, the day. Assigning to `bars$Date` replaces the "
          "column.",
          READ + '\n' + TRIM + '\nprint(bars$Date[1:3])'),
    Stage("compare", "Compare two numbers",
          "A comparison such as `>` or `<=` gives `TRUE` or `FALSE`. We use "
          "the fourth bar, `i <- 4`. The previous bar is `i - 1`. The first "
          "test asks the Oops question: did this bar open above the previous "
          "bar's high? The second asks whether price then came back to that "
          "high, that is, whether this bar's low is at or below it.",
          READ + '\n' + TRIM + '\ni <- {SELL_I}\n'
          'print(bars$Open[i] > bars$High[i - 1])\n'
          'print(bars$Low[i] <= bars$High[i - 1])'),
    Stage("if", "Decide with if",
          "`if (condition) { ... }` runs the lines inside the braces only when "
          "the condition is `TRUE`. `&&` means both conditions must be "
          "true. `cat()` prints text and values on one line. This is "
          "the bearish Oops on slide 194.",
          READ + '\n' + TRIM + '\ni <- {SELL_I}\n'
          'prev_high <- bars$High[i - 1]\n'
          'if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {\n'
          '  cat(bars$Date[i], "SELL at", prev_high, "stoploss", bars$High[i], "\\n")\n'
          '}'),
    Stage("elseif", "Give if a second case (else if)",
          "`else if` is tried only when the first condition is `FALSE`. The "
          "bullish Oops on slide 199 is the mirror image: open below the "
          "previous low, then price comes back up to it. We change `i` to a "
          "bar that opened below the previous low.",
          READ + '\n' + TRIM + '\ni <- {BUY_I}\n'
          'prev_high <- bars$High[i - 1]\nprev_low  <- bars$Low[i - 1]\n'
          'if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {\n'
          '  cat(bars$Date[i], "SELL at", prev_high, "stoploss", bars$High[i], "\\n")\n'
          '} else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {\n'
          '  cat(bars$Date[i], "BUY at", prev_low, "stoploss", bars$Low[i], "\\n")\n'
          '}'),
    Stage("loop", "Repeat for every bar (a loop over rows)",
          "`for (i in 2:nrow(bars))` runs the lines inside the braces once "
          "for every bar from the second to the last, with `i` taking each "
          "number in turn. We start at 2 because the first bar has no "
          "previous bar.",
          READ + '\n' + TRIM + '\nfor (i in 2:nrow(bars)) {\n' + LOOP_BODY + '\n}'),
    Stage("table", "Collect the results in a table",
          "Printing is not enough: we want a table we can save. First make an "
          "empty table with named columns. Then each time a signal is found, "
          "build a one-row table and add it to the bottom with `rbind()`.",
          READ + '\n' + TRIM + '\n' + TABLE_HEAD + '\n' + LOOP_COLLECT +
          '\nprint(head(signals, 4))\ncat(nrow(signals), "signals\\n")'),
    Stage("write", "Write a CSV file",
          "`write.csv()` saves a table as a CSV file. `dir.create()` makes "
          "the output folder first (it does nothing if the folder exists). "
          "Open the new file to see the signals.",
          READ + '\n' + TRIM + '\n' + TABLE_HEAD + '\n' + LOOP_COLLECT + '\n' + WRITE +
          '\ncat("Wrote output/signals.csv\\n")'),
    Stage("plot", "Draw a chart",
          "`png()` opens a picture file, the plot commands draw into it and "
          "`dev.off()` closes it. `plot()` makes the empty frame, "
          "`segments()` draws each bar's high-to-low line and `rect()` draws "
          "its body from the open to the close: white when the bar closed "
          "up, black when it closed down. When the picture file is closed R "
          "prints `null device 1`. That is normal.",
          READ + '\n' + TRIM + '\n' + TABLE_HEAD + '\n' + LOOP_COLLECT + '\n' + WRITE +
          '\n' + CANDLES + '\ndev.off()'),
    Stage("marks", "Mark the signals on the chart",
          "Chart commands draw on top of what is already there. `points()` "
          "puts a triangle at each signal's entry price: red pointing down "
          "for SELL, green pointing up for BUY. A short dash marks the "
          "stoploss and `text()` writes the signal's number just beyond that dash; it is its "
          "row in `signals.csv`.",
          READ + '\n' + TRIM + '\n' + TABLE_HEAD + '\n' + LOOP_COLLECT + '\n' + WRITE +
          '\n' + CANDLES + '\n' + MARKS),
    Stage("function", "Give a block of code a name (a function)",
          "A function packs lines under a name so they can be reused. "
          "`name <- function(inputs) { ... }` defines it, and the last value "
          "it produces is what it gives back. We make three: `read_bars`, "
          "`find_oops` and `draw_chart`. The lines inside are the ones you "
          "already wrote; only the packaging is new.",
          FUNCS_BODY + '\n\nbars    <- read_bars("data/KO.csv")\n'
          'signals <- find_oops(bars, "KO")\n'
          'dir.create("output", showWarnings = FALSE)\n'
          'draw_chart(bars, signals, "KO", "output/KO.png")\n'
          'write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)\n'
          'cat(nrow(signals), "signals\\n")'),
    Stage("files", "Repeat for every file (a loop over files)",
          "`list.files()` returns the names of the files in a folder. A "
          "`for` loop over them runs the three functions once per file, so "
          "any CSV you drop into `data` is read. Adding and saving all the "
          "signals together is the last piece. This is the finished script, "
          "exactly the file you were given.",
          ""),
)
