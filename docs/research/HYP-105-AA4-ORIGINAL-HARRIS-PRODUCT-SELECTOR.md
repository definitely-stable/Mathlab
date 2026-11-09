# HYP-105 / #230 — AA4-HARRIS: NEW all-h ORIGINAL local-priority product selector, 19.63× stronger adversarial deletion budget

**Mathematical scope:** strict scientific child of [Draft PR #753](https://github.com/definitely-stable/Mathlab/pull/753) frozen HEAD 3109d2bea8c325c907f34a574fa3b7170997dfe0. This slice independently proves a new ALL-ORDER source-priority probability inequality, replacing the older conservative r-first original J-owner survival bound at the exact LOW selector interface, and explicitly propagates the *improved* r=2/3 constants through the existing conditional original LOW/HEAVY numerical proof chain. Additionally it proves an ALL-ORDER nonzero (although still very weak) bound on the incompatible same-endpoint path pair weight B from #753. It includes independent exact real-original GQ source falsification, independent finite J graph priority enumeration, and a fail-closed workflow. No parent or main branch edited, no PR merge, no closure of root #230, no purported numeric graph supersaturation constants, and no automatic promotion of the full root Branch A theorem or new ASET exponent.

## 1. New independently proved source priority inequality — all dyadic h and arbitrary correlation

For EVERY genuine ORIGINAL symplectic generalized quadrangle W(3,s), s=2^h, every pair of fixed complete separately globally pair-injective maps f:P→binom([a],2) and g:L→binom([a],2) with arbitrary correlation, any adversarial named-original-ID deletion Z, and any remaining paired original core C⊆I\Z, let J_C be the true original point/line pencil-conflict graph on C. Its maximum original degree K is at most 64 in the pruned LOW branch; this degree cap is not needed for the more general degree-adaptive claim.

For each coordinate-proper directed TRUE physical CORE rpath γ, r∈{2,3}, its r original physical edge owners S={i_1,...,i_r} are distinct and pairwise J_C-nonadjacent, by separate global pair-injection of f and g and the requirement that all r+1 first-coordinate symbols and all r+1 second-coordinate symbols along γ are distinct. Each original owner carries BOTH real opposite physical rectangle diagonals. The original priority selector assigns ONE uniform random total order on all original IDs in C and keeps a flag i if and only if i is earlier than every neighbor in J_C, independently then requiring two real typed binary factor-pair crossing cuts.

The old all-h source proof #738/#745/#751 used the sufficient event that all r owner IDs are the first r elements of their union of original closed J-neighborhoods U_γ. This gives

\[
\Pr(S\text{ priority selected})\ge\binom{|U_\gamma|}r^{-1}
\ge\binom{r(K+1)}r^{-1}.
\tag{OLD-1}
\]

This is VALID but needlessly loses dependence structure among the original local minimum events. The NEW result gives a universally stronger *uniform K-based* bound, plus a degree-adaptive one that may be weaker or stronger than the individual first-r source event on a specific path.

### All-h ORIGINAL Harris/FKG association proof (self-contained)

Assign independent continuous random priorities T_i∼Uniform(0,1) to every i∈C. This induces the exact same uniform global original source order, with ties of probability zero. Let E_i={T_i<T_j for ALL original J_C neighbors j∈N_J(i)}. By the exchangeability of the 1+deg(i) independently drawn priorities on {i}∪N_J(i),

\[
\boxed{\Pr(E_i)=\frac1{1+d_J(i)}.}
\tag{H-1}
\]

Since the proper path owner set S is an independent set in the genuine original J_C, for ALL owners i∈S transform Y_i=1−T_i; leave Y_j=T_j for all outside owners j∉S. This is a measure-preserving per-coordinate map of independent uniforms. Every local-minimum condition for a source owner i∈S and its actual neighbor j∈C\S becomes

\[
T_i<T_j\iff Y_i+Y_j>1.
\]

There are NO J edges between distinct owners in S, so all such conditions (and therefore all E_i, i∈S) are **coordinatewise nondecreasing functions of ONE common independent vector Y**.

Elementary product-measure positive association: if F,G are bounded coordinatewise nondecreasing functions of independent scalar random variables, then E(FG)≥EF·EG. For a single independent scalar variable U and independent copy U',

\[
2\operatorname{Cov}(F(U),G(U))=
\mathbb E[(F(U)-F(U'))(G(U)-G(U'))]\ge0.
\]

For independent multiple coordinates, successively condition on the others and induct; conditional expectations preserve monotonicity. Iterating association over the increasing indicators E_i and their products therefore yields

\[
\boxed{\Pr(\bigcap_{i\in S}E_i)\ge
\prod_{i\in S}\Pr(E_i)
=\prod_{i\in S}\frac1{1+d_J(i)}
\ge\frac1{(K+1)^r}.}
\tag{H-2}
\]

**Scope warning:** if any two owners in S have a genuine J edge, they are MUTUALLY EXCLUSIVE, and H-2 is false. Here pairwise J-independence is DETERMINISTICALLY guaranteed by a coordinate-proper original-source physical path and complete separate global pair-injection, not assumed for arbitrary unrelated source IDs.

### The REAL physical typed cuts

A proper rpath has r+1 distinct typed physical symbols in EACH factor. The original f-pairs of its true incidence-ID owners are precisely the r edges joining successive first-coordinate symbols, and similarly for g and the second factor. Exactly TWO of the 2^{r+1} fair binary assignments on each factor make the entire rpath alternating; therefore each factor contributes exactly 2^{-r}, independently of original priorities and the OTHER factor cut. Both actual physical opposite diagonals of each selected source flag remain whole, not cloned or separately randomized.

Therefore, for every original proper rpath (and r=2,3 in the LOW proof),

\[
\boxed{
\Pr(\gamma\text{ retained})
\ge\underbrace{4^{-r}\prod_{i\in S_\gamma}
\frac1{1+d_J(i)}}_{\text{NEW degree-adaptive original source certificate}}
\ge\underbrace{\frac1{4^r(K+1)^r}}_{=\sigma_r^{\mathrm H}}.
}
\tag{H-3}
\]

The two distinct valid adaptive lower bounds \(\binom{|U_\gamma|}r^{-1}\) and \(\prod_i(1+d_J(i))^{-1}\) may be **combined by max**, but neither adaptive bound universally dominates the other for an individual path: if three independent owners all share one outside J neighbor, the exact original priority joint is 1/4, the old first-r bound is 1/4, and the new degree-product bound is 1/8. The **GLOBAL worst-case K=64** H-3 nonetheless strictly improves the historical uniform worst-case \(\sigma_r\).

## 2. New universal selector constants: exact arithmetic, not simulation

The old selector constants in #751 were

\[
q_2^{old}=4^2\binom{2(K+1)}2=134160,\quad
q_3^{old}=4^3\binom{3(K+1)}3=77879360.
\]

H-3 replaces these with

\[
\boxed{
q_2^{\mathrm H}=4^2(K+1)^2=67600,\quad
q_3^{\mathrm H}=4^3(K+1)^3=17576000.
}
\tag{H-4}
\]

Thus

\[
\boxed{
\frac{q_2^{old}}{q_2^{\mathrm H}}=\frac{134160}{67600}\approx1.984615,\quad
\frac{q_3^{old}}{q_3^{\mathrm H}}=\frac{77879360}{17576000}\approx4.431006.
}
\tag{H-5}
\]

This strengthening is valid for **every** legal original fixed correlated f/g labeling and every original LOW pruned core with source degree ≤64, even if the source owner neighborhoods overlap in adversarial ways.

### Jensen transfer retained with strictly stronger coefficients

For the true source original proper ordered path endpoint tensor P_r(u,v), and for ONE random original rank/two-cut selected genuine graph G_ω, let X_{r,ω}(u,v) count the actually selected proper paths. By the same completely general expectation linearity and Jensen (no independence between different paths),

\[
\begin{aligned}
\|P_r\|_F^2/(q_r^{\mathrm H})^2
&\le\|\mathbb E X_{r,\omega}\|_F^2\\
&\le \mathbb E\|X_{r,\omega}\|_F^2\\
&\le \mathbb E\operatorname{tr}(A_{G_\omega}^{2r}).
\end{aligned}
\tag{H-6}
\]

The selected graph is STILL bipartite by the first typed binary cut, has the SAME real original owner and ordinary graph maximum degree, and STILL injects every simple C6 into the same original positive D6 source class. The external graph C6 supersaturation theorem and the HEAVY ordinary graph construction are **unchanged**. This is purely a stronger independently proved selector interface, not an unlicensed change to the source model.

## 3. Full conditional all-h LOW/HEAVY constants, including original Z budget

Keep precisely the previously verified input constants from #750/#751: set

\[
R=93313,\ K=64,\quad
\delta=\frac{c_0}{R^6},\quad
T=\left\lceil\frac{17}{2}R^3 C_0^3\right\rceil,\quad
L_6=24+153T^2.
\]

Here \(C_0\ge\max(1,C_{\rm graph})\) and \(0<c_0\le\min(1,c_{\rm graph})\) are fixed ONCE, existential rational relaxations of the published ordinary C6 supersaturation constants, prior to choosing s,f,g,Z. No numerical values are asserted from the paper; displayed probe values such as (1,1) are FORMAL-only.

The source selector change affects exactly the LOW terms that depend on r2/r3 path survival, while the true original FULL-A/CORE-C two mixed blocker books, original endpoint projection and old external graph theorem require no new assumption. Define

\[
\begin{aligned}
q_2&=67600,\quad q_3=17576000,\\
L_4^{\mathrm H}&=
q_2^2\left\lceil\sqrt{\left\lceil17L_6/4\right\rceil}\right\rceil+19T,\\
B_0&=\left\lceil\sqrt{360(K+1)T}\right\rceil,\\
E_{\mathrm H}&=5q_3\lceil\sqrt{L_6}\rceil,\\
D_{\mathrm H}&=4\left\lceil\sqrt{B_0T L_4^{\mathrm H}}\right\rceil,\\
s_{0,\mathrm H}&=\max\{64,444T,(8E_{\mathrm H})^2,(8D_{\mathrm H})^8\},\\
t_\star&=\frac{119}{24}-2\frac{54162}{53838}\delta,\\
\boxed{\rho_{\mathrm H}}&=
\frac{t_\star^2}{12q_3^2L_6}.
\end{aligned}
\tag{H-7}
\]

**Exact preserved gates:** 1) HEAVY ordinary graph-density choice of T and R is unchanged, 2) the surviving original physical CORE has |C|≥¾s⁴ since ρ_H is still below 2^{-32} and 3/64, 3) max true physical degree Δ≤Ts, full paired-edge m≤17s⁴/8, original source K≤64, 4) coordinate-improper LOW error ≤(111/2)Ts⁵, 5) original non-Z end-bad energy ≤E_H s^{11/2}, 6) true original four A/C blockers ≤D_H s^{47/8}, 7) the Z-mask error by genuine three GQ anchor roles ≤q3√(12L6ρ_H)s⁶=t_\star s⁶, and 8) three other LOW errors each ≤s⁶/8 for dyadic s≥s0_H. The exact source original 2-to-1 BBo inverse thus retains the SAME positive LOW BBo sextic floor \( (54162/53838)\delta\,s^6\), conditionally on the inherited source lemmas and HEAVY graph theorem. The additive accepted full GF(5) signed risk coefficient is unchanged. The positive source coefficient δ of D6 in HEAVY is unchanged.

The improvement of the allowed *named ORIGINAL source-ID deletion radius* compared to #751 follows by exact cancellation of identical t_star,L6:

\[
\boxed{
\frac{\rho_{\mathrm H}}{\rho_{\rm old}}
=\left(\frac{q_3^{old}}{q_3^{\mathrm H}}\right)^2
=\left(\frac{77879360}{17576000}\right)^2
\approx19.6338134.
}
\tag{H-8}
\]

This is a **19.63× improvement to the previously extremely conservative positive deletion coefficient**, NOT a factor 19.63 improvement in the absolute Branch A six-motif leading constant, not an engineering speedup, and not an ASET exponent. It remains tiny because T is an enormous formal function of the existential external graph constant C0.

The strict old HEAVY density/pruning requirement remains safe: for ANY C0≥1, \(T\ge1,L_6\ge24\), \(0<t_\star<119/24\), hence

\[
0<\rho_H<
\frac{(119/24)^2}{12(17576000)^2\cdot24}
<2^{-32}.
\tag{H-9}
\]

Thus even this larger ρ_H does NOT invalidate the old fixed HEAVY R=93313, ROOT D6 c0/R^6 or physical-density argument. The new proof remains conditional on other inherited all-h source lemmas; the change to H-2/H-3 is an independent complete mathematical proof.

### Exact rational FORMAL examples (C0,c0 are NOT actual published numeric graph constants)

| FORMAL input (C0,c0) | Previous h0 for dyadic s | Harris h0 | Gain | New ρ_H / old ρ |
| --- | ---: | ---: | ---: | ---: |
| (1,1) | 751 | **743** | 8 dyadic exponents | ~19.634 |
| (2,1/5) | 781 | **773** | 8 dyadic exponents | ~19.634 |
| (7/3,1/17) | 787 | **779** | 8 dyadic exponents | ~19.634 |

The independent program uses arbitrary-size integers, exact Fraction rational comparisons, exact integer ceiling square roots and no float comparisons in the scientific gates. Its TEST-ONLY cross-check loads #751's **unchanged** old all-h LOW ledger and requires exact agreement for old q2/q3,L4/E/D/T/s0/rho, before asserting strengthened new constants.

## 4. NEW ALL-h source-compatible lower good-pair mass, hence a nonzero but weak B upper bound

The predecessor [#753](https://github.com/definitely-stable/Mathlab/pull/753) proved the exact covariance sign and factor-four compatibility theorem for two proper physical directed 3paths with the SAME ordered physical endpoints. The obstruction weight B is the exact sum over INCOMPATIBLE ordered same-endpoint path pairs of the PRODUCT of their individual actual selector survival probabilities, with incompatibility equivalent to source J conflict or opposite-depth typed physical inner coordinate equality. Let G be the analogous compatible pair product sum, M=G+B=||E X_3||_F².

H-3 **does imply** an unconditional uniform nonzero compatible fraction, but nowhere near strong enough to obtain a fourfold overall sixth-moment improvement by simply dropping B. Here is a new explicit ALL-h bound, valid for the exact true ORIGINAL source selector:

For each ordered physical endpoint pair (u,v), let \(\Gamma_{uv}\) be the actual proper physical 3paths with those endpoints, and let \(p_\gamma=\Pr(\gamma\text{ survives the ORIGINAL selector})\). All are positive and satisfy \(\sigma_3^{\mathrm H}=1/[64(K+1)^3]\le p_\gamma\). Define \(W_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma\).

Now draw the SAME original source priority experiment but choose each of the two actual typed physical fair-bit colorings **CONDITIONED** to assign the shared ordered physical endpoint bits (first endpoint 0, last endpoint 1). This conditioning is legitimate because a proper physical path has distinct typed endpoint symbols. For every actual proper physical length-three path, given the endpoint bits, each of its two internal symbols in each typed factor is uniquely prescribed to satisfy the alternating crossings; the conditional color probability is precisely (1/4)²=1/16. Therefore its conditional **full-source-selector** survival probability is \(p_J(S_\gamma)/16=4p_\gamma\).

In this endpoint-conditioned experiment define the nonnegative random weighted selected-path count

\[
Y_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma\,\mathbf1\{\gamma\text{ selected}\}.
\]

Then, with **NO path independence** assumption,

\[
\mathbb EY_{uv}=
4\sum_{\gamma\in\Gamma_{uv}}p_\gamma^2
\ge4\sigma_3^{\mathrm H}W_{uv}.
\tag{H-10}
\]

For every concrete realization of the actual original-source priority and two factor cuts, ANY two selected paths are automatically J-compatible and bichromatically compatible (their owner sets are subsets of ONE original local-minimum independent set; both typed cuts are shared). Thus \(Y_{uv}^2\) contains ONLY terms of the geometrically compatible original path-pair set, each bounded by its unselected product \(p_\gamma p_\eta\). Let \(G_{uv}\) denote the sum of these products over all compatible ordered pairs in this endpoint bin. Hence the pointwise bound \(Y_{uv}^2\le G_{uv}\) and Jensen together imply

\[
\begin{aligned}
G_{uv}&\ge\mathbb EY_{uv}^2
\ge(\mathbb EY_{uv})^2\\
&=16\left(\sum_{\gamma\in\Gamma_{uv}}p_\gamma^2\right)^2
\ge16(\sigma_3^{\mathrm H})^2W_{uv}^2.
\end{aligned}
\tag{H-11}
\]

Summing endpoints and setting \(\varepsilon_H=16(\sigma_3^{\mathrm H})^2\) yields the true universal original source bound

\[
\boxed{
G\ge\varepsilon_H M,\qquad
B\le(1-\varepsilon_H)M,\qquad
\varepsilon_H=\frac1{256(K+1)^6}
=\frac1{256\cdot65^6}.
}
\tag{H-12}
\]

This gives an explicit **uniform quantitative obstruction bound on B** for all dyadic s and all original fixed correlated f/g and adversarial Z. But \(\varepsilon_H\) is extremely small, and cannot yield \(B<\tfrac34 M\). In fact combining H-12 with the #753 new bound \(M\le L_6s^6/4+B\) would give \(M\le(L_6/(4\varepsilon_H))s^6\), much WORSE than the previous ordinary Jensen \(M\le L_6s^6\). Thus H-12 is a mathematically valid structural fallback and falsifier, **not** a license for a factor-four uniform LOW moment claim.

The immediate useful LOW improvement of THIS PR is instead the rigorously better \((q_2^{\mathrm H},q_3^{\mathrm H})\) in H-4, propagated through H-7/H-8. A meaningful stronger B estimate would still need a new source-geometric bound on the actual original J/opposite-depth collision weight, for example \(\sup_{f,g,Z}B/M<3/4\).

## 5. Independent original-source and small-graph falsification

The new main referee imports ONLY the genuine symplectic W(3,2),W(3,4) incidence source constructor, and rebuilds fixed original globally pair-injective f/g maps, ORIGINAL J pencil conflicts, actual full paired-source core C with named deletion Z, BOTH real diagonal physical edges for each flag, and every physical coordinate-proper length-two and length-three path. Its exact rank probability is computed by a new owner-permutation order-statistic integral with rational terms (≤3!), and its lower bound directly via the original owner degrees. It checks the older first-r local bound independently; on a particular source triple the two valid adaptive bounds may be ordered either way. The true independent original closed-neighborhood poset linear-extension integer DP (different algorithm) cross-checks the priority formula, and all 2^(2(r+1)) literal physical typed cut assignments are enumerated for r=2,3.

Finite source cases:
- W(3,2) original FULL lex, FULL reverse and shifted real original Z17 deletion: ALL true original CORE coordinate-proper directed 2paths/3paths enumerated, original J degree checked, degree-adaptive and old priority floors compared to exact probabilities on every path.
- W(3,4) true original 425 flag geometry, lex/reverse with even original CORE and shift with explicit original Z17 deletion: deterministic samples of 160 physical paths per r per configuration, expressly **NOT** full W34 path enumeration.
- Separate exhaustive plain J algebra falsifier: **all 2^10=1024 simple undirected graphs on five owner vertices**, every J-independent 2- or 3-owner subset, every global 5! source priority permutation; verify exact joint local minima >= product of exact one-owner 1/(deg+1). This is an independent finite falsifier of H-2, NOT a replacement for its all-h monotonicity proof.
- New direct **complete true-original W32 same-endpoint B/G weighted source audit** in three fixed complete global f/g mapping schemes, including actual original Z deleted flags: all 4370/2942/1766 directed ordered same-endpoint proper physical 3path pairs; reconstruct each exact marginal p_gamma and the source J/cross-depth four-way incompatibility directly; check G+B=M, the new instance-sensitive endpoint-conditioned lower G≥16Σ_bins(Σ_path p_gamma²)² and H-12 with exact rational arithmetic. Earlier AA4-DICHOTOMY routines are NOT imported by the main referee.

**Strongest scientific acceptance scoped to this PR:** all-order Harris source-owner product-retention lower, stronger LOW selector constants and purely conditional propagation of old all-h LOW/HEAVY inequalities with increased original Z deletion budget; independently rigorous weak uniform all-h incompatible pair-weight B estimate. **Unaccepted:** complete root HYP-105/Branch A proof DAG, arbitrary strengthening of accepted additive GF5 R3 to an overlapping event UNION probability, exact published C0/c0 numeric constants, ASET exponent and any merge/issue closure. The scientific status remains OPEN_WITH_FORMAL_BLOCKER.

**Next independently valuable gate:** directly bound the original incompatible pair weight B through the now explicit original source J owner conflicts and the four opposite-depth inner physical coordinate equalities. Target \(B/M<3/4\) (uniformly in correlated fixed f/g) if possible, or find a **real ORIGINAL symplectic adversary** refuting that target; do not infer a global 4× sixth-moment improvement from the weak epsilon_H bound.
