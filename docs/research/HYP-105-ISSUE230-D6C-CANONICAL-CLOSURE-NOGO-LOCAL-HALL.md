# HYP-105 #230 — D6-C: the ORIGINAL projection-closure NO-GO and finite exact Hall charging

**2026-10-13. New ALL-h NEGATIVE LEMMA for the CANONICAL local closure; finite W32 local repair oracles. ROOT Branch A/B OPEN.** Stacked on [D6-B #401](https://github.com/definitely-stable/Mathlab/pull/401) frozen HEAD `46f8cf23fd5f610abd407979c9432df8f79f0a3b` (all four exact-head CI gates SUCCESS). No merges, no main edits, keep #230/#176/#169 OPEN.

## 1. Precisely stated all-h **canonical closure obstruction**

For ANY `s=2^h`, ANY full globally injective ORIGINAL point and line unordered pair maps `f,g`, ANY physical subgraph `H⊆G`, take a proper oriented physical three-path `z0-z1-z2-z3` in H with four distinct first and four distinct second coordinates. Suppose its endpoint physical pair labels define a NONINCIDENT ORIGINAL pair `(q,r)`. Let its unique TRUE ORIGINAL GQ projection be `q-l-p-r`. Let `e1,e2,e3` be the three ORIGINAL incidences underlying the physical path edges, in path order.

The **canonical six-incidence candidate** is the multiset of `(e1,e2,e3),(q,l),(p,l),(p,r)`. If any incidence repeats, it is NOT a sixset of six distinct original incidences and therefore belongs to NONE of the seven accepted strictly positive classes. If all six incidences are distinct, their physical first-coordinate degree sequence can be read without geometrical averaging:

- the physical P3 uses first coordinates `x0,x1,x2,x3` once, twice, twice, once respectively;
- the additional incidence `(q,l)` adds f(q)={x0,x3}, yielding degree **two** on all four original path first coordinates;
- the two distinct new original incidences `(p,l),(p,r)` each contribute f(p), hence increase both coordinates of the physical pair f(p) by **two**.

Therefore the canonical candidate has **exactly six first coordinates each of degree two** if and only if `f(p)` is disjoint from all four first path coordinates. If f(p) intersects any of them, that physical first coordinate has degree four, violating the accepted six-coordinate 2-regular condition. The identical argument on the right: three-path + g(r) gives four coordinates of degree two; the two extra original incidences sharing original line l add g(l) **twice**. The right half is 2-regular on six coordinates iff g(l) avoids all four right path coordinates.

Thus **for every all-h ORIGINAL nonincident path with any of D1's mask bits LE,LI,RE,RI set**, its UNIQUE GQ-projected candidate is NOT in ANY of the seven accepted GF(5) positive original sixset families. This is a rigorous negative lemma about the **specific canonical closure map**, not a no-go for alternative nonlocal repairs, a lower bound on S, or Branch B. The converse leafless statement does NOT claim every alternative original 2-regular class is positive: for zero mask, PR394 independently proves the canonical closure is accepted **B/B-overlap** with oriented path multiplicity two. No universal small-blocked-path conclusion follows.

**Consequences for proof search.** Any viable charge for a blocked path MUST replace at least one incidence relative to the canonical GQ closure or use a different, noncanonical combinatorial target. Counting blocked path projections as accepted sixsets without this substitution is mathematically impossible. A Hall estimate on the canonical map alone is **vacuous**.

## 2. More ambitious three/two/one-source-incidence-preserving local repair

For the first genuine all-seven exact-instance `W(3,2)` with `a=6`, let `A(f,g)` be the **complete** accepted seven-positive-family original **six-incidence** target set, as computed independently by accepted E1-B0. Each oriented blocked physical H path P corresponds to exactly three DISTINCT original source incidences `T(P)`, despite possibly two physical diagonals belonging to the same original incidence: the proper four-distinct-first-coordinates requirement rules out repetition.

Test the explicit, falsifiable local transfer family, parameterized by `r∈{3,2,1}`:

```
R_r(P) = { Q in A(f,g) : |T(P) ∩ Q| >= r }.
```

An r-preserving charging rule chooses one recipient Q for every oriented blocked P from R_r(P) and may use the same target Q at most K times. Sources are grouped by identical ORIGINAL triple T: demands `w(T)` count ALL true oriented paths with that triple; they are not divided by reversal symmetry or 3!/6! permutations.

There is an exact finite integer network:

```
  source -> T               capacity w(T)
  T -> Q  if |T intersect Q|>=r    capacity totalDemand+1
  Q -> sink                capacity K
```

The minimum maximum congestion is the least K for which integral maxflow equals `C_H`. Max-flow integrality proves existence of an assignment at that K. When K-1 fails, the residual-reachable source subset U and its COMPLETE neighbor target set N(U) certify the **exact capacity Hall obstruction**

```
    sum_{T in U} w(T) > (K-1) |N(U)|.
```

The implementation verifies the actual maxflow deficit equals the Hall deficit, not merely a heuristic greedy matching. If any source triple has no recipient at all, it supplies a **direct local rule no-go** independent of K; the source triple, ORIGINAL endpoint q,r, projected p,l, 16-bit mask, and full physical grid path are explicitly reported. For r=0 there is the trivial global capacity floor ceil(C_H/S), but r=0 does not preserve any geometry and is not accepted as a meaningful proof route.

**Quantifiers:** An r-preserving transport that fails for one W32 case is false if formulated for every s>=2. It does NOT refute an asymptotic all-h theorem with h>=h0 beyond W32, nor rule out more complicated source-dependent GF5 repairs. If finite r=1 has bounded K, this K is ONLY a finite optimal integer; it may grow with s and does NOT prove any asymptotic Lambda bound.

## 3. Complete independent genuine ORIGINAL finite-falsification protocol

[Source](../../research/hyp105_issue230_d6c_local_charge_hall.py), [tests](../../research/test_hyp105_issue230_d6c_local_charge_hall.py). Evaluate W32 **lex** and S68 globally coherent original maps; for each one examine four true coherent retention policies:

1. FULL TRUE G — substantive original blocked-path source pool. Compute COMPLETE r=3,2,1 exact local Hall optimal capacities (or zero-repair witnesses).
2. FINITE-CALIBRATION — explicitly relaxed D6B H, not the original PR394 theorem.
3. COHERENT every 19th ORIGINAL incidence — nontrivial paired physical H.
4. LITERAL PR394 spectral pruning — empties W32 and must be marked `EMPTY-SOURCE-NO-INFERENCE`, NEVER a claimed successful zero-congestion rule.

For every source P, reconstruct its 3 distinct ORIGINAL edge IDs independently via actual retained physical edge->source identity and its ORIGINAL q-l-p-r projection. Verify the canonical sixset physical half-degrees: zero-mask is genuine accepted original B/B-overlap; every nonzero mask is either a repeated original incidence or a non-leafless true sixset, and is therefore NOT accepted in any of the seven classes. Check the complete D6B retained original sixteen-mask ledger independently by fixing original nonincident endpoint pairs, neighbors, and middle physical H edge.

For repair, compare all accepted seven-class target **true original six-incidence supports** with source triple intersection, not precomputed per-pair scores or signed GF5 events. The classifier/target count is independently pinned. Require exact integer deficits and per-mask conservation. The finite output includes explicit W32 first-obstruction witnesses and a Hall cut when optimal K exists.

## 4. What remains OPEN

The source-to-target overlap rule is **not** itself a universal compensated inequality, even if a finite K is found. To establish `C(H)<= (16-eta)s^6+Lambda S+o(s^6)` for the original coherently pruned large-s H, one must derive a uniform bound for all globally correlated original f,g and independently certify that the charge handles both endpoint and INTERNAL-only masks with h-independent congestion. Alternatively find a rigorous all-h **source-mass deficit** for families with no local recipient, or a new nonlocal transfer with a legitimate original-support witness and quantified multiplicity.

W34/W38 all-seven positive S is UNKNOWN. They are not silently substituted by synchronized BB, so their local all-target Hall optimum is deliberately not claimed. No full R3 risk bound, no ASET exponent, no root A/B classification and no merge to main. Hosted Contract, INDEX, parent Proof Audit, full Research at the final exact D6-C HEAD and independent mathematical review are separate acceptance conditions.
