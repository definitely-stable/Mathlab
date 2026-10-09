# HYP-105 G5-E2-B3.2 — Exact coincident six-cycle obstruction for fixed coordinate-pair labels

Date: 2026-10-09. Scope: [issue #176](https://github.com/definitely-stable/Mathlab/issues/176), roots [#169](https://github.com/definitely-stable/Mathlab/issues/169) / [#162](https://github.com/definitely-stable/Mathlab/issues/162). Extends [B3.0 projected six-edge forests](HYP-105-G5-E2-B3-FOREST-PROJECTION.md), [B3.1 exact signed flows](HYP-105-G5-E2-B3-B1-CRITICAL-FLOWS.md).

**PROVED_ALL-s_DETERMINISTIC_NECESSARY_R3_BOUND / EXACT_FINITE_GF2_GF4_OBSTRUCTION_COUNTER / INDEPENDENT_BRUTE_ORACLE / NO_ALL-h_STRICT_R3_UPPER / NO_NEW_ASET_EXPONENT / PRIOR_ART_NOT_YET_VERIFIED.**

## 1. Fixed theorem and strengthened exact GF(5) coefficient

Let `G_s=W(3,2^h)` be the classical symplectic point-line bipartite incidence graph, with `V=(s+1)(s²+1)` vertices per part and `N=(s+1)²(s²+1)` distinct incidence edges. Fix **any** pair of injections `f:P -> binom([a],2)`, `g:L -> binom([a],2)` with `a=min{r:binom(r,2)>=V}`. Incidence edge `e=(p,l)` yields a distinct GF(5) support4 column `f(p) union (a+g(l))`. Coefficients vary over 51 all-nonzero checksum-4 patterns for each column.

Define `D_s(f,g)` to be the number of **unordered six-element factor matchings** `S subset E(G_s)` such that the following holds. Each of the six selected point pair labels and line pair labels uses **exactly six** distinct physical coordinates and is a simple six-cycle (in each color separately); equivalently their *dual column-adjacency* graphs are simple cycles `C6` on the SAME set of six selected column IDs and have identical six adjacency edges.

For every such `S`, there is exactly one unordered balanced `3-vs-3` event given by the alternating bipartition of that shared `C6`. Its signed six-column physical two-color incidence motif is isomorphic to two copies of the same `C6`, independent of physical symbol names. Unlike the previous coarse all-one witness, the E2-B3.1 exact prescribed-boundary count proves

```text
F_(coincident C6/C6, alternating signs)(b;5) = 5643.
```

This equality is independently crosschecked using the actual 51³-side GF(5) sum-histogram meet-in-middle oracle, not the same spanning-subgraph inclusion/exclusion. No other condition on GQ geometry is used.

**Theorem B3.2-A (for every fixed pair-injective labeling, every h>=1):**

```text
R3(B_s(f,g)) >= (5643 / 51^6) * D_s(f,g).
```

Proof: every member of D_s produces the unique alternating unordered 3v3 event with exactly 5643 admissible six-column nonzero checksum-4 coefficient assignments. Different six-edge sets define different events, so their nonnegative risk contributions sum without duplication. All other events only increase R3. QED.

**Necessary obstruction, NOT a sufficient certificate:** any fixed all-h family seeking `R3(B_s)=O(s^(6-epsilon))` MUST satisfy `D_s(f_s,g_s)=O(s^(6-epsilon))` with the same epsilon. Conversely, even D_s=0 leaves every other positive GF(5) motif uncontrolled; this stage does not prove an upper bound on R3 or simultaneous R2.

## 2. Exact mean of the obstruction under independent random injections

Let `M6(G_s)` be the actual number of unordered six-edge **factor matchings** in G_s, `K=binom(a,2)`, and `P6=(a)_6/(K)_6`. For each fixed six-factor matching, the six selected point pair labels are uniformly distinct ordered pairs in the physical pair alphabet, independently of its six line pair labels. There are precisely `6!/12=60` labeled dual column C6 graphs. For any one of them, the probability in one half is exactly `P6`, and the sixty coincident events in both halves are pairwise disjoint. Hence the **exact all-h identity**

```text
E_uniform_pair_labels[D_s] = 60 * M6(G_s) * P6^2.
```

Using the already-proved greedy factor matching lower count
`M6(G_s) >= prod_{j=0}^5(N-2j(s+1))/720` and the elementary `M6(G_s)<=binom(N,6)`, gives explicit bounded lower and upper expectations for D_s and the strengthened

```text
E[R3] >= (5643 / 51^6) * 60 * M6(G_s) * P6^2
       = Omega(s^6).
```

This is still an **expectation over independent random injections**, NOT a lower bound valid for every injection. A fixed structured labeling can lie far below that expectation.

## 3. Exact counting algorithm without scanning C(N,6)

The [reference solver](../../research/hyp105_g5e2b3b2_coincident_cycles.py) accepts the actual incidence edges plus two independently injective physical pair-label arrays.

1. Form the **left physical simple graph** on `a` physical symbols, with one pair edge for each point factor vertex. Enumerate undirected simple six-cycles by DFS, canonically with the least used physical symbol as the first vertex and the smaller neighbor as the second vertex. A left C6 specifies a unique **cyclic order of six distinct point factor vertices**, hence six prospective column slots.
2. For each slot enumerate only actual incident factor lines. Enforce distinct factor line vertices. Incrementally check whether the corresponding six right physical pair labels form a simple coordinate C6 in exactly the same column-slot adjacency order: consecutive pair edges share one coordinate, all six shared symbols are distinct, and the last pair closes to the first.
3. Each output six-set then contributes exactly one to D_s. One valid physical left six-cycle has only the two possible orientations, and canonicalization retains exactly one. Distinct factor matchings cannot share all six chosen `(point,line)` incidences. Conversely, any counted D_s matching uniquely determines its left six-cycle and its ordered line assignment, so no valid event is missed.

This is a proof of **completeness and no double counting**. Let `C6(P_f)` be the number of six-cycles of the mapped left point-pair graph and `Delta=s+1`. A coarse worst-case bound is `O(C6(P_f)*Delta^6)` candidate line assignments, each examined by constant-depth physical-pair checks. It is **not** claimed that this bound is near-linear, nor that six-cycle enumeration will remain practical at arbitrary large h. For h=1/2 the exact solver is resource-guarded and raises if it cannot finish; it never substitutes sampling for an exact result.

## 4. Exact finite evidence, verification discipline and limits

The hosted checker reports D_s, the number of left physical C6 candidates, and actual six-column witnesses separately for the three established E2-A **control** rank-based schemes: lex, reverse-line and coordinate-flag, for s=2 and s=4. These are finite results only. No six-point exponent may be fitted from them and no candidate is a proved algebraic correlated all-h improvement.

Independent correctness checks:
- A bounded brute oracle enumerates actual 6-subsets of a **small selected incidence set**, rejects repeated factor endpoints and computes physical-coordinate degree-two profiles and both *dual column adjacency* edge sets directly, not using the DFS join. It must equal the optimized exact algorithm.
- Full GF2 controls remain invariant under exchanging left/right factor parts and under arbitrary tested permutations of physical coordinate symbols on either side. A full GF4 geometric witness must have six distinct point and line endpoints, matching dual C6 graphs, and a direct **all-one GF5 alternating signed subset-sum zero**.
- The exact C6/C6 signed flow count **5643** is checked by the independent E2-B1 direct full 51³-side GF5 MITM oracle; this numerical coefficient is a finite identity, not an asymptotic inference.

**STOP / no novelty promotion:** this counts only coincident matching C6 motifs; it does not count all the other positive-flow six-column motifs (B3.1-B), cannot upper-bound full R3, and does not prove any common family with `R2=O(s^(26/5-epsilon_2))`. Unaltered named schemes are controls, not new Sp(4,s)-equivariant embeddings.

### 4.1 Hosted exact finite results on accepted E2-A controls

The baseline GitHub-hosted report enumerated all physical left C6 for h=1 and h=2, and computed the EXACT D_s for every control, not sampled:

| Rank-based labeling | s=2, N=45, a=6 | s=4, N=425, a=14 |
| --- | ---: | ---: |
| lex | 15 | 8,481 |
| reverse-line | 3 | 8,417 |
| coordinate-flag | 3 | 10,602 |

The left physical factor-point pair graph has exactly **60 C6** at s=2 and **121,320 C6** at s=4, independent of the line-label control because all three use the same point labels. The h=2 exact candidate loop has 121,320 left cycles rather than an enumeration of `binom(425,6)` candidate six-sets. The strict GF5 obstruction lower for a fixed label is the reported D_s multiplied by **5643/51^6**, not a count of actual final ASET violations under a particular coefficient assignment.

At s=2, reverse-line/coordinate-flag reduce D_s by 5x versus lex, but at s=4 reverse-line is only slightly smaller than lex, and coordinate-flag is larger. Two finite field sizes do **not** justify fitting an asymptotic exponent or a claim that one of these controls solves the simultaneous R2/R3 condition. Existing E2-A rank orderings are NOT symplectic equivariance proofs.

## 5. Research decision

**Next B3.2-B:** use the exact D_s diagnostic to propose a genuinely geometry-aware *correlated* all-h pair labeling, with a published proof of injectivity for every h first. Require quantitative suppression of D_s AND a simultaneously proved bound on R2, then address every other positive GF5 motif class before claiming R3. If D_s stays large, prioritize classification of the other exponent-six motifs or a dependency-aware independent-set theorem. Keep issue #176 and scientific roots OPEN. Do not create Rust packages or claim a new ASET exponent.
