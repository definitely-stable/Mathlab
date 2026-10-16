"""Independent falsifiers for issue230's scoped analytic and quartic results."""
from collections import Counter
from fractions import Fraction
from importlib import import_module, util
from itertools import combinations, product
from math import prod
import random
import unittest


class Issue230ProofAuditTests(unittest.TestCase):
    def api(self):
        name = "hyp105_issue230_proof_audit"
        self.assertIsNotNone(util.find_spec(name), "issue230 proof implementation missing")
        return import_module(name)

    def test_exact_half_random_constant_and_centered_barrier(self):
        api = self.api()
        self.assertEqual(api.HALF_RANDOM_CONSTANT,
                         Fraction(180054835200, 13841287201))
        self.assertGreater(api.HALF_RANDOM_CONSTANT, 13)
        for s in (8, 16, 32, 128, 1024):
            row = api.analytic_certificate(s)
            self.assertGreater(row["expected_BA_lower"], 12*s**6)
            if s >= 32:
                self.assertLess(row["eta"], Fraction(1, 2))
                self.assertGreater(row["cs_error_to_mean_squared_lower"], 1)
            self.assertFalse(row["universal_S_lower_proved"])

    def test_invalid_geometry_orders_fail_closed(self):
        api = self.api()
        for s in (True, 0, 1, 3, -2, 2.0):
            with self.assertRaises(ValueError):
                api.analytic_certificate(s)

    def test_one_colored_square_has_no_orientation_factor(self):
        api = self.api()
        colors = (((0, 1),), ((1, 2),), ((2, 3),), ((0, 3),))
        row = api.colored_c4(colors, 4)
        self.assertEqual(row["simple_by_order"], (1, 0, 0))
        self.assertEqual(row["simple"], 1)

    def test_repeated_edge_closed_walks_are_not_source_witnesses(self):
        api = self.api()
        row = api.colored_c4(((((0, 1),)),)*4, 2)
        self.assertEqual(row["simple"], 0)
        self.assertEqual(row["walks_by_order"], (2, 2, 2))

    def test_colored_count_matches_direct_edge_assignment(self):
        api = self.api()
        rng = random.Random(230)
        palette = tuple(combinations(range(5), 2))
        for _ in range(30):
            colors = tuple(tuple(rng.sample(palette, rng.randint(0, 4)))
                           for _ in range(4))
            direct = 0
            for chosen in product(*colors):
                if len(set(chosen)) != 4:
                    continue
                degrees = Counter(x for edge in chosen for x in edge)
                direct += len(degrees) == 4 and set(degrees.values()) == {2}
            row = api.colored_c4(colors, 5)
            self.assertEqual(row["simple"], direct)
            for trace in row["walks_by_order"]:
                self.assertLessEqual(trace**2,
                                     16*prod(map(len, colors)))

    def test_complete_w32_quartic_source_matches_original_sixsets(self):
        api = self.api()
        from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
        for scheme in ("lex", "S68"):
            model = api.frozen_model(scheme)
            context = api.QuarticSource(model)
            expected = source_weighted_BA_hypergraph(model)
            actual = context.ledger()
            self.assertEqual(dict(actual), dict(expected))
            for R, weight in actual.items():
                self.assertLessEqual(weight, context.cap(R))
            with self.assertRaises(ValueError):
                context.weight((0, 0, 1, 2, 3, 4))

    def test_frozen_s68_refutes_both_exact_mean_strengthenings(self):
        api = self.api()
        row = api.finite_certificate("S68")
        self.assertEqual(row["seven_vector"], (0, 44, 21, 0, 0, 2, 1))
        self.assertEqual(row["source_mass"], 6098)
        self.assertEqual(row["dual_source_mass"], 4740)
        self.assertEqual(row["mu_f"], Fraction(12196, 143))
        self.assertEqual(row["P2_margin"], Fraction(-2901, 143))
        self.assertEqual(row["P7_margin"], Fraction(-2472, 143))
        self.assertEqual(row["Q7_GF5_floor_numerator"], 3112510)
        self.assertEqual(row["Q4"], 9)
        self.assertFalse(row["counterexample_B"])

    def test_actual_w34_w38_sharp_and_zero_global_source_maps(self):
        api = self.api()
        for power in (2, 3):
            for mode in ("sharp", "zero"):
                model, R = api.pencil_fixture(power, mode)
                context = api.QuarticSource(model)
                self.assertEqual(context.meeting_count(R), 1)
                wanted = (model["s"]+1)**2 if mode == "sharp" else 0
                self.assertEqual(context.weight(R), wanted)
                # Independently choose one actual source point on each residual line.
                p, rest = next(context.anchors(R))
                direct = 0
                for qs in product(*(context.lines[l] for l in rest)):
                    if len(set(qs)) != 4 or p in qs:
                        continue
                    edges = tuple(context.labels[q] for q in qs)
                    deg = Counter(x for edge in edges for x in edge)
                    direct += (len(deg) == 4 and set(deg.values()) == {2}
                               and not set(deg)&set(context.labels[p]))
                self.assertEqual(context.weight(R), direct)
                with self.assertRaises(ValueError):
                    context.ledger(max_sets=5005)

    def test_source_validation_rejects_duplicate_physical_labels(self):
        api = self.api()
        model = api.frozen_model("lex")
        labels = list(model["left_labels"])
        labels[1] = labels[0]
        model["left_labels"] = tuple(labels)
        with self.assertRaises(ValueError):
            api.QuarticSource(model)

    def test_source_validation_rejects_duplicate_incidences(self):
        api = self.api()
        model = api.frozen_model("lex")
        model["incidences"] += (model["incidences"][0],)
        with self.assertRaises(ValueError):
            api.QuarticSource(model)

    def test_regular_partial_linear_non_gq_is_rejected(self):
        api = self.api()
        model = api.frozen_model("lex")
        model["incidences"] = tuple((q, l) for l in range(15)
                                    for q in (l, (l+1)%15, (l+3)%15))
        with self.assertRaisesRegex(ValueError, "GQ projection axiom violated"):
            api.QuarticSource(model)

    def test_physical_palette_rejects_noncanonical_and_duplicate_edges(self):
        api = self.api()
        for edges in (((1, 0),), ((0, 0),), ((0, 4),), ((0, 1), (0, 1))):
            with self.assertRaises(ValueError):
                api.colored_c4((edges, (), (), ()), 4)

    def test_independent_original_and_permanent_oracles_replay_all_controls(self):
        name = "hyp105_issue230_independent"
        self.assertIsNotNone(util.find_spec(name), "independent source oracle missing")
        result = import_module(name).report()
        rows = {row["name"]: row for row in result["records"]}
        self.assertEqual(rows["lex"]["seven_vector"], [15, 98, 110, 13, 1, 8, 14])
        self.assertEqual(rows["reverse"]["S"], 169)
        self.assertEqual(rows["old_S68"]["source_mass"], 6098)
        self.assertEqual(rows["old_S68"]["S"], 68)
        self.assertEqual(rows["old_S68"]["P7_margin"], "-2472/143")


if __name__ == "__main__":
    unittest.main()
