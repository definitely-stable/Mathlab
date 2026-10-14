"""EICE-003-D: independent original middle-edge rectangle versus NB3 path oracles."""
from fractions import Fraction
from math import isclose, log
import unittest

from hyp105_issue230_anchor_lift import AnchorLiftedEnergy
from hyp105_issue230_nb_rectangles import (
    OriginalNBRectangle, rectangle_entropy_ceiling, report
)
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture


class OriginalRectangleTests(unittest.TestCase):
    def real_coherent(self,s,scheme):
        model=fixture(s.bit_length()-1,scheme)
        reg=paired_gstar(model,verify_paths=True)
        return model,reg,OriginalNBRectangle(
            model,reg['original_incidence_ids'],
            reg['colors_left'],reg['colors_right'])

    def test_W32_four_true_source_rectangles_and_independent_path_oracle(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model,reg,oracle=self.real_coherent(2,scheme)
                row=oracle.census(independent_oracle=True)
                prior=AnchorLiftedEnergy(model,selected=reg['original_incidence_ids']).census(
                    require_proper=True)
                self.assertEqual(Fraction(row['theta_internal_only']),
                                 Fraction(prior['theta_internal_only']))
                self.assertEqual(row['oriented_middle_rectangles'],
                                 4*len(reg['original_incidence_ids']))
                self.assertEqual(row['physical_edges'],
                                 2*len(reg['original_incidence_ids']))
                self.assertLessEqual(row['max_original_r_per_middle_source_q'],4)
                self.assertLessEqual(row['max_original_q_per_middle_source_r'],4)
                self.assertTrue(row['four_partial_matchings_verified'])
                self.assertFalse(row['universal_branch_A_proved'])

    def test_W34_complete_original_source_labels_and_cuts(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model,reg,oracle=self.real_coherent(4,scheme)
                try:
                    row=oracle.census(max_paths=2_000_000,independent_oracle=True)
                except ValueError as exc:
                    self.assertIn('no valid physical nonbacktracking rectangles',str(exc))
                    continue
                self.assertEqual(row['N'],425)
                self.assertEqual(row['oriented_middle_rectangles'],
                                 4*reg['final_original_count'])
                self.assertLessEqual(row['max_original_q_per_middle_source_r'],4)
                self.assertGreaterEqual(Fraction(row['eligible_end_clean_mass']),0)

    def test_true_source_one_orientation_at_most_one_original_q_and_r(self):
        model,reg,oracle=self.real_coherent(2,'reverse')
        row=oracle.census()
        self.assertTrue(row['four_partial_matchings_verified'])
        self.assertGreater(row['oriented_nonbacktracking_paths'],0)
        self.assertLessEqual(row['nonzero_true_transport_cells'],
                             row['oriented_nonbacktracking_paths'])
        self.assertLessEqual(row['max_original_r_per_middle_source_q'],4)
        self.assertLessEqual(row['max_original_q_per_middle_source_r'],4)

    def test_wrong_colors_and_full_graph_cherries_fail_closed(self):
        model,reg,oracle=self.real_coherent(2,'lex')
        colors=list(reg['colors_left'])
        colors[:]=[0]*len(colors)
        with self.assertRaisesRegex(ValueError,'bichromatic'):
            OriginalNBRectangle(model,reg['original_incidence_ids'],
                                colors,reg['colors_right'])
        with self.assertRaisesRegex(ValueError,'cherry|bichromatic'):
            OriginalNBRectangle(model,list(range(45)),
                                reg['colors_left'],reg['colors_right'])
        with self.assertRaisesRegex(ValueError,'complete fixed binary'):
            OriginalNBRectangle(model,reg['original_incidence_ids'],
                                [0],reg['colors_right'])

    def test_original_source_registry_fails_closed(self):
        model,reg,oracle=self.real_coherent(2,'lex')
        bad=fixture(1,'lex')
        bad['right_labels']=list(bad['right_labels'])
        bad['right_labels'][0]=bad['right_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            OriginalNBRectangle(bad,reg['original_incidence_ids'],
                                reg['colors_left'],reg['colors_right'])
        with self.assertRaisesRegex(ValueError,'rectangle budget'):
            oracle.census(max_paths=0)
        with self.assertRaisesRegex(ValueError,'rectangle budget'):
            oracle.census(max_paths=1)

    def test_stationary_rectangle_atom_bound_and_nonstationary_scope(self):
        for scheme in ('lex','reverse','S68','S72'):
            model,reg,oracle=self.real_coherent(2,scheme)
            row=oracle.census()
            if row['stationary']:
                d=row['minimum_positive_physical_degree']
                M=row['source_middle_ids']
                self.assertEqual(Fraction(row['raw_rectangle_law_mass']),
                                 4*M)
                self.assertEqual(Fraction(row['D3_stationary_atom_cap']),
                                 Fraction(1,M*(d-1)**2))
                self.assertIsNotNone(row['D4_info_upper_nats_diagnostic'])
                self.assertLessEqual(row['D4_info_nats_diagnostic'],
                                     row['D4_info_upper_nats_diagnostic']+1e-9)
            else:
                self.assertTrue(row['conditional_on_survival'])
                self.assertIsNone(row['D3_stationary_atom_cap'])
                self.assertIsNone(row['D4_info_nats_diagnostic'])

    def test_D4_information_ceiling_analytic_scaling(self):
        # A hypothetical dense G* with dmin~delta*s yields
        # I<= (4+o(1))log s (whereas C6 asks for >=1.5log s).
        # This algebra is not an actual all-h physically attained graph.
        for s in (2**24,2**28,2**32):
            degree=s//1_000_000
            V=(s+1)*(s*s+1)
            C=V*V
            upper=rectangle_entropy_ceiling(1.0,C,degree)
            self.assertGreater(upper,0)
            ratio=upper/log(s)
            self.assertGreater(ratio,3.9)
            self.assertLess(ratio,8.0)
        self.assertEqual(rectangle_entropy_ceiling(0,0,2),0)
        self.assertEqual(rectangle_entropy_ceiling(1,4,3),0)
        with self.assertRaisesRegex(ValueError,'invalid stationary'):
            rectangle_entropy_ceiling(1,4,1)
        with self.assertRaisesRegex(ValueError,'positive eligible'):
            rectangle_entropy_ceiling(1,0,2)

    def test_report_restricted_and_original_source_only(self):
        rows=report()
        self.assertEqual(rows['status'],'RESTRICTED_THEOREM_C')
        self.assertEqual(rows['root_A'],'OPEN')
        self.assertEqual(len(rows['rows']),4)
        self.assertTrue(all(('scope' not in r or 'original' not in r['scope'])
                            for r in rows['rows']))


if __name__=='__main__':
    unittest.main()
