# HYP-105 / #230 — AA4-CG-NOGO: projective-plane obstruction to density-only codegree-clique SS6 replacement

**Scoped mathematical no-go / scientific Draft** stacked strictly on frozen [#691](https://github.com/definitely-stable/Mathlab/pull/691) at exact HEAD `bd7ce49d6f9471fdeeb3071fc5eda79b5d88fba0`. This concerns **arbitrary ordinary simple bipartite graphs**, not a claimed actual original `W(3,2^h)` correlated-map counterexample and NOT a counterexample to root #230 Branch A. No merges/issue closure or third-party scientific acceptance.

## 1. Why this is the mathematically necessary next gate after AA4-CODEGREE

[#691](https://github.com/definitely-stable/Mathlab/pull/691) establishes a genuinely source-free, all-graph **sufficient** local certificate:

\[
\text{if }\min_{\{x,y\}\in\binom{S}{2}}|N(x)\cap N(y)|\ge k\ge3
\quad\Longrightarrow\quad
\#C_6(G)\ge\binom{|S|}{3}k(k-1)(k-2).
\tag{P0}
\]

For an actual coherent original `W(3,2^h)` selected physical graph, these ordinary C6s lift injectively to accepted **six DISTINCT original incidence-ID** D6 sixsets. It is tempting but INVALID to assume that the mere balanced `e(G)>=C*v(G)^(4/3)` density condition from published Jiang–Yepremyan ordinary C6 supersaturation produces such a large-codegree clique. This slice **rigorously falsifies that graph-only inference** by constructing an infinite family with extremely large cycle count but maximum pairwise common-neighbor count EXACTLY ONE.

This is important because root #659/#684 requires a genuine ordinary simple C6 theorem on a balanced chunk whose additional original source structure has not been shown to force codegree cliques. Discarding the external balanced SS6 theorem in favor of (P0) without an additional true original-source lemma would leave a GAP. We explicitly close this false prospective route.

## 2. An explicit infinite family over prime fields

For every prime `p>=2`, let `PG(2,p)` be the projective plane of dimension two over the FINITE FIELD `F_p`. Its points are one-dimensional subspaces of `F_p³`, represented uniquely by nonzero triples normalized so the first nonzero coordinate is 1. Its lines are nonzero normalized covectors `(a,b,c)`; a point `(x,y,z)` lies on a line iff `ax+by+cz=0 mod p`.

The **ordinary undirected bipartite point–line incidence graph** `G_p` is simple, has

\[
n=p^2+p+1\text{ vertices per side},\quad
v(G_p)=2n,\quad
e(G_p)=n(p+1).
\tag{P1}
\]

Every point lies on exactly `p+1` lines. Every TWO DISTINCT points determine exactly ONE original projective line: in homogeneous coordinates, the two linearly independent point vectors span a two-dimensional vector subspace, whose orthogonal dual is one-dimensional. Consequently

\[
\boxed{\forall x\ne y\in X,\quad
|N(x)\cap N(y)|=1.}
\tag{P2}
\]

The same property holds on the line side by duality. In particular, **NO subset** of three or more physical point-side vertices ever satisfies the local `k>=3` condition (P0). The certificate's local floor is zero for every subset, despite huge edge density and many genuine ordinary C6s.

## 3. Exact SIX-CYCLE count, independent of codegree formula

Each **NONCOLLINEAR** unordered triple of projective points `{x,y,z}` determines three distinct joining lines `xy,yz,zx`, hence EXACTLY ONE simple unoriented ordinary six-cycle

\[
x\;--\;\ell_{xy}\;--\;y\;--\;\ell_{yz}\;--\;z\;--\;\ell_{zx}\;--\;x.
\]

Conversely every simple C6 uses three distinct original projective point vertices and three distinct original projective line vertices, which forces the point triple noncollinear; its three intermediate lines are their unique joining lines. Every projective line contains `p+1` points and every collinear triple belongs to EXACTLY ONE projective line. Hence

\[
\boxed{
\#C_6(G_p)=
\binom{p^2+p+1}{3}
-(p^2+p+1)\binom{p+1}{3}.
}\tag{P3}
\]

This is an all-prime integer theorem proved directly from PG2 geometry, not finite extrapolation or the #691 codegree identity. The first finite cases are:

| p | v | e | Exact unoriented ordinary C6 | Maximum pair codegree |
|---|---:|---:|---:|---:|
| 2 | 14 | 21 | 28 | 1 |
| 3 | 26 | 52 | 234 | 1 |
| 5 | 62 | 186 | 3,875 | 1 |
| 7 | 114 | 456 | 26,068 | 1 |

The graph is bipartite, genuinely simple and sparse; these are true ordinary six-cycles, not homomorphism-only closed walks. For p=2,3 the direct independent source-free 6-injective-vertices oracle from #691 also exactly matches (P3).

## 4. Arbitrarily high balanced density with NO codegree clique

The exact normalized balanced-edge density is

\[
\boxed{
\frac{e(G_p)^3}{v(G_p)^4}
=\frac{(p+1)^3}{16(p^2+p+1)}
\ge\frac p{16}.
}\tag{P4}
\]

The last inequality is elementary because

\[
(p+1)^3-p(p^2+p+1)=2p^2+2p+1>0.
\]

Therefore for ANY fixed `C>0`, choose ANY prime `p>=16C³`. Euclid's theorem provides arbitrarily large primes. Then `e(G_p)^3>=C³v(G_p)^4`, i.e.

\[
\boxed{e(G_p)\ge C\,v(G_p)^{4/3},}
\tag{P5}
\]

while (P2) says its maximum point-side AND line-side pair codegree is 1 and it has NO `k>=3` codegree clique whatsoever.

**NO-GO theorem (ALL positive C):** In arbitrary ordinary simple bipartite graphs, neither balanced density at arbitrarily large `C*v^(4/3)` nor positive (indeed polynomially many) ordinary C6s implies existence of ANY three-vertex `k>=3` codegree clique. Hence the local codegree-clique certificate of #691 **cannot, from the graph density premise alone, replace the published balanced six-cycle supersaturation theorem** used in Branch A. It is valuable only when a particular fixed original-selected physical graph furnishes the clique or when an additional new genuine-original-source structural theorem proves it. This NO-GO does NOT refute the published theorem: the projective planes have plenty of C6s, exactly as expected.

## 5. Independent implementation and scope

The new `research/hyp105_codegree_clique_density_nogo.py` implements PG(2,p) from scratch using modular arithmetic on ALL nonzero homogeneous Fp³ triples, canonical projective normalization, all point–line incidences, and source-independent exact graph bitsets. It verifies projective point degrees `p+1`, every distinct point pair codegree EXACTLY ONE, all edges and vertices, and (P4).

A **second mathematically distinct** coefficient oracle uses ONLY the projective noncollinear-point formula (P3); #691's independently derived common-neighbor C6 identity provides a consistency check, and for p=2,3 a third **direct six-injective-vertex** enumeration independently agrees. The new seven unittest groups check p=2,3,5,7,11 exact C6s; arbitrarily large symbolic density bounds for p=17,23,31,53,101 without prohibitive graph enumeration; trial C test values p≥16C³ with **exact rational integer powers**, no float cube-root approximations; source-normalization uniqueness; negative prime, field and C inputs fail closed.

**Critical provenance boundary:** `PG(2,p)` is an abstract point–line ordinary bipartite graph. It is NOT the original source symplectic GQ `W(3,2^h)`, whose incidence structure, globally injected f,g maps and physical graph ownership constraints are different. No claim the projective plane incidence graph is realizable as an actual heavy balanced chunk of some allowed original-source map, hence NO counterexample to #230's all-map `D6+U_BBo=Omega(s^6)`, and NO improvement or deterioration of the full R3 risk exponent. The result refutes **precisely** a proposed extra universal graph-only premise, avoiding invalid promotion of #691's LOCAL certificate.

## 6. Subsequent research prioritization

1. Maintain the **published balanced ordinary C6 supersaturation** input (Jiang–Yepremyan 2020, DOI 10.1017/S0963548320000206) in the universal full-heavy-tail branch until a genuine alternative is rigorously established.
2. The new independent codegree C6 formula from #691 remains useful for exact local C6 counting, independent original D6 provenance audit and source-selected **verified** codegree-clique lower certificates; do not assume these cliques must exist.
3. Next meaningful proof task is an *independent adverse-source audit of the FULL/CORE mixed fourth-moment blocker*, followed by qualified external extremal-combinatorics peer review of the complete original #659/#672–#691 geometry; stop speculative density→clique claims without specific original-source structure.

Root scientific status remains `OPEN_WITH_FORMAL_BLOCKER`. Do not merge parent scientific Drafts, change main, close #230, or label this abstract graph no-go as an original W(3,s) correlated-map counterfamily.
