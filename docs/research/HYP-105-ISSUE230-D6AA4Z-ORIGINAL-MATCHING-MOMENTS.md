# HYP-105 / issue #230 — AA4-Z-SRC: ALL-h genuine ORIGINAL six-matching source A/A and P2+four-matching source A/B,B/A

**Type:** Research-only exact SOURCE-geometry theorem plus separately scoped full-GLOBAL-map probability corollary. **Stack:** strict child of [AA4-Y-SRC PR #499](https://github.com/definitely-stable/Mathlab/pull/499), pinned parent HEAD \`791f433a4842a964924c6b0f68c7aaf4819e788c\`. The parent dedicated 3/3, INDEX and Proof Audit were successful; its full Research workflow was **CANCELLED**, hence no 4/4 acceptance is claimed. Do not merge, do not close root #230. These results are independent of parallel AA4-Y2 Gram/correlated-swap branch.

**Mathematical literature / novelty accounting.** We specifically **do not claim discovery of the matching-polynomial root moments, Newton recurrence, self-avoiding-walk path tree, nor monomer–dimer cavity equations**. The general underlying tools are prior art, in particular C. D. Godsil, *Matchings and walks in graphs*, Journal of Graph Theory **5** (1981), 285–297, DOI [10.1002/jgt.3190050310](https://doi.org/10.1002/jgt.3190050310); I. M. Wanless, *Counting Matchings and Tree-Like Walks in Regular Graphs*, Combinatorics, Probability and Computing **19** (2010). The present bounded-order specialized contribution is an exact **true-ORIGINAL W(3,2^h) six-incidence A/A and A/B/B/A source-forest enumeration**, a separately implemented genuine-GQ finite graph-agnostic SAW audit, and a precise five-historical-tag GF(5) full-global-uniform reference that does not conflate expectation with a minimax.

## 1. Exact all-h geometry, source types and quantifier discipline

For all h≥1, s=2^h, let V=(s+1)(s²+1), d=s+1, N=Vd. The actual ORIGINAL symplectic generalized quadrangle W(3,s) incidence graph G is a **simple bipartite d-regular graph on 2V vertices, with exactly N ACTUAL original point–line incidence edges and girth 8**. Every Q is a set of six DIFFERENT actual original incidence IDs, selected before any physical pair-edge map.

- SOURCE **A/A** means all six original point endpoints are distinct AND all six original line endpoints are distinct; the Q-source graph is a six-edge matching in G.
- SOURCE **A/B** means six distinct original points but five original lines, exactly one occurring twice. The Q-source forest consists of a UNIQUE original two-edge path P–L–P (the doubled original line) and FOUR pairwise vertex-disjoint additional single original incidence edges, also avoiding all P–L–P source vertices. The dual SOURCE B/A uses point-line reversal.
- These source classes are NOT themselves physical A/B/C half acceptances: arbitrary globally injected f,g may reject all particular Q or align differently. The all-h positive physical claims below are strictly TWO complete uniform global maps and are only expectations.

## 2. A/A: universal low-order regular SOURCE matching-polynomial moments

Write \(m_k(G)\) for the number of k-edge source graph matchings and \(Z_G(z)=\sum_{k\ge0}m_k(G)z^k\) the monomer–dimer matching generating function. Define the traditional matching polynomial \(\mu_G(x)=x^{2V}Z_G(-x^{-2})\), which is real-rooted (Heilmann–Lieb). The root power sums at even orders obey Godsil's path-tree formula:

\[
p_j(G):=\sum_{\lambda:\mu_G(\lambda)=0}\lambda^{2j}
=\sum_{v\in V(G)}w_{2j}(T(G,v),v),
\]

where \(T(G,v)\) is the tree of actual-original **self-avoiding source paths rooted at v**, and \(w_{2j}\) counts its root-returning walks of length 2j. (This follows from \(\mu_{G-v}/\mu_G\) equalling the rooted path-tree diagonal resolvent and \(\mu_G'=\sum_v\mu_{G-v}\).)

A root-returning walk of length \(2j\) on a tree cannot rise beyond depth j. For every j≤6, the original girth at least 8 means that at every required SAW-path-tree source node of depth up to 5, its forward branch count is exactly d−1: otherwise an original source 6-cycle or shorter would exist. The root has exactly d neighbors. Therefore every such original source path tree has, **up to return-walk length 12**, the same root moments as the infinite d-regular tree. Let \(M_j(d)\) be the latter 2j-step root-returning closed-walk count. It can be computed with exact integers by a Dyck-height recurrence:

\[
F_0(0)=1,\quad
F_{t+1}(h+1)\mathrel{+}=
\begin{cases}
d\,F_t(0),&h=0,\\
(d-1)\,F_t(h),&h>0,
\end{cases}
\qquad
F_{t+1}(h-1)\mathrel{+}=F_t(h)\ (h>0),
\quad M_j(d)=F_{2j}(0).
\]

For j=1,...,6, \(p_j(G)=2V\,M_j(d)\). The ordinary matching coefficients follow from **Newton's exact identity** (no spectral numerical approximation):

\[
\boxed{
m_0=1,\qquad
2k\,m_k=\sum_{j=1}^k(-1)^{j+1}\,2V\,M_j(d)\,m_{k-j},
\qquad k=1,\ldots,6.
}
\]

Hence the SOURCE A/A original six-Q population has the complete closed finite universal recurrence

\[
\boxed{U_{A/A}(s)=m_6(W(3,s))}.
\]

This is exact for **every** h≥1, involves only integers and d,V, and is independent of f,g. For W(3,2), d=3,V=15:

\[
(M_1,\ldots,M_6)=(3,15,87,543,3543,23823),
\quad(m_0,\ldots,m_6)=(1,45,900,10560,80820,424404,\mathbf{1566360}).
\]

For the true W(3,4), d=5,V=85:

\[
(m_0,\ldots,m_6)=(1,425,88400,11995200,1194216000,
93020741440,\mathbf{5903320937600}).
\]

Note the **mathematical provenance**: this is an explicit specialized application of established Godsil/Wanless matching-moment tools, NOT a newly invented matching-polynomial theorem.

## 3. A/B and B/A: a true original rooted P2 cavity identity

Fix an actual ORIGINAL line-centered two-edge path \(S=p_1-\ell-p_2\), where p1,p2 are two different original neighbors of actual original line \(\ell\). Exactly

\[
R_2=V\binom d2
\]

different such un-oriented genuine ORIGINAL P2 exist. For each S, its four remaining isolated original incidence edges Q are an independent **four-edge matching** in \(G-V(S)\), the actual source incidence graph after removing all THREE original source vertices p1,\ell,p2. Thus

\[
U_{A/B}(s)=V\binom d2\,m_4(G-V(S)).
\]

The subtlety is that \(G-V(S)\) is NOT d-regular; blindly applying the full-graph regular-tree moment formula would be **incorrect**. We instead calculate the exact local rooted source monomer ratio through formal degree four.

For finite original matching partition function \(Z_G(z)\), let \(R_S(z):=Z_{G-V(S)}(z)/Z_G(z)\), the exact generating-function ratio for forcing these three actual source vertices to be unmatched. The d-regular tree cavity formal series \(x(z)\) and root-monomer series \(y(z)\) satisfy

\[
x=\frac1{1+(d-1)zx},\qquad
y=\frac1{1+dzx},\qquad x(0)=y(0)=1.
\]

For an actual **three-vertex connected star** S consisting of a source line and its two actual neighbor points, the corresponding infinite source regular-tree joint monomer probability is \(y\,x^2\): after requiring the source line unmatched, its two distinct point-branch monomer events have cavity factor x each. The true-original source GQ graph has girth eight, so any alternative path joining S endpoints outside S has length at least six; any correction to the joint-monomer cavity in its **formal coefficients through z⁴** would need a shorter source loop or an endpoint-connecting path. Hence, as an exact identity of finite formal power series (no all-order Bethe or independence assumption),

\[
\boxed{
R_S(z)\equiv y(z)x(z)^2\pmod{z^5}.
}
\]

This is only a low-order source-geometry identity, not a statement that a finite generalized quadrangle's entire partition function equals its infinite-cover Bethe approximation.

The formal coefficient of x has the exact signed Catalan form

\[
[z^j]x(z)=(-1)^j(d-1)^j\,\frac1{j+1}\binom{2j}{j},
\]

and y is obtained recursively by \(y_0=1\), \(y_j=-d\sum_{i=0}^{j-1}x_i y_{j-1-i}\). Let \(\rho_j=[z^j]y x^2\), j=0,...,4. Then

\[
\boxed{\begin{aligned}
m_4(G-V(S)) &= \sum_{j=0}^4 m_{4-j}(G)\rho_j,\\
U_{A/B}(s)&=V\binom d2\,\sum_{j=0}^4m_{4-j}(G)\rho_j,\\
U_{B/A}(s)&=U_{A/B}(s).
\end{aligned}}
\]

All quantities on the right are exact finite integer recurrences and all-h GQ parameters. For W(3,2), \((\rho_0,\ldots,\rho_4)=(1,-7,47,-319,2199)\), \(m_4(G-V(S))=\mathbf{37044}\), \(V\binom d2=45\), so

\[
\boxed{U_{A/B}(2)=U_{B/A}(2)=45\cdot37044=1666980},
\]

exactly the independent AA4-U *complete* original \(\binom{45}{6}=8,145,060\) source-census number. W(3,4) exact actual original values:

\[
m_4(G-V(S))=\mathbf{1051982912},
\quad V\binom d2=850,\quad
\boxed{U_{A/B}(4)=U_{B/A}(4)=894185475200}.
\]

### Independent graph-agnostic finite proof oracle

Our finite audit does **not** merely recalculate the symbolic all-h regular-tree formula twice. It builds the actual ORIGINAL W(3,s) point-line incidence graph, confirms full GQ nonincident point-line unique-anchor axiom, and independently implements Godsil's finite **self-avoiding-path-tree resolvent** for EACH actual root source vertex, with its ACTUAL excluded original vertices and its ACTUAL irregular degree after deleting S.

For a finite ACTUAL source adjacency G', each actual SAW path \(\pi\) has exact path-tree diagonal rooted Green's formal series

\[
H_\pi(z)=\frac{1}{1-z\sum_{w\in N(\mathrm{last}(\pi))\setminus V(\pi)}
H_{\pi w}(z)}.
\]

The independent algorithm truncates H to z^k, sums \([z^j]H_{(v)}\) across ALL original point/line source vertices, and applies the same **exact Newton matching-polynomial coefficient identity** on the ACTUAL source graph (without imposing d-regularity). Thus it computes:
- all m0..m6 on the full actual W(3,2) and W(3,4) source incidence graphs,
- m0..m4 separately on several actual NONREGULAR residual source graphs after deleting a rooted ORIGINAL P2, with actual source factor names retained.

The equality against the all-h regular-tree+cavity recurrences is a substantive independent model-level crosscheck. No complete \(\binom{425}6\) W(3,4) six-Q enumeration is performed or claimed. In true original W(3,2), the parent AA4-U separately exhausted every real source six-incidence Q, so there is also a completely distinct finite enumeration check.

Fake 15+15 degree-three graphs with forbidden original source 6-cycles and non-injectively labeled global physical models are REJECTED by the GQ projection gate. The source-only counts never infer that any particular pair f,g physically accepts all these source Q.

## 4. Five of seven selected ORIGINAL seven-GF5 ensemble classes are now exact all-h

Independently established AA4-W source-physical response for uniform **one complete global** point injection f and uniform **one independent complete global** line injection g, shared over all actual original Q, is

\[
p_H=\frac{(a)_6}{(K)_6},\quad
p_A=70p_H,\quad
p_B=\frac{72K\binom{a-2}{4}}{(K)_5},\quad
K=\binom a2\ge V.
\]

Use the new exact SOURCE A/A and A/B/B/A populations to obtain the two new exact full-global-uniform selected historical sector expectations:

\[
\boxed{\begin{aligned}
\mathbb E_{f,g}N_{D6}&=60\,U_{A/A}(s)\,p_H^2,\\
\mathbb E_{f,g}\big[N_{A/B}+N_{B/A}\big]
&=2\,U_{A/B}(s)\,p_Ap_B.
\end{aligned}}
\]

The first factor 60 counts the sixty connected original six-column positional cycle H templates, NOT 70 (the other ten physically A/A two-triangle templates are unaccepted D6). The one-sided A/B cells have two distinct historical accepted GF5 tags and both must be retained separately when applying their distinct fixed certified palette weights. The expression above groups their **unweighted counts only**, not their weighted 51-palette numerator.

The previous exact all-h source formulas from AA4-X-SRC and AA4-Y-SRC already established the three OTHER pooled positive historical GF5 tags \(C/A,C/B,B/B\text{-overlap}\). Thus we now have the **exact expectation of FIVE of the SEVEN accepted ORIGINAL GF5 tags** for every order s.

With \(a\sim\sqrt2\,s^{3/2}\), \(K\sim s^3\), the exact source recurrences give

\[
U_{A/A}(s)=\left(\frac1{720}+o(1)\right)s^{24},
\quad
U_{A/B}(s)=U_{B/A}(s)
=\left(\frac1{48}+o(1)\right)s^{21},
\]

while \(p_H=(8+o(1))s^{-9}\), \(p_A=(560+o(1))s^{-9}\), \(p_B=(12+o(1))s^{-6}\). Therefore

\[
\boxed{\begin{aligned}
\mathbb E_{f,g}N_{D6}&=\left(\frac{16}{3}+o(1)\right)s^6,\\
\mathbb E_{f,g}(N_{A/B}+N_{B/A})&=(280+o(1))s^6.
\end{aligned}}
\]

Add the previously established pooled three-tag \((160/3+o(1))s^6\):

\[
\boxed{
\mathbb E_{f,g}[N_{D6}+N_{A/B}+N_{B/A}+N_{C/A}+N_{C/B}+N_{BB,o}]
=\left(\frac{1016}{3}+o(1)\right)s^6.
}
\]

**Class/sector naming:** here the two A/B and B/A historical classes are distinct, while C/A, C/B each pool both mirrored SOURCE orientations. The above display names SIX entries syntactically; there are in fact **six historical accepted GF5 tags**, namely D6, A-left/B-right, B-left/A-right, C/A, C/B, and B/B-overlap; the sole unfinished historical tag is B/B-disjoint. Accordingly, this is **SIX of SEVEN** historical tags, NOT five. The Python oracle and PR must report "SIX" consistently. The mathematical sum remains 1016/3 and is not affected by that naming correction.

TRUE W(3,2) exact selected mean checks against the independent AA4-W FULL seven-tag source enumeration:

\[
\begin{aligned}
\mathbb E_{f,g}N_{D6}&=\frac{3759264}{1002001},\\
\mathbb E_{f,g}(N_{A/B}+N_{B/A})&=\frac{2857680}{20449}.
\end{aligned}
\]

TRUE W(3,4) examples:
\[
\mathbb E_{f,g}N_{D6}=\frac{88549814064000}{12317226289},\qquad
\mathbb E_{f,g}(N_{A/B}+N_{B/A})=\frac{93889474896000}{286447123}.
\]

**The sole remaining original source forest cell now without an all-h closed count is B/B-disjoint.** The true W32 finite full source census established its cardinality 707,580, but no uniform all-h formula is asserted here.

### Scientific boundary (essential)

Every expectation is for TWO **uniform COMPLETE globally injected** maps, f and g, independent by original factor type but each used identically for EVERY true original Q; no per-Q random physical independent projection is ever used. This proves no positive \(\min_{f,g}\) and does not discharge deterministic Branch A, infinite adversarial Branch B, the full R3 exponent or ASET.

Positive ensemble \(\Omega(s^6)\) follows even for one accepted D6 from older AA4-R-CYC. The scientific value of AA4-Z is quantitative source bookkeeping and exact baseline, **not a stronger adversarial theorem**. Do not confuse generic prior-art matching-polynomial technology with a genuinely new fundamental theorem.

## 5. Acceptance, integration and next AA4-AA

Dedicated 3 GitHub-hosted jobs include ten independently designed all-h tests, exact W32 full source sixset comparison against AA4-U, full actual real W32/W34 finite SAW root matching polynomial m0..m6, actual source P2-deleted nonregular SAW m0..m4 for several real rooted configurations, source GF5 weighted/original full ensemble independent AA4-W crosschecks, negative counterfeit GQ and full-global-injection failures. Third-party math review remains necessary after final exact-HEAD dedicated/INDEX/Proof Audit/FULL Research pass.

Four additive-only files: this proof, the all-h source proof/oracle, 10 tests, dedicated three-job hosted workflow. No edits to inherited code, main, unrelated cyclic stack or RCP's generated permanent Markdown. The parent AA4-Y-SRC FULL Research was cancelled, not green; its rerun/reacceptance is an explicit stack prerequisite.

**Next AA4-AA-SRC:** derive the missing B/B-disjoint original source count: TWO distinct disjoint source P2 paths (one original point-rooted, one original line-rooted) + TWO isolated genuine-original incidence edges. Classify joint P2 position/distance/blocked neighborhoods in actual GQ and compute m2 of the residual source graph, or use an independently proven low-order path-forest graph invariant. Once this is complete, obtain all nine source-cell capacities and the exact full seven-GF5 selected expectation for all h. Still prioritize independently the **adversarial** source/physical JPKC/EICE positional compensation problem; source-only ensemble identities are not its solution.
