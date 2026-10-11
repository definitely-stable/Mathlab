# HYP-105 B3.2-E1-C24-B4 — complete original right-swap flow, exact cut reconstruction and genuine W32 third neighborhood

Date: 2026-10-11. Scientific child of [C24-B3 #347](https://github.com/definitely-stable/Mathlab/pull/347), parent [#230](https://github.com/definitely-stable/Mathlab/issues/230). Stacked on C24-B3, with **no main merge**. This is **RESTRICTED_THEOREM_C (exact flow/cut identity)** plus **FINITE original W(3,2) evidence**, not Branch A or B.

## I. The exact all-h source-flow criterion (not a new lower bound)

Let s=2^h >=2, V=(s+1)(s^2+1), and f and g be *complete globally coherent* original GQ point/line-to-physical-pair injections into the two occupied physical pair alphabets. Let \mathcal J be the collection of distinct original six-incidence sets and \mathcal J_t(f) the statically tagged seven-family candidate subcollection. For each J, X_J(g) is one iff its entire original physical right image passes the accepted right test (and D6 dual test). Define S(f,g)=\sum_t\sum_{J\in\mathcal J_t}X_J(g).

For each unordered pair i,j of distinct **original right GQ lines**, let g^{ij} be the single legal global swap and define integer source flow

- G_{ij,t}=number of distinct static-tag-t original J with X_J(g)=0 and X_J(g^{ij})=1.
- L_{ij,t}=number of distinct static-tag-t original J with X_J(g)=1 and X_J(g^{ij})=0.

If \mathcal J_t is compressed, use its original integer multiplicity, not compressed row counts. Write G_{ij}=\sum_t G_{ij,t}, L_{ij}=\sum_t L_{ij,t}. Exactly, for every s,f,g,i,j,

    S_t(f,g^{ij})-S_t(f,g) = G_{ij,t}-L_{ij,t},
    d_{ij}:=S(f,g^{ij})-S(f,g) = G_{ij}-L_{ij}.

The distinct sixsets not touching i or j have zero delta. Each touching J has the same *static* tag before and after the swap. Consequently, for the frozen necessary GF5 numerator Q7=\sum_t w_t S_t, \Delta Q7=\sum_t w_t(G_{ij,t}-L_{ij,t}), with weights (5643,45600,45600,43320,49050,51750,45010). An identical gain/loss projection gives the accepted **original-right-C** change. Neither Q7 nor original-right-C is the complete GF5 R3.

**Local minimum exact criterion:** g is globally right one-transposition-stationary for S **if and only if** G_{ij} >= L_{ij} for every i<j (since d_{ij}=G_{ij}-L_{ij} >=0). A strictly improving swap exists iff L_{ij}>G_{ij} for at least one pair. This is a balance identity and exact stationarity characterization, NOT a proof that every S<cs^6 violates it.

The source support H(J) contains at most six original right line IDs. For |H(J)|=r, exactly \binom V2-\binom{V-r}2 swap edges touch J, independently of g. This gives an exact *exposure capacity* count; it does not force a positive lower on S because accepted and rejected source flows can compensate in the same and different tags.

## II. All-h signed-cut identity and exact gradient recovery

Regard the global-right permutation's one-swap neighborhood as the complete graph on the V original right lines, with signed integer edge weights d_{ij}=G_{ij}-L_{ij}. For every proper nonempty subset U of original right lines define the **aggregate of separate one-swap gradients**

    C(U) = sum_{i in U, j outside U} d_{ij}.

This is NOT the score of a single multi-line block permutation. Pure edge counting gives

    C({i}) = sum_{j != i} d_{ij},
    C({i,j}) = C({i})+C({j})-2*d_{ij},
    2*d_{ij} = C({i})+C({j})-C({i,j}).

Therefore one-swap stationarity is precisely the system of \binom V2 inequalities

    C({i,j}) <= C({i})+C({j})  for all i<j.

Every inequality violation reconstructs a **specific improving original right global transposition**. This holds for ALL h/f/g without probabilistic assumptions, symmetry assumptions or sign monotonicity of individual classes. The pair-cut data have quadratic size, so this is **not** an asymptotic compression breakthrough: the analytical challenge is to bound these correlated cut quantities from the genuine GQ sixset source, uniformly over f,g.

**Warning against weaker cut proxies.** On an abstract three-node signed gradient with d01=-1, d02=+1, d12=+1 all three singleton cuts are (0,0,2), nonnegative, and indeed all nontrivial cuts are nonnegative. Nevertheless the original edge (0,1) strictly improves S. Thus even all-cut nonnegativity is insufficient for one-swap stationarity in a general signed graph. This abstract signed example is not claimed to be GQ-realizable. The pair-cut *difference* identity recovers the missed negative edge.

## III. Genuine W(3,2) finite third neighborhood

Use exactly the C24-B3 frozen original left f=(13,4,2,14,0,11,1,7,10,6,9,5,12,3,8), complete original right g after the two previously verified swaps (6,14) and (12,13):

    (12,10,5,2,8,14,11,7,0,6,3,13,4,9,1).

Baseline S_seven=111. Exhaust all \binom{15}2=105 legal complete globally coherent original-right swaps on this **same** g; compute all seven signed deltas, correct original-right-C projection, necessary Q7 and all cut inequalities, including every nontrivial signed cut up to complement. Independently re-enumerate all 62,370 right-first distinct original sixsets for the 111 baseline and the best third neighbor (or baseline if stationary), then independently count the source-level gain/loss fibers for the best proposed swap. A chosen third swap is applied **only if** its full S strictly decreases. The executable reports whether 111 is truly one-swap stationary instead of assuming either result.

All exact finite values after this third neighborhood, including the best swap, must come from the executable and exact-head GitHub-hosted CI. **Do not predeclare an unknown numerical improvement.**

## IV. What the evidence would and would not mean

- A negative d_ij at 111 yields a third finite coherent W32 improvement, not a bound over all 15! right permutations.
- If all 105 d_ij >=0, the map is a *one-swap* local minimum, not necessarily a global minimum even for this f.
- This W32 check fixes one f and one h. Neither outcome settles \inf_{f,g} S_s(f,g)=\Omega(s^6) with a constant independent of h.
- The desired Branch-A implication S_s(f,g)<cs^6 => some negative d_ij requires an external **uniform, all-f, all-h** structural estimate. Cut inversion alone is an equivalent proof target. Branch B requires an infinite coherent correlated sequence. GF5 full R3 and ASET exponents are out of scope.

## V. Fail-closed acceptance

- A dedicated GitHub-hosted C24-B4 Contract runs exact genuine W32 tests and executable report on the precise PR HEAD.
- Preserve all predecessor Research commands, append only two explicit C24-B4 commands, independently update frozen count+FNV1a64, retain six hosted shards and fail-closed aggregate. INDEX must succeed.
- All three exact-head (Contract, full Research, INDEX) SUCCESS are needed before marking finite C24-B4 accepted. Root #230 stays OPEN_WITH_FORMAL_BLOCKER; do not merge any PR without separate permission or infer main validation.
- Falsifiers: original left-first 105-neighbor sparse change vs separate full right-first 62,370-source score; independent per-sixset gain/loss vs signed score vector; abstract signed-graph singleton-cut counterexample; all 105 pair-cut recovery identities.
