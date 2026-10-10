# DAG-002 × ALG-001 G1-C2-E — cross-history source-information gate

**Issue:** [#161](https://github.com/definitely-stable/Mathlab/issues/161), parent [#140](https://github.com/definitely-stable/Mathlab/issues/140).
**Branch independence:** built on current main, not on dependent PRs #267/#268/#271/#274.
**Mathematical status:** EXACT_CROSS_HISTORY_FIBER / ELEMENTARY_INJECTION / LAZY_QUERY_ESCAPE / STOP_THEOREM_NOVELTY_FOR_THIS_RESTRICTED_BOUND / UNIVERSAL_ROOT_STILL_OPEN.

## Precise difference from G1-B

G1-B bounds K distinct next-step outputs when a *single, identical complete old history* is fixed. G1-C2-E varies the previous DAG prefix while keeping its vertex count, IDs and the next parent command identical. Its K is therefore a **cross-history fiber**, and G1-B's conditional inequality CANNOT be invoked to bound it. No unjustified summing across histories is allowed.

An append-only DAG with vertices 0..n-1 receives APPEND_SINK(v=n,S), where S is a subset of earlier vertex IDs. The exact Boolean old-to-new reachability vector is

    T(prefix,S) = union_{p in S} ({p} union Ancestors_prefix(p)).

The parent incidence command is n input bits, available to the updater, and is NOT free to subsequent queries. The same target-only query answer must be correct for arbitrary permitted earlier prefixes.

## G1-C2-E-L1 (strict conditional, elementary): cross-history fiber requires old information

Freeze the public code/program, the next vertex n, its fresh-label address, the same next parent set S and all data independent of the earlier prefix. Assume:
- Updater performs R_u=0 remote/source reads and sees only S plus H retained mutable trusted bits.
- The next new-record writes and local-state updates are deterministic functions of that visible information; no free old remote directory, old source parent array, changing ROM, clock, history, allocation addresses, or out-of-band parent ancestry.
- Subsequent query(u,new_target) sees only the new target label/record plus the resulting H bits and public u,n,S-independent fixed code, with **no old-label/source reads**. It cannot use implicit old-address placement as a side channel.
- Correctness is exact and deterministic for every eligible prefix.

For any family F of earlier prefixes with identical public context and a fixed S, let K be the number of distinct truth vectors T(prefix,S). All previous prefixes with the same H-bit updater-visible state lead to the same fresh record and final local state, hence the same target-only answers. Therefore every distinct truth vector needs a distinct old local state:

    K <= 2^H, so H >= ceil(log2 K).

This is the elementary pigeonhole/indistinguishability argument. It is **NOT** a new general bit-probe lower bound, does not constrain actual DAG schemes that read parent labels at update or old labels at query, and cannot be promoted to UCT-005. If a representation is allowed free changing codebook/addresses or hidden local cache, the hypothesis is false.

## Exact fiber: the most recent parent

For fixed S={n-1}, the output always contains ancestor n-1 and can contain ANY subset of vertices 0..n-2. Realize each desired subset by keeping 0..n-2 an antichain and making precisely those vertices parents of n-1. Thus there are exactly

    K = 2^(n-1), for n>=1,
    H >= n-1 (conditional on R_u=0 and the target-only restriction above).

At n=2, two old DAGs

    F0=((),())       F1=((),(0,))
    S=(1,)
    T(F0,S)=binary 10
    T(F1,S)=binary 11

have identical public vertex count, IDs, next parent input and zero retained local state, but different correct query reach(0,2). A target-only/no-read new-label program cannot distinguish them. This does not contradict G1-B; its histories differ.

## Exact escape, refuting unrestricted read lower bounds

A **lazy adjacency** codec appends only the new vertex's parent list. It needs ZERO updater reads of older source records and remains correct for every append history. Queries perform backwards DFS and read older adjacency records, charging each read and its complete serialized bytes. For fixed horizon h, parent IDs cost max(1,ceil(log2 h/8)) bytes each and every new record has a four-byte length header. The complete n-bit next-parent incidence command is charged separately; the in-memory adjacency-array model does not claim full-page I/O, bounded R_q, authenticated storage, crash safety, bounded query time or trusted RAM cap.

This explicit counterconstruction destroys a proposed UNIVERSAL append-DAG "R_u>=1" theorem. It illustrates a paid update/query locality tradeoff, not a novel theorem. Similarly, retaining previous ancestor masks in H mutable bits moves costs to trusted state and its prior maintenance; cannot be assumed gratis.

## Prior art / sources and classification

1. [Bulteau, David, Horn, Tran-Girard, *Incremental Reachability Index*, SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9), primary source explicitly addresses append-only DAG and immutable labels. The lazy adjacency and eager closure constructions are classical baselines, not source-distinct new indexing schemes.
2. [Chandran, Kanukurthi, Ostrovsky, *Locally Updatable and Locally Decodable Codes*, TCC 2014](https://doi.org/10.1007/978-3-642-54242-8_21): already formalizes update-vs-decode locality in a distinct Prefix Hamming corruption model; no same-model fresh DAG lower bound follows automatically.
3. [Pătraşcu and Tarniţă, *On Dynamic Bit-Probe Complexity*, TCS 2007](https://doi.org/10.1016/j.tcs.2007.02.058): known update/query bit-probe tradeoff theory, not a same-model direct corollary of this cross-history fiber.
4. [Larsen and Yu, *Super-Logarithmic Lower Bounds for Dynamic Graph Problems*, FOCS 2023 / SIAM 2025](https://doi.org/10.1137/24M1638215): states a bound for DAG reachability under **edge insertions**, not append-only fresh sinks. Its graph-update lower bound cannot be transferred without a full resource-preserving reduction.
5. G1-B #159, G1-C1 #264, pending #267/#268/#271/#274: separate preexisting source/model/physical crash gates. No new work IDs here (#147 controls catalog reservation).

These are checked publication titles, abstracts and operation scopes; no claim is made to have reproduced every original-paper theorem/proof. Therefore record **STOP_THEOREM_NOVELTY for L1 and eager-vs-lazy comparison**. Do not claim an exhaustive STOP on all #161 possibilities.

## Independent finite falsification and reproducibility

    python research/dag002_g1c2e_prefix_gate.py
    python -m unittest discover -s research -p 'test_dag002_g1c2e_prefix_gate.py' -v

Oracle exhausts all ordered DAGs n<=4 and ALL next-parent subsets, cross-checking a second backward DFS oracle. The most-recent-parent K=2^(n-1) fiber is counted exactly through n=5. A separate lazy adjacency reference verifies zero updater reads and charged query record/byte reads on all 64 four-vertex graphs. Exact negative cases include n=2 prefix twins and empty parent command, input validation and unpriced source access rejection.

**Acceptance:** exact-head focused + full hosted Research CI, independent review, no overlap with parallel HYP/UCT source edits. Keep issue #161 OPEN for only a genuinely different, fully scoped root hypothesis after primary-theorem novelty audit. Given the existing UCT-005 COW/authenticated/GC lines, repeating them without a resource-preserving new premise is a STOP, not a new research milestone.
