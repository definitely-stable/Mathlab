# UCT-005 D1-B2-A — cross-construction transcript and partial-Pareto safety gate

**2026-10-10.** Parent [#223](https://github.com/definitely-stable/Mathlab/issues/223), UCT root [#105](https://github.com/definitely-stable/Mathlab/issues/105). Depends on the byte-conserving manifest fix [#241](https://github.com/definitely-stable/Mathlab/pull/241) / [#240](https://github.com/definitely-stable/Mathlab/issues/240) and on merged D1-B1 [#239](https://github.com/definitely-stable/Mathlab/pull/239).

**Classification:** `PARTIAL_SAME_TRANSCRIPT_UPPER_NO_FULL_PARETO_NO_NOVEL_LOWER_BOUND`.

## Scope and exact shared operations

The [reference comparator](../../research/uct005_d1b2a_partial_pareto.py) runs the same initial GF(2) word and same three authorized SET operations (one no-op) through three existing F1 *conditional upper* families. There are two independent readers: reader0 PINs epoch 0; reader1 authenticates a two-SET catch-up then PINs epoch 2. A subsequent SET publishes epoch 3. Every tested nonempty half-open range is answered at LATEST epoch 3 and AS_OF the two independently pinned roots; oracle answers come from direct XOR of separately maintained immutable words.

- **S — byte-conserving immutable snapshots:** the PAGE-001 fixed-stride manifest has exactly 48 remote bytes per epoch and the packed bit image has `ceil(n/8)` bytes; full-page remote write cost is `ceil(48/P)+ceil(ceil(n/8)/P)`. The corrected counter is tested at `P=1,2,3,64`. PIN authority is assumed ideal and charged separately from remote pages. After PIN-protected GC, only epochs `0,2,3` survive; after first UNPIN+GC only `2,3`; finally only latest `3`.
- **T — legacy authenticated immutable range tree:** independently verifies the canonical Merkle-style frontier against the trusted epoch root, for LATEST and PIN-specific AS_OF. The old `checked_query` function's anchor cost is **not** copied into the AS_OF accounting (a historical PIN already holds the authentic root). Its writer exposes *logical* node rewrites and response bytes, **not physical-page or crash-safe authenticated root-index costs**; old roots are held in the Python oracle. It does not furnish a priced F1 page GC.
- **R — legacy authenticated SET-log with trusted replicas:** verifies the reader1 catch-up before retaining its epoch-2 word, then checks LATEST from both readers against the actual chained author-log digest. AS_OF can answer locally from separately retained trusted n-bit pinned replicas; these extra copies cannot be counted as free. Legacy remote log/reply bytes, including reader1 pre-PIN catch-up, are reported **separately** from generic proof-only bytes and are **not** used to rank R against S or T. Full physical logs and history GC are not priced.

The old legacy code uses *inclusive* ranges; the adapter calls `[l,r-1]` to match F1's required *half-open* `[l,r)`. No extra query appears. Snapshot and tree both hash using explicit domain separators and trusted anchor pairs; this is **conditional computational integrity**, not a new proof of SHA security.

## Why numerical Pareto dominance is prohibited

The resource coordinates are a frozen ordered list `(trusted_bits, peak_remote_pages, set_remote_page_writes, query_remote_page_reads, proof_payload_bytes, pinned_retained_pages, gc_remote_reads, gc_remote_writes, author_upload_bytes, anchor_bytes, prover_work, verifier_work, setup_bytes, durability_barriers)`. Every missing value is represented by **null**, never silently zero.

The function `candidate_dominates(a,b)` only permits a Pareto verdict after:
1. both candidates have identical service and identical physical cost model;
2. both declare `FULLY_PRICED`;
3. **all** 14 cost coordinates are nonnegative integers, so the entire ledger is priced; and
4. `a` is no worse on every coordinate and strictly better on at least one.

No current R/S/T candidate clears this gate: physical pages, historical GC, setup/program bits, transport/authentication and the concrete trusted-authority durability contract are not complete for all three. The correct answer is `UNDECIDABLE_PARTIAL_PRICING`, not “Tree dominates snapshot”, “Replica dominates tree”, or a new joint lower bound. The apparent low remote-query cost of R consumes `n` trusted bits per replica plus each preserved historical copy; the larger snapshot page cost consumes `ceil(48/P)` manifest pages **per epoch**, including no-op epochs.

The script records only actual finite reference API counters; OS page calls are not measured NAND writes, ideal atomic PIN authority is not distributed consensus, and no finite oracle can certify PPT security at unbounded n. Size of author source memory, canonical remote proof framing, global-root pub/read, pinned registry, setup and physical GC are still required for a *real* Pareto-frontier theorem.

## Explicit negative gates and next work

The [independent tests](../../research/test_uct005_d1b2a_partial_pareto.py) replay all `2^n` initial words for `1<=n<=8` under the three common SET epochs and every selected range, compare S/T/R latest and historical parity, confirm PAGE-001 `n=33,P=2` exact page costs, and reject any partial-price Pareto verdict. A separate test demonstrates that Pareto comparison would be possible under **synthetic fully priced and identically scoped** vectors (this does **not** assert such real vectors exist).

**Next D1-B2-B:** implement *physically byte-conserving* immutable tree nodes, authenticated epoch→root manifest lookup, page-rounded allocator and PIN reachability GC; charge source reads, log/bitmap writes, memory, proof, anchor/authority calls, rollback and safe ABORT. D1-B2-C should match a physically priced log/replica comparator (including two offline readers and bounded history or explicitly unbounded retention) on the same sequence. Then run genuine nondominated-point search under fixed budgets and ask whether any new H1+H2 inequality excludes a region **not** eliminated by prior source theorems.

**No original lower bound, root `OPEN_UNPROVED`.**
