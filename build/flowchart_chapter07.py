"""The example script's flowchart, as plain data for build/bpmnkit.py.

Every task carries a number; the handout's table ties each number to the lines of
"First Automation FIN1209 - Example Script.R" it stands for.
"""

from bpmnkit import Diagram, Edge, Node

T, X = "task", "xor"


def _t(i, num, cx, cy, *lines):
    return Node(i, T, f"{num}. " + " ".join(lines), cx, cy, (f"{num}. " + lines[0],) + tuple(lines[1:]))


def build() -> Diagram:
    d = Diagram("OopsExample", "Example script: Williams' Oops signals")
    d.nodes = [
        Node("Start", "start", "Run the script", 60, 150, ("Run the script",)),
        _t("T1", 1, 200, 150, "List the CSV files", "in the data folder"),
        Node("G1", X, "Another file left?", 340, 150, ("Another", "file left?"), "aboveleft"),
        _t("T2", 2, 490, 150, "Read the file and", "clean its dates"),
        Node("G2", X, "Another day left?", 490, 330, ("Another day left?",), "belowleft"),
        Node("G3", X, "Gap up, then back to yesterday's high?", 660, 330,
             ("Gap up, then back to", "yesterday's high?"), "above"),
        Node("G4", X, "Gap down, then back to yesterday's low?", 820, 330,
             ("Gap down, then back to", "yesterday's low?"), "above"),
        _t("T3", 3, 660, 450, "Record a SELL signal", "entry = yesterday's high", "stoploss = today's high"),
        _t("T4", 4, 820, 450, "Record a BUY signal", "entry = yesterday's low", "stoploss = today's low"),
        _t("T5", 5, 350, 330, "Draw the chart", "with the signals marked"),
        _t("T6", 6, 200, 330, "Print the answer", "for this stock"),
        _t("T7", 7, 50, 330, "Add its signals", "to the full list"),
        _t("T8", 8, 490, 60, "Write", "output/signals.csv"),
        Node("End", "end", "Signals, charts and answers ready", 640, 60, ("Signals, charts", "and answers ready")),
    ]
    E = lambda i, a, b, pts, lab="": Edge(i, a, b, tuple(pts), lab)
    d.edges = [
        E("F1", "Start", "T1", [(78, 150), (135, 150)]),
        E("F2", "T1", "G1", [(265, 150), (315, 150)]),
        E("F3", "G1", "T2", [(365, 150), (425, 150)], "yes"),
        E("F4", "T2", "G2", [(490, 185), (490, 305)]),
        E("F5", "G2", "G3", [(515, 330), (635, 330)], "yes"),
        E("F6", "G3", "T3", [(660, 355), (660, 415)], "yes"),
        E("F7", "G3", "G4", [(685, 330), (795, 330)], "no"),
        E("F8", "G4", "T4", [(820, 355), (820, 415)], "yes"),
        E("F9", "T3", "G2", [(660, 485), (660, 540), (490, 540), (490, 355)]),
        E("F10", "T4", "G2", [(820, 485), (820, 540), (490, 540), (490, 355)]),
        E("F11", "G4", "G2", [(845, 330), (900, 330), (900, 540), (490, 540), (490, 355)], "no"),
        E("F12", "G2", "T5", [(465, 330), (415, 330)], "no"),
        E("F13", "T5", "T6", [(285, 330), (265, 330)]),
        E("F14", "T6", "T7", [(135, 330), (115, 330)]),
        E("F15", "T7", "G1", [(50, 295), (50, 240), (340, 240), (340, 175)]),
        E("F16", "G1", "T8", [(340, 125), (340, 60), (425, 60)], "no"),
        E("F17", "T8", "End", [(555, 60), (622, 60)]),
    ]
    return d
