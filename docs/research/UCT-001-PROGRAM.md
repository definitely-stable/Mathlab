# UCT-001 — Unified Resource-Constrained Distinguishability: research program

**Snapshot:** 2026-10-08. **Issue:** [#74](https://github.com/definitely-stable/Mathlab/issues/74). **Status:** RESEARCH_PROGRAM / NO ORIGINAL GENERAL THEOREM / NO RUST. The term "unified theory" is a working *program label*, not an accepted independent mathematical discipline. Scope: Mathlab only.

## Central problem
For evolving information, which combinations of representation bits, update writes, query probes, communication, certificate size, verification work and error budget are achievable, under **exactly specified** operation, adversarial, source-access and randomness contracts?

A family of known lower bounds is not itself a new theorem; any proposed joint bound must beat the conjunction of best existing bounds in a *single identical model* (or have an explicit formal reduction).

## Model families, deliberately separated
| ID | Mathematical object and costs | Established baseline | Novelty / feasibility gate |
|---|---|---|---|
| **UCT-A / UCT-001** | Finite transition graph, observables, q-ary representation, Hamming update locality w; separate space S, writes W, reads P, communication C, error epsilon | LENT-001 Hamming ball; Fredman–Saks 1989; Pătraşcu–Demaine 2006; Yi–Zhang 2010 | **SCOUT_NARROW**: a strict joint lower bound in one fixed model with an explicit stronger witness than individual bounds |
| **UCT-B / UCT-002** | Authenticated batch transform: persistent old state S, prover/verification work, bytes C, queries P, trust boundary and permitted soundness error | TOM-003; HYP-103 G0 classical certificate complexity; Wang–Yin static certificates; standard Merkle multiproofs | **STOP_BROAD**: no 'new' batch-certificate theory from the old-root probe characterization; REOPEN only for fully charged structural advantage |
| **UCT-C / UCT-003** | Source B, target T, precise codec and wire format, preprocessing/index/search/encoding costs, best-of-K trial protocol | TOM-005 A classical interval stop, TOM-006 positional q-gram bounds and adversarial weakness, Slepian–Wolf correlated coding (different probabilistic model) | **SCOUT_NARROW**: efficient admissible instance-specific floor with demonstrated nontrivial competitive tightness after *all* lookup work |
| **UCT-D / UCT-004** | Mergeable random representations; exact vs statistical vs computational guarantees; online/adaptive adversarial transcripts; fresh/key-reused randomness | DeltaMeter Energy/STRICT-COMPACT scope, Hardt–Woodruff adaptive sketch attack, union bound for fixed tests | **STOP_BROAD**: no adaptive guarantee without joint/conditional analysis; REOPEN for identified keyed protocol with explicit advantage bound |

Prior-art and source-level overlap: [UCT-001-PRIMARY-SOURCES.md](UCT-001-PRIMARY-SOURCES.md). Mathematical foundation and falsification: [UCT-001-MODEL-AND-BASELINE.md](UCT-001-MODEL-AND-BASELINE.md).

## Proposed G1 questions — none proved
1. **UCT-A-G1:** Fix *one* dynamic family (e.g. partial sums or membership) and RAM/cell/bit-probe model; determine whether enforcing write locality w in addition to space S yields a non-redundant lower bound on query probes P. Full enumeration for tiny n, and exact reductions to FS'89/PD'06/bit-probe literature required.
2. **UCT-B-G1:** Fix a bounded-treewidth or read-once Boolean DAG under authenticated, batched writes; find strictly better *end-to-end* shared certificate bounds (not just minimum old-bit probe sets) than full recomputation, independent proofs, shared Merkle multiproof and cached sufficient statistic. Include old-root+count trust costs; no free prover.
3. **UCT-C-G1:** For explicit source-only COPY/ADD bytes and bounded preprocessing, construct an admissible lower bound that remains useful on TOM-006's periodic counterexample `B=a^m bb a^m`, `T=(ab)^m`; compare optimal parse (not merely a relaxation). A per-query O(|T|²) "exact bound" is not an optimization.
4. **UCT-D-G1:** For exactly specified finite Q adaptive queries and item participation cap r, prove a transcript-conditional risk budget or refute it with a finite oracle. Separate one-shot ideal independent hash from practical keyed PRF and quantify any computational distinguishing advantage. No assumed adaptivity closure.

## Phase A acceptance (documentation + classical proof; NOT novel discovery)
- Claim inventory linked to existing KR-001, KR-011/012, KR-017, TOM-003, TOM-005/006, HYP-103 and DeltaMeter.
- Self-contained scoped theorem and finite independent oracle tests. Counterexample: volume condition not sufficient for low-dilation graph embedding.
- Primary-source identities verified against original publisher/arXiv/ECCC landing pages; **existing LIT identities remain authoritative**, no duplicative registry imports.
- Formally enumerate model-transfer exclusions: arbitrary vs externally validated updates; current-observation vs future-trace distinguishability; cell accesses vs physical changed cells; average vs worst-case; exact vs statistical vs PRF; static correlated source coding vs worst-case deltas.
- Hosted CI of PR exact head required for acceptance; passing unit tests cannot establish originality or asymptotic optimality.

## G2 and G3 decisions
- **G2_SOURCE_AUDIT:** compare exact theorem hypotheses, resource units, and parameter scaling to closest primary paper. Classify each claim as KNOWN, DERIVED_CLASSICAL, MODEL_MISMATCH, FALSE, or OPEN_NARROW; no orphan "novel" labels.
- **G2_FINITE_FALSIFICATION:** independent brute-force or SAT/SMT finite probes, explicit reference test oracles, adversarial constructions, reproducible seeds and query transcripts.
- **G3_THEOREM:** only after non-equivalence established: proof with quantified statement and quantified resource budget, construction or matching lower bound where relevant; independent proof audit and eventual Lean formalization for a tractable kernel.
- **G4_PRODUCT:** separate gate. No Rust, no software release, no source-only performance claim without baseline on genuine workloads with complete cost accounting. It is valid to STOP ALL four directions.

## The unification is a lens, not a claimed universal formula
UCT cannot sum or compose lower bounds proved for incompatible computational models. A map preserving valid operations, observable outputs, the adversary and all *charged* resources is a prerequisite for a sound theorem transfer. A proof of a weaker bound or a rename is NOT publication novelty.
