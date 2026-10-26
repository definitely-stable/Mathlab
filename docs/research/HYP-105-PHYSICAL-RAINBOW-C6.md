# HYP-105 / #230 — AA4-RC6: physical squarefree six-cycle bridge

**Status: all-h exact D6 identity plus finite independent source-ID tests.**
Root #230 stays OPEN_WITH_FORMAL_BLOCKER; no all-h universal D6 floor, seven-class floor, or ASET power.

## 1. Prior work and model

Prior Mathlab G5-E2-B3.2 already counts D6 by joining physical point C6s with six original line flags having the same named-column C6. AA4-RC6 is a **different single physical corner graph representation**, not an invention of the D6 criterion or its previously calculated GF5 weight. The preceding PR #651 constructed a restricted family with large five-ID collision noise AND many accepted D6 motifs; its counterexample invalidates the unrestricted five-ID variance shortcut, not root Branch A/B.

For \(s=2^h\), \(h\ge1\), let the true original symplectic generalized quadrangle \(W(3,s)\) have \(V=(s+1)(s^2+1)\) points and lines, incidence matrix \(M\), and minimal physical alphabet \(a=\min\{k:\binom k2\ge V\}\). Fix **arbitrary correlated complete separately globally injective** pair-label maps \(f\) and \(g\). Build the undirected physical corner graph \(H(f,g)\) with vertices \((u,x)\in[a]^2\): every TRUE original incidence flag \((p,l)\) with \(f(p)=\{u,v\}\), \(g(l)=\{x,y\}\) contributes physical edges \((u,x)-(v,y)\) and \((u,y)-(v,x)\). Separate global injection makes the physical graph simple; each physical edge determines one unique genuine original source flag ID.

The physical adjacency is exactly

\[
A_{(u,x),(v,y)}=
\begin{cases}
 M_{f^{-1}(\{u,v\}),g^{-1}(\{x,y\})},&
 u\ne v,\ x\ne y,\ \text{both inverse labels occupied};\\
 0,&\text{otherwise}.
\end{cases}
\]

## 2. All-h exact rainbow-C6 / D6 bijection

A physical undirected simple six-cycle \(C=(v_0,\ldots,v_5)\), \(v_i=(x_i,y_i)\), is **coordinate-rainbow** when its six first coordinates are all distinct AND its six second coordinates are all distinct.

**Theorem.** The unoriented, unrooted physical coordinate-rainbow C6s of \(H\) are in one-to-one correspondence with the historical accepted ORIGINAL six-incidence D6 sets: six distinct original source point IDs and original line IDs, physically projected to connected simple C6s on each side with identical **named-column adjacency**.

*Proof, physical to original.* Each physical edge has a unique TRUE original source flag \((p_i,l_i)\). As the first-coordinate vertices form a simple C6, their six coordinate-pair edges are distinct, and global \(f\)-injectivity gives six different \(p_i\). The second-coordinate C6 similarly gives six different \(l_i\). Original flag IDs are all different. The two half physical coordinate cycles have the **same adjacency order on the six source flags**, precisely the D6 accepted classifier. There is no source-free fake flag: every physical adjacency was inserted only from true original incidence.

*Proof, original to physical.* Given an accepted original D6 sixset, its named-column dual is a connected C6. Its unique cycle order up to dihedral symmetry fixes each neighboring shared point-coordinate and line-coordinate of consecutive flags. These two coordinates form one physical corner. Each source flag creates exactly the physical corner edge between its preceding and succeeding shared-coordinate corners, and the six corners are distinct in each coordinate. Reversing or rotating this construction does not change the unoriented physical C6. Original source sixsets cannot be counted twice, because the named-column adjacency C6 and its coordinate intersections uniquely reconstruct the same physical cycle. This establishes the bijection.

## 3. Exact squarefree cyclic trace

For \(v_6=v_0\) define

\[
\operatorname{Tr}^{\rm sf}_6(A)=
\sum_{\substack{v_0,\ldots,v_5\in[a]^2\\
|\{x_0,\ldots,x_5\}|=6\\
|\{y_0,\ldots,y_5\}|=6}}
\prod_{i=0}^{5}A_{v_i,v_{i+1}}.
\]

Each undirected unrooted rainbow C6 contributes exactly six starting corners times two traversal directions. Thus, **for all dyadic h and every allowed correlated f,g**,

\[
\boxed{\operatorname{Tr}^{\rm sf}_6(A)=12D_6(f,g).}
\]

Let \(C_6(H)\) be all ordinary unoriented undirected SIMPLE six-cycles of \(H\), and \(\operatorname{Defect}_6(H)\) count the simple six-cycles that repeat at least one coordinate on either side. Then exactly

\[
\boxed{D_6(f,g)=C_6(H)-\operatorname{Defect}_6(H).}
\]

**Crucial non-transfer:** original W(3,s) has bipartite source incidence girth eight, but physical H need not have girth eight. H can have TRIANGLES because consecutive physical edges may be supported by source flags that share no original factor ID. Hence raw adjacency trace, or the nonbacktracking closed-walk trace, is NOT the squarefree six-cycle trace; twice traversing a physical triangle already gives a nonbacktracking length-six closed walk. No unverified spectral positivity may be promoted into a D6 lower bound.

## 4. Independent exact original-source finite checks

An independent physical-graph oracle reconstructs H from true original symplectic GF(2)/GF(4) flags, rather than the established **left physical C6 + right original incidence join**. It enumerates each unoriented simple physical C6 exactly once by requiring its smallest corner first and its smaller adjacent corner second. Each rainbow cycle is mapped back to its six distinct original source flag IDs, point IDs and line IDs. The sixset is checked exactly once and verified with the accepted GF5 D6 classifier. Existing independent left/right join agrees at W(3,2), and a separately implemented finite-field oracle supplies the frozen table.

| Genuine fixed injected map | H triangles | All physical simple C6 | Accepted D6 (both coordinates injective) | Coordinate-repeat defect | x-injective C6 | y-injective C6 |
|---|---:|---:|---:|---:|---:|---:|
| W(3,2), lex K6 | 20 | 730 | 15 | 715 | 78 | 87 |
| W(3,2), reverse-line K6 | 25 | 485 | 3 | 482 | 44 | 50 |
| W(3,4), explicit adversarial K14 | 87 | 30306 | 4972 | 25334 | 12700 | 13193 |

These are exact finite certificates, NOT asymptotic estimates of the defect density. In particular, W(3,2) lex has only 15 accepted D6 among 730 physical simple C6, so counting all C6 is a very loose surrogate.

## 5. Boundary and next theorem

The new model exactly removes irrelevant five-original-flag noise from the D6 target. It does NOT show the rainbow trace is always \(\Omega(s^6)\), or that all seven GF5 accepted classes sum to \(\Omega(s^6)\). The original seven-class problem may involve same-map compensation from the other six accepted classes when D6 is small.

A next P0 phase should either derive a universal lower bound on the squarefree physical trace (which may fail), or identify a **genuine original-sixset, same-fixed-map compensation** inequality accounting for all accepted GF5 classes. Any bound on raw C6(H) requires a simultaneous upper bound on coordinate-repeat defect; such a bound is not supplied. Keep the scientific PR Draft and require both exact-head hosted CI and an independent qualified mathematical referee.
