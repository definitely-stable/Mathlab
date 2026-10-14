# HYP-105 / #230 — JPKC-012 direct ORIGINAL six-factor incidence tensor

**14 October 2026 — research-only Draft; strict child of JPKC-011 PR #442 at exact base HEAD `5610246a0407a74d4f71c22bc53f01ac424f3740`. Do not change or merge `main`. Root A/B OPEN.**

## 1. Why no more proper physical P3-based charging

JPKC-011 full true-original W32 confirmed 63/68 S68 and 66/72 S72 positive ORIGINAL six-incidence Q have **NO** coordinate-proper synchronized physical P3; this includes 41/19 and 33/28 true B/A and A/B wedges, so the issue is not restricted to C-half topology. A proof method that **requires** a proper P3 cannot count those sixsets. JPKC-012 removes that gate entirely and works with the six *actual ORIGINAL incidence ID* factors Q and a single original globally injective physical factor labeling f,g.

## 2. Exact-cover source enumeration, independent of historical W32 sixset generator

A physical left six-coordinate 2-regular multigraph with six physical edges is a degree-two exact cover. On the W32 K6 alphabet its complete edge-multiset decomposition has:
- 70 simple physical 2-factors (source A; 6 distinct ORIGINAL left points);
- 45 doubled edge plus simple C4 (source B; one original point used twice);
- 15 three-doubled-edge perfect matchings (source C; three original points each used twice).

Every physical edge is the unique globally injected ORIGINAL point label. For multiplicity one choose one genuine original incident line (3 choices); for multiplicity two choose two distinct genuine original incidences (3 choices). The source-factor incidence expansion gives exactly

`70*3^6 + 45*C(3,2)*3^4 + 15*C(3,2)^3 = 51,030 + 10,935 + 405 = 62,370`

distinct ORIGINAL Q with a left 2-regular physical six-coordinate projection. The new implementation enumerates the 130 physical *multigraph exact covers by recursive degree deficits*, not by importing the historical cycle/C4/matching enumerator. Every actual original Q is deduplicated by six incidence IDs. No physical P3 or common-right-image proxy is queried.

The 130 and 62,370 counts are special finite W32 K6 identities. For all h the exact coefficient identity applies, but these numbers and the implementation do not extend to a full W34 census.

## 3. J41 — all-h non-D6 direct right-original-factor profile contraction

Fix a genuine original host W(3,s), a globally injective original left pair labeling f, and the set `L_f` of all original six-incidence Q whose LEFT physical projection is exactly six degree-two physical coordinates. For each Q let `m(Q)` be the **ORIGINAL right line factor multiset**, retaining multiplicities. Define

`T_{alpha,m,o}(f) = #{Q in L_f: left original multiplicity type alpha in {A,B,C}, right line multiset m, source B/B overlap indicator o}`

where `o` is needed only for B/B and is 0 or 1 by original simple incidence uniqueness. This is an exact **nonnegative integer source incidence tensor**, calculated once using f and genuine ORIGINAL incidences and independent of g.

For each legal complete globally injective g, define `H_beta(m;g)` as the indicator that right ORIGINAL line profile m has multiplicity type beta in {A,B,C} and the corresponding physical six-edge projection is 2-regular on exactly six physical symbols. **This depends only on m and g**, not on which Q with right line profile m was used.

For the six classes apart from D6, the exact original GF5-necessary selected sixset count is

`S_nonD6(f,g) = sum_{alpha,m,o} T_{alpha,m,o}(f) * H_{beta}(m;g) * ClassSelector(alpha,beta,o)`

with appropriate class selectors:
`(A,B)->A-left/B-right`, `(B,A)->B-left/A-right`, `(A,C)/(C,A)->C/A`, `(B,C)/(C,B)->C/B`, `(B,B)->B/B-overlap/disjoint`. Every original Q contributes at most once. This is an **all-h exact factorization**, not a uniform strictly positive lower bound.

The factorization lets one evaluate many legal g maps without reconstructing per-Q original incidences or physical P3 witnesses. It does not declare distinct right source profiles probabilistically independent: all profiles are evaluated on the SAME globally injected complete g.

## 4. J42 — D6 exact named ORIGINAL right-line positional dual

(A,A) is special: both physical halves have six distinct ORIGINAL factors, yet GF5 D6 requires **the same connected physical six-column cycle**, not merely two physical 2-factors. This cannot be reconstructed from only original line multiset m or a Hall feasibility flag.

For each Q with source types (A,A), normalize each physical LEFT coordinate's two ORIGINAL incidence-column positions by their actual original RIGHT line IDs. The six resulting unordered pairs of named right lines define the **left six-line dual** `D_f(Q)`, independent of a six-column sort convention. Build an additional sparse nonnegative integer tensor

`T^D_{R,D}(f) = #{Q in L_f: six distinct ORIGINAL right lines R, normalized left dual D_f(Q)=D}`.

On the SAME g, compute `D_g(R)` by listing, for each of the six physical RIGHT coordinates, the two ORIGINAL line IDs touching it. Then

`S_D6(f,g) = sum_{R,D} T^D_{R,D}(f) * 1{D_g(R)=D and D is a single connected 6-cycle}`.

This preserves positional information exactly and avoids falsely treating any two six-coordinate cycles as aligned. The right line labels are global and shared across all Q. J42 is an exact all-h algebraic contraction; accepted W32 full historical independent GF5 seven-class oracle checks it.

## 5. J43 — conditional globally coherent source-profile minimax

For the same pinned original S68/S72 W32 four-ORIGINAL-right-line blocks as D6-AA4-B, the complete legal K6 factor assignment fiber has exactly 24 globally injected mappings. Compile `T(f)` ONCE; for each g in the true fiber evaluate all original right source profiles and D6 duals. Let `S_m(g)>=0` be the total positive original sixset contribution from profile m, including its D6 positional refinement.

By exact double counting and finite common-global-state minimization:

`min_{g in F} sum_m S_m(g) >= sum_m min_{g in F} S_m(g)`.

The nonnegative *source-profile coherence gap* measures how much independently favorable choices of g on individual profiles are incompatible with any ONE globally legal g. This is a conditional identity, not evidence of an all-h uniform gap. Unlike an arbitrary Q-local free-label optimization, each physical right factor is shared across all its original occurrences. Every one of the 24 states is compared to an INDEPENDENT historical `seven_census`, class by class. No W34 full positive original census and no new R3/ASET exponent.

## 6. Acceptance & next research blocker

Four files: `research/hyp105_issue230_jpkc012_incidence_tensor.py`, five fail-closed tests, this note, dedicated GitHub-hosted workflow with W32 full four-map exact oracle and two independently pinned 24-global-map matrix jobs. Exact final-HEAD dedicated + INDEX + Proof Audit + full Research all SUCCESS and independent math review required. Source input injection errors, missing maps, W34 full attempts, budget overflows and incomplete fibers fail closed.

**Open nontrivial question:** can genuine W(3,s) original incidence/physical capacity enforce a universal positive lower bound on this direct right-factor profile tensor contraction, or on its connected D6 dual sector, under all globally injective f,g? The exact factorization alone neither proves `S_s=Omega(s^6)` nor supplies an infinite correlated counterexample. It is a better algebraic object for a global positivity inequality than a graph of proper P3 demands.

## 7. Exact GitHub-hosted original tensor results

The initial dedicated original tensor run completed all five exact tests and both 24-state global right-factor matrix jobs successfully. The compiler counts ORIGINAL left physical 2-regular incidence candidates **without importing historical left generator or any proper-P3 condition**. Each six-source factor tensor contraction matched the independent previously accepted fixed-map `seven_census` exactly, by all seven classes and GF5 necessary weights.

| Genuine W32 original global map | Original left Q candidates | Distinct right ORIGINAL line multiset profiles | Sparse non-D6 profile rows | Named A/A positional D6 dual rows | Exact seven-S |
|---|---:|---:|---:|---:|---:|
| lex | 62,370 | 21,950 | 29,523 | 20,317 | 259 |
| reverse | 62,370 | 21,950 | 29,523 | 20,317 | 169 |
| S68 | 62,370 | 17,890 | 25,032 | 21,369 | 68 |
| S72 | 62,370 | 17,890 | 25,032 | 21,369 | 72 |

Distinct right source profiles share true ORIGINAL line factors. The source tensor is sparse compared with individually named Q, yet still retains enough positional structure in A/A to recover exact D6, and cannot be replaced by independent right profile assignments.

**J43 coherent original profile gap over ALL 24 true four-line globally injected right-map states:**

| Pinned complete W32 source block fiber | Independent source-profile count minima summed | Coherent minimum of full seven-S | **Exact profile coherence gap** |
|---|---:|---:|---:|
| S68 | **11** | **68** | **57** |
| S72 | **0** | **68** | **68** |

This is a direct **ORIGINAL right-factor-profile** coupling, not a source P3 matching Hall proxy. In particular, the zero independent S72 profile-min sum does NOT produce a globally legal zero-positive map; all 24 complete legally injected states have S≥68. This is a fixed finite fiber result, not any asymptotic theorem or universal bound over all f,g.

The compiler now additionally emits a deterministic non-optimal greedy **source profile coverage certificate**: each listed original right-line multiset profile is positive on an exact bitmask of 24 complete globally legal states. The union of these bitmasks must cover all 24 states. Its length is a reproducible sufficient cover, NOT a proven minimum cover size. An individually unavoidable profile is separately counted using full 24-state masks. This makes nonzero coherent positivity auditable at the source-profile layer without reciting all accepted Q.

Do not claim J41/J42 as a newly discovered GF5 lower-bound theorem: they are exact structural decompositions of the existing accepted seven-family class definitions. A future proof requires a NONTRIVIAL bound on this tensor contraction over **all** admissible global maps, beyond the finite 24-state fiber.
