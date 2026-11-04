#!/usr/bin/env python3
"""Really run every stage of the guide's script and record what R printed.

    .venv/bin/python build/run_stages.py --data DIR

DIR holds start/ and update/, each with KO.csv and F.csv. The price files are
not in the repository (see chapter-07/activity/README.md), so the build is
given a folder. Writes build/generated/activity2/stage_outputs.json and
counts.json, which the handout reads. Needs Rscript; nothing else.
"""
import argparse, json, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activity_chapter07 as A  # noqa: E402
from activity_chapter07_code import STAGES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "build" / "generated" / "activity2"
RSCRIPT = shutil.which("Rscript") or "/opt/homebrew/bin/Rscript"


def indexes(csv_path: Path):
    rows = [ln.split(",") for ln in csv_path.read_text().splitlines()[1:]]
    b = [(float(r[1]), float(r[2]), float(r[3])) for r in rows]   # o, h, l
    sell = [i + 1 for i in range(1, len(b)) if b[i][0] > b[i-1][1] and b[i][2] <= b[i-1][1]]
    buy = [i + 1 for i in range(1, len(b)) if b[i][0] < b[i-1][2] and b[i][1] >= b[i-1][2]]
    return sell[0], buy[0]


def run(code: str, work: Path) -> str:
    (work / "stage.R").write_text(code)
    r = subprocess.run([RSCRIPT, "stage.R"], cwd=work, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise SystemExit("stage failed:\n" + code + "\n" + r.stderr)
    return (r.stdout + r.stderr).rstrip("\n")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data", type=Path, required=True)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    sell_i, buy_i = indexes(a.data / "start" / "KO.csv")
    fills = {"SELL_I": sell_i, "BUY_I": buy_i}
    outs = {}
    with tempfile.TemporaryDirectory() as t:
        work = Path(t)
        shutil.copytree(a.data / "start", work / "data")
        for st in STAGES:
            code = A._stage_code(st, fills)
            o = run(code, work)
            outs[st.key] = o
            if st.key in ("plot", "marks"):
                shutil.copy(work / "output" / "KO.png", OUT / f"stage-{st.key}.png")
        # the final stage must print what the committed script prints
    counts = {}
    for phase in ("start", "update"):
        with tempfile.TemporaryDirectory() as t:
            work = Path(t)
            shutil.copytree(a.data / phase, work / "data")
            shutil.copy(A.SCRIPT_FILE, work / "script.R")
            subprocess.run([RSCRIPT, "script.R"], cwd=work, check=True, capture_output=True)
            for ln in (work / "output" / "signals.csv").read_text().splitlines()[1:]:
                k = ln.split(",")[0]
                counts[f"{k}_{phase}"] = counts.get(f"{k}_{phase}", 0) + 1
    (OUT / "stage_outputs.json").write_text(json.dumps(outs, indent=1))
    (OUT / "counts.json").write_text(json.dumps({**counts, **fills}, indent=1))
    print(json.dumps({**counts, **fills}))
    for k in ("variable", "compare", "if", "elseif", "table", "files"):
        print("--", k); print(outs[k][:400])

if __name__ == "__main__":
    main()
