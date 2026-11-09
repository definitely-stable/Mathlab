# HYP-105 / Issue #230 — AA4-CLIQUE: all-h incompatible ORIGINAL physical P3 pair weight via endpoint-conditioned source selector and weighted Motzkin–Straus

**Scientific scope:** strict child of [Draft PR #754](https://github.com/definitely-stable/Mathlab/pull/754), frozen parent HEAD e1333191a5c263fba2b9a4d6bedbfde641e2b5d4. The parent finished specialist, INDEX and **full Research SUCCESS** at that HEAD. This slice supplies a NEW substantially better *universal* bound on the weighted incompatible same-endpoint physical original proper-P3 pair mass \(B\), building on the already proved all-h Harris original source priority selector. It gives two other independent typed physical/source conflict bounds, complete independent real-original W32 instance-level graph and weight audits and a direct abstract weighted-graph falsifier. This is a mathematical advance but does NOT itself prove the target \(B/M<3/4\), a fourfold global sixth-moment gain, all remaining original HEAVY/LOW/GF5 lemmas or a new ASET exponent. All PRs remain Draft; main, original issue #230 and previous parents untouched, status OPEN_WITH_FORMAL_BLOCKER.

## 1. True original source, quantifiers and graph whose edge weights we must bound

For EVERY dyadic \(s=2^h\) and original symplectic generalized quadrangle \(W(3,s)\) with named ORIGINAL point–line incidence flags \(I\), take any fixed maps

\[
f:P\hookrightarrow\binom{[a]}2,\qquad g:L\hookrightarrow\binom{[a]}2
\]

that are separately complete globally pair-injective and arbitrarily mutually correlated. Delete any adversarial set \(Z\) of named ORIGINAL source IDs. Take any paired retained CORE \(C\subseteq I\setminus Z\) whose original source point/line pencil conflict graph \(J_C\) has maximum degree at most \(K=64\) (as independently constructed in the LOW branch). Each flag retains **BOTH actual physical opposite rectangle diagonals as one original source owner**; no cloned, invented or unowned physical edge is permitted.

Fix ONE uniform random global ORIGINAL source-priority order and two independent fair binary physical-coordinate symbol colorings. A source flag is kept when it is a strict local source-priority minimum among its actual J-neighbors and both its actual original fixed f/g label pairs cross their respective typed color cuts. This preserves both physical diagonals together.

For any ordered physical endpoints \(u=(x_0,y_0)\), \(v=(x_3,y_3)\), let \(\Gamma_{uv}\) denote the set of actual directed **coordinate-proper** physical length-three CORE paths

\[
\gamma=(u,(x_1,y_1),(x_2,y_2),v),
\]

where all four first and all four second physical coordinate symbols are distinct. Each such path has exactly three pairwise J-independent actual original source owner flags; its selection marginal \(p_\gamma\) is strictly positive, and by #754's fully proved all-h original Harris local-priority product and typed cuts,

\[
p_\gamma\ge\sigma_3:=\frac1{64(K+1)^3}.
\tag{CL-1}
\]

Each endpoint bin is finite; empty bins contribute zero. Define its total probability mass \(W_{uv}=\sum_{\gamma\in\Gamma_{uv}}p_\gamma\) and \(M_{uv}:=W_{uv}^2\). Let the **original incompatible path graph** \(Q_{uv}\) have one vertex per actual directed physical path \(\gamma\in\Gamma_{uv}\). Two distinct paths are adjacent precisely if they cannot both survive under the one shared source selector: some named ORIGINAL source owner of \(\gamma\) has a genuine J conflict with a named original owner of \(\eta\), or their first or second typed physical label-edge unions have an odd cycle. By #753's all-h original parity criterion, that latter alternative is **equivalent** to at least one of four actual inner symbol equalities

\[
x_1^\gamma=x_2^\eta,\ x_2^\gamma=x_1^\eta,\
y_1^\gamma=y_2^\eta,\ y_2^\gamma=y_1^\eta.
\tag{CL-2}
\]

This uses **true original physical paths with the SAME ordered physical endpoints**, not arbitrary sixsets, earlier historical path projections, or a synthetic product of f/g choices. The factor union bipartiteness is necessary and sufficient for two paths' typed color events to coexist, and a J-free union is necessary and sufficient for a simultaneous priority-rank local-minimum assignment to have positive probability. Thus graph adjacency means **exactly zero joint path survival probability**.

With path vertex weights \(w_\gamma=p_\gamma>0\), define

\[
\begin{aligned}
G_{uv}&=\sum_{\gamma,\eta\in\Gamma_{uv}:\
(\gamma=\eta\ {\rm or}\ \{\gamma,\eta\}\notin E(Q_{uv}))}
 w_\gamma w_\eta,\\
B_{uv}&=2\sum_{\{\gamma,\eta\}\in E(Q_{uv})}w_\gamma w_\eta,\qquad
M_{uv}=G_{uv}+B_{uv}=W_{uv}^2.
\end{aligned}
\tag{CL-3}
\]

Sum over all actual physical ordered endpoint bins to obtain \(G,B,M=G+B=\|\mathbb EX_3\|_F^2\). This is **exact source marginal-product weight**, not the selected endpoint path-pair joint probability or the six-motif count.

## 2. NEW ALL-h clique-size bound through endpoint-conditioned actual ORIGINAL selector

The crucial observation is that **fixing the actual two endpoints of a path** allows a fourfold improvement to its retention probability in an auxiliary probability experiment. For each nonempty \(\Gamma_{uv}\), condition the two independent physical binary symbol colorings on

\[
c_x(x_0)=c_y(y_0)=0,\qquad
c_x(x_3)=c_y(y_3)=1.
\tag{CL-4}
\]

The four endpoint symbols \(x_0,x_3,y_0,y_3\) are pairwise distinct **within their typed alphabets** because every path is coordinate proper. The two typed factors are drawn independently even if f,g were fixed and correlated. Conditional on (CL-4), the two **interior** symbols \(x_1,x_2\) of a proper x-path have exactly one admissible alternating fair-bit assignment among \(2^2\). Likewise, the two interior y-symbols give one of \(2^2\). As the ORIGINAL source priority experiment is independent of both typed cuts,

\[
\boxed{\Pr(\gamma\text{ selected}\mid\mathrm{endpoints\ fixed})
=\frac{p_J(S_\gamma)}{16}
=4p_\gamma\ge\frac1{16(K+1)^3}.}
\tag{CL-5}
\]

Here \(p_J(S_\gamma)\) is the **joint actual source-owner** local-minimum rank probability, not a product assumption.

Now choose any clique \(\mathcal C\) of the TRUE incompatibility graph \(Q_{uv}\). In any single realization of the endpoint-conditioned ORIGINAL selector, at most ONE path in \(\mathcal C\) can survive: two surviving real physical paths would have all their original owners retained (which makes their owner union J-independent) and BOTH true physical symbol pair sets bichromatic under a COMMON color choice (which makes both typed unions bipartite). Such a pair would not be adjacent in \(Q_{uv}\), contradiction.

Therefore, pointwise \(\sum_{\gamma\in\mathcal C}\mathbf1_{\gamma\rm\ selected}\le1\). Take expectation **without any path independence**, use (CL-5), and conclude

\[
1\ge\sum_{\gamma\in\mathcal C}\Pr(\gamma\rm\ selected\mid endpoints)
\ge\frac{|\mathcal C|}{16(K+1)^3}.
\]

Thus the exact first NEW all-h theorem is

\[
\boxed{
\omega(Q_{uv})\le Q_\star:=16(K+1)^3
=16\cdot65^3=\mathbf{4\,394\,000}.
}
\tag{CL-6}
\]

This is a source-compatible \(\omega\)-bound for **every** physical endpoint bin and **every** fixed correlated f/g with arbitrary adversarial named Z. It uses only one shared original source experiment, not independent selected paths, any black-box geometric symmetry or any finite-s example.

## 3. NEW elementary weighted Motzkin–Straus theorem, proved rather than assumed

Let \(H\) be an arbitrary finite simple undirected graph of clique number \(k\ge1\), with nonnegative vertex weights \(w_1,\ldots,w_n\) and \(W=\sum_i w_i\). Its weighted edge energy satisfies

\[
\boxed{
2\sum_{\{i,j\}\in E(H)}w_iw_j
\le\left(1-\frac1k\right)W^2.
}
\tag{CL-7}
\]

**Full short proof:** Normalize \(W=1\), discard zero-weight vertices. If two positive-support vertices \(i,j\) are not adjacent, moving ALL their combined weight to i or j changes edge energy **affinely** with the transfer parameter, because \(ij\notin E(H)\). One of the two extreme transfers is nondecreasing, allowing us to eliminate one positive nonadjacent support vertex. Repeat until every pair of positive-support vertices is adjacent, i.e. the support is a clique of size \(m\le k\). On this support,

\[
2\sum_{i<j}w_iw_j
=\left(\sum_iw_i\right)^2-\sum_iw_i^2
\le1-\frac1m
\le1-\frac1k,
\]

where Cauchy gives \(\sum_iw_i^2\ge1/m\). The preceding weight eliminations did not decrease the edge energy, so (CL-7) holds for the ORIGINAL weights. Homogeneity restores arbitrary W. This exact argument is valid for any fractional probability weights and repeated different physical paths.

Apply (CL-7) to the actual true ORIGINAL same-endpoint incompatibility graph \(Q_{uv}\) with weights \(p_\gamma\), and use (CL-6). From (CL-3),

\[
\boxed{
B_{uv}\le\left(1-\frac1{Q_\star}\right)M_{uv},\qquad
G_{uv}\ge\frac1{Q_\star}M_{uv}.
}
\tag{CL-8}
\]

Summing over ALL original physical endpoint bins gives the main NEW all-h result

\[
\boxed{
\begin{aligned}
G&\ge\varepsilon_\star M,\\
B&\le(1-\varepsilon_\star)M,\\
\varepsilon_\star&=\frac1{16\cdot65^3}
=\frac1{\mathbf{4\,394\,000}}.
\end{aligned}
}
\tag{CL-9}
\]

The inherited #754 endpoint-conditioned weighted-Jensen argument gave only \(\varepsilon_{\rm old}=1/(256\cdot65^6)=1/19\,307\,236\,000\,000\). The genuine all-h improvement is the **exact integer factor**

\[
\boxed{
\frac{\varepsilon_\star}{\varepsilon_{\rm old}}
=16\cdot65^3=\mathbf{4\,394\,000}.
}
\tag{CL-10}
\]

Neither the physical six-motif \(\Omega(s^6)\) exponent nor the HEAVY ordinary graph C6 constants have been changed. In particular \(\varepsilon_\star\) remains much smaller than \(1/4\). It is **not** permissible to combine (CL-9) with the #753 \(M\le(L_6/4)s^6+B\) and claim an improvement of the prior ordinary Jensen upper \(M\le L_6s^6\); that would give \(M\le Q_\star L_6s^6/4\), enormously weaker. The directly useful all-h LOW selector q2/q3 improvements in #754 remain intact.

## 4. NEW independent ALL-h typed-coordinate sharp two-thirds inequalities

The structure of the physical typed inner coordinate conflicts yields a separate stronger *single-type* result than the general clique cap.

For each directed proper physical 3path in the same endpoint bin, take only its ordered **first** internal typed coordinate arc \(a_\gamma\to b_\gamma\) where \(a_\gamma=x_1^\gamma\), \(b_\gamma=x_2^\gamma\), with \(a_\gamma\ne b_\gamma\). The first typed incompatibility graph \(Q^x_{uv}\) has an edge between two paths iff

\[
a_\gamma=b_\eta\quad\text{or}\quad b_\gamma=a_\eta.
\]

**All-order clique-three theorem:** Fix any path arc \(a\to b\). Every arc conflicting with it has **tail b** or **head a**. Among arcs sharing tail b there can be no conflicts with each other, because their heads are never b (no self-loops); similarly arcs sharing head a are mutually nonconflicting. Hence a clique containing \(a\to b\) has at most one additional member from each of these two groups. Therefore

\[
\boxed{\omega(Q^x_{uv})\le3.}
\tag{CL-11}
\]

The bound is sharp for the abstract three arcs \(0\to1,\,1\to2,\,2\to0\) (no assertion these arcs automatically form a true ORIGINAL GQ path triple). The same argument independently holds for the second typed physical coordinates and their arcs \(y_1\to y_2\).

Denote by \(B^x_{uv}\) the weighted ordered path pair mass with a first-typed opposite-depth collision, and similarly \(B^y_{uv}\), **without** excluding simultaneous original J conflicts or overlap with the other typed side. By (CL-7) with k≤3,

\[
\boxed{
B^x\le\frac23M,\qquad
B^y\le\frac23M.
}
\tag{CL-12}
\]

These are true all-h quantitative bounds for either individual typed incompatibility source, independent of original f/g mutual correlation, arbitrary Z and the LOW source K. They do not say \(B\le2M/3\): the x, y and J conflict graphs overlap and their union may contain a larger clique. **One must not add** \(B^x+B^y+B^J\) and infer a \(3/4\) bound.

### Independent ORIGINAL J-only clique and weighted conflict bound

There is an analogous but weaker source-only component estimate. Let \(Q^J_{uv}\) have an edge only when the union of two true ORIGINAL path owner sets contains an actual source J conflict. Source selector **without** any typed cuts keeps each proper 3path's owner set with probability at least \((K+1)^{-3}\), by the #754 rigorous all-h Harris local-priority inequality. A clique of \(Q^J_{uv}\) can contain at most one such retained path-owner set under ONE global priority order, because all local source minimum owners form a J-independent set. Exactly the same expectation argument as Section 2 gives

\[
\omega(Q^J_{uv})\le(K+1)^3=65^3=274625.
\]

Apply (CL-7) again to infer

\[
\boxed{B^J\le(1-65^{-3})M.}
\tag{CL-13}
\]

This is a separately quantified source-priority obstruction, NOT a bound on all incompatibility events together. The main checker independently reconstructs this J-only graph and full weighted \(B^J\) on the real source.

## 5. Independent finite original source and weighted-graph falsifiers

The NEW main Python referee imports **ONLY** the independently audited genuine symplectic original W32/W34 source incidence generator from AA4-DEGFACT/#748. It reconstructs independently original complete pair-injective f/g labels in lex, reverse and shifted schemes; original source pencil graph J; actual named Z/paired retained CORE flags and exactly TWO real physical opposite diagonal edges per flag; ALL proper directed physical P3 paths on the full W32 cases; and an independent rational source priority order-statistic integral for all 3 owner sets. It never imports the previous #753/#754 source probability or path-incompatibility implementation. The previous original weighted G/B census appears only in **TEST code** as an independent result cross-check.

For every same ordered physical endpoint family it constructs **FOUR exact simple incompatibility graphs**: combined source J/typed-odd-cycle, only source J, only first typed x-depth collision, only second typed y-depth collision. It computes their exact maximum clique sizes by independent bitset Bron–Kerbosch recursion (not by assuming the all-h bounds) and the exact rational weighted incompatible edge mass. Every endpoint bin is checked against its **own observed** weighted Motzkin cap \(B_{uv}\le(1-1/\omega_{uv})M_{uv}\), both single-type \(2M_{uv}/3\) bounds, source-only \((1-1/65^3)M_{uv}\) cap, and the universal combined \((1-1/4394000)M_{uv}\) cap. Every FIRST/SECOND OR J original path pair classification is direct, not inferred from previous hardcoded numeric result rows.

**Full REAL original W(3,2)** runs: 45 original flags, full lex (90 actual physical edges, all 1346 physical coordinate-proper directed P3s, exactly 4370 ordered same-endpoint pairs), full reverse (90 edges, 1154 paths, 2942 pairs), shifted fixed globally injected labels with 3 named ORIGINAL flags Z17 deleted (84 actual edges, all 838 paths, 1766 pairs). Exact W32 compatible/incompatible original fraction G/M and all three full historical rational G/B totals must agree independently with the frozen predecessor test oracle; no source label averaging. For the genuine W(3,4), 425 actual original flags, source even-pruned and Z17 COREs, three correlated schemes, 2000 **deterministic sampled proper P3 paths** per case; their same-endpoint selected subset is audited without claiming a complete W34 \(M,B,G\) census.

A separate **abstract typed physical factor** falsifier constructs all nonloop internal symbol arcs from five symbols and directly computes true clique number 3, including the sharp simple directed three-cycle. It is clearly labeled a plain graph sanity check, NOT a true GQ source replacement.

A second independent weighted graph oracle exhaustively checks **all 1024 labeled undirected simple graphs on five vertices, times 243 strictly positive integer weight vectors \(w_i\in\{1,2,3\}\)** — a total of **248,832 independently checked exact integer Motzkin inequalities**, with no use of the analytical weight-compression proof inside this test. The finite graphs include cliques of size 1–5 and both strict/equality cases. This is an independent falsification of CL-7, not a replacement for its all-order proof.

Dedicated Github-hosted Ubuntu 24.04 Python 3.12 specialist runs 22 tests and a strict single-line JSON proof artifact, independently of standard INDEX and full Research. At EXACT final PR HEAD all must be checked before treating engineering acceptance as complete.

## 6. Precisely stated result and limitations

**New rigorously proved all-h statements:** (CL-6) global actual original selector-compatible path incompatibility clique number ≤4,394,000, (CL-7) elementary exact weighted graph inequality, (CL-9) universal ORIGINAL same-endpoint incompatible \(B\) fraction at most \(1-1/4,394,000\), (CL-11)/(CL-12) each physical typed opposite-depth collision source has weighted mass ≤2M/3, and (CL-13) original J-only conflict mass ≤(1−65^{-3})M. Every quantifier allows arbitrary fixed correlated globally pair-injective labels, original named deletion Z, and any LOW-admissible paired core.

**Scientifically unaccepted:** a stronger *combined* \(B/M<3/4\) or any uniform fourfold LOW sixth moment improvement; universal proof completion of the independent original HEAVY/LOW/GF5 dependency DAG, numeric published ordinary graph C6 constants, full event union risk or a new ASET extraction exponent. The root remains OPEN_WITH_FORMAL_BLOCKER.

**NEXT meaningful proof gate:** either use true original GQ no-4-cycles, global source injection, low physical degree pruning and/or signed path-flow structure to prove a substantially better upper bound on the TOTAL combined J/x/y incompatibility clique/edge density; or produce a TRUE ORIGINAL fixed f/g adversary with \(B/M\ge3/4\) that disproves this aggressive target. The new separate 2/3 typed bounds indicate the potential but do not permit an invalid union bound. If full repo Research CI is disrupted by GitHub canceled/abandoned shards, record the exact run-level state and distinguish from mathematical specialist success.
