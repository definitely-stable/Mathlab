# DAG-002 G2-B2-B — SEA 2025 power-based anchor construction on Felsner chains

**Owner:** [#326](https://github.com/definitely-stable/Mathlab/issues/326). Depends on Felsner G2-B2-A [#329](https://github.com/definitely-stable/Mathlab/pull/329). Primary: [Bulteau, David, Horn, Tran-Girard, SEA 2025, Definition 8 / Strategy 2 / Lemma 9](https://drops.dagstuhl.de/storage/00lipics/lipics-vol338-sea2025/html/LIPIcs.SEA.2025.9/LIPIcs.SEA.2025.9.html).

**Evidence status:** CLASSICAL_SOURCE_DEFINITION_REPRODUCTION / FINITE_MODEL_GATE / ORIGINAL_RANK_CONVENTION_AUDIT / PHYSICAL_COST_UNMODELED / NO_NOVEL_THEOREM.

## Source-exact definitions

- rank(v) equals the number of ancestors of v **including v** under reflexive path reachability; a source therefore has rank 1.
- lp(v) is an incoming parent maximizing rank (deterministically smallest ID on ties), or null for a source; rank(null)=0.
- For integer B >= 2, pi_B(v) is the largest integer pi >= 0 for which there is a **positive integer x** satisfying rank(lp(v)) < x * B^pi <= rank(v). Equivalently, floor(rank(v)/B^pi) > floor(rank(lp(v))/B^pi). Never use floating-point logarithms or a crossing test with equality on both ends.
- AL(v) starts with v followed by the AL of its selected anchor; the selected anchor is the **first** element of AL(lp(v)) having pi_B(anchor) >= pi_B(v). If none qualifies, choose null. Do not search other parents or all ancestors.
- Immutable restricted top label for v contains the maximal ID on each Felsner chain among vertices in Anc(v) \ Anc(anchor(v)). A query walks its immutable target anchor records until its source chain appears, then compares source ID to the recovered top; it never loads the unpriced updater ancestor bitsets.

This is the actual **FELSNER + POWER** logical index and not FIRST_COMPATIBLE + RECORD. However it is **not** an honest production or physically priced page implementation because the updater stores complete previous ancestor bitsets and chain-family data in local RAM without remote read/write prices. This is visible as an explicit n² unpriced oracle bits diagnostic.

## Lemma 9 and a potential source convention issue

The paper states (a) |R_v^anchor(v)| <= B^(pi_B(v)+1), and (b) an O(B log(rank(v))) bound on anchor depth, printed as ad(v) <= B floor(log(rank(v))). Part (a) is checked on each finite model and from the original source. Part (b) needs a separate source-convention check: the paper defines ad(v)=length(AL(v)), so source v has rank(v)=1 and ad(v)=1, but B floor(log_B(1))=0. Its proof calls ad(v)=0 at the base case. Thus the **literal bound is inconsistent with the earlier inclusive-length definition for sources**; do not silently change a definition or assert that version of part (b). An adjusted off-by-one form may hold; proving/quoting it requires an independently documented fix.

Do not falsely label this as a new counterexample to the **asymptotic** logarithmic depth result. It is a boundary convention issue in the printed exact inequality.

## Source reproducibility and tests

Six independent stdlib tests:
- All 1024 ordered 5-vertex DAGs, with B=2,3,4, all 5 prefixes, all source/target reachability queries (3072 trace-index instances, 168960 queries).
- All ranks and integer power crossings against brute-force positive multiples, for B=2,3,4,10 and low/high rank ranges.
- Reproduce the paper's illustrative length-2302 base-10 path and test the powers of ranks 2000 and 2300, representative queries and restricted ancestor counts.
- Source rank-one/depth-one convention explicitly tested rather than assuming zero.
- Multi-parent, invalid input, immutable record and Felsner-family invariants.

Commands:

    python research/dag002_g2b2_power_anchors.py
    python -m unittest discover -s research -p 'test_dag002_g2b2_power_anchors.py' -v

Require exact-head GitHub-hosted focused CI and complete hosted Research CI before any merge. This branch is intentionally **stacked on Felsner #329**, not independently mergeable into main until that dependency passes. No machine benchmark, network/disk I/O, proofs of original high-probability SEA record strategy, authenticated history/PIN/GC or novel Mathlab lower bound is claimed.

## Next allowed slice G2-B2-C: same-cost index comparison

Unify serialized first-compatible record, Felsner record and Felsner power **including** complete rank/ancestor support, mutable F_i manifest and chain memberships, page allocation and layout, updater reads/writes, repeated-query cache, page request headers, parent incidence input, RAM envelope. Compare to G1-C2-C bitmap and lazy adjacency with a single serializer and independent query correctness. If an unpriced oracle remains, report it separately and do not claim physical dominance. Then conduct typed novelty STOP gate G2-C.
