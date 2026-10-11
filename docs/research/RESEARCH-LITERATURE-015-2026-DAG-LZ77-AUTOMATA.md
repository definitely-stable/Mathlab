# IMPORT-015 — five 2026 algorithms and proof-complexity breakthroughs

Issue [#343](https://github.com/definitely-stable/Mathlab/issues/343). Source audit: **2026-10-11**. Base: IMPORT-014 branch ([PR #333](https://github.com/definitely-stable/Mathlab/pull/333)), because the latter owns LIT-393–397. This import owns only **LIT-398–402**. The five published sources below are **new-to-Mathlab**, but their proofs are **not independently verified**.

## Source identities, exact model boundaries and interpretation

1. **LIT-398 — [Stochastic Embedding of Digraphs into DAGs](https://epubs.siam.org/doi/10.1137/1.9781611978971.5)**, Arnold Filtser, *SODA 2026*, pp. 105–119, DOI `10.1137/1.9781611978971.5`. For a weighted digraph G, author constructs a distribution of **pairs** of DAGs preserving source-to-target reachability and dominated distances in the specified paired-embedding model. It has expected distortion **tilde-O(log n)**, **tilde-O(m)** sparsity, and sampling time **tilde-O(m)**. This is stronger than a prior tilde-O(log³ n) guarantee. **Not** an exact single DAG, immutable reachability label, adaptive update algorithm, or byte-level persistence theorem.
2. **LIT-399 — [From Incremental Transitive Cover to Strongly Polynomial Maximum Flow](https://epubs.siam.org/doi/10.1137/1.9781611978971.7)**, Daniel Dadush, James B. Orlin, Aaron Sidford, László A. Végh, *SODA 2026*, pp. 150–163, DOI `10.1137/1.9781611978971.7`. New reductions on structured max-flow networks to **incremental supersets of transitive closure**, plus bounded-capacity flow instances, yielding strongly polynomial improvements for bipartite b-matching and bounded-treewidth flow. **A transitive cover superset is not necessarily the exact reachability relation**, and an algorithm with amortized graph work is not a lower bound on storage writes.
3. **LIT-400 — [The Complexity of Dynamic LZ77 is `tilde-Theta(n^(2/3))`](https://epubs.siam.org/doi/10.1137/1.9781611978971.67)**, Itai Boneh, Shay Golan, Matan Kraus, *SODA 2026*, pp. 1859–1872, DOI `10.1137/1.9781611978971.67`. Initial tilde-O(n) preprocessing; maintenance under substitutions, insertions, deletions in **tilde-O(n^(2/3))** time. Matching **SETH-conditional** lower bound against O(n^(2/3)-epsilon), even substitutions when maintaining only the number of factors. **Not** an unconditional bound, not CDC/FastCDC, not general patch-size lower bound and not proof about CAS rewrite volume.
4. **LIT-401 — [Determinization of Min-Plus Weighted Automata is Decidable](https://epubs.siam.org/doi/10.1137/1.9781611978971.11)**, Shaull Almagor, Guy Arbel, Sarai Sheinvald, *SODA 2026*, pp. 247–257, DOI `10.1137/1.9781611978971.11`. Resolves whether the **determinization property for min-plus/tropical weighted automata** is decidable, via analysis of nondeterministic runs. **Not** a theorem about arbitrary weighted oracles, lossless automaton compression in general, or complexity of the constructed determinizer.
5. **LIT-402 — [Monotone circuit lower bounds from spread matchings](https://eccc.weizmann.ac.il/report/2026/129/)**, Anup Rao, ECCC **TR26-129**, revision #5 September 3, 2026. Proves **exp(Omega(sqrt n))** gates necessary to detect bipartite perfect matchings on n-vertex graphs with *monotone circuits*, via a spread-matching lemma. **Not** a lower bound for unrestricted non-monotone circuits, randomized programs, GF(q) flows or physical graph-index layouts. **Author preprint**, not refereed proceedings; revision history includes corrected proof in July 2026.

## Dedup and genealogy

- Explicitly rejected *Tight Lower Bounds for Central String Queries in Compressed Space*, SODA 2026 DOI `10.1137/1.9781611978971.65`: already canonical **LIT-258**. No second identity or bibliographic record introduced.
- Imported **LIT-398–402** are not among preceding proposed FOCS 2026 papers (Ko dynamic DAG, robust turnstile, posterior matching, compressed ISA and dynamic connectivity); avoid counting those as part of this batch.
- Prior known sources: LIT-187/239/300/302 (DAG reachability), LIT-258/372/387 (compressed index/string lower bounds), LIT-298 (Larsen–Yu dynamic cell-probe), LIT-401 is a **new tropical automata** result, not identical to old **OM-129** questions about state complexity; LIT-402 relates methodologically to proof-complexity LIT-373, not a direct reduction.

## Typed scientific-use graph and negative transfer fences

Machine-readable: [IMPORT-015-ALGORITHM-RELATIONS.json](IMPORT-015-ALGORITHM-RELATIONS.json). These are **model-overlap, proof-model contrast, evaluation-baseline and assumption-incompatible edges**, never machine-certified theorem implications.

- **DAG-002:** compare pairs of DAG embeddings and incremental closure supersets against exact directed reachability. Freeze query oracle, updates, edge weights, failure probability, DAG semantics and output representation. *Kill:* inferred exact label construction from approximation/reduction.
- **UCT-005 / INDEX-001:** incremental transitive-cover maintenance and SETH-conditional LZ77 recomputation complexity require separate accounting for RAM, SSD reads, writes, full history replay, and proof size. *Kill:* claiming a conditional time bound as unconditional physical write lower bound.
- **ChunkShift / compressed-indexing:** maintain CDC chunks and true dynamic LZ77 factorization on the **same edit trace**, with throughput, output size, update RAM and representation-dependent conditions. *Kill:* equating distinct lossless representations without reduction.
- **proof-complexity / algebraic-algorithms:** monotone perfect-matching circuit lower bound and tropical-weighted-automaton decidability cover different models. Avoid any implied hardness of general hash families, GF(5) hypergraphs or dynamic query indexes.

## Verification / acceptance

- Canonical DOI pins: SODA SIAM publisher DOI pages; ECCC official TR26-129 ID (no invented DOI), peer-review flags correctly distinguished.
- All original 396 entries intact, plus exactly 5 unique LIT-398–402; 22 tracks unchanged; no reused IDs; no forged publisher-author/title pairs.
- `full_proof_verified=false` and `independent_reproduction=false` on all; `mentioned_in.kind=model_overlap` pins this exact audited document commit SHA.
- Regenerate forward and reverse navigation with project’s original deterministic renderer; preserve preceding import specific regression tests, adapt only aggregate collection counts.
- New isolated hosted import CI, plus standard full Research CI. **Do not merge** this stacked PR ahead of PR #333; test and merge only with appropriate green CI.

Source scope: audited primary publisher abstracts / ECCC metadata. No claim that a theorem, bound, priority or source novelty was independently reproduced.
