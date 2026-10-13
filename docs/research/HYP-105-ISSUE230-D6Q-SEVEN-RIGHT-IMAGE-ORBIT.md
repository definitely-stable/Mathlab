# HYP-105 issue #230 — D6-Q fixed-right-IMAGE orbit transfer for all seven GF(5) families

**2026-10-13. Status: RESTRICTED_THEOREM_C / Branch A,B OPEN.**
Strict stack: D6-P [Draft PR #415](https://github.com/definitely-stable/Mathlab/pull/415) four exact-head GitHub-hosted checks SUCCESS at `d3ef69ee5213a8ecd3880203d2f24fce565caad8`. D6-Q is a new Draft child. Do not modify `main` or close #230/#176/#169.

## The pivotal gap after D6-P: the fixed IMAGE of right g

D6-M proved right-random expected positive subclasses using **uniform right injections into the entire physical K_a alphabet**, and D6-O gave a joint B-left/A-right plus C-left/A-right second moment for this distribution. But the real all-label question fixes a particular complete injective right map g. At h>1, `V=(s+1)(s²+1)` ORIGINAL lines can be strictly fewer than `K=binom(a,2)` physical pair edges for the minimal a. The actual map has image `E_g⊆E(K_a)` of size V; **permuting the V original factor labels among this fixed image E_g is NOT uniform right completion into all K physical pairs**. It changes neither E_g nor the missing-edge pattern. Conflating the two measures loses an actual global-correlated constraint.

D6-Q supplies a precise group-orbit theorem for every fixed **physical right IMAGE**, without assuming E_g=K_a. This does NOT assert anything about the worst right labeling in that image orbit.

## Theorem Q1: exactly four physical image-shape probabilities, ALL finite h

Fix the true ORIGINAL W(3,s) incidence graph, any complete injective ORIGINAL left point-label map f, and any right IMAGE `E ⊆ E(K_a)` of cardinality V=number of ORIGINAL right lines. Draw a uniformly random **bijection** from the V original right line vertices to the V physical pair edges in E. This is the orbit of a fixed right injection g under all permutations of its ORIGINAL line identities. It preserves the entire missing physical pair-edge set.

A selected original six-incidence subset has its RIGHT ORIGINAL line endpoint repetition profile `A=(1,1,1,1,1,1)`, `B=(2,1,1,1,1)`, or `C=(2,2,2)` whenever its right physical pair projection can be a six-coordinate 2-regular graph. The right ORIGINAL incidence profiles cannot be inferred from physical right geometry alone.

Let `F_A(E)` be the number of *unordered* sets of SIX DISTINCT physical pair edges in E forming six-vertex 2-regular graphs (simple C6 or two vertex-disjoint triangles). Let `F_B(E)` count one physical pair edge plus a disjoint physical 4-cycle on the four remaining coordinates, with exactly FIVE distinct pair labels. Let `F_C(E)` count physical perfect matchings of size 3 on six distinct coordinate symbols. Let `F_D(E)` count unoriented simple 6-cycles in E.

Then the exact orbit probabilities of the necessary right physical projection are

    p_A(E) = 6! F_A(E)/(V)_6,
    p_B(E) = 4! F_B(E)/(V)_5,
    p_C(E) = 3! F_C(E)/(V)_3.

For left A, original right A, with the LEFT dual column pairing a connected C6, the stricter aligned D6 probability is

    p_D6(E) = 12 F_D(E)/(V)_6.

When the left dual is two triangles rather than a single connected C6, D6 probability is zero regardless of right labels. That case is not silently counted by p_A.

**Proof:** All injective images of r distinct ORIGINAL right line identities in E form the same `(V)_r` equiprobable tuples, with r=6,5,3 respectively. Each six-edge 2-factor supports 6! assignments to six distinct ORIGINAL right lines; each B 5-edge physical pattern supports 4! assignments to the four singleton ORIGINAL lines (the fifth physical edge is forced for the original doubled right line); and each C 3-edge matching supports 3! assignments to three ORIGINAL doubled right lines. For D6, the column-dual simple C6 among six immutable ORIGINAL incidence positions must agree with the fixed left dual pairing. Each physical C6 has exactly 12 cyclic/reversal bijections that induce that left dual, the dihedral automorphism group of C6. That factor is NOT 6! and must not be confused with arbitrary right A acceptance.

For any fixed ORIGINAL f and right IMAGE E, apply these four probabilities to the original six-incidence cylinder counts from D6-P. Classification is exact for each of the seven accepted GF5-positive classes:

| ORIGINAL left/right multiplicity | Positive class | Exact physical orbit probability |
| --- | --- | --- |
| B/A | B-left/A-right | p_A(E) |
| A/B | A-left/B-right | p_B(E) |
| C/A, A/C | aggregate C/A | p_A(E) or p_C(E), direction kept |
| C/B, B/C | aggregate C/B | p_B(E) or p_C(E), direction kept |
| B/B, repeated point/right line share incidence position | B/B-overlap | p_B(E) |
| B/B, repeated point/right line disjoint in positions | B/B-disjoint | p_B(E) |
| A/A, left dual C6 and matching right dual | D6 | p_D6(E) |
| A/A left disconnected triangles or C/C | no certified class | 0 |

Writing `n_f(tag,r)` for the integer number of TRUE ORIGINAL six-incidence subsets of the indicated left/right signature, the exact class-by-class expected counts are

    E_{g' : im(g')=E} U_tag(f,g')
      = sum_{r ∈ {A,B,C,D6}} n_f(tag,r)*p_r(E).

Consequently both the expected all-seven S and expected necessary GF5 selected lower numerator are EXACT:

    E_{g'} S_seven(f,g') = sum_tag E_{g'} U_tag,
    E_{g'} Y_7(f,g') = sum_tag GF5_FLOOR(tag) * E_{g'} U_tag,

with existing certified class weights 5643,45600,45600,43320,49050,51750,45010. The count is over DISTINCT ORIGINAL incidence sixsets, never over coordinate permutations or ten GF5 signs. The expected selected floor numerator divided by `51^6` is only an expected **necessary positive R3 lower contribution**, NOT an upper bound on full R3.

The executable full original-sixset enumeration is restricted to genuine W(3,2) where complete exact inputs are available. The all-h theorem itself needs neither an executable W34 nor a fabricated W38 seven-S census.

## Theorem Q2: robust finite-deletion bound for ANY right image E

For the COMPLETE physical graph K_a, the exact unoriented physical shape counts are

    F_A(K_a)  = 70 binom(a,6)
    F_B(K_a)  = 45 binom(a,6)
    F_C(K_a)  = 15 binom(a,6)
    F_D(K_a)  = 60 binom(a,6).

Derivation on each fixed six-coordinate set: 70 simple 2-factors = 60 connected C6 + 10 unordered pairs of triangles; 45 repeated-edge-plus-disjoint-C4 templates = 15 repeated pair choices *3 C4 choices; 15 matchings of 3 disjoint pair edges; 60 unoriented connected C6.

Let K=binom(a,2), m=K−V be the number of unavailable physical pair-edge labels. Each copy of a shape uses e_T DIFFERENT physical pair edges (e_A=6, e_B=5, e_C=3, e_D=6). By edge-transitivity of complete K_a, each physical edge occurs in exactly `e_T F_T(K_a)/K` copies of that shape, an integer. Removing m distinct edges destroys no more than m times that amount. Thus for EVERY E of size V:

    F_T(E) >= max(0, F_T(K_a) - m*e_T*F_T(K_a)/K).

This is the rigorous counting union bound, not independence of edge deletions. The deletion loss for overlapping copies of a shape is overestimated, never underestimated. For a single missing physical edge, equality holds for every one of the four template families.

For the minimal physical alphabet a required to encode ORIGINAL W(3,2^h), **all four guaranteed surviving counts are positive at every h>=1**: at h=1, (V,K,a,m)=(15,15,6,0). For all h>=2, s>=4, a>=14, and minimality yields `0<=m<=a−2`, so

    6m/K <= 12(a−2)/(a(a−1)) < 1   (a>=14).

The last expression is decreasing for a>=14, starting from 144/182<1. Therefore for all h and every admissible fixed right IMAGE, the physical A, B, C and D6 shape families are nonempty. This does not guarantee a specific original sixset support matches any of them under the given fixed right g.

## Theorem Q3: all-h fixed-IMAGE ORBIT expectation lower survives a missing-edge adversary

Write `p_A^{full}=6! F_A(K_a)/(K)_6` for the right-A probability under **uniform injections into the full K_a physical alphabet**, and `p_A^{E}=6! F_A(E)/(V)_6` for the fixed right IMAGE orbit. From Q2,

    p_A^{E} >= (1−6m/K) * (K)_6/(V)_6 * p_A^{full}
             >= (1−6m/K)*p_A^{full}.

Let `L_BC(s)` denote the PREVIOUSLY proved D6-M universal (all fixed original left f) lower for the **full-completion conditional mean** of the disjoint directed subclasses B-left/A-right and C-left/A-right, whose leading coefficient is `(455/3+o(1))s^6`. Both subclasses use exactly the same right A indicator, six DISTINCT ORIGINAL right lines, and neither duplicates any ORIGINAL sixset.

Therefore, for **every** s=2^h, every complete ORIGINAL left map f, and every fixed admissible right pair-edge IMAGE E,

    E_{g':im(g')=E} S_seven(f,g')
        >= (1−6m/K) * L_BC(s) > 0.

Since a≈sqrt(2V)=Theta(s^(3/2)) and m<a−1, `6m/K=O(s^(−3/2))`. Hence **uniformly over all fixed left maps f AND fixed right physical image sets E**,

    E_{g':im(g')=E} S_seven(f,g') >= (455/3−o(1)) s^6.

This is genuinely stronger in quantifier scope than the D6-M right-uniform-full-injection mean: the right IMAGE, and therefore the exact missing-edge pattern, can now be adversarial/fixed. But the **right assignment within that fixed image is still averaged**. Existence of at least one large-S relabeling in the orbit says NOTHING about the minimum-S relabeling and does not establish Branch A.

A further group-invariance fact: the exact expected seven-class vector is identical for any two concrete right maps g1,g2 that have the same fixed left map f and the same right IMAGE E, even if their actual S and GF5 floors are very different. For true W32, all bijections use the complete K6 image, so lex/reverse (same left) and S68/S72 (same left) necessarily have identical right-orbit mean vectors despite their different observed S.

## Implementation and independent finite original evidence

- `research/hyp105_issue230_d6q_seven_right_image_orbit.py`: exact four physical motif families, sparse per six-coordinate physical IMAGE enumeration (bounded by `max_six_coordinate_sets`), all-h deletion bounds, exact per-class original-incidence conditional expectation, and rigorous all-h fixed-image orbit mean certificate.
- `research/test_hyp105_issue230_d6q_seven_right_image_orbit.py`: independent direct physical 6-edge A/C6, 5-edge B, and 3-edge C shape enumerations on K6/K7, including single-edge deletions (exact deletion bound equality). Fully enumerate small synthetic 6!/5!/3! right-label permutations, including the D6 12-preserving assignments. Check real original W32 seven-class fixed counts, conditioned means, GF5 numerator and classwise deficit conservation; compare to independent legacy original GF5 classifier. Verify exact shape probabilities for real W(3,4) **right physical IMAGE only** without enumerating/fabricating full W34 seven-positive original S.
- `.github/workflows/hyp105-issue230-d6q-seven-right-image-orbit.yml`: dedicated hosted independent tests and exact report, with the same exact-head INDEX, Proof Audit, and Full Research requirements. Keep all PRs Draft and original issues OPEN.

**Root mathematical blocker:** none of Q1/Q2/Q3 forbids a specific adversarial assignment g to be a deep lower-tail outlier relative to its right-image orbit mean. D6-P produced two strict finite one-swap local minima, so simple adjacent-swap descent does not bridge that gap. The next genuine all-g step must establish a deterministic all-seven anti-avoidance inequality across every complete (f,g) or construct an explicit infinite coherent sub-s^6 family. Do not claim new ASET exponents, full GF5 R3 upper, Branch A or Branch B.
