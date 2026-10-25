# HYP-105 / issue #230 — AA4-BS: original sixflag-local all-seven Walsh covariance

**Scientific Draft.** Strict child of [AA4-BR #589](https://github.com/definitely-stable/Mathlab/pull/589), frozen exact accepted-as-parent-Draft HEAD 99c75cf6b2aa367fc6d932d51aa6210fecc76b60. Also reuses [AA4-BQ #587](https://github.com/definitely-stable/Mathlab/pull/587) for all-seven disjoint source-factor swap cube degree≤6. Parallel [#588](https://github.com/definitely-stable/Mathlab/pull/588) is a mixed POINT/LINE two-map repair, not a covariance theorem. [#471](https://github.com/definitely-stable/Mathlab/pull/471) already introduced the B/A quintic POINT-side swap gradient, [#476](https://github.com/definitely-stable/Mathlab/pull/476) the TRUE ORIGINAL seven-class source taxonomy. This is a quantitatively specified original-incidence **covariance support / signed cross-class interaction** result, not the general discovery of Walsh analysis, Parseval, Poincaré, or hypergraph dependency graphs.

## Actual root objective

Issue #230 Branch A asks a bound S_s(f,g)>=c s^6 on every ORIGINAL UNCHANGED complete correlated typed physical f,g, all dyadic s. Branch B asks an authentic infinite W3 correlated o(s^6) family; C a qualifying model-equivalent reduction. Current radius-4k repairs #585/#586 change the original maps, and #587/#589 only give local support and signed first-order class flux. **A quantitative cross-class covariance on the TRUE ORIGINAL six-flag source support** is the next precisely scoped stepping-stone, but no mean/covariance by itself determines the adversarial pointwise minimum.

## BS-LOCAL: all-seven genuine original Q Walsh support (all h>=1)

Fix actual symplectic W(3,s), s=2^h, V=(s+1)(s²+1) original POINT and V original LINE factors, d=s+1 incident original flags per factor and M=Vd genuine original incidence flag IDs. Choose arbitrary already fully globally injected original POINT pair-edge images f and LINE pair-edge images g, original physical right occupied support E unchanged. Choose m PAIRWISE DISJOINT original LINE factor-ID pairs (u_i,v_i), and for each x∈{0,1}^m define ONE WHOLE globally injected original full LINE map g^x with exactly those WHOLE source-factor image transpositions toggled, no independent per-Q resampling.

For any six DIFFERENT actual original source incidence ID Q, write L(Q) for its set of at most SIX different genuine original LINE source factors and D_Q={i:{u_i,v_i}∩L(Q) ≠∅}. The historical original GF5 acceptance indicator I_Q(x) is 0 or 1 with ONE immutable possible seven-class tag c(Q) from #476/#589. It depends ONLY on bits in D_Q, because other swaps modify no true original LINE factor image used by Q (original f remains unchanged).

Use Boolean Walsh characters χ_T(x)=(-1)^{Σ_{i∈T}x_i} with uniform averaging of the ONE complete global map g^x, and let \hat I_Q(T)=2^(−m)Σ_x χ_T(x) I_Q(x). Then:

\[
\boxed{\hat I_Q(T)=0\quad\text{unless}\quad T\subseteq D_Q,\qquad |D_Q|\le 6.}\tag{BS-LOCAL}
\]

For nonempty T, |\hat I_Q(T)|≤1/2: positive and negative χ_T halves each have exactly 2^(m−1) vertices and 0≤I_Q≤1. Consequently, for each of seven c, \hat S_c(T)=Σ_{Q:c(Q)=c}\hat I_Q(T); for selected weights w_c from original issue #230, \hat W(T)=Σ_c w_c \hat S_c(T). The coefficient \hat S_c(T) ONLY receives Q touching EVERY selected swapped source LINE pair T. It is NOT limited to source Q sharing exactly the same original incidence ID (two Q can be coupled by swapping the two DIFFERENT partner LINE factor IDs).

## BS-COUNT: explicit all-h source incidence upper on high-order coefficients

For any t≥1 pairwise disjoint genuine original LINE-factor source-ID pairs, and any true original six-distinct-incidence Q sensitive to ALL t selected switches, choose ONE witness incidence flag on one of the two genuine original LINE factors in EACH pair. Since every genuine original LINE has exactly d=s+1 incident POINT factor flags, there are at most (2d)^t possible ordered selected witness incidences (all DISTINCT because line-factor source IDs from different pairs do not overlap). There are at most binom(M−t,6−t) ways to extend with 6−t other genuine distinct source flags. This overcounts many Q, so a rigorous uniform UPPER bound is

\[
N_t\le \min\{\binom M6,\ (2d)^t\binom{M-t}{6-t}\}\quad (1\le t\le6),\qquad N_t=0\ (t>6).
\]

Thus for EVERY original complete correlated map f,g and every NONEMPTY T of size t, the all-seven score and selected necessary GF5 floor numerator obey

\[
\boxed{
|\hat S_c(T)|\le N_t/2,\qquad
|\hat W(T)|\le w_{\max}N_t/2,\quad w_{\max}=51750.}\tag{BS-COUNT}
\]

This uses **genuine original GQ line-factor incidence degree** and true six-ID selection. It does NOT use or assert independence of differently chosen true original Q, and the resulting combinatorial absolute bounds can be too weak to prove S(f,g)>0. The local W3 line-pair uniqueness has NOT yet sharpened the crude overcount, and no novel W3-specific spectral inequality is claimed.

## BS-GRAM: exact all-seven classwise signed covariance and positivity (all h>=1)

For uniform independent toggle bits x∈{0,1}^m, define the TRUE ORIGINAL seven-class score S_c(x)=Σ_{Q:c(Q)=c} I_Q(x). The class covariance matrix is EXACTLY the Gram matrix of all its NONCONSTANT source-local Walsh coefficients:

\[
\boxed{
\operatorname{Cov}_x(S_c,S_d)
=\sum_{\emptyset\ne T\subseteq[m]}\hat S_c(T)\hat S_d(T).}\tag{BS-COV}
\]

This is a classical Walsh orthogonality identity specialized to all seven historical true-original GF5 classes and their simultaneous globally coherent physical pair images. Importantly, **off-diagonal cross-class covariances may be SIGNED**, not assumed nonnegative. At the original-six-Q level,

\[
\operatorname{Cov}_x(I_Q,I_{Q'})=
\sum_{\emptyset\ne T\subseteq D_Q\cap D_{Q'}}
\hat I_Q(T)\hat I_{Q'}(T).
\]

Therefore the covariance is EXACTLY ZERO if D_Q∩D_Q'=∅ (including the case where two original Q share OTHER original incidence IDs but none of the SAME image-swap pairs). This is dependence caused by **whole-source-factor image-swap pairing**, not necessarily by actual source-Q intersection. The support identity is conditional on the FIXED family of source image swaps; it does NOT claim Q indicators are independent when globally resampling arbitrary factor maps.

For the historical necessary selected GF5 R3 lower numerator W(x)=Σ_c w_c S_c(x), Parseval yields an exact NONNEGATIVE squared spectral energy:

\[
\boxed{\operatorname{Var}_x W(x)
=\sum_{\emptyset\ne T}\Big(\sum_{c=1}^7 w_c\hat S_c(T)\Big)^2
=\sum_{c,d}w_cw_d\operatorname{Cov}_x(S_c,S_d).}\tag{BS-VAR}
\]

The exact cube gradient energy obeys a **classical** Efron–Stein/Poincaré inequality

\[
\boxed{\operatorname{Var}_x W
\le \frac14\sum_{i=1}^{m}\mathbb E_x\big(W(x)-W(x\oplus e_i)\big)^2
=\sum_{\emptyset\ne T}|T|\,\hat W(T)^2.}\tag{BS-POINCARE}
\]

The difference is precisely Σ_T(|T|−1)\hat W(T)^2≥0. It measures interactions between source-factor swap coordinates beyond an additive first-order model; a strict difference is valid finite evidence of higher-order interactions, NOT positivity of W at the original center.

## Falsifiers and reproducible original geometry

Source code research/hyp105_issue230_d6aa4bs_true_original_walsh_covariance.py, tests research/test_hyp105_issue230_d6aa4bs_true_original_walsh_covariance.py, dedicated 3-job hosted workflow. True-original W32 source model generated by existing symplectic fixture (not independent fake incidence IDs). Enumerate ALL exact 62,370 original six-flag LEFT 6-coordinate candidates once on true f. For EACH candidate, enumerate 2^m complete globally injected original LINE maps generated by m genuine source-ID-disjoint WHOLE image transpositions, and historical seven-GF5 classify EVERY Q under EVERY shared global right image map. Assert c(Q) immutable, verify every Q's Walsh support is localized to D_Q and aggregate all-seven Fourier coefficients equal an independent FULL-seven-count Walsh transform. Independently recompute whole historical seven_census for every one of the global maps and compare ALL SEVEN class counts and original root weighted floor numerator. Verify exact covariance by direct centered class series, weighted variance by direct mean/square, gradient energy by independently checking all cube neighbor differences. True individual original Q disjoint D_Q support has exactly zero covariance; independently compare first-order m=1 Fourier coefficient to genuine BR signed birth/death flux. All dyadic h1..80 exact arbitrary precision original V,d,M counting bounds with NO fictional high-h W3 enumeration. Reject noninjective, malformed six-ID, source overlap and wrong finite-model scope.

## Independent numerical signed cross-class evidence on REAL ORIGINAL W(3,2)

For the historical authentic original symplectic W32/K6 S72 complete global POINT/LINE pair-image labeling and three PAIRWISE DISJOINT actual LINE source-factor whole-image swaps `(0,1), (2,3), (4,5)`, the eight complete globally injected `g^x` are independently classified on **ALL 62,370 genuine original left-projection sixflag Q**. Exact (not floating-point) covariance and weighted necessary-GF5-floor variance:

- `Cov_x(S_B-left/A-right,S_C/A) = -357/32` (genuinely NEGATIVE historical seven-class cross interaction).
- `Cov_x(S_B-left/A-right,S_A-left/B-right) = 2167/32` (genuinely POSITIVE cross interaction).
- `Var_x(W) = 3508898523703/4`, with `W=Σ_c w_c S_c` and EXACT original issue #230 necessary GF5 R3-floor weights.
- `(1/4) Σ_i E_x[(W(x)-W(x xor e_i))²] = 1011049069881`.
- Higher-order Walsh interaction energy `Σ_{|T|>=2}(|T|-1)hat W(T)² = 535297755821/4 > 0`.

These values are pinned in the corrected final-HEAD dedicated CI regressions and independently reproduced by the historical original `seven_census` on every cube vertex, not estimated from fake geometries. **Signed cross-class covariance has BOTH signs on REAL ORIGINAL W32**, invalidating any naive positive-semidefinite-entrywise covariance assumption. The complete covariance matrix IS positive semidefinite as a Gram matrix, but its off-diagonal entries need NOT be nonnegative. The strong higher-order energy also means first-order signed BR switching gradients alone do not describe the entire three-source-switch interaction.

**All-h logical scope:** NONE of these finite s=2 numerics establishes positive S on the originally unchanged map for arbitrary higher h, an infinite o(s^6) counterfamily, or a root Branch A/B/C theorem.

## Known scope, prior art and next step

Walsh Fourier orthogonality and Parseval, cube Poincaré/Efron–Stein, and classical generalized quadrangle degree are established mathematics (see Ryan O'Donnell, *Analysis of Boolean Functions*; classical symplectic generalized quadrangle constructions). The NEW scoped research artifact is their fully grounded historical *all-seven* true ORIGINAL incidence-Q covariance decomposition and explicit finite certified signed cross-class source interactions on one shared complete global pair-image cube. This is NOT proof of any root #230 Branch A/B/C and does not establish all-original-center S_s(f,g)>0, a correlated infinite counterfamily or full R3/ASET exponent. Root stays OPEN_WITH_FORMAL_BLOCKER. Needed next: sharpen N_t using ORIGINAL W3 incidence intersection motifs and derive a signed **fixed-center** inequality stronger than variances of a local cube, or find an authentic all-h correlated counterfamily. Draft pending exact-head CI, independent mathematical referee, parent chain and research integration gate.
