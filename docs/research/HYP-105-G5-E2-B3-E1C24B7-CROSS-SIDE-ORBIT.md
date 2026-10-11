# HYP-105 B3.2-E1-C24-B7 — typed LEFT/RIGHT mixed global transpositions

Research parent: [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked scientific child of [C24-B6 PR #353](https://github.com/definitely-stable/Mathlab/pull/353) (then [B5 #352](https://github.com/definitely-stable/Mathlab/pull/352), [B4 #348](https://github.com/definitely-stable/Mathlab/pull/348), [B3 #347](https://github.com/definitely-stable/Mathlab/pull/347)). 2026-10-11. No `main` changes or merge.

## 0. Rigorous audit of existing results and the missing variable

B3/B4 establish exact ORIGINAL-GQ global-right transposition counting; B4 found finite S72 strict 1-right-swap minimum; B5 found a disjoint right double-swap escape S72 -> 82 -> 68; B6 independently established true ORIGINAL W(3,2) S68 strict right radius-two minimum (all 105 one-swaps S>=75; all 5005 exact two-swaps S>=69). Their contract, Research six-shard + aggregate, and INDEX have all succeeded on the actual predecessor PR heads.

**But the ROOT proof target in #230 quantifies over EVERY LEFT f and RIGHT g. All these finite S68 stationarity statements fix ONE left f. They neither imply minimization over global left maps nor an all-h obstruction.**

**Crucial correctness trap:** the set of ORIGINAL DISTINCT six-incidence J whose physical LEFT factor passes the six-coordinate 2-factor test depends on the complete global f. `compile_left(f)` enumerates 62,370 original W32 candidates for each f using physical K6 left 2-factor templates, but these are **not the same 62,370 original sixsets** after f changes. Taking a B6 compressed-left static source and applying a new left f is unsound: it silently loses newly LEFT-eligible original J and may retain ineligible ones. The accepted seven tags also depend on original left point and right line six-incidence structure. B7 recompiles and revalidates the original source for EVERY changed global LEFT f, then applies every global right g to that new source. No per-J independent label assignment.

## 1. Exact all-h mixed-side identity and intrinsic weak upper bound

For any original finite GQ W(3,s), s=2^h>=2, write V=(s+1)(s²+1) original points and lines; original incidence universe `I` has E=V(s+1) **distinct ORIGINAL incidences**. Fix any globally complete physical-pair injections f on ORIGINAL points and g on ORIGINAL lines. Let `J⊂I` be any *distinct* six-incidence subset, and define `X_J(f,g)∈{0,1}` as acceptance into one of the seven disjoint necessary positive GF5 families, with all six-coordinate physical-left/physical-right constraints and original incidence pattern preserved.

Let A be a transposition of two ORIGINAL **point** labels (changes the complete global f); let B be a transposition of two ORIGINAL **line** labels (changes the complete global g). These are typed actions and commute as map operations on different sides. Define

    κ^LR_{A,B}(f,g) =
      S(f^A,g^B)-S(f^A,g)-S(f,g^B)+S(f,g).

Every source J contributes

    κ^LR_J = X_J(f^A,g^B)-X_J(f^A,g)
             -X_J(f,g^B)+X_J(f,g).

If J contains no original incidence on either swapped POINT, its physical left image is unchanged under f^A, whence κ^LR_J=0. Similarly if J has no original incidence on either swapped LINE, κ^LR_J=0. Conversely, for any jointly touched source J, its four acceptance indicators are Boolean, so `|κ^LR_J|<=2`. Therefore, deterministically for ALL s,f,g:

    |κ^LR_{A,B}(f,g)| <= 2 M^LR_{A,B},

where M^LR_{A,B} is the number of ORIGINAL distinct six-incidence J touching the two-point support and the two-line support, **in the common fixed original incidence universe**, NOT just one f-dependent precompiled candidate source.

For A={p1,p2} and B={l1,l2}, the number of original incidences touching A is d=2(s+1), touching B is also d, and their intersection size c∈{0,1,2,3} (a full 2-by-2 incidence K2,2 is impossible in a generalized quadrangle: girth >=8 of the bipartite incidence graph). Inclusion–exclusion yields the **exact** original source joint-touch universe size

    M^LR_{A,B} = C(E,6)-2 C(E-d,6)+C(E-2d+c,6),
    E=(s+1)^2(s²+1), d=2(s+1).

For W32, E=45 and d=6. For larger s this bound is typically **far too large** relative to the desired S~s^6. It is purely an exact *possible-impact support bound*; it has NO sign or guaranteed-descent content, does NOT prove an all-h positive `Omega(s^6)`, and must not be confused with B6's **RIGHT/RIGHT** joint source counts restricted to one frozen f. Asymptotically its leading scale is much larger than s^6, even when most of those original sixsets fail physical 2-factor tests. The correct next theoretical target is *signed cancellation and jointly LEFT/RIGHT physical eligible incidence-tensor structure*, not this loose binomial envelope alone.

An entirely independently enumerated small-universe k-subset test verifies the generic inclusion–exclusion for E=6,7,8 and several k, plus true W32 typed overlap classification for every 105x105 pair.

## 2. Complete genuine W32 finite typed transposition rectangle

Freeze baseline true-original-W32 f0 = C24-B1 H45 (complete ORIGINAL global LEFT permutation), and g0 = C24-B5 S68 complete ORIGINAL global RIGHT permutation. Its seven-vector in frozen order is (0,44,21,0,0,2,1), necessary GF5 Q7 numerator =3,112,510, original right-C=0.

Enumerate all **11236** distinct complete typed map pairs in the inclusive `{identity or ONE LEFT transpose} x {identity or ONE RIGHT transpose}` rectangle:

- baseline (f0,g0): 1
- LEFT-only (f0^A,g0): exactly 105;
- RIGHT-only (f0,g0^B): exactly 105;
- mixed (f0^A,g0^B): exactly 105*105 = **11025**.

For **each** of 105 left transpositions A, compile its OWN distinct original left physical-source census: 62,370 ORIGINAL six-incidence sets enumerated under the new globally complete f0^A. Compile exactly its right-multiset source fibers; for each right transposition B score the result via all 130 physically eligible K6 right 2-factor templates (same globally complete g0^B on every original sixset). Record exact S, full seven-vector, original-right-C and frozen GF5 **NECESSARY** Q7 numerator. This is a genuine finite original GQ enumeration; it is not a sum of independent source choices.

For each mixed pair, compute exact signed typed curvature

    κ^LR_{A,B}=S(f0^A,g0^B)-S(f0^A,g0)-S(f0,g0^B)+68.

Count strictly improving mixed cells, negative curvatures, best mixed score, best left-only score, best necessary-GF5 Q7 comparator, and source-eligible multiplicity distribution. Also verify the true original cross incidence overlap c and the exact all-h source-universe support cap for all 11025 cells, with independently brute-force-tested formula.

Crucially check **both** the selected best left-only and best mixed endpoints against (i) a fresh independent whole original LEFT-first static source scorer under the new f and (ii) an **independently implemented RIGHT-FIRST 62,370 DISTINCT original six-incidence source census**. No global `(15!)^2` optimum, no unrestricted all-f min, no all-h positivity is inferred from the 11236 cells.

Numerical minima intentionally not guessed before first dedicated GitHub-hosted Contract. Once observed, pin result to an exact-head fail-closed finite regression. Distinguish evidence from any all-h theorem.

## 3. Acceptance and next mathematical decision

Dedicated GitHub-hosted B7 Contract runs light tests then EXACT 105-left-source recompile times 105-right-global-swap audit, separately from full six-shard hosted Research (existing 139 commands + exactly two new B7 commands, independently frozen FNV1a64), and mandatory INDEX. The large `105*105` report must not be repeated in broad Unit tests. All three workflows must show SUCCESS at the exact latest HEAD. Do not merge automatically.

If a LEFT-only or mixed step beats S68, this disproves only the *finite broader typed-radius-one stationarity* of that particular map. If it does not, that map is strict or nonstrict local minimum for this specific typed move set, not global f,g or asymptotic proof. A meaningful Branch C reduction would require an **explicit signed incidence-tensor inequality** uniform in h and over *all* f,g, or a rigorous counterfamily with correlated global assignments. The binomial support bound alone is deliberately not presented as such a reduction.

Scientific status before hosted run: ALL-h_EXACT_TYPED_CROSS_SUPPORT_AND_UNIVERSE_COUNT / FINITE_TRUE_W32_11236_TYPED_MAP_RECTANGLE_IMPLEMENTED_CI_PENDING / NO_PROVED_BRANCH_A_OR_B / ROOT_230_OPEN.
