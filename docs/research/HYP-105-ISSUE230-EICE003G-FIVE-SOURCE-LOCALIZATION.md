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

The search also reports the count of raw four-blocked physical rectangles **before** enforcing the five-source local coherence, the number of distinct TRUE original five-incidence source subsets and its maximum exact oriented-square multiplicity (audited <=20), and the distribution of adjacent-sharing versus strict checkerboard source blockers. This identifies whether the actual barrier is source geometry or the physical cherry/cut constraints. Frozen W32 lex/reverse/S68/S72, W34 lex/random, plus eight deterministic truly globally injected W32 right-label shuffled models are scanned on GitHub-hosted Linux; all search budgets fail closed.

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

## G4 — NEW all-h ≤20 oriented-squares-per-five-original-source-set packing

Retain the SAME legitimate TRUE coherent paired-diagonal G* and a fixed UNORDERED set \`F={e0,e1,e2,e3,e4}\` of exactly FIVE distinct original source incidence IDs. The restriction to F has exactly TWO physical diagonal edges per source, hence exactly 10 undirected physical edges and 20 oriented physical candidate middle edges.

Fix ONE of these 20 oriented middle physical edges \`u→v\`, owned by a source e∈F. For any coordinate-proper 2×2 plaquette with original-source set EXACTLY F, all four outside arms must be supplied by the four other source IDs. Each original source contributes two vertex-disjoint diagonal edges. Moreover the same original source cannot provide an arm at u AND an arm at v when \`u→v\` remains in a coherent graph: otherwise the constructed three-edge NB3 path using those two arms would have its first and last arm point-pair physically IDENTICAL, contradicting the requirement that all four left coordinates of every NB3 path are distinct. Thus each of the four other sources has at most one possible physical arm incident to {u,v}; if a 2×2 square with all five distinct sources exists, it consumes all four, so it is UNIQUE for this oriented middle edge.

Consequently every fixed five-original-incidence source set F supports at most

    # ORIENTED coherent all-four-blocked 2×2 plaquettes with source set F <=20.      (G4)

The upper is deliberately coarse, allowing the same physical square to be represented by reverse middle orientations. It depends on TRUE paired-diagonal provenance and coordinate-properness, NOT any GF5 classifier or arbitrary abstract five-edge graph.

In the EICE-002 high-degree all-h regime, F5+F6 already gives for the SAME globally injected f,g and SAME coherent G*:

    P4 >= [δ^4*s^8/1,280,000] *
          max(0,4*theta_I-3,theta_I^4-2/(δ*s-1))

oriented TRUE original all-four-blocked square occurrences for \`δ=10^-6\` and \`s=2^h>=4,000,000\`. Dividing by the ACTUAL all-h G4 upper multiplicity 20 establishes the unconditional-on-GF5, conditional-on-correct-G* **source-diversity lower bound**:

    # DISTINCT 5-ORIGINAL-incidence blocked source sets
      >= [δ^4*s^8/25,600,000] *
         max(0,4*theta_I-3,theta_I^4-2/(δ*s-1)).                (G4+F6)

If \`theta_I>=epsilon>0\` for fixed epsilon and sufficiently large s, there are \`Omega_epsilon(s^8)\` DISTINCT true ORIGINAL five-source blocked configurations, not merely s^8 physical representations of a handful of templates.

**This is a novel packing consequence in the present ORIGINAL-source counting setup, not a novel C4/Sidorenko inequality.** It still does not imply a single positive six-original-incidence GF5 source set. A possible proof route now is a true GQ geometric bound \`o(s^8)\` on the number of locally coherent all-blocked five-incidence sets for every complete global injection, or a bounded-preimage GF5 transfer from this diverse source reservoir. The W34 finite witnesses below prove a complete FORBIDDEN five-source theorem false, but do NOT refute a global \`o(s^8)\` abundance bound for large s.

## G5 — actual finite G2 results and falsified local-forbidden route

The GitHub-hosted finite complete-source census of REAL original global source maps (not an abstract transport or pseudomarginal) reports:
- W32 Lex: 180 oriented middle edges, 3966 outer path cells, 2 raw four-blocked physical 2×2 candidates, ZERO source-coherent five-incidence witnesses.
- W32 Reverse/S68/S72: 180 oriented middle edges each, respectively 3450/3104/3232 examined path cells, ZERO raw or coherent all-blocked source squares.
- W34 Lex: 1700 oriented middle edges, 133316 outer path cells, 2102 raw candidates, **934** coherent true original five-source allblocked oriented squares supported on **467 distinct five-original-incidence sets**. Of these 888 are adjacent-common-side and 46 are STRICT alternating checkerboards. Empirical maximum multiplicity per five-source set is **2**.
- W34 Random: 1700 oriented middle edges, 123382 outer path cells, 1930 raw candidates, **1150** coherent true original five-source allblocked oriented squares on **575 distinct five-original-incidence sets**. Of these 1072 are adjacent-common-side and 78 are STRICT checkerboards. Empirical maximum multiplicity per five-source set is **2**.

Each accepted W34 witness is independently constructed as its OWN five-genuine-source-incidence paired graph, checked for BOTH coordinate bicolorings and no-cherry constraints, with all four TRUE original q/r nonincident end-clean anchors internally blocked. One concrete W34 Lex witness uses original incidence IDs \`{10,26,45,126,206}\`, has middle original source ID \`10\`, oriented middle physical edge \`0→17\`, external first vertices \`52,90\`, last vertices \`142,163\`, and blocker mask \`RRRL\`. These are finite ACTUAL geometric counterexamples to a *universally forbidden five-source four-blocked configuration*, not counterexamples to the root Branch A lower bound or proofs of any positive six-incidence family.

Both W34 configurations have empirical 2-to-1 oriented-square/five-source-set multiplicity, a much stronger FINITE observation than the proved ALL-h 20-to-1 bound; no improvement of the universal constant is claimed. The W34 random fixture also contains a nonzero number of strict checkerboards, independently falsifying the idea that one can eliminate the alternating channel purely by local GQ/paired-diagonal realizability. Both F2 channels survive the true source and physical geometry constraints.

## G6 — why mere source scope or arbitrary blocked tensors is insufficient

The earlier C5 abstract midpoint coupling ignores genuine physical path realizability; G1–G2 refuse this. EICE-003-F only established a <=17-original-incidence **footprint** for four true corner anchors and two blocker channels; it never guaranteed an accepted positive six-ID GF5 motif. A finite G2 witness must preserve genuine TRUE original point/line IDs, true source edge IDs, the unique anchors and end-clean mask. Its local five-source graph is not assumed asymptotically dense, and no inference is made from a physical K2,2 or eight nonincident GQ cross pairs to a positive original GF5 sixset.

**Next rigorous proof gate (EICE-003-H):** G2 FOUND abundant true W34 witnesses, including BOTH strict alternating and adjacent-common-side mask channels, so **ABANDON UNIVERSAL LOCAL FORBIDDANCE**. Investigate whether the number of DISTINCT blocked coherent TRUE original five-source incidence sets can be upper bounded by `o(s^8)` uniformly for all globally injected f,g, OR construct an all-h accepted seven-GF5 sixset transfer with the correct positive source multiplicity. Existing finite W32 no-go does NOT generalize. The accepted seven-GF5 frozen K6 classifier must NOT run on W34 without a separately formalized generalization.

## Artifacts

- \`research/hyp105_issue230_five_source_blocked_search.py\`: exact five-original-source localization, exhaustive true complete-graph physical midpoint search, local coherent paired source certificate, true GQ endpoint and anchor masks, independently validated witness, and exact rational G3 conditional fourth-power upper.
- \`research/test_hyp105_issue230_five_source_blocked_search.py\`: true original four W32 frozen global maps, W34 lex/random, eight deterministic W32 globally injective right-label perturbations, real five-source complete endpoint square witness, fail-closed input/budgets, and G3 exact rational arithmetic.
- \`docs/research/HYP-105-ISSUE230-EICE003G-FIVE-SOURCE-LOCALIZATION.md\`: this theorem, limitations and search gates.
- \`.github/workflows/hyp105-issue230-eice003g.yml\`: GitHub-hosted Linux-only tests and the complete finite search report; no user PC or self-hosted runners.

**Research acceptance:** all-h localization theorem proved as elementary physical/original source geometry. G3 is a valid conditional estimate. A numeric CI is an independent falsifier, not a universal theorem. HYP-105 root OPEN; keep Draft.
