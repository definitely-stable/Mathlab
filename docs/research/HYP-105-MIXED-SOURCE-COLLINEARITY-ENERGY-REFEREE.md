# HYP-105 / #230 — AA4-MIXENERGY: exact ORIGINAL collinearity energy and sharper mixed FULL/CORE blocker

**Scientific Draft**, stacked STRICTLY on frozen [#700](https://github.com/definitely-stable/Mathlab/pull/700), exact parent HEAD \`6104e2ba5df8df230d6277a36d9060dde4c78ff6\`. New mathematical input: an exact **source book / spectral energy anti-correlation identity** for the first squared factor of the original mixed FULL/CORE source blocking count, leading to an all-h first-factor improvement from historical \(64s^{11/2}\) to \(7s^{11/2}\) and a safe original blocker-mass coefficient improvement \(64\to15\). The underlying global original point/line flag maps remain COMPLETE, separately globally pair-injective and arbitrarily correlated, with no remapping, random completion or artificial source IDs. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. No parent/main modifications, merges or newly accepted ASET theorem.

## 1. Precise frontier: audit (13)–(18), not an unproved new exponent

The historical #672/#685 mixed left internal-blocker witness is an ORIGINAL physical CORE first edge \((x,y)\to(k,y_1)\) sourced by an actual core flag with original point factor \(u=f^{-1}\{x,k\}\), together with original FULL source GQ projection \(q-\ell-p-r\) where \(q\in S_x\), \(p\in S_k\), \(q\) and p are ORIGINAL distinct collinear points, and the appropriate full original line r through p carries physical right coordinate y. The FULL anchors are not required to belong to CORE.

Write \(V=(s+1)(s^2+1)\), \(d=s+1\), \(S_x=\{p:x\in f(p)\}\) for the ORIGINAL source point stars of fixed f, \(C_P\) the ORIGINAL point-collinearity adjacency matrix, \(R(p,y)=\#\{\ell\ni p:y\in g(\ell)\}\) the FULL genuine right pencil array, and \(R_0(u,y)\) its core-only restriction. Define \(K_{pu}=\sum_y R(p,y)R_0(u,y)\). The historical original all-h first factor is

\[
F_1=\sum_{u\in{\rm ORIGINAL\,points}}
\sum_{(x,k)\in\overrightarrow{f(u)}}
\sum_{p\in S_k}
\big[(C_P\mathbf1_{S_x})(p)\big]^2.
\tag{M1}
\]

The second factor and mixed source superset mass are

\[
F_2=\sum_u\sum_{(x,k)\in\overrightarrow{f(u)}}\sum_{p\in S_k}K_{pu}^2,
\qquad
\Phi=\sum_u\sum_{(x,k)\in\overrightarrow{f(u)}}\sum_{p\in S_k}
(C_P\mathbf1_{S_x})(p)K_{pu}.
\tag{M2}
\]

These are actual SOURCE-PENCIL quantities on genuine original points and original flag IDs, not a graph with independently sampled physical edges. Cauchy is exact in this space: \(\Phi^2\le F_1F_2\). The historical source-first enumerator also gives \(|T_{\mathrm{blocker}}|=\Phi-\Psi\le\Phi\) where \(\Psi\) is the original incidence endpoint defect. It must NOT be assumed equal to \(\Phi\) without subtracting \(\Psi\).

## 2. NEW exact all-h original-GQ collinearity energy identity

By the true ORIGINAL symplectic generalized-quadrangle axioms already independently derived from source incidence in #698, for EVERY dyadic \(s\ge2\)

\[
\boxed{C_P^2=(s^2-1)I-2C_P+(s+1)J.}\tag{M3}
\]

For each physical coordinate x, let \(\mathbf v_x=\mathbf1_{S_x}\), \(k_x=|S_x|\). Multiply (M3) on both sides by \(\mathbf v_x^\top,\mathbf v_x\), and sum over x:

\[
\begin{aligned}
\Gamma_f
&:=\sum_x\|C_P\mathbf1_{S_x}\|_2^2\\
&=(s^2-1)\sum_x k_x
  -2\sum_x\mathbf v_x^\top C_P\mathbf v_x
  +(s+1)\sum_x k_x^2.
\end{aligned}
\]

Global distinct pair-label injection gives \(\sum_x k_x=2V\). Moreover \(\sum_x\mathbf v_x^\top C_P\mathbf v_x=2M_f\): every unordered pair of distinct ORIGINAL collinear points p,q occurs on EXACTLY ONE source line and their two distinct physical f-pairs share at most ONE coordinate. The full ORIGINAL line-pencil collision book \(M_f=\sum_{\ell,x}\binom{R_f(\ell,x)}2\) counts precisely these incidences. Consequently, with no independence assumptions,

\[
\boxed{
\Gamma_f=
2V(s^2-1)-4M_f+(s+1)\sum_x k_x^2.
}\tag{M4}
\]

This is an **equality for EVERY original f, regardless of g and any retained CORE**. It yields a genuinely new structural constraint: **for fixed physical coordinate-star sizes** \(k_x\), increasing the full ORIGINAL point collision book \(M_f\) by \(\Delta M_f\) reduces \(\Gamma_f\) by EXACTLY \(4\Delta M_f\). The previous mixed blocker proof bounded the collinearity energy and the books separately, overlooking this anti-correlation. This statement concerns \(M_f\), not \(M_g\), and does NOT imply that the actual mixed blocker mass \(\Phi\) itself necessarily decreases when f changes, because the CORE, support weights, and K may also change.

There is an additional exact nonnegative **index restriction defect**. Let

\[
w_{xp}=\#\{k\in f(p)\setminus\{x\}:\{x,k\}\in f({\rm ORIGINAL\ points})\}\in\{0,1,2\}.
\]

By the unique occupied source pair lookup, the sum in (M1) is exactly

\[
F_1=\sum_{x,p}w_{xp}\big[(C_P\mathbf1_{S_x})(p)\big]^2,\quad
0\le2\Gamma_f-F_1.
\tag{M5}
\]

The ceiling is **pointwise 2** for all f and follows without requiring CORE flags or FULL anchors to be retained. This is independent of the genuine right map g.

## 3. NEW all-h explicit universal envelope \(F_1\le7s^{11/2}\)

The legal minimal typed pair alphabet satisfies \(a\le(97/64)s\sqrt s\) for EVERY dyadic \(s\ge64\), independently proved for true ORIGINAL factor cardinality \(V\) in #690/#697. Also for \(s\ge64\), with \(\rho=(65/64)(4097/4096)\),

\[
V\le\rho s^3,\quad d=s+1\le(65/64)s,\quad
\sum_x k_x^2\le(a-1)\sum_xk_x=2V(a-1).
\]

Dropping only the two TRUE nonnegative quantities \(M_f\ge0\) and the source index restriction defect \(2\Gamma_f-F_1\ge0\), (M4)–(M5) give

\[
\begin{aligned}
F_1
&\le2\Gamma_f\\
&=4V(s^2-1)-8M_f+2d\sum_xk_x^2\\
&\le4V(s^2-1)+4dV(a-1)\\
&\le
\left[
\frac{4\rho}{8}+
4\frac{65}{64}\rho\frac{97}{64}
\right]s^{11/2}\\
&=\boxed{C_Es^{11/2}},\qquad
C_E=\frac{4\rho}{8}
+4\frac{65}{64}\rho\frac{97}{64}
<7.
\end{aligned}\tag{M6}
\]

This is **all-h exact rational arithmetic**, not a fit to W(3,2) or W(3,4). It strictly improves the historical coefficient \(64s^{11/2}\) by more than a factor of nine while preserving the SAME original-source FULL/CORE mixed witness set, fixed f,g and original K cap.

The old second factor is not silently altered:

\[
F_2\le K_{\max}\sum_{k,y}D_{\rm full}(k,y)D_{\rm core}(k,y)
\le 8d(K+1)N\Delta
\le32(K+1)T s^6.
\tag{M7}
\]

Indeed \(K_{pu}\le 2d(K+1)\) since each core pencil population is bounded by the ORIGINAL conflict graph CORE degree \(K\), and the EXACT unsquared tensor identity is

\[
\sum_u\sum_{(x,k)\in\overrightarrow{f(u)}}\sum_{p\in S_k}K_{pu}
=\sum_{k,y}D_{\rm full}(k,y)D_{\rm core}(k,y),
\tag{M8}
\]

with FULL degree sum \(4N\), core maximum physical degree \(\Delta\le Ts\). The finite referee independently computes both sides from the ACTUAL original source and physical corners.

By (M1)–(M8) and \(\Psi\ge0\), the historical candidate original blocker triple set obeys

\[
\boxed{
B=|T_{\rm blocker}|=\Phi-\Psi
\le\sqrt{224(K+1)T}\,s^{23/4}
\le15\sqrt{(K+1)T}\,s^{23/4}.
}\tag{M9}
\]

Compare historical \(B\le64\sqrt{(K+1)T}s^{23/4}\), which remains valid but substantially weaker. This new explicit improvement is proven for all allowed original s and all fixed correlated maps **conditional only on the SAME antecedent core caps \(K,T\)** as #672. It does not require new randomness.

The existing physical fourth-moment bound \(\operatorname{tr}(A_0^4)\le L_4s^5\) and \(\Delta\le Ts\) are unchanged. Hence the four-position internal-blocking error improves from historical

\[
4\sqrt{64\sqrt{(K+1)T}\ T L_4}\ s^{47/8}
\quad\text{to}\quad
\boxed{
4\sqrt{15\sqrt{(K+1)T}\ T L_4}\ s^{47/8}.
}\tag{M10}
\]

The multiplicative coefficient is \(\sqrt{15/64}\) of the previous one, about 0.484. **The exponent remains \(47/8\)**. Neither this proof nor the test suite claims a uniform exponent gain, a new ASET exponent, a finite exact h0, or complete original Branch A acceptance.

## 4. Independent true-original finite adversarial referee

The new standalone \`research/hyp105_mixed_source_collinearity_energy_referee.py\` imports **only** genuine ORIGINAL W32/W34 source generation. It does NOT import prior #685 weighted blocker, #693 cellwise, #698 spectral projectors or #672 root code. It independently:

1. Reconstructs all actual ORIGINAL point and line pencils, the ORIGINAL point-collinearity graph and checks EVERY ordered original point pair against the GQ strong-regular A² identity;
2. Builds actual original coordinate point-star sets \(S_x\) from fixed f and the entire exact \((C_P1_{S_x})(p)\) table, computes \(\Gamma_f\) directly, FULL original line-pencil collision book \(M_f\) independently by pencil binomials and point-pair-major overlaps, and demands exact equality (M4);
3. Computes the entire source-index restricted mixed first factor \(F_1\) and EXACT index defect \(2\Gamma_f-F_1\), the full original \(R\) and actual selected-core-only \(R_0\), the mixed \(K_{pu}\) and its exact \(F_2,\Phi\), then independently checks \(\Phi^2\le F_1F_2\);
4. Checks the ENTIRE source-first original nonincident blocker triple set by looping ACTUAL CORE original first-edge IDs (and both real diagonal orientations), genuine source collinear q,p and FULL source r through p. It computes the incident defect \(\Psi\) directly and checks \(\Phi-\Psi=\#\)distinct original nonincident triples;
5. Builds the ACTUAL physical paired-diagonal CORE graph and independently computes all its corner degrees, verifies the exact FULL/CORE degree product (M8), \(\sum D_{\rm full}=4N\), \(\sum D_{\rm core}=4|I|\), \(K_{\max}\le2d\,\max R_0\), \(F_2\le K_{\max}\sum K\); FULL source factors are **not** incorrectly pruned to the CORE.
6. Tests multiple complete separately injective but fixed correlated W32 and W34 f/g maps, including full, sparse, empty CORE, protected true ORIGINAL W34 16-ID K4,4 control. A test independently compares original \(\Phi,\Psi,\#T\) to the PREVIOUS #685 referee while keeping the new implementation source-independent. Multiple W32 complete reassignments of f with identical star size vector independently exercise the STRICT \(-4M_f\) anti-correlation.
7. Symbolically checks the all-h exact rational coefficient \(C_E<7\) for dyadic \(s=2^6,\ldots,2^{27}\) (without inventing geometric finite sources at huge h) and fails closed invalid original IDs, noncomplete factor maps and nondyadic s.

The **mathematical all-h proof** is Sections 2–3; finite W32/W34 tests are falsifiers, not evidence-based generalization. All original source-point/line ID labels remain fixed, no cloning or source replacement.

**Scientific acceptance:** #230 remains OPEN_WITH_FORMAL_BLOCKER pending a qualified independent human referee of the ENTIRE source heavy/dense chain and the cited ordinary simple C6 theorem. This slice strengthens the real FULL/CORE squared factor and sharpens the internal blocker coefficient; it neither establishes the full Branch A by itself nor changes the published existential graph constants or the GF5 target exponent. Keep all scientific PRs Draft/unmerged; no main/ancestor changes. The next highest-value task is to independently audit a remaining nontrivial all-h original dense-core implication, rather than repeatedly changing the same scalar constants.