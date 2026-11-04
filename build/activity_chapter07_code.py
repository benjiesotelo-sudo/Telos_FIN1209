"""The guide's running script: seven steps, each adding one idea, ending in the example script.

Every stage is a whole script that runs by itself on data/KO.csv. The last stage is the
committed example script, read from disk, so the guide's last step, the file students get
and what is typed in the video cannot differ. Placeholders {SELL_I} and {BUY_I} are filled
by the build with a real SELL and a real BUY row of the example file.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    key: str
    title: str            # the one new idea, as a heading
    text: str             # what the step teaches, in plain words
    code: str             # the whole script at this step ("" = the final file)
    after: str = ""


HEAD = '''# Williams' Oops (Lim 2016 p. 231, slides 194 and 199). Signals of a rule, not advice.
# Put CSV files in the data folder, run this script, read output/signals.csv.'''

READ = '''ticker <- "KO"
bars <- read.csv(paste0("data/", ticker, ".csv"))'''

DATE = '''bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))'''

EMPTY = '''empty <- data.frame(ticker = character(), date = as.Date(character()),
                    side = character(), entry = numeric(), stoploss = numeric())
signals <- empty'''

LOOP_PRINT = '''for (i in seq_along(bars$Date)[-1]) {
  prev_high <- bars$High[i - 1]
  prev_low <- bars$Low[i - 1]
  if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
    cat(format(bars$Date[i]), "SELL at", prev_high, "stoploss", bars$High[i], "\\n")
  } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
    cat(format(bars$Date[i]), "BUY at", prev_low, "stoploss", bars$Low[i], "\\n")
  }
}'''

LOOP_ROWS = '''for (i in seq_along(bars$Date)[-1]) {
  prev_high <- bars$High[i - 1]
  prev_low <- bars$Low[i - 1]
  if (bars$Open[i] > prev_high && bars$Low[i] <= prev_high) {
    row <- data.frame(ticker = ticker, date = bars$Date[i], side = "SELL",
                      entry = prev_high, stoploss = bars$High[i])
    signals <- rbind(signals, row)
  } else if (bars$Open[i] < prev_low && bars$High[i] >= prev_low) {
    row <- data.frame(ticker = ticker, date = bars$Date[i], side = "BUY",
                      entry = prev_low, stoploss = bars$Low[i])
    signals <- rbind(signals, row)
  }
}'''

WRITE = '''dir.create("output", showWarnings = FALSE)
write.csv(signals, "output/signals.csv", row.names = FALSE, quote = FALSE)'''

CHART = '''png(file.path("output", paste0(ticker, ".png")), width = 1200, height = 700)
plot(bars$Date, bars$Close, type = "l", xlab = "", ylab = "Close", main = paste(ticker, "- Oops signals"))
if (nrow(signals) > 0) {
  sell <- signals$side == "SELL"
  points(signals$date, signals$entry, pch = ifelse(sell, 25, 24), bg = ifelse(sell, "red", "darkgreen"), cex = 1.5)
  text(signals$date, signals$entry, labels = seq_len(nrow(signals)), pos = 3)
}
dev.off()'''

STAGES = (
    Stage("read", "Read a price file",
          "A **variable** is a name that holds a value: `ticker <- \"KO\"` puts the text KO into the name "
          "`ticker`. `read.csv()` opens a CSV file and gives back a table, which R calls a data frame. "
          "`paste0()` joins pieces of text, so the file is `data/KO.csv`. Each row is one trading day and "
          "each column is one price. A line starting with `#` is a note for people; R skips it. "
          "`head(bars, 3)` shows the first three rows.",
          HEAD + '\n' + READ + '\nprint(head(bars, 3))'),
    Stage("date", "Clean the date",
          "Google Sheets writes dates like `7/1/2026 16:00:00`. `sub(\" .*\", \"\", x)` cuts the time off, "
          "and `as.Date()` turns the text into a real date, trying each layout in `tryFormats`. "
          "`bars$Date` is the Date column, and assigning to it replaces the column.",
          HEAD + '\n' + READ + '\n' + DATE + '\nprint(head(bars$Date, 3))'),
    Stage("test", "Test one day for the Oops",
          "Square brackets pick a row: `bars$Open[i]` is the open of day `i`, and `bars$High[i - 1]` is "
          "yesterday's high. A comparison such as `>` gives `TRUE` or `FALSE`. The Oops on slide 194 "
          "asks two questions: did the day open above yesterday's high, and did price then come back down "
          "to that high, so that today's low is at or below it?",
          HEAD + '\n' + READ + '\n' + DATE + '\ni <- {SELL_I}\n'
          'print(bars$Open[i] > bars$High[i - 1])\nprint(bars$Low[i] <= bars$High[i - 1])'),
    Stage("loop", "Test every day",
          "`for (i in ...)` repeats the lines inside the braces once per day. `seq_along(bars$Date)[-1]` is "
          "every day number except the first, which has no yesterday. `if` runs its lines only when the "
          "condition is true, `&&` means both tests must pass, and `else if` is the mirror image on slide 199: "
          "open below yesterday's low, then price comes back up to it. `cat()` prints a line.",
          HEAD + '\n' + READ + '\n' + DATE + '\n' + LOOP_PRINT),
    Stage("table", "Keep the signals in a table",
          "Printing is not enough: we want a table we can save. `empty` is a table with the right columns "
          "and no rows. Each signal becomes a one-row table, added to the bottom with `rbind()`. "
          "`write.csv()` saves the table as a file, after `dir.create()` makes the output folder.",
          HEAD + '\n' + READ + '\n' + DATE + '\n' + EMPTY + '\n' + LOOP_ROWS + '\n' + WRITE),
    Stage("chart", "Draw the chart",
          "`png()` opens a picture file, the plotting commands draw into it, and `dev.off()` closes it. "
          "`plot()` draws the closing prices as a line, `points()` puts a triangle at each signal's entry price, "
          "red pointing down for SELL and green pointing up for BUY, and `text()` writes the signal's number, "
          "which is its row in `signals.csv`. The `if` skips the marks when a stock has no signals. When the "
          "picture file is closed R prints `null device 1`. That is normal.",
          HEAD + '\n' + READ + '\n' + DATE + '\n' + EMPTY + '\n' + LOOP_ROWS + '\n' + WRITE + '\n' + CHART),
    Stage("files", "Do it for every file",
          "`list.files()` lists the CSV files in `data`, and a `for` loop over them runs everything once per "
          "stock, so any file you drop in is read. The last pieces are a plain answer printed for each stock, "
          "and one table with every stock's signals. This is the finished script, exactly the file you were "
          "given.",
          ""),
)
