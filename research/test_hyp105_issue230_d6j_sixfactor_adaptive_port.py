"""D6-J independent brute force and true original GF5-positive W32 falsifiers."""
from random import Random
import unittest

from hyp105_issue230_d6j_sixfactor_adaptive_port import (
    adaptive_original_port_certificate,
    sharp_six_factor_capacity_frontier,
    genuine_W32_six_factor_report,
)
from hyp105_issue230_d6f_exception_budget_oracle import (
    exception_budget_for_capacity,
)
from hyp105_issue230_d6i_uniform_port_hall import uniform_port_hall_cut


def independent_exhaustive_unassigned(source_weights, accepted, K):
    """Enumerate individual source-to-recipient assignments, NO flow solver."""
    units = [t for t, w in source_weights.items() for _ in range(w)]
    targets = sorted(accepted)
    if len(units) > 8 or len(targets) > 3:
        raise AssertionError("small synthetic oracle only")
    nbr = [tuple(i for i, q in enumerate(targets)
                 if set(t).intersection(q)) for t in units]
    best = len(units)
    loads = [0] * len(targets)

    def dfs(i, dropped):
        nonlocal best
        if dropped >= best:
            return
        if i == len(units):
            best = dropped
            return
        dfs(i+1, dropped+1)
        for j in nbr[i]:
            if loads[j] < K:
                loads[j] += 1
                dfs(i+1, dropped)
                loads[j] -= 1

    dfs(0, 0)
    return best


class SharpSixFactorAdaptiveOriginalPortTests(unittest.TestCase):
    def verify_primal(self, src, sixsets, row, K):
        primal = row["adaptive_primal"]
        assignment = primal["per_source_port_assignment"]
        allocation = primal["per_recipient_port_allocation"]
        source_account = {}
        into_e = {}
        out_e = {}
        out_q = {}
        for a in assignment:
            t = tuple(a["original_source_triple"])
            e = a["original_incidence"]
            value = a["routed_oriented_mass"]
            self.assertIn(e, t)
            self.assertGreater(value, 0)
            source_account[t] = source_account.get(t, 0) + value
            into_e[e] = into_e.get(e, 0) + value
        for a in allocation:
            q = tuple(a["original_sixset"])
            e = a["original_incidence"]
            value = a["allocated_integer_K_slots"]
            self.assertIn(q, sixsets)
            self.assertIn(e, q)
            self.assertGreater(value, 0)
            out_e[e] = out_e.get(e, 0) + value
            out_q[q] = out_q.get(q, 0) + value
        for t, routed in source_account.items():
            self.assertLessEqual(routed, src[t])
        self.assertEqual(into_e, out_e)
        self.assertTrue(all(w <= K for w in out_q.values()))
        self.assertEqual(sum(into_e.values()),
                         row["full_original_exact_integral_flow"])
        self.assertEqual(sum(out_q.values()),
                         row["full_original_exact_integral_flow"])
        self.assertEqual(
            primal["port_load_sum"], row["full_original_exact_integral_flow"])
        self.assertEqual(
            sorted([[e, w] for e, w in out_e.items()]),
            primal["per_port_capacities"])

    def test_independent_brute_small_adaptive_optimality(self):
        rng = Random(230691)
        for i in range(48):
            source = {}
            while len(source) < 2 + i % 2:
                t = tuple(sorted(rng.sample(range(16), 3)))
                source[t] = rng.randint(1, 2)
            sixsets = {}
            while len(sixsets) < 1 + i % 3:
                q = tuple(sorted(rng.sample(range(16), 6)))
                sixsets[q] = "D6"
            for K in (0, 1, 2, 3):
                with self.subTest(i=i, K=K):
                    exact = independent_exhaustive_unassigned(source, sixsets, K)
                    row = adaptive_original_port_certificate(source, sixsets, K)
                    self.assertEqual(
                        row["full_original_exact_integer_exception"], exact)
                    self.assertLessEqual(
                        row["uniform_exception_lower_at_6K"], exact)
                    self.assertGreaterEqual(
                        row["uniform_exception_upper_at_K"], exact)
                    self.verify_primal(source, sixsets, row, K)

    def test_six_factor_unimprovable_one_original_port(self):
        N = 17
        source = {(0, 1, 2): N}
        accepted = {(0, 3, 4, 5, 6, 7): "D6"}
        frontier = sharp_six_factor_capacity_frontier(source, accepted)
        self.assertEqual(frontier["full_original_K"], N)
        self.assertEqual(frontier["uniform_original_K"], 6 * N)
        for K in (0, 1, 5, 16, 17, 18):
            with self.subTest(K=K):
                row = adaptive_original_port_certificate(source, accepted, K)
                self.assertEqual(
                    row["full_original_exact_integer_exception"], max(0, N-K))
                self.assertEqual(
                    row["uniform_exception_lower_at_6K"], max(0, N-K))
                self.assertEqual(
                    row["uniform_exception_upper_at_K"], max(0, N-K//6))
                self.verify_primal(source, accepted, row, K)

    def test_joint_E_I_support_and_unsupported_original_targets(self):
        source = {(0, 1, 2): 3, (6, 7, 8): 2}
        accepted = {(0, 3, 4, 5, 9, 10): "D6"}
        split = {"endpoint": {(0, 1, 2): 2, (6, 7, 8): 1},
                 "internal": {(0, 1, 2): 1, (6, 7, 8): 1}}
        for K in (0, 1, 3, 8):
            row = adaptive_original_port_certificate(
                source, accepted, K, split)
            self.assertEqual(row["split_source_mass"],
                             {"endpoint": 3, "internal": 2})
            self.assertEqual(row["full_original_exact_integer_exception"],
                             2 + max(0, 3-K))
            self.verify_primal(source, accepted, row, K)
        front = sharp_six_factor_capacity_frontier(source, accepted, split)
        self.assertEqual(front["status"], "NO-FINITE-K-UNSUPPORTED-SOURCE")
        no_source = sharp_six_factor_capacity_frontier({}, accepted)
        self.assertEqual(no_source["status"], "EMPTY-SOURCE-NO-INFERENCE")
        with self.assertRaises(ValueError):
            adaptive_original_port_certificate(source, accepted, -1)

    def test_many_target_single_port_six_factor_extremal(self):
        source = {(0, 1, 2): 41}
        accepted = {
            (0, 3+5*j, 4+5*j, 5+5*j, 6+5*j, 7+5*j): "D6"
            for j in range(5)
        }
        frontier = sharp_six_factor_capacity_frontier(source, accepted)
        self.assertEqual(frontier["full_original_K"], 9)
        self.assertEqual(frontier["uniform_original_K"], 50)
        self.assertLessEqual(frontier["uniform_original_K"],
                             6*frontier["full_original_K"])
        self.assertEqual(frontier["at_full_K"][
            "full_original_exact_integer_exception"], 0)

    def test_actual_complete_W32_all_seven_vs_independent_D6F(self):
        report = genuine_W32_six_factor_report()
        self.assertEqual(report["all_h_fixed_K"], "OPEN")
        self.assertEqual(report["root_Branch_A_or_B"], "OPEN")
        self.assertEqual(report["W34_W38_full_seven_original_positive_S"],
                         "UNKNOWN-NO-BB-SUBSTITUTION")
        expected = {
            "lex": (942, 259, 786, 156, 4),
            "reverse": (898, 169, 676, 222, 6),
            "S68": (606, 68, 544, 62, 9),
            "S72": (658, 72, 600, 58, 10),
        }
        self.assertEqual(len(report["genuine_complete_seven_W32_cases"]), 4)
        for row in report["genuine_complete_seven_W32_cases"]:
            C,S,E,I,K=expected[row["scheme"]]
            self.assertEqual(
                (row["C"],row["S"],row["E"],row["I"]),(C,S,E,I))
            self.assertEqual(row["K_full"],K)
            self.assertEqual(row["K_uniform"],K)
            self.assertEqual(row["port_budget_used"],C)
            self.assertEqual(row["full_exact_exception_at_K_full"],0)
            self.assertEqual(row["six_factor_lower_upper_at_K_full"],[0,0])


if __name__ == "__main__":
    unittest.main()
