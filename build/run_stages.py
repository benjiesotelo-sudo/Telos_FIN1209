#!/usr/bin/env python3
"""Really run the example script in its four modes and record what R printed.

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

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "build" / "generated" / "activity2"
RSCRIPT = shutil.which("Rscript") or "/opt/homebrew/bin/Rscript"


import re

SCENARIOS = (
    # name, folder, file, mode, stock, bought date, drop the last row, what it shows
    ("buy_wait", "start", None, "buy", "KO", "2026-08-12", 0),
    ("buy_signal", "update", None, "buy", "F", "2026-08-12", 1),
    ("sell_now", "start", None, "sell", "KO", "2026-08-12", 0),
    ("sell_hold", "update", None, "sell", "KO", "2026-10-12", 0),
    ("buy_update", "update", None, "buy", "KO", "2026-08-12", 0),
)


def settle(script: str, mode: str, stock: str, price: str, date: str) -> str:
    """The script with its four settings lines changed, comments kept."""
    def setv(name, val, s):
        return re.sub(r"^(%s <- )[^#\n]*?(\s*#.*)?$" % name, lambda m: m.group(1) + val + (m.group(2) or ""), s, flags=re.M, count=1)
    for k, v in (("mode", f'"{mode}"'), ("stock", f'"{stock}"'), ("bought_price", price), ("bought_date", f'"{date}"')):
        script = setv(k, v, script)
    return script


def close_on(csv_path: Path, date: str) -> str:
    for ln in csv_path.read_text().splitlines()[1:]:
        f = ln.split(",")
        m, d, y = f[0].split(" ")[0].split("/")
        if f"{y}-{int(m):02d}-{int(d):02d}" == date:
            return f[4]
    raise SystemExit(f"no row for {date}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data", type=Path, required=True)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "modes").mkdir(exist_ok=True)
    script0 = A.SCRIPT_FILE.read_text()
    runs = {}
    for name, folder, _f, mode, stock, date, drop in SCENARIOS:
        with tempfile.TemporaryDirectory() as t:
            work = Path(t)
            shutil.copytree(a.data / folder, work / "data")
            if drop:                                   # the same file, downloaded a day earlier
                p = work / "data" / f"{stock}.csv"
                ls = p.read_text().splitlines()
                p.write_text("\n".join(ls[:-drop]) + "\n")
            price = close_on(a.data / folder / f"{stock}.csv", date) if mode == "sell" else "87.29"
            code = settle(script0, mode, stock, price, date)
            (work / "s.R").write_text(code)
            r = subprocess.run([RSCRIPT, "s.R"], cwd=work, capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                raise SystemExit(f"{name} failed:\n{r.stderr}")
            settings = "\n".join(code.splitlines()[2:6])
            sig = (work / "output" / "signals.csv").read_text().splitlines()
            shutil.copy(work / "output" / f"{stock}.png", OUT / "modes" / f"{name}.png")
            runs[name] = {"mode": mode, "stock": stock, "settings": settings,
                          "answer": (work / "output" / "answer.txt").read_text().rstrip("\n"),
                          "signals": len(sig) - 1, "head": sig[:13], "rows": len(ls) - 1 - drop if drop else None}
    (OUT / "modes.json").write_text(json.dumps(runs, indent=1))
    shutil.copy(OUT / "modes" / "buy_wait.png", OUT / "start-chart.png")
    counts = {}
    # the two "why" charts, drawn by R from the real KO file
    why = OUT / "why"
    why.mkdir(parents=True, exist_ok=True)
    r = subprocess.run([RSCRIPT, str(REPO / "build" / "r" / "explain_osc.R"), str(why), str(a.data / "start" / "KO.csv"), "KO", str(a.data / "start" / "F.csv"), "F"],
                       capture_output=True, text=True, check=True)
    info = {}
    for ln in r.stdout.splitlines():
        w = ln.split()
        if w and w[0] in ("SELL", "BUY"):
            info[w[0].lower()] = {"ticker": w[1], "date": w[2], "entry": w[4], "agree": w[6].split("+")}
        if w and w[0] == "CORR":
            info["corr"] = {"rsi_macd": w[2], "rsi_stoch": w[4], "macd_stoch": w[6]}
    rb = subprocess.run([RSCRIPT, str(REPO / "build" / "r" / "explain_bar.R"), str(why), str(a.data / "start" / "KO.csv"), "KO", str(a.data / "start" / "F.csv"), "F"],
                        capture_output=True, text=True, check=True)
    for ln in rb.stdout.splitlines():
        w = ln.split()
        if w and w[0] == "BAR":
            info["bar"] = {"ticker": w[1], "date": w[2], "side": w[3], "volume": w[5], "avg": w[7]}
    (OUT / "why_info.json").write_text(json.dumps(info))
    for k, v in runs.items():
        print("--", k); print(v["answer"])

if __name__ == "__main__":
    main()
