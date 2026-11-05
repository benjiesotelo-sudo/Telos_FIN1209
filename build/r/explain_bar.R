# Draws the price-and-volume "why" chart of First Automation FIN1209 from real data.
# Rscript build/r/explain_bar.R <out dir> <file1.csv> <ticker1> [<file2.csv> <ticker2> ...]
# A key reversal day (Chapter 7, slides 123 and 126) on above-average volume (slide 128): the first one
# in the files where the trend vote agrees with the bar, marked 1 to 4 as the slides mark Figure 7.15.
args <- commandArgs(trailingOnly = TRUE)
out <- args[1]; files <- args[seq(2, length(args), by = 2)]; tickers <- args[seq(3, length(args), by = 2)]
suppressMessages(library(TTR))
found <- NULL
for (k in seq_along(files)) {
  b <- read.csv(files[k]); b$Date <- as.Date(sub(" .*", "", b$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
  n <- nrow(b); pl <- SMA(b$Close, 3); avg <- mean(b$Volume)
  for (i in 5:n) {
    bear <- b$High[i] > b$High[i - 1] && b$Close[i] <= b$Close[i - 1]
    bull <- b$Low[i] < b$Low[i - 1] && b$Close[i] >= b$Close[i - 1]
    if (!bear && !bull) next
    up <- b$Close[i] > pl[i]
    if (b$Volume[i] > avg && ((bull && up) || (bear && !up))) { found <- list(k = k, i = i, bull = bull, b = b, avg = avg); break }
  }
  if (!is.null(found)) break
}
stopifnot(!is.null(found))
b <- found$b; i <- found$i; bull <- found$bull; side <- if (bull) "BUY" else "SELL"
w <- (i - 6):(i + 2); w <- w[w >= 1 & w <= nrow(b)]; x <- seq_along(w); xi <- which(w == i)
png(file.path(out, "why-bar.png"), width = 1200, height = 900, res = 110)
layout(matrix(1:2), heights = c(2.3, 1)); par(mar = c(1.5, 5, 3.5, 2))
lo <- min(b$Low[w]); hi <- max(b$High[w]); pad <- (hi - lo) * 0.25
plot(NA, xlim = c(0.5, length(w) + 4.2), ylim = c(lo - pad * 0.3, hi + pad), xaxt = "n", xlab = "", ylab = "Price",
     main = sprintf("%s: a %s key reversal day on %s, on above-average volume", tickers[found$k], if (bull) "bullish" else "bearish", format(b$Date[i])))
for (j in x) {
  r <- b[w[j], ]
  segments(j, r$Low, j, r$High, lwd = 2)
  rect(j - 0.22, min(r$Open, r$Close), j + 0.22, max(r$Open, r$Close), col = if (r$Close >= r$Open) "white" else "black", lwd = 2)
}
prev <- b[i - 1, ]; cur <- b[i, ]
lvl <- if (bull) prev$Low else prev$High
abline(h = prev$Close, lty = 3, col = "blue"); abline(h = lvl, lty = 2, col = "gray40")
mk <- function(xx, yy, num, label, dy = 0) { points(xx, yy, pch = 21, bg = "gold", cex = 3); text(xx, yy, num, font = 2); text(xx + 0.3, yy + dy, label, pos = 4, cex = 1) }
mk(xi - 1, lvl, "1", if (bull) sprintf("yesterday's low %.2f", lvl) else sprintf("yesterday's high %.2f", lvl), if (bull) -pad * 0.2 else pad * 0.2)
mk(xi, if (bull) cur$Low else cur$High, "2", if (bull) sprintf("a new low %.2f", cur$Low) else sprintf("a new high %.2f", cur$High), if (bull) -pad * 0.2 else pad * 0.2)
mk(xi, cur$Close, "3", sprintf("closes %.2f, %s yesterday's close %.2f", cur$Close, if (bull) "above" else "below", prev$Close), 0)
par(mar = c(3, 5, 1.5, 2))
plot(x, b$Volume[w] / 1e6, type = "h", xlim = c(0.5, length(w) + 4.2), ylim = c(0, max(b$Volume[w]) / 1e6 * 1.15), lwd = 8, lend = 1, xaxt = "n", xlab = "", ylab = "Volume (millions)", col = ifelse(w == i, "gold", "gray70"))
abline(h = found$avg / 1e6, lty = 2)
text(length(w) + 4.2, found$avg / 1e6, "average volume of the file", adj = c(1, -0.5), cex = 0.95)
mk(xi, b$Volume[i] / 1e6, "4", sprintf("%.1f million, above the average %.1f", b$Volume[i] / 1e6, found$avg / 1e6), 0)
axis(1, at = x, labels = format(b$Date[w], "%b %d"), tick = FALSE)
dev.off()
cat(sprintf("BAR %s %s %s volume %.1f avg %.1f\n", tickers[found$k], format(b$Date[i]), side, b$Volume[i] / 1e6, found$avg / 1e6))
