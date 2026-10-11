# HYP-105 B3.2-E1-C24-B3 — ALL-h joint-seven exchange stationarity and genuine W32 penalty frontier

Date: 2026-10-11. Parent [#230](https://github.com/definitely-stable/Mathlab/issues/230), scientific child of [C24-B2 PR #346](https://github.com/definitely-stable/Mathlab/pull/346) -> C24-B1 #344 -> C24-A1 #340 -> C23 #334. No main modifications. This is a mathematically exact **ALL-h exchange identity and equivalence of a minimization claim to a local-stationarity gate**, with FINITE W(3,2) quantitative witnesses. It is NOT a proof of a positive universal lower or a full GF(5) risk theorem.

## 1. Model and source-level seven-family exchange

For every s=2^h>=2, let f map all V=(s+1)(s^2+1) ORIGINAL GQ points into an occupied size-V physical K_a pair alphabet, and let g map all V ORIGINAL right GQ lines by ONE complete globally coherent bijection onto the physical occupied F_R. An ORIGINAL six-incidence set J consists of six DISTINCT original incidence IDs and has exactly ONE static potential accepted seven-family tag t_f(J) determined by the original endpoint multiplicities, its physical LEFT projection and (D6 only) LEFT connected column-position dual. The right image under g then either passes the physical six-coordinate degree-two test (and D6 exact same-position dual requirement) or fails. For C/A and C/B keep ORIGINAL right endpoint profile distinct from the symmetric accepted tag.

Let X_J(g) in {0,1} be the acceptance indicator. Define

    S_t(f,g) = sum_{J:t_f(J)=t} X_J(g),
    S_seven = sum_t S_t,
    Q7 = sum_t w_t S_t

where w_t=(5643,45600,45600,43320,49050,51750,45010) are the accepted frozen NECESSARY GF5 numerator weights (Q7 is NOT entire R3). For a transposition (i,j) of TWO ORIGINAL right GQ lines, let g^{ij} swap their assigned physical pair labels globally. The exact ALL-h exchange identity is

    Delta_t^{ij} = S_t(f,g^{ij}) - S_t(f,g)
       = sum_{J:t_f(J)=t, J touches original right i or j}
                      [X_J(g^{ij})-X_J(g)].

Every original J not touching the swapped lines has exactly unchanged acceptance; one J cannot migrate from tag t to another accepted tag under this g-only modification. Across SEVEN tags and original right-C projection:

    Delta S = sum_t Delta_t,
    Delta Q7 = sum_t w_t Delta_t,
    Delta C = S_(original right=C)(f,g^{ij}) -
              S_(original right=C)(f,g).

These are exact integer identities for all-h W(3,s) original sources and all legal global f,g. A negative total Delta S can coexist with positive changes in some classes: compensation is from DIFFERENT original sixsets, not relabeling the same source J to a different tag.

## 2. Exact ALL-h transposition-stationarity proof gate

For any fixed s, complete occupied F_L,F_R and fixed f, the right g-space is finite (V! complete bijections). The global minimizer of the nonnegative integer S_seven is necessarily **one-global-right-transposition stationary**:

    Delta S^{ij}(f,g*) >= 0 for every pair of original right lines i != j.

Hence for any real threshold T, the following are EQUIVALENT (no probabilistic assumption):

    min_{all complete legal g} S_seven(f,g) >= T
    iff
    EVERY globally complete one-swap-stationary g satisfies S_seven(f,g) >= T.

Proof: the forward direction is immediate; if every stationary g has score >=T then any global minimizer is among those stationary g and has score >=T. This is NOT a shortcut to PROVED_A: it replaces all maps by potentially exponentially many stationary maps, with no bound yet known on them, and does not imply that every local minimum is a global minimum. Extending a threshold Omega(s^6) requires the above statement for EVERY s=2^h and EVERY legal f and F_R, with a single constant c>0 independent of h.

Equivalent negative-swap gate: S(f,g)<T implies some complete original right swap lowers S, for EVERY legal g. This has to be proved, not merely observed on a small neighborhood.

The executable tests this all-permutation equivalence on COMPLETE S_3 and S_4 toy groups, not on unenumerated original W32 15! right maps.

## 3. Independent genuine W32 restricted full-seven Lagrange envelope: exact switch at lambda=7

Fix the TRUE original symplectic W(3,2) host with 15 original point lines, 45 original incidences, ONE globally complete LEFT f from C24-B1 with H_C=45 and the ONE complete baseline RIGHT g from C24-B1 with S_seven=177 and S_(original right=C)=0. Consider the precise 105-element set N(g) of complete original RIGHT maps at transposition distance exactly one, not including g itself.

The independently accepted C24-B2 exact finite census gives:

    min_{g' in N(g)} S_seven(f,g') = 129
      at original right swap (6,14), S_(original right=C)=1;

    min_{g' in N(g): S_(original right=C)=0} S_seven(f,g') = 136
      at original right swap (10,14).

Every other complete one-swap g' has S_seven>=129 and integer S_(original right=C)>=0. If C>=1, then for lambda>=0, S+lambda*C>=129+lambda; if C=0 then S+lambda*C>=136. BOTH lower candidates are attained by the above globally coherent full original g' witnesses. Therefore the following is the EXACT lower envelope for every real lambda>=0, with no sampling or independence:

    min_{g' in N(g)} [ S_seven(f,g') + lambda*S_(original right=C)(f,g') ]
       = min(129+lambda, 136).

The two actual complete global right witnesses tie at lambda=7. For 0<=lambda<7 the 129/one-C witness wins; for lambda>7 the 136/zero-C witness wins. This is a **finite neighborhood Pareto/regularization threshold**, NOT a lower on all V! maps or an ALL-h positive S obstruction. It demonstrates why a forced C=0 surrogate can discard better joint-seven scores.

Unlike mere two-witness crossing, this is a provable full 105-map envelope: every other witness is dominated by the two exact minimum bounds above. The executable verifies exact rational lambda probes but the universal-lambda proof is algebraic in the integer bounds.

## 4. Executable joint transposition gradient and bounded descent

A new seven-component signed exchange oracle tracks all 105 complete right swaps of the baseline, computing Delta_t, Delta S, Delta Q7, and ORIGINAL right-C changes, and checks exact class/floor conservation. Several independent full original 62,370 RIGHT-FIRST recounts check selected decisive swaps against the sparse affected-fiber source, not just self-reference.

An additional SECOND one-swap neighborhood around the true complete 129-score global right map (obtained by baseline swap (6,14)) tests whether it is strictly one-swap stationary or has a further improving full S move. If it has a lower full-seven neighbor, apply ONE additional legal global right transposition and independently recount from the original right physical K6 two-factor templates; otherwise label the candidate only one-swap-stationary. No 15! minimum, unbounded local optimization, asymptotic inference or ASET claim. The executable does not assume the result of this second neighborhood ahead of its actual exact check.

- research/hyp105_g5e2b3e1c24b3_joint_swap_gradient.py
- research/test_hyp105_g5e2b3e1c24b3_joint_swap_gradient.py
- .github/workflows/hyp105-c24b3-contract.yml

## 5. Acceptance and next mathematical barrier

Acceptance requires exact PR-HEAD GitHub-hosted C24-B3 Contract SUCCESS, full six-shard Research SUCCESS with seventh fail-closed aggregate, and INDEX SUCCESS; older green HEADs do not transfer. Preserve all 131 C24-B2 named Research commands and append exactly two new C24-B3 commands (133 total), with newly frozen FNV1a64 digest. Do NOT merge into main without safe predecessor integration.

**Outcome to be claimed:** RESTRICTED_ALL-h_EXCHANGE_IDENTITY_AND_STATIONARY_REDUCTION, FINITE_W32_LAMBDA7_PARETO_SWITCH, and finite second-neighborhood audit. Root #230 remains **OPEN_WITH_FORMAL_BLOCKER**. The next proof task is to bound S at ALL global-right stationary maps UNIFORMLY across ALL f for s=2^h, or find an exact infinite correlated original-GQ low-S family. Mere exchange testing, concentration, and the finite penalty frontier do not close either branch A or B.
