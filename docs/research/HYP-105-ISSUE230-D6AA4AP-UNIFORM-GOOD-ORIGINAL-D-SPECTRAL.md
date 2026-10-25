# HYP-105 / issue #230 — AA4-AP: UNIVERSAL positive good true-original D-pair lower via trimmed incidence spectrum

**Research-only, strict stacked Draft child of [AA4-AO #535](https://github.com/definitely-stable/Mathlab/pull/535), frozen parent exact SHA a5960b1bb140e8e100663fcb7c198ac9553710f0.** Statements refer to actual symplectic ORIGINAL W(3,s) for s=2^h, h>=1, complete globally injected typed original point and line source-factor physical labels f,g using the minimal unordered-edge palette K_a. The new positivity theorem holds for **ALL h>=14, EVERY globally injected complete pair f,g** and counts genuine two-distinct-source-incidence-ID D pairs; it does NOT prove a positive original four-row Hall matching, GF5 acceptance, Branch A/B/C or the ASET exponent. Nothing is merged and no accepted RCP registry is modified.

## 1. Precise gap from AA4-AO and main result

AA4-AL previously proved for every actual f,g the number D(f,g) of UNORDERED genuine original flag pairs e={(p,l),(q,m)} satisfying p!=q, l!=m and both globally fixed physical factor images f(p)∩f(q)≠∅, g(l)∩g(m)≠∅ obeys D>=s^5. AA4-AO proved that each D pair whose FOUR actual physical ports avoid the exceptional physical missing-degree coordinates admits at least [n(n−1)(n−2)]²/4 **PHYSICALLY occupied two-sided P5×P5 residual templates**, for n=a-3, h>=3. The missing link was: are there uniformly many such good D pairs? Without a source-global estimate, at most 31 exceptional physical vertices per typed image did not control concentration of ORIGINAL source-incidence pairs on them.

**AA4-AP THEOREM (genuinely new specialized global composition).** Let
    V=(s+1)(s²+1), d=s+1,
    a=min{a:C(a,2)>=V}, m=C(a,2)-V.
For every genuine original symplectic W(3,2^h), h>=14, and ALL complete globally injected original point-map f and line-map g, mark a physical point coordinate c **bad** if it meets at least a/16 MISSING physical point-image edges in K_a, and similarly, INDEPENDENTLY, mark a physical line coordinate e **bad** if its line-image missing edge degree is at least a/16. Then at most 31 physical coordinates of each type are bad (AA4-AO).

Call an actual original bilateral D pair **GOOD** if its TWO distinct physical point-side PORT coordinates (the non-shared endpoints of f(p), f(q)) and its TWO distinct physical line-side PORT coordinates (non-shared endpoints of g(l),g(m)) all avoid their respective typed bad sets. The common physical center coordinates are NOT constrained. Denote their count D_good.

Then for EVERY h>=14 and EVERY complete f,g:

    **D_good(f,g) >= s^5/10**.

No source or physical map is random; this is a worst-case, all-map, all-large-h quantitative theorem. The proof below uses classical original GQ incidence singular values but a nontrivial globally trimmed original incidence-pair energy, not an unsupported one-cell spectral positivity claim.

Combining with the previously proved AA4-AO robust P5 physical theorem, EVERY GOOD original source D pair has at least [n(n−1)(n−2)]²/4 actual occupied typed point×line PHYSICAL completion template pairs, so:

    **sum_(e∈D_good) occupied physical P5(point,e) * occupied physical P5(line,e)
       >= (s^5/40) * [n(n−1)(n−2)]², ALL h>=14, ALL f,g.**

This is a globally indexed **PHYSICAL pre-Hall bound, NOT ≥accepted original GF5 motifs**. Indeed the right-hand side is enormous (of order s^14) while a single physical paired template can fail source-original Hall and final seven-GF5 alignment. These multiplicities MUST NOT be charged as independent selected original six-ID Q.

## 2. Exact true-original source incidence spectral cell bound

Let B be the ACTUAL V×V original point-line incidence matrix W(3,s). Its degree is d=s+1. Classical generalized-quadrangle collinearity gives original singular values d (multiplicity 1), sqrt(2s) (multiplicity s(s+1)^2/2), and 0 otherwise. The classical spectral fact (not claimed novel) is

    ||B-(d/V) J||_2 = sqrt(2s).

For the globally fixed complete injection f, let P_c={p:c∈f(p)}; for g let L_e={l:e∈g(l)}. Because each globally injected source factor maps to a DISTINCT unordered pair among K_a edges, no physical coordinate occurs in more than a−1 original source factors:

    |P_c|<=a−1, |L_e|<=a−1.

Original GQ expander-mixing for arbitrary actual source subsets of those cardinalities gives, for each physical point/line coordinate pair (c,e),

    M[c,e] := # {genuine ORIGINAL flags (p,l):p∈P_c,l∈L_e}
          <= d |P_c||L_e|/V
                + sqrt(2s) sqrt(|P_c|(1−|P_c|/V)|L_e|(1−|L_e|/V))
          <= d(a−1)²/V + sqrt(2s)(a−1).

To make every all-h bound exact rational integer arithmetic, set
    sigma=ceil(sqrt(2s))=isqrt(2s−1)+1,
    K=d(a−1)²/V + sigma(a−1)
so M[c,e]<=K for every physical cell and every correlated globally fixed typed pair of injections f,g. **This is an UPPER bound on a cell**, not the invalid old strategy of extracting a positive lower on an arbitrarily chosen cell from expander mixing.

## 3. Trim genuine original source flags touching exceptional physical coordinates

Let M_point and M_line be typed globally MISSING edge-image sets, each of size m. Total missing physical degree is 2m<2a, hence the number of point physical bad coordinates and of line physical bad coordinates is bounded by

    b := min(31, floor(32m/a)).

Let P_bad={p:f(p) touches a bad physical point coordinate}; let L_bad be the analogous actual ORIGINAL source line factors under g. Their sizes obey

    |P_bad|<=b(a−1), |L_bad|<=b(a−1).

The genuine ORIGINAL flags (p,l) with p∈P_bad OR l∈L_bad number at most

    d(|P_bad|+|L_bad|)<=2b(a−1)d.

Fix one such genuine ORIGINAL flag (p,l). Any legitimate D-neighbor original (q,k) with both physical intersections nonempty belongs to one of at most FOUR actual source incidence cell sets:
    (c,e) ∈ f(p)×g(l),
because both physical labels have exactly two coordinates. There are M[c,e]<=K genuine original flags in EACH of these four same-global-map cells, so one genuine original flag has at most 4K possible D-neighbors (possibly including itself and degenerate source factors — harmless for an UPPER).

Every D pair with at least ONE bad PORT physical coordinate must touch at least one original source point factor P_bad OR one original source line factor L_bad, because the bad port coordinate is one of its actual source factor's two physical label endpoints. Thus its number is bounded above by

    **D_bad_port <= 4*[2b(a−1)d]*K = 8b(a−1)d K.**

This is a strict worst-case ALL-f,g bound, not average incidence sampling. A truly good D pair may still include a source factor using a bad COMMON center; treating it as bad in the upper makes the result conservative, never invalidates the GOOD lower.

AA4-AL's exact Cauchy/source-repetition lower (UNORDERED) is

    D >= D0 := 8V²d²/a² − 2Vd² >= s^5.

Subtracting the universal bad-port upper yields the NEW exact all-h (not necessarily positive at small h) rational certificate:

    **D_good >= max(0, D0 − 8b(a−1)d [d(a−1)²/V + sigma(a−1)]).**

This is the formula in executable code. There is no assumption that physical point and physical line global labels are independent, and no factorization of the ORIGINAL GQ incidence distribution.

## 4. Fully rigorous universal h>=14 threshold

For h=14,...,23 inclusive, compute the closed-form integers a,m,b,sigma and exact rational D0 and K. The ten inequalities
    D0 − 8b(a−1)d K >= s^5/10
are individually proved by EXACT Fraction arithmetic, with no reconstructed W(3,s) of astronomical size. The table below displays approximations ONLY for human readability; the executable check uses no floats and computes each integer/rational inequality:

| h | minimal physical a | missing m | b=floor(32m/a) | exact rational bound divided by s^5 (display rounded) |
|---|---:|---:|---:|---:|
| 14 | 2,965,912 | 549,971 | 5 | 1.111530 |
| 15 | 8,388,737 | 4,169,791 | 15 | **0.125010** |
| 16 | 23,726,748 | 1,720,889 | 2 | 1.822837 |
| 17 | 67,109,121 | 33,456,255 | 15 | 1.062524 |
| 18 | 189,812,894 | 40,200,306 | 6 | 1.734517 |
| 19 | 536,871,425 | 268,042,495 | 15 | 1.531259 |
| 20 | 1,518,500,975 | 659,201,496 | 13 | 1.712575 |
| 21 | 4,294,968,321 | 2,145,911,295 | 15 | 1.765628 |
| 22 | 12,148,003,449 | 5,355,500,891 | 14 | 1.845285 |
| 23 | 34,359,740,417 | 17,173,578,751 | 15 | 1.882813 |

The least displayed h=15 margin is still **greater than 1/10**; the exact rational test, not rounding, establishes it.

For ALL h>=24 there is a UNIFORM analytic derivation that avoids infinitely many arithmetic checks. For every s>=4, minimal physical alphabet obeys
    a−1 <= 2*s^(3/2)
because C(2*s^(3/2),2) =2s^3−s^(3/2) >= (s+1)(s²+1)=V, as a monotone real binomial expression, so minimal integer a<=ceil(2s^(3/2)). Also d=s+1<=5s/4, sigma=ceil sqrt(2s)<=2sqrt(s), and V>=s^3. Therefore

    K <= 5s +4s² <=21s²/4,
    b<=31,

which leads to

    8b(a−1)d K
      <= 8*31*(2s^(3/2))*(5s/4)*(21s²/4)
       = **3255*s^(9/2)**.

Since D0>=s^5 and sqrt(s)>=4096 for h>=24,

    D_good >= s^5*(1−3255/sqrt(s))
            >= (841/4096)*s^5 > s^5/10.

This analytic argument covers EVERY h>=24. Combining it with the exact ten cases proves **D_good>=s^5/10 for EVERY h>=14**, all complete globally correlated original f,g.

Note carefully: h<14 is not claimed false. The particular robust universal spectral subtraction can be nonpositive for several smaller h; the lack of a positive certificate at those h is NOT a counterexample to existence of good pairs.

## 5. Honest GF5/source-Hall boundary and comparison to AA4-AO

The new result **solves the FIRST proposed AA4-AP gate**, establishing a global Ω(s^5) population of good original source bilateral D pairs. Combining with AA4-AO then guarantees strongly positive physical source-factor template mass on those pairs. This does NOT produce a SINGLE guaranteed genuinely original six-incidence-ID four-row Hall matching in any particular template, let alone an aligned seven-GF5-selected Q. The historical genuine W(3,2) S68 globally fixed example has ALL physical candidate templates occupied and ALL 257 D pairs physically good (since m=0), yet **193/257 are uncovered by all seven selected genuine GF5 six-Q**; 50 have no original source Hall and 143 have only original Hall six-Q in the unaligned A/A rejected class. This finite example warns against an unjustified physical-to-source-Hall lower, although it does not invalidate a sufficiently-large-h true original acceptance theorem.

AA4-AP has therefore sharpened the actual frontier: with the first GOOD-D population gate solved for h>=14, the remaining essential issue #230 obstacle is a **nontrivial SOURCE-HALL + aligned seven-GF5 positive extension-energy lower** across these globally many good D pairs or an independent all-h unanchored U motif lower. An unproven "all good D pairs extend" assumption would contradict finite small-h evidence and must not be silently used.

## 6. Independent real-source evidence, formal acceptance constraints and next task

- Versioned \`research/hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral.py\` implements exact all-h rational source spectral good-D theorem, coarse analytic tail, global physical bad-source trimming, and actual TRUE ORIGINAL complete f,g finite audit without constructing nonexistent large geometry.
- Seven/6 test groups in \`research/test_hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral.py\` test h14..23 exact rational inequality, h24..h60 analytic tail, honest unproven h<14; ACTUAL W(3,2) for five full globally bijective original f,g maps and ALL genuine original D pairs, plus genuine W(3,4) lex/random complete global source f/g injected into K14 with six missing physical edges on each typed side; genuine original source symplectic transvection and two independent typed physical coordinate permutations; negative fake-source guards and the historical 193/257 S68 full seven-positive finite nonextension witness.
- Independent original source finite spectral oracle already lives in AA4-AL; the new W34 test crosschecks each actual cell M[c,e] with its separate spectral cell cap K, and every genuinely original D pair's actual physical port status against the bad-original-source overcount.
- Dedicated four GitHub-hosted jobs, INDEX, Proof Audit, Full Research and independent mathematical referee are necessary on the exact child PR HEAD; no use of self-hosted CI, no merge to main or generated accepted theorem registry changes. Strict Draft atop AA4-AO #535. Original #230 remains OPEN.

**Next AA4-AQ:** Prove a genuine all-f,g source-perfect-matching and aligned seven-GF5 lower among the now guaranteed Ω(s^5) good original D pairs, with enough true extension multiplicity to reach E=Ω(s^6), OR rigorously derive an all-f,g lower on accepted zero-D-anchor U. Initial experiments must distinguish original source-Hall-zero vs real but unaligned A/A rejection in the per-pair AA4-AN funnel. Do not substitute physical occupancy, source forest independence, or four-index abstract graph counts for the six distinct ORIGINAL incidence IDs of W(3,s).

**Prior art:** Classical generalized quadrangle spectra and expander mixing are established known tools (see Newman 2004, *Independent Sets and Eigenspaces*, cited in AA4-AL); ordinary Cauchy and union bounds are classical. The specialized genuine all-global original source bad-coordinate trimming and quantitative h>=14 GOOD-D consequence are the present research statement, not a claim that the underlying spectral theorem is new.
