#!/usr/bin/env bash
# Download, verify and (optionally) extract AISHELL-5 (OpenSLR 159, CC BY-SA 4.0).
#
#   bash scripts/download_aishell5.sh                 # all parts, download + verify
#   bash scripts/download_aishell5.sh --extract       # ... then extract into corpora/
#   PARTS="Dev Eval1" bash scripts/download_aishell5.sh --extract
#
# Tarballs go to $DATA/raw/aishell5/, extracted data to $DATA/corpora/aishell5/.
# OpenSLR publishes no checksums for this resource, so each tarball is checked with
# `pigz -t` and its sha256 is recorded in raw/aishell5/CHECKSUMS. Re-running is safe:
# aria2c resumes partial downloads and verified/extracted parts are skipped. The URLs
# each tarball came from are recorded in raw/aishell5/SOURCES.
# Tarballs are never deleted here. Run inside tmux:
#   tmux new -d -s dl-aishell5 "bash scripts/download_aishell5.sh --extract 2>&1 | tee logs/20261026-dl-aishell5.log"
set -euo pipefail
DATA=${DATA:-/mnt/data}
PARTS=${PARTS:-"Dev Eval1 Eval2 train noise"}   # small parts first
MIRRORS=(https://openslr.elda.org https://openslr.trmal.net)
RAW=$DATA/raw/aishell5
OUT=$DATA/corpora/aishell5
EXTRACT=0
[[ "${1:-}" == "--extract" ]] && EXTRACT=1

mkdir -p "$RAW" "$OUT"
touch "$RAW/CHECKSUMS"

# Keep the resource's licence/about page next to the data.
for f in about.html info.txt; do
  [ -s "$RAW/$f" ] || curl -fsSL -o "$RAW/$f" "${MIRRORS[0]}/resources/159/$f" || true
done

for p in $PARTS; do
  tgz=$p.tar.gz
  echo "==> $tgz"

  if ! grep -q "  $tgz\$" "$RAW/CHECKSUMS"; then
    # Mirrors are not always in sync (as of 2026-10, elda serves older Dev/Eval1/Eval2
    # than trmal). Use every mirror only if they agree; otherwise only the newest copy.
    declare -A meta=()
    for m in "${MIRRORS[@]}"; do
      h=$(curl -fsSI "$m/resources/159/$tgz" | tr -d '\r') || continue
      len=$(awk 'tolower($1)=="content-length:"{print $2}' <<<"$h")
      mod=$(awk -F': ' 'tolower($1)=="last-modified"{print $2}' <<<"$h")
      meta[$m]="$(date -d "$mod" +%s) $len $mod"
    done
    newest=$(for m in "${!meta[@]}"; do echo "${meta[$m]%% *} $m"; done | sort -n | tail -1 | cut -d' ' -f2)
    [ -n "$newest" ] || { echo "    no mirror reachable for $tgz" >&2; exit 1; }
    urls=()
    for m in "${!meta[@]}"; do
      if [ "$(cut -d' ' -f2 <<<"${meta[$m]}")" == "$(cut -d' ' -f2 <<<"${meta[$newest]}")" ] \
         && [ "$(cut -d' ' -f1 <<<"${meta[$m]}")" == "$(cut -d' ' -f1 <<<"${meta[$newest]}")" ]; then
        urls+=("$m/resources/159/$tgz")
      else
        echo "    WARN: $m serves a different $tgz (${meta[$m]#* }); using ${newest} (${meta[$newest]#* })"
      fi
    done
    unset meta
    aria2c -x8 -s8 -c --file-allocation=none --console-log-level=warn --summary-interval=60 \
      -d "$RAW" -o "$tgz" "${urls[@]}"
    echo "$tgz ${urls[*]}" >> "$RAW/SOURCES"
    echo "    verifying gzip stream"
    pigz -t "$RAW/$tgz"
    (cd "$RAW" && sha256sum "$tgz" >> CHECKSUMS)
    echo "    verified: $(grep "  $tgz\$" "$RAW/CHECKSUMS" | cut -c1-16)…"
  else
    echo "    already verified, skipping download"
  fi

  if (( EXTRACT )); then
    if [ -e "$OUT/.extracted_$p" ]; then
      echo "    already extracted"
    else
      echo "    extracting -> $OUT"
      tar -I pigz -xf "$RAW/$tgz" -C "$OUT"
      touch "$OUT/.extracted_$p"
    fi
  fi
done

du -sh "$RAW" "$OUT"
df -h "$DATA"
echo "aishell5 OK"
