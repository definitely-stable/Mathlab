# HYP-105 #230 — AA4-LOW-MOMENT-RANK: exact expected ORIGINAL source-selected edge mass and a fourfold better sixth/fourth energy transfer

**Status:** independently proved ALL-ORDER **LOW selected expected-moment** theorem, with a stricter **conditional** no-deletion Branch A root ledger. This is a strict Draft child of frozen [PR #778](https://github.com/definitely-stable/Mathlab/pull/778), parent SHA \`8123615546bb87b17ce60a6d0dacbcf0c23c68fa\`. No parent/sibling/main changes or merges; root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) is **OPEN_WITH_FORMAL_BLOCKER**, not PROVED_A. No new GF(5), B75, ASET strict exponent or numeric published C6 supersaturation constants.

**Precise novelty:** old #738/#745 independently proved one-global-source-selector rank+cut Jensen and the universal all-bipartite sixth-walk inequality. #771 strengthened owner survival by positive association. However their global LOW proof budgets unnecessarily replace **expected selected edge count** by the much larger maximum possible selected edge count. A single global selector permits an EXACT source-degree-weighted expectation, with one-quarter of the original paired-CORE edge maximum even under fully dependent selected-owner/path events. This slice derives a new **source-sensitive two-moment inequality** and propagates its all-h consequence through the genuine original LOW four-blocker/endpoint budget at the SAME H/K/R/T that #778 now uses. Unlike an additional rounding tweak, it removes a factor FOUR from the asymptotic sixth-moment T² coefficient and a factor FOUR from the leading proper 2path fourth-energy bound (after a second Cauchy across the shared selector distribution).

## 1. Genuine ORIGINAL physical graph, one global source experiment and exact expected edge mass

Fix even H≥8, any dyadic s=2^h≥2^H, the REAL symplectic W(3,s) ORIGINAL point/line incidence flags I, original point count V=(s+1)(s²+1), original incidence count N=(s+1)^2(s²+1), minimal pair alphabet a=min{b:binom(b,2)≥V}; and ANY two fixed globally pair-injective and arbitrarily correlated original f/g pair maps. Root Branch A needs Z=empty. Let C⊆I be the actual named paired LOW original source CORE from the FULL Q_T/J-degree pruning, with true original conflict graph J_C on those IDs, maximum FULL degree at most K, and physical H_C obtained by keeping both vertex-disjoint real diagonals of each flag.

**Each physical edge has exactly ONE ORIGINAL source flag owner** from the pair-injection of f/g. The uncut true paired CORE graph H_C has precisely m_C=2|C| real simple physical edges on full n=a² corners (including isolates), degree cap Δ≤Ts. Source selection is the SAME established priority+cut experiment, not a separate independent selection per path:

1. Give each retained ORIGINAL source flag u∈C ONE independent continuous uniform priority t_u. Keep u if and only if t_u is less than t_v for every v∈N_{J_C}(u). Neighbor events may be strongly positively correlated and the kept source flags form a genuine independent set in J_C.
2. Give EVERY actual first-coordinate symbol one independent fair binary bit and EVERY second-coordinate symbol a separate independent fair binary bit; ALL these bits are independent of source priorities. A priority-winning owner u=(p,ell) survives both cuts if its true pair f(p) is bichromatic in the first cut AND its true pair g(ell) is bichromatic in the second cut. A surviving owner retains **BOTH** original physical diagonals, not one arbitrarily sampled edge.

Even though different original owners may share f/g symbols and priority neighbors, for each FIXED owner u separately:

\[
\mathbb P(u\text{ priority winner})=\frac1{d_{J_C}(u)+1},\qquad
\mathbb P(\text{both typed cuts for }u)=\frac14.
\]

There is no need for ANY independence between different u's. Put the exact deterministic source rank weight

\[
\boxed{W_C:=\sum_{u\in C}\frac1{d_{J_C}(u)+1}.}\tag{ME-1}
\]

By linearity, and by EXACTLY two distinct physical owned edges per selected ORIGINAL flag, one obtains the **NEW exact universal identities**

\[
\boxed{
\mathbb E_\omega |E(G_\omega)|=\frac12 W_C,\qquad
\mathbb E_\omega\operatorname{tr}(A_{G_\omega}^2)=W_C,
\qquad W_C\le|C|\le N.
}\tag{ME-2}
\]

This holds for every true W(3,s), every fixed correlated f,g, any true paired original CORE C, every source J_C (not just its bound K), and WITHOUT any independence between retained edges, owners, 2paths, 3paths or cycles. Crucially, **the graph Gω is simple** and has only source-owned physical edges, so |E(Gω)|=2#selected ORIGINAL flags. The identity would be FALSE if each diagonal were separately selected, if owners were cloned, or if different paths used independent selectors.

The old all-ω pointwise inequality |E(Gω)|≤m_C=2|C| is still true; the new bound replaces it ONLY INSIDE EXPECTATIONS. Do NOT claim |E(Gω)|≤m_C/4 for each outcome; a favorable shared bit coloring may retain every original owner in C. The distinction between individual outcome and the global expectation is essential.

## 2. Strict source-sensitive sixth-moment theorem — no supremum over selector outcomes

Each Gω is a TRUE simple BIPARTITE physical graph because EVERY surviving first-coordinate pair crosses the first fixed binary cut. All its edges are from the fixed H_C and its physical maximum degree is ≤Δ. The independent all-simple-bipartite sixthwalk lemma (fully justified in #745) says for EACH realization

\[
\operatorname{tr}(A_{G_\omega}^6)
\le12\,C_6(G_\omega)+6\Delta\operatorname{tr}(A_{G_\omega}^4)
\le24\,C_6(G_\omega)+72\,|E(G_\omega)|\Delta^2.
\tag{ME-3}
\]

Here C6 is the number of **UNORIENTED ordinary simple cycles**, not the sixth trace. Justification: any nonsimple closed sixwalk in a simple bipartite graph contains an immediate reversal (6 possible marked positions); removing it leaves a closed fourwalk and at most Δ reinsertion choices. Then spectral Cauchy (tr A4)^2≤tr A2 tr A6=2m tr A6, followed by Young, yields ME-3. This does not apply to a nonbipartite uncut H_C; the source selector's coherent FIRST cut is load-bearing.

By the independently established all-h original proper C6→D6 six-original-incidence-ID inverse, because the selected ORIGINAL source owners are J_C-independent and both physical typed cuts were coherent, for **every one global outcome ω**,

\[
C_6(G_\omega)\le D_6(f,g).\tag{ME-4}
\]

This bound counts TRUE six distinct ORIGINAL incidence ID sets, and remains valid even if some parent HEAVY construction deletes edges. It is NOT inferred from small examples alone.

Now average ME-3 over the SAME SINGLE global priority+two-cut probability space, then insert the NEW **exact** ME-2:

\[
\boxed{
\mathbb E_\omega\operatorname{tr}(A_{G_\omega}^6)
\le24D_6(f,g)+36\Delta^2W_C.
}\tag{ME-5}
\]

Unlike the historical \(\sup_\omega\operatorname{tr}A_{G_\omega}^6\), ME-5 is a source degree-weighted **expectation**. This is sufficient for BOTH correct source-path Jensen transfers; they require E of a moment, not a pointwise sup. No path-event independence is used anywhere. In highly conflicted source J_C the exact W_C may be substantially smaller than |C| and ME-5 improves still further on a case-by-case basis.

## 3. A NEW exact Cauchy inequality across the one shared selector distribution

For any simple symmetric adjacency matrix, spectral Cauchy gives \((\operatorname{tr}A^4)^2\le(\operatorname{tr}A^2)(\operatorname{tr}A^6)\) for each outcome. Both even traces are nonnegative. Apply scalar Cauchy ACROSS the one global selector distribution:

\[
\boxed{
\big(\mathbb E_\omega\operatorname{tr}(A_{G_\omega}^4)\big)^2
\le\big(\mathbb E_\omega\operatorname{tr}(A_{G_\omega}^2)\big)
     \big(\mathbb E_\omega\operatorname{tr}(A_{G_\omega}^6)\big)
\le W_C\,\big(24D_6(f,g)+36\Delta^2W_C\big).
}\tag{ME-6}
\]

This is valid **without** \(\operatorname{tr}A^4\) or \(\operatorname{tr}A^6\) being constant over outcomes. It would be INVALID to move the expectation through a nonlinear square root as if E√X=√EX; the proof explicitly uses inequality E√(XY)≤√(EX·EY), not equality. The exact deterministic source degree-weight W_C remains available when only a local source is investigated.

For r=2,3 and a proper ORIGINAL physical rpath γ in C, its r edge owners are pairwise source-J nonconflicting and its two typed coordinate sequences separately have r+1 distinct symbols. #771's all-order positive-association theorem applies to the SAME global priority/bit experiment:

\[
p_\gamma:=\Pr(\gamma\text{ survives})
\ge\frac{1}{4^r(K+1)^r}=:q_r^{-1},\quad
q_2=16(K+1)^2,\ q_3=64(K+1)^3.
\]

Let P_r(u,v) be the uncut actual source coordinate-proper rpath endpoint count, and X_{r,ω}(u,v) the actual surviving proper rpaths in Gω. Linearity and entrywise Jensen (NO independence across paths) yield

\[
\boxed{
q_r^{-2}\|P_r\|_F^2
\le\|\mathbb EX_{r,\omega}\|_F^2
\le\mathbb E\|X_{r,\omega}\|_F^2
\le\mathbb E\operatorname{tr}(A_{G_\omega}^{2r}).
}\tag{ME-7}
\]

**NEW joint weighted result** from ME-5/6/7:

\[
\boxed{
\begin{aligned}
\|P_3\|_F^2
 &\le q_3^2\Big(24D_6(f,g)+36\Delta^2W_C\Big),\\
\|P_2\|_F^2
 &\le q_2^2\sqrt{W_C\,\Big(24D_6(f,g)+36\Delta^2W_C\Big)}.
\end{aligned}
}\tag{ME-8}
\]

This is a new **source sensitive** sixth/fourth energy interface. It is at least as good as using W_C=|C|, and in any real source with conflicts further improves it.

## 4. All-h uniform SOURCE N envelope and precise root threshold at R=33281

For s=2^h≥2^H, genuine ORIGINAL flag count is N=(s+1)^2(s²+1), so

\[
\frac{N}{s^4}
=(1+1/s)^2(1+1/s^2)
\le \nu_H:=(1+2^{-H})^2(1+2^{-2H}).
\tag{ME-9}
\]

At fixed even H=32, \(\nu_H\) is an explicit positive rational ~1+2^-31, **not** the physical alphabet A_H from sibling #776. It bounds SOURCE flags, whereas A_H bounds PHYSICAL vertices. Do not conflate them.

Preserve the exact same global frozen source maps, physical Q_T, source J_C, K=10, R=33281 from parent #778, true original minimal alphabet A_H and its physical 3walk lower \(W_3>w_{K,H}s^6\), with \(w_{K,H}=(4c_{K,H})^3/A_H^2\), \(c_{K,H}=7/8-4M_H/(K+1)\). Fix unknown—but existential and independent of the map—external ordinary simple C6 supersaturation constants C0,c0 once, with C0≥max(1,C_graph), 0<c0≤min(1,c_graph); do NOT assign C0=1 for an actual theorem claim. Choose ONCE

\[
R=33281,\quad T=\left\lceil(17/2)R^3C_0^3\right\rceil,\quad
\delta=c_0/R^6.
\]

In LOW with D6<δs6, since δ≤1, Δ≤Ts and W_C≤N≤ν_Hs4, ME-5 yields

\[
\boxed{
\mathbb E\operatorname{tr}(A_G^6)
\le\left(24+\left\lceil36\nu_HT^2\right\rceil\right)s^6
=:L_6^{\rm rank}s^6.
}\tag{ME-10}
\]

This is not claimed to hold pointwise for EVERY selected graph (the old L6point remains a valid separately stronger-scope bound). Importantly, ME-7 and ME-8 NEED ONLY this expected moment. Compared to parent #778 \(L_6^{\rm old}=24+153T^2\), the T² coefficient is 36ν_H≈36, rather than 153, yielding a >4.24× reduction in the leading coefficient.

For proper two-step path energy, ME-6 and ME-7 give

\[
\|P_2\|_F^2
\le q_2^2 \sqrt{\nu_HL_6^{\rm rank}}\,s^5.
\]

The full uncut original paired physical CORE fourth trace (NOT a selected graph trace) still satisfies the exact proper/improper orthogonal endpoint split from #738:

\[
\operatorname{tr}(A_C^4)=\|P_2\|_F^2+\|B_2\|_F^2.
\]

The inherited source physical coordinate-return bound \(\|B_2\|_F^2\le19Ts^5\) is a **separate all-h premise**; the new rank-moment argument neither re-proves it nor silently strengthens it. Therefore the improved sufficient original fourth coefficient is

\[
\boxed{
L_4^{\rm rank}
=q_2^2\left\lceil\sqrt{\left\lceil\nu_H L_6^{\rm rank}\right\rceil}\right\rceil
+19T.
}\tag{ME-11}
\]

Previous #778 used \(L_4^{\rm old}=q_2^2\lceil\sqrt{\lceil17L_6^{\rm old}/4\rceil}\rceil+19T\). Again the improvement comes from the expected trace2 and expected trace6 rather than two independent pointwise bounds.

### Propagate to genuine ORIGINAL endpoint/mixed-book budget with NO false proof promotion

Keep every other inherited ORIGINAL LOW interface unchanged: endpoint projection on FULL true W(3,s), original allowed A=I versus paired smaller CORE C; source-injective four physical inner blockers from #770; actual produced P3→BBo two-directed-path reverse uniqueness from #751; true physical coordinate improper bound \((111/2)Ts^5\). Preserve both genuine source Harris reciprocals q2=1936, q3=85184 and original source point/line geometry, all fixed correlated f/g. Replace only:

\[
\begin{aligned}
L_6&=24+\lceil36\nu_HT^2\rceil,\\
L_4&=q_2^2\lceil\sqrt{\lceil\nu_H L_6\rceil}\rceil+19T,\\
B_0&=\lceil\sqrt{360(K+1)T}\rceil\quad\text{(unchanged)},\\
E&=5q_3\lceil\sqrt{L_6}\rceil,\\
D&=4\lceil\sqrt{B_0TL_4}\rceil.
\end{aligned}\tag{ME-12}
\]

At the SAME fixed \(T\) and the SAME ALREADY-IMPROVED \(w_{K,H}\) choose \(\alpha=(1/64,1/64,15/16)\) and

\[
s_0=\max\left\{2^{32},64,
\left\lceil111T/(2\alpha_1w)\right\rceil,
\left\lceil(E/(\alpha_2w))^2\right\rceil,
\left\lceil(D/(\alpha_3w))^8\right\rceil
\right\}.\tag{ME-13}
\]

Thus the conditional original produced source BBo floor \(\frac12 w(1-\sum\alpha)s^6\) and HEAVY δ=c0/33281^6 are **UNCHANGED**; only the sufficient global original source size threshold is reduced. Conditional on all *remaining* named original source premises, the same three-case HEAVY/LOW root composition gives the original unweighted seven-disjoint-class \(S_s(f,g)\ge\delta s^6\) for every s>=s0 and every fixed f/g. This is **not** full independent acceptance of those inherited all-h original projection/mixed-book/source-inverse prerequisites.

Three **FORMAL ONLY** exact Fraction probes of the EXTERNAL unknown graph theorem constants, without pretending they are published numerical values:

| FORMAL (C0,c0) | #778 previous h0, pointwise moments | NEW expected-edge rank h0 | Dyadic powers gained |
|---|---:|---:|---:|
| (1,1) | 620 | **612** | 8 |
| (2,1/5) | 650 | **642** | 8 |
| (7/3,1/17) | 657 | **648** | 9 |

The needed root s0 is formally 2^8–2^9 times smaller at those **hypothetical** graph constant inputs. It is **not a numerical value for the actual graph theorem**, not a new power s^6, not a new GF5/ASET result, and not a statement about practical experimental geometry sizes. The published C_graph,c_graph remain existential.

## 5. NEW independent REAL source falsifiers, including ONE global non-vacuous rank/cut experiment

The standalone Python module \`research/hyp105_original_low_moment_expected_edges.py\` imports ONLY the genuine original symplectic W32/W34 incidence constructor from old #748, and NO previous rank/moment/HYP105 root/selector/HEAVY/LOW/GF5 calculator. It independently reconstructs original named incidence flags, full complete pair-injected lex/reverse/shift f/g and REAL two-diagonal physical ownership, original J_C pencil neighbors. Its source and tests include:

1. **Exact global priority+two-cut exhaustive experiment on true ORIGINAL W(3,2).** Pick a true original source subset containing BOTH a genuine J conflict edge and a genuine J nonedge. Enumerate ALL relative source priority permutations, and ALL GLOBAL binary colorings for each physically occurring first and second coordinate symbol, never independently reselect per path. For every outcome build real source-selected paired physical graph, count m, tr A², tr A⁴, tr A⁶ and ordinary unoriented C6 independently by integer sparse walk / cycle DFS, and then average with Fraction. Assert \(\mathbb E m=W_C/2\), \(\mathbb E\operatorname{tr}A²=W_C\), \((\mathbb E\operatorname{tr}A⁴)^2\le (\mathbb E\operatorname{tr}A²)(\mathbb E\operatorname{tr}A⁶)\), and \(\mathbb E\operatorname{tr}A⁶\le24\mathbb EC_6+36\Delta_C²W_C\). Deliberately check some J-degree >0; the exact expectation must NOT accidentally rely on all source owners being independent.
2. **Separate NONVACUOUS true ORIGINAL W(3,4) six-source-ID D6 seed.** Six independently checked genuine mutually J-independent incidence flags and globally pair-injective source factor labels have a TRUE physical C6 before cuts. Exhaust ALL GLOBAL typed symbol bit assignments to this six-owner source graph, selecting both original diagonals or neither for each owner; source priorities are irrelevant ONLY because these six flags are ACTUALLY independent in J_C (explicitly checked). Require positive selected physical C6 outcomes. Independently enumerate ALL coordinate-proper r=2/3 paths, check their exact bit-survival probability =4^-r under ONE shared coloring, compute endpoint \(\|\mathbb EX_r\|_F^2\) and compare to the actual expected selected fourth/sixth trace. These are exact finite probability experiments, not Monte Carlo or falsely independent per path.
3. **Original source energy and graph-first integer walks.** Independently compute tr A²/⁴/⁶ as sums of squared integer A^1/A^2/A^3 walk counts; enumerate unoriented simple C6 by real physical DFS modulo rotation and reversal, count actual selected edges and maximum degree; retain all true named original edge source owners and both diagonals; check the previous all-bipartite SW2 bound on each individual outcome while **only** using the strengthened new coefficient on its actual probability-weighted expectation.
4. **FULL exact all-h root arithmetic with real quantifier scope:** Fraction, integer isqrt, integer powers and explicit maxima only; independent recreation of #778 historical R33281/L6=24+153T²/L4=q2²ceil sqrt(17L6/4)+19T and the new shared selector expected formulas, checks same T, same external formal C0/c0, source K, α, original positive BBo, and fixed HEAVY δ. Invalid input, false ROOT promotion, illegal source maps and scope confusion fail closed.

An independent GitHub-hosted Ubuntu24 Python3.12 specialist must validate **20** unit tests, exact nonvacuous true W34 physical sixthcycle and one-global-selector exact certificate, with PR and branch triggers and JSON artifact. INDEX and full Research must succeed on the EXACT FINAL HEAD for engineering acceptance.

## 6. Scientific acceptance and the next REAL mathematical blocker

**Independently proved in this slice for ALL h:** the exact named ORIGINAL owner priority/typed two-cut selected-edge expectation, expected trace2 identity, rank-weighted expectation sixthwalk ME-5, Cauchy across the SAME global selector ME-6, and the resulting Jensen moment-transfer/quantifier-safe improved LOW L6/L4. These use existing separately proved all-bipartite SW-2 and source six-ID D6 inverse, not new external graph theorem constants or novel existence theorems.

**Still separately INHERITED and NOT fully accepted by this finite work:** complete all-h original GQ endpoint-good/bad physical mask under all correlated fixed f/g; four mixed FULL original A=I / smaller paired CORE C blocker books with degree and trace weights; exact original P3→produced BBo six-ID two-to-one inverse; and final root seven-positive-class proof-DAG scientific signoff. Any failure of these premises blocks root PROVED_A regardless of improved numerical LOW threshold. Do not merge stacked Drafts, edit previous PRs or close issue #230.

**Next allowed scientific step after this:** independent adversarial original FULL A versus CORE C four-blocker witness inversion and global endpoint-projection ledger (starting from the first unsupported all-h step, if any), followed by full seven-class proof DAG. Avoid further unneeded constant-only loops until those source topology interfaces have been signed off.
