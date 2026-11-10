# HYP-105 #230 — AA4-DMID-ORIENT: all-h ORIGINAL middle-diagonal orientation gate and external-source J obstruction

**Scope and provenance.** A strictly stacked Draft descendant of [#758](https://github.com/definitely-stable/Mathlab/pull/758), frozen source HEAD \`2edc5766a0307490fcd567234eb369dcfcbb2a32\`. Original root #230 remains OPEN_WITH_FORMAL_BLOCKER. This slice resolves a *specific genuinely mathematical* disjoint-original-middle obstruction rather than optimizing another same-middle constant. The parent established, rigorously for all dyadic GQ orders, GQ no-K2,2 and sharp at most THREE physical P3 paths per ordered endpoint family per named original middle flag; complete W34 fixed-label source data assigned nearly 90% of incompatible B mass to different original middle points AND different middle lines. Those percentages were finite fixed-map observations, NOT a universal law.

The new all-h theorem classifies **coordinate-typed** incompatibility of paths with different ORIGINAL middle points AND lines in terms of overlapping point/line physical label pairs. It proves an exact finite 4x4 and sharp 3x3 orientation combinatorics, and it explicitly isolates the residual **SOURCE-J owner conflict** that can defeat the otherwise compatible orientations. A new full W32/W34 fixed source program independently reconstructs that obstruction; numerical data are finite evidence, not a global B75 theorem or infinite family.

## 1. Real ORIGINAL point/line middle flags, not fake graph edges

For ANY \(s=2^h\), true symplectic GQ \(W(3,s)\), complete separately globally pair-injective fixed label maps

\[
f:P\hookrightarrow {[a]\choose2},\qquad
g:L\hookrightarrow {[a]\choose2},
\]

arbitrary mutual correlation, original deletion Z and retained paired named source incidence CORE C, let each true flag \(i=(p,\ell)\in C\) own precisely TWO physical undirected opposite diagonals on its original four-corner rectangle \(f(p)\times g(\ell)\). Each has FOUR directed middle diagonals, corresponding to independent choices of the x-coordinate direction and y-coordinate direction.

Take two true directed coordinate-proper physical P3s \(\gamma=(u,a,b,v)\) and \(\eta=(u,c,d,v)\) with the SAME ordered physical endpoints, and with genuine named ORIGINAL middle incidence owners

\[
i=(p,\ell),\quad j=(q,m),\qquad p\ne q,\quad \ell\ne m.
\tag{DM-1}
\]

Because the maps are separately globally pair-injective, their first middle pair labels \(f(p),f(q)\) are different two-element subsets of the same alphabet, so intersection has size **0 or 1**, and likewise for \(g(\ell),g(m)\). Define the two source-overlap bits

\[
\alpha=|f(p)\cap f(q)|\in\{0,1\},\qquad
\beta=|g(\ell)\cap g(m)|\in\{0,1\}.
\tag{DM-2}
\]

These are original named physical label pair intersection facts; no distributional assumptions on f/g are made.

The true original source conflict graph J has edges only between ORIGINAL flags sharing a source point or source line, with the other-side physical pair collision. Therefore (DM-1) guarantees

\[
\boxed{\{i,j\}\notin E(J).}
\tag{DM-3}
\]

This statement does NOT rule out a J edge involving the OTHER four named source flags on \(\gamma,\eta\), and indeed those edges are the main residual obstruction.

## 2. NEW exact all-h orientation-matrix theorem

Each directed middle diagonal of a named original flag has two binary choices \(o_x,o_y\in\{0,1\}\): which of its unordered pair's x-symbol is the middle edge TAIL, and which y-symbol is the TAIL. There are exactly four distinct actual directed diagonals per flag: (++),(+-),(-+),(--).

For the two disjoint source-middle flags in (DM-1), **typed x-odd-cycle incompatibility** (proven source-first in #753) is exactly

\[
x_1^\gamma=x_2^\eta\ \lor\ x_2^\gamma=x_1^\eta;
\]

such an equality can exist ONLY if \(\alpha=1\). With one shared x symbol, it occurs exactly when that shared symbol is at OPPOSITE inner depths in the two oriented middle physical edges (tail in one, head in the other). If \(\alpha=0\), x-typed odd-cycle incompatibility is categorically impossible. The y statement is identical with \(\beta\).

Thus, for any fixed oriented middle edge of i, among the FOUR oriented diagonals of j, the number of *typed-compatible* pairs of source middle edges is \(4/2/2/1\) according to \((\alpha,\beta)=(0,0),(1,0),(0,1),(1,1)\). The result is invariant under relabeling of the two shared symbols or flipping the pair orientation convention, since that only permutes matrix rows and columns. Consequently the EXACT count among ALL FOUR × FOUR source-oriented middle diagonal pairs is

\[
\boxed{
C_{\mathrm{typed}}^{4\times4}(\alpha,\beta)
=16/8/8/4
\quad\text{for}\quad
(\alpha,\beta)=00/10/01/11.
}
\tag{DM-4}
\]

This is an analytical all-order statement about SOURCE MIDDLE DIAGONAL orientations, NOT a claim that all 16 combinations can appear as real P3s with the same fixed endpoints, and NOT an assertion about original source priority J compatibility.

### NEW sharp 3x3 subfamily orientation bound, using original GQ middle-owner THREE cap

#758 proves each ORIGINAL middle flag contributes at most 3 true proper P3 paths to a fixed ordered endpoint bin. If TWO original middle flags both contribute **exactly THREE** such paths, they each realize a distinct three-element subset of their four possible directed middle-edge orientations. How many source-oriented pairs are guaranteed free from TYPED coordinate conflict, before checking J?

- **00:** all nine pairs are typed-compatible, exactly 9.
- **10 or 01:** full 4x4 typed-compatible matrix has each row and each column of degree exactly 2, for eight compatible pairs total. Removing one row and one column deletes at most 2+2=4, so at least **4** remain. This is sharp: choose deleted row and deleted column NOT adjacent in the typed-compatible matrix.
- **11:** the full 4x4 typed-compatible matrix is a **perfect matching** (exactly one compatible counterpart for every orientation). Removing one row and one column deletes at most two of its four edges, so at least **2** remain. This is sharp: delete a row and a *nonmatched* column.

Therefore

\[
\boxed{
C_{\mathrm{typed,min}}^{3\times3}(\alpha,\beta)
=9/4/4/2
\quad\text{for}\quad
00/10/01/11,
}
\tag{DM-5}
\]

and all four numbers are attained in the pure 4x4 source orientation matrix, independently exhaustively checked over all \(4\cdot4=16\) choices of omitted directions for each of the four overlap cases. This statement is unconditional *only* at the level of typed physical coordinate constraints.

**CRITICAL SCIENTIFIC SCOPE:** A typed-compatible pair may be source-J incompatible because an OUTER owner of one physical path conflicts with a named ORIGINAL source owner of the other. Theorems DM-4/DM-5 do NOT promise actual common survival of a typed-compatible pair without checking original J. Any attempt to divide B by 16/8/4 or to infer B/M<3/4 from DM-4/DM-5 alone is INVALID.

## 3. NEW exact all-h disjoint-middle source-J/typed partition

Write the actual genuine owner triples of the two physical paths as \((i_0,i_1,i_2)\), \((j_0,j_1,j_2)\), with \(i_1=i=(p,\ell)\), \(j_1=j=(q,m)\), and (DM-1). Within either path the THREE owners are pairwise J-independent (coordinate-proper physical source). Between the triples, there are **nine** potential owner-owner comparisons \((i_r,j_t)\), but the *middle–middle* comparison \((i_1,j_1)\) is NEVER a J edge by (DM-3). Thus any source-J incompatibility involves at least ONE of the other **eight** cross-owner comparisons, and can be partitioned deterministically:

1. \(B_{\mathrm{J,\;middleOuter}}\): at least one actual original J conflict \(i_1\)--\(j_0/j_2\) or \(i_0/i_2\)--\(j_1\), including cases where an outer–outer J conflict also exists;
2. \(B_{\mathrm{J,\;outerOuterOnly}}\): no middle–outer J conflict, but at least one actual original J conflict between i_0/i_2 and j_0/j_2;
3. \(B_{\mathrm{noJ,\;typedFirst}}\): no ORIGINAL source J conflict across either path, but a first-coordinate opposite-depth collision of the physical middle oriented edges;
4. \(B_{\mathrm{noJ,\;typedSecondOnly}}\): neither source J nor x-typed conflict, but a second-coordinate opposite-depth collision.

These FOUR disjoint cases exhaust ALL bad ordered physical path pairs in the original middle incidence channel with distinct point and line. Therefore for every dyadic original GQ, every fixed legal original f/g and paired core,

\[
\boxed{
B_{\mathrm{middle\;point,line\;disjoint}}
=B_{\mathrm{J,\;middleOuter}}
+B_{\mathrm{J,\;outerOuterOnly}}
+B_{\mathrm{noJ,\;typedFirst}}
+B_{\mathrm{noJ,\;typedSecondOnly}}.
}
\tag{DM-6}
\]

All weights are EXACT marginal products \(p_\gamma p_\eta\), not joint selection probabilities. J/typed **events** can overlap; to make DM-6 disjoint we deliberately give original source J precedence, then x, then y. The underlying physical incompatibility criterion, determined before this decomposition, is unchanged.

**Immediate all-h typed-obstruction isolation:** For \((\alpha,\beta)=(0,0)\), no x or y inner opposite-depth collision is possible. Therefore

\[
\boxed{
B_{\mathrm{disjointMiddle},00}
=B_{\mathrm{J,\;middleOuter},00}
+B_{\mathrm{J,\;outerOuterOnly},00}.
}
\tag{DM-7}
\]

The truly hard source component is thus constrained to GQ-mediated external owner interactions when both middle label pairs are physically disjoint. Importantly, since #758's finite W34 source-disjoint channel is dominant, DM-7 and DM-6 tell the next all-h referee WHICH source J cross-incidence interactions still require a quantitative bound and which are merely physical typed orientations.

## 4. Independent complete true ORIGINAL W32/W34 falsification

The dedicated source-first program imports the already independently audited genuine original symplectic geometry, global fixed f/g pair labeling, true source J pencil graph and complete physical proper-P3 enumeration from the frozen #758 referee, and then implements a **SEPARATE** source J versus typed classification WITHOUT asking #758's four-incidence ledger to calculate any of its values. Every same-ordered-endpoint pair with genuinely different named middle point AND middle line is classified by:
- independent original middle f/g intersection bits alpha,beta, each checked to be 0/1;
- actual oriented x/y inner physical collision, independently checked against the source-overlap bit and SHARED SYMBOL'S TAIL/HEAD positions;
- explicit source-J inspection across ALL nine actual original owner pairs, independently asserting direct middle-middle J absence;
- the four disjoint exact cause labels of DM-6 plus a fifth compatible class, weighted with exact independent-original-priority Fraction marginals and physical two-cut factor 1/64.

The program recomputes the complete disjoint-middle pair census over **ALL original proper P3** for eight source cases, including W32 FULL lex/reverse/shifted-Z17 and W34 FULL lex/reverse/shifted, even retained CORE, shifted-Z17 retained CORE. There are NO 2,000-path truncations. It also computes the previous #758 full original W32/W34 quadruple-incidence ledger separately, and the new cross-source disjoint channel is required to agree with the **exact earlier rational B channel and ordered bad pair count**. The old program is only a cross-check, not the source of J/x/y cause classification.

Additional strict original witnesses contain all physical vertices of both selected P3s, each path's three actual named original owners, ordered physical endpoints, the exact positive marginal product weight, and either:
- A real **zero both original middle label overlaps** source-J bad pair, necessarily arising from the eight external-owner comparisons; or
- A real **typed-only bad pair** in which no source-J conflict exists, and the two true source middle labels share the necessary physical coordinate symbol.

Independent orientation-matrix tests enumerate all 16 oriented middle source pairs for each overlap signature and all 16 separate 3x3 subfamily omissions, with analytically required sharp tables (DM-4),(DM-5). A 16-test independent suite and dedicated strict Ubuntu-24 GitHub-hosted specialist assert no fake direct source-J middle edge, no impossible 00 typed-only bad, complete exact pair/weight conservation and root scientific non-promotion.

## 5. Acceptance boundaries and next necessary research step

**Proved all-h:** impossibility of direct J edge between different middle point and line, physical typed overlap necessity, 16/8/8/4 full orientation count, sharp 9/4/4/2 three-by-three typed-compatible count, and exact disjoint-middle B source-J/typed four-way partition with zero-overlap purely J channel.

**Not proved:** a sufficiently strong all-h upper on any of these four weighted B cause components, an all-h 75% bound on global B/M for arbitrary correlated original f/g, an infinite correlated counterfamily, a complete accepted HEAVY/LOW/GF5 original Branch A theorem or any new ASET exponent. Full finite source counts and specific observed share of J versus typed risk are not asymptotic theorems.

**Next source-level gate:** use true symplectic GQ unique projection of nonincident point-line and original source J pencil constraints to quantify the **external J middle–outer/outer–outer** terms of DM-6 under physically disjoint source middle pairs. If these are not dominant, attempt a uniform physical typed-overlap count, carefully respecting the possibility of arbitrarily large alphabet a and adversarial star-like pair-injective maps. Any claim that global pair-injection automatically makes physical pair-label overlaps rare requires an explicit constraint on a; in general a can be huge, and every source pair label may share a common symbol. Do not introduce an unproved minimal-alphabet assumption.

Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER; no main merge, issue closure or proof acceptance promotion.
