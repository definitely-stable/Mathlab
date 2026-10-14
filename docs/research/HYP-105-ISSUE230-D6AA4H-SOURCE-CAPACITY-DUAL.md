# HYP-105 #230 — D6-AA4-H: exact source-profile/capacity dual and physical-cut sufficiency frontier

**Scope: exact all-h one-cut weak dual, explicit s=4 capacity-pseudomarginal falsifiers, actual complete W(3,2) 24-state ORIGINAL-line-profile evidence, and a rigorous W32 scalar-capacity NO-GO.** Branch A all-h positive S_s >= c s^6 and Branch B infinite low-S family both remain OPEN. No full R3, ASET exponent, standard Sherali-Adams/SOS claim, or whole W32 minimum.

Stacked research-only Draft on [AA4-G #446](https://github.com/definitely-stable/Mathlab/pull/446) at final parent SHA f68d6de96af77035ad66dbe5b8cfecd061fd94e4. main is untouched; nothing merged. AA4-G's dedicated/INDEX/proof-audit CI were green; final full Research must be checked independently.

## 1. Main result — exact weak capacity multiplier theorem for every genuine W(3,2^h)

Fix any h>=1; original W(3,s) has V=(s+1)(s^2+1) genuine points and V lines, both assigned separately injectively to physical two-coordinate edges of K_a, K=binom(a,2), minimal K>=V, m=K-V. For any complete real map x=(f,g), let C(x) be its exact nonnegative ORIGINAL six-distinct-incidence seven-class GF5 score (or the nonnegative certified GF5 necessary floor numerator), counted once per ORIGINAL sixset. Let A_P(x),A_L(x) be the true physical image occupied adjacent edge-pair counts for the two types. Sharp valid capacity bound from D6-Y (Ahlswede–Katona special case):

A_t(x) <= Amax = a*binom(a-1,2) - 2*m*(a-2) + binom(m,2), t=P,L.

Let each q_j(x)<=0 be ANY rigorously proved valid additional full-map inequality (e.g. minus a genuine lifted physical-edge column inequality), in exactly stated physical/source coordinates. Fix an explicit candidate relaxation universe U containing an exact representation of **every genuine complete map** of the scope to be certified; each u in U has a well-defined cost C_U(u), consistent with C(x) on all genuine maps, and corresponding cut values q_j(u) consistent with the genuine values there. For any NONNEGATIVE rational vector lambda:

B_U(lambda)= inf over u in U of [C_U(u) + sum_j lambda_j*q_j(u)]
<= inf over all genuine x C(x).

**Proof:** every genuine x satisfies q_j(x)<=0, so C(x)+sum lambda*q_j(x) <= C(x); since x appears correctly in U, the infimum over U is <= this value. Minimize over genuine x. This is ordinary finite/tiny-scope Lagrangian weak duality, not a novel convex optimization theorem. The important formal gates are (i) the full original seven-class cost on genuine x, (ii) the correct inequality sign, and (iii) candidate-universe coverage. If U omits genuine maps, NO GLOBAL LOWER-BOUND CLAIM IS VALID.

Implemented exact rational one-constraint solver maximizes min_u (c_u + lambda*g_u) for lambda>=0 by exhaustively enumerating nonnegative intersections of all pairs of affine candidate rows and endpoint lambda=0. It requires at least one row with g<=0; computes exact active rows and rational optimum. A future multicut/cutting-plane LP needs independent verification of its full candidate universe and its actual GF5 local source-marginal realization.

## 2. Independent exact D6-X/Y unit-cost toy witnesses — NOT ORIGINAL GF5 risk

At genuine s=4: V=85, a=14, K=91, m=6. D6-Y true maximum occupied-edge adjacency is 963; the specified selected lifted-column-passing two-site pseudo has expected 1020, violating the valid image cut g=A-963 by 57. Take an EXPLICITLY SYNTHETIC two-candidate universe: one labeled real-capacity-feasible control with artificially assigned cost ONE and g=0; one pseudocandidate with artificially assigned cost ZERO and g=57. Their exact Lagrangian envelope is

max_{lambda>=0} min(1, 57*lambda) = 1, attained at lambda=1/57,

where without the global image cut it is zero.

D6-X projective-star local zero-GF5 pseudo fails a lifted physical column constraint by -5/182 at s=4. Taking the valid cut violation g=+5/182 and the SAME artificial control objective gives max min(1,lambda*5/182)=1 at lambda=182/5.

**These are precise separation demos, not a positive W(3,4) ORIGINAL sixset claim.** The control's unit cost is synthetic; neither the D6-X nor D6-Y pseudo is a globally realizable injection, and neither is claimed feasible for full standard SA/SOS. D6-X and D6-Y are previously established independent results, not original discoveries of this slice. The toy enforces the direction of the dual and provides concrete exact-price acceptance controls.

## 3. New obstruction — W32 physical-image capacity has zero slack under EVERY injection

For W(3,2), V=15 and the minimal physical alphabet a=6 gives K=binom(6,2)=15, m=0. Since every full typed assignment is a bijection onto ALL edges of K6 separately for points and lines, regardless of their correspondence to ORIGINAL source factors,

A_P(x) = A_L(x) = 6*binom(5,2) = Amax = 60

for all complete real maps x. Therefore ANY scalar Lagrangian multiplier of either D6-Y A_t-Amax physical-image cut adds EXACTLY ZERO on real states. It also adds zero on any relaxation state assembled from arbitrary distributions of complete maps when only these scalar A observables are carried through linearly.

**Restricted NO-GO:** the scalar SHARP adjacency-image cut alone cannot distinguish AA4-G's W32 source-profile/cluster relaxation from a complete globally coherent map, nor close a strict source-coherence gap. This does NOT say *all* physical column or mixed source-image capacity constraints vanish at W32; source-resolved pair or triple occupancy correlations could still enforce global coupling. In particular, it does NOT prove absence of global GF5 risk at s=4 or higher.

The finite checker explicitly appends an ABSTRACT independent-profile lower-cost candidate with g=0 to the 24 true global W32 source states, all with g=0, and verifies the exact multiplier optimum is unchanged. That abstract row is NOT claimed to be a completely feasible standard relaxation pseudodistribution; it only witnesses the scalar-cut limitation.

## 4. Actual ORIGINAL W(3,2) independent source-profile audit

For pinned true ORIGINAL W32 S68 and S72 separately:

1. Use the AA4-C actual 30 ORIGINAL point/line factors and 45 incidences, recompute exactly 53 / 119 source-four-factor hitting sets, and choose the first four-LINE original hitting set as in AA4-G. Freeze EVERY other original point/line factor label.
2. Enumerate all 4!=24 true globally separately injective complete maps of those exact FOUR ORIGINAL lines to their pinned physical K6 labels. Keep the actual same right map for ALL sixsets and all six incidence positions.
3. At EVERY state independently run full historical seven_census over 62,370 genuine ORIGINAL W32 candidate sixsets, capturing the actual class for every accepted ORIGINAL Q and exact nonnegative certified GF5 51-column numerator. No physical-P3-only witness or JPKC-012 cross-branch import.
4. Group ALL positive-in-any-state original Q by the multiset (with multiplicity) of their SIX ORIGINAL right LINE source factor IDs, derived from genuine incidence Q membership. Assert a Q's class is a function only of the exact original line factors in the four-factor block it touches; fail closed on any inconsistent sixset or class.
5. Reconstruct ALL 24 original full positive seven-S and certified GF5 51-column numerators exactly by summing group rows. Compare sum over profiles of individually optimized minima to the genuine coherent 24-state minimum. Do not independently assign physical labels to the profiles in the original model.
6. Build a **constructive sparse source-profile cover certificate**: for every active profile record a 24-bit mask of globally injected states where that ORIGINAL profile has >=1 positive accepted sixset. Greedily choose ORIGINAL line profiles whose OR covers every one of the 24 true complete maps. Independently verify each chosen profile maps to actual positive ORIGINAL Q for every state its bitmask claims, and that their union is all 24 states. The greedy cover is only an upper-bound witness, not by itself minimum-cardinality. **Independently run an exhaustive exact minimum-cover search for cardinalities 1, 2 and 3** after provably safe dominated-mask elimination; if none cover, a previously verified four-profile greedy witness certifies the exact minimum is FOUR. The exact search fails closed if the greedy witness requires more than four profiles; it does not make a fake minimum claim. The resulting sparse profile support certifies only S>=1 for this frozen-outside finite fiber, not a lower of 68 by itself.
7. Confirm exact coherent true source minimum S68=68, S72=68 in these selected four-LINE fibers (the minimum at S72 differs from its baseline 72); compare to independent profile minima and the scalar-image-cut dual. Certify both a sound greedy witness and exact minimality using complete state-mask enumeration of smaller covers. No statement about all W32 maps, W34, or all-h universality.

The profile masks and independent original source line profiles enable future import into a verified JPKC-012 named-line tensor relaxation. JPKC-012 [PR #443](https://github.com/definitely-stable/Mathlab/pull/443) independently reported original source-line-profile gaps S68 11 vs 68 and S72 0 vs 68 across pinned 24-state fibers, but this branch does NOT import unmerged code or assume exact equality until reproduced on the branch's own genuinely selected four-LINE blocks.


## 4A. Independently reproduced EXACT W32 minimal ORIGINAL profile covers (final hosted evidence)

On two **different frozen-outside all-four-original-LINE blocks** selected by AA4-G's first actual critical-source-transversal rule, the dedicated GitHub-hosted full 24-state six-position original-Q census reconstructed:

| Property | S68 | S72 |
|---|---:|---:|
| ORIGINAL global source factor IDs | (15,16,23,28) | (15,16,22,24) |
| Original W32 candidate Q classifications per each complete state | 62,370 | 62,370 |
| Distinct positive actual ORIGINAL Q over all 24 states | 544 | 555 |
| Active SIX original LINE incidence-multiset profiles | 307 | 294 |
| Sum of independent per-line-profile S minima | **0** | **0** |
| Exact coherent common-right-g S minimum | **68** | **68** |
| Sum of independent GF5 necessary numerator minima | **0** | **0** |
| Exact coherent common-right-g GF5 numerator minimum | **3,112,510** | **3,104,080** |
| Distinct undominated nonempty true 24-state profile masks | **34** | **34** |
| Greedy upper-bound source profile cover size | 4 | 4 |
| EXACT minimum source-profile cover cardinality | **4** | **4** |

**Exact finite cover theorem for these frozen W32 fibers:** no one, two or three true ORIGINAL line profiles suffice to meet every one of the 24 complete globally injected assignments. Four true-original line profiles DO suffice. The minimum is exactly four, independently for both S68 and S72. The algorithm first coalesces identical 24-state positive-profile masks and removes masks properly contained in another. This loses no minimum-cardinality covering solution: a dominated set can always be replaced by the dominating superset without increasing the number of selected profiles. The remaining 34 masks are exhaustively checked across all 1-, 2-, and 3-subsets. Since none covers the 24 states while an actual four-profile witness is checked and exists, the exact optimum is four. The hosted proof logs also print the four selected ORIGINAL source line profiles and their precise 24-bit coverage masks for independent review.

**Critical distinction:** a four-profile cover proves only that at least one positive ORIGINAL sixset exists in these 24 states. It does NOT imply S>=4 or S>=68 just from the set-cover cardinality. Exact S>=68 on these frozen outside assignments follows separately from classifying all Q on all 24 complete maps. The profile minima-zero versus global S=68 gap is REAL but remains *conditional finite*. It is NOT an all-W32 minimum, a global W34 bound, or Branch A.

The earlier JPKC-012 PR #443 found a positive independent source-profile floor for one pinned S68 block (11) and zero for another S72 block; the different selected S68 block here has independent floor ZERO. These statements are not contradictory: ORIGINAL source factor blocks and frozen outside labelings differ. Never conflate the two experimental protocols.


### Explicit four-by-six ORIGINAL source profile partition witnesses

The final dedicated GitHub-hosted exact census recorded the following complete witnesses. Each six-integer tuple is the sorted multiset of **SIX ORIGINAL right-line incidence IDs** in actual accepted source Q (repeated line factors must NOT be deduplicated). Each integer mask records which of the 24 genuine globally coherent full K6 label assignments has at least one positive ORIGINAL Q in that source line profile.

| Scheme | True original SIX right-line factor multiset | Exact 24-state mask | Number of covered maps |
|---|---|---:|---:|
| S68 | (0,0,3,5,6,7) | 16515072 | 6 |
| S68 | (0,0,3,10,11,14) | 4032 | 6 |
| S68 | (0,2,4,5,6,9) | 63 | 6 |
| S68 | (0,2,9,11,12,12) | 258048 | 6 |
| S72 | (0,0,3,5,8,14) | 16515072 | 6 |
| S72 | (0,0,6,11,13,14) | 258048 | 6 |
| S72 | (0,2,3,4,10,11) | 4032 | 6 |
| S72 | (0,2,5,6,12,13) | 63 | 6 |

For BOTH real original W32 schemes the selected four masks are exactly the disjoint collection 63, 4032, 258048 and 16515072. Each has SIX set bits, each pairwise bitwise AND is ZERO, and their bitwise OR equals 16777215 = 2^24-1. This yields a **constructive exact partition of all 24 completed source assignments into four distinct six-state witness families**; the masked sets coincide with the four possible physical images of the FIRST changed ORIGINAL right-line factor in the deterministic permutation ordering, with 3!=6 states per image.

**Separate exact MINIMALITY:** after reducing the active source-profile masks by legitimate dominance, BOTH S68/S72 have 34 inclusion-maximal candidate state masks. An independent exhaustive search over all size 1,2,3 subsets of these masks found no complete cover; the displayed size-4 partition proves that the minimum is EXACTLY FOUR. This is a stronger *finite combinatorial hitting certificate* than mere greedy upper bound. No claim is made that four positive Q always coexist in any single state: on each complete state only its matching selected profile is guaranteed active.

## 5. Acceptance and next stage

Files: research/hyp105_issue230_d6aa4h_source_capacity_dual.py; research/test_hyp105_issue230_d6aa4h_source_capacity_dual.py; dedicated GitHub-hosted workflow and this proof note. Independent rational tests compare optimum against every feasible candidate in random rational samples, demand exact price/cut signs, and reject missing valid rows, malformed source profiles, false universal scope and zero-slack W32 positive-inference.

Require exact HEAD dedicated (independent + BOTH S68/S72 real original full 24-state matrices), INDEX, Proof Audit, full Research SUCCESS, followed by INDEPENDENT mathematical peer review. Keep Draft and main unchanged.

**Next D6-AA4-I:** identify a verifiable all-h family of MIXED physical-image/source-incidence inequalities whose scalar image-only projection is insufficient; integrate actual JPKC-012 source-factor profiles and JPKC-011 physically-P3-invisible accepted Q into a tractable global moment/cutting-plane relaxation. Prove every original complete typed injection satisfies each added cut, and independently attempt a zero-cost pseudo respecting BOTH the full image and original source constraints. Without a positive global lower certificate, the root issue remains OPEN_WITH_FORMAL_BLOCKER.
