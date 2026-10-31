# HYP-105 #230 — AA4-SELPLUS: independent all-h path selector via positive dependence of original source-flag minima

**Scientific scope:** fixed true ORIGINAL symplectic \(W(3,2^h)\), **arbitrary fully correlated** separately globally injected point and line physical pair maps \(f,g\), and an arbitrary actual original source-flag core whose ORIGINAL conflict graph has maximum degree \(\le K\). This is a NEW deterministic-combinatorial probability lemma about the existing auxiliary random priority selector of [#672](https://github.com/definitely-stable/Mathlab/pull/672), not an assumption that f,g or distinct physical paths are random or independent. This improves the constants of the selector's \(r=2,3\) survival lower bounds **4-fold and 27-fold** and the proper-path squared Frobenius-envelope coefficients by **16-fold and 729-fold**. The exponent of the moment errors is unchanged. This does **NOT independently prove** the rest of Branch A, exact \(R_3\), or an ASET exponent. Root #230 remains OPEN_WITH_FORMAL_BLOCKER until qualified independent acceptance.

## 1. Exact all-h ORIGINAL source conflict setup

Take a finite simple undirected conflict graph \(H_{\rm src}=(I,E)\) on **actual ORIGINAL source incidence flag IDs** retained in the core. Two flags conflict iff the actual original point factors agree and their right pair labels intersect, or their original line factors agree and their left pair labels intersect. The existing #659/#672 source-pencil books imply \(\Delta(H_{\rm src})\le K\) after deterministic core pruning. Every coordinate-proper physical 2-path and every coordinate-proper physical 3-path in this core has \(r=2,3\) distinct ORIGINAL flag IDs and distinct ORIGINAL points/lines, hence these r target flags are **PAIRWISE NONCONFLICTING** in the core ORIGINAL graph. There is no assumption of edge-disjoint conflict neighborhoods. In fact overlap is possible and helps the local-minimum selector.

Give every core source flag \(v\in I\) an independent continuous uniform random priority \(U_v\in[0,1]\), equivalently one uniform random ordering of ALL retained ORIGINAL flags. Select a flag exactly if its priority is strictly less than those of ALL its neighbors. This is the same selector already defined in #672; its output is an ORIGINAL-ID independent subset. Retain BOTH actual physical diagonals of each selected flag. Then, **independently of priorities**, color LEFT and RIGHT physical coordinate symbols with independent unbiased binary colors and retain a selected ORIGINAL flag exactly when both typed pair labels are bichromatic.

## 2. New fundamental lemma — exact integral and positive correlation

Fix ANY set \(T=\{v_1,\ldots,v_r\}\) of pairwise nonadjacent ORIGINAL source flag vertices. Let \(N(T)=\cup_{v\in T}N(v)\), which is disjoint from T. Conditional on the target priorities \(t_v=U_v\) for \(v\in T\), all the remaining neighbor priorities \(U_w\), \(w\in N(T)\), are independent. The condition that ALL targets are selected is exactly
\[
 U_w>\max_{v\in N(w)\cap T}t_v\quad\text{for every }w\in N(T).
\]
Therefore the **EXACT** joint probability is
\[
\boxed{
\Pr(T\text{ all local minima})
=\int_{[0,1]^r}
\prod_{w\in N(T)}
 \left(1-\max_{v\in N(w)\cap T}t_v\right)
\,dt_1\cdots dt_r.
}\tag{SELPLUS-EXACT}
\]
This integral is valid for *all* finite source conflict graphs, all r, all shared neighborhoods, and does NOT multiply nonindependent local-minimum indicator probabilities.

For any numbers \(t_1,\ldots,t_k\in[0,1]\),
\[
 1-\max(t_1,\ldots,t_k)
 =\min_i(1-t_i)\ \ge\ \prod_i(1-t_i).
\]
Apply this to EVERY shared-neighbor factor in (SELPLUS-EXACT). The integrand is bounded below by
\[
 \prod_{w\in N(T)}\prod_{v\in N(w)\cap T}(1-t_v)
 =\prod_{v\in T}(1-t_v)^{\deg(v)}.
\]
Integrate the individual target priorities independently:
\[
\boxed{
 \Pr(T\text{ all selected})
 \ge\prod_{v\in T}\frac1{\deg_{H_{\rm src}}(v)+1}
 \ge\frac1{(K+1)^r}.
}\tag{SELPLUS-PRODUCT}
\]
This is strictly stronger than the old “all r targets first in the union of their neighborhoods” argument, which gave \([r(K+1)]^{-r}\). **Shared non-target neighbors are handled exactly rather than discarded**; they cause *positive* correlation of the nonadjacent local-minimum events, not independence. If any two selected source flags have a common neighbor, the first integrand inequality is strict on an open subset of target-priority space, so the exact probability is STRICTLY greater than the product bound. If all their neighborhoods are disjoint, equality holds.

### Efficient exact rational \(r!\)-term formula — no huge factorial

To independently audit (SELPLUS-EXACT) with exact fractions, order the r target priorities as
\(0<t_{\pi(0)}<\cdots<t_{\pi(r-1)}<1\).
For each \(j\), define \(n_j(\pi)\) as the number of *distinct* conflict-neighbor flags \(w\in N(T)\) whose latest target neighbor in priority order is \(\pi(j)\). The integrand restricted to this simplex is precisely
\(\prod_{j=0}^{r-1}(1-t_{\pi(j)})^{n_j}\).

Set \(z_j=1-t_{\pi(j)}\), so \(1>z_0>\cdots>z_{r-1}>0\). Repeated exact integration gives
\[
 \int_{1>z_0>\cdots>z_{r-1}>0}
   \prod_{j=0}^{r-1}z_j^{n_j}\,dz
 =\prod_{j=0}^{r-1}
  \left(\sum_{k=j}^{r-1}(n_k+1)\right)^{-1}.
\]
Summing the r! possible target orders yields
\[
\boxed{
\Pr(T\text{ all selected})
=\sum_{\pi\in S_r}
 \prod_{j=0}^{r-1}
 \frac1{\sum_{k=j}^{r-1}(n_k(\pi)+1)}.
}\tag{SELPLUS-RATIONAL}
\]
Every term is a rational number computable from the ORIGINAL conflict graph. The formula uses **at most six permutations for r=3** rather than enumerating \(|I|!\) orderings. Its proof does not depend on W32/W34 tests.

**Independent counterexample to local-minimum event independence:** in the source-conflict graph \(0-2-1\), the nonadjacent original target IDs 0 and 1 share neighbor 2. Their exact joint probability is \(1/3\), versus the product of individual minima probabilities \(1/4\). Thus an independence *equality* is incorrect; the positive product **lower bound** is correct. Our tests require both exact values.

## 3. Original proper-path physical coordinate cuts and new selector constants

For one fixed genuine physical coordinate-proper r-edge path \(v_0\ldots v_r\), its left physical coordinates \(x_0,\ldots,x_r\) are all DISTINCT, and similarly the right coordinates \(y_0,\ldots,y_r\). The two binary coordinate colorings are independent of priorities and of one another.

On one typed side, exactly TWO out of \(2^{r+1}\) binary color assignments alternate along all r edges; the probability is \(2^{-r}\). The two typed sides together retain all r source flag labels with probability exactly \(4^{-r}\). This is a statement about **one fixed original-source physical path**, not independence across different paths. Consequently (SELPLUS-PRODUCT) proves the all-h uniform lower bound
\[
 \Pr(\text{fixed coordinate-proper r-path survives the full selector})
 \ge\frac1{4^r(K+1)^r}.
\]
For the two values required by #672:
\[
\boxed{
 \sigma^{\rm NEW}_2=\frac1{16(K+1)^2}
    =4\,\sigma^{\rm OLD}_2,\qquad
 \sigma^{\rm NEW}_3=\frac1{64(K+1)^3}
    =27\,\sigma^{\rm OLD}_3.
}\tag{SELPLUS-SIGMAS}
\]
The old valid constants were
\(\sigma^{\rm OLD}_2=[64(K+1)^2]^{-1}\) and
\(\sigma^{\rm OLD}_3=[64\cdot27(K+1)^3]^{-1}\).
At the fixed #672 cap \(K=64\), the exact new floors are
\[
 \sigma_2^{\rm NEW}=1/67600,\qquad
 \sigma_3^{\rm NEW}=1/17576000.
\]
These are exact fractions, not measured empirical frequencies.

## 4. Propagation through #672's proven moment transfer

Let \(P_r(u,v)\) count ACTUAL coordinate-proper directed r-paths in the fixed physical core H0, without randomizing physical f,g or original source flags. For the *same* already existing auxiliary selector, \((A_G^r)_{uv}\) counts all r-walks in the selected graph. By linearity over proper ORIGINAL source paths and the pointwise new survival floor:
\[
 \mathbb E (A_G^r)_{uv}
 \ge\sigma_r^{\rm NEW}P_r(u,v).
\]
No different-path independence is used or needed. Jensen applied to the nonnegative random \((A_G^r)_{uv}\) and then summed over ordered endpoints yields
\[
 \boxed{
 \|P_r\|_F^2\le(\sigma_r^{\rm NEW})^{-2}
                    \mathbb E\operatorname{tr}(A_G^{2r})
 \le(\sigma_r^{\rm NEW})^{-2} L_{2r},
 }\tag{SELPLUS-MOMENTS}
\]
where for r=2 the appropriate fourth-moment bound of the selected graph is used and for r=3 the sixth-moment bound from #672 is used. In the #672 normalizations
\[
 \|P_3\|_F^2 \le [64(K+1)^3]^2 L_6s^6,
\]
versus the older coefficient \([64\cdot27(K+1)^3]^2\), **729 times larger**. Similarly
\[
 \|P_2\|_F^2
 \le[16(K+1)^2]^2\sqrt{8L_6}\,s^5,
\]
versus the older coefficient \([64(K+1)^2]^2\), **16 times larger**. Therefore the leading source-centered fourth-moment envelope
\[
 L_4^{\rm NEW}
 =2[16(K+1)^2]^2\sqrt{8L_6}+56T
\]
is smaller than or equal to #672's original
\(L_4^{\rm OLD}
=2[64(K+1)^2]^2\sqrt{8L_6}+56T\).
The exceptional-endpoint \(L_E=8\sigma_3^{-1}\sqrt{L_6}\) coefficient decreases **27-fold**, and the relevant sufficient-s0 terms become smaller without affecting their powers in s. The fourth/sixth graph moment estimates themselves and the physical/source-original sixset bridge remain exactly as before.

**CAUTION:** This PR does NOT modify existing ancestor theorem constants, nor claim that all downstream manuscript constants and thresholds have been globally minimized or independently accepted. The replacement is a valid stronger input to the already established selector-to-moment step. Full global Branch A proof and external referee remain separate.

## 5. Independent check plan and actual ORIGINAL source scope

- \`research/hyp105_selector_positive_correlation.py\` implements the exact all-h algebraic sigma table, the exact rational r!-term joint priority survival formula for arbitrarily overlapping source conflict neighborhoods, the product lower bound, and an independent finite ACTUAL original-source W(3,2)/W(3,4) proper physical 2/3-path certificate. It recomputes every path's three ORIGINAL flag IDs, rejects conflicts or repeated original source points/lines, and accounts for BOTH diagonals and BOTH physical coordinate alphabets.
- \`research/test_hyp105_selector_positive_correlation.py\` independently enumerates **every one of the \(2^{10}=1024\) undirected graphs on five vertices** and brute-enumerates all five-factorial (=120) priority permutations for every nonadjacent target pair/triple. Compares the brute probability to (SELPLUS-RATIONAL) and the product floor; includes an explicit shared-neighbor strict-correlation witness. Directly enumerates the left and right coordinate cuts independently. Applies the all-h formulas on genuine original W32 with FIVE globally injected right-map reassignments and real coordinate-proper original source paths and on true W34 full/sparse/reassigned-g original cores, preserving true flag IDs and checking two/three-path acceptance bounds, not relying on the #672 source fixture as expected values. Tests invalid original ID sets fail closed.
- \`.github/workflows/hyp105-selector-positive-correlation.yml\` runs exact tests using Python 3.12 on GitHub-hosted Linux; then exact-head Research and INDEX must be checked before scientific acceptance.

This is a provable analytic strengthening of the selector lower bound, and a meaningful independent audit of a key all-h step. It does **not** replace independent scholarly referee of the original dense-core selection, moments or eventual root acceptance. Keep Draft and #230 OPEN_WITH_FORMAL_BLOCKER; no changes to main or parent Drafts.
