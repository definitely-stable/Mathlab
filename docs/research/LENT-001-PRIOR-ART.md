# LENT-001 — prior-art audit

Status: **G1 OPEN / G1A COMPLETE / G1B AUDIT 01 COMPLETE**.

This document records the current source-level boundary. Mathematical
correctness and publication novelty remain separate gates.

## 1. Sparse parity-check baseline

Binary ASET is direct sparse parity-check territory.

For q>2, Lefmann (2005) studies support-bounded columns under the stronger
condition that every short set of columns is linearly independent for
arbitrary nonzero field coefficients.

Thus:

\[
\text{small-column linear independence}
\Longrightarrow
\text{ASET},
\]

but not conversely for q>2.

Lefmann constructions are valid ASET lower baselines. His q>2 upper bounds
are not automatically ASET upper bounds.

Primary:
https://doi.org/10.1017/S0963548304006625

## 2. Dissociated terminology corrected

Shkredov's \(k\)-dissociated terminology bounds coefficient magnitude
\(|\varepsilon|\le k\), not relation order.

Standard dissociation (\(k=1\)) forbids every finite signed relation and is
therefore stronger than finite-d ASET.

Primary:
https://arxiv.org/abs/2205.07296

Do not call ASET "k-dissociated" without an explicit custom definition.

## 3. Free / h-free / B_h^*

Nešetřil–Rödl–Sales provide unusually close terminology:

- free: all finite subset sums distinct;
- h-free: one collision side has size ≤h, the other is unrestricted;
- \(B_h^*\): h distinct-summand sums unique.

Consequently:

\[
\text{h-free}\Longrightarrow\text{ASET}_h
\]

and

\[
\text{ASET}_d\Longrightarrow B_h^*
\quad(h\le d).
\]

Neither is definitionally equal to ASET.

Primary:
https://doi.org/10.1007/s00493-024-00115-1

## 4. q=3 Sidon does not close ASET

Huang–Tait–Won identify 2-caps with Sidon sets in \(\mathbb F_3^n\), but
their Sidon property includes repeated-summand equations such as
\(a+a=b+c\).

ASET uses subsets and therefore forbids selecting one universe element twice.
It also imposes all-cardinality-through-d and cross-cardinality uniqueness.

The standard \(3^{n/2}\) even-dimensional Sidon maximum therefore is not
automatically an ASET d=2 maximum.

Primary:
https://arxiv.org/abs/1809.05117

## 5. Bounded-weight additive uniqueness is established prior art

Sima–Li–Shomorony–Milenkovic study binary constant-weight \(B_2\)-sequences:
constant-weight binary vectors whose real-valued sums of distinct pairs are
unique.

Primary:
https://arxiv.org/abs/2303.12990

This invalidates any broad claim that Hamming-weight-constrained additive
uniqueness itself is untouched.

The exact ASET combination remains different because of modular arithmetic,
all capacities through d, cross-cardinality collisions and the at-most-w
support model.

## 6. Signature/detecting/adder-code cluster added

Verified neighbors now include:

- Lindström detecting vectors / sum-distinct systems;
- Jevtić sum-distinct integral-vector representatives;
- Fan et al. constant-weight t-signature codes;
- Erdoğan–Maringer–Polyanskii q-ary signature codes.

These largely use ordinary/integer adder-channel arithmetic rather than
finite-field modulo-q ASET.

Primary anchors:

- https://doi.org/10.4153/CMB-1965-034-2
- https://doi.org/10.1137/S0895480194265623
- https://arxiv.org/abs/1905.10180
- https://arxiv.org/abs/2206.10735

This source cluster is now mandatory in G1B.

## 7. Additive / quantitative group testing is a direct comparator

Chang–Chen–Guo–Huang define additive \((D,d)\)-separable matrices as exact
measurement maps for different d-sparse vectors under standard arithmetic.

For \(D=\{0,1\}\), this is the ordinary-arithmetic bounded-d analogue of
ASET.

Primary:
https://arxiv.org/abs/1303.6020

For the same matrix/input domain:

\[
\text{mod-}q\text{ ASET}
\Longrightarrow
\text{ordinary bounded-d additive separability}.
\]

So compatible ordinary-arithmetic upper bounds can become necessary ASET
upper bounds.

The reverse implication fails in general.

This cluster, especially **bounded-column-weight quantitative group
testing**, must be closed before ASET novelty is decided.

## 8. Current novelty verdict

### Closed negatives

- binary sharp ASET: not a clean novelty target;
- generic "bounded-weight additive uniqueness is new": false;
- generic "k-dissociated = bounded-order ASET": false;
- generic "q=3 Sidon = ASET": false.

### Still alive

The exact combined model

\[
\boxed{
\text{modular finite-field addition}
+
|S|,|T|\le d
+
\text{distinct subset elements}
+
|\operatorname{supp}(a_i)|\le w
}
\]

has not been matched by a verified primary source in audit 01.

### G1B remains OPEN

Next required clusters:

1. bounded-column-weight quantitative/additive group testing;
2. finite-field/mod-q bounded-active-user signature codes;
3. q-ary bounded-support Sidon/\(B_h\)/dissociated families;
4. two-sided h-free / both-side-bounded signed relations;
5. q=3 distinct-summand variants;
6. characteristic-two q>2 variants.

Detailed evidence:
\`LENT-001-G1B-AUDIT-01.md\`.
