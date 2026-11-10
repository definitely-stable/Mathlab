"""Independent HYP-105 #230 AA4-SYMMOM true original GQ moment referee tests."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_original_symbol_secondmoments_referee import (
    SCHEMA,ROOT_STATUS,CASES,_minimal_pair_alphabet,
    _potential_original_middle_label_overlap_degree_bound,
    _observed_full_original_flag_label_overlap_degree,
    _full_exact_symbol_moments_one_bin,_full_moment_case,
    canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import (
    _source,_true_original_proper_P3,_rank_probability3,_pair_bad,
    _full_exact_case as old_independent_full_original_pairwise_case
)


class TestIndependentFullOriginalSymbolMomentReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()
        cls.rows=cls.report["true_genuine_original_W32_W34_complete_full_moment_censuses"]

    def test_root_scientific_acceptance_not_promoted(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertEqual(r["issue"],230)
        for key in ("all_h_complete_original_M_G_B_exact_linear_sparse_symbol_second_moment_formulas",
                    "all_h_exact_original_x_y_and_both_pair_overlap_inclusion_exclusion",
                    "all_h_exact_good_disjoint_middle_00_11_physical_corner_square_moments",
                    "all_h_heavy_original_physical_symbol_necessary_for_local_B_above_three_quarters",
                    "all_h_minimal_pair_alphabet_source_label_overlap_degree_O_s_5_over_2",
                    "all_h_unweighted_flag_label_overlap_fraction_O_s_minus_3_over_2"):
            self.assertTrue(r[key])
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["all_h_global_B_over_M_below_three_quarters_PROVED"])
        self.assertFalse(r["infinite_original_correlated_counterexample_family_claimed"])
        self.assertFalse(r["external_numeric_C6_graph_constants_claimed"])
        self.assertFalse(r["ASET_exponent_claimed"])
        self.assertTrue(r["this_does_NOT_claim_weighted_same_endpoint_overlap_sparsity"])

    def test_all_eight_exact_COMPLETE_original_proper_physical_P3_censuses(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual([(q["original_s"],q["original_scheme"],q["original_CORE"])
                          for q in self.rows],list(CASES))
        self.assertEqual([q["counts"]["total_full_original_coordinate_proper_P3_paths"]
                          for q in self.rows],
                         [1346,1154,838,83892,82846,79404,9966,66418])
        for q in self.rows:
            self.assertTrue(q["full_source_real_physical_path_census"])
            self.assertEqual(q["source_real_physical_owned_edges"],
                             2*q["source_original_retained_CORE_flag_count"])
            self.assertGreater(q["exact_original_priority_threeowner_source_sets"],0)
            self.assertGreater(q["counts"]["number_nonempty_original_endpoint_bins"],0)

    def test_true_source_minimal_symbol_alphabet_calculation(self):
        expected={2:6,4:14,8:35,16:94}
        for s,a in expected.items():
            V=(s+1)*(s*s+1)
            self.assertEqual(_minimal_pair_alphabet(V),a)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertLess(comb(a-1,2),V)
        self.assertEqual(_minimal_pair_alphabet(1),2)

    def test_invalid_original_minimal_alphabet_and_capacity_fail_closed(self):
        for V in (-1,0,2.5):
            with self.assertRaises(ValueError):
                _minimal_pair_alphabet(V)
        for s,a in ((1,5),(0,8),(2,5),(4,13),(8,34)):
            with self.assertRaises(ValueError):
                _potential_original_middle_label_overlap_degree_bound(s,a)

    def test_all_h_original_symbol_middle_label_overlap_degree_closed_formula(self):
        for z in self.report["independent_all_h_minimal_alphabet_degree_capacity_examples"]:
            s=z["s"];a=z["actual_alphabet"];V=z["original_points_and_lines_each"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertEqual(z["original_flags"],(s+1)*V)
            self.assertEqual(z["minimal_pair_alphabet"],a)
            self.assertEqual(z["raw_union_degree_cap"],2*((2*a-3)*(s+1)-1))
            self.assertEqual(z["unweighted_source_middle_pair_overlap_max_degree_cap"],
                min(z["original_flags"]-1,z["raw_union_degree_cap"]))
            self.assertEqual(Fraction(z["fraction_bound_for_distinct_original_flag_pairs"]),
                Fraction(z["unweighted_source_middle_pair_overlap_max_degree_cap"],
                         z["original_flags"]-1))
            self.assertTrue(z["all_h_asymptotic_finite_source_degree_over_flags_O_s_minus_three_halves_if_minimal_alphabet"])
            self.assertTrue(z["this_does_NOT_control_same_endpoint_weighted_B_over_M"])

    def test_original_minimal_alphabet_unweighted_capacity_fraction_decreases(self):
        examples=self.report["independent_all_h_minimal_alphabet_degree_capacity_examples"]
        self.assertEqual([q["s"] for q in examples],[2,4,8,16,32,64])
        for a,b in zip(examples[1:],examples[2:]):
            self.assertGreater(Fraction(a["fraction_bound_for_distinct_original_flag_pairs"]),
                               Fraction(b["fraction_bound_for_distinct_original_flag_pairs"]))
        self.assertLess(Fraction(examples[-1]["fraction_bound_for_distinct_original_flag_pairs"]),
                        Fraction(1,50))

    def test_independent_actual_FULL_original_flag_overlap_exact_capacity(self):
        for row in self.rows:
            z=row["unweighted_original_middle_flag_label_capacity"]
            env=z["full_source_alphabet_minimal_capacity_envelope"]
            self.assertTrue(z["all_original_flag_pair_overlaps_scanned_without_endpoint_condition"])
            self.assertEqual(env["s"],row["original_s"])
            self.assertEqual(env["actual_alphabet"],
                             row["source_actual_physical_pair_alphabet_size"])
            self.assertEqual(z["original_source_flags_in_CORE"],
                             row["source_original_retained_CORE_flag_count"])
            self.assertLessEqual(
                z["max_original_middle_label_overlap_degree_in_CORE"],
                env["unweighted_source_middle_pair_overlap_max_degree_cap"])
            self.assertLessEqual(z["exact_unweighted_original_middle_both_typed_pair_overlap_pairs"],
                                z["exact_unweighted_original_middle_label_pair_overlap_pairs"])

    def test_original_exact_full_M_G_B_fraction_conservation(self):
        for row in self.rows:
            M=Fraction(row["total_original_M"])
            G=Fraction(row["total_original_G"])
            B=Fraction(row["total_original_B"])
            self.assertGreater(M,0)
            self.assertGreater(G,0)
            self.assertGreaterEqual(B,0)
            self.assertEqual(M,B+G)
            self.assertEqual(B/M,Fraction(row["exact_original_B_over_M"]))
            self.assertFalse(row["root_PROVED_A"])
            self.assertFalse(row["all_h_global_B_over_M_below_three_quarters_PROVED"])

    def test_complete_original_non_J_G_symbol_moment_source_identity(self):
        for row in self.rows:
            m={k:Fraction(v) for k,v in row["moments"].items()}
            self.assertEqual(m["G"],m["D"]+m["G00"]+m["G11"])
            self.assertEqual(m["G11"],m["G11_tail"]+m["G11_head"])
            self.assertEqual(m["G00"],
                m["M"]-m["Ox"]-m["Oy"]+m["Oxy"])
            self.assertEqual(m["M"],m["B"]+m["G"])
            for key in ("M","G","D","Ox","Oy","Oxy","G00","G11","G11_tail","G11_head"):
                self.assertGreaterEqual(m[key],0)
            self.assertLessEqual(m["Oxy"],min(m["Ox"],m["Oy"]))
            self.assertLessEqual(m["G"],m["M"])
            self.assertEqual(m["M"],Fraction(row["total_original_M"]))

    def test_exact_true_original_full_lex_W32_previous_M_B_rational_regression(self):
        row=self.rows[0]
        self.assertEqual(Fraction(row["total_original_M"]),
                         Fraction(170009657654496199,164130319761408000000))
        self.assertEqual(Fraction(row["exact_original_B_over_M"]),
                         Fraction(395498199363009600,1190067603581473393))

    def test_exact_true_original_FULL_W34_lex_reverse_shift_previous_B_regression(self):
        expect=[
           Fraction(6455794325016624278974180549344,34112625017517015558762952579019),
           Fraction(1112181511961691267640954528608,5419443488794004529193758698293),
           Fraction(38485044924066111819475664,193743221070784284041268159)
        ]
        self.assertEqual([Fraction(x["exact_original_B_over_M"]) for x in self.rows[3:6]],expect)

    def test_all_h_true_original_weighted_star_concentration_G_gate(self):
        for row in self.rows:
            m={k:Fraction(v) for k,v in row["moments"].items()}
            self.assertGreaterEqual(m["G"],m["source_G_symbol_max_mass_lower_bound"])
            self.assertGreaterEqual(m["G"],
                m["D"]+m["M"]-m["Ox"]-m["Oy"])
            self.assertGreaterEqual(m["G"],m["D"])
            self.assertLessEqual(Fraction(row["source_symbol_actual_strict_local_bad_M_share"]),
                                 Fraction(row["source_symbol_heavy_weighted_M_share"]))
            self.assertLessEqual(
                row["counts"].get("actual_LOCAL_source_bad_B_over_M_above_three_quarters",0),
                row["counts"].get("heavy_symbol_candidate_endpoint_bins",0))
            self.assertGreaterEqual(Fraction(row["source_symbol_certified_strict_safe_M_share"]),0)

    def test_true_source_moment_source_fractional_positive_partition(self):
        for row in self.rows:
            self.assertEqual(
                Fraction(row["original_symbol_G00_weighted_fraction_of_M"])+
                Fraction(row["original_symbol_G11_weighted_fraction_of_M"])+
                Fraction(row["original_diagonal_D_fraction_of_M"]),
                1-Fraction(row["exact_original_B_over_M"]))
            self.assertLessEqual(Fraction(row["source_symbol_certified_strict_safe_M_share"]),
                                 1-Fraction(row["source_symbol_actual_strict_local_bad_M_share"]))

    def test_strict_bad_original_endpoint_has_heavy_symbol_neccessary(self):
        for row in self.rows:
            w=row["worst_true_original_local_source_endpoint"]
            self.assertEqual(len(w["physical_ordered_endpoints"]),2)
            self.assertGreater(w["number_real_proper_original_P3_paths"],0)
            self.assertGreater(w["middle_owner_source_flag_groups"],0)
            self.assertGreater(Fraction(w["x_y_largest_symbol_middle_source_mass_fraction_sum"]),0)
            self.assertGreaterEqual(Fraction(w["actual_original_pair_label_overlap_x_weight"]),0)
            self.assertGreaterEqual(Fraction(w["actual_original_pair_label_overlap_y_weight"]),0)
            self.assertGreaterEqual(Fraction(w["actual_original_both_label_overlap_weight"]),0)

    def test_all_h_independent_original_M_G_B_from_manual_W32_pair_census(self):
        # Independent audit: evaluate 100% of old J/typed directed path pairs
        # using original owner IDs, not the new symbol-second-moment kernel.
        for scheme,core in (("lex","full"),("reverse","full"),("shift","Z17")):
            c=_source(2,scheme,core)
            bins=defaultdict(list)
            cache={}
            for p,os in _true_original_proper_P3(c):
                k=tuple(sorted(os))
                if k not in cache:
                    cache[k]=_rank_probability3(k,c["J"])/64
                bins[(p[0],p[-1])].append((p,os,cache[k]))
            M=G=B=Fraction(0)
            for group in bins.values():
                result=_full_exact_symbol_moments_one_bin(group,c)
                local_M=local_G=local_B=Fraction(0)
                for p,os,wp in group:
                    for q,ot,wq in group:
                        w=wp*wq
                        local_M+=w
                        if p==q or _pair_bad(p,os,q,ot,c["J"])=="compatible":
                            local_G+=w
                        else:
                            local_B+=w
                self.assertEqual(result["M"],local_M)
                self.assertEqual(result["G"],local_G)
                self.assertEqual(result["B"],local_B)
                M+=local_M;G+=local_G;B+=local_B
            z=next(x for x in self.rows if (x["original_s"],x["original_scheme"],x["original_CORE"])==(2,scheme,core))
            self.assertEqual(M,Fraction(z["total_original_M"]))
            self.assertEqual(G,Fraction(z["total_original_G"]))
            self.assertEqual(B,Fraction(z["total_original_B"]))

    def test_independent_OLD_pairwise_W34_full_lex_reference_on_exact_source(self):
        # Full external original source J/collision + cliques parent computation:
        # completely distinct from moment-square inclusion/exclusion.
        old=old_independent_full_original_pairwise_case(4,"lex","full")
        new=self.rows[3]
        self.assertEqual(Fraction(new["total_original_M"]),Fraction(old["M"]))
        self.assertEqual(Fraction(new["total_original_G"]),Fraction(old["G"]))
        self.assertEqual(Fraction(new["total_original_B"]),Fraction(old["B"]))
        self.assertEqual(Fraction(new["exact_original_B_over_M"]),Fraction(old["B_over_M"]))
        self.assertEqual(new["counts"]["total_full_original_coordinate_proper_P3_paths"],
                         old["full_true_coordinate_proper_P3_count"])

    def test_true_original_physical_source_singleton_diagonal_exact(self):
        c=_source(2,"lex","full")
        p,os=next(iter(_true_original_proper_P3(c)))
        w=_rank_probability3(tuple(sorted(os)),c["J"])/64
        x=_full_exact_symbol_moments_one_bin([(p,os,w)],c)
        self.assertEqual(x["G"],w*w)
        self.assertEqual(x["B"],0)
        self.assertEqual(x["G00"],0)
        self.assertEqual(x["G11"],0)
        self.assertEqual(x["D"],w*w)
        self.assertEqual(x["M"],w*w)
        self.assertEqual(x["Ox"],w*w)
        self.assertEqual(x["Oy"],w*w)
        self.assertEqual(x["Oxy"],w*w)

    def test_bad_source_argument_validation_and_weight_fail_closed(self):
        c=_source(2,"lex","full")
        with self.assertRaises(ValueError):
            _full_exact_symbol_moments_one_bin([],c)
        p,os=next(iter(_true_original_proper_P3(c)))
        with self.assertRaises(AssertionError):
            _full_exact_symbol_moments_one_bin([(p,os,Fraction(0))],c)
        with self.assertRaises(AssertionError):
            _full_exact_symbol_moments_one_bin([(p,os,Fraction(-1))],c)

if __name__=="__main__":
    unittest.main()
