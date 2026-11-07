"""The guide video's opening: one real Coca Cola trade, told as a story, drawn frame by frame.

    Should you buy Coca Cola today? -> the prices (the instructor's real Google Sheets recording) -> the script in buy mode
    (BUY, the trigger and the stop) -> the chart -> sell mode every day (HOLD) -> sell mode on the sell day (SELL now) -> the
    chart with the gain -> "your own buy and sell prices, in one click".

Every number, date and printed line comes from build/generated/activity2/opening.json, which build/run_stages.py writes from
real Rscript runs of the committed script and checks (the build stops if the data no longer says what this opening says).
The RStudio window is drawn, not recorded: its editor shows the real settings lines of each run and its Console prints what
that run really printed, verbatim. The chart is purpose made: price only, large, with each mark appearing when the voice
names it. Each caption is its own `say` clip and is shown exactly while it is spoken, in the band below the picture.
"""
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
INFO = HERE / "generated" / "activity2" / "opening.json"
SHEETS = "sheets-2.mp4"           # the second piece of the Sheets recording, in build_video.REC
SHEETS_FROM, SHEETS_TO, SHEETS_SPEED = 2.5, 14.5, 1.7      # the formula typed, then the rows filling in, sped up 1.7 times
PICTURE_DATES_Y = 790             # top of the dates label over the Sheets recording, inside the 1080 px picture
SWITCH = 0.6                     # sell mode: seconds for the stop line to move to the sell stop before the first HOLD
FPS = 20                         # 10240 (the other segments' time base) / 20 is whole, so the joined file keeps exact times
SCRIPT = "First Automation FIN1209 - Example Script.R"
HELV = "/System/Library/Fonts/Helvetica.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"
GREEN, GOLD, INK, RED, BUYC = "#1E5631", "#F2A900", "#222222", "#C62828", "#1B8A3A"

_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen " \
        "eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
_ORD = {1: "first", 2: "second", 3: "third", 5: "fifth", 8: "eighth", 9: "ninth", 12: "twelfth", 20: "twentieth", 30: "thirtieth"}
_MONTHS = "January February March April May June July August September October November December".split()


def words(n: int) -> str:
    if n < 20:
        return _ONES[n]
    t, o = divmod(n, 10)
    return _TENS[t] + ("" if o == 0 else " " + _ONES[o])


def ordinal(n: int) -> str:
    if n in _ORD:
        return _ORD[n]
    t, o = divmod(n, 10)
    if o == 0:
        return _TENS[t][:-1] + "ieth"
    return (_TENS[t] + " " if t >= 2 else "") + (_ORD.get(o) or _ONES[o] + "th") if t >= 2 else _ONES[n] + "th"


def price(p: str) -> tuple:
    """How a price is said and how it is typed: ("seventy one dollars seventy eight", "$71.78")."""
    d, _, c = f"{float(p):.2f}".partition(".")
    return f"{words(int(d))} dollars {words(int(c))}", f"${float(p):.2f}"


def day(iso: str) -> tuple:
    y, m, d = (int(x) for x in iso.split("-"))
    return f"the {ordinal(d)} of {_MONTHS[m - 1]}", f"{d} {_MONTHS[m - 1]}"


def _load() -> dict:
    try:
        return json.loads(INFO.read_text())
    except (OSError, ValueError):
        return {}


O = _load()


def _pct(answer: str) -> str:
    """The gain or loss the script printed, as it printed it ("+11.4%")."""
    import re
    m = re.search(r"[+-]\d+\.\d%", answer)
    if not m:
        raise SystemExit(f"no percent in the opening's sell answer: {answer!r}")
    return m.group(0)


def cues() -> list:
    """(section, id, spoken, shown, pause after). The spoken text is what `say` reads; the shown text is the same words as
    they are typed (prices with $, dates as numbers). Every caption is a whole phrase."""
    if not O:
        return [("q", "q1", "Opening not built yet.", "Opening not built yet.", 0.5)]
    trig, stop, paid = price(O["trigger"]), price(O["stop"]), price(O["paid"])
    sstop, sold = price(O["sell_stop"]), price(O["sell_close"])
    bday, sday = day(O["buy_day"]), day(O["sell_day"])
    y, m, d = O["buy_day"].split("-")
    pct = _pct(O["sell"]["answer"])                       # "+11.4%"
    pw = pct.strip("+%").replace(".", " point ")
    pw = " point ".join(words(int(x)) for x in pw.split(" point "))
    yr = f"twenty {words(int(y) - 2000)}"
    fy = O["file_first"][:4]
    fday, fyr = day(O["file_first"]), f"twenty {words(int(fy) - 2000)}"
    c = [
        ("q", "q1", "Should you buy Coca-Cola today?", None, 0.35),
        ("q", "q2", "And if you do, when should you sell?", None, 0.35),
        ("q", "q3", "In this activity, your own program answers both, from real prices.", None, 0.6),
        ("s", "s1", "First, the prices.", None, 0.25),
        ("s", "s2", "One Google Sheets formula pulls Coca-Cola's daily prices.", None, 0.3),
        ("s", "s3", "You download them as a file, and the program reads it.", None, 0.3),
        ("s", "s4", "This recording pulls July to October twenty twenty six.", "This recording pulls July to October 2026.", 0.25),
        ("s", "s5", f"Our example uses the same formula, from {fday[0]}, {fyr}.",
         f"Our example uses the same formula, from {fday[1]} {fy}.", 0.6),
        ("r", "r1", f"Our file ends on {bday[0]}, {yr}.", f"Our file ends on {bday[1]} {y}.", 0.3),
        ("r", "r2", "Four settings at the top: buy mode, for Coca-Cola.", None, 0.3),
        ("r", "r3", "Then click Source.", None, 1.0),
        ("r", "r4", "The answer is BUY.", None, 0.3),
        ("r", "r5", f"Enter if the price goes above {trig[0]}.", f"Enter if the price goes above {trig[1]}.", 0.3),
        ("r", "r6", f"Stop at {stop[0]}.", f"Stop at {stop[1]}.", 0.6),
        ("c", "c1", "Here is that day on the chart.", None, 0.3),
        ("c", "c2", f"The buy signal, on {bday[0]}.", f"The buy signal, on {bday[1]}.", 0.3),
        ("c", "c3", f"The green line is the trigger, {trig[0]}.", f"The green line is the trigger, {trig[1]}.", 0.3),
        ("c", "c4", f"The red line is the stop, {stop[0]}.", f"The red line is the stop, {stop[1]}.", 0.3),
        ("c", "c5", f"The next day, Coca-Cola opened at {paid[0]}, above the trigger.",
         f"The next day, Coca-Cola opened at {paid[1]}, above the trigger.", 0.3),
        ("c", "c6", f"So you buy there, at {paid[0]}.", f"So you buy there, at {paid[1]}.", 0.4),
        ("c", "c7", "Now you run it again each day, in sell mode.", None, 0.3),
        ("c", "c8", f"Every day it says HOLD, with the stop at {sstop[0]}.", f"Every day it says HOLD, with the stop at {sstop[1]}.", 0.6),
        ("e", "e1", f"On {sday[0]}, you download the file again, and run it.",
         f"On {sday[1]}, you download the file again, and run it.", 0.3),
        ("e", "e2", "Sell mode, the price you paid, and the day you bought.", None, 0.3),
        ("e", "e3", "Then click Source.", None, 1.0),
        ("e", "e4", f"SELL now, at about {sold[0]}.", f"SELL now, at about {sold[1]}.", 0.3),
        ("e", "e5", "The reason: a sell signal that day.", None, 0.6),
        ("g", "g1", f"Back on the chart: the sell, on {sday[0]}.", f"Back on the chart: the sell, on {sday[1]}.", 0.3),
        ("g", "g2", f"Bought at {paid[0]}, sold at about {sold[0]}.", f"Bought at {paid[1]}, sold at about {sold[1]}.", 0.3),
        ("g", "g3", f"A gain of {pw} percent, in about six weeks.", f"A gain of {pct.strip('+')}, in about six weeks.", 0.7),
        ("p", "p1", "That is what you are about to build.", None, 0.3),
        ("p", "p2", "Your own buy and sell prices, in one click.", None, 1.6),
    ]
    return [(s, i, sp, sh or sp, pz) for s, i, sp, sh, pz in c]


def narration() -> str:
    return " ".join(sp for _s, _i, sp, _sh, _p in cues())


# ---------------------------------------------------------------- drawing helpers

def ease(x: float) -> float:
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def ramp(t: float, a: float, dur: float = 0.5) -> float:
    return ease((t - a) / dur) if dur > 0 else float(t >= a)


def lerp(a, b, k):
    if isinstance(a, (tuple, list)):
        return type(a)(lerp(x, y, k) for x, y in zip(a, b))
    return a + (b - a) * k


_FONTS: dict = {}


def font(size: int, bold: bool = False, mono: bool = False):
    from PIL import ImageFont
    k = (size, bold, mono)
    if k not in _FONTS:
        _FONTS[k] = ImageFont.truetype(MENLO if mono else HELV, size, index=0 if mono else (1 if bold else 0))
    return _FONTS[k]


def camera(im, box, W, H):
    """Crop `box` (x0, y0, x1, y1, same aspect as the picture) and fill the picture with it: zooms and drifts."""
    from PIL import Image
    x0, y0, x1, y1 = box
    if (x0, y0, x1, y1) == (0, 0, W, H):
        return im
    return im.transform((W, H), Image.EXTENT, (x0, y0, x1, y1), Image.BICUBIC)


def zoombox(cx, cy, z, W, H):
    w, h = W / z, H / z
    x0 = min(max(0, cx - w / 2), W - w)
    y0 = min(max(0, cy - h / 2), H - h)
    return (x0, y0, x0 + w, y0 + h)


def pointer(d, x, y, s=1.0):
    pts = [(0, 0), (0, 40), (10, 31), (18, 49), (25, 46), (17, 29), (30, 29)]
    pts = [(x + px * s, y + py * s) for px, py in pts]
    d.polygon(pts, fill="#ffffff", outline="#000000", width=3)


def ring(d, x, y, t, t0, color, r0=20, r1=90, dur=0.9, width=8):
    k = (t - t0) / dur
    if 0 <= k <= 1:
        r = r0 + (r1 - r0) * ease(k)
        d.ellipse([x - r, y - r, x + r, y + r], outline=color, width=max(2, int(width * (1 - k)) + 1))


def chip(d, xy, text, f, fill, ink, pad=(26, 14), anchor="lt", radius=18, outline=None):
    x0, y0, x1, y1 = d.textbbox((0, 0), text, font=f)
    w, h = x1 - x0 + 2 * pad[0], y1 - y0 + 2 * pad[1]
    x, y = xy
    if anchor[0] == "m":
        x -= w / 2
    if anchor[0] == "r":
        x -= w
    if anchor[1] == "m":
        y -= h / 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=4 if outline else 0)
    d.text((x + pad[0] - x0, y + pad[1] - y0), text, font=f, fill=ink)
    return (x, y, x + w, y + h)


# ---------------------------------------------------------------- the pictures

class Frames:
    """The real Sheets recording, read forward one frame at a time at the opening's frame rate."""

    def __init__(self, src: Path, ffmpeg: str, W: int, H: int):
        self.w, self.h = 1440, 722
        vf = f"setpts=(PTS-STARTPTS)/{SHEETS_SPEED},fps={FPS}"
        self.p = subprocess.Popen([ffmpeg, "-v", "error", "-ss", f"{SHEETS_FROM}", "-t", f"{SHEETS_TO - SHEETS_FROM}", "-i", str(src),
                                   "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        self.i, self.last, self.done = -1, None, False
        self.count = int((SHEETS_TO - SHEETS_FROM) / SHEETS_SPEED * FPS)

    def get(self, i: int):
        from PIL import Image
        while self.i < i and not self.done:
            b = self.p.stdout.read(self.w * self.h * 3)
            if len(b) < self.w * self.h * 3:
                self.done = True
                break
            self.last = Image.frombytes("RGB", (self.w, self.h), b)
            self.i += 1
        return self.last

    def close(self):
        self.p.stdout.close()
        self.p.wait()


class Opening:
    def __init__(self, T: dict, W: int, H: int, ffmpeg: str, end: float, rec: Path):
        self.T, self.W, self.H, self.end = T, W, H, end
        self.ffmpeg = ffmpeg
        self.series = O["series"]
        self.rec = Frames(rec / SHEETS, ffmpeg, W, H)
        self._chart = None
        y, m, d = (int(v) for v in O["file_first"].split("-"))
        y2, m2, d2 = (int(v) for v in O["buy_day"].split("-"))
        self.formula = f'=GOOGLEFINANCE("NYSE:KO","all",DATE({y},{m},{d}),DATE({y2},{m2},{d2}),"DAILY")'
        self.dates_note = (f"Rows {_short(O['file_first'])} to {_short(O['buy_day'])}. "
                           f"Later the same formula is downloaded again to {_short(O['sell_day'])}.")

    # -- section 1: the question
    def question(self, t):
        from PIL import Image, ImageDraw
        W, H, T = self.W, self.H, self.T
        im = Image.new("RGB", (W, H), GREEN)
        d = ImageDraw.Draw(im)
        cl = [p["Close"] for p in self.series]
        lo, hi = min(cl), max(cl)
        k = ease(t / max(1.0, T["q3"][1]))
        n = max(2, int(len(cl) * k))
        pts = [(80 + i * (W - 160) / (len(cl) - 1), 1030 - (c - lo) / (hi - lo) * 260) for i, c in enumerate(cl[:n])]
        d.line(pts, fill="#3c9a5c", width=12, joint="curve")
        if len(pts) > 1:
            hx, hy = pts[-1]
            d.ellipse([hx - 14, hy - 14, hx + 14, hy + 14], fill=GOLD)
        d.text((80, 60), "FIN1209  ·  First Automation", font=font(38, True), fill="#cfe3d5")
        for cid, y, text, col, size in (("q1", 290, "Should you buy Coca-Cola today?", "#ffffff", 112),
                                        ("q2", 450, "And when should you sell?", GOLD, 112)):
            a = ramp(t, T[cid][0] - 0.1, 0.45)
            if a > 0:
                layer = Image.new("RGBA", (W, 200), (0, 0, 0, 0))
                ImageDraw.Draw(layer).text((W // 2, 100), text, font=font(size, True), fill=col, anchor="mm")
                layer.putalpha(layer.getchannel("A").point(lambda v: int(v * a)))
                im.paste(layer, (0, int(y - 100 + 50 * (1 - a))), layer)
        a = ramp(t, T["q3"][0], 0.4)
        if a > 0:
            s = 0.85 + 0.15 * a
            f = font(int(56 * s), True)
            chip(d, (W // 2, 640), "Your own program answers. From real prices.", f, "#ffffff", GREEN, anchor="mm", pad=(40, 22))
        return camera(im, zoombox(W / 2, H / 2, 1 + 0.04 * ease(t / 8), W, H), W, H)

    # -- section 2: the real Sheets recording
    def sheets(self, t, t0):
        from PIL import Image, ImageDraw
        W, H = self.W, self.H
        i = int((t - t0) * FPS)
        fr = self.rec.get(min(i, self.rec.count - 1))
        src_t = SHEETS_FROM + min(i, self.rec.count - 1) / FPS * SHEETS_SPEED     # where in the recording we are
        typing = (0, 95, 760, 95 + 760 * 9 / 16)
        data = (0, 120, 1100, 120 + 1100 * 9 / 16)
        k = ramp(src_t, 11.6, 1.2)
        box = lerp(typing, data, k)
        hold = max(0.0, t - t0 - self.rec.count / FPS)
        if hold > 0:                                   # the voice is still speaking: keep moving, slowly closer to the rows
            z = 1 + 0.12 * ease(hold / 4) + 0.02 * hold     # and keeps moving for as long as the voice holds it
            cx, cy, bw, bh = 520, 120 + 1100 * 9 / 32, 1100 / z, 1100 * 9 / 16 / z
            box = (max(0, cx - bw / 2), cy - bh / 2, max(0, cx - bw / 2) + bw, cy + bh / 2)
        bw, bh = box[2] - box[0], box[3] - box[1]          # keep the box inside the recording, so no black edge shows
        x0 = min(max(0.0, box[0]), self.rec.w - bw)
        y0 = min(max(0.0, box[1]), self.rec.h - bh)
        box = (x0, y0, x0 + bw, y0 + bh)
        im = fr.transform((W, H), Image.EXTENT, box, Image.BICUBIC)
        d = ImageDraw.Draw(im)
        a = ramp(t, self.T["s4"][0] - 0.2, 0.4)
        if a > 0:                                     # this example's own dates, as text: the recording above has other dates
            fx = self.formula
            bx0, by0, bx1, by1 = 60, PICTURE_DATES_Y, W - 60, PICTURE_DATES_Y + 250
            ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            od = ImageDraw.Draw(ov)
            od.rounded_rectangle([bx0, by0, bx1, by1], radius=22, fill=(30, 86, 49, int(240 * a)), outline=(242, 169, 0, int(255 * a)), width=6)
            od.text((bx0 + 40, by0 + 28), "The same formula, with this example's dates (not recorded):", font=font(38, True),
                    fill=(255, 255, 255, int(255 * a)))
            od.text((bx0 + 40, by0 + 96), fx, font=font(40, mono=True), fill=(255, 226, 122, int(255 * a)))
            od.text((bx0 + 40, by0 + 168), self.dates_note, font=font(32), fill=(220, 236, 225, int(255 * a)))
            im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
            d = ImageDraw.Draw(im)
        chip(d, (W - 40, 30), "Google Sheets: the real recording, sped up", font(34, True), GREEN, "#ffffff", anchor="rt")
        return im

    # -- sections 3 and 5: RStudio, drawn
    def rstudio(self, t, run: str, t0):
        from PIL import Image, ImageDraw
        W, H, T = self.W, self.H, self.T
        im = Image.new("RGB", (W, H), "#dfe5ec")
        d = ImageDraw.Draw(im)
        sell = run == "sell"
        ids = ("e1", "e2", "e3", "e4", "e5") if sell else ("r1", "r2", "r3", "r4", "r5", "r6")
        R = O["sell" if sell else "buy"]
        final = R["settings"].splitlines()
        start = O["buy"]["settings"].splitlines()      # the committed script's own four lines: buy mode, KO
        # menu and toolbar
        d.rectangle([0, 0, W, 46], fill="#f4f6f8")
        x = 24
        for m in "File Edit Code View Plots Session Build Debug Profile Tools Help".split():
            d.text((x, 10), m, font=font(24), fill="#333")
            x += font(24).getlength(m) + 30
        d.text((W - 24, 10), "RStudio (drawn from the real run)", font=font(22), fill="#7a8794", anchor="ra")
        d.rectangle([0, 46, W, 92], fill="#eef1f4")
        d.line([0, 92, W, 92], fill="#c7ced6", width=2)
        # editor
        EX0, EY0, EX1, EY1 = 18, 104, 1350, 600
        d.rectangle([EX0, EY0, EX1, EY1], fill="#ffffff", outline="#c3cbd3", width=2)
        d.rectangle([EX0, EY0, EX1, EY0 + 48], fill="#e9edf1")
        d.rectangle([EX0 + 8, EY0 + 6, EX0 + 760, EY0 + 48], fill="#ffffff", outline="#c3cbd3")
        d.text((EX0 + 24, EY0 + 14), SCRIPT, font=font(24), fill="#222")
        d.rectangle([EX0, EY0 + 48, EX1, EY0 + 98], fill="#f7f8fa")
        d.line([EX0, EY0 + 98, EX1, EY0 + 98], fill="#d5dbe1", width=2)
        click = T[ids[2]][0] + 0.55
        pressed = 0 <= t - click < 0.25
        sx0, sy0, sx1, sy1 = EX1 - 200, EY0 + 56, EX1 - 14, EY0 + 92
        d.text((EX1 - 330, EY0 + 62), "Run", font=font(24), fill="#333")
        d.rounded_rectangle([sx0, sy0, sx1, sy1], radius=6, fill="#c9d6e3" if pressed else "#f7f8fa",
                            outline="#9aa8b6" if t >= T[ids[2]][0] else "#f7f8fa", width=2)
        d.polygon([(sx0 + 16, sy0 + 10), (sx0 + 16, sy1 - 10), (sx0 + 34, (sy0 + sy1) / 2)], fill="#2e7d32")
        d.text((sx0 + 46, sy0 + 5), "Source", font=font(26, True), fill="#222")
        # the code: lines 1 to 8 of the committed script, with the four settings lines of this run
        import activity_chapter07 as A
        code = A.SCRIPT_FILE.read_text().splitlines()[:8]
        # typing: only the value of each changed settings line is retyped; the gap and the comment stay exactly as written
        a0, a1 = T[ids[1]][0], T[ids[1]][1]
        shown, typing_line, cursor_x = settings_at(start, final, t, a0, a1)
        changed = [i for i in range(4) if start[i] != final[i]]
        code[2:6] = shown
        fm, lh = font(30, mono=True), 46
        y = EY0 + 112
        for n, ln in enumerate(code, 1):
            hl = (2 <= n - 1 <= 5) and (a0 <= t < T[ids[2]][0] + 0.3)
            if hl and (n - 3 in changed or not sell):
                d.rectangle([EX0 + 2, y - 4, EX1 - 2, y + lh - 6], fill="#fff2b3")
            d.text((EX0 + 14, y), f"{n:>2}", font=fm, fill="#9aa3ad")
            col = "#5e7d5e" if ln.lstrip().startswith("#") else "#1a1a1a"
            body, _, com = ln.partition("#") if not ln.lstrip().startswith("#") else ("", "", ln[1:])
            xx = EX0 + 82
            if body or not ln.lstrip().startswith("#"):
                d.text((xx, y), body, font=fm, fill="#1a1a1a")
                xx += fm.getlength(body)
                if com:
                    d.text((xx, y), "#" + com, font=fm, fill="#5e8a5e")
            else:
                d.text((xx, y), ln, font=fm, fill=col)
            if typing_line is not None and n - 3 == typing_line and int(t * 2.5) % 2 == 0:
                cx = EX0 + 82 + fm.getlength(cursor_x)
                d.line([cx, y, cx, y + 36], fill="#000", width=3)
            if not sell and n in (3, 4) and a0 <= t < T[ids[2]][0] + 0.3:      # buy mode: box the two values the voice names
                if n == 3 or t >= (a0 + a1) / 2:
                    m = SETTING.match(ln)
                    bx0 = EX0 + 82 + fm.getlength(m.group(1))
                    bx1 = bx0 + fm.getlength(m.group(2))
                    d.rounded_rectangle([bx0 - 6, y - 4, bx1 + 6, y + 40], radius=6, outline=GOLD, width=4)
            y += lh
        # files pane
        FX0, FY0, FX1, FY1 = 1362, 104, W - 18, 600
        d.rectangle([FX0, FY0, FX1, FY1], fill="#ffffff", outline="#c3cbd3", width=2)
        d.rectangle([FX0, FY0, FX1, FY0 + 48], fill="#e9edf1")
        d.text((FX0 + 20, FY0 + 12), "Files", font=font(26, True), fill="#222")
        d.text((FX0 + 110, FY0 + 12), "Plots   Packages   Help", font=font(24), fill="#6a7682")
        ran = t >= click + 0.5
        rows = [("data", True, 0), ("KO.csv", False, 1)]
        if ran:
            rows += [("output", True, 0), ("answer.txt", False, 1), ("KO.png", False, 1), ("signals.csv", False, 1)]
        elif sell:
            rows += [("output", True, 0), ("answer.txt", False, 1), ("KO.png", False, 1), ("signals.csv", False, 1)]
        rows.append((SCRIPT[:26] + "...", False, 0))
        yy = FY0 + 66
        for name, folder, ind in rows:
            xx = FX0 + 24 + 34 * ind
            if folder:
                d.rectangle([xx, yy + 6, xx + 26, yy + 26], fill="#e8b84a")
            else:
                d.rectangle([xx + 3, yy + 2, xx + 23, yy + 28], outline="#8a96a3", width=2)
            d.text((xx + 40, yy), name, font=font(26), fill="#222")
            yy += 46
        last = _short(O["sell_day"] if sell else O["buy_day"])
        a = ramp(t, T[ids[0]][0], 0.4)
        if a > 0:
            b = chip(d, (FX0 + 20, FY0 + 66 + 46 * 2 - 4 + 16 * (1 - a)), f"KO.csv: {_short(O['file_first'])} to {last}",
                     font(26, True), GOLD, INK, pad=(16, 10), radius=10)
            if sell and t < T[ids[0]][1] + 1:
                pass
        # console
        CX0, CY0, CX1, CY1 = 18, 612, W - 18, 1066
        d.rectangle([CX0, CY0, CX1, CY1], fill="#ffffff", outline="#c3cbd3", width=2)
        d.rectangle([CX0, CY0, CX1, CY0 + 48], fill="#e9edf1")
        d.text((CX0 + 20, CY0 + 12), "Console", font=font(26, True), fill="#222")
        d.text((CX0 + 140, CY0 + 12), "Terminal   Background Jobs", font=font(24), fill="#6a7682")
        d.text((CX0 + 520, CY0 + 13), "R 4.6.2  ·  ~/First Automation/", font=font(22), fill="#6a7682")
        fc = font(34, mono=True)
        yy = CY0 + 70
        d.text((CX0 + 20, yy), ">", font=fc, fill="#1f4fb3")
        boxes = []
        if t >= click:
            cmd = f'source("{SCRIPT}")'
            k = min(1.0, (t - click) / 0.35)
            d.text((CX0 + 62, yy), cmd[: int(len(cmd) * k)], font=fc, fill="#1f4fb3")
            yy += 54
            if t >= click + 0.5:
                out = R["stdout"].splitlines() + ([] if not R["stderr"] else R["stderr"].splitlines())
                for ln in out:
                    d.text((CX0 + 20, yy), ln, font=fc, fill="#111")
                    boxes.append((ln, yy))
                    yy += 54
                d.text((CX0 + 20, yy), ">", font=fc, fill="#1f4fb3")
                if int(t * 2.5) % 2 == 0:
                    d.rectangle([CX0 + 62, yy + 4, CX0 + 64 + 18, yy + 42], fill="#1f4fb3")
        # highlight the key parts of the printed answer as the voice names them
        marks = (("SELL now", "e4"), ("80.22", "e4"), ("sell signal on " + O["sell_day"], "e5")) if sell else \
                (("BUY", "r4"), (O["trigger"], "r5"), (O["stop"], "r6"))
        for key, cid in marks:
            if t >= T[cid][0]:
                for ln, by in boxes:
                    if key in ln:
                        x0 = CX0 + 20 + fc.getlength(ln[: ln.index(key)])
                        x1 = x0 + fc.getlength(key)
                        col = RED if (sell and "SELL" in key) or key == O["stop"] else (BUYC if key == "BUY" else GOLD)
                        d.rounded_rectangle([x0 - 8, by - 6, x1 + 8, by + 46], radius=8, outline=col, width=5)
                        ring(d, (x0 + x1) / 2, by + 20, t, T[cid][0], col, 30, 160, 0.8, 7)
                        break
        # the pointer: from the code to Source, a click, then it moves out of the way
        px0, py0 = (900, 330)
        bx, by_ = sx0 + 80, sy0 + 20
        tp = T[ids[2]][0]
        if t < tp:
            k = ease((t - T[ids[1]][0]) / max(0.5, T[ids[1]][1] - T[ids[1]][0]))
            px, py = lerp((1100, 520), (px0, py0), k) if t >= T[ids[1]][0] else (1100 + 30 * math.sin(t), 520)
        elif t < click:
            k = ease((t - tp) / (click - tp))
            px, py = lerp((px0, py0), (bx, by_), k)
        else:
            k = ease((t - click - 0.6) / 0.8)
            px, py = lerp((bx, by_), (1500, 760), k)
        ring(d, bx, by_, t, click, "#1f4fb3", 10, 60, 0.5, 6)
        pointer(d, px, py, 1.1)
        # camera: whole window, then closer on the printed answer
        z = 1 + 0.03 * ease((t - t0) / 6)
        zb = zoombox(W / 2, H / 2, z, W, H)
        if t >= click + 0.6:
            k = ease((t - click - 0.6) / 0.9)
            zz = 1.4
            zz = 1.4 + 0.012 * max(0.0, t - click - 1.5)
            zb = lerp(zb, (0, H - H / zz, W / zz, H), k)
        return camera(im, zb, W, H)

    # -- sections 4 and 6: the chart
    def chart(self, t, phase: str):
        if self._chart is None:
            self._chart = Chart(self)
        return self._chart.draw(t, phase)

    # -- section 7: the payoff
    def payoff(self, t):
        from PIL import Image, ImageDraw
        W, H, T = self.W, self.H, self.T
        im = Image.new("RGB", (W, H), GREEN)
        d = ImageDraw.Draw(im)
        cl = [p["Close"] for p in self.series]
        lo, hi = min(cl), max(cl)
        pts = [(80 + i * (W - 160) / (len(cl) - 1), 1000 - (c - lo) / (hi - lo) * 300) for i, c in enumerate(cl)]
        d.line(pts, fill="#2f7d4a", width=10, joint="curve")
        a = ramp(t, T["p1"][0], 0.4)
        if a > 0:
            d.text((W // 2, 260 + 30 * (1 - a)), "That is what you are about to build", font=font(64, True), fill="#cfe3d5", anchor="mm")
        a = ramp(t, T["p2"][0] - 0.05, 0.45)
        if a > 0:
            s = 0.8 + 0.2 * a
            d.text((W // 2, 470), "Your own buy and sell prices,", font=font(int(112 * s), True), fill="#ffffff", anchor="mm")
            d.text((W // 2, 630), "in one click.", font=font(int(140 * s), True), fill=GOLD, anchor="mm")
        return camera(im, zoombox(W / 2, H / 2, 1 + 0.05 * ease((t - T["p1"][0]) / 5), W, H), W, H)


import re as _re
SETTING = _re.compile(r'^(\w+ <- )(\S+)(\s+#.*)$')     # name <- value   # comment


def settings_at(start: list, final: list, t: float, a0: float, a1: float):
    """The four settings lines as shown at time t while the changed ones are retyped one after another between a0 and a1.
    Only the value changes: each line is the name, the value typed so far, then the line's own gap and comment, unchanged
    (as an editor shows it while you type). Returns (lines, the line being typed or None, the text left of the cursor)."""
    changed = [i for i in range(4) if start[i] != final[i]]
    shown, typing_line, cursor = list(start), None, ""
    if t < a0 or not changed:
        return shown, None, ""
    span = (a1 - a0) / len(changed)
    for j, i in enumerate(changed):
        k = min(1.0, max(0.0, (t - a0 - j * span) / (span * 0.85)))
        if k <= 0:
            continue
        if k >= 1:
            shown[i] = final[i]
            continue
        ms, mf = SETTING.match(start[i]), SETTING.match(final[i])
        if not (ms and mf and ms.group(1) == mf.group(1) and ms.group(3) == mf.group(3)):
            raise SystemExit(f"settings line {i + 3} changes more than its value: {start[i]!r} -> {final[i]!r}")
        value, live = _typed(ms.group(2), mf.group(2), k)
        shown[i] = ms.group(1) + value + ms.group(3)
        if live:
            typing_line, cursor = i, ms.group(1) + value
    return shown, typing_line, cursor


def _common(a: str, b: str):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]:
        j += 1
    return i, j


def _typed(a: str, b: str, k: float):
    """Line `a` turning into line `b` by deleting the differing middle, then typing the new one. Returns (text, live)."""
    if a == b:
        return a, False
    i, j = _common(a, b)
    old, new = a[i:len(a) - j], b[i:len(b) - j]
    steps = len(old) + len(new)
    s = int(round(k * steps))
    if s <= len(old):
        mid = old[: len(old) - s]
    else:
        mid = new[: s - len(old)]
    return a[:i] + mid + a[len(a) - j:], 0 < k < 1


def _short(iso: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {_MONTHS[m - 1][:3]} {y}"


class Chart:
    """The purpose-made opening chart: Coca Cola's daily close only, large, with the trade marked as the voice names it."""

    def __init__(self, op: Opening):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        from datetime import date
        self.op, self.T = op, op.T
        self.W, self.H = op.W, op.H
        self.plt, self.mdates = plt, mdates
        S = op.series
        self.x = [mdates.date2num(date.fromisoformat(p["date"])) for p in S]
        self.c = [p["Close"] for p in S]
        dn = {p["date"]: i for i, p in enumerate(S)}
        self.ib, self.ibought, self.isell = dn[O["buy_day"]], dn[O["bought_day"]], dn[O["sell_day"]]
        self.f = plt.figure(figsize=(self.W / 100, self.H / 100), dpi=100)
        self.ax = self.f.add_axes([0.085, 0.13, 0.885, 0.70])
        ax = self.ax
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        for s in ("left", "bottom"):
            ax.spines[s].set_linewidth(2)
        ax.tick_params(labelsize=26, width=2, length=8)
        ax.set_ylabel("Price (US dollars)", fontsize=30, labelpad=14)
        ax.set_xlabel("Trading day, 2025 to 2026", fontsize=30, labelpad=12)
        ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(nbins=7, steps=[1, 2, 5, 10], integer=True))
        ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("$%.0f"))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
        ax.grid(True, color="#e3e7ea", lw=1.5)
        self.f.text(0.085, 0.93, "Coca-Cola (KO), daily close", fontsize=46, weight="bold", color=GREEN)
        self.f.text(0.085, 0.885, f"Real prices: our Google Sheets file, from {day(O['file_first'])[1]} {O['file_first'][:4]}",
                    fontsize=24, color="#555555")
        self.line, = ax.plot([], [], color="#1f3b57", lw=5, solid_capstyle="round", zorder=3)
        self.head = ax.scatter([], [], s=260, color="#1f3b57", zorder=5)
        self.headlab = ax.text(0, 0, "", fontsize=26, weight="bold", color="#1f3b57", zorder=6,
                               bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1f3b57", lw=2))
        self.trig, = ax.plot([], [], color=BUYC, lw=4, ls=(0, (6, 4)), zorder=2)
        self.triglab = ax.text(0, 0, "", fontsize=28, weight="bold", color=BUYC, va="bottom", ha="right", zorder=6)
        self.stop, = ax.plot([], [], color=RED, lw=4, ls=(0, (6, 4)), zorder=2)
        self.stoplab = ax.text(0, 0, "", fontsize=28, weight="bold", color=RED, va="top", ha="right", zorder=6)
        self.buym = ax.scatter([], [], marker="^", s=1500, color=BUYC, edgecolor="white", lw=3, zorder=7)
        self.buylab = ax.text(0, 0, "", fontsize=30, weight="bold", color=BUYC, ha="center", va="top", zorder=8)
        self.paidm = ax.scatter([], [], marker="o", s=700, color=GOLD, edgecolor=INK, lw=3, zorder=7)
        self.paidlab = ax.text(0, 0, "", fontsize=28, weight="bold", color="#7a5200", zorder=8, ha="right",
                               bbox=dict(boxstyle="round,pad=0.35", fc="#fff4d6", ec=GOLD, lw=2))
        self.paidtie, = ax.plot([], [], color=GOLD, lw=3, zorder=6)
        self.sellm = ax.scatter([], [], marker="v", s=1500, color=RED, edgecolor="white", lw=3, zorder=7)
        self.selllab = ax.text(0, 0, "", fontsize=30, weight="bold", color=RED, ha="right", va="bottom", zorder=8)
        self.hold = self.f.text(0.62, 0.885, "", fontsize=30, weight="bold", color="white", zorder=9,
                                bbox=dict(boxstyle="round,pad=0.45", fc=GREEN, ec=GREEN))
        self.paidline, = ax.plot([], [], color=GOLD, lw=3, ls=(0, (2, 3)), zorder=2)
        self.sellline, = ax.plot([], [], color=RED, lw=3, ls=(0, (2, 3)), zorder=2)
        self.gainbar = None
        self.gaintxt = ax.text(0, 0, "", fontsize=96, weight="bold", color=BUYC, ha="right", va="center", zorder=9)
        self.rings = ax.scatter([], [], s=[], facecolors="none", edgecolors=[], lw=6, zorder=6)
        def view(x0, x1, top_extra=0.12, upto=None):
            ys = [c for xx, c in zip(self.x[:upto], self.c[:upto]) if x0 <= xx <= x1] + [float(O["stop"]), float(O["trigger"])]
            lo, hi = min(ys), max(ys)
            r = hi - lo
            return (x0, x1, lo - 0.36 * r, hi + top_extra * r + 0.4)
        self.views = {
            "all": view(self.x[0] - 2, self.x[self.isell] + 6, 0.35, self.ibought + 1),
            "buy": view(self.x[self.ib] - 16, self.x[self.ib] + 18, 0.35, self.ibought + 1),   # only the days seen so far
            "follow": view(self.x[self.ib] - 12, self.x[self.isell] + 8, 0.2),
            "gain": view(self.x[self.ib] - 12, self.x[self.isell] + 10, 0.22),
        }

    def upto(self, p: float):
        """Draw the close line through whole day int(p), never part of a day, so its end is always a real close."""
        i = max(0, min(len(self.x) - 1, int(math.floor(p + 1e-9))))
        self.line.set_data(self.x[: i + 1], self.c[: i + 1])
        return (self.x[i], self.c[i]), i

    def draw(self, t, phase):
        from PIL import Image
        T, ax = self.T, self.ax
        x, ib, ibo, isl = self.x, self.ib, self.ibought, self.isell
        trig, stop, paid = float(O["trigger"]), float(O["stop"]), float(O["paid"])
        sstop, sold = float(O["sell_stop"]), float(O["sell_close"])
        rings = []
        V = self.views
        hx = None
        if phase == "c":
            # the line draws up to the buy day, then one more day once the next day is named
            p = lerp(0, ib, ease((t - T["c1"][0] + 0.4) / max(1.0, T["c1"][1] - T["c1"][0] + 0.8)))
            if t >= T["c5"][0]:
                p = lerp(ib, ibo, ease((t - T["c5"][0]) / 0.6))
            if t >= T["c7"][0]:       # sell mode: the stop moves first, then one real day at a time, each with its HOLD
                s0 = T["c7"][0] + SWITCH
                p = lerp(ibo, isl - 1, ease((t - s0) / (T["c8"][1] - s0)))
            hx, hi = self.upto(p)
            v = V["all"]
            if t >= T["c3"][0] - 0.3:
                v = lerp(v, V["buy"], ease((t - T["c3"][0] + 0.3) / 0.9))
            if t >= T["c7"][0]:
                v = lerp(V["buy"], V["follow"], ease((t - T["c7"][0]) / 1.2))
        else:
            p = lerp(isl - 1, isl, ease((t - T["g1"][0]) / 0.6))
            hx, hi = self.upto(p)
            v = lerp(V["follow"], V["gain"], ease((t - T["g2"][0]) / 1.2))
            v = lerp(v, (v[0] + 3, v[1] - 0.5, v[2] + 0.2, v[3] - 0.2), ease((t - T["g3"][0]) / 3) * 0.6)
        p0 = T["c1"][0] if phase == "c" else T["g1"][0]
        k = min(0.10, 0.004 * max(0.0, t - p0))
        cx_, cy_ = (v[0] + v[1]) / 2, (v[2] + v[3]) / 2
        v = (cx_ - (cx_ - v[0]) * (1 - k * 0.6), cx_ + (v[1] - cx_) * (1 - k * 0.6),
             cy_ - (cy_ - v[2]) * (1 - k), cy_ + (v[3] - cy_) * (1 - k))
        ax.set_xlim(v[0], v[1])
        ax.set_ylim(v[2], v[3])
        span = v[3] - v[2]
        # the moving head of the line, with its price
        sellmode = phase == "c" and T["c7"][0] <= t
        following = phase == "c" and T["c7"][0] + SWITCH <= t
        headtext = ""
        if following or (phase == "c" and t < T["c2"][0]):
            self.head.set_offsets([hx])
            self.headlab.set_position((hx[0] + 0.6, hx[1] + span * 0.03))
            headtext = f"${self.op.series[hi]['Close']:.2f}"     # that day's own close, from the price file
            self.headlab.set_text(headtext)
        else:
            self.head.set_offsets(self.np_empty())
            self.headlab.set_text("")
        # buy signal
        if t >= T["c2"][0]:
            k = ease((t - T["c2"][0]) / 0.35)
            self.buym.set_offsets([(x[ib], stop - span * 0.05)])
            self.buym.set_sizes([1500 * k])
            self.buylab.set_position((x[ib], stop - span * 0.10))
            self.buylab.set_text(f"BUY signal\n{day(O['buy_day'])[1]}")
            rings.append((x[ib], stop - span * 0.05, T["c2"][0], BUYC))
        else:
            self.buym.set_offsets(self.np_empty()); self.buylab.set_text("")
        # trigger line
        if t >= T["c3"][0]:
            k = ease((t - T["c3"][0]) / 0.8)
            x1 = lerp(x[ib], v[1], k) if phase == "c" and t < T["c7"][0] else v[1]
            self.trig.set_data([x[ib], x1], [trig, trig])
            self.triglab.set_position((v[1] - (v[1] - v[0]) * 0.01, trig + span * 0.012))
            self.triglab.set_text(f"Trigger: enter above ${trig:.2f}")
            if phase == "g" or t >= T["c7"][0]:
                self.triglab.set_text("")
                self.trig.set_data([], [])
        else:
            self.trig.set_data([], []); self.triglab.set_text("")
        # stop line: the signal day's low in buy mode, then the bought day's low in sell mode
        if t >= T["c4"][0]:
            k = ease((t - T["c4"][0]) / 0.8)
            lvl, lab = stop, f"Stop: ${stop:.2f}"
            if phase == "g" or sellmode:            # sell mode's stop, from the moment sell mode starts, before any HOLD
                kk = 1.0 if phase == "g" else ease((t - T["c7"][0]) / (SWITCH * 0.8))
                lvl = lerp(stop, sstop, kk)
                lab = f"Stop in sell mode: ${sstop:.2f}, the low of {day(O['bought_day'])[1]}"
            x1 = lerp(x[ib], v[1], k) if phase == "c" and t < T["c7"][0] else v[1]
            self.stop.set_data([x[ib], x1], [lvl, lvl])
            self.stoplab.set_position((v[1] - (v[1] - v[0]) * 0.01, lvl - span * 0.015))
            self.stoplab.set_text(lab)
        else:
            self.stop.set_data([], []); self.stoplab.set_text("")
        # bought
        if t >= T["c5"][0] + 0.5:
            k = ease((t - T["c5"][0] - 0.5) / 0.35)
            big = t >= T["c6"][0]
            self.paidm.set_offsets([(x[ibo], paid)])
            self.paidm.set_sizes([(700 if big else 380) * k])
            self.paidlab.set_position((x[ibo] - 0.8, paid + span * 0.09))
            self.paidlab.set_text(f"Bought {day(O['bought_day'])[1]}, at ${paid:.2f}" if big else
                                  f"{day(O['bought_day'])[1]}: opened at ${paid:.2f}")
            if sellmode or phase == "g":            # zoomed out: a short label in the empty space below, tied to its mark
                self.paidlab.set_text(f"Bought at ${paid:.2f}")
                lx, ly = x[ibo] + 5.5, stop - span * 0.05
                self.paidlab.set_ha("left"); self.paidlab.set_va("top")
                self.paidlab.set_position((lx, ly))
                self.paidtie.set_data([x[ibo], lx + 0.4], [paid, ly])
            else:
                self.paidlab.set_ha("right"); self.paidlab.set_va("baseline")
                self.paidtie.set_data([], [])
            rings.append((x[ibo], paid, T["c5"][0] + 0.5, GOLD))
            if big:
                rings.append((x[ibo], paid, T["c6"][0], GOLD))

        else:
            self.paidm.set_offsets(self.np_empty()); self.paidlab.set_text(""); self.paidtie.set_data([], [])
        # every day in sell mode: HOLD
        badge = ""
        if following:
            hold = dict(O["holds"]).get(self.op.series[hi]["date"])
            if not hold:
                raise SystemExit(f"no real HOLD answer for {self.op.series[hi]['date']}")
            badge = f"Sell mode, {day(self.op.series[hi]['date'])[1]}:  HOLD"
        self.hold.set_text(badge)
        shown_stop = self.stoplab.get_text()
        self.state = {"day": self.op.series[hi]["date"], "badge": badge, "head": headtext, "end": hx, "stop": shown_stop}
        # the sell and the gain
        if phase == "g":
            k = ease((t - T["g1"][0] - 0.3) / 0.35)
            self.sellm.set_offsets([(x[isl], sold + span * 0.06)])
            self.sellm.set_sizes([1500 * k])
            self.selllab.set_position((x[isl] - 0.8, sold + span * 0.11))
            self.selllab.set_text(f"SELL now, {day(O['sell_day'])[1]}\nat about ${sold:.2f}")
            rings.append((x[isl], sold + span * 0.06, T["g1"][0] + 0.3, RED))
            if t >= T["g2"][0]:
                k2 = ease((t - T["g2"][0]) / 0.8)
                self.paidline.set_data([x[ibo], lerp(x[ibo], x[isl] + 3, k2)], [paid, paid])
                self.sellline.set_data([x[isl] - lerp(0, x[isl] - x[ibo], k2), x[isl] + 3], [sold, sold])
            if t >= T["g3"][0]:
                k3 = ease((t - T["g3"][0]) / 0.5)
                if self.gainbar is None:
                    self.gainbar = ax.annotate("", xy=(x[isl] + 3, sold), xytext=(x[isl] + 3, paid),
                                               arrowprops=dict(arrowstyle="-|>", lw=6, color=BUYC, mutation_scale=50), zorder=9)
                self.gainbar.set_alpha(k3)
                self.gaintxt.set_position((x[isl] + 1.8, paid + (sold - paid) * 0.38))
                self.gaintxt.set_text(_pct(O["sell"]["answer"]))
                self.gaintxt.set_alpha(k3)
                self.gaintxt.set_fontsize(60 + 40 * k3)
        else:
            self.sellm.set_offsets(self.np_empty()); self.selllab.set_text("")
            self.paidline.set_data([], []); self.sellline.set_data([], [])
        focus = None
        if phase == "g":
            focus = (x[isl], sold + span * 0.06, T["g1"][0] + 0.3, RED)
        elif T["c2"][0] <= t < T["c5"][0]:
            focus = (x[ib], stop - span * 0.05, T["c2"][0], BUYC)
        elif T["c5"][0] + 0.5 <= t < T["c7"][0]:
            focus = (x[ibo], paid, T["c5"][0] + 0.5, GOLD)
        if focus:
            fx, fy, f0, fc = focus
            n = int((t - f0) / 1.5)
            if n >= 1:
                rings.append((fx, fy, f0 + 1.5 * n, fc))
        live = [(rx, ry, c) for rx, ry, t0, c in rings if 0 <= t - t0 <= 0.9]
        if live:
            self.rings.set_offsets([(rx, ry) for rx, ry, _ in live])
            ks = [(t - t0) / 0.9 for _rx, _ry, t0, _c in rings if 0 <= t - t0 <= 0.9]
            self.rings.set_sizes([2000 + 9000 * ease(k) for k in ks])
            self.rings.set_edgecolors([_rgba(c, 1 - k) for (_x, _y, c), k in zip(live, ks)])
        else:
            self.rings.set_offsets(self.np_empty())
        self.f.canvas.draw()
        buf = self.f.canvas.buffer_rgba()
        im = Image.frombuffer("RGBA", self.f.canvas.get_width_height(), buf, "raw", "RGBA", 0, 1).convert("RGB")
        return im

    @staticmethod
    def np_empty():
        import numpy as np
        return np.empty((0, 2))


def _rgba(hexc: str, a: float):
    h = hexc.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)) + (max(0.0, min(1.0, a)),)


# ---------------------------------------------------------------- sound

def music(seconds: float, sr: int = 44100):
    """Quiet, plain background music made here from sine tones (no download): a I vi IV V progression in C with a soft
    pad, a low bass and a gentle eighth-note arpeggio, faded in and out. Returns a float array in -1..1."""
    import numpy as np
    n = int(seconds * sr)
    t = np.arange(n) / sr
    bar = 2.4
    prog = [(261.63, 329.63, 392.00), (220.00, 261.63, 329.63), (174.61, 220.00, 261.63), (196.00, 246.94, 293.66)]
    out = np.zeros(n)
    nb = int(math.ceil(seconds / bar)) + 1
    for b in range(nb):
        ch = prog[b % 4]
        a, z = int(b * bar * sr), int(min(n, (b + 1) * bar * sr + 0.6 * sr))
        if a >= n:
            break
        tt = t[a:z] - b * bar
        env = np.minimum(1, tt / 0.45) * np.clip((bar + 0.6 - tt) / 0.6, 0, 1)
        for f in ch:
            out[a:z] += 0.16 * env * (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt))
        out[a:z] += 0.22 * env * np.sin(2 * np.pi * ch[0] / 2 * tt)
        arp = [ch[0] * 2, ch[1] * 2, ch[2] * 2, ch[1] * 2]
        for s in range(8):
            a2 = a + int(s * bar / 8 * sr)
            z2 = min(n, a2 + int(0.6 * sr))
            if a2 >= n:
                break
            u = t[a2:z2] - t[a2]
            f = arp[s % 4]
            out[a2:z2] += 0.12 * np.exp(-u * 6) * np.minimum(1, u / 0.01) * (np.sin(2 * np.pi * f * u) + 0.1 * np.sin(6 * np.pi * f * u))
    fade = np.minimum(1, t / 1.0) * np.clip((seconds - t) / 1.8, 0, 1)
    out *= fade
    return out / (np.abs(out).max() + 1e-9)


# ---------------------------------------------------------------- the build

def build(tmp: Path, n: int, voice: str, say_clip, probe, sub_image, W: int, PICTURE_H: int, H: int, ffmpeg: str, rec: Path):
    """Render the opening to one segment. Returns (segment, [(start, end, caption)])."""
    import numpy as np
    from PIL import Image
    if not O:
        raise SystemExit("build/generated/activity2/opening.json is missing: run build/run_stages.py --data ... --year ...")
    cl = cues()
    # 1. the voice, one clip per caption, and the timeline from the clips' real lengths
    T, caps, clips, at = {}, [], [], 0.5
    sec_start = {}
    for s, cid, sp, sh, pz in cl:
        if s not in sec_start:
            sec_start[s] = at
        f = say_clip(sp, voice)
        d = probe(f)
        T[cid] = (at, at + d)
        caps.append((at, at + d, sh))
        clips.append((at, f))
        at += d + pz
        if s == "s" and cid == "s5":           # the Sheets recording plays for its whole length before the next section
            at = max(at, sec_start["s"] + (SHEETS_TO - SHEETS_FROM) / SHEETS_SPEED + 0.4)
    end = at
    order = ["q", "s", "r", "c", "e", "g", "p"]
    first = {s: min(T[c][0] for ss, c, *_ in cl if ss == s) for s in order}
    last = {s: max(T[c][1] for ss, c, *_ in cl if ss == s) for s in order}
    bounds = {}
    for a, b in zip(order, order[1:]):
        bounds[b] = (last[a] + first[b]) / 2
    sr = 44100
    total = int(round(end * FPS)) / FPS
    N = int(round(total * sr))
    vo = np.zeros(N)
    for t0, f in clips:
        raw = subprocess.run([ffmpeg, "-v", "error", "-i", str(f), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"],
                             capture_output=True, check=True).stdout
        x = np.frombuffer(raw, dtype=np.float32).astype(float)
        a = int(t0 * sr)
        vo[a:a + len(x)] += x[: max(0, N - a)]
    m = music(total, sr)
    speech = np.abs(vo) > 0.01
    rms_v = math.sqrt(float(np.mean(vo[speech] ** 2))) if speech.any() else 0.1
    env = np.convolve(speech.astype(float), np.ones(int(0.25 * sr)) / int(0.25 * sr), mode="same")
    duck = 1 - 0.45 * np.clip(env * 3, 0, 1)
    gain = rms_v * 10 ** (-17 / 20) / (math.sqrt(float(np.mean(m ** 2))) + 1e-9)
    mix = vo + m * gain * duck
    peak = float(np.abs(mix).max())
    if peak > 0.98:
        mix *= 0.98 / peak
    wav = tmp / f"{n:03d}_open.wav"
    import wave
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
    levels = {"voice_rms_db": round(20 * math.log10(rms_v), 1),
              "music_rms_db": round(20 * math.log10(math.sqrt(float(np.mean((m * gain * duck) ** 2))) + 1e-12), 1),
              "peak": round(min(peak, 0.98), 3)}
    # 2. the captions, drawn once each, the same strip as every other scene, in the band below the picture
    capims = []
    for k, (a, b, text) in enumerate(caps):
        png = tmp / f"{n:03d}_oc{k}.png"
        sub_image(text, png)
        band = Image.open(png).convert("RGBA").crop((0, PICTURE_H, W, H))
        capims.append((a, b, band))
    # 3. the frames
    if not (rec / SHEETS).is_file():
        raise SystemExit(f"missing recording {rec / SHEETS}")
    op = Opening(T, W, PICTURE_H, ffmpeg, end, rec)

    def picture(sec: str, t: float):
        if sec == "q":
            return op.question(t)
        if sec == "s":
            return op.sheets(t, bounds["s"])
        if sec == "r":
            return op.rstudio(t, "buy", bounds["r"])
        if sec == "e":
            return op.rstudio(t, "sell", bounds["e"])
        if sec == "c":
            return op.chart(t, "c")
        if sec == "g":
            return op.chart(t, "g")
        return op.payoff(t)

    seg = tmp / f"{n:03d}.mp4"
    enc = subprocess.Popen([ffmpeg, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
                            "-video_track_timescale", "10240", "-c:a", "aac", "-b:a", "128k", "-ar", str(sr), "-ac", "1",
                            "-shortest", str(seg)], stdin=subprocess.PIPE)
    XF = 0.35
    frames = int(round(total * FPS))
    for i in range(frames):
        t = i / FPS
        sec = order[0]
        for s in order[1:]:
            if t >= bounds[s]:
                sec = s
        im = picture(sec, t)
        nxt = next((s for s in order[1:] if 0 <= bounds[s] - t < XF / 2), None)
        prv = next((s for s in order[1:] if 0 <= t - bounds[s] < XF / 2), None)
        if prv is not None and prv == sec:                 # just after a cut: fade in from the last picture of the section before
            k = 0.5 + (t - bounds[prv]) / XF
            before = order[order.index(prv) - 1]
            im = Image.blend(picture(before, bounds[prv] - 1e-3), im, min(1.0, k))
        elif nxt is not None:
            k = 0.5 - (bounds[nxt] - t) / XF
            im = Image.blend(im, picture(nxt, bounds[nxt]), max(0.0, k))
        frame = Image.new("RGB", (W, H), "#FFFFFF")
        frame.paste(im, (0, 0))
        for a, b, band in capims:
            if a <= t <= b:
                frame.paste(band, (0, PICTURE_H), band)
        enc.stdin.write(frame.tobytes())
    enc.stdin.close()
    if enc.wait() != 0:
        raise SystemExit("encoding the opening failed")
    op.rec.close()
    (tmp / "opening_timeline.json").write_text(json.dumps({"T": T, "bounds": bounds, "end": total, "levels": levels}, indent=1))
    print("opening:", f"{total:.1f}s", levels, flush=True)
    return seg, [(a, b, text) for a, b, text in caps]
