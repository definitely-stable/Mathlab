# DAG-002 G2-B2-A — original Felsner up-growing online chain partition

**Owner:** [#326](https://github.com/definitely-stable/Mathlab/issues/326) / [#322](https://github.com/definitely-stable/Mathlab/issues/322), predecessor [#325](https://github.com/definitely-stable/Mathlab/pull/325).

**Classification:** EXISTING_THEOREM_REPRODUCTION / FINITE_EXACT_ORACLE / PHYSICAL_COST_UNMODELED / NO_NEW_THEOREM.

## Primary-source algorithm

1. [Felsner 1994, On-Line Chain Partitions of Orders](https://www.inf.fu-berlin.de/inst/pubs/tr-b-94-21.abstract.html), original up-growing upper/lower bound.
2. [Bosek et al., On-line Chain Partitions of Orders: A Survey, Theorem 3.5, pp. 6–7](https://piotrmicek.staff.tcs.uj.edu.pl/pubs/survey.pdf), exact short proof and implementable family exchange.
3. [Bulteau et al., Incremental Reachability Index, SEA 2025](https://doi.org/10.4230/LIPIcs.SEA.2025.9), existing LIT-187, its application to incremental immutable DAG reachability.

New vertices enter only as maximal points with predecessor/parent subset of old vertices. Maintain families F_1,F_2,... of disjoint chains; F_i contains at most i chains, and tops of its chains form an antichain. Find least j for which F_j has room or contains a chain whose top reaches the incoming x. If a compatible top exists, extend its chain (deterministic minimum-ID tie-break); else create a chain. For j>1 move whole chain IDs, never old vertices, using the exact published exchange

    F_(j-1)' = F_j minus {C}
    F_j'     = F_(j-1) union {C}

with newly created C treated as part of F_j before exchange. This preserves the chain-top antichain invariant. Classical theorem 3.5 guarantees W <= w(w+1)/2 chains for width w in the up-growing model. It does **not** guarantee that a first-compatible algorithm meets this bound.

## Finite independent verification

The source and seven Python unittest cases enumerate all 1024 topologically ordered 5-vertex DAGs and all 5120 insertion prefixes. An independently computed maximum antichain certifies exact width of every prefix; reachability is independently verified by backwards DFS. Check family top antichains, capacities, irrevocable chain assignments, old-old reachability, invalid parent commands, and source/chain/fan-in/layered 100-node workloads.

    python research/dag002_g2b2_felsner.py
    python -m unittest discover -s research -p 'test_dag002_g2b2_felsner.py' -v

Dedicated GitHub-hosted focused workflow must pass alongside the **entire full Research workflow** on exact PR head before merge. The code stores a complete ancestor-bitset oracle in memory; all its I/O, lookup and F_i manifest handling are **unpriced**. Its O(n²) reference state is explicitly exposed in the output. The number of compared chain heads is diagnostic only. This is NOT the physical index of SEA 2025, a byte-level benchmark, a cryptographic theorem or a new nonfactorizing DAG lower bound.

## Next scientific slice

SEA 2025 Section 3.2.2 power-based anchors: exact ancestor count rank, maximal-rank parent lp, largest crossed base-B power pi, first qualifying member of parent anchor list; independent Lemma 9 proof and base-case convention audit. Then integrate Felsner chains with anchors under common record/manifest serialization, counting all retained rank and ancestry support metadata, page read/write and query cost. Keep independent labels FIRST_COMPATIBLE vs FELSNER and RECORD vs POWER. No unsafe claim of published full algorithm performance before this cross-check.
