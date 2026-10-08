# HYP-002-C — hosted finite decoder evidence and product decision

Status: **PHASE-A ORACLE ACCEPTED; PROPOSE STOP_STANDALONE_DENSE_TWO_ID**.
Date 2026-10-08. This is a *research result*, not a Rust implementation.

## Verified CI run

GitHub Actions: https://github.com/definitely-stable/Mathlab/actions/runs/37768055325
Source HEAD: f87a6ab879f4f10acd52b8c39210bde3c97ecdc8.
Job succeeded; 77 unit tests passed; cross-repo catalog check accepted
61 entries. G0/G1A/G2A/G2B/TOM/HYP-001/HYP-002 gates remained green.

New executable markers:
- HYP002C_EXHAUSTIVE_ORACLE_PASS;
- HYP002C_OVER_CAPACITY_ALIAS_PASS;
- HYP002C_INDEX_FREE_DECODER_PASS;
- HYP002C_STORAGE_ACCOUNTING_PASS;
- HYP002C_PHASE_A_PASS;
- HYP002C_BENCHMARK_COMPLETED_NO_PERF_GATE.

Exhaustively checked 2 promised snapshots (rank 1, m=3),
79 (rank 2, m=9), and 6904 (rank 3, m=27). The rank-2
snapshot generator was checked against an independent
coordinate-count loop and the original G1A ASET oracle.
Affine point-pair completion was checked for every distinct
pair at ranks 1,2,3.

The separate 3-distinct-lines to 2-other-lines collision
was reproduced exactly. This proves cardinality overload
is not always detectable from the trit snapshot alone.
Missing deletes, duplicates and noncanonical IDs were
also covered by fail-closed checked-API regressions.

## Payload comparison (exact arithmetic, no performance claims)

| rank | m | V | information bound | ideal packed trits | 2-bit counters | two canonical IDs with occupancy |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 9 | 12 | 7 | 15 | 18 | 18 |
| 3 | 27 | 117 | 13 | 43 | 54 | 22 |
| 4 | 81 | 1080 | 20 | 129 | 162 | 30 |
| 5 | 243 | 9801 | 26 | 386 | 486 | 34 |

Information bound = ceil(log2(1+V+C(V,2))) bits.
Ideal trit bits = ceil(m*log2(3)).
Direct ID payload = 4*ceil(log2 m)+2 occupancy bits.
Physical Python tuples do not occupy these packed bit counts;
this table is **theoretical payload**, not measured heap usage.

## Non-gating hosted Python diagnostic

The same CI job executed fixed-warmup, five-round median-of-400
Python calls on each rank. Selected observed numbers from run:

| m | Python dense decode | checked dense delete | direct two-ID delete |
|---:|---:|---:|---:|
| 9 | 24,785 ns | 34,873 ns | 476 ns |
| 27 | 30,581 ns | 33,952 ns | 476 ns |
| 81 | 41,904 ns | 45,517 ns | 478 ns |
| 243 | 69,909 ns | 75,345 ns | 472 ns |

These diagnostic numbers are **NOT a Rust benchmark or
controlled cross-machine product performance claim**.
They reflect different operations/data layouts in Python,
including O(m) immutable-tuple copying by the sketch
implementation. The direct-ID comparator only removes
an entry from a two-element tuple. They are useful solely
for understanding this proof-of-concept implementation.
No speed threshold is an acceptance condition.

## Mathematical and product conclusion

A table-free index-free codec with deterministic O(m) full-state
decode exists under the **strict <=2 distinct active IDs** promise.

A separate source-state-only decoder **cannot** detect every
over-capacity update history because of the explicit 3->2 alias.
Unvalidated raw modulo-3 update cannot guarantee set semantics.

The asymptotic payload gap is Theta(m) bits for dense trits vs
O(log m) bits for storing two canonical line IDs. For the narrow
single-machine exact-two-ID set primitive, no demonstrated advantage
offsets this gap or the need for membership/capacity validation.

**Research/product gate: STOP_STANDALONE_DENSE_TWO_ID**.

Do not create a Rust crate or assert new scientific originality
from this decoder. Investigate a different enforceable workload
(e.g. algebraic merge or trusted bounded multi-party workflow)
only after giving end-to-end metadata, decoding and fallback costs;
or continue unrelated higher-potential Mathlab hypotheses.

Canonical analysis: HYP-002-C-AFFINE-DECODER-PROTOCOL.md.
Implementation: research/affine_two_id.py.
Tests: research/test_affine_two_id.py.
Diagnostics: research/bench_affine_two_id.py.
