"""AA4-SRGMIX genuine original point/line spectral and mixed-source red-team."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_original_source_srg_mixed_referee import (
    _source, _geometry, _original_conflicts, _point_books, _dualize,
    _physical_graph, _spectral_conflict, canonical_report, referee_case,
)


class TestOriginalSRGMixedReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_exact_original_SRG_point_and_line_collinearity_dimensions(self):
        for h in (1,2):
            case=_source(h,"lex")
            geo=_geometry(case)
            s,V,a=case["s"],case["V"],case["a"]
            self.assertEqual(V,(s+1)*(s*s+1))
            self.assertEqual(len(case["flags"]),V*(s+1))
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            for side in ("pt","ln"):
                self.assertTrue(all(len(n)==s*(s+1) for n in geo[side]))

    def test_SRG_spectral_collision_one_side_bound_for_adversarial_global_maps(self):
        for h,scheme,shf,shg in (
            (1,"lex",0,0),(1,"reverse-line",3,7),
            (2,"lex",0,0),(2,"reverse-line",11,23),
            (2,"lex",7,19),(2,"reverse-line",29,2)):
            with self.subTest(h=h,scheme=scheme,shift_f=shf,shift_g=shg):
                c=_source(h,scheme,shf,shg)
                geo=_geometry(c)
                conflicts,point,line=_original_conflicts(c,geo)
                Cs=(c["s"]**2+1)*(c["s"]**2+c["a"]-2)
                self.assertEqual(point["all_h_spectral_collinear_conflict_cap"],Cs)
                self.assertEqual(line["all_h_spectral_collinear_conflict_cap"],Cs)
                self.assertLessEqual(point["true_original_conflict_pairs"],Cs)
                self.assertLessEqual(line["true_original_conflict_pairs"],Cs)
                self.assertLessEqual(sum(map(len,conflicts))//2,2*Cs)
                self.assertEqual(point["signed_collinearity_G"],
                                 point["exact_original_G_from_SRG"])
                self.assertEqual(line["signed_collinearity_G"],
                                 line["exact_original_G_from_SRG"])

    def test_independent_exact_FULL_ALLOWED_CORE_contraction_even_when_anchors_outside(self):
        for z in self.report["genuine_complete_original_cases"]:
            with self.subTest(s=z["s"],scheme=z["scheme"],
                              shift_f=z["shift_f"],shift_g=z["shift_g"]):
                x=z["original_full_core_point_books"]
                y=z["original_full_core_LINE_dual_books"]
                self.assertTrue(all(x["checks"].values()))
                self.assertTrue(all(y["checks"].values()))
                self.assertGreaterEqual(x["Theta"],0)
                self.assertGreaterEqual(y["Theta"],0)
                self.assertEqual(z["core_physical_edges"],2*z["original_core_flags"])
                self.assertLessEqual(z["max_original_core_degree"],z["T"]*z["s"])

    def test_four_independent_true_GQ_original_blocker_positions(self):
        positive=0
        for z in self.report["genuine_complete_original_cases"]:
            b=z["physical_four_original_projection_blockers"]
            self.assertTrue(all(b["checks"].values()))
            self.assertEqual(len(b["four_separate_original_blocked_path_counts"]),4)
            self.assertGreaterEqual(b["physical_walks3"],b["proper_paths3"])
            self.assertGreaterEqual(b["proper_paths3"],
                                    b["true_original_projection_admissible_paths"])
            positive+=sum(b["four_separate_original_blocked_path_counts"])
        self.assertGreater(positive,0)

    def test_genuine_original_W34_mixed_heavy_retained_core_and_source_deletion(self):
        rows=[r for r in self.report["genuine_complete_original_cases"]
              if r["s"]==4]
        self.assertEqual(len(rows),5)
        self.assertTrue(any(r["full_original_heavy_touching_ids"]>0 for r in rows))
        self.assertTrue(any(r["original_core_flags"]>0 for r in rows))
        self.assertTrue(all(r["adversarial_deleted_original_ids"]>0 for r in rows))
        self.assertTrue(any(r["original_core_flags"]>0 and
                            r["physical_four_original_projection_blockers"]["proper_paths3"]>0
                            for r in rows))

    def test_actual_true_original_Z_mask_is_not_physical_owner_or_label_reassignment(self):
        c=_source(1,"lex",shift_f=2,shift_g=3)
        adj,owners=_physical_graph(c,range(len(c["flags"])))
        self.assertEqual(len(owners),2*len(c["flags"]))
        self.assertTrue(all(isinstance(i,int) for i in owners.values()))
        with self.assertRaises(ValueError):
            _physical_graph(c,[1,1])
        with self.assertRaises(ValueError):
            _physical_graph(c,[-1,0])
        with self.assertRaises(ValueError):
            referee_case(1,"lex",0,0,4,8,(45,))
        with self.assertRaises(ValueError):
            referee_case(1,"lex",0,0,4,0,())
        with self.assertRaises(ValueError):
            _source(3,"lex")
        with self.assertRaises(ValueError):
            _source(2,"lex",shift_f=1.5)

    def test_independent_historical_original_SRG_G_energy_TEST_ONLY(self):
        # Main referee intentionally imports no prior source energy code.
        # Use one historic independent implementation only in the TEST.
        from hyp105_original_lowtail_cap_closure import source_energy
        for h,scheme in ((1,"lex"),(1,"reverse-line"),
                         (2,"lex"),(2,"reverse-line")):
            c=_source(h,scheme)
            geo=_geometry(c)
            x=_spectral_conflict(c,geo,"point")
            y=_spectral_conflict(c,geo,"line")
            old_x=source_energy(c["s"],c["flags"],c["f"],c["a"])
            old_y=source_energy(c["s"],
                                tuple((ell,p) for p,ell in c["flags"]),
                                c["g"],c["a"])
            self.assertEqual(x["signed_collinearity_G"],old_x["G"])
            self.assertEqual(y["signed_collinearity_G"],old_y["G"])
            self.assertEqual(x["true_original_conflict_pairs"],
                             old_x["collinear_symbol_pairs"])
            self.assertEqual(y["true_original_conflict_pairs"],
                             old_y["collinear_symbol_pairs"])

    def test_SOURCE_book_cap_does_not_allow_uncapped_arbitrary_core(self):
        # An arbitrarily large valid ORIGINAL core is not entitled to
        # pretend K=0. The checker must fail its pointwise K cap.
        c=_source(2,"lex")
        geo=_geometry(c)
        C=tuple(range(len(c["flags"])))
        physical,_=_physical_graph(c,C)
        delta=max(map(len,physical.values()))
        with self.assertRaises(AssertionError):
            _point_books(c,geo,C,set(),delta,K=0)

    def test_true_line_duality_as_independent_source_geometry(self):
        c=_source(2,"reverse-line",11,23)
        geo=_geometry(c)
        dual,dgeo=_dualize(c,geo)
        d_spectral=_spectral_conflict(dual,dgeo,"point")
        original_line=_spectral_conflict(c,geo,"line")
        self.assertEqual(d_spectral["signed_collinearity_G"],
                         original_line["signed_collinearity_G"])
        self.assertEqual(d_spectral["true_original_conflict_pairs"],
                         original_line["true_original_conflict_pairs"])

    def test_complete_report_keeps_root_mathematical_stop(self):
        z=self.report
        self.assertEqual(z["schema"],"mathlab.hyp105.original-source-SRGMIX.v1")
        self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertTrue(z["original_all_order_SRG_bound_has_analytic_proof"])
        self.assertTrue(z["all_order_four_blocker_Cauchy_full_referee_pending"])
        self.assertFalse(z["root_universally_accepted"])
        self.assertEqual(len(z["genuine_complete_original_cases"]),7)
        self.assertTrue(all(v["all_referee_inequalities_valid"]
                            for v in z["genuine_complete_original_cases"]))


if __name__=="__main__":
    unittest.main()
