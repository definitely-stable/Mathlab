# HYP-105 / #230 — AA4-SPW: original-GQ spectral pencil return bound \(O(s^4)\)

**Status:** rigorous **all-\(h\)** deterministic source-geometric inequality; independently checked exact finite integer spectra and original source collinearity on \(W(3,2)\), \(W(3,4)\). Root issue remains **OPEN_WITH_FORMAL_BLOCKER**, not all-seven-class \(\Omega(s^6)\) and not an ASET improvement.

## 1. Motivation and prior frontiers

The stacked AA4-LCR-W slice in PR #653 proves for genuine symplectic \(W(3,s)\), \(s=2^h\), arbitrary *complete separately globally injective*, possibly correlated typed physical pair labels \(f,g\):

\[
J_x=2\sum_{p,y}\binom{d_p(y)}2,\qquad
J_y=2\sum_{l,x}\binom{e_l(x)}2,
\]

where \(d_p(y)\) counts original **LINES through genuine source point** \(p\) whose injected coordinate-pair label \(g(l)\) contains the physical symbol \(y\), and \(e_l(x)\) is the dual count for original source points on \(l\) whose physical label contains \(x\). The previous elementary upper was \(J_x,J_y\le Vs(s+1)=O(s^5)\) for \(V=(s+1)(s^2+1)\).

PR #654 (AA4-COMP) separately proved exact simple-six-cycle completion kernel \(\operatorname{comp}_6(w)\) and \(W_{2,x}=\sum_{w\in\mathcal J_x}\operatorname{comp}_6(w)\) (similarly y). Its suggested \(O(s)\) mean completion gate depended on the **weaker** previous \(O(s^5)\) wedge count. The present theorem makes that gate easier *without making assumptions about completions*.

The source incidence singular spectrum of genuine \(W(3,s)\) had been studied in parallel AA4-DM and AA4-DEG. We do not claim the **classical GQ eigenvalues** as new mathematics. The new contribution to Mathlab is the exact **source collinearity + occupied physical coordinate-star** wedge transfer and \(O(s^4)\) universal bound, including its original-flag and exact integer audit.

## 2. All-h original line-collinearity graph identity

Let \(M\in\{0,1\}^{V\times V}\) be the *genuine* original GQ source POINT–LINE incidence matrix, \(d=s+1\). Source girth eight implies two distinct source lines meet in at most one original source point, so the original line-collinearity adjacency

\[
C_L=M^{\mathsf T}M-dI
\]

is a simple unweighted graph adjacency on \(V\) original source LINE IDs. It is strongly regular with parameters

\[
(V,k,\lambda,\mu)=
((s+1)(s^2+1),s(s+1),s-1,s+1).
\]

This yields the **exact integer matrix identity** for every genuine \(W(3,s)\):

\[
\boxed{C_L^2=(s^2-1)I-2C_L+(s+1)J.}
\]

The line-collinearity graph has trivial eigenvalue \(k=s(s+1)\) and nonconstant eigenvalues \(s-1\), \(-s-1\). The same is true of the point-collinearity adjacency \(C_P=MM^{\mathsf T}-dI\).

**Important boundary:** an arbitrary regular source incidence graph need not satisfy this polynomial or the subsequent spectral inequalities. Every scientific quantifier below explicitly requires the **genuine original symplectic** source \(W(3,s)\); no synthetic or randomly regular source substitution is permitted.

## 3. A new all-h fixed-map spectral pencil inequality

For every physical line-coordinate \(y\in[a]\), define the set of **actual original source line IDs**

\[
S_y=\{l:\ y\in g(l)\},\qquad t_y=|S_y|.
\]

Exactly because distinct source lines have at most one common source point, and every counted pair of source lines at fixed \(y\) yields precisely one original pencil wedge, we have

\[
\boxed{
J_x=2\sum_y E(C_L[S_y]).
}
\]

Here \(E(C_L[S_y])\) is the number of *unoriented original collinear line pairs* fully contained in the fixed occupied physical coordinate star \(S_y\). This is an exact original-incidence identity, not a physical-corner surrogate.

Let \(\boldsymbol{1}_{S_y}=\frac{t_y}{V}\boldsymbol1+z_y\), where \(z_y\perp\boldsymbol1\). Use the known **maximum nonconstant** source line-collinearity eigenvalue \(s-1\):

\[
\begin{aligned}
2 E(C_L[S_y])
&=\boldsymbol1_{S_y}^{\mathsf T}C_L\boldsymbol1_{S_y}\\
&\le\frac{k}{V}t_y^2
+(s-1)\left(t_y-\frac{t_y^2}{V}\right)\\
&=(s-1)t_y+\frac{s^2+1}{V}t_y^2.
\end{aligned}
\]

Since \(J_x=\sum_y 2E(C_L[S_y])\) and each occupied physical pair contains exactly two symbols, \(\sum_y t_y=2V\). Consequently, for **every** allowed fixed complete injected \(f,g\), with no distributional assumptions,

\[
\boxed{
J_x\le 2V(s-1)+
\frac{s^2+1}{V}\sum_y t_y^2.
}
\]

The dual source **point** collinearity graph and \(r_x=|\{p:x\in f(p)\}|\) give

\[
\boxed{
J_y\le 2V(s-1)+
\frac{s^2+1}{V}\sum_x r_x^2.
}
\]

### Minimal physical alphabet and genuine pair injection

Every distinct original source LINE image is an occupied edge in the same **simple** \(K_a\) on the second coordinates, so \(\max_y t_y\le a-1\), and \(\sum_y t_y^2\le(a-1)\sum_y t_y=2V(a-1)\). The point labels satisfy the same property. Thus:

\[
\boxed{
J_x,\ J_y\le
2V(s-1)+2(s^2+1)(a-1)
=\mathbf{O(s^4)}.
}
\]

Here \(V=(s+1)(s^2+1)=\Theta(s^3)\) and the **minimal** physical alphabet \(a=\Theta(\sqrt V)=\Theta(s^{3/2})\). The first right-hand term is \(O(s^4)\), while the second is \(O(s^{7/2})\). Both inequalities hold for every dyadic \(h\ge1\) without independent f/g sampling, an average over labels or any regularity of the physical graph.

The all-h \(O(s^4)\) estimate is strictly better in exponent than the earlier \(O(s^5)\), but the finite **integer** coefficients need not attain an asymptotic optimum.

## 4. Exact original-source integer oracles and independent falsifiers

The spectral certificate rebuilds the **true** original symplectic source GQ line-point incidence. It independently checks every entry of

\[
C_L^2=(s^2-1)I-2C_L+(s+1)J
\]

using only integer cardinalities of original collinearity neighborhoods, not floating-point eigensolvers. It rejects a regular degree-preserving non-GQ 2-edge switch in the original incidence graph.

A second independent oracle directly counts original collinear line pairs inside each actual occupied physical coordinate star \(S_y\), and similarly original point pairs inside each x-star; its results match the *independent original pencil* and *independent physical corner-neighbor wedge* algorithms. The spectral upper comparisons use the exact integers \(VJ_x\) and \(VJ_y\), with no float roundoff or asymptotic extrapolation.

| True complete globally injected map | \(J_x\) | \(J_y\) | Spectral \(J_x\) upper | Spectral \(J_y\) upper | Alphabet-only cap (each) | Previous bound (each) |
|---|---:|---:|---:|---:|---:|---:|
| \(W(3,2)\), lex \(K_6\) | 64 | 52 | \(1200/15=80\) | \(1200/15=80\) | 80 | 90 |
| \(W(3,2)\), reverse-line \(K_6\) | 42 | 52 | \(1200/15=80\) | \(1200/15=80\) | 80 | 90 |
| \(W(3,4)\), adversarial full \(K_{14}\) | 624 | 602 | \(78642/85=925.2\) | \(78880/85=928\) | 952 | 1,700 |

The W(3,4) coordinate-star occupancy sums are \(\sum_y t_y^2=2076\) and \(\sum_xr_x^2=2090\), and each finite assertion is preserved under independent physical coordinate permutations. The tests explicitly refuse noninjective/incomplete maps and non-GQ source geometry, rather than silently applying the spectral theorem to a surrogate.

## 5. Consequence for the completion barrier — conditional, not root proof

Let \(\mathcal J_x,\mathcal J_y\) denote the genuine-returning physical wedges in PR #654 and \(\operatorname{comp}_6(w)\) their exact physical simple C6 completion number. By the existing **exact all-h double count**,

\[
W_2=
\sum_{w\in\mathcal J_x}\operatorname{comp}_6(w)
+\sum_{w\in\mathcal J_y}\operatorname{comp}_6(w).
\]

**A changed conditional frontier:** if one could independently prove **uniformly over all fixed complete possibly correlated maps** that the *mean* completion count over each nonempty wedge class satisfies \(O(s^2)\), then the new \(J_x,J_y=O(s^4)\) would imply \(W_2=O(s^6)\). This is substantially weaker than the former \(O(s)\) mean-completion premise and is not established in this slice.

Even that conditional \(W_2=O(s^6)\) would **not** bound pure-three-step coordinate returns, imply positive D6, or prove the historical **sum of seven original GF(5)-accepted six-distinct-incidence classes** \(\Omega(s^6)\). Those are separate source-sensitive blockers. The large-five-ID counterfamily and its coherent D6 compensation in PR #651 remain valid and are not bypassed by a pure source-pencil bound.

**Next P0:** test the fixed-map-uniform \(O(s^2)\) completion mean against the existing **infinite paired-subfield correlated maps** of PR #651, or develop a direct source-collinearity codegree argument for the sixcycle completion kernel. Reject any assertion of \(\operatorname{Defect}_6(H)=O(s^6)\) derived from \(J_x,J_y=O(s^4)\) alone.
