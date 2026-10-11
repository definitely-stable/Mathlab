# DAG-002 G2-B2-C2-B2 — Felsner + SEA power index on a real-file store

Parent: issue #339 / #336. This slice is STACKED ON C2-B1 PR #342 (which itself depends on file primitive PR #341). It uses the accepted source-equivalent Felsner/Power construction from PR #331, with the paid historical-state approach of PR #338, but is an independent implementation that reads/writes via FilePageStore only.

Scientific state: SOURCE_EQUIVALENT_FINITE_LOGICAL_COMPARATOR / CHARGED_FILE_PAGE_SYSCALLS_AND_DIRECTORY / BOUNDED_APPLICATION_LRU_ONLY / NO_DEVICE_IO_OR_RSS_THEOREM / NOVELTY_UNPROVED.

## Model, parser, provenance

- APPEND_SINK(v, parents): canonical prior-vertex parents, reflexive directed reachability, no old-old arc edits; independent old-label immutability. Every old ancestor-support bitmap is loaded via a charged key lookup and os.pread page-image read. No predecessor rank, anchor, ancestry, old assignment, chain head or family comes from cached Python persistent graph state.
- The published Felsner family manifest contains version, horizon, power-base, vertex count, each chain's ID and current head, and the disjoint F_i membership; the least admissible family and the exact Felsner exchange are reconstructed from this charged on-disk record.
- SEA 2025 Strategy 2: rank includes vertex itself, maximum-rank parent, largest crossed base-B integer power, first qualifying member of that parent's anchor list. All parent and traversed anchor labels are charged reads.
- Restricted per-chain tops are produced by reading all required historical chain IDs from immutable label pages plus ancestor-support bitmap; update count can be O(n) key/directory scans. Avoid concealing this as O(1).
- New immutable parent record, ancestry support bitmap, and anchor label are written before the mutable publication manifest. Manifest-last is logical order only. Without fsync, journal or atomic directory root, there is NO crash/recovery theorem. Obsolete manifests and their physical pages remain allocated.
- The parent record uses exactly the same u16 count and u32 ID bytes as disk lazy and ancestor-bitmap alternatives from #342. Every candidate uses the same FilePageStore, on-disk linear directory, checksum, complete P-byte page syscall counters and application LRU.

## Cost semantics and limits

Report os_pread_directory_pages, os_pread_payload_pages, os_pwrite_directory_pages, os_pwrite_payload_pages, entire file lengths, cache hits/evictions, address overhead, n(n-1)/2 parent incidence input bits, and conservative modeled scratch bytes. All page images are in *actual files*. Both directory hit and miss scan are charged; no free name-to-file-offset map.

The modeled scratch cap is not a memory-safety proof and DOES NOT cap Python heap objects, interpreter buffers, OS kernel page cache, inode metadata, the process RSS or physical SSD I/O. os.pread/os.pwrite calls may hit kernel cache. No trusted-store signatures, authenticated proofs, persistent snapshots, PIN/GC, allocator cost, fsync durability, concurrency or asynchronous storage correctness is claimed. There is no new information-theoretic lower bound.

## Independent falsifiers

Six tests:
1. All 64 ordered 4-vertex DAGs at 16/64-byte pages; each append replayed independently using Felsner up-growing oracle; all prefix source/target reachability answers compared to a separate backward DFS; exact disk reopen.
2. Same source-row payloads and all Boolean answers vs file lazy and disk ancestor-bitmap on the same six-vertex DAG.
3. Close/reopen then continue append with no retained Python graph/chain arrays.
4. Too-small modeled scratch cap rejects *before writing* any new published or immutable data.
5. Malformed/truncated/duplicate manifest, base/horizon mismatches.
6. Bounded data+directory application LRU, repeated reads and explicit negative flags for unproved crash, kernel cache/RSS and device I/O.

Reproduce after installing the two parent PRs:

    python -m unittest discover -s research -p 'test_dag002_g2c2_disk_power.py' -v

Focus CI on GitHub-hosted runners plus exact-head complete Research CI required for acceptance. DO NOT merge out of order or promote a new theorem by numerical cost ratios.

## Next C2-C and G2-C STOP

1. Build Felsner+Record and Felsner+SimpleChainTop under this **same** codec and directory, then compare full five-way vectors under one frozen trace, P, cache, horizon and source-input accounting.
2. Record actual resident RSS and kernel I/O separately as diagnostics; do not conflate them with application-cache caps or disk media IOPS.
3. Prove prior-art model equivalence and isolate a formal irreducible claim before a new nonfactorizing lower-bound theorem is even proposed. If any hidden resource remains or a reduction to existing schemes resolves the claim, emit STOP_THEOREM_NOVELTY.
