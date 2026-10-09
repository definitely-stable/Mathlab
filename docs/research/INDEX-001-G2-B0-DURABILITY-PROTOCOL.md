# INDEX-001 G2-B0/B1 — durable exact range map: frozen filesystem protocol

**Date:** 2026-10-09. **Parent:** [#117](https://github.com/definitely-stable/Mathlab/issues/117), [G2-B #126](https://github.com/definitely-stable/Mathlab/issues/126). Predecessors: G0/G1 #120 and synthetic page-cost G2-A #123. **RESEARCH REFERENCE ONLY / NOT PRODUCTION / NO NEW LOWER BOUND / NO RUST.**

## 1. Task and process assumptions
- One writer, no concurrent process access and no malicious storage. Logical domain `[0,N)` with integer symbols `0..2^32-1`; `1<=N<=2^32-1`. Half-open `assign(l,r,value)`, `lookup(pos)`, `scan(l,r)` use exact latest-write-wins. `l==r` is a no-op. Existing `ExactRangeMap` is reused for visible semantics; independent dense-array oracle checks correctness.
- Durable implementation is *WAL + whole-state checkpoint* with intentionally simple and costly writes; its purpose is a falsifier / reference comparator, not an improved index. A separate snapshot-only reference deliberately rewrites the full map on every operation.
- This stage assumes working `fsync(file)`, `os.replace()` atomic same-directory file replacement, and `fsync(directory)` on POSIX/Linux (GitHub-hosted Ubuntu). Neither power-loss hardware guarantees nor Windows portability are established. A named deterministic fault after an operation means the process stops at that boundary; bytes that have already been written may remain visible in the test filesystem. The harness cannot force actual power failure or reorder storage devices.
- Only an acknowledged update must be retained. An interrupted/unacknowledged update may be entirely absent or present after a restart, but the recovered value map must equal **one of the two entire states**, never a mixture. We do **not** allow further writes after injected failure without closing and reopening.

## 2. Binary on-disk grammar (little endian, no pickle)
- `snapshot.bin`: header `<4sQII` (magic `IXS1`, latest seq: uint64, N: uint32, reserved zero: uint32); array of N uint32 values; CRC32 `<I` over *header+payload*. Exact file length required; CRC failure is fatal (CorruptStore), never silently ignored.
- `wal.bin`: contiguous 28-byte records `<4sQIIII`: magic `IXW1`, seq uint64, lo/hi/value uint32, CRC32 uint32 over first 24 bytes. Records strictly increase in sequence. An incomplete trailing (<28 byte) suffix is discarded only at restart; a *complete* checksum-invalid record is fatal. Valid WAL suffix newer than snapshot must be contiguous from `snapshot.seq+1`.
- Supported sequence count must fit uint64. Reopen verifies snapshot universe size. No compression, versions, rollback proofs, encryption, authentication or external payload file.
- Uncommitted complete WAL records may be applied on restart: they are valid new states at the end of the durable prefix, never mixed/partial range updates. The next operation uses the recovered sequence.

## 3. Commit and checkpoint protocol
- Create: write and fsync a **whole** initial snapshot temp, atomic rename to `snapshot.bin`, fsync parent directory; only then return an opened store.
- `assign`: append exactly one complete WAL record, fsync WAL, then apply update in memory and acknowledge. Injected failpoints: `before_wal`, `after_wal_write`, `after_wal_sync`. Complete but unacknowledged records may survive; a torn trailing WAL record is discarded on recovery. No WAL read-cache claim.
- `checkpoint`: if there are updates since last snapshot, build whole dense image at latest committed seq, write an initial partial temp prefix (fault gate), write remainder, fsync temp, atomic replace, fsync directory, then truncate WAL and fsync WAL. Gates: `after_checkpoint_partial`, `after_checkpoint_sync`, `after_checkpoint_replace`, `after_checkpoint_dirsync`, `after_wal_truncate`. Reopen discards stale WAL record seq <= snap.seq only if structurally and checksum valid. This permits crash before WAL truncation without losing records.
- **Ordering invariant:** checkpoint WAL deletion happens *after* durable replacement of the snapshot. Do not move WAL truncation before durable snapshot installation; that would produce a acknowledged-update-loss counterexample.
- Restart: validate snapshot/CRC, parse WAL records, truncate incomplete suffix, ignore fully valid obsolete records, replay increasing suffix, then reopen WAL for append. A corrupt complete record, stale mismatch, duplicate/out-of-order newer record or snapshot corruption causes a hard failure.

## 4. Precisely defined accounting
- `written.wal`, `written.checkpoint_temp` count **actual lengths returned by `os.write`**. File shrink/truncate is tracked by event count, not falsely charged as bytes. No double inclusion of checkpoint bytes in total.
- `read.snapshot`, `read.wal`: application-level returned byte lengths (`Path.read_bytes`), **not physical page reads nor guaranteed system-call counts**. `fsync_files`, `fsync_dirs` count direct sync invocations, not physical flush durations.
- Checkpoint metadata bytes include the full materialized N*4 value image, framing and checksum. Separate `logical_blocks_assigned`; if nonzero, application write amplification is `(wal_bytes+checkpoint_bytes)/(4*logical_blocks_assigned)` in this *reference* model only. This is NOT SSD NAND write amplification, not a hardware lower bound.
- Instrumentation excludes filesystem internal metadata, copy-on-write filesystem snapshots, writeback cache, device controller, directory internals, compaction payload GC and memory allocation. Measure wall-clock only after the full correctness gate if needed.

## 5. Falsification matrix and acceptance
- Exact dense reference for all single/two-update binary traces over small N and nested/alternating sequences.
- Fault injection at every specified point for one update and checkpoint, restart each case, verify recovered *whole-state* map is in the permitted {old,new} states (checkpoint must preserve previously acknowledged state).
- Corrupt snapshot, full WAL checksum error, duplicate/gap sequence, torn WAL suffix; no silent acceptance of wrong complete data.
- Check per-category byte totals and file sizes; test whether read/write counts are independent of original payload device mechanics.
- `python -m unittest discover -s research -p "test_index001_durable.py"` and full GitHub-hosted Research workflow on **exact PR head**. No standalone claim of a new theorem or crash-proof filesystem.
- Future G2-B2: multi-generation atomically rotated snapshots, committed frame markers, multiwriter leases, compatibility/versioning, synthetic B2 versus measured B1 Pareto. G2-B0/B1 is intentionally one-writer reference only.

## 6. Scientific decision
`DURABLE_REFERENCE_CORRECTNESS_PENDING_CI`; `PHYSICAL_LOWER_BOUND_OPEN`; `NOVELTY_NOT_ESTABLISHED`; `PRODUCTION_AND_RUST_NO_GO`.
