#!/usr/bin/env python3
"""Make the narration script, and the computer-voice walkthrough video.

    .venv/bin/python build/build_video.py --narration-only
    .venv/bin/python build/build_video.py --video-out <path .mp4>

The narration script (a Markdown file in the student folder) is written from
build/video_chapter07.py, the same scenes the video speaks. The video is made
with macOS `say` and ffmpeg and is too large for git, so it is written to a
path outside the repository. Pass --screens for the folder of screenshots.
"""
import argparse, html, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activity_chapter07 as A  # noqa: E402
import chrome  # noqa: E402
from video_chapter07 import SCENES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SCREENS = REPO / "chapter-07" / "activity" / "screens"
GEN = REPO / "build" / "generated" / "activity2"
WEB = REPO / "build" / "generated" / "video" / "web"
import os
REC = Path(os.environ.get("FM_REC") or "/Users/benjie/.treehouse/benjie-agent-workspace-8bf1b0/1/benjie-agent-workspace/data/fin1209-activity2/rec")
HANDOUT = A.STUDENT / f"{A.NAME}.pdf"
NARRATION = A.STUDENT / f"{A.NAME} - Narration Script.md"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
W, H = 1920, 1080
TIMES = REPO / "build" / "video_times.json"        # the real start of each version in the finished video
MARKS = {"long": "The long version", "short": "The short version", "out": "The answer"}


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


def banner(path: Path, text: str) -> None:
    from PIL import Image, ImageDraw, ImageFont
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 64)
    x0, y0, x1, y1 = d.textbbox((0, 0), text, font=f)
    w, h = x1 - x0, y1 - y0
    cx, cy = W // 2, H - 150
    d.rounded_rectangle([cx - w // 2 - 50, cy - h // 2 - 38, cx + w // 2 + 50, cy + h // 2 + 38], radius=26,
                        fill="#F2A900", outline="#1E5631", width=8)
    d.text((cx, cy), text, font=f, fill="#222222", anchor="mm")
    im.save(path)


def write_narration(times=None) -> None:
    out = [f"# {A.NAME}: narration script", "",
           "Read this over the video's pictures, one "
           "section per picture, in the handout's order. The video has a long and a short version of the coding, and the skip times below are the real ones. Say the words in "
           "your own voice and change anything that is not how you talk.", ""]
    for n, s in enumerate(SCENES, 1):
        pic = {"card": "a title card", "shot": f"screenshot `{s.ref}`", "web": "a capture of a public web page",
               "page": "the handout page: " + s.ref, "code": f"the code of R step {s.ref}", "frame": f"the last frame of {s.ref}", "code": f"the code of R step {s.ref}", "gen": f"an image R drew ({s.ref})", "clip": f"a screen recording ({s.ref})"}[s.kind]
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
    k = min(W / im.width, H / im.height)
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    bg = Image.new("RGB", (W, H), "#FFFFFF")
    bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
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
        sc = min(W / im.width, H / im.height)
        im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        bg = Image.new("RGB", (W, H), "#FFFFFF"); bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
        f = out.with_name(out.stem + f"_{k}.png"); bg.save(f); outs.append(f)
    return outs


def code_image(key: str, out: Path, fills: dict, outs: dict) -> None:
    from activity_chapter07 import _stage_code, _new_lines
    from activity_chapter07_code import STAGES
    idx = [st.key for st in STAGES].index(key)
    st = STAGES[idx]
    code = _stage_code(st, fills)
    prev = _stage_code(STAGES[idx - 1], fills) if idx else ""
    new = set(_new_lines(prev, code))
    lines = code.splitlines()
    cap = 30
    start = 0
    if len(lines) > cap:
        first = min(new) if new else 1
        start = max(0, min(first - 3, len(lines) - cap))
    shown = lines[start:start + cap]
    rows = []
    for n, ln in enumerate(shown, start + 1):
        cls = "new" if n in new else ""
        rows.append(f'<div class="l {cls}"><span class="n">{n}</span><span>{html.escape(ln) or "&nbsp;"}</span></div>')
    more_top = '<div class="m">... earlier lines not shown</div>' if start else ""
    more_bot = '<div class="m">... later lines not shown</div>' if start + cap < len(lines) else ""
    output = html.escape(outs.get(key, ""))
    if len(output.splitlines()) > 9:
        output = "\n".join(output.splitlines()[:9]) + "\n..."
    doc = f"""<!doctype html><meta charset=utf-8><style>
    body{{margin:0;width:{W}px;height:{H}px;background:#fff;font-family:Helvetica,Arial,sans-serif;overflow:hidden}}
    .bar{{height:24px;background:#1E5631;border-bottom:12px solid #F2A900}}
    h1{{font-size:44px;color:#1E5631;margin:22px 50px 8px;font-weight:600}}
    .code{{margin:0 50px;border:2px solid #cfd8d1;border-radius:10px;padding:10px 0;font:25px/1.32 Menlo,monospace}}
    .l{{display:flex;padding:0 16px;white-space:pre}} .n{{width:52px;color:#889;text-align:right;margin-right:18px;flex:none}}
    .new{{background:#fff0b8;border-left:12px solid #F2A900;padding-left:4px}}
    .m{{padding:0 16px;color:#889;font:italic 22px Helvetica}}
    .out{{margin:16px 50px 0;background:#1f2a24;color:#e8f1ea;border-radius:10px;padding:12px 22px;font:24px/1.3 Menlo,monospace;white-space:pre}}
    .out b{{display:block;font:600 18px Helvetica;color:#9fb8a8;letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}}
    </style><div class=bar></div><h1>{html.escape(st.title)}</h1>
    <div class=code>{more_top}{''.join(rows)}{more_bot}</div>
    <div class=out><b>R printed</b>{output or '(nothing printed: open the file it wrote)'}</div>"""
    h = out.with_suffix(".html"); h.write_text(doc)
    subprocess.run([str(chrome.CHROME), "--headless", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}",
                    f"--screenshot={out}", h.as_uri()], check=True, capture_output=True)


def _probe(path: Path) -> float:
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                capture_output=True, text=True).stdout)


def make_video(out: Path, screens: Path, voice: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    gen = json.loads((REPO / "build" / "generated" / "activity2" / "counts.json").read_text())
    outs = json.loads((REPO / "build" / "generated" / "activity2" / "stage_outputs.json").read_text())
    fills = {"SELL_I": gen["SELL_I"], "BUY_I": gen["BUY_I"]}
    cache: dict = {}
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)

        def render(n: int, s, times) -> Path:
            """One scene to one segment. Scenes that name a time are redrawn when the times move."""
            img = t / f"{n:03d}.png"
            imgs = [img]
            say = resolve(s.say, times)
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
            elif s.kind == "clip":
                imgs = []
            elif s.kind == "code":
                code_image(s.ref, img, fills, outs)
            else:
                card(s, img)
            if s.popup:
                for im in imgs:
                    banner(im, resolve(s.popup, times))
            aiff = t / f"{n:03d}.aiff"
            subprocess.run(["say", "-v", voice, "-r", "165", "-o", str(aiff), say], check=True)
            seg = t / f"{n:03d}.mp4"
            dur = _probe(aiff) + 0.7
            vv = t / f"{n:03d}_v.mp4"
            if s.kind == "clip":
                src = REC / f"{s.ref}.mp4"
                if not src.is_file():
                    raise SystemExit(f"missing recording {src}")
                cd = _probe(src) / s.speed
                extra = dur if s.after else max(0.0, dur - cd)      # `after`: speak over the last frame, never over the typing
                vf = (f"setpts=PTS/{s.speed},scale={W}:{H}:force_original_aspect_ratio=decrease,"
                      f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,tpad=stop_mode=clone:stop_duration={extra:.3f},fps=10")
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(src), "-vf", vf, "-an", "-c:v", "libx264",
                                "-pix_fmt", "yuv420p", str(vv)], check=True)
                if s.after:        # silence while the recording plays, then the voice
                    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(aiff), "-af",
                                    f"adelay={int(cd * 1000)}:all=1,apad=pad_dur=0.7", str(aiff.with_suffix(".wav"))], check=True)
                    aiff = aiff.with_suffix(".wav")
            else:
                parts = []
                for k, im in enumerate(imgs):
                    pv = t / f"{n:03d}_{k}.mp4"
                    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-t", f"{dur / len(imgs):.3f}", "-i", str(im),
                                    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "10", str(pv)], check=True)
                    parts.append(pv)
                vl = t / f"{n:03d}_v.txt"; vl.write_text("".join(f"file '{p}'\n" for p in parts))
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(vl), "-c", "copy", str(vv)], check=True)
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(vv), "-i", str(aiff), "-c:v", "copy", "-c:a", "aac",
                            "-b:a", "128k", "-af", "apad=pad_dur=0.7", "-shortest", str(seg)], check=True)
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
