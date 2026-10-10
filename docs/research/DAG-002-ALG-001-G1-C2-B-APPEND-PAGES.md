# DAG-002 × ALG-001 G1-C2-B — real append-only reachability versus dynamic edge update

**Owner:** [issue #161](https://github.com/definitely-stable/Mathlab/issues/161). **Depends on:** [G1-C2-A PR #267](https://github.com/definitely-stable/Mathlab/pull/267), preceded by [G1-C1 PR #264](https://github.com/definitely-stable/Mathlab/pull/264). **Decision:** RESTRICTED_CONSTRUCTIVE_BASELINE / MODEL_NONTRANSFER_PROVED / SCIENTIFIC_NOVELTY_UNPROVED / NO_UCT_ROOT_TRANSFER.

## 1. Freeze two different update semantics before comparing theorems

**APPEND_SINK(S):** vertex v is fresh, every parent p in S has p<v and the directed arc p->v is inserted; existing vertices and their arcs are immutable. Reach(u,v) means a directed path including the length-zero path u=v. All queries are Boolean. Every new parent subset S is supplied *to the updater* in a canonical v-bit incidence payload, counted in source_input_bits. It is not free input to a future query. No changes to old-old reachability.

**INSERT_OLD_EDGE(u,v):** an edge between two previously published vertices is allowed. Reach(u,v) of an old-old pair may change. This is a distinct dynamic-graph update alphabet; even when the graph remains acyclic, it cannot be simulated as a semantic-equivalent APPEND_SINK that preserves the same fixed old-old reachability query.

**G1-C2-A DELTA(d):** a physical codeword is mutated with prescribed GF(2) XOR of n *fixed* observable coordinates under the same decoder. In APPEND_SINK the output coordinate family and node universe grow with each append, so the G1-C2-A invariant/syndrome theorems do not automatically transfer to repeated appends. Re-encoding historical queries as queries against **new target IDs** is a change of operation/observable that must be charged and proved, not silently renamed.

**G1-C2-B-L1 (elementary non-transfer).** For every APPEND_SINK operation, every pair u,t that existed before the append has unchanged Boolean reach(u,t). **Proof:** any path whose vertices are all old uses pre-existing arcs, and no path between old vertices can visit the new sink, since it has no outgoing arcs. In contrast, INSERT_OLD_EDGE(0,1) changes reach(0,1) from false to true in a two-vertex edgeless DAG. No identity-preserving old-old-query, single-append, update-model reduction exists for this pair. This says NOTHING about arbitrary simulation reductions with larger data structures or remapped queries. Classical property; no novelty.

## 2. Exact immutable transitive-closure page baseline

At vertex v append, the updater writes a fresh immutable ancestor bitmap C_v of v bits, with
C_v = union_{p in parents(v)} (C_p union {p}).
Older C_p are never modified. Each label is stored in ceil(v/(8P)) full P-byte pages with public virtual addresses (v,page). Each parent p requires reading **all** ceil(p/(8P)) previously stored pages of C_p. Each new label page is written once, including zero-filled pages. Query reach(u,t) for u<t reads exactly one P-byte page of C_t and one bit; reach(t,t) and u>t use only the public topological IDs and cost zero page reads. Initial remote storage is empty. Unit costs:

- APPEND(v,S): update_read_pages = sum_{p in S} ceil(p/(8P)); update_write_pages = ceil(v/(8P)); input_parent_bits = v; new_label_one_bits = popcount(C_v).
- Every physical page read/write transfers P application bytes, including entire final pages, even when only one bit is useful. The n-bit parent-command encoding is a **separate** source transmission charge.
- No caches/reuse, allocator, page-address serialization, remote-key namespace costs, RAM cap, GC, crash recovery, durable writes, encryption, authentication or wall-clock SSD/NAND claims. The virtual key-address map is public/free, preventing universal bit-storage claims. Honest storage only; intentional corruption goes undetected.
- Values labelled "physical page" mean **logical full-page application transfers** in this frozen reference, not verified device-level operations.

**G1-C2-B-L2 (constructive correctness).** Under this model, the query returns true iff a directed path u->t exists. **Proof:** induction on appended vertex t; each ancestor path to t either ends directly at a parent p or reaches p and traverses p->t. The union recurrence enumerates exactly these possibilities. Previously published labels and old-old query answers remain unchanged. Classical transitive-closure DP, not new.

**G1-C2-B-L3 (scoped information baseline).** From an n-vertex antichain, the last APPEND has 2^n legal parent subsets, each inducing a different truth vector of n old-to-new reachability queries. Thus for the one-shot fixed-prefix *no-other-input-dependent-read-source* model, the post-append representation must distinguish >=2^n cases. This does NOT imply >=n newly written bits on an arbitrary external storage model (addresses, trusted state, source-access probes, setup and caches must be charged). Elementary injection, already represented by G0 #138; do not promote to theorem novelty.

## 3. Mandatory falsifiers

- Graph ((),(0,),(1,)) has reach(0,2)=TRUE but direct-parent(0,2)=FALSE. Direct adjacency bits cannot replace transitive closure in general.
- Diamond ((),(0,),(0,),(1,2)): two source-to-sink paths give GF(2) path parity=0 but Boolean reachability TRUE. A linear parity/syndrome or rank computation over GF(2) alone is not a universal Boolean reachability oracle.
- Edgeless old pair 0,1 followed by APPEND_SINK never changes reach(0,1), but inserting old edge 0->1 does. This is a concrete dynamic-edge/append model transfer rejection, not a proof that more expressive encodings are impossible.
- Malicious modification of a stored page can flip reachability answers without detection; it is explicitly **not** an authenticated UCT-005 theorem.

## 4. Source-level comparison, not a black-box transfer

- [Bulteau, David, Horn, Tran-Girard, *Incremental Reachability Index*, SEA 2025 DOI 10.4230/LIPIcs.SEA.2025.9](https://doi.org/10.4230/LIPIcs.SEA.2025.9) directly covers append-only DAG and immutable vertex index state. Our dense bitmap is only a simple source-distinct reference/comparator, not a new compressed index.
- [Larsen–Yu, *Super-Logarithmic Lower Bounds for Dynamic Graph Problems*, FOCS 2023 DOI 10.1109/FOCS57990.2023.00096](https://doi.org/10.1109/FOCS57990.2023.00096) proves bounds under DAG edge insertions, not APPEND_SINK with frozen old-old queries. Do not transfer its bound without an explicit resource-preserving reduction. The 2025 SIAM Journal version DOI 10.1137/24M1638215 is not an independent new result.
- [van den Brand–Kumar–Zhang, *Dynamic Rank, Basis, and Matching*, ICALP 2026 DOI 10.4230/LIPIcs.ICALP.2026.45](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) studies dynamic rank with entry-/column-update semantics and output contracts unlike Boolean reachability; GF(2) parity path cancellations and rank alone are not sufficient to infer equivalence.
- [Mathlab G0 DAG oracle](../../research/dag002_oracle.py) and [G1-C2-A](../../research/dag002_g1c2_synthesis.py) are retained, no code or proof changes. Full original-paper theorem-level audit is still required for any nontrivial lower-bound novelty claim.

## 5. Reproduction and acceptance

Run:
~~~bash
python research/dag002_g1c2b_append_pages.py
python -m unittest discover -s research -p 'test_dag002_g1c2b_append_pages.py' -v
~~~

All 1, 2, 3, 4 and 5-vertex topological DAGs (1024 at 5 vertices), for page sizes P=1 and P=2, are independently checked against DFS at each append; all exact transfer counters are checked from separate formulas. Additional controls span 35 vertices across page boundaries with P=1/2/4, all parent subsets for antichains n<=7, old-old snapshots, GF(2) cancellation, direct-parent bug, and silent corruption. Strictly finite controls, not proof of any asymptotic bound.

Accepted as **G1-C2-B restricted model/reference** only after exact-head focused and full hosted Research CI succeed and independent review verifies costs. Preserve #161 OPEN for next scientific novelty gate. No cross-repo changes.

**Next:** G1-C2-C should price allocator/metadata and compare immutable closure pages vs existing chain-top index and source-level compressed DAG baselines on identical logical/physical contracts, or STOP on theorem novelty. No Rust.
