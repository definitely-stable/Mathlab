# HYP-105 / #230 — AA4-ZTAIL: deletion-robust ORIGINAL heavy-tail to ordinary \(C_6\), exact instance-adaptive SS6 certificate

**Scientific scope.** New independently derived **all finite dyadic \(s=2^h\)** deterministic heavy-tail/real-source \(D_6\) transfer. Adversarial source-ID deletions are included, and an instance-adaptive threshold uses actual ORIGINAL source-conflict density, not just the source-wide spectral envelope. The heavy-tail branch uses the peer-reviewed ordinary graph sixcycle supersaturation theorem, Jiang–Yepremyan (2020), Theorem 1.1 specialized to \(r=2,k=3\), DOI [10.1017/S0963548320000206](https://doi.org/10.1017/S0963548320000206). That theorem asserts *existence* of absolute positive \(C_{\rm graph},c_{\rm graph}\); neither their numerical values nor an explicit numerical dyadic \(h_0\) are certified here. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**. Strictly stacked on unchanged CI-green scientific Draft [#729](https://github.com/definitely-stable/Mathlab/pull/729) exact parent HEAD \`837e1916e22277cc1c3ac328819787ee34fe482e\`. No merge, no upstream/main changes.

## 1. The EXACT original-to-ordinary graph theorem interface

Let \(I\) be the complete genuine ORIGINAL set of incidence flags \((p,\ell)\) of the symplectic generalized quadrangle \(W(3,s)\), \(s=2^h\); \(|I|=N=(s+1)^2(s^2+1)\), and let \(V=(s+1)(s^2+1)\) and \(a=\min\{b:\binom b2\ge V\}\). Freeze any complete, globally separately pair-injective point map \(f:p\mapsto\binom{[a]}2\) and line map \(g:\ell\mapsto\binom{[a]}2\), with **arbitrary correlation**. Each ORIGINAL flag ID \(i=(p,\ell)\) owns EXACTLY the two physical opposite-corner diagonal edges of the rectangle \(f(p)\times g(\ell)\); no two distinct ORIGINAL source flags own one physical edge. Let \(H\) be the complete ordinary physical graph on the **fixed** alphabet \([a]^2\), and fix any threshold \(T>0\). Define once and for all, BEFORE any source deletion:

\[
Q_T=\{v:\deg_H(v)>Ts\},\quad q=|Q_T|,\quad
E_T=\#\{uv\in E(H):\{u,v\}\cap Q_T\ne\varnothing\}.
\]

Now let **ANY** adversarial set \(Z\subseteq I\) of true ORIGINAL source IDs be deleted, without changing any global \(f,g\) or recomputing \(Q_T\). Put \(A=I\setminus Z\) and define \(E_A\) as the number of surviving true original-flag-owned physical edges of \(H\) incident with original \(Q_T\). Since each removed ORIGINAL flag owns exactly two diagonals, **for every** \(Z\),

\[
\boxed{E_A\ge E_T-2|Z|.}\tag{ZTAIL-1}
\]

Let \(I_A=\{i\in A:\text{at least one physical diagonal owned by }i\text{ touches }Q_T\}\) and \(L=|I_A|\). Then \(L\ge E_A/2\). Every source-ID in \(I_A\) has a distinct actual heavy-witness physical edge; the chosen selected graph will retain it.

Build the exact ORIGINAL-ID conflict graph \(J_{I_A}\): for distinct \(i=(p,\ell),j=(q,r)\in I_A\), connect them iff \(p=q\) and \(g(\ell)\cap g(r)\ne\varnothing\), or \(\ell=r\) and \(f(p)\cap f(q)\ne\varnothing\). The two conditions cannot overlap for distinct genuine original flags. Let \(e_J\) be its **ACTUAL** number of source-conflict pairs. Unlike #659's coarse universal bound \(e_J\le2C_s\), retain the actual \(e_J\) to obtain a strictly potentially stronger instance-dependent bound.

Caro–Wei/Cauchy gives a source-ID conflict-independent family \(J\subseteq I_A\) of size

\[
|J|\ge\sum_{i\in I_A}\frac1{1+\deg_{J_{I_A}}(i)}
\ge\frac{L^2}{L+2e_J}.
\]

Apply both deterministic coordinate two-color cuts to the **WHOLE** ORIGINAL flags \(J\). Each cut preserves at least half the actual flags by the elementary conditional-expectation algorithm; every kept original flag retains BOTH true physical diagonals. The resulting genuine source-owned selected graph \(G\subseteq H_A\) satisfies

\[
\boxed{|I_G|\ge \frac{L^2}{4(L+2e_J)}.}\tag{ZTAIL-2}
\]

Selected source flag owners are conflict-independent, so the physical G has no row/column cherries, and both original left and right coordinate cuts are bichromatic. Every ordinary simple six-cycle in G is coordinate-proper and recovers SIX DIFFERENT **nondeleted** ORIGINAL incidence flags, with the same aligned true source left/right original \(D_6\) six-cycle geometry. Consequently

\[
\boxed{C_6(G)\le D_{6,\bar Z}(f,g),}\tag{ZTAIL-3}
\]

where the right side counts accepted historical GF(5) **D6**, not arbitrary physical closed sixwalks or fake projected-flag counts. **This is independent of any randomization of \(f,g\)**.

## 2. NEW instance-adaptive *balanced ordinary chunk* and exact cubic SS6 hypothesis

For each retained true original source flag in \(I_G\), choose one ACTUAL surviving physical heavy-witness edge touching the frozen original Q_T. Assign its heavy endpoint to one of the TWO left-coordinate color classes of G; one class receives at least half, so that at least \(|I_G|/2\) **distinct physical** witness edges join \(R:=Q_T\cap X\) in this color class \(X\) to the opposite side \(Y\) of G. Write \(r=|R|>0\). All physical vertices are real named pairs \((x,y)\in[a]^2\); no cloned vertices, source flags or physical edges are introduced.

With the full original physical alphabet \(n=a^2\), partition the actual opposite color side \(Y\) into at most \(\lceil|Y|/r\rceil\le 2n/r\) disjoint blocks of size at most \(r\). Choose one actual winning block \(Y_*\) maximizing its genuine physical edge count into R and take the ordinary simple bipartite subgraph \(F=G[R,Y_*]\). It need NOT retain both source-flag diagonals (ordinary published graph theorem imposes no such restriction). By true physical edge pigeonhole,

\[
e(F)\ge \frac{|I_G|r}{4n},\qquad
v(F)\le2r\le2q,\qquad
\frac{e(F)}{v(F)}\ge \frac{|I_G|}{8n}.
\]

Together with (ZTAIL-2), **NEW exact instance-adaptive lower bound**

\[
\boxed{\frac{e(F)}{v(F)}\ge
     d_{\rm adaptive}:=\frac{L^2}{32n(L+2e_J)},
\qquad v(F)\le 2q.}\tag{ZTAIL-4}
\]

The genuine external graph theorem is stated in Jiang–Yepremyan (2020), Theorem 1.1, \(r=2,k=3\): positive **not numerically specified** constants \(C_{\rm graph},c_{\rm graph}\) exist such that

\[
e(F)\ge C_{\rm graph} v(F)^{4/3}
\implies C_6(F)\ge c_{\rm graph}\left(\frac{e(F)}{v(F)}\right)^6.
\tag{SS6}
\]

The exact source-adaptive sufficient hypothesis, equivalent to \(d_{\rm adaptive}^3\ge 2q C_{\rm graph}^3\), is:

\[
\boxed{
L^6\ge 2^{16} C_{\rm graph}^3 n^3 q (L+2e_J)^3.
}\tag{ZTAIL-5}
\]

When **(ZTAIL-5) holds for the ACTUAL positive published C_graph**, the independently constructed literal F meets the real theorem hypothesis \(e(F)^3\ge C_{\rm graph}^3 v(F)^4\). The **real original source** conclusion then follows:

\[
\boxed{ D_{6,\bar Z}(f,g)
 \ge C_6(F)
 \ge c_{\rm graph}\left(\frac{L^2}{32n(L+2e_J)}\right)^6.}
\tag{ZTAIL-6}
\]

No assumption that F is nearly regular, that its two sides have equal sizes, or that F retains both physical diagonals per source flag is necessary. The output stores the actual **integer physical** \(e(F),v(F)\) and the exact rational \(e(F)^3/v(F)^4\), in addition to the SOURCE lower bound in (ZTAIL-5). A trial \(C_{\rm graph}=1\) is *never* relabeled as the actual published existential constant.

## 3. NEW universal adversarial ORIGINAL deletion resilient tail branch; threshold improves 2× over frozen #674

The preceding theorem is all-N and includes any adversarial Z, with exact instance-specific \((L,e_J,q,n)\). For the **uniform all-h** form, use the already independently verified source incidence spectral bounds of #659/#684, valid for every \(s=2^h\ge64\):

\[
 a^2=n\le4s^3,\quad
 N\le2s^4,\quad
 e_J\le2C_s\le3s^4,\quad
 qTs<\sum_v\deg_H(v)=4N\le8s^4,
 \quad\boxed{q\le8s^3/T}.
\]

For every Z, suppose the frozen complete-source original heavy tail has

\[
E_T\ge2|Z|+\varepsilon s^4,\qquad \varepsilon>0.
\]

By (ZTAIL-1), surviving heavy edges number \(E_A\ge\varepsilon s^4\), hence \(L\ge\varepsilon s^4/2\), while \(4C_s+L\le8s^4\). Caro–Wei and both coordinate cuts now yield \(|I_G|\ge\beta s^4\) with \(\beta=\varepsilon^2/2^7\). The physical balanced chunk satisfies

\[
v(F)\le16s^3/T,\qquad
e(F)/v(F)\ge\beta s/32.
\]

Therefore the **sharp previously audited #684 all-h threshold**, now proven robust against ALL arbitrary ORIGINAL ID deletions Z, is

\[
\boxed{
T\ge 2^{19}C_{\rm graph}^3\beta^{-3}
     =2^{40}C_{\rm graph}^3\varepsilon^{-6}
\implies
D_{6,\bar Z}(f,g)\ge
c_{\rm graph}\varepsilon^{12}s^6/2^{72}.
}\tag{ZTAIL-7}
\]

This is a true-original **heavy-branch** theorem. It is stronger in both deletion scope and data-adaptive threshold than #659's undeleted 2^41 theorem; it imports #684's independently checked halved heavy-cardinality constant, but does **NOT** re-prove the external 24-page graph theorem or the complementary low-degree/core-proper-path branch. All maps f,g remain frozen and arbitrarily correlated, and Z can be an adversary dependent on f,g.

**Important conditional consequence for frozen #674:** its heavy-case dichotomy uses \(\varepsilon_{\rm full}=1/8\), \(|Z|\le\rho s^4\) with \(\rho\le1/32\), so \(\varepsilon_{\rm rem}\ge1/8-2\rho\ge1/16\). The sufficient original heavy-only cap therefore improves from its frozen \(2^{65}C_{\rm graph}^3\) to

\[
\boxed{T_{\rm new}=2^{64}C_{\rm graph}^3.}\tag{ZTAIL-8}
\]

All #674 low-tail degree/projection/mixed moment estimates are affected by T and need separate proof-consistent recalculation before changing **any** root h0/rho or claiming the root all-h theorem. This slice explicitly leaves all older parent constants untouched; it DOES NOT automatically establish a stronger complete Branch A or a new power-law exponent.

## 4. Independent historical original source and no-clone falsifiers

The new \`research/hyp105_original_deletion_adaptive_heavy_tail.py\` independently constructs TRUE symplectic W(3,2)/W(3,4) original flags and complete physically separately globally injected lex/reverse-line f,g. It does NOT use #684's selector implementation to create the witness. Instead it independently reconstructs real two-diagonal original physical owners, frozen FULL-Q before Z, exact original flag deletion loss, all surviving heavy original IDs, ACTUAL original source-conflict pair graph and its Caro–Wei sum, deterministic min-current-degree independent set, two deterministic conditional-expectation coordinate cuts, and both physical source diagonals per surviving original flag.

It then assigns actual heavy witness physical edges to the two color sides, takes a genuine no-clone physical opposite-side chunk, computes its *actual integer* e,v and exact external SS6 cubic ratio, enumerates ordinary simple physical sixcycles of the full selected source graph and the winning F independently, and checks every cycle's SIX distinct nondeleted original incidence flags and the historical accepted ORIGINAL GF(5) D6 topology. Every original source ID is preserved; there is no synthetic replacement for GQ geometry. Separate earlier #684 and #691 referees are used **only as comparison** in the independent unit tests.

The pure ordinary no-clone combinatorial test independently enumerates all \(2^{12}=4096\) labeled bipartite 3×4 graphs times all seven possible nonempty left heavy R subsets, or **28,672 exact finite instances**, to verify the exact genuine physical-vertex chunk lemma without relying on any symplectic incidence assumptions. These synthetic tiny graphs are algebraic falsifiers only; they never replace the original W32/W34 six-ID physics tests. All external graph constants in the universal expressions are explicitly **formal placeholders**, never certified numeric values. All exact fractions are stored without floating point.

**Strict CI acceptance:** use GitHub-hosted Ubuntu Actions only and enforce \`set -euo pipefail\` with a uniquely parsed machine-readable true-original proof JSON, plus independent permanent replay and mutation/refusal tests. Full INDEX and Research must also pass on the exact final HEAD. No merge or root #230 closure.

## 5. Distinguish established scope from remaining root science

The new **data-adaptive source-heavy SS6 gate and robust heavy-branch theorem** are rigorous given the published graph theorem (for its actual existential C,c); the proof is self-contained beyond the source model, the published theorem, and established #659/#684 original spectral Caro–Wei source lemma. The full universal root claim #230 requires ALSO an independently accepted low-tail case with selected original dense core, proper three-path completion, source collinearity and all four mixed FULL/CORE blockers, and the exact ORIGINAL six-ID lifting across the seven positive classes. Earlier #672/#674 low-tail Drafts have computationally audited internal source/physical interfaces, but that is **not equivalent to independent mathematical acceptance of the entire all-h theorem**.

Do not claim that numerical small W32/W34 executions satisfy SS6 with its unknown *actual* constants. Do not replace unknown published C,c with 1. The next most important research step after this robust heavy-branch source proof is to combine the sharper T with an independently re-proven original low-tail incidence-spectral bound, or find a counterexample in the actual core/proper-path six-ID lift. The root remains **OPEN_WITH_FORMAL_BLOCKER**.
