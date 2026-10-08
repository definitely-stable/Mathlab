# Research catalog — provenance-first index

This is Mathlab's **curated, cross-repository research navigator**, not a mirror of other projects and not a ranking of proven mathematical discoveries.

- [Readable index](INDEX.md): ID-indexed Russian one-paragraph summaries, topical tags, precise source links, primary papers and bidirectional metadata relationships.
- [Thematic navigator](THEMES.md): generated topic-to-record cross-repository discovery with source/status badges.
- [Import decision memo](IMPORT-002-REVIEW.md): source selection criteria, fresh pins, scope and limitations.
- [Machine registry](registry.json): normative record metadata, stable IDs and exact upstream revision pins.
- [Mathlab research authority](../README.md): proofs, decisions and accepted claim hierarchy remain in their original files.
- [Catalog program](../../../research/catalog.py): deterministic offline validation and index generation.

## Coverage as of 2026-10-08

**RESEARCH-INDEX-002:** 51 curated records (Mathlab 11, DELSK 12, DeltaMeter 14, openai/math 14), cross-linked across 54 generated topics. Existing 26 IDs preserved; 25 new records.

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
4. Run `python research/catalog.py --write`; commit the JSON and **both** generated `INDEX.md` and `THEMES.md`.
5. Run `--check` and CI; review semantic changes independently of syntax/link validation.
6. If upstream changed, review affected entries and alter the whole source snapshot revision *only after* updating all links/claims for that namespace. For mixed-version imports, extend schema explicitly instead of silently changing source SHA per item.

The validator checks schema, IDs, graph endpoints, source pins, URL syntax and deterministic generated docs **offline**. It does **not** fetch HTTP resources, verify paper claims, reproduce external benchmarks, determine copyright licenses or assert that all links remain live. Copies of external PDFs/binaries/Lean code are not included. Attribution remains with the original authors and repositories.

## Inclusion / exclusion

Include a new item only when it changes a concrete mathematical hypothesis, measured engineering decision, comparison baseline, or formalization methodology for Mathlab. Exclude automatically discovered low-relevance papers, unchecked social-media claims and duplicate summaries. Retain negative findings with scope limits. Keep Mathlab's accepted LENT-001 and TOM protocols authoritative; this index is a navigation/provenance layer, **not** a new research decision authority.

Maintenance: [RESEARCH-INDEX-001 issue #20](https://github.com/definitely-stable/Mathlab/issues/20) (foundation); [RESEARCH-INDEX-002 issue #27](https://github.com/definitely-stable/Mathlab/issues/27) (expanded import and thematic discovery).
