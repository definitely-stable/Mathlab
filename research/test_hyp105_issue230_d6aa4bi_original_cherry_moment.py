"""AA4-BI independent original W32 and nononto W34 seven-GF5 source cherry tests."""
import unittest
from collections import Counter
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    exact_ONE_side_original_projection_index,exact_two_sided_original_seven_join)
from hyp105_issue230_d6aa4bh_local_seven_compensation import (
    localized_original_seven_fiber)
from hyp105_issue230_d6aa4bi_original_cherry_moment import (
    genuine_original_source_cherries,true_original_fixed_pair_source_cherry_fiber,
    all_h_original_source_cherry_equivalent_obstruction,_sector_stats)
from hyp105_issue230_d6aa4bg_fixed_squarefree_D6_trace import squarefree_trace_six_dp
from hyp105_g5e2b3e1b0_seven_signature import seven_census,R3_CERTIFIED_FLOORS


def original_W32_independent_two_side_cherry_histogram(model):
    """Unrelated ORIGINAL source-six-ID pair-set join, not new physical multigraph enumerator."""
    P=exact_ONE_side_original_projection_index(model,0)["candidate_sixset_map"]
    L=exact_ONE_side_original_projection_index(model,1)["candidate_sixset_map"]
    inc=tuple(tuple(q) for q in model["incidences"])
    hist=Counter()
    bb_overlap=0
    for Q in P.keys()&L.keys():
        c=genuine_original_source_cherries(Q,inc)
        n=c["total_source_cherries"]
        hist[n]+=1
        if n==2: bb_overlap+=c["BB_same_true_original_flag_overlap"]
    return hist,bb_overlap


class AA4BIOriginalCherryMoments(unittest.TestCase):
    def test_01_true_W32_five_fixed_f_g_independent_seven_join_and_GF5(self):
        mods=[("dual_zero",zero_split_original_W32())]+[
            (n,fixture(1,n)) for n in ("lex","reverse","S68","S72")]
        stronger=False
        P=tuple(range(6))
        for n,model in mods:
            res=true_original_fixed_pair_source_cherry_fiber(model,P)
            self.assertEqual(set(res["sectors"]),{P})
            z=res["sectors"][P]
            hist,BB=original_W32_independent_two_side_cherry_histogram(model)
            self.assertEqual(z["source_cherry_histogram_c0_through4"],
                             {i:hist[i] for i in range(5)})
            self.assertEqual(z["BB_overlapping_original_source_flag_count"],BB)
            historic=seven_census(model,independent_checks=False)
            old=exact_two_sided_original_seven_join(
                model,independent_history=False)
            trace=squarefree_trace_six_dp(model)
            self.assertEqual(z["six_original_incidence_join"],
                             old["exact_source_original_Q_double_projection_intersection"])
            self.assertEqual(z["AA_six_original_factor_distinct"],
                             old["physical_A_A_joint_candidates"])
            self.assertEqual(z["nonAA_seven_GF5_positive_source_cherry_exact"]+
                             trace["accepted_original_six_ID_D6"],
                             historic["S_seven"])
            self.assertEqual(z["GF5_51palette_nonAA_certified_numerator"]+
                             5643*trace["accepted_original_six_ID_D6"],
                             historic["GF5_seven_lower_numerator"])
            self.assertEqual(z["nonAA_from_moment_exact_inclusion_exclusion"],
                             z["nonAA_seven_GF5_positive_source_cherry_exact"])
            self.assertEqual(z["source_cherry_square_moment"],
                             z["source_cherry_binomial_moments_M1_to_M4"][0]+
                             2*z["source_cherry_binomial_moments_M1_to_M4"][1])
            self.assertLessEqual(z["nonAA_from_first_second_Cauchy_lower"],
                                 z["nonAA_seven_GF5_positive_source_cherry_exact"])
            stronger|=(z["nonAA_from_first_second_Cauchy_lower"]>
                       z["nonAA_from_first_moment_universal_lower"])
            print("AA4BI_TRUE_W32",n,"hist",z["source_cherry_histogram_c0_through4"],
                  "original_GF5_nonAA",z["nonAA_seven_GF5_positive_source_cherry_exact"],
                  "Cauchy",z["nonAA_from_first_second_Cauchy_lower"])
        self.assertTrue(stronger,"nonlinear second moment should strictly improve flat 1/4 on real W32")

    def test_02_W32_S68_S72_D6_zero_but_source_cherry_energy_positive(self):
        for name in ("S68","S72"):
            model=fixture(1,name)
            z=true_original_fixed_pair_source_cherry_fiber(model,tuple(range(6)))["sectors"][tuple(range(6))]
            self.assertEqual(squarefree_trace_six_dp(model)["accepted_original_six_ID_D6"],0)
            self.assertGreater(z["source_cherry_binomial_moments_M1_to_M4"][0],0)
            self.assertGreater(z["nonAA_from_first_second_Cauchy_lower"],0)
            self.assertEqual(z["nonAA_seven_GF5_positive_source_cherry_exact"],
                             seven_census(model,independent_checks=False)["S_seven"])

    def test_03_true_original_W34_nononto_two_schemes_local_cherry_and_weight(self):
        P=tuple(range(6))
        total_charged=0
        for name in ("lex","random"):
            model=fixture(2,name)
            z=true_original_fixed_pair_source_cherry_fiber(model,P)
            bh=localized_original_seven_fiber(model,P)["local_right_physical_fibers"]
            self.assertEqual(z["V"],85)
            self.assertEqual(z["a"],14)
            self.assertEqual(set(z["sectors"]),set(bh))
            for L,here in z["sectors"].items():
                old=bh[L]
                self.assertEqual(here["six_original_incidence_join"],
                                 old["two_sided_join_coefficient"])
                self.assertEqual(here["AA_six_original_factor_distinct"],
                                 old["AA_squarefree_source_factor_coefficient"])
                self.assertEqual(here["nonAA_seven_GF5_positive_source_cherry_exact"],
                                 old["compensator_non_AA"])
                self.assertEqual(here["GF5_51palette_nonAA_certified_numerator"],
                                 old["GF5_51palette_certified_weighted_numerator"]-
                                 5643*old["original_D6_from_trace"])
                self.assertEqual(here["nonAA_from_moment_exact_inclusion_exclusion"],
                                 old["compensator_non_AA"])
                self.assertTrue(here["nonAA_from_first_second_Cauchy_lower"]<=
                                old["compensator_non_AA"])
                total_charged+=here["source_cherry_binomial_moments_M1_to_M4"][0]
        self.assertGreater(total_charged,0)

    def test_04_sharp_cherry_weight_constants_on_allowed_source_charge_classes(self):
        cases={
            "B/A":((1,1,0,0),45600,1),
            "B/B-disjoint":((2,1,1,0),45010,2),
            "B/B-overlap":((2,1,1,1),51750,2),
            "C/A":((3,3,0,0),43320,3),
            "C/B":((4,3,1,0),49050,4),
        }
        for name,(t,w,n) in cases.items():
            z=_sector_stats([t])
            self.assertEqual(z["GF5_51palette_nonAA_certified_numerator"],w)
            self.assertEqual(z["source_cherry_binomial_moments_M1_to_M4"][0],n)
            self.assertEqual(z["nonAA_seven_GF5_positive_source_cherry_exact"],1)
            self.assertEqual(z["nonAA_from_first_second_Cauchy_lower"],1)
        self.assertEqual(
            _sector_stats([cases["C/B"][0]])["weighted_GF5_source_cherry_ratio_lower"],49050)
        self.assertEqual(
            _sector_stats([cases["B/A"][0]])["weighted_GF5_source_cherry_ratio_upper"],45600)

    def test_05_all_h_exact_integer_scope_no_fake_high_h_source_graph(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            z=all_h_original_source_cherry_equivalent_obstruction(1<<h)
            self.assertEqual(z["h"],h)
            self.assertEqual(z["possible_joined_original_source_cherry_counts"],
                             (0,1,2,3,4))
            self.assertTrue(z["no_original_all_fixed_positive_lower_proved"])
            self.assertTrue(z["root_branch_C_not_accepted"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            self.assertEqual(z["exact_nonAA_cherry_moment_inclusion_exclusion"],
                             "NONAA=M1-M2+M3-M4")

    def test_06_invalid_original_source_factor_sixincidence_and_palettemask(self):
        model=fixture(1,"lex")
        inc=tuple(model["incidences"])
        for bad in ((0,0,1,2,3,4),(-1,0,1,2,3,4),(0,1,2,3,4,500),(0,1,2,3,4,True)):
            with self.assertRaises(ValueError):
                genuine_original_source_cherries(bad,inc)
        for bad in ((0,1,2,3,4,4),(0,1,2,3,4,6),(0,1,2,3,4,True)):
            with self.assertRaises(ValueError):
                true_original_fixed_pair_source_cherry_fiber(model,bad)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                true_original_fixed_pair_source_cherry_fiber(bad,tuple(range(6)))
        for bad in (0,3,-4,33,True):
            with self.assertRaises(ValueError):
                all_h_original_source_cherry_equivalent_obstruction(bad)

if __name__=="__main__":
    unittest.main()
