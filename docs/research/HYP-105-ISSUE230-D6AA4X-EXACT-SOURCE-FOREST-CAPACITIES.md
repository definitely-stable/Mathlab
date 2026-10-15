# HYP-105 / issue #230 — D6-AA4-X: ALL-h exact ORIGINAL six-source-forest capacities and two selected seven-GF5 ensemble sectors

**Mathematical scope:** genuine ORIGINAL symplectic generalized quadrangle W(3,s), s=2^h, h>=1; six **distinct actual original point-line incidence IDs**; complete source incidence graph with V=(s+1)(s²+1) original points and V original lines, degree d=s+1, N=Vd original incidences, source girth 8. No physical relabeling is needed for the two new SOURCE-only counts. The GF5 corollary subsequently uses exactly the independently proved [AA4-W #494](https://github.com/definitely-stable/Mathlab/pull/494) full uniform globally injected pair-image kernel, not per-Q independent maps.

**Research-only stacked Draft** child of [AA4-W PR #494](https://github.com/definitely-stable/Mathlab/pull/494) pinned parent exact HEAD \`f36d809b976d4dfaa1d1cb84f2c22a13bd1f4011\`. This is deliberately **AA4-X-SRC** rather than the already existing **AA4-X-CYC PR #493** in the parallel cyclic variance/swap branch. We do not duplicate its global line-swap Pareto analysis. HYP-105 root #230 Branch A/B/C remains OPEN.

## 1. New ALL-h exact B/C and C/B source-forest cardinality — four-edge path + disjoint two-edge path

The TRUE ORIGINAL source profile B/C means one original **point** appears twice among the six flags (B=(2,1,1,1,1)), and three distinct original **lines** each appear twice (C=(2,2,2)); because the original GQ source graph has girth 8, any six original selected incidences form an acyclic max-degree-two graph of paths. Exactly one four-original-incidence path

\[
p_0-\ell_1-p_2-\ell_3-p_4
\]

contains the repeated original point and two repeated original lines, and the other two original incidences form one vertex-disjoint original line-centered path \(q_0-m-q_2\). Both path components are intrinsically distinguishable by length, so no division for component interchange is needed.

The number of **undirected** genuine original four-edge point→point paths, counted with endpoints both orientations then divided by 2, is exactly

\[
P_4=\frac{V\,d(d-1)^3}{2}.
\]

Fix any one such path. Delete its 3 original points \(\{p_0,p_2,p_4\}\) and its 2 original lines \(\{\ell_1,\ell_3\}\). Among **remaining original lines**, exactly \(3d-4\) meet exactly one of those deleted original points, and exactly \(V-3d+2\) meet none. No remaining line can meet two of the deleted points: \(p_0,p_2\) already share unique original \(\ell_1\), \(p_2,p_4\) already share unique original \(\ell_3\), and any third \(p_0,p_4\) connecting line would create a forbidden true-original six-cycle. Thus the number of disjoint original line-centered two-edge paths remaining is exactly

\[
R_2=(3d-4)\binom{d-1}{2}
 +(V-3d+2)\binom d2.
\]

Every source B/C six-incidence Q has a unique four-edge path and unique two-edge remainder. Therefore for **all** s=2^h>=2, independently of ANY physical map,

\[
\boxed{U_{B/C}(s)=\frac{Vd(d-1)^3}{2}
\left[(3d-4)\binom{d-1}{2}
 +(V-3d+2)\binom d2\right].}
\]

By true original point↔line GQ duality, the equally exact C/B original source count is

\[
\boxed{U_{C/B}(s)=U_{B/C}(s).}
\]

This is an ALL-h original source combinatorial theorem, not a physical acceptance or deterministic \(S_s(f,g)\) lower.

## 2. New ALL-h exact B/B-overlap source-forest count — three-edge path + three disjoint original incidences

The TRUE ORIGINAL B/B-overlap source pattern has exactly ONE twice-repeated original point and ONE twice-repeated original line, and their unique shared actual original incidence is in Q. The selected source graph is uniquely a **three-edge original point-to-line path**

\[
p_0-\ell_1-p_2-\ell_3
\]

plus THREE isolated (pairwise vertex-disjoint, with path excluded) original incidence edges. Every B/B-overlap selected Q has exactly one distinguished three-edge path; the other three selected original edges form a 3-matching of the **original residual source graph** after deleting the four vertices of that path.

The number of un-oriented point-to-line original three-edge paths is

\[
P_3=Vd(d-1)^2,
\]

with *no division by 2*: the point endpoint and line endpoint have different original types.

### 2.1 Residual true GQ graph after deleting P3

Let \(G'\) be the original source bipartite incidence graph after deleting the two original points \(p_0,p_2\) and two original lines \(\ell_1,\ell_3\) of this P3, together with all their incident edges. GQ girth at least 8, regularity d and unique common-line/point geometry give:

- \(e'=Vd-4d+3\) remaining actual original incidence edges;
- \(A=4d-6\) remaining source vertices of degree \(d-1\), each adjacent to exactly one deleted path vertex;
- \(U=2(V-2d+1)\) remaining source vertices of degree d;
- no residual original edge joins TWO degree-(d−1) vertices: otherwise their two deleted-neighbor edges and the unique original path joining those deleted-neighbors give an original cycle of length between 3 and 6;
- hence exactly \(m=A(d-1)\) mixed low/high-degree actual residual source edges, and exactly \(e'-m\) high/high edges.

Both handshake checks hold exactly: \(A+U=2V-4\) and \(A(d-1)+Ud=2e'\).

### 2.2 Exact three-matching via the residual original LINE graph

The line graph \(L(G')\) has a vertex for each actual remaining original incidence, with two line-graph vertices adjacent iff the corresponding original incidences share an original point or original line. A 3-edge matching in \(G'\) is an independent THREE-vertex subset in \(L(G')\).

Let \(\ell\) be its number of edges (adjacent original-incidence pairs), \(w\) the number of unordered wedges (pairs of line-graph edges sharing a line-graph vertex), and \(t\) the number of line-graph triangles. For a simple graph H with \(e'\) vertices,

\[
i_3(H)=\binom{e'}3-\ell(e'-2)+w-t
\]

by ordinary inclusion-exclusion over the adjacent pairs present in each proposed independent triple. Here every triangle in \(L(G')\) comes from THREE actual original incidences sharing one actual original point/line (the source graph is bipartite, so no physical/original graph triangles). The exact original source values are

\[
\begin{aligned}
\ell &= A\binom{d-1}2+U\binom d2,\\
w &= m\binom{2d-3}2+(e'-m)\binom{2d-2}2,\\
t &= A\binom{d-1}3+U\binom d3.
\end{aligned}
\]

Thus every deleted genuine-original three-edge path has the EXACT same remaining original three-matching capacity

\[
\boxed{
M_3=\binom{e'}3-\ell(e'-2)+w-t.
}
\]

It follows without any all-label independence assumption that

\[
\boxed{
U_{B/B\text{-overlap}}(s)
=Vd(d-1)^2
\left[
\binom{e'}3-\ell(e'-2)+w-t
\right].
}
\]

The count is integer and depends only on the genuine original W(3,s) parameters V,d; not on any physical f,g, not on how the path is embedded in GQ, and not on higher-order original incidence-cycle statistics. It is a **NEW ALL-h SOURCE classification theorem**; it does not assert \(B/B\)-disjoint or other six-forest capacities have been solved.

## 3. Exact W(3,2), W(3,4) true-original independent geometry cross-checks

At s=2,d=3,V=15,N=45 (all actual source incidences):

| All-source object | Genuine W(3,2) exact value | Independent audit |
|---|---:|---|
| Original four-edge point-ended P4 | 180 | actual original GQ path sampling |
| Disjoint line-centered P2 per P4 | 29 | direct remaining original line degree enumeration |
| **Source U_B/C = U_C/B** | **5,220** | AA4-U FULL \(\binom{45}6=8,145,060\) source-sixset census |
| Original point-to-line P3 | 180 | actual original flags |
| Residual incidence edges \(e'\) | 36 | deletion of four actual path vertices |
| Residual lower-degree/high-degree source vertices | 6 / 20 | actual incidence degrees |
| Residual mixed original source edges | 12 | direct actual residual source graph |
| Residual original 3-edge matchings M3 | 5,056 | independently brute-force all \(\binom{36}{3}=7,140\) actual 3-edge subsets |
| **Source U_B/B-overlap** | **910,080** | independent AA4-U full original \(\binom{45}{6}\) source-sixset census |

At s=4, d=5, V=85, N=425:
- Four-edge point-ended original P4 roots: **6,800**; admissible source line-centered P2 per root: **1,572**, giving **U_B/C=U_C/B=10,689,600**;
- Three-edge source P3 roots: **6,800**; true-original residual edge count **408**, lower/high vertex counts **14/152**, lower/high residual incidence-edge count **56**; universal actual source 3-matching count **10,594,688**, giving **U_B/B-overlap=72,043,878,400**.

The actual W(3,4) GQ fixture is used for independent root-specific local original graph deletions, but **NOT** a complete six-source census of \(\binom{425}6\) (infeasible for exhaustive CI). This is explicitly an independent local original-model crosscheck combined with the all-h derivation, not a finite census-to-asymptotic inference.

The strict full original GQ projection/unique-anchor checker is used before all finite original graph tests; a fake degree-3 15+15 regular graph with no forbidden C4 but a six-cycle is rejected. Globally non-injective physical fixture labels are also rejected by the validator; physical labels themselves are not used to establish source-only cardinalities.

## 4. New exact ALL-h full-global uniform selected GF5 C/B and B/B-overlap expectations

Apply the **separately proven AA4-W all-h one-complete-globally-injective-typed-map pattern response**:

\[
p_B=\frac{72K\binom{a-2}{4}}{(K)_5},\qquad
p_C=\frac{(a)_6}{8(K)_3},\qquad
K=\binom a2,\quad a=\min\{b:K\ge V\}.
\]

Draw one independent UNIFORM COMPLETE global point pair-edge injection f and ONE independent UNIFORM COMPLETE global line pair-edge injection g. The maps are **shared over all actual genuine original six-incidence subsets** and nothing is independently resampled per-Q.

For the **selected full seven GF5 C/B tag**, BOTH source orientation B/C and C/B contribute the same selected class under true point/line type duality. For the separately selected **B/B-overlap** tag:

\[
\boxed{\begin{aligned}
\mathbb E_{f,g}N_{C/B}
  &= 2\,U_{B/C}(s)\,p_Bp_C,\\
\mathbb E_{f,g}N_{B/B\text{-overlap}}
  &= U_{B/B\text{-overlap}}(s)\,p_B^2.
\end{aligned}}
\]

Both are exact all-h explicit closed formulas requiring NO other unknown original nine-cell source capacities; this is a strict strengthening of the source-capacity-incomplete full seven ensemble formula from AA4-W. They are NOT lower bounds for every adversarial fixed f,g, and do NOT prove Branch A/B or R3/ASET.

### New asymptotic quantitative full-global ensemble constants

As s=2^h tends to infinity, \(V\sim s^3\), \(d\sim s\), \(a\sim \sqrt2\,s^{3/2}\), \(K\sim s^3\), with precise source cardinality asymptotics

\[
U_{B/C}(s)=\left(\frac14+o(1)\right)s^{12},
\quad
U_{B/B\text{-overlap}}(s)
=\left(\frac16+o(1)\right)s^{18}.
\]

The exact AA4-W response coefficients obey

\[
p_B=(12+o(1))s^{-6},\qquad p_C=1-o(1),
\]

hence the **two independently positive selected GF5 classes** have

\[
\boxed{
\mathbb E_{f,g}N_{C/B}
=(6+o(1))s^6,\quad
\mathbb E_{f,g}N_{B/B\text{-overlap}}
=(24+o(1))s^6.
}
\]

Combined,

\[
\boxed{
\mathbb E_{f,g}\big[N_{C/B}+N_{B/B\text{-overlap}}\big]
=(30+o(1))s^6.
}
\]

This \(\mathbf{30}\) is a **two-tag true-original ensemble first-moment leading constant**. It is NOT a worst-case f,g lower bound, NOT the selected palette GF5 numerator constant, and NOT the full seven-class S leading constant. Other selected sectors still contribute nonnegative additional expectation. The leading terms are proven from the exact all-h integer formulas above and not fitted to finite W32 values.

For the fixed 51-palette certified positive GF5 tag weights, the two-tag corresponding exact weighted mean is

\[
w_{C/B}\,2U_{B/C}p_Bp_C
+w_{B/B\text{-overlap}}\,U_{B/B\text{-overlap}}p_B^2,
\]

with the immutable certified class weights defined upstream in the original GF5 registry. This weight expression is not promoted to a new full R3 or ASET bound.

## 5. Acceptance / scope / next proof obligation

This Draft contains four additive research-only files: independent exact source forest executable, nine original-independent proof/negative tests, this formal mathematical Markdown, and a three-job dedicated GitHub-hosted workflow. One dedicated job exhaustively enumerates ALL true W32 \(\binom{45}6\) six-incidence source IDs via independent AA4-U source oracle, two independent actual GQ jobs inspect W32/W34 local vertex deletion and matching counts and verify exact formulas. Test all powers s=2^h up to 2^18 with exact unbounded integers/Fraction. The W34 audit only samples actual rooted local configurations because the theorem is all-h.

A green CI is evidence of reproducible calculations, **not** independently accepted pure mathematics. Require final exact HEAD dedicated + INDEX + Proof Audit + full Research all green and independent mathematical review before promotion.

**Core root #230 remains unsolved.** Neither the exact U_B/C nor U_BBoverlap **SOURCE** capacity proves that any fixed adversarial global physical f,g accepts ANY of these source Q. The AA4-U nine-cell marginal Fréchet lower is exactly zero on actual globally coherent S68 and S72, even though those real maps have selected GF5-positive non-AA S=68/72; the new exact all-h SOURCE counts do not remove that adversarial intersection obstruction.

**Next AA4-Y:** extend closed-form source capacity to the remaining seven original forest cells if it strengthens the universal GF5 reference, but prioritize **a genuine deterministic physical/source Hall/JPKC–EICE compensated correlation inequality** proving selected non-AA joint acceptance OR connected coincident D6 for EVERY complete globally injected f,g. The novel class-source counts and exact full-global ensemble expectations are controlled baseline invariants for falsification of any claimed minimax lower, not replacements for one.
