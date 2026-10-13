# HYP-105 / issue #230 — D6-R exact seven-class disjoint-swap Hessian

**2026-10-13. RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.**
Stacked strictly on D6-Q Draft PR #416 at all-four-GitHub-hosted-green HEAD `8fc40298c19459e344d0702560b5deafefe6b94e`. No main mutation. Root #230/#176/#169 stay OPEN. Independent mathematical review is NOT replaced by CI.

## 1. Why this follows D6-P/Q: strict W32 one-swap traps and right-orbit underdispersion

D6-P computed exactly all 105 original-line right-label transpositions for four TRUE original W(3,2) complete global pair injections. S68, with original seven-family count S=68, is a strict transposition-local minimum: every single right transposition increases S (smallest delta +7). S72 with S=72 is also strict, smallest +2. In both cases the previously certified weighted GF5 necessary selected lower numerator increases under all 105 single swaps. D6-Q then found both S68 and S72 strongly below the EXACT all-seven mean over the orbit of their fixed physical right IMAGE E: E[S]=870476/5005≈173.92. These finite facts refute any proof premise that a large orbit mean implies a nonnegative descent route from every small-S labeling by **one** swap.

The next exact question is therefore: can **interactions between two globally legal relabelings** overcome individual positive swap costs? The right mathematical object is a discrete second derivative of S over the permutation group, not another random-right first moment.

## 2. New ALL finite h deterministic mixed-Hessian theorem

Fix s=2^h, h>=1, any complete globally injective physical pair maps f,g on the ORIGINAL point and line factors of W(3,s). Use the D6-P incidence-POSITION-aware ORIGINAL right cylinders `tau`, their exact integer ORIGINAL six-incidence multiplicities `m_f(tau)`, their right ORIGINAL line supports `R(tau)`, and the certified accepted seven-family indicator `a_tau(g)∈{0,1}`. For the weighted selected positive GF5 necessary lower numerator use `y_tau(g)∈{0,5643,45600,43320,49050,51750,45010}`.

Let `sigma=(u v)` and `tau=(w z)` be **two disjoint transpositions of ORIGINAL right-factor identities**: `{u,v}∩{w,z}=∅`. These act by exchanging the associated physical right pair labels in the same globally injective original map g. They commute: g^(sigma tau)=g^(tau sigma).

For any seven-class score F=Σ_c m_f(c) a_c(g), define

    Δ_sigma F(g)=F(g^sigma)-F(g).

Its mixed permutation curvature is

    H_{sigma,tau} F(g)
      = F(g^(sigma tau))-F(g^sigma)-F(g^tau)+F(g).

Define the ORIGINAL cylinder-impact sets

    I_sigma={c:R(c) intersects {u,v}},
    I_tau={c:R(c) intersects {w,z}}.

**The all-h exact intersection-support identity is**

    H_{sigma,tau} S_seven(f,g)
      = Σ_{c∈I_sigma∩I_tau} m_f(c) [
          a_c(g^(sigma tau))-a_c(g^sigma)
          -a_c(g^tau)+a_c(g)
        ].

The proof is an elementary but crucial cancellation: if a cylinder misses sigma's ORIGINAL line IDs, its physical right labels are identical at g and g^sigma, and since the transpositions are **disjoint**, are also identical at g^tau and g^(sigma tau). Its two sigma-related contributions cancel. A cylinder missing tau's two ORIGINAL line IDs cancels symmetrically. Thus only cylinders touched by **both** nonoverlapping label swaps survive. All seven GF5 class discriminators, including original position-dependent D6 and B/B overlap/disjoint, are retained in each indicator. NO assumption about independence or random right g.

**Exact second-order composition:**

    Δ_{sigma tau} S(g)
       = Δ_sigma S(g)+Δ_tau S(g)+H_{sigma,tau}S(g).

The analogous identity holds CLASSWISE for each of seven certified GF5 sectors and for the selected GF5 numerator `Y_7(g)=Σ_c m_f(c)y_c(g)`. It is not an identity about total R3.

### Rigorous deterministic curvature budget

For any four binary values a00,a10,a01,a11∈{0,1},

    |a11-a10-a01+a00| ≤ 2.

Let `M_{sigma,tau}(f)=Σ_{c∈I_sigma∩I_tau}m_f(c)`, the NUMBER of original six-incidence subsets counted with multiplicity in the doubly touched cylinder shadow. Therefore, **for every finite h and arbitrary globally correlated f,g**,

    |H_{sigma,tau} S(g)| ≤ 2M_{sigma,tau}(f),

and for the selected GF5 necessary floor NUMERATOR with maximal class coefficient `51750`,

    |H_{sigma,tau}Y_7(g)| ≤ 103500 M_{sigma,tau}(f).

These bounds are certified (may be loose), nonprobabilistic and keep all original six-incidence multiplicities exact. For two individual swap increments d_sigma,d_tau>0, a composed two-swap descent is possible only if

    H_{sigma,tau} S(g) < -(d_sigma+d_tau).

Thus a necessary **negative mixed curvature threshold** is required to escape a strict one-swap minimum by two disjoint swaps. More generally, if d_sigma+d_tau≥2M, this particular composed move is certified non-improving without computing a full second map; this implication may be vacuous on dense W32 cylinders and is NEVER interpreted as global optimality.

**Scope guard:** The intersection-only cancellation formula above explicitly requires **disjoint** original-right transpositions. For swaps sharing a line factor, the two group actions fail to commute; the formula must be replaced by an order-sensitive 3-cycle composition. Such 3-cycles and all possible multi-swap permutations are NOT covered in this slice. Do not apply the disjoint formula to arbitrary swaps.

## 3. New original-cylinder algorithm

The algorithm composes D6-P's original-line inverted index, rather than enumerating all original sixsets for each candidate:

1. Compute the exact two singleton seven-class vectors `Δ_sigma`, `Δ_tau` on genuine complete global right injections.
2. Build the **intersection** of their two original-line cylinder impact sets, not the union used for an individual swap.
3. For each cylinder in that intersection, evaluate the exact seven-class indicator on g, g^sigma, g^tau, g^(sigma tau); combine as (+,−,−,+). Sum integer weighted ORIGINAL sixset contributions.
4. Combine singleton deltas and mixed Hessian for the exact composed seven-class vector and selected GF5 floor numerator. Verify both complete class conservation identities and absolute curvature-support bounds.
5. Validate with the **independent preexisting original six-incidence seven_census classifier** applied to the four genuine right physical pair-bijections. This classifier does not use the D6-R Hessian or D6-P right-cylinder classification.

The all-h mathematical identity is exact even where exhaustive ORIGINAL sixset enumeration would be infeasible. The executable full-original-class W32 oracle is intentionally pinned to h=1 only.

## 4. Honest limited two-swap exploration, not a global search

For the two proven true-original W32 strict one-transposition minima **S68** and **S72**, enumerate all 105 singleton original-right-line swaps and sort by unweighted ΔS (lexicographic tiebreak on original factor IDs). Freeze the **top K=12 smallest singleton ΔS swaps** before evaluating any pair. Enumerate every pair of those 12 candidate swaps whose ORIGINAL right supports are disjoint, applying their commuting composition. Evaluate every candidate exactly using the intersection-shadow Hessian. Report:

- number of tested disjoint two-swap pairs (NOT all C(105,2), not all possible distinct 2-swap permutations);
- minimum/maximum mixed Hessian and positive/negative curvature sample counts;
- count of improving/equal/worsening two-swap composites for S, and number improving the weighted necessary GF5 numerator;
- best and worst precisely identified global two-swap assignments, full original seven-class delta vector and exact GF5 floor numerator delta;
- whether any improvement among sampled disjoint two-swaps escapes an S68/S72 strict one-transposition trap, with its required negative curvature threshold.

This is a **deterministically defined exploratory subset**; *no claim* is made about the complement of those pairs, overlapping 3-cycles, global minimum over all right g, or all-h Branch A/B. If the best sampled double-swap delta is positive, label the result a limited two-swap no-escape within that explicit subset, not a proof for all 2-swaps or all maps.

The hosted dedicated workflow runs independent 6-method tests first and the top-12 exact S68/S72 two-swap report only once, avoiding the excessive repeated 4×105-swap exhaustive CI in D6-P. Printed finite exact values are facts only after hosted execution returns SUCCESS and are then pinned as regression controls. W(3,4)/W(3,8) full original seven-positive counts are not generated.


## 4a. Pinned genuine-original W(3,2) hosted measurements

The initial hosted dedicated contract for PR #417 (commit `ed37c0e03ba99f6c370f2942f8ab6eafb080d42a`, run #38393223553) passed all six independent methods. Its second step computed all targeted disjoint pairs. The exact data below are now pinned by the dedicated workflow for fail-closed future reproducibility.

| True original fixed mapping | S before | singleton swaps (all 105 strict >0) minimum | top-12 disjoint two-swap pairs scanned | negative mixed Hessians | minimum Hessian H_S | strictly improving pairs in scanned subset | best combined delta S | best combined delta GF5 selected numerator | best original swap pair |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| S68 | 68 | +7 | 49 | 19 | −14 | **0** | **+7** | +266353 | (1,13) and (10,12) |
| S72 | 72 | +2 | 45 | 19 | −15 | **0** | **+6** | +287590 | (3,7) and (0,1) |

The mixed Hessian at the best delta-S pair is −13 for S68 and −15 for S72. There were **zero** scanned two-swap compositions improving either the seven-family count or the certified GF5 necessary lower numerator. A negative Hessian is observable and correctly computed, but it was not sufficiently negative to offset BOTH individually positive singleton deltas among the **explicit top-12 disjoint candidates**. This is a **finite and subset-only non-escape result**. It does NOT prove that S68/S72 are locally optimal against all disjoint double swaps, against overlapping 3-cycles or against arbitrary right-image permutations.

## 5. Root theorem gate / next D6-S

The new curvature identity describes nonlocal interactions of admissible right permutations and provides a rigorous obstruction to escaping local minima using selected pairs. It does NOT prove a nontrivial minimum of S over all right permutations, let alone all fixed f or all h. No all-g `Ω(s^6)`, no infinite coherent o(s^6) family, no full R3 upper and no new ASET exponent.

A meaningful next all-g research direction is to derive a **global negative-curvature budget** (or exact constraint-system certificate) across ALL right permutations, or explicit coherent infinite construction. Any finite local bound from only one- and two-swap moves must not be promoted to a global optimum theorem without a rigorous complete coverage/completion argument. The data from D6-R determine whether two-exchange escapes already invalidate 1-exchange locality as a route.

## Acceptance

Stacked Draft only. Require on exact final head: dedicated D6-R Contract, INDEX, Proof Audit, and full Research workflows all SUCCESS, plus independent mathematical peer review. Keep #230/#176/#169 OPEN.
