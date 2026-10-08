# TOM-001 — Theorem Opportunity Map (Phase A)

Status: **SCOUTED / SELECT_FOR_AUDIT**  
Novelty: **NOT ESTABLISHED**  
Date: **2026-10-08**  
Issue: [#15](https://github.com/definitely-stable/Mathlab/issues/15)  
Source baseline: `main@9c0c76da987f0031d4aeef2a0de081306fe532b4`

## Why this program exists

The previous research process repeatedly promoted plausible mathematical ideas before checking for exact model reductions and strong existing theorems. TOM-001 reverses the process:

1. Identify an exact operation worth providing as a small Rust primitive.
2. Freeze a cost/model/guarantee contract.
3. Map the nearest known results and known impossibilities.
4. Attempt to falsify the claimed novelty and utility.
5. Only then select a theorem statement to prove.

An "opportunity" below is **not** a verified open problem, a conjecture with known positive evidence, or a promise of a crate.

This cross-domain exploration must not change the LENT-001 G2B protocol, acceptance markers, proof claims, or CI.

## Status vocabulary

- **KNOWN / STOP-BROAD**: the broad headline is already in prior art; narrower variants require a new audit.
- **SCOUT**: potentially interesting, but novelty and feasible mathematical target not established.
- **AUDIT-PRIORITY**: stronger combination of product operation and clear model questions; still no novelty conclusion.
- **CURRENT-RESEARCH**: independent program already has frozen model and evidence.
- **THEOREM-ELIGIBLE**: available only after source-level prior-art closure and explicit counterexample attempts. **No TOM-001 item is theorem-eligible yet.**

## Four research clusters / 14 candidate questions

Columns: **question** is the possible narrow advancement; **known boundary** is the strongest nearby primary work verified at abstract/model level; **kill test** is the fastest objection to investigate; **Rust primitive** is a proposed one-operation product, not an API commitment.

### A — Local verification, incremental reasoning, proof size

**O01 — Exact no-effect certificates in restricted bounded-fanin computational DAGs** — AUDIT-PRIORITY.

- Question: For a *specified* finite class of node functions and update patterns, characterize the minimum retained metadata \(s\) and cell probes \(t\) required to **accept all genuinely no-effect updates** while never accepting a change that alters the root. Distinguish verification time, metadata construction time, and update propagation.
- Known boundary: [Ramalingam, 1993](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/), [self-adjusting computation, 2006](https://doi.org/10.1016/j.entcs.2005.11.043), [differential execution, ECOOP 2025](https://doi.org/10.4230/LIPIcs.ECOOP.2025.20).
- Kill test: if a standard maintained sufficient statistic or existing dynamic algorithm already has the same \(s,t\), or if a trivial \(O(1)\) digest satisfies a weakened statement, reject the theorem.
- Rust operation: `certify_unchanged(old_metadata, input_delta)`; comparator: full recomputation, dependency-graph propagation, cached statistics.
- Formalize the **no-trivial-always-reject condition** before selecting any theorem.

**O02 — Minimal composition of no-effect certificates for overlapping batches** — AUDIT-PRIORITY.

- Question: For restricted DAGs and *specified overlap patterns*, can a joint exact certificate have provably smaller bit/probe cost than separately checking each update? Seek an information lower bound and constructive packing; count all shared metadata.
- Known boundary: [Change Actions](https://arxiv.org/abs/2002.05256), [Ramalingam 1993](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/), standard sharing of dependency paths.
- Kill test: union of overlapping tree paths or monoid associativity may explain the entire bound; check against existing batch/dynamic algorithms.
- Rust operation: `compose_certificates(a, b)`; comparator: verify each edit, union-of-path validation.

**O03 — Auditable persistent incremental-cache reuse** — SCOUT.

- Question: In a frozen crash/restart and I/O dependency model, can compact validation evidence detect omitted dynamic dependencies without rebuilding all tasks? Include adversarial filesystem changes and input nondeterminism explicitly.
- Known boundary: [Riker, USENIX ATC 2022](https://www.usenix.org/conference/atc22/presentation/curtsinger); dependency-aware build systems.
- Kill test: if complete dynamic tracing is necessary, certificate merely re-encodes the whole trace; if metadata is hash-based, don't call it information-theoretically exact.
- Rust operation: `verify_cache_reuse`; comparator: Riker, tracing and clean builds.

### B — Canonical dynamic representations and edit locality

**O04 — Local updates to strongly history-independent variable-length partitions** — AUDIT-PRIORITY.

- Question: Can a *precisely defined physical/canonical layout* support insertion, deletion, split and query while limiting moved bytes and retaining strict history independence? Seek a new lower bound or explicit construction only outside published models.
- Known boundary: [Bender et al., PODS 2024](https://doi.org/10.1145/3651609), [Buchbinder–Petrank 2006](https://doi.org/10.1016/j.ic.2005.11.001), [Hartline et al. 2005](https://www.microsoft.com/en-us/research/publication/characterizing-history-independent-data-structures/).
- Kill test: if canonicality concerns only logical nodes rather than actual bytes/pointers, problem can collapse to a textbook immutable tree; if fully physical, existing lower bounds may prohibit the target.
- Rust operation: `canonical_partition`; comparator: history-independent partitioning, balanced trees.

**O05 — Adversarially stable content boundaries including periodic runs** — SCOUT.

- Question: Is there a *non-overlapping guarantee* in a regime excluded or penalized by existing content-defined chunkers, covering minimum/maximum chunk size, propagation distance, deterministic adversary, and periodic strings simultaneously?
- Known boundary: [Chonkers, arXiv 2025](https://arxiv.org/abs/2509.11121), [Ellert–Kociumaka, STACS 2026](https://doi.org/10.4230/LIPIcs.STACS.2026.36).
- Kill test: reproduce Chonkers assumptions/theorem exactly; if the new bound is literally the known statement with different terminology, STOP.
- Rust operation: `update_boundaries`; comparator: Chonkers and established CDC.

**O06 — Canonical persistent rope with efficient split/concat and stable sharing** — SCOUT.

- Question: For a fixed serialization model, characterize tradeoff between structural sharing, canonical serialized representation, edit locality, and split/concat. State whether initial fixed randomness is allowed.
- Known boundary: [history-independent dynamic partitioning, 2024](https://doi.org/10.1145/3651609), [Chonkers/Yarn 2025](https://arxiv.org/abs/2509.11121).
- Kill test: canonical rope via deterministic balancing, hashing or order labels may already satisfy proposed targets; inspect physical-vs-logical definition.
- Rust operations: `split`, `concat`, `replace_range`.

**O07 — Edit-dynamic multi-scale synchronizing sets with shared retained state** — SCOUT.

- Question: For a set of scales \(T\), obtain update and memory bounds that account for cross-scale reuse, edits, and periodic inputs, versus reconstructing each \(\tau\)-set.
- Known boundary: [time-optimal construction of synchronizing sets, STACS 2026](https://doi.org/10.4230/LIPIcs.STACS.2026.36).
- Kill test: existing static optimality or dynamic synchronizing-set algorithms may settle the exact parameter regime; do not misstate the STACS result as an online update theorem.
- Rust operation: `update_sync_positions`; comparator: rebuild per scale.

### C — Dynamic data structures and exact string/query maintenance

**O08 — Update-pattern-sensitive exact query maintenance** — SCOUT.

- Question: Pick a named conjunctive-query class and update language (e.g., bounded runs of FIFO + arbitrary edits) *not already classified*, seek a sharp update/enumeration boundary.
- Known boundary: [Hu–Wang, PODS 2025](https://doi.org/10.1145/3725254), [Khamis et al., 2026](https://www.cs.ox.ac.uk/publications/publication17212-abstract.html).
- Kill test: existing FIFO/mixed-sequence dichotomy already settles it; no claim of novelty from just studying practical update patterns.
- Rust operation: `apply_delta` on a local materialized-view core.

**O09 — History-independent gap-entropy-aware ordered dictionary** — SCOUT.

- Question: Under an exact canonical-storage definition, can gap-entropy-sensitive encoding coexist with efficient updates and rank/select? Prove upper and lower bounds beyond separately known properties.
- Known boundary: [Blelloch–Hu–Kuszmaul–Liang–Zhou, arXiv Aug 2026](https://arxiv.org/abs/2608.06077), [HI dynamic partitioning 2024](https://doi.org/10.1145/3651609).
- Kill test: the 2026 paper already settles broad gap-encoding tradeoffs; check whether adding HI makes the regime impossible or already solved.
- Rust operation: `insert_rank`; comparator: published difference-encoded dictionaries.

**O12 — Adaptive-threshold exact dynamic weighted edit distance** — SCOUT.

- Question: For a precisely fixed allowed threshold-update schedule, can preprocessing/rebuild costs improve when the distance threshold \(k\) changes during execution?
- Known boundary: [Boneh–Gorbachev–Kociumaka, ESA 2025](https://doi.org/10.4230/LIPIcs.ESA.2025.45), [dynamic tree edit-distance hardness, 2025](https://arxiv.org/abs/2511.09842).
- Kill test: rebuild-at-powers-of-two or published threshold tradeoff may settle the claim; conditional lower bounds restrict gains.
- Rust operation: `update_distance`; comparator: fixed-\(k\) algorithm, rebuild strategy.

**O13 — Incrementally reusable authenticated multiproofs across versions** — SCOUT.

- Question: For a fixed hash-based tree and batch-update schedule, characterize minimal transmitted *new* authentication data and verifier work if the verifier retains prior proof nodes. Count trusted retained state and version linking.
- Known boundary: [Ethereum consensus SSZ multiproof spec](https://github.com/ethereum/consensus-specs/blob/master/ssz/merkle-proofs.md), standard Merkle multiproof path sharing.
- Kill test: path deduplication / cached node union may already give optimality; cryptographic collision resistance is not information-theoretic proof uniqueness.
- Rust operation: `verify_patch`; comparator: recomputed canonical multiproofs.

**O14 — Broad optimal dynamic succinct dictionaries** — KNOWN / STOP-BROAD.

- Broad space/update tradeoff is **not** a fresh target: [tight cell-probe lower bounds](https://www.cs.princeton.edu/~hy2/files/dynamic_succinct_dictionary_lower_bound.pdf); [gap-encoded dictionaries with matching bounds, Aug 2026](https://arxiv.org/abs/2608.06077).
- Reopen only with a specific new *additional* constraint and a demonstrated model gap.
- Rust comparator: ordinary dynamic dictionaries.

### D — Retained Mathlab finite-field program (not the focus of the new crate)

**O10 — Hard-support odd-characteristic signed-sum capacity** — CURRENT-RESEARCH.

- Question: find genuinely support-sensitive results for \(A_q^{set}(m,w,d)\) with \(q>2\), \(m>w\), signed separately bounded collisions, and new exponent/construction.
- Existing proof/evidence: [Mathlab G1B](LENT-001-G1B-AUDIT-03-FINAL.md), [G2A](LENT-001-G2A-EVIDENCE.md); next run [issue #14](https://github.com/definitely-stable/Mathlab/issues/14).
- Strong closest comparator: [Han–Yildiz–Hassibi 2026](https://arxiv.org/abs/2605.08644).
- Kill test: map to known signature/Bh / support-constrained codes for all fixed parameters; finite model separation **does not** imply asymptotic separation.
- Rust operation if later warranted: `apply_local_identity`; no current crate decision.

**O11 — Nested prefix families + bounded per-key update support** — SCOUT / DEPRIORITIZED.

- Question: is there an extra (nonzero) simultaneous competitive-ratio penalty *specifically* caused by nestedness combined with hard update support?
- Existing scope: [Mathlab open questions](OPEN-QUESTIONS.md) and [decision D007](DECISIONS.md).
- Kill test: pure nestedness is already deprioritized; avoid deriving a claimed new tax without a supported rate-compatible-code reduction.
- Rust operation: `extend_capacity`.

## Provisional shortlist — not a theorem decision

| Candidate | Why it survives initial scouting | Principal objection | Next falsification |
| --- | --- | --- | --- |
| **O01/O02** | Clearly testable certificate bit/probe tradeoff and small Rust operation | self-adjusting/change-action literature is extensive; trivial all-reject certificates | freeze a finite nontrivial function class and full-coverage rule; search exact maintained-state lower bounds |
| **O04/O06** | Clear canonical representation, update and sharing operation | strong HI has deep impossibility results; CDC/rope methods overlap | freeze bytes-vs-logical representation and physical movement measure; derive a counterexample pair |
| **O10** | Existing exact solver/witness/CI and model separation | signature and sparse coding are established prior art; Rust differentiation unclear | complete G2B, independently; no crossing milestone boundaries |

Ranking is **provisional** and subjective. No numerical novelty probability, fabricated confidence percentage, claimed theorem exponent, or publication promise is justified.

## Formal proof target template for the next gate

A proper next theorem candidate requires:

1. **Domain**: exact family \(\mathcal X_n\); admissible updates \(\Delta\); deterministic/randomized/adaptive adversary.
2. **Operation**: input and output of the Rust primitive; validity preconditions.
3. **Cost**: bit budget and layout, word/cell probes, construction/preprocessing, update/verification time, memory, amortized/worst-case; charge discarded work.
4. **Guarantee**: exact/worst-case or quantified error, explicit failure/fallback, and a non-vacuity/coverage condition.
5. **Known bound**: closest primary theorem copied with all side conditions.
6. **Potential improvement**: concrete inequality or existence claim that is not the same known result.
7. **Attack**: one minimal counterexample target and one model-reduction target.
8. **Practical gate**: comparator crate/algorithm, workload and acceptable memory/time range.

Do not promote an inequality of the form \(W=O(|A|+|\partial A|)\) unless the cost of **discovering** \(A,\partial A\), metadata creation and all verification probes is included. Do not assert a general lower bound if a trivial array or precomputed table is allowed by the model.

## Acceptance / next research slices

- **TOM-001-A (this file):** 14 candidate map, primary anchors, status discipline, product operation and falsification tests. **SCOUT MAP ONLY.**
- **TOM-001-B:** write source-to-claim matrix for O01/O02 and O04/O06; record exact theorem statements and model mismatches; select one or STOP.
- **TOM-001-C:** build tiny independent exact counterexample oracles on GitHub-hosted CI; no benchmark-only evidence promoted to theorem.
- **TOM-001-D:** after a mathematically plausible new gap survives, write 1 frozen proof target and establish a Rust prototype experiment.

## Research-to-product decision

- No new crate, release, issue series of speculative implementations, or preprint before the first proof/novelty gate.
- Keep LENT-001/G2B running independently; do not claim TOM supersedes or closes it.
- A negative novelty result is an accepted outcome.

**TOM-001 Phase A decision: SELECT_FOR_AUDIT (O01/O02; O04/O06), with O10 as existing independent evidence lane.**
