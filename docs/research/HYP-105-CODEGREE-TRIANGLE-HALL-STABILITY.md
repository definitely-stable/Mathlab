# HYP-105 / #230 — AA4-HALL2: Hall-SDR stability of strongly supported codegree triangles

**Status:** proved universal all-finite-bipartite structural lemma; genuine-source \(W(3,2)\)/\(W(3,4)\) finite independent tests; deterministic same-fixed-map **necessary condition** for hypothetical \(\,S_{\rm seven}=o(s^6)\) based on already established #659–660 original-ID selector. **This is not an unconditional all-map seven-GF5 \(\Omega(s^6)\) theorem and does not close Branch A/B/C.** The original source GQ is not replaced by an arbitrary regular graph in any claimed HYP-105 application.

## 1. Why this is a distinct new step after #659–660

Parent [Draft #659](https://github.com/definitely-stable/Mathlab/pull/659) proves that significant **FULL physical graph** high-degree tails force accepted original six-flag D6; conditional on low accepted \(S_{\rm seven}\), the degree tail is uniformly integrable. Parent [Draft #660](https://github.com/definitely-stable/Mathlab/pull/660) proves the exact ordinary C6 trace formula and its original sixflag GF5 D6 application to the **source-conflict-free / two-coordinate-2-cut coherent selected graph** \(G\):

\[
C_6(G)=\operatorname{tr}(K^3)/6-\operatorname{Correction}(G)
\le D_6(f,g)\le S_{\rm seven}(f,g).
\]

The density of such a graph may remain at the *critical* extremal scale \(e(G)=\Theta(v(G)^{4/3})\), so generic density alone need not imply even one C6. A positive raw cubic codegree moment may be **entirely canceled** by right-witness collisions, as seen in the true original GQ abstract Levi incidence graph. Instead of another numerical trace reformulation, this step gives a sharp **STRUCTURAL CLASSIFICATION of where such cancellation can occur** in the sector of sufficiently supported codegree triangles.

## 2. Three right-witness sets and a sharp local Hall-SDR theorem

Let \(G=(L,R,E)\) be any finite **simple bipartite graph**. For three distinct left vertices \(\{u,v,w\}\subseteq L\), form their three right-witness sets:

\[
A=N(u)\cap N(v),\quad
B=N(v)\cap N(w),\quad
C=N(w)\cap N(u),\qquad
q_A=|A|,\ q_B=|B|,\ q_C=|C|.
\]

Any ordered choice \((a,b,c)\in A\times B\times C\) of **three pairwise different right vertices** is equivalent to one *unoriented, unorooted* simple six-cycle with exactly \(\{u,v,w\}\) as its left vertex set:

\[
u-a-v-b-w-c-u.
\]

Thus \(C_6(u,v,w)\) is exactly the number of **systems of distinct representatives (SDRs)** of the three sets. In particular the exact finite expression from #660, now applied **per left triple** rather than summed over right stars, is

\[
\boxed{
C_6(u,v,w)=q_Aq_Bq_C-t(q_A+q_B+q_C)+2t,
\quad t=|A\cap B\cap C|=|N(u)\cap N(v)\cap N(w)|.
}
\]

For every source graph, the three different pairwise list intersections satisfy \(A\cap B=B\cap C=C\cap A=A\cap B\cap C\): a right vertex shared by two witness sets is automatically adjacent to all three left vertices. The formula follows by inclusion-exclusion of the three events \(a=b\), \(b=c\), \(c=a\); all pairwise event intersections coincide with the all-three-equal event. The constant \(+2t\) is exact.

**Theorem AA4-HALL2 (sharp no-C6 saturation dichotomy).** If \(|A|,|B|,|C|\ge2\), then:

\[
\boxed{
C_6(u,v,w)=0
\quad\Longleftrightarrow\quad
A=B=C=\{r_1,r_2\}\ \text{for distinct }r_1,r_2\in R.
}
\]

Otherwise the triple supports **at least two** distinct simple six-cycles. If all three codegrees are at least three, it supports **at least six** distinct simple six-cycles.

*Proof of the equivalence.* Hall's marriage theorem applied to the three lists \(A,B,C\) states that a three-element SDR exists exactly when every subfamily has union size at least its cardinality. Individual and two-list Hall conditions are automatic because *each individual set contains at least two right vertices*. Only the three-list condition can fail, and this is equivalent to \(|A\cup B\cup C|\le2\). Since each list has size at least two, this forces all three lists to be the identical two-element set. Then every attempted assignment repeats one of the two right witnesses and gives no simple C6. Conversely, if the three lists do not coincide with precisely two witnesses, their union contains at least three right vertices, so Hall gives a valid SDR, hence a C6. \(\square\)

*Why at least two when productive?* Let \((a,b,c)\) be a valid SDR. Every one of its three lists has at least one alternative right vertex distinct from its assigned representative. If an alternative is currently unmatched, changing that assignment gives a second SDR. Otherwise all three chosen alternatives lie among the other assigned representatives, giving a directed graph on the three assigned representatives with outdegree at least one and no loops; it contains a directed cycle. Rotating the corresponding assignments around that cycle gives a different SDR. Thus a unique SDR is impossible when every list has size at least two. The \(\ge2\) coefficient is sharp: for a genuine bipartite \(K_{3,2}\), adjoining one additional right vertex adjacent to exactly two of its three left vertices gives codegrees \((3,2,2)\), common intersection size two and **exactly two** simple C6.

*Why at least six for all codegrees \(\ge3\)?* Choose the witness for the first pair in at least three ways, the second pair in at least two remaining ways, and the third pair in at least one remaining way. The product \(3\cdot2\cdot1=6\) is a valid all-graph lower bound; equality holds on \(K_{3,3}\).

## 3. Global integer positive count and stability inequality

Define the **strong left codegree support graph** \(Q_2(G)\) on \(L\): an undirected edge \(uv\) belongs to \(Q_2\) iff \(q_{uv}\ge2\). Its triangles are precisely the left triples with all three pair-codegrees at least two.

Write:
- \(T_2(G)\): number of ordinary triangles in \(Q_2(G)\).
- \(S_2(G)\): number of those triangles whose three pair-witness sets are **identically the same two right vertices**. Each is a *saturated* \(K_{3,2}\), in the sense that no additional right witness occurs for any of its three left pairs.
- \(T_3(G)\): number of left triples with all three pair-codegrees at least three (triangles of the analogous strong support graph \(Q_3\)).

Every \(Q_3\) triangle is productive and contributes at least six C6; every other productive \(Q_2\) triangle contributes at least two; saturated \(Q_2\) triangles contribute none. Different left triples account for disjoint sets of simple C6. Therefore:

\[
\boxed{
C_6(G)\ \ge\
2\big(T_2(G)-S_2(G)\big)+4T_3(G).
}
\tag{HALL2}
\]

This is an **unconditional all-finite-simple-bipartite theorem**, requiring no spectral expansion, uniform degree hypothesis, original graph geometry or f/g independence.

The exact positive count on the \(Q_2\) sector is also explicitly computable:

\[
\boxed{
C_{6,\ge2}(G)=
\sum_{\substack{\{u,v,w\}\subseteq L\\
q_{uv},q_{vw},q_{wu}\ge2}}
\bigl(q_{uv}q_{vw}q_{wu}
-t_{uvw}(q_{uv}+q_{vw}+q_{wu})+2t_{uvw}\bigr).
}
\]

Then \(C_{6,\ge2}(G)\ge2(T_2-S_2)+4T_3\), and \(C_{6,\ge2}(G)\le C_6(G)\). Equality \(C_6=0\) imposes a sharp *necessary* structural restriction: **EVERY codegree-\(\ge2\) support triangle MUST be saturated by exactly the same two right vertices**, and \(Q_3\) is triangle-free.

## 4. Consequence under REAL original-source HYP-105 quantifiers

Fix a legal full separately globally injected, potentially arbitrarily correlated pair of typed physical labels \(f,g\) on a **genuine symplectic** \(W(3,s)\), \(s=2^h\). Let \(G\) be ANY of the source-ID conflict-free coherent physical subgraphs obtained by selection of **whole genuine original incidence IDs (both physical diagonals)** and both source-coordinate 2-cuts of #659–660. Every ordinary C6 in \(G\) is physical-coordinate-rainbow, uses six different original incidence IDs, six different original point/line factors, and belongs to the historic accepted original GF5 D6 family by #652. Thus the all-graph Hall stability bound becomes a **same-fixed-map rigorous positive original-six-ID GF5 lower certificate**:

\[
\boxed{
S_{\rm seven}(f,g)\ge D_6(f,g)\ge
C_6(G)\ge 2(T_2(G)-S_2(G))+4T_3(G).
}
\]

This is stronger as a *structural necessary obstruction* than simply writing \(C_6=\operatorname{trace}-\operatorname{correction}\): it gives a direct positive alternative from non-saturated strong-codegree support triangles.

**New explicit counterfamily restriction:** Suppose a sequence of LEGAL maps at \(s\to\infty\) had \(S_{\rm seven}(f,g)=o(s^6)\). Then for **every** source-ID coherent selection \(G_s\) of the kind above,

\[
T_3(G_s)=o(s^6),\qquad
T_2(G_s)-S_2(G_s)=o(s^6).
\]

This is a theorem conditional on the **hypothetical premise** \(S_{\rm seven}=o(s^6)\), not a proof that that premise is impossible. In particular it does not claim that the number of saturated \(K_{3,2}\) triangles is small. The selected graph could have many codegree-\(\ge2\) triangles yet avoid all accepted D6 from them through saturated \(K_{3,2}\) configurations.

Those source-coherent \(K_{3,2}\) saturation patterns are now a **precise candidate location for the missing compensating accepted original GF5 classes**, rather than an undifferentiated high-moment correction term. No theorem currently says that any particular such pattern automatically belongs to one of the other six accepted original-sixflag classes; this must be proved or disproved separately with actual original source IDs.

## 5. Finite falsifiers and scientific scope

The new code independently computes \(Q_2\) by common-neighbor sets, enumerates each strong-support left triangle once, classifies exactly the saturated \(K_{3,2}\) case, computes each triple's C6 population using the *local* formula, and compares the result against the **independent aggregate codegree-trace** in #660. The tests add a separate DFS on all 512 bipartite \(3\times3\) graphs and all 4096 bipartite \(3\times4\) graphs, including:
- \(K_{3,2}\): \(T_2=S_2=1\), zero C6.
- \(K_{3,2}\) plus an extra right witness shared by exactly two left vertices: \(T_2=1,S_2=0,T_3=0,C_6=2\), showing sharpness.
- \(K_{3,3}\): \(T_2=T_3=1\), exact six C6 and lower six.
- \(K_{4,4}\): \(T_2=T_3=4\), exact 96 C6 but lower only 24.
- TRUE-source \(W(3,2)\)/\(W(3,4)\) complete typed injections processed through the real #659 source-ID selector and both physical-coordinate cuts, with the historic original GF5 D6 classifier verifying the selected graph's accepted-six-source flags.
- TRUE original \(W(3,4)\) full-map protected 16-source-ID \(4\times4\) physical hub/free structure, with both physical diagonals retained: exactly 96 accepted D6 and a rigorous Hall2 lower of 24.

**Asymptotic limitations:** The finite oracle does not construct a universal minimum-\(S\) counterfamily, and the Hall2 inequality need not be of order \(s^6\) for every map. It remains possible that ALL retained coherent graphs have most strong-codegree support triangles saturated, or most genuine D6 carried by triples with at least one codegree 1. Any root proof must confront that possibility and/or get acceptance from the remaining six original GF5 classes.

**Scientific next P0:** derive a source-original-incidence constraint on the total saturated \(K_{3,2}\) mass after selecting genuine IDs and both coordinate cuts, or show this mass quantitatively transfers into a different ACCEPTED original GF5 sixflag class on the SAME fixed correlated map. A synthetic bipartite K3,2 alone is NOT such a theorem. Keep Draft until exact GitHub-hosted specialized/full Research/INDEX checks and external qualified proof review. Root #230 OPEN_WITH_FORMAL_BLOCKER.
