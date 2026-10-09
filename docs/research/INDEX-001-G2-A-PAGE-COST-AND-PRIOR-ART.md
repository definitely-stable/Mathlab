# INDEX-001 G2-A — explicit page-cost simulation and compaction novelty audit

**As of 2026-10-09.** [Scoped task #121](https://github.com/definitely-stable/Mathlab/issues/121), parent [INDEX-001 #117](https://github.com/definitely-stable/Mathlab/issues/117), proved elementary [G0/G1 baseline](INDEX-001-G0-RANGE-MAP-FOUNDATION.md) (main PR #120).

**Status:** cost-simulation foundation (not a real filesystem or durable store), source identities audited against publisher/author pages, no independent full-paper proof or benchmark reproduction. H1/H3 lower bounds OPEN, H2 general novelty STOP, no Rust.

## 1. A page-model, not fabricated physical measurements
- Addresses [0,N), assignment [l,r) with latest-write-wins; integer metadata record r bytes, disk page B bytes, B divisible by r. Each record costs one slot, C=B/r records/page.
- Comparator A: materialized per-cell direct array with p blocks/page. Assign touches each overlapping physical page at most once, *including* redundant/idempotent overwrites (literal-write policy); lookup reads one cold page, scan reads all overlapping cold pages. No WAL/durability in this comparator.
- Comparator B: append-only overlay of range assignments over canonical maximal-run base. Each append modeled as a **whole-page** metadata journal write, no batching. Each lookup cold-scans overlay newest-first then base runs sequentially. Charge logical record probes independently from distinct cold pages visited. Each range scan conservatively reads all base and overlay pages (then exact virtual query). No cross-query page cache.
- B.compact(): read all base+overlay metadata pages once, canonicalize the latest-write-wins map, write an entire rounded-up new base metadata image as compaction bytes; drop overlay. No physical payload GC or authenticated recovery. Without pending entries compaction does no work.
- No claim that this upper-cost simulator matches RASK/RocksDB physical I/O; it is a **falsification comparator** showing sensitivity to workload and thresholds. Source data payload bytes, SSD FTL amplification, WAL durability and clock latency are not modeled. Never add compaction bytes to total twice.

## 2. Mathematical source/model barriers
| Publication identity | Scope | Non-transfer |
| --- | --- | --- |
| [doi:10.1007/s00224-025-10229-8](https://doi.org/10.1007/s00224-025-10229-8) | Navarro, *(Worst-case) Optimal Adaptive Dynamic Bitvectors*, Theory of Computing Systems, 2025; lower bound for rank/select/update under q query/update ratio and cell probes | Different from Navarro practical 2025 LIT-180, and not a physical compaction theorem. The 2024 arXiv:2405.15088 is an **earlier version of this journal work**; do not create a separate arXiv record. |
| [doi:10.1016/j.future.2026.108425](https://doi.org/10.1016/j.future.2026.108425) | Lu et al., *C2LSM: A configuration paradigm for efficient compaction in LSM-tree-based key-value stores*, FGCS 2026; per-level capacity/SSTable size and compaction timing modeling | Specific tunable LSM family and author evaluations, not a new universal cell-probe/physical-byte lower bound. |
| [doi:10.14778/3796195.3796208](https://doi.org/10.14778/3796195.3796208) | Liu–Xie–Luo, *ArceKV: Towards Workload-driven LSM-compactions for Key-Value Store Under Dynamic Workloads*, PVLDB 2026; workload-switching, ElasticLSM and compaction control | Direct engineering competitor for H2, includes adaptation overhead; does not prove optimality for arbitrary exact range-assignment indices. |
| [doi:10.1109/ICDE65706.2026.00194](https://doi.org/10.1109/ICDE65706.2026.00194) | Kaushik–Athanassoulis–Sarkar, *RangeReduce: Query-Driven LSM Compactions*, ICDE 2026; range-query work in multi-run LSM | Indexing a range *query* across SSTables is not an exact range-as-key overwrite API; empirical query/compaction gains are not general theorem guarantees. |

**Version bookkeeping:** Springer SPIRE 2024 [*Adaptive Dynamic Bitvectors*](https://doi.org/10.1007/978-3-031-72200-4_16) is preliminary to Navarro's **theoretical** 2025 worst-case-optimal line (LIT-183): the author identifies SPIRE 2024 as an earlier partial version of the theoretical journal study. The **practical** 2025 journal study remains independently identified as LIT-180 with its own performance/space regime. Re-check model and textual overlap before treating publications as separate mathematical lower bounds.

**Reuse existing works, not new IDs:** LIT-007/008 HI partition, LIT-011 dynamic gap dictionary, LIT-098 competitive dynamization, LIT-112 cell-probe, LIT-175 RASK, LIT-176 HATS, LIT-177..182 G0 sources.

## 3. Actual research decision
1. **H1**: a page/bytes lower bound cannot be inferred from the fact a range update changes at most two *new* logical boundaries; an overwrite can delete Theta(k) old boundaries. Fully loaded index movement is unproved.
2. **H2 broad generic adaptive compaction novelty: STOP.** 2024 Moose/Smoose, 2026 C2LSM, ArceKV, RangeReduce already optimize variants. A new contribution needs a new *same-model* exact overwrite cost theorem or decisively distinct measured Pareto curve.
3. **H3**: dynamic membership reduces to exact binary range service by singleton inserts assign(i,i+1,1) and membership=lookup(i). Thus any lower bound transferred from Verbin–Zhang is only valid under the identical external-memory and operation cost model; it **does not automatically imply** a bound on SSD physical written bytes.
4. Next G2-B: actual persistent page engine, WAL/crash-consistency oracle, fault-injection and measured read/write bytes, before adopting RASK comparisons or proposing a crate.

**Acceptance:** exact model, independent finite dense reference, nonnegative and disjoint counters, explicit cold-page treatment, no time/performance claim, source catalog regenerated with historical IDs preserved, hosted CI exact HEAD.
