#!/usr/bin/env python3
"""Make the narration script, and the computer-voice walkthrough video.

    .venv/bin/python build/build_video.py --narration-only
    .venv/bin/python build/build_video.py --video-out <path .mp4>

The narration script (a Markdown file in the student folder) is written from
build/video_chapter07.py, the same scenes the video speaks. The video is made
with macOS `say` and ffmpeg and is too large for git, so it is written to a
path outside the repository. Pass --screens for the folder of screenshots.
"""
import argparse, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import activity_chapter07 as A  # noqa: E402
from video_chapter07 import SCENES  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SCREENS = REPO / "chapter-07" / "activity" / "screens"
NARRATION = A.STUDENT / f"{A.NAME} - Narration Script.md"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
W, H = 1920, 1080


def write_narration() -> None:
    out = [f"# {A.NAME}: narration script", "",
           "Read this over the screenshots of Part 5 of the handout, one "
           "section per picture. About four minutes. Say the words in "
           "your own voice and change anything that is not how you talk.", ""]
    for n, s in enumerate(SCENES, 1):
        pic = f"Picture: `{s.shot}.png`" if s.shot else "Picture: a title card"
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


def make_video(out: Path, screens: Path, voice: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        t = Path(t); segs = []
        for n, s in enumerate(SCENES, 1):
            img = t / f"{n:02d}.png"
            if s.shot:
                src = screens / f"{s.shot}.png"
                if not src.is_file():
                    raise SystemExit(f"missing screenshot {src}")
                fit(src, img)
            else:
                card(s, img)
            aiff = t / f"{n:02d}.aiff"
            subprocess.run(["say", "-v", voice, "-r", "165", "-o", str(aiff), s.say], check=True)
            seg = t / f"{n:02d}.mp4"
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", str(img),
                            "-i", str(aiff), "-c:v", "libx264", "-tune", "stillimage",
                            "-pix_fmt", "yuv420p", "-r", "10", "-c:a", "aac", "-b:a", "128k",
                            "-af", "apad=pad_dur=0.6", "-shortest", str(seg)], check=True)
            segs.append(seg)
        lst = t / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in segs))
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c", "copy", str(out)], check=True)
    print("wrote", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--narration-only", action="store_true")
    ap.add_argument("--video-out", type=Path)
    ap.add_argument("--screens", type=Path, default=SCREENS)
    ap.add_argument("--voice", default="Samantha")
    a = ap.parse_args()
    write_narration()
    if not a.narration_only:
        if not a.video_out:
            raise SystemExit("--video-out is required")
        make_video(a.video_out, a.screens, a.voice)
