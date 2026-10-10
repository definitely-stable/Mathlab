# DAG-002 G2-B2-C0 — common page-image ledger with explicit oracle debt

**Issue:** https://github.com/definitely-stable/Mathlab/issues/326 → https://github.com/definitely-stable/Mathlab/issues/322.
**Dependencies:** Felsner PR #329 → SEA Power PR #331 → this C0 slice.
**Original baseline:** Bulteau et al., Incremental Reachability Index, SEA 2025, https://doi.org/10.4230/LIPIcs.SEA.2025.9 (LIT-187).

**Scientific verdict:** PARTIAL_COMMON_SERIALIZATION / LOGICAL_PAGE_IO_ONLY / POWER_UPDATE_UNPRICED_ORACLE / NOVELTY_UNPROVED / NOT_FULL_COMPARISON.

## Identical update and query semantics, distinct representation

All variants support APPEND_SINK(v,S): fresh sink, sorted unique old parents S, immutable old-old edges, Boolean reachability with reflexive paths. Source parent rows are common graph data and are always serialized and charged to all variants, rather than freely excluded. Input incidence cost is also counted separately as v bits per append. All query answers are checked against independent backwards DFS.

- LAZY: immutable source parent row, count:u16 and parent IDs:u32. Query conducts charged backwards DFS.
- BITMAP: immutable fixed-horizon ancestor bitmap, ceil(horizon/8) bytes per vertex. Update reads old bitmap images via charged page store; query reads only target's image.
- FELSNER_POWER: immutable Felsner chain IDs, anchor pointers and SEA §3.2.2 restricted top sets. Label codec: chain:u32, anchor:i32, rank:u32, pi:u32, lp:i32, num_pairs:u16 plus 8 bytes per (chain, top) pair. Full ancestor bitsets are separately serialized as immutable support images, charged in storage and writes. Felsner family/chain-head manifest is serialized as mutable metadata and rewritten in full on every append. Query reads only serialized immutable source and target/anchor label images, not free historical parent records.

Each page-image key is separately page-aligned, with P application bytes per transfer, 8-byte logical address request overhead per page, full ceil(payload/P) page writes and reads (minimum one page). Exact payload bytes and address bytes counted separately. Manifest overwrite updates logical image; physical media reclamation is outside model. Reads are cold within each query; no cache persists.

**Essential unpaid resource warning:** In the FELSNER_POWER construction, logical ancestry and online family updates still use full *unpriced* Python in-memory ancestor bitsets and manifest objects. Serializing those bitsets and charging their writes does not magically bill update reads or bound RAM. Machine-readable output MUST flag unpriced_update_ancestor_oracle=true and verdict=INCOMPLETE_COMPARATOR_IF_UNPRICED_ORACLE. The simpler LAZY/BITMAP implementations are fully charged only within this narrow abstract page store; this is not a file/SSD/network benchmark. No performance claim compares the three under a fully shared resource contract.

Absent: on-disk files, real allocator, root crash publication, WAL, PIN/GC, cache miss paths, authenticated observers, query concurrency, execution-time profiling, Python object RSS or CPU time. Not a new lower-bound theorem.

## Exact finite falsifiers and gates

- All 64 four-node topologically ordered DAGs, two page sizes P=16,64, three variants and all source/target queries at every insertion prefix, compared to independent backwards DFS.
- Byte-level image coder/decoder, immutable old images vs mutable manifest, exact page padding and eight-byte address overhead.
- Query works after in-memory original parent-list reference is overwritten; real query is sourced only from stored pages.
- Mandatory source-parent byte equality and charged auxiliary-ancestry sidecar, plus explicit negative-control failure if the power implementation is erroneously called fully priced.
- Three reproducible 64-node traces (chain, antichain, fan-in), with no asymptotic interpretation.

Run Python commands:

    python research/dag002_g2b2c_paid_ledger.py
    python -m unittest discover -s research -p 'test_dag002_g2b2c_paid_ledger.py' -v

Focused GitHub-hosted and complete Research checks at exact PR SHA are mandatory. The PR is STACKED on #331 and indirectly #329. Do not merge directly into main, bypass parent PRs or force-push.

## Required successor G2-B2-C1

Implement **fully charged** Felsner+Power update using only data actually read from page store, immutable publication, mutable family manifest, explicit page index/addressing, bounded RAM and read/write counters. Integrate identical-format Record-based (#325) and original paid bitmap vs chain-top (#271); only then compare full shared resource vectors on uniform graph/query traces. If source-state dependence remains unbilled, retain INCOMPLETE_COMPARATOR and STOP theorem promotion.
