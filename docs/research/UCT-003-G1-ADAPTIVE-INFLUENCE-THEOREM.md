# UCT-003 G1-A — adaptive read/write influence and one-probe exact barrier

**Date:** 2026-10-09. **Issue:** [#82](https://github.com/definitely-stable/Mathlab/issues/82); parent [UCT-002 #77](https://github.com/definitely-stable/Mathlab/issues/77), original-novelty selection [#76](https://github.com/definitely-stable/Mathlab/issues/76). **Evidence:** SELF-CONTAINED DERIVED_CLASSICAL / EXACT FINITE ORACLES. **NOT a new scientific theorem.** No Rust. No imported source proof treated as independently reproved.

## 1. Exact dynamic bit-probe contract

Let X be any finite state set and E⊆X×X any allowed directed update edges. A deterministic, state-independent memory encoder M:X→{0,1}^m is correct for a public family of Boolean functions f_j:X→{0,1}, j∈J, if **one fixed query algorithm** A_j, using only its public query index j, program constants and adaptive reads of M(x), returns f_j(x) on every x∈X. Updates may be modeled as transformations of states; the cost charged here is the number of physically *changed bits*, NOT the number of update probes, computation steps or touched physical machine words.

For an edge e=(x,y), W_e={c∈[m]:M(x)_c≠M(y)_c}. During A_j on M(x), let R_j(x)⊆[m] be the set of bit-cell addresses actually read (one address can be probed more than once; multiplicity does not affect intersections). Each A_j reads at most p cells. No state-dependent annotation, cached root, auxiliary hint, oracle response, randomness, history, authenticated proof or public state-dependent operation arguments are available to queries without **explicit inclusion in this charged memory**. The program and query index are fixed across x,y. This is an exact bit-probe model, not the cell-probe model with multi-bit words.

Define D_e={j∈J:f_j(x)≠f_j(y)}. Define τ(𝔽) as the minimum cardinality of a set hitting every member of 𝔽, with τ(∅)=0 and τ(𝔽)=∞ if 𝔽 contains the empty set.

## 2. Theorem A — adaptive influence/transversal lemma

**THEOREM (DERIVED_CLASSICAL).** For every allowed edge e=(x,y),

    W_e ∩ R_j(x) ≠ ∅   for each j∈D_e
    and therefore |W_e| ≥ τ({ R_j(x) : j∈D_e }).                  (1)

**Proof.** Suppose a query j has f_j(x)≠f_j(y) yet W_e∩R_j(x)=∅. Execute A_j on M(x) and M(y) in lockstep. The first probed address is the same because no state-dependent information has been read. Inductively, all previous answers on the old-state trace are identical (none of the probed coordinates changed), so the deterministic program selects exactly the same next address and receives the same answer. It terminates at the same time and returns the same bit, contradicting correctness. Thus W_e intersects every old-state read path R_j(x) whose observable changes. Every such path is a set requiring a hitting cell, yielding (1). QED.

**Two useful scoped refinements.** (i) The conclusion remains valid with arbitrary *adaptive* probes, because the proof fixes the old-state transcript; it does NOT require static/nonadaptive query addresses. (ii) With a set S of update edges along a path from x to y, the union of changed-cell supports along that path hits the old-state query read paths for queries whose endpoint outputs differ; consequently the *total number of physical writes along the path*, including repeated writes, is at least the same τ. This path claim is also classical and not an amortized optimum.

**Important failure modes.** The theorem does **not** apply when queries have free state-dependent external storage, an uncharged authenticated root, a separately changed proof/annotation, or access to update history (unless all such observations are included as charged cells/probes). A hash collision probability or a proof's cryptographic security cannot be derived from (1). On-line untrusted prover soundness additionally needs a model of who can generate a witness and when; the bit-path argument alone is not such a proof.

## 3. Theorem B — exact characterization of all one-probe Boolean services

Let 𝔽 be the set of nonconstant functions among {f_j}, quotient by f~g iff g=f or g=1−f *as functions on the entire X*. Let c=|𝔽/~|. For edge e=(x,y), let

    d(e)=#{classes [f]∈𝔽/~ : f(x)≠f(y)}.

**THEOREM (DERIVED_CLASSICAL, EXACT FRONTIER).** If all f_j are correctly answered with at most **one bit probe** and no free state-dependent side channel, then

    m ≥ c  and  |W_e| ≥ d(e) for every e∈E,
    hence w ≥ max_{e∈E} d(e).                                   (2)

Both bounds are simultaneously attainable in the abstract representation/known-new-state model by storing one representative f(x) per class. This is a *complete extremal characterization for the p≤1 representation model*, not a claim for general multi-probe, randomized or real online algorithms.

**Proof.** A query for a nonconstant f_j cannot use zero probes. Because it has at most one probe, its queried address a_j∈[m] is fixed by the public j, before it has observed any state-dependent bit. Its output is a Boolean map g_j(M(x)_{a_j}), independent of x except through the read bit. Nonconstancy of f_j forces g_j to be either the identity or negation (the other two Boolean unary functions are constants). Thus for all x, M(x)_{a_j}=f_j(x)⊕δ_j for one fixed δ_j. If two query functions select the same address, they are identical or complements, so distinct classes require distinct codeword cells. There are at least c such cells. Along any edge e, each changed function class forces its associated distinct cell to change. Hence (2). Conversely store one representative f from each class in a distinct bit; every function is either constant, that stored bit, or its complement. On edge e exactly d(e) of those bits change. QED.

**Online implementability warning.** If queries distinguish only a quotient of states, a representation may not admit correct updates from its bit vector and a public operation label alone. The upper-bound construction is an exact representation and a valid update implementation only if public labeled updates preserve the representation equivalence (a transition congruence), or the updater receives appropriately charged information about the new state. Dynamic prefix parity below **does** satisfy labeled-update congruence.

## 4. A natural task: full dynamic prefix parity (XOR partial sums)

Let X=F₂^n and for k=1,...,n define

    f_k(x)=⊕_{i=1}^k x_i.

Permitted updates toggle a single input bit i (public operation label `toggle(i)`). All n prefix functions are nonconstant and pairwise distinct even modulo complement; for k≠l, their XOR is a nonconstant contiguous parity of some input bits.

A toggle of input bit i changes precisely f_i,...,f_n, so d(toggle(i))=n−i+1. Theorem B gives the exact simultaneous necessary bounds, for **any** deterministic nonlinear binary representation and exact one-bit-probe query decoder:

    m ≥ n,   w ≥ n.                                               (3)

These bounds are **sharp** in this model: store all n prefix parities in n bits. Query f_k uses one direct bit probe. Toggle(i) flips the stored bits k≥i, changing n−i+1 cells, with worst case n for i=1; the updater needs only the public index, so no hidden old-state oracle is needed.

This is **strictly stronger than the UCT-002 Hamming-ball capacity bound on this named operational task**: using the raw input bits M(x)=x with m=n and write locality w=1, the global observation-capacity bound holds (take d=n from 0^n, V₂(n,n)=2^n), but each f_k query requires up to k input probes. Thus UCT-002 alone cannot derive w≥n at p=1. Conversely UCT-003 exploits which query needs which codeword reads. It does **not** imply a new worldwide lower bound for dynamic partial sums: Fredman–Saks 1989, Pătraşcu–Demaine 2006, Pătraşcu–Tarniţă 2007 and dynamic coding already address much harder multi-probe regimes.

## 5. Contrast: two sharp extremes and the Fenwick middle

Three exact F₂^n representations are a falsification check against claiming `w*p ≥ n` universally:

| Representation | Stored bits | Worst changed cells per toggle | Worst bit probes per prefix |
|---|---:|---:|---:|
| Raw input bits | n | 1 | n |
| Stored every prefix parity | n | n | 1 |
| Standard Fenwick binary indexed tree | n | ≤⌊log₂n⌋+1 | ≤⌊log₂n⌋+1 |

The Fenwick design is an existing data structure (not UCT novelty). For sufficiently large n it contradicts the tempting false `wp≥n` conjecture because the product is O(log²n)≪n. Exact dynamic bit-probe/cell-probe lower bounds in the literature must be checked before proposing any stronger generic w–p theorem.

## 6. Relation to other Mathlab theorem bricks

| Brick | Typed relationship | Forbidden shortcut |
|---|---|---|
| UCT-002 exact capacity | **STRICTER TASK-SPECIFIC NECESSARY BOUND**: adds actual read-trace/query influence not present when the whole encoding is freely observed. | UCT-002's product formula does not entail sharp one-probe sensitivity. |
| LENT-001 sparse-write bound | **PARALLEL RESOURCE BOUND**: Hamming growth of reachable codes + (1) influence hitting sets. | Cannot assume an additive-code construction or equivalence of read/write code locality. |
| TOM-003 transition equivalence | **MODEL BRIDGE**: on-line implementation of function vector must be congruent under operation labels. | Observational equality on one snapshot does not imply future equivalence. |
| HYP-103 certificate reduction | **DUAL HITTING-SET LEMMA**: certificate search and update/write hitting the changed-query read paths are both classical transversals, but quantify different objects. | They are not equal optimal certificates or a free untrusted-prover protocol. |
| TOM-005 output fanout | **RESTRICTED SPECIAL CASE**: when n distinct outputs are separately materialized and one read each, forcing all to change costs n physical writes. | Lazy or encoded multi-read representations evade the bound. |
| UCT-003 patch qgram gap | **ANALOGY ONLY**: weak local summaries need not bound full operation cost tightly. | No reduction from COPY/ADD patch bytes to prefix parity cell writes. |
| DeltaMeter | **THREAT-MODEL ONLY**: error/adaptive guarantees must be explicit. | (1) is exact deterministic, does not certify finite-sample statistical estimators. |

## 7. Prior-art barrier and next genuinely new theorem question

**Primary mathematical foundations:**
- [Fredman–Saks 1989, STOC, DOI 10.1145/73007.73040](https://doi.org/10.1145/73007.73040) (canonical Mathlab LIT-111): dynamic partial sums, access/read–rewrite complexity lower bounds.
- [Pătraşcu–Demaine 2006, SIAM J. Comput., DOI 10.1137/S0097539705447256](https://doi.org/10.1137/S0097539705447256) (LIT-112): sharper dynamic update–query tradeoffs under cell-probe word/probability models.
- [Pătraşcu–Tarniţă 2007, TCS, DOI 10.1016/j.tcs.2007.02.058](https://doi.org/10.1016/j.tcs.2007.02.058) (LIT-114): dynamic bit-probe complexity; partial sums as an existing target.
- [Viola, *Bit-Probe Lower Bounds for Succinct Data Structures*, SIAM J. Comput., DOI 10.1137/090766619](https://doi.org/10.1137/090766619): lower bounds for *static* succinct local queries, not the theorem (3); metadata/abstract consulted, full original proof not audited.
- [Chandran–Kanukurthi–Ostrovsky 2014, TCC, DOI 10.1007/978-3-642-54242-8_21](https://doi.org/10.1007/978-3-642-54242-8_21) (LIT-127): local writes and local decoding under their own corruption/security assumptions.
- [Chakrabarti–Cormode–McGregor–Thaler 2014, DOI 10.1145/2636924](https://doi.org/10.1145/2636924) (LIT-129): sound untrusted annotations and verifier-space tradeoffs.
- [Ko 2026, ECCC TR26-047](https://eccc.weizmann.ac.il/report/2026/047/) (LIT-119): contemporary Multiphase joint update/query barrier.

**Current verdict:** (1) and (2) are **PROVED_DERIVED_CLASSICAL** with independent finite oracles, **NO NOVELTY CERTIFICATION**. The `n`-write one-probe lower bound is already suggested by known representation/probe arguments. The central original theorem of UCT remains OPEN: construct a **natural dynamic task** with p≥2 plus *fully charged authenticated/untrusted verification* for which a quantified nonfactorizing joint bound is **strictly stronger** than all existing same-model theorems and survives an upper construction/finitary adversarial audit. We should not label (1) as that discovery.
