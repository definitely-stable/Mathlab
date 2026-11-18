# HYP-105 / #230 — AA4-LOW-ENDPOINT-OVERLAP: exact SOURCE degree-quadratic and correlated physical endpoint union

**Scientific status:** all-order scoped ORIGINAL source theorem; exact finite checks on true W(3,2) and W(3,4). Strict child of frozen [Draft #772](https://github.com/definitely-stable/Mathlab/pull/772) HEAD cf34035ecd869d7d3577e66ffd4da3ba33a49be5. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**, not PROVED_A, no ASET exponent, no merges or parent/main changes.

## 1. Novelty and source attribution

[PR #748](https://github.com/definitely-stable/Mathlab/pull/748) **ALREADY** proved the deletion union identity M=8s²|Z|+4(D-H-F), with H counting all three deleted anchors and F counting the two deleted outer anchors with a retained middle. This work DOES NOT claim to rediscover that identity. Its new result is the **local O(|I|+|Z|) degree-quadratic formula for H+F** (no exhaustive nonincident projection scan); two independent point/line source-first evaluations; an exact degree-weighted application of the previously known GQ incidence spectrum; and full physical END-BAD/deletion intersection bookkeeping without independence of f and g.

## 2. Quantified genuine ORIGINAL model

Let s=2^h, h≥1, V=(s+1)(s²+1). Let I consist of the N=(s+1)V original named flags (p,ell) in symplectic W(3,s). Fix **any** named original deletion Z⊆I, possibly chosen after any two arbitrarily correlated, complete, separately globally pair-injective physical maps f and g. A nonincident q (point) and r (line) have a unique FULL ORIGINAL GQ projection with three distinct anchor flags (q,ell), (p,ell), (p,r). These are not artificial source copies and need not all be in the retained CORE.

Let d_p and d_ell denote numbers of Z-flags incident with p and ell, respectively. Let T_outer count FULL projections with BOTH first and last ORIGINAL anchors in Z, regardless of middle deletion. Let D_middle count deleted middle anchors with both outer anchors **not** deleted, and U_Z count projections hit by at least one deleted anchor. Every ORIGINAL flag belongs to exactly s² projections in each of the three roles.

## 3. New exact local OUTER intersection formula

Fix a deleted LAST flag (p,r)∈Z, then choose a different original line ell through p and a deleted first flag (q,ell), q≠p. At fixed ell this gives d_ell−1_{(p,ell)∈Z} choices. Summing exact FINITE integer counts and exchanging the summation order proves

\[
\boxed{T_{\mathrm{outer}}=
\sum_{(p,\ell)\in I}d_p d_\ell
-\sum_{\ell\in L}d_\ell^2
-\sum_{p\in P}d_p(d_p-1).}\tag{EO-1}
\]

The first sum arises because each source point p occurs in d_p deleted last flags; excluding ell=r costs the sum of d_ell², and excluding q=p costs the sum of d_p(d_p−1). The point/line dual derivation starts with the deleted FIRST flag and counts deleted last flags directly; both are implemented separately from exhaustive (q,r) projection census. The identity holds for any simple typed incidence graph as a statement about nonbacktracking length-three source paths; in a true GQ these paths coincide bijectively with the uniquely projected nonincident endpoints.

Retain the **already established #748** factorization

\[
D_{\mathrm{middle}}=\sum_{(p,\ell)\in Z}
(s+1-d_p)(s+1-d_\ell).
\tag{EO-2}
\]

Since deleted first and last source roles each occur s²|Z| times, the previously known union identity is rewritten exactly as

\[
\boxed{U_Z=2s^2|Z|-T_{\mathrm{outer}}+D_{\mathrm{middle}},\qquad
M_{\mathrm{deleted,all}}=4U_Z.}\tag{EO-3}
\]

The multiplicity four means two endpoint orders in f and two in g; it is NOT a fourfold original six-motif claim.

**New computational benefit:** EO-1 to EO-3 require O(N+|Z|) integer operations and O(V) memory after reading the FULL source. Historical source-first H/F verification enumerated nonincident pairs; the new source-only quadratic avoids this O(V²) scan. The implementation treats genuine GQ geometry as an axiom; independent exhaustive small-order oracles validate that axiom, never extrapolate finite calculations to all h.

## 4. Star deletion and conditional LOW error improvement

By #748, D_middle=0 if and only if Z is a union of complete ORIGINAL point/line stars. Therefore EO-3 and T_outer≥0 imply

\[
\boxed{M_{\mathrm{deleted,all}}\le 8s^2|Z|
\quad\text{if }D_{\mathrm{middle}}=0,}
\]

versus the universal bound 12s²|Z|. A single complete point star or line star attains 8s²|Z| exactly. The true W(3,2) mixed point/line star test yields |Z|=5, T_outer=4, D_middle=0, M_deleted=144; old #748 defect-only upper=160, naive universal upper=240.

For arbitrary Z, EO-3 is never worse than the pre-existing #748 defect-only bound because T_outer≥0. A single deleted ORIGINAL flag saturates the older universal estimate and hence NO unconditional coefficient-8 claim is made for arbitrary deletion. This is an exact deletion-mask-dependent improvement, not a better all-label universal ASET exponent.

## 5. Weighted GQ spectrum applied to deletion degree vectors

Let B be the TRUE original point-line incidence matrix, NOT the arbitrarily deleted physical graph. The classical GQ singular values imply the centered bound for d_P,d_L,

\[
\boxed{\big[Vd_P^\top Bd_L-(s+1)|Z|^2\big]^2
\le 2s\big[V\sum_p d_p^2-|Z|^2\big]
        \big[V\sum_\ell d_\ell^2-|Z|^2\big].}\tag{EO-4}
\]

The source spectrum is known prior art and was also proved in [#762](https://github.com/definitely-stable/Mathlab/pull/762); this is a scoped new application. Every certificate uses the exact nonnegative INTEGER slack, not numerical eigenvalue fitting. EO-4 alone does NOT prove a positive universal lower bound for T_outer, and no Cheeger-equality or root Branch A claim is inferred from it.

## 6. Correlated physical END-BAD and deleted union

For every nonincident (q,r), let (p,ell) be its genuine GQ projection. Define X=[f(q) shares a physical symbol with f(p)], Y=[g(r) shares a symbol with g(ell)], and Zhit=[at least one of the three true ORIGINAL anchors is in Z]. Let e_f count unordered distinct collinear ORIGINAL point pairs with overlapping physical f labels; let e_g be the corresponding ORIGINAL line-pair count. Exact GQ path multiplicities yield ΣX=2s e_f, ΣY=2s e_g. Define true correlations C_XY=ΣXY and C_Zbad=Σ Zhit(X∨Y). No pair-label independence is assumed. Then

\[
B_{\mathrm{nonincident\ bad}}
=2s(e_f+e_g)-C_{XY}+U_Z-C_{Zbad}.\tag{EO-5}
\]

For minimal a with binom(a,2)≥V, set Bpair=binom(a,2). There are exactly 4Bpair² oriented off-coordinate physical endpoint pairs. Among them 4(Bpair²−V²) have missing source endpoint labels and 4N have a decoded ORIGINAL incident point-line pair. Thus the **exact** endpoint pair census is

\[
\boxed{|E_{\mathrm{bad}}|=
4(Bpair^2-V^2+N+B_{\mathrm{nonincident\ bad}}),}
\quad
|E_{\mathrm{good}}|=4(V^2-N-B_{\mathrm{nonincident\ bad}}).\tag{EO-6}
\]

The two cardinalities sum to 4Bpair². They are endpoint-PAIR counts, not direct counts of prohibited original physical 3paths. For the proper threepath endpoint multiplicity matrix P3, the permitted Cauchy transfer is

\[
\sum_{(u,v)\in E_{\mathrm{bad}}}P3(u,v)
\le \sqrt{|E_{\mathrm{bad}}|\,\|P3\|_F^2}.\tag{EO-7}
\]

In particular, for the deleted-only endpoint class one can conservatively use 4U_Z instead of 12s²|Z|; EO-5 additionally subtracts true endbad/deletion overlap and prevents double charging. This is a conditional tightening of the global LOW endpoint budget; source fourth/sixth-moment, selected C6->D6 and produced P3->BBo assumptions remain separately subject to publication-grade review.

## 7. Independent falsifiers and restrictions

The source implementation gives three independent OUTER oracles: the fast EO-1 formula; point-FIRST and line-LAST genuine source pencils; and a FULL (q,r) GQ projection enumeration with three-role multiplicity checks. Tests cover true W(3,2) and W(3,4), structured/adversarial masks from #748, all 990 two-flag deletion subsets of W32, original point-line duality, flag-index reversal, and separately injected lex/reversed g pair labels including physical X/Y/Z correlations. They reject malformed original IDs, invalid flag lists and repeated pair labels. Specialist GitHub-hosted Python 3.12, strict JSON, INDEX and Research at **the same final PR HEAD** are required; a passing finite suite is not an all-order proof. Root #230 remains OPEN_WITH_FORMAL_BLOCKER. No parent/main updates, merge or new numerical external C6 constants.
