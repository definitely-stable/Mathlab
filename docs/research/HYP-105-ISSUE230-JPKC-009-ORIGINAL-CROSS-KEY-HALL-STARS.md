# HYP-105 / #230 — JPKC-009: ORIGINAL cross-key source-factor overlaps and Hall star capacities

**2026-10-14. RESTRICTED_THEOREM_C: ALL-h exact original matching identities, true-original finite falsifiers. Root A/B OPEN.**
Strict Draft child of fully 4/4 successful [JPKC-008 #437](https://github.com/definitely-stable/Mathlab/pull/437), pinned parent HEAD `759627a707131f7efbbec6e65f1d9dced5abb7fe`. Do NOT touch or merge `main`. True W(3,s) original incidence geometry and ONE coherent pair of globally injective source→physical labels f,g throughout. Distinct from parallel coherent right-factor injection-fiber [D6-AA4-B #434](https://github.com/definitely-stable/Mathlab/pull/434).

## 1. Why JPKC-008 is insufficient

JPKC008 J28 proves a FULL demanded source key `(P,L)`, with P a three-ORIGINAL-point factor P4 and L a three-ORIGINAL-line factor P4, fixes ONE original GQ endpoint anchor (q,r). Therefore simply counting repeated **identical** 3×3 Hall demands CANNOT yield a cross-anchor expansion inequality.

However, distinct full keys `(P,L1)` and `(P,L2)` may share the SAME left ORIGINAL point triple P and hence original endpoint q, while their right source triples L1,L2 determine DIFFERENT original endpoint lines r1,r2. The dual holds for right source L. These are **actual shared source factors across different anchors**, not independently re-optimized abstract Hall pseudomarginals.

JPKC009 constructs this true bipartite ORIGINAL source factor demand graph: left vertices P (three ORIGINAL point factors), right vertices L (three ORIGINAL line factors), edges `(P,L)` only where at least ONE eligible physically coordinate-proper endpoint-bad 3-path requests that pair's fully occupied physical A-left and A-right continuations. Multiple physical paths may request the same edge; it still has ONE underlying immutable ORIGINAL GQ Hall value and at most ONE perfect matching. Its left and right vertices can be shared by different original GQ anchors. The source factor labels are never resampled.

## 2. THEOREM J30 (ALL h): one-sided source triple fixes one ORIGINAL endpoint factor

For a physically occupied A-left continuation P, the ORIGINAL physical source pair labels `{f(p):p∈P}` form a simple physical three-edge P4 on four distinct row symbols. Its two degree-one symbols are precisely the physical row pair-label `f(q)` of the original GQ endpoint q of EVERY seed that can demand P. By global f-injectivity q is uniquely determined by P. Thus `P→q` is a well-defined partial function on genuinely demanded left vertices. Dually `L→r` for every genuinely demanded right ORIGINAL line-factor triple L.

The JPKC008 full-key rigidity J28 is their combination. J30 permits distinct ORIGINAL nonincident (q,r1),(q,r2) anchors to SHARE P, and distinct (q1,r),(q2,r) to share L. Therefore graph overlap must be analyzed via vertices across DIFFERENT full keys, rather than via repeated edges.

## 3. THEOREM J31 (ALL h): exact local Hall star capacity, not an independence model

Fix ANY three distinct ORIGINAL GQ points P={p1,p2,p3} (not necessarily an occupied physical P4). Let d=s+1. Define

`c(P)=#{unordered pairs {pi,pj} that are ORIGINAL collinear}`,

`t(P)=1` if all three ORIGINAL points lie on ONE common ORIGINAL line, else 0.

The number of triples of DISTINCT ORIGINAL lines L that admit a source incidence perfect matching to P equals

```
Cap(P) = d³ − d*c(P) + 2*t(P).                      (J31)
```

**Proof:** choose an ORIGINAL line independently from the d genuine incident lines at each of the three points. There are exactly d³ labeled choices. For each collinear point pair (i,j), the two independently chosen line slots can collide at their unique common ORIGINAL line, with exactly d ways to choose the third slot: subtract d for each of c(P) pairs. If TWO such collision conditions hold simultaneously, all three lines are the same; this can happen iff all three original points lie on one common line, when the three pairwise intersection terms contribute +3 and the triple intersection contributes −1, producing +2*t(P). There are no original three-point collinearity triangles on distinct lines because of GQ girth 8. The remaining choices use three distinct lines. Different choices cannot yield the SAME unordered L by JPKC008 J25 (the original induced 3×3 graph has at most ONE matching). Therefore the count is EXACTLY Cap(P). QED.

The dual formula `Cap(L)=d³−d*c_dual(L)+2*t_dual(L)` counts source point triples matched to any three distinct ORIGINAL lines.

**Source graph consequence** (ALL h): the degree of a left P vertex in the TRUE *Hall-feasible* demanded source graph is ≤ Cap(P), and dually the degree of right L is ≤ Cap(L). These caps are exact global ORIGINAL source-incidence star capacities. They are **UPPER** bounds on demanded matching degrees, NOT positive lower bounds on selected GF5 D6 witnesses.

## 4. THEOREM J32 (ALL h): point-triple capacity sum is exactly J29 original matching capacity

GQ partial linearity gives exactly `V*binom(d,2)` collinear pairs of original points and `V*binom(d,3)` triples lying together on an ORIGINAL line. Hence summing J31 over ALL `binom(V,3)` original point triples gives

```
Sum_P Cap(P) =
  binom(V,3)*d³
  −d*V*binom(d,2)*(V−2)
  +2*V*binom(d,3).                              (J32)
```

Every three-original-incidence matching has exactly one unordered set P of three original point endpoints, so this sum MUST equal the previous **independent** JPKC008 J29 line-graph inclusion-exclusion formula for the number M3 of three-edge original matchings:

```
binom(N,3) − N(d−1)(N−2)
 + N*binom(2(d−1),2) − 2V*binom(d,3),   N=Vd.
```

Both formulae are checked algebraically in the executable on true ORIGINAL W32 and W34; the first also checked by independent enumeration of **all 455** original point triples on W32 and direct d³ ORIGINAL source line choices for each, with the analogous **all 455** original line triples. No source physics or GF5 approximations enter this identity.

## 5. THEOREM J33: exact cross-key, cross-ORIGINAL-anchor overlap decomposition (ALL h)

Let `D⊂X×Y` be the set of DISTINCT demanded full source keys (P,L), with endpoint maps q(P),r(L) from J30. For fixed P, put
`deg_r(P)=#{L:(P,L)∈D and r(L)=r}`. For fixed L, put
`deg_q(L)=#{P:(P,L)∈D and q(P)=q}`.

Then the exact number of unordered pairs of DISTINCT source demand graph edges meeting at a left P vertex but belonging to DIFFERENT original (q,r) anchors equals

```
Cross_left(D) =
 sum_P [ binom(deg(P),2) − sum_r binom(deg_r(P),2) ].
```

Likewise

```
Cross_right(D) =
 sum_L [ binom(deg(L),2) − sum_q binom(deg_q(L),2) ].
```

These are exact tautological-but-operational identities for an ACTUAL globally injected ORIGINAL source demand graph. They carefully distinguish:
- repeated physical P3 requests for exactly the SAME (P,L) full key (discarded for DISTINCT edge overlap);
- different full keys within the SAME original (q,r) anchor;
- different full keys sharing the SAME original 3-point or 3-line factor source vertex across DISTINCT original anchors (this stage's real target).

The implementation checks one immutable Hall status per globally shared full key and counts Hall-feasible demanded right neighbors of each P and left neighbors of each L, rejecting any capacity violation from J31. It separately retains genuine positional selected-D6 vs nonaligned matching losses. It never assumes source incidence matching events are independent and never changes f/g per seed.

**Limitation:** Positive Cross_left/ Cross_right is NOT itself a positive selected-GF5 motif count. Cross-key sharing creates genuine coupling that could be exploited by a future joint geometric constraint, but the exact overlap identities and local Hall capacity UPPER bounds do not prove selected positivity.

## 5a. J34 exact nested support: true original cross-anchor overlap does NOT force positive D6

Let \(D\) be the set of distinct demanded source factor edges (P,L),
let \(H\subseteq D\) be the subset for which the TRUE ORIGINAL induced
3×3 incidence graph satisfies Hall, and let \(A\subseteq H\) be the
subset for which **at least one real seed** using that key forms a
genuinely selected ORIGINAL D6. The nested edge sets are finite,
entirely globally coherent and depend on the original f/g labeling.
For either side of the source demand graph the cross-anchor
edge-pair count from J33 is monotone under edge deletion:

```
0 <= Cross(A) <= Cross(H) <= Cross(D).                 (J34)
```

**Proof:** each cross-anchor unordered pair of distinct edges in a
subgraph is also a pair in the supergraph, and the original endpoint
factor functions q(P),r(L) remain fixed under deletion. The labels
are ORIGINAL incidence factor triples, not merely physical slots. QED.

This is an EXACT monotonicity certificate, NOT a lower bound on
the selected positive graph. It prevents the opposite inference:
the presence of arbitrarily many raw original cross-anchor source
demands does not itself imply any selected D6.

### First full W32 true ORIGINAL raw cross-anchor data

Counts below are unordered pairs of DISTINCT full keys sharing one
source factor triple vertex and lying on DIFFERENT original nonincident
GQ endpoint anchors. Multiple physical P3 requests for one and the
same full key are counted ONCE before forming edge pairs.

| Genuine ORIGINAL W32 f,g | Left cross-anchor pairs | Right cross-anchor pairs | Unique ORIGINAL source demand keys | Positive original D6 occurrences |
|---|---:|---:|---:|---:|
| lex | 4,616 | 4,792 | 1,380 | 64 |
| reverse | 3,912 | 3,784 | 1,228 | 24 |
| S68 | **2,632** | **2,696** | 1,016 | **0** |
| S72 | **2,928** | **3,312** | 1,092 | **0** |

### Three-level independently audited ORIGINAL cross-anchor loss tensor

| Real W32 f/g | Left raw | Left Hall | Left selected D6 | Right raw | Right Hall | Right selected D6 |
|---|---:|---:|---:|---:|---:|---:|
| lex | 4,616 | 47 | 5 | 4,792 | 59 | 5 |
| reverse | 3,912 | 13 | 0 | 3,784 | 10 | 0 |
| S68 | **2,632** | **1** | **0** | **2,696** | **4** | **0** |
| S72 | **2,928** | **7** | **0** | **3,312** | **3** | **0** |

These numbers count pairs of DISTINCT source-demand full keys, never
duplicate physical paths, and every pair shares one ORIGINAL
three-factor source vertex but uses different original (q,r) anchors.
For each map, the Hall-only pairs are obtained by deleting the
source edges whose ORIGINAL 3×3 point-line graph has no perfect matching.
The final selected-D6 pairs require actual ORIGINAL six-incidence
positional dual alignment on at least one real physical P3 for EACH
retained demanded source edge. All are checked using the SAME
globally complete f,g and independently reconciled with JPKC-006.

Thus W32 S68/S72 demonstrate an even stricter finite method
obstruction: **even nonzero truly Hall-feasible cross-anchor source
overlap does not guarantee a single selected D6 extension**.

On the bounded genuine W34 D4 spread 8-seed source graph, raw
right cross-anchor pairs 186,543 reduce to **1** Hall-feasible
pair and **0** selected D6 cross-anchor pairs. The corresponding
eight-seed lex/random source graphs have zero raw cross-anchor
pairs. None of these partial W34 counts is a full original W34
seven-family census or a statistical estimate.

S68 and S72 are **finite globally realizable counterexamples** to
the naive implication `Cross(D)>0 => at least one selected D6`.
This does not construct an all-h counterfamily for Root B and
does not exclude positive OTHER GF5 classes (indeed both fixtures
have nonzero true original total S). The new executable measures
Cross(H) and Cross(A) separately, exposing exactly which filter
causes the raw cross-anchor source overlap to disappear.

At genuine W34, the 8-seed explicitly targeted lex/random/true
D4 spread calculations are NOT a complete cross-anchor census.
The selected true D4 W34 8-seed source demand graph already
contains **186,543** distinct RIGHT-side cross-anchor demand
edge pairs, while the selected lex/random 8-seed graphs happen
to have none. This contrast is a property of the PINNED finite
seed choices, not a guarantee or a trend with s.

## 6. Independent verification scope and epistemic contract

`research/hyp105_issue230_jpkc009_cross_key_overlap.py` and dedicated six tests:
- TRUE ORIGINAL W32 lex/reverse/S68/S72: **all** endpoint-bad coordinate-proper physical P3 seed demands, original 3×3 factor key sets, actual Hall status, source incidence three-matchings, source D6 positional selection and cross-anchor source vertex overlaps;
- Direct enumerate d³ original line choices for EVERY one of the 455 true W32 original point triples (and d³ original point choices for every one of the 455 true original line triples), establish J31 and sum to exactly 10,560. Also validate J32 against independent JPKC008 J29 original line-graph formula;
- W34 lex/random plus TRUE original D4 Desarguesian symplectic-spread, **eight deterministically distributed** endpoint-bad proper physical P3 seeds per map, exhaustive real demand graph and Hall source star capacities PER SELECTED SEED. NO W34 full seven-GF5 sixset census;
- fail-closed invalid original f/g injection, source cardinality, path and unique source key budgets.

Research issue #230 and Root A/B stay OPEN. The next legitimate JPKC-010 task is to search for a NONTRIVIAL all-h inequality transferring cross-key vertex overlaps + globally occupied physical Ka resources to actual aligned D6 or point/line wedge positive Q. It must explicitly survive low-S W32 S68/S72 and true original D4 spread; D6-AA4-B's nonzero finite coherence gaps show candidate coupling is worth investigating but do NOT provide that inequality.

Do not merge without independent proof review and exact final-HEAD focused CI, INDEX, Proof Audit, and Research all SUCCESS. Do not claim full R3/ASET exponent or unconditional S=Ω(s⁶).
