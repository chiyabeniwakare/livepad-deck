# LIVEPAD DECK

配信向けのポン出しサンプラー＆BGMデッキです。ブラウザで開くだけで使えます（インストール不要）。

**▶ アプリを開く：https://chiyabeniwakare.github.io/livepad-deck/**

## できること

- **SE DECK**：効果音のパッド（4×4、iPhoneは4×2）。MP3・WAVなどを割り当てたり、その場で録音（REC）して鳴らせます。キーボード（1234/QWER… またはテンキー）でも鳴らせます
- **BGM DECK**：BGMのプレイリスト。フォルダ分け、リピート（OFF／FOLDER／ALL／ONE）、クロスフェード
- **FX PAD**：指でなぞってかけるエフェクト12種類（FILTER・ECHO・GATE・PITCH・TAPE STOP・ROLL・REVERB・FREEZE・BACKSPIN・LO-FI・RISER・FLANGER）
- **EQ DECK・PITCH DECK・MIXER**：BGMの音質・テンポ・キー、音量、DUCK（BGMを一時的に下げる）、PANIC STOP
- **レイアウト**：パネルの大きさと配置を自由に変えて保存
- **Googleドライブ同期**（任意）：ログインすると、音と設定を自分のGoogleドライブに保存して、別の端末でも同じ内容を使えます

各パネルの「？」を押すと、図つきの使い方が出ます。

## おすすめの環境

- PC：Chrome または Edge の最新版
- iPhone・iPad：Safari で開いて **「ホーム画面に追加」** して使うのがおすすめです（アドレスバーが消えて広く使え、保存したデータも消えにくくなります）

## ご注意

- 登録した音や設定は、使っている端末のブラウザの中に保存されます。iPhone・iPad の Safari は、しばらく開かないサイトのデータを消すことがあるので、ホーム画面に追加するか、Googleでログインしてバックアップしておいてください
- 内蔵の効果音はアプリがその場で作っている音なので、配信で自由に使えます。自分で追加したBGM・効果音は、配信で流してよいものかご自身で確認してください
- 作者のサーバーはありません。音や設定が作者に送られることはありません（[プライバシーポリシー](https://chiyabeniwakare.github.io/livepad-deck/privacy.html)）

## 不具合の報告・要望

[GitHub の Issues](https://github.com/chiyabeniwakare/livepad-deck/issues) からお送りください。

---

## 開発メモ

| 場所 | 中身 |
|---|---|
| `_src/index.html` | 編集する元のファイル（ここだけを直す）。開発用の Tailwind（CDN）で直接開いても動く |
| `dev/` | テスト版：https://chiyabeniwakare.github.io/livepad-deck/dev/ （自動で作る） |
| `index.html` | 公開版（テスト版で確認したものをコピーする） |
| `_tools/` | ビルドの道具 |

```sh
cd _tools && npm install          # 初回だけ
python3 _tools/build.py           # _src → テスト版（dev/）を作る
python3 _tools/build.py --release # テスト版を、そのまま公開版（index.html）にする
```

- テスト版（dev/）は、保存データ（IndexedDB）と Googleドライブのフォルダ（「LIVEPAD DECK (dev)」）が公開版と別なので、公開版のデータには触りません。画面の左上に **DEV** と出ます
- `_` で始まるフォルダは GitHub Pages では公開されません
