"""D6-H independent falsifiers for all-h sufficient incidence budgets."""
import unittest

from hyp105_issue230_d6h_incidence_budget_certificate import (
    incidence_budget_certificate, finite_w32_certificate_report,
)
from hyp105_issue230_d6f_exception_budget_oracle import (
    exception_budget_for_capacity,
)


def _independent_bruteforce_exception(source_weights, accepted, K):
    """Small ORIENTED unit-by-unit exhaustive assignment, not a flow solver."""
    units = [t for t, mass in source_weights.items() for _ in range(mass)]
    recipients = list(accepted)
    if len(units) > 9 or len(recipients) > 4:
        raise ValueError("only small synthetic exact oracle allowed")
    neighbors = [
        tuple(i for i, q in enumerate(recipients) if set(t) & set(q))
        for t in units
    ]
    best = len(units)
    loads = [0] * len(recipients)

    def rec(i, missing):
        nonlocal best
        if missing >= best:
            return
        if i == len(units):
            best = missing
            return
        rec(i + 1, missing + 1)
        for j in neighbors[i]:
            if loads[j] < K:
                loads[j] += 1
                rec(i + 1, missing)
                loads[j] -= 1

    rec(0, 0)
    return best


class IncidenceBudgetTests(unittest.TestCase):
    def check_certificate(self, sources, accepted, K, split=None):
        row = incidence_budget_certificate(sources, accepted, K, split)
        brute = _independent_bruteforce_exception(sources, accepted, K)
        exact = exception_budget_for_capacity(sources, accepted, K, split)
        self.assertEqual(exact["minimal_exception_mass"], brute)
        self.assertGreaterEqual(row["best_certified_exception_upper"], brute)
        self.assertGreaterEqual(
            row["uniform"]["certified_integer_exception_upper"], brute)
        self.assertGreaterEqual(
            row["uniform"]["equal_source_thirds_exception_upper"], brute)
        self.assertGreaterEqual(
            row["largest_load_orientation"]["certified_integer_exception_upper"],
            brute)
        self.assertGreaterEqual(
            row["greedy_remaining_load_orientation"]["certified_integer_exception_upper"],
            brute)
        self.assertEqual(row["source_incidence_load_sum"], 3 * sum(sources.values()))
        self.assertEqual(
            row["positive_target_incidence_degree_sum"], 6 * len(accepted))
        return row

    def test_independent_bruteforce_on_local_and_global_obstructions(self):
        q0 = (0, 6, 7, 8, 9, 10)
        q1 = (3, 11, 12, 13, 14, 15)
        source = {(0, 1, 2): 2, (3, 4, 5): 3}
        targets = {q0: "D6", q1: "B/B-overlap"}
        at_k3 = self.check_certificate(source, targets, 3)
        self.assertEqual(at_k3["best_certified_exception_upper"], 0)
        self.assertFalse(
            at_k3["uniform"]["pointwise_incidence_domination_holds"])
        self.assertGreater(
            at_k3["uniform"]["certified_integer_exception_upper"], 0)
        self.assertEqual(
            at_k3["largest_load_orientation"]["certified_integer_exception_upper"],
            0)
        for K in (0, 1, 2, 4):
            self.check_certificate(source, targets, K)

        # Only one of two positive recipients touches either source: local
        # Hall excess survives despite globally sufficient total capacity.
        local = {(0, 1, 2): 3, (0, 3, 4): 3}
        distractor = {
            (0, 1, 2, 3, 4, 5): "D6",
            (6, 7, 8, 9, 10, 11): "B/B-overlap",
        }
        for K in (1, 2, 3, 6):
            self.check_certificate(local, distractor, K)

    def test_irreducible_unsupported_and_zero_capacity(self):
        sources = {(0, 1, 2): 2, (20, 21, 22): 4}
        accepted = {(0, 3, 4, 5, 6, 7): "D6"}
        for K in (0, 1, 2, 6):
            row = self.check_certificate(sources, accepted, K)
            self.assertEqual(row["component_source_masses"]["total"], 6)
            self.assertEqual(row["source_incidences_without_positive_target"], 5)
        self.assertEqual(
            self.check_certificate(sources, accepted, 6)[
                "best_certified_exception_upper"], 4)
        self.check_certificate({}, accepted, 2)
        self.check_certificate(sources, {}, 1)

    def test_joint_endpoint_internal_pointwise_sufficient(self):
        sources = {(0, 1, 2): 2, (3, 4, 5): 3}
        accepted = {
            (0, 1, 2, 6, 7, 8): "D6",
            (3, 4, 5, 9, 10, 11): "D6",
        }
        split = {
            "endpoint": {(0, 1, 2): 1, (3, 4, 5): 2},
            "internal": {(0, 1, 2): 1, (3, 4, 5): 1},
        }
        # 2L(e)<=Kd(e) for every original source incidence at K=6.
        row = self.check_certificate(sources, accepted, 6, split)
        self.assertTrue(row["uniform"]["pointwise_incidence_domination_holds"])
        self.assertEqual(row["component_source_masses"], {
            "endpoint": 3, "internal": 2
        })
        self.assertEqual(row["best_certified_exception_upper"], 0)
        with self.assertRaises(ValueError):
            incidence_budget_certificate(
                sources, accepted, 6, {"endpoint": {(0, 1, 2): 1}})
        with self.assertRaises(ValueError):
            incidence_budget_certificate(sources, accepted, -1)

    def test_complete_original_W32_full_seven_exact_D6F_comparator(self):
        result = finite_w32_certificate_report()
        self.assertEqual(result["all_h_incidence_budget_upper_theorem"], "PROVED")
        self.assertEqual(result["all_h_uniform_K"], "OPEN")
        expected = {
            "lex": (942, 259, 4), "reverse": (898, 169, 6),
            "S68": (606, 68, 9), "S72": (658, 72, 10),
        }
        for row in result["W32_true_original_complete_seven_cases"]:
            C, S, K = expected[row["scheme"]]
            self.assertEqual((row["blocked_C"], row["true_original_complete_seven_S"],
                              row["D6D_optimal_K"]), (C, S, K))
            self.assertEqual(row["E"] + row["I"], C)
            for point in row["capacity_rows"]:
                cert = point["certificates"]
                self.assertGreaterEqual(
                    cert["best_certified_exception_upper"],
                    point["exact_D6F_exception"])
                self.assertEqual(
                    cert["component_source_masses"]["endpoint"] +
                    cert["component_source_masses"]["internal"], C)
                if point["K"] == K:
                    self.assertEqual(point["exact_D6F_exception"], 0)


if __name__ == "__main__":
    unittest.main()
