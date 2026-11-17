# HYP-105 #230 — AA4-LOW-FORMAL: universal reversible ORIGINAL source witnesses and weighted four-blocker lemma

**Status: a newly derived self-contained ALL-ORDER LOCAL mathematical theorem, not global root Branch A acceptance.** Strict Draft child of [#769](https://github.com/definitely-stable/Mathlab/pull/769) frozen at 7ea3d3438be2035c6659a09fa0f5386a483ba346. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. No modifications to parents or main, merges or ASET exponent claims. Independent original W(3,2)/W(3,4) finite oracles help falsify the statement but do not establish universal validity.

## 1. Source model and a useful strict generalization

Let I be a finite actual named point–line incidence relation, with point type P and line type L. Take separately **globally pair-injective** maps f:P→binom(X,2), g:L→binom(Y,2), arbitrary and mutually correlated. For arbitrary deleted named ORIGINAL IDs Z, define the FULL allowed source A=I\Z and an arbitrary paired CORE C⊆A.

Every ORIGINAL retained flag (u,ell_u) owns exactly the TWO opposite physical diagonals of its rectangle f(u)×g(ell_u). Global pair injection guarantees that every physical undirected edge has exactly one named ORIGINAL flag owner. Let H be the adjacency matrix of this real physical graph on all X×Y vertices, including isolates; d(v) its degree, D the diagonal degree matrix, Δ its maximum degree, and t4=tr(H^4).

For nonincident q∈P,r∈L suppose a **partial single-valued** original projection π(q,r)=(p,ell) is defined whenever the required named anchors (q,ell),(p,ell),(p,r) all belong to A. The projection must satisfy p≠q. A genuine symplectic GQ W(3,s), s=2^h, has a unique original projection for every nonincident q,r; an arbitrary bipartite incidence system can use any fixed **single** valid projection where one exists. This allows the local theorem below to be proved without assuming a GQ spectrum or even GQ incidence uniqueness beyond the chosen projection.

For a point p and physical second-coordinate symbol y, define R_A(p,y) as the number of ORIGINAL flags (p,r) in A whose actual line factor g(r) contains y; define R_C analogously. Write K_AC(p,u)=sum_y R_A(p,y) R_C(u,y). Let c_x(p) be the number of distinct ORIGINAL points q≠p sharing an original line with p and whose f(q) contains x.

The **total** point-coordinate book is

\[
B_x=\sum_{\substack{u:\,C(u)\ne\varnothing\\(x,k)\in\mathrm{oriented}(f(u))}}
\sum_{p:\,k\in f(p)}c_x(p)K_{AC}(p,u).
\tag{W-BOOK-X}
\]

The notation B_x represents the sum over ALL physical symbols x, not a pointwise book for one symbol. The line-side B_y is defined independently by exchanging P↔L, f↔g, point/line collinearity and the physical x/y coordinates. B_x=B_y is **not** assumed.

## 2. Literal ORIGINAL source-book expansion and inverse

Expanding B_x counts all *distinct literal named source witness keys*

\[
w=(u,\ell_u,x,k,p,q,r,y)
\tag{W-KEY-X}
\]

such that (u,ell_u)∈C, oriented f(u)=(x,k), k∈f(p), q≠p collinear with p in the FULL ORIGINAL incidence geometry, x∈f(q), (p,r)∈A, and y∈g(r)∩g(ell_u). Each element of the product defining c_x and the product defining K_AC supplies exactly one such key; conversely every key supplies one product term. **This is a literal equality of integer multiplicities**, not an inequality.

Let T_x,1 be the set of ordered physical triples t=(v0,v1,v3) satisfying: v0—v1 is one actual physical CORE edge; the endpoint first factor pair {v0.x,v3.x} decodes to the unique q=f^{-1}(...), the second factor pair {v0.y,v3.y} to the unique r=g^{-1}(...); the named ORIGINAL projection π(q,r)=(p,ell) is defined and its three anchors lie in A; and the FIRST interior x-coordinate v1.x belongs to f(p).

Deliberately, T_x,1 does **not** require any middle 2walk, physical coordinate-properness, endpoint-goodness, or projected source anchors in C. It therefore overcounts the paths whose first x coordinate is blocked, which is safe for an upper bound.

Every triple t has exactly one ORIGINAL first edge owner (u,ell_u)∈C. Set

\[
\Psi_x(t)=(u,\ell_u,v_0.x,v_1.x,p,q,r,v_0.y).
\]

The projection has the ORIGINAL anchor flags (q,ell),(p,ell),(p,r)∈A, so q is collinear with p and (p,r) is a FULL allowed original flag. The physical first edge gives oriented f(u)=(v0.x,v1.x) and v0.y∈g(ell_u); the endpoint r has v0.y∈g(r). Therefore Ψ_x(t) is one of the **actual** W-KEY-X witnesses counted by B_x.

The crucial explicit LEFT INVERSE reconstructs the whole physical triple from its source key:

\[
v_0=(x,y),\quad
v_1=(k,\operatorname{other}(g(\ell_u),y)),\quad
v_3=(\operatorname{other}(f(q),x),\operatorname{other}(g(r),y)).
\tag{W-INVERSE-X}
\]

Because every physical factor label is a two-element set of distinct symbols, the other symbol is unique. Hence Ψ_x is injective, not merely existence-preserving, and

\[
\boxed{|T_{x,1}|\le B_x.}\tag{W-1}
\]

The LINE dual has literal witness key (ell_u,u,y,k,ell,r,q,x), with retained original (u,ell_u)∈C, oriented g(ell_u)=(y,k), k∈g(ell), r an ORIGINAL collinear line of ell with y∈g(r), (q,ell)∈A, and x∈f(q)∩f(u). Its explicit left inverse is

\[
v_0=(x,y),\quad
v_1=(\operatorname{other}(f(u),x),k),\quad
v_3=(\operatorname{other}(f(q),x),\operatorname{other}(g(r),y)).
\tag{W-INVERSE-Y}
\]

Thus independently |T_y,1|≤B_y without imposing artificial left/right symmetries.

## 3. NEW full exact weighted source-path certificate

For any t=(v0,v1,v3) in T_x,1, let

\[
w_2(t)=(H^2)(v_1,v_3)
\]

be the **actual** number of possible middle physical CORE two-walk completions v1→v2→v3. Write I_x,1 for the number of real coordinate-proper, endpoint-good, Z-avoiding ORIGINAL-C physical directed 3paths whose FIRST interior x coordinate is blocked. Every such path maps to a triple in T_x,1, and is one of its w2(t) completions. Therefore the direct, nonmoment source charge is

\[
\boxed{I_{x,1}\le W_{x,1}:=\sum_{t\in T_{x,1}}w_2(t).}
\tag{W-2}
\]

W is the exact number of **unfiltered completions** and need not equal I. Cauchy on the actual finite triples gives

\[
W_{x,1}^{\,2}\le |T_{x,1}|\Phi_{x,1},\qquad
\Phi_{x,1}=\sum_{t\in T_{x,1}}(H^2(v_1,v_3))^2.
\tag{W-3}
\]

For fixed ordered (v1,v3), at most d(v1) distinct preceding vertices v0 give a legal first CORE edge. Hence

\[
\begin{aligned}
\Phi_{x,1}
&\le \sum_{v_1,v_3} d(v_1)\,(H^2(v_1,v_3))^2\\
&=\sum_{v_1} d(v_1)\,(H^4)(v_1,v_1)\\
&=\boxed{\mathrm{tr}(D H^4)}
\le \Delta\,\mathrm{tr}(H^4).
\end{aligned}\tag{W-4}
\]

The middle identity follows exactly from symmetric real physical H and matrix multiplication, not an asymptotic estimate, GQ spectral assumption, or sampled empirical identity. Combining with W-1:

\[
\boxed{
I_{x,1}^{\,2}\le W_{x,1}^{\,2}
\le |T_{x,1}|\Phi_{x,1}
\le B_x\,\mathrm{tr}(D H^4)
\le B_x\Delta\,\mathrm{tr}(H^4).
}\tag{W-5}
\]

The new degree-weighted fourth spectral moment tr(DH4) is always ≤Δtr(H4), potentially strictly so for irregular physical cores. This is a **real all-order improvement of the local blocker inequality**, not automatically an improvement of the universal asymptotic root exponent. The exact earlier stages W and Phi can be substantially smaller still.

Directed path reversal preserves the unordered decoded endpoint q,r, projection π(q,r), and allowed original anchor IDs. It exchanges FIRST/LAST interiors:

\[
I_{x,2}=I_{x,1},\qquad I_{y,2}=I_{y,1}.
\tag{W-6}
\]

Apply the separately proved line-side book inverse. For all four actual physically coordinate-proper blocker classes, universally

\[
\boxed{
I_{x,j}^{\,2}\le B_x\,\mathrm{tr}(D H^4),\qquad
I_{y,j}^{\,2}\le B_y\,\mathrm{tr}(D H^4),
\quad j=1,2.
}\tag{W-7}
\]

These classes may overlap. Their union is at most 2sqrt(B_x tr(DH4)) + 2sqrt(B_y tr(DH4)); no invalid disjointness is introduced. W-7 *strictly subsumes* the point/line mixed-book BLOCK-3 upper bound in the previously published internal draft #737.

## 4. Independent FULL A / smaller paired C equality

Both literal book expansions are independently checked against actual source multiplicity contractions:

\[
B_x=\sum_{u,(x,k)\in f(u)}\sum_{p:k\in f(p)}
 c_x(p)\sum_yR_A(p,y)R_C(u,y),
\]

with the exact line dual separately recomputed. An additional independent source-to-physical contraction is

\[
\Theta_{AC}
=\sum_{u,(x,k)}\sum_{p:k\in f(p)}K_{AC}(p,u)
=\sum_{v\in X\times Y}d_A(v)d_C(v)
\le 4|A|\Delta.
\tag{W-8}
\]

Here d_A uses ALL ORIGINAL flags of A, d_C uses only true paired core C. The projection anchors may lie outside C and are never silently replaced by an imaginary core flag. The exact equality is checked from the independently built physical adjacency both for point and for line source books. No HEAVY/LOW partition, root theorem status, probabilistic independence or graph eigenvalue is needed for W-1 to W-8.

## 5. What is proved, what remains open

**PROVED by the explicit all-finite-order mathematical argument in sections 1–4:** the reversible injection from real ordered first-blocker physical triples into literal FULL/CORE original source book terms; exact stagewise weighted charge; tr(DH4) tightening; four blocker positions by reversal and independently typed dual; validity for any finite bipartite typed source with a single-valued compatible projection, in particular all original W(3,2^h) with actual GQ projection.

**NOT proved by this slice:** the all-order original SRG cap e_J≤5s4/2, original heavy source selection/no-clone D6 injection, global LOW moment and Jensen transfer, coordinate-improper and endpoint budgets, actual ORIGINAL P3→BBo two-to-one six-ID inverse, or the complete root HYP-105 Branch A (or ASET) theorem. Those are separate dependencies of the candidate #743/#769 proof. Green CI or finite W32/W34 examples do not promote root issue #230 to PROVED_A.

The improvement is **instance-sensitive**. Without new all-h degree moment or physical weight estimates there is NO justified replacement of the parent asymptotic exponent or threshold s0.

## 6. Independent concrete scientific falsification

Artifacts: research/hyp105_original_low_formal_weighted_witness.py, research/test_hyp105_original_low_formal_weighted_witness.py, and .github/workflows/hyp105-aa4-low-formal-weighted-witness.yml. The standalone code imports only the trusted genuine W(3,2)/W(3,4) incidence constructor; it imports no preceding source-blocker, SRG, LOW, root-bridge or theorem evaluator.

Five actual true symplectic source cases include complete independently pair-injected lex/reverse/shift f/g, Z=empty and Z nonempty, A≠C, 45/425 true original flags, two genuine opposite diagonals per retained source flag, true q--ell--p--r GQ anchors for every nonincident endpoint, and exact independently recomputed point/line source collinearity. An additional THREE NON-GQ abstract bipartite typed incidence cases exercise a partial deterministic single-valued projection, demonstrating that the lemma does not depend on hidden GQ spectral assumptions.

For every case the referee (a) explicitly enumerates every *literal* book source key separately for x/y; (b) independently recomputes Bx/By through R_A/R_C and c_x/c_y multiplicities and requires exact integer equality; (c) constructs every first-edge physical triple, checks membership in the **actual** source book and exact inverse reconstruction; (d) calculates exact W, Phi, tr(DH4), tr(H4), Δ and verifies each link of W-5; (e) independently enumerates every actual coordinate-proper physical P3 and its four genuine original blockers and exact reversal; (f) recomputes the FULL/CORE Theta physically and sourcewise; and (g) includes fail-closed negative inputs: noninjective f/g, malformed pairs, duplicate original IDs, invalid/empty paired source, and false root/ASET status.

If any finite oracle fails, STOP the alleged local proof interface and identify its FIRST invalid source mapping. Do not mask it with a numeric upper estimate. The separate next mathematical acceptance gate remains the global source-priority/Jensen fourth/sixth-moment interpolation and complete quantified HEAVY/LOW proof DAG, not merging parent branches merely because CI passes.
