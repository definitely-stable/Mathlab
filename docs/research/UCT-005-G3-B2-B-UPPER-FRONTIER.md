# UCT-005 G3-B2-B — three F1 upper constructions and novelty gate

**Date:** 2026-10-09. Parent [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105), [G3-B2 #178](https://github.com/definitely-stable/Mathlab/issues/178). Follows [G3-B2-A F0/F1 proof](UCT-005-G3-B2-A-FRESHNESS-INDISTINGUISHABILITY.md).

**Scientific status:** THREE_F1_UPPER_CONSTRUCTIONS / CONDITIONAL_HASH_SECURITY / FINITE_INDEPENDENT_ORACLES / BYTE_EXACT_REFERENCE_WIRE / NO_PHYSICAL_PAGE_MODEL / NO_NEW_ASYMPTOTIC_LOWER_BOUND / UCT005_ROOT_OPEN / NO_RUST.

## 1. Frozen task and assumptions

One honest sequential writer maintains n nonempty mutable binary bits. SET(i,b) commits a new strictly increasing uint64 epoch even if it changes no bit. RANGE_PARITY(a,b) returns XOR of an inclusive interval at the current epoch. Independent readers can disconnect and rejoin; a fully Byzantine remote server can hide, replay, reorder or corrupt historical replies and proofs but cannot control trusted clients or the independently trusted anchor. No gossip or reliable author-to-reader update delivery is secretly free.

F1 assumes a trusted, atomically published, globally monotone pair (uint64 epoch, 32-byte digest). Every writer commit publishes 40 raw bytes. Every reader query explicitly performs a one-byte anchor-read request and receives 40 trusted raw response bytes or ABORTs on anchor outage. Each protocol publishes a commitment to its own authenticated representation of the *same logical SET state*. This is a **strong, paid** global anti-rollback primitive, not a construction of consensus. Acceptance refers to the state when the anchor was read; a later commit is outside the freshness claim.

Assume authentic initial state and code bootstrap, uncompromised writer, sound trusted anchor, and domain-separated SHA-256 binding (collision/second-preimage resistance). This reference does not prove cryptographic security, unbounded adversary resistance, signature implementation, crash atomicity or storage durability. If the server withholds required data, safe ABORT is allowed; liveness against an arbitrary withholding attacker is not guaranteed.

## 2. Three concrete implementations under the same F1 trust primitive

| Protocol | Trusted durable client space | Author SET | Rejoining query | Remote response |
| --- | --- | --- | --- | --- |
| **R — full trusted replica with authenticated SET chain** | n bits plus 40-byte epoch/digest | One writer-bit write; one chained SHA; 40-byte anchor publication | Apply and verify all k missed SETs; XOR local interval | Canonically encoded contiguous SET log suffix, k entries; reject missing/altered messages |
| **S — full snapshot with anchored digest** | 40 bytes, no full local row | One bit write, one SHA over **n bytes** in reference; 40-byte publication | Verify n-bit array against anchored hash; XOR requested range | Canonical full-row JSON; old valid versions fail LATEST |
| **T — authenticated range-aggregate tree** | 40 bytes, no full local row | Persistent copy of leaf-to-root path, at most ceil(log2(n))+1 node reads/writes; two SHA per changed node; 40-byte publication | Canonical interval-cover proof; worst-case O(log n) hash/XOR operations | Each frontier subtree publishes its parity and 32-byte payload digest; outside pieces also expose parity |

Implementations: [range-parity tree](../../research/uct005_g3b2b_range_tree.py), [replica and snapshot baselines](../../research/uct005_g3b2b_baselines.py), [independent adversarial tests](../../research/test_uct005_g3b2b_upper.py).

**Same task:** all three answer identical ranges after the same SET history at the same trusted anchor epoch. **Different trade-offs:** R pays the entire n-bit trusted replica and k delivered authenticated changes after offline time. S avoids durable n-bit local data, but retransmits all bits at every successful query and hashes the full state at SET. T stores only the latest trusted root client-side, paying more tree-node work at SET to reduce large-n interval proof transfer.

## 3. Exact proof obligations (upper correctness only)

**R (replica).** The writer commits each epoch,index,bit tuple into a one-way chained commitment. A rejoining reader uses only its stored authentic previous root, processes a contiguous suffix in a scratch copy, and requires both resulting epoch and digest equal the *independent trusted anchor*. Conditioned on hash binding, that establishes the exact author update suffix; applying each SET yields the correct current array, and XOR returns range parity. State/checkpoint replacement is all-or-nothing within this interpreter, not a guaranteed disk transaction. A missing or reordered record fails epoch continuity or the final digest; initial n bits must have been authenticated and paid.

**S (snapshot).** The returned n-bit row hashes to the independently anchored full-state digest, and its epoch equals the anchor. Thus, under conditional hash binding and honest author publication, it is the exact row at the anchor read. XOR is correct. A still-valid old row fails the epoch check, including across no-op commits.

**T (range tree).** Commit a leaf bit through a domain-separated leaf payload and a node commitment binding segment length and parity. At an internal node bind child commitments and their XOR parity. Recursively decompose the *fixed, public* query interval into fully included, excluded and partial nodes. Every terminal proof pair carries parity and 32-byte precommit payload; verifier hashes it to the expected segment commitment. Every split recomputes the parent commitment from both children. Structural induction proves that a reconstructed root equaling the independently anchored digest implies the included parity XOR is correct, conditional on hash binding. Noncanonical shapes and malformed proofs are rejected. The static balanced split visits at most ceil(log2 n)+1 nodes on a SET; an interval frontier visits O(log n) nodes in the worst case. This is an authenticated segment-tree **classical upper construction**, not an original lower bound.

## 4. Typed accounting: scope and exclusions

- **Measured exact serialization:** reference canonical ASCII JSON request and response lengths (all field names, epochs, hexadecimal 32-byte digests included). Trusted anchor uses one-byte reference request opcode and 40 raw response bytes; each author root publication sends 40 raw bytes. This is a specified reference *payload* protocol, not a complete TLS/TCP/HTTP or signing benchmark.
- **Logical storage operations:** R counts log entries delivered; S counts one bit overwritten and all n bytes input to rehash; T counts in-memory tree nodes read/copied and frontier nodes visited. T builds 2n-1 nodes and performs 2(2n-1) setup SHA calls. No physical page writes, WAL, allocation benchmark, fragmentation, RAM residency, reclamation or crash-safe persistence has been measured.
- **Verification:** SHA call counts and XOR counts are separately recorded. A SHA call over an n-byte snapshot is not equal cost to a fixed-size SHA of a tree node. Proof construction, anchor trust, client bootstrap, verifier program, signature/key distribution, software deployment and prover CPU need external charges before any system-wide theorem.
- **Client state:** R has n data bits (ceil(n/8) bytes after packing) + 40 B checkpoint. S/T have 40 B checkpoint, not an uncharged local n-bit replica. Python object header sizes are intentionally excluded.
- **Availability/fork:** old genuine versions may be presented to two disconnected clients, but the independent trusted root detects staleness. Compromised author double-signing or dishonest anchor is outside F1. No liveness under withheld data.

## 5. Exact oracle and negative tests

The tests compare independent direct XOR against R/S/T for every initial binary word, every single SET (including no-op), and every nonempty range for n=2,3,4; stale server prefixes, omitted/reordered/modified SET, tampered tree branches, malformed/noncanonical responses, anchor outage and rollback, and author commit after the trusted anchor read. They assert actual serialized byte lengths, update path operation counts, verifier work and persistent-memory distinctions. Small exhaustive tests **do not** imply unbounded hash binding.

**Important crossover counterexample:** for a 64-bit full snapshot, JSON hex-encoded frontier proofs can exceed the entire snapshot response; for a 4096-bit array and a short range, the tree proof is smaller. Thus the claim that authenticated trees *always* use fewer bytes, without serialization constants and n, is false. A fully trusted replica can have no additional per-query proof after catching up, but paid n trusted bits and all missed SETs. There can be no universal lower bound on remote proof bytes that ignores trusted-state size and delivered updates.

## 6. Source audit and G3-B2-C gate

The F0 freshness barrier is consistent with [SUNDR (OSDI 2004)](https://www.usenix.org/conference/osdi-04/secure-untrusted-data-repository-sundr) and [COP (Information and Computation 2018)](https://doi.org/10.1016/j.ic.2018.03.004). [ADSC-SNARK, JISA 2026](https://doi.org/10.1016/j.jisa.2026.104444) proves stateful authenticated-computation properties under its own assumptions, **not** free independent-reader latest-state publication. Do not treat it or UpBARG/IVC as an implemented same-task comparator without mapping the exact circuit, update authorization, global anchor, setup, prover, verifier and per-reader proof costs. Prior LIT-127, LIT-157/158, LIT-119, ROST G3-A and G3-B1 are explicit assumption-audit barriers. No new canonical literature IDs are assigned while #132/#142 may conflict.

**Next candidate G3-B2-C:** freeze a full vector of trusted space, remote storage, update source reads, physical writes/bytes, query probes, proof traffic, client catch-up receipts, anchor traffic, prover/verifier work, program/setup costs, horizon and security error. Identify one falsifiable formula F_n(resources) >= g(n) that excludes a uniform asymptotic feasible-looking region not already excluded by transferable published results. Check the proposed inequality against all three constructions *before* proof attempts. Otherwise record **STOP_NOVELTY** for this service instead of announcing a classical combination as a novel theorem. Root #105 stays OPEN.
