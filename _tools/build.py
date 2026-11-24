#!/usr/bin/env python3
"""LIVEPAD DECK のビルド

  python3 _tools/build.py            _src/index.html から テスト版（dev/）を作る
  python3 _tools/build.py --release  テスト版（dev/index.html）を、そのまま公開版（index.html）にコピーする

- 編集するのは _src/index.html だけ。dev/index.html と index.html は自動で作るファイル
- Tailwind の CSS は先に作って <style> として埋め込む（開発用の cdn.tailwindcss.com は使わない）
- 公開版は「テスト版で確認したもの」をそのままコピーするだけ（作り直さない）
- 初回だけ _tools で `npm install` が必要
"""
import datetime
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / '_tools'
SRC = ROOT / '_src' / 'index.html'
DEV_DIR = ROOT / 'dev'
JST = datetime.timezone(datetime.timedelta(hours=9))


def build_dev():
    src = SRC.read_text(encoding='utf-8')
    css = subprocess.run(
        ['npx', '--no-install', 'tailwindcss', '-c', str(TOOLS / 'tailwind.config.js'), '-i', str(TOOLS / 'in.css'), '--minify'],
        cwd=TOOLS, check=True, capture_output=True, text=True
    ).stdout
    if '.bg-accent-500' not in css:
        sys.exit('Tailwind の CSS がうまく作れていません')
    # 開発用の Tailwind（CDN と設定）を外し、作った CSS を <head> の最後に入れる
    # （CDN も実行時に <head> の最後へ足すので、ほかの <style> との優先順位が同じになる）
    out, n = re.subn(r'  <!-- TAILWIND-DEV：ここから[\s\S]*?<!-- TAILWIND-DEV：ここまで -->\n', '', src)
    if n != 1:
        sys.exit('TAILWIND-DEV の目印が見つかりません')
    out = out.replace('</head>', '  <style id="tailwind">' + css.strip() + '</style>\n</head>', 1)
    stamp = datetime.datetime.now(JST).strftime('%Y.%m.%d-%H%M')
    out = out.replace('__APP_BUILD__', stamp)
    out = out.replace('<!DOCTYPE html>', '<!DOCTYPE html>\n<!-- 自動で作ったファイルです。編集は _src/index.html に（python3 _tools/build.py） -->', 1)
    if 'cdn.tailwindcss.com' in out:
        sys.exit('cdn.tailwindcss.com が残っています')
    DEV_DIR.mkdir(exist_ok=True)
    (DEV_DIR / 'index.html').write_text(out, encoding='utf-8')
    shutil.copyfile(ROOT / 'privacy.html', DEV_DIR / 'privacy.html')
    print(f'テスト版を作りました: dev/index.html（{stamp}、CSS {len(css) // 1024}KB）')


def release():
    dev = DEV_DIR / 'index.html'
    if not dev.exists():
        sys.exit('先に python3 _tools/build.py でテスト版を作ってください')
    shutil.copyfile(dev, ROOT / 'index.html')
    stamp = re.search(r"const APP_BUILD = '([^']+)'", dev.read_text(encoding='utf-8'))
    print(f'公開版にしました: index.html（{stamp.group(1) if stamp else "?"}）')


if __name__ == '__main__':
    if '--release' in sys.argv:
        release()
    else:
        build_dev()
