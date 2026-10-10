# IMPORT-012 — scientific cross-study audit, corrected Deep Research sources and source genealogy

**Date:** 2026-10-10. **Parent issues:** [#228](https://github.com/definitely-stable/Mathlab/issues/228), [#236](https://github.com/definitely-stable/Mathlab/issues/236), [HYP-105 #95](https://github.com/definitely-stable/Mathlab/issues/95), [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105). Baseline main: `975a33afd15552830d523e2ac4868f7f431a6334` (364 canonical records). Sources: two user-provided, untrusted Deep Research PDFs (31-page *От пробелов в литературе к новым теоремам*; 30-page *Фундаментальные математические связи, пробелы покрытия и междисциплинарное расширение исследовательской программы Mathlab*), reconciled with original DOI, official publisher, arXiv and ACL Anthology records.

**Scope:** verified publication identities, metadata, limitations and typed conceptual genealogy; **no imported source theorem is independently reproved**, no benchmark is independently reproduced, and **no Mathlab theorem/exponent is promoted**. PDF recommendations are NOT source authority; neither report may be cited as proving a theorem. Baseline source identity matching includes lowercase DOI, title, arXiv aliases, publication versions. This document explicitly preserves prior IMPORT-011 LIT-357..365 and avoids duplicate publication records.

## 1. Corrected bibliographic claims and prior-art gates

| Claim in external PDFs | Source-grounded correction | Decision |
| --- | --- | --- |
| Komargodski–Lin, ORAM all parameters, DOI `10.1137/23M1559821`, universal `Omega(log N)` | Actual SIAM J. Comput. 2025 DOI **[10.1137/21M1428431](https://doi.org/10.1137/21M1428431)** (CRYPTO 2021 earlier version). In a specified online vs offline ORAM setting they prove `Omega(log N/log log N)` amortized online probes against offline o(1). Do not infer a universal authentication/INDEX bound. | IMPORT |
| Alman–Dai, “Cell-Probe Lower Bounds from Online Communication Complexity”, arXiv 2602.04551 | Exact original work is Alman–**Wang–Yu**, STOC **2018**, [arXiv:1704.06185](https://arxiv.org/abs/1704.06185). The model distinguishes online Bob inputs from ordinary one-shot communication; do not silently assign 2026 result/author. | IMPORT corrected |
| “Optimal Cell-Probe Reductions for Suffix Arrays and Prefix Range Queries”, Kociumaka–Kosolobov, 2026 | Actual [arXiv:2608.19172](https://arxiv.org/abs/2608.19172) is **Kempa–Kociumaka**, *Cell-Probe Lower Bounds and Complexity-Preserving Reductions for Suffix Array Queries*. Static suffix-query lower bound, not dynamic recourse. | IMPORT corrected |
| `10.4230/LIPIcs.CCC.2026.41` claimed absent/other article in a preliminary audit | **The original Dagstuhl record confirms .41 IS** *Systematic Data Structure Lower Bounds via the Query-With-Sketch Model* (Garg, He, Li, Papakonstantinou, Yang); [DOI 10.4230/LIPIcs.CCC.2026.41](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2026.41). `.42` is Fedor Kiselev, unrelated black-box TFNP. Never use `.42` for the sketch paper. | IMPORT verified |
| “Counting de Bruijn Graphs Index k-mer Abundances”, gr.276404.121 | Actual paper: Karasikov–Mustafa–Rätsch–Kahles, *Lossless indexing with counting de Bruijn graphs*, [DOI 10.1101/gr.276607.122](https://doi.org/10.1101/gr.276607.122) (2022); author-reported 8x smaller example refers to a particular indexed RNA-seq corpus, not a universal bound. | IMPORT corrected |
| Hickey–Sirén `10.3389/fgene.2025.1679660` | Actual review is **Nyaga, Zaied, Silander, Black, O'Sullivan**, *Beyond single references: pangenome graphs and the future of genomic medicine*, [DOI](https://doi.org/10.3389/fgene.2025.1679660). This is a genomic **survey**, not a DAG lower-bound theorem. | IMPORT corrected |
| Campos–Samotij 2026 `10.1007/s00493-025-00180-2` | Correct published 2026 Combinatorica DOI **[10.1007/s00493-026-00214-1](https://doi.org/10.1007/s00493-026-00214-1)**; authors examine uniform-hypergraph containers and alternative approximate-independence definitions; not free for mixed 4/6 weighted signed trades. | IMPORT corrected |
| Regular lines in rank-3 polar spaces, `10.1016/j.ffa.2024.102569` | Actual authors Ihringer–Rodgers. First arXiv 2023, journal volume 2025, DOI string contains 2024. Requires exact finite-polar-space conditions. | IMPORT |
| Fractional clique decomposition `10.1112/blms.13110` | Real Delcourt–Lesgourgues–Postle work first arXiv 2025, final DOI **[10.1112/blms.70382](https://doi.org/10.1112/blms.70382)**; threshold for fractional clique decomposition of dense *r-uniform hypergraphs*, not signed-trade containers. | IMPORT corrected |
| *A common generalization of hypercube partitions and ovoids in polar spaces* | D'haeseleer–Ihringer–Schmidt, DOI [10.1007/s10623-024-01489-5](https://doi.org/10.1007/s10623-024-01489-5), first preprint 2024; obstructions in high-rank polar geometries, not a GF(5) ASET theorem. | IMPORT |
| 2024 ACL temporal TPAR, 2024 EMNLP NEDA and 2025 NeusymBridge CEGRL-TKGR | Official ACL Anthology confirms primary identities and authors; CEGRL has no verified DOI at ACL entry, so pin its ACL publisher identifier instead of fabricating a DOI. | IMPORT with empirical-only labels |
| GraphRAG-R1, arXiv 2507.23581 | Actual authors Yu et al.; it is a reinforcement-learning/adaptive-retrieval method, **not** a proof of complete causal/graph provenance. | IMPORT empirical |
| "Embedding-Based RAG Outperforms GraphRAG", DOI `10.5281/zenodo.edm2026.386` | Correct official proceedings title *Comparing RAG and GraphRAG for Page-Level Retrieval Question Answering on a Math Textbook*, [DOI 10.5281/zenodo.21039806](https://doi.org/10.5281/zenodo.21039806) (published 2026, preliminary arXiv 2025). Authors' negative result restricted to **477 QA pairs for a math textbook**; never generalize to all GraphRAG. | IMPORT negative control |
| Source genealogy not provided in either PDF | Old foundation: **Saxton–Thomason** [DOI 10.1007/s00222-014-0562-8](https://doi.org/10.1007/s00222-014-0562-8); **Balogh–Morris–Samotij** [DOI 10.1090/S0894-0347-2014-00816-X](https://doi.org/10.1090/S0894-0347-2014-00816-X), online 2014/journal 2015; methodological survey [arXiv:1801.04584](https://arxiv.org/abs/1801.04584); 2026 Campos–Samotij and existing LIT-360. | IMPORT / crosslinks |

## 2. Typed cross-disciplinary research graph

See [`IMPORT-012-SOURCE-GENEALOGY.json`](IMPORT-012-SOURCE-GENEALOGY.json) for machine-readable edges. An edge may mean source-reference relation, explicit methodological extension, compatible mathematical object, or hypothesis of possible transfer — **not** automatically logical derivation.

1. **Sparse forbidden configurations (HYP-105):** BMS 2015 / Saxton–Thomason 2015 → BMS 2018 survey → Campos–Samotij 2026 → existing LIT-360 2026 counting linear-cycle-free hypergraphs → HYP-105 G5-C2 actual signed trade forbidden hypergraph **requires independent balanced supersaturation and codegree bounds**. Freeze two models: restricted all-one 2+2 mixed 4/6 edges versus unrestricted weighted support≤4 including unbalanced 3-vs-2. None of these works proves full ASET exponent.
2. **Polar geometry and extremal rank (HYP-105/LENT-001):** finite classical polar spaces and rank-5 association schemes → Ihringer–Rodgers line-regular-set spectrum / D'haeseleer–Ihringer–Schmidt generalized ovoid nonexistence / Ihringer–Kupavskii 2026 vector-space sunflowers using MRD codes → possible finite-geometry constructions. All relevance is **model overlap**; no signed-trade injectivity reduction verified.
3. **Communication/information lower bounds (UCT-005/INDEX-001):** original Alman–Wang–Yu online communication 2018 + Komargodski–Lin ORAM 2021/2025 + existing cell-probe work LIT-298/352/353 → 2026 Garg et al. query-with-sketch/min-entropy lower bounds → compare to UCT authenticated history, Byzantine freshness and paid physical rewrites **only on the exact same task/model**.
4. **Genomic compression and DAG indexing (DAG-002/INDEX-001):** existing LIT-321 Bifrost colored compacted DBG and LIT-322 buffered dynamic DBG → Karasikov et al. counting DBG 2022 → existing LIT-328 multidollar-BWT pangenome index 2025 → Nyaga et al. genomic medicine survey 2025. These algorithms index **declared sequence/haplotype paths** and k-mer counts, not arbitrary DAG transitive closure or crash consistency.
5. **Temporal causal retrieval (TKG-001):** TPAR 2024 interpolation/extrapolation + NEDA 2024 asynchronous event patches + CEGRL 2025 causal/confounder representation + existing LIT-273 DYNA + GraphRAG-R1 adaptive 2025/2026 → contrast the 2026 Chen et al. negative page-retrieval comparator. This is an evaluation/research-family DAG, **not** a claim of actual paper-to-paper citation or a proved SCM causal effect.

## 3. Exact mathematical obligations / no-transfer criteria

For any hypergraph-container transfer, define a **single r-uniform** auxiliary hypergraph or a clearly justified way to handle mixed edge sizes 4,6, `Delta_j`, `e(H)`, finite container parameters, a signed-coefficient-consistent incidence model and an actual supersaturation lemma. A bare hypergraph formalization (`G5-C2`) is not sufficient.

For query-with-sketch/ORAM, the source assumes a particular systematic static matrix and offline/online oblivious access experiment respectively; these **do not imply** arbitrary authenticated/GC/freshness physical I/O lower bounds. For causal graph memory, a model that predicts links under interventions **does not authenticate factual origin**. For genomic compressed indexes, indexing stored strings/paths is **not** unrestricted DAG reachability.

**STOP:** if a source's formal assumptions cannot be mapped to the current Mathlab task or theorem without changing the query, update model, adversary, metric or coefficient restrictions, tag `NO_TRANSFER`; preserve source as prior art only.

## 4. Disposition of all 32 items in the second PDF

| PDF item | Final scientific disposition |
| --- | --- |
| 1 memory checking | ALREADY_PRESENT LIT-157; wrong author/DOI universal-bound statement rejected |
| 2 ORAM | IMPORT corrected DOI 10.1137/21M1428431 |
| 3 online communication cell-probe | IMPORT original 2018 Alman–Wang–Yu; 2026 title/author/year rejected |
| 4 CSP odd-locality | ALREADY_PRESENT LIT-359; report's 2025 SODA DOI unverified |
| 5 suffix-array lower bounds | IMPORT original Kempa–Kociumaka arXiv:2608.19172 |
| 6 Cauchyproofs | ALREADY_PRESENT LIT-358; report's DOI rejected |
| 7 vector commitments Tas–Boneh | ALREADY_PRESENT LIT-159; report's version conflation rejected |
| 8 fully dynamic transitive reduction | ALREADY_PRESENT LIT-164; wrong author/bound corrected in IMPORT-011 |
| 9 LycheeMemory V2 | ALREADY_PRESENT LIT-364 |
| 10 TPAR temporal interpolation/extrapolation | IMPORT corrected ACL authors and DOI |
| 11 NEDA asynchronous TKG | IMPORT official ACL Anthology |
| 12 CEGRL-TKGR | IMPORT with ACL publisher identity (no verified DOI), experimental only |
| 13 TimE temporal benchmark | IMPORT original NeurIPS 2025 TIME [arXiv:2505.12891](https://arxiv.org/abs/2505.12891), benchmark only; no proof of freshness or causality |
| 14 GraphRAG-R1 | IMPORT correct preprint metadata |
| 15 negative GraphRAG baseline | IMPORT corrected official proceedings title/DOI |
| 16 FAIR GraphRAG | ALREADY_PRESENT **LIT-216** (arXiv:2607.11464); official ICKG 2025 [DOI 10.1109/ICKG66886.2025.00019](https://doi.org/10.1109/ICKG66886.2025.00019) added as alias; no duplicate |
| 17 dynamic pangenome via RLE skiplists/syncmers | IMPORT Richard Durbin 2026 non-reviewed bioRxiv [DOI 10.64898/2026.03.26.714584](https://doi.org/10.64898/2026.03.26.714584); path-set queries, no full DAG reachability guarantee |
| 18 counting de Bruijn | IMPORT corrected original paper and DOI |
| 19 Bifrost | ALREADY_PRESENT LIT-321; report's Nature DOI is wrong |
| 20 HEDGES | ALREADY_PRESENT LIT-365 |
| 21 non-symmetric DNA storage codes | NEEDS_SOURCE_IDENTITY_RECHECK; no GF(5) equivalence |
| 22 genomic pangenome overview | IMPORT corrected real review/actual authors |
| 23 2026 hypergraphs without linear cycles | ALREADY_PRESENT LIT-360; wrong report authors corrected |
| 24 optimal container lemma | IMPORT official Campos–Samotij 2026 DOI |
| 25 regular sets polar rank 3 | IMPORT original publisher identity |
| 26 generalized ovoids | IMPORT original first-online 2024 |
| 27 weak Sidon subsets | ALREADY_PRESENT LIT-362; wrong report arXiv/bound corrected |
| 28 formal Singer Lean | ALREADY_PRESENT LIT-363; authors corrected |
| 29 fractional clique decompositions | IMPORT corrected final DOI 10.1112/blms.70382 |
| 30 semiring provenance OASIcs 2024-25 report | REJECT_AS_PRIMARY: composite report-style identity unverified; actual foundational semiring provenance ALREADY_PRESENT LIT-252 |
| 31 dynamic fully indexable dictionaries | ALREADY_PRESENT LIT-212; report's ACM pseudo-DOI rejected |
| 32 dynamic meta-kernelization | IMPORT official STOC 2026 DOI 10.1145/3798129.3800774, **not** the report's pseudo-DOI |

The first PDF also contains blogs, index pages, and other low-information/secondary sources; these are **not automatically promoted to canonical scientific publications**. Verified relevant material is treated as explicit source-graph ancestry/descendancy and catalog candidate; speculative theorem-formulas remain in quarantine.

## 5. Additional source-grounded reviews

TIME temporal benchmark (LIT-386) and Durbin dynamic GBWT preprint (LIT-387) are source-verified late additions. FAIR GraphRAG is **ALREADY_PRESENT LIT-216**, correctly deduplicated with ICKG 2025 DOI as a new alternate identity; the report's incorrect earlier deferral has been superseded. No author-reported benchmark is independently reproduced. Source genealogy distinguishes method-family rather than literal citations.

## 6. Acceptance

- Distinct canonical identities; primary source URLs matching DOI/arXiv or verified ACL publisher record; first-online dates versus journal dates explained.
- Generated forward/reverse index from canonical JSON; source title pins, tests, typed source genealogy.
- Original proofs and empirical results are **NOT independently reproduced**; no novelty promotion or product release.
- GitHub-hosted exact-HEAD CI SUCCESS and postmerge verification before acceptance; protect concurrently open bibliography PR #132.
