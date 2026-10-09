"""Independent proof-oriented checks of finite HYP-105 D_s joins."""
from itertools import combinations
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b1_energy import single_signed_trade_mitm
from hyp105_g5e2b3b2_coincident_cycles import (
    check_input, physical_six_cycles, exact_coincident_c6,
    independent_brute_small_incidence, _physical_dual_column_edges,
    exact_alternating_cycle_weight,
)


def toy_model():
    cycle = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5))
    return {"h": 0, "s": None, "scheme": "fixture", "a": 6, "m": 12,
            "N": 6, "left_labels": cycle, "right_labels": cycle,
            "incidences": tuple((i, i) for i in range(6))}


def swap_sides(model):
    result = dict(model)
    result["left_labels"], result["right_labels"] = (
        model["right_labels"], model["left_labels"])
    result["incidences"] = tuple((j, i) for i, j in model["incidences"])
    return result


def reorder_physical_symbols(model):
    result = dict(model)
    a = model["a"]
    perm_left = tuple(reversed(range(a)))
    perm_right = tuple((i + 3) % a for i in range(a))
    result["left_labels"] = tuple(sorted((perm_left[i], perm_left[j]))
                                  for i, j in model["left_labels"])
    result["right_labels"] = tuple(sorted((perm_right[i], perm_right[j]))
                                   for i, j in model["right_labels"])
    return result


def restrict_incidence(model, ids):
    result = dict(model)
    result["incidences"] = tuple(model["incidences"][i] for i in ids)
    result["N"] = len(ids)
    return result


def check_true_unit_signed_trade(model, cycle_ids):
    assert len(cycle_ids) == 6
    vectors = [0] * model["m"]
    a = model["a"]
    for j, colid in enumerate(cycle_ids):
        pid, lid = model["incidences"][colid]
        for coordinate in model["left_labels"][pid]:
            vectors[coordinate] += 1 if j % 2 == 0 else -1
        for coordinate in model["right_labels"][lid]:
            vectors[a + coordinate] += 1 if j % 2 == 0 else -1
    return all(value % 5 == 0 for value in vectors)


class CoincidentSixCycleTests(unittest.TestCase):
    def test_complete_k6_and_synthetic_single_event(self):
        pairs = tuple(combinations(range(6), 2))
        self.assertEqual(len(tuple(physical_six_cycles(pairs, 6))), 60)
        model = toy_model()
        report = exact_coincident_c6(model)
        self.assertEqual(report["left_physical_C6_cycles_examined"], 1)
        self.assertEqual(report["exact_coincident_C6_factor_matchings_D"], 1)
        self.assertEqual(report["exact_GF5_flow_weight_per_agreeing_cycle"], 5643)
        self.assertEqual(report["fixed_label_R3_lower_exact"], "5643/51^6")
        self.assertEqual(exact_alternating_cycle_weight(), 5643)
        left = model["left_labels"]
        right = model["right_labels"]
        supports = tuple(tuple(sorted(left[i] + tuple(
            model["a"] + x for x in right[i]))) for i in range(6))
        signs = (1, -1, 1, -1, 1, -1)
        self.assertEqual(
            single_signed_trade_mitm(
                supports, signs, 12)["weighted_flow_count"], 5643)

        self.assertEqual(
            independent_brute_small_incidence(model)["D"], 1)
        self.assertTrue(check_true_unit_signed_trade(
            model, report["witness_column_ids_in_canonical_left_cycle_order"][0]))
        self.assertEqual(
            exact_coincident_c6(swap_sides(model))[
                "exact_coincident_C6_factor_matchings_D"], 1)

    def test_malformed_and_budget_fail_closed(self):
        model = toy_model()
        with self.assertRaises(ValueError):
            exact_coincident_c6(model, cycle_limit=0)
        complete = dict(model)
        complete["left_labels"] = tuple(combinations(range(6), 2))
        complete["right_labels"] = complete["left_labels"]
        complete["incidences"] = tuple((i, i) for i in range(15))
        complete["N"] = 15
        with self.assertRaises(RuntimeError):
            exact_coincident_c6(complete, cycle_limit=1)
        with self.assertRaises(ValueError):
            independent_brute_small_incidence(
                pair_labeled_symplectic(1,"lex"))
        wrong = dict(model)
        wrong["right_labels"] = model["right_labels"][:-1] + (
            model["right_labels"][0],)
        with self.assertRaises(ValueError):
            check_input(wrong)

    def test_full_gf2_three_scheme_counts_invariant_under_side_swap(self):
        accepted = {"lex": 15, "reverse-line": 3, "coordinate-flag": 3}
        for scheme in ("lex", "reverse-line", "coordinate-flag"):
            model = pair_labeled_symplectic(1, scheme)
            original = exact_coincident_c6(model)
            self.assertEqual(
                original["exact_coincident_C6_factor_matchings_D"],
                accepted[scheme])
            flipped = exact_coincident_c6(swap_sides(model))
            self.assertEqual(original["exact_coincident_C6_factor_matchings_D"],
                             flipped["exact_coincident_C6_factor_matchings_D"])
            permuted = exact_coincident_c6(reorder_physical_symbols(model))
            self.assertEqual(original["exact_coincident_C6_factor_matchings_D"],
                             permuted["exact_coincident_C6_factor_matchings_D"])
            self.assertFalse(original["enumerated_N_choose_6"])
            self.assertFalse(original["strict_R3_exponent_proved"])
            for witness in original[
                    "witness_column_ids_in_canonical_left_cycle_order"]:
                self.assertTrue(check_true_unit_signed_trade(model, witness))

    def test_independent_subset_oracle_on_actual_gf2_incidence(self):
        model = pair_labeled_symplectic(1, "lex")
        full = exact_coincident_c6(model)
        witness = full["witness_column_ids_in_canonical_left_cycle_order"]
        if witness:
            ids = list(witness[0])
            ids += [i for i in range(model["N"]) if i not in ids][:6]
        else:
            ids = list(range(12))
        small = restrict_incidence(model, ids)
        report = exact_coincident_c6(small)
        brute = independent_brute_small_incidence(small)
        self.assertEqual(report["exact_coincident_C6_factor_matchings_D"],
                         brute["D"])
        for w in report["witness_column_ids_in_canonical_left_cycle_order"]:
            self.assertTrue(check_true_unit_signed_trade(small, w))

    def test_real_gf4_join_symmetry_and_structural_witness(self):
        model = pair_labeled_symplectic(2, "lex")
        result = exact_coincident_c6(model)
        self.assertEqual(result["left_physical_C6_cycles_examined"], 121320)
        self.assertEqual(result["exact_coincident_C6_factor_matchings_D"], 8481)
        for w in result["witness_column_ids_in_canonical_left_cycle_order"]:
            self.assertTrue(check_true_unit_signed_trade(model, w))
            pp = [model["incidences"][i][0] for i in w]
            ll = [model["incidences"][i][1] for i in w]
            self.assertEqual(len(set(pp)), 6)
            self.assertEqual(len(set(ll)), 6)
            graph_left = _physical_dual_column_edges(
                [model["left_labels"][p] for p in pp])
            graph_right = _physical_dual_column_edges(
                [model["right_labels"][l] for l in ll])
            self.assertIsNotNone(graph_left)
            self.assertEqual(graph_left, graph_right)
        self.assertFalse(result["all_h_upper_bound_proved"])


if __name__ == "__main__":
    unittest.main()
