# LENT-001-G2A — exact-search proof obligations

Status: **DERIVED / EXACT NUMERICAL FRAMEWORK**

No publication novelty is claimed.

## 1. Exact d=2 incremental condition

For a selected family \(C\), let \(S(C)\) contain:

- the zero state;
- all singleton sums;
- all sums of two distinct selected columns.

Assume \(C\) is ASET-exact through \(d=2\).

A new column \(c\) preserves exactness iff:

1. \(c\notin S(C)\);
2. for every \(a\in C\),
   \[
   a+c\notin S(C).
   \]

The newly created sums \(a+c\) are pairwise distinct because cancellation of
the same \(c\) gives \(a=b\).

Therefore the G2A incremental predicate is necessary and sufficient.

## 2. Branch-and-bound exactness

The DFS considers every candidate column in a fixed order and branches on
include/exclude.

The only pruning rule is:

\[
|C_{\text{selected}}|+
|\text{remaining candidates}|
\le
|\text{incumbent}|.
\]

Even selecting every remaining candidate cannot then improve the incumbent,
so pruning cannot discard a better solution.

Hence exhaustive completion proves the reported maximum exactly.

## 3. Independent witness check

Every reported ASET witness is rechecked by the pre-existing
\`is_exact_family\` oracle.

The stronger linear baseline is independently checked with
\`linear_dependency_witness\`.

## 4. w=1 decomposition theorem for d=2

Let

\[
a_q=A_q^{set}(1,1,2).
\]

Then

\[
\boxed{
A_q^{set}(m,1,2)=m a_q.
}
\]

### Upper bound

Every support-one column belongs to exactly one coordinate.

Restrict an ASET family to one coordinate. Its local subset sums through
size two must remain distinct, so at most \(a_q\) columns can occupy that
coordinate.

Summing over \(m\) coordinates gives

\[
A_q^{set}(m,1,2)\le m a_q.
\]

### Lower bound

Take an optimal one-coordinate family of size \(a_q\) and place an independent
copy on each coordinate.

Within one coordinate, exactness is inherited from the local family.

A two-coordinate pair sum identifies both occupied coordinates and the local
values, so it cannot collide with a different cross-coordinate pair.

A cross-coordinate state cannot collide with a state supported on one
coordinate.

Thus the union is ASET-exact and has size \(m a_q\).

## 5. Local exact values used in Phase A

Counting gives

\[
1+t+\binom t2\le q
\]

for a one-coordinate family of size \(t\).

For the frozen fields the bound is attained by:

- q=3: \(\{1\}\), so \(a_3=1\);
- q=5: \(\{1,2\}\), so \(a_5=2\);
- q=7: \(\{1,2,4\}\), so \(a_7=3\).

Therefore:

\[
A_3^{set}(m,1,2)=m,
\]

\[
A_5^{set}(m,1,2)=2m,
\]

\[
A_7^{set}(m,1,2)=3m.
\]

These are baseline exact results, not novelty claims.
