# Research catalog — provenance-first index

## UCT-004 G2-A — original randomized-certificate and 2026 source imports (2026-10-09)

Three new deduplicated canonical identities **LIT-142..144** raise the [forward](LITERATURE.md) and [reverse](LITERATURE-BY-RESEARCH.md) literature index from 141 to **144**. LIT-142 Aaronson JCSS 2008 randomized certificate complexity; LIT-143 Ambainis et al. ACM TOCT 2021 total-function fractional adversary equivalence; LIT-144 Ben-David and Kothari September 2026 author preprint separating randomized queries and deterministic certificate complexity. Each has exact DOI/arXiv identity, pinned title, Russian model limits, `full_proof_verified=false` and [G2 source-model boundary audit](../UCT-004-G2-A-PRIMARY-SOURCE-AUDIT.md). No claim these original papers independently prove our dynamic theorem, or that the 2026 preprint has been peer-reviewed.

## UCT-003 G1 — static bit-probe primary prior art (2026-10-09)

Original [Viola (2012), *Bit-Probe Lower Bounds for Succinct Data Structures*](https://doi.org/10.1137/090766619) is imported as **LIT-141** with DOI identity, Russian abstract/model boundary, `full_proof_verified=false`, regenerated [forward](LITERATURE.md) and [inverse](LITERATURE-BY-RESEARCH.md) indexes and a title pin. Canonical bibliography grows from 140 to **141**, preserving the parallel HYP-105 G2 sources LIT-137..140. Static succinct bit-probe redundancy theory does **not** automatically imply our dynamic read/write or authenticated proof results. [UCT-003 source audit](../UCT-003-G1-SOURCE-AND-GAP-AUDIT.md).

## HYP-105 G2 grid-trade / sparse-code prior art (2026-10-09)

Four unique original publication identities **LIT-137..140** imported, without disturbing 136 existing records: 2022 AMS dense grid-free linear 3-graphs (the crucial Omega(m²) construction), Naor–Verstraëte 2005 ISIT sparse linear-dependence bounds, Santos–Tyomkyn 2025 Brown–Erdős–Sós high-density partial result, and Frankl–Füredi–Goorevitch–Holzman–Simonyi 2026 triple-system extremal study. Exact source-to-claim scope, provenance and false model-transfer warnings in [HYP-105 G2 audit](../HYP-105-G2-GRID-FREE-QUADRATIC.md). Authors/publisher abstracts checked; entire cited source proofs not independently checked. **140 unique works** with generated forward/reverse indices.

## HYP-105 G1 classical graph-source import (2026-10-09)

LIT-135 Wenger 1991 graph constructions avoiding C4/C6/C10 (JCTB original) and LIT-136 Abreu et al. 2011 explicit girth-8 cages (author arXiv preprint) are separately verified canonical identities. Links, Russian summaries, scope and false-novelty constraints are in [the self-contained w=2,d=3 proof](../HYP-105-G1-W2D3-GIRTH8.md), `literature.json`, and generated forward/reverse indices. **136** unique sources (previous 134 unchanged). Finite oracle verifies a 30-node graph only; external infinite-family existence is attributed to known literature, not independently formalized by CI.

## UCT-002 — wider original source imports (2026-10-09)

Eight additional unique original identities **LIT-127..134** cover local update/decoding codes, dynamic repair, annotated streams, Merlin–Arthur verification, leakage-resilient codes and Blackwell decision theory, expanding the canonical bibliography to **134**. [Source-model audit](../UCT-002-PRIMARY-SOURCE-AND-BRICKS.md) and [master theorem](../UCT-002-MASTER-THEOREM.md); all new records have `full_proof_verified=false`, provenance and generated forward/reverse links. Concurrent HYP-101 G1 LIT-123..126 are retained.

## HYP-101 G1 dynamic-string and BLAKE3 specification sources (2026-10-09)

Four unique primary source identities **LIT-123..126** extend the UCT-001 bibliography from 122 to **126**: 2018 SODA *Optimal Dynamic Strings*, 2026 TCS FeST, official [C2SP BLAKE3 v1.0.0](https://c2sp.org/BLAKE3@v1.0.0) (**normative technical specification, not a peer-reviewed paper**), and Duyster–Kociumaka 2026 dynamic internal pattern matching. Each is cross-mapped to [the HYP-101 phase/counter audit](../HYP-101-G1-PHASE-COUNTER-FRONTIER.md), with original Russian summaries and explicit non-transfer to unrestricted standard BLAKE3 edit-time lower bounds. Their metadata and historical source identities are validated offline by `research/literature.py --check`; verification of full external proofs is not claimed.

## UCT-001 cross-domain primary-source import (2026-10-08)

Twelve new, deduplicated original publication identities **LIT-111..122** are imported with exact DOI/ECCC URLs, Russian model-level summaries, limitation statements, source-provenance paths, reverse links and explicit `full_proof_verified=false` into [canonical literature.json](literature.json), [forward](LITERATURE.md) and [reverse](LITERATURE-BY-RESEARCH.md) generated indexes. Source and model/novelty separation: [UCT-001 primary-source audit](../UCT-001-PRIMARY-SOURCES.md); [program](../UCT-001-PROGRAM.md), [issue #74](https://github.com/definitely-stable/Mathlab/issues/74). The corpus grows from 110 to **122** unique identities, but this is **not** twelve independently verified theorems. LIT-041 and LIT-100 already existed and are not duplicated. Exact-head GitHub-hosted CI acceptance remains mandatory.

This is Mathlab's **curated, cross-repository research navigator**, not a mirror of other projects and not a ranking of proven mathematical discoveries.

- [OM-116/OM-140 mathematical transfer audit](../TOM-002-OM116-OM140-THEOREM-AUDIT.md): original theorem statements, positive-characteristic correction, transfer impossibilities and scoped model comparisons.
- [Readable index](INDEX.md): ID-indexed Russian one-paragraph summaries, topical tags, precise source links, primary papers and bidirectional metadata relationships.
- [Thematic navigator](THEMES.md): generated topic-to-record cross-repository discovery with source/status badges.
- [Import decision memo](IMPORT-002-REVIEW.md): cross-repo source selection, pins and constraints.
- [Primary-source scope audit](IMPORT-003-OPENAI-PRIMARY-AUDIT.md): ten selected openai/math families; manuscript metadata, Lean comparators, mismatches and verification limits.
- [Machine registry](registry.json): normative record metadata, stable IDs and exact upstream revision pins.
- [Mathlab research authority](../README.md): proofs, decisions and accepted claim hierarchy remain in their original files.
- [Catalog program](../../../research/catalog.py): deterministic offline validation and index generation.

## TOM-007 targeted source reconciliation (2026-10-08)

Seven original primary sources LIT-096..102 were absent from the previous 95-work canonical catalog: Nominal Adapton, Bigtable merge compaction, Competitive Data-Structure Dynamization, CPM 2026 dynamic LCE, Hardt–Woodruff adaptive linear sketches, Cohen–Singhal–Stemmer adaptive cardinality and Riker incremental builds. See [TOM-007 model/primary-source decision matrix](../TOM-007-SIX-HYPOTHESIS-AUDIT.md). The original seven paper identities, Russian model-specific summaries and citation/provenance links are in [literature.json](literature.json), the forward [literature index](LITERATURE.md) and the reverse [links by research](LITERATURE-BY-RESEARCH.md). Catalog **102 unique** identities; 40 historical known/STOP claims and 61 cross-project research records remain unchanged. New LIT entries are `model_overlap`, not fictitious citations or independently checked full mathematical proofs.

## HYP-103 targeted primary literature (2026-10-08)

Further six unique primary identities LIT-103..108 complement the previous 102 works: MFCS 2024 batch query maintenance; ESA 2020 parallel batch dynamic trees; ITCS 2020 instance/unlabeled certificates; ECCC 2026 certification complexity of Boolean functions; arXiv 2026 certificate-complexity condensation (v2); Buhrman–de Wolf 2002 decision-tree complexity survey. Source-model scope and the original elementary old-root probe reduction are recorded in [HYP-103 G0 audit](../HYP-103-G0-CERTIFICATE-REDUCTION.md). 108 unique primary records; existing 102 identities and historical research registries preserved. Full proofs not independently reverified; no new theorem or Rust claim.

## HYP-101 foundational cryptography sources (2026-10-08)

Added two unique papers **LIT-109** (CRYPTO 1994, Bellare–Goldreich–Goldwasser) and **LIT-110** (EUROCRYPT 1997, Bellare–Micciancio). They establish that incremental hashing as a broad research idea is classical, while exact standardized BLAKE3 digest compatibility is a different, not yet proven time–space theorem target. Russian summaries, distinct DOI identities, model boundary, author provenance and inverse research links are registered in [literature.json](literature.json) and [HYP-101 model audit](../HYP-101-G0-INCREMENTAL-HASH-AUDIT.md). Total **110** unique sources, prior 108 records unchanged, no independently checked full proofs.

## Coverage as of 2026-10-08

**RESEARCH-INDEX-002:** 61 curated records (Mathlab 11, DELSK 12, DeltaMeter 14, openai/math 24), cross-linked across 60 generated topics. Existing IDs preserved; RESEARCH-INDEX-003 adds 10 narrowly selected OpenAI families with explicitly recorded paper-package and Lean-scope checks.

The current external revision pins were verified on 2026-10-08; Mathlab was advanced to the HYP-001/002 merged main snapshot `c3ffc69563ac15241e67f4b6ccfe8063720590f1` (including G2B-A). See the import decision memo for representative source-level checks and claim-policy gates.

- **Mathlab (ML):** baseline/proof/evidence for LENT-001 and TOM-001 falsification and opportunity review.
- **Shift-lab/DELSK (DL):** primary-source comparison, negative screening, selector experiments and in-system ChunkShift development screen.
- **DeltaMeter (DM):** finite-sample model, published GF(2) reproduction, strict parity NO-GO, continuous exact certificate and comparator contracts.
- **openai/math (OM):** the collection index and a deliberately small selection of algorithmic/information-theoretic manuscript families. These are **claims in the source collection**, not independent validation or a recommendation to rely upon claimed breakthroughs.

A source may have more recent changes than the pinned revision. To track them, follow the **latest** link separately; updating the snapshot requires a review, never a silent SHA change. In particular, this is **not** an exhaustive copy of hundreds of OpenAI manuscripts; upstream [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md), [overview](https://github.com/openai/math/blob/main/overview.pdf), [Lean catalog](https://github.com/openai/math/blob/main/lean/formalization.yaml) and [release history](https://github.com/openai/math/blob/main/history.md) are the authoritative full indexes.

## Stable identity and structure

IDs are permanent, independent of filenames, titles, branch renames and changing evidence:

- `ML-###`, `DL-###`, `DM-###`, `OM-###`: short human references.
- `source.repo`, `source.revision`, `source.path`: the *specific observed artifact*; `source.permalink` must be an exact commit-based URL.
- `source.latest`: convenience navigation to a live branch, explicitly non-pinned.
- `summary_ru`: authored abstract, not copied wholesale from any paper or repository.
- `status`: what kind of claim this record makes; `verification`: which checking method was actually used. These fields are deliberately orthogonal.
- `topics`, `application_ru`, `limitations_ru`: discovery and scoping, never proof.
- `primary_sources`: DOI/arXiv/publisher references or first-party CI/artifacts; these are navigational, not automatic validation.
- `related`: typed ID-to-ID edges. Reverse links in INDEX are **generated**, not manually duplicated.

One catalog record currently points to one principal source artifact. Split entries when theorem and benchmark statuses differ rather than stamping a whole report 'THEOREM'. Avoid duplicate source paths; other connected papers remain `primary_sources` references.

## Evidence vocabulary / no claim promotion

`DERIVED_RESULT` means a proof/calculation is recorded in the linked repo, **not** that novelty or formalization is established. `EXACT_NUMERICAL` means finite exact evidence, **not** an asymptotic proof. `EMPIRICAL_RESULT` means measurements under a specific workload; never promote to mathematical theorem. `RESEARCH_DECISION` (including STOP/NO-GO) is scoped to its recorded model. `PRIOR_ART_AUDIT` may be limited by abstracts and inaccessible full texts. `OPEN_QUESTION` is open **within that program**, not certified open in world literature.

`EXTERNAL_MANUSCRIPT_CLAIM` / `source_catalog` marks the **author's reported conclusion** in openai/math. A linked Lean document is evidence of formalization work being present, but says nothing by itself about independent acceptance, scope of the formalized statement, or scientific novelty. Do not auto-map external claims to `THEOREM`, `PROVEN` or product dependencies.

`exact_hosted_ci` validates specific finite artifacts/accepted constraints only. None of the catalogue statuses should be conflated with a mathematical-proof assistant's guarantee.

## Reproducible workflow

Run locally or on GitHub-hosted CI (no new dependency, network fetch or credential):

```sh
python research/catalog.py --check
python -m unittest discover -s research -p "test_*.py"
```

To change the catalogue:

1. Read upstream's **canonical source** and confirm provenance, date, source version, theorem assumptions/claim status.
2. Reuse an existing ID; for genuinely distinct results allocate the next free ID in the relevant namespace. **Never renumber.**
3. Edit `registry.json`; use the fixed commit/revision of each source, link papers, record limitations and typed relationships.
4. Run `python research/catalog.py --write`; commit JSON, `INDEX.md` and `THEMES.md`. If importing an external source with a `source_audit`, check that every author package, comparator manifest and primary PDF path exists at the pinned SHA and record the exact Lean/main-paper mismatch.
5. Run `--check` and CI; review semantic changes independently of syntax/link validation.
6. If upstream changed, review affected entries and alter the whole source snapshot revision *only after* updating all links/claims for that namespace. For mixed-version imports, extend schema explicitly instead of silently changing source SHA per item.

The validator checks schema, IDs, graph endpoints, source pins, URL syntax, audited primary-source link presence in the registry, and deterministic generated docs **offline**. It does **not** fetch HTTP resources, verify paper claims, reproduce external benchmarks, determine copyright licenses or assert that all links remain live. Copies of external PDFs/binaries/Lean code are not included. Attribution remains with the original authors and repositories.

## Inclusion / exclusion

Include a new item only when it changes a concrete mathematical hypothesis, measured engineering decision, comparison baseline, or formalization methodology for Mathlab. Exclude automatically discovered low-relevance papers, unchecked social-media claims and duplicate summaries. Retain negative findings with scope limits. Keep Mathlab's accepted LENT-001 and TOM protocols authoritative; this index is a navigation/provenance layer, **not** a new research decision authority.

Maintenance: [RESEARCH-INDEX-003 issue #30](https://github.com/definitely-stable/Mathlab/issues/30) (selected OpenAI manuscript metadata audit); [RESEARCH-INDEX-001 issue #20](https://github.com/definitely-stable/Mathlab/issues/20) (foundation); [RESEARCH-INDEX-002 issue #27](https://github.com/definitely-stable/Mathlab/issues/27) (expanded import and thematic discovery).

## External primary literature (RESEARCH-LITERATURE-001/002/003/003B)

- [LITERATURE.md](LITERATURE.md): 95 curated DOI/arXiv/official publisher primary works with summaries, model restrictions, research relationships and commit-pinned citation provenance.
- [LITERATURE-BY-RESEARCH.md](LITERATURE-BY-RESEARCH.md): reverse navigation from existing ML/DL/DM/OM research IDs to papers.
- [LITERATURE-001-AUDIT.md](LITERATURE-001-AUDIT.md): selection, direct prior-art impact, mismatched models and decisions.
- [LITERATURE-002-SOURCE-AUDIT.md](LITERATURE-002-SOURCE-AUDIT.md): verified source corrections, 17 new papers, citation-model barriers and next targets.
- [LITERATURE-003-2026-OPPORTUNITY-AUDIT.md](LITERATURE-003-2026-OPPORTUNITY-AUDIT.md): 20 peer-reviewed/preprint 2026 works beyond sketch, ranked model-transfer and research kill tests.
- [RESEARCH-LITERATURE-003B addendum](../RESEARCH-LITERATURE-003B-2026-STOC-ICALP-EUROSYS.md): 26 additional STOC, ICALP and EuroSys publications, no duplicates with LIT-050–069, full provenance scope and priorities.
- [literature.json](literature.json): normative external-work IDs. Run `python research/literature.py --write`, then `--check` before merging.

This bibliography is a **separate work-entity type**: internal research registry entries stay 61, external literature adds 95 works and no novel theorem/benchmark is asserted.

