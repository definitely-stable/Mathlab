# IMPORT-013 — ICML 2026 graph algorithm learning and graph foundation transfer

Source audit: **2026-10-11** · Issue [#318](https://github.com/definitely-stable/Mathlab/issues/318). This is a **publisher proceedings / abstract / bibliography audit**, not a reproduction of the authors' proofs or empirical results. Canonical identities use PMLR volume/article keys: the PMLR pages do not provide a DOI; never invent one.

## Five distinct canonical primary publications

| LIT | Publisher identity | Primary proceedings (PMLR 306, ICML 2026) | Scientific scope and strict transfer boundary |
| --- | --- | --- | --- |
| LIT-388 | `publisher:pmlr-v306-wittig26a` | [Which Algorithms Can Graph Neural Networks Learn?](https://proceedings.mlr.press/v306/wittig26a.html) · Wittig et al., pp. 135232–135307 | Sufficient conditions for MPNNs trained on small examples to **approximate** graph-algorithm execution on arbitrary input sizes with worst-case guarantees; impossibility results for standard architectures. No exact immutable DAG labeling or priced physical writes follow. |
| LIT-389 | `publisher:pmlr-v306-fetrat-qharabagh26a` | [Learning to Execute Graph Algorithms Exactly with Graph Neural Networks](https://proceedings.mlr.press/v306/fetrat-qharabagh26a.html) · Fetrat Qharabagh et al., pp. 30992–31124 | **Exact** learned local instructions (NTK-trained MLP ensemble) under bounded degree, finite precision and probability conditions; LOCAL, BFS/DFS/Bellman–Ford. Exactness is conditional on this architecture/training/model, not a universal neural guarantee or an online DAG index. |
| LIT-390 | `publisher:pmlr-v306-zhu26e` | [When Do Graph Foundation Models Transfer? A Data-Centric Theory](https://proceedings.mlr.press/v306/zhu26e.html) · Zhu et al., pp. 166802–166822 | Dense-graph **graphon** model, Lipschitz backbone, finite-sample versus relabeling-invariant domain mismatch and spectral PE stability. No theorem transfer to sparse arbitrary dynamic DAGs, disk page I/O or exact reachability. |
| LIT-391 | `publisher:pmlr-v306-koke26a` | [Graph Neural Networks Are Not Continuous Across Graph Resolutions](https://proceedings.mlr.press/v306/koke26a.html) · Koke et al., pp. 59879–59931 | Non-continuity of GNN representations under some natural graph convergence modes; constructive architecture modification. Neither a universal discontinuity claim for every model nor preserved provenance/query correctness from embedding continuity. |
| LIT-392 | `publisher:pmlr-v306-li26ig` | [GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving](https://proceedings.mlr.press/v306/li26ig.html) · Li et al., pp. 71745–71762 | Shared workflow graph `wGraph`, adaptive planning and KV-cache reuse. Authors report approximately 4× smaller memory footprint and 4.95 percentage-point average quality improvement **in their experimental setup**, not independently reproduced and not a worst-case storage trade-off. |

No full-paper theorem audit was performed. Proceedings dates: 6–11 July 2026. Exact publisher title/author/volume/pages checked on the five PMLR pages.

## Model typed links and non-transfer firewall

Machine-readable graph: [IMPORT-013-GRAPH-LEARNING-RELATIONS.json](IMPORT-013-GRAPH-LEARNING-RELATIONS.json). `model_overlap` means **shared abstract vocabulary only**, not mathematical implication; `contrasts_with` identifies assumptions and outputs that must be reconciled before a comparison; `evaluation_baseline` is an empirical suggestion.

- **DAG-002**: Compare immutable labels and online reachability with learnable message-passing/local instructions (LIT-388/389). Train/test graph-size shifts, adaptivity and unchanged frozen metadata are explicit separate constraints. A BFS result is not a paid-write immutable reachability index.
- **ALG-001**: Contrast small-sample approximation lower limits (LIT-388) with conditional exact learning (LIT-389). Require the *same* precision, degree, error probability, graph family and training budget before claiming a contradiction or equivalence.
- **UCT-005**: Do **not** identify information-theoretic, cell-probe, Byzantine freshness or durable history retention costs with representational stability/error bounds (LIT-390/391).
- **INDEX-001**: Graphon cross-domain stability and graph-resolution continuity concern learned representations, **not** bytes rewritten, WAL, fsync, page recourse, B-tree/LSM or immutable index query truth. `wGraph` KV-cache savings (LIT-392) are an experiment-oriented comparison; measure ingestion, cold/warm cache, update invalidation and actual memory separately.
- **GraphRAG and agent memory**: Link as comparison against LIT-221, LIT-243, LIT-294 and LIT-317 but do not equate workflow planning, fact extraction, memory truth, retrieval effectiveness and exact graph computation.

## Proposed falsification gates for next research slice

1. **Same-model exact-vs-approx audit**: Find a common restricted graph family and precision/training model for LIT-388 and LIT-389; classify cases where the claims address different quantifiers. Never infer universal exact learnability from the LOCAL result.
2. **Dense-to-sparse shift**: Test bounded-width DAGs and strongly sparse families against the dense graphon assumptions of LIT-390. Treat counterexamples as transfer failures, not contradictions of the paper.
3. **Resolution invariance**: Construct graph coarsening/refinement families with preserved reachability and changed GNN embeddings. Separate embedding discrepancy from exact query answer correctness for LIT-391.
4. **Paid KV-cache/IO trade-off**: Benchmark LIT-392 with identical task distributions, graph-building amortization, memory units, cached prompt prefixes and cache invalidations against non-graph workflows.

## Acceptance boundaries

- Append exactly five unique canonical records; preserve the old 386 IDs and aliases unchanged.
- Introduce a dedicated `graph-learning-theory` track for LIT-388..391; classify LIT-392 as `graph-reasoning` (workflow systems).
- Label all five `publisher_abstract_checked`, `full_proof_verified=false`, `independent_reproduction=false`. The only provenance kind is `model_overlap`.
- Deterministically regenerate `LITERATURE.md` and `LITERATURE-BY-RESEARCH.md`; run both catalog validator and import-specific checks in GitHub-hosted Research CI.
- **No theorem promotion and no claimed performance reproduction**.
