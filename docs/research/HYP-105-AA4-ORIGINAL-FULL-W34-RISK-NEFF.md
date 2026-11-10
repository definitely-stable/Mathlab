# HYP-105 #230 — AA4-FULLW34: ALL-h weighted effective path multiplicity and COMPLETE ORIGINAL W(3,4) risk census

**Provenance and strict governance.** This independent scientific Draft is stacked on frozen [#756](https://github.com/definitely-stable/Mathlab/pull/756), HEAD \`4d691415bef4bf26a9161db5c577f4c07d1acaf2\`; at the start of this slice its dedicated specialist, INDEX, **full Research** GitHub-hosted CI were all SUCCESS. This step deliberately avoids another W32-only adversarial local sample. It (1) proves an exact new all-order *weighted diagonal-effective multiplicity* refinement to the previously proved original source weighted Motzkin–Straus incompatible-pair bound, (2) proves an all-order ORIGINAL oriented-middle-flag inversion, and (3) computes complete genuine original W(3,4) physical proper-P3 sources with **exact rational** risk and endpoint local graph clique data. It does not assume independence of paths or randomized f/g labels and NEVER claims full root Branch A/ASET exponent acceptance. Issue #230 remains OPEN_WITH_FORMAL_BLOCKER; no ancestors/main modified, no merges.

## 1. Original objects, quantifiers and exact operator

Let \(W(3,s)\) be the genuine symplectic GQ with \(s=2^h\), ORIGINAL point and line sets \(P,L\), named original incidence flags \(I=\{(p,\ell):p\in\ell\}\), and **fixed separately globally pair-injective, arbitrarily mutually correlated** assignments \(f:P\hookrightarrow\binom{[a]}2,\ g:L\hookrightarrow\binom{[a]}2\). An adversary may delete a set Z of named original IDs; the remaining paired core C comprises genuine incidence IDs with both real opposite physical diagonals owned by each retained source flag, and original point/line source conflict graph J_C with degree at most K=64 in LOW.

Each actual directed coordinate-proper physical 3path \(\gamma=(u,a,b,v)\) has 4 mutually distinct first typed coordinates and 4 mutually distinct second typed coordinates, and three pairwise J_C-independent genuine ORIGINAL flag owners. Under ONE uniform original source-priority permutation and TWO independent shared typed fair-bit cuts, it survives with exactly the strictly positive marginal

\[
p_\gamma=\Pr(\mathrm{all\ 3\ original\ owners\ local\ minima})/64,
\]

not a product of path probabilities or random choice of f/g maps. The all-order Harris selector lower from #754 gives \(p_\gamma\ge[64(K+1)^3]^{-1}\).

For each fixed ordered physical endpoints \(u,v\), denote the finite set of all such paths by \(\Gamma_{uv}\). Let

\[
W_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma,\quad
M_{uv}=W_{uv}^2,\quad
D_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma^2.
\]

Construct the *actual* original incompatibility graph \(H_{uv}\) on paths in this bin, with an edge iff two distinct paths' original named owners have some genuine source J_C edge, or their true first-/second-coordinate inner typed arcs have one of the four opposite-depth equalities. This is precisely the mutually exclusive joint-retention locus proved in #753. Let \(\omega_{uv}\) be its ordinary graph clique number, and \(B_{uv}\) the weighted ordered adjacent-pair sum \(2\sum_{\{\gamma,\eta\}\in E(H_{uv})}p_\gamma p_\eta\), so \(G_{uv}=M_{uv}-B_{uv}\) is the original-compatible ordered path-pair *marginal product* weight, including all diagonal pairs.

## 2. NEW all-h theorem: source-weighted diagonal + Motzkin effective multiplicity

The original weighted Motzkin–Straus argument of #755, with a full standalone elementary proof in that ancestor, gives

\[
G_{uv}\ge M_{uv}/\omega_{uv}.
\tag{W34-1}
\]

**Additional exact structural positivity:** every path is compatible with ITSELF (three proper original owners J-independent and the single path's factor constraint graphs are 3-edge paths, hence bipartite). Consequently the diagonal part of G includes exactly \(D_{uv}\), regardless of any source-owner overlaps, adversarial f/g correlations, Z or independent-path heuristics:

\[
G_{uv}
=D_{uv}+2\!\!\sum_{\{\gamma,\eta\}\notin E(H_{uv})}p_\gamma p_\eta
\ge D_{uv}.
\tag{W34-2}
\]

Define the true source probability-weighted effective physical path count

\[
n_{\rm eff}(u,v)=M_{uv}/D_{uv}
=\frac{(\sum_\gamma p_\gamma)^2}{\sum_\gamma p_\gamma^2}
\qquad(\Gamma_{uv}\neq\varnothing),
\]

which lies between 1 and \(|\Gamma_{uv}|\) by Cauchy. There is no numerical approximation in its definition.

Combining **two independently valid** lower bounds is legitimate with a maximum (not their SUM):

\[
\boxed{
G_{uv}\ge\max\left\{\frac{M_{uv}}{\omega_{uv}},D_{uv}\right\}
=M_{uv}\max\left\{\frac1{\omega_{uv}},\frac1{n_{\rm eff}(u,v)}\right\}.
}
\tag{W34-3}
\]

Summation over all ordered physical endpoint bins produces the new universal exact risk certificate

\[
\boxed{
\frac BM\le 1-
\frac1M\sum_{u,v}\max\left\{\frac{M_{uv}}{\omega_{uv}},D_{uv}\right\},
\qquad M=\sum M_{uv}>0.
}
\tag{W34-4}
\]

This uniformly strengthens the #756 clique-tail certificate by a nonnegative, explicitly computable amount without external probability estimates, source f/g independence, graph regularity or a priori infinite-family bounds. Its sufficient strict GLOBAL \(B/M<3/4\) acceptance gate is

\[
\boxed{\sum_{u,v}\max\{M_{uv}/\omega_{uv},D_{uv}\}>M/4.}
\tag{W34-5}
\]

Crucially, a single endpoint bin with **strictly** \(B_{uv}/M_{uv}>3/4\) requires BOTH

\[
\boxed{\omega_{uv}\ge5\quad\text{AND}\quad n_{\rm eff}(u,v)>4.}
\tag{W34-6}
\]

The clique-five necessity is strict: for a four-clique of equal weights, \(B/M=3/4\) is allowed. The new effective-multiplicity condition can discard some high-clique bins that did NOT qualify as dangerous by clique alone, and defines a smaller adversarial target: the \(M\)-mass in bins satisfying BOTH predicates. The combined condition is NECESSARY, NOT sufficient for local bad ratio exceeding 3/4.

**Scientific bound:** Without a source-geometric estimate of the global distribution of \(n_{\rm eff}\) and \(\omega\) for *arbitrary* original fixed correlated f/g as s grows, this theorem does NOT claim a global \(B/M<3/4\). Its improvement may be zero in some instances. It is also independent of the inherited selected sixth-moment upper \(L_6s^6\): do not illegitimately subtract B or promote full Branch A.

## 3. NEW all-h genuine ORIGINAL middle-flag inverse (no synthetic graph path injection)

Each REAL physical edge \(\{a,b\}\) lies in exactly one original retained incidence flag \(i=(p,\ell)\) (physical edge ownership), because f and g separately injectively determine its two unordered coordinate pairs. That actual flag owns exactly TWO opposite rectangle diagonals. A directed real physical P3 \(\gamma=(u,a,b,v)\) has exactly one **directed middle physical edge** \(a\to b\), with middle ORIGINAL ID \(i_{\rm mid}\); and its inner coordinate pairs must satisfy

\[
\boxed{
f(p_{\rm mid})=\{a_x,b_x\},\qquad
g(\ell_{\rm mid})=\{a_y,b_y\}.
}
\tag{W34-7}
\]

These identify the named original source point and line of the middle edge independently; the pair \((p_{\rm mid},\ell_{\rm mid})\) must be a TRUE incidence flag. Fix the ordered physical endpoints \((u,v)\). Given any *directed* middle physical edge \(a\to b\), the physical P3 path is uniquely determined as \((u,a,b,v)\), if both required outer edges exist and the four typed coordinates are proper.

An original source flag owns only 2 undirected diagonals, i.e. 4 possible directed middle physical edges. Consequently, **for every dyadic s, every original f/g correlation, every retained named source CORE and any ordered physical endpoint bin**,

\[
\boxed{
\#\{\gamma\in\Gamma_{uv}:\operatorname{owner}_{\rm middle}(\gamma)=i\}\le4.
}
\tag{W34-8}
\]

This is a small but directly source-geometric constraint on localization of the dangerous bin path multiplicity, not an unspecified graph-label path. Full source finite programs check (W34-7) for EVERY physical P3, enforce unique directed middle edge per endpoint bin, and count maximum repeat multiplicity of each REAL original middle flag. Values greater than four fail closed. This lemma by itself does not bound dangerous endpoint M-mass globally, but provides a source-first anchor for a future true GQ incidence charge argument.

## 4. Complete finite-original source risk census; zero sampled paths where labeled COMPLETE

The main referee imports **ONLY** the true symplectic source incidence fixture from #748; unlike prior #755/#756 snippets it independently rebuilds fixed f/g pair maps, original point/line J conflict pencils, named Z and BOTH original-owned physical flag diagonals. It then exhaustively enumerates all valid directed coordinate-proper P3s for the listed cores, caching exact **six-permutation original priority integrals** as arbitrary-precision Fractions for each 3-owner set. Every path's marginal uses these exact true ORIGINAL priorities times 1/64. It groups ALL paths by ordered physical endpoints and computes all ordered same-endpoint pairs, disjoint source J/typed collision classes, exact weighted \(B,G,M,D\), and exact maximal clique by independent bitset recursive enumeration for EVERY nonempty endpoint bin. All middle source-flag inversions and physical owner counts checked on every path; no sample cutoff exists in this main referee.

| Exact finite ORIGINAL source case | Named source flags | Physical owned edges | Known full true proper P3 count |
|---|---:|---:|---:|
| W(3,2), full lex | 45 | 90 | 1,346 |
| W(3,2), full reverse | 45 | 90 | 1,154 |
| W(3,2), fixed shifted labels, Z17 CORE | 42 | 84 | 838 |
| W(3,4), **FULL lex** | **425** | **850** | **83,892** |
| W(3,4), **FULL reverse** | **425** | **850** | **82,846** |
| W(3,4), **FULL shifted** | **425** | **850** | computed independently |
| W(3,4), even retained CORE | 213 | 426 | computed independently |
| W(3,4), named-Z17 CORE | 400 | 800 | computed independently |

The full W34 lex/reverse 3path counts are **predeclared external regression checks** from prior independent #751 source construction, not computed assumptions inside the new main proof. All full W34 risks and every endpoint clique/multiplicity are newly rederived from scratch. The W34 even/Z17 source core cases are also fully enumerated **for their named cores**; their ~half/full flag deletions are NOT claimed to satisfy the asymptotic very small root \(|Z|\le\rho s^4\) premise at s=4.

The strict JSON result includes, for every case, all B/G/M exact Fraction totals, the number of properly directed physical P3, the full same-endpoint pair count, the clique histogram over all physical ordered endpoint bins, the maximum multiplicity per ORIGINAL middle flag, the exact diagonal M-weight, the previous Motzkin and new stronger hybrid G-weight floors, the weighted share of bins with clique≥5, the weighted share with BOTH clique≥5 and effective multiplicity>4, and the strongest true-original local bad ratio witness with its physical endpoints, all original source-flag owner triples, path vertices and exact probability weights. This evidence can expose a TRUE original risk counterexample if present but **finite W34 evidence cannot prove all-h asymptotic global B/M<3/4**, even if all its ratios stay below threshold.

The dedicated GitHub-hosted Ubuntu 24.04 Python 3.12 specialist has an independent suite of 18 tests (including exact W32 baseline equations and full W34 lex/reverse required P3 populations) plus a strict fail-closed one-line machine certificate. INDEX and full Research must be checked at exact PR HEAD independently. The main source is standalone with respect to previous AA4 calculations; inherited source geometry fixture is the only imported component.

## 5. What this proves, does not prove, and next scientific gate

**New standalone all-h results:** (W34-3) and (W34-4) the universal *maximum of diagonal and Motzkin* source-weighted good-pair energy, (W34-6) the stricter necessary conjunction (clique≥5 AND effective original path multiplicity>4) for a local strictly bad endpoint, and (W34-7)/(W34-8) exact original middle-flag source inverse/multiplicity cap. The full W34 finite scientific audit is *separate* exhaustive geometric evidence, not part of the all-h proof.

**Not proved:** an automatic all-h \(B/M<3/4\), any fixed positive asymptotic gap below 3/4, a stronger all-h selected sixth-moment \(L_6\), a new positive seven ORIGINAL six-ID motif theorem beyond inherited conditional HEAVY/LOW or a new ASET exponent. No numeric ordinary graph C6 theorem constants are presumed.

**Next allowed mathematical step:** use actual original incidence geometry and the source-middle-flag injection to bound the **global weighted \(M\) mass of endpoint bins with BOTH \(\omega\ge5\) and \(n_{\rm eff}>4\)**. If that tail is small enough versus the safe bins' positive Motzkin/diagonal slack, a strict global B/M<3/4 could follow. Or construct a valid all-h adversarial fixed-correlated f/g family that prevents such a bound. In parallel, independently close or invalidate remaining inherited source HEAVY/LOW/GF5 proof acceptance gates, without merging unaccepted Draft research to main.
