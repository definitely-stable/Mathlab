# TKG-001 G0 — Bitemporal provenance in an evolving DAG: exactness and recourse controls

Date 2026-10-09 · [issue #190](https://github.com/definitely-stable/Mathlab/issues/190) · follows [IMPORT-006 #184](https://github.com/definitely-stable/Mathlab/issues/184), [DAG-002](DAG-002-G0-IMMUTABLE-REACHABILITY.md), [UCT-005 G3](UCT-005-G3-A-ROBUST-OBSERVABLE-STATE-THEOREM.md) and [UCT-005 G3-B2](UCT-005-G3-B2-A-FRESHNESS-INDISTINGUISHABILITY.md).

**Classification:** EXACT_RESTRICTED_SEMANTICS / ELEMENTARY_PROOFS / FINITE_INDEPENDENT_ORACLE / CLASSICAL_PROVENANCE_PRIOR_ART / MATERIALIZED_OUTPUT_RECOURSE_COUNTERMODEL / NO_NEW_GLOBAL_THEOREM / NO_CRYPTO / NO_PRODUCTION_RAG.

## 1. Genuine 2025–2026 prior art, at model level

| Original publication | What is established/studied | Not transferable without proof |
| --- | --- | --- |
| [Green–Karvounarakis–Tannen, PODS 2007](https://doi.org/10.1145/1265530.1265535), Provenance semirings | Polynomial provenance, sum of derivations, product of source dependencies | A factorized expression is not a cryptographic certificate, physical write locality bound or verified truth |
| [Van Assche et al., 2026](https://doi.org/10.1177/22104968251412270), Incremental Knowledge Graph Construction from Heterogeneous Data Sources | Practical incremental source evolution and historical/version-aware KG construction | No uniform guarantee of constant physical compaction or query time |
| [Zhao, FM 2026](https://doi.org/10.1007/978-3-032-26220-2_18), Correct-by-Construction Dynamic Reachability | Counting-augmented derivation hypergraphs for deletions and alternative proofs under Dyck-CFL reachability | Our plain finite DAG paths are strictly simpler than their CFL reachability problem |
| [Li et al., EDBT 2026](https://doi.org/10.48786/EDBT.2026.05), In-memory Incremental Maintenance of Provenance Sketches | Maintained provenance sketches and selective computational maintenance | A sketch is not automatically an exact complete proof listing; memory and false-positive conditions differ |
| [Han et al., 2025](https://arxiv.org/abs/2510.13590), RAG Meets Temporal Graphs | Temporal GraphRAG with a temporal KG and time hierarchy, incremental reports and ECT-QA | Evaluation of retrieved answers does not imply verified origin, freshness or worst-case resource lower bounds |

The earlier [LIT-235 Zep](catalog/LITERATURE.md#lit-235), [LIT-232 Hindsight](catalog/LITERATURE.md#lit-232), [LIT-231 MAGMA](catalog/LITERATURE.md#lit-231), [LIT-243 TAGGRAPH](catalog/LITERATURE.md#lit-243) and [LIT-244 ReCAP](catalog/LITERATURE.md#lit-244) are already imported; do not double-count. They concern different memory/query objectives.

## 2. Frozen restricted mathematical task, no hidden oracle

One honest **sequential** writer creates a finite list of operations \`add(id,u,v,[a,b))\` and \`retract(id)\`. Here \`id\` is a unique asserted edge/evidence identifier never reused, \`0<=u<v\` imposes a topological DAG (general cyclic knowledge graphs are OUT OF SCOPE), and integer \`a<b\` is the fact's **valid-time** window. Every operation commits one transaction **epoch** \`k=1,2,...\`; only a live ID can be retracted. A retraction at epoch \`k\` makes the edge absent for snapshots with transaction epoch \`s>=k\` but leaves the past unchanged.

A query \`Q(u,v;s,t)\` asks whether there exists a sequence of co-valid edges forming a directed path from \`u\` to \`v\`, where **every** path edge is present after replay of operations \`1..s\` AND satisfies \`a<=t<b\`. Reachability is reflexive. The separate axes are \`s\` = transaction/knowledge-as-of and \`t\` = target world-valid time. No global latest-time guarantee, privileged anti-rollback channel, authenticated source signatures, inferred trust, exclusive property constraints, entity resolution, LLM extraction or probabilistic confidence is assumed.

A positive witness is an ordered tuple of **edge IDs**, not a truth proof. It is accepted by a trusted local checker iff every named edge is visible at \`(s,t)\`, the identifiers form an uninterrupted directed path, and the endpoints match. **No negative witness/completeness proof is supplied** by this check. A malicious server could omit other sources, invent an old snapshot or withhold an updated epoch, as shown already by UCT-005 G3-B2.

## 3. G0 theorem P1: exact two-clock replay and positive witness correctness (elementary)

Let \`E(s,t)\` be the set of source assertions inserted on or before epoch \`s\`, not retracted on or before \`s\`, with \`a<=t<b\`. Define \`Paths(E(s,t),u,v)\` as ordered edge-ID paths. Then the reference event-replay algorithm computes exactly \`Paths\`, and its verifier accepts exactly those positive witness tuples (plus the reflexive empty path \`u=v\`).

**Proof.** Induction on event prefix: initially active edge set is empty. On insertion, exactly the new ID becomes active; on retraction, exactly its live ID disappears. The replay invariant therefore yields the asserted active set for each \`s\`. Filtering by \`a<=t<b\` independently imposes simultaneous world-valid time. Strict \`src<dst\` makes every nonempty walk finite and simple, so the reference DFS enumerates every path and only paths. For a given ordered witness, verification follows the same uniquely identified active assertions, checking continuity at every step; acceptance iff it is an actual path. QED. This is a finite **classical semantics argument**, not a new dynamic reachability theorem.

**Counterexample to accidental interval-wise existential retrieval:** edge 0→1 valid [0,2), edge 1→2 valid [2,4); each edge was true at some time, but **there is no common t** for a path 0→2. Transaction time cannot substitute for valid time.

**Deletion alternative-support witness:** two distinct assertions \`a,b:0→1\` and assertion \`c:1→2\`; after \`retract(a)\`, path \`(b,c)\` remains valid while \`(a,c)\` becomes invalid. A single boolean dependency on \`a\` produces the classical *ghost-path* error.

## 4. G0 theorem P2: exponential evidence expansion versus factorized path count

For every \`k>=1\`, construct \`k\` chained diamond gadgets. Gadget \`i\` connects vertex \`3i\` to \`3i+3\` via two internally disjoint 2-edge routes \`3i→3i+1→3i+3\` or \`3i→3i+2→3i+3\`. All 4k edge assertions are active on the same \`(s,t)\`.

There are **3k+1 vertices, 4k edges, exactly 2^k distinct positive witness paths**, each length 2k. At each gadget a witness chooses one of two disjoint routes; choices are independent across all k gadgets, giving 2^k. Any **explicit listing** of every distinct edge-ID witness requires at least 2^k output records, so an always-complete enumeration API cannot have polynomial *total output size* on this family. But the factored provenance expression \`Π_i[(Lia·Lib)+(Ria·Rib)]\` uses **O(k) arithmetic gates**, and dynamic-programmed **path counts** require only a DAG traversal of the active subgraph (the reference implementation charges the numeric ID span, so its own worst-case cost is O(id_span+|E|), not free O(V+E)). This is an old arithmetic-circuit / provenance-semiring distinction, **not** a new impossibility theorem for a factored proof system.

A complete factorized object, a single positive witness, boolean reachability and listing all witnesses are **four different service contracts**. No automatic transfer to negative answer certificates, exact belief revision, or trusted cross-epoch audit.

## 5. G0 proposition P3: materialized-answer recourse, plus a necessary countermodel

For any k, assertions \`bridge:0→1\` and \`leaf_i:1→i+2\` for \`i=0,...,k-1\` make the k boolean queries \`Q(0,i+2;s,t)\` all true. Retracting **one** bridge assertion makes all k false. Thus an implementation obliged to maintain those k individually stored, immediately up-to-date answer **bits** must change at least k bit values. This is an **output-specific materialization lower bound**, not universal write cost.

**Disproving the overbroad claim:** an append-only event log and a live-ID dictionary can process that retraction with **one appended event and one logical index mutation** (constant *number* of abstract edits). Queries replay or consult current state and pay potentially much more. Sharing the bridge flag/factorization also avoids k separate answer writes. No lower bound on arbitrary algorithms, bytes, page images, SSD NAND, trusted roots or query time follows.

**Reference resource ledger** per operation: one event log append, one live-ID index mutation, and on first insertion a never-reused ID claim. These count logical records/operations only. Historical as-of queries scan O(s) event records, and explicit witness output can be exponential. Python dictionary worst-case time is not modeled; real storage compaction/write amplification/transaction crash recovery are explicitly OUT OF SCOPE. Every graph **fact** is merely an assertion; a correct edge lookup does not prove that a human/LLM-derived fact is true.

## 6. Independent evidence and acceptance gate

- [Reference](../../research/tkg001_bitemporal.py) has event-time and transaction-time slices, positive witness checker, explicit DFS enumeration, factorized exact path count, and a logical event/index ledger.
- [Independent tests](../../research/test_tkg001_bitemporal.py) use vertex-sequence permutations and cartesian edge-key products rather than the reference DFS/DP; exhaust all 64 topological edge masks on 4 vertices across 3 as-of epochs, four valid-time points and all 16 ordered endpoint queries.
- Explicit fixtures: bitemporal retraction preserving historical answers; non-overlapping valid-time facts; independent alternative sources; k=1..8 diamonds; one-edge k=24 answer flips against a constant logical mutation-count countermodel; invalid/corrupt source ID and interval/cycle/reuse rejection.
- **Required evidence:** exact PR-head GitHub-hosted Research workflow SUCCESS and repository post-merge checks, documented actual results. Do not claim success from merely committed tests.

**Scientific decision G0:** \`EXACT_RESTRICTED_SEMANTICS\` + \`PROVED_ELEMENTARY_RECOURSE_AND_EXPANSION\` + \`PRIOR_ART_BARRIER\`, not \`NEW_THEOREM\`.

## 7. G1 — real open frontier, only after model cost is frozen

Study a **same-task** joint time/provenance/update/read bound: (i) bitemporal as-of queries with mutable source IDs and retractions; (ii) either complete factored proof or explicit positive witnesses **and** signed/anchored negative completeness if required; (iii) exact number of page images read/written, persistent metadata, compaction and version history retention; (iv) honest latest anchor separately priced from historical as-of; (v) adversarial update sequences and temporal cuts. Compare source semirings, dynamic reachability, temporal GraphRAG, and indexed bitemporal DB against simple event replay. Require a strict source/model novel joint inequality or a certified counterexample. STOP if only restating an output-size bound, known provenance circuit factorization or UCT-005 F0 freshness indistinguishability. No production API or Rust authorized by this G0.
