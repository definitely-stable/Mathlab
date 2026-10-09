# DAG-002 G0 — immutable append-only DAG observability, exact finite foundation

**Status (2026-10-09):** MODEL_FROZEN / ELEMENTARY_COUNTING_PROOF / KNOWN_CHAIN_PRIOR_ART / ORACLE_PENDING_UNTIL_CI / NO_NEW_NONFACTORIZING_THEOREM / NO_RUST. [Issue #133](https://github.com/definitely-stable/Mathlab/issues/133), paired with [ALG-001 #134](https://github.com/definitely-stable/Mathlab/issues/134). This is an independent model audit, **not a claim to reprove all SEA 2025 results**.

## 1. Mandatory primary prior art and novelty separation

- [LIT-187 — Bulteau–David–Horn–Tran-Girard, *Incremental Reachability Index*, SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9): an existing append-only DAG reachability index preserving old labels, based on Jagadish's chain-top labels and Felsner's online chain decomposition, plus anchors. Source [official open HTML](https://drops.dagstuhl.de/storage/00lipics/lipics-vol338-sea2025/html/LIPIcs.SEA.2025.9/LIPIcs.SEA.2025.9.html) §§1–3: constant query time with online chains, at most O(W) labels per vertex where online chain count W can be O(width²), or compressed O(log n) query variant. **Every chain-top argument below is known prior art**, implemented as a transparent *simplified* baseline, not a competing 2025 result.
- [LIT-195 — van den Brand–Kumar–Zhang, *Dynamic Rank, Basis, and Matching*, ICALP 2026](https://doi.org/10.4230/LIPIcs.ICALP.2026.45) is for arithmetic operation costs under matrix updates, not endpoint-only reachability labels. See [ALG-001 G0](ALG-001-G0-RANK-OBSERVATION.md).
- [LIT-119](../research/catalog/LITERATURE.md#lit-119) etc. UCT data-structure lower bounds and [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) already cover stronger priced-memory/verification models; nothing here transfers to those settings without a resource-preserving reduction.

## 2. Freeze the distinct model, including forbidden free resources

Graph sequence `G_0,G_1,...` over IDs `0,...,t−1`. Update `append(v,P_v)` adds **only a new sink** `v=t` and directed arcs `p→v` with `P_v⊆[0,t)`; there are no backward arcs, deletes or updates to old edges. Reachability includes reflexivity. A query `Reach(u,v)` must answer exactly whether there is a directed path `u→*v`.

**Two-label no-remote-probe observer:** every old vertex `u` has an immutable string `L_u` that depends only on the prefix in which it was published. The new vertex has a `b`-bit label `L_v`, and an input-dependent `g`-bit globally readable manifest `M_v` may change on append. The deterministic decoder may read `u,v,n,L_u,L_v,M_v` plus arbitrary fixed/public code and parameters, but may **not** read the new incoming parent list, source graph, an external keyed dictionary, a mutable per-vertex index, or free hidden state. All input-dependent mutable bits accessible to the query must be charged as `g`. Old labels remain unchanged even while decoding. Randomized/errorful protocols are **outside** this G0 lemma.

**Exact resource vector** for future comparisons: new label `B_v` bits, shared manifest `G_v` bits, remote query probes `P_q`, remote memory bytes `S`, update logical operations `U`, physical bytes written `W`, CPU `C`, and optional trust/proof bits `V`. G0 counting fixes `P_q=0`; the chain baseline reports only integer logical slots, **not physical bytes, CPU benchmarking or certified I/O**.

## 3. G0 theorem: sharp fixed-width restricted observer counting

**Theorem DAG-002-G0-L1 (elementary, not new).** Fix a prefix with `n` pairwise-incomparable, edgeless prior vertices `u_0,...,u_{n−1}` and all their published immutable labels. A new vertex `v` may have any parent subset `S⊆{u_0,...,u_{n−1}}`. Suppose the exact observer above uses `b` bits for `L_v` and `g` bits of input-dependent global manifest after the append. Then

`b + g >= n.`

**Proof.** In the fixed antichain prefix, `Reach(u_i,v)=1` exactly when `u_i ∈ S`. Thus the vector of all `n` query outputs is precisely the characteristic vector of `S`, and the family has `2^n` different required output vectors. Every old label is fixed independently of the choice of `S` and the decoder is fixed, so output vectors can differ only when the `(L_v,M_v)` pair differs. It has at most `2^(b+g)` values. By injectivity `2^n<=2^(b+g)`; hence `b+g>=n`. **Tight for this same model:** take the `n`-bit new label as the parent incidence bit-vector, `g=0`; compare `L_v[i]`. QED.

**Kill conditions / scope:** the lemma **does not** imply `n` bits of extra metadata when query may probe the original `n`-bit parent array: a one-bit remote read per query and no new label suffices if address `i` is public. Nor does it imply `n` bits for chain-width-bounded DAGs, fixed indegree, restricted allowed subsets, externally cached source graphs, randomized approximation or unbounded query computation. If new vertex `v` has only `K` allowed different observable ancestor sets after a fixed prefix, the same argument only gives `b+g>=ceil(log₂K)`. Do not multiply per-query probe costs by `n` and call it a novel joint cell-probe lower bound: a global remote dictionary can be shared across all queries.

**Indegree-constrained subfamily:** if `|S|=d` exactly, same counting gives `b+g>=ceil(log₂ binom(n,d))` for that fixed-prefix family, not necessarily `n`; proof by identical injection. This is a classical fixed-subset entropy bound, not ASET or a novel theorem.

## 4. G0 correctness baseline — immutable chain-top index

Define `A_v={v}∪⋃_{p∈P_v}A_p`. A chain partition into `C_0,...,C_{c−1}` is maintained online, never reassigning previously published vertices. Every chain has vertices in insertion order that are pairwise comparable. A new `v` may join a chain `C_j` only when its current head belongs to `A_v`, else create a singleton chain.

For each vertex `v` and chain `j`, define `T_v[j]=max(A_v∩C_j)` or absent. Publish only nonempty `(j,T_v[j])` entries as immutable new label. Inductively, union of parent ancestor prefixes and the new vertex yields the exact top for each chain, without editing any older label. Query `u→*v` iff `T_v[chain(u)]` exists and `u<=T_v[chain(u)]`: earlier chain elements reach later chain elements and reachability is transitive. This is exactly the Jagadish/Felsner-style chain-top observation reviewed by SEA 2025, with a **simple first-compatible-chain heuristic** rather than their worst-case-optimal Felsner decomposition.

Upper accounting: each new label has at most `c_v` top entries plus its immutable chain ID; total logical top entries `Σ_v |T_v|v <= Σ_v c_v <= n(n+1)/2` over n vertices. Metadata manifest stores `c_n` chain-head IDs. Algorithm scans `deg(v)` parent labels and at most `c_v` heads: `O(Σ_{p∈P_v}|T_p| + c_v)` elementary processing, **not** amortized physical page writes. The code uses immutable sorted-pair tuples and a binary search for the chain ID: `O(log c_v)` lookup (ignoring Python overhead), rather than claiming O(1) deterministic dictionary access. No optimal width relationship is claimed for first-fit: SEA 2025 obtains `O(width²)` using a different chain-selection algorithm.

## 5. Oracles, reductions and acceptance

- **Oracle A (separate graph search):** enumerate every topological DAG of sizes n≤5 (2^(n(n−1)/2) graph states); compare all ordered reachability queries at all prefixes against independent backward graph DFS, and test old labels and chain IDs remain literally unchanged.
- **Oracle B:** test exact `2^n` observer outputs for all parent subsets at n≤8 and fixed `binom(n,d)` subclasses; independently verify label bound using collision counting. A deliberately out-of-model one-cell remote-memory control returns all answers with zero label bits, rejecting the false global `b+g>=n` claim.
- **Oracle C:** deterministic six-node adversarial fixture families (empty/full, path, alternating layered) and corrupt parent/out-of-order updates rejected. The ledger counts logical stored top entries/manifest head entries, not bytes or cycle timings.
- **Cross-check ALG-001:** same `n` observed bits form a GF(2) `1×n` matrix of rank ≤1; for nonzero choices rank is exactly 1, nevertheless position query capacity remains exponential.

**Scientific gate:** `PROVED_RESTRICTED_ELEMENTARY_INJECTION` / `REPRODUCED_KNOWN_CHAIN_TOP` / `NO_GENERAL_DAG_LOWER_BOUND` / `NO_NEW_THEOREM_NOVELTY` / `NO_RUST`. G1 may seek a *same-model, nonfactorizing* inequality only after pricing source probes, update bytes, mutable dictionaries, manifest bits, randomization and auth soundness, comparing against SEA 2025 and UCT-005. No such G1 theorem is proven here.
