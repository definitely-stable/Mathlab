# UCT-005 G2-B2 — exact multi-subscriber broadcast frontier (restricted information layer)

**Date:** 2026-10-09 · [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) · [G2-B #131](https://github.com/definitely-stable/Mathlab/issues/131) · [G2-B2 #151](https://github.com/definitely-stable/Mathlab/issues/151). **Status: ELEMENTARY_EXACT_RESTRICTED_PROOF / FINITE_EXHAUSTIVE_ORACLE / ROOT_NOVELTY_OPEN_UNPROVED.** Do not claim an original communication-complexity theorem, authenticated protocol, general lower bound or Rust production primitive.

## 1. Why G2-B1 does not finish the root

[G2-B1](UCT-005-G2-B1-DAG-SEMANTIC-STRUCTURAL-COUNTERMODELS.md) proves a restricted exact semantic/path-parity identity and shows eager hash-DAG invalidation is representation-dependent, not universal. Its proposed continuation involves multiple independent subscribers, but unpriced **free public FLIP labels**, anonymous multicast assumptions or unconstrained trusted local memory make nearly any attempted universal positive per-subscriber-proof lower bound false. We first freeze a correctly priced deterministic information-only broadcast layer before authentication.

## 2. Exact model: independent consumers of one fixed XOR DAG

An immutable topologically ordered GF(2) DAG has m independent Boolean source inputs and h designated subscriber output vertices. By G2-B1-L1, each subscriber output equals a known linear form (y_j=a_j\cdot x\) over GF(2), so row vectors form a fixed `h×m` binary influence matrix `A`. Initial input `x_0` is fixed. At epoch t, a trusted author applies a source delta `d_t in D subset GF(2)^m`, giving `x_{t+1}=x_t XOR d_t`. The **allowed update alphabet D is frozen in the task** and may include zero (a no-op); a publicly scheduled **tick** occurs even if d_t=0. A subscriber j starts with the correct one-bit local output `y_j=A_j·x_0` and an epoch counter; initialization of those outputs, distribution, and trust are separately charged. The publisher sends **one identical, fixed-length b-bit logical message** `M_t=Enc(x_t,d_t,t)` to all subscribers. No subscriber observes d_t, the original source array, the server, private per-user updates or any other update-dependent signals; its local state before seeing `M_t` is determined by prior messages and its own row, and therefore is independent of the fresh `d_t`. Each must output its correct next bit immediately with deterministic zero error. Encoders/decoders may have finite public lookup tables but **their complete length/setup must be priced**; no free arbitrary oracle.

**Information-only objective:** minimum b for one epoch, worst-case x, with *public* `D,A,t` and no update-dependent side channel. The synchronization of update *occurrence* is part of the given clock; if clock/ticks are not free, include their communication separately. This is **not** adaptive Byzantine server verification, proof freshness, persistent availability or computationally secure broadcast. For several epochs, the same one-epoch bound holds each time in the worst case because any allowable new delta may follow a common identical past; epoch and recipient identities do not convey the delta.

Define `Sigma(A,D)={A d : d in D} subset GF(2)^h`; define `K(A,D)=|Sigma(A,D)|`. `Sigma` contains the *joint* changes in all subscriber values, not the union of individually touched vertices.

## 3. G2-B2-L1 — exact zero-error broadcast bits (ELEMENTARY)

**Statement (under section 2, no unpriced update side channel):**

[
b^*(A,D)=\left\lceil \log_2 |\{Ad:d\in D\}| \right\rceil .
]

**Proof (lower bound):** freeze *the same epoch, identical past history and same pre-update x*, so every subscriber's private pre-message state is fixed. If two deltas `d,d'` with `Ad != Ad'` produced the same broadcast, then some j has `a_j d != a_j d'`; that subscriber has the same private past state and receives the same new message but must produce different next bits, contradiction. Thus the publisher's broadcast is an injective label on the equivalence classes of D modulo the relation `d~d' iff Ad=Ad'`. A fixed b-bit string has at most 2^b possibilities, so `2^b >= K`.

**Proof (upper bound):** enumerate `Sigma` in a fixed canonical order and send the b-bit index of `Ad`. Subscriber j decodes bit j of the selected h-bit syndrome and toggles its previously cached output. Every subscriber is correct. General codebook preprocessing/decoding may use `Theta(K h)` public bits and must be charged; absent bounded `T_program/T_preprocess` there is no polynomial-time *uniform* upper bound. **QED.**

This is ordinary exact deterministic one-way communication / quotient counting, *not* a novel lower bound about cryptographic signatures, linear FSS, memory checking or dynamic cell probes. A choice of a clever encoder cannot evade the quotient counting because all clients share one message but retain different one-bit outputs.

## 4. Three exact consequences and two killer counterexamples

1. **Full arbitrary deltas:** if `D=GF(2)^m`, then `Sigma=im A` and `K=2^rank_GF2(A)`, hence exactly `b^*=rank_GF2(A)`. A polynomial-time linear encoder computes a basis coordinate representation of `Ad`, requiring a public matrix basis plus its `O(mh)` setup (not free).
2. **One-coordinate toggles:** if `D={e_1,...,e_m}`, then `Sigma` is exactly the set of distinct **columns** of A. `b^*=ceil(log2 number_of_distinct_columns)`, including possibly a zero column. If zero delta also allowed, add the all-zero syndrome if not already present. All subscribers know a tick occurred but not the coordinate.
3. **Restricted affine delta families:** if `D=d_0+L` for an F2-linear subspace L, then `K=2^rank(A|_L)`; the constant offset `Ad_0` is publicly known and does not cost new broadcast bits. No requirement of *uniform efficient enumeration* beyond a given basis.

**False universal lower bound 1:** `b>=rank A` for all update alphabets is FALSE. For `A=I_m,D={e_i}`, `rank A=m` but `b=ceil(log2 m)`; for m=8, **3 bits**, not 8. If public update index `i` is supplied through another channel and not charged, the *additional* delta broadcast is zero; the complete communication must count the `ceil(log2 m)`-bit source label and its authenticity.

**False universal lower bound 2:** `b>=h` (one bit per subscriber) is FALSE. An entire h-subscriber system with identical nonzero rows A has only two possible syndromes under arbitrary d, so `b=1`; with obligatory single-flip and all identical columns, even `b=0` per known tick is possible. This does **not** eliminate the separate physical cost of copies to h receivers without a genuine multicast channel.

The independent tests [research/test_uct005_g2b2_broadcast.py](../../research/test_uct005_g2b2_broadcast.py) exhaustively enumerate small A and D and cross-check brute-force conflict coloring against the quotient formula. They test exact subscriber-output replay across deterministic adaptive update sequences. No cryptographic soundness claimed.

## 5. Fully charged protocols for the same task (not an asymptotic root proof)

| Named protocol | Subscriber trusted memory | Common logical update bits | Other priced costs/limitations |
|---|---:|---:|---|
| Quotient broadcast, section 3 | 1 output bit + epoch `ceil(log2(H+1))` | `b^*` | `T_codebook=Theta(Kh)` in generic nonuniform case, owner computation of `Ad`; transport h copies if pure unicast |
| Full update row `d` sent | 1 output bit + epoch | m | owner sends m-bit source mask; each reader computes row dot product, O(m) worst-case CPU; authenticated owner channel extra |
| Source-coordinate label (single FLIP) | 1 output bit + epoch | `ceil(log2 m)` | applies only to known mandatory unit updates; publication of source label **counts** in total C, not zero |
| Every client caches full `x` | m + epoch | same coordinate label or m-bit delta | changing x still requires notifying which update occurred, unless clients can read trusted state elsewhere |
| Individual per-subscriber update bit | 1 output bit + epoch | h bits aggregate across unicast | each recipient receives only its one parity-change bit; h delivery channels; authenticators separately priced |
| Trusted authenticated online owner broadcast | 1 output bit + trusted epoch + key/root | at least information-layer `b^*` | MAC/signature/epoch/authorization and replay prevention cost `lambda + O(log H)` payload per tick **for typical constructions**, not a universal lower bound or completed cryptographic security proof |

**Crucial adversary distinction:** if an adversarial server can forge owner updates, `b^*` provides NO integrity. Authenticated receipts, owner-only signatures/MAC, key rotation, missed epochs and server-equivocated history require a separate security experiment. If independent subscribers do not share a trusted genesis and sender identity, they can accept *different signed histories* from a malicious or double-signing owner; cross-subscriber consistency needs gossip/quorum/shared log and separately charged communication. A no-communication upper bound is only possible when **the complete update label/information is already present on a free external channel or each subscriber directly gets trusted state**; those mechanisms cannot be silently discarded from resource accounting.

## 6. Prior art: the exact right distinction for distributed proofs

This result is **not** a new "broadcast vs verification" theorem.

- **Patt-Shamir–Perry (TCS 2022), DOI 10.1016/j.tcs.2022.05.006**: proof-labeling schemes under broadcast, unicast and bounded number of distinct messages per node. Some predicates incur tight message/label size tradeoffs. Their network-local verification and maximum outdegree are **not** identical to our trusted publisher synchronously sending source deltas to subscribers; a transfer needs a model-reduction.
- **Local Verification of Global Proofs (DISC 2018), DOI 10.4230/LIPIcs.DISC.2018.25**: compares a shared global certificate with per-node local proof-labels and proves separations based on distributed verification. Global proof size does **not** directly bound authenticated multicast updates, but stops first-ever shared-vs-local-certificate headlines.
- **Explicit Space-Time Tradeoffs for Proof Labeling Schemes in Graphs with Small Separators (OPODIS 2021), DOI 10.4230/LIPIcs.OPODIS.2021.21**: published separator/verification-round/certificate tradeoffs; our communication-only quotient theorem has no separator or PLS lower-bound originality.
- **Emek–Gil (DISC 2020), DOI 10.4230/LIPIcs.DISC.2020.20**: approximate proof-labeling schemes, different approximation/soundness condition; source reviewed for model barriers but not automatically imported as same task. Classical local broadcast and proof-labeling scheme literature must not be conflated with malicious server computational soundness.
- **Already indexed:** LIT-068 model-generic UpBARG IVC (ITCS 2026), LIT-156/157/158 memory checking, LIT-159 VC proof refresh, LIT-072 cell-probe proof barrier, LIT-201 FSS/data-structure reduction. None supplies an unconditional lower bound on **our** authenticated multi-subscriber `C_total + Q_read + G_prover` tuple without additional formal reduction.

See [typed primary-source metadata](UCT-005-G2-B2-SOURCES.json). Source-paper verification tier is publisher theorem/abstract evidence; proofs are **not** independently reproduced.

## 7. Decision and next admissible mathematical work

**G2-B2 ACCEPT** restricted elementary exact information broadcast counting + finite tests + source-import inventory. **STOP_AS_ROOT**: no general original nonfactorizing theorem, no cryptographic authenticated data structure theorem and no product of independently published bounds.

Potential **G2-B3** (separate hypothesis, freeze before work): signed incremental broadcasts to intermittently disconnected subscribers with bounded catch-up size, bounded persistent memory and a malicious relay, *where a client must verify exactly-once ordered updates and current derived output without fetching all missed source deltas*. Distinguish total information communicated since last receipt from cryptographic witness cost; compare signed logs, Merkle checkpoints, vector commitments, IVC and accumulator frequency **under the same threat model**. Prove a quantitative bound stronger than known same-model communication/indexing and cryptographic authenticated stream literature, or STOP. Never declare novelty from replay-counter tests. UCT-005 root #105 stays **OPEN_UNPROVED**.
