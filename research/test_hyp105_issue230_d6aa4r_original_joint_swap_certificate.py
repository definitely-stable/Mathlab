"""AA4-R: adversarial globally coherent two-type ORIGINAL GF5 swap oracles."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    strict_true_W32_model, exact_two_sided_original_seven_join)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model, accepted_on_fixed_right,
    all_h_two_type_support_ceiling, exact_W32_joint_mixed_swap_certificate)


class OriginalTwoTypeGlobalSwapTests(unittest.TestCase):
    def test_001_full_TRUE_W32_GQ_axiom_on_all_four_pinned_schemes(self):
        for scheme in ("lex","reverse","S68","S72"):
            inc, f, g = strict_true_W32_gq_model(fixture(1,scheme))
            self.assertEqual(len(inc),45)
            self.assertEqual(len(f),15)
            self.assertEqual(len(g),15)

    def test_002_regression_fake_girth_six_partial_linear_NOT_a_GQ(self):
        real = fixture(1,"lex")
        # The incidence graph is 3-regular, 15+15, and has NO C4:
        # the cyclic difference set {0,1,3} has 6 distinct signed
        # nonzero differences modulo 15. But source (p0,p1,p2)
        # and (line0,line1,line14) form a genuine SOURCE C6.
        fake = {**real, "incidences": tuple(
            (p,ell) for ell in range(15)
            for p in (ell, (ell+1)%15, (ell+3)%15))}
        inc, _, _ = strict_true_W32_model(fake)
        self.assertEqual(len(inc),45)  # old NO-C4-only gate lets it through
        forbidden = ((0,0),(1,0),(1,1),(2,1),(2,14),(0,14))
        self.assertTrue(all(edge in inc for edge in forbidden))
        self.assertEqual(Counter(p for p,l in forbidden),{0:2,1:2,2:2})
        self.assertEqual(Counter(l for p,l in forbidden),{0:2,1:2,14:2})
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            strict_true_W32_gq_model(fake)
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            accepted_on_fixed_right(fake)
        with self.assertRaisesRegex(ValueError,"GQ unique anchor"):
            exact_W32_joint_mixed_swap_certificate(fake,(0,1),(0,1))

    def test_003_all_h_mixed_support_ceiling_is_a_valid_union_bound(self):
        # No fitted exponent or fake per-Q resampling: this is an exact
        # all-h set-union inequality, independently exhaustively checked
        # on a toy ORIGINAL bipartite incidence universe.
        inc=((0,0),(0,1),(1,2),(1,3),(2,0),(2,3),(3,1),(3,2))
        cert=all_h_two_type_support_ceiling(inc,(0,1),(0,1))
        U={i for i,e in enumerate(inc) if e[0] in (0,1)}
        V={i for i,e in enumerate(inc) if e[1] in (0,1)}
        actual=sum(bool(U.intersection(Q)) and bool(V.intersection(Q))
                   for Q in combinations(range(len(inc)),6))
        self.assertLessEqual(actual,cert["mixed_original_sixset_ceiling"])
        self.assertEqual(cert["N"],8)
        self.assertLessEqual(cert["shared_original_incidence_ids"],3)
        for bad in (((0,0),(0,0)),):
            with self.assertRaises(ValueError):
                all_h_two_type_support_ceiling(bad,(0,1),(0,1))

    def test_004_fixed_right_one_side_seven_exact_independent_legacy(self):
        for scheme,expected in (("S68",68),("S72",72),("lex",259),("reverse",169)):
            model=fixture(1,scheme)
            original=accepted_on_fixed_right(model)
            historical=seven_census(model,independent_checks=False,witness_sets=True)
            self.assertEqual(len(original),expected)
            self.assertEqual(original,historical["sets"])
            self.assertEqual(sum(R3_CERTIFIED_FLOORS[t] for t in original.values()),
                             historical["GF5_seven_lower_numerator"])

    def test_005_both_global_swaps_exact_four_map_numerator_and_seven(self):
        for scheme in ("S68","S72"):
            base=fixture(1,scheme)
            p,l=(0,1),(0,1)
            cert=exact_W32_joint_mixed_swap_certificate(base,p,l)
            # Independent hosted exact ORIGINAL-GQ four-map witness: mixed
            # nonzero disproves universally additive F(f)+G(g) formulas.
            golden={
                "S68":([68,89,87,104],-4,-185680),
                "S72":([72,95,84,102],-5,-287757),
            }[scheme]
            self.assertEqual(cert["seven_S_00_10_01_11"],golden[0])
            self.assertEqual(cert["genuine_two_type_mixed_delta"],golden[1])
            self.assertEqual(cert["certified_GF5_mixed_numerator"],golden[2])
            def swap_labels(arr,uv):
                out=list(arr);u,v=uv;out[u],out[v]=out[v],out[u]
                return tuple(out)
            models=(base,
                    {**base,"left_labels":swap_labels(base["left_labels"],p)},
                    {**base,"right_labels":swap_labels(base["right_labels"],l)},
                    {**base,"left_labels":swap_labels(base["left_labels"],p),
                            "right_labels":swap_labels(base["right_labels"],l)})
            direct=[exact_two_sided_original_seven_join(m,independent_history=False)
                    for m in models]
            self.assertEqual(cert["seven_S_00_10_01_11"],
                             [x["accepted_seven_GF5_original_S"] for x in direct])
            self.assertEqual(cert["certified_GF5_numerator_00_10_01_11"],
                             [x["selected_GF5_51palette_certified_numerator"]
                              for x in direct])
            self.assertEqual(sum(cert["mixed_delta_by_each_of_7_GF5_classes"].values()),
                             cert["genuine_two_type_mixed_delta"])
            self.assertEqual(
                sum(R3_CERTIFIED_FLOORS[tag]*delta
                    for tag,delta in cert["mixed_delta_by_each_of_7_GF5_classes"].items()),
                cert["certified_GF5_mixed_numerator"])
            self.assertLessEqual(cert["original_sixsets_in_mixed_support"],
                                 cert["original_gq_combinatorial_ceiling"][
                                     "mixed_original_sixset_ceiling"])
            self.assertTrue(cert["all_h_exact_two_type_swap_support_theorem"])
            self.assertFalse(cert["full_all_h_global_S_lower_PROVED"])

    def test_006_real_global_maps_not_independent_pseudolabeling(self):
        # Both swapped sides reuse exactly ONE injection per source factor.
        model=fixture(1,"S72")
        cert=exact_W32_joint_mixed_swap_certificate(model,(2,13),(3,11))
        self.assertEqual(len(cert["seven_S_00_10_01_11"]),4)
        self.assertEqual(len(cert["mixed_delta_by_each_of_7_GF5_classes"]),7)
        self.assertEqual(cert["seven_S_00_10_01_11"][0],72)
        self.assertFalse(cert["branch_B_infinite_counterfamily_PROVED"])

    def test_007_fail_closed_on_non_injective_and_bad_swap(self):
        model=fixture(1,"S68")
        with self.assertRaises(ValueError):
            exact_W32_joint_mixed_swap_certificate(model,(1,1),(0,1))
        with self.assertRaises(ValueError):
            exact_W32_joint_mixed_swap_certificate(model,(0,1),(15,1))
        labels=list(model["left_labels"])
        labels[0]=labels[1]
        with self.assertRaises(ValueError):
            exact_W32_joint_mixed_swap_certificate(
                {**model,"left_labels":tuple(labels)},(0,1),(0,1))


if __name__=="__main__":
    unittest.main()
