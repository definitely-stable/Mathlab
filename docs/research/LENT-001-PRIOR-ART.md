# LENT-001 — preliminary prior-art audit

Status: **G1 NOT CLOSED**.

This file records enough evidence to prevent an incorrect novelty claim. It is not yet a systematic literature review.

## 1. Sparse parity-check matrices — direct binary overlap

### Lefmann, Pudlák, Savický (1996)

They study the maximum number of columns in a binary matrix with a bounded number of ones per column such that every small collection of columns is linearly independent.

Reference:
- “On sparse parity check matrices”, LNCS 1090 (1996).
- DOI: https://doi.org/10.1007/3-540-61332-3_137

Parameter map to LENT for (q=2):

```text
their rows n              <-> m
their independent columns k <-> 2d
their column weight r     <-> w
their number of columns   <-> V
```

This is essentially the binary extremal problem induced by exact set-sketch injectivity.

### Naor, Verstraete (2005)

“Improved bounds on the size of sparse parity check matrices”, ISIT 2005.

DOI:
https://doi.org/10.1109/ISIT.2005.1523645

They study (N_F(n,k,r)): the largest number of columns in an n-row finite-field matrix, each column having at most r nonzero entries, with every k columns linearly independent.

This can yield stronger bounds than the elementary LENT Hamming-ball argument in the binary fixed-(d,w) regime.

**Decision:** do not market LENT-C or a binary (A_2) asymptotic as new.

## 2. PinSketch / Minisketch

Minisketch is an optimized BCH-based implementation of PinSketch-style set reconciliation.

Primary project:
https://github.com/bitcoin-core/minisketch

Mathematical overview:
https://github.com/bitcoin-core/minisketch/blob/master/doc/math.md

Its documentation states that a b-bit-element sketch of capacity c uses (bc) bits and that sketches combine linearly to represent symmetric difference.

Relevance:

- demonstrates the practical large-alphabet/BCH point;
- does **not** supply constant support locality as c grows;
- update/creation work scales with capacity.

Therefore Minisketch motivates the tradeoff but is not a counterexample to it.

## 3. Stuffed IBLTs

Jonas Klausen, Rasmus Pagh, Stefan Walzer,
“Stuffed IBLTs: Optimal Linear Multiset Sketches” (2026).

Preprint:
https://arxiv.org/abs/2609.17487

The construction achieves, for its stated randomized model and parameter regime, space within (1+arepsilon) of the information-theoretic optimum, constant-time updates, (O(n)) decoding, and high-probability recovery.

Relevance:

- establishes that “near-optimal space + constant-time update” is possible after relaxing the deterministic worst-case exact model;
- requires a careful model comparison rather than an apparent contradiction;
- motivates separating alphabet/cell richness, randomization, failure probability, and exact injectivity.

## 4. B_h / Sidon-type viewpoint

For q>2, a collision between two set sums produces a relation with coefficients in ({-1,0,1}), not an arbitrary finite-field linear dependence.

This is closer to restricted-coefficient (B_h)/Sidon-type additive-combinatorial questions than to ordinary minimum-distance coding alone.

**G1 task:** locate the sharp literature for bounded-support vectors inside q-ary Hamming balls with distinct sums of up to d distinct columns.

No novelty conclusion is recorded yet.

## 5. Locally updatable coding literature

There is a broad literature on locally updatable/decodable codes, but its update model, encoded-message model and adversarial requirements are not automatically the same as additive set-sketch column support.

**G1 task:** build an explicit definition-by-definition map before importing lower bounds.

## 6. openai/math process reference

The public `openai/math` repository separates manuscripts, supporting verification artifacts, and a Lean formalization catalogue, while explicitly warning that not all unformalized results are guaranteed correct.

Reference:
https://github.com/openai/math

Mathlab adopts the process separation, not the mathematical content.

## 7. Preliminary novelty verdict

- finite counting lemma: **useful baseline, novelty not claimed**;
- binary constant-locality impossibility: **likely subsumed/strengthened by known sparse parity-check results**;
- sharp binary (A_2): **not a clean new target**;
- q-ary restricted-coefficient version: **plausible research gap, unverified**;
- nested-prefix strengthening: **plausible research gap, unverified**;
- joint computation/locality/communication theorem: **potentially strong, model not frozen**.

G1 remains open.
