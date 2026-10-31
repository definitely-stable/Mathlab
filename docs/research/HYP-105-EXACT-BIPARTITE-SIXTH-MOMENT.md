# HYP-105 #230 — AA4-MOM6: exact all-h noninjective 6-walk classification and improved selected-graph moment bound

**Scope:** independent exact combinatorics for EVERY finite SIMPLE BIPARTITE physical graph, with its specialization to the same complete, arbitrarily correlated original-source W(3,2^h) pair-label maps f,g and selected genuine ORIGINAL flag-ID subgraphs of [#672](https://github.com/definitely-stable/Mathlab/pull/672). The new bound improves the numerical coefficient of the selected-graph sixth moment by a factor **two** (144 to 72 in m Δ²), and combines naturally with the independently proven 4×/27× path selector in [#679](https://github.com/definitely-stable/Mathlab/pull/679). This does NOT independently establish the universal Branch A theorem or improve the powers of s. All root claims remain scientific Draft pending qualified external referee; [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) is OPEN_WITH_FORMAL_BLOCKER.

## 1. Exact all-h graph combinatorics: every non-simple closed six-walk

Let G=(U,W,E) be ANY simple undirected bipartite graph. Define A its full symmetric adjacency matrix, m=|E|, Δ=max physical degree, and C6 the number of unoriented, unrooted SIMPLE physical six-cycles. For u∈U let \(d_u=|N(u)|\). For pairwise different u,v,w∈U put
\[
 c_{uv}=|N(u)\cap N(v)|,\quad
 t_{uvw}=|N(u)\cap N(v)\cap N(w)|.
\]
A length-six closed walk rooted in U has three ordered LEFT positions u,v,w (not necessarily distinct) and three RIGHT positions which must lie in the three corresponding pairwise common-neighbor sets. Writing \(B\) for the U×W incidence matrix of this BIPARTITE physical graph gives \(A=\bigl[\begin{smallmatrix}0&B\\B^T&0\end{smallmatrix}\bigr]\), and therefore
\[
 \operatorname{tr}(A^6)=2\operatorname{tr}[(BB^T)^3]
 =2\sum_{u,v,w\in U}c_{uv}c_{vw}c_{wu},
 \quad c_{uu}=d_u.\tag{MOM6-TENSOR}
\]
This is a direct exact matrix trace identity, not a probabilistic or asymptotic approximation.

For three DISTINCT left vertices u,v,w, an injective physical six-cycle requires THREE DISTINCT right choices
\[
 r_{uv}\in N(u)\cap N(v),\
 r_{vw}\in N(v)\cap N(w),\
 r_{wu}\in N(w)\cap N(u).
\]
The number of distinct-right assignments is obtained by elementary inclusion–exclusion:
\[
 h_{uvw}=c_{uv}c_{vw}c_{wu}
   -t_{uvw}(c_{uv}+c_{vw}+c_{wu}-2)\ge0.
\tag{MOM6-RIGHT}
\]
Indeed, equality of any two right choices forces that shared right neighbor to be adjacent to ALL THREE left vertices, of which there are t. The three pair-equality event sizes are t*c_third; all intersections describe equality of all three rights and contribute +2t overall. Because every simple C6 has precisely three U vertices and three W vertices, each unoriented unrooted physical C6 contributes EXACTLY ONCE to h for the corresponding unordered left triple:
\[
 \boxed{ C_6=\sum_{\{u,v,w\}\subseteq U}h_{uvw}. }\tag{MOM6-CYCLES}
\]

Separating all three types of repetitions in (MOM6-TENSOR) yields the new **exact all-graph identity**
\[
\boxed{\begin{aligned}
 \operatorname{tr}(A^6)=12C_6&
 +2\sum_{u\in U}d_u^3\\
 &+6\sum_{\{u,v\}\subseteq U}(d_u+d_v)c_{uv}^2\\
 &+12\sum_{\{u,v,w\}\subseteq U}
      t_{uvw}(c_{uv}+c_{vw}+c_{wu}-2).
\end{aligned}}\tag{MOM6-EXACT}
\]
Every noncycle term is nonnegative. The first accounts for rooted six-walks using one distinct left vertex; the second accounts for repeated left vertices (two distinct left vertices); the last accounts for three distinct left vertices but two or more right positions equal. Thus the noninjective correction is a **fully explicit graph-local statistic**, not a loose “O(Δ trace4)” estimate. The same formula must hold independently on the RIGHT physical half W with its own degree, pair and triple common-neighbor statistics, providing a dual exact audit.

For example, K3,3 has C6=6, tr(A6)=1458, and 1386 noninjective closed length-six walks. These are exact unrooted cycles versus rooted walks, avoiding a common 12-fold error.

## 2. Independent all-h *strictly better* universal sixth moment

The earlier #672 used, for the selected simple bipartite graph,
\[
 X=\operatorname{tr}(A^6)
 \le12C_6+6\Delta\operatorname{tr}(A^4).
 \tag{MOM6-OLD-STEP}
\]
This is valid: a noninjective closed bipartite six-walk contains at least one two-step cyclic backtrack. There are six possible backtrack positions. Removing it yields a rooted closed four-walk, and reinserting it has at most Δ possibilities. This *upper bound* is independently checked against the exact decomposition above; we do not assume all such backtracks are disjoint (overcount is harmless).

An exact eigenvalue/Cauchy inequality for any real symmetric A gives
\[
 \operatorname{tr}(A^4)^2
 \le\operatorname{tr}(A^2)\operatorname{tr}(A^6)
 =2mX.
\]
Consequently
\[
 X\le12C_6+6\Delta\sqrt{2mX}.
\]
The only next step is elementary **Young inequality**
\[
 6\Delta\sqrt{2mX}
 \le\tfrac12 X+36m\Delta^2
\]
(which is precisely \(2ab\le a^2+b^2\), with \(a=\sqrt{X}\), \(b=6\Delta\sqrt{2m}\), divided by two). Rearranging:
\[
\boxed{\qquad
 \operatorname{tr}(A^6)
 \le24C_6+72m\Delta^2.
 \qquad}\tag{MOM6-72}
\]
This is the same all-h graph hypothesis as in #672, without adding any unknown source or graph-spectrum assumption. It replaces the old coefficient **144 by 72** (2× tightening). More generally, Young's inequality with θ∈(0,1) yields a tradeoff
\[
 X\le\frac{12}{1-\theta}C_6+
      \frac{18}{\theta(1-\theta)}m\Delta^2;
\]
θ=1/2 is optimal for the coefficient of the degree-error term at a fixed cycle coefficient 24.

## 3. Quantitative specialization to fixed arbitrary original W(3,s) f,g

Use the SAME original-source bounded core as #672. No change to f,g, and no resampling original flags: the auxiliary random priority/source-flag selector and two typed physical coordinate bichromatic cuts from #672/#679 produce a selected physical graph G which is *simple, bipartite and has no row/column cherries*. Every simple C6 of G is therefore coordinate-proper. By the original source flag-bijection [#652](https://github.com/definitely-stable/Mathlab/pull/652), each corresponds injectively to one historically accepted original D6 SIXSET using six DISTINCT original source incidence IDs:
\[
 C_6(G)\le D_6(f,g).
\]
The unchanged #672 core guarantees \(m_G\le m_0\le4s^4\) and \(\Delta_G\le\Delta_0\le Ts\). In the branch where original \(D_6(f,g)<\delta s^6\le s^6\), our improved universal inequality yields, **for every selector outcome**,
\[
 \operatorname{tr}(A_G^6)
 \le24s^6+72(4s^4)(Ts)^2
 =\boxed{(24+288T^2)s^6}. \tag{MOM6-NEW-L6}
\]
The old #672 bound was \(L_6^{\mathrm{OLD}}=24+576T^2\). Our new value
\[
 \boxed{L_6^{\mathrm{NEW}}=24+288T^2<L_6^{\mathrm{OLD}}\quad(T\ge1)}
\]
is a proven strictly stronger UNIFORM all-h selected-graph sixth-moment envelope. This is an improvement of constants only. The all-h dyadic geometry is used only to guarantee the actual source-flag and selected-physical-graph hypotheses; the pure graph inequality holds more generally.

Combine with the stronger [#679](https://github.com/definitely-stable/Mathlab/pull/679) path-priority selection constants \(\sigma_2^{\rm NEW}=1/[16(K+1)^2]\), \(\sigma_3^{\rm NEW}=1/[64(K+1)^3]\). Jensen yields
\[
 \|P_3\|_F^2\le
 [64(K+1)^3]^2(24+288T^2)s^6,
\tag{MOM6-P3}
\]
whereas #672 originally had \([64\cdot27(K+1)^3]^2(24+576T^2)s^6\). Hence the new squared Frobenius coefficient is **strictly more than 729 times smaller**. Similarly, \(\|P_2\|_F^2\) has a 16× smaller selector coefficient and a smaller \(\sqrt{8L_6}\) input. This propagates to the proper-path norm and source-core fourth-moment coefficients in #672, but does not change the powers \(s^6,s^5\) or the full-root proof status.

**Do not silently replace parent #674's explicit ρ,δ,s0** without a separate mathematically controlled all-dependency constant calculation. This PR is a valid stronger input bound; all earlier conservative proofs remain valid under their own pinned hypotheses.

## 4. Independent falsification, not an all-h computational claim

\`research/hyp105_exact_bipartite_sixth_moment.py\` independently implements THREE distinct sixth-moment computations for finite graphs:
1. Exact left and separately right **degree/codegree/triple-neighbor combinatorial expansion** (MOM6-EXACT), including the exact number of physical simple C6s and the three types of noninjective rooted six-walks.
2. Independent original physical vertex-by-vertex **length-four and length-six closed walk enumeration**, with no reliance on codegree expansion or a spectral numerical library.
3. Independent **simple physical sixcycle DFS**, including the 12 rooted/orientation multiplicity check.

Every result verifies \(tr(A4)^2\le2mtr(A6)\), \(tr(A6)\le12C6+6\Delta tr(A4)\), and the sharpened Young bound \(tr(A6)\le24C6+72m\Delta^2\). It fails closed on non-simple/non-bipartite/incorrectly typed inputs.

\`research/test_hyp105_exact_bipartite_sixth_moment.py\` exhaustively checks **ALL 4096 simple labeled bipartite graphs with three left and four right vertices**, plus K3,3, K4,4, stars, empty and asymmetric examples, with independent graph-walk and cycle DFS. It also independently builds from the **TRUE ORIGINAL W(3,2)** and **TRUE ORIGINAL W(3,4)** source flag data:
- fixed arbitrary *complete* separately injected f,g (five globally reassigned right g on W32, genuine W34 full/sparse/right reassigned);
- deterministic local-minimum source-flag priority selectors and independent typed coordinate bichromatic physical cuts, preserving BOTH original diagonals or removing BOTH;
- physical graph bipartiteness, actual original conflict independence and every selected physical sixcycle's coordinate properness;
- for every produced physical C6, six distinct ORIGINAL flags and six distinct original source point/line factors, independently classified as historical original D6 GF5 and checked injective as ORIGINAL sixsets;
- equality of direct closed-walk traces, exact codegree expansion and direct C6 enumeration, and the tighter \(\le24C6+72m\Delta^2\).

The all-h mathematical proof is §§1–3, not induction from finite W32/W34. The GitHub-hosted Python3.12 workflow runs this specialized independent fail-closed suite at exact commit SHA, alongside standard INDEX and full Research. External qualified mathematical review remains needed for global Branch A's entire path-selection and moment-to-original-sixset synthesis.

**Formal STOP:** No parent/main changes, no merges, no root #230 closure, no new ASET exponent or total signed \(R_3\). A successfully tested strict coefficient improvement does not imply a second independent proof of the root theorem.
