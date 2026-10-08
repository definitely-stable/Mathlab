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
