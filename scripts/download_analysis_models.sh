#!/usr/bin/env bash
# Speaker-embedding models used ONLY for error analysis (voice similarity of merged / split
# speakers), never for training or the submitted system. Appends their pins to
# results/model_shas.md. Declare them in challenge resource lists if that ever changes.
#   - nvidia/speakerverification_en_titanet_large (CC-BY-4.0), HF, pinned commit
#   - 3D-Speaker CAM++ iic/speech_campplus_sv_zh-cn_16k-common (Apache-2.0), ModelScope tag v2.0.2,
#     sha256-verified; model code from github.com/modelscope/3D-Speaker (Apache-2.0) at a pinned commit
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
DATA=${DATA:-/mnt/data}
export HF_HOME=${HF_HOME:-$DATA/hf_cache}
set -a; source "$REPO/.env"; set +a
PY=$HOME/miniforge3/envs/nemo/bin/python
HF=$HOME/miniforge3/envs/nemo/bin/hf
OUT=$REPO/results/model_shas.md

TITANET=nvidia/speakerverification_en_titanet_large
sha=$("$PY" -I -c "from huggingface_hub import HfApi;print(HfApi().model_info('$TITANET').sha)")
tdir=$DATA/models/${TITANET/\//__}
echo "==> $TITANET @ $sha"
"$HF" download "$TITANET" --revision "$sha" --local-dir "$tdir"

CAMPP=iic/speech_campplus_sv_zh-cn_16k-common
CAMPP_REV=v2.0.2
cdir=$DATA/models/${CAMPP/\//__}
mkdir -p "$cdir"
api="https://modelscope.cn/api/v1/models/$CAMPP/repo"
for f in campplus_cn_common.bin config.yaml configuration.json README.md; do
  want=$(curl -sf "$api/files?Revision=$CAMPP_REV&Recursive=true" | "$PY" -I -c "
import sys, json
print(next(x['Sha256'] for x in json.load(sys.stdin)['Data']['Files'] if x['Path'] == '$f'))")
  if [ ! -f "$cdir/$f" ] || [ "$(sha256sum "$cdir/$f" | cut -d' ' -f1)" != "$want" ]; then
    curl -sfL -o "$cdir/$f" "$api?Revision=$CAMPP_REV&FilePath=$f"
  fi
  [ "$(sha256sum "$cdir/$f" | cut -d' ' -f1)" = "$want" ] || { echo "sha256 mismatch: $f"; exit 1; }
  echo "    verified $f"
done
echo "$CAMPP $CAMPP_REV" > "$cdir/REVISION"

SPK_COMMIT=065629c313eaf1a01c65c640c46d77e61e9607b4
SPK_SRC=$HOME/src/3D-Speaker
[ -d "$SPK_SRC/.git" ] || git clone -q https://github.com/modelscope/3D-Speaker "$SPK_SRC"
git -C "$SPK_SRC" fetch -q origin && git -C "$SPK_SRC" checkout -q "$SPK_COMMIT"

grep -q "^## Analysis-only models" "$OUT" || printf "\n## Analysis-only models (error analysis, not training)\n\n| Model | Pin | Local dir | Size |\n|---|---|---|---|\n" >> "$OUT"
sed -i "/speakerverification_en_titanet_large\|speech_campplus_sv_zh-cn\|3D-Speaker (model code)/d" "$OUT"
echo "| \`$TITANET\` (CC-BY-4.0) | \`$sha\` | \`$tdir\` | $(du -sh "$tdir" | cut -f1) |" >> "$OUT"
echo "| \`$CAMPP\` (ModelScope, Apache-2.0) | tag \`$CAMPP_REV\`, sha256-verified | \`$cdir\` | $(du -sh "$cdir" | cut -f1) |" >> "$OUT"
echo "| 3D-Speaker (model code) | \`$SPK_COMMIT\` | \`$SPK_SRC\` | – |" >> "$OUT"
echo "analysis models OK"
