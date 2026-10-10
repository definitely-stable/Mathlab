# IMPORT-010 — graph memory, DNA/pangenome graphs and neurobiology

Date: 2026-10-10. [Research issue #220](https://github.com/definitely-stable/Mathlab/issues/220), graph literature umbrella [#184](https://github.com/definitely-stable/Mathlab/issues/184).

Scope: 32 first-party verified DOI/arXiv publication identities in 3 new catalog lanes (genomic-graphs, biological-memory, molecular-dna-storage) plus existing agent-memory. Classification: PRIMARY_PUBLISHER_OR_AUTHOR_ABSTRACT / NO_INDEPENDENT_PROOF_AUDIT / NO_REPRODUCED_BENCHMARK. Metadata are verified publication/abstract references, not re-proved results. The full canonical ID, abstract-level Russian summary, model-transfer caution and links are in literature.json and its generated LITERATURE.md and LITERATURE-BY-RESEARCH.md views.

## Four non-equivalent notions of memory and graph

- Agent GraphRAG: fact assertions, source pointers, semantic relation edges, entity disambiguation, time/retractions, and relevance-based retrieval.
- DNA pangenome: sequence-labeled bidirected variation graph, orientation and reverse complements, genomic haplotype paths, population/sample annotation. A graph walk may be biologically impossible unless path/color-consistent.
- Biological engram: neural ensemble and plastic hippocampal/neocortical circuitry. Imaging and behavioral experiments do NOT prove an algorithmic asymptotic bound or biologically faithful software simulation.
- Synthetic DNA storage: molecular oligonucleotides encode arbitrary digital bytes, with synthesis/sequencing error and primers; physical reads have no direct page-IO equivalence.

## Critical falsifiers and research hypotheses

**G10-H1: colored provenance paths.** Adapt annotated de Bruijn sample color sets to TKG source IDs; require a *single coherent sample and time-valid witness across every edge*. Counterexample: every k-mer is locally present but consecutive k-mers originate from incompatible samples; the uncolored union graph contains a phantom reconstructed path. Do not infer globally existing full-length path merely from independent per-k-mer memberships. Falsify by exhaustive tiny color-annotated graph oracles.

**G10-H2: buffered graph maintenance.** Compare BufBOSS, immutable event-log scans and a paid MVCC colored graph index under identical bounded RAM, page bytes, delete/retract, pinned epochs and compaction workload. Dynamic graph mutations can split unitigs and propagate non-local recourse; logical k-mer update is not guaranteed one physical page write. Explicitly separate cold-read cost, output completeness and late retraction.

**G10-H3: associative retrieval.** Compare HippoRAG PPR and context-gated linking inspired by hippocampal studies to BM25, vectors and equal-budget hybrid retrieval with identical corpora, LLMs, update pattern and total ingest/query costs. Neural engram biology is only an inspiration; reject false context merges and all uncertified fresh/negative claims.

**G10-H4: molecular noisy path recovery.** DNA Fountain and de-Bruijn graph partitioning use erasures, substitutions, indels, sequencing coverage and chemical access; require full oligo source-ID consistency plus checksum for exact reconstruction. Never identify molecular random access with SSD page reads.

## Prior-art non-duplication and research mapping

HippoRAG 2024 is distinct from HippoRAG 2 / From RAG to Memory [LIT-237](catalog/LITERATURE.md#lit-237); Zep [LIT-235](catalog/LITERATURE.md#lit-235) and Mem0 [LIT-240](catalog/LITERATURE.md#lit-240) remain unchanged. Graph-structure/index links go to ML-004 and ML-006; biological associative memory additionally relates to OM-133 only by analogy. All 315 old literature IDs remain stable. No original theorem, clinical claim, measured SSD improvement or new Rust primitive is asserted by this bibliographic import.
