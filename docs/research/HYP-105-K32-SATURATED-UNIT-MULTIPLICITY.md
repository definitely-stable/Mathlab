# HYP-105 / #230 — AA4-K32SAT1: saturated-parent unit multiplicity for accepted ORIGINAL D6

**Scientific verdict: a scoped all-\(h\) theorem; root HYP-105 #230 remains OPEN_WITH_FORMAL_BLOCKER.** This improves the factor-six two-source-incidence exchange bound of stacked Draft PR #663 **to factor ONE** for a specifically defined family of **saturated** \(K_{3,2}\) blocks in ONE AND THE SAME original-source-ID selected physical graph. It does not imply that such blocks have positive fresh-neighbor mass uniformly over all correlated maps.

## 1. Exact assumptions and prior theorem

Let the source be the TRUE original symplectic \(W(3,s)\), \(s=2^h\). Point and line labels \(f,g\) are complete, separately globally injective pairs of physical coordinate symbols and may be **arbitrarily correlated**. Let \(G\subseteq H(f,g)\) be a coherent physical graph obtained from whole ACTUAL original incidence IDs, with **both** physical diagonals retained, a source-pencil-conflict-free selected ID set, and **both** typed coordinate 2-cuts, as constructed in PR #659. Each physical edge has exactly one true-original incidence-ID provenance.

An actual physical \(K_{3,2}\) block is a set of five corners, three hubs \(U=\{h_0,h_1,h_2\}\) and two frees \(Z=\{z_0,z_1\}\), with **exactly six** hub/free cross-edges, all five first coordinates distinct and all five second coordinates distinct. Its six physical edges give six **distinct** ORIGINAL incidence IDs \(F\). Such a block is called **saturated in G** if for every hub pair \(i<j\),

\[
N_G(h_i)\cap N_G(h_j)=Z.
\]

This definition is strictly relative to **one selected G**, not to the full H. The family \(\mathcal{K}_{\rm sat}(G)\) is the set of DISTINCT actual six-ID source sets \(F\) of these saturated blocks. Physical complementary paired diagonals, potentially lying in the opposite parity component, are kept and verified.

Parent [AA4-K32X2, Draft #663](https://github.com/definitely-stable/Mathlab/pull/663), independently proved for every such \(F\) on the SAME full \(f,g\):

\[
\mathcal E_2(F)
=\{F':\text{one of seven accepted ORIGINAL GF5 six-ID classes},
\;|F\setminus F'|=2\}
\]

contains **only accepted D6**, and

\[
|\mathcal E_2(F)|=2\sum_{i<j}|W_{ij}^H(F)|,
\]

where \(W_{ij}^H(F)\) are actual common neighbors of physical hubs \(h_i,h_j\) in the FULL H whose first AND second physical coordinates avoid all five occupied hub/free coordinate symbols. These are TRUE-source physical neighbors; no synthetic edges or independent-f/g averaging. Parent #663 also proved the global multiplicity \(\sum_F|\mathcal E_2(F)|\le6D_6\) for arbitrary, not necessarily saturated, K3,2 blocks, with genuinely sourced K3,3 sharpness.

## 2. NEW all-h theorem: no two saturated source parents per accepted D6

**Theorem AA4-K32SAT1.** For ANY fixed complete globally separately injected correlated \(f,g\) on genuine \(W(3,s)\), ANY coherent selected graph \(G\) above, and its saturated source-sixset family \(\mathcal K_{\rm sat}(G)\), the accepted original sets \(\{\mathcal E_2(F):F\in\mathcal K_{\rm sat}(G)\}\) are **pairwise disjoint**. Thus the following *exact* positive population identity and *stronger* same-fixed-map lower bound hold:

\[
\boxed{
\left|\bigcup_{F\in\mathcal K_{\rm sat}(G)}\mathcal E_2(F)\right|
=\sum_{F\in\mathcal K_{\rm sat}(G)}|\mathcal E_2(F)|
=2\sum_{F\in\mathcal K_{\rm sat}(G)}\sum_{i<j}|W_{ij}^H(F)|
\le D_6(f,g)\le S_{\rm seven}(f,g).
}
\]

The coefficient **ONE** instead of **SIX** is valid **ONLY** for saturated K3,2 blocks simultaneously present in the SAME selected graph. This is NOT a stronger claim for an arbitrary collection of K3,2 parent blocks in the FULL H, where the sharp factor six from #663 still applies.

### Proof — uniqueness by a third selected common neighbor

Suppose a single accepted original D6 six-ID set \(F'\) belongs to \(\mathcal E_2(F_1)\cap\mathcal E_2(F_2)\) for two different saturated source parents \(F_1,F_2\subseteq E(G)\).

By the prior proved original source incidence-ID-to-physical-rainbow-C6 bijection #652, the accepted \(F'\) reconstructs a **unique** simple physical rainbow six-cycle \(C\) in the FULL H. By #663's exact extension classification, for each parent \(F_i\) the new physical vertex \(w_i\) of that cycle is removed and its **other five corners** give the parent \(K_{3,2}\): all three corners in one alternating parity side of \(C\) are the hubs, and the other two are the frees. The six parent edges are the entire \(3\times2\) cross-edge block on these five vertices, and they are **present in G**. The other source-paired physical diagonals in G do not weaken any of these inclusions.

If \(w_1=w_2\), the parent is uniquely determined by the four-edge path of \(C\) and its two obligatory cross edges, so \(F_1=F_2\). Because we supposed distinct parents, \(w_1\ne w_2\).

If both \(w_1,w_2\) lie in the **same** alternating side of \(C\), then the two corresponding \(3\times2\) parent edge sets combine into a FULL physical \(K_{3,3}\) on the six C6 vertices. Hence each pair of the first parent's three hubs has a **third common neighbor in G** distinct from its two frees, contrary to saturation.

If the two removed vertices lie in **opposite** alternating sides of \(C\), then the second parent's three hubs are the first parent's three frees, and its two frees are two of the first parent's hubs. Its six selected edges join those two first-parent hubs to the **third** vertex of the second parent's hub side, which is exactly the one C6 corner absent from the first parent's frees. Thus at least one pair of the first parent's hubs has a **third common neighbor in G**, again contradicting saturation.

Both possibilities fail; therefore two different saturated parents in a single G can never extend to the SAME ORIGINAL accepted D6. Their accepted source sixsets are disjoint, proving the equality and the coefficient-one transfer. \(\square\)

### Stronger necessary obstruction for any hypothetical low-seven-class family

If \(\{(f_s,g_s)\}\) were legal fixed correlated full maps with \(S_{\rm seven}(f_s,g_s)=o(s^6)\), then **for every coherent original-source selected graph \(G_s\)**,

\[
\boxed{
\sum_{F\in\mathcal K_{\rm sat}(G_s)}
\sum_{i<j}|W_{ij}^{H_s}(F)|=o(s^6).
}
\]

This is NOT a universal bound on the number of saturated blocks. A selected graph may contain many saturated K3,2 blocks with zero fresh FULL H common neighbors, in which case the left-side extension mass is zero and the theorem gives no accepted source motifs. The result is a precise all-h obstruction to strong two-flag compensation from such blocks, not proof that \(S_{\rm seven}=\Omega(s^6)\).

## 3. Independent exact finite original-source checks

New finite \`research/hyp105_k32_saturated_unit_multiplicity.py\` reuses parent #663's independent, classifier-checked exact radius-two source-ID extension census, but builds the saturation set by a NEW **selected-graph only** pair-codegree inverse-posting oracle:

1. Rebuild the genuine source \(W(3,2)\) or \(W(3,4)\); independently validate full globally injected point/line pair label maps and source incidence IDs.
2. Verify the selected original IDs have no pencil conflicts, construct **both** valid typed 2-cuts and invoke the exact #659 independent \`verify_selected\` source-ID/GF5 verifier. Ensure both physical diagonals of each selected original ID are present.
3. Count precisely the saturated 3-hub/2-free blocks with equal original actual selected pair-common-neighbor sets of size two, and reject any coordinate-injective violation.
4. Build the FULL 425-source-flag W(3,4) physical H on the **same f/g**, enumerate each saturated parent's exact 2-flag accepted D6 extensions via the source-ID-provenance and historical GF5 classifier, and **independently enforce global zero overlap** of accepted original source sixsets.

A structurally independent physical-only exhaustive falsifier checks **ALL 512** \(3\times3\) edge-subgraphs: for each of the six physical C6 of a full \(K_{3,3}\), at most one source-free saturated candidate parent can have four common physical edges with that C6 and its two required completion chords in the same selected graph. These graphs are used **ONLY** to check the purely combinatorial uniqueness; the actual scientific source claim uses genuine \(W(3,s)\) flags and completed f/g.

**True-source sharp positivity:** the previously protected complete \(W(3,4)\) eight-flag matching of PR #662 supplies a single saturated selected parent with at least two accepted D6 full-H extensions. A separate new genuine W34 augmenting-source-matching construction selects **12 distinct actual original source flags** for TWO disjoint saturated physical K3,2 blocks on the SAME full independently injected K14 f/g, and assigns **four further actual original flags** to physically fresh common-neighbor extensions. It retains both physical diagonals for all 12 selected IDs, has zero selected-graph C6, and has **at least four accepted ORIGINAL D6** from the two disjoint saturated parents, with no duplicate accepted source sixset. The formula must certify exact unit multiplicity on the complete 425-source-incidence H, without restricting new common neighbors to the four designated flags.

## 4. Remaining scientific blocker

This sharply improves the **global deduplication coefficient** for the saturated population from sixfold to one, which is precisely the population created by the Hall-C6-free frontier in #661. It is NOT a uniform positive lower bound on the cumulative fresh-neighbor mass itself. To finish root HYP-105 #230 one would still need either a genuine-source all-map bound forcing \(\sum_F\sum_{i<j}|W_{ij}^H(F)|=\Omega(s^6)\) on a suitable selected G, or a same-map lower bound involving the other six historical GF5 accepted sixflag classes when this mass is sparse.

Keep Draft, exact-head GitHub-hosted CI and independent qualified mathematical referee gates. \`main\` unchanged; **OPEN_WITH_FORMAL_BLOCKER**.
