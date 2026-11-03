"""字幕(.srt)とチャプターを作る。出力: build/<ep>/subtitles.srt, chapters.txt
usage: python pipeline/subs.py ep11_onoda
"""
import json, os, re, sys
from common import load
ep, WORK = load(sys.argv[1])
os.chdir(WORK)

T = json.load(open("timing.json"))
TOTAL = T["total"]


def split_text(text, limit=24):
    """Split a narration line into subtitle chunks at punctuation, each <= ~2 lines."""
    parts = re.findall(r"[^。]+。?", text)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        while len(p) > 40:
            cut = p.rfind("、", 12, 40)
            if cut < 0:
                cut = 30
            out.append(p[: cut + 1])
            p = p[cut + 1:]
        out.append(p)
    # merge very short fragments with the next one
    merged = []
    for s in out:
        if merged and len(merged[-1]) + len(s) <= limit and len(merged[-1]) < 10:
            merged[-1] += s
        else:
            merged.append(s)
    return merged


def wrap(s, limit=24):
    if len(s) <= limit:
        return [s]
    best = -1
    for i in range(8, min(len(s) - 4, limit + 2)):
        if s[i] in "、―" or (s[i] in "はがをにのでと" and i + 1 < len(s) and s[i + 1] not in "、。" and not ("ぁ" <= s[i + 1] <= "ゖ")):
            best = i
    if best < 0:
        best = limit - 1
    while best + 1 < len(s) and s[best + 1] == "―":
        best += 1
    return [s[: best + 1], s[best + 1:]]


# ---- subtitle events (timed proportionally to characters inside each line)
events = []
for ln in T["lines"]:
    chunks = split_text(ln["text"])
    total_chars = sum(len(c) for c in chunks)
    t0, dur = ln["start"], ln["end"] - ln["start"]
    for c in chunks:
        d = dur * len(c) / total_chars
        events.append({"start": t0, "end": t0 + d, "text": c, "cut": ln["cut"], "line": ln["text"]})
        t0 += d


def ts(sec):
    ms = int(round(sec * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


with open("subtitles.srt", "w") as f:
    for i, e in enumerate(events, 1):
        f.write(f"{i}\n{ts(e['start'])} --> {ts(e['end'])}\n" + "\n".join(wrap(e["text"])) + "\n\n")


CHAPTERS = ep.CHAPTERS
chap=dict(CHAPTERS); seen=set(); out=[]
for ln in T["lines"]:
    if ln["cut"] in chap and ln["cut"] not in seen:
        seen.add(ln["cut"]); s=0 if not out else ln["start"]
        out.append(f"{int(s//60)}:{int(s%60):02d} {chap[ln['cut']]}")
open("chapters.txt","w").write("\n".join(out)+"\n"); print("\n".join(out)); print(len(events),"subs")
