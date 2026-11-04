# HYP-105 / #230 — AA4-SELMOM: original-ID-adaptive selector, weighted fourth/sixth moments and true D6 injection

**Scientific status:** a new elementary but nontrivial all-finite-order *adaptive* original-source probabilistic selection and weighted moment lemma, with a full independent source/physical-original W(3,2)/W(3,4) finite falsifier. It supplies an independent and strictly sharper version of the critical uniform \(\sigma_2,\sigma_3\) selector-to-moment mechanism in [#672](https://github.com/definitely-stable/Mathlab/pull/672) §§3–4, in combination with the Z-masked ORIGINAL FULL/CORE interface in [#728](https://github.com/definitely-stable/Mathlab/pull/728), on whose EXACT frozen HEAD \`8110617fcff7e396199da2171f0955743973d5d7\` this new draft is stacked. It is not a newly accepted complete universal all-h Branch A proof; it does not reproduce the external balanced C6 supersaturation input or the full #659 heavy-tail theorem. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**. No merge, no ancestor/main modifications.

## 1. All-order original-source theorem: adaptive priority, NOT independent path selection

Fix ANY dyadic \(s=2^h\) and the full genuine original W(3,s) incidence flags \(I\). Fix complete separately globally pair-injective original factor-pair maps \(f,g\) into the minimal physical \(K_a\); **arbitrary correlations** are allowed. Freeze arbitrary adversarial original-ID deletion \(Z\subset I\) and any retained paired ORIGINAL-flag core \(C\subseteq I\setminus Z\). Each retained original source incidence \((p,\ell)\in C\) contributes its TWO exact real opposite physical diagonal edges to the simple physical core graph \(H_C\) with adjacency \(A\).

On the set of actual ORIGINAL source ID flags in C construct the full exact source-conflict graph \(J_C\): two distinct original flags conflict iff they have the same source point and intersecting right \(g\)-pair supports, or the same original source line and intersecting left \(f\)-pair supports. Let \(K=\max\deg J_C\). A *proper* directed physical \(r\)-path for \(r=2,3\) has \(r+1\) pairwise different first physical coordinates and \(r+1\) pairwise different second physical coordinates.

**Proven true-original property:** every proper physical 2/3-path uses **r different ORIGINAL flags** and their original source point factors are distinct and original line factors are distinct. Repeating either source point or line repeats its fixed coordinate pair and violates properness. Thus the r original source flags are pairwise **nonconflicting in J_C** (this is not an independence statement about different physical paths).

Define the literal closed original source-conflict neighborhood union
\[
 B(\gamma)=\bigcup_{i\in S(\gamma)}\bigl(\{i\}\cup N_{J_C}(i)\bigr),
 \quad b_\gamma=|B(\gamma)|,\quad r\le b_\gamma\le r(K+1).
\]

Run exactly the SOURCE selector of #672: give all retained ORIGINAL flags i.i.d. continuous uniform priorities, keep each flag iff its priority precedes all its conflict neighbors in \(J_C\); **separately** choose uniform independent \(\{0,1\}\) binary colors of ALL left and right physical coordinate symbols, keeping each selected flag with both actual physical diagonals iff **both** of its fixed factor-pair supports are bichromatic. The result is a genuine physical source-owned subgraph \(G\subseteq H_C\) with adjacency \(A_G\).

For every proper path \(\gamma\), the sufficient priority event that its r distinct actual source IDs have the r earliest priorities among all b_\gamma IDs in B(\gamma) has EXACT probability
\[
 \Pr(\text{all r flags first among }B(\gamma))
    =\binom{b_\gamma}{r}^{-1}.
\]
This event forces every selected original path flag to precede every original source conflict neighbor, because all such neighbors lie in B and no two selected path IDs conflict. There is no need to assert that local-minimum selections of different paths are independent. The independent left/right binary physical coordinate cuts preserve all r SOURCE edges of that path with EXACT probability \(4^{-r}\): the two physical coordinate sequences are individually of length \(r+1\) with all entries different, and each must alternate across r consecutive edges, with exactly two alternating color assignments per side.

Therefore a rigorous path-specific selector lower bound is

\[
\boxed{\Pr(\gamma\text{ survives }G)\ge
 w_\gamma:=\frac{1}{4^r\binom{b_\gamma}{r}}.}
\tag{SELMOM-1}
\]

This probability is exact for the displayed **sufficient** event, not in general the full path-survival probability. It is at least the historical uniform selector coefficient since

\[
w_\gamma\ge
 \frac1{4^r[r(K+1)]^r}
 =:\sigma_r,\quad
 \boxed{\sigma_2=\frac1{64(K+1)^2},
 \ \sigma_3=\frac1{64\cdot27(K+1)^3}.}
\tag{SELMOM-2}
\]

The inequality is strict for every r≥2 at any actual valid path since \(\binom br<b^r\). This is a **strict strengthening** of the uniform scalar \(\sigma_2,\sigma_3\) lemma, not a change in its established power-law exponent.

## 2. NEW weighted fourth/sixth moment theorem (all finite original W(3,s))

For ordered physical endpoints u,v let \(\mathcal P_r(u,v)\) be all genuine original-source **proper directed** physical r-paths, and define

\[
W_r(u,v):=\sum_{\gamma\in\mathcal P_r(u,v)}
  \frac1{4^r\binom{b_\gamma}{r}},\quad
P_r(u,v):=|\mathcal P_r(u,v)|.
\]

As the selector's nonnegative integer entry \((A_G^r)_{uv}\) counts all selected r-walks, including each genuine surviving proper path, linearity of expectation alone gives
\[
\boxed{
 \sigma_rP_r(u,v)\le W_r(u,v)
 \le \mathbb E(A_G^r)_{uv}.
}
\tag{SELMOM-3}
\]

**Crucial:** no independence across paths is claimed or required. Jensen, summed over all ordered physical endpoints, and ordinary undirected symmetric adjacency trace identities imply

\[
\begin{aligned}
\boxed{
 \sigma_r^2\|P_r\|_F^2
 \le\|W_r\|_F^2
 \le \mathbb E\,\mathrm{tr}(A_G^{2r})
 \le \mathrm{tr}(A^{2r}),\quad r=2,3.
}
\end{aligned}
\tag{SELMOM-4}
\]

The final inequality is deterministic: G is physically a subgraph of the exact source-owned H_C, and each closed positive-length walk of G is also a closed walk of H_C. In particular the **adaptive** moment bounds are valid after arbitrary ORIGINAL-ID source Z deletion and arbitrary original f/g correlations without any all-h asymptotic premise. For actual computations the endpoint weights and both Frobenius squares are stored as full exact integer-rational fractions, never floating point or Monte Carlo samples.

This all-order adaptive inequality is **strictly stronger at the path-lower-bound level** than the uniform \(\sigma_r\) inequality used in #672, but does not by itself produce a uniformly better asymptotic exponent: \(\binom{b_\gamma}{r}\) may be of order \((rK)^r\).

## 3. Full-source cycle injection and independent six-motif structural proof

The random SOURCE priority winner set is an independent set of original flags in J_C. A pair of consecutive physical selected edges having equal first coordinate at the endpoints of a length-two path would force a repeated original point or a common source line/right coordinate conflict; those two source flags cannot both win the conflict selection. A completely analogous statement holds for second-coordinate cherries. Therefore the selected physical graph has no row/column two-step returns.

Every retained original physical flag also has bichromatic left and right physical coordinate pair labels. Along EVERY selected physical edge both left and right coordinate bit colors flip; hence a physical coordinate cannot repeat at **odd** path length. A simple physical 6-cycle can only repeat a coordinate at cyclic distance 2 or 3, and both cases have just been excluded. Each simple physical 6-cycle is thus coordinate-proper on all six original source-owned edges.

The six true original flag owners are pairwise distinct and use six original point factors and six original line factors. The six fixed left physical factor pairs f(p_i) form a **simple C6 on six left coordinate symbols**, and the six right factor pairs g(ell_i) form a **simple C6 on six right coordinate symbols**, with the **same owner cyclic order**. This is precisely the positive original D6 class of the historical seven-family GF(5) source model (not a projected/synthetic surrogate). Moreover one fixed original sixset can produce at most one unrooted, unoriented simple physical C6: its ordered left source-pair cycle is uniquely determined up to reversal/rotation, and consecutive left/right source-pair intersections uniquely fix the six actual physical vertices when an aligned physical cycle exists.

Thus, with \(D_{6,\bar Z}\) denoting the count of genuine original GF(5)-positive D6 sixsets avoiding deleted ORIGINAL source ID set Z, **pointwise on every selector outcome**

\[
\boxed{C_6(G)\le D_{6,\bar Z},}
\tag{SELMOM-5}
\]

including when C contains only a subset of all allowed original flags. No all-h random independence of original maps is used. The unit tests deliberately construct real W32 **positive** D6 source flags and choose priorities/left-right bichromatic colors that FORCE an actual original source-owned selected physical six-cycle, rather than merely observing empty random selected graphs.

## 4. Independent analytic moment estimate and exponent ledger

The original [#672](https://github.com/definitely-stable/Mathlab/pull/672) §4 also uses an elementary bound for any finite simple bipartite selected physical G with m physical edges, maximum physical degree Δ and C6(G) unrooted unoriented simple 6-cycles:

\[
\mathrm{tr}(A_G^6)
 \le 12C_6(G)+6\Delta\,\mathrm{tr}(A_G^4).
\]

Every non-simple closed length-six walk in a bipartite simple graph has at least one cyclic two-step return; marking one of six such returns and contracting it to a rooted closed four-walk yields at most \(6\Delta\,\mathrm{tr}(A_G^4)\) walks. Non-self-repeating simple 6-cycles contribute precisely 12 directed rooted walks each. By Cauchy on the real adjacency spectrum,
\[
\mathrm{tr}(A_G^4)
  \le \sqrt{\mathrm{tr}(A_G^2)\mathrm{tr}(A_G^6)}
  =\sqrt{2m\,\mathrm{tr}(A_G^6)}.
\]
Using \(6\Delta\sqrt{2m X}\le X/2+36m\Delta^2\) (Young) yields the conservative safe envelope
\[
\boxed{\mathrm{tr}(A_G^6)\le24C_6(G)+72m\Delta^2
              \le24D_{6,\bar Z}+144m_C\Delta_C^2.}
\tag{SELMOM-6}
\]
The first upper coefficient 72 is sharper than the parent 144 but the second formula intentionally agrees with #672's conservative envelope. It is valid even if the selected physical edges form only a tiny subgraph.

If \(\Delta_C\le Ts\), \(m_C\le4s^4\), \(D_{6,\bar Z}\le s^6\), \(K\le64\), then
\[
L_6=24+576T^2,\quad
\sigma_2^{-1}=64(65)^2,\quad
\sigma_3^{-1}=64\cdot27\cdot65^3,
\]
give
\[
\|P_3\|_F^2\le\sigma_3^{-2}L_6s^6,\qquad
\|P_2\|_F^2\le\sigma_2^{-2}\sqrt{8L_6}\,s^5.
\tag{SELMOM-7}
\]

For the **physical core** A, write \(A^2=P_2+B_2\) where B2 counts improper physical two-walks (source coordinate return). The original source-pencil equalities \(\ Q_x=2\sum_{p,y} R_C(p,y)^2\) and \(\ Q_y=2\sum_{\ell,x}R_C^{\vee}(\ell,x)^2\) are FULL 2-path counts with equal first/second endpoint coordinates respectively. Each B2 entry is at most Δ_C; \(\sum B_2\le Q_x+Q_y\). Hence
\[
\boxed{\mathrm{tr}(A^4)\le
 2\sigma_2^{-2}\sqrt{8L_6}\,s^5
 +2\Delta_C(Q_x+Q_y).
}
\tag{SELMOM-8}
\]
When the separately required ORIGINAL source book estimate \(Q_x+Q_y\le28s^4\) holds, this becomes the parent's core fourth moment
\[
 \mathrm{tr}(A^4)\le
 \underbrace{\bigl[2\sigma_2^{-2}\sqrt{8L_6}
                    +56T\bigr]}_{L_4}\,s^5.
\tag{SELMOM-9}
\]

The exact mixed original FULL/CORE blocker proof in the frozen #728 gives for its original source book B
\[
B\le B_0s^{23/4},\quad B_0=64\sqrt{(K+1)T},
\]
from the independent source collinearity factor \(F_1\le64s^{11/2}\) and the exact mixed FULL/CORE factor \(F_2\le32(K+1)Ts^6\), where the former is a separately necessary original generalized-quadrangle spectral input. Weighted Cauchy on two-step physical completions gives

\[
\boxed{I_{\rm internal}
 \le4\sqrt{B_0TL_4}\,s^{47/8},\qquad
 \frac{(23/4)+1+5}{2}=\frac{47}{8}<6.}
\tag{SELMOM-10}
\]

These analytic inequalities are now clearly separated into (i) NEW exact adaptive original-source selector/spectral transfer; (ii) classical elementary closed-walk estimates and true source-pencil return identities; (iii) independent original geometric prerequisites from #659/#672/#728 that must be accepted to assert *uniform* large-h estimates. A finite W32/W34 certificate does not alone validate (iii).

## 5. Actual genuine source finite falsifiers, CI and acceptance boundaries

\`research/hyp105_original_adaptive_selector_moments.py\` independently rebuilds original full W(3,2) and W(3,4) flags and independently verifies legal globally pair-injected complete original f,g and every retained original source ID, source conflict neighbors, physical diagonal owner multiplicity, actual proper 2- and 3-paths, exact union-closed-neighborhood b per path, \(W_2,W_3\) exact rational endpoint weights and Frobenius squares, physical core \(\mathrm{tr}(A^4),\mathrm{tr}(A^6)\), actual source pencil Qx/Qy and the improper/proper two-path fourth moment decomposition. It requires the strict weighted moment chain (SELMOM-4) for each genuine source fixture.

The independent tests reconstruct source conflict pairs **again** through the historical bucket oracle and independently reconstruct both physical diagonals, then cross-check against the new methods. They independently enumerate small priority permutations and all binary color assignments for r=2/3 to confirm exact \(1/\binom br\) and \(4^{-r}\) without probabilistic sampling. They construct a truly positive original W32 D6 source sixset for both lex and reverse-line complete physical maps, force its survival by original flag priority order and coordinate bichromatic cuts, and independently verify its actual selected physical cycle with the historical SOURCE D6 classifier. Other deterministic priority/color assignments on genuine W32 and sparse W34 are checked for spurious physical sixcycles, repeated real source ID owners or nonproper coordinates. Finite original W32 and W34 cores include arbitrary adversarial original source-ID deletions, while the full source global f,g are NOT resampled.

All arithmetic in the certificate is EXACT (rational strings / integer trace) and all malformed original source inputs fail closed. Workflow \`.github/workflows/hyp105-aa4-original-adaptive-selector-moments.yml\` uses GitHub-hosted Ubuntu only, requires actual complete proof JSON under \`set -euo pipefail\`, and runs independent negative corruption/frozen-certificate replay checks. **No local PC** needed.

The mathematical advance is genuinely **path-adaptive priority preservation**, stronger than the uniform selector used in #672; we do not assert a changed \(s^{47/8}\) exponent or claim to have proved every all-h geometric prerequisite. The ultimate remaining root scientific gate is independently accepting/correcting the heavy-tail geometric selection and external balanced C6 supersaturation transfer, combined with this and #728's already audited source/fullcore interface. Until then #672/#674/root #230 remain scientific Draft / OPEN_WITH_FORMAL_BLOCKER.


## 6. NEW exact independent tightening of original selector L6 and 47/8 numerical proof ledger

The companion independently developed \`research/hyp105_original_selector_symbolic_ledger.py\` verifies the elementary original source-selected graph sixth-moment coefficient **72** rather than the parent conservative **144**. This is *not* a claim that published graph supersaturation constants can be chosen as \(C_{\rm graph}=c_{\rm graph}=1\): it requires none of those constants. The proof is the explicit Young inequality

\[
6\Delta\sqrt{2mX}
\ \le\ \frac{X}{2}+36m\Delta^2
\quad (X\ge0).
\]

Combined with \(\ X\le12C_6+6\Delta\sqrt{2mX}\), we obtain

\[
\boxed{\ X=\operatorname{tr}(A_G^6)
\ \le\ 24C_6(G)+72m_G\Delta_G^2. \ }\tag{SELMOM-L6-TIGHT}
\]

For the #672 SOURCE CORE numerical hypotheses, the exact sufficient bound becomes \(L_{6,\rm tight}=24+288T^2\), compared with the old safe \(L_{6,\rm parent}=24+576T^2\). This halves the leading \(T^2\) coefficient; it does not claim a reduction in the exponent of s. The independent integer-only symbolic referee computes the tighter \(\ L_4=2\sigma_2^{-2}\sqrt{8L_{6,\rm tight}}+56T\), upper-enveloped by the ceiling of the integer square root, and the resulting four-position original mixed-blocker constant. For any formal integer source core cap \(K\ge0\) and physical cap \(T\ge1\), it verifies *without floating-point arithmetic* that the strengthened L4 and four-blocker constants never exceed their historical parent envelopes, and that

\[
 \boxed{\ \frac{11/2+6}{2}=\frac{23}{4},\qquad
 \frac{23/4+1+5}{2}=\frac{47}{8},\qquad
 6-\frac{47}{8}=\frac18>0. \ }
\]

It does **not** independently prove that the f,g geometric source core satisfies the prerequisite \(m_C\le4s^4\), \(\Delta_C\le Ts\), \(Q_x+Q_y\le28s^4\) or the full/core mixed original collinearity energy for every sufficiently large dyadic s. The prior #659/#672/#674 analytic provenance of those premises remains a distinct scientific review gate.

The tests independently enumerate **ALL 512 simple bipartite graphs** contained in \(K_{3,3}\) as algebraic negative falsifiers for BOTH \(\operatorname{tr}A^6\le12C_6+6\Delta\,\operatorname{tr}A^4\) and the new tightened moment inequality. These abstract six-vertex graphs are only independent universal *algebra* falsifiers — they are NOT substituted for the true symplectic original source. The same checks also run on SIX separately generated genuine original SOURCE-selector outputs on W(3,2)/W(3,4), built from actual original flag priorities, fixed globally injected f,g and both required physical coordinate color cuts. All source-selected graph inputs pass the true-original factor-pair provenance and bichromatic edge tests.

## 7. Actual ORIGINAL W32/W34 finite weighted source certificate results

The first hosted true-original specialized run [#41914849598](https://github.com/definitely-stable/Mathlab/actions/runs/41914849598) passed all six source priority/color/Jensen/D6 injection tests and strict machine-readable proof JSON. The permanent original full exact rational certificate is \`research/hyp105_original_adaptive_selector_moments_certificates.json\`, independently reproduced by eight permanent replay/tamper tests. The analytical tightened-L6 symbolic and six true-original selected graph evidence is retained in \`research/hyp105_original_selector_symbolic_ledger_certificates.json\`, with its own seven replay/tamper tests.

| Genuine symplectic ORIGINAL source / frozen global maps | Core original incidence IDs | Deleted actual original IDs | Max original flag conflict K | Actual proper physical 2-paths | Actual proper physical 3-paths | Exact true physical core \(\operatorname{tr}(A_C^6)\) |
|---|---:|---:|---:|---:|---:|---:|
| W(3,2), lex | 45 | 0 | 4 | 614 | 1,346 | 52,674 |
| W(3,2), reverse-line | 30 | 3 | 3 | 272 | 292 | 8,868 |
| W(3,4), lex | 205 | 15 | 3 | 3,042 | 9,622 | 109,480 |
| W(3,4), reverse-line | 164 | 14 | 4 | 2,168 | 5,304 | 85,748 |

For every row **both** new adaptive path moment Frobenius squares are computed as exact rational numbers and obey \(\sigma_r^2\|P_r\|_F^2<\|W_r\|_F^2\le\operatorname{tr}(A_C^{2r})\) for r=2 and r=3. No Monte Carlo approximate selector probability was substituted. For example, for genuine W(3,2) lex:

\[
 \|W_2\|_F^2=\frac{3493493}{203212800},
 \qquad
 \|W_3\|_F^2=\frac{310019889}{3283356876800}.
\]

A separate deterministic true physical selector **FORCES a selected positive six-coordinate simple C6** from an ORIGINAL historical source D6:
- W(3,2) lex: real original source flag IDs \(\{0,11,18,29,35,44\}\), **1** selected physical C6, all six true owner IDs distinct.
- W(3,2) reverse-line: real original source flag IDs \(\{1,8,17,18,40,42\}\), **1** selected physical C6, all six true owner IDs distinct.

This ensures the sixcycle-to-D6 original GF(5) bridge test is NOT merely vacuous because random priority/color selections often contain zero C6. Both actual source graph constructors and owner maps are independently checked against a preexisting separate source conflict bucket and physical diagonal oracle. The exact-sharp safe sixth-moment inequality on selected graphs has also been checked by a completely independent physical matrix-power implementation.

**Acceptance gates:** the GH-hosted specialist workflow must on its FINAL head pass all independent original geometry tests, complete source rational/moment proof replay, all 512 algebraic bipartite checks, the six actual selected true-original source graphs, all negative tamper tests and strict \`set -euo pipefail\` JSON verification. Full Research and INDEX workflows must also be green on that same HEAD. The all-h geometric source six-motif obstruction remains a separate pending scientific proof review, not replaced by test success.

## 8. What was independently proved and what remains

**New independently derived theorem:** path-adaptive retention probability and weighted original-source 4th/6th moment inequality (SELMOM-1)–(SELMOM-4), the conservative source D6 injection (SELMOM-5), and the true bipartite sixth-moment coefficient strengthening (SELMOM-L6-TIGHT) as universal discrete combinatorial statements. Their formulas were implemented and independently falsified on genuine original GQ source data.

**Still not newly proved in this slice:** uniform large-h existence of a source core satisfying #659/#674 heavy degree and all source-conflict caps for every f,g, source collinearity operator norm and full original geometric mixed source spectrum, numerical valid balanced graph C6 supersaturation constants, root all-h Branch A/B/C, any impossibility of deterministic specially chosen full GF5 ASET, or a new ASET exponent. The mathematically responsible next gate is independent line-by-line proof verification of the external balance/chunk supersaturation application in #659 and its exact original-source-heavy edge-to-six-positive-motif transfer, now that selector/moment and masked FULL/CORE interfaces have independent all-N proofs.
