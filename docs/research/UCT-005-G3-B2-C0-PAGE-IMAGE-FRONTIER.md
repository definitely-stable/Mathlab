# UCT-005 G3-B2-C0 — Physical page-image recourse, RAM cap, and falsification-first frontier

**Date:** 2026-10-09. [UCT-005 root #105](https://github.com/definitely-stable/Mathlab/issues/105), [G3-B2 issue #178](https://github.com/definitely-stable/Mathlab/issues/178), [G3-B2-B upper constructions](UCT-005-G3-B2-B-UPPER-FRONTIER.md).

**Scientific status:** RESTRICTED_PAGE_IMAGE_ACCOUNTING / COMPLETE_FINITE_TRACE_ORACLES / CLASSICAL_PACKING_LEMMA / THREE_FALSE_CANDIDATE_FAMILIES / CONDITIONAL_CRASH_PREFIX_PROOF / NO_NEW_UCT_LOWER_BOUND / NO_PHYSICAL_DEVICE_BENCHMARK / ROOT_OPEN.

## 1. Important distinction: logical node probes versus physical page I/O

G3-B2-B established three conditional authenticated upper protocols for exactly one task (honest sequential SET; independent offline readers query latest RANGE_PARITY). A *logical node* is NOT a 4-KiB page, and Python allocation/cached tuples do not provide empirical disk I/O. This research freezes an executable **counterfactual storage-layout model** with fixed page images. Claims below hold only for that model. No operating system, actual SSD, fsync, filesystem, wear levelling, FTL, network or authenticated hardware is simulated.

Fixed parameters in the default reference:

| Quantity | Type / value |
| --- | --- |
| Page image | 4096 bytes; each page read/write charged in FULL |
| Header / payload | 64 / 4032 bytes |
| Tree node record | 160 bytes including required span, parity, digest(s), child identifiers / fixed metadata budget |
| Tree packing fan-out | floor(4032/160) = 25 records/page |
| Epoch root-directory record | 48 bytes; a dedicated COW directory page per epoch (deliberately conservative) |
| Replica SET log record | 13 bytes (uint64 epoch, uint32 index, byte value); append ONE new dedicated page per SET |
| Cold server LRU | 1 full page = 4096 bytes; reset on each independent update/query |
| Trusted latest publication | separately trusted epoch u64 + root digest 32B; 40 bytes per SET and 40B per successful lookup, 1B lookup opcode |
| Trusted reader state | 40 bytes S/T; 40 + ceil(n/8) bytes R; initial trust bootstrap charged separately |
| Versions, GC, compaction | every prior root and allocated page retained; NO hidden free reclamation or bounded lifetime |
| Commit durability | idealized atomic page writes and explicit flush barriers, then separately trusted monotonic publication; no real crash implementation |

The chosen node record is a **layout definition**, not a serialization of actual Python TreeNode objects. The iterator maps immutable object identities to declared page/slot positions so all page reads can be traced reproducibly. Initial tree nodes are preorder-packed. Each update's new root-to-leaf copy is packed into fresh pages and followed by one fresh epoch-directory page; there is no in-place mutation of previously published pages. Parent records include pointers to children; no uncharged client root pointer is needed. The hostile server may locate epoch-directory entries by public version, but a missing/tampered directory never authenticates a wrong root against the independently anchored digest.

All page image transfers charge 4096 bytes, even if the written page contains a single 160-byte record. An operation-local LRU has bounded capacity and counts repeated faults on eviction. Capacity zero means no *persistent server cache*; even then a real device would require transient page input buffers, excluded from the cap in that diagnostic mode. The default has one explicitly charged page of cache.

## 2. Exact, model-scoped tree page lemma (classical, not a new lower bound)

Let an SET copy exactly k distinct immutable nodes of the current tree (leaf plus ancestors), let the page payload be P-h bytes and each fixed record r bytes. Let F=floor((P-h)/r) >=1. Our stipulated COW layout packs ONLY the k new nodes sequentially into fresh page images, never mixing versions, and writes exactly one separate epoch-directory image. Therefore

**U_write_pages = ceil(k/F) + 1; U_write_bytes = P[ceil(k/F)+1].**

The updater reads the previous root-directory page and the k old-path nodes, subject to its frozen one-operation bounded LRU. Thus 1 <= U_read_pages <= k+1; exact fault count follows the recorded page-address trace, **not** ceil(k/F) without a placement hypothesis. Query for a range reads the directory page plus precisely the nodes visited by the deterministic G3-B2-B canonical proof traversal, again subject to the LRU; transferred reply bytes are the *actual serialized JSON length*. With zero in-operation caching the same page can be read repeatedly; a statement in terms of unique pages alone is not valid.

**Proof:** A page holds at most F prescribed fixed records. The explicit allocation divides k new records into consecutive groups of size at most F, so precisely ceil(k/F) fully charged page images are written. The epoch-directory page is a disjoint write. On reads, LRU faults count each requested page missing from the bounded resident set; they can never exceed the number of listed touches, and at least one directory page is accessed. The reference module records every touched page ID and tests this logic against independent small models. QED.

For n=256 and a leftmost SET, k=9. With F=25, exactly **2** page images are written (1 packed data + 1 directory); with F=1 (256-byte page, 64-byte header, 160-byte record), **10** page images are written. The underlying logical k=9 is unchanged, while raw byte volume changes too. This establishes **layout sensitivity**, not a new universal lower bound. Root-only full-range RANGE_PARITY has one logical tree-node read and, in our cold placement, two page reads (one directory, one root). It is an explicit counterexample to any claim that *every range* must touch Omega(log n) physical pages in this particular construction.

A trusted n-bit replicated reader whose SET log is already synchronized can have **zero remote log-page reads** for a range query while still paying its anchor call, its 40+ceil(n/8) trusted bytes and the cost of all earlier delivered updates. This defeats any claim of positive universal per-query remote pages **without restricting trusted state and backlog**.

## 3. Physical upper ledgers S/R/T are not secretly the same storage algorithm

**T (tree):** the executable TreePageLedger calls the exact G3-B2-B author SET and range-proof code, then follows the old node IDs and the immutable new nodes to map actual *logical* accesses onto frozen *physical page IDs*. It charges page faults including root-directory lookup; writes are fresh packed COW node pages plus one directory page, regardless of idempotent SET. It retains all previous versions for comparison, so retained page count grows each epoch. Hash/XOR verification and exact canonical JSON response bytes are inherited from the prior verified implementation. No real durability proof for these pages is claimed.

**S (snapshot):** an explicitly *different* full immutable COW bitmap layout packs ceil(n/8) data bytes into pages with identical 64-byte headers, and allocates a complete new bitmap plus one new directory page per committed SET. A cold SET must read every bitmap page and the directory and write new data pages plus directory; an independent query reads every bitmap page plus directory. The existing Python G3-B2-B snapshot hashes **n bytes** (a byte per bit) per SET, not ceil(n/8); both physical packed-bit bytes and hashing input bytes are kept separate rather than reporting misleading identical units. Alternative in-place updates need a different crash-atomicity proof and are not represented.

**R (replica):** to avoid free log-page overwrite under per-epoch crash durability, each 13-byte SET receives its own append-only 4096-byte physical page plus a distinct directory image. Rejoining from k missed epochs reads k log pages and one directory page (if k>0), even though only 13k logical bytes are informative; this is **one conservative concrete upper construction**, not an optimal page packing theorem. The client stores n authenticated bits and pays the k digest updates and transferred JSON receipts. Client-side durable writes/atomic adoption still require an explicit protocol; the previous in-memory all-or-nothing reference does not establish crash safety.

All three have the same F1 trusted authority and same logical request/update semantics, **but different frozen storage representations**, so physical costs are construction upper points, not comparisons of identical encodings. No lower bound may be inferred merely from their Pareto frontier.

## 4. Publication order, crash cuts, and what is proved

Freeze the *ideal* publication protocol:

1. WRITE_DATA (new immutable data pages)
2. FLUSH_DATA
3. WRITE_DIRECTORY (epoch-to-root pointer/digest record)
4. FLUSH_DIRECTORY
5. PUBLISH_ANCHOR (trusted atomic publication, externally linearizing commit)
6. ACK_COMMIT

Under the explicit assumptions that FLUSH really makes **all** preceding complete page images durable and that anchor publication is durable, every crash prefix obeys: if the new anchor is visible, new data and directory were already durably flushed. If publication did not occur, the former anchor remains authoritative; partially written newer pages may become **orphans**, and no GC/reclamation is proven. A Byzantine server can still withhold, causing ABORT.

**Proof:** The publication step is ordered after both flush barriers; any prefix containing PUBLISH_ANCHOR contains both completed flushes. Conversely a prefix without publication cannot authenticate a new latest version against the still-old independent anchor. This implication is true only under the stipulated flush and atomic-anchor semantics. QED.

Countermodels are explicitly enumerated: publishing before the first data flush admits a crash with a new root but missing data; placing FLUSH_DATA before WRITE_DATA is not a valid durability barrier. The oracle rejects both orderings. Real-world fsync ordering, directory-page torn writes, disk failure and client checkpoint crash atomicity remain **OPEN**; do not report the symbolic prefix result as a production crash-safe engine.

## 5. Falsification gate: rejected conjectures versus original root

The deterministic method [page oracle](../../research/uct005_g3b2c0_pages.py) and [independent unit tests](../../research/test_uct005_g3b2c0_pages.py) falsify at least these too-strong candidate claims:

| Candidate stated without qualifications | Explicit countermodel | Decision |
| --- | --- | --- |
| Every SET writes at least as many physical pages as logical updated nodes | n=256, k=9 logical nodes, page writes=2 under F=25 | REJECTED |
| Every authenticated RANGE_PARITY query reads at least Omega(log n) physical pages | Query [0,n-1] is one covered tree root + one directory page (2 pages) | REJECTED |
| Every correct F1 reader must read at least one untrusted data page per query | Full local replica at latest checkpoint, k=0; anchor read is charged separately, untrusted log-page reads=0 | REJECTED |

These are classical explicit constructions. They **do not** refute published BKV memory-checking results: BKV uses a different query/service/security model and careful local memory/read-write definitions. These witnesses show why such a bound cannot simply be transferred to our broad formulation without hypotheses.

**Already-indexed direct same-task partial-sums barriers:** [LIT-111 Fredman–Saks, STOC 1989](https://doi.org/10.1145/73007.73040) studies parity partial sums PS(n,2) under update/probe budgets; [LIT-112 Pătraşcu–Demaine, SIAM J. Computing 2006](https://doi.org/10.1137/S0097539705447256) proves stronger cell-probe and external-memory bounds for partial sums under their respective word, operation and amortization assumptions. The RANGE_PARITY(a,b) service subsumes prefix parity queries via a=0; SET can simulate binary point flips by reading the old bit or supplying current value as part of an authorized update, **but that extra source information/read and our independent 40-byte trusted root oracle must be charged**. Therefore neither paper can be called a new UCT theorem, nor can an equation be imported into F1 without an assumption-preserving reduction. This prior-art barrier is at least as relevant as BKV for candidate C1. Both papers are already canonical; do NOT allocate new LIT IDs.

Reference verification: [Boyle–Komargodski–Vafa, STOC 2024](https://doi.org/10.1145/3618260.3649686) explicitly proves general computational memory-checking constraints, including strong read/write-space tradeoffs (our existing LIT-157). [Cachin–Ohrimenko COP, I&C 2018](https://doi.org/10.1016/j.ic.2018.03.004) has server forks and honest-server linearizability (not a trusted global F1 bulletin). [Reinhart–Blass–Annighoefer, JISA 2026 ADSC-SNARK](https://doi.org/10.1016/j.jisa.2026.104444) proves stateful authenticated computation with domain-specific assumptions; it does not supply free latest-root publication to arbitrary offline readers. Source verification here is publication abstracts and available primary descriptions, **not full independent reproduction of their theorem hypotheses**; that transfer audit is still required. Do not mint duplicate LIT IDs.

## 6. Research milestone and next admission gate

**C0 acceptance:** executable page/record and LRU model; explicit immutable per-version layout and root directory; actual complete-page read/write bytes; RAM cap; reference serialized proof bytes; an ideal ordered crash-prefix oracle; independent finite tests, no hidden network/physical benchmarks; documented rejected candidate inequalities; typed theorem tree node; GitHub-hosted Research CI.

**C1 next:** fix *one genuine*, fully charged physical online service (durable writer/source state, 2 offline readers, page RAM and cell widths, query and update adversary, anchor publisher setup/time, verifier hash CPU, physical page-byte reads+writes, proof wire bytes, trust bootstrap, crash recovery and retained-version GC). Compare S/R/T and authenticated-state succinct candidates only when all dimensions match. Seek a quantified uniform-family inequality F_n(R)>=g(n) that excludes tuples still allowed by **audited same-model published bounds**; require an independent proof and explicit achievability counterexamples. If none survives, mark STOP_NOVELTY for this natural task, not a fake UCT-005 root proof.

**No original asymptotic lower bound established; UCT-005 #105 and G3-B2 #178 remain OPEN.**
