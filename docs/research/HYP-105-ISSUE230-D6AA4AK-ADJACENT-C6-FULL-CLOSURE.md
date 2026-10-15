# HYP-105 / #230 — AA4-AK: full genuine-original connected C6 closure at adjacent physical pins; global internal-link pre-Hall mass

**Research-only mathematical Draft; root #230 = OPEN_WITH_FORMAL_BLOCKER; AK-3 is the nonduplicated result.** Parent: [AA4-AJ PR #521](https://github.com/definitely-stable/Mathlab/pull/521), exact pinned HEAD `195f80eb7d8770d6f0ddce0d59087f13c9f9e0e4`. Scientific parallel predecessors: [AA4-AI pencil #518](https://github.com/definitely-stable/Mathlab/pull/518), [AA4-AJ 2+2 #522](https://github.com/definitely-stable/Mathlab/pull/522), [AA4-AJ source-site cap #523](https://github.com/definitely-stable/Mathlab/pull/523). AJ #521 **already exhaustively solved disjoint pinned physical C6** (two crossed-spoke + four internal-link templates). Do NOT repeat or rename its proof. This AK work addresses the **missing adjacent pin sector** and a new globally quantified original line-pencil/internal-link physical candidate bound. Neither is an all-seven positive-Hall bound.

## Live overlap / originality correction (15 October 2026)

**Verified concurrent overlap:** [scientific Draft #524](https://github.com/definitely-stable/Mathlab/pull/524) already treats adjacent-pinned original B/A complete A sectors, and [scientific Draft #525](https://github.com/definitely-stable/Mathlab/pull/525) already gives the SAME adjacent connected-C6 source upper bound `24(s+1)^2`, a different sparse source algorithm, plus a *conditional* adjacent physical occupancy and Hall-dilution upper. **Accordingly AK-1 and AK-2 BELOW ARE NOT CLAIMED AS NEW ORIGINAL RESULTS IN THIS PR.** They are independently implemented cross-validation/falsifiers of those concurrent mathematical claims; their acceptance and integration must be judged separately. The true new nonduplicated theorem here is **AK-3: ALL-global-map unconditional source-indexed INTERNAL-LINK (disjoint pins, all four physical crosslink-hole elimination) physical pre-Hall mass `P_link>=s^14/384` for s>=16**, which neither #524 nor #525 asserts. Do not conflate conditional per-adjacent-pair occupancy from #525 with unconditional global original-rooted 1+3 presence here.

This PR intentionally retains code/tests for the adjacent transfer as independent checks on its UNIQUE new all-map pre-Hall theorem's source/model semantics. On integration, reconcile/prune redundant portions rather than stacking separate duplicate public theorem claims.

## Model and exact scope

For every integer h>=1, s=2^h, genuine indexed symplectic generalized quadrangle W(3,s) with V=(s+1)(s²+1) original point factors and V original line factors, degree d=s+1, bipartite original incidence graph of girth eight. The physical alphabet is K_a, a=min{t:C(t,2)>=V}, with exactly m=C(a,2)-V<=a-2 unoccupied physical unordered edges for each typed image separately. Maps f and g are **each complete and globally injective** on their typed original source-factor domain and **arbitrarily correlated**. We always count six *DISTINCT ORIGINAL incidence IDs* on the SAME source sixset Q in both physical projections.

Fix one actual original doubled B root p (or its dual), two distinct actual original flags through p with opposite original factors l0,l1, and an occupied first-side complementary B physical four-cycle composed of four OTHER distinct original source factors q0,q1,q2,q3. The frozen positive six-coordinate GF(5) B/A (or A/B) condition on the opposite side is a simple occupied six-vertex twofactor, and the original source matching weight is the exact permanent of the actual 4x4 GQ incidence submatrix, hence 0,1,2 (girth eight).

## AK-1 exact adjacent pinned physical C6 classification

Assume the two opposite pinned physical images share ONE physical coordinate, so e0={u,v}, e1={v,w} with u,v,w distinct. There are precisely three pinned physical coordinates. The six-vertex physical connected C6 containing these pinned edges must be

```text
u -- v -- w -- y -- z -- t -- u
```

for **three pairwise distinct auxiliary physical coordinates** y,z,t outside {u,v,w}. The four unpinned physical edges are {w,y},{y,z},{z,t},{t,u}; all must belong to the ONE actual globally injected opposite typed image. The order (y,z,t) is uniquely recovered from each H because the path after deleting the two adjacent pinned edges has distinguished ends w and u. Consequently physical COMPLETE K_a adjacent-pinned C6 capacity is EXACTLY

```text
(a-3)(a-4)(a-5) = 6*C(a-3,3).
```

No factor-two/oriented-cycle or physical automorphism quotient is applied. Independent brute physical full-twofactor census on *every* adjacent physical pinned pair of K6, K7, K8 checks exact equality, and edge-hole deletion falsifiers check occupied (not imaginary surjective) patterns.

### AK-1 genuine ORIGINAL incidence-anchored 4-by-4 Hall transfer

Let N(q) denote the **actual original** degree-d opposite neighborhood, and let `G^{-1}(xy)` denote the actual inverse source factor for a globally occupied physical edge xy. In any accepted original Q, the unique original singleton row q_k assigned to the middle physical edge {y,z} must satisfy

```text
t_yz = G^{-1}({y,z}) in N(q_k).
```

Enumerate original row `k=0..3`, one of its d actual opposite incident factors t_yz whose globally injected physical edge has **both endpoints outside {u,v,w}**, and the two ordered assignments (y,z) of those physical endpoints. For each `j != k`, accept the physical outer edge {w,y} only if globally occupied and its inverse factor is an ACTUAL original neighbor of q_j. The remaining two singleton rows `R=[4]\{k,j}` must be matched bijectively to the two actual opposite factors

```text
G^{-1}({z,t}), G^{-1}({t,u})
```

for an auxiliary physical site t outside the three pinned vertices and distinct from y,z. This contributes the **true original 2x2 permanent**, which is 0 or 1 by the forbidden original GQ C4.

The exact formula, with all operations on the one common global physical map, is

```text
T_adj =
  sum_{k=0}^3 sum_{ell in N(q_k)} sum_{(y,z) orientation of G(ell)}
     1[y,z outside pinned triple]
     * sum_{j in [4]\{k}} 1[G^-1(wy) in N(q_j)]
     * sum_{t outside pinned triple,y,z}
           per_2( incidence of q_([4]\{k,j}) to
                  [G^-1(zt),G^-1(tu)] ),
```

where any absent physical inverse `G^{-1}` contributes zero. **Proof of exactness.** Every physically occupied connected C6 with adjacent pins has the unique u-v-w-y-z-t-u representation. Each accepted actual original 4-rook bijection assigns **exactly one** q_k to the unique physical edge yz and exactly one different q_j to wy; the other two genuine rows are assigned bijectively to zt,tu. Conversely every term builds one such six original incidence-ID set and a genuine original source perfect matching. Distinct matched permutations are counted as distinct accepted source-incidence sixsets; when the same physical H admits two original GQ matchings its permanent contributes two, as already required by AA4-AE's induced C8 accounting. Hence the formula is EXACT for every h, all physical holes, arbitrary f,g, both typed orientations. QED.

**NEW all-h per fixed cohort upper.** For each k there are at most d TRUE original middle-edge factors; there are two orientations and at most three j. At fixed k,ell,(y,z),j, the set of eligible t admitting the genuine 2x2 matching injects into the degree-d original opposite neighborhood of either one of the two remaining rows: the matched original factor physically has edge {z,t} or {t,u}, which varies injectively with t (and local two-rook perfect matching is UNIQUE because GQ girth eight). Therefore at most d sites t occur. Consequently, for EVERY genuine fixed root/flags/B-C4 cohort with physically adjacent pins,

```text
0 <= T_adj <= 4 * d * 2 * 3 * d = 24(s+1)^2.
```

This is a **genuine accepted GF5 UPPER, not an all-global-maps positive lower**; it does not conflate a physical C6 with an actual original Hall-accepted Q.

### AK-2 full connected-C6 completion

Sibling #521 exactly counts the disjoint pinned physical C6 source acceptance, including both its 2-spoke and all four internal-link templates. New AK-1 counts **all** adjacent-pinned physical C6. These are mutually exclusive, exhaustive and their sum gives the entire B/A or A/B **connected physical C6**, for all h, all original f,g and each genuine physical B-C4 rooted cohort:

```text
T_connected_full = T_connected_disjoint_AJ521 + T_connected_adjacent_AK.
```

Independent finite oracle enumerates ALL pinned physically occupied original A twofactors in the prior AA4-AI implementation and directly counts actual 24 source bijections without reference to the AJ or AK reductions. Thus the combined formula closes a **previously missing exact sector**, but not the positive Hall minimax.

On the one frozen complete genuine original W(3,2) zero-split witness from #519, for ALL original 15 roots x three genuine flag pairs x three real physical C4, both orientations:

| Genuine original side B | Physical occupied C6 with disjoint pins | Accepted original disjoint | Physical occupied C6 with adjacent pins | Accepted original adjacent | FULL accepted connected |
|---|---:|---:|---:|---:|---:|
| original points | 504 | 17 | 558 | 23 | 40 |
| original lines | 756 | 41 | 432 | 17 | 58 |

The data reconcile to historical full connected physical mass 1062 / 1188 respectively. These are genuine finite counts, **not** an asymptotic theorem.

## AK-3 independent all-map ORIGINAL 1+3 internal-link pre-Hall bound

For disjoint opposite pinned physical edges e0={u,v},e1={w,x}, sibling #521 proved an exhaustive physical connected C6 internal-link class with FOUR possible direct physical cross-links between their pinned endpoints, each occupied physical direct cross-link h together with a three-edge bridge with two auxiliary outside coordinates y!=z. **New obstruction:** a safe source rootpair from #518 does NOT necessarily have any of its four direct cross-links globally occupied. We address this with an ORIGINAL-GQ source rootpair count, **not** an independence assumption.

The pencil-aware #518 bound, on the **one common opposite global g**, gives at least

```text
N_safe = [V*C(d,2) - a*C(a-1,2) - floor(32m/a)*(a-1)*d*(d-1)]_+
```

genuine original rooted two-flag pairs whose pinned physical edges are disjoint and none of the four pinned physical coordinates is *hot* (each missing physical degree < a/16). A physical missing edge {x,y} can be a cross-link between a physically disjoint unordered pinned pair `{{x,r},{y,t}}` in at most `(a-2)(a-3)` ways. Because the original GQ has **at most one source root** for each pair of real original intersecting line factors, distinct genuine rooted source pairs are injective into physically distinct unordered pinned pairs. Every genuinely safe source rooted pair with **ALL FOUR** cross-links missing is charged to FOUR such missing-edge incidences. Consequently

```text
B_dead <= floor[m*(a-2)*(a-3)/4],
N_link >= [N_safe-B_dead]_+.
```

For every remaining source rootpair, at least one of the FOUR physically direct cross-links exists in im(g). Choose any one h. Let r0 and r1 be its other two pinned endpoints. They are *cold*, so for the same fixed global map, each of their physical outside-neighbor sets has size >=15a/16-4. The number of ordered pairs y!=z outside the pinned four physical coordinates with occupied edges `r0-y, y-z, z-r1` satisfies

```text
>= (15a/16-4)^2 - a - 2m
>= a^2/4                    for a>=32.
```

The second inequality follows by `m<=a-2` and the positive increasing polynomial `161a²/256 -21a/2 +20>0` at all a>=32. A missing unpinned central yz edge invalidates **at most two orientations** of the ordered physical (y,z), so the 2m union bound is valid even for adversarially placed holes. All six physical edges are occupied actual inverse source factors under the *same* g. The physical 1+3 C6 H are distinct and are counted with original root/pinned-flag/C4 provenance.

At EVERY actual original point p, every complete globally injected first-side f has at least the existing #518 occupied complementary first physical C4 floor

```text
C4_floor=[3*C(a-2,4)-m*(a-4)*(a-5)]_+ .
```

Thus the **NEW deterministic global pre-Hall physical indexed floor** is

```text
P_link(f,g) >= N_link*C4_floor*ceil(a²/4).
```

For **all powers s=2^h>=128**, #518 proved `N_safe>=N/2`, with `N=V*C(s+1,2)>=s^5/2`, `a<=3s^(3/2)/2`. Our new missing-cross bound satisfies `B_dead/N<=a^3/(4N)<=27/(16 sqrt(s))<1/6`, so `N_link>=N/3`. Also `C4_floor>=a^4/128` and `a²>=2V>=2s³`. Therefore

```text
P_link>= (N/3)*(a^4/128)*(a²/4) >= s^14/384.
```

For the **only smaller powers** in the claim, exact integer closed-form cases (no fitting, no asymptotic extrapolation):

| s | minimal a | missing m | N_safe from #518 | max fully unoccupied-cross source pairs B_dead | NEW N_link floor |
|---|---:|---:|---:|---:|---:|
| 16 | 94 | 2 | 192052 | 4186 | **187866** |
| 32 | 261 | 105 | 5777010 | 1754077 | **4022933** |
| 64 | 731 | 510 | 292596665 | 67665780 | **224930885** |

Direct exact integer multiplication in the oracle verifies `384*N_link*C4_floor*ceil(a²/4)>=s^14` in each case. The all-h statement is:

```text
FOR ALL h>=4, s=2^h, EVERY complete genuinely original global f,g:
  P_link(f,g) >= s^14/384.
```

**IMPORTANT:** This P_link counts **physically occupied 1+3 connected-C6 patterns before checking the real original 4x4 Hall permanent**. It does **NOT** bound the accepted GF5 six-ID counts below. An adversarial original source matching can vanish locally even when P_link is huge. The previous sibling #521 even bounds original accepted 1+3 internal-link motifs by `192(s+1)` PER fixed source C4/root/pinned pair, highlighting this source/physical discrepancy. No positive all-map S, no Branch B infinite counterfamily, no strict R3/ASET follows.

### AK-4 — NEW all-global genuine-original Hall-FAILED INTERNAL-LINK mass theorem (NON-Hall lower)

The separate exact original-incidence source transfer of parent #521 bounds accepted genuine original *internal-link* 1+3 Q per fixed root/true-flags/occupied B-C4 by **`192d`**, where d=s+1. Each of the newly certified `N_link*C4_floor` genuinely original global-map-safe ACTIVE cohorts from AK-3 has **at least `ceil(a²/4)` occupied 1+3 physical C6 patterns**. Each Hall-positive physical H contributes at least one distinct genuine original accepted source Q; thus the number of Hall-positive H is at most the accepted Q and

```text
fraction(Hall-positive physical internal-link H in each ACTIVE cohort)
   <= 192d / ceil(a²/4)
   <= 768d / a²
   <= 384/(s²+1),
```

using only `a² >= 2V =2(s+1)(s²+1)`. This is an **UPPER on positive original Hall incidence**, NOT an all-map positive lower. Summing the nonnegative complementary Hall-FAILED counts over every safe-active original-indexed root/pins/C4 cohort gives

```text
FOR EVERY complete original globally injected f,g, EVERY s=2^h>=32:
  R_link,Hall-FAILED(f,g)
    >= (1-384/(s²+1)) * P_link,certified
    >= (1-384/(s²+1))*s^14/384 > 0.
```

This is a new unconditional all-global-map genuine ORIGINAL **Hall-FAILED** candidate lower `Omega(s^14)` in the specific internally linked connected-C6 physical sector, with a stronger forced failure fraction `1-O(s^-2)`. It improves the explanatory source-vs-physical barrier: despite guaranteed physical occupancy for arbitrary correlated maps, almost all of these indexed candidates are necessarily source-Hall rejected. It **cannot** establish `S_s>=Omega(s^6)`; even an all-map physical Hall success fraction as small as `Theta(s^-8)` remains compatible with the upper bound. The earlier parallel #523 establishes a separate forced Hall failure on the split-two-triangle sector with different `1-O(s^-1)` factor. Neither result implies Branch A/B/C. The code provides exact `fractions.Fraction` certificates for every power h up to 42 and the analytic bound holds for all larger h.

## Verification and next missing lemma

Versioned code: `research/hyp105_issue230_d6aa4ak_adjacent_c6_full_closure.py`, tests: `research/test_hyp105_issue230_d6aa4ak_adjacent_c6_full_closure.py`, dedicated hosted workflow.

- **Oracle I** (incidence anchored): genuine original `q_k -> g^-1(yz)` middle-edge restriction; actual globally shared opposite source neighborhoods; 2x2 GQ source rook transfer, including source-cycle double charge; bound `24(s+1)^2`.
- **Oracle II** (independent): enumerate EVERY physical complete A twofactor with adjacent pinned edges, keep occupied connected C6, invert each of four actual globally injected physical opposite edges, count all 24 REAL original 4-row/4-factor bijections. It NEVER uses middle-edge anchoring or decomposed site sets.
- **Finite falsification:** every adjacent pinned K6/K7/K8 pair, edge-deletion holes, all 135 root/flag/C4 cohorts in each typed direction for true original W32 global zero-split witness, lex/S68/S72 alternate true W32 global maps, genuine W34 K14 non-surjective physical injection both orientations, true symplectic common point/line source automorphism and independent physical coordinate permutations, invalid domains and source maps; all h=1..42 integer analytic evidence, plus explicit s=16/32/64 boundary values.
- **Prior art:** source GQ girth eight and bounded-degree structure are classical generalized-quadrangle facts; Laplace/permanent restrictions are standard. Applied original-GQ rooted physical occupancy / exact globally coherent adjacent-pinned source transfer is the scoped new claim. This document makes no literature-wide originality claim.

**Next mathematical gate:** all-map lower on TRUE original Hall-positive GF5 across every relevant sector (the complete B/A and A/B original connected C6 now has exact transfer, not lower), plus all remaining five GF5 tags and D6 if pursuing Branch A/B. A sufficient restricted Hall-density `Omega(s^-8)` does not follow from large physical P_link or adjacent capacities. Do not promote science Draft merely because tests succeed.

**Integration:** AK is strict Draft child of #521; #522 is a parallel 2+2 subset of #521 and #518/#523 are parallel separate scientific stacks. Integrate scientific proofs only after independent mathematical referee, exact final HEAD dedicated/INDEX/Proof Audit/Full Research and reconciled ancestry, then regenerate derived structured registries from canonical JSON; do not hand-edit `registry/*.md` or close #230.
