"""Independent exact falsifiers for D6-I weighted Hall port cuts."""
import unittest
from random import Random

from hyp105_issue230_d6i_uniform_port_hall import (
    positive_port_degrees,
    source_closed_port_profile,
    uniform_port_hall_cut,
    uniform_port_zero_exception_capacity,
    finite_w32_port_report,
)
from hyp105_issue230_d6f_exception_budget_oracle import (
    exception_budget_for_capacity,
)
from hyp105_issue230_d6h_incidence_budget_certificate import (
    incidence_budget_certificate,
)


def direct_subset_oracle(weights, targets, K):
    """Enumerate EVERY subset of original source triples: NO maxflow reuse."""
    triple_list = sorted(weights)
    best = 0
    maximisers = []
    for mask in range(1 << len(triple_list)):
        chosen = [triple_list[i] for i in range(len(triple_list))
                  if mask & (1 << i)]
        F = set(e for t in chosen for e in t)
        mass = sum(weights[t] for t in chosen)
        # Independent target-first direct incidence intersection count:
        # do not use the library's Counter degrees, cut, or closed profile.
        ports = sum(len(F.intersection(q)) for q in targets)
        value = 6 * mass - K * ports
        if value > best:
            best = value
            maximisers = [F]
        elif value == best:
            maximisers.append(F)
    return best, maximisers


def direct_uniform_minimum_K(weights, targets):
    """Independent exact rational max ratio over all source subsets."""
    triples = sorted(weights)
    if not triples:
        return 0
    minimum = 0
    for mask in range(1, 1 << len(triples)):
        selected = [triples[i] for i in range(len(triples)) if mask & (1 << i)]
        F = {e for t in selected for e in t}
        ports = sum(len(F.intersection(q)) for q in targets)
        mass = sum(weights[t] for t in selected)
        if not ports:
            return None
        minimum = max(minimum, (6 * mass + ports - 1) // ports)
    return minimum


class UniformPortHallTests(unittest.TestCase):
    def test_universal_exact_dual_against_subset_enumeration(self):
        rng = Random(230681)
        for i in range(72):
            source = {}
            while len(source) < 2 + i % 3:
                triple = tuple(sorted(rng.sample(range(17), 3)))
                source[triple] = 1 + rng.randrange(3)
            targets = {}
            while len(targets) < 1 + i % 4:
                q = tuple(sorted(rng.sample(range(17), 6)))
                targets[q] = "D6"
            direct_minimum_K = direct_uniform_minimum_K(source, targets)
            solver_minimum = uniform_port_zero_exception_capacity(source, targets)
            self.assertEqual(
                solver_minimum["uniform_minimum_K"], direct_minimum_K)
            for K in (0, 1, 2, 3, 6):
                with self.subTest(i=i, K=K):
                    row = uniform_port_hall_cut(source, targets, K)
                    brute, _ = direct_subset_oracle(source, targets, K)
                    self.assertEqual(
                        row["exact_uniform_scaled_Hall_deficit_Delta6"], brute)
                    self.assertEqual(
                        row["mincut"]["six_M_minus_K_D"], brute)
                    F = set(row["mincut"][
                        "source_closed_original_incidence_support_F"])
                    mass = sum(w for t, w in source.items() if set(t) <= F)
                    ports = sum(len(F.intersection(q)) for q in targets)
                    self.assertEqual(6 * mass - K * ports, brute)
                    self.assertEqual(
                        row["original_D6F_integer_exception_upper_floor_Delta6_div6"],
                        brute // 6)
                    original = exception_budget_for_capacity(source, targets, K)
                    old = incidence_budget_certificate(source, targets, K)
                    self.assertLessEqual(
                        original["minimal_exception_mass"], brute // 6)
                    self.assertEqual(
                        old["uniform"]["certified_integer_exception_upper"],
                        brute // 6)

    def test_active_source_closure_eliminates_inert_incidence_ids(self):
        source = {(0, 1, 2): 4, (2, 3, 4): 2}
        targets = {(0, 4, 5, 6, 7, 8): "D6",
                   (2, 7, 8, 9, 10, 11): "B/B-overlap"}
        a = source_closed_port_profile(source, targets, [0, 1, 2], candidate_K=1)
        b = source_closed_port_profile(source, targets, [0, 1, 2, 888, 999],
                                       candidate_K=1)
        self.assertEqual(a["oriented_source_mass_M"], 4)
        self.assertEqual(a["positive_port_degree_sum_D"], 2)
        self.assertEqual(a["signed_scaled_Hall_deficit"], 22)
        self.assertEqual(a["positive_scaled_Hall_deficit"],
                         b["positive_scaled_Hall_deficit"])
        self.assertEqual(a["original_active_incidence_support"],
                         b["original_active_incidence_support"])

    def test_endpoint_internal_shared_port_budget_and_unsupported(self):
        source = {(0, 1, 2): 3, (2, 3, 4): 2}
        split = {"endpoint": {(0, 1, 2): 2, (2, 3, 4): 1},
                 "internal": {(0, 1, 2): 1, (2, 3, 4): 1}}
        targets = {(0, 2, 4, 5, 6, 7): "D6"}
        F = [0, 1, 2, 3, 4]
        profile = source_closed_port_profile(source, targets, F, split,
                                             candidate_K=4)
        self.assertEqual(profile["split_oriented_source_mass"],
                         {"endpoint": 3, "internal": 2})
        self.assertEqual(profile["positive_port_degree_sum_D"], 3)
        self.assertEqual(profile["signed_scaled_Hall_deficit"], 18)
        row = uniform_port_hall_cut(source, targets, 4, split)
        self.assertEqual(row["exact_uniform_scaled_Hall_deficit_Delta6"], 18)
        self.assertEqual(row[
            "original_D6F_integer_exception_upper_floor_Delta6_div6"], 3)
        self.assertEqual(
            uniform_port_zero_exception_capacity(
                {(12, 13, 14): 9}, targets)["uniform_minimum_K"], None)
        self.assertEqual(
            uniform_port_zero_exception_capacity(
                {}, targets)["uniform_minimum_K"], 0)
        self.assertEqual(uniform_port_hall_cut({}, targets, 9)[
            "exact_uniform_scaled_Hall_deficit_Delta6"], 0)
        with self.assertRaises(ValueError):
            uniform_port_hall_cut(source, targets, -1)
        with self.assertRaises(ValueError):
            source_closed_port_profile(source, targets, [0, -1])

    def test_arbitrary_precision_all_h_integer_ratio(self):
        huge = 10**80 + 5
        source = {(0, 1, 2): huge}
        target = {(0, 3, 4, 5, 6, 7): "D6"}
        # Every source uses the same single supported port.
        # Restriction assigns K/6 capacity to that port.
        expected = 6 * huge
        self.assertEqual(
            uniform_port_zero_exception_capacity(
                source, target)["uniform_minimum_K"], expected)
        self.assertEqual(
            source_closed_port_profile(
                source, target, [0, 1, 2])["exact_port_capacity_floor_K"],
            expected)
        row = uniform_port_hall_cut(source, target, expected - 1)
        self.assertEqual(row["exact_uniform_scaled_Hall_deficit_Delta6"], 1)
        self.assertEqual(
            row["original_D6F_integer_exception_upper_floor_Delta6_div6"], 0)
        # A fractional deficiency smaller than 1 can be closed by
        # integral full D6-D flow; floor is essential, NOT ceil.
        self.assertEqual(
            exception_budget_for_capacity(source, target, expected - 1)[
                "minimal_exception_mass"], 0)

    def test_true_W32_complete_seven_independent_capacity_comparison(self):
        data = finite_w32_port_report()
        self.assertEqual(data["all_h_uniform_K"], "OPEN")
        self.assertEqual(data["W34_W38_full_positive_seven_S"],
                         "UNKNOWN-NO-BB-SUBSTITUTION")
        expected = {
            "lex": (942, 786, 156, 259, 4, 165),
            "reverse": (898, 676, 222, 169, 6, 53),
            "S68": (606, 544, 62, 68, 9, 62),
            "S72": (658, 600, 58, 72, 10, 10),
        }
        rows = data["genuine_W32_complete_seven_cases"]
        self.assertEqual(len(rows), 4)
        for row in rows:
            C, E, I, S, K, deficiency = expected[row["scheme"]]
            self.assertEqual(
                (row["C"], row["E"], row["I"], row["S"]), (C, E, I, S))
            self.assertEqual(row["D6D_exact_full_original_minimum_K"], K)
            self.assertEqual(row["D6I_uniform_restricted_minimum_K"], K)
            self.assertEqual(row["uniform_K_extra_over_full_original_K"], 0)
            self.assertEqual(
                [(z["K"], z["D6F_exact_exception"],
                  z["D6H_uniform_exception_upper"])
                 for z in row["capacity_cases"]],
                [(K-1, deficiency, deficiency), (K, 0, 0)])
            for point in row["capacity_cases"]:
                cut = point["port_cut"]
                self.assertEqual(
                    cut["mincut"]["six_M_minus_K_D"],
                    cut["exact_uniform_scaled_Hall_deficit_Delta6"])


if __name__ == "__main__":
    unittest.main()
