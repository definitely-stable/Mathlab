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

    def test_g3b2b_stays_upper_only_and_root_open(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        self.assertEqual(nodes["UCT005G3B2B"]["kind"], "research_input")
        self.assertIn("NO_NEW_LOWER_BOUND", nodes["UCT005G3B2B"]["status"])
        self.assertIn({"parent": "UCT005G3B", "child": "UCT005G3B2B",
                       "relation": "UPPER_CONSTRUCTIONS_NOT_LOWER_BOUND"},
                      self.data["edges"])
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_g3b2c0_is_restricted_cost_model_not_root_proof(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        self.assertEqual(nodes["UCT005G3B2C0"]["kind"], "research_input")
        self.assertIn("NO_ORIGINAL_LOWER_BOUND",
                      nodes["UCT005G3B2C0"]["status"])
        self.assertIn({"parent": "UCT005G3B2B", "child": "UCT005G3B2C0",
                       "relation": "COST_MODEL_AND_COUNTEREXAMPLES_NOT_ROOT_PROOF"},
                      self.data["edges"])
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_g3b2c1_does_not_promote_gc_to_original_uct(self):
        nodes = {node["id"]: node for node in self.data["nodes"]}
        node = nodes["UCT005G3B2C1"]
        self.assertEqual(node["kind"], "research_input")
        self.assertIn("REJECTED_FALSE_JOINT_LOWER_BOUND", node["status"])
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")
        self.assertIn(
            {"parent": "UCT005G3B2C0", "child": "UCT005G3B2C1",
             "relation": "RETENTION_COST_AND_FALSE_CONJECTURE_NOT_ROOT_PROOF"},
            self.data["edges"],
        )

    def test_g3b2c2a_is_bounded_gc_not_new_uct_theorem(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        node = nodes["UCT005G3B2C2A"]
        self.assertEqual(node["kind"], "research_input")
        self.assertIn("NO_NEW_LOWER_BOUND", node["status"])
        self.assertIn(
            {"parent": "UCT005G3B2C1", "child": "UCT005G3B2C2A",
             "relation": "BOUNDED_PAGE_BUFFER_MODEL_NOT_ORIGINAL_THEOREM"},
            self.data["edges"],
        )
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_g3b2c2b1_is_ideal_fence_only_no_real_crash_proof(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        node = nodes["UCT005G3B2C2B1"]
        self.assertEqual(node["kind"], "research_input")
        self.assertIn("NO_POWERLOSS_PROOF", node["status"])
        self.assertIn("NO_NEW_LOWER_BOUND", node["status"])
        self.assertIn(
            {"parent": "UCT005G3B2C2A", "child": "UCT005G3B2C2B1",
             "relation": "IDEAL_FENCE_MODEL_NOT_END_TO_END_GC_PROOF"},
            self.data["edges"],
        )
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_g3b2c2b2a_is_fenced_upper_not_root_lower_bound(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        node = nodes["UCT005G3B2C2B2A"]
        self.assertEqual(node["kind"], "research_input")
        self.assertIn("NO_NEW_LOWER_BOUND", node["status"])
        self.assertIn("NO_END_TO_END_DURABILITY", node["status"])
        self.assertIn(
            {"parent": "UCT005G3B2C2B1", "child": "UCT005G3B2C2B2A",
             "relation": "FILE_BUFFERED_CONTROL_JOIN_NOT_ORIGINAL_THEOREM"},
            self.data["edges"],
        )
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_g3b2c2b2b_is_only_scoped_cow_upper_with_stale_gc_gate(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        entry = nodes["UCT005G3B2C2B2B"]
        self.assertEqual(entry["kind"], "research_input")
        self.assertIn("NO_REAL_DURABILITY", entry["status"])
        self.assertIn("NO_NEW_LOWER_BOUND", entry["status"])
        self.assertIn(
            {"parent": "UCT005G3B2C2B2A", "child": "UCT005G3B2C2B2B",
             "relation": "ROOT_PUBLICATION_UPPER_AND_EXPLICIT_NONCOMPOSITION"},
            self.data["edges"],
        )
        self.assertEqual(self.data["root_novelty"], "OPEN_UNPROVED")

    def test_no_unsound_logical_arrows(self):
        relations = {e["relation"] for e in self.data["edges"]}
        self.assertIn("THREAT_MODEL_NONTRANSFER", relations)
        self.assertIn("APPLICATION_ONLY", relations)
        self.assertIn("INDEPENDENT_OPEN", relations)
        self.assertNotIn("THEOREM_IMPLICATION", relations)
        self.assertIn("not a proof implication", self.data["edge_semantics"])

if __name__ == "__main__":
    unittest.main()
