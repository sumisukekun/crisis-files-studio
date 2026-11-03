"""ナレーション: VOICEVOX エンジン（HTTP）で全行を合成し、1本の WAV とタイミングを作る。

出力: build/<ep>/narration.wav, build/<ep>/timing.json
usage: python pipeline/tts.py ep11_onoda [--url http://localhost:50021]
"""
import argparse
import io
import json
import time
import urllib.parse
import urllib.request
import wave

import numpy as np

from common import GAPS, load

ap = argparse.ArgumentParser()
ap.add_argument("episode")
ap.add_argument("--url", default="http://localhost:50021")
ap.add_argument("--speaker", type=int, default=13)  # 青山龍星
a = ap.parse_args()
ep, work = load(a.episode)
SR, LEAD = 24000, 1.5
READ = getattr(ep, "READINGS", {})


def post(path, body=None, ctype="application/json"):
    req = urllib.request.Request(a.url + path, data=body, method="POST", headers={"Content-Type": ctype})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception:
            if i == 4:
                raise
            time.sleep(3)


def synth(text):
    for k, v in READ.items():
        text = text.replace(k, v)
    q = json.loads(post(f"/audio_query?speaker={a.speaker}&text={urllib.parse.quote(text)}", b""))
    q.update(speedScale=getattr(ep, "TTS_SPEED", 0.97), intonationScale=0.9, prePhonemeLength=0.05, postPhonemeLength=0.05,
             outputSamplingRate=SR, outputStereo=False)
    wav = post(f"/synthesis?speaker={a.speaker}", json.dumps(q).encode())
    with wave.open(io.BytesIO(wav)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)


chunks = [np.zeros(int(SR * LEAD), np.int16)]
t, lines = LEAD, []
for i, (cut, text, pause, _prompt) in enumerate(ep.LINES):
    pcm = synth(text)
    dur = len(pcm) / SR
    lines.append({"cut": cut, "text": text, "start": round(t, 3), "end": round(t + dur, 3)})
    gap = GAPS[pause]
    chunks += [pcm, np.zeros(int(SR * gap), np.int16)]
    t += dur + gap
    print(f"{i + 1}/{len(ep.LINES)} {dur:.1f}s", flush=True)

with wave.open(f"{work}/narration.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(np.concatenate(chunks).tobytes())
json.dump({"total": round(t, 3), "lines": lines}, open(f"{work}/timing.json", "w"), ensure_ascii=False)
print(f"narration {t / 60:.1f} min")
