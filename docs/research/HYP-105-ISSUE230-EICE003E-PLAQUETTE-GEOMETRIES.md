# HYP-105 / issue #230 — EICE-003-E: four-corner ORIGINAL GQ source plaquettes

**Status RESTRICTED_THEOREM_C / OPEN_WITH_FORMAL_BLOCKER.** Strict research-only child of [PR #454](https://github.com/definitely-stable/Mathlab/pull/454) at frozen HEAD \`cf7a71b9ebf05fd825e6f6527c79a95536bd77ea\`. Main untouched. No new accepted GF(5) six-incidence proof, no Branch A/B, no ASET exponent.

## Original geometric setup

Let s=2^h, V=(s+1)(s²+1), a minimal such that binom(a,2)>=V. f maps EVERY ORIGINAL GQ point to a different unordered physical pair from K_a; g independently maps EVERY ORIGINAL GQ line to a different unordered pair. True ORIGINAL source incidences (p,ell) are retained with BOTH physical Kikuchi diagonals.

Work only in a coherent paired G* satisfying EICE-002 physical properties: two side-specific coordinate bicolorings (every edge switches both colors), and injective left/right neighbor coordinates at every physical vertex. Thus all oriented physical nonbacktracking 3-paths are coordinate-proper. For an oriented MIDDLE physical edge u→v set A=N(u)\{v}, B=N(v)\{u}, r=|A|, c=|B|. Every actual cell (w,z)∈A×B is an oriented physical NB3 path w-u-v-z, with first and final physical coordinates (x(w),y(w)),(x(z),y(z)). Both original physical pair decoders may or may not exist.

## E1 — exact double K_2,2 ORIGINAL source plaquette

Choose distinct w0,w1∈A and distinct z0,z1∈B. The four paths w_i-u-v-z_j form a **physical 2×2 plaquette**. Side-specific cuts force x(w_i) to have the opposite color to x(z_j); neighbor uniqueness forces x(w0) != x(w1) and x(z0) != x(z1), with all four labels distinct. Hence the four left physical endpoint pairs

    { x(w_i), x(z_j) },  i,j∈{0,1}

form precisely the edges of a physical K_{2,2} (simple C4). Duality gives a separate physical K_{2,2} on the four right coordinates y(w_i),y(z_j).

If ALL four cells decode actual source labels, the left original source IDs q00,q01,q10,q11 are four DISTINCT GQ points whose global f-images form the first K2,2, and the right source IDs r00,r01,r10,r11 are four DISTINCT GQ lines whose g-images form the second K2,2. This is a strictly source-aware statement: it does **NOT** identify adjacent physical edges with adjacent ORIGINAL GQ incidences and does **NOT** form a positive original GF(5) sixset.

## E2 — girth-eight bound on the 4×4 TRUE original incidence submatrix

For any four DISTINCT true GQ points Q={q00,q01,q10,q11} and any four DISTINCT true GQ lines R={r00,r01,r10,r11}, form the genuine 4×4 ORIGINAL incidence matrix J[i,j]=1[q_i incident r_j]. The incidence graph of W(3,s) has girth 8: it contains NO cycles of lengths 4 or 6. On just 4+4 vertices a bipartite graph with >=9 edges must have a cycle (a forest has <=7 edges). Since its shortest allowable cycle has length 8, that cycle uses ALL 8 vertices. Every ninth edge is a chord of the 8-cycle and creates a 4- or 6-cycle. Contradiction. Hence exactly and universally,

    sum_(q∈Q,r∈R) 1[q incident r] <=8,      (E2)
    # true ORIGINAL nonincident cross (q,r) >=8.

This cap is SHARP: an original GQ C8 gives four points and four lines with exactly eight original incidences. TRUE W(3,2) and an independent 2^16 bipartite-matrix exhaustive falsifier verify this. The C4-free condition ALONE only gives maximum 9 edges; both forbidden cycle lengths are essential.

Each ORIGINAL nonincident *cross* pair (q_i,r_j) admits the unique GQ projection q_i--ell--p--r_j. However it need NOT correspond to a physical NB3 path with those endpoints in the SAME rectangle; it need not be end-clean, unblocked, or positive GF(5). In particular E2 is NOT a covert source-motif compensation lemma.

## E3 — robust plaquette completeness from minimal physical alphabet

Each globally injected side misses only

    u=binom(a,2)-V,       0<=u<a-1=O(s^(3/2))

physical pair labels. By E1's injectivity on the whole r×c rectangle, at most u cells lack the left original point q and at most u lack right original line r; therefore at most m<=2u cells lack one of the original endpoints (EICE-003-D D5).

Let Q=binom(r,2)*binom(c,2) be the total number of physical 2×2 plaquettes for this oriented middle edge, requiring r,c>=2. Every missing cell appears in precisely (r-1)(c-1) plaquettes. Union bound gives a new **all-h local quartic-original-closure inequality**

    # fully original-endpoint-decoded plaquettes
      >= Q - m*(r-1)*(c-1)
      >= Q - 2u*(r-1)*(c-1),

and after dividing by Q,

    fraction fully ORIGINAL decoded
       >= max(0, 1-8u/(r*c)).                     (E3)

In particular on a high-degree EICE-002 G* with d_min>=3, r*c >= (d_min-1)^2, giving 1-O(s^(-1/2)) locally and for each of the following probability samplers.

The exact number of four-corner fully labeled plaquettes in any boolean grid is also

    sum_{0<=i<j<r} binom( |{k: cell(i,k) and cell(j,k) both labeled}|, 2).   (E3-EXACT)

This is a separate exact co-degree formula, tested independently against direct row/column quartet enumeration. The same formula also applies to cells satisfying *any* of the disjoint original source-status predicates: endpoint-defined, nonincident+end-clean, internally blocked, or unblocked.

## E4 — four-corner source-status amplification under a real NB3 law

Each true ORIGINAL physical NB3 cell falls into precisely ONE category:
0. one or both original endpoint labels absent;
1. endpoints exist but the true original point q lies on the true original line r;
2. endpoints nonincident but the unique ORIGINAL GQ anchor is end-dirty;
3. endpoints nonincident, anchor end-clean, but internally source-blocked;
4. endpoints nonincident, anchor end-clean and internally unblocked.

These cases are mutually exclusive and exhaustive. Category 4 corresponds to the previously known synchronized B/B-overlap source closure from PR #394, not a new 7-family theorem. Category 3 has the TRUE ORIGINAL GQ source-midpoint block predicate of EICE-003-C.

Define a **probability sampler on 2×2 plaquettes**: choose an oriented middle physical edge UNIFORMLY among those with r,c>=2; choose a two-element subset of A and a two-element subset of B uniformly; obtain the physical 2×2 grid. Select an additional random corner uniformly. That corner is an EXACT uniformly random cell of its middle rectangle. Define epsilon_missing, epsilon_eligible, epsilon_blocked as the corresponding single-cell probabilities.

By a four-event union bound the sampler satisfies, with no independence between corners,

    Pr[all four ORIGINAL endpoints defined]
       >= max(0,1-4*epsilon_missing),

    Pr[all four paths ORIGINAL nonincident/end-clean]
       >= max(0,4*epsilon_eligible-3),

    Pr[all four paths ORIGINAL internally blocked]
       >= max(0,4*epsilon_blocked-3).              (E4)

The probability measure here samples the oriented middle edge uniformly, NOT a globally uniformly sampled plaquette (which would size-bias high-degree middle edges). The implementation keeps these distributions separate and FAILS CLOSED if any claimed E4 lower bound mixes them.

For genuinely stationary NB3 on G* with active d_min>=3, **every oriented middle edge supports squares**, so the single-cell marginal of this sampler equals the genuine stationary original NB3 distribution from EICE-003-D. Hence

    Pr[all four internally blocked] >= max(0,4*theta_I-3).

Thus if a hypothetical S=o(s^6) forces theta_I=1-o(1) by a SEPARATELY ACCEPTED complete version of Opus theorem R, then under the valid high-degree EICE-002 regularizer, a 1-o(1) proportion of source plaquette samples consists of FOUR simultaneously internally blocked *genuine ORIGINAL endpoint paths*. This is a structural **necessary** condition for a counterexample, NOT a contradiction. It may give a promising input for JPKC-014 coherent source assignment / multi-anchor overlap and GF(5) accepted sixsets.

## E5 — geometrically meaningful no-go and precise next proof gate

Neither E2 nor E4 implies that the ORIGINAL cross pairs (q_ij,r_kl) appear as actual endpoints of a path. E2 only guarantees their unique source projections, and the four **diagonal** actual paths may be all blocked. An argument that '>=8 nonincident cross anchors -> >=8 newly positive sixsets' would be INVALID, repeating the physical-vs-original adjacency confusion identified in JPKC-004 J11–J13 and JPKC-005 J17.

The missing theorem for **EICE-003-F** is now specific: show that, among 2×2 plaquettes with all four actual original end-clean NB3 paths internally blocked, the configuration of their four ORIGINAL GQ anchor pairs and the common true original middle incidence **forces either** a quantitatively bounded count of such plaquettes **or** a bounded-multiplicity injection/compensation into the seven permitted positive ORIGINAL GF(5) source sixsets. Any compensation must account for all ORIGINAL incidence IDs, double diagonals, accepted checksum and exact duplication multiplicity. Current E1–E4 do NOT resolve this.

## Executable tests and provenance

- \`research/hyp105_issue230_source_plaquettes.py\`: exact Fraction true original status of every physical NB3 path, true q/r decode, true GQ unique projection, true source-midpoint internal block, actual coordinate K2,2, E2 original 4×4 incidence girth, exact co-degree plaquette formulas, and independent brute-force full enumeration under explicit budgets.
- \`research/test_hyp105_issue230_source_plaquettes.py\`: genuine W(3,2) lex/reverse/S68/S72 and W(3,4) lex/random paired coherent source IDs, independent NB3 source status vs EICE-003-D, original C8 tightness in true W(3,2), separate exhaustive 2^16 source 4×4 matrices (including C4-free max 9 vs true girth8 max 8), and negative input/path/cut tests.
- \`docs/research/HYP-105-ISSUE230-EICE003E-PLAQUETTE-GEOMETRIES.md\`: mathematical proofs, all-h scopes and next falsifier gate.
- \`.github/workflows/hyp105-issue230-eice003e.yml\`: single focused GitHub-hosted \`ubuntu-latest\` independent source/geometry test; all parent checks remain separate.

**Acceptance:** E1–E4 are exact all-h ORIGINAL geometric/combinatorial consequences under the explicit paired coherent graph assumptions. Neither the finite experiments nor these identities establish the needed universal source-anchored blocking gap or ASET theorem. Keep PR DRAFT, main unchanged, root HYP-105 issue #230 OPEN.
