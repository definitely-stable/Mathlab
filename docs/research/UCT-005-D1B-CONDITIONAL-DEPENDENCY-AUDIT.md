# UCT-005 D1-B — 2026 3SUM/APSP conditional-hardness dependency audit

**2026-10-10.** Parent [IMPORT-011 #228](https://github.com/definitely-stable/Mathlab/issues/228) · [D1-B #231](https://github.com/definitely-stable/Mathlab/issues/231) · original [Alman–Vassilevska Williams, arXiv:2610.06783](https://arxiv.org/abs/2610.06783) = existing LIT-357. Scientific classification: **EXPLICIT_TEXT_DEPENDENCY_NOT_FOUND / IMPLICIT_DEPENDENCY_NOT_EXCLUDED / UNCONDITIONAL_LOWER_BOUNDS_UNAFFECTED / ROOT_OPEN**.

## 1. What source establishes; what it does not

Authors claim deterministic O(n^1.9992) for integer 3SUM of polynomially bounded magnitude and O(n^2.9995) for directed APSP with polynomially bounded integer edge weights, plus separately described transfers to real instances, Exact Triangle, and selected hinted matrix-vector variants. This contradicts the **standard fine-grained hypotheses** that all algorithms require n^(2-o(1)) and n^(3-o(1)) respectively in their respective models. The paper is an author preprint; Mathlab has **not independently replayed its full proof**. A conditional theorem of the form H implies L is still a valid mathematical implication when H is false, but it **cannot substantiate L as an operative hardness barrier**. The reduction itself has not been disproved. None of this refutes SETH, OVH, arbitrary OMv variants, or unconditional cell-probe/memory-checker statements.

## 2. Actual source inventory — fail-closed CI scan of non-generated Markdown/JSON

Six non-generated documents contain 3SUM/APSP/SETH/Exact-Triangle/OMv-type text. All eleven matching lines were classed under explicit anchors in [machine-readable audit register](UCT-005-D1B-CONDITIONAL-DEPENDENCY-REGISTER.json); the catalog was reviewed separately (364 entries).

| Path or source | Evidence found | Classification |
| --- | --- | --- |
| RESEARCH-LITERATURE-004-CACHING-GRAPHS-2025-2026.md | ICALP 2025 `A Simple Dynamic Spanner via APSP` | **ALGORITHM_TITLE_NO_HARDNESS**; the paper title is not a hardness assumption. |
| RESEARCH-LITERATURE-005-DYNAMIC-ALGEBRA-GRAPHS-2025-2026.md | LIT-190, incremental approximate APSP; anchor paragraph | **APSP_ALGORITHM_NOT_HARDNESS**; retains valid algorithm comparison. |
| RESEARCH-LITERATURE-011-EXTERNAL-PDF-AUDIT-2026.md | Four statements about the October 2026 source and needed dependencies | **SCOPED_SOURCE_AUDIT**; not an underlying lower-bound proof. |
| UCT-005-ROOT-THEOREM-PROGRAM.md | IMPORT-011 warning note | **SCOPED_SOURCE_AUDIT**; ROOT_OPEN. |
| catalog/README.md | IMPORT-011 navigation and historical count | **BIBLIOGRAPHY_NAVIGATION**, not theorem. |
| catalog/LITERATURE-003-2026-OPPORTUNITY-AUDIT.md | Two historical source/proposal references to SETH and cell-probe | **INDEPENDENT_SETH_PRIOR_ART / SCOPED_SOURCE_AUDIT**; do not treat independent SETH results as refuted. |
| LIT-058 | Dynamic pattern matching, a conditional limitation via SETH | **INDEPENDENT_SETH_PRIOR_ART**, unaffected. |
| LIT-163 | Dynamic spanner via APSP | **APSP_ALGORITHM_NOT_HARDNESS**. |
| LIT-357 | Alman–Vassilevska Williams refutation source | **REFUTATION_SOURCE**, not Mathlab original theorem. |

**Audit correction:** An initial file-name exclusion swept up historical LITERATURE-003 along with generated catalog views. GitHub-hosted CI correctly flagged two SETH mentions. This register now pins both lines; generated LITERATURE.md and LITERATURE-BY-RESEARCH.md alone are excluded from the scan. No semantic lower-bound transfer is inferred from either mention.

**Result:** No explicit text in the audited non-generated corpus or canonical LIT metadata claims a Mathlab lower-bound theorem conditional *only* on the classical 3SUM/APSP hypotheses. This is **not a universal negative theorem**: dependencies hidden in unstated reductions, linked PDF proofs or future open PRs are not ruled out.

## 3. Mandatory future source-model decision

For any further original research claim, record: (i) precise baseline hypothesis/quantifier, (ii) input and integer/real/weight domain, (iii) RAM/cell-probe/conditional-conjecture model, (iv) preprocessing, update/query/adversarial budget, (v) time exponent and any reductions, (vi) independent publication status and proof-verification level. Distinguish `CONJECTURE_ALREADY_REFUTED`, `OTHER_UNRESOLVED_HYPOTHESIS`, `UNCONDITIONAL_PROVED`, and `AUTHOR_EXPERIMENT_ONLY`.

Only direct, source-grounded dependency links justify correction of a theorem. A pure bibliographic mention or shortest-path algorithm name does not. In particular, DO NOT label an information-transfer argument obsolete simply because a paper's title contains APSP.

## 4. CI and falsification acceptance

`research/uct005_d1b_conditional_audit.py` enforces the typed **known-mention inventory**, re-scans non-generated Markdown/JSON and the canonical catalog, and fails closed for new sensitive occurrences until a person classifies them. The paired unit test checks canonical source identity, inventory completeness and an injected unreviewed-hardness counterexample. It does not attempt automated deep proof interpretation.

**D1-B STOP:** no direct conditional theorem to revoke. Do not claim the UCT-005 root proved or rename an unrelated lower bound; proceed with D1-A exact restricted parity/falsification and the later HYP-105 signed-trade supersaturation work independently.
