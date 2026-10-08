# LENT-001-G1A — ASET model/oracle protocol

Status: **FROZEN FOR ORACLE EXECUTION v2**

Issue: #3

Execution baseline:

\[
\texttt{main@15c1bf7bb47c5edb3727fd50b27c4044daf4813f}
\]

No publication novelty is claimed in G1A.

## 1. Primary object

Let \(q\) be a prime power and

\[
a_1,\ldots,a_V\in\mathbb F_q^m,
\qquad
|\operatorname{supp}(a_i)|\le w.
\]

For \(S\subseteq[V]\),

\[
\Phi(S)=\sum_{i\in S}a_i.
\]

The family is ASET-exact through capacity \(d\) when

\[
S\ne T,\quad |S|,|T|\le d
\implies
\Phi(S)\ne\Phi(T).
\]

Define

\[
A_q^{\mathrm{set}}(m,w,d)
\]

as the maximum \(V\) for which such a family exists.

## 2. Signed-relation theorem target

ASET exactness is equivalent to the absence of a nonzero

\[
\varepsilon\in\{-1,0,1\}^V
\]

such that

\[
\sum_i\varepsilon_i a_i=0,
\]

with separate side bounds

\[
n_+(\varepsilon)\le d,
\qquad
n_-(\varepsilon)\le d.
\]

The side bounds are part of the model and must not be replaced by only
\(\|\varepsilon\|_0\le2d\).

A complete proof is recorded in
\`LENT-001-G1A-PROOF.md\`.

## 3. Boundary with arbitrary-coefficient small-column independence

Define LIN-\(2d\) to mean that every nonempty set of at most \(2d\)
distinct columns is linearly independent over \(\mathbb F_q\).

For every field,

\[
\text{LIN-}2d
\Longrightarrow
\text{ASET-exact}.
\]

### q=2

For \(q=2\),

\[
\text{LIN-}2d
\Longleftrightarrow
\text{ASET-exact}.
\]

This is a known-territory baseline, not a novelty claim.

### q=3

Pinned separation:

\[
m=1,\quad d=1,\quad a_1=1,\quad a_2=2=-1.
\]

The states \(0,1,2\) are distinct, so ASET exactness holds through \(d=1\),
while

\[
a_1+a_2=0.
\]

### q=5

Pinned separation:

\[
m=1,\quad d=1,\quad a_1=1,\quad a_2=2.
\]

The singleton states are distinct, while the two nonzero columns in
\(\mathbb F_5^1\) are linearly dependent; for example

\[
2a_1-a_2=0.
\]

Therefore arbitrary-coefficient small-column independence is strictly
stronger than ASET exactness in these nonbinary examples.

## 4. Exact oracle scope

The executable G1A oracle is intentionally restricted to prime fields

\[
q\in\{2,3,5\}.
\]

Coordinate-wise integer arithmetic modulo \(q\) is therefore valid field
arithmetic.

General \(GF(p^k)\) with \(k>1\) is out of scope until a real finite-field
representation is introduced.

The oracle independently checks:

1. ASET subset-sum exactness;
2. bounded signed-relation absence;
3. arbitrary-coefficient small-column independence.

It must not derive one checker from another, because the purpose is to
falsify incorrect equivalence assumptions.

## 5. Frozen exhaustive grid

The v2 grid is:

- \(q=2,m=4,d=2,w=2,\max V=4\);
- \(q=3,m=3,d=2,w=2,\max V=4\);
- \(q=5,m=3,d=2,w=1,\max V=4\).

The grid is deliberately tiny and exact.

No runtime expansion is allowed without a protocol update.

## 6. Required invariants

For every enumerated family:

\[
\text{ASET exact}
\Longleftrightarrow
\text{no legal signed relation}.
\]

For every enumerated family:

\[
\text{no arbitrary dependency among }\le2d\text{ columns}
\Longrightarrow
\text{ASET exact}.
\]

For \(q=2\), the latter implication must be an equivalence.

The q=3 and q=5 pinned families must demonstrate strict separation.

Every ASET-exact family must continue to satisfy the finite
Sparse-Update Hamming-Ball Bound.

## 7. Boundary rules retained from G1 planning

### Sidon / B_h / dissociated families

No equivalence claim is allowed without a definition-level map covering:

- repeated versus distinct summands;
- exactly \(h\) versus all sizes through \(h\);
- cross-cardinality collisions;
- coefficient set;
- ambient operation;
- bounded support.

### Locality

Mathlab locality is write/change locality

\[
w=\max_i|\operatorname{supp}(a_i)|.
\]

It is not LCC/LDC query locality.

### Nested families

Pure nestedness tax is deprioritized.
The retained candidate is nestedness plus bounded update locality.

### Computation

No computation tradeoff is active until an independent computational
cost model is frozen.

## 8. Acceptance

G1A execution accepts only if GitHub-hosted CI emits all markers:

\`G1A_SIGNED_EQUIV_PASS\`

\`G1A_Q2_EQUIV_PASS\`

\`G1A_Q3_SEPARATION_PASS\`

\`G1A_Q5_SEPARATION_PASS\`

\`G1A_ORACLE_PASS\`

and unit tests pass on the latest PR head.

The planning marker \`G1A_MODEL_PLAN_PASS\` remains historical evidence.

## 9. Next gate

After G1A acceptance, the next allowed research gate is **G1B prior-art
closure**.

G1B, not G1A, decides one of:

- CONTINUE_ASET;
- REDUCE_TO_KNOWN_OBJECT;
- SPLIT_Q3_QGT3;
- STOP_NOT_NOVEL.

Only after that decision may Mathlab choose a sharp asymptotic ASET theorem
as a novelty target.
