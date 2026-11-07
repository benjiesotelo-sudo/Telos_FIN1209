#!/usr/bin/env python3
"""Really run the example script in its four modes and record what R printed.

    .venv/bin/python build/run_stages.py --data DIR

    .venv/bin/python build/run_stages.py --data DIR --year YEARDIR

DIR holds start/ and update/, each with KO.csv and F.csv. The price files are
not in the repository (see chapter-07/activity/README.md), so the build is
given a folder. Writes build/generated/activity2/stage_outputs.json and
counts.json, which the handout reads. Needs Rscript; nothing else.

--year names a folder holding a year of Coca Cola (KO.csv, Google Sheets, from
3 November 2025). The video's opening is one real round trip on it: the file cut
at OPEN_BUY_DAY answers BUY in buy mode, the next day opens above the trigger,
and sell mode, run on the file cut at every later day, answers HOLD until
OPEN_SELL_DAY and SELL now on that day. Every one of those claims is a real run
here, and the build stops if any of them is not what the opening says. Writes
build/generated/activity2/opening.json.
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
    """The script with its four settings lines changed, comments kept except the stock line's, which is rewritten
    to name the stock actually set (the committed script always says "data/KO.csv")."""
    def setv(name, val, s):
        def repl(m):
            head = m.group(1) + val
            if name == "stock":
                return head + " " * max(1, 31 - len(head)) + f"# which file in the data folder: data/{stock}.csv"
            return head + (m.group(2) or "")
        return re.sub(r"^(%s <- )[^#\n]*?(\s*#.*)?$" % name, repl, s, flags=re.M, count=1)
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


OPEN_STOCK, OPEN_BUY_DAY, OPEN_SELL_DAY, OPEN_FROM = "KO", "2026-01-20", "2026-03-02", "2025-12-01"


def _iso(d: str) -> str:
    m, dd, y = d.split(" ")[0].split("/")
    return f"{y}-{int(m):02d}-{int(dd):02d}"


def _rscript(rows: list, stock: str, mode: str, price: str, date: str, chart: Path = None) -> dict:
    """One real run of the committed script on a file of `rows`, with only the four settings changed."""
    with tempfile.TemporaryDirectory() as t:
        work = Path(t)
        (work / "data").mkdir()
        (work / "data" / f"{stock}.csv").write_text("\n".join(rows) + "\n")
        code = settle(A.SCRIPT_FILE.read_text(), mode, stock, price, date)
        (work / "s.R").write_text(code)
        r = subprocess.run([RSCRIPT, "s.R"], cwd=work, capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            raise SystemExit(f"opening run failed:\n{r.stderr}")
        if chart:
            shutil.copy(work / "output" / f"{stock}.png", chart)
        return {"settings": "\n".join(code.splitlines()[2:6]), "stdout": r.stdout.rstrip("\n"), "stderr": r.stderr.rstrip("\n"),
                "answer": (work / "output" / "answer.txt").read_text().rstrip("\n")}


def opening(year: Path) -> dict:
    """The opening's round trip, every step a real run. Stops the build if the data does not say what the opening says."""
    lines = (year / f"{OPEN_STOCK}.csv").read_text().splitlines()
    head, body = lines[0], lines[1:]
    bars = [dict(zip(head.split(","), x.split(","))) for x in body]
    days = [_iso(b["Date"]) for b in bars]
    k = days.index(OPEN_BUY_DAY)
    buy = _rscript([head] + body[:k + 1], OPEN_STOCK, "buy", "87.29", "2026-08-12", OUT / "modes" / "open_buy.png")
    sig = bars[k]
    if buy["answer"] != f"BUY: enter if price trades above {sig['High']}, stop at {sig['Low']}":
        raise SystemExit(f"the opening's buy day no longer answers BUY: {buy['answer']}")
    nxt = bars[k + 1]
    if not float(nxt["Open"]) > float(sig["High"]):
        raise SystemExit("the day after the opening's buy signal did not open above the trigger")
    paid, bought = nxt["Open"], days[k + 1]       # a buy above the trigger fills at that day's open, which was already above it
    holds = []
    sell = None
    for j in range(k + 1, len(body)):
        run = _rscript([head] + body[:j + 1], OPEN_STOCK, "sell", paid, bought)
        if run["answer"].startswith("SELL"):
            sell = (days[j], run)
            break
        if not run["answer"].startswith("HOLD"):
            raise SystemExit(f"unexpected sell mode answer on {days[j]}: {run['answer']}")
        holds.append((days[j], run["answer"]))
    if sell is None or sell[0] != OPEN_SELL_DAY:
        raise SystemExit(f"the opening's sell day is not {OPEN_SELL_DAY}: {sell and sell[0]}")
    s = days.index(OPEN_SELL_DAY)
    sell_run = _rscript([head] + body[:s + 1], OPEN_STOCK, "sell", paid, bought, OUT / "modes" / "open_sell.png")
    if sell_run["answer"] != sell[1]["answer"]:
        raise SystemExit("the opening's sell run is not repeatable")
    lo = days.index(next(d for d in days if d >= OPEN_FROM))
    return {"stock": OPEN_STOCK, "file_first": days[0], "buy_day": OPEN_BUY_DAY, "sell_day": OPEN_SELL_DAY,
            "trigger": sig["High"], "stop": sig["Low"], "bought_day": bought, "paid": paid,
            "sell_stop": bars[k + 1]["Low"], "sell_close": bars[s]["Close"], "buy": buy, "sell": sell_run, "holds": holds,
            "series": [{"date": days[i], **{c: float(bars[i][c]) for c in ("Open", "High", "Low", "Close")}}
                       for i in range(lo, s + 1)]}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--year", type=Path, required=True, help="a year of KO.csv from Google Sheets, for the video's opening")
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
    op = opening(a.year)
    (OUT / "opening.json").write_text(json.dumps(op, indent=1))
    print("-- opening:", op["buy"]["answer"], "|", op["sell"]["answer"].replace("\n", " | "), f"| {len(op['holds'])} HOLD days")
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
