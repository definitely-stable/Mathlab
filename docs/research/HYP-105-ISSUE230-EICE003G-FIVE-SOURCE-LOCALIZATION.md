# HYP-105 #230 — EICE-003-G: complete original five-incidence localization and exhaustive local counterwitness search

**Scope and acceptance: RESTRICTED_THEOREM_G / OPEN_WITH_FORMAL_BLOCKER.** Research-only strict child of fully green [Draft PR #461](https://github.com/definitely-stable/Mathlab/pull/461) pinned at \`e1c6a8a80e278112b5b70636db2d30e8c7ca0830\`. No changes to main, no merge, no Branch A/B, no ASET claim. In particular, a finite W32/W34 no-witness scan cannot prove a universal all-h forbidden configuration theorem.

## G1 — all-h exact five-ORIGINAL-incidence localization

For the genuine original W(3,s), globally injective original point/line maps f,g, and any *coherent* physical G* retaining both diagonals of each chosen original incidence, fix a genuine all-four-end-clean and internally blocked 2×2 physical NB3 plaquette. Its four physical paths have one oriented middle physical edge \`u→v\`, two distinct outside neighbors \`w0,w1\` at u, and two \`z0,z1\` at v:

    (w_i,u,v,z_j),  i,j∈{0,1}.

The physical edges in these four 3-paths are **exactly five**: \`{u,v}, {u,w0}, {u,w1}, {v,z0}, {v,z1}\`. Each physical edge has exactly one TRUE original source incidence ID under the global f,g injection. Moreover these five IDs are **different**. An original (p,l) has two vertex-disjoint physical diagonals, so source repetitions cannot occur among edges sharing u or among those sharing v, nor between the middle edge and an arm. The only remaining possible repetition would pair one u-arm (u,w_i) with one disjoint v-arm (v,z_j); their ORIGINAL point physical labels would then satisfy f(p)={x(u),x(w_i)}={x(v),x(z_j)}. But the NB3 path w_i-u-v-z_j is coordinate-proper, so its four x-coordinates are distinct, a contradiction. Thus all five source IDs are distinct, including across opposite arms (checked explicitly in CI).

Take the **paired source restriction** consisting of these five true original incidences and **BOTH** their physical diagonals. It still satisfies:
- both globally fixed physical coordinate cuts used by G*;
- all local unique-neighbor left/right coordinate constraints (edge deletion cannot introduce a cherry);
- the same actual four paths, their original endpoint q_ij,r_ij, their true unique GQ anchor q_ij--ell_ij--p_ij--r_ij, and their true middle source e=(p2,l2);
- therefore exactly the same L/R/B internal blocker masks and all-four-blocked status.

No globally uniform Ω(s⁴) density or Ω(s) degree is required for the **restricted 5-source witness**. Leaves outside the actual paths are irrelevant to the pointwise geometric identity.

**G1 all-h equivalence:** a globally injected original f,g can admit an all-four-blocked square in some coherent paired subgraph only if its **complete** physical Kikuchi graph contains an oriented five-edge 2×2 rectangle whose source IDs form a locally coherent five-original-incidence paired subgraph and whose four TRUE endpoints are coordinate proper, nonincident, end-clean, and internally blocked. Conversely each such locally coherent five-source witness itself gives a valid coherent paired subgraph with an all-four-blocked square, though not necessarily with the all-h density/min-degree certificate.

This is stronger and more falsifiable than searching just the small canonical EICE-002 G*, which can have no square at s=2. It is a **localization equivalence**, not a positive GF5 sixset or full Branch A proof.

## G2 — finite exact ORIGINAL physical source search, fail closed

Given ONE complete true original W32 or W34 global map:
1. Enumerate ALL oriented true physical middle edges in the **complete** Kikuchi graph (not in just the canonical G*).
2. For both exterior-neighbor sets, inspect EVERY physically coordinate-proper outer cell; decode TRUE original point and line labels; verify q not incident r; compute the unique ORIGINAL GQ anchor and its end-clean status.
3. Compute both TRUE original anchor-to-middle-source physical label intersections. A cell is internally blocked iff at least one of the two typed masks is 1.
4. For every pair of rows and pair of columns yielding four genuine end-clean internally blocked corners, recover the exact FIVE physical edge source IDs and reject source coincidences.
5. Require both complete source-coordinate bicolorings and strict no-left/no-right-cherry constraints after retaining **both** diagonals of each of the five source incidences. Do NOT accept an arbitrary four-path collection that cannot be realized as a coherent paired subgraph.
6. If a witness remains, independently construct that true five-source graph and run the existing EICE-003-F \`FourAnchorCapacity\` oracle; assert a genuine all-four-blocked square, 4 original points, 4 original lines, exact source GQ anchors and the valid L/R/B mask channel. Persist all original IDs.
7. If none remains AND the complete finite middle-edge/cell/candidate budgets were not exhausted, record a **finite NO-GO for that single original global map only**. Never generalize to every W32 map, every s, or all injective labels.

The search also reports the count of raw four-blocked physical rectangles **before** enforcing the five-source local coherence, and keeps the distribution of adjacent-sharing versus strict checkerboard source blockers. This identifies whether the actual barrier is source geometry or the physical cherry/cut constraints. Frozen W32 lex/reverse/S68/S72, W34 lex/random, plus eight deterministic truly globally injected W32 right-label shuffled models are scanned on GitHub-hosted Linux; all search budgets fail closed.

## G3 — conditional source-finite forbidden template implies a quantitative gap

Let H be ANY actual high-degree coherent paired physical G*, with min active degree d_*>=3, and let θ_I be its genuine stationary true ORIGINAL end-clean internal-blocking mass. F6 established from standard C4 homomorphism CS and Jensen (not a novel inequality):

    Pr_uniform-oriented-physical-middle-and-uniform-2×2 [
        all four ORIGINAL paths end-clean and internally blocked]
       >= max(0, θ_I^4 - 2/(d_*-1)).

If, for the SAME COMPLETE original f,g map, the G1 five-source search has established that **no locally coherent all-four-blocked five-incidence template exists ANYWHERE in the complete source**, then no coherent paired G* can have such a square. The probability on the left equals 0, so

    θ_I^4 <= 2/(d_*-1),
    θ_I <= (2/(d_*-1))^(1/4).                    (G3)

In particular if a FOR-ALL-H theorem could prohibit the true original five-source blocked template for EVERY globally injected original f,g, then EICE-002 d_*>=δs yields \`θ_I=O(s^-1/4)\`, a very strong true internal-blocking contraction. Combined with separately required correctness/completeness of the Opus R root compensation theorem, this would be a plausible Branch A completion route.

**But universal prohibition is OPEN.** A single genuine five-source witness in any finite W32/W34 map refutes the universal forbidden-template route; it does NOT refute the root S=Ω(s⁶), since the counterexample may still have many positive original motifs. Conversely finite NO-GO only applies to tested frozen maps.

## G4 — why mere source scope or arbitrary blocked tensors is insufficient

The earlier C5 abstract midpoint coupling ignores genuine physical path realizability; G1–G2 refuse this. EICE-003-F only established a <=17-original-incidence **footprint** for four true corner anchors and two blocker channels; it never guaranteed an accepted positive six-ID GF5 motif. A finite G2 witness must preserve genuine TRUE original point/line IDs, true source edge IDs, the unique anchors and end-clean mask. Its local five-source graph is not assumed asymptotically dense, and no inference is made from a physical K2,2 or eight nonincident GQ cross pairs to a positive original GF5 sixset.

**Next rigorous proof gate:** determine whether G2 discovers genuine locally coherent all-four-blocked source witnesses. If yes, abandon blanket universal local forbidden template and investigate how many can coexist inside high-degree G*; prove a density/tradeoff or an actual accepted GF5 sixset compensation with bounded multiplicity O(s²). If none is found in only the finitely tested maps, expand structured global original label families and seek a *mathematical universal* impossibility argument, not a CI extrapolation. The accepted seven-GF5 frozen K6 classifier must NOT run on W34 without a separately formalized generalization.

## Artifacts

- \`research/hyp105_issue230_five_source_blocked_search.py\`: exact five-original-source localization, exhaustive true complete-graph physical midpoint search, local coherent paired source certificate, true GQ endpoint and anchor masks, independently validated witness, and exact rational G3 conditional fourth-power upper.
- \`research/test_hyp105_issue230_five_source_blocked_search.py\`: true original four W32 frozen global maps, W34 lex/random, eight deterministic W32 globally injective right-label perturbations, real five-source complete endpoint square witness, fail-closed input/budgets, and G3 exact rational arithmetic.
- \`docs/research/HYP-105-ISSUE230-EICE003G-FIVE-SOURCE-LOCALIZATION.md\`: this theorem, limitations and search gates.
- \`.github/workflows/hyp105-issue230-eice003g.yml\`: GitHub-hosted Linux-only tests and the complete finite search report; no user PC or self-hosted runners.

**Research acceptance:** all-h localization theorem proved as elementary physical/original source geometry. G3 is a valid conditional estimate. A numeric CI is an independent falsifier, not a universal theorem. HYP-105 root OPEN; keep Draft.
