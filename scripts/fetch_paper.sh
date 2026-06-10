#!/usr/bin/env bash
# 重新抓取 2026 新高考 I 卷数学试卷（逐页 PNG）并合成 PDF
set -euo pipefail
cd "$(dirname "$0")/../paper"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
SRC="https://www.gk100.com/read_122151413.htm"   # 高考100 整理版（含答案解析）
PY="${PY:-/opt/conda/bin/python}"                  # 需含 img2pdf 的 python

echo "[1/3] 拉取来源页 …"
curl -sL -A "$UA" "$SRC" -o source.html

echo "[2/3] 下载逐页 PNG …"
mkdir -p gk100_pages; i=1
for u in $(grep -oE 'https://p1\.gk100\.com/article/20260608/[^"]+\.png' source.html); do
  curl -sL -A "$UA" -e "$SRC" "$u" -o "$(printf 'gk100_pages/page_%02d.png' $i)"
  i=$((i+1))
done
echo "  下载 $((i-1)) 页"

echo "[3/3] 合成 PDF …"
"$PY" - <<'PYEOF'
import img2pdf, glob
files=sorted(glob.glob('gk100_pages/page_*.png'))
open('2026_新高考I卷_数学_真题及解析.pdf','wb').write(img2pdf.convert(files))
print('  写入 PDF：', len(files), '页')
PYEOF
echo "完成 ✅"
