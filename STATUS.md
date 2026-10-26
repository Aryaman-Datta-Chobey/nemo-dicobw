# STATUS

**Current phase:** 0 — VM, disk, repo, environments
**Last updated:** 2026-10-26

## Last completed step
- Repo skeleton, `.gitignore`, `STATUS.md`, `EXPERIMENTS.md` created.

## Disk
- Boot: `/dev/sda1`, 97 GB (78 GB free).
- Data: `/dev/sdb`, GCP PersistentDisk `disk-20261023-053306`, 1000 GiB (1.07 TB). Below the ~1.5 TB peak in §3.1.5, so process **one corpus at a time**.
- Mount status: pending (see below).

## Blockers
- LICENSE is MIT; CLAUDE.md §3.3 says Apache-2.0. Waiting on the user's decision.

## Next action
- Mount `/dev/sdb` at `/mnt/data`, create the §3.2 layout, add the `~/.bashrc` exports.
- Add submodules and pin their commits; build the `dicow` and `nemo` envs.
