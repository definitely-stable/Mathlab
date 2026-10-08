# Research decisions

## 2026-10-08 — D001

**ACCEPT:** LENT-001 as the first Mathlab research family.

Rationale: finite combinatorial core, easy exact falsification, suitable Lean kernel, directly relevant to set reconciliation.

## 2026-10-08 — D002

**ACCEPT:** separate mathematical correctness from novelty.

The finite locality/state bound may be recorded as a theorem even while its novelty field remains "not claimed".

## 2026-10-08 — D003

**STOP AS DEFAULT TARGET:** sharp binary extremal \(A_2(m,w,d)\).

Reason: exact binary set-sketch injectivity maps directly to sparse parity-check matrices with bounded column weight and small-set column independence. Existing work from at least 1996/2005 directly overlaps and may be stronger.

This does not forbid using the binary case as a baseline or formalization target.

## 2026-10-08 — D004

**REVISED:** q-ary work remains a novelty candidate, but must be expressed through the exact subset-sum object \(A_q^{\mathrm{set}}(m,w,d)\), not generic "restricted dependencies".

Reason: for \(q>2\), arbitrary-coefficient short linear independence is stronger than the restricted signed collision condition induced by exact set sums.

## 2026-10-08 — D005

**ACCEPT:** no preprint promotion during G0/G1 model correction.

The repository may contain a complete baseline proof and verification artifacts without representing them as a new publication result.

## 2026-10-08 — D006

**ACCEPT:** G1A becomes the first active post-foundation slice.

G1A freezes:

- \(A_q^{\mathrm{set}}(m,w,d)\);
- the signed-relation equivalence;
- q=2 equivalence to small-column independence;
- q>2 implication/separation;
- exact definition maps to Sidon/B_h/dissociated objects;
- update-locality boundaries.

Issue: #3.

## 2026-10-08 — D007

**DEPRIORITIZE:** pure nestedness tax.

Neighboring rate-compatible coding results make a positive asymptotic penalty from nestedness alone an unsafe primary conjecture.

**RETAIN:** nestedness + bounded update locality as a secondary novelty candidate.

## 2026-10-08 — D008

**REJECT AS MODEL EQUIVALENCE:** LCC/LDC query locality is not Mathlab update locality.

Mathlab locality measures how many sketch coordinates change under one element update. Prior-art transfer must start from update-efficient/sparse-generator notions or provide an explicit reduction.

## 2026-10-08 — D009

**DEFER:** communication + locality + computation theorem.

No computation parameter is considered frozen until it is independent of the update-support measure. Candidate future resources are decoding work, incremental decoding work, cell probes, or memory probes.

## 2026-10-08 — D010

**ACCEPT AS DERIVED BASELINE:** mixed-alphabet LENT counting.

For coordinate alphabet sizes \(q_1,\ldots,q_m\), the reachable-state count

\[
\sum_{\substack{J\subseteq[m]\\|J|\le dw}}
\prod_{j\in J}(q_j-1)
\]

may be used as a baseline upper bound on the number of exact input states.

No novelty is claimed until mixed-alphabet coding prior art is closed.

## 2026-10-08 — D011

**CLASSIFY:** IBLT-style structures as randomized/additive comparators, not deterministic exact instances by default.

Their practical space/update frontier remains relevant, but a probabilistic listing guarantee is not the frozen all-input injectivity guarantee.


## 2026-10-08 — D012

**RENAME PUBLIC TERMINOLOGY; RETAIN INTERNAL ID.**

`LENT-001` remains the stable historical research identifier so that issue, protocol, evidence, and CI references do not break.

Deprecated public label:

`Locality–Entropy Trilemma`

Preferred labels:

- research program: **Exact Additive Sketch Locality Frontier**;
- baseline theorem: **Sparse-Update Hamming-Ball Bound for Exact Additive Set Sketches**;
- current extremal lane: **Sparse Bounded-Order Subset-Sum Families** / `A_q^set(m,w,d)`.

Rationale:

1. the word *trilemma* overstates the mathematical content currently proved;
2. the finite theorem is specifically a reachable-state/Hamming-ball counting bound under sparse updates;
3. "locality" and "entropy" are heavily overloaded across unrelated fields;
4. precise terminology reduces false novelty and search ambiguity.

Historical documents may retain the old wording when necessary for traceability, but new README headings, issue titles, roadmap entries, preprints, and theorem names must use the preferred terminology.


## 2026-10-08 — D013

**ACCEPT:** G1A model/oracle gate is complete.

Evidence:

- ASET-SIGNED proof accepted;
- q=2 equivalence accepted;
- q=3 and q=5 strict finite separations accepted;
- G1A_ORACLE_PASS on hosted CI;
- post-merge CI green at `e435b72fbf7b94f3f514a3f5fbbae88070876525`.

This establishes a model gap, not publication novelty.

## 2026-10-08 — D014

**OPEN:** G1B primary-source novelty closure as the only allowed next gate for ASET.

Issue: #6.

No sharp ASET theorem may be promoted as new until G1B chooses exactly one
of CONTINUE_ASET, REDUCE_TO_KNOWN_OBJECT, SPLIT_Q3_QGT3, or
STOP_NOT_NOVEL.


## 2026-10-08 — D015

**CORRECT TERMINOLOGY:** standard "k-dissociated" is not used as a synonym
for bounded-order ASET.

In Shkredov's verified definition, k bounds coefficient magnitude. Standard
dissociation is an all-orders property and is stronger than finite-d ASET.

## 2026-10-08 — D016

**EXPAND G1B PRIOR ART:** signature/detecting/adder codes and
additive/quantitative group testing are mandatory source clusters.

Reason: primary sources contain all-subset or bounded-d exact
standard-arithmetic sum-identification models, including constant-weight
variants. They are materially closer to ASET than the initial coding-only
map suggested.

## 2026-10-08 — D017

**DO NOT CLOSE G1B AFTER AUDIT 01.**

Audit 01 found no verified source matching all five active ASET features
simultaneously: modular finite-field addition, both collision sides bounded
by d, distinct subset elements, all cardinalities through d, and
per-generator support at most w.

However established bounded-weight B2/signature and additive-separable
literature makes a broader novelty claim unsafe.

Next required audit is bounded-column-weight quantitative group testing and
finite-field/mod-q bounded-active-user signature/separable codes.
