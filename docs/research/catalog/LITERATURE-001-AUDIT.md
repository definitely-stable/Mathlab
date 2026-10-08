# RESEARCH-LITERATURE-001 — source-aware cross-project citation audit

Status: **CURATED PRIMARY-SOURCE METADATA / NO THEOREM NOVELTY CLAIM**  
Date: 2026-10-08 · Issue: [#43](https://github.com/definitely-stable/Mathlab/issues/43)  
Normative bibliographic registry: [literature.json](literature.json)  
Forward navigation: [LITERATURE.md](LITERATURE.md)  
Reverse navigation: [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md)  
Original internal research index: [INDEX.md](INDEX.md)

## What was imported — and what was not

32 unique, deduplicated **primary bibliographic works** from the paper families already cited in, or specifically model-related to, Mathlab, DELSK and DeltaMeter. Each literature entry has:

- stable `LIT-XXX` ID and canonical DOI/arXiv/venue identity (only one row per work);
- date, first-party paper or publisher/author abstract, concise original-language-independent Russian summary;
- explicit scope caveat, research `ML/DL/DM/OM` edges and commit-pinned mention or explicitly labelled `model_overlap`;
- verification tier distinguishing author preprint/publisher abstract, first-party text spot-check and **bibliographic** check.

This imports **metadata, summaries and exact source pointers**, not third-party PDF contents, code, licenses or benchmarks. The repository's 61 prior research records remain unchanged; the external bibliography is a **parallel scholarly-works entity type**, not an attempt to turn 32 papers into 32 Mathlab theorem results. In particular, source `main` is never relied on for old references; internal source mentions are linked using frozen revisions in `literature.json`.

## Five subcorpora

| Cluster | Count | Audited direct model links |
| --- | ---: | --- |
| Bounded-support codes / combinatorics | 7 | ASET HYP-001/002, GF(5) weak-Sidon finite upper, support-constrained codes |
| Dynamic structures / canonical layout | 5 | TOM O04/O05/O06/O07/O09, history-independent dynamic partitioning, CDC locality |
| Incremental computation | 3 | TOM O01/O02 and finite certificate indistinguishability |
| Delta compression / content similarity | 10 | DELSK feature extraction, reference selection, codec-aware sketch, CDC and index |
| Streaming estimation / reconciliation | 7 | DeltaMeter F-PCSA strict finite coverage, PinSketch vs Simple Set Sketching and RIBLT |

## Independent primary source checks and important mathematical distinctions

### A. Mathlab: codes and locality

- [LIT-001](LITERATURE.md#lit-001) **bounded-contention coding** precedes generic binary active-set identification, but its radio/communication model does not settle ASET's strict hard support of code columns.
- [LIT-002](LITERATURE.md#lit-002) **Roth–Seroussi 1996** supplies the classical weak-Sidon upper used in G2B-B1. The implication ASET → weak Sidon is only **one-way**. This import in no way updates issue #42 or its mathematical search.
- [LIT-003](LITERATURE.md#lit-003) **Blackburn 2015** includes t=2 separable-code context. [LIT-004](LITERATURE.md#lit-004) **Cheng et al. 2015** is a separate **t=3** separable code paper despite both sources involving length-three structures; treating them as the same 2-ID collision theorem would be wrong.
- [LIT-005](LITERATURE.md#lit-005) **union-free hypergraphs** concern edge **unions**, not modular additive sums. Code families may overlap in restricted 0/1 settings; general GF(q) equivalence is not shown.
- [LIT-006](LITERATURE.md#lit-006) **support-constrained parity checks** study different support orientation and minimum distance. This is a priority *model comparison*, not an ASET bound.
- [LIT-007/008](LITERATURE.md#lit-007) **history-independent partitioning** from 2024 and extended 2026 cover large parts of O04's originally broad conjecture. Both are retained separately as distinct publisher versions, not falsely deduplicated as the *same publication*.
- [LIT-009](LITERATURE.md#lit-009) **Chonkers**, [LIT-011](LITERATURE.md#lit-011) dynamic gap dictionaries and [LIT-012](LITERATURE.md#lit-012) string synchronizing sets require separate edits/bytes/canonicality/adversary models before any novelty transfer.
- [LIT-010](LITERATURE.md#lit-010), [LIT-013](LITERATURE.md#lit-013) and [LIT-032](LITERATURE.md#lit-032) establish substantial prior art for change propagation; separately certified no-effect changes do not compose without additional conditions.

### B. DELSK: key negative novelty findings

- [LIT-020](LITERATURE.md#lit-020) Broder's resemblance **and asymmetric containment** predates DELSK. A claim that simply noting asymmetry is new would be wrong.
- [LIT-014](LITERATURE.md#lit-014) Finesse and [LIT-015](LITERATURE.md#lit-015) DeepSketch already implement compact feature-based delta reference search, with DeepSketch using **actual delta ratio in learning**. Therefore neither general sketch → delta-base nor generic codec awareness is an unoccupied contribution.
- [LIT-016](LITERATURE.md#lit-016) Palantir conditions hierarchy/filtering on real patch utility; [LIT-018](LITERATURE.md#lit-018) SpeedSketch affects both sketch preparation and encoder. Their author gains are **not** DELSK measurements.
- [LIT-017/030](LITERATURE.md#lit-017) Odess conference 2021 and journal 2023 are **different publications** with distinct evaluation conditions; no merging reported speedups.
- [LIT-021/022](LITERATURE.md#lit-021) LSHBloom and FED are *document/LLM dataset* deduplication baselines, not automatically comparable delta encoding protocols. [LIT-019](LITERATURE.md#lit-019) FastCDC concerns boundaries, not reference-search optimality.

### C. DeltaMeter: estimator vs recoverer vs rateless protocol

- [LIT-023](LITERATURE.md#lit-023) is Wang's original F-PCSA, important specifically because its **asymptotic** estimator guarantee cannot be silently promoted to strict finite-sample one-sided coverage.
- [LIT-024](LITERATURE.md#lit-024) AMS frequency moments and [LIT-025](LITERATURE.md#lit-025) Fish-number cardinality-estimation theory answer different statistical questions; Fisher information does not certify ParityDeltaMeter's finite row budgets.
- [LIT-026](LITERATURE.md#lit-026) Simple Set Sketching is a *recoverable* XOR sketch with probabilistic decoding; [LIT-027](LITERATURE.md#lit-027) Rateless IBLT is an incrementally extended *reconciliation protocol*. A communicated coded-symbol count is not a byte count; framing/key/checksum fields matter.
- [LIT-028/029](LITERATURE.md#lit-028) Gaussian streaming memory lower bounds are the nearest earlier comparators for OM-140, but noisy and linear-prediction versions have distinct assumptions. No lower bound for TOM O01 follows without a proof of reduction.

## Coverage and negative-space audit

- **No exhaustive literature claim.** More publications are mentioned across the source repositories than the 32 curated high-relevance sources. Selection criteria: direct mathematical neighbor, concrete protocol comparator, falsification of proposed originality, or practical source of measured algorithmic comparison.
- **No DOI/URL live polling in CI.** Primary landing pages or author paper source abstracts were inspected during this import; GitHub-hosted checks validate metadata, identities, pins, link edges and generated documents offline. External PDFs were not fully read/reproved.
- `cited` means the paper is explicitly cited in a source doc; `model_overlap` means relevance was inferred and recorded **without claiming that the source document cited it**.
- No automatic inference that papers with similar keywords prove the same result; proof model, field characteristic, active-cardinality promise, randomness, probability level, storage layout and resource cost must align.
- Source snapshots intentionally separate from Mathlab's pre-existing 61-entry registry snapshots. Future updates must not overwrite original provenance.

## Next recommended relevance gates (without touching G2B-B2)

1. **HYP-002 prior-art:** compare the exact *weighted/general-support* theorem to LIT-003/004/005/006, writing explicit maps of collision relations. Determine whether any sharp constant or new phenomenon remains. Coordinate with #25, not #42.
2. **DELSK:** cost/codec/selector matrix for LIT-014..019 and LIT-020, with fixed source/patch budgets, provenance and no benchmark cherry-picking.
3. **DeltaMeter:** keep finite-sample coverage separate from progressive recovery; use LIT-023/025/026/027 as different baselines, not substitutes. Do not reopen a STOP_SYSTEM_PRODUCT gate without new evidence.
4. **TOM O01/O04:** review memory/probe and byte-write/adaptive-adversary models against LIT-007/008/010/011/013/032 before proposing a theorem.

**Decision:** `LITERATURE_IMPORT_ACCEPT` for bibliography and mathematical model mappings **only**. **NO THEOREM SELECTED / NO RUST CRATE AUTHORIZED.**
