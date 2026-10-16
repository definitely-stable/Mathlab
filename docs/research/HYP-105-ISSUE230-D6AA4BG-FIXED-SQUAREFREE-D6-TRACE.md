# HYP-105 / #230 — AA4-BG: exact squarefree bicolored trace on EVERY fully fixed genuine-original f,g

**Scientific research Draft; strict child of [AA4-BF #570](https://github.com/definitely-stable/Mathlab/pull/570), pinned parent exact head f0255c0f09da62d8a818247f38ee3aa7ab9b745c.** The root all-seven-GF(5) Branch A/B/C remains OPEN. This is a NEW algebraic squarefree-trace formulation and a finite falsification toolkit for the previously known ORIGINAL D6 colored-rainbow D-edge cycle correspondence [#539](https://github.com/definitely-stable/Mathlab/pull/539), not an invented new D6 lower bound. Crucially this mathematical identity applies to EVERY **already fully fixed** pair f,g without any random global line reassignment, source-line pins, or favorable completion. It is **D6-only**, not equivalent to the root seven-class sum.

## Quantifiers and original data

Fix ANY dyadic s=2^h, h>=1, the ACTUAL symplectic original W(3,s), and ANY two already COMPLETE typed globally injective original physical pair-edge factor maps f,g into E(K_a), where V=(s+1)(s²+1) is the count of true original point factors and true original LINE factors; a is minimal with binom(a,2)>=V. Do not identify source incidence flags under any source symmetry: there are N=V(s+1) TRUE ORIGINAL incidence IDs i=(p_i,l_i), one for each incident original source point and LINE factor.

Let D denote the undirected graph whose VERTICES are all those actual original incidence-flag IDs. For i!=j, D_ij=1 iff p_i!=p_j, l_i!=l_j, and f(p_i),f(p_j) are two DIFFERENT physical pair edges intersecting in exactly one physical point coordinate c(i,j), while g(l_i),g(l_j) intersect in exactly one physical line coordinate e(i,j). Each source adjacency is the authentic AA4-AL D pair from [#539](https://github.com/definitely-stable/Mathlab/pull/539); its two physical coordinate colors (c,e) are uniquely defined. No source fake graph replacement is allowed.

## NEW AA4-BG1: an exact all-h fully fixed-map nilpotent matrix trace identity

Consider the commutative square-zero ring

\[
\mathcal R=\mathbb Z[x_0,\ldots,x_{a-1},y_0,\ldots,y_{a-1}]
          /(x_i^2,\ y_j^2:\ 0\le i,j<a).
\]

The variables x track actual original POINT physical coordinates, and y track original LINE physical coordinates; the two palettes are independent even when their physical integer names coincide. Define the N by N symmetric matrix A over the ring by

\[
A_{ij}=\begin{cases}
x_{c(i,j)}\,y_{e(i,j)}, & D_{ij}=1,\\
0, & D_{ij}=0.
\end{cases}
\]

For six-element subsets P,L of the respective physical coordinate palettes, write \(x_P=\prod_{p\in P}x_p\), \(y_L=\prod_{\ell\in L}y_\ell\). Define \(D6_{P,L}(f,g)\) as the HISTORICAL positive ORIGINAL GF(5) D6 six-distinct-source-incidence class whose point physical 6-cycle uses vertex-coordinate set P and whose line physical 6-cycle uses coordinate set L. Because D6 uses the SAME six ACTUAL original incidence flags on both typed physical sides, this partition is well defined (no source-factor orbit quotient or random maps).

**The exact all-h identity is**

\[
\boxed{
\operatorname{Tr}_{\mathcal R}(A^6)
=12\sum_{\substack{P,L\subseteq\{0,\ldots,a-1\}\\ |P|=|L|=6}}
D6_{P,L}(f,g)\;x_P y_L .
}
\tag{BG-TRACE}
\]

All coefficients are NONNEGATIVE integer multiples of 12. In particular, with the linear functional \(\Lambda(x_P y_L)=1\) for degree-(6,6) squarefree monomials,

\[
\boxed{
S_{D6}(f,g)
=\frac1{12}\Lambda\!\left(\operatorname{Tr}_{\mathcal R}(A^6)\right).
}
\tag{BG-COUNT}
\]

This is an exact finite integral identity for EVERY dyadic h>=1 and EVERY COMPLETELY FIXED correlated source f,g, not merely an expectation or random coordinate relabeling. It provides an exact algebraic certificate for D6=0 (the squarefree trace vanishes), and for D6>0 (at least one coefficient positive). It does NOT prove that trace is uniformly positive for all original full f,g, and it is not a polynomial-time algorithm in high physical-alphabet dimension.

### Proof: expanding the trace and why nilpotence automatically enforces true ORIGINAL six-ID distinctness

Expand \(\operatorname{Tr}A^6\) as a sum over ALL directed rooted CLOSED length-six walks \((i_0,i_1,\ldots,i_5,i_6=i_0)\) of the actual ORIGINAL D graph, with one monomial \(x_{c(i_j,i_{j+1})}y_{e(i_j,i_{j+1})}\) per original D edge. There is NO assumption or explicit requirement that the six intermediate source vertices are different. The square-zero relations erase every walk that repeats ANY point physical shared coordinate or ANY line physical shared coordinate across its six edge steps. Every surviving walk has SIX different point colors and SIX different line colors.

**Automatically distinct source factors:** Suppose the same actual original POINT factor p appeared at two DIFFERENT vertex positions r,t of a surviving closed walk. Those two positions cannot be adjacent, since true ORIGINAL D adjacency explicitly excludes p_i=p_j. At each vertex position, the TWO incident physical point colors belong to the TWO-element physical point edge f(p), and they are distinct because the total six edge colors are squarefree. The two nonadjacent walk positions use FOUR DISTINCT incoming/outgoing edge steps (also when their cyclic distance is two). Thus they would require FOUR different elements of the TWO-element f(p), a contradiction. The identical argument with g(l) establishes that all SIX actual original LINE factor IDs are distinct. In particular, all SIX original incidence-flag vertices i_r=(p_r,l_r) are distinct, so the surviving walk is an ACTUAL SIMPLE SIX-CYCLE on SIX different true original source incidence IDs, without explicit source distinctness enforcement or a synthetic geometry assumption.

The existing [#539](https://github.com/definitely-stable/Mathlab/pull/539) true-original bicolored-rainbow D-sixcycle theorem identifies exactly these surviving directed rooted closed walks with the historically accepted GF(5) original D6 class. Conversely each accepted original D6 contributes precisely the six cyclic choices for the root and two possible orientations, i.e. exactly 12 monomials with the SAME physical point and line six-coordinate sets P,L. All coefficients in the trace are positive, so no cancellation is possible. This proves BG-TRACE and BG-COUNT.

The proof uses only actual original factor uniqueness and the physical TWO-coordinate pair nature of f(p) and g(l), and true D-edge semantics, not the valency or spectrum of the source beyond genuineness. Thus the identity is all-h for true symplectic originals but is not a new GQ-specific spectral lower theorem.

## NEW AA4-BG2: exact ordinary-moment nonimplication for fully fixed original maps

The ordinary scalar adjacency \(B_{ij}=1[D_{ij}=1]\) (equivalently evaluate x=y=1 BEFORE quotient) has trace \(Tr(B^6)\) containing backtracks, repeated original vertices, wrong physical color transitions and ordinary sixcycles not rainbow in both typed physical coordinates. This evaluation is NOT well defined as a ring homomorphism from \(\mathcal R\) because x_i^2=0 while 1^2!=0. Therefore

\[
\operatorname{Tr}(B^6)\ \text{or ordinary sixcycle count}>0
\quad\not\Rightarrow\quad S_{D6}(f,g)>0.
\]

The true ORIGINAL W32, i.e. W(3,2), physically globally injected S68 and S72 fixtures already from #539 have respectively 257 and 261 undirected D edges and CONTAIN ordinary simple uncolored sixcycles, but historically accepted original D6=0 on BOTH; the new exact squarefree trace is identically zero on both. This is a concrete **fully fixed original** counterexample to using just D-graph edge mass, plain uncolored C6 or ordinary spectral sixth moment to derive the historical D6 positive class. It is NOT an all-h original seven-class Branch B counterfamily. The basic non-rainbow counterexample was observed in #539; the new contribution is its explicit NILPOTENT TRACE annihilation mechanism and reproducible coefficientwise fixed-map certificate, not the rediscovery of its zero count.

A separate abstract SIX-vertex physical colored C6 (explicitly NOT claimed a genuine W(3,s) model) has all sixcolor-rainbow closed trace 12 but when just the 6th physical POINT edge color repeats color0 the squarefree trace becomes 0 while the ordinary uncolored C6 remains. This falsifies using uncolored trace without respecting the two independent color palettes.

## Implemented tests, alternate algorithms and limits

The source includes TWO INDEPENDENT finite implementations of the algebraic fixed-map count:

1. **Sparse nilpotent matrix-power dynamic programming:** For every actual original source flag root i, six multiplications of A in the commutative square-zero ring, represented by exact state (current actual original source flag ID, point physical color bitmask, line physical color bitmask) with integer coefficients. The transition never explicitly forbids repeated source vertices/POINT/LINE IDs; nilpotence alone discards repeated physical colors. Gather full coefficient dictionary keyed by masks of size six and assert every coefficient divisible by 12 on a FULL ORIGINAL source-root scan.
2. **Independent literal closed-walk DFS:** Enumerate original D color-labeled walks with no source-factor or simple-cycle pruning and physically squarefree color masks. ONLY after a CLOSED degree-six monomial survives does it independently assert six distinct original source point IDs, LINE IDs and flags; its exact coefficient dictionary must equal the sparse matrix-power dictionary.
3. **Historical actual-original seven-GF(5) independent census** via the existing project oracle, wholly separate from the bicolored D graph, on genuine W32 complete global physical typed maps dual_zero, lex, reverse, S68 and S72: accepted D6 counts 1,15,3,0,0 respectively. Independently compare with original #539 exact rainbow cycle enumerator, on its own actual source IDs. This validates the numerical 12 multiplier, exact source ID semantics and no accidental 'ordinary C6 implies D6' shortcut.
4. Physically independently permute both POINT and LINE coordinate alphabets for a genuine original W32 full map and verify the sum of all squarefree trace coefficients and selected accepted D6 unchanged (different coordinate masks but same true source Q).
5. Real original W34 GF(4) lex physical maps: do a PARTIAL root trace for two specified true original source flag IDs and compare BOTH independent DP and DFS coefficient dictionaries. Explicitly mark result partial and do NOT divide by 12 or call it the complete original selected D6 count.
6. Malformed full globally injected original physical maps, repeated original source incidence IDs, invalid or duplicate partial root sets fail closed.

**Cost limitations:** Enumerating a squarefree degree-(6,6) matrix trace may remain expensive for large s. The compact bitmask DP reduces repeated colored paths in actual W32; it does not constitute a viable asymptotic algorithm for all h. All-h part is the mathematical identity and proof, not synthetic W3 construction in numerical tests.

**Scientific significance and prior art:** The use of square-zero algebras, colored closed walks, and algebraic sieves for paths/cycles is classical and must be credited (e.g. Koutis/Williams-style algebraic k-path detection). The project-specific exact two-typed physical color trace and automatic global source-factor distinctness specialize the **already established #539** genuine-original bicolored D6 correspondence. It is a new scoped algebraic form and a certificate that generic ordinary scalar spectral arguments LOSE essential information; it is NOT an independent proof of the original rainbow equivalence, a uniform original D6 positive minimax bound, or a root Branch C model-equivalent reduction for the complete historical seven-class sum. Earlier #555/#558 prove separate swap-Hessian sign and gauge no-go; these do not imply BG-TRACE's coefficientwise nonnegative fixed-map identity. All six other historical accepted GF(5) classes are expressly OUTSIDE this matrix trace and require additional original incidence/physical pattern matrices and residual Hall constraints.

**Next root-facing mathematics:** Either (a) seek a genuinely ORIGINAL all-fixed-map inequality that bounds the squarefree two-color sixth trace (or compensates its zeros with the SIX OTHER historical accepted GF(5) classes, on the SAME given f,g), or (b) exhibit a genuine infinite family of fully fixed original source f_s,g_s with ALL SEVEN class counts o(s^6), carefully distinguishing it from D6-only W32 zeros. The present trace shows what needs to be retained by any spectral/information-theoretic approach: BOTH physical color alphabets and squarefree conservation of six distinct source incidence positions, not just the numerical spectrum of an uncolored D graph. No false ASET or R3 exponent claims.

**Acceptance:** Keep Draft (parent #570 is Draft and its final Full Research check was CANCELLED), do not merge main or promote canonical RCP claims based on dedicated checks alone. Require exact final-head specialized, INDEX, Proof Audit, Full Research SUCCESS, independent human mathematical review, and intact ancestor stack before integration. Root issue #230 stays OPEN_WITH_FORMAL_BLOCKER.
