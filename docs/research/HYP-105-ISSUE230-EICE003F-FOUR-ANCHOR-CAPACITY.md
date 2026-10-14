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

When the footprint produces multiple accepted sixsets, those hits are counted as observed finite same-label evidence only. No universal lower bound on hits per blocked plaquette or upper bound on how many plaquettes one sixset serves has been established. If all-four-blocked real plaquettes can be found with zero accepted scoped witnesses, record them as a potential obstruction to THIS LOCAL transfer, not automatically to Branch A.

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

## 5. Rigorous limits and acceptance gates

- **No false original incidence relation.** Adjacent physical NB3 path factors need not be adjacent ORIGINAL GQ incidences.
- **No false motif closure.** A physical K2,2, physical C6, or eight nonincident original cross pairs is not a seven-family positive sixset.
- **No false finite density.** The EICE-002 canonical W32 source graph has no 2×2 plaquettes; a separate deterministic bounded search constructs a real W32 5-source pair-coherent 2×2 square, but this is not an asymptotic uniform-degree/density example.
- **No false all-blocked witness.** The experiment reports the count of truly four-times internally blocked source plaquettes, whether zero or positive; it does NOT assert existence when none was observed.
- **No unproved transfer.** F1–F4 remain compatible with nearly all corners being blocked, and an all-h source-compensation Hall or bounded-multiplicity map to positive sixsets is still open.

The NEXT actual EICE-003-G proof gate is therefore a **quantitative TRUE source-fibre theorem**: among all-four-blocked 2×2 plaquettes with complete nonincident end-clean original endpoints, rule out high density of BOTH the adjacent-shared-side channel and the strict alternating channel, OR construct a bounded-multiplicity map from these genuine plaquettes to positive six-incidence ORIGINAL witnesses in the seven accepted GF5 families. Such a map must carry all original IDs and a proof of the multiplicity bound uniform in s.

## Implementation

- \`research/hyp105_issue230_four_anchor_capacity.py\`: all-h algebraic F1/F2, exact W32-specific source GF5 classification, independent provenance and footprint validation, known C4 supersaturation, deterministic nonvacuous W32 fixture.
- \`research/test_hyp105_issue230_four_anchor_capacity.py\`: exhaustive 3^4 mask signatures, exhaustive binary 2×2/2×3/3×3/3×4 quartic C4 lower falsifiers, exact real W32 four schemes + W34 lex/random full maps, nonvacuous genuine five-original-source W32 plaquette, canonical six-source closure, independent frozen seven GF5 global index check, fail-closed invalid source/cut/budget tests.
- \`docs/research/HYP-105-ISSUE230-EICE003F-FOUR-ANCHOR-CAPACITY.md\`: this proof and scope.
- \`.github/workflows/hyp105-issue230-eice003f.yml\`: only GitHub-hosted \`ubuntu-latest\`, no local PC or self-hosted runner.

Research Draft only; no root Branch A or B, no ASET exponent, no main merge.
