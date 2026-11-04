"""The example script's flowchart, as plain data for build/bpmnkit.py.

Every task carries a number; the handout's table ties each number to the
lines of "First Automation FIN1209 - Example Script.R" it stands for.
"""

from bpmnkit import Diagram, Edge, Node

T, X = "task", "xor"


def _t(i, num, cx, cy, *lines):
    return Node(i, T, f"{num}. " + " ".join(lines), cx, cy, (f"{num}. " + lines[0],) + tuple(lines[1:]))


def build() -> Diagram:
    d = Diagram("OopsExample", "Example script: Williams' Oops signals")
    d.nodes = [
        Node("Start", "start", "Run the script", 60, 150, ("Run the script",)),
        _t("T1", 1, 190, 150, "Name the data", "and output folders"),
        _t("T2", 2, 340, 150, "List the CSV files", "in the data folder"),
        Node("G1", X, "Another file left?", 490, 150, ("Another", "file left?"), "aboveleft"),
        _t("T3", 3, 640, 150, "Read the file", "into a table"),
        _t("T4", 4, 790, 150, "Start an empty", "signals table"),
        Node("G2", X, "Another bar left?", 790, 360, ("Another bar left?",), "belowleft"),
        Node("G3", X, "Gap up and price back to the previous high?", 960, 360,
             ("Gap up and back", "to previous high?"), "above"),
        Node("G4", X, "Gap down and price back to the previous low?", 1130, 360,
             ("Gap down and back", "to previous low?"), "above"),
        _t("T5", 5, 960, 470, "Record a SELL signal", "entry = previous high", "stoploss = new high"),
        _t("T6", 6, 1130, 470, "Record a BUY signal", "entry = previous low", "stoploss = new low"),
        _t("T7", 7, 640, 360, "Draw the chart", "and mark the signals"),
        _t("T8", 8, 490, 360, "Add this file's", "signals to the list"),
        _t("T9", 9, 640, 60, "Write", "output/signals.csv"),
        Node("End", "end", "Signals and charts updated", 790, 60, ("Signals and", "charts updated")),
    ]
    E = lambda i, a, b, pts, lab="": Edge(i, a, b, tuple(pts), lab)
    d.edges = [
        E("F1", "Start", "T1", [(78, 150), (125, 150)]),
        E("F2", "T1", "T2", [(255, 150), (275, 150)]),
        E("F3", "T2", "G1", [(405, 150), (465, 150)]),
        E("F4", "G1", "T3", [(515, 150), (575, 150)], "yes"),
        E("F5", "T3", "T4", [(705, 150), (725, 150)]),
        E("F6", "T4", "G2", [(790, 185), (790, 335)]),
        E("F7", "G2", "G3", [(815, 360), (935, 360)], "yes"),
        E("F8", "G3", "T5", [(960, 385), (960, 435)], "yes"),
        E("F9", "G3", "G4", [(985, 360), (1105, 360)], "no"),
        E("F10", "G4", "T6", [(1130, 385), (1130, 435)], "yes"),
        E("F11", "T5", "G2", [(960, 505), (960, 560), (790, 560), (790, 385)]),
        E("F12", "T6", "G2", [(1130, 505), (1130, 560), (790, 560), (790, 385)]),
        E("F13", "G4", "G2", [(1155, 360), (1250, 360), (1250, 560), (790, 560), (790, 385)], "no"),
        E("F14", "G2", "T7", [(765, 360), (705, 360)], "no"),
        E("F15", "T7", "T8", [(575, 360), (555, 360)]),
        E("F16", "T8", "G1", [(490, 325), (490, 175)]),
        E("F17", "G1", "T9", [(490, 125), (490, 60), (575, 60)], "no"),
        E("F18", "T9", "End", [(705, 60), (772, 60)]),
    ]
    return d
