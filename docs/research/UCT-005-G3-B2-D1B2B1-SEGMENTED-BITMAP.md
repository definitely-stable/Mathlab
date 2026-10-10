# UCT-005 D1-B2-B1 — segmented allocation bitmap: exact page point updates

**2026-10-10** · [Issue #254](https://github.com/definitely-stable/Mathlab/issues/254) · parent [#244](https://github.com/definitely-stable/Mathlab/issues/244), stacked on **unmerged** [PR #248](https://github.com/definitely-stable/Mathlab/pull/248). Scientific classification: \`CONDITIONAL_PAGE_IMAGE_UPPER_WITH_BOUNDED_ALLOCATOR_WRITES_NOT_PARETO_THEOREM\`. UCT-005 root: **OPEN_UNPROVED**.

This implementation is separate from D1-B2-D's authenticated **reader PIN bitmap**. This file describes the **physical allocation occupancy bitmap of remote COW nodes and historical epoch slots**, not a trusted source of PIN membership or Byzantine availability.

## Model and frozen page grammar

Let \`P >= 1\` be the complete remote page size in bytes and \`B = 8P\` occupancy bits per segment. There are two disjoint, fixed-address bitmap namespaces:

- Node ID \`i >= 1\`: index \`i-1\`, page \`floor((i-1)/B)\`, bit \`(i-1) mod B\`. Node data itself still uses the original immutable 122-byte record at public node data page offset \`(i-1)*ceil(122/P)\`.
- Epoch \`e >= 0\`: index \`e\`, page \`floor(e/B)\`, bit \`e mod B\`. The authenticated 48-byte remote epoch/root manifest remains at page offset \`e*ceil(48/P)\` in its own data namespace.

Every allocated bitmap segment is a physically persisted **exactly P-byte image** with zeros in unused padding bits. Addressable missing segments mean a full P-byte zero-page read, **counted** as an attempted remote page read. Old all-zero segments remain allocated, and their live page count contributes to \`S\`; their page IDs are not silently reclaimed. There is no free B-tree/hashmap to map IDs to pages: integer division computes the address. The reference's Python dictionaries only simulate remote addressed pages, not trusted metadata. Monotone \`next_id\`, current epoch, independent anchor and PIN records remain in the separately charged authority state. The existing COW record digest, remote root-slot commitment, and two-reader PIN semantics are unchanged.

## SET: true distinct-page writes, no global bitmap copy

For \`SET(i,b)\`, the author calculates its COW path depth \`d\` from public \`n,i\`. A COW rewrite creates exactly d contiguous, never-reused node IDs, followed by one new epoch slot. The author reads each *distinct* bitmap page intersecting the new node IDs plus the epoch page, charges P padded bytes and 9 request bytes (one namespace byte and one u64 segment address). The image contents are checked for malformed size and nonzero future/padding bits. Each changed page is serialized **once** after all new bits have been set. There is no scan/rewrite of previous bitmap segments or cached bit index on the update path.

The exact upper bound on distinct bitmap pages written by one successful \`SET\` is

\[
W_{\rm bitmap}^{\rm segmented}
\leq \left\lceil \frac{d}{8P}\right\rceil+2,
\qquad d \leq \lceil\log_2 n\rceil+1 .
\]

The slack accommodates a node path crossing a preexisting segment boundary and the independent root segment. Every touched page is both read and written once; remote requests and full-page response/upload bytes are charged. The old full-rewrite allocator paid at least \`ceil(ceil(n/8)/P)\` *bitmap* page writes on every SET, independently of COW path length. The new bound applies **only to the allocation bitmap portion**, not to full update cost \`U_w\`: COW path nodes, the root manifest, reader/author trusted messages, CPU, and durability remain additional charges.

A finite counterexample to the earlier global-rewrite model is \`n=257,P=1\`: previous bitmap writes >=65 pages per SET, while the segmented bitmap touches at most four pages. At this small n and P, its **complete** COW node write cost still exceeds the packed snapshot write; do not promote this result to universal Pareto domination.

## GC: charge scan, write only changed segments

Garbage collection retains independently authenticated latest and all atomic-PIN roots, recursively verifies reachable records, then scans all issued COW node/root page slots including holes (the parent COW reference charges this explicitly). It reads every allocated bitmap segment, validating byte width and zero-reserved padding. **Only segments whose occupancy bits change after reclamation are page-rounded rewritten.** Collector CPU is charged as the number of occupancy bits scanned. A mutation to ordinary advisory occupancy bits cannot cause a trusted-root-reachable page to be reclaimed: bitmap membership is never the proof of reachability, and the collector reconstructs segment bits from authenticated roots and the actual accounted page images. A missing/truncated or nonzero-reserved bitmap segment aborts, without declaring data corruption physically recovered.

All changes occur in a sequential, idealized page-image simulation. It does **not** implement crash-safe atomic page-group updates, fsync/write barriers, signed remote roots, byzantine live availability, authenticated allocator bitmap roots, concurrent multi-process GC, real SSD discard or cryptographic reduction. Failures/ABORT cost must not be read as liveness proofs.

## Acceptance and typed scientific status

The independent finite oracle checks all \`2^n\` initial words for \`1<=n<=6\`, two independent historical PINs at epochs 0/2, a no-op and two toggling SETs, every nonempty interval, GC before/after UNPIN and adversarial bitmap damage. P=1/2/8/64/4096 checks exact page grammar, boundary crossing, padded transport and the bound above. It compares accepted answers with the predecessor COW and the existing PAGE-001 snapshot. It also verifies that n=257/P=1 improves only the *bitmap* coordinate and **does not prove a strict whole-vector Pareto improvement**. The predecessor [#248](https://github.com/definitely-stable/Mathlab/pull/248) must be accepted and merged first; this branch is intentionally stacked, not an independent alternative replacement.

**Stop gate:** No H1+H2 joint lower bound follows from this engineering upper comparator. Root remains \`OPEN_UNPROVED\`.
