"""Independent ORIGINAL incidence and physical-path falsifiers for EICE-002."""
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_paired_gstar import (
    all_h_certificate, paired_gstar, _conditional_cut, _paired_peel,
    verify_paired_regularizer, PEEL_DELTA
)
from hyp105_issue230_projection import fixture


class PairedGStarTests(unittest.TestCase):
    def test_all_h_exact_analytic_constants_and_strict_domain(self):
        for s in (64,128,256,512,1024,2048):
            row=all_h_certificate(s)
            self.assertLessEqual(2*Fraction(row['spectral_ratio']),3)
            self.assertGreater(Fraction(row['paired_edges_after_peeling_lower']),
                               Fraction(s**4,40000))
            self.assertEqual(row['degree_factor'],'1/1000000')
            self.assertFalse(row['universal_s_lower_proved'])
        for s in (2,4,8,16,32,48,63,0):
            with self.assertRaises(ValueError):
                all_h_certificate(s)

    def test_four_complete_true_W32_global_maps(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                out=paired_gstar(model,verify_paths=True)
                self.assertFalse(out['universal_S_lower_proved'])
                self.assertFalse(out['uniform_theorem_applicable'])
                self.assertTrue(out['graph']['both_diagonals'])
                self.assertEqual(out['graph']['physical_edges'],
                                 2*out['final_original_count'])
                self.assertGreaterEqual(out['stage1_original_count'],
                                        out['stage2_original_count'])
                self.assertGreaterEqual(out['stage2_original_count'],
                                        out['stage3_left_color_count'])
                self.assertGreaterEqual(out['stage3_left_color_count'],
                                        out['stage4_both_colors_count'])
                self.assertGreaterEqual(out['stage4_both_colors_count'],
                                        out['final_original_count'])
                self.assertGreaterEqual(2*out['stage3_left_color_count'],
                                        out['stage2_original_count'])
                self.assertGreaterEqual(2*out['stage4_both_colors_count'],
                                        out['stage3_left_color_count'])
                self.assertEqual(out['final_original_count'],
                                 len(set(out['original_incidence_ids'])))

    def test_real_W34_global_maps_and_original_provenance(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                out=paired_gstar(model,verify_paths=True)
                self.assertTrue(out['graph']['both_diagonals'])
                self.assertEqual(out['graph']['physical_edges'],
                                 2*out['final_original_count'])
                self.assertGreater(out['stage4_both_colors_count'],0)

    def test_paired_peel_removes_both_diagonals_and_can_be_empty(self):
        model=fixture(1,'lex')
        ctx=EndpointEnergy(model)
        ids=(0,)
        kept,iterations=_paired_peel(ids,ctx.inc,ctx.f,ctx.g,ctx.a,2)
        self.assertEqual(kept,())
        self.assertGreaterEqual(iterations,1)
        kept2,iterations2=_paired_peel(ids,ctx.inc,ctx.f,ctx.g,ctx.a,1)
        self.assertEqual(kept2,(0,))
        self.assertEqual(iterations2,0)

    def test_arbitrary_bichromatic_subsets_fail_closed_if_cherry(self):
        model=fixture(1,'lex')
        out=paired_gstar(model)
        colorsL=out['colors_left']
        colorsR=out['colors_right']
        ids=out['original_incidence_ids']
        verify_paired_regularizer(model,ids,colorsL,colorsR,require_paths=True)
        with self.assertRaisesRegex(AssertionError,'unbichromatic'):
            verify_paired_regularizer(model,ids,[0]*model['a'],colorsR)
        with self.assertRaisesRegex(ValueError,'min_degree'):
            paired_gstar(model,min_degree=-1)
        with self.assertRaisesRegex(ValueError,'path proof budget'):
            verify_paired_regularizer(model,ids,colorsL,colorsR,
                                     require_paths=True,walk_budget=0)

    def test_independent_source_pencil_cherry_validator(self):
        model=fixture(1,'lex')
        ctx=EndpointEnergy(model)
        two_point_neighbors=None
        for p in range(ctx.v):
            candidate=[i for i,(q,l) in enumerate(ctx.inc) if q==p]
            for i,j in combinations(candidate,2):
                if set(ctx.g[ctx.inc[i][1]]) & set(ctx.g[ctx.inc[j][1]]):
                    two_point_neighbors=(i,j)
                    break
            if two_point_neighbors:
                break
        self.assertIsNotNone(two_point_neighbors)
        result=paired_gstar(model)
        with self.assertRaises(AssertionError):
            verify_paired_regularizer(model,two_point_neighbors,
                                     result['colors_left'],result['colors_right'])

    def test_no_fake_finite_asymptotic_s_2_4_8(self):
        for s in (2,4,8):
            self.assertLess(Fraction(s,1_000_000),1)
        # A finite model cannot certify dmin >=2 from delta*s.
        self.assertLess(PEEL_DELTA*8,2)


if __name__ == '__main__':
    unittest.main()
