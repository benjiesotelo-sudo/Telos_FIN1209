"""The example script's flowchart, as plain data for build/bpmnkit.py.

Four stages (Data in, Measure, Decide, Report), a data object for the input file with its types,
a text annotation on every metric with its rule and settings (and the slide), the agreement count
as its own gateway, the two price rules annotated, data objects for the outputs, and the loop for
the next file. Every task carries a number; the handout's table ties each number to the lines of
"First Automation FIN1209 - Example Script.R" it stands for.
"""

from bpmnkit import Diagram, Edge, Node

T, X = "task", "xor"


def _t(i, num, cx, cy, *lines):
    return Node(i, T, f"{num}. " + " ".join(lines), cx, cy, (f"{num}. " + lines[0],) + tuple(lines[1:]))


def _n(i, cx, cy, w, h, *lines):
    return Node(i, "note", " ".join(lines), cx, cy, tuple(lines), w=w, h=h)


def build() -> Diagram:
    d = Diagram("OscillatorExample", "Example script: three window oscillators")
    G = lambda i, name, x0, x1: Node(i, "group", name, (x0 + x1) / 2, 450, (), w=x1 - x0, h=860)
    d.nodes = [
        G("S1", "Data in", 10, 270), G("S2", "Measure", 280, 700), G("S3", "Decide", 710, 1130), G("S4", "Report", 1140, 1520),
        Node("Start", "start", "Run the script", 140, 80, ("Run the script",)),
        _t("T1", 1, 140, 170, "List the CSV", "files in the", "data folder"),
        _t("T2", 2, 140, 300, "Read each file", "and clean its dates"),
        Node("D1", "data", "data/<ticker>.csv", 140, 430, ("data/<ticker>.csv",), "right"),
        _n("N1", 140, 560, 240, 112, "Input: one CSV file per stock,", "about a year of daily rows.", "Date (a date)",
           "Open, High, Low, Close (prices,", "numbers)", "Volume (a whole number)"),
        _n("N2", 380, 160, 190, 112, "RSI, 14 days (slide 195)", "Equilibrium line: 50", "BUY: crosses above 50",
           "SELL: crosses below 50", "(slide 74)"),
        _t("T3", 3, 590, 160, "Work out the RSI", "and its crossings"),
        _n("N3", 380, 340, 190, 126, "MACD: 12 day EMA minus", "26 day EMA, signal line", "of 9 days (slides 166-168)",
           "BUY: MACD crosses above", "its signal line", "SELL: crosses below it", "(slide 83)"),
        _t("T4", 4, 590, 340, "Work out MACD", "and its crossings"),
        _n("N4", 380, 520, 190, 112, "Stochastic: %K over 14 days,", "%D = 3 day average of %K", "(slides 185, 187)",
           "BUY: %K crosses above %D", "SELL: %K crosses below %D"),
        _t("T5", 5, 590, 520, "Work out the", "stochastic and", "its crossings"),
        _t("T6", 6, 915, 100, "Count how many", "oscillators crossed", "each day"),
        Node("G2", X, "How many of the 3 agree?", 915, 215, ("How many of", "the 3 agree?"), "belowleft"),
        _n("N5", 1052, 215, 140, 60, "agree = oscillators that", "crossed the same way"),
        _t("T7", 7, 915, 330, "Choose BUY or", "SELL by net vote"),
        Node("G3", X, "BUY or SELL?", 915, 440, ("BUY or SELL?",), "below"),
        _n("N6", 778, 355, 134, 62, "BUY price = the", "day's high (Lim's", "trigger, slide 201)"),
        _n("N7", 1060, 355, 160, 62, "SELL price = the close:", "our choice, the slides", "give no sell trigger"),
        _t("T8", 8, 770, 440, "BUY price =", "the day's high"),
        _t("T9", 9, 1060, 440, "SELL price =", "the day's close"),
        _t("T10", 10, 915, 620, "Record the", "signal day: side,", "price, agree"),
        Node("M", X, "", 915, 730, (), "right"),
        _t("T11", 11, 1230, 100, "Draw the chart:", "price + 3", "oscillators"),
        Node("D2", "data", "chart (PNG)", 1420, 100, ("chart", "output/<ticker>.png"), "below"),
        _t("T12", 12, 1230, 240, "Print summary", "for this stock"),
        Node("D3", "data", "console summary", 1420, 240, ("console summary", "(signal days, agree)"), "below"),
        _t("T13", 13, 1230, 380, "Add signals to", "the full list"),
        Node("G4", X, "Another file left?", 1230, 500, ("Another", "file left?"), "aboveleft"),
        _t("T14", 14, 1230, 630, "Write the", "signals table"),
        Node("D4", "data", "signals.csv", 1420, 630, ("signals.csv",), "below"),
        _n("N8", 1395, 745, 250, 74, "ticker, date, side, entry,", "rsi, macd, stoch (BUY, SELL or empty),", "agree (how many agree)"),
        Node("End", "end", "Signals and charts ready", 1230, 750, ("Signals and", "charts ready")),
    ]
    E = lambda i, a, b, pts, lab="", k="flow": Edge(i, a, b, tuple(pts), lab, k)
    d.edges = [
        E("F1", "Start", "T1", [(140, 98), (140, 138)]),
        E("F2", "T1", "T2", [(140, 202), (140, 268)]),
        E("A1", "D1", "T2", [(140, 405), (140, 332)], "", "datain"),
        E("A2", "N1", "D1", [(140, 504), (140, 455)], "", "assoc"),
        E("F3", "T2", "T3", [(205, 300), (245, 300), (245, 55), (590, 55), (590, 128)]),
        E("A3", "T3", "N2", [(525, 160), (475, 160)], "", "assoc"),
        E("F4", "T3", "T4", [(590, 192), (590, 308)]),
        E("A4", "T4", "N3", [(525, 340), (475, 340)], "", "assoc"),
        E("F5", "T4", "T5", [(590, 372), (590, 488)]),
        E("A5", "T5", "N4", [(525, 520), (475, 520)], "", "assoc"),
        E("F6", "T5", "T6", [(655, 520), (680, 520), (680, 100), (850, 100)]),
        E("F7", "T6", "G2", [(915, 132), (915, 190)]),
        E("A6", "G2", "N5", [(940, 215), (982, 215)], "", "assoc"),
        E("F8", "G2", "T7", [(915, 240), (915, 298)], "1, 2 or 3"),
        E("F9", "T7", "G3", [(915, 362), (915, 415)]),
        E("F10", "G3", "T8", [(890, 440), (835, 440)], "BUY"),
        E("F11", "G3", "T9", [(940, 440), (995, 440)], "SELL"),
        E("A7", "T8", "N6", [(770, 408), (770, 386)], "", "assoc"),
        E("A8", "T9", "N7", [(1060, 408), (1060, 386)], "", "assoc"),
        E("F12", "T8", "T10", [(770, 472), (770, 540), (915, 540), (915, 588)]),
        E("F13", "T9", "T10", [(1060, 472), (1060, 540), (915, 540), (915, 588)]),
        E("F14", "G2", "M", [(890, 215), (702, 215), (702, 730), (890, 730)], "none: skip"),
        E("F15", "T10", "M", [(915, 652), (915, 705)]),
        E("F16", "M", "T11", [(915, 755), (915, 815), (1140, 815), (1140, 100), (1165, 100)]),
        E("F17", "T11", "T12", [(1230, 132), (1230, 208)]),
        E("F18", "T12", "T13", [(1230, 272), (1230, 348)]),
        E("F19", "T13", "G4", [(1230, 412), (1230, 475)]),
        E("O1", "T11", "D2", [(1295, 100), (1402, 100)], "", "dataout"),
        E("O2", "T12", "D3", [(1295, 240), (1402, 240)], "", "dataout"),
        E("F20", "G4", "T14", [(1230, 525), (1230, 598)], "no"),
        E("O3", "T14", "D4", [(1295, 630), (1402, 630)], "", "dataout"),
        E("A9", "D4", "N8", [(1420, 681), (1420, 708)], "", "assoc"),
        E("F21", "T14", "End", [(1230, 662), (1230, 732)]),
        E("F22", "G4", "T2", [(1255, 500), (1300, 500), (1300, 880), (24, 880), (24, 300), (75, 300)], "yes"),
    ]
    return d
