# Draws the two "why" charts of First Automation FIN1209 from real data (oscillator version).
# Rscript build/r/explain_osc.R <out dir> <file1.csv> <ticker1> [<file2.csv> <ticker2> ...]
# The BUY and the SELL come from the first file that has one where two or more oscillators agree.
# For one real BUY and one real SELL where the oscillators agree: the price and the three oscillators
# for the weeks around that day, with what each oscillator did that day and where the entry price comes from.
suppressMessages(library(TTR))
args <- commandArgs(trailingOnly = TRUE)
out <- args[1]
files <- args[seq(2, length(args), by = 2)]; tickers <- args[seq(3, length(args), by = 2)]
cross <- function(a, b) {
  a <- round(a, 6); b <- round(rep(b, length.out = length(a)), 6)
  before <- function(x) c(NA, head(x, -1))
  s <- ifelse(a > b & before(a) <= before(b), 1, ifelse(a < b & before(a) >= before(b), -1, 0)); s[is.na(s)] <- 0; s
}
prep <- function(f) {
  bars <- read.csv(f)
  bars$Date <- as.Date(sub(" .*", "", bars$Date), tryFormats = c("%Y-%m-%d", "%m/%d/%Y"))
  rsi <- RSI(bars$Close, n = 14, maType = "SMA")
  macd <- MACD(bars$Close, nFast = 12, nSlow = 26, nSig = 9, percent = FALSE)
  sto <- stoch(bars[, c("High", "Low", "Close")], nFastK = 14, nFastD = 3)
  sig <- cbind(rsi = cross(rsi, 50), macd = cross(macd[, "macd"], macd[, "signal"]), stoch = cross(sto[, "fastK"], sto[, "fastD"]))
  list(bars = bars, rsi = rsi, macd = macd, sto = sto, sig = sig, votes = rowSums(sig))
}
D <- lapply(files, prep)
find <- function(sign) for (k in seq_along(D)) {
  x <- D[[k]]; ok <- which(sign * x$votes > 0 & rowSums(x$sig == sign) >= 2 & seq_along(x$votes) >= 36)
  if (length(ok)) return(list(k = k, i = ok[1]))
}
draw <- function(k, i, side, file) {
  bars <- D[[k]]$bars; rsi <- D[[k]]$rsi; macd <- D[[k]]$macd; sto <- D[[k]]$sto; sig <- D[[k]]$sig; ticker <- tickers[k]
  w <- max(1, i - 14):min(nrow(bars), i + 6); d <- bars$Date[w]
  sign <- if (side == "BUY") 1 else -1
  entry <- if (side == "BUY") bars$High[i] else bars$Low[i]
  who <- names(which(sig[i, ] == sign)); n_agree <- length(who)
  png(file, width = 1200, height = 900, res = 110)
  layout(matrix(1:4), heights = c(2.4, 1, 1, 1)); par(mar = c(1.5, 5, 3.5, 2))
  plot(d, bars$Close[w], type = "o", pch = 16, cex = 0.7, xlab = "", ylab = "Close", ylim = range(c(bars$Close[w], bars$High[i], bars$Low[i])),
       main = sprintf("%s: the %s on %s. %d of 3 oscillators agree (%s)", ticker, side, format(bars$Date[i]), n_agree, paste(toupper(who), collapse = " and ")))
  abline(v = bars$Date[i], lty = 2, col = "gray40")
  abline(h = entry, lty = 3, col = if (side == "BUY") "darkgreen" else "red")
  points(bars$Date[i], entry, pch = if (side == "BUY") 24 else 25, bg = if (side == "BUY") "darkgreen" else "red", cex = 2.4)
  text(bars$Date[i], entry, "1  trigger", pos = 4, cex = 1.1, font = 2)
  text(d[length(d)] + 0.4, entry, if (side == "BUY") "trigger = above that day's high (slide 201)" else "trigger = below that day's low (mirror of slide 201, our choice)", adj = c(1, if (side == "BUY") 1.6 else -0.6), cex = 0.95, col = "gray20")
  mark <- function(name, col) {
    got <- sig[i, name] == sign
    points(bars$Date[i], col, pch = 21, bg = if (got) "gold" else "white", cex = 3)
    text(bars$Date[i], col, if (got) "crossed" else "no cross", pos = 4, cex = 1.05, font = 2, col = if (got) "black" else "gray40")
  }
  plot(d, rsi[w], type = "l", ylab = "RSI 14", xlab = ""); abline(h = 50, lty = 2); abline(v = bars$Date[i], lty = 2, col = "gray40"); mark("rsi", rsi[i])
  text(d[length(d)] + 0.4, 50, "50 line (slide 74)", adj = c(1, -0.6), cex = 0.9)
  matplot(d, macd[w, ], type = "l", lty = 1, ylab = "MACD", xlab = ""); abline(v = bars$Date[i], lty = 2, col = "gray40"); mark("macd", macd[i, "macd"])
  text(d[length(d)] + 0.4, min(macd[w, ], na.rm = TRUE), "MACD (black), signal line (red), slide 83", adj = c(1, -0.6), cex = 0.9)
  par(mar = c(3, 5, 1.5, 2))
  matplot(d, sto[w, c("fastK", "fastD")], type = "l", lty = 1, ylab = "Stochastic", xlab = ""); abline(v = bars$Date[i], lty = 2, col = "gray40"); mark("stoch", sto[i, "fastK"])
  text(d[length(d)] + 0.4, 0.05, "%K (black), %D (red), slide 187", adj = c(1, -0.6), cex = 0.9)
  dev.off()
}
B <- find(1); S <- find(-1)
draw(B$k, B$i, "BUY", file.path(out, "why-buy.png")); draw(S$k, S$i, "SELL", file.path(out, "why-sell.png"))
bb <- D[[B$k]]; ss <- D[[S$k]]
cat("BUY", tickers[B$k], format(bb$bars$Date[B$i]), "entry", bb$bars$High[B$i], "agree", paste(names(which(bb$sig[B$i, ] == 1)), collapse = "+"), "\n")
cat("SELL", tickers[S$k], format(ss$bars$Date[S$i]), "entry", ss$bars$Low[S$i], "agree", paste(names(which(ss$sig[S$i, ] == -1)), collapse = "+"), "\n")
al <- do.call(rbind, lapply(D, function(x) cbind(rsi = x$rsi, macd = x$macd[, "macd"], stoch = x$sto[, "fastK"])))
r <- cor(al, use = "complete.obs")
cat(sprintf("CORR rsi_macd %.2f rsi_stoch %.2f macd_stoch %.2f\n", r["rsi", "macd"], r["rsi", "stoch"], r["macd", "stoch"]))
