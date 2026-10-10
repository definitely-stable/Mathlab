# DAG-002 G2-B1 — SEA 2025 record-based anchor component and exact virtual page ledger

**Owner:** [G2 #322](https://github.com/definitely-stable/Mathlab/issues/322), [G2-A #324](https://github.com/definitely-stable/Mathlab/pull/324). **Primary:** Bulteau–David–Horn–Tran-Girard, [SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9), [full official HTML §§2–3.2.1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol338-sea2025/html/LIPIcs.SEA.2025.9/LIPIcs.SEA.2025.9.html), canonical LIT-187.

**Status:** RESTRICTED_CONSTRUCTIVE_BASELINE / EXACT_FINITE_DFS / SOURCE_MODEL_DISTINCTION / NOVELTY_UNPROVED / NOT_FULL_FELSNER_REPRODUCTION / NO_ACTUAL_DEVICE_IO.

## 1. Exact source correspondence and boundary

Implements paper Section 3.2.1 **record-score Anchor Strategy 1**, but uses Mathlab's **first-compatible** online chain assignment, NOT the paper's Felsner chain-decomposition algorithm. It does not implement §3.2.2 power-based anchors, reproduce experiments, or independently establish source bounds and high-probability performance. This is a **component-level adaptation**, not a complete SEA-index reproduction.

Each immutable label stores chain ID, anchor ID and restricted top pairs. The top of a chain under vertex v is its latest ancestor of v. With anchor a being an older ancestor of v, the restricted top on chain C is the latest ancestor of v which is **not** an ancestor of a. Full top(v,C) is its restricted top, if present, otherwise recursively top(a,C). Query reach(u,v) returns whether u is no later than recovered top(v,chain(u)). A new vertex combines parent top maps by coordinatewise maximum, extends the first compatible chain (or creates a new one), and picks an anchor among parent anchor-list members having a greater score. The choice minimizes the restricted top count and then applies depth cap D to that chosen candidate, with deterministic depth/vertex tie breaking (not filtering candidates before minimization). The reference chooses the best eligible candidate even when it does not strictly reduce the top-pair count, matching the selection rule in SEA 2025 Strategy 1.

A deterministic BLAKE2b hash supplies reproducible pseudo-random scores for vertex IDs; these are **not mathematically independent continuous random variables**, so no high-probability theorem from SEA 2025 is claimed. Historical parent records are stored exclusively for test construction, not used in query.

## 2. Explicit serialized byte/page cost model

- Page P is **16 application bytes**. Identifier width d is frozen by the declared horizon. Simulated serialized label bytes = 2d+2+2dk where k is the number of restricted top pairs; manifest bytes = 4+d*c for c chains. The record image is modeled by a length formula: it is NOT written to actual disk pages.
- Cold update charges all old-manifest pages and each old label read once per invocation, including parent and anchor traversal, with full ceil(record_bytes/P) page transfers. Append writes a new immutable label and fully rewrites the current manifest.
- Cold query reads the complete source label, then target and successive anchor records until the relevant chain top resolves; queries never see free parent-input incidence rows. Every transfer is billed 1+2d logical address bytes separately from application bytes.
- Parent command counts v input bits for a vertex of insertion index v; updater logical buffering gets a conservative explicit byte envelope, **not** Python RSS.
- Excluded: actual page contents, allocator and physical directory, fsync and torn writes, CAS/root publication, PIN/GC, concurrent readers, SSD/NAND IOPS, network transfer timings, encryption, Byzantine adversary, wall-clock CPU or actual full-process RAM measurements.

## 3. Independent finite oracle and non-dominance result

The tests cover **all 1024** topologically ordered DAGs on five vertices, with D=1, 3, 8 and unbounded, checking old-label immutability and **all pair queries after every append** against an independent backward DFS. Six unit tests also verify zero/invalid parents, record-score monotonicity, depth bounds and complete transfer/address ledger formulas.

For an exactly specified 160-vertex fan-in graph (32 independent source vertices, their common child, then 127 additional chain vertices), page P=16, seed 73, *same record codec*:

| Scheme | Live label pages | Update page reads | Update page writes | Four query page reads | Current manifest pages |
| --- | ---: | ---: | ---: | ---: | ---: |
| No anchor, D=1 | 672 | 1105 | 1112 | 22 | 3 |
| Record anchors, D=3 | 192 | 1226 | 632 | 15 | 3 |

The four queries are (0,159), (31,159), (32,159), (159,159). On this exact trace, anchors make labels **3.5× smaller** and reduce writes while increasing updater reads by 121 pages; no universal performance or asymptotic conclusion follows. On a 160-vertex chain and a 160-vertex antichain, each vertex has one label page with the reference D=8; there is no universal anchor storage gain.

**Fairness limitation:** G1-C2-C uses a different label header and page-key serialization, so its earlier bitmap/chain results are NOT a same-codec head-to-head comparison. These two rows vary only D in this implementation; a full SEA vs bitmap comparison requires a unified serializer and the source's real Felsner procedure.

## 4. Reproducibility and next gate

Run these exact Python stdlib commands:

    python research/dag002_g2b_record_anchors.py
    python -m unittest discover -s research -p 'test_dag002_g2b_record_anchors.py' -v

Focused GitHub-hosted workflow and full Research CI must both succeed at the **exact PR SHA** before merger. No changes to bibliographic IDs, UCT root or production code, and no forced merges.

**G2-B2:** implement source-faithful Felsner online chain selection (not first-compatible), with a primary proof/pseudocode correspondence matrix, and separately SEA §3.2.2 power-based anchors. Harmonize serialized page images and manifest costs before any full cross-algorithm comparisons. If this cannot be validated, explicitly retain FIRST_COMPATIBLE / PARTIAL_SEA status.
