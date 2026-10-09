# INDEX-001 G0/G1 — exact range assignment maps and fully priced maintenance

**Status (2026-10-09):** elementary logical lemmas only; original asymptotic physical-storage theorem **NOT PROVED**. [Issue #117](https://github.com/definitely-stable/Mathlab/issues/117) | predecessor [IMPORT-004 #111](https://github.com/definitely-stable/Mathlab/issues/111).

## 1. Frozen basic service
Let N>=1, finite alphabet Sigma of size a>=2, domain [0,N). State f:[0,N)->Sigma. An update assign(l,r,v), 0<=l<=r<=N, replaces f(i) by v for l<=i<r; empty update is a no-op. lookup(i) returns f(i). scan(l,r) returns **the exact maximal constant-run decomposition within [l,r)**. No overlapping historical stabbing-output semantics: old overwritten intervals are not query results. Valid maps contain no gaps, overlaps, zero-length runs, or adjacent runs with equal values. Logical run boundaries B(f)={i: 1<=i<N and f(i-1)!=f(i)} and k(f)=1+|B(f)|.

**Atomicity and crash durability are NOT part of this finite G0 service**; these belong to future G2 physical pages/WAL/fault model. The oracle is not an actual block index.

## 2. Elementary proven baseline (not scientific originality)
**L1:** For 1<=k<=N, number of maps with exactly k maximal binary runs is 2*C(N-1,k-1); choose k-1 internal boundaries and first bit. Hence any zero-error, standalone *complete encoding* of such a map needs >=ceil(log2(2*C(N-1,k-1))) bits. **NOT** an independently valid lower bound for RAM-only index when an auxiliary external store can be probed.

For a>=2 values, count = a*(a-1)^(k-1)*C(N-1,k-1), because adjacent run symbols must differ.

**L2:** For every nonempty assign(l,r,v), k(f_new)<=k(f_old)+2. Every old boundary strictly inside [l,r) disappears; only endpoints l,r (when internal) may appear. This is sharp (all zero, change single interior cell to one). Decreases can be arbitrarily larger than two, so the assertion |k_new-k_old|<=2 is **false**.

**L3:** A range overwrite only changes boundary presence at l and r or removes boundaries inside (l,r). Thus B(f_new) subseteq (B(f_old) outside (l,r)) union ({l,r} intersect (0,N)); whether endpoints become boundaries depends on neighbor symbols. This is a logical-support statement, **not** an upper bound on physical pages rewritten.

Independent code paths: run-based implementation in [index001_oracle.py](../../research/index001_oracle.py) and dense-array oracle in [test_index001.py](../../research/test_index001.py). Complete enumerations test counts, range writes/queries, canonicalization, nested edits, and adversarial alternation on small domains; no automated test proves asymptotics.

## 3. Full resource ledger for the next stage
Fix word bits w, page size B bytes, N, physical disk model, persistence semantics, allowed auxiliary indexes, cache warmth, read/write sequence and comparator. Report for each operation:
- S_RAM bits of indexes/cached metadata and S_disk bytes for live+dead metadata + WAL; charge allocation to the owner.
- Q_io physical page *reads* and B_read transferred bytes; worst-case, amortized and observed wall clock are different.
- B_write_fg + B_write_wal + B_write_compaction + B_write_other equals total physical write bytes, with mutually disjoint **accounting** categories. No second addition of compaction to total.
- C_cpu, recourse R_logical=|B(f_t) symmetric_difference B(f_(t-1))|, and R_physical as separately measured relocated bytes/pages.
- Space and writes for old versions, compaction and recovery cannot be hidden. p99 latency is an experiment, not an asymptotic theorem.

A cheap logical update may still force page/index/GC work. Conversely, a raw materialized array can offer O(1) point lookup without succinct metadata: do not invent a universal update/query tradeoff that it falsifies.

## 4. Original-source novelty barriers (source identity checked; full proofs not independently reconstructed)

| Identity | Source | Transfer boundary |
| --- | --- | --- |
| doi:10.1137/S009753970240481X | [Arge & Vitter, *Optimal External Memory Interval Management* (SIAM J. Comput. 2003)](https://doi.org/10.1137/S009753970240481X) | Dynamic interval stabbing reports all covering intervals; not latest-write-wins assignment/physical compaction. |
| doi:10.1137/110842211 | [Verbin & Zhang, *The Limits of Buffering: A Tight Lower Bound for Dynamic Membership in the External Memory Model* (2013)](https://doi.org/10.1137/110842211) | Exact external memory membership tradeoff with <1 amortized update IO; no free conversion to physical overwrite bytes. |
| doi:10.1109/FOCS57990.2023.00112 | [Li, Liang, Yu & Zhou, *Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries* (FOCS 2023)](https://doi.org/10.1109/FOCS57990.2023.00112) | Set membership/redundancy in cell probes, not range-map overwritten payload pages. |
| doi:10.1002/spe.3433 | [Navarro, *Practical Adaptive Dynamic Bitvectors* (2025)](https://doi.org/10.1002/spe.3433) | Rank/select query/update ratio adaptation; not overwrite-range compaction. Earlier working title 'Optimal Adaptive Dynamic Bitvectors' is a DIFFERENT 2024 study, do not misattribute. |
| arxiv:2608.06066 | [Blelloch, Hu, Kuszmaul, Li & Zhou, *Dynamic Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space* (2026)](https://arxiv.org/abs/2608.06066) | Fixed-alphabet dynamic symbol arrays under word-RAM compressed representation; no automatic durable-page / write amplification result. Preprint, not peer-reviewed claim. |
| doi:10.1145/3654978 | [*Structural Designs Meet Optimality: Exploring Optimized LSM-tree Structures in a Colossal Configuration Space* (Moose/Smoose, 2024)](https://doi.org/10.1145/3654978) | Flexible LSM design + reported RocksDB evaluation, not universal competitive lower bound. |

**Existing catalog — reuse without new identities**: history-independent dynamic partition LIT-007/008, gap-coded dynamic dictionary LIT-011, online competitive dynamization LIT-098, Pătraşcu–Demaine LIT-112, RASK FAST'26 LIT-175, HATS FAST'26 LIT-176. Crucially, SODA 2021 *Competitive Data-Structure Dynamization* already explicitly models compaction with batch inputs and variable read cost: any novel online-ratio claim must be stronger in the **same** model.

Verification level in this audit: primary publisher/author bibliographic pages and abstracts; source-proofs independently reconstructed = FALSE, benchmark reproduction = FALSE. Do not promote publisher use of 'optimal' into transfer to another task.

## 5. Falsification program
- **H1 / locality+recourse:** require a PAGE model, exact bytes and bounded-space conditions; counterexample with alternating one-cell writes, unchanged payload, and cheap raw overwrite.
- **H2 / adaptive runs-vs-overlay:** freeze common offline OPT, write bandwidth weights, memory headroom, switch costs and all queries; challenge with short-lived hotsets and nested overwrites. No generic competitive factor asserted.
- **H3 / joint cell-probe-physical cost:** search for tuples outside known transferred boundaries only; STOP if follows from Verbin–Zhang, Li et al, interval tree, or uncharged free state.
- **Physical G2 acceptance:** real durable implementation + complete WAL/compaction ledger + crash oracle before performance recommendations. G0/G1 must not be mislabeled production-readiness.

**Research decision:** LOGICAL_FOUNDATION_ACCEPTABLE_IF_INDEPENDENT_TESTS_PASS; PHYSICAL_LOWER_BOUND_OPEN; NEW_THEOREM_NOVELTY_NOT_VERIFIED; RUST_NO_GO.
