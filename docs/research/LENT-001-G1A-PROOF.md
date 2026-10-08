# LENT-001-G1A — ASET model proof note

Status: **DERIVED RESULTS / NOVELTY NOT CLAIMED**

This note proves the model equivalences used by the G1A oracle.

## 1. ASET-SIGNED

Let

\[
\Phi(S)=\sum_{i\in S}a_i
\]

for \(S\subseteq[V]\). Fix \(d\ge0\).

### Claim

The following are equivalent:

1. \(\Phi\) is injective on all sets \(S\) with \(|S|\le d\);
2. there is no nonzero \(\varepsilon\in\{-1,0,1\}^V\) such that
   \[
   \sum_i\varepsilon_i a_i=0,
   \qquad
   n_+(\varepsilon)\le d,
   \qquad
   n_-(\varepsilon)\le d.
   \]

### Proof: collision implies signed relation

Assume distinct \(S,T\subseteq[V]\), with \(|S|,|T|\le d\), satisfy

\[
\Phi(S)=\Phi(T).
\]

Cancel \(S\cap T\). Put

\[
P=S\setminus T,
\qquad
N=T\setminus S.
\]

Then \(P\cap N=\varnothing\), at least one of \(P,N\) is nonempty, and

\[
|P|\le d,
\qquad
|N|\le d.
\]

Define

\[
\varepsilon_i=
\begin{cases}
+1,&i\in P,\\
-1,&i\in N,\\
0,&\text{otherwise}.
\end{cases}
\]

Then \(\varepsilon\ne0\),

\[
n_+(\varepsilon)=|P|\le d,
\qquad
n_-(\varepsilon)=|N|\le d,
\]

and

\[
\sum_i\varepsilon_i a_i
=
\sum_{i\in P}a_i-\sum_{i\in N}a_i
=
0.
\]

### Proof: signed relation implies collision

Conversely, suppose such a nonzero \(\varepsilon\) exists. Let

\[
P=\{i:\varepsilon_i=+1\},
\qquad
N=\{i:\varepsilon_i=-1\}.
\]

The supports \(P,N\) are disjoint, and

\[
|P|,|N|\le d.
\]

The relation gives

\[
\Phi(P)=\Phi(N).
\]

Because \(\varepsilon\ne0\), \(P\ne N\). Hence two distinct admissible sets
collide, so ASET exactness fails.

Therefore the two conditions are equivalent. ∎

## 2. ASET-BINARY

Assume \(q=2\).

### Claim

ASET exactness through capacity \(d\) is equivalent to the absence of a
nonempty GF(2) dependency among at most \(2d\) distinct columns.

### Proof

By ASET-SIGNED, a collision gives a relation supported on at most

\[
n_+(\varepsilon)+n_-(\varepsilon)\le2d
\]

columns. In characteristic two, \(-1=+1\), so this is a nonempty GF(2)
subset dependency.

Conversely, let \(U\) be a nonempty dependent set of at most \(2d\)
distinct columns:

\[
\sum_{i\in U}a_i=0.
\]

Partition \(U=P\sqcup N\) so that

\[
|P|\le d,
\qquad
|N|\le d.
\]

Such a partition exists because \(|U|\le2d\). In GF(2),

\[
\sum_{i\in P}a_i
=
-\sum_{i\in N}a_i
=
\sum_{i\in N}a_i.
\]

Since \(U\ne\varnothing\), the disjoint sets \(P,N\) are distinct. Thus
they form an admissible collision.

Hence the conditions are equivalent. ∎

## 3. LIN-2d implies ASET over every field

If ASET exactness fails, ASET-SIGNED supplies a nonzero relation over at
most \(2d\) distinct columns, with coefficients in \(\{+1,-1\}\subseteq
\mathbb F_q\) after field interpretation.

Therefore those columns are linearly dependent.

Contrapositively,

\[
\text{LIN-}2d
\Longrightarrow
\text{ASET-exact}.
\]

No converse is claimed for \(q>2\).

## 4. Nonbinary strict separations

### q=3

Take

\[
m=1,\quad d=1,\quad a_1=1,\quad a_2=2.
\]

The admissible states are

\[
0,\quad1,\quad2,
\]

so ASET exactness holds.

But

\[
a_1+a_2=1+2=0\pmod3,
\]

so the two columns are linearly dependent.

This relation uses two positive terms. It is not an admissible ASET
collision relation for \(d=1\), because ASET requires at most one positive
and at most one negative term after cancellation.

### q=5

Take

\[
m=1,\quad d=1,\quad a_1=1,\quad a_2=2.
\]

Again the states \(0,1,2\) are distinct.

However

\[
2a_1-a_2=2-2=0\pmod5,
\]

so the columns are linearly dependent with arbitrary nonzero field
coefficients.

Thus full small-column independence is strictly stronger than ASET
exactness in both pinned nonbinary examples. ∎

## 5. Degenerate cases

### d=0

The only admissible source set is the empty set, so ASET exactness holds
for every column family.

The signed-relation side bounds force

\[
n_+=n_-=0,
\]

so no nonzero legal signed relation exists. ASET-SIGNED remains valid.

### V=0

There is only the empty source set and no nonzero coefficient vector.
The equivalence is trivial.

### w=0

Every column is the zero vector.

If \(d=0\), the previous case applies.

If \(d\ge1\) and \(V\ge1\), the empty set collides with any singleton, and
a one-term signed zero relation exists. ASET-SIGNED again agrees.

### m=0

The state space contains only the zero vector. The same reasoning as
\(w=0\) applies.

## 6. Evidence role

These are model-level derived results.

They establish which mathematical problem the repository is studying; they
do not establish that the sharp extremal function
\(A_q^{\mathrm{set}}(m,w,d)\) is new.

Publication novelty remains blocked on G1B prior-art closure.
