# UCT-005 G2-B1 — semantic vs structural influence in mutable XOR DAGs

**Date:** 2026-10-09. [Root #105](https://github.com/definitely-stable/Mathlab/issues/105) · [G2-B #131](https://github.com/definitely-stable/Mathlab/issues/131) · [G2-B1 #148](https://github.com/definitely-stable/Mathlab/issues/148). **Status: RESTRICTED_ALGEBRAIC_LEMMA / FINITE_ORACLE / CRYPTOGRAPHIC_MODEL_COMPARISON / NOVEL_NONFACTORIZING_THEOREM_UNPROVED.** No Rust/production, no asymmetric cryptography/security proof.

## 1. An explicit prior-art barrier — not a new unified theory by renaming it

- **LIT-068, Eden Aldema Tshuva–Rotem Oshman**, [Model-Generic Incrementally Verifiable Computation from Updatable BARGs, ITCS 2026](https://doi.org/10.4230/LIPIcs.ITCS.2026.6). Published generic lifting of suitable delegation schemes to IVC for streaming, RAM, PRAM, distributed graph and MPC models; an UpBARG primitive. It **already constructs a cross-model online-certificate umbrella**; novelty of merely joining graph computations + incremental proofs is **STOP**. Its security is computational, subject to delegation and UpBARG hypotheses; it does not automatically charge every physical RAM write, each dependent subscription receipt or forkable client state.
- **LIT-187, Bulteau et al.**, [Incremental Reachability Index, SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9). Existing append-only reachability index and immutable labels, not an unstudied DAG update/query task. [DAG-002 G0](DAG-002-G0-IMMUTABLE-REACHABILITY.md) has only a **restricted classical no-remote-probe counting lemma**; G2-B1 is not a new proof of that theorem.
- **G2B1-SRC-01, Larsen–Yu**, [Super-Logarithmic Lower Bounds for Dynamic Graph Problems, SIAM J. Comput. DOI 10.1137/24M1638215](https://doi.org/10.1137/24M1638215). Published online 2025-02-13, volume 55(3) issue 2026, FOCS 2023 proceedings are **one research work**, not 3 independent results. Establishes unconditional `~Omega(log^(3/2) n)` cell-probe lower bound for dynamic **directed DAG reachability under edge insertions**, max of update/query. Not for **source-bit flips in an immutable XOR circuit**, and NOT an authenticated proof-size lower bound. Any DAG root theorem must beat same-model cell-probe literature rather than casually replacing graph reachability with parity.
- **G2B1-SRC-02, Afshar–Goyal**, [Verifiable Streaming Computation and Step-by-Step Zero-Knowledge, IACR 2025/251](https://eprint.iacr.org/2025/251). Original publisher record explicitly says **Preprint**; IVsC produces incremental proofs for streaming-input RAM computations and step-by-step simulation of prover private state under cryptographic assumptions. This is a second prior-art STOP for "first general ongoing verifier" or unqualified incremental proof novelty. It is not a public multi-reader fork/freshness theorem.

Canonical bibliography is **currently blocked by [#142](https://github.com/definitely-stable/Mathlab/issues/142) and open HYP-105 PR #132 reserving LIT-205**. Both new original works are imported into `UCT-005-G2-B1-SOURCES.json` with canonical source IDs and publication versions/verification tiers. Duplicate LIT-068/LIT-187 are referenced, not reimported. Source audits here inspect publisher abstracts/metadata and a clearly scoped result, **not full independent proofs**.

## 2. A concrete same-task DAG model

Fix a finite labelled directed acyclic graph `G=(V,E)` in topological order. Let `S` be its set of indegree-zero source vertices. Input `x in GF(2)^S`. The value at a source is `y_s(x)=x_s`; for each other vertex `v`, its value is
`y_v(x)= XOR_{u in Pred(v)} y_u(x)`. All predecessor IDs, topology, evaluation program and canonical edge ordering are static. An online **FLIP(s)** toggles exactly one source input bit; **READ(v)** returns the current Boolean node output. The adversary may choose operations adaptively. This is **not** the append-sink/edge-insert reachability model in LIT-187 or the changing-edge reachability model of Larsen–Yu.

Let `p_{v,s}` be the number of directed paths from `s` to `v`, with `p_{s,s}=1`, including no zero-length path to other vertices. Two distinct influence indicators:
- `D_{v,s} = p_{v,s} mod 2` (semantic / GF(2) derivative);
- `R_{v,s} = 1[p_{v,s} > 0]` (structural dependency reachability).

**Lemma G2B1-L1, restricted and classical (PROVED by induction):** `y_v(x)=XOR_{s in S} D_{v,s} x_s`, so `y_v(x xor e_s) xor y_v(x)=D_{v,s}` for every input x. Thus if *every node output bit is explicitly materialized* as a separate up-to-date remote bit and the update modifies only the cells that changed, exactly
`h_s=Σ_{v∈V} D_{v,s}`
output cells flip; this is a property of the specified eager representation, **not** a lower bound on all implementations. Its derivation is the GF(2) linearity of a circuit, not a new fundamental theorem. Since path parity implies path existence, `h_s≤r_s=Σ_{v∈V}R_{v,s}`.

**Proof:** Source basis case `D_{s,t}=1[s=t]`. For internal v, substituting the inductive expansions gives `D_{v,s}=XOR_{u∈Pred(v)}D_{u,s}`, exactly parity of all directed s-to-v paths partitioned by their final predecessor. Linearity yields the flip difference. For any v, if `D_{v,s}=1`, there exists at least one path, hence `R_{v,s}=1`; sum both indicators. QED.

**Lemma G2B1-L2, *specified hash representation only*:** Suppose each node caches a digest of **domain-separated (vertex ID, static ordered predecessor IDs, its own Boolean value, all ordered predecessor digests)**, with trusted previous roots/version held by the owner. A FLIP(s) structurally recomputes each digest at every reachable descendant v. In the *collision-free restriction* (or computational collision-resistance conditioned on no adversary producing a hash collision) every v with `R_{v,s}=1` has a different digest after the update: prove by induction from the source along any affected predecessor path, because at least one predecessor digest differs even if `y_v` cancels to the old value. There are exactly `r_s` changed cached digest nodes in this representation. This **does not** imply any general lower bound on other ADS designs, on proof bytes, on HMT/VC, on an owner's CPU without eager caching, or on the semantic `h_s`.

**Security boundary:** SHA-256 finite tests merely compare concrete digests, and do not establish computational collision resistance. A DAG root might require an additional commitment aggregating multiple sinks. Replaying an epoch, maintaining forked clients, batching updates, or suppressing messages requires an independent threat/security experiment. No claim here that a changed digest alone proves authenticated UPDATE correctness: a malicious server could construct a different root unless the owner verifies the transition (as in G2-B).

## 3. An arbitrarily large falsifying family

For any K≥1 construct a diamond fanout DAG with vertices
`s, a, b, t_1,...,t_K` and arcs `s→a,s→b,a→t_j,b→t_j` for all j.
Every terminal `t_j` has exactly two directed paths from s. Each `t_j` depends structurally on s but its GF(2) value always equals `x_s xor x_s=0`.

For FLIP(s):
- all `K+3` vertices are reachable, `r_s=K+3`;
- only `s,a,b` output bits change, `h_s=3`;
- the K terminal output bits are unchanged **yet K terminal SHA-256-style digests change** because their predecessor digests change.

Thus `r_s/h_s=(K+3)/3` diverges with K. **A bound of the form "every structural dependent semantic output must change" is false**; the converse assertion "only changed output bits can require structural certificate work" is false for the *specified* hash-DAG representation. These are direct countermodels, not novel lower bounds.

## 4. Cost ledger for the SAME FLIP/READ task

Let `n=|V|,m=|E|,w` physical cell bits and `lambda` hash digest bits. Charge preprocessing `T_setup`, trusted roots/version `S_trusted`, remote input/output/digest bits `S_remote`, update reads/writes `U_r,U_w`, query reads `Q_r`, `C_total` bits of both directions, prover hashes `G`, owner verifier hashes `V`, adaptive horizon H and error epsilon.

| Named implementation | Setup & remote storage | FLIP(s) physical writes | READ(v) work | Proof / freshness |
|---|---|---|---|---|
| Recompute-on-query source bits | `|S|` bits + immutable topology | **1 bit** source flip | evaluate ancestor DAG, potentially Θ(n+m) logical operations (or query path count) | NO |
| Eager materialized values | n output bits + source encoding | `h_s` stored Boolean bits change; computing affected nodes can read many unaffected values | **1 bit-probe** | NO |
| Eager structural hash-DAG | n outputs + nλ digests + topology | `h_s` output bits + `r_s` changed digest cells of λ bits each; work depends on incident edges | reading stored output 1 bit only if client trusts server; malicious proof requires a separate authenticated path | **Conditional hash binding only with authorized transition verification** |
| Lazy invalidation/memoization | source bits, cached values, dirtiness flags | can mark `r_s` flags starting clean; if already dirty, fewer physical bit changes | pay recomputation on cache misses; proofs separate | NO automatically |
| IVC/UpBARG/stream prover | model-specific proof/digest/store/public params | **requires original cited hypotheses and full protocol** | costs in author's model, not inferred from this table | computational conditional security |

**Minimal no-free-helper warning:** A client who receives all FLIP labels *and stores all source bits* can locally answer requests; that pays `S_trusted≥|S|`. If the client starts with trusted current values and no server, `B_proof=0`; any universal strictly positive proof-size lower bound with unconstrained trusted state is false. This is a different resource point of the same task.

**Strongest honest conclusion:** These constructions separate algebraic propagation and structural proof invalidation, **but do not exhibit an `R in B_known\Ach` asymptotic infeasible point** for authenticated protocols. Merkle path validation, IVC and lower bounds live in different models until a reduction prices each resource identically.

## 5. G2-B1 status and next falsifiable problem

**STOP**: basic online 2D XOR aggregate authentication (G2-B) as original-root headline; source material already overlaps ADS and VC. Also **STOP**: reachability counts as the obligatory semantic-update work of a DAG; path parity cancels. Also **STOP**: cryptographic hash-metadata maintenance = inherent cost of every authenticated protocol; eager hash DAG is just one construction.

**GO for G2-B2 only after further prior art:** choose one natural *persistent multi-subscriber* task with untrusted server and separately maintained clients. Each subscriber has a fixed demand for a historical/derived DAG output, a maximum persistent trusted-state budget `s`, a bounded `q` source probes per query and `v` authenticated proof verification work; every public update must preserve both **state evolution** and **freshness against adversarial server equivocation**. Charge per-client receipts, total broadcasts, work, persistent setup, explicit computational security and fork/rollback conditions. Compare zero-communication `|S|`-bit client upper protocol, eager Merkle DAG, IVC, direct source reads and proof-carrying updates **in one exact scenario**, rather than multiplying published independent bounds.

**No G2-B2 numeric inequality yet**. Next allowed action: freeze the actual subscriber set/visibility/leader authority/horizon, specify three costed upper constructions, and then one candidate asymptotic separation from same-model published `B_known`. If none survives, declare STOP of root approach rather than invent one.
