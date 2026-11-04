"""The example script's flowchart, as plain data for build/bpmnkit.py.

Every task carries a number; the handout's table ties each number to the lines of
"First Automation FIN1209 - Example Script.R" it stands for.
"""

from bpmnkit import Diagram, Edge, Node

T, X = "task", "xor"


def _t(i, num, cx, cy, *lines):
    return Node(i, T, f"{num}. " + " ".join(lines), cx, cy, (f"{num}. " + lines[0],) + tuple(lines[1:]))


def build() -> Diagram:
    d = Diagram("OscillatorExample", "Example script: three window oscillators")
    d.nodes = [
        Node("Start", "start", "Run the script", 60, 150, ("Run the script",)),
        _t("T1", 1, 190, 150, "List the CSV files", "in the data folder"),
        Node("G1", X, "Another file left?", 330, 150, ("Another", "file left?"), "aboveleft"),
        _t("T2", 2, 470, 150, "Read the file and", "clean its dates"),
        _t("T3", 3, 620, 150, "Work out the RSI,", "MACD and stochastic"),
        _t("T4", 4, 770, 150, "Find each", "oscillator's crossings"),
        _t("T5", 5, 920, 150, "Add the votes, keep", "the signal days"),
        _t("T6", 6, 920, 300, "Draw the chart with", "the signals marked"),
        _t("T7", 7, 770, 300, "Add its signals", "to the full list"),
        _t("T8", 8, 470, 60, "Write", "output/signals.csv"),
        Node("End", "end", "Signals and charts ready", 620, 60, ("Signals and", "charts ready")),
    ]
    E = lambda i, a, b, pts, lab="": Edge(i, a, b, tuple(pts), lab)
    d.edges = [
        E("F1", "Start", "T1", [(78, 150), (125, 150)]),
        E("F2", "T1", "G1", [(255, 150), (305, 150)]),
        E("F3", "G1", "T2", [(355, 150), (405, 150)], "yes"),
        E("F4", "T2", "T3", [(535, 150), (555, 150)]),
        E("F5", "T3", "T4", [(685, 150), (705, 150)]),
        E("F6", "T4", "T5", [(835, 150), (855, 150)]),
        E("F7", "T5", "T6", [(920, 185), (920, 265)]),
        E("F8", "T6", "T7", [(855, 300), (835, 300)]),
        E("F9", "T7", "G1", [(705, 300), (330, 300), (330, 175)]),
        E("F10", "G1", "T8", [(330, 125), (330, 60), (405, 60)], "no"),
        E("F11", "T8", "End", [(535, 60), (602, 60)]),
    ]
    return d
