# DAG-002 G2-B2-C2-B1 — common-source disk lazy and bitmap comparators

**Owner:** issue #339. **Dependency:** standalone file store PR #341; this slice is stacked on its branch and must not merge first.

**Scientific status:** EXACT_FINITE_DAG_REACHABILITY / REAL_OS_FILE_IO / PAID_DIRECTORY_AND_PAGE_LRU / NO_BLOCK_DEVICE_METRICS / NO_FULL_SEA_COMPARISON / NO_NEW_THEOREM.

## Identical update and query model

Both candidate indexes use APPEND_SINK only: append one new vertex n with an ordered subset of old parents, with no old-old edge modifications. Reachability is reflexive. Both serialize and retain the same immutable parent record (u16 count plus u32 old parent IDs), charge its data page writes and directory lookup/writes, and maintain an identical mutable publication manifest (magic, version, method ID, fixed horizon, published vertex count). Manifest replacement adds another on-disk directory version; no physical reclamation or WAL.

- Disk lazy adjacency: query a published source/target pair by reverse DFS, loading each old parent row through the charged FilePageStore directory and data pages. No retained Python parent adjacency table.
- Disk ancestor bitmap: on update, read every parent ancestor bitmap through the charged store, OR into the current inclusive bitset, then write a fixed-horizon bitmap record. Query reads only the published target's bitmap after the charged manifest lookup. No in-process historical bitmap array or unbilled predecessor oracle.

All reads and writes use the same backing store with a disk-linear directory, SHA-256 record corruption validation and shared bounded data/directory LRU. Manifest byte format is versioned and method/horizon-specific so a program cannot reopen the wrong index by accident. Both account parent-incidence command bits separately; the exact serialized parent-row bytes are also charged.

**Explicit exclusions:** Python interpreter RSS, system page cache, filesystem metadata-call costs, directory fsync, torn pages, allocator, crash-durable generations and external-memory lower-bound proof. Reported pread/pwrite page counts are userspace-issued operating-system calls, not proof of device I/O or SSD latency. A user-controlled cache_pages limit caps only the FilePageStore *application page cache*, not total process or kernel memory.

## Evidence and falsifiers

Six stdlib tests cover all 64 topologically ordered four-node DAGs, both representations and page sizes P=16,64; every prefix query compared with independent backwards DFS; restart from actual byte files with no persistent graph object; old parent row immutability; invalid parent commands and unpublished rows; corrupt/mismatched manifest; cache capacity; 5 repeated queries with cold (0 pages) vs large (256 pages) application page cache; and explicitly priced directory scan counters.

    python -m unittest discover -s research -p 'test_dag002_g2c2_disk_reach.py' -v

Run focused and **full Research CI** on exact stacked PR SHA with GitHub-hosted runners. Do not merge until parent #341 is reviewed and accepted, the branch is reconciled to current main without stray parent changes, and the exact-head full checks pass.

## Next C2-B2

Integrate G2-B2-C1's Felsner+Power updater from #338 on exactly this FilePageStore and manifest protocol, with explicit rank support, F_i family directory reads, old label reads, bounded application page cache, counted directory probes and identical parent rows. Then source-fair cross-candidate profiling with bitmap/lazy, and incorporate Felsner-record / simple-chain only under byte-identical serialization. Maintain STOP_THEOREM_NOVELTY until all update and query resource assumptions are source equivalent to primary references and classical information bounds are exhausted.
