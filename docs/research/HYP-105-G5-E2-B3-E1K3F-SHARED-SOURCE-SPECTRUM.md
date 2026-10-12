# HYP-105 B3.2-E1-K3-F1 — shared-source physical-star transport and spectral tail bound

Date: 2026-10-12. Root issue #230. Direct scientific parent PR #370, pinned exact HEAD 841e6fb5b6d59748b8a77ff2232b45169c4fce8f. Inherited PRs #366–369. This is a STACKED DRAFT scientific child; no main change or merge.

**Status: RESTRICTED_THEOREM_C_ALL_h_SHARED_SOURCE_SPECTRAL / OPEN_WITH_FORMAL_BLOCKER_WEIGHTED_BOOK_PACKING.** Exact margin identities, a rigorous all-h Frobenius inequality and high-star tail bounds are proved below. A uniform positive Omega(s^6) for proper D6, the original seven-family sum S, full R3, or ASET is NOT proved.

## 1. Why K3-E does not already solve the problem

K3-E proved for the single globally coherent Kikuchi graph of W(3,s):

    Bmixed=sum_{k=3}^{Cmax} Q_k
       <=sum_{k=3}^{Cmax}Qstar_k
       =sum_mixed max(min(Cmax,d_u,d_v)-2,0)*binom(c(u,v),2),

where Qstar_k still contains the actual mixed codegree weights. Without a JOINT all-h constraint on the physical star degrees, its right-hand side can remain too large. The objective here is a genuine shared-source constraint, not another per-pair inequality.

## 2. Exact source-star transport, all s=2^h

Let V=(s+1)(s^2+1), N=(s+1)V, a the host alphabet. Let M be the V-by-V ORIGINAL W(3,s) point-line incidence matrix. Define P (a-by-V) with P_xp=1 iff x is an endpoint of the SINGLE physical pair f(p), and L (a-by-V) analogously for the SINGLE physical line-pair map g(l). Every column of P,L has exactly two ones. Put

    alpha_x=sum_p P_xp, beta_y=sum_l L_yl,
    D=P*M*L^T.

The matrix entry D_xy equals the degree of Kikuchi vertex (x,y), exactly as in K3-A, but the transport is globally constrained because the same P,M,L occur for ALL x,y.

Counting incidences first by a fixed original point then by its two line-label endpoints yields

    sum_y D_xy=2(s+1)*alpha_x,
    sum_x D_xy=2(s+1)*beta_y,
    sum_xy D_xy=4N,
    sum_x alpha_x=sum_y beta_y=2V.                  (TRANSPORT)

These are exact all-h identities valid for every globally coherent injection. The source physical graphs with V edges have maximum vertex degree alpha_max,beta_max <=a-1. They need not be regular or automorphism-invariant.

## 3. Spectral GQ ingredient: proved from strongly regular point graph

For W(3,s), two distinct original points are on at most one line. The original collinearity graph C on V points is strongly regular with parameters

    v=(s+1)(s^2+1), degree=s(s+1),
    lambda=s-1, mu=s+1.

One can verify these using the GQ axiom (unique point of a line collinear with an off-line point). It follows that

    M*M^T=(s+1)*I+C.

Because C has eigenvalues s(s+1), s-1, and -(s+1), the singular values of M are (s+1), sqrt(2s), and 0. The (s+1) singular direction is the uniform all-ones vector. Therefore

    ||M - ((s+1)/V) 11^T||_op = sqrt(2s).          (GQ-SPECTRUM)

The test suite independently reconstructs point collinearity from original incidences for W(3,2), W(3,4), checking the degree, lambda and mu parameters without importing spectral routines.

## 4. All-h SHARED-SOURCE spectral Frobenius bound

Let mu_xy=(s+1)*alpha_x*beta_y/V. Then

    D-mu = P*[M-((s+1)/V)11^T]*L^T.

By submultiplicativity of matrix norms,

    ||D-mu||_F^2 <= ||P||_op^2 * 2s * ||L^T||_F^2.

Now P*P^T=diag(alpha)+adjacency(G_f), with max absolute row sum 2*alpha_max. Thus ||P||_op^2<=2*alpha_max, and ||L^T||_F^2=2V. The dual inequality swaps P,L. Taking their minimum,

    sum_xy (D_xy-mu_xy)^2
       <= 8sV*min(alpha_max,beta_max).           (FROBENIUS)

For exact integer arithmetic, equivalently

    sum_xy (V*D_xy-(s+1)*alpha_x*beta_y)^2
       <=8s*V^3*min(alpha_max,beta_max).

For each individual physical star pair, zero-mean original point/line indicator vectors and (GQ-SPECTRUM) also give

    (V*D_xy-(s+1)*alpha_x*beta_y)^2
       <=2s*alpha_x*beta_y*(V-alpha_x)*(V-beta_y).

This second inequality is checked exactly as a source-structure falsifier, not presented as a uniform D6 obstruction.

## 5. Joint threshold packing and its limitations

Let H_k=# {(x,y): D_xy>=k}. From exact row and column margins,

    H_k <= sum_x min(a,floor(2(s+1)*alpha_x/k)),
    H_k <= sum_y min(a,floor(2(s+1)*beta_y/k)),
    H_k <= floor(4N/k).

Write mu_max=(s+1)*alpha_max*beta_max/V. If k>mu_max, every physical star with D_xy>=k contributes at least (k-mu_max)^2 to the Frobenius error. Thus

    H_k*(k*V-(s+1)*alpha_max*beta_max)^2
       <= 8s*V^3*min(alpha_max,beta_max).        (SPECTRAL-TAIL)

Let Hupper_k be the minimum of these certified integer upper bounds and a^2. Both left and right original physical maps participate simultaneously in Hupper; it cannot be obtained by choosing independent f,g for each motif.

K3-E's mixed C4-weighted star tail has

    Qstar_k=sum_mixed binom(codeg(u,v),2)
               1[min(d_u,d_v,Cmax)>=k].

At most binom(H_k,2) unordered pairs of distinct high-star vertices exist, while each weight is at most binom(Cmax,2). Consequently

    Qstar_k <= binom(Cmax,2)*binom(Hupper_k,2).
    Bmixed <= sum_{k=3}^{Cmax}
                  min(M2mixed,binom(Cmax,2)*binom(Hupper_k,2)).
                                                              (JOINT-TAIL)

This is a bona fide all-h joint structural upper bound. The last estimate contains the still-unknown C4 second-moment mass M2mixed; replacing it by a valid coarser universal upper would produce a map-independent but potentially very weak estimate. The numeric reporter compares the new JOINT-TAIL bound with K3-E's conditional exact-star bound and EXPLICITLY records whether it improves it. It is not assumed to do so.

**What is NOT proved:** no assertion that the joint-tail bound is o(s^6), any positive proper D6 floor, a seven-family S obstruction, or a full R3 exponent. When the spectral estimate is too loose, retaining a formal NEGATIVE diagnostic is more scientifically valuable than interpreting observed finite slack as a uniform theorem.

## 6. Independent falsification, runner budget, and next gate

Reference: research/hyp105_g5e2b3e1k3f_shared_source_spectrum.py.
Independent tests: research/test_hyp105_g5e2b3e1k3f_shared_source_spectrum.py.

Tests construct the integer matrix P*M*L^T directly from ORIGINAL incidences instead of using K1's source degree tensor; reconstruct original GQ collinearity and check its SRG parameters; verify exact row/column star margins, Frobenius and pointwise spectral inequalities, high-star threshold packing, actual mixed C4 diagonal weights, and K3-E star-tail certificate for globally coherent W(3,2) and W(3,4) labels. Budgets fail closed. Dedicated path-limited 15-minute GitHub-hosted contract plus inherited Research/INDEX, no new full CI matrix, no local PC requirement.

**Next K3-F2:** study explicit overlap-preserving conversion of LARGE source-weighted C4 books to six DISTINCT-ORIGINAL-COLUMN cycles, preferably proper D6 or the accepted seven original six-families, with a proved multiplicity cap and triangle-hook/K4/repeated-column subtraction. Alternatively, show a source-star spectral packing inequality strong enough to dominate the negative book term at order s^6. Neither follows from spectral mixing alone.

Keep issue #230, #176, #169 OPEN and PR Draft until final-head CI + independent review.
