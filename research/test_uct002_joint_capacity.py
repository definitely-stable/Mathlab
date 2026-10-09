"""UCT-002 finite independent oracles: classical capacity, not general proof."""
from itertools import product
import json
from pathlib import Path
from math import comb, log2
import unittest


def volume_formula(q, m, radius):
    return sum(comb(m, j) * (q-1)**j
               for j in range(min(radius, m)+1))


def volume_bruteforce(q, m, radius):
    center = (0,) * m
    return sum(sum(a != b for a, b in zip(center, word)) <= radius
               for word in product(range(q), repeat=m))


def max_leaf_count(alphabet_size, depth):
    """Independent complete rooted s-ary tree recursion, worst-case leaves."""
    if depth == 0:
        return 1
    return sum(max_leaf_count(alphabet_size, depth-1)
               for _ in range(alphabet_size))


def binary_joint_service_states(n):
    """All x have public INDEX queries. Each query reads one external bit."""
    for x in product((0, 1), repeat=n):
        answers = tuple(x[i] for i in range(n))
        yield answers


class Uct002JointCapacityTests(unittest.TestCase):
    def test_exact_qary_ball_formula_for_all_small_codes(self):
        for q in (2, 3, 4):
            for m in range(5):
                for radius in range(m+2):
                    self.assertEqual(volume_formula(q, m, radius),
                                     volume_bruteforce(q, m, radius))

    def test_adaptive_leaf_count_does_not_exceed_probe_budget(self):
        for s in (2, 3, 4):
            for p in range(5):
                self.assertEqual(max_leaf_count(s, p), s**p)
                # At any node, replacing a subtree by an early leaf
                # only reduces the number of distinct observations.
                if p:
                    self.assertLessEqual(1 + (s-1)*s**(p-1), s**p)

    def test_sharp_star_saturates_joint_bound_with_charged_side_channels(self):
        center_code = (0, 0)
        candidate_codes = [(0, 0), (0, 1), (1, 0)]
        states = list(product(candidate_codes, (0, 1), (0, 1)))
        self.assertEqual(len(states), 12)
        self.assertEqual(len(set(states)), 12)
        center = (center_code, 0, 0)
        self.assertIn(center, states)
        # each center->leaf edge rewrites at most one code coordinate
        for code, helper, oracle in states:
            self.assertLessEqual(sum(a != b for a, b
                                     in zip(center_code, code)), 1)
        observed = [(tuple(code), helper, oracle) for code, helper, oracle in states]
        self.assertEqual(len(set(observed)), 12)
        self.assertEqual(len(states), volume_bruteforce(2, 2, 1)*2*2)

    def test_one_query_budget_does_not_apply_to_query_service(self):
        for n in range(2, 8):
            signatures = set(binary_joint_service_states(n))
            self.assertEqual(len(signatures), 2**n)
            self.assertGreater(len(signatures), 2)  # false shortcut P=1
            self.assertEqual(len(signatures), volume_formula(2, 0, 0)*2**n)

    def test_bounded_error_coarse_fano_noncontradiction(self):
        # A source with no code, no helper and no oracle transcript
        # can guess a uniform K-message identity with success 1/K.
        for k in range(2, 13):
            e = 1-1/k
            coarse_rhs = 1 + e*log2(k)
            self.assertLessEqual(log2(k), coarse_rhs + 1e-10)

    def test_typed_theorem_bricks_do_not_turn_analogies_into_proofs(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/research/UCT-002-THEOREM-BRICKS.json"
        d = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(d["schema"], "mathlab.uct002.theorem-bricks.v1")
        nodes = {n["id"]: n for n in d["nodes"]}
        self.assertEqual(len(nodes), len(d["nodes"]))
        self.assertEqual(nodes["MASTER-A"]["tier"], "DERIVED_CLASSICAL")
        self.assertEqual(nodes["MASTER-B"]["tier"], "DERIVED_CLASSICAL")
        self.assertEqual(nodes["FRONTIER-C"]["tier"], "CONJECTURE")
        valid_kinds = {"SPECIAL_CASE", "PROOF_INGREDIENT",
                       "PRIOR_ART_BARRIER", "ANALOGY_ONLY",
                       "FALSIFIER", "OPEN_REDUCTION"}
        for n in d["nodes"]:
            if n["source"].startswith("docs/"):
                self.assertTrue((root / n["source"]).is_file(), n["id"])
        for e in d["edges"]:
            self.assertIn(e["from"], nodes)
            self.assertIn(e["to"], nodes)
            self.assertIn(e["kind"], valid_kinds)
            self.assertGreater(len(e["condition"]), 18)
        self.assertTrue(any(e["kind"] == "SPECIAL_CASE" and
                            e["from"] == "MASTER-A" and e["to"] == "LENT"
                            for e in d["edges"]))
        self.assertTrue(all(e["kind"] != "SPECIAL_CASE"
                            for e in d["edges"] if e["from"] == "DELTAMETER"))

    def test_no_unpaid_state_dependent_old_root(self):
        # If any externally supplied perfect current ID is free,
        # m=b=P=0 can distinguish any number K; model assumption fails.
        for k in (2, 3, 8):
            legitimate_capacity = volume_formula(2, 0, 0)
            self.assertEqual(legitimate_capacity, 1)
            self.assertGreater(k, legitimate_capacity)
            # Charging ceil(log2 K) helper bits immediately permits K IDs.
            needed_bits = (k-1).bit_length()
            self.assertLessEqual(k, legitimate_capacity*(2**needed_bits))


if __name__ == "__main__":
    unittest.main()
