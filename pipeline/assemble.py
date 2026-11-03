"""本編の組み立て: 画像 + ナレーションのタイミングから動画を作り、アップロード用に圧縮する。

出力: build/<ep>/episode_up.mp4
usage: python pipeline/assemble.py ep11_onoda
"""
import argparse, json, os, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
from common import SANS_BOLD, SERIF_BLACK, load

ap = argparse.ArgumentParser()
ap.add_argument("episode")
ap.add_argument("--fps", type=int, default=30)
a = ap.parse_args()
ep, WORK = load(a.episode)
os.chdir(WORK)
W, H, FPS = 1920, 1080, a.fps
IMG = "images"
STAMPS = getattr(ep, "STAMPS", {})
T = json.load(open("timing.json"))
lines = T["lines"]
assert len(lines) == len(ep.LINES), "timing.json is out of date: run tts.py again"
k = W / 1920
f_stamp = ImageFont.truetype(SERIF_BLACK, int(96 * k))
f_ph_big = ImageFont.truetype(SERIF_BLACK, int(120 * k))
f_ph = ImageFont.truetype(SANS_BOLD, int(40 * k))
work = "_clips"
shutil.rmtree(work, ignore_errors=True)
os.makedirs(work)


def find_images(n):
    out = []
    for suf in ["", "a", "b", "c", "d"]:
        for ext in ("png", "jpg", "jpeg", "webp"):
            p = f"{IMG}/{n:03d}{suf}.{ext}"
            if os.path.exists(p):
                out.append(p)
                break
    return out


def wrap(text, font, maxw, d):
    rows, cur = [], ""
    for ch in text:
        if d.textlength(cur + ch, font=font) > maxw:
            rows.append(cur)
            cur = ch
        else:
            cur += ch
    return rows + [cur]


def placeholder(n, part, text):
    img = Image.new("RGB", (W, H), (10, 22, 34))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(8 + 10 * (1 - t)), int(20 + 26 * (1 - t)), int(32 + 40 * (1 - t))))
    label = f"{n:03d}{part}"
    lw = d.textlength(label, font=f_ph_big)
    d.text(((W - lw) / 2, H * 0.30), label, font=f_ph_big, fill=(120, 160, 175))
    y = H * 0.55
    for r in wrap(text, f_ph, W * 0.75, d)[:3]:
        rw = d.textlength(r, font=f_ph)
        d.text(((W - rw) / 2, y), r, font=f_ph, fill=(150, 180, 190))
        y += f_ph.size * 1.4
    return img


def fit(path):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (W, H), Image.LANCZOS)


def stamp(img, text):
    d = ImageDraw.Draw(img)
    x, y = int(70 * k), int(H - 230 * k)
    d.text((x, y), text, font=f_stamp, fill=(255, 170, 60), stroke_width=int(6 * k), stroke_fill=(0, 0, 0))
    return img


def clip(img, dur, idx, zoom_in):
    src = f"{work}/{idx:04d}.png"
    big = img.resize((int(W * 1.12), int(H * 1.12)), Image.LANCZOS)
    big.save(src)
    frames = max(1, round(dur * FPS))
    z = f"1+0.08*on/{frames}" if zoom_in else f"1.08-0.08*on/{frames}"
    vf = (f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
          f"format=yuv420p")
    out = f"{work}/{idx:04d}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-vf", vf, "-frames:v", str(frames),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out], check=True)
    return out, frames / FPS


clips, idx, current_stamp, t_video, missing = [], 0, None, 0.0, []
for i, ln in enumerate(lines):
    n = i + 1
    start = 0.0 if i == 0 else ln["start"]
    end = lines[i + 1]["start"] if i + 1 < len(lines) else T["total"] + 1.0
    text = ln["text"]
    current_stamp = STAMPS.get(text)
    paths = find_images(n)
    dur = end - start
    if not paths:
        parts = 1 if dur <= 4.5 else (2 if dur <= 9 else 3)
        imgs = [placeholder(n, "abc"[j] if parts > 1 else "", text) for j in range(parts)]
        missing.append(n)
    else:
        imgs = [fit(p) for p in paths]
    seg = dur / len(imgs)
    for j, im in enumerate(imgs):
        if current_stamp:
            im = stamp(im, current_stamp)
        # keep total video length locked to the audio timeline
        target_end = start + seg * (j + 1)
        out, real = clip(im, target_end - t_video, idx, zoom_in=(idx % 2 == 0))
        clips.append(out)
        t_video += real
        idx += 1

with open(f"{work}/list.txt", "w") as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt",
                "-c", "copy", f"{work}/video.mp4"], check=True)

# audio: narration + low cave drone
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{work}/video.mp4", "-i", "narration.wav",
                "-f", "lavfi", "-t", str(T["total"] + 5),
                "-i", "anoisesrc=color=brown:amplitude=0.6,lowpass=f=220,volume=0.05,aecho=0.6:0.5:180:0.25",
                "-filter_complex", "[1:a]aresample=48000[n];[2:a]aresample=48000[b];[n][b]amix=inputs=2:duration=longest:normalize=0[aout]",
                "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "episode_raw.mp4"], check=True)
print(f"done: {"episode_raw.mp4"}  clips={len(clips)}  video={t_video:.1f}s  missing images for {len(missing)} lines")

# アップロード用に圧縮（音量も -14 LUFS にそろえる）
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "episode_raw.mp4", "-c:v", "libx264", "-crf", "26",
                "-tune", "stillimage", "-preset", "medium", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "episode_up.mp4"], check=True)
os.remove("episode_raw.mp4")
shutil.rmtree(work, ignore_errors=True)
print("episode_up.mp4 ready")
