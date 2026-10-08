# TOM-003 D2 — authenticated overwrite, total-cost and novelty gate

**2026-10-08 · Issue #53 · parent #15 · research decision: STOP-BROAD-MERKLE (pending CI).**

This is a *red-team comparison*, NOT a proposed new cryptographic primitive,
a theorem of originality, or a Rust release. Previous D1 issue #49 derived
the classical essential-input state lower bound for no-probe arbitrary
overwrites. Here we deliberately give the verifier a **different trust model**
to see whether a claimed compact threshold-update certificate remains useful
after charging its trust boundary and proof costs.

## 1. Nearest PRIMARY sources and model mismatches

1. **Ethereum consensus-specs SSZ Merkle multiproofs**:
   https://github.com/ethereum/consensus-specs/blob/master/ssz/merkle-proofs.md
   gives generalized-index helper-node selection and reconstructing
   a tree root from selected leaves; the computed root can be recalculated
   for updated leaves. Thus "compact batch overwrite proofs" and shared
   proof-sibling elimination are ALREADY KNOWN. We implement a pinned
   *power-of-two Boolean tree subset* of these ideas, not a new multiproof.
2. **Transparency.dev compact ranges**:
   https://github.com/transparency-dev/merkle/blob/main/docs/compact_ranges.md
   explicitly includes updatable proofs, incremental range merging,
   and witness-state reuse for append-only log trees. Its append-only
   history-tree model is NOT the same as arbitrary overwrite, but
   refutes any broad "first to reuse authenticated state across versions"
   originality claim.
3. **RFC 9162 Certificate Transparency 2.0**, section 2.1:
   https://www.rfc-editor.org/rfc/rfc9162.html
   explicitly defines domain-separated leaf hash 0x00 and internal
   hash 0x01, and discusses second preimage security. Our domain
   separation follows this precedent; our *leaf includes fixed index*
   and the tree is fixed power-of-two, so it is not wire compatible.
4. **TOM-003 D1 source proof**:
   TOM-003-TRUST-BOUNDARY-PROTOCOL.md. Without access to old bits
   or authenticated witnesses, the finite-state lower bound is e bits
   for arbitrary overwrites. Authenticated Merkle proof bytes AND root
   verification are additional information, so the two bounds are
   not contradictory.

The 2026 authenticated update/cached proof literature is broader
than these three reviewed protocols. This is a **bounded prior-art
audit**, not a comprehensive theorem-by-theorem global novelty search.

## 2. Frozen exact task/trust domain

- Leaf count n=2^h, h>=1. Every leaf is an indexed Boolean value.
  An initialization authority certifies a SHA-256 old Merkle root
  **and** an exact count of ones. Root alone does NOT bind the count.
- Verifier retains the trusted root (256 bits) and exact count
  (ceil(log2(n+1)) bits), and receives k distinct overwrite triples
  (index, claimed_old, new) and the minimal required sibling hashes.
- For all claimed old values the verifier reconstructs a root and
  rejects unless it equals the trusted old root; then computes the
  new root, updates the verified count, and computes
  "no effect" for a named threshold f=1[count>=threshold].
- New root is computed from the old authenticated proof; it need
  not equal the old root. The verifier then MUST persist the **pair**
  (new root, new count) atomically and bind subsequent proofs to it.
  Crash durability, rollback protection, signatures, fork handling,
  adversarial proof cache consistency and multi-writer concurrency
  are outside the D2 experimental model.
- Security is **computational** under a suitable cryptographic
  hash binding assumption and trusted setup. SHA-256 collision
  resistance is NOT exact mathematical injectivity. Model U in D1
  is information-theoretic; do not conflate the two.

## 3. Actual accounting; no free "small summary"

For h=ceil(log2 n), batch index-set I with |I|=k, let H(I)
be the exact SSZ-style complement/helper frontier. The following
are distinguishable resources, not a single "optimal" number:

| Scheme | Retained at verifier | Batch payload and verification | What the claim does NOT cover |
| --- | --- | --- | --- |
| Full trusted bitmap | n bits (+optional count) | k indexed replacements, k old-value accesses; no remote proof | If the verifier does not own trusted data, it cannot magically authenticate an untrusted remote update |
| Independent Merkle proofs | trusted 256-bit root + externally authenticated count | k*h SHA-256 sibling digests (without path sharing), k old + k new + k indices, roughly two hashes per tree path after leaf hashing | This is a *naive fresh-transmission baseline*, not the best available implementation |
| One batch Merkle multiproof | same trusted root/count | exactly |H(I)| shared sibling digests and the leaf index/old/new fields; old and new root reconstruction work, with overlapping paths combined | No guaranteed advantage over the **existing** SSZ multiproof or a well-maintained authenticated cache |
| Merkle with retained full tree | n-bit trusted bitmap plus potentially (2n-1)*32 bytes digest tree | Can update in place with no sibling-proofs; construction requires n leaves + n-1 internal hashes | Index/state upkeep and retaining the original trusted data must be charged |

Under the *chosen uncompressed fixed-field wire layout*, proof has
32*|H(I)| SHA-256 bytes plus k*(h+2) bits for index, old and new
value. Real wire framing, metadata count, old/new state versions,
security anchors, signatures, and transport are **additional** bytes.
Do not call this a universal information-theoretic minimum.
For one hash, 32 bytes; verified root/count memory is 32 bytes
plus count bits; initialization full Merkle tree construction
touches n leaves and n-1 internal nodes (2n-1 digest calls).

For n=8, I={0,1}, independent proofs need 6 sibling digests
(192 bytes), while the batch helper frontier has 2 (64 bytes).
For I={0,7}, batch uses 4 sibling digests (128 bytes).
This is the ordinary SSZ multiproof advantage and **not** a new
scientific achievement.

These counts are *structural exact*, not Rust benchmarks. Full
memory layout, object allocations, cache lines, retained old-value
checks, and provenance version metadata are still not measured.
If real trust assumptions differ, these comparators cease to be
equivalent and must not be ranked on bytes alone.

## 4. Reproducible independent falsification protocol

- Exhaustively compute all nonempty selected subsets n=2,4,8;
  compare algorithm's helper frontier against independently
  enumerated leaf-to-root path/sibling set subtraction.
- Test all 2^n bitstrings n<=8 against a second recursive SHA-256
  implementation without calling the main tree builder.
- Reconstruct the root for every selected subset in small trees
  using actual helper hashes. Replay sequential update batches,
  verifying root, count, and threshold no-effect against direct state.
- Reject forgery of claimed old bit, any changed helper hash,
  missing/extra helper, duplicate index, mismatched source root,
  wrong value/index domain and **proof from a stale root**.
- Deliberately supply a *false but in-range initial count* to show
  that a valid Merkle root does NOT authenticate the count.
  This is a **negative trust-boundary counterexample**, not
  a security bug in a protocol whose setup promise is honored.
- Run the original G2B exact=10 DRUP checker and all Mathlab
  G0/G1A/HYP/TOM/literature validations unchanged on GH-hosted CI.

## 5. Mathematical and product decision

**Already-known construction / STOP-BROAD:** authenticated old-value
confirmation + verified overwrite + recomputed Merkle root + batched
path-sharing are standard combinations. Any claim that these
alone constitute a new Rust theorem or first proof primitive is
false.

**Genuine narrower research gap not established:** To reopen this
lane, specify an *end-to-end* workload where verifier cannot afford
the full bitmap but has a fixed authenticated state root/count,
and provide measured bytes/CPU plus a novel proof or strict
performance bound **against** SSZ multiproofs, compact-range
updates and the best cached authenticated-state baseline. Account
for sender's tree upkeep, crash consistency, metadata version
binding, stale cache invalidation, signature/fork semantics and
all transmitted bits. A claim that saves 4 classical shared
sibling nodes is insufficient.

**D2 decision after green CI:** STOP_STANDALONE_MERKLE_UPDATE_CRATE.
This is a valid negative research conclusion, independent of the
already accepted GF(5) exact numerical certificate and not
evidence against all possible dynamic-authentication research.

## 6. Artifacts

- research/tom_authenticated_overwrite.py — structural comparator
  and SHA-256 based update/root/count toy simulator.
- research/test_tom_authenticated_overwrite.py — exact independent
  frontier/reference-root, sequential tests and trust-boundary
  attacks.
- This document + frozen issue #53. No background benchmark,
  publication novelty, Lean theorem or Rust code is claimed.
