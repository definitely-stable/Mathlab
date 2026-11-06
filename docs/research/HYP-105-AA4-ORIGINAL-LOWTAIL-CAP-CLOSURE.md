# HYP-105 / #230 — AA4-CAPCLOSE: original collinearity and moment cap closure

**Status:** new restricted mathematical lemma plus independent exact original-source falsifiers, in a scientific Draft child of #731. Not an accepted proof of universal Branch A, not an external referee report, and not an ASET exponent. Keep #230 open and do not merge the scientific stack without independent mathematical acceptance.

## 1. Quantifiers and genuine original source

For every dyadic \(s=2^h\), let \(V=(s+1)(s^2+1)\), \(d=s+1\), \(N=dV\) and \(a=\min\{t:\binom{t}{2}\ge V\}\). Use precisely the **original** point-line incidence flags of symplectic \(W(3,s)\), not a synthetic host, with complete separately globally pair-injective physical labels \(f,g\). The two maps may be arbitrarily correlated. Fix any adversarial deleted set \(Z\) of original incidence IDs, full allowed source \(A=I\setminus Z\), and paired original flag core \(C\subseteq A\). Every core flag retains BOTH original opposite physical diagonals in the simple physical graph \(H_C\) on \(a^2\) vertices. Write \(m=2|C|\), \(\Delta=\max\deg H_C\), and \(K\) for the maximum degree of the ORIGINAL source pencil conflict graph on C.

The [AA4-LOWCERT source/path theorem](HYP-105-AA4-ORIGINAL-LOWTAIL-ALLN-ENERGY.md) gives a lower bound on genuine GF(5)-positive **six distinct original incidence ID** B/B-overlap sixsets in terms of two dual original mixed source books \(B_x,B_y\), \(\|P_3\|_F^2\), \(\operatorname{tr}A_C^4\), original return books and the exact original Z-masked endpoint set. The purpose here is to independently close the four upper-bound inputs under stated caps. Without those caps this result does **not** make LOWCERT positive.

## 2. NEW exact original collinearity-energy identity

Let \(M_P\) be the **genuine original** off-diagonal point-collinearity adjacency of \(W(3,s)\). The generalized-quadrangle point graph is strongly regular with parameters

\[
(v,k,\lambda,\mu)=(V,s(s+1),s-1,s+1).
\]

Counting length-two collinearity walks gives the exact all-order matrix identity

\[
\boxed{M_P^2=(s^2-1)I-2M_P+(s+1)J.}\tag{C1}
\]

For each first-coordinate physical symbol \(x\), define \(S_x=\{p:x\in f(p)\}\), \(d_x=|S_x|\), and \(e_x=\#\{\{p,q\}\subset S_x:p\sim q\}\), counting unordered **original** distinct collinear point pairs. The original source energy is \(G_f=\sum_x\|M_P1_{S_x}\|_2^2\).

Since \(\sum_x d_x=2V\) and \(1_{S_x}^{T}M_P1_{S_x}=2e_x\), (C1) proves the **exact** formula

\[
\boxed{G_f=2V(s^2-1)+(s+1)\sum_xd_x^2-4\sum_xe_x.}\tag{C2}
\]

No randomness, random f/g independence, or physical-coordinate averaging enters this formula. Global injection into pairs of \(K_a\) gives \(d_x\le a-1\) and \(\sum_xd_x^2\le 2V(a-1)\), so

\[
\boxed{G_f\le2V\{s^2-1+(s+1)(a-1)\}.}\tag{C3}
\]

Independently, \(M_P\) has eigenvalues \(s(s+1),s-1,-(s+1)\). Decomposing \(1_{S_x}\) into its constant and orthogonal parts yields

\[
G_f\le 2(s+1)^2V+
\frac{(s+1)^2(s^2-1)}{V}\sum_xd_x^2.\tag{C4}
\]

The **line-dual** original \(W(3,s)\) incidence geometry has the same generalized-quadrangle parameters and gives a distinct exact \(G_g\) formula for source lines and right labels \(g\). We **never identify** \(G_f\) with \(G_g\). Formula (C2) improves practical instance-specific upper bounds by retaining the negative induced-collinearity correction, which spectral bounds discard. For \(s\ge64\), the known \(V\le2s^3\), \(d\le2s\), \(a\le2s^{3/2}\) imply \(G_f,G_g\le20s^{11/2}\) by (C3), independent of the correlation between f and g.

## 3. Exact deletion-aware original mixed books

For the actual ORIGINAL full allowed source \(A=I\setminus Z\), set
\(R_A(p,y)=\#\{(p,\ell)\in A:y\in g(\ell)\}\) and define \(R_C\) similarly. Put

\[
K_{AC}(p,u)=\sum_yR_A(p,y)R_C(u,y),\qquad
c_x(p)=|S_x\cap N_{M_P}(p)|.
\]

The x-blocker book \(B_x\) has precisely the summation semantics of LOWCERT: sum over a core original point u, both orientations \((x,k)\) of its physical pair \(f(u)\), and original \(p\in S_k\), of \(c_x(p)K_{AC}(p,u)\). Its Cauchy factors are \(F_{1,x}=\sum c_x(p)^2\) and \(F_{2,x}=\sum K_{AC}(p,u)^2\) over that same index set.

For fixed \((x,p)\), at most two values k occur because the original physical pair \(f(p)\) has exactly two coordinates; restricting u to core points can only decrease the sum. Consequently

\[
\boxed{F_{1,x}\le2\sum_x\|M_P1_{S_x}\|^2=2G_f.}\tag{C5}
\]

All original core flags on the same point u and containing the same right-coordinate symbol y are pairwise adjacent in the ORIGINAL source conflict graph. Thus \(R_C(u,y)\le K+1\). Each original point has d incidence flags in the FULL source, even after Z, so \(\sum_yR_A(p,y)\le2d\), and \(K_{AC}(p,u)\le2d(K+1)\).

The EXACT ORIGINAL-source to physical contraction from #728 is

\[
\Theta_{AC}=\sum_{(x,k,u)}\sum_{p\in S_k}K_{AC}(p,u)
=\sum_{k,y}D_A(k,y)D_C(k,y)\le4|A|\Delta.
\]

Here \(D_A,D_C\) are physical degrees from the two diagonals of each surviving ORIGINAL flag; a projected original anchor may lie outside C but must be outside Z. Combining this contraction with the pointwise K cap gives

\[
\boxed{F_{2,x}\le2d(K+1)\Theta_{AC}
\le8d(K+1)|A|\Delta.}\tag{C6}
\]

Cauchy then proves, **separately for the point and line duals**,

\[
\boxed{
B_x\le\sqrt{16d(K+1)|A|\Delta G_f},\qquad
B_y\le\sqrt{16d(K+1)|A|\Delta G_g}.
}\tag{C7}
\]

These are all-finite-order original deletion-aware mixed source upper bounds. In particular, if \(K=O(1)\), \(\Delta=O(s)\), and \(|A|\le N=O(s^4)\), then \(F_{2,x},F_{2,y}=O(s^6)\) and \(B_x,B_y=O(s^{23/4})\). A sparse core may have much smaller B but the asymptotic theorem cannot infer a positive leading path count from sparsity.

## 4. Independently closed selector fourth and sixth moments

For each original core flag draw a random *priority*, retain its flag only if earlier than each actual source-conflict neighbor, then independently color both physical coordinate alphabets and retain WHOLE original flags with two bichromatic labels. Neither f nor g changes. In each outcome the selected physical graph G is bipartite, has no row/column two-cherries, and every simple physical C6 is coordinate proper, represents six **distinct original** surviving source flags and injects into a historical GF(5)-positive original D6 sixset avoiding Z. Hence \(C_6(G)\le D_Z\), with \(D_Z\) the full original six-ID D6 count avoiding Z.

For \(r=2,3\), a coordinate-proper physical r-path has r pairwise nonconflicting original flag owners. If b is the union size of their closed source-conflict neighborhoods then \(b\le r(K+1)\). The event that these r flags are earliest in their union has exact probability \(\binom{b}{r}^{-1}\); both independent coordinate cuts preserve r proper path edges with probability \(4^{-r}\). Therefore every actual proper r-path survives with probability at least

\[
\boxed{\sigma_r=\frac{4^{-r}}{\binom{r(K+1)}r},
\qquad q_r=\sigma_r^{-1}=4^r\binom{r(K+1)}r.}\tag{C8}
\]

There is **no** independence assumption between distinct paths. Let \(D_*\) be a separately justified upper on \(D_Z\). For any bipartite selected G, a nonsimple closed 6-walk contains a 2-step backtrack. Contraction of the backtrack and Cauchy give \(\operatorname{tr}(A_G^6)\le12C_6(G)+6\Delta\sqrt{2m\operatorname{tr}(A_G^6)}\). Young's inequality \(6\Delta\sqrt{2mX}\le X/2+36m\Delta^2\) proves the **outcome-wise** cap

\[
\boxed{\operatorname{tr}(A_G^6)\le X_6:=24D_*+72m\Delta^2.}\tag{C9}
\]

Consequently \(\operatorname{tr}(A_G^4)\le\sqrt{2mX_6}\). Let \(P_r(u,v)\) count the actual original-core coordinate-proper directed physical r-paths from u to v. Their selector expectation is bounded below **pointwise** by \(\sigma_r P_r(u,v)\). Jensen, summed over original physical endpoints, without assuming independent path survival, yields

\[
\boxed{\|P_3\|_F^2\le q_3^2 X_6,\qquad
\|P_2\|_F^2\le q_2^2\sqrt{2mX_6}.}\tag{C10}
\]

The UNCUT physical core \(H_C\) is not assumed bipartite. Write \(A_C^2=P_2+R_2\) where \(R_2\) is the nonnegative matrix of two-walks repeating a first or second physical coordinate. Its total mass is at most \(Q_x+Q_y\), the exact genuine ORIGINAL point/line pencil return books from LOWCERT, and each entry is at most \(\Delta\). Therefore \(\|R_2\|_F^2\le\Delta(Q_x+Q_y)\), and

\[
\boxed{\operatorname{tr}(A_C^4)
\le2q_2^2\sqrt{2mX_6}+2\Delta(Q_x+Q_y).}\tag{C11}
\]

If \(D_*=O(s^6)\), \(m=O(s^4)\), \(\Delta=O(s)\), and \(Q_x+Q_y=O(s^4)\), these prove \(\|P_3\|_F^2=O(s^6)\), \(\operatorname{tr}(A_C^4)=O(s^5)\), and by (C7) each original internal blocker error is \(O(s^{47/8})=o(s^6)\). This derives the actual bounds requested by the preceding scientific Draft, **conditionally on an original dense capped core and the D6 upper**, not by promoting four W32/W34 sample computations to an all-order theorem.

## 5. Combined exact LOWCERT and the fixed-rho obstruction

Use independently established upper data \(\Delta,K,Q_*,E_*,D_*,G_f,G_g\), with \(Q_*\ge Q_x+Q_y\), \(E_*\ge|E_{bad}|\), \(D_*\ge D_Z\), and the true original core size C. Apply (C7)-(C11) to obtain ceilings \(B_x^*,B_y^*,P_3^*,t_4^*\). The pre-existing original six-ID LOWCERT source bridge now gives the explicit valid, exact rational inequality

\[
\boxed{
2\,BBo_{\overline Z}
\ge\max\{0,\frac{(4|C|)^3}{a^4}
-3\Delta Q_*
-\sqrt{E_* P_3^*}
-2\sqrt{B_x^*\Delta t_4^*}
-2\sqrt{B_y^*\Delta t_4^*}\}.}\tag{C12}
\]

The implementation takes upward-rounded integer square roots at every use, so it is a conservative exact arithmetic certificate. Its finite tests use the **unconditional but deliberately loose** \(D_*=\binom{|A|}{6}\). Supplying \(D_*=s^6\) without proving the actual ORIGINAL D6 bound is **not permitted**.

The true source projection mask has \(E_*\le O(s^5)+12s^2|Z|\). Consequently its path-energy penalty is \(O(s^{11/2})+O(s^4\sqrt{|Z|})\). This is \(o(s^6)\) when \(|Z|=o(s^4)\); however, for fixed \(|Z|\le\rho s^4\) with \(\rho>0\), the second term has magnitude \(O(\sqrt\rho\,s^6)\), **not** little-o. Positive-density deletion resilience requires a separate quantitative choice of sufficiently small rho to absorb it into the leading \(\Omega(s^6)\) density, plus correct constants/thresholds.

For every correlated f,g these caps are valid *when their explicit hypotheses hold*. They do **not** by themselves establish existence of \(|C|\ge c s^4\), \(\Delta\le Ts\), \(K\le K_0\), a suitable \(D_Z\) hypothesis, or the heavy-tail dichotomy. Those remain separate original-GQ geometric proof and scientific acceptance gates in #659/#672/#674/#730. No general weighted ASET claim, full R3 bound or root #230 acceptance follows here.

## 5a. NEW exact improved quantitative original-deletion-mask absorption

The preceding uniform selector and the new tighter sixth-moment coefficient permit an **explicit, stronger conditional deletion budget** than the original conservative #674 mask ledger. Assume, in addition to genuine original W(3,s) and fixed correlated f/g, that for the actual original deletion-free paired core (itself a subset of I\Z), the verified caps are

\[
m\le4s^4,\qquad \Delta\le Ts,\qquad K\le K_0,\qquad
D_Z\le s^6,\qquad s\ge64.
\]

Here T is a real positive physical degree constant; an integer ceiling can be used in the executable exact rational ledger. Define

\[
q_3=64\binom{3(K_0+1)}3,\qquad
L_6^{new}=24+288T^2.
\]

Equations (C9)–(C10) give the **actual ORIGINAL-source proper path moment**
\(\|P_3\|_F^2\le q_3^2 L_6^{new}s^6\).
The projection deletion part of the source endpoint union has at most \(12s^2|Z|\) ordered physical endpoints; the true FULL original GQ, not the pruned core, determines those projected anchors. Cauchy therefore bounds its contribution by

\[
M_{\rm Zmask}\le \sqrt{12s^2|Z|\,q_3^2L_6^{new}s^6}
=q_3\sqrt{12L_6^{new}}\;s^4\sqrt{|Z|}.
\]

**Conditional quantitative lemma (CAP-RHO):** if

\[
\boxed{|Z|\le\rho_{\rm new}s^4,\qquad
\rho_{\rm new}=\frac1{768\,q_3^2(24+288T^2)},}
\tag{C13}
\]

then \(M_{\rm Zmask}\le s^6/8\) for every dyadic \(s\ge64\) and **every** correlated fixed legal f/g satisfying the displayed core and D6 caps. This is a *bounded sextic* error, not little-o. It must still be combined with the distinct original non-Z endpoint O(s^(11/2)) term, the other errors, and a positive dense-core leading term to infer a positive lower bound.

For identical formal K,T input the old conservative #674/#672 error ledger used \(q_{3,old}=64\cdot27(K+1)^3\), \(L_{6,old}=24+576T^2\), and \(\rho_{old}=1/(768q_{3,old}^2L_{6,old})\). Our \(\rho_{\rm new}>\rho_{\rm old}\) **strictly for every K>=0,T>=1**. For FORMAL \(K=64,T=2^{65}\), the exact rational ratio \(\rho_{\rm new}/\rho_{\rm old}\) lies between 74 and 75. This is an algebraic sensitivity comparison; the published C6 graph supersaturation theorem supplies **existential** graph constants, NOT numeric \(C_{\rm graph}=1\). No root or full deletion-resilience theorem is promoted by this improved conditional budget.


## 6. Independent falsification and reproducibility

The new research module reconstructs the **real ORIGINAL** W(3,2) and W(3,4) incidence graphs, both original point and line-dual collinearity graphs, checks every SRG common-neighbor parameter, independently computes both sides of (C2) as integers, and checks (C4), (C5)-(C7), (C10)-(C12). It computes K from actual original retained flag IDs and their original source-pencil conflicts.

It crosschecks the original W32/W34 lex and reverse-line schemes against the existing **separately implemented** #731 full original six-ID source-path/GF(5) certificate (including adversarial Z and core C). It uses the genuine original 15-duad/15-syntheme W(3,2) construction as an additional manual algebra falsifier. Malformed original incidence, noninjective labels, bad caps, and the mistaken fixed-density little-o claim have negative tests.

The dedicated hosted fail-closed workflow verifies eight unit tests and a machine-readable four-case certificate under explicit shell pipefail; published green CI is evidence of correct reproducibility of these finite statements only, **never** proof of universal all-h acceptance. Root #230 remains OPEN_WITH_FORMAL_BLOCKER, with no merge.

**Next critical step:** independently verify the dense source core existence and the quantitatively absorbed deletion-mask term on every legal fixed f,g, then do an independent mathematical review of the complete parent stack and exact-HEAD Research CI.
