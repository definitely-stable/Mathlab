# IMPORT-014 — ICML 2026: learnable connectivity, graph label budget and dual-graph memory

Issue [#332](https://github.com/definitely-stable/Mathlab/issues/332) · Source discovery 2026-10-11 · **PMLR official proceedings, vol. 306**.

This is an **abstract / publisher bibliographic identity audit**. It does NOT reproduce the source proofs, evaluate code, confirm claimed gains or establish novel Mathlab theorems. Proceedings are peer reviewed; results remain claims of the cited authors until independently verified. PMLR official bibliographic IDs do not require inventing a DOI.

## Five genuinely new canonical publications

| New LIT | Primary PMLR identity | Scope, with authors' assumptions | Mathlab opportunity and non-transfer boundary |
| --- | --- | --- | --- |
| **LIT-393** | [Transformers Provably Learn Algorithmic Solutions for Graph Connectivity, But Only with the Right Data](https://proceedings.mlr.press/v306/ye26f.html) · Qilin Ye, Deqing Fu, Robin Jia, Vatsal Sharan · `publisher:pmlr-v306-ye26f` · pp. 148293–148324 | Disentangled Transformer of depth L **can compute** graph connectivity for diameter up to 3^L through adjacency-power-like algorithm; training-dynamics arguments depend on training instances lying within representational capacity. Standard Transformer transfer is **empirical**. | Contrast with LIT-388/LIT-389: expressivity and training-data curriculum vs exact local GNN execution. *Undirected connectivity* or tested graph families do not establish arbitrary **directed DAG reachability**, immutable label update bounds, authenticated witnesses or even a universal training guarantee. |
| **LIT-394** | [An Approximation Algorithm for Graph Label Selection](https://proceedings.mlr.press/v306/john26a.html) · Josia John, Simon Meierhans, Maximilian Probst Gutenberg · `publisher:pmlr-v306-john26a` · pp. 54486–54500 | Under the standard budget k, choose k vertices to reveal **ground-truth task labels** for predicting remaining vertex labels; authors claim first tilde-O(log^{1.5} n) approximation rather than resource augmentation. | Prior art for budgeted *representative selection* of expensive labels; important **negative model fence**: these are supervised target labels, *not* exact reachability labels / dynamic index metadata / hash signatures. Need define objective function and oracle before comparing to INDEX-001. |
| **LIT-395** | [Adaptive Memory Retention in Dynamic Graphs](https://proceedings.mlr.press/v306/de-castelli26a.html) · Fabrizio De Castelli, Alessio Gravina, Moshe Eliasof, Carola-Bibiane Schönlieb, Davide Bacciu · `publisher:pmlr-v306-de-castelli26a` · pp. 23292–23315 | LAMP models **snapshot-based dynamic graph embeddings** with impulsive neural ODE, antisymmetric conservative and learned dissipative dynamics; authors give stability / representational arguments. | Link to graph-memory temporal dynamics and LIT-391 resolution stability. **State-retention of embeddings ≠ lossless history retention**, causal evidence, bitemporal provenance, cryptographic freshness or bounded SSD read/write cost. |
| **LIT-396** | [Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph](https://proceedings.mlr.press/v306/wang26ip.html) · Qiuchen Wang et al. (12 authors) · `publisher:pmlr-v306-wang26ip` · pp. 131006–131031 | VimRAG: **dynamic directed acyclic graph** of iterative reasoning states and multimodal evidence; graph-topology-aware high-resolution visual token retention, with graph-guided policy optimization and pruning. | Especially relevant to DAG-002/agent memory for a *budgeted provenance evidence graph*. But pruned retrieval nodes do not guarantee exact evidence preservation, witness replay, answer faithfulness or safe negative-cycle exclusion. Validate against a frozen evidence oracle and time/byte/token budgets. |
| **LIT-397** | [A Tale of Two Graphs: Separating Knowledge Exploration from Outline Structure for Open-Ended Deep Research](https://proceedings.mlr.press/v306/shi26n.html) · Zhuofan Shi et al. (10 authors) · `publisher:pmlr-v306-shi26n` · pp. 112015–112043 | DualGraph maintains separate **Knowledge Graph (KG)** of fine-grained evidence concepts and **Outline Graph (OG)** for writing/coverage; topology gaps guide targeted follow-up search; experiments on four deep-research benchmarks. | Directly applicable as a **design baseline** for Mathlab's agent-oriented research search/indexing; use a *bibliographic identity graph* + *research-question/claim map* with explicit cited-by / contrasts / missing-prior-art edges. Still empirical: no guarantee that generated research gaps represent complete literature or logically valid causal links. |

## Deduplication

Candidate **MRAgent**, “Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents”, *already exists* at **LIT-230** (`arxiv:2606.06036`). Its ICML PMLR page is [ji26d](https://proceedings.mlr.press/v306/ji26d.html), same paper. It is deliberately **not** counted as a new LIT record. A separate provenance-only alias update may be considered, not a new publication.

## Typed prior-art and transfer claims

Machine-readable edges: [IMPORT-014-GRAPH-AI-RELATIONS.json](IMPORT-014-GRAPH-AI-RELATIONS.json). Edges of type `model_overlap`, `contrasts_with`, `assumption_incompatible`, `evaluation_baseline`, `useful_design_analogy` are **bibliographic annotations, not theorems**.

### Alignment to existing research

- **DAG-002 / ALG-001**: LIT-393 clarifies that `can represent connectivity` / `learn under a curriculum` differs from `construct a valid *immutable directed reachability oracle* for every online update sequence`. LIT-394 is a counter-model for the overloaded word *label*. Train/query/evidence verification and write-amplification prices are distinct.
- **UCT-005**: LIT-395's continuous-time signal dissipation is **not** safe forgotten-history reclamation in authenticated retention. LIT-396's path pruning of visually irrelevant items may invalidate later exact evidence reconstruction. A verified PIN/reference model must be preserved separately.
- **INDEX-001**: Graph selection k is not paid bytes on disk; adapted KV/visual tokens are not fsync or RAM page buffers. Report all costs separately: `(accuracy, token_budget, ingest, queries, historical_replay, bytes_read, bytes_written, RAM_peak)`.
- **Research graph for AI agents**: LIT-397 motivates separate `source/claim/proof graph` vs `open-questions/outline/task graph`, linked by source-verified **typed edges**, *without* treating graph proximity or a generated relationship as proof.
- **Prior IMPORT-013**: LIT-393 complements LIT-388/389; LIT-395 has a separate stability model from LIT-391; LIT-396's multimodal evidence DAG contrasts with LIT-392's `wGraph` agent workflow planning.

## Four falsification-first experiments (not yet performed)

1. **Transformer capacity curriculum**: fix training/test graph families, degree, number of vertices, depth L, and diameters around `3^L`. Compare simple heuristics, exact BFS oracle and disjoint split. **Kill criterion:** claimed result requires oracle features not available at inference.
2. **Label semantics and budget**: freeze graph label selection's prediction loss/k against graph reachability labeling's query-correctness/metadata budget. **Kill criterion:** no common objective -> drop cross-theorem transfer.
3. **Snapshot memory vs history truth**: create conflicting updates with time gaps, tombstones, replay and provenance PINs; compare learned LAMP representations to an exact event-sourced oracle. **Kill criterion:** forgotten history breaks required temporal queries.
4. **DualGraph/VimRAG evidence retention**: deterministic citation/evidence DAG of Mathlab claims with known gold parents, forbidden hallucinated ancestors, and exhaustive 2-hop coverage; evaluate dual-graph gap planning and DAG token-pruning against plain search and a strict evidence oracle. **Kill criterion:** any source-independent novelty assertion or deletion of a necessary original witness.

## Acceptance gates

1. Original **391 identities** and entries preserved byte-for-byte as logical JSON records; exactly five records added (LIT-393..397). PMLR publisher identities are not disguised as DOI.
2. All five `verification=publisher_abstract_checked`, `full_proof_verified=false`, `independent_reproduction=false`; `mentioned_in.kind=model_overlap` and pinned source document commit.
3. Generated both literature indices from the existing standard deterministic renderer.
4. Updated count tests without destroying IMPORT-013 cohort-specific regression fences. Checked against GitHub-hosted unit and import-specific CI.
