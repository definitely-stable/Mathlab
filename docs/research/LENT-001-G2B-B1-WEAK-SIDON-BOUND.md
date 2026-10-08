# LENT-001 / G2B-B1 — weak-Sidon upper certificate

**Status:** PROOF-DERIVED RIGOROUS INTERVAL. Not an exact optimum.
**Scope:** ASET with d=2, finite odd-prime fields, arbitrary support bound.
**Issue:** [#14](https://github.com/definitely-stable/Mathlab/issues/14).
**Novelty:** NONE. This is an application of a classical weak-Sidon
group-order bound, not a new mathematical theorem.

This B1 document supplements, and does not rewrite, the frozen
G2B-A [signed-collision hypergraph protocol](LENT-001-G2B-A-PROTOCOL.md).

## 1. Correct definition-level implication

Let C={a_1,...,a_V} be distinct, nonzero columns of F_q^m
with all subset sums of sizes 0,1,2 distinct. Let

    G=(F_q^m,+),  N=q^m,  S=C union {0},  s=V+1.

A *weak Sidon set* means that sums a+b of all unordered
pairs of DISTINCT a,b in S are pairwise distinct.

These off-diagonal sums are:
- 0+a_i = a_i, the original singleton states;
- a_i+a_j, i<j, the original doubleton states.

Their mutual uniqueness is exactly a subset of ASET's
injectivity requirements. Therefore **ASET implies weak Sidon**,
and the weak-Sidon upper bound applies.

**WARNING — not equivalence.** Weak Sidon does not require
the empty sum 0 to be different from an off-diagonal pair
sum. For example, in Z_11, S={0,1,2,4,7} is weak Sidon, but
4+7=0; hence C=S\{0} fails ASET against the empty subset.
The reduction is only **one-way** and can certify upper
bounds, never a witness's ASET correctness.

No forbidden equation with three positive coefficients is
introduced: d=2 signed-side bounds remain as frozen in G2B-A.

## 2. Classical odd-group inequality, fully proved

**THEOREM (known weak-Sidon bound).** If S is weak Sidon in
an abelian group G of odd order N, then

    s(s-3)+1 <= N, where s=|S|.

**Proof.** For each nonzero group element t define f(t)
as the number of ordered pairs (a,b) of DISTINCT S-elements
with a-b=t. Thus

    sum_{t!=0} f(t) = s(s-1).

Suppose different ordered pairs (a,b) and (c,d) have
the same difference. Then a+d=b+c. If the four points
were distinct, this would violate weak Sidon. The only
remaining nontrivial possibilities are a=d or b=c,
giving respectively 2a=b+c or 2b=a+d.

In an odd-order group the two possibilities cannot hold
simultaneously for distinct endpoints: this would imply
2(a-b)=0 and hence a=b. Thus every pair of representations
of a fixed difference corresponds to a unique **centered
three-term arithmetic progression** (x,y,z) in S satisfying

    x != z,  x != y, z != y, and x+z=2y.

For any fixed center y in S, **at most one** unordered
pair of distinct endpoints {x,z} can have x+z=2y.
If two different such unordered pairs existed, their
off-diagonal sums would collide. Hence at most s
centered progressions exist.

Every centered progression accounts for exactly TWO
unordered pairs of equal ordered-difference
representations: one orientation of its endpoints and
the reversed orientation. This counting remains valid
in characteristic three, where a 3-cycle can produce
difference multiplicity three — we count unordered pairs
of representations, not a false per-difference cap of 2.

Consequently,

    sum_{t!=0} binom(f(t),2) <= 2s.

As k-1<=binom(k,2) for any integer k>=1, the number of
ordered-pair representations in excess of one per nonzero
difference satisfies

    sum_{t:f(t)>0} (f(t)-1) <= 2s.

At most N-1 nonzero differences can occur, so

    s(s-1)
       = number of represented differences + excess
       <= (N-1)+2s.

Rearranging gives s(s-3)+1<=N. QED.

The resulting bound is **independent of the hard support w**,
so it can tighten G2B without proving novelty or sparse
asymptotic strength.

**Prior-art attribution:** Ron M. Roth and Gadiel Seroussi,
*Location-correcting codes*, IEEE Transactions on
Information Theory 42(2), 554–565 (1996), Lemma 5.
DOI https://doi.org/10.1109/18.485724 .
The primary-source lemma contains this inequality; the
above argument is a self-contained restatement in our
exact model. Source verification must not confuse
2-LCC *correction locality* with ASET *write locality*.

## 3. The q=5,m=3,w=2 exact finite deduction

For G=F_5^3, N=5^3=125.
ASET implies s=V+1 obeys

    s(s-3)+1 <= 125.

For s=12, the left side is 12*9+1=109.
For s=13, it is 13*10+1=131>125.
Therefore s<=12 and **V<=11**.

G2B-A already provided and independently verified a
10-column support<=2 exact ASET witness:

    (0,1,1) (0,1,2) (0,1,3) (0,3,1)
    (1,0,2) (1,3,0) (2,0,4) (2,4,0)
    (3,0,0) (4,0,0)

Hence the rigorously proved numerical interval is

    10 <= A_5^set(3,2,2) <= 11.

This strictly improves the old Hamming-ball interval [10,15].
It does NOT settle whether 11 is attainable with support<=2.
An incomplete existence search for an eleventh column
cannot turn the interval into the exact optimum 10.
Conversely, one valid 11-column family independently
verified by the original ASET oracle would make the
optimum exactly 11, *without an exhaustive search*.

## 4. Exact-arithmetic implementation and independent checks

Source: research/lent_weak_sidon.py

- weak_sidon_max_size computes the largest s using exact
  integer sqrt of 4N+5 and checks BOTH threshold inequalities.
- weak_sidon_upper_v computes s-1 for pinned odd prime fields.
- is_weak_sidon_with_zero enumerates unordered pair sums
  independently of the forbidden-hypergraph construction.
- difference_multiplicities and the certificate count
  ordered differences, duplicates and centered progressions
  exactly in the declared finite group.
- original research/lent_exhaustive.py:is_exact_family
  independently validates the 10-column witness.
- test_lent_weak_sidon.py tests exhaustively all small
  candidate families; q=3 characteristic-3 triple cycle;
  extremal Z_11 weak-Sidon-but-not-ASET fixture;
  malformed inputs and fail-closed domain.

Integration in research/lent_hypergraph.py uses

    global_upper = min(hamming_upper, weak_sidon_upper).

This bound is used only to cap pending frontier upper
estimates or stop if a matching verified incumbent is
found; it does **not** introduce an unsound heuristic
pruning rule. Existing G2B-A edge construction and
witness verification remain unchanged.

## 5. G2B-B decision

G2B-B1: ACCEPT if the hosted CI confirms full legacy
oracles, signed-collision regression and new integer
threshold/difference certificate.

G2B-B2 remains **OPEN**, with two possibilities:
- produce an 11-column exact witness (then ASET max=11);
- rigorously refute all 11-column families under
  w<=2, with a separately independently checkable
  search or mathematical impossibility certificate
  (then ASET max=10).

Any SAT/ILP heuristic, time limit, node cutoff or
unfinished search is strictly PROVISIONAL evidence;
do not report exactness from one.

No source in this slice justifies publication novelty,
Lean completion or a Rust crate; original extremal
proof target selection is deferred pending G2B-B2.
