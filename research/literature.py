#!/usr/bin/env python3
"""External literature: offline metadata validator and deterministic navigation.

Do NOT equate cited external literature with a verified proof, benchmark, or
novelty claim. No network, no dependencies, no external code execution.
Usage: python research/literature.py --check | --write
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/research/catalog/literature.json"
INTERNAL = ROOT / "docs/research/catalog/registry.json"
INDEX = ROOT / "docs/research/catalog/LITERATURE.md"
REVERSE = ROOT / "docs/research/catalog/LITERATURE-BY-RESEARCH.md"
REPO_ID = re.compile(r"^LIT-[0-9]{3}$")
SHA = re.compile(r"^[a-f0-9]{40}$")
URL = re.compile(r"^https://[^\s<>]+$")
IDENTITY = re.compile(
    r"^(?:doi:10\.[0-9]{4,9}/[^\s]+|arxiv:[0-9]{4}\.[0-9]{4,5}"
    r"|usenix:[a-z0-9-]+:[a-z0-9-]+|publisher:[a-z0-9:-]+)$"
)
TRACKS = {
    "sparse-coding": "Кодирование, ограниченная поддержка, экстремальные границы",
    "dynamic-data-structures": "Динамические структуры, каноничность и локальность правок",
    "incremental-computation": "Инкрементальные вычисления и сертификаты",
    "delta-base-selection": "DELSK: поиск delta-базы, сжатие, признаки",
    "streaming-reconciliation": "DeltaMeter: потоковые оценки и согласование множеств",
    "compressed-indexing": "Сжатые структуры, индексация строк и нижние границы",
    "online-optimization": "Онлайн-оптимизация, конкурентные оценки и барьеры",
    "caching": "Кэширование, online paging, консистентность и память",
    "graph-algorithms": "Динамические графы, гиперграфы и sparsification",
    "genomic-graphs": "DNA, пангеномы, de Bruijn и sequence graph индексы",
    "biological-memory": "Когнитивные карты, гиппокамп, engram и биологическая память",
    "molecular-dna-storage": "Молекулярная запись в DNA, кодирование и графовая реконструкция",
    "graph-rag": "GraphRAG, knowledge-graph retrieval, системное сравнение с RAG",
    "agent-memory": "Графовая память агентов, темпоральность и эволюция знаний",
    "graph-reasoning": "Графовые зависимости шагов рассуждения, DAG-планирование",
    "graph-learning-theory": "Теория обучения графовым алгоритмам, перенос GFM и устойчивость представлений",
    "algebraic-algorithms": "Алгебраические алгоритмы, subset sum и разреженные матрицы",
    "proof-certification": "Машинные доказательства, сертификаты и верификация",
    "proof-complexity": "Нижние границы доказательств, IPS/PIT и сертификаты",
    "algebraic-complexity": "Алгебраические схемы, математика и нижние границы",
    "fine-grained-algorithms": "Edit distance, строки и тонкая сложность",
    "randomized-sampling": "Рандомизированная выборка, подсчёт и memory-sample",

}
VERIFICATIONS = {
    "primary_abstract_checked",
    "publisher_abstract_checked",
    "publisher_bibliography_checked",
    "publisher_full_text_spotchecked",
    "author_paper_or_bibliography_checked",
}
SOURCE_REPOS = {"MATHLAB", "DELSK", "DELTAMETER"}
NEW_2026_IDS = {f"LIT-{i:03d}" for i in range(50, 70)}
VENUE_2026_IDS = {f"LIT-{i:03d}" for i in range(70, 96)}
PUBLICATION_STAGES = {"peer_reviewed_proceedings", "author_preprint"}
PRIORITIES = {"A", "B"}

SOURCE_TITLE_PINS = {
    # IMPORT-013: exact ICML 2026 PMLR publisher titles.
    "publisher:pmlr-v306-wittig26a": "Which Algorithms Can Graph Neural Networks Learn?",
    "publisher:pmlr-v306-fetrat-qharabagh26a": "Learning to Execute Graph Algorithms Exactly with Graph Neural Networks",
    "publisher:pmlr-v306-zhu26e": "When Do Graph Foundation Models Transfer? A Data-Centric Theory",
    "publisher:pmlr-v306-koke26a": "Graph Neural Networks Are Not Continuous Across Graph Resolutions",
    "publisher:pmlr-v306-li26ig": "GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving",
    # IMPORT-012 additional primary source benchmarks and dynamic GBWT.
    "arxiv:2505.12891": "TIME: A Multi-level Benchmark for Temporal Reasoning of LLMs in Real-World Scenarios",
    "doi:10.64898/2026.03.26.714584": "A run-length-compressed skiplist data structure for dynamic GBWTs supports time and space efficient pangenome operations over syncmers",
    # IMPORT-012 verified canonical primary title identities (provenance and genealogy).
    "doi:10.1007/s00222-014-0562-8": "Hypergraph containers",
    "doi:10.1090/S0894-0347-2014-00816-X": "Independent sets in hypergraphs",
    "doi:10.1007/s00493-026-00214-1": "Towards an Optimal Hypergraph Container Lemma",
    "arxiv:1801.04584": "The method of hypergraph containers",
    "doi:10.1137/21M1428431": "A Logarithmic Lower Bound for Oblivious RAM (For All Parameters)",
    "arxiv:1704.06185": "Cell-Probe Lower Bounds from Online Communication Complexity",
    "arxiv:2608.19172": "Cell-Probe Lower Bounds and Complexity-Preserving Reductions for Suffix Array Queries",
    "doi:10.4230/LIPIcs.CCC.2026.41": "Systematic Data Structure Lower Bounds via the Query-With-Sketch Model",
    "doi:10.1016/j.ffa.2024.102569": "Regular sets of lines in rank 3 polar spaces",
    "doi:10.1007/s10623-024-01489-5": "A common generalization of hypercube partitions and ovoids in polar spaces",
    "doi:10.1016/j.ffa.2025.102746": "The Erdős-Rado sunflower problem for vector spaces",
    "doi:10.1112/blms.70382": "Fractional clique decompositions of dense hypergraphs",
    "doi:10.1101/gr.276607.122": "Lossless indexing with counting de Bruijn graphs",
    "doi:10.3389/fgene.2025.1679660": "Beyond single references: pangenome graphs and the future of genomic medicine",
    "doi:10.18653/v1/2024.acl-long.8": "A Unified Temporal Knowledge Graph Reasoning Model Towards Interpolation and Extrapolation",
    "doi:10.18653/v1/2024.findings-emnlp.543": "Natural Evolution-based Dual-Level Aggregation for Temporal Knowledge Graph Reasoning",
    "publisher:aclanthology:2025-neusymbridge-1-2": "CEGRL-TKGR: A Causal Enhanced Graph Representation Learning Framework for Temporal Knowledge Graph Reasoning",
    "arxiv:2507.23581": "GraphRAG-R1: Graph Retrieval-Augmented Generation with Process-Constrained Reinforcement Learning",
    "doi:10.5281/zenodo.21039806": "Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on a Math Textbook",
    "doi:10.1145/3798129.3800774": "Dynamic Meta-Kernelization",
    # IMPORT-011: external PDF corrections, checked publisher/author identities.
    "arxiv:2610.06783": "Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs",
    "doi:10.1109/SP61157.2025.00247": "Cauchyproofs: Batch-Updatable Vector Commitment with Easy Aggregation and Application to Stateless Blockchains",
    "arxiv:2507.22265": "Cell-Probe Lower Bounds via Semi-Random CSP Refutation: Simplified and the Odd-Locality Case",
    "arxiv:2609.38772": "Counting hypergraphs without linear cycles of fixed length",
    "arxiv:2603.00428": "Spectral Turán Problems for Expanded hypergraphs",
    "arxiv:2602.23282": "Largest Sidon subsets in weak Sidon sets",
    "arxiv:2605.03274": "Formalizing Singer Sidon Constructions and Sidon Set Infrastructure in Lean 4",
    "arxiv:2608.12990": "LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation",
    "doi:10.1073/pnas.2004821117": "HEDGES error-correcting code for DNA storage corrects indels and allows sequence constraints",
    # UCT-005 D0 originals, after genomic IMPORT-010 LIT-317..348.
    "usenix:osdi04:li-j": "Secure Untrusted Data Repository (SUNDR)",
    "doi:10.1016/j.ic.2018.03.004": "Verifying the consistency of remote untrusted services with conflict-free operations",
    "doi:10.1016/j.jisa.2026.104444": "SNARKs for stateful computations on authenticated data",
    "doi:10.1145/2213977.2213987": "The Cell Probe Complexity of Dynamic Range Counting",
    "doi:10.1145/2897518.2897556": "Cell-probe lower bounds for dynamic problems via a new communication model",
    "doi:10.1016/0022-0000(89)90034-2": "Making data structures persistent",
    "arxiv:2608.25206": "Authenticated Data Structures for Dynamic Workloads",
    "doi:10.1016/j.future.2024.107629": "Integrita: A BFT distributed storage system",
    # IMPORT-010: original 2024–2026 graph/DNA/biology and foundational titles.
    "arxiv:2405.14831": "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models",
    "arxiv:2310.08560": "MemGPT: Towards LLMs as Operating Systems",
    "doi:10.1038/nbt.4227": "Variation graph toolkit improves read mapping by representing genetic variation in the reference",
    "doi:10.1093/bioinformatics/btz575": "Haplotype-aware graph indexes",
    "doi:10.1186/s13059-020-02135-8": "Bifrost: highly parallel construction and indexing of colored and compacted de Bruijn graphs",
    "doi:10.1016/j.csbj.2021.06.047": "Buffering updates enables efficient dynamic de Bruijn graphs",
    "doi:10.1093/bioinformatics/btac308": "ODGI: understanding pangenome graphs",
    "doi:10.1038/s41586-023-05896-x": "A draft human pangenome reference",
    "doi:10.1038/s41587-023-01793-w": "Pangenome graph construction from genome alignments with Minigraph-Cactus",
    "doi:10.1038/s41588-024-02029-6": "Pangenome graphs and their applications in biodiversity genomics",
    "doi:10.1186/s13059-025-03606-6": "A survey of sequence-to-graph mapping algorithms in the pangenome era",
    "doi:10.4230/LIPIcs.SEA.2025.13": "Pangenome Graph Indexing via the Multidollar-BWT",
    "doi:10.1038/s41586-025-09603-w": "Efficient and accurate search in petabase-scale sequence repositories",
    "doi:10.1038/s41588-025-02478-7": "Compressive pangenomics using mutation-annotated networks",
    "doi:10.1038/s41586-026-10924-7": "An Icelandic pangenome reference",
    "doi:10.1186/s13059-026-04242-4": "COSIGT: population-scalable genotyping of complex loci from low-coverage sequencing data using pangenome graphs",
    "doi:10.1038/s41576-026-00987-7": "Building and applying pangenome references to capture genetic diversity",
    "doi:10.1186/s13059-026-04017-x": "Multi-context seeds enable fast and high-accuracy read mapping",
    "doi:10.1038/s41467-026-74126-5": "Interpretable graph-based models on multimodal biomedical data integration: a technical review and benchmarking",
    "doi:10.1038/s41586-024-07973-1": "Human hippocampal and entorhinal neurons encode the temporal structure of experience",
    "doi:10.1038/s41586-025-08993-1": "Systems consolidation reorganizes hippocampal engram circuitry",
    "doi:10.1038/s41593-025-01986-3": "Formation of an expanding memory representation in the hippocampus",
    "doi:10.1038/s41593-026-02231-1": "The prefrontal cortex controls memory organization in the hippocampus",
    "doi:10.1038/s41593-026-02230-2": "Deconstruction of a memory engram reveals distinct ensembles recruited at learning",
    "doi:10.1038/s41583-025-01012-2": "Astroengrams: rethinking the cellular substrate for memory",
    "doi:10.1038/s41467-024-44871-6": "Latent representations in hippocampal network model co-evolve with behavioral exploration of task structure",
    "doi:10.1038/s41593-026-02357-2": "Experience reorganizes content-specific memory traces in macaques",
    "doi:10.1016/j.nlm.2025.108057": "The molecular and cellular basis of memory engrams: Mechanisms of synaptic and systems consolidation",
    "doi:10.1126/science.aaj2038": "DNA Fountain enables a robust and efficient storage architecture",
    "doi:10.1038/nbt.4079": "Random access in large-scale DNA data storage",
    "doi:10.1093/bioinformatics/btaf618": "De-Bruijn graph partitioning for scalable and accurate DNA storage processing",
    "doi:10.1093/nargab/lqab126": "High-scale random access on DNA storage systems",
    # IMPORT-009: DAG lower bound, graph indexes, temporal provenance and memory originals.
    "doi:10.1137/24M1638215": "Super-Logarithmic Lower Bounds for Dynamic Graph Problems",
    "doi:10.7155/jgaa.v30i1.3148": "Parameterized Linear Time Transitive Closure",
    "doi:10.1007/s44443-025-00310-0": "MLRQ: an efficient labeling scheme for reachability queries on reduced DAGs",
    "doi:10.1145/3776737": "Indexing Techniques for Graph Reachability Queries",
    "arxiv:2607.21390": "Reachability in Directed Acyclic Graphs with Near-Linear Cut Queries",
    "arxiv:2604.28096": "Succinct Graph Representations and Algorithmic Applications",
    "arxiv:2506.21436": "Succinct Preferential Attachment Graphs",
    "arxiv:2402.11028": "Incremental Topological Ordering and Cycle Detection with Predictions",
    "arxiv:0803.0792": "Incremental Topological Ordering and Strong Component Maintenance",
    "doi:10.1109/ICDE65706.2026.00177": "Lightweight 2-Hop Labels for Reachability Queries on Large-Scale Graphs",
    "doi:10.1109/ICDE65706.2026.00179": "Clue-RAG: Towards Accurate and Cost-Efficient Graph-Based RAG Via Multi-Partite Graph-Based Index",
    "arxiv:2607.18368": "Neuro-Symbolic Meta-Policies for Temporal Knowledge-Graph Memory under Partial Observability",
    "arxiv:2605.07121": "AdaTKG: Adaptive Memory for Temporal Knowledge Graph Reasoning",
    "arxiv:2604.17114": "The Provenance Gap in Clinical AI: Evidence-Traceable Temporal Knowledge Graphs for Rare Disease Reasoning",
    "doi:10.1038/s41598-026-51488-w": "Temporal knowledge graph reasoning using global and recent history information",
    "doi:10.1145/3183713.3183724": "Incremental View Maintenance for Property Graph Queries",
    "doi:10.1609/aaai.v40i19.38619": "ArchRAG: Attributed Community-based Hierarchical Retrieval-Augmented Generation",
    "doi:10.1007/s00778-026-00977-5": "Efficiently querying connected components in large temporal graphs via scalable and maintainable indices",
    "doi:10.14778/3819518.3819556": "BookRAG: A Hierarchical Structure-aware Index-based Approach for Retrieval-Augmented Generation on Complex Documents",
    # IMPORT-008: DAG shortcutting, graph compression, memory cost and temporal evidence.
    "doi:10.4230/LIPIcs.ITCS.2026.102": "Smoothed Analysis of Dynamic Graph Algorithms",
    "doi:10.4230/LIPIcs.ESA.2026.7": "Symmetry-Preserving Graph Compression",
    "doi:10.4230/LIPIcs.ESA.2026.35": "Dynamic Detours",
    "doi:10.4230/LIPIcs.ESA.2026.57": "Dynamic Matroids: Base Packing and Covering",
    "doi:10.4230/LIPIcs.ESA.2026.59": "Revisiting Diameter in Directed Graphs",
    "doi:10.4230/LIPIcs.ESA.2026.108": "Maximum Coverage k-Antichains and Chains: A Greedy Approach",
    "doi:10.4230/LIPIcs.ESA.2026.109": "Dynamic Dominating Set in Uniformly Sparse Graphs",
    "doi:10.4230/LIPIcs.ICALP.2026.15": "Parallel Reachability and Shortest Paths on Non-Sparse Digraphs: Near-Linear Work and Sub-Square-Root Depth",
    "doi:10.4230/LIPIcs.ICALP.2026.70": "Incremental (k, z)-Clustering on Graphs",
    "doi:10.4230/LIPIcs.ICALP.2026.105": "Better Diameter Bounds for Efficient Shortcuts and a Structural Criterion for Constructiveness",
    "doi:10.4230/LIPIcs.SWAT.2026.12": "Strategy Repair in Reachability Games via a Graph Quotientation",
    "arxiv:2609.23315": "Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query, Ingest, and Update Performance Across Graph Database Engines",
    "arxiv:2608.08055": "SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents",
    "arxiv:2606.17183": "VL-MemKnG: Hybrid Memory with a Spatio-Temporal Knowledge Graph for Question Answering over Long Egocentric Navigation Trajectories",
    "arxiv:2510.13614": "MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning",
    # IMPORT-007: source-verified temporal/dynamic graphs and graph RAG primary titles.
    "doi:10.4230/LIPIcs.SAND.2026.4": "Families of Tractable Problems with Respect to Vertex-Interval-Membership Width and Its Generalisations",
    "doi:10.4230/LIPIcs.SAND.2026.5": "Complexity Gaps Between Point and Interval Temporal Graphs for Some Reachability Problems",
    "doi:10.4230/LIPIcs.SAND.2026.6": "Broadcasts in Anonymous, Dynamic Networks: A New Algorithm and Impossibility Results",
    "doi:10.4230/LIPIcs.SAND.2026.7": "Extending Ghouila-Houri’s Characterization of Comparability Graphs to Temporal Graphs",
    "doi:10.4230/LIPIcs.SAND.2026.9": "FO and MSO Model Checking on Temporal Graphs",
    "doi:10.4230/LIPIcs.SAND.2026.10": "Asymptotic Subspace Consensus in Dynamic Networks",
    "doi:10.4230/LIPIcs.SAND.2026.14": "Robust Temporal Cut",
    "doi:10.4230/LIPIcs.SAND.2026.15": "Designing Sparse Temporal Graphs Satisfying Connectivity Requirements",
    "doi:10.4230/LIPIcs.SAND.2026.16": "On Sufficient Conditions for Short Journeys in Temporal Graphs",
    "doi:10.4230/LIPIcs.SAND.2026.17": "Label Correcting Algorithms for the Multiobjective Temporal Shortest Path Problem",
    "doi:10.4230/LIPIcs.SAND.2026.19": "Minimize the Sum of Waiting Times in Periodic Temporal Trees",
    "doi:10.4230/LIPIcs.ESA.2026.122": "Maximizing Reachability via Shifting of Temporal Paths",
    "doi:10.4230/LIPIcs.LICS.2026.36": "Dynamic Planar Graph Isomorphism Is in DynFO",
    "arxiv:2606.06044": "IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval",
    "arxiv:2606.15778": "DYNA : Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning",
    "arxiv:2508.01680": "T-GRAG: A Dynamic GraphRAG Framework for Resolving Temporal Conflicts and Redundancy in Knowledge Retrieval",
    "arxiv:2601.16462": "Graph-Anchored Knowledge Indexing for Retrieval-Augmented Generation",
    "arxiv:2510.16582": "Can Knowledge-Graph-based Retrieval Augmented Generation Really Retrieve What You Need?",
    "arxiv:2603.00026": "ActMem: Bridging the Gap Between Memory Retrieval and Reasoning in LLM Agents",
    "doi:10.1007/978-981-96-0668-9_19": "Succinct Representations of Graphs",
    "doi:10.1016/j.ic.2021.104862": "A practical succinct dynamic graph representation",
    "doi:10.1016/j.neunet.2025.108056": "Dynamic graph representation learning with disentangled information bottleneck",
    # TKG-001: exact 2026 KG maintenance, provenance and original semiring baselines.
    "doi:10.1145/1265530.1265535": "Provenance semirings.",
    "doi:10.1177/22104968251412270": "Incremental Knowledge Graph Construction from Heterogeneous Data Sources",
    "doi:10.1007/978-3-032-26220-2_18": "Correct-by-Construction Dynamic Reachability: A Galois-Connected Approach to Bidirected Dyck Languages",
    "doi:10.48786/EDBT.2026.05": "In-memory Incremental Maintenance of Provenance Sketches",
    "arxiv:2510.13590": "RAG Meets Temporal Graphs: Time-Sensitive Modeling and Retrieval for Evolving Knowledge",
    "doi:10.18653/v1/2026.acl-long.1776": "Evolving Beyond Snapshots: Harmonizing Structure and Sequence via Entity State Tuning for Temporal Knowledge Graph Forecasting",
    # IMPORT-006B: late 2026 fresh primary references.
    "arxiv:2609.38353": "TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories",
    "arxiv:2609.40118": "Persistent Context Graphs for Efficient Memory Compaction in LLM Agents",
    "arxiv:2609.08599": "Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation",
    "doi:10.1162/tacl.a.615": "Dissecting GraphRAG: A Modular Analysis of Knowledge Structuring for Factoid Question Answering",
    "doi:10.18653/v1/2026.findings-acl.679": "WildGraphBench: Benchmarking GraphRAG with Wild-Source Corpora",
    "doi:10.18653/v1/2026.acl-short.47": "Defense Against Knowledge Poisoning Attack on GraphRAG",
    "doi:10.18653/v1/2026.findings-acl.290": "Breaking the Static Graph: Context-Aware Traversal for Graph-Based RAG",
    "doi:10.18653/v1/2026.findings-acl.321": "TagRAG: Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented Generation",
    "doi:10.63317/35ddm5i6bjyd": "Injecting Structured Biomedical Knowledge into Language Models:Continual Pretraining vs. GraphRAG",
    # IMPORT-006: graph/DAG/GraphRAG/agent memory: first-party title pins.
    "arxiv:2609.14066": "GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning",
    "arxiv:2609.18317": "Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering",
    "arxiv:2607.11464": "FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis",
    "arxiv:2606.26458": "MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation",
    "arxiv:2606.25656": "Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization",
    "arxiv:2606.00610": "MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation",
    "doi:10.1609/aaai.v40i36.40278": "You Don’t Need Pre-Built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures",
    "arxiv:2506.05690": "When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation",
    "arxiv:2510.10114": "LinearRAG: Linear Graph Retrieval Augmented Generation on Large-scale Corpora",
    "doi:10.18653/v1/2025.findings-emnlp.568": "LightRAG: Simple and Fast Retrieval-Augmented Generation",
    "arxiv:2501.00309": "Retrieval-Augmented Generation with Graphs (GraphRAG)",
    "arxiv:2501.13958": "A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models",
    "arxiv:2408.08921": "Graph Retrieval-Augmented Generation: A Survey",
    "arxiv:2404.16130": "From Local to Global: A Graph RAG Approach to Query-Focused Summarization",
    "arxiv:2402.07630": "G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering",
    "arxiv:2602.05665": "Graph-based Agent Memory: Taxonomy, Techniques, and Applications",
    "arxiv:2606.06036": "Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents",
    "arxiv:2601.03236": "MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents",
    "doi:10.18653/v1/2026.acl-demo.27": "Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects",
    "arxiv:2511.07800": "From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory",
    "arxiv:2511.15715": "Graph-Memoized Reasoning: Foundations Structured Workflow Reuse in Intelligent Systems",
    "arxiv:2501.13956": "Zep: A Temporal Knowledge Graph Architecture for Agent Memory",
    "arxiv:2502.12110": "A-MEM: Agentic Memory for LLM Agents",
    "arxiv:2502.14802": "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models",
    "doi:10.1609/aaai.v38i16.29720": "Graph of Thoughts: Solving Elaborate Problems with Large Language Models",
    "doi:10.14778/1920841.1920879": "GRAIL: Scalable Reachability Index for Large Graphs",
    "arxiv:2504.19413": "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory",
    "doi:10.18653/v1/2026.acl-long.252": "LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation",
    "doi:10.18653/v1/2026.acl-long.1738": "LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning",
    # INDEX-001 G2-B4-C3 MFCS25 and 2025 succinct B-tree primary pins.
    "doi:10.4230/LIPIcs.MFCS.2025.87": "Lazy B-Trees",
    "doi:10.1007/s00224-025-10238-7": "Space-Efficient B Trees via Load-Balancing",
    # INDEX-001 G2-B4-C2 SIAM SODA 2026 primary title pin.
    "doi:10.1137/1.9781611978971.65": "Tight Lower Bounds for Central String Queries in Compressed Space",
    # INDEX-001 G2-B4-A 2026 author abstracts, audited in primary arXiv.
    "arxiv:2603.23119": "Compressing Dynamic Fully Indexable Dictionaries in Word-RAM",
    "arxiv:2604.24080": "Dynamic Grammar-Compressed Self-Index in δ-Optimal Space",
    # INDEX-001 G2-B3-B publisher/author primary venue identities (2026).
    "doi:10.4230/LIPIcs.ITCS.2026.75": "Prior-Independent and Subgame Optimal Online Algorithms",
    "arxiv:2603.29233": "Robust and Consistent Ski Rental with Distributional Advice",
    "doi:10.1016/j.orl.2025.107382": "A new performance metric for the ski rental problem",
    # INDEX-001 G2-B3-A verified primary identities; LIT-205 reserved by parallel PR #132.
    "usenix:osdi25:leblanc": "PoWER Never Corrupts: Tool-Agnostic Verification of Crash Consistency and Corruption Detection",
    "doi:10.1145/2872362.2872406": "Specifying and Checking File System Crash-Consistency Models",
    "doi:10.15514/ISPRAS-2026-38(1)-7": "Lightweight file system crash-consistency checking with differential fuzzing",
    # UCT-005 G2-A new LIT-199..204 pins (STOC 2026 LIT-072 already present).
    "doi:10.1007/978-3-032-01878-6_6": "Merkle Mountain Ranges are Optimal: On Witness Update Frequency for Cryptographic Accumulators",
    "doi:10.1007/978-3-032-25330-9_7": "Lower Bounding Update Frequency in Short Accumulators and Vector Commitments",
    "doi:10.4230/LIPIcs.ITCS.2026.71": "Lower Bounds on FSS from Dynamic Data Structures",
    "doi:10.1007/978-3-642-00457-5_30": "How Efficient Can Memory Checking Be?",
    "publisher:iacr:2025-110": "Verification-efficient Homomorphic Signatures for Verifiable Computation over Data Streams",
    "doi:10.1007/978-3-642-14712-8_11": "On the Impossibility of Batch Update for Cryptographic Accumulators",
    # IMPORT-005 exact primary publisher DOI and title pin cohort.
    "doi:10.4230/LIPIcs.SEA.2025.9": "Incremental Reachability Index",
    "doi:10.4230/LIPIcs.ESA.2025.92": "Incremental Maximization for a Broad Class of Objectives",
    "doi:10.4230/LIPIcs.ESA.2025.93": "Recognizing and Realizing Temporal Reachability Graphs",
    "doi:10.4230/LIPIcs.ICALP.2025.93": "On Incremental Approximate Shortest Paths in Directed Graphs",
    "doi:10.4230/LIPIcs.STACS.2025.18": "Online Disjoint Set Covers: Randomization Is Not Necessary",
    "doi:10.4230/LIPIcs.ICALP.2026.16": "Fully Dynamic Algorithms for Coloring Triangle-Free Graphs",
    "doi:10.4230/LIPIcs.ICALP.2026.26": "Fast Decremental Tree Sums in Forests",
    "doi:10.4230/LIPIcs.ICALP.2026.44": "Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction",
    "doi:10.4230/LIPIcs.ICALP.2026.45": "Dynamic Rank, Basis, and Matching",
    "doi:10.4230/LIPIcs.ICALP.2026.157": "Fully Dynamic Spectral and Cut Sparsifiers for Directed Graphs",
    "doi:10.4230/LIPIcs.ESA.2026.125": "Incongruity-Sensitive Access to Highly Compressed Strings",
    "doi:10.4230/LIPIcs.SWAT.2026.21": "Dynamic MIS Revisited: Incremental, Fault Tolerant and Fully Dynamic",
    # INDEX-001 G2-A: separately verified compaction and adaptive bitvector identities.
    "doi:10.1007/s00224-025-10229-8": "(Worst-case) Optimal Adaptive Dynamic Bitvectors",
    "doi:10.1016/j.future.2026.108425": "C2LSM: A configuration paradigm for efficient compaction in LSM-tree-based key-value stores",
    "doi:10.14778/3796195.3796208": "ArceKV: Towards Workload-driven LSM-compactions for Key-Value Store Under Dynamic Workloads",
    "doi:10.1109/ICDE65706.2026.00194": "RangeReduce: Query-Driven LSM Compactions",
    # INDEX-001 G0: original source identity pins (six new works; no aliases duplicated).
    "doi:10.1137/S009753970240481X": "Optimal External Memory Interval Management",
    "doi:10.1137/110842211": "The Limits of Buffering: A Tight Lower Bound for Dynamic Membership in the External Memory Model",
    "doi:10.1109/FOCS57990.2023.00112": "Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries",
    "doi:10.1002/spe.3433": "Practical Adaptive Dynamic Bitvectors",
    "arxiv:2608.06066": "Dynamic Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space",
    "doi:10.1145/3654978": "Structural Designs Meet Optimality: Exploring Optimized LSM-tree Structures in a Colossal Configuration Space",
    # IMPORT-004: official source/title pins 2025–2026.
    "doi:10.4230/LIPIcs.ICALP.2025.123": "New and Improved Bounds for Markov Paging",
    "doi:10.1145/3717823.3718217": "Tight Results for Online Convex Paging",
    "doi:10.1145/3717823.3718131": "The Cost of Consistency: Submodular Maximization with Constant Recourse",
    "doi:10.4230/LIPIcs.ICALP.2025.111": "A Simple Dynamic Spanner via APSP",
    "doi:10.4230/LIPIcs.ICALP.2025.92": "Fully Dynamic Algorithms for Transitive Reduction",
    "doi:10.4230/LIPIcs.ICALP.2025.77": "Minimizing Recourse in an Adaptive Balls and Bins Game",
    "doi:10.1145/3717823.3718168": "Bounded Edit Distance: Optimal Static and Dynamic Algorithms for Small Integer Weights",
    "usenix:fast25:zhou-wenbin": "3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches",
    "usenix:osdi25:lyerly": "Skybridge: Bounded Staleness for Distributed Caches",
    "usenix:osdi25:park-sujin": "Principles and Methodologies for Serial Performance Optimization",
    "usenix:osdi26:li-liujia": "Merlin: An Efficient Adaptive Cache Eviction Algorithm via Fine-Grained Characterization",
    "usenix:osdi26:xia": "Learning-Augmented Heuristics: Simple Yet Smart, Robust and Interpretable Cache Eviction",
    "usenix:osdi26:mao-ziming-writeguards": "WriteGuards: Distributed Storage Support for Strongly Consistent Caches",
    "usenix:osdi26:xie-yizheng": "Incr: Faster Re-Execution via Bolt-On Incrementalization",
    "usenix:osdi26:yang-zhijun": "FORGE: Mitigating Synchronization Amplification for Memory-Disaggregated Caching Systems",
    "usenix:fast26:zhao": "\"Range as a Key\" is the Key! Fast and Compact Cloud Block Store Index with RASK",
    "usenix:fast26:ren": "Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage",
    "doi:10.1109/SFCS.1991.185352": "Checking the Correctness of Memories",
    "doi:10.1145/3618260.3649686": "Memory Checking Requires Logarithmic Overhead",
    "doi:10.1007/978-3-031-91092-0_11": "The Complexity of Memory Checking with Covert Security",
    "doi:10.4230/LIPIcs.AFT.2023.29": "Vector Commitments with Efficient Updates",
    # Authoritative arXiv title checks: forbid a paper ID being paired with
    # a hallucinated or different publication title.
    "arxiv:2501.01046": "SEDD: Scalable and Efficient Dataset Deduplication with GPUs",
    "arxiv:1507.00954": "Bounds and Constructions for overline-3-Separable Codes with Length 3",
    "arxiv:2509.11121": "The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality",
    "arxiv:2609.14442": "Toward Optimal Time-Space Tradeoffs for Set Reconciliation",
    "arxiv:2607.11271": "OptFSST: Optimized FSST String Compression",
    "arxiv:2602.08692": "PBLean: Pseudo-Boolean Proof Certificates for Lean 4",
    "arxiv:2607.00563": "Certificate-Carrying Transformation of Event-Driven Block Programs",
    "arxiv:2606.09600": "Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4",
    "arxiv:1503.07792": "Incremental Computation with Names",
    "arxiv:1407.3008": "Bigtable Merge Compaction",
    "arxiv:2011.02615": "Competitive Data-Structure Dynamization",
    "doi:10.4230/LIPIcs.CPM.2026.20": "Longest Common Extension of a Dynamic String in Parallel Constant Time",
    "arxiv:1211.1056": "How Robust are Linear Sketches to Adaptive Inputs?",
    "publisher:pmlr:cohen25c": "Breaking the Quadratic Barrier: Robust Cardinality Sketches for Adaptive Queries",
    "usenix:atc22:curtsinger": "Riker: Always-Correct and Fast Incremental Builds from Simple Specifications",
    "doi:10.4230/LIPIcs.MFCS.2024.46": "Query Maintenance Under Batch Changes with Small-Depth Circuits",
    "doi:10.4230/LIPIcs.ESA.2020.2": "Parallel Batch-Dynamic Trees via Change Propagation",
    "doi:10.4230/LIPIcs.ITCS.2020.56": "Instance Complexity and Unlabeled Certificates in the Decision Tree Model",
    "publisher:eccc:tr26-206": "Certification complexity of Boolean functions",
    "arxiv:2602.01042": "On Condensation of Block Sensitivity, Certificate Complexity and the $\\mathsf{AND}$ (and $\\mathsf{OR}$) Decision Tree Complexity",
    "doi:10.1016/S0304-3975(01)00144-X": "Complexity measures and decision tree complexity: a survey",
    "doi:10.1007/3-540-48658-5_22": "Incremental Cryptography: The Case of Hashing and Signing",
    "doi:10.1007/3-540-69053-0_13": "A New Paradigm for Collision-Free Hashing: Incrementality at Reduced Cost",
    # UCT-001 source-title identities (abstract/bibliography verified; not proof verified).
    "doi:10.1145/73007.73040": "The cell probe complexity of dynamic data structures",
    "doi:10.1137/S0097539705447256": "Logarithmic Lower Bounds in the Cell-Probe Model",
    "doi:10.1137/1.9781611973075.12": "On the Cell Probe Complexity of Dynamic Membership",
    "doi:10.1016/j.tcs.2007.02.058": "On dynamic bit-probe complexity",
    "doi:10.1016/j.tcs.2019.01.043": "New amortized cell-probe lower bounds for dynamic problems",
    "doi:10.1109/TIT.1973.1055037": "Noiseless coding of correlated information sources",
    "doi:10.1016/j.entcs.2005.11.043": "A Library for Self-Adjusting Computation",
    "doi:10.1002/rsa.20069": "Lower bounds for adaptive locally decodable codes",
    "publisher:eccc:tr26-047": "An $\\Omega((\\log n / \\log\\log n)^2)$ Cell-Probe Lower Bound for Dynamic Boolean Data Structures",
    "doi:10.1016/0095-8956(75)90067-2": "On cubical graphs",
    "doi:10.1016/S0019-9958(85)80012-7": "The complexity of cubical graphs",
    "doi:10.1016/0895-7177(88)90486-4": "Embeddings in hypercubes",
    "doi:10.1137/1.9781611975031.99": "Optimal Dynamic Strings",
    "doi:10.1016/j.tcs.2026.115746": "A textbook solution for dynamic strings",
    "publisher:c2sp:blake3-v1-0-0": "The BLAKE3 Hashing Framework (C2SP v1.0.0)",
    "doi:10.1007/s00224-026-10266-x": "Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts",
    # UCT-002 sourced identities, NOT full theorem proofs.
    "doi:10.1007/978-3-642-54242-8_21": "Locally Updatable and Locally Decodable Codes",
    "arxiv:1305.3224": "Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes",
    "doi:10.1145/2636924": "Annotations in Data Streams",
    "arxiv:1304.3816": "Annotations for Sparse Data Streams",
    "doi:10.4230/LIPIcs.ITCS.2024.53": "New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification",
    "doi:10.1016/j.ic.2014.12.011": "Arthur–Merlin streaming complexity",
    "doi:10.1016/j.ic.2019.05.001": "Tight upper and lower bounds for leakage-resilient, locally decodable and updatable non-malleable codes",
    "doi:10.1214/aoms/1177729032": "Equivalent Comparisons of Experiments",
    "doi:10.1016/0095-8956(91)90097-4": "Extremal graphs with no C4\'s, C6\'s, or C10\'s",
    "arxiv:1111.3279": "An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8",
    "doi:10.1090/proc/15673": "Constructing dense grid-free linear 3-graphs",
    "doi:10.1109/ISIT.2005.1523645": "Improved bounds on the size of sparse parity check matrices",
    "arxiv:2508.09841": "The Brown-Erdős-Sós conjecture in dense triple systems",
    "doi:10.37236/14115": "Triangle-Free Triple Systems",
    "doi:10.1137/090766619": "Bit-Probe Lower Bounds for Succinct Data Structures",
    # UCT-004 G2-A: certificate, adversary and 2026 R-vs-C original identities.
    "doi:10.1016/j.jcss.2007.06.020": "Quantum Certificate Complexity",
    "doi:10.1145/3442357": "All Classical Adversary Methods Are Equivalent for Total Functions",
    "arxiv:2609.15063": "Randomized Query Complexity Can Beat Certificate Complexity",
    "arxiv:2602.14716": "Grid-free linear hypergraphs via Cayley-Bacharach",
    "doi:10.1016/j.disc.2022.113025": "The linear Turán number of small triple systems or why is the wicket interesting?",
    "doi:10.1016/j.disc.2024.114029": "Wickets in 3-uniform hypergraphs",
    "doi:10.1006/jctb.2002.2123": "The Size of Bipartite Graphs with a Given Girth",
    "doi:10.1137/20M1325769": "New Turán Exponents for Two Extremal Hypergraph Problems",
    "doi:10.1007/s00493-008-2195-2": "Parity check matrices and product representations of squares",
    "arxiv:2609.39680": "Additive codes arising from hypergraphs",
    # G2-C original certification and PCPP source identities.
    "arxiv:2609.26757": "Certification complexity of Boolean functions",
    "doi:10.1145/1595391.1595394": "Sound 3-Query PCPPs Are Long",
    # G2-D source statement spotchecks (classical PPZ/MFCS).
    "doi:10.4086/cjtcs.1999.011": "Satisfiability Coding Lemma",
    "doi:10.4230/LIPIcs.MFCS.2022.47": "CNF Encodings of Parity",
}




def valid(data, catalog):
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    check(data.get("schema") == "mathlab.external-literature.v1", "invalid schema")
    snaps = data.get("source_snapshots", {})
    check(set(snaps) == SOURCE_REPOS, "unexpected/missing source snapshots")
    for key, source in snaps.items():
        check(key in SOURCE_REPOS and isinstance(source.get("repo"), str), "invalid snapshot repo")
        check(bool(SHA.fullmatch(source.get("sha", ""))), f"{key}: invalid snapshot SHA")

    allowed_research = {e["id"] for e in catalog["entries"]}
    entries = data.get("entries", [])
    check(isinstance(entries, list) and len(entries) >= 30, "literature corpus too small")
    seen_ids, seen_ident, seen_urls = set(), set(), set()

    for e in entries:
        ident = e.get("id", "?")
        check(bool(REPO_ID.fullmatch(ident)), f"{ident}: malformed ID")
        check(ident not in seen_ids, f"{ident}: duplicate ID")
        seen_ids.add(ident)
        ref = e.get("identity", "")
        check(bool(IDENTITY.fullmatch(ref)), f"{ident}: malformed canonical identity")
        aliases = e.get("alternate_identities", [])
        check(isinstance(aliases, list), f"{ident}: invalid alternate identity list")
        all_identity = [ref] + (aliases if isinstance(aliases, list) else [])
        for name in all_identity:
            if not isinstance(name, str):
                check(False, f"{ident}: invalid alternate identity")
                continue
            check(bool(IDENTITY.fullmatch(name)), f"{ident}: malformed canonical/alternate identity")
            check(name.lower() not in seen_ident, f"{ident}: duplicate canonical identity")
            seen_ident.add(name.lower())
        pinned_title = SOURCE_TITLE_PINS.get(ref)
        if pinned_title is not None:
            check(e.get("title") == pinned_title, f"{ident}: primary source title mismatch")
        authors = e.get("authors")
        if authors is not None:
            check(isinstance(authors, list) and bool(authors) and all(
                isinstance(a, str) and len(a) > 3 for a in authors
            ), f"{ident}: invalid author list")
        url = e.get("primary_url", "")
        check(bool(URL.fullmatch(url)), f"{ident}: malformed primary URL")
        check(url not in seen_urls, f"{ident}: duplicate primary URL")
        seen_urls.add(url)
        if ref.startswith("doi:"):
            check(url.lower() == "https://doi.org/" + ref[4:].lower(), f"{ident}: DOI mismatch")
        elif ref.startswith("arxiv:"):
            check(url.lower() == "https://arxiv.org/abs/" + ref[6:].lower(), f"{ident}: arxiv mismatch")
        check(isinstance(e.get("year"), int) and 1950 <= e["year"] <= 2026,
              f"{ident}: invalid year")
        for key in ("title", "summary_ru", "limits_ru"):
            check(isinstance(e.get(key), str) and len(e[key].strip()) >= 12,
                  f"{ident}: missing {key}")
        check(e.get("track") in TRACKS, f"{ident}: invalid track")
        if ident in NEW_2026_IDS:
            check(e.get("year") == 2026, f"{ident}: non-2026 cohort entry")
            check(e.get("publication_stage") in PUBLICATION_STAGES,
                  f"{ident}: unverified 2026 publication status")
            check(e.get("selection_priority") in PRIORITIES,
                  f"{ident}: missing 2026 selection priority")
            if e.get("publication_stage") == "peer_reviewed_proceedings":
                check(ref.startswith("doi:"), f"{ident}: proceedings DOI missing")
            check(all(o.get("kind") == "model_overlap" for o in e.get("mentioned_in", [])),
                  f"{ident}: invented existing citation; new survey must use model_overlap")

        if ident in VENUE_2026_IDS:
            check(e.get("year") == 2026, f"{ident}: venue-2026 cohort has non-2026 work")
            check(e.get("publication_stage") == "peer_reviewed_proceedings",
                  f"{ident}: 2026 venue cohort publication status incorrect")
            check(e.get("selection_priority") in PRIORITIES,
                  f"{ident}: 2026 venue cohort missing source priority")
            check(e.get("venue") in {"STOC 2026", "ICALP 2026", "EuroSys 2026"},
                  f"{ident}: 2026 venue cohort unknown venue")
            check(bool(URL.fullmatch(e.get("source_listing_url", ""))),
                  f"{ident}: primary 2026 venue URL missing")
            expected_listing = {
                "STOC 2026": "https://acm-stoc.org/stoc2026/toc.html",
                "ICALP 2026": ("https://drops.dagstuhl.de/entities/document/" + ref[4:]
                               if ref.startswith("doi:") else ""),
                "EuroSys 2026": "https://2026.eurosys.org/papers.html",
            }
            check(e.get("source_listing_url") ==
                  expected_listing.get(e.get("venue")),
                  f"{ident}: primary 2026 listing/identity mismatch")
            check(e.get("verification") in {"publisher_abstract_checked",
                                             "publisher_bibliography_checked"},
                  f"{ident}: unsupported 2026 full-text verification")
            check(e.get("source_access") in {
                "official_conference_toc_abstract_linked_doi",
                "publisher_article_abstract_and_bibliography_checked",
                "conference_paper_list_and_delsk_fulltext_review"},
                  f"{ident}: unknown 2026 source access")
            check(all(o.get("kind") == "model_overlap"
                      for o in e.get("mentioned_in", [])),
                  f"{ident}: false explicit citation for imported 2026 paper")

        check(e.get("verification") in VERIFICATIONS, f"{ident}: invalid verification")
        check(e.get("full_proof_verified") is False and
              e.get("independent_reproduction") is False,
              f"{ident}: unsupported proof/reproduction promotion")
        relates = e.get("maps_to", [])
        check(isinstance(relates, list) and len(relates) >= 1, f"{ident}: missing research links")
        for rid in relates:
            check(rid in allowed_research, f"{ident}: dangling research link {rid}")
        check(len(relates) == len(set(relates)), f"{ident}: duplicate research mapping")
        mentions = e.get("mentioned_in", [])
        check(isinstance(mentions, list) and len(mentions) >= 1,
              f"{ident}: missing pinned provenance")
        seen_origins = set()
        for origin in mentions:
            r = origin.get("repo")
            path = origin.get("path", "")
            check(r in SOURCE_REPOS, f"{ident}: origin repository invalid")
            check(origin.get("kind") in ("cited", "model_overlap"),
                  f"{ident}: origin kind invalid")
            if "source_sha" in origin:
                check(bool(SHA.fullmatch(origin["source_sha"])),
                      f"{ident}: origin pin SHA malformed")
            check(bool(path) and not path.startswith("/") and
                  ".." not in Path(path).parts and path.endswith(".md"),
                  f"{ident}: origin path unsafe")
            check((r, path) not in seen_origins, f"{ident}: duplicate origin")
            seen_origins.add((r, path))
    return errors


def manuscript_link(e):
    return f"[{e['title']}]({e['primary_url']})"


def source_link(snapshot, origin):
    source = snapshot[origin["repo"]]
    path = origin["path"]
    return (f"[{origin['repo']}:{path}]("
            f"https://github.com/{source['repo']}/blob/{origin.get('source_sha', source['sha'])}/{path})")


def render(data):
    rows = data["entries"]
    snap = data["source_snapshots"]
    groups = defaultdict(list)
    for e in rows:
        groups[e["track"]].append(e)
    out = [
        "# External primary literature — тематический каталог",
        "",
        "> Generated from `literature.json` by `research/literature.py`. "
        "Редактировать следует только JSON.",
        "",
        f"Срез: **{data['snapshot_date']}** · **{len(rows)}** проверенных ссылок "
        "на первичные публикации/авторские рукописи.",
        "",
        "**Критически важно:** проверенная библиография или авторский abstract "
        "не равны независимо проверенному доказательству, статистическому "
        "результату либо научной новизне. Точные условия — в каждой записи.",
        "",
        "Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md]"
        "(LITERATURE-BY-RESEARCH.md). "
        "Внутренние исследования: [INDEX.md](INDEX.md).",
        "",
        "| Направление | Записей |",
        "| --- | ---: |",
    ]
    for track, title in TRACKS.items():
        out.append(f"| [{title}](#{track}) | {len(groups[track])} |")
    for track, title in TRACKS.items():
        out += ["", f"## {track}", f"*{title}*", ""]
        for e in sorted(groups[track], key=lambda x: x["id"]):
            links = ", ".join(
                f"[{item}](INDEX.md#{item.lower()})" for item in e["maps_to"])
            sources = "; ".join(
                f"{source_link(snap, o)} ({o['kind']})" for o in e["mentioned_in"])
            out += [
                f"### {e['id']}",
                f"**{manuscript_link(e)}** ({e['year']})",
                "",
                e["summary_ru"],
                "",
                f"**Ограничение:** {e['limits_ru']}",
                "",
                f"**Идентичность:** `{e['identity']}`"
                + (f" · **Также:** {', '.join(e['alternate_identities'])}"
                   if e.get("alternate_identities") else "")
                + (f" · **Авторы:** {', '.join(e['authors'])}"
                   if e.get("authors") else "")
                + " · "
                + f"**Проверка:** `{e['verification']}` · "
                "**Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.",
                "",
                *([f"**Первоисточник / издательский список:** "
                    f"[{e['venue']}]({e['source_listing_url']}) · "
                    f"**Доступ:** `{e['source_access']}`", ""]
                  if e.get("source_listing_url") else []),
                f"**Связь с исследованиями →** {links}",
                "",
                f"**Происхождение цитаты / пересечения →** {sources}",
                "",
            ]
    return "\n".join(out).rstrip() + "\n"


def render_reverse(data, catalog):
    by_research = defaultdict(list)
    for e in data["entries"]:
        for rid in e["maps_to"]:
            by_research[rid].append(e)
    out = [
        "# External literature by Mathlab research record",
        "",
        "> Generated from `literature.json` and `registry.json`. "
        "Связи обозначают релевантность, но не логическое следствие.",
        "",
        f"**{len(data['entries'])}** работ сопоставлены с "
        f"**{len(by_research)}** внутренними исследованиями.",
        "",
        "[Основной индекс литературы](LITERATURE.md) · "
        "[Индекс исследований](INDEX.md)",
        "",
    ]
    for rec in sorted(catalog["entries"], key=lambda z: z["id"]):
        related = by_research.get(rec["id"])
        if not related:
            continue
        out += [f"## {rec['id']}", "",
                f"**[{rec['title']}](INDEX.md#{rec['id'].lower()})**", ""]
        for e in sorted(related, key=lambda x: x["id"]):
            out.append(
                f"- [{e['id']}](LITERATURE.md#{e['id'].lower()}) — "
                f"{e['title']} ({e['year']}; {e['verification']})"
            )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument("--check", action="store_true")
    command.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))
    errors = valid(data, catalog)
    if errors:
        for error in errors:
            print("LITERATURE_ERROR:", error)
        raise SystemExit(1)
    expected = render(data)
    expected_reverse = render_reverse(data, catalog)
    if args.write:
        INDEX.write_text(expected, encoding="utf-8")
        REVERSE.write_text(expected_reverse, encoding="utf-8")
    else:
        if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != expected:
            raise SystemExit("LITERATURE_ERROR: LITERATURE.md drift; run --write")
        if not REVERSE.exists() or REVERSE.read_text(encoding="utf-8") != expected_reverse:
            raise SystemExit("LITERATURE_ERROR: LITERATURE-BY-RESEARCH.md drift; run --write")
    print("LITERATURE_SCHEMA_AND_SOURCE_PINS_PASS")
    print("LITERATURE_CANONICAL_IDENTITIES_PASS")
    print("LITERATURE_GENERATED_DOCUMENTS_PASS")
    print("LITERATURE_NO_NOVELTY_PROMOTION_PASS")


if __name__ == "__main__":
    main()
