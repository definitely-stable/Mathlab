# HYP-105 / #230 — AA4-C6TRACE: exact coherent C6 source-ID moment certificate

**Scientific status:** exact all-graph identity, plus a genuine-source finite audit and restricted positive D6 transfer. This is a *new calculation in the Mathlab proof stack*, not a claim of priority over known six-cycle counting identities. **It does NOT prove the all-map original seven-class \(\Omega(s^6)\) lower bound, Branch A/B/C or an ASET exponent.** Root #230 remains \`OPEN_WITH_FORMAL_BLOCKER\`.

## 1. Why the next gate differs from the already settled tail theorem

Parent [scientific Draft #659](https://github.com/definitely-stable/Mathlab/pull/659) established a full-physical-graph degree-tail alternative for every fixed complete separately globally injected, arbitrarily correlated pair-labeling on **true original symplectic** \(W(3,s)\), \(s=2^h\). When the tail of high physical degrees has \(\Omega(s^4)\) incident edges, the actual accepted ORIGINAL six-incidence GF5 D6 already has \(\Omega(s^6)\) mass at a quantitative high threshold. Thus hypothetical \(S_{\rm seven}=o(s^6)\) forces degree-tail uniform integrability. A local source-ID conflict-graph selector and two coordinate 2-cuts preserve a positive fraction of any \(\Omega(s^4)\) subset of ORIGINAL incidence IDs as a physically **coherent**, row/column-cherry-free, globally color-cut graph \(G\).

Nevertheless \(e(G)=\Theta(s^4)\) and \(v(G)=O(s^3)\) alone do not imply a positive multiple of \(s^6\) simple six-cycles. This is a **critical extremal density** \(e=\Theta(v^{4/3})\). There exist ordinary bipartite \(C_6\)-free graphs at this density. The original incidence (Levi) graph of \(W(3,s)\), **considered only as an abstract bipartite graph**, is an explicit such example: \(v=2(s+1)(s^2+1)=\Theta(s^3)\), \(e=(s+1)^2(s^2+1)=\Theta(s^4)\), but no ordinary C6 because its original incidence graph has girth eight. **This abstract Levi graph is NOT asserted to be a legal selected physical graph on \([a]^2\) backed by both diagonals**. The example refutes only a proposed *density-only graph-theoretic implication*.

The present slice identifies the exact excess over the no-C6 threshold on the **selected physical graph**, without any generic supersaturation constants or heuristics about f/g independence.

## 2. Exact all-graph bipartite codegree-triangle identity

Let \(G=(L,R,E)\) be any finite simple undirected bipartite graph, with \(d_r=|N(r)|\) for \(r\in R\). For **distinct** \(u,v\in L\), define the right common-neighbor codegree

\[
q_{uv}=|N(u)\cap N(v)|.
\]

Construct the symmetric nonnegative matrix \(K\) indexed by \(L\) with \(K_{uv}=q_{uv}\) for \(u\ne v\) and \(K_{uu}=0\).

**Theorem (all finite simple bipartite graphs):**

\[
\boxed{
C_6(G)
=\frac{\operatorname{tr}(K^3)}6
-\sum_{r\in R}
\left[
(d_r-2)\sum_{\{u,v\}\subseteq N(r)}q_{uv}
-2\binom{d_r}{3}
\right].
}
\tag{C6-T}
\]

Here \(C_6(G)\) is the number of **unoriented, unorooted, simple** ordinary six-cycles. The right side is a nonnegative INTEGER for every admissible graph; it does not count closed walks with repeated vertices as cycles.

**Proof.** Fix three different left vertices \(u,v,w\). Choosing a right common neighbor for each of the unordered left pairs \(uv,vw,wu\) produces \(q_{uv}q_{vw}q_{wu}\) triples of right witnesses. Requiring that the three chosen right vertices be distinct yields precisely one simple undirected C6 for each such witness triple (and conversely every simple C6 has exactly one unordered triple of its left vertices).

Let \(t_{uvw}=|N(u)\cap N(v)\cap N(w)|\). Among all right-witness triples, a prescribed collision of two witnesses forces their value to be a common neighbor of **all three** left vertices, and leaves \(q\) choices on the remaining left pair. Inclusion-exclusion for the three pairwise witness-equality events gives exactly

\[
q_{uv}q_{vw}q_{wu}
-t_{uvw}(q_{uv}+q_{vw}+q_{wu})
+2t_{uvw}
\]

valid distinct-right assignments.

Summing over \(\{u,v,w\}\subseteq L\), the first term is \(\operatorname{tr}(K^3)/6\). For the collision sum use

\[
t_{uvw}=\sum_{r\in R}{\bf1}_{u,v,w\in N(r)}.
\]

For each fixed \(r\), each unordered left pair in \(N(r)\) belongs to exactly \(d_r-2\) left triples inside \(N(r)\). Hence

\[
\sum_{\{u,v,w\}\subset N(r)}
(q_{uv}+q_{vw}+q_{wu})
=(d_r-2)\sum_{\{u,v\}\subset N(r)}q_{uv},
\]

and \(\sum_{\{u,v,w\}\subset N(r)}2=2\binom{d_r}{3}\). Substitution proves (C6-T). Every coefficient and orientation factor is exact. \(\square\)

**Safe interpretation:** the first moment \(\operatorname{tr}(K^3)\) is **not** a lower bound for simple six-cycles until the full exact right-witness collision correction is subtracted. A graph can have a large positive codegree triangle trace and **zero C6** (e.g. the genuine source GQ Levi negative control below).

## 3. A source-safe same-map accepted D6 certificate

Take the exact full-ID selector from parent #659 on the genuine original \(W(3,s)\) with complete distinct typed point/line labels \(f,g\) and arbitrary correlation. It chooses a subset \(I_G\) of **ACTUAL original point-line incidence IDs** with no shared-original-pencil physical-coordinate conflicts, and retains BOTH diagonals per selected original ID. After two global 2-cuts, its physical graph \(G\) is bipartite and has no row or column cherries.

A simple C6 in this graph has six pairwise different first coordinates and six pairwise different second coordinates: repetitions at cyclic distance 2 or 4 would create a same-coordinate neighbor pair at one intermediate physical corner (forbidden by source conflict-freeness), and repetitions at distance 3 would connect same-color symbols across an edge-distance-3 walk (forbidden by each 2-cut). There are no other nontrivial repetition distances. Each physical edge retains its **unique genuine original source incidence ID**. Existing source-ID bijection AA4-RC6 (#652) identifies these simple coordinate-rainbow C6 with accepted ORIGINAL six-flag GF5 D6.

Therefore, for every such **actual same-map coherent subset** of original IDs,

\[
\boxed{
D_6(f,g)\ge C_6(G)
=\frac{\operatorname{tr}(K_G^3)}6
-\mathrm{Correction}_G,
}
\tag{D6-CERT}
\]

where the right side is **exactly** the accepted D6 count *inside the selected graph* and is a rigorous lower certificate on the complete original physical graph.

This proof does **not** need any subfield-packet existence theorem, extra randomness of the map, synthetic edges, source cloning, conjectured unbalanced supersaturation or a large constant in a general extremal graph theorem.

**Boundary:** it does not guarantee that the final displayed right side is \(\Omega(s^6)\) for **every** allowed correlated source pair-label map. Selection and bicoloring can retain \(\Theta(s^4)\) original flags but land in a graph at the exact critical extremal density, with no a priori positive C6 count. A universal asymptotic lower bound on the **excess** \(\operatorname{tr}(K^3)/6-\mathrm{Correction}\), or compensation by the other six accepted historical GF5 classes, remains the original problem.

## 4. Reproducible independent finite falsifiers

Code: \`research/hyp105_coherent_c6_codegree_trace.py\`. Tests: \`research/test_hyp105_coherent_c6_codegree_trace.py\`.

- **All 512** simple bipartite graphs on a labeled \(3+3\) vertex set are checked against a separately written DFS counting unrooted/unoriented simple C6.
- \(K_{3,3}\) gives triangle codegree moment \(27\), collision correction \(21\), hence **6** simple C6. \(K_{4,4}\) gives **96**.
- TRUE original symplectic \(W(3,2)\) and \(W(3,4)\) **Levi** graphs have **0 C6**, with the entire positive first term canceled by the right-witness correction; this is an *abstract bipartite density-only negative control*, not a proposed original physical labeling.
- TRUE original \(W(3,2)\), \(W(3,4)\) with lex and reverse-line complete globally injected pair labels, and an adversarial full \(W(3,4)\) labeling, are processed through the REAL source-ID conflict selector, independent-set construction and two coordinate cuts from parent #659, with various finite thresholds. The new arithmetic trace count must equal BOTH the independent enumerated original physical C6 count and the historical original source-ID GF5 D6 acceptance census of the selector.
- TRUE \(W(3,4)\) 16 selected original source-flags forming a protected \(4\times4\) physical hub/free structure, with full \(K_{14}\) injection completion and BOTH diagonals retained, gives **96** accepted original D6 source sixsets, independently recovered by the new matrix trace.

These tests validate the exact arithmetic and original-source provenance for tiny fields; they do **not** establish asymptotic claims for \(s\ge64\). Invalid asymmetric/non-bipartite input is rejected.

## 5. Next mathematical frontier

The new **third codegree moment minus exact right-collision penalty** is the correct invariant for the bounded-degree/coherent remainder. The root can be approached by either:

1. A genuinely **source-geometric, fixed-map-uniform** lower bound on this surplus for a collection of coherence selections/color cuts; merely bounding total edges and vertices cannot suffice.
2. A **same-map compensation theorem** showing that if every such source-coherent graph is near its C6-free threshold, a positive proportion of the *other six* historical accepted ORIGINAL GF5 classes necessarily exists.

The old all-map D6-only claims remain unproved. An ordinary source-GQ Levi graph is a falsifier of any proposed universal statement based only on \(v\), \(e\) and maximum degree, but is not a valid counterexample to full HYP-105. Retain root \`OPEN_WITH_FORMAL_BLOCKER\`, parent and child Draft, full exact-head GH-hosted CI and independent qualified scientific review.
