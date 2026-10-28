# メンテナンス事務局 LP 初校ソース（仮置き）

リポジトリ swo2026-maintenance ができるまでの一時保管（2026-10-28、ver1.0）。
できたら、このブランチの _src/ を新リポジトリの source ブランチに移す。

- 組み立て: python3 -I _src/build.py _src out/index.html
- 校正PDF用: python3 -I _src/build.py _src pdfsrc/index.html --comp（comp/95794004.jpg を pdfsrc/comp/ に置く。PIXTA透かし見本なので公開しない）
- 校正PDF: python3 _src/make_pdf.py file:///.../pdfsrc/index.html pdf
