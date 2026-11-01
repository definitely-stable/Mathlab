# HYP-105 / #230 — AA4-WALKMOBIUS: exact bipartite sixth-walk Möbius referee

**Scientific Draft**, stacked STRICTLY on frozen [#702](https://github.com/definitely-stable/Mathlab/pull/702), immutable parent HEAD \`89e365e06210bc157bf8099b9cbd00935be6f82b\`. Only four new files; no parent/main mutations, merges or issue closure. This is an independent audit of an important **universal ordinary-graph input** used for the dense-core Jensen/trace transfer, not a new source \(s^6\) lower, a new exponent, or independent qualified peer acceptance. The scientific root #230 remains \`OPEN_WITH_FORMAL_BLOCKER\`.

## 1. Precise mathematical audit target and attribution

Historical [#672](https://github.com/definitely-stable/Mathlab/pull/672) and [#686](https://github.com/definitely-stable/Mathlab/pull/686) require for a true simple bipartite ordinary graph \(G\) with \(m=e(G)\), maximum degree \(\Delta\) and adjacency matrix \(A\):

\[
\operatorname{tr}(A^6)\le 12C_6(G)+6\Delta\operatorname{tr}(A^4)
\le 24C_6(G)+72m\Delta^2.
\tag{W1}
\]

The factor **72 is ALREADY present in #686**; the conservative new integrated root [#702](https://github.com/definitely-stable/Mathlab/pull/702) permits \(144m\Delta^2\) and \(L_6=24+576T^2\). This slice **does not misattribute either bound as newly discovered**. The new mathematical certificate is a more exact identity that decomposes **EVERY** closed 6-walk into injective cycles and collision strata using the lattice Möbius inversion of equality patterns among the three alternating left and three alternating right vertices. The independent ordinary-graph trace approach is logically different from the triple-codegree \(C_6\) formula of [#691](https://github.com/definitely-stable/Mathlab/pull/691) and the source-six-ID canonical inverse of #699.

## 2. NEW exact all-bipartite six-walk versus injective-cycle identity

Fix ANY finite simple bipartite \(G=(X,Y,E)\), allowing uneven sides, isolates, disconnected components and arbitrary degree concentration. Let \(d(v)\) be the real vertex degree and \(c_X(x,x')=|N(x)\cap N(x')|\), \(c_Y(y,y')=|N(y)\cap N(y')|\), **including** \(c(v,v)=d(v)\). Define the true nonnegative graph statistics

\[
\begin{aligned}
W_6&=\operatorname{tr}(A^6),\quad W_4=\operatorname{tr}(A^4),\quad m=|E|,\\
H&=\sum_{x,x'\in X}d(x)c_X(x,x')^2+
   \sum_{y,y'\in Y}d(y)c_Y(y,y')^2,\\
D_3&=\sum_{v\in X\cup Y}d(v)^3,\qquad
D_2=\sum_{v\in X\cup Y}d(v)^2,\\
P&=\sum_{\{x,y\}\in E}d(x)d(y).
\end{aligned}
\tag{W2}
\]

Then the EXACT signed integer **all-graph equality** is

\[
\boxed{
12C_6(G)=
W_6-6H+4D_3+6W_4+6P-12D_2+8m.
}
\tag{W3}
\]

Here \(C_6\) is the number of ordinary **unrooted unoriented simple** cycles on SIX pairwise distinct vertices; no multiple-edge graph interpretation, no factor-six correction left unspecified.

**Direct proof by six-slot partition Möbius inversion, completely independent of #691.** A rooted oriented closed six-walk starting on the X side has an alternating representation

\[
x_0-y_0-x_1-y_1-x_2-y_2-x_0.
\]

There are \(W_6/2\) such representations; equality of the two parity-rooted halves follows because the nonzero spectra of the two bipartite Gram matrices agree. To be injective the three \(x_i\) and separately the three \(y_j\) must each be pairwise distinct. For three positions, the exact distinctness indicator is

\[
1-\bigl([0=1]+[1=2]+[0=2]\bigr)+2[0=1=2].
\]

Multiply that expression independently for X and Y. Enumerate its equality strata by **DIRECT** graph homomorphism counting:

- A specified equality of two X positions contributes \(\sum_{x,x'}d(x)c_X(x,x')^2\); a specified equality of two Y positions is the dual. There are three choices on each parity side.
- All three X positions equal contributes \(\sum_xd(x)^3\), and all three Y positions equal contributes the dual.
- Among the NINE ways to impose one X pair equality and one Y pair equality, **SIX** give \(\sum_{x,x'}c_X(x,x')^2=W_4/2\), and the other **THREE** give \(P=\sum_{\{x,y\}\in E}d(x)d(y)\). This is an essential alignment distinction: replacing all nine by \(W_4/2\) is INCORRECT on irregular graphs.
- All X positions equal plus a specified Y pair equality contributes \(\sum_xd(x)^2\); dually all Y equal plus an X pair equality contributes \(\sum_yd(y)^2\). There are three choices each.
- All six positions collapse within their individual parity classes to one X and one Y vertex, contributing \(m\).

After combining the \(1,-3,+2\) factors on both alternating sides, the number of injective 6-walks rooted on X equals

\[
6C_6=
\frac{W_6}{2}
-3H+2D_3
+6\frac{W_4}{2}+3P
-6D_2+4m.
\]

Multiply by two to obtain (W3). This derivation is an exact combinatorial proof for **ALL** finite simple bipartite graphs; no numerical, randomized, or finite-geometry extrapolation.

**Important audit stress point:** the mixed pair-equality contribution \(P\) is distinct from the codegree-square contribution on irregular graphs. The new implementation explicitly records both \(P\) and the parity-specific \(H\), preventing accidental replacement of the full six-walk degeneration structure by a single scalar count.

## 3. Independent universal moment inequalities and source transfer

Every NONINJECTIVE rooted closed six-walk in a simple bipartite graph contains a vertex return at cyclic distance two. Delete that two-edge backtrack to obtain a rooted closed four-walk. There are at most SIX rooted positions for reinsertion, and each has at most \(\Delta\) choices. Therefore

\[
0\le W_6-12C_6\le6\Delta W_4.
\tag{W4}
\]

The symmetric real adjacency spectrum gives the Cauchy inequality

\[
W_4^2\le\operatorname{tr}(A^2)\operatorname{tr}(A^6)
=2mW_6.
\tag{W5}
\]

Use \(6\Delta\sqrt{2mW_6}\le W_6/2+36m\Delta^2\) to deduce

\[
\boxed{W_6\le24C_6+72m\Delta^2.}\tag{W6}
\]

The exact identity (W3), verified by a completely separate count, is a **stronger falsifier** of the walk-compression inequalities (W4)–(W6) than merely testing their final bound. It does not assert all noninjective walks are individually uniquely assigned to a backtrack, nor that arbitrary graph \(\Delta\) is comparable to its average degree.

For the actual ORIGINAL coherent selected graph \(G\) constructed from the TRUE W(3,s) flag source and two complete typed binary cuts (#659/#699), the original-six-ID injection gives \(C_6(G)\le D_6(f,g)\), with genuine original flag ownership for EACH physical edge. The existing dense-branch m≤4s⁴ and Δ≤Ts imply via (W6)

\[
\operatorname{tr}(A_G^6)\le
24D_6(f,g)+288T^2s^6.
\tag{W7}
\]

This sharpened constant was **previously available in #686**. The current #702 \(L_6=24+576T^2\) remains conservative and valid. Applying (W7) in any next root ledger would require changing all dependent \(\sigma_3\), \(L_4\) and loss computations consistently on a separate stacked PR, never silently rewriting an inherited proof threshold.

The external graph input remains different: Jiang–Yepremyan (2020, CPC 29(5), 698–721; DOI 10.1017/S0963548320000206) records the ordinary-graph Simonovits supersaturation statement \(e(G)\ge Cn^{4/3}\implies C_6(G)\ge c(e(G)/n)^6\) with positive **existential** constants. Neither (W3) nor (W6) supplies those constants; they do NOT remove the need for this published extremal-combinatorics theorem in the heavy branch.

## 4. Truly independent finite falsifiers

The new standalone \`research/hyp105_bipartite_sixwalk_mobius_moment_referee.py\` implements (W3) entirely in integer arithmetic using actual left- and right-side rows, computes \(\operatorname{tr}(A^4)\) and \(\operatorname{tr}(A^6)\) separately from the **two parity Gram** powers, and asserts the exact equality of their spectral traces. The module never imports any #691 codegree C6 formula, previous ordinary six-cycle DFS, source sixset classifier or old root calculator.

The new TESTS crosscheck the resulting exact \(C_6\) against two independent old sources used ONLY as adversarial oracles, and also against a separately implemented full rooted SIX-STEP physical adjacency DFS at selected bounded sizes. They exhaust **ALL 4096 labelled 3×4** and **ALL 65536 labelled 4×4** simple bipartite graphs, check disconnected/isolated/highly degree-irregular controls, all complete \(K_{u,v}\) for \(u,v\le6\), \(C_6\) and two copies of \(K_{4,4}\). They verify the exact-integer spectral Cauchy (W5), backtrack upper (W4) and \(72m\Delta^2\) (W6) on every input, not a few graph examples.

A separate genuinely independent adapter reconstructs true-original W(3,2) and W(3,4) incidence ID flags (only importing \`genuine_source\` as finite geometry input), checks complete separately injected correlated fixed f,g and the ORIGINAL conflict-free selector/two typed binary cuts, builds exactly BOTH real physical diagonals of every selected true original ID, preserves unique original edge ownership, then checks (W3) on the actual selected physical bipartite graph. A protected original W(3,4) 16-source-ID K4,4 control must yield exactly **96 ordinary physical C6** with all source provenance intact. These finite tests do NOT imply that a selected graph always contains a positive six-cycle — actual admissible W32 cuts may be acyclic.

**STOP:** This is a fully independent universal ordinary-graph moment identity audit, NOT a new external SS6 theorem, not a proof of full HYP-105 Branch A, no published numerical C,c or actual h0, no new ASET exponent. Root remains OPEN_WITH_FORMAL_BLOCKER, parents/main unchanged, every scientific PR Draft/unmerged. Next mathematical acceptance gate should be independent outside peer review of entire original-source heavy/dense manuscript; a newly found adversarial breach in any critical inherited lemma must be fixed before such review.
