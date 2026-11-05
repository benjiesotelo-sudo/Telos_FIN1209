"""The guide's running script: seven steps, each adding lines to the same script, ending in the example script.

Every stage is a whole script, in the final script's own layout (the file loop is there from step one), and
each runs by itself on the files in data/. A stage is the final script's lines for that step, plus one
throwaway line that prints the step's result (build/explain_chapter07.py lists them). The last stage is the
committed example script itself, so the guide's last step, the file students get and what is typed in the
video cannot differ.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from explain_chapter07 import STEPS, TEMPS

SCRIPT = (Path(__file__).resolve().parent.parent / "chapter-07" / "activity" / "First Automation FIN1209"
          / "First Automation FIN1209 - Example Script.R")

# The final lines (1-based) each step has typed by the end of it. Temps go just before the loop's closing brace.
UPTO = {
    1: [(1, 6), (19, 22)],
    2: [(1, 7), (19, 22), (24, 26)],
    3: [(1, 7), (19, 29)],
    4: [(1, 16), (19, 35)],
    5: [(1, 45), (60, 60)],
    6: [(1, 60)],
}


@dataclass(frozen=True)
class Stage:
    key: str
    title: str
    text: str
    code: str             # the whole script at this step ("" = the final file)
    after: str = ""


def _final() -> list[str]:
    return SCRIPT.read_text(encoding="utf-8").splitlines()


def stage_code(step: int) -> str:
    """Full text of the script after `step` has been typed, with its throwaway print line."""
    F = _final()
    if step == 7:
        return "\n".join(F)
    picked = []
    for a, b in UPTO[step]:
        picked += F[a - 1:b]
    # The loop opens at line 19 and closes at line 62: both are always present from step one.
    out = list(picked)
    if step < 6:
        out.append("  " + TEMPS[step])
    out.append(F[61])                 # line 62, the closing brace of the loop
    if step >= 5:
        out.append(F[62])             # line 63, write.csv after the loop
    return "\n".join(out)


KEYS = ("read", "trend", "bar", "osc", "table", "chart", "files")

STAGES = tuple(
    Stage(KEYS[i - 1], STEPS[i][0], STEPS[i][1], "" if i == 7 else stage_code(i))
    for i in range(1, 8)
)
