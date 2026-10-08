# TOM-007 — Six strong hypotheses: falsification-first model and primary-source audit

Date: 2026-10-08 · [issue #68](https://github.com/definitely-stable/Mathlab/issues/68).
Research baseline: main \`dd83c142952b8bffaad3222d378a81197e759ee6\`.
**No original theorem claimed. No Rust crate authorized.** This is an input-to-G4 decision report, not publication clearance.
Precedence: [40-record no-repeat register](KNOWN-AND-STOPPED-RESEARCH.md), [TOM-001](TOM-001-OPPORTUNITY-MAP.md), [TOM-005](TOM-005-SEVEN-THEOREM-AUDIT.md), [TOM-006 STOP](TOM-006-EARLY-KILL-GATE.md) and [curated external literature](catalog/LITERATURE.md).

## Evidence vocabulary

- **PROVED_FINITE_WITNESS:** exact finite constructions, independently checkable with Python. No asymptotic generality implied.
- **KNOWN_BROAD:** original advertised scope already has source-level mathematical overlap.
- **MODEL_UNSPECIFIED:** expression not yet a theorem because computational model / cost / adversary is missing.
- **SCOUT_NARROW:** a specific follow-up could be novel, but full source-proof audit is still missing.
- **NO_GO_CURRENT_HEADLINE:** do not pursue this broad statement; NOT a universal impossibility result.
- **NOT_MEASURED:** no real workload/end-to-end or Rust evidence; therefore no standalone product GO.

## Decision matrix

| Candidate | Frozen useful question, NOT yet a theorem | Status / fastest kill | Next allowed scoped work |
| --- | --- | --- | --- |
| **HYP-101** exact BLAKE3 edit updates | For standard BLAKE3-256 with mandatory digest after every arbitrary insertion/deletion, what is the worst-case number of *fresh idealized compression-oracle calls* with S bits of maintained persistent auxiliary state and preprocessing charged? | **MODEL_UNSPECIFIED / SCOUT_NARROW**. The official specification gives 1024-byte fixed chunks, but shifted boundaries alone do NOT prove an Omega(n/1024) lower bound against precomputed alignments or other representations. See LIT-099? (Dynamic LCE is separately relevant); BLAKE3 original specification pinned below. | Define compression oracle / interface and complete time-space lower-bound hypothesis. Test shift invalidation vs exact recomputation under toy fixed-block model; forbid interpreting this as a BLAKE3 lower bound. |
| **HYP-102** periodic edit-local canonical partition | Under deterministic content-only canonicality, explicit boundary transport/matching and every chunk strictly within [b,2b], determine exact worst-case changed physical bytes and boundary positions for identical-symbol insertion. | **KNOWN_BROAD / SCOUT_NARROW**. Chonkers (LIT-009), 2024/2026 history-independent partition (LIT-007/008), 2026 synchronizing-set construction (LIT-012), dynamic LCE (new LIT-099) already address broad claims. The proposed R+E/b Omega(n/b) cannot be used without defining R and E against transformed coordinates. | Specify index normalization and periodic exception model; compare with existing theorem text. STOP if equivalent to their model. |
| **HYP-103** joint batch output/no-effect certificate | For finite Boolean DAGs of treewidth t, what minimal *verifier-visible* old values, probes, and shared witness bits certify a batch root, relative to an explicitly enumerated family of competitor algorithms? | **SCOUT_NARROW, NOT THEOREM-ELIGIBLE**. Naive per-edit no-effect certificates are **UNSOUND** for a batch (ML KR-017). Existing LIT-010 Differential Execution, LIT-013 Change Actions, LIT-032 Ramalingam, LIT-041 Certificates in Data Structures and newly imported Nominal Adapton / Riker constrain claims. Circular expression T=O((|Delta|+W*)poly(t,log n)) is not meaningful until W* is precisely defined and its computation cost is charged. | Narrow to read-once monotone circuits or bounded-treewidth DAG with externally declared function library; exhaustive proof minimization vs full recomputation, union-of-path and cached sufficient stats. |
| **HYP-104** snapshot-pinned pack compaction | What competitive lower bound remains for immutable physical packs when P snapshots have **different** live-object incidence matrices under charged read/write/space costs? | **NO_GO_CURRENT_HEADLINE on P-only penalty**: arbitrarily many identical snapshots need no additional packs or compaction. Compaction is a studied online optimization problem (new Bigtable Merge Compaction / Competitive Data-Structure Dynamization; LIT-097/098). | Freeze object-pack incidence matrix, pin lifetimes, pack addressability, reference sharing and offline comparator; seek difference based on version *diversity*, not count P. |
| **HYP-105** sparse signed-set vs linear independence | For fixed odd q, d>=3,w, does A_set(q,m,w,d)/A_lin(q,m,w,2d) grow unbounded as m->infinity? | **PROVED_FINITE_WITNESS / SCOUT_ASYMPTOTIC**. Trivial finite separation: GF(5), m=1, w=1, columns (1),(2) have 4 distinct subset sums yet are linearly dependent. This is NOT asymptotic growth. Lefmann 2005 (LIT-043), sparse support-constrained codes (LIT-006), B_h/separable work (LIT-003/004/005) must be compared definition-by-definition. | First compute/compare feasible finite values at q=5, d=3, w=2 or 3; locate exact B_h vs linear-dependence asymptotic results before theorem claims. Avoid exponential searches without a model gap. |
| **HYP-106** one-sided adaptive cardinality | With Q adaptively chosen queries, each item appearing at most r times, and transcript-dependent keyed observation, what conditional one-sided coverage bound survives? | **KNOWN_BROAD / SCOUT_NARROW**. Hardt–Woodruff (new LIT-100) gives adaptivity attack for linear sketches; Cohen–Singhal–Stemmer 2025 (new LIT-101) has robust cardinality guarantees with bounded item participation. Do NOT transfer a nonadaptive probability guarantee to adaptive sessions; PRF behavior is a separate computational assumption. | Only narrow to a named DeltaMeter parity/occupancy estimator with specified key secrecy, repeated participation and explicit conditional probability. No new standalone crate based on this broad headline. |

**Selection:** HYP-103 is a *conditional* best lead for independent product operation, HYP-101 for a hard oracle lower-bound direction, HYP-105 for pure mathematics. **None currently passes the theorem-originality gate**, so no Rust or standalone artifact is approved.

## Finite model falsification and its scope

Test file: \`research/test_tom007_hypotheses.py\` runs in existing hosted unittest discovery. It contains three deliberate independence checks and no external dependencies.

1. **HYP-103**: for Boolean AND at old input (0,0), flipping either bit alone preserves output zero, but flipping both yields one. Exhaustively enumerate all 16 two-input Boolean functions and all four old assignments; an independently bit-mask represented oracle must agree with table-function direct evaluation. This falsifies universal conjunction of singleton no-effect certificates; it does *not* disprove correct jointly-verified certificates.
2. **HYP-105**: over GF(5), columns [1,2] have subset sums {0,1,2,3} for all subsets of up to d=3, yet have a nonzero linear dependency (e.g. 2*1 - 1*2 =0 mod 5). Two independent algorithms (subset enumeration and coefficient enumeration) check each side. Proves finite strict separation, **not** the conjectured unbounded ratio as m grows.
3. **HYP-101**: in a *toy fixed-size byte-block input model*, insertion of one byte into an adversarial nonperiodic input changes many aligned leaf inputs; insertion into an all-a input does not. Test verifies counts against independent direct recomputation. This explains why a simple blanket argument "every insert destroys all suffix hashes" is invalid, **not** a claim about BLAKE3's true compression-oracle complexity.
4. **HYP-104**: for any P>=1 identical pinned snapshots, the distinct-object union (thus ideal shared logical content) is unchanged; this kills the notion that P by itself yields a positive universal physical-overhead lower bound. Compaction policy and pack layout remain a separate question.

No CI finite test proves a general asymptotic theorem, prevents all cryptographic attacks, or verifies an external publication.

## Source-to-claim reconciliation: existing papers not duplicated

| Already in 95-work catalog | Candidate(s) / older Mathlab cross-project gap | Decision |
| --- | --- | --- |
| LIT-007 and LIT-008 Bender et al. history-independent partitions (2024, 2026) | HYP-102 / TOM-O04/O06 | Broad partition novelty STOP; a physical-byte/adversarial-model variant needs quantified mismatch. |
| LIT-009 Chonkers (2025) and LIT-012 STACS 2026 synchronizing sets | HYP-102 / TOM-O05/O07, DELSK/ChunkShift | Do not claim first bounded-locality CDC; distinguish strict chunk size, periodic exceptions and updates. |
| LIT-010 differential execution, LIT-013 Change Actions, LIT-032 Bounded Incremental Computation, LIT-041 Certificates in Data Structures | HYP-103 / TOM-O01/O02/O03 | Existing delta semantics, incremental DAGs and certifier lower bounds; only costed interactive joint certificates potentially different. |
| LIT-043 Lefmann 2005, LIT-006 2026 support-constrained codes, LIT-003/004/005 separable/union-free | HYP-105 / LENT/HYP-001/002 | Broad 2-cell/3-cell exponent already known; do not claim 2-column finite gap as new theorem. |
| LIT-072 STOC 2026 cell-probe natural-proof barriers and LIT-095 ICALP 2026 pure DP limits | HYP-101/103/104 | Formal model must match; statements are conditional/limited and not transferred wholesale. |
| LIT-068 ITCS 2026 incrementally verifiable computation | HYP-103 / TOM-003 | Updatable arguments are cryptographic proof objects; they are **not** exact information-theoretic DAG certificates. |
| LIT-087 EuroSys 2026 rolling hash reuse | HYP-102 / DELSK/ChunkShift and TOM-006 | Hash-reuse itself is already prior art. |
| LIT-025, LIT-027 and LIT-042 streaming/cardinality/reconciliation | HYP-106 / DeltaMeter | Different promise models; no direct theorem transfer from a static estimator. |

## Newly identified primary sources (unique canonical IDs; catalog entries below are generated)

- **LIT-096:** Hammer et al., [Incremental Computation with Names](https://arxiv.org/abs/1503.07792) (2015). OOPSLA Nominal Adapton: explicit names, from-scratch consistency; not a new minimal shared batch witness theorem.
- **LIT-097:** Mathieu et al., [Bigtable Merge Compaction](https://arxiv.org/abs/1407.3008) (2014; later revised). Online file-merge policy competitive analysis; overlap with HYP-104 and previous Mathlab compaction/storage opportunities.
- **LIT-098:** Mathieu et al., [Competitive Data-Structure Dynamization](https://arxiv.org/abs/2011.02615) (2020). Online weighted set cover/merge cost under varying read rates; not immutable-packs-with-pins.
- **LIT-099:** Albert, [Longest Common Extension of a Dynamic String in Parallel Constant Time](https://doi.org/10.4230/LIPIcs.CPM.2026.20) (2026). String synchronizing hierarchy and updates, not a proof of global canonical CDC lower bound.
- **LIT-100:** Hardt–Woodruff, [How Robust are Linear Sketches to Adaptive Inputs?](https://arxiv.org/abs/1211.1056) (2012 preprint, STOC 2013). Adversarial linear sketch failure; not universally all non-linear/keyed estimators.
- **LIT-101:** Cohen–Singhal–Stemmer, [Breaking the Quadratic Barrier: Robust Cardinality Sketches for Adaptive Queries](https://proceedings.mlr.press/v267/cohen25c.html) (ICML 2025). Bounded participation; scope differs from DeltaMeter one-sided parity and security game.
- **LIT-102:** Curtsinger–Barowy, [Riker: Always-Correct and Fast Incremental Builds from Simple Specifications](https://www.usenix.org/conference/atc22/presentation/curtsinger) (2022). Fully tracked filesystem dependencies; doesn't solve optimal Boolean DAG witness size.

**BLAKE3 authoritative specification (not a separately dated 2026 scientific finding):** [BLAKE3-team/BLAKE3-specs](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.tex), chunk length 1024. The specification is the normative compression/tree model; any oracle lower-bound must use its *exact* semantics or explicitly declare an idealized substitute. It is linked directly here rather than assigned an invented paper DOI.

**Additional previously studied source overlap:** [Riker 2022](https://www.usenix.org/conference/atc22/presentation/curtsinger) supplies a stronger comparator for TOM-O03 persistent cache reuse; [Bigtable Merge Compaction](https://arxiv.org/abs/1407.3008) and [Competitive Data-Structure Dynamization](https://arxiv.org/abs/2011.02615) fill the online-compaction gap absent in earlier TOM-O04 notes; [Nominal Adapton](https://arxiv.org/abs/1503.07792) closes a source omission in TOM-O01/O02. These are metadata and model comparisons, **not** a complete audit of full proofs.

## Decision / strict next actions

1. **Freeze** the exact verifier/oracle model for HYP-103, else downgrade to DEFER.
2. **Evaluate** the asymptotic HYP-105 against exact source theorems before larger SAT/finite-field work.
3. **Audit** HYP-101 only in a named black-box compression-oracle model; hash tree precomputation is charged.
4. **Stop broad HYP-102/104/106 headlines** until strict source-model mismatch plus product operation is shown.
5. No selected theorem, no G4 claim, no Rust; close TOM-007 only for *scouting/sourcing* when full CI and review pass. A separate issue must be opened for a genuinely eligible narrowly defined theorem.

Existing 40 historical known/STOP records, 61 cross-repository internal research records, LENT/ASET math, TOM-006 and external product repos must stay unchanged.
