# INDEX-001 G2-B2-A — exact application-level byte-cost baseline

**Date 2026-10-09**, [issue #137](https://github.com/definitely-stable/Mathlab/issues/137), parent [G2-B #126](https://github.com/definitely-stable/Mathlab/issues/126), root [#117](https://github.com/definitely-stable/Mathlab/issues/117). Requires accepted [durable protocol](INDEX-001-G2-B0-DURABILITY-PROTOCOL.md) and [implementation](../../research/index001_durable.py). G2-B2-A is one-writer **experimental cost accounting**, not a proven new theorem, deployed storage engine, physical NAND measurement or Rust API.

## 1. Operations, units and frozen workload
Let universe N=32, initial map zero, each trace contain U acknowledged nonempty range overwrites and L=sum_t(r_t-l_t) logically *assigned blocks* (including idempotent assignments). Each cell is encoded as uint32. The snapshot has S=20+4N+4=24+4N bytes, the WAL record is E=28 bytes. Every `os.write`-returned byte is recorded under one disjoint category; no true hardware page/block/page-cache data are inferred.

Compare (i) `SnapshotReference`: every overwrite rewrites full snapshot with atomic replace and `fsync`; (ii) `DurableRangeStore`: WAL-append every update plus full snapshot checkpoint after every threshold t updates; leave the final incomplete WAL tail until recovery. Both create and fsync an initial complete snapshot; both are tested using the **same independent dense oracle**, then close/reopen to verify durable logical state.

Frozen workloads, generated without randomness:
- `full_overwrite`: U=8 full N-block updates.
- `alternating_singletons`: U=12 one-block updates at modular steps.
- `nested_ranges`: U=10 contracting overwrite windows.
- `repeated_hot_region`: U=12 4-block overlapping hot-area updates.
Checkpoint policies t∈{1,4,16}. Snapshot-only comparator has no checkpoint tuning. Reporter: `python research/index001_workload_io.py [--json]`; independent numerical tests: `research/test_index001_workload_io.py`. No wall-clock benchmarks, external runners, optional packages or network dependency.

## 2. Complete same-model byte equations (elementary, not novel)
Under successful acknowledgments, no injected failures, no recovery mid-trace, no short-write retries and fixed full-image snapshots, `C_t=floor(U/t)` **nonempty** checkpoints occur, with terminal WAL tail `U mod t`. Direct accounting gives

```
W_snapshot(N,U) = S * (1+U)
W_WAL(N,U,t)    = S * (1+floor(U/t)) + E * U
R_restart(N,U,t)= S + E * (U mod t)
S = 24 + 4N, E = 28.
```

These are exact byte counts of `os.write` return values (and `Path.read_bytes` return values for `R_restart`) for the **two frozen reference implementations**, not asymptotic lower bounds for competing structures. The proof is counting complete frame writes, one initial image, each checkpoint image, and U fixed-size WAL frames. Truncate operations and `fsync` invocations are **separate event counters**, not magically assigned zero device work. A truncation may still force filesystem metadata writes. Read checks and time are separate.

For N=32, S=152:

| Updates U | Snapshot-only W | WAL t=1 | WAL t=4 | WAL t=16 |
| ---: | ---: | ---: | ---: | ---: |
| 8 | 1,368 | 1,592 | 680 | 376 |
| 10 | 1,672 | 1,952 | 736 | 432 |
| 12 | 1,976 | 2,312 | 944 | 488 |

All units above are **application bytes written in this reference protocol only**. In particular, WAL t=1 is worse than snapshot-only for this workload: adding a WAL append before *every* full checkpoint adds 28U bytes. Longer thresholds reduce checkpoint writes but retain more WAL bytes to replay, which can increase restart reading/work; `R_restart` is non-monotone in t when U is divisible by a threshold. There is no universally best compaction policy from this toy study.

## 3. Correctness / accepted result boundary
The module checks every acknowledged update with point and range queries against an independent dense-array oracle, then reopens the files for final recovery. It asserts exact closed-form write counts, checkpoint counts, WAL suffix size and recovery input byte counts. Unit tests include U=0, U=1, malformed ranges, duplicate/invalid thresholds and repeatability of the JSON report on fresh temporary filesystem directories.

**Scientific barriers:** existing LIT-098 (competitive dynamization), LIT-175 RASK, LIT-176 HATS, LIT-182 Moose/Smoose, LIT-184 C2LSM, LIT-185 ArceKV and LIT-186 RangeReduce already cover substantial compaction design space. G2-B2-A does not infer a new online competitive ratio, cell-probe lower bound or improvement over these published systems. The 186 canonical bibliographic identities are retained; no new unindexed distinct primary work was identified in this slice.

## 4. What remains
- B2-B: compare *actual file layout sizes, metadata growth, repeated clean restarts and fault/replay work* under explicitly frozen trace horizons, including compaction reads and temp-file lifecycle.
- B3: study configurable archival checkpoint generations, WAL commit marker semantics, process single-writer fencing and recovery without trusting a valid but unacknowledged WAL tail.
- B4: run actual I/O instrumentation / perf separately in controlled environments, distinguishing write syscalls from page cache, filesystem metadata and NAND writes; GitHub-hosted runner timing is not a publication-quality device benchmark.
- B5: only then attempt same-model nonfactorizing range-index lower bounds. Explicit STOP if reduced to known dynamic membership/buffering tradeoffs.

**Decision:** `APPLICATION_IO_EXACT_COST_BASELINE` (subject to full CI); `PHYSICAL_NAND_UNMEASURED`; `ORIGINAL_LOWER_BOUND_OPEN`; `NO_RUST`.
