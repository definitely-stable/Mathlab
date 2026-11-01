# HYP-105 / #230 — AA4-CODEGREE: independent exact ordinary C6 source-ID referee, no cycle-DFS circularity

**Scientific Draft**, stacked STRICTLY on frozen [#690](https://github.com/definitely-stable/Mathlab/pull/690) HEAD `ed8356c43ece533f75f8eb66072d564481552cef`; original `main`, #659/#672–#690 untouched. Genuine `W(3,2^h)`, all complete, typed separately globally injected, arbitrary correlated fixed f,g, and six different ORIGINAL incidence flag IDs remain the exact model. No theorem acceptance, issue closure, or scientific merge.

## 1. Frontier and why this is not another numerical constant change

Previous analyses [#659](https://github.com/definitely-stable/Mathlab/pull/659), [#684](https://github.com/definitely-stable/Mathlab/pull/684), [#686](https://github.com/definitely-stable/Mathlab/pull/686) rely on two logically separate steps:

1. external **ordinary graph** balanced C6 supersaturation, valid for every simple graph satisfying `e>=C_graph*v^(4/3)`, yielding `#ordinary_unoriented_C6>=c_graph*(e/v)^6`; and
2. **source-native injection** from EACH such ordinary physical C6 in an ORIGINAL-source coherent, two-binary-cut G to a DIFFERENT `D6` sixset of true original flags of the SAME genuine W(3,s), including both physical diagonals per selected original flag.

The prior source audit used physical cycle DFS plus the historical original sixset classifier. A new independent **pure codegree-algebra** oracle and direct six-vertex injection oracle reduce dependence on those previous implementations. This slice also identifies a new **local explicit graph certificate** which can replace the external SS6 theorem *only when the selected graph demonstrably contains a specified dense common-neighbor clique*. It does NOT assert that such a clique exists for every map (therefore does NOT replace SS6 in the universal Branch A proof).

## 2. Exact finite identity — proved for EVERY simple bipartite graph

Let `G=(X,Y,E)` be ANY finite simple bipartite graph (unbalanced, disconnected and with isolated vertices permitted), and for distinct `x,y,z in X` put

\[
c_{xy}=|N(x)\cap N(y)|,\qquad
t_{xyz}=|N(x)\cap N(y)\cap N(z)|.
\]

The exact number of **ordinary simple unoriented unrooted** six-cycles is

\[
\boxed{
\#C_6(G)=
\sum_{\{x,y,z\}\in\binom X3}
\left[
c_{xy}c_{yz}c_{zx}
-t_{xyz}(c_{xy}+c_{yz}+c_{zx})+2t_{xyz}
\right].
}\tag{CG1}
\]

**Independent proof:** for one unordered left triple `{x,y,z}`, choose a right vertex `a in N(x)∩N(y)`, `b in N(y)∩N(z)`, and `c in N(z)∩N(x)`. There are `c_xy*c_yz*c_zx` ordered candidates; each of the three pairwise collisions `a=b, b=c, c=a` has count exactly `t_xyz*c_opposite`. All three pairwise-collision events have common intersection of size `t_xyz`; their inclusion/exclusion has correction `+2t_xyz`. The survivors have SIX **distinct** physical vertices, and form one simple `x-a-y-b-z-c-x` cycle. Conversely a simple C6 has exactly ONE left three-set `{x,y,z}` and exactly ONE intermediate right-vertex choice for each fixed pair of left vertices. Hence NO extra division by 2,3,6 or 12 occurs.

In particular, for `K_{3,3}`, (CG1) gives 6; for `K_{4,4}`, it gives 96; for any `K_{u,v}` it gives `6*binom(u,3)*binom(v,3)`, as required for an **unoriented** cycle.

A completely independent brute-force reference enumerates all injections of three distinct right vertices for each unordered left triple, WITHOUT evaluating (CG1), any moment/tr(A^6) identity, adjacency graph DFS, or the historical `#684` implementation.

## 3. NEW exact LOCAL original D6 certificate: a codegree clique

For ANY specified subset `S⊆X` of `t=|S|>=3` actual ordinary physical vertices, suppose every two different `x,y in S` have `c_xy>=k`, where integer `k>=3`. In the proof of (CG1) fix ANY three different `x,y,z in S`. Choose `a` from the first pair's common neighbors (>=k choices), `b` from the next (at least k-1 choices after excluding a), and `c` from the third (at least k-2 after excluding a and b). Every choice yields a different physical simple six-cycle for this unordered left triple. Therefore

\[
\boxed{
\#C_6(G)\ge
\binom{t}{3}k(k-1)(k-2).
}\tag{CG2}
\]

This is a **self-contained universal finite graph lemma** requiring NO Jiang–Yepremyan SS6 theorem, balanced regularization, graph maximum degree assumptions or randomization. If no such source-selected subset S is given, the lemma offers no positive global lower; no assumption of its existence for arbitrary f,g is made.

For TRUE `W(3,s)` physical G consisting of BOTH paired diagonals of a selected subset of ORIGINAL source flags, assume:

* all selected original flag IDs genuinely occur in `W(3,s)`;
* none of the selected ORIGINAL flag pairs conflict at common original point/shared right symbol or common original line/shared left symbol;
* the fixed whole-flag left and right coordinate colorings are both bichromatic on each selected original pair.

These are the #659/#684 **coherent selector** conditions, not new stochastic hypotheses. They imply each physical ordinary C6 has six distinct left-coordinate symbols and separately six distinct right-coordinate symbols (distance-2 coordinate repeats contradict source cherry-freedom; distance-3 repeats contradict binary cuts). Every physical edge carries precisely ONE original incidence flag owner, because f and g are injective, and distinct edges in a coordinate-proper six-cycle use distinct original point and original line factors. Thus an ordinary C6 yields six different genuine ORIGINAL source incidence IDs with matching factor partitions, precisely a D6 sixset. Moreover two distinct physical unoriented C6 cannot give the same D6 original sixset under this coherence: the original six flag pair projections determine its common physical six-cycle up to reversal, as in the independently reviewed #652 inverse. Hence

\[
\boxed{
D_6(f,g)\ge\#C_6(G)\ge
\binom{t}{3}k(k-1)(k-2).
}\tag{CG3}
\]

**This is a conditional-on-a-concrete-selected-codegree-clique numerical certificate that may be applied to ANY LEGAL fixed f,g without external SS6**, including any adversarial correlated assignments. Its logical input is the observed combinatorial codegree clique; no uniform Omega(s^6) from this alone is asserted.

## 4. Original W32/W34, exhaustive graph falsifiers and independence

The new `research/hyp105_independent_codegree_c6_source_referee.py` is independent of historical physical cycle DFS, GF5 flow/classifier, graph supersaturation, ROOT h0 calculators and original selected-graph source lookup. It constructs its own original-to-two-physical-diagonals assignment directly from true `genuine_source(power)`, checks complete typed pair injections and ORIGINAL source-flag conflicts by pairwise ID comparison, verifies both actual binary coordinate cuts, then:

1. recreates the selected physical graph with its true original-flag provenance;
2. counts ALL ordinary unrooted C6 using (CG1), via bitset common-neighbor intersections;
3. independently constructs every ordinary C6 from distinct left and right triples; re-checks each physical coordinate's sixfold distinctness;
4. recovers all SIX TRUE original flag IDs from each of the cycle's SIX actual physical edges; verifies original point and line matching separately and rejects duplicate sixsets;
5. compares exact SOURCE D6 count with BOTH pure-codegree and independent direct-six-vertex counts.

The exhaustive **4096** labelled 3×4 bipartite graph universe and **65536** labelled 4×4 bipartite graph universe are checked by TWO independently coded methods. Additional `K_{t,k}` and adversarial small graphs verify C6 cycle normalization and the exact explicit clique lower. Genuine W32/W34 complete correlated physical maps and independently greedy coherent source cuts are checked. A protected planted ORIGINAL W34 matching control realizes a physical K4,4 and **exactly 96 ordinary physical C6 / 96 DIFFERENT accepted ORIGINAL D6 sixsets**, preserving exact six source flag IDs. A simultaneous global permutation of both typed coordinate alphabets must preserve the complete original sixset census. Incomplete injections, source-ID duplicates, wrong binary cuts and malformed graph adjacency fail closed.

Finite W32/W34 observations serve as **falsifiers**, not proof of the all-h matching/injection theorem or SS6. The all-h graph identity (CG1) and conditional clique bound (CG2) are proved above for every finite simple bipartite graph; (CG3) additionally uses the previously proved original selected-source C6-to-D6 map and its stated requirements.

## 5. Acceptance and next mathematical work

This is an independent exact route through the most important **ordinary C6 counting and ORIGINAL provenance transfer** boundary in #659/#684, including an explicit local *source-lifted* cycle lower lemma. The non-circular nature of the finite tests supports this boundary, but **does not independently reprove** the balanced graph SS6 theorem, the universal existence of codegree cliques, the mixed FULL/CORE fourth-moment blocker, or the entire #672–#690 all-map Branch A geometric proof. The complete original-source theorem remains `OPEN_WITH_FORMAL_BLOCKER` and requires qualified external mathematical peer review. No automatic merging of scientific Draft PRs or #230 closure is authorized.

Next valuable challenge: investigate whether the actual balanced chunk F created from arbitrary original maps (after Caro–Wei source coherence and whole-flag cuts) admits a uniform **codegree-triangle** lower, potentially giving an elementary alternative to the external SS6 step. That is NOT implied by the simple local clique hypothesis and must be established or falsified with adversarial ordinary bipartite examples before promotion.
