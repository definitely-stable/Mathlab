# HYP-105 / #230 — AA4-SELGAP: independently prove original path selector and sharpen the fourth-moment lemma

**Scientific Draft**, strict child of [#737](https://github.com/definitely-stable/Mathlab/pull/737), frozen parent HEAD \`2849789cdce665349476c5b585add370d88ef93f\`. This slice proves the all-order ORIGINAL-source random-priority + two-cut short-path selector, rederives its moment transfer, and removes a *genuine factor of two of slack* in the inherited fourth-moment bound. It never edits main or parent branches, closes issue #230, merges or claims a new ASET exponent.

**Quantifiers and provenance.** For EVERY dyadic original symplectic \(W(3,s)\), any complete separately globally pair-injective physical point/line maps \(f,g\), with arbitrary correlation, any adversarial deleted ORIGINAL incidence-ID set \(Z\), and any paired ORIGINAL core \(C\subseteq I\setminus Z\), let \(H_C\) contain BOTH actual physical opposite diagonals of each source flag in C. Let \(\Delta\) be its maximum actual physical degree and K its maximum genuine source pencil-conflict degree. Under the already-established source conflict definition, two different original flags conflict iff they share an original point and intersect as physical *line-pairs*, or share an original line and intersect as physical *point-pairs*. NO randomized relabeling of f/g occurs. The only randomness in the all-order argument is a temporary independently chosen priority permutation on C and independent fair binary colors on each physical coordinate of each typed alphabet.

## 1. ALL-ORDER short proper path source conflict lemma

Let \(\gamma=(v_0,\dots,v_r)\), \(r\in\{2,3\}\), be an ordered physical path in \(H_C\) such that its \(r+1\) first coordinates are all distinct and its \(r+1\) second coordinates are also all distinct. Each physical edge \(\{v_{j-1},v_j\}\) has exactly one ORIGINAL incidence-ID source owner \(i_j=(p_j,\ell_j)\), because globally injected complete physical point/line pair maps fix a unique rectangle owner. A source flag owns two mutually vertex-disjoint opposite physical diagonals, so two successive physical edges cannot come from one original flag. In fact all \(i_j\) are distinct: if \(p_j=p_k\), then the same physical first-coordinate pair \(f(p_j)=f(p_k)\) would repeat both of its physical symbols along the path, contradicting r+1 distinct first coordinates. Dually all \(\ell_j\) are distinct. Hence no two \(i_j\) are SOURCE-conflicting. This is a deterministic theorem, not an assumption about random label maps.

Define the union of the **closed** original conflict neighborhoods of the r owners as

\[
U_\gamma=\bigcup_{j=1}^r(\{i_j\}\cup N_J(i_j)),
\quad
b_\gamma=|U_\gamma|\in[r,r(K+1)].
\]

## 2. ALL-ORDER priority / physical color survival probability

The selector keeps an ORIGINAL source ID iff (i) it precedes **all its genuine original conflict neighbors** in a uniformly random source priority permutation, (ii) its actual f-pair physical endpoints have opposite independently random left bits, and (iii) its actual g-pair physical endpoints have opposite independently random right bits. When kept, its TWO true physical diagonals remain together, preserving one owner per selected edge.

Since the r original owners of the proper path are pairwise conflict-free, the **sufficient event** that these r owners occupy the FIRST r priority ranks within \(U_\gamma\) implies each of them wins every own source conflict. Among all \(b_\gamma!\) local permutations, exactly \(r!(b_\gamma-r)!\) satisfy this event. Its exact probability is

\[
\boxed{\mathbb P(\text{sufficient source-rank event})
=\binom{b_\gamma}{r}^{-1}.}
\tag{SEL-1}
\]

This is a **LOWER bound**, not a false exact equality for the probability the real selector retains all owners: there may be additional favorable permutations where outside neighbors interleave harmlessly.

The proper path's r left physical coordinate-pairs form a simple chain on r+1 DISTINCT left symbols; each edge must cross its own fair binary cut. Exactly TWO color assignments on those r+1 left symbols satisfy all r constraints, giving probability \(2^{-r}\). The r+1 distinct right symbols independently give another \(2^{-r}\). The source-priority event and both physical typed color cuts are independent. Consequently, for every fixed proper source path,

\[
\begin{aligned}
\mathbb P(\gamma\text{ fully retained})
&\ge\frac{4^{-r}}{\binom{b_\gamma}{r}}\\
&\ge\boxed{\sigma_r
=\frac1{4^r\binom{r(K+1)}{r}}}.
\end{aligned}\tag{SEL-2}
\]

This source-priority and color probability is valid for every genuine original core, arbitrary fixed correlated f/g, all adversarial original Z, and all \(r=2,3\). The separate numerical source oracle exhausts all \(2^{2(r+1)}\) local two-cut colorings (64 when r=2, 256 when r=3), and independently enumerates finite b! local permutations. It never invents independence between different physical paths.

## 3. ALL-ORDER endpoint Jensen and spectral moment transfer

For each ordered pair of actual physical vertices (u,v), let \(P_r(u,v)\) count the original CORE coordinate-proper physical ordered r-paths. Let \(G_\omega\subseteq H_C\) be the actual true source-priority + both-cut selected physical graph; let \(X_{r,\omega}(u,v)\) count the selected proper ordered r-paths. Linearity of expectation, which does NOT require distinct paths to be independent, gives

\[
\mathbb E X_{r,\omega}(u,v)
=\sum_{\gamma:u\leadsto v}\mathbb P(\gamma\text{ kept})
\ge\sigma_rP_r(u,v).
\]

Jensen and the fact that \(G_\omega\) is an actual subgraph of the fixed physical CORE graph imply

\[
\begin{aligned}
\sigma_r^2\|P_r\|_F^2
&\le\|\mathbb E X_{r,\omega}\|_F^2
\le\mathbb E\|X_{r,\omega}\|_F^2\\
&\le\mathbb E\operatorname{tr}(A_{G_\omega}^{2r})
\le\operatorname{tr}(A_C^{2r}).
\end{aligned}
\tag{SEL-3}
\]

The stronger **adaptive** source-neighborhood lower-weight \(4^{-r}/\binom{b_\gamma}{r}\) is also retained explicitly in the machine certificate. The proof uses ONLY expectation linearity and Jensen, never false event-wise independence.

For r=2,3 define exact reciprocal constants \(q_r=4^r\binom{r(K+1)}r\). Then

\[
\boxed{\|P_r\|_F^2\le q_r^2\operatorname{tr}(A_C^{2r}),\quad r=2,3.}
\tag{SEL-4}
\]

More importantly, the same expectation/Jensen inequality can be applied against the *uniformly bounded selected* graph moments rather than the full CORE trace, allowing the prior #729/#732 sixth-moment source-count input to transfer to proper path energy:
\(\|P_r\|_F^2\le q_r^2\sup_\omega\operatorname{tr}(A_{G_\omega}^{2r})\).
That supremum depends on the source conflict-free source selection ensuring every selected C6 is a genuine six ORIGINAL ID D6, as independently checked in #734 and again below.

## 4. SELECTED C6 source injection and exact sixth moment

On a genuine source conflict-free selected graph, two physical edges of a length-two physical path cannot return to the same first coordinate: the unique owners would then share an original point and a common actual physical right coordinate, which is exactly a prohibited source conflict. Same for the other physical coordinate. Thus no selected simple path of length 2 has a repeated typed coordinate. Across a selected length-three physical path, each physical edge reverses its OWN typed two-color bit, so endpoints at graph distance three cannot share any typed physical coordinate. Therefore every simple selected physical C6 has six distinct first coordinates and six distinct second coordinates (cyclic distances 1,2,3 exhaust all distinct vertex pairs on C6). It consequently has six distinct actual original flag owners and injects into one ORIGINAL positive D6 class sixset by the independent six-ID inverse of #734. This remains true if a downstream ordinary no-clone heavy chunk drops some physical diagonals: edge deletion cannot introduce new cycles or coordinate collisions.

For ANY simple physical BIPARTITE graph G, a closed sixwalk is either a genuine simple C6 (12 rooted oriented walks per unoriented cycle) or has an immediate reversal. The latter can be mapped to a closed fourwalk plus the position of one of six possible removed reversals and at most \(\Delta\) choices of its middle edge. Hence

\[
\boxed{\operatorname{tr}(A_G^6)\le12C_6(G)+6\Delta\,\operatorname{tr}(A_G^4).}
\]

Spectral Cauchy for nonnegative eigenvalue even powers gives
\(\operatorname{tr}(A_G^4)^2\le\operatorname{tr}(A_G^2)\operatorname{tr}(A_G^6)=2m\operatorname{tr}(A_G^6)\).
Finally Young \(6\Delta\sqrt{2mX}\le X/2+36m\Delta^2\) proves

\[
\boxed{\operatorname{tr}(A_G^6)\le24C_6(G)+72m\Delta^2.}\tag{SEL-5}
\]

With true source core \(m\le4s^4\), \(\Delta\le Ts\), and original surviving D6 source sixsets count below \(s^6\), (SEL-5) yields the preexisting uniform selected \(L_6s^6\) with \(L_6=24+288T^2\). This slice rederives the combinatorial closed-walk step and checks it directly on actual original selected W32/W34 physical graphs.

## 5. NEW sharp fourth moment: remove an unnecessary factor TWO

The inherited original source fourth-moment estimate used the safe bound
\[
\operatorname{tr}(A_C^4)
\le2\|P_2\|_F^2+2\Delta(Q_x+Q_y).
\]

But the exact genuine physical graph supports a strictly stronger identity. For every ordered endpoint pair (u,v), its two-step walk count \((A_C^2)_{uv}\) is either:
- in **proper** \(P_2(u,v)\), whenever its endpoints have DIFFERENT first and DIFFERENT second coordinates, or
- in **improper** \(B_2(u,v)\), whenever its endpoints share a first or second coordinate.

There is no overlap, since one physical diagonal edge always changes BOTH typed coordinates, and a two-step physical path with endpoint coordinates distinct in each factor automatically has three distinct symbols per factor. Therefore

\[
\boxed{
\operatorname{tr}(A_C^4)
=\|P_2\|_F^2+\|B_2\|_F^2
}\tag{SEL-6}
\]

**with equality**, not merely a factor-two inequality.

Every entry \(B_2(u,v)\) is at most \(\Delta\); its total mass is bounded by the actual physical two-walk typed return books \(Q_x+Q_y\), even when the same two-step return is counted in BOTH books. Thus

\[
\boxed{
\|B_2\|_F^2
\le\Delta\sum_{u,v}B_2(u,v)
\le\Delta(Q_x+Q_y).
}
\tag{SEL-7}
\]

Combining (SEL-6), (SEL-7) and selected-moment Jensen (SEL-3) with
\(m\le4s^4\), \(\Delta\le Ts\), \(Q_x+Q_y\le28s^4\), \(L_6=24+288T^2\), one obtains

\[
\boxed{
\operatorname{tr}(A_C^4)
\le L_4^{\rm SHARP}s^5,\quad
L_4^{\rm SHARP}
=q_2^2\lceil\sqrt{8L_6}\rceil+28T.
}
\tag{SEL-8}
\]

The historical safe constant from #736 was
\(L_4^{\rm OLD}=2q_2^2\lceil\sqrt{8L_6}\rceil+56T\);
therefore **the new L4 is EXACTLY HALF of the earlier sufficient bound**, independent of s, map correlation, c0/C0 values, source deletion and all GF5/physical path classification.

The sharper \(L_4\) can be substituted into the original mixed-book INTERNAL-BLOCKER bound from independently established #737:
\[
D^{\rm SHARP}=4\lceil\sqrt{B_0 T L_4^{\rm SHARP}}\rceil
\le D^{\rm OLD}.
\]
The original projected deletion radius \(\rho=1/(12q_3^2 L_6)\), the heavy C6 threshold T, the sixth moment L6, and universal source sixset \(\delta=c_0/2^{120}\) are UNCHANGED. The sufficient ORIGINAL all-h size threshold improves to

\[
\boxed{s_0^{\rm SHARP}=\max\{64,672T,(8E)^2,(8D^{\rm SHARP})^8\}.}\tag{SEL-9}
\]

## 6. Exact formal graph-constant samples and quantitative impact

All computations use integer ceil-sqrt and Python Fraction. Because the graph C6 supersaturation theorem supplies only existential \(C_{\rm graph},c_{\rm graph}>0\), *formal* rational inputs \(C_0,c_0\) are used only to test exact algebra; **none** is claimed to equal or bound actual published numerical graph constants. For three formal probes:

| Formal (C0,c0) | Old sufficient dyadic h0 | New sufficient h0 | Gain |
|---|---:|---:|---:|
| (1,1) | 876 | **872** | 4 powers of two |
| (2,1/5) | 906 | **902** | 4 powers of two |
| (7/3,1/17) | 912 | **908** | 4 powers of two |

The change is a genuine **16× reduction in the sufficient s threshold at the dyadic level for these formal inputs**, NOT proof at any practical geometry size, NOT a published graph constant estimate, NOT a new power or ASET exponent. The exact admissible deletion radius rho and GF(5) risk coefficient from #736 do not change.

## 7. Independent source and CI falsifiers

A new independent implementation [research/hyp105_original_selector_sharp_fourth_referee.py](../../research/hyp105_original_selector_sharp_fourth_referee.py) imports no older selector, Fourier or root-gate implementation. It reconstructs genuine W32/W34 source and complete globally injected fixed physical maps, original source pencil-conflict graph, both actual original physical diagonals, local source priority rank event, exhaustive two-factor color events, independently selected source graph and physical 4th/6th moments. Its path-first source-ID ownership and properness validator rejects repeated/adjacent conflicting owners. The actual selected source graph must be free of typed coordinate cherries; every selected physical C6 must inject into one six-ORIGINAL-ID D6 set. The test-only code verifies nonvacuous W34 positive D6 source seeds from #730 via the independent inverse of #734, retained by a **new** source priority + two cut selector.

All actual W32/W34 testcases check exact 2-walk proper/improper disjoint identity (SEL-6), typed return books Qx/Qy, \(\|B_2\|^2\le\Delta(Q_x+Q_y)\), Jensen lower weight, \(t_4^2\le2m t_6\), all sixth-walk inequalities, plus negative cases invalid source priorities, duplicate original IDs, illegal globally injected maps and malformed formal graph parameters. The prior #736 exact dyadic ledger is imported **ONLY by a separate test** to ensure the old constants have not drifted; the new proof module independently derives both old and sharp constants.

Dedicated GitHub-hosted Ubuntu 24.04 Python 3.12 workflow runs **ten tests** plus full source and three formal exact rational JSON certificate under fail-closed pipefail. Specialist, INDEX and full Research must be inspected on the **same final HEAD** before engineering acceptance.

## 8. Scientific STOP and next gate

This slice independently establishes the **original selector rank/typed-cut lower probability** and its **Jensen moment transfer**, rederives the selected graph simple-bipartite sixth-walk bound, and removes a genuine wasted factor of 2 in the original fourth-moment estimate. It does not independently derive every other core source collinearity/projection lemma in #730–#737, the ordinary graph C6 supersaturation constant values, or magically promote the root theorem from Scientific Draft. Root #230 stays **OPEN_WITH_FORMAL_BLOCKER**, with no merge, no closure, no ASET exponent.

**Next allowed mathematical task:** a complete independent adversarial review of the original HEAVY no-clone Caro–Wei chunk/supersaturation chain and a coherent all-h final theorem proof where every inherited lemma is explicitly cited and scoped. Do not accept root #230 solely because all finite tests or this improved source L4 ledger pass.
