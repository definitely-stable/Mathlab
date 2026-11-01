# HYP-105 / issue #230 — independent genuine-source covariance referee

**Scientific status:** scoped mathematical theorem and independently testable finite
falsifiers; NOT a qualified external human review, NOT an attack on the proved
one-path selector, NOT a counterexample to the universal Branch A risk claim.
Acceptance remains `OPEN_WITH_FORMAL_BLOCKER`.

**Frozen parent:** scientific Draft #705, exact HEAD
`7f855282323f09f9ce98363723417f32e8ed91ea`. This audit creates
a separate child Draft and does not modify the parent or `main`.

## 1. Independently discovered all-h true-original counterexample

**Theorem (negative TWO-path survival covariance in true original W(3,s)).**
For **every** dyadic `s=2^h >= 2`, there are COMPLETE, separately globally
pair-injective physical coordinate maps `f,g` on the genuine symplectic
generalized quadrangle `W(3,s)`, and TWO individually coordinate-proper
source-owned two-edge physical paths `P,Q` in its full physical graph,
such that under the ORIGINAL source-conflict local-minimum priority selector
followed by TWO typed unbiased coordinate bichromatic cuts,

```
Pr(P survives)>0,  Pr(Q survives)>0,
Pr(P and Q both survive)=0,
Cov(1_P,1_Q)=-Pr(P survives)*Pr(Q survives)<0.
```

This holds on the **FULL genuine original source**, and also on a retained
three-ORIGINAL-ID sparse core. The theorem is constructed algebraically,
not fitted to W32/W34.

### All-h construction (actual GQ flags, not artificial incidence)

Let `d=s+1`, `V=(s+1)(s^2+1)`, `N=V*d`, and
`a=min{b:binom(b,2)>=V}`, so `a>=6`. The true ORIGINAL incidence graph
is `d`-regular on the two typed parts. Choose three pairwise endpoint-
disjoint actual incidence flags `i0=(p0,l0), i1=(p1,l1), i2=(p2,l2)`.
A direct greedy proof suffices: after choosing at most two disjoint flags,
at most `4d<N` original flags meet a used point or line because `V>4`;
therefore a third original flag exists. All three are mutually NONCONFLICTING
in the original source-pencil conflict graph, for ANY injected maps.

Prescribe six physical factor-pair labels, on THREE genuine original points
and THREE genuine original lines:

```
           i0       i1       i2
f(point):  {0,1}    {1,2}    {0,2}
g(line):   {0,1}    {1,2}    {2,3}
```

All three pairs on each side are distinct. Extend these partial assignments
by any bijection/injection into the remaining `binom([a],2)` labels; this
is possible because its capacity is >=V. Both maps are now COMPLETE,
separately globally pair-injective and fixed. The unrestricted correlation
between their six reserved images is legal.

Each true flag contributes BOTH opposite-corner physical edges, with unique
original provenance. In particular they give the real physical paths

```
P: (0,0) --[i0]-- (1,1) --[i1]-- (2,2)
Q: (1,1) --[i1]-- (2,2) --[i2]-- (0,3).
```

Each path has THREE different first coordinates and THREE different second
coordinates. No original factor edge or sixset is invented; the two paths
share one *real* original source flag `i1`, and their union uses exactly
three pairwise nonconflicting ORIGINAL incidence IDs.

### Why the joint event is ZERO, regardless of priority correlations

A whole-flag cut keeps any original flag iff its left AND right coordinate
pairs are both bichromatic. For `P`, the left requirements are
`color(0)!=color(1)` and `color(1)!=color(2)`; for `Q` they are
`color(1)!=color(2)` and `color(2)!=color(0)`.
Their union demands all THREE inequalities on the triangle `0-1-2-0`,
impossible with two colors. Therefore `Pr(P&Q)=0` even before considering
the original source priority selection.

Each individual left factor constraint graph is a path on three symbols
and is cut with probability `1/4`. The same holds on the independent
right alphabet. Consequently each individually proper physical two-path
passes BOTH typed cuts with probability exactly `1/16`.

The original priorities of its two NONCONFLICTING flags are simultaneously
locally minimal with positive probability (put all three designated flags
ahead of all other source flags in a strict total ordering). Thus both
individual full-source path survival probabilities are positive.
The covariance is strictly negative on the true FULL W(3,s), for ALL h.

On the legal core retaining ONLY these three true original IDs, the
original conflict graph is edgeless and priority selection always keeps
all three. Hence the sharp **exact** sparse-core witness is

```
Pr(P)=Pr(Q)=1/16,   Pr(P&Q)=0,   Cov=-1/256.
```

It is a restriction to an intentionally sparse core; it must NOT be
misrepresented as an instance of the dense `m0>=s^4` root hypothesis.

## 2. Independent priority probability identity (full source)

For ANY finite source conflict graph, let the target original IDs `i,j`
be nonadjacent, and partition their external neighbor sets into A (only
i), B (only j), C (both), of sizes `a,b,c`. Uniform independent continuous
priorities `t,u` give the exact conditional joint density

`(1-t)^a (1-u)^b (1-max(t,u))^c`.

Integrating over the two triangles `t>=u` and `u>=t` yields EXACTLY

```
Pi(i,j) =
  [1/(a+c+1) - 1/(a+b+c+2)] / (b+1)
+ [1/(b+c+1) - 1/(a+b+c+2)] / (a+1).
```

No target priorities, path indicators, or pair-label maps are claimed
independent. In our true-source witness, the two individual survival
probabilities are `Pi(i0,i1)/16` and `Pi(i1,i2)/16` for the FULL source.
The joint probability remains zero because of the left odd cycle.
Thus the full-source covariance is the negative PRODUCT of those two
strictly positive **individual** probabilities.

This is an independently derived source-probability formula rather than
a call to the #679/#695 selector code.

## 3. Bounded exact falsifiers

The new module `research/hyp105_real_source_negative_path_covariance_referee.py`
imports ONLY the existing `genuine_source` true symplectic geometry fixture
for `h=1,2`; no earlier selector/covariance or original physical-graph
construction code is imported. It independently:

1. Builds genuine W32 and W34 three-source matchings, complete f/g,
   and ALL full source-owned two diagonals; checks 2N unique physical
   edges and exact source edge ownership of BOTH witness paths.
2. Independently builds the original source pencil conflicts from actual
   point/line IDs and arbitrary completed maps, for sparse and FULL
   source; checks the two local-minima formula probabilities.
3. Enumerates **all 2^7=128** relevant independent left/right coordinate
   binary assignments, with a second independent bipartite parity oracle:
   individual cuts 1/16, joint cut zero.
4. Exhaustively checks the exact two-target priority integral against
   **all 5!=120 strict orders** for **all 2^9=512** labelled simple
   five-vertex conflict graphs with the prescribed target nonedge.
5. Checks integer-minimal alphabet capacity for all dyadic exponents
   `1<=h<=25`, including odd exponents, without floating point.
6. Rejects malformed input. All source/priority probabilities are
   exact `fractions.Fraction`, not Monte Carlo estimates.

These experiments falsify possible finite mistakes; the **all-h theorem**
is proved in Section 1, not inferred from them.

## 4. Independent scientific assessment of Branch A

**R1 source provenance:** the new TRUE original W32/W34 examples check
complete global pair injections and exact full-source edge ownership.
This is an additional independent finite challenge, NOT a full all-h
review of every source-provenance assertion in #659/#672.

**R4 selector:** the single-path priority lower bound #679 is compatible
with this witness, while any replacement by *positive covariance* or
*independence of two path-survival events* is **FALSE even on the genuine
full W(3,s)** for every dyadic order. #704's use of linearity of the
individual path marginals followed by Jensen is compatible with the
negative example. No counterexample to that actual Jensen route found.

**R2/R3/R5/R6/R7/R8:** historical heavy-tail chunks, all-h core
pruning, four FULL/CORE mixed blockers, B/B original-sixset inverse,
ten-sign GF(5) coefficients and the final global root are NOT
independently re-proved by this covariance audit. Their scientific
acceptance remains `NOT_REVIEWED` by an external qualified human referee.

**The root issue remains OPEN_WITH_FORMAL_BLOCKER**. Passing GitHub
tests, this valid scoped no-go, or an internal AI technical analysis must
not be represented as qualified external independent peer review.

## 5. Next highest-value work after this slice

- Obtain an actual external qualified written referee judgement on
  R1–R8 from the frozen #705 dossier; prioritize source-indexed
  FULL/CORE blocker and the exact B/B six-ID inverse.
- In parallel, investigate coefficient-level and hypergraph extraction
  strategies outside the expectation-risk inference. The Branch A
  `R3=Omega(s^6)` lower does NOT rule out a particular deterministic
  GF(5) assignment or nonclassical extraction.
- No cosmetic constant-only stack, no unsourced theorem acceptance,
  no change to `main`, no merges or root issue closure.

**Reference root:** https://github.com/definitely-stable/Mathlab/issues/230
