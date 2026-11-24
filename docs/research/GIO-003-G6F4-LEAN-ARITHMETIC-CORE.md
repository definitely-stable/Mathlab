# GIO-003 G6-F4 — Lean 4 kernel-check of critical arithmetic in the G6-F3 source transfer

**Parent:** [G6-F3 Draft #819](https://github.com/definitely-stable/Mathlab/pull/819) exact SHA e3ac1e432c1b0d6c3d1df835c3ac417c0365c7b4. Parent specialist **25/25 SUCCESS**, INDEX SUCCESS, full Research **SUCCESS**. New G6-F4 is a SEPARATE stacked Draft. Do not merge ancestors, change main, or close issue #793.

## Scientific motivation and literature

An explicit source-conditional original six-ID T3 transfer is now written in [G6-F3 standalone manuscript](GIO-003-G6F3-STANDALONE-ORIGINAL-T3.md), but mathematical prose and independent finite tests are NOT kernel-checked universal proofs. The next step is genuine, initially SMALL-SCOPE Lean 4 formalization of high-risk algebraic bridges, with an honest formalization coverage table. The graph-supersaturation result in G6-F1 is a conservative explicit quantitative presentation of CLASSICAL Simonovits prior art, not a new even-cycle existence theorem; Jiang and Yepremyan, *Supersaturation of even linear cycles in linear hypergraphs*, CPC 29 (2020), 698–721, [DOI](https://doi.org/10.1017/S0963548320000206), also contains an r=2 ordinary-graph argument. The random-priority local-minimum independent set method is classical Caro–Wei. No claims of outside referee or independent Lean proof for T3 are made.

## Exact scope of new Lean 4 artifact

The independent pinned project lives in **formal/gio003_f4/** with a reproducible Lean 4 v4.34.0 and Mathlib v4.34.0 toolchain. GitHub-hosted CI on Ubuntu 24.04 uses the officially maintained **leanprover/lean-action@v1**, compiles the theorem source, re-runs the Lean kernel, prints the actual axiom dependencies of each theorem, rejects any source words sorry/admit/axiom and uploads the axiom audit. This is a **real proof checker** for the statements actually formalized, not a Python sample that calls itself Lean.

The proved theorems in formal/gio003_f4/Gio003F4.lean are intentionally separated from their still-external mathematical assumptions:

| Lean theorem | Universal statement it actually checks | Essential NOT-yet-formalized premise |
|---|---|---|
| sixth_walk_young | For any real u,c,d,m,e satisfying u²≤12c+6dum and m²=2e, proves u²≤24c+72ed² with exact factor **72** | the graph-theoretic injection of noninjective C6 walks and the Cauchy trace inequality |
| heavy_density_from_source | For ALL nonnegative real v,r and positive R, from v(RC0)³≤r³ and vr≤eR proves C0³v⁴≤e³ | existence of an actual simple HEAVY host F with the two premises |
| four_low_losses | Four real losses individually ≤epsilon*r6 imply total ≤4epsilon*r6 | combinatorial proof of each loss on real original source |
| four_low_losses_half | Exact substitution epsilon=w/8 gives total ≤(w/2)*r6 | same four original endpoint/book/return obligations |
| source_delta_pos | For ALL c0,R,w>0 gives min(c0/R⁶,w/4)>0 | obtaining positive real source parameters from source assumptions |
| heavy_or_low_obstruction | Under the source's heavy-or-low disjunction and D6,BBo≥0, yields D6+BBo≥delta*r6 | proof that actual source satisfies one alternative |
| low_core_fraction | For ALL J0≥0, 1−1/8−1/32−2J0/(16J0+2)>1/2 | original J and heavy-edge discard counting |
| six_original_flag_ids | Three distinct named FULL original flag IDs plus three distinct named CORE IDs, disjoint, have union cardinality exactly SIX | injective physical-to-original source inverse and actual owner disjointness |
| c6_regularization_fixed_integer_gates | Explicit 2^20≥9^6, 4·2^20≥9^4 and 2^40≥192·2^20 | G6-F1's full all-simple-graph density regularization induction |

**Important: formalization is deliberately NOT complete.** In particular no theorem in this PR states the full T3 conclusion from girth, Loewner W, or factor maps in Lean. The following central all-order graph/source inputs remain in the *mathematical manuscript only*: C1 original girth8/defect double count, typed PSD source j0/G0, Caro–Wei independent owner source choices, one GLOBAL uniform source owner priority and correlated simultaneous minima, global point/line bit cuts, source-first FULL/CORE BBo six-ID inverse, unique proper D6 physical sixcycle, trace6 combinatorial six-backtrack injection, matrix-moment Jensen, physical source-book triples, endpoint bad-mask and four bound inequalities. The F4 module proves the transformations **AFTER these stated premises**, never silently elevates those inputs to axioms named as if they were proved.

## Strict formal dependency & import map

**F1:** ordinary simple graph C6 numeric constant pair C0=2^41,c0=1/98304 (proved by the explicit source-independent paper and exact Python tests, NOT yet Lean-formalized as a full graph theorem).

**G6-C1/D7:** actual source girth≥8, quadratic Moore excess, two-typed local Loewner W gate, real/source-original missing-projection identity (mathematical proof, independently exact finite tests, NOT yet Lean-formalized).

**G6-F3:** all-order universal original source six-ID combinatorial transfer in 477-line manuscript: full/CORE mixed book, global owner priority and cuts, HEAVY/LOW, two reverse BBo orientation and shared sixth moment (mathematical proof, 25 Python tests on actual source and all 512 small bipartite hosts; NOT a Lean-formalized statement).

**G6-F4:** formal kernel proof for exactly nine universally quantified arithmetic/finite-set implications, no imported user axioms or sorries. This is a **meaningful first formalization milestone**, and a proof hygiene gate, not the proof's final certification.

## Independent verification and acceptance

A new GitHub-hosted Lean workflow at .github/workflows/gio003-g6f4-lean-kernel-core.yml pins the compiler and mathlib version, runs the compiled library and checker, prints original axioms for all nine theorems, explicitly checks that no sorry/admit/user-defined axiom occurs and uploads output as a standalone artifact. Acceptance requires this specialist **SUCCESS on exact final HEAD**, plus inherited INDEX and full Research **SUCCESS**, as well as a scoped separate mathematical review including exact formal statement coverage.

**STOP:** Preserve G6-F3/frozen parent, source stack as Draft, main unchanged, #793 OPEN. Full T3 still **source-conditional** and not formally verified, and dependent coefficient GF5 ASET remains open. Next substantive F5 proof priority after kernel partial success: formalize the universal original three-corner FULL/CORE source book injection or the joint ONE-global owner-priority conditional probability inequality (which needs genuine finite graph and probabilistic models), then the physical C6-to-original D6 inverse. This has substantially more mathematical content than merely checking numeric constants.
