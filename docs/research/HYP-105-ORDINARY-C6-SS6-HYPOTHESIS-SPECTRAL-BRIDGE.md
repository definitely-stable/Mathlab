# HYP-105 / #230 — AA4-SS6GATE: independent published ordinary-C6 theorem-hypothesis gate and self-contained spectral subbranch

**Scientific Draft** stacked strictly on frozen [#695](https://github.com/definitely-stable/Mathlab/pull/695), parent exact HEAD `bc6f24f9a09ac214c6b7bb3ca51445f91aaa4db5`. No changes to parent/main, no merge, root issue remains OPEN_WITH_FORMAL_BLOCKER. This slice verifies the *type of object* and *exact numerical hypothesis* to which Branch A applies the external ordinary-cycle theorem. It also proves a new completely ELEMENTARY EXPLICIT C6 lower certificate on an additional degree-regularity subbranch, strictly distinguishing this new sufficient condition from a universal all-map result.

## 1. Primary source and exact theorem being imported

**Externally verified primary published source:** Tao Jiang & Liana Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, **Combinatorics, Probability and Computing 29(5) (2020), 698–721**, published online 23 June 2020, DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206). See the [publisher's article and abstract](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/supersaturation-of-even-linear-cycles-in-linear-hypergraphs/240493C1F42618819DA9B16CE7F3E4BD) and independent [arXiv record 1707.03091](https://arxiv.org/abs/1707.03091). The publisher describes Simonovits' ordinary simple-graph even-cycle supersaturation theorem and states that Jiang–Yepremyan's proof includes the ordinary graph `r=2` case.

**Precisely imported statement, specialized to C6:** There exist ABSOLUTE but **not numerically specified** `C_graph,c_graph>0` such that for every ordinary finite simple graph F of `v` vertices and `e` undirected physical edges,

\[
\boxed{e\ge C_{\rm graph}v^{4/3}
\Longrightarrow
\#C_6(F)\ge c_{\rm graph}(e/v)^6.}\tag{SG1}
\]

Here `#C6` is the number of **simple, injective-vertex, unoriented and unrooted** ordinary six-cycles. The statement is about actual graph **copies**, not `hom(C6,F)`, `tr(A_F^6)` or number of even closed walks. It does NOT require F to be a generalized quadrangle, to have balanced bipartition sizes, be connected, be almost regular, or preserve both paired diagonals of an original incidence flag. The source's `r` is hyperedge uniformity (=2 for graphs), NOT the length of an original three-edge path. Its `2k=6` is obtained by specializing `k=3` in the quoted graph theorem. We **do not** substitute invented numerical values for the existential constants or claim we reconstructed the paper's full constants from the abstract.

## 2. Exact hypothesis normalization, no cube roots/floating point

For a fixed ACTUAL ordinary simple graph with integer `v,e` and any **hypothetical trial** positive EXACT rational `C`, the numerical hypothesis is equivalent to the integer/rational inequality

\[
\boxed{e^3\ge C^3v^4.}\tag{SG2}
\]

The implementation returns the exact fraction `e³/v⁴` for each measured graph, and will only say "hypothesis met" **relative to the explicitly supplied C**. No label such as `C=1` or `c=1` is EVER promoted to the actually published unknown values. The arithmetic check on any finite small graph is NOT an all-h proof of the source heavy-tail-chunk lemma.

### Original W(3,s) heavy-tail branch gate

On the actual-original-source heavy-tail branch from [#684](https://github.com/definitely-stable/Mathlab/pull/684), the FULL original physical graph has EXACTLY two physical edges per genuine incidence flag, and the original heavy physical vertex list is taken **before** pruning. After Caro–Wei original-ID conflict selection and two whole-flag typed-coordinate cuts, the selected coherent physical graph G is simple and bipartite and every C6 injects into a distinct ORIGINAL D6 six-incidence-ID class.

The heavy endpoint witness pigeonhole + no-clone opposite-side chunk produce an **actual ordinary physical subgraph** `F=G[R,Y_*]`, not a synthetic hypergraph nor a graph on original points and lines:

\[
e(F)/v(F)\ge\beta s/32,\qquad
v(F)\le16s^3/T,\qquad
\beta=\varepsilon^2/2^7.
\tag{SG3}
\]

The selected parent G retains BOTH paired diagonals per selected source flag, but the **subgraph F need not retain both**. This is NOT a problem: it is an ordinary subgraph of the coherent selected graph, and every one of its simple cycles remains coordinate-proper, still carrying six distinct original incidence flags and giving an original D6 sixset. The published ordinary graph theorem is valid on F with no pairing constraint.

For all dyadic `s=2^h>=64` and symbolic actual external constant `C_graph`, the exact algebraic sufficient condition (not a fitted h0) is

\[
\boxed{
T\ge2^{19}C_{\rm graph}^3\beta^{-3}
=2^{40}C_{\rm graph}^3\varepsilon^{-6}
\Longrightarrow\ e(F)\ge C_{\rm graph}v(F)^{4/3}.
}\tag{SG4}
\]

It follows by cubing the two inequalities of (SG3), not by assuming the actual F is regular. From (SG1) and exact original-source six-ID injection:

\[
\boxed{D_6(f,g)\ge c_{\rm graph}\,\varepsilon^{12}2^{-72}s^6.}\tag{SG5}
\]

The right side still depends on the **unknown published** `c_graph` and is CONDITIONAL on the full #659/#684 source flag selection plus true physical graph construction. This is the mathematically correct all-h heavy-tail branch of Branch A; it does not by itself prove the other dense-core case.

## 3. NEW elementary, constant-explicit C6 lower bound in a restricted subbranch

**Proposition (all finite simple BIPARTITE graphs, no published theorem input).**
Let F be any finite simple bipartite graph with `n=v(F)>0`, `m=e(F)>0`, maximum degree `Delta`, symmetric adjacency `A`, mean degree `d=2m/n`. If

\[
\boxed{d^5\ge144n\Delta^2,}\tag{SG6}
\]

then F contains at least

\[
\boxed{\#C_6(F)\ge\frac{d^6}{24}.}\tag{SG7}
\]

The criterion is EXACT INTEGER-CHECKABLE, since (SG6) is precisely

\[
\boxed{(2m)^5\ge144n^6\Delta^2.}\tag{SG8}
\]

**Independent proof:** First the largest eigenvalue of symmetric A is at least d (Rayleigh quotient of the all-one vector), hence `X=tr(A^6)>=d^6`. Next every non-simple rooted closed six-walk in a **simple bipartite** graph contains a cyclic length-two backtrack. There are six candidate positions, deleting a backtrack gives a rooted closed four-walk and at most Delta choices for its reinsertion, so

\[
X\le12\#C_6(F)+6\Delta\operatorname{tr}(A^4).
\]

This is the exact *type distinction*: one simple unoriented C6 contributes 12 rooted oriented walks, whereas nonsimple walks must be subtracted. Spectral Cauchy gives `tr(A^4)^2<=tr(A^2)tr(A^6)=2mX=ndX`. Combine:

\[
12\#C_6(F)\ge X-6\Delta\sqrt{ndX}.
\]

If (SG6) holds, `d^6>=144\Delta^2nd`, so `\sqrt X>=d^3>=12\Delta\sqrt{nd}`; the last correction is at most `X/2`, and

\[
12\#C_6(F)\ge X/2\ge d^6/2.
\]

This completes the proof. No external constants, distributional assumptions, graph regularization, f/g independence, original source geometry or numerical spectrum computation are required. Bipartiteness IS required for the stated noninjective-walk subtraction; we explicitly reject general nonbipartite graphs instead of silently applying this theorem to them.

**Non-vacuous example:** K_{18,18} has `n=36,m=324,Delta=d=18`; (SG8) holds, giving a fully explicit lower `18^6/24=1,417,176` simple unoriented C6 without (SG1). Its exact number is `6*binom(18,3)^2=3,995,136`. The criterion fails for K_{12,12}, but this says NOTHING about whether K12,12 has cycles (it does); a failed sufficient condition is not a counterexample.

**Essential scientific limitation:** for a general true W(3,s) selected/trimmed F, the established #684 estimates `d(F)>=beta*s/16` (from e/v and the definition of d), `n(F)<=16s^3/T` and `Delta(F)<=T*s` DO NOT establish (SG6) for arbitrary giant fixed T, beta. All quantities in (SG6) can scale at the same s-power and the available constants do not force the desired inequality. In particular, unlike the **published** ordinary supersaturation theorem, this elementary argument requires a substantial degree-to-max-degree separation, so it **CANNOT REPLACE (SG1) IN THE GENERAL HEAVY-TAIL BRANCH**. It is a valid independent certificate in the restricted favorable cases.

### NEW additional EXACT original-source one-diagonal subgraph theorem

There is a particularly important source-to-graph edge case: the **published** ordinary C6 theorem is applied NOT to the whole ORIGINAL source-selected graph G (where both flag diagonals survive), but to the smaller balanced **ordinary subgraph F**, where at most ONE of a flag's two diagonal edges might be present. Therefore requiring F to preserve paired diagonals would be an INVALID application hypothesis.

The full ORIGINAL selected G obeys two independent typed binary coordinate cuts `lc,rc`. For every physical cell v=(x,y), define its *binary physical parity sector* `eta(v)=lc(x) XOR rc(y)`. Every actual physical edge in G flips BOTH cuts, hence its two endpoints have the SAME parity eta. Thus G is the disjoint union of two actual ordinary subgraphs G_0,G_1 on the eta=0 and eta=1 physical vertices, with NO edges between them.

Every retained actual ORIGINAL source flag (p,ell) has f(p)={x,z} and g(ell)={y,w} bichromatic on both cuts, and produces **exactly two genuine opposite-corner physical diagonal edges**:
`(x,y)--(z,w)` and `(x,w)--(z,y)`. They lie in DIFFERENT eta sectors, because the left x coordinate is the same on their first endpoints whereas right y/w have opposite colors. Hence **EACH original flag contributes EXACTLY ONE actual physical edge to EACH sector G_i**. This does not clone source flags or introduce new original IDs. Any physical simple C6 lies entirely in one sector and by the original no-cherry plus both-cut argument has six distinct left coordinate symbols and six distinct right symbols, thus six distinct source flag owners and a genuine ORIGINAL D6 sixset.

Therefore, for every true original W(3,2^h) and any fixed correlated complete f,g with a source-coherent two-cut selected G, the following deterministic identities hold:

\[
\boxed{
e(G_0)=e(G_1)=|I_G|,\quad
e(G)=2|I_G|,\quad
C_6(G)=C_6(G_0)+C_6(G_1),\quad
\#C_6(F)\le\#C_6(G)\le D_6(f,g)
\quad (\forall F\subseteq G).
}\tag{SG9}
\]

The last inequality is **valid for any actual ordinary subgraph F of G**, whether it preserves both, one or zero of a given original flag's physical diagonals. This is exactly why the actual balanced chunk F=G[R,Y_*] in #684 satisfies the ordinary graph theorem's source-ID application conditions. The new independent referee constructs both sectors directly from actual ORIGINAL W32/W34 flag IDs and BOTH physical diagonals, separately counts their ordinary physical six-cycles, checks every cycle's six ORIGINAL IDs and injectivity into original D6, and demands sector cycle counts sum to the parent G count; protected genuine W34 control has exactly 96 source-distinct D6 in G. This is a finite falsifier of the formal all-h identity above, **not** a proof that the balanced chunk automatically satisfies the external density threshold for arbitrary small s.

## 4. Direct ordinary/source bridge and independent finite falsifiers

The new standalone Python module `research/hyp105_ordinary_c6_ss6_hypothesis_spectral_bridge.py` does **not** import #680's closed-walk moment calculator, #691's ordinary C6 codegree formula or #684's selected-chunk operator. From scratch:

1. checks an explicit finite graph's actual vertex set, including isolates, symmetric undirected simple physical edges and a valid bipartition, excluding loops and non-crossing edges;
2. counts ACTUAL ordinary simple unoriented C6 using inclusion/exclusion on triple common-neighbor sets (NOT closed walks);
3. separately computes `tr(A^4)` and `tr(A^6)` by direct A²/A³ physical adjacency contractions, verifies the bipartite six-walk backtrack bound and spectral Cauchy, tests the new (SG8) criterion and certified (SG7) using exact rational arithmetic;
4. checks the external theorem's density hypothesis exactly as `e³>=C³v⁴` for **explicitly flagged trial rational C ONLY**;
5. independently reconstructs TRUE original W(3,2)/W(3,4) complete injected f,g and selected actual ORIGINAL coherent source IDs with BOTH physical diagonals and both binary cuts, rejects original pencil conflicts, and checks every selected simple physical C6 gives a DIFFERENT SIX original flag IDs with six different original point/line factors. No pseudo-W source, no invented original IDs;
6. checks the symbolic (SG4)/(SG5) epsilon-beta-T algebra on exact rationals and dyadic s, without asserting actual external theorem constants or numerically verified h0.

The new tests exhaustively verify **all 4096 labeled 3×4 bipartite graphs** by an INDEPENDENT rooted closed-six-walk brute-force and INDEPENDENT injective six-vertex DFS with mandatory factor-12 normalization. Additional selected 4×4 graphs and regular/unbalanced K_{a,b} test both successful and failing spectral gates, including the explicit K18,18 case; every genuine W32/W34 complete correlated mapping is tested through independent greedy conflict-free whole-flag cuts and actual source IDs. The planted true-original W34 protected K4,4 control must yield exactly **96 distinct ORIGINAL D6 sixsets / 96 ordinary C6**. Invalid original maps, missing source flags, asymmetric/mis-bipartitioned graphs and non-dyadic parameter inputs fail closed.

**Scientific acceptance remains OPEN_WITH_FORMAL_BLOCKER.** This new theorem is a useful standalone *explicit* nonexternal **subbranch** and a publication-hypothesis audit, not an externally refereed proof of the WHOLE original W(3,s) sextic Branch A obstruction, new ASET exponent, R2/R3 general bound or replacement numerical c_graph. Parent Drafts and `main` remain untouched; no merges or root issue closure. The strongest remaining work is independent qualified extremal-combinatorics review of the full original source proof, particularly the source-heavy-tail/full-to-balanced-chunk injection and the cited general ordinary C6 theorem.
