# DAG-002 G2-B2-C2-A — file-backed pages with charged directory

Owner: issue #339, under #336. This independently developed file-store primitive is based on main. It is not yet integrated with the page-billed DAG updater of PR #338; integration is a separate later acceptance gate.

Status: FILE_BACKED_SYSCALL_REFERENCE / PRICED_DIRECTORY_SCANS / BOUNDED_USER_PAGE_CACHE / ACTUAL_RSS_UNBOUNDED / NO_CRASH_SAFETY / NO_NEW_THEOREM.

## On-disk format

The backing directory contains actual files data.bin and directory.bin. The data file is append-only and each image occupies max(1,ceil(bytes/P)) complete application pages. An empty value still occupies one page, and obsolete versions are not reclaimed.

The directory file contains a P-byte v1 header identifying page width and layout magic, followed by fixed-size aligned slots of ceil(120/P)*P bytes. Each slot records fixed tag, canonical UTF-8 key of at most 64 bytes, immutable flag, logical payload size, start data page and SHA-256 digest. Every key lookup scans the on-disk directory in reverse creation order; directory page reads are counted. Deliberately there is NO hidden Python key-to-offset hash index and no free lookup. Manifest overwrites append another directory slot and leave older payload and slot allocated.

All payload loads verify SHA-256 to detect accidental file corruption. This check is not an authenticated remote-store proof.

## Operational resource ledger

Counters named os_pread_directory_pages, os_pread_payload_pages, os_pwrite_directory_pages and os_pwrite_payload_pages measure page-granular calls actually issued via os.pread/os.pwrite. Logical page requests include cache hits; bounded LRU covers both streams under a shared cache_pages capacity. Record cache hits, evictions, maximum resident *data page cache* pages, directory entry probes and byte totals. Eight modeled address bytes per logical page request are separate from actual file transfer payload bytes.

No claim of physical device I/O follows from these calls: the Linux kernel page cache may serve them without an SSD access. No fsync is performed, so there is no durability or atomic publish contract. The Python runtime's actual RSS, system metadata calls, directory/file open cost, page allocator, file system journal and kernel cache are not memory-bounded or fully priced. The use of genuine files does not convert this reference into a production storage engine.

## Acceptance tests

Seven independent stdlib tests run for P=16,64,4096, checking actual byte-accurate files and reopening, persistence of immutable keys and append-only versions of mutable keys, directory miss page counts, newest/oldest directory scan pricing, bounded cache with observed evictions, data tampering detection after reopening, malformed file header, truncated/corrupted directory entries and reporting of excluded physical costs.

Reproduce with command:

    python -m unittest discover -s research -p 'test_dag002_g2c2_file_store.py' -v

Exact-head GitHub-hosted focused workflow and full Research CI must pass before merge. This branch adds only four new files, and never touches existing C1, UCT, catalog or production code.

## Next C2-B

Integrate FilePageStore into the C1 updater, replacing the prior PageImageStore dictionary while preserving the exact byte format and independently checking DAG reachability and restart from actual files. Do not use any hidden page-image or manifest cache. Charge the directory scans and explicit cache read hits/misses. Then implement a fully specified resident RAM model that includes directory decode/state and bounded updater scratch; maintain honest limitations for Python process RSS and kernel page cache. Only then begin the same-codec five-way DAG comparison and G2-C prior-art novelty STOP gate.
