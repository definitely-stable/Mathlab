# INDEX-001 G2-B4-C3 — shared-page CRC-RLE partition and bitmap countermodel

Frozen 2026-10-09 · [issue #183](https://github.com/definitely-stable/Mathlab/issues/183) · parents #173/#126 · predecessor [C2](INDEX-001-G2-B4-C2-ADAPTIVE-PARTITIONS.md).

**Classification: restricted lower bound + falsification of universal transfer.** Research-only finite page-image model. No SSD/NAND metrics, POSIX writes, crash durability, concurrency, production Rust or verified general cell-probe theorem.

## G0. Freeze the complete cost model

Service: exact binary f:[0,N)->{0,1}, point lookup and last-write-wins nonempty assign(l,r,v) including idempotent writes. B>=4 bytes/page. Global comparator S(f) is the exact full canonical IXR1+CRC32 RLE snapshot.

- C2: independent IXR1 CRC segment frames each occupy whole B-byte pages; separate CRC IDR1 page-padded directory stores logical lengths and segment *page counts*. D_C2 = B[ceil(L2/B)+sum ceil(S_i/B)].
- C3: adaptive partition; each segment is a full canonical IXR1+CRC32 frame but all segment frames share one byte-packed data region and page padding appears only at the region end. Distinct CRC-checked IPD1 directory, separately page-aligned, stores magic, uvarint N, uvarint K, K pairs (logical length, exact frame byte length), CRC32. Every byte and allocation charged; no free index, offset table or indirection. D_C3 = B[ceil(L3/B)+ceil(sum S_i/B)]. The directory is rebuilt when the partition changes; prefix sums determine segment starts.
- Bitmap negative control: ceil(N/8) raw little-endian-bit-order bytes, page-padded once, with universe N a service parameter. No directory. Point query uses one page; updates can stream byte-wise through touched page span. Its space may FAIL the global RLE-relative compressed bound for sufficiently large uniform maps; a finite N=64 counterexample is not an all-N scheme.
- Same-offset new/old images yield X changed page positions, G disappearing trailing positions and A new tail pages. Idealized in-place peak=max(D_old,D_new), no atomicity/power cuts. Page images are NOT actual OS writes, data relocations or NAND bytes.
- The streaming **point lookup** parses the full IPD1 directory sequentially, checking CRC before trusting a segment, then parses only the chosen frame prefix, with NO segment CRC validation. A warm mirror uses the exact directory bytes held in RAM; restart/cold rereads the on-disk directory. A one-page cursor and a declared 96-byte register allowance yield logical R=B+96 cold or B+96+L3 warm. In mirrored mode auxiliary M_dir=8L3 bits; never assume RAM decode table free. Python host stores reference images and dense state: its process memory and reencoding **updates** are unbounded; only logical point-read cursor has the R limit. This is not a proof of a bounded-working-RAM end-to-end index.
- Exact offline partition selector is admitted under D<=floor(alpha*S(f))+beta B, Q<=Qcap and point-lookup R<=Rcap. Scalar target is X+G in pages; no online competitive theorem.

## G1. Exact restricted results and counterexamples

For any nonempty binary IXR1 segment, S_i>=12 bytes; L3>=8+|var(N)|+|var(K)|+2K. Hence:

D_C3 >= B[ceil((8+|var(N)|+|var(K)|+2K)/B)+ceil(12K/B)].

This is merely a **representation-specific K–D lower bound**, not a universal succinct-structure theorem. In comparison to C2, payload packing saves B[sum ceil(S_i/B)-ceil(sum S_i/B)] >=0 bytes; the directory formats differ, so D_C3<=D_C2 is NOT asserted for all geometries.

The old C2 rule that K independently allocated pages are required is **false** once frames may share pages. An explicit N=64,B=32 alternating-bit state followed by a single assign(0,64,0) gives:

| g | K | C2 bytes initially | C3 bytes initially | C3 zero bytes | C3 retired pages | Bitmap old/new bytes | Bitmap retired pages |
| - | -: | -: | -: | -: | -: | -: | -: |
| 4 | 16 | 576 | 352 | 64 | 9 | 32 / 32 | 0 |
| 8 | 8 | 288 | 256 | 64 | 6 | 32 / 32 | 0 |

Canonical zero S(0^64)=12 bytes; the state-dependent alpha=4,beta=2 cap is 112 bytes. Both the C3 compressed zero snapshot and uncompressed bitmap fit this cap; the alternating initial bitmap also fits the corresponding budget. Therefore **there is no universal requirement to retire pages upon full-range reset for all representations of this N=64 service**. An all-N compressed-space lower bound might yet exist, but requires different quantifiers; for uniform N growing, bitmaps violate the RLE-relative cap. C2's conditional statement about its own independently page-aligned representation remains correct.

The streaming IPD1 cold directory reader's page probes plus segment prefix are counted from actual serialized storage. Mirrored warm queries charge RAM and omit disk-directory probes; cold/restoration reload does not. Segment CRC remains unchecked for prefix queries and must be separately verified for integrity claims. The oracle is not an algorithmic proof of write locality for arbitrary page-sharing allocators.

## G2. Gates, literature, and next theorem question

1. Enumerate all binary maps N<=7, all ordered partitions and every position at B=16/32. Rebuild independent directory and segment CRC frames; roundtrip complete images; check cold/warm query, logical read-buffer limit and all byte/pad corruptions.
2. Independently census changed page images for all nonempty one-step assignments N<=4, representative old/new partitions, plus a full Cartesian partition-policy enumerator versus separate dynamic programming over small N/U<=3. Record both feasible and infeasible cases.
3. Compare against packed bitmap, which defeats the naive universal page-reclamation transfer; do NOT claim compression-cost impossibility at all N.
4. Prior art: existing [LIT-008](catalog/LITERATURE.md#lit-008), history-independent dynamic partitioning (2026), [LIT-175](catalog/LITERATURE.md#lit-175) RASK, [LIT-183](catalog/LITERATURE.md#lit-183) dynamic bitvectors, [LIT-050](catalog/LITERATURE.md#lit-050) dynamic compressed indexes. New canonical [LIT-281](catalog/LITERATURE.md#lit-281) (Lazy B-Trees, MFCS 2025, DOI 10.4230/LIPIcs.MFCS.2025.87) and [LIT-282](catalog/LITERATURE.md#lit-282) (Space-Efficient B Trees via Load-Balancing, 2025, DOI 10.1007/s00224-025-10238-7). Publisher abstracts checked, their complete proofs not independently reconstructed; IDs and source-index provenance deduplicated against the parallel IMPORT-007 cohort.
5. **No original universal theorem accepted** merely from a fixed layout or its page-diff arithmetic. Follow-up C4 must model sparse/dense switching, shared-page allocator slack, bounded-RAM updating and persistence/recovery with complete resource prices; parent research issues remain OPEN.

**Decision: C3 accepts a valid counterexample and a restricted format bound, not an original universal locality–compression–recourse theorem.**
