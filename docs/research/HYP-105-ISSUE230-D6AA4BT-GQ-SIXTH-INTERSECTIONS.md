# HYP-105 / #230 — AA4-BT: true-original generalized-quadrangle intersection sieve for SIXTH Walsh order

Scientific **Draft** strict child of [AA4-BS #590](https://github.com/definitely-stable/Mathlab/pull/590) at frozen exact parent HEAD bbd9659c6c1be769910e10ad86a05a405109248e. This work depends on BS-LOCAL, the already-established true-original source-ID sixflag disjoint whole-factor source LINE image transposition cube, and on existing historical ORIGINAL seven-GF5 source taxonomy [#476](https://github.com/definitely-stable/Mathlab/pull/476). Parallel stacks #586, #588 correct one or both globally injected maps for k roots, not original SAME-MAP high-order source-GQ spectral coefficients. No changes to main or accepted RCP registry. Issue #230 remains OPEN_WITH_FORMAL_BLOCKER.

## Geometric prior art

The needed original GQ property is CLASSICAL: every line has exactly d=s+1 incident points, and any two distinct lines meet in at most one actual point. For the real symplectic W(3,s), V=(s+1)(s²+1) source LINE factors and M=V(s+1) actual original incidence IDs. See classical Payne–Thas/Bamberg *Finite Generalized Quadrangles* (https://cage.ugent.be/~bamberg/FGQ.pdf) and [Encyclopedia of Mathematics, Quadrangle](https://encyclopediaofmath.org/wiki/Quadrangle). We do NOT claim to discover finite-GQ line uniqueness, inclusion/exclusion, the 15 six-element perfect matchings or Walsh upper bounds.

## BT-PACKET exact all-h counting for all t

Fix any TRUE ORIGINAL symplectic W(3,2^h), h>=1, arbitrary globally injected and correlated complete f,g physical edge maps, and t pairwise disjoint original LINE-factor pairs P_i={u_i,v_i}, 2t<=V. Define B_i as ALL actual 2d distinct original incidence IDs whose LINE source factor lies in P_i. Different packets B_i are disjoint because an original incidence has ONE original LINE factor, even when packet LINES share an original POINT.

The number H_t of arbitrary SIX DISTINCT ACTUAL ORIGINAL incidence ID subsets Q meeting EACH B_i is EXACTLY

\[
\boxed{H_t=\sum_{j=0}^{t}(-1)^j\binom tj\binom{M-2dj}{6},\qquad 0\le t\le6,}
\]

with binomial convention binom(n,6)=0 for n<6, and H_t=0 for t>=7. This is ordinary inclusion/exclusion on the actual original LINE source-factor packet incidence subsets, and counts Q without prematurely assuming historical GF5 positivity or independent maps. In particular

\[
\boxed{H_6=(2d)^6.}
\]

This is an exact refinement of AA4-BS's coarse N_t≤(2d)^t binom(M−t,6−t). It is still a LINE-incidence-side subset count, so further actual original POINT-incidence multiplicity structure is necessary for a classwise bound.

## BT-FILTER and true-original LINE-multiplicity elimination at order six

Consider SIX disjoint whole-original-LINE-factor image swaps, and true-original historical Q contributing to the Walsh coefficient \hat S_c(T) for T consisting of ALL SIX bits. AA4-BS source-locality forces Q to meet all six original packets. Since Q has exactly six original incidence IDs, Q contains EXACTLY ONE genuine original flag from each packet. Because all six source LINE-pair packets consist of mutually disjoint genuine ORIGINAL LINE factor IDs, the six ORIGINAL LINE IDs of Q are pairwise DIFFERENT. Its right ORIGINAL source factor multiplicity must therefore be A=(1,1,1,1,1,1).

Hence at order six ONLY the accepted historical source profiles with RIGHT A are possible:

- D6 (A-left/A-right accepted physical connected aligned D6);
- B-left/A-right (one repeated true original POINT factor);
- C/A (three repeated true original POINT factors).

The OTHER FOUR accepted historical seven GF5 class sixth-order coefficients are **IDENTICALLY ZERO** for every actual original complete f,g and all dyadic h>=1:

\[
\boxed{\widehat S_{A/B}(T)=\widehat S_{C/B}(T)
=\widehat S_{B/B,o}(T)=\widehat S_{B/B,d}(T)=0,\quad |T|=6.}
\]

This is true under arbitrarily correlated original typed global physical maps and does not assert that any of the remaining three coefficients have a definite sign.

## BT-POINT-INTERSECTION: uniform in s sixth-order C/A and B/A bounds from genuine original LINE uniqueness

Fix the six different original LINE factor source packets P_1..P_6. For each distinct packet index i,j, define K_{ij} as the set of pairs of actual original source incidence IDs, one from packet i and one from packet j, that have the SAME ACTUAL original POINT factor. Since P_i and P_j each contain two different genuine original LINE factors and any two distinct original GQ lines meet at most one point,

\[
\boxed{|K_{ij}|\le 2\cdot2=4\quad\text{for every }i\ne j.}
\]

If a six-packet-hitting original Q has original POINT profile B=(2,1,1,1,1), its unique repeated original POINT must come from SOME pair (i,j) of the six packets. Choose these two actual incidences in at most 4 ways and choose one of 2d genuine flags from each of the four remaining source packets: at most

\[
\boxed{N_{6,B}\le\min\{(2d)^6,\ \binom62\cdot4\cdot(2d)^4\}=
\min\{(2d)^6,\ 60(2d)^4\}.}
\]

For the much more constrained ORIGINAL POINT C source profile (2,2,2), Q has a UNIQUE partition of its six packet indices into three unordered disjoint pairs with each pair sharing one actual original POINT. There are exactly (6−1)!!=15 perfect packet matchings. Each matched pair admits at most four actual original same-POINT incidence choices, giving

\[
\boxed{N_{6,C}\le15\cdot4^3=960,\quad\text{uniformly for ALL }s=2^h,\ h\ge1.}
\]

There can be further constraints: all three repeated original POINT factors must be different. To have the unchanged f physically accepted left C, their physical pair-edge images must have SIX distinct endpoints, i.e. be pairwise disjoint physical graph edges. Thus the precise TRUE ORIGINAL C-left *physically feasible* source Q set is computed by the exact finite 15-matching incidence-intersection formula, discarding repeated point choices and physically intersecting f-point pair edges. Its cardinal H_C(f;P_1,...,P_6) is computable from actual line-line point intersections and fixed GLOBAL original f alone, independent of any proposed alternate LINE map g^x, and always ≤960.

For any Boolean acceptance indicator of a true original Q, its nonconstant Walsh coefficient magnitude is ≤1/2. Hence

\[
\boxed{|\widehat S_{C/A}(T)|\le\frac{H_C(f;P_1,\ldots,P_6)}2\le480,}
\]

and

\[
\boxed{|\widehat S_{B/A}(T)|\le
\frac12\min\{(2d)^6,\ 60(2d)^4\}.}
\]

The remaining D6 sixth coefficient obeys the general |hat S_D6|≤(2d)^6/2. All four other seven-class sixth coefficients vanish EXACTLY. An issue #230 selected necessary R3 GF5 weighted sixth coefficient inherits the sum of these per-class absolute bounds with historical positive weights w_D6=5643, w_B/A=45600, w_C/A=43320 and all other terms exactly zero. Even this strong TOP-ORDER filter does NOT furnish the required initial unchanged-center positive S_s(f,g)≥c s^6; it controls magnitude of one family of high-order Fourier coefficients on neighbor cubes, not the full fixed-map count.

## Exact true-original geometric oracle and independent historical source-GF5 finite falsifiers

- All dyadic h1..36,40,48,64,80: exact arbitrary-precision source V,d,M and inclusion/exclusion H_t, t=0..7, SIX packet equality H_6=(2d)^6, classwise zero filter, uniform C/A cap 480 and refined B/A cap, no imaginary W3 high-h materialization.
- TRUE symplectic original W32/K6 schemes lex and S72: generate SIX 2-original-LINE-ID packets (12 of 15 actual original LINE IDs), each containing exactly 2d=6 REAL ORIGINAL incidence IDs. Independently enumerate ALL 6^6=46,656 sixflag packet choices via direct Cartesian product and compare EXACT sets of original POINT C-profile Q and unchanged physical LEFT-C-eligible Q against separate 15-perfect-matching genuine source-line intersection algorithm. Validate all packet-pair original point intersection counts ≤4 and historical true-original Q unicity.
- TRUE symplectic original W34/GF4 nononto physical K14 lex/random: no false s>=32 theorem promotion; direct true original W34 point-line incidence intersection matchings on six disjoint packet pairs, each of size 10 actual W3 flags, geometric C upper 960.
- Real original W32 full historical GF5 seven-class classifier on 64 COMPLETE globally injected physical LINE maps generated by six ORIGINAL factor-image swaps. Restrict to TRUE source Q with all six packets hit; independently check its only possible immutable historical class is D6/B-left/C/A, calculate all seven exact sixth Walsh coefficient numerators and verify all four prohibited classes identically zero plus C/A refined physical H_C/2 bound.
- An additional independent complete 64-map scan of all 62,370 genuine original LEFT six-coordinate Q checks classwise sixth Walsh coefficients without using the packet-support shortcut. This is finite W32 ONLY, not a high-h proof. Negative source mismatch/invalid swap packets and preconditions.

## Scope, acceptance and next step

This stage proves a real all-h **source-profile spectral filtration** and the genuinely finite-geometry line-intersection uniform top-order C/A capacity. Generalized quadrangle uniqueness and Walsh techniques are classical; these original-GF5 applications are new in this Draft research scope, not asserted peer-reviewed or globally unprecedented. We do not infer the universal unchanged-map root issue #230 Branch A bound, a true-original correlated infinite o(s^6) counterfamily (B), a qualifying equivalent reduction (C), or any complete R3/ASET exponent result. All-h algebra does not silently extrapolate finite actual W32 or W34 to a high-h fake GQ.

Next recommended open lemma: derive a sharpened fifth-order or fourth-order ORIGINAL line-packet intersection bound incorporating source POINT patterns A/B/C, and investigate whether original true-GQ constrained cross-order covariance can force a CENTER sign; on AA4-BQ and AA4-BS evidence alone this remains OPEN_WITH_FORMAL_BLOCKER. Keep Draft until exact-head dedicated/INDEX/Proof Audit/Full Research and independent mathematical referee including parent #590, not merely green CI.
