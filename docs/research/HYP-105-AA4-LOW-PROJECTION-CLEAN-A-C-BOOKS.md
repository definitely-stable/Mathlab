# HYP-105 / issue #230 — AA4-LOW-AC-CLEAN: independent GQ endpoint audit and projection-clean mixed FULL-A / CORE-C books

**Scientific state:** local all-order theorem and a sharper, instance-adaptive original-source blocker certificate; the complete root theorem remains **OPEN_WITH_FORMAL_BLOCKER**. This Draft is strictly stacked on frozen [PR #779](https://github.com/definitely-stable/Mathlab/pull/779), parent HEAD c3c1e3287b8aa307e083a29b219f702602c90be3. No parent, sibling or main changes or merges, no automatic root issue closure, and no new GF(5)/ASET exponent.

Prior [#737](https://github.com/definitely-stable/Mathlab/pull/737) proved the historical full/core books and Cauchy bound, [#751](https://github.com/definitely-stable/Mathlab/pull/751) connected real original paths to the GQ projection and six-ID topology, and [#770](https://github.com/definitely-stable/Mathlab/pull/770) supplied an explicit source-witness inverse and improved the degree-weighted fourth trace. These are **not** claimed as discoveries in this slice. The new contribution is a fully explicit, strictly stronger projection-/endpoint-clean filtration of both historical source books, combined with an independent all-order four-blocker and GQ three-role projection review, including genuine W(3,2)/W(3,4) adversarial source falsifiers.

## 1. Quantifiers: TRUE ORIGINAL source and two different incidence sets

Fix any dyadic s=2^h with h≥1, the genuine symplectic generalized quadrangle W(3,s), original point and line sets P,L of size V=(s+1)(s²+1), and exactly N=(s+1)²(s²+1) named original incidence flags I={(p,ell):p lies on ell}. Fix arbitrary separately **globally** pair-injective complete maps f:P→binom([a],2), g:L→binom([a],2), where a is the minimal physical pair alphabet. Their correlation is unrestricted; NO probability is taken over f/g.

Let Z be an arbitrary deleted set of original incidence IDs, A=I minus Z the **FULL allowed original source**, and C a subset of A the **paired physical CORE**. The root issue's Branch A only needs Z empty, but A does **not** generally equal C even then. Every original source flag i=(u,ell_u)∈C owns exactly TWO opposite, physically vertex-disjoint, genuine edges of its f(u)×g(ell_u) rectangle. Each physical edge has a UNIQUE original source ID owner, since the physical unordered differences in its x and y coordinates decode through the globally pair-injective f and g. The real uncut physical CORE graph H_C has exactly 2|C| undirected edges on a² physical vertices (isolates included).

Let D_C be its genuine vertex-degree diagonal and Δ_C its actual maximum degree. Source projected anchor flags can be in A outside C; no imaginary source/core owners are inserted.

## 2. All-order TRUE GQ projection and an exact three-role census

For any original point q **not incident** with original line r, the genuine GQ axiom guarantees EXACTLY one point p on r collinear with q and exactly one line ell through q,p. This yields a unique original projection

\[
\pi(q,r)=(p,\ell),\qquad
(q,\ell),(p,\ell),(p,r)\in I.
\tag{AC-1}
\]

For source deletions, the projection is allowed iff all THREE named original anchors belong to FULL A, not necessarily C.

**All-order role lemma.** For any named original incidence flag i, the number of nonincident original (q,r) endpoint pairs whose three-anchor GQ projection uses i in a specified one of the three roles q-ell, p-ell or p-r is exactly s². Proof:

- If i=(q,ell) is first, select one of s other points p on ell and then one of s lines r through p other than ell.
- If i=(p,ell) is middle, select one of s other points q on ell and one of s other lines r through p other than ell.
- If i=(p,r) is last, select one of s other lines ell through p and one of s other points q on ell.

Every choice has a unique reverse interpretation by the GQ axiom; no two configurations are identified. Therefore, for any deleted named IDs Z,

\[
\boxed{
|\{(q,r):\text{some true projection anchor lies in }Z\}|
\le 3s^2|Z|.
}
\tag{AC-2}
\]

For each q and r, their two genuine physical pair labels produce exactly four ordered physical endpoint corners, so the physical deletion charge is at most 12s²|Z|. It vanishes **identically** for Z empty. The source role appearances may overlap in the deleted union: a union bound, not three-way disjointness, is used.

## 3. Historical original source books overcount ineligible endpoint configurations

For point p and physical second-coordinate symbol y define R_A(p,y) as the number of original FULL allowed flags (p,r)∈A with y∈g(r), and R_C(u,y) similarly using C. Define K_AC(p,u)=Σ_y R_A(p,y)R_C(u,y). Let c_x(p) count distinct original collinear q≠p with x∈f(q). The historical mixed point book is the literal count of keys

\[
w_x=(i,x,k,p,q,r,y),
\]

where i=(u,ell_u)∈C; f(u) is the oriented pair (x,k); k∈f(p); q≠p is original-collinear with p; x∈f(q); (p,r)∈A; and y∈g(r)∩g(ell_u). It is exactly

\[
B_x=\sum_{u:C(u)\ne\varnothing}\sum_{(x,k)\in\vec f(u)}
 \sum_{p:k\in f(p)}c_x(p)K_{AC}(p,u).
\tag{AC-3}
\]

The line-dual book B_y uses true ORIGINAL line collinearity, an oriented g(ell_u)=(y,k), a projected ell with k∈g(ell), a line r≠ell collinear with ell and y∈g(r), an allowed original (q,ell)∈A and x∈f(q)∩f(u). **B_x and B_y need not be equal** for correlated f/g.

The historical books deliberately include source keys which could never be produced by a genuine coordinate-proper, endpoint-GQ-good physical CORE three-path: a proposed endpoint (q,r) can be incident; one or more of its actual GQ anchors can have been deleted; or the projected endpoint first/second physical labels can collide. Thus B_x and B_y are valid but often severely loose upper bounds.

## 4. NEW literal projection-clean mixed books Bh_x and Bh_y

Declare a historical source key **clean** if and only if:

1. Its original endpoint factors q,r are nonincident and their unique true full GQ projection is **exactly** the proposed original p,ell. Equivalently, on the point side the original line r through p is not the unique line through p and q.
2. All THREE named source anchors (q,ell),(p,ell),(p,r) belong to FULL allowed A.
3. Both projected endpoint factor pairs are genuinely disjoint,

\[
\boxed{f(q)\cap f(p)=\varnothing,\qquad
g(r)\cap g(\ell)=\varnothing.}
\tag{AC-4}
\]

Define **Bh_x** and **Bh_y** as the distinct literal original-source x- and line-dual y-key counts surviving these checks. They require no random labels, no surrogate incidence, no independent path events, and **no** assertion that projected anchors lie inside C.

The filtration gives an all-order exact first-failing-key partition: historical source keys are either clean; fail a valid original projection/nonincidence; fail FULL A three-anchor eligibility; or fail endpoint pair disjointness. Tests occur in that order, so multiply-invalid keys are NOT counted multiple times. Necessarily,

\[
\boxed{0\le Bh_x\le B_x,\qquad0\le Bh_y\le B_y.}
\tag{AC-5}
\]

This is a strict local refinement, not a claim of an improved uniform power of s or universal mixed-book coefficient.

## 5. Explicit independent physical triple → clean source witness, both ORIGINAL types

Fix an ordered triple t=(v0,v1,v3) with v0v1 a **REAL physical CORE edge**. Its endpoint unordered first-symbol pair {v0.x,v3.x} decodes through f to original q; its second-symbol pair {v0.y,v3.y} decodes through g to original r. Demand that (q,r) is offincidence, has the genuine FULL original projection p,ell of AC-1, all three projected anchors lie in A, and AC-4 holds. Do **not** yet demand any physical two-walk v1→v2→v3. This deliberately produces an overcover of actual admissible three-paths.

For the **FIRST interior x blocker**, require v1.x∈f(p). Since v0v1 has exactly one original owner i=(u,ell_u)∈C, set x=v0.x, k=v1.x, y=v0.y. The physical triple maps to the actual literal clean key

\[
\boxed{\Psi_x(t)=(i,x,k,p,q,r,y).}
\tag{AC-6}
\]

Its explicit left inverse recovers all three real physical corners:

\[
v0=(x,y),\quad
v1=(k,\operatorname{other}(g(\ell_u),y)),\quad
v3=(\operatorname{other}(f(q),x),\operatorname{other}(g(r),y)).
\tag{AC-7}
\]

Every other operation returns exactly one symbol of a genuine two-element original physical label. Therefore two distinct physical triples CANNOT have the same clean key; in particular, if Tx1 denotes the actual first-x-blocker triple family,

\[
\boxed{|Tx1|\le Bh_x\le B_x.}
\tag{AC-8}
\]

The independent genuine **LINE dual**, without asserting Bx=By, maps a first y-blocker triple to key (i,y,k,ell,r,q,x), where g(ell_u) has orientation (y,k) with k=v1.y, the true projected ell contains k and x∈f(q)∩f(u). Its explicit left inverse is

\[
v0=(x,y),\quad
v1=(\operatorname{other}(f(u),x),k),\quad
v3=(\operatorname{other}(f(q),x),\operatorname{other}(g(r),y)).
\tag{AC-9}
\]

It similarly proves |Ty1|≤Bh_y. These are literal inverse maps using the ORIGINAL source owners, not mere equality of two independently computed counts.

## 6. Exact weighted two-walk charge and all FOUR blockers

Let H=H_C be the actual symmetric physical adjacency of the CORE, including both original diagonals of every C source owner. For each first-blocker physical triple t=(v0,v1,v3) put the ACTUAL integer a2(t)=H²(v1,v3), the number of physical middle-vertex completions v1→v2→v3. Define Wx=Σ_{t∈Tx1}a2(t), Phix=Σ_{t∈Tx1}a2(t)², and analogously Wy, Phiy.

Every genuine physical **coordinate-proper**, FULL-A-allowed, endpoint-clean ORIGINAL three-path with first internal x blocked is among these completions, so

\[
I_{x,1}\le Wx,\qquad Wx^2\le |Tx1|\,Phix.
\tag{AC-10}
\]

For fixed ordered physical (v1,v3), the number of distinct first physical neighbors v0 is at most d_C(v1). Symmetry of the REAL adjacency H gives

\[
\begin{aligned}
Phix
 &\le\sum_{v1,v3}d_C(v1)\big(H^2(v1,v3)\big)^2\\
 &=\operatorname{tr}(D_CH^4)
 \le\Delta_C\operatorname{tr}(H^4).
\end{aligned}
\tag{AC-11}
\]

Combining AC-8 to AC-11 and the TRUE original line dual,

\[
\boxed{
I_{x,1}^2\le Bh_x\,\operatorname{tr}(D_CH^4)
\le B_x\,\Delta_C\operatorname{tr}(H^4),
}
\]

\[
\boxed{
I_{y,1}^2\le Bh_y\,\operatorname{tr}(D_CH^4)
\le B_y\,\Delta_C\operatorname{tr}(H^4).
}
\tag{AC-12}
\]

Path reversal (v0,v1,v2,v3)↦(v3,v2,v1,v0) preserves the decoded ORIGINAL endpoint factors q,r, the unique full GQ projection and FULL A allowed anchors, so it exchanges the FIRST/LAST x-blockers exactly and also FIRST/LAST y-blockers. Therefore Ix2=Ix1 and Iy2=Iy1. These four categories may overlap. The correct **union** charge, without false disjointness, is

\[
\boxed{
I_{\mathrm{blocker\ union}}
\le2\sqrt{Bh_x\,\operatorname{tr}(D_CH^4)}
 +2\sqrt{Bh_y\,\operatorname{tr}(D_CH^4)}.
}
\tag{AC-13}
\]

The proof uses only nonnegative integer weights, genuine projection uniqueness, two-element pair labels and ordinary Cauchy. It does NOT need statistical independence or the numerical threshold of the full root theorem.

## 7. Interface with prior #779: correctly retain universal LOW budget

The previous genuine FULL-A/CORE-C mixed source bounds from #737 remain available independently:

\[
B_x^2\le16(s+1)(K+1)|A|\Delta_C G_f,\qquad
B_y^2\le16(s+1)(K+1)|A|\Delta_C G_g,
\tag{AC-14}
\]

where G_f,G_g are the true ORIGINAL point- and line-SRG Gram energies. This requires an actual ORIGINAL source-J clique cap of K+1 on every retained CORE original pencil, not arbitrary synthetic source cliques. For the fixed Branch A LOW K=10 and actual Δ_C≤Ts the inherited uniform bound is Bx,By≤B0 s^(23/4), B0=ceil_sqrt[360(K+1)T]. By AC-5 the SAME uniform bound is valid for Bh_x,Bh_y.

**No new universal B0 or root h0 value is claimed merely because finite books shrink.** Parent #779 already provides the improved selected EXPECTED sixth/fourth moments L6=24+ceil(36 nu_H T²) and L4=q2²ceil_sqrt(ceil(nu_H L6))+19T, with fixed H=32, K=10, R=33281 and ONE common T. The cleaned books strictly improve the instance-specific remaining mixed blocker charge at those SAME universal coefficients; they cannot by themselves close the missing original six-ID P3→BBo and full-root theorem.

## 8. Independent real symplectic falsifiers

The new standalone research program imports ONLY the genuine symplectic W(3,2)/W(3,4) original incidence fixture, not any previous GQ projection, endpoint, source-book, A/C blocker, LOW/root or sixset evaluator.

Seven truly original configurations under complete, correlated, separately globally injected lex/reverse/shift maps exercise:
- FULL A=C and genuine smaller paired CORE C within A, including source deletions Z=empty and sparse Z; no rebased/modified ancestor source data.
- ALL original q outside r pairs, unique true projection and exactly s² appearances of EACH of the N flags in EACH of its THREE original roles.
- Genuine point/line collinearity and FULL/CORE source-first historical book enumerations Bx/By, independent filtered Bh_x/Bh_y and exact first-failing-key loss counts.
- Independently PHYSICAL-first enumerated original endpoint-good first-blocker triples and their explicitly inverse-decoded clean source keys on BOTH typed sides. Actual anchors in A outside C are kept; a diagnostic that forbids them is an invalid attempted proof shortcut.
- Separately enumerated ALL actual physical coordinate-proper P3, exact four internal blocker counts and union, reversal equalities, true CORE degree-weighted fourth trace, and every integer step of AC-10/AC-12.
- Negative test controls for invalid symplectic orders, unknown map schemes, original IDs outside the true I, malformed CORE, nonsubset relationships and false ROOT promotion.

Representative fully enumerated source-first results (old source book → NEW clean source book) on W(3,4): lex FULL CORE Bx 49181→17122, By 49447→17491; reverse two-thirds CORE Bx 32515→11477, By 32729→11781. These are exact integer *instance* results, not numerical extrapolation to s→∞. Real W(3,4) lex full CORE also has 32428 genuine endpoint-good physical directed proper 3paths, of which 17364 have at least one of the four blockers. Hence the source/physical positive tests are genuinely nonvacuous.

The GitHub-hosted specialist workflow on Ubuntu 24.04 / Python 3.12 runs 20 independent tests plus an exact fail-closed JSON certificate and artifact. Require specialist, INDEX and full Research CI SUCCESS on the FINAL exact child commit before engineering acceptance; finite tests alone do not establish the symbolic all-h theorem.

**Next allowed scientific step:** independent original six-incidence-ID P3→produced U_BB-overlap reverse-inverse (exactly two opposite directed physical paths per produced original sixset), followed by an end-to-end proof dependency audit and only then a possible decision whether root #230 is PROVED_A. No ancestor/main PR merges, issue closure or ASET exponent promotion from this local result.
