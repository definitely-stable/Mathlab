# HYP-105 / #230 — AA4-PTK: all-h pair-codegree transversality kernel

**Status:** exact deterministic all-h counting identity and two nontrivial source-safe lower-bound certificates for accepted ORIGINAL six-incidence GF(5) D6 motifs. Finite independent symplectic W(3,2)/W(3,4) tests. This slice does **not** prove the root seven-class bound or a universal D6 lower bound. Root remains OPEN_WITH_FORMAL_BLOCKER.

## 1. Research frontier and prerequisites

PR #652 proved that coordinate-rainbow physical six-cycles of H(f,g) biject with original six-flag GF(5)-accepted D6. PR #657 (AA4-PC3) proved a **complete**, rather than K3,3-only, exact identity:

\[
2D_6(f,g)=\sum_U \mathcal T(A_U,B_U,C_U).
\]

The sum runs over unordered, coordinate-injective triples U=(h0<h1<h2) of physical corners in H. The three sets are the **pairwise** physical common-neighbor sets for (h0,h1), (h1,h2) and (h0,h2), filtered to exclude every coordinate occupied by a hub in U. All six physical edges in a transversal witness arise from genuine original point–line incidence flags of W(3,s), s=2^h, with full separately globally injected typed f/g and arbitrary correlation. A transversal triple of one corner from each set produces an accepted original D6 physical cycle. Each D6 has exactly two alternating hub-triple representations.

Previously the transversality count required enumerating all triples of pair-neighbor corners. A high raw pair-codegree product is not a D6 count because many corners can collide on physical first/second coordinates. The new all-h results give (a) an **exact quadratic-time** formula, (b) an exact raw-minus-coordinate-collision decomposition, (c) deterministic lower certificates that do not require a full physical K3,3.

## 2. Exact three-list kernel

For an arbitrary set of typed physical corners X, let

\[
d_X^x(i)=|\{(i,j)\in X\}|,\qquad
d_X^y(j)=|\{(i,j)\in X\}|.
\]

Take arbitrary finite A,B,C. Given a∈A and b∈B with a_x≠b_x and a_y≠b_y, put

\[
\begin{aligned}
R_C(a,b)={}&|C|-d_C^x(a_x)-d_C^x(b_x)-d_C^y(a_y)-d_C^y(b_y)\\
&+\sum_{i\in\{a_x,b_x\}}\sum_{j\in\{a_y,b_y\}}\mathbf1_{(i,j)\in C}.
\end{aligned}
\]

**Theorem (all-h, actually any finite typed coordinate sets).**

\[
\boxed{
\mathcal T(A,B,C)=
\sum_{\substack{a\in A,\ b\in B\\a_x\ne b_x,\ a_y\ne b_y}}R_C(a,b).
}
\]

*Proof.* A possible c∈C is prohibited if it lies in one of the two first-coordinate stars of a,b or one of their two second-coordinate stars. The two first stars are disjoint, as are the two second stars. The four cross-axis intersections consist of exactly the four possible physical corners (a_x,a_y), (a_x,b_y), (b_x,a_y), (b_x,b_y). Inclusion-exclusion gives precisely R_C(a,b), proving the theorem.

With precomputed x/y degree dictionaries and O(1) membership lookup in C, evaluating the entire sum takes **O(|A||B|+|C|)** operations, compared with cubic enumeration. The result is exact integer arithmetic and retains all necessary coordinate transversality, not an approximate probabilistic estimate.

## 3. Pairwise coordinate collision energy and exact loss

For any two such sets define

\[
E(A,B)=\sum_i d_A^x(i)d_B^x(i)+
\sum_j d_A^y(j)d_B^y(j)-|A\cap B|.
\]

This is **exactly** the number of cross-list pairs (a,b) sharing x OR y. The intersection correction matters: the same physical corner in both lists collides on both axes but is only one pair.

Define the raw product P(A,B,C)=|A||B||C| and exact coordinate-conflict loss L=P−T. Then the previous original-source D6 identity implies the all-h conservation formula

\[
\boxed{
2D_6(f,g)=
\sum_U |A_U||B_U||C_U|
-\sum_U \big(|A_U||B_U||C_U|-\mathcal T(A_U,B_U,C_U)\big).
}
\]

The raw products count actual triple choices among genuine physical pair-common-neighbor sets; only the second, coordinate-transverse remainder represents accepted ORIGINAL D6 motifs. Neither source graph girth transfer nor independence of f and g is used.

## 4. Universal deterministic lower certificates

Let a=|A|, b=|B|, c=|C|. By a union bound on the **three inter-list pair collision events**:

\[
\boxed{
\mathcal T(A,B,C)\ge
L_{\rm union}:=
[abc-cE(A,B)-bE(A,C)-aE(B,C)]_+.
}
\]

For a second independent lower bound, let Δ_C^x=max_i d_C^x(i), Δ_C^y=max_j d_C^y(j), or zero for the empty list. Exactly ab−E(A,B) admissible (a,b) pairs exist. Each such pair forbids at most two first-coordinate stars and two second-coordinate stars of C. Therefore

\[
\boxed{
\mathcal T(A,B,C)\ge
(ab-E(A,B))[c-2(\Delta_C^x+\Delta_C^y)]_+.
}
\]

Apply this also to AC|B and BC|A. The maximum L_* of the union bound and these three sequential bounds is a rigorous all-h integer lower certificate. Therefore, for any true source symplectic W(3,s) and **every fixed admissible correlated full injection f,g**,

\[
\boxed{
D_6(f,g)\ge\frac12\sum_U
\max\{L_{\rm union}(U),L_{\rm seq}^{AB|C}(U),
L_{\rm seq}^{AC|B}(U),L_{\rm seq}^{BC|A}(U)\}.
}
\]

This holds without requiring any triple-common neighbor: pairwise intersections of physical neighborhoods suffice. No universal positive value is asserted for the right-hand side.

## 5. Genuine-original-source independent finite falsifiers

The finite oracle rebuilds the physical graph only from TRUE symplectic source flags. It independently indexes all pair-common-neighbor sets, applies the **quadratic** kernel, checks exact raw-loss conservation and the lower bounds per hub triple, and compares with the **different original-source sixflag/ historical seven-family GF(5) oracle** in #657 and the independent full physical-rainbow-C6 oracle in #652.

The accepted counts, independently frozen in the earlier source verification, are:

| True original map | Oriented accepted triple witnesses | Original GF(5) D6 | Full physical K3,3 supported D6 |
|---|---:|---:|---:|
| W(3,2) lex K6 | 30 | 15 | 6 |
| W(3,2) reverse-line K6 | 6 | 3 | 0 |
| W(3,4) adversarial full K14 | 9944 | 4972 | 0 |

Other tests cover a true-original W(3,4) 16-flag matching realized as a 4-hub × 4-free physical grid (at least 96 accepted D6), exact pairwise overlap correction, no-transversality examples with raw product 729, independent direct cubic enumeration under all list permutations on small abstract **algebraic** examples, complete typed coordinate relabeling, and malformed-source fail-closed cases.

**Critical boundary:** a raw product of three pair-codegrees may be arbitrarily large while T is exactly zero, for example when all three lists lie in one common first-coordinate star. Likewise the two inexpensive lower certificates may be zero although T itself is positive. Neither raw energy nor these certificates alone proves D6=Ω(s^6).

## 6. Next formal mathematical gate

Quantify the **cumulative positive transversality certificate** ∑_U L_*(U), or prove a same-fixed-map compensation statement for other original accepted GF(5) sixflag families when D6 transversality is sparse. The packet-concentrated maps from PR #651 and the adversarial original W(3,4) certificate are mandatory falsifiers for any conjectured all-map estimate.

The new exact kernel and the lower bounds are elementary, unconditional combinatorial facts **for every finite typed coordinate set**; only interpreting T as accepted original D6 depends on the original-source bijection from #652 and the double-cover identity from #657. This work does not depend on the infinite paired-subfield existence proof in #651. Keep the scientific PR Draft, exact-head hosted CI, independent proof referee and issue #230 status OPEN_WITH_FORMAL_BLOCKER. Do not merge directly into main.
