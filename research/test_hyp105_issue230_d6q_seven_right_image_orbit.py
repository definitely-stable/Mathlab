"""Independent exact all-seven conditional right IMAGE orbit probability tests.

Direct edge-mask enumeration and independent 3!/4!/6! physical permutation
oracles, plus true-original W32 seven-GF5 and W34 image-only controls.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
import unittest

from hyp105_issue230_d6q_seven_right_image_orbit import (
    complete_physical_template_counts,
    deletion_template_bounds,
    falling,
    image_physical_template_census,
    right_image_orbit_probabilities,
    original_w3_parameters,
    original_all_h_image_robust_certificate,
    fixed_f_right_image_exact_expectation,
    real_original_W32_full_seven_orbit_report,
)
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    _physical_dual, cylinder_seven_class, compile_original_W32_cylinders,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6m_gq_collinearity_ca_transfer import (
    exact_right_A_probability,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)


def independent_graph_shape_census(a,available):
    """Direct unranked graph enumeration without template tables/masks."""
    E=tuple(sorted(available))
    counts=Counter()
    for six in combinations(E,6):
        deg=Counter(v for edge in six for v in edge)
        if len(deg)!=6 or set(deg.values())!={2}:
            continue
        counts["A"]+=1
        adj={v:set() for v in deg}
        for u,v in six:
            adj[u].add(v);adj[v].add(u)
        visited={next(iter(adj))}
        todo=list(visited)
        while todo:
            for y in adj[todo.pop()]:
                if y not in visited:
                    visited.add(y);todo.append(y)
        if len(visited)==6:
            counts["D6"]+=1
    for five in combinations(E,5):
        for rep in five:
            deg=Counter(v for edge in five for v in edge)
            for v in rep:
                deg[v]+=1
            if len(deg)==6 and set(deg.values())=={2}:
                counts["B"]+=1
    for three in combinations(E,3):
        if len(set(v for edge in three for v in edge))==6:
            counts["C"]+=1
    return {k:counts[k] for k in ("A","B","C","D6")}


def source_canonical_line_cycle():
    return ((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))


class ExactRightImageOrbitTests(unittest.TestCase):
    def test_independent_physical_graph_census_K6_K7_and_single_deletion(self):
        for a in (6,7):
            full=set(combinations(range(a),2))
            for image in (full,full-{(0,1)}):
                with self.subTest(a=a,missing=len(full)-len(image)):
                    independent=independent_graph_shape_census(a,image)
                    actual=image_physical_template_census(a,image)
                    self.assertEqual(actual,independent)
                    bounds=deletion_template_bounds(a,len(image))
                    self.assertEqual(
                        actual,
                        {k:bounds["complete_templates"][k]-
                            len(full-image)*bounds[
                                "per_single_missing_edge_templates"][k]
                         for k in actual})
                    self.assertTrue(all(
                        actual[k]>=bounds[
                            "guaranteed_surviving_templates"][k]
                        for k in actual))
            self.assertEqual(
                image_physical_template_census(a,full),
                complete_physical_template_counts(a))

    def test_independent_exhaustive_fixed_image_permutation_oracles(self):
        # Physical K6 C6: six ORIGINAL line images are all six physical C6
        # edges. All right assignments are type A; precisely 12 out of 720
        # preserve the left incidence-column dual for aligned D6.
        cycle=source_canonical_line_cycle()
        left_dual=_physical_dual(tuple(range(6)),cycle)
        sig_D=("A",tuple(range(6)),left_dual,())
        total_D=sum(
            cylinder_seven_class(sig_D,p)=="D6"
            for p in permutations(cycle))
        self.assertEqual(total_D,12)
        p_D=right_image_orbit_probabilities(
            6,6,image_physical_template_census(6,cycle))
        self.assertEqual(p_D["A"],1)
        self.assertEqual(p_D["D6"],Fraction(1,60))
        self.assertEqual(Fraction(total_D,factorial(6)),p_D["D6"])
        # One right repeated original factor + 4 singles: E is one K2
        # disjoint from a C4. Exactly 4!=24 out of 5!=120 permutations
        # preserve right B (the repeated edge is distinguished).
        B_E=((0,1),(2,3),(3,4),(4,5),(2,5))
        sig_B=("A",(0,0,1,2,3,4),(),())
        n_B=sum(cylinder_seven_class(sig_B,p)=="A-left/B-right"
                for p in permutations(B_E))
        p_B=right_image_orbit_probabilities(
            6,5,{**{"A":0,"B":1,"C":0,"D6":0}})
        self.assertEqual(n_B,24)
        self.assertEqual(p_B["B"],Fraction(1,5))
        # A physical 3-matching: all bijections to three ORIGINAL right
        # line IDs preserve the right C three-double-edge configuration.
        C_E=((0,1),(2,3),(4,5))
        sig_C=("A",(0,0,1,1,2,2),(),())
        n_C=sum(cylinder_seven_class(sig_C,p)=="C/A"
                for p in permutations(C_E))
        self.assertEqual(n_C,factorial(3))

    def test_all_h_minimal_a_image_template_robustness(self):
        for s in (2,4,8,16):
            with self.subTest(s=s):
                p=original_w3_parameters(s)
                b=original_all_h_image_robust_certificate(s)
                self.assertEqual((p["a"],p["V"]),
                                 (b["a"],b["V"]))
                self.assertLess(Fraction(
                    b["six_edge_template_deletion_fraction"]),1)
                self.assertTrue(all(n>0 for n in
                                    b["physical_template_deletion_lower_counts"].values()))
                self.assertGreater(Fraction(
                    b["new_all_f_all_IMAGE_permutation_orbit_S_mean_floor"]),0)
                self.assertEqual(b["Branch_A"],"OPEN")
                self.assertEqual(b["Branch_B"],"OPEN")
                self.assertTrue(b["NOT_a_bound_on_each_fixed_right_injection"])
                self.assertTrue(b["NOT_complete_W34_W38_original_seven_S"])
                self.assertEqual(
                    Fraction(b["unconditional_injection_probability"]["A"]),
                    exact_right_A_probability(s))

    def test_true_original_W32_all_seven_exact_orbit_expected_vs_fixed_g(self):
        data=real_original_W32_full_seven_orbit_report()
        self.assertEqual(data["Branch_A"],"OPEN")
        self.assertEqual(data["Branch_B"],"OPEN")
        self.assertEqual(data["complete_W34_W38_ORIGINAL_seven_S"],
                         "NOT-CLAIMED")
        rows=data["original_W32_rows"]
        self.assertEqual([r["scheme"] for r in rows],
                         ["lex","reverse","S68","S72"])
        self.assertEqual([r["fixed_actual_S_seven"] for r in rows],
                         [259,169,68,72])
        self.assertEqual(
            rows[0]["expected_seven_class_counts"],
            rows[1]["expected_seven_class_counts"])
        self.assertEqual(
            rows[2]["expected_seven_class_counts"],
            rows[3]["expected_seven_class_counts"])
        self.assertEqual(
            rows[0]["exact_right_image_orbit_shape_probabilities"],
            {"A":"2/143","B":"3/1001","C":"3/91","D6":"1/5005"})
        for row in rows:
            with self.subTest(scheme=row["scheme"]):
                expected={k:Fraction(v) for k,v in
                          row["expected_seven_class_counts"].items()}
                self.assertTrue(all(v>=0 for v in expected.values()))
                self.assertEqual(
                    sum(expected.values(),Fraction()),
                    Fraction(row["expected_all_seven_S"]))
                self.assertEqual(
                    sum(expected[k]*R3_CERTIFIED_FLOORS[k]
                        for k in R3_CERTIFIED_FLOORS),
                    Fraction(row[
                        "expected_GF5_seven_selected_lower_numerator"]))
                self.assertEqual(
                    sum(Fraction(v) for v in row[
                        "actual_minus_image_orbit_mean_by_class"].values()),
                    Fraction(row["fixed_actual_S_seven"])-
                    Fraction(row["expected_all_seven_S"]))
                self.assertEqual(
                    row["profile_eligible_original_sixsets"]+
                    row["profile_ineligible_original_sixsets"],
                    62370)
                self.assertTrue(row[
                    "right_orbit_fixed_IMAGE_not_unconditional_completion"])
                self.assertTrue(row["conditional_expectation_not_all_g_lower"])

    def test_real_W34_right_IMAGE_physical_only_no_full_seven_oracle(self):
        """True original W(3,4) right injection, PHYSICAL image alone.

        Does not enumerate original W34 six-incidence S or infer full risk.
        """
        model=fixture(2,"lex")
        params=original_w3_parameters(4)
        self.assertEqual((model["a"],len(model["right_labels"])),
                         (params["a"],params["V"]))
        assert (params["a"],params["V"],params["K"],params[
            "missing_pair_edges"])==(14,85,91,6)
        physical=image_physical_template_census(
            model["a"],model["right_labels"])
        bounds=deletion_template_bounds(14,85)
        for shape in ("A","B","C","D6"):
            self.assertGreaterEqual(
                physical[shape],
                bounds["guaranteed_surviving_templates"][shape])
            self.assertLessEqual(
                physical[shape],bounds["complete_templates"][shape])
        actual=right_image_orbit_probabilities(14,85,physical)
        lower=right_image_orbit_probabilities(
            14,85,bounds["guaranteed_surviving_templates"])
        for shape in ("A","B","C","D6"):
            self.assertGreaterEqual(actual[shape],lower[shape])

    def test_reject_noncanonical_illegal_input_and_missing_orbit_shapes(self):
        with self.assertRaises(ValueError):
            original_w3_parameters(3)
        with self.assertRaises(ValueError):
            original_w3_parameters(1)
        with self.assertRaises(ValueError):
            deletion_template_bounds(6,16)
        with self.assertRaises(ValueError):
            deletion_template_bounds(6,5)
        with self.assertRaises(ValueError):
            image_physical_template_census(6,[(1,0)]*15)
        with self.assertRaises(ValueError):
            image_physical_template_census(14,
                list(combinations(range(14),2))[:85],
                max_six_coordinate_sets=100)
        with self.assertRaises(ValueError):
            right_image_orbit_probabilities(6,15,
                {"A":70,"B":45,"C":15})
        with self.assertRaises(ValueError):
            right_image_orbit_probabilities(6,15,
                {"A":999,"B":45,"C":15,"D6":60})
        with self.assertRaises(ValueError):
            falling(3,5)
        model=fixture(1,"lex")
        compiled=compile_original_W32_cylinders(model)
        probs=right_image_orbit_probabilities(
            6,15,complete_physical_template_counts(6))
        with self.assertRaises(ValueError):
            fixed_f_right_image_exact_expectation(
                compiled,probs,(model["right_labels"][0],)*15)


if __name__=="__main__":
    unittest.main()
