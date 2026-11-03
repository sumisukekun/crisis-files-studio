"""画像: OpenAI 画像API で各行の絵を並行生成する。できている番号は飛ばすので、途中で止まっても再実行で続きから。

必要: 環境変数 OPENAI_API_KEY
出力: build/<ep>/images/001.jpg ...
usage: python pipeline/images.py ep11_onoda [--workers 6] [--only 5,12] [--model gpt-image-1] [--quality medium]
"""
import argparse
import base64
import io
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image

from common import load

ap = argparse.ArgumentParser()
ap.add_argument("episode")
ap.add_argument("--workers", type=int, default=6)
ap.add_argument("--only", default="")
ap.add_argument("--model", default=os.environ.get("IMAGE_MODEL", "gpt-image-1"))
ap.add_argument("--quality", default=os.environ.get("IMAGE_QUALITY", "medium"))
ap.add_argument("--size", default="1536x1024")
a = ap.parse_args()
ep, work = load(a.episode)

try:
    from openai import OpenAI
except ImportError:
    sys.exit("pip install openai")
client = OpenAI()

todo = [int(x) for x in a.only.split(",") if x] or list(range(1, len(ep.LINES) + 1))
todo = [n for n in todo if a.only or not os.path.exists(f"{work}/images/{n:03d}.jpg")]
print(f"{len(todo)} images to generate", flush=True)


def gen(n):
    prompt = (f"Style: {ep.STYLE}.\nScene ({ep.SCENE}): {ep.LINES[n - 1][3]}\n"
              "Landscape 16:9 composition. No text of any kind in the image.")
    for attempt in range(4):
        try:
            r = client.images.generate(model=a.model, prompt=prompt, size=a.size, quality=a.quality, n=1)
            im = Image.open(io.BytesIO(base64.b64decode(r.data[0].b64_json))).convert("RGB")
            im.save(f"{work}/images/{n:03d}.jpg", quality=92)
            return n, "ok"
        except Exception as e:  # rate limit / moderation / network
            msg = str(e)
            if "moderation" in msg or "safety" in msg:
                return n, "blocked: " + msg[:120]
            time.sleep(10 * (attempt + 1))
    return n, "failed"


bad = []
with ThreadPoolExecutor(a.workers) as ex:
    for f in as_completed([ex.submit(gen, n) for n in todo]):
        n, s = f.result()
        print(f"{n:03d} {s}", flush=True)
        if s != "ok":
            bad.append(n)
print("failed:", ",".join(map(str, sorted(bad))) or "none")
sys.exit(1 if bad else 0)
