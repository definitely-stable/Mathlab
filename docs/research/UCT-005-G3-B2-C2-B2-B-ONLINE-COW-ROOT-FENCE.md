# UCT-005 G3-B2-C2-B2-B — Online COW SET with root-fenced admission

**10 October 2026.** Parent [#178](https://github.com/definitely-stable/Mathlab/issues/178); root [#105](https://github.com/definitely-stable/Mathlab/issues/105). Predecessor: [C2-B2-A PIN-fenced disk GC](UCT-005-G3-B2-C2-B2-A-FENCED-DISK-GC.md).

**Scientific classification:** CLASSICAL_FILE_PAGE_COW_AUTHOR_UPPER / IDEAL_ROOT_CAS / ASSUMED_COMPLETE_FSYNC_BARRIERS / STALE_GC_FAIL_CLOSED / NO_REAL_POWERLOSS_PROOF / NO_END_TO_END_BOUNDED_MEMORY / NO_NEW_UCT_LOWER_BOUND / ROOT_OPEN.

## 1. Executable online author

The [online file-COW reference model](../../research/uct005_g3b2c2b2b_online_cow.py) initializes epoch 0 by exporting the older in-memory B2-B binary tree to C2-A's full-page NODE files, and then performs successive online SET updates **without keeping any TreeWriter root object or an in-memory array of all bits**. Each operation authenticates the physical root against an independently trusted 40-byte (epoch,digest) value, reads SHA256-bound path nodes from the file, and appends one immutable full-page NODE per updated leaf or parent. A no-op SET still publishes an epoch. The online updater's logical stack is O(log n), and it uses constant full-page buffers per recursive frame; *not* a claim of bounded total Python RSS.

The root index and new root metadata occupy their own P-byte images. Each root metadata page records epoch, physical root pointer, SHA256 root, and the logical node-page highwater; a separately domain-separated SHA256 checksum detects image modifications. The trusted root bulletin is not inferred from this untrusted metadata. The historic PIN authority B1 holds the authorized root catalog and two independently pinned reader slots, with one serialized honest actor as an explicit assumption.

**Exact write/commit order:**

1. Append all COW NODE page images; barrier on node file
2. Mark each newly allocated node live by complete-page bitmap rewrites; barrier on bitmap file
3. Append one immutable ROOT index image for next epoch; barrier on root file
4. Append the next epoch's canonical metadata and node-page highwater; barrier on metadata file
5. Perform independently trusted monotone root CAS from epoch e to epoch e+1; only then acknowledge

A failure before step 5 leaves the separately trusted root unchanged. Recovery selects only the metadata matching its trusted (epoch,digest), truncates uncommitted NODE, root and metadata tails, and clears unused bitmap slots outside the committed highwater. After successful CAS but before ACK, replay recovers the **new** epoch instead of falsely rolling back to its predecessor. These statements depend on ideal trusted CAS, ordering, complete-image fsync and honest serializable actor premises. Python TemporaryFile cannot be reopened after process termination and does not prove actual drive power-loss behavior.

The new root is added to B1's authenticated historical root catalog on modeled replay; preexisting historical pins remain protected. The program checks SHA256 root and path-node commitments; this does not amount to a formal computational soundness theorem against a Byzantine concurrent store.

## 2. Safety theorem — restricted and classical

Let A_e be the independently trusted root pair (epoch,digest), and assume (A1) immutable published node pages, (A2) binding SHA256 node commitments and authentic ROOT pointer under the trusted digest, (A3) complete and ordered page-image durability barriers for nodes/bitmap/root/metadata, (A4) one atomic monotone trusted root CAS serializing updates and the PIN/root authority, and (A5) replay can reject missing/tampered committed file images.

**Conditional root admission lemma:** If a file-COW SET fails before the trusted root CAS, it cannot publish an epoch newer than A_e, and all previously committed historical NODE images remain immutable. If the CAS succeeds, the new root was assembled from the COW path and has already traversed all modeled data/metadata fsync barriers. Crash after CAS but before ACK recovers A_(e+1) rather than an old root. The lemma follows by induction along the immutable path and linearization at the trusted CAS. It is **not** a real filesystem crash-safety proof or a novel lower bound.

## 3. Resource accounting and independent evidence

[Independent test suite](../../research/test_uct005_g3b2c2b2b_online_cow.py) exhaustively checks binary initial arrays n=1..6, SET indices and all inclusive ranges against separately constructed B2-B versions. It also checks two offline historically pinned epochs across multiple SETs, all pre-CAS write/flush cuts and lost post-CAS ACK, forged old NODE and root-index/metadata images, n=131 bitmap boundary, invalid crash parameter purity, and an explicit stale GC rejection. [Short focused workflow](../../.github/workflows/uct005-c2b2b-fast.yml) uses only GitHub-hosted runners. The full Research workflow is the integration acceptance gate.

The ledger separates NODE/root/meta/bitmap page reads and writes, explicit fsync calls, file-truncate calls and SHA256 calls, 40-byte trusted root publications, historic PIN journal costs and epoch-zero setup pages. Every counted page transfer is a **program file API operation**, not physical SSD traffic. No actual hole punching, compaction, SSD write amplification, directory sync or durable local filename is implemented.

## 4. Composition firewall and next gate

A C2-B2-A DiskFencedGC instance binds its exact initial immutable node count, latest epoch and root digest. This change makes its prepare, publish, recover and query **fail closed** after an online writer increases the forest epoch. It also checks a **process-local in-flight author flag**, so an untrusted pre-publication bitmap tail cannot be swept by the old collector, and it checks the trusted root *epoch* immediately at CAS time (before author ACK/recovery), including no-op updates with an unchanged digest. Independent crash tests exercise crashes at NODE_FLUSH, PRE_PUBLISH and POST_PUBLISH/ACK: only pre-CAS rollback restores admissibility of an old GC instance. A process-local flag is NOT a crash-persistent lease or multi-process serialization protocol. Failing closed is essential: the old collector's bitmap cardinality and signed generation digest can no longer account for freshly appended pages. This is *not* a complete online SET+GC composition. The next slice C2-B2-C must design a monotone generation migration and new PIN/author-root fence preserving already retained epochs, while retaining file-streamed bitmap/queue processing without giant RAM reachability caches.

End-to-end bounded RSS is also still OPEN: the initialization exporter and B1's historical root catalog are O(n+H) in Python. Optimized RANGE_PARITY verification, physical compaction, real power-loss recovery and new same-model hard-query lower bounds are likewise not completed. Standard dynamic partial-sums and memory-checker lower bounds require full hypothesis-preserving reductions rather than mere citation.

**Formal novelty decision:** restricted classical upper + idealized crash safety only; root UCT-005 OPEN_UNPROVED. No production adoption authorized.
