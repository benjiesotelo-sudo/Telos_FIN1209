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
WEB = REPO / "build" / "generated" / "video" / "web"
REC = Path("/Users/benjie/.treehouse/benjie-agent-workspace-8bf1b0/1/benjie-agent-workspace/data/fin1209-activity2/rec")
HANDOUT = A.STUDENT / f"{A.NAME}.pdf"
NARRATION = A.STUDENT / f"{A.NAME} - Narration Script.md"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
W, H = 1920, 1080


def write_narration() -> None:
    out = [f"# {A.NAME}: narration script", "",
           "Read this over the video's pictures, one "
           "section per picture, in the handout's order. About twenty minutes. Say the words in "
           "your own voice and change anything that is not how you talk.", ""]
    for n, s in enumerate(SCENES, 1):
        pic = {"card": "a title card", "shot": f"screenshot `{s.ref}`", "web": "a capture of a public web page",
               "page": "the handout page: " + s.ref, "code": f"the code of R step {s.ref}", "clip": f"a screen recording ({s.ref})"}[s.kind]
        pic = "Picture: " + pic
        out += [f"## {n}. {s.title}", "", f"*{pic}*", "", s.say, ""]
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


def fit(src: Path, path: Path) -> None:
    from PIL import Image
    im = Image.open(src).convert("RGB")
    k = min(W / im.width, H / im.height)
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    bg = Image.new("RGB", (W, H), "#FFFFFF")
    bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
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


def make_video(out: Path, screens: Path, voice: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    gen = json.loads((REPO / "build" / "generated" / "activity2" / "counts.json").read_text())
    outs = json.loads((REPO / "build" / "generated" / "activity2" / "stage_outputs.json").read_text())
    fills = {"SELL_I": gen["SELL_I"], "BUY_I": gen["BUY_I"]}
    cache: dict = {}
    with tempfile.TemporaryDirectory() as t:
        t = Path(t); segs = []
        for n, s in enumerate(SCENES, 1):
            img = t / f"{n:03d}.png"
            imgs = [img]
            if s.kind == "shot":
                src = screens / f"{s.ref}.png"
                if not src.is_file():
                    raise SystemExit(f"missing screenshot {src}")
                fit(src, img)
            elif s.kind == "web":
                src = WEB / f"{s.ref}.png"
                if not src.is_file():
                    raise SystemExit(f"missing web capture {src}")
                fit(src, img)
            elif s.kind == "page":
                imgs = page_images(s.ref, s.crop, img, cache)
            elif s.kind == "clip":
                imgs = []                        # video comes from the recording, below
            elif s.kind == "code":
                code_image(s.ref, img, fills, outs)
            else:
                card(s, img)
            aiff = t / f"{n:03d}.aiff"
            subprocess.run(["say", "-v", voice, "-r", "165", "-o", str(aiff), s.say], check=True)
            seg = t / f"{n:03d}.mp4"
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(aiff)],
                                       capture_output=True, text=True).stdout) + 0.7
            vv = t / f"{n:03d}_v.mp4"
            if s.kind == "clip":
                src = REC / f"{s.ref}.mp4"
                if not src.is_file():
                    raise SystemExit(f"missing recording {src}")
                cd = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(src)],
                                          capture_output=True, text=True).stdout)
                extra = max(0.0, dur - cd)       # hold the last frame if the narration is longer
                vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,"
                      f"tpad=stop_mode=clone:stop_duration={extra:.3f},fps=10")
                subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(src), "-vf", vf, "-an", "-c:v", "libx264",
                                "-pix_fmt", "yuv420p", str(vv)], check=True)
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
            segs.append(seg)
        lst = t / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in segs))
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c", "copy", str(out)], check=True)
        if a_keep:
            shutil.copytree(t, a_keep, dirs_exist_ok=True)
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
    write_narration()
    if not a.narration_only:
        if not a.video_out:
            raise SystemExit("--video-out is required")
        make_video(a.video_out, a.screens, a.voice)
