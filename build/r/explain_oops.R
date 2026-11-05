# Draws the two "why" charts of First Automation FIN1209 from real data.
# Rscript build/r/explain_oops.R <KO.csv> <out dir>
# Picks the SELL and the BUY with the widest gap, then draws just the yesterday bar and the signal bar
# with numbered marks: 1 yesterday's high (or low), 2 the open that gaps past it, 3 price coming
# back to it (the entry), 4 the stoploss.
args <- commandArgs(trailingOnly = TRUE)
bars <- read.csv(args[1])
bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
out <- args[2]
n <- nrow(bars)
gap_up <- rep(NA_real_, n); gap_dn <- rep(NA_real_, n)
for (i in 2:n) {
  if (bars$Open[i] > bars$High[i - 1] && bars$Low[i] <= bars$High[i - 1]) gap_up[i] <- bars$Open[i] - bars$High[i - 1]
  if (bars$Open[i] < bars$Low[i - 1] && bars$High[i] >= bars$Low[i - 1]) gap_dn[i] <- bars$Low[i - 1] - bars$Open[i]
}
draw <- function(i, side, file) {
  prev <- bars[i - 1, ]; cur <- bars[i, ]
  sell <- side == "SELL"
  level <- if (sell) prev$High else prev$Low
  stop_at <- if (sell) cur$High else cur$Low
  lo <- min(prev$Low, cur$Low) ; hi <- max(prev$High, cur$High)
  pad <- (hi - lo) * 0.18
  png(file, width = 1200, height = 700, res = 110)
  par(mar = c(3, 5, 4, 2))
  plot(NA, xlim = c(0.4, 4.4), ylim = c(lo - pad, hi + pad), xaxt = "n", xlab = "", ylab = "Price",
       main = paste0(args[3], ": the ", side, " on ", format(cur$Date)))
  axis(1, at = c(1, 2), labels = c(paste("yesterday", format(prev$Date)), paste("today", format(cur$Date))), tick = FALSE)
  for (k in 1:2) {
    b <- bars[i - 2 + k, ]
    segments(k, b$Low, k, b$High, lwd = 2)
    rect(k - 0.18, min(b$Open, b$Close), k + 0.18, max(b$Open, b$Close), col = if (b$Close >= b$Open) "white" else "black", lwd = 2)
  }
  abline(h = level, lty = 2, col = "gray40")
  abline(h = stop_at, lty = 3, col = "orange3")
  col <- if (sell) "red" else "darkgreen"
  mark <- function(x, y, num, label, dy = 0) {
    points(x, y, pch = 21, bg = "gold", cex = 3.2)
    text(x, y, num, font = 2, cex = 1.1)
    text(x + 0.17, y + dy, label, pos = 4, cex = 1.05, col = "gray15")
  }
  up <- if (sell) 1 else -1
  mark(1, level, "1", paste0(if (sell) "yesterday's high " else "yesterday's low ", sprintf("%.2f", level)), -up * pad * 0.6)
  mark(2, cur$Open, "2", paste0("today opens ", sprintf("%.2f", cur$Open), if (sell) ", above it" else ", below it"), -up * pad * 0.45)
  mark(2.55, level, "3", paste0("price comes back to ", sprintf("%.2f", level), ": ", side, " here"), 0)
  mark(2, stop_at, "4", paste0("stoploss ", sprintf("%.2f", stop_at), " (today's ", if (sell) "high)" else "low)"), up * pad * 0.45)
  points(2.55, level, pch = if (sell) 25 else 24, bg = col, cex = 2.2)
  dev.off()
}
si <- which.max(gap_up); bi <- which.max(gap_dn)
draw(si, "SELL", file.path(out, "why-sell.png"))
draw(bi, "BUY", file.path(out, "why-buy.png"))
cat("SELL", format(bars$Date[si]), "entry", bars$High[si - 1], "stoploss", bars$High[si], "\n")
cat("BUY", format(bars$Date[bi]), "entry", bars$Low[bi - 1], "stoploss", bars$Low[bi], "\n")
