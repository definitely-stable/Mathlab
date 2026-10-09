# UCT-005 G3-B2-C2-A — Disk-backed bounded page-buffer GC

**10 October 2026.** [UCT root #105](https://github.com/definitely-stable/Mathlab/issues/105), [G3-B2 #178](https://github.com/definitely-stable/Mathlab/issues/178), [C1](UCT-005-G3-B2-C1-GC-AND-NOVELTY-GATE.md).

**Status:** DISK_FILE_COLLECTOR / CONSTANT_COLLECTOR_PAGE_BUFFERS / CHARGED_FULL_PAGE_FILE_OPERATIONS / FINITE_PIN_AND_CRASH_CUT_ORACLES / NO_REAL_DURABILITY / NO_ORIGINAL_LOWER_BOUND / ROOT_OPEN.

## 1. Correct the C1 model gap

C1 charged remote bitmap images but materialized entire reachability and resident-page sets as unbounded Python heap objects. Hence its declared one-page LRU did not bound GC workspace. C2-A implements an independent full-page **disk-backed immutable DAG** with a disk FIFO traversal queue, a disk-backed mark bitmap, a disk-backed resident bitmap, an epoch-root file and fixed on-disk reader-pin slots. Each node occupies one whole page, **NOT** the 25-record packed-page construction of C0. Physical update charges from the two layouts must not be conflated.

Algorithmic **collector** workspace is at most SIX P-byte page buffers, where P defaults to 4096 bytes; graph, queue, bitmaps and pin slots grow on temporary files, not as an in-memory array, list, queue or set. The Python process RSS, runtime interpreter, OS file page cache, initial export of an in-memory authenticated B2-B writer forest and query-verifier stack are NOT bounded by this statement. The source explicitly distinguishes these phases.

[Executable disk collector](../../research/uct005_g3b2c2a_disk_gc.py) · [independent finite tests](../../research/test_uct005_g3b2c2a_disk_gc.py).

## 2. Frozen binary layout and exact accounting units

Immutable NODE page: uint64 left/right child IDs, uint32 span, parity byte, two SHA-256 commitments and zero padding. Parent commitments are the same as B2-B; versions share physical node-page IDs across paths. Each epoch gets its own separate P-byte root-index image (root pointer + digest). Each independent reader gets one separate P-byte PIN image (epoch, root pointer, digest), and a pin must match its independently authenticated 40-byte checkpoint. Initially, before the first sweep, historical root pins may be registered; after any reclamation only the latest epoch can receive a NEW pin. This conservative rule prohibits resurrecting an old reclaimed version without a special recovery protocol.

PIN charges one root-index read and a pin image write. RELEASE charges pin image read and rewrite. Neither operation has a durable journal or actual crash safety: PIN/RELEASE and GC must be serialized and freeze the root set. The independent F1 trusted monotone root publication remains separately charged (40 bytes writer publish; one-byte request and 40-byte reader response). Malicious remote withholding => ABORT, not live progress. SHA-256 soundness and the independent trusted authority are assumptions, not security results.

**GC algorithm:** initialize a disk mark file with ceil(N/P) full zero pages for N allocated node-page IDs. Enqueue the latest root and authenticated historical pinned roots into a disk FIFO; every enqueue writes one P-byte queue image and every dequeue reads one P-byte image. For every popped ID, read the mark bitmap page; if unmarked, rewrite it, verify its live-bitmap bit (charged page read), read its NODE image (charged P bytes), and enqueue the two child IDs. Shared nodes are expanded only once. Scan all allocated IDs and compare bitmap images: if live but unmarked, write its live bit to zero as one full P-byte bitmap rewrite and issue one **logical TRIM command**. A concluding disk-resident census reads bitmap pages with full-image read accounting.

The original live bitmap initialization, NODE pages, root-index pages and initial PIN pages are charged separately as SETUP. GC page-read and page-write counters partition the direct temporary-file calls across queue, node, bitmap, root and pin classes; returned read_bytes and write_bytes multiply these page counts by P. Unbounded host caching means these are **file operation counts, not verified physical SSD I/O**. Logical TRIM does not punch holes, erase sectors or return measured filesystem capacity: old bytes remain in the file but are inaccessible through the authenticated reference reader.

## 3. Elementary classical reachability proof, scoped

Let G=(V,E) be the finite immutable exported node DAG and R be the union of the current root and all validated historical PIN root pointers. A disk FIFO enumerates descendants of R. A mark bit prevents repeated expansion; every visited internal node enqueues both child IDs. By induction on path length, every v reachable from R is eventually marked. Conversely every marked v was enqueued from a root or from an already marked parent. Therefore a sweep deleting only still-live unmarked node pages preserves exactly the reachable subgraph. At most N nodes are newly marked and at most 2N+|R| queue records are written. All N-variable structures are **files**, and the collector retains a constant number (at most 6) of P-sized page buffers and fixed-size counters. This is a basic classical graph traversal invariant, NOT a new asymptotic data-structure lower bound.

The collector also validates every visited leaf and internal node against its domain-separated B2-B SHA-256 commitment: it reads both referenced child images, checks segment lengths and XOR parity, recomputes each parent's payload/digest, and compares the newest root digest against the independently trusted checkpoint. This link check occurs **before any live-bitmap deletion**; two SHA calls per newly visited node and two extra full-page child reads per internal node are charged. A modified self-referential root child must abort collection without deleting pages. Soundness remains conditional on SHA-256 binding and an honest, externally authenticated PIN service. This is not a cryptographic security reduction.

The collector rejects stale expected epoch, malformed pointers and mismatching pinned-root credentials. The reference range verifier reconstructs B2-B SHA-256 commitments from leaf upward; it is intentionally O(n) page accesses and O(log n) recursion, **not** an optimized same-task upper bound and **not** covered by the collector workspace guarantee. No online author SET is implemented in this disk arena: the authentic B2-B SET history is exported first, paying setup writes for all nodes and epoch directories. The exported source forest is no longer consulted during collection.

**Injected failure model:** after completing an entire mark phase, interrupt after a specified number of logical bitmap deallocations; with unchanged authentic roots/pins and non-torn page writes, a subsequent fresh mark/sweep preserves all retained versions and finishes reclamation. This tests logical idempotence only. It does **not** imply atomic fsync, torn-write recovery, durable pin registration, crash-safe compaction, writer/GC concurrency or actual disk hardware safety. A logical server-page bitmap may be corrupted or lost in reality. Concurrent pin registration must be fenced before physical deletion; C2-A does not provide that fence.

## 4. Research novelty and model-transfer audit

An explicit counterexample in C1 rejected the false **for-all-query** product W_pages times Q_pages >= ceil(log2(n)), without falsifying the max-over-queries or hard-query distribution results in prior art. C2-A proves no stronger inequality. These existing primary-source barriers remain:

- [LIT-111, Fredman–Saks STOC 1989](https://doi.org/10.1145/73007.73040): lower bounds for dynamic cell-probe partial sums, with prescribed word width and updates.
- [LIT-112, Pătraşcu–Demaine SICOMP 2006](https://doi.org/10.1137/S0097539705447256): dynamic partial sums with word b and bounded update argument delta, amortized tradeoffs and external-memory results. A binary SET operation must not silently inherit the delta proportional-to-word formula.
- [LIT-157, Boyle–Komargodski–Vafa STOC 2024](https://doi.org/10.1145/3618260.3649686): computational memory checking with its own local-storage and Read/Write service model, NOT a theorem about all range-parity protocols with an independently trusted latest-root bulletin.

No new literature IDs are allocated because these are already in the canonical Mathlab catalog. Full theorem-hypothesis transfer remains open. A single convenient full-range query cannot establish a worst-case query lower bound; multiplying unrelated classical theorems is unsound.

## 5. Admission and next gate

**C2-A acceptance:** hosted CI executes disk-file oracle and independent exhaustive small-n tests, two offline historical readers, pin/release, tampering, retained-root verification, GC after simulated interruption, and exact page-image account partition equalities. The report and UCT theorem tree explicitly say **MODEL_SCOPED_CLASSICAL_GC_ONLY**.

**C2-B NEXT:** durable PIN/RELEASE append-only journal, generation-fenced GC atomically published bitmap, fsync crash-cut tests, true bounded-space setup and online author SET, compaction/reuse cost, adversarial retention. Only then examine a falsifiable max-query joint bound strictly beyond applicable published results or issue STOP_NOVELTY for this service. Until then UCT root #105 and #178 stay OPEN; no Rust or production integration.
