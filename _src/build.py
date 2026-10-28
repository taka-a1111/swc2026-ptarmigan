"""緊急対策PHP LP（Ver.1）を組み立てる
使い方: python3 -I build.py <srcフォルダ> <出力HTML> [--comp <見本画像の相対パス>]
--comp を付けると、画像エリアに PIXTA の見本（透かし入り）を仮に置いた校正PDF用のHTMLを出す。
納品・確認用URLのHTMLには付けない（見本画像は公開しない）。
"""
import sys, os, datetime

src, out = sys.argv[1], sys.argv[2]
comp = sys.argv[sys.argv.index('--comp') + 1] if '--comp' in sys.argv else None
BUILD_TAG = 'swc2026_ptarmigan_ver1.2 / 2026-10-28'

t = open(os.path.join(src, 'template.html'), encoding='utf-8').read()
css = open(os.path.join(src, 'base_v1.css'), encoding='utf-8').read() + open(os.path.join(src, 'add.css'), encoding='utf-8').read()
mailto = open(os.path.join(src, 'mailto.txt'), encoding='utf-8').read().strip()

def rep(s, old, new, n=1):
    c = s.count(old)
    if c != n:
        raise SystemExit(f'置換数が違う: {old[:40]!r} {c}件（期待 {n}）')
    return s.replace(old, new)

t = rep(t, '{{BUILD_TAG}}', BUILD_TAG)
t = rep(t, '{{CSS}}', css)
t = rep(t, '{{MAILTO}}', mailto)
if comp:
    img = (f'<img src="{comp}" alt="仮画像" class="on">'
           '<span class="comp-badge">仮画像：PIXTA 106556065 の見本（ご購入後に差し替え）</span>')
    t = rep(t, '{{TOP_IMG}}', img)
    t = rep(t, '/* ===== 緊急対策PHP：ここまで ===== */',
            '.media-slot img{object-fit:contain;background:#eef2f6;}\n'
            '.comp-badge{position:absolute;left:10px;top:10px;z-index:2;background:var(--red);color:#fff;'
            'font-size:13px;font-weight:800;padding:4px 10px;border-radius:4px;}\n'
            '/* ===== 緊急対策PHP：ここまで ===== */')
else:
    t = rep(t, '{{TOP_IMG}}', '')
assert '{{' not in t, '置き換え残り'
open(out, 'w', encoding='utf-8').write(t)
print('built', out, len(t), 'comp' if comp else 'deliver')
