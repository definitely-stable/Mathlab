# HYP-105 / issue #230 — AA4-GQ2EP: exact two-endpoint ORIGINAL middle-incidence shadows and weighted GQ spectral contraction

**Research scope:** strict Draft child of [#762](https://github.com/definitely-stable/Mathlab/pull/762), frozen parent HEAD \`211ddfea2df52cd4feb390fb513c03f4be3c3a7b\`, with dedicated specialist, INDEX and FULL Research GitHub-hosted CI **SUCCESS**. The new all-order source theorem requires genuine symplectic \(W(3,s)\), fixed separately globally pair-injective but potentially arbitrarily mutually correlated f/g, real named original incidence flags, actual paired physical opposite diagonals and a retained original CORE. The ORIGINAL root [#230](https://github.com/definitely-stable/Mathlab/issues/230) is still **OPEN_WITH_FORMAL_BLOCKER**; no main mutation, merge, full global B/M<3/4, original seven-class six-motif theorem or ASET exponent is asserted.

**Prior art:** the REAL GQ point–line incidence singular values \((s+1),\sqrt{2s},0\) are classical, e.g. de Caen–Moorhouse, *The p-rank of the Sp(4,p) Generalized Quadrangle* (2000), §1, https://ericmoorhouse.org/pub/sp4p.pdf, and standard bipartite expander mixing as in Yufei Zhao, *Graph Theory and Additive Combinatorics*, MIT OCW Lecture 3, https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/. **Not claimed new:** GQ spectrum or the abstract expander-mixing lemma. **New in our source architecture:** the exact two-physical-endpoint orientation-based \(\phi^\top N_C\psi\) relaxation, quantification of its physical coupling defect and universal nonrandom f/g weighted GQ mixing certificate.

## 1. Why single-vertex original \(\Delta^2\) is insufficient

PR #762 proved an all-h source-degree bound under the ROOT minimal physical pair alphabet \(a_s\), \(\Delta_{\rm physical}=O(s^2)\). Hence every genuine coordinate-proper physical length-3 directed path family between fixed ordered physical endpoints \((u,v)\) obeys \(|\Gamma_{uv}|\le d_C(u)d_C(v)\le\Delta_s^2=O(s^4)\). In all complete genuine W34 fixed full label mappings the ACTUAL maximum \(|\Gamma_{uv}|\) is only 16, 21 and 17, compared with the root spectral cap \(41^2=1681\); this one-vertex bound discards almost all **two-endpoint** geometry. The next defensible step is therefore to derive a real GQ incidence cut that knows BOTH physical endpoint neighborhoods.

A tempting but INVALID shortcut is to claim that the label-overlap conflict graph of original middle source flags inherits the nontrivial \(\sqrt{2s}\) norm of the ORIGINAL GQ incidence matrix. It generally does not: the conflict graph depends on adversarial fixed f/g pair correlations. Our proof applies the known spectral norm ONLY to the genuine ORIGINAL point-line incidence operator \(N\), never to the arbitrary source physical-label conflict graph.

## 2. Genuine physical projection sets and ordered-pair orientation weights

Let \(s=2^h\), \(V=(s+1)(s^2+1)\), and \(I\subseteq P\times L\) be the complete genuine ORIGINAL source GQ incidence flags. Let \(I_C\subseteq I\) be any retained paired source CORE with actual physical graph \(H_C\). For any physical vertex \(z=(z_x,z_y)\), denote its ACTUAL physical CORE neighbor set by \(N_C(z)\) and its two typed coordinate projections by

\[
X_z=\{x:\exists y\ (x,y)\in N_C(z)\},\quad
Y_z=\{y:\exists x\ (x,y)\in N_C(z)\}.
\tag{EP-1}
\]

Do not confuse the physical-neighbor symbol sets \(X_z,Y_z\) with source point/line subsets from #762. The sets are derived from actual original paired opposite-diagonal edges, not from a guessed physical graph.

Fix ordered physical endpoints \(u,v\). For each ORIGINAL point \(p\) with fixed physical pair \(f(p)=\{\alpha,\beta\}\), define

\[
\boxed{
\phi_{uv}(p)=
\sum_{(a_x,b_x)\in\{(\alpha,\beta),(\beta,\alpha)\}}
\mathbf1[a_x\in X_u]\mathbf1[b_x\in X_v]\,
\mathbf1[\,|\,\{u_x,a_x,b_x,v_x\}\,|=4\,].
}
\tag{EP-2}
\]

For each ORIGINAL line \(\ell\) with physical pair \(g(\ell)=\{\gamma,\delta\}\), define \(\psi_{uv}(\ell)\) by exactly the same expression in y-coordinates with \(Y_u,Y_v\). Both weights belong to \(\{0,1,2\}\), and are computed from the actual ORIGINAL CORE physical endpoint neighborhoods but indexed by the full original source points/lines.

The ORIGINAL source incidence matrix \(N_{p\ell}=\mathbf1[p\sim\ell]\) is the full classical GQ matrix; the retained incidence matrix \(N_C\le N\) has ones only for the genuine retained named source flags.

## 3. NEW all-h two-endpoint weighted incidence shadow

A genuine proper directed physical three-path

\[
\gamma=(u,a,b,v),\qquad
a,b\in[a]^2,
\]

has real ORIGINAL incidence flag \((p,\ell)\in I_C\) as owner of its middle physical edge. Because that edge is one of the TWO actual opposite diagonals of the physical rectangle \(f(p)\times g(\ell)\), its ORIENTED first/last x-coordinates form one of the two orientations of \(f(p)\), and independently its y-coordinates form one of the two orientations of \(g(\ell)\). Real physical adjacency implies \(a\in N_C(u)\), \(b\in N_C(v)\). Genuine coordinate properness implies all four x coordinates and all four y coordinates are pairwise distinct. Therefore the middle edge's orientation contributes one of the \(\phi_{uv}(p)\psi_{uv}(\ell)\) possibilities.

Each oriented physical middle edge has a UNIQUE pair of actual internal vertices \((a,b)\). With fixed endpoints \(u,v\), it can determine at most one directed physical P3. Distinct source flags cannot share the same physical oriented middle edge by separate global f/g pair injection. Thus the following are true for EVERY legal order, retained CORE and arbitrarily correlated fixed f/g:

\[
\boxed{
n_{uv}:=|\Gamma_{uv}|
\ \le\ S_C(u,v):=\phi_{uv}^{\mathsf T}N_C\psi_{uv}
\ \le\ S_F(u,v):=\phi_{uv}^{\mathsf T}N\psi_{uv}.
}
\tag{EP-3}
\]

All terms are NONNEGATIVE exact INTEGERS. The first inequality can be strict even in FULL original W(3,s): independent x and y projection membership does not ensure the PHYSICAL joint first/last inner vertex is adjacent to the correct endpoint.

### NEW exact nonnegative coupling defect

Define

\[
\boxed{
E_{\rm coupling}(u,v)=S_C(u,v)-n_{uv}\ge0.
}
\tag{EP-4}
\]

This is not a probabilistic covariance. It is exactly the number of physically oriented middle source-flag diagonals whose x/y projections individually qualify as endpoint neighbor coordinates yet **fail to form actual first/last physical endpoint adjacencies together**. Equivalently, enumerate all FOUR true ORIENTED middle diagonals of every retained ORIGINAL source flag, require the proper x/y four-coordinate distinctness and independent projected endpoint membership, and count the subset that also satisfies true \(u\sim a\), \(b\sim v\); the counts are \(S_C\) and \(n\), respectively.

This is a concrete failure mode to preserve in future proofs: pretending the two endpoint coordinate projections are independent would incorrectly equate \(n_{uv}\) and \(S_C\).

For retained CORE the exact second nonnegative deletion defect is \(E_{\rm deleted}=S_F-S_C\ge0\). For full CORE \(E_{\rm deleted}=0\), while \(E_{\rm coupling}\) can still be positive.

### 3.1. NEW exact JOINT two-endpoint ORIGINAL incidence kernel (the missing correction)

There is also a direct ALL-h exact source-indexed tensor contraction, without the independent-coordinate relaxation. For a TRUE original middle source flag i=(p,l) and each of its FOUR oriented opposite-diagonal edges a→b, set

\[
K_{uv}(i)=\sum_{a\to b\text{ among the 4 real middle directions of }i}
\mathbf1[\,u\sim_{H_C}a\,]
\mathbf1[\,b\sim_{H_C}v\,]
\mathbf1[\,u_x,a_x,b_x,v_x\text{ all distinct}\,]
\mathbf1[\,u_y,a_y,b_y,v_y\text{ all distinct}\,].
\]

Then the EXACT source-first identity is

\[
\boxed{n_{uv}=\sum_{i\in I_C}K_{uv}(i).}
\tag{EP-4a}
\]

Indeed, each correct physical path has exactly one middle directed original source edge; conversely every counted orientation is a real adjacent coordinate-proper physical 3path. Coordinate properness forces the three original owner f-pairs (and separately g-pairs) to be distinct, so no two owners share the same genuine original point or line, and the true original J-properness requirement is satisfied. This is NOT a claim that original path selection events are independent.

Let \(\widehat K_{uv}(i)\) be exactly the same sum with the two JOINT physical-neighbor tests \(u\sim a,b\sim v\) relaxed to their separate first and second coordinate projection memberships, as in EP-2. Then

\[
\boxed{\widehat K_{uv}(i)=\phi_{uv}(p)\psi_{uv}(l),\quad
E_{\rm coupling}(u,v)=
\sum_{i\in I_C}\bigl[\widehat K_{uv}(i)-K_{uv}(i)\bigr].}
\tag{EP-4b}
\]

**Each individual summand is nonnegative** because a true physical neighbor implies BOTH coordinate memberships. This gives an exact source-flag-by-source-flag nonnegative defect decomposition, not merely a global integer difference; it identifies precisely the **JOINT endpoint physical-adjacency condition** that any next weighted GQ theorem must preserve. The independent verification does not assume the two coordinate factors are independent: it explicitly enumerates the four actual oriented ORIGINAL middle diagonals and recomputes both \(K\) and \(\widehat K\).

## 4. ALL-h centered REAL GQ weighted spectral upper (classical operator, NEW input vectors)

Let \(S_\phi=\sum_p\phi(p)\), \(Q_\phi=\sum_p\phi(p)^2\), \(S_\psi=\sum_\ell\psi(\ell)\), \(Q_\psi=\sum_\ell\psi(\ell)^2\). The complete true original GQ incidence matrix \(N\) is \((s+1)\)-biregular and its largest nonconstant REAL singular value is \(\sqrt{2s}\).

Center arbitrary real orientation vectors, \(\phi^\circ=\phi-(S_\phi/V)\mathbf1\), \(\psi^\circ=\psi-(S_\psi/V)\mathbf1\). The mixed constant/nonconstant terms vanish, and by Cauchy–Schwarz plus the known operator norm,

\[
\left|S_F-\frac{(s+1)S_\phi S_\psi}{V}\right|
\le
\sqrt{2s\left(Q_\phi-\frac{S_\phi^2}{V}\right)
\left(Q_\psi-\frac{S_\psi^2}{V}\right)}.
\tag{EP-5}
\]

Since \(S_F\) is an integer, the ALL-h exact integer upper bound is

\[
\boxed{
S_F\le U_{\rm GQ}(u,v):=
\left\lfloor
\frac{(s+1)S_\phi S_\psi+
\sqrt{2s(VQ_\phi-S_\phi^2)(VQ_\psi-S_\psi^2)}}{V}
\right\rfloor.
}
\tag{EP-6}
\]

**Implementation requires NO floating arithmetic:** compute \(A=2s(VQ_\phi-S_\phi^2)(VQ_\psi-S_\psi^2)\), then evaluate \(U_{\rm GQ}=\lfloor((s+1)S_\phi S_\psi+\lfloor\sqrt A\rfloor)/V\rfloor\) using integer \`isqrt\`. Independently check every original full source endpoint's EXACT squared inequality

\[
\boxed{
\bigl(VS_F-(s+1)S_\phi S_\psi\bigr)^2
\le2s(VQ_\phi-S_\phi^2)(VQ_\psi-S_\psi^2).
}
\tag{EP-7}
\]

This is valid for any nonnegative orientation weights, not merely x/y randomly chosen or independent labels. It applies to the FULL original incidence only; for retained arbitrary CORE, use the nonnegative monotonicity \(S_C\le S_F\).

## 5. Combined two-endpoint geometry and exact moment consequences

Every proper P3 also has first interior physical vertex in \(N_C(u)\) and last in \(N_C(v)\). Therefore

\[
\boxed{
n_{uv}\le
\min\{d_C(u)d_C(v),\ S_C(u,v),\ U_{\rm GQ}(u,v)\}.
}
\tag{EP-8}
\]

The \(S_C\) bound is itself source-explicit and is at most \(S_F\le U_{\rm GQ}\); therefore WHEN computing all of \(S_C\) exactly, the direct GQ spectral bound is redundant in the minimum. The spectral inequality is valuable as a SEPARATE *source-agnostic functional* bound using only the original full incidence spectrum, endpoint projections and source label maps. Do not claim that the spectral expression is always stronger than the EXACT retained projection shadow.

Squaring EP-8 and summing over all actual source nonempty ordered endpoint families gives the exact ALL-h Frobenius control

\[
\boxed{
\sum_{uv}n_{uv}^2
\le\sum_{uv}\min\{d_C(u)d_C(v),S_C(u,v)\}^2,
}
\tag{EP-9}
\]

where bins with n=0 can be omitted from both sides only if treating the RHS as a **restricted sum over nonempty bins**; for the global full endpoint universe, retaining all bins makes the upper bound still valid.

Since one true proper physical P3 selector marginal satisfies \(0<p_\gamma\le1/64\) under the original shared source priority and TWO typed fair cuts, the exact original squared first-moment mass has the valid UPPER bound

\[
\boxed{
M=\sum_{uv}\left(\sum_{\gamma\in\Gamma_{uv}}p_\gamma\right)^2
\le\frac1{4096}\sum_{uv} n_{uv}^2
\le\frac1{4096}\sum_{uv}\min\{d_C(u)d_C(v),S_C(u,v)\}^2.
}
\tag{EP-10}
\]

This remains an UPPER control. It does not automatically imply the required GLOBAL original \(B/M<3/4\), a lower bound on the compatible path mass, or the seven-class six-motif Branch A. In particular, no independence of source selector events is used.

## 6. Independent full ORIGINAL W32/W34 verification protocol

The new referee uses genuine original symplectic flag and physical opposite-diagonal edge builder from #758 and the source's already independently audited path generator. It DOES NOT invoke source J cross-path conflict or the prior #760 compatible/incompatible moment algorithm in its new shadow/spectral computation.

- For **every nonempty physical endpoint bin** in all eight complete true original W32/W34 fixed-label source cases, compute \(\phi,\psi\), exact FULL GQ and retained CORE incidence bilinear shadows, exact integer GQ mixing upper, first/last physical degree product, the true independent complete coordinate-proper P3 baseline n, and exact two nonnegative defects EP-4 and E_deleted.
- Independently verify ALL numerical identities \(n\le S_C\le S_F\le U_{\rm GQ}\), \(n\le d(u)d(v)\), EP-7 in integers, \(\sum n^2\) and source shadow/deleted/coupling conservation. Export exact per-bin maxima and a genuine physical endpoint witness for the strongest improvement from the direct original CORE source shadow vs degree-product.
- For **EVERY W32** active endpoint bin and deterministic physical endpoint samples including each largest W34 source P3 family, an entirely separate oracle iterates all FOUR real ORIENTED paired diagonal middle physical edges of each retained ORIGINAL incidence flag and checks its actual physical neighbor coupling. Exact first/second counts must equal \(S_C,n\), independently of the algebraic \(\phi^\top N_C\psi\) computation and previous path enumeration.
- W32 full lex/reverse and shift Z17, plus W34 FULL lex/reverse/shift, lex even, shifted Z17: the complete directed proper P3 population must be exactly **1,346/1,154/838** and **83,892/82,846/79,404/9,966/66,418**. All eight are complete, not truncated sample populations.
- A dedicated Ubuntu24 GitHub-hosted Python3.12 workflow runs 14 independent tests plus a strict single-line JSON/Fraction/integer source certificate; INDEX and FULL Research must be independently green on the FINAL HEAD. No CI green assertion will be carried forward from an earlier HEAD without rechecking.

## 6.1. COMPLETE TRUE ORIGINAL W34 experimental falsification of uncorrected projection tightness

The first dedicated full true source CI completed [specialist #43495403926](https://github.com/definitely-stable/Mathlab/actions/runs/43495403926) **SUCCESS, 13/13 independently checked tests plus exact eight-case integer machine JSON**, [INDEX #43495403852](https://github.com/definitely-stable/Mathlab/actions/runs/43495403852) **SUCCESS** on the initial scientific code HEAD \`77a979468fbdc934183c381e3afcc6a5049e96e1\`. The full Research workflow #43495403745 was independently running when the table was drafted. The new final-head additional finite-result test and documentation will trigger another CI, which must be separately checked. Exact integers below are complete source censuses, not extrapolated numerical estimates or random f/g expectations.

| Genuine FULL ORIGINAL W(3,4), fixed f/g | Actual proper P3 n summed over ordered endpoint bins | Two-endpoint retained source orientation projection shadow S_C summed | Exact physical JOINT endpoint-coupling defect S_C−n | Fraction of all projected orientations NOT real proper paths | Nonempty endpoint bins where S_C beats d(u)d(v) |
| --- | ---: | ---: | ---: | ---: | ---: |
| FULL lex | **83,892** | 2,117,602 | **2,033,710** | **96.0383%** | 19,066 / 28,136 = 67.76% |
| FULL reverse | **82,846** | 2,037,178 | **1,954,332** | **95.9333%** | 19,418 / 27,648 = 70.23% |
| FULL shifted | **79,404** | 2,077,654 | **1,998,250** | **96.1782%** | 18,494 / 27,948 = 66.17% |

The true original physical coordinate-proper projection shadow \(S_C\) is **24.59–26.17× larger** than the actual proper physical P3 count across these finite fixed-source labelings. Therefore a proof that treats independent x/y endpoint projections as a faithful approximation to joint actual physical source adjacency would be **strongly false even in these small full original cases**.

The separate GQ SPECTRAL-ONLY relaxed upper \(U_{\rm GQ}\) beats the actual endpoint degree product \(d(u)d(v)\) for only **284/28,136 (1.01%)**, **626/27,648 (2.26%)**, and **222/27,948 (0.79%)** of the respective nonempty W34 endpoint families. This is a **negative practical result** for using only the true classical GQ spectral mixing on the independently projected source labels.

However the exact source CORE projection contraction does give a valid **instance-dependent upper improvement**: the sum of squared endpoint upper bounds
\(\sum_{uv}\min\{d(u)d(v),S_C(u,v)\}^2\)
reduces from **232,414,728 to 182,468,398** in FULL lex (**21.49% reduction**), from **227,950,208 to 171,649,626** in reverse (**24.70% reduction**), and from **214,337,828 to 165,337,138** in shift (**22.86% reduction**). These bounds are still HUGE compared with the TRUE full proper path endpoint square sums **358,424 / 360,670 / 323,816**. Therefore the new upper bound, although mathematically exact as a source projection-relaxation certificate, is nowhere near a sharp enough estimate for the original universal weighted-good-mass proof.

**RESEARCH DECISION:** Stop trying to improve the root's conditional weighted source collision bound via further refinements of the **SEPARATE x/y projection** spectral norm alone. The next valuable source proof must retain the JOINT endpoint-neighbor incidence masks in \(K_{uv}(i)\), then transfer the exact genuine shared selector 3-owner priority marginals to a source-flag-indexed weighted tensor \(W_{uv,i}\) and control its pair-label-overlap quadratic \(R/M\) with genuine GQ incidence. No all-h gain from finite fixed f/g percentages is claimed; the correct counterexample search must allow fully correlated f/g at arbitrary h.

## 7. Scientific conclusion, negative controls and next allowed action

**PROVED all-h algebraically:** the true ORIGINAL physical two-endpoint oriented projection source bilinear EP-3; nonnegative, independently countable original physical endpoint coupling and retained-CORE deletion defects EP-4; centered real GQ weighted source mixing EP-5/6/7; combined source-specific and spectral two-endpoint path count/Frobenius upper EP-8/9; fixed-selector M upper EP-10. All retain arbitrary f/g correlation and original paired incidence ownership.

**NOT PROVED:** a strict universal global \(B/M<3/4\), a lower GF5 six-motif source obstruction \(S_s(f,g)\ge c s^6\), a uniform bound on the SOURCE middle-label-overlap \(R/M\), an all-order endpoint-fiber ratio \(n/U_{\rm GQ}\), an infinite correlated adversarial counterfamily or ASET exponent. If projected orientation shadows turn out much larger than real n in finite source cases, that is a NEGATIVE precision result, not permission to silently assume coordinate independence.

**Next genuinely useful proof gate after this slice:** retain endpoint-coupled source incidences rather than only coordinate projections. The next operator must count \((p,\ell)\) incidences weighted by the actual *joint* first/last inner physical vertex-adjacency indicators and ultimately incorporate exact original three-owner selector marginal weights; only then can the two-endpoint geometry be related quantitatively to the source middle-overlap quadratic \(R\) from #760/#761. Spectral arguments must act on the TRUE original GQ incidence N, not on an arbitrary fixed-label overlap graph. No merge, no root closure.
