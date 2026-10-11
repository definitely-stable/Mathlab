# DAG-002 G2-B2-C1 — page-read-backed Felsner/Power updater

Owner: issue #336; parent #326 and root #322.
Dependency chain: PR #329 Felsner -> PR #331 SEA Power -> PR #335 common page ledger -> C1.

Primary: Felsner up-growing online chain theorem 3.5 and Bulteau et al. SEA 2025 §3.2.2, DOI 10.4230/LIPIcs.SEA.2025.9 (LIT-187).

Status: FINITE_LOGICAL_PAGE_REFERENCE / HISTORICAL_SUPPORT_READS_BILLED / MODELED_SCRATCH_ONLY / NO_PHYSICAL_RAM_OR_DEVICE_CLAIM / NO_NEW_THEOREM.

## Exact updater cost graph

The previous C0 implementation wrote ancestor support pages, but built future ancestry and chain-family state using inherited, unpriced Python arrays. C1 instead:
1. Reads the whole previous serialized family manifest through the page interface. This yields published vertex count, heads, chain groups and capacities.
2. Validates the fresh APPEND_SINK command, canonical parents, fixed horizon and modeled scratch cap before performing any write.
3. Loads each parent ancestor-support image through the charged page read interface, building the new inclusive ancestor bitmap.
4. Reads parent labels to select a maximum-rank parent, traverses old anchor pointers through separately charged label reads, and calculates integer crossing powers without floating point.
5. Uses only the decoded previous family manifest and new bitmap to execute Felsner's first eligible family and exact family exchange.
6. Loads the chosen anchor's old support bitmap and every required prior restricted-top label by charged reads; computes the new per-chain restricted tops without a hidden chain-to-vertex directory.
7. Publishes new immutable parent record, support image and anchor label, then replaces mutable manifest last. Publication order alone is not crash-atomic or durable.
8. Answers exact Boolean queries by reading published manifest and serialized immutable labels. Queries do not use old graph Python parent arrays or ancestry tables. A new index instance can continue from just the backing page images.

The C0 page image store, fixed parent/label codecs, page padding and eight-byte request headers are reused. C1 manifests also carry published vertex count; the format is scoped separately and should not be silently decoded as C0.

## Accounted vs excluded resources

Charged in this model: old-graph support and label page reads, full old manifest reads, immutable support/label/parent writes, complete new manifest writes, per-key page alignment, padded page transfer bytes, eight-byte logical address overhead and cumulative n(n-1)/2 input bits.

The configurable modeled logical scratch upper bound includes old and new manifest, three bitmap work buffers, parent record, one maximum-sized label and fixed control bytes. Exceeding the cap raises MemoryError before publication. This is NOT process RSS and does NOT limit the backing dictionary holding every page image. Key directory lookups are unpriced. The result explicitly identifies both caveats.

Out of scope: actual disk/filesystem I/O, bounded physical RAM, name-to-page directory cost, allocator, fsync, torn pages, WAL, physical reclamation, PIN/GC, concurrent writers, authenticated freshness, wall time and CPU cycles. It is incorrect to describe this as a production external-memory algorithm or a physically established performance gain.

## Tests and acceptance

Source: research/dag002_g2b2c1_billed_updater.py
Tests: research/test_dag002_g2b2c1_billed_updater.py

Six independent tests: 64 ordered four-node DAGs, P=16 and P=64, every after-prefix reachability query checked against independent backwards DFS; byte-padded read/write counters; fresh instance rebuilding from stored page images; old record immutability; invalid and duplicated manifest entries; low scratch cap rejection without partially publishing new records; and prohibitions on persistent Python parents/partition/labels arrays.

Focused GitHub-hosted CI and full Research CI must pass at exact head SHA. PR is stacked on #335 and can merge only after #329 -> #331 -> #335, with fresh checks and review.

## Next step C2

Build an actual file-backed page store with priced address directory, bounded resident cache, old manifest retention, allocator and page availability. Reuse UCT-005 crash-cut and pinned-generation contracts with their exact trust assumptions. Then add #325 record anchors and #271 chain-top under the same byte format and common workloads. Until all resources are charged and primary results matched, return INCOMPLETE_COMPARATOR and STOP_THEOREM_NOVELTY instead of a joint DAG lower-bound claim.
