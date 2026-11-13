# HYP-105 / #230 — AA4-GQSPEC: known GQ incidence spectrum → NEW all-h correlated ORIGINAL physical-vertex degree cap O(s²)

**Scientific status:** independent rigorous ALL-h application of the classical generalized-quadrangle real incidence spectrum to the exact, fixed, separately globally pair-injective, potentially mutually correlated f/g physical rectangles of the true symplectic \(W(3,s)\). Strict **Draft child of [#761](https://github.com/definitely-stable/Mathlab/pull/761)** at frozen parent HEAD \`7722dadb6fd6b53db399fd70efff3caf366601d6\`, whose specialist (17/17), INDEX and full Research GitHub-hosted runs all **SUCCESS**. No main mutation, parent merge or issue closure. Issue [#230](https://github.com/definitely-stable/Mathlab/issues/230) stays **OPEN_WITH_FORMAL_BLOCKER**. The spectrum itself is CLASSICAL prior art, not a new spectral discovery; the application to arbitrary ORIGINAL physical symbol-injective pair maps and exact source-degree certificate is the new slice.

**Classical provenance, prior-art honesty.** The matrix identity \(NN^T=(s+1)I+A\), point-graph strongly regular parameters and eigenvalues \((s+1)^2,2s,0\) appear explicitly in D. de Caen & G. E. Moorhouse, *The p-rank of the Sp(4,p) Generalized Quadrangle*, draft dated December 26, 2000, https://ericmoorhouse.org/pub/sp4p.pdf, section 1, and in standard generalized quadrangle incidence geometry (e.g. Brouwer/Godsil treatments). The p-rank over finite fields is a **different problem**; here we use only REAL operator norm and exact INTEGER source incidence identities. Never claim an original discovery of the GQ eigenvalues.

## 1. Why this is the next legitimate geometry gate

The prior #759–#761 original source-first work established exact weighted compatible/incompatible physical P3 moments \(M,G,B\) for fixed ordered physical endpoints, a corrected ORIGINAL middle-label overlap burden \(R\), and an all-order necessary heavy closed original middle overlap neighborhood for local strict \(B/M>3/4\).

The latest strict #761 result is mathematically real but DOES NOT prove the global \(B/M<3/4\). Its source-middle label-overlap neighborhood graph depends on arbitrary f/g, so applying a standard expander-mixing statement directly to THAT label-overlap graph would be INVALID: this graph need not inherit the spectral gap of the original symplectic incidence graph. We must first identify an operator on which the original GQ spectrum genuinely acts.

The correct such operator is the TRUE ORIGINAL point–line incidence \(N\). For each physical coordinate pair \((x,y)\), the actual physical vertex degree is exactly the **GQ incidence count between two ORIGINAL symbol-star subsets**, not an arbitrary weighted middle-overlap count. This yields a concrete, deterministic, all-h, fixed-label and correlation-safe geometric estimate, with a sharp distinction between full ORIGINAL GQ and a retained paired CORE. It is a legitimate next geometric input to the still-open high-order LOW/HEAVY and physical endpoint controls.

## 2. Real incidence spectrum — all-h, independently proved from GQ axioms (KNOWN classical theorem)

Let \(s=2^h\ge2\), \(V_s=(s+1)(s^2+1)\). Let \(P,L\) be the TRUE ORIGINAL points and lines of \(W(3,s)\), both of cardinality \(V_s\), with \(N\in\{0,1\}^{V_s\times V_s}\) the complete, genuine point–line incidence matrix. Every row and every column contains \(s+1\) ones. Define \(T=NN^\top\) and \(J=\mathbf1\mathbf1^\top\).

Since any two distinct original points are on at most one common line (GQ no-\(K_{2,2}\)),

\[
T=(s+1)I+A
\tag{GS-1}
\]

where \(A\) is the TRUE original point-collinearity adjacency matrix. The GQ unique projection axiom implies that \(A\) is strongly regular with

\[
(v,k,\lambda,\mu)=
((s+1)(s^2+1),\,s(s+1),\,s-1,\,s+1).
\]

Indeed two collinear points share precisely \(s-1\) other points on their common original line; a noncollinear pair has \(s+1\) common collinear points (one GQ projection point on each line through the second point). Counting common neighbors gives

\[
A^2=kI+\lambda A+\mu(J-I-A).
\]

Substitute \(T=(s+1)I+A\) to derive, EXACTLY over the integers for every order \(s\),

\[
\boxed{T^2=2sT+(s+1)J.}
\tag{GS-2}
\]

Since \(T\mathbf1=(s+1)^2\mathbf1\), and \(J\) annihilates the zero-sum orthogonal complement, (GS-2) implies \(T^2=2sT\) there. Because \(T=NN^\top\) is real positive semidefinite, its only zero-sum eigenvalues are \(0\) and \(2s\); on the constants, the eigenvalue is \((s+1)^2\). Thus the real singular values of \(N\) are precisely

\[
\boxed{s+1,\quad \sqrt{2s},\quad 0.}
\tag{GS-3}
\]

The nontrivial square-eigenvalue multiplicity is \(s(s+1)^2/2\) and the zero multiplicity is \(V_s-1-s(s+1)^2/2\), directly from the trace \(\operatorname{tr}(NN^\top)=(s+1)V_s\). All are PREVIOUSLY KNOWN facts, reproduced here to make the new application source-auditable.

The dedicated integer source referee checks every entry of (GS-2) for each genuine full W32/W34 fixture, plus the independently computed TRUE ORIGINAL point collinearity \(k,\lambda,\mu\), no fake incidence edge ownership or guessed real eigenvalues via a floating-point eigensolver.

## 3. Real original physical-vertex degree = symbol-star GQ incidence

Fix ANY fully legal maps, separately globally injective but mutually arbitrarily correlated,

\[
f:P\hookrightarrow\binom{[a]}2,\qquad
g:L\hookrightarrow\binom{[a]}2.
\]

For a physical first-factor symbol \(x\in[a]\), let

\[
P_x=\{p\in P:x\in f(p)\},\quad r_x=|P_x|.
\]

For a physical second-factor symbol \(y\), let

\[
L_y=\{\ell\in L:y\in g(\ell)\},\quad c_y=|L_y|.
\]

Because distinct physical point-pair labels containing x have distinct other symbols, and similarly on lines,

\[
\boxed{0\le r_x,c_y\le a-1,\qquad
\sum_xr_x=\sum_yc_y=2V_s.}
\tag{GS-4}
\]

Each TRUE ORIGINAL incidence flag \((p,\ell)\) contributes precisely its TWO opposite undirected physical diagonals on the four corners of its rectangle \(f(p)\times g(\ell)\). Every one of these four physical corners belongs to EXACTLY ONE of those two diagonals, so it adds exactly one incident physical edge at every corner. Separate global pair-injection guarantees that two distinct original source flags cannot own the same physical edge.

Hence in the FULL (unpruned) ORIGINAL physical source graph

\[
\boxed{
d_{\rm full}(x,y)
=\#\{(p,\ell)\in I:p\in P_x,\ell\in L_y\}
=\mathbf1_{P_x}^\top N\mathbf1_{L_y}.
}
\tag{GS-5}
\]

This equation is not a proxy: it identifies the degree in the ACTUAL original physical edge graph. It does not use a random label map, synthetic edge owners or independence of f/g.

If a named original incidence CORE retains only \(I_C\subseteq I\), with its true paired two-diagonal physical edges and deletion \(Z=I\setminus I_C\), then

\[
\boxed{
d_C(x,y)=\#\{(p,\ell)\in I_C:p\in P_x,\ell\in L_y\}
\le d_{\rm full}(x,y).
}
\tag{GS-6}
\]

The full GQ spectrum acts on \(d_{\rm full}\), and this inequality transfers the resulting UPPER degree bound to any retained CORE; NO expander-mixing claim for the arbitrarily deleted CORE incidence matrix is made.

## 4. NEW all-h centered expander-mixing bound for ORIGINAL physical degrees

Decompose the two 0/1 symbol-star indicators into their constant and zero-sum components:

\[
\mathbf1_{P_x}=\frac{r_x}{V_s}\mathbf1+u_x,\qquad
\mathbf1_{L_y}=\frac{c_y}{V_s}\mathbf1+v_y,\qquad
u_x\perp\mathbf1,\quad v_y\perp\mathbf1.
\]

The original GQ incidence matrix is (s+1)-regular, so the mixed terms vanish. From (GS-3),

\[
|u_x^\top Nv_y|\le\sqrt{2s}\,\|u_x\|_2\|v_y\|_2.
\]

Their exact norms are \(r_x(1-r_x/V_s)\) and \(c_y(1-c_y/V_s)\). Substitution into (GS-5) gives the UNCONDITIONAL ALL-h degree inequality

\[
\boxed{
\left|d_{\rm full}(x,y)-\frac{(s+1)r_xc_y}{V_s}\right|
\le
\sqrt{2s\,r_x\left(1-\frac{r_x}{V_s}\right)
c_y\left(1-\frac{c_y}{V_s}\right)}.
}
\tag{GS-7}
\]

Neither \(f\) nor \(g\) need be random or mutually independent. Both sets \(P_x,L_y\) can depend arbitrarily on each other, because (GS-7) holds for EVERY pair of subsets of the TRUE incidence graph. No Sp(4,s) symmetry assumption is imposed on the physical labeling.

The dedicated strict referee evaluates the integer-squared version for EVERY physical vertex in each TRUE full W32/W34 source:

\[
\boxed{
\bigl(V_s d_{\rm full}-(s+1)r_xc_y\bigr)^2
\le2s\,r_x(V_s-r_x)c_y(V_s-c_y).
}
\tag{GS-8}
\]

It checks this EXACTLY with integer multiplication, no floating-point tolerance, and independently tests all actual \(\operatorname{degree}(x,y)\) from the original physical graph adjacency against original-source incidence cross-counts. The sharp integer spectral UPPER cap at a fixed vertex is

\[
\boxed{
d_C(x,y)\le d_{\rm full}(x,y)
\le\left\lfloor\frac{(s+1)r_xc_y+
\lfloor\sqrt{2s\,r_x(V_s-r_x)c_y(V_s-c_y)}\rfloor}{V_s}\right\rfloor.
}
\tag{GS-9}
\]

All rounding is rigorous because \(V_sd-(s+1)r_xc_y\) is integer.

## 5. NEW all-h global minimal-alphabet physical maximum degree O(s²)

ROOT #230 fixes the MINIMAL physical pair alphabet

\[
a_s=\min\{a:\binom a2\ge V_s\}.
\]

Write \(t_s=a_s-1\). For all dyadic \(s\ge2\), \(t_s\le V_s/2\), so both \(r(V_s-r)\) and \(c(V_s-c)\) are monotone increasing throughout the interval \([0,t_s]\). Combining (GS-4),(GS-9) gives

\[
\boxed{
\Delta(H_C)\le\Delta(H_{\rm full})
\le\left\lfloor
\frac{(s+1)t_s^2+
\sqrt{2s}\,t_s(V_s-t_s)}{V_s}
\right\rfloor
=O(s^2).
}
\tag{GS-10}
\]

This is a STRICT quantitative and asymptotic improvement over the trivial original source-point bound \(\Delta\le(s+1)(a_s-1)=O(s^{5/2})\).

The big-O claim is transparent: \(a_s=\Theta(s^{3/2})\), so the first mean term is \(O(s)\) and the nontrivial GQ spectral fluctuation term is \(O(s^2)\). If the physical alphabet a is freely much larger than the ROOT minimal a_s, (GS-7) still holds using actual occupancy \(r_x,c_y\), but (GS-10)'s stated \(O(s^2)\) corollary requires the minimal-alphabet condition; never silently extend it to arbitrary a.

Independently, the TRUE ORIGINAL GQ incidence is \(K_{2,2}\)-free, so for ANY original point subset U of size r and line subset T of size c, the number E of incidences satisfies

\[
E^2-rE\le rc(c-1),\qquad
E^2-cE\le cr(r-1).
\]

This follows from \(\sum_{p\in U}\binom{d_T(p)}2\le\binom c2\) and Cauchy, plus its dual. Their exact integer roots give an additional **independent K22 cap**; each physical-vertex result uses the MINIMUM of the centered spectral cap, the combinatorial K22 cap, and the trivial bound \((s+1)\min(r,c)\). These are all individually valid for EVERY fixed legal original source labeling; no unproved ordering is asserted for arbitrary subsets.

### Computable all-order symbolic root-minimal capacities (NO fake higher-GQ fixtures)

| Original dyadic order s | V points = V lines | Root minimal a_s | NEW centered uniform spectral max degree | Old simple GQ incidence max degree |
| --- | ---: | ---: | ---: | ---: |
| 2 | 15 | 6 | **11** | 15 |
| 4 | 85 | 14 | **41** | 65 |
| 8 | 585 | 35 | **145** | 306 |
| 16 | 4,369 | 94 | **548** | 1,581 |
| 32 | 33,825 | 261 | **2,129** | 8,580 |
| 64 | 266,305 | 731 | **8,366** | 47,450 |

The s=8,16,32,64 rows are **algebraic evaluations of the ALL-h proven formula only**, not a claim that this CI constructed actual W(3,s) source flags at those orders. Only s=2 and s=4 have independently examined full original source flags and physical graphs in this slice.

## 6. NEW source physical degree second-moment bound and exact source conservation

Each true named ORIGINAL retained source flag owns exactly TWO undirected physical diagonal edges. Therefore \(|E(H_C)|=2|I_C|\) and the handshaking lemma gives

\[
\boxed{
\sum_{z\in[a_s]^2}d_C(z)=4|I_C|.
}
\tag{GS-11}
\]

Together with (GS-10) this implies the robust ALL-h source physical degree-square bound

\[
\boxed{
\sum_{z}d_C(z)^2
\le4|I_C|\Delta(H_C)
\le4|I_C|\Delta_{\mathrm{spectral}}(s).
}
\tag{GS-12}
\]

This could serve as a legitimate host-graph norm input for the still-open original LOW/HEAVY proof. For the FULL original graph \(|I|=(s+1)V_s=\Theta(s^4)\), the resulting general bound is \(O(s^6)\). For an arbitrarily retained CORE it scales with the ACTUAL number of retained original incidence flags, not a guessed |Z| or renamed source flag count.

**Critical limitation:** the physical degree second moment by itself is NOT the needed source weighted \(B/M\) estimate or the six-incidence motif floor. For example, replacing all higher spectral terms by worst-case \(\Delta\) in a generic sixth-walk bound can still produce an \(O(s^{10})\) error, far above the target \(O(s^6)\) six-motif scale. Neither the original-weighted endpoint conditional source overlap sum \(\sum_{uv,i}w_{uv,i}N_{uv,i}\) nor the original GF5 positive seven-class incidence motif sum has yet been controlled by GS-12.

The new lemma therefore improves a **genuine original incidence-geometric bottleneck** while retaining the main scientific blocker. A valid subsequent step must couple the physical vertex symbol-star bound to original P3 endpoint distribution and source-selector marginal weights without treating f/g as random or using an invalid physical alphabet assumption.

## 7. Independent complete ORIGINAL source verification

The dedicated referee runs only on the TRUE original symplectic W32/W34 incidence fixtures available in the source project. The following are all independent, fail-closed checks:

1. From genuine ORIGINAL point-line flags, form T=NNᵀ and exhaustively check all V_s² entries of the INTEGER identity (GS-2) for s=2 and s=4; check every original point/line has s+1 incidence neighbors; check source no-K22 and true point collinearity strongly regular \(k,\lambda,\mu\), including exact eigenvalue multiplicity consistency. No use of numerical eigensolver.
2. Independently reconstruct the FULL source \((x,y)\) physical degree by summing ORIGINAL incidence rectangle-corner contributions of ALL GQ flags; separately reconstruct retained CORE physical degree from retained original flags; require exact equality with the actual paired ORIGINAL opposite-diagonal physical graph adjacency at all a² physical vertices.
3. Independently reconstruct every local physical symbol star \(P_x,L_y\) from the exact globally pair-injective point/line labels and recompute \(\mathbf1_{P_x}^\top N\mathbf1_{L_y}\) by DIRECT source incidence checking. Test GS-8 EXACTLY as squared-integer arithmetic. Test the local centered spectral, K22 and simple source-degree caps, and the global root-minimal spectral degree cap.
4. Check all ORIGINAL source \(\sum d=4F\) conservation (full and retained), \(\sum d^2\le4F\Delta\), real physical max-degree witnesses (actual vertex x,y, original star sizes, exact integer squared slack), and all real W32/W34 cases with fixed labels lex/reverse/shift and named retained cores full/even/Z17.
5. Separate algebra-only minimal-alphabet cap examples s=2,4,8,16,32,64, with explicit STOP for unsupported high-s source fixtures; invalid order or negative source star size fails closed.

The specialist GitHub-hosted Ubuntu24 Python3.12 workflow executes 15 independent tests plus a strict eight-source, exact-integer machine JSON certificate; INDEX and full Research must be green on the FINAL HEAD before announcing all-CI acceptance. No changes to main or ancestor PRs, no ROOT PROVED_A, motif S_s lower proof or ASET exponent.

## 7.1. FULL genuine ORIGINAL GQ physical degree observations and strict CI (not all-h extrapolation)

On the scientific code/test HEAD \`247790b5a0ff34c214920e84e884b33c5dc88832\`, the first hosted [specialist #43422311390](https://github.com/definitely-stable/Mathlab/actions/runs/43422311390) completed **SUCCESS, 15/15 independent tests**, plus the strict complete eight-case source JSON certificate. [INDEX #43422311342](https://github.com/definitely-stable/Mathlab/actions/runs/43422311342) completed **SUCCESS** and full [Research #43422311379](https://github.com/definitely-stable/Mathlab/actions/runs/43422311379) must be checked independently. This documentation addition changes HEAD, so success on the new FINAL HEAD must be verified again; never transfer CI acceptance blindly.

All table values below are EXACT integer ORIGINAL source physical degree measurements, not fitted graph data. Degrees are computed twice: (a) from actual physical opposite-diagonal owned edges and (b) from ORIGINAL point-line incidence count \(\mathbf1_{P_x}^\top N\mathbf1_{L_y}\) at EVERY physical vertex.

| Actual TRUE ORIGINAL source configuration | Full source physical max degree | Retained physical max degree | Uniform all-h centered spectral cap | Real full physical \(\sum_z d(z)^2\) |
| --- | ---: | ---: | ---: | ---: |
| W(3,2), FULL lex | **9** | 9 | 11 | 1,026 |
| W(3,2), FULL reverse | **8** | 8 | 11 | 968 |
| W(3,2), shift/Z17 | **8** | 8 | 11 | 950 |
| W(3,4), FULL lex | **25** | 25 | 41 | 16,918 |
| W(3,4), FULL reverse | **18** | 18 | 41 | 16,818 |
| W(3,4), FULL shift | **19** | 19 | 41 | 16,394 |
| W(3,4), lex/even retained CORE | **25** | **13** | 41 | 16,918 |
| W(3,4), shift/Z17 retained CORE | **19** | **18** | 41 | 16,394 |

For comparison, at \(s=4\) the classical no-\(K_{2,2}\) Kővári–Sós–Turán two-set Cauchy bound permits degree 52, the naive source point degree bound permits 65, while the **new application of centered original GQ spectrum proves 41** for every fixed legal minimal-alphabet f/g pair labeling. The actual FULL lex maximum 25 still lies well below 41, so this certificate is a universal worst-case geometric bound, NOT a tight exact degree prediction. The lex/even retained CORE actual maximum 13 demonstrates the necessity of distinguishing FULL GQ spectral mixing from arbitrary CORE source incidence truncation.

Importantly, the real \(\sum d^2\) values can be far smaller than the universal handshaking bound \(4F\Delta_{\rm spectral}\): for FULL W34 lex this generic cap is \(4\cdot425\cdot41=69\,700\), while the exact ORIGINAL source degree square energy is only **16,918**. Therefore using only \(\Delta_{\rm spectral}\) may discard most of the structure needed for a true weighted six-motif result. A legitimate next step should preserve the whole physical degree distribution and the source weighted middle overlap structure, instead of treating the new maximum-degree estimate as a completed Branch A proof.

## 8. Mathematical acceptance, known prior art and next allowed root proof gate

**All-h PROVED (as mathematics, subject to strict head-CI implementation checks):** original GQ incidence spectral polynomial GS-2 (classical, not new); exact true ORIGINAL physical-vertex degree as a source-GQ symbol-star incidence GS-5/6 (source pairing application); CENTERED arbitrary correlated label mixing GS-7/8; root-minimal-alphabet uniform physical max degree \(\Delta=O(s^2)\) GS-10; exact physical degree conservation and square-energy GS-11/12.

**NOT PROVED:** unconditional all-h global original \(B/M<3/4\), source expected true six-incidence \(S_s(f,g)\ge c s^6\), original HEAVY/LOW/GF(5) full seven-class proof acceptance, an infinite correlated bad-label family or any ASET exponent. Source weights need not inherit the original GQ spectral gap merely because source physical vertex degrees do.

**Next step from genuine geometry to weighted risk:** use the new physical degree matrix \(d(x,y)=\mathbf1_{P_x}^\top N\mathbf1_{L_y}\) to bound true weighted proper P3 endpoint fibers, i.e. the frequency with which an ORIGINAL middle physical symbol-star neighborhood can contribute to *two proper paths with the same physical endpoints*. This requires a source GQ incidence tensor contraction (not just a one-point spectral degree bound) and a proof that the resulting weighted R is controlled by \(D+G_{00}+G_{11}\) at scale \(M\), or a concrete infinite legal counterfamily. The current slice supplies a rigorously quantified stronger operator-norm input, not a false conclusion.
