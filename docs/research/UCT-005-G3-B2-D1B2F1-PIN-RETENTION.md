# UCT-005 D1-B2-F1 — paid offline PIN-root reachability and retained pages

**2026-10-10** · [Issue #270](https://github.com/definitely-stable/Mathlab/issues/270) · parent [F1 resource ledger #262](https://github.com/definitely-stable/Mathlab/issues/262) / [PR #265](https://github.com/definitely-stable/Mathlab/pull/265) · predecessors [#244](https://github.com/definitely-stable/Mathlab/issues/244) and [#254](https://github.com/definitely-stable/Mathlab/issues/254) are CLOSED.

**Status**: conditional paid **offline** reachability oracle; NOT an online F1 PIN protocol, crash-durable GC, full Pareto ordering or a new information lower bound. UCT-005 root \`OPEN_UNPROVED\`.

## Why this is a distinct problem

The raw \`retained_pinned_pages\` number of the PAGE-001 snapshot is exact because each immutable historical version occupies its own fixed-stride packed-data pages and 48-byte manifest pages. An immutable authenticated COW tree shares unchanged nodes across epochs. Therefore \`number_of_PINs * all_live_nodes\` is generally **not** the COW retained-page cost; likewise counting dictionary keys without authenticating roots and pricing reads is a forbidden free metadata oracle.

D1-B2-F normalizes the known SET/query/GC axes but leaves its *online full-F1* pinned-retained-page axis \`null\`: no same-trust, crash-safe, fully charged online history-retention protocol has yet been established. This F1 slice produces an **independent offline audit** that can falsify an incorrect retention calculation without promoting that axis or a strict full Pareto claim.

## Exact accounting model

Let \`L\` be the latest trusted epoch; \`E\` be the **distinct** independently trusted historical PIN epochs after deduplicating same-epoch reader tokens; \`R(e)\` the SHA256-verified immutable COW node-ID set reachable from the remote root slot of epoch \`e\`. Node image width is exactly 122 bytes, root slot exactly 48 bytes, and page size \`P\` is shared across models.

Define \`p_N=ceil(122/P)\`, \`p_R=ceil(48/P)\`, and \`B\` the physical allocation-bitmap remote pages already issued (global or segmented). The exact **conditional** kept remote page count after GC under the reference's no-reuse, fixed-stride grammar is:

\[
K = \left|\bigcup_{e\in E\cup\{L\}}R(e)\right|p_N
      +|E\cup\{L\}|p_R+B.
\]

The number of additional page images held **solely to keep historical PINs in addition to LATEST** is:

\[
\Delta_{\rm PIN}=K-\bigl(|R(L)|p_N+p_R+B\bigr).
\]

For PAGE-001 snapshots, with complete snapshot page cost \`p_S=ceil(ceil(n/8)/P)+ceil(48/P)\`, the corresponding values are \`K=|E union {L}|*p_S\` and \`\Delta_PIN=|E minus {L}|*p_S\`.

No assumed physical file extents, SSD erase counts, network frames, proof compression or live remote directory indexes are inserted into these formulas. In particular, **the bitmap page count B is a paid resident metadata cost but is not charged AGAIN per historical root**. An empty bitmap segment already allocated by the highwater remains a remote page under the model.

## Restricted path-injection upper bound

An elementary finite counting result strengthens the retention audit without requiring a new theorem. The accepted immutable COW reference builds exactly `2n-1` node IDs at setup and allocates exactly the root-to-leaf path of depth `d_i` at each SET, **including a no-op**. Its latest version uses `2n-1` distinct node IDs. Every historical node ID not used by latest must belong to the initial issue set or one of the finite update paths.

For the frozen three-SET trace (updates `0`, `min(1,n-1)`, `n-1`), letting `d_1,d_2,d_3` be the public balanced path lengths, the elementary upper bounds on **additional distinct PIN-retained COW node IDs** are:

- PIN epochs 0 and 2 retained over latest 3: `N_extra <= d_1+d_2+d_3` (conservative all-issue bound)
- Only epoch 2 retained over latest 3: `N_extra <= d_3` (only path 3 was newly allocated since epoch 2)
- No historical PIN: `N_extra = 0`

The inequalities follow directly from the immutable path-allocation injection; they are **not** information-theoretic lower bounds, do **not** account for root manifests/bitmap metadata, and do not establish that keeping old content can be done with that space under an adversarial unknown-future workload. Independent finite tests assert these bounds against the actual SHA-authenticated union, including the no-op path.

## Independent charged audit

[\`research/uct005_d1b2f1_pin_retention.py\`](../../research/uct005_d1b2f1_pin_retention.py) validates each historical PIN commitment against independently authenticated epoch slots; it verifies every visited COW node with the accepted reference's actual SHA256 node grammar, and charges the complete aligned pages fetched for each epoch/root walk. Bitmap segment/page reads are separately charged, including zero-filled issued segments. For snapshots, it charges the packed payload + full manifest page images, recomputes epoch/root digest and validates the remote manifest.

For each offline COW audit pass, the implementation additionally checks the exact equality between the source counters and the paid distinct node/root/bitmap page images. Its aggregate padded remote reply size is exactly `P*(audited_node_page_reads + audited_root_page_reads + audited_bitmap_page_reads)`; each authenticated node/root record uses an 8-byte public locator, each bitmap page a 9-byte namespace/segment locator. These are **offline charged request/response diagnostics**, not additional online F1 queries. The Snapshot counterpart charges the actual full packed-data+manifest page images and 8-byte epoch-slot requests. Independent tests enforce complete-page byte conservation.

Every additional scan and hash appears in a separately identified \`retention_audit_*\` ledger, *not* in the source's normal \`query_*\`, \`set_*\` or \`gc_*\` counters. Cached Python node dictionaries are only the simulated fixed-location untrusted remote pages, not paid trusted indexing. The oracle additionally reports a naive **8 bytes per enumerated node ID** fixed-width list diagnostic, expressly **not** Python heap consumption or an algorithm-independent space lower bound.

After a two-reader identical three-SET transcript (\`e2\` no-op), it checks the authenticated K prediction against the model's actually retained physical image pages through three GC passes: PIN0+PIN2; after UNPIN0; and after UNPIN2. Distinct protected roots must remain, unpinned root/node records become reclaimable, and the actual page-count drop must equal the collector's reported **logical** freed pages. The first GC may reclaim unpinned e1. These are **not** actual SSD TRIM or atomic durability results.

## Negative tests and limits

The independently named tests iterate all \`2^n\` initial binary words for \`1<=n<=5\` and \`P in {1,2,64}\`, plus boundary cases \`n=33,P=2\` and \`n=257,P=4096\`. They verify same reader/PIN history, parity, duplicate PINs on one epoch, root-sharing, immutable remote page counts and protected GC retention. Missing or modified authenticated COW root and node images **ABORT**, rather than allowing an apparently free pin removal. Extra audit scans must not mutate already priced online F1 source counters.

**STOP:** The new \`offline_audit.incremental_PIN_remote_pages_over_latest\` diagnostic is **not** silently copied into D1-B2-F's full \`pinned_retained_pages\` axis, because that would misrepresent the executable online cost, peak trusted GC scratch and globally linearizable authority/durability contract. UCT root remains \`OPEN_UNPROVED\`.
