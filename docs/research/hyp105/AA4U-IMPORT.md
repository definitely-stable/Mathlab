# HYP-105 — AA4-U original six-forest source and nine-cell transportation import

Research source: [PR #486](https://github.com/definitely-stable/Mathlab/pull/486), exact pinned original commit `f49dcef044e8a4f1bb17f080ffa11c7b365a077a`. Scientific root [issue #230](https://github.com/definitely-stable/Mathlab/issues/230) remains OPEN; [research infrastructure #474](https://github.com/definitely-stable/Mathlab/issues/474) is separate.

## I. All-h genuine source-topology statement

For every genuine original W(3,s), s=2^h, h>=1, an actual six-DISTINCT-incidence-ID set Q is a forest in the ORIGINAL point-line incidence graph, because the host GQ has girth 8. If BOTH original endpoint multiplicity profiles are in A=(1^6), B=(2,1^4), C=(2^3), the source forest is a disjoint union of paths, partitioned into exactly nine eligible cells:

| Original source cell | Genuine original path lengths |
|---|---|
| A/A | (1,1,1,1,1,1) |
| A/B, B/A | (2,1,1,1,1) |
| A/C, C/A | (2,2,2) |
| B/C, C/B | (4,2) |
| B/B overlap | (3,1,1,1) |
| B/B disjoint | (2,2,1,1) |

C/C is impossible by original GQ girth. Original sixsets outside the two-sided A/B/C admissibility filter remain outside the nine-cell table; this is NOT a ten-type partition of every original source sixset. These are source topology facts, not physical acceptance claims.

## II. Deterministic nine-cell relaxed transportation lower

Let `U_F` be the entire **source-only** universe of actual six-distinct-original-incidence-ID subsets in eligible cell F; `L_F(f)` and `R_F(g)` are its physically valid one-sided halves, built from ONE complete typed globally injected f and ONE complete typed globally injected g. For each eligible cell, using the SAME original sixset IDs,

\[
X_F(f,g)=|L_F(f)\cap R_F(g)|\ge
\max\{0,\,|L_F(f)|+|R_F(g)|-|U_F|\}.
\]

Summing the floors over the eight non-AA cells gives a valid lower for the non-AA accepted original sixset population; as an **abstract unrestricted subset-transportation relaxation** the floor is tight. This is not a claim that corresponding extremal subsets can be realized by any legal complete pair of physical-label injections. AA needs SAME original-column physically aligned connected D6 (the previously registered 60-position tensor), so no positive D6 floor follows from a coarse A/A marginal intersection count.

The result is an explicit method limitation: a zero relaxed bound neither proves that the true intersection vanishes nor disproves the simultaneous all-(f,g) HYP-105 conjecture.

## III. Exhaustive true W32 original source universe — FINITE only

The original research PR enumerated all \(\binom{45}{6}=8\,145\,060\) genuine original W(3,2) six-incidence-ID subsets, independent of f and g. The eligible nine-cell source universe is:

| Source cell | Eligible Q |
|---|---:|
| A/A | 1,566,360 |
| A/B | 1,666,980 |
| B/A | 1,666,980 |
| A/C | 6,225 |
| C/A | 6,225 |
| B/C | 5,220 |
| C/B | 5,220 |
| B/B overlap | 910,080 |
| B/B disjoint | 707,580 |
| **Nine eligible cells** | **6,540,870** |
| **Outside A/B/C eligible grid** | **1,604,190** |

Do not confuse these source-only counts with the far smaller physical one-sided populations (A=51,030, B=10,935, C=405). The finite 8,145,060-source enumeration remains the ORIGINAL research oracle; the import separately checks shape identities, independent hash pins and arithmetic but does not falsely claim to rerun the full original census.

For two coherent original W32 complete K6 map pairs S68 and S72, the exact joined source-cell counts are:

| Forest cell | Actual S68 physical joint | Actual S72 physical joint |
|---|---:|---:|
| A/A | 263 | 286 |
| A/B | 21 | 31 |
| B/A | 44 | 36 |
| A/C | 0 | 0 |
| C/A | 0 | 2 |
| B/C | 0 | 0 |
| C/B | 0 | 0 |
| B/B overlap | 2 | 1 |
| B/B disjoint | 1 | 2 |
| **All nine physically joined** | **331** | **358** |
| **Aligned D6** | **0** | **0** |
| **Accepted seven-GF5 original S** | **68** | **72** |
| **Nine-cell relaxed non-AA Fréchet bound** | **0** | **0** |

Crucial: positive actual S=68 or 72 coexists with a ZERO coarse relaxed marginal lower. This is NOT a globally injective zero-S counterexample, not an infinite family, and not a proof of root Branch A or B.

## IV. Immutable scientific provenance and reproducibility

Recorded independent source metadata: `DOCUMENTED_IN_DRAFT` / `NOT_REVIEWED` / `NOT_ASSESSED` / `ROOT_BRANCHES_OPEN`.

- Four distinct source-pinned claims: `HYP105-AA4U-NINE-ORIGINAL-FOREST`; `HYP105-AA4U-FOREST-FRECHET-LOWER`; `HYP105-AA4U-W32-NINE-FOREST-CENSUS`; `HYP105-AA4U-W32-ZERO-MARGINAL-POSITIVE-JOINT`.
- Three byte-for-byte original source Git blobs under `research/rcp/hyp105/archive/PR486/`, each checked against PR #486 original Git blob SHA-1 and separately pinned SHA-256. Receipt: `HYP105-EV-AA4U`.
- Separate negative knowledge: `HYP105-NG-AA4U-NINE-FOREST-MARGINAL-NOT-MINIMAX`, explicitly preserving possible higher-order original-incidence physical coupling methods.
- Five scoped formulas ` HYP105-F-022 ` through ` HYP105-F-026 ` are derived into the five versioned Markdown registers under `docs/research/hyp105/registry/`.

Reproducible import gates:

~~~bash
python -m unittest research.test_rcp_aa4u_import -v
python -m research.rcp.claim_registry --verify-sources
python -m research.rcp.evidence_ledger --verify-originals
python -m research.rcp.structured_docs --check
~~~

Original source PR #486 is still an independent scientific Draft, **not merged or declared mathematically peer-reviewed** by the infrastructure import. The root issue #230 stays open.
