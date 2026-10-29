# HYP-105 #230 — AA4-BA2: exact all-\(h\) joint accepted B/A kernel and full conditional second-moment identity

**Scope:** true original symplectic \(W(3,2^h)\), any \(h\ge1\), **arbitrary fixed complete globally injected original point pair map \(f\)**, and **one** globally injected original line pair map \(g\) drawn uniformly WITHOUT replacement, possibly conditioned on arbitrary frozen ORIGINAL source-line factors and their legal fixed physical pair images. Six **different ORIGINAL source incidence IDs** on both sides. Historical strictly-positive GF(5) class B-left/A-right, not a synthetic motif. This is an exact **all-\(h\) conditional second-moment identity**, **NOT** a universal lower bound on every *completed* correlated \(g\), not a root Branch A/B/C proof, not total \(R_3\), and not a new ASET exponent.

## 1. The precise target after #669/#670

Previous [#669](https://github.com/definitely-stable/Mathlab/pull/669) and [#670](https://github.com/definitely-stable/Mathlab/pull/670) prove a positive \(\Omega(s^6)\) FIRST moment \(\mathbb E_g U_{B/A}(f,g)\), uniformly in arbitrary fixed \(f\) and even arbitrary macroscopic frozen \(g_J\). To quantify its lower tail one must study TWO original sixsets at once under the SAME completed \(g\). Multiplying individual success probabilities would illegally assume independent right images of source lines and would ignore original source-line overlaps.

Earlier [#487](https://github.com/definitely-stable/Mathlab/pull/487) develops joint original D6 signature kernels: their shared line-cycle positions matter. For B-left/A-right, unlike D6, the right **A** requirement only says that the six physically distinct edge images form a simple 2-regular graph on six physical vertices. It does NOT constrain which of the six named original line factors occupy which of the six cycle edges. This symmetry permits an **exact 7-value** pair kernel indexed solely by the number of common original line-factor IDs.

## 2. Universal original-source sixset family and joint kernel

Fix the true original source incidence tensor and any complete physical f. Define \(\mathcal B_f(J)\) to be **the complete family of ORIGINAL six-incidence-ID sets \(Q\)** such that:

1. The original point factor multiplicity is B=(2,1,1,1,1), with six original flags and exactly five distinct source points.
2. Its left physical pair projection \(f\) has precisely six physical symbols of degree two, equivalently a repeated pair edge plus a coordinate-disjoint C4 on four other f point-factor pair edges.
3. The six ORIGINAL line factor IDs occurring in \(Q\) are all distinct and none is in the pre-frozen ORIGINAL source line set \(J\).

This family is deterministic, finite, and depends on \(f\), \(J\) and the **same true source flags**, but NOT on the remaining random right pair images. No two original sixsets are collapsed even if they happen to have identical sets of six original source line-factor IDs. The underlying historical classifier returns exactly B-left/A-right for \(Q\in\mathcal B_f(J)\) iff the six corresponding physical right pairs form a simple six-edge, six-coordinate 2-factor.

Put \(\mathcal P=E(K_a)\setminus g_J(J)\), \(m=|\mathcal P|=\binom a2-b\). Let \(\mathcal F_6(\mathcal P)\) denote the **SET** of unordered six-edge subsets \(F\subset\mathcal P\) whose graph is 2-regular on exactly six coordinate vertices; on those six coordinates the possibilities are one simple C6 or two disjoint C3. Define for \(0\le r\le6\):
\[
 N_r(\mathcal P)
 :=\#\{(F,G)\in\mathcal F_6(\mathcal P)^2:
                |F\cap G|=r\}.
\]
Both \(F,G\) are **ordered** as a pair of six-edge SETS. Define \((m)_k\) as the falling factorial, and \(p_r=0\) when \((m)_{12-r}=0\); otherwise
\[
 \boxed{
 p_r(\mathcal P)=
    \frac{N_r(\mathcal P)\,r!\,((6-r)!)^2}
         {(m)_{12-r}}.
 }\tag{BA2-KERNEL}
\]

**Proof.** Let \(Q,Q'\in\mathcal B_f(J)\), with \(L(Q),L(Q')\) their six ORIGINAL line-factor ID sets. Suppose \(r=|L(Q)\cap L(Q')|\). Because the actual complete right map \(g\) is injective, the six-edge physical images \(F=g(L(Q))\) and \(G=g(L(Q'))\) have intersection size **exactly r**. For each fixed ordered \(F,G\) with intersection r, the named r common ORIGINAL source line factors can be bijectively assigned to the r common physical pair edges in \(r!\) ways, and the \(6-r\) exclusive original source lines of Q and Q' each can be assigned to their respective nonshared physical edges in \(((6-r)!)^2\) ways. Conversely each valid common assignment determines uniquely the images of all \(12-r\) distinct ORIGINAL source-line factors. The uniform globally injected g completion makes every such ordered assignment to distinct unoccupied pair edges equally likely, with probability \(1/(m)_{12-r}\). Hence
\[
  \Pr_g(Q,Q'\text{ BOTH right A}\mid f,g_J)
    =p_r(\mathcal P).                   \tag{1}
\]
Crucially, source factor geometry and positions of common source lines in the two sixsets are IRRELEVANT to the *right A* event; only r enters. This is **not** true of aligned original D6, where relative cycle positions affect the sign/matching constraints.

In particular \(N_6=|\mathcal F_6|\) (identical right-edge sets) and
\[
p_6=\frac{6!|\mathcal F_6|}{(m)_6}
=\Pr_g(Q\text{ right A}\mid f,g_J),   \tag{2}
\]
even for two **different original incidence-sixsets** Q,Q' with the SAME six original line-factor IDs. These multiple genuine source sixsets must **not** be deduplicated.

## 3. The all-h exact full SECOND MOMENT (not just an anchored row)

Let
\[
 X_f(g;J)=\sum_{Q\in\mathcal B_f(J)}
 {\bf1}[g(L(Q))\in\mathcal F_6(\mathcal P)]
\]
be a rigorous **lower subcount of the actual historical accepted original B/A class** for completed maps g, because it deliberately restricts all six original line IDs outside J. For J empty, \(X_f(g;\emptyset)=U_{B\text{-left}/A\text{-right}}(f,g)\) exactly, because class B/A *requires* six distinct ORIGINAL line IDs (right A).

Let
\[
 H_r(f,J)=\#\{(Q,Q')\in\mathcal B_f(J)^2:
                 |L(Q)\cap L(Q')|=r\},\qquad0\le r\le6.
\]
These count **ORDERED** pairs of actual ORIGINAL incidence-sixsets, including distinct Q,Q' with identical six original line IDs; \(\sum_rH_r=|\mathcal B_f(J)|^2\).

By the exact pair probability identity (1) and ordinary linearity of expectation — no independent indicators —
\[
\boxed{
 \mathbb E_g X_f=|\mathcal B_f(J)|\,p_6(\mathcal P),
 \qquad
 \mathbb E_g X_f^2=\sum_{r=0}^6 H_r(f,J)\,p_r(\mathcal P),
}\tag{BA2-MOMENT}
\]
\[
\boxed{
 \operatorname{Var}_g X_f
 =\sum_{r=0}^6 H_r p_r
   -|\mathcal B_f(J)|^2p_6^2\ge0 .
}\tag{BA2-VAR}
\]
This is an **exact all-h full moment**, not an anchored overlap row or a heuristic iid pair model. All source information is isolated in the **seven exact original source line-support overlap coefficients** \(H_r\). All random-without-replacement right-image information is isolated in the seven physical pair-kernel coefficients \(p_r\). The two families live in their proper typed factors; the same ORIGINAL six-ID set Q is used on both sides. If the expectation is positive, Paley–Zygmund/Cauchy yields the rigorous conditional completion guarantee
\[
 \Pr_g(X_f>0\mid f,g_J)
 \ge \frac{|\mathcal B_f(J)|^2p_6^2}
          {\sum_rH_rp_r}.             \tag{3}
\]
More generally \(\Pr(X_f\ge\theta \mathbb EX_f)\ge
(1-\theta)^2(\mathbb EX_f)^2/\mathbb EX_f^2\) for \(0<\theta<1\).
A strictly positive probability of many motifs is **not** a universal pointwise lower bound for every completed correlated g, and (3) may be weak if variance is large.

## 4. A surprisingly small exact UNRESTRICTED all-a polynomial kernel

For J empty, \(\mathcal P=E(K_a)\), \(m=M=\binom a2\). A complete K6 has **exactly 70** six-edge twofactors: **60** connected 6-cycles and **10** unordered pairs of disjoint triangles.

Fix one representative first twofactor F of each type \(t\in\{C6, 2C3\}\) on original physical coordinate labels \(\{0,1,2,3,4,5\}\). For \(k=0,\ldots,6\), select k old physical vertices; choose the other 6−k as NEW distinct physical vertices in a canonically named \(\{6,\ldots,11-k\}\) set. Let \(A_{t,k,r}\) be the **exact integer** count of pairs (k-selected-old-subset, G six-edge twofactor on the union of the k old and canonical 6−k new vertices) such that F and G share EXACTLY r physical K_a pair edges.

Crucially \(A_{t,k,r}\) is a tiny FINITE integer tensor: over all k it requires only \(2\cdot 2^6\cdot70=8960\) second-factor tests. Because every connected six-cycle F is isomorphic and every two-triangle F is isomorphic, this canonical calculation is independent of the chosen representative. The number of ordered original physical factor pairs F,G with r common physical pair edges in \(K_a\) is then, for **EVERY integer a≥6**,
\[
 \boxed{
 N_r(K_a)=\binom a6
 \sum_{t\in\{C6,2C3\}}n_t
 \sum_{k=0}^6 A_{t,k,r}\binom{a-6}{6-k},
 \quad n_{C6}=60,\ n_{2C3}=10.
 }\tag{BA2-POLYNOMIAL}
\]
Terms with \(6-k>a-6\) vanish. The factor \(\binom a6\) chooses six physical vertices for F; \(n_t\) chooses its physical 2factor on them; the remaining factor chooses the additional 6−k physical vertices for G, while \(A_{t,k,r}\) selects which k coordinates are shared and all 70 valid possible G shapes on those six vertices. The sum is **exact**, without diagram overcount or finite-h extrapolation. The identity \(\sum_rN_r=[70\binom a6]^2\) holds exactly; \(N_5=0\) (two distinct 2regular six-edge graphs cannot differ by exactly one physical edge). In particular the right **all-h unrestricted** physical pair kernel is obtained by substituting (BA2-POLYNOMIAL) into (BA2-KERNEL), with seven rational values \(p_0,\ldots,p_6\), no expensive enumeration of all \(\binom a6\) factor sets.

For nonempty frozen J, (BA2-KERNEL) and (BA2-MOMENT) remain **exact for every physical forbidden pair SET** \(g_J(J)\), but the pair-count coefficient \(N_r(\mathcal P)\) can depend on the actual FORBIDDEN physical K_a edges, not only their number b. This slice provides an **ALL-a exact one-frozen-edge specialization** proved in Section 5, and independent direct tiny-physical-alphabet oracles for a=6,7 with arbitrary TWO forbidden edges. It does NOT falsely claim that the unrestricted closed polynomial applies after TWO or more arbitrary right-edge deletions, nor a general all-a fast multi-frozen-F evaluation. The all-h polynomial is specifically for J empty.

## 5. NEW: exact all-h one-frozen-source-line *kernel invariance*

The independent CI discovered a wrong test assumption: on genuine W32, freezing one original line's physical right pair edge did **not** change any of the seven conditional right A/A pair probabilities for original candidate sixsets that avoided this line. This is NOT a coincidence of W32.

For ALL physical alphabets \(a\ge6\), any single frozen physical edge \(e\in E(K_a)\), let \(M=\binom a2\). Every ordered pair \((F,G)\) of physical six-edge 2factors with \(|F\cap G|=r\) occupies exactly \(12-r\) different physical K_a pair edges in the union \(F\cup G\). The full symmetric group \(S_a\) acts transitively on the **individual physical pair edges** \(e\in E(K_a)\) while preserving the class \(|F\cap G|=r\). Therefore the number of such ordered 2factor pairs containing ANY fixed \(e\) is precisely
\[
 \frac{12-r}{M}N_r(K_a).
\]
Every numerator here is an exact integer by orbit counting. Thus
\[
\boxed{\quad
N_r(K_a\setminus\{e\})
   =N_r(K_a)\,\frac{M-12+r}{M}.\quad}\tag{BA2-ONE-FROZEN}
\]
With \(b=1\), \((M-1)_{12-r}=(M)_{12-r}(M-12+r)/M\); hence the factors cancel:
\[
\boxed{\quad
p_r(K_a\setminus\{e\})=p_r(K_a)
\qquad(\forall a\ge6,\ r=0,\ldots,6).\quad}\tag{BA2-ANCHOR-INVARIANCE}
\]

This proves **exact all-h conditional pair-kernel invariance after fixing ONE ORIGINAL right source line pair label** for any allowed original W(3,s), any complete fixed point map f, and any choice of frozen original line factor and legal physical edge image, provided counted original sixsets avoid that original line factor.

**Crucial distinction:** the ORIGINAL source candidate family \(\mathcal B_f(\{\ell\})\) does SHRINK when a particular source line \(\ell\) is excluded; its size and overlap histogram \(H_r\) can change. The theorem does NOT say the unconditional total B/A second moment is unchanged after removing candidates. It says only the right conditional *kernel* \(p_r\) for each fixed pair of eligible source sixsets is unchanged.

The K6, K7 and K8 direct independently enumerated physical forbidden-single-pair 2factor pair kernels reproduce (BA2-ONE-FROZEN); the symbolic formula is exact for arbitrary much larger a and does NOT depend on computational extrapolation. This also explains why the earlier test expecting one-frozen \(p_r\neq p_r(\emptyset)\) was an invalid scientific assumption: it is refuted by a general group-action proof, not by rounding.

## 6. Implemented independent falsifiers and genuine original W32 certificates

- \`research/hyp105_allh_BA_overlap_second_moment.py\`: enumerate 70 K6 2factors, derive exact two-isomorphism-type \(A_{t,k,r}\), and evaluate seven unrestricted \(N_r(K_a)\) for arbitrary integer \(a\ge6\), exact Fraction \(p_r\). Direct frozen-F finite oracle for a=6,7. Construct genuine W32 source B sixsets from the EXISTING historical all-original-incidence-ID selected_left_six enumerator, and build full original-source overlap H_r using six-bit original LINE ID supports with integer multiplicities (do not collapse different Q with same six source lines). Exact E, E², Var and Paley lower.
- \`research/test_hyp105_allh_BA_overlap_second_moment.py\`: independently enumerate all K6, K7 and K8 six-edge 2factors and directly count ordered physical factor-pair intersections against the two-template all-a formula; separately test arbitrary frozen 1/2 physical pair edges for K6, K7; confirm \(p_6\) equals exact one-event probability, nonnegative variance and independently sourced original W32 historical f=lex and reverse-line full sixset second moments including a true frozen original line; original IDs and malformed cases fail closed. No external random seed, Monte Carlo or floating-point estimates.
- \`.github/workflows/hyp105-allh-BA-pair-kernel.yml\`: dedicated Python 3.12 GitHub-hosted fail-closed exact test pipeline. Once exact SHA CI passes, pin the numeric W32 conditional second-moment certificates and publish the exact evidence on issue #230. No modification of historical source or parent Draft PRs.

### Exact independently source-checked finite W(3,2) conditional second-moment certificate

The historical original source-ID left B generator enumerates **10,935** W32 left-B sixset candidates. Exactly **5,000** of those six-incidence sets have SIX distinct original right source line-factor IDs, and therefore belong to the original B/A conditional indicator family \(X_f\) for either W32 lex or reverse-line scenario (they have the same fixed physical point map f). The exact **full source** overlap profile, with ORDEREDED original candidate pairs, is:
\[
(H_0,\ldots,H_6)
=(444340,\ 3812726,\ 9229530,\ 8297702,\
 2865426,\ 339960,\ 10316),\quad
\sum_rH_r=5000^2.
\]
Note \(H_6=10{,}316>5{,}000\): different ORIGINAL six-incidence-ID sets can have the same SIX original line-factor IDs. Collapsing their masks would corrupt both mean and variance.

Directly enumerated physical K6 right 2-factor ordered-pair coefficients:
\[
 (N_0,\ldots,N_6)=(300,720,1710,1200,900,0,70),
 \qquad\sum_rN_r=70^2.
\]
Inserting these exact independent source/physical coefficients in the all-h identity gives for a uniformly random COMPLETE legal original right pair-label injection g:
\[
\begin{aligned}
\mathbb E_g X_f &= \frac{10000}{143},\\
\mathbb E_g X_f^2&=\frac{2142290}{429},\\
\operatorname{Var}_g X_f&=\frac{6347470}{61347},\\
\Pr_g(X_f>0)&\ge\frac{30000000}{30634747}
                    \quad\text{(exact Paley lower, about 97.9%)}.
\end{aligned}
\]
This last inequality is a mathematically rigorous statement about the **uniform-completion ENSEMBLE** for that fixed true W32 point injection, not the particular deterministic reverse-line or lex complete right injection.

Fix **ONE ACTUAL original source line factor**, with its own genuine right physical pair edge from the W32 model, and remove all source B sixsets using that original line. The resulting true-source conditional subfamily has exactly **2,736** different ORIGINAL six-incidence-ID sets and the exact support-overlap profile
\[
(H_0,\ldots,H_6)
=(74064,848242,2555168,2748138,1104102,150614,5368),
\qquad\sum_rH_r=2736^2.
\]
The *physical pair kernel probability* \(p_r\) is IDENTICAL to its unrestricted version, while the actual physical 2factor pair counts decrease to \((60,192,570,480,420,0,42)\). Consequently the exact conditional second moments for the restricted source subfamily are
\[
 \mathbb E_g X_f=\frac{5472}{143},
 \quad
 \mathbb E_g X_f^2=\frac{12217264}{8085},
 \quad
 \operatorname{Var}_g X_f=\frac{703947536}{15030015},
\]
\[
 \Pr_g(X_f>0\mid g_{\{\ell\}})
 \ge\frac{1375496640}{1419493361}
 \quad\text{(exact Paley lower, about 96.9%).}
\]

Every integer coefficient and rational certificate here is computed by historical-original-source flags AND independently brute-enumerated physical pair factors, then **pinned exactly in regression tests**. They prove neither all-h concentration nor positivity for every particular legal completed correlated g. Because this section compares two different original sixset families (with and without excluded source line), the change in \(H_r\) is NOT an additional physical-kernel covariance term.

## 7. Sharp statement of what remains open

The exact 7-value kernel reduces variance to \(\sum_r H_rp_r-(\sum_Q1)^2p_6^2\) for arbitrary genuine original W(3,s), f. It does **not** bound the size of **source** support-overlap coefficients \(H_r\) uniformly in arbitrary f at all h and cannot alone show concentration, even for random g, much less prove a lower bound for EVERY deterministic correlated completed g. The critical next analytic tasks are to bound \(H_r\) using true GQ source incidence geometry and physical f injectivity, and then find a *deterministic* same-map compensation mechanism across all seven classes or an infinite sub-sextic counterfamily. As previous historical finite W32 fixtures have actual D6=0 under fixed g despite a positive annealed D6 mean, no Jensen/Paley implication may be upgraded to a universal root all-g claim.

**Status:** mathematical partial all-h exact joint and second-moment identity, independent exact finite source/physical checks, root remains **OPEN_WITH_FORMAL_BLOCKER**. Independent scientific referee required for mathematical acceptance separately from green CI.
