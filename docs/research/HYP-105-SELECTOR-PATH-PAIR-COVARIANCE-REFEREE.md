# HYP-105 / #230 — AA4-PAIRSEL: exact JOINT source-path selector, signed covariance and independent Jensen referee

**Scientific Draft**, stacked STRICTLY on frozen [#694](https://github.com/definitely-stable/Mathlab/pull/694) HEAD `29bea5e052cd296fcf92fe545ae4bf367ed3e975`. No ancestor/main modifications, scientific mergers, root acceptance, new ASET theorem or external-qualified referee claims. Fix the genuine complete original W(3,2^h), **the same** separately globally injected but arbitrarily correlated physical point/line f,g into minimal K_a pair labels, the same ORIGINAL core source incidence flag IDs, BOTH physical diagonals for each retained flag and the same random flag-priority/bichromatic typed-coordinate selection of [#679](https://github.com/definitely-stable/Mathlab/pull/679).

## 1. Precise prior frontier and error being excluded

[#679](https://github.com/definitely-stable/Mathlab/pull/679) correctly proves that if ORIGINAL source flags in one coordinate-proper physical r-path, r∈{2,3}, are pairwise nonconflicting in the ORIGINAL source conflict graph of max degree K, then

\[
\boxed{
\Pr(\text{one fixed true ORIGINAL physical r-path survives})
\ge 4^{-r}(K+1)^{-r}.
}\tag{PAIR-ONE}
\]

Its proof uses the exact random-priority integral and the fact that on each side the r physical edge labels form a path on r+1 DIFFERENT physical coordinates, hence both typed binary cuts survive with probability exactly 4^{-r}. The source-priority local-minimum events of pairwise NONADJACENT original flags are positively correlated. **This does not imply that TWO different physical paths have positive covariance**: the UNION of their source flag ID sets can contain original conflicts, or their union of physical typed pair-label parity constraints can have odd cycles, even though each individual path has full positive survival probability. We now prove the exact pair law and its precise second-moment consequence without claiming stronger assumptions.

## 2. All-graph exact source-priority union law, including incompatible flags

Let H_src be ANY finite undirected simple conflict graph of ORIGINAL incidence flag IDs I. Let P and Q be coordinate-proper actual physical r-path witnesses, each using exactly r different original flag IDs whose original physical edge labels match BOTH f and g, and whose own flag sets are pairwise independent in H_src. Let

\[
T=S_P\cup S_Q\subset I,
\qquad 1\le|T|\le 2r.
\]

If ANY two original source flags in T are adjacent in H_src, then they cannot both be local minima under ANY strict priority ordering, and

\[
\boxed{\Pr(T\text{ all priority-selected})=0.}\tag{PAIR-PRIO0}
\]

If T is source-conflict-independent, let N(T) be its distinct external neighbors. Assign independent continuous uniform priorities U_i to all ORIGINAL source flags. Condition on `t_i=U_i`, i∈T. Each distinct neighbor w must be later than EVERY selected target neighbor of w. Since other priorities are independent, exactly

\[
\boxed{
\Pi_{\rm prio}(T)
=\int_{[0,1]^{|T|}}
\prod_{w\in N(T)}
\left(1-\max_{i\in T\cap N(w)}t_i\right)\,d\mathbf t.
}\tag{PAIR-PRIO}
\]

As in #679 but **for unions of TWO path ID sets**, this can be evaluated exactly as a sum of at most (2r)! rational simplex terms: for each ordering π of T, let n_j(π) count distinct external source neighbors w whose last target neighbor is π(j). Then

\[
\Pi_{\rm prio}(T)
=\sum_{\pi\in S_{|T|}}
\prod_{j=0}^{|T|-1}
\frac1{\sum_{k=j}^{|T|-1}(n_k(\pi)+1)}.
\tag{PAIR-RATIONAL}
\]

For each independent T this is ≥\(\prod_{i\in T}(d_i+1)^{-1}\), but that is a statement about the **UNION**, not positive association of complete path events. If the union contains a single actual source conflict, probability is exactly zero irrespective of its two positive single-path marginals. This is a deterministic logical distinction, not a random f/g assumption.

## 3. NEW all-graph exact typed color-CSP law; can vanish on odd cycles

For the SAME union T of ACTUAL selected source flag IDs, consider on the left physical coordinate alphabet the graph \(F_T\) with edges \(f(p_i)\), i∈T (duplicates collapse). Dually, on the right physical alphabet take \(G_T\) with edges \(g(\ell_i)\), i∈T. Each selected ORIGINAL flag remains with BOTH opposite-corner physical diagonals iff both its left and right pair edges are bichromatic. These two families of vertex-bit constraints are independent of source priorities and mutually independent between typed alphabets.

**Exact elementary graph-color theorem:** for ANY finite undirected simple parity-constraint graph F with n_F used vertices and c_F connected components, if F is bipartite each component has exactly two alternating binary colorings; among all 2^{n_F} independent bits, the probability is exactly 2^{c_F-n_F}. If F contains an ODD cycle, the probability is zero. Thus set

\[
\chi(F)=
\begin{cases}
2^{c_F-n_F},& F\text{ is bipartite},\\
0,& F\text{ is not bipartite}.
\end{cases}
\tag{PAIR-CSP}
\]

The overall law is the exact PRODUCT of the three INDEPENDENT random sources—original source priorities, left physical coordinate colors, right physical coordinate colors:

\[
\boxed{
\Pr(P,Q\text{ BOTH survive})
=\Pi_{\rm prio}(S_P\cup S_Q)
\,\chi(F_{S_P\cup S_Q})
\,\chi(G_{S_P\cup S_Q}).
}\tag{PAIR-EXACT}
\]

The two paths may share original source flags, physical coordinate symbols or a subpath, as well as distinct endpoints. No pair-path independence or positive association is asserted. This is an all-h **analytical combinatorial identity** because the selector is the same fixed W(3,s) original-source construction; finite W32/W34 tests serve only as falsifiers.

### Source-native covariance can be NEGATIVE, even though #679 is correct

The exact covariance is
\[
\operatorname{Cov}({\bf1}_P,{\bf1}_Q)
=\Pr(P,Q\text{ both})-\Pr(P)\Pr(Q).
\tag{PAIR-COV}
\]

The generic legal typed-source toy with three distinct original matching IDs (0,0),(1,1),(2,2), typed left labels f={(0,1),(1,2),(0,2)}, and right labels g={(0,1),(1,2),(2,3)}, supports individually proper physical 2-paths

\[
P:(0,0)\to(1,1)\to(2,2),\quad
Q:(1,1)\to(2,2)\to(0,3).
\]

Their source conflict graph is empty, so priority union probability is ONE. Each physical path independently survives both cuts with exact probability 1/16. But their union left physical pair labels is a TRIANGLE, whose edge-bichromatic binary coloring is impossible: \(\chi(F_T)=0\). Hence

\[
\boxed{
\Pr(P\cap Q)=0,\quad
\Pr(P)=\Pr(Q)=1/16,\quad
\operatorname{Cov}=-1/256.
}\tag{PAIR-NEG}
\]

A separate four-ID toy witnesses zero joint survival because the UNION has real original conflicts although the typed physical parity constraints are satisfiable. These are **local graph/source selector witnesses**, not claims that these small matching toy flags comprise a complete symplectic W(3,s) geometry or disprove root #230.

Positive pair covariance is equally possible: taking two different proper 2-paths with shared endpoints through the two arms of a typed physical four-cycle, the single marginals are each 1/16 but joint survival is 1/64, so covariance=3/256>0. Thus **neither an all-positive nor an all-negative assumption about path pair survival is justified**. For the actual full true W(3,s) source, the exact (PAIR-EXACT) handles every allowed pair, without importing such generalization.

## 4. NEW independent exact second-moment transfer, no path independence

Fix a core H0 from ACTUAL ORIGINAL source flag IDs, and ordered physical endpoints (u,v). Let \(\mathcal P_r(u,v)\) be ANY chosen nonempty family of distinct actual coordinate-proper directed r-paths in the SAME original core with those endpoints. For the original source-priority and typed-cut random selector let \(X_{uv}\) be the number of these particular physical paths that actually survive, counted with ORIGINAL source IDs. Define

\[
\begin{aligned}
\mu_{uv}&=\mathbb E X_{uv}
=\sum_{P\in\mathcal P_r(u,v)}\Pr(P),\\
M_{uv}&=\mathbb E X_{uv}^{2}
=\sum_{P,Q\in\mathcal P_r(u,v)}\Pr(P,Q).
\end{aligned}
\tag{PAIR-MOM}
\]

Both quantities are *exact rational numbers* using (PAIR-EXACT), not iid-binomial approximations. Since \(X_{uv}\ge0\),

\[
\boxed{
\mu_{uv}^2\le M_{uv}
\le\mathbb E[(A_G^r)_{uv}^2].
}\tag{PAIR-JENSEN}
\]

The first inequality is exact nonnegative variance. The second is a **pointwise** inequality: selected proper paths are a SUBSET of ALL selected physical r-walks, and no multiple provenance edge is invented because the original physical pair maps are globally injected and each retained ID contributes both diagonals. Summing over all ordered physical endpoint cells,

\[
\sum_{u,v}\mu_{uv}^2
\le\sum_{u,v}M_{uv}
\le\mathbb E\operatorname{tr}(A_G^{2r}).
\tag{PAIR-TRACE}
\]

For the complete actual proper path family of H0 and r∈{2,3}, #679 proves \(\mu_{uv}\ge\sigma_rP_r(u,v)\) with \(\sigma_r=4^{-r}(K+1)^{-r}\). Hence

\[
\boxed{
\sigma_r^2\|P_r\|_F^2
\le\sum_{u,v}\mu_{uv}^2
\le\sum_{u,v}M_{uv}
\le\mathbb E\mathrm{tr}(A_G^{2r}).
}\tag{PAIR-TRANSFER}
\]

The established #679 and #686 moment-transfer bound is recovered exactly, now with a **new explicit pair-probability reason** why Jensen is the correct approach: complete path indicators are NOT in general positively associated, so replacing it with product formulas for arbitrary path pairs would be invalid. The exact \(\mu\) and \(M\) allow stronger *embedding-specific*, not uniform-in-h, certificates for chosen path subfamilies, without any randomization of f,g, claim of universal exponent gain, or external SS6 calculation.

An EXACT local two-path control illustrates (PAIR-MOM): for physical 2-paths (0,0)→(1,1)→(3,3) and (0,0)→(2,2)→(3,3) with four source-independent original matching IDs, both have probability 1/16, joint=1/64, and
\[
\mu=1/8,\qquad M=5/32,\qquad\operatorname{Var}X=9/64>0.
\]
Again this generic toy is NOT a fabricated W(3,s) geometry.

## 5. Two independent finite falsifiers and limits

The NEW standalone `research/hyp105_selector_path_pair_covariance_referee.py` is independent of #679's exact priority function, original source path test implementation, parent six-walk/endpoint oracles and GF5 classifier. It:

1. recomputes EXACT rational priority union survival from source-conflict graph as r!-simplex integrals for up to SIX selected ORIGINAL IDs, returning zero when their union conflicts;
2. computes the exact 2-color **parity CSP** by graph traversal and component counting; rejects odd cycles without assuming parity constraints independent;
3. validates each individual physically coordinate-proper 2/3 path against its three/four actual physical vertex coordinates and the **SAME** original incidence IDs which own its physical edges on BOTH f/g sides, not just factor-index projections;
4. computes pair joint survival, individual marginals and signed covariance; independently counts exact \(\mu\), \(M\), variance and Jensen for two or more different proper paths with the SAME ordered endpoints;
5. independently constructs TRUE original symplectic W(3,2)/W(3,4) source conflict graphs via ACTUAL point/line pencil flag pairs, builds BOTH original diagonals into the physical graph, enumerates actual coordinate-proper physical paths and checks exact pair law and the original uniform #679 one-path sigma floor.

The NEW tests (a) compare source priority integrals against independently enumerated **all strict permutations** for ALL 64 labeled 4-vertex source conflict graphs and every nonempty target subset (960 cases), including conflicting unions; (b) compare 2-color CSP against complete binary assignment enumeration for ALL 1024 simple five-coordinate parity graphs; (c) construct separate exact POSITIVE and NEGATIVE path-pair covariance witnesses, the incompatible-source union and odd-typed-parity failure modes; (d) verify exact two-path Jensen mean=1/8, second moment=5/32 and variance=9/64; (e) check actual TRUE W32 full sources under several globally injected, fully correlated typed right maps and true W34 full/sparse source cores, both r=2 and 3, with real original flag IDs and both diagonals. Malformed graphs, source IDs, path corners or pair maps fail closed.

**Scope/STOP:** These are all-finite probability/graph identities with an analytical all-h source application; **not** an independent proof of root original HYP-105 Branch A, external balanced ordinary C6 supersaturation, entire original gf5 class/colored-flow statement, R2/R3 exponent upper, or qualified third-party mathematics referee. All source f,g remain arbitrary fixed maps. No changes/merges to scientific ancestor Draft PRs or main; keep #230 OPEN_WITH_FORMAL_BLOCKER.

**Next most meaningful step:** independent professional/extremal-graph peer review of ALL full-root original source steps #659/#672–#695, or construction of concrete adversarial fixed f,g W(3,2^h) cases that challenge the population lower rather than assuming arbitrary path indicators independent. Neither #679 nor this exact pair-covariance refinement justifies closing the root issue without that review.
