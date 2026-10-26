# STATUS

**Current phase:** 0 — VM, disk, repo, environments
**Last updated:** 2026-10-26

## Last completed step
- Repo skeleton, `.gitignore`, `STATUS.md`, `EXPERIMENTS.md` created; submodules pinned (see README).
- `/dev/sdb` formatted ext4 and mounted at `/mnt/data` via fstab (UUID `c8396159-02cf-432c-bfc4-2e23bc38ae6d`, `nofail`); `mount -a` verified. Data layout (`raw/ corpora/ audio16k/ refs/ manifests/ models/ exp/` + caches) created. `~/.bashrc` exports added.
- Envs built (Miniforge 26.7.2 at `~/miniforge3`); both see the A100. Locks in `env/requirements-lock-*.txt`.
  - `dicow`: Py 3.11, torch 2.7.0+cu128, transformers 4.55.0, flash-attn 2.7.4.post1 (prebuilt wheel), lhotse 1.28.0, meeteval 0.4.2.
  - `nemo`: Py 3.12, nemo-toolkit 3.0.0, torch 2.14.1; NeMo Speech scripts at `~/src/NeMo-Speech` @ v3.0.0 (`fd6a877`).

## Disk
- Boot: `/dev/sda1`, 97 GB (78 GB free).
- Data: `/dev/sdb`, GCP PersistentDisk `disk-20261023-053306`, 1000 GiB (1.07 TB). Below the ~1.5 TB peak if tarballs and extracted copies coexist, so process **one corpus at a time**.
- Mounted: `/mnt/data`, 984 GB usable. Backup of the old fstab: `/etc/fstab.bak.20261026`.

## Blockers
- (none)

## Next action
- `hf auth login` (user).
- Fill `third_party/TS-ASR-Whisper/configs/local_paths.sh` (SRC_ROOT, MANIFEST_DIR, PRETRAINED_CTC_MODELS_PATH, MUSAN_ROOT).
- Phase 1: download models (accept Nemotron terms on HF first). Phase 2: AISHELL-5 download.
