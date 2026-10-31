# HYP-105 / #230 — AA4-B2INT: exact improper two-walk intersection, tighter core fourth moment and proper three-path bound

**New independently derived all-\(h\) combinatorial improvement**, stacked on [scientific Draft #680](https://github.com/definitely-stable/Mathlab/pull/680) with fixed original source W(3,2^h) and *arbitrary complete, separately globally injected, arbitrarily correlated* source point and line pair maps f,g. No source random completion, no synthetic GQ; original six-incidence IDs are unchanged. This is a local source/physical moment refinement, **not** a new independent proof or external acceptance of root Branch A in [#672](https://github.com/definitely-stable/Mathlab/pull/672). Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Exact all-h local graph identity, NO source probability

Let H0 be ANY simple physical graph on the typed coordinate grid \([a]\times[a]\), with every edge changing BOTH physical coordinates (automatic for every genuine original flag diagonal). Let \(A_0\) denote its symmetric adjacency, \(m_0\) its number of physical edges, \(\Delta\) its maximum degree. For every ordered endpoints \((u,v)\), split the two-walk population:
\[
(A_0^2)_{uv}=P_2(u,v)+B_2(u,v),
\]
where \(P_2\) counts coordinate-proper two-walks with three pairwise distinct left coordinates and three pairwise distinct right coordinates; \(B_2\) counts two-walks where the initial and terminal vertices share a LEFT OR a RIGHT coordinate.

Write
\[
Q_x=\sum_{u,v:\ u_x=v_x}(A_0^2)_{uv},\quad
Q_y=\sum_{u,v:\ u_y=v_y}(A_0^2)_{uv}.
\]
**Crucial inclusion–exclusion missing from the conservative #672 bound**: a two-walk that returns to BOTH coordinates has \(u=v\), i.e. it is an actual backtrack \(u\to w\to u\). There are precisely \(\sum_u\deg(u)=2m_0\) such oriented two-walks, with multiplicity as actual walks. Therefore for EVERY physical grid graph,
\[
\boxed{
 \sum_{u,v} B_2(u,v)
 =Q_x+Q_y-2m_0.
}\tag{B2INT-EXACT}
\]
This is a true equality; \(Q_x+Q_y\) alone double-counts every diagonal backtrack. No bipartiteness or source geometry is required.

## 2. EXACT original W(3,s) flag-count formula

Let the core I contain \(N_0\) **genuine distinct ORIGINAL flag IDs** \((p,\ell)\). Every retained original flag contributes BOTH physical diagonals, with distinct edge ownership under globally injected f,g, hence
\[
 m_0=2N_0,\qquad 2m_0=4N_0.
\]
Let
\[
 R_0(p,y)=\#\{\ell:(p,\ell)\in I,\ y\in g(\ell)\},\quad
 \widetilde R_0(\ell,x)
 =\#\{p:(p,\ell)\in I,\ x\in f(p)\}.
\]
For the original-source pencil books:
\[
 M_g(I)=\sum_{p,y}\binom{R_0(p,y)}2,\quad
 M_f(I)=\sum_{\ell,x}\binom{\widetilde R_0(\ell,x)}2.
\]
A direct count of two-step coordinate returns gives the already known exact formulas
\[
 Q_x=2\sum_{p,y}R_0(p,y)^2
 =4N_0+4M_g(I),\quad
 Q_y=2\sum_{\ell,x}\widetilde R_0(\ell,x)^2
 =4N_0+4M_f(I).
\]
The factor two in each formula counts both diagonals of every ORIGINAL retained flag. These are full original source-to-physical identities, not estimates.

Combining them with (B2INT-EXACT):
\[
\boxed{
 \sum_{u,v}B_2(u,v)
 =4N_0+4[M_f(I)+M_g(I)].
}\tag{B2INT-SOURCE}
\]
This is independently derivable directly from the original-incidence books without constructing the physical graph, and independently from the physical two-walk population without source books.

## 3. NEW uniformly stronger original-core fourth-moment transfer

Every entry of \(B_2\), being a subcount of \((A_0^2)_{uv}\), is at most \(\Delta\), the graph maximum degree (each two-walk interior vertex must be a common neighbor of its endpoints). Thus
\[
 \|B_2\|_F^2
 \le\Delta\sum_{u,v}B_2(u,v)
 =4\Delta[N_0+M_f(I)+M_g(I)].
\]
By the elementary squared triangle inequality:
\[
\begin{aligned}
 \operatorname{tr}(A_0^4)=\|A_0^2\|_F^2
 &=\|P_2+B_2\|_F^2\\
 &\le2\|P_2\|_F^2+2\|B_2\|_F^2\\
 &\le2\|P_2\|_F^2+8\Delta[N_0+M_f(I)+M_g(I)].
\end{aligned}
\tag{B2INT-FOURTH}
\]

From the **same established original-source #672** bounds for \(s\ge64\),
\[
 N_0\le N\le2s^4,\quad M_f(I)+M_g(I)\le2C_s\le3s^4,
 \quad \Delta\le Ts.
\]
Hence
\[
 \boxed{
 \operatorname{tr}(A_0^4)
 \le2\|P_2\|_F^2+40Ts^5.
 }\tag{B2INT-L4}
\]
The previous #672 coefficient was **56T**, because it bounded \(\sum B_2\) by \(Q_x+Q_y\), treating the entire diagonal intersection twice. The new 40T is a strict improvement without modifying f,g, the core, or any selector hypothesis. Combining independently verified #679 selector \(\sigma_2^{\rm new}\) and #680 sixth moment \(L_6^{\rm new}\) yields a strictly improved all-h chosen-core fourth-moment envelope
\[
 \boxed{
 L_4^{\rm new}
 =2(\sigma_2^{\rm new})^{-2}\sqrt{8L_6^{\rm new}}+40T.
 }\tag{B2INT-L4-NEW}
\]
Its **order remains \(O(s^5)\)**. The original #672 formula with its conservative parameters remains valid unchanged; no unreviewed downstream constants are silently patched.

## 4. NEW smaller exceptional/improper three-walk loss

Count actual **directed** length-three walks \(v_0v_1v_2v_3\) of the same uncut original core H0. Since every edge changes BOTH coordinates, coordinate properness fails precisely when either:

1. the initial two-step subwalk \(v_0v_1v_2\) is in the improper \(B_2\) population;
2. the terminal two-step subwalk \(v_1v_2v_3\) is in \(B_2\);
3. the FIRST and LAST physical vertices share a first coordinate or a second coordinate (distance-three coordinate return).

There are at most \(\Delta \sum B_2\) walks in each of cases 1 and 2: extend one fixed oriented two-walk by at most \(\Delta\) neighboring vertices. For case 3, the original exact row-vector contraction from #672 gives
\[
 \sum_x {\bf1}_x^TA_0^3{\bf1}_x
 =\sum_x(A_0{\bf1}_x)^TA_0(A_0{\bf1}_x)
 \le\Delta\sum_x\|A_0{\bf1}_x\|^2=\Delta Q_x
\]
and the true line/right physical coordinate dual gives \(\le\Delta Q_y\). A union bound yields the **new all-h** inequality
\[
\begin{aligned}
 \#\{\text{improper directed three-walks}\}
 &\le2\Delta\sum B_2+\Delta(Q_x+Q_y)\\
 &=\Delta[16N_0+12(M_f(I)+M_g(I))]\\
 &\le68Ts^5.
\end{aligned}
\tag{B2INT-P3-BAD}
\]
The previous #672 estimate was \(84Ts^5\). The new bound subtracts the **same exact two-step intersection** in both length-two locations and uses no claim of independence of path events.

The #672 ordinary three-walk lower bound from the same core, \( {\bf1}^TA_0^3{\bf1}\ge s^6/2\), is unchanged. Therefore:
\[
\boxed{
 \sum_{u,v}P_3(u,v)\ge\frac{s^6}{2}-68Ts^5,
}\tag{B2INT-P3-NEW}
\]
replacing \(\frac{s^6}2-84Ts^5\). **The leading sextic coefficient 1/2 and all asymptotic exponents remain unchanged.** We do not extrapolate this large-h lower bound to W32/W34 (whose s are far below the parent's very large sufficient threshold).

## 5. Independent original-source/physical falsifiers

New \`research/hyp105_improper_path_intersection.py\` contains two mathematically independent algorithms:
- physical-grid-first: directly enumerate EVERY two-step walk in an input graph to construct exact \(A_0^2,P_2,B_2,Q_x,Q_y\), all their squared norms and \(P_2\)-\(B_2\) cross term; directly enumerate every three-walk and classify distance-two and distance-three coordinate returns; independently test the new improved P3 upper; reject an asymmetric edge list, self-loop or a physical edge that leaves one coordinate unchanged;
- ORIGINAL-source-first: construct actual \(W(3,2)\) or \(W(3,4)\) genuine ORIGINAL flag-ID source R0 and its line-dual, compute \(M_f(I),M_g(I)\), \(Q_x,Q_y\) from the source pencils WITHOUT the physical walker, then independently build the paired-diagonal physical graph and check exact equality in every case. The original core may be full, empty or sparse, with any legal complete, globally injected and mutually correlated pair assignments f,g. The algorithm does NOT call #672's cached source certificate or fixture reference values.

New \`research/test_hyp105_improper_path_intersection.py\` enumerates **all 4096 simple coordinate-changing physical graphs on a 2×4 physical grid**, checking exact P2/B2 accounting and all three-walks by direct traversal, and genuine W32 original source with five globally reallocated right maps, full/empty/sparse cores and both typed map orientations, plus genuine W34 dense/sparse/reassigned right map cores. Uses independent rational all-h coefficient tests for all small/large formal K,T values and malformed-input checks. These are **finite falsifiers**, not an all-h computational proof. The all-h proof is the direct inclusion–exclusion and source-pencil argument in §§1–4.

Dedicated GitHub-hosted Python3.12 CI plus full Research/INDEX at the EXACT branch HEAD are required before acceptance.

**Scientific STOP:** this is a new rigorous local all-h refinement of the source/core moment and path-count constants, not an independent proof of the global universal Branch A, a new signed \(R_3\) determination, or an improved ASET exponent. Scientific drafts #672–#680 remain dependent on qualified external mathematical review, and root #230 stays OPEN_WITH_FORMAL_BLOCKER. Do not merge the stack or close the root.
