"""共通: エピソード設定の読み込みと作業フォルダ。

各エピソードは episodes/<名前>/episode.py に
  LINES     [(カット番号, ナレーション, 間 's'|'l'|'c'|'x', 画像プロンプト), ...]
  CHAPTERS  [(カット番号, 章タイトル), ...]
  SCENE, STYLE, READINGS, STAMPS, THUMB, SHORT, META
を書く。生成物はすべて build/<名前>/ に出る（git には入れない）。
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAPS = {"s": 0.3, "l": 0.6, "c": 1.2, "x": 2.0}

FONT_DIR = "/usr/share/fonts/opentype/noto"
SERIF_BLACK = f"{FONT_DIR}/NotoSerifCJK-Black.ttc"
SERIF_BOLD = f"{FONT_DIR}/NotoSerifCJK-Bold.ttc"
SANS_BLACK = f"{FONT_DIR}/NotoSansCJK-Black.ttc"
SANS_BOLD = f"{FONT_DIR}/NotoSansCJK-Bold.ttc"


def load(name):
    """name: 'ep11_onoda' のようなフォルダ名。戻り値: (episodeモジュール, 作業フォルダ)"""
    path = os.path.join(ROOT, "episodes", name, "episode.py")
    if not os.path.exists(path):
        sys.exit(f"episode not found: {path}")
    spec = importlib.util.spec_from_file_location("episode", path)
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    work = os.path.join(ROOT, "build", name)
    os.makedirs(os.path.join(work, "images"), exist_ok=True)
    return ep, work
