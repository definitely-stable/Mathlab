# TOM-001-B — Adversarial prior-art audit and model correction

Status: **PHASE B, SOURCE-AWARE TRIAGE / NO THEOREM SELECTED**  
Date: 2026-10-08  
Parent issue: [#15](https://github.com/definitely-stable/Mathlab/issues/15)  
Phase-A map: [TOM-001-OPPORTUNITY-MAP](TOM-001-OPPORTUNITY-MAP.md)  
Novelty: **NOT ESTABLISHED**; no new Rust crate authorized.

## 1. Scope and review of Phase A

Phase A (#16, merged at `a5dcb60185e5163ea9560cafa43b9561ee99de27`) is a useful **scouting catalog**, not 14 confirmed open problems. It supplies operation-level hooks and kill tests. Its weakest points were:
- O01 "accept all no-effect updates" has no frozen old-state memory/probe/certificate validity model. Without this, a cheap full-recompute algorithm or a retained complete truth table satisfies the guarantee vacuously.
- O02 "combine certificates" did not establish whether individual certificates are evaluated against the same baseline or sequentially; no-effect under separate edits **is not closed under composition**.
- O04 undercounted 2026 prior art: an extended ACM TODS version of history-independent dynamic partitioning with B-tree/skip-list/fusion-tree applications exists (DOI 10.1145/3810240, online April 2026).
- O06 confused canonical *logical tree*, deterministic *serialization* and strong history independence of *observable physical memory*. They are different invariants.
- The shared `O(log n)` branch-update heuristic is not a new lower bound; for point replacement in an array a constant number of cells is enough.
- Exact finite test success cannot establish asymptotic novelty or verify a statement about all input sizes.

This audit examines O01/O02 and O04/O06. It does **not** change any LENT-001 theorem, G2B choice, source matrix or CI protocol.

## 2. Sources and valid transfers (primary-source matrix)

| Source and link | Confirmed content and model | Valid relevance | Invalid extrapolation / remaining check |
| --- | --- | --- | --- |
| [Ramalingam, *Bounded Incremental Computation* (PhD, 1993)](https://www.microsoft.com/en-us/research/publication/bounded-incremental-computation/) | Defines incremental complexity relative to input/output change size; gives upper/lower results on particular problems | Output-sensitive incremental complexity is established | Do not describe output-sensitive update bounds alone as a new theorem |
| [Acar et al., *A Library for Self-Adjusting Computation* (2006)](https://doi.org/10.1016/j.entcs.2005.11.043) | Modifiable references and memoization; measured incremental performance | Maintained traces and reuse are well-established | No theorem in this source alone about optimal *certificate* bit-length |
| [Acar–Blume–Donham, *A Consistent Semantics...* (JFP 2013)](https://doi.org/10.1017/S0956796813000099) | Correctness/consistency of memoizing change propagation, mechanized in Twelf | Soundness of reuse is not a new headline | Does not automatically close a precisely scoped certificate memory-probe lower bound |
| [Kumar–Pacak–Erdweg, *Incremental Computing by Differential Execution* (ECOOP 2025)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2025.20) | Differential semantics and formal correctness/optimizations in Rocq, asymptotic improvements for loops | Hard prior-art constraint on O01 | Abstract and publisher metadata checked; theorem-by-theorem model mapping remains |
| [Change Actions (2020)](https://arxiv.org/abs/2002.05256) | Change actions and compositional derivatives | Basic change composition not novel | Does **not** imply arbitrary separately issued no-effect certificates compose |
| [Hartline et al., *Characterizing History Independent Data Structures* (2005)](https://www.microsoft.com/en-us/research/publication/characterizing-history-independent-data-structures/) | For most strongly history-independent models, canonical representation follows up to stated caveats | Canonicality/SHI relationship already investigated | Identical logical nodes do not imply identical physical representations |
| [Buchbinder–Petrank, *Lower and Upper Bounds on Obtaining History Independence* (2006)](https://doi.org/10.1016/j.ic.2005.11.001) | Comparison-based model; exponential separation of weak and strong history independence for some structures | Real lower bounds already exist | Cannot import bounds into a different RAM/cell-probe model without a reduction |
| [Bender–Farach-Colton–Goodrich–Komlós, *History-Independent Dynamic Partitioning* (PACMMOD 2024)](https://doi.org/10.1145/3651609) | Dynamic ordered partition into groups of size Θ(B); O(1) expected operations per update against oblivious adversary, with separate high-probability bound | Broad O04 claim **KNOWN / STOP-BROAD** | Their *partition operation* metric is not automatically bytes moved, or worst-case against an adaptive adversary |
| [Same authors, *History-Independent Dynamic Partitioning with Applications...* (ACM TODS 2026)](https://doi.org/10.1145/3810240) | Extended construction and B-tree, fusion-tree, skip-list applications; accepted March, online April 2026 | MUST cite when scoping O04 | Do not claim a strict canonical byte-level rope theorem is proved here without model match |
| [Berger, *Chonkers / Yarn* (arXiv 2025)](https://arxiv.org/abs/2509.11121) | Content-defined chunk sizes/edit locality and Yarn string representation (preprint) | Direct baseline for O06 | Must distinguish abstract claims from reviewed/fully source-checked theorem assumptions |

**Source-validation level:** publisher/official abstract and bibliographic records checked for the listed primary papers. Full proofs and hypotheses are **not** yet independently rederived; the conclusions here are model-level exclusions and negative finite witnesses, **not publication novelty clearance**.

## 3. O01 — correct, non-vacuous certificate contract

Input model: a finite DAG of total, deterministic functions with explicitly bounded fan-in and finite alphabets. All old inputs are retained in an addressable baseline store, and update requests contain positions and new values. Separate accounts of (i) baseline bytes, (ii) extra retained metadata bits, (iii) certificate bits, (iv) bit/word/cell probes, (v) setup/update cost, (vi) recomputation fallback and (vii) changed-result witnesses are mandatory.

A verifier receives baseline metadata, the changed input positions/values, and a (possibly absent) certificate. It may output:
- `UNCHANGED` only if the exact output remains equal;
- `CHANGED` only if the output provably differs;
- `UNKNOWN` otherwise, triggering a full correct computation.

**Soundness**: every `UNCHANGED` is true. **Non-vacuity**: completeness must specify a target class, e.g. all single changes preserving output, or a stated coverage fraction over a declared distribution. No unrestricted universal fast verifier is promised.

**Elementary kill witness: old output alone is insufficient.** Let f(x1,x2)=x1 OR x2. Starting from either (1,0) or (1,1), the retained old output is 1. The identical update "set x1 to zero" yields outputs 0 and 1 respectively. Any verifier seeing only the old output + edit is forced to give the same answer; it cannot simultaneously distinguish both without extra information or probes. This is a correctness/model demonstration, **not a novel lower bound**.

A full retained input state trivially allows exact verification; the challenge must charge reads, metadata and time. Narrow candidate survives only as **AUDIT-PENDING**, no "Optimal Frontier" theorem status.

## 4. O02 — independently sound certificates do not compose

**Exact counterexample:** f(x,y)=x AND y and baseline (0,0). Individually:
- changing only x to 1 leaves f=0;
- changing only y to 1 leaves f=0.

The simultaneous joint change (1,1) makes f=1. Thus *independence of edited input locations* does not imply independence of their effects, and the naïve `cert1 AND cert2` combiner is **unsound**.

Safe alternatives must *explicitly* prove:
- independent cone decomposition with separability of f on the edited subspaces, **or**
- a joint certificate for the combined update, **or**
- a sequential certificate with revalidation against the modified intermediate baseline.

Basic composition by revalidation is prior art; target improvement has to be a **strict** proof-size/probe bound for a narrow class beyond path union/monoid reduction. This remains **REVISE / AUDIT-PENDING**, not a theorem.

## 5. O04 — broad history-independent partitioning is closed as novelty

Dynamic ordered partitioning with Θ(B)-sized groups and O(1) *expected number of partition operations* under an **oblivious adversary** is explicitly achieved in the 2024 paper, with a 2026 extended publication and data-structure applications.

Hence reject as new:
- "history-independent partition exists";
- "expected constant operations for arbitrary simple insert/delete under same adversary/model";
- "canonical representation is sufficient for history independence" as a fresh insight.

A genuine remaining question (NOT VERIFIED OPEN): exact tradeoff when demanding *physical canonical serialized bytes* + worst-case *bytes rewritten* + variable-length split/concat with a fully adaptive adversary. If those stronger requirements are inconsistent or already solved, close O04 completely. **Decision: STOP-BROAD; retain only precisely stronger model as SCOUT.**

## 6. O06 — canonical rope is not automatically a new primitive

Three distinct representations must be defined:
1. **Logical canonical shape**: same content yields same abstract tree.
2. **Canonical serialization**: same content and fixed public parameters yield the same byte string.
3. **Physical strong HI**: adversary observing memory snapshots gains no additional history-dependent information, under a specified observation/initial-randomness model.

Trivial string serialization gives (2) without edit efficiency. Persistent balanced trees may have fast edits without canonical serialization. Shared subtrees' addresses and allocation remnants can reveal history even when logical trees match.

**Adversarial toy witness:** partition unique values into consecutive fixed-length pairs. A single prepended symbol shifts every old pair boundary; all old pairs disappear, causing Θ(n) boundary turnover. This refutes an unqualified stable-locality claim for positional partitioning, not all canonical rope constructions.

Freeze a cost metric (new bytes written, changed chunk identifiers, memory probes, lifetime/GC cost) and a deterministic or seeded adversary before making another theorem candidate. **Decision: SCOUT / NO THEOREM SELECTED.**

## 7. Joint decision, product gating

| Candidate | Math status after audit | Critical blocker | Allowed next |
| --- | --- | --- | --- |
| O01 | **AUDIT-PENDING / REVISE** | retained-state/probe class and strongest exact reuse bound missing | define one finite nontrivial function family, compare exact maintained sufficient statistic |
| O02 | **NAIVE CLAIM REFUTED**; narrower class AUDIT-PENDING | interaction between simultaneous edits | formalize separability and valid joint certificates |
| O04 | **STOP-BROAD** | existing 2024 + 2026 HI partition theory | only stronger byte/worst-case/adaptive model after paper-level map |
| O06 | **SCOUT / DEFER** | Chonkers/Yarn, canonical logical/physical confusion | choose representation+cost+adversary; prove one nontrivial impossibility or improvement |

**No general lower-bound theorem, novel capacity exponent, or crate is claimed.** Compared with Phase A, priority moves toward **a narrow O01 oracle model** only conditionally; O02 provides a hard counterexample. O04/O06 are downgraded.

## 8. Follow-up evidence gate (TOM-001-C)

1. Maintain independent tiny exhaustive witness tests for OR old-output ambiguity and AND simultaneous-interaction unsoundness; use bit-exact oracles only. These establish counterexamples to overbroad contracts, not novel results.
2. Select a nontrivial O01 class with **two different old inputs sharing retained metadata**; enumerate sound and complete short certificates under explicit allowed probes.
3. Identify the nearest maintained-state algorithm and derive the exact same cost accounting. If no defensible improvement, **STOP O01**.
4. For O04/O06, check paper-level theorem assumptions (randomized setup, word/byte model, adversary and physical representation); if no leftover measurable Rust benefit, **STOP**.
5. Only after a verified open mathematical gap and a measurable operation exists, allow `SELECT_THEOREM`; otherwise terminate scouting without a new crate.

Acceptance markers: `TOM_B_SOURCE_MATRIX_RECORDED`, `TOM_B_O02_INTERACTION_COUNTEREXAMPLE`, `TOM_B_O01_AMBIGUITY_COUNTEREXAMPLE`, `TOM_B_NO_PREMATURE_NOVELTY`.
