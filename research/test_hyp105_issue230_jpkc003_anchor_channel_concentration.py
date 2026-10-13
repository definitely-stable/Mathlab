"""Independent exact ORIGINAL anchor channel and source-capacity acceptance tests."""
from fractions import Fraction
import unittest

from hyp105_issue230_jpkc003_anchor_channel_concentration import (
    _cut, _occupied_image_cut, anchor_concentration_certificate, report,
)
from hyp105_issue230_projection import fixture, ProjectionClosure


class JPKC003Tests(unittest.TestCase):
    def test_all_four_true_W32_source_anchor_channels(self):
        known={
            "lex":(942,1872),
            "reverse":(898,1432),
            "S68":(606,512),
            "S72":(658,664),
        }
        for scheme,(B,K) in known.items():
            with self.subTest(scheme=scheme):
                c=anchor_concentration_certificate(
                    fixture(1,scheme),compare_pair_ledger=True,
                    include_anchor_rows=True)
                self.assertEqual((c["J6_total_blocked_paths"],
                                  c["J6_total_ordered_blocked_collisions"]),(B,K))
                self.assertTrue(c["J6_exact_identity_verified"])
                self.assertTrue(c["J7_region_separation_no_mixed_anchor_pairs"])
                self.assertTrue(c["independent_JPKC002_fully_reconciled"])
                self.assertEqual(c["original_nonincident_anchors"],180)
                self.assertEqual(c["J7_endpoint_E"]+c["J7_internal_only_I"],B)
                self.assertEqual(c["J7_endpoint_region_collisions"]+
                                 c["J7_internal_region_collisions"],K)
                rows=c["original_anchor_channels"]
                self.assertEqual(len(rows),180)
                self.assertEqual(sum(row["blocked_paths"] for row in rows),B)
                self.assertEqual(sum(row["blocked_collisions"] for row in rows),K)
                for row in rows:
                    d0,d1=row["diagonal_0_paths"],row["diagonal_1_paths"]
                    self.assertEqual(row["blocked_paths"],2*(d0+d1))
                    self.assertEqual(row["blocked_collisions"],
                                     2*(d0*(d0-1)+d1*(d1-1)))
                lhs=Fraction(K)
                rhs=(Fraction(B*B,4*180)-B+
                     Fraction(c["J6_anchor_variance_exact"])+
                     c["J6_diagonal_imbalance_energy"])
                self.assertEqual(lhs,rhs)
                self.assertGreaterEqual(Fraction(c["J6_anchor_variance_exact"]),0)
                self.assertGreaterEqual(c["J6_diagonal_imbalance_energy"],0)
                self.assertGreaterEqual(K,Fraction(c["J7_combined_anchor_CS_lower_exact"]))
                self.assertEqual(c["occupied_point_image"]["missing_physical_edges"],0)

    def test_true_original_W34_geometry_lex_random_and_source_caps(self):
        for scheme,B,K in (("lex",55384,161256),("random",48542,117356)):
            with self.subTest(scheme=scheme):
                c=anchor_concentration_certificate(fixture(2,scheme),
                                                   compare_pair_ledger=True)
                self.assertEqual((c["J6_total_blocked_paths"],
                                  c["J6_total_ordered_blocked_collisions"]),(B,K))
                self.assertEqual(c["original_nonincident_anchors"],6800)
                self.assertLessEqual(c["endpoint_bad_union_original_anchors"],
                                     2*4*(c["M_f_original_collinear"]+
                                          c["M_g_original_concurrent"]))
                self.assertEqual(c["endpoint_bad_left_original_anchors"],
                                 8*c["M_f_original_collinear"])
                self.assertEqual(c["endpoint_bad_right_original_anchors"],
                                 8*c["M_g_original_concurrent"])
                self.assertEqual(c["occupied_point_image"]["missing_physical_edges"],6)
                self.assertEqual(c["occupied_point_image"]["sharp_Ahlswede_Katona_upper"],963)
                self.assertEqual(c["occupied_line_image"]["sharp_Ahlswede_Katona_upper"],963)

    def test_D4_real_original_spread_W34_full_anchor_ledger(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        m,cert=spread_adversary_model(2)
        c=anchor_concentration_certificate(m,compare_pair_ledger=True)
        self.assertEqual(cert["M_f_original_exact"],259)
        self.assertEqual(c["M_f_original_collinear"],259)
        self.assertEqual(c["J6_total_blocked_paths"],52760)
        self.assertEqual(c["J6_total_ordered_blocked_collisions"],149716)
        self.assertEqual(c["J7_endpoint_region_collisions"]+
                         c["J7_internal_region_collisions"],149716)

    def test_occupied_image_cut_exact_and_global_marginal_limit(self):
        for scheme in ("lex","reverse","S68"):
            m=fixture(1,scheme)
            ctx=ProjectionClosure(m)
            for labels in (ctx.f,ctx.g):
                c=_occupied_image_cut(labels,ctx.a)
                self.assertEqual(c["sharp_Ahlswede_Katona_upper"],
                                 c["observed"])
        ctx=ProjectionClosure(fixture(2,"random"))
        for labels in (ctx.f,ctx.g):
            c=_occupied_image_cut(labels,ctx.a)
            # Direct O(V^2) physical pair adjacency definition, independent
            # of the degree-binom formula and of D6-Y implementation.
            count=sum(bool(set(u)&set(v))
                      for u,v in __import__("itertools").combinations(labels,2))
            self.assertEqual(c["observed"],count)
            self.assertLessEqual(c["observed"],
                                 c["sharp_Ahlswede_Katona_upper"])

    def test_fail_closed_source_models_and_scopes(self):
        with self.assertRaises(AssertionError):
            _cut(1,0)
        self.assertEqual(_cut(0,0),0)
        with self.assertRaises(ValueError):
            _occupied_image_cut(((0,1),)*16,6)
        m=fixture(1,"lex")
        labels=list(m["right_labels"])
        labels[2]=labels[0]
        m["right_labels"]=tuple(labels)
        with self.assertRaises(ValueError):
            anchor_concentration_certificate(m)
        with self.assertRaisesRegex(ValueError,"path budget"):
            anchor_concentration_certificate(fixture(1,"lex"),max_paths=1)

    def test_summary_does_not_claim_root_proof(self):
        r=report()
        self.assertEqual(len(r["records"]),6)
        self.assertFalse(r["root_universal_S_omega_s6_PROVED_A"])
        self.assertTrue(r["all_h_J6_J7_exact"])


if __name__=="__main__":
    unittest.main()
