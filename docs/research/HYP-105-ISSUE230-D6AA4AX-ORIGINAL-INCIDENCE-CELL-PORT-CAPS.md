# HYP-105 #230 — AA4-AX: original mixed incidence-cell GOOD two-port activation certificate and sharp scalar spectral no-lift

**Status: restricted deterministic same-global genuine ORIGINAL pre-Hall transfer + a precise ABSTRACT scalar-method no-go. Original #230 Branch A/B/C REMAINS OPEN.** Strict additive research-only Draft child of [AA4-AW #556](https://github.com/definitely-stable/Mathlab/pull/556), frozen original parent HEAD \`0fa177eef742551cc6784f4d17cd4485374d27f7\`. Actual original symplectic W(3,s), s=2^h≥2, full globally injected typed original point and original line maps f,g into minimal physical K_a, held simultaneously FIXED for every actual original source incidence flag. Never invent source incidences for large h or independently redraw f/g per flag.

## 1. What is PRIOR and the precise missing step

- [AA4-AP #538](https://github.com/definitely-stable/Mathlab/pull/538) ALREADY proved the genuine original GQ spectral physical coordinate-cell bound \(M_{c,e}\le K=\frac{d(a-1)^2}{V}+\lceil\sqrt{2s}\rceil(a-1)\) for \(M=F^\top BG\), where \(B\) is the true W(3,s) source point-line incidence matrix, F/G the two globally fixed typed original factor-to-physical coordinate incidence matrices. It also proved the unconditional all-global GOOD bilateral D-edge population \(E_{\rm GOOD}\ge L_s\) for h≥14 (strong exact rational parameter lower).
- [AA4-AV #554](https://github.com/definitely-stable/Mathlab/pull/554) ALREADY proved \(W_{AA}^{\rm GOOD}\ge s^6/10\) TRUE original centered three-distinct-point AND three-distinct-line 3-flag wedges for EVERY full original globally injected f,g when h≥16. It also proved exact actual global source-factor degeneracy-corrected four-port 2×2 transport \(X_i(c,e)=M_{c,e}-(BG)_{p,e}-(F^\top B)_{c,\ell}+1\) for every genuine original source center flag i=(p,l).
- [AA4-AW #556](https://github.com/definitely-stable/Mathlab/pull/556) ALREADY proved the sharp original centered GOOD opposite physical two-port lower \(R_{\rm GOOD}\ge\sum_i\mathfrak F(r_i^P,r_i^L)\ge\frac12\sum_i m_i^P m_i^L\), where point/line GOOD physical port *minorities* mP,mL are measured on the same true original source flag center. Parent did NOT show this sum positive for arbitrary globally correlated f,g.

**NEW AA4-AX objective:** calculate *CERTIFIABLE* GOOD physical port minority lower bounds using ONLY the true source mixed **uncolored** original incidence-cell transport \(F^\top BG\), its genuine-original source-degeneracy correction, and true GOOD D degree at each flag, WITHOUT requiring the point×line joint GOOD four-bin distribution. Then prove exactly why the old scalars \(E_{\rm GOOD}\), \(W_{AA}^{\rm GOOD}\) and per-cell spectral upper K alone cannot establish a positive universal two-port product; document a mathematically sound numerical RELAXATION, not a false genuine original global construction.

## 2. NEW exact ORIGINAL all-h cell-cap transfer theorem

Let actual genuine original source W(3,s) have \(V=(s+1)(s^2+1)\) original points and V lines, incidence valency d=s+1 and N=Vd ACTUAL source point-line incident flag IDs. Fix *one* globally injected f,g. For every TRUE original source center flag \(i=(p,\ell)\), write f(p)=(c0,c1), g(l)=(e0,e1). Let
\[
M_{c,e}=(F^\top B G)_{c,e}
=|\{(q,m)\text{ ACTUAL original incidence flags}:c\in f(q),\,e\in g(m)\}|.
\]
All FOUR cells M_{c_u,e_v} contain the **same actual center source flag i**, and therefore have at least one entry. Define the raw true ORIGINAL **cell-cap** physical point-port row and physical line-port column upper bounds
\[
U^P_{i,u}=\sum_{v=0}^1(M_{c_u,e_v}-1),\qquad
U^L_{i,v}=\sum_{u=0}^1(M_{c_u,e_v}-1).
\]
They upper-bound, respectively, the number of other source flags sharing point port c_u and ANY line center port, and sharing line port e_v and ANY point center port, after removing at least the TWO copies of the center genuine incidence flag. Some remaining candidates may repeat an original source point or line, may violate the good physical free-port condition, or may be double-counted between the cells; these are harmless since we use strict **UPPER** capacity bounds. Crucially every eligible true original GOOD D neighbor has its **unique** physical shared point port and unique line port, because distinct globally injected source factor pair-edge images share at most ONE physical coordinate.

Let \(d_i^{\rm GOOD}\) be the true actual GOOD bilateral D degree at source center i, and \(m_i^P,m_i^L\) the two GOOD typed physical port minority counts. Since both point rows sum to d_i^GOOD and each is ≤ its individual U^P, and analogously line columns, the exact elementary capacity forcing yields:
\[
\boxed{
m_i^P\ge P_i^{\rm raw}:=
[d_i^{\rm GOOD}-\max(U^P_{i,0},U^P_{i,1})]_+,\quad
m_i^L\ge L_i^{\rm raw}:=
[d_i^{\rm GOOD}-\max(U^L_{i,0},U^L_{i,1})]_+.
}
\]
Here [z]_+=max(z,0). The true source-degeneracy-corrected ALL-D 2×2 bin \(X_i^{uv}\) of parent #554 is a still stronger upper on the corresponding TRUE GOOD physical bin. Replace U^P by the sum of each X row and U^L by the sum of each X column. This gives \(P_i^{\rm corr}\ge P_i^{\rm raw}\), \(L_i^{\rm corr}\ge L_i^{\rm raw}\), and both are ≤ ACTUAL GOOD minorities.

Applying parent #556 SHARP half-minority theorem pointwise proves the NEW **source-incidence-cell certificate**:
\[
\boxed{
R_{\rm GOOD}(f,g)\ge
\sum_{i\text{ actual source flags}}
\left\lceil\frac{P_i^{\rm corr}L_i^{\rm corr}}2\right\rceil
\ge
\sum_i\left\lceil\frac{P_i^{\rm raw}L_i^{\rm raw}}2\right\rceil.
}
\]
This is a fully deterministic true original same-global-map bound and, unlike previous AA4-AW, its RHS is computed from the TRUE original mixed source incidence-cell tensor and the uncolored GOOD D degree alone; actual joint GOOD four-bin assignment is needed **only for independent validation**. The cell-corrected transfer is valid ALL dyadic h, all genuine original full f,g. It does **NOT** assert the resulting sum is universally positive.

## 3. NEW spectral-only universal local cap, and method limitation

Since M_{c,e} are nonnegative integer actual-original flag counts, the PREEXISTING spectral inequality \(M_{c,e}\le K\) yields \(M_{c,e}\le\lfloor K\rfloor\). Consequently for all source centers i,
\[
U^P_{i,u},U^L_{i,v}\le T_s=2\lfloor K\rfloor-2,
\]
and hence
\[
\boxed{
R_{\rm GOOD}(f,g)\ge
\sum_i\left\lceil
\frac{[d_i^{\rm GOOD}-T_s]_+^2}{2}\right\rceil.
}
\]
This is an ALL-h all-fixed original/source-GQ **HIGH-DEGREE activation theorem**. Any true source flag with \(d_i^{\rm GOOD}>T_s\) necessarily has BOTH point typed physical ports AND BOTH line typed physical ports active, with at least the displayed positive count of actual physically opposite GOOD three-source-flag wedges. It does not automatically yield any TRUE original 6-ID Hall extension or seven-GF5 class.

**Critical exact quantitative failure of the old scalar strategy:** For ALL dyadic h≥16, define d=s+1, N=Vd and take an *ABSTRACT local numerical RELAXATION*, where every one of N local vertices is assigned the four-bin tuple \((4d,0,0,0)\) and numerical degree \(4d\). This is explicitly NOT asserted to be a genuine globally labeled original flag graph (the local cells need not glue into a true global FᵀBG tensor). Its **scalar** undirected edge proxy is \(N(4d)/2=2Vd^2\), which dominates the true all-global AA4-AP GOOD D lower \(L_s\): minimal physical alphabet has \(a^2>2V\), so AA4-AP's upper of its own positive lower parameter is \(L_s<2Vd^2\).

Its all-distinct-source wedge **numerical proxy** is \(N\binom{4d}{2}\ge s^6/10\), so the AA4-AV SOURCE A/A GOOD wedge lower is numerically satisfied. Its cell size requirement is \(4d+1\) (the center flag plus 4d formally colocated neighbors) and even this fits the **PREEXISTING scalar GQ spectral one-cell cap** for all h≥16: original minimal a satisfies a−1≥d, sigma=ceil√(2s)≥5, and \(K=\frac{d(a-1)^2}{V}+\sigma(a-1)\ge5d+\text{positive}\), so \(\lfloor K\rfloor\ge4d+1\).

Yet every formal local vertex is physically monochromatic on BOTH typed physical ports; its opposite count \(R_i=0\), and \(\sum_i m_i^Pm_i^L=0\).

**Exact logically supported NO-GO:** the three SCALAR statements “many GOOD original D edges”, “many SOURCE A/A GOOD 3flag wedges” and “each physical FᵀBG cell ≤K” **do not by themselves logically imply a positive opposite-port count**. The explicit abstract local data satisfy their numerical restrictions and have zero opposite-port products. This does NOT disprove any stronger theorem using **true joint globally injected source incidence-cell compatibility**, does NOT supply ANY actual original GQ fake labeling or original infinite counterfamily and does NOT refute root Branch A. It identifies which missing information matters: nontrivial mixed physical cell layout, the 2×2 global f/g source correlations and/or higher-order incidence expansion, beyond the used scalars.

The actual global mixed transport and corrected source caps in the previous section retain that information and can give nonzero numerical certificates in genuine finite models, even when the universal K-only cap is vacuous.

## 4. Strict independent TRUE ORIGINAL finite oracles and all-h proof gates

FOUR additive research-only files: explicit all-h original spectral row cap and abstract scalar-method limitation, true finite original FᵀBG cell RAW+source-corrected GOOD physical port minority activation, **independent direct original source flag Q-first matrix M** and literal original D-neighbor source-factor exclusion oracle, comprehensive versioned mathematics and GitHub-hosted ONLY dedicated workflow.

Independent audits:
1. All dyadic h=1,...,80 exact rational source spectral K integer floor, original minimal palette a, source valency, original flag count and scalar abstract regular-degree/AA-wedge/cell-bound nonimplication h≥16, with no synthetic high-order finite GQ construction.
2. Five complete genuine original W32 globally injected typed f,g K6 models (dual-zero, lex, reverse, S68, S72), all 45 ORIGINAL source flags and all four center point/line physical mixed cells; independently reconstruct literal actual-original source-flag Q-first FᵀBG and the FULL original D-port 2×2 table by source-first exclusion, compare with inherited tensor and nested source/physical cap floors. A different original GOOD D physical neighbor oracle checks each forced minority and actual R; prior #554 genuine source A/A GOOD wedge and #556 sharp-marginal floors independently reconciled.
3. Genuine symplectic W34 lex/random full globally injected source factor f,g K14 with **six globally unoccupied physical pair edges per type**, all 425 actual source flags and mixed physical cells; no random per-Q source physical maps, no full seven-GF5 census.
4. Original source symplectic transvection and **two different typed physical-coordinate relabels** preserve true-original invariant scalar cell capacity/forced GOOD opposite counts.
5. All-h proof that \(T_s=2\lfloor K\rfloor-2\) is a valid per-point-port and per-line-port original GQ spectral candidate upper, and a **separate honest method no-go numerical relaxation** never presented as an actual original W(3,s) model. Fake incomplete source incidence, noninjective full physical source maps and bad parameter s rejected.

**Acceptance:** strict research-only Draft child of #556 pinned to exact parent SHA. Require exact FINAL child SHA GitHub-hosted dedicated / INDEX / Proof Audit / Full Research SUCCESS, plus separate INDEPENDENT mathematics referee, before accepted SHA-pinned scientific RCP JSON promotion or five regenerated derived registries. Main unchanged; root #230 OPEN. **Next AA4-AY**: Prove lower on the globally coupled actual original mixed FᵀBG source cell-cap excess-degree activation charge, or a genuine original infinite globally complete counterfamily; a lower deduced merely from old E_good/W_AA scalar moments+K is mathematically ruled out as a method. Separately any positive GOOD opposite threeflag count still needs the actual original residual T/P and 3×3 Hall survival and final positively selected sevenclass GF5 alignment.
