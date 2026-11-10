"""ショート（縦1080x1920・60秒未満）: 本編の画像とナレーションから作る。出力: build/<ep>/short.mp4
usage: python pipeline/short.py ep11_onoda
"""
import json, os, subprocess, shutil, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps

import sys
from common import load
ep, WORK = load(sys.argv[1])
CFG = dict(ep.SHORT, out="short.mp4")
E2_NEW = "▶ 続きは本編で\n画面下の「関連動画」から見られます"
if len(sys.argv) > 2:  # 追加ショート: python pipeline/short.py <ep> <alt.json>
    CFG.update(json.load(open(os.path.abspath(sys.argv[2]))))
if "固定コメント" in CFG.get("e2", ""): CFG["e2"] = E2_NEW
os.chdir(WORK)
SEL = CFG["sel"]
GAP = 0.2
W, H, FPS = 1080, 1920, 30
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"
RED = (214, 20, 28)
AMBER = (255, 170, 60)
STAMP = {int(k): v for k, v in CFG["stamp"].items()}

T = json.load(open("timing.json"))["lines"]
work = "_short" + CFG.get("suffix", "")
shutil.rmtree(work, ignore_errors=True)
os.makedirs(work)

# ---------- audio ----------
with wave.open("narration.wav") as w:
    sr = w.getframerate()
    pcm = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
segs, t, spans = [], 0.0, []
for n in SEL:
    ln = T[n - 1]
    a, b = int((ln["start"] - 0.03) * sr), int((ln["end"] + 0.08) * sr)
    x = pcm[a:b]
    segs += [x, np.zeros(int(GAP * sr), np.int16)]
    spans.append((n, t, t + len(x) / sr + GAP))
    t += len(x) / sr + GAP
END = 2.4
segs.append(np.zeros(int(END * sr), np.int16))
total = t + END
audio = np.concatenate(segs)
with wave.open(f"{work}/voice.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(audio.tobytes())
print("duration", round(total, 2))

# ---------- frames ----------
f_t1 = ImageFont.truetype(SERIF, 92)
f_t2 = ImageFont.truetype(SERIF, 70)
f_sub = ImageFont.truetype(SANS, 62)
f_stamp = ImageFont.truetype(SERIF, 120)
f_end1 = ImageFont.truetype(SERIF, 84)
f_end2 = ImageFont.truetype(SANS, 54)


def wrap(text, font, maxw, d):
    text = text.replace("――", "、")
    rows, cur = [], ""
    for ch in text:
        if d.textlength(cur + ch, font=font) > maxw and ch not in "、。」":
            rows.append(cur); cur = ch
        else:
            cur += ch
    rows.append(cur)
    return [r for r in rows if r]


def ctext(d, y, s, font, fill, sw=6):
    w_ = d.textlength(s, font=font)
    d.text(((W - w_) / 2, y), s, font=font, fill=fill, stroke_width=sw, stroke_fill=(0, 0, 0))


def frame(n, text, end=False):
    src = Image.open(f"images/{n:03d}.jpg").convert("RGB")
    bg = ImageOps.fit(src, (W, H)).filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.35)
    fh = 900
    fg = src.resize((round(src.width * fh / src.height), fh), Image.LANCZOS)
    cx = (fg.width - W) // 2
    fg = fg.crop((cx, 0, cx + W, fh))
    bg.paste(fg, (0, 420))
    d = ImageDraw.Draw(bg)
    # header
    ctext(d, 110, CFG["h1"], ImageFont.truetype(SERIF, min(92, int((W - 70) / max(1, len(CFG["h1"]))))), (255, 255, 255), 8)
    ctext(d, 235, CFG["h2"], ImageFont.truetype(SERIF, min(92, int((W - 70) / max(1, len(CFG["h2"]))))), RED, 8)
    if n in STAMP or any(n > k for k in STAMP):
        k = max([k for k in STAMP if k <= n], default=None)
        if k:
            d.text((50, 1160), STAMP[k], font=f_stamp, fill=AMBER, stroke_width=8, stroke_fill=(0, 0, 0))
    if end:
        d.rectangle([0, 1340, W, 1640], fill=(0, 0, 0))
        fe = ImageFont.truetype(SERIF, min(84, int((W - 90) / max(1, len(CFG["e1"])))))
        ctext(d, 1370 + (84 - fe.size) // 2, CFG["e1"], fe, (255, 255, 255), 0)
        e2 = CFG["e2"].split("\n")
        f2 = ImageFont.truetype(SANS, min(60, int((W - 80) / max(1, len(e2[0])))))
        ctext(d, 1480, e2[0], f2, AMBER, 0)
        if len(e2) > 1:
            f3 = ImageFont.truetype(SANS, min(46, int((W - 80) / max(1, len(e2[1])))))
            ctext(d, 1480 + f2.size + 22, e2[1], f3, (255, 255, 255), 0)
    else:
        rows = wrap(text, f_sub, W - 120, d)
        y = 1370
        for r in rows[:3]:
            ctext(d, y, r, f_sub, (255, 255, 255), 7)
            y += 84
    return bg


clips = []
for i, (n, a, b) in enumerate(spans):
    is_last = i == len(spans) - 1
    dur = (b - a) + (END if is_last else 0)
    img = frame(n, T[n - 1]["text"], end=is_last)
    p = f"{work}/{i:02d}.png"
    img.resize((int(W * 1.06), int(H * 1.06)), Image.LANCZOS).save(p)
    fr = round(dur * FPS)
    z = f"1+0.05*on/{fr}" if i % 2 == 0 else f"1.05-0.05*on/{fr}"
    out = f"{work}/{i:02d}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", p, "-vf",
                    f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s={W}x{H}:fps={FPS},format=yuv420p",
                    "-frames:v", str(fr), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out], check=True)
    clips.append(out)
    if i == 0:
        img.save(f"short_preview_first{CFG.get('suffix','')}.jpg", quality=85)
    if is_last:
        img.save(f"short_preview_last{CFG.get('suffix','')}.jpg", quality=85)

with open(f"{work}/list.txt", "w") as f:
    for c in clips:
        f.write(f"file '{os.path.abspath(c)}'\n")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt",
                "-c", "copy", f"{work}/video.mp4"], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{work}/video.mp4", "-i", f"{work}/voice.wav",
                "-f", "lavfi", "-t", str(total + 1),
                "-i", "anoisesrc=color=brown:amplitude=0.6,lowpass=f=160,volume=0.07",
                "-filter_complex",
                "[1:a]aresample=48000[n];[2:a]aresample=48000[b];[n][b]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout]",
                "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                CFG["out"]], check=True)
print("ok")
