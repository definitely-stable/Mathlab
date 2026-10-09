# INDEX-001 G2-B4-C2 — adaptive CRC-RLE page partitions

**Frozen 2026-10-09**; [issue #183](https://github.com/definitely-stable/Mathlab/issues/183), parents #173/#126. Research-only finite model following G2-B4-C0/C1 and B4-B. This is NOT a universal compressed-index, cell-probe, NAND, POSIX atomicity, or filesystem lower bound.

## G0 — service, encoding and paid metadata

Binary state f of N>=1 cells, exact lookup and nonempty range assign(l,r,v) with last-write-wins (including semantic no-op writes). Adaptive partition 0=x0<x1<...<xK=N: every segment has its own *complete* canonical IXR1+CRC32 frame, page-padded independently to B-byte pages, B>=4; no page-sharing among segments.

One independent on-disk page-padded directory **IDR1** contains four magic bytes, uvarint N and K, K pairs (uvarint segment length, uvarint segment page count), CRC32 little-endian. Every directory and segment byte/page is charged; data pages are concatenated in logical partition order after the padded directory. Segment addresses are derived as prefix sums of paid page counts: no uncharged indirection, allocator table, hash map or free-list. Directory offsets and encoded byte lengths are reconstructed via parsing; each segment frame and CRC is independently validated when explicitly decoding state. The canonical *global* RLE snapshot is used ONLY as the space-budget comparator.

Physical page-image recourse is computed on full packed directory+segment byte images at the same byte offsets, with absent bytes comparing as zero. X counts changed page positions including newly allocated positions; G counts old trailing page positions no longer allocated. Model writes = B*X, not actual writes or NAND. In-place *idealized* peak P=max(D_old,D_new), no simultaneous shadow version, torn write, failure recovery or atomic commit. Logical segment deletions must not be mistaken for G freed physical pages. Transient CPU/working RAM remains unbounded; all guarantees concern persistent auxiliary RAM only.

**Disk-only directory**: zero persistent auxiliary RAM bits; each point lookup reads the entire directory including CRC plus the segment prefix (without reading/validating the segment CRC). Page reads Qcold=directory_pages+prefix_pages; fully verified lookup replaces prefix_pages by all segment pages. **Mirrored directory**: store the same directory on disk and cache its entire unpadded encoded bytes in persistent RAM M=8*directory_length bits; Qwarm=prefix_pages; restart/cold Qcold unchanged and directory must be refilled. There is no uncharged decoded lookup table. The RAM gate requires M<=M_cap_bits explicitly; no exchange from RAM to allowed disk bytes.

Space cap for each state f is C(f)=floor(alpha_num*S_global(f)/alpha_den)+beta*B, with alpha_num,beta>=0 and alpha_den>0 integers fixed for all N and histories. Require after-step D_new<=C(f_new); old state D_old<=C(f_old); in-place P=max(D_old,D_new)<=max(C(f_old),C(f_new)). A stronger peak cap tied only to the new state would trivially forbid rapid compression from a previously larger valid state, and is NOT used here. Apply worst-case Q<=Q_cap either disk-only or mirrored-warm as expressly selected. Exact finite offline comparator chooses new partition after each operation; no general competitive claim.

## Restricted theorem — representation fragmentation and compulsory zero-reset reclamation

Let Kold be the segment count before assign(0,N,0), Dold physical bytes including directory and padded segments. Let C0=C(0^N), U0=floor(C0/B). Every feasible new partition with Knew segments satisfies:

(1) Dnew >= B*(Knew+ceil(Ldirectory_new/B)) >= B*(Knew+1).

(2) Knew <= U0-1. Thus at least max(0,Kold-U0+1) logical segment boundaries must be eliminated by re-partitioning.

(3) G >= max(0,Dold/B-U0) **trailing physical page positions** disappear in the compact same-offset model. This is not a NAND physical page rewrite lower bound. Proof: directory and each nonempty segment occupy at least one distinct page; page-aligned Dnew<=C0 gives Dnew/B<=U0, and the compact file shrinks by Dold/B-Dnew/B pages.

For disk-only full CRC-directory lookups, Qcold>=ceil(Ldir/B)+1. For the *literal mirrored-directory* implementation the RAM cache cost is exactly M=8*Ldir bits, so Qwarm may omit the directory but Qcold does not. These are parser/layout-specific bounds, not universal succinct metadata lower bounds.

**Asymptotic conditional family:** for fixed B, g admitting one-page segments, N divisible by g, start alternating bits in Kold=N/g independent g-cell segments. A full-range assign(0,N,0) makes a globally uniform state of exact IXR1 length S0=O(log N). Under a fixed alpha,beta cap, feasible new partitions must occupy O(log N) bytes and hence O(log N/B) pages; the old physical allocation was at least BN/g bytes. Therefore G >= N/g - O(log N/B) retired **page positions** in this single interval overwrite, *conditional on an old K=N/g partition and an admitted new partition*. A compact one-segment layout avoids this burst, so no universal incompatibility of compressed space and local writes is proved.

**Concrete certificate:** N=64, B=32, g=8, alternating old state has eight one-page segments and one directory page (Dold=288); a new zero state has global IXR1 size 12, and cap alpha=4,beta=2 is 112. Any feasible new K<=2, removing at least 6 logical segments; old Dold=9 pages and new Dnew<=3 pages force G>=6 page positions. A one-segment new state has Dnew=64 and retires 7 page positions. All counts include CRC, on-disk directory, padding and zero persistent auxiliary RAM.

## Verification and novelty gate

- Exhaustive binary states N<=7 and every 2^(N-1) ordered partition: canonical directory serialization/decoding, CRC/tamper/varint checks, per-segment decoding, all point queries; all one-step range writes N<=5 and exact independent byte/block/page ledgers.
- Independent finite enumerator of all partition policies vs DP optimum for N<=5, U<=3 under disk-only and mirrored RAM limits; compare exactly priced modeled changed pages, retire pages, space/old-new-admissible peak and Q; do not claim larger Cartesian exhaustive coverage.
- Explicit distinction between disk-only query, warm mirrored query and cold/restart full directory; no generic RAM bound because transient decoding memory is unbounded.
- Reuse catalog LIT-098 (online dynamization), LIT-175 (RASK), LIT-177/179/180/181/212/213 (succinct dynamics), LIT-182/184/185/186 (compaction), LIT-050 ESA 2026. **Potentially missing 2026 primary-source novelty barrier** Kempa and Kociumaka, SIAM SODA 2026, DOI 10.1137/1.9781611978971.65, concerning compressed static string-query lower bounds (not this model); full proof not reconstructed. Import only after canonical dedup and generated source-index check.
- Hosted GitHub CI only. **STOP** general theorem claims until real shared-page, RAM-bounded query implementations, persistence/versioning and admissible representation classes are specified. Production Rust remains NO-GO; issues #183/#173/#126 stay open.

**Decision:** exact adaptive-partition reference model and restricted fragmentation/reclamation certificate, no original universal locality–compression–recourse theorem.
