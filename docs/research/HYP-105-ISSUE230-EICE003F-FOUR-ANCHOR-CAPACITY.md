# HYP-105 #230 — EICE-003-F: four TRUE original anchors, blocker signatures and finite GF(5) scope

**Acceptance: RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Strict research-only child of [PR #459](https://github.com/definitely-stable/Mathlab/pull/459), parent frozen at \`56878a4fe071697e1a3836c3ec70a782d3d35053\`. Main untouched. Branch A/B and universal lower \`S_s(f,g)=Omega(s^6)\` **NOT proved**. This is a source-aware classification/certificate, not a claimed GF5 compensation or a novel C4 supersaturation result.

## 1. Typed ORIGINAL four-corner source identity (F1)

Retain a true original GQ W(3,s), globally injective maps \`f:P->E(K_a)\`, \`g:L->E(K_a)\` with canonical minimal a, and a WHOLE original-incidence paired-diagonal EICE-002 coherent physical G*. Fix an oriented true physical MIDDLE edge \`u->v\` with source ID e=(p2,ell2), and two distinct true outer neighbours on both ends: \`w0,w1 in N(u)\\{v}\` and \`z0,z1 in N(v)\\{u}\`. Four ACTUAL nonbacktracking paths \`w_i-u-v-z_j\` define one physical 2×2 plaquette. Each resulting true original endpoint pair, when present, decodes \`q_ij=f^-1({x(w_i),x(z_j)})\`, \`r_ij=g^-1({y(w_i),y(z_j)})\`. If nonincident and end-clean, its unique ORIGINAL GQ projection is \`q_ij--ell_ij--p_ij--r_ij\`.

Define TWO **typed, source-aware** blocker bits on this corner:

    L_ij = 1[ f(p_ij) intersects f(p2) ],
    R_ij = 1[ g(ell_ij) intersects g(ell2) ].

EICE-003-C C1 proves EXACTLY that the corner is internally blocked iff \`L_ij OR R_ij\`. Consequently for an all-four-internally-blocked end-clean original plaquette every corner has one of three signatures: L-only, R-only, BOTH. Across all four corners there are at most 3^4=81 **a priori** typed strings. These are possibility signatures, NOT a claim all 81 are geometrically attainable, nor a new GF5-positive pattern.

## 2. F2 — exact four-corner source-side dichotomy

The 2×2 corner adjacency graph is a C4. Assign at each blocked corner a nonempty subset of the two sides {L,R}. Then either:

(a) some adjacent two corners share a common blocker side (a true left/left or right/right double anchor pressure), OR

(b) there is no such adjacent pair, in which case ALL four masks are singletons and the ONLY possibilities are the two strict checkerboard words LRRL or RLLR (corner order 00,01,10,11).

Proof: If any mask contains BOTH, each adjacent mask must intersect it, so case (a). Otherwise masks are a proper two-colouring of the C4 if and only if no adjacent cells share the same side. There are exactly two 2-colourings, the checkboards. Exhaustive 3^4 oracle validation separately confirms this finite combinatorial identity.

This is a useful exact reduction from 81 types to an adjacent-same-side channel versus 2 alternating source channels. It does NOT bound the total mass of either channel, and the 2 colour checkerboards are not impossible GQ configurations by this argument.

Further source pressure: any three corners blocked on the left have three anchor point labels drawn from the physical star meeting the TWO coordinates of the middle source f(p2). By pigeonhole at least two of these three anchor points intersect the SAME fixed physical coordinate of f(p2). Likewise for ≥3 right corners. This is a necessary source fibre pressure, not a uniform global Hall/SOS or GF5 transfer theorem.

## 3. F3 — canonical six-ORIGINAL-incidence closure and seven-class scope gate

For EVERY end-clean actual physical 3-path, identify all THREE genuine original physical edge source IDs \`(e0,e2,e3)\` by \`ctx.provenance\`, preserving their original (p,line) incidence pairs. If the unique original projection is \`q--ell--p--r\`, identify its THREE true original anchor incidence IDs

    a0=id(q,ell),  a1=id(p,ell),  a2=id(p,r).

The canonical ORIGINAL candidate is the union of these SIX POSITIONS, not an assumed six-set:

    C_path = { e0,e2,e3,a0,a1,a2 }.

Repeated original source incidence IDs may collapse this union to fewer than six DISTINCT factors. Such a degenerate candidate cannot be passed to the accepted original-sixset GF5 classifier. If \`|C_path|=6\`, apply the EXACT frozen seven-family \`classify_seven_prechecked\` to these six ORIGINAL incidence IDs and the SAME true global maps f,g. A classifier return of None is a REJECTION, not a positive motif.

For a four-corner all-blocked plaquette, combine the ACTUAL four canonical source sets into the genuine original incidence footprint \`U\`. The physical NB3 sides contribute at most five DISTINCT source incidence IDs, and four GQ anchors contribute at most 4*3=12, hence

    |U| <= 5+4*3 = 17.

This is an exact all-h source-incidence capacity identity. It does NOT imply the existence of a qualifying six-subset. For finite true original W32/K6 maps we enumerate ALL binom(|U|,6) candidates with explicit budget, classify each under the SAME f,g into the seven accepted classes, and, if requested, INDEPENDENTLY compare each candidate's classification to the *global* full \`seven_census(...,witness_sets=True)\` 62,370-left-six candidate oracle. The acceptance check therefore cannot silently infer positivity from physical K2,2s, from the 4×4 GQ cross-nonincidence count, or from a six-position multiset with repeats. **Extending the accepted seven-family classifier to arbitrary a is a separate formal gate**, not accomplished in EICE-003-F.

When the footprint produces multiple accepted sixsets, those hits are counted as observed finite same-label evidence only. No universal lower bound on hits per blocked plaquette or upper bound on how many plaquettes one sixset serves has been established. If all-four-blocked real plaquettes can be found with zero accepted scoped witnesses, record them as a potential obstruction to THIS LOCAL transfer, not automatically to Branch A. The finite W32 verifier attempts to compare ALL six-subsets in the ORIGINAL incidence footprint of every complete 2×2 plaquette with the independent global seven-census index, and records the exact number of comparisons. **The first genuine coherent five-source W32 square has zero eligible local six-subsets for this comparison.** This is an important limitation, not a successful local transfer. Independent *global* positive W32 six-incidence witnesses provide separate nonvacuous classification controls; they are explicitly NOT counted as four-blocked-plaquette compensation evidence.

## 4. F4 — sharper known bipartite C4 supersaturation, not claimed novel

Inside a fixed genuine r×c oriented NB3 rectangle with r,c>=2, set \`B_{ij}=1\` precisely when its cell is an end-clean internally blocked true original path. Let \`m=sum B_{ij}\` and \`rho=m/(rc)\`. Let \`K\` be the exact number of unordered distinct-row/distinct-column 2×2 plaquettes all of whose four cells are blocked.

By the standard C4 homomorphism Cauchy–Schwarz inequality,

    H = sum_(i,i',j,j') B_ij B_ij' B_i'j B_i'j' >= rho^4 * r^2*c^2.

Subtracting degenerate index terms \`i=i'\` and \`j=j'\` removes at most \`r c^2 + r^2 c\`. Every true distinct 2×2 K2,2 contributes 4 index-orderings. Thus

    K / (binom(r,2)*binom(c,2))
       >= max(0, [rho^4-1/r-1/c] * [rc/((r-1)(c-1))]).     (F4)

This can improve the EICE-003-E elementary four-event union bound \`max(0,4rho-3)\` substantially for moderate blocker densities. It is particularly useful when \`rho\` is bounded below but not near 1; it is a STANDARD bipartite C4 supersaturation consequence, not a new graph theorem or a GF5 compensation.

In the EICE-002 high-degree G* regime \`r,c>=delta*s-1\`, F4 asymptotically reads

    Pr[all four blocked | uniform local 2x2] >= rho^4 - O(1/s).

For an orientation-uniform sampler over squareable middle edges, take the AVERAGE of the LOCAL F4 lower bounds, NEVER replace it by an unsupported global plaquette size-weighted mean. The finite oracle compares this exact Fraction lower against direct enumeration of true original blocker statuses.

## 5. F5 — explicit all-h Ω(s^8) true blocked-plaquette reservoir (conditional on θ)

A quantitative implication of PREVIOUSLY ACCEPTED EICE-002 density/min-degree and EICE-003-E four-corner union sampling is worth stating with its CONSTANTS; it is a valid all-h combinatorial theorem, **NOT a sixset-compensation proof**.

For s=2^h>=4,000,000, let δ=10^-6, and choose the EICE-002 coherent paired G* guaranteed to satisfy

    m=|E(G*)|>=s^4/40000,
    d_*=min_positive_degree(G*)>=δ*s>=4.

Let θ=θ_I∈[0,1] be the ACTUAL stationary true ORIGINAL end-clean internal-blocked NB3 probability for the SAME G*. Every oriented physical middle edge has r,c>=δ*s-1 outer neighbors. Since δ*s>=4,

    binom(r,2) >= δ²*s²/8,
    binom(c,2) >= δ²*s²/8.

Thus each of the exactly 2m oriented middle edges supports at least δ⁴*s⁴/64 **distinct-index 2×2** original physical plaquettes. EICE-003-E E4 gives an orientation-uniform probability at least \`q=max(0,4θ-3)\` that all four ACTUAL endpoints are original nonincident, end-clean and internally blocked. Multiplying the uniform-orientation probability by the MINIMUM number of physical squares per orientation (never by an incorrect globally size-weighted probability) yields

    # oriented all-four-blocked TRUE ORIGINAL plaquettes
       >= q * (2m) * (δ⁴*s⁴/64)
       >= q * δ⁴*s⁸ / 1,280,000.                 (F5)

When θ=1-o(1), this is \`Ω(s^8)\` with an ABSOLUTE explicit though exceedingly small constant. The lower bound is on **ORIENTED physical middle-edge plaquettes**, which may represent the same unordered object multiple times; a future map must preserve this convention or divide by its rigorously bounded multiplicity.

Now suppose a genuinely new theorem constructs a map from EVERY counted all-four-blocked TRUE original plaquette to one of the accepted POSITIVE GF5 six-ORIGINAL-incidence sets with no more than \`K*s²\` oriented plaquettes per target, with absolute K. THEN pure counting would imply the desired

    S_s(f,g) >= q * δ⁴*s⁶ / (1,280,000*K).      (F5-IF-TRANSFER)

This is a precise quantitative TARGET, **not a result**: no such map, all-h accepted-seven classifier, positivity certificate, or multiplicity ≤K*s² exists in this PR. A finite W32 source square with zero blocked corners cannot validate F5's all-h reservoir; the proof above is symbolic for large s. The executable exact Fraction helper \`all_h_blocked_plaquette_reservoir\` deliberately labels the optional K as a NOT-PROVED hypothesis and refuses s below the stated threshold.

### F6 — positive four-corner reservoir already at fixed θ>0 (standard C4 + Jensen)

The local F4 known C4 bound also yields a stronger GLOBAL stationary estimate. Let ρ_e be the fraction of blocked cells in the rectangle of the uniformly sampled oriented middle edge e. Under the genuine stationary NB3 measure (min active degree d_*>=3),

    theta_I = mean_e rho_e.

The F4 bound is at least \`rho_e^4-1/r_e-1/c_e\` (the additional r_e*c_e/[(r_e-1)(c_e-1)] factor is >=1 whenever its inner term is positive; negative terms are handled by the probability floor zero). As r_e,c_e>=d_*-1, average and apply Jensen to the convex fourth power:

    Pr_orient_uniform[all four blocked]
       >= max(0, theta_I^4 - 2/(d_*-1)).        (F6)

Combining with EICE-003-E four-event union bound gives

    q = max(0,4*theta_I-3, theta_I^4-2/(d_*-1)).

Using EICE-002 d_*>=delta*s, the explicit F5 count can be sharpened for
s=2^h>=4,000,000 to

    # oriented all-blocked TRUE ORIGINAL 2×2 plaquettes
       >= max(0,4θ-3,θ^4-2/(delta*s-1))
          * delta^4*s^8 / 1,280,000.             (F5+F6)

Consequently, if θ_I>=ε>0 along an all-h family, then for all sufficiently large s (depending on ε and delta), the all-blocked true four-anchor reservoir is Ω_ε(s^8) even when θ is FAR BELOW 3/4. This is a stronger quantitative profile than E4 alone. It uses the **standard**, previously known C4 Sidorenko/Cauchy–Schwarz inequality and Jensen, and is NOT an original graph-theoretic discovery. Nor is it the missing positive-GF5 transfer; arbitrary all-blocked quadruples could still fail to produce accepted original sixsets.

## 6. Rigorous limits and acceptance gates

- **No false original incidence relation.** Adjacent physical NB3 path factors need not be adjacent ORIGINAL GQ incidences.
- **No false motif closure.** A physical K2,2, physical C6, or eight nonincident original cross pairs is not a seven-family positive sixset.
- **No false finite density.** The EICE-002 canonical W32 source graph has no 2×2 plaquettes; a separate deterministic bounded search constructs a real W32 5-source pair-coherent 2×2 square, but this is not an asymptotic uniform-degree/density example.
- **No false all-blocked witness.** The experiment reports the count of truly four-times internally blocked source plaquettes, whether zero or positive; it does NOT assert existence when none was observed.
- **No unproved transfer.** F1–F4 remain compatible with nearly all corners being blocked, and an all-h source-compensation Hall or bounded-multiplicity map to positive sixsets is still open.

The NEXT actual EICE-003-G proof gate is therefore a **quantitative TRUE source-fibre theorem** of scale O(s²) preimages per accepted positive original sixset, or a genuine all-h exclusion of near-total four-blocking: among all-four-blocked 2×2 plaquettes with complete nonincident end-clean original endpoints, rule out high density of BOTH the adjacent-shared-side channel and the strict alternating channel, OR construct a bounded-multiplicity map from these genuine plaquettes to positive six-incidence ORIGINAL witnesses in the seven accepted GF5 families. Such a map must carry all original IDs and a proof of the multiplicity bound uniform in s.

## Implementation

- \`research/hyp105_issue230_four_anchor_capacity.py\`: all-h algebraic F1/F2, exact W32-specific source GF5 classification, independent provenance and footprint validation, known C4 supersaturation, explicit F5 asymptotic Ω(s⁸) reservoir and strictly hypothetical O(s²) sixset transfer, deterministic nonvacuous W32 fixture.
- \`research/test_hyp105_issue230_four_anchor_capacity.py\`: exhaustive 3^4 mask signatures, exhaustive binary 2×2/2×3/3×3/3×4 quartic C4 lower falsifiers, exact rational F5/F6 s=2^22..2^26 threshold and positive moderate-blocking tests, exact real W32 four schemes + W34 lex/random full maps, nonvacuous genuine five-original-source W32 plaquette, canonical six-source closure, independent frozen seven GF5 global index check, fail-closed invalid source/cut/budget tests.
- \`docs/research/HYP-105-ISSUE230-EICE003F-FOUR-ANCHOR-CAPACITY.md\`: this proof and scope.
- \`.github/workflows/hyp105-issue230-eice003f.yml\`: only GitHub-hosted \`ubuntu-latest\`, no local PC or self-hosted runner.

Research Draft only; no root Branch A or B, no ASET exponent, no main merge.
