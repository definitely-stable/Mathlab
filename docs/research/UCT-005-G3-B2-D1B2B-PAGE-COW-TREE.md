# UCT-005 D1-B2-B — fixed-stride page-image authenticated COW parity tree

**Date:** 2026-10-10 · Parent [#244](https://github.com/definitely-stable/Mathlab/issues/244), [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223), [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105) · Comparators [D1-B2-A #243](https://github.com/definitely-stable/Mathlab/pull/243) and [PAGE-001 #241](https://github.com/definitely-stable/Mathlab/pull/241).

**Scientific state:** FINITE_TWO_READER_PAGE_IMAGE_UPPER / ABSTRACT_MONOTONE_ANCHOR / PAGE_ROUNDING_EXACT_IN_API / AUTHENTICITY_CONDITIONAL / NO_REAL_DURABILITY / NO_NOVEL_LOWER_BOUND / ROOT_OPEN_UNPROVED.

The [reference](../../research/uct005_d1b2b_page_cow.py) is the first separately serialized page-accounted immutable COW tree in this family. All statements concern an **abstract fixed-address page-image storage API**: not POSIX files, fsync, NAND page writes, physical discards, crash consistency, computational security proof or a production library.

## 1. Freeze exact bytes and addresses

A logical binary word has n>=1 bits; fixed complete page size P>=1 **bytes**. Every node record is **122 bytes**, from a 90-byte big-endian prefix followed by 32-byte SHA-256 digest:

| Field | Bytes | Grammar |
|---|---:|---|
| magic | 4 | ASCII UCTN |
| kind | 1 | 0=leaf, 1=internal |
| span | 4 | unsigned span length |
| parity | 1 | exactly 0 or 1 |
| left node ID | 8 | unsigned physical fixed-stride node ID; 0 for leaf |
| right node ID | 8 | same |
| left digest | 32 | SHA-256 of child node record; zero for leaf |
| right digest | 32 | same |
| node digest | 32 | SHA256(domain-separator || first 90 bytes) |

The 90-byte input binds kind, aggregate parity, length, children **addresses** and their hashes. This is not a collision-resistant *proof* on its own: it assumes the collision resistance of SHA256 and an honest serialized author. Node ID 1 occupies the first node extent; ID i is at page offset (i-1)*ceil(122/P) in a distinct node namespace. IDs only increase. A Python dictionary of IDs represents sparse physical pages; it is not free index state or a trusted cached replica.

Each epoch has a remote **48-byte** manifest, u64 epoch || u64 root node ID || 32-byte root digest. Epoch e's public address is page offset e*ceil(48/P) in a separate root namespace. The separately trusted monotone root is u64 epoch || 32-byte root digest (**40 bytes**). Neither node nor root page can be returned without its full-page fetch being counted. The root digest also authenticates physical pointers because pointer fields are included in the node hash. A new root slot is written on *every* SET, including no-op epochs.

The allocated/deleted bitmap is explicitly persisted and charged: ceil(ceil((next_node_id + issued_epoch + 1)/8)/P) full pages at each state. Setup, each SET and each GC charge rewriting these bitmap pages, as well as padding and upload bytes. Freed node/root physical page IDs are not recycled. Peak remote allocation S includes live nodes, live root slots and metadata bitmap pages. GC probes *every* issued node ID and epoch slot, including holes: a sparse Python map does not make directory reads free.

## 2. Operations and F1 contract

- **SET(i,b):** fetch and authenticate latest 48-byte root slot against paid trusted anchor, read each existing COW path node, emit a newly serialized immutable node along that path, then a new epoch root slot; publish separate paid anchor. Author does **not** persist a trusted n-bit replica or the full history. Each page read/write, SHA, source bit-change, padded upload and bitmap write is charged. A failed/withheld SET can leave abandoned allocated nodes without publication; GC reclaims unreachable nodes.
- **LATEST_RANGE_PARITY([l,r)):** first reads a 40-byte monotone trusted anchor (including paid control request), then fetches and authenticates the current 48-byte root slot, the canonical ordered Merkle frontier records, verifies the root binding and XOR parity. This claim is linearized at the anchor read, not at response delivery. Remote transport charges 24 request bytes and exactly 48+122*f response bytes, where f is the frontier record count; remote page reads are ceil(48/P)+f*ceil(122/P).
- **PIN_CURRENT(reader):** ideal trusted authority atomically registers the current root before any GC decision, stores the separate 41-byte reader/epoch/digest PIN record, and supplies reader-local 40-byte trusted PIN state. Readers 0 and 1 may be offline.
- **AS_OF_PINNED(reader,e,[l,r)):** uses that reader's prior PIN digest, fetches the paid remote root slot and canonical proof, but needs no new LATEST anchor read. Multiple reader PIN records and authority duplicates contribute to trusted-state s. A revoked or missing PIN must ABORT.
- **UNPIN(reader,e):** serialized trusted authority revocation, charged as ceil(41/P) trusted-authority page writes. Not a remote page write.
- **GC:** collect **all** current and authority-pinned roots, authenticate every live manifest and node, then determine reachability; probe all public node/root slots, free only unreachable immutable pages, charge complete bitmap writes and logical page frees. A stale expected serialization generation aborts before mutation. GC page frees are **logical API reclamation only**, not SSD discard guarantees. The trusted authority is a separately billed ideal assumption; the code does not implement consensus or a true concurrent CAS.

## 3. Adversarial and finite proof obligations

The [independent oracle tests](../../research/test_uct005_d1b2b_page_cow.py) exercise all 2^n initial words for n=1..6, both independent readers, no-op SET, all nonempty intervals, latest and AS_OF at two retained epochs, mark/sweep after each UNPIN, exact P=1/2/64/4096 page record rounding, raw wire truncation and mutation, forged/stale root manifests, old/latest replay, missing nodes, malformed/reordered/trailing proofs, authority unavailability and stale collector generation.

An accepted parity is conditioned on the independently authenticated latest or PIN root; server omissions and tampering must fail closed. The finite oracle does **not** establish real computational security for SHA-256, adversarial liveness, physical crash safety, atomic reader PIN synchronization across processes or a universal asymptotic lower bound. The abstract bitmap/allocator and stable page addresses are **explicit layout assumptions**. A production implementation would additionally need atomic publication and page-durability ordering, multi-process fences, free-space journaling, signatures/transport, bounded address space and a crash recovery proof.

## 4. Comparison boundary and next gate

The PAGE-001 full-snapshot construction is already a page-conserving F1 upper comparator. This COW tree now provides a second **page-rounded** upper point: for a SET it allocates at most ceil(log2 n)+1 nodes plus one root slot and bitmap pages, while a snapshot replaces the entire packed logical word plus manifest each epoch. The page count does *not* imply a full strict Pareto improvement, because the tree has different trusted setup, root/bitmap, verifier work, proof bytes, garbage collection and persistent metadata costs. For small n and small P a snapshot may be strictly cheaper on multiple coordinates. Identical T/setup, author state, anchor/authority and complete GC cost accounting is a prerequisite for declaring dominance.

**D1-B2-C / issue #245** studies alternative epoch-scan versus eager reclaim. D1-B2-D should consolidate these upper costs into a shared vector without misclassifying bitmap page *rewrites* as measured SSD write amplification. D1-B3 may only state a conjectural joint H1+H2 lower bound after complete source audit and upper-frontier falsification.

**UCT-005 root remains OPEN_UNPROVED.**
