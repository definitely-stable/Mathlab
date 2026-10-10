# Mathlab execution backlog — 2026-10-10

**Status:** proposed implementation sequence, not accepted scientific claims or automatic GitHub issue closure. Source: [55-issue dated inventory](ISSUE-TRIAGE-ALL-OPEN.md), [issue action review](ISSUE-TRIAGE-2026-10-10.md), [UCT-005 theorem tree](UCT-005-THEOREM-TREE.json), and [canonical source catalog](catalog/literature.json).

## Decision rule

Priorities are **engineering triage heuristics**, not measurements of theorem truth: impact `I` and near-term tractability `T` are ordinal 1–5; `I×T` sorts practical work, not expected probability of mathematical discovery. P0 = 1–3 days, P1 = 1–2 weeks, P2 = 1–2 months, P3 = longer/unbounded research. Estimates are rough and contingent on existing concurrent PRs and CI.

| Rank | Phase | Issue / action | I×T | Effort | Dependencies | Verifiable exit condition |
| ---: | --- | --- | ---: | --- | --- | --- |
| 1 | P0 | [#256](https://github.com/definitely-stable/Mathlab/pull/256) status integrity | 5×5=25 | 0.5–1 d | Exact HEAD; full Research CI | Focused+full hosted SUCCESS on same SHA; no root promotion; independent review |
| 2 | P0 | [#257](https://github.com/definitely-stable/Mathlab/pull/257) full issue inventory | 4×5=20 | 0.5–1 d | Snapshot 55, current main | Focused+full CI, 55 unique IDs, valid parent DAG, reproducible dashboard |
| 3 | P0 | [#252](https://github.com/definitely-stable/Mathlab/issues/252) merged PIN bitmap checkpoint | 5×4=20 | 0.5–1 d | PR #253 merged | Exact postmerge main CI, paid two-reader PIN root/remote bitmap cost audit, scoped result |
| 4 | P0 | [#142](https://github.com/definitely-stable/Mathlab/issues/142) / [#154](https://github.com/definitely-stable/Mathlab/issues/154) LIT identity reconciliation | 5×4=20 | 1–2 d | Current 386-entry catalog; source inventory | Dedup LIT-355/LIT-298; no fixed LIT-205 IDs; exact source pins and generated indexes |
| 5 | P0 | [#231](https://github.com/definitely-stable/Mathlab/issues/231) obsolete 3SUM/APSP transfer gate | 4×4=16 | 0.5–1 d | PR #232 merged | Postmerge Research/INDEX gate and explicit source transfer limitations |
| 6 | P0 | [#147](https://github.com/definitely-stable/Mathlab/issues/147) Ko/covering-code source audit | 3×4=12 | 1 d | Catalog alias check | DOI/arXiv/ECCC identity verified, model overlap tagged, no LIT collision |
| 7 | P1 | [#236](https://github.com/definitely-stable/Mathlab/issues/236) import vs math separation | 4×4=16 | 1–2 d | PR #246 merged; HYP #251 | Mark imported sources accepted only as metadata; leave supersaturation transfer open |
| 8 | P1 | [#244](https://github.com/definitely-stable/Mathlab/issues/244) COW implementation acceptance | 5×3=15 | 2–4 d | Open PR #248, F1 model | 122-byte node/root/PIN ledger, exact-head tests and review; postmerge check if merged |
| 9 | P1 | [#254](https://github.com/definitely-stable/Mathlab/issues/254) segmented allocator | 5×3=15 | 2–4 d | #244 model; exact n=257/P=1 falsifier | Global-vs-segmented paid-page comparison; no unsupported Pareto dominance |
| 10 | P1 | [#223](https://github.com/definitely-stable/Mathlab/issues/223) same-F1 comparator | 5×3=15 | 3–5 d | #244/#252 scoped implementations | One cost-vector ledger with all missing axes marked UNKNOWN, same trace/adversary |
| 11 | P1 | [#234](https://github.com/definitely-stable/Mathlab/issues/234) typed proof-transfer audit | 5×3=15 | 2–4 d | Existing G4 atlas, primary sources | Every proposed Fano/future-quotient transfer has quantified model map and countermodel |
| 12 | P1 | [#247](https://github.com/definitely-stable/Mathlab/issues/247) insdel/polar source PR | 3×4=12 | 1–2 d | Open PR #250; catalog lock | Exact-head CI and source alias validation; explicit STOP for unproved ASET transfer |
| 13 | P1 | [#25](https://github.com/definitely-stable/Mathlab/issues/25) / [#24](https://github.com/definitely-stable/Mathlab/issues/24) derived theorem close review | 3×4=12 | 1–2 d | Exact proof artifacts and main CI | Derived/classical proof grade documented; close only if original acceptance fulfilled |
| 14 | P2 | [#183](https://github.com/definitely-stable/Mathlab/issues/183) physical page recourse | 4×3=12 | 1–2 wk | #211 allocator assumptions | Explicit adversarial bounded-slack lower or counterexample; charged RAM/GC |
| 15 | P2 | [#211](https://github.com/definitely-stable/Mathlab/issues/211) bounded-workspace recovery | 4×3=12 | 1–2 wk | INDEX #183 / #173 | Crash-prefix, allocator generation and peak workspace oracles, exact CI |
| 16 | P2 | [#195](https://github.com/definitely-stable/Mathlab/issues/195) bitemporal provenance | 4×3=12 | 1–2 wk | Output contract selection | Fix authenticated Boolean/negative proof vs enumerated witness semantics; typed costs |
| 17 | P2 | [#140](https://github.com/definitely-stable/Mathlab/issues/140) / [#161](https://github.com/definitely-stable/Mathlab/issues/161) DAG×ALG | 4×3=12 | 1–2 wk | Source/edge model audit | Explicit arbitrary-edge vs append-new-sink reduction or STOP |
| 18 | P2 | [#255](https://github.com/definitely-stable/Mathlab/issues/255) total PIN trusted budget | 5×2=10 | 2–4 wk | F1 #223, merged #253, COW #248 | Full writer+two-reader+PIN authority information accounting and a falsified/proved candidate |
| 19 | P2 | [#105](https://github.com/definitely-stable/Mathlab/issues/105) original joint bound program | 5×2=10 | 2–6 wk | #223, #234, source audit | Precisely quantified candidate with same-model upper falsifiers; otherwise scoped STOP |
| 20 | P3 | [#230](https://github.com/definitely-stable/Mathlab/issues/230) all-h correlated seven-motif obstruction | 5×1=5 | Open-ended | HYP #176/#169/#162; weighted GF5 | Full all-h Ω(s⁶) proof **or** infinite correlated counterfamily; finite cases insufficient |

## Dependency and acceptance rules

**P0:** unblock trustworthy metadata and remove stale literature/PR checkpoints before moving scientific ownership. Two independent draft PRs (#256, #257) must pass their own exact-head CI; merging either one is a separate reviewed decision.

**P1:** implement and test only frozen F1 service coordinates; do not let a byte-authenticated COW reference, remote PIN bitmap, or allocator trick become a new lower-bound claim. Literature imports must be serialized on current main because LIT IDs and generated indexes are shared.

**P2:** use distinct proof obligations for physical-page recourse, authenticated bitemporal provenance, dynamic DAG and PIN information. A model-preserving reduction is a prerequisite for cross-domain theorem transfer.

**P3:** mathematical discovery remains unbounded. A negative result (valid counterexample or sourced STOP) is an acceptable outcome; finite computation is not a substitute for all-h/all-s quantification.

## Risks, rollback, and authority

- **Merge conflict / stale CI:** re-read current main and PR HEAD, compare exact SHA; rollback by reverting the narrow PR, not by overwriting concurrently changed source indexes.
- **False novelty / model mixing:** leave UCT-005 `OPEN_UNPROVED`; no automated scientific status promotion. Rollback any unsupported theorem-edge to `REDUCTION_REQUIRED` or `NO_THEOREM_TRANSFER`.
- **Bibliography collisions:** DOI/arXiv/ECCC aliases and stable LIT IDs are the canonical key; never reuse an ID because an old issue quoted a smaller catalog count.
- **Physical-cost overclaim:** page-write ledger is not NAND wear or crash atomicity unless those semantics are separately modeled and proved.
- **Issue churn:** all 55 inventory entries are a dated snapshot, not a live issue closure list. Refresh through a reviewed new snapshot rather than silently changing the 2026-10-10 historical record.

**Definition of done:** code/document changes reviewed on exact SHA; focused and full GitHub-hosted CI; postmerge main checks where applicable; scientific claims separately proof- and source-audited. The plan is not itself a proof.
