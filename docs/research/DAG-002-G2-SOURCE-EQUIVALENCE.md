# DAG-002 G2-A — source-equivalent reachability gate, primary-work matrix and finite non-transfer oracles

**Authority:** [DAG-002 G2 #322](https://github.com/definitely-stable/Mathlab/issues/322) → [G1-C #161](https://github.com/definitely-stable/Mathlab/issues/161) → [G1 #140](https://github.com/definitely-stable/Mathlab/issues/140). Related UCT-005 root [#105](https://github.com/definitely-stable/Mathlab/issues/105).

**Evidence classification:** SOURCE_SCOPE_CHECKED / FINITE_MODEL_BARRIERS / NOVELTY_UNPROVED / NO_GENERAL_LOWER_BOUND / NO_AUTH_TRANSFER. This slice is not a new theorem, paper reproduction, disk benchmark, proof-level publication audit, or comparison against the full SEA 2025 anchor algorithm.

## 1. Exact target type and scientific question

The target update is **APPEND_SINK(v,S)**: vertices are numbered in topological insertion order, v is fresh, and each new directed arc p→v has p<v. The *entire* S is a charged input to the updater; no future query sees S for free. Old arcs and old-old Boolean reachability remain immutable. Reachability includes the zero-length u=v path. The target query is reach(u,t) returning one **Boolean** bit for a specified pair. Different observables, such as path parity modulo 2, matrix-rank scalar, complete ancestor vector, negative proof, and verified latest epoch are separate contracts.

Resources to freeze in a future theorem (none given for free): immutable per-vertex labels, trusted mutable H bits and previous update cost, external N c-bit cells, total remote S bytes, updater old-source reads R_u, updater remote reads/writes W_phys, net Hamming changes W_net, query probe P_q, number and adaptivity of queries Q, fixed codebook T, page size/cold caches, persistent layout, RAM cap, crash model and trust/root freshness. Do **not** conflate a cell with a page, memory overwrite with bit change, one-step state count with viable online transitions or unconditional proof size with prover CPU.

The problem is **not** closed just because a source is called a dynamic graph paper. Every transfer requires a cost-preserving reduction on the *same allowed update alphabet and query output*.

## 2. Original sources mapped to the actual model

The auditable machine-readable table is [DAG-002-G2-SOURCE-EQUIVALENCE.json](DAG-002-G2-SOURCE-EQUIVALENCE.json). Each row has a canonical LIT ID where present, one primary URL, actual update/query types, resource scope, relation type, provenance granularity and an explicit **restriction**. This table can be indexed as a typed research graph without equating ANALOGY_ONLY with THEOREM_TRANSFER.

| Source (catalog) | What is supported by the primary source | Relation to APPEND_SINK |
| --- | --- | --- |
| [Bulteau et al., SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9) (**LIT-187**) | Immutable append-only reachability labels with chains/anchors and mutable manifest | **Direct algorithmic baseline**; first-compatible chain is NOT its anchor implementation |
| [Chandran–Kanukurthi–Ostrovsky, TCC 2014](https://doi.org/10.1007/978-3-642-54242-8_21) (**LIT-127**) | Locally decodable/updatable codes including Prefix Hamming error model | Related coding tradeoff, but not same DAG update or physical I/O |
| [Pătraşcu–Tarniţă, TCS 2007](https://doi.org/10.1016/j.tcs.2007.02.058) (**LIT-114**) | Dynamic bit-probe problems with specific membership/partial-sum operators | General lower-bound techniques, no free same-model theorem |
| [Larsen–Yu, SIAM 2025 / FOCS 2023](https://doi.org/10.1137/24M1638215) (**LIT-298**) | Cell-probe lower bound for dynamic DAG reachability under **edge insertions** | **No identity-preserving transfer** to new-sink-only updates |
| [Ko, ECCC TR25-156](https://eccc.weizmann.ac.il/report/2025/156/) (**catalog backlog #147**) | One-way communication → dynamic cell-probe translation under a hard f, public S_i, product distribution | A new reduction must preserve input distribution, query and update language |
| [Ko, ECCC TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) (**LIT-119**) | Boolean Multiphase cell-probe lower bound using 2.5-round communication | NOT a blanket Boolean reachability or authenticated DAG bound |
| [Koucký–Loff–Molli–Saks, STOC 2026](https://acm-stoc.org/stoc2026/toc.html) (**LIT-072**) | Natural-proofs methodological barrier in data-structure lower bounds | A **methodological** warning, not impossibility for every model |
| [Tas–Boneh, AFT 2023](https://doi.org/10.4230/LIPIcs.AFT.2023.29) (**LIT-159**) | Vector-commitment proof update/information tradeoffs | Different authenticated proof-update query |
| [Abusalah et al., EUROCRYPT 2026](https://doi.org/10.1007/978-3-032-25330-9_7) (**LIT-200**) | Update frequency of short accumulators/vector commitments under explicit assumptions | Different authenticated witness model |
| [Graph Reachability Index Survey, ACM CSUR 2025](https://doi.org/10.1145/3776737) (**LIT-301**) | Taxonomy of graph reachability indexes | Comparator discovery, not online immutable-label guarantee |
| [Cohen–Lobstein–Sloane, IEEE IT 1986](https://doi.org/10.1109/TIT.1986.1057227) (**catalog backlog #147**) | Classical Hamming covering-radius/code-size bounds | Only fixed-coordinate XOR-center submodel |
| [Dynamic Rank, Basis, and Matching, ICALP 2026](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) (**LIT-195**) | Rank and basis changes under matrix updates | Rank scalar ≠ coordinate membership |

**Verification limit:** source identities, official abstracts and the problem/model scopes above have been checked. This work **does not claim line-by-line replay of full published proofs**. In particular, no full Larsen–Yu/Ko theorem derivation has been transplanted, and no natural-proofs barrier is asserted for this specific DAG model.

## 3. Fully proved elementary model separations (CLASSICAL, not publication-novel)

**G2-A-L1: old-old immutability.** For APPEND_SINK(v,S), any path from an old u to an old t cannot use v: v has no outgoing edges. It therefore consists entirely of old vertices and old edges. Thus reach_new(u,t)=reach_old(u,t). By contrast, INSERT_OLD_EDGE(0,1) changes reach(0,1) on the edgeless graph of two old vertices from false to true. No *identity-preserving, one-append, old-old-query* transfer of this edge-insertion example exists. More complicated model-changing reductions are not ruled out; they must be written and priced.

**G2-A-L2: same final append, different old history.** Prefix A=((),()) and prefix B=((),(0,)) contain vertices 0 and 1; both get final command APPEND_SINK(2,{1}). In A, reach(0,2)=false; in B it is true. Their final command, public IDs and vertex count are identical. Therefore any updater that reads no old source records and only observes this command, with no retained prior-state information, cannot publish sufficient **target-only** information to distinguish the outputs. This is elementary indistinguishability, not a new n-bit lower bound.

**G2-A-F1: lazy query escape.** Store only the immutable, per-vertex parent record at append time (zero reads of any *old parent-record contents*). A query runs backward DFS with charged parent-record reads. This works for every append history and falsifies an unqualified claim that every append-only reachability updater MUST read an old record. The abstract immutable tuple records in the Python reference are NOT a physical page allocator: pointer copies, record placement, cache and allocation are not priced. For physical performance use G1-C2-C/D, not this oracle.

**G2-A-F2: published lower-bound transfer barrier.** Larsen–Yu's edge-insertion lower bound is not automatically a same-model APPEND_SINK bound, because G2-A-L1 fixes all old-old reachability. Ko TR25-156 includes a specified communication distribution/function and cannot be invoked with an arbitrary DAG membership predicate without proving a hard-function reduction. Rank and GF(2) path parity likewise cannot be silently substituted for Boolean reachability.

These statements are short classical proofs and countermodels. They do **not** establish any joint worst-case bound over (H,T,S,R_u,W_phys,W_net,P_q,RAM,Q) and do not imply UCT-005's PIN/GC/freshness results.

## 4. Independent executable falsification

[Finite oracle](../../research/dag002_g2_model_gate.py) and [unit tests](../../research/test_dag002_g2_model_gate.py) enumerate every topologically ordered DAG on 4 vertices (2^6=64), each of 16 possible next parent sets (1,024 appends), and all 25 pair queries after each append (25,600 Boolean queries). A separate backwards reference DFS checks the lazy decoder and preservation of every old-old result; cross-history and edge-insertion witnesses are explicit. Catalog/model tests reject implicit equation of operation types or novelty status. No probabilistic extrapolation, elapsed-time benchmark or disk durability is claimed.

    python research/dag002_g2_model_gate.py
    python -m unittest discover -s research -p 'test_dag002_g2_model_gate.py' -v

Dedicated GitHub-hosted exact-head workflow: .github/workflows/dag002-g2a-source-gate.yml. Full Research CI test discovery is an independent required acceptance check; green focused tests alone are insufficient.

## 5. Next allowed research steps

1. **G2-A acceptance:** focused AND full hosted Research CI exact head; independent diff review, preserving all 77 existing Research commands and catalog unchanged.
2. **G2-B separate PR:** faithfully implement SEA 2025 anchor algorithm from the primary full paper/pseudocode, with the same serialized page/request/parent-input/RAM ledger as G1-C2-C, plus paid lazy adjacency; distinguish reference code from published procedure. Compare on same workload, adversarial trace, cold-cache boundary; avoid device claims from virtual pages.
3. **G2-C novelty decision:** only ONE formal resource-preserving reduction or ONE fresh joint candidate with complete same-model proof, exhaustive finite falsifiers, and explicit counterexamples (antichain/chain/diamond/long histories). Otherwise STOP_THEOREM_NOVELTY, archive evidence as a source-backed constructive result.
4. **Source backlog:** issue #147 must be rebased against latest catalog. On 2026-10-11 main already contains Ko 2026 as LIT-119; do **not** allocate duplicate. Ko 2025 TR25-156 and Cohen et al. 1986 remain candidates for independent collision-safe import. Never assume LIT-205 is free.

**Cross-track relationship:** SOURCE_SCOPE LIT-187 directly precedes the G2-B comparator; LIT-127/LIT-114/LIT-298/LIT-119 and TR25-156 are model-transfer gates; LIT-159/LIT-200 relate only to authenticated observer models owned by UCT-005. A graph-of-research index should preserve these relationship *types* rather than inferring a proof from a topic overlap.
