# UCT-005 D1-B2-F3-B — three upper constructions, one F1 transcript and partial Pareto STOP

2026-10-10. Parent [UCT-005 #105](https://github.com/definitely-stable/Mathlab/issues/105), scientific owner [D1 #223](https://github.com/definitely-stable/Mathlab/issues/223). The branch combines **unmerged research candidates** F2 [#283](https://github.com/definitely-stable/Mathlab/pull/283) and F3-A [#287](https://github.com/definitely-stable/Mathlab/pull/287) solely for gated experiments. Their acceptance is NOT inherited. F1 [#272](https://github.com/definitely-stable/Mathlab/pull/272), remote PIN [#253](https://github.com/definitely-stable/Mathlab/pull/253), segmented COW [#258](https://github.com/definitely-stable/Mathlab/pull/258), physical ledger [#265](https://github.com/definitely-stable/Mathlab/pull/265) are merged predecessors.

**Status: RESEARCH_INPUT / CONDITIONAL_SAME_F1_UPPER_COMPARISON / NOT_FULLY_PRICED / ROOT_OPEN_UNPROVED.** Does not prove a new joint information lower bound, real crash durability or implementation-independent Pareto theorem.

## One frozen physical F1 service transcript

Exactly the same binary initial state, page size P, bounded epoch capacity C, update positions (0,min(1,n-1),n-1), one no-op SET at epoch 2, PIN reader0 at epoch0, PIN reader1 at epoch2, independent LATEST/AS_OF range parity (every nonempty half-open interval for n<=6), then GC / UNPIN0 / GC / UNPIN2 / GC for all three upper constructions:

- Accepted remote **bulk** PIN bitmap plus immutable PAGE-001 whole snapshots;
- Pending F2 two-pass page-streamed authenticated remote PIN bitmap plus **identical** immutable PAGE-001 snapshots and remote staged updates;
- Accepted segmented node-allocation bitmap + immutable 122-byte COW nodes with independently authenticated SHA history audit (F1).

All snapshot PINs are authenticated against the actual remote bitmap and separately trusted client tokens, rather than the deliberately empty inherited trusted PIN registry. The COW reachability audit independently verifies full root/node SHA images. Every offline audit operation is charged; it is **not an online free history index**.

## Exact model-scoped ledger identities

Let B=ceil(2C/8), M=ceil(B/P), S=ceil(ceil(n/8)/P)+ceil(48/P), four PIN bitmap mutations (two PIN, two UNPIN), and three SETs. Then for the exact F2 implementation:

| Metric on this same transcript | Bulk remote PIN | Two-pass streamed PIN |
| --- | --- | --- |
| Online remote bitmap page reads | 7M | 11M |
| Additional F2 online bitmap page reads | — | 4M |
| PIN bitmap page writes / full-page staged uploads | 4M | 4M |
| Stage old-slot retirement controls | no double-slot protocol | 4M addressed DROP_PAGE requests, 32M request bytes |
| Bitmap scratch (specific buffer lifetime *upper*, not a lower) | chosen three-image 3B | at most 2 min(B,P) |
| Peak allocated remote page images, including two-slot stage | 3S+M | 3S+2M |
| Historical snapshot images after GC | (k+1)S+M | (k+1)S+M |

Here k is the number of **distinct** historical PIN epochs; for the frozen trace k=2,1,0 across the three stages. The time-independent shared COW subtree accounts for historical node-ID excess via the accepted F1 exact checkpoint-path-union identity, multiplied by ceil(122/P) and augmented by historical 48-byte root-slot pages. Its own bitmap allocations are counted separately, not multiplied by pinned roots.

**Offline test audit is not free:** for every stage the deliberately independent F2 auditor checks every one of C epoch memberships with a full SHA-rooted scan of M pages, hence exactly C M extra P-byte page reads, 8 C M address bytes, C trusted digest reads and C complete hash-input passes, plus full authenticated snapshot image/manifest/root reads. Across the three stages the separately paid remote bitmap diagnostic consumes 3CM page reads. The retained PIN epoch-list representation is disclosed as a fixed-u64-width diagnostic, **not** real Python heap bytes nor a total trusted memory bound. In particular the O(P) F2 bitmap scratch upper does NOT apply to this intentionally expensive audit.

Every claimed full bitmap page upload contains P physical bytes (including canonical padding), and all public fixed-address retired pages require 8-byte request locators. These counts do NOT include transport frames, SHA backend memory, process RSS, disk TRIM, wear leveling, fsync, crash-recovery barriers, dynamic table/code size or trusted anti-rollback infrastructure.

## Resource tradeoff and theorem firewall

For this *particular selected bulk three-buffer schedule*, the F2 streamed protocol has a smaller conceptual bitmap payload working set **but strictly more online page reads and an extra M remote staging pages at transient peak**. No all-axis Pareto winner follows; the assumed 3B bulk upper is not a universal scratch lower bound on bulk PIN algorithms. The output carries six explicitly unknown resource axes as `null` and sets `all_axis_pareto_order=null`. Mismatch, corruption or withheld bitmap, pinned snapshot or independently retained PIN token must abort. F2's crash-cut result remains conditional on durable full-page writes ordered before an ideal atomic trusted publication, not implementation-level crash safety.

## Independent finite verification and acceptance

[Reference comparator](../../research/uct005_d1b2f3b_three_model_pareto.py) and [independent tests](../../research/test_uct005_d1b2f3b_three_model_pareto.py) exhaust all GF(2) initial states for 1<=n<=5 and P=1,2,64, all specified query ranges, exact cost identities for C=8/17/257, dual-reader same-epoch PIN, remote corruption/missing snapshot/invalid manifest/token divergence, and negative resource-transfer claims. Reproduced by an additional GitHub-hosted workflow; full Research and INDEX CI on **exact final head**, followed by predecessor integration and post-merge main CI, are nonnegotiable. This stacked draft must not merge while #283 or #287 is unaccepted.

## Next research direction (not implemented by this comparator)

F3-C must choose a **single** same-model adversarial cost game including the independently paid trusted PIN authority, live temporal page retention and historical proof freshness under a specified horizon. Before conjecturing a joint inequality, compare exact prior-art lower bounds (Fredman–Saks, Pătraşcu–Demaine, BKV memory checking, SUNDR/COP and persistence) under identical assumptions, then kill universal formulas against the three concrete constructions here. Only a strict nonredundant quantitative improvement with a full source transfer could advance UCT-005 #105 beyond `OPEN_UNPROVED`.

## Theorem-tree parent invariant (hosted D1-A falsifier correction)

The repository's typed UCT-005 research hierarchy is a **rooted tree**: every non-root node has exactly **one** organizing parent. F3-B joins two *scientific* research inputs, but the hierarchy cannot encode both as two parent edges. The sole `UCT005G3B2D1B2F3B` tree parent is F2 `UCT005G3B2D1B2F2`; the accepted F3-A [#287](https://github.com/definitely-stable/Mathlab/pull/287) is instead an explicit prerequisite here and in the PR description. Neither edge is a mathematical proof implication. The first stacked HEAD was rejected by D1-A `test_unique_root_and_complete_tree` for incorrectly giving F3-B two tree parents, even though its focused three-model tests passed. The model registry has been corrected to one parent, and exact updated-head CI must pass.
