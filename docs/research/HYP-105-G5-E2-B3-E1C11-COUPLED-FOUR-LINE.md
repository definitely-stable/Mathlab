# HYP-105 B3.2-E1-C11 — common-prefix second moments and coupled original four-line completions

Date: 2026-10-10. Parent issue #230. Dependency stack: C0 #249 MERGED → C1 #260 → C2 #261 → C3 #266 → C4 #269 → C5 #273 → C6 #278 → C7 adversarial #279 → C8 #284 → C9 #285 → C10 #286 → C11. Parallel C7 conditional selector #280 remains separate.

**RESTRICTED_THEOREM_C / ALL-h EXACT CONDITIONAL MOMENT / FINITE W32 PREFIX MINIMUM.** The result is for one legitimate original GQ-left map f, one physical occupied right image F, and only original B-left/A-right six-incidence motif overlap. It does not prove all-f,g positive seven-class S, GF5 R3, or ASET exponent.

## One shared right map — all-h exact pair-orbit identity

Let m_f(R) be the nonnegative original-right sixset weight and t_F(Q) be the actual physical K_a occupied two-factor target indicator on V occupied pair-edge labels. For an injective partial map p:D→F of ORIGINAL right lines, set n=V-|D|. A uniform full extension g assigns ALL remaining original lines to distinct remaining physical labels using ONE COMMON bijection.

For ordered original sixsets R,S, define A=R∩D, B=S∩D; r=6-|A|, t=6-|B| and j=|(R∩S)\D|. Its image pair is uniform among all ordered target-label sixset pairs with prescribed pinned memberships p(A),p(B) and j shared unpinned labels; orbit cardinality:

    N(n;r,t,j)=C(n,r)*C(r,j)*C(n-r,t-j).

Write S_(A,B,j) for the ordered weighted source pair mass for this signature and Q_(pA,pB,j) for the count of ordered occupied physical target pairs of this signature. Then exactly:

    E[U(g)^2 | p] = SUM_(A,B,j) S_(A,B,j)*Q_(pA,pB,j)/N(n;r,t,j).

All summands are rational and nonnegative. This is NOT a product of C4 separately frozen anchor conditional expectations; the orbit is for ONE common g. The independent exact first moment is:

    E[U(g)|p] = SUM_(A subset D) b_p(A)*q_p(pA)/C(n,6-|A|).

For no pins these reproduce C5's one-common-bijection mean and seven-overlap second moment. For full pins they equal fixed-g U and U².

## A true fixed-prefix deterministic bound from the common variance

Let M=n! full common completions of p and mu and sigma² their exact first/centered second moment. For EACH individual completion value x, the finite mean-zero constraint plus Cauchy on the other M−1 values implies:

    (x-mu)^2 <= (M-1)*sigma².
    L2(p)=max(0,ceil(mu-sqrt((M-1)*sigma²)))
         <= min_(g extending p) U(g)
         <= floor(mu).

If M=1 or sigma²=0, mu must be an integer and equals every completion. The lower is computed by integer binary search and exact Fraction squared comparisons; no floating roots. The upper is existential, not an exhibited completion. Neither establishes a positive ALL-g minimum unless the lower is uniform over ALL possible p and legitimate f,F.

## Complete genuine W(3,2) four-right-line coupling oracle

For the real W(3,2) reverse-line left map, use C4's exact ORIGINAL distinguished concurrent pair P and residual four ORIGINAL lines H tensor b_f(P,H). Fix the first 11 original right-line physical images of a genuine historical map, leaving original right indices 11–14 and FOUR physical pair labels. Exhaust ALL 4!=24 common bijections of those remaining lines. Each full g must satisfy:

    U(g)=SUM_(P,H) b_f(P,H)*1[g(H) in C_F(g(P))].

Cross-check this original-pair+four-line tensor census against the independently recomputed C5 sixset source/physical target overlap for EVERY one of the 24 maps. Its exact 24-map mean, second moment and variance must agree with the new conditional pair-orbit formula; the historical map must independently reproduce B/A=77. The 24-map minimum is exact ONLY for this one 11-pinned-right prefix, not the full 15! permutation minimum or any all-f,g result.

Finite V=8 oracles enumerate one-common completions (4! and 2!) and independently compare the conditional first and second moments; no-pin V8 comparison uses C5's seven-overlap reference. Generic K8 star fixtures demonstrate exact zero-variance positive-prefix bounds. Inputs reject invalid signed source weights, non-injective pinned maps, duplicate targets, and oversized computation budgets.

## Acceptance and next

Reference: research/hyp105_g5e2b3e1c11_coupled_four.py. Independent tests: research/test_hyp105_g5e2b3e1c11_coupled_four.py. Exact PR-head dedicated GitHub-hosted hyp105-c11-contract and full Research SUCCESS both required, followed by sequential integration of C1–C10 and postmerge Research SUCCESS.

Parent #230 stays OPEN_WITH_FORMAL_BLOCKER. C10's <=3 pin zero-barrier applies to the separate classwise-INDEPENDENT rearrangement relaxation, NOT to these genuinely coupled second moments.

C12: derive globally checkable restricted prefix-orbit stabilizer certificates for every admissible p without factorial enumeration, jointly retaining ORIGINAL GQ concurrency and physical 2-factor completion; or construct an actual full all-h seven-motif counterfamily. Never infer an all-g result from one frozen-prefix W32 sample.
