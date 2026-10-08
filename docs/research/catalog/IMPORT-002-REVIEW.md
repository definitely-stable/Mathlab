# RESEARCH-INDEX-002 — source review and import decisions

Status: **CURATED IMPORT / REVIEW REQUIRED BEFORE CLAIM PROMOTION**  
Date: **2026-10-08**  
Tracking: [issue #27](https://github.com/definitely-stable/Mathlab/issues/27)  
Normative data: [registry.json](registry.json)  
Human index: [INDEX.md](INDEX.md) · [THEMES.md](THEMES.md)

## Snapshot and reproducibility

| Repository | Exact source SHA | New / total entries |
| --- | --- | ---: |
| Mathlab | `0c41da53d39aaeecc4f736ee063cc9f8bc4ff1d7` | 2 / 9 |
| DELSK / Shift-lab | `e1ee235fe08c7cc1f6e8ec8884b65439435adf92` | 6 / 12 |
| DeltaMeter | `862579643fb44bfd3df3b65a863bfdc90b998611` | 7 / 14 |
| openai/math | `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` | 8 / 14 |
| **Total** | | **23 / 49** |

Existing 26 record identities were preserved. Mathlab's namespace snapshot advanced to the verified current main commit; older paths were checked against the new revision and their pinned permalinks updated consistently. The other three sources remain pinned at the exact previously cataloged commit (also verified as their current `main` at import time). Updating a revision does **not** change whether a claim is proven or original.

## Inclusion criteria

Curate an external item only when it (a) affects a mathematical question, (b) changes a product-level decision, (c) records a reproducibility/provenance technique, or (d) provides a relevant exact, negative, or independently-auditable comparison. Do not import a paper simply because it appears in a collection. Do not equate `FOUND IN REPO` with `THEOREM VERIFIED`.

Every new entry was read from its indicated UTF-8 markdown/protocol path at the pinned snapshot. Source existence and record-level annotation were examined. The offline CI checks the catalog graph and formatting only; it does **not** verify external DOI resolvability, the completeness of each scientific argument, authorial peer review or machine-readable verification of an external proof.

## Import review by lane

### Mathlab — ML-008, ML-009

- [ML-008](INDEX.md#ml-008) imports [G2B-A finite evidence](https://github.com/definitely-stable/Mathlab/blob/0c41da53d39aaeecc4f736ee063cc9f8bc4ff1d7/docs/research/LENT-001-G2B-A-EVIDENCE.md). **(A_3^{set}(4,2,2)=7) is exact** in the frozen prime-field model; **(10le A_5^{set}(3,2,2)le15) is only a certified interval**. The GF(5) search hit its budget. No asymptotic theorem is inferred.
- [ML-009](INDEX.md#ml-009) imports the corresponding [protocol](https://github.com/definitely-stable/Mathlab/blob/0c41da53d39aaeecc4f736ee063cc9f8bc4ff1d7/docs/research/LENT-001-G2B-A-PROTOCOL.md) separately from experimental evidence.
- TOM-001 and LENT-001 are distinct research programs. Neither is changed by catalog ingestion.

### DELSK — DL-007 through DL-012

- [DL-007](INDEX.md#dl-007) — proposed reproducible research practices (not a frozen mandatory protocol).
- [DL-008](INDEX.md#dl-008) — adversarial selection/canonicality audit; initial E0 NOT READY must **not** be read as the latest E0 status.
- [DL-009](INDEX.md#dl-009) — critical prior-art comparison of two external reports; copying their conjectures as findings is forbidden.
- [DL-010](INDEX.md#dl-010) — frozen v4 experiment provenance contract; distinguished from the measurement model and post-activation outcome.
- [DL-011](INDEX.md#dl-011) — v4 activation *log*, a non-normative operational evidence record.
- [DL-012](INDEX.md#dl-012) — sealed S4-C holdout **PREREGISTRATION / NOT_RUN** on the pinned source; this is not a positive result or a release gate.

These entries deliberately distinguish desk research, frozen contract, external experimental log and future test plan.

### DeltaMeter — DM-008 through DM-014

- [DM-008](INDEX.md#dm-008) — guarded incremental prefix works in an explicitly bounded private lab; final correctness still depends on oracle/guard conditions.
- [DM-009](INDEX.md#dm-009) — exact BM-state equivalence but measured micro-optimization NO-GO.
- [DM-010](INDEX.md#dm-010) — fixed-constant finite-field reduction ACCEPT **only** in private decoder lane.
- [DM-011](INDEX.md#dm-011) — five-runner evidence for STOP_ALGEBRAIC_MICRO_OPT under a fixed 25% gate.
- [DM-012](INDEX.md#dm-012) — SYSTEM readiness success, **NOT** an efficacy or production result.
- [DM-013](INDEX.md#dm-013) — 3900 observations / 360 cells, verdict **STOP_SYSTEM_PRODUCT**; a scoped decision rather than universal impossibility.
- [DM-014](INDEX.md#dm-014) — research audit documenting why snapshot-codec assumptions and Amdahl estimates must match real measured code.

These studies supply real engineering counterexamples to overconfident mathematical/product extrapolation; none upgrades public ExactSmallDelta to GO.

### openai/math — OM-127, OM-128, OM-129, OM-130, OM-132, OM-133, OM-134, OM-137

Imported **specific markdown scope documents** under `lean/docs/*.md`, plus the original paper paths referenced directly inside those files. Only author-reported/collection-reported scope was inspected; imported PDFs themselves were **not independently reviewed** and Lean files were **not replayed**. All eight remain `EXTERNAL_MANUSCRIPT_CLAIM / source_catalog`.

- [OM-127](INDEX.md#om-127), [OM-132](INDEX.md#om-132) — sensitivity/block sensitivity, theoretical cautions for local vs batched influence.
- [OM-129](INDEX.md#om-129), [OM-134](INDEX.md#om-134) — automata state cost and generalized star-height, not direct Rust data-structure performance claims.
- [OM-130](INDEX.md#om-130), [OM-137](INDEX.md#om-137) — precise arithmetic-model vs bit/RAM-model distinction. No guarantee that the claimed theoretical DFT gain transfers to practical numerical FFT libraries.
- [OM-128](INDEX.md#om-128), [OM-133](INDEX.md#om-133) — string approximation and graph identification lower-bound contexts.

The authoritative full collection remains the upstream [CONTENTS.md](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md) and [Lean scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/formalization.yaml). This catalog must never suggest that external manuscripts have received independent acceptance simply because a scope document or comparator theorem exists.

## Cross-project discovery paths (interpretation; not mathematical results)

1. **Exact vs empirical:** [ML-008](INDEX.md#ml-008) ↔ [DM-011](INDEX.md#dm-011) ↔ [DL-007](INDEX.md#dl-007): finite exact certification, replicated negative performance gate and disciplined experiment design require different evidence.
2. **Costs of local influence:** [ML-006](INDEX.md#ml-006) ↔ [OM-127](INDEX.md#om-127) ↔ [OM-132](INDEX.md#om-132): distinguish one-edit response equivalence, average sensitivity and block sensitivity; no derived general incremental lower bound yet.
3. **Model-boundary discipline:** [ML-002](INDEX.md#ml-002) ↔ [DM-010](INDEX.md#dm-010) ↔ [OM-130](INDEX.md#om-130): algebraic operations and circuit models need explicit transformations before any performance claim.
4. **Honest product NO-GO:** [DL-012](INDEX.md#dl-012) ↔ [DM-013](INDEX.md#dm-013) ↔ [ML-004](INDEX.md#ml-004): preregistration, failed qualification and unproven mathematical opportunity must remain separate.
5. **Provenance chains:** [DL-010](INDEX.md#dl-010) ↔ [DL-011](INDEX.md#dl-011) ↔ [ML-009](INDEX.md#ml-009): normative protocol, activation evidence and fixed solver specification are different authorities.

## Remaining limits / next gate

- Current import is **curated, not exhaustive**: 14 imported records are only a small sample of the much larger openai/math collection.
- Related edges are semantic discovery hints; they are not theorem implications. Reverse links are auto-generated.
- The schema uses one SHA per repository namespace; mixed-version imports require explicit schema migration before use.
- Existing source entries are verified by readback at import time, not continuously re-fetched in CI.
- Future phases: per-paper theorem-level primary-source audit for **one selected** OM family; expand relevant DELSK/DeltaMeter coverage only when a tangible Mathlab question requires it; add theorem-claim-to-lemma graph **only after** distinguishing logical dependence from contextual similarity.

**RESEARCH-INDEX-002 import decision: CATALOG-EXPAND (scoped). NO THEOREM SELECTED.**
