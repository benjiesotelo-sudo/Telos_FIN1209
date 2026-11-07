#!/usr/bin/env python3
"""Make the narration script, and the computer-voice walkthrough video.

    .venv/bin/python build/build_video.py --narration-only
    .venv/bin/python build/build_video.py --video-out <path .mp4>

The narration script (a Markdown file in the student folder) is written from
build/video_chapter07.py, the same scenes the video speaks. The video is made
with macOS `say` and ffmpeg and is too large for git, so it is written to a
path outside the repository. Pass --screens for the folder of screenshots.
"""
import argparse, hashlib, html, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activity_chapter07 as A  # noqa: E402
import chrome  # noqa: E402
from video_chapter07 import SCENES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SCREENS = REPO / "chapter-07" / "activity" / "screens"
GEN = REPO / "build" / "generated" / "activity2"
WEB = REPO / "build" / "generated" / "video" / "web"
SAYCACHE = REPO / "build" / "generated" / "video" / "saycache"
import os
REC = Path(os.environ.get("FM_REC") or "/Users/benjie/.treehouse/benjie-agent-workspace-8bf1b0/1/benjie-agent-workspace/data/fin1209-activity2/rec")
HANDOUT = A.STUDENT / f"{A.NAME}.pdf"
NARRATION = A.STUDENT / f"{A.NAME} - Narration Script.md"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
W, PICTURE_H = 1920, 1080        # PICTURE_H is the picture area every generator still draws into, unchanged
TIMES = REPO / "build" / "video_times.json"        # the real start of each version in the finished video
MARKS = {}                       # no skip popups in v6: one walkthrough, not a long and a short form


def load_times():
    try:
        return json.loads(TIMES.read_text())
    except (OSError, ValueError):
        return None


def mmss(sec: int) -> str:
    return f"{sec // 60}:{sec % 60:02d}"


def spoken(sec: int) -> str:
    m, r = divmod(sec, 60)
    return f"{m} minute{'s' * (m != 1)} {r} second{'s' * (r != 1)}"


def resolve(text: str, times) -> str:
    """Fill {T_*} (on screen) and {S_*} (spoken) from the video's real times; mm:ss until they are known."""
    for k in ("short", "out", "long"):
        v = None if times is None else times.get(k)
        text = text.replace("{T_%s}" % k.upper(), mmss(v) if v is not None else "mm:ss")
        text = text.replace("{S_%s}" % k.upper(), spoken(v) if v is not None else "the time shown on screen")
    return text


SUBH = 230                      # the canvas is enlarged by this much below the unchanged picture area, for the
                                 # subtitle alone, sized for the worst case measured from the real narration: two
                                 # wrapped rows at up to 210px (build/README.md)
H = PICTURE_H + SUBH             # the real frame height: the picture on top, the subtitle strip below it, never over it
FONT = "/System/Library/Fonts/Helvetica.ttc"
DISPLAY = (                     # how a spoken word is written in the subtitle: the same words, as you would type them
    ("R S I", "RSI"), ("M A C D", "MACD"), ("T T R", "TTR"), ("S M A", "SMA"), ("N Y S E", "NYSE"), ("B P M N", "BPMN"),
    ("B U Y", "BUY"), ("S E L L", "SELL"), ("K O dot csv", "KO.csv"), ("K O", "KO"), ("read dot csv", "read.csv"),
    ("Read dot csv", "Read.csv"), ("list dot files", "list.files"), ("List dot files", "List.files"),
    ("as dot Date", "as.Date"), ("As dot Date", "As.Date"), ("data dot frame", "data.frame"), ("Data dot frame", "Data.frame"),
    ("dev dot off", "dev.off"), ("Dev dot off", "Dev.off"), ("write dot csv", "write.csv"), ("Write dot csv", "Write.csv"),
    ("signals dot csv", "signals.csv"), ("install dot packages", "install.packages"), ("sheets dot new", "sheets.new"),
    ("dot csv", ".csv"), ("dot bpmn", ".bpmn"), ("dot R", ".R"), ("underscore", "_"), ("P D F", "PDF"),
    ("percent K", "%K"), ("percent D", "%D"), ("answer dot text", "answer.txt"), ("N A", "NA"), ("P L dot", "PLdot"),
)


def display(text: str) -> str:
    for a, b in DISPLAY:
        text = text.replace(a, b)
    return text


def sentences(text: str) -> list:
    return [x for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x]


def _protect(text: str) -> str:
    """Join the words of a spoken phrase from DISPLAY with NUL so a chunk boundary never falls inside one
    (so "R S I" is never cut to "R S" | "I")."""
    for spoken, _ in DISPLAY:
        if " " in spoken:
            text = text.replace(spoken, spoken.replace(" ", "\x00"))
    return text


def cue_chunks(sentence: str, limit: int = 78) -> list:
    """The sentence's own words, cut into chunks of at most two display rows each. Each chunk is returned as
    its own spoken text (what `say` should read), so every chunk can be synthesised and timed on its own real
    clip rather than a guess split from the whole sentence's duration."""
    words, out, cur = _protect(sentence).split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if cur and len(display(cand.replace("\x00", " "))) > limit:
            out.append(cur); cur = w
        else:
            cur = cand
    if cur:
        out.append(cur)
    return [c.replace("\x00", " ") for c in out]


def sub_image(text: str, path: Path) -> None:
    """One subtitle: a dark strip at the bottom with the words in large white type, at most two rows."""
    from PIL import Image, ImageDraw, ImageFont
    f = ImageFont.truetype(FONT, 60)
    d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    rows, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d0.textlength(t, font=f) > W - 160 and cur:
            rows.append(cur); cur = w
        else:
            cur = t
    rows.append(cur)
    if len(rows) > 2:        # SUBH is sized for two rows (build/README.md); a third would dip into the picture
        raise SystemExit(f"subtitle needs {len(rows)} rows, more than SUBH allows: {text!r}")
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    h = 80 * len(rows) + 30
    d.rectangle([0, H - h - 20, W, H], fill=(0, 0, 0, 215))
    for i, r in enumerate(rows):
        d.text((W // 2, H - h - 20 + 15 + 40 + 80 * i), r, font=f, fill=(255, 255, 255, 255), anchor="mm")
    im.save(path)


def banner(path: Path, text: str) -> None:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 64)
    x0, y0, x1, y1 = d.textbbox((0, 0), text, font=f)
    w, h = x1 - x0, y1 - y0
    cx, cy = W // 2, 120
    d.rounded_rectangle([cx - w // 2 - 50, cy - h // 2 - 38, cx + w // 2 + 50, cy + h // 2 + 38], radius=26,
                        fill="#F2A900", outline="#1E5631", width=8)
    d.text((cx, cy), text, font=f, fill="#222222", anchor="mm")
    im.save(path)


def write_narration(times=None) -> None:
    out = [f"# {A.NAME}: narration script", "",
           "Read this over the video's pictures, one "
           "section per picture, in the order of the video. Say the words in "
           "your own voice and change anything that is not how you talk.", ""]
    for n, s in enumerate(SCENES, 1):
        pic = {"card": "a title card", "block": f"the labelled block {s.ref} of the script", "walk": f"line {s.ref} of the script, highlighted", "run": f"the settings and the real printed answer ({s.ref})", "shot": f"screenshot `{s.ref}`", "web": "a capture of a public web page",
               "page": "the handout page: " + s.ref, "code": f"the code of R step {s.ref}", "frame": f"the last frame of {s.ref}", "code": f"the code of R step {s.ref}", "gen": f"an image R drew ({s.ref})", "clip": f"a screen recording ({s.ref})",
               "opening": "the animated opening: the question, the real Google Sheets recording, RStudio drawn from the real runs "
                          "(buy mode, then sell mode), and the trade on a price chart"}[s.kind]
        pic = "Picture: " + pic
        out += [f"## {n}. {s.title}", "", f"*{pic}*", "", resolve(s.say, times), ""]
        if s.popup:
            out[-3:-3] = [f"*On screen: {resolve(s.popup, times)}*", ""]
    NARRATION.write_text("\n".join(out), encoding="utf-8")
    print("wrote", NARRATION.name)


def card(scene, path: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 24], fill="#1E5631")
    d.rectangle([0, 24, W, 36], fill="#F2A900")
    f1 = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 92)
    f2 = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 54)
    y = 330
    for i, t in enumerate(scene.card):
        d.text((W // 2, y), t, font=f1 if i == 0 else f2, fill="#1E5631" if i == 0 else "#222222", anchor="mm")
        y += 150 if i == 0 else 90
    im.save(path)


def fit(src: Path, path: Path, label: str = "") -> None:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.open(src).convert("RGB")
    top = 70 if label else 0
    k = min(W / im.width, (PICTURE_H - top) / im.height)
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    bg = Image.new("RGB", (W, H), "#FFFFFF")
    bg.paste(im, ((W - im.width) // 2, top + (PICTURE_H - top - im.height) // 2))
    if label:
        d = ImageDraw.Draw(bg)
        f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        d.rectangle([0, 0, W, 64], fill="#F2A900")
        d.text((W // 2, 32), label, font=f, fill="#222222", anchor="mm")
    bg.save(path)


def page_images(marker: str, crop, out: Path, cache: dict) -> list:
    from PIL import Image
    if "pages" not in cache:
        n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(HANDOUT)], capture_output=True, text=True).stdout).group(1))
        cache["pages"] = [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(HANDOUT), "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]
    hits = [i for i, t in enumerate(cache["pages"], 1) if marker in t]
    if not hits:
        raise SystemExit(f"no handout page contains {marker!r}")
    pg = hits[0] if not marker.startswith("Which lines") else hits[0]
    base = out.parent / f"page{pg}.png"
    if not base.exists():
        subprocess.run(["pdftoppm", "-r", "220", "-png", "-singlefile", "-f", str(pg), "-l", str(pg), str(HANDOUT), str(base.with_suffix(""))], check=True)
    full = Image.open(base).convert("RGB")
    w, h = full.size
    import math
    n = max(1, math.ceil((crop[1] - crop[0]) / 0.36))
    step = (crop[1] - crop[0]) / n
    outs = []
    for k in range(n):
        a = crop[0] + k * step
        b = min(1.0, a + step + 0.02)
        im = full.crop((int(w * 0.04), int(h * a), int(w * 0.96), int(h * b)))
        sc = min(W / im.width, PICTURE_H / im.height)
        im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        bg = Image.new("RGB", (W, H), "#FFFFFF"); bg.paste(im, ((W - im.width) // 2, (PICTURE_H - im.height) // 2))
        f = out.with_name(out.stem + f"_{k}.png"); bg.save(f); outs.append(f)
    return outs


def _probe(path: Path) -> float:
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                capture_output=True, text=True).stdout)


def say_clip(chunk: str, voice: str) -> Path:
    """The cached `say` clip of one caption chunk (speech is kept per chunk, so a stalled or repeated build resumes)."""
    key = hashlib.sha1(f"{voice}|165|{chunk}".encode()).hexdigest()[:20]
    cached = SAYCACHE / f"{key}.aiff"
    if not cached.is_file():
        SAYCACHE.mkdir(parents=True, exist_ok=True)
        for attempt in range(4):
            try:
                subprocess.run(["say", "-v", voice, "-r", "165", "-o", str(cached) + ".part", chunk], check=True, timeout=120)
                break
            except subprocess.TimeoutExpired:
                print("say stalled on one chunk; trying again", flush=True)
        else:
            raise SystemExit("the speech synthesiser kept stalling")
        Path(str(cached) + ".part").rename(cached)
    return cached


def speak(t: Path, n: int, text: str, voice: str):
    """The scene's speech, one subtitle chunk at a time: each chunk is its own `say` clip, so its cue's start and
    end are exactly that clip's own ffprobe duration, never a share of a longer sentence guessed by character count.
    Returns (audio file, [(start, end, words)] relative to the start of the audio, audio length)."""
    parts, cues, at, gap = [], [], 0.0, 0.18
    i = 0
    for sen in sentences(text):
        for chunk in cue_chunks(sen):
            i += 1
            f = t / f"{n:03d}_s{i}.aiff"
            shutil.copy(say_clip(chunk, voice), f)
            d = _probe(f)
            cues.append((at, at + d, display(chunk)))
            parts.append(f); at += d + gap
    out = t / f"{n:03d}.wav"
    ins = []
    for f in parts:
        ins += ["-i", str(f)]
    chain = "".join(f"[{k}:a]aresample=44100,apad=pad_dur={gap}[a{k}];" for k in range(len(parts)))
    chain += "".join(f"[a{k}]" for k in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[o]"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", *ins, "-filter_complex", chain, "-map", "[o]", str(out)], check=True)
    return out, cues, at


def burn(t: Path, n: int, video: Path, cues: list) -> Path:
    """Draw the subtitles onto a segment: one transparent strip per cue, shown only while it is spoken."""
    if not cues:
        return video
    ins, chain, last = [], "", "[0:v]"
    for k, (a, b, text) in enumerate(cues, 1):
        png = t / f"{n:03d}_c{k}.png"
        sub_image(text, png)
        ins += ["-loop", "1", "-t", f"{b + 1:.3f}", "-i", str(png)]
        nxt = f"[v{k}]"
        chain += f"{last}[{k}:v]overlay=enable='between(t,{a:.3f},{b:.3f})'{nxt};"
        last = nxt
    out = t / f"{n:03d}_sub.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(video), *ins, "-filter_complex", chain.rstrip(";"), "-map", last,
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "10", str(out)], check=True)
    return out


def _shoot_content(doc: str, path: Path) -> None:
    """Screenshot an HTML page sized to the unchanged picture area, then pad it onto the enlarged frame so the
    SUBH strip below it stays blank, left for the subtitle, never drawn into."""
    from PIL import Image
    h = path.with_suffix(".html"); h.write_text(doc)
    subprocess.run([str(chrome.CHROME), "--headless", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{PICTURE_H}",
                    f"--screenshot={path}", h.as_uri()], check=True, capture_output=True)
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", (W, H), "#FFFFFF")
    bg.paste(im, (0, 0))
    bg.save(path)


def _script_view(path: Path, title: str, lo: int, hi: int, hl=None, key=None, cap: int = 17, note: str = "") -> None:
    """A block of the committed script drawn large: the line `hl` highlighted whole, and its key part boxed when `key` is given."""
    import walk_chapter07 as WK
    lines = WK.script_lines()
    start, end = lo, hi
    if hi - lo + 1 > cap:
        c = hl or lo
        start = max(lo, min(c - cap // 2, hi - cap + 1)); end = min(hi, start + cap - 1)
    rows = []
    for n in range(start, end + 1):
        ln = lines[n - 1]
        esc = html.escape(ln) or "&nbsp;"
        if n == hl and key and html.escape(key) in esc:
            esc = esc.replace(html.escape(key), f'<mark>{html.escape(key)}</mark>', 1)
        rows.append(f'<div class="l {"hl" if n == hl else ""}"><span class="n">{n}</span><span>{esc}</span></div>')
    up = '<div class="m">... lines above not shown</div>' if start > lo else ""
    dn = '<div class="m">... lines below not shown</div>' if end < hi else ""
    doc = f"""<!doctype html><meta charset=utf-8><style>
    body{{margin:0;width:{W}px;height:{PICTURE_H}px;background:#fff;font-family:Helvetica,Arial,sans-serif;overflow:hidden}}
    .bar{{height:24px;background:#1E5631;border-bottom:12px solid #F2A900}}
    h1{{font-size:46px;color:#1E5631;margin:22px 50px 4px;font-weight:600}}
    .note{{font-size:28px;color:#555;margin:0 50px 12px}}
    .code{{margin:0 50px;border:2px solid #cfd8d1;border-radius:10px;padding:10px 0;font:25px/1.42 Menlo,monospace}}
    .l{{display:flex;padding:0 16px;white-space:pre-wrap;word-break:break-all}} .n{{width:56px;color:#889;text-align:right;margin-right:20px;flex:none}}
    .hl{{background:#ffe27a;border-left:12px solid #F2A900;padding-left:4px}}
    mark{{background:#ffb300;outline:4px solid #8a5a00;border-radius:4px;padding:0 2px}}
    .m{{padding:0 16px;color:#889;font:italic 22px Helvetica}}
    </style><div class=bar></div><h1>{html.escape(title)}</h1><div class=note>{html.escape(note)}</div>
    <div class=code>{up}{''.join(rows)}{dn}</div>"""
    _shoot_content(doc, path)


def block_image(ref: str, path: Path) -> None:
    import walk_chapter07 as WK
    k = int(ref[1:])
    for kk, title, purpose, a, b, rows in WK.blocks():
        if kk == k:
            _script_view(path, f"Block {k} of 6: {title}", a, b, None, None, cap=19, note=purpose)
            return
    raise SystemExit(f"no block {ref}")


def walk_image(ref: str, path: Path) -> None:
    import walk_chapter07 as WK
    b, r, ph = ref.split(":")
    k, ri, phase = int(b[1:]), int(r[1:]), int(ph)
    for kk, title, purpose, a, bb, rows in WK.blocks():
        if kk == k:
            ln, text, key, says, keys = rows[ri - 1]
            _script_view(path, f"Block {k} of 6: {title}", a, bb, ln, key if phase == 2 else None, cap=15,
                         note="The whole line" if phase == 1 else "The key part of the line, boxed")
            return
    raise SystemExit(f"no walk {ref}")


def run_image(ref: str, path: Path, modes: dict) -> None:
    """The four settings lines as typed and what R really printed (or the first rows of signals.csv)."""
    titles = {"buy_wait": "Buy mode: WAIT", "buy_signal": "Buy mode: BUY", "sell_now": "Sell mode: SELL now",
              "sell_hold": "Sell mode: HOLD",
              "buy_update": "New data, run again", "table": "output/signals.csv"}
    if ref == "table":
        head = modes["buy_wait"]["head"][:8]
        settings, out, label = [], "\n".join(head), "output/signals.csv, the first rows"
    else:
        r = modes[ref]
        settings, out, label = r["settings"].splitlines(), r["answer"], "R printed, and the same lines in output/answer.txt"
    code = "".join(f'<div class="l"><span class="n">{3 + i}</span><span>{html.escape(x)}</span></div>' for i, x in enumerate(settings))
    box = f'<div class="code">{code}</div>' if settings else ""
    cap = '<div class="note">The four settings lines, as typed</div>' if settings else ""
    doc = f"""<!doctype html><meta charset=utf-8><style>
    body{{margin:0;width:{W}px;height:{PICTURE_H}px;background:#fff;font-family:Helvetica,Arial,sans-serif;overflow:hidden}}
    .bar{{height:24px;background:#1E5631;border-bottom:12px solid #F2A900}}
    h1{{font-size:50px;color:#1E5631;margin:22px 50px 8px;font-weight:600}}
    .note{{font-size:28px;color:#555;margin:0 50px 10px}}
    .code{{margin:0 50px 26px;border:2px solid #cfd8d1;border-radius:10px;padding:10px 0;font:27px/1.42 Menlo,monospace}}
    .l{{display:flex;padding:0 16px;white-space:pre}} .n{{width:56px;color:#889;text-align:right;margin-right:20px;flex:none}}
    .out{{margin:0 50px;background:#1f2a24;color:#e8f1ea;border-radius:12px;padding:18px 28px;font:30px/1.4 Menlo,monospace;white-space:pre-wrap}}
    .out b{{display:block;font:600 22px Helvetica;color:#9fb8a8;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}}
    </style><div class=bar></div><h1>{html.escape(titles[ref])}</h1>{cap}{box}
    <div class=out><b>{html.escape(label)}</b>{html.escape(out)}</div>"""
    _shoot_content(doc, path)


def make_video(out: Path, screens: Path, voice: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    cache: dict = {}
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)

        cuelog: dict = {}

        def render(n: int, s, times) -> Path:
            """One scene to one segment. Scenes that name a time are redrawn when the times move."""
            img = t / f"{n:03d}.png"
            imgs = [img]
            say = resolve(s.say, times)
            if s.kind == "opening":       # the opening is drawn frame by frame, with its own timed captions (opening_chapter07.py)
                import opening_chapter07 as OP
                seg, cues = OP.build(t, n, voice, say_clip, _probe, sub_image, W, PICTURE_H, H, FFMPEG, REC)
                cuelog[n] = cues
                return seg
            if s.kind == "shot":
                src = screens / f"{s.ref}.png"
                if not src.is_file():
                    raise SystemExit(f"missing screenshot {src}")
                fit(src, img, s.label)
            elif s.kind == "web":
                src = WEB / f"{s.ref}.png"
                if not src.is_file():
                    raise SystemExit(f"missing web capture {src}")
                fit(src, img)
            elif s.kind == "page":
                imgs = page_images(s.ref, s.crop, img, cache)
            elif s.kind == "gen":
                src = GEN / f"{s.ref}.png"
                if not src.is_file():
                    raise SystemExit(f"missing generated image {src}")
                fit(src, img)
            elif s.kind == "frame":
                fr = t / f"{n:03d}_frame.png"
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-sseof", "-0.4", "-i", str(REC / f"{s.ref}.mp4"),
                                "-frames:v", "1", str(fr)], check=True)
                from PIL import Image
                im0 = Image.open(fr).convert("RGB")
                if s.crop:
                    im0 = im0.crop(s.crop)
                im0.save(fr)
                fit(fr, img)
            elif s.kind == "block":
                block_image(s.ref, img)
            elif s.kind == "walk":
                walk_image(s.ref, img)
            elif s.kind == "run":
                run_image(s.ref, img, json.loads((GEN / "modes.json").read_text()))
            elif s.kind == "clip":
                imgs = []
            else:
                card(s, img)
            if s.popup:
                for im in imgs:
                    banner(im, resolve(s.popup, times))
            aiff, cues, adur = speak(t, n, say, voice)
            seg = t / f"{n:03d}.mp4"
            dur = adur + 0.7
            vv = t / f"{n:03d}_v.mp4"
            if s.kind == "clip":
                src = REC / f"{s.ref}.mp4"
                if not src.is_file():
                    raise SystemExit(f"missing recording {src}")
                cd = _probe(src) / s.speed
                extra = dur if s.after else max(0.0, dur - cd)      # `after`: speak over the last frame, never over the typing
                vf = (f"setpts=PTS/{s.speed},scale={W}:{PICTURE_H}:force_original_aspect_ratio=decrease,"
                      f"pad={W}:{PICTURE_H}:(ow-iw)/2:(oh-ih)/2:white,pad={W}:{H}:0:0:white,"
                      f"tpad=stop_mode=clone:stop_duration={extra:.3f},fps=10")
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(src), "-vf", vf, "-an", "-c:v", "libx264",
                                "-pix_fmt", "yuv420p", str(vv)], check=True)
                if s.after:        # silence while the recording plays, then the voice
                    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(aiff), "-af",
                                    f"adelay={int(cd * 1000)}:all=1,apad=pad_dur=0.7", str(aiff.with_suffix(".delayed.wav"))], check=True)
                    aiff = aiff.with_suffix(".delayed.wav")
                    cues = [(a + cd, b + cd, x) for a, b, x in cues]
            else:
                parts = []
                for k, im in enumerate(imgs):
                    pv = t / f"{n:03d}_{k}.mp4"
                    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-t", f"{dur / len(imgs):.3f}", "-i", str(im),
                                    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10", str(pv)], check=True)
                    parts.append(pv)
                vl = t / f"{n:03d}_v.txt"; vl.write_text("".join(f"file '{p}'\n" for p in parts))
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(vl), "-c", "copy", str(vv)], check=True)
            vv = burn(t, n, vv, cues)
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(vv), "-i", str(aiff), "-c:v", "copy", "-c:a", "aac",
                            "-b:a", "128k", "-af", "apad=pad_dur=0.7", "-shortest", str(seg)], check=True)
            cuelog[n] = cues
            return seg

        def joined(segs: list, name: str) -> Path:
            lst = t / f"{name}.txt"
            lst.write_text("".join(f"file '{p}'\n" for p in segs))
            f = t / f"{name}.mp4"
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(f)], check=True)
            return f

        def locate(final: Path, seg: Path, approx: float, win: float = 8.0) -> float:
            """When a scene really starts in the joined file: the first frame, near where the sums say, that equals the
            scene's own first frame. The sums of segment lengths drift by a second or two, so they are not trusted."""
            import numpy as np
            from PIL import Image
            d = t / "loc"; shutil.rmtree(d, ignore_errors=True); d.mkdir()
            ref = d / "ref.png"
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-ss", "0.25", "-i", str(seg), "-frames:v", "1",
                            "-vf", "scale=320:-1", str(ref)], check=True)
            t0 = max(0.0, approx - win)
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-ss", f"{t0:.3f}", "-t", f"{2 * win:.3f}", "-i", str(final),
                            "-vf", "fps=10,scale=320:-1", str(d / "%04d.png")], check=True)
            r = np.asarray(Image.open(ref).convert("L"), dtype=float)
            for i, f in enumerate(sorted(d.glob("0*.png"))):
                g = np.asarray(Image.open(f).convert("L"), dtype=float)
                if g.shape == r.shape and abs(g - r).mean() < 2.5:
                    return t0 + i / 10
            raise SystemExit(f"could not find the start of {seg.name} in the joined video near {approx:.1f}s")

        def starts(segs: list) -> dict:
            final = joined(segs, "probe")
            acc, at = 0.0, {}
            for n, (sc, sg) in enumerate(zip(SCENES, segs)):
                for k, title in MARKS.items():
                    if sc.title == title:
                        at[k] = int(locate(final, sg, acc))          # whole second at or just before the real start
                acc += _probe(sg)
            return at

        times = {"short": 20 * 60, "out": 40 * 60, "long": 5 * 60}       # provisional, so the first drawing has the right shape
        times = {k: v for k, v in (load_times() or times).items() if k in times}
        if not MARKS:
            times = {}
        segs = [render(n, s, times) for n, s in enumerate(SCENES, 1)]
        timed = [n for n, s in enumerate(SCENES) if "{" in s.say or "{" in s.popup]
        for rounds in range(30):
            real = starts(segs)
            if real == times:
                break
            times = real
            for n in timed:
                segs[n] = render(n + 1, SCENES[n], times)
        else:
            raise SystemExit(f"the times did not settle: {times} vs {real}")
        if MARKS:
            TIMES.write_text(json.dumps({**times, "label": {k: mmss(v) for k, v in times.items()}}, indent=1))
        lst = t / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in segs))
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c", "copy", str(out)], check=True)
        chk = {}
        acc = 0.0
        for n, (sc, sg) in enumerate(zip(SCENES, segs)):
            for k, title in MARKS.items():
                if sc.title == title:
                    chk[k] = locate(out, sg, acc)
            acc += _probe(sg)
        for k, v in chk.items():                 # what the popups say must be where the scene really starts
            if not (times[k] <= v < times[k] + 1.0 + 1e-6):
                raise SystemExit(f"the time shown for {k} ({mmss(times[k])}) is not where it starts ({v:.2f}s)")
        print("verified in the finished file:", {k: round(v, 2) for k, v in chk.items()})
        acc, starts_at = 0.0, {}
        for n, sg in enumerate(segs, 1):
            starts_at[n] = acc
            acc += _probe(sg)
        for k, v in chk.items():       # the sums of segment lengths and the real positions must agree closely: the subtitle file uses the sums
            sm = next(starts_at[i + 1] for i, sc in enumerate(SCENES) if sc.title == MARKS[k])
            if abs(sm - v) > 0.35:
                raise SystemExit(f"segment sums say {k} starts at {sm:.2f}s but it is at {v:.2f}s: the subtitle times would drift")
        def stamp(x: float) -> str:
            ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
            return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
        srt, k = [], 0
        for n in sorted(cuelog):
            for a, b, text in cuelog[n]:
                k += 1
                srt += [str(k), f"{stamp(starts_at[n] + a)} --> {stamp(starts_at[n] + b)}", text, ""]
        out.with_suffix(".srt").write_text("\n".join(srt), encoding="utf-8")
        total = _probe(out)
        print("times (mm:ss):", {k: mmss(v) for k, v in times.items()}, "| length", mmss(int(total)), f"({total:.1f}s)")
        if a_keep:
            shutil.copytree(t, a_keep, dirs_exist_ok=True)
    write_narration(times)         # the narration script carries the same times
    print("wrote", out)


a_keep = None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--narration-only", action="store_true")
    ap.add_argument("--video-out", type=Path)
    ap.add_argument("--screens", type=Path, default=SCREENS)
    ap.add_argument("--voice", default="Samantha")
    ap.add_argument("--keep-frames", type=Path)
    a = ap.parse_args()
    a_keep = a.keep_frames
    write_narration(load_times())
    if not a.narration_only:
        if not a.video_out:
            raise SystemExit("--video-out is required")
        make_video(a.video_out, a.screens, a.voice)
