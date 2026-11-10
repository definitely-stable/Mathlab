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

## 3.1. STRONGER ALL-h theorem: every source J obstruction collapses to TWO physical endpoint tests

The initial DM-6 partition is correct but not sharp enough: the source-middle-to-outer J channel is actually IDENTICALLY ZERO for all coordinate-proper physical P3s with the SAME endpoints, not just in the W32/W34 cases. This has a short, rigorous original-source proof.

Let the two actual proper paths have their four physical vertices written

\[
\gamma=(u,a,b,v),\qquad\eta=(u,c,d,v),\qquad
u=(u_x,u_y),\ v=(v_x,v_y).
\]

Each ORIGINAL physical edge has the unique original point f-inverse of its unordered x pair and unique original line g-inverse of its unordered y pair. The two source owner triples are associated with edges \((u,a),(a,b),(b,v)\) and \((u,c),(c,d),(d,v)\).

**No middle–outer J edges:** The middle x pair of either path contains precisely its two interior x coordinates, both distinct from BOTH its endpoint x coordinates \(u_x,v_x\) by coordinate-properness. The first outer x pair of EITHER path contains \(u_x\); the last outer x pair contains \(v_x\). Therefore the middle original point cannot equal any outer original point. The same argument with the y pairs excludes equality of their original lines. Since ORIGINAL J edges require a shared source point or line, middle-to-outer source J adjacency is impossible.

**No first–last J edges:** The first outer physical x pair contains \(u_x\); the last outer x pair of EITHER proper path excludes \(u_x\). Thus their original points differ; their lines differ by the analogous y argument. This prohibits first-outer versus last-outer J adjacency (in both cross-path directions), independent of GQ order, original f/g correlations, or source J degree.

**Middle–middle source J:** For the disjoint ORIGINAL middle flags considered in (DM-1), there is also no J middle–middle edge because their point and line are both different. Hence the ONLY potentially source-J-adjacent owner comparisons are (first,first) and (last,last) — **TWO**, instead of the original nine or preliminary eight.

Now compare the two actual first physical edges \((u,a)\) and \((u,c)\). Their original first-edge owners share a genuine source point iff their first x pair labels are equal, which is equivalent to \(a_x=c_x\). They share a genuine source line iff \(a_y=c_y\). If \(a=c\), they are the SAME real physical edge and thus have the SAME named source owner; J has no self-edge, so there is NO conflict from this comparison. If \(a\ne c\), either equal typed coordinate gives a true J edge: on a shared original source point the other-side physical y pairs both contain \(u_y\); dually on a shared original line the x pairs both contain \(u_x\). So the first–first J event is EXACTLY

\[
E_{\rm first}
=\mathbf1\bigl[a\ne c\ \wedge\
   (a_x=c_x\vee a_y=c_y)\bigr].
\tag{DM-8}
\]

Identically the last–last owner J event is EXACTLY

\[
E_{\rm last}
=\mathbf1\bigl[b\ne d\ \wedge\
   (b_x=d_x\vee b_y=d_y)\bigr].
\tag{DM-9}
\]

Therefore the new all-h **physical source equality lemma** is

\[
\boxed{
\text{source-J conflict of }\gamma,\eta
\iff E_{\rm first}\vee E_{\rm last}.
}
\tag{DM-10}
\]

The equation is valid whenever the two proper P3s have the same ordered physical endpoints and their true middle point AND line differ. No access to the FULL original J graph is needed to decide the source-J part of their incompatibility once the true physical proper paths and their unique middle-source IDs are known.

## 3.2. STRONGER ALL-h full ORIGINAL compatibility theorem: 16 / 0 / 0 / 2

Combine DM-10 with the exact typed opposite-inner-depth criterion. Let \(\alpha,\beta\in\{0,1\}\) be the middle source label overlap bits of (DM-2).

**Case 00 (neither middle label pair overlaps).** The two paths have disjoint x inner symbols and disjoint y inner symbols. Thus no same-depth or opposite-depth inner typed coordinate equalities can occur. By DM-8/DM-9 there is NO endpoint-source J event either; by DM-3 no middle–middle J, and by properness no other J. Therefore **EVERY such actual pair is FULLY compatible**, and

\[
\boxed{B_{\mathrm{disjointMiddle},\,00}=0.}
\tag{DM-11}
\]

This is stronger than the earlier correct but unhelpful observation that typed conflicts alone vanish. Any proposed true ORIGINAL zero-overlap bad-pair witness is an outright contradiction to this all-h source theorem, not a real GQ counterexample.

**Case 10 or 01 (exactly ONE typed middle label overlap).** There is exactly one shared inner symbol, occurring once in each path. If it appears at OPPOSITE depths, the typed factor has an odd-cycle incompatibility. If it appears at the SAME depth, the two corresponding physical inner vertices agree in that typed coordinate but differ in the OTHER coordinate (the other middle pair labels are disjoint), hence \(E_{\rm first}\) or \(E_{\rm last}\) is a TRUE ORIGINAL J edge by DM-8 or DM-9. Thus **EVERY actual pair of such true original proper P3s is FULLY incompatible**. The classification into source J or typed only depends precisely on the direction of the shared middle typed symbol.

**Case 11 (BOTH middle pair labels share one symbol).** For FULL compatibility, neither x nor y may have opposite-depth shared symbols; they must each occur at SAME depth in the two paths. If these two shared physical symbols occur at DIFFERENT depths from each other (x shared at first, y shared at last, or vice versa), an outer first–first or last–last pair has a same-depth partial typed collision and hence J conflict. Full compatibility is therefore possible ONLY when the shared x and y symbols occur BOTH at the FIRST inner vertex of both paths, giving \(a=c\), or BOTH at the LAST inner vertex of both paths, giving \(b=d\). In these two cases the corresponding outer source flag is IDENTICAL, not J-adjacent, while the other outer source flags differ in BOTH original point and line, so J and typed conflicts both vanish. Thus the exact source condition is

\[
\boxed{
\gamma,\eta\text{ FULLY compatible}
\iff(\alpha=\beta=0)
\ \lor\
(\alpha=\beta=1\ \wedge\ (a=c\ \lor\ b=d)).
}
\tag{DM-12}
\]

Note that \(\alpha=\beta=1\) is essential to the second branch; merely sharing an inner vertex is not claimed to prove compatibility for unrelated middle source types.

As a consequence, among the FOUR directed middle-diagonal orientations of each true source flag, the FULL ORIGINAL **J-plus-typed** compatibility count is

\[
\boxed{
C^{4\times4}_{\mathrm{full\ ORIGINAL}}(00,10,01,11)
=(16,\;0,\;0,\;2).
}
\tag{DM-13}
\]

The first table 16/8/8/4 remains exactly valid for **typed-only** compatibility, but ignoring source J would double-count apparent good orientations. For three-element orientation subfamilies of two source middle flags (the maximal local multiplicity by GQ no-K2,2), the SHARP abstract FULL ORIGINAL minimal compatible counts are now \(9,0,0,0\): in overlap 11 the full compatibility matrix consists of only two disjoint matching edges, both of which can be covered by deleting one row and one column. Again, this abstract extremum does not assert that every 3×3 subset is realized as actual same-endpoint proper paths in a given GQ.

**New exact global source support theorem (valid all-h, no fixed-alphabet-size assumption):**

\[
\boxed{
B_{\mathrm{middlePointLineDisjoint}}
=B_{\mathrm{middlePointLineDisjoint},\,10}
+B_{\mathrm{middlePointLineDisjoint},\,01}
+B_{\mathrm{middlePointLineDisjoint},\,11}.
}
\tag{DM-14}
\]

The disjoint-middle ORIGINAL bad-weight support is empty when BOTH middle source label pairs have disjoint symbols. Every weight is still the true original source marginal-product \(p_\gamma p_\eta\) and can be arbitrarily nonuniform, so the orientation counts do NOT automatically imply a constant-fraction global B bound. In particular, separate global pair-injection alone does NOT force overlap sparsity for arbitrarily large alphabet a: a fixed-label star family can make many pairs intersect.

Finally, the new source referee recomputes **EVERY** real disjoint-middle original same-endpoint path-pair status in all eight finite W32/W34 source cases TWICE: once by original J plus true typed parity, and once by the simple PHYSICAL ONLY formula DM-12. Exact rational total good and bad weights MUST coincide between these independent calculations and also with the ancestor #758 four-channel source ledger. A true zero-overlap J-bad witness is now categorically forbidden; the strict JSON instead exports positive real source witnesses of a single-overlap same-depth outer J conflict and a two-overlap common-inner-corner fully compatible pair.

## 3.3. NEW exact non-pairwise ORIGINAL middle-source GOOD kernel and all-h positive lower bound

The full compatibility condition DM-12 is strong enough to eliminate the entire path-pair source-J graph traversal from the disjoint-middle compatible-mass calculation. This produces a **positive compatible-pair quadratic form** expressed solely through true original middle-flag groups and the four physical corners.

Fix an ordered physical endpoint bin (u,v). For each actual named ORIGINAL middle owner i=(p,l) of the genuine proper P3 paths in this bin, let

\[
\Gamma_i=\{\gamma=(u,a,b,v):\mathrm{midOwner}(\gamma)=i\},\quad
W_i=\sum_{\gamma\in\Gamma_i}p_\gamma.
\]

For each actual physical corner z of that middle owner's rectangle, define the nonnegative source-grouped marginal weights

\[
T_i(z)=\sum_{\gamma\in\Gamma_i:\ a=z}p_\gamma,\qquad
H_i(z)=\sum_{\gamma\in\Gamma_i:\ b=z}p_\gamma.
\tag{DM-15}
\]

These are actual *source-priority-plus-typed-cuts path marginals*, not independent Bernoulli event products. An ORIGINAL flag owns just two opposite physical undirected diagonals, so for each specific middle oriented edge with tail z or head z the relevant P3 with fixed endpoints is unique if it exists. Each T_i(z),H_i(z) has therefore at most ONE term, but the formula remains correct if written as a sum.

For a pair of **distinct ORIGINAL middle flags i=(p,l), j=(q,m)** with both p≠q and l≠m, let (alpha,beta) be their genuine middle label pair overlap bits. By DM-12:

- If alpha=beta=0, EVERY cross-group source path pair is fully compatible, so its *ordered* good mass is EXACTLY \(2W_iW_j\).
- If alpha!=beta, NONE of the cross-group path pairs is fully compatible, so its good mass is EXACTLY 0.
- If alpha=beta=1, the two original physical rectangles share a UNIQUE corner z, the Cartesian product of their two shared physical symbols. A path from i and a path from j are fully compatible iff they both have FIRST internal vertex z or both have LAST internal vertex z. The exact **ordered** source good weight is therefore \(2[T_i(z)T_j(z)+H_i(z)H_j(z)]\).

Summing over unordered distinct middle-owner SOURCE PAIRS gives the exact all-h identity

\[
\boxed{
G_{uv}^{\mathrm{disjointMid}}
=2\!\!\sum_{\substack{i<j;\ p_i\ne p_j,\ l_i\ne l_j\\
\alpha_{ij}=\beta_{ij}=0}}\!\!W_iW_j
+
2\!\!\sum_{\substack{i<j;\ p_i\ne p_j,\ l_i\ne l_j\\
\alpha_{ij}=\beta_{ij}=1}}
\left[T_i(z_{ij})T_j(z_{ij})+
H_i(z_{ij})H_j(z_{ij})\right].
}
\tag{DM-16}
\]

This identity is **exact in all dyadic orders, not a bound**. It depends on the genuine original middle incidence ID and source f/g pair labels, and it does not need to examine any J owner conflict nor each path pair when evaluating the right side. Original source GQ is used in establishing real paired source edges and uniqueness, not replaced by a synthetic graph.

The corresponding cross-group *total ordered pair weight* is

\[
M_{uv}^{\mathrm{disjointMid}}
=2\sum_{i<j,\ p_i\ne p_j,\ l_i\ne l_j}W_iW_j.
\]

Hence the full disjoint-middle incompatible weight is **exactly**

\[
\boxed{
B_{uv}^{\mathrm{disjointMid}}
=M_{uv}^{\mathrm{disjointMid}}-
G_{uv}^{\mathrm{disjointMid}}.
}
\tag{DM-17}
\]

The proof is term-by-term disjoint by the true middle owner pair and by DM-12. Every positive source group weight is a real original selector marginal. No independent-source/product-of-path-probabilities assumption is introduced.

**NEW rigorous all-h compatible-mass lower bound.** All diagonal ordered path-pairs \((\gamma,\gamma)\) are self-compatible (previous #757), while all the different-middle-owner pairs counted in DM-16 are also compatible, and the two collections are **disjoint**. Thus for every ordered physical endpoint family

\[
\boxed{
G_{uv}\ge D_{uv}+G_{uv}^{\mathrm{disjointMid}},
\qquad
D_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma^2.
}
\tag{DM-18}
\]

In particular, together with #755's original weighted Motzkin–Straus lower bound, one may safely take

\[
\boxed{
G_{uv}\ge
\max\{M_{uv}/\omega_{uv},\ D_{uv}+G_{uv}^{\mathrm{disjointMid}}\}.
}
\tag{DM-19}
\]

This uses MAXIMUM, not an INVALID additive sum of two overlapping lower-bound contributions. Summing over all physical endpoint bins yields a genuinely new universally valid, explicitly source-computable lower bound on total G; it is not automatically strong enough for global G/M>1/4 under every adversarial fixed f/g.

**Independent falsification:** The updated source referee evaluates DM-16 using only **source-middle grouped marginal weights and the original physical shared-corner test**, without iterating over path pairs or asking the original J graph. It separately scans EVERY true original same-endpoint path pair, computing source J/typed causes; the two methods' entire exact rational G_disjoint, B_disjoint and alpha=beta=00/11 good subweights must match for all eight COMPLETE W32/W34 cores. The same module independently checks \(D+G_{\rm disjoint}\le G_{\rm full}\) against the parent full-original source exact compatible-mass ledger. The 26-test suite includes separate exact checks of the nonpairwise kernel, diagonal separation, and W32 physical-only full pair equivalence.

## 3.4. FINAL stronger all-h identity — ENTIRE ORIGINAL M, G, B from true middle-source groups

The preceding inequality DM-18 is in fact an **equality**, for a source-geometric reason not needing any extra assumption. Let two **distinct** genuine coordinate-proper physical P3s share ordered endpoints (u,v). If their ORIGINAL middle incidence owners are the SAME named flag, the paths have different directed middle physical diagonals (a fixed directed middle edge uniquely determines the path), and those diagonals disagree in at least one typed orientation, so the two paths are incompatible (#758). If middle original flags are distinct but share their genuine ORIGINAL point p, their middle **x-coordinate pair labels are identical**. The shared two x-symbols cannot occupy opposite inner depths without a typed collision, and if their x-directions agree, the corresponding distinct first-inner (or last-inner) physical vertices have equal x-symbol but differing y-symbol, producing an ORIGINAL J conflict between the two first (or last) outer source owners. Dually, two different middle flags sharing an ORIGINAL line necessarily produce the same dichotomy in y. Therefore **any two different fully compatible physical P3s with same ordered endpoints must have middle owners with BOTH different ORIGINAL point AND different ORIGINAL line**.

In those two-source-disjoint middle cases, the EXACT full compatibility criterion was already established in DM-12, and the independently computed group kernel DM-16 counts all of them. Diagonal path pairs are individually compatible. This yields the NEW exact all-h theorem

\[
\boxed{G_{uv}=D_{uv}+G_{uv}^{\mathrm{disjointMid}}.}
\tag{DM-20}
\]

Moreover, if \(W_{uv,i}=\sum_{\gamma\in\Gamma_{uv}(i)}p_\gamma\) are exact positive source marginal sums for each true original middle flag i, then by elementary expansion

\[
\boxed{M_{uv}=\left(\sum_iW_{uv,i}\right)^2,\qquad
B_{uv}=M_{uv}-D_{uv}-G_{uv}^{\mathrm{disjointMid}}.}
\tag{DM-21}
\]

These are **exact**, not upper or lower approximations, for every dyadic \(W(3,s)\), every fixed arbitrary correlation of separately globally pair-injective f and g, every original named Z and retained paired source CORE, with proper original path owner conditions as above. The source middle kernel computes the ENTIRE weighted-compatible and incompatible physical path-pair products **without inspecting source-J conflict edges between individual path pairs**; the only remaining exponential/large-order challenge is to derive a universally strong lower bound on these exact quadratic forms under all allowed GQ incidence and f/g correlations.

The formula also yields exact nonnegative conservation:
\(B=B_{\rm sharedOriginalMiddlePointOrLine}+B_{\rm disjointMiddle}\).
All distinct-path pairs whose middle source points or lines coincide contribute to the first term, whereas disjoint-middle B is the exact complement of DM-16 in its group-pair total. The exact source diagonal accounts for all repeated-path pairs.

**Final-head GitHub-hosted proof acceptance for implementation:** [specialist #42783186358](https://github.com/definitely-stable/Mathlab/actions/runs/42783186358) **SUCCESS, 28/28 tests**, strict 8-case source JSON certificate, comparing the independently grouped all-order source \(M,G,B\) against all 8 previously accepted complete physical pairwise original-collision tensors as exact Fractions. [INDEX #42783186276](https://github.com/definitely-stable/Mathlab/actions/runs/42783186276) **SUCCESS** and [full Research #42783186316](https://github.com/definitely-stable/Mathlab/actions/runs/42783186316) **SUCCESS** on the same HEAD \`0359f97ef62301418745fa179b922dae18fb0b3a\`. This documentation enhancement will create a new HEAD and therefore the CI of that new HEAD must still be independently verified.

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

Independent orientation-matrix tests enumerate all 16 oriented middle source pairs for each overlap signature and all 16 separate 3x3 subfamily omissions, with analytically required sharp tables (DM-4),(DM-5). A 28-test independent suite and dedicated strict Ubuntu-24 GitHub-hosted specialist assert no fake direct source-J middle edge, no impossible 00 typed-only bad, complete exact pair/weight conservation and root scientific non-promotion.

## 5. Acceptance boundaries and next necessary research step

**Proved all-h:** exact SOURCE-middle compressed positive GOOD kernel DM-16, independent full disjoint-middle B complement DM-17 and new compatible positive bound DM-18/DM-19; no direct middle–middle J edge for distinct original middle point and line; source J middle-to-outer and first-to-last comparisons impossible for any proper same-endpoint paths; exact physical first–first/last–last partial-coordinate J criterion; typed-only 16/8/8/4 and sharp 9/4/4/2 3×3 counts; **FULL ORIGINAL J+typed 16/0/0/2 orientation compatibility** and physical-only criterion DM-12; **NO bad pairs with two disjoint middle physical label pairs**; exact original disjoint-middle bad-source/typed risk conservation. No universal global risk ratio is claimed.

**Not proved:** a sufficiently strong all-h upper on any of these four weighted B cause components, an all-h 75% bound on global B/M for arbitrary correlated original f/g, an infinite correlated counterfamily, a complete accepted HEAVY/LOW/GF5 original Branch A theorem or any new ASET exponent. Full finite source counts and specific observed share of J versus typed risk are not asymptotic theorems.

**Next source-level gate:** exploit the new exact physical-only condition DM-12 to bound the source-weighted number of **SAME-ENDPOINT middle pair label overlaps** under actual original GQ incidence/projection and owner-priority marginals, or produce an infinite legal fixed-label correlated counterfamily. The middle–outer J term is identically zero, the outer–outer J term reduces exactly to first/last same-depth physical corner collisions, and all disjoint-middle overlap 00 bad mass vanishes. Do NOT assert pair-label overlaps are sparse from global injection if alphabet a is unrestricted or may grow adversarially. Any claim that global pair-injection automatically makes physical pair-label overlaps rare requires an explicit constraint on a; in general a can be huge, and every source pair label may share a common symbol. Do not introduce an unproved minimal-alphabet assumption.

Root issue #230 remains OPEN_WITH_FORMAL_BLOCKER; no main merge, issue closure or proof acceptance promotion.
