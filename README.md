# crisis-files-studio

YouTube「クライシス・ファイル〜極限サバイバル劇画〜」の動画を、GitHub Actions で作るための置き場所です。

## 流れ（1本あたり）

| 工程 | スクリプト | 中身 |
|---|---|---|
| 台本 | `episodes/<名前>/episode.py` | ナレーション・画像プロンプト・章・サムネ・ショート・投稿文 |
| 画像 | `pipeline/images.py` | OpenAI 画像API で約200枚を並行生成（できた分は飛ばすので再実行で続きから） |
| 声 | `pipeline/tts.py` | VOICEVOX（青山龍星）でナレーションとタイミングを作る |
| 字幕・章 | `pipeline/subs.py` | `subtitles.srt` と `chapters.txt` |
| サムネ | `pipeline/thumb.py` | `thumbnail.jpg` |
| 本編 | `pipeline/assemble.py` | 画像＋声＋字幕タイミングから `episode_up.mp4`（圧縮済み） |
| ショート | `pipeline/short.py` | 縦型 60秒未満の `short.mp4` |
| 投稿 | `pipeline/upload.py` | YouTube API で非公開/予約アップロード、サムネ・字幕・ショートのコメントまで |

生成物は `build/<名前>/` に出ます（git には入れません）。

## 動かし方

GitHub の **Actions → build-episode → Run workflow** で

- `episode`: 例 `ep12_andes`
- `steps`: `images,tts,assemble,short`（投稿まで自動なら `,upload` を足す）
- `publish_at`: 予約公開する日時（空なら非公開）

完成した動画・サムネ・字幕は、実行結果ページの「Artifacts」からダウンロードできます。

## 必要な Secrets（Settings → Secrets and variables → Actions）

| 名前 | 用途 |
|---|---|
| `OPENAI_API_KEY` | 画像生成（有料） |
| `YT_CLIENT_ID` / `YT_CLIENT_SECRET` / `YT_REFRESH_TOKEN` | YouTube へのアップロード |

## 手作業が残るところ

- ショートの固定コメントを「固定」する、ショートの「関連動画」に本編を設定する（API が対応していないため）
- YouTube API の審査が通るまでは、API でアップロードした動画は非公開に固定される。審査中は Artifacts の動画をブラウザでアップロードする。

## クレジット

ナレーション：VOICEVOX:青山龍星
