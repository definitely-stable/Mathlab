# UCT-005 D1-B2-F3-D — deferred-output phase-cut counting bound

2026-10-11. [Research issue #297](https://github.com/definitely-stable/Mathlab/issues/297), [root #105](https://github.com/definitely-stable/Mathlab/issues/105), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). Depends on the one-pass speculative-stage *research input* [F3-C #294](https://github.com/definitely-stable/Mathlab/pull/294), itself downstream of accepted F3-B [#290](https://github.com/definitely-stable/Mathlab/pull/290). **Status: RESTRICTED_CLASSICAL_COUNTING_LEMMA / ONE_PHASE_INFORMATION_PIGEONHOLE / NO_NEW_UCT_ROOT / ROOT_OPEN_UNPROVED.**

## Frozen deterministic exact-output model

Fix a binary old source payload of N bits and a known distinguished coordinate i. Require a new full N-bit image with i overwritten to 1, all other coordinates unchanged. Restrict the input family to x_i=0; therefore **2^(N−1)** distinct requested outputs exist.

Let λ be total trusted digest/root bits that may carry information about x, b be additional data-dependent trusted algorithmic memory at the authentication boundary, W_pre be full P-byte untrusted staging pages written *before old-source authenticity is accepted*, q_after be full P-byte old-source reads performed after authentication, and A be **all extra data-dependent channel bits** (addresses, variable lengths/timing, receipts, helper state, free copies), zero only when protocol forbids them or charges fixed public addresses and fixed sizes. The model excludes unpriced external data-dependent advice, server-side copy, trusted full replica, write-before-gate shortcuts other than W_pre, and randomized error claims. Both SHA-root and (digest+generation) bookkeeping are separately paid; real SHA preimage security is NOT used in this inequality.

### Restricted necessary inequality (trivial classical counting, not a novel theorem)

For every **deterministic** exact reconstruction protocol in this grammar:

```
N − 1 ≤ λ + b + 8P (W_pre + q_after) + A .
```

**Proof:** Fix x_i=0. Across the verification boundary, at most 2^(λ+b+8PW_pre+A) data-dependent states are available (digest, scratch, speculative externally written payload and separately charged side channels). With at most q_after additional P-byte old-source reads, at most another 2^(8Pq_after) result sequences can occur. Adaptively selected read addresses are deterministic from previous state and responses; any independently data-dependent address channel belongs in A. If the total number of distinguishable transcripts were below 2^(N−1), two inputs would produce the same transcript but demand distinct outputs. Contradiction. This is a vanilla **injection/pigeonhole lemma**. It is only necessary, not sufficient for any SHA-authenticated protocol.

When W_pre=0 and A=0:

```
q_after ≥ max(0, ceil((N−1−λ−b)/(8P))).
```

This forces a second-phase volume of old-source reads only when N≫λ+b. It does **not** force an entire second scan at all sizes, and becomes vacuous if λ+b≥N−1. No physical security/durability, verifier error, prover CPU, NAND amplification or original UCT lower bound follows.

## Relation to F2 and F3-C

F2's stronger *zero speculative write* discipline uses W_pre=0 and its chosen concrete second SHA pass reads M pages. F3-C permits speculative write-before-authentication, so W_pre=M and q_after=0 while preserving a trusted publish-after-check gate under ideal serialized/durable-stage assumptions. The restricted phase-cut counting inequality accommodates **both** and cannot rank all resource axes. It does not imply F2's 11M and F3-C's 7M online totals are universally optimal. Failure-side speculative P-byte writes and paid stage deletion must be included independently; the total-memory claim remains conceptual bitmap payload only.

## Reproducibility and limits of finite witness

[Standalone analytic oracle](../../research/uct005_d1b2f3d_deferred_output.py) reports the exact bit capacity, necessary post-auth page ceiling and explicit unknown security fields, without iterating exponential 2^N transcript sets. [Independent finite tests](../../research/test_uct005_d1b2f3d_deferred_output.py) enumerate N up to 80 across arithmetic budgets, and **fully enumerate all 2^(N−1) fixed-target inputs for N=8 and 16** for selected boundary constructions. Those witness codes deliberately use a freely designed λ-bit abstract digest carrying designated input coordinates, memory bits for the rest and public fixed-suffix P-byte reads; they are **not SHA**, do not prove a secure construction and do not collapse F1 authentication into free advice. Side-channel A, staging W_pre, trusted λ≥N, insufficient trusted bits and non-page-aligned words have separate kill tests.

This finite exact census is a **sanity check of a separately written counting proof**, not a proof of a new information-theoretic discovery.

## Prior-art caution and negative gates

Nearby but different streaming models include Beame–Jayram–Rudra, *Lower Bounds for Randomized Read/Write Stream Algorithms* (STOC 2007, [author text](https://cse.buffalo.edu/faculty/atri/papers/complexity/rand-lb.pdf), [DOI](https://doi.org/10.1145/1250790.1250891)), and François–Jain–Magniez, *Unidirectional Input/Output Streaming Complexity of Reversal and Sorting* (APPROX/RANDOM 2014, [published full reference](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2014.654)). Their original result assumptions and task alphabets must be mapped before any formal transfer. This restricted pigeonhole inequality is plainly classical; record **STOP_NOVELTY** as to the *UCT root* even if focused finite tests all pass.

Countermodels that invalidate stronger unqualified claims: complete n-bit trusted replica; free remote server clone, unpriced source lookups or public programmable advice; variable-length/addresses hiding state; λ≥N; user-visible speculative page writes before authentication; randomized errors without explicit entropy/Fano terms; adversarial server denying page reads; page-size padding and multi-epoch anti-rollback not in this model. These are scope restrictions, not uncharged conveniences.

GitHub-hosted exact-head dedicated + full Research/INDEX/D1-A CI (as triggered), inherited F3-C/F3-B finite regressions and post-merge main evidence required. This stacked draft must not merge before F3-C predecessor acceptance. Parent UCT-005 remains **OPEN_UNPROVED**.
