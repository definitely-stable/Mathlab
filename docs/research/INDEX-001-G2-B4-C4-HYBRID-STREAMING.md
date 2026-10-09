# INDEX-001 G2-B4-C4 — hybrid bitmap/sparse/RLE and paid streaming updates

Frozen 2026-10-10. Parent issue #183 (also #173, #126). Follows C3 shared pages. Research-only, not a general lower-bound theorem or production storage engine.

## G0: Exact service and accounting

Binary map f on N cells, 1 <= N < 2^63, last-write-wins nonempty range assignment, exact state reconstruction. Byte-page size B, fixed universe. Canonical HYB4 frame: magic (4 bytes), uvarint N, one mode byte, uvarint payload size, payload, little-endian CRC32 of header plus payload, and zero page padding. No hidden in-file directory.

Six modes: U0/U1 represent constant vectors with zero payload; S0/S1 store a default bit, an encoded count and strictly increasing positions of exceptions; R stores maximal alternating-value runs using positive varint lengths; B stores N raw bits in ceil(N/8) bytes. Each candidate pays full metadata, CRC, physical page alignment and unused tail. D=B*ceil((header+payload+CRC)/B). The comparison against canonical full IXR1 uses D(f)<=floor(alpha*S_IXR1(f))+beta*B.

All mode-policy comparisons use the SAME full-CRC verified query service, priced at Q=D/B page reads, not unsafe prefix reading for one option. Finite offline mode selection minimizes changed same-offset page images plus retired trailing pages; all added pages are already counted among changed images.

## G1: Streaming implementation and its limits

The file-backed updater performs a source CRC/padding preflight, then an exact first semantic pass computing every eligible output format's encoded length, then a second semantic pass producing the chosen target representation. It uses a B-byte reader buffer, a B-byte writer buffer and an explicitly declared 128-byte register allowance; modeled update working buffers R=2B+128. CRC, page-read requests from all three passes, output page-write requests, final file bytes and discarded tail pages are accounted. Source and output reside in separate temporary files throughout the operation.

IMPORTANT: the Python interpreter heap, tempfile internals and OS cache are NOT bounded by the abstract buffer claim. The independent testing oracle and the finite policy selector allocate entire images in RAM. This is not evidence of an end-to-end physically bounded-RSS updater. A two-file update peaks at least at Dold+Dnew bytes, rather than the idealized in-place max(Dold,Dnew). Filesystem directory entries, allocation metadata, fsync, atomic rename, torn-write recovery, dead generations and crash durability are not priced or proven; the model is not admissible under a peak constraint smaller than this sum.

## G2: Restricted proofs and falsifiers

Bitmap-only cannot satisfy an all-N state-dependent constant-factor IXR1 space cap on uniform vectors: S_IXR1(0^N)=O(log N), while bitmap D=Omega(N) for fixed B, alpha and beta. U0/U1 avoid the size blowup, but switching costs must be charged. This is elementary class exclusion, NOT a new universal bound on succinct dynamic indexes.

A stricter counterexample to greedy immediate size minimization is N=257, B=32 with an admitted initial bitmap containing only bit 0 set. The effective overwrite assign(0,1,0) makes the entire map uniform zero. Staying in bitmap mode changes one logical page image, retires none, and keeps D=64 bytes. Converting to the byte-minimal uniform U0 mode changes its first page and retires one trailing page, yielding two paid recourse units even though it stores only D=32 bytes. Both outputs satisfy alpha=4,beta=2 state-dependent space cap and the same full-CRC service. The initial bitmap is deliberately history-dependent and non-minimal, so this disproves greedy optimality for arbitrary admitted starting states, not every policy that always starts from minimal representations.

The two-pass mode-selection construction also defeats the naive assertion that a streaming hybrid updater must retain N target bits in RAM; it trades additional source reads for bounded reference I/O buffers. No universal asymptotic lower bound follows from these finite models.

## G3: Reproducibility and novelty gate

Independent exhaustive small binary maps N<=7 test all admitted formats and complete serialized images against a separate encoder, all CRC and payload canonicality rules, and page-transfer accounting. Range-overwrite cases through N<=5 test each source mode and multiple destination modes. A 6^U independent Cartesian policy oracle checks a dynamic-programming optimum for N<=4 and U=3. The N=257 counterexample is pinned. Exact GitHub-hosted Research CI is the acceptance gate.

Prior art already indexed: LIT-008 history-independent dynamic partitioning, LIT-175 RASK, LIT-183 adaptive dynamic bitvectors, LIT-281 Lazy B-Trees and LIT-282 space-efficient B-Trees. No duplicate imports or unjustified novelty promotion.

## STOP / C5 boundary

A general joint theorem requires a fully charged external-memory slot allocator and dynamic directory, bounded-memory update implementation with crash-safe publication, and honest physical I/O and recovery quantifiers. This slice addresses hybrid format choice and emulated streaming update only. Root issue #183 stays OPEN; #173 and #126 stay OPEN. NO new universal compression-locality-RAM-recourse theorem is claimed.
