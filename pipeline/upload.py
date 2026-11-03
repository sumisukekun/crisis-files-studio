"""YouTube へアップロード（本編＋ショート）。YouTube Data API v3。

必要な環境変数（GitHub の Secrets に登録）:
  YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN
usage:
  python pipeline/upload.py ep11_onoda                       # 非公開でアップロード
  python pipeline/upload.py ep11_onoda --publish-at 2026-11-05T19:00:00+09:00   # 予約公開
  python pipeline/upload.py ep11_onoda --only short           # ショートだけ
出力: build/<ep>/uploaded.json（動画ID）
※ 固定コメントの「固定」と、ショートの「関連動画」は API で設定できないため、公開後にブラウザで行う。
※ 審査（監査）前の API プロジェクトからアップロードした動画は非公開に固定される。審査が通るまでは
  --dry-run で中身を確認し、アップロードはブラウザで行う。
"""
import argparse
import json
import os
import sys

from common import load

ap = argparse.ArgumentParser()
ap.add_argument("episode")
ap.add_argument("--publish-at", default="")
ap.add_argument("--only", choices=["main", "short", "both"], default="both")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
ep, WORK = load(a.episode)
os.chdir(WORK)

chapters = open("chapters.txt").read().strip() if os.path.exists("chapters.txt") else ""
desc = ep.META["description"].replace("{CHAPTERS}", chapters)
status = {"privacyStatus": "private", "selfDeclaredMadeForKids": False}
if a.publish_at:
    status["publishAt"] = a.publish_at
done = json.load(open("uploaded.json")) if os.path.exists("uploaded.json") else {}

if a.dry_run:
    print(json.dumps({"title": ep.META["title"], "description": desc, "tags": ep.META["tags"], "status": status},
                     ensure_ascii=False, indent=1))
    sys.exit(0)

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

creds = Credentials(None, refresh_token=os.environ["YT_REFRESH_TOKEN"], token_uri="https://oauth2.googleapis.com/token",
                    client_id=os.environ["YT_CLIENT_ID"], client_secret=os.environ["YT_CLIENT_SECRET"],
                    scopes=["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.force-ssl"])
yt = build("youtube", "v3", credentials=creds)


def insert(path, title, description, tags):
    body = {"snippet": {"title": title, "description": description, "tags": tags, "categoryId": "24",
                        "defaultLanguage": "ja", "defaultAudioLanguage": "ja"}, "status": status}
    req = yt.videos().insert(part="snippet,status", body=body,
                             media_body=MediaFileUpload(path, chunksize=16 * 1024 * 1024, resumable=True))
    res = None
    while res is None:
        st, res = req.next_chunk()
        if st:
            print(f"  {int(st.progress() * 100)}%", flush=True)
    return res["id"]


if a.only in ("main", "both") and "main" not in done:
    vid = insert("episode_up.mp4", ep.META["title"], desc, ep.META["tags"])
    print("main:", vid)
    yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload("thumbnail.jpg")).execute()
    yt.captions().insert(part="snippet", body={"snippet": {"videoId": vid, "language": "ja", "name": "日本語"}},
                         media_body=MediaFileUpload("subtitles.srt")).execute()
    done["main"] = vid
    json.dump(done, open("uploaded.json", "w"))

if a.only in ("short", "both") and "short" not in done:
    main = done.get("main")
    first = f"▶ 本編（結末まで）：https://youtu.be/{main}" if main else "▶ 本編（結末まで）は近日公開"
    sid = insert("short.mp4", ep.SHORT["title"], first + "\n" + ep.SHORT["desc"], ep.META["tags"][:5])
    print("short:", sid)
    if main:
        yt.commentThreads().insert(part="snippet", body={"snippet": {"videoId": sid, "topLevelComment": {"snippet": {
            "textOriginal": f"▶ 本編（結末まで）はこちら https://youtu.be/{main}"}}}}).execute()
    done["short"] = sid
    json.dump(done, open("uploaded.json", "w"))

print(json.dumps(done))
