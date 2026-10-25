# HYP-105 / #230 AA4-DEG — exact centered physical-degree spectral transfer

**Status: scoped partial theorem / exact finite falsifiers / root OPEN_WITH_FORMAL_BLOCKER.** This result follows AA4-VT on Draft PR #648. It is **not** a proof of the sought \(\chi^2(N_3)=O(1)\), \(P=O(s^6)\), \(M_B=o(s^6)\), or the all-seven-class six-original-flag GF(5) risk floor.

## 1. Scope and connection to established spectral work

Let \(s=2^h\), \(h\ge1\), \(V=(s+1)(s^2+1)\), \(d=s+1\), and \(a=\min\{k:\binom{k}{2}\ge V\}\). The underlying point-line incidence matrix \(M\in\{0,1\}^{V\times V}\) is that of the genuine symplectic generalized quadrangle \(W(3,s)\). The source spectrum (singular values \(d,\sqrt{2s},0\)) is **already known** and appears in the parallel AA4-DM research; it is not claimed as a newly discovered theorem.

Fix *arbitrary correlated*, separately injective and complete typed mappings \(f:P\to\binom{[a]}2\), \(g:L\to\binom{[a]}2\). Define the coordinate-versus-original-factor unsigned incidence matrices \(B_f,B_g\in\{0,1\}^{a\times V}\), where each column contains exactly two ones. Write \(r_u=\sum_q(B_f)_{uq}\) and \(t_x=\sum_l(B_g)_{xl}\); in both cases \(\sum r=\sum t=2V\), and \(r_u,t_x\le a-1\).

The physical graph on ordered coordinate corners \((u,x)\in[a]^2\) is **simple** because of the two global source injections. Its physical corner degree matrix is

\[
\boxed{D=B_f M B_g^{\mathsf T},\quad D_{ux}=\deg_H((u,x)),\quad \sum_{u,x}D_{ux}=4Vd.}
\]

The factorization is exact; every original source incidence contributes four endpoint degrees.

Define the rank-one baseline and residual

\[
D^{(0)}=\frac dV rt^{\mathsf T},\qquad
E=D-D^{(0)}=B_f\left(M-\frac dV J\right)B_g^{\mathsf T}.
\]

This is a centered *physical degree* residual, **not** the centered source-endpoint physical 3-walk multiplicity \(N_3(q,l)\).

## 2. Exact all-h spectral lemma and independent finite identity

The genuine \(GQ(s,s)\) point-collinearity graph is strongly regular:

\[
(v,k,\lambda,\mu)
=\left(V,s(s+1),s-1,s+1\right).
\]

Consequently, \(MM^{\mathsf T}\) has eigenvalues \(d^2,2s,0\). In particular, for \(C=M-\frac dV J\), \(\lVert C\rVert_2^2=2s\), \(C\mathbf1=C^{\mathsf T}\mathbf1=0\). This statement uses the classical original source geometry, and **not** independence or mixing of source label maps.

It admits an integer certificate. Put \(X=VMM^{\mathsf T}-d^2J\). Then

\[
\boxed{X^2=2sV X,\qquad X\mathbf1=0.}
\]

The independent oracle rebuilds the true \(W(3,2)\) and \(W(3,4)\) projective GF(2)/GF(4) incidence flags and checks every entry of this polynomial identity using integers, not floating-point eigenvalues. The rank of \(X\) is \(s(s+1)^2/2\).

## 3. A stronger *restricted* coordinate embedding inequality

Let \(T_a\) be the unsigned vertex-edge incidence matrix of the *complete* \(K_a\). It satisfies

\[
T_aT_a^{\mathsf T}=(a-2)I+J.
\]

Therefore \(T_a\) has squared singular values \(2a-2\) on the constant direction and \(a-2\) on its orthogonal complement. Since the physical image of a typed source embedding comprises **distinct** \(K_a\) edges, padding any \(z\in\mathbb R^V\) with zeros on missing edges yields a complete-edge vector. If \(\mathbf1^{\mathsf T}z=0\), its padded version is orthogonal to the constant edge vector. Hence:

\[
\boxed{\|B_fz\|_2^2\le(a-2)\|z\|_2^2
\quad\text{for all }z\perp\mathbf1.}
\]

And symmetrically for \(B_g\). The improved factor \(a-2\) rather than the trivial top singular value \(2a-2\) relies critically on **source centering plus global injection**, without any regularity assumption on missing edges.

## 4. Exact universal degree-energy bound

Every column of \(CB_g^{\mathsf T}\) has zero source-point sum. Use the restricted embedding inequality on the left, then the known source spectral norm of \(C\):

\[
\begin{aligned}
\|E\|_F^2
&=\|B_f C B_g^{\mathsf T}\|_F^2\\
&\le(a-2)\|CB_g^{\mathsf T}\|_F^2\\
&\le 2s(a-2)\sum_x\left(t_x-\frac{t_x^2}{V}\right)\\
&=2s(a-2)\left(2V-\frac{\sum_x t_x^2}{V}\right).
\end{aligned}
\]

By transposition the point-side degree sequence gives a second independent upper bound. Therefore, for **every** admissible fixed pair \(f,g\):

\[
\boxed{
\|D-\tfrac dVrt^{\mathsf T}\|_F^2
\le 2s(a-2)\min\left\{
2V-\tfrac{\sum_u r_u^2}{V},\,
2V-\tfrac{\sum_x t_x^2}{V}
\right\}.}
\]

This bound is \(O(s^{11/2})\) because \(V=\Theta(s^3)\) and \(a=\Theta(s^{3/2})\). All computations in the test oracle use the exact integer numerator \(V^2\|E\|_F^2=\sum_{u,x}(VD_{ux}-dr_ut_x)^2\), and compare to the exact integer upper bound. No large-\(h\) floats are involved.

### Sharp pointwise source mixing within the same model

For each physical corner independently, project the coordinate-incidence indicator vectors onto the source zero-sum subspaces. Expander mixing gives:

\[
\boxed{(VD_{ux}-dr_ut_x)^2
\le 2s\,r_u(V-r_u)\,t_x(V-t_x).}
\]

This and the Frobenius bound are checked entry-by-entry for both genuine \(W(3,2)\) and \(W(3,4)\), using separate original incidence and physical adjacency reconstructions.

## 5. What this gives — and what it does **not** give

The mean model satisfies \(\|D^{(0)}\|_F^2=O(s^5)\), and the centered residual bound gives \(\|E\|_F^2=O(s^{11/2})\). Thus

\[
\sum_{u,x}D_{ux}^2=O(s^{11/2}).
\]

The pointwise bound and \(r_u,t_x\le a-1\) give maximum physical degree \(\Delta_H=O(s^2)\).

Since the total number of directed 3-walks in any undirected physical graph \(H\) is \(\mathbf d^{\mathsf T}A_H\mathbf d\le\Delta_H\|\mathbf d\|_2^2\), we obtain the (very loose) *universal* envelope

\[
\boxed{P\le\#\{\text{all directed physical 3-walks}\}=O(s^{15/2}).}
\]

This does **not** reach the \(P=O(s^6)\) condition required by AA4-VT, and says even less about the accepted original six-flag GF(5) count.

Quantitatively, \(a^2=\Theta(s^3)\) corners and \(\|E\|_F^2=O(s^{11/2})\) leave RMS **degree** residual \(O(s^{5/4})\), while the average degree is \(\Theta(s)\). These source-spectrum inequalities alone are too weak to certify relative degree concentration, much less \(\chi^2(N_3)=O(1)\). **This is a limitation of the bounds, not a counterexample to the desired \(\chi^2\) theorem.**

A useful next advance must exploit the special four-distinct-first-coordinate/four-distinct-second-coordinate endpoint projection and the genuine GQ source 3-path selection; purely bounding ordinary adjacency-matrix norms discards that information.

## 6. Independent verification / accept-or-reject gate

- [Exact all-h spectral-to-coordinate-degree audit](../../research/hyp105_physical_degree_energy.py) computes the degree matrix, exact centering, both global bounds, all pointwise bounds and an ordinary 3-walk envelope.
- [Independent falsifiers](../../research/test_hyp105_physical_degree_energy.py) use true projective \(W(3,2)\) and \(W(3,4)\) original flags, compare graph degree matrices against direct corner adjacency reconstructions, check the exact \(X^2=2sV X\) polynomial and integer residual upper bounds, independently relabel physical coordinates, and reject malformed noninjective maps.
- All numerical W(3,4) labelings use the existing explicit globally injected adversarial certificate; no stored census counts are used to construct the matrices.
- Scope: **SCOPED DEGREE-ENERGY THEOREM**, not root Branch A/B/C; exact-HEAD CI and independent qualified mathematical referee still required. Never merge the scientific Draft solely because the CI passes.


## 7. Cross-language independent finite integer witnesses

The existing exact symplectic original flags and complete typed maps were recomputed using a separate integer finite-field implementation. The following finite values are frozen as independent regression targets; each residual energy is the **numerator** \(V^2\|E\|_F^2\), not \(\|E\|_F^2\) itself.

| Genuine fixed input | \(\Delta_H\) | \(\sum D_{ux}^2\) | \(V^2\|E\|_F^2\) | spectral upper numerator | \(\Delta_H\sum D^2\) |
|---|---:|---:|---:|---:|---:|
| \(W(3,2)\), LCG seed 41 | 9 | 1,002 | 22,950 | 72,000 | 9,018 |
| \(W(3,2)\), LCG seed 91 | 8 | 970 | 15,750 | 72,000 | 7,760 |
| \(W(3,4)\), explicit adversarial witness | 18 | 16,124 | 8,079,200 | 100,857,600 | 290,232 |

The exact numeric residuals are comfortably within the proven bounds; small finite slack does not establish an all-h \(P=O(s^6)\) or \(\chi^2(N_3)=O(1)\). The generic all-3-walk envelopes are larger than the actual proper nonincident path counts of 986/860/58,730, demonstrating why coordinate-injective projection information must be retained in the next step.
