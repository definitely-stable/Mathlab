# UCT-005 D1-B2-C — paid trusted-PIN eager reclaim vs slot scanning

Owner: [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). Concurrent [D1-B2-A #243](https://github.com/definitely-stable/Mathlab/pull/243) addresses tree/log/snapshot partial pricing; this slice compares two complete-snapshot GC algorithms in one PAGE-001 page-slot model. Status: **CLASSICAL RESTRICTED REFERENCE UPPER, NOT A NEW LOWER BOUND. UCT ROOT_OPEN_UNPROVED.**

## Frozen identical service and bytes

One serial honest writer of n bits; every SET including no-op publishes a new epoch; LATEST_RANGE_PARITY, two independently trusted readers, PIN_CURRENT, AS_OF_PINNED, UNPIN and GC. A paid linearizable trusted anchor plus trusted PIN authority serializes all author, PIN and GC transitions. Only PIN_CURRENT is legal: superseded versions cannot be pinned for the first time later. Malicious remote omission yields ABORT, not availability.

PAGE-001 serializes a B=ceil(n/8)-byte packed image and a 48-byte (u64 epoch, u64 image length, 32-byte digest) remote manifest into separately page-aligned extents. Let D=ceil(B/P), M=ceil(48/P), L=D+M. The address of epoch e is public fixed-stride page index e*L, rather than an unpriced hidden version→object index. Each SET writes L full remote page images and the same PAGE-001 SHA, trusted anchor and physical wire bytes as in the scan baseline. Reader queries still read L pages and verify against independent PIN or latest trusted root.

## Two alternatives and their fully explicit different charges

S, scan collector in PAGE-001: leave versions until explicit GC, which probes the manifest region of every epoch e=0..E, including holes, at cost (E+1)*M remote manifest page reads per call. Executing GC after each of H epochs results in M*H*(H+3)/2 scan probes. This is a cost of one reference algorithm, **never a universal lower bound**.

E, new eager collector: after SET(e) is published, the author consults the authoritative PIN registry and deletes the superseded epoch e-1 only if nobody pins it. After UNPIN(reader,epoch), check and delete this exact epoch if no other reader PIN remains and it is no longer latest. This is correct only because the PIN/UNPIN/SET authority is globally serialized and an arbitrary-old PIN operation is **not** supported. No historical slot scans occur.

At any retirement decision with A active PIN records E charges 41*A bytes of trusted PIN-record reads, A*ceil(41/P) trusted page-image reads, A trusted comparisons and a 40-byte trusted latest-root read. When eligible, E invokes one explicit page-deletion API operation for each of L remote pages and charges 8*L addressed control bytes. The server's honest page-delete API reclaims allocated remote slots; this does not establish SSD TRIM, NAND erase, physical compaction, filesystem fsync, crash recovery or network framing costs. A malicious server may refuse deletion, so the resource upper bound describes **honest-server execution**, while Byzantine data integrity and abort follow the separately assumed F1 trusted-root SHA model. Trusted-authority accesses and remote delete commands are distinct axes and **must not be silently treated as zero**. Both use the same 41-byte trusted PIN record and 40-byte trusted anchor.

## Restricted exact invariant and proof

Following each completed serialized public operation, for an honest remote page store:

LiveEpochs = {LatestEpoch} union { e : an active authoritative PIN of epoch e exists }.

Initially only epoch 0 exists. PIN_CURRENT changes only the trusted PIN registry for the already-live latest. A SET creates one new latest and then deletes its previous latest precisely when no PIN keeps that old version alive. UNPIN removes its own token and deletes the referred epoch only if it is now obsolete and has no remaining active PIN. GC does nothing because no unprotected obsolete version remains. There is no operation capable of resurrecting a deleted old epoch. This elementary induction is not a new information-theoretic theorem.

Let K be the number of distinct pinned historical epochs. After any operation E stores exactly (K+1)*L live pages; during SET its transient storage is at most (K_before+2)*L. With no pinned history after each SET, only L live pages remain, peak 2L, while sparse virtual address arithmetic still grows in the epoch counter.

In the shared three-SET witness with one no-op, reader0 pins epoch0 and reader1 pins epoch2: E reaches three live versions {0,2,3} and at most 3L peak pages; S temporarily holds four {0,1,2,3}, peak 4L before GC. E eliminates S's repeated historical manifest scans but incurs trusted PIN record scans and remote page-delete commands. Thus **no unconditional Pareto dominance** has been shown.

## Falsification and scope

Independent finite tests enumerate every initial word for n=1..6 at P in {1,2,64}, exact nonempty ranges and pinned historic answers against independently updated logical states, plus multi-reader same-epoch PIN, replay/tamper/withholding, a no-op SET, invalid operations, sequential late UNPIN, repeated GC, and nine-epoch unpinned histories. A local Python dictionary models existence of sparse pages, not an uncharged lookup directory: page indices derive from public epoch*L and the deletion API is explicitly accounted.

GitHub-hosted focused and main Research CI on exact PR HEAD are required before merge. D1-B2-B physical Merkle/LSM page comparators and all source-to-proof lower-bound transfers remain OPEN.
