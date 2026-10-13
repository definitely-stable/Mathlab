# HYP-105 issue #230 — D6-B: true ORIGINAL coherent PR394 retention and coupled E/I/C ledger

**2026-10-13 — OPEN_WITH_FORMAL_BLOCKER / FINITE EXACT CERTIFICATES ONLY.**
Stacked child of D6-A [Draft PR #400](https://github.com/definitely-stable/Mathlab/pull/400) at frozen head `9e5752c1fc175e1050ad460b76ccc25722839845`. This work preserves `main`, never merges the Draft scientific stack, and keeps #230, #176, #169 open. The root universal seven-motif lower `S_s(f,g)=Omega(s^6)` remains **UNPROVED**.

## 1. The specific unresolved all-h implication

The parent [PR394 path-reservoir proof](HYP-105-ISSUE230-PROJECTION-CLOSURE.md) constructs for every globally injective original `f,g` and sufficiently large `s=2^h` a coherently pruned TRUE physical graph `H'⊆G` with `(16-o(1))s^6` oriented proper endpoint-complete three-paths. It proves:

```
(16-o(1))*s^6 <= C(H') + 2*S(f,g) + sqrt(192*m*S(f,g)).
```

Here `C(H')=E(H')+I(H')` is the EXACT ORIGINAL nonincident-projection blocked mass. D5 proved the **unconditional** auxiliary energy `W_H=o(s^(59/10))` false on its infinite explicit spread family even after deleting `o(s^4)` arbitrary physical edges; nothing about full seven-family S follows.

D6-B's goal is to reproduce *the actual PR394 coherent retention on actual GQ and same f,g*, NOT to present full-G measurements as evidence about the pruned H'. It also tests separately whether endpoint-only analysis ignores internal-only blockers.

## 2. Deterministic faithful PR394 pruning on original incidences

For each ORIGINAL incidence `e=(p,l)`, keep its two physical diagonal edges as **one atomic object**. Every deletion stage deletes entire e; a physical edge uniquely identifies its original incidence by full global pair-injectivity. Represent each intermediate graph by a subset of ORIGINAL incidences. Let `a=min{b:binom(b,2)>=V}`, `V=(s+1)(s²+1)`, `Delta=s+1`.

Use the PR394 **spectrally refined** variant (not its original coarser `L=s^(3/4)` variant):

1. `kappa=floor(s^(1/16))`. For each first physical coordinate `u` determine how many `K_a` edges incident to u are missing from *the complete f(P)*. Similarly for each right coordinate from *the complete g(L)*. Delete any true original incidence whose physical diagonal endpoints lie on a bad row or column with missing count exceeding kappa.
2. In the ORIGINAL FULL physical G (PR394's named ORIGINAL graph), for each grid vertex z and each fixed neighbor **first** coordinate and each fixed neighbor **second** coordinate, compute the full original neighbor block. For every block `b>s^(1/10)`, delete all source incidences of those edges, and consequently each opposite diagonal. This is one simultaneous original-block sweep; NOT adaptive repeated removal of blocks after earlier deletion.
3. On remaining graph, repeatedly choose the lowest-index grid vertex of positive degree `d<s^(31/32)`, and delete all its source incidences, including the other physical diagonals. Stop only when no positive low-degree vertex exists; isolated grid vertices are ignored.

No floating-point exponents are used. The exact integer decision predicates are:

```
kappa = largest integer k such that k^16<=s
big original physical block iff b^10>s
positive retained vertex is low iff d^32<s^31
```

Thus our finite `s=2,4,8` experiments do not depend on numerical imprecision. Validate independently that **all** retained physical edges come in source-incidence pairs, retained `t_H` obeys `t_H^10<=s`, and every positive retained degree `d` obeys `d^32>=s^31`. Each original incidence belongs to exactly one of four categories: retained or deleted in stage 1, 2, 3; no synthetic/non-original grid edges appear.

**Finite-size warning:** for all s in {2,4,8} kappa=1 and the integer block cap is b<=1. In the large-s theorem this threshold grows, but at small s it is exceptionally restrictive. The proof's asymptotic `m(H')=(1-o(1))*m(G)` is NOT claimed for these h. If the literal finite H' is empty, `W=E=I=C=BB=0` is a vacuous finite output, **not** evidence of the universal compensation inequality. Such a case is not treated as a proof nor as a regression error.

## 3. True retained E/I/C census with independent ORIGINAL endpoint oracle

[Implementation](../../research/hyp105_issue230_d6b_coherent_pruning.py), [regression tests](../../research/test_hyp105_issue230_d6b_coherent_pruning.py).

For each retained graph H, exhaust all proper oriented physical P3 with four distinct first and four distinct second coordinates. Identify physical endpoint pair labels by the **same complete** f and g, not by remapping the retained incidence subset. If both exist, classify whether original (q,r) are incident in the ORIGINAL GQ. If nonincident, recover the one exact original projection `q-l-p-r` from ORIGINAL W(3,s); classify four bits:

```
1: f(p) meets physical endpoint first coordinates
2: f(p) meets physical INTERNAL first coordinates
4: g(l) meets physical endpoint second coordinates
8: g(l) meets physical INTERNAL second coordinates.
```

Count 16 exact disjoint masks `C_b(H)`. Then independently assert

```
proper(H) = missing(H) + incident(H) + sum_b C_b(H)
E(H) = sum_{b&5 != 0} C_b(H)
I(H) = sum_{b&5 == 0, b&10 != 0} C_b(H)
C(H) = E(H)+I(H) = sum_{b=1}^{15} C_b(H)
BB_sync(H) = C_0(H)/2, an accepted original sixset subset.
```

Independently enumerate nonincident masks AGAIN by fixing ORIGINAL nonincident `(q,r)`, expanding both antipodal endpoint rectangle diagonals in both orientations, choosing H-neighbors at each end, and testing the middle H edge. This does not reuse the forward P3 traversal or D1's method. D2's separate ORIGINAL projection chord oracle independently computes physical `W_H` and t_H; D5's independently proved retained-energy certificate checks its genuine W34/W38 spread models.

For any H⊆G, the above quantities for valid paths and the nonnegative energy are individually nonincreasing under edge deletion: `E(H)<=E(G)`, `I(H)<=I(G)`, `C(H)<=C(G)`, `BB_sync(H)<=BB_sync(G)`, `W_H<=W_G`. They are useful exact checks, not the required asymptotic upper with fixed eta.

## 4. Control policies — explicitly NOT confused with PR394

Each complete global original model has four regimes:

| Policy | Description | Scientific status |
|---|---|---|
| FULL-TRUE-ORIGINAL-G | All incidences retained | D6-A comparison baseline |
| PR394-EXACT-AS-WRITTEN | Three stages and exact integer power thresholds above | Faithful finite literal asymptotic construction |
| CALIBRATION-NOT-PR394 | Missing-degree cap relaxed to a-1, block cap max(2,floor((s+1)/2)), minimum positive degree 2 | Finite engineering control, **not** the claimed PR394 theorem |
| COHERENT-... | For D5 spread models, delete full original incidences associated with first 20% sorted selected witness physical edges; for W32 delete every 19th original incidence | Adversarial or systematic coherence control, **not** the PR394 pruning |

Every physical removal is paired via its single ORIGINAL incidence; the previous D5 *unpaired* physical-edge deletion model remains independently valid for its theorem but is not mislabeled `coherent`.

Models: two W32 complete maps (lex,S68), two *genuine* W34 D5 spread maps (balanced/reversed globally injective g), plus W38 D5 **literal PR394** retention and independent retained-energy validation. Full seven-family `S` is accepted and known ONLY for W32; it stays unchanged as a function of f,g regardless of H. For W34/W38 full S remains unknown, even if BB_sync(H) is computed exactly.

## 5. What would prove the universal root statement (NOT accomplished here)

A new all-h theorem must use S or a bounded-multiplicity original GF5 sixset charging map to control **both** E and I jointly on this same coherently pruned H'. The sufficient form is

```
C(H') <= (16-eta)*s^6 + Lambda*S(f,g) + o(s^6)
```

for absolute eta>0 and Lambda>=0 and a uniform, map-independent remainder. To avoid circularity one must count ORIGINAL distinct six-incidence sets, not signed GF5 events, physical path orbits, random-label expectations, or only BB_sync. A proposed all-h injection/charge must explicitly bound congestion and prove source/target class compatibility for all h.

The finite experiments can identify and falsify strong local transfer rules, but cannot infer a fixed eta from s=2,4,8. If the literal finite PR394 graph collapses, the correct next step is to study a nonvacuous large-s analytic charging lemma, using the finite-calibration graph only to generate counterexamples and debug local combinatorics. No ASET exponent, complete R3 risk upper, or Branch A/B is established. Keep Draft pending exact-head hosted CI and independent proof review.
