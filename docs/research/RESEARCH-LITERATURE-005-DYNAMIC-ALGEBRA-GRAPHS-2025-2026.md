# RESEARCH-LITERATURE-005 — 2025–2026 dynamic algebra, graphs, online algorithms and immutable DAGs

**Source-scope audit:** 2026-10-09 · [IMPORT-005 issue #124](https://github.com/definitely-stable/Mathlab/issues/124) · parent commit `936a3205d82dc06ea7848eb004d0d97e9d491108` · 182 external works, 19 (2025) and 71 (2026) at original scouting baseline; the current merge base contains 186 external works after INDEX-001 G2-A LIT-183..186, making the 12 new IMPORT-005 papers LIT-187..198. All 12 exact publisher DOIs below absent in parent canonical identity and aliases. **No original theorem, proof replication, system performance reproduction, or product/crate acceptance is asserted.**

## Research thesis and source verification

Five 2025 and seven 2026 original, peer-reviewed LIPIcs publications from **SEA, ESA, ICALP, STACS, SWAT**. Publisher DOI, full original title, author lists, proceedings year and abstracts independently checked against official Dagstuhl publication pages, several with open HTML full text. **Claim strength: bibliographic identity and scoped author-reported theorem statements; NOT independently reproduced all lemmas/proofs.** A verified official abstract is not equivalent to `full_proof_verified`. Import metadata only, no PDF/code copying.

This widens Mathlab beyond DeltaMeter/reconciliation: online derandomization and optimization, algebraic matrix maintenance, exact vs approximate DAG/graph observability, temporal graph realizability, directed spectral sparsifiers, and compression-sensitive random access. The theorem family UCT-005 remains an **open** research program; LENT/HYP-105 no new exponent claim; INDEX-001 six previously imported papers LIT-177..182 are kept.

## Primary source table: model, result and transfer limits

| Proposed ID | Venue | Publication / original publisher | Exact research scope | Transfer boundary |
| --- | --- | --- | --- | --- |
| LIT-187 | 2025-SEA | [Incremental Reachability Index](https://doi.org/10.4230/LIPIcs.SEA.2025.9) | Append-only directed acyclic graph; nodes added in topological order; immutable old per-node index labels; query time O(1) or O(log n) with altered index size. | Not arbitrary edge deletions, not generic fully dynamic transitive closure, and no server/authentication guarantee. |
| LIT-188 | 2025-ESA-92 | [Incremental Maximization for a Broad Class of Objectives](https://doi.org/10.4230/LIPIcs.ESA.2025.92) | Monotone beta-accountable objective; construct one ordering competitive at each cardinality using a scaling algorithm, including monotone subadditive objectives. | Incremental solution prefixes and objective classes matter; not arbitrary update/delete workloads, not universal storage cost. |
| LIT-189 | 2025-ESA-93 | [Recognizing and Realizing Temporal Reachability Graphs](https://doi.org/10.4230/LIPIcs.ESA.2025.93) | Ask whether directed static reachability relation has a temporal graph realization with edge activation times; NP-complete in most model variants, with FPT by feedback edge set of a solid graph for undirected case. | Temporal paths require strict/non-strict time order; not ordinary static reachability, not live dynamic transitive reduction. |
| LIT-190 | 2025-ICALP-93 | [On Incremental Approximate Shortest Paths in Directed Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2025.93) | Sparse directed graphs with polynomially bounded nonnegative weights and edge insertions; deterministic and randomized (1+epsilon)-approximate APSP against adaptive adversary. | Insertion-only not fully dynamic; approximate distances not exact reachability, and total update bounds not memory/proof costs. |
| LIT-191 | 2025-STACS-18 | [Online Disjoint Set Covers: Randomization Is Not Necessary](https://doi.org/10.4230/LIPIcs.STACS.2025.18) | Hyperedges arrive online; choose colors to maximize disjoint complete covers, deterministic O(log^2 n) competitive via derandomizing potential function. | Online cover-decomposition maximization, not standard offline set cover, not caching or ASET vector-sum collision. |
| LIT-192 | 2026-ICALP-16 | [Fully Dynamic Algorithms for Coloring Triangle-Free Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2026.16) | Randomized update method on triangle-free maximum-degree Delta graphs with insertions and deletions, O(Delta/ln Delta) colors and Delta^{o(1)}log n amortized updates w.h.p. against adaptive adversary. | Triangle-free invariant and high-probability randomized bounds mandatory; entropy-compression proof != information-theoretic cache compression. |
| LIT-193 | 2026-ICALP-26 | [Fast Decremental Tree Sums in Forests](https://doi.org/10.4230/LIPIcs.ICALP.2026.26) | Edge-deletion-only weighted forest with path/component aggregate queries under a group model; dynamic tree cost and optimality carefully dependent on operation family. | Decremental forest is not general graph; aggregate operation group assumptions and query scope must be preserved before transplanting lower bounds. |
| LIT-194 | 2026-ICALP-44 | [Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction](https://doi.org/10.4230/LIPIcs.ICALP.2026.44) | Union-closure chain length of set system characterizes multiplicative-error reweighting/sparsification of atoms; generalizes contractions and weighted CSP sparsification. | Multiplicative approximation is not exact bounded-active subset-sum injectivity of ASET; atom weights not finite-field additive code coordinates. |
| LIT-195 | 2026-ICALP-45 | [Dynamic Rank, Basis, and Matching](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) | Maintain rank, basis, full-rank submatrices and dynamic graph matching; Õ(r^1.405) update bound for single matrix entry under specified algebraic operations, r=matrix rank. | Rank-sensitive algebraic work not per-byte writes, not arbitrary-word bit-probe bound, not dynamic forest rank over all rings. |
| LIT-196 | 2026-ICALP-157 | [Fully Dynamic Spectral and Cut Sparsifiers for Directed Graphs](https://doi.org/10.4230/LIPIcs.ICALP.2026.157) | Directed dynamic spectral approximation with degree-balance preservation and cut sparsifier for beta-balanced directed graphs; polylog update dependence on epsilon and beta with specified adversary. | Spectral, cut, and reachability are distinct guarantees; epsilon/beta balance and adversary assumptions essential; no cryptographic certificate. |
| LIT-197 | 2026-ESA-125 | [Incongruity-Sensitive Access to Highly Compressed Strings](https://doi.org/10.4230/LIPIcs.ESA.2026.125) | RLSLP or block-tree compressed strings; adaptive query time depends on longest repeated substring containing the requested character, with O(g_rl) or O(L) index space. | Static highly compressed representation and local repetitiveness, not arbitrary dynamic text updates or general global cache locality. |
| LIT-198 | 2026-SWAT-21 | [Dynamic MIS Revisited: Incremental, Fault Tolerant and Fully Dynamic](https://doi.org/10.4230/LIPIcs.SWAT.2026.21) | O(sqrt m) amortized insertion-only MIS; sensitivity after k deleted edges and O(m^{2/3}) fully dynamic amortized updates using black-box combination. | Maximal (not maximum) independent set; adaptive-adversary hardness under its exact conditional model does not imply oblivious-case hardness. |

## Existing-result audit and hypothesis impact

### DAG-002 — immutable-index/query frontier (OPEN)

**Anchor:** SEA 2025 [LIT-187], in comparison with INDEX-001 and dynamic reachability from IMPORT-004. `G=(V,E)` grows by topological append-only node insertion; legacy index entries may not change, but a separately priced `O(1)` mutable manifest is permitted only if specified. Cost tuple `(S` label bits, `P` query probes, `W` physical appended bytes, `T` preprocessing, `C` total verification/proof bytes, `R` rollback work). **Research question:** Is there a workload-specific strict Pareto gap between immutable labels and fully mutable indexes after bounding width and query universe? **Kill:** direct implication from chain-decomposition/labeling schemes; no claim that append-only indexing forces an original theorem. Test path graph, star, anti-chain and layered width-two DAG.

### GRAPH-002 — exact, approximate, temporal and authenticated observability (OPEN)

**Anchor:** ICALP'25 incremental APSP and ESA'25 temporal realizability plus ICALP'26 directed sparsifiers, dynamic coloring and MIS. Freeze distinct observables: reachability boolean, weighted approximate distance, directed cut, spectrum, temporal reachability, independent set, and separately priced signed verification. **Kill:** transferring an approximation-preserving sparsifier into an exact connectivity certificate or comparing unrelated adversary guarantees. Counterexamples include highly unbalanced directed cuts, temporal edges in wrong order, update-to-cycle and triangle insertion violating assumptions.

### ALG-001 — dynamic rank-sensitive maintenance (OPEN)

**Anchor:** ICALP'26 [LIT-195] rank r vs dimension n. Freeze field, matrix update type (entry vs column), arithmetic operations, randomized failure parameter, index/preprocessing size, and whether output basis materialization or just rank is needed. **Kill:** claiming rank-dependent arithmetic complexity is a new lower bound on writes/cell probes for online verified memory. Compare dense recomputation, low-rank updates and minimum observable output change.

### ONLINE-001 — deterministic online potential and all-prefix optimization (OPEN)

**Anchors:** STACS'25 deterministic disjoint cover and ESA'25 incremental maximization; contrast IMPORT-004 Markov paging/convex paging/submodular recourse. Exact comparator (offline OPT), online history, reward objective, randomization, and prefix constraint are mandatory. **Kill:** `O(log^2 n)` competitive cover ratio cannot be reinterpreted as online paging optimality or theorem on sparse ASET capacity.

### COMP-001 — local compressibility vs query cost (OPEN)

**Anchor:** ESA'26 [LIT-197], compare existing grammar self-index [LIT-050] and dynamic compressed index [LIT-179..181]. Cost model (grammar/RLSLP size, block tree length, random access probe cost, local repetition length, updates, preprocessing). **Kill:** static-compressed random access theorem erroneously promoted to dynamic read/write tradeoff. No claim that incompressibility automatically yields faster general-purpose cache.

## Immediate gates and preserved negative evidence

1. **Dedup:** canonical DOI, arXiv aliases and normalized original title; external papers form new records only if absent at exact main HEAD.
2. **Citation semantics:** `model_overlap` with a committed research note and per-origin `source_sha`; no invented explicit historical citation.
3. **Publication truth:** all source entries `publisher_abstract_checked`, `full_proof_verified=false`, `independent_reproduction=false`. The official HTML available for many studies is **not** a replayed proof.
4. **No-repeat:** exact original 182 identities and UCT/HYP/INDEX historical source SHA remain unchanged.
5. **CI:** regenerate `LITERATURE.md` and `LITERATURE-BY-RESEARCH.md`; exact-ID title pins, cohort assertions, duplicate mutation tests, GitHub-hosted `research` and `g2bb2` at exact PR HEAD; merge only if green and no conflict.
6. **Scientific decision:** metadata ACCEPT / novel scientific theorem NOT ESTABLISHED / no new Rust crate or production change.

## Canonical mapping and baseline note

Allocate contiguous `LIT-187..194` **only if the source catalog at implementation time still ends at LIT-182**. If a parallel PR merges first, rebase and reallocate without touching old IDs. The mapping is a discoverability aid, never grounds scientific novelty. Full author attribution and stable DOI are retained in each canonical entry.
