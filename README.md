# Mathlab

**Verification-first mathematical research workspace for humans and AI agents.** Mathlab studies, falsifies, links and — where justified — proves results across mathematics, algorithms and storage. This is an **internal research system first**, not a promotional website or a claim that every hypothesis is original.

> **Agent entry point:** [AGENTS.md](AGENTS.md) → [Research Index](docs/RESEARCH-INDEX.md) → [machine navigation map](docs/research/RESEARCH-MAP.json). Navigation pages are not proofs, acceptance records or live GitHub state.

## Task routing

| What you need | First source |
| --- | --- |
| Resume work, find current PR/CI | [Live navigation](docs/STATUS-LIVE.md), then GitHub exact HEAD/PR/checks |
| Find program, issue and entry artifacts | [Task-oriented index](docs/RESEARCH-INDEX.md) |
| Prevent re-discovering known or stopped work | [Machine no-repeat registry](docs/research/KNOWN-AND-STOPPED-RESEARCH.json) · [readable registry](docs/research/KNOWN-AND-STOPPED-RESEARCH.md) |
| Inspect literature, provenance and links | [Literature index](docs/research/catalog/INDEX.md) · [literature.json](docs/research/catalog/literature.json) · [registry.json](docs/research/catalog/registry.json) |
| Inspect UCT-005 root theorem claims | [Theorem tree](docs/research/UCT-005-THEOREM-TREE.json) · [root issue #105](https://github.com/definitely-stable/Mathlab/issues/105) |
| Inspect executable and formal evidence | [Research artifacts](docs/research/README.md) · [reference programs](research/README.md) · [Lean](lean/README.md) |

## Research tracks

| Family | Entry | Do not infer |
| --- | --- | --- |
| UCT-005 — observation, history, proof resources | [UCT-005](docs/RESEARCH-INDEX.md#uct-005) | Scoped lemmas do not establish the open root theorem |
| HYP-105 — finite geometry, GF(5), six-motifs | [HYP-105](docs/RESEARCH-INDEX.md#hyp-105) | Finite enumerations do not settle the global bound |
| DAG-002 / ALG-001 — reachability and oracle cost | [DAG-002 / ALG-001](docs/RESEARCH-INDEX.md#dag-002--alg-001) | Changed model assumptions invalidate transfer |
| INDEX-001 — page recourse, WAL, checkpointing | [INDEX-001](docs/RESEARCH-INDEX.md#index-001) | Logical bounds do not measure physical IO |
| LENT-001 — sparse additive sketches | [LENT-001](docs/RESEARCH-INDEX.md#lent-001) | Classical counting bounds are not novel |
| TKG-001, dynamic graphs, graph memory and DNA | [TKG-001 / graph memory](docs/RESEARCH-INDEX.md#tkg-001--graph-memory) | Analogy is not an equivalence theorem |
| TOM-006 / HYP-101 — patches, hashing | [TOM-006 / HYP-101](docs/RESEARCH-INDEX.md#tom-006--hyp-101) | Toy lower bounds do not imply product performance |

## Evidence and maintenance

1. Get HEAD and exact-head CI from **GitHub itself**. [STATUS-LIVE.md](docs/STATUS-LIVE.md) links to live evidence. [CURRENT_STATE.md](docs/CURRENT_STATE.md) records earlier slices and is **not current CI status**.
2. Distinguish literature, informal proof, Lean theorem, finite certificate, numerical evidence, open conjecture, counterexample and product gate.
3. Before claiming novelty, consult [known/stopped work](docs/research/KNOWN-AND-STOPPED-RESEARCH.json), exact primary literature and any explicit reopen condition.
4. Independent checking and honest quantifier/model scope are required. CI SUCCESS is not by itself mathematical correctness. Synthetic gains do not prove real-world improvements.
5. Update [the index](docs/RESEARCH-INDEX.md) for new *stable* research families only; do not copy every PR, inflate README with chronology or freeze SHA/CI/source counts.

See [decision history](docs/research/DECISIONS.md), [roadmap](docs/ROADMAP.md) and [publication-oriented material](preprints/README.md). The former long README is available in Git history.
