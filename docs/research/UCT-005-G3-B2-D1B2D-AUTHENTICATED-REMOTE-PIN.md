# UCT-005 D1-B2-D — trusted PIN capacity and authenticated remote bitmap

Owner [#252](https://github.com/definitely-stable/Mathlab/issues/252) and [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). Depends on accepted PAGE-001 #241 and D1-B2-C #245; does not overlap D1-B2-B tree #248. **CLASSICAL RESTRICTED CAPACITY + CONDITIONAL UPPER; ROOT_OPEN_UNPROVED.**

## Classical exact PIN information lemma (not novel)

Before each of H sequential distinct *no-op SET epochs*, reader0 may either PIN_CURRENT or skip PIN; no UNPIN is needed until after the horizon. Thus all 2^H subsets of the H historical epochs are attainable with identical latest logical bits and epoch H. An exact deterministic GC authority that must identify the full active PIN subset, cannot read remote state, cannot query any client or free external helper, and has no other state-dependent input, needs at least H trusted bits: otherwise two distinguishable subsets share the same representation by pigeonhole. This is a standard observability-counting lemma, not a new F1 lower bound. Reader-owned PIN roots, remote metadata and communication are all permitted but **must be charged** in F1. A constant 256-bit SHA digest is NOT an injective information-theoretic representation of arbitrary H-bit states; its collision-resistance guarantee is only computational and assumption-dependent.

## Authenticated remote membership upper construction

Fix two readers and public epoch capacity C; the bounded registry stores 2C membership bits, indexed 2e+r for epoch e and reader r in {0,1}, packed as ceil(2C/8) remote bytes. Its full remote page charge is

\[
P_{\rm bitmap}=\left\lceil {\lceil 2C/8\rceil\over P} \right\rceil.
\]

The authoritative PIN controller retains only a 40-byte trusted pair (u64 bitmap generation and SHA256 digest of domain-separated bitmap), *no hidden trusted PIN map*. Every PIN_CURRENT or UNPIN first fetches/authenticates the full bitmap and then writes the full updated bitmap, computes its new SHA and publishes its next trusted digest/generation. A SET authenticates the bitmap before modifying the state and tests the two already-authenticated bits for its superseded epoch. Both clients independently keep their trusted historical 40-byte epoch/root tokens, which remain part of total trusted s. The remote PIN bitmap occupies physical page addresses 0..P_bitmap-1; PAGE-001 data version e begins at **P_bitmap + e*L** rather than at e*L, preventing a hidden physical overlap. Both addresses are computed from public C,n,P without a free directory. Fixed-size C excludes free resizing.

Data remains the PAGE-001 snapshot: B=ceil(n/8) packed data bytes plus 48-byte manifest, on L=ceil(B/P)+ceil(48/P) aligned full-page remote slots, publicly located at epoch*L. Historical live versions are reclaimed by one 8-byte logical DROP_PAGE request per L remote pages. These commands are explicitly paid and assume an honest remote deletion API; this is not real SSD GC, NAND operations, fsync durability or Byzantine server availability. A malicious remote bitmap tamper, replay or omission must ABORT rather than be trusted.

The service assumes atomic publication of remote bitmap and its trusted controller root, and a separate globally monotone latest data anchor. This *ideal linearized transaction* is not implemented as a crash-safe write protocol. Reads and writes of remote bitmap pages, wire bytes, digest hashing and trusted-root publications are separate ledgers. Extra authenticity checks performed only by test/invariant diagnostics are counted separately under bitmap_audit_* rather than being misreported as part of the online workload. Omitted network framing/authorization and true physical durability are unpriced **unknown axes**, never zero.

## Restricted live-set invariant

After each completed serialized operation on an honest remote page store:

LiveEpochs = {current latest epoch} union {epochs with either authenticated reader PIN bit set}.

Proof by induction: initially latest epoch0 only; PIN_CURRENT changes bitmap for already live latest; SET publishes next latest, then retires former latest iff neither reader bit is set; UNPIN clears its own bit and retires its non-latest epoch iff the other bit is zero; GC is vacuous. No public operation can PIN a previously superseded version for the first time. A strong/old-epoch PIN API would invalidate this proof. The invariant is an elementary algorithm property, NOT a novel global resource lower bound.

## Three distinct same-service upper baselines

S = PAGE-001 version-history scanner; O(H) per-GC remote manifest probes in the chosen full-history scan implementation. E = #245 eager reclaimer with paid trusted active PIN-entry scans (41 bytes per record and ceil(41/P) trusted pages) and remote DROP_PAGE calls. R = authenticated remote bitmap, which reduces *central persistent trusted PIN-membership state* to 40 bytes but pays O(C/P) remote pages per read and full bitmap rewrite per PIN/UNPIN, plus hashing and frequent trusted root updates. The two reader clients can still retain O(H) historical roots, so **total trusted state is not constant**. No unconditional Pareto dominance or novel joint theorem follows.

## Finite acceptance/STOP

The independent tests enumerate 2^H historical PIN subsets for H<=8, identical F1 histories across E/R for every initial word n<=5 and P=1,2,64, all exact range parity answers and two distinct AS_OF PIN roots; two clients pinning the *same* genesis; bitmap bytes/pages at capacities C=2,5,8,17; tamper/replay/withhold ABORT; and capacity/invalid operations. GitHub-hosted exact-head focused and Research CI required. These are finite sanity gates only.

Root #105 remains OPEN_UNPROVED. Next D1-B2-E research must freeze a common **total** resource vector including all client roots, authority CPU, remote pages, proof and control bytes and source-level comparisons with authenticated dictionaries and memory checking. A classical H-bit capacity bound does not fulfill that novelty gate.
