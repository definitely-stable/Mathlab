# HYP-105 #230 — AA4-ROOT-PUBLICATION-HEAVY-SRG-REFEREE

**Status:** original HEAVY source-spectrum/Caro–Wei/physical top-r F all-order mathematical referee; independent genuine finite W(3,2)/W(3,4) falsifiers. **Root OPEN_WITH_FORMAL_BLOCKER**, NOT PROVED_A or GF5/ASET R3. Strict Draft child of [PR #782](https://github.com/definitely-stable/Mathlab/pull/782), parent frozen HEAD \`8284ef190ed14db775147c98cc6a2da3815020f5\`. No parent, sibling or main mutation; no merge.

## 0. Precise scientific verdict, originality and remaining root gates

The target [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) is the original **seven-positive-class unweighted six-incidence-ID** lower bound \(\inf_{f,g}S_s(f,g)=\Omega(s^6)\), for genuine symplectic \(W(3,s)\), \(s=2^h\to\infty\), with actual globally minimal physical alphabet and EVERY fixed, separately globally pair-injective, arbitrarily correlated \(f:P\hookrightarrow\binom{[a]}2,\ g:L\hookrightarrow\binom{[a]}2\).

Recent inherited strict Drafts: #775 original SRG source conflict bound, #776 minimal actual physical alphabet, #777 source-owned unrounded top-r, #778 combined HEAVY R33281 and original LOW W3, #779 expected one-priority/two-cut sixth/fourth moment, #780 original FULL A versus paired CORE C mixed book and GQ endpoint, #781 source-positive BBo six-ID zero/two inverse and 3/9 alignment, #782 exact original source coordinate returns and 17T/49T LOW error. The local mathematical statements are NOT invented here. The new contribution is an **independent single-piece, first-principles publication-level derivation** of the entire all-h HEAVY source J spectral upper bound **including its delicate 23/16 coefficient**, then source Caro–Wei, TWO coherent whole-owner source cuts, genuinely unrounded physical top-r F and the external simple graph theorem applicability, together with new implementation pathways that do NOT import any preceding J/Caro–Wei/physical HEAVY algorithm.

The logical HEAVY **source-graph construction** is now independently mathematically accepted conditional only on the classical published ordinary graph \(C_6\) theorem and the separately accepted true original HEAVY \(C_6\to D_6\) source-sixset injection. The other half, **LOW_PRODUCED**, is NOT promoted to publication acceptance by these calculations; in particular all inherited mixed-source original book, Jensen moment and sixset-class premises remain separately open for final proof-level signoff. A finite green CI is NOT a proof of a general \(s\) bound.

## 1. Original GQ source and strongly regular collinearity spectrum, all orders

Fix any dyadic \(s=2^h\). Genuine symplectic \(W(3,s)\) is a generalized quadrangle of order (s,s); ORIGINAL point and line sets each have \(V=(s+1)(s^2+1)\) members, and its exactly \(N=(s+1)^2(s^2+1)\) incident **named original flag IDs** form \(I\).

Let \(G_P\) be the ordinary undirected graph on ORIGINAL points joining two distinct points when they lie on a common ORIGINAL line. Let \(G_L\) be the dual graph on ORIGINAL lines joining two distinct lines when they intersect at an ORIGINAL point. Both are strongly regular with exactly
\[
\boxed{(v,k,\lambda,\mu)=\big((s+1)(s^2+1),\ s(s+1),\ s-1,\ s+1\big).}\tag{HR-1}
\]

Derivation without invoking external numerical source constants: each point lies on \(s+1\) lines and each line contains s other points, giving \(k=s(s+1)\), no duplicates by unique original line for two collinear points. Two adjacent points have the s−1 other points of their common original line as common neighbors; no off-line triangle occurs in any GQ (girth 8 of the incidence graph). Two nonadjacent points: for each of s+1 lines through the first, the GQ axiom supplies exactly one neighbor on that line collinear with the second, giving \(\mu=s+1\). The point–line dual proof is the same, using original line intersection.

The adjacency equation
\[
A^2=kI+\lambda A+\mu(J-I-A)
\]
implies every nontrivial eigenvalue \(\theta\) solves \(\theta^2+(\mu-\lambda)\theta-(k-\mu)=0\). Because \(\mu-\lambda=2\) and \(k-\mu=s^2-1\), its two roots are precisely
\[
\boxed{\theta_+=s-1,\qquad\theta_-=-s-1.}\tag{HR-2}
\]
For ANY original point/line subset \(U\) of size \(m\), decompose its indicator into the constant all-one vector and orthogonal part. Since the maximum nontrivial eigenvalue is s−1, the actual induced original collinearity edges satisfy
\[
\boxed{
2e_{G_P}(U),\,2e_{G_L}(U)
\le\frac{k}{V}m^2+(s-1)\left(m-\frac{m^2}{V}\right)
\le\frac{k}{V}m^2+(s-1)m.
}\tag{HR-3}
\]
This is a **positive-side** spectral bound; using the negative eigenvalue \(-s-1\) instead would be incorrect for an upper edge bound.

## 2. Original SOURCE pencil conflict J for arbitrary *fixed* correlated f/g

Let \(a=\min\{b:\binom b2\ge V\}\). Fix arbitrary globally complete separately pair-injective source maps f/g **once**; no randomness in their labels is assumed. Every ORIGINAL point p maps to exactly two first symbols f(p), every ORIGINAL line ell to exactly two second symbols g(ell).

Define the genuine undirected conflict graph \(J\) on the named ORIGINAL incidence flags. Two *distinct* flags conflict on the point side iff they have the SAME ORIGINAL point and their ACTUAL g-line unordered pairs intersect; on the line side iff they have the SAME ORIGINAL line and their ACTUAL f-point pairs intersect. Distinct named flags never share both original factors, so these two types have disjoint edge sets:
\[
e(J)=e_P(J)+e_L(J).
\tag{HR-4}
\]

For any physical second symbol \(y\), let \(L_y=\{\ell\in L:y\in g(\ell)\}\), a REAL subset of original L. Globally injected g realizes different original lines as different edges of ordinary \(K_a\); at most a−1 such edges meet any vertex y, so \(|L_y|\le a-1\). Each original line appears in exactly TWO such symbol fibres, hence \(\sum_y|L_y|=2V\), and
\[
\sum_y|L_y|^2\le(a-1)\sum_y|L_y|=2V(a-1).
\tag{HR-5}
\]

An original flag pair with one repeated original point and overlapping g-line symbols corresponds to exactly ONE pair of distinct original lines meeting on an original point, and their two injected g-pairs intersect in exactly ONE physical y. Thus, literally, with no overcount or independence,
\[
e_P(J)=\sum_y e_{G_L}(L_y).
\]
Applying HR-3 separately to every actual L_y,
\[
e_P(J)\le \frac12\sum_y\left(\frac{k}{V}|L_y|^2+(s-1)|L_y|\right)
\le k(a-1)+(s-1)V.
\tag{HR-6}
\]
Completely independently with the actual physical first symbols \(P_x=\{p:x\in f(p)\}\), point graph \(G_P\) and source line pencils,
\[
\boxed{e_L(J)\le k(a-1)+(s-1)V.}\tag{HR-7}
\]
Consequently
\[
\boxed{e(J)\le2\big[s(s+1)(a-1)+(s-1)(s+1)(s^2+1)\big].}\tag{HR-8}
\]
No additional original source regularity condition, stochastic f/g correlation assumption, arbitrary f/g permutation averaging or replacement of the physical paired flags has entered.

### A delicate all-h coefficient: independently justify the **same** M_H from #775

Minimality of the ACTUAL global source alphabet a means \((a-2)(a-1)<2V\), hence \(a-1<\sqrt{2V}+1\). For \(s\ge256\), set \(t=1/s\), so \(0<t\le1/256\). Direct rational squaring gives
\[
2(1+t)(1+t^2)
\le 2(1+1/256)(1+1/256^2)
< (10/7)^2.
\tag{HR-9}
\]

Therefore \(\sqrt{2V}<\frac{10}{7}s^{3/2}\) and
\[
\frac{k(a-1)+(s-1)V}{s^4}
<1-t^4+\frac{10}{7}\sqrt t(1+t)+(1+t)t^2.
\tag{HR-10}
\]
Compare this with \(M(s)=(1+t^2)(1+\frac{23}{16}\sqrt t)\). Their difference satisfies
\[
M(s)-\left(1-t^4+\frac{10}{7}\sqrt t(1+t)+(1+t)t^2\right)
=\sqrt t\left[
\frac1{112}-\frac{10}{7}t+\frac{23}{16}t^2-t^{5/2}+t^{7/2}
\right].
\tag{HR-11}
\]

For **EVERY** \(0<t\le1/256\), the bracket is strictly positive, because
\[
\frac1{112}-\frac{10}{7}\frac1{256}-\frac1{256^2\cdot16}>0,
\]
with both discarded \(\frac{23}{16}t^2\) and \(t^{7/2}\) nonnegative. This is an exact rational inequality. Therefore the original source bound from #775 follows **independently and for ALL s≥256**, not by fitting true W(3,2)/W(3,4) samples:
\[
\boxed{e(J)<2M(s)s^4\le2M_Hs^4,\quad
M_H=(1+2^{-2H})(1+23/(16\cdot2^{H/2})),\
s\ge2^H,\ H\ge8\text{ even}.}\tag{HR-12}
\]
The monotonicity of the positive factors in M(s) gives \(M(s)\le M_H\) immediately. This calculation also identifies the **actual safety margin** required by the 23/16 choice and does not silently replace \(\sqrt2\) with 23/16 and incorrectly lose \(1/s\) correction terms. A coarse 23/16 substitution made too early in HR-10 can fail to establish the stated M_H; the independent rational margin 10/7 avoids this problem.

**Scope:** the exact HR-8 is true even below s=256; only the universal fixed-envelope simplification HR-12 assumes s≥256.

## 3. All-h HEAVY one frozen full original source, Caro–Wei and TWO true symbol cuts

Fix even H=32 BEFORE any s/f/g and use the true globally minimal physical alphabet. Define the real physical full graph \(H\) on all \(a^2\) physical corners, whose exactly \(2N\) genuinely distinct edges consist of BOTH opposite diagonals of EACH original flag. Every physical edge changes BOTH typed coordinates; f/g injectivity determines its unique ORIGINAL source owner.

Fix one global \(T>0\) BEFORE source f/g. Freeze the real predeletion physical high degree set
\[
Q_T=\{v:d_H(v)>Ts\},\qquad
E_T=\#\{e\in E(H):e\cap Q_T\ne\varnothing\}.
\]
This is a count of DISTINCT physical undirected real edges, not source owners or an oriented walk count. In the HEAVY alternative \(E_T\ge s^4/8\), select the set L of ALL named original incidence owners of these Q-touching edges. Each original source flag owns exactly two real edges, so \(|L|\ge E_T/2\ge s^4/16\).

Turan/Caro–Wei on the ACTUAL induced original conflict graph \(J[L]\), using HR-12, yields an independent set I0 of genuinely named whole ORIGINAL owner flags of cardinality
\[
\begin{aligned}
|I_0|
&\ge\frac{|L|^2}{|L|+2e(J[L])}
\ge\frac{|L|^2}{|L|+2e(J)}\\
&>\boxed{\frac{s^4}{16(1+64M_H)}}.
\end{aligned}
\tag{HR-13}
\]
All its original source flags are distinct, no edge is cloned, and I0 is actually J-independent.

Use **one globally coherent** binary color per first physical symbol. Every actual original f(p) pair crosses a random cut with probability EXACTLY 1/2. By linearity, some single coherent first cut retains at least |I0|/2 flags, without requiring different flags to be independent. For those owners, independently use **one globally coherent second-symbol binary cut** and retain at least half again. Conditional-expectation sequential bit assignments can construct both cuts deterministically. We get one actual genuine original J-independent WHOLE-ID set S:
\[
\boxed{|S|\ge|I_0|/4>
\frac{s^4}{64(1+64M_H)}.}\tag{HR-14}
\]
Both original opposite diagonals of EVERY S owner cross BOTH typed cuts. This step is not a random selection of different physical diagonals or an independent label f/g relabeling.

Each i∈S still has at least ONE pre-existing Q-touching real source-owned edge because it was selected from L and both diagonals remain in the globally cut physical graph. Fix a single such edge and an actual heavy endpoint q_i∈Q_T. Pigeonhole the FIRST symbol cut bit of q_i: for some bit b, at least |S|/2 DISTINCT original owners have a witness q_i of bit b. Let
\[
R_Q=\{q\in Q_T:b_x(q_x)=b\},\quad r=|R_Q|\ge1.
\]
Let Y be the actual set of other-side, opposite-first-bit physical vertices adjacent by REAL selected S-owned edges to R_Q, with y=|Y|≤a². Let E denote the number of DISTINCT real selected R_Q−Y edges. Every selected owner has exactly one named physical witness and source ownership is unique, so \(E\ge|S|/2\).

## 4. Real opposite physical TOP-r F (no bins, no edge cloning)

Choose \(Y_*\) as the \(\min(r,y)\) actual vertices of Y with highest actual number of S-selected real edges to R_Q. The degree averaging inequality for the actual finite simple R_Q×Y graph is
\[
\boxed{\sum_{v\in Y_*}d_{R_Q}(v)
\ge E\min(1,r/y)\ge Er/a^2.}\tag{HR-15}
\]
When y≥r this is the average of the highest r degrees among y actual physical vertices. When y<r choose ALL y, giving E≥Er/a² since r≤a². Neither a ceiling in the number of chunks nor a hypothetical copy of an overfull physical vertex is used.

Let F consist of ONLY those actual original S-owned physical edges joining R_Q to Y*. All its physical vertices and edges occur in the frozen true full source H; it is a SIMPLE ordinary undirected bipartite physical graph under the selected first-coordinate bit cut. Although initially paired ownership of S was essential to preserve heavy witnesses and cuts, F is permitted to delete individual diagonals of S owners: every remaining edge still has its uniquely determined ORIGINAL owner. Since its nonisolated true physical vertex set has at most r+min(r,y)≤2r vertices, HR-15, E≥|S|/2 and n=a² give
\[
\boxed{
\frac{e(F)}{v(F)}
\ge\frac{|S|}{4a^2}
>\frac{s}{256 A_H(1+64M_H)},\
A_H=\frac{\text{upper bound on }a^2}{s^3}.
}\tag{HR-16}
\]

**Independently check actual a² bound:** a<√(2V)+2, and for s≥2^H with H≥8, \(V/s^3\le(1+2^{-H})(1+2^{-2H})\) and \(V\le(33/32)s^3\). Since \((23/16)^2>2(33/32)\), \(\sqrt{2V}<(23/16)s^{3/2}\). Therefore
\[
\boxed{
a^2<A_Hs^3,\
A_H=2(1+2^{-H})(1+2^{-2H})
+\frac{23}{4\cdot2^{3H/2}}+4\cdot2^{-3H}.}\tag{HR-17}
\]
Here the 23/16 is used in a simple positive **upper** algebraic bound that is actually legitimate. Keep both variants HR-9/10 and HR-17 distinct; interchanging them silently could lose the proof of the separate stricter M_H.

The all-order exact-rational HEAVY threshold is
\[
R_H=\left\lceil256A_H(1+64M_H)\right\rceil,\qquad
\boxed{R_{32}=33281.}\tag{HR-18}
\]
Consequently \(e(F)/v(F)>s/R\). The full H has degree sum 4N; by the defining strict frozen Q degree threshold,
\[
|Q_T| Ts<\sum_{v\in Q_T}d_H(v)
\le4N.
\]
At s≥64, the genuine source \(4N\le(17/4)s^4\), so
\[
\boxed{
v(F)\le2|Q_T|<\frac{17}{2}\frac{s^3}{T}.}\tag{HR-19}
\]
No source geometry or clock-dependent probabilistic constants were secretly changed by the top-r construction. Both HEAVY and complementary LOW use the SAME single globally frozen original Q_T and T.

## 5. Ordinary GRAPH C6 theorem: correct published provenance, normalization and source inverse

The necessary external theorem is the **classical Simonovits supersaturation theorem for simple UNDIRECTED ordinary graph C6**, not a theorem about hypergraphs or closed trace sixwalks. Its k=3 specialization supplies positive constants \(C_{\rm graph},c_{\rm graph}\), depending only on length six, such that any finite simple graph F with
\[
e(F)\ge C_{\rm graph}\,v(F)^{4/3}
\]
has at least \(c_{\rm graph}(e(F)/v(F))^6\) UNORIENTED ordinary simple sixcycles. **No numerical C_graph or c_graph is established in this repo.** Source check: Jiang–Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, Combinatorics, Probability and Computing 29 (2020), 698–721, DOI 10.1017/S0963548320000206, introduction/abstract explicitly attributes the ordinary graph supersaturation to Simonovits and extends it to hypergraphs. The 2020 paper is not a source for any fictitious C0=1 numeric claim. URLs: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/supersaturation-of-even-linear-cycles-in-linear-hypergraphs/240493C1F42618819DA9B16CE7F3E4BD and https://arxiv.org/abs/1707.03091.

Choose **once**, before s/f/g, unknown rational \(C_0\ge\max(1,C_{\rm graph}),0<c_0\le\min(1,c_{\rm graph})\). With the ACTUAL new R33281 choose the one global
\[
T=\left\lceil\frac{17}{2}R^3C_0^3\right\rceil.
\]
From HR-18/HR-19,
\[
v(F)<\frac{17s^3}{2T}\le \left(\frac{s}{RC_0}\right)^3
\le\left(\frac{e(F)}{v(F)C_0}\right)^3.
\]
Thus the graph theorem is applicable to precisely the real ordinary F and gives at least \(c_0(s/R)^6\) physical **unoriented** sixcycles.

A selected F may retain only ONE diagonal of a selected owner; the earlier independent all-h original source inverse [#772](https://github.com/definitely-stable/Mathlab/pull/772) specifically allows physical edge deletion. Under original source J independence and BOTH coherent symbol cuts, every simple F sixcycle has six distinct first symbols and six distinct second symbols: cyclic distance 1 by actual diagonal changes, distance 2 by source point/line pencil J independence, distance 3 by parity of the corresponding global cut. Consequently its six actual edge owners have distinct original points and lines, and the full original factor-cycle inverse injects it into a unique original D6 six-ID source set. There is NO 6!, 12 or clone multiplicity loss. This latter source inverse is **independently accepted elsewhere**, not reproved in the present HEAVY paper; global ROOT proof signoff still has to review its exact historical positive six-class membership.

Thus, **conditional only on the separately sourced original D6 class positive six-ID inverse and externally published Simonovits graph theorem**, the newly independently certified HEAVY source construction gives
\[
\boxed{\mathrm{HEAVY}\implies D_6(f,g)\ge
\frac{c_0}{33281^6}s^6.}\tag{HR-20}
\]

## 6. Genuine finite false-case tests and scientific STOP

The executable independent original referee does not import previous J, SRG, Caro–Wei, top-r, physical source owner, GF5, selected moment, C6 or root calculators. It imports ONLY the genuine symplectic W(3,2)/W(3,4) named incidence constructor (source fixture). All other mathematical objects and algorithms are reimplemented independently.

For every TRUE W32/W34 and lex/reverse/shift COMPLETE globally injected fixed f/g source map, six total cases:

1. Build FULL original I=(point,line) flag IDs and all point/line incidence pencils from scratch; rebuild both actual ORIGINAL point and line collinearity graphs. Verify the *complete* strongly regular adjacency parameters HR-1, including every adjacent and nonadjacent pair's precise common-neighbor count. Independently compute both source J point-pencil and line-pencil conflicts, and both physical-symbol-fibre SRG induced-edge energies; demand their exact equality and each symbolic spectral HR-6/7 upper bound.
2. Build every genuine original physical edge from exactly two opposite diagonals per named source ID. Assert full physical edge cardinality exactly 2N, unique source ownership and the actual full degree per real physical vertex.
3. Freeze separately three diagnostic Q_T scenarios T∈{0,1,2}. These are **small-source structural falsifiers, NOT actual astronomical ROOT T**. Independently construct the named Q-touching heavy-owner set, implement a genuine original J-induced greedy Caro–Wei independent set, choose TWO actual coherent whole-source bit cuts using **global conditional expectations over all real typed symbols**, retaining at least a quarter of original independent selected flags.
4. Select one Q-touching physical witness per retained actual source owner, choose a genuine majority Q-first-bit, select its actual R_Q vertices, and choose actual top-r degree Y corners. Verify source witness ≥|S|/2, actual top-r edge averaging, true F physical edges and original owner IDs, **no clone**, \(|V(F)|\le2|R_Q|\), \(e(F)/v(F)\ge|S|/(4a^2)\) with exact Fraction. This is NOT a synthetic expected-value graph.
5. Independently compute three **FORMAL ONLY** external C0,c0 rational scenarios (1,1),(2,1/5),(7/3,1/17), with correct common global HEAVY T and δ and no fake published numerical constants or root proof promotion.

Mandatory **22 independent tests** and GitHub-hosted Ubuntu24/Python3.12 specialist (push + PR) fail closed if any TRUE original flag ownership, SRG λ/μ, J/SRG edge count, global symbol bit cut, Caro–Wei, witness, unrounded top-r F density or quantifier check fails. At least six true W32/W34 diagnostic heavy F cases must be **nonempty**, preventing vacuous certifications; a JSON source-certificate artifact is uploaded on specialist CI success. Full Research and INDEX are required on the exact final child HEAD for engineering acceptance.

**First remaining scientific gate:** an independent publication-level all-order LOW_PRODUCED referee combining the physical 3walk exact disjoint partition, GQ endpoint exception, spectral selected sixth/fourth moments under ONE source selector, full original A=I versus paired C mixed point/line books, original 0/2-produced positive six-ID BBo, and the exact s0/δ quantifiers. This is the next gate, not a further irrelevant HEAVY numerical rounding cycle. Root #230 remains OPEN_WITH_FORMAL_BLOCKER and all PRs Draft; no merge, main edit, issue closure or ASET exponent.
