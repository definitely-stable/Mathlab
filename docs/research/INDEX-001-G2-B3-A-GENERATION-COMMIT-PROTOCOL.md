# INDEX-001 G2-B3-A — frozen two-slot checkpoint/manifest crash-boundary reference

**Scope frozen 2026-10-09**. [Issue #146](https://github.com/definitely-stable/Mathlab/issues/146), parent [#126](https://github.com/definitely-stable/Mathlab/issues/126); predecessors [G2-B0/B1](INDEX-001-G2-B0-DURABILITY-PROTOCOL.md), [G2-B2-A](INDEX-001-G2-B2-A-APPLICATION-IO.md), [G2-B2-B](INDEX-001-G2-B2-B-CHECKPOINT-POLICY.md). **RESEARCH-ONLY, POSIX, ONE WRITER, NO REAL POWER-LOSS/DISK/NAND VALIDATION, NO PRODUCTION OR RUST.**

## 1. New exact state grammar and safety predicate

- Finite exact latest-write-wins map of N uint32 cells. Two slot names `snapshot.0.bin`, `snapshot.1.bin` store **unchanged G2-B1** snapshot format `<4sQII> + 4*N bytes + CRC32`, length `S=24+4N`. Each slot is a *replaceable complete generation*, not a concurrent transaction protocol.
- `manifest.bin` is `<4sB3xQ> + <I CRC32>`, 20 bytes exactly: `IXM1`, active slot 0 or 1, uint64 snapshot LSN and CRC32 over 16 leading bytes. Reader **only** uses active slot selected by checksum-valid manifest, verifies snapshot CRC and **exact** LSN match. Absent/corrupt manifest or absent/mismatching active slot fails closed; inactive slot is **not** an automatic rollback candidate.
- `wal.bin` retains unchanged G2-B1 28-byte `IXW1` records. Strictly increasing complete record sequences; noncontiguous *newer* suffix fails closed; torn trailing record may be discarded only on reopen. Complete invalid CRC never ignored. Fully verified records `seq <= manifest.seq` are obsolete, skipped. Verified records > snapshot.seq are replayed as an exact full range update. **A valid but unacknowledged complete WAL update may appear upon restart**; operation is not automatically classified as committed.
- Only one writer and no secondary process reading/holding a slot during overwrite. "Generation pinning" is the active manifest snapshot name/LSN **across the operation**; long-lived concurrent readers/pins are not supported. A file's previous generation is not trusted for corruption recovery after WAL truncation.
- Path files may be inspected using `stat()`; that is an observation of application-visible bytes, not physical device pages, writeback, journal traffic, or SSD NAND writes.

## 2. Creation, update, checkpoint and garbage collection

**Initialize** only in an empty directory: write+fsync `snapshot.0.tmp`, rename to `snapshot.0.bin` and sync directory; create+fsync `wal.bin` and sync directory; create+fsync `manifest.tmp`, rename to `manifest.bin` and sync directory. A non-empty folder with no valid manifest is **not** silently initialized (interrupted initialization is a hard error). This reference does not handle interrupted creation automatically.

**Assign** nonempty range: WAL append exactly one record, fsync WAL, update in-memory and acknowledge. Fault gates `before_wal`, `after_wal_partial`, `after_wal_write`, `after_wal_sync`. No post-failure reuse without reopen.

**Checkpoint** when latest seq differs from manifest LSN:
1. Encode current state into inactive slot temp `snapshot.{1-active}.tmp`, fully write and fsync; fault gates after partial write and fsync.
2. Atomic same-dir replace into `snapshot.{1-active}.bin` followed by `fsync(directory)`; fault gates after replace and directory sync. Active slot **still pinned to old generation**.
3. Write+fsync a new `manifest.tmp`, containing inactive slot index and new seq; atomic replace to `manifest.bin`, `fsync(directory)`; fault gates after partial write/fsync/replace/directory sync. This manifest switch is the **visibility pivot** in the actual POSIX directory view; the protocol waits for directory fsync before WAL is truncated.
4. Truncate the WAL to zero and fsync it, then return. Since all acknowledged in-memory updates are now in the manifest-selected verified snapshot, a successful truncate cannot lose them under the stated ordered-file-sync assumption. Inject fault after truncation.
5. Inactive slot persists until explicit `gc_inactive()`. Only the **not-selected** slot may be unlinked, followed by `fsync(directory)`. Inject fault before unlink, after unlink and after directory sync. An obsolete temp is retained for forensic observation, never used for recovery; optional manual cleanup is outside this initial reference.

**Critical invariant (conditional on the frozen POSIX sequence):** before durable manifest switch, the old active generation **and full WAL** remain; after switch+dirsync, the new full verified generation exists before WAL truncation. A crash at any named application boundary preserves all previously acknowledged range updates in the observable reference filesystem. Valid unacknowledged WAL suffix may be observed whole-or-none. These are **test-model guarantees only**; no simulated exception can establish real power-failure ordering.

## 3. Observable models and accounting

- Separate `snapshot_written`, `manifest_written` and `wal_written`: actual returned `os.write` lengths, no same byte double counted. The `manifest_written` **20 bytes are additional** to G2-B1; for successful no-fault U updates and C nonempty checkpoints (no GC writes), `W_2gen=(1+C)*(S+20)+28*U`. Initial `wal.bin` is zero bytes. A checkpoint full snapshot plus manifest is `S+20`, not just `S`.
- Recovery reading includes one snapshot, one manifest and full *stale or active* WAL file, even if replay ignores obsolete frames; classify snapshot/manifest/WAL read bytes separately. `fsync` files/directories, unlinks, renames, WAL truncations, and temporary occupancy are distinct event counters. Removal/truncate may cause non-zero filesystem/device writes not represented by `os.write` bytes.
- After successful checkpoint with retained prior slot: `snapshot.active=S`, `snapshot.inactive=S`, `manifest=20`, `WAL=0`. After optional `gc_inactive`, inactive slot removed. Before manifest rename two snapshots and WAL may coexist with a partial/full temp manifest. During snapshot staging old selected+inactive+temp may coexist; peak file footprint differs from the B2-B one-slot formula.
- Fail-closed corrupt *active* generation rather than pretending there is a valid fallback: the other slot lacks a full independently retained WAL suffix after compaction. A physically survivable rollback requires an additional archival/rotation contract, deferred to G2-B3-B.

## 4. Falsification and stronger theory gate

Unit tests must cover all named fault gates, two consecutive checkpoints (slot switching), WAL tails, partial/complete WAL corruptions, manifest checksum, slot/LSN binding, missing active snapshot, unsafe initialization, no-op updates and GC stages. A completely independent dense oracle verifies every `lookup` and every `scan` after restart; a checkpoint fault cannot revert acknowledged operations. The test does *not* claim device-level crash consistency or fault tolerance under malicious corruption.

**Primary research barriers / source intake (scope, not logical implications):**
- [PoWER Never Corrupts: Tool-Agnostic Verification of Crash Consistency and Corruption Detection (OSDI 2025)](https://www.usenix.org/conference/osdi25/technical-sessions): proof preconditions for recoverability and media-corruption detection. Our executable Python boundary tests do **not** inherit PoWER's formal verification.
- [Specifying and Checking File System Crash-Consistency Models (ASPLOS 2016)](https://doi.org/10.1145/2872362.2872406): POSIX does not specify universal crash outcomes; model-checking and implementation-specific litmus tests remain necessary.
- [Lightweight file system crash-consistency checking with differential fuzzing (2026)](https://doi.org/10.15514/ISPRAS-2026-38(1)-7): relevant adversarial differential crash testing, but its file-system-specific findings are **not** automatically transferred to our manifest protocol.

These primary works were discovered as missing from the current `main` literature cohort (204 entries on intake), not independently reproduced. Catalog import is deduplicated by canonical identity; HYP-105 PR #132 already reserves the next LIT-205 identity, so INDEX-001 sources must not overwrite it. All new literature must be imported with generated indexes and exact CI validation.

**B3-A acceptance:** exhaustive deterministic fault/restart correctness + counters on Ubuntu-hosted Research CI exact PR head. **B3-B separate:** hardware weakened ordering, independent rollback/commit marker, archival WAL and online adversarial checkpoint policies. **Status:** `GENERATION_REFERENCE_PENDING_CI`, `STRONG_DURABILITY_UNPROVED`, `ORIGINAL_THEOREM_UNPROVED`, `PRODUCTION_RUST_NO_GO`.
