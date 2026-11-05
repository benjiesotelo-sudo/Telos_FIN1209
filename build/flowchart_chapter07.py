"""The example script's flowchart, as plain data for build/bpmnkit.py.

Four stages (Data in, Measure, Decide, Report). A data object names the input file and its types.
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
    d = Diagram("VotesExample", "Example script: five votes and a volume check")
    G = lambda i, name, x0, x1: Node(i, "group", name, (x0 + x1) / 2, 505, (), w=x1 - x0, h=970)
    d.nodes = [
        G("S1", "Data in", 10, 270), G("S2", "Measure: five votes", 280, 720), G("S3", "Decide", 730, 1150), G("S4", "Report", 1160, 1540),
        Node("Start", "start", "Run the script", 140, 80, ("Run the script",), "right"),
        _t("T1", 1, 140, 170, "List the CSV", "files in the", "data folder"),
        _t("T2", 2, 140, 300, "Read each file", "and clean its dates"),
        Node("D1", "data", "data/<ticker>.csv", 140, 440, ("data/<ticker>.csv",), "right"),
        _n("N1", 140, 590, 240, 124, "Input: one CSV file per stock,", "about a year of daily rows.", "Date (a date)",
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
        _t("T8", 8, 940, 100, "Add the five votes", "for each day"),
        Node("G2", X, "Did a bar or oscillator fire, and the votes do not cancel?", 940, 225,
             ("Signal day?", "(a bar or oscillator", "fired, votes not cancel)"), "belowleft"),
        _t("T9", 9, 940, 350, "Choose BUY or", "SELL by net vote"),
        Node("G3", X, "BUY or SELL?", 940, 465, ("BUY or SELL?",), "below"),
        _n("N5", 814, 380, 118, 62, "BUY price = the", "day's high", "(slide 201)"),
        _n("N6", 1085, 380, 150, 62, "SELL price = the close:", "our choice, the slides", "give no sell trigger"),
        _t("T10", 10, 800, 465, "BUY price =", "the day's high"),
        _t("T11", 11, 1085, 465, "SELL price =", "the day's close"),
        _t("T12", 12, 940, 640, "Record the", "signal day: side,", "price, agree"),
        _n("N7", 1085, 640, 130, 80, "agree = the votes", "on the winning", "side, of five"),
        _t("T13", 13, 940, 770, "Mark the volume:", "CONFIRMED if above", "the average"),
        _n("N8", 1085, 770, 130, 80, "Volume is not a vote.", "Average of the whole", "file (slide 128)"),
        Node("M", X, "", 940, 890, (), "right"),
        _t("T14", 14, 1250, 100, "Draw the chart:", "price, volume, and", "three oscillators"),
        Node("D2", "data", "chart (PNG)", 1450, 100, ("chart", "output/<ticker>.png"), "below"),
        _t("T15", 15, 1250, 250, "Print a summary", "for this stock"),
        Node("D3", "data", "console summary", 1450, 250, ("console summary", "(signal days, votes)"), "below"),
        _t("T16", 16, 1250, 400, "Add its signals", "to the full list"),
        Node("G4", X, "Another file left?", 1250, 530, ("Another", "file left?"), "aboveleft"),
        _t("T17", 17, 1250, 670, "Write the", "signals table"),
        Node("D4", "data", "signals.csv", 1450, 670, ("signals.csv",), "below"),
        _n("N9", 1440, 800, 200, 100, "ticker, date, side, entry,", "trend, bar, rsi, macd, stoch,", "agree (votes on the side),",
           "volume (CONFIRMED or NOT)"),
        Node("End", "end", "Signals and charts ready", 1240, 820, ("Signals and", "charts ready")),
    ]
    E = lambda i, a, b, pts, lab="", k="flow": Edge(i, a, b, tuple(pts), lab, k)
    d.edges = [
        E("F1", "Start", "T1", [(140, 98), (140, 138)]),
        E("F2", "T1", "T2", [(140, 202), (140, 268)]),
        E("A1", "D1", "T2", [(140, 415), (140, 332)], "", "datain"),
        E("A2", "N1", "D1", [(140, 528), (140, 465)], "", "assoc"),
        E("F3", "T2", "T3", [(205, 300), (250, 300), (250, 55), (610, 55), (610, 108)]),
        E("Aa", "T3", "Na", [(545, 140), (485, 140)], "", "assoc"),
        E("F4", "T3", "T4", [(610, 172), (610, 268)]),
        E("Ab", "T4", "Nb", [(545, 300), (485, 300)], "", "assoc"),
        E("F5", "T4", "T5", [(610, 332), (610, 438)]),
        E("A3", "T5", "N2", [(545, 470), (485, 470)], "", "assoc"),
        E("F6", "T5", "T6", [(610, 502), (610, 608)]),
        E("A4", "T6", "N3", [(545, 640), (485, 640)], "", "assoc"),
        E("F7", "T6", "T7", [(610, 672), (610, 778)]),
        E("A5", "T7", "N4", [(545, 810), (485, 810)], "", "assoc"),
        E("F8", "T7", "T8", [(675, 810), (700, 810), (700, 100), (875, 100)]),
        E("F9", "T8", "G2", [(940, 132), (940, 200)]),
        E("F10", "G2", "T9", [(940, 250), (940, 318)], "yes"),
        E("F11", "T9", "G3", [(940, 382), (940, 440)]),
        E("F12", "G3", "T10", [(915, 465), (865, 465)], "BUY"),
        E("F13", "G3", "T11", [(965, 465), (1020, 465)], "SELL"),
        E("A6", "T10", "N5", [(800, 433), (800, 411)], "", "assoc"),
        E("A7", "T11", "N6", [(1085, 433), (1085, 411)], "", "assoc"),
        E("F14", "T10", "T12", [(800, 497), (800, 560), (940, 560), (940, 608)]),
        E("F15", "T11", "T12", [(1085, 497), (1085, 560), (940, 560), (940, 608)]),
        E("A8", "T12", "N7", [(1005, 640), (1020, 640)], "", "assoc"),
        E("F16", "T12", "T13", [(940, 672), (940, 738)]),
        E("A9", "T13", "N8", [(1005, 770), (1020, 770)], "", "assoc"),
        E("F17", "T13", "M", [(940, 802), (940, 865)]),
        E("F18", "G2", "M", [(915, 225), (742, 225), (742, 890), (915, 890)], "no: skip"),
        E("F19", "M", "T14", [(940, 915), (940, 945), (1155, 945), (1155, 100), (1185, 100)]),
        E("F20", "T14", "T15", [(1250, 132), (1250, 218)]),
        E("F21", "T15", "T16", [(1250, 282), (1250, 368)]),
        E("F22", "T16", "G4", [(1250, 432), (1250, 505)]),
        E("O1", "T14", "D2", [(1315, 100), (1432, 100)], "", "dataout"),
        E("O2", "T15", "D3", [(1315, 250), (1432, 250)], "", "dataout"),
        E("F23", "G4", "T17", [(1250, 555), (1250, 638)], "no"),
        E("O3", "T17", "D4", [(1315, 670), (1432, 670)], "", "dataout"),
        E("A10", "D4", "N9", [(1450, 721), (1450, 750)], "", "assoc"),
        E("F24", "T17", "End", [(1250, 702), (1250, 760), (1240, 760), (1240, 802)]),
        E("F25", "G4", "T2", [(1275, 530), (1330, 530), (1330, 975), (24, 975), (24, 300), (75, 300)], "yes"),
    ]
    return d
