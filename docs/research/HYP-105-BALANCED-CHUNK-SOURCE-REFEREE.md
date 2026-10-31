# HYP-105 #230 — AA4-CHUNKREF: independent all-h full physical heavy-tail balanced chunk referee and sharper \(2^{40}\) threshold

**Status:** NEW rigorous all-\(h\) deterministic strengthening and independent original-source audit of the critical [#659](https://github.com/definitely-stable/Mathlab/pull/659) heavy full physical-degree compensation lemma, stacked exclusively on the frozen [#683](https://github.com/definitely-stable/Mathlab/pull/683) integrated-science Draft. Every claim concerns the TRUE original symplectic generalized quadrangle \(W(3,2^h)\), every full separately globally injected and arbitrarily correlated fixed physical point/line pair maps \(f,g\), both diagonals of every original incidence flag, and accepted GF5 D6 sixsets of six **different original source ID flags**. This is not a random completion of \(g\), does not invent values for external graph-theorem constants, and does not independently accept the entire #230 root theorem or merge parents.

## 1. Critical source-input check — exact FULL physical degree sum

For dyadic \(s\ge64\), let
\[
 V=(s+1)(s^2+1),\quad N=V(s+1),\quad
 a=\min\{b:\binom b2\ge V\}.
\]
The *full* original source has \(N\) actual distinct incidence IDs. For every original flag \((p,\ell)\), globally injected \(f(p)\) and \(g(\ell)\) generate **both** distinct opposite-corner physical diagonals, with uniquely recoverable original flag owner because f and g are globally injective. Thus the complete physical graph \(H\) has **exactly \(2N\) ordinary simple undirected edges**, and total degree
\[
 \boxed{\qquad\sum_{v\in V(H)}\deg_H(v)=4N\le8s^4.\qquad}\tag{CHUNK-DEGREE}
\]
The last inequality is the already proved #659 bound \(N\le2s^4\) for every \(s\ge64\).

For ANY real \(T>0\), define the **FULL physical high-degree vertex set** (never recompute after pruning):
\[
 Q_T=\{v:\deg_H(v)>Ts\}.
\]
By the degree sum, **without any probabilistic argument**,
\[
 |Q_T|Ts<\sum_{v\in Q_T}\deg_H(v)\le4N\le8s^4,
 \quad\text{therefore}\quad
 \boxed{|Q_T|\le8s^3/T.}\tag{CHUNK-HEAVY}
\]
This is **TWICE AS TIGHT** as the conservative \(16s^3/T\) used in #659. Because the full vertex alphabet size is \(n=a^2\le4s^3\), one also has \(1\le |Q_T|\le n\) whenever the heavy tail is nonempty.

## 2. Retain SAME original source flag selection, no new stochastic source assumptions

Write \(E_T\) for the number of different physical edges of full \(H\) incident with \(Q_T\). Assume
\[
 E_T\ge\varepsilon s^4,\qquad \varepsilon>0.
\]
Assign each original flag with a heavy physical diagonal ONE fixed actual heavy diagonal witness, preserving its actual ORIGINAL source flag ID. Every original ID has at most two distinct physical diagonals, so there are \(L\ge E_T/2\ge\varepsilon s^4/2\) distinct original flags with assigned heavy witnesses.

The actual original source pencil conflict graph has at most \(M_f+M_g\le2C_s\), with \(C_s\le1.5s^4\). Caro–Wei applied to this ORIGINAL-ID graph gives an independent source-flag set of size at least \(L^2/(4C_s+L)\ge\varepsilon^2s^4/32\). Apply an independent **left-coordinate binary cut**, and then an **independent right-coordinate binary cut** to all whole flags: each cut keeps at least half the chosen original IDs while preserving **BOTH diagonals** for every surviving ID. The resulting fixed selected physical graph \(G\) contains at least
\[
 \boxed{|I_G|\ge \beta s^4,\qquad\beta=\varepsilon^2/2^7,}\tag{CHUNK-SOURCE}
\]
with pairwise nonconflicting ORIGINAL source flag IDs, physical row/column-cherry exclusion, and an actual two-coordinate binary-cut bipartition. All original preassigned heavy witness edges survive. This is the *same* established #659 selector; no change to f,g or their original source geometry.

Every selected physical simple C6 lies in one side-color alternating bipartite graph and has six pairwise distinct left coordinates and six pairwise distinct right coordinates: equal coordinates at distance two would be a row/column cherry, whereas equal coordinates at distance three would violate the typed binary cut. Its six physical edges are backed by six distinct ORIGINAL source incidence flag IDs. The independent original GF5 sixset classification and the #652 physical-to-original D6 injectivity preserve
\[
 \boxed{\#C_6(G)\le D_6(f,g).}\tag{CHUNK-ID}
\]
No equality to any other historical class and no statement about signed \(R_3\) are used.

## 3. NEW rigorous balanced ordinary subgraph — twofold stronger threshold

Choose, for each of the \(|I_G|\) retained ORIGINAL IDs, its actual original heavy witness edge of G. Assign it to one of its endpoints in **original FULL** \(Q_T\). By pigeonhole on the two LEFT-physical binary-color sides of the chosen graph, at least \(|I_G|/2\ge\beta s^4/2\) **distinct physical witness edges** have their assigned high-degree endpoint in the same color side \(X\).

Let
\[
 R=Q_T\cap X,\quad r=|R|>0,\qquad
 Y=\text{the opposite color side of }G,\quad n=a^2.
\]
All selected witness edges counted above join the actual R to actual Y, so the real simple bipartite subgraph \(G[R,Y]\) has at least \(E\ge\beta s^4/2\) distinct edges. By (CHUNK-HEAVY), \(r\le8s^3/T\).

Partition the ACTUAL Y vertices into disjoint chunks of size at most r. There are at most
\[
 \bigl\lceil |Y|/r\bigr\rceil\le\frac{2n}r
\]
chunks because \(1\le r\le n\), \(|Y|\le n\), and \(\lceil z\rceil\le z+1\). By an exact nonprobabilistic pigeonhole argument, one chunk \(Y_*\) satisfies
\[
 \begin{aligned}
 e(F)&\ge\frac{Er}{2n}
       \ge\frac{\beta rs}{16},\\
 v(F)&\le2r\le\frac{16s^3}{T},\\
 e(F)/v(F)&\ge\beta s/32,
 \end{aligned}\tag{CHUNK-BALANCED}
\]
where \(F=G[R,Y_*]\) is an **actual subgraph of the already selected physical G**. R and Y_* are subsets of distinct original physical vertices, no cloned vertices, fake extra edges, synthetic GQ, or forced paired-diagonal assumption for the resulting F. It is okay for F to retain only ONE of a selected original flag's two diagonals: source coherence and original labels are inherited from the larger G.

Let \(C_{\rm graph},c_{\rm graph}>0\) be the **actual (unspecified)** absolute constants of the published **BALANCED** ordinary C6 supersaturation theorem (Jiang–Yepremyan, 2020; incorporating Simonovits): for every ordinary simple graph F,
\[
 e(F)\ge C_{\rm graph}\,v(F)^{4/3}
 \quad\Longrightarrow\quad
 \#C_6(F)\ge c_{\rm graph}(e(F)/v(F))^6.
 \tag{SS6}
\]
By (CHUNK-BALANCED), the **improved sufficient condition** is
\[
 \frac{\beta s}{32}
 \ge C_{\rm graph}\!\left(\frac{16s^3}{T}\right)^{1/3}
 \quad\Longleftarrow\quad
 \boxed{T\ge2^{19}C_{\rm graph}^3\beta^{-3}
          =2^{40}C_{\rm graph}^3\varepsilon^{-6}.}\tag{CHUNK-T}
\]
The old #659 used \(T\ge2^{41}C_{\rm graph}^3\varepsilon^{-6}\). The only improvement is the **exact total FULL physical degree count**, carried through the SAME source-ID coherent selection and SAME actual no-clone chunk, not a change to the external theorem. The achieved ORIGINAL D6 bound is UNCHANGED:
\[
 \begin{aligned}
 D_6(f,g)&\ge\#C_6(F)
 \ge c_{\rm graph}(\beta s/32)^6\\
 &=\boxed{c_{\rm graph}\varepsilon^{12}2^{-72}s^6}.
 \end{aligned}\tag{CHUNK-D6}
\]
Indeed \(\beta^6/32^6=(\varepsilon^2/2^7)^6/2^{30}
=\varepsilon^{12}/2^{72}\).

Therefore at the #672 fixed \(\varepsilon=1/8\) the sufficient heavy-degree cap threshold improves from \(2^{59}C_{\rm graph}^3\) to
\[
 \boxed{T\ge2^{58}C_{\rm graph}^3.}\tag{CHUNK-ROOT}
\]
The original threshold \(2^{59}C^3\) and every parent #672–#683 proof remain valid and unchanged; the new threshold is a strictly stronger input one may use in a separately audited future root-threshold optimization. The published external constants C,c are **not numerically specified**, and no numeric actual \(h_0\) is claimed.

## 4. Independent REAL original-source and abstract finite falsifiers

The NEW \`research/hyp105_balanced_chunk_source_referee.py\` implements an independent no-clone bipartite chunk enumerator and independently reconstructs:
- TRUE W(3,2) or W(3,4) original source flags and physical paired diagonals from complete globally injected fixed f,g;
- FULL physical heavy vertex set and actual provenance-preserving physical heavy witness per ORIGINAL flag;
- ORIGINAL source-ID conflict graph by independently comparing all ORIGINAL flag pairs, plus min-current-degree Caro–Wei greedy lower with EXACT Fraction scores;
- both typed coordinate binary cuts from their independent conditional expectations, both original flag diagonals retained together;
- assignment of real selected original heavy witness edges to one full-H heavy physical endpoint, both side-color populations, construction of the ACTUAL uncloned F=G[R,Y_*];
- independent direct enumeration of all physical selected C6, their six DISTINCT original source ID owners, original point and line factor uniqueness, historical accepted GF5 D6 classifier, and uniqueness of the original source sixset across physical cycles; a direct check of every simple C6(F) as a subset of C6(G).

The NEW \`research/test_hyp105_balanced_chunk_source_referee.py\` independently checks the **entire \(2^{12}=4096\) labeled 3×4 ordinary bipartite graphs and all \(2^3-1=7\) nonempty R subsets**, i.e. **28672 no-clone chunk cases**, with direct counting of each retained physical edge, chunk totals, physical vertex counts, exact rational density and the correct 2n/r ceiling. It also tests five legal globally injected right-g reassignments on true W32, full/reassigned adversarial W34 source, a TRUE W34 original planted protected K4,4 control with 96 accepted ORIGINAL D6 sixsets (old #659 oracle used **only as comparison**), malformed original ID subsets, and independent exact Fraction tests for all symbolic C,c,epsilon inputs. The reported rational trial values are placeholders to falsify the **constant algebra**, not real graph theorem constants.

For every true original source case, finite code also verifies selected-graph original source flag count, BOTH physical diagonals, every surviving original heavy witness, Caro–Wei lower, both typed cuts, un-cloned actual F and exact original source GF5 D6. No source-random f/g experiment or synthetic GQ is used.

## 5. Acceptance / further required review

This is a **new deterministic all-h improvement and independent referee of a specific root bottleneck**: sharpen physical heavy-degree bound and independently check the no-clone balanced chunk and physical-to-original source injection. It does not independently prove the external balanced supersaturation theorem itself, prove the whole of #672's FULL/core projection block bounds, assign actual C,c values, infer finite h≤h0 coverage, establish a signed R3 equality or ASET exponent, or qualify as independent expert peer review.

**Scientific STOP:** leave #230 OPEN_WITH_FORMAL_BLOCKER, no changes to main/ancestor PRs and no merges. Root acceptance requires an independent extremal-combinatorics referee to validate external hypotheses and the complete source-ID proof chain. The recommended next critical slice is independent FULL/core four-orientation internal-blocker proof; do not spend remaining time repeatedly tweaking constants without genuine new information.
