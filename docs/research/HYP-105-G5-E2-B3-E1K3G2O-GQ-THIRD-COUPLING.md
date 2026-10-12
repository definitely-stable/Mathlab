# HYP-105 E1-K3-G2-O: original GQ triple coupling and Johnson rank three

Date 2026-10-12. Root issue #230, stacked Draft child of #387 at 6ddf54f6e48914b948c0331a358bc759487d5dce. Main and #230/#176/#169 remain unchanged/open. All-h mathematical identities and finite computational tests are explicitly separate.

## O1. Exact ALL-a third Johnson harmonic

The physical six-edge target T_a contains 70*C(a,6) six-edge 2-factors in J(K,6), K=C(a,2). Its physical rank-zero coefficient is p=70*C(a,6)/C(K,6), rank one vanishes, and rank-two pair harmonic h2 is already established in K3-G2-N.

Every triple A of distinct K_a physical pair edges has one of FIVE shapes: triangle, path P4, star K1,3, P3 plus disjoint edge, 3-matching. Their physical target triple codegrees are exactly:

    c3=[C(a-3,3),2*C(a-4,2),0,5*C(a-5,1),8]

and physical triple orbit counts are:

    N3=[C(a,3),12*C(a,4),4*C(a,4),30*C(a,5),15*C(a,6)].

For each physical triple A let H2(A)=sum of h2(B) over its three pairs B. The down-marginal of the lifted H2 on A equals C(K-5,3)*H2(A). The down-marginal of the constant is p*C(K-3,3). On harmonic rank three the up/down-incidence eigenvalue is C(K-6,3). Thus the exact ALL-a rank-three coefficient is

    h3(A)=[c3(A)-p*C(K-3,3)-C(K-5,3)*H2(A)]/C(K-6,3).

The lifted value is t3(S)=sum_{A subset S, |A|=3}h3(A). Its squared norm is C(K-6,3)*sum_{five types o}N3(o)*h3(o)^2. The residual physical squared energy on ranks 4-6 is exactly |T_a|-|T_a|^2/C(K,6)-E2-E3.

At physical a=6 the h3 coefficients for those five shapes are respectively:

    [57/4004, -25/6006, 1/429, 5/4004, 20/3003].

Its exact rank-three squared energy is 710/1001. The entire physical K6 table of 5005 sixsets is independently checked against the separate N Johnson projector on every sixset; no finite interpolation is used to claim the ALL-a formula.

## O2. Original GQ source restriction, ALL h

The original line-intersection graph for W(3,s), s=2^h, has standard strongly regular parameters

    V=(s+1)(s^2+1), k=s(s+1), lambda=s-1, mu=s+1.

This is the classical GQ theorem from the unique-projection axiom, NOT a new strongly regular graph theorem (see Brouwer and Haemers, Spectra of Graphs, section 9.6.3). Its ORIGINAL right-line triple populations classified by r intersecting line pairs are:

    r=3: V*C(s+1,3)
    r=2: V*C(k,2)-3*N3
    r=1: (V*k/2)*(V-2*k+lambda)
    r=0: C(V,3)-N3-N2-N1.

At W32 these are r=0..3 [80,180,180,15]; at W34 [43520,40800,13600,850]. They follow from original GQ, regardless of arbitrary physical f,g.

For every original right-line sixset R, write e_GQ(R) for the number of meeting ORIGINAL right-line pairs within it. Every accepted original B-left six-incidence source support has precisely one doubled original left point; that point uniquely certifies an intersecting pair among the chosen six right lines. After fixing this pair at most (s+1)^4 selections of the remaining original left points exist. Hence for every legal global injection f, ALL h and original R:

    0 <= w_f(R) <= (s+1)^4 * e_GQ(R).

In particular, six mutually disjoint GQ right lines have zero source weight. This genuinely restricts GQ source sixth-order support beyond a generic nonnegative weighted hypergraph, improving C0 uniform 15*(s+1)^4 pointwise for e_GQ(R)<15. It alone does NOT imply a positive overlap lower bound.

## O3. Actual 4x5 original-GQ/physical target correlation tensor

For an ORIGINAL legal coherent (f,g), define the joint nonnegative integer 4x5 tensor

    M[r,o]=sum_R w_f(R) sum_{Q subset R, |Q|=3}
             1[#original GQ meeting pairs inside Q=r]
             1[physical three-edge graph g(Q) has orbit o].

Here r=0..3 uses actual ORIGINAL line IDs and o is one of the five actual physical shapes; crucially both data originate from the SAME Q. The exact mass identity is sum_{r,o}M[r,o]=20*sum_R w_f(R). Rank-three physical target correlation becomes the exact cross-orbit contraction

    C3(f,g)=sum_{r,o}M[r,o]*h3(o).

Independently compute the source rank-three harmonic from real weighted source single/pair/triple moments zero-padded to ALL K_a physical pairs, including unused pair labels when V<K. Writing c0^W=mass/C(K,6), source rank one h1^W, rank two h2^W, triple marginal m3^W(A), obtain

    h3^W(A)=[
       m3^W(A)-c0^W*C(K-3,3)
       -C(K-4,3)*sum_{e in A}h1^W(e)
       -C(K-5,3)*sum_{B subset A,|B|=2}h2^W(B)
    ]/C(K-6,3).

The independent Johnson contraction MUST coincide exactly:

    C3=C(K-6,3)*sum_{|A|=3}h3^W(A)*h3^T(A).

A third method uses N's independent 5005-sixset exact full spectrum. The source rank-three down-kernel and its squared energy are checked. Subtracting rank three leaves C456 and a rigorous but potentially loose bound

    C456^2 <= E_source_ge4 * E_target_ge4.

The ORIGINAL GQ transpose gives a second INDEPENDENT A/B tensor with swapped whole f,g and transposed original incidence. The dual random-injection mean is not replaced by original mu_f. Complete independent B0 seven-family and C0 original/dual sixsource evaluations are retained for finite W32 certificates.

## Exact falsification and limits

Independently enumerate K6 and K9 target triple codegrees, compare entire 5005 physical K6 third harmonic against N rank-three level, verify W32/W34 original GQ triple counts by brute enumeration, and check real W32 ORIGINAL sixsource cherry support including deliberate invalid-weight negative tests. Test W32 lex and K3-G2-M harder correlated original maps including their TRUE dual. Run full paired B0/C0 only twice, not the 223-map old corpus, in dedicated hosted Contract.

The results remain **restricted exact identities, rank-three and source-support theorems**. No proof of universal P2, P7, ALL-h S=Omega(s^6), all-h charge K, full R3 or new ASET exponent. The next K3-G2-P must exploit GQ fiber restrictions on the FEASIBLE 4x5 joint tensors and/or rank 4-6 signed cancellation, not merely rename P2 as a rank decomposition. A counterexample to P2 alone does not refute P7. No merge without exact final HEAD 3/3 SUCCESS and independent mathematical review.
