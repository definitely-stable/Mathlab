# UCT-005 G2-B — frozen dynamic authenticated 2D parity model, accounting and falsifiers

**Date:** 2026-10-09. **Root:** [#105](https://github.com/definitely-stable/Mathlab/issues/105); **G2-B:** [#131](https://github.com/definitely-stable/Mathlab/issues/131). **Status:** `MODEL_FROZEN / CONSTRUCTIVE_BASELINE / EXACT_FINITE_FALSIFIERS / NEW_THEOREM_OPEN_UNPROVED`. A proposed inequality is *not* a theorem just because a finite test does not refute it.

## 1. Primary-source additions and immediate novelty STOP gates

The audited source identities below were **absent at G2-B baseline 204-entry main** (additional canonical catalog rows LIT-205+ assigned without overwriting concurrent work):

1. **Wang–Lin–Yu 2016, IET Information Security**, [DOI 10.1049/iet-ifs.2014.0408](https://doi.org/10.1049/iet-ifs.2014.0408) — *Authenticating multi-dimensional query results in outsourced database*. Fully outsourced dynamic k-dimensional authenticated skip-list structure for multi-dimensional query authenticity/completeness. The source proves a conditional RSA-signature/hash statement under its specific range/search setting. A `RECT XOR` aggregate or full adaptive update consistency is **not automatically** that theorem. **STOP**: "first multidimensional authenticated dynamic range queries".
2. **Pennino–Pizzonia–Papi 2019, IEEE Access**, [DOI 10.1109/ACCESS.2019.2957346](https://doi.org/10.1109/ACCESS.2019.2957346), [same research arXiv 1910.11754](https://arxiv.org/abs/1910.11754) — *Overlay Indexes: Efficiently Supporting Aggregate Range Queries and Authenticated Data Structures in Off-the-Shelf Databases*. DB-tree for aggregate range queries **and ADS** using logarithmic data transfers and a small number of database round-trips under its assumptions. **STOP**: "first combining authenticated data with aggregate range queries"; this source is not a lower bound.
3. **Sun–Xu–Ni–Chen–Cheng–Zhang 2025, PVLDB**, [DOI 10.14778/3748191.3748219](https://doi.org/10.14778/3748191.3748219) — *Authenticated Aggregate Queries with Boolean Range Predicates on Blockchains*. Merkle Bloom Filter Tree (MBFT) improves aggregate query authentication for blockchain keyword/range predicates with false-positive/selectivity accounting; **not an unconditional theorem** about XOR bit-probe complexity. **STOP**: "first verification of aggregate range queries".
4. **Shangguan–Yaish–Malkhi, August 2026 author preprint**, [arXiv:2608.25206](https://arxiv.org/abs/2608.25206) — *Authenticated Data Structures for Dynamic Workloads*. Dynamic Huffman-Merkle Tree (HMT) for skewed point access and hashed proof/reshaping costs. Author preprint, **not a published peer-reviewed 2026 theorem**, and its membership point lookup is **not** an authenticated 2D XOR aggregate. It defeats any blanket claim that changing access frequencies in ADS is unstudied.
5. **Shekelyan–Dignös–Gamper, Information Systems 2019**, [DOI 10.1016/j.is.2018.06.009](https://doi.org/10.1016/j.is.2018.06.009) — *Sparse prefix sums: Constant-time range sum queries over sparse multidimensional data cubes*. Corrects a dimension-dependent update-cost claim for relative prefix sums and provides sparse-data aggregate upper construction. It is not authenticated, but invalidates unqualified 2D dynamic rectangle query/update headlines.

Earlier hard barriers still apply with original `LIT` identities: [BKV memory checking / Tas–Boneh](UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md), [FSS↔dynamic range DS, accumulators, natural proofs](UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md). `LIT-072` STOC 2026 is already indexed and not a newly discovered original theorem. **No imported paper's full proof was independently reproduced.**

## 2. Freeze a single natural task family and adversarial experiment

Let `N=2^k`, `n=N²`, `a in GF(2)^(N×N)`. Initially all `a[i,j]=0`. Public operations:

- `FLIP(i,j)` from the **trusted owner/verifier**, authenticated as an instruction: exactly one bit toggled. No server-selected unapproved update.
- `RECT(r0,c0,r1,c1)` returns `xor_{r0≤i<r1, c0≤j<c1} a[i,j]` with nonempty half-open interval boundaries; full and singleton rectangles both allowed. Query schedule and coordinates may be chosen adaptively by a computationally bounded adversary based on all past accepted replies.
- Fixed finite horizon `H(N,lambda)`, with explicit version `v` advanced at each accepted FLIP. Owner stores the last accepted **digest and version** in trusted durable memory. Omitting durable client state makes rollback defense impossible in this protocol. Client must not lose or fork that state.
- The server is Byzantine and may corrupt all untrusted stored cells and messages, return old proofs, omit elements or abort. **Abort/DoS is outside soundness**: completeness holds for the honest server; security requires that an accepted result equals the canonical post-update grid.
- Security assumption: a *collision-resistant*, domain-separated hash `Hash_lambda` and correct, exclusive authorized owner updates. Against polynomial-time adversaries, a divergent accepted proof would yield a hash binding violation in this *fixed-structure* scheme; **this conditional argument is not a new cryptographic theorem and is not independently formalized**. It is NOT an information-theoretic guarantee. `SHA-256` used in tests is an engineering digest, not proof of collision resistance.
- No public-key signatures or multiple clients; owner and verifier are the same endpoint. A third-party reader with an untrusted old root cannot inherit freshness from this model. Client keeps exactly one trusted root plus `v`; always charge user-provided update indices, all messages, hash CPU, and initial full-tree commitment. No free state-dependent helper tables.

**Resource units and cost tuple** (separate `bit`, `byte`, `hash invocation`, remote `cell probe`; do not mix with GF(2) bit writes):
`R=(S_trusted_bits, S_remote_bits, U_reads, U_writes, U_changed, Q_reads, Q_writes, B_update_bits, B_query_bits, C_total_bits, G_hash, V_hash, T_program_bits, T_setup, H, lambda, epsilon)`.
Costs are per accepted logical operation, tagged worst-case; `C_total` includes both update request, proof and response/receipt. `G_hash, V_hash` count calls, not runtime or hash work in cycles. We do not charge the *initiator's construction of coordinates* as arbitrary free server power; it is O(log N) input bits. Fixed-code vs growing lookup tables explicitly charged to `T_program_bits`. Data owner genesis commitment of `n` zero leaves costs `Theta(n)` hash operations, remote state initialization and initial trusted digest; not hidden in the per-operation costs. Cryptographic parameter lambda in the physical digest and transport, not merely an asymptotic name. **Client trusted program/setup, crash durability and serializability require their own implementation; out of scope of finite oracle.**

## 3. Four competing honest upper constructions (plus one authenticated upper)

| Candidate for same public FLIP/RECT task | State | Update workload | Query workload | Malicious answer soundness |
|---|---|---|---|---|
| Raw grid | n bits | one bit read+write | `area(rect)` bit reads | NO |
| 2D materialized prefix | n bits | `(N-i)*(N-j)` prefix-bit changes | ≤4 prefix reads | NO |
| 2D Fenwick | n bits | ≤`(k+1)^2` bit reads+writes | ≤`4(k+1)^2` prefix-bit reads | NO |
| Spatial quadtree XOR aggregate | `(4n-1)/3` tree nodes; n leaf data bits + internal aggregate bits | one leaf+one parent per level | cover decomposition; at most O(n) visited nodes | NO |
| **Authenticated XOR quadtree** (this G2-B finite model) | `(4n-1)/3` λ-bit digests + `(n-1)/3` internal aggregates + n leaves | update proof: old leaf + `3k` sibling digests + k ancestor aggregates; owner recomputes k+1 hashes; server O(k) changed nodes | partial-node expansion + full-covered subtree aggregates and outside sibling digests; root rehashed; worst-case O(n) proof/hash; **full-grid query 4 digests + 1 aggregate**, point query O(k) proof/hash | Conditional binding + trusted root/version; finite mutation tests only |

For `N=1`, handle root leaf without internal nodes. An internal node `X` with rectangle `b_X` has `aggregate_X = xor` of all leaves below and
`digest_X=Hash_lambda(DomainInternal, b_X, aggregate_X, digest_child_0, ... digest_child_3)`. A leaf contains `Hash_lambda(DomainLeaf,b_X,a[i,j])`. Coordinate bounds and node type are always hashed.

**Proof grammar**:
- `OUTSIDE(hash)` permitted only when the entire node is disjoint from the query rectangle.
- `FULL(aggregate,child-digests[4])` for an interior node completely covered by the query; `FULL(bit)` for leaf.
- `PARTIAL(aggregate,child-proofs[4])` only for a strictly partially intersected interior node.
The verifier **rebuilds every visited node hash**, including the root, and accumulates XOR of canonical FULL aggregates. OUTSIDE supplies digest alone. The invariant that stored aggregate equals XOR of descendants is established by trusted genesis and preserved by every *client-verified* single-bit update, **not** by checking all children for every query.

**Update proof**: old leaf bit, path of parent aggregate, child index (from geometry), 3 canonical ordered sibling hashes per parent; verify old root; compute the new root by toggling the old leaf and each ancestor aggregate. Owner increments `v` only after authenticated acceptance. The committed digest has no arbitrary collision-free "ideal hash" oracle hidden in the model. Physical remote read vs changes and wire bytes of canonical encoding must be independently measured for a production candidate. The Python suite uses structural counts and SHA-256; it does NOT implement a production serializer, persistence, access control or crash recovery.

This is an **upper construction**, not a new theorem. Published ADS/range-aggregate research is at least as important as this simple baseline when evaluating novelty.

## 4. An exact simple reduction brick (NOT original)

**Lemma (restricted embedding):** For any correct `T_N` service with FLIP and RECT, embed an n=N²-bit point-memory interface:
`READ(t) := RECT(i,j,i+1,j+1)`; `WRITE(t,b) := READ(t); if old!=b then FLIP(i,j)`, where `t=iN+j`. Correctness is immediate by induction. The memory-checker simulation costs *at most* the cost of one point query plus one flip and carries over **only if** the original service's authenticity, client trust, adaptive security and RAM operation semantics match the published checker formalism. It is invalid to identify `U_changed` with remote `q_w` or crypto proof bytes with `q_r` unless those costs are converted. The simulated READ and WRITE include possible rejection; this is not a guarantee of liveness.

**Test/falsifier:** finite exact bit-model tests enumerate all `N=2` states and every single flip and rectangle against independently computed XOR. They verify owner-root update, old-proof rejection after genuine state changes, wrong epoch, corrupted FULL aggregates, missing PARTIAL branches and malformed/incorrect sibling proofs. The mathematical soundness claim remains conditional and **cannot be proved by these tests**.

## 5. A concrete quantitative claim, challenged before any proof

**CANDIDATE G2B-H0 (explicitly scoped, status: PRIOR_ART_OVERLAP / NOT NOVEL):** Assume at most `O(lambda+log H)` trusted client bits, polynomial `H`, a polynomial-time malicious server, and fixed binary physical cells. Hypothesize for a *worst-case point-query or point-update pair* with soundness `epsilon ≤ 1/3` that
`max{ U_reads+U_writes, Q_reads + ceil(B_query_bits/lambda) } = Omega(log(N²)/log log(N²))`.
This is a **testable inequality** (not a theorem; constant-hash proofs may violate naive bit-probe accounting if the protocol assumptions are relaxed). Even if true, its order overlaps existing BKV memory-checker results and classical partial-sums work after the necessary reductions; therefore it is **STOP_AS_ROOT** pending strictly stronger joint claim. It cannot be multiplied by Tas–Boneh's per-proof refresh or accumulator witness-change rates without model-preserving transfer.

**G2B-H1 (rejected)**: "every authenticated rectangle proof has size `Omega(lambda*N)` bits" is **false**: a FULL-grid query in authenticated aggregate quadtree sends only `4lambda+O(1)` bits (for N≥2), with the owner recomputing one parent digest. Any universal `B_query≥lambda*N` claim without a geometrically restricted query family is refuted. Another false universal claim is `U_changed*Q_probes≥N²`: the honest 2D Fenwick data structure has each term `polylog N`, even though it is not authenticated.

**Decision:** A+B+D progress can be audited; **NO nonfactorizing asymptotic improvement over B_known is yet isolated**. G2-B strong-theorem acceptance remains OPEN. The next potentially distinctive axis is *simultaneous proof maintenance for a charged family of persistent subscriptions / derived DAG outputs*, but prior incremental-verification research needs a new primary-source gate first. The UCT-005 root remains OPEN_UNPROVED; do not label the present basic authenticated quadtree invention.

## 6. Hard provenance/acceptance boundary

- New sources: catalog identities + generated bibliographic indices with no duplicate proceedings/preprints; source status distinguishes publisher text, abstract and author preprint.
- Fixed `N=2` exhaustive / sampled `N=4` independent numerical and adversarial countermodels in `research/test_uct005_g2b_auth_tree.py`.
- Offline deterministic `research/literature.py --check`, full hosted tests, exact PR HEAD CI and post-merge main.
- No Rust, library API or production crypto/benchmark; no source-paper full proof reproduction; no root theorem or research claim beyond the explicit restricted lemmas.
