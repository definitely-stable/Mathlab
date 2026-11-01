"""AA4-ROOTJOINT: all-h exact integer/rational conditional root gate and W32/W34."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_dense_global_exact_dyadic_closure_referee import (
    EPSILON,K,SIG2_INV,SIG3_INV,BUDGET_LOWER,
    actual_source_budget,integrated_dense_closure,
    finite_true_original_path_partition,_normalized_power_upper,
)
from hyp105_exact_original_book_core_budget import original_core_budget
from hyp105_BBo_original_core_cubic_polynomial_referee import (
    source_first_original_BBo_cubic_catalog,
)


def maps(power,step=None,shift=0):
    s,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    palette=tuple(combinations(range(a),2))[:V]
    if step is None:
        step=7 if power==1 else 19
    return palette,tuple(palette[(step*i+shift)%V] for i in range(V))


class OriginalDenseIntegratedRoot(unittest.TestCase):
    def test_exact_true_original_source_budget_all_h_and_independent_prior_ref(self):
        for h in range(6,29):
            s=2**h
            got=actual_source_budget(s)
            old=original_core_budget(s)
            self.assertEqual(got["epsilon_chosen"],EPSILON)
            self.assertEqual(got["exact_original_book_Cs"],old["Cs"])
            self.assertEqual(got["minimal_pair_alphabet"],old["a"])
            self.assertEqual(got["exact_epsilon_core_budget"],
                             old["exact_max_epsilon_for_m0_ge_s4"])
            self.assertEqual(got["analytically_proved_all_h_lower_budget"],
                             BUDGET_LOWER)
            self.assertGreater(got["exact_epsilon_core_budget"],EPSILON)
            self.assertGreater(got["paired_CORE_edges_lower_if_small_full_tail"],
                               s**4)

    def test_hypothetical_graph_constants_exact_joint_root_vs_old_same_T(self):
        for C,c in ((1,1),(Fraction(1,2),Fraction(3,5)),
                    (Fraction(7,9),Fraction(2,11)),
                    (Fraction(13,4),Fraction(1,19))):
            with self.subTest(C=C,c=c):
                new=integrated_dense_closure(C,c)
                old=integrated_dense_closure(C,c,prior_B0=True)
                self.assertEqual(new["original_heavy_tail_T"],
                                 old["original_heavy_tail_T"])
                self.assertEqual(new["root_delta"],old["root_delta"])
                self.assertEqual(new["mixed_blocker_coefficient"],15)
                self.assertEqual(old["mixed_blocker_coefficient"],64)
                self.assertLess(new["mixed_blocker_B0_conservative_integer"],
                                old["mixed_blocker_B0_conservative_integer"])
                self.assertLessEqual(
                    new["dyadic_h0_combined_exact_rational"],
                    old["dyadic_h0_combined_exact_rational"])
                self.assertLessEqual(
                    new["dyadic_h0_combined_exact_rational"],
                    new["dyadic_h0_individually_budgeted"])
                self.assertGreaterEqual(
                    sum(new["joint_certified_relative_losses_upper"]),0)
                self.assertLessEqual(
                    sum(new["joint_certified_relative_losses_upper"]),Fraction(1,4))
                self.assertGreaterEqual(
                    new["joint_certified_remaining_fraction"],Fraction(1,4))
                self.assertEqual(new["core_U_BBo_lower_coefficient"],Fraction(1,8))
                self.assertTrue(new[
                    "applies_to_all_larger_dyadic_h_by_analytic_monotone_losses"])
                self.assertTrue(new["graph_constants_ACTUALLY_UNKNOWN_NOT_CERTIFIED"])
                self.assertEqual(new["conservative_sigma2_inverse"],64*65*65)
                self.assertEqual(new["conservative_sigma3_inverse"],64*27*65**3)

    def test_combined_gate_integer_root_upper_monotonic_across_actual_dyadic_orders(self):
        result=integrated_dense_closure(Fraction(5,4),Fraction(3,7))
        h=result["dyadic_h0_combined_exact_rational"]
        T=result["original_heavy_tail_T"]
        L6=result["conservative_L6"]
        E=result["exceptional_term_E"]
        D=result["internal_term_D"]
        for offset in (0,1,2,3,4,5,7,8,9,10,16,24,32):
            hh=h+offset
            ratios=(Fraction(84*T,2**hh),
                    E*_normalized_power_upper(hh,11,2),
                    D*_normalized_power_upper(hh,47,8))
            self.assertLessEqual(sum(ratios),Fraction(1,4))
        self.assertGreater(result["root_delta"],0)
        self.assertGreater(result["new_heavy_original_flag_fraction_beta"],
                           EPSILON**2/128)

    def test_test_only_unit_graph_constants_never_promote_published_unknown(self):
        r=integrated_dense_closure(1,1)
        self.assertEqual(r["hypothetical_C_graph"],1)
        self.assertEqual(r["hypothetical_c_graph"],1)
        self.assertTrue(r["graph_constants_ACTUALLY_UNKNOWN_NOT_CERTIFIED"])
        self.assertTrue(r["not_an_external_scientific_referee"])
        self.assertLessEqual(
            r["conditional_signed_GF5_R3_floor"],Fraction(54162)*r["root_delta"]/51**6)
        self.assertEqual(
            r["conditional_signed_GF5_R3_floor"],
            min(Fraction(54162)*r["root_delta"],Fraction(53526,8))/51**6)
        self.assertEqual(r["original_heavy_tail_T"],39352331442479)
        self.assertEqual(r["dyadic_h0_individually_budgeted"],697)
        self.assertEqual(r["dyadic_h0_combined_exact_rational"],685)
        self.assertEqual(integrated_dense_closure(1,1,prior_B0=True)[
            "dyadic_h0_combined_exact_rational"],693)
        self.assertLessEqual(
            sum(r["joint_certified_relative_losses_upper"]),Fraction(1,4))
        self.assertTrue(r["graph_constants_ACTUALLY_UNKNOWN_NOT_CERTIFIED"])

    def test_true_original_W32_full_independent_source_physical_mass_conservation(self):
        s,V,flags=genuine_source(1)
        f,g=maps(1,step=1)
        output=finite_true_original_path_partition(1,f,g)
        self.assertEqual(output["original_source_flags_full"],45)
        self.assertEqual(output["original_physical_edges"],90)
        self.assertEqual(output["proper_directed_W3"],1346)
        self.assertEqual(output["proper_good_unblocked"],4)
        self.assertEqual(output["original_BBo_sixset_count"],2)
        self.assertEqual(output["actual_directed_W3"],
                         output["independent_degree_product_W3"])
        self.assertTrue(output["all_seven_source_physical_accounting_classes_exact"])
        source_catalog=source_first_original_BBo_cubic_catalog(1,f,g)
        self.assertEqual(
            output["original_BBo_sixset_count"],
            source_catalog["aligned_original_BBo_sixset_count"])
        f,g=maps(1,step=-1,shift=V-1)
        second=finite_true_original_path_partition(1,f,g)
        self.assertEqual(second["proper_directed_W3"],1154)
        self.assertEqual(second["proper_good_unblocked"],0)

    def test_true_original_W32_sparse_core_and_FULL_source_anchors(self):
        _,V,flags=genuine_source(1)
        f,g=maps(1,step=1)
        for core in ((),(0,),tuple(range(0,45,2)),tuple(range(0,45,3))):
            with self.subTest(n=len(core)):
                z=finite_true_original_path_partition(1,f,g,core)
                self.assertEqual(z["original_physical_edges"],2*len(core))
                self.assertEqual(z["proper_good_unblocked"],
                                 2*z["original_BBo_sixset_count"])
                self.assertLessEqual(z["proper_good_unblocked"],
                                     z["proper_directed_W3"])
                self.assertEqual(
                    z["proper_directed_W3"]+z["improper_directed_W3"],
                    z["actual_directed_W3"])
                cat=source_first_original_BBo_cubic_catalog(1,f,g,core)
                self.assertEqual(z["original_BBo_sixset_count"],
                                 cat["aligned_original_BBo_sixset_count"])

    def test_true_original_W34_full_and_sparse_CORRELATED_geometry(self):
        _,V,flags=genuine_source(2)
        f,g=maps(2,step=19)
        for core in (None,tuple(range(0,425,3))):
            with self.subTest(core=None if core is None else len(core)):
                out=finite_true_original_path_partition(2,f,g,core)
                self.assertTrue(out["all_seven_source_physical_accounting_classes_exact"])
                self.assertEqual(out["proper_good_unblocked"],
                                 2*out["original_BBo_sixset_count"])
                self.assertEqual(out["original_physical_edges"],
                                 850 if core is None else 2*len(core))
                self.assertEqual(out["actual_directed_W3"],
                                 out["independent_degree_product_W3"])
                cat=source_first_original_BBo_cubic_catalog(2,f,g,core)
                self.assertEqual(out["original_BBo_sixset_count"],
                                 cat["aligned_original_BBo_sixset_count"])

    def test_true_original_W34_protected_K44_D6_not_assumed_BBo(self):
        f,g,ids=planted_original_k44()
        z=finite_true_original_path_partition(2,f,g,ids)
        self.assertEqual(z["original_physical_edges"],32)
        self.assertEqual(z["proper_good_unblocked"],2*z["original_BBo_sixset_count"])
        self.assertTrue(z["not_an_sge64_dense_branch_certificate"])

    def test_bad_external_placeholders_and_source_maps_fail_closed(self):
        for C,c in ((0,1),(-1,1),(True,1),(1.0,1),
                    ("1",1),(1,0),(1,Fraction(-1,2))):
            with self.assertRaises(ValueError):
                integrated_dense_closure(C,c)
        for s in (0,63,65,1.0,True,96):
            with self.assertRaises(ValueError):
                actual_source_budget(s)
        for power in (0,3,True):
            f,g=maps(1)
            with self.assertRaises(ValueError):
                finite_true_original_path_partition(power,f,g)
        f,g=maps(1)
        for badf,badg,core in ((f[:-1],g,None),((f[0],)*len(f),g,None),
                               (f,g,(0,0)),(f,g,(True,)),(f,g,(45,))):
            with self.assertRaises(ValueError):
                finite_true_original_path_partition(1,badf,badg,core)


if __name__=="__main__":
    unittest.main()
