# Mathlab — internal research navigation

Curated **entry routes for AI agents**; not a second bibliography, proof ledger or real-time dashboard.

[Agent rules](../AGENTS.md) · [machine-readable graph](research/RESEARCH-MAP.json) · [Live GitHub status](STATUS-LIVE.md) · [historical current-state log](CURRENT_STATE.md) · [research chronology](research/README.md)

## Locate the authority

| Intent | Source |
| --- | --- |
| Current acceptance and CI | [STATUS-LIVE](STATUS-LIVE.md) then exact GitHub commit/PR/actions |
| Original or stopped claim | [KNOWN-AND-STOPPED JSON](research/KNOWN-AND-STOPPED-RESEARCH.json) |
| UCT-005 claim state | [UCT theorem tree](research/UCT-005-THEOREM-TREE.json) |
| Source, topic, bibliography | [Catalog](research/catalog/INDEX.md) · [literature](research/catalog/literature.json) · [relations](research/catalog/registry.json) |
| Code, Lean, evidence | [Executable research](../research/README.md) · [Lean](../lean/README.md) |

## Programs

### UCT-005

Joint information, authenticated history, updates and proof resources. [Root program](research/UCT-005-ROOT-THEOREM-PROGRAM.md) · [claim tree](research/UCT-005-THEOREM-TREE.json) · [scoped D1-C1 falsifiers](research/UCT-005-G3-B2-D1C1-HYPOTHESIS-KILL-GATE.md) · [root issue #105](https://github.com/definitely-stable/Mathlab/issues/105). **Root OPEN_UNPROVED**; restricted results never imply the combined lower bound.

### HYP-105

Finite geometry, GF(5) flow and six-motif construction/risk. [Weighted overlap model](research/HYP-105-G5-E2-B3-E1C0-WEIGHTED-OVERLAP-TRANSFER.md) · [issue #176](https://github.com/definitely-stable/Mathlab/issues/176) · [issue #230](https://github.com/definitely-stable/Mathlab/issues/230). Separate exact W32 enumerations, random averages, restricted all-h results and the unresolved global target.

### DAG-002 / ALG-001

Reachability/oracle complexity and online consistency. [Immutable DAG baseline](research/DAG-002-G0-IMMUTABLE-REACHABILITY.md) · [priced probe/write model](research/DAG-002-ALG-001-G1-A-PRICED-PROBE-WRITE-FRONTIER.md) · [online consistency](research/DAG-002-ALG-001-G1-C1-ONLINE-CONSISTENCY.md). Spell out preprocessing, adaptivity, writes, reads and offline knowledge.

### INDEX-001

Physical page cost, generations, WAL and checkpoint decisions. [Cost model / sources](research/INDEX-001-G2-A-PAGE-COST-AND-PRIOR-ART.md) · [page recourse](research/INDEX-001-G2-B4-B-PAGE-RECOURSE.md) · [bounded-space WAL](research/INDEX-001-G2-B4-C0-BOUNDED-SPACE-WAL.md). Charge pages, bytes moved, RAM, metadata and compaction.

### LENT-001

Exact additive sketches and hard support. [State-space baseline](research/LENT-001-FOUNDATION.md) · [GF5 finite certificate](research/LENT-001-G2B-B2-EXACT10-CERTIFICATE.md) · [known/STOP register](research/KNOWN-AND-STOPPED-RESEARCH.json). Counting baseline is classical; no claim of general novel trilemma.

### TKG-001 / graph memory

Bitemporal provenance, dynamic/temporal knowledge graphs and pangenome connections. [TKG model](research/TKG-001-G0-BITEMPORAL-PROVENANCE-AND-RECOURSE.md) · [2026 DAG/memory research](research/RESEARCH-LITERATURE-008-GRAPH-DAG-MEMORY-2026.md) · [DNA/pangenome](research/RESEARCH-LITERATURE-010-DNA-PANGENOME-BIOLOGICAL-GRAPH-MEMORY.md) · [cross-field genealogy](research/RESEARCH-LITERATURE-012-CROSS-DISCIPLINARY-ANCESTORS-DESCENDANTS.md). Related sources ≠ an exact theorem transfer.

### TOM-006 / HYP-101

Patch lower bounds and incremental hashing. [TOM-006 scope/kill gate](research/TOM-006-EARLY-KILL-GATE.md) · [HYP-101 literature audit](research/HYP-101-G0-INCREMENTAL-HASH-AUDIT.md). Toy models do not measure practical patch compression or justify hash-library changes.

## Cross-program search

Read the **exact research ID/claim**, then [catalog THEMES](research/catalog/THEMES.md) and [literature by research](research/catalog/LITERATURE-BY-RESEARCH.md). For speculative bridges follow [machine map](research/RESEARCH-MAP.json) `navigation_related` edges as **candidate directions only**. Before opening an issue, search [known/stopped](research/KNOWN-AND-STOPPED-RESEARCH.json).

## Update contract

Add nodes for **stable family entry points only**; do not duplicate every paper/PR or store changing HEAD, run status or numeric counts. Run `python research/validate_navigation.py` and check the exact commit CI.
