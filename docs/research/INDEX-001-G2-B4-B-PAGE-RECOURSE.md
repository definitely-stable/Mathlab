# INDEX-001 G2-B4-B — page-model locality and physical recourse

**Frozen 2026-10-09**, issue #173, parent #126, predecessor INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md. Research-only logical page-image accounting: NOT SSD/NAND, POSIX, atomicity, crash durability, or general cell-probe lower bounds.

## G0 — frozen model, *before code*

Binary latest-write-wins f:[0,N)→{0,1}, acknowledged nonempty assign(l,r,v), exact lookup(i). Fix B>=4 bytes/page, group width 1<=g<=N, and the canonical CRC32 IXR1 binary RLE snapshot format of G2-B4-A. Three reference representations of exactly the same logical state:

1. **Packed canonical**: one contiguous binary IXR1 image, new image after every update. A logical page p changes if its padded B-byte old/new images differ at the same byte offsets; missing tail bytes compare as zeros. X_pages = count of changed page positions, X_bytes = B*X_pages. This is a necessary changed-page-position count for same-offset canonical overwrites, **not** an achievable crash-safe storage schedule. Truncation, inode writes, NAND and directory metadata not priced.
2. **Fixed segmented slots**: divide into ceil(N/g) groups of <=g bits; each group has its own IXR1 frame, padded to C(g,B)=B*ceil((8+2*|var(g)|+g*(|var(g)|+1))/B) bytes and addressed by arithmetic. This conservative upper capacity accommodates every group with at most g cells; slot padding and all slots charge steady disk space. No directory, extra RAM metadata, GC, or dynamic overflow; N,g,B treated as given service parameters. An update may affect multiple groups.
3. **Raw byte cells**: N fixed bytes, each one logical bit. In-place byte updates; explicit non-succinct control, not a packed bitmap.

Ledger per update: exact logical boundary symmetric difference L, steady allocated bytes D, old/new serialized snapshot lengths, changed logical pages X_pages and X_bytes, and *point-query* unique page probes Q. Avoid calling X_bytes actual application I/O, NAND programming, SSD write amplification, or relocated live bytes. Files with different lengths also report page deallocation separately.

**Queries**: packed and segmented use a specified forward-only run-pair parser from the corresponding frame start until the containing run. Only bytes of the traversed prefix are read; no CRC verification on these integrity-unchecked point reads. A whole-frame CRC-verified read counts all pages separately. This models the given parser only; no lower bound for other readers with RAM metadata, caches, rank/select, or alternative encodings.

## G1 — restricted contiguous-layout physical-page theorem

Let N be odd, N>=3, and |uvar(N)|=|uvar(N-1)| (exclude varint power-of-128 crossings). Initial binary state alternates 0101…0, so it has N unit-length runs. Update assign(0,1,1) changes it to 1101…0 with N-1 runs. **Exactly one boundary disappears: L=1.**

Let h=4+|var(N)|+|var(N)| be the fixed pre-payload IXR1 header length (magic, N, k). Initially the N two-byte run pairs alternate (1,0),(1,1); afterwards the N-1 pairs are (2,1),(1,0),(1,1),... . Throughout the overlap interval [h+2, h+2N-2), each run-symbol byte differs (phase-shifted by one removed two-byte pair). Every full page within this interval (B>=4) contains at least one changed symbol byte, thus cannot retain its old byte image.

Consequently, **every same-offset canonical packed overwrite** has

X_pages >= max(0, floor((h+2N-2)/B) - ceil((h+2)/B)).

For fixed B and stable varint widths this is Omega(N/B) changed page positions even though L=1. This is a simple layout-specific bound, not a universal theorem: alternative pointers, indirection, buffers, chunking, dynamic succinct structures and noncanonical representations are outside its quantifiers. It also says nothing about the number of underlying SSD writes during a real update.

## G2 — constructive countermodel to any universal locality claim

If C(g,B)=B (for example g=8,B=32), each group occupies one page. A single-cell update affects at most one group, hence X_pages<=1; arithmetic-addressed point lookup consumes at most one page, Q<=1, for every N. The cost: D_slots = ceil(N/g)*B bytes regardless of how compressible the full state is. For all zeros global packed IXR1 is O(log N) bytes, but fixed slots consume Theta(NB/g). For alternating data packed takes Theta(N) and the restricted adversary rewrites Omega(N/B) positions, whereas slots have Theta(NB/g) allocation and O(1) local changes. A raw byte-array shows a second local-write alternative at N bytes of storage.

When C(g,B)>B, the one-page query/update claim is withdrawn; bound by the number of pages in the slot instead. Slot size is charged; do not hide RAM index or page padding. This is a separation between these **specific layouts and workloads**, not an all-data-structures Pareto frontier.

## Verification and scientific novelty gate

- Entire binary state space N<=8, and every one-step nonempty binary assignment N<=5, independently checked against dense-array truth and canonical IXR1 decoding.
- Exact page-difference comparison via independent zero-padded chunk oracle, including file shrink/expand; B=8,16,32. Exhaustive lookups for every position with exact page-offset accounting.
- Deterministic adversarial sequence for growing N=3,5,31,129,511 away from excluded varint boundaries. Verify L=1, page lower bound, fixed-slot <=1 for g=8,B=32; include hot/nested and all-zero workload controls.
- Explicitly separate integrity-unchecked prefix Q from fully CRC-verified snapshot pages, steady allocated space from changed-page bytes, and page-image differences from file writes.
- Novelty gate against pre-existing canonical Mathlab sources LIT-098 (online dynamization), LIT-175 (RASK), LIT-177/179/180/181 (dynamic succinct structures), LIT-182/185/186 (LSM/compaction). No new LIT ID without verified distinct primary-source identity.
- GitHub-hosted exact-head CI and review, no hardware performance claims. Issue #173/#126 remain open: an **original joint theorem** would still require fixed admissible representation classes, RAM bits, persistence/dead-version overhead, query workloads, and update/read quantifiers.

**Decision boundary**: restricted packed-layout lower bound + explicit alternative construction accepted if checks pass; universal locality–compression–recourse bound and production Rust remain unproved/no-go.
