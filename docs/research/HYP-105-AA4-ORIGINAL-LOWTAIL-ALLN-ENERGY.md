# HYP-105 / #230 — AA4-LOWCERT: exact finite-order ORIGINAL deletion-masked low-tail energy certificate

**Scope.** Strict mathematical Draft stacked on frozen, CI-green [#730](https://github.com/definitely-stable/Mathlab/pull/730) HEAD \`ee015de1484bb954b14dc47e9358552c79b40dc9\`. This slice constructs a self-contained **all-finite-original-order deterministic inequality**, combining the genuine physical three-path density, exact original endpoint-source exception and deletion masks, and the two TRUE ORIGINAL point/line dual FULL-allowed/CORE four-blocker source books. It uses any fixed separately globally injective but arbitrarily correlated f,g on the TRUE symplectic W(3,s), source-ID deletion Z and paired source CORE C⊆I\Z. No assumptions about probabilistic f/g, external C6 graph supersaturation constants or small D6 are needed for the inequality itself. To turn its right side into an all-h positive \(\Omega(s^6)\) floor requires separate genuine geometric moment and core-existence estimates; root #230 stays **OPEN_WITH_FORMAL_BLOCKER**. No main or parent edits, no merge.

## 1. TRUE ORIGINAL source, physical and dual parameters

Let \(I\) be the complete genuine W(3,s) point/line incidence source flags and \(a\) the fixed minimal physical point/line pair alphabet. Every retained source flag owns both REAL opposite physical diagonals. Fix ANY deleted ORIGINAL source flag ID set \(Z\) and a paired physical source core \(C\subseteq I\setminus Z\). Let \(A_C\) be the physical core adjacency on the full \([a]^2\) physical vertex set including isolated physical corners, \(m=2|C|\) its physical edges and \(\Delta=\max\deg A_C\), \(n=a^2\).

Define actual original point pencil \(R_C(p,y)=\#\{(p,\ell)\in C:y\in g(\ell)\}\) and the dual line pencil \(R_C^\vee(\ell,x)=\#\{(p,\ell)\in C:x\in f(p)\}\). Their coordinate-return books

\[
Q_x=2\sum_{p,y}R_C(p,y)^2,\quad
Q_y=2\sum_{\ell,x}(R_C^\vee(\ell,x))^2
\tag{LOW-1}
\]

are EXACT sums of source physical two-walks with equal first (respectively second) physical coordinate endpoints, regardless of whether the physical core itself is coherent or bipartite. Write \(P_3(u,v)\) for the count of directed length-three physical CORE walks whose FOUR first coordinates are pairwise distinct and FOUR second coordinates are separately pairwise distinct. Let \(\|P_3\|_F^2=\sum_{u,v}P_3(u,v)^2\). Its exact full-core physical length-three walk total is \(W_3=\boldsymbol1^\top A_C^3\boldsymbol1\).

## 2. NEW exact arbitrary-Z exceptional ENDPOINT union

For all ordered physical endpoint pairs \((u=(x,y),v=(z,w))\) with \(x\ne z,y\ne w\), partition into five **mutually disjoint** true-original states:

1. **Missing:** \(\{x,z\}\) or \(\{y,w\}\) is not an actually occupied original global f/g factor pair.
2. **Incident:** the uniquely decoded original point q=f⁻¹{x,z} is incident with original line r=g⁻¹{y,w}.
3. **Original source end-bad:** genuine GQ projection q—ℓ—p—r exists (q nonincident r) but \(f(p)\cap\{x,z\}\ne\varnothing\) or \(g(\ell)\cap\{y,w\}\ne\varnothing\).
4. **Deleted ORIGINAL GQ projection:** all preceding conditions pass, but at least one of the THREE uniquely projected original source flags \((q,\ell),(p,\ell),(p,r)\) is in Z. The SOURCE geometry, not a pruned/random replacement, supplies these actual original ID flags. In particular **NONE of the three projection flags is forced to lie inside the smaller physical core C**.
5. **Admissible:** none of the above; all three projected ORIGINAL flag IDs survive Z.

Let \(E_{\mathrm{bad}}\) be the **actual set** of the first four categories (not the sum of their old union-bound cardinalities), \(e_{\mathrm{bad}}=|E_{\mathrm{bad}}|\). The union is computed exactly using FULL original GQ projection geometry, before looking at physical core paths. The total partition has exactly \(a^2(a-1)^2\) ordered off-coordinate endpoint pairs. Every proper physical three-path with endpoints in \(E_{\mathrm{bad}}\) is excluded as an ORIGINAL B/B-overlap source sixset; weighted Cauchy yields

\[
\boxed{
M_{\mathrm{bad}}=\sum_{(u,v)\in E_{\mathrm{bad}}}P_3(u,v)
\le \sqrt{\,e_{\mathrm{bad}}\|P_3\|_F^2\,}.
}
\tag{LOW-2}
\]

This is strictly more source-instance-specific than replacing \(e_{\mathrm{bad}}\) by the rough sum of separate analytic \(O(s^5)\) exceptions and \(12s^2|Z|\). It never assumes original f/g are independent or physical paths are uniformly distributed across their endpoint pairs.

## 3. NEW pair of ORIGINAL FULL-allowed/CORE masked source blocker books

For the true nondeleted full source \(A=I\setminus Z\) (NOT the smaller core C), define

\[
R_A(p,y)=\sum_{(p,r)\in A}\mathbf1[y\in g(r)],\qquad
K_{A,C}(p,u)=\sum_y R_A(p,y)R_C(u,y).
\]

Let \(S_x=\{q:x\in f(q)\}\), \(c_x(p)=|\{q\in S_x:q\ne p,\ q\sim p\}|\), where \(q\sim p\) is the actual original GQ point-collinearity relation. The TRUE SOURCE first-inner-x book is

\[
\boxed{B_x=
 \sum_{\substack{u,\,(x,k)\text{ either orientation}\\ f(u)=\{x,k\}}}
 \sum_{\substack{p:k\in f(p)}}c_x(p)K_{A,C}(p,u).}
\tag{LOW-3}
\]

**Important:** ORIGINAL \((p,r)\) flags in \(A\) can be OUTSIDE C. The first physical path flag belongs to C; its source right y coordinate couples \(R_C(u,y)\) to the FULL-allowed original r anchor through \(R_A(p,y)\). The original collinearity \(c_x(p)\) overcounts projected q. This gives a rigorous upper for the number of physically possible first-edge/end triples with all THREE projected original flags nondeleted and first-inner-x blocked by \(f(p)\). We do not pretend it counts only genuine surviving 3-paths; it is an honest overcount.

Define the distinct **line-dual** book \(B_y\) by exchanging all ORIGINAL source points/lines and the physical left/right factors f,g, using the TRUE original line-collinearity graph. Crucially \(B_x\) and \(B_y\) need not agree for arbitrarily correlated f,g. Each of the two first-coordinate blocker positions is bounded by the same source book after physical path reversal; likewise the two second-coordinate blocker positions are bounded by \(B_y\). Let \(t_4=\operatorname{tr}(A_C^4)\). By Cauchy and source-owner first-edge counting,

\[
\boxed{I_{\rm blocked}
 \le 2\sqrt{B_x\Delta t_4}
       +2\sqrt{B_y\Delta t_4}.}
\tag{LOW-4}
\]

The independent source physical witness verifies each of the **FOUR** separate inequalities \(I_{x,1}^2,I_{x,2}^2\le B_x\Delta t_4\) and \(I_{y,1}^2,I_{y,2}^2\le B_y\Delta t_4\). No illegitimate assumption that left/right original source and physical coordinates are interchangeable is made.

## 4. Main new finite-order low-tail ORIGINAL six-ID positive BBo inequality

There are \(W_3\) actual directed physical three-walks in the core. Blakley–Roy gives a universal density floor for any undirected physical graph on n=a² vertices:

\[
 W_3\ge\frac{(2m)^3}{n^2}
       =\frac{(4|C|)^3}{a^4}.
\]

Coordinate returns of a physical walk at gap 2 or 3 are at most \(3\Delta(Q_x+Q_y)\), even though the original core may have all physical coordinate-return defects and may not itself be bipartite. Thus actual proper three-walk count satisfies

\[
 \sum_{u,v}P_3(u,v)\ge
 \frac{(4|C|)^3}{a^4}-3\Delta(Q_x+Q_y).
\tag{LOW-5}
\]

Exclude the **exact union of original endpoint exceptions and projection deletions** using (LOW-2), then the four internal blockers using (LOW-4). Every remaining proper physical 3-path is endpoint-good, all three path flag owners in the Z-free core, all three true original projected GQ flags outside Z, and has all four internal blockers absent. Such a path yields SIX DIFFERENT actual original source incidence ID flags of the historical GF(5)-positive B/B-overlap sixset. Its exactly two directed path representations are its two reversals, so the TRUE ORIGINAL full positive \(B_{\bar Z}\) class contains at least half the surviving good paths.

Therefore the **new deterministic, all finite dyadic orders, arbitrary correlated fixed f,g and adversarial deleted Z, SOURCE-ID sixset bound** is

\[
\boxed{
2B_{\bar Z}(f,g)\ \ge\
\max\left\{0,\
\frac{(4|C|)^3}{a^4}
-3\Delta(Q_x+Q_y)
-\sqrt{e_{\rm bad}\|P_3\|_F^2}
-2\sqrt{B_x\Delta t_4}
-2\sqrt{B_y\Delta t_4}
\right\}.
}
\tag{LOWCERT}
\]

The stronger true-observable source correction \(\sum P_3-M_{\rm bad}-2\sqrt{B_x\Delta t_4}-2\sqrt{B_y\Delta t_4}\) is also valid. An even stronger exact source/physical tally is

\[
2B_{\rm produced}
=\sum P_3-M_{\rm bad}-I_{\rm blocked},
\tag{LOWCERT-EXACT}
\]

where \(B_{\rm produced}\) is the set of positive BBo sixsets realized by the particular physical paired core C; all its six original IDs avoid Z. This is an exact identity and \(B_{\bar Z}\ge B_{\rm produced}\). Neither proof imports the graph SS6 theorem. It is an integrated, independently falsifiable low-tail source bridge, not a new claim of uniform positivity for all maps at an arbitrary finite h.

The code uses **exact integer square-root ceilings** and exact Fraction-valued \((4|C|)^3/a^4\) to produce a conservative integer-checkable lower. It additionally reports the exact proper, bad endpoint and four blocked sets of physical paths, their original positive sixsets, all four source/physical blocker inequalities and the exact source point/line mixed B/F1/F2 records.

## 5. Limitations and relation to existing all-h arguments

Previous #672/#674 argue that, after source heavy-tail and conflict removal, **for every sufficiently large dyadic s**, a core C with \(|C|=\Omega(s^4)\), \(\Delta=O(s)\), original Qx+Qy=O(s^4), the proper path \(L^2\) moment \(O(s^6)\), fourth moment \(O(s^5)\), and source-mixed \(B_x,B_y=O(s^{23/4})\) exists whenever surviving D6 is small. If those auxiliary bounds and the external heavy-tail theorem are mathematically accepted, our new finite-order (LOWCERT) applies directly: its leading lower density is \(\Omega(s^6)\), while its three error classes are \(O(s^5),O(s^{11/2}),O(s^{47/8})\), all \(o(s^6)\). **This algebra does not supply those auxiliary geometric moment bounds itself** and is NOT independent proof of the complete root A/B/C theorem.

The new benefit is a SINGLE all-N SOURCE-ID-preserving, deletion-mask-aware inequality with completely separated physical/source inputs, independently computed dual blocker books, and exact finite per-instance rejection gates; this makes incorrect source/coordinate substitutions or hidden dependence on f/g randomization falsifiable. Future scientific priority: independently obtain/check strong analytic upper bounds for the low-tail original collinearity F1 energies for all admissible fixed f,g under the same Z mask, or find a geometric correlated counterexample.

No merge, issue closure, arbitrary host theorem, numerical published C_graph/c_graph guess or new ASET exponent.


## 6. Independently checked complete genuine ORIGINAL W32/W34 finite source results

The specialist source test [GitHub Actions #41958240123](https://github.com/definitely-stable/Mathlab/actions/runs/41958240123) on the then-exact source HEAD completed **SUCCESS: 7 independent all-original tests + 8 permanent exact replay/tamper tests**, and a separate required full four-case source JSON proof gate under \`set -euo pipefail\`. The complete **58,657-character** genuine source six-ID certificates are retained in \`research/hyp105_original_lowtail_alln_energy_certificates.json\` and independently rebuilt by the permanent checker. The seven ordinary tests include a *different prior* #673 source-projection oracle with independently constructed physical paths and original six-ID BBo outputs: **exactly the same positive SIX-ID source sets** result in all four distinct true original f,g,Z,C cases. Separate literal physical \(A_C^2\) two-walk return measurements reproduce both original point/line \(Q_x,Q_y\) source-pencil equalities.

| True original symplectic source/frozen global maps | Retained C ORIGINAL flag IDs | Deleted Z ORIGINAL flags | ALL directed physical 3-walks | Proper directed physical 3-paths | Paths excluded by exact ORIGINAL endpoint+Z mask | Paths excluded by ≥1 of FOUR internal geometric blockers | Genuine positive ORIGINAL BBo sixsets |
|---|---:|---:|---:|---:|---:|---:|---:|
| W(3,2) lex | 30 | 1 | 2,254 | 416 | 370 | 44 | **1** |
| W(3,2) reverse-line | 34 | 1 | 2,504 | 448 | 362 | 86 | 0 |
| W(3,4) lex | 247 | 14 | 43,880 | 18,624 | 12,114 | 3,442 | **1,534** |
| W(3,4) reverse-line | 176 | 15 | 14,592 | 5,854 | 3,748 | 1,180 | **463** |

Each row independently verifies the **exact** original source identity
\[
\#(\mathrm{proper\ directed\ physical\ 3paths})
=\#(\mathrm{masked/bad\ endpoint\ paths})
+\#(\mathrm{internally\ blocked\ admissible\ paths})
+2\#(\mathrm{accepted\ original\ BBo\ sixsets}).
\]

On W(3,4), the newly integrated ORIGINAL projection bad-endpoint union consists of:

| W34 frozen maps | Missing original f/g endpoint labels | Original incident q,r | Original-end-bad projection | Projection anchors with ≥1 deleted ORIGINAL ID | EXACT union of bad ordered physical endpoints |
|---|---:|---:|---:|---:|---:|
| lex | 4,224 | 1,700 | 14,592 | 1,272 | **21,788** |
| reverse-line | 4,224 | 1,700 | 14,600 | 1,216 | **21,740** |

This disjoint five-state classification counts *real* original projected ID flags, rather than summing independent invented source-coordinate error populations. Specifically, the ORIGINAL deletion-projection component in these examples is **1,272** vs the old coarse bound \(12s^2|Z|=2,688\) for lex and **1,216** vs \(2,880\) for reverse-line. The source-projection mask is therefore materially sharper and provably complete for these finite original cases.

The two dual internal point/line source books are genuinely **different**:
- W34 lex \(B_x=28,073\), \(B_y=28,355\).
- W34 reverse-line \(B_x=20,095\), \(B_y=19,505\).

The four independently recorded actual physical blocker populations also differ: W34 lex \((1046,1046,1138,1138)\); reverse-line \((357,357,411,411)\). Treating the point and line sources as numerically identical would be wrong even for these ordinary globally injected complete original maps.

**Essential limitation / correct interpretation:** the all-N bound (LOWCERT) is rigorous and nonnegative after taking \(\max\{0,\cdot\}\), but its **conservative analytic right side is negative in all four small-source fixtures before the maximum**. The strong positive 1/1,534/463 historical ORIGINAL BBo counts in the table are obtained by the **exact source/physical partition (LOWCERT-EXACT)** and independently verified original classifier, **NOT** by pretending the coarse analytic inequality is positive at W32/W34. Improving its all-h positive use requires separately accepted source existence/caps and moment estimates (or stronger numerical low-tail certificates), not numerical extrapolation from the small true source cases.

The completed checks are proof-oriented finite falsifiers of the exact combinatorial identity and each independently named all-N bound. They cannot certify a uniform all-map \(\Omega(s^6)\) theorem, numerical unknown external graph-theorem constants or a new ASET exponent. Root #230 must remain OPEN_WITH_FORMAL_BLOCKER.
