# Mathlab: research and AI retrieval guide

Before making mathematical or bibliography claims, read
[graph indexing and provenance](docs/research/graph/README.md) and the
canonical [research catalog](docs/research/catalog/registry.json),
[literature catalog](docs/research/catalog/literature.json),
[theorem tree](docs/research/UCT-005-THEOREM-TREE.json),
[G4 typed bridges](docs/research/UCT-005-G4-TYPED-BRIDGES.json) and
[known/stopped register](docs/research/KNOWN-AND-STOPPED-RESEARCH.json).

## How to search the repository

Run from the repository root with Python 3 (stdlib only):

```sh
python research/research_graph.py validate
python research/research_graph.py search "GF5 signed trades" --limit 10
python research/research_graph.py neighbors P:LIT-355 --hops 1 --direction out --relation MAPS_TO_RESEARCH
python research/research_graph.py impact P:LIT-355 --depth 2
python research/research_graph.py build --out .work/research-graph
python research/research_graph_fts.py sync --jsonl .work/research-graph/retrieval.jsonl
python research/research_graph_fts.py search "historical PIN"
python research/research_graph_eval.py --check
```

The generated `graph.json`, `graph.jsonld`, `adjacency.json`,
`retrieval.jsonl`, `manifest.json`, `coverage.json` and SQLite FTS5
index are **derived caches**; never edit them as primary sources.

## Evidence and scientific safety

- A graph edge means a typed and sourced relationship, **not** theorem implication.
  In particular, `MAPS_TO_RESEARCH`, `TEXT_MENTIONS_ID`,
  `ORG_TREE`, `CATALOG_RELATED` and `SOURCE_GENEALOGY` do not prove a result.
- A search excerpt with path, line range and SHA-256 is a retrieval pointer,
  not independent proof verification. Follow it to the canonical file and
  pinned source revision; do not cite an invented SHA or CI run.
- UCT-005 central result is `OPEN_UNPROVED`. Finite-oracle success,
  source similarity and classical restricted lemmas do not establish a
  new joint asymptotic bound or novelty.
- Historical GitHub issue snapshots and CI metadata are not live. Check
  the exact PR HEAD and workflow run separately.
- Preserve negative findings, proof-model assumptions, non-implication
  and falsification criteria in all cross-study summaries.

## How to add a new study or paper

1. New research: allocate an unused ID in `docs/research/catalog/registry.json`,
   with scope, model, limitation, local or pinned cross-repo source, topics and
   only verifiable related links.
2. New paper: deduplicate DOI/arXiv/publisher identities against
   `docs/research/catalog/literature.json` and preserve all existing LIT IDs.
   A literature-to-research map is model overlap, not a theorem citation.
3. New Markdown under `docs/research/` is indexed automatically, including
   explicit references to existing canonical IDs. Add optional bilingual
   aliases, facet tags and issue anchors only in `docs/research/graph/curation.json`.
4. Run canonical validators plus graph tests, regenerate derived navigation,
   inspect evidence and GitHub-hosted CI. Do not merge or close a scientific
   issue based only on passing graph/search tests.
