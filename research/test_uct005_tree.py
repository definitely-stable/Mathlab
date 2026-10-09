"""UCT-005: typed research hierarchy metadata checks; NOT theorem proofs."""
import json
from collections import Counter, defaultdict
from pathlib import Path
import unittest

REPO = Path(__file__).resolve().parents[1]
DOC = REPO / "docs/research/UCT-005-THEOREM-TREE.json"

class Uct005TreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DOC.read_text(encoding="utf-8"))

    def test_unique_root_and_complete_tree(self):
        d = self.data
        self.assertEqual(d["schema"], "mathlab.uct005.theorem-tree.v1")
        self.assertEqual(d["root"], "UCT005")
        self.assertEqual(d["root_novelty"], "OPEN_UNPROVED")
        ids = [n["id"] for n in d["nodes"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn(d["root"], ids)
        children = Counter(e["child"] for e in d["edges"])
        self.assertNotIn(d["root"], children)
        self.assertEqual(set(children), set(ids) - {d["root"]})
        self.assertTrue(all(value == 1 for value in children.values()))
        adjacency = defaultdict(list)
        for edge in d["edges"]:
            self.assertIn(edge["parent"], ids)
            self.assertIn(edge["child"], ids)
            self.assertNotEqual(edge["parent"], edge["child"])
            adjacency[edge["parent"]].append(edge["child"])
        visited = set()
        def visit(node):
            self.assertNotIn(node, visited, "cycle or multiple routes")
            visited.add(node)
            for child in adjacency[node]:
                visit(child)
        visit(d["root"])
        self.assertEqual(visited, set(ids))

    def test_local_sources_exist_and_no_fake_novel_proofs(self):
        nodes = self.data["nodes"]
        for node in nodes:
            self.assertIn(node["kind"], {"root", "branch", "theorem_brick", "research_input"})
            self.assertNotIn(node["status"], {"PROVED_ORIGINAL", "WORLD_FIRST", "NOVEL_PROVED"})
            source = node["source"]
            if source.startswith("https://"):
                self.assertEqual(node["id"], "DELTAMETER")
            else:
                self.assertTrue((REPO / source).is_file(), f"missing source: {source}")
        self.assertEqual(next(n for n in nodes if n["id"] == "UCT005")["status"], "OPEN_UNPROVED")

    def test_g3a_is_foundational_not_promoted_to_original_root(self):
        d = self.data
        nodes = {n["id"]: n for n in d["nodes"]}
        self.assertEqual(nodes["UCT005G3A"]["kind"], "theorem_brick")
        self.assertIn("CLASSICAL", nodes["UCT005G3A"]["status"])
        self.assertIn("OPEN", nodes["UCT005G3B"]["status"])
        self.assertEqual(d["root_novelty"], "OPEN_UNPROVED")
        self.assertIn({"parent": "GEOMETRY", "child": "UCT005G3A",
                       "relation": "RESTRICTED_CLASSICAL_SPECIALIZATION_NOT_ROOT_PROOF"},
                      d["edges"])
        self.assertIn({"parent": "UCT005G3A", "child": "UCT005G3B",
                       "relation": "NOVELTY_PROBLEM_NOT_PROOF_IMPLICATION"},
                      d["edges"])

    def test_no_unsound_logical_arrows(self):
        relations = {e["relation"] for e in self.data["edges"]}
        self.assertIn("THREAT_MODEL_NONTRANSFER", relations)
        self.assertIn("APPLICATION_ONLY", relations)
        self.assertIn("INDEPENDENT_OPEN", relations)
        self.assertNotIn("THEOREM_IMPLICATION", relations)
        self.assertIn("not a proof implication", self.data["edge_semantics"])

if __name__ == "__main__":
    unittest.main()
