# LENT-001-G1B — Audit 03 final closure

Status: **COMPLETE — SPLIT_BY_CHARACTERISTIC**

Date: 2026-10-08

Issue: #6

This document closes G1B. It does **not** claim publication novelty. It
authorizes the next research stage only for a precisely narrowed
support-sensitive odd-characteristic lane.

## 1. What G1B has ruled out

The following are not valid Mathlab novelty claims:

1. exact bounded-active subset identification itself;
2. binary modular bounded-contention coding;
3. finite-field bounded-active signature coding;
4. constant-weight / sparse active-user signatures as a generic concept;
5. support-constrained parity-check coding as a generic concept.

Primary anchors include:

- Censor-Hillel et al., Bounded-Contention Coding:
  https://arxiv.org/abs/1208.6125
- Goseling–Stefanović–Popovski, finite-field signature codes:
  https://arxiv.org/abs/1602.02612
- Fan–Gu–Hachimori–Miao, constant-weight signature codes:
  https://arxiv.org/abs/1905.10180
- Han–Yildiz–Hassibi, support-constrained parity checks:
  https://arxiv.org/abs/2605.08644

Therefore the repository must not present ASET existence, sparse signatures,
or parity-check sparsity themselves as new.

## 2. New 2026 direct baseline: support-constrained parity checks

Han, Yildiz and Hassibi (2026) study linear codes with **arbitrary support
constraints on the parity-check matrix** and derive the best minimum distance
permitted by the support mask. Their framework explicitly includes support
patterns motivated by limiting how often a symbol is accessed (column
weight), as well as row-weight restrictions.

For a mask \(M\), they define a structural Kruskal-rank quantity and show:

- every matrix filling obeying the mask has minimum distance bounded by the
  mask's structural quantity;
- over sufficiently large finite fields, that mask-optimal distance is
  achievable.

This is important prior art because a hard column-support restriction is not
an untouched coding concept.

It does **not** directly close Mathlab:

- characteristic-two ASET expands to a binary matrix, whereas their generic
  achievability theorem may require a sufficiently large field;
- odd-characteristic ASET forbids only side-bounded \(\pm1\) relations, not
  arbitrary field-coefficient dependencies;
- Mathlab asks an extremal question over the choice of support pattern under a
  per-column support budget, not only the optimum filling for one prescribed
  mask.

Novelty effect: **strong baseline, not an equivalence**.

## 3. Characteristic two

For \(q=2^s\), G1B proves

\[
\text{ASET}_d
\Longleftrightarrow
\text{no nonempty binary subset dependency of size }\le2d
\]

after expansion through an \(\mathbb F_2\)-basis.

The hard q-ary support condition becomes a bound on the number of nonzero
binary blocks.

The extremal sandwich is

\[
A_2(m,w,d)
\le
A_{2^s}^{\mathrm{set}}(m,w,d)
\le
A_2(sm,sw,d).
\]

Thus characteristic two is structurally embedded in binary sparse
parity-check/BCC theory.

### G1B classification

- \(q=2\): **STOP as primary novelty lane**.
- \(q=2^s,\ s>1\): **DEPRIORITIZE**. A block-aware sharpening may still be
  mathematically interesting, but it is not the best first target for a new
  theorem because the lane inherits strong binary sparse-code baselines.

This is not a statement that every block-sparse constant is known sharply.

## 4. q=3

In \(\mathbb F_3\),

\[
\mathbb F_3^\*=\{\pm1\}.
\]

Therefore coefficient restriction alone does not distinguish ASET from
ordinary nonzero-coefficient relations.

The distinction is the **two-sided capacity condition**

\[
n_+(\varepsilon)\le d,\qquad n_-(\varepsilon)\le d.
\]

G1A already gives exact finite examples where ASET holds despite a short
linear dependency because the relation violates those side bounds.

Standard q=3 Sidon/2-cap results do not automatically close this lane because
their repeated-summand and fixed-cardinality conventions differ.

### G1B classification

**CONTINUE as odd-characteristic testbed.**

The allowed research target is not "q=3 ASET is new". It is the sharp
hard-support extremal law under the two-sided relation constraint.

## 5. Odd q > 3

For odd \(q>3\), ASET differs from arbitrary small-column independence in
two independent ways:

1. coefficients are restricted to \(\pm1\);
2. positive and negative supports are separately bounded by \(d\).

Lefmann-style sparse parity-check constructions remain valid lower baselines
because they satisfy a stronger condition.

Their arbitrary-coefficient upper bounds do not automatically upper-bound
ASET.

Finite-field signature codes show that bounded-active identity recovery is
known when support is unrestricted or not the optimized parameter.

Constant-weight ordinary-adder signature codes show that hard support and
active-user identification are known together under a different arithmetic
model.

### G1B classification

**CONTINUE as primary research lane.**

The precise surviving question is:

> For fixed odd \(q\), fixed \(d\), and hard column support \(w\), what is the
> sharp asymptotic growth of
> \(A_q^{\mathrm{set}}(m,w,d)\) as \(m\to\infty\)?

Any theorem must be compared against:

- the Sparse-Update Hamming-Ball upper bound;
- sparse arbitrary-coefficient parity-check lower constructions;
- ordinary-addition constant-weight signature / \(B_h\) upper bounds when a
  valid transfer exists;
- support-constrained parity-check mask bounds when a valid reduction exists.

## 6. Group-testing / detecting-matrix closure

Constant-column-weight group testing is highly relevant to the **location of
the sparsity constraint**: each item participates in only a bounded number of
tests.

The best-known constant-column-weight group-testing work audited in G1B uses
Boolean OR observations and probabilistic/asymptotic recovery, not zero-error
finite-field additive observations.

Therefore it remains a comparator rather than an equivalent ASET theorem.

Additive/quantitative group testing under ordinary arithmetic is closer, but
ordinary equality is stronger than equality modulo \(q\). Its upper bounds
can constrain ASET only when the exact transfer assumptions are satisfied.

## 7. Why G1B can close without claiming novelty

Audit 03 is fail-closed with respect to publication claims, but G1B does not
need to prove that no unseen paper exists.

The purpose of G1B is to decide whether there is a sufficiently precise,
source-aware research target worth testing next.

That condition is met for the odd-characteristic support-sensitive lane.

The repository still labels the candidate theorem **OPEN / NOVELTY NOT YET
CLAIMED** until:

1. G2 finite evidence identifies a concrete regime;
2. G4 produces a theorem;
3. the exact theorem statement receives a final theorem-level prior-art
   review before preprint promotion.

## 8. Final G1B decision

\[
\boxed{\texttt{SPLIT\_BY\_CHARACTERISTIC}}
\]

Classification:

- characteristic two: binary/block-sparse coding baseline; deprioritized;
- q=3: continue as the clean side-bound testbed;
- odd q>3: continue as the primary coefficient-plus-side-bound lane.

## 9. Next gate

G2 is authorized only for odd characteristic.

Initial exact fields:

\[
q\in\{3,5,7\}.
\]

Initial priority:

- \(d=2\);
- small fixed \(w\in\{1,2,3\}\);
- exact or certified interval values of
  \(A_q^{\mathrm{set}}(m,w,d)\);
- comparison with LENT and arbitrary-coefficient sparse-linear baselines.

G2 must select a **specific theorem target**, not merely accumulate tables.
