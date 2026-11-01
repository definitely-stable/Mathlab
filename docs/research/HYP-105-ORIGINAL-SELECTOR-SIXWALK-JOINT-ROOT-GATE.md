# HYP-105 / #230 — AA4-SELROOT: integrate the PREVIOUSLY PROVED original priority-path selector and sharp sixth-walk bound into ONE exact all-h root gate

**Scientific Draft**, strictly stacked on FROZEN [#703](https://github.com/definitely-stable/Mathlab/pull/703), exact parent HEAD \`024c196fd2779a3ba0d1035c6bed65bf616044d2\`; no main or ancestor mutations, no scientific merge or issue #230 closure. Main conclusion: the full original heavy/dense gate in #702 deliberately retained TWO weaker, formally valid inputs, even though [#679](https://github.com/definitely-stable/Mathlab/pull/679) had already established strictly stronger proper-path **single-marginal** probabilities and [#686](https://github.com/definitely-stable/Mathlab/pull/686)/[#703](https://github.com/definitely-stable/Mathlab/pull/703) had already established the sharper true bipartite sixth-moment bound. This new slice is a mathematically justified **matched 2×2 all-h integrated propagation**, not a claim that either marginal or sixth-walk inequality was first discovered here. Source science remains \`OPEN_WITH_FORMAL_BLOCKER\` pending an external qualified reviewer.

## 1. Source/model invariants — no new independence premise

Fix the genuine ORIGINAL W(3,s), \`s=2^h>=64\`, V=(s+1)(s²+1) ORIGINAL points and V lines and N=(s+1)V distinct ORIGINAL incidence flag IDs. Fix complete separately pair-injective but arbitrarily correlated typed f,g on the minimal physical pair alphabet; NEVER randomize or independently remap them, never clone original source IDs or physical vertices. Each selected ORIGINAL flag owns BOTH physical diagonals. The prior original FULL source budget is exactly

\[
\varepsilon=\frac{1787}{4096}
<\frac7{16}-\frac{38245}{33554432}
\le\frac Ns^4-\frac12-\frac{C_s}{16s^4},\quad C_s=(s^2+1)(s^2+a-2).
\tag{S1}
\]

The improved heavy-tail original source-ID Caro–Wei fraction #697 remains \(\beta=5\varepsilon^2/(384+40\varepsilon)=15966845/6735233024\). **ALL four comparisons below keep the SAME heavy branch**: for actual positive, NUMERICALLY UNKNOWN ordinary graph supersaturation constants \(C_{\rm graph},c_{\rm graph}\) of Simonovits/Jiang–Yepremyan,

\[
T=\max\{1,\lceil2^{19}C_{\rm graph}^3/\beta^3\rceil\},
\quad\delta=\min\{1/8,c_{\rm graph}(\beta/32)^6\}.
\tag{S2}
\]

In the case \(\,D_6<\delta s^6\), the already-proved contrapositive heavy-tail argument yields the true ORIGINAL dense CORE with \(m_0\ge s^4\), \(\Delta_0\le Ts\), source conflict maximum degree \(K=64\), no change to FULL source geometric anchors.

## 2. Sharper original SINGLE proper path selector (previously proved in #679)

Give independently uniformly random strict continuous priorities to the actual retained ORIGINAL source flag IDs of the conflict graph \(H_{\rm src}\), with max degree K, then select each local minimum. Only after this, independently color the complete LEFT and RIGHT physical coordinate alphabets with unbiased binary colors and keep an ORIGINAL selected flag if BOTH of its physical factor pairs are bichromatic. Source f,g themselves remain fixed and may be maximally correlated.

For ONE physical coordinate-proper r-edge path (r=2 or 3), its true ORIGINAL owner IDs \(\{i_1,\ldots,i_r\}\) are pairwise nonconflicting and their left and right physical coordinate sequences each have r+1 distinct symbols. The original source priority exact integral on these nonadjacent owner flags has lower bound

\[
\Pr(\text{all }i_j\text{ priority minima})
\ge\prod_{j=1}^r\frac1{\deg(i_j)+1}\ge(K+1)^{-r}.
\tag{S3}
\]

**Proof without assuming local-minimum independence:** condition on each target priority t_i; for each *external* conflict neighbor w, it must exceed the maximum target neighbor priority. The exact conditional probability factor is \(1-\max(t_i:i\in T\cap N(w))=\min(1-t_i)\ge\prod(1-t_i)\). Multiplying over w and integrating the independent target priorities yields (S3), even if external conflict neighborhoods overlap arbitrarily. Shared neighbors actually increase the probability relative to the product lower bound.

For one coordinate-proper r-path, its TWO binary coordinate color constraints each have probability \(2^{-r}\), so their joint cut probability is exactly \(4^{-r}\), independent of priority selection. Hence the sharp proven pointwise marginal floor is

\[
\boxed{
\sigma_2=\frac1{16(K+1)^2},\qquad
\sigma_3=\frac1{64(K+1)^3}.
}
\tag{S4}
\]

The conservative inputs in #702 were instead \(1/[64(K+1)^2]\) and \(1/[64\cdot27(K+1)^3]\), respectively. Thus #679 improves the same original source fixed-path survival floors by factors 4 and 27. These hold for arbitrary legal correlated f,g.

**CRITICAL guard against an invalid proof:** [#695](https://github.com/definitely-stable/Mathlab/pull/695) proves that TWO different path survival events may have NEGATIVE covariance because their union of typed coordinate-pair constraints can contain an odd cycle, even though each path separately survives with positive probability. Therefore this proof DOES NOT multiply probabilities of two paths or assume positive association of whole-path indicators. For each ordered endpoint cell (u,v), first use **linearity of expectation over each fixed proper source path**, then Jensen on the nonnegative selected walk count:

\[
\sigma_r P_r(u,v)
\le\mathbb E(A_G^r)_{uv},
\quad
\sigma_r^2\|P_r\|_F^2
\le\mathbb E\,\operatorname{tr}(A_G^{2r}).
\tag{S5}
\]

The right-hand expectation is of the entire selected graph, not independent path events. This preserves the all-h all-map valid moment-transfer machinery of #672/#679.

## 3. Sharper sixth moment (previously available in #686 and independently audited in #703)

For any simple physical bipartite graph \(G\) with true maximum degree \(\Delta\), m edges, and ordinary unrooted unoriented simple C6 copies,

\[
\operatorname{tr}(A_G^6)\le24C_6(G)+72m\Delta^2.
\tag{S6}
\]

This is an independent elementary backtrack/Cauchy inequality, and #703 additionally verified its exact Möbius degeneracy identity on all 65536 labeled 4×4 bipartite graphs. The factor **72 is not new**.

Every actual source-conflict-free/two-typed-cut selected graph has \(C_6(G)\le D_6(f,g)\) by the genuine ORIGINAL six-ID source injection of #652/#699. In the dense branch \(D_6<\delta s^6\le s^6/8\), m(G)≤4s⁴ and \(\Delta(G)\le Ts\). Thus the stronger **still conservative** all-h selected sixth-moment envelope

\[
\boxed{L_6=24+288T^2}
\tag{S7}
\]

holds; the old #702 input was \(L_6=24+576T^2\). We retain the loose 24 constant for a rigorously matched audit; lowering it to 3 is unnecessary and would mix extra changes into the comparison.

## 4. Integrate with the SAME dense-core inequalities, unchanged original FULL/CORE blocker

The new propagation ONLY changes \((\sigma_2^{-1},\sigma_3^{-1},L_6)\). It explicitly preserves ALL other conservative root assumptions of #702, notably:

\[
K=64,\quad m_0\ge s^4,\quad
84Ts^5\ \text{improper threewalk loss},\quad
56T\ \text{fourth-moment CORE book term},\quad
B_0=15\sqrt{(K+1)T}
\tag{S8}
\]

with the **original FULL/source mixed blocking theorem** of #701. The FULL source geometric anchors are never required to remain among the CORE physical edge IDs, and the actual B/B-overlap original six-ID inverse is precisely two directed reverse paths per accepted produced sextuple (#677/#700).

Use positive exact integer upper coefficients

\[
\begin{aligned}
\widehat L_4&=2(\sigma_2^{-1})^2\lceil\sqrt{8L_6}\rceil+56T,\\
\widehat B_0&=15\lceil\sqrt{65T}\rceil,\\
E&=8\sigma_3^{-1}\lceil\sqrt{L_6}\rceil,\\
D&=4\lceil\sqrt{\widehat B_0T\widehat L_4}\rceil.
\end{aligned}\tag{S9}
\]

The actual dense original image count is bounded below by the UNCHANGED #702 proof scheme:

\[
2U_{BB,\rm produced}
\ge s^6/2-84Ts^5
-E s^{11/2}-D s^{47/8}.
\tag{S10}
\]

Set \(s=2^h\). The single sufficient joint original dense error gate is

\[
\boxed{\frac{84T}{2^h}
+\frac E{2^{h/2}}
+\frac D{2^{h/8}}\le\frac14.}
\tag{S11}
\]

The new standalone code verifies this in **EXACT rational arithmetic**, not binary floats. It bounds each irrational \(2^{-h/d}\) above by the integer \(d\)-th-root certificate with denominator \(2^{12}\), using a direct all-integer binary search for \(d=2,8\). The starting sufficient \(h_{\rm sep}\) follows separately budgeting all three errors \(\le1/12\); exact downward joint exploration yields an often smaller \(h_{\rm joint}\), then records the exact Fraction upper of each error and verifies their sum ≤1/4. Because the underlying **actual** analytic three losses decrease for increasing s, a successful dyadic \(h_0\) certifies every larger dyadic order without requiring a possibly rounded fraction sequence itself to be monotone.

The source heavy/dense dichotomy now yields, conditional on the independently established prior original source and graph supersaturation inputs:

\[
\boxed{
D_6(f,g)+U_{BB,\rm overlap}(f,g)\ge\delta s^6,\qquad
\delta=\min\{1/8,c_{\rm graph}(\beta/32)^6\}.
}
\tag{S12}
\]

NO real numerical \(h_0\) is asserted: positive \(C_{\rm graph},c_{\rm graph}\) remain existential and NUMERICALLY UNKNOWN.

## 5. NEW exact 2×2 matched ablation — distinguish what actually improves

The standalone \`research/hyp105_original_selector_sixwalk_joint_root_gate.py\` has no dependency on any prior root calculator. It recomputes the exact heavy T/delta once, and runs the four combinations below **with identical original source budget, K, heavy beta/T, mixed blocking B0, fourth-moment tail +56T and three error types**:

| Label | Proper path marginals | Sixth-walk term |
|---|---|---|
| \`baseline_702\` | conservative #702, \(\sigma_2^{-1}=64\cdot65^2,\sigma_3^{-1}=64\cdot27\cdot65^3\) | \(L_6=24+576T^2\) |
| \`selector_only_679\` | sharper #679, \(\sigma_2^{-1}=16\cdot65^2,\sigma_3^{-1}=64\cdot65^3\) | \(L_6=24+576T^2\) |
| \`sixwalk_only_703\` | conservative #702 | \(L_6=24+288T^2\) |
| \`joint_679_703\` | sharper #679 | \(L_6=24+288T^2\) |

Tests compare the matched old baseline EXACT integer inputs to the independently implemented [#702](https://github.com/definitely-stable/Mathlab/pull/702) calculator (in TESTS ONLY). They check the new selector constants against the independent #679 module; additionally, true-original W32/W34 original-ID fixed physical proper r-path sample checks are performed with #679's independent real source-provenance oracle (tests only). The new module separately enumerates all \(4!=24\) priority orders in a 3-target ORIGINAL source-conflict star, and all \(2^8=256\) typed coordinate color assignments. It finds priority survival=1/4, two-cut survival=1/64 and whole original proper-three-path survival=1/256 vs original degree-one safe floor=1/512. This is a direct finite falsifier of (S3)–(S5), NOT a finite-h extrapolation. It also enumerates an odd-cycle two-path parity constraint witness to assert **negative** covariance, explicitly prohibiting any shortcut through false pair independence.

**The hypothetical C_graph=c_graph=1 regression is TEST ONLY**, never a claim that these are genuine published Simonovits/Jiang–Yepremyan graph constants. The repository CI outputs all four h choices for that algebra test, with the shared exact original T and loss fractions; the markdown numeric comparison should be updated only after verifying those CI outputs. Any smaller h is a **sufficient** all-h threshold conditional on the named prior proofs, not a minimum possible optimal threshold or outside acceptance.

## 6. Scientific acceptance and STOP

The new combined gate is a technically meaningful all-h strengthening obtained by carrying ALREADY PROVED source-selector and sixth-walk lemmas through the SAME global root, not a new proof of those historical inputs, GF5 original six-ID classification or external ordinary C6 supersaturation. It does not independently verify the entire heavy-tail balanced chunk, original source-core deletion, B/B FULL-source anchor or colored GF5 acceptance chain. It does not justify R3/ASET exponent changes or assign any numerical published graph constants. Root issue #230 stays **OPEN_WITH_FORMAL_BLOCKER** pending a qualified external extremal-combinatorics proof referee. Never merge stacked scientific Draft PRs or change main without permission.

**Next genuine external-facing milestone:** consolidate #659/#672 through #703 as a single checkable original-source manuscript with named lemmas, exact provenance and open external theorem dependencies, ask an independent qualified human reviewer to challenge the all-h quantifiers, and respond to actual mathematical objections rather than generating more purely constant-only stacked research Draft PRs.
