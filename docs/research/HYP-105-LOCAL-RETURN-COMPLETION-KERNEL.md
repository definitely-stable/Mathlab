# HYP-105 / #230 — AA4-COMP: exact genuine-source wedge-to-C6 completion kernel

**Status: scoped all-h graph identity and independent exact GF(2)/GF(4) oracle. Root OPEN_WITH_FORMAL_BLOCKER.** No universal O(s) bound for wedge completions, O(s^6) physical coordinate defect, seven-class GF(5) lower bound, or improved ASET exponent is claimed.

## 1. Scientific target and relation to prior slices

AA4-RC6, PR #652, proves that historical accepted ORIGINAL six-incidence D6 motifs correspond exactly to coordinate-rainbow simple cycles of the physical corner graph. AA4-LCR / AA4-LCR-W, PR #653, proves that all nonrainbow simple physical C6 have local two- or three-step coordinate returns. It also gives the following rigorous **ALL-h original source-pencil wedge identities**:

\[
J_x=2\sum_{p,y}\binom{d_p(y)}2\le Vs(s+1),\quad
J_y=2\sum_{l,x}\binom{e_l(x)}2\le Vs(s+1),
\]

where \(V=(s+1)(s^2+1)\), \(s=2^h\), and the fixed full pair-label maps \(f,g\) on the genuine symplectic \(W(3,s)\) are separately globally injective and may be arbitrarily correlated. The \(J_x,J_y\) count **physical two-edge wedges before completion into C6**; they do not count six-cycles.

The new goal is an exact finite-source preserving description of **how many** physical six-cycles contain each returning wedge. This avoids an unfounded spectral estimate on the physical graph and permits testing candidate \(O(s)\) completion bounds.

## 2. Exact all-h completion kernel

Let \(H=H(f,g)\) be the genuine-source physical **simple** graph on corners \([a]^2\), created from both diagonal physical edges of every ACTUAL original source incidence flag \((p,l)\). Each physical undirected edge carries exactly one original source incidence ID by separate global injection.

Take any **unoriented** returning physical wedge \(w=a-b-c\), where \(a,b,c\) are three **distinct actual physical corners**, physical edges \(ab,bc\) exist, and a and c share **exactly one coordinate**. Define \(S=\{a,b,c\}\) and let \(N(z)\) be physical neighbors of z.

**Theorem (for every dyadic h and every fixed complete injected f,g):**

\[
\boxed{
\operatorname{comp}_6(a,b,c)=
\sum_{\substack{u\in N(c)\setminus S\\
w\in N(a)\setminus S,\ w\ne u}}
\left|(N(u)\cap N(w))\setminus S\right|.
}
\]

*Proof.* A simple undirected physical C6 containing the specified wedge is uniquely represented as the concatenation

\[
a-b-c-u-v-w-a,
\]

where \(u,v,w\) lie outside \(S\) and are pairwise distinct. For each choice of \(u\in N(c)\setminus S\), \(w\in N(a)\setminus S\), \(u\ne w\), the permitted \(v\) are exactly \(N(u)\cap N(w)\setminus S\). Because the physical graph is loopless, \(v\ne u,w\) automatically. Conversely each triple \(u,v,w\) counted here gives one simple six-cycle containing the fixed unoriented wedge. Reversing the wedge swaps the roles of a and c but does **not** double count cycles. All source physical arcs were created solely from genuine original incidence IDs, so no synthetic source-free edge is counted. \(\square\)

An equivalent vertex-deleted matrix form can be used to structure future proofs. Let \(A_T\) be the physical adjacency induced on \(T=V(H)\setminus S\), and let \(r_c,r_a\) be the restrictions of the neighbor indicator vectors of c,a to T. Then

\[
\operatorname{comp}_6(a,b,c)=
r_c^{\mathsf T}A_T^2 r_a
-\sum_{u\in (N(a)\cap N(c))\setminus S}\deg_T(u).
\]

The subtraction removes precisely the non-simple length-two central backtracks \(u-v-u\). This is an **exact identity**; simply substituting \((A^4)_{ac}\), an uncorrected nonbacktracking power, or a scalar eigenvalue bound loses the actual wedge's forbidden vertices and need not count simple C6.

## 3. Exact global double counting and a conditional frontier

Let \(\mathcal J_x,\mathcal J_y\) be the true-original physical returning wedges on either physical coordinate axis. Each physical C6 with a two-step x-coordinate return contributes exactly one term for each index of that return, and similarly for y. Consequently:

\[
\boxed{
W_{2,x}=\sum_{z\in\mathcal J_x}\operatorname{comp}_6(z),\qquad
W_{2,y}=\sum_{z\in\mathcal J_y}\operatorname{comp}_6(z).
}
\]

As proved in AA4-LCR, the local two-step witnesses are not disjoint six-cycles; one physical C6 may contribute multiple returns. Hence the sum \(W_{2,x}+W_{2,y}\) is a **witness population**, not the number of distinct defective C6.

The **conditional implication** is:

\[
\frac{W_{2,x}}{J_x}=O(s),\
\frac{W_{2,y}}{J_y}=O(s)
\quad\text{uniformly over every legal fixed pair }f,g
\quad\Longrightarrow\quad W_2=O(s^6),
\]

because \(J_x,J_y=O(s^5)\). The premise is **not proved**. Also, even if it holds, three-step-only returns still need an independent bound, and a defect upper of \(O(s^6)\) alone is not enough to yield a positive D6 floor without a larger lower bound for all physical C6.

## 4. Exact independent genuinely sourced finite witnesses

A new kernel oracle enumerates physical returning wedges by each actual physical middle corner and unordered endpoint pair, retains the two actual original incidence IDs and their typed source point/line factors, computes all physical four-step completions by two-neighbor common-neighbor intersections, and tests the result against a **second independent depth-four physical path DFS**.

Furthermore:

- An independent **original source-pencil** GQ oracle recomputes total wedge counts \(J_x,J_y\) without relying on the corner adjacency grouping.
- The earlier **independent physical simple C6 source-ID** oracle enumerates every physical C6, records the counts of x/y two-step returning positions, and independently verifies \(W_{2,x},W_{2,y}\).
- Original W(3,2)/W(3,4) full typed pair injections, source-incidence membership, and physical-coordinate permutation invariance are enforced.
- All sums, maxima, second moments, rational means and stored assertions use exact integers and exact rational arithmetic. Hosted exhaustive physical enumeration is restricted to h=1,2; the identity itself is all-h.

| Genuine complete map | \(J_x\) | \(J_y\) | \(W_{2,x}\) | \(W_{2,y}\) | Max comp x | Max comp y |
|---|---:|---:|---:|---:|---:|---:|
| W(3,2), lex K6 | 64 | 52 | 586 | 493 | 28 | 26 |
| W(3,2), reverse-line K6 | 42 | 52 | 352 | 372 | 28 | 16 |
| W(3,4), adversarial full K14 | 624 | 602 | 15,438 | 14,756 | 71 | 86 |

Additional independent integer invariants:

| Genuine map | \(\sum_{w\in\mathcal J_x}\operatorname{comp}_6(w)^2\) | y-side analogue | Nonzero x wedges | Nonzero y wedges |
|---|---:|---:|---:|---:|
| W(3,2), lex | 7,956 | 6,717 | 64 | 51 |
| W(3,2), reverse-line | 4,166 | 3,208 | 42 | 51 |
| W(3,4), adversarial | 484,084 | 459,984 | 624 | 602 |

In particular, **neither** a pointwise inequality \(\operatorname{comp}_6(w)\le s\) **nor** an average inequality \((\sum_w\operatorname{comp}_6(w))/J\le s\) is true for all legal dyadic widths and maps: the W(3,2) and W(3,4) true-source counters refute those coefficient-one versions. The worst y-side W(3,4) returning wedge has **86** completions at \(s=4\), ratio \(21.5s\); the average x-side W(3,4) is \(2573/104\approx24.74\) completions, ratio \(\approx6.185s\). These are **finite coefficient lower constraints**, NOT asymptotic counterexamples to an unrestricted \(O(s)\) conjecture.

## 5. Quantitative next gate and scientific limitations

The remaining all-h mathematical problem is an upper bound for the **average** physical common-neighbor kernel over all **genuine source-returning wedges**, not an independent random-map average. It may require original generalized quadrangle incidence constraints on the **four other source flags** that complete a wedge and/or a truly adversarial infinite correlated-label family. One should test against packed paired-subfield constructions already developed in PR #651 before positing a uniform mean \(O(s)\).

A fixed global label maps source point and line IDs to pair coordinates injectively, and the physical graph may contain triangles despite original incidence girth eight; no unrelated source-graph girth or independent coordinate mixing may be assumed.

Even a full \(W_2=O(s^6)\) upper does NOT settle the pure three-step defect class or the seven-original-sixset GF5 compensation route. **Root #230 remains OPEN_WITH_FORMAL_BLOCKER**. Keep scientific Draft, exact-head GitHub-hosted CI, and an independent qualified mathematical referee gate.
