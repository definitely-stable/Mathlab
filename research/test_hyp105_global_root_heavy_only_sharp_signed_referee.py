"""Exact arithmetic adversarial regressions for the independently derived root gate."""
from fractions import Fraction
import unittest
from hyp105_global_root_heavy_only_sharp_signed_referee import (
    EPSILON,ANALYTIC_CORE_BUDGET,ETA_STAR,SHARP_D6,
    SHARP_PRODUCED_BBO,GF5_PALETTE_SIX,source_heavy_beta,
    original_source_budget,_gate_inputs,relative_dense_loss_upper,
    whole_root_certificate,finite_h_full_root_lower,
    _dyadic_fractional_inverse_upper,_ceil_kroot,_rational_positive,
)
from hyp105_original_selector_sixwalk_joint_root_gate import selector_moment_root_gate

class IndependentOriginalRootLedger(unittest.TestCase):
    def test_true_original_all_h_book_budget(self):
        self.assertLess(EPSILON,ANALYTIC_CORE_BUDGET)
        self.assertGreater(source_heavy_beta(),EPSILON**2/128)
        for h in range(6,26):
            r=original_source_budget(h)
            s=r["s"];v=r["V"];a=r["a_minimal"]
            self.assertLess((a-1)*(a-2)//2,v)
            self.assertGreaterEqual(a*(a-1)//2,v)
            self.assertGreater(r["true_source_retention_budget"],EPSILON)
            self.assertGreater(2*(Fraction(r["N_original_flags"],s**4)
                 -EPSILON-Fraction(r["Cs_original_pencil_book_bound"],16*s**4)),1)

    def test_new_exact_heavy_only_threshold(self):
        self.assertEqual(ETA_STAR,Fraction(991,7976))
        self.assertEqual(SHARP_PRODUCED_BBO*(Fraction(1,4)-ETA_STAR),
                         Fraction(SHARP_D6,8))
        self.assertLess(Fraction(SHARP_PRODUCED_BBO,8),Fraction(SHARP_D6,8))
        self.assertGreater(Fraction(SHARP_PRODUCED_BBO,4),Fraction(SHARP_D6,8))
        self.assertEqual(GF5_PALETTE_SIX,51**6)

    def test_exact_hypothetical_graph_inputs_cross_independent_old_gate(self):
        for C,c in ((1,1),(Fraction(3,2),Fraction(5,7)),
                    (2,Fraction(1,10))):
            a=_gate_inputs(C,c)
            b=selector_moment_root_gate(C,c)
            for name,oldname in (
                ("T","T"),("delta","delta"),("beta","beta"),
                ("sixwalk_bound_L6","L6"),
                ("fourwalk_bound_L4_integer_upper","L4_integer_upper"),
                ("exceptional_E_integer_upper","exceptional_E_integer_upper"),
                ("four_internal_D_integer_upper","internal_D_integer_upper")):
                self.assertEqual(a[name],b[oldname],(name,C,c))

    def test_heavy_only_signed_lower_valid_every_larger_h(self):
        for C,c in ((1,1),(Fraction(3,2),Fraction(5,7)),
                    (2,Fraction(1,10))):
            p=whole_root_certificate(C,c)
            h=p["new_heavy_only_sufficient_h"]
            self.assertGreaterEqual(h,p["old_dense_one_eighth_sufficient_h"])
            self.assertLessEqual(sum(p["exact_relative_loss_upper_at_h"]),ETA_STAR)
            self.assertTrue(p["external_graph_constants_numeric_are_UNKNOWN"])
            self.assertEqual(p["scientific_acceptance"],"OPEN_WITH_FORMAL_BLOCKER")
            self.assertEqual(p["sharp_full_root_R3_coefficient"],
                             Fraction(SHARP_D6,GF5_PALETTE_SIX)*p["delta"])
            for j in (h,h+1,h+2,h+8,h+32):
                q=finite_h_full_root_lower(j,C,c)
                self.assertLessEqual(sum(q["loss_terms_exact_upper"]),ETA_STAR)
                self.assertEqual(q["full_original_signed_R3_relative_lower"],
                                 p["sharp_full_root_R3_coefficient"])

    def test_finite_h_clip_nonnegative_and_no_claim_under_gate(self):
        p=whole_root_certificate(1,1)
        low=finite_h_full_root_lower(6,1,1)
        self.assertTrue(low["zero_floor_is_allowed_for_finite_h_below_symbolic_h0"])
        self.assertEqual(low["full_original_signed_R3_relative_lower"],0)
        self.assertGreaterEqual(finite_h_full_root_lower(
            p["new_heavy_only_sufficient_h"],1,1)
            ["full_original_signed_R3_relative_lower"],0)

    def test_independent_exact_irrational_root_enclosure(self):
        for k in (2,8):
            for h in range(33):
                q=_dyadic_fractional_inverse_upper(h,k)
                self.assertGreaterEqual(q**k,Fraction(1,2**h))
                self.assertLess(q**k,Fraction(9,8)*Fraction(1,2**h))
        for x,k in ((0,2),(1,2),(17,8),(256,8),(65537,8)):
            y=_ceil_kroot(x,k)
            self.assertGreaterEqual(y**k,x)
            if y:self.assertLess((y-1)**k,x)

    def test_true_W32_W34_original_sixID_heavy_and_dense_GF5_sources(self):
        # Independently recombine BOTH true original six-source-ID classes:
        # historical D6 matching flag lift and #708 genuine aligned BBo.
        # The actual finite geometry is not manufactured from a template.
        from hyp105_gf5_original_sixid_flow_referee import (
            planted_original_d6, original_projected_column_edges,
        )
        from hyp105_original_aligned_bbo_gf5_fourier_referee import (
            aligned_template_types, lift_template,
            source_coordinate_edges, count_actual_physical_owner_paths,
            gf5_fourier_potential_oracle, SIGNS,
        )
        typ=next(t for t in aligned_template_types() if t["aligned"])
        for power in (1,2):
            with self.subTest(power=power):
                d=planted_original_d6(power)
                ids=d["ids"];flags=d["flags"]
                self.assertEqual(len({flags[i][0] for i in ids}),6)
                self.assertEqual(len({flags[i][1] for i in ids}),6)
                edges=original_projected_column_edges(
                    flags,ids,d["f"],d["g"])
                self.assertEqual(
                    sum(gf5_fourier_potential_oracle(edges,s) for s in SIGNS),
                    SHARP_D6)
                _s,_v,ff,bbids,f,g=lift_template(power,typ)
                self.assertEqual(len({ff[i][0] for i in bbids}),5)
                self.assertEqual(len({ff[i][1] for i in bbids}),5)
                self.assertEqual(
                    count_actual_physical_owner_paths(ff,bbids,f,g),2)
                e=source_coordinate_edges(ff,bbids,f,g)
                self.assertEqual(
                    sum(gf5_fourier_potential_oracle(e,s) for s in SIGNS),
                    SHARP_PRODUCED_BBO)
                self.assertTrue(set(bbids[:3]).isdisjoint(bbids[3:]))

    def test_frozen_hypothetical_h0_regression_is_explicitly_not_published(self):
        # C=c=1 are ILLUSTRATIVE exact arithmetic inputs only.
        r=whole_root_certificate(1,1)
        self.assertEqual(r["old_dense_one_eighth_sufficient_h"],666)
        self.assertEqual(r["new_heavy_only_sufficient_h"],667)
        self.assertTrue(r["external_graph_constants_numeric_are_UNKNOWN"])

    def test_inputs_not_guessed_published_constants(self):
        for bad in (0,-1,True,1.0,None,"1"):
            with self.assertRaises(ValueError):_rational_positive(bad)
            with self.assertRaises(ValueError):whole_root_certificate(bad,1)
            with self.assertRaises(ValueError):whole_root_certificate(1,bad)
        for bad in (0,1,5,False,6.0):
            with self.assertRaises(ValueError):original_source_budget(bad)

if __name__=="__main__":
    unittest.main()
