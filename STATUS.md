# STATUS

**Current phase:** 0 — VM, disk, repo, environments
**Last updated:** 2026-10-26

## Last completed step
- Repo skeleton, `.gitignore`, `STATUS.md`, `EXPERIMENTS.md` created; submodules pinned (see README).
- `/dev/sdb` formatted ext4 and mounted at `/mnt/data` via fstab (UUID `c8396159-02cf-432c-bfc4-2e23bc38ae6d`, `nofail`); `mount -a` verified. §3.2 layout created. `~/.bashrc` exports added.

## Disk
- Boot: `/dev/sda1`, 97 GB (78 GB free).
- Data: `/dev/sdb`, GCP PersistentDisk `disk-20261023-053306`, 1000 GiB (1.07 TB). Below the ~1.5 TB peak in §3.1.5, so process **one corpus at a time**.
- Mounted: `/mnt/data`, 984 GB usable. Backup of the old fstab: `/etc/fstab.bak.20261026`.

## Blockers
- LICENSE is MIT; CLAUDE.md §3.3 says Apache-2.0. Waiting on the user's decision.

## Next action
- Build the `dicow` and `nemo` envs.
