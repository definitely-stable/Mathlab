# LENT-001-G1A — exact oracle evidence

Status: **EXACT NUMERICAL RESULT**

Novelty status: **NOT CLAIMED**

Implementation commit:

\[
\texttt{891e3dff1c7053043bb24e5bb1659a866055bc26}
\]

Reviewed PR head:

\[
\texttt{40ffeecaff8c3558810f498cafa359a3bde9e6ea}
\]

GitHub-hosted PR CI:

- workflow run: \`37724834067\`;
- conclusion: SUCCESS;
- unit tests: 11 passed.

Observed acceptance markers:

- \`G1A_SIGNED_EQUIV_PASS\`
- \`G1A_Q2_EQUIV_PASS\`
- \`G1A_Q3_SEPARATION_PASS\`
- \`G1A_Q5_SEPARATION_PASS\`
- \`G1A_ORACLE_PASS\`

## 1. What was exhaustively enumerated

For each frozen case, the oracle enumerated every family of \(V\) distinct
nonzero columns from the complete set of vectors satisfying the support
bound.

For every family it independently checked:

1. exact subset-sum injectivity through capacity \(d\);
2. absence of a legal signed relation with
   \(n_+\le d\) and \(n_-\le d\);
3. absence of any arbitrary-coefficient dependency on at most \(2d\)
   columns.

The first two properties agreed on every enumerated family.

## 2. q=2 baseline

Parameters:

\[
q=2,\quad m=4,\quad d=2,\quad w=2.
\]

There are 10 candidate nonzero support-at-most-2 columns.

| V | all families | ASET-exact | full-linear independent | ASET but not full-linear |
|---:|---:|---:|---:|---:|
| 1 | 10 | 10 | 10 | 0 |
| 2 | 45 | 45 | 45 | 0 |
| 3 | 120 | 110 | 110 | 0 |
| 4 | 210 | 125 | 125 | 0 |

This exactly matches the proved binary equivalence in the searched box.

## 3. q=3 finite separation

Parameters:

\[
q=3,\quad m=3,\quad d=2,\quad w=2.
\]

There are 18 candidate columns.

| V | all families | ASET-exact | full-linear independent | ASET but not full-linear |
|---:|---:|---:|---:|---:|
| 1 | 18 | 18 | 18 | 0 |
| 2 | 153 | 144 | 144 | 0 |
| 3 | 816 | 576 | 544 | 32 |
| 4 | 3060 | 726 | 0 | 726 |

Thus the frozen nontrivial \(d=2\) grid already contains 32 size-3 ASET
families that fail arbitrary-coefficient small-column independence.

A first exact witness is

\[
a_1=(0,0,1),\quad
a_2=(0,1,0),\quad
a_3=(0,2,2).
\]

It satisfies

\[
a_1+a_2+a_3=0
\]

over \(\mathbb F_3\), so the columns are linearly dependent.

However this relation uses three positive terms. For \(d=2\), it violates
the ASET side bound \(n_+\le2\), and exhaustive subset-sum checking confirms
that the family is ASET-exact through capacity two.

At \(V=4\), no family in the complete candidate set is full-linear
independent through four columns, while 726 families remain ASET-exact.

## 4. q=5 finite separation

Parameters:

\[
q=5,\quad m=3,\quad d=2,\quad w=1.
\]

There are 12 candidate columns.

| V | all families | ASET-exact | full-linear independent | ASET but not full-linear |
|---:|---:|---:|---:|---:|
| 1 | 12 | 12 | 12 | 0 |
| 2 | 66 | 60 | 48 | 12 |
| 3 | 220 | 160 | 64 | 96 |
| 4 | 495 | 240 | 0 | 240 |

A first size-2 witness is

\[
a_1=(0,0,1),\qquad
a_2=(0,0,2).
\]

The family is ASET-exact through \(d=2\), but

\[
a_1+2a_2=0
\]

over \(\mathbb F_5\).

Here the separation is caused directly by the coefficient restriction:
the dependency coefficient \(2\) is not an allowed ASET signed coefficient
\(\pm1\).

## 5. Interpretation

These exact results establish a finite **model gap**:

- binary ASET coincides with the small-column GF(2) baseline in the frozen
  grid;
- q=3 can separate because the ASET positive/negative side bounds are
  stricter than an undirected support-size bound;
- q=5 can additionally separate because arbitrary field coefficients are
  richer than \(\pm1\).

This is important evidence that \(A_q^{\mathrm{set}}(m,w,d)\) is not merely
a notational copy of arbitrary-coefficient sparse linear independence.

It does **not** establish:

- a new asymptotic exponent;
- a sharp value of \(A_q^{\mathrm{set}}(m,w,d)\);
- publication novelty;
- separation from every known Sidon, \(B_h\), dissociated-set, or coding
  formulation.

Those questions remain gated on G1B prior-art closure.

## 6. Safety checks

Across the complete frozen grid:

- ASET exactness agreed with signed-relation absence;
- full small-column independence always implied ASET exactness;
- q=2 equivalence held;
- every ASET-exact family satisfied the finite Sparse-Update Hamming-Ball
  Bound.

Therefore G1A execution evidence supports the frozen model and allows the
project to proceed to G1B after the evidence commit itself passes latest-head
CI.
