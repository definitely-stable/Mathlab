# HYP-105 E1-K3-G2-S — original/dual incidence-local Hall charging gate

Date: 2026-10-12. Root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked directly on [Draft PR #391](https://github.com/definitely-stable/Mathlab/pull/391) at its exact parent HEAD `cc20469da6eddaf576287ca2ad7243bb32b248c2`. Both PRs stay Draft pending mathematical review. No merges or modifications to main. #230/#176/#169 remain open.

## 1. Mathematical motivation and strict separation of claims

R proves a complete physical **target** rank-0..6 Johnson spectrum, but a true W32 coherent global f,g has BOTH joint source-weighted physical ranks 5 and 6 **negative**. Consequently, neither termwise sign nor the TARGET norm alone can certify universal P2. Q, however, gives an all-h structural decomposition of each **true ORIGINAL** B-left six-incidence support into a unique repeated ORIGINAL point and a 4x4 GQ square-incidence permanent (0,1,2). TRUE transposition yields the dual original A/B line anchor.

This slice replaces sign-only reasoning with a nonnegative *capacity-constrained* flow **candidate**. It uses actual original GQ incidence and actual permanent-1/2 support multiplicities; it does not generate surrogate independent label events, and it does not promote two selected W32 maps to universal quantification.

## 2. Exact all-h sufficient incidence-Hall condition

Let `s=2^h`, `V=(s+1)(s^2+1)`, and `a=min{a:C(a,2)>=V}`. Let the original balanced GQ have point set P, line set L, incidence E, and globally injective true physical unordered-pair maps `f:P->E(K_a)`, `g:L->E(K_a)`. Fix `T_a`, the physical 70*C(a,6) simple six-edge 2-factors, and their density

    rho_a = 70*C(a,6)/C(C(a,2),6).

For the ORIGINAL B/A family, refine Q's nonnegative sixsource weights by their **unique ORIGINAL repeated point**:

    w_f(R) = sum_{p in P} w_f(p,R),
    w_f(p,R) = sum_{B subset R, |B|=2, intersection(B)=p}
                     sum_{Q in Sq_f(p)} perm(E[R\B,Q]).

For the TRUE ORIGINAL DUAL A/B family, with E transposed and whole (f,g) exchanged, define w_g^dual(l,X) analogously with unique ORIGINAL line l. Let

    M_p = sum_{|R|=6} w_f(p,R),
    A_p = sum_{|R|=6} w_f(p,R) 1[g(R) in T_a],
    B_l = sum_{|X|=6} w_g^dual(l,X) 1[f(X) in T_a].

Define BA demand `D_p=rho_a*M_p`. Original BA credit `A_p` is usable only at the SAME original point p. Original dual AB credit `B_l` is usable at point p **only if** `(p,l) in E`. Each credit has total capacity A_p or B_l, even if many original points are incident with one l; credit may not be spent twice.

A nonnegative feasible charging is exactly equivalent (finite capacitated Hall/max-flow-min-cut) to the **specific** full family of inequalities

    for every X subseteq P:
    sum_{p in X} D_p <= sum_{p in X} A_p
                            + sum_{l in N_GQ(X)} B_l.

If this stronger incidence-Hall condition holds for all coherent pairs f,g, summing the full-set inequality proves

    U_BA(f,g) + U_AB(f,g) >= rho_a sum_R w_f(R) = mu_f.

That is the P2 inequality considered in N/M. Crucially, the converse is FALSE: P2 only tests the X=P scalar inequality, not all proper X. This S gate therefore can **fail without refuting P2**. The hall inequality is an explicit testable all-h *sufficient proposal*, not an assertion that it is universally true. It includes the entire exact physical target function `1_T=rho+H2+H3+H4+H5+H6`, allowing cross-rank compensation; it does NOT assert nonnegative H5 or H6.

## 3. Exact finite implementation and two independent falsifiers

For each of two physically coherent original W(3,2) global f,g maps, `lex` and the already pinned `hardest-M` original left swap (13,14):

1. Independently reconstruct all 5005 original right sixsets and all 5005 true transposed original-dual right sixsets using Q's complete GQ square/permanent oracle.
2. Re-enumerate each nonzero source sixset's true ORIGINAL meeting-line anchors, physical disjoint-square candidates, and 4x4 exact GQ permanents, attributing every distinct original support to exactly one original point (or dual line). Check each original sixset's permanent-one and -two counts against Q and the full B0/C0 seven-family oracle.
3. Partition the original and dual source-weighted Johnson ranks 0..6 by their GQ anchors; exact target membership and rank sums must agree. Freeze the hard original joint rank5=`-2473/462`, rank6=`-26/7`. These negative ranks are diagnostic, never “negative capacity.”
4. Scale all demands and credits by `rho.denominator=143`, so that the only capacities are **exact integers**: `demand[p]=2*M_p`, `BA_credit[p]=143*A_p`, `AB_credit[l]=143*B_l`. Edges from p to its BA own credit and to true incident dual l have sufficiently large capacity, credit-to-sink edges have bounded capacities.
5. Compute exact augmenting-path integer max-flow **and its residual minimum-cut witness** independently of a second complete enumeration of **all 32768 point subsets**. The maximum positive Hall violation must be EXACTLY `total_demand-maxflow`. A failing subset has the precise original point IDs, neighborhood and integer deficit, is automatically machine-checkable, and refutes only this explicitly declared local charging.
6. Test adversarial synthetic geometries including a positive scalar P2 margin but *failing* local Hall, and shared dual budget reuse where independent allocation would be invalid. Thus the testing protocol guards against confusing simple scalar positivity with true local geometric transport.

Specialized runner on GitHub-hosted ubuntu-latest must execute the focused tests and independent full W32 JSON report. INDEX and full Research must pass at the exact final PR HEAD, independently of mathematics review. This is a single new focused CI lane, not an ever-expanding redundant matrix.

## 4. Exact preserved hard W32 facts and acceptance criteria

The hard physical global map has ORIGINAL B/A source mass 4984 and actual target 36, TRUE dual A/B target 39, and the fixed-original-left `rho*M=9968/143`. Scalar P2 margin is exactly

    36+39-9968/143 = 757/143 > 0.

The joint rank5/6 signs stay negative. **Whether the restricted GQ-incidence charging succeeds is decided by exact integer max-flow and the 32768 Hall inequalities, NOT by positive scalar margin or signed rank positivity.** The program's `finite_model_feasible` and `hall_shortfall` must be read as computed outcomes; do not predeclare success or falsification in documentation.

A Hall success on the two W32 witnesses is only finite *consistency* for the chosen charging graph. A Hall failure exhibits a valid finite counterexample to that **specific charging graph** and should lead to a relaxation through larger physically justified neighborhoods or additional positive families, not an unsupported claim against P2/P7.

## 5. Next all-h decision gate

After exact-head CI and independent mathematical review, inspect each reported minimum Hall cut. If all finite cuts succeed, the next proof obligation is an all-h expansion/charging theorem: bound simultaneously the ORIGINAL point demands and capacity in their **true incident original dual line neighborhoods**, for arbitrary correlated f,g (and not random labels), with capacities counted exactly once. If some cut fails, identify its incidence geometry, test the minimal non-tautological valid relaxation (e.g. alternating length-three original GQ routes with explicit congestion per supply node), and seal an independent finite falsifier. NEVER infer an all-h conclusion from W32 only.

Status: P2, P7, lower bound S_s=Omega(s^6), R3 upper and ASET exponent remain **OPEN**. No unreviewed all-h statement is presented as a theorem.
