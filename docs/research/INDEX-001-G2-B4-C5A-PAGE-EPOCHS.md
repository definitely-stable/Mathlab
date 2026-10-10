# INDEX-001 G2-B4-C5A — paid page slots, root publication and volatile pins

Frozen 2026-10-10. Scope: [C5 issue #211](https://github.com/definitely-stable/Mathlab/issues/211), parent #183 and roots #173/#126. Continues C4 hybrid codecs.

**Classification: CONDITIONAL_ATOMIC_ROOT_SAFETY / EXPLICIT_SLOT_REUSE / PINNED_PEAK_COUNTEREXAMPLE / NO UNIVERSAL NEW THEOREM.** A research model of page-addressed immutable generations, NOT production filesystem durability, physical NAND behavior or a general lower bound for compressed indexes.

## Frozen finite page model

Service: binary map snapshots encoded as complete HYB4 files, point/read service via a full validated image, latest and explicitly pinned historical epochs, single writer. Every physical slot costs exactly B bytes, B>=64. Page 0 is a persistent R5IX root containing epoch, head physical page address, chain page count, total unpadded data bytes and CRC32, root CRC32 and zero padding. All pointers are u32 and bytes/count/epoch use u32 in this restricted format.

Every immutable D5IX data page has magic 4 bytes, next-page u32, payload length u16, at most B-14 payload bytes, zero padding and full-page CRC32 trailer. F5IX free records are themselves a full CRC-validated B-byte physical page. Any allocated slot no longer referenced remains a paid dead slot until sweep overwrites it with a F5IX marker. No free list/index is silently available in RAM: allocation finds free slots by physically scanning pages and paying each read. Staging writes pages with terminal links and separately patches predecessor links, charging additional full-page writes. No sharing/dedup of pages between immutable generations.

Pins are volatile descriptors of five integers; pin tables and the CPython object graph are not fixed-RAM bounded. The version proof concerns only model events; no durable pinned-reader history across crash. Under a full-image integrity contract, an abstract one-pass verifier reads root plus every data page and validates root, page and entire-image CRC and chain length. The Python reference may make additional reads; all are separately counted. Opaque HYB4 inner CRC is a higher layer verified by the existing C4 decoder.

**Failure assumption**: complete B-byte page writes become durable in order; every new linked page is durable before a single atomic whole-page root overwrite; no torn sector/page, write reordering, multiwriter races or failed flush. The implementation uses tempfile and flush, NOT fsync or a real atomic-page filesystem contract. Therefore no real crash-safety or NAND guarantee follows.

## Restricted theorem, counterexample and limitations

Given old complete immutable root R0, stage new pages only in physically FREE slots or newly appended slots, never overwriting pages reachable from R0 or any current pin. Before root publication every operation prefix preserves R0 and its reachable data. After root publication the new root points to the already checked complete new chain. Thus every modeled crash at a page-write boundary recovers the old or the new complete generation. Proof: induction on prepublication page writes (all outside old live/pin set), followed by one root-atomic switch.

If p_old occupied immutable data pages must stay intact while p_new new distinct data pages are staged, the *physical* peak is at least 1+p_old+p_new pages, including the paid root page. This lower bound applies to the explicit immutable no-dedup one-root model, regardless of whether the old reader remains pinned when the new generation is committed: R0 is still active until the swap. If a disk cap forbids this overlap, the update cannot complete. A later GC may reclaim old unpinned data pages but cannot retroactively avoid the peak. Other storage formats, content sharing, overwrite-in-place logging, specialized encodings or a different crash contract are countermodels to any unqualified universal claim.

Physical allocation is P*B where P includes live, pinned, dead and FREE slots, even if some were reclaimed. Logical page-image changes are distinguished from actual file read/write method calls, OS syscalls, fsync and hardware I/O.

## Independent hosted acceptance

The Python module research/index001_page_epochs.py implements real tempfile page writes, scan-to-find-free allocator, pin/unpin, full CRC chain reader, explicit GC and replayable crash-prefix hooks. Its source HYB4 data is streamed in B-14 byte chunks; it has a one-page serializer, but DOES NOT certify bounded total Python RSS, bounded reader pin table or bounded allocator CPU cost.

The independent tests research/test_index001_page_epochs.py reconstruct raw root/data CRC and page chains without reusing model readers; exhaust all binary maps N<=6 in B/R/S0/S1 modes at B=64/128; examine every simulated crash prefix of page writes (including intermediate link patches), recovery/sweep, pin retention, finite disk caps and page CRC corruption. The in-memory crash snapshot oracle is explicitly NOT a working-RAM implementation.

**STOP_NOVELTY:** conditional page-atomic old/new safety and disjoint-generation peak are elementary model-specific facts. Original joint compression/query/RAM/update/durability lower bound remains OPEN. Next C5-B must address actual atomic publication and fsync, torn pages, persistent pins, shared-page indirection and full bounded-RSS constraints. Compare LIT-008/098/175/183/281/282, including the already documented Lazy B-Trees erratum. Parent issues #183/#173/#126 and C5 #211 remain OPEN.
