# UCT-005 G3-B2-A — two-reader latest-state freshness and rollback/fork limits

**Date:** 2026-10-09. Parent [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105), G3 [#164](https://github.com/definitely-stable/Mathlab/issues/164), G3-B2 [#178](https://github.com/definitely-stable/Mathlab/issues/178).

**Research status:** PROVED_CLASSICAL_F0_INDISTINGUISHABILITY / CONDITIONAL_IDEAL_F1_UPPER_CONSTRUCTION / FINITE_EXHAUSTIVE_ORACLES / NO_CRYPTO_PROOF / NO_ORIGINAL_ROOT_THEOREM / NO_RUST.

## 1. Frozen natural online task and four distinct guarantees

An honest single sequential writer maintains x in {0,1}^n. SET(i,b) overwrites one bit, and creates a fresh numbered committed epoch even for a no-op. RANGE_PARITY(a,b) is XOR of the inclusive interval, 0<=a<=b<n. Two independent readers can disconnect and miss arbitrarily many writer commits; remote storage may withhold, replay, reorder or tamper with replies, but cannot mint a genuine writer attestation. A signed full-state receipt contains (epoch, parent seal, all n state bits, seal). The author signs exactly one successor per epoch, and a sealed receipt is authenticated as a complete immutable tuple.

The four properties MUST remain separate: (A) receipt was issued by author, (B) its chain descends from a reader's durable checkpoint, (C) it reflects the latest globally committed epoch at query linearization, and (D) it is available on request. A server can satisfy A and B while violating C by hiding newer genuine updates. D is unavailable against an unrestricted withholding adversary.

The verifier in the finite oracle uses a SYMBOLIC pre-issued-receipt predicate for signature authentication, not actual public-key cryptography. It exposes only whether a particular receipt is valid, not the latest issued epoch or the bit vector of an undisclosed receipt. That idealized primitive is a model assumption, not a proof of cryptographic unforgeability. The client durably saves only (epoch,seal) and public n/program constants, NOT the entire signed data vector. The reference tests assert its actual in-memory checkpoint has no bit field.

## 2. Two explicitly different reader models

F0 (no independent freshness channel): a reader begins with the authentic genesis checkpoint and learns updates solely from untrusted server messages. There is NO trusted bulletin, author push, direct peer gossip, global epoch clock, offline reliable receipt distribution, or other state-dependent side channel. The reader can verify a signed historical snapshot (AS_OF) but generally cannot certify the answer is LATEST.

F1 (trusted, paid root publication): the honest author publishes the latest (epoch, seal) pair atomically to a separately trusted monotone anchor after every commit. Before claiming LATEST, the reader performs a trusted anchor read and compares the returned pair to the independently authenticated signed full-state receipt. If the trusted anchor is inaccessible, the reader ABORTS. An anchored accepted result is correct at the anchor-read linearization point; concurrent post-read commits are outside the claim. **The anchor is an explicit powerful assumption, not a free solution to consensus, offline availability or global trust.**

## 3. Main classical negative theorem — latest-state indistinguishability F0-L1

Choose a common initial state x0, an inclusive query interval Q, world W0 with NO newer commits, and world W1 with a legitimate hidden writer update leading to xt with Q(xt) != Q(x0). In both worlds the reader starts with IDENTICAL public parameters and authenticated epoch-0 checkpoint. The Byzantine server supplies the EXACT SAME original signed epoch-0 receipt and identical entire untrusted query transcript in both worlds, and no trusted new-epoch information arrives.

**Theorem F0-L1.** No deterministic reader can simultaneously answer the correct LATEST parity with termination in both worlds. A randomized reader whose coins are independent of world identity and whose two required answers differ has P(correct W0)+P(correct W1)<=1. Hence completeness and latest-correctness probability >=1-epsilon in BOTH worlds demands epsilon>=1/2. Allowing indefinite abort permits safety but does not meet a liveness requirement on W0.

**Proof.** Every incoming bit, setup parameter, previous reliable state and private-coin distribution of the reader are identical in W0 and W1. Its output distribution is therefore identical. The two required correct Boolean values are different, so their output events are disjoint; their probabilities sum to at most 1. This rules out deterministic simultaneous correctness and proves the epsilon threshold. Abortion is a third, incorrect-for-termination outcome. QED.

This proof is **elementary and classical**, not a new global lower bound or authenticated consistency protocol. It is compatible with SUNDR/COP prior art. It is not even a freshness contradiction if the updates leave the particular queried parity unchanged: that case is intentionally excluded. If the reader has a reliable writer push, a trusted monotone publication channel, or paid and correctly updated local replica, the key identical-transcript premise is false. Authenticated historical AS_OF answers and globally LATEST answers are different service contracts.

## 4. Paid symbolic F1 upper point and its exact limits

Writer computes the new full n-bit array, issues one symbolic author-signed full-state receipt and publishes (epoch, seal) to the trusted anchor. Rejoining reader performs a paid anchor read, receives full signed state from server, tests author validity, proves ancestry to its durable checkpoint through issuer-authenticated predecessor links, compares epoch+seal to trusted latest, computes XOR over the authenticated n-bit row and saves just epoch+seal.

**Proposition F1-P1 (conditional).** Under one honest sequential writer, sound ideal authentication, consistent atomically published latest root, and a successful trusted anchor read, each ACCEPT answer is the exact latest committed range parity at that anchor snapshot time. Proof: receipt authentication pins the complete state; descendant check prevents local rollback; equality with independently trusted published current root pins the latest epoch; XOR over the authenticated row yields the correct range query. QED. It does NOT guarantee progress on withheld data or unavailable anchor, protect against compromised author or split-brain publication, nor prove security of actual signatures/Merkle trees/SNARKs.

Reference logical charging (declared fixed parameter widths, NOT measured protocol byte counts):

- Persistent client state: epoch_bits + signature_bits for checkpoint epoch and seal; public n, verifier program and key setup must be charged separately in production.
- Full signed-state receipt transmitted for each query: n + signature_bits + root_bits + 2*epoch_bits logical bits; server reads n state bits to prepare it. This implementation does NOT implement sublinear authenticated range queries.
- Trusted anchor call: 1 call and signature_bits + epoch_bits authenticated response bits per latest query. Author anchor publication: 1 latest-root publication per committed SET.
- Signature verification CPU, writer local refresh, prover time, cryptographic hash strength, consensus and network byte framing, crash durability, OS page rewrites and key distribution remain unmeasured. Illustrative configured signature/root widths are NOT cryptographically proved secure.

## 5. Server prefix hiding versus author equivocation

With an honest single writer the valid signed receipts form one chain. The hostile server can expose distinct authentic PREFIXES to readers A/B, but cannot forge two conflicting AUTHENTIC children for the same parent and epoch. With no anchor, both readers accept their locally consistent old views, yet at least one might be stale for LATEST. Under F1, the older root fails once the true latest epoch/root is independently fetched.

If AUTHOR integrity is deliberately broken by allowing it to double-sign two successor states at the same epoch, two F0 readers can each accept a different authentic branch. A single trusted anchor publishing just one of these roots rejects the unpublished sibling, subject to its own trust assumption. This is a DIFFERENT attack class from server-only prefix hiding; it does not establish Byzantine-writer security.

A tampered state with a recycled seal fails the ideal authenticity predicate; a signed receipt older than a reader's already accepted checkpoint fails the ancestry check even without an anchor. Neither property alone proves global latest-state freshness.

## 6. Independent finite evidence

Implementation: [symbolic reference](../../research/uct005_g3b2a_freshness.py), [independent tests](../../research/test_uct005_g3b2a_freshness.py).

The test suite exhausts every binary initial array for n=2..4, every changed one-step SET, every valid range query, and paired W0/W1 with exactly identical visible inputs. It independently computes the correct parity under both worlds. It then exhausts all SET sequences for (n,d)=(2,3),(3,2),(4,1) including no-op commits; for each pair of independent reader-prefix choices, verifies unanchored AS_OF acceptance versus anchored LATEST acceptance/rejection. It exercises withheld root publication, unavailable trusted anchor, fake signed payload, rollback below checkpoint, and deliberately compromised author double-sign. It explicitly checks the client's trusted checkpoint never retains the n-bit state vector and that all logical receipt/anchor traffic is charged.

These are finite regression oracles, not proof of cryptographic security or scalability. The mathematical proof above is the justification for arbitrary n under its exact assumptions.

## 7. Three upper-baseline candidates for G3-B2-B (not implemented by this PR)

1. Full trusted n-bit client replica, plus authenticated SET receipts delivered reliably to EACH subscriber; pays n trusted bits and full delivery cost, no remote query required. Missing update delivery destroys latest knowledge.
2. The IMPLEMENTED SYMBOLIC signed full snapshot with paid trusted root anchor, O(n) signed response bits per query and charged checkpoint delivery; demonstrates safety given a strong anchor, not efficient proofs.
3. Dynamic authenticated Merkle/augmented range index or state-consistent succinct certificate (ADSC-SNARK), with FULL author update reads/writes, prover work, verification CPU, trusted root publication and wire bytes measured in the SAME security model. **Not yet implemented and no uniform performance or complexity claim**.

A genuinely original UCT-005 G3-B2-B theorem must identify an asymptotic same-task resource vector excluded by its new joint constraint but permitted by the audited strongest already-known bounds; it needs an explicit quantified inequality and an independently checked impossibility proof with honest constructions. An indistinguishability lemma, a product of unrelated classical bounds or a renamed SUNDR/BKV claim is NOT sufficient. If no strict gap survives, mark STOP_NOVELTY for this service and choose another one honestly.

## 8. Original source priority and verification tiers

- [SUNDR: Secure Untrusted Data Repository, Li–Krohn–Mazières–Shasha, OSDI 2004](https://www.usenix.org/conference/osdi-04/secure-untrusted-data-repository-sundr). Established fork consistency and its client-visibility limitation.
- [COP: Verifying the consistency of remote untrusted services with conflict-free operations, Cachin–Ohrimenko, Information and Computation 260, 2018](https://doi.org/10.1016/j.ic.2018.03.004). Honest-server linearizability and malicious-server fork-linearizability; 2013 arXiv 1302.4808 is an earlier version of the SAME research identity.
- [SNARKs for stateful computations on authenticated data, Reinhart–Blass–Annighoefer, JISA 99 (June 2026)](https://doi.org/10.1016/j.jisa.2026.104444). Authenticated, state-consistent iteration; DOES NOT by itself imply independent reader fork prevention. Its 2025 IACR preprint is the same source.
- Existing canonical LIT-127 (locally updatable/decodable codes), LIT-157/LIT-158 (strong memory checking lower bounds), LIT-119 (Ko dynamic cell-probe): MUST compare exact adversary and cost units before transferring.

[Typed primary-source inventory](UCT-005-G3-B2-A-SOURCES.json) pins SUNDR/COP identities and cross-references already known work, without inventing new canonical LIT IDs. Canonical promotion remains coordinated with #142/#147/#154 and concurrent HYP-105 #132 reservation. Source verification here is publisher/institutional abstract and metadata level, NOT an independent reproof of those publications.

**Boundary of this slice:** MODEL_AND_FALSIFIERS_ACCEPTED subject to hosted tests; original nonfactorizing UCT-005 remains OPEN, no production recommendations or generalized cryptographic claims.
