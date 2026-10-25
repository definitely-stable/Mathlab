# HYP-105 / #230 — AA4-VT centered variance transfer and covariance-sign falsifiers

**Status: DRAFT / rigorous identity plus exact finite W(3,2) witnesses.** Root #230 stays `OPEN_WITH_FORMAL_BLOCKER`. This document is an independent sub-slice of AA4-WE on PR #648, NOT a proof of all-h seven-class GF(5) \(S_s=\Omega(s^6)\).

## 1. State space and notation

Let \(s=2^h\), \(h\ge1\), \(V=(s+1)(s^2+1)\), and \(a\) be minimal with \(\binom a2\ge V\). Fix any **complete separately globally injective** typed physical pair-label maps \(f:P(W(3,s))\to\binom{[a]}2\) and \(g:L(W(3,s))\to\binom{[a]}2\), with arbitrary dependence. The genuine symplectic original GQ flags are immutable.

Set \(\mathcal E=\{(q,r):q\in P,\ r\in L,\ q\notin r\}\), with \(U=|\mathcal E|=Vs^2(s+1)\). Let \(q-l_0-p-r\) be the uniquely determined original three-incidence path. Let \(B\) denote the union of \(f(q)\cap f(p)\neq\varnothing\) and \(g(l_0)\cap g(r)\neq\varnothing\), \(b=|B|\).

Let \(H\) be the physical corner graph as defined in AA4-WE. \(N_3(q,r)\) counts proper directed physical three-walks whose endpoint physical pairs recover this source nonincident \((q,r)\), **before** internal blocking. Write

\[
P=\sum_{\mathcal E}N_3,\quad Q=\sum_{\mathcal E}N_3^2,\quad
M_B=\sum_B N_3.
\]

These are NOT the original GF(5)-accepted six-distinct-source-incidence-ID counts.

## 2. A small but useful all-h structural theorem: the physical graph is simple

For every physical pair of distinct corner vertices \((u,x),(v,y)\) with \(u\neq v,\ x\neq y\), define \(\iota_f(\{u,v\})\) and \(\iota_g(\{x,y\})\) as the unique source factor IDs when those two physical edges are occupied. The adjacency matrix is exactly

\[
A_{(u,x),(v,y)}
=
\begin{cases}
M_{\iota_f(\{u,v\}),\iota_g(\{x,y\})},&
\text{both inverse images exist},\\
0,&\text{otherwise}.
\end{cases}
\]

Entries with \(u=v\) or \(x=y\) are zero. \(M\) is the original \(0/1\) incidence matrix. **Proof:** each true source flag \((p,l)\) contributes the two physical undirected matching edges between opposite corners of the rectangle \(f(p)\times g(l)\). Any such physical edge determines the two unordered coordinate pairs uniquely, which by injectivity determine at most one source \(p\) and at most one source \(l\). Therefore there are *no parallel physical arcs* under the agreed root model, regardless of correlations between the maps.

In tensor form, if \(F_p\) and \(G_l\) are the adjacency matrices of the physical \(K_a\) edges \(f(p)\) and \(g(l)\), then

\[
A=\sum_{p,l}M_{p,l}(F_p\otimes G_l).
\]

Each original incidence contributes exactly two undirected edges, so

\[
\|A\|_F^2=\operatorname{tr}(A^2)=4V(s+1).
\]

This is an exact structural identity for all admissible \(s,f,g\); it does NOT control a particular bad-endpoint \(N_3\) distribution by itself.

## 3. Exact centered finite-population transfer theorem (all h)

Let \(I_B\) be the indicator of the arbitrary fixed bad original endpoint subset. Center it along with the actual path multiplicities:

\[
\sum_{\mathcal E}(I_B-b/U)(N_3-P/U)=M_B-\frac{bP}{U}.
\]

By Cauchy–Schwarz, using **two actual squared norms**, the following holds with no independence:

\[
\boxed{
\left(M_B-\frac{bP}{U}\right)^2
\le
\frac{b(U-b)}{U}\left(Q-\frac{P^2}{U}\right).
}
\]

Equivalently the exact integer obstruction has nonnegative slack

\[
\boxed{b(U-b)(UQ-P^2)-(UM_B-bP)^2\ge0.}
\]

If \(P>0\), define the nonnegative endpoint-distribution divergence

\[
\chi^2=\frac{UQ}{P^2}-1.
\]

The normalized theorem is

\[
\boxed{\left|\frac{M_B}{P}-\frac bU\right|
\le\sqrt{\frac bU\left(1-\frac bU\right)\chi^2}.}
\]

**Precise conditional asymptotic corollary:** the already proved unweighted \(b/U=O(s^{-1/2})\), plus separately proven *uniform* \(P=O(s^6)\) and \(\chi^2=O(1)\), would entail \(M_B=O(s^{23/4})=o(s^6)\) for every admissible correlated map. More generally \(\chi^2=o(s^{1/2})\), together with \(P=O(s^6)\), is sufficient for \(M_B=o(s^6)\). Neither \(\chi^2\) nor \(P\) has been proved uniformly bounded in this PR.

To deduce a positive sixth-order **projected** \(BBo\) floor from \(2BBo_{\mathrm{proj}}=P-M_B-I_G\), one ALSO requires \(P\ge c s^6\) and \(I_G=o(s^6)\). A projected physical walk identity is still NOT the accepted original seven-GF(5)-class source count.

## 4. Two exact genuine W(3,2) sign counterexamples

Use the actual original \(W(3,2)\) symplectic GF(2) geometry: 15 original source points, 15 source lines, 45 original incidence flags, 180 genuine source nonincident typed point/line pairs. The physical alphabet is the **minimal K6**, with 15 distinct physical pairs; *both* f and g are complete independent-injection permutations, not fabricated partial coordinate maps.

To make the example deterministic and inspectable, start from the lexicographically ordered 15 \(K_6\) pairs and apply Fisher–Yates permutation driven by unsigned 32-bit LCG \(x\gets1664525x+1013904223\pmod{2^{32}}\). Each swap at position \(i\) uses \(j=\lfloor x(i+1)/2^{32}\rfloor\). Use seeds \(31+17t\) on the point side and \(900+29t\) on the line side.

| W(3,2) maps | \(b\) | \(P\) | \(M_B\) | \(Q\) | \(UM_B-bP\) | covariance sign |
|---|---:|---:|---:|---:|---:|---|
| both lex | 153 | 946 | 786 | 7,604 | -3,258 | negative |
| LCG \(t=41\) | 145 | 986 | 822 | 8,612 | **+4,990** | **positive** |
| LCG \(t=91\) | 146 | 860 | 636 | 6,312 | **-11,080** | **negative** |

The finite witnesses refute both naive all-\(h\) statements \(\mathrm{Cov}_{\mathcal E}(I_B,N_3)\ge0\) **and** \(\le0\) over **all** legal correlated label maps. Since both sides have legal genuine W(3,2) maps and the samples have opposite signs, any general theorem needs a magnitude bound, additional assumptions, or a different invariant. This does not rule out a sign law restricted to sufficiently large \(h\).

The independent code computes each witness twice: by iterating all genuine incidence-created physical 3-walks, and by contracting four fixed physical endpoint corner orientations with sparse physical adjacency. Additional tests independently reconstruct every physical adjacency entry from the original incidence matrix, reject noninjective f/g, check exact integer centered-variance slack and test arbitrary physical-coordinate renamings.

## 5. Exact W(3,4) continuation, not a new claim

At the earlier W(3,4) explicit certificate: \(U=6800,\ b=4086,\ P=58730,\ M_B=35616,\ Q=676700\); the centered-variance theorem is independently evaluated by exact rational arithmetic. Its \(\chi^2=6800\cdot676700/58730^2-1\) is about 0.3341. The finite \(\chi^2\) observations do **not** establish a uniform all-h variance bound.

## 6. Scientific boundary and next needed theorem

Three separate asymptotic proof obligations remain before even a projected sextic floor could follow:

1. A uniform **upper** \(P=O(s^6)\) and a positive **lower** \(P\ge c s^6\), on the exact physical proper-walk model, rather than assuming the finite census scales universally.
2. A true uniform bound for \(\chi^2\), or a stronger **bad-subset-localized** centered covariance estimate, sufficient to prove \(M_B=o(s^6)\).
3. Independent uniform control \(I_G=o(s^6)\), or an exact original six-incidence GF(5)-acceptance compensation argument across all seven historical classes.

The all-h tensor identity and centered Cauchy inequality are PROVED as scoped mathematics; the finite positive/negative covariance witnesses are **exact counterexamples to sign shortcuts**; none constitutes root `PROVED_A`, `COUNTEREXAMPLE_B` or `RESTRICTED_THEOREM_C`. Preserve scientific Draft and an independent proof-referee gate.
