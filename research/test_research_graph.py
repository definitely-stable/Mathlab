"""Regression and adversarial gates for canonical research graph and AI retrieval."""
import copy
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from research_graph import (ROOT, CURATION, Graph, ingest, validate, neighbors,
                            impact, search, export, read, POLICY)


class GraphIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = ingest()
        cls.summary = validate(cls.graph)

    def test_canonical_coverage_without_snapshot_cardinality_freeze(self):
        self.assertIn("T:UCT005", self.graph.nodes)
        self.assertIn("P:LIT-355", self.graph.nodes)
        self.assertIn("R:ML-002", self.graph.nodes)
        self.assertIn("K:KR-001", self.graph.nodes)
        self.assertIn("B:G4-ATLAS", self.graph.nodes)
        self.assertGreaterEqual(self.summary["nodes"], 61 + 386 + 44 + 55)
        self.assertGreater(self.summary["chunks"], 100)

    def test_root_not_proved(self):
        self.assertEqual(self.graph.nodes["T:UCT005"]["status"], "OPEN_UNPROVED")
        self.assertEqual(self.summary["root_scientific_status"], "OPEN_UNPROVED")
        self.assertIn("No edge", POLICY)

    def test_cross_type_genealogy_has_scoped_nontransfer(self):
        matches = [e for e in self.graph.edges.values()
                   if e["from"] == "P:LIT-360" and e["to"] == "R:ML-002"]
        self.assertTrue(matches)
        self.assertEqual(matches[0]["qualifier"], "PROPOSED_TRANSFER_STOP")
        self.assertIn("non_implication", matches[0]["semantics"])

    def test_auto_markdown_literature_mentions_are_index_only(self):
        matches = [e for e in self.graph.edges.values()
                   if e["from"] == "DOC:docs/research/README.md"
                   and e["to"] == "P:LIT-349"
                   and e["relation"] == "TEXT_MENTIONS_ID"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["semantics"], "index_only")
        self.assertIn("AUTOMATIC_TEXT_MENTION_NOT_VERIFIED_CITATION",
                      matches[0]["qualifier"])
        self.assertEqual(matches[0]["evidence_path"], "docs/research/README.md")

    def test_paper_to_research_canonical_reverse_links(self):
        links = [e for e in self.graph.edges.values()
                 if e["relation"] == "MAPS_TO_RESEARCH"]
        self.assertGreater(len(links), 700)
        self.assertTrue(any(e["from"] == "P:LIT-001"
                            and e["to"] == "R:ML-002" for e in links))
        self.assertTrue(all(e["semantics"] == "model_overlap_non_implication"
                            for e in links))
        paper = neighbors(self.graph, "P:LIT-001", 1)
        self.assertIn("R:ML-002", {n["id"] for n in paper["nodes"]})

    def test_curated_issue_anchors_are_not_proofs(self):
        r = [e for e in self.graph.edges.values()
             if e["from"] == "ISSUE:105" and e["to"] == "T:UCT005"]
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]["relation"], "TRACKS_RESEARCH")
        self.assertIn("non_implication", r[0]["semantics"])

    def test_future_research_file_is_searchable_and_has_citation_backlink(self):
        # A brand-new Markdown file requires no frontmatter, ontology rewrite,
        # or hand-maintained graph node; canonical LIT IDs become index-only edges.
        with TemporaryDirectory(prefix="graph_future_", dir=ROOT / "docs/research") as path:
            new_file = Path(path) / "FUTURE-RESEARCH.md"
            new_file.write_text(
                "# Новая исследовательская работа\n\n"
                "This study discusses LIT-355 and bounded observability.\n",
                encoding="utf-8")
            rel = new_file.relative_to(ROOT).as_posix()
            graph = ingest()
            validate(graph)
            doc_id = "DOC:" + rel
            self.assertIn(doc_id, graph.nodes)
            matches = [e for e in graph.edges.values()
                       if e["from"] == doc_id and e["to"] == "P:LIT-355"
                       and e["relation"] == "TEXT_MENTIONS_ID"]
            self.assertEqual(len(matches), 1)
            self.assertTrue(any(c["path"] == rel and
                                "LIT-355" in c["text"] and
                                c["line_start"] <= 3 <= c["line_end"]
                                for c in graph.chunks))
            self.assertIn(doc_id, {node["id"] for node in
                                   neighbors(graph, "P:LIT-355", 1,
                                             direction="in",
                                             relations={"TEXT_MENTIONS_ID"},
                                             max_nodes=500)["nodes"]})

    def test_missing_canonical_local_source_is_an_error(self):
        original = Graph.doc
        def missing(graph, path):
            if path == "docs/research/LENT-001-FOUNDATION.md":
                return None
            return original(graph, path)
        with patch.object(Graph, "doc", missing):
            with self.assertRaisesRegex(ValueError, "source file missing"):
                ingest()

    def test_root_false_promotion_fails(self):
        g = copy.copy(self.graph)
        g.nodes = dict(self.graph.nodes)
        g.nodes["T:UCT005"] = dict(g.nodes["T:UCT005"], status="PROVED")
        with self.assertRaisesRegex(ValueError, "root promoted"):
            validate(g)

    def test_forced_organization_cycle_fails(self):
        g = copy.copy(self.graph)
        g.edges = dict(self.graph.edges)
        last = next(e for e in g.edges.values()
                    if e["relation"] == "ORG_TREE" and e["from"] == "T:UCT005")
        fake = dict(last, id="E:forged-cycle",
                    **{"from": last["to"], "to": "T:UCT005"})
        g.edges[fake["id"]] = fake
        with self.assertRaisesRegex(ValueError, "cyclic theorem"):
            validate(g)

    def test_invalid_relation_or_dangling_target_rejected(self):
        g = Graph()
        g.relations = read(CURATION)["relation_classes"]
        g.node("R:1", "internal_research", "test")
        with self.assertRaisesRegex(ValueError, "dangling"):
            g.edge("R:1", "R:missing", "CATALOG_RELATED",
                   source_path="docs/research/catalog/registry.json")
        g.node("R:2", "internal_research", "test 2")
        with self.assertRaisesRegex(ValueError, "unregistered"):
            g.edge("R:1", "R:2", "PROVES_UNIVERSAL_THEOREM",
                   source_path="docs/research/catalog/registry.json")

    def test_filtered_inbound_papers_only(self):
        neighborhood = neighbors(
            self.graph, "R:ML-002", 1, direction="in",
            relations={"MAPS_TO_RESEARCH"}, max_nodes=500)
        self.assertTrue(neighborhood["edges"])
        self.assertTrue(all(x["relation"] == "MAPS_TO_RESEARCH"
                            and x["to"] == "R:ML-002"
                            for x in neighborhood["edges"]))
        self.assertIn("P:LIT-001", {n["id"] for n in neighborhood["nodes"]})
        with self.assertRaisesRegex(ValueError, "unknown relation"):
            neighbors(self.graph, "R:ML-002",
                      relations={"PROVES_UNIVERSAL_THEOREM"})

    def test_paper_change_impact_paths_are_nonproof(self):
        result = impact(self.graph, "P:LIT-001", 2, 100)
        by_id = {x["id"]: x for x in result["affected"]}
        self.assertIn("R:ML-002", by_id)
        self.assertIn("R:ML-001", by_id)
        direct = by_id["R:ML-002"]
        self.assertEqual(direct["path"][0]["relation"], "MAPS_TO_RESEARCH")
        self.assertEqual(direct["path"][0]["grade"],
                         "CURATED_MODEL_OVERLAP_NOT_PROOF")
        self.assertIn("not theorem implications", result["semantics"])

    def test_reverse_text_mention_impact_is_not_verified_citation(self):
        result = impact(self.graph, "P:LIT-349", 1, 500)
        match = next(x for x in result["affected"]
                     if x["id"] == "DOC:docs/research/README.md")
        self.assertEqual(match["path"][0]["relation"], "TEXT_MENTIONS_ID")
        self.assertEqual(match["path"][0]["traversal"], "reverse")
        self.assertEqual(match["path"][0]["grade"], "UNVERIFIED_TEXT_MENTION")

    def test_impact_rejects_unscoped_source_and_unbounded_search(self):
        with self.assertRaisesRegex(ValueError, "impact source"):
            impact(self.graph, "TAG:signed-trades", 1)
        with self.assertRaisesRegex(ValueError, "depth"):
            impact(self.graph, "P:LIT-001", 10)
        with self.assertRaisesRegex(ValueError, "limit"):
            impact(self.graph, "P:LIT-001", 2, 0)

    def test_neighbor_reverse_lookup(self):
        n = neighbors(self.graph, "T:UCT005", 1)
        self.assertGreater(len(n["edges"]), 0)
        self.assertTrue(any(e["relation"] == "ORG_TREE" for e in n["edges"]))
        self.assertEqual(n["anchor"], "T:UCT005")

    def test_search_returns_publication_identity_and_source_verification(self):
        item = search(self.graph, "P:LIT-355", 1, "publication")["results"][0]
        self.assertEqual(item["id"], "P:LIT-355")
        self.assertTrue(item["identity"].startswith(("arxiv:", "doi:", "publisher:")))
        self.assertTrue(item["primary_url"].startswith("https://"))
        self.assertIn("full_proof_verified", item)
        self.assertIn("independent_reproduction", item)

    def test_search_bilingual_and_citation_pointers(self):
        for q in ("GF(5)", "authenticated", "PIN", "ASET"):
            results = search(self.graph, q, 7)
            self.assertTrue(results["results"], q)
            self.assertTrue(all(item.get("path") or item.get("provenance")
                                for item in results["results"]))
        exact = search(self.graph, "T:UCT005", 1)
        self.assertEqual(exact["results"][0]["id"], "T:UCT005")

    def test_russian_concept_alias_expands_to_documents(self):
        data = search(self.graph, "аутентифицированная наблюдаемость", 30)
        self.assertIn("authenticated-observability", data["expanded_concepts"])
        self.assertTrue(any(x["id"].startswith("DOC:") and
                            "UCT-005" in x.get("path", "")
                            for x in data["results"]))

    def test_retrieval_bundle_reproducible_and_bidirectional(self):
        with TemporaryDirectory() as a, TemporaryDirectory() as b:
            summary_a = export(self.graph, Path(a))
            summary_b = export(self.graph, Path(b))
            self.assertEqual(summary_a, summary_b)
            for name in ("graph.json", "graph.jsonld", "retrieval.jsonl",
                         "adjacency.json", "manifest.json", "coverage.json", "INDEX.md"):
                one = (Path(a) / name).read_bytes()
                two = (Path(b) / name).read_bytes()
                self.assertEqual(hashlib.sha256(one).digest(),
                                 hashlib.sha256(two).digest())
            ld = json.loads((Path(a) / "graph.jsonld").read_text("utf-8"))
            self.assertEqual(ld["@context"]["@version"], 1.1)
            iri_set = {item["@id"] for item in ld["@graph"]}
            self.assertEqual(len(iri_set), len(ld["@graph"]))
            for item in ld["@graph"]:
                if item.get("@type") == "mathlab:TypedRelation":
                    self.assertIn(item["mathlab:source"]["@id"], iri_set)
                    self.assertIn(item["mathlab:target"]["@id"], iri_set)
            manifest = json.loads((Path(a) / "manifest.json").read_text("utf-8"))
            self.assertIn("docs/research/catalog/literature.json", manifest["files"])
            coverage = json.loads((Path(a) / "coverage.json").read_text("utf-8"))
            self.assertEqual(coverage["unlinked_count"],
                             len(coverage["unlinked_markdown"]))
            self.assertGreaterEqual(self.summary["by_relation"]["MAPS_TO_RESEARCH"], 700)
            index = json.loads((Path(a) / "adjacency.json").read_text("utf-8"))
            self.assertTrue(index["inbound"].get("T:UCT005"))
            self.assertTrue(index["outbound"].get("T:UCT005"))


if __name__ == "__main__":
    unittest.main()
