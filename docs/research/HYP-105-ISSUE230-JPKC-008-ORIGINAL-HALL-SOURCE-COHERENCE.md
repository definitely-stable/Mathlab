# HYP-105 #230 — JPKC-008: exact 3×3 ORIGINAL source Hall matching and globally shared demand coherence

**2026-10-14. RESTRICTED_THEOREM_C (J25–J29 universal exact structure; Root A/B remain OPEN).**
Strict research-only Draft child of [JPKC-007 #435](https://github.com/definitely-stable/Mathlab/pull/435), parent final HEAD `6816514f70f7a6d76e50c4066a284f9eb6ab23bd` (4/4 GitHub-hosted CI SUCCESS). No merges, no `main` change. Use only globally consistent ORIGINAL point/line injection f,g.

## 1. Why Hall is the next proper test and what D6-AA4-B already covers

JPKC-007 decomposed each genuine endpoint-bad physical three-path's A/A matching proposals into missing ORIGINAL incidence, nonaligned A/A dual cycles, and selected ORIGINAL D6. The count was `6LR` for the two physical A-half family sizes L and R. In S68 and S72 nearly every permutation failed the **genuine ORIGINAL** source point-line incidence check. Treating these six permutations as independent original assignments is misleading because their adjacency statuses all belong to a SINGLE fixed original GQ incidence graph.

Parallel D6-AA4-B [#434](https://github.com/definitely-stable/Mathlab/pull/434) already proves finite conditional coherence across globally injected ORIGINAL right-label four-factor fibers. JPKC-008 does **not** repeat its 24 global completions or its source-cylinder cover. Instead JPKC-008 derives a NEW structural theorem about the underlying TRUE ORIGINAL GQ 3×3 incidence subgraph, independent of images f,g, and checks whether repeated demand for THE SAME point/line factor triples can actually cross distinct ORIGINAL GQ anchors. J28 proves it cannot.

## 2. THEOREM J25 — ALL h: one or zero ORIGINAL perfect matchings per 3+3 source factors

Let P={p1,p2,p3} be any THREE DISTINCT ORIGINAL points and L={ell1,ell2,ell3} THREE DISTINCT ORIGINAL lines of a genuine generalized quadrangle W(3,s), s=2^h. Consider their induced bipartite ORIGINAL incidence graph `H(P,L)`, with an edge pi–ellj iff `pi∈ellj`. This graph has girth at least 8 (as an induced subgraph of the ORIGINAL generalized quadrangle incidence graph). Then:

```
# {bijections pi -> ell_{sigma(i)} : each pi lies on its paired ell} <= 1.
```

**Proof.** If two different perfect matchings existed, their symmetric difference would be a disjoint union of nonempty alternating even cycles in a bipartite graph on exactly six vertices. Such a cycle would have length 4 or 6. GQ incidence graphs have neither 4-cycles (unique original line through two collinear points) nor 6-cycles (the GQ uniqueness/triangle prohibition). Contradiction. Therefore at most one PERFECT matching. QED. This is all-h, independent of f,g, not a finite W32 inference.

The successful matching, when one exists, fixes a UNIQUE **THREE ORIGINAL incidence-ID** set U. Any feasible positive D6 extending a genuine endpoint-bad physical P3 through chosen physical A halves must use this fixed U: there are no alternative original 3-incidence matchings on the same source (P,L).

## 3. THEOREM J26 — ALL h: exact Hall subset certificate and source matching uniqueness

For any P,L as above define `N_L(A)={ell∈L : ell is incident to at least one p∈A}` for A⊆P. Put

```
d_H(P,L)=max_{A⊆P} (|A|-|N_L(A)|) >=0 .
```

There are exactly 7 nonempty subsets of P. **Hall's marriage theorem** gives:

```
d_H(P,L)=0 iff H(P,L) contains a perfect matching
           iff that matching exists and is UNIQUE by J25.
```

For d_H>0, an explicit deficient subset A (one or two or three source points) certifies impossible completion independently of ANY physical palette arguments. For d_H=0, a unique original incidence matching U exists and may be checked for positional physical A/A dual **alignment**. Hall-feasibility by itself NEVER implies the selected positive D6 class.

This exact Hall witness is much more precise than regarding six possible source-label bijections as unrelated random trials. We must not claim a Hall-deficient source triple pair could become feasible by changing f,g: ORIGINAL GQ adjacency is fixed independently of physical images.

## 4. THEOREM J27 — ALL h exact globally shared ORIGINAL source-demand ledger

For a TRUE globally complete pair f,g, let \(\mathcal E\) be its endpoint-bad proper physical P3s. For each P3 seed t, enumerate actual physically available left A-side source 3-point triples \(\mathcal A_L(t)\) and right A-side source 3-line triples \(\mathcal A_R(t)\) using the existing exact physical occupied-edge oracle.

For each occurrence of a source pair key \(k=(P,L)\) in their cartesian product, let \(m_k\) denote its multiplicity across *all selected physical seeds and ORIGINAL endpoint GQ anchors*. The key has the SAME immutable original Hall value \(d_H(k)\) and, if feasible, the same unique ORIGINAL source matching U(k), irrespective of where or how often it is demanded. Define

```
T_pair = sum_k m_k    (= sum_(seed t) |A_L(t)| |A_R(t)| ),
T_Hall = sum_(k: d_H(k)=0) m_k ,
T_noHall = sum_(k: d_H(k)>0) m_k .
```

**Exact identities** on ONE true original f,g:

```
T_pair = T_Hall + T_noHall.
6 T_pair = (6 T_pair - T_Hall) + T_nonAligned + T_D6.
T_Hall = T_nonAligned + T_D6 .
```

The `6 T_pair-T_Hall` term EXACTLY equals JPKC-007's number of failed ORIGINAL source incidence permutations, because J25 permits **at most ONE valid matching per 3×3 key**. Of the feasible unique source matchings, the genuine ORIGINAL six-incidence Q must still satisfy the positional GF5 selected-D6 classifier; those that fail contribute to `T_nonAligned`. The remaining `T_D6` are actual selected positive Q witnesses, with ORIGINAL six incidence IDs preserved.

These formulas are exact definitional consequences, not an improved lower bound for T_D6. The source Hall status of one key is NOT independently tunable for each physical seed. However, J28 below proves that the same exact A/A source key **cannot** be reused by distinct ORIGINAL GQ anchors. Thus this precise fixed-key mechanism gives within-anchor consistency, NOT the originally hoped-for cross-anchor global coupling. The executable reports distinct keys, repeated source demand occurrences, and enforces ZERO distinct-GQ-anchor sharing. Do not sell these within-anchor repetitions as a nontrivial global anchor-expansion theorem.

**Important falsification gate:** in W32 S68/S72 one can have many Hall-feasible keys but STILL no positive D6 because positional A/A matching fails. Thus even a proved Hall-expansion theorem alone could be insufficient; the final selected GF5 alignment gate must be retained.

## 4a. NEW THEOREM J28 — ALL h source-key anchor rigidity (restricted cross-anchor NO-GO)

Fix the unordered three ORIGINAL point factors P appearing as an A-half physical C6 continuation of a coordinate-proper physical P3 seed. Their **physical pair-label edges** f(p), p∈P, form a simple undirected three-edge P4, joining projected endpoint symbols z3 and z0 via the two outside symbols. Its two degree-one vertices are **exactly** {z3,z0}, intrinsic to the unordered source triple P, irrespective of which physical path seed prompted it. The original point endpoint q=f⁻¹({z3,z0}) is uniquely determined because f is globally injective.

Dually, the three ORIGINAL line factors L of the right physical A-half form a 3-edge P4 whose degree-one physical symbols uniquely identify r=g⁻¹({y3,y0}).

**J28 (all h).** The EXACT source demand key (P,L) for physically occupied left and right A-half triple completions fixes one and only one ORIGINAL nonincident endpoint anchor (q,r). Therefore it **cannot** occur as an actual demand for two different original GQ nonincident anchors. In symbols,

```
# { (q,r) genuine ORIGINAL GQ anchors demanding a fixed (P,L) } <= 1.
```

This is a uniform structural negative result for the specific JPKC-008 two-A-half matching design. Even though an identical key can be reused by two or more physical P3 realizations, their ORIGINAL q,r anchor must be the SAME. The proof uses only the physical P4 degree-one endpoints and global injection of f,g; no enumeration or random assumption. It does **not** say all ORIGINAL source labels have no cross-anchor interactions in a more general matching/wedge witness construction.

This conclusively closes the naive "deduplicate exact 3×3 A-half source keys and obtain cross-GQ-anchor Hall expansion" proof route. A future global theorem must relate **different** source keys through shared original point/line factors or actual global f/g occupancy, or include B/A and A/B wedges in an expanded incidence-demand hypergraph. This also distinguishes JPKC-008 from the genuine four-factor injection-fiber global coupling already studied in D6-AA4-B.

### Complete W32 exact endpoint-bad source Hall split

| Genuine global W32 | Source 3×3 demand occurrences | Distinct source keys | Repeated physical-seed demand occurrences | Hall-feasible occurrences | Hall-feasible but NONALIGNED A/A | Selected positive ORIGINAL D6 |
|---|---:|---:|---:|---:|---:|---:|
| lex | 3,144 | 1,380 | 1,764 | 288 | 224 | 64 |
| reverse | 2,704 | 1,228 | 1,476 | 152 | 128 | 24 |
| S68 | 2,176 | 1,016 | 1,160 | 54 | 54 | **0** |
| S72 | 2,400 | 1,092 | 1,308 | 84 | 84 | **0** |

Every tested W32 key has exactly **ZERO** repeated demand across distinct original (q,r) GQ anchors, as J28 requires. The full independent W32 experiment additionally tested **ALL 207,025** arbitrary ORIGINAL 3×3 source factor pairs against the seven Hall subsets and all six perfect-matching permutations.

On genuine W34 lex/random and original D4 symplectic spread, the bounded full-per-seed census of eight genuine endpoint-bad physical P3s yielded respectively 47, 43 and 55 Hall-feasible occurrences out of 44,055; 40,506; 41,697 source triple-pair occurrences. Of those, only 9, 4 and 9, respectively, have true selected ORIGINAL D6 positional alignment. These are strictly targeted finite source checks, not full W34 seven-Q census or an asymptotic estimate.

## 4b. NEW THEOREM J29 — ALL h exact global ORIGINAL three-matching capacity

Let `d=s+1`, `V=(s+1)(s²+1)`, `N=Vd` be the number
of ORIGINAL incidence edges. Denote by `M_3(GQ)` the number of
UNORDERED original three-edge matchings (three mutually disjoint
point–line incidences). Since a 3×3 ORIGINAL source factor pair has
at most one perfect matching by J25, `M_3` also counts EXACTLY the
distinct Hall-feasible pairs of three original point factors and
three original line factors, among `binom(V,3)²` possibilities.

The line graph of the ORIGINAL regular bipartite incidence graph has
`N` vertices, degree `2(d−1)`, `N(d−1)` edges, and exactly
`2V*binom(d,3)` triangles (each consists of three original
incidences through the same original point or same original line).
The count of independent triples in ANY graph with n vertices,
m edges, degrees D_v and t triangles equals
`binom(n,3)−m(n−2)+sum_v binom(D_v,2)−t`.
Its independent triples are exactly the three-matchings of the
ORIGINAL bipartite incidence graph, giving the closed formula

```
M_3(GQ) = binom(N,3)
          − N(d−1)(N−2)
          + N*binom(2(d−1),2)
          − 2V*binom(d,3).                      (J29)
```

**Proof:** the independent-triple identity is inclusion–exclusion
over conflicting edge pairs, two-conflict wedges, and three-conflict
triangles in the original line graph. The displayed degree and
triangle counts follow from ORIGINAL bipartite d-regularity.
J25 gives the required bijection with Hall-feasible 3×3 factor keys.
No physical pair-label model is used. QED.

For W(3,2), `V=15,d=3,N=45`, so `M_3=10560`.
The exact 207,025-pair W32 Hall oracle independently obtains
**10,560 Hall-feasible** source factor pairs, verifying the formula.
The rest `207025−10560=196465` are original-Hall-deficient.
Unlike a local independent-incidence heuristic, this is a
TRUE universal ORIGINAL global source matching capacity.

**Limit:** J29 counts Hall-feasible factor triples *before* the
physical source triples are selected by f/g A-half occupancy,
before restriction to endpoint-bad three-paths, and before
positional D6 alignment. It does NOT imply a positive lower
bound on the number of Hall-feasible keys *demanded* by the
endpoint seed population. The independence of physical f/g
from GQ incidences is neither assumed nor asserted. Thus
J29 alone does not prove S=Ω(s⁶).

## 5. Reproducible exact ORIGINAL checks

`research/hyp105_issue230_jpkc008_source_hall_coherence.py` and independent tests perform:
1. an **EXHAUSTIVE** check of all \(\binom{15}3^2=207025\) true original 3×3 point-line factor pairs on one genuine W32 source geometry, independently comparing all 7 Hall subsets to all 6 matching permutations (rejects multiple perfect matchings);
2. complete W32 lex/reverse/S68/S72 actual physical endpoint-bad P3 populations, matching genuine original incidences to the EXACT previous JPKC-007 stage totals and the independently constructed JPKC-006 source-positive D6 Q output;
3. source demand factor-pair key deduplication on ONE global original f,g, immutable Hall feasibility/unique matching across physical P3s, and strict J28 prohibition on use of the SAME exact source key by distinct original nonincident anchors;
4. true W34 lex/random and the true ORIGINAL D4 Desarguesian symplectic-spread globally injected f,g, over **8 deterministically spread-out true endpoint-bad P3s each** (all 3×3 source pairs completely checked per chosen seed; NOT a full W34 scan);
5. fail-closed illegal maps, W34-as-W32 requests, invalid or overflowing true source demand budgets, and non-distinct or out-of-range source factor triples.

Dedicated small GitHub-hosted workflow, independent Research/INDEX/Proof Audit workflows. No self-hosted runner. No W34 full GF5 seven-family S census.

## 6. Scientific consequence and the next actually open hurdle

J25/J26/J28 show that **the overwhelming original-incidence matching failures** in JPKC-007 cannot be treated as six independent assignments: each true triple of source point factors and triple of source line factors has only 0 or 1 admissible ORIGINAL bijections, with an exact Hall obstruction for the zero case. This sharpens the source-level arithmetic and identifies which shared demands are inherently impossible.

However there is NO universal ALL-h lower bound on the *number* of Hall-feasible source triples seen by the physical endpoint-bad seed population, and there is also NO bound making all Hall-feasible source sixsets positionally aligned D6. Neither the Hall identities nor the rigorously anchor-confined finite exact demand reuse disproves a hypothetical sequence with S=o(s^6).

The mathematically appropriate JPKC-009 target is a **joint ORIGINAL source-demand Hall expansion AND physical A/A positional alignment** inequality across many distinct source anchors under globally fixed f,g, potentially tied to the coherent factor fiber tests of D6-AA4-B [#434](https://github.com/definitely-stable/Mathlab/pull/434). Before asserting it, falsify the proposed inequality with true W32 S68/S72, true W34 D4 spread, and an adversarial correlated global assignment. Do not merge or claim Root A/B, full R3 or ASET exponent.
