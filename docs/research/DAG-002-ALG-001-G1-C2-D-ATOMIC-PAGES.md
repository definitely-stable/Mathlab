# DAG-002 × ALG-001 G1-C2-D: atomic-root page publication

**Issue:** [#161](https://github.com/definitely-stable/Mathlab/issues/161).
**Dependency stack:** [#267](https://github.com/definitely-stable/Mathlab/pull/267) → [#268](https://github.com/definitely-stable/Mathlab/pull/268) → [#271](https://github.com/definitely-stable/Mathlab/pull/271) → this slice.
**Classification:** FINITE_CRASH_PREFIX_REFERENCE / CLASSICAL_COW / STOP_THEOREM_NOVELTY_FOR_ATOMIC_ROOT / NO_AUTHENTICATED_FRESHNESS / NO_GC.

## 1. Typed model and physical-resource ledger

Single writer, append-only DAG vertices in topological order, Boolean reflexive reachability. APPEND_SINK(v,S) receives a complete charged v-bit parent-incidence row, not made available freely to queries. Every stored vertex label is the *immutable* strict-ancestor bitmap. A persistent, copy-on-write directory maps each vertex to a physical page extent using a 32-bit starting page plus 32-bit page count. Each directory image has eight header bytes and eight bytes per vertex, rebuilt for every append. There are two special physical root slots (pages 0 and 1); a root contains a committed generation, directory start/page count, committed vertex count and paid 32-bit high-watermark allocator pointer, with CRC32 over its header.

Storage consists of C pages of P application bytes each, 32 ≤ P ≤ 4096; a single complete page write is assumed atomic and durable. **All stage pages are assumed persisted in order before the final atomic root-slot overwrite.** A crash may occur only *between* completed page writes. The implementation does not invoke fsync, flush hardware, verify filesystem ordering, implement a WAL, tolerate partial pages or guarantee any actual drive durability. Only serial updates and readers observing recovery after an operation/crash are modeled: no concurrent readers, pinned generations, ABA, trusted remote clock, cryptographic proof, live GC, malicious Byzantine behavior or hidden versioned state.

The persistent root's high-watermark pointer allocates only previously uncommitted consecutive tail pages. Uncommitted pages left after an aborted update can be overwritten on the next update without moving prior committed pages. **Committed pages are never reclaimed**: capacity exhaustion rejects updates without root change. An actual allocator directory/free list is not needed under this restricted monotonically growing address model; its limitation is explicitly part of the cost contract. Copying the directory every append costs real newly allocated full pages; this is not a B-tree or compressed directory.

Charge per operation:
- Each full-page read and write separately, including the final root-slot overwrite and both root-slot reads on recovery.
- Page-transfer bytes = P times counted page transfers; an additional four logical address bytes per read/write request, independent of page bytes.
- Parent incidence command v bits per successful append.
- Two initialized root pages (included in capacity, reported separately from subsequent write traffic).
- Conservative upper envelope for logical image buffers, checked before persistent writes against a declared RAM cap, **not** the Python interpreter's complete runtime memory.
- Directory-record bytes and the current high-watermark are truly stored in charged pages. No charge is claimed for Python object/dictionary bookkeeping, OS framing, device erase blocks or time.

## 2. Exact restricted formulas

Let k_p=ceil(ceil(p/8)/P), d_v=ceil((8+8v)/P), where d_0 is interpreted as zero because no directory exists at genesis. On append v with parent set S:

    preparation remote reads: 2 + d_v + sum_{p in S} k_p
    new immutable label pages: k_v
    new immutable directory pages: d_(v+1)
    completed root overwrite pages: 1
    completed writes: k_v + d_(v+1) + 1
    newly committed allocation: k_v + d_(v+1)
    parent incidence input: v bits

Root writes reuse one of the two slots. The page-address ledger charges four bytes per read/write request. These are exact equalities **for this serialized construction**, not lower bounds for arbitrary reachability indexes.

## 3. Classical crash-prefix invariant, with proof

Assume a valid old committed root R, stage addresses disjoint from every old committed extent, ordered durability of staged bitmap pages and complete directory pages, then exactly one atomic new-root write into the *other* root slot. For any interruption after a prefix of the planned page writes, recovery returns **either the complete old graph or the complete new graph**.

Before the root write, the old root and all of its referenced immutable pages remain intact, while partial staging is unreachable. After the root write, every new referenced page has already become durable; recovery selects the valid root with larger generation. Its directory contains all prior immutable extents and precisely one new label. The label represents the union of its parents' ancestor sets and parents themselves, hence answers Boolean reachability by standard DAG induction. No mixed-epoch prefix is returned. This is the standard shadow-paging/copy-on-write root-switch principle specialized to a restricted DAG reference, **not an original theorem**.

The premise assumes complete atomic page writes and persistence ordering; the implementation cannot validate those on hardware. Neither CRC32 nor a two-slot version is a cryptographic monotonic-freshness protocol. Replaying an older valid root can cause rollback, explicitly demonstrated by the negative oracle. The old slot itself can be overwritten on the next epoch, so two slots do not promise unlimited history retention or PIN preservation.

## 4. Exact falsification and acceptance

Run:

    python research/dag002_g1c2d_atomic_pages.py
    python -m unittest discover -s research -p 'test_dag002_g1c2d_atomic_pages.py' -v

Nine focused tests:
- Every 4-vertex topological DAG (64 graphs), every append and every crash cut between atomic page writes, verifying recovered reachability against independent backward DFS.
- All 1,024 topological DAGs with five vertices after fully committed appends.
- A chain of 45 vertices spanning directory pages and reachability transitivity.
- Aborted-tail reuse without exposing an incomplete previous write; refusal of out-of-capacity and RAM-over-budget updates.
- Independently recomputed input bits, directory/label/root page writes, update reads, full transfer bytes and address bytes.
- An exact replayed-old-root rollback counterexample: CRC32 is no trusted antirollback clock.
- Type/budget/parent validation, no unpriced parent access or false zero-cost garbage collection.

**Must pass** dedicated GitHub-hosted workflow and full Research CI on exact PR head; local passing tests alone do not grant acceptance.

## 5. Source and novelty gate

[Incremental Reachability Index, Bulteau et al., SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9) explicitly uses immutable append-only DAG labels, a small mutable manifest and discusses manifest rollback (see introduction). The newer work does not make our two-root COW publication novel. [Copy-on-write B-tree / shadow-paging principle](https://primitives.pub/databases/monographs/copy-on-write-btrees) similarly describes immutable replacements and final atomic root publication. Our complete-directory copying is simpler but more write-amplifying than tree path-copy; there is no claim to reproduce the SEA 2025 anchor algorithms.

**Decision:** STOP_THEOREM_NOVELTY for this bare two-slot atomic-root lemma. That is a *scoped* STOP, not proof that every cross-domain G1 bound is known; issue #161 remains open for a genuine joint update/read/observer theorem and source-level audit. Authentication/PIN/GC is already explored in [UCT-005](https://github.com/definitely-stable/Mathlab/issues/105); avoid duplicating it without a specifically different, resource-preserving hypothesis. Next G1-C2-E: either a new, precisely scoped joint lower-bound candidate with explicit novelty audit or STOP and archive C1-C2D as source-backed finite baseline. No Rust/production integration.

**Safe merge:** This PR is stacked on #271, which depends on #268 and #267. Each predecessor requires its own successful hosted exact-head CI and review before merge; no force merges or assuming queued checks passed.
