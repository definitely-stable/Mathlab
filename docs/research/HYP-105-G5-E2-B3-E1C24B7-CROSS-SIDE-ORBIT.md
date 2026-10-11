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

## 3. Exact support-envelope asymptotics — why it cannot close Branch A

Let `M_c=C(E,6)-2C(E-d,6)+C(E-2d+c,6)` as above, with `E~s^4`, `d~2s` and fixed c in {0,1,2,3}. For ZERO shared incidences (c=0), double inclusion-exclusion counts primarily one incidence from each swapped support and four arbitrary other incidences. Expanding the binomial discrete second difference gives

    M_0 = (1+o(1)) d^2 E^4/24 = (1/6+o(1)) s^18.

With c>=1, the fact that ONE source incidence can touch BOTH swap supports creates a much larger correction by the exact hockey-stick identity:

    M_c-M_0 = sum_{t=0}^{c-1} C(E-2d+t,5),

and therefore for any fixed nonzero c,

    M_c = (c/120+o(1)) s^20.

Thus the valid bound `|kappa_LR|<=2M_c` only caps a quantity at order s^18 (c=0) or s^20 (c>=1), many powers above the desired S~s^6 scale. **No positive universal lower bound, signed descent theorem, or asymptotically sharp comparison is proved by this envelope.** This documented failure is deliberate: an all-h solution must exploit coherent PHYSICAL 2-factor eligibility, original seven-family correlations, and/or a signed incidence-tensor cancellation inequality.

## 4. Exact hosted ORIGINAL W32 11,236-map finite outcome

Dedicated [GitHub-hosted C24-B7 Contract run #38134355587](https://github.com/definitely-stable/Mathlab/actions/runs/38134355587) completed SUCCESS on its then exact PR head `5ace8a57a39c0c0ce295133c820b1c9bace097dc`, including independent fast source tests and exhaustive B7 11,236 typed global map pairs. Every left map was independently recompiled from **62,370 distinct ORIGINAL W32 six-incidence candidates** under that LEFT mapping, and decisive endpoints were checked against separate LEFT-source scoring and full **RIGHT-FIRST original 62,370-source** enumeration.

- Baseline: S68 at frozen complete f0,g68, frozen seven-vector (0,44,21,0,0,2,1), necessary GF5 Q7=3,112,510.
- All **105 LEFT-only** global swaps have S>=**70**, best left (3,7), zero improving.
- All **105 RIGHT-only** global swaps have S>=**75**, best right (8,9), zero improving.
- All **11,025 simultaneous LEFT+RIGHT** swaps have S>=**70**, with exactly **TWO** tied maps attaining S70, zero improving.
- Lexical best typed mixed swaps: LEFT **(3,8)** and RIGHT **(0,14)**. LEFT-alone would be S95, RIGHT-alone S97, simultaneously they produce **S70** with signed mixed curvature **-54**: `95+97-68-54=70`. The complete new left map is `(13,4,2,10,0,11,1,7,14,6,9,5,12,3,8)`; complete new right map is `(8,9,11,4,1,6,0,13,5,14,3,7,2,10,12)`. Original accepted seven vector is **(0,46,18,0,0,2,4)**, necessary Q7 **3,201,940**, original right-C=0.
- There are **8,286 negative** signed typed mixed curvatures among 11,025 cells; strongest negative is **-70** for LEFT (4,14), RIGHT (4,11). Even these signs alone imply no descent.
- Independent true-original W32 cross incidence c histogram across exactly 11,025 typed pairs: c=0:4,185; c=1:5,040; c=2:1,620; c=3:180. Total unrestricted original sixset joint-touch envelope across these cells: **32,252,059,350**, emphatically much larger than any observed signed `kappa`.
- The number of source sixsets statically eligible under each global LEFT swap **varied**, from **52,856** to **54,217** (initial f0 had 53,907), providing a direct quantitative falsifier of the unsafe idea that a compiled left candidate census may be reused when swapping f.

**Exact finite separation:** The true ORIGINAL W32 map (f0,g68) is strict local minimum in the *typed* rectangle where LEFT moves <=1 transposition and RIGHT moves <=1 transposition (including their simultaneous action). Combined with C24-B6 it is separately strict under 1–2 RIGHT swaps. This does NOT imply any other mixed move (e.g. two LEFT plus one RIGHT), global minimum over (15!)² assignments, or universal S>=Omega(s^6).

Following new fail-closed regression and both-tied-minima independent cross-check, the updated latest PR HEAD needs **new exact-head hosted Contract/Research/INDEX success**; the older-head success cannot be reused.

## 5. Acceptance and next mathematical decision

Dedicated GitHub-hosted B7 Contract runs light tests then EXACT 105-left-source recompile times 105-right-global-swap audit, separately from full six-shard hosted Research (existing 139 commands + exactly two new B7 commands, independently frozen FNV1a64), and mandatory INDEX. The large `105*105` report must not be repeated in broad Unit tests. All three workflows must show SUCCESS at the exact latest HEAD. Do not merge automatically.

If a LEFT-only or mixed step beats S68, this disproves only the *finite broader typed-radius-one stationarity* of that particular map. If it does not, that map is strict or nonstrict local minimum for this specific typed move set, not global f,g or asymptotic proof. A meaningful Branch C reduction would require an **explicit signed incidence-tensor inequality** uniform in h and over *all* f,g, or a rigorous counterfamily with correlated global assignments. The binomial support bound alone is deliberately not presented as such a reduction.

Scientific status before hosted run: ALL-h_EXACT_TYPED_CROSS_SUPPORT_AND_UNIVERSE_COUNT / FINITE_TRUE_W32_11236_TYPED_MAP_RECTANGLE_IMPLEMENTED_CI_PENDING / NO_PROVED_BRANCH_A_OR_B / ROOT_230_OPEN.
