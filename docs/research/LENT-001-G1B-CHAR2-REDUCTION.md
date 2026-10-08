# LENT-001-G1B — characteristic-two reduction

Status: **DERIVED RESULT / NOVELTY NOT CLAIMED**

## Theorem

Let

\[
q=2^s
\]

and let

\[
a_1,\ldots,a_V\in\mathbb F_q^m.
\]

For \(d\ge0\), the following are equivalent:

1. all subset sums
   \[
   \sum_{i\in S}a_i,\qquad |S|\le d,
   \]
   are distinct;
2. every nonempty \(U\subseteq[V]\) with \(|U|\le2d\) satisfies
   \[
   \sum_{i\in U}a_i\ne0;
   \]
3. after expansion through any fixed \(\mathbb F_2\)-basis of
   \(\mathbb F_q\), every nonempty set of at most \(2d\) expanded columns is
   GF(2)-linearly independent.

If each \(a_i\) has q-ary coordinate support at most \(w\), then every
expanded binary column has at most \(w\) nonzero blocks of size \(s\).

## Proof: 1 implies 2

Assume there is a nonempty \(U\) with

\[
|U|\le2d,\qquad \sum_{i\in U}a_i=0.
\]

Partition

\[
U=P\sqcup N
\]

with

\[
|P|\le d,\qquad |N|\le d.
\]

Because the field has characteristic two,

\[
-\sum_{i\in N}a_i=\sum_{i\in N}a_i.
\]

Therefore

\[
\sum_{i\in P}a_i
=
\sum_{i\in N}a_i.
\]

The disjoint sets \(P,N\) are distinct because \(U\ne\varnothing\). This is
an admissible ASET collision, contradiction.

## Proof: 2 implies 1

Suppose two distinct sets \(S,T\) with

\[
|S|,|T|\le d
\]

have the same sum.

In characteristic two,

\[
0
=
\sum_{i\in S}a_i-\sum_{i\in T}a_i
=
\sum_{i\in S}a_i+\sum_{i\in T}a_i.
\]

Terms indexed by \(S\cap T\) occur twice and cancel. Hence

\[
\sum_{i\in S\triangle T}a_i=0.
\]

Since \(S\ne T\),

\[
S\triangle T\ne\varnothing,
\]

and

\[
|S\triangle T|\le |S|+|T|\le2d.
\]

This contradicts condition 2.

Therefore 1 and 2 are equivalent.

## Proof: 2 iff 3

Choose an \(\mathbb F_2\)-basis

\[
b_1,\ldots,b_s
\]

of \(\mathbb F_q\).

Coordinate expansion defines an additive-group isomorphism

\[
\beta:\mathbb F_q^m\to\mathbb F_2^{sm}.
\]

For every subset \(U\),

\[
\beta\!\left(\sum_{i\in U}a_i\right)
=
\sum_{i\in U}\beta(a_i).
\]

Thus

\[
\sum_{i\in U}a_i=0
\]

iff

\[
\bigoplus_{i\in U}\beta(a_i)=0.
\]

Since all coefficients are 1, this is exactly a binary subset dependency.

## Locality preservation

Partition the \(sm\) binary coordinates into \(m\) blocks, each block
representing one original \(\mathbb F_q\) coordinate.

For every \(i\),

\[
|\operatorname{supp}_{q}(a_i)|
=
|\operatorname{blocksupp}_{2}(\beta(a_i))|.
\]

Therefore

\[
|\operatorname{supp}_{q}(a_i)|\le w
\]

iff the expanded binary vector occupies at most \(w\) nonzero blocks.

Ordinary binary Hamming weight only satisfies

\[
|\operatorname{supp}_{2}(\beta(a_i))|
\le sw;
\]

it does not preserve the stronger block structure.

## Research consequence

For characteristic two, the sharp Mathlab extremal problem is best viewed as
a **block-sparse binary BCC/parity-check problem**.

This is structurally different from Lefmann's arbitrary
\(\mathbb F_q\)-coefficient independence.

It also means that q=2 is only the block-size-one member of an entire
characteristic-two lane.

No novelty is claimed for this reduction.
