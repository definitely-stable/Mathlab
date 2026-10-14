# HYP-105 / issue #230 — EICE-003-C: original middle-source Gram transport

**Acceptance class: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Research-only strict child of [PR #452](https://github.com/definitely-stable/Mathlab/pull/452) frozen at HEAD \`3e407388dfb966c3c03e39e0798c99666e212591\`. Parent #451 / #450 / #449 / #394 preserved. No merge or production change. No root Branch A/B proof.

## 1. What EICE-003-B leaves open

EICE-003-B proved, for true globally injected point/line labels f,g and a normalized reversible physical nonbacktracking length-3 path law, the **EXACT identity** \`theta_I=8P/(a-2)+2*(Delta_f+Delta_g)-D\`. Proving \`2*(Delta_f+Delta_g)-D<=1-eta\` is equivalent to proving a gap on theta_I up to its explicit small baseline; renaming the problem a signed-covariance problem does NOT by itself make progress. In particular the symplectic GQ spectrum cannot be applied to an arbitrary original/physical correlation tensor as if it were independent. The correct next step is an explicit transport operator retaining both the original endpoint-anchor and the true ORIGINAL source of the physical middle edge.

## 2. C1 — exact all-h TRUE middle-incidence source kernel

Let s=2^h, V=(s+1)(s²+1), a minimal with binom(a,2)>=V. Let original globally injective f:P→E(K_a), g:L→E(K_a). Let I* be ANY subset of true original GQ incidence IDs, always retaining both physical diagonals, and H the resulting physical graph. Let mu be any normalized **path-reversal-invariant** probability on oriented physical NB3 paths; define the eligible event as in EICE-003-A: coordinate-proper, complete original physical endpoint q and r with (q,r) nonincident, unique true original projection \`q--ell--p--r\`, and end-clean \`f(p)∩f(q)=g(ell)∩g(r)=empty\`.

The physical MIDDLE edge (z1,z2) has exactly one original source ID e2=(p2,l2). By construction its first/second internal left coordinates {x1,x2} are EXACTLY f(p2), and right {y1,y2} are EXACTLY g(l2). Therefore, **pointwise for EVERY eligible path**:

    blocked_left   = 1[ f(p) intersect f(p2) != empty ],
    blocked_right  = 1[ g(ell) intersect g(l2) != empty ],
    blocked_either = blocked_left OR blocked_right.                 (C1)

No fictitious relation between adjacent ORIGINAL incidences is used. No GF(5) motif conclusion is inferred.

Define the TRUE nonnegative transport tensor

    T[(q,r),e] = Pr_mu[eligible, ORIGINAL endpoint factors q,r,
                              ORIGINAL physical MIDDLE edge source ID e].

Rows index genuine original point/line endpoint pairs (q,r); columns index selected original incidence IDs. It is a subprobability transport matrix (sum T=P<=1) and retains all 6-position incidence identities because e is a true source ID.

With p(q,r),ell(q,r) from the unique GQ projection and p(e),ell(e) from the exact original middle incidence,

    B[(q,r),e] = A_f[p(q,r),p(e)] OR A_g[ell(q,r),ell(e)],

    theta_I = sum_(q,r,e) T[(q,r),e]*B[(q,r),e].                    (C1-T)

This identity is exact all-h.

## 3. C2 — exact coordinate Gram factorization and strong source sparsity

Let H_f[p,x]=1[x in f(p)] and H_g[ell,y]=1[y in g(ell)]. Each row contains exactly two ones. Since every distinct original point/line has a distinct unordered physical pair, two different rows overlap at most once. Consequently, the **INCLUSIVE intersection mask**, including identical source factors, is

    A_f = H_f H_f^T - I_V,       A_g = H_g H_g^T - I_V.            (C2)

Here A_f[p,p']=1 iff f(p)∩f(p') is nonempty. Its diagonal is one, NOT zero. The shifted Gram matrices A_f+I, A_g+I are positive semidefinite and have rank at most a; thus A_f and A_g have eigenvalue -1 on subspaces of dimensions at least V-a respectively. This is exact linear algebra, independent of symplectic/W(3,s) spectral estimates. In particular the FULL joint OR kernel B is **NOT claimed** to have rank <=a: the Boolean product and the original source-equality corrections may have much larger rank.

Each physical pair meets at most \`2(a-2)\` OTHER physical pairs, hence every row of A_f,A_g has at most \`2a-3\` ones including itself. Since any true original point or line occurs in only \`s+1\` original incidences, for any original end-clean endpoint pair i=(q,r), the number of selected middle ORIGINAL source IDs able to block is at most

    b_i := |{e in I*: B[i,e]=1}| <= 2*(2a-3)*(s+1).             (C2-SPARSE)

This is exact all-h, correlated-label-safe. On an EICE-002 dense G* with \`M=|I*|=m(G*)/2>=s^4/80000\`, the corresponding **uniform-column baseline**

    beta_i = b_i/M <= 160000*(2a-3)*(s+1)/s^4 = O(s^(-3/2)).

The coefficient is poor at experimentally accessible s but vanishes asymptotically. This is NOT an upper bound on actual blocked-path probability: endpoints and middle sources are strongly coupled.

## 4. C3 — stationary ORIGINAL middle-source uniformity

For every finite undirected physical graph H with m physical edges and degree at least 2 on all active vertices, consider the standard stationary edge-rooted NB3 law

    mu(z0,z1,z2,z3) = 1/[2m*(deg(z1)-1)*(deg(z2)-1)].

Summing over the permitted outer vertices z0,z3 for a FIXED oriented physical middle edge (z1,z2) gives exactly 1/(2m), with no expansion assumption. Since every selected true original incidence ID contributes EXACTLY two physical edges and each has two orientations, there are exactly four oriented physical middle edges per original source e. With M=|I*|, m=2M,

    Pr_mu[middle original source=e] = 4/(2m) = 1/M.             (C3)

This is an **unconditional, exact ALL-h midpoint marginal**. It fails in general for finite graphs with degree-1 vertices when the raw weights are conditioned on successful survival; the implementation explicitly marks conditioned-on-survival cases and never promotes them to C3.

## 5. C4 — centered middle-source transport and the new proof bottleneck

Let \`t_i=sum_e T[i,e]\`, \`beta_i=b_i/M\` and let \`P=sum_i t_i\`. Add and subtract the uniform middle-source *reference distribution* in each eligible original endpoint row:

    theta_I = sum_i t_i*beta_i
            + sum_(i,e) [T[i,e]-t_i/M]*(B[i,e]-beta_i).          (C4)

Here row sums of T[i,e]-t_i/M are zero. C2-SPARSE controls the nonnegative baseline:

    sum_i t_i beta_i <= beta_max P,
    beta_max <= min(1,2*(2a-3)*(s+1)/M)=O(s^(-3/2))

on any all-h EICE-002-certified dense G*. This is a **real new cancellation**: the entire possible O(1) internal blocking mass must arise from the SIGNED TRUE endpoint-to-middle transport correlation, not from the uniform-column baseline.

The missing theorem is now explicit and falsifiable:

    forall complete globally injected f,g, exists valid coherent paired G*
    with fixed Omega(s^4) physical edges / Omega(s) min active degree
    and sum_(i,e) (T[i,e]-t_i/M)*(B[i,e]-beta_i) <= 1-eta          (OPEN)

for some absolute eta>0 (uniform in large s). **This is still equivalent in difficulty to forcing a gap in actual blocking when beta_max=o(1)**, and is not claimed as proved. The value of C4 is that the exact source coupling and available Gram/sparsity constraints are exposed for a genuinely new operator estimate. A simple scalar application of the GQ incidence spectral norm to this arbitrary T is unjustified.

Potential next objects:
- project T along the coordinate channels H_f,H_g and retain the TRUE diagonal source correction (p=p2,ell=ell2);
- classify high positive covariance via original middle-source equality and JPKC-014 original scope capacities;
- compare the same-map observed transport against the seven ORIGINAL GF(5) accepted sixsets, without treating arbitrary physical C6 as positive motifs.

## 6. C5 — rigorous NO-GO for an inadequate proof route

Suppose one discards the requirements that T arise from coordinate-proper physical NB3 paths and that (q,r) have an end-clean anchor; retain ONLY exact uniform original middle-source columns, true W(3,s) unique GQ projections and the exact overlap Gram/sparsity kernel. These conditions **cannot imply** theta_I<1-eta: for every original source e=(p2,l2), choose a genuine original q not on r=l2 whose unique GQ projection to r has anchor point p2. Such q always exists (pick another original line through p2 and a different point q on it). Put exactly 1/M probability on the abstract transport cell \`((q,r),e)\`. The original middle-source marginal is 1/M, and left anchor p=p2 ensures the overlap mask B=1 for **all mass**.

This is a counterexample to the **relaxed transportation argument only**. It does NOT impose true physical path realizability or end-clean constraints, is not a valid globally blocked physical G*, and is **NOT** a counterexample to Branch A or the stationary endpoint/middle transport theorem. It proves why the actual source provenance and endpoint constraints must enter any spectral route.

## 7. C6 — Shannon list-information necessity for near-total blocking

This is an additional **NEW all-h, unconditional-for-stationary-G*** consequence of C2-SPARSE and C3, not merely the tautological rearrangement C4.

In the full normalized stationary NB3 probability space (the one with uniform original middle-source marginal), let E denote the true selected ORIGINAL middle incidence ID, so H(E)=log M in natural units by C3. Define the ORIGINAL endpoint symbol X to be the true pair (q,r) when the full path is coordinate-proper, the endpoints exist and are nonincident, and its unique original anchor is end-clean; otherwise set X=⊥. This makes X a valid deterministic statistic of the true random path, WITHOUT conditioning away ineligible mass.

For every true endpoint row i=(q,r), define the ORIGINAL midpoint blocking list L(i)={e in I*: B[i,e]=1}. Put L(⊥)=empty. By C2, |L(i)|<=b with

    b=min(M, 2*(2a-3)*(s+1)).

Let Z be the indicator E∈L(X); thus **Pr(Z=1)=theta_I exactly**. Because Z is a function of (X,E),

    H(E|X) = H(Z|X) + H(E|X,Z)
           <= h_2(theta_I) + theta_I log b + (1-theta_I) log M,

where h_2(t)=-t log t-(1-t) log(1-t), h_2(0)=h_2(1)=0. The conditional entropy bound uses only the fact that when Z=1 the ORIGINAL middle source E is among at most b allowed IDs, and otherwise among at most M. Subtracting from H(E)=log M proves **C6 (Shannon list information obstruction):**

    I(X;E) >= theta_I log(M/b) - h_2(theta_I).      (C6)

The bound is valid for all-h stationary coherent physical H with active min degree>=2, arbitrary globally injected f,g, no independence or expansion assumption. It is not generally valid with log M if the NB law is *conditioned on survival from degree-1 vertices*.

**Asymptotic consequence in EICE-002 G*.** There M>=s^4/80000 and a<=2s^(3/2), hence b/M=O(s^-3/2). For any hypothetical sequence of admissible f,g and appropriate stationary dense G* with theta_I=1-o(1),

    I(X;E) >= (3/2-o(1))*log(s) - O(1).           (C6-NECESSARY)

In particular a true **upper** bound I(X;E)<=(3/2-eta)*log s+O(1) on at least one valid G* per f,g (eta>0), under the already separately required path-counting theorem R, would exclude theta_I=1-o(1). No such upper bound has been established. Ordinary GQ spectral gap, C2 rank bound, and uniform E marginal do NOT imply it without actual path-realizability constraints.

**Sharpness and NO-GO:** In the abstract relaxation, take M=8, E uniform, X=floor(E/2) with four endpoint symbols, each list L(X) containing exactly its two source IDs. Then theta_I=1 and I(X;E)=log 4=log(M/b): equality in C6. This is NOT a physical GQ path or a counterexample to Branch A. It shows C6's constant is optimal for generic list channels and why one must exploit ORIGINAL physical-path/geometric constraints.

The finite Python diagnostic computes I(X;E) from the complete original joint source-path tensor, including the ⊥ row, and checks the C6 lower bound in floating-point for inspection. The all-h theorem is the algebraic entropy chain above, not the numeric log checks. C1–C4 and all source identities remain exact-Fraction checks.

## 8. Independent finite evidence and proof gates

New files:
- \`research/hyp105_issue230_middle_transport.py\`: true original middle source ID per physical 3-path, stationary exact midpoint uniformity audit, full C1–C4 transport and C6 Shannon list ledger and source Gram/diagonal correction, independent transport-tensor oracle, source-row cap, and explicit C5 relaxed witness.
- \`research/test_hyp105_issue230_middle_transport.py\`: true original W32 all four global maps and W34 lex/random; independent C1-C4 vs previously pinned EICE-003-B B3/source correction; complete bit-level Gram matrices; stationary-vs-leaf law; coherent paired-G* finite checks; explicit positive-relaxation witness; independent sharp abstract C6 list-channel equality and real stationary GQ midpoint information audit.
- \`docs/research/HYP-105-ISSUE230-EICE003C-MIDDLE-TRANSPORT.md\`: this all-h proof, assumptions, no-go and next theorem gate.
- \`.github/workflows/hyp105-issue230-eice003c.yml\`: separate GitHub-hosted runner, no self-hosted runners or user PC dependency.

**Next EICE-003-D:** prove a genuinely non-tautological upper bound on true ORIGINAL endpoint/middle information I(X;E) below (3/2-eta) log(s), or directly on source-transport correlations using path realizability and GQ spectral/representation structure (not middle uniformity alone), or construct a genuine globally injected family exhibiting near-total internal blocking in every permitted G*. A finite W32 graph or an artificial coupling from C5 is not such a family.

**Status:** Branch A OPEN, Branch B OPEN, ASET exponent OPEN. Research PR DRAFT, main untouched, all-h analytic proofs independent of finite CI checks.
