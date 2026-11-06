"""The example script's flowchart, as plain data for build/bpmnkit.py.

Five stages (Settings and data, Measure, Signal days, Answer, Report). A data object names the input file and its types.
Every metric task has a text annotation with its rule, settings and slide. The agreement count is its
own gateway, the volume check is its own task (volume is not a vote), the price rules are annotated, the
outputs are data objects, and the next-file loop returns to the read task. Every task carries a number;
the manual's table ties each number to the lines of the example script it stands for.
"""

from bpmnkit import Diagram, Edge, Node

T, X = "task", "xor"


def _t(i, num, cx, cy, *lines):
    return Node(i, T, f"{num}. " + " ".join(lines), cx, cy, (f"{num}. " + lines[0],) + tuple(lines[1:]))


def _n(i, cx, cy, w, h, *lines):
    return Node(i, "note", " ".join(lines), cx, cy, tuple(lines), w=w, h=h)


def build() -> Diagram:
    d = Diagram("BuySellExample", "Example script: five votes, then a buy or sell answer")
    G = lambda i, name, x0, x1: Node(i, "group", name, (x0 + x1) / 2, 505, (), w=x1 - x0, h=970)
    d.nodes = [
        G("S1", "Settings and data", 10, 270), G("S2", "Measure: five votes", 280, 720), G("S3", "Signal days", 730, 1010),
        G("S4", "Answer", 1020, 1550), G("S5", "Report", 1560, 1860),
        Node("Start", "start", "Run the script", 140, 70, ("Run the script",), "right"),
        _t("T1", 1, 140, 170, "Read the settings:", "mode, stock,", "bought price, date"),
        _t("T2", 2, 140, 400, "Read the data file", "for the stock"),
        Node("D1", "data", "data/<stock>.csv", 140, 520, ("data/<stock>.csv",), "right"),
        _n("N1", 140, 670, 240, 124, "Input: one CSV file per stock,", "about a year of daily rows.", "Date (a date)",
           "Open, High, Low, Close (prices,", "numbers)", "Volume (a whole number)"),
        _n("Na", 385, 140, 200, 100, "Price trend (Chapter 5)", "Close above its 3 bar average", "of closes: up, else down",
           "(slides 109, 110)"),
        _t("T3", 3, 610, 140, "Vote 1: price trend", "up or down"),
        _n("Nb", 385, 300, 200, 112, "Price bar (Chapter 7)", "BUY: new low, close at or", "above the previous close",
           "SELL: new high, close at or", "below it (slides 123, 126)"),
        _t("T4", 4, 610, 300, "Vote 2: price bar", "(key reversal)"),
        _n("N2", 385, 470, 200, 100, "RSI, 14 days (slide 195)", "BUY: crosses above 50", "SELL: crosses below 50",
           "(slide 74)"),
        _t("T5", 5, 610, 470, "Vote 3: RSI", "crossing 50"),
        _n("N3", 385, 640, 200, 124, "MACD 12, 26, signal line 9", "(slides 166 to 168)", "BUY: MACD crosses above", "its signal line",
           "SELL: crosses below it", "(slide 83)"),
        _t("T6", 6, 610, 640, "Vote 4: MACD", "crossing its signal"),
        _n("N4", 385, 810, 200, 112, "Stochastic: %K 14 days,", "%D = 3 day average", "BUY: %K crosses above %D",
           "SELL: %K crosses below %D", "(slides 185, 187)"),
        _t("T7", 7, 610, 810, "Vote 5: stochastic", "%K crossing %D"),
        _t("T8", 8, 870, 100, "Count the BUY and", "SELL votes", "for each day"),
        Node("G2", X, "3 or more of the 5 votes agree?", 870, 225, ("3 or more of", "the 5 agree?"), "belowleft"),
        _t("T9", 9, 870, 350, "Record the", "signal day: side,", "trigger, stop, agree"),
        _n("N8", 945, 475, 110, 100, "Volume above", "the file's average:", "CONFIRMED", "(slide 128).", "Not a vote."),
        Node("M", X, "", 870, 600, (), "right"),
        Node("G3", X, "Mode: buy or sell?", 1150, 600, ("mode: buy", "or sell?"), "belowleft"),
        Node("G4", X, "Buy signal today?", 1150, 330, ("Buy signal", "today?"), "aboveleft"),
        _t("T10", 10, 1330, 330, "BUY: enter above", "the signal day's high,", "stop at its low"),
        _n("N10", 1330, 215, 200, 80, "Trigger above the high (slide 201).", "Stop at the low: our choice", "(Chapter 5, slide 74 idea)."),
        _t("T11", 11, 1150, 130, "WAIT: show the last", "buy signal and what", "must happen next"),
        Node("G5", X, "Sell signal since you bought, or close below the stop?", 1150, 770, ("Sell signal, or", "close below stop?"), "aboveleft"),
        _t("T12", 12, 1330, 770, "SELL now, at about", "the last close,", "+/- % since you bought"),
        _n("N11", 1330, 655, 210, 90, "Sell signal after your buy day,", "or a close below the stop.", "Stop = the low of your buy day:", "our choice (Chapter 5, slide 74)."),
        _t("T13", 13, 1150, 890, "HOLD: stop at the", "low of your buy", "day, +/- % so far"),
        _t("T14", 14, 1675, 420, "Draw the chart,", "today's answer", "marked on it"),
        Node("D2", "data", "chart (PNG)", 1805, 420, ("chart", "output/<stock>.png"), "below"),
        _t("T15", 15, 1675, 560, "Write signals.csv", "and answer.txt,", "print the answer"),
        Node("D3", "data", "signals.csv", 1805, 545, ("signals.csv",), "below"),
        Node("D4", "data", "answer.txt", 1805, 640, ("answer.txt",), "below"),
        Node("End", "end", "Answer ready", 1675, 730, ("Answer ready",)),
    ]
    E = lambda i, a, b, pts, lab="", k="flow": Edge(i, a, b, tuple(pts), lab, k)
    d.edges = [
        E("F1", "Start", "T1", [(140, 98), (140, 138)]),
        E("F2", "T1", "T2", [(140, 202), (140, 368)]),
        E("A1", "D1", "T2", [(140, 495), (140, 432)], "", "datain"),
        E("A2", "N1", "D1", [(140, 608), (140, 545)], "", "assoc"),
        E("F3", "T2", "T3", [(205, 400), (250, 400), (250, 55), (610, 55), (610, 108)]),
        E("Aa", "T3", "Na", [(545, 140), (485, 140)], "", "assoc"),
        E("F4", "T3", "T4", [(610, 172), (610, 268)]),
        E("Ab", "T4", "Nb", [(545, 300), (485, 300)], "", "assoc"),
        E("F5", "T4", "T5", [(610, 332), (610, 438)]),
        E("A3", "T5", "N2", [(545, 470), (485, 470)], "", "assoc"),
        E("F6", "T5", "T6", [(610, 502), (610, 608)]),
        E("A4", "T6", "N3", [(545, 640), (485, 640)], "", "assoc"),
        E("F7", "T6", "T7", [(610, 672), (610, 778)]),
        E("A5", "T7", "N4", [(545, 810), (485, 810)], "", "assoc"),
        E("F8", "T7", "T8", [(675, 810), (700, 810), (700, 100), (805, 100)]),
        E("F9", "T8", "G2", [(870, 132), (870, 200)]),
        E("F10", "G2", "T9", [(870, 250), (870, 318)], "yes"),
        E("A6", "T9", "N8", [(910, 382), (910, 425)], "", "assoc"),
        E("F11", "T9", "M", [(870, 382), (870, 575)]),
        E("F12", "G2", "M", [(845, 225), (745, 225), (745, 600), (845, 600)], "no: skip"),
        E("F13", "M", "G3", [(895, 600), (1125, 600)]),
        E("F14", "G3", "G4", [(1150, 575), (1150, 355)], "buy"),
        E("F15", "G4", "T10", [(1175, 330), (1265, 330)], "yes"),
        E("A7", "T10", "N10", [(1330, 298), (1330, 255)], "", "assoc"),
        E("F16", "G4", "T11", [(1150, 305), (1150, 162)], "no"),
        E("F17", "G3", "G5", [(1150, 625), (1150, 745)], "sell"),
        E("F18", "G5", "T12", [(1175, 770), (1265, 770)], "yes"),
        E("A8", "T12", "N11", [(1330, 738), (1330, 700)], "", "assoc"),
        E("F19", "G5", "T13", [(1150, 795), (1150, 858)], "no"),
        E("F20", "T11", "T14", [(1215, 130), (1595, 130), (1595, 405), (1610, 405)]),
        E("F21", "T10", "T14", [(1395, 330), (1585, 330), (1585, 415), (1610, 415)]),
        E("F22", "T12", "T14", [(1395, 770), (1565, 770), (1565, 425), (1610, 425)]),
        E("F23", "T13", "T14", [(1215, 890), (1575, 890), (1575, 435), (1610, 435)]),
        E("F24", "T14", "T15", [(1675, 452), (1675, 528)]),
        E("O1", "T14", "D2", [(1740, 420), (1787, 420)], "", "dataout"),
        E("O2", "T15", "D3", [(1740, 548), (1787, 548)], "", "dataout"),
        E("O3", "T15", "D4", [(1740, 575), (1760, 575), (1760, 640), (1787, 640)], "", "dataout"),
        E("F25", "T15", "End", [(1675, 592), (1675, 712)]),
    ]
    return d
