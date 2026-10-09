# IMPORT-004 — 2025–2026: caching, online algorithms, dynamic graphs and incremental computation

**Snapshot:** 2026-10-09; **issue:** [#111](https://github.com/definitely-stable/Mathlab/issues/111); **scope:** source/model audit, not scientific discovery or deployment. **Historical baseline**: 155 canonical external works, of which 7 from 2025 and 63 from 2026, 14 external tracks at the first audit. **Current merge-base**: 159 works after UCT-005 G1 imports LIT-156..159; this IMPORT-004 adds exactly 17 different works as LIT-160..176 (176 in total). Recompute on later revisions. The publication selection below is **not** ranked by worldwide citation/impact and does **not** claim independent reproduction, full source proof verification or that paper measurements are universal.

## Research decision

Increase breadth beyond sparse sketches, ASET and patching. Recover missing **2025** mathematical foundations first; group **2026** engineering systems separately; import verified unique bibliographic identities and distinguish publisher-abstract evidence from independently proven claims. Preserve existing published/derived results, G5-C signed-trade open exponent, and [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) root-theorem research. Four memory-checking/vector-commitment novelty barriers belong to UCT-005 G1; no duplicate import under this project.

**Core source-level distinctions:**
1. Online paging competitive ratio depends on comparator, request model and objective: object-hit/byte-hit improvements on traces are not competitive bounds. Markov paging assumes requests sampled from a fixed Markov chain; adversarial paging does not.
2. Cache eviction, consistency and staleness are three separate objects. Bounded staleness observed at a service percentile is not linearizability and not a worst-case theorem.
3. Dynamic graph spanner approximates graph distances; transitive reduction preserves reachability; recourse counts representation modifications and is not equal to physical bytes written.
4. Exact DAG recomputation is not equivalent to detection of no-effect updates, cryptographically authenticated maintenance, proof generation or distributed invalidation. Count dependency discovery, recompute CPU, output bytes, storage, metadata, effect handling and verification separately.
5. RASK/HATS/LSM results concern storage and workload-specific physical indexes; they do not prove optimal Word-RAM/cell-probe bounds or HYP-105 asymptotic exponents.
6. Reported systems speedups from publication abstracts are **author-reported**; they are not independently reproduced by Mathlab.

## Selection table — exact publisher identities, testable model and transfer barrier

All URLs below are original publisher/official conference publication pages. For ACM STOC, the official TOC publishes full abstracts and article DOI links; the ACM full text may be access-restricted. USENIX and LIPIcs show abstracts and bibliography. **Verification level:** venue abstract + exact bibliographic identity; full proofs and systems evaluations not independently checked.

### A. Mathematical / algorithmic studies, 2025

| Cohort | Primary publication | Identifiable fact and concrete resource model | Research mapping and **non-transfer** |
|---|---|---|---|
| T25-01 | [Pabbaraju–Vakilian, *New and Improved Bounds for Markov Paging*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.123) | Dominating-distribution algorithm improves analysis to 2-competitive against optimal **in Markov request model**; authors also give 1.5907 lower for that algorithm. | CACHE-001, ML-004; not arbitrary/adaptive traces, object-size eviction or verification. |
| T25-02 | [Gupta–Kumar–Panigrahi, *Tight Results for Online Convex Paging*, STOC 2025](https://doi.org/10.1145/3717823.3718217) | Competitive bounds for convex norms of eviction counts and associated fairness objectives; direct integral design, fractional integrality-gap warning. | CACHE-001/ML-004; not plain miss-count ratio or measured systems speed. |
| T25-03 | [Dütting et al., *The Cost of Consistency: Submodular Maximization with Constant Recourse*, STOC 2025](https://doi.org/10.1145/3717823.3718131) | For online monotone submodular maximization with constant number of solution changes per step, authors give tight 2/3 general, 3/4 coverage information-theoretic approximation limits and a 0.51 randomized polynomial-time solution. | GRAPH-001/ML-004; recourse of abstract chosen set is not cache replacement cost or storage rewrite bytes. |
| T25-04 | [Kyng–Meierhans–Zöcklein, *A Simple Dynamic Spanner via APSP*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.111) | Dynamic approximate distance spanner using APSP with controlled total recourse under specified insertion/deletion sequences. | GRAPH-001/ML-004; approximate distances are not exact reachability or ASET signed trade exclusion. |
| T25-05 | [Goranci–Karczmarz–Momeni–Parotsidis, *Fully Dynamic Algorithms for Transitive Reduction*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.92) | Maintains reachability-preserving minimal subgraph under directed edge insertions/deletions; amortized O(m+n log n) algorithm and matrix-multiplication alternative. | GRAPH-001/DAG-001; algorithmic upper bounds, not certified authenticated answers or universal update lower bounds. |
| T25-06 | [Fine–Kaplan–Stemmer, *Minimizing Recourse in an Adaptive Balls and Bins Game*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.77) | Random placement in live bins incurs O(n log n) recourse against an adversary that observes assignments and kills bins. | GRAPH-001/CACHE-001; jobs/bins stochastic game is not an arbitrary failed distributed cache or a 0-failure worst-case theorem. |
| T25-07 | [Gorbachev–Kociumaka, *Bounded Edit Distance: Optimal Static and Dynamic Algorithms for Small Integer Weights*, STOC 2025](https://doi.org/10.1145/3717823.3718168) | In the bounded-distance regime gives deterministic dynamic unweighted edit distance with ~O(k) worst-case per single-character update; small **integer** edit weights have separate parameter dependence. | DAG-001/ML-004, DL-001; does not solve arbitrary weighted global delta compression. |

### B. Systems, cache and storage studies 2025–2026 (empirical)

| Cohort | Primary publication | Operational result / important design choice | Research mapping and **non-transfer** |
|---|---|---|---|
| S25-01 | [Zhou et al., *3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches*, FAST 2025](https://www.usenix.org/conference/fast25/presentation/zhou-wenbin) | Object- and byte-miss oriented learned eviction, sampling and bounded training overhead; authors evaluate on 4855 traces. | CACHE-001; not competitive-ratio theorem or optimality proof. |
| S25-02 | [Lyerly et al., *Skybridge: Bounded Staleness for Distributed Caches*, OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/lyerly) | Out-of-band replication stream reduces observed cache freshness lag with limited deployment footprint; published service percentile results. | CACHE-001/UCT-005 trust branch; percentile-specific empirical freshness is not universally bounded staleness or linearizability. |
| S25-03 | [Park et al., *Principles and Methodologies for Serial Performance Optimization*, OSDI 2025](https://www.usenix.org/conference/osdi25/presentation/park-sujin) | Taxonomy: remove, replace, reorder sequential work; batching, caching, precomputation, deferral, relaxation, contextualization, hardware specialization, layering. | DAG-001, INDEX-001/ML-004; taxonomy is not a new complexity lower bound. |
| S26-01 | [Li et al., *Merlin: An Efficient Adaptive Cache Eviction Algorithm via Fine-Grained Characterization*, OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/li-liujia) | Workload/object-level behavior classification, separated components, measured trace robustness. | CACHE-001; trace performance is not universal adversarial guarantee. |
| S26-02 | [Xia et al., *Learning-Augmented Heuristics: Simple Yet Smart, Robust and Interpretable Cache Eviction*, OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/xia) | LAH/S4-FIFO: learn occasional policy parameters offline/asynchronously and keep hot-path heuristic simple. | CACHE-001; model trained on finite production traces, no worst-case guarantee for every workload. |
| S26-03 | [Mao et al., *WriteGuards: Distributed Storage Support for Strongly Consistent Caches*, OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-writeguards) | Fenced writes at **key-range ownership** granularity prevent delayed-write anomaly and support described linearizable memory cache reads. | UCT-005/INDEX-001; a protocol under specific storage assumptions, not free authenticity, rollback proof or cryptographic security. |
| S26-04 | [Xie et al., *Incr: Faster Re-Execution via Bolt-On Incrementalization*, OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/xie-yizheng) | Dependency and effect analysis reuses intermediate shell-program results, including attention to non-idempotent steps. | DAG-001/HYP-101/TOM; reported execution speedup not a lower bound on incremental DAG maintenance. |
| S26-05 | [Yang et al., *FORGE: Mitigating Synchronization Amplification for Memory-Disaggregated Caching Systems*, OSDI 2026](https://www.usenix.org/conference/osdi26/presentation/yang-zhijun) | Group synchronization, contention reduction and lazy hotness metadata in disaggregated-memory cache. | CACHE-001/INDEX-001; RDMA/NIC-specific comparisons not abstract paging optimality. |
| S26-06 | [Zhao et al., *“Range as a Key” is the Key! Fast and Compact Cloud Block Store Index with RASK*, FAST 2026](https://www.usenix.org/conference/fast26/presentation/zhao) | Range-native tree index, log-structured leaves, range-aware splitting/merging; real workload tradeoff between RAM and maintenance. | INDEX-001/ML-004; contiguous block-write trace patterns, not arbitrary workloads or bit-probe lower bound. |
| S26-07 | [Ren et al., *Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage*, FAST 2026](https://www.usenix.org/conference/fast26/presentation/ren) | Co-schedules read placement and compaction rate control in distributed Cassandra-like LSM system. | INDEX-001/CACHE-001; operational queueing/performance objective, not universal optimal recourse theorem. |

**Dedup rule:** Compare **canonical DOI / proceedings paper ID** and normalized official title, including alternate versions. No new LIT IDs are justified by duplicate web titles/updated preprints. Original LIT-070..095 (2026 STOC/ICALP) and HYP-105 LIT-145..155 remain authoritative. The presence of related indexed papers (2026 dynamic matching, set cover, compressed rank/select, 2025 Brown–Erdős–Sós) is **NOT** an import of the 17 exact identities above.

## Fully priced research hypotheses and early kill gates

**CACHE-001 — cache capacity, adaptation and maintenance tradeoff (OPEN).**
Freeze sequence of requests `r_1..r_T`, object sizes `s_i`, mutable contents/version, cache bytes `M`, base-store fetch/latency cost, eviction cost, admission/prefetch, metadata space `B`, per-operation CPU `U`, recourse `R`, staleness/trust goals. Separate: (a) offline OPT; (b) adversarial online; (c) stationary Markov; (d) trace distributions. Compare LRU/FIFO/S3-FIFO, named published learned policies where artifacts exist; test a changing-hotset adversarial trace and a size-skew trace. **STOP** if alleged lower bound is Markov/convex paging reformulated, or supposed advantage depends on free prediction/history. Empirical performance alone => applied evidence only.

**DAG-001 — exact effect-sensitive incremental computation (OPEN).**
For a dependency DAG/Boolean circuit `G`, input revision sequence `x^t`, cached subset of nodes, observable output `f(x^t)`: charge `S` persisted values+indices; `Q` dependency discovery/source probes; `U` cache metadata writes/invalidations; `W` exact recomputation CPU; `E` side-effect log; `P` verification accesses and proof bytes if untrusted, and `T` preprocessing/program description. Test (i) cancellation diamond, (ii) shared subexpressions, (iii) hidden dependencies, (iv) non-idempotent effect, (v) cheap full recomputation. Distinguish from HYP-101 strict BLAKE3 canonical-cache bound and TOM-005 materialization-fanout lemma; read LIT-010, LIT-046, LIT-096, LIT-102 and Incr before novelty claim. **STOP** if statement is a change-propagation restatement or fails under saved metadata/free auxiliary state.

**GRAPH-001 — dynamic graph answer *plus separately authenticated witness* (OPEN).**
Freeze graph type, edge update adversary, answer service (reachability vs distance approximation, not both implicitly), witness correctness/error, client trust root, online horizon, `U_r,U_w`, recourse `R`, proof bytes `B`, verifier probes `P`, prover CPU `G`, and physical output changes `W`. Compare spanners, transitive reduction, graph-streaming proof bounds and UCT-005 memory checker. Small adversarial directed cycles and multi-update interaction cases; prove any claimed transfer. **STOP** if it factors into known recourse bounds + standard Merkle inclusion verification without strictly stronger same-model inequality.

**INDEX-001 — compact mutable range index with honest maintenance (OPEN).**
Input variable-sized nonoverlapping/overlapping range writes, reads, deletes, compaction and crash/recovery. Resource vector `(RAM-index bits, I/O reads, I/O bytes written, write amplification, update CPU, tail latency, persisted proof/state, recovery work)`; compare conventional block index, interval trees, RASK, and LSM. Construct adversarial alternating tiny-range writes and sequential stretches. **STOP** if claimed universal compactness relies on sequential-write-only workload or unpriced compaction/GC.

## Integration order and non-overlap

- **A (math 2025):** T25-01..07; priority is exact theorem assumptions, existing graph/recourse prior-art overlap, and falsification targets. Relation to LIT-072 natural-proofs data-structure barrier and LIT-073 compressed dictionaries is *methodological*, not implication.
- **B (cache systems):** S25-01..03, S26-01..03, S26-05; classify scientific claims as author-reported measured results and consistency conditions.
- **C (incremental/storage):** S26-04, S26-06..07; domain models; no automatic crate/product or HYP-101 extension.
- **UCT-005 G1:** defer memory checker/vector commitment identities to [#105](https://github.com/definitely-stable/Mathlab/issues/105), reconcile title/DOI when that slice lands; do not create parallel incompatible bibliography.

**Acceptance gate:** unique canonical IDs; author/publisher primary links; Russian scopes; no `full_proof_verified=true`; no `independent_reproduction=true`; regenerated literature indexes matching canonical JSON; no drift in known/STOP and HYP-105 results; GitHub-hosted CI exact PR SHA. No Lean theorem, Rust crate or scientific novelty authorization in this import.

## Canonical import mapping (first merged-ready metadata slice)

The 17 selection-table works above map **one-to-one** to canonical identities; no source work is repeated as an LIT paper under another new ID. The bibliography pins this audit through a per-origin `source_sha` pointing to the document-only commit that precedes the canonical JSON import; this preserves the upstream UCT-005 source pins.

| Cohort | Normative catalog ID | Cohort | Normative catalog ID |
| --- | --- | --- | --- |
| T25-01 | [LIT-160](catalog/LITERATURE.md#lit-156) | T25-02 | [LIT-161](catalog/LITERATURE.md#lit-157) |
| T25-03 | [LIT-162](catalog/LITERATURE.md#lit-158) | T25-04 | [LIT-163](catalog/LITERATURE.md#lit-159) |
| T25-05 | [LIT-164](catalog/LITERATURE.md#lit-160) | T25-06 | [LIT-165](catalog/LITERATURE.md#lit-161) |
| T25-07 | [LIT-166](catalog/LITERATURE.md#lit-162) | S25-01 | [LIT-167](catalog/LITERATURE.md#lit-163) |
| S25-02 | [LIT-168](catalog/LITERATURE.md#lit-164) | S25-03 | [LIT-169](catalog/LITERATURE.md#lit-165) |
| S26-01 | [LIT-170](catalog/LITERATURE.md#lit-166) | S26-02 | [LIT-171](catalog/LITERATURE.md#lit-167) |
| S26-03 | [LIT-172](catalog/LITERATURE.md#lit-168) | S26-04 | [LIT-173](catalog/LITERATURE.md#lit-169) |
| S26-05 | [LIT-174](catalog/LITERATURE.md#lit-170) | S26-06 | [LIT-175](catalog/LITERATURE.md#lit-171) |
| S26-07 | [LIT-176](catalog/LITERATURE.md#lit-172) | | |

**Decision:** `IMPORT_METADATA_ACCEPTABLE_IF_EXACT_HEAD_CI`; `THEOREM_NOVELTY_NOT_VERIFIED`; `NEW_RUST_NO_GO`. Follow-on literature must cite a source-level theorem, model, or benchmark and pass pre-import identity dedup. Four candidate programs above remain open and require separately funded/defined research slices; the catalog import itself is not their mathematical completion.
