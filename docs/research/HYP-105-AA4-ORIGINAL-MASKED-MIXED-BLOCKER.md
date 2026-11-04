# HYP-105 / #230 — AA4-ZMIX: ORIGINAL-source deletion-commuting FULL/CORE mixed blockers

**Research Draft, distinct from scientific acceptance of the root theorem.** Strictly stacked on frozen [#727](https://github.com/definitely-stable/Mathlab/pull/727) exact HEAD \`f1c9e4b924b41ef3ae7358d96ab5dd757bb0c1a1\` (all 3 exact-head CI workflows SUCCESS). The root #230 remains \`OPEN_WITH_FORMAL_BLOCKER\`. No merge, no changes to main or frozen ancestors. This result targets the most substantive outstanding independent proof gates from the earlier all-h Drafts [#672](https://github.com/definitely-stable/Mathlab/pull/672) and [#674](https://github.com/definitely-stable/Mathlab/pull/674): the mixed FULL/CORE blocker estimate and the translation of physical proper paths into genuine, positive GF(5) six-ORIGINAL-incidence-ID B/B-overlap motifs, even after deleting adversarial original flag IDs.

## 1. What was actually missing

The previously documented universal proof relies on a source FULL/CORE mixed contraction (eqs. 13–18 of #672) for internally blocked physical three-paths and its transfer to source-deleted paired cores in #674. Prior finite referees variously tested the undamaged original full source against a core, or deleted original ID sets against positive B/B-overlap path counts. To independently validate *their conjunction*, we must not silently do any of these three things: (i) replace deleted original source flags with new factor labels; (ii) force the projection anchor source flags to lie in the retained CORE (they may be OUTSIDE the core while still outside Z); (iii) change the source-owner granularity from two diagonals per real flag to unrelated physical coordinate edges.

The new lemma is an **exact all-N identity** for the FULL/CORE term for any fixed global separate pair injections f,g and any deletion Z, and its proof does not need the external even-cycle supersaturation theorem or small-D6 assumption.

## 2. Theorem: exact mask-contraction and ORIGINAL owner sensitivity

Write I for all distinct true ORIGINAL point-line incidence flags in the *same* genuine W(3,s), s=2^h. Freeze complete globally injective physical point/line pair embeddings f,g. Let Z be ANY set of real original flag IDs, A=I\Z all allowed source flags and C⊆A ANY retained paired original source CORE.

For every original point p and right physical coordinate y set

\[
 R_A(p,y)=\sum_{\ell:(p,\ell)\in A}\mathbf1[y\in g(\ell)],
 \quad R_C(u,y)=\sum_{\ell:(u,\ell)\in C}\mathbf1[y\in g(\ell)].
\]

Define the FULL-allowed and CORE physical vertex degrees by

\[
 D_A(k,y)=\sum_{p:k\in f(p)}R_A(p,y),
 \qquad
 D_C(k,y)=\sum_{u:k\in f(u)}R_C(u,y).
\]

Each real original source flag contributes exactly TWO unique opposite diagonals to the physical graph, hence these are EXACT degrees of physical vertices (k,y), NOT surrogate counts.

Define \(K_{A,C}(p,u)=\sum_y R_A(p,y)R_C(u,y)\) and

\[
 \Theta_{A,C}:=\sum_{k,y}D_A(k,y)D_C(k,y).
\]

**New exact all-source identity:**

\[
\boxed{
\Theta_{A,C}
 =\sum_{u\,:\,f(u)=\{x,k\}}
       \ \sum_{\text{both orientations }(x,k)}
       \ \sum_{p:k\in f(p)}K_{A,C}(p,u).
}\tag{ZMIX-1}
\]

The first sum is over source points u that own at least one original flag in C; for other points, \(R_C(u,\cdot)=0\). Equivalently, this sums the two factor-pair orientations for each u, not the number of its incidence flags twice. The proof is a finite rearrangement of nonnegative counts:

\[
\sum_{k,y}
  \underbrace{\sum_{p:k\in f(p)} R_A(p,y)}_{D_A(k,y)}
  \underbrace{\sum_{u:k\in f(u)} R_C(u,y)}_{D_C(k,y)}
=\sum_{u,(x,k),p}\sum_y R_A(p,y)R_C(u,y).
\]

Now hold the same core C FIXED and compare the all-flags-original physical graph degrees \(D_I\) with \(D_A\). For any deleted original flag \(i=(p,\ell)\in Z\), its two physical diagonals touch exactly FOUR distinct physical vertices

\[
 (f(p)_0,g(\ell)_0),\
 (f(p)_0,g(\ell)_1),\
 (f(p)_1,g(\ell)_0),\
 (f(p)_1,g(\ell)_1).
\]

Its removal subtracts exactly one from each of these four degrees, and never alters any remaining source owner or the core graph.

**New exact deletion sensitivity:**

\[
\boxed{
\Theta_{I,C}-\Theta_{A,C}
 =\sum_{i=(p,\ell)\in Z}
    \sum_{k\in f(p)}\sum_{y\in g(\ell)}D_C(k,y).
}\tag{ZMIX-2}
\]

It immediately proves monotonicity in original source deletions Z for a **fixed** C, even if Z is map-dependent/adversarial. It also quantifies the precise physical CORE interaction weight of EACH removed ORIGINAL flag — four endpoint degrees, NOT two source incidences or four independent source edges.

With \(\Delta_C=\max_{v}D_C(v)\), \(\sum_v D_A(v)=4|A|\) gives

\[
0\le\Theta_{A,C}\le4|A|\Delta_C.
\tag{ZMIX-3}
\]

If \(d=s+1\) is the number of lines through an original point, and \(M_C=\max_{u,y} R_C(u,y)\), then \(\sum_yR_A(p,y)\le 2d\) and

\[
0\le K_{A,C}(p,u)\le 2dM_C,\qquad
\sum_{u,(x,k),p}K_{A,C}(p,u)^2
\le (2dM_C)\Theta_{A,C}.
\tag{ZMIX-4}
\]

For a source-conflict-capped paired core as in #672/#674, one has the independent requisite \(M_C\le K+1\), recovering its original mixed FULL/CORE Cauchy factor without any assertion of random f,g, uniform fiber distribution, or anchor core membership. The deleted-original-source contraction gives a deterministic improvement over using the full source degree \(D_I\) when Z has positive mass.

## 3. True original source blocker book and complete physical first-edge equality

For each candidate core physical first edge \(v_0=(x,y)\to v_1=(k,y_1)\) owned by real source flag \((u,\lambda)\in C\), and every original point p with k∈f(p), consider each original point q collinear with p and x∈f(q), and original line r incident with p such that (p,r)∈A and y∈g(r). Denote by \(c_x(p)\) the number of original q collinear with p whose point label f(q) contains x.

The exact count of these ORIGINAL-SOURCE records is

\[
\boxed{
 B_{A,C}=
 \sum_{u,(x,k),p}
 c_x(p)K_{A,C}(p,u).
 }\tag{ZMIX-5}
\]

This book counts ORIGINAL incidence-backed records: a core physical first edge, an actual source p, an actual collinear q, and an actual nondeleted original anchor flag (p,r). It DOES NOT claim these records are all geometric three-paths or that their anchors (q,\ell),(p,\ell) have survived; it is an overcount for paths relevant to B/B-overlap.

Let \(F_1=\sum_{u,(x,k),p}c_x(p)^2\) and \(F_2=\sum_{u,(x,k),p}K_{A,C}(p,u)^2\). Cauchy together with (ZMIX-4) gives the true masked ALL-N chain

\[
\boxed{ B_{A,C}^2\le F_1F_2
  \le F_1(2dM_C)\Theta_{A,C}
  \le F_1(2dM_C)\,4|A|\Delta_C. }\tag{ZMIX-6}
\]

The original #672 collinearity spectral estimate on F1 is unchanged by Z. The masked book can therefore be inserted into the original sub-sextic original-blocker argument without introducing a new exponent, while making explicit that only the **anchor (p,r)** has been restricted. Other original projection anchors are checked separately using the exact GQ source projection; no deletion is silently ignored.

For nonincident q,r, the original generalized-quadrangle projection q--ell--p--r is unique. Both physically and source-first, the set of eligible first-edge/last-vertex triples (v0,v1,v3) with all three projection flags outside Z and k∈f(p) is reconstructed from the SAME six original source IDs. All eligible triples are among the counted \(B_{A,C}\) records. If \(W=\sum_{\mathrm{eligible}}(A_C^2)_{v_1,v_3}\), the physical Cauchy and source-Degree trace identity independently prove

\[
\boxed{W^2\le \#\mathrm{eligible}\!
  \sum_{\mathrm{eligible}}(A_C^2)_{v_1,v_3}^2
\le B_{A,C}\,\Delta_C\,\operatorname{tr}(A_C^4).}
\tag{ZMIX-7}
\]

This bounds the **weighted** number of actual physical two-step completions after the first edge; it does not assume uniformity of endpoint paths. The formula is a valid local original source/physical step whether or not an all-h positive sextic bound is already accepted.

## 4. Independent full G7 original source six-ID B/B-overlap reconstruction

On the SAME allowed original flags A=I\Z and retained paired C, independently enumerate proper directed three-edge physical CORE paths \(v_0,v_1,v_2,v_3\) with four different x and four different y physical coordinates, occupied nonincident endpoint original q,r, and FULL-source unique GQ projection q--ell--p--r. Require the endpoint-good conditions \(f(p)\cap\{x_0,x_3\}=\varnothing\) and \(g(\ell)\cap\{y_0,y_3\}=\varnothing\), all THREE original projection anchor IDs outside Z, and absence of each of the FOUR physical inner-coordinate blockers:
\[
x_1,x_2\notin f(p),\qquad y_1,y_2\notin g(\ell).
\]
The physical three-core-edge path is tagged by its ACTUAL three original flag owners using the physical edge owner table, then the UNIQUE original projection contributes its three ORIGINAL flags. All six original IDs must be different and outside Z, and the historical GF5 original sixset classifier must accept **B/B-overlap**. Each accepted original sixset has precisely TWO directed paths, related by reversal. This is a direct original-side finite falsifier of #672 §7 / #674 G7 with arbitrary source deletion Z and anchors **outside C** still permitted. The direct path census is independently checked against the existing different #673 forward source-deletion oracle on W32/W34.

An all-N abstract inverse proof of the at-most-two path normalization already appears in the source-first #BBOINV module; this slice's new contribution is its rigorous **simultaneous pairing with (ZMIX-1)–(ZMIX-7) under arbitrary Z** and comprehensive numerical independent finite checks. We do not claim to have freshly proved the full #672 mixed-blocker 47/8 exponent: it still depends on accepted moment and collinearity estimates.

## 5. Proof completeness and exactly what remains

\`research/hyp105_original_masked_mixed_blocker.py\` rebuilds all real symplectic source flags and uses TWO independent source-first vs physical-endpoint-first algorithms for all GQ projection triples. It verifies (ZMIX-1) with a direct ORIGINAL full-core 28D/12D physical degree contraction, the completely separate four-cell original flag source-owner deletion sensitivity in (ZMIX-2), direct original p,q,r source records vs the physical book in (ZMIX-5), exact F1/F2 and weighted physical A_C^2 Cauchy in (ZMIX-6)–(ZMIX-7). An independent THIRD enumeration walks actual core physical 3-paths with all six original-ID flags and full source historical acceptance and proves the path multiplicity exactly two.

The tests cover genuine W(3,2) AND W(3,4) globally injected lex/reverse-line maps, zero/singleton/minimum-hitting-set adversarial Z from #727, full and sparse cores, Z changes while holding the CORE fixed, and physical original flags whose nondeleted projection anchors lie OUTSIDE C. The independent source G7 forward auditor from #673 crosschecks all produced original sixset IDs. Deliberately malformed complete f,g, overlapping core/deleted original IDs and duplicate source IDs fail closed. All runs use **GitHub-hosted runners only**, no local PC.

**This does NOT prove:** the published graph C6 supersaturation theorem's numerical valid constants, a new D6+BBo Ω(s⁶) result for every possible globally injected f,g, the #672 selector/moment/exceptional-endpoint lemmas, all-h root HYP-105 #230, or a new ASET power. It is an independently derived original-source-mask commutation and G7 bridge: a stronger **necessary acceptance gate**, but not automatic acceptance of #672/#674. Scientific Draft review and qualified mathematical assessment remain separate from finite successful GitHub CI.

**Next allowed mathematical gate after this slice:** independently reconstruct the #672 all-h sixth/fourth moment selector and the 47/8 error bound from first principles with explicitly proven original source projection, or isolate a specific failure. No all-h Branch A/B/C promotion until those gaps are closed.
