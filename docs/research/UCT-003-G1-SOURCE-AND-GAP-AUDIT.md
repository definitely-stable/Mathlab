# UCT-003 G1: decisive source-to-model comparison and next nonfactorizing target

**Date:** 2026-10-09. **Issue:** [#82](https://github.com/definitely-stable/Mathlab/issues/82). Primary proof: [UCT-003 influence theorem](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md). Status: **DERIVED_CLASSICAL proof, novelty STOP at p=1; p>=2 with trusted/untrusted verification OPEN, not asserted feasible/novel**.

## A. What actually changed relative to UCT-002

UCT-002 assumed the entire maintained q-ary code was available to the verifier as one observed string and charged only *additional* external reads, so its necessary capacity formula omitted costs for *locally accessing the maintained representation*. To bridge it to an implementable query service we must add:
- a public query index; a deterministic potentially adaptive program; all memory-probe addresses and returned bits; timing/order and exact read quota p;
- the actual bit locations changed by an update edge (and not merely the nominal abstract state transition);
- an update-label congruence rule so the online update is implementable without free historical raw input;
- complete accounting for any shared trusted helper, cryptographic authenticated root, untrusted prover witness, external oracle, randomness and transmitted data.

With these charged objects, a changed query answer forces old-path read/write intersection. The minimum local write support is bounded by a **transversal of adaptive read paths**, unlike global Shannon/Hamming capacity. This is a valid extra operational **constraint**, but classical graph/hitting-set information, not automatic novel theory.

## B. Exact source and theorem overlap

| Original work | Precise overlap | What remains untransferred |
|---|---|---|
| [Fredman & Saks, STOC 1989](https://doi.org/10.1145/73007.73040), **LIT-111** | Dynamic partial sums mod 2, lower bounds connecting reads and register rewrites; foundational chronogram. | Their amortized/cell-probe model and history-sensitive operation sequences differ from **changed** Boolean coordinates measured in this elementary local theorem. Our prefix p=1 extreme must NOT be claimed to supersede them. |
| [Pătraşcu & Demaine, SIAM J. Comput. 2006](https://doi.org/10.1137/S0097539705447256), **LIT-112** | Randomized/amortized optimal partial-sum and connectivity tradeoffs in word cell-probe, includes stronger complexity phenomena than p=1 counting. | Bit writes vs word probes, expectation vs worst-case, randomized vs deterministic. |
| [Pătraşcu & Tarniţă, TCS 2007](https://doi.org/10.1016/j.tcs.2007.02.058), **LIT-114** | Explicit dynamic **bit-probe** partial sums, update/read tradeoffs, related group problems; closest direct prior art. | Must read full paper's model and results before claiming any p>=2 sharp separation. |
| [Chandran, Kanukurthi & Ostrovsky, TCC 2014](https://doi.org/10.1007/978-3-642-54242-8_21), **LIT-127** | Already couples low write-locality and low read-locality under corruption/security goals. | Prefix-Hamming/adversarial corruptions, update algorithm and cryptographic shared secret are not present in our deterministic proof. |
| [Viola, SIAM J. Comput. 2012](https://doi.org/10.1137/090766619), **source-scoped, not imported in this first G1 cut** | Static succinct bit-probe lower bounds for ternary sequences and set membership, including adaptive probes; shows 'local read + info capacity' is classical. | Static succinct redundancy and randomized/localized encoding assumptions differ from updates and sound proofs. |
| [Annotated data streams, ACM 2014](https://doi.org/10.1145/2636924), **LIT-129** | Proof-helper bytes vs verifier memory and data order, with **soundness against dishonest prover**. | Counting honest witness bits or treating them as persistent trusted state is NOT online Merlin–Arthur soundness. |
| [Ko, ECCC 2026](https://eccc.weizmann.ac.il/report/2026/047/), **LIT-119** | Existing modern cell-probe joint update/query lower bound and communication verification round. | Auxiliary verifier round in lower-bound proof is not equivalent to authenticated dynamic witness. |

Related original Mathlab anchors: [UCT-002](UCT-002-MASTER-THEOREM.md), [LENT-001](LENT-001-FOUNDATION.md), [TOM-003](TOM-003-TRUST-BOUNDARY-PROTOCOL.md), [HYP-103](HYP-103-G0-CERTIFICATE-REDUCTION.md), [TOM-005](TOM-005-SEVEN-THEOREM-AUDIT.md). They are **bricks** with different quantified models, not six statements of a universal new law.

## C. Four new candidates, only one selected at each exact proof gate

**Candidate C1 — adaptive influence transversal (PROVED_CLASSICAL / STOP_NOVELTY).** Full state-local hitting-set theorem and *sharp complete* one-probe Boolean service characterization; tight prefix XOR example m=w=n and a Fenwick falsifier for wp>=n. This becomes an accepted auxiliary theorem but **NOT a standalone publication target**.

**Candidate C2 — two-probe dynamic signed prefix service (SCOUT_NARROW).** Freeze bit-probe, n-bit prefix parity updates, p=2, state-dependent reusable authenticated witness with stated bytes/maintenance costs and adversarial choice of query. A claimed lower bound must distinguish a stable trusted witness from malicious prover messages, account for all cell accesses and not be subsumed by 1989/2006/2007 prior art. First finite task: enumerate optimal solutions at n<=3 with and without charged shared state, and compare bit-probe lower bounds before attempting a general theorem. If only a trivial storage/encoding trick survives, STOP.

**Candidate C3 — batch certificate influence cut (SCOUT_NARROW).** For a fully specified batch update protocol with authenticated old root, derive a *conditional* information transfer cut over all changed query answers with an explicit old-state oracle and source proof. HYP-103 already solves broad min-old-bit probes by promise certificates; new claim must be an additional strict **end-to-end** bound involving transcript consistency across many updates, not rebrand hitting set.

**Candidate C4 — adaptive stochastic/cyber-security analogue (SOURCE_AUDIT_FIRST).** Replace exact deterministic answers by conditional risk guarantees and **one fixed** adversarial experiment. Transfer requires a legitimate random seed/side-information model, union-of-bad-events bound, leakage or PRF reduction. No equation summing probability loss and computational advantage without proof. Existing DeltaMeter risk is not automatically a certificate for this dynamic query service.

## D. Broad result and exact STOP boundaries

- **ACCEPT as derived classical:** equations (1)/(2), prefix XOR tight w=n at p=1, and Fenwick counterexample against the false generic product `w*p>=n`.
- **STOP** calling this an originally discovered joint lower bound, a cryptographic verification theorem, or asymptotically optimal p>=2 coding.
- **OPEN** whether ANY natural fully priced C2/C3/C4 case gives a strictly new nonfactorizing theorem not implied by cell-probe, LULDC, annotated streaming or certificate complexity.
- **NEXT ISSUE / proof:** if finite C2 search exhibits a persistent gap, freeze its exact quantified claim before implementation; if prior art covers it, mark STOP and change direction. A mathematical theorem cannot be 'proved by many CI tests'; CI is a falsification and regression companion to a deductive proof.

## E. Mandatory reproducibility
`research/test_uct003_influence.py` covers 256 binary memory encodings x 128 depth-two decision trees, exhaustive 3-query one-probe Boolean families on two-state bits, independently computed hitting sets, exact prefix-XOR updates, Fenwick construction and the uncharged external helper countermodel. Success is not evidence of originality.

## F. Additional complete unit-write rigidity result (G1-A)

[Theorem C](UCT-003-G1-ADAPTIVE-INFLUENCE-THEOREM.md#4b-theorem-c--exact-unit-write-hypercube-embedding-rigidity-second-sharp-frontier) proves that any injective embedding of the FULL n-dimensional labeled bit-toggle hypercube into a binary maintained code with at most one changed bit per toggle must be a fixed coordinate injection plus a constant offset. Consequently every deterministic query requires at least D(f) reads; for full prefix parity, p>=n when w<=1. This is the **opposite sharp endpoint** to the w>=n barrier when p<=1. A fully exhaustive small-hypercube embedding oracle was added. This remains **DERIVED_CLASSICAL**, overlapping cubical-graph embedding theory (Mathlab LIT-120..122) and dynamic bit-probe partial-sum prior art (LIT-114), NOT a new n-parameter general theorem at p>=2. The Fenwick middle prevents false broad interpolations.
