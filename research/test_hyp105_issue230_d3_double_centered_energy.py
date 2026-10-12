"""Independent exact ORIGINAL W(3,s) spectral/ANOVA checks for D3."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d3_double_centered_energy import (
    _pencil_motifs, double_centered_energy, report,
)
from hyp105_issue230_endpoint_mixedbook_d2 import _chord_ledger
from hyp105_issue230_projection import ProjectionClosure


def frac(v):
    return Fraction(v)


class Issue230D3DoubleCenteredTests(unittest.TestCase):
    def test_coherent_S68_exact_mean_and_center_partition(self):
        x=double_centered_energy(fixture(1,"S68"))
        self.assertEqual(x["physical_full_G_endpoint_energy_W"],3289)
        self.assertEqual(x["union_bad_original_pair_count"],166)
        self.assertEqual(x["left_bad_pair_count"],2*x["s"]*x["left_concurrent_physical_Mf"])
        self.assertEqual(x["right_bad_pair_count"],2*x["s"]*x["true_dual_concurrent_physical_Mg"])
        self.assertEqual(frac(x["W_mean"])+frac(x["W_centered_correlation"]),3289)
        self.assertLessEqual(frac(x["W_mean"]),frac(x["W_mean_cap_original_star"]))
        self.assertTrue(x["spectral_R_has_ZERO_row_column_sums"])
        self.assertTrue(x["exact_integer_double_centered_Cauchy"])
        self.assertFalse(x["uniform_new_10pct_exponent_gain_proved"])
        self.assertEqual(x["issue230_Branch_A"],"OPEN")

    def test_full_real_W32_all_named_maps(self):
        for scheme,w in (("lex",2977),("reverse",2709),("S68",3289),("S72",3303)):
            with self.subTest(scheme=scheme):
                state=fixture(1,scheme)
                x=double_centered_energy(state)
                self.assertEqual(x["physical_full_G_endpoint_energy_W"],w)
                self.assertEqual(frac(x["W_mean"])+frac(x["W_centered_correlation"]),w)
                self.assertEqual(frac(x["mean_original_weight_integer"]),
                                 frac(x["mean_physical_weight_integer"]))
                self.assertLessEqual(
                    frac(x["original_GQ_residual_R_Frobenius_squared"]),
                    8*x["s"]*(x["a"]-1)*x["V"])
                self.assertGreaterEqual(frac(x["centered_B_Frobenius_squared"]),0)

    def test_actual_W34_exact_F_I_L_expander_residual(self):
        for scheme,w in (("lex",133432),("random",115088)):
            with self.subTest(scheme=scheme):
                x=double_centered_energy(fixture(2,scheme))
                self.assertEqual(x["physical_full_G_endpoint_energy_W"],w)
                self.assertEqual(frac(x["W_mean"])+frac(x["W_centered_correlation"]),w)
                self.assertLessEqual(frac(x["Cauchy_ratio_squared"]),1)
                self.assertFalse(x["universal_internal_only_I_small_proved"])

    def test_true_real_W38_all_h_small_fixture(self):
        x=double_centered_energy(fixture(3,"random"))
        self.assertEqual(x["physical_full_G_endpoint_energy_W"],4927736)
        self.assertEqual(x["union_bad_original_pair_count"],70174)
        self.assertEqual(x["physical_full_G_endpoint_energy_W"],
                         frac(x["W_mean"])+frac(x["W_centered_correlation"]))
        self.assertTrue(x["all_h_exact_F_U_Ltranspose"])
        self.assertTrue(x["all_h_exact_F_IncGQ_Ltranspose"])
        self.assertFalse(x["universal_W_H_small_o_s59over10_proved"])

    def test_permute_both_physical_coordinate_alphabets_independently(self):
        state=fixture(1,"S68")
        baseline=double_centered_energy(state)
        aa=state["a"]
        left=list(range(aa));right=list(range(aa))
        left[0],left[2]=left[2],left[0]
        right[1],right[3]=right[3],right[1]
        transformed=dict(state)
        transformed["left_labels"]=[
            tuple(sorted(left[z] for z in p)) for p in state["left_labels"]]
        transformed["right_labels"]=[
            tuple(sorted(right[z] for z in p)) for p in state["right_labels"]]
        moved=double_centered_energy(transformed)
        keys=("physical_full_G_endpoint_energy_W",
              "union_bad_original_pair_count","W_mean",
              "W_centered_correlation","centered_B_Frobenius_squared",
              "original_GQ_residual_R_Frobenius_squared",
              "Cauchy_ratio_squared")
        for k in keys:
            self.assertEqual(baseline[k],moved[k],k)

    def test_all_h_original_pencil_Mf_Mg_independent_of_physical_grid(self):
        core=ProjectionClosure(fixture(2,"random"))
        mf,mg=_pencil_motifs(core)
        self.assertGreater(mf,0)
        self.assertGreater(mg,0)
        # Direct original concurrent ORIGINAL point pair count, independent
        # physical coordinate-pencil counter from D3.
        left_pairs=set()
        for points in core.lines:
            for q,p in comb_pairs(points):
                if set(core.f[q])&set(core.f[p]):
                    left_pairs.add((min(q,p),max(q,p)))
        right_pairs=set()
        for lines in core.point_lines:
            for l,r in comb_pairs(lines):
                if set(core.g[l])&set(core.g[r]):
                    right_pairs.add((min(l,r),max(l,r)))
        self.assertEqual(mf,len(left_pairs))
        self.assertEqual(mg,len(right_pairs))

    def test_all_report_records_reject_full_root_A_claim(self):
        r=report()
        self.assertEqual(r["slice"],"ISSUE230-D3-DOUBLE-CENTERED-ORIGINAL-GQ-ENERGY")
        self.assertEqual(len(r["records"]),7)
        self.assertEqual(r["uniform_W_upper_o_s59over10"],"OPEN")
        for x in r["records"]:
            self.assertFalse(x["universal_endpoint_blocking_E_small_proved"])
            self.assertEqual(frac(x["W_mean"])+frac(x["W_centered_correlation"]),
                             x["physical_full_G_endpoint_energy_W"])
            self.assertTrue(x["exact_integer_double_centered_Cauchy"])
            self.assertTrue(x["spectral_R_has_ZERO_row_column_sums"])
            self.assertTrue(x["double_centered_original_bad_relation_ZERO_row_column_sums"])


def comb_pairs(items):
    from itertools import combinations
    return combinations(sorted(items),2)


if __name__=="__main__":
    unittest.main()
